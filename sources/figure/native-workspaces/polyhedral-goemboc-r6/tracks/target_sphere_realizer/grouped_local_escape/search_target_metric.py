#!/usr/bin/env python3
"""Recover the robust (2,2,2) metric chamber on the exact target sphere."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution, linprog, minimize

from build_target_tutte import BASE, barycentric_2d, graph, target_faces, tutte
from search_recover_far_side import FixedSphere

HERE = Path(__file__).resolve().parent


def targeted_cap() -> tuple[dict[int, np.ndarray], list[list[int]], dict]:
    faces, old, new = target_faces()
    ids, nb, ef = graph(faces)
    xy = tutte(ids, nb)
    interior = [i for i in ids if i not in set(BASE)]
    loc = {i: k for k, i in enumerate(interior)}
    rows = []
    for c in [c for c in faces if set(c) != set(BASE)]:
        tri = np.stack([xy[i] for i in c])
        for j in ids:
            if j in c:
                continue
            lam = barycentric_2d(xy[j], tri)
            row = np.zeros(len(interior))
            if j in loc:
                row[loc[j]] += 1.0
            for v, z in zip(c, lam):
                if v in loc:
                    row[loc[v]] -= z
            rows.append(row)
    A = np.asarray(rows)
    # Historical optimum is about 4.35644e-7.  A smaller fixed strict gap
    # leaves a broad cap realization cell for the directional objective.
    gamma = 2.0e-8
    b = np.full(len(A), -gamma)
    objective = np.ones(len(interior))
    objective[[loc[245], loc[246]]] = -10.0
    res = linprog(
        objective,
        A_ub=A,
        b_ub=b,
        bounds=[(0.0, 1.0)] * len(interior),
        method="highs",
        options={"primal_feasibility_tolerance": 1e-10, "dual_feasibility_tolerance": 1e-10},
    )
    assert res.success, res.message
    P = {i: np.array([xy[i][0], xy[i][1], 0.0]) for i in ids}
    for i, z in zip(interior, res.x):
        P[i][2] = z
    return P, faces, {"gamma": gamma, "max_constraint_residual": float(np.max(A @ res.x - b))}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=831701)
    ap.add_argument("--maxiter", type=int, default=700)
    ap.add_argument("--popsize", type=int, default=20)
    ap.add_argument("--out", default="target_metric.json")
    args = ap.parse_args()

    P, faces, cap_audit = targeted_cap()
    sphere = FixedSphere(raw_points=P, faces_ids=faces, extra_face=(8, 245, 246))
    start = sphere.evaluate(np.zeros(8), details=True)
    print("START", start["class"], start["hard"], start["stable"], flush=True)

    def fun(x):
        return -sphere.evaluate(np.asarray(x))["score"]

    best_x = np.zeros(8)
    best = sphere.evaluate(best_x)

    def callback(xk, convergence=0.0):
        nonlocal best_x, best
        z = sphere.evaluate(np.asarray(xk))
        if z.get("valid") and z.get("hard", -1e99) > best.get("hard", -1e99):
            best_x, best = np.asarray(xk).copy(), z
            print("BEST", best["hard"], best["score"], convergence, best_x.tolist(), flush=True)
        return z.get("hard", -1) > 5e-5

    res = differential_evolution(
        fun,
        [(-5.5, 5.5)] * 5 + [(-1.7, 1.7)] * 3,
        seed=args.seed,
        maxiter=args.maxiter,
        popsize=args.popsize,
        mutation=(0.35, 1.4),
        recombination=0.86,
        tol=1e-8,
        polish=False,
        callback=callback,
    )
    candidates = [best_x, np.asarray(res.x)]
    for x0 in candidates[:]:
        rr = minimize(fun, x0, method="Nelder-Mead", options={"maxiter": 3500, "xatol": 1e-9, "fatol": 1e-10})
        candidates.append(np.asarray(rr.x))
    best_x = max(candidates, key=lambda x: sphere.evaluate(x).get("hard", -1e99))
    detail = sphere.evaluate(best_x, details=True)
    detail.update({"theta": best_x.tolist(), "cap_audit": cap_audit})
    json.dump(detail, open(HERE / args.out, "w"), indent=2)
    with open(HERE / (Path(args.out).stem + "_points.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source_id", "x", "y", "z"])
        for i in sphere.ids:
            w.writerow([i, *detail["points"][str(i)]])
    print("FINAL", detail["class"], detail["hard"], detail["stable"], detail["unstable"], detail["saddles"], flush=True)


if __name__ == "__main__":
    main()
