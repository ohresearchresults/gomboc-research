#!/usr/bin/env python3
"""Independent reconstruction of the exact mandatory-rail wall."""
from __future__ import annotations

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
import certify_intrinsic_event as builder  # noqa: E402


CERTIFICATE = HERE / "intrinsic_event_exact_certificate.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main() -> None:
    certificate = json.loads(CERTIFICATE.read_text())
    if certificate["verdict"] != "EXACT_MANDATORY_RAIL_WALL_NONWINNER":
        raise AssertionError("unexpected verdict")
    start, far, path, construction = builder.exact_path()
    if construction["path_digest"] != certificate["construction"]["path_digest"]:
        raise AssertionError("path digest mismatch")
    circuit = tuple(certificate["event"]["circuit"])
    polynomial = source.determinant_polynomial(path, circuit)
    if polynomial.exact() != certificate["event"]["polynomial_exact"]:
        raise AssertionError("event polynomial mismatch")
    if canonical_hash(polynomial.exact()) != certificate["event"]["polynomial_digest"]:
        raise AssertionError("event polynomial hash mismatch")
    root = certificate["event"]["root"]
    lo, hi = Q(root["lo"]), Q(root["hi"])
    if polynomial.eval(lo) * polynomial.eval(hi) >= 0:
        raise AssertionError("root bracket has no sign change")
    sign, _leaves, _worst = source.ex.bernstein_sign(
        polynomial.derivative(), lo, hi, max_depth=60
    )
    if sign != root["derivative_sign"] or sign == 0:
        raise AssertionError("root is not uniquely monotone")

    records = (
        ("pre_cell", (Q(0) + lo) / 2, [60, 158, 100], []),
        ("far_cell", (hi + Q(1)) / 2, [60, 158, 100], [(251, 252)]),
    )
    for name, parameter, expected_fvector, expected_missing in records:
        face_file = ROOT / certificate[name]["face_file"]
        faces = json.loads(face_file.read_text())
        if canonical_hash(faces) != certificate[name]["face_hash"]:
            raise AssertionError((name, "face hash"))
        points = source.evaluate_path(path, parameter)
        rebuilt, _ = source.fresh_faces(points)
        if rebuilt != faces:
            raise AssertionError((name, "face reconstruction"))
        support = source.ex.supporting_cell(points, faces)
        _ledger, mechanics = source.ex.classify_point(points, faces)
        if support["f_vector"] != expected_fvector or mechanics["class"] != [2, 2, 2]:
            raise AssertionError((name, support["f_vector"], mechanics["class"]))
        if support["active_labels"] != sorted(set(points) - {73}):
            raise AssertionError((name, "active rows"))
        missing = sorted(source.forced_rails() - set(support["edges"]))
        if missing != expected_missing:
            raise AssertionError((name, "rail ledger", missing))

    wall_parameter = (lo + hi) / 2
    wall_file = ROOT / certificate["wall"]["face_file"]
    wall_faces = json.loads(wall_file.read_text())
    if canonical_hash(wall_faces) != certificate["wall"]["face_hash"]:
        raise AssertionError("wall face hash")
    wall_points = source.evaluate_path(path, wall_parameter)
    rebuilt_wall, _ = source.fresh_faces(wall_points, coplanar_rel=2e-11)
    if rebuilt_wall != wall_faces:
        raise AssertionError("wall face reconstruction")
    wall_fvector, wall_edges = source.wall_f_vector(wall_faces)
    if wall_fvector != [60, 157, 99]:
        raise AssertionError(wall_fvector)
    if frozenset(circuit) not in {frozenset(face) for face in wall_faces}:
        raise AssertionError("wall quadrilateral absent")
    if sorted(source.forced_rails() - wall_edges) != [(251, 252)]:
        raise AssertionError("wall rail ledger")
    wall_mechanics = source.ex.certify_mechanics_interval(
        path, wall_faces, source.PROTECTED, lo, hi
    )
    if wall_mechanics["midpoint_class"]["class"] != [2, 2, 2]:
        raise AssertionError(wall_mechanics["midpoint_class"])

    exact_start = source.ex.read_rows(builder.EXACT_START)
    if exact_start != start:
        raise AssertionError("exact source table mismatch")
    far_path = ROOT / certificate["far_cell"]["point_file"]
    if source.ex.read_rows(far_path) != far:
        raise AssertionError("exact far table mismatch")
    for relative, expected in certificate["generated_sha256"].items():
        if sha256(ROOT / relative) != expected:
            raise AssertionError(("SHA mismatch", relative))

    print("INDEPENDENT_EXACT_MANDATORY_RAIL_WALL_PASS")


if __name__ == "__main__":
    main()
