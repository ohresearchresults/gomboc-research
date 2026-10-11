#!/usr/bin/env python3
"""Optimize a coordinated long-rail carrier across the stable wall."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution, minimize

from actual_hull_mechanics import evaluate, load_common_lattice
from search_two_actuator import SOURCE, project, row228_shortcut


HERE = Path(__file__).resolve().parent
BASE = tuple(range(17))


def bernstein_weights(control: np.ndarray, count: int) -> np.ndarray:
    """Cubic Bernstein profile with final endpoint fixed to one."""
    p0, p1, p2 = control
    s = np.linspace(0, 1, count)
    return (
        p0 * (1 - s) ** 3
        + 3 * p1 * s * (1 - s) ** 2
        + 3 * p2 * s**2 * (1 - s)
        + s**3
    )


class Search:
    def __init__(self, labels, shell, direction, crossing):
        self.labels = labels
        self.index = {label: offset for offset, label in enumerate(labels)}
        self.shell = shell
        self.direction = direction
        self.crossing = crossing
        self.calls = 0
        self.best = (-1e100, None, None)

    def candidate(self, controls):
        result = self.shell.copy()
        weights = bernstein_weights(np.asarray(controls), 12)
        for label, weight in zip(range(247, 259), weights):
            result[self.index[label]] += self.crossing * weight * self.direction
        return result, weights

    def evaluate(self, controls, report=False):
        self.calls += 1
        candidate, weights = self.candidate(controls)
        try:
            mechanics = evaluate(self.labels, candidate)
        except Exception:
            return 1000.0
        if BASE not in mechanics.face_decisions or 8 not in mechanics.vertex_decisions:
            return 1000.0
        guards = []
        for face, decision in mechanics.face_decisions.items():
            guards.append(decision if face == BASE else -decision)
        for vertex, decision in mechanics.vertex_decisions.items():
            guards.append(decision if vertex == 8 else -decision)
        guards.extend(-decision for decision in mechanics.edge_decisions.values())
        guards = np.asarray(guards)
        balanced = guards / (0.03 + np.abs(guards))
        score = 0.7 * float(np.min(balanced)) + 0.3 * float(np.mean(balanced))
        if score > self.best[0]:
            record = {
                "score": score,
                "hard": float(np.min(guards)),
                "controls": np.asarray(controls).tolist(),
                "weights_247_to_258": weights.tolist(),
                "f_vector": [mechanics.vertices, mechanics.edges, mechanics.faces],
                "class": list(mechanics.cls),
                "stable_faces": [sorted(face) for face in mechanics.stable_faces],
                "unstable_vertices": mechanics.unstable_vertices,
                "saddle_edges": [list(edge) for edge in mechanics.saddle_edges],
            }
            self.best = (score, np.asarray(controls).copy(), record)
            if report:
                print("best", self.calls, json.dumps(record, sort_keys=True), flush=True)
        return -score


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=831701)
    parser.add_argument("--generations", type=int, default=45)
    parser.add_argument("--popsize", type=int, default=7)
    parser.add_argument("--crossing", type=float, default=1.05)
    parser.add_argument("--output", default="group_carrier_search.json")
    args = parser.parse_args()

    labels, source = load_common_lattice(SOURCE)
    index = {label: offset for offset, label in enumerate(labels)}
    shell = row228_shortcut(source, index, 0.01, -0.01)
    endpoint = project(
        shell[index[258]], shell[index[198]], shell[index[224]], shell[index[241]]
    )
    direction = endpoint - shell[index[258]]
    search = Search(labels, shell, direction, args.crossing)
    result = differential_evolution(
        lambda controls: search.evaluate(controls, report=True),
        [(-3, 3)] * 3,
        seed=args.seed,
        maxiter=args.generations,
        popsize=args.popsize,
        polish=False,
        updating="immediate",
        workers=1,
    )
    start = search.best[1] if search.best[1] is not None else result.x
    minimize(
        lambda controls: search.evaluate(controls, report=True),
        start,
        method="Nelder-Mead",
        options={"maxiter": 500, "xatol": 1e-10, "fatol": 1e-10},
    )
    payload = {
        "seed": args.seed,
        "crossing": args.crossing,
        "calls": search.calls,
        "best": search.best[2],
        "optimizer_message": str(result.message),
    }
    (HERE / args.output).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2), flush=True)


if __name__ == "__main__":
    main()
