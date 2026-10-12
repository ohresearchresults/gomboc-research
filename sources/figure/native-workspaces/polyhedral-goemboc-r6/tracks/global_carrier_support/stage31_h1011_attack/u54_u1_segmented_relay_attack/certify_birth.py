#!/usr/bin/env python3
"""Certify the exact U1/H(1,54) birth on the accepted rational epoch."""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

import relay_common as rc


ROOT_WIDTH = Q(1, 10**30)


def strict_other_receipt(rows, excluded):
    digest = hashlib.sha256()
    count = 0
    leaves = 0
    worst = None
    family_counts = {}
    for name, polynomial, family in rows:
        family_counts[family] = family_counts.get(family, 0) + 1
        if name in excluded:
            continue
        source_value = polynomial.eval(Q(0))
        if not source_value:
            raise AssertionError(("unexpected source zero", name))
        expected = 1 if source_value > 0 else -1
        sign, row_leaves, margin = rc.ex.bernstein_sign(
            polynomial, Q(0), Q(1), max_depth=60
        )
        if sign != expected:
            raise AssertionError(("non-target sign drift", name, expected, sign))
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


def checkpoint_receipt(points, faces, expected, parameter: Q):
    receipt = rc.exact_checkpoint(points, faces, expected)
    return {
        "parameter": rc.ex.qs(parameter),
        **receipt,
    }


def main() -> None:
    certifier_path = Path(__file__).resolve()
    common_path = rc.HERE / "relay_common.py"
    proposer_code_path = rc.HERE / "propose_epoch.py"
    locator_code_path = rc.HERE / "locate_epoch.py"
    endpoint_path = rc.HERE / "post_birth_checkpoint.csv"
    proposal_path = rc.HERE / "birth_proposal.json"
    event_scan_path = rc.HERE / "birth_event_scan.json"
    checkpoint_path = rc.HERE / "post_birth_class233_checkpoint.json"
    certificate_path = rc.HERE / "birth_certificate.json"

    proposal = json.loads(proposal_path.read_text())
    event_scan = json.loads(event_scan_path.read_text())
    if proposal.get("verdict") != "RATIONAL_FULL_SUPPORT_BIRTH_PROPOSAL_PASS":
        raise AssertionError(("proposal verdict", proposal.get("verdict")))
    if event_scan.get("verdict") != "EXHAUSTIVE_EXACT_BIRTH_FIRST_EVENT_LOCATOR_PASS":
        raise AssertionError(("locator verdict", event_scan.get("verdict")))
    if rc.sha256(rc.SOURCE) != proposal["source_hashes"][rc.relative(rc.SOURCE)]:
        raise AssertionError("proposal source binding drift")
    if rc.sha256(endpoint_path) != proposal["exact_endpoint"]["sha256"]:
        raise AssertionError("proposal endpoint binding drift")
    for path in (rc.SOURCE, endpoint_path, rc.FACES, proposal_path):
        if event_scan["source_hashes"][rc.relative(path)] != rc.sha256(path):
            raise AssertionError(("locator binding drift", path))

    source = rc.ex.read_rows(rc.SOURCE)
    endpoint = rc.ex.read_rows(endpoint_path)
    faces = json.loads(rc.FACES.read_text())
    path = rc.affine_path(source, endpoint)
    rows = list(rc.primitive_rows(path, faces))
    if len(rows) != 7922:
        raise AssertionError(("primitive count", len(rows)))
    lookup = {name: polynomial for name, polynomial, _family in rows}
    aliases = set(rc.ALIASES["birth"])
    if not aliases.issubset(lookup):
        raise AssertionError(("missing target aliases", sorted(aliases - set(lookup))))
    target = lookup[rc.ALIASES["birth"][0]]
    if any(lookup[name] != target for name in aliases):
        raise AssertionError("birth aliases are not one exact polynomial")

    strict = strict_other_receipt(rows, aliases)
    if strict != event_scan["exhaustive_strict_other_primitives"]:
        raise AssertionError("locator strict receipt does not reproduce")
    event = event_scan["first_event"]
    if set(event["aliases"]) != aliases:
        raise AssertionError(("locator alias family", event["aliases"]))
    if event["polynomial_digest"] != rc.canonical_hash(target.exact()):
        raise AssertionError("locator target polynomial drift")
    lo, hi = Q(event["lo"]), Q(event["hi"])
    root = rc.ex.isolate_monotone_root(target, lo, hi, ROOT_WIDTH)
    if root["lo"] != lo or root["hi"] != hi:
        raise AssertionError("locator root interval is not canonical")
    source_sign = 1 if target.eval(Q(0)) > 0 else -1
    endpoint_sign = 1 if target.eval(Q(1)) > 0 else -1
    if (source_sign, endpoint_sign) != (-1, 1):
        raise AssertionError(("birth target endpoint signs", source_sign, endpoint_sign))
    pre_sign, pre_leaves, pre_worst = rc.ex.bernstein_sign(
        target, Q(0), lo, max_depth=60
    )
    post_sign, post_leaves, post_worst = rc.ex.bernstein_sign(
        target, hi, Q(1), max_depth=60
    )
    if (pre_sign, post_sign) != (-1, 1):
        raise AssertionError(("birth target open-piece signs", pre_sign, post_sign))

    pre_parameter = lo / 2
    post_parameter = (hi + 1) / 2
    source_checkpoint = checkpoint_receipt(source, faces, rc.PRE_FEATURES, Q(0))
    pre_checkpoint = checkpoint_receipt(
        rc.evaluate_path(path, pre_parameter), faces, rc.PRE_FEATURES, pre_parameter
    )
    post_checkpoint = checkpoint_receipt(
        rc.evaluate_path(path, post_parameter), faces, rc.MIDDLE_FEATURES, post_parameter
    )
    endpoint_checkpoint = checkpoint_receipt(
        endpoint, faces, rc.MIDDLE_FEATURES, Q(1)
    )
    if endpoint_checkpoint["coordinate_hash"] != proposal[
        "exact_endpoint"
    ]["checkpoint"]["coordinate_hash"]:
        raise AssertionError("proposal/certifier endpoint coordinate hash drift")

    row230 = {
        label: rc.row230_values(points, faces)
        for label, points in (
            ("source", source),
            ("pre", rc.evaluate_path(path, pre_parameter)),
            ("post", rc.evaluate_path(path, post_parameter)),
            ("endpoint", endpoint),
        )
    }
    if any(Q(value) <= 0 for receipt in row230.values() for value in receipt.values()):
        raise AssertionError("row230 danger support lost strictness")

    checkpoint_payload = {
        "version": 1,
        "scope": (
            "Literal rational post-birth class-(2,3,3) checkpoint after the "
            "simple exact B = vertex:1:54 = edge:(1,54):t event."
        ),
        "source_hashes": {
            rc.relative(rc.SOURCE): rc.sha256(rc.SOURCE),
            rc.relative(endpoint_path): rc.sha256(endpoint_path),
            rc.relative(rc.FACES): rc.sha256(rc.FACES),
            rc.relative(proposal_path): rc.sha256(proposal_path),
            rc.relative(event_scan_path): rc.sha256(event_scan_path),
            rc.relative(rc.EXACT_CORE): rc.sha256(rc.EXACT_CORE),
            rc.relative(common_path): rc.sha256(common_path),
            rc.relative(proposer_code_path): rc.sha256(proposer_code_path),
            rc.relative(locator_code_path): rc.sha256(locator_code_path),
            rc.relative(certifier_path): rc.sha256(certifier_path),
        },
        "checkpoint": endpoint_checkpoint,
        "row230_squared_margins": row230["endpoint"],
        "verdict": "EXACT_POST_BIRTH_CLASS_233_CHECKPOINT_PASS",
    }
    checkpoint_path.write_text(json.dumps(checkpoint_payload, indent=2) + "\n")

    root_record = {
        "target": rc.ALIASES["birth"][0],
        "complete_zero_family": sorted(aliases),
        "lo": rc.ex.qs(lo),
        "hi": rc.ex.qs(hi),
        "decimal_interval": [float(lo), float(hi)],
        "value_lo": rc.ex.qs(root["value_lo"]),
        "value_hi": rc.ex.qs(root["value_hi"]),
        "polynomial_degree": target.degree,
        "polynomial_exact": target.exact(),
        "polynomial_digest": rc.canonical_hash(target.exact()),
        "derivative_sign": root["derivative_sign"],
        "derivative_bernstein_leaves": root["derivative_bernstein_leaves"],
        "simple_root": True,
        "pre_sign": pre_sign,
        "post_sign": post_sign,
        "pre_bernstein_leaf_count": pre_leaves,
        "post_bernstein_leaf_count": post_leaves,
        "pre_minimum_bernstein_log10_abs": pre_worst,
        "post_minimum_bernstein_log10_abs": post_worst,
        "unique_root_on_unit_epoch": True,
    }
    certificate = {
        "version": 1,
        "event": "U1 and H(1,54) exact simultaneous birth",
        "scope": (
            "Exact rational affine epoch with exhaustive strictness of all 7,920 "
            "non-target primitives, one simple common B root, and exact open-piece "
            "class checks. No floating root or tolerance is accepted."
        ),
        "source_hashes": {
            **rc.bindings(),
            rc.relative(rc.SOURCE): rc.sha256(rc.SOURCE),
            rc.relative(endpoint_path): rc.sha256(endpoint_path),
            rc.relative(proposal_path): rc.sha256(proposal_path),
            rc.relative(event_scan_path): rc.sha256(event_scan_path),
            rc.relative(checkpoint_path): rc.sha256(checkpoint_path),
            rc.relative(common_path): rc.sha256(common_path),
            rc.relative(proposer_code_path): rc.sha256(proposer_code_path),
            rc.relative(locator_code_path): rc.sha256(locator_code_path),
            rc.relative(certifier_path): rc.sha256(certifier_path),
        },
        "exhaustive_strict_other_primitives": strict,
        "exact_root": root_record,
        "open_piece_classes": {
            "pre_interval": ["0", rc.ex.qs(lo)],
            "pre_sample": pre_checkpoint,
            "post_interval": [rc.ex.qs(hi), "1"],
            "post_sample": post_checkpoint,
            "class_transition": {
                "before": rc.PRE_FEATURES,
                "after": rc.MIDDLE_FEATURES,
                "delta": [0, 1, 1],
            },
        },
        "source_checkpoint": source_checkpoint,
        "post_birth_checkpoint": endpoint_checkpoint,
        "row230_squared_margins": row230,
        "mechanics_alias_identity": {
            "source": rc.mechanics_identity(source, faces),
            "endpoint": rc.mechanics_identity(endpoint, faces),
        },
        "fresh_proposer_checks": proposal["selected_branch"]["endpoint_audit"][
            "checks"
        ],
        "generated_file_sha256": {
            rc.relative(endpoint_path): rc.sha256(endpoint_path),
            rc.relative(checkpoint_path): rc.sha256(checkpoint_path),
            rc.relative(event_scan_path): rc.sha256(event_scan_path),
        },
        "death_authorized": True,
        "verdict": "EXACT_U1_BIRTH_EPOCH_PASS",
    }
    if not all(certificate["fresh_proposer_checks"].values()):
        raise AssertionError("fresh proposer check is false")
    certificate_path.write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps({
        "verdict": certificate["verdict"],
        "complete_zero_family": root_record["complete_zero_family"],
        "root_decimal_interval": root_record["decimal_interval"],
        "strict_other_primitive_count": strict["strict_other_primitive_count"],
        "class_transition": certificate["open_piece_classes"]["class_transition"],
        "post_birth_checkpoint_sha256": rc.sha256(endpoint_path),
        "certificate": certificate_path.name,
    }, indent=2))


if __name__ == "__main__":
    main()
