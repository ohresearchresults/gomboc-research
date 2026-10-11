#!/usr/bin/env python3
"""Exactify the first genuine mechanics transfer on the third rechart ray."""
from __future__ import annotations

import argparse
import csv
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
OUTPUT = HERE / "step03_transfer_certificate.json"
FAR_OUT = HERE / "step03_transfer_far.csv"

sys.path.insert(0, str(TRACK / "rigorous_local_bypass"))
import exact_core as ex  # noqa: E402
sys.path.insert(0, str(ATTACK))
import build_exact_circuit_flip as residual_core  # noqa: E402
sys.path.insert(0, str(HERE))
import certify_fixed_cell_step as fixed  # noqa: E402


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


def trim(values):
    values = list(values)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return values or [Q(0)]


def poly_remainder(left, right):
    left = trim(left)
    right = trim(right)
    if right == [Q(0)]:
        raise ZeroDivisionError
    while len(left) >= len(right) and left != [Q(0)]:
        shift = len(left) - len(right)
        scale = left[-1] / right[-1]
        for index, coefficient in enumerate(right):
            left[index + shift] -= scale * coefficient
        left = trim(left)
    return left


def monic_gcd(first, second):
    left, right = trim(first.c), trim(second.c)
    while right != [Q(0)]:
        left, right = right, poly_remainder(left, right)
    scale = left[-1]
    return ex.P(tuple(value / scale for value in left))


def restrict(path, lo, hi):
    return {
        label: tuple(polynomial.affine(lo, hi) for polynomial in xyz)
        for label, xyz in path.items()
    }


def point(path, parameter):
    return {
        label: tuple(polynomial.eval(parameter) for polynomial in xyz)
        for label, xyz in path.items()
    }


def write_rows(path, rows):
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(("source_id", "x", "y", "z"))
        for label in sorted(rows):
            writer.writerow((label, *(ex.qs(value) for value in rows[label])))


def strict_rows(rows, lo, hi, excluded=()):
    excluded = set(excluded)
    digest = hashlib.sha256()
    count = 0
    leaves = 0
    worst = None
    for name, polynomial, family in rows:
        if name in excluded:
            continue
        midpoint = (lo + hi) / 2
        value = polynomial.eval(midpoint)
        if value == 0:
            raise AssertionError(("unexpected midpoint zero", name))
        expected = 1 if value > 0 else -1
        sign, row_leaves, margin = ex.bernstein_sign(
            polynomial, lo, hi, max_depth=60
        )
        if sign != expected:
            raise AssertionError((name, expected, sign))
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


def residuals(path, faces):
    before = point(path, Q(0))
    after = point(path, FAR)
    output = {}
    for name in fixed.TARGETS:
        source_record = residual_core.selected_residual_record(before, faces, name)
        far_record = residual_core.selected_residual_record(after, faces, name)
        source_value = Q(source_record["squared_value"])
        far_value = Q(far_record["squared_value"])
        if not far_value < source_value:
            raise AssertionError((name, source_value, far_value))
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
        if sign != -1:
            raise AssertionError((name, "not decreasing to far", sign))
        output[name] = {
            "source": source_record,
            "far": far_record,
            "exact_squared_drop": ex.qs(source_value - far_value),
            "derivative_sign": sign,
            "derivative_degree": derivative.degree,
            "derivative_bernstein_leaf_count": leaves,
            "derivative_minimum_bernstein_log10_abs": worst,
            "derivative_digest": canonical_hash(derivative.exact()),
        }
    return output


def danger(path, faces):
    output = {}
    for face_index, witness, support in ex.support_polynomials(path, faces):
        family = (frozenset(faces[face_index]), witness)
        if family not in fixed.DANGER:
            continue
        normal = ex.cycle_normal(faces[face_index], path)
        norm2 = ex.norm2(normal)
        square = support * support
        derivative = square.derivative() * norm2 - square * norm2.derivative()
        sign, leaves, worst = ex.bernstein_sign(
            derivative, Q(0), FAR, max_depth=60
        )
        if sign != 1:
            raise AssertionError((family, "row-230 margin not increasing"))
        source_value = square.eval(Q(0)) / norm2.eval(Q(0))
        far_value = square.eval(FAR) / norm2.eval(FAR)
        if not far_value > source_value:
            raise AssertionError((family, source_value, far_value))
        output[f"{sorted(family[0])}|{witness}"] = {
            "source_squared_normalized_margin": ex.qs(source_value),
            "far_squared_normalized_margin": ex.qs(far_value),
            "derivative_sign": sign,
            "derivative_degree": derivative.degree,
            "derivative_bernstein_leaf_count": leaves,
            "derivative_minimum_bernstein_log10_abs": worst,
            "derivative_digest": canonical_hash(derivative.exact()),
        }
    if len(output) != 2:
        raise AssertionError(output)
    return output


def h910(path, faces):
    rows = ex.mechanics_primitives(path, faces)["edge"][(9, 10)]
    components = ("t", "one_minus_t", "beta1", "beta2")
    witness = min(components, key=lambda name: rows[name].eval(Q(0)))
    polynomial = rows[witness]
    sign, leaves, worst = ex.bernstein_sign(
        polynomial, Q(0), FAR, max_depth=60
    )
    if sign != -1:
        raise AssertionError("H910 resurrects before far")
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
    global SOURCE, UNIT_ENDPOINT, FACES_PATH, PROPOSAL, SCAN, OUTPUT, FAR_OUT, FAR
    global TARGET, ZERO_FAMILY

    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=str(SOURCE))
    parser.add_argument("--endpoint", default=str(UNIT_ENDPOINT))
    parser.add_argument("--faces", default=str(FACES_PATH))
    parser.add_argument("--proposal", default=str(PROPOSAL))
    parser.add_argument("--scan", default=str(SCAN))
    parser.add_argument("--output", default=str(OUTPUT))
    parser.add_argument("--far-output", default=str(FAR_OUT))
    parser.add_argument("--far", default=ex.qs(FAR))
    parser.add_argument("--target", required=True)
    parser.add_argument("--zero-family", action="append", required=True)
    parser.add_argument("--interpretation", required=True)
    parser.add_argument(
        "--verdict",
        default="EXACT_ROW230_BYPASS_FIRST_MECHANICS_TRANSFER_PASS",
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
    OUTPUT = resolve(args.output)
    FAR_OUT = resolve(args.far_output)
    FAR = Q(args.far)
    if FAR <= 0:
        raise ValueError("far parameter must be positive")
    TARGET = args.target
    ZERO_FAMILY = set(args.zero_family)
    if TARGET not in ZERO_FAMILY:
        raise ValueError("target must belong to the declared zero family")
    if len(ZERO_FAMILY) != len(args.zero_family) or len(ZERO_FAMILY) < 2:
        raise ValueError("zero family must contain at least two distinct primitives")

    proposal = json.loads(PROPOSAL.read_text())
    scan = json.loads(SCAN.read_text())
    if proposal["verdict"] != "ROW230_FULL_CONTROL_RATIONAL_RECHART_PROPOSAL_PASS":
        raise AssertionError(proposal["verdict"])
    if scan["verdict"] != "EXHAUSTIVE_EXACT_FIRST_EVENT_LOCATOR_PASS":
        raise AssertionError(scan["verdict"])
    if scan["first_candidate"]["name"] != TARGET:
        raise AssertionError(scan["first_candidate"]["name"])
    if {row["name"] for row in scan["overlapping_first_candidates"]} != ZERO_FAMILY:
        raise AssertionError(scan["overlapping_first_candidates"])

    source = ex.read_rows(SOURCE)
    unit_endpoint = ex.read_rows(UNIT_ENDPOINT)
    faces = json.loads(FACES_PATH.read_text())
    path = fixed.affine_path(source, unit_endpoint)
    rows = list(fixed.primitive_rows(path, faces))
    if len(rows) != 7904:
        raise AssertionError(len(rows))
    lookup = {name: polynomial for name, polynomial, _family in rows}
    target = lookup[TARGET]
    candidate = scan["first_candidate"]
    root = ex.isolate_monotone_root(
        target, Q(candidate["lo"]), Q(candidate["hi"]), ROOT_WIDTH
    )
    if not Q(0) < root["lo"] < root["hi"] < FAR:
        raise AssertionError(root)

    shared = {}
    for name in sorted(ZERO_FAMILY):
        polynomial = lookup[name]
        gcd = monic_gcd(target, polynomial)
        if gcd.degree < 1:
            raise AssertionError((name, "no common exact factor"))
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

    pre_interval = strict_rows(rows, Q(0), root["lo"])
    wall_interval = strict_rows(rows, root["lo"], root["hi"], ZERO_FAMILY)
    post_interval = strict_rows(rows, root["hi"], FAR)
    pre_cover = ex.certify_path_segment(
        restrict(path, Q(0), root["lo"]), faces, fixed.PROTECTED
    )
    wall_cover = ex.certify_mechanics_interval(
        path, faces, fixed.PROTECTED, root["lo"], root["hi"]
    )
    post_cover = ex.certify_path_segment(
        restrict(path, root["hi"], FAR), faces, fixed.PROTECTED
    )
    for cover in (pre_cover, wall_cover, post_cover):
        key = "midpoint_class" if "midpoint_class" in cover else "start_class"
        if cover[key]["class"] != [2, 2, 2]:
            raise AssertionError(cover)

    source_checkpoint = fixed.checkpoint(source, faces)
    far = point(path, FAR)
    far_checkpoint = fixed.checkpoint(far, faces)
    write_rows(FAR_OUT, far)
    certificate = {
        "version": 1,
        "type": "exact class-preserving own-centroid mechanics transfer",
        "scope": (
            f"The full-support rechart from t=0 through rational t={ex.qs(FAR)}, "
            f"including the exact mechanics transfer near t={float(root['lo']):.17g}; all "
            "other support/four-cone primitives stay strict, 61 rows/base/U8/rails "
            "survive, H910 stays negative and all directed residuals decrease."
        ),
        "source_hashes": {
            str(file.relative_to(ROOT)): sha256(file)
            for file in (SOURCE, UNIT_ENDPOINT, FACES_PATH, PROPOSAL, SCAN)
        },
        "path": {
            "unit_delta_digest": canonical_hash({
                str(label): [
                    ex.qs(unit_endpoint[label][axis] - source[label][axis])
                    for axis in range(3)
                ]
                for label in sorted(source)
            }),
            "far_parameter": ex.qs(FAR),
            "root": {
                "target": TARGET,
                "lo": ex.qs(root["lo"]),
                "hi": ex.qs(root["hi"]),
                "value_lo": ex.qs(root["value_lo"]),
                "value_hi": ex.qs(root["value_hi"]),
                "decimal_interval": [float(root["lo"]), float(root["hi"])],
                "derivative_sign": root["derivative_sign"],
                "polynomial_degree": target.degree,
                "polynomial_exact": target.exact(),
                "polynomial_digest": canonical_hash(target.exact()),
            },
        },
        "event": {
            "zero_family": sorted(ZERO_FAMILY),
            "shared_algebraic_factor": shared,
            "interpretation": args.interpretation,
            "pre_f_vector": [61, 162, 103],
            "wall_f_vector": [61, 162, 103],
            "post_f_vector": [61, 162, 103],
            "pre_class": [2, 2, 2],
            "post_class": [2, 2, 2],
        },
        "exact_intervals": {
            "pre": pre_interval,
            "wall_other_primitives": wall_interval,
            "post": post_interval,
        },
        "class_covers": {
            "pre": pre_cover,
            "wall": wall_cover,
            "post": post_cover,
        },
        "checkpoints": {
            "source": source_checkpoint,
            "far": far_checkpoint,
        },
        "directed_residuals": residuals(path, faces),
        "row230_strict_inward_certificate": danger(path, faces),
        "h910_nonresurrection": h910(path, faces),
        "generated_file_sha256": {
            str(FAR_OUT.relative_to(ROOT)): sha256(FAR_OUT),
        },
        "residual_verdict": {
            "winner": False,
            "far_class": [2, 2, 2],
            "next_action": f"rebuild the full-support chart from {FAR_OUT.name}",
        },
        "verdict": args.verdict,
    }
    OUTPUT.write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps({
        "verdict": certificate["verdict"],
        "root": certificate["path"]["root"]["decimal_interval"],
        "far_decisions": {
            name: row["far"]["decision_value"]
            for name, row in certificate["directed_residuals"].items()
        },
        "far": str(FAR_OUT),
    }, indent=2))


if __name__ == "__main__":
    main()
