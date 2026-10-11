#!/usr/bin/env python3
"""Search the reconstructed row-228 shortcut plus one stable-edge actuator."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from actual_hull_mechanics import evaluate, load_common_lattice


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / "M42_acute_bridge_fifth_cell_work" / "fifth_cell_endpoint" / "input_rows_common_lattice.csv"


def project(point: np.ndarray, a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    normal = np.cross(b - a, c - a)
    return point - normal * np.dot(normal, point - a) / np.dot(normal, normal)


def row228_shortcut(
    points: np.ndarray, index: dict[int, int], delta: float, eta: float
) -> np.ndarray:
    a, b, c = (points[index[label]] for label in (224, 229, 247))
    old = points[index[228]]
    projected = project(old, a, b, c)
    edge1, edge2, rhs = b - a, c - a, projected - a
    gram = np.asarray(
        [[np.dot(edge1, edge1), np.dot(edge1, edge2)],
         [np.dot(edge1, edge2), np.dot(edge2, edge2)]]
    )
    bary_b, bary_c = np.linalg.solve(gram, [np.dot(edge1, rhs), np.dot(edge2, rhs)])
    weight_b = bary_b / (bary_b + bary_c)
    edge_point = weight_b * b + (1 - weight_b) * c
    wall = -delta * a + (1 + delta) * edge_point
    result = points.copy()
    result[index[228]] = wall + eta * (old - projected)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--actuator", choices=("258", "241"), default="258")
    parser.add_argument("--delta", type=float, default=0.1)
    parser.add_argument("--eta", type=float, default=-1e-6)
    parser.add_argument("--t-min", type=float, default=-0.5)
    parser.add_argument("--t-max", type=float, default=2.5)
    parser.add_argument("--steps", type=int, default=301)
    parser.add_argument("--output", type=Path, default=HERE / "two_actuator_scan.json")
    args = parser.parse_args()

    labels, source = load_common_lattice(SOURCE)
    index = {label: offset for offset, label in enumerate(labels)}
    shortcut = row228_shortcut(source, index, args.delta, args.eta)

    moving = int(args.actuator)
    if moving == 258:
        plane = (198, 224, 241)
    else:
        plane = (198, 224, 258)
    endpoint = project(
        shortcut[index[moving]], *(shortcut[index[label]] for label in plane)
    )
    direction = endpoint - shortcut[index[moving]]

    records: list[dict[str, object]] = []
    seen: dict[tuple[object, ...], dict[str, object]] = {}
    for t in np.linspace(args.t_min, args.t_max, args.steps):
        if abs(t - 1) < 1e-10:
            continue
        candidate = shortcut.copy()
        candidate[index[moving]] += t * direction
        try:
            mechanics = evaluate(labels, candidate)
        except Exception as exc:  # Qhull/near-wall proposer failure is recorded, not hidden.
            records.append({"t": float(t), "error": repr(exc)})
            continue
        record: dict[str, object] = {
            "t": float(t),
            "f_vector": [mechanics.vertices, mechanics.edges, mechanics.faces],
            "class": list(mechanics.cls),
            "stable_faces": [sorted(face) for face in mechanics.stable_faces],
            "unstable_vertices": mechanics.unstable_vertices,
            "saddle_edges": [list(edge) for edge in mechanics.saddle_edges],
            "centroid": mechanics.centroid.tolist(),
            "min_nonzero_margin": mechanics.min_nonzero_margin,
        }
        records.append(record)
        signature = (
            tuple(record["f_vector"]),
            tuple(record["class"]),
            tuple(tuple(face) for face in record["stable_faces"]),
            tuple(record["unstable_vertices"]),
            tuple(tuple(edge) for edge in record["saddle_edges"]),
        )
        seen.setdefault(signature, record)
        if mechanics.cls == (1, 1, 0):
            print("WINNER", json.dumps(record, sort_keys=True))

    payload = {
        "source": str(SOURCE.relative_to(ROOT)),
        "shortcut_delta": args.delta,
        "shortcut_eta": args.eta,
        "actuator": moving,
        "projection_plane": list(plane),
        "range": [args.t_min, args.t_max, args.steps],
        "distinct_signatures": len(seen),
        "winner_count": sum(record.get("class") == [1, 1, 0] for record in records),
        "representatives": list(seen.values()),
        "records": records,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        "DONE", args.actuator, "evaluations", len(records),
        "signatures", len(seen), "winners", payload["winner_count"]
    )


if __name__ == "__main__":
    main()
