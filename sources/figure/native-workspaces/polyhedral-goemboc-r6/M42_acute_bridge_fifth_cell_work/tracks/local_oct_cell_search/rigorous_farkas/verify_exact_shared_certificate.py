#!/usr/bin/env python3
"""Independent exact verifier for row54_shared_exact.json."""
from __future__ import annotations

import argparse
import csv
import json
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import rational_shared_certificate as model  # noqa: E402

PROJECT = model.TRACK.parents[2]
ATLAS = PROJECT / "tracks" / "circuit_atlas"
sys.path.insert(0, str(ATLAS))
import materialize_row54_cells as materializer  # noqa: E402
import row54_four_residual_search as carrier  # noqa: E402


def parse_fraction(item: dict) -> F:
    return F(int(item["numerator"]), int(item["denominator"]))


def parse_matrix(items: list[list[dict]]) -> list[list[F]]:
    return [[parse_fraction(x) for x in row] for row in items]


def load_float_points(path: Path) -> tuple[list[int], np.ndarray]:
    rows = {}
    with path.open() as f:
        for row in csv.DictReader(f):
            rows[int(row["source_id"])] = np.array(
                [float(row[k]) for k in ("x", "y", "z")], dtype=float
            )
    ids = sorted(rows)
    return ids, np.array([rows[row] for row in ids])


def fresh_hull_audit(csv_path: Path, faces_path: Path) -> dict:
    ids, points = load_float_points(csv_path)
    hull, faces, _ = carrier.group_maximal_faces(ids, points)
    mechanics, stable, unstable, saddles = carrier.classify(ids, points, faces)
    expected = {frozenset(face) for face in json.load(faces_path.open())}
    rebuilt = {frozenset(face) for face in faces}
    missing = sorted(materializer.forced_rail_edges() - set(mechanics["ef"]))
    return {
        "faces_match": expected == rebuilt,
        "f_vector": [len(hull.vertices), len(mechanics["ef"]), len(faces)],
        "all_rows_active": len(hull.vertices) == len(ids) and mechanics["active"] == ids,
        "class": [len(stable), len(unstable), len(saddles)],
        "stable_faces": stable,
        "unstable_vertices": unstable,
        "saddle_edges": saddles,
        "missing_forced_rails": [list(edge) for edge in missing],
    }


def reconstruct_problem():
    p = model.rational_chart_points()
    centroid = model.own_centroid(p)
    normals = model.face_normals(p)
    stable_face = next(i for i, face in enumerate(model.FACES)
                       if frozenset(face) == frozenset((7, 8, 246)))
    targets = [
        ("S[7,8,246]-death",
         -model.stable_primitives(stable_face, p, centroid, normals)[1]),
        ("U54-death", -model.vertex_primitive(54, 1, p, centroid)),
        ("H67-death", -model.edge_primitives((6, 7), p, centroid, normals)[0]),
        ("H910-death", -model.edge_primitives((9, 10), p, centroid, normals)[1]),
    ]
    selected = [
        targets[1], targets[2],
        ("topology:f15:row8", model.topology_primitive(15, 8, p, normals)),
        ("antiedge:263-264:c3",
         -model.edge_primitives((263, 264), p, centroid, normals)[3]),
    ]
    jt = [list(item.grad) for _, item in targets]
    gram = model.matmul(jt, model.mat_transpose(jt))
    four = model.matmul(model.mat_transpose(jt), model.inverse(gram))
    shared = [[row[0], row[1], row[2] + row[3]] for row in four]
    values = [item.value for _, item in selected]
    jac = [list(item.grad) for _, item in selected]
    a = [[-x for x in row] for row in model.matmul(jac, shared)]
    epsilon = F(1, 1_000_000)
    b = [value - need for value, need in zip(values, (epsilon, epsilon, F(0), F(0)))]
    return [name for name, _ in selected], values, a, b


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--certificate", type=Path,
                    default=HERE / "row54_shared_exact.json")
    ap.add_argument("--output", type=Path,
                    default=HERE / "row54_shared_exact_audit.json")
    args = ap.parse_args()

    certificate = json.load(args.certificate.open())
    names, values, rebuilt_a, rebuilt_b = reconstruct_problem()
    stored_values = [parse_fraction(x) for x in certificate["selected_values"]]
    stored_a = parse_matrix(certificate["A"])
    stored_b = [parse_fraction(x) for x in certificate["b"]]
    y = [parse_fraction(x) for x in certificate["dual_y"]]

    residual = [sum((stored_a[i][j] * y[i] for i in range(len(y))), F(0))
                for j in range(len(stored_a[0]))]
    b_dot_y = sum((x * weight for x, weight in zip(stored_b, y)), F(0))
    hashes = {
        path.name: model.sha256(path) for path in (
            model.SOURCE, model.FACES_SOURCE,
            model.ACTUAL_ENDPOINT, model.ACTUAL_ENDPOINT_FACES,
        )
    }
    fixed_hull = fresh_hull_audit(model.SOURCE, model.FACES_SOURCE)
    actual_hull = fresh_hull_audit(model.ACTUAL_ENDPOINT, model.ACTUAL_ENDPOINT_FACES)

    checks = {
        "artifact_hashes_match": hashes == certificate["frozen_artifacts"],
        "selected_names_match": names == certificate["selected_names"],
        "primitive_values_match": values == stored_values,
        "matrix_A_matches_exact_AD": rebuilt_a == stored_a,
        "vector_b_matches_exact_AD": rebuilt_b == stored_b,
        "dual_nonnegative": all(weight >= 0 for weight in y),
        "dual_normalized": sum(y, F(0)) == 1,
        "A_transpose_y_exact_zero": all(x == 0 for x in residual),
        "b_dot_y_strictly_negative": b_dot_y < 0,
        "fixed_faces_fresh": fixed_hull["faces_match"],
        "actual_faces_fresh": actual_hull["faces_match"],
        "fixed_rails_present": not fixed_hull["missing_forced_rails"],
        "actual_rails_present": not actual_hull["missing_forced_rails"],
    }
    assert all(checks.values()), {name: value for name, value in checks.items() if not value}

    out = {
        "status": "PASS",
        "logical_contradiction": (
            "If A*x <= b, then y>=0 gives (A^T*y).x <= b^T*y. "
            "The left side is exactly 0 and the right side is strictly negative."
        ),
        "checks": checks,
        "dual_y_decimal": [float(x) for x in y],
        "A_transpose_y": [str(x) for x in residual],
        "b_dot_y": {
            "numerator": str(b_dot_y.numerator),
            "denominator": str(b_dot_y.denominator),
            "decimal": float(b_dot_y),
        },
        "fixed_cell_fresh_hull": fixed_hull,
        "actual_endpoint_fresh_hull": actual_hull,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
