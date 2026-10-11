#!/usr/bin/env python3
"""Focused intrinsic base-plane actuator audit for the endpoint cell.

The broad scan adds an actual-cell direction after the projective map.  At a
large parameter this fixed seed tangent need not remain tangent to the mapped
base plane.  Here the candidate row is first moved in the source base plane,
then the projective map is applied.  Base coplanarity is therefore preserved
identically; fresh loss of the source cell cannot be blamed on an extrinsic
tangent convention.
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares


HERE = Path(__file__).resolve().parent


def load_scan():
    path = HERE / "rank6_row54_rail_scan.py"
    spec = importlib.util.spec_from_file_location("row54_rank_scan", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


SCAN = load_scan()


def main():
    stem = "row54_endpoint_rebuilt"
    checkpoint = json.loads((HERE / f"rank6_{stem}.json").read_text())
    ids, original, faces, _ = SCAN.read_cell(stem)
    control_basis = np.asarray(checkpoint["rank5_control_basis_8x5"], float)
    specs = checkpoint["wall_specs"] + [checkpoint["sixth_wall_spec"]]
    g6x5 = np.asarray(checkpoint["six_by_five_jacobian"], float)
    values6 = np.asarray(checkpoint["six_wall_seed_values"], float)
    candidates = [(11, "base_v"), (54, "base_v"), (54, "base_u"),
                  (1, "base_v"), (1, "base_u")]
    results = []
    for row, axis in candidates:
        response = next(
            z for z in checkpoint["top_remote_responses"]
            if z["row"] == row and z["axis"] == axis
        )
        vector = np.asarray(response["vector"], float)
        column = np.asarray(response["six_wall_column"], float)
        linear = np.linalg.solve(np.column_stack([g6x5, column]), -values6)
        starts = [linear, np.r_[checkpoint["rank5_nonlinear_root"], 0.0]]
        if row == 11 and axis == "base_v":
            extrinsic = next(
                z for z in checkpoint["nonlinear_rank6_completions"]
                if z["remote"]["row"] == row and z["remote"]["axis"] == axis
            )
            if extrinsic["nonlinear_parameters"] is not None:
                starts.insert(0, np.asarray(extrinsic["nonlinear_parameters"], float))
        row_index = ids.index(row)

        def points(x):
            moved = original.copy()
            moved[row_index] += x[5] * vector
            return SCAN.projective_cell(moved, control_basis @ x[:5])

        def residual(x):
            try:
                q, _ = points(x)
                z = SCAN.spec_values(ids, q, faces, specs)
                if np.all(np.isfinite(z)):
                    return z
            except Exception:
                pass
            return np.ones(6) * (100.0 + np.linalg.norm(x))

        trials = []
        for start in starts:
            sol = least_squares(
                residual, start, max_nfev=350, x_scale="jac",
                xtol=2e-11, ftol=2e-11, gtol=2e-11,
            )
            r = residual(sol.x)
            trials.append((float(np.max(np.abs(r))), sol, r))
        max_residual, sol, r = min(trials, key=lambda z: z[0])
        qevent, den = points(sol.x)
        qinside, _ = points(sol.x * (1.0 - 1e-5))
        try:
            fresh, _, _ = SCAN.R54.fresh_audit(ids, qinside, faces)
            rails = SCAN.rail_audit(ids, qinside)
        except Exception as exc:
            fresh = {"error": repr(exc), "faces_match_fixed_cell": False}
            rails = {"error": repr(exc), "all_37_forced_rails_present": False}
        result = {
            "row": row,
            "axis": axis,
            "vector": vector.tolist(),
            "left_null_response": response["left_null_response"],
            "absolute_response": response["absolute_response"],
            "linear_parameters": linear.tolist(),
            "best_parameters": sol.x.tolist(),
            "best_residuals": r.tolist(),
            "best_max_abs_residual": max_residual,
            "minimum_projective_denominator": float(np.min(den)),
            "actual_shared_event": max_residual < 2e-7,
            "one_sided_fresh_audit": fresh,
            "one_sided_rail_audit": rails,
            "solver_status": int(sol.status),
            "solver_nfev": int(sol.nfev),
        }
        results.append(result)
        print(
            row, axis, "residual", max_residual,
            "cell", fresh.get("faces_match_fixed_cell", False),
            "rails", rails.get("all_37_forced_rails_present", False),
            flush=True,
        )
    results.sort(key=lambda z: z["best_max_abs_residual"])
    out = {
        "version": 1,
        "type": "intrinsic pre-projective base-plane actuator audit",
        "cell": stem,
        "convention": (
            "Move the selected row along the seed base-plane tangent before normalization/projective map; "
            "then solve the same six scalar wall equations."
        ),
        "results": results,
        "accepted_fixed_cell_event": any(
            z["actual_shared_event"]
            and z["one_sided_fresh_audit"].get("faces_match_fixed_cell", False)
            and z["one_sided_rail_audit"].get("all_37_forced_rails_present", False)
            for z in results
        ),
    }
    path = HERE / "rank6_row54_intrinsic_actuator.json"
    path.write_text(json.dumps(out, indent=2) + "\n")
    print("ROW54_INTRINSIC_ACTUATOR_SCAN_PASS")
    print("accepted fixed-cell event", out["accepted_fixed_cell_event"])
    print("output", path)


if __name__ == "__main__":
    main()
