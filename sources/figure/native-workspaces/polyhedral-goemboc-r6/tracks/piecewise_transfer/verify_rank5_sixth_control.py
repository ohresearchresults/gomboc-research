#!/usr/bin/env python3
"""Regenerate and verify the support-valid sixth-control obstruction."""
from __future__ import annotations

import json
import subprocess
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
sys.set_int_max_str_digits(0)


def main():
    subprocess.run([sys.executable, str(HERE / "rank5_sixth_control.py")], check=True)
    record = json.loads((HERE / "rank5_sixth_control.json").read_text())
    assert record["verdict"] == "EXACT_RANK6_SUPPORT_CONTROL_VALID_BUT_TRUST_BOX_TARGET_INFEASIBLE"
    sixth = record["sixth_control"]
    assert sixth["row"] == 246
    assert [Q(z) for z in sixth["direction_exact"]] == [Q(-7), Q(8), Q(-90)]
    assert Q(sixth["normal_dot_direction_exact"]) == 0
    probes = sixth["support_valid_exact_actual_hull_probes"]
    assert {probe["sign"] for probe in probes} == {-1, 1}
    for probe in probes:
        assert Q(probe["max_abs_coordinate_displacement_exact"]) == Q(1, 10)
        assert Q(probe["shell_plane_value_exact"]) == 3700
        assert probe["f_vector"] == [61, 150, 91]
        assert probe["class"] == [3, 4, 5]
        assert probe["base_stable"] is True
        assert probe["U8_unstable"] is True
        assert probe["forced_rails_present"] == 37
        assert probe["all_37_forced_rails_present"] is True

    exact_rank = record["exact_rank"]
    assert exact_rank["six_by_six_gradient_rank"] == 6
    assert Q(exact_rank["gradient_determinant_exact"]) != 0

    root = record["unique_affine_common_root"]
    assert root["outside_physical_trust_1_over_10"] is True
    assert Q(root["max_abs_physical_displacement_exact"]) > Q(1, 10)
    audit = root["fresh_actual_hull_audit"]
    assert audit["valid"] is True
    assert audit["exact_all_proposed_planes_support_all_119_rows"] is True
    assert audit["exact_mass_centroid_and_mechanics_rebuilt"] is True
    assert audit["f_vector"] == [24, 65, 43]
    assert audit["class"] == [3, 5, 6]
    assert audit["base_face_present"] is False
    assert audit["U8_unstable"] is False
    assert audit["forced_rails_present"] == 20
    assert audit["all_37_forced_rails_present"] is False
    assert len(audit["missing_forced_rails"]) == 17
    assert audit["unstable_vertices"] == [228, 232, 245, 246, 254]

    cert = record["physical_trust_farkas_certificate"]
    assert cert["row_count"] == 42
    assert len(cert["necessary_death_inequalities"]) == 6
    assert cert["exact_stationarity_all_6_columns_zero"] is True
    assert cert["all_exact_multipliers_nonnegative"] is True
    assert cert["strictly_negative_farkas_rhs"] is True
    assert Q(cert["repaired_farkas_rhs_exact"]) < 0
    assert all(Q(row["weight_exact"]) > 0 for row in cert["positive_locator_support"])
    assert all(
        Q(row["weight_exact"]) >= 0
        for row in cert["exact_stationarity_repair_with_physical_trust_rows"]
    )
    print("ALL_EXACT_RANK5_SIXTH_SUPPORT_CONTROL_VERIFIERS_PASS")


if __name__ == "__main__":
    main()
