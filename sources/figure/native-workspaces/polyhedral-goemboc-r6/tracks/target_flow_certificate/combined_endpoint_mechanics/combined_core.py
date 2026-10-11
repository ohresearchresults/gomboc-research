#!/usr/bin/env python3
"""Reconstruct and evaluate the exact combined forced-edge M42 endpoint.

The two codimension-one mergers are imposed exactly:

* row 54 is inserted just beyond base edge (0,1), in the base plane;
* row 246 is projected to the plane through (7,8,245).

The resulting maximal-face lattice is (V,E,F)=(61,161,102).  A primal
tree rooted at vertex 8 and its complementary dual tree rooted at the
18-gonal base give 161 signed mechanical rows.  The target base, target
maximum, and global topology guard make the 164-row target ledger.

This module deliberately has no dependency on the lost worker-local tracks.
It rebuilds the hull, centroid, normal-cone signs, and tree/cotree ledger from
the surviving exact fifth-cell coordinates.
"""
from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction as Q
from functools import reduce
from pathlib import Path
import csv
import json
import math
import random

import numpy as np
from scipy.spatial import ConvexHull


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE = ROOT / "M42_acute_bridge_fifth_cell_complete" / "fifth_cell_endpoint" / "coordinates_all_exact.csv"
BASE = tuple(range(17)) + (54,)
QUAD = frozenset((7, 8, 245, 246))
TARGET_U = 8


def qadd(a, b):
    return tuple(a[k] + b[k] for k in range(3))


def qsub(a, b):
    return tuple(a[k] - b[k] for k in range(3))


def qmul(a, t):
    return tuple(a[k] * t for k in range(3))


def qdot(a, b):
    return sum((a[k] * b[k] for k in range(3)), Q(0))


def qcross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def primitive_plane(a, b, c, rows):
    n = qcross(qsub(b, a), qsub(c, a))
    h = qdot(n, a)
    vals = [qdot(n, p) - h for p in rows.values()]
    if any(z > 0 for z in vals):
        n = qmul(n, Q(-1))
        h = -h
        vals = [-z for z in vals]
    if any(z > 0 for z in vals):
        raise ValueError("triangle is not supporting")
    den = 1
    for z in (*n, h):
        den = den * z.denominator // math.gcd(den, z.denominator)
    ints = [int(z * den) for z in (*n, h)]
    g = reduce(math.gcd, (abs(z) for z in ints if z))
    return tuple(z // g for z in ints)


def read_exact_fork(epsilon=Q(1, 128)):
    rows = {}
    lineage = {}
    with SOURCE.open() as f:
        for r in csv.DictReader(f):
            if r["active"] != "1":
                continue
            i = int(r["source_id"])
            rows[i] = tuple(Q(r[k]) for k in ("x_exact", "y_exact", "z_exact"))
            lineage[i] = r["lineage"]

    # q54: a small exact outward displacement from the midpoint of base edge
    # (0,1), using the in-plane perpendicular component toward row 2.
    a, b, p = rows[0], rows[1], rows[2]
    d = qsub(b, a)
    line_foot = qadd(a, qmul(d, qdot(qsub(p, a), d) / qdot(d, d)))
    outward = qsub(line_foot, p)
    midpoint = qmul(qadd(a, b), Q(1, 2))
    rows[54] = qadd(midpoint, qmul(outward, epsilon))
    lineage[54] = "combined_base_merger_q54"

    # q246: exact orthogonal projection to plane(7,8,245).
    a, b, c, p = rows[7], rows[8], rows[245], rows[246]
    n = qcross(qsub(b, a), qsub(c, a))
    rows[246] = qsub(p, qmul(n, qdot(n, qsub(p, a)) / qdot(n, n)))
    lineage[246] = "combined_quad_merger_q246"
    return rows, lineage


def exact_faces(rows):
    ids = sorted(rows)
    xyz = np.asarray([[float(z) for z in rows[i]] for i in ids])
    hull = ConvexHull(xyz, qhull_options="Qt Qx")
    groups = defaultdict(set)
    planes = {}
    for simplex in hull.simplices:
        cyc = [ids[int(j)] for j in simplex]
        key = primitive_plane(*(rows[i] for i in cyc), rows)
        groups[key].update(cyc)
        planes[key] = key[:3]

    faces = []
    for key, vertices in groups.items():
        vv = sorted(vertices)
        pts = np.asarray([[float(z) for z in rows[i]] for i in vv])
        drop = int(np.argmax(np.abs(np.asarray(key[:3], dtype=float))))
        h2 = ConvexHull(np.delete(pts, drop, axis=1))
        cyc = [vv[int(j)] for j in h2.vertices]
        area = (Q(0), Q(0), Q(0))
        for u, v in zip(cyc, cyc[1:] + cyc[:1]):
            area = qadd(area, qcross(rows[u], rows[v]))
        if qdot(area, tuple(Q(z) for z in key[:3])) < 0:
            cyc = [cyc[0]] + list(reversed(cyc[1:]))
        faces.append(cyc)
    faces.sort(key=lambda c: (0 if set(c) == set(BASE) else 1, min(c), len(c), tuple(c)))

    incidence = defaultdict(list)
    for fi, cyc in enumerate(faces):
        for u, v in zip(cyc, cyc[1:] + cyc[:1]):
            incidence[tuple(sorted((u, v)))].append(fi)
    if not all(len(fs) == 2 for fs in incidence.values()):
        raise ValueError("nonmanifold reconstructed hull")
    active = set().union(*(set(c) for c in faces))
    if (len(active), len(incidence), len(faces)) != (61, 161, 102):
        raise ValueError(f"wrong fork f-vector {(len(active), len(incidence), len(faces))}")
    if set(active) != set(rows):
        raise ValueError("not every reconstructed row is active")
    if set(faces[0]) != set(BASE):
        raise ValueError("base merger missing")
    if not any(set(c) == set(QUAD) for c in faces):
        raise ValueError("quad merger missing")
    return faces, dict(incidence)


def rigid_base_chart(rows):
    """Put the base in z=0 by a rigid motion and normalize RMS radius."""
    p0 = np.asarray([float(z) for z in rows[0]])
    p1 = np.asarray([float(z) for z in rows[1]])
    p2 = np.asarray([float(z) for z in rows[2]])
    e1 = p1 - p0
    e1 /= np.linalg.norm(e1)
    e3 = np.cross(p1 - p0, p2 - p0)
    e3 /= np.linalg.norm(e3)
    mean = np.mean(np.asarray([[float(z) for z in p] for p in rows.values()]), axis=0)
    if np.dot(mean - p0, e3) < 0:
        e3 = -e3
    e2 = np.cross(e3, e1)
    basis = np.column_stack((e1, e2, e3))
    out = {i: (np.asarray([float(z) for z in p]) - p0) @ basis for i, p in rows.items()}
    for i in BASE:
        out[i][2] = 0.0
    cloud = np.asarray(list(out.values()))
    scale = math.sqrt(float(np.mean(np.sum((cloud - cloud.mean(axis=0)) ** 2, axis=1))))
    for i in out:
        out[i] = out[i] / scale
    return out, basis, p0, scale


@dataclass
class Chart:
    ids: tuple
    base: tuple
    free: tuple
    labels: tuple

    def pack(self, points):
        vals = []
        for i in self.base:
            vals.extend(points[i][:2])
        for i in self.free:
            vals.extend(points[i])
        a = points[7]
        M = np.column_stack((points[8] - a, points[245] - a))
        coeff, *_ = np.linalg.lstsq(M, points[246] - a, rcond=None)
        vals.extend(coeff)
        return np.asarray(vals, dtype=float)

    def unpack(self, x):
        x = np.asarray(x, dtype=float)
        out = {}
        k = 0
        for i in self.base:
            out[i] = np.asarray((x[k], x[k + 1], 0.0))
            k += 2
        for i in self.free:
            out[i] = np.asarray(x[k:k + 3])
            k += 3
        aa, bb = x[k:k + 2]
        out[246] = out[7] + aa * (out[8] - out[7]) + bb * (out[245] - out[7])
        k += 2
        if k != len(x):
            raise ValueError((k, len(x)))
        return out


def make_chart(points):
    ids = tuple(sorted(points))
    free = tuple(i for i in ids if i not in BASE and i != 246)
    labels = []
    for i in BASE:
        labels.extend((f"{i}.x", f"{i}.y"))
    for i in free:
        labels.extend((f"{i}.x", f"{i}.y", f"{i}.z"))
    labels.extend(("246.a", "246.b"))
    chart = Chart(ids, BASE, free, tuple(labels))
    if len(labels) != 164:
        raise ValueError(f"expected 164 chart coordinates, got {len(labels)}")
    return chart


def orient_faces_for_positive_volume(points, faces):
    d6 = 0.0
    for cyc in faces:
        a = points[cyc[0]]
        for j in range(1, len(cyc) - 1):
            d6 += float(np.dot(a, np.cross(points[cyc[j]], points[cyc[j + 1]])))
    if d6 < 0:
        return [[c[0]] + list(reversed(c[1:])) for c in faces]
    return [list(c) for c in faces]


def edge_face_component(X, cyc, edge):
    a0 = X[cyc[0]]
    n = None
    for j in range(1, len(cyc) - 1):
        z = np.cross(X[cyc[j]] - a0, X[cyc[j + 1]] - a0)
        if np.linalg.norm(z) > 1e-14:
            n = z
            break
    if n is None:
        return math.nan
    h = float(np.dot(n, a0))
    if h < 0:
        n = -n
        h = -h
    foot = n * (h / float(np.dot(n, n)))
    ref = np.mean(np.asarray([X[i] for i in cyc]), axis=0)
    u, v = edge
    if u not in cyc or v not in cyc:
        raise ValueError((cyc, edge))
    # Use the boundary orientation belonging to this face.
    found = None
    for a, b in zip(cyc, cyc[1:] + cyc[:1]):
        if {a, b} == {u, v}:
            found = (a, b)
            break
    if found is None:
        raise ValueError((cyc, edge))
    a, b = found
    e = X[b] - X[a]
    raw = float(np.dot(np.cross(e, foot - X[a]), n))
    side = float(np.dot(np.cross(e, ref - X[a]), n))
    if side < 0:
        raw = -raw
    return raw / (np.linalg.norm(e) * np.linalg.norm(n))


def mass_centroid(points, faces):
    d6 = 0.0
    mint = np.zeros(3)
    for cyc in faces:
        a = points[cyc[0]]
        for j in range(1, len(cyc) - 1):
            b, c = points[cyc[j]], points[cyc[j + 1]]
            d = float(np.dot(a, np.cross(b, c)))
            d6 += d
            mint += d * (a + b + c)
    if d6 <= 1e-14:
        raise ValueError(f"nonpositive volume determinant {d6}")
    return mint / (4.0 * d6), d6 / 6.0


def raw_geometry(points, faces, incidence):
    centroid, volume = mass_centroid(points, faces)
    X = {i: np.asarray(points[i]) - centroid for i in points}
    rms = math.sqrt(float(np.mean([np.dot(p, p) for p in X.values()])))
    X = {i: p / rms for i, p in X.items()}
    volume /= rms ** 3

    face_components = {}
    support_guards = []
    polygon_guards = []
    face_normals = []
    for fi, cyc in enumerate(faces):
        a0 = X[cyc[0]]
        n = None
        for j in range(1, len(cyc) - 1):
            z = np.cross(X[cyc[j]] - a0, X[cyc[j + 1]] - a0)
            if np.linalg.norm(z) > 1e-13:
                n = z
                break
        if n is None:
            raise ValueError(f"degenerate face {fi}")
        h = float(np.dot(n, a0))
        if h < 0:
            n = -n
            h = -h
        nn = np.linalg.norm(n)
        face_normals.append((n, h))
        cs = set(cyc)
        support_guards.extend((h - float(np.dot(n, X[i]))) / nn for i in X if i not in cs)
        ref = np.mean(np.asarray([X[i] for i in cyc]), axis=0)
        foot = n * (h / float(np.dot(n, n)))
        for u, v in zip(cyc, cyc[1:] + cyc[:1]):
            e = X[v] - X[u]
            en = np.linalg.norm(e)
            side = float(np.dot(np.cross(e, ref - X[u]), n))
            sign = 1.0 if side >= 0 else -1.0
            raw = sign * float(np.dot(np.cross(e, foot - X[u]), n))
            face_components[(fi, tuple(sorted((u, v))))] = raw / (en * nn)
            for w in cyc:
                if w in (u, v):
                    continue
                polygon_guards.append(sign * float(np.dot(np.cross(e, X[w] - X[u]), n)) / (en * nn))

    neighbors = defaultdict(set)
    for u, v in incidence:
        neighbors[u].add(v)
        neighbors[v].add(u)
    vertex_components = {}
    for u in X:
        ru = max(np.linalg.norm(X[u]), 1e-15)
        for v in neighbors[u]:
            d = X[v] - X[u]
            # Positive is the unstable-vertex support sign.
            vertex_components[(u, v)] = -float(np.dot(X[u], d)) / (ru * np.linalg.norm(d))
    return {
        "X": X,
        "centroid": centroid,
        "volume": volume,
        "rms": rms,
        "face_components": face_components,
        "vertex_components": vertex_components,
        "support_guards": np.asarray(support_guards),
        "polygon_guards": np.asarray(polygon_guards),
        "neighbors": {i: sorted(v) for i, v in neighbors.items()},
        "face_normals": face_normals,
    }


class DSU:
    def __init__(self, xs):
        self.p = {x: x for x in xs}

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        self.p[b] = a
        return True


def forced_rail_edges():
    short = [228] + list(range(229, 247)) + [8]
    long = [228] + list(range(247, 265)) + [8]
    edges = {tuple(sorted(e)) for p in (short, long) for e in zip(p, p[1:])}
    edges.remove((228, 229))
    return edges


def orient_tree(edges, root):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    parent = {root: None}
    q = deque([root])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in parent:
                parent[v] = u
                q.append(v)
    return parent


def dual_edge_map(incidence):
    return {e: tuple(fs) for e, fs in incidence.items()}


def tree_ledger(tree_edges, faces, incidence):
    parent_v = orient_tree(tree_edges, TARGET_U)
    if len(parent_v) != 61:
        raise ValueError("primal tree is disconnected")
    complement = set(incidence) - set(tree_edges)
    dual_edges = [(incidence[e][0], incidence[e][1], e) for e in complement]
    adj = defaultdict(list)
    for f, g, e in dual_edges:
        adj[f].append((g, e))
        adj[g].append((f, e))
    parent_f = {0: (None, None)}
    q = deque([0])
    while q:
        f = q.popleft()
        for g, e in adj[f]:
            if g not in parent_f:
                parent_f[g] = (f, e)
                q.append(g)
    if len(parent_f) != 102:
        raise ValueError("complement is not a dual tree")
    return parent_v, parent_f


def target_rows(geom, faces, parent_v, parent_f):
    rows = []
    labels = []
    vc = geom["vertex_components"]
    fc = geom["face_components"]
    for child in sorted(i for i in parent_v if i != TARGET_U):
        par = parent_v[child]
        rows.append(-vc[(child, par)])
        labels.append(f"V{child}->{par}")
    for child in sorted(i for i in parent_f if i != 0):
        par, edge = parent_f[child]
        rows.append(-fc[(child, edge)])
        labels.append(f"F{child}->{par}@E{edge[0]}_{edge[1]}")
    root_face = [fc[(0, tuple(sorted((u, v))))] for u, v in zip(faces[0], faces[0][1:] + faces[0][:1])]
    root_vertex = [vc[(TARGET_U, v)] for v in geom["neighbors"][TARGET_U]]
    topology = np.concatenate((geom["support_guards"], geom["polygon_guards"]))
    rows.extend((min(root_face), min(root_vertex), float(np.min(topology))))
    labels.extend(("TARGET_BASE_STABLE", "TARGET_U8_UNSTABLE", "TOPOLOGY_MIN"))
    if len(rows) != 164:
        raise ValueError(len(rows))
    return np.asarray(rows), labels


def choose_tree(points, faces, incidence, trials=5000, seed=831500):
    geom = raw_geometry(points, faces, incidence)
    forced = forced_rail_edges()
    if not forced <= set(incidence):
        raise ValueError(f"missing forced rail edges {sorted(forced - set(incidence))}")
    d0 = DSU(points)
    for e in forced:
        if not d0.union(*e):
            raise ValueError("forced rail edges contain a cycle")

    vc, fc = geom["vertex_components"], geom["face_components"]
    base_key = {}
    for e, fs in incidence.items():
        u, v = e
        primal = max(-vc[(u, v)], -vc[(v, u)])
        dual = max(-fc[(fs[0], e)], -fc[(fs[1], e)])
        base_key[e] = primal - dual

    rng = random.Random(seed)
    best = None
    candidates = [0.0, 0.02, 0.05, 0.10, 0.20, 0.40, 0.80, 1.50]
    for trial in range(trials):
        sigma = candidates[trial % len(candidates)]
        order = sorted(
            (e for e in incidence if e not in forced),
            key=lambda e: base_key[e] + rng.gauss(0.0, sigma),
            reverse=True,
        )
        dsu = DSU(points)
        tree = set()
        for e in forced:
            dsu.union(*e)
            tree.add(e)
        for e in order:
            if dsu.union(*e):
                tree.add(e)
                if len(tree) == len(points) - 1:
                    break
        try:
            pv, pf = tree_ledger(tree, faces, incidence)
        except ValueError:
            continue
        vals, labels = target_rows(geom, faces, pv, pf)
        mech = vals[:-3]
        key = (
            int(np.sum(vals > 0)),
            int(np.sum(mech > 0)),
            float(np.quantile(vals, 0.05)),
            float(np.min(vals)),
            float(np.mean(np.minimum(vals, 0.0))),
        )
        if best is None or key > best[0]:
            best = (key, tree, pv, pf, vals, labels)
    if best is None:
        raise RuntimeError("no tree/cotree ledger found")
    return best


def evaluate_chart(x, chart, faces, incidence, parent_v, parent_f):
    points = chart.unpack(x)
    geom = raw_geometry(points, faces, incidence)
    vals, labels = target_rows(geom, faces, parent_v, parent_f)
    guards = np.concatenate((geom["support_guards"], geom["polygon_guards"]))
    return vals, guards, geom, labels


def class_counts(geom, faces, incidence):
    stable = []
    for fi, cyc in enumerate(faces):
        vals = [geom["face_components"][(fi, tuple(sorted((u, v))))] for u, v in zip(cyc, cyc[1:] + cyc[:1])]
        if min(vals) > 0:
            stable.append(fi)
    unstable = []
    for i, ns in geom["neighbors"].items():
        if min(geom["vertex_components"][(i, j)] for j in ns) > 0:
            unstable.append(i)
    saddles = []
    X = geom["X"]
    for e, fs in incidence.items():
        i, j = e
        d = X[j] - X[i]
        t = -float(np.dot(X[i], d)) / float(np.dot(d, d))
        p = X[i] + t * d
        n1, _ = geom["face_normals"][fs[0]]
        n2, _ = geom["face_normals"][fs[1]]
        aa, bb, cc = float(np.dot(n1, n1)), float(np.dot(n1, n2)), float(np.dot(n2, n2))
        r1, r2 = float(np.dot(p, n1)), float(np.dot(p, n2))
        den = aa * cc - bb * bb
        b1 = (r1 * cc - r2 * bb) / den
        b2 = (r2 * aa - r1 * bb) / den
        if min(t, 1.0 - t, b1, b2) > 0:
            saddles.append(e)
    return stable, unstable, saddles


def rebuild_hull(points, expected_faces):
    ids = sorted(points)
    xyz = np.asarray([points[i] for i in ids])
    hull = ConvexHull(xyz, qhull_options="Qt Qx")
    # Group float facets by which expected supporting plane contains them.  This
    # is only a verifier; fixed-chart support margins are the primary predicate.
    actual = []
    for cyc in expected_faces:
        a = points[cyc[0]]
        n = None
        for j in range(1, len(cyc) - 1):
            z = np.cross(points[cyc[j]] - a, points[cyc[j + 1]] - a)
            if np.linalg.norm(z) > 1e-12:
                n = z
                break
        h = float(np.dot(n, a))
        vals = np.asarray([float(np.dot(n, points[i]) - h) for i in ids])
        if np.max(vals) > -np.min(vals):
            vals = -vals
        actual.append(float(np.max(vals[[i not in set(cyc) for i in ids]])))
    return {
        "qhull_vertices": len(hull.vertices),
        "qhull_simplices": len(hull.simplices),
        "expected_faces": len(expected_faces),
        "maximum_expected_support_violation": max(actual),
    }


def save_reconstruction(trials=5000, seed=831500):
    rows, lineage = read_exact_fork()
    faces, incidence = exact_faces(rows)
    points, basis, origin, scale = rigid_base_chart(rows)
    faces = orient_faces_for_positive_volume(points, faces)
    chart = make_chart(points)
    x0 = chart.pack(points)
    best = choose_tree(points, faces, incidence, trials=trials, seed=seed)
    key, tree, pv, pf, vals, labels = best
    geom = raw_geometry(points, faces, incidence)
    stable, unstable, saddles = class_counts(geom, faces, incidence)

    with (HERE / "combined_endpoint_exact.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(("source_id", "x_exact", "y_exact", "z_exact", "lineage"))
        for i in sorted(rows):
            w.writerow((i, *(str(z) for z in rows[i]), lineage[i]))
    np.save(HERE / "combined_start_chart.npy", x0)
    payload = {
        "verdict": "RECONSTRUCTED_EXACT_COMBINED_ENDPOINT",
        "f_vector": [61, 161, 102],
        "base_face": list(faces[0]),
        "quad_face": next(c for c in faces if set(c) == set(QUAD)),
        "faces": faces,
        "edges": [[*e, *incidence[e]] for e in sorted(incidence)],
        "chart_dimension": len(x0),
        "chart_labels": list(chart.labels),
        "tree_edges": [list(e) for e in sorted(tree)],
        "forced_rail_edges": [list(e) for e in sorted(forced_rail_edges())],
        "omitted_full_cycle_edge": [228, 229],
        "vertex_parent": {str(k): v for k, v in pv.items() if v is not None},
        "face_parent": {str(k): {"face": v[0], "edge": list(v[1])} for k, v in pf.items() if v[0] is not None},
        "ledger_rows": len(vals),
        "ledger_labels": labels,
        "ledger_values": vals.tolist(),
        "ledger_positive": int(np.sum(vals > 0)),
        "ledger_hard_min": float(np.min(vals)),
        "topology_guard_min": float(min(np.min(geom["support_guards"]), np.min(geom["polygon_guards"]))),
        "raw_class": [len(stable), len(unstable), len(saddles)],
        "raw_stable_faces": [{"face": i, "cycle": faces[i]} for i in stable],
        "raw_unstable_vertices": unstable,
        "raw_saddle_edges": [list(e) for e in saddles],
        "tree_search_key": list(key),
        "rigid_chart": {"origin": origin.tolist(), "basis": basis.tolist(), "scale": scale},
        "fork_q54": [str(z) for z in rows[54]],
        "fork_q246": [str(z) for z in rows[246]],
    }
    (HERE / "combined_reconstruction.json").write_text(json.dumps(payload, indent=2))
    print(json.dumps({k: payload[k] for k in ("f_vector", "chart_dimension", "ledger_positive", "ledger_hard_min", "topology_guard_min", "raw_class")}, indent=2))
    return payload


def load_problem():
    rows, _ = read_exact_fork()
    faces, incidence = exact_faces(rows)
    points, *_ = rigid_base_chart(rows)
    faces = orient_faces_for_positive_volume(points, faces)
    chart = make_chart(points)
    data = json.loads((HERE / "combined_reconstruction.json").read_text())
    tree = {tuple(e) for e in data["tree_edges"]}
    pv, pf = tree_ledger(tree, faces, incidence)
    x0 = np.load(HERE / "combined_start_chart.npy")
    return chart, faces, incidence, pv, pf, x0


if __name__ == "__main__":
    save_reconstruction()
