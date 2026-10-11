#!/usr/bin/env python3
"""Multidimensional guard buffer inside the strict round-10 far cell.

The five directed guards are the three accumulated topology signs and the two
shared U-H endpoint numerators.  Five independent axes are constructed inside
the nullspace of the four residual target rows.  A fresh-hull piecewise-linear
path and all 32 corners of a local five-cube certify that the buffer is an open
actual-cell neighborhood rather than a single fortuitous scalar direction.
"""
from __future__ import annotations

import argparse
import itertools
import json
import sys
from pathlib import Path

import numpy as np
from scipy.linalg import expm, null_space

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(ROOT / "tracks/circuit_atlas")]

from actual_grouped import evaluate, summarize  # noqa: E402
from row54_direct_actual_search import DirectActual, read_points  # noqa: E402
from row54_full_minimax import BASE, LONG_RAIL, SHORT_RAIL, guards  # noqa: E402
from row54_joint_actual_search import write_csv  # noqa: E402
import row54_four_residual_search as core  # noqa: E402


SOURCE = HERE / "row54_round10_topology_event_far.csv"
OUT = HERE / "row54_round10_far_multiguard_buffer.json"
TOPOLOGY_QUADS = (
    ("round4_far", (7, 8, 245, 246), -1.0),
    ("round8_pre", (9, 198, 263, 264), -1.0),
    ("round10_far", (8, 264, 246, 198), 1.0),
)
ROUND12_QUAD = ("round12_far", (198, 263, 262, 11), 1.0)
TARGET_KEYS = (
    ("U-", 54), ("H-", (6, 7)),
    ("S-", (7, 8, 245)), ("H-", (198, 263)),
)
MECHANICS_KEYS = (("U-", 263), ("H-", (10, 263)),
                   ("U-", 1), ("H-", (1, 54)))
ALT_ROUTE = (228, 198, 263, 9, 8)


def label_key(label):
    kind, item = label
    return kind, tuple(sorted(item)) if isinstance(item, list) else item


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, default=SOURCE)
    ap.add_argument("--output", type=Path, default=OUT)
    ap.add_argument("--include-round12", action="store_true")
    ap.add_argument("--allow-long-rail-loss", action="store_true")
    args = ap.parse_args()
    topology_quads = (TOPOLOGY_QUADS + (ROUND12_QUAD,)
                      if args.include_round12 else TOPOLOGY_QUADS)
    ids, source = read_points(args.source)
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
        if np.min(den) <= 0.08:
            return None
        a, b, c, d, e = theta[3:]
        h = np.array([[a, b, c], [b, d, e],
                      [c, e, -a - d]], dtype=float)
        return origin + scale0 * ((qn / den[:, None]) @ expm(h).T)

    def centroid_longdouble(points):
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

    def topology_guards(points):
        p = np.asarray(points, dtype=np.longdouble)
        centered = p - np.mean(p, axis=0)
        scale = np.sqrt(np.mean(np.sum(centered * centered, axis=1)))
        result = []
        for _, quad, sign in topology_quads:
            q = [p[ix[i]] for i in quad]
            det = np.dot(q[1] - q[0], np.cross(q[2] - q[0], q[3] - q[0]))
            result.append(np.longdouble(sign) * det / scale**3)
        return np.asarray(result, dtype=np.longdouble)

    def endpoint_guards(points):
        p = np.asarray(points, dtype=np.longdouble)
        c = centroid_longdouble(p)
        x10, x263 = p[ix[10]] - c, p[ix[263]] - c
        x1, x54 = p[ix[1]] - c, p[ix[54]] - c
        # Positive on the excluded side of each exact shared U-H numerator.
        return np.asarray([
            -np.dot(x263, x263 - x10),
            np.dot(x1, x54 - x1),
        ], dtype=np.longdouble)

    def directed_guards(points):
        return np.r_[topology_guards(points), endpoint_guards(points)]

    def fixed(z):
        points = construct(z)
        if points is None:
            return None
        try:
            g, labels = guards(core.mechanics(ids, points, faces), faces)
        except Exception:
            return None
        return g, labels, points, np.asarray(directed_guards(points), float)

    zero = np.zeros(nvar)
    base = fixed(zero)
    if base is None:
        raise RuntimeError("invalid source")
    g0, labels, _, d0 = base
    lookup = {label_key(label): k for k, label in enumerate(labels)}
    target_indices = np.asarray([lookup[k] for k in TARGET_KEYS])
    eps = 2e-6
    jac = np.empty((len(g0), nvar))
    n_directed = len(topology_quads) + 2
    directed_jac = np.empty((n_directed, nvar))
    for j in range(nvar):
        dz = np.zeros(nvar)
        dz[j] = eps
        plus, minus = fixed(dz), fixed(-dz)
        if plus is None or minus is None:
            raise RuntimeError(f"finite difference failed at {j}")
        jac[:, j] = (plus[0] - minus[0]) / (2 * eps)
        directed_jac[:, j] = (plus[3] - minus[3]) / (2 * eps)

    residual_constraint = jac[target_indices]
    ns = null_space(residual_constraint)
    response = directed_jac @ ns
    response_rank = int(np.linalg.matrix_rank(response))
    if response_rank != n_directed:
        raise RuntimeError(
            f"directed guard response rank {response_rank}, expected {n_directed}"
        )
    # Columns change exactly one directed guard to first order while leaving
    # every residual target row unchanged.  This is the independent-control
    # certificate for the accumulated guards.
    axes = ns @ np.linalg.pinv(response)
    linear_response = directed_jac @ axes

    guard_names = [z[0] for z in topology_quads] + ["U263_H10_263", "U1_H1_54"]
    requested_floors = np.asarray(
        ([5e-11, 5e-10, 5e-10, 5e-10] if args.include_round12
         else [5e-11, 5e-10, 5e-10]) + [5e-9, 5e-9]
    )
    requested_delta = np.maximum(requested_floors - d0, requested_floors * 0.2)
    predicted = axes @ requested_delta

    def graph_record(points, actual):
        x = {i: points[ix[i]] - actual.centroid for i in ids}
        edges = set(actual.edges)
        edge = (8, 198)
        a, b = edge
        new_edge = {
            "present": edge in edges,
            "positive_dot": float(np.dot(x[a], x[b])),
            "directed_198_to_8": float(np.dot(x[198], x[8] - x[198])),
            "directed_8_to_198": float(np.dot(x[8], x[198] - x[8])),
        }
        pairs = list(zip(ALT_ROUTE, ALT_ROUTE[1:]))
        return {
            "new_diagonal_8_198": new_edge,
            "alternate_route": {
                "path": list(ALT_ROUTE),
                "all_edges_present": all(tuple(sorted(e)) in edges for e in pairs),
                "positive_dot_min": min(float(np.dot(x[u], x[v])) for u, v in pairs),
                "directed_support_min": min(
                    float(np.dot(x[u], x[v] - x[u])) for u, v in pairs
                ),
            },
        }

    def audit(z, name):
        packet = fixed(z)
        if packet is None:
            return {"name": name, "valid": False, "error": "fixed evaluation"}
        g, audit_labels, points, directed = packet
        actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
        if not actual.valid:
            return {"name": name, "valid": False, "error": actual.error}
        keys = {frozenset(f["cycle"]) for f in actual.faces}
        edges = set(actual.edges)
        alookup = {label_key(label): k for k, label in enumerate(audit_labels)}
        rails = {
            rail_name: all(tuple(sorted(e)) in edges for e in zip(path, path[1:]))
            for rail_name, path in (("short", SHORT_RAIL), ("long", LONG_RAIL))
        }
        return {
            "name": name,
            "valid": True,
            "parameters": np.asarray(z).tolist(),
            "fresh_actual": summarize(actual),
            "same_open_face_cell": keys == source_keys,
            "base_face_present": BASE in keys,
            "U8_present": 8 in [i for i, _ in actual.unstable],
            "literal_rails": rails,
            "hard_margin": float(np.min(g)),
            "target_ledger": {str(k): float(g[alookup[k]]) for k in TARGET_KEYS},
            "old_mechanics_ledger": {
                str(k): float(g[alookup[k]]) for k in MECHANICS_KEYS
            },
            "directed_guard_ledger": {
                k: float(v) for k, v in zip(guard_names, directed)
            },
            "graph": graph_record(points, actual),
        }

    source_audit = audit(zero, "source")
    scan = []
    chosen = None
    for alpha in np.geomspace(1e-3, 8.0, 220):
        z = float(alpha) * predicted
        rec = audit(z, f"combined_{alpha:.3e}")
        vals = np.asarray(list(rec.get("directed_guard_ledger", {}).values()))
        scan.append({
            "alpha": float(alpha),
            "valid": rec.get("valid", False),
            "same_open_face_cell": rec.get("same_open_face_cell"),
            "f_vector": rec.get("fresh_actual", {}).get("f_vector"),
            "class": rec.get("fresh_actual", {}).get("class"),
            "topology_margin": rec.get("fresh_actual", {}).get("topology_margin"),
            "hard_margin": rec.get("hard_margin"),
            "directed_guards": vals.tolist(),
        })
        if (rec.get("valid") and rec["same_open_face_cell"]
                and rec["fresh_actual"]["class"] == [2, 2, 2]
                and rec["base_face_present"] and rec["U8_present"]
                and rec["literal_rails"]["short"]
                and (args.allow_long_rail_loss
                     or rec["literal_rails"]["long"])
                and rec["graph"]["alternate_route"]["all_edges_present"]
                and rec["graph"]["alternate_route"]["positive_dot_min"] > 0
                and len(vals) == n_directed
                and np.all(vals >= requested_floors)
                and min(rec["old_mechanics_ledger"].values()) > 0):
            chosen = (float(alpha), z, rec)
            break
    if chosen is None:
        raise RuntimeError("no joint five-guard buffer reached")
    alpha, z_buffer, buffer_audit = chosen

    # Piecewise path activates the independent axes one at a time.  Scale all
    # five axis increments by the jointly accepted nonlinear alpha.
    increments = [alpha * axes[:, j] * requested_delta[j]
                  for j in range(n_directed)]
    path_records = []
    current = zero.copy()
    nodes = [("source", current.copy(), source_audit)]
    for j, inc in enumerate(increments):
        nxt = current + inc
        for k, t in enumerate(np.linspace(0.0, 1.0, 21)):
            if j > 0 and k == 0:
                continue
            z = (1.0 - t) * current + t * nxt
            rec = audit(z, f"axis{j}_{k:02d}")
            path_records.append({
                "axis": j,
                "sample": k,
                "t": float(t),
                "parameters": z.tolist(),
                "valid": rec.get("valid", False),
                "same_open_face_cell": rec.get("same_open_face_cell"),
                "f_vector": rec.get("fresh_actual", {}).get("f_vector"),
                "class": rec.get("fresh_actual", {}).get("class"),
                "topology_margin": rec.get("fresh_actual", {}).get("topology_margin"),
                "base_face_present": rec.get("base_face_present"),
                "U8_present": rec.get("U8_present"),
                "literal_rails": rec.get("literal_rails"),
                "graph": rec.get("graph"),
                "hard_margin": rec.get("hard_margin"),
                "directed_guard_ledger": rec.get("directed_guard_ledger"),
                "old_mechanics_min": min(rec.get("old_mechanics_ledger", {"x": -np.inf}).values()),
            })
        current = nxt
        nodes.append((f"axis{j}_node", current.copy(), audit(current, f"axis{j}_node")))

    # A small full-dimensional cube about the buffer checks independent signs
    # in all simultaneous combinations, not merely along the construction path.
    cube_scale = 0.04
    corners = {}
    for signs in itertools.product((-1, 1), repeat=n_directed):
        z = z_buffer + cube_scale * sum(
            (s * inc for s, inc in zip(signs, increments)),
            np.zeros(nvar),
        )
        name = "c_" + "".join("p" if s > 0 else "m" for s in signs)
        corners[name] = audit(z, name)

    path_ok = all(
        r["valid"] and r["same_open_face_cell"]
        and r["f_vector"] == [61, 162, 103] and r["class"] == [2, 2, 2]
        and r["base_face_present"] and r["U8_present"]
        and r["literal_rails"]["short"]
        and (args.allow_long_rail_loss or r["literal_rails"]["long"])
        and r["graph"]["alternate_route"]["all_edges_present"]
        and r["graph"]["alternate_route"]["positive_dot_min"] > 0
        and min(r["directed_guard_ledger"].values()) > 0
        and r["old_mechanics_min"] > 0
        for r in path_records
    )
    corners_ok = all(
        r.get("valid") and r.get("same_open_face_cell")
        and r.get("fresh_actual", {}).get("class") == [2, 2, 2]
        and min(r.get("directed_guard_ledger", {"x": -np.inf}).values()) > 0
        for r in corners.values()
    )

    output = args.output
    write_csv(output.with_name(output.stem + "_source.csv"), ids, source)
    points_buffer = construct(z_buffer)
    write_csv(output.with_name(output.stem + "_buffer.csv"), ids, points_buffer)
    actual_buffer = evaluate(dict(zip(ids, points_buffer)), coplanar_rel=1e-11)
    output.with_name(output.stem + "_buffer_faces.json").write_text(
        json.dumps([f["cycle"] for f in actual_buffer.faces], indent=2) + "\n"
    )

    # The new edge row is mechanically safe and independent, but it is not an
    # acute shortcut.  Its row-gradient rank test is recorded explicitly.
    h8198 = lookup[("H-", (8, 198))]
    base_control = np.vstack([residual_constraint, directed_jac])
    base_normalized = base_control / np.maximum(
        np.linalg.norm(base_control, axis=1, keepdims=True), 1e-300
    )
    h_normalized = jac[h8198] / max(np.linalg.norm(jac[h8198]), 1e-300)
    base_null = null_space(base_normalized, rcond=1e-10)
    h_projected = base_null @ (base_null.T @ h_normalized)
    out = {
        "version": 1,
        "method": "five-axis nullspace buffer in the strict round10 far cell",
        "source_path": str(args.source),
        "round12_guard_enabled": args.include_round12,
        "literal_long_rail_required": not args.allow_long_rail_loss,
        "guard_names": guard_names,
        "source_directed_guards": d0.tolist(),
        "requested_floors": requested_floors.tolist(),
        "requested_delta": requested_delta.tolist(),
        "target_constraint_rank": int(np.linalg.matrix_rank(residual_constraint)),
        "target_nullspace_dimension": int(ns.shape[1]),
        "directed_response_rank": response_rank,
        "directed_linear_response": linear_response.tolist(),
        "axis_directions": axes.tolist(),
        "combined_predicted_parameters": predicted.tolist(),
        "accepted_alpha": alpha,
        "source": source_audit,
        "buffer": buffer_audit,
        "hard_change": buffer_audit["hard_margin"] - source_audit["hard_margin"],
        "piecewise_path": path_records,
        "piecewise_path_all_open_class222": path_ok,
        "piecewise_path_minimum_topology_margin": min(
            r["topology_margin"] for r in path_records
        ),
        "cube_scale": cube_scale,
        "cube_corners": corners,
        "all_32_cube_corners_open_class222": corners_ok,
        "new_diagonal_control": {
            "edge": [8, 198],
            "source_guard_Hminus": float(g0[h8198]),
            "jacobian_rank_without_row": int(np.linalg.matrix_rank(
                base_normalized, tol=1e-9
            )),
            "jacobian_rank_with_row": int(np.linalg.matrix_rank(
                np.vstack([base_normalized, h_normalized]), tol=1e-9
            )),
            "projected_gradient_norm": float(np.linalg.norm(h_projected)),
            "positive_dot_shortcut": False,
            "directed_shortcut": False,
        },
        "scan": scan,
    }
    output.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({
        "response_rank": response_rank,
        "nullspace_dimension": ns.shape[1],
        "source_guards": d0.tolist(),
        "buffer_guards": list(buffer_audit["directed_guard_ledger"].values()),
        "requested_floors": requested_floors.tolist(),
        "accepted_alpha": alpha,
        "source_hard": source_audit["hard_margin"],
        "buffer_hard": buffer_audit["hard_margin"],
        "path_ok": path_ok,
        "corners_ok": corners_ok,
        "min_topology": out["piecewise_path_minimum_topology_margin"],
        "new_diagonal": out["new_diagonal_control"],
        "graph": buffer_audit["graph"],
    }, indent=2))


if __name__ == "__main__":
    main()
