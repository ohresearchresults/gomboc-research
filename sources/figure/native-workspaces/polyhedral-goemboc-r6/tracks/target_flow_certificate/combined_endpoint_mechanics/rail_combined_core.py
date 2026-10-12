#!/usr/bin/env python3
"""Reproducible rail-preserving combined endpoint on the swapped target sphere.

This is the corrected reconstruction.  ``combined_core.py`` is intentionally
left in place as an old-lattice control.  Here the starting sphere is the
old-minus-16-plus-16 target Tutte sphere, the robust projective/SPD map is
applied with the *target sphere's* normalization, and the two merger points
are then audited by rebuilding the maximal-face hull.

The q246 point is selected in the wall plane so that the wall quad and all 61
vertices survive while both prescribed rail paths remain in the edge graph.
The more obvious orthogonal projection loses q264; the earlier far-side
tangent choice loses the forced edge (8,264).
"""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import csv
import json
import sys

import numpy as np
from scipy.linalg import expm

import combined_core as base


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ATLAS = ROOT / "tracks" / "circuit_atlas"
TARGET_CSV = ATLAS / "target_sphere_rebuilt.csv"
ROBUST_JSON = ATLAS / "robust_rebuilt_fast.json"
CANONICAL_WALL_CSV = ATLAS / "row54_combined_wall_rebuilt.csv"
CANONICAL_WALL_AUDIT = ATLAS / "row54_combined_wall_rebuilt_audit.json"

# These parameters are in the untransformed rebuilt-target coordinates.
TANGENT_A = -0.21
TANGENT_B = 0.0
EXTERIOR = 0.04
EDGE_FRACTION = 0.5

POINTS_CSV = HERE / "rail_combined_robust_wall.csv"
FACES_JSON = HERE / "rail_combined_faces.json"
START_NPY = HERE / "rail_combined_start_chart.npy"
REPORT_JSON = HERE / "rail_combined_reconstruction.json"


def _atlas_module():
    sys.path.insert(0, str(ATLAS))
    import row54_four_residual_search as atlas
    return atlas


def _read_target():
    rows = {}
    with TARGET_CSV.open() as f:
        for r in csv.DictReader(f):
            rows[int(r["source_id"])] = np.asarray(
                [float(r[k]) for k in ("x", "y", "z")], dtype=float
            )
    ids = sorted(rows)
    return ids, np.asarray([rows[i] for i in ids])


def _apply_target_reference_transform(target, points, theta):
    """Apply the robust map using target's normalization, not wall's."""
    origin = target.mean(axis=0)
    scale = float(np.sqrt(np.mean(np.sum((target - origin) ** 2, axis=1))))
    z = (points - origin) / scale
    pole = theta[:3]
    den = 1.0 + z @ pole
    if float(np.min(den)) <= 0.08:
        raise ValueError(f"projective pole crossed: {float(np.min(den))}")
    a, b, c, d, e = theta[3:]
    h = np.asarray([[a, b, c], [b, d, e], [c, e, -a - d]])
    linear = expm(h)
    return (z / den[:, None]) @ linear.T, den


def _incidence(faces):
    ans = defaultdict(list)
    for fi, cyc in enumerate(faces):
        for u, v in zip(cyc, cyc[1:] + cyc[:1]):
            ans[tuple(sorted((u, v)))].append(fi)
    if not all(len(fs) == 2 for fs in ans.values()):
        raise ValueError("nonmanifold rail-wall face lattice")
    return dict(ans)


def build_geometry():
    atlas = _atlas_module()
    ids, raw = _read_target()
    if CANONICAL_WALL_CSV.exists():
        rows = {}
        with CANONICAL_WALL_CSV.open() as f:
            for r in csv.DictReader(f):
                rows[int(r["source_id"])] = np.asarray(
                    [float(r[k]) for k in ("x", "y", "z")], dtype=float
                )
        if sorted(rows) != ids:
            raise ValueError("canonical wall has a different active row set")
        robust = np.asarray([rows[i] for i in ids])
        audit = json.loads(CANONICAL_WALL_AUDIT.read_text())
        meta = {
            "canonical_wall_source": str(CANONICAL_WALL_CSV.relative_to(ROOT)),
            "canonical_wall_audit": str(CANONICAL_WALL_AUDIT.relative_to(ROOT)),
            "theta": audit["robust_theta"],
            "minimum_projective_denominator": audit["construction"][
                "minimum_original_projective_denominator"
            ],
            "wall_construction": audit["construction"],
            "q54_robust": rows[54].tolist(),
            "q246_robust": rows[246].tolist(),
        }
    else:
        wall = atlas.build_rebuilt_combined_rows(
            ids, raw, 0.0, TANGENT_A, TANGENT_B, EXTERIOR, EDGE_FRACTION
        )
        theta = np.asarray(json.loads(ROBUST_JSON.read_text())["theta"], dtype=float)
        robust, den = _apply_target_reference_transform(raw, wall, theta)
        meta = {
            "theta": theta.tolist(),
            "minimum_projective_denominator": float(np.min(den)),
            "wall_parameters_raw_target_chart": {
                "tangent_a": TANGENT_A,
                "tangent_b": TANGENT_B,
                "far_depth": 0.0,
                "exterior": EXTERIOR,
                "edge_fraction": EDGE_FRACTION,
            },
            "q54_raw": wall[ids.index(54)].tolist(),
            "q246_raw": wall[ids.index(246)].tolist(),
            "q54_robust": robust[ids.index(54)].tolist(),
            "q246_robust": robust[ids.index(246)].tolist(),
        }
    hull, faces, _ = atlas.group_maximal_faces(ids, robust)
    faces.sort(
        key=lambda cyc: (
            0 if set(cyc) == set(base.BASE) else 1,
            min(cyc),
            len(cyc),
            tuple(cyc),
        )
    )
    incidence = _incidence(faces)
    active = set().union(*(set(c) for c in faces))
    f_vector = (len(active), len(incidence), len(faces))
    if f_vector != (61, 161, 102) or active != set(ids) or len(hull.vertices) != 61:
        raise ValueError(f"wrong rail-wall f-vector/active set: {f_vector}")
    if set(faces[0]) != set(base.BASE):
        raise ValueError("enlarged base is not the root face")
    if not any(set(c) == set(base.QUAD) for c in faces):
        raise ValueError("q246 wall quad is missing")
    forced = base.forced_rail_edges()
    if not forced <= set(incidence):
        raise ValueError(f"forced rail edges missing: {sorted(forced - set(incidence))}")
    qstar = {frozenset(c) for c in faces if 246 in c}
    expected_qstar = {
        frozenset((7, 8, 245, 246)),
        frozenset((8, 246, 264)),
        frozenset((198, 245, 246)),
        frozenset((198, 246, 264)),
    }
    if qstar != expected_qstar:
        raise ValueError(f"unexpected q246 star: {sorted(map(sorted, qstar))}")
    points = {i: robust[k] for k, i in enumerate(ids)}
    meta["q246_star"] = [list(c) for c in faces if 246 in c]
    return points, faces, incidence, meta


def save_reconstruction(trials=30000, seed=831500):
    robust, faces, incidence, meta = build_geometry()
    points, basis, origin, scale = base.rigid_base_chart(robust)
    faces = base.orient_faces_for_positive_volume(points, faces)
    chart = base.make_chart(points)
    x0 = chart.pack(points)
    key, tree, pv, pf, vals, labels = base.choose_tree(
        points, faces, incidence, trials=trials, seed=seed
    )
    geom = base.raw_geometry(points, faces, incidence)
    stable, unstable, saddles = base.class_counts(geom, faces, incidence)

    with POINTS_CSV.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(("source_id", "x", "y", "z"))
        for i in sorted(robust):
            w.writerow((i, *map(repr, robust[i])))
    FACES_JSON.write_text(json.dumps({"faces": faces}, indent=2))
    np.save(START_NPY, x0)
    payload = {
        "verdict": "REBUILT_RAIL_PRESERVING_COMBINED_ENDPOINT",
        "source_lattice": "rebuilt target sphere (old 16 faces removed, new 16 faces inserted)",
        "control_warning": "combined_core.py artifacts use the old unswapped lattice",
        "f_vector": [61, 161, 102],
        "active_vertices": sorted(points),
        "base_face": faces[0],
        "quad_face": next(c for c in faces if set(c) == set(base.QUAD)),
        "faces": faces,
        "edges": [[*e, *incidence[e]] for e in sorted(incidence)],
        "chart_dimension": len(x0),
        "chart_labels": list(chart.labels),
        "tree_edges": [list(e) for e in sorted(tree)],
        "forced_rail_edges": [list(e) for e in sorted(base.forced_rail_edges())],
        "omitted_full_cycle_edge": [228, 229],
        "vertex_parent": {str(k): v for k, v in pv.items() if v is not None},
        "face_parent": {
            str(k): {"face": v[0], "edge": list(v[1])}
            for k, v in pf.items() if v[0] is not None
        },
        "ledger_rows": len(vals),
        "ledger_labels": labels,
        "ledger_values": vals.tolist(),
        "ledger_positive": int(np.sum(vals > 0)),
        "mechanical_positive": int(np.sum(vals[:-1] > 0)),
        "ledger_hard_min": float(np.min(vals)),
        "mechanical_hard_min": float(np.min(vals[:-1])),
        "topology_guard_min": float(min(
            np.min(geom["support_guards"]), np.min(geom["polygon_guards"])
        )),
        "raw_class": [len(stable), len(unstable), len(saddles)],
        "raw_stable_faces": [{"face": i, "cycle": faces[i]} for i in stable],
        "raw_unstable_vertices": unstable,
        "raw_saddle_edges": [list(e) for e in saddles],
        "tree_search_key": list(key),
        "rigid_chart": {
            "origin": origin.tolist(), "basis": basis.tolist(), "scale": scale
        },
        **meta,
    }
    REPORT_JSON.write_text(json.dumps(payload, indent=2))
    print(json.dumps({k: payload[k] for k in (
        "f_vector", "chart_dimension", "ledger_positive", "mechanical_positive",
        "mechanical_hard_min", "topology_guard_min", "raw_class"
    )}, indent=2))
    return payload


def load_problem():
    robust, faces, incidence, _ = build_geometry()
    points, *_ = base.rigid_base_chart(robust)
    faces = base.orient_faces_for_positive_volume(points, faces)
    chart = base.make_chart(points)
    data = json.loads(REPORT_JSON.read_text())
    tree = {tuple(e) for e in data["tree_edges"]}
    pv, pf = base.tree_ledger(tree, faces, incidence)
    x0 = np.load(START_NPY)
    return chart, faces, incidence, pv, pf, x0


# Re-export the evaluator API consumed by the SLP driver.
evaluate_chart = base.evaluate_chart
class_counts = base.class_counts
rebuild_hull = base.rebuild_hull


if __name__ == "__main__":
    save_reconstruction()
