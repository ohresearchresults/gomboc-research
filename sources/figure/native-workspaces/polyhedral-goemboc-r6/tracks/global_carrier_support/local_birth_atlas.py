#!/usr/bin/env python3
"""Two-parameter actual-hull atlas around the first carrier birth wall.

Axis x is the saved minimum-norm pair-wall direction.  Axis y is the steepest
antibirth direction in the numerical nullspace of the four desired decision
gradients S(7,8,245), U54, H(6,7), H(9,10).  Two normalized local directions
of row 228 are included alongside the twenty in-base-plane variables.  Hence y
does not alter the desired first-order rates, but opposes the linked
S(8,245,246)/H(8,245) birth as strongly as that nullspace permits.

All quadrant and bypass-path samples rebuild the hull, use its own volume
centroid, and hard-check the enlarged base plus all 37 named rails.
"""

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
from optimize_base_escape import CONTROLLED, Search  # noqa: E402
from search_row54_remote228 import load_points, summarize  # noqa: E402
from search_two_actuator import project  # noqa: E402


FEATURES = (
    "S(7,8,245)",
    "S(8,245,246)",
    "U54",
    "H(6,7)",
    "H(8,245)",
    "H(9,10)",
)
KEEP = ("S(7,8,245)", "U54", "H(6,7)", "H(9,10)")
BIRTH = ("S(8,245,246)", "H(8,245)")


def decisions(mechanics):
    return np.asarray([
        mechanics.face_decisions[(7, 8, 245)],
        mechanics.face_decisions[(8, 245, 246)],
        mechanics.vertex_decisions[54],
        mechanics.edge_decisions[(6, 7)],
        mechanics.edge_decisions[(8, 245)],
        mechanics.edge_decisions[(9, 10)],
    ])


def compact(record):
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--continuation", type=Path, required=True)
    parser.add_argument("--roots", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--fd-step", type=float, default=2e-5)
    parser.add_argument("--radius", type=float, default=5e-4)
    parser.add_argument("--path-points", type=int, default=41)
    args = parser.parse_args()

    labels, source = load_points(args.source)
    index = {label: offset for offset, label in enumerate(labels)}
    audit = json.loads(args.audit.read_text())
    rails = {
        tuple(sorted(edge))
        for edge in audit["fresh_hull_audit"]["forced_rail_edges"]
    }
    search = Search(labels, source, rails, report=False)
    continuation = json.loads(args.continuation.read_text())
    roots = json.loads(args.roots.read_text())
    p0 = np.asarray(continuation["accepted"][0]["parameters"], dtype=float)
    p1 = np.asarray(continuation["accepted"][1]["parameters"], dtype=float)
    alpha_star = float(np.mean([
        row["alpha"] for row in roots["roots_in_order"]
    ]))
    base_star = p0 + alpha_star * (p1 - p0)

    old228 = search.coordinates(base_star)[index[228]]
    a, b, c = (source[index[label]] for label in (224, 229, 247))
    projected = project(old228, a, b, c)
    tangent = c - b
    tangent /= np.linalg.norm(tangent)
    normal = old228 - projected
    if np.linalg.norm(normal) < 1e-12:
        normal = np.cross(b - a, c - a)
    normal /= np.linalg.norm(normal)
    remote_scale = min(np.linalg.norm(old228 - source[index[label]]) for label in (224, 229, 247))
    remote_basis = remote_scale * np.stack((tangent, normal))

    def coordinates(parameters):
        points = search.coordinates(parameters[:20])
        points[index[228]] += parameters[20] * remote_basis[0]
        points[index[228]] += parameters[21] * remote_basis[1]
        return points

    def sample(parameters):
        points = coordinates(parameters)
        mechanics = evaluate(labels, points)
        record = summarize(labels, points, rails)
        return decisions(mechanics), record

    star = np.r_[base_star, 0.0, 0.0]
    value_star, summary_star = sample(star)
    jacobian = np.empty((len(FEATURES), len(star)))
    for column in range(len(star)):
        plus = star.copy()
        minus = star.copy()
        plus[column] += args.fd_step
        minus[column] -= args.fd_step
        plus_values, _ = sample(plus)
        minus_values, _ = sample(minus)
        jacobian[:, column] = (plus_values - minus_values) / (2 * args.fd_step)

    feature_index = {name: offset for offset, name in enumerate(FEATURES)}
    keep_indices = [feature_index[name] for name in KEEP]
    birth_indices = [feature_index[name] for name in BIRTH]
    keep_jacobian = jacobian[keep_indices]
    u, singular_values, vt = np.linalg.svd(keep_jacobian, full_matrices=True)
    tolerance = max(keep_jacobian.shape) * np.finfo(float).eps * singular_values[0]
    rank = int(np.sum(singular_values > tolerance))
    null_basis = vt[rank:].T

    birth_rows = jacobian[birth_indices]
    normalized_birth_rows = birth_rows / np.linalg.norm(birth_rows, axis=1)[:, None]
    combined_birth_gradient = normalized_birth_rows.mean(axis=0)
    projected_birth_gradient = null_basis @ (null_basis.T @ combined_birth_gradient)
    projected_norm = float(np.linalg.norm(projected_birth_gradient))

    direction_x = np.r_[p1 - p0, 0.0, 0.0]
    direction_x /= np.linalg.norm(direction_x)
    if projected_norm <= 1e-12:
        direction_y_unit = np.zeros_like(direction_x)
        direction_y = direction_y_unit.copy()
        scale_y = float("inf")
    else:
        direction_y_unit = -projected_birth_gradient / projected_norm
        rate_x = float(combined_birth_gradient @ direction_x)
        rate_y_unit = float(combined_birth_gradient @ direction_y_unit)
        # Equal positive x/y atlas coordinates give a strict antibirth rate:
        # b'(x + y) = rate_x - 2 rate_x = -rate_x.
        scale_y = 2.0 * abs(rate_x) / max(abs(rate_y_unit), 1e-300)
        direction_y = scale_y * direction_y_unit
        if combined_birth_gradient @ direction_y > 0.0:
            direction_y *= -1.0

    derivative_x = jacobian @ direction_x
    derivative_y = jacobian @ direction_y

    quadrant_records = []
    for sx in (-1, 1):
        for sy in (-1, 1):
            parameters = star + args.radius * (
                sx * direction_x + sy * direction_y
            )
            values, record = sample(parameters)
            quadrant_records.append({
                "quadrant": [sx, sy],
                "coordinates": [sx * args.radius, sy * args.radius],
                "feature_decisions": dict(zip(FEATURES, values.tolist())),
                "summary": compact(record),
                "hard_valid": bool(
                    record["base_face_present"]
                    and not record["missing_forced_rails"]
                ),
            })

    # L-shaped bypass: scalar pre-wall -> lift into +y -> cross in +x.
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
                values, record = sample(parameters)
                path.append({
                    "segment": segment,
                    "alpha": float(alpha),
                    "feature_decisions": dict(zip(FEATURES, values.tolist())),
                    "summary": compact(record),
                    "hard_valid": bool(
                        record["base_face_present"]
                        and not record["missing_forced_rails"]
                    ),
                })
            except Exception as error:
                path.append({
                    "segment": segment,
                    "alpha": float(alpha),
                    "error": repr(error),
                    "hard_valid": False,
                })

    baseline = path[0]
    endpoint = path[-1]
    start_stable = {tuple(face) for face in baseline["summary"]["stable_faces"]}
    start_saddles = {tuple(edge) for edge in baseline["summary"]["saddle_edges"]}
    avoided_birth = all(
        "error" not in row
        and (8, 245, 246) not in {tuple(face) for face in row["summary"]["stable_faces"]}
        and (8, 245) not in {tuple(edge) for edge in row["summary"]["saddle_edges"]}
        for row in path
    )
    no_other_birth = all(
        "error" not in row
        and {tuple(face) for face in row["summary"]["stable_faces"]} <= start_stable
        and {tuple(edge) for edge in row["summary"]["saddle_edges"]} <= start_saddles
        for row in path
    )
    desired_names = ("U54", "H(6,7)", "H(9,10)")
    simultaneous_decrease = all(
        endpoint["feature_decisions"][name]
        < baseline["feature_decisions"][name]
        for name in desired_names
    )
    bypass = bool(
        projected_norm > 1e-12
        and all(row["hard_valid"] for row in path)
        and avoided_birth
        and no_other_birth
        and simultaneous_decrease
    )

    rowspace_coefficients, *_ = np.linalg.lstsq(
        keep_jacobian.T, combined_birth_gradient, rcond=None
    )
    rowspace_residual = combined_birth_gradient - keep_jacobian.T @ rowspace_coefficients
    payload = {
        "version": 1,
        "scope": "22D local actual-hull atlas: 20 base variables plus 2 row228 variables",
        "source": str(args.source.resolve()),
        "continuation": str(args.continuation.resolve()),
        "roots": str(args.roots.resolve()),
        "features": list(FEATURES),
        "keep_decisions": list(KEEP),
        "birth_decisions": list(BIRTH),
        "alpha_star": alpha_star,
        "star_parameters": star.tolist(),
        "star_feature_decisions": dict(zip(FEATURES, value_star.tolist())),
        "star_summary": compact(summary_star),
        "remote_basis": {
            "labels": [228],
            "scale": remote_scale,
            "tangent": remote_basis[0].tolist(),
            "normal": remote_basis[1].tolist(),
        },
        "fd_step": args.fd_step,
        "jacobian": jacobian.tolist(),
        "keep_singular_values": singular_values.tolist(),
        "keep_rank": rank,
        "nullity": int(null_basis.shape[1]),
        "birth_jacobian_singular_values": np.linalg.svd(
            birth_rows, compute_uv=False
        ).tolist(),
        "birth_gradient_cosine": float(
            np.dot(birth_rows[0], birth_rows[1])
            / (np.linalg.norm(birth_rows[0]) * np.linalg.norm(birth_rows[1]))
        ),
        "nullspace_antibirth_projection_norm": projected_norm,
        "rowspace_blocker": {
            "coefficients": rowspace_coefficients.tolist(),
            "residual_norm": float(np.linalg.norm(rowspace_residual)),
        },
        "direction_x": direction_x.tolist(),
        "direction_y_unit": direction_y_unit.tolist(),
        "direction_y_scale": scale_y,
        "direction_y": direction_y.tolist(),
        "remote_fraction_x": float(np.linalg.norm(direction_x[20:])),
        "remote_fraction_y_unit": float(np.linalg.norm(direction_y_unit[20:])),
        "feature_derivative_x": dict(zip(FEATURES, derivative_x.tolist())),
        "feature_derivative_y": dict(zip(FEATURES, derivative_y.tolist())),
        "radius": args.radius,
        "quadrants": quadrant_records,
        "bypass_waypoints": [point.tolist() for point in waypoints],
        "bypass_path": path,
        "bypass_audit": {
            "hard_valid_everywhere": all(row["hard_valid"] for row in path),
            "avoided_linked_birth_everywhere": avoided_birth,
            "no_other_stable_or_saddle_birth": no_other_birth,
            "simultaneous_U54_H67_H910_decrease": simultaneous_decrease,
            "start_feature_decisions": baseline.get("feature_decisions"),
            "end_feature_decisions": endpoint.get("feature_decisions"),
            "bypass_found": bypass,
        },
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "alpha_star": alpha_star,
        "keep_rank": rank,
        "nullity": int(null_basis.shape[1]),
        "birth_gradient_cosine": payload["birth_gradient_cosine"],
        "nullspace_antibirth_projection_norm": projected_norm,
        "direction_y_scale": scale_y,
        "remote_fraction_y_unit": payload["remote_fraction_y_unit"],
        "feature_derivative_x": payload["feature_derivative_x"],
        "feature_derivative_y": payload["feature_derivative_y"],
        "quadrants": quadrant_records,
        "bypass_audit": payload["bypass_audit"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
