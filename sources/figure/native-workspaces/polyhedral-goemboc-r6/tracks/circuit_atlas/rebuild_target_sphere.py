#!/usr/bin/env python3
"""Reconstruct the lost old-minus-16-plus-16 target sphere.

The construction mirrors the durable description: recover the two boundary
disks of the explicit 16-tetrahedron OCT_X_SHORT_RELAY ball, replace the disk
present in the fifth-cell sphere, take a uniform Tutte embedding with the
17-gon base fixed to a regular polygon, and solve one linear height program.
No stochastic step is used.
"""
from __future__ import annotations

import csv
import itertools
import json
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
from scipy.optimize import linprog
from scipy.spatial import ConvexHull

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE_FACES = ROOT / "M42_acute_bridge_fifth_cell_work/fifth_cell_endpoint/face_cycles.json"


def relay_tetrahedra():
    tets = [(198, 224, k, k - 1) for k in range(241, 229, -1)]
    tets += [
        (198, 247, 224, 229),
        (198, 247, 229, 228),
        (198, 247, 228, 258),
        (198, 247, 258, 224),
    ]
    return [tuple(sorted(t)) for t in tets]


def boundary_triangles(tets):
    count = Counter()
    for t in tets:
        for f in itertools.combinations(t, 3):
            count[tuple(sorted(f))] += 1
    return {f for f, n in count.items() if n == 1}


def target_faces():
    old_cycles = json.load(SOURCE_FACES.open())
    old_triangles = {tuple(sorted(c)) for c in old_cycles if len(c) == 3}
    boundary = boundary_triangles(relay_tetrahedra())
    old_disk = boundary & old_triangles
    new_disk = boundary - old_triangles
    assert len(boundary) == 32 and len(old_disk) == len(new_disk) == 16
    faces = [c for c in old_cycles if tuple(sorted(c)) not in old_disk]
    faces += [list(f) for f in sorted(new_disk)]
    assert len(faces) == 104
    return faces, sorted(old_disk), sorted(new_disk)


def edge_graph(faces):
    edges = set()
    nbr = defaultdict(set)
    for cyc in faces:
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            e = tuple(sorted((a, b)))
            edges.add(e)
            nbr[a].add(b)
            nbr[b].add(a)
    return edges, nbr


def tutte(faces):
    edges, nbr = edge_graph(faces)
    vertices = sorted(nbr)
    base = list(range(17))
    interior = [i for i in vertices if i not in base]
    xy = {
        i: np.array([np.cos(2 * np.pi * i / 17), np.sin(2 * np.pi * i / 17)])
        for i in base
    }
    pos = {i: k for k, i in enumerate(interior)}
    a = np.zeros((len(interior), len(interior)))
    rhs = np.zeros((len(interior), 2))
    for i in interior:
        row = pos[i]
        a[row, row] = 1.0
        degree = len(nbr[i])
        for j in nbr[i]:
            if j in pos:
                a[row, pos[j]] -= 1.0 / degree
            else:
                rhs[row] += xy[j] / degree
    sol = np.linalg.solve(a, rhs)
    for i in interior:
        xy[i] = sol[pos[i]]
    return vertices, base, interior, xy, edges


def height_lp(faces, vertices, base, interior, xy):
    pos = {i: k for k, i in enumerate(interior)}
    n = len(interior)
    aub, bub = [], []
    for cyc in faces:
        if len(cyc) != 3:
            continue
        mat = np.vstack([[xy[i][0], xy[i][1], 1.0] for i in cyc]).T
        for j in vertices:
            if j in cyc:
                continue
            lam = np.linalg.solve(mat, np.array([xy[j][0], xy[j][1], 1.0]))
            row = np.zeros(n + 1)
            if j in pos:
                row[pos[j]] += 1.0
            for i, q in zip(cyc, lam):
                if i in pos:
                    row[pos[i]] -= q
            row[-1] = 1.0
            aub.append(row)
            bub.append(0.0)
    # Keep the base as the unique bottom face with the same optimized margin.
    for i in interior:
        row = np.zeros(n + 1)
        row[pos[i]] = -1.0
        row[-1] = 1.0
        aub.append(row)
        bub.append(0.0)
    objective = np.zeros(n + 1)
    objective[-1] = -1.0
    result = linprog(
        objective,
        A_ub=np.asarray(aub),
        b_ub=np.asarray(bub),
        bounds=[(0.0, 1.0)] * n + [(0.0, None)],
        method="highs",
    )
    if not result.success:
        raise RuntimeError(result.message)
    heights = {i: 0.0 for i in base}
    heights.update({i: float(result.x[pos[i]]) for i in interior})
    return heights, float(result.x[-1]), result


def group_face_sets(vertices, points, tol=3e-8):
    hull = ConvexHull(points, qhull_options="Qt Qx")
    groups = []
    for tri, eq0 in zip(hull.simplices, hull.equations):
        eq = eq0 / np.linalg.norm(eq0[:3])
        for old in groups:
            if np.max(np.abs(eq - old[0])) < tol:
                old[1].update(vertices[k] for k in tri)
                break
        else:
            groups.append([eq, set(vertices[k] for k in tri)])
    return hull, {frozenset(g[1]) for g in groups}


def main():
    faces, old_disk, new_disk = target_faces()
    vertices, base, interior, xy, edges = tutte(faces)
    heights, gamma, lp = height_lp(faces, vertices, base, interior, xy)
    points = np.array([[xy[i][0], xy[i][1], heights[i]] for i in vertices])
    hull, got = group_face_sets(vertices, points)
    wanted = {frozenset(c) for c in faces}
    assert got == wanted
    assert len(hull.vertices) == 61 and len(edges) == 163 and len(faces) == 104

    with (HERE / "target_sphere_rebuilt.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source_id", "x", "y", "z"])
        for i, p in zip(vertices, points):
            w.writerow([i, *[format(float(q), ".17g") for q in p]])
    json.dump(faces, (HERE / "target_sphere_rebuilt_faces.json").open("w"), indent=2)
    report = {
        "version": 1,
        "construction": "regular 17-gon + uniform Tutte embedding + upper-cap height LP",
        "relay_tetrahedra": [list(t) for t in relay_tetrahedra()],
        "old_disk": [list(f) for f in old_disk],
        "new_disk": [list(f) for f in new_disk],
        "height_lp_margin": gamma,
        "height_range_interior": [min(heights[i] for i in interior), max(heights[i] for i in interior)],
        "f_vector": [len(hull.vertices), len(edges), len(faces)],
        "qhull_triangles": len(hull.simplices),
        "all_target_face_sets_match": got == wanted,
        "vertices": vertices,
    }
    json.dump(report, (HERE / "target_sphere_rebuilt.json").open("w"), indent=2)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
