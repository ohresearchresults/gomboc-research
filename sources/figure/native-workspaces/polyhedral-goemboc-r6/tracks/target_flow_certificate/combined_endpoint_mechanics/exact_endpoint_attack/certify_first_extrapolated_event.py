#!/usr/bin/env python3
"""Exact certificate for the first support event beyond path parameter one."""
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


CIRCUIT = (69, 228, 237, 255)
SEARCH_BRACKET = (Q(1013, 1000), Q(1015, 1000))
START = Q(1)
FAR = Q(51, 50)
CERTIFICATE = HERE / "first_extrapolated_event_certificate.json"
PRE_FACES = HERE / "first_extrapolated_event_pre_faces.json"
WALL_FACES = HERE / "first_extrapolated_event_wall_faces.json"
FAR_FACES = HERE / "first_extrapolated_event_far_faces.json"
FAR_POINTS = HERE / "first_extrapolated_event_far.csv"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n")


def main() -> None:
    _start, _endpoint, path, construction = source.build_exact_path()
    event_polynomial, root = source.isolate_event(path, CIRCUIT, SEARCH_BRACKET)
    lo, hi = Q(root["lo"]), Q(root["hi"])
    if not START < lo < hi < FAR:
        raise AssertionError((START, lo, hi, FAR))

    pre_representative = (START + lo) / 2
    far_representative = (hi + FAR) / 2
    pre_points = source.evaluate_path(path, pre_representative)
    far_points = source.evaluate_path(path, far_representative)
    pre_faces, _ = source.fresh_faces(pre_points)
    far_faces, _ = source.fresh_faces(far_points)
    pre_support, pre_mechanics = source.assert_cell(pre_points, pre_faces)
    far_support, far_mechanics = source.assert_cell(far_points, far_faces)

    wall_midpoint = (lo + hi) / 2
    wall_points = source.evaluate_path(path, wall_midpoint)
    wall_faces, _ = source.fresh_faces(wall_points, coplanar_rel=2e-11)
    wall_f_vector, wall_edges = source.wall_f_vector(wall_faces)
    if wall_f_vector != source.EXPECTED_WALL_F_VECTOR:
        raise AssertionError(("wall f-vector", wall_f_vector))
    wall_face_sets = {frozenset(face) for face in wall_faces}
    if frozenset(CIRCUIT) not in wall_face_sets:
        raise AssertionError("event quadrilateral absent at isolated wall")
    if source.BASE not in wall_face_sets or frozenset(source.QUAD) not in wall_face_sets:
        raise AssertionError("protected base or quadrilateral absent at wall")
    if not source.forced_rails().issubset(wall_edges):
        raise AssertionError("wall loses a forced rail")

    pre_sets = {frozenset(face) for face in pre_faces}
    far_sets = {frozenset(face) for face in far_faces}
    removed = sorted(sorted(face) for face in pre_sets - far_sets)
    added = sorted(sorted(face) for face in far_sets - pre_sets)
    expected_removed = [[69, 228, 237], [69, 228, 255]]
    expected_added = [[69, 237, 255], [228, 237, 255]]
    if removed != expected_removed or added != expected_added:
        raise AssertionError((removed, added))

    pre_cover = source.exact_class_cover(path, pre_faces, START, lo)
    far_cover = source.exact_class_cover(path, far_faces, hi, FAR)
    pre_event_support = source.support_event_audit(
        path, pre_faces, event_polynomial, lo, hi
    )
    far_event_support = source.support_event_audit(
        path, far_faces, event_polynomial, lo, hi
    )
    wall_mechanics = source.ex.certify_mechanics_interval(
        path, wall_faces, source.PROTECTED, lo, hi
    )

    write_json(PRE_FACES, pre_faces)
    write_json(WALL_FACES, wall_faces)
    write_json(FAR_FACES, far_faces)
    source.write_exact_csv(FAR_POINTS, source.evaluate_path(path, FAR))

    generated = [PRE_FACES, WALL_FACES, FAR_FACES, FAR_POINTS]
    payload = {
        "version": 1,
        "scope": "first exact support event after the certified U54 material endpoint",
        "verdict": "STRICT_EXACT_POST_ENDPOINT_SUPPORT_FLIP_NONWINNER",
        "path_polynomial_digest": construction["path_polynomial_digest"],
        "parameter_interval": {
            "start": source.ex.qs(START),
            "root": root,
            "far": source.ex.qs(FAR),
        },
        "event": {
            "circuit": list(CIRCUIT),
            "polynomial_exact": event_polynomial.exact(),
            "polynomial_digest": canonical_hash(event_polynomial.exact()),
            "pre_support_on_root_bracket": pre_event_support,
            "far_support_on_root_bracket": far_event_support,
            "removed_faces": removed,
            "added_faces": added,
        },
        "pre_cell": {
            "representative": source.ex.qs(pre_representative),
            "face_file": str(PRE_FACES.relative_to(ROOT)),
            "face_hash": canonical_hash(pre_faces),
            "support": {k: v for k, v in pre_support.items() if k != "edges"},
            "mechanics": pre_mechanics,
            "class_cover": pre_cover,
        },
        "wall": {
            "representative": source.ex.qs(wall_midpoint),
            "face_file": str(WALL_FACES.relative_to(ROOT)),
            "face_hash": canonical_hash(wall_faces),
            "f_vector": wall_f_vector,
            "mechanics": wall_mechanics,
        },
        "far_cell": {
            "representative": source.ex.qs(far_representative),
            "endpoint_parameter": source.ex.qs(FAR),
            "point_file": str(FAR_POINTS.relative_to(ROOT)),
            "face_file": str(FAR_FACES.relative_to(ROOT)),
            "face_hash": canonical_hash(far_faces),
            "support": {k: v for k, v in far_support.items() if k != "edges"},
            "mechanics": far_mechanics,
            "class_cover": far_cover,
        },
        "generated_sha256": {
            str(path.relative_to(ROOT)): sha256(path) for path in generated
        },
        "conclusion": (
            "The first extrapolated event is one isolated quadrilateral flip; "
            "both adjacent open cells and the merged wall are exact strict (2,2,2) "
            "with the enlarged base, protected U8, quadrilateral and all rails."
        ),
    }
    CERTIFICATE.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "verdict": payload["verdict"],
        "root": root["decimal_interval"],
        "removed_faces": removed,
        "added_faces": added,
        "pre_class": pre_mechanics["class"],
        "wall_class": wall_mechanics["midpoint_class"]["class"],
        "far_class": far_mechanics["class"],
        "certificate": str(CERTIFICATE),
    }, indent=2))


if __name__ == "__main__":
    main()
