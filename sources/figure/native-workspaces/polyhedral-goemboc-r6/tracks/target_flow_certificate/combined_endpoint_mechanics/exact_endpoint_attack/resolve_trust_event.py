#!/usr/bin/env python3
"""Resolve the post-flip trust-SLP evaluator band into adjacent hull cells."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
sys.path.insert(0, str(PARENT))

import build_u54_material_exact_path as exact_path  # noqa: E402
import combined_four_death_lp as four  # noqa: E402
from integrate_four_death_direction import write_csv  # noqa: E402
from predictor_bypass_epoch import candidate_circuits  # noqa: E402


REPORT = HERE / "post_flip_trust_pass2_slp.json"
SOURCE = HERE / "post_flip_trust_pass2_step_003.csv"


def apply_direction(points, direction, fraction):
    return {
        label: np.asarray(points[label], dtype=float) + fraction * direction[label]
        for label in points
    }


def faces(result):
    return tuple(sorted(tuple(sorted(face["cycle"])) for face in result.faces))


def snapshot(result):
    return {
        "valid": bool(result.valid),
        "error": result.error,
        "f_vector": [len(result.active), len(result.edges), len(result.faces)],
        "class": [len(result.stable), len(result.unstable), len(result.saddles)],
        "active": list(result.active),
        "stable": [
            sorted(result.faces[index]["cycle"]) for index, _ in result.stable
        ],
        "unstable": [index for index, _ in result.unstable],
        "saddles": [list(edge) for edge, _ in result.saddles],
        "topology_margin": float(result.topology_margin),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", default=str(REPORT))
    parser.add_argument("--source", default=str(SOURCE))
    parser.add_argument("--prefix", default="post_flip_trust")
    parser.add_argument("--coplanar-rel", type=float, default=2e-12)
    args = parser.parse_args()
    report_path = Path(args.report)
    source_path = Path(args.source)
    if not report_path.is_absolute():
        report_path = HERE / report_path
    if not source_path.is_absolute():
        source_path = HERE / source_path
    report = json.loads(report_path.read_text())
    event_row = report["history"][-1]
    bracket = event_row["first_event"]["fraction_bracket"]
    centre = sum(bracket) / 2.0
    points = four.load_points(source_path)
    before_points = four.load_points(HERE / event_row["first_event"]["before_file"])
    left_fraction = bracket[0]
    direction = {
        label: (before_points[label] - points[label]) / left_fraction
        for label in points
    }
    baseline = exact_path.actual.evaluate(points, coplanar_rel=args.coplanar_rel)
    if not baseline.valid:
        raise RuntimeError(baseline.error)
    baseline_faces = faces(baseline)

    offsets = (
        -1e-4, -1e-5, -1e-6, -1e-7, -1e-8, 0.0,
        1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 5e-1,
    )
    probes = []
    post = None
    for offset in offsets:
        fraction = centre + offset
        candidate = apply_direction(points, direction, fraction)
        result = exact_path.actual.evaluate(candidate, coplanar_rel=args.coplanar_rel)
        record = {
            "offset": offset,
            "fraction": fraction,
            "snapshot": snapshot(result),
        }
        if result.valid:
            signature = faces(result)
            record["removed_faces"] = [
                list(face) for face in sorted(set(baseline_faces) - set(signature))
            ]
            record["added_faces"] = [
                list(face) for face in sorted(set(signature) - set(baseline_faces))
            ]
            record["candidate_circuits"] = [
                list(circuit)
                for circuit in candidate_circuits(
                    {frozenset(face) for face in baseline_faces},
                    {frozenset(face) for face in signature},
                )
            ] if signature != baseline_faces else []
            if offset > 0 and signature != baseline_faces and post is None:
                post = (fraction, candidate, result, record)
        probes.append(record)

    if post is None:
        output = HERE / f"{args.prefix}_resolved_event.json"
        output.write_text(json.dumps({
            "version": 1,
            "scope": "unresolved physical-trust evaluator band",
            "source": source_path.name,
            "fraction_bracket": bracket,
            "fraction_centre": centre,
            "probes": probes,
            "conclusion": "no valid changed post-cell found in probe range",
        }, indent=2) + "\n")
        raise RuntimeError("no valid changed post-cell found in probe range")
    fraction, post_points, post_result, post_record = post
    post_file = HERE / f"{args.prefix}_event_resolved_post.csv"
    write_csv(post_file, post_points)
    payload = {
        "version": 1,
        "scope": "resolution of first physical-trust event after exact support flip",
        "source": source_path.name,
        "fraction_bracket": bracket,
        "fraction_centre": centre,
        "probes": probes,
        "first_valid_changed_post": {
            **post_record,
            "file": post_file.name,
        },
        "conclusion": "adjacent post-cell identified; exact wall isolation remains required",
    }
    output = HERE / f"{args.prefix}_resolved_event.json"
    output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "baseline": snapshot(baseline),
        "post": payload["first_valid_changed_post"],
        "output": str(output),
    }, indent=2))


if __name__ == "__main__":
    main()
