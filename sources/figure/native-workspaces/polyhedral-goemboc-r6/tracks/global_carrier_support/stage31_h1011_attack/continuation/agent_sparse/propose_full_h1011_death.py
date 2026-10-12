#!/usr/bin/env python3
"""Propose a rational full-control path to the first post-flip H1011 death.

The LP uses the complete 165-dimensional chart: two exact in-base modes for
each enlarged-base row and three Cartesian modes for every nonbase active row.
It drives H(10,11) outward while S(7,8,245), U54, H(5,6), and the already dead
H(9,10) have strict inward first jets.  All nearby forbidden equilibria and
all nearby support inequalities are directed inward.  This script is only a
numerical proposer; exact first-event and continuum claims belong to the exact
builder and its independent verifier.
"""
from __future__ import annotations

import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
from scipy.optimize import brentq, linprog


HERE = Path(__file__).resolve().parent
PARENT = HERE.parents[1]
TRACK = PARENT.parent
ROOT = TRACK.parents[1]
SOURCE = PARENT / "exact_circuit_far.csv"
FACES_PATH = PARENT / "exact_circuit_post_faces.json"
OUTPUT = HERE / "full_h1011_path_definition.json"
POST_FACES = HERE / "full_h1011_post_faces.json"

sys.path.insert(0, str(TRACK))
from actual_hull_mechanics import evaluate  # noqa: E402
sys.path.insert(0, str(PARENT))
import h1011_common as common  # noqa: E402
sys.path.insert(0, str(TRACK / "rigorous_local_bypass"))
import exact_core as ex  # noqa: E402


BASE = common.BASE
BASE_SET = common.BASE_SET
PRIMARY = common.PRIMARY
TARGETS = {
    "S": ("S", PRIMARY),
    "U54": ("U", 54),
    "H56": ("H", (5, 6)),
    "H1011": ("H", (10, 11)),
    "H910": ("H", (9, 10)),
}
RATE_CAP_FACTORS = {
    "S": 1e-2,
    "U54": 1e-2,
    "H56": 1e-2,
    "H910": 5e-2,
}


def positive_roots(polynomial):
    roots = []
    coefficients = np.asarray([float(value) for value in polynomial.c])
    for candidate in np.polynomial.polynomial.polyroots(coefficients):
        if abs(candidate.imag) > 1e-7 * max(1.0, abs(candidate.real)):
            continue
        value = float(candidate.real)
        if value <= 1e-16 or value >= 1.0:
            continue
        epsilon = max(1e-18, value * 1e-7)
        left = polynomial.eval(Q(format(value - epsilon, ".17g")))
        right = polynomial.eval(Q(format(value + epsilon, ".17g")))
        if left * right < 0:
            roots.append(value)
    return sorted(roots)


def forced_rails():
    rails = set()
    for route in (
        [228] + list(range(229, 247)) + [8],
        [228] + list(range(247, 265)) + [8],
    ):
        rails.update(tuple(sorted(edge)) for edge in zip(route, route[1:]))
    rails.remove((228, 229))
    return rails


def edges(faces):
    return {
        tuple(sorted((a, b)))
        for cycle in faces
        for a, b in zip(cycle, cycle[1:] + cycle[:1])
    }


def h1011_numerator(labels, points):
    mechanics = evaluate(labels, points)
    index = {label: offset for offset, label in enumerate(labels)}
    q10 = points[index[10]] - mechanics.centroid
    return -float(np.dot(q10, points[index[11]] - points[index[10]]))


def main():
    exact_rows = common.read_exact_rows(SOURCE)
    labels = sorted(exact_rows)
    index = {label: offset for offset, label in enumerate(labels)}
    points = np.asarray(
        [[float(value) for value in exact_rows[label]] for label in labels]
    )
    faces = json.loads(FACES_PATH.read_text())
    source_mechanics = evaluate(labels, points)
    if source_mechanics.cls != (2, 2, 2):
        raise AssertionError(source_mechanics.cls)
    source_signature = common.full_signature(labels, points, source_mechanics)
    if source_signature["f_vector"] != [61, 162, 103]:
        raise AssertionError(source_signature)

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
    for label in labels:
        if label in BASE_SET:
            continue
        for axis, name in enumerate("xyz"):
            mode = np.zeros_like(points)
            mode[index[label], axis] = 1.0
            modes.append(mode)
            mode_names.append((label, name))
    modes = np.asarray(modes)
    if len(modes) != 165:
        raise AssertionError(len(modes))

    face_keys = sorted(source_mechanics.face_decisions)
    vertex_keys = sorted(source_mechanics.vertex_decisions)
    edge_keys = sorted(source_mechanics.edge_decisions)
    keys = (
        [("S", key) for key in face_keys]
        + [("U", key) for key in vertex_keys]
        + [("H", key) for key in edge_keys]
    )
    key_index = {key: offset for offset, key in enumerate(keys)}
    source_vector = common.mechanics_vector(
        source_mechanics, face_keys, vertex_keys, edge_keys
    )

    mechanics_step = 1e-9
    mechanics_jacobian = np.asarray([
        (
            common.mechanics_vector(
                evaluate(labels, points + mechanics_step * mode),
                face_keys, vertex_keys, edge_keys,
            )
            - common.mechanics_vector(
                evaluate(labels, points - mechanics_step * mode),
                face_keys, vertex_keys, edge_keys,
            )
        ) / (2 * mechanics_step)
        for mode in modes
    ]).T
    numerator_step = 1e-9
    h1011_numerator_row = np.asarray([
        (
            h1011_numerator(labels, points + numerator_step * mode)
            - h1011_numerator(labels, points - numerator_step * mode)
        ) / (2 * numerator_step)
        for mode in modes
    ])

    near_support, all_support = common.support_specs(
        labels, points, faces, source_mechanics.centroid
    )
    support_step = 1e-6
    support_jacobian = np.asarray([
        (
            common.support_values(
                labels, points + support_step * mode, faces, near_support
            )
            - common.support_values(
                labels, points - support_step * mode, faces, near_support
            )
        ) / (2 * support_step)
        for mode in modes
    ]).T

    target_rows = {
        name: mechanics_jacobian[key_index[key]] for name, key in TARGETS.items()
    }
    source_residuals = {
        "S": source_mechanics.face_decisions[PRIMARY],
        "U54": source_mechanics.vertex_decisions[54],
        "H56": source_mechanics.edge_decisions[(5, 6)],
        "H1011": source_mechanics.edge_decisions[(10, 11)],
        "H910": source_mechanics.edge_decisions[(9, 10)],
    }

    inequalities = []
    rhs = []
    constraint_names = []
    for name in ("S", "U54", "H56"):
        cap = -RATE_CAP_FACTORS[name] * abs(source_residuals[name])
        inequalities.append(target_rows[name])
        rhs.append(cap)
        constraint_names.append(["target_inward", name, cap])
    h910_cap = -RATE_CAP_FACTORS["H910"] * abs(source_residuals["H910"])
    inequalities.append(target_rows["H910"])
    rhs.append(h910_cap)
    constraint_names.append(["old_carrier_inward", "H910", h910_cap])

    for key in (("S", tuple(sorted(BASE_SET))), ("U", 8)):
        inequalities.append(-mechanics_jacobian[key_index[key]])
        rhs.append(0.0)
        constraint_names.append(["protected_nondecrease", list(key)])
    for offset, (key, value) in enumerate(zip(keys, source_vector)):
        if value < 0 and value > -0.05 and key != TARGETS["H910"]:
            inequalities.append(mechanics_jacobian[offset])
            rhs.append(0.0)
            constraint_names.append(["forbidden_inward", list(key), float(value)])
    for row, spec in zip(support_jacobian, near_support):
        inequalities.append(-row)
        rhs.append(0.0)
        constraint_names.append(["support_inward", spec[0], labels[spec[1]], spec[3]])

    inequality_matrix = np.asarray(inequalities)
    rhs_vector = np.asarray(rhs)
    attempts = []
    variants = (
        ("strict_tangent", frozenset()),
        ("exact_checked_without_forbidden_tangents", frozenset({"forbidden_inward"})),
        ("exact_checked_without_support_tangents", frozenset({"support_inward"})),
        (
            "exact_checked_endpoint_cone",
            frozenset({"forbidden_inward", "support_inward"}),
        ),
    )
    result = None
    solver_variant = None
    for name, dropped in variants:
        mask = np.asarray([row[0] not in dropped for row in constraint_names])
        candidate = linprog(
            h1011_numerator_row,
            A_ub=inequality_matrix[mask],
            b_ub=rhs_vector[mask],
            bounds=[(-1, 1)] * len(modes),
            method="highs",
        )
        attempts.append({
            "name": name,
            "dropped_constraint_families": sorted(dropped),
            "constraint_count": int(np.sum(mask)),
            "success": bool(candidate.success),
            "objective": float(candidate.fun) if candidate.fun is not None else None,
            "message": candidate.message,
        })
        if candidate.success and candidate.fun < 0:
            result = candidate
            solver_variant = name
            break
    if result is None:
        raise AssertionError(("no negative H1011 rate", attempts))

    float_velocity = np.tensordot(result.x, modes, axes=(0, 0))
    physical_norm = max(np.linalg.norm(row) for row in float_velocity)
    float_velocity /= physical_norm
    velocity, base_coefficients = common.exactify_velocity(
        exact_rows, labels, float_velocity
    )
    rational_velocity = np.asarray([
        [float(value) for value in velocity[label]] for label in labels
    ])
    exact_path = {
        label: tuple(
            ex.P((exact_rows[label][axis], velocity[label][axis]))
            for axis in range(3)
        )
        for label in labels
    }
    ledger = ex.mechanics_primitives(exact_path, faces)
    event_polynomial = ledger["edge"][(10, 11)]["t"]
    if event_polynomial != ledger["vertex"][10][11]:
        raise AssertionError("H1011/U10 exact endpoint identity failed")
    roots = positive_roots(event_polynomial)
    if not roots:
        floating_roots = np.polynomial.polynomial.polyroots(
            np.asarray([float(value) for value in event_polynomial.c])
        )
        raise AssertionError({
            "reason": "rationalized H1011 path has no positive death root in (0,1)",
            "event_polynomial_degree": event_polynomial.degree,
            "event_polynomial_exact": event_polynomial.exact(),
            "value_at_zero": str(event_polynomial.eval(Q(0))),
            "derivative_at_zero": str(event_polynomial.derivative().eval(Q(0))),
            "floating_roots": [[float(root.real), float(root.imag)] for root in floating_roots],
            "solver_variant": solver_variant,
            "physical_normalization": physical_norm,
        })
    root_estimate = roots[0]

    def points_at(parameter):
        return points + parameter * rational_velocity

    def h1011(parameter):
        mechanics = evaluate(labels, points_at(parameter))
        return mechanics.edge_decisions[(10, 11)]

    root_numeric = brentq(
        h1011, root_estimate * (1 - 1e-5), root_estimate * (1 + 1e-5)
    )
    if abs(root_numeric - root_estimate) > max(1e-14, root_estimate * 1e-6):
        raise AssertionError((root_estimate, root_numeric))

    next_support = 1.0
    earlier_support = []
    for face_index, witness, polynomial in ex.support_polynomials(exact_path, faces):
        for root in positive_roots(polynomial):
            if root < root_estimate * (1 - 1e-7):
                earlier_support.append((root, face_index, witness))
            if root > root_estimate * (1 + 1e-7):
                next_support = min(next_support, root)
    if earlier_support:
        raise AssertionError(("support before H1011 death", sorted(earlier_support)[:10]))

    post_gap = min(root_estimate * 1e-2, (next_support - root_estimate) / 10)
    if post_gap <= 0:
        raise AssertionError((root_estimate, next_support))
    end_parameter = Q(format(root_estimate + post_gap, ".17g"))
    pre_parameter = root_estimate * 0.98
    for parameter in np.linspace(0.0, pre_parameter, 121):
        current = evaluate(labels, points_at(parameter))
        if common.full_signature(labels, points_at(parameter), current) != source_signature:
            raise AssertionError(("event before H1011 death", parameter, common.signature(current)))

    end_points = points_at(float(end_parameter))
    end_mechanics = evaluate(labels, end_points)
    end_signature = common.full_signature(labels, end_points, end_mechanics)
    if end_signature["maximal_faces"] != source_signature["maximal_faces"]:
        raise AssertionError(("support changed", end_signature))
    if end_mechanics.cls != (2, 2, 1):
        raise AssertionError(common.signature(end_mechanics))
    if end_mechanics.edge_decisions[(9, 10)] >= 0:
        raise AssertionError(("H910 returned", end_mechanics.edge_decisions[(9, 10)]))
    if end_signature["active_labels"] != source_signature["active_labels"]:
        raise AssertionError("active rows changed")
    if not forced_rails().issubset(edges(common.actual_faces(labels, end_points))):
        raise AssertionError("forced rail lost")

    end_residuals = {
        "S": end_mechanics.face_decisions[PRIMARY],
        "U54": end_mechanics.vertex_decisions[54],
        "H56": end_mechanics.edge_decisions[(5, 6)],
        "H1011": end_mechanics.edge_decisions[(10, 11)],
        "H910": end_mechanics.edge_decisions[(9, 10)],
    }
    for name in ("S", "U54", "H56"):
        if end_residuals[name] >= source_residuals[name]:
            raise AssertionError(("target did not improve", name, source_residuals[name], end_residuals[name]))
    if end_residuals["H1011"] >= 0:
        raise AssertionError(("H1011 did not die", end_residuals["H1011"]))

    post_faces = common.actual_faces(labels, end_points)
    POST_FACES.write_text(json.dumps(post_faces, indent=2) + "\n")
    nonzero_modes = [
        [list(mode_names[offset]), float(coefficient)]
        for offset, coefficient in enumerate(result.x)
        if abs(coefficient) > 1e-10
    ]
    payload = {
        "version": 1,
        "scope": (
            "Literal rational full-control path from the exact post-flip H1011 "
            "cell through the first H1011 mechanics death"
        ),
        "source": str(SOURCE.relative_to(ROOT)),
        "source_faces": str(FACES_PATH.relative_to(ROOT)),
        "end_parameter": str(end_parameter),
        "velocity": {
            str(label): [str(value) for value in velocity[label]] for label in labels
        },
        "base_velocity_coefficients": base_coefficients,
        "numerical_proposer": {
            "mode_count": len(modes),
            "nonzero_mode_count": len(nonzero_modes),
            "nonzero_modes": nonzero_modes,
            "constraint_count": len(inequalities),
            "solver_variant": solver_variant,
            "solver_attempts": attempts,
            "near_support_constraint_count": len(near_support),
            "total_support_row_count": len(all_support),
            "lp_h1011_rate": float(result.fun),
            "lp_normalized_h1011_rate": float(target_rows["H1011"] @ result.x),
            "physical_normalization": physical_norm,
            "root_estimate": root_estimate,
            "next_support_root_lower_estimate": next_support,
        },
        "source_signature": source_signature,
        "source_residuals": source_residuals,
        "post_signature": end_signature,
        "post_residuals": end_residuals,
        "event_identity": "vertex:10:11 == edge:(10,11):t",
        "verdict": "DIRECTED_FULL_CONTROL_H1011_DEATH_PROPOSAL_PASS",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": payload["verdict"],
        "root_estimate": root_estimate,
        "mode_count": len(modes),
        "nonzero_mode_count": len(nonzero_modes),
        "classes": [list(source_mechanics.cls), list(end_mechanics.cls)],
        "source_residuals": source_residuals,
        "post_residuals": end_residuals,
        "next_support_root_lower_estimate": next_support,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
