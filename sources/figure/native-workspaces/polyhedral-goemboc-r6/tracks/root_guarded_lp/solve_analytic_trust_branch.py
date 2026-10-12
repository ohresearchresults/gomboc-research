#!/usr/bin/env python3
"""Solve one clean-flip branch using the analytic dlog first jet.

The parent guarded atlas uses a cached finite-difference primitive Jacobian.
This diagnostic keeps the same frozen 175 binary64 modes and physical
displacement map, but replaces all guard and death derivatives by the exact
analytic Fraction ledger before converting the resulting LP to binary64.
"""

from __future__ import annotations

import argparse
import ast
import importlib.util
import json
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


HERE = Path(__file__).resolve().parent
TRACKS = HERE.parent
PIECEWISE = TRACKS / "piecewise_transfer"
CACHE = HERE / "row54_flip_guarded_jacobian.npz"
ANALYTIC_CACHE = PIECEWISE / "rank4_flip_175_analytic_guard_rows.npz"
sys.path.insert(0, str(PIECEWISE))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--branch", type=int, required=True)
    parser.add_argument("--trust", type=float, default=0.1)
    parser.add_argument("--bound", type=float, default=20.0)
    parser.add_argument("--method", default="highs-ipm",
                        choices=("highs", "highs-ds", "highs-ipm"))
    parser.add_argument("--delta-cap", type=float,
                        help="solve feasibility with delta fixed at this cap")
    parser.add_argument("--output")
    args = parser.parse_args()

    dr = load_module(
        "rank4_flip_exact_directed_root",
        PIECEWISE / "rank4_flip_exact_directed.py",
    )
    tf = load_module(
        "rank4_flip_exact_trust_root",
        PIECEWISE / "rank4_flip_exact_trust_farkas.py",
    )

    saved = np.load(CACHE, allow_pickle=True)
    displacement = np.asarray(saved["displacement"], dtype=float)
    keys = [ast.literal_eval(str(z)) for z in saved["primitive_keys"]]
    deaths = tf.branch_deaths(keys, args.branch)
    analytic = np.load(ANALYTIC_CACHE, allow_pickle=True)
    guard_loss = np.asarray(analytic["guard_loss"], dtype=float)

    rows, faces = tf.read_rows_faces()
    q, _ = dr.build_mode_jets(rows, displacement)
    ledger = dr.ExactFractionalLedger(q, faces)
    death_rows = np.asarray([
        [float(z) for z in ledger.row(key)[1]] for key in deaths
    ])

    n = displacement.shape[1]
    ng = guard_loss.shape[0]
    nd = displacement.shape[0]
    if args.delta_cap is None:
        a_ub = np.vstack((
            np.hstack((guard_loss, -np.ones((ng, 1)))),
            np.hstack((displacement, np.zeros((nd, 1)))),
            np.hstack((-displacement, np.zeros((nd, 1)))),
            np.hstack((death_rows, np.zeros((len(deaths), 1)))),
        ))
        b_ub = np.r_[
            np.zeros(ng),
            np.full(nd, args.trust),
            np.full(nd, args.trust),
            np.full(len(deaths), -1.0),
        ]
        objective = np.r_[np.zeros(n), 1.0]
        variable_bounds = [(-args.bound, args.bound)] * n + [(-1000.0, 1000.0)]
    else:
        a_ub = np.vstack((guard_loss, displacement, -displacement, death_rows))
        b_ub = np.r_[
            np.full(ng, args.delta_cap),
            np.full(nd, args.trust),
            np.full(nd, args.trust),
            np.full(len(deaths), -1.0),
        ]
        objective = np.zeros(n)
        variable_bounds = [(-args.bound, args.bound)] * n
    solve = linprog(
        objective,
        A_ub=a_ub,
        b_ub=b_ub,
        bounds=variable_bounds,
        method=args.method,
        options={"presolve": True},
    )

    result = {
        "version": 1,
        "scope": "analytic-dlog clean-flip LP in frozen 175-mode physical trust box",
        "branch": args.branch,
        "deaths": [repr(key) for key in deaths],
        "method": args.method,
        "trust": args.trust,
        "bound": args.bound,
        "delta_cap": args.delta_cap,
        "success": bool(solve.success),
        "status": int(solve.status),
        "message": solve.message,
    }
    if solve.success:
        coefficient = np.asarray(solve.x[:n])
        guard_values = guard_loss @ coefficient
        death_values = death_rows @ coefficient
        physical = displacement @ coefficient
        result.update({
            "delta": float(solve.x[-1]) if args.delta_cap is None else args.delta_cap,
            "coefficients": coefficient.tolist(),
            "maximum_guard_loss": float(np.max(guard_values)),
            "minimum_guard_survival_at_unit_death": float(1.0 - np.max(guard_values)),
            "death_derivatives": death_values.tolist(),
            "maximum_coordinate_displacement": float(np.max(np.abs(physical))),
            "maximum_coefficient": float(np.max(np.abs(coefficient))),
            "worst_guard_index": int(np.argmax(guard_values)),
            "inequality_residual_max": float(np.max(a_ub @ solve.x - b_ub)),
        })
        if solve.ineqlin.marginals is not None:
            dual = np.maximum(0.0, -np.asarray(solve.ineqlin.marginals))
            result["dual_guard_mass"] = float(np.sum(dual[:ng]))
            result["dual_death_mass"] = float(np.sum(dual[ng + 2 * nd:]))
            result["dual_trust_mass"] = float(np.sum(dual[ng:ng + 2 * nd]))

    output = Path(args.output) if args.output else (
        HERE / (
            f"analytic_trust_branch{args.branch}_{args.method}.json"
            if args.delta_cap is None else
            f"analytic_trust_branch{args.branch}_delta{args.delta_cap:g}_{args.method}.json"
        )
    )
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result.get(key) for key in (
        "branch", "deaths", "success", "status", "message", "delta",
        "maximum_guard_loss", "minimum_guard_survival_at_unit_death",
        "death_derivatives", "maximum_coordinate_displacement",
        "inequality_residual_max", "dual_guard_mass", "dual_death_mass",
        "dual_trust_mass",
    )}, indent=2), flush=True)
    print("saved", output, flush=True)


if __name__ == "__main__":
    main()
