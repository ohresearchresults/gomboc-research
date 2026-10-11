#!/usr/bin/env python3
"""Scaled analytic Farkas search for a flip-atlas branch.

The finite-difference atlas is unreliable on ultrathin beta/support rows.
This locator instead uses the analytic dlog guard matrix materialized by
``rank4_flip_exact_trust_farkas.py``.  It searches the fixed-delta=1 Farkas
dual after scaling every primal inequality to unit infinity row norm:

    A c <= b infeasible  <=>  exists y>=0, A^T y=0, b^T y<0.

The normalization sum(y_scaled)=1 makes the ray search bounded.  Output from
this script is only an active-set proposal; the companion exact script must
replace every row and multiplier by Fractions and repair stationarity exactly.
"""
from __future__ import annotations

import argparse
import ast
import csv
import json
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


def read_rows_faces():
    rows = {}
    with (ATLAS / "row54_multiwall_flip.csv").open() as f:
        for row in csv.DictReader(f):
            rows[int(row["source_id"])] = tuple(Q(row[k]) for k in ("x", "y", "z"))
    faces = json.loads((ATLAS / "row54_multiwall_flip_faces.json").read_text())
    return rows, faces


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--branch", type=int, default=102)
    parser.add_argument("--method", choices=("highs", "highs-ds", "highs-ipm", "revised simplex", "simplex"), default="highs-ipm")
    args = parser.parse_args()

    saved = np.load(CACHE, allow_pickle=True)
    keys = [ast.literal_eval(str(z)) for z in saved["primitive_keys"]]
    displacement = np.asarray(saved["displacement"], dtype=float)
    deaths = tf.branch_deaths(keys, args.branch)
    analytic = np.load(ANALYTIC, allow_pickle=True)
    guard = np.asarray(analytic["guard_loss"], dtype=float)
    guard_keys = [ast.literal_eval(str(z)) for z in analytic["guard_keys"]]

    # Only four exact target rows are rebuilt here; the expensive 6301-row
    # analytic ledger is already materialized in ANALYTIC.
    rows, faces = read_rows_faces()
    q, _ = dr.build_mode_jets(rows, displacement)
    ledger = dr.ExactFractionalLedger(q, faces)
    death = np.asarray([[float(z) for z in ledger.row(key)[1]] for key in deaths])

    n = displacement.shape[1]
    eye = np.eye(n)
    a = np.vstack((guard, death, displacement, -displacement, eye, -eye))
    b = np.r_[
        np.ones(len(guard)),
        -np.ones(len(death)),
        np.full(len(displacement), 0.1),
        np.full(len(displacement), 0.1),
        np.full(n, 20.0),
        np.full(n, 20.0),
    ]
    scale = np.max(np.abs(a), axis=1)
    if np.any(scale <= 0) or not np.all(np.isfinite(scale)):
        raise AssertionError("invalid row scale")
    scaled_a = a / scale[:, None]
    scaled_b = b / scale
    aeq = np.vstack((scaled_a.T, np.ones(len(a))))
    beq = np.r_[np.zeros(n), 1.0]
    options = (
        {"primal_feasibility_tolerance": 1e-10, "dual_feasibility_tolerance": 1e-10}
        if args.method.startswith("highs") else
        {"tol": 1e-13, "maxiter": 250000, "presolve": True}
    )
    solve = linprog(
        scaled_b,
        A_eq=aeq,
        b_eq=beq,
        bounds=[(0.0, None)] * len(a),
        method=args.method,
        options=options,
    )
    if not solve.success:
        raise RuntimeError(solve.message)
    y_scaled = np.maximum(0.0, solve.x)
    y_original = y_scaled / scale
    residual = a.T @ y_original
    rhs = float(b @ y_original)
    offsets = {
        "guard": (0, len(guard)),
        "death": (len(guard), len(guard) + len(death)),
        "trust_plus": (len(guard) + len(death), len(guard) + len(death) + len(displacement)),
        "trust_minus": (len(guard) + len(death) + len(displacement),
                        len(guard) + len(death) + 2 * len(displacement)),
        "box_plus": (len(guard) + len(death) + 2 * len(displacement),
                     len(guard) + len(death) + 2 * len(displacement) + n),
        "box_minus": (len(guard) + len(death) + 2 * len(displacement) + n, len(a)),
    }
    support = np.flatnonzero(y_original > 1e-14)
    order = support[np.argsort(y_original[support])[::-1]]
    record = {
        "version": 1,
        "type": "scaled analytic Farkas active-set locator",
        "branch": args.branch,
        "deaths": [repr(z) for z in deaths],
        "method": args.method,
        "scaled_dual_objective": float(solve.fun),
        "original_farkas_rhs": rhs,
        "original_stationarity_inf_norm": float(np.max(np.abs(residual))),
        "scaled_multiplier_sum": float(np.sum(y_scaled)),
        "nonzero_original_multiplier_count_gt_1e-14": int(len(support)),
        "offsets": offsets,
        "multipliers_original_decimal": y_original.tolist(),
        "top_support": [],
    }
    for k in order[:80]:
        item = {"row": int(k), "weight": float(y_original[k])}
        if k < len(guard):
            item.update(group="guard", key=repr(guard_keys[k]))
        elif k < offsets["death"][1]:
            item.update(group="death", key=repr(deaths[k - offsets["death"][0]]))
        else:
            item["group"] = next(name for name, (lo, hi) in offsets.items() if lo <= k < hi)
            item["local_index"] = int(k - offsets[item["group"]][0])
        record["top_support"].append(item)
    path = HERE / f"rank4_flip_analytic_dual_branch{args.branch}.json"
    path.write_text(json.dumps(record, indent=2) + "\n")
    print("branch", args.branch, "deaths", record["deaths"])
    print("scaled objective", solve.fun, "original rhs", rhs)
    print("stationarity inf", np.max(np.abs(residual)), "support", len(support))
    for item in record["top_support"][:16]:
        print(item)
    print("output", path)


if __name__ == "__main__":
    main()
