#!/usr/bin/env python3
"""Direct local vertex-chart search with a fresh grouped hull every call."""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from actual_grouped import evaluate, summarize  # noqa: E402
from row54_joint_actual_search import (  # noqa: E402
    feature_guards, BASE, RAIL_EDGES, write_csv,
)


def read_points(path):
    rows = {}
    with path.open() as f:
        for r in csv.DictReader(f):
            rows[int(r["source_id"])] = np.asarray(
                [float(r[k]) for k in ("x", "y", "z")]
            )
    ids = sorted(rows)
    return ids, np.asarray([rows[i] for i in ids])


class DirectActual:
    def __init__(self, ids, source):
        self.ids = ids
        self.source = source
        self.ix = {i: k for k, i in enumerate(ids)}
        a = source[self.ix[0]]
        normal = np.cross(source[self.ix[1]] - a,
                          source[self.ix[2]] - a)
        normal /= np.linalg.norm(normal)
        u = source[self.ix[1]] - a
        u /= np.linalg.norm(u)
        v = np.cross(normal, u)
        self.controls = []
        # Keep every enlarged-base vertex exactly in its common plane.
        for i, scale in ((1, 0.002), (6, 0.01), (7, 0.01),
                         (8, 0.01), (54, 0.002)):
            self.controls.extend([(i, scale * u), (i, scale * v)])
        # These vertices have only triangular incident faces in the source
        # cell, so unrestricted local moves do not destroy a prescribed
        # coplanarity. q198 is deliberately excluded: its normal cone is so
        # shallow that 1e-9 moves deactivate many rail vertices.
        for i, scale in ((245, 0.005), (246, 0.005), (263, 0.005)):
            self.controls.extend((i, scale * e) for e in np.eye(3))
        self.calls = 0
        self.feasible = 0
        self.best_hard = (-np.inf, None, None)
        self.best_score = (-np.inf, None, None)
        self.best_by_class = {}

    def construct(self, y):
        p = self.source.copy()
        for z, (i, direction) in zip(y, self.controls):
            p[self.ix[i]] += float(z) * direction
        return p

    def audit(self, y):
        p = self.construct(y)
        actual = evaluate(
            {i: p[k] for k, i in enumerate(self.ids)}, coplanar_rel=1e-11
        )
        if not actual.valid:
            return p, actual, None
        faces = {frozenset(f["cycle"]) for f in actual.faces}
        if (len(actual.active) != 61 or set(actual.active) != set(self.ids)
                or BASE not in faces or 8 not in actual.vertex_decisions
                or not RAIL_EDGES <= set(actual.edges)
                or actual.topology_margin <= 1e-12):
            return p, actual, None
        return p, actual, feature_guards(actual)

    def objective(self, y, report=True):
        self.calls += 1
        p, actual, packet = self.audit(y)
        if packet is None:
            return 3.0
        self.feasible += 1
        guards, labels = packet
        balanced = guards / (0.002 + np.abs(guards))
        order = np.argsort(balanced)
        score = (0.62 * float(balanced[order[0]])
                 + 0.25 * float(np.mean(balanced[order[:6]]))
                 + 0.10 * float(np.mean(balanced[order[:20]]))
                 + 0.03 * float(np.mean(balanced)))
        hard = float(np.min(guards))
        worst = [
            {"value": float(guards[k]), "feature": labels[k]}
            for k in np.argsort(guards)[:16]
        ]
        cls = (len(actual.stable), len(actual.unstable), len(actual.saddles))
        if cls not in self.best_by_class or hard > self.best_by_class[cls][0]:
            self.best_by_class[cls] = (hard, np.asarray(y).copy())
        if hard > self.best_hard[0]:
            self.best_hard = (hard, np.asarray(y).copy(), worst)
            if report:
                print("hard", self.calls, hard, "class", cls,
                      "f", [len(actual.active), len(actual.edges), len(actual.faces)],
                      "worst", worst[:6], flush=True)
        if score > self.best_score[0]:
            self.best_score = (score, np.asarray(y).copy(), worst)
            if report:
                print("score", self.calls, score, "hard", hard,
                      "class", cls, flush=True)
        if hard > 0:
            print("OPEN_TARGET", hard, flush=True)
        return -score


def encode(search, y):
    points, actual, packet = search.audit(y)
    guards, labels = packet
    order = np.argsort(guards)
    return points, {
        "parameters": np.asarray(y).tolist(),
        "hard_margin": float(np.min(guards)),
        "fresh_actual": summarize(actual),
        "worst_guards": [
            {"value": float(guards[k]), "feature": labels[k]}
            for k in order[:30]
        ],
        "rail_edges_present": RAIL_EDGES <= set(actual.edges),
        "base_face_present": BASE in {
            frozenset(f["cycle"]) for f in actual.faces
        },
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path,
                    default=HERE / "row54_joint_actual_best.csv")
    ap.add_argument("--iterations", type=int, default=1100)
    ap.add_argument("--simplex", type=float, default=0.012)
    ap.add_argument("--radius", type=float, default=1.0)
    ap.add_argument("--output", type=Path,
                    default=HERE / "row54_direct_actual.json")
    args = ap.parse_args()

    ids, source = read_points(args.source)
    search = DirectActual(ids, source)
    y0 = np.zeros(len(search.controls))
    search.objective(y0)
    simplex = np.zeros((len(y0) + 1, len(y0)))
    for j in range(len(y0)):
        simplex[j + 1, j] = args.simplex
    result = minimize(
        lambda z: search.objective(z), y0, method="Nelder-Mead",
        bounds=[(-args.radius, args.radius)] * len(y0),
        options={"maxiter": args.iterations, "initial_simplex": simplex,
                 "xatol": 2e-10, "fatol": 2e-10,
                 "adaptive": True},
    )
    records = []
    for name, y in (("best_hard", search.best_hard[1]),
                    ("best_score", search.best_score[1])):
        points, record = encode(search, y)
        record["name"] = name
        records.append(record)
        if name == "best_hard":
            write_csv(args.output.with_name(args.output.stem + "_best.csv"),
                      ids, points)
            actual = search.audit(y)[1]
            with args.output.with_name(args.output.stem + "_best_faces.json").open("w") as f:
                json.dump([face["cycle"] for face in actual.faces], f, indent=2)
    output = {
        "version": 1,
        "method": "post-metric direct local vertex chart; fresh actual hull",
        "source": str(args.source),
        "control_vertex_ids": [i for i, _ in search.controls],
        "calls": search.calls,
        "feasible_calls": search.feasible,
        "best_hard_seen": float(search.best_hard[0]),
        "best_score_seen": float(search.best_score[0]),
        "best_by_actual_class": {
            str(k): {"hard_margin": float(v[0]),
                     "parameters": v[1].tolist()}
            for k, v in sorted(search.best_by_class.items())
        },
        "audited_candidates": records,
        "optimizer_message": str(result.message),
    }
    args.output.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
