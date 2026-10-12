#!/usr/bin/env python3
"""Lexicographic material-improvement LP in the final epoch-5 actual cell.

The earlier U54 frontier deliberately treated H910 only monotonically.  That
cannot by itself lower the *worst* canonical residual below 0.98: after U54,
H910(t) is the second bottleneck.  Here every primitive H67/H910 branch is
enumerated while the canonical U54 and H910(t) rows are both required to reach
0.98 in their original-combined-wall normalization.  The primary objective is
the same signed full-ledger guard minimax.  A second LP keeps that optimum
within a small relative tolerance and minimizes max chart displacement, which
is the useful nonlinear actual-cell candidate.
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
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default="epoch4_cluster_event3_deep_after.csv")
    ap.add_argument("--jacobian", default="epoch5_lp_jacobian.npz")
    ap.add_argument("--prefix", default="u54_material_lp")
    ap.add_argument("--target", type=float, default=0.98)
    ap.add_argument(
        "--quad-buffer", type=float, default=0.0,
        help="required negative fractional quad change (nonlinear monotonicity buffer)",
    )
    ap.add_argument(
        "--h67-buffer", type=float, default=0.0,
        help="required negative fractional H67(1-t) change",
    )
    ap.add_argument("--bound", type=float, default=300.0)
    ap.add_argument("--delta-slack", type=float, default=0.01)
    ap.add_argument("--plane-tol", type=float, default=1e-11)
    ap.add_argument("--h67-component", help="optional single H67 component")
    ap.add_argument("--h910-component", help="optional single H910 component")
    ap.add_argument(
        "--fixed-only", action="store_true",
        help="regularize only canonical quad/H67 rows; component atlas is supplied by u54_priority_lp",
    )
    args = ap.parse_args()

    source = four.load_points(args.source)
    result, values = four.primitive_ledger(source, plane_tol=args.plane_tol)
    modes, mode_meta, _ = four.chart_modes(source)
    data = np.load(args.jacobian, allow_pickle=True)
    jacobian = np.asarray(data["jacobian"], dtype=float)
    keys = [ast.literal_eval(str(item)) for item in data["primitive_keys"]]
    key_index = {key: i for i, key in enumerate(keys)}

    quad = next(
        key for key in values
        if key[0] == "face" and frozenset(key[1]) == four.QUAD and key[2] == (8, 246)
    )
    u54 = ("vertex", 54, 1)
    fixed_h67 = ("edge", (6, 7), "one_minus_t")
    fixed_h910 = ("edge", (9, 10), "t")
    h67 = sorted(key for key in values if key[0] == "edge" and key[1] == (6, 7))
    h910 = sorted(key for key in values if key[0] == "edge" and key[1] == (9, 10))
    if args.h67_component:
        h67 = [key for key in h67 if key[2] == args.h67_component]
    if args.h910_component:
        h910 = [key for key in h910 if key[2] == args.h910_component]
    if not h67 or not h910:
        raise ValueError("requested component filter is absent")

    canonical = four.load_points(HERE / "../../circuit_atlas/row54_combined_wall_rebuilt.csv")
    _canonical_result, canonical_values = four.primitive_ledger(
        canonical, plane_tol=args.plane_tol
    )
    current_ratios = {
        "quad": float(values[quad] / canonical_values[quad]),
        "u54": float(values[u54] / canonical_values[u54]),
        "h67_one_minus_t": float(values[fixed_h67] / canonical_values[fixed_h67]),
        "h910_t": float(values[fixed_h910] / canonical_values[fixed_h910]),
    }
    required_fractional = {
        "u54": float(args.target / current_ratios["u54"] - 1.0),
        "h910_t": float(args.target / current_ratios["h910_t"] - 1.0),
    }

    def fractional_row(key):
        return jacobian[key_index[key]] / values[key]

    r_quad = fractional_row(quad)
    r_u54 = fractional_row(u54)
    r_h67 = fractional_row(fixed_h67)
    r_h910 = fractional_row(fixed_h910)

    guards = four.chosen_guards(values)
    guard_matrix, guard_info = [], []
    for key, sign, kind in guards:
        scale = max(abs(values[key]), 1e-12)
        guard_matrix.append(-sign * jacobian[key_index[key]] / scale)
        guard_info.append({
            "key": repr(key), "kind": kind, "value": float(values[key]), "sign": sign,
        })
    guard_matrix = np.asarray(guard_matrix)
    n = len(modes)
    records = []

    for key67 in h67:
        for key910 in h910:
            preserve = [
                (r_quad, -args.quad_buffer),
                (r_h67, -args.h67_buffer),
            ]
            if not args.fixed_only:
                preserve.extend([
                    (fractional_row(key67), 0.0),
                    (fractional_row(key910), 0.0),
                ])
            # H910(t) has a strict material target below; keep it out of the
            # merely-monotone set to avoid a duplicate inequality.
            unique, unique_rhs = [], []
            for row, rhs in preserve:
                duplicate = next(
                    (i for i, old in enumerate(unique) if np.array_equal(row, old)), None
                )
                if duplicate is None:
                    unique.append(row)
                    unique_rhs.append(rhs)
                else:
                    unique_rhs[duplicate] = min(unique_rhs[duplicate], rhs)

            primary_A = [np.c_[guard_matrix, -np.ones(len(guards))]]
            primary_b = [np.zeros(len(guards))]
            primary_A.append(np.asarray([np.r_[row, 0.0] for row in unique]))
            primary_b.append(np.asarray(unique_rhs))
            primary_A.append(np.asarray([np.r_[r_u54, 0.0], np.r_[r_h910, 0.0]]))
            primary_b.append(np.asarray([
                required_fractional["u54"], required_fractional["h910_t"]
            ]))
            primary = linprog(
                np.r_[np.zeros(n), 1.0],
                A_ub=np.vstack(primary_A), b_ub=np.concatenate(primary_b),
                bounds=[(-args.bound, args.bound)] * n + [(-1e6, 1e6)],
                method="highs",
            )
            record = {
                "h67_component": key67[2],
                "h910_component": key910[2],
                "success": bool(primary.success),
                "message": primary.message,
            }
            if not primary.success:
                records.append(record)
                continue

            delta = float(primary.x[-1])
            delta_cap = delta * (1.0 + args.delta_slack) + 1e-10
            # Variables [d, t].  The guard budget is lexicographically fixed,
            # and +/-d_j <= t minimizes the largest actual chart displacement.
            second_A = [np.c_[guard_matrix, np.zeros(len(guards))]]
            second_b = [np.full(len(guards), delta_cap)]
            second_A.append(np.asarray([np.r_[row, 0.0] for row in unique]))
            second_b.append(np.asarray(unique_rhs))
            second_A.append(np.asarray([np.r_[r_u54, 0.0], np.r_[r_h910, 0.0]]))
            second_b.append(np.asarray([
                required_fractional["u54"], required_fractional["h910_t"]
            ]))
            second_A.extend([
                np.c_[np.eye(n), -np.ones(n)],
                np.c_[-np.eye(n), -np.ones(n)],
            ])
            second_b.extend([np.zeros(n), np.zeros(n)])
            secondary = linprog(
                np.r_[np.zeros(n), 1.0],
                A_ub=np.vstack(second_A), b_ub=np.concatenate(second_b),
                bounds=[(None, None)] * n + [(0.0, args.bound)],
                method="highs",
            )
            if not secondary.success:
                record.update({
                    "delta": delta,
                    "secondary_success": False,
                    "secondary_message": secondary.message,
                })
                records.append(record)
                continue

            displacement = np.asarray(secondary.x[:n])
            worsening = guard_matrix @ displacement
            order = np.argsort(worsening)[-20:][::-1]
            rates = {
                "quad": float(r_quad @ displacement),
                "u54": float(r_u54 @ displacement),
                "h67_one_minus_t": float(r_h67 @ displacement),
                "h910_t": float(r_h910 @ displacement),
                "selected_h67": float(fractional_row(key67) @ displacement),
                "selected_h910": float(fractional_row(key910) @ displacement),
            }
            record.update({
                "delta": delta,
                "delta_cap": delta_cap,
                "secondary_success": True,
                "minimax_displacement": float(secondary.x[-1]),
                "l2_displacement": float(np.linalg.norm(displacement)),
                "coefficients": displacement.tolist(),
                "fractional_changes": rates,
                "max_guard_worsening": float(np.max(worsening)),
                "top_guard_blockers": [
                    {**guard_info[i], "fractional_worsening": float(worsening[i])}
                    for i in order
                ],
                "active_modes": [
                    {"column": int(i), "coefficient": float(displacement[i]), **mode_meta[i]}
                    for i in np.argsort(np.abs(displacement))[-20:][::-1]
                ],
            })
            if primary.ineqlin.marginals is not None:
                dual = -np.asarray(primary.ineqlin.marginals)
                record["primary_dual_certificate"] = {
                    "objective": float(primary.fun),
                    "guard_dual_l1": float(np.sum(dual[:len(guards)])),
                    "u54_target_dual": float(dual[-2]),
                    "h910_target_dual": float(dual[-1]),
                    "largest_guard_duals": [
                        {**guard_info[i], "dual_weight": float(dual[i])}
                        for i in np.argsort(dual[:len(guards)])[-20:][::-1]
                        if dual[i] > 1e-10
                    ],
                }
            records.append(record)

    successful = [row for row in records if row.get("secondary_success")]
    successful.sort(key=lambda row: (
        row["minimax_displacement"], row["delta"],
        row["h67_component"], row["h910_component"],
    ))
    payload = {
        "version": 1,
        "scope": "epoch-5 direct material U54+H910 target, all component branches",
        "source": args.source,
        "jacobian": args.jacobian,
        "f_vector": [len(result.active), len(result.edges), len(result.faces)],
        "class": [len(result.stable), len(result.unstable), len(result.saddles)],
        "target_ratio_to_original": args.target,
        "current_ratios_to_original": current_ratios,
        "required_fractional_changes": required_fractional,
        "guard_count": len(guards),
        "mode_count": n,
        "bound": args.bound,
        "delta_slack": args.delta_slack,
        "quad_buffer": args.quad_buffer,
        "h67_buffer": args.h67_buffer,
        "fixed_only": args.fixed_only,
        "records": records,
        "ranked_by_minimax_displacement": successful,
    }
    output = HERE / f"{args.prefix}.json"
    output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "target": args.target,
        "current_ratios": current_ratios,
        "required_fractional_changes": required_fractional,
        "branches": len(records),
        "best": [
            {
                "h67": row["h67_component"], "h910": row["h910_component"],
                "delta": row["delta"],
                "max_displacement": row["minimax_displacement"],
                "l2_displacement": row["l2_displacement"],
                "changes": row["fractional_changes"],
            }
            for row in successful[:16]
        ],
    }, indent=2))


if __name__ == "__main__":
    main()
