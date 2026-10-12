#!/usr/bin/env python3
"""Independent reconstruction of the first exact post-bypass material step."""
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
import certify_mandatory_rail_bypass as bypass  # noqa: E402
import certify_post_bypass_step as builder  # noqa: E402


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main() -> None:
    certificate = json.loads(builder.CERTIFICATE.read_text())
    if certificate["verdict"] != "EXACT_POST_BYPASS_MATERIAL_STEP_PASS":
        raise AssertionError("unexpected verdict")
    start_raw = source.ex.read_rows(builder.START_FILE)
    endpoint_raw = source.ex.read_rows(builder.RAW_ENDPOINT)
    start, endpoint, _repair = builder.repair_pair(start_raw, endpoint_raw)
    if source.ex.read_rows(builder.EXACT_ENDPOINT) != endpoint:
        raise AssertionError("exact endpoint table mismatch")
    path = bypass.make_path(start, endpoint)
    midpoint = source.evaluate_path(path, Q(1, 2))
    faces, _ = source.fresh_faces(midpoint)
    stored_faces = json.loads((ROOT / certificate["face_file"]).read_text())
    if faces != stored_faces or canonical_hash(faces) != certificate["face_hash"]:
        raise AssertionError("face reconstruction mismatch")
    support, mechanics = source.assert_cell(midpoint, faces)
    if support["f_vector"] != certificate["f_vector"]:
        raise AssertionError("f-vector mismatch")
    if mechanics != certificate["mechanics"]:
        raise AssertionError("mechanics mismatch")
    cover = source.exact_class_cover(path, faces, Q(0), Q(1))
    if cover != certificate["class_cover"]:
        raise AssertionError("class-cover mismatch")
    determinant = source.determinant_polynomial(path, bypass.CIRCUIT)
    midpoint_value = determinant.eval(Q(1, 2))
    sign = 1 if midpoint_value > 0 else -1 if midpoint_value < 0 else 0
    sign_record = source.exact_sign_record(determinant, Q(0), Q(1), sign)
    if sign_record != certificate["mandatory_circuit_sign"]:
        raise AssertionError("mandatory-circuit sign mismatch")
    reference = bypass.selected_residuals(start, faces)
    endpoint_values = bypass.selected_residuals(endpoint, faces)
    comparison = bypass.comparison_packet(reference, endpoint_values)
    if comparison != certificate["endpoint_material_comparison"]:
        raise AssertionError("material comparison mismatch")
    for relative, expected in certificate["generated_sha256"].items():
        if sha256(ROOT / relative) != expected:
            raise AssertionError(("SHA mismatch", relative))
    print("INDEPENDENT_EXACT_POST_BYPASS_MATERIAL_STEP_PASS")


if __name__ == "__main__":
    main()
