#!/usr/bin/env python3
"""Diagnose the literal exact event ordering of a proposed relay epoch.

This is deliberately separate from :mod:`locate_epoch`: the locator remains
fail-closed and accepts only an epoch on which every non-target primitive is
strict.  This diagnostic explains a rejected proposal by finding every
primitive that cannot retain its source sign, isolating its leftmost root, and
ordering those roots against the intended relay alias.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

import relay_common as rc


BRACKET_DEPTH = 80
ROOT_WIDTH = Q(1, 10**30)


def phase_paths(phase: str):
    if phase == "birth":
        return (
            rc.SOURCE,
            rc.HERE / "post_birth_checkpoint.csv",
            rc.HERE / "birth_proposal.json",
        )
    return (
        rc.HERE / "post_birth_checkpoint.csv",
        rc.HERE / "far_u1.csv",
        rc.HERE / "death_proposal.json",
    )


def signed(value: Q) -> int:
    return (value > 0) - (value < 0)


def normalized_bernstein(polynomial, lo: Q, hi: Q, start_sign: int):
    return tuple(
        start_sign * value
        for value in rc.ex.bernstein_coefficients(polynomial.affine(lo, hi))
    )


def leftmost_non_strict_bracket(polynomial, start_sign: int):
    """Return the leftmost depth-80 cell not proved to retain start_sign."""
    stack = [(Q(0), Q(1), 0)]
    while stack:
        lo, hi, depth = stack.pop()
        if all(value > 0 for value in normalized_bernstein(
            polynomial, lo, hi, start_sign
        )):
            continue
        if depth >= BRACKET_DEPTH:
            return lo, hi
        middle = (lo + hi) / 2
        # LIFO: visit the left interval first.
        stack.append((middle, hi, depth + 1))
        stack.append((lo, middle, depth + 1))
    return None


def poly_trim(coefficients):
    values = list(coefficients)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return values or [Q(0)]


def poly_derivative(coefficients):
    return poly_trim([
        degree * coefficient
        for degree, coefficient in enumerate(coefficients)
        if degree
    ] or [Q(0)])


def poly_value(coefficients, value: Q):
    result = Q(0)
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def poly_remainder(numerator, denominator):
    numerator = poly_trim(numerator)
    denominator = poly_trim(denominator)
    if denominator == [Q(0)]:
        raise ZeroDivisionError("zero polynomial")
    while len(numerator) >= len(denominator) and numerator != [Q(0)]:
        shift = len(numerator) - len(denominator)
        factor = numerator[-1] / denominator[-1]
        for index, coefficient in enumerate(denominator):
            numerator[index + shift] -= factor * coefficient
        numerator = poly_trim(numerator)
    return numerator


def sturm_sequence(coefficients):
    sequence = [poly_trim(coefficients), poly_derivative(coefficients)]
    while sequence[-1] != [Q(0)]:
        remainder = poly_remainder(sequence[-2], sequence[-1])
        if remainder == [Q(0)]:
            break
        sequence.append([-value for value in remainder])
    return sequence


def sturm_variations(sequence, value: Q):
    signs = []
    for polynomial in sequence:
        evaluated = poly_value(polynomial, value)
        if evaluated:
            signs.append(signed(evaluated))
    return sum(left != right for left, right in zip(signs, signs[1:]))


def sturm_root_count(sequence, lo: Q, hi: Q):
    return sturm_variations(sequence, lo) - sturm_variations(sequence, hi)


def root_record(name, polynomial, family, bracket):
    lo, hi = bracket
    value_lo = polynomial.eval(lo)
    value_hi = polynomial.eval(hi)
    if not value_lo or not value_hi:
        raise AssertionError((name, "rational root lies on diagnostic bracket"))
    sturm = sturm_sequence(polynomial.c)
    before_count = sturm_root_count(sturm, Q(0), lo)
    bracket_count = sturm_root_count(sturm, lo, hi)
    total_count = sturm_root_count(sturm, Q(0), Q(1))
    if before_count != 0 or bracket_count != 1:
        raise AssertionError((
            name,
            "leftmost bracket is not a single first root",
            before_count,
            bracket_count,
        ))
    root = rc.ex.isolate_monotone_root(polynomial, lo, hi, ROOT_WIDTH)
    return {
        "name": name,
        "family": family,
        "degree": polynomial.degree,
        "start_sign": signed(polynomial.eval(Q(0))),
        "end_sign": signed(polynomial.eval(Q(1))),
        "diagnostic_bracket": [rc.ex.qs(lo), rc.ex.qs(hi)],
        "root_interval": [rc.ex.qs(root["lo"]), rc.ex.qs(root["hi"])],
        "decimal_interval": [float(root["lo"]), float(root["hi"])],
        "value_lo": rc.ex.qs(root["value_lo"]),
        "value_hi": rc.ex.qs(root["value_hi"]),
        "derivative_sign": root["derivative_sign"],
        "derivative_bernstein_leaves": root["derivative_bernstein_leaves"],
        "sturm_root_count_before_interval": before_count,
        "sturm_root_count_in_interval": bracket_count,
        "sturm_root_count_on_unit_epoch": total_count,
        "polynomial_digest": rc.canonical_hash(polynomial.exact()),
    }


def main() -> None:
    diagnostic_path = Path(__file__).resolve()
    locator_path = rc.HERE / "locate_epoch.py"
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", choices=("birth", "death"), required=True)
    args = parser.parse_args()
    phase = args.phase
    source_path, endpoint_path, proposal_path = phase_paths(phase)
    output_path = rc.HERE / f"{phase}_ordering_diagnosis.json"
    proposal = json.loads(proposal_path.read_text())
    expected_verdict = f"RATIONAL_FULL_SUPPORT_{phase.upper()}_PROPOSAL_PASS"
    if proposal.get("verdict") != expected_verdict:
        raise AssertionError(("proposal verdict", proposal.get("verdict")))
    if rc.sha256(source_path) != proposal["source_hashes"][rc.relative(source_path)]:
        raise AssertionError("proposal source binding drift")
    if rc.sha256(endpoint_path) != proposal["exact_endpoint"]["sha256"]:
        raise AssertionError("proposal endpoint binding drift")

    source = rc.ex.read_rows(source_path)
    endpoint = rc.ex.read_rows(endpoint_path)
    faces = json.loads(rc.FACES.read_text())
    rows = list(rc.primitive_rows(rc.affine_path(source, endpoint), faces))
    if len(rows) != 7922:
        raise AssertionError(("primitive count", len(rows)))

    candidates = []
    strict_count = 0
    family_counts = {}
    for name, polynomial, family in rows:
        family_counts[family] = family_counts.get(family, 0) + 1
        start_sign = signed(polynomial.eval(Q(0)))
        if not start_sign:
            raise AssertionError(("zero primitive at source", name))
        try:
            sign, _leaves, _margin = rc.ex.bernstein_sign(
                polynomial, Q(0), Q(1), max_depth=60
            )
            if sign != start_sign:
                raise AssertionError(("strict sign drift", name, start_sign, sign))
            strict_count += 1
            continue
        except AssertionError:
            bracket = leftmost_non_strict_bracket(polynomial, start_sign)
            if bracket is None:
                # A depth-60 proof failure that resolves by depth 80 is strict.
                sign, _leaves, _margin = rc.ex.bernstein_sign(
                    polynomial, Q(0), Q(1), max_depth=BRACKET_DEPTH
                )
                if sign != start_sign:
                    raise AssertionError(("late strict sign drift", name))
                strict_count += 1
                continue
            candidates.append(root_record(name, polynomial, family, bracket))

    candidates.sort(key=lambda row: (Q(row["root_interval"][0]), row["name"]))
    aliases = set(rc.ALIASES[phase])
    target_rows = [row for row in candidates if row["name"] in aliases]
    if {row["name"] for row in target_rows} != aliases:
        raise AssertionError(("target candidate family", target_rows))
    if len({row["polynomial_digest"] for row in target_rows}) != 1:
        raise AssertionError("target aliases do not share one exact polynomial")
    target = target_rows[0]
    target_lo = Q(target["root_interval"][0])
    preceding = [
        row for row in candidates
        if Q(row["root_interval"][1]) < target_lo
    ]
    first = candidates[0]
    first_lo, first_hi = map(Q, first["root_interval"])
    first_family = [
        row for row in candidates
        if Q(row["root_interval"][0]) <= first_hi
        and Q(row["root_interval"][1]) >= first_lo
    ]
    candidate_digest = hashlib.sha256(
        "".join(
            f'{row["name"]}|{row["polynomial_digest"]}|'
            f'{row["root_interval"][0]}|{row["root_interval"][1]}\n'
            for row in candidates
        ).encode()
    ).hexdigest()
    payload = {
        "version": 1,
        "phase": phase,
        "scope": (
            "Exact exhaustive ordering diagnosis over the same 7,922 primitive "
            "family as locate_epoch.py. This diagnoses a rejected proposal and "
            "does not accept an event."
        ),
        "source_hashes": {
            rc.relative(source_path): rc.sha256(source_path),
            rc.relative(endpoint_path): rc.sha256(endpoint_path),
            rc.relative(rc.FACES): rc.sha256(rc.FACES),
            rc.relative(proposal_path): rc.sha256(proposal_path),
            rc.relative(rc.EXACT_CORE): rc.sha256(rc.EXACT_CORE),
            rc.relative(locator_path): rc.sha256(locator_path),
            rc.relative(diagnostic_path): rc.sha256(diagnostic_path),
        },
        "primitive_count": len(rows),
        "family_counts": family_counts,
        "strict_whole_epoch_count": strict_count,
        "root_candidate_count": len(candidates),
        "candidate_digest": candidate_digest,
        "first_exact_event_family": first_family,
        "target_alias_family": target_rows,
        "preceding_non_target_event_count": len(preceding),
        "preceding_non_target_events": preceding,
        "all_root_candidates": candidates,
        "target_is_exact_first_event": not preceding and {
            row["name"] for row in first_family
        } == aliases,
        "verdict": (
            f"EXACT_{phase.upper()}_ORDERING_DIAGNOSIS_TARGET_FIRST"
            if not preceding and {row["name"] for row in first_family} == aliases
            else f"EXACT_{phase.upper()}_ORDERING_DIAGNOSIS_PRECEDING_EVENT"
        ),
    }
    output_path.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "verdict": payload["verdict"],
        "primitive_count": payload["primitive_count"],
        "strict_whole_epoch_count": strict_count,
        "root_candidate_count": len(candidates),
        "first_exact_event_family": first_family,
        "target_alias_family": target_rows,
        "preceding_non_target_event_count": len(preceding),
        "output": output_path.name,
    }, indent=2))


if __name__ == "__main__":
    main()
