#!/usr/bin/env python3
"""Propose a rational Stage-31 path through the first H910 carrier relay.

The numerical LP is only a proposer.  Its output is converted into one literal
rational affine path rooted at the independently exact Stage-31 checkpoint.
The exact builder and the independent verifier audit that frozen path without
trusting the LP or finite differences.
"""
from __future__ import annotations

import csv
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
from scipy.optimize import brentq, linprog


HERE = Path(__file__).resolve().parent
TRACK = HERE.parent
ROOT = HERE.parents[2]
SOURCE = TRACK / "stage31_exact_checkpoint.csv"
FACES_PATH = TRACK / "stage31_exact_checkpoint_faces.json"
OUTPUT = HERE / "path_definition.json"

sys.path.insert(0, str(TRACK))
from actual_hull_mechanics import evaluate  # noqa: E402


BASE = (0, 54, *range(1, 17))
BASE_SET = set(BASE)
CARRIER_ROWS = (198, 228, 245, 246, 263, 264)
PRIMARY = (7, 8, 245)
OLD_QUAD = (7, 8, 245, 246)
TARGETS = (("S", PRIMARY), ("U", 54), ("H", (5, 6)), ("H", (9, 10)))
END_PARAMETER = Q(41, 5000)


def read_exact_rows(path: Path):
    rows = {}
    with path.open(newline="") as handle:
        for row in csv.DictReader(handle):
            rows[int(row["source_id"])] = tuple(
                Q(row[column]) for column in ("x", "y", "z")
            )
    return rows


def qadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def qsub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def qmul(a, scalar):
    return tuple(x * scalar for x in a)


def qdot(a, b):
    return sum(x * y for x, y in zip(a, b))


def qcross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def determinant(points, index, quad):
    rows = np.c_[points[[index[label] for label in quad]], np.ones(4)]
    return float(np.linalg.det(rows))


def mechanics_vector(mechanics, face_keys, vertex_keys, edge_keys):
    return np.asarray(
        [mechanics.face_decisions[key] for key in face_keys]
        + [mechanics.vertex_decisions[key] for key in vertex_keys]
        + [mechanics.edge_decisions[key] for key in edge_keys]
    )


def carrier_numerators(labels, points):
    mechanics = evaluate(labels, points)
    index = {label: offset for offset, label in enumerate(labels)}
    q10 = points[index[10]] - mechanics.centroid
    return np.asarray(
        [
            np.dot(q10, points[index[10]] - points[index[9]]),
            np.dot(q10, points[index[11]] - points[index[10]]),
        ],
        dtype=float,
    )


def support_specs(labels, points, faces, centroid, threshold=1e-4):
    index = {label: offset for offset, label in enumerate(labels)}
    specs = []
    all_specs = []
    for face_index, face in enumerate(faces):
        offsets = [index[label] for label in face]
        a, b, c = points[offsets[:3]]
        normal = np.cross(b - a, c - a)
        orientation = -1 if np.dot(normal, centroid - a) > 0 else 1
        incident = set(offsets)
        for witness in range(len(labels)):
            if witness in incident:
                continue
            value = -orientation * np.dot(normal, points[witness] - a)
            value /= np.linalg.norm(normal)
            if value <= 0:
                raise AssertionError(("bad source support", face_index, labels[witness], value))
            row = (face_index, witness, orientation, float(value))
            all_specs.append(row)
            if value < threshold:
                specs.append(row)
    return specs, all_specs


def support_values(labels, points, faces, specs):
    index = {label: offset for offset, label in enumerate(labels)}
    values = []
    for face_index, witness, orientation, _ in specs:
        offsets = [index[label] for label in faces[face_index]]
        a, b, c = points[offsets[:3]]
        normal = np.cross(b - a, c - a)
        value = -orientation * np.dot(normal, points[witness] - a)
        values.append(value / np.linalg.norm(normal))
    return np.asarray(values)


def exactify_velocity(exact_rows, labels, float_velocity):
    """Freeze a rational velocity while preserving the exact base plane."""
    p0 = exact_rows[0]
    basis_u = qsub(exact_rows[1], p0)
    basis_v = qsub(exact_rows[2], p0)
    basis_float = np.column_stack(
        ([float(x) for x in basis_u], [float(x) for x in basis_v])
    )
    velocity = {}
    coefficient_packet = {}
    for offset, label in enumerate(labels):
        raw = float_velocity[offset]
        if label in BASE_SET:
            coefficients, *_ = np.linalg.lstsq(basis_float, raw, rcond=None)
            alpha = Q(format(float(coefficients[0]), ".17g"))
            beta = Q(format(float(coefficients[1]), ".17g"))
            velocity[label] = qadd(qmul(basis_u, alpha), qmul(basis_v, beta))
            coefficient_packet[str(label)] = [str(alpha), str(beta)]
        else:
            velocity[label] = tuple(Q(format(float(value), ".17g")) for value in raw)

    normal = qcross(basis_u, basis_v)
    for label in BASE:
        if qdot(normal, velocity[label]):
            raise AssertionError(("base velocity left exact plane", label))
    return velocity, coefficient_packet


def main():
    exact_rows = read_exact_rows(SOURCE)
    labels = sorted(exact_rows)
    index = {label: offset for offset, label in enumerate(labels)}
    points = np.asarray(
        [[float(value) for value in exact_rows[label]] for label in labels]
    )
    faces = json.loads(FACES_PATH.read_text())
    source_mechanics = evaluate(labels, points)
    if source_mechanics.cls != (2, 2, 2):
        raise AssertionError(source_mechanics.cls)

    plane_u = points[index[1]] - points[index[0]]
    plane_u /= np.linalg.norm(plane_u)
    plane_normal = np.cross(plane_u, points[index[2]] - points[index[0]])
    plane_normal /= np.linalg.norm(plane_normal)
    plane_v = np.cross(plane_normal, plane_u)
    plane_v /= np.linalg.norm(plane_v)

    modes = []
    mode_names = []
    for label in BASE:
        for name, direction in (("u", plane_u), ("v", plane_v)):
            mode = np.zeros_like(points)
            mode[index[label]] = direction
            modes.append(mode)
            mode_names.append((label, name))
    for label in CARRIER_ROWS:
        for axis, name in enumerate("xyz"):
            mode = np.zeros_like(points)
            mode[index[label], axis] = 1.0
            modes.append(mode)
            mode_names.append((label, name))
    modes = np.asarray(modes)

    face_keys = sorted(source_mechanics.face_decisions)
    vertex_keys = sorted(source_mechanics.vertex_decisions)
    edge_keys = sorted(source_mechanics.edge_decisions)
    keys = (
        [("S", key) for key in face_keys]
        + [("U", key) for key in vertex_keys]
        + [("H", key) for key in edge_keys]
    )
    key_index = {key: offset for offset, key in enumerate(keys)}
    source_vector = mechanics_vector(
        source_mechanics, face_keys, vertex_keys, edge_keys
    )

    mechanics_step = 1e-10
    mechanics_jacobian = np.asarray(
        [
            (
                mechanics_vector(
                    evaluate(labels, points + mechanics_step * mode),
                    face_keys,
                    vertex_keys,
                    edge_keys,
                )
                - mechanics_vector(
                    evaluate(labels, points - mechanics_step * mode),
                    face_keys,
                    vertex_keys,
                    edge_keys,
                )
            )
            / (2 * mechanics_step)
            for mode in modes
        ]
    ).T
    numerator_jacobian = np.asarray(
        [
            (
                carrier_numerators(labels, points + mechanics_step * mode)
                - carrier_numerators(labels, points - mechanics_step * mode)
            )
            / (2 * mechanics_step)
            for mode in modes
        ]
    ).T

    near_support, all_support = support_specs(
        labels, points, faces, source_mechanics.centroid
    )
    support_step = 1e-6
    support_jacobian = np.asarray(
        [
            (
                support_values(
                    labels, points + support_step * mode, faces, near_support
                )
                - support_values(
                    labels, points - support_step * mode, faces, near_support
                )
            )
            / (2 * support_step)
            for mode in modes
        ]
    ).T

    inequalities = []
    inequality_names = []
    for key in TARGETS[:3]:
        inequalities.append(mechanics_jacobian[key_index[key]])
        inequality_names.append(["target_nonincrease", list(key)])
    for key in (("S", tuple(sorted(BASE))), ("U", 8)):
        inequalities.append(-mechanics_jacobian[key_index[key]])
        inequality_names.append(["protected_nondecrease", list(key)])
    for offset, (key, value) in enumerate(zip(keys, source_vector)):
        if value < 0 and (value > -0.1 or key == ("H", (8, 245))):
            inequalities.append(mechanics_jacobian[offset])
            inequality_names.append(["birth_inward", list(key), float(value)])
    for row, spec in zip(support_jacobian, near_support):
        inequalities.append(-row)
        inequality_names.append(
            ["support_inward", spec[0], labels[spec[1]], spec[3]]
        )
    # Keep N10R initially inward so the second saddle is not invited by the
    # first jet.  Its eventual nonlinear reversal is the event being audited.
    inequalities.append(-numerator_jacobian[1])
    inequality_names.append(["N10R_nondecrease"])
    inequalities = np.asarray(inequalities)
    zero_rhs = np.zeros(len(inequalities))

    h910_row = mechanics_jacobian[key_index[("H", (9, 10))]]
    first = linprog(
        h910_row,
        A_ub=inequalities,
        b_ub=zero_rhs,
        bounds=[(-1, 1)] * len(modes),
        method="highs",
    )
    if not first.success:
        raise AssertionError(first.message)

    determinant_step = 1e-6
    quad_jacobian = np.asarray(
        [
            (
                determinant(points + determinant_step * mode, index, OLD_QUAD)
                - determinant(points - determinant_step * mode, index, OLD_QUAD)
            )
            / (2 * determinant_step)
            for mode in modes
        ]
    )
    second = linprog(
        -quad_jacobian,
        A_ub=np.vstack((inequalities, h910_row)),
        b_ub=np.r_[zero_rhs, 0.55 * first.fun],
        bounds=[(-1, 1)] * len(modes),
        method="highs",
    )
    if not second.success:
        raise AssertionError(second.message)

    float_velocity = np.tensordot(second.x, modes, axes=(0, 0))
    physical_norm = max(np.linalg.norm(row) for row in float_velocity)
    float_velocity /= physical_norm
    velocity, base_coefficients = exactify_velocity(
        exact_rows, labels, float_velocity
    )
    rational_velocity_float = np.asarray(
        [[float(value) for value in velocity[label]] for label in labels]
    )

    def points_at(parameter):
        return points + parameter * rational_velocity_float

    def numerator(parameter, which):
        return carrier_numerators(labels, points_at(parameter))[which]

    root_r = brentq(lambda value: numerator(value, 1), 0.0, float(END_PARAMETER))
    root_l = brentq(lambda value: numerator(value, 0), 0.0, float(END_PARAMETER))
    if not root_r < root_l:
        raise AssertionError((root_r, root_l))

    samples = []
    expected_signature = (
        source_mechanics.vertices,
        source_mechanics.edges,
        source_mechanics.faces,
    )
    minimum_support = float("inf")
    for parameter in np.linspace(0.0, float(END_PARAMETER), 161):
        if abs(parameter - root_r) < 5e-8 or abs(parameter - root_l) < 5e-8:
            continue
        sample_points = points_at(parameter)
        mechanics = evaluate(labels, sample_points)
        if (mechanics.vertices, mechanics.edges, mechanics.faces) != expected_signature:
            raise AssertionError(("support changed", parameter, mechanics))
        support_here = support_values(labels, sample_points, faces, all_support)
        if np.min(support_here) <= 0:
            raise AssertionError(("support sign changed", parameter))
        minimum_support = min(minimum_support, float(np.min(support_here)))
        samples.append(
            {
                "parameter": float(parameter),
                "class": list(mechanics.cls),
                "stable_faces": [list(face) for face in mechanics.stable_faces],
                "unstable_vertices": mechanics.unstable_vertices,
                "saddle_edges": [list(edge) for edge in mechanics.saddle_edges],
            }
        )

    sample_parameters = {
        "pre": Q(format(root_r - 1e-6, ".17g")),
        "middle": Q(format((root_r + root_l) / 2, ".17g")),
        "far": END_PARAMETER,
    }
    sample_classes = {}
    sample_residuals = {}
    for name, parameter in sample_parameters.items():
        mechanics = evaluate(labels, points_at(float(parameter)))
        sample_classes[name] = list(mechanics.cls)
        sample_residuals[name] = {
            "S": mechanics.face_decisions.get(PRIMARY),
            "U54": mechanics.vertex_decisions.get(54),
            "H56": mechanics.edge_decisions.get((5, 6)),
            "H910": mechanics.edge_decisions.get((9, 10)),
            "H1011": mechanics.edge_decisions.get((10, 11)),
        }
    if sample_classes != {
        "pre": [2, 2, 2],
        "middle": [2, 3, 3],
        "far": [2, 2, 2],
    }:
        raise AssertionError(sample_classes)

    payload = {
        "version": 1,
        "scope": (
            "Literal rational affine path from the exact Stage-31 FAR/H56 "
            "checkpoint through the first H910-to-H1011 own-centroid carrier relay"
        ),
        "source": str(SOURCE.relative_to(ROOT)),
        "source_faces": str(FACES_PATH.relative_to(ROOT)),
        "end_parameter": str(END_PARAMETER),
        "velocity": {
            str(label): [str(value) for value in velocity[label]]
            for label in labels
        },
        "base_velocity_coefficients": base_coefficients,
        "numerical_proposer": {
            "mode_count": len(modes),
            "mode_names": [list(row) for row in mode_names],
            "near_support_constraint_count": len(near_support),
            "total_support_row_count": len(all_support),
            "inequality_count": len(inequalities),
            "first_lp_h910_rate": float(first.fun),
            "retained_first_lp_fraction": 0.55,
            "second_lp_h910_rate": float(h910_row @ second.x),
            "second_lp_old_quad_rate": float(quad_jacobian @ second.x),
            "physical_normalization": float(physical_norm),
            "root_estimates": {"N10R": root_r, "N10L": root_l},
            "root_gap_N10L_minus_N10R": root_l - root_r,
            "sample_count": len(samples),
            "minimum_sampled_support_margin": minimum_support,
        },
        "rational_samples": {key: str(value) for key, value in sample_parameters.items()},
        "sample_classes": sample_classes,
        "sample_residuals": sample_residuals,
        "verdict": "DIRECTED_STAGE31_H910_TO_H1011_RELAY_PROPOSAL_PASS",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": payload["verdict"],
        "roots": payload["numerical_proposer"]["root_estimates"],
        "gap": payload["numerical_proposer"]["root_gap_N10L_minus_N10R"],
        "classes": sample_classes,
        "minimum_sampled_support_margin": minimum_support,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
