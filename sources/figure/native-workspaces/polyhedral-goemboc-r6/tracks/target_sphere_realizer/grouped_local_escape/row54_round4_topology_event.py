#!/usr/bin/env python3
"""Materialize the first directed round-4 topology event and its far cell."""
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

SOURCE = HERE / "row54_combined_hard_slp_round4c_best.csv"
OUT = HERE / "row54_round4_topology_event.json"
QUAD = (7, 8, 245, 246)


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

    def construct(z):
        q = direct.construct(z[:n_direct])
        qn = (q - origin) / scale
        theta = z[n_direct:]
        den = 1.0 + qn @ theta[:3]
        if np.min(den) <= 0.08:
            raise RuntimeError("invalid chart")
        a, b, c, d, e = theta[3:]
        h = np.array([[a, b, c], [b, d, e],
                      [c, e, -a - d]], dtype=float)
        return origin + scale * ((qn / den[:, None]) @ expm(h).T)

    def fixed(z):
        points = construct(z)
        return (*guards(core.mechanics(ids, points, source_faces), source_faces),
                points)

    zero = np.zeros(n_direct + 8)
    g0, labels, _ = fixed(zero)
    lookup = {label_key(label): k for k, label in enumerate(labels)}
    wall_indices = [lookup[("U-", 263)], lookup[("U-", 1)]]
    target_keys = [
        ("U-", 54), ("H-", (6, 7)),
        ("S-", (7, 245, 246)), ("H-", (198, 263)),
    ]
    target_indices = [lookup[k] for k in target_keys]
    epsilon = 2e-6
    jac = np.empty((len(g0), len(zero)))
    for j in range(len(zero)):
        step = np.zeros(len(zero))
        step[j] = epsilon
        jac[:, j] = (fixed(step)[0] - fixed(-step)[0]) / (2 * epsilon)
    wall_jac = jac[wall_indices]
    target_jac = jac[target_indices]
    lp = linprog(
        np.r_[np.zeros(len(zero)), -1.0],
        A_ub=np.c_[-target_jac, np.ones(len(target_indices))],
        b_ub=g0[target_indices] - float(np.min(g0[target_indices])),
        A_eq=np.c_[wall_jac, np.zeros(len(wall_indices))],
        b_eq=np.zeros(len(wall_indices)),
        bounds=[(-1.0, 1.0)] * len(zero) + [(None, None)],
        method="highs",
    )
    if not lp.success:
        raise RuntimeError(lp.message)
    direction = lp.x[:-1]

    def points_at(s):
        return construct(s * direction)

    def determinant(s):
        p = points_at(s)
        q = [p[local[i]] for i in QUAD]
        return float(np.dot(q[1] - q[0],
                            np.cross(q[2] - q[0], q[3] - q[0])))

    root = float(brentq(determinant, 2e-8, 2.5e-8,
                        xtol=np.nextafter(0.0, 1.0), rtol=1e-15))
    wall_points = points_at(root)
    # Project only the last quad vertex onto the other three's plane.  The
    # correction is at rounding scale and materializes an exactly grouped wall
    # independently of scalar-root conditioning.
    q0, q1, q2 = (wall_points[local[i]] for i in QUAD[:3])
    normal = np.cross(q1 - q0, q2 - q0)
    correction = normal * (float(np.dot(wall_points[local[QUAD[3]]] - q0,
                                         normal))
                           / float(np.dot(normal, normal)))
    wall_points[local[QUAD[3]]] -= correction

    source_actual = evaluate(dict(zip(ids, source)), coplanar_rel=1e-11)
    wall_actual = evaluate(dict(zip(ids, wall_points)), coplanar_rel=1e-11)
    if not source_actual.valid or not wall_actual.valid:
        raise RuntimeError((source_actual.error, wall_actual.error))
    old_faces = {frozenset((7, 245, 246)), frozenset((7, 8, 246))}
    new_faces = {frozenset((7, 8, 245)), frozenset((8, 245, 246))}
    far_keys_expected = (source_keys - old_faces) | new_faces

    scan = []
    far = None
    far222 = None
    first_class233 = None
    deltas = np.unique(np.r_[np.geomspace(1e-12, 1e-6, 80),
                             [6e-10, 1e-9, 2e-9, 5e-9, 1e-8, 2e-8,
                              5e-8, 1e-7],
                             np.asarray([2.45e-8, 2.47e-8, 2.48e-8,
                                         2.49e-8, 2.50e-8, 2.51e-8,
                                         2.52e-8, 2.55e-8, 2.60e-8,
                                         2.70e-8, 3.00e-8]) - root])
    for delta in deltas:
        s = root + float(delta)
        points = points_at(s)
        actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11,
                          strict_tol=1e-12)
        keys = {frozenset(f["cycle"]) for f in actual.faces} if actual.valid else set()
        packet = {
            "s": s,
            "delta_from_wall": float(delta),
            "valid": actual.valid,
            "error": actual.error,
            "f_vector": summarize(actual)["f_vector"] if actual.valid else None,
            "class": summarize(actual)["class"] if actual.valid else None,
            "far_face_lattice": keys == far_keys_expected,
            "topology_margin": actual.topology_margin,
        }
        scan.append(packet)
        if far is None and actual.valid and keys == far_keys_expected:
            far = (s, points, actual)
        if (far222 is None and actual.valid and keys == far_keys_expected
                and summarize(actual)["class"] == [2, 2, 2]):
            far222 = (s, points, actual)
        if (first_class233 is None and actual.valid and keys == far_keys_expected
                and summarize(actual)["class"] == [2, 3, 3]):
            first_class233 = (s, points, actual)
    if far is None:
        raise RuntimeError("no certifiable far-side cell")

    def audit(name, s, points, actual):
        faces = [f["cycle"] for f in actual.faces]
        g, labels = guards(core.mechanics(ids, points, faces), faces)
        lookup = {label_key(label): k for k, label in enumerate(labels)}
        keys = {frozenset(f["cycle"]) for f in actual.faces}
        edges = set(actual.edges)
        ledger_keys = [
            ("U-", 54), ("H-", (6, 7)),
            ("H-", (198, 263)), ("U-", 263),
            ("H-", (10, 263)), ("U-", 1), ("H-", (1, 54)),
        ]
        ledger = {}
        for key in ledger_keys:
            if key in lookup:
                ledger[str(key)] = float(g[lookup[key]])
        return {
            "name": name,
            "s": float(s),
            "fresh_actual": summarize(actual),
            "base_face_present": BASE in keys,
            "rail_edges_present": {
                rail_name: all(tuple(sorted(e)) in edges
                               for e in zip(path, path[1:]))
                for rail_name, path in (("short", SHORT_RAIL),
                                        ("long", LONG_RAIL))
            },
            "guard_ledger": ledger,
            "hard_margin": float(np.min(g)),
        }

    far_s, far_points, far_actual = far
    audits = {
        "pre": audit("pre", 0.0, source, source_actual),
        "wall": audit("wall", root, wall_points, wall_actual),
        "far": audit("far", far_s, far_points, far_actual),
    }
    write_csv(OUT.with_name(OUT.stem + "_pre.csv"), ids, source)
    write_csv(OUT.with_name(OUT.stem + "_wall.csv"), ids, wall_points)
    write_csv(OUT.with_name(OUT.stem + "_far.csv"), ids, far_points)
    for name, actual in (("wall", wall_actual), ("far", far_actual)):
        OUT.with_name(OUT.stem + f"_{name}_faces.json").write_text(
            json.dumps([f["cycle"] for f in actual.faces], indent=2) + "\n"
        )
    out = {
        "version": 1,
        "method": "directed tangent LP plus exact quad determinant",
        "source": str(SOURCE),
        "direction": direction.tolist(),
        "target_directional_derivatives": (target_jac @ direction).tolist(),
        "protected_wall_directional_derivatives": (
            wall_jac @ direction
        ).tolist(),
        "quad": list(QUAD),
        "oriented_volume_root": root,
        "oriented_volume_at_scalar_root": determinant(root),
        "wall_projection_correction_norm": float(np.linalg.norm(correction)),
        "flip": {
            "removed_faces": [sorted(f) for f in old_faces],
            "added_faces": [sorted(f) for f in new_faces],
        },
        "audits": audits,
        "first_certifiable_far_s": far_s,
        "first_certifiable_far_class222_s": (
            None if far222 is None else far222[0]
        ),
        "first_certifiable_class233_s": (
            None if first_class233 is None else first_class233[0]
        ),
        "event_order": (
            "quad wall first; no mandatory-Gram-valid far-side class222 "
            "sample was found before the U263/H(10,263) recross"
            if far222 is None else
            "quad flip first; a nonempty far-side class222 cell precedes "
            "the U263/H(10,263) recross"
        ),
        "scan": scan,
    }
    OUT.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({
        "root": root,
        "root_determinant": out["oriented_volume_at_scalar_root"],
        "projection_correction": out["wall_projection_correction_norm"],
        "flip": out["flip"],
        "classes": {k: v["fresh_actual"]["class"]
                    for k, v in audits.items()},
        "f_vectors": {k: v["fresh_actual"]["f_vector"]
                      for k, v in audits.items()},
        "topology_margins": {k: v["fresh_actual"]["topology_margin"]
                             for k, v in audits.items()},
        "first_far_s": far_s,
        "first_far_class222_s": out["first_certifiable_far_class222_s"],
        "first_class233_s": out["first_certifiable_class233_s"],
        "event_order": out["event_order"],
    }, indent=2))


if __name__ == "__main__":
    main()
