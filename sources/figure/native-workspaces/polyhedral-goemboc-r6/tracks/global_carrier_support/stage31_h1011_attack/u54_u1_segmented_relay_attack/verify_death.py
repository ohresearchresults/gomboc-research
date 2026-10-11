#!/usr/bin/env python3
"""Independent exact verifier for U54 death and the completed U54 -> U1 relay."""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

import relay_common as rc


EXPECTED_DEATH_SOURCE_SHA256 = (
    "301ee45fecc7166d76fa8abadd53bf92d0c63224853cee191c4237493f84f11a"
)


def strict_other_receipt(rows, excluded):
    digest = hashlib.sha256()
    leaves = 0
    worst = None
    count = 0
    family_counts = {}
    for name, polynomial, family in rows:
        family_counts[family] = family_counts.get(family, 0) + 1
        if name in excluded:
            continue
        source_value = polynomial.eval(Q(0))
        if not source_value:
            raise AssertionError(("non-target source zero", name))
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


def verify_state(points, faces, expected):
    support = rc.ex.supporting_cell(points, faces)
    ledger, mechanics = rc.ex.classify_point(points, faces)
    if support["f_vector"] != [61, 162, 103] or support["euler"] != 2:
        raise AssertionError(("support", support))
    if support["active_labels"] != rc.EXPECTED_ACTIVE:
        raise AssertionError(("active labels", support["active_labels"]))
    for key, value in expected.items():
        if mechanics[key] != value:
            raise AssertionError((key, mechanics[key], value))
    if rc.BASE not in {frozenset(face) for face in faces}:
        raise AssertionError("enlarged base absent")
    missing_rails = sorted(rc.forced_rails() - set(support["edges"]))
    if missing_rails:
        raise AssertionError(("missing rails", missing_rails))
    constant_path = {
        label: tuple(rc.ex.P((value,)) for value in xyz)
        for label, xyz in points.items()
    }
    turns = [
        row for row in rc.primitive_rows(constant_path, faces)
        if row[2] == "in_face_turn"
    ]
    if len(turns) != 18 or any(not polynomial.eval(Q(0)) for _, polynomial, _ in turns):
        raise AssertionError("base-turn contract")
    row230 = rc.row230_values(points, faces)
    if any(Q(value) <= 0 for value in row230.values()):
        raise AssertionError("row230 danger support is not strict")
    h910 = ledger["edge"][(9, 10)]
    h910_witness = min(
        ("t", "one_minus_t", "beta1", "beta2"), key=lambda key: h910[key]
    )
    if h910[h910_witness] >= 0:
        raise AssertionError("H910 is not strictly dead")
    d6, m24 = rc.ex.exact_centroid_numerators(points, faces)
    centroid = tuple(value / (4 * d6) for value in m24)
    return {
        "coordinate_hash": rc.canonical_hash({
            str(label): [rc.ex.qs(value) for value in points[label]]
            for label in sorted(points)
        }),
        "centroid": [rc.ex.qs(value) for value in centroid],
        "f_vector": support["f_vector"],
        "euler": support["euler"],
        "active_label_count": len(support["active_labels"]),
        "strict_support_count": support["strict_support_count"],
        "class": mechanics["class"],
        "stable_faces": mechanics["stable_faces"],
        "unstable_vertices": mechanics["unstable_vertices"],
        "saddle_edges": mechanics["saddle_edges"],
        "forced_rail_count": len(rc.forced_rails()),
        "base_turn_count": len(turns),
        "row230_squared_margins": row230,
        "h910_negative_component": h910_witness,
        "h910_negative_value": rc.ex.qs(h910[h910_witness]),
    }


def main() -> None:
    verifier_path = Path(__file__).resolve()
    common_path = rc.HERE / "relay_common.py"
    proposer_code_path = rc.HERE / "propose_epoch.py"
    locator_code_path = rc.HERE / "locate_epoch.py"
    certifier_code_path = rc.HERE / "certify_death.py"
    birth_certificate_path = rc.HERE / "birth_certificate.json"
    birth_verification_path = rc.HERE / "birth_verification.json"
    source_path = rc.HERE / "post_birth_checkpoint.csv"
    endpoint_path = rc.HERE / "far_u1.csv"
    proposal_path = rc.HERE / "death_proposal.json"
    event_scan_path = rc.HERE / "death_event_scan.json"
    ordering_path = rc.HERE / "death_ordering_diagnosis.json"
    checkpoint_path = rc.HERE / "far_u1_class222_checkpoint.json"
    certificate_path = rc.HERE / "death_certificate.json"
    output_path = rc.HERE / "death_verification.json"

    birth_certificate = json.loads(birth_certificate_path.read_text())
    birth_verification = json.loads(birth_verification_path.read_text())
    proposal = json.loads(proposal_path.read_text())
    event_scan = json.loads(event_scan_path.read_text())
    ordering = json.loads(ordering_path.read_text())
    checkpoint_receipt = json.loads(checkpoint_path.read_text())
    certificate = json.loads(certificate_path.read_text())
    if birth_certificate.get("verdict") != "EXACT_U1_BIRTH_EPOCH_PASS":
        raise AssertionError(("birth certificate verdict", birth_certificate.get("verdict")))
    if birth_verification.get("verdict") != "INDEPENDENT_EXACT_U1_BIRTH_VERIFICATION_PASS":
        raise AssertionError(("birth verification verdict", birth_verification.get("verdict")))
    if certificate.get("verdict") != "EXACT_U54_DEATH_EPOCH_PASS":
        raise AssertionError(("certificate verdict", certificate.get("verdict")))
    if checkpoint_receipt.get("verdict") != "EXACT_FAR_U1_CLASS_222_CHECKPOINT_PASS":
        raise AssertionError(("checkpoint verdict", checkpoint_receipt.get("verdict")))
    if proposal.get("verdict") != "RATIONAL_FULL_SUPPORT_DEATH_PROPOSAL_PASS":
        raise AssertionError(("proposal verdict", proposal.get("verdict")))
    if event_scan.get("verdict") != "EXHAUSTIVE_EXACT_DEATH_FIRST_EVENT_LOCATOR_PASS":
        raise AssertionError(("locator verdict", event_scan.get("verdict")))
    if ordering.get("verdict") != "EXACT_DEATH_ORDERING_DIAGNOSIS_TARGET_FIRST":
        raise AssertionError(("ordering verdict", ordering.get("verdict")))
    if ordering.get("preceding_non_target_event_count") != 0:
        raise AssertionError("ordering diagnosis has a preceding event")
    if rc.sha256(source_path) != EXPECTED_DEATH_SOURCE_SHA256:
        raise AssertionError("death source hash")
    if birth_certificate["generated_file_sha256"][rc.relative(source_path)] != (
        EXPECTED_DEATH_SOURCE_SHA256
    ):
        raise AssertionError("birth certificate source authority")
    if birth_verification["source_hashes"][rc.relative(source_path)] != (
        EXPECTED_DEATH_SOURCE_SHA256
    ):
        raise AssertionError("birth verification source authority")

    for path in (
        source_path,
        endpoint_path,
        rc.FACES,
        proposal_path,
        event_scan_path,
        ordering_path,
        checkpoint_path,
        birth_certificate_path,
        birth_verification_path,
        common_path,
        proposer_code_path,
        locator_code_path,
        certifier_code_path,
    ):
        relative = rc.relative(path)
        if certificate["source_hashes"].get(relative) != rc.sha256(path):
            raise AssertionError(("certificate source binding", relative))
    for path in (endpoint_path, checkpoint_path, event_scan_path):
        if certificate["generated_file_sha256"].get(rc.relative(path)) != rc.sha256(path):
            raise AssertionError(("generated-file binding", path))
    if proposal["exact_endpoint"]["sha256"] != rc.sha256(endpoint_path):
        raise AssertionError("proposal endpoint binding")
    if not all(proposal["selected_branch"]["endpoint_audit"]["checks"].values()):
        raise AssertionError("proposal endpoint check false")
    support_guard = proposal["selected_branch"]["endpoint_audit"][
        "exact_support_endpoint_guard"
    ]
    raw_guard = proposal["selected_branch"]["endpoint_audit"][
        "exact_raw_endpoint_guard"
    ]
    if support_guard["changed_count"] or not support_guard[
        "all_endpoint_signs_preserved"
    ]:
        raise AssertionError("proposal exact support endpoint guard failed")
    if raw_guard["changed_count"] or not raw_guard[
        "all_non_target_endpoint_signs_preserved"
    ]:
        raise AssertionError("proposal exact raw endpoint guard failed")

    source = rc.ex.read_rows(source_path)
    endpoint = rc.ex.read_rows(endpoint_path)
    faces = json.loads(rc.FACES.read_text())
    path = rc.affine_path(source, endpoint)
    rows = list(rc.primitive_rows(path, faces))
    if len(rows) != 7922:
        raise AssertionError(("primitive count", len(rows)))
    lookup = {name: polynomial for name, polynomial, _family in rows}
    aliases = set(rc.ALIASES["death"])
    target = lookup[rc.ALIASES["death"][0]]
    if set(certificate["exact_root"]["complete_zero_family"]) != aliases:
        raise AssertionError("certificate zero family")
    if any(lookup[name] != target for name in aliases):
        raise AssertionError("target aliases differ")
    strict = strict_other_receipt(rows, aliases)
    if strict != certificate["exhaustive_strict_other_primitives"]:
        raise AssertionError("certificate strict receipt mismatch")
    if strict != event_scan["exhaustive_strict_other_primitives"]:
        raise AssertionError("locator strict receipt mismatch")

    root_record = certificate["exact_root"]
    lo, hi = Q(root_record["lo"]), Q(root_record["hi"])
    if root_record["polynomial_exact"] != target.exact():
        raise AssertionError("certificate target coefficients")
    if root_record["polynomial_digest"] != rc.canonical_hash(target.exact()):
        raise AssertionError("certificate target digest")
    ordering_family = ordering["first_exact_event_family"]
    if {row["name"] for row in ordering_family} != aliases:
        raise AssertionError("ordering zero family")
    if ordering.get("root_candidate_count") != 2 or not ordering.get(
        "target_is_exact_first_event"
    ):
        raise AssertionError("ordering target-first contract")
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
    value_lo, value_hi = target.eval(lo), target.eval(hi)
    if not value_lo or not value_hi or (value_lo > 0) == (value_hi > 0):
        raise AssertionError("death root bracket does not change sign")
    derivative_sign, derivative_leaves, _derivative_worst = rc.ex.bernstein_sign(
        target.derivative(), lo, hi, max_depth=60
    )
    if derivative_sign != -1 or derivative_leaves != root_record[
        "derivative_bernstein_leaves"
    ]:
        raise AssertionError("death root is not independently simple")
    pre_sign, _pre_leaves, _pre_worst = rc.ex.bernstein_sign(
        target, Q(0), lo, max_depth=60
    )
    post_sign, _post_leaves, _post_worst = rc.ex.bernstein_sign(
        target, hi, Q(1), max_depth=60
    )
    if (pre_sign, post_sign) != (1, -1):
        raise AssertionError(("target open-piece signs", pre_sign, post_sign))

    pre_parameter = Q(certificate["open_piece_classes"]["pre_sample"]["parameter"])
    post_parameter = Q(certificate["open_piece_classes"]["post_sample"]["parameter"])
    if not (Q(0) < pre_parameter < lo < hi < post_parameter < Q(1)):
        raise AssertionError("class sample ordering")
    source_state = verify_state(source, faces, rc.MIDDLE_FEATURES)
    pre_state = verify_state(
        rc.evaluate_path(path, pre_parameter), faces, rc.MIDDLE_FEATURES
    )
    post_state = verify_state(
        rc.evaluate_path(path, post_parameter), faces, rc.FAR_FEATURES
    )
    endpoint_state = verify_state(endpoint, faces, rc.FAR_FEATURES)
    if endpoint_state["coordinate_hash"] != checkpoint_receipt[
        "checkpoint"
    ]["coordinate_hash"]:
        raise AssertionError("FAR checkpoint coordinate hash")
    if checkpoint_receipt["source_hashes"][rc.relative(endpoint_path)] != rc.sha256(
        endpoint_path
    ):
        raise AssertionError("FAR checkpoint file binding")
    if checkpoint_receipt["checkpoint"]["mechanics"]["class"] != [2, 2, 2]:
        raise AssertionError("FAR checkpoint class")
    if certificate["open_piece_classes"]["class_transition"] != {
        "before": rc.MIDDLE_FEATURES,
        "after": rc.FAR_FEATURES,
        "delta": [0, -1, -1],
    }:
        raise AssertionError("certificate class transition")
    expected_relay = {
        "birth_class_transition": [[2, 2, 2], [2, 3, 3]],
        "death_class_transition": [[2, 3, 3], [2, 2, 2]],
        "initial_unstable_vertices": [8, 54],
        "final_unstable_vertices": [1, 8],
        "initial_saddles": [[5, 6], [10, 11]],
        "final_saddles": [[5, 6], [10, 11]],
        "carrier_transferred": [54, 1],
    }
    if certificate.get("relay_summary") != expected_relay:
        raise AssertionError("relay summary")
    if not certificate.get("relay_complete"):
        raise AssertionError("certificate did not complete relay")

    payload = {
        "version": 1,
        "scope": (
            "Independent reconstruction of the fresh exact death epoch, all "
            "7,922 primitives, the simple two-alias D zero family, exact open-"
            "piece classes, FAR hull/mechanics, and accepted birth-source binding."
        ),
        "source_hashes": {
            rc.relative(source_path): rc.sha256(source_path),
            rc.relative(endpoint_path): rc.sha256(endpoint_path),
            rc.relative(rc.FACES): rc.sha256(rc.FACES),
            rc.relative(proposal_path): rc.sha256(proposal_path),
            rc.relative(event_scan_path): rc.sha256(event_scan_path),
            rc.relative(ordering_path): rc.sha256(ordering_path),
            rc.relative(checkpoint_path): rc.sha256(checkpoint_path),
            rc.relative(certificate_path): rc.sha256(certificate_path),
            rc.relative(birth_certificate_path): rc.sha256(birth_certificate_path),
            rc.relative(birth_verification_path): rc.sha256(birth_verification_path),
            rc.relative(rc.EXACT_CORE): rc.sha256(rc.EXACT_CORE),
            rc.relative(common_path): rc.sha256(common_path),
            rc.relative(proposer_code_path): rc.sha256(proposer_code_path),
            rc.relative(locator_code_path): rc.sha256(locator_code_path),
            rc.relative(certifier_code_path): rc.sha256(certifier_code_path),
            rc.relative(verifier_path): rc.sha256(verifier_path),
        },
        "birth_source_authority": {
            "checkpoint_sha256": EXPECTED_DEATH_SOURCE_SHA256,
            "birth_certificate_verdict": birth_certificate["verdict"],
            "birth_verification_verdict": birth_verification["verdict"],
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
        "exact_event": {
            "complete_zero_family": sorted(aliases),
            "root_interval": [rc.ex.qs(lo), rc.ex.qs(hi)],
            "decimal_interval": [float(lo), float(hi)],
            "polynomial_degree": target.degree,
            "polynomial_digest": rc.canonical_hash(target.exact()),
            "derivative_sign": derivative_sign,
            "simple_unique_unit_epoch_root": True,
        },
        "state_readbacks": {
            "source": source_state,
            "pre": pre_state,
            "post": post_state,
            "endpoint": endpoint_state,
        },
        "relay_summary": expected_relay,
        "far_u1_class": [2, 2, 2],
        "relay_complete": True,
        "verdict": "INDEPENDENT_EXACT_U54_DEATH_VERIFICATION_PASS",
    }
    output_path.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "verdict": payload["verdict"],
        "primitive_count": strict["primitive_count"],
        "strict_other_primitive_count": strict["strict_other_primitive_count"],
        "complete_zero_family": payload["exact_event"]["complete_zero_family"],
        "root_decimal_interval": payload["exact_event"]["decimal_interval"],
        "far_u1_class": payload["far_u1_class"],
        "far_u1_sha256": rc.sha256(endpoint_path),
        "relay_complete": payload["relay_complete"],
        "output": output_path.name,
    }, indent=2))


if __name__ == "__main__":
    main()
