#!/usr/bin/env python3
"""Actual-hull scan of the remote row-228 carrier on the row-54 endpoint.

Every sample rebuilds the convex hull, recomputes its own volume centroid and
audits the complete S/U/H classification.  The enlarged base is untouched by
construction; the audit additionally requires all 37 named rail edges.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
from actual_hull_mechanics import evaluate  # noqa: E402
from search_two_actuator import row228_shortcut  # noqa: E402


DEFAULT_SOURCE = ROOT / "tracks/circuit_atlas/row54_endpoint_rebuilt.csv"
DEFAULT_AUDIT = ROOT / "tracks/circuit_atlas/row54_endpoint_rebuilt_audit.json"
DEFAULT_OUTPUT = HERE / "row54_remote228_grid.json"
BASE = frozenset(tuple(range(17)) + (54,))


def signed_log_grid(wide=False):
    values = [
        [1e-6, 1e-4, 1e-3, 2e-3, 5e-3, 1e-2, 2e-2, 5e-2,
         1e-1, 2e-1, 5e-1, 1.0, 2.0, 5.0]
    ][0]
    if wide:
        values.extend([10.0, 20.0, 50.0, 100.0, 200.0, 500.0, 1000.0])
    positive = np.asarray(values)
    return np.r_[-positive[::-1], 0.0, positive]


def load_points(path: Path):
    labels, points = [], []
    with path.open(newline="") as handle:
        for row in csv.DictReader(handle):
            labels.append(int(row["source_id"]))
            points.append([float(row[column]) for column in ("x", "y", "z")])
    return labels, np.asarray(points)


def summarize(labels, points, forced_rails):
    mechanics = evaluate(labels, points)
    stable_sets = [frozenset(face) for face in mechanics.stable_faces]
    base_key = tuple(sorted(BASE))
    base_present = base_key in mechanics.face_decisions
    stable_base = BASE in stable_sets
    edges = set(mechanics.edge_decisions)
    missing_rails = sorted(edge for edge in forced_rails if edge not in edges)

    desired_components = []
    if base_present:
        desired_components.append(("base", mechanics.face_decisions[base_key]))
    else:
        desired_components.append(("base_missing", -1.0))
    desired_components.append(("U8", mechanics.vertex_decisions.get(8, -1.0)))
    desired_components.extend(
        (f"nonstable:{list(face)}", -decision)
        for face, decision in mechanics.face_decisions.items()
        if frozenset(face) != BASE
    )
    desired_components.extend(
        (f"nonunstable:{label}", -decision)
        for label, decision in mechanics.vertex_decisions.items()
        if label != 8
    )
    desired_components.extend(
        (f"nonsaddle:{list(edge)}", -decision)
        for edge, decision in mechanics.edge_decisions.items()
    )
    if missing_rails:
        desired_components.append(("forced_rail_missing", -1.0))
    target_guard_feature, target_guard = min(desired_components, key=lambda item: item[1])
    target_violations = [
        (feature, value) for feature, value in desired_components if value <= 0.0
    ]

    return {
        "f_vector": [mechanics.vertices, mechanics.edges, mechanics.faces],
        "class": list(mechanics.cls),
        "stable_faces": [sorted(face) for face in mechanics.stable_faces],
        "unstable_vertices": mechanics.unstable_vertices,
        "saddle_edges": [list(edge) for edge in mechanics.saddle_edges],
        "centroid": mechanics.centroid.tolist(),
        "target_guard": float(target_guard),
        "target_guard_feature": target_guard_feature,
        "target_violation_count": len(target_violations),
        "target_violation_sum": float(sum(-value for _, value in target_violations)),
        "target_violations": [
            {"feature": feature, "magnitude": float(-value)}
            for feature, value in target_violations
        ],
        "base_face_present": base_present,
        "stable_base": stable_base,
        "missing_forced_rails": [list(edge) for edge in missing_rails],
        "active_labels": list(mechanics.active_labels),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--audit", type=Path, default=DEFAULT_AUDIT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--wide", action="store_true")
    args = parser.parse_args()

    labels, source = load_points(args.source)
    index = {label: offset for offset, label in enumerate(labels)}
    audit = json.loads(args.audit.read_text())
    forced_rails = {
        tuple(sorted(edge))
        for edge in audit["fresh_hull_audit"]["forced_rail_edges"]
    }
    assert len(forced_rails) == 37

    records = []
    original = summarize(labels, source, forced_rails)
    original.update({"kind": "original", "delta": None, "eta": None})
    records.append(original)

    grid = signed_log_grid(args.wide)
    for delta in grid:
        for eta in grid:
            # eta=0 is exactly coplanar with a prospective wall and is retained
            # only as a recorded Qhull boundary/error, never as a strict winner.
            try:
                candidate = row228_shortcut(source, index, float(delta), float(eta))
                record = summarize(labels, candidate, forced_rails)
                record.update({
                    "kind": "shortcut",
                    "delta": float(delta),
                    "eta": float(eta),
                })
            except Exception as error:
                record = {
                    "kind": "shortcut",
                    "delta": float(delta),
                    "eta": float(eta),
                    "error": repr(error),
                    "target_guard": -float("inf"),
                }
            records.append(record)

    valid = [record for record in records if "error" not in record]
    valid.sort(key=lambda record: record["target_guard"], reverse=True)
    winners = [
        record for record in valid
        if record["class"] == [1, 1, 0]
        and record["stable_base"]
        and not record["missing_forced_rails"]
    ]
    class_counts = Counter(tuple(record["class"]) for record in valid)
    payload = {
        "version": 1,
        "source": str(args.source.resolve()),
        "grid": grid.tolist(),
        "sample_count": len(records),
        "error_count": len(records) - len(valid),
        "winner_count": len(winners),
        "class_counts": {str(key): value for key, value in sorted(class_counts.items())},
        "best": valid[0],
        "winners": winners,
        "top_records": valid[:80],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: payload[key] for key in (
        "sample_count", "error_count", "winner_count", "class_counts", "best"
    )}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
