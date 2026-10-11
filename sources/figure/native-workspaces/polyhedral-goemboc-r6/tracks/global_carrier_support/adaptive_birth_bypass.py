#!/usr/bin/env python3
"""Adaptive fresh-hull Newton continuation after the local birth bypass.

The four positive unwanted decisions S(7,8,245), U54, H(6,7), H(9,10)
are assigned equal relative first-order decay.  At every accepted point their
Jacobian is rebuilt after a fresh hull/own-centroid evaluation.  The linked
S(8,245,246)/H(8,245) gradients supply a nullspace correction that keeps both
birth guards negative without changing the four Newton rates to first order.

The run stops at, bisects, and materializes the first nonlocal discrete wall.
The enlarged base and all 37 named rails are hard constraints throughout.
"""

from __future__ import annotations

import argparse
import csv
import itertools
import json
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import LinearConstraint, linprog, minimize
from scipy.spatial import ConvexHull


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
from actual_hull_mechanics import _merge_coplanar_facets, evaluate  # noqa: E402
from optimize_base_escape import Search  # noqa: E402
from search_row54_remote228 import load_points, summarize  # noqa: E402


FEATURES = (
    "S(7,8,245)",
    "S(8,245,246)",
    "U54",
    "H(6,7)",
    "H(8,245)",
    "H(9,10)",
)
KEEP_INDEX = (0, 2, 3, 5)
BIRTH_INDEX = (1, 4)
CIRCUIT = (8, 9, 10, 263)
FOCUS_KEEP = {"S1": 0, "U54": 1, "H67": 2, "H910": 3}


def feature_values(
    mechanics,
    primary_face=(7, 8, 245),
    linked_face=(8, 245, 246),
    linked_edge=(8, 245),
    extra_birth_faces=(),
    extra_birth_vertices=(),
    extra_birth_edges=(),
    extra_keep_edges=(),
    secondary_edge=(9, 10),
):
    keys_present = (
        primary_face in mechanics.face_decisions,
        linked_face in mechanics.face_decisions,
        54 in mechanics.vertex_decisions,
        (6, 7) in mechanics.edge_decisions,
        linked_edge in mechanics.edge_decisions,
        secondary_edge in mechanics.edge_decisions,
    )
    if not all(keys_present):
        raise KeyError(dict(zip(FEATURES, keys_present)))
    result = [
        mechanics.face_decisions[primary_face],
        mechanics.face_decisions[linked_face],
        mechanics.vertex_decisions[54],
        mechanics.edge_decisions[(6, 7)],
        mechanics.edge_decisions[linked_edge],
        mechanics.edge_decisions[secondary_edge],
    ]
    result.extend(mechanics.face_decisions[face] for face in extra_birth_faces)
    result.extend(
        mechanics.vertex_decisions[vertex] for vertex in extra_birth_vertices
    )
    result.extend(mechanics.edge_decisions[edge] for edge in extra_birth_edges)
    result.extend(mechanics.edge_decisions[edge] for edge in extra_keep_edges)
    return np.asarray(result)


def discrete(record):
    return {
        "class": record["class"],
        "f_vector": record["f_vector"],
        "stable_faces": sorted(sorted(face) for face in record["stable_faces"]),
        "unstable_vertices": sorted(record["unstable_vertices"]),
        "saddle_edges": sorted(sorted(edge) for edge in record["saddle_edges"]),
        "base_face_present": record["base_face_present"],
        "missing_forced_rails": record["missing_forced_rails"],
    }


def compact(record):
    result = discrete(record)
    result["target_violations"] = record["target_violations"]
    result["centroid"] = record["centroid"]
    return result


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
    parser.add_argument("--circuit-atlas", type=Path)
    parser.add_argument(
        "--start-adaptive", type=Path,
        help=(
            "optional prior adaptive JSON; start from wall.pre_parameters "
            "or its last trace point instead of the circuit-atlas endpoint"
        ),
    )
    parser.add_argument(
        "--start-trace-last",
        action="store_true",
        help=(
            "with --start-adaptive, resume from its last accepted trace point "
            "instead of a bisection point on the reported wall"
        ),
    )
    parser.add_argument(
        "--start-parameters-json", type=Path,
        help=(
            "JSON artifact containing a literal branch_parameters vector; "
            "takes precedence over adaptive and atlas waypoints"
        ),
    )
    parser.add_argument(
        "--start-parameters-key", default="branch_parameters",
        help="field read from --start-parameters-json",
    )
    parser.add_argument(
        "--local-control", type=float, nargs=5, action="append", default=[],
        metavar=("LABEL", "DX", "DY", "DZ", "INITIAL"),
        help=(
            "repeatable extra point displacement: label, direction, and "
            "initial scalar coefficient"
        ),
    )
    parser.add_argument(
        "--freeze-local-control", type=int, action="append", default=[],
        metavar="LABEL",
        help="repeatable local-control coefficient constrained to zero tangent rate",
    )
    parser.add_argument(
        "--guard-circuit", type=int, nargs=5, action="append", default=[],
        metavar=("A", "B", "C", "D", "SIGN"),
        help="repeatable four-label determinant guard followed by valid sign",
    )
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--pre-csv", type=Path, required=True)
    parser.add_argument("--post-csv", type=Path, required=True)
    parser.add_argument("--fd-step", type=float, default=1e-5)
    parser.add_argument(
        "--local-fd-step", type=float,
        help=(
            "finite-difference step for appended point controls; use a "
            "smaller value when a control only has a narrow topology-safe band"
        ),
    )
    parser.add_argument(
        "--fixed-topology-jacobian", action="store_true",
        help=(
            "differentiate own-centroid mechanics on the current fixed hull "
            "cycles, while retaining fresh-hull validation for every trial"
        ),
    )
    parser.add_argument("--initial-step", type=float, default=8e-4)
    parser.add_argument("--max-step", type=float, default=8e-3)
    parser.add_argument("--iterations", type=int, default=40)
    parser.add_argument("--wall-bisections", type=int, default=45)
    parser.add_argument(
        "--birth-tangent-band", type=float, default=1e-2,
        help=(
            "negative birth guards farther from zero than this are checked "
            "by line search but omitted from the local tangent cone"
        ),
    )
    parser.add_argument(
        "--birth-inward-buffer", type=float, default=0.0,
        help=(
            "with --focus-keep, require each active birth guard to have at "
            "least this normalized inward rate relative to the focused unit rate"
        ),
    )
    parser.add_argument(
        "--circuit-tangent-band", type=float, default=float("inf"),
        help=(
            "only signed circuit margins at or below this raw determinant "
            "enter the local tangent cone; all circuits remain hard line-search guards"
        ),
    )
    parser.add_argument(
        "--focus-keep", choices=tuple(FOCUS_KEEP),
        help=(
            "accelerate one keep decision: give it unit relative decay and "
            "treat the other three as no-worsen inequalities"
        ),
    )
    parser.add_argument(
        "--primary-face", type=int, nargs=3, default=(7, 8, 245),
        metavar=("A", "B", "C"),
        help="current unwanted stable face followed as the first keep feature",
    )
    parser.add_argument(
        "--linked-face", type=int, nargs=3, default=(8, 245, 246),
        metavar=("A", "B", "C"),
        help="adjacent nonstable face guarded against a linked S-H birth",
    )
    parser.add_argument(
        "--linked-edge", type=int, nargs=2, default=(8, 245),
        metavar=("A", "B"),
        help="edge shared by --primary-face and --linked-face",
    )
    parser.add_argument(
        "--focus-no-worsen-buffer", type=float, default=0.0,
        help=(
            "with --focus-keep, require each other relative keep rate to be "
            "at most minus this fraction of the focused unit rate; a small "
            "positive value supplies inward curvature slack"
        ),
    )
    parser.add_argument(
        "--secondary-edge", type=int, nargs=2, default=(9, 10),
        metavar=("A", "B"),
        help=(
            "fourth unwanted keep edge; use 10 11 after the stage-18 "
            "H(9,10)->H(10,11) transfer"
        ),
    )
    parser.add_argument(
        "--secondary-cap", type=float,
        help=(
            "in focused mode, permit the transported secondary saddle to "
            "grow up to this absolute decision value; the other two "
            "nonfocused defects remain monotone, and the secondary becomes "
            "a tangent no-worsen guard after reaching 80 percent of the cap"
        ),
    )
    parser.add_argument(
        "--birth-face", type=int, nargs=3, action="append", default=[],
        metavar=("A", "B", "C"),
        help="repeatable additional stable-face birth guard",
    )
    parser.add_argument(
        "--birth-vertex", type=int, action="append", default=[],
        metavar="V",
        help="repeatable additional unstable-vertex birth guard",
    )
    parser.add_argument(
        "--birth-edge", type=int, nargs=2, action="append", default=[],
        metavar=("A", "B"),
        help="repeatable additional saddle-edge birth guard",
    )
    parser.add_argument(
        "--extra-keep-edge", type=int, nargs=2, action="append", default=[],
        metavar=("A", "B"),
        help=(
            "repeatable additional positive saddle decision constrained by "
            "the focused no-worsen cone"
        ),
    )
    args = parser.parse_args()
    primary_face = tuple(sorted(args.primary_face))
    linked_face = tuple(sorted(args.linked_face))
    linked_edge = tuple(sorted(args.linked_edge))
    secondary_edge = tuple(sorted(args.secondary_edge))
    extra_birth_faces = [tuple(row) for row in args.birth_face]
    extra_birth_vertices = [int(row) for row in args.birth_vertex]
    extra_birth_edges = [tuple(row) for row in args.birth_edge]
    extra_keep_edges = [tuple(sorted(row)) for row in args.extra_keep_edge]
    features = [
        "S(" + ",".join(map(str, primary_face)) + ")",
        "S(" + ",".join(map(str, linked_face)) + ")",
        "U54",
        "H(6,7)",
        "H(" + ",".join(map(str, linked_edge)) + ")",
        "H(9,10)",
    ]
    features[5] = "H(" + ",".join(map(str, secondary_edge)) + ")"
    features.extend(
        "S(" + ",".join(map(str, face)) + ")"
        for face in extra_birth_faces
    )
    features.extend("U" + str(vertex) for vertex in extra_birth_vertices)
    features.extend(
        "H(" + ",".join(map(str, edge)) + ")"
        for edge in extra_birth_edges
    )
    birth_index = list(BIRTH_INDEX) + list(range(len(FEATURES), len(features)))
    first_extra_keep = len(features)
    features.extend(
        "H(" + ",".join(map(str, edge)) + ")"
        for edge in extra_keep_edges
    )
    keep_index = list(KEEP_INDEX) + list(range(first_extra_keep, len(features)))

    labels, source = load_points(args.source)
    index = {label: offset for offset, label in enumerate(labels)}
    audit = json.loads(args.audit.read_text())
    rails = {
        tuple(sorted(edge))
        for edge in audit["fresh_hull_audit"]["forced_rail_edges"]
    }
    search = Search(labels, source, rails, report=False)
    atlas = json.loads(args.atlas.read_text())
    remote_basis = np.asarray([
        atlas["remote_basis"]["tangent"],
        atlas["remote_basis"]["normal"],
    ])
    local_controls = []
    for raw in args.local_control:
        label = int(raw[0])
        if label not in index:
            raise ValueError(("unknown local-control label", label))
        direction = np.asarray(raw[1:4], dtype=float)
        norm = float(np.linalg.norm(direction))
        if norm == 0.0:
            raise ValueError(("zero local-control direction", label))
        local_controls.append((label, direction / norm, float(raw[4])))

    def coordinates(parameters):
        points = search.coordinates(parameters[:20])
        points[index[228]] += parameters[20] * remote_basis[0]
        points[index[228]] += parameters[21] * remote_basis[1]
        for offset, (label, direction, _) in enumerate(local_controls):
            points[index[label]] += parameters[22 + offset] * direction
        return points

    def circuit_values(points):
        result = []
        for labels4, _ in circuit_specs:
            rows = np.c_[points[[index[label] for label in labels4]], np.ones(4)]
            result.append(float(np.linalg.det(rows)))
        return np.asarray(result)

    def fixed_feature_values(points, cycles):
        """Smooth mechanics extension on oriented cycles of the current cell.

        This is used only for the local Jacobian.  Trial acceptance still
        rebuilds a fresh ConvexHull through ``sample``.  It prevents a tiny
        protected circuit from making a centred finite difference sample the
        adjacent triangulation and corrupt the own-centroid derivative.
        """
        normals = []
        edge_faces = {}
        neighbours = {offset: set() for offset in range(len(points))}
        face_lookup = {}
        for face_index, cycle in enumerate(cycles):
            area = np.zeros(3)
            for first, second in zip(cycle, cycle[1:] + cycle[:1]):
                area += np.cross(points[first], points[second])
                edge = tuple(sorted((first, second)))
                edge_faces.setdefault(edge, []).append(face_index)
                neighbours[first].add(second)
                neighbours[second].add(first)
            normal_norm = float(np.linalg.norm(area))
            if normal_norm == 0.0:
                raise ValueError("degenerate fixed-topology face")
            normals.append(area / normal_norm)
            face_lookup[tuple(sorted(labels[offset] for offset in cycle))] = (
                face_index, cycle
            )

        determinant_sum = 0.0
        moment_sum = np.zeros(3)
        for cycle in cycles:
            for offset in range(1, len(cycle) - 1):
                a, b, c = points[[cycle[0], cycle[offset], cycle[offset + 1]]]
                determinant = np.linalg.det(np.stack((a, b, c)))
                determinant_sum += determinant
                moment_sum += determinant * (a + b + c)
        if determinant_sum <= 0.0:
            raise ValueError("nonpositive fixed-topology oriented volume")
        centroid = moment_sum / (4.0 * determinant_sum)
        centred = points - centroid

        def face_decision(face):
            face_index, cycle = face_lookup[tuple(sorted(face))]
            normal = normals[face_index]
            height = np.dot(normal, centred[cycle[0]])
            foot = height * normal
            reference = centred[cycle].mean(axis=0)
            values = []
            for first, second in zip(cycle, cycle[1:] + cycle[:1]):
                value = np.dot(
                    np.cross(centred[second] - centred[first], foot - centred[first]),
                    normal,
                )
                if np.dot(
                    np.cross(
                        centred[second] - centred[first], reference - centred[first]
                    ),
                    normal,
                ) < 0.0:
                    value = -value
                values.append(
                    value / np.linalg.norm(centred[second] - centred[first])
                )
            return min(values)

        def vertex_decision(label):
            offset = index[label]
            values = [
                -np.dot(centred[offset], centred[other] - centred[offset])
                / (
                    np.linalg.norm(centred[offset])
                    * np.linalg.norm(centred[other] - centred[offset])
                )
                for other in neighbours[offset]
            ]
            return min(values)

        def edge_decision(edge_labels):
            first, second = sorted(index[label] for label in edge_labels)
            incident = edge_faces[(first, second)]
            direction = centred[second] - centred[first]
            t = -np.dot(centred[first], direction) / np.dot(direction, direction)
            closest = centred[first] + t * direction
            normal1, normal2 = normals[incident[0]], normals[incident[1]]
            aa = np.dot(normal1, normal1)
            ab = np.dot(normal1, normal2)
            bb = np.dot(normal2, normal2)
            r1 = np.dot(closest, normal1)
            r2 = np.dot(closest, normal2)
            denominator = aa * bb - ab * ab
            beta1 = (r1 * bb - r2 * ab) / denominator
            beta2 = (r2 * aa - r1 * ab) / denominator
            closest_norm_squared = max(float(np.dot(closest, closest)), 1e-300)
            return min(
                t,
                1.0 - t,
                beta1 * np.sqrt(aa / closest_norm_squared),
                beta2 * np.sqrt(bb / closest_norm_squared),
            )

        result = [
            face_decision(primary_face),
            face_decision(linked_face),
            vertex_decision(54),
            edge_decision((6, 7)),
            edge_decision(linked_edge),
            edge_decision(secondary_edge),
        ]
        result.extend(face_decision(face) for face in extra_birth_faces)
        result.extend(vertex_decision(vertex) for vertex in extra_birth_vertices)
        result.extend(edge_decision(edge) for edge in extra_birth_edges)
        result.extend(edge_decision(edge) for edge in extra_keep_edges)
        return np.asarray(result)

    def sample(parameters, require_features=True):
        points = coordinates(parameters)
        mechanics = evaluate(labels, points)
        record = summarize(labels, points, rails)
        values = (
            feature_values(
                mechanics,
                primary_face,
                linked_face,
                linked_edge,
                extra_birth_faces,
                extra_birth_vertices,
                extra_birth_edges,
                extra_keep_edges,
                secondary_edge,
            )
            if require_features else None
        )
        return values, record, points, circuit_values(points)

    circuit_atlas = None
    if args.circuit_atlas:
        circuit_atlas = json.loads(args.circuit_atlas.read_text())
    if args.start_parameters_json:
        start_packet = json.loads(args.start_parameters_json.read_text())
        parameters = np.asarray(
            start_packet[args.start_parameters_key], dtype=float
        )
    elif args.start_adaptive:
        start_adaptive = json.loads(args.start_adaptive.read_text())
        if args.start_trace_last:
            parameters = np.asarray(
                start_adaptive["trace"][-1]["parameters"], dtype=float
            )
        elif start_adaptive.get("wall", {}).get("pre_parameters") is not None:
            parameters = np.asarray(
                start_adaptive["wall"]["pre_parameters"], dtype=float
            )
        else:
            parameters = np.asarray(
                start_adaptive["trace"][-1]["parameters"], dtype=float
            )
    elif circuit_atlas is not None:
        parameters = np.asarray(
            circuit_atlas["bypass_waypoints"][-1], dtype=float
        )
    else:
        parameters = np.asarray(atlas["bypass_waypoints"][-1], dtype=float)
    if len(parameters) == 22 and local_controls:
        parameters = np.r_[parameters, [row[2] for row in local_controls]]
    expected_parameter_count = 22 + len(local_controls)
    if len(parameters) != expected_parameter_count:
        raise ValueError((
            "parameter/local-control dimension mismatch",
            len(parameters), expected_parameter_count,
        ))
    circuit_specs = []
    if circuit_atlas is not None:
        circuit_specs.append((
            tuple(circuit_atlas.get("circuit", CIRCUIT)),
            int(circuit_atlas.get("valid_sign", -1)),
        ))
    for row in args.guard_circuit:
        labels4, sign = tuple(row[:4]), int(row[4])
        if sign not in (-1, 1):
            raise ValueError(("guard sign", sign))
        spec = (labels4, sign)
        if spec not in circuit_specs:
            circuit_specs.append(spec)

    def circuit_dict(circuit_array):
        return {
            f"{list(labels4)} sign {sign}": float(value)
            for (labels4, sign), value in zip(circuit_specs, circuit_array)
        }

    values, record, points, circuits = sample(parameters)
    initial_parameters = parameters.copy()
    initial_values = values.copy()
    baseline_signature = discrete(record)
    trace = [{
        "iteration": 0,
        "step": 0.0,
        "parameters": parameters.tolist(),
        "feature_values": dict(zip(features, values.tolist())),
        "circuit_determinants": circuit_dict(circuits),
        "summary": compact(record),
    }]
    step = args.initial_step
    wall = None

    def valid_same(candidate, old_values, signature):
        try:
            new_values, new_record, new_points, new_circuits = sample(candidate)
        except Exception as error:
            return False, {"error": repr(error)}, None, None
        hard = new_record["base_face_present"] and not new_record["missing_forced_rails"]
        linked_safe = bool(np.all(new_values[birth_index] < 0.0))
        circuit_safe = bool(all(
            sign * value > 0.0
            for (_, sign), value in zip(circuit_specs, new_circuits)
        ))
        # Near a circuit wall the accepted arclength can fall below 1e-7.  A
        # fresh hull/centroid evaluation then moves an individual conditioned
        # margin by only a few ulps, so demanding four strict floating-point
        # inequalities creates a spurious wall.  Keep the monotonicity test
        # scale-aware: allow evaluation noise in every component, while still
        # requiring a resolvable decrease in at least one component.
        old_keep = old_values[keep_index]
        new_keep = new_values[keep_index]
        keep_scale = np.maximum(1.0, np.abs(old_keep))
        comparison_tolerance = 5.0e-12 * keep_scale
        progress_tolerance = 1.0e-13 * keep_scale
        relaxed_secondary = bool(
            args.secondary_cap is not None
            and args.focus_keep is not None
            and FOCUS_KEEP[args.focus_keep] != 3
        )
        monotone_indices = [
            index for index in range(len(old_keep))
            if not (relaxed_secondary and index == 3)
            and (
                args.focus_keep is None
                or old_keep[index] > 0.0
                or index == FOCUS_KEEP[args.focus_keep]
            )
        ]
        secondary_cap_safe = bool(
            not relaxed_secondary
            or new_keep[3] <= args.secondary_cap + comparison_tolerance[3]
        )
        decreased = bool(
            np.all(
                new_keep[monotone_indices]
                <= old_keep[monotone_indices] + comparison_tolerance[monotone_indices]
            )
            and np.any(
                new_keep[monotone_indices]
                < old_keep[monotone_indices] - progress_tolerance[monotone_indices]
            )
            and secondary_cap_safe
        )
        same = discrete(new_record) == signature
        diagnostics = {
            "hard": hard,
            "linked_safe": linked_safe,
            "circuit_safe": circuit_safe,
            "circuit_determinants": circuit_dict(new_circuits),
            "keep_decreased": decreased,
            "secondary_cap_safe": secondary_cap_safe,
            "keep_delta": (new_keep - old_keep).tolist(),
            "keep_comparison_tolerance": comparison_tolerance.tolist(),
            "same_signature": same,
            "feature_values": dict(zip(features, new_values.tolist())),
            "summary": compact(new_record),
        }
        return hard and linked_safe and circuit_safe and decreased and same, diagnostics, new_values, new_points

    for iteration in range(1, args.iterations + 1):
        fixed_cycles = None
        if args.fixed_topology_jacobian:
            fixed_hull = ConvexHull(points)
            fixed_cycles, _ = _merge_coplanar_facets(points, fixed_hull)
        jacobian = np.empty((len(features), len(parameters)))
        derivative_failure = None
        for column in range(len(parameters)):
            column_step = (
                args.local_fd_step
                if column >= 22 and args.local_fd_step is not None
                else args.fd_step
            )
            plus = parameters.copy()
            minus = parameters.copy()
            plus[column] += column_step
            minus[column] -= column_step
            try:
                if fixed_cycles is not None:
                    plus_points = coordinates(plus)
                    minus_points = coordinates(minus)
                    plus_values = fixed_feature_values(plus_points, fixed_cycles)
                    minus_values = fixed_feature_values(minus_points, fixed_cycles)
                    plus_circuits = circuit_values(plus_points)
                    minus_circuits = circuit_values(minus_points)
                else:
                    plus_values, _, plus_points, plus_circuits = sample(plus)
                    minus_values, _, minus_points, minus_circuits = sample(minus)
            except Exception as error:
                derivative_failure = {"column": column, "error": repr(error)}
                break
            jacobian[:, column] = (plus_values - minus_values) / (2 * column_step)
            if column == 0:
                circuit_jacobian = np.empty((len(circuit_specs), len(parameters)))
            if circuit_specs:
                circuit_jacobian[:, column] = (
                    plus_circuits - minus_circuits
                ) / (2 * column_step)
        if derivative_failure is not None:
            wall = {"kind": "finite_difference_topology", **derivative_failure}
            break

        keep_values = values[keep_index]
        keep_jacobian = jacobian[keep_index]
        relative_jacobian = keep_jacobian / keep_values[:, None]
        focus_keep_index = (
            None if args.focus_keep is None else FOCUS_KEEP[args.focus_keep]
        )
        if focus_keep_index is None:
            equality_matrix = relative_jacobian
            equality_rhs = -np.ones(len(keep_values))
        else:
            equality_matrix = relative_jacobian[[focus_keep_index]]
            equality_rhs = -np.ones(1)
        for frozen_label in args.freeze_local_control:
            matching = [
                offset for offset, (label, _, _) in enumerate(local_controls)
                if label == frozen_label
            ]
            if len(matching) != 1:
                raise ValueError(("freeze-local-control not unique", frozen_label, matching))
            freeze_row = np.zeros(len(parameters))
            freeze_row[22 + matching[0]] = 1.0
            equality_matrix = np.vstack((equality_matrix, freeze_row))
            equality_rhs = np.r_[equality_rhs, 0.0]
        # Minimum-norm direction with equal relative decay rates.
        direction = equality_matrix.T @ np.linalg.solve(
            equality_matrix @ equality_matrix.T
            + 1e-13 * np.eye(len(equality_rhs)),
            equality_rhs,
        )

        _, singular_values, vt = np.linalg.svd(equality_matrix, full_matrices=True)
        tolerance = max(equality_matrix.shape) * np.finfo(float).eps * singular_values[0]
        rank = int(np.sum(singular_values > tolerance))
        null_basis = vt[rank:].T
        all_birth_rows = jacobian[birth_index]
        birth_values = values[birth_index]
        active_birth_mask = birth_values >= -args.birth_tangent_band
        birth_rows = all_birth_rows[active_birth_mask]
        active_birth_features = [
            features[index]
            for index, active in zip(birth_index, active_birth_mask)
            if active
        ]
        anti_norm = 0.0
        if len(birth_rows):
            normalized_birth = (
                birth_rows / np.linalg.norm(birth_rows, axis=1)[:, None]
            )
            birth_gradient = normalized_birth.mean(axis=0)
            anti = -null_basis @ (null_basis.T @ birth_gradient)
            anti_norm = float(np.linalg.norm(anti))
            if anti_norm > 1e-14:
                anti /= anti_norm
                birth_rate = birth_rows @ direction
                anti_rate = birth_rows @ anti
                needed = 0.0
                for current_rate, correction_rate in zip(birth_rate, anti_rate):
                    if current_rate > 0.0 and correction_rate < 0.0:
                        needed = max(
                            needed, 1.10 * current_rate / -correction_rate
                        )
                direction += needed * anti

        # With the hard base circuit enabled, alternating nullspace projections
        # find the minimum local correction satisfying all three guard rows.
        if focus_keep_index is not None and args.birth_inward_buffer > 0.0:
            focus_row = equality_matrix[0]
            guard_rows = [
                row - args.birth_inward_buffer * np.linalg.norm(row) * focus_row
                for row in birth_rows
            ]
        else:
            guard_rows = list(birth_rows)
        if focus_keep_index is not None:
            # Preserve the other three unwanted decisions while allowing the
            # selected dominant witness to decay as rapidly as the cell permits.
            # Since the focused equality has h*d=-1, the homogeneous row
            # (r-epsilon*h)*d<=0 is exactly r*d<=-epsilon.  This supplies
            # controllable inward slack without changing the cone machinery.
            focus_row = equality_matrix[0]
            relaxed_secondary = bool(
                args.secondary_cap is not None and focus_keep_index != 3
            )
            secondary_cap_active = bool(
                relaxed_secondary
                and keep_values[3] >= 0.8 * args.secondary_cap
            )
            guard_rows.extend(
                (
                    relative_jacobian[index]
                    - args.focus_no_worsen_buffer * focus_row
                )
                for index in range(len(keep_values))
                if index != focus_keep_index
                and not (relaxed_secondary and index == 3)
                and keep_values[index] > 0.0
            )
            if secondary_cap_active:
                guard_rows.append(relative_jacobian[3])
        else:
            relaxed_secondary = False
            secondary_cap_active = False
        signed_circuit_values = np.asarray([
            sign * value
            for (_, sign), value in zip(circuit_specs, circuits)
        ])
        active_circuit_mask = (
            signed_circuit_values <= args.circuit_tangent_band
        )
        active_circuit_specs = [
            {"circuit": list(labels4), "valid_sign": sign}
            for (labels4, sign), active in zip(circuit_specs, active_circuit_mask)
            if active
        ]
        for row, (_, sign), active in zip(
            circuit_jacobian, circuit_specs, active_circuit_mask
        ):
            if not active:
                continue
            # The projection loop enforces row*d <= 0, whereas a valid signed
            # circuit guard sign*det > 0 must have nonnegative derivative.
            guard_rows.append(-sign * row)
        guard_rows = np.asarray(guard_rows)
        null_projector = null_basis @ null_basis.T
        for _ in range(40):
            rates = guard_rows @ direction
            if np.max(rates) <= 1e-10:
                break
            for guard, rate in zip(guard_rows, rates):
                if rate <= 0.0:
                    continue
                projected = null_projector @ guard
                denominator = float(guard @ projected)
                if denominator > 1e-20:
                    direction -= 1.10 * rate / denominator * projected

        # Complete linear tangent-cone feasibility.  Normalize every row, use
        # HiGHS as a feasibility oracle, then enumerate active guard subsets to
        # obtain the true minimum-norm tangent without ill-conditioned QP
        # iterations near a diagonal flip.
        guard_norms = np.linalg.norm(guard_rows, axis=1)
        scaled_guards = guard_rows / np.maximum(guard_norms[:, None], 1e-300)
        tangent_lp = linprog(
            np.zeros(len(parameters)),
            A_ub=scaled_guards,
            b_ub=np.zeros(len(scaled_guards)),
            A_eq=equality_matrix,
            b_eq=equality_rhs,
            bounds=[(None, None)] * len(parameters),
            method="highs",
        )
        if not tangent_lp.success:
            # Farkas alternative for Gd<=0, Ad=b: find z>=0,y free with
            # G^T z + A^T y = 0 and b^T y = -1.
            guard_count = len(scaled_guards)
            equality_count = len(equality_rhs)
            farkas_matrix = np.zeros(
                (len(parameters) + 1, guard_count + equality_count)
            )
            farkas_matrix[:len(parameters), :guard_count] = scaled_guards.T
            farkas_matrix[:len(parameters), guard_count:] = equality_matrix.T
            farkas_matrix[-1, guard_count:] = equality_rhs
            farkas_rhs = np.r_[np.zeros(len(parameters)), -1.0]
            farkas = linprog(
                np.zeros(guard_count + equality_count),
                A_eq=farkas_matrix,
                b_eq=farkas_rhs,
                bounds=(
                    [(0.0, None)] * guard_count
                    + [(None, None)] * equality_count
                ),
                method="highs",
            )
            wall = {
                "kind": "linear_tangent_farkas_blocker",
                "tangent_lp_status": tangent_lp.message,
                "farkas_success": bool(farkas.success),
                "farkas_guard_weights": (
                    farkas.x[:guard_count].tolist() if farkas.success else None
                ),
                "farkas_equality_weights": (
                    farkas.x[guard_count:].tolist() if farkas.success else None
                ),
                "farkas_identity_residual": (
                    float(np.max(np.abs(farkas_matrix @ farkas.x - farkas_rhs)))
                    if farkas.success else None
                ),
            }
            break
        best_active = None
        best_direction = None
        best_norm = float("inf")
        for active_count in range(len(scaled_guards) + 1):
            for active in itertools.combinations(range(len(scaled_guards)), active_count):
                matrix = equality_matrix
                rhs = equality_rhs
                if active:
                    matrix = np.vstack((matrix, scaled_guards[list(active)]))
                    rhs = np.r_[rhs, np.zeros(active_count)]
                candidate, *_ = np.linalg.lstsq(matrix, rhs, rcond=1e-12)
                if np.max(np.abs(equality_matrix @ candidate - equality_rhs)) > 2e-7:
                    continue
                if active and np.max(np.abs(scaled_guards[list(active)] @ candidate)) > 2e-7:
                    continue
                if np.max(scaled_guards @ candidate) > 2e-8:
                    continue
                norm = float(np.linalg.norm(candidate))
                if norm < best_norm:
                    best_norm = norm
                    best_direction = candidate
                    best_active = active
        if best_direction is not None:
            direction = best_direction
            tangent_solver = f"active_set_minimum_norm:{list(best_active)}"
        else:
            direction = tangent_lp.x
            tangent_solver = "highs_feasible_extreme_after_active_set_failure"

        keep_rates = keep_jacobian @ direction
        birth_rates = birth_rows @ direction
        all_birth_rates = all_birth_rows @ direction
        circuit_rates = circuit_jacobian @ direction
        signed_circuit_rates = np.asarray([
            sign * rate for (_, sign), rate in zip(circuit_specs, circuit_rates)
        ])
        scaled_guard_rates = scaled_guards @ direction
        direction_norm = float(np.linalg.norm(direction))
        nonfocus_rate_indices = [
            index for index in range(len(keep_values))
            if index != focus_keep_index
            and not (relaxed_secondary and index == 3)
            and keep_values[index] > 0.0
        ]
        keep_rate_valid = (
            bool(np.all(keep_rates < 0.0))
            if focus_keep_index is None
            else bool(
                keep_rates[focus_keep_index] < 0.0
                and (
                    not nonfocus_rate_indices
                    or np.max(
                        keep_rates[nonfocus_rate_indices]
                        / np.maximum(
                            np.abs(keep_values[nonfocus_rate_indices]), 1e-300
                        )
                    ) <= 5e-8
                )
                and (
                    not secondary_cap_active
                    or keep_rates[3] <= 5e-8 * max(abs(keep_values[3]), 1e-300)
                )
            )
        )
        if (
            direction_norm == 0.0
            or not keep_rate_valid
            or np.max(scaled_guard_rates) > 5e-8
        ):
            wall = {
                "kind": "first_order_rank_blocker",
                "keep_rates": keep_rates.tolist(),
                "birth_rates": birth_rates.tolist(),
                "all_birth_rates": all_birth_rates.tolist(),
                "active_birth_features": active_birth_features,
                "active_circuit_specs": active_circuit_specs,
                "circuit_rates": circuit_rates.tolist(),
                "signed_circuit_rates": signed_circuit_rates.tolist(),
                "scaled_guard_rates": scaled_guard_rates.tolist(),
                "anti_projection_norm": anti_norm,
                "tangent_solver": tangent_solver,
            }
            break
        direction /= direction_norm

        accepted = None
        trial_step = min(step, args.max_step)
        first_bad = None
        for _ in range(18):
            candidate = parameters + trial_step * direction
            ok, diagnostics, candidate_values, candidate_points = valid_same(
                candidate, values, baseline_signature
            )
            if ok:
                accepted = (
                    trial_step, candidate, candidate_values,
                    diagnostics, candidate_points,
                )
                break
            first_bad = (trial_step, candidate, diagnostics)
            trial_step *= 0.5
        if accepted is None:
            wall = {
                "kind": "no_positive_safe_step",
                "first_bad": first_bad[2] if first_bad else None,
                "direction": direction.tolist(),
                "direction_norm_before_normalization": direction_norm,
                "keep_rates_before_normalization": keep_rates.tolist(),
                "birth_rates_before_normalization": birth_rates.tolist(),
                "all_birth_rates_before_normalization": all_birth_rates.tolist(),
                "active_birth_features": active_birth_features,
                "active_circuit_specs": active_circuit_specs,
                "circuit_rates_before_normalization": circuit_rates.tolist(),
                "signed_circuit_rates_before_normalization": signed_circuit_rates.tolist(),
                "scaled_guard_rates_before_normalization": scaled_guard_rates.tolist(),
                "tangent_solver": tangent_solver,
            }
            break

        # A failed large step is a wall only if a hard, birth, circuit, or
        # discrete-signature condition changed.  Failure of the monotonicity
        # check alone merely says the local Newton model needs a shorter step;
        # accept that shorter step and rebuild the Jacobian.  Conflating these
        # cases used to bisect floating-point noise into a fake wall.
        structural_wall = bool(
            first_bad is not None
            and not (
                first_bad[2].get("hard", False)
                and first_bad[2].get("linked_safe", False)
                and first_bad[2].get("circuit_safe", False)
                and first_bad[2].get("same_signature", False)
            )
        )
        if structural_wall:
            lo = 0.0
            hi = first_bad[0]
            pre = (parameters.copy(), values.copy(), record, points)
            post = None
            for _ in range(args.wall_bisections):
                mid = (lo + hi) / 2.0
                candidate = parameters + mid * direction
                ok, diagnostics, mid_values, mid_points = valid_same(
                    candidate, values, baseline_signature
                )
                if ok:
                    lo = mid
                    _, mid_record, _, mid_circuits = sample(candidate)
                    pre = (candidate, mid_values, mid_record, mid_points, mid_circuits)
                else:
                    hi = mid
                    post = (candidate, diagnostics, mid_values, mid_points)
            if len(pre) == 4:
                pre = (*pre, circuits)
            pre_parameters, pre_values, pre_record, pre_points, pre_circuits = pre
            if post is None:
                candidate = parameters + hi * direction
                _, diagnostics, post_values, post_points = valid_same(
                    candidate, values, baseline_signature
                )
                post = (candidate, diagnostics, post_values, post_points)
            post_parameters, post_diagnostics, post_values, post_points = post
            wall = {
                "kind": "first_discrete_or_guard_wall",
                "iteration": iteration,
                "step_lo": lo,
                "step_hi": hi,
                "parameter_width": hi - lo,
                "direction": direction.tolist(),
                "keep_rates_before_normalization": keep_rates.tolist(),
                "birth_rates_before_normalization": birth_rates.tolist(),
                "tangent_solver": tangent_solver,
                "pre_parameters": pre_parameters.tolist(),
                "pre_feature_values": dict(zip(features, pre_values.tolist())),
                "pre_circuit_determinants": circuit_dict(pre_circuits),
                "pre_summary": compact(pre_record),
                "post_parameters": post_parameters.tolist(),
                "post_diagnostics": post_diagnostics,
            }
            write_csv(args.pre_csv, labels, pre_points)
            if post_points is not None:
                write_csv(args.post_csv, labels, post_points)
            break

        trial_step, parameters, values, diagnostics, points = accepted
        record = summarize(labels, points, rails)
        circuits = circuit_values(points)
        trace.append({
            "iteration": iteration,
            "step": trial_step,
            "direction_norm_before_normalization": direction_norm,
            "keep_jacobian_singular_values": singular_values.tolist(),
            "anti_projection_norm": anti_norm,
            "tangent_solver": tangent_solver,
            "keep_rates_before_normalization": keep_rates.tolist(),
            "birth_rates_before_normalization": birth_rates.tolist(),
            "all_birth_rates_before_normalization": all_birth_rates.tolist(),
            "active_birth_features": active_birth_features,
            "active_circuit_specs": active_circuit_specs,
            "circuit_rates_before_normalization": circuit_rates.tolist(),
            "signed_circuit_rates_before_normalization": signed_circuit_rates.tolist(),
            "scaled_guard_rates_before_normalization": scaled_guard_rates.tolist(),
            "parameters": parameters.tolist(),
            "feature_values": dict(zip(features, values.tolist())),
            "circuit_determinants": circuit_dict(circuits),
            "summary": compact(record),
        })
        step = min(args.max_step, trial_step * 1.5)

    if wall is None:
        wall = {"kind": "iteration_limit"}
        write_csv(args.pre_csv, labels, points)
        write_csv(args.post_csv, labels, points)

    final_keep = values[keep_index]
    payload = {
        "version": 1,
        "scope": "adaptive 22D actual-hull Newton continuation with linked-birth guards",
        "source": str(args.source.resolve()),
        "atlas": str(args.atlas.resolve()),
        "circuit_atlas": None if args.circuit_atlas is None else str(args.circuit_atlas.resolve()),
        "start_adaptive": None if args.start_adaptive is None else str(args.start_adaptive.resolve()),
        "local_controls": [
            {
                "label": label,
                "direction": direction.tolist(),
                "initial": initial,
            }
            for label, direction, initial in local_controls
        ],
        "frozen_local_controls": list(args.freeze_local_control),
        "features": list(features),
        "keep_features": [features[i] for i in keep_index],
        "birth_guards": [features[i] for i in birth_index],
        "extra_birth_faces": [list(face) for face in extra_birth_faces],
        "extra_birth_edges": [list(edge) for edge in extra_birth_edges],
        "extra_keep_edges": [list(edge) for edge in extra_keep_edges],
        "birth_tangent_band": args.birth_tangent_band,
        "birth_inward_buffer": args.birth_inward_buffer,
        "circuit_tangent_band": args.circuit_tangent_band,
        "focus_keep": args.focus_keep,
        "focus_no_worsen_buffer": args.focus_no_worsen_buffer,
        "secondary_edge": list(secondary_edge),
        "secondary_cap": args.secondary_cap,
        "circuit_guards": [
            {"circuit": list(labels4), "valid_sign": sign}
            for labels4, sign in circuit_specs
        ],
        "fd_step": args.fd_step,
        "local_fd_step": args.local_fd_step,
        "fixed_topology_jacobian": args.fixed_topology_jacobian,
        "initial_step": args.initial_step,
        "max_step": args.max_step,
        "initial_parameters": initial_parameters.tolist(),
        "initial_feature_values": dict(zip(features, initial_values.tolist())),
        "trace": trace,
        "wall": wall,
        "relative_keep_reduction_at_stop": dict(zip(
            [features[i] for i in keep_index],
            (final_keep / initial_values[keep_index]).tolist(),
        )),
        "pre_wall_coordinates": str(args.pre_csv.resolve()),
        "post_wall_coordinates": str(args.post_csv.resolve()),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "accepted_steps": len(trace) - 1,
        "initial_feature_values": payload["initial_feature_values"],
        "last_feature_values": trace[-1]["feature_values"],
        "relative_keep_reduction_at_stop": payload["relative_keep_reduction_at_stop"],
        "wall": wall,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
