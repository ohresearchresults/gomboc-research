#!/usr/bin/env python3
"""Nullspace atlas and L-bypass of a linked S/H birth wall."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from actual_hull_mechanics import evaluate  # noqa: E402
from optimize_base_escape import Search  # noqa: E402
from search_row54_remote228 import load_points, summarize  # noqa: E402


DEFAULT_BIRTH_FACE = (8, 245, 246)
DEFAULT_BIRTH_EDGE = (8, 245)
KEEP_INDEX = (0, 2, 3, 5)
BIRTH_INDEX = (1, 4)


def values(
    mechanics, birth_face, birth_edge, guard_birth_faces=(), guard_birth_edges=()
):
    result = [
        mechanics.face_decisions[(7, 8, 245)],
        mechanics.face_decisions[birth_face],
        mechanics.vertex_decisions[54],
        mechanics.edge_decisions[(6, 7)],
        mechanics.edge_decisions[birth_edge],
        mechanics.edge_decisions[(9, 10)],
    ]
    result.extend(mechanics.face_decisions[face] for face in guard_birth_faces)
    result.extend(mechanics.edge_decisions[edge] for edge in guard_birth_edges)
    return np.asarray(result)


def compact(record):
    return {
        "class": record["class"],
        "f_vector": record["f_vector"],
        "stable_faces": sorted(sorted(face) for face in record["stable_faces"]),
        "unstable_vertices": sorted(record["unstable_vertices"]),
        "saddle_edges": sorted(sorted(edge) for edge in record["saddle_edges"]),
        "centroid": record["centroid"],
        "base_face_present": record["base_face_present"],
        "missing_forced_rails": record["missing_forced_rails"],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--birth-atlas", type=Path, required=True)
    parser.add_argument("--adaptive", type=Path, required=True)
    parser.add_argument("--certificate", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--fd-step", type=float, default=1e-7)
    parser.add_argument("--radius", type=float, default=3e-4)
    parser.add_argument("--quadrant-radius", type=float, default=1e-5)
    parser.add_argument("--path-points", type=int, default=61)
    parser.add_argument(
        "--birth-face", type=int, nargs=3, default=DEFAULT_BIRTH_FACE,
        metavar=("A", "B", "C"),
    )
    parser.add_argument(
        "--birth-edge", type=int, nargs=2, default=DEFAULT_BIRTH_EDGE,
        metavar=("A", "B"),
    )
    parser.add_argument(
        "--guard-birth-face", type=int, nargs=3, action="append", default=[],
        metavar=("A", "B", "C"),
    )
    parser.add_argument(
        "--guard-birth-edge", type=int, nargs=2, action="append", default=[],
        metavar=("A", "B"),
    )
    parser.add_argument("--guard-birth-tangent-band", type=float, default=1e-3)
    args = parser.parse_args()
    birth_face = tuple(args.birth_face)
    birth_edge = tuple(args.birth_edge)
    if not set(birth_edge) <= set(birth_face):
        raise ValueError(("birth edge must lie in birth face", birth_edge, birth_face))
    guard_birth_faces = [tuple(row) for row in args.guard_birth_face]
    guard_birth_edges = [tuple(row) for row in args.guard_birth_edge]
    feature_names = (
        "S(7,8,245)",
        "S(" + ",".join(map(str, birth_face)) + ")",
        "U54",
        "H(6,7)",
        "H(" + ",".join(map(str, birth_edge)) + ")",
        "H(9,10)",
    )
    feature_names = list(feature_names)
    feature_names.extend(
        "S(" + ",".join(map(str, face)) + ")"
        for face in guard_birth_faces
    )
    feature_names.extend(
        "H(" + ",".join(map(str, edge)) + ")"
        for edge in guard_birth_edges
    )
    birth_index = list(BIRTH_INDEX) + list(range(6, len(feature_names)))

    labels, source = load_points(args.source)
    index = {label: offset for offset, label in enumerate(labels)}
    source_audit = json.loads(args.audit.read_text())
    rails = {
        tuple(sorted(edge))
        for edge in source_audit["fresh_hull_audit"]["forced_rail_edges"]
    }
    birth_atlas = json.loads(args.birth_atlas.read_text())
    adaptive = json.loads(args.adaptive.read_text())
    certificate = json.loads(args.certificate.read_text())
    search = Search(labels, source, rails, report=False)
    remote_basis = np.asarray([
        birth_atlas["remote_basis"]["tangent"],
        birth_atlas["remote_basis"]["normal"],
    ])
    controls = [
        (int(row["label"]), np.asarray(row["direction"], dtype=float))
        for row in adaptive.get("local_controls", [])
    ]

    def coordinates(parameters):
        points = search.coordinates(parameters[:20])
        points[index[228]] += parameters[20] * remote_basis[0]
        points[index[228]] += parameters[21] * remote_basis[1]
        for offset, (label, direction) in enumerate(controls):
            points[index[label]] += parameters[22 + offset] * direction
        return points

    circuit_specs = [
        (tuple(row["circuit"]), int(row["valid_sign"]))
        for row in adaptive["circuit_guards"]
    ]

    def circuit_values(points):
        return np.asarray([
            np.linalg.det(np.c_[
                points[[index[label] for label in circuit]], np.ones(4)
            ])
            for circuit, _ in circuit_specs
        ])

    def sample(parameters):
        points = coordinates(parameters)
        mechanics = evaluate(labels, points)
        record = summarize(labels, points, rails)
        return (
            values(
                mechanics, birth_face, birth_edge,
                guard_birth_faces, guard_birth_edges,
            ),
            record,
            circuit_values(points),
        )

    start = np.asarray(adaptive["trace"][-1]["parameters"], dtype=float)
    wall_direction = np.asarray(adaptive["wall"]["direction"], dtype=float)
    root = float(certificate["root_float"])
    star = start + root * wall_direction
    direction_x = wall_direction / np.linalg.norm(wall_direction)
    star_values, star_record, star_circuits = sample(star)

    jacobian = np.empty((len(feature_names), len(star)))
    circuit_jacobian = np.empty((len(circuit_specs), len(star)))
    for column in range(len(star)):
        plus = star.copy()
        minus = star.copy()
        plus[column] += args.fd_step
        minus[column] -= args.fd_step
        plus_values, _, plus_circuits = sample(plus)
        minus_values, _, minus_circuits = sample(minus)
        jacobian[:, column] = (
            plus_values - minus_values
        ) / (2 * args.fd_step)
        circuit_jacobian[:, column] = (
            plus_circuits - minus_circuits
        ) / (2 * args.fd_step)

    keep_jacobian = jacobian[list(KEEP_INDEX)]
    _, singular_values, vt = np.linalg.svd(keep_jacobian, full_matrices=True)
    tolerance = max(keep_jacobian.shape) * np.finfo(float).eps * singular_values[0]
    rank = int(np.sum(singular_values > tolerance))
    null_basis = vt[rank:].T

    all_birth_rows = jacobian[birth_index]
    active_birth_mask = star_values[birth_index] >= -args.guard_birth_tangent_band
    birth_rows = all_birth_rows[active_birth_mask]
    if len(birth_rows) < 2:
        raise ValueError(("fewer than the selected linked pair active", active_birth_mask))
    normalized_birth_rows = (
        birth_rows / np.linalg.norm(birth_rows, axis=1)[:, None]
    )
    combined_birth_gradient = normalized_birth_rows.mean(axis=0)
    projected = null_basis @ (null_basis.T @ combined_birth_gradient)
    projected_norm = float(np.linalg.norm(projected))
    if projected_norm <= 1e-12:
        raise ValueError(("birth gradient trapped in keep rowspace", projected_norm))
    direction_y_unit = -projected / projected_norm
    rate_x = float(combined_birth_gradient @ direction_x)
    rate_y_unit = float(combined_birth_gradient @ direction_y_unit)
    direction_y_scale = 2.0 * abs(rate_x) / max(abs(rate_y_unit), 1e-300)
    direction_y = direction_y_scale * direction_y_unit
    if combined_birth_gradient @ direction_y > 0.0:
        direction_y *= -1.0

    def record(parameters, name):
        feature_values, hull_record, circuits = sample(parameters)
        signed_circuits = np.asarray([
            sign * value
            for (_, sign), value in zip(circuit_specs, circuits)
        ])
        return {
            "name": name,
            "parameters": parameters.tolist(),
            "feature_values": dict(zip(feature_names, feature_values.tolist())),
            "circuit_determinants": {
                str(list(circuit)): float(value)
                for (circuit, _), value in zip(circuit_specs, circuits)
            },
            "minimum_signed_circuit": float(np.min(signed_circuits)),
            "summary": compact(hull_record),
            "hard_valid": bool(
                hull_record["base_face_present"]
                and not hull_record["missing_forced_rails"]
                and np.all(signed_circuits > 0.0)
            ),
        }

    quadrants = []
    for sx in (-1, 1):
        for sy in (-1, 1):
            parameters = star + args.quadrant_radius * (
                sx * direction_x + sy * direction_y
            )
            try:
                quadrants.append(record(parameters, f"quadrant:{sx},{sy}"))
            except Exception as error:
                quadrants.append({
                    "name": f"quadrant:{sx},{sy}",
                    "parameters": parameters.tolist(),
                    "error": repr(error),
                    "hard_valid": False,
                })

    waypoints = (
        star - args.radius * direction_x,
        star - args.radius * direction_x + args.radius * direction_y,
        star + args.radius * direction_x + args.radius * direction_y,
    )
    path = []
    for segment, (left, right) in enumerate(zip(waypoints, waypoints[1:])):
        for offset, alpha in enumerate(np.linspace(0.0, 1.0, args.path_points)):
            if segment and offset == 0:
                continue
            row = record(
                left + alpha * (right - left),
                f"segment:{segment}:alpha:{alpha:.17g}",
            )
            row["segment"] = segment
            row["alpha"] = float(alpha)
            path.append(row)

    baseline, endpoint = path[0], path[-1]
    start_keep = np.asarray([
        baseline["feature_values"][feature_names[index]] for index in KEEP_INDEX
    ])
    end_keep = np.asarray([
        endpoint["feature_values"][feature_names[index]] for index in KEEP_INDEX
    ])
    avoided_birth = all(
        all(row["feature_values"][feature_names[index]] < 0.0 for index in birth_index)
        for row in path
    )
    expected_signature = baseline["summary"]
    same_mechanics = all(
        row["summary"]["class"] == expected_signature["class"]
        and row["summary"]["f_vector"] == expected_signature["f_vector"]
        and row["summary"]["stable_faces"] == expected_signature["stable_faces"]
        and row["summary"]["unstable_vertices"] == expected_signature["unstable_vertices"]
        and row["summary"]["saddle_edges"] == expected_signature["saddle_edges"]
        for row in path
    )
    bypass = bool(
        rank == 4
        and projected_norm > 1e-12
        and all(row["hard_valid"] for row in path)
        and avoided_birth
        and same_mechanics
        and np.all(end_keep < start_keep)
    )
    assert bypass

    rowspace_coefficients, *_ = np.linalg.lstsq(
        keep_jacobian.T, combined_birth_gradient, rcond=None
    )
    rowspace_residual = (
        combined_birth_gradient - keep_jacobian.T @ rowspace_coefficients
    )
    first_circuit, first_sign = circuit_specs[0]
    payload = {
        "version": 1,
        "scope": "local nullspace atlas around an exact linked S/H birth",
        "source": str(args.source.resolve()),
        "adaptive": str(args.adaptive.resolve()),
        "certificate": str(args.certificate.resolve()),
        # These compatibility fields let adaptive_birth_bypass use this file
        # as its next chart endpoint and retain the stage-6 branch guard.
        "circuit": list(first_circuit),
        "valid_sign": first_sign,
        "local_controls": adaptive.get("local_controls", []),
        "root": root,
        "star_parameters": star.tolist(),
        "fd_step": args.fd_step,
        "radius": args.radius,
        "quadrant_radius": args.quadrant_radius,
        "features": list(feature_names),
        "birth_face": list(birth_face),
        "birth_edge": list(birth_edge),
        "guard_birth_faces": [list(face) for face in guard_birth_faces],
        "guard_birth_edges": [list(edge) for edge in guard_birth_edges],
        "guard_birth_tangent_band": args.guard_birth_tangent_band,
        "active_birth_features": [
            feature_names[index]
            for index, active in zip(birth_index, active_birth_mask)
            if active
        ],
        "keep_rank": rank,
        "nullity": len(star) - rank,
        "keep_singular_values": singular_values.tolist(),
        "birth_gradient_cosine": float(
            normalized_birth_rows[0] @ normalized_birth_rows[1]
        ),
        "nullspace_antibirth_projection_norm": projected_norm,
        "rowspace_blocker": {
            "coefficients": rowspace_coefficients.tolist(),
            "residual_norm": float(np.linalg.norm(rowspace_residual)),
        },
        "direction_x": direction_x.tolist(),
        "direction_y": direction_y.tolist(),
        "direction_y_unit": direction_y_unit.tolist(),
        "direction_y_scale": direction_y_scale,
        "feature_derivative_x": (jacobian @ direction_x).tolist(),
        "feature_derivative_y": (jacobian @ direction_y).tolist(),
        "signed_circuit_derivative_x": [
            float(sign * row @ direction_x)
            for row, (_, sign) in zip(circuit_jacobian, circuit_specs)
        ],
        "signed_circuit_derivative_y": [
            float(sign * row @ direction_y)
            for row, (_, sign) in zip(circuit_jacobian, circuit_specs)
        ],
        "star_feature_values": dict(zip(feature_names, star_values.tolist())),
        "star_summary": compact(star_record),
        "star_circuit_determinants": {
            str(list(circuit)): float(value)
            for (circuit, _), value in zip(circuit_specs, star_circuits)
        },
        "quadrants": quadrants,
        "bypass_waypoints": [row.tolist() for row in waypoints],
        "bypass_path": path,
        "bypass_audit": {
            "bypass_found": bypass,
            "all_hard_valid": all(row["hard_valid"] for row in path),
            "linked_birth_absent": avoided_birth,
            "same_mechanics": same_mechanics,
            "all_keep_decisions_decreased": bool(np.all(end_keep < start_keep)),
            "start_keep_values": start_keep.tolist(),
            "end_keep_values": end_keep.tolist(),
            "end_to_start_keep_ratios": (end_keep / start_keep).tolist(),
        },
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "bypass_audit": payload["bypass_audit"],
        "keep_rank": rank,
        "nullity": payload["nullity"],
        "birth_gradient_cosine": payload["birth_gradient_cosine"],
        "nullspace_antibirth_projection_norm": projected_norm,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
