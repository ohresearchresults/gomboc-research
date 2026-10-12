#!/usr/bin/env python3
"""Constraint-generated rational endpoint proposer for U1/H1011.

Every candidate is checked against all exact raw and support rows.  The LP is
only a search oracle: a row omitted from an intermediate LP can never be
omitted from acceptance.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

import front_common as fc


sys.path.insert(0, str(fc.SIDE))
import propose_epoch as parent  # noqa: E402
sys.path.insert(0, str(fc.TRACK))
from actual_hull_mechanics import evaluate  # noqa: E402


TARGET_ALIASES = frozenset(fc.TARGET_ALIASES["U1"] + fc.TARGET_ALIASES["H1011"])
INITIAL_RAW_GUARDS = {
    "edge:(1, 54):one_minus_t",
    "vertex:54:1",
    "edge:(9, 10):one_minus_t",
    "vertex:10:9",
}
POST_FACTORS = (Q(1001, 1000), Q(101, 100), Q(33, 32), Q(17, 16), Q(9, 8), Q(5, 4))
FLOOR = Q(1, 8)
MAX_ROUNDS = 12
SUPPORT_NAME = re.compile(r"support:f([0-9]+):w([0-9]+)$")


def qsign(value):
    return (value > 0) - (value < 0)


def exact_raw_changes(source_rows, endpoint, faces):
    endpoint_rows = parent.exact_raw_mechanics_values(endpoint, faces)
    if [name for name, _ in endpoint_rows] != [name for name, _ in source_rows]:
        raise AssertionError("raw row order drift")
    changed = []
    for (name, source_value), (_name2, endpoint_value) in zip(source_rows, endpoint_rows):
        if name in TARGET_ALIASES:
            continue
        if qsign(endpoint_value) != qsign(source_value):
            changed.append(name)
    return changed


def support_derivative(labels, points, faces, modes, name):
    match = SUPPORT_NAME.fullmatch(name)
    if not match:
        raise AssertionError(("bad support name", name))
    face_index, witness_label = map(int, match.groups())
    offsets = {label: index for index, label in enumerate(labels)}
    a_label, b_label, c_label = faces[face_index][:3]
    a, b, c = (points[offsets[label]] for label in (a_label, b_label, c_label))
    witness = points[offsets[witness_label]]
    edge_b, edge_c, ray = b - a, c - a, witness - a
    normal = np.cross(edge_b, edge_c)
    row = []
    for mode in modes:
        da, db, dc, dw = (
            mode[offsets[label]] for label in (a_label, b_label, c_label, witness_label)
        )
        dnormal = np.cross(db - da, edge_c) + np.cross(edge_b, dc - da)
        row.append(float(np.dot(dnormal, ray) + np.dot(normal, dw - da)))
    return np.asarray(row)


def fresh_signature(endpoint, labels, faces):
    points = np.asarray([[float(value) for value in endpoint[label]] for label in labels])
    mechanics = evaluate(labels, points)
    actual_faces = fc.chart.common.actual_faces(labels, points)
    signature = fc.chart.signature(mechanics)
    expected = fc.EXPECTED_ENDPOINT_FEATURES["U1_H1011"]
    checks = {
        "face_ledger_unchanged": fc.rc.face_sets(actual_faces) == fc.rc.face_sets(faces),
        "f_vector_61_162_103": signature["f_vector"] == [61, 162, 103],
        "active_labels_61": signature["active_labels"] == fc.rc.EXPECTED_ACTIVE,
        "class_2_1_1": signature["class"] == expected["class"],
        "stable_faces_preserved": signature["stable_faces"] == expected["stable_faces"],
        "unstable_exactly_8": signature["unstable_vertices"] == expected["unstable_vertices"],
        "saddle_exactly_5_6": signature["saddle_edges"] == expected["saddle_edges"],
        "all_37_rails": fc.rc.forced_rails().issubset(fc.rc.edge_set(actual_faces)),
    }
    return signature, checks


def main() -> None:
    source_hashes = fc.bindings()
    audit_path = fc.HERE / "reachability_audit.json"
    audit = json.loads(audit_path.read_text())
    if audit.get("selected_target") != "U1_H1011":
        raise AssertionError("reachability selection drift")

    source = fc.rc.ex.read_rows(fc.SOURCE)
    faces = json.loads(fc.FACES.read_text())
    labels = sorted(source)
    points = np.asarray([[float(value) for value in source[label]] for label in labels])
    modes, mode_names, plane_normal = fc.chart.build_modes(labels, points)
    if len(modes) != 165:
        raise AssertionError(("mode count", len(modes)))
    displacement = np.asarray([
        [mode[offset, axis] for mode in modes]
        for offset in range(len(labels)) for axis in range(3)
    ])

    raw_names, raw_values = parent.raw_mechanics_vector(labels, points, faces)
    raw_jacobian = parent.raw_mechanics_jacobian(labels, points, faces, modes, raw_names)
    raw_index = {name: index for index, name in enumerate(raw_names)}
    exact_source_raw = parent.exact_raw_mechanics_values(source, faces)
    exact_source_support = parent.exact_support_values(source, faces)
    support_source = dict(exact_source_support)

    target_values = np.asarray([
        raw_values[raw_index["vertex:1:54"]],
        raw_values[raw_index["edge:(10, 11):t"]],
    ])
    target_jacobian = np.asarray([
        raw_jacobian[raw_index["vertex:1:54"]],
        raw_jacobian[raw_index["edge:(10, 11):t"]],
    ])
    if np.any(target_values <= 0) or np.linalg.matrix_rank(target_jacobian) != 2:
        raise AssertionError(("target source/rank", target_values.tolist()))

    active_raw = set(INITIAL_RAW_GUARDS)
    active_support = set()
    support_derivatives = {}
    trials = []
    accepted = None
    for post in POST_FACTORS:
        for round_index in range(1, MAX_ROUNDS + 1):
            rows, rhs = [], []
            for name in sorted(active_raw):
                index = raw_index[name]
                value, jacobian = raw_values[index], raw_jacobian[index]
                row_sign = 1.0 if value > 0 else -1.0
                rows.append(np.r_[-float(post) * row_sign * jacobian / abs(value), 0.0])
                rhs.append(1.0 - float(FLOOR))
            for name in sorted(active_support):
                value = float(support_source[name])
                jacobian = support_derivatives.setdefault(
                    name, support_derivative(labels, points, faces, modes, name)
                )
                row_sign = 1.0 if value > 0 else -1.0
                rows.append(np.r_[-float(post) * row_sign * jacobian / abs(value), 0.0])
                rhs.append(1.0 - float(FLOOR))
            for coordinate_row in displacement:
                rows.append(np.r_[coordinate_row, -1.0]); rhs.append(0.0)
                rows.append(np.r_[-coordinate_row, -1.0]); rhs.append(0.0)
            equality = np.column_stack((target_jacobian / target_values[:, None], np.zeros(2)))
            lp = linprog(
                np.r_[np.zeros(len(modes)), 1.0],
                A_ub=np.asarray(rows), b_ub=np.asarray(rhs),
                A_eq=equality, b_eq=np.asarray([-1.0, -1.0]),
                bounds=[(-1000.0, 1000.0)] * len(modes) + [(0.0, 0.01)],
                method="highs", options={"time_limit": 30.0},
            )
            record = {
                "post_factor": fc.rc.ex.qs(post), "round": round_index,
                "active_raw_count": len(active_raw),
                "active_support_count": len(active_support),
                "solver_success": bool(lp.success), "solver_status": int(lp.status),
                "solver_message": lp.message,
            }
            if not lp.success:
                trials.append(record)
                break

            coefficients = np.asarray(lp.x[:-1])
            delta = np.tensordot(coefficients, modes, axes=(0, 0))
            wall_linf = float(np.max(np.abs(delta)))
            endpoint, velocity, base_coefficients, wall_step = parent.exact_endpoint(
                source, labels, delta, wall_linf, post
            )
            raw_changed = exact_raw_changes(exact_source_raw, endpoint, faces)
            support_guard = parent.exact_support_endpoint_guard(
                exact_source_support, endpoint, faces
            )
            support_changed = [row["name"] for row in support_guard["changed_rows"]]
            endpoint_targets = fc.target_polynomials(
                fc.affine_path(endpoint, {label: (Q(0), Q(0), Q(0)) for label in labels}),
                faces,
            )
            target_signs = {
                name: qsign(endpoint_targets[name].eval(Q(0))) for name in ("U1", "H1011")
            }
            try:
                checkpoint = fc.rc.exact_checkpoint(
                    endpoint, faces, fc.EXPECTED_ENDPOINT_FEATURES["U1_H1011"]
                )
                checkpoint_error = None
            except Exception as error:
                checkpoint, checkpoint_error = None, repr(error)
            try:
                signature, fresh_checks = fresh_signature(endpoint, labels, faces)
            except Exception as error:
                signature, fresh_checks = None, {"fresh_audit_completed": False}
                fresh_error = repr(error)
            else:
                fresh_error = None
            row230 = fc.rc.row230_values(endpoint, faces)
            checks = {
                "all_non_target_raw_endpoint_signs_preserved": not raw_changed,
                "all_support_endpoint_signs_preserved": not support_changed,
                "both_targets_crossed": target_signs == {"U1": -1, "H1011": -1},
                "exact_checkpoint": checkpoint is not None,
                "fresh_endpoint": all(fresh_checks.values()),
                "row230_strict": all(Q(value) > 0 for value in row230.values()),
            }
            record.update({
                "linear_wall_linf": float(lp.x[-1]), "actual_wall_linf": wall_linf,
                "exact_wall_step": fc.rc.ex.qs(wall_step),
                "endpoint_sha256": hashlib.sha256(fc.rc.exact_csv_bytes(endpoint)).hexdigest(),
                "changed_raw": raw_changed, "changed_support": support_changed,
                "target_signs": target_signs, "signature": signature,
                "checkpoint_error": checkpoint_error, "fresh_error": fresh_error,
                "checks": checks, "accepted": all(checks.values()),
            })
            trials.append(record)
            if record["accepted"]:
                accepted = (record, endpoint, velocity, base_coefficients, wall_step, checkpoint)
                break
            newly_raw = set(raw_changed) - active_raw
            newly_support = set(support_changed) - active_support
            if not newly_raw and not newly_support:
                break
            active_raw.update(newly_raw)
            active_support.update(newly_support)
        if accepted:
            break

    source_packet = {
        **source_hashes,
        fc.rc.relative(audit_path): fc.sha256(audit_path),
        fc.rc.relative(Path(__file__)): fc.sha256(Path(__file__)),
    }
    if accepted is None:
        payload = {
            "version": 1, "source_hashes": source_packet,
            "search": {"post_factors": [fc.rc.ex.qs(v) for v in POST_FACTORS],
                       "floor": fc.rc.ex.qs(FLOOR), "max_rounds": MAX_ROUNDS},
            "trials": trials,
            "first_blocker": "constraint generation found no exact accepted U1/H1011 endpoint",
            "verdict": "FAIL_CLOSED_SPARSE_CONDITIONED_U1_H1011_NO_ENDPOINT",
        }
        (fc.HERE / "sparse_joint_failure_receipt.json").write_text(json.dumps(payload, indent=2) + "\n")
        raise RuntimeError(payload["first_blocker"])

    record, endpoint, velocity, base_coefficients, wall_step, checkpoint = accepted
    endpoint_path = fc.HERE / "joint_candidate.csv"
    endpoint_path.write_bytes(fc.rc.exact_csv_bytes(endpoint))
    payload = {
        "version": 1,
        "scope": "Constraint-generated rational endpoint; exact joint-root ordering remains unclaimed.",
        "source_hashes": source_packet,
        "search": {"post_factors": [fc.rc.ex.qs(v) for v in POST_FACTORS],
                   "floor": fc.rc.ex.qs(FLOOR), "max_rounds": MAX_ROUNDS,
                   "initial_predecessor_guards": sorted(INITIAL_RAW_GUARDS)},
        "trials": trials, "selected_trial": record,
        "base_plane_normal": plane_normal.tolist(),
        "exact_direction": {
            "wall_step": fc.rc.ex.qs(wall_step),
            "velocity": {str(label): [fc.rc.ex.qs(v) for v in velocity[label]] for label in labels},
            "base_velocity_coefficients": base_coefficients,
        },
        "exact_endpoint": {"file": endpoint_path.name, "sha256": fc.sha256(endpoint_path),
                           "checkpoint": checkpoint},
        "proof_boundary": "No event accepted until an exact common root and exhaustive ordering are certified.",
        "verdict": "RATIONAL_SPARSE_CONDITIONED_U1_H1011_ENDPOINT_PASS_NOT_EVENT_CERTIFIED",
    }
    (fc.HERE / "joint_proposal.json").write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({"verdict": payload["verdict"], "selected_trial": record,
                      "endpoint_sha256": fc.sha256(endpoint_path)}, indent=2))


if __name__ == "__main__":
    main()
