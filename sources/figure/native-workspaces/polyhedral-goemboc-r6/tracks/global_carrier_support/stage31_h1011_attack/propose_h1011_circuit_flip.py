#!/usr/bin/env python3
"""Propose a short H1011-local circuit flip with all four defects inward.

The target wall is the actual four-point support circuit (8,9,263,264),
immediately upstream of the new H(10,11) carrier.  The numerical LP removes only the two
support inequalities proportional to that wall, keeps every other nearby
support inequality inward, and imposes strict negative first jets for
S(7,8,245), U54, H(5,6), H(10,11), and the extinct H(9,10).  Its rationalized
path is merely a proposal; exact first-wall and mechanics proofs are built by
separate code.
"""
from __future__ import annotations

import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


HERE = Path(__file__).resolve().parent
TRACK = HERE.parent
ROOT = HERE.parents[2]
SOURCE = TRACK / "stage31_attack" / "exact_relay_far.csv"
FACES_PATH = TRACK / "stage31_attack" / "exact_relay_faces.json"
OUTPUT = HERE / "circuit_path_definition.json"
POST_FACES = HERE / "circuit_post_faces.json"

sys.path.insert(0, str(TRACK))
from actual_hull_mechanics import evaluate  # noqa: E402
sys.path.insert(0, str(HERE))
import h1011_common as common  # noqa: E402
sys.path.insert(0, str(TRACK / "rigorous_local_bypass"))
import exact_core as ex  # noqa: E402


BASE = common.BASE
BASE_SET = common.BASE_SET
CARRIER_ROWS = common.CARRIER_ROWS
PRIMARY = common.PRIMARY
TARGET_CIRCUIT = (8, 9, 263, 264)
TARGET_FAMILY = {
    (frozenset((8, 9, 264)), 263),
    (frozenset((9, 263, 264)), 8),
}
TARGET_RATE_CAPS = {
    "S": -1e-6,
    "U54": -1e-4,
    "H56": -1e-4,
    "H1011": -1e-8,
    "H910": -1e-6,
}


def determinant(points, index, circuit):
    rows = np.c_[points[[index[label] for label in circuit]], np.ones(4)]
    return float(np.linalg.det(rows))


def exact_positive_roots(polynomial):
    roots = []
    coefficients = np.asarray([float(value) for value in polynomial.c])
    for candidate in np.polynomial.polynomial.polyroots(coefficients):
        if abs(candidate.imag) > 1e-7 * max(1.0, abs(candidate.real)):
            continue
        value = float(candidate.real)
        if value <= 1e-12 or value >= 1.0:
            continue
        epsilon = max(1e-14, value * 1e-7)
        left = polynomial.eval(Q(format(value - epsilon, ".17g")))
        right = polynomial.eval(Q(format(value + epsilon, ".17g")))
        if left * right < 0:
            roots.append(value)
    return sorted(roots)


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
        "S": mechanics_jacobian[key_index[("S", PRIMARY)]],
        "U54": mechanics_jacobian[key_index[("U", 54)]],
        "H56": mechanics_jacobian[key_index[("H", (5, 6))]],
        "H1011": mechanics_jacobian[key_index[("H", (10, 11))]],
        "H910": mechanics_jacobian[key_index[("H", (9, 10))]],
    }
    inequalities = []
    rhs = []
    names = []
    for name, row in target_rows.items():
        inequalities.append(row)
        rhs.append(TARGET_RATE_CAPS[name])
        names.append(["directed_target", name, TARGET_RATE_CAPS[name]])
    for key in (("S", tuple(sorted(BASE_SET))), ("U", 8)):
        inequalities.append(-mechanics_jacobian[key_index[key]])
        rhs.append(0.0)
        names.append(["protected_nondecrease", list(key)])
    for offset, (key, value) in enumerate(zip(keys, source_vector)):
        if value < 0 and value > -0.05 and key != ("H", (9, 10)):
            inequalities.append(mechanics_jacobian[offset])
            rhs.append(0.0)
            names.append(["forbidden_inward", list(key), float(value)])

    removed_support = []
    for row, spec in zip(support_jacobian, near_support):
        family_key = (frozenset(faces[spec[0]]), labels[spec[1]])
        if family_key in TARGET_FAMILY:
            removed_support.append({
                "face_index": spec[0],
                "face": faces[spec[0]],
                "witness": labels[spec[1]],
                "source_margin": spec[3],
            })
            continue
        inequalities.append(-row)
        rhs.append(0.0)
        names.append(["support_inward", spec[0], labels[spec[1]], spec[3]])
    if {(frozenset(row["face"]), row["witness"]) for row in removed_support} != TARGET_FAMILY:
        raise AssertionError(("target support family missing", removed_support))

    determinant_step = 1e-6
    circuit_gradient = np.asarray([
        (
            determinant(points + determinant_step * mode, index, TARGET_CIRCUIT)
            - determinant(points - determinant_step * mode, index, TARGET_CIRCUIT)
        ) / (2 * determinant_step)
        for mode in modes
    ])
    circuit_source = determinant(points, index, TARGET_CIRCUIT)
    circuit_sign = 1 if circuit_source > 0 else -1
    result = linprog(
        circuit_sign * circuit_gradient,
        A_ub=np.asarray(inequalities),
        b_ub=np.asarray(rhs),
        bounds=[(-1, 1)] * len(modes),
        method="highs",
    )
    if not result.success or result.fun >= 0:
        raise AssertionError((result.message, result.fun))

    float_velocity = np.tensordot(result.x, modes, axes=(0, 0))
    physical_norm = max(np.linalg.norm(row) for row in float_velocity)
    float_velocity /= physical_norm
    velocity, base_coefficients = common.exactify_velocity(
        exact_rows, labels, float_velocity
    )
    rational_velocity_float = np.asarray(
        [[float(value) for value in velocity[label]] for label in labels]
    )
    exact_path = {
        label: tuple(
            ex.P((exact_rows[label][axis], velocity[label][axis]))
            for axis in range(3)
        )
        for label in labels
    }
    target_polynomial = ex.circuit_polynomial(exact_path, TARGET_CIRCUIT)
    target_roots = exact_positive_roots(target_polynomial)
    if not target_roots:
        raise AssertionError("rationalized target circuit does not cross")
    root_estimate = target_roots[0]

    earlier_support = []
    next_support = 1.0
    for face_index, witness, polynomial in ex.support_polynomials(exact_path, faces):
        ratio = ex.proportional(polynomial, target_polynomial)
        for root in exact_positive_roots(polynomial):
            if ratio is None and root < root_estimate * (1 - 1e-7):
                earlier_support.append((root, face_index, witness))
            if ratio is None and root > root_estimate * (1 + 1e-7):
                next_support = min(next_support, root)
    if earlier_support:
        raise AssertionError(("earlier support wall", sorted(earlier_support)[:10]))

    post_gap = min(root_estimate * 1e-2, (next_support - root_estimate) / 10)
    if post_gap <= 0:
        raise AssertionError((root_estimate, next_support))
    end_parameter = Q(format(root_estimate + post_gap, ".17g"))

    def points_at(parameter):
        return points + parameter * rational_velocity_float

    pre_parameter = root_estimate * 0.98
    for parameter in np.linspace(0.0, pre_parameter, 101):
        mechanics = evaluate(labels, points_at(parameter))
        if mechanics.cls != (2, 2, 2):
            raise AssertionError(("earlier mechanics event", parameter, common.signature(mechanics)))
    end_points = points_at(float(end_parameter))
    end_mechanics = evaluate(labels, end_points)
    post_faces = common.actual_faces(labels, end_points)
    POST_FACES.write_text(json.dumps(post_faces, indent=2) + "\n")

    source_residuals = {
        "S": source_mechanics.face_decisions[PRIMARY],
        "U54": source_mechanics.vertex_decisions[54],
        "H56": source_mechanics.edge_decisions[(5, 6)],
        "H1011": source_mechanics.edge_decisions[(10, 11)],
        "H910": source_mechanics.edge_decisions[(9, 10)],
    }
    end_residuals = {
        "S": end_mechanics.face_decisions.get(PRIMARY),
        "U54": end_mechanics.vertex_decisions.get(54),
        "H56": end_mechanics.edge_decisions.get((5, 6)),
        "H1011": end_mechanics.edge_decisions.get((10, 11)),
        "H910": end_mechanics.edge_decisions.get((9, 10)),
    }
    for name in ("S", "U54", "H56", "H1011"):
        if end_residuals[name] is None or end_residuals[name] > source_residuals[name]:
            raise AssertionError(("target did not improve", name, source_residuals[name], end_residuals[name]))
    if end_residuals["H910"] is None or end_residuals["H910"] >= 0:
        raise AssertionError(("H910 returned", source_residuals["H910"], end_residuals["H910"]))

    source_face_sets = {tuple(sorted(face)) for face in faces}
    post_face_sets = {tuple(sorted(face)) for face in post_faces}
    payload = {
        "version": 1,
        "scope": (
            "Literal rational short path from the exact H1011 far cell through "
            "the first H1011-upstream support circuit (8,9,263,264)"
        ),
        "source": str(SOURCE.relative_to(ROOT)),
        "source_faces": str(FACES_PATH.relative_to(ROOT)),
        "target_circuit": list(TARGET_CIRCUIT),
        "end_parameter": str(end_parameter),
        "velocity": {
            str(label): [str(value) for value in velocity[label]] for label in labels
        },
        "base_velocity_coefficients": base_coefficients,
        "numerical_proposer": {
            "mode_count": len(modes),
            "mode_names": [list(row) for row in mode_names],
            "target_rate_caps": TARGET_RATE_CAPS,
            "constraint_count": len(inequalities),
            "removed_target_support_family": removed_support,
            "circuit_source": circuit_source,
            "circuit_lp_rate": float(result.fun),
            "physical_normalization": physical_norm,
            "root_estimate": root_estimate,
            "next_support_root_lower_estimate": next_support,
        },
        "source_class": list(source_mechanics.cls),
        "post_class": list(end_mechanics.cls),
        "source_residuals": source_residuals,
        "post_residuals": end_residuals,
        "removed_faces": [list(face) for face in sorted(source_face_sets - post_face_sets)],
        "added_faces": [list(face) for face in sorted(post_face_sets - source_face_sets)],
        "verdict": "DIRECTED_STAGE31_H1011_LOCAL_CIRCUIT_PROPOSAL_PASS",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": payload["verdict"],
        "root_estimate": root_estimate,
        "classes": [payload["source_class"], payload["post_class"]],
        "source_residuals": source_residuals,
        "post_residuals": end_residuals,
        "removed_faces": payload["removed_faces"],
        "added_faces": payload["added_faces"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
