#!/usr/bin/env python3
"""Find a sparse ray for the four currently active residual components."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.optimize import linprog

import attack_common as c


ACTIVE_LABELS = (
    ("S198_243_245", (198, 243)),
    ("U1", 2),
    ("H4_5", "one_minus_t"),
    ("H12_13", "one_minus_t"),
)


def row_scale(matrix, rhs):
    coefficient_scale = np.asarray(
        np.abs(matrix).max(axis=1).toarray()
    ).ravel()
    scale = np.maximum.reduce(
        (coefficient_scale, np.abs(rhs), np.full(len(rhs), 1e-30))
    )
    return sparse.diags(1.0 / scale) @ matrix, rhs / scale


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--trust", type=float, default=1e-6)
    ap.add_argument("--target-relative", type=float, default=1e-6)
    ap.add_argument("--retention", type=float, default=0.25)
    ap.add_argument("--output", type=Path, default=c.HERE / "active_sparse_ray.json")
    args = ap.parse_args()
    if not 0.0 < args.retention < 1.0:
        raise ValueError("retention must be in (0,1)")

    ids, points = c.read_float_points()
    faces = c.read_faces()
    controls, scale = c.full_controls(ids, points)
    zero = np.zeros(len(controls))

    def residual_at(z):
        return c.flatten_residual_components(
            c.residual_components(
                ids, c.construct(points, ids, controls, z), faces
            )
        )[1]

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

    lookup = {label: k for k, label in enumerate(residual_labels)}
    target_indices = [lookup[label] for label in ACTIVE_LABELS]
    n = len(controls)
    # Rows unable to approach the retained fraction anywhere in the trust box
    # are mathematically redundant for this LP.
    support_radius = args.trust * np.asarray(
        np.abs(support_jac).sum(axis=1)
    ).ravel()
    support_keep = np.flatnonzero(
        (1.0 - args.retention) * support_values - support_radius <= 0.0
    )
    protected_jac = sparse.csr_matrix(guard_jac[protected_indices])
    protected_values = guard_values[protected_indices]
    mechanics_radius = args.trust * np.asarray(
        np.abs(protected_jac).sum(axis=1)
    ).ravel()
    mechanics_keep = np.flatnonzero(
        (1.0 - args.retention) * protected_values - mechanics_radius <= 0.0
    )

    # Variables are d (signed chart direction) and u>=|d|.  Minimize sum(u)
    # subject to a fixed simultaneous relative decrease of all four active
    # components and a strict retained fraction of every local guard.
    blocks = []
    rhs = []
    blocks.append(
        sparse.hstack(
            (-support_jac[support_keep], sparse.csr_matrix((len(support_keep), n)))
        )
    )
    rhs.append((1.0 - args.retention) * support_values[support_keep])
    blocks.append(
        sparse.hstack(
            (
                -protected_jac[mechanics_keep],
                sparse.csr_matrix((len(mechanics_keep), n)),
            )
        )
    )
    rhs.append(
        (1.0 - args.retention) * protected_values[mechanics_keep]
    )
    blocks.append(
        sparse.hstack(
            (
                sparse.csr_matrix(residual_jac[target_indices]),
                sparse.csr_matrix((4, n)),
            )
        )
    )
    rhs.append(-args.target_relative * residual_values[target_indices])
    identity = sparse.identity(n, format="csr")
    blocks.append(sparse.hstack((identity, -identity)))
    rhs.append(np.zeros(n))
    blocks.append(sparse.hstack((-identity, -identity)))
    rhs.append(np.zeros(n))
    a_ub = sparse.vstack(blocks, format="csr")
    b_ub = np.concatenate(rhs)
    scaled_a, scaled_b = row_scale(a_ub, b_ub)
    lp = linprog(
        np.r_[np.zeros(n), np.ones(n)],
        A_ub=scaled_a,
        b_ub=scaled_b,
        bounds=[(-args.trust, args.trust)] * n + [(0.0, args.trust)] * n,
        method="highs-ds",
        options={
            "primal_feasibility_tolerance": 1e-9,
            "dual_feasibility_tolerance": 1e-9,
        },
    )
    if not lp.success:
        raise RuntimeError((lp.status, lp.message))
    direction = np.asarray(lp.x[:n], dtype=float)
    target_after = (
        residual_values[target_indices] + residual_jac[target_indices] @ direction
    )
    support_after = support_values + support_jac @ direction
    protected_after = (
        protected_values + guard_jac[protected_indices] @ direction
    )
    endpoint = c.construct(points, ids, controls, direction)
    actual = c.fresh_summary(ids, endpoint)
    endpoint_faces = {frozenset(face["cycle"]) for face in actual.faces}
    endpoint_edges = set(actual.edges)
    nonzero = np.flatnonzero(np.abs(direction) > 1e-13)
    payload = {
        "version": 1,
        "method": (
            "L1-minimum ray in the complete 165D affine chart for the four "
            "currently active residual components"
        ),
        "trust": args.trust,
        "target_relative": args.target_relative,
        "retention": args.retention,
        "chart_scale": scale,
        "control_count": n,
        "support_row_count": len(support_rows),
        "box_relevant_support_row_count": len(support_keep),
        "protected_mechanics_row_count": len(protected_indices),
        "box_relevant_protected_mechanics_row_count": len(mechanics_keep),
        "active_components": [
            [kind, list(item) if isinstance(item, tuple) else item]
            for kind, item in ACTIVE_LABELS
        ],
        "active_component_values": residual_values[target_indices].tolist(),
        "active_component_linearized_after": target_after.tolist(),
        "realized_relative_decrease": (
            (residual_values[target_indices] - target_after)
            / residual_values[target_indices]
        ).tolist(),
        "l1_norm": float(np.sum(np.abs(direction))),
        "nonzero_direction_count": len(nonzero),
        "direction": direction.tolist(),
        "nonzero_controls": [
            {
                "index": int(j),
                "label": controls[j].name,
                "coefficient": float(direction[j]),
            }
            for j in nonzero
        ],
        "minimum_support_linearized_after": float(np.min(support_after)),
        "minimum_protected_mechanics_linearized_after": float(
            np.min(protected_after)
        ),
        "fresh_endpoint": {
            "f_vector": [len(actual.active), len(actual.edges), len(actual.faces)],
            "class": [
                len(actual.stable),
                len(actual.unstable),
                len(actual.saddles),
            ],
            "active_labels": actual.active,
            "base_present": c.BASE in endpoint_faces,
            "missing_rails": [
                list(edge) for edge in sorted(c.rail_edges() - endpoint_edges)
            ],
            "topology_margin": float(actual.topology_margin),
        },
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(
        json.dumps(
            {
                "nonzero_direction_count": len(nonzero),
                "nonzero_controls": payload["nonzero_controls"],
                "relative_decrease": payload["realized_relative_decrease"],
                "fresh_endpoint": payload["fresh_endpoint"],
                "sha256": hashlib.sha256(args.output.read_bytes()).hexdigest(),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
