#!/usr/bin/env python3
"""Raise the U6/H(5,6) no-birth margin in the guarded far cell.

The direction is chosen in the nullspace of the four target residuals and all
six inherited directed guards.  The nonlinear path is projected back onto
those ten source levels and every sample rebuilds the actual hull and centroid.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
from scipy.linalg import expm, null_space

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
ROOT = PARENT.parents[2]
sys.path[:0] = [str(PARENT), str(ROOT / "tracks/circuit_atlas")]

from actual_grouped import evaluate, summarize  # noqa: E402
from row54_direct_actual_search import DirectActual, read_points  # noqa: E402
from row54_full_minimax import BASE, SHORT_RAIL, guards  # noqa: E402
from row54_joint_actual_search import write_csv  # noqa: E402
import row54_four_residual_search as core  # noqa: E402


SOURCE = HERE / "guarded_continuation_best.csv"
OUTPUT = HERE / "birth6_guard_buffer.json"
ALT_ROUTE = (228, 198, 263, 9, 8)
TOPOLOGY_QUADS = (
    ("round4_far", (7, 8, 245, 246), -1.0),
    ("round8_pre", (9, 198, 263, 264), -1.0),
    ("round10_far", (8, 264, 246, 198), 1.0),
    ("round12_far", (198, 263, 262, 11), 1.0),
)
TARGET_KEYS = (
    ("U-", 54), ("H-", (6, 7)),
    ("S-", (7, 8, 245)), ("H-", (198, 263)),
)
PROTECTED_KEYS = (
    ("U-", 263), ("H-", (10, 263)),
    ("U-", 1), ("H-", (1, 54)),
)


def label_key(label):
    kind, item = label
    return kind, tuple(sorted(item)) if isinstance(item, list) else item


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, default=SOURCE)
    ap.add_argument("--output", type=Path, default=OUTPUT)
    ap.add_argument("--floor", type=float, default=5e-9)
    ap.add_argument("--epsilon", type=float, default=2e-6)
    ap.add_argument("--mode", choices=("u6", "s67245"), default="u6")
    args = ap.parse_args()

    ids, source = read_points(args.source)
    ix = {i: k for k, i in enumerate(ids)}
    direct = DirectActual(ids, source)
    nd = len(direct.controls)
    nvar = nd + 8
    origin = source.mean(axis=0)
    scale0 = float(np.sqrt(np.mean(np.sum((source - origin) ** 2, axis=1))))
    _, faces, _ = core.group_maximal_faces(ids, source)
    face_keys = {frozenset(f) for f in faces}

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
        for cycle in faces:
            c = [ix[i] for i in cycle]
            a = p[c[0]] - shift
            for j in range(1, len(c) - 1):
                b = p[c[j]] - shift
                q = p[c[j + 1]] - shift
                det = np.dot(a, np.cross(b, q))
                d6 += det
                m24 += det * (a + b + q)
        return shift + m24 / (4 * d6)

    def u6_guard(points):
        p = np.asarray(points, dtype=np.longdouble)
        c = centroid_ld(p)
        x5, x6 = p[ix[5]] - c, p[ix[6]] - c
        return np.dot(x6, x5 - x6)

    def inherited(points):
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
        vals.extend((-np.dot(x263, x263 - x10), np.dot(x1, x54 - x1)))
        if args.mode == "s67245":
            vals.append(u6_guard(p))
        return np.asarray(vals, dtype=np.longdouble)

    def packet(z):
        points = construct(z)
        if points is None:
            return None
        values, labels = guards(core.mechanics(ids, points, faces), faces)
        if args.mode == "u6":
            new = float(u6_guard(points))
        else:
            local_lookup = {label_key(label): k for k, label in enumerate(labels)}
            new = float(values[local_lookup[("S-", (6, 7, 245))]])
        return values, labels, points, np.asarray(inherited(points), float), new

    zero = np.zeros(nvar)
    base = packet(zero)
    if base is None:
        raise RuntimeError("invalid source")
    values0, labels, _, inherited0, birth0 = base
    lookup = {label_key(label): k for k, label in enumerate(labels)}
    target_idx = np.asarray([lookup[k] for k in TARGET_KEYS])
    protected_idx = np.asarray([lookup[k] for k in PROTECTED_KEYS])

    jac = np.empty((len(values0), nvar))
    inherited_jac = np.empty((len(inherited0), nvar))
    birth_jac = np.empty(nvar)
    for j in range(nvar):
        dz = np.zeros(nvar)
        dz[j] = args.epsilon
        plus, minus = packet(dz), packet(-dz)
        if plus is None or minus is None:
            raise RuntimeError(f"finite difference failed {j}")
        jac[:, j] = (plus[0] - minus[0]) / (2 * args.epsilon)
        inherited_jac[:, j] = (plus[3] - minus[3]) / (2 * args.epsilon)
        birth_jac[j] = (plus[4] - minus[4]) / (2 * args.epsilon)

    constraints = np.vstack([jac[target_idx], inherited_jac])
    ns = null_space(constraints)
    projected = ns @ (ns.T @ birth_jac)
    response = float(birth_jac @ projected)
    if not response > 1e-18:
        raise RuntimeError(f"new guard has no transverse response: {response}")
    desired = args.floor - birth0
    direction = projected * (desired / response)
    target_levels = np.r_[values0[target_idx], inherited0]
    gram = constraints @ constraints.T

    def project(z):
        z = np.asarray(z, float).copy()
        for _ in range(14):
            p = packet(z)
            if p is None:
                return None
            error = target_levels - np.r_[p[0][target_idx], p[3]]
            if np.max(np.abs(error)) < 2e-15:
                break
            z += constraints.T @ np.linalg.solve(gram, error)
        return z

    source_actual = evaluate(dict(zip(ids, source)), coplanar_rel=1e-11)
    source_signature = (
        tuple(tuple(source_actual.faces[i]["cycle"]) for i, _ in source_actual.stable),
        tuple(i for i, _ in source_actual.unstable),
        tuple(e for e, _ in source_actual.saddles),
    )

    def audit(z, name):
        p = packet(z)
        if p is None:
            return {"name": name, "valid": False, "failures": ["packet"]}
        values, audit_labels, points, old, new = p
        actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
        if not actual.valid:
            return {"name": name, "valid": False, "failures": [actual.error]}
        keys = {frozenset(f["cycle"]) for f in actual.faces}
        signature = (
            tuple(tuple(actual.faces[i]["cycle"]) for i, _ in actual.stable),
            tuple(i for i, _ in actual.unstable),
            tuple(e for e, _ in actual.saddles),
        )
        edges = set(actual.edges)
        centered = {i: points[ix[i]] - actual.centroid for i in ids}
        route_pairs = list(zip(ALT_ROUTE, ALT_ROUTE[1:]))
        route_min = min(float(np.dot(centered[a], centered[b])) for a, b in route_pairs)
        failures = []
        if set(actual.active) != set(ids): failures.append("active_rows")
        if keys != face_keys: failures.append("face_cell")
        if signature != source_signature: failures.append("mechanics_signature")
        if BASE not in keys: failures.append("base")
        if not all(tuple(sorted(e)) in edges for e in zip(SHORT_RAIL, SHORT_RAIL[1:])):
            failures.append("short_rail")
        if not all(tuple(sorted(e)) in edges for e in route_pairs) or route_min <= 0:
            failures.append("alternate_route")
        if actual.topology_margin <= 1e-12: failures.append("topology_margin")
        if np.any(old <= 0): failures.append("inherited_guards")
        if np.any(values[protected_idx] <= 3e-9): failures.append("protected_mechanics")
        if new <= 0: failures.append("new_birth_guard")
        return {
            "name": name,
            "valid": not failures,
            "failures": failures,
            "parameters": np.asarray(z).tolist(),
            "fresh_actual": summarize(actual),
            "hard": float(np.min(values)),
            "target_values": values[target_idx].tolist(),
            "target_level_error": (values[target_idx] - values0[target_idx]).tolist(),
            "inherited_guards": old.tolist(),
            "inherited_level_error": (old - inherited0).tolist(),
            "new_birth_guard": new,
            "protected_mechanics": values[protected_idx].tolist(),
            "alternate_route_positive_dot_min": route_min,
        }

    chosen = None
    scan = []
    for alpha in np.geomspace(1e-3, 32.0, 260):
        z = project(float(alpha) * direction)
        rec = audit(z, f"scan_{alpha:.6e}") if z is not None else {"valid": False}
        scan.append({
            "alpha": float(alpha), "valid": rec.get("valid", False),
            "new_birth_guard": rec.get("new_birth_guard"),
            "class": rec.get("fresh_actual", {}).get("class"),
            "topology_margin": rec.get("fresh_actual", {}).get("topology_margin"),
            "failures": rec.get("failures"),
        })
        if rec.get("valid") and rec["new_birth_guard"] >= args.floor:
            chosen = (float(alpha), z, rec)
            break
    if chosen is None:
        raise RuntimeError("no guarded birth6 buffer found")
    alpha, z_buffer, buffer_rec = chosen

    path = []
    for k, t in enumerate(np.linspace(0.0, 1.0, 101)):
        z = project(float(t) * z_buffer)
        rec = audit(z, f"path_{k:03d}")
        path.append(rec)
    path_ok = all(r["valid"] for r in path)
    if not path_ok:
        raise RuntimeError("projected buffer path is not fully guarded")

    points_buffer = construct(z_buffer)
    write_csv(args.output.with_name(args.output.stem + "_source.csv"), ids, source)
    write_csv(args.output.with_name(args.output.stem + "_buffer.csv"), ids, points_buffer)
    actual_buffer = evaluate(dict(zip(ids, points_buffer)), coplanar_rel=1e-11)
    args.output.with_name(args.output.stem + "_buffer_faces.json").write_text(
        json.dumps([f["cycle"] for f in actual_buffer.faces], indent=2) + "\n"
    )
    out = {
        "version": 1,
        "method": ("U6/H56" if args.mode == "u6" else "S[6,7,245]/H(7,245)") +
                  " no-birth buffer in the guarded target-nullspace",
        "mode": args.mode,
        "source": str(args.source),
        "target_keys": [[k, list(v) if isinstance(v, tuple) else v] for k, v in TARGET_KEYS],
        "inherited_guard_names": ([q[0] for q in TOPOLOGY_QUADS] +
                                  ["U263_H10_263", "U1_H1_54"] +
                                  (["U6_H5_6"] if args.mode == "s67245" else [])),
        "constraint_rank": int(np.linalg.matrix_rank(constraints)),
        "nullspace_dimension": int(ns.shape[1]),
        "birth_gradient_projected_norm": float(np.linalg.norm(projected)),
        "birth_response": response,
        "source_new_birth_guard": birth0,
        "requested_floor": args.floor,
        "accepted_alpha": alpha,
        "direction": direction.tolist(),
        "source": audit(zero, "source"),
        "buffer": buffer_rec,
        "path": path,
        "path_all_open_class222": path_ok,
        "scan": scan,
    }
    args.output.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({
        "constraint_rank": out["constraint_rank"],
        "nullspace_dimension": out["nullspace_dimension"],
        "source_new_birth_guard": birth0,
        "buffer_new_birth_guard": buffer_rec["new_birth_guard"],
        "accepted_alpha": alpha,
        "path_ok": path_ok,
        "hard_change": buffer_rec["hard"] - out["source"]["hard"],
        "minimum_topology_margin": min(r["fresh_actual"]["topology_margin"] for r in path),
    }, indent=2))


if __name__ == "__main__":
    main()
