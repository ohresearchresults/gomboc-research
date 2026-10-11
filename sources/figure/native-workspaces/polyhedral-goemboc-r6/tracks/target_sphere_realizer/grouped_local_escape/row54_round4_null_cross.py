#!/usr/bin/env python3
"""Nullspace cross of the {7,8,245,246} flip preserving both endpoint walls."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from scipy.linalg import expm

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(ROOT / "tracks/circuit_atlas")]

from actual_grouped import evaluate, summarize  # noqa: E402
from row54_direct_actual_search import DirectActual, read_points  # noqa: E402
from row54_full_minimax import BASE, LONG_RAIL, SHORT_RAIL, guards  # noqa: E402
from row54_joint_actual_search import write_csv  # noqa: E402
import row54_four_residual_search as core  # noqa: E402

SOURCE = HERE / "row54_combined_hard_slp_round4c_best.csv"
EVENT = HERE / "row54_round4_topology_event.json"
OUT = HERE / "row54_round4_null_cross.json"


def label_key(label):
    kind, item = label
    return kind, tuple(sorted(item)) if isinstance(item, list) else item


def main() -> None:
    event = json.loads(EVENT.read_text())
    direction = np.asarray(event["direction"], float)
    wall_s = float(event["oriented_volume_root"])
    far_s = float(event["first_certifiable_far_s"])
    ids, source = read_points(SOURCE)
    direct = DirectActual(ids, source)
    n_direct = len(direct.controls)
    _, faces, _ = core.group_maximal_faces(ids, source)
    origin = source.mean(axis=0)
    scale = float(np.sqrt(np.mean(np.sum((source - origin) ** 2, axis=1))))
    local = {i: k for k, i in enumerate(ids)}

    def construct(z):
        q = direct.construct(z[:n_direct])
        qn = (q - origin) / scale
        theta = z[n_direct:]
        den = 1.0 + qn @ theta[:3]
        a, b, c, d, e = theta[3:]
        h = np.array([[a, b, c], [b, d, e],
                      [c, e, -a - d]], dtype=float)
        return origin + scale * ((qn / den[:, None]) @ expm(h).T)

    def fixed(z):
        points = construct(z)
        g, labels = guards(core.mechanics(ids, points, faces), faces)
        return g, labels, points

    def quad_det(z):
        p = construct(z)
        q = [p[local[i]] for i in (7, 8, 245, 246)]
        return float(np.dot(q[1] - q[0],
                            np.cross(q[2] - q[0], q[3] - q[0])))

    zero = np.zeros(len(direction))
    g0, labels, _ = fixed(zero)
    lookup = {label_key(label): k for k, label in enumerate(labels)}
    constraint_keys = [
        ("U-", 54), ("H-", (6, 7)),
        ("S-", (7, 245, 246)), ("H-", (198, 263)),
        ("U-", 1),
    ]
    constraint_indices = [lookup[k] for k in constraint_keys]
    wall_index = lookup[("U-", 263)]
    epsilon = 2e-6
    jac = np.empty((len(g0), len(zero)))
    topo_grad = np.empty(len(zero))
    for j in range(len(zero)):
        step = np.zeros(len(zero))
        step[j] = epsilon
        jac[:, j] = (fixed(step)[0] - fixed(-step)[0]) / (2 * epsilon)
        topo_grad[j] = (quad_det(step) - quad_det(-step)) / (2 * epsilon)
    constraint_jac = np.vstack([jac[constraint_indices], topo_grad])
    _, singular_values, vt = np.linalg.svd(constraint_jac, full_matrices=True)
    null_basis = vt[len(constraint_indices) + 1:].T
    transverse = null_basis @ (null_basis.T @ jac[wall_index])
    transverse /= np.max(np.abs(transverse))
    if float(jac[wall_index] @ transverse) < 0:
        transverse = -transverse

    representatives = {
        "pre_bad": -1e-8 * transverse,
        "pre_good": 1e-5 * transverse,
        "far_bad": far_s * direction - 2e-10 * transverse,
        "far_good": far_s * direction + 1e-6 * transverse,
        "wall_buffered": wall_s * direction + 1e-6 * transverse,
        "deep_direct": 1e-6 * direction,
        # Move well inside the new diagonal cell before restarting SLP.  The
        # large transverse buffer is mechanically harmless to first order
        # and makes the fresh topology margin roughly 300 times larger.
        "deep_far": 1e-6 * direction + 1e-4 * transverse,
    }

    def audit(name, z):
        points = construct(z)
        # A tight threshold resolves the signed mechanical sectors; the
        # sampled path below separately uses the standard 1e-9 class cutoff.
        actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11,
                          strict_tol=1e-12)
        faces_actual = [f["cycle"] for f in actual.faces] if actual.valid else []
        if actual.valid:
            g, labels = guards(core.mechanics(ids, points, faces_actual),
                               faces_actual)
            lookup_actual = {label_key(label): k
                             for k, label in enumerate(labels)}
            edges = set(actual.edges)
            keys = {frozenset(f["cycle"]) for f in actual.faces}
            ledger = {
                str(k): float(g[lookup_actual[k]])
                for k in (("U-", 54), ("H-", (6, 7)),
                          ("H-", (198, 263)), ("U-", 263),
                          ("H-", (10, 263)), ("U-", 1),
                          ("H-", (1, 54))) if k in lookup_actual
            }
            hard = float(np.min(g))
            base = BASE in keys
            rails = {
                rail_name: all(tuple(sorted(e)) in edges
                               for e in zip(path, path[1:]))
                for rail_name, path in (("short", SHORT_RAIL),
                                        ("long", LONG_RAIL))
            }
        else:
            ledger, hard, base, rails = {}, None, False, {}
        return {
            "name": name,
            "parameters": np.asarray(z).tolist(),
            "fresh_actual": summarize(actual),
            "base_face_present": base,
            "rail_edges_present": rails,
            "guard_ledger": ledger,
            "hard_margin": hard,
            "quad_oriented_volume": quad_det(z),
            "points": points,
        }

    audits = {}
    for name, z in representatives.items():
        packet = audit(name, z)
        points = packet.pop("points")
        audits[name] = packet
        write_csv(OUT.with_name(OUT.stem + f"_{name}.csv"), ids, points)
        if packet["fresh_actual"]["valid"]:
            actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
            OUT.with_name(OUT.stem + f"_{name}_faces.json").write_text(
                json.dumps([f["cycle"] for f in actual.faces], indent=2) + "\n"
            )

    pre_keys = {
        frozenset(f["cycle"])
        for f in evaluate(dict(zip(ids, construct(zero))),
                          coplanar_rel=1e-11).faces
    }
    far_keys = {
        frozenset(f["cycle"])
        for f in evaluate(dict(zip(ids, construct(representatives["far_good"]))),
                          coplanar_rel=1e-11).faces
    }
    wall_keys = {
        frozenset(f["cycle"])
        for f in evaluate(dict(zip(ids, construct(representatives["wall_buffered"]))),
                          coplanar_rel=1e-11).faces
    }

    # Sample a piecewise-linear path through the grouped wall and then move
    # deeper into the new diagonal cell.  The stable cross-product Gram test
    # in actual_grouped.py makes the mandatory 1e-26 cutoff meaningful here.
    segment_scan = []
    for segment, a, b in (
        ("pre_to_buffer", zero, representatives["pre_good"]),
        ("buffered_cross", representatives["pre_good"],
         representatives["far_good"]),
        ("far_deepen", representatives["far_good"],
         representatives["deep_far"]),
    ):
        for t in np.linspace(0.0, 1.0, 41):
            z = (1.0 - t) * a + t * b
            points = construct(z)
            actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
            summary = summarize(actual)
            if actual.valid:
                keys = {frozenset(f["cycle"]) for f in actual.faces}
                edges = set(actual.edges)
                base = BASE in keys
                rails = all(
                    tuple(sorted(e)) in edges
                    for path in (SHORT_RAIL, LONG_RAIL)
                    for e in zip(path, path[1:])
                )
                g, path_labels = guards(
                    core.mechanics(ids, points,
                                   [f["cycle"] for f in actual.faces]),
                    [f["cycle"] for f in actual.faces],
                )
                path_lookup = {label_key(label): k
                               for k, label in enumerate(path_labels)}
                protected = {
                    str(key): float(g[path_lookup[key]])
                    for key in (("U-", 263), ("H-", (10, 263)),
                                ("U-", 1), ("H-", (1, 54)))
                    if key in path_lookup
                }
                allowed_lattice = keys in (pre_keys, wall_keys, far_keys)
            else:
                keys, base, rails, protected = set(), False, False, {}
                allowed_lattice = False
            certified = bool(
                actual.valid
                and set(actual.active) == set(ids)
                and summary["class"] == [2, 2, 2]
                and summary["f_vector"] in ([61, 162, 103], [61, 161, 102])
                and base and rails and allowed_lattice
                and all(value > 0 for value in protected.values())
            )
            segment_scan.append({
                "segment": segment,
                "t": float(t),
                "valid": actual.valid,
                "error": actual.error,
                "f_vector": summary["f_vector"] if actual.valid else None,
                "class": summary["class"] if actual.valid else None,
                "topology_margin": actual.topology_margin,
                "base_face_present": base,
                "rails_present": rails,
                "allowed_lattice": allowed_lattice,
                "protected_guards": protected,
                "certified": certified,
            })

    out = {
        "version": 1,
        "method": "six-row nullspace topology/mechanics cross",
        "source": str(SOURCE),
        "event": str(EVENT),
        "constraint_keys": [[a, list(b) if isinstance(b, tuple) else b]
                            for a, b in constraint_keys]
                           + [["quad_oriented_volume", list((7, 8, 245, 246))]],
        "constraint_singular_values": singular_values.tolist(),
        "constraint_rank": int(np.linalg.matrix_rank(constraint_jac)),
        "nullspace_dimension": int(null_basis.shape[1]),
        "transverse_direction": transverse.tolist(),
        "constraint_derivatives_along_transverse": (
            constraint_jac @ transverse
        ).tolist(),
        "U263_derivative_along_transverse": float(
            jac[wall_index] @ transverse
        ),
        "audits": audits,
        "quadrant_classes": {
            k: audits[k]["fresh_actual"]["class"]
            for k in ("pre_bad", "pre_good", "far_bad", "far_good")
        },
        "null_cross_succeeds": (
            audits["pre_good"]["fresh_actual"]["class"] == [2, 2, 2]
            and audits["far_good"]["fresh_actual"]["class"] == [2, 2, 2]
            and audits["pre_good"]["fresh_actual"]["valid"]
            and audits["far_good"]["fresh_actual"]["valid"]
        ),
        "segment_scan": segment_scan,
        "segment_valid_counts": {
            segment: sum(p["valid"] for p in segment_scan
                         if p["segment"] == segment)
            for segment in ("pre_to_buffer", "buffered_cross", "far_deepen")
        },
        "segment_certified_counts": {
            segment: sum(p["certified"] for p in segment_scan
                         if p["segment"] == segment)
            for segment in ("pre_to_buffer", "buffered_cross", "far_deepen")
        },
        "sampled_path_certified": all(p["certified"] for p in segment_scan),
        "minimum_sampled_topology_margin": min(
            p["topology_margin"] for p in segment_scan if p["valid"]
        ),
        "note": (
            "Three 41-point segments certify a sampled class-222 path through "
            "the grouped topology wall and into the new diagonal cell."
        ),
    }
    OUT.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({
        "rank": out["constraint_rank"],
        "nullspace_dimension": out["nullspace_dimension"],
        "constraint_derivatives": out[
            "constraint_derivatives_along_transverse"
        ],
        "quadrant_classes": out["quadrant_classes"],
        "quadrant_valid": {k: audits[k]["fresh_actual"]["valid"]
                           for k in out["quadrant_classes"]},
        "null_cross_succeeds": out["null_cross_succeeds"],
        "segment_valid_counts": out["segment_valid_counts"],
        "segment_certified_counts": out["segment_certified_counts"],
        "sampled_path_certified": out["sampled_path_certified"],
        "minimum_sampled_topology_margin": out[
            "minimum_sampled_topology_margin"
        ],
        "far_good_hard": audits["far_good"]["hard_margin"],
        "deep_far_hard": audits["deep_far"]["hard_margin"],
        "deep_far_topology_margin": audits["deep_far"]["fresh_actual"][
            "topology_margin"
        ],
    }, indent=2))


if __name__ == "__main__":
    main()
