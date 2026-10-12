#!/usr/bin/env python3
"""Certify the exact U54/H(1,54) death and completed U54 -> U1 relay."""
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
    return {
        "parameter": rc.ex.qs(parameter),
        **rc.exact_checkpoint(points, faces, expected),
    }


def main() -> None:
    certifier_path = Path(__file__).resolve()
    common_path = rc.HERE / "relay_common.py"
    proposer_code_path = rc.HERE / "propose_epoch.py"
    locator_code_path = rc.HERE / "locate_epoch.py"
    birth_certificate_path = rc.HERE / "birth_certificate.json"
    birth_verification_path = rc.HERE / "birth_verification.json"
    source_path = rc.HERE / "post_birth_checkpoint.csv"
    endpoint_path = rc.HERE / "far_u1.csv"
    proposal_path = rc.HERE / "death_proposal.json"
    event_scan_path = rc.HERE / "death_event_scan.json"
    ordering_path = rc.HERE / "death_ordering_diagnosis.json"
    checkpoint_path = rc.HERE / "far_u1_class222_checkpoint.json"
    certificate_path = rc.HERE / "death_certificate.json"

    birth_certificate = json.loads(birth_certificate_path.read_text())
    birth_verification = json.loads(birth_verification_path.read_text())
    proposal = json.loads(proposal_path.read_text())
    event_scan = json.loads(event_scan_path.read_text())
    ordering = json.loads(ordering_path.read_text())
    if birth_certificate.get("verdict") != "EXACT_U1_BIRTH_EPOCH_PASS":
        raise AssertionError(("birth certificate verdict", birth_certificate.get("verdict")))
    if birth_verification.get("verdict") != "INDEPENDENT_EXACT_U1_BIRTH_VERIFICATION_PASS":
        raise AssertionError(("birth verification verdict", birth_verification.get("verdict")))
    if proposal.get("verdict") != "RATIONAL_FULL_SUPPORT_DEATH_PROPOSAL_PASS":
        raise AssertionError(("proposal verdict", proposal.get("verdict")))
    if event_scan.get("verdict") != "EXHAUSTIVE_EXACT_DEATH_FIRST_EVENT_LOCATOR_PASS":
        raise AssertionError(("locator verdict", event_scan.get("verdict")))
    if ordering.get("verdict") != "EXACT_DEATH_ORDERING_DIAGNOSIS_TARGET_FIRST":
        raise AssertionError(("ordering verdict", ordering.get("verdict")))
    if ordering.get("preceding_non_target_event_count") != 0:
        raise AssertionError("ordering diagnosis has a preceding event")
    if ordering.get("root_candidate_count") != 2 or not ordering.get(
        "target_is_exact_first_event"
    ):
        raise AssertionError("ordering diagnosis target family")
    if rc.sha256(source_path) != (
        "301ee45fecc7166d76fa8abadd53bf92d0c63224853cee191c4237493f84f11a"
    ):
        raise AssertionError("unexpected death source hash")
    if rc.sha256(source_path) != birth_certificate[
        "generated_file_sha256"
    ][rc.relative(source_path)]:
        raise AssertionError("birth certificate source binding drift")
    if rc.sha256(source_path) != birth_verification[
        "source_hashes"
    ][rc.relative(source_path)]:
        raise AssertionError("birth verification source binding drift")
    if rc.sha256(endpoint_path) != proposal["exact_endpoint"]["sha256"]:
        raise AssertionError("proposal endpoint binding drift")
    for path in (source_path, endpoint_path, rc.FACES, proposal_path):
        if event_scan["source_hashes"][rc.relative(path)] != rc.sha256(path):
            raise AssertionError(("locator binding drift", path))
    for path in (source_path, endpoint_path, rc.FACES, proposal_path, rc.EXACT_CORE):
        if ordering["source_hashes"][rc.relative(path)] != rc.sha256(path):
            raise AssertionError(("ordering binding drift", path))

    source = rc.ex.read_rows(source_path)
    endpoint = rc.ex.read_rows(endpoint_path)
    faces = json.loads(rc.FACES.read_text())
    path = rc.affine_path(source, endpoint)
    rows = list(rc.primitive_rows(path, faces))
    if len(rows) != 7922:
        raise AssertionError(("primitive count", len(rows)))
    lookup = {name: polynomial for name, polynomial, _family in rows}
    aliases = set(rc.ALIASES["death"])
    if not aliases.issubset(lookup):
        raise AssertionError(("missing target aliases", sorted(aliases - set(lookup))))
    target = lookup[rc.ALIASES["death"][0]]
    if any(lookup[name] != target for name in aliases):
        raise AssertionError("death aliases are not one exact polynomial")

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
    ordering_family = ordering["first_exact_event_family"]
    if {row["name"] for row in ordering_family} != aliases:
        raise AssertionError("ordering zero family")
    for row in ordering_family:
        if row["root_interval"] != [rc.ex.qs(lo), rc.ex.qs(hi)]:
            raise AssertionError(("ordering root interval", row["name"]))
        if row["polynomial_digest"] != rc.canonical_hash(target.exact()):
            raise AssertionError(("ordering polynomial digest", row["name"]))
        if (
            row["sturm_root_count_before_interval"],
            row["sturm_root_count_in_interval"],
            row["sturm_root_count_on_unit_epoch"],
        ) != (0, 1, 1):
            raise AssertionError(("ordering Sturm counts", row["name"]))
    source_sign = 1 if target.eval(Q(0)) > 0 else -1
    endpoint_sign = 1 if target.eval(Q(1)) > 0 else -1
    if (source_sign, endpoint_sign) != (1, -1):
        raise AssertionError(("death target endpoint signs", source_sign, endpoint_sign))
    pre_sign, pre_leaves, pre_worst = rc.ex.bernstein_sign(
        target, Q(0), lo, max_depth=60
    )
    post_sign, post_leaves, post_worst = rc.ex.bernstein_sign(
        target, hi, Q(1), max_depth=60
    )
    if (pre_sign, post_sign) != (1, -1):
        raise AssertionError(("death target open-piece signs", pre_sign, post_sign))

    pre_parameter = lo / 2
    post_parameter = (hi + 1) / 2
    pre_points = rc.evaluate_path(path, pre_parameter)
    post_points = rc.evaluate_path(path, post_parameter)
    source_checkpoint = checkpoint_receipt(source, faces, rc.MIDDLE_FEATURES, Q(0))
    pre_checkpoint = checkpoint_receipt(
        pre_points, faces, rc.MIDDLE_FEATURES, pre_parameter
    )
    post_checkpoint = checkpoint_receipt(
        post_points, faces, rc.FAR_FEATURES, post_parameter
    )
    endpoint_checkpoint = checkpoint_receipt(endpoint, faces, rc.FAR_FEATURES, Q(1))
    if endpoint_checkpoint["coordinate_hash"] != proposal[
        "exact_endpoint"
    ]["checkpoint"]["coordinate_hash"]:
        raise AssertionError("proposal/certifier endpoint coordinate hash drift")

    row230 = {
        label: rc.row230_values(points, faces)
        for label, points in (
            ("source", source),
            ("pre", pre_points),
            ("post", post_points),
            ("endpoint", endpoint),
        )
    }
    if any(Q(value) <= 0 for receipt in row230.values() for value in receipt.values()):
        raise AssertionError("row230 danger support lost strictness")

    checkpoint_payload = {
        "version": 1,
        "scope": (
            "Literal rational FAR U1-carrier class-(2,2,2) checkpoint after the "
            "simple exact D = vertex:54:1 = edge:(1,54):one_minus_t event."
        ),
        "source_hashes": {
            rc.relative(source_path): rc.sha256(source_path),
            rc.relative(endpoint_path): rc.sha256(endpoint_path),
            rc.relative(rc.FACES): rc.sha256(rc.FACES),
            rc.relative(proposal_path): rc.sha256(proposal_path),
            rc.relative(event_scan_path): rc.sha256(event_scan_path),
            rc.relative(ordering_path): rc.sha256(ordering_path),
            rc.relative(birth_certificate_path): rc.sha256(birth_certificate_path),
            rc.relative(birth_verification_path): rc.sha256(birth_verification_path),
            rc.relative(rc.EXACT_CORE): rc.sha256(rc.EXACT_CORE),
            rc.relative(common_path): rc.sha256(common_path),
            rc.relative(proposer_code_path): rc.sha256(proposer_code_path),
            rc.relative(locator_code_path): rc.sha256(locator_code_path),
            rc.relative(certifier_path): rc.sha256(certifier_path),
        },
        "checkpoint": endpoint_checkpoint,
        "row230_squared_margins": row230["endpoint"],
        "verdict": "EXACT_FAR_U1_CLASS_222_CHECKPOINT_PASS",
    }
    checkpoint_path.write_text(json.dumps(checkpoint_payload, indent=2) + "\n")

    root_record = {
        "target": rc.ALIASES["death"][0],
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
        "event": "U54 and H(1,54) exact simultaneous death",
        "scope": (
            "Exact fresh rational death epoch with exhaustive strictness of all "
            "7,920 non-target primitives, one simple common D root, exact open-"
            "piece classes, and bindings to the accepted independent birth source."
        ),
        "source_hashes": {
            **rc.bindings(),
            rc.relative(source_path): rc.sha256(source_path),
            rc.relative(endpoint_path): rc.sha256(endpoint_path),
            rc.relative(proposal_path): rc.sha256(proposal_path),
            rc.relative(event_scan_path): rc.sha256(event_scan_path),
            rc.relative(ordering_path): rc.sha256(ordering_path),
            rc.relative(checkpoint_path): rc.sha256(checkpoint_path),
            rc.relative(birth_certificate_path): rc.sha256(birth_certificate_path),
            rc.relative(birth_verification_path): rc.sha256(birth_verification_path),
            rc.relative(common_path): rc.sha256(common_path),
            rc.relative(proposer_code_path): rc.sha256(proposer_code_path),
            rc.relative(locator_code_path): rc.sha256(locator_code_path),
            rc.relative(certifier_path): rc.sha256(certifier_path),
        },
        "birth_source_authority": {
            "checkpoint_sha256": rc.sha256(source_path),
            "birth_certificate_verdict": birth_certificate["verdict"],
            "birth_verification_verdict": birth_verification["verdict"],
            "birth_zero_family": birth_certificate["exact_root"][
                "complete_zero_family"
            ],
        },
        "exhaustive_strict_other_primitives": strict,
        "ordering_diagnosis": {
            "verdict": ordering["verdict"],
            "primitive_count": ordering["primitive_count"],
            "strict_whole_epoch_count": ordering["strict_whole_epoch_count"],
            "root_candidate_count": ordering["root_candidate_count"],
            "preceding_non_target_event_count": ordering[
                "preceding_non_target_event_count"
            ],
            "candidate_digest": ordering["candidate_digest"],
            "sha256": rc.sha256(ordering_path),
        },
        "exact_root": root_record,
        "open_piece_classes": {
            "pre_interval": ["0", rc.ex.qs(lo)],
            "pre_sample": pre_checkpoint,
            "post_interval": [rc.ex.qs(hi), "1"],
            "post_sample": post_checkpoint,
            "class_transition": {
                "before": rc.MIDDLE_FEATURES,
                "after": rc.FAR_FEATURES,
                "delta": [0, -1, -1],
            },
        },
        "source_checkpoint": source_checkpoint,
        "far_u1_checkpoint": endpoint_checkpoint,
        "row230_squared_margins": row230,
        "mechanics_alias_identity": {
            "source": rc.mechanics_identity(source, faces),
            "endpoint": rc.mechanics_identity(endpoint, faces),
        },
        "fresh_proposer_checks": proposal["selected_branch"]["endpoint_audit"][
            "checks"
        ],
        "row230_margin_increase_diagnostic": proposal["selected_branch"].get(
            "row230_margin_increase_diagnostic"
        ),
        "generated_file_sha256": {
            rc.relative(endpoint_path): rc.sha256(endpoint_path),
            rc.relative(checkpoint_path): rc.sha256(checkpoint_path),
            rc.relative(event_scan_path): rc.sha256(event_scan_path),
        },
        "relay_summary": {
            "birth_class_transition": [[2, 2, 2], [2, 3, 3]],
            "death_class_transition": [[2, 3, 3], [2, 2, 2]],
            "initial_unstable_vertices": [8, 54],
            "final_unstable_vertices": [1, 8],
            "initial_saddles": [[5, 6], [10, 11]],
            "final_saddles": [[5, 6], [10, 11]],
            "carrier_transferred": [54, 1],
        },
        "relay_complete": True,
        "verdict": "EXACT_U54_DEATH_EPOCH_PASS",
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
        "far_u1_sha256": rc.sha256(endpoint_path),
        "relay_complete": certificate["relay_complete"],
        "certificate": certificate_path.name,
    }, indent=2))


if __name__ == "__main__":
    main()
