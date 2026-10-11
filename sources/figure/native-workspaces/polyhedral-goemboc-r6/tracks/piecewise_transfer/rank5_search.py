#!/usr/bin/env python3
"""Search the reconstructed rank-five supporting-shell family.

The exact shell wall is the orthogonal projection of source rows 231..246
onto 100*x + 20*y - 6*z = 3700.  Row 228 is initialized at the rational
actuator endpoint (-19,-35,-12).  Every evaluation rebuilds the actual hull,
ordinary-volume centroid and complete S/U/H mechanics.

This is a numerical proposer.  A winner must subsequently be rationalized and
verified by rank5_exact_certificate.py.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
WORK = ROOT / "M42_acute_bridge_fifth_cell_work"
sys.path.insert(0, str(WORK / "fourth_cell_endpoint"))
from numeric_hull_proposer import evaluate  # type: ignore

N = np.array([100.0, 20.0, -6.0])
H = 3700.0
N2 = float(N @ N)
BASE = set(range(17))
TARGET_VERTEX = 8


def read_rows() -> dict[int, np.ndarray]:
    path = WORK / "fifth_cell_endpoint" / "input_rows_common_lattice.csv"
    out: dict[int, np.ndarray] = {}
    for row in csv.DictReader(path.open()):
        den = float(int(row["denominator"]))
        out[int(row["source_id"])] = np.array(
            [float(int(row[k])) / den for k in ("x_int", "y_int", "z_int")]
        )
    return out


ORIGINAL = read_rows()


def shell_seed() -> dict[int, np.ndarray]:
    rows = {i: p.copy() for i, p in ORIGINAL.items()}
    for i in range(231, 247):
        p = rows[i]
        rows[i] = p + (H - float(N @ p)) / N2 * N
    rows[228] = np.array([-19.0, -35.0, -12.0])
    return rows


def frame_for(i: int, seed: dict[int, np.ndarray]) -> np.ndarray:
    """A well-scaled orthonormal local frame; first axis is radial."""
    p = seed[i]
    e0 = p / np.linalg.norm(p)
    trial = N / np.linalg.norm(N)
    e1 = trial - float(trial @ e0) * e0
    if np.linalg.norm(e1) < 1e-8:
        trial = np.array([0.0, 0.0, 1.0])
        e1 = trial - float(trial @ e0) * e0
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(e0, e1)
    e2 /= np.linalg.norm(e2)
    return np.column_stack([e0, e1, e2])


def diagnostics(res) -> dict:
    if not res.valid:
        return {"valid": False, "error": res.error, "hard": -1.0e6}
    target_face_idx = next(
        (fi for fi, face in enumerate(res.faces) if set(face["cycle"]) == BASE), None
    )
    base_dec = (
        float(res.face_decisions[target_face_idx])
        if target_face_idx is not None
        else -10.0
    )
    u8_dec = float(res.vertex_decisions.get(TARGET_VERTEX, -10.0))
    face_bad = max(
        (float(d) for fi, d in enumerate(res.face_decisions) if fi != target_face_idx),
        default=-10.0,
    )
    vertex_bad = max(
        (float(d) for i, d in res.vertex_decisions.items() if i != TARGET_VERTEX),
        default=-10.0,
    )
    edge_bad = max((float(d) for d in res.edge_decisions.values()), default=-10.0)
    # Intentional shell coplanarity is represented by one maximal face and is
    # already excluded from topology_margin by evaluate().
    hard = min(
        base_dec,
        u8_dec,
        -face_bad,
        -vertex_bad,
        -edge_bad,
        float(res.topology_margin),
        float(res.inactive_margin),
    )
    return {
        "valid": True,
        "hard": float(hard),
        "class": [len(res.stable), len(res.unstable), len(res.saddles)],
        "f_vector": [len(res.active), len(res.edges), len(res.faces)],
        "centroid": [float(z) for z in res.centroid],
        "volume": float(res.volume),
        "base": base_dec,
        "u8": u8_dec,
        "face_bad": face_bad,
        "vertex_bad": vertex_bad,
        "edge_bad": edge_bad,
        "topology": float(res.topology_margin),
        "inactive": float(res.inactive_margin),
        "stable": [
            {"cycle": res.faces[fi]["cycle"], "decision": float(d)}
            for fi, d in res.stable
        ],
        "unstable": [{"vertex": int(i), "decision": float(d)} for i, d in res.unstable],
        "saddles": [{"edge": list(e), "decision": float(d)} for e, d in res.saddles],
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rows", default="228,229,254,255")
    ap.add_argument("--scale", type=float, default=8.0)
    ap.add_argument("--seed", type=int, default=831601)
    ap.add_argument("--popsize", type=int, default=12)
    ap.add_argument("--generations", type=int, default=120)
    ap.add_argument("--output", default="rank5_search.json")
    args = ap.parse_args()

    moved = [int(x) for x in args.rows.split(",") if x]
    seed = shell_seed()
    frames = {i: frame_for(i, seed) for i in moved}
    eval_count = 0
    best: tuple[float, dict, np.ndarray] | None = None

    # Per-coordinate local-frame scales.  Row 228 starts at the large rational
    # actuator endpoint, so keep it tighter; star neighbours are allowed to
    # rebuild the local supporting fan macroscopically.
    local_scales = []
    for i in moved:
        s = args.scale * (0.55 if i == 228 else 1.0)
        local_scales.extend([s, s, s])
    local_scales = np.asarray(local_scales)

    def build(x: np.ndarray) -> dict[int, np.ndarray]:
        rows = {i: p.copy() for i, p in seed.items()}
        for k, i in enumerate(moved):
            rows[i] = rows[i] + frames[i] @ x[3 * k : 3 * k + 3]
        return rows

    def objective(x: np.ndarray) -> float:
        nonlocal eval_count, best
        eval_count += 1
        rows = build(x)
        res = evaluate(rows, plane_tol=1e-7, strict_tol=1e-9)
        d = diagnostics(res)
        hard = float(d["hard"])
        # The primary objective is the strict common margin.  A smooth
        # secondary minimax term guides the search before every sign is right.
        if d.get("valid"):
            violations = np.array(
                [
                    max(0.0, -d["base"]),
                    max(0.0, -d["u8"]),
                    max(0.0, d["face_bad"]),
                    max(0.0, d["vertex_bad"]),
                    max(0.0, d["edge_bad"]),
                ]
            )
            obj = -hard + 0.05 * float(np.linalg.norm(violations))
        else:
            obj = 1.0e5
        if best is None or hard > best[0]:
            best = (hard, d, x.copy())
            print(
                json.dumps(
                    {
                        "eval": eval_count,
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
        return obj

    x0 = np.zeros(3 * len(moved))
    initial = np.random.default_rng(args.seed).uniform(
        -local_scales, local_scales, size=(max(args.popsize * len(x0), 5), len(x0))
    )
    initial[0] = x0
    result = differential_evolution(
        objective,
        bounds=list(zip(-local_scales, local_scales)),
        seed=args.seed,
        popsize=args.popsize,
        maxiter=args.generations,
        tol=1e-9,
        polish=False,
        workers=1,
        updating="immediate",
        init=initial,
        disp=True,
    )
    assert best is not None
    hard, diag, bx = best
    brow = build(bx)
    payload = {
        "version": 1,
        "type": "numerical proposer for reconstructed rank-five supporting shell",
        "shell_plane": {"normal": [100, 20, -6], "height": 3700},
        "shell_rows": list(range(231, 247)),
        "moved_rows": moved,
        "seed": args.seed,
        "bounds_scale": args.scale,
        "evaluations": eval_count,
        "best_hard": hard,
        "best_diagnostics": diag,
        "best_local_parameters": bx.tolist(),
        "best_coordinates": {str(i): brow[i].tolist() for i in moved},
        "optimizer": {
            "fun": float(result.fun),
            "success": bool(result.success),
            "message": str(result.message),
        },
    }
    (HERE / args.output).write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({"output": args.output, "best_hard": hard, "class": diag.get("class")}))


if __name__ == "__main__":
    main()
