#!/usr/bin/env python3
"""Enumerate the smallest active point/triangle support slacks at one source."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

import post_flip_trust_slp as engine


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--plane-tol", type=float, default=1e-11)
    parser.add_argument("--limit", type=int, default=64)
    parser.add_argument("--output")
    args = parser.parse_args()

    source = Path(args.source).resolve()
    if args.limit <= 0:
        raise ValueError("limit must be positive")
    points = engine.load_exact_float(source)
    result, _values, _faces, _equilibria = engine.state(points, args.plane_tol)
    radius = float(np.sqrt(np.mean([
        np.dot(point - result.centroid, point - result.centroid)
        for point in points.values()
    ])))
    if not np.isfinite(radius) or radius <= 0:
        raise ValueError("invalid RMS radius")

    records = {}
    for face in result.faces:
        cycle = tuple(int(label) for label in face["cycle"])
        if len(cycle) != 3:
            continue
        for vertex in result.active:
            vertex = int(vertex)
            if vertex in cycle:
                continue
            slack = -(
                float(np.dot(points[vertex], face["n"])) + float(face["off"])
            ) / radius
            if not np.isfinite(slack) or slack <= 0:
                raise ValueError(("nonstrict active point/face slack", cycle, vertex, slack))
            circuit = tuple(sorted(cycle + (vertex,)))
            record = records.setdefault(circuit, {
                "circuit": list(circuit),
                "minimum_normalized_support_slack": slack,
                "representatives": [],
            })
            record["minimum_normalized_support_slack"] = min(
                record["minimum_normalized_support_slack"], slack
            )
            record["representatives"].append({
                "face": list(cycle),
                "vertex": vertex,
                "normalized_support_slack": slack,
            })

    ordered = sorted(
        records.values(),
        key=lambda row: (row["minimum_normalized_support_slack"], row["circuit"]),
    )
    for record in ordered:
        circuit = tuple(record["circuit"])
        record["sorted_orientation_determinant"] = (
            engine.topology_guard_determinants(points, (circuit,))[circuit]
        )

    payload = {
        "schema": "polyhedral-goemboc.topology-guard-audit",
        "version": 1,
        "source": str(source),
        "source_sha256": sha256(source),
        "plane_tolerance": args.plane_tol,
        "source_f_vector": [
            len(result.active), len(result.edges), len(result.faces)
        ],
        "source_class": [
            len(result.stable), len(result.unstable), len(result.saddles)
        ],
        "all_37_forced_rails_retained": engine.forced_rails_retained(result),
        "unique_triangle_point_circuit_count": len(ordered),
        "reported_count": min(args.limit, len(ordered)),
        "circuits": ordered[: args.limit],
        "verdict": "READ_ONLY_NEAR_TOPOLOGY_CIRCUIT_AUDIT_PASS",
    }
    text = json.dumps(payload, indent=2) + "\n"
    if args.output:
        output = Path(args.output)
        output.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
