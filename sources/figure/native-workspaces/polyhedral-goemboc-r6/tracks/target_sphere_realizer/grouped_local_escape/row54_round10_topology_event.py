#!/usr/bin/env python3
"""Materialize the first independent topology event after the round-8 detour."""
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


SOURCE = HERE / "row54_combined_hard_slp_round10_double_tangent_best.csv"
OUT = HERE / "row54_round10_topology_event.json"
OLD_QUAD = (7, 8, 245, 246)
ROUND8_QUAD = (9, 198, 263, 264)
# Plane (8,264,246) is approached by row 198 at the terminal checkpoint.
EVENT_QUAD = (8, 264, 246, 198)
ALT_ACUTE_ROUTE = (228, 198, 263, 9, 8)
LEDGER_KEYS = (
    ("U-", 54), ("H-", (6, 7)), ("S-", (7, 8, 245)),
    ("H-", (198, 263)), ("U-", 263), ("H-", (10, 263)),
    ("U-", 1), ("H-", (1, 54)),
)


def label_key(label):
    kind, item = label
    return kind, tuple(sorted(item)) if isinstance(item, list) else item


def main() -> None:
    ids, source = read_points(SOURCE)
    ix = {i: k for k, i in enumerate(ids)}
    direct = DirectActual(ids, source)
    nd = len(direct.controls)
    nvar = nd + 8
    origin = source.mean(axis=0)
    scale0 = float(np.sqrt(np.mean(np.sum((source - origin) ** 2, axis=1))))
    _, faces, _ = core.group_maximal_faces(ids, source)
    source_keys = {frozenset(f) for f in faces}

    def construct(z):
        q = direct.construct(z[:nd])
        qn = (q - origin) / scale0
        theta = z[nd:]
        den = 1.0 + qn @ theta[:3]
        a, b, c, d, e = theta[3:]
        h = np.array([[a, b, c], [b, d, e],
                      [c, e, -a - d]], dtype=float)
        return origin + scale0 * ((qn / den[:, None]) @ expm(h).T)

    def oriented(points, quad):
        q = [np.asarray(points[ix[i]], dtype=np.longdouble) for i in quad]
        return np.dot(q[1] - q[0], np.cross(q[2] - q[0], q[3] - q[0]))

    def rms(points):
        p = np.asarray(points, dtype=np.longdouble)
        q = p - np.mean(p, axis=0)
        return np.sqrt(np.mean(np.sum(q * q, axis=1)))

    def old_guard(points):
        return float(-oriented(points, OLD_QUAD) / rms(points) ** 3)

    def round8_pre_guard(points):
        return float(-oriented(points, ROUND8_QUAD) / rms(points) ** 3)

    def fixed(z):
        points = construct(z)
        g, labels = guards(core.mechanics(ids, points, faces), faces)
        return g, labels, points

    zero = np.zeros(nvar)
    g0, labels, _ = fixed(zero)
    lookup = {label_key(label): k for k, label in enumerate(labels)}
    protected = np.asarray([lookup[("U-", 263)], lookup[("U-", 1)]])
    eps = 2e-6
    jac = np.empty((len(g0), nvar))
    old_grad = np.empty(nvar)
    round8_grad = np.empty(nvar)
    for j in range(nvar):
        dz = np.zeros(nvar)
        dz[j] = eps
        gp, _, pp = fixed(dz)
        gm, _, pm = fixed(-dz)
        jac[:, j] = (gp - gm) / (2 * eps)
        old_grad[j] = (old_guard(pp) - old_guard(pm)) / (2 * eps)
        round8_grad[j] = (
            round8_pre_guard(pp) - round8_pre_guard(pm)
        ) / (2 * eps)

    objective = np.flatnonzero(g0 <= 0.03)
    trust = 1e-4
    lp = linprog(
        np.r_[np.zeros(nvar), -1.0],
        A_ub=np.vstack([
            np.c_[-jac[objective], np.ones(len(objective))],
            np.c_[-jac[protected], np.zeros(len(protected))],
        ]),
        b_ub=np.r_[g0[objective], g0[protected]],
        A_eq=np.c_[np.vstack([old_grad, round8_grad]), np.zeros((2, 1))],
        b_eq=np.zeros(2),
        bounds=[(-trust, trust)] * nvar + [(None, None)], method="highs",
    )
    if not lp.success:
        raise RuntimeError(lp.message)
    direction = lp.x[:-1]
    guard_targets = np.asarray([old_guard(source), round8_pre_guard(source)])
    grad_matrix = np.vstack([old_grad, round8_grad])
    gram = grad_matrix @ grad_matrix.T

    def path(alpha):
        z = float(alpha) * direction
        for _ in range(8):
            p = construct(z)
            error = guard_targets - np.asarray([old_guard(p), round8_pre_guard(p)])
            z += grad_matrix.T @ np.linalg.solve(gram, error)
        return z

    def event_det(alpha):
        return float(oriented(construct(path(alpha)), EVENT_QUAD))

    source_det = event_det(0.0)
    scan = []
    bracket = None
    pa, pd = 0.0, source_det
    for alpha in np.geomspace(1e-12, 1.0, 241):
        alpha = float(alpha)
        points = construct(path(alpha))
        actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
        det = event_det(alpha)
        keys = ({frozenset(f["cycle"]) for f in actual.faces}
                if actual.valid else set())
        scan.append({
            "alpha": alpha,
            "event_oriented_volume": det,
            "fresh_valid": actual.valid,
            "fresh_f_vector": summarize(actual)["f_vector"] if actual.valid else None,
            "fresh_class": summarize(actual)["class"] if actual.valid else None,
            "fresh_topology_margin": actual.topology_margin,
            "same_source_faces": keys == source_keys,
        })
        if det * pd <= 0:
            bracket = (pa, alpha)
            break
        pa, pd = alpha, det
    if bracket is None:
        raise RuntimeError("event determinant did not bracket")
    root = brentq(event_det, *bracket, xtol=1e-16, rtol=1e-14)

    wall_z = path(root)
    wall_points = construct(wall_z)
    a, b, c = [wall_points[ix[i]] for i in EVENT_QUAD[:3]]
    normal = np.cross(b - a, c - a)
    normal /= np.linalg.norm(normal)
    correction = float(np.dot(wall_points[ix[EVENT_QUAD[3]]] - a, normal))
    wall_points[ix[EVENT_QUAD[3]]] -= correction * normal

    # Pick the nearest unambiguously retriangulated far sample.
    far_points = None
    far_alpha = None
    far_actual = None
    for delta in np.geomspace(max(root * 1e-8, 1e-12), 1.0, 220):
        alpha = root + float(delta)
        points = construct(path(alpha))
        actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
        if not actual.valid or set(actual.active) != set(ids):
            continue
        keys = {frozenset(f["cycle"]) for f in actual.faces}
        if keys != source_keys and summarize(actual)["f_vector"] == [61, 162, 103]:
            far_points, far_alpha, far_actual = points, alpha, actual
            break
    if far_points is None:
        raise RuntimeError("no open far cell found")

    def audit(name, points):
        actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
        rec = {"name": name, "fresh_actual": summarize(actual)}
        if not actual.valid:
            return rec
        face_cycles = [f["cycle"] for f in actual.faces]
        g, audit_labels = guards(core.mechanics(ids, points, face_cycles), face_cycles)
        alookup = {label_key(label): k for k, label in enumerate(audit_labels)}
        keys = {frozenset(f["cycle"]) for f in actual.faces}
        edges = set(actual.edges)
        x = {i: points[ix[i]] - actual.centroid for i in ids}

        def path_record(path):
            pairs = list(zip(path, path[1:]))
            return {
                "all_edges_present": all(tuple(sorted(e)) in edges for e in pairs),
                "positive_dot_min": min(float(np.dot(x[a], x[b])) for a, b in pairs),
                "directed_support_min": min(
                    float(np.dot(x[a], x[b] - x[a])) for a, b in pairs
                ),
            }

        return {
            **rec,
            "hard_margin": float(np.min(g)),
            "guard_ledger": {str(k): float(g[alookup[k]])
                             for k in LEDGER_KEYS if k in alookup},
            "base_face_present": BASE in keys,
            "U8_present": 8 in [i for i, _ in actual.unstable],
            "rails": {
                "short_literal": path_record(SHORT_RAIL),
                "long_literal": path_record(LONG_RAIL),
                "alternate_positive_dot": path_record(ALT_ACUTE_ROUTE),
            },
            "old_quad_far_guard": old_guard(points),
            "round8_quad_pre_guard": round8_pre_guard(points),
            "event_oriented_volume": float(oriented(points, EVENT_QUAD)),
        }

    packets = {
        "pre": audit("pre", source),
        "wall": audit("wall", wall_points),
        "far": audit("far", far_points),
    }
    for name, points in (("pre", source), ("wall", wall_points),
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
        "method": "double-topology-tangent 27D LP and independent quad root",
        "source": str(SOURCE),
        "protected_quads": [list(OLD_QUAD), list(ROUND8_QUAD)],
        "event_quad": list(EVENT_QUAD),
        "lp_predicted_hard": float(lp.x[-1]),
        "direction": direction.tolist(),
        "protected_quad_derivatives": [float(old_grad @ direction),
                                       float(round8_grad @ direction)],
        "source_event_oriented_volume": source_det,
        "root_alpha": root,
        "oriented_volume_at_root": event_det(root),
        "wall_projection_correction": correction,
        "far_alpha": far_alpha,
        "removed_faces": [sorted(k) for k in sorted(source_keys - far_keys,
                                                      key=lambda x: sorted(x))],
        "added_faces": [sorted(k) for k in sorted(far_keys - source_keys,
                                                   key=lambda x: sorted(x))],
        "audits": packets,
        "scan": scan,
    }
    OUT.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({
        "event_quad": list(EVENT_QUAD),
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
