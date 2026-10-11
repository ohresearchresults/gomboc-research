#!/usr/bin/env python3
"""Topology-free nonlinear escape search in the enlarged base plane.

Ten rows around the four-defect arc receive independent two-dimensional moves
in their common base plane.  Each trial is judged only after a fresh hull and
own-centroid rebuild.  The exact enlarged base label set and all 37 rail edges
are hard acceptance gates; topology changes elsewhere are allowed.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import differential_evolution


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
from search_row54_remote228 import (  # noqa: E402
    BASE,
    load_points,
    summarize,
)


DEFAULT_SOURCE = ROOT / "tracks/circuit_atlas/row54_endpoint_rebuilt.csv"
DEFAULT_AUDIT = ROOT / "tracks/circuit_atlas/row54_endpoint_rebuilt_audit.json"
DEFAULT_OUTPUT = HERE / "base_escape_search.json"
DEFAULT_CSV = HERE / "base_escape_best.csv"
CONTROLLED = (0, 1, 5, 6, 7, 8, 9, 10, 11, 54)
BASE_CYCLE = (0, 54) + tuple(range(1, 17))


class Search:
    def __init__(self, labels, source, forced_rails, focus="balanced", report=True):
        self.labels = labels
        self.source = source
        self.forced_rails = forced_rails
        self.index = {label: offset for offset, label in enumerate(labels)}
        self.report = report
        self.focus = focus
        self.calls = 0
        self.best = None
        self.improvements = []

        a = source[self.index[BASE_CYCLE[0]]]
        u = source[self.index[BASE_CYCLE[1]]] - a
        u /= np.linalg.norm(u)
        witness = source[self.index[BASE_CYCLE[2]]] - a
        normal = np.cross(u, witness)
        normal /= np.linalg.norm(normal)
        v = np.cross(normal, u)
        self.u, self.v = u, v
        self.scales = {}
        for offset, label in enumerate(BASE_CYCLE):
            previous = BASE_CYCLE[(offset - 1) % len(BASE_CYCLE)]
            following = BASE_CYCLE[(offset + 1) % len(BASE_CYCLE)]
            self.scales[label] = min(
                np.linalg.norm(source[self.index[label]] - source[self.index[previous]]),
                np.linalg.norm(source[self.index[following]] - source[self.index[label]]),
            )

    def coordinates(self, parameters):
        candidate = self.source.copy()
        for offset, label in enumerate(CONTROLLED):
            du, dv = parameters[2 * offset:2 * offset + 2]
            candidate[self.index[label]] += self.scales[label] * (
                du * self.u + dv * self.v
            )
        return candidate

    def evaluate(self, parameters):
        self.calls += 1
        candidate = self.coordinates(parameters)
        try:
            record = summarize(self.labels, candidate, self.forced_rails)
        except Exception:
            return 100.0
        valid = record["base_face_present"] and not record["missing_forced_rails"]
        violations = record["target_violations"]
        stable = [row["magnitude"] for row in violations if row["feature"].startswith("nonstable:")]
        unstable = [row["magnitude"] for row in violations if row["feature"].startswith("nonunstable:")]
        saddles = sorted(
            row["magnitude"] for row in violations if row["feature"].startswith("nonsaddle:")
        )
        focus_penalty = 0.0
        if self.focus == "stable_pair":
            focus_penalty = 10.0 * (sum(stable) + (saddles[0] if saddles else 0.0))
        elif self.focus == "unstable_pair":
            focus_penalty = 10.0 * (sum(unstable) + (saddles[-1] if saddles else 0.0))
        objective = (
            100.0 * record["target_violation_count"]
            + focus_penalty
            + record["target_violation_sum"]
            + 0.25 * max(0.0, -record["target_guard"])
            if valid else 10000.0
        )
        if self.best is None or objective < self.best[0]:
            self.best = (objective, np.asarray(parameters).copy(), record, candidate.copy())
            update = {
                "call": self.calls,
                "objective": float(objective),
                "target_guard": record["target_guard"],
                "target_guard_feature": record["target_guard_feature"],
                "target_violation_count": record["target_violation_count"],
                "target_violation_sum": record["target_violation_sum"],
                "focus": self.focus,
                "class": record["class"],
                "stable_faces": record["stable_faces"],
                "unstable_vertices": record["unstable_vertices"],
                "saddle_edges": record["saddle_edges"],
                "f_vector": record["f_vector"],
                "base_face_present": record["base_face_present"],
                "missing_forced_rails": record["missing_forced_rails"],
            }
            self.improvements.append(update)
            if self.report:
                print(json.dumps(update, sort_keys=True), flush=True)
        return objective


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--audit", type=Path, default=DEFAULT_AUDIT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--csv-output", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--seed", type=int, default=831811)
    parser.add_argument("--generations", type=int, default=40)
    parser.add_argument("--popsize", type=int, default=5)
    parser.add_argument("--bound", type=float, default=8.0)
    parser.add_argument("--start-json", type=Path)
    parser.add_argument(
        "--focus", choices=("balanced", "stable_pair", "unstable_pair"),
        default="balanced",
    )
    args = parser.parse_args()

    labels, source = load_points(args.source)
    source_audit = json.loads(args.audit.read_text())
    forced_rails = {
        tuple(sorted(edge))
        for edge in source_audit["fresh_hull_audit"]["forced_rail_edges"]
    }
    search = Search(labels, source, forced_rails, focus=args.focus)
    start = np.zeros(2 * len(CONTROLLED))
    if args.start_json:
        start_record = json.loads(args.start_json.read_text())
        start = np.asarray(start_record["best_parameters"], dtype=float)
        if start.shape != (2 * len(CONTROLLED),):
            raise ValueError(("start parameter shape", start.shape))
        bounds = [(float(value - args.bound), float(value + args.bound)) for value in start]
    else:
        bounds = [(-args.bound, args.bound)] * (2 * len(CONTROLLED))
    result = differential_evolution(
        search.evaluate,
        bounds,
        seed=args.seed,
        maxiter=args.generations,
        popsize=args.popsize,
        tol=1e-8,
        polish=False,
        updating="immediate",
        workers=1,
        x0=start,
    )
    assert search.best is not None
    objective, parameters, best, coordinates = search.best
    with args.csv_output.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(("source_id", "x", "y", "z"))
        for label, point in zip(labels, coordinates):
            writer.writerow([label, *[format(float(value), ".17g") for value in point]])
    payload = {
        "version": 1,
        "source": str(args.source.resolve()),
        "scope": "20-dimensional in-base-plane nonlinear actual-hull search",
        "controlled_rows": list(CONTROLLED),
        "base_cycle": list(BASE_CYCLE),
        "base_u": search.u.tolist(),
        "base_v": search.v.tolist(),
        "row_scales": search.scales,
        "seed": args.seed,
        "generations": args.generations,
        "popsize": args.popsize,
        "bound": args.bound,
        "start_json": None if args.start_json is None else str(args.start_json.resolve()),
        "start_parameters": start.tolist(),
        "focus": args.focus,
        "calls": search.calls,
        "optimizer_message": str(result.message),
        "best_parameters": parameters.tolist(),
        "best": best,
        "best_coordinates": str(args.csv_output.resolve()),
        "winner": bool(
            best["class"] == [1, 1, 0]
            and best["stable_base"]
            and not best["missing_forced_rails"]
        ),
        "improvements": search.improvements,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "calls": search.calls,
        "winner": payload["winner"],
        "best": best,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
