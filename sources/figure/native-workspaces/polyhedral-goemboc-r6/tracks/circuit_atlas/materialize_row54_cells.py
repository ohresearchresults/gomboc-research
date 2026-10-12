#!/usr/bin/env python3
"""Materialize and independently audit the robust row-54 endpoint cells.

The construction intentionally uses two coordinate charts:

* row 246 is moved in the *raw rebuilt target* before applying the already
  certified robust projective/SPD map (with the original source normalization
  held fixed); this is what preserves the two forced rail paths;
* row 54 is placed just outside edge 0--1 in the resulting robust base plane;
  this is the small endpoint move that changes U1 to U54 while retaining all
  61 hull vertices.

Every output is rebuilt with Qhull, grouped into maximal faces, evaluated at
its own volume centroid, and checked against the asserted face/rail data.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np
from scipy.linalg import expm

import row54_four_residual_search as core


HERE = Path(__file__).resolve().parent
RAW_SOURCE = HERE / "target_sphere_rebuilt.csv"
THETA_SOURCE = HERE / "robust_rebuilt_fast.json"

ENDPOINT_EXTERIOR = 0.01
ENDPOINT_EDGE_FRACTION = 0.9
WALL_TANGENT_A = -0.21
WALL_TANGENT_B = 0.0
FAR_DEPTH = 1.0e-5

QUAD = frozenset((7, 8, 245, 246))
TARGET_H = {(6, 7), (9, 10)}


def load_csv(path: Path):
    rows = {}
    with path.open() as f:
        for row in csv.DictReader(f):
            rows[int(row["source_id"])] = np.asarray(
                [float(row[k]) for k in ("x", "y", "z")], dtype=float
            )
    ids = sorted(rows)
    return ids, np.asarray([rows[i] for i in ids])


def robust_transform_with_fixed_reference(points: np.ndarray, reference: np.ndarray,
                                          theta: np.ndarray):
    """Apply the robust map without recomputing normalization after row moves."""
    origin = reference.mean(axis=0)
    scale = float(np.sqrt(np.mean(np.sum((reference - origin) ** 2, axis=1))))
    z = (points - origin) / scale
    den = 1.0 + z @ theta[:3]
    if float(np.min(den)) <= 0.0:
        raise ValueError("projective pole crossed the source point set")
    a, b, c, d, e = theta[3:]
    h = np.asarray([[a, b, c], [b, d, e], [c, e, -a - d]], dtype=float)
    return (z / den[:, None]) @ expm(h).T, den


def forced_rail_edges():
    short = [228] + list(range(229, 247)) + [8]
    long = [228] + list(range(247, 265)) + [8]
    edges = {
        tuple(sorted(edge))
        for path in (short, long)
        for edge in zip(path, path[1:])
    }
    edges.remove((228, 229))
    return edges


def wall_and_far_raw(ids: Sequence[int], raw: np.ndarray):
    ix = {i: k for k, i in enumerate(ids)}
    a = raw[ix[7]]
    n = np.cross(raw[ix[8]] - a, raw[ix[245]] - a)
    n = n / np.linalg.norm(n)
    signed_depth = float(np.dot(n, raw[ix[246]] - a))
    wall_projection = raw[ix[246]] - signed_depth * n
    u = raw[ix[8]] - a
    u = u / np.linalg.norm(u)
    v = np.cross(n, u)
    wall = wall_projection + WALL_TANGENT_A * u + WALL_TANGENT_B * v
    far = wall - np.sign(signed_depth) * FAR_DEPTH * n
    # Durable cross-check against the independently reconstructed rail-valid
    # coordinate supplied by the combined-mechanics track.
    selected = np.asarray(
        (-0.48253021382009076, 0.2923046074439142, 0.46444522728375714)
    )
    if not np.allclose(wall, selected, rtol=0.0, atol=6e-16):
        raise AssertionError((wall, selected))
    return wall, far, {
        "raw_plane_unit_normal": n.tolist(),
        "original_signed_depth": signed_depth,
        "raw_wall_projection": wall_projection.tolist(),
        "raw_tangent_u": u.tolist(),
        "raw_tangent_v": v.tolist(),
        "tangent_a": WALL_TANGENT_A,
        "tangent_b": WALL_TANGENT_B,
        "far_depth": FAR_DEPTH,
        "raw_wall_q246": wall.tolist(),
        "raw_far_q246": far.tolist(),
    }


def topology_audit(ids: Sequence[int], points: np.ndarray,
                   faces: Sequence[Sequence[int]], normals: Sequence[np.ndarray]):
    """Strict support and in-face convexity margins for every maximal face."""
    ix = {i: k for k, i in enumerate(ids)}
    support_rows = []
    polygon_rows = []
    coplanarity_rows = []
    for face_index, (cyc, n0) in enumerate(zip(faces, normals)):
        n = np.asarray(n0, dtype=float)
        n = n / np.linalg.norm(n)
        h = float(np.dot(n, points[ix[cyc[0]]]))
        cset = set(cyc)
        support = [
            h - float(np.dot(n, points[ix[j]])) for j in ids if j not in cset
        ]
        plane_errors = [
            abs(float(np.dot(n, points[ix[j]])) - h) for j in cyc
        ]
        polygon = []
        for u, v in zip(cyc, cyc[1:] + cyc[:1]):
            edge = points[ix[v]] - points[ix[u]]
            edge_norm = float(np.linalg.norm(edge))
            for j in cyc:
                if j in (u, v):
                    continue
                polygon.append(
                    float(np.dot(np.cross(edge, points[ix[j]] - points[ix[u]]), n))
                    / edge_norm
                )
        support_rows.append({
            "face_index": face_index,
            "face": list(cyc),
            "minimum_nonface_support_slack": float(min(support)),
        })
        polygon_rows.append({
            "face_index": face_index,
            "face": list(cyc),
            "minimum_polygon_edge_slack": float(min(polygon)),
        })
        coplanarity_rows.append({
            "face_index": face_index,
            "face": list(cyc),
            "maximum_coplanarity_error": float(max(plane_errors)),
        })
    return {
        "minimum_nonface_support_slack": min(
            row["minimum_nonface_support_slack"] for row in support_rows
        ),
        "minimum_polygon_edge_slack": min(
            row["minimum_polygon_edge_slack"] for row in polygon_rows
        ),
        "maximum_coplanarity_error": max(
            row["maximum_coplanarity_error"] for row in coplanarity_rows
        ),
        "support_by_face": support_rows,
        "polygon_by_face": polygon_rows,
        "coplanarity_by_face": coplanarity_rows,
    }


def requested_margins(mechanics, faces, stable_faces: Iterable[frozenset],
                      unstable_vertices: Iterable[int], saddle_edges: Iterable[tuple[int, int]]):
    stable_faces = set(stable_faces)
    unstable_vertices = set(unstable_vertices)
    saddle_edges = {tuple(sorted(e)) for e in saddle_edges}
    records = []
    for k, cyc in enumerate(faces):
        decision = float(mechanics["fdec"][k])
        requested_positive = frozenset(cyc) in stable_faces
        records.append({
            "kind": "face",
            "feature": list(cyc),
            "decision": decision,
            "requested_positive": requested_positive,
            "requested_signed_margin": decision if requested_positive else -decision,
            "components": [float(x) for x in mechanics["fcomponents"][k]],
        })
    for i, decision0 in mechanics["udec"].items():
        decision = float(decision0)
        requested_positive = i in unstable_vertices
        records.append({
            "kind": "vertex",
            "feature": i,
            "decision": decision,
            "requested_positive": requested_positive,
            "requested_signed_margin": decision if requested_positive else -decision,
            "components": [float(x) for x in mechanics["ucomponents"][i]],
        })
    for edge, decision0 in mechanics["edec"].items():
        decision = float(decision0)
        requested_positive = edge in saddle_edges
        records.append({
            "kind": "edge",
            "feature": list(edge),
            "decision": decision,
            "requested_positive": requested_positive,
            "requested_signed_margin": decision if requested_positive else -decision,
            "components": [float(x) for x in mechanics["ecomponents"][edge]],
        })
    records.sort(key=lambda r: (r["kind"], str(r["feature"])))
    signed = [r["requested_signed_margin"] for r in records]
    return {
        "hard_requested_margin": float(min(signed)),
        "minimum_absolute_decision": float(min(abs(r["decision"]) for r in records)),
        "records": records,
    }


def write_csv(path: Path, ids: Sequence[int], points: np.ndarray):
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(("source_id", "x", "y", "z"))
        for i, p in zip(ids, points):
            w.writerow([i, *[format(float(x), ".17g") for x in p]])


def set_of_faces(faces):
    return {frozenset(c) for c in faces}


def materialize(name: str, ids: Sequence[int], points: np.ndarray, expected_f_vector,
                expected_stable, expected_unstable, expected_saddles, construction,
                expected_q246_star=None, assert_forced=False):
    hull, faces, normals = core.group_maximal_faces(ids, points)
    mechanics, stable, unstable, saddles = core.classify(ids, points, faces)
    edges, _ = core.edge_lattice(faces)
    f_vector = [len(hull.vertices), len(edges), len(faces)]
    assert f_vector == list(expected_f_vector), f_vector
    assert mechanics["active"] == list(ids), mechanics["active"]
    assert set_of_faces(stable) == set(expected_stable), stable
    assert unstable == list(expected_unstable), unstable
    assert {tuple(e) for e in saddles} == {tuple(e) for e in expected_saddles}, saddles
    assert (0, 1) not in edges and (0, 54) in edges and (1, 54) in edges
    forced = forced_rail_edges()
    if assert_forced:
        assert forced <= set(edges), sorted(forced - set(edges))
    if expected_q246_star is not None:
        actual_star = {frozenset(c) for c in faces if 246 in c}
        assert actual_star == set(expected_q246_star), (
            sorted(map(sorted, actual_star)), sorted(map(sorted, expected_q246_star))
        )
    topology = topology_audit(ids, points, faces, normals)
    assert topology["minimum_nonface_support_slack"] > 0.0
    assert topology["minimum_polygon_edge_slack"] > 0.0
    csv_name = f"{name}.csv"
    faces_name = f"{name}_faces.json"
    audit_name = f"{name}_audit.json"
    write_csv(HERE / csv_name, ids, points)
    with (HERE / faces_name).open("w") as f:
        json.dump(faces, f, indent=2)
    margins = requested_margins(
        mechanics, faces, expected_stable, expected_unstable, expected_saddles
    )
    record = {
        "version": 1,
        "name": name,
        "source": str(RAW_SOURCE.name),
        "robust_theta_source": str(THETA_SOURCE.name),
        "robust_theta": construction["robust_theta"],
        "transform_convention": (
            "reference o=mean(raw source), s=rms_radius(raw source); "
            "z=(q-o)/s; den=1+pole.z; y=(z/den)@expm(H).T; "
            "H=[[a,b,c],[b,d,e],[c,e,-a-d]]"
        ),
        "construction": construction,
        "coordinates": csv_name,
        "fixed_expected_faces": faces_name,
        "fresh_hull_audit": {
            "f_vector": f_vector,
            "active": mechanics["active"],
            "centroid": mechanics["centroid"].tolist(),
            "class": [len(stable), len(unstable), len(saddles)],
            "stable_faces": stable,
            "unstable_vertices": unstable,
            "saddle_edges": saddles,
            "edge_0_1_present": (0, 1) in edges,
            "edge_0_54_present": (0, 54) in edges,
            "edge_1_54_present": (1, 54) in edges,
            "forced_rail_edge_count": len(forced),
            "all_forced_rail_edges_present": forced <= set(edges),
            "forced_rail_edges": [list(e) for e in sorted(forced)],
            "q246_star": [list(c) for c in faces if 246 in c],
        },
        "all_mechanics_margins": margins,
        "topology_audit": topology,
    }
    with (HERE / audit_name).open("w") as f:
        json.dump(record, f, indent=2)
    return record, faces


def main():
    ids, raw = load_csv(RAW_SOURCE)
    ix = {i: k for k, i in enumerate(ids)}
    theta = np.asarray(json.load(THETA_SOURCE.open())["theta"], dtype=float)
    robust, robust_den = robust_transform_with_fixed_reference(raw, raw, theta)

    # Endpoint row 54 is constructed in the robust base plane.  Restoring
    # q246 is necessary because build_wall_rows also projects it when depth=0.
    endpoint = core.build_wall_rows(
        ids, robust, 0.0, ENDPOINT_EXTERIOR, ENDPOINT_EDGE_FRACTION
    )
    endpoint[ix[246]] = robust[ix[246]]

    raw_wall_q246, raw_far_q246, q246_construction = wall_and_far_raw(ids, raw)
    moved_wall_raw = raw.copy()
    moved_wall_raw[ix[246]] = raw_wall_q246
    moved_far_raw = raw.copy()
    moved_far_raw[ix[246]] = raw_far_q246
    wall_q246_robust, wall_den = robust_transform_with_fixed_reference(
        moved_wall_raw, raw, theta
    )
    far_q246_robust, far_den = robust_transform_with_fixed_reference(
        moved_far_raw, raw, theta
    )
    wall = endpoint.copy()
    wall[ix[246]] = wall_q246_robust[ix[246]]
    far = endpoint.copy()
    far[ix[246]] = far_q246_robust[ix[246]]

    base = core.BASE
    endpoint_record, _ = materialize(
        "row54_endpoint_rebuilt", ids, endpoint, (61, 162, 103),
        {base, core.F0}, (8, 54), TARGET_H,
        {
            "robust_theta": theta.tolist(),
            "minimum_original_projective_denominator": float(np.min(robust_den)),
            "row54_chart": "post-robust enlarged-base exterior move",
            "row54_exterior": ENDPOINT_EXTERIOR,
            "row54_edge_fraction": ENDPOINT_EDGE_FRACTION,
            "row246_chart": "unchanged robust target row246",
        },
        expected_q246_star={
            core.F0, frozenset((8, 246, 264)), frozenset((198, 245, 246)),
            frozenset((198, 246, 263)), frozenset((246, 263, 264)),
        },
        assert_forced=True,
    )
    wall_record, _ = materialize(
        "row54_combined_wall_rebuilt", ids, wall, (61, 161, 102),
        {base, QUAD}, (8, 54), TARGET_H,
        {
            "robust_theta": theta.tolist(),
            "minimum_original_projective_denominator": float(np.min(robust_den)),
            "row54_chart": "post-robust enlarged-base exterior move",
            "row54_exterior": ENDPOINT_EXTERIOR,
            "row54_edge_fraction": ENDPOINT_EDGE_FRACTION,
            "row246_chart": "raw target plane tangent, then fixed-reference robust map",
            "row246_projective_denominator": float(wall_den[ix[246]]),
            **q246_construction,
        },
        expected_q246_star={
            QUAD, frozenset((8, 246, 264)), frozenset((198, 245, 246)),
            frozenset((198, 246, 264)),
        },
        assert_forced=True,
    )
    far_record, _ = materialize(
        "row54_far_rebuilt", ids, far, (61, 162, 103),
        {base, core.SFAR}, (8, 54), TARGET_H,
        {
            "robust_theta": theta.tolist(),
            "minimum_original_projective_denominator": float(np.min(robust_den)),
            "row54_chart": "post-robust enlarged-base exterior move",
            "row54_exterior": ENDPOINT_EXTERIOR,
            "row54_edge_fraction": ENDPOINT_EDGE_FRACTION,
            "row246_chart": "raw target far-side normal+tangent, then fixed-reference robust map",
            "row246_projective_denominator": float(far_den[ix[246]]),
            **q246_construction,
        },
        expected_q246_star={
            core.SFAR, frozenset((7, 245, 246)), frozenset((8, 246, 264)),
            frozenset((198, 245, 246)), frozenset((198, 246, 264)),
        },
        assert_forced=True,
    )

    print(json.dumps({
        "endpoint": {
            "f_vector": endpoint_record["fresh_hull_audit"]["f_vector"],
            "class": endpoint_record["fresh_hull_audit"]["class"],
            "hard_margin": endpoint_record["all_mechanics_margins"]["hard_requested_margin"],
            "topology_min": endpoint_record["topology_audit"]["minimum_nonface_support_slack"],
        },
        "wall": {
            "f_vector": wall_record["fresh_hull_audit"]["f_vector"],
            "class": wall_record["fresh_hull_audit"]["class"],
            "hard_margin": wall_record["all_mechanics_margins"]["hard_requested_margin"],
            "topology_min": wall_record["topology_audit"]["minimum_nonface_support_slack"],
        },
        "far": {
            "f_vector": far_record["fresh_hull_audit"]["f_vector"],
            "class": far_record["fresh_hull_audit"]["class"],
            "hard_margin": far_record["all_mechanics_margins"]["hard_requested_margin"],
            "topology_min": far_record["topology_audit"]["minimum_nonface_support_slack"],
        },
    }, indent=2))


if __name__ == "__main__":
    main()
