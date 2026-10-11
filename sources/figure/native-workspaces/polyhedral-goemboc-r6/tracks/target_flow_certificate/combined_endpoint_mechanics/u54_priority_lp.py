#!/usr/bin/env python3
"""Guard-aware U54-priority frontier in the epoch-5 actual cell.

Unlike the equal-rate four-death LP, this program preserves the other three
fixed residuals only monotonically and drives U54 at a requested fractional
rate.  Every H67/H910 primitive-component pair is enumerated; the historically
tracked H67=1-t and H910=t rows are always protected as well.
"""
from __future__ import annotations

from pathlib import Path
import argparse
import ast
import json

import numpy as np
from scipy.optimize import linprog

import combined_four_death_lp as four


HERE = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="epoch4_cluster_event3_deep_after.csv")
    parser.add_argument("--jacobian", default="epoch5_lp_jacobian.npz")
    parser.add_argument("--prefix", default="u54_priority_lp")
    parser.add_argument("--bound", type=float, default=300.0)
    parser.add_argument("--plane-tol", type=float, default=1e-11)
    parser.add_argument(
        "--rates", default="1,2,5,10,20,50,100,200",
        help="comma-separated required negative fractional U54 derivatives",
    )
    args = parser.parse_args()

    four.ACTIVE_PLANE_TOL = args.plane_tol
    source = Path(args.source)
    points = four.load_points(source)
    result, values = four.primitive_ledger(points)
    modes, mode_meta, _chart = four.chart_modes(points)
    data = np.load(args.jacobian, allow_pickle=True)
    jacobian = np.asarray(data["jacobian"], dtype=float)
    keys = [ast.literal_eval(str(item)) for item in data["primitive_keys"]]
    key_index = {key: index for index, key in enumerate(keys)}
    if jacobian.shape[1] != len(modes):
        raise RuntimeError("Jacobian/chart dimension mismatch")

    quad = next(
        key for key in values
        if key[0] == "face" and frozenset(key[1]) == four.QUAD and key[2] == (8, 246)
    )
    u54 = ("vertex", 54, 1)
    fixed_h67 = ("edge", (6, 7), "one_minus_t")
    fixed_h910 = ("edge", (9, 10), "t")
    h67 = sorted(key for key in values if key[0] == "edge" and key[1] == (6, 7))
    h910 = sorted(key for key in values if key[0] == "edge" and key[1] == (9, 10))

    def fractional_row(key):
        return jacobian[key_index[key]] / values[key]

    r_quad = fractional_row(quad)
    r_u54 = fractional_row(u54)
    r_fixed_h67 = fractional_row(fixed_h67)
    r_fixed_h910 = fractional_row(fixed_h910)

    guards = four.chosen_guards(values)
    guard_matrix = []
    guard_info = []
    for key, sign, kind in guards:
        scale = max(abs(values[key]), 1e-12)
        guard_matrix.append(-sign * jacobian[key_index[key]] / scale)
        guard_info.append({
            "key": repr(key), "kind": kind, "value": values[key], "sign": sign,
        })
    guard_matrix = np.asarray(guard_matrix)
    n = len(modes)
    coefficient_bounds = [(-args.bound, args.bound)] * n
    rates = [float(rate) for rate in args.rates.split(",")]

    # Pure differential U54-nullspace direction, included as a branch-agnostic
    # geometric comparator rather than a guard-feasible certificate.
    preserve = np.vstack((r_quad, r_fixed_h67, r_fixed_h910))
    _u, singular_values, vt = np.linalg.svd(preserve, full_matrices=True)
    rank = int(np.linalg.matrix_rank(preserve))
    null_basis = vt[rank:].T
    projected_u54 = null_basis @ (null_basis.T @ r_u54)
    null_direction = -projected_u54
    null_direction *= args.bound / max(np.max(np.abs(null_direction)), 1e-300)

    records = []
    for key67 in h67:
        for key910 in h910:
            preserve_rows = [
                r_quad,
                fractional_row(key67),
                fractional_row(key910),
                r_fixed_h67,
                r_fixed_h910,
            ]
            # Remove duplicate numerical rows without changing their semantics.
            unique_rows = []
            for row in preserve_rows:
                if not any(np.array_equal(row, old) for old in unique_rows):
                    unique_rows.append(row)

            for required_rate in rates:
                # Variables are [c, delta]. Guards minimize the worst signed
                # fractional worsening; U54 gets the requested rate and every
                # protected defect is nonincreasing.
                A = [np.hstack((guard_matrix, -np.ones((len(guards), 1))))]
                b = [np.zeros(len(guards))]
                A.append(np.asarray([np.r_[row, 0.0] for row in unique_rows]))
                b.append(np.zeros(len(unique_rows)))
                A.append(np.asarray([np.r_[r_u54, 0.0]]))
                b.append(np.asarray([-required_rate]))
                A_ub = np.vstack(A)
                b_ub = np.concatenate(b)
                objective = np.r_[np.zeros(n), 1.0]
                lp = linprog(
                    objective,
                    A_ub=A_ub,
                    b_ub=b_ub,
                    bounds=coefficient_bounds + [(-1e6, 1e6)],
                    method="highs",
                )
                record = {
                    "h67_component": key67[2],
                    "h910_component": key910[2],
                    "required_u54_rate": required_rate,
                    "success": bool(lp.success),
                    "message": lp.message,
                }
                if lp.success:
                    coefficients = np.asarray(lp.x[:n])
                    worsening = guard_matrix @ coefficients
                    order = np.argsort(worsening)[-20:][::-1]
                    fixed_rates = {
                        "quad": float(r_quad @ coefficients),
                        "u54": float(r_u54 @ coefficients),
                        "h67_one_minus_t": float(r_fixed_h67 @ coefficients),
                        "h910_t": float(r_fixed_h910 @ coefficients),
                        "selected_h67": float(fractional_row(key67) @ coefficients),
                        "selected_h910": float(fractional_row(key910) @ coefficients),
                    }
                    record.update({
                        "delta": float(lp.x[-1]),
                        "coefficients": coefficients.tolist(),
                        "max_abs_coefficient": float(np.max(np.abs(coefficients))),
                        "l2_coefficient": float(np.linalg.norm(coefficients)),
                        "fractional_rates": fixed_rates,
                        "top_guard_blockers": [
                            {**guard_info[index], "fractional_worsening": float(worsening[index])}
                            for index in order
                        ],
                        "active_modes": [
                            {"column": int(index), "coefficient": float(coefficients[index]), **mode_meta[index]}
                            for index in np.argsort(np.abs(coefficients))[-20:][::-1]
                        ],
                    })
                    if lp.ineqlin.marginals is not None:
                        dual = -np.asarray(lp.ineqlin.marginals)
                        record["dual_certificate"] = {
                            "objective": float(lp.fun),
                            "guard_dual_l1": float(np.sum(dual[:len(guards)])),
                            "u54_rate_dual": float(dual[-1]),
                            "largest_guard_duals": [
                                {**guard_info[index], "dual_weight": float(dual[index])}
                                for index in np.argsort(dual[:len(guards)])[-20:][::-1]
                                if dual[index] > 1e-10
                            ],
                        }
                records.append(record)

    successful = [record for record in records if record.get("success")]
    successful.sort(key=lambda record: (record["delta"], -record["required_u54_rate"]))
    pareto = []
    best_delta = float("inf")
    for record in sorted(successful, key=lambda row: row["required_u54_rate"]):
        if record["delta"] < best_delta - 1e-10:
            pareto.append(record)
            best_delta = record["delta"]

    payload = {
        "version": 1,
        "scope": "epoch-5 full-chart U54-priority guarded component frontier",
        "source": args.source,
        "jacobian": args.jacobian,
        "f_vector": [len(result.active), len(result.edges), len(result.faces)],
        "class": [len(result.stable), len(result.unstable), len(result.saddles)],
        "modes": n,
        "guards": len(guards),
        "bound": args.bound,
        "fixed_preserved_components": [repr(quad), repr(fixed_h67), repr(fixed_h910)],
        "nullspace_comparator": {
            "preserve_rank": rank,
            "preserve_singular_values": singular_values.tolist(),
            "nullity": int(null_basis.shape[1]),
            "u54_projection_norm": float(np.linalg.norm(projected_u54)),
            "coefficients": null_direction.tolist(),
            "fractional_rates": {
                "quad": float(r_quad @ null_direction),
                "u54": float(r_u54 @ null_direction),
                "h67_one_minus_t": float(r_fixed_h67 @ null_direction),
                "h910_t": float(r_fixed_h910 @ null_direction),
            },
            "max_guard_worsening": float(np.max(guard_matrix @ null_direction)),
        },
        "records": records,
        "best_by_delta": successful[:20],
        "pareto": pareto,
    }
    prefix = HERE / args.prefix
    prefix.with_suffix(".json").write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "nullspace_comparator": payload["nullspace_comparator"],
        "best_by_delta": [
            {
                "h67": row["h67_component"],
                "h910": row["h910_component"],
                "required_u54_rate": row["required_u54_rate"],
                "delta": row["delta"],
                "rates": row["fractional_rates"],
            }
            for row in successful[:20]
        ],
    }, indent=2))


if __name__ == "__main__":
    main()
