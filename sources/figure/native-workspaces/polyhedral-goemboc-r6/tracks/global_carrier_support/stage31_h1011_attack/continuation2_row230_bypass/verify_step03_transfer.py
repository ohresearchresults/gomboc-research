#!/usr/bin/env python3
"""Independent reconstruction of the first post-bypass mechanics transfer."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
ATTACK = HERE.parent
TRACK = ATTACK.parent
ROOT = HERE.parents[4]
SOURCE = HERE / "step02_candidate.csv"
UNIT_ENDPOINT = HERE / "step03_candidate.csv"
FACES_PATH = ATTACK / "continuation" / "main" / "exact_full_control_chain_post_faces.json"
PROPOSAL = HERE / "step03_proposal.json"
SCAN = HERE / "step03_event_scan.json"
CERTIFICATE = HERE / "step03_transfer_certificate.json"
FAR_PATH = HERE / "step03_transfer_far.csv"
OUTPUT = HERE / "step03_transfer_verification.json"

sys.path.insert(0, str(TRACK / "rigorous_local_bypass"))
import exact_core as ex  # noqa: E402
sys.path.insert(0, str(ATTACK))
import build_exact_circuit_flip as residual_core  # noqa: E402
sys.path.insert(0, str(HERE))
import verify_fixed_cell_step as clean  # noqa: E402


TARGET = "edge:(249, 250):beta2"
ZERO_FAMILY = {
    "edge:(249, 250):beta2",
    "face_raw:(224, 249, 250):(249, 250)",
}
FAR = Q(3)
ROOT_WIDTH = Q(1, 10**30)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def trim(coefficients):
    coefficients = list(coefficients)
    while len(coefficients) > 1 and coefficients[-1] == 0:
        coefficients.pop()
    return coefficients or [Q(0)]


def remainder(left, right):
    left = trim(left)
    right = trim(right)
    assert right != [Q(0)]
    while len(left) >= len(right) and left != [Q(0)]:
        shift = len(left) - len(right)
        scale = left[-1] / right[-1]
        for index, coefficient in enumerate(right):
            left[index + shift] -= scale * coefficient
        left = trim(left)
    return left


def rational_gcd(first, second):
    a, b = trim(first.c), trim(second.c)
    while b != [Q(0)]:
        a, b = b, remainder(a, b)
    scale = a[-1]
    return ex.P(tuple(value / scale for value in a))


def restrict(path, lo, hi):
    return {
        label: tuple(polynomial.affine(lo, hi) for polynomial in xyz)
        for label, xyz in path.items()
    }


def evaluate(path, parameter):
    return {
        label: tuple(polynomial.eval(parameter) for polynomial in xyz)
        for label, xyz in path.items()
    }


def strict_receipt(rows, lo, hi, excluded=()):
    excluded = set(excluded)
    digest = hashlib.sha256()
    count = 0
    leaves = 0
    worst = None
    for name, polynomial, family in rows:
        if name in excluded:
            continue
        midpoint_value = polynomial.eval((lo + hi) / 2)
        assert midpoint_value != 0
        expected = 1 if midpoint_value > 0 else -1
        sign, row_leaves, margin = ex.bernstein_sign(
            polynomial, lo, hi, max_depth=60
        )
        assert sign == expected
        count += 1
        leaves += row_leaves
        worst = margin if worst is None else min(worst, margin)
        digest.update(
            f"{name}|{family}|{sign}|{'|'.join(polynomial.exact())}\n".encode()
        )
    return {
        "lo": ex.qs(lo),
        "hi": ex.qs(hi),
        "excluded_zero_family": sorted(excluded),
        "primitive_count": count,
        "bernstein_leaf_count": leaves,
        "minimum_bernstein_log10_abs": worst,
        "primitive_digest": digest.hexdigest(),
    }


def residual_receipt(path, faces):
    source = evaluate(path, Q(0))
    far = evaluate(path, FAR)
    result = {}
    for name in clean.TARGETS:
        before = residual_core.selected_residual_record(source, faces, name)
        after = residual_core.selected_residual_record(far, faces, name)
        before_value = Q(before["squared_value"])
        after_value = Q(after["squared_value"])
        assert after_value < before_value
        numerator, denominator = residual_core.selected_fraction_polynomials(
            path, faces, name
        )
        derivative = (
            numerator.derivative() * denominator
            - numerator * denominator.derivative()
        )
        sign, leaves, worst = ex.bernstein_sign(
            derivative, Q(0), FAR, max_depth=60
        )
        assert sign == -1
        result[name] = {
            "source": before,
            "far": after,
            "exact_squared_drop": ex.qs(before_value - after_value),
            "derivative_sign": sign,
            "derivative_degree": derivative.degree,
            "derivative_bernstein_leaf_count": leaves,
            "derivative_minimum_bernstein_log10_abs": worst,
            "derivative_digest": canonical_hash(derivative.exact()),
        }
    return result


def row230_receipt(path, faces):
    result = {}
    for face_index, witness, support in ex.support_polynomials(path, faces):
        family = (frozenset(faces[face_index]), witness)
        if family not in clean.DANGER:
            continue
        normal = ex.cycle_normal(faces[face_index], path)
        norm2 = ex.norm2(normal)
        square = support * support
        derivative = square.derivative() * norm2 - square * norm2.derivative()
        sign, leaves, worst = ex.bernstein_sign(
            derivative, Q(0), FAR, max_depth=60
        )
        assert sign == 1
        before = square.eval(Q(0)) / norm2.eval(Q(0))
        after = square.eval(FAR) / norm2.eval(FAR)
        assert after > before
        result[f"{sorted(family[0])}|{witness}"] = {
            "source_squared_normalized_margin": ex.qs(before),
            "far_squared_normalized_margin": ex.qs(after),
            "derivative_sign": sign,
            "derivative_degree": derivative.degree,
            "derivative_bernstein_leaf_count": leaves,
            "derivative_minimum_bernstein_log10_abs": worst,
            "derivative_digest": canonical_hash(derivative.exact()),
        }
    assert len(result) == 2
    return result


def h910_receipt(path, faces):
    rows = ex.mechanics_primitives(path, faces)["edge"][(9, 10)]
    components = ("t", "one_minus_t", "beta1", "beta2")
    witness = min(components, key=lambda name: rows[name].eval(Q(0)))
    polynomial = rows[witness]
    sign, leaves, worst = ex.bernstein_sign(
        polynomial, Q(0), FAR, max_depth=60
    )
    assert sign == -1
    return {
        "component": witness,
        "source": ex.qs(polynomial.eval(Q(0))),
        "far": ex.qs(polynomial.eval(FAR)),
        "sign": sign,
        "bernstein_leaf_count": leaves,
        "minimum_bernstein_log10_abs": worst,
        "polynomial_degree": polynomial.degree,
        "polynomial_digest": canonical_hash(polynomial.exact()),
    }


def main():
    global SOURCE, UNIT_ENDPOINT, FACES_PATH, PROPOSAL, SCAN, CERTIFICATE, FAR_PATH, OUTPUT, FAR
    global TARGET, ZERO_FAMILY

    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=str(SOURCE))
    parser.add_argument("--endpoint", default=str(UNIT_ENDPOINT))
    parser.add_argument("--faces", default=str(FACES_PATH))
    parser.add_argument("--proposal", default=str(PROPOSAL))
    parser.add_argument("--scan", default=str(SCAN))
    parser.add_argument("--certificate", default=str(CERTIFICATE))
    parser.add_argument("--far", dest="far_path", default=str(FAR_PATH))
    parser.add_argument("--output", default=str(OUTPUT))
    parser.add_argument("--target", required=True)
    parser.add_argument("--zero-family", action="append", required=True)
    parser.add_argument("--interpretation", required=True)
    parser.add_argument(
        "--expected-verdict",
        default="EXACT_ROW230_BYPASS_FIRST_MECHANICS_TRANSFER_PASS",
    )
    parser.add_argument(
        "--receipt-verdict",
        default="INDEPENDENT_EXACT_ROW230_BYPASS_FIRST_MECHANICS_TRANSFER_PASS",
    )
    args = parser.parse_args()

    def resolve(value):
        path = Path(value)
        return path if path.is_absolute() else HERE / path

    SOURCE = resolve(args.source)
    UNIT_ENDPOINT = resolve(args.endpoint)
    FACES_PATH = resolve(args.faces)
    PROPOSAL = resolve(args.proposal)
    SCAN = resolve(args.scan)
    CERTIFICATE = resolve(args.certificate)
    FAR_PATH = resolve(args.far_path)
    OUTPUT = resolve(args.output)
    TARGET = args.target
    ZERO_FAMILY = set(args.zero_family)
    if TARGET not in ZERO_FAMILY:
        raise ValueError("target must belong to the declared zero family")
    if len(ZERO_FAMILY) != len(args.zero_family) or len(ZERO_FAMILY) < 2:
        raise ValueError("zero family must contain at least two distinct primitives")

    frozen = json.loads(CERTIFICATE.read_text())
    assert frozen["verdict"] == args.expected_verdict
    assert frozen["path"]["root"]["target"] == TARGET
    assert frozen["event"]["zero_family"] == sorted(ZERO_FAMILY)
    assert frozen["event"]["interpretation"] == args.interpretation
    FAR = Q(frozen["path"]["far_parameter"])
    assert FAR > 0
    for file in (SOURCE, UNIT_ENDPOINT, FACES_PATH, PROPOSAL, SCAN):
        key = str(file.relative_to(ROOT))
        assert sha256(file) == frozen["source_hashes"][key]

    source = ex.read_rows(SOURCE)
    unit_endpoint = ex.read_rows(UNIT_ENDPOINT)
    faces = json.loads(FACES_PATH.read_text())
    path = clean.build_path(source, unit_endpoint)
    assert canonical_hash({
        str(label): [
            ex.qs(unit_endpoint[label][axis] - source[label][axis])
            for axis in range(3)
        ]
        for label in sorted(source)
    }) == frozen["path"]["unit_delta_digest"]
    assert frozen["path"]["far_parameter"] == ex.qs(FAR)

    rows = list(clean.enumerate_primitives(path, faces))
    assert len(rows) == 7904
    lookup = {name: polynomial for name, polynomial, _family in rows}
    target = lookup[TARGET]
    stored_root = frozen["path"]["root"]
    assert target.exact() == stored_root["polynomial_exact"]
    assert canonical_hash(target.exact()) == stored_root["polynomial_digest"]
    root = ex.isolate_monotone_root(
        target, Q(stored_root["lo"]), Q(stored_root["hi"]), ROOT_WIDTH
    )
    assert ex.qs(root["lo"]) == stored_root["lo"]
    assert ex.qs(root["hi"]) == stored_root["hi"]
    assert ex.qs(root["value_lo"]) == stored_root["value_lo"]
    assert ex.qs(root["value_hi"]) == stored_root["value_hi"]
    assert root["derivative_sign"] == stored_root["derivative_sign"]
    assert Q(0) < root["lo"] < root["hi"] < FAR

    shared = {}
    for name in sorted(ZERO_FAMILY):
        polynomial = lookup[name]
        gcd = rational_gcd(target, polynomial)
        assert gcd.degree >= 1
        isolated = ex.isolate_monotone_root(
            gcd, root["lo"], root["hi"], ROOT_WIDTH
        )
        shared[name] = {
            "polynomial_degree": polynomial.degree,
            "polynomial_digest": canonical_hash(polynomial.exact()),
            "gcd_degree": gcd.degree,
            "gcd_exact": gcd.exact(),
            "gcd_digest": canonical_hash(gcd.exact()),
            "gcd_root_interval": [ex.qs(isolated["lo"]), ex.qs(isolated["hi"])],
        }
    assert shared == frozen["event"]["shared_algebraic_factor"]

    intervals = {
        "pre": strict_receipt(rows, Q(0), root["lo"]),
        "wall_other_primitives": strict_receipt(
            rows, root["lo"], root["hi"], ZERO_FAMILY
        ),
        "post": strict_receipt(rows, root["hi"], FAR),
    }
    assert intervals == frozen["exact_intervals"]
    covers = {
        "pre": ex.certify_path_segment(
            restrict(path, Q(0), root["lo"]), faces, clean.PROTECTED
        ),
        "wall": ex.certify_mechanics_interval(
            path, faces, clean.PROTECTED, root["lo"], root["hi"]
        ),
        "post": ex.certify_path_segment(
            restrict(path, root["hi"], FAR), faces, clean.PROTECTED
        ),
    }
    assert covers == frozen["class_covers"]

    far = evaluate(path, FAR)
    assert ex.read_rows(FAR_PATH) == far
    assert sha256(FAR_PATH) == frozen["generated_file_sha256"][str(FAR_PATH.relative_to(ROOT))]
    assert clean.point_receipt(source, faces) == frozen["checkpoints"]["source"]
    assert clean.point_receipt(far, faces) == frozen["checkpoints"]["far"]
    actual_residuals = residual_receipt(path, faces)
    assert actual_residuals == frozen["directed_residuals"]
    assert row230_receipt(path, faces) == frozen["row230_strict_inward_certificate"]
    assert h910_receipt(path, faces) == frozen["h910_nonresurrection"]

    receipt = {
        "version": 1,
        "certificate_sha256": sha256(CERTIFICATE),
        "far_sha256": sha256(FAR_PATH),
        "primitive_count": len(rows),
        "strict_other_wall_primitives": intervals["wall_other_primitives"]["primitive_count"],
        "zero_family": sorted(ZERO_FAMILY),
        "own_centroid_reconstructed": True,
        "active_rows": 61,
        "forced_rails": 37,
        "pre_class": [2, 2, 2],
        "post_class": [2, 2, 2],
        "h910_strictly_negative": True,
        "far_decisions": {
            name: row["far"]["decision_value"]
            for name, row in actual_residuals.items()
        },
        "verdict": args.receipt_verdict,
    }
    OUTPUT.write_text(json.dumps(receipt, indent=2) + "\n")
    print(receipt["verdict"])


if __name__ == "__main__":
    main()
