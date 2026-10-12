#!/usr/bin/env python3
"""Locate and cross the first support wall after the two birth bypasses."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq, linprog

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
ROOT = PARENT.parents[2]
sys.path[:0] = [str(PARENT), str(ROOT / "tracks/circuit_atlas")]

from actual_grouped import evaluate, summarize  # noqa: E402
from row54_direct_actual_search import DirectActual, read_points  # noqa: E402
from row54_full_minimax import BASE, guards  # noqa: E402
from row54_joint_actual_search import write_csv  # noqa: E402
import row54_four_residual_search as core  # noqa: E402


SOURCE = HERE / "guarded_after_s67245_best.csv"
OUT = HERE / "quad_6_198_244_245_event.json"
EVENT_QUAD = (6, 198, 244, 245)
ALT_ROUTE = (228, 198, 263, 9, 8)
TOPOLOGY_QUADS = (
    ("round4_far", (7, 8, 245, 246), -1.0),
    ("round8_pre", (9, 198, 263, 264), -1.0),
    ("round10_far", (8, 264, 246, 198), 1.0),
    ("round12_far", (198, 263, 262, 11), 1.0),
)
PROTECTED_KEYS = (
    ("U-", 263), ("H-", (10, 263)),
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
    _, source_faces, _ = core.group_maximal_faces(ids, source)
    source_keys = {frozenset(f) for f in source_faces}

    def construct(z):
        q = direct.construct(z[:nd])
        qn = (q - origin) / scale0
        theta = z[nd:]
        den = 1.0 + qn @ theta[:3]
        if np.min(den) <= 0.08:
            return None
        a, b, c, d, e = theta[3:]
        h = np.array([[a, b, c], [b, d, e], [c, e, -a - d]])
        return origin + scale0 * ((qn / den[:, None]) @ expm(h).T)

    def centroid_ld(points):
        p = np.asarray(points, dtype=np.longdouble)
        shift = np.mean(p, axis=0)
        d6 = np.longdouble(0)
        m24 = np.zeros(3, dtype=np.longdouble)
        for cycle in source_faces:
            c = [ix[i] for i in cycle]
            a = p[c[0]] - shift
            for j in range(1, len(c) - 1):
                b = p[c[j]] - shift
                q = p[c[j + 1]] - shift
                det = np.dot(a, np.cross(b, q))
                d6 += det
                m24 += det * (a + b + q)
        return shift + m24 / (4 * d6)

    def geometric_guards(points):
        p = np.asarray(points, dtype=np.longdouble)
        centered = p - np.mean(p, axis=0)
        scale = np.sqrt(np.mean(np.sum(centered * centered, axis=1)))
        vals = []
        for _, quad, sign in TOPOLOGY_QUADS:
            q = [p[ix[i]] for i in quad]
            det = np.dot(q[1] - q[0], np.cross(q[2] - q[0], q[3] - q[0]))
            vals.append(np.longdouble(sign) * det / scale**3)
        c = centroid_ld(p)
        x10, x263 = p[ix[10]] - c, p[ix[263]] - c
        x1, x54 = p[ix[1]] - c, p[ix[54]] - c
        x5, x6 = p[ix[5]] - c, p[ix[6]] - c
        vals.extend((
            -np.dot(x263, x263 - x10),
            np.dot(x1, x54 - x1),
            np.dot(x6, x5 - x6),
        ))
        return np.asarray(vals, dtype=np.longdouble)

    def fixed(z):
        points = construct(z)
        if points is None:
            return None
        values, labels = guards(core.mechanics(ids, points, source_faces), source_faces)
        lookup = {label_key(label): k for k, label in enumerate(labels)}
        dvals = list(np.asarray(geometric_guards(points), float))
        dvals.append(float(values[lookup[("S-", (6, 7, 245))]]))
        return values, labels, points, np.asarray(dvals, float)

    zero = np.zeros(nvar)
    base = fixed(zero)
    if base is None:
        raise RuntimeError("invalid source")
    values0, labels, _, guard_target = base
    lookup = {label_key(label): k for k, label in enumerate(labels)}
    protected = np.asarray([lookup[k] for k in PROTECTED_KEYS])

    eps = 2e-6
    jac = np.empty((len(values0), nvar))
    djac = np.empty((len(guard_target), nvar))
    for j in range(nvar):
        dz = np.zeros(nvar)
        dz[j] = eps
        plus, minus = fixed(dz), fixed(-dz)
        if plus is None or minus is None:
            raise RuntimeError(f"finite difference failed {j}")
        jac[:, j] = (plus[0] - minus[0]) / (2 * eps)
        djac[:, j] = (plus[3] - minus[3]) / (2 * eps)

    objective = np.flatnonzero(values0 <= 0.03)
    trust = 1e-4
    lp = linprog(
        np.r_[np.zeros(nvar), -1.0],
        A_ub=np.vstack([
            np.c_[-jac[objective], np.ones(len(objective))],
            np.c_[-jac[protected], np.zeros(len(protected))],
        ]),
        b_ub=np.r_[values0[objective], values0[protected] - 3e-9],
        A_eq=np.c_[djac, np.zeros((len(guard_target), 1))],
        b_eq=np.zeros(len(guard_target)),
        bounds=[(-trust, trust)] * nvar + [(None, None)], method="highs",
    )
    if not lp.success:
        raise RuntimeError(lp.message)
    direction = lp.x[:-1]
    gram = djac @ djac.T

    def projected(alpha):
        z = float(alpha) * direction
        for _ in range(14):
            packet = fixed(z)
            if packet is None:
                raise RuntimeError("projection left chart")
            error = guard_target - packet[3]
            if np.max(np.abs(error)) < 2e-16:
                break
            z += djac.T @ np.linalg.solve(gram, error)
        return z

    def oriented(points):
        p = np.asarray(points, dtype=np.longdouble)
        q = [p[ix[i]] for i in EVENT_QUAD]
        return np.dot(q[1] - q[0], np.cross(q[2] - q[0], q[3] - q[0]))

    def event_value(alpha):
        return float(oriented(construct(projected(alpha))))

    source_det = event_value(0.0)
    bracket = None
    scan = []
    previous_alpha, previous_det = 0.0, source_det
    for alpha in np.geomspace(1e-12, 64.0, 360):
        alpha = float(alpha)
        z = projected(alpha)
        points = construct(z)
        actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
        det = float(oriented(points))
        keys = {frozenset(f["cycle"]) for f in actual.faces} if actual.valid else set()
        scan.append({
            "alpha": alpha,
            "event_determinant": det,
            "valid": actual.valid,
            "f_vector": summarize(actual)["f_vector"] if actual.valid else None,
            "class": summarize(actual)["class"] if actual.valid else None,
            "same_source_faces": keys == source_keys,
            "topology_margin": actual.topology_margin,
        })
        if det * previous_det <= 0:
            bracket = (previous_alpha, alpha)
            break
        previous_alpha, previous_det = alpha, det
    if bracket is None:
        raise RuntimeError("event determinant did not bracket")
    root = brentq(event_value, *bracket, xtol=1e-15, rtol=1e-14)

    # The source is already a strict open pre-cell and has a substantially
    # larger directed determinant than a tolerance-sized root offset.
    pre_alpha = 0.0
    pre_points = source.copy()
    wall_points = construct(projected(root))
    a, b, c = [wall_points[ix[i]] for i in EVENT_QUAD[:3]]
    normal = np.cross(b - a, c - a)
    normal /= np.linalg.norm(normal)
    correction = float(np.dot(wall_points[ix[EVENT_QUAD[3]]] - a, normal))
    wall_points[ix[EVENT_QUAD[3]]] -= correction * normal

    far_points = None
    far_alpha = None
    far_keys_target = None
    for delta in np.geomspace(max(root * 1e-7, 1e-10),
                              max(root * 100.0, 1e-2), 340):
        alpha = root + float(delta)
        points = construct(projected(alpha))
        actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
        if not actual.valid or set(actual.active) != set(ids):
            continue
        keys = {frozenset(f["cycle"]) for f in actual.faces}
        if keys != source_keys and summarize(actual)["f_vector"] == [61, 162, 103]:
            if far_keys_target is None:
                far_keys_target = keys
                far_points, far_alpha = points, alpha
            elif keys != far_keys_target:
                break
            if keys == far_keys_target and actual.topology_margin > 1e-10:
                far_points, far_alpha = points, alpha
                break
    if far_points is None:
        raise RuntimeError("no strict far cell found")

    def audit(name, points):
        actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
        rec = {"name": name, "fresh_actual": summarize(actual)}
        if not actual.valid:
            return rec
        cycles = [f["cycle"] for f in actual.faces]
        values, audit_labels = guards(core.mechanics(ids, points, cycles), cycles)
        alookup = {label_key(label): k for k, label in enumerate(audit_labels)}
        edges = set(actual.edges)
        centered = {i: points[ix[i]] - actual.centroid for i in ids}
        route_pairs = list(zip(ALT_ROUTE, ALT_ROUTE[1:]))
        keys = {frozenset(f["cycle"]) for f in actual.faces}
        geom = np.asarray(geometric_guards(points), float)
        s_guard = float(values[alookup[("S-", (6, 7, 245))]])
        return {
            **rec,
            "hard": float(np.min(values)),
            "all_rows_active": set(actual.active) == set(ids),
            "base_face_present": BASE in keys,
            "protected_u8": 8 in [i for i, _ in actual.unstable],
            "alternate_route": {
                "path": list(ALT_ROUTE),
                "all_edges_present": all(tuple(sorted(e)) in edges for e in route_pairs),
                "positive_dot_min": min(float(np.dot(centered[a], centered[b]))
                                        for a, b in route_pairs),
            },
            "inherited_guards": geom.tolist() + [s_guard],
            "protected_mechanics": {
                str(k): float(values[alookup[k]]) for k in PROTECTED_KEYS
            },
            "event_determinant": float(oriented(points)),
        }

    packets = {
        "pre": audit("pre", pre_points),
        "wall": audit("wall", wall_points),
        "far": audit("far", far_points),
    }
    for name, points in (("pre", pre_points), ("wall", wall_points), ("far", far_points)):
        write_csv(OUT.with_name(OUT.stem + f"_{name}.csv"), ids, points)
        actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
        OUT.with_name(OUT.stem + f"_{name}_faces.json").write_text(
            json.dumps([f["cycle"] for f in actual.faces], indent=2) + "\n"
        )

    pre_actual = evaluate(dict(zip(ids, pre_points)), coplanar_rel=1e-11)
    far_actual = evaluate(dict(zip(ids, far_points)), coplanar_rel=1e-11)
    pre_keys = {frozenset(f["cycle"]) for f in pre_actual.faces}
    far_keys = {frozenset(f["cycle"]) for f in far_actual.faces}
    out = {
        "version": 1,
        "method": "eight-guard tangent LP with projected directed support crossing",
        "source": str(SOURCE),
        "event_quad": list(EVENT_QUAD),
        "guard_names": [q[0] for q in TOPOLOGY_QUADS] +
                       ["U263_H10_263", "U1_H1_54", "U6_H5_6", "S67245_H7_245"],
        "guard_target": guard_target.tolist(),
        "guard_jacobian_rank": int(np.linalg.matrix_rank(djac)),
        "guard_tangent_nullity": int(nvar - np.linalg.matrix_rank(djac)),
        "lp_predicted_hard": float(lp.x[-1]),
        "direction": direction.tolist(),
        "source_event_determinant": source_det,
        "root_bracket": list(bracket),
        "root_alpha": root,
        "root_residual": event_value(root),
        "wall_projection_correction": correction,
        "far_alpha": far_alpha,
        "removed_faces": [sorted(k) for k in sorted(pre_keys - far_keys, key=lambda x: sorted(x))],
        "added_faces": [sorted(k) for k in sorted(far_keys - pre_keys, key=lambda x: sorted(x))],
        "audits": packets,
        "scan": scan,
    }
    OUT.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({
        "event_quad": list(EVENT_QUAD),
        "root_alpha": root,
        "root_residual": out["root_residual"],
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
