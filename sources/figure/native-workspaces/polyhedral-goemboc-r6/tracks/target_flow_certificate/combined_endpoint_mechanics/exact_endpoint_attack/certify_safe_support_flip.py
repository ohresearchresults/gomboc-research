#!/usr/bin/env python3
"""Certify one rail-preserving support flip between two resolved checkpoints."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
ROOT = HERE.parents[3]
sys.path[:0] = [str(PARENT), str(HERE)]

import build_u54_material_exact_path as source  # noqa: E402
import certify_mandatory_rail_bypass as bypass  # noqa: E402
import certify_post_bypass_chain as chain  # noqa: E402


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def parse_circuit(text):
    circuit = tuple(int(value) for value in text.split(","))
    if len(circuit) != 4 or len(set(circuit)) != 4:
        raise ValueError(("circuit must contain four distinct labels", circuit))
    return circuit


def locate_bracket(polynomial, subdivisions=4096):
    changes = []
    previous_t = Q(0)
    previous_value = polynomial.eval(previous_t)
    if not previous_value:
        raise AssertionError("event already occurs at source")
    for index in range(1, subdivisions + 1):
        parameter = Q(index, subdivisions)
        value = polynomial.eval(parameter)
        if not value:
            left = Q(index - 1, subdivisions)
            right = Q(min(index + 1, subdivisions), subdivisions)
            changes.append((left, right))
        elif (value > 0) != (previous_value > 0):
            changes.append((previous_t, parameter))
        previous_t, previous_value = parameter, value
    unique = []
    for bracket in changes:
        if not unique or bracket != unique[-1]:
            unique.append(bracket)
    if len(unique) != 1:
        raise AssertionError(("expected one isolated sign change", unique))
    return unique[0]


def reconstruct(source_file, far_file, circuit):
    raw = [source.ex.read_rows(source_file), source.ex.read_rows(far_file)]
    snapshots, repair = chain.repair_snapshots(raw)
    start, far = snapshots
    path = bypass.make_path(start, far)
    event_polynomial = source.determinant_polynomial(path, circuit)
    bracket = locate_bracket(event_polynomial)
    _polynomial, root = source.isolate_event(path, circuit, bracket)
    if _polynomial != event_polynomial:
        raise AssertionError("event polynomial reconstruction mismatch")
    lo, hi = Q(root["lo"]), Q(root["hi"])
    if not Q(0) < lo < hi < Q(1):
        raise AssertionError(root)

    pre_parameter = lo / 2
    far_parameter = (hi + 1) / 2
    pre_points = source.evaluate_path(path, pre_parameter)
    far_points = source.evaluate_path(path, far_parameter)
    pre_faces, _ = source.fresh_faces(pre_points)
    far_faces, _ = source.fresh_faces(far_points)
    pre_support, pre_mechanics = source.assert_cell(pre_points, pre_faces)
    far_support, far_mechanics = source.assert_cell(far_points, far_faces)
    pre_sets = {frozenset(face) for face in pre_faces}
    far_sets = {frozenset(face) for face in far_faces}
    removed = sorted(sorted(face) for face in pre_sets - far_sets)
    added = sorted(sorted(face) for face in far_sets - pre_sets)
    if len(removed) != 2 or len(added) != 2:
        raise AssertionError(("not a two-to-two support flip", removed, added))

    wall_parameter = (lo + hi) / 2
    wall_points = source.evaluate_path(path, wall_parameter)
    wall_faces, _ = source.fresh_faces(wall_points, coplanar_rel=2e-11)
    wall_fvector, wall_edges = source.wall_f_vector(wall_faces)
    if wall_fvector != source.EXPECTED_WALL_F_VECTOR:
        raise AssertionError(wall_fvector)
    wall_sets = {frozenset(face) for face in wall_faces}
    if frozenset(circuit) not in wall_sets:
        raise AssertionError("event quadrilateral absent from wall")
    if not source.forced_rails().issubset(wall_edges):
        raise AssertionError(("wall rail loss", sorted(source.forced_rails() - wall_edges)))

    pre_cover = source.exact_class_cover(path, pre_faces, Q(0), lo)
    far_cover = source.exact_class_cover(path, far_faces, hi, Q(1))
    pre_event_support = source.support_event_audit(
        path, pre_faces, event_polynomial, lo, hi
    )
    far_event_support = source.support_event_audit(
        path, far_faces, event_polynomial, lo, hi
    )
    wall_mechanics = source.ex.certify_mechanics_interval(
        path, wall_faces, source.PROTECTED, lo, hi
    )
    comparison = bypass.comparison_packet(
        bypass.selected_residuals(start, pre_faces),
        bypass.selected_residuals(far, far_faces),
    )
    return {
        "snapshots": snapshots,
        "repair": repair,
        "path": path,
        "event_polynomial": event_polynomial,
        "root": root,
        "pre_faces": pre_faces,
        "wall_faces": wall_faces,
        "far_faces": far_faces,
        "event": {
            "circuit": list(circuit),
            "root": root,
            "polynomial_exact": event_polynomial.exact(),
            "polynomial_digest": canonical_hash(event_polynomial.exact()),
            "pre_support_on_root_bracket": pre_event_support,
            "far_support_on_root_bracket": far_event_support,
            "removed_faces": removed,
            "added_faces": added,
        },
        "pre_cell": {
            "interval": [source.ex.qs(Q(0)), source.ex.qs(lo)],
            "representative": source.ex.qs(pre_parameter),
            "support": {key: value for key, value in pre_support.items() if key != "edges"},
            "mechanics": pre_mechanics,
            "class_cover": pre_cover,
        },
        "wall": {
            "interval": [source.ex.qs(lo), source.ex.qs(hi)],
            "representative": source.ex.qs(wall_parameter),
            "f_vector": wall_fvector,
            "mechanics": wall_mechanics,
            "missing_forced_rails": [],
        },
        "far_cell": {
            "interval": [source.ex.qs(hi), source.ex.qs(Q(1))],
            "representative": source.ex.qs(far_parameter),
            "support": {key: value for key, value in far_support.items() if key != "edges"},
            "mechanics": far_mechanics,
            "class_cover": far_cover,
            "missing_forced_rails": [],
        },
        "endpoint_material_comparison": comparison,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--far", required=True)
    parser.add_argument("--circuit", required=True)
    parser.add_argument("--prefix", required=True)
    args = parser.parse_args()
    source_file = Path(args.source)
    far_file = Path(args.far)
    if not source_file.is_absolute():
        source_file = HERE / source_file
    if not far_file.is_absolute():
        far_file = HERE / far_file
    circuit = parse_circuit(args.circuit)
    data = reconstruct(source_file, far_file, circuit)

    exact_source = HERE / f"{args.prefix}_exact_source.csv"
    exact_far = HERE / f"{args.prefix}_exact_far.csv"
    pre_faces_file = HERE / f"{args.prefix}_pre_faces.json"
    wall_faces_file = HERE / f"{args.prefix}_wall_faces.json"
    far_faces_file = HERE / f"{args.prefix}_far_faces.json"
    source.write_exact_csv(exact_source, data["snapshots"][0])
    source.write_exact_csv(exact_far, data["snapshots"][1])
    for path, faces in (
        (pre_faces_file, data["pre_faces"]),
        (wall_faces_file, data["wall_faces"]),
        (far_faces_file, data["far_faces"]),
    ):
        path.write_text(json.dumps(faces, indent=2) + "\n")

    pre_cell = data["pre_cell"]
    wall = data["wall"]
    far_cell = data["far_cell"]
    pre_cell.update({
        "face_file": str(pre_faces_file.relative_to(ROOT)),
        "face_hash": canonical_hash(data["pre_faces"]),
    })
    wall.update({
        "face_file": str(wall_faces_file.relative_to(ROOT)),
        "face_hash": canonical_hash(data["wall_faces"]),
    })
    far_cell.update({
        "point_file": str(exact_far.relative_to(ROOT)),
        "face_file": str(far_faces_file.relative_to(ROOT)),
        "face_hash": canonical_hash(data["far_faces"]),
    })
    generated = [
        exact_source, exact_far, pre_faces_file, wall_faces_file, far_faces_file
    ]
    certificate_file = HERE / f"{args.prefix}_certificate.json"
    payload = {
        "version": 1,
        "scope": "exact rail-preserving support flip",
        "verdict": "EXACT_RAIL_PRESERVING_SUPPORT_FLIP_PASS",
        "source_raw": str(source_file.relative_to(ROOT)),
        "far_raw": str(far_file.relative_to(ROOT)),
        "exact_source": str(exact_source.relative_to(ROOT)),
        "construction": {
            "repair": data["repair"],
            "path_digest": canonical_hash({
                str(label): [coordinate.exact() for coordinate in data["path"][label]]
                for label in sorted(data["path"])
            }),
        },
        "event": data["event"],
        "pre_cell": pre_cell,
        "wall": wall,
        "far_cell": far_cell,
        "endpoint_material_comparison": data["endpoint_material_comparison"],
        "generated_sha256": {
            str(path.relative_to(ROOT)): sha256(path) for path in generated
        },
        "conclusion": (
            "One algebraic two-to-two support flip is isolated exactly.  Both "
            "strict cells and the wall retain the complete protected geometry, "
            "all 37 rails, own-centroid class (2,2,2), and the endpoint strictly "
            "improves every selected residual."
        ),
    }
    certificate_file.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "verdict": payload["verdict"],
        "root": data["root"]["decimal_interval"],
        "removed_faces": data["event"]["removed_faces"],
        "added_faces": data["event"]["added_faces"],
        "endpoint_ratios": {
            name: row["decimal_ratio"]
            for name, row in data["endpoint_material_comparison"].items()
        },
        "certificate": str(certificate_file),
    }, indent=2))


if __name__ == "__main__":
    main()
