#!/usr/bin/env python3
"""Hard-minimum SLP inside one actual combinatorial cell."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CIRCUIT = ROOT / "tracks/circuit_atlas"
sys.path[:0] = [str(HERE), str(CIRCUIT)]

from actual_grouped import evaluate, summarize  # noqa: E402
import row54_four_residual_search as core  # noqa: E402
from row54_full_minimax import (  # noqa: E402
    read_points, guards, BASE, SHORT_RAIL, LONG_RAIL,
)
from row54_joint_actual_search import write_csv  # noqa: E402


BOUNDS = np.asarray([(-0.75, 0.75)] * 3 + [(-1.6, 1.6)] * 5)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path,
                    default=HERE / "row54_direct_actual_best.csv")
    ap.add_argument("--iterations", type=int, default=45)
    ap.add_argument("--trust", type=float, default=0.012)
    ap.add_argument("--epsilon", type=float, default=1e-5)
    ap.add_argument("--output", type=Path,
                    default=HERE / "row54_metric_hard_slp.json")
    args = ap.parse_args()

    ids, source = read_points(args.source)
    p0, _ = core.transform(source, np.zeros(8))
    hull, faces, _ = core.group_maximal_faces(ids, p0)
    ef, _ = core.edge_lattice(faces)
    if [len(hull.vertices), len(ef), len(faces)] != [61, 162, 103]:
        raise RuntimeError("unexpected source lattice")

    def values(theta):
        p, den = core.transform(source, theta)
        if p is None or np.min(den) <= 0.08:
            return None
        try:
            m = core.mechanics(ids, p, faces)
        except Exception:
            return None
        return guards(m, faces)[0], p, den

    theta = np.zeros(8)
    base = values(theta)
    g = base[0]
    hard = float(np.min(g))
    best_theta, best_hard = theta.copy(), hard
    trust = args.trust
    history = [{"iteration": -1, "hard": hard, "trust": trust}]
    print("start", hard, flush=True)

    for iteration in range(args.iterations):
        jac = np.zeros((len(g), 8))
        for j in range(8):
            step = np.zeros(8)
            step[j] = args.epsilon
            gp, gm = values(theta + step), values(theta - step)
            if gp is None or gm is None:
                raise RuntimeError(f"finite difference failed at {j}")
            jac[:, j] = (gp[0] - gm[0]) / (2 * args.epsilon)
        c = np.r_[np.zeros(8), -1.0]
        aub = np.c_[-jac, np.ones(len(g))]
        step_bounds = []
        for j in range(8):
            step_bounds.append((
                max(-trust, BOUNDS[j, 0] - theta[j]),
                min(trust, BOUNDS[j, 1] - theta[j]),
            ))
        lp = linprog(c, A_ub=aub, b_ub=g,
                     bounds=step_bounds + [(None, None)], method="highs")
        if not lp.success:
            trust *= 0.5
            history.append({"iteration": iteration, "hard": hard,
                            "trust": trust, "accepted": False,
                            "lp_message": lp.message})
            continue
        direction = lp.x[:-1]
        trials = []
        chosen = None
        for alpha in (1.0, 0.7, 0.5, 0.3, 0.2, 0.1, 0.05,
                      0.02, 0.01, 0.005):
            candidate = theta + alpha * direction
            packet = values(candidate)
            h = float("-inf") if packet is None else float(np.min(packet[0]))
            trials.append({"alpha": alpha, "hard": h})
            if chosen is None or h > chosen[0]:
                chosen = (h, alpha, candidate, packet)
        if chosen[0] <= hard + 1e-11:
            trust *= 0.45
            history.append({"iteration": iteration, "hard": hard,
                            "trust": trust, "predicted": float(lp.x[-1]),
                            "accepted": False, "trials": trials})
            print("reject", iteration, hard, "trust", trust, flush=True)
            if trust < 1e-7:
                break
            continue

        hard, alpha, theta, base = chosen
        g = base[0]
        best_hard, best_theta = hard, theta.copy()
        effective = max(alpha * trust, 1e-7)
        trust = min(0.15, max(trust * 0.7, effective * 1.8))
        history.append({"iteration": iteration, "hard": hard,
                        "trust": trust, "predicted": float(lp.x[-1]),
                        "accepted": True, "alpha": alpha,
                        "trials": trials})
        order = np.argsort(g)[:6]
        print("accept", iteration, hard, "alpha", alpha,
              "trust", trust, "worst", g[order].tolist(), flush=True)
        if hard > 0:
            print("OPEN_TARGET", hard, flush=True)
            break

    final = values(best_theta)
    g, points, den = final
    actual = evaluate({i: points[k] for k, i in enumerate(ids)},
                      coplanar_rel=1e-11)
    actual_faces = {frozenset(f["cycle"]) for f in actual.faces}
    source_faces = {frozenset(c) for c in faces}
    edges = set(actual.edges)
    rail = {
        name: all(tuple(sorted(e)) in edges for e in zip(path, path[1:]))
        for name, path in (("short", SHORT_RAIL), ("long", LONG_RAIL))
    }
    _, labels = guards(core.mechanics(ids, points, faces), faces)
    order = np.argsort(g)
    output = {
        "version": 1,
        "method": "fixed-actual-cell hard-minimum sequential LP",
        "source": str(args.source),
        "theta": best_theta.tolist(),
        "hard_margin": float(np.min(g)),
        "minimum_projective_denominator": float(np.min(den)),
        "worst_guards": [
            {"value": float(g[k]), "feature": labels[k]}
            for k in order[:30]
        ],
        "fresh_actual": summarize(actual),
        "fresh_faces_match_source": actual_faces == source_faces,
        "rail_edges_present": rail,
        "base_face_present": BASE in actual_faces,
        "history": history,
    }
    write_csv(args.output.with_name(args.output.stem + "_best.csv"), ids, points)
    with args.output.with_name(args.output.stem + "_best_faces.json").open("w") as f:
        json.dump([face["cycle"] for face in actual.faces], f, indent=2)
    args.output.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
