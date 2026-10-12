#!/usr/bin/env python3
"""Conditioned fresh 165D proposer for the selected U1/H1011 annihilation."""
from __future__ import annotations

import hashlib
import json
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


FD_STEP = 1e-8
POST_FACTORS = (Q(1001, 1000), Q(101, 100), Q(33, 32), Q(17, 16))
GUARD_FLOORS = (Q(1, 4), Q(1, 2), Q(3, 4))
TARGET_NAMES = ("U1", "H1011")
TARGET_ALIASES = frozenset(
    fc.TARGET_ALIASES["U1"] + fc.TARGET_ALIASES["H1011"]
)
EXEMPT_DECISIONS = {("U", 1), ("H", (10, 11))}


def raw_target_values(labels, points, faces):
    point_map = {label: tuple(points[offset]) for offset, label in enumerate(labels)}
    d6, xscaled = fc.rc.ex.scaled_centered(point_map, faces)
    incidence, _neighbors, _face_by_key = fc.rc.ex.edge_data(faces)
    u1 = fc.rc.ex.vertex_component(point_map, xscaled, 1, 54)
    h1011 = fc.rc.ex.edge_components(
        point_map, faces, xscaled, incidence, (10, 11)
    )["t"]
    return np.asarray([float(u1), float(h1011)])


def raw_target_jacobian(labels, points, faces, modes):
    return np.asarray([
        (
            raw_target_values(labels, points + FD_STEP * mode, faces)
            - raw_target_values(labels, points - FD_STEP * mode, faces)
        ) / (2 * FD_STEP)
        for mode in modes
    ]).T


def fresh_audit(endpoint, labels, faces):
    points = np.asarray([[float(value) for value in endpoint[label]] for label in labels])
    mechanics = evaluate(labels, points)
    actual_faces = fc.chart.common.actual_faces(labels, points)
    signature = fc.chart.signature(mechanics)
    expected = fc.EXPECTED_ENDPOINT_FEATURES["U1_H1011"]
    checks = {
        "fresh_face_ledger_unchanged": fc.rc.face_sets(actual_faces) == fc.rc.face_sets(faces),
        "fresh_f_vector": signature["f_vector"] == [61, 162, 103],
        "fresh_active_labels": signature["active_labels"] == fc.rc.EXPECTED_ACTIVE,
        "fresh_class": signature["class"] == expected["class"],
        "fresh_stable_faces": signature["stable_faces"] == expected["stable_faces"],
        "fresh_unstable_vertices": signature["unstable_vertices"] == expected["unstable_vertices"],
        "fresh_saddle_edges": signature["saddle_edges"] == expected["saddle_edges"],
        "fresh_rails": fc.rc.forced_rails().issubset(fc.rc.edge_set(actual_faces)),
    }
    return signature, checks


def main() -> None:
    output_path = fc.HERE / "joint_candidate.csv"
    proposal_path = fc.HERE / "joint_proposal.json"
    failure_path = fc.HERE / "joint_failure_receipt.json"
    audit_path = fc.HERE / "reachability_audit.json"
    source_hashes = fc.bindings()
    audit = json.loads(audit_path.read_text())
    if audit.get("verdict") != "EXACT_POST_RELAY_FIRST_JET_REACHABILITY_AUDIT_PASS":
        raise AssertionError(("reachability verdict", audit.get("verdict")))
    if audit.get("selected_target") != "U1_H1011":
        raise AssertionError(("selected target", audit.get("selected_target")))

    source = fc.rc.ex.read_rows(fc.SOURCE)
    faces = json.loads(fc.FACES.read_text())
    source_checkpoint = fc.rc.exact_checkpoint(source, faces, fc.rc.FAR_FEATURES)
    labels = sorted(source)
    points = np.asarray([[float(value) for value in source[label]] for label in labels])
    source_mechanics = evaluate(labels, points)
    if fc.chart.signature(source_mechanics)["class"] != [2, 2, 2]:
        raise AssertionError("fresh numerical source class")
    if fc.rc.face_sets(fc.chart.common.actual_faces(labels, points)) != fc.rc.face_sets(faces):
        raise AssertionError("fresh source hull differs from frozen ledger")

    modes, mode_names, plane_normal = fc.chart.build_modes(labels, points)
    if len(modes) != 165:
        raise AssertionError(("mode count", len(modes)))
    displacement = np.asarray([
        [mode[offset, axis] for mode in modes]
        for offset in range(len(labels))
        for axis in range(3)
    ])

    face_keys = sorted(source_mechanics.face_decisions)
    vertex_keys = sorted(source_mechanics.vertex_decisions)
    edge_keys = sorted(source_mechanics.edge_decisions)
    key_groups = (face_keys, vertex_keys, edge_keys)
    decision_keys = (
        [("S", key) for key in face_keys]
        + [("U", key) for key in vertex_keys]
        + [("H", key) for key in edge_keys]
    )
    mechanics_jacobian, fd_diagnostics = fc.chart.central_mechanics_jacobian(
        labels, points, modes, source_mechanics, key_groups
    )
    mechanics_values = fc.chart.mechanics_vector(source_mechanics, *key_groups)
    raw_names, raw_values = parent.raw_mechanics_vector(labels, points, faces)
    raw_jacobian = parent.raw_mechanics_jacobian(
        labels, points, faces, modes, raw_names
    )
    exact_source_raw = parent.exact_raw_mechanics_values(source, faces)
    exact_source_support = parent.exact_support_values(source, faces)
    _near, support_specs = fc.chart.common.support_specs(
        labels, points, faces, source_mechanics.centroid, threshold=2e-3
    )
    support_values, support_jacobian = parent.exact_support_linearization(
        source, labels, faces, support_specs, modes, mode_names
    )
    turn_values = parent.in_face_turn_values(labels, points, faces)
    turn_jacobian = parent.in_face_turn_jacobian(labels, points, faces, modes)
    target_values = raw_target_values(labels, points, faces)
    target_jacobian = raw_target_jacobian(labels, points, faces, modes)
    if np.any(target_values <= 0) or np.linalg.matrix_rank(target_jacobian) != 2:
        raise AssertionError(("target source/rank", target_values.tolist()))

    branches = []
    accepted = None
    branch_number = 0
    for post in POST_FACTORS:
        for floor in GUARD_FLOORS:
            branch_number += 1
            rows = []
            rhs = []
            for key, value, jacobian in zip(
                decision_keys, mechanics_values, mechanics_jacobian
            ):
                if key in EXEMPT_DECISIONS:
                    continue
                row_sign = 1.0 if value > 0 else -1.0
                rows.append(np.r_[
                    -float(post) * row_sign * jacobian / abs(value), 0.0
                ])
                rhs.append(1.0 - float(floor))
            for name, value, jacobian in zip(raw_names, raw_values, raw_jacobian):
                if name in TARGET_ALIASES:
                    continue
                row_sign = 1.0 if value > 0 else -1.0
                rows.append(np.r_[
                    -float(post) * row_sign * jacobian / abs(value), 0.0
                ])
                rhs.append(1.0 - float(floor))
            for value, jacobian in zip(support_values, support_jacobian):
                rows.append(np.r_[
                    -float(post) * jacobian / value, 0.0
                ])
                rhs.append(1.0 - float(floor))
            for value, jacobian in zip(turn_values, turn_jacobian):
                row_sign = 1.0 if value > 0 else -1.0
                rows.append(np.r_[
                    -float(post) * row_sign * jacobian / abs(value), 0.0
                ])
                rhs.append(1.0 - float(floor))
            for row in displacement:
                rows.append(np.r_[row, -1.0])
                rhs.append(0.0)
                rows.append(np.r_[-row, -1.0])
                rhs.append(0.0)

            equality = np.column_stack((
                target_jacobian / target_values[:, None],
                np.zeros(2),
            ))
            lp = linprog(
                np.r_[np.zeros(len(modes)), 1.0],
                A_ub=np.asarray(rows),
                b_ub=np.asarray(rhs),
                A_eq=equality,
                b_eq=np.asarray([-1.0, -1.0]),
                bounds=[(-1000.0, 1000.0)] * len(modes) + [(0.0, 0.01)],
                method="highs",
                options={"time_limit": 30.0},
            )
            record = {
                "branch_id": f"b{branch_number:02d}",
                "post_factor": fc.rc.ex.qs(post),
                "guard_floor": fc.rc.ex.qs(floor),
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
            endpoint, velocity, base_coefficients, wall_step = parent.exact_endpoint(
                source, labels, delta, wall_linf, post
            )
            record.update({
                "linear_wall_linf": float(lp.x[-1]),
                "actual_wall_linf": wall_linf,
                "exact_wall_step": fc.rc.ex.qs(wall_step),
                "exact_endpoint_sha256": hashlib.sha256(
                    fc.rc.exact_csv_bytes(endpoint)
                ).hexdigest(),
                "active_mode_count": int(np.sum(np.abs(coefficients) > 1e-14)),
            })
            try:
                support_guard = parent.exact_support_endpoint_guard(
                    exact_source_support, endpoint, faces
                )
                # The parent death guard exempts the old D family.  This front
                # instead performs the same exact sign audit with only its four
                # declared target aliases exempted.
                endpoint_raw = parent.exact_raw_mechanics_values(endpoint, faces)
                changed = []
                for (name, source_value), (_name2, endpoint_value) in zip(
                    exact_source_raw, endpoint_raw
                ):
                    if name in TARGET_ALIASES:
                        continue
                    source_sign = (source_value > 0) - (source_value < 0)
                    if source_sign:
                        endpoint_sign = (endpoint_value > 0) - (endpoint_value < 0)
                        if endpoint_sign != source_sign:
                            changed.append(name)
                exact_receipt = fc.rc.exact_checkpoint(
                    endpoint, faces, fc.EXPECTED_ENDPOINT_FEATURES["U1_H1011"]
                )
                fresh_signature, fresh_checks = fresh_audit(endpoint, labels, faces)
                endpoint_targets = fc.target_polynomials(
                    fc.affine_path(endpoint, {
                        label: (Q(0), Q(0), Q(0)) for label in endpoint
                    }),
                    faces,
                )
                target_signs = {
                    name: (polynomial.eval(Q(0)) > 0) - (polynomial.eval(Q(0)) < 0)
                    for name, polynomial in endpoint_targets.items()
                    if name in TARGET_NAMES
                }
                row230 = fc.rc.row230_values(endpoint, faces)
                checks = {
                    **fresh_checks,
                    "exact_support_endpoint_signs_preserved": support_guard[
                        "all_endpoint_signs_preserved"
                    ],
                    "exact_non_target_raw_endpoint_signs_preserved": not changed,
                    "exact_checkpoint": True,
                    "both_targets_crossed": target_signs == {"U1": -1, "H1011": -1},
                    "row230_strict": all(Q(value) > 0 for value in row230.values()),
                }
                record["endpoint_audit"] = {
                    "exact": exact_receipt,
                    "fresh_signature": fresh_signature,
                    "support_guard": support_guard,
                    "changed_non_target_raw_rows": changed,
                    "target_signs": target_signs,
                    "row230_squared_margins": row230,
                    "checks": checks,
                }
                record["accepted"] = all(checks.values())
            except Exception as error:
                record["endpoint_error"] = repr(error)
                record["accepted"] = False
            branches.append(record)
            if record["accepted"]:
                accepted = (record, endpoint, velocity, base_coefficients, wall_step)
                break
        if accepted:
            break

    if accepted is None:
        payload = {
            "version": 1,
            "source_hashes": {
                **source_hashes,
                fc.rc.relative(audit_path): fc.sha256(audit_path),
                fc.rc.relative(Path(__file__)): fc.sha256(Path(__file__)),
            },
            "source_checkpoint": source_checkpoint,
            "branches": branches,
            "first_blocker": "no conditioned exact/fresh endpoint passed",
            "verdict": "FAIL_CLOSED_CONDITIONED_U1_H1011_NO_ENDPOINT",
        }
        failure_path.write_text(json.dumps(payload, indent=2) + "\n")
        raise RuntimeError(payload["first_blocker"])

    record, endpoint, velocity, base_coefficients, wall_step = accepted
    output_path.write_bytes(fc.rc.exact_csv_bytes(endpoint))
    payload = {
        "version": 1,
        "scope": (
            "Fresh conditioned 165D U1/H1011 rational endpoint proposer. "
            "This is locator input and does not claim an exact joint event."
        ),
        "source_hashes": {
            **source_hashes,
            fc.rc.relative(audit_path): fc.sha256(audit_path),
            fc.rc.relative(Path(__file__)): fc.sha256(Path(__file__)),
        },
        "source_checkpoint": source_checkpoint,
        "target": {
            "pair": "U1_H1011",
            "semantic_targets": list(TARGET_NAMES),
            "aliases": sorted(TARGET_ALIASES),
            "source_raw": target_values.tolist(),
        },
        "search_contract": {
            "mode_count": len(modes),
            "support_guard_count": len(support_specs),
            "support_linearization": "sparse exact-rational unnormalized first jets",
            "raw_guard_count": len(raw_names) - len(TARGET_ALIASES),
            "base_turn_guard_count": len(turn_values),
            "post_factors": [fc.rc.ex.qs(value) for value in POST_FACTORS],
            "guard_floors": [fc.rc.ex.qs(value) for value in GUARD_FLOORS],
        },
        "finite_difference_diagnostics": fd_diagnostics,
        "base_plane_normal": plane_normal.tolist(),
        "branches": branches,
        "selected_branch": record,
        "exact_direction": {
            "wall_step": fc.rc.ex.qs(wall_step),
            "velocity": {
                str(label): [fc.rc.ex.qs(value) for value in velocity[label]]
                for label in labels
            },
            "base_velocity_coefficients": base_coefficients,
        },
        "exact_endpoint": {
            "file": output_path.name,
            "sha256": fc.sha256(output_path),
            "checkpoint": record["endpoint_audit"]["exact"],
        },
        "proof_boundary": (
            "The two target roots need exact ordering and common-factor audit; "
            "no floating tie is accepted here."
        ),
        "verdict": "RATIONAL_CONDITIONED_U1_H1011_ENDPOINT_PASS_NOT_EVENT_CERTIFIED",
    }
    proposal_path.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "verdict": payload["verdict"],
        "selected_branch": record["branch_id"],
        "endpoint_sha256": fc.sha256(output_path),
        "target_signs": record["endpoint_audit"]["target_signs"],
        "fresh_signature": record["endpoint_audit"]["fresh_signature"],
    }, indent=2))


if __name__ == "__main__":
    main()
