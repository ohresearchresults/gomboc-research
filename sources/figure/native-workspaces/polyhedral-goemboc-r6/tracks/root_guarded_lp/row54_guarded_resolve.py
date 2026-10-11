#!/usr/bin/env python3
"""Re-solve the cached row54 guarded atlas under a physical trust box."""

from __future__ import annotations

import argparse
import ast
import importlib.util
import json
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("row54_lp", HERE / "row54_guarded_lp.py")
lpmod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(lpmod)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--trust", type=float, required=True)
    ap.add_argument("--bound", type=float, default=20.0)
    args = ap.parse_args()
    data = np.load(HERE / "row54_guarded_jacobian.npz", allow_pickle=True)
    jac = np.asarray(data["jacobian"], dtype=float)
    keys = [ast.literal_eval(str(item)) for item in data["primitive_keys"]]
    values = np.asarray(data["primitive_values"], dtype=float)
    vals = dict(zip(keys, values))
    meta = [json.loads(str(item)) for item in data["mode_meta"]]
    displacement = np.asarray(data["displacement"], dtype=float)
    key_index = {key: i for i, key in enumerate(keys)}
    guards = lpmod.chosen_guards(vals)
    guard_rows, guard_info = [], []
    for key, sign, kind in guards:
        guard_rows.append(-sign * jac[key_index[key]] / max(abs(vals[key]), 1e-12))
        guard_info.append({"key": repr(key), "kind": kind, "value": vals[key], "sign": sign})
    guard_rows = np.asarray(guard_rows)
    n = jac.shape[1]
    common_a = np.vstack((
        np.hstack((guard_rows, -np.ones((len(guard_rows), 1)))),
        np.hstack((displacement, np.zeros((len(displacement), 1)))),
        np.hstack((-displacement, np.zeros((len(displacement), 1)))),
    ))
    common_b = np.r_[
        np.zeros(len(guard_rows)),
        np.full(len(displacement), args.trust),
        np.full(len(displacement), args.trust),
    ]
    packets = [
        [key for key in vals if key[0] == "face" and frozenset(key[1]) == lpmod.EXTRA_FACE],
        [key for key in vals if key[0] == "vertex" and key[1] == lpmod.EXTRA_U],
        [key for key in vals if key[0] == "edge" and key[1] == (6, 7)],
        [key for key in vals if key[0] == "edge" and key[1] == (9, 10)],
    ]
    objective = np.r_[np.zeros(n), 1.0]
    bounds = [(-args.bound, args.bound)] * n + [(-1000.0, 1000.0)]
    results = []
    for fkey in packets[0]:
        for ukey in packets[1]:
            for h67 in packets[2]:
                for h910 in packets[3]:
                    deaths = [fkey, ukey, h67, h910]
                    rows = [jac[key_index[key]] / vals[key] for key in deaths]
                    a = np.vstack((common_a, *[np.r_[row, 0.0] for row in rows]))
                    b = np.r_[common_b, np.full(4, -1.0)]
                    solve = linprog(objective, A_ub=a, b_ub=b, bounds=bounds, method="highs")
                    record = {"deaths": [repr(key) for key in deaths], "success": bool(solve.success),
                              "message": solve.message}
                    if solve.success:
                        coefficient = solve.x[:n]
                        worsening = guard_rows @ coefficient
                        order = np.argsort(worsening)[-16:][::-1]
                        active = np.argsort(np.abs(coefficient))[-20:][::-1]
                        record.update(
                            delta=float(solve.x[-1]),
                            coefficients=[float(z) for z in coefficient],
                            max_coordinate_displacement=float(np.max(np.abs(displacement @ coefficient))),
                            fractional_death_derivatives=[float(row @ coefficient) for row in rows],
                            top_guard_blockers=[{**guard_info[i], "fractional_worsening": float(worsening[i])}
                                                for i in order],
                            active_modes=[{"column": int(i), "coefficient": float(coefficient[i]), **meta[i]}
                                          for i in active],
                        )
                    results.append(record)
    results.sort(key=lambda item: item.get("delta", 1e100))
    output = {
        "version": 1,
        "trust": args.trust,
        "bound": args.bound,
        "atlas": results,
    }
    path = HERE / f"row54_guarded_sensitivity_trust{args.trust:g}.json"
    path.write_text(json.dumps(output, indent=2))
    feasible = [item for item in results if item["success"]]
    print("trust", args.trust, "feasible", len(feasible), "best", None if not feasible else feasible[0]["delta"],
          "maxdisp", None if not feasible else feasible[0]["max_coordinate_displacement"], flush=True)
    if feasible:
        print("deaths", feasible[0]["deaths"], flush=True)


if __name__ == "__main__":
    main()
