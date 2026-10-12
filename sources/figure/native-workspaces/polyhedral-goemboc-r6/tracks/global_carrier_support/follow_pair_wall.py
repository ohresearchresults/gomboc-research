#!/usr/bin/env python3
"""Follow the nearest extra stable-face/saddle-edge wall on an actual hull.

The continuation starts from a saved base-plane search point.  A finite-
difference Jacobian of one stable-face and one saddle-edge decision supplies
minimum-norm Newton corrections.  Every accepted point is independently
rebuilt by Qhull, recentered at its own volume centroid, and required to retain
the enlarged base and every named rail.  A dense scan of each accepted segment
records the first actual combinatorial/mechanical event rather than trusting
the local linear model.
"""

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
from optimize_base_escape import CONTROLLED, Search  # noqa: E402
from search_row54_remote228 import load_points, summarize  # noqa: E402


def mechanics_pair(search: Search, parameters: np.ndarray, face, edge):
    points = search.coordinates(parameters)
    mechanics = evaluate(search.labels, points)
    if face not in mechanics.face_decisions or edge not in mechanics.edge_decisions:
        raise KeyError({
            "missing_face": face not in mechanics.face_decisions,
            "missing_edge": edge not in mechanics.edge_decisions,
        })
    return np.asarray([
        mechanics.face_decisions[face],
        mechanics.edge_decisions[edge],
    ]), mechanics, points


def finite_jacobian(search, parameters, face, edge, step):
    jacobian = np.empty((2, len(parameters)))
    for column in range(len(parameters)):
        plus = parameters.copy()
        minus = parameters.copy()
        plus[column] += step
        minus[column] -= step
        plus_value, _, _ = mechanics_pair(search, plus, face, edge)
        minus_value, _, _ = mechanics_pair(search, minus, face, edge)
        jacobian[:, column] = (plus_value - minus_value) / (2.0 * step)
    return jacobian


def signature(record):
    return {
        "class": record["class"],
        "f_vector": record["f_vector"],
        "stable_faces": record["stable_faces"],
        "unstable_vertices": record["unstable_vertices"],
        "saddle_edges": record["saddle_edges"],
        "target_violations": record["target_violations"],
        "base_face_present": record["base_face_present"],
        "missing_forced_rails": record["missing_forced_rails"],
    }


def discrete_signature(record):
    """Combinatorial/mechanical state, deliberately excluding margin values."""
    return {
        "class": record["class"],
        "f_vector": record["f_vector"],
        "stable_faces": record["stable_faces"],
        "unstable_vertices": record["unstable_vertices"],
        "saddle_edges": record["saddle_edges"],
        "base_face_present": record["base_face_present"],
        "missing_forced_rails": record["missing_forced_rails"],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--start-json", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--csv-output", type=Path, required=True)
    parser.add_argument("--face", type=int, nargs="+", default=(7, 8, 245))
    parser.add_argument("--edge", type=int, nargs=2, default=(9, 10))
    parser.add_argument("--fd-step", type=float, default=2e-5)
    parser.add_argument("--target", type=float, default=-2e-4)
    parser.add_argument("--iterations", type=int, default=12)
    parser.add_argument("--max-step", type=float, default=0.025)
    parser.add_argument("--scan-points", type=int, default=501)
    args = parser.parse_args()

    labels, source = load_points(args.source)
    audit = json.loads(args.audit.read_text())
    forced_rails = {
        tuple(sorted(edge))
        for edge in audit["fresh_hull_audit"]["forced_rail_edges"]
    }
    search = Search(labels, source, forced_rails, report=False)
    start_record = json.loads(args.start_json.read_text())
    start = np.asarray(start_record["best_parameters"], dtype=float)
    if start.shape != (2 * len(CONTROLLED),):
        raise ValueError(("bad start shape", start.shape))

    face = tuple(sorted(args.face))
    edge = tuple(sorted(args.edge))
    parameters = start.copy()
    value, _, points = mechanics_pair(search, parameters, face, edge)
    start_summary = summarize(labels, points, forced_rails)
    accepted = [{
        "iteration": 0,
        "pair_decisions": value.tolist(),
        "parameters": parameters.tolist(),
        "summary": signature(start_summary),
    }]
    dense_records = []
    first_changed = None
    baseline_signature = discrete_signature(start_summary)

    for iteration in range(1, args.iterations + 1):
        jacobian = finite_jacobian(
            search, parameters, face, edge, args.fd_step
        )
        residual = value - args.target
        gram = jacobian @ jacobian.T
        direction = -jacobian.T @ np.linalg.solve(
            gram + 1e-14 * np.eye(2), residual
        )
        norm = float(np.linalg.norm(direction))
        if norm > args.max_step:
            direction *= args.max_step / norm

        chosen = None
        for fraction in (1.0, 0.5, 0.25, 0.125, 0.0625):
            trial = parameters + fraction * direction
            try:
                trial_value, _, trial_points = mechanics_pair(
                    search, trial, face, edge
                )
                trial_summary = summarize(labels, trial_points, forced_rails)
            except Exception:
                continue
            valid = (
                trial_summary["base_face_present"]
                and not trial_summary["missing_forced_rails"]
            )
            if valid and np.linalg.norm(trial_value - args.target) < np.linalg.norm(
                value - args.target
            ):
                chosen = (fraction, trial, trial_value, trial_points, trial_summary)
                break
        if chosen is None:
            break

        fraction, trial, trial_value, trial_points, trial_summary = chosen
        for scan_index, alpha in enumerate(
            np.linspace(0.0, 1.0, args.scan_points)[1:], start=1
        ):
            scan_parameters = parameters + alpha * (trial - parameters)
            try:
                scan_points = search.coordinates(scan_parameters)
                scan_summary = summarize(labels, scan_points, forced_rails)
                scan_pair, _, _ = mechanics_pair(
                    search, scan_parameters, face, edge
                )
                row = {
                    "iteration": iteration,
                    "scan_index": scan_index,
                    "alpha": float(alpha),
                    "pair_decisions": scan_pair.tolist(),
                    "summary": signature(scan_summary),
                }
            except Exception as error:
                row = {
                    "iteration": iteration,
                    "scan_index": scan_index,
                    "alpha": float(alpha),
                    "error": repr(error),
                }
            dense_records.append(row)
            if first_changed is None and (
                "error" in row
                or discrete_signature(scan_summary) != baseline_signature
            ):
                first_changed = row

        parameters = trial
        value = trial_value
        points = trial_points
        accepted.append({
            "iteration": iteration,
            "accepted_fraction": fraction,
            "jacobian": jacobian.tolist(),
            "jacobian_singular_values": np.linalg.svd(
                jacobian, compute_uv=False
            ).tolist(),
            "step_norm": float(np.linalg.norm(fraction * direction)),
            "pair_decisions": value.tolist(),
            "parameters": parameters.tolist(),
            "summary": signature(trial_summary),
        })
        if np.all(value < 0.0):
            break

    final_summary = summarize(labels, points, forced_rails)
    with args.csv_output.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(("source_id", "x", "y", "z"))
        for label, point in zip(labels, points):
            writer.writerow([label, *[format(float(x), ".17g") for x in point]])

    payload = {
        "version": 1,
        "scope": "actual-hull own-centroid minimum-norm pair-wall continuation",
        "source": str(args.source.resolve()),
        "start_json": str(args.start_json.resolve()),
        "controlled_rows": list(CONTROLLED),
        "face": list(face),
        "edge": list(edge),
        "fd_step": args.fd_step,
        "target": args.target,
        "max_step": args.max_step,
        "scan_points_per_segment": args.scan_points,
        "start": accepted[0],
        "accepted": accepted,
        "first_signature_change": first_changed,
        "final_parameters": parameters.tolist(),
        "final_pair_decisions": value.tolist(),
        "final": final_summary,
        "final_coordinates": str(args.csv_output.resolve()),
        "dense_scan": dense_records,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "accepted_steps": len(accepted) - 1,
        "start_pair": accepted[0]["pair_decisions"],
        "final_pair": value.tolist(),
        "first_signature_change": first_changed,
        "final": signature(final_summary),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
