#!/usr/bin/env python3
"""Audit the first non-feature-key topology wall after five circuit guards."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
from actual_hull_mechanics import evaluate  # noqa: E402
from optimize_base_escape import Search  # noqa: E402
from search_row54_remote228 import load_points, summarize  # noqa: E402


def write_csv(path, labels, points):
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(("source_id", "x", "y", "z"))
        for label, point in zip(labels, points):
            writer.writerow([label, *[format(float(x), ".17g") for x in point]])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--birth-atlas", type=Path, required=True)
    parser.add_argument("--adaptive", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--pre-csv", type=Path, required=True)
    parser.add_argument("--post-csv", type=Path, required=True)
    parser.add_argument("--offset", type=float, default=2e-6)
    args = parser.parse_args()

    labels, source = load_points(args.source)
    index = {label: offset for offset, label in enumerate(labels)}
    source_audit = json.loads(args.audit.read_text())
    rails = {
        tuple(sorted(edge))
        for edge in source_audit["fresh_hull_audit"]["forced_rail_edges"]
    }
    search = Search(labels, source, rails, report=False)
    birth_atlas = json.loads(args.birth_atlas.read_text())
    adaptive = json.loads(args.adaptive.read_text())
    remote_basis = np.asarray([
        birth_atlas["remote_basis"]["tangent"],
        birth_atlas["remote_basis"]["normal"],
    ])
    start = np.asarray(adaptive["trace"][-1]["parameters"], dtype=float)
    direction = np.asarray(adaptive["wall"]["direction"], dtype=float)
    estimate = 0.5 * (
        adaptive["wall"]["step_lo"] + adaptive["wall"]["step_hi"]
    )

    def coordinates(parameters):
        points = search.coordinates(parameters[:20])
        points[index[228]] += parameters[20] * remote_basis[0]
        points[index[228]] += parameters[21] * remote_basis[1]
        return points

    def sample(t):
        parameters = start + t * direction
        points = coordinates(parameters)
        mechanics = evaluate(labels, points)
        record = summarize(labels, points, rails)
        return parameters, points, mechanics, record

    rows = []
    offsets = (-1e-4, -2e-5, -1e-5, -2e-6, -2e-7, 0.0,
               2e-7, 2e-6, 1e-5, 2e-5, 1e-4)
    for offset in offsets:
        t = estimate + offset
        try:
            parameters, points, mechanics, record = sample(t)
            rows.append({
                "offset": offset,
                "t": t,
                "parameters": parameters.tolist(),
                "f_vector": record["f_vector"],
                "class": record["class"],
                "active_labels": record["active_labels"],
                "stable_faces": record["stable_faces"],
                "unstable_vertices": record["unstable_vertices"],
                "saddle_edges": record["saddle_edges"],
                "base_face_present": record["base_face_present"],
                "missing_forced_rails": record["missing_forced_rails"],
                "local_faces": sorted(
                    list(face) for face in mechanics.face_decisions
                    if set(face) & {7, 8, 245, 246}
                ),
                "local_edges": sorted(
                    list(edge) for edge in mechanics.edge_decisions
                    if set(edge) <= {7, 8, 245, 246}
                ),
            })
        except Exception as error:
            rows.append({"offset": offset, "t": t, "error": repr(error)})

    pre_t, post_t = estimate - args.offset, estimate + args.offset
    pre_parameters, pre_points, pre_mechanics, pre_record = sample(pre_t)
    post_parameters, post_points, post_mechanics, post_record = sample(post_t)
    write_csv(args.pre_csv, labels, pre_points)
    write_csv(args.post_csv, labels, post_points)
    pre_faces, post_faces = set(pre_mechanics.face_decisions), set(post_mechanics.face_decisions)
    pre_edges, post_edges = set(pre_mechanics.edge_decisions), set(post_mechanics.edge_decisions)
    payload = {
        "version": 1,
        "scope": "actual-hull audit around five-guard feature-key topology wall",
        "estimate": estimate,
        "wall_parameters": (start + estimate * direction).tolist(),
        "comparison_offset": args.offset,
        "pre_parameters": pre_parameters.tolist(),
        "post_parameters": post_parameters.tolist(),
        "pre_coordinates": str(args.pre_csv.resolve()),
        "post_coordinates": str(args.post_csv.resolve()),
        "pre": {
            "f_vector": pre_record["f_vector"],
            "class": pre_record["class"],
            "active_labels": pre_record["active_labels"],
            "base_face_present": pre_record["base_face_present"],
            "missing_forced_rails": pre_record["missing_forced_rails"],
        },
        "post": {
            "f_vector": post_record["f_vector"],
            "class": post_record["class"],
            "active_labels": post_record["active_labels"],
            "base_face_present": post_record["base_face_present"],
            "missing_forced_rails": post_record["missing_forced_rails"],
        },
        "topology_change": {
            "active_removed": sorted(set(pre_record["active_labels"]) - set(post_record["active_labels"])),
            "active_added": sorted(set(post_record["active_labels"]) - set(pre_record["active_labels"])),
            "faces_removed": [list(face) for face in sorted(pre_faces - post_faces)],
            "faces_added": [list(face) for face in sorted(post_faces - pre_faces)],
            "edges_removed": [list(edge) for edge in sorted(pre_edges - post_edges)],
            "edges_added": [list(edge) for edge in sorted(post_edges - pre_edges)],
        },
        "samples": rows,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
