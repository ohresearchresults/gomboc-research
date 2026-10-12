#!/usr/bin/env python3
"""Rebuild the 14 primitive rows and verify the exact full-13D dual."""
from __future__ import annotations

import argparse
import json
import re
import sys
from fractions import Fraction as F
from pathlib import Path


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import rational_shared_certificate as model  # noqa: E402


def parse_fraction(item: dict) -> F:
    return F(int(item["numerator"]), int(item["denominator"]))


def primitive_by_name(name, p, centroid, normals, stable_face):
    if name == "target:S[7,8,246]-death":
        return -model.stable_primitives(stable_face, p, centroid, normals)[1], True
    if name == "target:U54-death":
        return -model.vertex_primitive(54, 1, p, centroid), True
    match = re.fullmatch(r"guard:topology:f(\d+):row(\d+)", name)
    if match:
        return model.topology_primitive(int(match[1]), int(match[2]), p, normals), False
    match = re.fullmatch(r"guard:U8:to(\d+)", name)
    if match:
        return model.vertex_primitive(8, int(match[1]), p, centroid), False
    match = re.fullmatch(r"guard:antiface:f(\d+):c(\d+)", name)
    if match:
        return -model.stable_primitives(int(match[1]), p, centroid, normals)[int(match[2])], False
    match = re.fullmatch(r"guard:antivertex:v(\d+):to(\d+)", name)
    if match:
        return -model.vertex_primitive(int(match[1]), int(match[2]), p, centroid), False
    match = re.fullmatch(r"guard:antiedge:(\d+)-(\d+):c(\d+)", name)
    if match:
        edge = (int(match[1]), int(match[2]))
        return -model.edge_primitives(edge, p, centroid, normals)[int(match[3])], False
    raise ValueError(f"unrecognized primitive {name}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--certificate", type=Path,
                    default=HERE / "row54_full13_exact.json")
    ap.add_argument("--output", type=Path,
                    default=HERE / "row54_full13_exact_audit.json")
    args = ap.parse_args()
    certificate = json.load(args.certificate.open())

    p = model.rational_chart_points()
    centroid = model.own_centroid(p)
    normals = model.face_normals(p)
    stable_face = next(i for i, face in enumerate(model.FACES)
                       if frozenset(face) == frozenset((7, 8, 246)))
    epsilon = F(1, 1_000_000)

    matrix, vector, dual = [], [], []
    row_checks = []
    for stored in certificate["support"]:
        item, target = primitive_by_name(
            stored["name"], p, centroid, normals, stable_face
        )
        raw_a = [-x for x in item.grad]
        raw_b = item.value - (epsilon if target else F(0))
        expected_scale = F(1, 1) / max([abs(raw_b), *(abs(x) for x in raw_a)])
        scale = parse_fraction(stored["scale"])
        a = [parse_fraction(x) for x in stored["A"]]
        b = parse_fraction(stored["b"])
        y = parse_fraction(stored["y"])
        checks = {
            "scale": scale == expected_scale,
            "A": a == [scale * x for x in raw_a],
            "b": b == scale * raw_b,
            "y_nonnegative": y >= 0,
        }
        row_checks.append({"name": stored["name"], **checks})
        matrix.append(a); vector.append(b); dual.append(y)

    residual = [sum((matrix[i][j] * dual[i] for i in range(len(dual))), F(0))
                for j in range(model.DIM)]
    b_dot_y = sum((x * y for x, y in zip(vector, dual)), F(0))
    checks = {
        "all_primitive_rows_rebuilt": all(
            all(value for key, value in item.items() if key != "name")
            for item in row_checks
        ),
        "support_size_is_14": len(dual) == 14,
        "dual_strictly_positive": all(y > 0 for y in dual),
        "dual_exactly_normalized": sum(dual, F(0)) == 1,
        "A_transpose_y_exact_zero": all(x == 0 for x in residual),
        "b_dot_y_strictly_negative": b_dot_y < 0,
    }
    assert all(checks.values()), {name: value for name, value in checks.items() if not value}
    out = {
        "status": "PASS",
        "logical_contradiction": (
            "A*x <= b and y>=0 would imply 0=(A^T*y).x <= b^T*y<0."
        ),
        "checks": checks,
        "row_checks": row_checks,
        "dual_y_decimal": [float(x) for x in dual],
        "A_transpose_y": [str(x) for x in residual],
        "b_dot_y": {
            "numerator": str(b_dot_y.numerator),
            "denominator": str(b_dot_y.denominator),
            "decimal": float(b_dot_y),
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
