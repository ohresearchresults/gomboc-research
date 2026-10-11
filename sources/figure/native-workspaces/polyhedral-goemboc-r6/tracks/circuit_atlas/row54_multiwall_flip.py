#!/usr/bin/env python3
"""Cross the first compensating topology wall without losing either rail.

Starting from the best guarded four-defect packet, solve a rank-revealing
linear program that crosses only the two support walls of quad
{2,3,88,242}.  The LP minimizes L1 base motion, keeps every other fixed-cell
support/convexity guard nonnegative, and is then checked nonlinearly in both
the well-conditioned projective preimage and the final metric coordinates.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

import materialize_row54_cells as material
import row54_four_residual_search as core
import row54_guarded_escape as guarded


HERE = Path(__file__).resolve().parent
START = HERE / "row54_guarded_from_831551.json"
EPSILON = 1.0e-8
FD_STEP = 1.0e-5
TRUST = 1.0e-3


def preimage(problem: guarded.Problem, source: np.ndarray, x: np.ndarray):
    q = source.copy()
    for k, i in enumerate(guarded.BASE_CYCLE):
        du, dv = x[8 + 2 * k: 8 + 2 * k + 2]
        q[problem.chart.ix[i]] += problem.chart.base_scales[i] * (
            du * problem.chart.base_u + dv * problem.chart.base_v
        )
    return q


def write_csv(path, ids, points):
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(("source_id", "x", "y", "z"))
        for i, p in zip(ids, points):
            w.writerow([i, *[format(float(v), ".17g") for v in p]])


def main():
    ids, source, old_faces = guarded.load_problem()
    problem = guarded.Problem(ids, source, old_faces)
    start = json.load(START.open())
    x0 = np.asarray(start["best"]["parameters"], dtype=float)
    q0 = preimage(problem, source, x0)
    top0, labels = guarded.topology_guards(ids, q0, old_faces)

    wall = np.asarray([
        k for k, label in enumerate(labels)
        if label[0] == "support" and (
            (label[2] == [3, 242, 2] and label[3] == 88)
            or (label[2] == [88, 2, 242] and label[3] == 3)
        )
    ], dtype=int)
    if len(wall) != 2:
        raise AssertionError(wall)
    keep = np.asarray([k for k in range(len(top0)) if k not in set(wall)], dtype=int)

    jac = np.zeros((len(top0), 36))
    for j in range(36):
        xp = x0.copy()
        xm = x0.copy()
        xp[8 + j] += FD_STEP
        xm[8 + j] -= FD_STEP
        gp, lp = guarded.topology_guards(ids, preimage(problem, source, xp), old_faces)
        gm, lm = guarded.topology_guards(ids, preimage(problem, source, xm), old_faces)
        if lp != labels or lm != labels:
            raise AssertionError("topology labels changed")
        jac[:, j] = (gp - gm) / (2.0 * FD_STEP)

    # Variables are delta[36], abs_delta[36].
    scale = np.maximum(top0, 1.0e-7)
    aub, bub = [], []
    for k in wall:
        aub.append(np.r_[jac[k] / scale[k], np.zeros(36)])
        bub.append((-EPSILON - top0[k]) / scale[k])
    for k in keep:
        aub.append(np.r_[-jac[k] / scale[k], np.zeros(36)])
        bub.append(top0[k] / scale[k])
    aub.extend(np.c_[np.eye(36), -np.eye(36)])
    bub.extend(np.zeros(36))
    aub.extend(np.c_[-np.eye(36), -np.eye(36)])
    bub.extend(np.zeros(36))
    objective = np.r_[np.zeros(36), np.ones(36)]
    lp = linprog(
        objective,
        A_ub=np.asarray(aub),
        b_ub=np.asarray(bub),
        bounds=[(-TRUST, TRUST)] * 36 + [(0.0, TRUST)] * 36,
        method="highs",
    )
    if not lp.success:
        raise RuntimeError(lp.message)

    x = x0.copy()
    x[8:] += lp.x[:36]
    q = preimage(problem, source, x)
    points, den = problem.chart.coordinates(x)
    crossed_old_guards, _ = guarded.topology_guards(ids, q, old_faces)
    if not np.all(crossed_old_guards[wall] < 0.0):
        raise AssertionError(crossed_old_guards[wall])
    if not np.all(crossed_old_guards[keep] > 0.0):
        raise AssertionError(float(np.min(crossed_old_guards[keep])))

    pre_hull, new_faces, pre_normals = core.group_maximal_faces(ids, q)
    pre_edges, _ = core.edge_lattice(new_faces)
    forced = guarded.forced_rail_edges()
    assert [len(pre_hull.vertices), len(pre_edges), len(new_faces)] == [61, 162, 103]
    assert forced <= set(pre_edges)
    assert (2, 242) not in pre_edges and (3, 88) in pre_edges
    assert frozenset(guarded.BASE_CYCLE) in {frozenset(c) for c in new_faces}

    final_hull, final_faces, final_normals = core.group_maximal_faces(ids, points)
    final_edges, _ = core.edge_lattice(final_faces)
    assert [len(final_hull.vertices), len(final_edges), len(final_faces)] == [61, 162, 103]
    assert {frozenset(c) for c in final_faces} == {frozenset(c) for c in new_faces}
    assert forced <= set(final_edges)

    mechanics, stable, unstable, saddles = core.classify(ids, points, final_faces)
    expected_stable = {core.BASE, frozenset((198, 243, 244))}
    expected_unstable = {2, 8}
    expected_saddles = {(4, 5), (12, 13)}
    assert {frozenset(c) for c in stable} == expected_stable
    assert set(unstable) == expected_unstable
    assert {tuple(e) for e in saddles} == expected_saddles
    margins = material.requested_margins(
        mechanics, final_faces, {core.BASE}, {8}, set()
    )
    final_topology = material.topology_audit(ids, points, final_faces, final_normals)
    pre_topology_values, pre_topology_labels = guarded.topology_guards(ids, q, new_faces)

    pre_csv = HERE / "row54_multiwall_flip_preimage.csv"
    final_csv = HERE / "row54_multiwall_flip.csv"
    faces_json = HERE / "row54_multiwall_flip_faces.json"
    audit_json = HERE / "row54_multiwall_flip_audit.json"
    write_csv(pre_csv, ids, q)
    write_csv(final_csv, ids, points)
    json.dump(final_faces, faces_json.open("w"), indent=2)
    record = {
        "version": 1,
        "verdict": "CLEAN_COMPENSATING_QUAD_FLIP_PRESERVES_ALL61_AND_FORCED_RAILS",
        "source": START.name,
        "old_diagonal": [2, 242],
        "new_diagonal": [3, 88],
        "quad_vertices": [2, 3, 88, 242],
        "crossed_old_support_guards": [
            {
                "label": labels[k],
                "before": float(top0[k]),
                "linear_prediction": float(top0[k] + jac[k] @ lp.x[:36]),
                "after": float(crossed_old_guards[k]),
            }
            for k in wall
        ],
        "guarded_lp": {
            "success": bool(lp.success),
            "message": str(lp.message),
            "epsilon": EPSILON,
            "fd_step": FD_STEP,
            "trust": TRUST,
            "l1_motion": float(np.sum(np.abs(lp.x[:36]))),
            "base_control_delta": lp.x[:36].tolist(),
            "nonzero_controls": [
                {
                    "name": problem.chart.names[8 + k],
                    "value": float(v),
                }
                for k, v in enumerate(lp.x[:36]) if abs(v) > 1e-15
            ],
            "minimum_uncrossed_old_topology_guard": float(np.min(crossed_old_guards[keep])),
        },
        "full_parameters": x.tolist(),
        "minimum_projective_denominator": float(np.min(den)),
        "preimage": {
            "coordinates": pre_csv.name,
            "f_vector": [len(pre_hull.vertices), len(pre_edges), len(new_faces)],
            "minimum_new_cell_topology_guard": float(np.min(pre_topology_values)),
            "worst_new_cell_topology_guards": [
                {"value": float(v), "label": lab}
                for v, lab in sorted(
                    zip(pre_topology_values, pre_topology_labels), key=lambda z: z[0]
                )[:24]
            ],
        },
        "final": {
            "coordinates": final_csv.name,
            "fixed_expected_faces": faces_json.name,
            "f_vector": [len(final_hull.vertices), len(final_edges), len(final_faces)],
            "active": mechanics["active"],
            "centroid": mechanics["centroid"].tolist(),
            "class": [len(stable), len(unstable), len(saddles)],
            "stable_faces": stable,
            "unstable_vertices": unstable,
            "saddle_edges": saddles,
            "all_forced_rail_edges_present": forced <= set(final_edges),
            "forced_rail_edges": [list(e) for e in sorted(forced)],
            "all_target_mechanics_margins": margins,
            "topology_audit": final_topology,
        },
    }
    json.dump(record, audit_json.open("w"), indent=2)
    print(json.dumps({
        "verdict": record["verdict"],
        "old_to_new_diagonal": [[2, 242], [3, 88]],
        "l1_motion": record["guarded_lp"]["l1_motion"],
        "nonzero_controls": record["guarded_lp"]["nonzero_controls"],
        "preimage_topology_min": record["preimage"]["minimum_new_cell_topology_guard"],
        "f_vector": record["final"]["f_vector"],
        "class": record["final"]["class"],
        "stable_faces": stable,
        "unstable_vertices": unstable,
        "saddle_edges": saddles,
        "hard_target_margin": margins["hard_requested_margin"],
    }, indent=2))


if __name__ == "__main__":
    main()
