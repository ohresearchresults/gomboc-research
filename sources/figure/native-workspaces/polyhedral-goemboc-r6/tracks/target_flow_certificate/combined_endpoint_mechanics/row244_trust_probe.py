#!/usr/bin/env python3
"""Hard max-displacement trust probe for the rank-six row244-z actuator."""
from __future__ import annotations

from pathlib import Path
import ast
import json

import numpy as np
from scipy.optimize import linprog

import combined_four_death_lp as four
import combined_rank6_scan as rank6


HERE = Path(__file__).resolve().parent


def main():
    points = four.load_points()
    base_res, vals = four.primitive_ledger(points)
    modes, meta, _ = four.chart_modes(points)
    data = np.load(HERE / "combined_four_death_jacobian.npz", allow_pickle=True)
    J = data["jacobian"]
    keys = [ast.literal_eval(str(z)) for z in data["primitive_keys"]]
    key_index = {k: i for i, k in enumerate(keys)}
    rank = json.loads((HERE / "combined_rank6_scan.json").read_text())
    local5 = list(map(int, rank["chosen_rank5_columns"]))
    remote = next(i for i, m in enumerate(meta) if m.get("row") == 244 and m.get("axis") == "z")

    fkey = next(k for k in vals if k[0] == "face" and frozenset(k[1]) == four.QUAD and k[2] == (8, 246))
    deaths = [
        fkey,
        ("vertex", 54, 1),
        ("edge", (6, 7), "one_minus_t"),
        ("edge", (9, 10), "t"),
    ]
    R = np.vstack([J[key_index[k]] / vals[k] for k in deaths])
    guards = four.chosen_guards(vals)
    G = np.vstack([
        -sign * J[key_index[k]] / max(abs(vals[k]), 1e-12)
        for k, sign, _ in guards
    ])
    ids = sorted(points)
    base_faces = {frozenset(f["cycle"]) for f in base_res.faces}
    cases = []
    for use_remote in (False, True):
        cols = local5 + ([remote] if use_remote else [])
        # Each column is a complete point-displacement field.
        displacement = np.asarray([
            np.concatenate([modes[col][i] for i in ids]) for col in cols
        ]).T
        for trust in (1e-6, 3e-6, 1e-5, 3e-5, 1e-4, 3e-4, 1e-3):
            for budget in (0.01, 0.05, 0.20):
                k = len(cols)
                # Variables: selected coefficients and common fractional death progress tau.
                A = [np.column_stack((R[:, cols], np.ones(4)))]
                b = [np.zeros(4)]
                A.append(np.column_stack((G[:, cols], np.zeros(len(G)))))
                b.append(np.full(len(G), budget))
                A.append(np.column_stack((displacement, np.zeros(len(displacement)))))
                b.append(np.full(len(displacement), trust))
                A.append(np.column_stack((-displacement, np.zeros(len(displacement)))))
                b.append(np.full(len(displacement), trust))
                lp = linprog(
                    np.r_[np.zeros(k), -1.0],
                    A_ub=np.vstack(A), b_ub=np.concatenate(b),
                    bounds=[(None, None)] * k + [(0.0, 1.0)], method="highs",
                )
                rec = {
                    "use_row244_z": use_remote,
                    "columns": cols,
                    "trust": trust,
                    "guard_budget": budget,
                    "success": bool(lp.success),
                    "message": lp.message,
                }
                if lp.success:
                    coeffs = lp.x[:-1]
                    candidate = rank6.apply_modes(points, [modes[i] for i in cols], coeffs)
                    try:
                        fresh, new_vals = four.primitive_ledger(candidate)
                        faces = {frozenset(f["cycle"]) for f in fresh.faces}
                        ratios = [
                            sign * new_vals[key] / (sign * vals[key])
                            for key, sign, _ in guards
                        ] if faces == base_faces else []
                        audit = {
                            "valid": True,
                            "f_vector": [len(fresh.active), len(fresh.edges), len(fresh.faces)],
                            "faces_match": faces == base_faces,
                            "class": [len(fresh.stable), len(fresh.unstable), len(fresh.saddles)],
                            "topology_margin": fresh.topology_margin,
                            "actual_minimum_guard_ratio": None if not ratios else float(min(ratios)),
                            "actual_death_ratios": {
                                repr(key): float(new_vals[key] / vals[key])
                                for key in deaths if key in new_vals
                            },
                        }
                    except Exception as exc:
                        audit = {"valid": False, "error": repr(exc)}
                    rec.update(
                        predicted_common_progress=float(lp.x[-1]),
                        coefficients=coeffs.tolist(),
                        max_abs_coefficient=float(np.max(np.abs(coeffs))),
                        realized_max_displacement=float(np.max(np.abs(displacement @ coeffs))),
                        fresh_audit=audit,
                    )
                cases.append(rec)
    out = {
        "version": 1,
        "scope": "row244-z hard max-displacement rank-six trust probe",
        "local5_columns": local5,
        "local5_chart": [{"column": i, **meta[i]} for i in local5],
        "remote_column": remote,
        "remote_chart": {"column": remote, **meta[remote]},
        "death_keys": [repr(k) for k in deaths],
        "cases": cases,
    }
    (HERE / "row244_trust_probe.json").write_text(json.dumps(out, indent=2))
    for use in (False, True):
        valid = [
            z for z in cases
            if z["use_row244_z"] == use and z.get("fresh_audit", {}).get("faces_match")
        ]
        best = max(valid, key=lambda z: z["predicted_common_progress"])
        print("remote", use, "best", {
            k: best[k] for k in ("trust", "guard_budget", "predicted_common_progress",
                                 "realized_max_displacement")
        }, "actual", best["fresh_audit"])


if __name__ == "__main__":
    main()
