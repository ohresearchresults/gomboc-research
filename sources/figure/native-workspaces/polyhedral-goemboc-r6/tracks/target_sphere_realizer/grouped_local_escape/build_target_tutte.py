#!/usr/bin/env python3
"""Reconstruct the lost old-minus-16-plus-16 target sphere realization.

The combinatorial swap is the exact relay-disk/octahedral shortcut recovered
from the run state.  A regular 17-gon is fixed as outer boundary, the 44
interior vertices receive the uniform Tutte embedding, and a height LP makes
every target triangle a strict upper supporting plane.  The base is z=0.
"""
from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.optimize import linprog
from scipy.spatial import ConvexHull

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[2]
SOURCE = PROJECT / "M42_acute_bridge_fifth_cell_complete" / "fifth_cell_endpoint"
BASE = list(range(17))


def target_faces() -> tuple[list[list[int]], list[list[int]], list[list[int]]]:
    faces = [list(c) for c in json.load(open(SOURCE / "face_cycles.json"))]
    old = [
        [198, 224, 241],
        [198, 224, 258],
        [224, 229, 230],
        [224, 229, 247],
        *[[224, k, k + 1] for k in range(230, 241)],
        [228, 229, 247],
    ]
    new = [
        [198, 228, 229],
        [198, 228, 258],
        [198, 229, 230],
        *[[198, k, k + 1] for k in range(230, 241)],
        [224, 247, 258],
        [228, 247, 258],
    ]
    assert len(old) == len(new) == 16
    oldkeys = {frozenset(c) for c in old}
    have = {frozenset(c) for c in faces}
    assert oldkeys <= have and not ({frozenset(c) for c in new} & have)
    target = [c for c in faces if frozenset(c) not in oldkeys] + new
    assert len(target) == 104
    return target, old, new


def graph(faces: list[list[int]]) -> tuple[list[int], dict[int, set[int]], dict[tuple[int, int], list[int]]]:
    nb: dict[int, set[int]] = defaultdict(set)
    ef: dict[tuple[int, int], list[int]] = defaultdict(list)
    for fi, c in enumerate(faces):
        for a, b in zip(c, c[1:] + c[:1]):
            e = tuple(sorted((a, b)))
            ef[e].append(fi)
            nb[a].add(b)
            nb[b].add(a)
    ids = sorted(nb)
    assert len(ids) == 61 and len(ef) == 163 and all(len(z) == 2 for z in ef.values())
    assert len(ids) - len(ef) + len(faces) == 2
    return ids, nb, ef


def tutte(ids: list[int], nb: dict[int, set[int]]) -> dict[int, np.ndarray]:
    boundary = set(BASE)
    interior = [i for i in ids if i not in boundary]
    loc = {i: k for k, i in enumerate(interior)}
    # Clockwise/counterclockwise choice only reflects the eventual body.
    xy = {i: np.array([np.cos(2 * np.pi * i / 17), np.sin(2 * np.pi * i / 17)]) for i in BASE}
    A = np.zeros((len(interior), len(interior)))
    rhs = np.zeros((len(interior), 2))
    for i in interior:
        r = loc[i]
        A[r, r] = len(nb[i])
        for j in nb[i]:
            if j in loc:
                A[r, loc[j]] -= 1.0
            else:
                rhs[r] += xy[j]
    sol = np.linalg.solve(A, rhs)
    for i in interior:
        xy[i] = sol[loc[i]]
    return xy


def barycentric_2d(p: np.ndarray, tri: np.ndarray) -> np.ndarray:
    M = np.vstack((tri.T, np.ones(3)))
    return np.linalg.solve(M, np.r_[p, 1.0])


def height_lp(ids: list[int], xy: dict[int, np.ndarray], faces: list[list[int]]) -> tuple[dict[int, float], float, dict]:
    interior = [i for i in ids if i not in set(BASE)]
    loc = {i: k for k, i in enumerate(interior)}
    gamma_idx = len(interior)
    rows = []
    meta = []
    triangles = [c for c in faces if set(c) != set(BASE)]
    assert len(triangles) == 103 and all(len(c) == 3 for c in triangles)
    for fi, c in enumerate(triangles):
        tri = np.stack([xy[i] for i in c])
        for j in ids:
            if j in c:
                continue
            lam = barycentric_2d(xy[j], tri)
            row = np.zeros(len(interior) + 1)
            if j in loc:
                row[loc[j]] += 1.0
            for v, z in zip(c, lam):
                if v in loc:
                    row[loc[v]] -= z
            row[gamma_idx] = 1.0
            rows.append(row)
            meta.append((fi, tuple(c), j))
    A = np.asarray(rows)
    objective = np.zeros(len(interior) + 1)
    objective[gamma_idx] = -1.0
    bounds = [(0.0, 1.0)] * len(interior) + [(0.0, 1.0)]
    res = linprog(
        objective,
        A_ub=A,
        b_ub=np.zeros(len(A)),
        bounds=bounds,
        method="highs",
        options={
            "primal_feasibility_tolerance": 1e-10,
            "dual_feasibility_tolerance": 1e-10,
            "ipm_optimality_tolerance": 1e-12,
        },
    )
    assert res.success, res.message
    h = {i: 0.0 for i in BASE}
    for i in interior:
        h[i] = float(res.x[loc[i]])
    gamma = float(res.x[gamma_idx])
    vals = A @ res.x
    order = np.argsort(vals)[::-1]
    audit = {
        "constraints": len(rows),
        "gamma": gamma,
        "maximum_lhs": float(np.max(vals)),
        "tightest": [
            {"face": list(meta[k][1]), "other": meta[k][2], "lhs": float(vals[k])}
            for k in order[:32]
        ],
    }
    return h, gamma, audit


def hull_face_keys(P: dict[int, np.ndarray], tol: float = 1e-8) -> set[frozenset[int]]:
    ids = sorted(P)
    pts = np.stack([P[i] for i in ids])
    hull = ConvexHull(pts, qhull_options="Qt Qx")
    groups: list[dict] = []
    for tri, eq in zip(hull.simplices, hull.equations):
        n = eq[:3] / np.linalg.norm(eq[:3])
        off = eq[3] / np.linalg.norm(eq[:3])
        found = None
        for g in groups:
            if np.dot(n, g["n"]) > 1 - tol and abs(off - g["off"]) < tol:
                found = g
                break
        if found is None:
            found = {"n": n, "off": off, "verts": set()}
            groups.append(found)
        found["verts"].update(ids[int(k)] for k in tri)
    return {frozenset(g["verts"]) for g in groups}


def write_points(name: str, P: dict[int, np.ndarray]) -> None:
    with open(HERE / name, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source_id", "x", "y", "z"])
        for i in sorted(P):
            w.writerow([i, *(repr(float(z)) for z in P[i])])


def main() -> None:
    faces, old, new = target_faces()
    ids, nb, ef = graph(faces)
    xy = tutte(ids, nb)
    h, gamma, lp_audit = height_lp(ids, xy, faces)
    P = {i: np.array([xy[i][0], xy[i][1], h[i]]) for i in ids}
    actual = hull_face_keys(P, tol=1e-10)
    expected = {frozenset(c) for c in faces}
    assert actual == expected, (len(actual), len(expected), [sorted(c) for c in actual - expected], [sorted(c) for c in expected - actual])
    write_points("target_tutte_float.csv", P)

    # A denominator-1e9 reconstruction is ample for the tiny LP margin.  Try
    # 1e6 first to reproduce the historical robust-rational convention, then
    # fall back deterministically if that rounding is too coarse.
    rounded = None
    chosen_den = None
    for den in (10**6, 10**7, 10**8, 10**9, 10**10):
        QP = {i: np.rint(P[i] * den).astype(np.int64) / den for i in ids}
        if hull_face_keys(QP, tol=1e-10) == expected:
            rounded, chosen_den = QP, den
            break
    assert rounded is not None
    with open(HERE / "target_tutte_exact.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source_id", "x_int", "y_int", "z_int", "denominator", "x", "y", "z"])
        for i in ids:
            ints = np.rint(rounded[i] * chosen_den).astype(np.int64)
            w.writerow([i, *map(int, ints), chosen_den, *(repr(float(z)) for z in rounded[i])])
    report = {
        "verdict": "TARGET_SPHERE_REALIZED",
        "f_vector": [61, 163, 104],
        "old_faces": old,
        "new_faces": new,
        "tutte_boundary": BASE,
        "interior_vertices": 44,
        "height_lp": lp_audit,
        "rounded_denominator": chosen_den,
        "exact_face_set_match_after_rounding": True,
    }
    json.dump(report, open(HERE / "target_tutte_report.json", "w"), indent=2)
    json.dump(faces, open(HERE / "target_faces.json", "w"), indent=2)
    print("PASS target sphere", report["f_vector"], "gamma", gamma, "den", chosen_den)


if __name__ == "__main__":
    main()
