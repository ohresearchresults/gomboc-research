#!/usr/bin/env python3
"""Complete 144-branch analytic-dlog Farkas atlas at physical trust R=.1.

All branches share one cached 6301-row analytic guard matrix, the same frozen
175 binary64 modes, physical displacement trust rows, and coefficient box.
Only four death-component rows change.  For every branch this script solves
the row-scaled, normalized Farkas ray LP for the fixed delta=1 system and
records the dual objective.  A negative objective is a numerical analytic
infeasibility proposal; the branch closest to zero must be exactified with
``rank4_flip_exact_analytic_farkas.py``.
"""
from __future__ import annotations

import argparse
import ast
import csv
import json
import multiprocessing as mp
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

import rank4_flip_exact_directed as dr
import rank4_flip_exact_trust_farkas as tf


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ATLAS = ROOT / "tracks" / "circuit_atlas"
ROOT_LP = ROOT / "tracks" / "root_guarded_lp"
CACHE = ROOT_LP / "row54_flip_guarded_jacobian.npz"
ANALYTIC = HERE / "rank4_flip_175_analytic_guard_rows.npz"
OUTPUT = HERE / "rank4_flip_analytic_dual_atlas.json"

G = {}


def read_rows_faces():
    rows = {}
    with (ATLAS / "row54_multiwall_flip.csv").open() as f:
        for row in csv.DictReader(f):
            rows[int(row["source_id"])] = tuple(Q(row[k]) for k in ("x", "y", "z"))
    faces = json.loads((ATLAS / "row54_multiwall_flip_faces.json").read_text())
    return rows, faces


def solve_branch(branch):
    death = G["death_rows"][branch]
    death_scale = np.max(np.abs(death), axis=1)
    scaled_death = death / death_scale[:, None]
    b_death = -np.ones(4) / death_scale
    scaled_a = np.vstack((G["guard_scaled"], scaled_death, G["rest_scaled"]))
    scaled_b = np.r_[G["guard_b"], b_death, G["rest_b"]]
    aeq = np.vstack((scaled_a.T, np.ones(len(scaled_a))))
    beq = np.r_[np.zeros(175), 1.0]
    try:
        method = G["method"]
        options = (
            {"primal_feasibility_tolerance": 1e-10, "dual_feasibility_tolerance": 1e-10}
            if method.startswith("highs") else
            {"tol": 1e-13, "maxiter": 250000, "presolve": True}
        )
        solve = linprog(
            scaled_b,
            A_eq=aeq,
            b_eq=beq,
            bounds=[(0.0, None)] * len(scaled_a),
            method=method,
            options=options,
        )
        record = {
            "branch": branch,
            "deaths": [repr(z) for z in G["death_keys"][branch]],
            "success": bool(solve.success),
            "status": int(solve.status),
            "message": str(solve.message),
        }
        if solve.success:
            y_scaled = np.maximum(0.0, solve.x)
            scale = np.r_[G["guard_scale"], death_scale, G["rest_scale"]]
            y = y_scaled / scale
            original_a = np.vstack((G["guard"], death, G["rest"]))
            original_b = np.r_[np.ones(len(G["guard"])), -np.ones(4), G["rest_original_b"]]
            residual = original_a.T @ y
            record.update(
                scaled_dual_objective=float(solve.fun),
                original_farkas_rhs=float(original_b @ y),
                original_stationarity_inf_norm=float(np.max(np.abs(residual))),
                support_gt_1e_14=int(np.sum(y > 1e-14)),
                fixed_delta_one_numerical_verdict=(
                    "ANALYTIC_INFEASIBILITY_RAY" if solve.fun < 0 else "NO_NEGATIVE_RAY_FOUND"
                ),
            )
            if G["save_weights"]:
                record["multipliers_original_decimal"] = y.tolist()
        return record
    except Exception as exc:
        return {
            "branch": branch,
            "deaths": [repr(z) for z in G["death_keys"][branch]],
            "success": False,
            "status": -999,
            "message": repr(exc),
        }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--method", choices=("highs-ipm", "revised simplex"), default="highs-ipm")
    parser.add_argument("--save-weights", action="store_true")
    parser.add_argument("--output")
    args = parser.parse_args()

    saved = np.load(CACHE, allow_pickle=True)
    primitive_keys = [ast.literal_eval(str(z)) for z in saved["primitive_keys"]]
    displacement = np.asarray(saved["displacement"], dtype=float)
    analytic = np.load(ANALYTIC, allow_pickle=True)
    guard = np.asarray(analytic["guard_loss"], dtype=float)

    rows, faces = read_rows_faces()
    q, _ = dr.build_mode_jets(rows, displacement)
    ledger = dr.ExactFractionalLedger(q, faces)
    packets = tf.death_packets(primitive_keys)
    component_rows = {
        key: np.asarray([float(z) for z in ledger.row(key)[1]])
        for packet in packets for key in packet
    }
    death_keys = [tf.branch_deaths(primitive_keys, branch) for branch in range(144)]
    death_rows = [np.asarray([component_rows[key] for key in deaths]) for deaths in death_keys]

    eye = np.eye(175)
    rest = np.vstack((displacement, -displacement, eye, -eye))
    rest_original_b = np.r_[
        np.full(len(displacement), 0.1),
        np.full(len(displacement), 0.1),
        np.full(175, 20.0),
        np.full(175, 20.0),
    ]
    guard_scale = np.max(np.abs(guard), axis=1)
    rest_scale = np.max(np.abs(rest), axis=1)
    if np.any(guard_scale <= 0) or np.any(rest_scale <= 0):
        raise AssertionError("zero row")
    G.update(
        guard=guard,
        guard_scale=guard_scale,
        guard_scaled=guard / guard_scale[:, None],
        guard_b=np.ones(len(guard)) / guard_scale,
        rest=rest,
        rest_scale=rest_scale,
        rest_scaled=rest / rest_scale[:, None],
        rest_b=rest_original_b / rest_scale,
        rest_original_b=rest_original_b,
        death_keys=death_keys,
        death_rows=death_rows,
        method=args.method,
        save_weights=args.save_weights,
    )

    # Fork after the common matrices are built so workers share copy-on-write
    # pages instead of serializing the 6301x175 guard ledger per branch.
    context = mp.get_context("fork")
    results = []
    with context.Pool(processes=args.workers) as pool:
        for record in pool.imap_unordered(solve_branch, range(144), chunksize=1):
            results.append(record)
            print("branch", record["branch"], "success", record["success"],
                  "objective", record.get("scaled_dual_objective"), flush=True)
    results.sort(key=lambda z: z["branch"])
    successful = [z for z in results if z["success"]]
    negative = [z for z in successful if z["scaled_dual_objective"] < 0]
    closest_negative = max(negative, key=lambda z: z["scaled_dual_objective"]) if negative else None
    most_negative = min(negative, key=lambda z: z["scaled_dual_objective"]) if negative else None
    output = {
        "version": 1,
        "type": "complete row-scaled analytic-dlog fixed-delta Farkas atlas",
        "scope": (
            "Numerical active-set atlas on one analytic 6301-row guard ledger, 14 exact-analytic "
            "death components, frozen 175-mode chart, physical trust R=.1, and coefficient box 20. "
            "Negative rays require exactification."
        ),
        "branch_count": 144,
        "successful_count": len(successful),
        "negative_ray_count": len(negative),
        "all_144_have_negative_analytic_ray": len(negative) == 144,
        "closest_negative_branch": closest_negative,
        "most_negative_branch": most_negative,
        "branches": results,
    }
    output_path = Path(args.output) if args.output else OUTPUT
    output_path.write_text(json.dumps(output, indent=2) + "\n")
    print("successful/negative", len(successful), len(negative))
    print("closest negative", closest_negative)
    print("output", output_path)


if __name__ == "__main__":
    main()
