#!/usr/bin/env python3
"""Locate the first exact primitive wall on the rational full-control ray.

Every support polynomial and every zero-equivalent own-centroid mechanics
primitive is scanned.  Exact Bernstein subdivision is used, so an even-order
touch is not silently missed merely because endpoint signs agree.  This file
is a locator, not the final event certificate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ATTACK = HERE.parents[1]
TRACK = ATTACK.parent
ROOT = HERE.parents[4]
SOURCE = ATTACK / "exact_circuit_far.csv"
FACES_PATH = ATTACK / "exact_circuit_post_faces.json"
ENDPOINT = HERE / "full_control_candidate.csv"
PROPOSAL = HERE / "full_control_proposal.json"
OUTPUT = HERE / "first_event_scan.json"

sys.path.insert(0, str(TRACK / "rigorous_local_bypass"))
import exact_core as ex  # noqa: E402


sys.set_int_max_str_digits(0)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def path_from_endpoints(source, endpoint):
    return {
        label: tuple(
            ex.P((source[label][axis], endpoint[label][axis] - source[label][axis]))
            for axis in range(3)
        )
        for label in source
    }


def primitive_rows(path, faces):
    ledger = ex.mechanics_primitives(path, faces)
    yield "volume_d6", ledger["d6"], "mechanics_denominator"
    for face_index, witness, polynomial in ex.support_polynomials(path, faces):
        yield f"support:f{face_index}:w{witness}", polynomial, "support"
    for face_key, rows in sorted(ledger["reference"].items()):
        for edge, value in sorted(rows.items()):
            yield f"face_reference:{face_key}:{edge}", value, "mechanics_denominator"
    for face_key, rows in sorted(ledger["face"].items()):
        for edge, value in sorted(rows.items()):
            yield f"face_raw:{face_key}:{edge}", value, "face_component"
    for vertex, rows in sorted(ledger["vertex"].items()):
        for neighbor, value in sorted(rows.items()):
            yield f"vertex:{vertex}:{neighbor}", value, "vertex_component"
    for edge, rows in sorted(ledger["edge"].items()):
        for component in (
            "direction_norm2", "gram", "t", "one_minus_t", "beta1", "beta2"
        ):
            yield f"edge:{edge}:{component}", rows[component], "edge_component"


def normalized_coefficients(polynomial, lo, hi, start_sign):
    coefficients = ex.bernstein_coefficients(polynomial.affine(lo, hi))
    return tuple(start_sign * value for value in coefficients)


def strictly_same_sign(polynomial, lo, hi, start_sign, max_depth=30):
    stack = [(lo, hi, 0)]
    leaves = 0
    worst = None
    while stack:
        left, right, depth = stack.pop()
        coefficients = normalized_coefficients(polynomial, left, right, start_sign)
        if all(value > 0 for value in coefficients):
            leaves += 1
            magnitude = min(coefficients)
            log = ex.qlog10(magnitude)
            worst = log if worst is None else min(worst, log)
            continue
        if depth >= max_depth:
            return False, leaves, worst
        middle = (left + right) / 2
        stack.append((middle, right, depth + 1))
        stack.append((left, middle, depth + 1))
    return True, leaves, worst


def first_non_strict_bracket(polynomial, hi, start_sign, depth=72):
    """Return the leftmost dyadic interval not provably of the start sign."""
    stack = [(Q(0), hi, 0)]
    while stack:
        lo, right, level = stack.pop()
        coefficients = normalized_coefficients(polynomial, lo, right, start_sign)
        if all(value > 0 for value in coefficients):
            continue
        if level >= depth:
            return lo, right
        middle = (lo + right) / 2
        # LIFO: append right first so the left interval is examined first.
        stack.append((middle, right, level + 1))
        stack.append((lo, middle, level + 1))
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=str(SOURCE))
    parser.add_argument("--faces", default=str(FACES_PATH))
    parser.add_argument("--endpoint", default=str(ENDPOINT))
    parser.add_argument("--proposal", default=str(PROPOSAL))
    parser.add_argument("--output", default=str(OUTPUT))
    parser.add_argument(
        "--expected-verdict",
        default="FULL_CONTROL_RATIONAL_ACTUAL_CELL_DESCENT_PROPOSAL_PASS",
    )
    args = parser.parse_args()

    def resolve(value):
        path = Path(value)
        return path if path.is_absolute() else HERE / path

    source_path = resolve(args.source)
    faces_path = resolve(args.faces)
    endpoint_path = resolve(args.endpoint)
    proposal_path = resolve(args.proposal)
    output_path = resolve(args.output)
    proposal = json.loads(proposal_path.read_text())
    if proposal["verdict"] != args.expected_verdict:
        raise AssertionError(proposal["verdict"])
    source = ex.read_rows(source_path)
    endpoint = ex.read_rows(endpoint_path)
    if set(source) != set(endpoint):
        raise AssertionError("endpoint labels differ")
    faces = json.loads(faces_path.read_text())
    path = path_from_endpoints(source, endpoint)
    rows = list(primitive_rows(path, faces))
    starts = []
    for name, polynomial, family in rows:
        value = polynomial.eval(Q(0))
        if not value:
            raise AssertionError(("zero primitive at source", name))
        starts.append(1 if value > 0 else -1)

    horizon = Q(2)
    horizon_audits = []
    while horizon <= Q(2**18):
        failures = []
        leaf_count = 0
        worst = None
        for (name, polynomial, family), sign in zip(rows, starts):
            strict, leaves, margin = strictly_same_sign(
                polynomial, Q(0), horizon, sign
            )
            leaf_count += leaves
            if margin is not None:
                worst = margin if worst is None else min(worst, margin)
            if not strict:
                failures.append({"name": name, "family": family})
        horizon_audits.append({
            "horizon": ex.qs(horizon),
            "strict": not failures,
            "failure_count": len(failures),
            "first_failures": failures[:20],
            "proved_leaf_count": leaf_count,
            "minimum_proved_bernstein_log10_abs": worst,
        })
        if failures:
            break
        horizon *= 2
    else:
        raise RuntimeError("no primitive event through configured horizon")

    candidates = []
    for (name, polynomial, family), sign in zip(rows, starts):
        strict, _leaves, _margin = strictly_same_sign(
            polynomial, Q(0), horizon, sign
        )
        if strict:
            continue
        bracket = first_non_strict_bracket(polynomial, horizon, sign)
        if bracket is None:
            raise AssertionError(("failed horizon but no bracket", name))
        lo, hi = bracket
        candidates.append({
            "name": name,
            "family": family,
            "lo": ex.qs(lo),
            "hi": ex.qs(hi),
            "decimal": [float(lo), float(hi)],
            "degree": polynomial.degree,
            "start_sign": sign,
            "value_lo": ex.qs(polynomial.eval(lo)),
            "value_hi": ex.qs(polynomial.eval(hi)),
            "polynomial_exact": polynomial.exact(),
            "polynomial_digest": hashlib.sha256(
                "|".join(polynomial.exact()).encode()
            ).hexdigest(),
        })
    candidates.sort(key=lambda row: (Q(row["lo"]), Q(row["hi"]), row["name"]))
    if not candidates:
        raise AssertionError("no candidate event")
    first_lo = Q(candidates[0]["lo"])
    first_hi = Q(candidates[0]["hi"])
    tied = [
        row for row in candidates
        if Q(row["lo"]) <= first_hi and Q(row["hi"]) >= first_lo
    ]

    payload = {
        "version": 1,
        "scope": "exact-Bernstein exhaustive first-event locator on full-control rational ray",
        "source_hashes": {
            str(source_path.relative_to(ROOT)): sha256(source_path),
            str(faces_path.relative_to(ROOT)): sha256(faces_path),
            str(endpoint_path.relative_to(ROOT)): sha256(endpoint_path),
            str(proposal_path.relative_to(ROOT)): sha256(proposal_path),
        },
        "primitive_count": len(rows),
        "family_counts": {
            family: sum(1 for _name, _poly, item in rows if item == family)
            for family in sorted({family for _name, _poly, family in rows})
        },
        "horizon_audits": horizon_audits,
        "search_horizon": ex.qs(horizon),
        "candidate_count": len(candidates),
        "first_candidate": candidates[0],
        "overlapping_first_candidates": tied,
        "next_candidates": candidates[:20],
        "verdict": "EXHAUSTIVE_EXACT_FIRST_EVENT_LOCATOR_PASS",
    }
    output_path.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "verdict": payload["verdict"],
        "primitive_count": payload["primitive_count"],
        "family_counts": payload["family_counts"],
        "search_horizon": payload["search_horizon"],
        "first_candidate": payload["first_candidate"],
        "overlapping_first_candidates": payload["overlapping_first_candidates"],
        "output": str(output_path),
    }, indent=2))


if __name__ == "__main__":
    main()
