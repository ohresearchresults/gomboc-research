#!/usr/bin/env python3
"""Search a full-control descent ray that moves away from rail wall 255--256.

This is a numerical proposer only.  It reads the frozen exact source cell and
never treats optimizer status as a proof.  Every proposed route must later be
rationalized and audited by an exact builder plus an independent verifier.

The declared chart is the complete 165-dimensional enlarged-base-preserving
affine chart from ``attack_common.full_controls``.  In addition to retaining
all source support and non-target class guards, the LP requires both oriented
support representatives of circuit {69,224,255,256} to have nonnegative (or
strictly positive) first derivative.  The old sparse ray has the opposite
sign, so a successful route is not a continuation through its rail-deleting
wall.
"""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.optimize import linprog


HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
sys.path.insert(0, str(PARENT))

import attack_common as c  # noqa: E402


SOURCE = PARENT / "exact_event_source.csv"
FACES = PARENT / "exact_event_source_faces.json"
OLD_RAY = PARENT / "active_sparse_ray.json"
OUTPUT = HERE / "full_control_search.json"
ENDPOINT = HERE / "full_control_candidate_float.csv"

ACTIVE_LABELS = (
    ("S198_243_245", (198, 243)),
    ("U1", 2),
    ("H4_5", "one_minus_t"),
    ("H12_13", "one_minus_t"),
)
CIRCUIT_ROWS = {(57, 69), (58, 224)}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_exact_float(path: Path):
    rows = {}
    with path.open(newline="") as stream:
        for row in csv.DictReader(stream):
            rows[int(row["source_id"])] = np.asarray(
                [float(Q(row[key])) for key in ("x", "y", "z")], dtype=float
            )
    ids = sorted(rows)
    return ids, np.asarray([rows[label] for label in ids], dtype=float)


def write_float_csv(path: Path, ids, points) -> None:
    with path.open("w", newline="") as stream:
        out = csv.writer(stream)
        out.writerow(("source_id", "x", "y", "z"))
        for label, xyz in zip(ids, points):
            out.writerow((label, *(format(float(value), ".17g") for value in xyz)))


def scaled_rows(matrix, rhs):
    matrix = sparse.csr_matrix(matrix)
    coefficient_scale = np.asarray(np.abs(matrix).max(axis=1).toarray()).ravel()
    scale = np.maximum.reduce(
        (coefficient_scale, np.abs(rhs), np.full(len(rhs), 1e-30))
    )
    return sparse.diags(1.0 / scale) @ matrix, rhs / scale


def box_relevant(values, jacobian, trust, retention):
    radius = trust * np.asarray(np.abs(jacobian).sum(axis=1)).ravel()
    return np.flatnonzero((1.0 - retention) * values - radius <= 0.0)


def solve_scenario(
    *,
    trust,
    retention,
    circuit_gain,
    orthogonal_to_old,
    residual_values,
    residual_jac,
    guard_values,
    guard_jac,
    protected_indices,
    support_values,
    support_jac,
    circuit_indices,
    old_direction,
    active_indices,
):
    n = len(old_direction)
    support_keep = box_relevant(
        support_values, support_jac, trust, retention
    )
    protected_values = guard_values[protected_indices]
    protected_jac = sparse.csr_matrix(guard_jac[protected_indices])
    mechanics_keep = box_relevant(
        protected_values, protected_jac, trust, retention
    )

    # Solve in the dimensionless variable y=d/trust.  Dividing every retained
    # guard row by its own positive source value turns the right-hand side into
    # the O(1) number 1-retention.  This avoids accepting absolute 1e-15
    # violations of the tiny circuit-adjacent supports as LP tolerance noise.
    blocks = []
    rhs = []
    support_relative = sparse.diags(1.0 / support_values[support_keep]) @ (
        trust * support_jac[support_keep]
    )
    blocks.append(
        sparse.hstack(
            (
                -support_relative,
                sparse.csr_matrix((len(support_keep), 1)),
            ),
            format="csr",
        )
    )
    rhs.append(np.full(len(support_keep), 1.0 - retention))
    mechanics_relative = sparse.diags(1.0 / protected_values[mechanics_keep]) @ (
        trust * protected_jac[mechanics_keep]
    )
    blocks.append(
        sparse.hstack(
            (
                -mechanics_relative,
                sparse.csr_matrix((len(mechanics_keep), 1)),
            ),
            format="csr",
        )
    )
    rhs.append(np.full(len(mechanics_keep), 1.0 - retention))

    # Keep every one of the fourteen target-family components strictly
    # positive at the linearized endpoint, not merely the four selected ones.
    blocks.append(
        sparse.csr_matrix(
            np.c_[
                -trust * residual_jac / residual_values[:, None],
                np.zeros(len(residual_values)),
            ]
        )
    )
    rhs.append(np.full(len(residual_values), 1.0 - retention))

    old_circuit_slopes = np.asarray(
        support_jac[circuit_indices] @ old_direction
    ).ravel()
    circuit_scale = np.abs(old_circuit_slopes)
    if np.any(circuit_scale <= 0.0):
        raise AssertionError("old ray has a zero circuit slope")
    circuit_lower = circuit_gain * circuit_scale
    blocks.append(
        sparse.hstack(
            (
                -trust
                * sparse.diags(1.0 / circuit_scale)
                @ support_jac[circuit_indices],
                sparse.csr_matrix((len(circuit_indices), 1)),
            ),
            format="csr",
        )
    )
    rhs.append(np.full(len(circuit_indices), -circuit_gain))

    # gamma is a common relative first-order decrease of the four active
    # components: J_i d + value_i * gamma <= 0.
    blocks.append(
        sparse.csr_matrix(
            np.c_[
                trust
                * residual_jac[active_indices]
                / residual_values[active_indices, None],
                np.ones(len(active_indices)),
            ]
        )
    )
    rhs.append(np.zeros(len(active_indices)))

    a_ub = sparse.vstack(blocks, format="csr")
    b_ub = np.concatenate(rhs)
    a_eq = None
    b_eq = None
    if orthogonal_to_old:
        norm = float(np.linalg.norm(old_direction))
        if not norm:
            raise AssertionError("old direction is zero")
        # This explicit search restriction guarantees a genuinely different
        # chart direction.  It is not needed by the later exact certificate.
        a_eq = np.r_[old_direction / norm, 0.0][None, :]
        b_eq = np.zeros(1)

    lp = linprog(
        np.r_[np.zeros(n), -1.0],
        A_ub=a_ub,
        b_ub=b_ub,
        A_eq=a_eq,
        b_eq=b_eq,
        bounds=[(-1.0, 1.0)] * n + [(0.0, None)],
        method="highs-ds",
        options={
            "primal_feasibility_tolerance": 1e-9,
            "dual_feasibility_tolerance": 1e-9,
        },
    )
    record = {
        "trust": trust,
        "retention": retention,
        "circuit_gain_over_old_opposite_slope": circuit_gain,
        "orthogonal_to_old": orthogonal_to_old,
        "support_rows_in_solver": int(len(support_keep)),
        "mechanics_rows_in_solver": int(len(mechanics_keep)),
        "success": bool(lp.success),
        "status": int(lp.status),
        "message": str(lp.message),
    }
    if not lp.success:
        return record, None

    direction = trust * np.asarray(lp.x[:-1], dtype=float)
    support_after = support_values + support_jac @ direction
    mechanics_after = protected_values + protected_jac @ direction
    residual_after = residual_values + residual_jac @ direction
    circuit_slopes = np.asarray(
        support_jac[circuit_indices] @ direction
    ).ravel()
    old_norm = float(np.linalg.norm(old_direction))
    direction_norm = float(np.linalg.norm(direction))
    cosine = float(np.dot(direction, old_direction) / (direction_norm * old_norm))
    active_relative = (
        (residual_values[active_indices] - residual_after[active_indices])
        / residual_values[active_indices]
    )
    linear_valid = bool(
        np.min(support_after / support_values) >= retention - 2e-8
        and np.min(mechanics_after / protected_values) >= retention - 2e-8
        and np.min(residual_after / residual_values) >= retention - 2e-8
        and np.min(circuit_slopes - circuit_lower) >= -2e-22
        and np.min(active_relative) >= float(lp.x[-1]) - 2e-8
    )
    record.update(
        {
            "gamma": float(lp.x[-1]),
            "direction_l1": float(np.sum(np.abs(direction))),
            "direction_l2": direction_norm,
            "nonzero_control_count": int(np.count_nonzero(np.abs(direction) > 1e-12)),
            "cosine_with_old_sparse_ray": cosine,
            "circuit_slopes": circuit_slopes.tolist(),
            "circuit_required_lower": circuit_lower.tolist(),
            "linear_primal_valid": linear_valid,
            "minimum_support_ratio_linearized": float(
                np.min(support_after / support_values)
            ),
            "minimum_protected_mechanics_ratio_linearized": float(
                np.min(mechanics_after / protected_values)
            ),
            "minimum_residual_ratio_linearized": float(
                np.min(residual_after / residual_values)
            ),
            "active_relative_decrease_linearized": active_relative.tolist(),
        }
    )
    return record, direction


def main() -> None:
    ids, points = read_exact_float(SOURCE)
    faces = json.loads(FACES.read_text())
    old_payload = json.loads(OLD_RAY.read_text())
    old_direction = np.asarray(old_payload["direction"], dtype=float)
    controls, chart_scale = c.full_controls(ids, points)
    if len(controls) != len(old_direction):
        raise AssertionError("chart dimension drift")
    zero = np.zeros(len(controls))

    def residual_at(coefficients):
        return c.flatten_residual_components(
            c.residual_components(
                ids, c.construct(points, ids, controls, coefficients), faces
            )
        )[1]

    def guards_at(coefficients):
        return c.class_guard_packet(
            ids, c.construct(points, ids, controls, coefficients), faces
        )[0]

    residual_labels, _ = c.flatten_residual_components(
        c.residual_components(ids, points, faces)
    )
    residual_values, residual_jac = c.finite_difference_jacobian(
        residual_at, zero, epsilon=2e-7
    )
    guard_values, guard_jac = c.finite_difference_jacobian(
        guards_at, zero, epsilon=2e-7
    )
    _, guard_labels = c.class_guard_packet(ids, points, faces)
    target_guard_indices = set(c.target_guard_indices(guard_labels))
    protected_indices = np.asarray(
        [k for k in range(len(guard_labels)) if k not in target_guard_indices],
        dtype=int,
    )
    if np.any(guard_values[protected_indices] <= 0.0):
        raise AssertionError("protected source mechanics guard is nonpositive")
    support_rows, support_values, support_jac = c.support_first_jet(
        ids, points, faces, controls, chart_scale
    )
    circuit_indices = np.asarray(
        [
            k
            for k, row in enumerate(support_rows)
            if (row.face_index, row.witness) in CIRCUIT_ROWS
        ],
        dtype=int,
    )
    if len(circuit_indices) != 2:
        raise AssertionError(("circuit support row mismatch", circuit_indices))

    lookup = {label: k for k, label in enumerate(residual_labels)}
    active_indices = np.asarray([lookup[label] for label in ACTIVE_LABELS], dtype=int)
    scenarios = []
    candidates = []
    # This finite family is declared up front.  There is no semantic fallback:
    # every status is retained, and selection is by one fixed ranking below.
    for trust in (2e-7, 5e-7, 1e-6, 2e-6):
        for circuit_gain in (1.0, 0.25, 0.0):
            for orthogonal in (True, False):
                record, direction = solve_scenario(
                    trust=trust,
                    retention=0.25,
                    circuit_gain=circuit_gain,
                    orthogonal_to_old=orthogonal,
                    residual_values=residual_values,
                    residual_jac=residual_jac,
                    guard_values=guard_values,
                    guard_jac=guard_jac,
                    protected_indices=protected_indices,
                    support_values=support_values,
                    support_jac=support_jac,
                    circuit_indices=circuit_indices,
                    old_direction=old_direction,
                    active_indices=active_indices,
                )
                record["index"] = len(scenarios)
                scenarios.append(record)
                if direction is not None:
                    candidates.append((record, direction))
                print(
                    "scenario",
                    record["index"],
                    record["success"],
                    record.get("gamma"),
                    flush=True,
                )

    linear_candidates = [
        item for item in candidates if item[0].get("linear_primal_valid")
    ]
    if not linear_candidates:
        payload = {
            "version": 1,
            "type": "numerical-proposer-no-certificate",
            "verdict": "NO_VALIDATED_LINEAR_PRIMAL_WITNESS_IN_DECLARED_GRID",
            "source_sha256": sha256(SOURCE),
            "faces_sha256": sha256(FACES),
            "old_ray_sha256": sha256(OLD_RAY),
            "scenarios": scenarios,
        }
        OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
        print(payload["verdict"])
        return

    # Prefer an explicitly orthogonal route, then a circuit slope at least as
    # large as the old ray's opposite slope, then common descent.  Check the
    # nonlinear materialized endpoint in that fixed order; a solver flag alone
    # never selects the route.
    ranked_candidates = sorted(
        linear_candidates,
        key=lambda item: (
            item[0]["orthogonal_to_old"],
            item[0]["circuit_gain_over_old_opposite_slope"],
            item[0]["gamma"],
            min(item[0]["circuit_slopes"]),
        ),
        reverse=True,
    )
    selected = None
    for record, direction in ranked_candidates:
        endpoint = c.construct(points, ids, controls, direction)
        try:
            actual = c.fresh_summary(ids, endpoint, coplanar_rel=2e-12)
        except Exception as error:  # diagnostic only; never an obstruction
            record["actual_checked"] = True
            record["actual_valid"] = False
            record["actual_error"] = repr(error)
            continue
        actual_residual = residual_at(direction)
        actual_relative = (
            (residual_values[active_indices] - actual_residual[active_indices])
            / residual_values[active_indices]
        )
        endpoint_edges = set(actual.edges)
        endpoint_face_keys = {frozenset(face["cycle"]) for face in actual.faces}
        actual_f_vector = [len(actual.active), len(actual.edges), len(actual.faces)]
        actual_class = [
            len(actual.stable),
            len(actual.unstable),
            len(actual.saddles),
        ]
        missing_rails = sorted(c.rail_edges() - endpoint_edges)
        actual_valid = bool(
            actual_f_vector == [61, 162, 103]
            and actual_class == [2, 2, 2]
            and sorted(actual.active) == ids
            and c.BASE in endpoint_face_keys
            and not missing_rails
            and float(np.min(actual_relative)) > 0.0
        )
        record.update(
            {
                "actual_checked": True,
                "actual_valid": actual_valid,
                "actual_active_relative_decrease": actual_relative.tolist(),
                "actual_f_vector": actual_f_vector,
                "actual_class": actual_class,
                "actual_topology_margin": float(actual.topology_margin),
                "actual_base_present": c.BASE in endpoint_face_keys,
                "actual_missing_rails": [list(edge) for edge in missing_rails],
            }
        )
        if actual_valid:
            selected = (record, direction, endpoint)
            break

    if selected is None:
        payload = {
            "version": 1,
            "type": "numerical-proposer-no-certificate",
            "verdict": "NO_MATERIALIZED_PRIMAL_WITNESS_IN_DECLARED_GRID",
            "source_sha256": sha256(SOURCE),
            "faces_sha256": sha256(FACES),
            "old_ray_sha256": sha256(OLD_RAY),
            "scenarios": scenarios,
        }
        OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
        print(payload["verdict"])
        return

    selected_record0, selected_direction, endpoint = selected
    selected_record = dict(selected_record0)
    selected_record.update(
        {
            "direction": selected_direction.tolist(),
            "nonzero_controls": [
                {
                    "index": int(k),
                    "label": controls[k].name,
                    "coefficient": float(selected_direction[k]),
                }
                for k in np.flatnonzero(np.abs(selected_direction) > 1e-12)
            ],
        }
    )
    write_float_csv(ENDPOINT, ids, endpoint)
    payload = {
        "version": 1,
        "type": "numerical-proposer-no-certificate",
        "verdict": "FULL_CONTROL_RAIL_SEPARATING_PRIMAL_WITNESS_FOUND",
        "scope": (
            "Numerical first-jet proposer only; exact materialization and "
            "complete interval verification are mandatory before use."
        ),
        "source_sha256": sha256(SOURCE),
        "faces_sha256": sha256(FACES),
        "old_ray_sha256": sha256(OLD_RAY),
        "chart_scale": chart_scale,
        "control_count": len(controls),
        "support_row_count": len(support_rows),
        "protected_mechanics_guard_count": len(protected_indices),
        "residual_component_count": len(residual_values),
        "active_labels": [
            [kind, list(item) if isinstance(item, tuple) else item]
            for kind, item in ACTIVE_LABELS
        ],
        "circuit": [69, 224, 255, 256],
        "circuit_support_rows": [
            {
                "row_index": int(k),
                "face_index": support_rows[k].face_index,
                "witness": support_rows[k].witness,
                "source_value": float(support_values[k]),
                "old_sparse_slope": float(
                    np.asarray(support_jac[k] @ old_direction).ravel()[0]
                ),
            }
            for k in circuit_indices
        ],
        "scenarios": scenarios,
        "selected": selected_record,
        "endpoint_file": ENDPOINT.name,
        "endpoint_sha256": sha256(ENDPOINT),
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(payload["verdict"])
    print("selected_scenario", selected_record["index"])
    print("gamma", selected_record["gamma"])
    print("circuit_slopes", selected_record["circuit_slopes"])
    print("cosine_with_old", selected_record["cosine_with_old_sparse_ray"])
    print("actual_relative_decrease", selected_record["actual_active_relative_decrease"])
    print("actual_f_vector", selected_record["actual_f_vector"])
    print("actual_class", selected_record["actual_class"])
    print("missing_rails", selected_record["actual_missing_rails"])
    print("output_sha256", sha256(OUTPUT))


if __name__ == "__main__":
    main()
