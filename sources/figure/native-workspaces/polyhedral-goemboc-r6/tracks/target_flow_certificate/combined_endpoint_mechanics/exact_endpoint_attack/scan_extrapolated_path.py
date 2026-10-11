#!/usr/bin/env python3
"""Locate the first actual event beyond the exact U54 material endpoint.

This is a discovery pass only.  It evaluates the already certified rational
polynomial path for t > 1, rebuilds the complete hull and own-centroid
mechanics at every sample, and stops at the first incidence or equilibrium
signature change.  The subsequent certificate builder must isolate and prove
that event exactly; sampled output is never a completion claim.
"""
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


def float_path(polynomial_path):
    return {
        label: tuple(tuple(float(value) for value in coordinate.c) for coordinate in xyz)
        for label, xyz in polynomial_path.items()
    }


def evaluate_float(coefficients, parameter):
    points = {}
    for label, xyz in coefficients.items():
        values = []
        for coordinate in xyz:
            value = 0.0
            for coefficient in reversed(coordinate):
                value = value * parameter + coefficient
            values.append(value)
        points[label] = np.asarray(values, dtype=float)
    return points


def face_signature(result):
    return tuple(sorted(tuple(sorted(face["cycle"])) for face in result.faces))


def equilibrium_signature(result):
    stable = tuple(
        sorted(tuple(sorted(result.faces[index]["cycle"])) for index, _ in result.stable)
    )
    unstable = tuple(sorted(index for index, _ in result.unstable))
    saddles = tuple(sorted(tuple(edge) for edge, _ in result.saddles))
    return stable, unstable, saddles


def snapshot(result):
    faces = face_signature(result)
    equilibria = equilibrium_signature(result)
    face_index = {
        frozenset(face["cycle"]): index for index, face in enumerate(result.faces)
    }
    quad_index = face_index.get(frozenset(exact_path.QUAD))
    edge_decisions = result.edge_decisions
    return {
        "valid": bool(result.valid),
        "error": result.error,
        "f_vector": [len(result.active), len(result.edges), len(result.faces)],
        "class": [len(result.stable), len(result.unstable), len(result.saddles)],
        "active": list(result.active),
        "inactive": sorted(set(range(265)) & (set(range(265)) - set(result.active))),
        "face_signature": [list(face) for face in faces],
        "stable_faces": [list(face) for face in equilibria[0]],
        "unstable_vertices": list(equilibria[1]),
        "saddle_edges": [list(edge) for edge in equilibria[2]],
        "topology_margin": float(result.topology_margin),
        "inactive_margin": float(result.inactive_margin),
        "base_present": exact_path.BASE in {frozenset(face) for face in faces},
        "quad_present": frozenset(exact_path.QUAD) in {frozenset(face) for face in faces},
        "u8_present": 8 in equilibria[1],
        "all_rails_present": exact_path.forced_rails().issubset(set(result.edges)),
        "selected_decisions": {
            "S_quad": (
                float(result.face_decisions[quad_index]) if quad_index is not None else None
            ),
            "U54": float(result.vertex_decisions.get(54, float("nan"))),
            "H67": float(edge_decisions.get((6, 7), float("nan"))),
            "H910": float(edge_decisions.get((9, 10), float("nan"))),
        },
    }


def compact(record):
    return {
        key: record[key]
        for key in (
            "f_vector",
            "class",
            "stable_faces",
            "unstable_vertices",
            "saddle_edges",
            "topology_margin",
            "inactive_margin",
            "base_present",
            "quad_present",
            "u8_present",
            "all_rails_present",
            "selected_decisions",
        )
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--step", type=float, default=0.001)
    parser.add_argument("--maximum", type=float, default=5.0)
    parser.add_argument("--coplanar-rel", type=float, default=2e-12)
    parser.add_argument("--output", default="extrapolated_path_scan.json")
    args = parser.parse_args()
    if not (args.step > 0 and args.maximum > 1):
        raise ValueError("require step > 0 and maximum > 1")

    _start, endpoint, polynomial_path, construction = exact_path.build_exact_path()
    coefficients = float_path(polynomial_path)
    endpoint_float = {
        label: np.asarray([float(value) for value in xyz], dtype=float)
        for label, xyz in endpoint.items()
    }
    endpoint_result = exact_path.actual.evaluate(
        endpoint_float, coplanar_rel=args.coplanar_rel
    )
    if not endpoint_result.valid:
        raise RuntimeError(endpoint_result.error)
    endpoint_snapshot = snapshot(endpoint_result)
    endpoint_faces = face_signature(endpoint_result)
    endpoint_equilibria = equilibrium_signature(endpoint_result)

    previous_parameter = 1.0
    previous_result = endpoint_result
    event = None
    samples = 0
    minimum_topology_margin = float(endpoint_result.topology_margin)
    minimum_selected = dict(endpoint_snapshot["selected_decisions"])
    parameter = 1.0 + args.step
    while parameter <= args.maximum + args.step * 0.25:
        samples += 1
        points = evaluate_float(coefficients, parameter)
        result = exact_path.actual.evaluate(points, coplanar_rel=args.coplanar_rel)
        if not result.valid:
            event = {
                "type": "evaluator_failure",
                "bracket": [previous_parameter, parameter],
                "left": compact(snapshot(previous_result)),
                "right_error": result.error,
            }
            break
        current = snapshot(result)
        minimum_topology_margin = min(minimum_topology_margin, result.topology_margin)
        for key, value in current["selected_decisions"].items():
            if value is not None and np.isfinite(value):
                minimum_selected[key] = min(minimum_selected[key], value)
        faces = face_signature(result)
        equilibria = equilibrium_signature(result)
        if faces != endpoint_faces or equilibria != endpoint_equilibria:
            previous_snapshot = snapshot(previous_result)
            event = {
                "type": (
                    "support_or_incidence"
                    if faces != endpoint_faces
                    else "mechanics_only"
                ),
                "bracket": [previous_parameter, parameter],
                "left": compact(previous_snapshot),
                "right": compact(current),
                "removed_faces": [
                    list(face) for face in sorted(set(endpoint_faces) - set(faces))
                ],
                "added_faces": [
                    list(face) for face in sorted(set(faces) - set(endpoint_faces))
                ],
            }
            break
        previous_parameter = parameter
        previous_result = result
        parameter += args.step

    payload = {
        "version": 1,
        "scope": "sampled first-event locator beyond exact U54 material endpoint",
        "discovery_only": True,
        "path_polynomial_digest": construction["path_polynomial_digest"],
        "scan": {
            "start": 1.0,
            "maximum": args.maximum,
            "step": args.step,
            "sample_count": samples,
            "minimum_topology_margin": minimum_topology_margin,
            "minimum_selected_decisions": minimum_selected,
        },
        "endpoint": compact(endpoint_snapshot),
        "first_event": event,
        "conclusion": (
            "first actual event bracketed; exact isolation required"
            if event is not None
            else "no actual event found on sampled interval"
        ),
    }
    output = HERE / args.output
    output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "endpoint": payload["endpoint"],
        "scan": payload["scan"],
        "first_event": event,
        "output": str(output),
    }, indent=2))


if __name__ == "__main__":
    main()
