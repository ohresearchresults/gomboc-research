#!/usr/bin/env python3
"""Four independent rational star actuators on the supporting-shell wall.

The controls are deliberately integral so that any numerical chamber found by
this proposer can be exactified without changing the family:

  t229 * ( 41,-16, 2)   kills/bends the U231 witness through edge 229--231;
  t254 * (-18,-36,-9)   opens the first row-228 face/edge star;
  t255 * (-18,-36,-9)   independently opens its other side;
  t264 * ( 28, 51, 2)   bends the U246 / face(228,264,246) star.

Together with the row-228 actuator this is the reconstructed rank-five shell
template.  Every call rebuilds the actual hull and ordinary-volume centroid.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution

import rank5_search as core

HERE = Path(__file__).resolve().parent
ROWS = [229, 254, 255, 264]
DIRS = {
    229: np.array([41.0, -16.0, 2.0]),
    254: np.array([-18.0, -36.0, -9.0]),
    255: np.array([-18.0, -36.0, -9.0]),
    264: np.array([28.0, 51.0, 2.0]),
}


def build(x: np.ndarray) -> dict[int, np.ndarray]:
    rows = core.shell_seed()
    for i, t in zip(ROWS, x):
        rows[i] = rows[i] + float(t) * DIRS[i]
    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=831611)
    ap.add_argument("--generations", type=int, default=100)
    ap.add_argument("--popsize", type=int, default=18)
    ap.add_argument("--bound", type=float, default=2.0)
    ap.add_argument("--output", default="rank5_star.json")
    args = ap.parse_args()
    neval = 0
    best = None

    def objective(x):
        nonlocal neval, best
        neval += 1
        res = core.evaluate(build(x), plane_tol=1e-7, strict_tol=1e-9)
        d = core.diagnostics(res)
        hard = float(d["hard"])
        if d.get("valid"):
            vv = np.array(
                [
                    max(0.0, -d["base"]),
                    max(0.0, -d["u8"]),
                    max(0.0, d["face_bad"]),
                    max(0.0, d["vertex_bad"]),
                    max(0.0, d["edge_bad"]),
                ]
            )
            val = -hard + 0.12 * float(np.linalg.norm(vv))
        else:
            val = 1e4
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
        "type": "rank-five rational integral star-control proposer",
        "shell_plane": {"normal": [100, 20, -6], "height": 3700},
        "shell_rows": list(range(231, 247)),
        "fixed_row228": [-19, -35, -12],
        "control_rows": ROWS,
        "directions": {str(i): DIRS[i].astype(int).tolist() for i in ROWS},
        "seed": args.seed,
        "evaluations": neval,
        "best_parameters": bx.tolist(),
        "best_hard": hard,
        "best_diagnostics": diag,
        "best_coordinates": {str(i): br[i].tolist() for i in [228] + ROWS},
        "optimizer": {"fun": float(result.fun), "message": str(result.message)},
    }
    (HERE / args.output).write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({"output": args.output, "best_hard": hard, "class": diag.get("class")}))


if __name__ == "__main__":
    main()
