#!/usr/bin/env python3
"""Rebuild the correct old-minus-16-plus-16 combined target by Tutte + LP.

The outer face already contains row 54 and the quad already contains row 246,
so the realization is directly in the desired (61,161,102) face lattice.
All non-base faces form a planar Tutte disk.  With xy fixed, asking every face
plane to support all vertices is a linear program in the 43 interior heights.
"""
from __future__ import annotations

from collections import Counter, defaultdict, deque
from pathlib import Path
import json

import numpy as np
from scipy.optimize import linprog
from scipy.spatial import ConvexHull

import combined_core as core


HERE = Path(__file__).resolve().parent
SOURCE_FACES = core.ROOT / "M42_acute_bridge_fifth_cell_complete" / "fifth_cell_endpoint" / "face_cycles.json"
BASE_CYCLE = [0, 54] + list(range(1, 17))
QUAD_CYCLE = [7, 245, 246, 8]
OLD_SWAP = {51, 52, 64, 94, *range(65, 77)}
NEW_SWAP = (
    [[198, 228, 229], [198, 228, 258], [198, 229, 230]]
    + [[198, k, k + 1] for k in range(230, 241)]
    + [[224, 247, 258], [228, 247, 258]]
)


def target_faces():
    source = json.loads(SOURCE_FACES.read_text())
    remove = OLD_SWAP | {0, 2, 15, 16}
    faces = [list(c) for i, c in enumerate(source) if i not in remove]
    faces += [list(c) for c in NEW_SWAP]
    faces = [BASE_CYCLE, QUAD_CYCLE] + faces

    # Orient the sphere consistently from the chosen base orientation.
    ef = defaultdict(list)
    for fi, cyc in enumerate(faces):
        for u, v in zip(cyc, cyc[1:] + cyc[:1]):
            ef[tuple(sorted((u, v)))].append(fi)
    if Counter(map(len, ef.values())) != Counter({2: 161}):
        raise ValueError((len(faces), len(ef), Counter(map(len, ef.values()))))
    seen = {0}
    q = deque([0])
    while q:
        fi = q.popleft()
        cyc = faces[fi]
        for u, v in zip(cyc, cyc[1:] + cyc[:1]):
            edge = tuple(sorted((u, v)))
            fj = next(z for z in ef[edge] if z != fi)
            if fj in seen:
                continue
            other = faces[fj]
            same = any((a, b) == (u, v) for a, b in zip(other, other[1:] + other[:1]))
            if same:
                faces[fj] = [other[0]] + list(reversed(other[1:]))
            seen.add(fj)
            q.append(fj)
    if len(seen) != 102:
        raise ValueError("target sphere is disconnected")
    return faces, dict(ef)


def tutte_xy(faces, incidence, radial_power=1.0):
    ids = sorted(set().union(*(set(c) for c in faces)))
    boundary = list(faces[0])
    interior = [i for i in ids if i not in boundary]
    neighbors = defaultdict(set)
    for u, v in incidence:
        neighbors[u].add(v)
        neighbors[v].add(u)

    xy = {}
    m = len(boundary)
    # Clockwise boundary: the cap triangles then have consistent positive
    # projected orientation with the chosen sphere orientation.
    for k, i in enumerate(boundary):
        theta = -2.0 * np.pi * k / m
        radius = 1.0 + 0.04 * np.cos(3.0 * theta) + 0.025 * np.sin(5.0 * theta)
        xy[i] = radius * np.asarray((np.cos(theta), np.sin(theta)))

    pos = {i: k for k, i in enumerate(interior)}
    A = np.zeros((len(interior), len(interior)))
    B = np.zeros((len(interior), 2))
    for i in interior:
        r = pos[i]
        A[r, r] = len(neighbors[i])
        for j in neighbors[i]:
            if j in pos:
                A[r, pos[j]] -= 1.0
            else:
                B[r] += xy[j]
    sol = np.linalg.solve(A, B)
    for i in interior:
        xy[i] = sol[pos[i]]
    return ids, boundary, interior, xy


def barycentric_xy(xy, tri, p):
    M = np.asarray(
        [
            [xy[tri[0]][0], xy[tri[1]][0], xy[tri[2]][0]],
            [xy[tri[0]][1], xy[tri[1]][1], xy[tri[2]][1]],
            [1.0, 1.0, 1.0],
        ]
    )
    return np.linalg.solve(M, np.asarray((xy[p][0], xy[p][1], 1.0)))


def height_lp(ids, boundary, interior, xy, faces, z_floor=0.0):
    pos = {i: k for k, i in enumerate(interior)}
    n = len(interior)
    Aub = []
    bub = []
    Aeq = []
    beq = []

    # Quad coplanarity in the chosen triangulation chart.
    quad = faces[1]
    lam = barycentric_xy(xy, quad[:3], quad[3])
    eq = np.zeros(n + 1)
    if quad[3] in pos:
        eq[pos[quad[3]]] += 1.0
    for a, w in zip(quad[:3], lam):
        if a in pos:
            eq[pos[a]] -= w
    Aeq.append(eq)
    beq.append(0.0)

    for fi, cyc in enumerate(faces[1:], start=1):
        tri = cyc[:3]
        cs = set(cyc)
        for j in ids:
            if j in cs:
                continue
            lam = barycentric_xy(xy, tri, j)
            # plane_f(x_j)-z_j >= t; convert to <= form.
            row = np.zeros(n + 1)
            for a, w in zip(tri, lam):
                if a in pos:
                    row[pos[a]] -= w
            if j in pos:
                row[pos[j]] += 1.0
            row[-1] += 1.0
            Aub.append(row)
            bub.append(0.0)

    c = np.zeros(n + 1)
    c[-1] = -1.0
    bounds = [(z_floor, 1.0)] * n + [(0.0, 1.0)]
    lp = linprog(
        c,
        A_ub=np.asarray(Aub),
        b_ub=np.asarray(bub),
        A_eq=np.asarray(Aeq),
        b_eq=np.asarray(beq),
        bounds=bounds,
        method="highs",
    )
    if not lp.success:
        raise RuntimeError(lp.message)
    z = {i: 0.0 for i in boundary}
    for i in interior:
        z[i] = float(lp.x[pos[i]])
    return z, float(lp.x[-1]), lp


def maximal_float_faces(points, tol=5e-8):
    ids = sorted(points)
    xyz = np.asarray([points[i] for i in ids])
    hull = ConvexHull(xyz, qhull_options="Qt Qx")
    # Union triangulated Qhull facets whose normalized planes agree.
    groups = []
    for simplex in hull.simplices:
        verts = {ids[int(k)] for k in simplex}
        a, b, c = [points[i] for i in verts]
        n = np.cross(b - a, c - a)
        n /= np.linalg.norm(n)
        h = float(np.dot(n, a))
        if h < 0:
            n, h = -n, -h
        hit = None
        for g in groups:
            if np.linalg.norm(n - g[0]) < tol and abs(h - g[1]) < tol:
                hit = g
                break
        if hit is None:
            groups.append([n, h, set(verts)])
        else:
            hit[2].update(verts)
    return hull, [frozenset(g[2]) for g in groups]


def build():
    faces, incidence = target_faces()
    ids, boundary, interior, xy = tutte_xy(faces, incidence)
    z, vertical_margin, lp = height_lp(ids, boundary, interior, xy, faces)
    points = {i: np.asarray((xy[i][0], xy[i][1], z[i])) for i in ids}
    faces = core.orient_faces_for_positive_volume(points, faces)
    hull, actual = maximal_float_faces(points)
    expected = {frozenset(c) for c in faces}
    if set(actual) != expected:
        missing = sorted([sorted(x) for x in expected - set(actual)])
        extra = sorted([sorted(x) for x in set(actual) - expected])
        raise RuntimeError(f"wrong hull: missing={missing[:10]} extra={extra[:10]} count={len(actual)}")
    chart = core.make_chart(points)
    x0 = chart.pack(points)
    best = core.choose_tree(points, faces, incidence, trials=12000, seed=831510)
    key, tree, pv, pf, vals, labels = best
    geom = core.raw_geometry(points, faces, incidence)
    stable, unstable, saddles = core.class_counts(geom, faces, incidence)
    guards = np.concatenate((geom["support_guards"], geom["polygon_guards"]))

    np.save(HERE / "target_combined_start_chart.npy", x0)
    np.save(HERE / "target_combined_points.npy", np.asarray([points[i] for i in ids]))
    payload = {
        "verdict": "CORRECT_TARGET_SPHERE_COMBINED_ENDPOINT_RECONSTRUCTED",
        "f_vector": [len(hull.vertices), len(incidence), len(faces)],
        "ids": ids,
        "faces": faces,
        "base_face": faces[0],
        "quad_face": faces[1],
        "old_faces_removed": sorted(OLD_SWAP),
        "new_faces_inserted": NEW_SWAP,
        "vertical_lp_margin": vertical_margin,
        "height_min": min(z[i] for i in interior),
        "height_max": max(z[i] for i in interior),
        "chart_dimension": len(x0),
        "tree_edges": [list(e) for e in sorted(tree)],
        "forced_rail_edges": [list(e) for e in sorted(core.forced_rail_edges())],
        "omitted_full_cycle_edge": [228, 229],
        "vertex_parent": {str(k): v for k, v in pv.items() if v is not None},
        "face_parent": {str(k): {"face": v[0], "edge": list(v[1])} for k, v in pf.items() if v[0] is not None},
        "ledger_rows": len(vals),
        "ledger_labels": labels,
        "ledger_values": vals.tolist(),
        "ledger_positive": int(np.sum(vals > 0)),
        "ledger_hard_min": float(np.min(vals)),
        "topology_guard_min": float(np.min(guards)),
        "raw_class": [len(stable), len(unstable), len(saddles)],
        "raw_stable_faces": [{"face": i, "cycle": faces[i]} for i in stable],
        "raw_unstable_vertices": unstable,
        "raw_saddle_edges": [list(e) for e in saddles],
        "tree_search_key": list(key),
        "xy": {str(i): xy[i].tolist() for i in ids},
        "z": {str(i): z[i] for i in ids},
    }
    (HERE / "target_combined_reconstruction.json").write_text(json.dumps(payload, indent=2))
    print(json.dumps({k: payload[k] for k in ("f_vector", "vertical_lp_margin", "height_min", "chart_dimension", "ledger_positive", "ledger_hard_min", "topology_guard_min", "raw_class")}, indent=2))


def load_problem():
    data = json.loads((HERE / "target_combined_reconstruction.json").read_text())
    faces = [list(c) for c in data["faces"]]
    incidence = defaultdict(list)
    for fi, cyc in enumerate(faces):
        for u, v in zip(cyc, cyc[1:] + cyc[:1]):
            incidence[tuple(sorted((u, v)))].append(fi)
    ids = data["ids"]
    arr = np.load(HERE / "target_combined_points.npy")
    points = {i: arr[k].copy() for k, i in enumerate(ids)}
    chart = core.make_chart(points)
    tree = {tuple(e) for e in data["tree_edges"]}
    pv, pf = core.tree_ledger(tree, faces, dict(incidence))
    x0 = np.load(HERE / "target_combined_start_chart.npy")
    return chart, faces, dict(incidence), pv, pf, x0


if __name__ == "__main__":
    build()
