#!/usr/bin/env python3
"""Bounded full-165D search for the selected U54/H1011 first event.

This is a proposer/search receipt, not an exact shared-root certificate.  Every
accepted endpoint must survive a fresh-hull check and a numerical scan of all
7,904 existing primitives plus the 18 enlarged-base in-face turns.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares, linprog


sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
ATTACK = HERE.parent
TRACK = ATTACK.parent
ROOT = HERE.parents[4]
WORKSPACE = HERE.parents[3]
MAIN = ATTACK / "continuation" / "main"
SOURCE = ATTACK / "continuation2_row230_bypass" / "step13_transfer_far.csv"
FACES = MAIN / "exact_full_control_chain_post_faces.json"
OBSTRUCTION = HERE / "fixed_ledger_obstruction_receipt.json"
OUTPUT = HERE / "search_receipt.json"
RELAXED_ENDPOINT = HERE / "best_relaxed_endpoint.csv"
CANDIDATE_ENDPOINT = HERE / "candidate_endpoint.csv"

EXPECTED_SOURCE_SHA256 = "81cb9b2b0666b413906f45ec7db69da81750b304940b3f8466778f73a0895552"
EXPECTED_FACES_SHA256 = "c1d74d638df21a0492645aa39e4d3943b8401ed0732393505c838ec2f1c0ed77"
EXPECTED_OBSTRUCTION_VERDICT = (
    "EXACT_FIXED_LEDGER_SELECTED_U54_NEIGHBOR1_"
    "PRECEDING_ZERO_OBSTRUCTION_PASS"
)

TRUST_GRID = (Q(1, 100000), Q(1, 50000), Q(1, 20000), Q(1, 10000))
POST_FACTOR_GRID = (Q(33, 32), Q(17, 16), Q(9, 8))
GUARD_FLOOR_GRID = (Q(0), Q(1, 20), Q(1, 4))
PROFILE_GRID = ("target_only", "topology_only", "mechanics_only", "all_guards")
MAX_TRUST = Q(1, 10000)
FD_STEP = 1e-8
TARGET_RESIDUAL_TOLERANCE = 1e-7
ROOT_TIE_TOLERANCE = 1e-8
ROOT_RESIDUAL_TOLERANCE = 1e-5

TARGET_KEYS = {("U", 54), ("H", (10, 11))}
TARGET_ALIASES = {
    "U54": {"vertex:54:1", "edge:(1, 54):one_minus_t"},
    "H1011": {"edge:(10, 11):t", "vertex:10:11"},
}
TARGET_RAW_NAMES = set().union(*TARGET_ALIASES.values())

sys.path.insert(0, str(MAIN))
import propose_full_control as base  # noqa: E402
import locate_first_event as locator  # noqa: E402
sys.path.insert(0, str(TRACK))
from actual_hull_mechanics import evaluate  # noqa: E402
sys.path.insert(0, str(TRACK / "rigorous_local_bypass"))
import exact_core as ex  # noqa: E402
SAFE_FLIP = WORKSPACE / "tracks" / "piecewise_transfer" / "post_c17_attack" / "recovery2" / "main"
sys.path.insert(0, str(SAFE_FLIP))
import certify_safe_flip as exhaustive  # noqa: E402


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


def json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    raise TypeError(f"unsupported JSON value: {type(value)!r}")


def atomic_json(path: Path, payload) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, default=json_default) + "\n"
    )
    temporary.replace(path)


def exact_csv_bytes(rows) -> bytes:
    handle = io.StringIO(newline="")
    writer = csv.writer(handle)
    writer.writerow(("source_id", "x", "y", "z"))
    for label in sorted(rows):
        writer.writerow((label, *(str(value) for value in rows[label])))
    return handle.getvalue().encode()


def write_exact_csv(path: Path, rows) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_bytes(exact_csv_bytes(rows))
    temporary.replace(path)


def edge_set(faces) -> set[tuple[int, int]]:
    return {
        tuple(sorted((first, second)))
        for cycle in faces
        for first, second in zip(cycle, cycle[1:] + cycle[:1])
    }


def selected_raw_pair(labels, points, faces, incidence) -> np.ndarray:
    point_map = {label: tuple(points[offset]) for offset, label in enumerate(labels)}
    _d6, xscaled = ex.scaled_centered(point_map, faces)
    return np.asarray([
        float(ex.vertex_component(point_map, xscaled, 54, 1)),
        float(ex.edge_components(
            point_map, faces, xscaled, incidence, (10, 11)
        )["t"]),
    ])


def target_jacobian(labels, points, faces, incidence, modes, source_raw) -> np.ndarray:
    columns = []
    for mode in modes:
        plus = selected_raw_pair(labels, points + FD_STEP * mode, faces, incidence)
        minus = selected_raw_pair(labels, points - FD_STEP * mode, faces, incidence)
        columns.append((plus - minus) / (2 * FD_STEP))
    return np.asarray(columns).T / source_raw[:, None]


def in_face_turn_values(labels, points, faces) -> np.ndarray:
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


def in_face_turn_jacobian(labels, points, faces, modes) -> np.ndarray:
    return np.asarray([
        (
            in_face_turn_values(labels, points + FD_STEP * mode, faces)
            - in_face_turn_values(labels, points - FD_STEP * mode, faces)
        ) / (2 * FD_STEP)
        for mode in modes
    ]).T


def refine_joint_wall(
    labels, points, faces, incidence, modes, source_raw, target_rows, coefficients
):
    correction_basis = target_rows.T @ np.linalg.inv(target_rows @ target_rows.T)

    def residual(correction):
        adjusted = coefficients + correction_basis @ correction
        delta = np.tensordot(adjusted, modes, axes=(0, 0))
        return selected_raw_pair(labels, points + delta, faces, incidence) / source_raw

    fit = least_squares(
        residual,
        np.zeros(2),
        method="lm",
        ftol=1e-14,
        xtol=1e-14,
        gtol=1e-14,
        max_nfev=300,
    )
    refined = coefficients + correction_basis @ fit.x
    delta = np.tensordot(refined, modes, axes=(0, 0))
    return fit, refined, delta, residual(fit.x)


def normalized_guard_rows(source, mechanics_jacobian, keys):
    values = base.mechanics_vector(
        source,
        sorted(source.face_decisions),
        sorted(source.vertex_decisions),
        sorted(source.edge_decisions),
    )
    rows = []
    names = []
    for offset, (key, value) in enumerate(zip(keys, values)):
        if key in TARGET_KEYS:
            continue
        sign = 1.0 if value > 0 else -1.0
        rows.append(sign * mechanics_jacobian[offset] / abs(value))
        names.append(repr(key))
    return np.asarray(rows), names


def solve_branch(
    profile,
    floor,
    post,
    modes,
    displacement,
    target_rows,
    mechanics_rows,
    support_rows,
    turn_rows,
):
    scale = float(MAX_TRUST)
    post_float = float(post)
    floor_float = float(floor)
    rows = []
    rhs = []

    if profile in ("mechanics_only", "all_guards"):
        rows.extend(np.c_[
            -post_float * scale * mechanics_rows,
            np.zeros(len(mechanics_rows)),
        ])
        rhs.extend(np.full(len(mechanics_rows), 1.0 - floor_float))
    if profile in ("topology_only", "all_guards"):
        topology = np.vstack((support_rows, turn_rows))
        rows.extend(np.c_[
            -post_float * scale * topology,
            np.zeros(len(topology)),
        ])
        rhs.extend(np.full(len(topology), 1.0 - floor_float))

    rows.extend(np.c_[displacement, -np.ones(len(displacement))])
    rhs.extend(np.zeros(len(displacement)))
    rows.extend(np.c_[-displacement, -np.ones(len(displacement))])
    rhs.extend(np.zeros(len(displacement)))

    return linprog(
        np.r_[np.zeros(len(modes)), 1.0],
        A_ub=np.asarray(rows),
        b_ub=np.asarray(rhs),
        A_eq=np.c_[scale * target_rows, np.zeros(2)],
        b_eq=np.asarray([-1.0, -1.0]),
        bounds=[(-1000.0, 1000.0)] * len(modes)
        + [(0.0, 1.0 / post_float)],
        method="highs",
        options={"time_limit": 15.0},
    )


def endpoint_audit(exact_source, exact_endpoint, faces, labels, source_signature):
    points = np.asarray([
        [float(value) for value in exact_endpoint[label]] for label in labels
    ])
    mechanics = evaluate(labels, points)
    signature = base.signature(mechanics)
    actual_faces = base.common.actual_faces(labels, points)
    actual_edges = edge_set(actual_faces)
    base_key = sorted(base.common.BASE_SET)
    primary_key = sorted(base.common.PRIMARY)
    expected_stable = sorted((base_key, primary_key))
    expected_saddles = [[5, 6]]
    expected_unstable = [8]
    decisions = {
        "S": mechanics.face_decisions.get(tuple(primary_key)),
        "U8": mechanics.vertex_decisions.get(8),
        "U54": mechanics.vertex_decisions.get(54),
        "H56": mechanics.edge_decisions.get((5, 6)),
        "H1011": mechanics.edge_decisions.get((10, 11)),
    }
    rails = base.frozen_builder.forced_rails()
    checks = {
        "fresh_face_ledger_unchanged": (
            base.face_sets(actual_faces) == base.face_sets(faces)
        ),
        "f_vector_unchanged": signature["f_vector"] == [61, 162, 103],
        "all_active_rows_remain": (
            signature["active_labels"] == source_signature["active_labels"]
        ),
        "base_stable": base_key in signature["stable_faces"],
        "u8_remains_unstable": 8 in signature["unstable_vertices"],
        "all_37_rails_remain": rails.issubset(actual_edges),
        "s_positive": decisions["S"] is not None and decisions["S"] > 0,
        "h56_positive": decisions["H56"] is not None and decisions["H56"] > 0,
        "u54_post_negative": decisions["U54"] is not None and decisions["U54"] < 0,
        "h1011_post_negative": (
            decisions["H1011"] is not None and decisions["H1011"] < 0
        ),
        "post_class_2_1_1": signature["class"] == [2, 1, 1],
        "post_feature_sets_exact": (
            signature["stable_faces"] == expected_stable
            and signature["unstable_vertices"] == expected_unstable
            and signature["saddle_edges"] == expected_saddles
        ),
    }
    return {
        "signature": signature,
        "decisions": decisions,
        "checks": checks,
        "passed_check_count": sum(checks.values()),
        "required_check_count": len(checks),
    }


def root_semantic(name: str) -> str | None:
    for semantic, aliases in TARGET_ALIASES.items():
        if name in aliases:
            return semantic
    return None


def numerical_roots(name, polynomial, family):
    coefficients = np.asarray([float(value) for value in polynomial.c], dtype=float)
    magnitude = float(np.max(np.abs(coefficients)))
    if polynomial.degree == 0 or not math.isfinite(magnitude) or magnitude == 0:
        return []
    normalized = coefficients / magnitude
    roots = []
    for candidate in np.polynomial.polynomial.polyroots(normalized):
        if abs(candidate.imag) > 1e-7 * max(1.0, abs(candidate.real)):
            continue
        parameter = float(candidate.real)
        if parameter <= 1e-12 or parameter > 1.0 + 1e-10:
            continue
        residual = abs(float(np.polynomial.polynomial.polyval(parameter, normalized)))
        if residual > ROOT_RESIDUAL_TOLERANCE:
            continue
        if any(abs(parameter - row["parameter"]) <= 1e-9 for row in roots):
            continue
        epsilon = max(1e-12, min(parameter * 1e-7, 1e-7))
        left_parameter = max(0.0, parameter - epsilon)
        right_parameter = min(1.0, parameter + epsilon)
        left = polynomial.eval(Q(format(left_parameter, ".17g")))
        right = polynomial.eval(Q(format(right_parameter, ".17g")))
        derivative = np.arange(1, len(normalized)) * normalized[1:]
        derivative_value = float(
            np.polynomial.polynomial.polyval(parameter, derivative)
        ) if len(derivative) else 0.0
        roots.append({
            "parameter": parameter,
            "name": name,
            "family": family,
            "semantic": root_semantic(name),
            "degree": polynomial.degree,
            "normalized_residual": residual,
            "normalized_derivative": derivative_value,
            "odd_crossing": left * right < 0,
        })
    return roots


def scan_endpoint(exact_source, exact_endpoint, faces):
    path = locator.path_from_endpoints(exact_source, exact_endpoint)
    rows = list(exhaustive.primitive_rows(path, faces))
    if len(rows) != 7922:
        raise AssertionError(("unexpected exhaustive primitive count", len(rows)))
    roots = []
    family_counts = {}
    for name, polynomial, family in rows:
        family_counts[family] = family_counts.get(family, 0) + 1
        roots.extend(numerical_roots(name, polynomial, family))
    roots.sort(key=lambda row: (row["parameter"], row["name"]))
    if not roots:
        return {
            "primitive_count": len(rows),
            "family_counts": family_counts,
            "root_count_in_unit_segment": 0,
            "first_event": None,
            "target_roots": [],
            "joint_first_event": False,
        }

    first_parameter = roots[0]["parameter"]
    first_group = [
        row for row in roots
        if abs(row["parameter"] - first_parameter) <= ROOT_TIE_TOLERANCE
    ]
    target_roots = [row for row in roots if row["name"] in TARGET_RAW_NAMES]
    semantics = {row["semantic"] for row in first_group if row["semantic"]}
    first_names = {row["name"] for row in first_group}
    joint = (
        semantics == {"U54", "H1011"}
        and first_names.issubset(TARGET_RAW_NAMES)
        and all(row["odd_crossing"] for row in first_group)
    )
    return {
        "primitive_count": len(rows),
        "family_counts": family_counts,
        "root_count_in_unit_segment": len(roots),
        "first_event": {
            "parameter": first_parameter,
            "rows": first_group,
        },
        "target_roots": target_roots[:12],
        "first_32_roots": roots[:32],
        "joint_first_event": joint,
        "root_tie_tolerance": ROOT_TIE_TOLERANCE,
        "warning": (
            "Floating polynomial roots are locator evidence only; exact sharing "
            "requires a nontrivial rational gcd and an independent certificate."
        ),
    }


def branch_score(record) -> tuple:
    audit = record.get("endpoint_audit") or {}
    checks = audit.get("checks") or {}
    return (
        audit.get("passed_check_count", -1),
        int(checks.get("u54_post_negative", False)),
        int(checks.get("h1011_post_negative", False)),
        int(checks.get("f_vector_unchanged", False)),
        int(checks.get("all_active_rows_remain", False)),
        -record.get("target_wall_residual_max", math.inf),
        -record.get("exact_endpoint_linf", math.inf),
        record["branch_id"],
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(OUTPUT))
    args = parser.parse_args()
    output = Path(args.output).resolve()
    if output.parent != HERE:
        raise ValueError("output must stay inside the sidecar directory")
    if sha256(SOURCE) != EXPECTED_SOURCE_SHA256:
        raise AssertionError("source hash drift")
    if sha256(FACES) != EXPECTED_FACES_SHA256:
        raise AssertionError("face-ledger hash drift")
    obstruction = json.loads(OBSTRUCTION.read_text())
    if obstruction["verdict"] != EXPECTED_OBSTRUCTION_VERDICT:
        raise AssertionError("obstruction receipt verdict mismatch")
    if obstruction["source_hashes"][relative(SOURCE)] != sha256(SOURCE):
        raise AssertionError("obstruction receipt source mismatch")
    if obstruction["source_hashes"][relative(FACES)] != sha256(FACES):
        raise AssertionError("obstruction receipt faces mismatch")
    if base.frozen_builder.SELECTED_COMPONENTS["U54"] != 1:
        raise AssertionError("authoritative U54 selected component drift")
    if base.frozen_builder.SELECTED_COMPONENTS["H1011"] != "t":
        raise AssertionError("authoritative H1011 selected component drift")

    exact_source = ex.read_rows(SOURCE)
    labels = sorted(exact_source)
    points = np.asarray([
        [float(value) for value in exact_source[label]] for label in labels
    ])
    faces = json.loads(FACES.read_text())
    exact_support = ex.supporting_cell(exact_source, faces)
    _exact_ledger, exact_mechanics = ex.classify_point(exact_source, faces)
    source = evaluate(labels, points)
    source_signature = base.signature(source)
    if exact_support["f_vector"] != [61, 162, 103]:
        raise AssertionError(exact_support)
    if exact_mechanics["class"] != [2, 2, 2]:
        raise AssertionError(exact_mechanics)
    if source_signature["class"] != [2, 2, 2]:
        raise AssertionError(source_signature)
    if base.face_sets(base.common.actual_faces(labels, points)) != base.face_sets(faces):
        raise AssertionError("fresh source hull differs from supplied ledger")

    modes, mode_names, plane_normal = base.build_modes(labels, points)
    if len(modes) != 165:
        raise AssertionError(("mode count", len(modes)))
    displacement = np.asarray([
        [mode[offset, axis] for mode in modes]
        for offset in range(len(labels))
        for axis in range(3)
    ])

    face_keys = sorted(source.face_decisions)
    vertex_keys = sorted(source.vertex_decisions)
    edge_keys = sorted(source.edge_decisions)
    key_groups = (face_keys, vertex_keys, edge_keys)
    keys = (
        [("S", key) for key in face_keys]
        + [("U", key) for key in vertex_keys]
        + [("H", key) for key in edge_keys]
    )
    mechanics_jacobian, fd_diagnostics = base.central_mechanics_jacobian(
        labels, points, modes, source, key_groups
    )
    mechanics_rows, mechanics_names = normalized_guard_rows(
        source, mechanics_jacobian, keys
    )

    incidence, _neighbors, _face_by_key = ex.edge_data(faces)
    source_raw = selected_raw_pair(labels, points, faces, incidence)
    if not np.all(source_raw > 0):
        raise AssertionError(("target raw source signs", source_raw))
    target_rows = target_jacobian(
        labels, points, faces, incidence, modes, source_raw
    )
    if np.linalg.matrix_rank(target_rows) != 2:
        raise AssertionError("joint target Jacobian is rank deficient")

    near_support, all_support = base.common.support_specs(
        labels, points, faces, source.centroid, threshold=2e-3
    )
    all_support_values = np.asarray([row[3] for row in all_support])
    all_support_jacobian = base.support_jacobian(
        labels, points, faces, all_support, modes
    )
    support_rows = all_support_jacobian / all_support_values[:, None]

    source_turns = in_face_turn_values(labels, points, faces)
    if len(source_turns) != 18 or np.any(source_turns == 0):
        raise AssertionError(("base turn source values", source_turns))
    turn_jacobian = in_face_turn_jacobian(labels, points, faces, modes)
    turn_rows = (
        np.sign(source_turns)[:, None] * turn_jacobian
        / np.abs(source_turns)[:, None]
    )

    branches = []
    endpoints = {}
    branch_counter = 0
    for profile in PROFILE_GRID:
        floors = (Q(0),) if profile == "target_only" else GUARD_FLOOR_GRID
        for floor in floors:
            for post in POST_FACTOR_GRID:
                branch_counter += 1
                branch_id = f"b{branch_counter:02d}-{profile}-f{floor}-p{post}"
                lp = solve_branch(
                    profile,
                    floor,
                    post,
                    modes,
                    displacement,
                    target_rows,
                    mechanics_rows,
                    support_rows,
                    turn_rows,
                )
                record = {
                    "branch_id": branch_id,
                    "profile": profile,
                    "guard_floor": ex.qs(floor),
                    "post_factor": ex.qs(post),
                    "solver_status": int(lp.status),
                    "solver_success": bool(lp.success),
                    "solver_message": lp.message,
                }
                if not lp.success:
                    branches.append(record)
                    continue

                coefficients = float(MAX_TRUST) * np.asarray(lp.x[:-1])
                fit, refined, delta, target_residual = refine_joint_wall(
                    labels,
                    points,
                    faces,
                    incidence,
                    modes,
                    source_raw,
                    target_rows,
                    coefficients,
                )
                wall_linf = float(np.max(np.abs(delta)))
                if not wall_linf > 0:
                    raise AssertionError("zero refined wall direction")
                float_velocity = delta / wall_linf
                exact_velocity, _base_coefficients = base.common.exactify_velocity(
                    exact_source, labels, float_velocity
                )
                exact_wall_step = Q(format(wall_linf, ".17g"))
                exact_endpoint = {
                    label: tuple(
                        exact_source[label][axis]
                        + post * exact_wall_step * exact_velocity[label][axis]
                        for axis in range(3)
                    )
                    for label in labels
                }
                exact_endpoint_linf = max(
                    abs(float(exact_endpoint[label][axis] - exact_source[label][axis]))
                    for label in labels
                    for axis in range(3)
                )
                endpoint_sha = hashlib.sha256(exact_csv_bytes(exact_endpoint)).hexdigest()
                record.update({
                    "linear_wall_linf": float(MAX_TRUST) * float(lp.x[-1]),
                    "refinement_success": bool(fit.success),
                    "refinement_message": fit.message,
                    "target_wall_residuals": target_residual.tolist(),
                    "target_wall_residual_max": float(np.max(np.abs(target_residual))),
                    "refined_float_wall_linf": wall_linf,
                    "exact_wall_step": ex.qs(exact_wall_step),
                    "exact_endpoint_linf": exact_endpoint_linf,
                    "eligible_trust_grid": [
                        ex.qs(trust) for trust in TRUST_GRID
                        if exact_endpoint_linf <= float(trust)
                    ],
                    "exact_endpoint_sha256": endpoint_sha,
                    "active_mode_count": int(np.sum(np.abs(refined) > 1e-14)),
                    "largest_active_modes": [
                        {
                            "mode": list(mode_names[index]),
                            "coefficient": float(refined[index]),
                        }
                        for index in np.argsort(np.abs(refined))[-12:][::-1]
                        if abs(refined[index]) > 1e-14
                    ],
                })
                try:
                    audit = endpoint_audit(
                        exact_source,
                        exact_endpoint,
                        faces,
                        labels,
                        source_signature,
                    )
                    audit["checks"]["target_wall_refined"] = (
                        record["target_wall_residual_max"]
                        <= TARGET_RESIDUAL_TOLERANCE
                    )
                    audit["checks"]["linf_at_most_1e_4"] = (
                        exact_endpoint_linf <= float(MAX_TRUST)
                    )
                    audit["passed_check_count"] = sum(audit["checks"].values())
                    audit["required_check_count"] = len(audit["checks"])
                    record["endpoint_audit"] = audit
                    record["accepted_before_first_event_scan"] = all(
                        audit["checks"].values()
                    )
                except Exception as error:
                    record["endpoint_error"] = repr(error)
                    record["accepted_before_first_event_scan"] = False
                endpoints[branch_id] = exact_endpoint
                branches.append(record)

    feasible = [row for row in branches if row["solver_success"]]
    if not feasible:
        raise AssertionError("every bounded LP branch failed to return a primal point")
    preaccepted = [
        row for row in feasible if row.get("accepted_before_first_event_scan")
    ]
    scans = []
    accepted = []
    scan_rows = preaccepted[:]
    if not scan_rows:
        scan_rows = [max(feasible, key=branch_score)]
    for row in scan_rows:
        endpoint = endpoints[row["branch_id"]]
        scan = scan_endpoint(exact_source, endpoint, faces)
        scan_record = {
            "branch_id": row["branch_id"],
            "endpoint_sha256": row["exact_endpoint_sha256"],
            **scan,
        }
        scans.append(scan_record)
        if row.get("accepted_before_first_event_scan") and scan["joint_first_event"]:
            accepted.append(row)

    if accepted:
        chosen = min(accepted, key=lambda row: row["branch_id"])
        write_exact_csv(CANDIDATE_ENDPOINT, endpoints[chosen["branch_id"]])
        endpoint_artifact = {
            "kind": "numerical_candidate_not_exactly_certified",
            "file": relative(CANDIDATE_ENDPOINT),
            "sha256": sha256(CANDIDATE_ENDPOINT),
            "branch_id": chosen["branch_id"],
        }
        verdict = "NUMERICAL_JOINT_U54_H1011_CANDIDATE_FOUND_NOT_EXACTLY_CERTIFIED"
    else:
        chosen = max(feasible, key=branch_score)
        write_exact_csv(RELAXED_ENDPOINT, endpoints[chosen["branch_id"]])
        endpoint_artifact = {
            "kind": "best_relaxed_noncandidate",
            "file": relative(RELAXED_ENDPOINT),
            "sha256": sha256(RELAXED_ENDPOINT),
            "branch_id": chosen["branch_id"],
        }
        verdict = "BOUNDED_JOINT_U54_H1011_SEARCH_NO_ACCEPTED_CANDIDATE"

    payload = {
        "version": 1,
        "scope": (
            "Deterministic full-165D finite numerical search for a shared odd "
            "selected U54-neighbor-1/H1011-t first event from the exact step13 "
            "transfer FAR checkpoint."
        ),
        "source_hashes": {
            relative(SOURCE): sha256(SOURCE),
            relative(FACES): sha256(FACES),
            relative(OBSTRUCTION): sha256(OBSTRUCTION),
        },
        "source_checkpoint": {
            "exact_support": {
                key: value for key, value in exact_support.items() if key != "edges"
            },
            "exact_mechanics": exact_mechanics,
            "numerical_signature": source_signature,
            "selected_decisions": {
                "S": source.face_decisions[base.common.PRIMARY],
                "U54": source.vertex_decisions[54],
                "H56": source.edge_decisions[(5, 6)],
                "H1011": source.edge_decisions[(10, 11)],
            },
        },
        "search_contract": {
            "mode_count": len(modes),
            "physical_coordinate_count": len(displacement),
            "mechanics_decision_count": len(keys),
            "mechanics_guard_count": len(mechanics_rows),
            "mechanics_guard_names_digest": hashlib.sha256(
                "\n".join(mechanics_names).encode()
            ).hexdigest(),
            "near_support_count": len(near_support),
            "all_support_guard_count": len(all_support),
            "in_face_turn_guard_count": len(source_turns),
            "exhaustive_event_primitive_count": 7922,
            "target_raw_rows": {
                key: sorted(value) for key, value in TARGET_ALIASES.items()
            },
            "selected_component_authority": {
                "owner": relative(Path(base.frozen_builder.__file__)),
                "owner_sha256": sha256(Path(base.frozen_builder.__file__)),
                "U54": base.frozen_builder.SELECTED_COMPONENTS["U54"],
                "H1011": base.frozen_builder.SELECTED_COMPONENTS["H1011"],
            },
            "target_jacobian_rank": int(np.linalg.matrix_rank(target_rows)),
            "target_source_raw": source_raw.tolist(),
            "trust_grid": [ex.qs(value) for value in TRUST_GRID],
            "post_factor_grid": [ex.qs(value) for value in POST_FACTOR_GRID],
            "guard_floor_grid": [ex.qs(value) for value in GUARD_FLOOR_GRID],
            "profile_grid": list(PROFILE_GRID),
            "branch_count": len(branches),
            "solver_time_limit_seconds_per_branch": 15,
            "root_tie_tolerance": ROOT_TIE_TOLERANCE,
        },
        "finite_difference_diagnostics": fd_diagnostics,
        "base_plane_normal": plane_normal.tolist(),
        "branches": branches,
        "event_scans": scans,
        "selected_endpoint_artifact": endpoint_artifact,
        "exact_fixed_ledger_obstruction": {
            "receipt": relative(OBSTRUCTION),
            "sha256": sha256(OBSTRUCTION),
            "verdict": obstruction["verdict"],
            "consequence": obstruction["consequence"],
        },
        "negative_scope": (
            "The LP/refinement result is a finite-grid negative, not an LP-dual "
            "or global geometric impossibility claim. The separately bound exact "
            "identity receipt proves only the requested retained-ledger selected-"
            "component invariant."
        ),
        "proof_boundary": (
            "No floating root tie is promoted to an exact shared root. A positive "
            "result would still require exact gcd, multiplicity, Bernstein interval, "
            "and independent post-class verification."
        ),
        "implementation": {
            "search_script": relative(Path(__file__)),
            "search_script_sha256": sha256(Path(__file__)),
            "exact_core_sha256": sha256(Path(ex.__file__)),
            "full_chart_owner_sha256": sha256(Path(base.__file__)),
            "exhaustive_primitive_owner_sha256": sha256(Path(exhaustive.__file__)),
        },
        "verdict": verdict,
    }
    atomic_json(output, payload)
    print(json.dumps({
        "verdict": verdict,
        "branch_count": len(branches),
        "solver_feasible_branch_count": len(feasible),
        "pre_event_accepted_branch_count": len(preaccepted),
        "accepted_candidate_count": len(accepted),
        "selected_endpoint_artifact": endpoint_artifact,
        "first_scanned_event": scans[0]["first_event"] if scans else None,
        "output": str(output),
    }, indent=2, default=json_default))


if __name__ == "__main__":
    main()
