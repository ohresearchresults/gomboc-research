#!/usr/bin/env python3
"""Hard-minimum SLP in the topology-exact eight-dimensional projective family."""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
GROUPED = ROOT / "tracks/target_sphere_realizer/grouped_local_escape"
CIRCUIT = ROOT / "tracks/circuit_atlas"
sys.path[:0] = [str(GROUPED), str(CIRCUIT)]

from actual_grouped import evaluate, summarize  # noqa: E402
from row54_full_minimax import BASE, LONG_RAIL, SHORT_RAIL, guards  # noqa: E402
import row54_four_residual_search as core  # noqa: E402


def read_points(path):
    rows = {}
    with path.open() as stream:
        for row in csv.DictReader(stream):
            rows[int(row["source_id"])] = np.asarray(
                [float(row[k]) for k in ("x", "y", "z")]
            )
    ids = sorted(rows)
    return ids, np.asarray([rows[i] for i in ids])


def write_csv(path, ids, points):
    with path.open("w", newline="") as stream:
        out = csv.writer(stream)
        out.writerow(("source_id", "x", "y", "z"))
        for i, point in zip(ids, points):
            out.writerow((i, *(format(float(x), ".17g") for x in point)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, default=HERE / "far.csv")
    ap.add_argument("--start", type=Path)
    ap.add_argument("--iterations", type=int, default=80)
    ap.add_argument("--trust", type=float, default=0.08)
    ap.add_argument("--epsilon", type=float, default=2e-6)
    ap.add_argument("--output", type=Path, default=HERE / "projective_hard_slp.json")
    args = ap.parse_args()

    ids, source = read_points(args.source)
    _, faces, _ = core.group_maximal_faces(ids, source)
    face_keys = {frozenset(face) for face in faces}
    rails = {
        tuple(sorted(edge))
        for path in (SHORT_RAIL, LONG_RAIL)
        for edge in zip(path, path[1:])
    }

    def values(theta):
        points, denominator = core.transform(source, theta)
        if points is None or float(np.min(denominator)) <= 0.04:
            return None
        try:
            g, labels = guards(core.mechanics(ids, points, faces), faces)
        except Exception:
            return None
        return g, labels, points, denominator

    def audit(theta):
        packet = values(theta)
        if packet is None:
            return None
        g, labels, points, denominator = packet
        fresh = evaluate({i: points[k] for k, i in enumerate(ids)}, coplanar_rel=2e-12)
        if not fresh.valid:
            return None
        keys = {frozenset(face["cycle"]) for face in fresh.faces}
        if (
            set(fresh.active) != set(ids)
            or keys != face_keys
            or BASE not in keys
            or not rails <= set(fresh.edges)
        ):
            return None
        return g, labels, points, denominator, fresh

    theta = np.zeros(8)
    if args.start:
        theta = np.asarray(json.loads(args.start.read_text())["theta"], float)
    current = audit(theta)
    if current is None:
        raise RuntimeError("invalid projective start")
    hard = float(np.min(current[0]))
    trust = args.trust
    history = []
    print("start", hard, flush=True)

    for iteration in range(args.iterations):
        g = current[0]
        jac = np.zeros((len(g), 8))
        for j in range(8):
            step = np.zeros(8)
            step[j] = args.epsilon
            plus, minus = values(theta + step), values(theta - step)
            if plus is None or minus is None:
                raise RuntimeError(("finite difference failed", j))
            jac[:, j] = (plus[0] - minus[0]) / (2 * args.epsilon)
        bounds = [
            (max(-trust, -3.0 - theta[j]), min(trust, 3.0 - theta[j]))
            for j in range(8)
        ]
        lp = linprog(
            np.r_[np.zeros(8), -1.0],
            A_ub=np.c_[-jac, np.ones(len(g))],
            b_ub=g,
            bounds=bounds + [(None, None)],
            method="highs",
        )
        if not lp.success:
            trust *= 0.5
            history.append({"iteration": iteration, "accepted": False, "reason": lp.message})
            continue
        direction = lp.x[:-1]
        chosen = None
        trials = []
        for alpha in (1.0, 0.7, 0.5, 0.3, 0.2, 0.1, 0.05, 0.02, 0.01):
            candidate_theta = theta + alpha * direction
            candidate = audit(candidate_theta)
            candidate_hard = -np.inf if candidate is None else float(np.min(candidate[0]))
            trials.append([alpha, candidate_hard])
            if chosen is None or candidate_hard > chosen[0]:
                chosen = (candidate_hard, candidate_theta, candidate, alpha)
        if chosen[2] is None or chosen[0] <= hard + 2e-10:
            trust *= 0.5
            history.append(
                {
                    "iteration": iteration,
                    "accepted": False,
                    "hard": hard,
                    "predicted": float(lp.x[-1]),
                    "trust": trust,
                    "trials": trials,
                }
            )
            print("reject", iteration, hard, "trust", trust, flush=True)
            if trust < 2e-7:
                break
            continue
        hard, theta, current, alpha = chosen
        trust = min(0.25, max(1e-5, trust * (1.25 if alpha >= 0.5 else 0.75)))
        order = np.argsort(current[0])[:8]
        history.append(
            {
                "iteration": iteration,
                "accepted": True,
                "hard": hard,
                "predicted": float(lp.x[-1]),
                "alpha": alpha,
                "trust": trust,
                "worst": [float(current[0][k]) for k in order],
                "trials": trials,
            }
        )
        print("accept", iteration, hard, "worst", history[-1]["worst"], flush=True)
        if hard > 0:
            print("OPEN_TARGET", hard, flush=True)
            break

    g, labels, points, denominator, fresh = current
    order = np.argsort(g)
    payload = {
        "version": 1,
        "method": "topology-exact projective hard-minimum SLP",
        "source": str(args.source),
        "theta": theta.tolist(),
        "hard_margin": float(np.min(g)),
        "minimum_projective_denominator": float(np.min(denominator)),
        "fresh_actual": summarize(fresh),
        "fresh_faces_match_source": {frozenset(f["cycle"]) for f in fresh.faces} == face_keys,
        "all_37_forced_rails": rails <= set(fresh.edges),
        "worst_guards": [
            {"value": float(g[k]), "feature": labels[k]} for k in order[:30]
        ],
        "history": history,
    }
    write_csv(args.output.with_suffix(".csv"), ids, points)
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({k: payload[k] for k in ("hard_margin", "minimum_projective_denominator", "fresh_actual")}, indent=2))


if __name__ == "__main__":
    main()
