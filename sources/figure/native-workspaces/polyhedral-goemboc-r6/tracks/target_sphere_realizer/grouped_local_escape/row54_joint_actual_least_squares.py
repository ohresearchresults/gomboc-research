#!/usr/bin/env python3
"""Nonlinear least-squares escape over all fresh actual feature guards."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from row54_joint_actual_search import JointActual, write_csv  # noqa: E402
from row54_joint_actual_slp import (  # noqa: E402
    packet, encode, GLOBAL_BOUNDS, SCALES, CIRCUIT, mat,
)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path,
                    default=HERE / "row54_joint_actual.json")
    ap.add_argument("--max-evals", type=int, default=900)
    ap.add_argument("--target-margin", type=float, default=2e-6)
    ap.add_argument("--radius", type=float, default=1.25)
    ap.add_argument("--output", type=Path,
                    default=HERE / "row54_joint_actual_least_squares.json")
    args = ap.parse_args()

    source = json.load(args.source.open())
    if "audited_candidates" in source:
        starts = {r["name"]: r for r in source["audited_candidates"]}
        x0 = np.asarray(starts["best_hard"]["parameters"], dtype=float)
    else:
        x0 = np.asarray(source["parameters"], dtype=float)

    ids, raw = mat.load_csv(CIRCUIT / "target_sphere_rebuilt.csv")
    robust_theta = np.asarray(
        json.load((CIRCUIT / "robust_rebuilt_fast.json").open())["theta"]
    )
    search = JointActual(ids, raw, robust_theta)
    p0 = packet(search, x0)
    if p0 is None:
        raise RuntimeError("invalid start")
    keys = p0[1]
    n_guards = len(keys)
    best = [float(np.min(p0[0])), x0.copy(), p0]
    calls = 0

    lower = np.maximum((GLOBAL_BOUNDS[:, 0] - x0) / SCALES, -args.radius)
    upper = np.minimum((GLOBAL_BOUNDS[:, 1] - x0) / SCALES, args.radius)

    def residual(y):
        nonlocal calls
        calls += 1
        x = x0 + SCALES * np.asarray(y)
        p = packet(search, x, keys)
        if p is None:
            return np.full(n_guards, 100.0)
        guards = p[0]
        hard = float(np.min(guards))
        if hard > best[0]:
            best[:] = [hard, x.copy(), p]
            ii = np.argsort(guards)[:6]
            print("best", calls, hard,
                  [(float(guards[i]), keys[i]) for i in ii], flush=True)
        # One-sided nonlinear feasibility residual.  Scaling is constant and
        # therefore does not alter the zero set; it only helps finite-difference
        # tolerances at the 1e-6--1e-4 margins of interest.
        return np.minimum(guards - args.target_margin, 0.0) / 1e-3

    result = least_squares(
        residual, np.zeros(len(x0)), bounds=(lower, upper),
        jac="2-point", diff_step=2e-4, x_scale="jac",
        max_nfev=args.max_evals, ftol=1e-13, xtol=1e-13, gtol=1e-13,
        verbose=1,
    )
    points, output = encode(search, best[1], history=[])
    output.update({
        "version": 1,
        "method": "fresh-actual one-sided nonlinear least squares",
        "target_margin": args.target_margin,
        "calls": calls,
        "optimizer_status": int(result.status),
        "optimizer_message": str(result.message),
        "optimizer_cost": float(result.cost),
        "optimizer_optimality": float(result.optimality),
        "start_parameters": x0.tolist(),
    })
    write_csv(args.output.with_name(args.output.stem + "_best.csv"), ids, points)
    final = packet(search, best[1])
    with args.output.with_name(args.output.stem + "_best_faces.json").open("w") as f:
        json.dump([face["cycle"] for face in final[3].faces], f, indent=2)
    args.output.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
