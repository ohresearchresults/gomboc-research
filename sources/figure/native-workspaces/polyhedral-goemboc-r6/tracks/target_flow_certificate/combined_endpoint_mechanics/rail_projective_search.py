#!/usr/bin/env python3
"""Projective/trace-free-SPD macromotion inside the fixed combined cell.

Unlike arbitrary 164-chart steps, this eight-dimensional family preserves the
entire face lattice for every positive projective denominator.  It is thus a
safe macromotion on the extremely thin rebuilt Tutte cap.  The objective asks
for the simultaneous death of the extra quad-stable, U54, H67 and H910
features while retaining only the enlarged base and U8.
"""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import argparse
import csv
import json
import sys

import numpy as np
from scipy.optimize import differential_evolution, minimize

import combined_core as ledger_core
import rail_combined_core as rail_core


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ATLAS = ROOT / "tracks" / "circuit_atlas"
sys.path.insert(0, str(ATLAS))
import row54_four_residual_search as metric  # noqa: E402


def incidence(faces):
    ans = defaultdict(list)
    for fi, cyc in enumerate(faces):
        for u, v in zip(cyc, cyc[1:] + cyc[:1]):
            ans[tuple(sorted((u, v)))].append(fi)
    return dict(ans)


def save_csv(path, ids, points):
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(("source_id", "x", "y", "z"))
        for i, p in zip(ids, points):
            w.writerow((i, *(f"{float(z):.17g}" for z in p)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=831731)
    ap.add_argument("--generations", type=int, default=100)
    ap.add_argument("--popsize", type=int, default=12)
    ap.add_argument("--local-iters", type=int, default=1200)
    ap.add_argument("--output", default="rail_projective_search.json")
    args = ap.parse_args()

    robust, faces, inc, _ = rail_core.build_geometry()
    ids = sorted(robust)
    p0 = np.asarray([robust[i] for i in ids])
    # Keep the face order shared with the 164-row tree/cotree certificate.
    points0, *_ = ledger_core.rigid_base_chart(robust)
    faces = ledger_core.orient_faces_for_positive_volume(points0, faces)
    # The atlas search calls the extra stable face ``SFAR``.  At the exact
    # combined wall its two triangles have merged into this maximal quad.
    metric.SFAR = frozenset((7, 8, 245, 246))
    search = metric.Search(ids, p0, faces, "escape")
    zero = np.zeros(8)
    search.evaluate(zero, report=True)
    bounds = [(-0.9, 0.9)] * 3 + [(-2.2, 2.2)] * 5
    de = differential_evolution(
        lambda x: search.evaluate(x, report=True), bounds,
        seed=args.seed, maxiter=args.generations, popsize=args.popsize,
        tol=1e-9, polish=False, updating="immediate", workers=1, x0=zero,
    )
    theta = search.best[2] if search.best[2] is not None else de.x
    local = None
    if args.local_iters:
        local = minimize(
            lambda x: search.evaluate(x, report=True), theta,
            method="Nelder-Mead",
            options={"maxiter": args.local_iters, "xatol": 1e-11, "fatol": 1e-11},
        )
        theta = search.best[2]

    p, den = metric.transform(p0, theta)
    fixed, metric_stable, metric_unstable, metric_saddles = metric.classify(ids, p, faces)
    guards, labels = metric.signed_guards(fixed, faces, "escape")
    audit, fresh_faces, _ = metric.fresh_audit(ids, p, faces)

    # Re-evaluate the fixed 164-row tree/cotree ledger at the same point.
    _, _, _, pv, pf, _ = rail_core.load_problem()
    rigid, *_ = ledger_core.rigid_base_chart({i: p[k] for k, i in enumerate(ids)})
    chart = ledger_core.make_chart(rigid)
    x = chart.pack(rigid)
    vals, topo, geom, ledger_labels = ledger_core.evaluate_chart(
        x, chart, faces, inc, pv, pf
    )

    record = {
        "version": 1,
        "scope": "rail-preserving fixed combined endpoint",
        "seed": args.seed,
        "theta": theta.tolist(),
        "minimum_projective_denominator": float(np.min(den)),
        "escape_hard_margin": float(np.min(guards)),
        "escape_positive": int(np.sum(guards > 0)),
        "escape_rows": len(guards),
        "worst_escape_guards": [
            {"value": float(guards[k]), "feature": labels[k]}
            for k in np.argsort(guards)[:30]
        ],
        "fixed_class": [len(metric_stable), len(metric_unstable), len(metric_saddles)],
        "fixed_stable_faces": metric_stable,
        "fixed_unstable_vertices": metric_unstable,
        "fixed_saddle_edges": metric_saddles,
        "fresh_hull_audit": audit,
        "ledger_positive": int(np.sum(vals > 0)),
        "ledger_mechanical_positive": int(np.sum(vals[:-1] > 0)),
        "ledger_hard": float(np.min(vals)),
        "topology_guard_min": float(np.min(topo)),
        "worst_ledger": [
            {"value": float(vals[k]), "label": ledger_labels[k]}
            for k in np.argsort(vals)[:30]
        ],
        "calls": search.calls,
        "optimizer_message": str(de.message),
        "local_optimizer_message": None if local is None else str(local.message),
    }
    out = HERE / args.output
    out.write_text(json.dumps(record, indent=2) + "\n")
    save_csv(out.with_suffix(".csv"), ids, p)
    print(json.dumps({k: record[k] for k in (
        "escape_hard_margin", "escape_positive", "fixed_class",
        "ledger_positive", "ledger_hard", "topology_guard_min", "calls"
    )}, indent=2))


if __name__ == "__main__":
    main()
