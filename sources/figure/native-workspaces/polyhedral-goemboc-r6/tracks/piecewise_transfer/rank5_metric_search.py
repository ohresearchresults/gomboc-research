#!/usr/bin/env python3
"""Global SPD/linear metric search over a rank-five shell candidate.

An invertible linear map preserves the complete actual hull lattice and sends
the ordinary-volume centroid covariantly.  It is therefore a clean independent
mechanical control layer over the locally preconditioned shell candidates.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution

import rank5_search as core

HERE = Path(__file__).resolve().parent


def matrix(x):
    return np.array(
        [
            [np.exp(x[0]), 0.0, 0.0],
            [x[3], np.exp(x[1]), 0.0],
            [x[4], x[5], np.exp(x[2])],
        ]
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidate", required=True)
    ap.add_argument("--seed", type=int, default=831631)
    ap.add_argument("--bound", type=float, default=1.25)
    ap.add_argument("--popsize", type=int, default=16)
    ap.add_argument("--generations", type=int, default=120)
    ap.add_argument("--output", default="rank5_metric.json")
    args = ap.parse_args()
    source = json.loads((HERE / args.candidate).read_text())
    rows0 = core.shell_seed()
    for key, p in source["best_coordinates"].items():
        rows0[int(key)] = np.array(p, float)
    seed_eval = core.evaluate(rows0, plane_tol=1e-7, strict_tol=1e-9)
    seed_diag = core.diagnostics(seed_eval)
    neval = 0
    best = None

    def build(x):
        a = matrix(x)
        return {i: a @ p for i, p in rows0.items()}, a

    def objective(x):
        nonlocal neval, best
        neval += 1
        rows, a = build(x)
        res = core.evaluate(rows, plane_tol=2e-7, strict_tol=1e-9)
        d = core.diagnostics(res)
        hard = float(d["hard"])
        if d.get("valid"):
            bad = np.array(
                [
                    max(0.0, -d["base"]),
                    max(0.0, -d["u8"]),
                    max(0.0, d["face_bad"]),
                    max(0.0, d["vertex_bad"]),
                    max(0.0, d["edge_bad"]),
                ]
            )
            val = -hard + 0.06 * float(np.linalg.norm(bad))
        else:
            val = 1e5
        if best is None or hard > best[0]:
            best = (hard, d, np.array(x, float), a.copy())
            print(
                json.dumps(
                    {
                        "eval": neval,
                        "hard": hard,
                        "class": d.get("class"),
                        "f_vector": d.get("f_vector"),
                        "base": d.get("base"),
                        "u8": d.get("u8"),
                        "face_bad": d.get("face_bad"),
                        "vertex_bad": d.get("vertex_bad"),
                        "edge_bad": d.get("edge_bad"),
                    },
                    separators=(",", ":"),
                ),
                flush=True,
            )
        return val

    popn = max(5, args.popsize * 6)
    init = np.random.default_rng(args.seed).uniform(
        -args.bound, args.bound, size=(popn, 6)
    )
    init[0] = 0
    result = differential_evolution(
        objective,
        [(-args.bound, args.bound)] * 6,
        seed=args.seed,
        popsize=args.popsize,
        maxiter=args.generations,
        init=init,
        polish=False,
        updating="immediate",
        tol=1e-10,
        disp=True,
    )
    assert best is not None
    hard, diag, bx, ba = best
    out = {
        "version": 1,
        "type": "global invertible lower-triangular metric search over rank-five shell candidate",
        "source_candidate": args.candidate,
        "source_diagnostics": seed_diag,
        "seed": args.seed,
        "evaluations": neval,
        "best_hard": hard,
        "best_parameters": bx.tolist(),
        "best_linear_map": ba.tolist(),
        "best_metric": (ba.T @ ba).tolist(),
        "determinant": float(np.linalg.det(ba)),
        "best_diagnostics": diag,
        "optimizer": {"fun": float(result.fun), "message": str(result.message)},
    }
    (HERE / args.output).write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({"output": args.output, "best_hard": hard, "class": diag.get("class")}))


if __name__ == "__main__":
    main()
