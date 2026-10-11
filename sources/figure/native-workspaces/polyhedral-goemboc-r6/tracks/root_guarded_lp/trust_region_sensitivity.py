#!/usr/bin/env python3
"""Physical-displacement trust-region sensitivity for baseline_guarded_lp.py."""

from __future__ import annotations

import ast
import importlib.util
import json
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("guarded", HERE / "baseline_guarded_lp.py")
guarded = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(guarded)


def main():
    base = guarded.load_points()
    res, vals = guarded.primitive_ledger(base)
    modes, meta = guarded.build_modes(base, res)
    cache = np.load(HERE / "baseline_guarded_jacobian.npz", allow_pickle=True)
    J = np.asarray(cache["jacobian"])
    keys = [ast.literal_eval(str(z)) for z in cache["primitive_keys"]]
    key_index = {k: i for i, k in enumerate(keys)}
    assert all(abs(float(cache["primitive_values"][i]) - vals[k]) < 1e-10 for i, k in enumerate(keys))

    guards = guarded.chosen_guards(res, vals)
    G = []
    guard_info = []
    for key, sign, kind in guards:
        G.append(-sign * J[key_index[key]] / max(abs(vals[key]), 1e-12))
        guard_info.append((key, kind))
    G = np.asarray(G)

    ids = sorted(base)
    displacement = np.zeros((3 * len(ids), len(modes)))
    for col, mode in enumerate(modes):
        for ii, vertex in enumerate(ids):
            displacement[3 * ii : 3 * ii + 3, col] = mode[vertex]

    extra_face_keys = [k for k in vals if k[0] == "face" and frozenset(k[1]) == guarded.EXTRA_FACE]
    saddle_keys = [k for k in vals if k[0] == "edge" and k[1] == guarded.SADDLE_EDGE]
    n = len(modes)
    bounds = [(-1000.0, 1000.0)] * n + [(-1000.0, 1000.0)]
    objective = np.r_[np.zeros(n), 1.0]
    unrestricted = json.loads((HERE / "baseline_guarded_lp.json").read_text())["atlas"][:3]
    candidate_pairs = {(r["face_death"], r["saddle_death"]) for r in unrestricted}
    records = []
    for radius in [0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0]:
        best = None
        for fk in extra_face_keys:
            for ek in saddle_keys:
                if (repr(fk), repr(ek)) not in candidate_pairs:
                    continue
                d1 = J[key_index[fk]] / vals[fk]
                d2 = J[key_index[ek]] / vals[ek]
                A = np.vstack(
                    (
                        np.hstack((G, -np.ones((len(G), 1)))),
                        np.hstack((displacement, np.zeros((len(displacement), 1)))),
                        np.hstack((-displacement, np.zeros((len(displacement), 1)))),
                        np.r_[d1, 0.0],
                        np.r_[d2, 0.0],
                    )
                )
                b = np.r_[
                    np.zeros(len(G)),
                    np.full(len(displacement), radius),
                    np.full(len(displacement), radius),
                    -1.0,
                    -1.0,
                ]
                lp = linprog(objective, A_ub=A, b_ub=b, bounds=bounds, method="highs")
                if not lp.success:
                    continue
                c = lp.x[:n]
                rec = {
                    "radius_linf_coordinate": radius,
                    "delta": float(lp.x[-1]),
                    "face_death": repr(fk),
                    "saddle_death": repr(ek),
                    "max_coordinate_displacement": float(np.max(np.abs(displacement @ c))),
                    "rms_vertex_displacement": float(np.sqrt(np.mean((displacement @ c) ** 2) * 3.0)),
                    "coefficients": [float(z) for z in c],
                }
                worsening = G @ c
                order = np.argsort(worsening)[-12:][::-1]
                rec["top_blockers"] = [
                    {"key": repr(guard_info[i][0]), "kind": guard_info[i][1], "fractional_worsening": float(worsening[i])}
                    for i in order
                ]
                if best is None or rec["delta"] < best["delta"]:
                    best = rec
        records.append(best or {"radius_linf_coordinate": radius, "infeasible": True})
        print(radius, "infeasible" if best is None else (best["delta"], best["face_death"], best["saddle_death"]))
    (HERE / "trust_region_sensitivity.json").write_text(json.dumps({"version": 1, "records": records}, indent=2))


if __name__ == "__main__":
    main()
