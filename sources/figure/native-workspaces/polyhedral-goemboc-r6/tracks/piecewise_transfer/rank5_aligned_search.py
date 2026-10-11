#!/usr/bin/env python3
"""Mechanically aligned five-control search on the exact shell cell.

Unlike free Cartesian search, each rational direction addresses one forced
component while preserving the shell support plane when appropriate:

  row228 : q* - q_original       global/base and row228-star actuator
  row232 : ( 15,-69,20)          shell tangent, U231 via edge 231--232
  row254 : (-18,-36,-9)          first side of the row228 star
  row255 : (-18,-36,-9)          second side of the row228 star
  row246 : (-24,132,40)          shell tangent, U246/H(8,246)/second face

Both shell-tangent vectors have exact dot product zero with (100,20,-6).
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution

import rank5_search as core

HERE = Path(__file__).resolve().parent
ROWS = [228, 232, 254, 255, 246]


def directions(seed):
    q228_original = None
    path = core.WORK / "fifth_cell_endpoint" / "input_rows_common_lattice.csv"
    for row in csv.DictReader(path.open()):
        if int(row["source_id"]) == 228:
            den = float(int(row["denominator"]))
            q228_original = np.array(
                [float(int(row[k])) / den for k in ("x_int", "y_int", "z_int")]
            )
            break
    assert q228_original is not None
    out = {
        228: seed[228] - q228_original,
        232: np.array([15.0, -69.0, 20.0]),
        254: np.array([-18.0, -36.0, -9.0]),
        255: np.array([-18.0, -36.0, -9.0]),
        246: np.array([-24.0, 132.0, 40.0]),
    }
    assert abs(float(core.N @ out[232])) < 1e-12
    assert abs(float(core.N @ out[246])) < 1e-12
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=831621)
    ap.add_argument("--generations", type=int, default=150)
    ap.add_argument("--popsize", type=int, default=20)
    ap.add_argument("--bound", type=float, default=1.0)
    ap.add_argument("--output", default="rank5_aligned.json")
    args = ap.parse_args()
    seed = core.shell_seed()
    dirs = directions(seed)
    neval = 0
    best = None

    def build(x):
        rows = {i: p.copy() for i, p in seed.items()}
        for i, t in zip(ROWS, x):
            rows[i] += float(t) * dirs[i]
        return rows

    def objective(x):
        nonlocal neval, best
        neval += 1
        res = core.evaluate(build(x), plane_tol=1e-7, strict_tol=1e-9)
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
            val = -hard + 0.08 * float(np.linalg.norm(bad))
        else:
            val = 1e5
        if best is None or hard > best[0]:
            best = (hard, d, np.array(x, float))
            print(
                json.dumps(
                    {
                        "eval": neval,
                        "x": list(map(float, x)),
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

    popn = max(5, args.popsize * len(ROWS))
    init = np.random.default_rng(args.seed).uniform(
        -args.bound, args.bound, size=(popn, len(ROWS))
    )
    init[0] = 0
    result = differential_evolution(
        objective,
        [(-args.bound, args.bound)] * len(ROWS),
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
    hard, diag, bx = best
    br = build(bx)
    out = {
        "version": 1,
        "type": "mechanically aligned rational five-control actual-hull search",
        "shell_plane": {"normal": [100, 20, -6], "height": 3700},
        "shell_rows": list(range(231, 247)),
        "control_rows": ROWS,
        "directions": {str(i): dirs[i].tolist() for i in ROWS},
        "seed": args.seed,
        "evaluations": neval,
        "best_parameters": bx.tolist(),
        "best_hard": hard,
        "best_diagnostics": diag,
        "best_coordinates": {str(i): br[i].tolist() for i in ROWS},
        "optimizer": {"fun": float(result.fun), "message": str(result.message)},
    }
    (HERE / args.output).write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({"output": args.output, "best_hard": hard, "class": diag.get("class")}))


if __name__ == "__main__":
    main()
