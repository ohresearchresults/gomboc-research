#!/usr/bin/env python3
"""Rebuild and search the row-54 enlarged-base / row-246 far-side cell.

The script is deliberately self-contained.  It starts from the exact common-
lattice fifth-cell rows, performs two rational constructions (the 246
boundary flip and an exterior point 54 in the old base plane), extracts the
actual maximal-face lattice once, and then searches the eight-dimensional
projective + trace-free SPD metric family.  Every reported candidate is
re-audited after rebuilding its convex hull and its own volume centroid.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import numpy as np
from scipy.linalg import expm
from scipy.optimize import differential_evolution, minimize
from scipy.spatial import ConvexHull

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
INPUT = ROOT / "M42_acute_bridge_fifth_cell_work/fifth_cell_endpoint/input_rows_common_lattice.csv"

BASE_ORIGINAL = frozenset(range(17))
BASE = BASE_ORIGINAL | {54}
F0 = frozenset((8, 245, 246))
SFAR = frozenset((7, 8, 246))
TARGET_U = {8, 54}
TARGET_H = {(6, 7), (9, 10)}


def read_rows() -> Tuple[List[int], np.ndarray]:
    rows = {}
    with INPUT.open() as f:
        for r in csv.DictReader(f):
            den = float(r["denominator"])
            rows[int(r["source_id"])] = np.array(
                [float(r[k]) / den for k in ("x_int", "y_int", "z_int")], dtype=float
            )
    ids = sorted(rows)
    return ids, np.array([rows[i] for i in ids])


def projection_to_plane(q: np.ndarray, a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    n = np.cross(b - a, c - a)
    return q - n * (np.dot(n, q - a) / np.dot(n, n))


def build_wall_rows(ids: Sequence[int], raw: np.ndarray, depth: float, exterior: float,
                    edge_fraction: float = 0.5) -> np.ndarray:
    """Far-side row 246 and small exterior row 54 exactly in the old base plane."""
    ix = {i: k for k, i in enumerate(ids)}
    p = raw.copy()
    w246 = projection_to_plane(raw[ix[246]], raw[ix[7]], raw[ix[8]], raw[ix[245]])
    p[ix[246]] = w246 + depth * (w246 - raw[ix[246]])
    w54 = projection_to_plane(raw[ix[54]], raw[ix[0]], raw[ix[1]], raw[ix[2]])
    edge = raw[ix[1]] - raw[ix[0]]
    line_parameter = float(np.dot(w54 - raw[ix[0]], edge) / np.dot(edge, edge))
    line_foot = raw[ix[0]] + line_parameter * edge
    outward = w54 - line_foot
    # In the original fifth-cell realization row 54 projects outside edge
    # 01; in a Tutte cap it projects inside.  Orient the in-plane transverse
    # vector geometrically, away from the base interior (witness row 2), so
    # the same constructor works for both realizations.
    if np.dot(outward, raw[ix[2]] - line_foot) > 0:
        outward = -outward
    edge_point = (1.0 - edge_fraction) * raw[ix[0]] + edge_fraction * raw[ix[1]]
    p[ix[54]] = edge_point + exterior * outward
    return p


def build_rebuilt_combined_rows(ids: Sequence[int], raw: np.ndarray, far_depth: float,
                                tangent_a: float, tangent_b: float, exterior: float,
                                edge_fraction: float) -> np.ndarray:
    """A support-valid far-side flip in the reconstructed Tutte realization."""
    ix = {i: k for k, i in enumerate(ids)}
    p = build_wall_rows(ids, raw, 0.0, exterior, edge_fraction)
    a = raw[ix[7]]
    n = np.cross(raw[ix[8]] - a, raw[ix[245]] - a)
    n = n / np.linalg.norm(n)
    signed_depth = float(np.dot(n, raw[ix[246]] - a))
    wall = raw[ix[246]] - n * signed_depth
    u = raw[ix[8]] - a
    u = u / np.linalg.norm(u)
    v = np.cross(n, u)
    p[ix[246]] = (wall - np.sign(signed_depth) * far_depth * n
                  + tangent_a * u + tangent_b * v)
    return p


def group_maximal_faces(ids: Sequence[int], p: np.ndarray, tol: float = 1e-10):
    """Group Qhull triangles into maximal faces through coplanar adjacency.

    Comparing every plane with every other plane can accidentally merge two
    disjoint, almost-parallel faces after a strongly anisotropic metric map.
    A true triangulation diagonal is local: its two triangles share an edge.
    Therefore union only adjacent triangles whose normalized equations agree.
    This also makes a fresh audit materially stricter than the old global
    3e-8 equation bucket.
    """
    hull = ConvexHull(p, qhull_options="Qt Qx")
    equations = np.asarray([
        eq0 / np.linalg.norm(eq0[:3]) for eq0 in hull.equations
    ])
    parent = list(range(len(hull.simplices)))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a

    edge_facets: Dict[Tuple[int, int], List[int]] = {}
    for k, tri in enumerate(hull.simplices):
        for a, b in ((tri[0], tri[1]), (tri[1], tri[2]), (tri[2], tri[0])):
            edge_facets.setdefault(tuple(sorted((int(a), int(b)))), []).append(k)
    for inc in edge_facets.values():
        if len(inc) == 2:
            a, b = inc
            if np.max(np.abs(equations[a] - equations[b])) < tol:
                union(a, b)

    by_root: Dict[int, dict] = {}
    for k, tri in enumerate(hull.simplices):
        root = find(k)
        group = by_root.setdefault(root, {"eq": equations[k], "verts": set()})
        group["verts"].update(ids[int(j)] for j in tri)
    groups = list(by_root.values())
    ix = {i: k for k, i in enumerate(ids)}
    faces, normals = [], []
    for g in groups:
        vs = sorted(g["verts"])
        n = g["eq"][:3].copy()
        pts = np.array([p[ix[i]] for i in vs])
        cen = pts.mean(axis=0)
        radial = pts - cen
        j = int(np.argmax(np.linalg.norm(radial, axis=1)))
        u = radial[j] / np.linalg.norm(radial[j])
        v = np.cross(n, u)
        angles = np.arctan2(radial @ v, radial @ u)
        cyc = [vs[j] for j in np.argsort(angles)]
        area = sum(
            (np.cross(p[ix[a]], p[ix[b]]) for a, b in zip(cyc, cyc[1:] + cyc[:1])),
            np.zeros(3),
        )
        if np.dot(area, n) < 0:
            cyc = [cyc[0]] + list(reversed(cyc[1:]))
        faces.append(cyc)
        normals.append(n)
    order = sorted(range(len(faces)), key=lambda k: (len(faces[k]), tuple(sorted(faces[k]))))
    faces = [faces[k] for k in order]
    normals = [normals[k] for k in order]
    return hull, faces, normals


def edge_lattice(faces: Sequence[Sequence[int]]):
    ef: Dict[Tuple[int, int], List[int]] = {}
    nbr: Dict[int, set] = {}
    for fi, cyc in enumerate(faces):
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            e = tuple(sorted((a, b)))
            ef.setdefault(e, []).append(fi)
            nbr.setdefault(a, set()).add(b)
            nbr.setdefault(b, set()).add(a)
    if not all(len(v) == 2 for v in ef.values()):
        raise ValueError("nonmanifold maximal-face edge lattice")
    return ef, nbr


def own_centroid(ids: Sequence[int], p: np.ndarray, faces: Sequence[Sequence[int]]) -> np.ndarray:
    ix = {i: k for k, i in enumerate(ids)}
    d6 = 0.0
    mint = np.zeros(3)
    for cyc in faces:
        for j in range(1, len(cyc) - 1):
            a, b, c = (p[ix[i]] for i in (cyc[0], cyc[j], cyc[j + 1]))
            d = float(np.dot(a, np.cross(b, c)))
            d6 += d
            mint += d * (a + b + c)
    if d6 < 0:
        d6 = -d6
        mint = -mint
    if not d6 > 1e-14:
        raise ValueError("degenerate oriented volume")
    return mint / (4.0 * d6)


def face_normals(ids: Sequence[int], p: np.ndarray, faces: Sequence[Sequence[int]]) -> List[np.ndarray]:
    ix = {i: k for k, i in enumerate(ids)}
    out = []
    for cyc in faces:
        a = p[ix[cyc[0]]]
        n = None
        for j in range(1, len(cyc) - 1):
            z = np.cross(p[ix[cyc[j]]] - a, p[ix[cyc[j + 1]]] - a)
            if np.linalg.norm(z) > 1e-20:
                n = z
                break
        if n is None:
            raise ValueError("flat face")
        area = sum(
            (np.cross(p[ix[u]], p[ix[v]]) for u, v in zip(cyc, cyc[1:] + cyc[:1])),
            np.zeros(3),
        )
        if np.dot(area, n) < 0:
            n = -n
        out.append(n)
    return out


def mechanics(ids: Sequence[int], p: np.ndarray, faces: Sequence[Sequence[int]]):
    ix = {i: k for k, i in enumerate(ids)}
    ef, nbr = edge_lattice(faces)
    active = sorted(set().union(*(set(c) for c in faces)))
    c0 = own_centroid(ids, p, faces)
    x = {i: p[ix[i]] - c0 for i in active}
    norms = face_normals(ids, p, faces)
    fdec = []
    fcomponents = []
    for cyc, n in zip(faces, norms):
        h = float(np.dot(n, x[cyc[0]]))
        foot = n * h / float(np.dot(n, n))
        ref = np.mean([x[i] for i in cyc], axis=0)
        vals = []
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            e = x[b] - x[a]
            z = float(np.dot(np.cross(e, foot - x[a]), n))
            if np.dot(np.cross(e, ref - x[a]), n) < 0:
                z = -z
            vals.append(z / (np.linalg.norm(e) * np.linalg.norm(n)))
        fcomponents.append(vals)
        fdec.append(min(vals))
    udec, ucomponents = {}, {}
    for i in active:
        vals = [
            -float(np.dot(x[i], x[j] - x[i])) / (np.linalg.norm(x[i]) * np.linalg.norm(x[j] - x[i]))
            for j in nbr[i]
        ]
        ucomponents[i] = vals
        udec[i] = min(vals)
    edec, ecomponents = {}, {}
    for e, inc in ef.items():
        i, j = e
        d = x[j] - x[i]
        t = -float(np.dot(x[i], d)) / float(np.dot(d, d))
        q = x[i] + t * d
        n1, n2 = norms[inc[0]], norms[inc[1]]
        aa, bb, cc = float(n1 @ n1), float(n1 @ n2), float(n2 @ n2)
        # The Gram determinant aa*cc-bb^2 catastrophically cancels when an
        # anisotropic projective/metric map makes a perfectly valid dihedral
        # angle tiny.  The identical cross-product form retains the small
        # angle, and the vector triple products give the two dual normals
        # without subtracting two O(aa*cc) scalars.
        cross12 = np.cross(n1, n2)
        den = float(cross12 @ cross12)
        if den <= 1e-300 * aa * cc:
            raise ValueError("parallel incident face normals")
        b1 = float(q @ np.cross(n2, cross12)) / den
        b2 = float(q @ np.cross(cross12, n1)) / den
        qn = max(float(q @ q), 1e-300)
        vals = [t, 1.0 - t, b1 * math.sqrt(aa / qn), b2 * math.sqrt(cc / qn)]
        ecomponents[e] = vals
        edec[e] = min(vals)
    return {
        "centroid": c0,
        "active": active,
        "ef": ef,
        "fdec": np.array(fdec),
        "fcomponents": fcomponents,
        "udec": udec,
        "ucomponents": ucomponents,
        "edec": edec,
        "ecomponents": ecomponents,
    }


def transform(p0: np.ndarray, theta: np.ndarray):
    origin = p0.mean(axis=0)
    scale = float(np.sqrt(np.mean(np.sum((p0 - origin) ** 2, axis=1))))
    z = (p0 - origin) / scale
    pole = theta[:3]
    den = 1.0 + z @ pole
    if np.min(den) <= 0.08:
        return None, den
    a, b, c, d, e = theta[3:]
    h = np.array([[a, b, c], [b, d, e], [c, e, -a - d]], dtype=float)
    l = expm(h)
    return (z / den[:, None]) @ l.T, den


def classify(ids, p, faces):
    m = mechanics(ids, p, faces)
    stable = [list(faces[k]) for k, z in enumerate(m["fdec"]) if z > 0]
    unstable = [i for i, z in m["udec"].items() if z > 0]
    saddles = [list(e) for e, z in m["edec"].items() if z > 0]
    return m, stable, unstable, saddles


def signed_guards(m, faces, mode: str):
    """Return one signed guard per feature; positive means requested sign."""
    vals, labels = [], []
    if mode == "seed":
        sf = {BASE, SFAR}
        uu = TARGET_U
        hh = TARGET_H
    elif mode == "row54":
        sf = {BASE, F0}
        uu = TARGET_U
        hh = TARGET_H
    elif mode == "robust":
        sf = {BASE_ORIGINAL, F0}
        uu = {1, 8}
        hh = TARGET_H
    elif mode == "escape":
        sf = {BASE}
        uu = {8}
        hh = set()
    else:
        raise ValueError(mode)
    for k, cyc in enumerate(faces):
        positive = frozenset(cyc) in sf
        vals.append(float(m["fdec"][k]) if positive else -float(m["fdec"][k]))
        labels.append(("S+" if positive else "S-", list(cyc)))
    for i, z in m["udec"].items():
        positive = i in uu
        vals.append(float(z) if positive else -float(z))
        labels.append(("U+" if positive else "U-", i))
    for e, z in m["edec"].items():
        positive = e in hh
        vals.append(float(z) if positive else -float(z))
        labels.append(("H+" if positive else "H-", list(e)))
    return np.asarray(vals), labels


class Search:
    def __init__(self, ids, p0, faces, mode, escape_objective="packet"):
        self.ids, self.p0, self.faces, self.mode = ids, p0, faces, mode
        self.escape_objective = escape_objective
        self.calls = 0
        self.best = (-1e100, -1e100, None, None)
        self.best_hard = (-1e100, None, None)
        p_identity, _ = transform(self.p0, np.zeros(8))
        m_identity = mechanics(self.ids, p_identity, self.faces)
        g_identity, labels_identity = signed_guards(m_identity, self.faces, self.mode)
        self.guard_scales = np.maximum(0.03, np.abs(g_identity))
        # In the far source these are exactly S[7,8,246], U54, H67,
        # H9,10.  After a successful multiwall move the same four defects can
        # transfer to a compensating packet.  Identify the active packet from
        # the actual source signs so a continuation search attacks the new
        # walls rather than continuing to over-reward already-fixed old ones.
        self.escape_critical = np.asarray(g_identity < 0.0, dtype=bool)
        if self.mode == "escape" and int(np.sum(self.escape_critical)) != 4:
            raise ValueError("failed to identify the four row54 escape residuals")

    def evaluate(self, theta, report=False):
        self.calls += 1
        p, den = transform(self.p0, np.asarray(theta))
        if p is None:
            return 1000.0 + 100.0 * max(0.0, 0.08 - float(np.min(den)))
        try:
            m = mechanics(self.ids, p, self.faces)
            guards, labels = signed_guards(m, self.faces, self.mode)
        except Exception:
            return 1000.0
        hard = float(np.min(guards))
        # Raw beta guards can be hundreds of units while vertex guards are
        # bounded by one.  A raw minimax therefore spends the entire search
        # merely rescaling a single negative beta.  This monotone bounded map
        # preserves every zero/sign and makes the score a balanced sign-cell
        # objective.  The untransformed hard margin remains the acceptance
        # gate and is what is written to the certificate.
        balanced = guards / (self.guard_scales + np.abs(guards))
        plus = np.asarray([balanced[k] for k, lab in enumerate(labels) if str(lab[0]).endswith("+")])
        minus = np.asarray([balanced[k] for k, lab in enumerate(labels) if str(lab[0]).endswith("-")])
        # The positive features are only a few rows among more than three
        # hundred exclusions.  Weight their bottleneck explicitly or the
        # identity cell (which gets almost every exclusion right) becomes a
        # false global attractor.  In escape mode the four known residuals
        # S[7,8,246], U54, H67, H9,10 are a separate minimax packet; otherwise
        # their four votes are drowned by the already-correct exclusions.
        if self.mode == "escape":
            if self.escape_objective == "rawmin":
                ordered_raw = np.sort(guards)
                worst_raw = ordered_raw[:min(12, len(ordered_raw))]
                score = (
                    0.94 * float(ordered_raw[0])
                    + 0.06 * float(np.mean(worst_raw))
                )
            elif self.escape_objective == "minimax":
                ordered = np.sort(balanced)
                worst = ordered[:min(12, len(ordered))]
                score = (
                    0.90 * float(ordered[0])
                    + 0.08 * float(np.mean(worst))
                    + 0.015 * float(np.min(plus))
                    + 0.005 * float(np.mean(plus))
                )
            else:
                critical = balanced[self.escape_critical]
                ordinary = np.asarray([
                    balanced[k] for k, lab in enumerate(labels)
                    if str(lab[0]).endswith("-") and not self.escape_critical[k]
                ])
                score = (
                    0.32 * float(np.min(plus)) + 0.08 * float(np.mean(plus))
                    + 0.40 * float(np.min(critical)) + 0.10 * float(np.mean(critical))
                    + 0.07 * float(np.min(ordinary)) + 0.03 * float(np.mean(ordinary))
                )
        else:
            score = (0.58 * float(np.min(plus)) + 0.22 * float(np.mean(plus))
                     + 0.15 * float(np.min(minus)) + 0.05 * float(np.mean(minus)))
        worst = sorted(zip(guards.tolist(), labels), key=lambda z: z[0])[:12]
        if hard > self.best_hard[0]:
            self.best_hard = (hard, np.asarray(theta).copy(), worst)
        if score > self.best[0]:
            self.best = (score, hard, np.asarray(theta).copy(), worst)
            if report:
                print("best", self.calls, "hard", hard, "balanced", score, "worst", worst[:5], flush=True)
        return -score


def fresh_audit(ids, p, expected_faces):
    hull, faces, _ = group_maximal_faces(ids, p)
    m, stable, unstable, saddles = classify(ids, p, faces)
    return {
        "f_vector": [len(hull.vertices), len(m["ef"]), len(faces)],
        "faces_match_fixed_cell": {frozenset(c) for c in faces} == {frozenset(c) for c in expected_faces},
        "active": m["active"],
        "centroid": m["centroid"].tolist(),
        "class": [len(stable), len(unstable), len(saddles)],
        "stable_faces": stable,
        "unstable_vertices": unstable,
        "saddle_edges": saddles,
    }, faces, m


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=("robust", "seed", "row54", "escape"), default="seed")
    ap.add_argument(
        "--source",
        choices=("bundle", "rebuilt-target", "rebuilt-combined", "row54-far"),
        default="bundle",
    )
    ap.add_argument(
        "--source-csv",
        help="override the named source with a source_id,x,y,z CSV in the current track",
    )
    ap.add_argument("--seed", type=int, default=831501)
    ap.add_argument("--generations", type=int, default=300)
    ap.add_argument("--popsize", type=int, default=14)
    ap.add_argument("--depth", type=float, default=1.5)
    ap.add_argument("--exterior", type=float, default=1e-4)
    ap.add_argument("--edge-fraction", type=float, default=0.5)
    ap.add_argument("--far-depth", type=float, default=1e-5)
    ap.add_argument("--tangent-a", type=float, default=-0.11911849736323583)
    ap.add_argument("--tangent-b", type=float, default=-0.10923192527775075)
    ap.add_argument("--start-json")
    ap.add_argument(
        "--escape-objective",
        choices=("packet", "minimax", "rawmin"),
        default="packet",
    )
    ap.add_argument("--local-iters", type=int, default=1500)
    ap.add_argument("--output", default="row54_four_residual_search.json")
    args = ap.parse_args()

    if args.source_csv:
        source_path = Path(args.source_csv)
        if not source_path.is_absolute():
            source_path = HERE / source_path
        rows = {}
        with source_path.open() as f:
            for r in csv.DictReader(f):
                rows[int(r["source_id"])] = np.array(
                    [float(r[k]) for k in ("x", "y", "z")]
                )
        ids = sorted(rows)
        p0 = np.array([rows[i] for i in ids])
    elif args.source == "bundle":
        ids, raw = read_rows()
        p0 = build_wall_rows(ids, raw, args.depth, args.exterior, args.edge_fraction)
    elif args.source == "row54-far":
        rows = {}
        with (HERE / "row54_far_rebuilt.csv").open() as f:
            for r in csv.DictReader(f):
                rows[int(r["source_id"])] = np.array(
                    [float(r[k]) for k in ("x", "y", "z")]
                )
        ids = sorted(rows)
        p0 = np.array([rows[i] for i in ids])
    else:
        rows = {}
        with (HERE / "target_sphere_rebuilt.csv").open() as f:
            for r in csv.DictReader(f):
                rows[int(r["source_id"])] = np.array([float(r[k]) for k in ("x", "y", "z")])
        ids = sorted(rows)
        raw = np.array([rows[i] for i in ids])
        if args.source == "rebuilt-combined":
            p0 = build_rebuilt_combined_rows(ids, raw, args.far_depth, args.tangent_a,
                                             args.tangent_b, args.exterior, args.edge_fraction)
        else:
            p0 = raw
    hull0, faces0, _ = group_maximal_faces(ids, p0)
    ef0, _ = edge_lattice(faces0)
    wanted_base = BASE_ORIGINAL if args.source == "rebuilt-target" and not args.source_csv else BASE
    base = [c for c in faces0 if frozenset(c) == wanted_base]
    assert len(base) == 1, base
    if args.source_csv or args.source in ("bundle", "rebuilt-combined", "row54-far"):
        assert (0, 1) not in ef0 and (0, 54) in ef0 and (1, 54) in ef0
    print("cell", len(hull0.vertices), len(ef0), len(faces0), "base", base[0], flush=True)

    search = Search(ids, p0, faces0, args.mode, args.escape_objective)
    x0 = np.zeros(8)
    if args.start_json:
        old = json.load(open(args.start_json))
        x0 = np.asarray(old["theta"], dtype=float)
        search.evaluate(x0, report=True)
    bounds = [(-0.7, 0.7)] * 3 + [(-1.4, 1.4)] * 5
    result = differential_evolution(
        lambda x: search.evaluate(x, report=True),
        bounds,
        seed=args.seed,
        maxiter=args.generations,
        popsize=args.popsize,
        tol=1e-9,
        polish=False,
        updating="immediate",
        workers=1,
        x0=x0,
    )
    xb = search.best[2] if search.best[2] is not None else result.x
    # Local nonsmooth cleanup.
    local = None
    if args.local_iters > 0:
        local = minimize(lambda x: search.evaluate(x, report=True), xb, method="Nelder-Mead",
                         options={"maxiter": args.local_iters, "xatol": 1e-11, "fatol": 1e-11})
    if search.best[2] is not None:
        xb = search.best[2]
    p, den = transform(p0, xb)
    fixed_m, fixed_stable, fixed_unstable, fixed_saddles = classify(ids, p, faces0)
    guards, labels = signed_guards(fixed_m, faces0, args.mode)
    audit, fresh_faces, fresh_m = fresh_audit(ids, p, faces0)
    record = {
        "version": 1,
        "source": args.source_csv if args.source_csv else args.source,
        "mode": args.mode,
        "escape_objective": args.escape_objective,
        "seed": args.seed,
        "depth": args.depth,
        "exterior": args.exterior,
        "edge_fraction": args.edge_fraction,
        "theta": xb.tolist(),
        "minimum_projective_denominator": float(np.min(den)),
        "fixed_cell_f_vector": [len(hull0.vertices), len(ef0), len(faces0)],
        "fixed_cell_class": [len(fixed_stable), len(fixed_unstable), len(fixed_saddles)],
        "fixed_cell_stable_faces": fixed_stable,
        "fixed_cell_unstable_vertices": fixed_unstable,
        "fixed_cell_saddle_edges": fixed_saddles,
        "requested_hard_margin": float(np.min(guards)),
        "worst_requested_guards": [
            {"value": float(v), "feature": lab} for v, lab in sorted(zip(guards, labels), key=lambda z: z[0])[:24]
        ],
        "fresh_hull_audit": audit,
        "calls": search.calls,
        "optimizer_message": str(result.message),
        "local_optimizer_message": None if local is None else str(local.message),
    }
    out = HERE / args.output
    json.dump(record, out.open("w"), indent=2)
    print(json.dumps(record, indent=2), flush=True)


if __name__ == "__main__":
    main()
