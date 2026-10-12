#!/usr/bin/env python3
"""Exact certificate for the second recovery2 safe support flip."""
from __future__ import annotations

import json
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ATTACK = MAIN.parents[1]
SOURCE = MAIN / "safe_flip_far.csv"
SOURCE_FACES = MAIN / "safe_flip_post_faces.json"
ENDPOINT = HERE / "candidate.csv"
PROPOSAL = HERE / "proposal.json"
SCAN = HERE / "first_event_scan.json"
CERTIFICATE = HERE / "certificate.json"
PRE_OUT = HERE / "pre.csv"
POST_OUT = HERE / "post.csv"
FAR_OUT = HERE / "far.csv"
WALL_FACES_OUT = HERE / "wall_faces.json"
POST_FACES_OUT = HERE / "post_faces.json"
sys.path.insert(0, str(MAIN))
sys.path.insert(0, str(ATTACK))

import certify_safe_flip as core  # noqa: E402
import post_c17_exact as pc  # noqa: E402


CIRCUIT = (3, 4, 88, 237)
REMOVED_FACES = ((3, 237, 4), (3, 88, 237))
ADDED_FACES = ((3, 88, 4), (4, 88, 237))
WALL_FACE = (3, 88, 237, 4)
REMOVED_EDGE = (3, 237)
ADDED_EDGE = (4, 88)
TARGET = "support:f71:w88"
EVENT_MULTIPLICITY = {
    "edge:(3, 237):beta1": 1,
    "edge:(3, 237):beta2": 1,
    "edge:(3, 237):gram": 2,
    "support:f71:w88": 1,
    "support:f72:w4": 1,
}
FAR_PARAMETER = Q(16)
EXPECTED_FIRST_CANDIDATE = "edge:(3, 237):beta1"
SUPPORT_WITNESSES = (88, 4)
CERTIFICATE_VERDICT = "EXACT_POST_C17_SECOND_SAFE_FLIP_PASS"
NEXT_ACTION = "Rebuild the chart from far.csv in the (4,88)-diagonal cell."


def configure_core():
    core.CIRCUIT = CIRCUIT
    core.REMOVED_FACES = REMOVED_FACES
    core.ADDED_FACES = ADDED_FACES
    core.WALL_FACE = WALL_FACE
    core.REMOVED_EDGE = REMOVED_EDGE
    core.ADDED_EDGE = ADDED_EDGE
    core.TARGET = TARGET
    core.EVENT_FAMILY = tuple(EVENT_MULTIPLICITY)
    core.EVENT_MULTIPLICITY = EVENT_MULTIPLICITY
    core.FAR_PARAMETER = FAR_PARAMETER


def main():
    configure_core()
    proposal = json.loads(PROPOSAL.read_text())
    scan = json.loads(SCAN.read_text())
    assert proposal["verdict"] == "RATIONAL_POST_SAFE_FLIP_DESCENT_PROPOSAL_PASS"
    assert scan["verdict"] == "EXHAUSTIVE_EXACT_POST_C17_FIXED_PLANE_FIRST_EVENT_LOCATOR_PASS"
    source = pc.read_rows(SOURCE)
    endpoint = pc.read_rows(ENDPOINT)
    path = core.path_from_endpoints(source, endpoint)
    pre_cycles, wall_cycles, post_cycles = core.build_face_ledgers(
        json.loads(SOURCE_FACES.read_text())
    )
    pre_rows = list(core.primitive_rows(path, pre_cycles))
    assert len(pre_rows) == 12363
    by_name = {name: polynomial for name, polynomial, _family in pre_rows}
    candidate = scan["first_candidate"]
    assert candidate["name"] == EXPECTED_FIRST_CANDIDATE
    target = by_name[TARGET]
    assert pc.root_count(target.c, Q(candidate["lo"]), Q(candidate["hi"])) == 1
    root = core.ex.isolate_monotone_root(
        target, Q(candidate["lo"]), Q(candidate["hi"]), core.ROOT_WIDTH
    )
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
    event_audit = core.exact_event_audit(pre_rows, root, target)
    first_support = core.ex.certify_first_support_wall(path, pre_cycles, root, target)
    expected_support = {
        (tuple(sorted(REMOVED_FACES[0])), SUPPORT_WITNESSES[0]),
        (tuple(sorted(REMOVED_FACES[1])), SUPPORT_WITNESSES[1]),
    }
    actual_support = {
        (tuple(sorted(pre_cycles[row["face_index"]])), row["witness"])
        for row in first_support["target_support_family"]
    }
    assert actual_support == expected_support

    pre_interval = {
        "exhaustive": core.exhaustive_strict_interval(
            pre_rows, Q(0), root["lo"]
        ),
        "class_cover": core.ex.certify_path_segment(
            core.restrict_path(path, Q(0), root["lo"]), pre_cycles, core.PROTECTED
        ),
    }
    wall_cover = core.ex.certify_mechanics_interval(
        path, wall_cycles, core.PROTECTED, root["lo"], root["hi"]
    )
    assert wall_cover["midpoint_class"]["class"] == [2, 4, 4]
    post_rows = list(core.primitive_rows(path, post_cycles))
    assert len(post_rows) == 12363
    post_interval = {
        "exhaustive": core.exhaustive_strict_interval(
            post_rows, root["hi"], FAR_PARAMETER
        ),
        "class_cover": core.ex.certify_path_segment(
            core.restrict_path(path, root["hi"], FAR_PARAMETER),
            post_cycles,
            core.PROTECTED,
        ),
    }

    pre_edges = core.edge_set(pre_cycles)
    wall_edges = core.edge_set(wall_cycles)
    post_edges = core.edge_set(post_cycles)
    assert pre_edges - post_edges == {REMOVED_EDGE}
    assert post_edges - pre_edges == {ADDED_EDGE}
    assert [len(pre_edges), len(wall_edges), len(post_edges)] == [150, 149, 150]
    assert all(not (pc.esc.forced_rails() - edges) for edges in (pre_edges, wall_edges, post_edges))

    pre_points = core.evaluate_path(path, root["lo"])
    post_points = core.evaluate_path(path, root["hi"])
    far_points = core.evaluate_path(path, FAR_PARAMETER)
    checkpoints = {
        "source": core.checkpoint(source, pre_cycles, [61, 150, 91]),
        "pre": core.checkpoint(pre_points, pre_cycles, [61, 150, 91]),
        "post": core.checkpoint(post_points, post_cycles, [61, 150, 91]),
        "far": core.checkpoint(far_points, post_cycles, [61, 150, 91]),
    }
    residuals = core.residual_audit(source, far_points, pre_cycles, post_cycles)
    pc.write_rows(PRE_OUT, pre_points)
    pc.write_rows(POST_OUT, post_points)
    pc.write_rows(FAR_OUT, far_points)
    WALL_FACES_OUT.write_text(json.dumps(wall_cycles, indent=2) + "\n")
    POST_FACES_OUT.write_text(json.dumps(post_cycles, indent=2) + "\n")
    generated = (PRE_OUT, POST_OUT, FAR_OUT, WALL_FACES_OUT, POST_FACES_OUT)
    payload = {
        "version": 1,
        "type": "exact second rational-affine post-C17 safe support flip",
        "scope": "All 12,363 support/in-face/own-centroid primitives in both strict cells, algebraic event family and exact checkpoints.",
        "source_hashes": {
            str(path.relative_to(ATTACK)): core.sha256(path)
            for path in (SOURCE, SOURCE_FACES, ENDPOINT, PROPOSAL, SCAN)
        },
        "path": {
            "formula": "q_i(t)=source_i+t*(endpoint_i-source_i)",
            "root": root_record,
            "far_parameter": core.ex.qs(FAR_PARAMETER),
        },
        "event": {
            "circuit": list(CIRCUIT),
            "removed_faces": [list(face) for face in REMOVED_FACES],
            "wall_face": list(WALL_FACE),
            "added_faces": [list(face) for face in ADDED_FACES],
            "removed_edge": list(REMOVED_EDGE),
            "added_edge": list(ADDED_EDGE),
            "pre_f_vector": [61, 150, 91],
            "wall_f_vector": [61, 149, 90],
            "post_f_vector": [61, 150, 91],
            "class_transition": [[2, 4, 4], [2, 4, 4], [2, 4, 4]],
            "first_support_wall": first_support,
            "exact_zero_family_audit": event_audit,
            "wall_mechanics_cover": wall_cover,
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
            str(path.relative_to(ATTACK)): core.sha256(path) for path in generated
        },
        "verdict": CERTIFICATE_VERDICT,
        "winner_status": "NONWINNER",
        "next_action": NEXT_ACTION,
    }
    CERTIFICATE.write_text(json.dumps(payload, indent=2) + "\n")
    print(payload["verdict"])
    print("root", root_record["decimal_interval"])
    print("target_ratios", residuals["target_ratios_decimal"])
    print("certificate_sha256", core.sha256(CERTIFICATE))


if __name__ == "__main__":
    main()
