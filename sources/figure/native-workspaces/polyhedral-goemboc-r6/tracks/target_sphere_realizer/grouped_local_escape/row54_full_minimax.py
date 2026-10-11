#!/usr/bin/env python3
"""Full all-feature minimax in the row54 far-side projective metric family."""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution, minimize

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CIRCUIT = ROOT / "tracks/circuit_atlas"
sys.path.insert(0, str(CIRCUIT))
sys.path.insert(0, str(HERE))

import row54_four_residual_search as core  # noqa: E402
from actual_grouped import evaluate, summarize  # noqa: E402

BASE = frozenset(range(17)) | {54}
SHORT_RAIL = [228] + list(range(229, 247)) + [8]
LONG_RAIL = [228] + list(range(247, 265)) + [8]


def read_points(path):
    rows = {}
    with path.open() as f:
        for r in csv.DictReader(f):
            rows[int(r["source_id"])] = np.array([float(r[k]) for k in ("x", "y", "z")])
    ids = sorted(rows)
    return ids, np.array([rows[i] for i in ids])


def guards(m, faces):
    g, labels = [], []
    for k, cyc in enumerate(faces):
        keep = frozenset(cyc) == BASE
        g.append(float(m["fdec"][k]) if keep else -float(m["fdec"][k]))
        labels.append(("S+" if keep else "S-", list(cyc)))
    for i, z in m["udec"].items():
        keep = i == 8
        g.append(float(z) if keep else -float(z))
        labels.append(("U+" if keep else "U-", i))
    for e, z in m["edec"].items():
        g.append(-float(z))
        labels.append(("H-", list(e)))
    return np.asarray(g), labels


class FullMinimax:
    def __init__(self, ids, source, faces):
        self.ids, self.source, self.faces = ids, source, faces
        self.calls = 0
        self.best_score = (-np.inf, None, None)
        self.best_hard = (-np.inf, None, None)
        p, _ = core.transform(source, np.zeros(8))
        g, self.labels = guards(core.mechanics(ids, p, faces), faces)
        self.scale = np.maximum(0.025, np.minimum(1.0, np.abs(g)))

    def evaluate(self, theta, report=False):
        self.calls += 1
        p, den = core.transform(self.source, np.asarray(theta))
        if p is None or float(np.min(den)) <= 0.055:
            return 10.0 + max(0.0, 0.055 - float(np.min(den)))
        try:
            g, labels = guards(core.mechanics(self.ids, p, self.faces), self.faces)
        except Exception:
            return 10.0
        b = g / (self.scale + np.abs(g))
        order = np.argsort(b)
        score = (0.58 * float(b[order[0]]) +
                 0.27 * float(np.mean(b[order[:6]])) +
                 0.10 * float(np.mean(b[order[:18]])) +
                 0.05 * float(np.mean(b)))
        hard = float(np.min(g))
        worst = [(float(g[k]), labels[k]) for k in np.argsort(g)[:16]]
        if hard > self.best_hard[0]:
            self.best_hard = (hard, np.asarray(theta).copy(), worst)
        if score > self.best_score[0]:
            self.best_score = (score, np.asarray(theta).copy(), worst)
            if report:
                print("best", self.calls, "score", score, "hard", hard,
                      "best_hard", self.best_hard[0], "worst", worst[:5], flush=True)
        return -score


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, default=CIRCUIT / "row54_far_rebuilt.csv")
    ap.add_argument("--start", type=Path, default=None)
    ap.add_argument("--seed", type=int, default=831561)
    ap.add_argument("--generations", type=int, default=80)
    ap.add_argument("--popsize", type=int, default=12)
    ap.add_argument("--local-iters", type=int, default=800)
    ap.add_argument("--output", type=Path, default=HERE / "row54_full_minimax.json")
    args = ap.parse_args()

    ids, source = read_points(args.source)
    p0, _ = core.transform(source, np.zeros(8))
    hull, faces, _ = core.group_maximal_faces(ids, p0)
    ef, _ = core.edge_lattice(faces)
    assert [len(hull.vertices), len(ef), len(faces)] == [61, 162, 103]
    face_keys = {frozenset(c) for c in faces}
    x0 = np.zeros(8)
    if args.start:
        x0 = np.asarray(json.load(args.start.open())["theta"])
    search = FullMinimax(ids, source, faces)
    search.evaluate(x0, report=True)
    # Wider boxes find formally better sign scores only by collapsing true
    # edge normal cones below the mandatory 1e-26 Gram cutoff.  This box
    # contains the audited transfer path but excludes those ill-conditioned
    # pseudo-improvements.
    bounds = [(-0.75, 0.75)] * 3 + [(-1.6, 1.6)] * 5
    de = differential_evolution(
        lambda z: search.evaluate(z, report=True), bounds,
        x0=x0, seed=args.seed, maxiter=args.generations, popsize=args.popsize,
        polish=False, tol=1e-9, updating="immediate", workers=1,
    )
    theta = search.best_score[1] if search.best_score[1] is not None else de.x
    local = None
    if args.local_iters:
        local = minimize(lambda z: search.evaluate(z, report=True), theta,
                         method="Nelder-Mead",
                         options={"maxiter": args.local_iters,
                                  "xatol": 1e-11, "fatol": 1e-11})
        theta = search.best_score[1]
    p, den = core.transform(source, theta)
    g, labels = guards(core.mechanics(ids, p, faces), faces)
    actual = evaluate({i: p[k] for k, i in enumerate(ids)}, coplanar_rel=1e-11)
    actual_faces = {frozenset(f["cycle"]) for f in actual.faces} if actual.valid else set()
    edges = set(actual.edges) if actual.valid else set()
    rail_ok = {
        name: all(tuple(sorted(e)) in edges for e in zip(path, path[1:]))
        for name, path in (("short", SHORT_RAIL), ("long", LONG_RAIL))
    }
    out = {
        "version": 1,
        "theta": theta.tolist(),
        "requested_hard_margin": float(np.min(g)),
        "best_raw_hard_seen": float(search.best_hard[0]),
        "best_raw_hard_theta": search.best_hard[1].tolist(),
        "worst_requested_guards": [
            {"value": float(g[k]), "feature": labels[k]} for k in np.argsort(g)[:30]
        ],
        "minimum_projective_denominator": float(np.min(den)),
        "fresh_actual": summarize(actual),
        "fresh_faces_match_source": actual_faces == face_keys,
        "rail_edges_present": rail_ok,
        "calls": search.calls,
        "optimizer_message": str(de.message),
        "local_optimizer_message": None if local is None else str(local.message),
    }
    args.output.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
