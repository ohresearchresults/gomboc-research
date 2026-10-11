#!/usr/bin/env python3
"""Identify and materialize the first nonlocal wall of adaptive continuation."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import brentq


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
from actual_hull_mechanics import evaluate  # noqa: E402
from optimize_base_escape import Search  # noqa: E402
from search_row54_remote228 import load_points, summarize  # noqa: E402


CIRCUIT = (8, 9, 10, 263)


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
    parser.add_argument("--atlas", type=Path, required=True)
    parser.add_argument("--adaptive", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--wall-csv", type=Path, required=True)
    parser.add_argument("--branch-csv", type=Path, required=True)
    parser.add_argument("--branch-offset", type=float, default=2e-5)
    parser.add_argument("--circuit", type=int, nargs=4, default=CIRCUIT)
    args = parser.parse_args()
    circuit = tuple(args.circuit)

    labels, source = load_points(args.source)
    index = {label: offset for offset, label in enumerate(labels)}
    source_audit = json.loads(args.audit.read_text())
    rails = {
        tuple(sorted(edge))
        for edge in source_audit["fresh_hull_audit"]["forced_rail_edges"]
    }
    search = Search(labels, source, rails, report=False)
    atlas = json.loads(args.atlas.read_text())
    adaptive = json.loads(args.adaptive.read_text())
    remote_basis = np.asarray([
        atlas["remote_basis"]["tangent"],
        atlas["remote_basis"]["normal"],
    ])
    local_controls = [
        (int(row["label"]), np.asarray(row["direction"], dtype=float))
        for row in adaptive.get("local_controls", [])
    ]
    start = np.asarray(adaptive["trace"][-1]["parameters"], dtype=float)
    direction = np.asarray(adaptive["wall"]["direction"], dtype=float)
    estimate = 0.5 * (
        adaptive["wall"]["step_lo"] + adaptive["wall"]["step_hi"]
    )

    def coordinates(parameters):
        points = search.coordinates(parameters[:20])
        points[index[228]] += parameters[20] * remote_basis[0]
        points[index[228]] += parameters[21] * remote_basis[1]
        for offset, (label, control_direction) in enumerate(local_controls):
            points[index[label]] += (
                parameters[22 + offset] * control_direction
            )
        return points

    def circuit_determinant(t):
        points = coordinates(start + t * direction)
        rows = np.c_[points[[index[label] for label in circuit]], np.ones(4)]
        return float(np.linalg.det(rows))

    width = max(args.branch_offset * 8.0, 1e-5)
    lo, hi = estimate - width, estimate + width
    while circuit_determinant(lo) * circuit_determinant(hi) > 0.0:
        width *= 2.0
        lo, hi = estimate - width, estimate + width
        if width > 0.1:
            raise ValueError("could not bracket circuit determinant")
    root = brentq(circuit_determinant, lo, hi, xtol=5e-15, rtol=1e-14)

    samples = []
    offsets = (-1e-4, -2e-5, -1e-5, -2e-6, 0.0, 2e-6, 1e-5, 2e-5, 1e-4)
    for offset in offsets:
        t = root + offset
        parameters = start + t * direction
        points = coordinates(parameters)
        mechanics = evaluate(labels, points)
        record = summarize(labels, points, rails)
        samples.append({
            "offset": offset,
            "t": t,
            "circuit_determinant": circuit_determinant(t),
            "f_vector": record["f_vector"],
            "class": record["class"],
            "stable_faces": record["stable_faces"],
            "unstable_vertices": record["unstable_vertices"],
            "saddle_edges": record["saddle_edges"],
            "base_face_present": record["base_face_present"],
            "missing_forced_rails": record["missing_forced_rails"],
            "circuit_faces_present": sorted(
                list(face) for face in mechanics.face_decisions
                if set(face) <= set(circuit) and len(face) >= 3
            ),
            "circuit_edges_present": sorted(
                list(edge) for edge in mechanics.edge_decisions
                if set(edge) <= set(circuit)
            ),
        })

    wall_parameters = start + root * direction
    wall_points = coordinates(wall_parameters)
    branch_t = root + args.branch_offset
    branch_parameters = start + branch_t * direction
    branch_points = coordinates(branch_parameters)
    branch_record = summarize(labels, branch_points, rails)
    write_csv(args.wall_csv, labels, wall_points)
    write_csv(args.branch_csv, labels, branch_points)

    pre_points = coordinates(start + (root - args.branch_offset) * direction)
    post_points = branch_points
    pre_mechanics = evaluate(labels, pre_points)
    post_mechanics = evaluate(labels, post_points)
    pre_faces, post_faces = set(pre_mechanics.face_decisions), set(post_mechanics.face_decisions)
    pre_edges, post_edges = set(pre_mechanics.edge_decisions), set(post_mechanics.edge_decisions)
    payload = {
        "version": 1,
        "scope": "actual-hull circuit audit of first adaptive nonlocal wall",
        "source": str(args.source.resolve()),
        "adaptive": str(args.adaptive.resolve()),
        "local_controls": adaptive.get("local_controls", []),
        "circuit": list(circuit),
        "circuit_determinant_root": root,
        "determinant_at_root": circuit_determinant(root),
        "root_bracket": [lo, hi],
        "branch_offset": args.branch_offset,
        "wall_parameters": wall_parameters.tolist(),
        "branch_parameters": branch_parameters.tolist(),
        "wall_coordinates": str(args.wall_csv.resolve()),
        "branch_coordinates": str(args.branch_csv.resolve()),
        "branch_audit": {
            "f_vector": branch_record["f_vector"],
            "class": branch_record["class"],
            "stable_faces": branch_record["stable_faces"],
            "unstable_vertices": branch_record["unstable_vertices"],
            "saddle_edges": branch_record["saddle_edges"],
            "base_face_present": branch_record["base_face_present"],
            "missing_forced_rails": branch_record["missing_forced_rails"],
        },
        "topology_flip": {
            "faces_removed": [list(face) for face in sorted(pre_faces - post_faces)],
            "faces_added": [list(face) for face in sorted(post_faces - pre_faces)],
            "edges_removed": [list(edge) for edge in sorted(pre_edges - post_edges)],
            "edges_added": [list(edge) for edge in sorted(post_edges - pre_edges)],
        },
        "samples": samples,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
