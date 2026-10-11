#!/usr/bin/env python3
"""Two-dimensional tangent atlas around the hard (8,9,10,263) base wall."""

from __future__ import annotations

import argparse
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


CIRCUIT = (8, 9, 10, 263)
FEATURES = ("S(7,8,245)", "U54", "H(6,7)", "H(9,10)")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--birth-atlas", type=Path, required=True)
    parser.add_argument("--adaptive", type=Path, required=True)
    parser.add_argument("--wall-audit", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--fd-step", type=float, default=1e-6)
    parser.add_argument("--linearization-offset", type=float, default=2e-5)
    parser.add_argument("--radius", type=float, default=1e-5)
    parser.add_argument("--path-points", type=int, default=41)
    parser.add_argument(
        "--bypass-factor", type=float, default=2.0,
        help="signed-circuit y correction relative to the x crossing rate",
    )
    parser.add_argument("--circuit", type=int, nargs=4, default=CIRCUIT)
    parser.add_argument("--valid-sign", type=int, choices=(-1, 1), default=-1)
    parser.add_argument(
        "--guard-birth-face", type=int, nargs=3, action="append", default=[],
        metavar=("A", "B", "C"),
    )
    parser.add_argument(
        "--guard-birth-edge", type=int, nargs=2, action="append", default=[],
        metavar=("A", "B"),
    )
    args = parser.parse_args()
    circuit_labels = tuple(args.circuit)
    guard_birth_faces = [tuple(row) for row in args.guard_birth_face]
    guard_birth_edges = [tuple(row) for row in args.guard_birth_edge]

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
    wall_audit = json.loads(args.wall_audit.read_text())
    remote_basis = np.asarray([
        birth_atlas["remote_basis"]["tangent"],
        birth_atlas["remote_basis"]["normal"],
    ])
    local_controls = [
        (int(row["label"]), np.asarray(row["direction"], dtype=float))
        for row in adaptive.get("local_controls", [])
    ]
    if "wall_parameters" in wall_audit:
        star = np.asarray(wall_audit["wall_parameters"], dtype=float)
    elif wall_audit.get("wall", {}).get("pre_parameters") is not None:
        wall = wall_audit["wall"]
        pre = np.asarray(wall["pre_parameters"], dtype=float)
        post = np.asarray(wall.get("post_parameters", pre), dtype=float)
        star = (pre + post) / 2.0
    else:
        raise KeyError("wall_parameters or wall.pre_parameters")
    direction_x = np.asarray(adaptive["wall"]["direction"], dtype=float)
    direction_x /= np.linalg.norm(direction_x)

    def coordinates(parameters):
        points = search.coordinates(parameters[:20])
        points[index[228]] += parameters[20] * remote_basis[0]
        points[index[228]] += parameters[21] * remote_basis[1]
        for offset, (label, control_direction) in enumerate(local_controls):
            points[index[label]] += (
                parameters[22 + offset] * control_direction
            )
        return points

    def circuit_value(points):
        rows = np.c_[points[[index[label] for label in circuit_labels]], np.ones(4)]
        return float(np.linalg.det(rows))

    inherited_circuit_specs = [
        (tuple(row["circuit"]), int(row["valid_sign"]))
        for row in adaptive.get("circuit_guards", [])
    ]

    def inherited_circuit_values(points):
        return np.asarray([
            sign * np.linalg.det(np.c_[
                points[[index[label] for label in circuit]], np.ones(4)
            ])
            for circuit, sign in inherited_circuit_specs
        ])

    def values(points, mechanics):
        return np.asarray([
            mechanics.face_decisions[(7, 8, 245)],
            mechanics.vertex_decisions[54],
            mechanics.edge_decisions[(6, 7)],
            mechanics.edge_decisions[(9, 10)],
        ])

    def birth_guard_values(mechanics):
        result = {
            "S(" + ",".join(map(str, face)) + ")": mechanics.face_decisions[face]
            for face in guard_birth_faces
        }
        result.update({
            "H(" + ",".join(map(str, edge)) + ")": mechanics.edge_decisions[edge]
            for edge in guard_birth_edges
        })
        return result

    def sample(parameters):
        points = coordinates(parameters)
        mechanics = evaluate(labels, points)
        record = summarize(labels, points, rails)
        return (
            points,
            mechanics,
            record,
            values(points, mechanics),
            circuit_value(points),
            inherited_circuit_values(points),
        )

    # Keep decisions containing row 9 cease to exist on the forbidden side.
    # Linearize strictly inside the valid chamber, close to the exact wall.
    linearization = star - args.linearization_offset * direction_x
    keep_jacobian = np.empty((4, len(star)))
    circuit_gradient = np.empty(len(star))
    for column in range(len(star)):
        plus = linearization.copy()
        minus = linearization.copy()
        plus[column] += args.fd_step
        minus[column] -= args.fd_step
        plus_points, plus_mechanics, _, plus_values, plus_circuit, _ = sample(plus)
        minus_points, minus_mechanics, _, minus_values, minus_circuit, _ = sample(minus)
        keep_jacobian[:, column] = (plus_values - minus_values) / (2 * args.fd_step)
        circuit_gradient[column] = (plus_circuit - minus_circuit) / (2 * args.fd_step)

    _, singular_values, vt = np.linalg.svd(keep_jacobian, full_matrices=True)
    tolerance = max(keep_jacobian.shape) * np.finfo(float).eps * singular_values[0]
    rank = int(np.sum(singular_values > tolerance))
    null_basis = vt[rank:].T
    signed_circuit_gradient = args.valid_sign * circuit_gradient
    projection = null_basis @ (null_basis.T @ signed_circuit_gradient)
    projection_norm = float(np.linalg.norm(projection))
    direction_y_unit = projection / projection_norm
    rate_x = float(signed_circuit_gradient @ direction_x)
    rate_y_unit = float(signed_circuit_gradient @ direction_y_unit)
    direction_y_scale = (
        args.bypass_factor * abs(rate_x) / max(abs(rate_y_unit), 1e-300)
    )
    direction_y = direction_y_scale * direction_y_unit
    if signed_circuit_gradient @ direction_y < 0.0:
        direction_y *= -1.0
    direction_y_solver = "keep_nullspace_anticircuit_projection"
    keep_rate_x = keep_jacobian @ direction_x
    positive_keep = keep_rate_x > 0.0
    repair_targets = np.zeros(len(keep_rate_x))
    if np.any(positive_keep):
        # The saved wall direction can have a locally positive conditioned
        # derivative even though its preceding finite segment decreased that
        # decision.  The L path spans 2*x+y from start to end, so prescribe a
        # y-rate of -3*x for each such row.  Together with the required signed
        # circuit rate this is a five-equality minimum-norm solve in the large
        # local chart.
        repair_targets[positive_keep] = -3.0 * keep_rate_x[positive_keep]
        repair_matrix = np.vstack((keep_jacobian, signed_circuit_gradient))
        repair_rhs = np.r_[
            repair_targets,
            args.bypass_factor * abs(rate_x),
        ]
        direction_y, *_ = np.linalg.lstsq(
            repair_matrix, repair_rhs, rcond=1e-12
        )
        repair_residual = repair_matrix @ direction_y - repair_rhs
        if np.max(np.abs(repair_residual)) > 1e-8:
            raise ValueError(("positive-keep repair residual", repair_residual))
        direction_y_scale = float(np.linalg.norm(direction_y))
        direction_y_unit = direction_y / direction_y_scale
        direction_y_solver = "minimum_norm_circuit_plus_positive_keep_repair"

    quadrant_records = []
    for sx in (-1, 1):
        for sy in (-1, 1):
            parameters = star + args.radius * (sx * direction_x + sy * direction_y)
            try:
                _, mechanics, record, feature_values, circuit, inherited = sample(parameters)
                guarded_births = birth_guard_values(mechanics)
                quadrant_records.append({
                    "quadrant": [sx, sy],
                    "parameters": parameters.tolist(),
                    "circuit_determinant": circuit,
                    "minimum_signed_inherited_circuit": (
                        float(np.min(inherited)) if len(inherited) else None
                    ),
                    "feature_values": dict(zip(FEATURES, feature_values.tolist())),
                    "guarded_birth_values": guarded_births,
                    "class": record["class"],
                    "f_vector": record["f_vector"],
                    "stable_faces": record["stable_faces"],
                    "unstable_vertices": record["unstable_vertices"],
                    "saddle_edges": record["saddle_edges"],
                    "base_face_present": record["base_face_present"],
                    "missing_forced_rails": record["missing_forced_rails"],
                    "hard_valid": bool(
                        args.valid_sign * circuit > 0.0
                        and (not len(inherited) or np.all(inherited > 0.0))
                        and record["base_face_present"]
                        and not record["missing_forced_rails"]
                        and all(value < 0.0 for value in guarded_births.values())
                    ),
                })
            except Exception as error:
                quadrant_records.append({
                    "quadrant": [sx, sy],
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
            parameters = left + alpha * (right - left)
            try:
                _, mechanics, record, feature_values, circuit, inherited = sample(parameters)
                guarded_births = birth_guard_values(mechanics)
                path.append({
                    "segment": segment,
                    "alpha": float(alpha),
                    "circuit_determinant": circuit,
                    "minimum_signed_inherited_circuit": (
                        float(np.min(inherited)) if len(inherited) else None
                    ),
                    "feature_values": dict(zip(FEATURES, feature_values.tolist())),
                    "guarded_birth_values": guarded_births,
                    "class": record["class"],
                    "f_vector": record["f_vector"],
                    "stable_faces": record["stable_faces"],
                    "unstable_vertices": record["unstable_vertices"],
                    "saddle_edges": record["saddle_edges"],
                    "base_face_present": record["base_face_present"],
                    "missing_forced_rails": record["missing_forced_rails"],
                    "hard_valid": bool(
                        args.valid_sign * circuit > 0.0
                        and (not len(inherited) or np.all(inherited > 0.0))
                        and record["base_face_present"]
                        and not record["missing_forced_rails"]
                        and all(value < 0.0 for value in guarded_births.values())
                    ),
                })
            except Exception as error:
                path.append({
                    "segment": segment,
                    "alpha": float(alpha),
                    "error": repr(error),
                    "hard_valid": False,
                })

    start_values = path[0].get("feature_values", {})
    end_values = path[-1].get("feature_values", {})
    decreased = bool(start_values and all(
        end_values[name] < start_values[name] for name in FEATURES
    ))
    linked_birth_absent = all(
        "error" not in row
        and (8, 245, 246) not in {tuple(face) for face in row["stable_faces"]}
        and (8, 245) not in {tuple(edge) for edge in row["saddle_edges"]}
        and all(value < 0.0 for value in row["guarded_birth_values"].values())
        for row in path
    )
    bypass = bool(
        projection_norm > 1e-12
        and all(row["hard_valid"] for row in path)
        and linked_birth_absent
        and decreased
    )
    rowspace_coefficients, *_ = np.linalg.lstsq(
        keep_jacobian.T, signed_circuit_gradient, rcond=None
    )
    rowspace_residual = signed_circuit_gradient - keep_jacobian.T @ rowspace_coefficients
    payload = {
        "version": 1,
        "scope": f"{len(star)}D tangent atlas around hard circuit {circuit_labels}",
        "circuit": list(circuit_labels),
        "valid_sign": args.valid_sign,
        "inherited_circuit_guards": [
            {"circuit": list(circuit), "valid_sign": sign}
            for circuit, sign in inherited_circuit_specs
        ],
        "guard_birth_faces": [list(face) for face in guard_birth_faces],
        "guard_birth_edges": [list(edge) for edge in guard_birth_edges],
        "local_controls": adaptive.get("local_controls", []),
        "features": list(FEATURES),
        "star_parameters": star.tolist(),
        "linearization_parameters": linearization.tolist(),
        "linearization_offset": args.linearization_offset,
        "fd_step": args.fd_step,
        "keep_jacobian": keep_jacobian.tolist(),
        "keep_singular_values": singular_values.tolist(),
        "keep_rank": rank,
        "nullity": int(null_basis.shape[1]),
        "circuit_gradient": circuit_gradient.tolist(),
        "signed_circuit_gradient": signed_circuit_gradient.tolist(),
        "nullspace_anticircuit_projection_norm": projection_norm,
        "rowspace_blocker": {
            "coefficients": rowspace_coefficients.tolist(),
            "residual_norm": float(np.linalg.norm(rowspace_residual)),
        },
        "direction_x": direction_x.tolist(),
        "direction_y_unit": direction_y_unit.tolist(),
        "direction_y_scale": direction_y_scale,
        "bypass_factor": args.bypass_factor,
        "direction_y_solver": direction_y_solver,
        "positive_keep_repair_targets": dict(zip(FEATURES, repair_targets.tolist())),
        "direction_y": direction_y.tolist(),
        "remote_fraction_y_unit": float(np.linalg.norm(direction_y_unit[20:])),
        "feature_derivative_x": dict(zip(FEATURES, (keep_jacobian @ direction_x).tolist())),
        "feature_derivative_y": dict(zip(FEATURES, (keep_jacobian @ direction_y).tolist())),
        "circuit_derivative_x": rate_x,
        "circuit_derivative_y": float(signed_circuit_gradient @ direction_y),
        "radius": args.radius,
        "quadrants": quadrant_records,
        "bypass_waypoints": [point.tolist() for point in waypoints],
        "bypass_path": path,
        "bypass_audit": {
            "hard_valid_everywhere": all(row["hard_valid"] for row in path),
            "linked_birth_absent_everywhere": linked_birth_absent,
            "all_keep_decisions_decreased": decreased,
            "start_feature_values": start_values,
            "end_feature_values": end_values,
            "bypass_found": bypass,
        },
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "projection_norm": projection_norm,
        "direction_y_scale": direction_y_scale,
        "circuit_derivative_x": rate_x,
        "circuit_derivative_y": payload["circuit_derivative_y"],
        "remote_fraction_y_unit": payload["remote_fraction_y_unit"],
        "quadrants": quadrant_records,
        "bypass_audit": payload["bypass_audit"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
