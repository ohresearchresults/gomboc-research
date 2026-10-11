#!/usr/bin/env python3
"""Materialize a guarded nullspace bypass of the stage-24 quad wall.

The bypass stays in the pre-flip ``(61,162,103)`` cell.  Its transverse
direction is first-order invisible to the four live defects, the U1/H(1,54)
anti-birth pair, and every previously declared circuit except the target quad
``(7,8,245,246)``.  Every saved path sample is accepted only after a fresh
convex-hull, own-centroid, and full S/U/H rebuild.
"""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))

from actual_hull_mechanics import evaluate  # noqa: E402
from optimize_base_escape import Search  # noqa: E402
from search_row54_remote228 import load_points, summarize  # noqa: E402


SOURCE = ROOT / "tracks/circuit_atlas/row54_far_rebuilt.csv"
SOURCE_AUDIT = ROOT / "tracks/circuit_atlas/row54_far_rebuilt_audit.json"
ATLAS = HERE / "local_birth_atlas.json"
STAGE24 = HERE / "adaptive_stage24_far_u54_u1h154_guarded.json"
OUT = HERE / "stage24_guarded_quad_null_bypass.json"
TARGET_QUAD = (7, 8, 245, 246)
ADVANCE_MULTIPLIER = 3.0
TRANSVERSE_AMPLITUDE = 8.5e-5
PATH_SAMPLES_PER_LEG = 101


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_csv(path: Path, labels, points) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(("source_id", "x", "y", "z"))
        for label, point in zip(labels, points):
            writer.writerow([label, *[format(float(x), ".17g") for x in point]])


def main() -> None:
    stage = json.loads(STAGE24.read_text())
    labels, source = load_points(SOURCE)
    index = {label: offset for offset, label in enumerate(labels)}
    audit = json.loads(SOURCE_AUDIT.read_text())
    rails = {
        tuple(sorted(edge))
        for edge in audit["fresh_hull_audit"]["forced_rail_edges"]
    }
    search = Search(labels, source, rails, report=False)
    atlas = json.loads(ATLAS.read_text())
    remote_basis = np.asarray(
        [atlas["remote_basis"]["tangent"], atlas["remote_basis"]["normal"]]
    )
    local_controls = [
        (int(row["label"]), np.asarray(row["direction"], dtype=float))
        for row in stage["local_controls"]
    ]

    def coordinates(parameters):
        points = search.coordinates(parameters[:20])
        points[index[228]] += parameters[20] * remote_basis[0]
        points[index[228]] += parameters[21] * remote_basis[1]
        for offset, (label, direction) in enumerate(local_controls):
            points[index[label]] += parameters[22 + offset] * direction
        return points

    def determinant(parameters, quad):
        points = coordinates(parameters)
        rows = np.c_[points[[index[label] for label in quad]], np.ones(4)]
        return float(np.linalg.det(rows))

    def decisions(parameters):
        mechanics = evaluate(labels, coordinates(parameters))
        values = np.asarray(
            [
                mechanics.face_decisions[(7, 8, 245)],
                mechanics.vertex_decisions[54],
                mechanics.edge_decisions[(5, 6)],
                mechanics.edge_decisions[(9, 10)],
                mechanics.vertex_decisions[1],
                mechanics.edge_decisions[(1, 54)],
            ]
        )
        return values, mechanics

    start = np.asarray(stage["trace"][-1]["parameters"], dtype=float)
    forward = np.asarray(stage["wall"]["direction"], dtype=float)
    wall_step = 0.5 * (stage["wall"]["step_lo"] + stage["wall"]["step_hi"])
    initial_values, initial_mechanics = decisions(start)
    initial_faces = set(initial_mechanics.face_decisions)

    circuit_specs = [
        (tuple(row["circuit"]), int(row["valid_sign"]))
        for row in stage["circuit_guards"]
    ]
    frozen_circuits = [
        quad for quad, _ in circuit_specs if quad != TARGET_QUAD
    ]
    parameter_count = len(start)
    mechanics_jacobian = np.empty((6, parameter_count))
    circuit_jacobian = np.empty((len(frozen_circuits), parameter_count))
    target_gradient = np.empty(parameter_count)
    for column in range(parameter_count):
        epsilon = 1e-8 if column < 22 else 1e-10
        step = np.zeros(parameter_count)
        step[column] = epsilon
        mechanics_jacobian[:, column] = (
            decisions(start + step)[0] - decisions(start - step)[0]
        ) / (2.0 * epsilon)
        target_gradient[column] = (
            determinant(start + step, TARGET_QUAD)
            - determinant(start - step, TARGET_QUAD)
        ) / (2.0 * epsilon)
        for row, quad in enumerate(frozen_circuits):
            circuit_jacobian[row, column] = (
                determinant(start + step, quad)
                - determinant(start - step, quad)
            ) / (2.0 * epsilon)

    frozen_jacobian = np.vstack((mechanics_jacobian, circuit_jacobian))
    _, singular_values, vt = np.linalg.svd(frozen_jacobian, full_matrices=True)
    rank = int(np.linalg.matrix_rank(frozen_jacobian))
    null_basis = vt[rank:].T
    transverse = null_basis @ (null_basis.T @ target_gradient)
    transverse /= np.max(np.abs(transverse))
    if float(target_gradient @ transverse) < 0.0:
        transverse = -transverse

    buffered = start + TRANSVERSE_AMPLITUDE * transverse
    endpoint = (
        start
        + ADVANCE_MULTIPLIER * wall_step * forward
        + TRANSVERSE_AMPLITUDE * transverse
    )

    path = []
    failures = []
    minimum_target_determinant = float("inf")
    minimum_topology_margin = float("inf")
    minimum_u1_guard = float("inf")
    minimum_h154_guard = float("inf")
    maximum_live_ratio = np.full(4, -float("inf"))
    for leg, first, second in (
        ("start_to_buffer", start, buffered),
        ("buffer_to_endpoint", buffered, endpoint),
    ):
        for offset, t in enumerate(np.linspace(0.0, 1.0, PATH_SAMPLES_PER_LEG)):
            if leg == "buffer_to_endpoint" and offset == 0:
                continue
            parameters = (1.0 - t) * first + t * second
            values, mechanics = decisions(parameters)
            points = coordinates(parameters)
            record = summarize(labels, points, rails)
            signed_circuits = {
                str(list(quad)): sign * determinant(parameters, quad)
                for quad, sign in circuit_specs
            }
            valid = bool(
                mechanics.cls == (2, 2, 2)
                and (mechanics.vertices, mechanics.edges, mechanics.faces)
                == (61, 162, 103)
                and set(mechanics.face_decisions) == initial_faces
                and record["base_face_present"]
                and not record["missing_forced_rails"]
                and min(signed_circuits.values()) > 0.0
                and values[4] < 0.0
                and values[5] < 0.0
            )
            if not valid:
                failures.append({"leg": leg, "offset": offset, "t": float(t)})
            live_ratios = values[:4] / initial_values[:4]
            maximum_live_ratio = np.maximum(maximum_live_ratio, live_ratios)
            minimum_target_determinant = min(
                minimum_target_determinant,
                determinant(parameters, TARGET_QUAD),
            )
            minimum_topology_margin = min(
                minimum_topology_margin, mechanics.min_nonzero_margin
            )
            minimum_u1_guard = min(minimum_u1_guard, -values[4])
            minimum_h154_guard = min(minimum_h154_guard, -values[5])
            path.append(
                {
                    "leg": leg,
                    "offset": offset,
                    "t": float(t),
                    "feature_values": values.tolist(),
                    "live_ratios": live_ratios.tolist(),
                    "target_quad_determinant": determinant(parameters, TARGET_QUAD),
                    "minimum_signed_circuit": min(signed_circuits.values()),
                    "topology_margin": mechanics.min_nonzero_margin,
                }
            )

    if failures:
        raise AssertionError(failures[:3])
    endpoint_values, endpoint_mechanics = decisions(endpoint)
    endpoint_points = coordinates(endpoint)
    endpoint_record = summarize(labels, endpoint_points, rails)
    endpoint_csv = OUT.with_name(OUT.stem + "_endpoint.csv")
    buffered_csv = OUT.with_name(OUT.stem + "_buffered.csv")
    write_csv(endpoint_csv, labels, endpoint_points)
    write_csv(buffered_csv, labels, coordinates(buffered))
    face_path = OUT.with_name(OUT.stem + "_endpoint_faces.json")
    face_path.write_text(
        json.dumps([list(face) for face in sorted(endpoint_mechanics.face_decisions)], indent=2)
        + "\n"
    )

    payload = {
        "version": 1,
        "verdict": "FRESH_HULL_GUARDED_STAGE24_QUAD_NULL_BYPASS_PASS",
        "source_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (SOURCE, SOURCE_AUDIT, ATLAS, STAGE24)
        },
        "target_quad": list(TARGET_QUAD),
        "frozen_feature_order": ["S(7,8,245)", "U54", "H(5,6)", "H(9,10)", "U1", "H(1,54)"],
        "frozen_circuits": [list(quad) for quad in frozen_circuits],
        "jacobian_singular_values": singular_values.tolist(),
        "jacobian_rank": rank,
        "nullspace_dimension": int(null_basis.shape[1]),
        "transverse_direction": transverse.tolist(),
        "maximum_feature_derivative_leak": float(
            np.max(np.abs(mechanics_jacobian @ transverse))
        ),
        "maximum_frozen_circuit_derivative_leak": float(
            np.max(np.abs(circuit_jacobian @ transverse))
        ),
        "target_determinant_derivative": float(target_gradient @ transverse),
        "wall_step": wall_step,
        "advance_multiplier": ADVANCE_MULTIPLIER,
        "transverse_amplitude": TRANSVERSE_AMPLITUDE,
        "start_parameters": start.tolist(),
        "buffered_parameters": buffered.tolist(),
        "endpoint_parameters": endpoint.tolist(),
        "initial_feature_values": initial_values.tolist(),
        "endpoint_feature_values": endpoint_values.tolist(),
        "endpoint_live_ratios": (endpoint_values[:4] / initial_values[:4]).tolist(),
        "path_sample_count": len(path),
        "path_all_valid": True,
        "path_minimum_target_determinant": minimum_target_determinant,
        "path_minimum_topology_margin": minimum_topology_margin,
        "path_minimum_u1_guard": minimum_u1_guard,
        "path_minimum_h154_guard": minimum_h154_guard,
        "path_maximum_live_ratio": maximum_live_ratio.tolist(),
        "endpoint": {
            "f_vector": endpoint_record["f_vector"],
            "class": endpoint_record["class"],
            "base_face_present": endpoint_record["base_face_present"],
            "missing_forced_rails": endpoint_record["missing_forced_rails"],
            "stable_faces": endpoint_record["stable_faces"],
            "unstable_vertices": endpoint_record["unstable_vertices"],
            "saddle_edges": endpoint_record["saddle_edges"],
            "coordinates": str(endpoint_csv.relative_to(ROOT)),
            "face_ledger": str(face_path.relative_to(ROOT)),
        },
        "path": path,
    }
    OUT.write_text(json.dumps(payload, indent=2) + "\n")
    print("FRESH_HULL_GUARDED_STAGE24_QUAD_NULL_BYPASS_PASS")


if __name__ == "__main__":
    main()
