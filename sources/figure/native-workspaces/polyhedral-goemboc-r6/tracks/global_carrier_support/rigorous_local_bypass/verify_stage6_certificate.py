#!/usr/bin/env python3
"""Clean-process exact verifier for the stage-6 tetrahedral flip."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from build_certificate import canonical_hash
from build_stage6_certificate import (
    BASE_ADAPTIVE,
    BIRTH_ATLAS,
    SOURCE,
    SOURCE_AUDIT,
    STAGE6,
    STAGE6_AUDIT,
    STAGE6_POST,
    STAGE6_PRE,
    compute,
)
import exact_core as ex


HERE = Path(__file__).resolve().parent
DEFAULT = HERE / "stage6_certificate.json"


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", type=Path, default=DEFAULT)
    args = parser.parse_args()
    saved = json.loads(args.certificate.read_text())
    paths = (SOURCE, SOURCE_AUDIT, BIRTH_ATLAS, BASE_ADAPTIVE, STAGE6,
             STAGE6_AUDIT, STAGE6_PRE, STAGE6_POST)
    if saved["source_hashes_sha256"] != {path.name: ex.sha256(path) for path in paths}:
        raise AssertionError("stage6 source hash mismatch")
    ledgers = saved["face_ledgers"]
    for side in ("pre", "wall", "post"):
        if canonical_hash(ledgers[f"{side}_faces"]) != ledgers[f"{side}_faces_sha256"]:
            raise AssertionError(("face hash", side))
    rebuilt = compute(ledgers["pre_faces"], ledgers["post_faces"])
    if canonical(rebuilt) != canonical(saved):
        a = hashlib.sha256(canonical(rebuilt).encode()).hexdigest()
        b = hashlib.sha256(canonical(saved).encode()).hexdigest()
        raise AssertionError(("stage6 rebuild mismatch", a, b))
    root = saved["circuit_root"]
    if root["support_order"]["other_strict_support_polynomial_count"] != 5957:
        raise AssertionError("stage6 order incomplete")
    if len(root["support_order"]["target_support_family"]) != 2:
        raise AssertionError("stage6 target family")
    transition = saved["sides"]["feature_transition"]
    if not transition["no_vertex_or_saddle_birth"]:
        raise AssertionError("stage6 unexpected feature birth")
    if saved["verdict"] != "EXACT_DIRECTED_STAGE6_TETRAHEDRAL_FLIP_PASS":
        raise AssertionError(saved["verdict"])
    print("VERIFY_STAGE6_SOURCE_AND_FACE_HASHES_PASS")
    print("VERIFY_STAGE6_LITERAL_CIRCUIT_ROOT_ORDER_PASS")
    print("VERIFY_STAGE6_MERGED_SUPPORTING_QUADRILATERAL_PASS")
    print("VERIFY_STAGE6_POST_SIDE_CLASS_AND_FEATURE_TRANSFER_PASS")
    print("EXACT_DIRECTED_STAGE6_TETRAHEDRAL_FLIP_PASS")


if __name__ == "__main__":
    main()

