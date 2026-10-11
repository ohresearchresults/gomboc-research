#!/usr/bin/env python3
"""Full-control actual-cell descent from the exact H1011 post-flip far cell.

This is a numerical proposer only.  It uses every physical tangent coordinate:
two in the frozen enlarged-base plane for each base vertex and three Cartesian
coordinates for every other active row.  A trust-bounded LP maximizes common
fractional descent of S/U54/H56/H1011 while H910 is pushed farther outward,
the enlarged base and U8 do not worsen, every other equilibrium decision keeps
a strict signed guard, and every near support inequality keeps a strict guard.

The accepted rational direction is subsequently audited by exact polynomial
first jets.  Event isolation and interval certification are deliberately left
to a separate exact builder/verifier.
"""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


HERE = Path(__file__).resolve().parent
ATTACK = HERE.parents[1]
TRACK = ATTACK.parent
ROOT = HERE.parents[4]
SOURCE = ATTACK / "exact_circuit_far.csv"
FACES_PATH = ATTACK / "exact_circuit_post_faces.json"
OUTPUT = HERE / "full_control_proposal.json"
ENDPOINT = HERE / "full_control_candidate.csv"

sys.path.insert(0, str(TRACK))
sys.path.insert(0, str(ATTACK))
import h1011_common as common  # noqa: E402
import build_exact_circuit_flip as frozen_builder  # noqa: E402
from actual_hull_mechanics import evaluate  # noqa: E402
sys.path.insert(0, str(TRACK / "rigorous_local_bypass"))
import exact_core as ex  # noqa: E402


TARGET_KEYS = {
    "S": ("S", common.PRIMARY),
    "U54": ("U", 54),
    "H56": ("H", (5, 6)),
    "H1011": ("H", (10, 11)),
}
H910_KEY = ("H", (9, 10))
PROTECTED_KEYS = {
    ("S", tuple(sorted(common.BASE_SET))),
    ("U", 8),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_exact_csv(path: Path, rows) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(("source_id", "x", "y", "z"))
        for label in sorted(rows):
            writer.writerow((label, *(str(value) for value in rows[label])))


def face_sets(faces):
    return {tuple(sorted(face)) for face in faces}


def signature(mechanics):
    return {
        "f_vector": [mechanics.vertices, mechanics.edges, mechanics.faces],
        "class": list(mechanics.cls),
        "stable_faces": sorted(sorted(face) for face in mechanics.stable_faces),
        "unstable_vertices": sorted(mechanics.unstable_vertices),
        "saddle_edges": sorted(sorted(edge) for edge in mechanics.saddle_edges),
        "active_labels": list(mechanics.active_labels),
    }


def build_modes(labels, points):
    index = {label: offset for offset, label in enumerate(labels)}
    plane_u = points[index[1]] - points[index[0]]
    plane_u /= np.linalg.norm(plane_u)
    plane_normal = np.cross(plane_u, points[index[2]] - points[index[0]])
    plane_normal /= np.linalg.norm(plane_normal)
    plane_v = np.cross(plane_normal, plane_u)
    plane_v /= np.linalg.norm(plane_v)
    modes = []
    names = []
    for label in labels:
        if label in common.BASE_SET:
            directions = (("u", plane_u), ("v", plane_v))
        else:
            directions = tuple(
                (name, np.eye(3)[axis]) for axis, name in enumerate("xyz")
            )
        for name, direction in directions:
            mode = np.zeros_like(points)
            mode[index[label]] = direction
            modes.append(mode)
            names.append((label, name))
    return np.asarray(modes), names, plane_normal


def mechanics_vector(mechanics, face_keys, vertex_keys, edge_keys):
    return np.asarray(
        [mechanics.face_decisions[key] for key in face_keys]
        + [mechanics.vertex_decisions[key] for key in vertex_keys]
        + [mechanics.edge_decisions[key] for key in edge_keys],
        dtype=float,
    )


def central_mechanics_jacobian(labels, points, modes, source, keys, initial=1e-8):
    source_faces = common.full_signature(labels, points, source)["maximal_faces"]
    columns = []
    diagnostics = []
    for column, mode in enumerate(modes):
        failures = []
        accepted = None
        for reduction in range(10):
            step = initial / (4.0 ** reduction)
            try:
                plus = evaluate(labels, points + step * mode)
                minus = evaluate(labels, points - step * mode)
                if list(plus.active_labels) != list(source.active_labels):
                    raise RuntimeError("plus active labels changed")
                if list(minus.active_labels) != list(source.active_labels):
                    raise RuntimeError("minus active labels changed")
                if common.full_signature(labels, points + step * mode, plus)["maximal_faces"] != source_faces:
                    raise RuntimeError("plus maximal faces changed")
                if common.full_signature(labels, points - step * mode, minus)["maximal_faces"] != source_faces:
                    raise RuntimeError("minus maximal faces changed")
                plus_vector = mechanics_vector(plus, *keys)
                minus_vector = mechanics_vector(minus, *keys)
                columns.append((plus_vector - minus_vector) / (2 * step))
                accepted = step
                break
            except Exception as error:  # every rejected scale is evidence
                failures.append({"step": step, "error": repr(error)})
        if accepted is None:
            raise RuntimeError(("central derivative failed", column, failures))
        if failures:
            diagnostics.append({
                "column": column,
                "accepted_step": accepted,
                "rejected_scales": failures,
            })
    return np.asarray(columns).T, diagnostics


def support_jacobian(labels, points, faces, specs, modes, step=1e-7):
    columns = []
    for mode in modes:
        plus = common.support_values(labels, points + step * mode, faces, specs)
        minus = common.support_values(labels, points - step * mode, faces, specs)
        columns.append((plus - minus) / (2 * step))
    return np.asarray(columns).T


def exact_first_jet(path, faces, name):
    numerator, denominator = frozen_builder.selected_fraction_polynomials(
        path, faces, name
    )
    derivative = numerator.derivative() * denominator - numerator * denominator.derivative()
    value = derivative.eval(Q(0))
    if value >= 0:
        raise AssertionError(("nonnegative exact selected first jet", name, value))
    return {
        "degree": derivative.degree,
        "value": ex.qs(value),
        "polynomial_digest": hashlib.sha256(
            "|".join(derivative.exact()).encode()
        ).hexdigest(),
    }


def main():
    exact_rows = ex.read_rows(SOURCE)
    labels = sorted(exact_rows)
    points = np.asarray(
        [[float(value) for value in exact_rows[label]] for label in labels],
        dtype=float,
    )
    faces = json.loads(FACES_PATH.read_text())
    source = evaluate(labels, points)
    if signature(source)["f_vector"] != [61, 162, 103]:
        raise AssertionError(signature(source))
    if source.cls != (2, 2, 2):
        raise AssertionError(signature(source))
    if face_sets(common.actual_faces(labels, points)) != face_sets(faces):
        raise AssertionError("saved post faces differ from fresh actual hull")

    modes, mode_names, plane_normal = build_modes(labels, points)
    face_keys = sorted(source.face_decisions)
    vertex_keys = sorted(source.vertex_decisions)
    edge_keys = sorted(source.edge_decisions)
    key_groups = (face_keys, vertex_keys, edge_keys)
    keys = (
        [("S", key) for key in face_keys]
        + [("U", key) for key in vertex_keys]
        + [("H", key) for key in edge_keys]
    )
    key_index = {key: offset for offset, key in enumerate(keys)}
    source_vector = mechanics_vector(source, *key_groups)
    mechanics_jacobian, fd_diagnostics = central_mechanics_jacobian(
        labels, points, modes, source, key_groups
    )

    # All support rows are audited.  Only the numerically near rows enter the
    # LP guard; the exact builder later checks all 5,959 polynomials.
    near_support, all_support = common.support_specs(
        labels, points, faces, source.centroid, threshold=2e-3
    )
    support_source = np.asarray([row[3] for row in near_support])
    support_derivative = support_jacobian(
        labels, points, faces, near_support, modes
    )

    displacement = np.asarray([
        [mode[offset, axis] for mode in modes]
        for offset in range(len(labels)) for axis in range(3)
    ])
    trust_values = (2e-8, 5e-8, 1e-7, 2e-7, 5e-7, 1e-6)
    branches = []
    best = None
    for trust in trust_values:
        rows = []
        rhs = []
        names = []
        # Variables are chart coefficients followed by common fractional
        # descent q.  Each target satisfies d(value)/value + q <= 0.
        for name, key in TARGET_KEYS.items():
            value = source_vector[key_index[key]]
            if value <= 0:
                raise AssertionError((name, value))
            row = mechanics_jacobian[key_index[key]] / value
            rows.append(np.r_[row, 1.0])
            rhs.append(0.0)
            names.append(("target", name))

        # H910 is already dead and is pushed strictly farther from zero.
        h910_value = source_vector[key_index[H910_KEY]]
        if h910_value >= 0:
            raise AssertionError(("H910 resurrected at source", h910_value))
        rows.append(np.r_[mechanics_jacobian[key_index[H910_KEY]], 0.0])
        rhs.append(-1e-10)
        names.append(("dead_inward", "H910"))

        # The enlarged stable base and U8 may not worsen at first order.
        for key in sorted(PROTECTED_KEYS, key=repr):
            rows.append(np.r_[-mechanics_jacobian[key_index[key]], 0.0])
            rhs.append(0.0)
            names.append(("protected_nondecrease", repr(key)))

        # Keep every non-target equilibrium decision on its current strict side
        # by at least 80% of its present decision margin under the LP step.
        exempt = set(TARGET_KEYS.values()) | {H910_KEY} | PROTECTED_KEYS
        for offset, (key, value) in enumerate(zip(keys, source_vector)):
            if key in exempt:
                continue
            sign = 1.0 if value > 0 else -1.0
            rows.append(np.r_[-sign * mechanics_jacobian[offset], 0.0])
            rhs.append(0.2 * abs(value))
            names.append(("mechanics_guard", repr(key), float(value)))

        # No near support slack may lose more than 20% in one accepted step.
        for offset, (spec, margin) in enumerate(zip(near_support, support_source)):
            rows.append(np.r_[-support_derivative[offset], 0.0])
            rhs.append(0.2 * margin)
            names.append(("support_guard", spec[0], labels[spec[1]], float(margin)))

        # Physical L-infinity trust, independent of chart conditioning.
        rows.extend(np.c_[displacement, np.zeros(displacement.shape[0])])
        rhs.extend(np.full(displacement.shape[0], trust))
        names.extend(("physical_trust_plus", index) for index in range(displacement.shape[0]))
        rows.extend(np.c_[-displacement, np.zeros(displacement.shape[0])])
        rhs.extend(np.full(displacement.shape[0], trust))
        names.extend(("physical_trust_minus", index) for index in range(displacement.shape[0]))

        lp = linprog(
            np.r_[np.zeros(len(modes)), -1.0],
            A_ub=np.asarray(rows),
            b_ub=np.asarray(rhs),
            bounds=[(-1000.0, 1000.0)] * len(modes) + [(0.0, 1.0)],
            method="highs",
        )
        record = {
            "trust": trust,
            "success": bool(lp.success),
            "message": lp.message,
            "constraint_count": len(rows),
        }
        if lp.success:
            coefficients = np.asarray(lp.x[:-1])
            delta = np.tensordot(coefficients, modes, axes=(0, 0))
            endpoint = points + delta
            try:
                endpoint_mechanics = evaluate(labels, endpoint)
                endpoint_faces = common.actual_faces(labels, endpoint)
                endpoint_signature = signature(endpoint_mechanics)
                same_cell = (
                    face_sets(endpoint_faces) == face_sets(faces)
                    and endpoint_signature["class"] == [2, 2, 2]
                    and endpoint_signature["stable_faces"] == signature(source)["stable_faces"]
                    and endpoint_signature["unstable_vertices"] == signature(source)["unstable_vertices"]
                    and endpoint_signature["saddle_edges"] == signature(source)["saddle_edges"]
                )
                endpoint_values = mechanics_vector(endpoint_mechanics, *key_groups)
                ratios = {
                    name: float(endpoint_values[key_index[key]] / source_vector[key_index[key]])
                    for name, key in TARGET_KEYS.items()
                }
                h910_endpoint = float(endpoint_values[key_index[H910_KEY]])
            except Exception as error:
                endpoint_signature = None
                same_cell = False
                ratios = {}
                h910_endpoint = None
                record["endpoint_error"] = repr(error)
            record.update({
                "common_fractional_descent": float(lp.x[-1]),
                "physical_linf": float(np.max(np.abs(delta))),
                "same_actual_cell": same_cell,
                "endpoint_signature": endpoint_signature,
                "target_ratios": ratios,
                "h910_endpoint": h910_endpoint,
                "active_modes": [
                    {
                        "column": int(index),
                        "label": mode_names[index][0],
                        "axis": mode_names[index][1],
                        "coefficient": float(coefficients[index]),
                    }
                    for index in np.argsort(np.abs(coefficients))[-30:][::-1]
                    if abs(coefficients[index]) > 1e-14
                ],
            })
            if (
                same_cell
                and all(value < 1.0 for value in ratios.values())
                and h910_endpoint is not None
                and h910_endpoint < h910_value
            ):
                best = (record, delta)
        branches.append(record)

    if best is None:
        OUTPUT.write_text(json.dumps({
            "version": 1,
            "verdict": "FULL_CONTROL_NO_ACCEPTED_NUMERICAL_STEP",
            "source_hashes": {
                str(SOURCE.relative_to(ROOT)): sha256(SOURCE),
                str(FACES_PATH.relative_to(ROOT)): sha256(FACES_PATH),
            },
            "mode_count": len(modes),
            "branches": branches,
            "finite_difference_diagnostics": fd_diagnostics,
        }, indent=2) + "\n")
        raise RuntimeError("no accepted full-control actual-cell step")

    best_record, delta = best
    float_velocity = delta / best_record["physical_linf"]
    velocity, base_coefficients = common.exactify_velocity(
        exact_rows, labels, float_velocity
    )
    physical_step = Q(format(best_record["physical_linf"], ".17g"))
    exact_delta = {
        label: tuple(physical_step * value for value in velocity[label])
        for label in labels
    }
    exact_endpoint = {
        label: tuple(exact_rows[label][axis] + exact_delta[label][axis] for axis in range(3))
        for label in labels
    }
    exact_path = {
        label: tuple(ex.P((exact_rows[label][axis], exact_delta[label][axis])) for axis in range(3))
        for label in labels
    }
    exact_jets = {
        name: exact_first_jet(exact_path, faces, name) for name in TARGET_KEYS
    }
    # Exact H910 non-resurrection witness: its minimum raw component at the
    # source remains negative at the candidate endpoint.
    source_ledger = ex.mechanics_primitives(exact_rows, faces)
    endpoint_ledger = ex.mechanics_primitives(exact_endpoint, faces)
    components = ("t", "one_minus_t", "beta1", "beta2")
    h910_source = source_ledger["edge"][(9, 10)]
    h910_witness = min(components, key=lambda name: h910_source[name])
    if h910_source[h910_witness] >= 0:
        raise AssertionError(("no exact negative H910 witness", h910_witness))
    if endpoint_ledger["edge"][(9, 10)][h910_witness] >= h910_source[h910_witness]:
        raise AssertionError(("exact H910 witness did not move outward", h910_witness))

    # The rational endpoint itself must remain in the exact source cell.
    support = ex.supporting_cell(exact_endpoint, faces)
    _ledger, mechanics = ex.classify_point(exact_endpoint, faces)
    if support["f_vector"] != [61, 162, 103] or mechanics["class"] != [2, 2, 2]:
        raise AssertionError((support, mechanics))
    if not common.BASE_SET.issubset(set().union(*(set(face) for face in faces))):
        raise AssertionError("base labels absent")
    missing_rails = sorted(frozen_builder.forced_rails() - set(support["edges"]))
    if missing_rails:
        raise AssertionError(("missing rails", missing_rails))
    write_exact_csv(ENDPOINT, exact_endpoint)

    payload = {
        "version": 1,
        "scope": "full 165-mode actual-cell rational proposal after H1011 circuit flip",
        "source_hashes": {
            str(SOURCE.relative_to(ROOT)): sha256(SOURCE),
            str(FACES_PATH.relative_to(ROOT)): sha256(FACES_PATH),
        },
        "source_signature": signature(source),
        "mode_count": len(modes),
        "mode_names": [list(item) for item in mode_names],
        "base_plane_normal": plane_normal.tolist(),
        "finite_difference_diagnostics": fd_diagnostics,
        "near_support_count": len(near_support),
        "all_support_count": len(all_support),
        "branches": branches,
        "selected_branch": best_record,
        "physical_step": ex.qs(physical_step),
        "velocity": {
            str(label): [ex.qs(value) for value in velocity[label]] for label in labels
        },
        "base_velocity_coefficients": base_coefficients,
        "exact_selected_first_jets": exact_jets,
        "exact_h910_witness": {
            "component": h910_witness,
            "source": ex.qs(h910_source[h910_witness]),
            "endpoint": ex.qs(endpoint_ledger["edge"][(9, 10)][h910_witness]),
        },
        "exact_endpoint": {
            "file": ENDPOINT.name,
            "sha256": sha256(ENDPOINT),
            "support": {key: value for key, value in support.items() if key != "edges"},
            "mechanics": mechanics,
            "forced_rail_count": len(frozen_builder.forced_rails()),
            "missing_forced_rails": [],
        },
        "verdict": "FULL_CONTROL_RATIONAL_ACTUAL_CELL_DESCENT_PROPOSAL_PASS",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "verdict": payload["verdict"],
        "mode_count": payload["mode_count"],
        "selected": best_record,
        "exact_first_jet_signs": {name: "negative" for name in exact_jets},
        "endpoint": payload["exact_endpoint"],
    }, indent=2))


if __name__ == "__main__":
    main()
