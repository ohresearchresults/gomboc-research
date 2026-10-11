#!/usr/bin/env python3
"""Locate and fresh-audit the first class event of constrained round 3."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(ROOT / "tracks/circuit_atlas")]

from actual_grouped import evaluate, summarize  # noqa: E402
from row54_direct_actual_search import DirectActual, read_points  # noqa: E402
from row54_full_minimax import BASE, LONG_RAIL, SHORT_RAIL, guards  # noqa: E402
from row54_joint_actual_search import write_csv  # noqa: E402
import row54_four_residual_search as core  # noqa: E402


SOURCE = HERE / "row54_round2_null_bypass_C_buffered_post.csv"
ROUND3 = HERE / "row54_combined_hard_slp_round3.json"
OUT = HERE / "row54_round3_mechanical_event.json"


def label_key(label):
    kind, item = label
    return kind, tuple(sorted(item)) if isinstance(item, list) else item


def main() -> None:
    ids, source = read_points(SOURCE)
    direct = DirectActual(ids, source)
    n_direct = len(direct.controls)
    event = json.loads(ROUND3.read_text())["class_event"]
    pre_z = np.asarray(event["pre_parameters"], float)
    post_z = np.asarray(event["post_parameters"], float)

    def construct(z):
        q = direct.construct(z[:n_direct])
        points, den = core.transform(q, z[n_direct:])
        if points is None or float(np.min(den)) <= 0.08:
            raise RuntimeError("invalid projective chart")
        return points, den

    pre_points, _ = construct(pre_z)
    pre_actual = evaluate(dict(zip(ids, pre_points)), coplanar_rel=1e-11)
    if not pre_actual.valid:
        raise RuntimeError(pre_actual.error)
    face_keys = {frozenset(f["cycle"]) for f in pre_actual.faces}
    face_cycles = [f["cycle"] for f in pre_actual.faces]
    local = {i: k for k, i in enumerate(ids)}

    def centroid_longdouble(points):
        p = np.asarray(points, dtype=np.longdouble)
        origin = np.mean(p, axis=0)
        d6 = np.longdouble(0)
        moment24 = np.zeros(3, dtype=np.longdouble)
        for cycle in face_cycles:
            c = [local[i] for i in cycle]
            a = p[c[0]] - origin
            for j in range(1, len(c) - 1):
                b = p[c[j]] - origin
                z = p[c[j + 1]] - origin
                det = np.dot(a, np.cross(b, z))
                d6 += det
                moment24 += det * (a + b + z)
        return origin + moment24 / (4 * d6)

    def packet(t):
        z = (1.0 - t) * pre_z + t * post_z
        points, den = construct(z)
        actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11,
                          strict_tol=1e-12)
        if not actual.valid:
            raise RuntimeError(actual.error)
        return z, points, den, actual

    def vertex(t):
        return packet(t)[3].vertex_decisions[1]

    def saddle(t):
        return packet(t)[3].edge_decisions[(1, 54)]

    def endpoint_numerator(t):
        _, points, _, _ = packet(t)
        p = np.asarray(points, dtype=np.longdouble)
        centroid = centroid_longdouble(p)
        x1 = p[local[1]] - centroid
        x54 = p[local[54]] - centroid
        return -float(np.dot(x1, x54 - x1))

    roots = {
        "U1": float(brentq(vertex, 0.0, 1.0, xtol=5e-15,
                           rtol=4 * np.finfo(float).eps)),
        "H1_54": float(brentq(saddle, 0.0, 1.0, xtol=5e-15,
                              rtol=4 * np.finfo(float).eps)),
        "shared_endpoint_numerator": float(
            brentq(endpoint_numerator, 0.0, 1.0, xtol=5e-15,
                   rtol=4 * np.finfo(float).eps)
        ),
    }
    event_t = roots["shared_endpoint_numerator"]
    open_delta = 1e-4
    audits = {}
    wall_points = None
    wall_actual = None
    for name, t in (
        ("pre_open", max(0.0, event_t - open_delta)),
        ("wall", event_t),
        ("post_open", min(1.0, event_t + open_delta)),
    ):
        z, points, den, actual = packet(t)
        faces = [f["cycle"] for f in actual.faces]
        g, labels = guards(core.mechanics(ids, points, faces), faces)
        lookup = {label_key(label): k for k, label in enumerate(labels)}
        keys = {frozenset(f["cycle"]) for f in actual.faces}
        edges = set(actual.edges)
        order = np.argsort(g)[:14]
        audits[name] = {
            "t": float(t),
            "parameters": z.tolist(),
            "fresh_actual": summarize(actual),
            "faces_match_pre": keys == face_keys,
            "base_face_present": BASE in keys,
            "rail_edges_present": {
                rail_name: all(tuple(sorted(e)) in edges
                               for e in zip(path, path[1:]))
                for rail_name, path in (("short", SHORT_RAIL),
                                        ("long", LONG_RAIL))
            },
            "minimum_projective_denominator": float(np.min(den)),
            "U1_decision": float(actual.vertex_decisions[1]),
            "H1_54_decision": float(actual.edge_decisions[(1, 54)]),
            "protected_U263_guard": float(g[lookup[("U-", 263)]]),
            "protected_H10_263_guard": float(
                g[lookup[("H-", (10, 263))]]
            ),
            "worst_guards": [
                {"value": float(g[k]), "feature": labels[k]}
                for k in order
            ],
        }
        if name == "wall":
            wall_points, wall_actual = points, actual

    assert wall_points is not None and wall_actual is not None
    p_long = np.asarray(wall_points, dtype=np.longdouble)
    centroid_long = centroid_longdouble(p_long)
    x1 = p_long[local[1]] - centroid_long
    x54 = p_long[local[54]] - centroid_long
    direction = x54 - x1
    dd = float(np.dot(direction, direction))
    shared_numerator = -float(np.dot(x1, direction))
    tau = shared_numerator / dd
    vertex_component = float(-float(np.dot(x1, direction)) / (
        np.linalg.norm(x1) * np.linalg.norm(direction)
    ))
    endpoint_scale = float(np.linalg.norm(x1) / np.linalg.norm(direction))

    out = {
        "version": 1,
        "method": "27D chart-segment brent roots with fresh grouped hull",
        "source": str(SOURCE),
        "round3": str(ROUND3),
        "roots": roots,
        "normalized_root_separation": roots["H1_54"] - roots["U1"],
        "event_t": event_t,
        "open_sample_delta": open_delta,
        "interpretation": "shared endpoint event: U1 and H(1,54) are born together",
        "endpoint_identity": {
            "longdouble_shared_numerator": shared_numerator,
            "vertex_component_on_neighbor_54": vertex_component,
            "edge_endpoint_component_tau": tau,
            "norm_ratio": endpoint_scale,
            "identity_residual": float(tau - endpoint_scale * vertex_component),
            "explanation": "tau = (||X1||/||X54-X1||) * U1(edge 54)",
        },
        "audits": audits,
    }
    write_csv(OUT.with_name(OUT.stem + "_wall.csv"), ids, wall_points)
    OUT.with_name(OUT.stem + "_wall_faces.json").write_text(
        json.dumps([f["cycle"] for f in wall_actual.faces], indent=2) + "\n"
    )
    OUT.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({
        "roots": roots,
        "normalized_root_separation": out["normalized_root_separation"],
        "identity": out["endpoint_identity"],
        "classes": {k: v["fresh_actual"]["class"]
                    for k, v in audits.items()},
        "topology_margins": {k: v["fresh_actual"]["topology_margin"]
                             for k, v in audits.items()},
        "protected": {k: [v["protected_U263_guard"],
                           v["protected_H10_263_guard"]]
                      for k, v in audits.items()},
    }, indent=2))


if __name__ == "__main__":
    main()
