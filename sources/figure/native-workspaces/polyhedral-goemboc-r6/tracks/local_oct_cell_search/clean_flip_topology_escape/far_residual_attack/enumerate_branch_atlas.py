#!/usr/bin/env python3
"""Enumerate all 144 residual edge-cone branches in the complete affine chart."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.optimize import linprog

import attack_common as c


def canonical_hash(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def label_json(label):
    kind, item = label
    return [kind, list(item) if isinstance(item, tuple) else item]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--trust", type=float, default=0.02)
    ap.add_argument("--mechanics-floor", type=float, default=0.0)
    ap.add_argument("--interior-factor", type=float, default=0.5)
    ap.add_argument("--output", type=Path, default=c.HERE / "branch_atlas.json")
    args = ap.parse_args()
    if not 0.0 < args.interior_factor < 1.0:
        raise ValueError("interior factor must lie strictly between zero and one")

    ids, points = c.read_float_points()
    faces = c.read_faces()
    controls, scale = c.full_controls(ids, points)
    zero = np.zeros(len(controls))

    def residual_at(z):
        packet = c.residual_components(
            ids, c.construct(points, ids, controls, z), faces
        )
        return c.flatten_residual_components(packet)[1]

    def guards_at(z):
        return c.class_guard_packet(
            ids, c.construct(points, ids, controls, z), faces
        )[0]

    residual_labels, _ = c.flatten_residual_components(
        c.residual_components(ids, points, faces)
    )
    residual_values, residual_jac = c.finite_difference_jacobian(
        residual_at, zero
    )
    guard_values, guard_jac = c.finite_difference_jacobian(guards_at, zero)
    _, guard_labels = c.class_guard_packet(ids, points, faces)
    target_guard_indices = set(c.target_guard_indices(guard_labels))
    protected_indices = [
        k for k in range(len(guard_labels)) if k not in target_guard_indices
    ]
    support_rows, support_values, support_jac = c.support_first_jet(
        ids, points, faces, controls, scale
    )

    residual_lookup = {label: k for k, label in enumerate(residual_labels)}
    face_choices = [
        label for label in residual_labels if label[0] == "S198_243_245"
    ]
    vertex_choices = [label for label in residual_labels if label[0] == "U1"]
    h45_choices = [label for label in residual_labels if label[0] == "H4_5"]
    h1213_choices = [label for label in residual_labels if label[0] == "H12_13"]
    branches = list(
        itertools.product(
            face_choices, vertex_choices, h45_choices, h1213_choices
        )
    )
    if len(branches) != 144:
        raise AssertionError(len(branches))

    n = len(controls)
    # Exact first-jet box screening.  For a row a.x + margin >= 0 and
    # |x_j|<=trust, margin-trust*||a||_1 is its literal box minimum.  Rows
    # with a positive minimum cannot bind any branch and need not be handed
    # to HiGHS; they remain represented in the full support digest below.
    support_radius = args.trust * np.asarray(
        np.abs(support_jac).sum(axis=1)
    ).ravel()
    support_keep = np.flatnonzero(support_values - support_radius <= 0.0)
    protected_all_jac = sparse.csr_matrix(guard_jac[protected_indices])
    protected_all_values = guard_values[protected_indices]
    mechanics_radius = args.trust * np.asarray(
        np.abs(protected_all_jac).sum(axis=1)
    ).ravel()
    mechanics_keep = np.flatnonzero(
        protected_all_values - mechanics_radius <= float(args.mechanics_floor)
    )
    protected_jac = protected_all_jac[mechanics_keep]
    protected_rhs = (
        protected_all_values[mechanics_keep] - float(args.mechanics_floor)
    )
    a_common = sparse.vstack(
        (-support_jac[support_keep], -protected_jac), format="csr"
    )
    b_common = np.r_[support_values[support_keep], protected_rhs]
    records = []
    best = None
    print(
        "atlas",
        len(branches),
        "branches",
        n,
        "controls",
        len(support_rows),
        "support rows",
        len(support_keep),
        "box-relevant",
        len(protected_indices),
        "mechanics rows",
        len(mechanics_keep),
        "box-relevant",
        flush=True,
    )
    for branch_index, branch in enumerate(branches):
        indices = [residual_lookup[label] for label in branch]
        target_block = sparse.csr_matrix(
            np.c_[residual_jac[indices], residual_values[indices]]
        )
        common_block = sparse.hstack(
            (a_common, sparse.csr_matrix((a_common.shape[0], 1))),
            format="csr",
        )
        a_ub = sparse.vstack((common_block, target_block), format="csr")
        b_ub = np.r_[b_common, np.zeros(4)]
        # Normalize each inequality by its own coefficient/RHS scale.  The
        # raw ledger spans many orders of magnitude; leaving this to solver
        # defaults produced status-4 numerical failures, not mathematical
        # infeasibility.  This is an equivalent positive row scaling.
        coefficient_scale = np.asarray(
            np.abs(a_ub).max(axis=1).toarray()
        ).ravel()
        row_scale = np.maximum.reduce(
            (coefficient_scale, np.abs(b_ub), np.full(len(b_ub), 1e-30))
        )
        scaled_a = sparse.diags(1.0 / row_scale) @ a_ub
        scaled_b = b_ub / row_scale
        lp = linprog(
            np.r_[np.zeros(n), -1.0],
            A_ub=scaled_a,
            b_ub=scaled_b,
            bounds=[(-args.trust, args.trust)] * n + [(None, None)],
            method="highs-ds",
            options={
                "primal_feasibility_tolerance": 1e-9,
                "dual_feasibility_tolerance": 1e-9,
            },
        )
        record = {
            "index": branch_index,
            "components": [label_json(label) for label in branch],
            "component_values": residual_values[indices].tolist(),
            "success": bool(lp.success),
            "status": int(lp.status),
            "message": str(lp.message),
        }
        if lp.success:
            raw_direction = np.asarray(lp.x[:-1], dtype=float)
            direction = args.interior_factor * raw_direction
            support_after = support_values + support_jac @ direction
            mechanics_after = (
                guard_values[protected_indices]
                + guard_jac[protected_indices] @ direction
            )
            target_after = (
                residual_values[indices] + residual_jac[indices] @ direction
            )
            active_support = np.argsort(support_after)[:12]
            realized_relative_descent = float(
                np.min(
                    -residual_jac[indices] @ direction
                    / residual_values[indices]
                )
            )
            record.update(
                {
                    "solver_boundary_relative_descent": float(lp.x[-1]),
                    "interior_factor": args.interior_factor,
                    "relative_descent": realized_relative_descent,
                    "direction": direction.tolist(),
                    "nonzero_direction_count": int(
                        np.count_nonzero(np.abs(direction) > 1e-12)
                    ),
                    "target_linearized_after": target_after.tolist(),
                    "minimum_support_linearized_after": float(
                        np.min(support_after)
                    ),
                    "minimum_protected_mechanics_linearized_after": float(
                        np.min(mechanics_after)
                    ),
                    "active_support_candidates": [
                        {
                            "row": int(k),
                            "value": float(support_after[k]),
                            "face_index": support_rows[k].face_index,
                            "face": list(support_rows[k].face),
                            "witness": support_rows[k].witness,
                            "triple": list(support_rows[k].triple),
                        }
                        for k in active_support
                    ],
                }
            )
            rank_key = (
                float(lp.x[-1]),
                float(np.min(mechanics_after)),
                -int(np.count_nonzero(np.abs(direction) > 1e-12)),
            )
            if best is None or rank_key > best[0]:
                best = (rank_key, branch_index)
        records.append(record)
        if branch_index % 24 == 23:
            print("completed", branch_index + 1, flush=True)

    success_count = sum(record["success"] for record in records)
    ranked = sorted(
        (
            record
            for record in records
            if record["success"]
        ),
        key=lambda record: (
            record["relative_descent"],
            record["minimum_protected_mechanics_linearized_after"],
        ),
        reverse=True,
    )
    payload = {
        "version": 1,
        "method": (
            "complete 165D enlarged-base-preserving affine first-jet atlas; "
            "all 3*3*4*4 residual edge-cone branches"
        ),
        "source": str((c.PARENT / "far.csv").relative_to(c.ROOT)),
        "source_faces": str((c.PARENT / "far_faces.json").relative_to(c.ROOT)),
        "trust": args.trust,
        "mechanics_floor": args.mechanics_floor,
        "interior_factor": args.interior_factor,
        "control_count": n,
        "control_labels": [control.name for control in controls],
        "support_row_count": len(support_rows),
        "box_relevant_support_row_count": len(support_keep),
        "protected_mechanics_row_count": len(protected_indices),
        "box_relevant_protected_mechanics_row_count": len(mechanics_keep),
        "residual_component_labels": [
            label_json(label) for label in residual_labels
        ],
        "residual_component_values": residual_values.tolist(),
        "branch_count": len(records),
        "successful_branch_count": success_count,
        "failed_branch_count": len(records) - success_count,
        "best_branch_index": None if best is None else best[1],
        "top_branch_indices": [record["index"] for record in ranked[:12]],
        "support_ledger_digest": canonical_hash(
            [
                [
                    row.face_index,
                    list(row.face),
                    row.witness,
                    list(row.triple),
                    row.orientation,
                    format(float(value), ".17g"),
                ]
                for row, value in zip(support_rows, support_values)
            ]
        ),
        "branches": records,
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(
        json.dumps(
            {
                "branch_count": payload["branch_count"],
                "successful_branch_count": success_count,
                "best_branch_index": payload["best_branch_index"],
                "top_branch_indices": payload["top_branch_indices"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
