#!/usr/bin/env python3
"""Turn away from the round-8 quad wall in the full 27D identity chart.

This is deliberately a pre-cell continuation, not a claim that the sign of
det(9,198,263,264) can change while the old 263--264 rail edge is retained.
One planar axis increases the directed pre-side determinant while annihilating
the six mechanical-ledger rows and the earlier quad guard to first order.  A
second axis is tangent to both topology walls and improves the four residual
target guards.  Fresh grouped hulls certify an L-shaped detour and four local
quadrants in the original open cell.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from scipy.linalg import expm, null_space
from scipy.optimize import linprog

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(ROOT / "tracks/circuit_atlas")]

from actual_grouped import evaluate, summarize  # noqa: E402
from row54_direct_actual_search import DirectActual, read_points  # noqa: E402
from row54_full_minimax import BASE, LONG_RAIL, SHORT_RAIL, guards  # noqa: E402
from row54_joint_actual_search import write_csv  # noqa: E402
import row54_four_residual_search as core  # noqa: E402


SOURCE = HERE / "row54_round8_topology_event_pre.csv"
OUT = HERE / "row54_round8_pre_planar_bypass.json"
OLD_QUAD = (7, 8, 245, 246)
NEW_QUAD = (9, 198, 263, 264)
TARGET_KEYS = (
    ("U-", 54),
    ("H-", (6, 7)),
    ("S-", (7, 8, 245)),
    ("H-", (198, 263)),
)
OLD_WALL_KEYS = (("U-", 263), ("U-", 1))
LEDGER_KEYS = TARGET_KEYS + OLD_WALL_KEYS


def label_key(label):
    kind, item = label
    return kind, tuple(sorted(item)) if isinstance(item, list) else item


def main() -> None:
    ids, source = read_points(SOURCE)
    ix = {i: k for k, i in enumerate(ids)}
    direct = DirectActual(ids, source)
    n_direct = len(direct.controls)
    n = n_direct + 8
    origin = source.mean(axis=0)
    scale0 = float(np.sqrt(np.mean(np.sum((source - origin) ** 2, axis=1))))
    _, faces, _ = core.group_maximal_faces(ids, source)
    source_keys = {frozenset(f) for f in faces}

    def construct(z):
        q = direct.construct(z[:n_direct])
        qn = (q - origin) / scale0
        theta = z[n_direct:]
        den = 1.0 + qn @ theta[:3]
        if np.min(den) <= 0.08:
            return None
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

    def new_pre_guard(points):
        return float(-oriented(points, NEW_QUAD) / rms(points) ** 3)

    def fixed(z):
        points = construct(z)
        if points is None:
            return None
        try:
            g, labels = guards(core.mechanics(ids, points, faces), faces)
        except Exception:
            return None
        return g, labels, points

    zero = np.zeros(n)
    base = fixed(zero)
    if base is None:
        raise RuntimeError("invalid identity source")
    g0, labels, _ = base
    lookup = {label_key(label): k for k, label in enumerate(labels)}
    ledger_indices = np.asarray([lookup[k] for k in LEDGER_KEYS], int)
    target_indices = np.asarray([lookup[k] for k in TARGET_KEYS], int)
    wall_indices = np.asarray([lookup[k] for k in OLD_WALL_KEYS], int)

    eps = 2e-6
    jac = np.empty((len(g0), n))
    old_grad = np.empty(n)
    new_grad = np.empty(n)
    for j in range(n):
        dz = np.zeros(n)
        dz[j] = eps
        plus, minus = fixed(dz), fixed(-dz)
        if plus is None or minus is None:
            raise RuntimeError(f"finite difference failed for coordinate {j}")
        jac[:, j] = (plus[0] - minus[0]) / (2 * eps)
        old_grad[j] = (old_guard(plus[2]) - old_guard(minus[2])) / (2 * eps)
        new_grad[j] = (new_pre_guard(plus[2]) - new_pre_guard(minus[2])) / (2 * eps)

    # First plane axis: preserve the complete six-row ledger and the older
    # {7,8,245,246} topology guard to first order, while moving inward from
    # the new wall as efficiently as possible.
    constraint = np.vstack([jac[ledger_indices], old_grad])
    ns = null_space(constraint)
    transverse = ns @ (ns.T @ new_grad)
    if float(new_grad @ transverse) < 0:
        transverse = -transverse
    transverse /= max(float(np.max(np.abs(transverse))), 1e-300)

    # Second plane axis: improve all four residual rows, remain tangent to
    # both topology walls, and do not consume either earlier U-H wall guard.
    a_ub = [np.c_[-jac[target_indices], np.ones(len(target_indices))],
            np.c_[-jac[wall_indices], np.zeros(len(wall_indices))]]
    b_ub = [np.zeros(len(target_indices)), np.zeros(len(wall_indices))]
    near = np.flatnonzero((g0 > 0) & (g0 < 5e-5))
    if len(near):
        # Keep every already-correct nearby mechanics sign nondecreasing at
        # first order.  This is stronger than just freezing the two identities.
        a_ub.append(np.c_[-jac[near], np.zeros(len(near))])
        b_ub.append(np.zeros(len(near)))
    lp = linprog(
        np.r_[np.zeros(n), -1.0],
        A_ub=np.vstack(a_ub), b_ub=np.concatenate(b_ub),
        A_eq=np.c_[np.vstack([old_grad, new_grad]), np.zeros((2, 1))],
        b_eq=np.zeros(2),
        bounds=[(-1.0, 1.0)] * n + [(None, None)], method="highs",
    )
    if not lp.success:
        raise RuntimeError(lp.message)
    tangent = lp.x[:-1]
    tangent /= max(float(np.max(np.abs(tangent))), 1e-300)

    edges_source = None

    def audit(z, name):
        nonlocal edges_source
        packet = fixed(z)
        if packet is None:
            return {"name": name, "valid": False, "error": "fixed evaluation"}
        g, audit_labels, points = packet
        actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
        if not actual.valid:
            return {"name": name, "valid": False, "error": actual.error}
        keys = {frozenset(f["cycle"]) for f in actual.faces}
        edges = set(actual.edges)
        if edges_source is None:
            edges_source = edges
        alookup = {label_key(label): k for k, label in enumerate(audit_labels)}
        x = {i: points[ix[i]] - actual.centroid for i in ids}
        rails = {}
        for rail_name, path in (("short", SHORT_RAIL), ("long", LONG_RAIL)):
            pairs = list(zip(path, path[1:]))
            rails[rail_name] = {
                "all_edges_present": all(tuple(sorted(e)) in edges for e in pairs),
                "directed_support_min": min(
                    float(np.dot(x[a], x[b] - x[a])) for a, b in pairs
                ),
                "positive_dot_min": min(
                    float(np.dot(x[a], x[b])) for a, b in pairs
                ),
            }
        return {
            "name": name,
            "valid": True,
            "parameters": np.asarray(z).tolist(),
            "fresh_actual": summarize(actual),
            "same_open_face_cell": keys == source_keys,
            "same_true_edge_lattice": edges == edges_source,
            "base_face_present": BASE in keys,
            "U8_present": 8 in [i for i, _ in actual.unstable],
            "rails": rails,
            "hard_margin": float(np.min(g)),
            "ledger": {str(k): float(g[alookup[k]]) for k in LEDGER_KEYS},
            "old_quad_far_guard": old_guard(points),
            "new_quad_pre_guard": new_pre_guard(points),
        }

    source_audit = audit(zero, "source")
    source_hard = source_audit["hard_margin"]
    source_new = source_audit["new_quad_pre_guard"]

    # Find an inward buffer that materially separates the new determinant
    # from zero without altering the open face lattice or the class.
    buffer_scan = []
    chosen_buffer = None
    for amp in np.geomspace(1e-9, 2e-2, 180):
        z = float(amp) * transverse
        rec = audit(z, f"buffer_{amp:.3e}")
        buffer_scan.append({
            "amplitude": float(amp),
            "valid": rec.get("valid", False),
            "f_vector": rec.get("fresh_actual", {}).get("f_vector"),
            "class": rec.get("fresh_actual", {}).get("class"),
            "topology_margin": rec.get("fresh_actual", {}).get("topology_margin"),
            "new_quad_pre_guard": rec.get("new_quad_pre_guard"),
            "hard_margin": rec.get("hard_margin"),
        })
        if (rec.get("valid") and rec["same_open_face_cell"]
                and rec["fresh_actual"]["class"] == [2, 2, 2]
                and rec["base_face_present"] and rec["U8_present"]
                and all(v["all_edges_present"] for v in rec["rails"].values())
                and rec["old_quad_far_guard"] > 5e-12
                and rec["new_quad_pre_guard"] > max(2e-10, 50 * source_new)
                and min(rec["ledger"][str(k)] for k in OLD_WALL_KEYS) > 0):
            chosen_buffer = (float(amp), z, rec)
            break
    if chosen_buffer is None:
        raise RuntimeError("no valid inward buffer found")
    buffer_amp, z_buffer, buffer_audit = chosen_buffer

    # Continue along the tangent axis from the buffered point, choosing the
    # strongest fresh-hull accepted improvement before any independent event.
    tangent_scan = []
    chosen_tangent = None
    for amp in np.geomspace(1e-9, 2e-2, 220):
        z = z_buffer + float(amp) * tangent
        rec = audit(z, f"tangent_{amp:.3e}")
        tangent_scan.append({
            "amplitude": float(amp),
            "valid": rec.get("valid", False),
            "same_open_face_cell": rec.get("same_open_face_cell"),
            "class": rec.get("fresh_actual", {}).get("class"),
            "topology_margin": rec.get("fresh_actual", {}).get("topology_margin"),
            "hard_margin": rec.get("hard_margin"),
            "new_quad_pre_guard": rec.get("new_quad_pre_guard"),
        })
        if not (rec.get("valid") and rec["same_open_face_cell"]
                and rec["fresh_actual"]["class"] == [2, 2, 2]
                and rec["base_face_present"] and rec["U8_present"]
                and all(v["all_edges_present"] for v in rec["rails"].values())
                and rec["old_quad_far_guard"] > 5e-12
                and rec["new_quad_pre_guard"] > 1e-10
                and min(rec["ledger"][str(k)] for k in OLD_WALL_KEYS) > 0):
            break
        if rec["hard_margin"] > source_hard + 1e-10:
            chosen_tangent = (float(amp), z, rec)
    if chosen_tangent is None:
        raise RuntimeError("no accepted tangent descent found")
    tangent_amp, z_next, next_audit = chosen_tangent

    # Four quadrants around the buffered node.  Keep the radius well below
    # both axis lengths so every quadrant lies in the same certified open cell.
    radius = min(buffer_amp / 5.0, tangent_amp / 5.0)
    quadrants = {}
    quadrant_parameters = {}
    for s, t in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
        name = f"q_{s:+d}_{t:+d}".replace("+", "p").replace("-", "m")
        z = z_buffer + radius * (s * transverse + t * tangent)
        quadrants[name] = audit(z, name)
        quadrant_parameters[name] = z

    # Fresh L path: source -> inward buffer -> tangent continuation.
    path_records = []
    for segment, za, zb in (("inward", zero, z_buffer),
                            ("tangent", z_buffer, z_next)):
        for k, t in enumerate(np.linspace(0.0, 1.0, 51)):
            if segment == "tangent" and k == 0:
                continue
            z = (1.0 - t) * za + t * zb
            rec = audit(z, f"{segment}_{k:02d}")
            path_records.append({
                "segment": segment,
                "sample": k,
                "t": float(t),
                "parameters": z.tolist(),
                "valid": rec.get("valid", False),
                "same_open_face_cell": rec.get("same_open_face_cell"),
                "f_vector": rec.get("fresh_actual", {}).get("f_vector"),
                "class": rec.get("fresh_actual", {}).get("class"),
                "topology_margin": rec.get("fresh_actual", {}).get("topology_margin"),
                "hard_margin": rec.get("hard_margin"),
                "old_quad_far_guard": rec.get("old_quad_far_guard"),
                "new_quad_pre_guard": rec.get("new_quad_pre_guard"),
                "base_face_present": rec.get("base_face_present"),
                "U8_present": rec.get("U8_present"),
                "rail_edges": {
                    k: v["all_edges_present"] for k, v in rec.get("rails", {}).items()
                },
                "old_wall_min": min(
                    (rec.get("ledger", {}).get(str(q), float("-inf"))
                     for q in OLD_WALL_KEYS), default=float("-inf")
                ),
            })

    node_data = {
        "pre": (zero, source_audit),
        "buffer": (z_buffer, buffer_audit),
        "next": (z_next, next_audit),
    }
    for name, (z, rec) in node_data.items():
        points = construct(z)
        write_csv(OUT.with_name(OUT.stem + f"_{name}.csv"), ids, points)
        actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
        OUT.with_name(OUT.stem + f"_{name}_faces.json").write_text(
            json.dumps([f["cycle"] for f in actual.faces], indent=2) + "\n"
        )
    for name, z in quadrant_parameters.items():
        points = construct(z)
        write_csv(OUT.with_name(OUT.stem + f"_{name}.csv"), ids, points)

    all_path_ok = all(
        r["valid"] and r["same_open_face_cell"]
        and r["f_vector"] == [61, 162, 103]
        and r["class"] == [2, 2, 2]
        and r["base_face_present"] and r["U8_present"]
        and all(r["rail_edges"].values())
        and r["old_wall_min"] > 0
        and r["old_quad_far_guard"] > 0
        and r["new_quad_pre_guard"] > 0
        for r in path_records
    )
    out = {
        "version": 1,
        "method": "27D two-axis pre-cell planar detour with fresh grouped L path",
        "scope": {
            "claim": "rail-contract-preserving pre-cell continuation",
            "not_claimed": "crossing det(9,198,263,264)=0 while retaining edge 263-264",
        },
        "source": str(SOURCE),
        "old_quad": list(OLD_QUAD),
        "new_quad": list(NEW_QUAD),
        "finite_difference_epsilon": eps,
        "ledger_keys": [[k, list(v) if isinstance(v, tuple) else v]
                        for k, v in LEDGER_KEYS],
        "constraint_rank": int(np.linalg.matrix_rank(constraint)),
        "nullspace_dimension": int(ns.shape[1]),
        "constraint_singular_values": np.linalg.svd(constraint, compute_uv=False).tolist(),
        "transverse_direction": transverse.tolist(),
        "transverse_new_wall_derivative": float(new_grad @ transverse),
        "transverse_ledger_derivatives": (jac[ledger_indices] @ transverse).tolist(),
        "transverse_old_quad_derivative": float(old_grad @ transverse),
        "tangent_direction": tangent.tolist(),
        "tangent_lp_predicted_common_improvement": float(lp.x[-1]),
        "tangent_old_quad_derivative": float(old_grad @ tangent),
        "tangent_new_quad_derivative": float(new_grad @ tangent),
        "buffer_amplitude": buffer_amp,
        "tangent_amplitude": tangent_amp,
        "quadrant_radius": radius,
        "nodes": {name: rec for name, (_, rec) in node_data.items()},
        "quadrants": quadrants,
        "all_quadrants_same_open_class222": all(
            r.get("valid") and r.get("same_open_face_cell")
            and r.get("fresh_actual", {}).get("class") == [2, 2, 2]
            for r in quadrants.values()
        ),
        "L_path_samples": path_records,
        "L_path_all_open_class222_with_contract": all_path_ok,
        "L_path_minimum_topology_margin": min(r["topology_margin"] for r in path_records),
        "L_path_minimum_new_quad_pre_guard": min(r["new_quad_pre_guard"] for r in path_records),
        "L_path_minimum_old_quad_far_guard": min(r["old_quad_far_guard"] for r in path_records),
        "L_path_minimum_old_wall_guard": min(r["old_wall_min"] for r in path_records),
        "hard_improvement": next_audit["hard_margin"] - source_hard,
        "buffer_scan": buffer_scan,
        "tangent_scan": tangent_scan,
    }
    OUT.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({
        "constraint_rank": out["constraint_rank"],
        "nullspace_dimension": out["nullspace_dimension"],
        "buffer_amplitude": buffer_amp,
        "tangent_amplitude": tangent_amp,
        "source_hard": source_hard,
        "next_hard": next_audit["hard_margin"],
        "hard_improvement": out["hard_improvement"],
        "source_new_guard": source_new,
        "buffer_new_guard": buffer_audit["new_quad_pre_guard"],
        "next_new_guard": next_audit["new_quad_pre_guard"],
        "all_quadrants": out["all_quadrants_same_open_class222"],
        "L_path_ok": all_path_ok,
        "L_path_min_topology": out["L_path_minimum_topology_margin"],
    }, indent=2))


if __name__ == "__main__":
    main()
