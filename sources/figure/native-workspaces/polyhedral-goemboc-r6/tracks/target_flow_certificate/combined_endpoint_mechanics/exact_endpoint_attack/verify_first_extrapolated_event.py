#!/usr/bin/env python3
"""Independent reconstruction of the first post-endpoint support flip."""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(PARENT))

import build_u54_material_exact_path as source  # noqa: E402


CERTIFICATE = HERE / "first_extrapolated_event_certificate.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def read_json(path: Path):
    return json.loads(path.read_text())


def main() -> None:
    certificate = read_json(CERTIFICATE)
    if certificate["verdict"] != "STRICT_EXACT_POST_ENDPOINT_SUPPORT_FLIP_NONWINNER":
        raise AssertionError("unexpected certificate verdict")
    _start, _endpoint, path, construction = source.build_exact_path()
    if construction["path_polynomial_digest"] != certificate["path_polynomial_digest"]:
        raise AssertionError("path digest mismatch")

    circuit = tuple(certificate["event"]["circuit"])
    polynomial = source.determinant_polynomial(path, circuit)
    if polynomial.exact() != certificate["event"]["polynomial_exact"]:
        raise AssertionError("event polynomial mismatch")
    if canonical_hash(polynomial.exact()) != certificate["event"]["polynomial_digest"]:
        raise AssertionError("event polynomial digest mismatch")
    root = certificate["parameter_interval"]["root"]
    lo, hi = Q(root["lo"]), Q(root["hi"])
    start = Q(certificate["parameter_interval"]["start"])
    far = Q(certificate["parameter_interval"]["far"])
    if not start < lo < hi < far:
        raise AssertionError("root ordering failed")
    if polynomial.eval(lo) * polynomial.eval(hi) >= 0:
        raise AssertionError("isolating bracket does not change sign")
    derivative_sign, _leaves, _worst = source.ex.bernstein_sign(
        polynomial.derivative(), lo, hi, max_depth=60
    )
    if derivative_sign != root["derivative_sign"] or derivative_sign == 0:
        raise AssertionError("event polynomial is not monotone on the bracket")

    pre_file = ROOT / certificate["pre_cell"]["face_file"]
    wall_file = ROOT / certificate["wall"]["face_file"]
    far_file = ROOT / certificate["far_cell"]["face_file"]
    point_file = ROOT / certificate["far_cell"]["point_file"]
    pre_faces, wall_faces, far_faces = map(read_json, (pre_file, wall_file, far_file))
    for file_path, faces, expected in (
        (pre_file, pre_faces, certificate["pre_cell"]["face_hash"]),
        (wall_file, wall_faces, certificate["wall"]["face_hash"]),
        (far_file, far_faces, certificate["far_cell"]["face_hash"]),
    ):
        if canonical_hash(faces) != expected:
            raise AssertionError(("face hash mismatch", file_path))

    pre_parameter = Q(certificate["pre_cell"]["representative"])
    far_parameter = Q(certificate["far_cell"]["representative"])
    wall_parameter = Q(certificate["wall"]["representative"])
    for parameter, stored_faces, expected_fvector, expected_class in (
        (pre_parameter, pre_faces, [60, 158, 100], [2, 2, 2]),
        (far_parameter, far_faces, [60, 158, 100], [2, 2, 2]),
    ):
        points = source.evaluate_path(path, parameter)
        rebuilt_faces, _ = source.fresh_faces(points)
        if rebuilt_faces != stored_faces:
            raise AssertionError(("strict-cell face mismatch", parameter))
        support = source.ex.supporting_cell(points, rebuilt_faces)
        _ledger, mechanics = source.ex.classify_point(points, rebuilt_faces)
        if support["f_vector"] != expected_fvector or mechanics["class"] != expected_class:
            raise AssertionError((support["f_vector"], mechanics["class"]))
        if support["active_labels"] != sorted(set(points) - {73}):
            raise AssertionError("wrong active-row set")
        if not source.forced_rails().issubset(set(support["edges"])):
            raise AssertionError("strict cell loses a rail")

    wall_points = source.evaluate_path(path, wall_parameter)
    rebuilt_wall, _ = source.fresh_faces(wall_points, coplanar_rel=2e-11)
    if rebuilt_wall != wall_faces:
        raise AssertionError("wall face mismatch")
    wall_fvector, wall_edges = source.wall_f_vector(wall_faces)
    if wall_fvector != [60, 157, 99]:
        raise AssertionError(wall_fvector)
    if frozenset(circuit) not in {frozenset(face) for face in wall_faces}:
        raise AssertionError("wall quadrilateral missing")
    if not source.forced_rails().issubset(wall_edges):
        raise AssertionError("wall loses a rail")
    wall_mechanics = source.ex.certify_mechanics_interval(
        path, wall_faces, source.PROTECTED, lo, hi
    )
    if wall_mechanics["midpoint_class"]["class"] != [2, 2, 2]:
        raise AssertionError(wall_mechanics["midpoint_class"])

    exact_far = source.evaluate_path(path, far)
    stored_far = source.ex.read_rows(point_file)
    if exact_far != stored_far:
        raise AssertionError("far exact point table mismatch")

    for relative, expected in certificate["generated_sha256"].items():
        if sha256(ROOT / relative) != expected:
            raise AssertionError(("generated file SHA mismatch", relative))

    removed = sorted(
        sorted(face)
        for face in {frozenset(face) for face in pre_faces}
        - {frozenset(face) for face in far_faces}
    )
    added = sorted(
        sorted(face)
        for face in {frozenset(face) for face in far_faces}
        - {frozenset(face) for face in pre_faces}
    )
    if removed != certificate["event"]["removed_faces"]:
        raise AssertionError("removed-face ledger mismatch")
    if added != certificate["event"]["added_faces"]:
        raise AssertionError("added-face ledger mismatch")

    print("INDEPENDENT_EXACT_POST_ENDPOINT_SUPPORT_FLIP_PASS")


if __name__ == "__main__":
    main()
