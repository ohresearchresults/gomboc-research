#!/usr/bin/env python3
"""Clean-process verifier for ``certificate.json``.

The verifier never asks Qhull to decide a theorem statement.  It takes the two
stored face ledgers as explicit combinatorial inputs, checks their hashes, and
reconstructs every support, mechanics, Bernstein, root, and tangent assertion
from the hashed source artifacts using exact Fraction arithmetic.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
DEFAULT = HERE / "certificate.json"

from build_certificate import (  # noqa: E402
    ADAPTIVE,
    ATLAS_JSON,
    CONTINUATION,
    NUMERIC_WALL,
    ROOTS,
    SOURCE,
    SOURCE_AUDIT,
    canonical_hash,
    compute,
)
import exact_core as ex  # noqa: E402


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", type=Path, default=DEFAULT)
    args = parser.parse_args()
    saved = json.loads(args.certificate.read_text())

    paths = (SOURCE, SOURCE_AUDIT, ATLAS_JSON, CONTINUATION, ROOTS, ADAPTIVE, NUMERIC_WALL)
    expected_hashes = {path.name: ex.sha256(path) for path in paths}
    if saved["source_hashes_sha256"] != expected_hashes:
        raise AssertionError("source hash mismatch")
    star_faces = saved["chart"]["star_faces"]
    post_faces = saved["first_hard_wall"]["post_faces"]
    if canonical_hash(star_faces) != saved["chart"]["star_faces_sha256"]:
        raise AssertionError("star face-ledger hash mismatch")
    if canonical_hash(post_faces) != saved["first_hard_wall"]["post_faces_sha256"]:
        raise AssertionError("post face-ledger hash mismatch")

    rebuilt = compute(star_faces=star_faces, post_faces=post_faces)
    if canonical(rebuilt) != canonical(saved):
        left = hashlib.sha256(canonical(rebuilt).encode()).hexdigest()
        right = hashlib.sha256(canonical(saved).encode()).hexdigest()
        raise AssertionError(("certificate rebuild mismatch", left, right))

    if saved["verdict"] != "EXACT_DIRECTED_LOCAL_BYPASS_AND_FIRST_HARD_WALL_PASS":
        raise AssertionError(saved["verdict"])
    if saved["linked_common_root"]["face_beta_identity_polynomial_exact"] != ["0"]:
        raise AssertionError("linked wall identity is not literal zero")
    if saved["independent_antibirth_tangent"]["keep_annihilation_polynomials"] != [["0"]] * 4:
        raise AssertionError("keep annihilation is not literal zero")
    if saved["independent_antibirth_tangent"]["birth_rate_sign_on_root_interval"] != -1:
        raise AssertionError("tangent is not antibirth")
    if [row["certified_polynomial_count"] for row in saved["continuous_L_path"]["segments"]] != [6968, 6968]:
        raise AssertionError("unexpected L guard count")
    order = saved["first_hard_wall"]["support_order_certificate"]
    if len(order["target_support_family"]) != 2 or order["other_strict_support_polynomial_count"] != 5957:
        raise AssertionError("hard-wall order certificate incomplete")

    print("VERIFY_SOURCE_AND_FACE_HASHES_PASS")
    print("VERIFY_LINKED_COMMON_ROOT_IDENTITY_PASS")
    print("VERIFY_EXACT_INDEPENDENT_ANTIBIRTH_TANGENT_PASS")
    print("VERIFY_FOUR_FRESH_QUADRANT_CELLS_PASS")
    print("VERIFY_CONTINUOUS_L_PATH_13936_POLYNOMIALS_PASS")
    print("VERIFY_FIRST_HARD_CIRCUIT_AND_ORDER_PASS")
    print("EXACT_DIRECTED_LOCAL_BYPASS_AND_FIRST_HARD_WALL_PASS")


if __name__ == "__main__":
    main()

