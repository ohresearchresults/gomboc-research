#!/usr/bin/env python3
"""Exact class-preserving (229,231) mechanics transfer after the fifth flip."""
from __future__ import annotations

import json
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ATTACK = MAIN.parents[1]
SOURCE = MAIN / "post_flip_round4" / "far.csv"
FACES_PATH = MAIN / "post_flip_round4" / "post_faces.json"
ENDPOINT = HERE / "candidate.csv"
PROPOSAL = HERE / "proposal.json"
SCAN = HERE / "first_event_scan.json"
CERTIFICATE = HERE / "transfer_certificate.json"
FAR_OUT = HERE / "transfer_far.csv"

sys.path.insert(0, str(MAIN))
sys.path.insert(0, str(ATTACK))

import certify_safe_flip as core  # noqa: E402
import post_c17_exact as pc  # noqa: E402


TARGET = "edge:(229, 231):beta1"
EVENT_FAMILY = (
    "edge:(229, 231):beta1",
    "face_raw:(229, 231, 247):(229, 231)",
)
EVENT_MULTIPLICITY = {name: 1 for name in EVENT_FAMILY}
FAR_PARAMETER = Q(1)


def configure_core():
    core.EVENT_FAMILY = EVENT_FAMILY
    core.EVENT_MULTIPLICITY = EVENT_MULTIPLICITY
    core.FAR_PARAMETER = FAR_PARAMETER


def exact_common_factor_audit(rows, root, target):
    by_name = {name: (polynomial, family) for name, polynomial, family in rows}
    assert set(EVENT_FAMILY).issubset(by_name)
    face_polynomial = by_name[EVENT_FAMILY[1]][0]
    factor = core.monic_gcd(target, face_polynomial)
    assert factor.degree >= 1
    isolated = core.ex.isolate_monotone_root(
        factor, root["lo"], root["hi"], core.ROOT_WIDTH
    )
    assert isolated["lo"] <= root["hi"] and isolated["hi"] >= root["lo"]

    strict_count = 0
    strict_leaves = 0
    strict_worst = None
    for name, polynomial, _family in rows:
        if name in EVENT_FAMILY:
            continue
        _sign, leaves, margin = core.ex.bernstein_sign(
            polynomial, root["lo"], root["hi"], max_depth=60
        )
        strict_count += 1
        strict_leaves += leaves
        strict_worst = margin if strict_worst is None else min(strict_worst, margin)

    shared = {}
    multiplicities = {}
    for name in EVENT_FAMILY:
        polynomial, family = by_name[name]
        multiplicity, quotient = core.factor_multiplicity(polynomial, factor)
        assert multiplicity >= 1
        sign, leaves, margin = core.ex.bernstein_sign(
            quotient, root["lo"], root["hi"], max_depth=60
        )
        multiplicities[name] = multiplicity
        shared[name] = {
            "family": family,
            "polynomial_degree": polynomial.degree,
            "polynomial_digest": core.canonical_hash(polynomial.exact()),
            "common_factor_multiplicity": multiplicity,
            "crosses_sign": multiplicity % 2 == 1,
            "quotient_sign": sign,
            "quotient_bernstein_leaf_count": leaves,
            "quotient_minimum_bernstein_log10_abs": margin,
        }
    assert all(value % 2 == 1 for value in multiplicities.values())
    return {
        "allowed_zero_family": list(EVENT_FAMILY),
        "strict_other_primitive_count": strict_count,
        "strict_other_bernstein_leaf_count": strict_leaves,
        "strict_other_minimum_bernstein_log10_abs": strict_worst,
        "shared_algebraic_factor": {
            "degree": factor.degree,
            "exact": factor.exact(),
            "digest": core.canonical_hash(factor.exact()),
            "root_interval": [
                core.ex.qs(isolated["lo"]), core.ex.qs(isolated["hi"])
            ],
        },
        "family_records": shared,
        "multiplicity_pattern": multiplicities,
    }


def main():
    configure_core()
    proposal = json.loads(PROPOSAL.read_text())
    scan = json.loads(SCAN.read_text())
    assert proposal["verdict"] == "RATIONAL_POST_SAFE_FLIP_DESCENT_PROPOSAL_PASS"
    assert scan["verdict"] == "EXHAUSTIVE_EXACT_POST_C17_FIXED_PLANE_FIRST_EVENT_LOCATOR_PASS"
    assert scan["first_candidate"]["name"] == TARGET
    assert {row["name"] for row in scan["overlapping_first_candidates"]} == set(EVENT_FAMILY)

    source = pc.read_rows(SOURCE)
    endpoint = pc.read_rows(ENDPOINT)
    faces = json.loads(FACES_PATH.read_text())
    path = core.path_from_endpoints(source, endpoint)
    rows = list(core.primitive_rows(path, faces))
    assert len(rows) == 12363
    by_name = {name: polynomial for name, polynomial, _family in rows}
    target = by_name[TARGET]
    candidate = scan["first_candidate"]
    assert pc.root_count(target.c, Q(candidate["lo"]), Q(candidate["hi"])) == 1
    root = core.ex.isolate_monotone_root(
        target, Q(candidate["lo"]), Q(candidate["hi"]), core.ROOT_WIDTH
    )
    assert Q(0) < root["lo"] < root["hi"] < FAR_PARAMETER
    root_record = {
        "lo": core.ex.qs(root["lo"]),
        "hi": core.ex.qs(root["hi"]),
        "decimal_interval": [float(root["lo"]), float(root["hi"])],
        "value_lo": core.ex.qs(root["value_lo"]),
        "value_hi": core.ex.qs(root["value_hi"]),
        "derivative_sign": root["derivative_sign"],
        "derivative_bernstein_leaves": root["derivative_bernstein_leaves"],
        "polynomial_degree": target.degree,
        "polynomial_exact": target.exact(),
        "polynomial_digest": core.canonical_hash(target.exact()),
        "sturm_root_count": 1,
    }
    event_audit = exact_common_factor_audit(rows, root, target)
    pre_interval = {
        "exhaustive": core.exhaustive_strict_interval(rows, Q(0), root["lo"]),
        "class_cover": core.ex.certify_path_segment(
            core.restrict_path(path, Q(0), root["lo"]), faces, core.PROTECTED
        ),
    }
    wall_cover = core.ex.certify_mechanics_interval(
        path, faces, core.PROTECTED, root["lo"], root["hi"]
    )
    post_interval = {
        "exhaustive": core.exhaustive_strict_interval(
            rows, root["hi"], FAR_PARAMETER
        ),
        "class_cover": core.ex.certify_path_segment(
            core.restrict_path(path, root["hi"], FAR_PARAMETER),
            faces,
            core.PROTECTED,
        ),
    }
    for cover in (
        pre_interval["class_cover"], wall_cover, post_interval["class_cover"]
    ):
        key = "midpoint_class" if "midpoint_class" in cover else "start_class"
        assert cover[key]["class"] == [2, 4, 4]

    pre_points = core.evaluate_path(path, root["lo"])
    post_points = core.evaluate_path(path, root["hi"])
    far_points = core.evaluate_path(path, FAR_PARAMETER)
    checkpoints = {
        "source": core.checkpoint(source, faces, [61, 150, 91]),
        "pre": core.checkpoint(pre_points, faces, [61, 150, 91]),
        "post": core.checkpoint(post_points, faces, [61, 150, 91]),
        "far": core.checkpoint(far_points, faces, [61, 150, 91]),
    }
    residuals = core.residual_audit(source, far_points, faces, faces)
    pc.write_rows(FAR_OUT, far_points)
    payload = {
        "version": 1,
        "type": "exact class-preserving post-C17 own-centroid mechanics transfer",
        "scope": (
            "All 12,363 support/in-face/own-centroid primitives on the complete "
            "rational-affine segment, with exactly the declared two-polynomial "
            "zero family allowed at the isolated wall."
        ),
        "source_hashes": {
            str(file.relative_to(ATTACK)): core.sha256(file)
            for file in (SOURCE, FACES_PATH, ENDPOINT, PROPOSAL, SCAN)
        },
        "path": {
            "formula": "q_i(t)=source_i+t*(endpoint_i-source_i)",
            "root": root_record,
            "far_parameter": core.ex.qs(FAR_PARAMETER),
        },
        "event": {
            "zero_family": list(EVENT_FAMILY),
            "exact_zero_family_audit": event_audit,
            "wall_mechanics_cover": wall_cover,
            "interpretation": (
                "class-preserving transfer between edge (229,231) beta1 and "
                "the boundary component of face (229,231,247); support topology unchanged"
            ),
            "pre_f_vector": [61, 150, 91],
            "wall_f_vector": [61, 150, 91],
            "post_f_vector": [61, 150, 91],
            "class_transition": [[2, 4, 4], [2, 4, 4], [2, 4, 4]],
            "all_37_forced_rails_preserved": True,
        },
        "open_intervals": {"pre": pre_interval, "post": post_interval},
        "rational_parameters": {
            "source": "0",
            "pre": core.ex.qs(root["lo"]),
            "post": core.ex.qs(root["hi"]),
            "far": core.ex.qs(FAR_PARAMETER),
        },
        "rational_checkpoints": checkpoints,
        "directed_residuals": residuals,
        "generated_file_sha256": {
            str(FAR_OUT.relative_to(ATTACK)): core.sha256(FAR_OUT)
        },
        "verdict": "EXACT_POST_C17_FIRST_MECHANICS_TRANSFER_PASS",
        "winner_status": "NONWINNER",
        "next_action": "Rebuild the complete chart from transfer_far.csv in the same support cell.",
    }
    CERTIFICATE.write_text(json.dumps(payload, indent=2) + "\n")
    print(payload["verdict"])
    print("root", root_record["decimal_interval"])
    print("target_ratios", residuals["target_ratios_decimal"])
    print("certificate_sha256", core.sha256(CERTIFICATE))


if __name__ == "__main__":
    main()
