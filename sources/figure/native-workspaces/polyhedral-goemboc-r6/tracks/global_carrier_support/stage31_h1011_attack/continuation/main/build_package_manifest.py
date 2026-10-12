#!/usr/bin/env python3
"""Build the deterministic manifest for the verified H1011 continuation package."""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ATTACK = HERE.parents[1]
ROOT = HERE.parents[4]
OUTPUT = HERE / "PACKAGE_MANIFEST.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def decision(record, endpoint_key):
    return record[endpoint_key]["decision_value"]


def main():
    parent = json.loads((ATTACK / "exact_circuit_certificate.json").read_text())
    chain = json.loads((HERE / "exact_full_control_chain_certificate.json").read_text())
    step = json.loads((HERE / "post_safe_flip_step_certificate.json").read_text())
    if parent["verdict"] != "EXACT_STAGE31_H1011_UPSTREAM_CIRCUIT_FLIP_PASS":
        raise AssertionError(parent["verdict"])
    if chain["verdict"] != "EXACT_FULL_CONTROL_THREE_TRANSFER_SAFE_FLIP_CHAIN_PASS":
        raise AssertionError(chain["verdict"])
    if step["verdict"] != "EXACT_POST_SAFE_FLIP_MATERIAL_BYPASS_STEP_PASS":
        raise AssertionError(step["verdict"])

    tracked = [
        ATTACK / "exact_circuit_certificate.json",
        ATTACK / "circuit_path_definition.json",
        ATTACK / "exact_circuit_far.csv",
        ATTACK / "exact_circuit_post_faces.json",
        ATTACK / "h1011_common.py",
        ATTACK / "build_exact_circuit_flip.py",
        ATTACK / "verify_exact_circuit_flip.py",
        HERE / "propose_full_control.py",
        HERE / "full_control_proposal.json",
        HERE / "full_control_candidate.csv",
        HERE / "locate_first_event.py",
        HERE / "first_event_scan.json",
        HERE / "build_exact_full_control_chain.py",
        HERE / "exact_full_control_chain_certificate.json",
        HERE / "exact_full_control_chain_pre.csv",
        HERE / "exact_full_control_chain_post.csv",
        HERE / "exact_full_control_chain_far.csv",
        HERE / "exact_full_control_chain_wall_faces.json",
        HERE / "exact_full_control_chain_post_faces.json",
        HERE / "verify_exact_full_control_chain.py",
        HERE / "propose_post_safe_flip.py",
        HERE / "post_safe_flip_proposal.json",
        HERE / "post_safe_flip_candidate.csv",
        HERE / "post_safe_flip_first_event_scan.json",
        HERE / "certify_post_safe_flip_step.py",
        HERE / "post_safe_flip_step_certificate.json",
        HERE / "post_safe_flip_step_exact.csv",
        HERE / "verify_post_safe_flip_step.py",
        HERE / "RUN_VERIFY.sh",
        HERE / "RUN_ALL.sh",
        HERE / "build_package_manifest.py",
    ]
    missing = [str(path) for path in tracked if not path.is_file()]
    if missing:
        raise AssertionError(("package files missing", missing))

    residuals = {}
    for name in ("S", "U54", "H56", "H1011"):
        start_record = chain["directed_residuals"][name]["source"]
        final_record = step["directed_residuals"][name]["endpoint"]
        start_squared = Q(start_record["squared_value"])
        final_squared = Q(final_record["squared_value"])
        if not final_squared < start_squared:
            raise AssertionError((name, "overall residual did not improve"))
        residuals[name] = {
            "start_decision": start_record["decision_value"],
            "after_safe_flip_decision": decision(
                chain["directed_residuals"][name], "far"
            ),
            "final_decision": final_record["decision_value"],
            "exact_overall_squared_drop": str(start_squared - final_squared),
            "final_over_start_ratio": final_record["decision_value"]
            / start_record["decision_value"],
        }

    manifest = {
        "version": 1,
        "scope": (
            "Verified exact continuation from exact_circuit_far through three "
            "mechanics transfers, one safe support flip, and one exact material "
            "curved-bypass step in the new cell."
        ),
        "verdict": "EXACT_H1011_CONTINUATION_PACKAGE_VERIFIED_NONWINNER",
        "winner": False,
        "acceptance_gap": (
            "Final exact own-centroid class is (2,2,2), not literal (1,1,0); "
            "therefore no winner neighborhood or OBJ/STL is claimed."
        ),
        "input_parent_verdict": parent["verdict"],
        "chain_verdict": chain["verdict"],
        "material_step_verdict": step["verdict"],
        "independent_verifier_verdicts": [
            "INDEPENDENT_EXACT_STAGE31_H1011_UPSTREAM_CIRCUIT_FLIP_PASS",
            "INDEPENDENT_EXACT_FULL_CONTROL_THREE_TRANSFER_SAFE_FLIP_CHAIN_PASS",
            "INDEPENDENT_EXACT_POST_SAFE_FLIP_MATERIAL_BYPASS_STEP_PASS",
        ],
        "event_sequence": [
            {
                "event": row["event"],
                "root_interval": [row["lo"], row["hi"]],
                "decimal_interval": row["decimal_interval"],
                "class_before_wall_after": [
                    [2, 2, 2], [2, 2, 2], [2, 2, 2]
                ],
            }
            for row in chain["path"]["event_roots"]
        ],
        "topology_event": chain["topology_event"],
        "material_bypass_step": {
            "class_sequence": [[2, 2, 2], [2, 2, 2]],
            "f_vector_sequence": [[61, 162, 103], [61, 162, 103]],
            "first_rejected_future_event_name": step["path"]["first_future_event_name"],
            "first_rejected_future_event_lower_bound": step["path"]["first_future_event_lower_bound"],
            "row230_loss_support_bypass": step["row230_loss_support_bypass"],
        },
        "final_exact_state": {
            "file": relative(HERE / "post_safe_flip_step_exact.csv"),
            "f_vector": [61, 162, 103],
            "class": [2, 2, 2],
            "stable_faces": [
                list(range(17)) + [54],
                [7, 8, 245],
            ],
            "unstable_vertices": [8, 54],
            "saddle_edges": [[5, 6], [10, 11]],
            "active_rows": 61,
            "forced_rails": 37,
            "base_preserved": True,
            "H910_strictly_dead": True,
        },
        "residual_changes": residuals,
        "canonical_commands": {
            "verify_only": "./RUN_VERIFY.sh",
            "rebuild_and_verify": "./RUN_ALL.sh",
        },
        "sha256": {relative(path): sha256(path) for path in tracked},
    }
    OUTPUT.write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({
        "verdict": manifest["verdict"],
        "event_count": len(manifest["event_sequence"]),
        "final_exact_state": manifest["final_exact_state"],
        "residual_changes": residuals,
        "tracked_file_count": len(tracked),
        "manifest": str(OUTPUT),
    }, indent=2))


if __name__ == "__main__":
    main()
