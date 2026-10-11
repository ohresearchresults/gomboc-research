#!/usr/bin/env python3
"""Deterministic full-support numerical proposer for one relay epoch."""
from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

import relay_common as rc


sys.path.insert(0, str(rc.ATTACK / "continuation" / "main"))
import propose_full_control as chart  # noqa: E402
sys.path.insert(0, str(rc.TRACK))
from actual_hull_mechanics import evaluate  # noqa: E402
sys.path.insert(0, str(rc.ATTACK))
import build_exact_circuit_flip as selected_owner  # noqa: E402


FD_STEP = 1e-8
POST_FACTORS = (Q(101, 100), Q(33, 32), Q(17, 16), Q(9, 8))
GUARD_FLOORS = (Q(1, 20), Q(1, 4))
INWARD_FACTORS = (Q(1), Q(4), Q(16))


def in_face_turn_values(labels, points, faces):
    index = {label: offset for offset, label in enumerate(labels)}
    values = []
    for cycle in faces:
        if len(cycle) <= 3:
            continue
        offsets = [index[label] for label in cycle]
        normal = np.cross(
            points[offsets[1]] - points[offsets[0]],
            points[offsets[2]] - points[offsets[0]],
        )
        for offset, current in enumerate(offsets):
            previous = offsets[offset - 1]
            following = offsets[(offset + 1) % len(offsets)]
            values.append(float(np.dot(
                np.cross(
                    points[current] - points[previous],
                    points[following] - points[current],
                ),
                normal,
            )))
    return np.asarray(values)


def in_face_turn_jacobian(labels, points, faces, modes):
    return np.asarray([
        (
            in_face_turn_values(labels, points + FD_STEP * mode, faces)
            - in_face_turn_values(labels, points - FD_STEP * mode, faces)
        ) / (2 * FD_STEP)
        for mode in modes
    ]).T


def target_value(labels, points, faces, phase):
    point_map = {label: tuple(points[offset]) for offset, label in enumerate(labels)}
    _d6, centered = rc.ex.scaled_centered(point_map, faces)
    if phase == "birth":
        return float(rc.ex.vertex_component(point_map, centered, 1, 54))
    return float(rc.ex.vertex_component(point_map, centered, 54, 1))


def target_jacobian(labels, points, faces, modes, phase):
    return np.asarray([
        (
            target_value(labels, points + FD_STEP * mode, faces, phase)
            - target_value(labels, points - FD_STEP * mode, faces, phase)
        ) / (2 * FD_STEP)
        for mode in modes
    ])


def exact_support_values(points, faces):
    """Return every frozen-ledger support row as an exact rational value."""
    labels = set(points)
    rows = []
    for face_index, cycle in enumerate(faces):
        normal = rc.ex.cycle_normal(cycle, points)
        anchor = points[cycle[0]]
        for witness in sorted(labels - set(cycle)):
            rows.append((
                f"support:f{face_index}:w{witness}",
                rc.ex.dot(normal, rc.ex.sub(points[witness], anchor)),
            ))
    if len(rows) != 5959:
        raise AssertionError(("exact support row count", len(rows)))
    if any(not value for _name, value in rows):
        raise AssertionError("zero exact support row")
    return rows


def exact_support_endpoint_guard(source_rows, endpoint, faces):
    endpoint_rows = exact_support_values(endpoint, faces)
    if [name for name, _value in endpoint_rows] != [
        name for name, _value in source_rows
    ]:
        raise AssertionError("exact support row order drift")
    changed = []
    for (name, source_value), (_endpoint_name, endpoint_value) in zip(
        source_rows, endpoint_rows
    ):
        source_sign = (source_value > 0) - (source_value < 0)
        endpoint_sign = (endpoint_value > 0) - (endpoint_value < 0)
        if endpoint_sign != source_sign:
            changed.append({
                "name": name,
                "source_sign": source_sign,
                "endpoint_sign": endpoint_sign,
                "source_log10_abs": rc.ex.qlog10(source_value),
                "endpoint_log10_abs": rc.ex.qlog10(endpoint_value),
            })
    return {
        "guard_count": len(source_rows),
        "changed_count": len(changed),
        "changed_rows": changed,
        "all_endpoint_signs_preserved": not changed,
    }


def exact_support_linearization(source, labels, faces, specs, modes, mode_names):
    """Build exact-rational source values and sparse first jets for supports.

    The prior normalized double finite difference loses the smallest support
    rows to cancellation.  Support sign is the sign of the unnormalized triple
    product, whose first derivative is polynomial and can be formed exactly.
    Only modes attached to the face triple or witness can contribute.
    """
    zero = (Q(0), Q(0), Q(0))
    exact_mode_vectors = []
    modes_by_label = {}
    for mode_index, (mode, mode_name) in enumerate(zip(modes, mode_names)):
        moving_label = mode_name[0]
        exact_mode, _coefficients = chart.common.exactify_velocity(
            source, labels, mode
        )
        if any(
            any(value for value in velocity)
            for label, velocity in exact_mode.items()
            if label != moving_label
        ):
            raise AssertionError(("exact mode is not sparse", mode_name))
        exact_mode_vectors.append(exact_mode[moving_label])
        modes_by_label.setdefault(moving_label, []).append(mode_index)

    values = []
    jacobian = np.zeros((len(specs), len(modes)), dtype=float)
    for row_index, (face_index, witness_offset, orientation, _value) in enumerate(specs):
        cycle = faces[face_index]
        a_label, b_label, c_label = cycle[:3]
        witness_label = labels[witness_offset]
        a, b, c = source[a_label], source[b_label], source[c_label]
        witness = source[witness_label]
        edge_b = rc.ex.sub(b, a)
        edge_c = rc.ex.sub(c, a)
        ray = rc.ex.sub(witness, a)
        value = -orientation * rc.ex.det3(edge_b, edge_c, ray)
        if value <= 0:
            raise AssertionError((
                "nonpositive exact oriented support",
                face_index,
                witness_label,
                rc.ex.qs(value),
            ))
        values.append(float(value))
        involved = {a_label, b_label, c_label, witness_label}
        for moving_label in involved:
            for mode_index in modes_by_label[moving_label]:
                velocity = exact_mode_vectors[mode_index]
                da = velocity if moving_label == a_label else zero
                db = velocity if moving_label == b_label else zero
                dc = velocity if moving_label == c_label else zero
                dw = velocity if moving_label == witness_label else zero
                derivative = -orientation * (
                    rc.ex.det3(rc.ex.sub(db, da), edge_c, ray)
                    + rc.ex.det3(edge_b, rc.ex.sub(dc, da), ray)
                    + rc.ex.det3(edge_b, edge_c, rc.ex.sub(dw, da))
                )
                jacobian[row_index, mode_index] = float(derivative)
    return np.asarray(values), jacobian


def raw_mechanics_vector(labels, points, faces):
    point_map = {label: tuple(points[offset]) for offset, label in enumerate(labels)}
    ledger = rc.ex.mechanics_primitives(point_map, faces)
    names = ["volume_d6"]
    values = [float(ledger["d6"])]
    for face_key, rows in sorted(ledger["reference"].items()):
        for edge, value in sorted(rows.items()):
            names.append(f"face_reference:{face_key}:{edge}")
            values.append(float(value))
    for face_key, rows in sorted(ledger["face"].items()):
        for edge, value in sorted(rows.items()):
            names.append(f"face_raw:{face_key}:{edge}")
            values.append(float(value))
    for vertex, rows in sorted(ledger["vertex"].items()):
        for neighbor, value in sorted(rows.items()):
            names.append(f"vertex:{vertex}:{neighbor}")
            values.append(float(value))
    for edge, rows in sorted(ledger["edge"].items()):
        for component in (
            "direction_norm2", "gram", "t", "one_minus_t", "beta1", "beta2"
        ):
            names.append(f"edge:{edge}:{component}")
            values.append(float(rows[component]))
    return names, np.asarray(values)


def exact_raw_mechanics_values(points, faces):
    """Return the 1,945 exact raw mechanics guards in canonical order."""
    ledger = rc.ex.mechanics_primitives(points, faces)
    rows = [("volume_d6", ledger["d6"])]
    for face_key, values in sorted(ledger["reference"].items()):
        for edge, value in sorted(values.items()):
            rows.append((f"face_reference:{face_key}:{edge}", value))
    for face_key, values in sorted(ledger["face"].items()):
        for edge, value in sorted(values.items()):
            rows.append((f"face_raw:{face_key}:{edge}", value))
    for vertex, values in sorted(ledger["vertex"].items()):
        for neighbor, value in sorted(values.items()):
            rows.append((f"vertex:{vertex}:{neighbor}", value))
    for edge, values in sorted(ledger["edge"].items()):
        for component in (
            "direction_norm2", "gram", "t", "one_minus_t", "beta1", "beta2"
        ):
            rows.append((f"edge:{edge}:{component}", values[component]))
    if len(rows) != 1945:
        raise AssertionError(("exact raw mechanics row count", len(rows)))
    return rows


def exact_raw_endpoint_guard(source_rows, endpoint, faces, phase):
    """Reject a candidate if any non-target raw guard changes endpoint sign.

    The finite-difference LP is unreliable for the smallest raw components.
    This exact post-check prevents such a row from being hidden by an accepted
    endpoint class.  Interior even touches remain the locator's responsibility.
    """
    endpoint_rows = exact_raw_mechanics_values(endpoint, faces)
    if [name for name, _value in endpoint_rows] != [
        name for name, _value in source_rows
    ]:
        raise AssertionError("exact raw mechanics row order drift")
    aliases = set(rc.ALIASES[phase])
    changed = []
    checked = 0
    for (name, source_value), (_endpoint_name, endpoint_value) in zip(
        source_rows, endpoint_rows
    ):
        if name in aliases:
            continue
        checked += 1
        source_sign = (source_value > 0) - (source_value < 0)
        endpoint_sign = (endpoint_value > 0) - (endpoint_value < 0)
        if not source_sign or endpoint_sign != source_sign:
            changed.append({
                "name": name,
                "source_sign": source_sign,
                "endpoint_sign": endpoint_sign,
                "source_log10_abs": rc.ex.qlog10(source_value),
                "endpoint_log10_abs": rc.ex.qlog10(endpoint_value),
            })
    if checked != 1943:
        raise AssertionError(("exact raw non-target guard count", checked))
    return {
        "guard_count": checked,
        "changed_count": len(changed),
        "changed_rows": changed,
        "all_non_target_endpoint_signs_preserved": not changed,
    }


def raw_mechanics_jacobian(labels, points, faces, modes, expected_names):
    columns = []
    for mode in modes:
        plus_names, plus = raw_mechanics_vector(
            labels, points + FD_STEP * mode, faces
        )
        minus_names, minus = raw_mechanics_vector(
            labels, points - FD_STEP * mode, faces
        )
        if plus_names != expected_names or minus_names != expected_names:
            raise AssertionError("raw mechanics row order drift")
        columns.append((plus - minus) / (2 * FD_STEP))
    return np.asarray(columns).T


def expected_for_phase(phase):
    if phase == "birth":
        return rc.SOURCE, rc.PRE_FEATURES, rc.MIDDLE_FEATURES, rc.HERE / "post_birth_checkpoint.csv"
    return rc.HERE / "post_birth_checkpoint.csv", rc.MIDDLE_FEATURES, rc.FAR_FEATURES, rc.HERE / "far_u1.csv"


def selected_keys(phase):
    if phase == "birth":
        return {("U", 1), ("H", (1, 54))}
    return {("U", 54), ("H", (1, 54))}


def exact_endpoint(source, labels, delta, wall_linf, post):
    velocity, base_coefficients = chart.common.exactify_velocity(
        source, labels, delta / wall_linf
    )
    wall_step = Q(format(wall_linf, ".17g"))
    endpoint = {
        label: tuple(
            source[label][axis] + post * wall_step * velocity[label][axis]
            for axis in range(3)
        )
        for label in labels
    }
    return endpoint, velocity, base_coefficients, wall_step


def fresh_audit(endpoint, labels, faces, expected):
    points = np.asarray([
        [float(value) for value in endpoint[label]] for label in labels
    ])
    mechanics = evaluate(labels, points)
    actual_faces = chart.common.actual_faces(labels, points)
    signature = chart.signature(mechanics)
    checks = {
        "fresh_face_ledger_unchanged": rc.face_sets(actual_faces) == rc.face_sets(faces),
        "fresh_f_vector": signature["f_vector"] == [61, 162, 103],
        "fresh_active_labels": signature["active_labels"] == rc.EXPECTED_ACTIVE,
        "fresh_class": signature["class"] == expected["class"],
        "fresh_stable_faces": signature["stable_faces"] == expected["stable_faces"],
        "fresh_unstable_vertices": signature["unstable_vertices"] == expected["unstable_vertices"],
        "fresh_saddle_edges": signature["saddle_edges"] == expected["saddle_edges"],
        "fresh_rails": rc.forced_rails().issubset(rc.edge_set(actual_faces)),
    }
    return signature, checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", choices=("birth", "death"), required=True)
    args = parser.parse_args()
    phase = args.phase
    source_path, source_features, endpoint_features, endpoint_path = expected_for_phase(phase)
    proposal_path = rc.HERE / f"{phase}_proposal.json"
    failure_path = rc.HERE / f"{phase}_failure_receipt.json"
    external_bindings = rc.bindings()
    if phase == "death":
        birth_certificate = rc.HERE / "birth_certificate.json"
        if not birth_certificate.exists():
            raise AssertionError("death requires the exact birth certificate")
        frozen_birth = json.loads(birth_certificate.read_text())
        if frozen_birth.get("verdict") != "EXACT_U1_BIRTH_EPOCH_PASS":
            raise AssertionError("birth certificate is not accepted")
        if rc.sha256(source_path) != frozen_birth["generated_file_sha256"][rc.relative(source_path)]:
            raise AssertionError("literal post-birth checkpoint drift")
    if selected_owner.SELECTED_COMPONENTS["U54"] != 1:
        raise AssertionError("authoritative U54 selected component drift")

    source = rc.ex.read_rows(source_path)
    faces = json.loads(rc.FACES.read_text())
    source_checkpoint = rc.exact_checkpoint(source, faces, source_features)
    exact_source_support = exact_support_values(source, faces)
    source_row230 = {key: Q(value) for key, value in rc.row230_values(source, faces).items()}
    labels = sorted(source)
    points = np.asarray([
        [float(value) for value in source[label]] for label in labels
    ])
    numerical_source = evaluate(labels, points)
    if chart.signature(numerical_source)["class"] != source_features["class"]:
        raise AssertionError("numerical source class differs from exact source")
    if rc.face_sets(chart.common.actual_faces(labels, points)) != rc.face_sets(faces):
        raise AssertionError("fresh source hull differs from frozen exact ledger")

    modes, mode_names, plane_normal = chart.build_modes(labels, points)
    if len(modes) != 165:
        raise AssertionError(("mode count", len(modes)))
    displacement = np.asarray([
        [mode[offset, axis] for mode in modes]
        for offset in range(len(labels))
        for axis in range(3)
    ])
    face_keys = sorted(numerical_source.face_decisions)
    vertex_keys = sorted(numerical_source.vertex_decisions)
    edge_keys = sorted(numerical_source.edge_decisions)
    key_groups = (face_keys, vertex_keys, edge_keys)
    keys = (
        [("S", key) for key in face_keys]
        + [("U", key) for key in vertex_keys]
        + [("H", key) for key in edge_keys]
    )
    mechanics_jacobian, fd_diagnostics = chart.central_mechanics_jacobian(
        labels, points, modes, numerical_source, key_groups
    )
    mechanics_values = chart.mechanics_vector(numerical_source, *key_groups)
    raw_names, raw_values = raw_mechanics_vector(labels, points, faces)
    if len(raw_names) != 1945 or np.any(raw_values == 0):
        raise AssertionError(("raw mechanics source contract", len(raw_names)))
    exact_source_raw = exact_raw_mechanics_values(source, faces)
    if [name for name, _value in exact_source_raw] != raw_names:
        raise AssertionError("floating/exact raw mechanics row order drift")
    if any(not value for _name, value in exact_source_raw):
        raise AssertionError("zero exact raw mechanics guard at source")
    raw_jacobian = raw_mechanics_jacobian(
        labels, points, faces, modes, raw_names
    )
    _near_support, support_specs = chart.common.support_specs(
        labels, points, faces, numerical_source.centroid, threshold=2e-3
    )
    support_values, support_jacobian = exact_support_linearization(
        source, labels, faces, support_specs, modes, mode_names
    )
    turn_values = in_face_turn_values(labels, points, faces)
    turn_jacobian = in_face_turn_jacobian(labels, points, faces, modes)
    if len(turn_values) != 18 or np.any(turn_values == 0):
        raise AssertionError("fresh base-turn rows are not 18 strict values")
    target_source = target_value(labels, points, faces, phase)
    required_source_sign = -1 if phase == "birth" else 1
    if (target_source > 0) - (target_source < 0) != required_source_sign:
        raise AssertionError(("target source sign", target_source))
    target_row = target_jacobian(labels, points, faces, modes, phase)
    desired_fractional_change = -required_source_sign

    danger_indices = []
    for index, spec in enumerate(support_specs):
        family = (frozenset(faces[spec[0]]), labels[spec[1]])
        if family in rc.DANGER:
            danger_indices.append(index)
    if len(danger_indices) != 2:
        raise AssertionError(("danger support rows", danger_indices))

    branches = []
    accepted = None
    branch_number = 0
    for post in POST_FACTORS:
        for floor in GUARD_FLOORS:
            for inward in INWARD_FACTORS:
                branch_number += 1
                rows = []
                rhs = []
                exempt = selected_keys(phase)
                for key, value, jacobian in zip(keys, mechanics_values, mechanics_jacobian):
                    if key in exempt:
                        continue
                    sign = 1.0 if value > 0 else -1.0
                    rows.append(np.r_[
                        -float(post) * sign * jacobian / abs(value), 0.0
                    ])
                    rhs.append(1.0 - float(floor))
                for name, value, jacobian in zip(raw_names, raw_values, raw_jacobian):
                    if name in rc.ALIASES[phase]:
                        continue
                    sign = 1.0 if value > 0 else -1.0
                    rows.append(np.r_[
                        -float(post) * sign * jacobian / abs(value), 0.0
                    ])
                    rhs.append(1.0 - float(floor))
                for value, jacobian in zip(support_values, support_jacobian):
                    rows.append(np.r_[
                        -float(post) * jacobian / value, 0.0
                    ])
                    rhs.append(1.0 - float(floor))
                for value, jacobian in zip(turn_values, turn_jacobian):
                    sign = 1.0 if value > 0 else -1.0
                    rows.append(np.r_[
                        -float(post) * sign * jacobian / abs(value), 0.0
                    ])
                    rhs.append(1.0 - float(floor))
                for index in danger_indices:
                    rows.append(np.r_[
                        -support_jacobian[index] / support_values[index], 0.0
                    ])
                    rhs.append(-float(inward))
                for row in displacement:
                    rows.append(np.r_[row, -1.0])
                    rhs.append(0.0)
                    rows.append(np.r_[-row, -1.0])
                    rhs.append(0.0)
                equality = np.r_[target_row / abs(target_source), 0.0][None, :]
                lp = linprog(
                    np.r_[np.zeros(len(modes)), 1.0],
                    A_ub=np.asarray(rows),
                    b_ub=np.asarray(rhs),
                    A_eq=equality,
                    b_eq=np.asarray([desired_fractional_change]),
                    bounds=[(-1000.0, 1000.0)] * len(modes) + [(0.0, 0.01)],
                    method="highs",
                    options={"time_limit": 20.0},
                )
                record = {
                    "branch_id": f"b{branch_number:02d}",
                    "post_factor": rc.ex.qs(post),
                    "guard_floor": rc.ex.qs(floor),
                    "row230_inward_factor": rc.ex.qs(inward),
                    "solver_success": bool(lp.success),
                    "solver_status": int(lp.status),
                    "solver_message": lp.message,
                }
                if not lp.success:
                    branches.append(record)
                    continue
                coefficients = np.asarray(lp.x[:-1])
                delta = np.tensordot(coefficients, modes, axes=(0, 0))
                wall_linf = float(np.max(np.abs(delta)))
                endpoint, velocity, base_coefficients, wall_step = exact_endpoint(
                    source, labels, delta, wall_linf, post
                )
                record.update({
                    "linear_wall_linf": float(lp.x[-1]),
                    "actual_wall_linf": wall_linf,
                    "exact_wall_step": rc.ex.qs(wall_step),
                    "exact_endpoint_sha256": __import__("hashlib").sha256(
                        rc.exact_csv_bytes(endpoint)
                    ).hexdigest(),
                    "active_mode_count": int(np.sum(np.abs(coefficients) > 1e-14)),
                    "largest_active_modes": [
                        {
                            "mode": list(mode_names[index]),
                            "coefficient": float(coefficients[index]),
                        }
                        for index in np.argsort(np.abs(coefficients))[-16:][::-1]
                        if abs(coefficients[index]) > 1e-14
                    ],
                })
                try:
                    support_endpoint_guard = exact_support_endpoint_guard(
                        exact_source_support, endpoint, faces
                    )
                    record["exact_support_endpoint_guard"] = support_endpoint_guard
                    if not support_endpoint_guard["all_endpoint_signs_preserved"]:
                        raise AssertionError((
                            "exact support endpoint sign changes",
                            [row["name"] for row in support_endpoint_guard["changed_rows"]],
                        ))
                    exact_receipt = rc.exact_checkpoint(endpoint, faces, endpoint_features)
                    raw_endpoint_guard = exact_raw_endpoint_guard(
                        exact_source_raw, endpoint, faces, phase
                    )
                    fresh_signature, fresh_checks = fresh_audit(
                        endpoint, labels, faces, endpoint_features
                    )
                    endpoint_row230 = {
                        key: Q(value) for key, value in rc.row230_values(endpoint, faces).items()
                    }
                    row230_checks = {
                        key: endpoint_row230[key] > source_row230[key]
                        for key in source_row230
                    }
                    checks = {
                        **fresh_checks,
                        "exact_support_endpoint_signs_preserved": (
                            support_endpoint_guard["all_endpoint_signs_preserved"]
                        ),
                        "exact_checkpoint": True,
                        "exact_raw_non_target_endpoint_signs_preserved": (
                            raw_endpoint_guard[
                                "all_non_target_endpoint_signs_preserved"
                            ]
                        ),
                        "row230_preserved_strict": all(
                            value > 0 for value in endpoint_row230.values()
                        ),
                    }
                    if phase == "death":
                        record["row230_margin_increase_diagnostic"] = row230_checks
                    record["endpoint_audit"] = {
                        "exact": exact_receipt,
                        "fresh_signature": fresh_signature,
                        "checks": checks,
                        "exact_support_endpoint_guard": support_endpoint_guard,
                        "exact_raw_endpoint_guard": raw_endpoint_guard,
                        "row230_checks": row230_checks,
                        "row230_source_squared_margins": {
                            key: rc.ex.qs(value) for key, value in source_row230.items()
                        },
                        "row230_endpoint_squared_margins": {
                            key: rc.ex.qs(value) for key, value in endpoint_row230.items()
                        },
                    }
                    record["accepted"] = all(checks.values())
                except Exception as error:
                    record["endpoint_error"] = repr(error)
                    record["accepted"] = False
                branches.append(record)
                if record["accepted"]:
                    accepted = (
                        record, endpoint, velocity, base_coefficients, wall_step,
                    )
                    break
            if accepted:
                break
        if accepted:
            break

    if accepted is None:
        payload = {
            "version": 1,
            "phase": phase,
            "source_hashes": {
                **external_bindings,
                rc.relative(source_path): rc.sha256(source_path),
            },
            "source_checkpoint": source_checkpoint,
            "branches": branches,
            "first_blocker": "no exact/fresh-hull endpoint passed the bounded full-support branch grid",
            "verdict": f"FAIL_CLOSED_{phase.upper()}_PROPOSER_NO_ACCEPTED_ENDPOINT",
        }
        failure_path.write_text(json.dumps(payload, indent=2) + "\n")
        raise RuntimeError(payload["first_blocker"])

    record, endpoint, velocity, base_coefficients, wall_step = accepted
    rc.write_exact_csv(endpoint_path, endpoint)
    payload = {
        "version": 1,
        "phase": phase,
        "scope": (
            "Numerical 165-mode full-support proposer followed by literal rational "
            "endpoint, exact ledger/class checks, and a fresh ConvexHull readback. "
            "This is locator input, not an accepted algebraic event certificate."
        ),
        "source_hashes": {
            **external_bindings,
            rc.relative(source_path): rc.sha256(source_path),
        },
        "source_checkpoint": source_checkpoint,
        "target": {
            "aliases": list(rc.ALIASES[phase]),
            "source_raw": target_source,
            "source_sign": required_source_sign,
            "target_jacobian_rank": int(np.linalg.matrix_rank(target_row[None, :])),
        },
        "search_contract": {
            "mode_count": len(modes),
            "support_guard_count": len(support_specs),
            "support_linearization": "sparse exact-rational unnormalized first jets",
            "base_turn_guard_count": len(turn_values),
            "mechanics_decision_count": len(keys),
            "raw_mechanics_guard_count": len(raw_names) - len(rc.ALIASES[phase]),
            "raw_mechanics_names_digest": __import__("hashlib").sha256(
                "\n".join(raw_names).encode()
            ).hexdigest(),
            "exempt_mechanics_aliases": [repr(key) for key in sorted(selected_keys(phase), key=repr)],
            "post_factor_grid": [rc.ex.qs(value) for value in POST_FACTORS],
            "guard_floor_grid": [rc.ex.qs(value) for value in GUARD_FLOORS],
            "row230_inward_factor_grid": [rc.ex.qs(value) for value in INWARD_FACTORS],
        },
        "finite_difference_diagnostics": fd_diagnostics,
        "base_plane_normal": plane_normal.tolist(),
        "branches": branches,
        "selected_branch": record,
        "exact_direction": {
            "wall_step": rc.ex.qs(wall_step),
            "velocity": {
                str(label): [rc.ex.qs(value) for value in velocity[label]]
                for label in labels
            },
            "base_velocity_coefficients": base_coefficients,
        },
        "exact_endpoint": {
            "file": endpoint_path.name,
            "sha256": rc.sha256(endpoint_path),
            "checkpoint": record["endpoint_audit"]["exact"],
        },
        "proof_boundary": (
            "No floating root is accepted here; locate_epoch.py must prove the "
            "exhaustive first event and the exact certifier must prove multiplicity."
        ),
        "verdict": f"RATIONAL_FULL_SUPPORT_{phase.upper()}_PROPOSAL_PASS",
    }
    proposal_path.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "verdict": payload["verdict"],
        "selected_branch": record["branch_id"],
        "endpoint": endpoint_path.name,
        "endpoint_sha256": rc.sha256(endpoint_path),
        "fresh_signature": record["endpoint_audit"]["fresh_signature"],
    }, indent=2))


if __name__ == "__main__":
    main()
