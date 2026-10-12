#!/usr/bin/env python3
"""Build a fresh-hull 2D nullspace bypass of the U263/H(10,263) wall."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(ROOT / "tracks/circuit_atlas")]

from actual_grouped import evaluate, summarize  # noqa: E402
from row54_direct_actual_search import DirectActual, read_points  # noqa: E402
from row54_full_minimax import BASE, LONG_RAIL, SHORT_RAIL, guards  # noqa: E402
from row54_joint_actual_search import write_csv  # noqa: E402
import row54_four_residual_search as core  # noqa: E402


SOURCE = HERE / "row54_combined_hard_slp_best.csv"
ROUND2 = HERE / "row54_combined_hard_slp_round2_event.json"
EVENT = HERE / "row54_round2_mechanical_event.json"
OUT = HERE / "row54_round2_null_bypass.json"


def label_key(label):
    kind, item = label
    if isinstance(item, list):
        item = tuple(sorted(item))
    return kind, item


def main() -> None:
    ids, source = read_points(SOURCE)
    direct = DirectActual(ids, source)
    n_direct = len(direct.controls)
    _, faces, _ = core.group_maximal_faces(ids, source)
    face_keys = {frozenset(c) for c in faces}
    event = json.loads(ROUND2.read_text())["class_event"]
    pre_z = np.asarray(event["pre_parameters"], float)
    post_z = np.asarray(event["post_parameters"], float)
    event_t = float(json.loads(EVENT.read_text())["event_t"])
    wall_z = (1.0 - event_t) * pre_z + event_t * post_z

    def construct(z):
        q = direct.construct(z[:n_direct])
        points, den = core.transform(q, z[n_direct:])
        if points is None or float(np.min(den)) <= 0.08:
            raise RuntimeError("invalid chart")
        return points, den

    def fixed(z):
        points, den = construct(z)
        mechanics = core.mechanics(ids, points, faces)
        g, labels = guards(mechanics, faces)
        return g, labels, points, den

    def audit(z):
        g, labels, points, den = fixed(z)
        actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
        keys = {frozenset(f["cycle"]) for f in actual.faces} if actual.valid else set()
        edges = set(actual.edges) if actual.valid else set()
        lookup = {label_key(label): k for k, label in enumerate(labels)}
        return {
            "parameters": np.asarray(z).tolist(),
            "hard_margin": float(np.min(g)),
            "U263_guard": float(g[lookup[("U-", 263)]]),
            "H10_263_guard": float(g[lookup[("H-", (10, 263))]]),
            "target_residuals": {
                "U54": float(g[lookup[("U-", 54)]]),
                "H67": float(g[lookup[("H-", (6, 7))]]),
                "S7_245_246": float(g[lookup[("S-", (7, 245, 246))]]),
                "H198_263": float(g[lookup[("H-", (198, 263))]]),
            },
            "minimum_projective_denominator": float(np.min(den)),
            "fresh_actual": summarize(actual),
            "faces_match_source": keys == face_keys,
            "base_face_present": BASE in keys,
            "rail_edges_present": {
                name: all(tuple(sorted(e)) in edges
                          for e in zip(path, path[1:]))
                for name, path in (("short", SHORT_RAIL),
                                   ("long", LONG_RAIL))
            },
            "points": points,
        }

    g0, labels, _, _ = fixed(wall_z)
    lookup = {label_key(label): k for k, label in enumerate(labels)}
    target_keys = [
        ("U-", 54), ("H-", (6, 7)),
        ("S-", (7, 245, 246)), ("H-", (198, 263)),
    ]
    target_indices = [lookup[key] for key in target_keys]
    wall_index = lookup[("U-", 263)]
    paired_index = lookup[("H-", (10, 263))]

    epsilon = 2e-6
    jac = np.empty((len(g0), len(wall_z)))
    for j in range(len(wall_z)):
        step = np.zeros(len(wall_z))
        step[j] = epsilon
        jac[:, j] = (fixed(wall_z + step)[0]
                     - fixed(wall_z - step)[0]) / (2 * epsilon)
    target_jac = jac[target_indices]
    _, singular_values, vt = np.linalg.svd(target_jac, full_matrices=True)
    null_basis = vt[len(target_indices):].T
    transverse = null_basis @ (null_basis.T @ jac[wall_index])
    transverse /= np.max(np.abs(transverse))
    if float(jac[wall_index] @ transverse) < 0:
        transverse = -transverse

    raw = post_z - pre_z
    tangent = raw - (float(jac[wall_index] @ raw)
                     / float(jac[wall_index] @ transverse)) * transverse
    tangent /= np.max(np.abs(tangent))

    quadrant_radius = 2e-4
    quadrants = {}
    for su in (-1, 1):
        for sv in (-1, 1):
            name = f"u{su:+d}_v{sv:+d}"
            packet = audit(wall_z + quadrant_radius
                           * (su * tangent + sv * transverse))
            packet.pop("points")
            quadrants[name] = packet

    bypass = 0.004
    node_z = {
        "A_pre": pre_z,
        "B_buffered_pre": pre_z + bypass * transverse,
        "C_buffered_post": post_z + bypass * transverse,
    }
    nodes = {}
    for name, z in node_z.items():
        packet = audit(z)
        points = packet.pop("points")
        nodes[name] = packet
        write_csv(OUT.with_name(OUT.stem + f"_{name}.csv"), ids, points)

    path = []
    for leg, a, b, count in (
        ("A_to_B", node_z["A_pre"], node_z["B_buffered_pre"], 21),
        ("B_to_C", node_z["B_buffered_pre"], node_z["C_buffered_post"], 31),
    ):
        for k, t in enumerate(np.linspace(0.0, 1.0, count)):
            if leg == "B_to_C" and k == 0:
                continue
            packet = audit((1.0 - t) * a + t * b)
            packet.pop("points")
            packet["leg"] = leg
            packet["leg_t"] = float(t)
            path.append(packet)

    endpoint_points = audit(node_z["C_buffered_post"])["points"]
    endpoint_actual = evaluate(dict(zip(ids, endpoint_points)), coplanar_rel=1e-11)
    OUT.with_name(OUT.stem + "_endpoint_faces.json").write_text(
        json.dumps([f["cycle"] for f in endpoint_actual.faces], indent=2) + "\n"
    )

    out = {
        "version": 1,
        "method": "27D target-Jacobian nullspace transverse bypass",
        "source": str(SOURCE),
        "event_t": event_t,
        "finite_difference_epsilon": epsilon,
        "target_jacobian_singular_values": singular_values.tolist(),
        "target_jacobian_rank": int(np.linalg.matrix_rank(target_jac)),
        "nullspace_dimension": int(null_basis.shape[1]),
        "transverse_direction": transverse.tolist(),
        "target_derivatives_along_transverse": (
            target_jac @ transverse
        ).tolist(),
        "U263_derivative_along_transverse": float(
            jac[wall_index] @ transverse
        ),
        "H10_263_derivative_along_transverse": float(
            jac[paired_index] @ transverse
        ),
        "tangent_direction": tangent.tolist(),
        "U263_derivative_along_tangent": float(jac[wall_index] @ tangent),
        "quadrant_radius": quadrant_radius,
        "quadrants": quadrants,
        "bypass_amplitude": bypass,
        "nodes": nodes,
        "L_path": path,
        "L_path_all_valid": all(
            p["fresh_actual"]["valid"] and p["faces_match_source"]
            and p["base_face_present"]
            and all(p["rail_edges_present"].values())
            for p in path
        ),
        "L_path_all_class222": all(
            p["fresh_actual"]["class"] == [2, 2, 2] for p in path
        ),
        "L_path_minimum_topology_margin": min(
            p["fresh_actual"]["topology_margin"] for p in path
        ),
        "L_path_minimum_U263_guard": min(p["U263_guard"] for p in path),
        "L_path_minimum_H10_263_guard": min(
            p["H10_263_guard"] for p in path
        ),
    }
    OUT.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({
        "rank": out["target_jacobian_rank"],
        "nullspace_dimension": out["nullspace_dimension"],
        "target_derivatives_along_transverse": out[
            "target_derivatives_along_transverse"
        ],
        "quadrant_classes": {
            k: v["fresh_actual"]["class"] for k, v in quadrants.items()
        },
        "L_path_all_valid": out["L_path_all_valid"],
        "L_path_all_class222": out["L_path_all_class222"],
        "L_path_minimum_topology_margin": out[
            "L_path_minimum_topology_margin"
        ],
        "L_path_minimum_U263_guard": out["L_path_minimum_U263_guard"],
        "L_path_minimum_H10_263_guard": out[
            "L_path_minimum_H10_263_guard"
        ],
        "endpoint_hard": nodes["C_buffered_post"]["hard_margin"],
    }, indent=2))


if __name__ == "__main__":
    main()
