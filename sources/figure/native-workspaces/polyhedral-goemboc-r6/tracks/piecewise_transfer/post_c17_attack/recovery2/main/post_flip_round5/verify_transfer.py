#!/usr/bin/env python3
"""Independent reconstruction of the first post-C17 mechanics transfer."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ATTACK = MAIN.parents[1]
SOURCE = MAIN / "post_flip_round4" / "far.csv"
FACES_PATH = MAIN / "post_flip_round4" / "post_faces.json"
CANDIDATE = HERE / "candidate.csv"
CERTIFICATE = HERE / "transfer_certificate.json"
FAR_PATH = HERE / "transfer_far.csv"
OUTPUT = HERE / "transfer_verification.json"

ENGINE_PATH = MAIN / "verify_safe_flip.py"
SPEC = importlib.util.spec_from_file_location(
    "post_c17_transfer_clean_engine", ENGINE_PATH
)
assert SPEC is not None and SPEC.loader is not None
clean = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(clean)
pc = clean.pc
ex = clean.ex

TARGET = "edge:(229, 231):beta1"
EVENT_FAMILY = (
    "edge:(229, 231):beta1",
    "face_raw:(229, 231, 247):(229, 231)",
)
FAR_PARAMETER = Q(1)
PROTECTED = {
    "stable": [sorted((228, 264, 246)), list(range(17))],
    "unstable": [8, 228, 231, 246],
    "saddles": [[8, 246], [228, 254], [231, 247], [236, 237]],
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def rational_gcd(first, second):
    left = clean.trim(first.c)
    right = clean.trim(second.c)
    while right != [Q(0)]:
        _quotient, remainder = clean.divmod_poly(left, right)
        left, right = right, remainder
    scale = left[-1]
    return ex.P(tuple(value / scale for value in left))


def restrict(path, lo, hi):
    return {
        label: tuple(polynomial.affine(lo, hi) for polynomial in xyz)
        for label, xyz in path.items()
    }


def checkpoint_record(points, faces):
    support, mechanics, centroid, _ledger = clean.checkpoint(
        points, faces, [61, 150, 91]
    )
    return support, mechanics, centroid


def main():
    certificate = json.loads(CERTIFICATE.read_text())
    assert certificate["verdict"] == "EXACT_POST_C17_FIRST_MECHANICS_TRANSFER_PASS"
    assert certificate["winner_status"] == "NONWINNER"
    for relative, expected in certificate["source_hashes"].items():
        assert sha256(ATTACK / relative) == expected

    source = pc.read_rows(SOURCE)
    candidate = pc.read_rows(CANDIDATE)
    faces = json.loads(FACES_PATH.read_text())
    path = clean.line_points(source, candidate)
    rows = list(clean.primitive_rows(path, faces))
    assert len(rows) == 12363
    by_name = {name: (polynomial, family) for name, polynomial, family in rows}
    target = by_name[TARGET][0]
    stored_root = certificate["path"]["root"]
    lo, hi = Q(stored_root["lo"]), Q(stored_root["hi"])
    assert target.exact() == stored_root["polynomial_exact"]
    assert canonical_hash(target.exact()) == stored_root["polynomial_digest"]
    assert pc.root_count(target.c, lo, hi) == 1
    assert target.eval(lo) * target.eval(hi) < 0

    factor = rational_gcd(target, by_name[EVENT_FAMILY[1]][0])
    frozen_audit = certificate["event"]["exact_zero_family_audit"]
    frozen_factor = frozen_audit["shared_algebraic_factor"]
    assert factor.degree == frozen_factor["degree"]
    assert factor.exact() == frozen_factor["exact"]
    assert canonical_hash(factor.exact()) == frozen_factor["digest"]
    isolated = ex.isolate_monotone_root(factor, lo, hi, Q(1, 10**30))
    assert [ex.qs(isolated["lo"]), ex.qs(isolated["hi"])] == frozen_factor[
        "root_interval"
    ]

    strict_count = 0
    strict_leaves = 0
    strict_worst = None
    for name, polynomial, _family in rows:
        if name in EVENT_FAMILY:
            continue
        _sign, leaves, margin = ex.bernstein_sign(
            polynomial, lo, hi, max_depth=60
        )
        strict_count += 1
        strict_leaves += leaves
        strict_worst = margin if strict_worst is None else min(strict_worst, margin)
    assert strict_count == frozen_audit["strict_other_primitive_count"]
    assert strict_leaves == frozen_audit["strict_other_bernstein_leaf_count"]
    assert strict_worst == frozen_audit["strict_other_minimum_bernstein_log10_abs"]

    family_records = {}
    multiplicities = {}
    for name in EVENT_FAMILY:
        polynomial, family = by_name[name]
        count, quotient = clean.multiplicity(polynomial, factor)
        sign, leaves, margin = ex.bernstein_sign(
            quotient, lo, hi, max_depth=60
        )
        multiplicities[name] = count
        family_records[name] = {
            "family": family,
            "polynomial_degree": polynomial.degree,
            "polynomial_digest": canonical_hash(polynomial.exact()),
            "common_factor_multiplicity": count,
            "crosses_sign": count % 2 == 1,
            "quotient_sign": sign,
            "quotient_bernstein_leaf_count": leaves,
            "quotient_minimum_bernstein_log10_abs": margin,
        }
    assert family_records == frozen_audit["family_records"]
    assert multiplicities == frozen_audit["multiplicity_pattern"]

    pre_interval = clean.strict_interval(rows, Q(0), lo)
    post_interval = clean.strict_interval(rows, hi, FAR_PARAMETER)
    assert pre_interval == certificate["open_intervals"]["pre"]["exhaustive"]
    assert post_interval == certificate["open_intervals"]["post"]["exhaustive"]
    pre_cover = ex.certify_path_segment(
        restrict(path, Q(0), lo), faces, PROTECTED
    )
    wall_cover = ex.certify_mechanics_interval(
        path, faces, PROTECTED, lo, hi
    )
    post_cover = ex.certify_path_segment(
        restrict(path, hi, FAR_PARAMETER), faces, PROTECTED
    )
    assert pre_cover == certificate["open_intervals"]["pre"]["class_cover"]
    assert wall_cover == certificate["event"]["wall_mechanics_cover"]
    assert post_cover == certificate["open_intervals"]["post"]["class_cover"]

    points = {
        "source": source,
        "pre": clean.evaluate(path, lo),
        "post": clean.evaluate(path, hi),
        "far": clean.evaluate(path, FAR_PARAMETER),
    }
    checkpoint_summary = {}
    for name, values in points.items():
        support, mechanics, centroid = checkpoint_record(values, faces)
        expected = certificate["rational_checkpoints"][name]
        assert [ex.qs(value) for value in centroid] == expected["exact_centroid"]
        assert mechanics == expected["exact_mechanics"]
        checkpoint_summary[name] = {
            "class": mechanics["class"],
            "strict_support_count": support["strict_support_count"],
        }

    assert pc.read_rows(FAR_PATH) == points["far"]
    for relative, expected in certificate["generated_file_sha256"].items():
        assert sha256(ATTACK / relative) == expected
    source_values = clean.named_values(source, faces)
    far_values = clean.named_values(points["far"], faces)
    ratios = {
        name: far_values[name] / source_values[name] for name in source_values
    }
    assert all(Q(0) < ratio < Q(1) for ratio in ratios.values())
    assert {
        name: ex.qs(value) for name, value in ratios.items()
    } == certificate["directed_residuals"]["target_ratios_exact"]

    receipt = {
        "version": 1,
        "scope": "clean reconstruction of exact post-C17 mechanics transfer",
        "certificate_sha256": sha256(CERTIFICATE),
        "far_sha256": sha256(FAR_PATH),
        "primitive_count": len(rows),
        "strict_other_wall_primitives": strict_count,
        "zero_family": list(EVENT_FAMILY),
        "multiplicity_pattern": multiplicities,
        "checkpoints": checkpoint_summary,
        "target_ratios_exact": {
            name: ex.qs(value) for name, value in ratios.items()
        },
        "verdict": "INDEPENDENT_EXACT_POST_C17_FIRST_MECHANICS_TRANSFER_PASS",
        "winner_status": "NONWINNER",
    }
    OUTPUT.write_text(json.dumps(receipt, indent=2) + "\n")
    print(receipt["verdict"])
    print("winner_status", receipt["winner_status"])
    print("certificate_sha256", receipt["certificate_sha256"])
    print("verification_sha256", sha256(OUTPUT))


if __name__ == "__main__":
    main()
