#!/usr/bin/env python3
"""Fresh-hull maximal-face evaluator with a scale-aware coplanarity test."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass

import numpy as np
from scipy.spatial import ConvexHull


@dataclass
class Result:
    valid: bool
    error: str | None
    active: list[int]
    faces: list[dict]
    edges: list[tuple[int, int]]
    edge_faces: dict[tuple[int, int], list[int]]
    centroid: np.ndarray
    volume: float
    stable: list[tuple[int, float]]
    unstable: list[tuple[int, float]]
    saddles: list[tuple[tuple[int, int], float]]
    face_decisions: list[float]
    vertex_decisions: dict[int, float]
    edge_decisions: dict[tuple[int, int], float]
    neighbors: dict[int, set[int]]
    topology_margin: float
    inactive_margin: float


def _boundary_cycle(tris: list[tuple[int, int, int]], n: np.ndarray, pts: np.ndarray) -> list[int]:
    count: dict[tuple[int, int], int] = defaultdict(int)
    for tri in tris:
        for a, b in ((tri[0], tri[1]), (tri[1], tri[2]), (tri[2], tri[0])):
            count[tuple(sorted((a, b)))] += 1
    bedges = [e for e, k in count.items() if k == 1]
    adj: dict[int, list[int]] = defaultdict(list)
    for a, b in bedges:
        adj[a].append(b)
        adj[b].append(a)
    if not adj or any(len(v) != 2 for v in adj.values()):
        raise ValueError("grouped facet has non-cyclic boundary")
    start = min(adj)
    cycle = [start]
    prev = None
    cur = start
    while True:
        nxt = adj[cur][0] if adj[cur][0] != prev else adj[cur][1]
        if nxt == start:
            break
        if nxt in cycle:
            raise ValueError("grouped facet boundary repeats")
        cycle.append(nxt)
        prev, cur = cur, nxt
    if len(cycle) != len(adj):
        raise ValueError("grouped facet has multiple boundary components")
    area = np.zeros(3)
    for a, b in zip(cycle, cycle[1:] + cycle[:1]):
        area += np.cross(pts[a], pts[b])
    if np.dot(area, n) < 0:
        cycle = [cycle[0]] + list(reversed(cycle[1:]))
    return cycle


def _groups(hull: ConvexHull, pts: np.ndarray, coplanar_tol: float) -> list[dict]:
    groups: list[dict] = []
    for tri, eq in zip(hull.simplices, hull.equations):
        tri = tuple(map(int, tri))
        n = np.asarray(eq[:3], float)
        off = float(eq[3])
        ln = np.linalg.norm(n)
        n, off = n / ln, off / ln
        found = None
        for g in groups:
            if np.dot(n, g["n"]) < 0:
                continue
            # Mutual point-to-plane tests distinguish genuinely coplanar
            # triangulations from very shallow but distinct adjacent faces.
            if max(abs(float(np.dot(g["n"], pts[i]) + g["off"])) for i in tri) > coplanar_tol:
                continue
            if max(abs(float(np.dot(n, pts[i]) + off)) for i in g["sample"]) > coplanar_tol:
                continue
            found = g
            break
        if found is None:
            groups.append({"n": n, "off": off, "tris": [tri], "sample": set(tri)})
        else:
            found["tris"].append(tri)
            found["sample"].update(tri)
    return groups


def evaluate(points: dict[int, np.ndarray], *, coplanar_rel: float = 2e-10, strict_tol: float = 1e-9) -> Result:
    ids = sorted(points)
    P = np.stack([np.asarray(points[i], float) for i in ids])
    scale = max(float(np.sqrt(np.mean(np.sum((P - np.mean(P, axis=0)) ** 2, axis=1)))), 1e-300)
    try:
        hull = ConvexHull(P, qhull_options="Qt Qx")
        groups = _groups(hull, P, coplanar_rel * scale)
        faces = []
        for g in groups:
            c = _boundary_cycle(g["tris"], g["n"], P)
            # Qhull equations become noticeably less accurate after a near-
            # pole projective map.  Recompute the face plane from its actual
            # grouped boundary, using translated coordinates to avoid the
            # large-origin cancellation in cross(P[a], P[b]).
            anchor = P[c[0]]
            area = np.zeros(3)
            for j in range(1, len(c) - 1):
                area += np.cross(P[c[j]] - anchor, P[c[j + 1]] - anchor)
            area_norm = float(np.linalg.norm(area))
            if not area_norm > 1e-300:
                raise ValueError("grouped face has zero geometric area")
            n_geom = area / area_norm
            if float(np.dot(n_geom, g["n"])) < 0:
                n_geom = -n_geom
            faces.append({
                "cycle_local": c,
                "cycle": [ids[i] for i in c],
                "n": n_geom,
                "off": -float(np.dot(n_geom, anchor)),
                "tris": g["tris"],
            })

        D6 = 0.0
        M24 = np.zeros(3)
        for f in faces:
            c = f["cycle_local"]
            for j in range(1, len(c) - 1):
                a, b, z = P[c[0]], P[c[j]], P[c[j + 1]]
                d = float(np.dot(a, np.cross(b, z)))
                D6 += d
                M24 += d * (a + b + z)
        volume = D6 / 6.0
        if not np.isfinite(volume) or volume <= 1e-14 * scale**3:
            raise ValueError(f"bad volume {volume}")
        centroid = M24 / (4.0 * D6)
        X = P - centroid
        radius = max(float(np.sqrt(np.mean(np.sum(X * X, axis=1)))), 1e-300)

        active_local = sorted(set(hull.vertices.tolist()))
        inactive_local = sorted(set(range(len(P))) - set(active_local))
        topo = []
        inactive_slacks = []
        for f in faces:
            vals = -(P @ f["n"] + f["off"]) / radius
            cs = set(f["cycle_local"])
            topo.extend(float(vals[i]) for i in range(len(P)) if i not in cs and i in active_local)
            inactive_slacks.extend(float(vals[i]) for i in inactive_local)
        topology_margin = min(topo, default=float("inf"))
        inactive_margin = min(inactive_slacks, default=float("inf"))

        ef_local: dict[tuple[int, int], list[int]] = defaultdict(list)
        for fi, f in enumerate(faces):
            c = f["cycle_local"]
            for a, b in zip(c, c[1:] + c[:1]):
                ef_local[tuple(sorted((a, b)))].append(fi)
        if any(len(v) != 2 for v in ef_local.values()):
            raise ValueError("nonmanifold true edge")
        neighbors: dict[int, set[int]] = defaultdict(set)
        for a, b in ef_local:
            neighbors[a].add(b)
            neighbors[b].add(a)

        fdec = []
        stable = []
        for fi, f in enumerate(faces):
            c, n = f["cycle_local"], f["n"]
            h = -(f["off"] + float(np.dot(n, centroid)))
            foot = h * n
            ref = np.mean(X[c], axis=0)
            vals = []
            for a, b in zip(c, c[1:] + c[:1]):
                e = X[b] - X[a]
                z = float(np.dot(np.cross(e, foot - X[a]), n) / max(np.linalg.norm(e) * radius, 1e-300))
                if np.dot(np.cross(e, ref - X[a]), n) < 0:
                    z = -z
                vals.append(z)
            dec = min(vals)
            fdec.append(dec)
            if dec > strict_tol:
                stable.append((fi, dec))

        vdec: dict[int, float] = {}
        unstable = []
        for i in active_local:
            vals = []
            for j in neighbors[i]:
                d = X[j] - X[i]
                vals.append(float(-np.dot(X[i], d) / max(np.linalg.norm(X[i]) * np.linalg.norm(d), 1e-300)))
            dec = min(vals)
            vdec[ids[i]] = dec
            if dec > strict_tol:
                unstable.append((ids[i], dec))

        edec: dict[tuple[int, int], float] = {}
        saddles = []
        edge_faces: dict[tuple[int, int], list[int]] = {}
        for (a, b), inc in ef_local.items():
            d = X[b] - X[a]
            dd = float(np.dot(d, d))
            t = float(-np.dot(X[a], d) / dd)
            p = X[a] + t * d
            n1, n2 = faces[inc[0]]["n"], faces[inc[1]]["n"]
            # Computing the two-normal Gram determinant as
            # ``1 - dot(n1, n2)**2`` is catastrophically unstable for the
            # intentionally shallow adjacent faces in this construction: a
            # perfectly resolvable angle with determinant around 1e-18 can
            # round to dot == 1 in binary64.  The algebraically identical
            # squared-cross-product formula retains the angle information.
            # Keep the solve in long double as well so the cutoff below is a
            # geometric test rather than a binary64 cancellation test.
            n1q = np.asarray(n1, dtype=np.longdouble)
            n2q = np.asarray(n2, dtype=np.longdouble)
            pq = np.asarray(p, dtype=np.longdouble)
            aa = np.dot(n1q, n1q)
            cc = np.dot(n2q, n2q)
            bb = np.dot(n1q, n2q)
            crossq = np.cross(n1q, n2q)
            den = np.dot(crossq, crossq)
            if den <= np.longdouble("1e-26"):
                raise ValueError("parallel face normals below 1e-26")
            r1, r2 = np.dot(pq, n1q), np.dot(pq, n2q)
            l1 = float((r1 * cc - r2 * bb) / den)
            l2 = float((r2 * aa - r1 * bb) / den)
            pn = max(float(np.linalg.norm(p)), 1e-300)
            dec = min(t, 1.0 - t, l1 / pn, l2 / pn)
            eids = tuple(sorted((ids[a], ids[b])))
            edec[eids] = dec
            edge_faces[eids] = inc
            if dec > strict_tol:
                saddles.append((eids, dec))

        edges = sorted(edec)
        nb_ids = {ids[i]: {ids[j] for j in js} for i, js in neighbors.items()}
        return Result(
            True,
            None,
            [ids[i] for i in active_local],
            faces,
            edges,
            edge_faces,
            centroid,
            volume,
            stable,
            unstable,
            saddles,
            fdec,
            vdec,
            edec,
            nb_ids,
            topology_margin,
            inactive_margin,
        )
    except Exception as exc:
        return Result(False, repr(exc), [], [], [], {}, np.full(3, np.nan), float("nan"), [], [], [], [], {}, {}, {}, float("-inf"), float("-inf"))


def summarize(r: Result) -> dict:
    return {
        "valid": r.valid,
        "error": r.error,
        "f_vector": [len(r.active), len(r.edges), len(r.faces)] if r.valid else None,
        "class": [len(r.stable), len(r.unstable), len(r.saddles)] if r.valid else None,
        "stable": [r.faces[i]["cycle"] for i, z in r.stable] if r.valid else [],
        "unstable": [i for i, z in r.unstable],
        "saddles": [list(e) for e, z in r.saddles],
        "centroid": r.centroid.tolist() if r.valid else None,
        "topology_margin": r.topology_margin,
        "inactive_margin": r.inactive_margin,
    }
