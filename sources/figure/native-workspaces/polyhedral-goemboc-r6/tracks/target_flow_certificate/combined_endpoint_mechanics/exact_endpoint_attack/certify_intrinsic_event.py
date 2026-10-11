#!/usr/bin/env python3
"""Exactify the intrinsic SLP flip on circuit 224,228,251,252."""
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


RAW_START = HERE / "post_flip_intrinsic_step_008.csv"
RAW_FAR = HERE / "intrinsic_event_far.csv"
CIRCUIT = (224, 228, 251, 252)
ROOT_BRACKET = (Q(22, 25), Q(89, 100))
EXACT_START = HERE / "intrinsic_event_exact_source.csv"
EXACT_FAR = HERE / "intrinsic_event_exact_far.csv"
PRE_FACES = HERE / "intrinsic_event_exact_pre_faces.json"
WALL_FACES = HERE / "intrinsic_event_exact_wall_faces.json"
FAR_FACES = HERE / "intrinsic_event_exact_far_faces.json"
CERTIFICATE = HERE / "intrinsic_event_exact_certificate.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def exact_path():
    raw_start = source.ex.read_rows(RAW_START)
    raw_far = source.ex.read_rows(RAW_FAR)
    if set(raw_start) != set(raw_far):
        raise AssertionError("source/far labels differ")
    anchor = raw_start[0]
    normal = source.ex.cross(
        source.ex.sub(raw_start[1], anchor), source.ex.sub(raw_start[2], anchor)
    )
    normal_norm2 = source.ex.norm2(normal)
    start, start_base = source.project_base(raw_start, anchor, normal, normal_norm2)
    far, far_base = source.project_base(raw_far, anchor, normal, normal_norm2)
    start, start_uv, start_quad = source.repair_quad(start)
    far, far_uv, far_quad = source.repair_quad(far)
    path = {
        label: tuple(
            source.P((start[label][axis], far[label][axis] - start[label][axis]))
            for axis in range(3)
        )
        for label in start
        if label != 246
    }
    u = source.P((start_uv[0], far_uv[0] - start_uv[0]))
    v = source.P((start_uv[1], far_uv[1] - start_uv[1]))
    path[246] = source.ex.add(
        path[7],
        source.ex.add(
            source.ex.mul(source.ex.sub(path[8], path[7]), u),
            source.ex.mul(source.ex.sub(path[245], path[7]), v),
        ),
    )
    if source.determinant_polynomial(path, source.QUAD) != source.P.zero():
        raise AssertionError("protected quadrilateral is not identically planar")
    return start, far, path, {
        "start_base": start_base,
        "far_base": far_base,
        "start_quad": start_quad,
        "far_quad": far_quad,
        "path_digest": canonical_hash({
            str(label): [coordinate.exact() for coordinate in path[label]]
            for label in sorted(path)
        }),
    }


def main() -> None:
    start, far, path, construction = exact_path()
    source.write_exact_csv(EXACT_START, start)
    source.write_exact_csv(EXACT_FAR, far)
    event_polynomial, root = source.isolate_event(path, CIRCUIT, ROOT_BRACKET)
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
    far_support = source.ex.supporting_cell(far_points, far_faces)
    _far_ledger, far_mechanics = source.ex.classify_point(far_points, far_faces)
    if far_support["f_vector"] != source.EXPECTED_CELL_F_VECTOR:
        raise AssertionError(far_support)
    if far_support["active_labels"] != sorted(set(far_points) - {73}):
        raise AssertionError(("wrong far active labels", far_support["active_labels"]))
    if far_mechanics["class"] != source.EXPECTED_CLASS:
        raise AssertionError(far_mechanics)
    far_face_sets = {frozenset(face) for face in far_faces}
    if source.BASE not in far_face_sets or frozenset(source.QUAD) not in far_face_sets:
        raise AssertionError("far cell loses protected base or quadrilateral")
    missing_far_rails = sorted(source.forced_rails() - set(far_support["edges"]))
    if missing_far_rails != [(251, 252)]:
        raise AssertionError(("unexpected far rail ledger", missing_far_rails))
    pre_sets = {frozenset(face) for face in pre_faces}
    far_sets = {frozenset(face) for face in far_faces}
    removed = sorted(sorted(face) for face in pre_sets - far_sets)
    added = sorted(sorted(face) for face in far_sets - pre_sets)
    if removed != [[224, 251, 252], [228, 251, 252]]:
        raise AssertionError(("removed", removed))
    if added != [[224, 228, 251], [224, 228, 252]]:
        raise AssertionError(("added", added))

    wall_parameter = (lo + hi) / 2
    wall_points = source.evaluate_path(path, wall_parameter)
    wall_faces, _ = source.fresh_faces(wall_points, coplanar_rel=2e-11)
    wall_fvector, wall_edges = source.wall_f_vector(wall_faces)
    if wall_fvector != [60, 157, 99]:
        raise AssertionError(wall_fvector)
    wall_sets = {frozenset(face) for face in wall_faces}
    if frozenset(CIRCUIT) not in wall_sets:
        raise AssertionError("event quadrilateral absent")
    if source.BASE not in wall_sets or frozenset(source.QUAD) not in wall_sets:
        raise AssertionError("protected face absent")
    missing_wall_rails = sorted(source.forced_rails() - wall_edges)
    if missing_wall_rails != [(251, 252)]:
        raise AssertionError(("unexpected wall rail ledger", missing_wall_rails))

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

    for file_path, value in (
        (PRE_FACES, pre_faces),
        (WALL_FACES, wall_faces),
        (FAR_FACES, far_faces),
    ):
        file_path.write_text(json.dumps(value, indent=2) + "\n")
    generated = [EXACT_START, EXACT_FAR, PRE_FACES, WALL_FACES, FAR_FACES]
    payload = {
        "version": 1,
        "scope": "exact intrinsic post-endpoint support flip",
        "verdict": "EXACT_MANDATORY_RAIL_WALL_NONWINNER",
        "construction": construction,
        "event": {
            "circuit": list(CIRCUIT),
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
            "face_file": str(PRE_FACES.relative_to(ROOT)),
            "face_hash": canonical_hash(pre_faces),
            "support": {key: value for key, value in pre_support.items() if key != "edges"},
            "mechanics": pre_mechanics,
            "class_cover": pre_cover,
        },
        "wall": {
            "interval": [source.ex.qs(lo), source.ex.qs(hi)],
            "representative": source.ex.qs(wall_parameter),
            "face_file": str(WALL_FACES.relative_to(ROOT)),
            "face_hash": canonical_hash(wall_faces),
            "f_vector": wall_fvector,
            "mechanics": wall_mechanics,
            "missing_forced_rails": [list(edge) for edge in missing_wall_rails],
        },
        "far_cell": {
            "interval": [source.ex.qs(hi), source.ex.qs(Q(1))],
            "representative": source.ex.qs(far_parameter),
            "point_file": str(EXACT_FAR.relative_to(ROOT)),
            "face_file": str(FAR_FACES.relative_to(ROOT)),
            "face_hash": canonical_hash(far_faces),
            "support": {key: value for key, value in far_support.items() if key != "edges"},
            "mechanics": far_mechanics,
            "class_cover": far_cover,
            "missing_forced_rails": [list(edge) for edge in missing_far_rails],
        },
        "generated_sha256": {
            str(file_path.relative_to(ROOT)): sha256(file_path)
            for file_path in generated
        },
        "conclusion": (
            "One isolated actual quadrilateral flip is certified exactly.  The "
            "pre-cell retains all guards, but the merged wall and strict far cell "
            "delete mandatory rail edge (251,252); this event cannot "
            "be accepted without a higher-dimensional bypass or replacement route."
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
