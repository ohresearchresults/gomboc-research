#!/usr/bin/env python3
"""Locate and fresh-audit the first mechanics-class event in round 2."""
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


PRE = HERE / "row54_combined_hard_slp_round2_event_event_pre.csv"
POST = HERE / "row54_combined_hard_slp_round2_event_event_post.csv"
SOURCE = HERE / "row54_combined_hard_slp_best.csv"
EVENT = HERE / "row54_combined_hard_slp_round2_event.json"
OUT = HERE / "row54_round2_mechanical_event.json"


def main() -> None:
    ids, source = read_points(SOURCE)
    direct = DirectActual(ids, source)
    event = json.loads(EVENT.read_text())["class_event"]
    pre_z = np.asarray(event["pre_parameters"], float)
    post_z = np.asarray(event["post_parameters"], float)

    def construct(z: np.ndarray) -> np.ndarray:
        q = direct.construct(z[:len(direct.controls)])
        points, den = core.transform(q, z[len(direct.controls):])
        if points is None or float(np.min(den)) <= 0.08:
            raise RuntimeError("invalid projective chart")
        return points

    pre = construct(pre_z)
    post = construct(post_z)
    pre_actual = evaluate(dict(zip(ids, pre)), coplanar_rel=1e-11)
    if not pre_actual.valid:
        raise RuntimeError(pre_actual.error)
    face_keys = {frozenset(f["cycle"]) for f in pre_actual.faces}

    def packet(t: float):
        # The chart path is essential here: straight interpolation of the
        # already transformed coordinates collapses an unrelated ultra-shallow
        # dihedral cone, although both endpoints are valid.
        z = (1.0 - t) * pre_z + t * post_z
        points = construct(z)
        actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11,
                          strict_tol=1e-12)
        if not actual.valid:
            raise RuntimeError(actual.error)
        return points, actual

    def vertex(t: float) -> float:
        return packet(t)[1].vertex_decisions[263]

    def saddle(t: float) -> float:
        return packet(t)[1].edge_decisions[(10, 263)]

    roots = {
        "U263": float(brentq(vertex, 0.0, 1.0, xtol=5e-15,
                             rtol=4 * np.finfo(float).eps)),
        "H10_263": float(brentq(saddle, 0.0, 1.0, xtol=5e-15,
                                rtol=4 * np.finfo(float).eps)),
    }
    t_event = 0.5 * (roots["U263"] + roots["H10_263"])

    audits = {}
    root_points = None
    root_actual = None
    open_delta = 1e-5
    for name, t in (
        ("pre_open", max(0.0, t_event - open_delta)),
        ("wall", t_event),
        ("post_open", min(1.0, t_event + open_delta)),
    ):
        points, actual = packet(t)
        faces = [f["cycle"] for f in actual.faces]
        g, labels = guards(core.mechanics(ids, points, faces), faces)
        edges = set(actual.edges)
        keys = {frozenset(f["cycle"]) for f in actual.faces}
        order = np.argsort(g)[:12]
        audits[name] = {
            "t": float(t),
            "fresh_actual": summarize(actual),
            "faces_match_pre": keys == face_keys,
            "base_face_present": BASE in keys,
            "rail_edges_present": {
                rail_name: all(tuple(sorted(e)) in edges
                               for e in zip(path, path[1:]))
                for rail_name, path in (("short", SHORT_RAIL),
                                        ("long", LONG_RAIL))
            },
            "U263_decision": float(actual.vertex_decisions[263]),
            "H10_263_decision": float(actual.edge_decisions[(10, 263)]),
            "worst_guards": [
                {"value": float(g[k]), "feature": labels[k]}
                for k in order
            ],
        }
        if name == "wall":
            root_points, root_actual = points, actual

    assert root_points is not None and root_actual is not None
    local = {i: k for k, i in enumerate(ids)}
    xa = root_points[local[10]] - root_actual.centroid
    xb = root_points[local[263]] - root_actual.centroid
    direction = xb - xa
    dd = float(np.dot(direction, direction))
    endpoint_parameter = 1.0 + float(np.dot(xa, direction)) / dd
    vertex_component = float(
        np.dot(xb, direction)
        / (np.linalg.norm(xb) * np.linalg.norm(direction))
    )
    endpoint_scale = float(np.linalg.norm(xb) / np.linalg.norm(direction))
    out = {
        "version": 1,
        "method": "27D chart-segment brent roots with fresh grouped hull",
        "pre": str(PRE),
        "post": str(POST),
        "roots": roots,
        "root_separation": roots["H10_263"] - roots["U263"],
        "event_t": t_event,
        "open_sample_delta": open_delta,
        "interpretation": (
            "shared endpoint event: U263 and H(10,263) are born together"
        ),
        "endpoint_identity": {
            "vertex_component_on_neighbor_10": vertex_component,
            "edge_endpoint_component_1_minus_tau": endpoint_parameter,
            "norm_ratio": endpoint_scale,
            "identity_residual": endpoint_parameter
            - endpoint_scale * vertex_component,
            "explanation": (
                "1-tau = (||X263||/||X263-X10||) * U263(edge 10)"
            ),
        },
        "audits": audits,
    }
    write_csv(OUT.with_name(OUT.stem + "_wall.csv"), ids, root_points)
    OUT.with_name(OUT.stem + "_wall_faces.json").write_text(
        json.dumps([f["cycle"] for f in root_actual.faces], indent=2) + "\n"
    )
    OUT.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
