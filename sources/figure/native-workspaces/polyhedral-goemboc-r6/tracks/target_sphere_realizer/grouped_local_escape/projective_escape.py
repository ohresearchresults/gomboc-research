#!/usr/bin/env python3
"""Guarded projective/trace-free-SPD escape on the reconstructed far-side cell.

The projective family is useful here because, while all projective
denominators have one sign, it preserves the complete face lattice exactly.
Candidates are optimized with the fixed maximal-face mechanics and then
recomputed from a fresh Qhull by :mod:`actual_grouped` before they are saved.
"""
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
from actual_grouped import evaluate as actual_evaluate, summarize  # noqa: E402

TARGET_SOURCE = CIRCUIT / "target_sphere_rebuilt.csv"
ROBUST_AUDIT = CIRCUIT / "robust_target_rebuilt_audit.json"
BASE = frozenset(range(17))
TARGET_U = {8}
SHORT_RAIL = [228] + list(range(229, 247)) + [8]
LONG_RAIL = [228] + list(range(247, 265)) + [8]


def read_rows(path: Path = TARGET_SOURCE):
    rows: dict[int, np.ndarray] = {}
    with path.open() as f:
        for r in csv.DictReader(f):
            rows[int(r["source_id"])] = np.array(
                [float(r[k]) for k in ("x", "y", "z")], dtype=float
            )
    ids = sorted(rows)
    return ids, np.array([rows[i] for i in ids])


def far_side_rows(ids, raw, *, depth=1e-3,
                  tangent_a=-0.21,
                  tangent_b=0.0):
    """Move 246 through (7,8,245) in the support-valid tangent chamber."""
    ix = {i: k for k, i in enumerate(ids)}
    out = raw.copy()
    a = raw[ix[7]]
    n = np.cross(raw[ix[8]] - a, raw[ix[245]] - a)
    n /= np.linalg.norm(n)
    signed_depth = float(np.dot(n, raw[ix[246]] - a))
    wall = raw[ix[246]] - signed_depth * n
    u = raw[ix[8]] - a
    u /= np.linalg.norm(u)
    v = np.cross(n, u)
    out[ix[246]] = (
        wall - np.sign(signed_depth) * depth * n
        + tangent_a * u + tangent_b * v
    )
    return out


def target_guards(m, faces, ids, p, den):
    """One signed guard per requested feature; positive is feasible."""
    vals: list[float] = []
    labels: list[tuple] = []
    for k, cyc in enumerate(faces):
        positive = frozenset(cyc) == BASE
        vals.append(float(m["fdec"][k]) if positive else -float(m["fdec"][k]))
        labels.append(("S+" if positive else "S-", list(cyc)))
    for i, z in m["udec"].items():
        positive = i in TARGET_U
        vals.append(float(z) if positive else -float(z))
        labels.append(("U+" if positive else "U-", i))
    for e, z in m["edec"].items():
        vals.append(-float(z))
        labels.append(("H-", list(e)))

    # The true-edge part of each rail is invariant projectively.  These two
    # metric acute guards are not, and therefore belong in the search.
    ix = {i: k for k, i in enumerate(ids)}
    x = p - m["centroid"]
    for name, rail in (("short", SHORT_RAIL), ("long", LONG_RAIL)):
        for a, b in zip(rail, rail[1:]):
            xa, xb = x[ix[a]], x[ix[b]]
            edge = xb - xa
            vals.append(float(np.dot(xa, edge) /
                              max(np.linalg.norm(xa) * np.linalg.norm(edge), 1e-300)))
            labels.append(("Rdir+", name, [a, b]))
            # Rdir+ implies xa.xb > ||xa||^2 > 0, so a second positive-dot
            # row would be redundant in the optimization.  It is rechecked
            # explicitly in the final certificate.

    # A positive common affine chart is the projective topology certificate.
    for i, z in zip(ids, den):
        vals.append(float(z - 0.035))
        labels.append(("Pden+", i))
    return np.asarray(vals), labels


class Search:
    def __init__(self, ids, raw, faces, start):
        self.ids, self.raw, self.faces = ids, raw, faces
        self.calls = 0
        self.best = (-np.inf, -np.inf, None, None)
        p, den = core.transform(raw, start)
        m = core.mechanics(ids, p, faces)
        g, labels = target_guards(m, faces, ids, p, den)
        self.labels = labels
        # Decisions have different natural units.  This fixed sign-preserving
        # scale prevents large edge beta values from drowning vertex guards.
        self.scales = np.maximum(0.04, np.minimum(1.0, np.abs(g)))

    def objective(self, theta, report=False):
        self.calls += 1
        p, den = core.transform(self.raw, np.asarray(theta, dtype=float))
        if p is None or float(np.min(den)) <= 0.035:
            return 20.0 + max(0.0, 0.035 - float(np.min(den)))
        try:
            m = core.mechanics(self.ids, p, self.faces)
            g, labels = target_guards(m, self.faces, self.ids, p, den)
        except Exception:
            return 20.0
        b = g / (self.scales + np.abs(g))
        order = np.argsort(b)
        worst = b[order[:16]]
        # A broad lower-tail objective has a usable basin; raw feasibility is
        # still gated solely by the unscaled minimum signed guard.
        score = (0.44 * float(b[order[0]]) +
                 0.36 * float(np.mean(worst[:8])) +
                 0.15 * float(np.mean(worst)) +
                 0.05 * float(np.mean(b)))
        hard = float(np.min(g))
        if score > self.best[0]:
            self.best = (score, hard, np.asarray(theta).copy(),
                         [(float(g[k]), labels[k]) for k in np.argsort(g)[:20]])
            if report:
                print("best", self.calls, "score", score, "hard", hard,
                      "worst", self.best[3][:5], flush=True)
        return -score


def write_csv(path: Path, ids, p):
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source_id", "x", "y", "z"])
        for i, xyz in zip(ids, p):
            w.writerow([i, *(f"{float(z):.17g}" for z in xyz)])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=831541)
    ap.add_argument("--generations", type=int, default=80)
    ap.add_argument("--popsize", type=int, default=12)
    ap.add_argument("--local-iters", type=int, default=1200)
    ap.add_argument("--depth", type=float, default=1e-5)
    ap.add_argument("--output", default="projective_escape.json")
    args = ap.parse_args()

    ids, target_raw = read_rows()
    raw = far_side_rows(ids, target_raw, depth=args.depth)
    start_record = json.load(ROBUST_AUDIT.open())
    start = np.asarray(start_record["theta"], dtype=float)
    p0, _ = core.transform(raw, start)
    hull0, faces0, _ = core.group_maximal_faces(ids, p0)
    ef0, _ = core.edge_lattice(faces0)
    assert [len(hull0.vertices), len(ef0), len(faces0)] == [61, 163, 104]
    assert any(frozenset(c) == BASE for c in faces0)
    assert any(frozenset(c) == frozenset((7, 8, 246)) for c in faces0)

    search = Search(ids, raw, faces0, start)
    search.objective(start, report=True)
    bounds = [(-0.92, 0.92)] * 3 + [(-2.4, 2.4)] * 5
    de = differential_evolution(
        lambda z: search.objective(z, report=True), bounds,
        seed=args.seed, maxiter=args.generations, popsize=args.popsize,
        x0=start, polish=False, tol=1e-9, updating="immediate", workers=1,
    )
    theta = search.best[2] if search.best[2] is not None else de.x
    local = None
    if args.local_iters:
        local = minimize(lambda z: search.objective(z, report=True), theta,
                         method="Nelder-Mead",
                         options={"maxiter": args.local_iters,
                                  "xatol": 1e-11, "fatol": 1e-11})
        theta = search.best[2]

    p, den = core.transform(raw, theta)
    fixed = core.mechanics(ids, p, faces0)
    guards, labels = target_guards(fixed, faces0, ids, p, den)
    actual = actual_evaluate({i: p[k] for k, i in enumerate(ids)})
    actual_faces = ({frozenset(f["cycle"]) for f in actual.faces}
                    if actual.valid else set())
    fixed_faces = {frozenset(c) for c in faces0}
    rail_edges = {
        name: all(tuple(sorted(e)) in set(actual.edges)
                  for e in zip(rail, rail[1:]))
        for name, rail in (("short", SHORT_RAIL), ("long", LONG_RAIL))
    } if actual.valid else {"short": False, "long": False}
    out = {
        "version": 1,
        "seed": args.seed,
        "far_side": {"depth": args.depth,
                     "tangent_a": -0.21,
                     "tangent_b": 0.0},
        "theta": theta.tolist(),
        "minimum_projective_denominator": float(np.min(den)),
        "requested_hard_margin": float(np.min(guards)),
        "worst_requested_guards": [
            {"value": float(guards[k]), "feature": labels[k]}
            for k in np.argsort(guards)[:30]
        ],
        "fixed_faces_match_fresh": actual_faces == fixed_faces,
        "rail_edges_present": rail_edges,
        "fresh_actual": summarize(actual),
        "calls": search.calls,
        "optimizer_message": str(de.message),
        "local_optimizer_message": None if local is None else str(local.message),
    }
    outpath = HERE / args.output
    outpath.write_text(json.dumps(out, indent=2) + "\n")
    write_csv(outpath.with_suffix(".csv"), ids, p)
    print(json.dumps(out, indent=2), flush=True)


if __name__ == "__main__":
    main()
