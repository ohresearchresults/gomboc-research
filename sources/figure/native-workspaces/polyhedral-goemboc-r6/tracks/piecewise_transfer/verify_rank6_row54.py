#!/usr/bin/env python3
"""Rebuild and verify the exact row-54 rank-5/6 certificates."""
from __future__ import annotations

import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ATLAS = ROOT / "tracks" / "circuit_atlas"


def run(script):
    subprocess.run([sys.executable, str(HERE / script)], check=True, cwd=ROOT)


def main():
    run("rank6_row54_exact_affine.py")
    exact = json.loads((HERE / "rank6_row54_exact_affine.json").read_text())
    assert len(exact["cells"]) == 2
    for cell in exact["cells"]:
        assert cell["ranks"] == {
            "five_wall_gradient_5x5": 5,
            "six_wall_gradient_6x5": 5,
            "six_wall_augmented_value_gradient_6x6": 6,
            "six_wall_with_row54_tangent_actuator_6x6": 6,
        }
        affine = cell["exact_local_affine_certificate"]
        assert affine["lambda_times_five_control_gradient_exact"] == ["0"] * 5
        assert affine["lambda_times_wall_values_exact"] != "0"
        lift = cell["exact_sixth_actuator_rank_lift"]
        assert lift["lambda_times_row54_tangent_column_exact"] != "0"
        assert lift["six_by_six_gradient_determinant_exact"] != "0"
        farkas = cell["exact_trust_box_inequality_farkas"]
        assert all(z > 0 for z in farkas["primitive_positive_integer_multipliers"])
        assert farkas["lambda_times_A_exact"] == ["0"] * 5
        assert Fraction(farkas["lambda_times_b_exact"]) < 0

    endpoint = json.loads((HERE / "rank6_row54_endpoint_rebuilt.json").read_text())
    far = json.loads((HERE / "rank6_row54_far_rebuilt.json").read_text())
    for record, stem in (
        (endpoint, "row54_endpoint_rebuilt"),
        (far, "row54_far_rebuilt"),
    ):
        source = json.loads((ATLAS / f"{stem}_audit.json").read_text())
        assert source["fresh_hull_audit"]["all_forced_rail_edges_present"]
        assert source["fresh_hull_audit"]["forced_rail_edge_count"] == 37
        assert record["six_by_five_rank"] == 5
        assert record["left_null_residual_norm"] < 1e-12
        assert record["local_affine_obstruction_absolute"] > 1e-5

    # Endpoint has an actual five-wall root in the unchanged rail cell.  Far
    # has no accepted root: retaining the nonzero residual and recording its
    # path singularity are part of the reported result.
    assert endpoint["rank5_nonlinear_max_abs_residual"] < 1e-12
    assert endpoint["rank5_root_fresh_audit"]["faces_match_fixed_cell"]
    assert far["rank5_nonlinear_max_abs_residual"] > 1e-6
    assert far["rank5_path_first_singularity"] is not None
    # An endpoint six-scalar algebraic root exists with a remote row-11
    # actuator, but its one-sided hull is not the supplied fixed cell.  No
    # completion may be advertised as a fixed-cell event.
    assert any(
        c["actual_shared_event"]
        and c["one_sided_rail_audit"].get("all_37_forced_rails_present", False)
        and not c["one_sided_faces_match_fixed_cell"]
        for c in endpoint["nonlinear_rank6_completions"]
    )
    assert not any(
        c["actual_shared_event"] and c["one_sided_faces_match_fixed_cell"]
        for r in (endpoint, far) for c in r["nonlinear_rank6_completions"]
    )
    intrinsic = json.loads((HERE / "rank6_row54_intrinsic_actuator.json").read_text())
    assert not intrinsic["accepted_fixed_cell_event"]
    assert min(z["best_max_abs_residual"] for z in intrinsic["results"]) > 1e-6
    assert all(
        z["one_sided_rail_audit"].get("all_37_forced_rails_present", False)
        and not z["one_sided_fresh_audit"].get("faces_match_fixed_cell", False)
        for z in intrinsic["results"]
    )
    print("ALL_ROW54_EXACT_RANK6_AND_NUMERICAL_SCOPE_VERIFIERS_PASS")


if __name__ == "__main__":
    main()
