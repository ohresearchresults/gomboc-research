#!/usr/bin/env python3
"""Fail-closed exact first-event locator for a proposed relay epoch."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Q

import relay_common as rc


ROOT_WIDTH = Q(1, 10**30)


def phase_paths(phase):
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


def bisect_sign_change(polynomial, width=ROOT_WIDTH):
    lo, hi = Q(0), Q(1)
    value_lo, value_hi = polynomial.eval(lo), polynomial.eval(hi)
    if value_lo == 0 or value_hi == 0 or (value_lo > 0) == (value_hi > 0):
        raise AssertionError("target does not have an odd interior crossing")
    while hi - lo > width:
        middle = (lo + hi) / 2
        value_middle = polynomial.eval(middle)
        if value_middle == 0:
            lo = middle - width / 4
            hi = middle + width / 4
            value_lo = polynomial.eval(lo)
            value_hi = polynomial.eval(hi)
            break
        if (value_middle > 0) == (value_lo > 0):
            lo, value_lo = middle, value_middle
        else:
            hi, value_hi = middle, value_middle
    return lo, hi


def strict_receipt(rows, excluded):
    digest = hashlib.sha256()
    count = 0
    leaves = 0
    worst = None
    family_counts = {}
    for name, polynomial, family in rows:
        family_counts[family] = family_counts.get(family, 0) + 1
        if name in excluded:
            continue
        value = polynomial.eval(Q(0))
        if value == 0:
            raise AssertionError(("unexpected zero at epoch source", name))
        expected = 1 if value > 0 else -1
        try:
            sign, row_leaves, margin = rc.ex.bernstein_sign(
                polynomial, Q(0), Q(1), max_depth=60
            )
        except Exception as error:
            raise AssertionError(("non-target primitive not strict", name, repr(error)))
        if sign != expected:
            raise AssertionError(("non-target sign changed", name, expected, sign))
        count += 1
        leaves += row_leaves
        worst = margin if worst is None else min(worst, margin)
        digest.update(
            f"{name}|{family}|{sign}|{'|'.join(polynomial.exact())}\n".encode()
        )
    return {
        "primitive_count": len(rows),
        "family_counts": family_counts,
        "strict_other_primitive_count": count,
        "strict_other_bernstein_leaf_count": leaves,
        "strict_other_minimum_bernstein_log10_abs": worst,
        "strict_other_primitive_digest": digest.hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", choices=("birth", "death"), required=True)
    args = parser.parse_args()
    phase = args.phase
    source_path, endpoint_path, proposal_path = phase_paths(phase)
    output_path = rc.HERE / f"{phase}_event_scan.json"
    failure_path = rc.HERE / f"{phase}_locator_failure_receipt.json"
    proposal = json.loads(proposal_path.read_text())
    expected_verdict = f"RATIONAL_FULL_SUPPORT_{phase.upper()}_PROPOSAL_PASS"
    if proposal.get("verdict") != expected_verdict:
        raise AssertionError(("proposal verdict", proposal.get("verdict")))
    if rc.sha256(source_path) != proposal["source_hashes"][rc.relative(source_path)]:
        raise AssertionError("proposal source binding drift")
    if rc.sha256(endpoint_path) != proposal["exact_endpoint"]["sha256"]:
        raise AssertionError("proposal endpoint binding drift")
    if rc.sha256(rc.FACES) != rc.EXPECTED_FACES_SHA256:
        raise AssertionError("face-ledger drift")

    source = rc.ex.read_rows(source_path)
    endpoint = rc.ex.read_rows(endpoint_path)
    faces = json.loads(rc.FACES.read_text())
    path = rc.affine_path(source, endpoint)
    rows = list(rc.primitive_rows(path, faces))
    if len(rows) != 7922:
        raise AssertionError(("primitive count", len(rows)))
    lookup = {name: polynomial for name, polynomial, _family in rows}
    aliases = set(rc.ALIASES[phase])
    if not aliases.issubset(lookup):
        raise AssertionError(("missing aliases", sorted(aliases - set(lookup))))
    try:
        strict = strict_receipt(rows, aliases)
        first_name = rc.ALIASES[phase][0]
        target = lookup[first_name]
        if any(lookup[name] != target for name in aliases):
            raise AssertionError("target aliases are not the same exact polynomial")
        lo, hi = bisect_sign_change(target)
        root = rc.ex.isolate_monotone_root(target, lo, hi, ROOT_WIDTH)
        start_sign = 1 if target.eval(Q(0)) > 0 else -1
        end_sign = 1 if target.eval(Q(1)) > 0 else -1
        if start_sign == end_sign:
            raise AssertionError("target aliases do not cross")
        pre_sign, pre_leaves, pre_worst = rc.ex.bernstein_sign(
            target, Q(0), root["lo"], max_depth=60
        )
        post_sign, post_leaves, post_worst = rc.ex.bernstein_sign(
            target, root["hi"], Q(1), max_depth=60
        )
        if pre_sign != start_sign or post_sign != end_sign:
            raise AssertionError("target is not strict on both open epoch pieces")
    except Exception as error:
        failure = {
            "version": 1,
            "phase": phase,
            "source_sha256": rc.sha256(source_path),
            "endpoint_sha256": rc.sha256(endpoint_path),
            "first_exact_blocker": repr(error),
            "verdict": f"FAIL_CLOSED_{phase.upper()}_LOCATOR_REJECT",
        }
        failure_path.write_text(json.dumps(failure, indent=2) + "\n")
        raise

    root_record = {
        "target": first_name,
        "aliases": sorted(aliases),
        "lo": rc.ex.qs(root["lo"]),
        "hi": rc.ex.qs(root["hi"]),
        "value_lo": rc.ex.qs(root["value_lo"]),
        "value_hi": rc.ex.qs(root["value_hi"]),
        "decimal_interval": [float(root["lo"]), float(root["hi"])],
        "derivative_sign": root["derivative_sign"],
        "derivative_bernstein_leaves": root["derivative_bernstein_leaves"],
        "polynomial_degree": target.degree,
        "polynomial_exact": target.exact(),
        "polynomial_digest": rc.canonical_hash(target.exact()),
        "pre_sign": pre_sign,
        "post_sign": post_sign,
        "pre_bernstein_leaf_count": pre_leaves,
        "post_bernstein_leaf_count": post_leaves,
        "pre_minimum_bernstein_log10_abs": pre_worst,
        "post_minimum_bernstein_log10_abs": post_worst,
    }
    payload = {
        "version": 1,
        "phase": phase,
        "scope": (
            "Exact exhaustive first-event locator over volume, all support rows, "
            "18 base turns, mechanics denominators, and every raw face/vertex/edge "
            "component on the literal rational epoch."
        ),
        "source_hashes": {
            rc.relative(source_path): rc.sha256(source_path),
            rc.relative(endpoint_path): rc.sha256(endpoint_path),
            rc.relative(rc.FACES): rc.sha256(rc.FACES),
            rc.relative(proposal_path): rc.sha256(proposal_path),
            rc.relative(rc.EXACT_CORE): rc.sha256(rc.EXACT_CORE),
            rc.relative(rc.SELECTED_OWNER): rc.sha256(rc.SELECTED_OWNER),
        },
        "exhaustive_strict_other_primitives": strict,
        "first_event": root_record,
        "overlapping_first_candidates": [
            {
                "name": name,
                "family": next(family for row_name, _poly, family in rows if row_name == name),
                "lo": root_record["lo"],
                "hi": root_record["hi"],
                "polynomial_digest": root_record["polynomial_digest"],
            }
            for name in sorted(aliases)
        ],
        "only_target_aliases_non_strict_on_unit_epoch": True,
        "verdict": f"EXHAUSTIVE_EXACT_{phase.upper()}_FIRST_EVENT_LOCATOR_PASS",
    }
    output_path.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "verdict": payload["verdict"],
        "primitive_count": strict["primitive_count"],
        "strict_other_primitive_count": strict["strict_other_primitive_count"],
        "first_event": {
            "aliases": root_record["aliases"],
            "decimal_interval": root_record["decimal_interval"],
            "derivative_sign": root_record["derivative_sign"],
        },
        "output": output_path.name,
    }, indent=2))


if __name__ == "__main__":
    main()
