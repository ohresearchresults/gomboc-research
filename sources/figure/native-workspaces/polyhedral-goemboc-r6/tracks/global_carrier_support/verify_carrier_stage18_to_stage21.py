#!/usr/bin/env python3
"""Audit the stage-18 branch choice and the successful vertex-6 transfer."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load(name):
    return json.loads((HERE / name).read_text())


def hard(summary):
    assert summary["f_vector"] == [61, 162, 103]
    assert summary["base_face_present"]
    assert not summary["missing_forced_rails"]


def main():
    stage18 = load("stage18_vertex_transfer_certificate.json")
    far = load("adaptive_stage19_far_carrier_cap_h67.json")
    pre = load("adaptive_stage19_pre_null_detour_h67.json")
    bypass = load("local_stage19_circuit_bypass_atlas.json")
    continued = load("adaptive_stage20_pre_postcircuit_guarded_h67.json")
    stage21 = load("stage21_vertex6_transfer_certificate.json")

    assert stage18["passed"]
    assert stage18["transition"]["classes"] == [
        [2, 2, 2], [2, 3, 3], [2, 2, 2]
    ]
    start = stage18["samples"]["pre"]["keep_decisions"]["H(6,7)"]

    far_pre = far["wall"]["pre_feature_values"]
    far_summary = far["wall"]["pre_summary"]
    hard(far_summary)
    assert far_summary["class"] == [2, 2, 2]
    far_reduction = 1.0 - far_pre["H(6,7)"] / start
    assert far_reduction > 0.05
    assert far["wall"]["post_diagnostics"]["summary"]["f_vector"] == [60, 159, 101]
    assert far["wall"]["post_diagnostics"]["summary"]["missing_forced_rails"] == [
        [249, 250], [250, 251]
    ]

    pre_first = pre["wall"]["pre_feature_values"]
    pre_first_summary = pre["wall"]["pre_summary"]
    hard(pre_first_summary)
    assert pre_first_summary["class"] == [2, 2, 2]
    assert pre_first["H(9,10)"] < pre["secondary_cap"]
    assert pre_first["H(10,11)"] < 0.0
    assert bypass["bypass_audit"]["bypass_found"]
    assert bypass["bypass_audit"]["hard_valid_everywhere"]
    assert bypass["bypass_audit"]["linked_birth_absent_everywhere"]

    continued_pre = continued["wall"]["pre_feature_values"]
    continued_summary = continued["wall"]["pre_summary"]
    hard(continued_summary)
    assert continued_summary["class"] == [2, 2, 2]
    pre_reduction = 1.0 - continued_pre["H(6,7)"] / start
    assert pre_reduction > 0.97
    assert continued_pre["H(9,10)"] < pre["secondary_cap"]
    assert continued_pre["H(10,11)"] < 0.0
    assert pre_reduction > far_reduction

    assert stage21["passed"]
    assert stage21["transition"]["classes"] == [
        [2, 2, 2], [2, 3, 3], [2, 2, 2]
    ]
    assert stage21["polynomials"]["5"]["actual_degree"] == 5
    assert stage21["polynomials"]["7"]["actual_degree"] == 5
    assert stage21["polynomials"]["5"]["root_float"] < stage21["polynomials"]["7"]["root_float"]
    far21 = stage21["samples"]["far"]
    hard(far21)
    assert far21["class"] == [2, 2, 2]
    assert far21["H(6, 7)"] < 0.0
    assert far21["H(5, 6)"] > 0.0
    assert far21["U6"] < 0.0

    payload = {
        "version": 1,
        "passed": True,
        "stage18_exact_transfer": {
            "roots": {
                key: row["root_float"]
                for key, row in stage18["polynomials"].items()
            },
            "root_gap": stage18["root_gap"]["float"],
            "classes": stage18["transition"]["classes"],
        },
        "branch_comparison": {
            "common_H67_start": start,
            "actual_far": {
                "H67_at_first_blocker": far_pre["H(6,7)"],
                "relative_reduction": far_reduction,
                "first_blocker": "vertex 250 loss; rails (249,250),(250,251) disappear",
            },
            "pre_null_detour": {
                "H67_before_vertex6_transfer": continued_pre["H(6,7)"],
                "relative_reduction": pre_reduction,
                "H910": continued_pre["H(9,10)"],
                "H1011": continued_pre["H(10,11)"],
                "same_cell_circuit_bypass": True,
            },
            "chosen": "pre_null_detour",
            "reason": "97% H67 descent versus 5% before the FAR rail blocker",
        },
        "stage21_exact_vertex6_transfer": {
            "birth_root_N5": stage21["polynomials"]["5"]["root_float"],
            "death_root_N7": stage21["polynomials"]["7"]["root_float"],
            "root_gap": stage21["root_gap"]["float"],
            "classes": stage21["transition"]["classes"],
            "far_H67": far21["H(6, 7)"],
            "far_H56": far21["H(5, 6)"],
            "far_U6": far21["U6"],
            "far_S": far21["keep_decisions"]["S(7,8,245)"],
            "far_U54": far21["keep_decisions"]["U54"],
            "f_vector": far21["f_vector"],
            "base_u8_all37_rails_preserved": True,
        },
    }
    output = HERE / "carrier_stage18_to_stage21_comparison.json"
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))
    print("CARRIER_STAGE18_TO_STAGE21_BRANCH_AND_EXACT_TRANSFER_PASS")


if __name__ == "__main__":
    main()
