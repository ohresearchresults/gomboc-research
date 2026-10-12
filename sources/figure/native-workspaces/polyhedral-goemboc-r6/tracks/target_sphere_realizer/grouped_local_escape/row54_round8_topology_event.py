#!/usr/bin/env python3
"""Locate the independent {9,198,263,264} topology wall after round 8."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq, linprog

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(ROOT / "tracks/circuit_atlas")]

from actual_grouped import evaluate, summarize  # noqa: E402
from row54_direct_actual_search import DirectActual, read_points  # noqa: E402
from row54_full_minimax import BASE, LONG_RAIL, SHORT_RAIL, guards  # noqa: E402
from row54_joint_actual_search import write_csv  # noqa: E402
import row54_four_residual_search as core  # noqa: E402

SOURCE = HERE / "row54_combined_hard_slp_far_round8_projected_tangent_best.csv"
OUT = HERE / "row54_round8_topology_event.json"
OLD_QUAD = (7, 8, 245, 246)
NEW_QUAD = (9, 198, 263, 264)


def label_key(label):
    kind, item = label
    return kind, tuple(sorted(item)) if isinstance(item, list) else item


def main() -> None:
    ids, source = read_points(SOURCE)
    direct = DirectActual(ids, source)
    n_direct = len(direct.controls)
    _, source_faces, _ = core.group_maximal_faces(ids, source)
    source_keys = {frozenset(f) for f in source_faces}
    origin = source.mean(axis=0)
    scale = float(np.sqrt(np.mean(np.sum((source - origin) ** 2, axis=1))))
    local = {i: k for k, i in enumerate(ids)}
    n = n_direct + 8

    def construct(z):
        q = direct.construct(z[:n_direct])
        qn = (q - origin) / scale
        theta = z[n_direct:]
        den = 1.0 + qn @ theta[:3]
        a, b, c, d, e = theta[3:]
        h = np.array([[a, b, c], [b, d, e],
                      [c, e, -a - d]], dtype=float)
        return origin + scale * ((qn / den[:, None]) @ expm(h).T)

    def oriented(points, quad):
        q = [points[local[i]] for i in quad]
        return float(np.dot(q[1] - q[0],
                            np.cross(q[2] - q[0], q[3] - q[0])))

    def normalized_old_guard(points):
        s = float(np.sqrt(np.mean(np.sum(
            (points - points.mean(axis=0)) ** 2, axis=1))))
        return -oriented(points, OLD_QUAD) / s**3

    def fixed(z):
        points = construct(z)
        g, labels = guards(core.mechanics(ids, points, source_faces),
                           source_faces)
        return g, labels, points

    zero = np.zeros(n)
    g0, labels, _ = fixed(zero)
    lookup = {label_key(label): k for k, label in enumerate(labels)}
    protected_indices = [lookup[("U-", 263)], lookup[("U-", 1)]]
    epsilon = 2e-6
    jac = np.empty((len(g0), n))
    old_grad = np.empty(n)
    for j in range(n):
        step = np.zeros(n)
        step[j] = epsilon
        gp, _, pp = fixed(step)
        gm, _, pm = fixed(-step)
        jac[:, j] = (gp - gm) / (2 * epsilon)
        old_grad[j] = (
            normalized_old_guard(pp) - normalized_old_guard(pm)
        ) / (2 * epsilon)

    objective = np.flatnonzero(g0 <= 0.05)
    trust = 1e-4
    a_ub = [np.c_[-jac[objective], np.ones(len(objective))],
            np.c_[-jac[protected_indices], np.zeros(len(protected_indices))]]
    b_ub = [g0[objective], g0[protected_indices]]
    lp = linprog(
        np.r_[np.zeros(n), -1.0],
        A_ub=np.vstack(a_ub), b_ub=np.concatenate(b_ub),
        A_eq=np.c_[old_grad[None, :], np.zeros((1, 1))],
        b_eq=np.zeros(1),
        bounds=[(-trust, trust)] * n + [(None, None)],
        method="highs",
    )
    if not lp.success:
        raise RuntimeError(lp.message)
    direction = lp.x[:-1]
    old_target = normalized_old_guard(source)
    old_grad_sq = float(np.dot(old_grad, old_grad))

    def path(alpha):
        z = alpha * direction
        for _ in range(6):
            points = construct(z)
            error = old_target - normalized_old_guard(points)
            z += (error / old_grad_sq) * old_grad
        return z

    def new_det(alpha):
        return oriented(construct(path(alpha)), NEW_QUAD)

    source_det = new_det(0.0)
    scan = []
    bracket = None
    previous_alpha, previous_det = 0.0, source_det
    for alpha in np.geomspace(1e-10, 1.0, 151):
        det = new_det(float(alpha))
        points = construct(path(float(alpha)))
        actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
        scan.append({
            "alpha": float(alpha),
            "oriented_volume": det,
            "fresh_valid": actual.valid,
            "fresh_f_vector": summarize(actual)["f_vector"] if actual.valid else None,
            "fresh_class": summarize(actual)["class"] if actual.valid else None,
            "fresh_topology_margin": actual.topology_margin,
        })
        if det * previous_det <= 0:
            bracket = (previous_alpha, float(alpha))
            break
        previous_alpha, previous_det = float(alpha), det
    if bracket is None:
        raise RuntimeError("new topology wall not bracketed")
    root = brentq(new_det, *bracket, xtol=1e-16, rtol=1e-14)

    # Exact grouped wall: project vertex 264 onto plane (9,198,263).
    wall_z = path(root)
    wall_points = construct(wall_z)
    a, b, c = [wall_points[local[i]] for i in (9, 198, 263)]
    normal = np.cross(b - a, c - a)
    normal /= np.linalg.norm(normal)
    correction = float(np.dot(wall_points[local[264]] - a, normal))
    wall_points[local[264]] -= correction * normal

    pre_points = source.copy()
    pre_actual = evaluate(dict(zip(ids, pre_points)), coplanar_rel=1e-11)
    pre_keys = {frozenset(f["cycle"]) for f in pre_actual.faces}
    far_points = None
    far_alpha = None
    far_actual = None
    for delta in np.geomspace(max(root * 1e-8, 1e-10), 1.0, 180):
        alpha = root + float(delta)
        points = construct(path(alpha))
        actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
        if not actual.valid or set(actual.active) != set(ids):
            continue
        keys = {frozenset(f["cycle"]) for f in actual.faces}
        # Skip the finite coplanar grouping band; require the open, retriangulated
        # far cell rather than mistaking the grouped quadrilateral wall for it.
        if (keys != pre_keys
                and summarize(actual)["f_vector"] == [61, 162, 103]):
            far_points, far_alpha, far_actual = points, alpha, actual
            break
    if far_points is None:
        raise RuntimeError("no fresh far topology cell found")

    def audit(name, points):
        actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
        result = summarize(actual)
        if not actual.valid:
            return {"name": name, "fresh_actual": result}
        face_cycles = [f["cycle"] for f in actual.faces]
        g, audit_labels = guards(core.mechanics(ids, points, face_cycles),
                                 face_cycles)
        audit_lookup = {label_key(label): k
                        for k, label in enumerate(audit_labels)}
        ledger_keys = (("U-", 54), ("H-", (6, 7)),
                       ("H-", (198, 263)), ("U-", 263),
                       ("H-", (10, 263)), ("U-", 1),
                       ("H-", (1, 54)))
        edges = set(actual.edges)
        keys = {frozenset(f["cycle"]) for f in actual.faces}
        return {
            "name": name,
            "fresh_actual": result,
            "hard_margin": float(np.min(g)),
            "guard_ledger": {str(k): float(g[audit_lookup[k]])
                             for k in ledger_keys if k in audit_lookup},
            "old_quad_guard": normalized_old_guard(points),
            "new_quad_oriented_volume": oriented(points, NEW_QUAD),
            "base_face_present": BASE in keys,
            "rail_edges_present": {
                rail_name: all(tuple(sorted(e)) in edges
                               for e in zip(rail, rail[1:]))
                for rail_name, rail in (("short", SHORT_RAIL),
                                        ("long", LONG_RAIL))
            },
        }

    packets = {
        "pre": audit("pre", pre_points),
        "wall": audit("wall", wall_points),
        "far": audit("far", far_points),
    }
    for name, points in (("pre", pre_points), ("wall", wall_points),
                         ("far", far_points)):
        write_csv(OUT.with_name(OUT.stem + f"_{name}.csv"), ids, points)
        actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
        if actual.valid:
            OUT.with_name(OUT.stem + f"_{name}_faces.json").write_text(
                json.dumps([f["cycle"] for f in actual.faces], indent=2) + "\n"
            )

    far_keys = {frozenset(f["cycle"]) for f in far_actual.faces}
    out = {
        "version": 1,
        "method": "far-wall tangent LP plus independent quad root",
        "source": str(SOURCE),
        "old_quad": list(OLD_QUAD),
        "new_quad": list(NEW_QUAD),
        "lp_predicted_hard": float(lp.x[-1]),
        "direction": direction.tolist(),
        "old_quad_gradient_dot_direction": float(old_grad @ direction),
        "source_new_oriented_volume": source_det,
        "root_alpha": root,
        "oriented_volume_at_root": new_det(root),
        "wall_projection_correction": correction,
        "far_alpha": far_alpha,
        "removed_faces": [sorted(k) for k in sorted(pre_keys - far_keys,
                                                      key=lambda x: sorted(x))],
        "added_faces": [sorted(k) for k in sorted(far_keys - pre_keys,
                                                   key=lambda x: sorted(x))],
        "audits": packets,
        "scan": scan,
    }
    OUT.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({
        "root_alpha": root,
        "oriented_volume_at_root": out["oriented_volume_at_root"],
        "wall_projection_correction": correction,
        "far_alpha": far_alpha,
        "removed_faces": out["removed_faces"],
        "added_faces": out["added_faces"],
        "pre": packets["pre"],
        "wall": packets["wall"],
        "far": packets["far"],
    }, indent=2))


if __name__ == "__main__":
    main()
