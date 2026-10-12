#!/usr/bin/env python3
"""Recover the lost far-side projective/metric seed from its mechanical signature.

The source is reconstructed exactly from the accepted fifth endpoint by moving
row 246 orthogonally through plane (7,8,245) with depth 3/2.  The ensuing
surface flip is (7,8,245),(8,245,246) -> (7,8,246),(7,245,246).

Within this fixed incidence sphere we search the 8-dimensional family

    x |-> exp(S) x / (1 + ell.x),

where S is symmetric traceless.  Translation and overall scale are immaterial
after recomputing the volume centroid.  The target signature is the robust
far-side (2,2,2) state recorded in the run log:

  stable: base [0..16], [7,8,246]
  unstable: 1, 8
  saddles: (6,7), (9,10).
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
from scipy.linalg import expm
from scipy.optimize import differential_evolution, minimize
from scipy.special import logsumexp

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[2]
SOURCE = PROJECT / "M42_acute_bridge_fifth_cell_complete" / "fifth_cell_endpoint"


def load_exact_rows() -> dict[int, tuple[Q, Q, Q]]:
    out = {}
    with open(SOURCE / "coordinates_all_exact.csv", newline="") as f:
        for r in csv.DictReader(f):
            if int(r["active"]):
                out[int(r["source_id"])] = tuple(Q(r[k]) for k in ("x_exact", "y_exact", "z_exact"))
    assert len(out) == 61
    return out


def exact_far_side(rows: dict[int, tuple[Q, Q, Q]]) -> dict[int, tuple[Q, Q, Q]]:
    def sub(a, b):
        return tuple(a[k] - b[k] for k in range(3))

    def add(a, b):
        return tuple(a[k] + b[k] for k in range(3))

    def mul(a, t):
        return tuple(t * a[k] for k in range(3))

    def dot(a, b):
        return sum(a[k] * b[k] for k in range(3))

    def cross(a, b):
        return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])

    a, b, c, p = rows[7], rows[8], rows[245], rows[246]
    n = cross(sub(b, a), sub(c, a))
    lam = dot(sub(p, a), n) / dot(n, n)
    projection = sub(p, mul(n, lam))
    out = dict(rows)
    # p + (3/2)(projection-p) = projection - (p-projection)/2.
    out[246] = add(p, mul(sub(projection, p), Q(3, 2)))
    return out


def source_faces() -> list[list[int]]:
    faces = json.load(open(SOURCE / "face_cycles.json"))
    old = {frozenset((7, 8, 245)), frozenset((8, 245, 246))}
    faces = [list(c) for c in faces if frozenset(c) not in old]
    faces += [[7, 8, 246], [7, 246, 245]]
    assert len(faces) == 104
    return faces


def orient_faces(P: dict[int, np.ndarray], faces: list[list[int]]) -> list[list[int]]:
    center = np.mean(np.stack(list(P.values())), axis=0)
    ans = []
    for cc in faces:
        c = list(cc)
        a, b, z = (P[i] for i in c[:3])
        n = np.cross(b - a, z - a)
        if np.dot(n, center - a) > 0:
            c = [c[0]] + list(reversed(c[1:]))
        ans.append(c)
    return ans


class FixedSphere:
    def __init__(
        self,
        exact_rows: dict[int, tuple[Q, Q, Q]] | None = None,
        *,
        raw_points: dict[int, np.ndarray] | None = None,
        faces_ids: list[list[int]] | None = None,
        extra_face: tuple[int, int, int] = (7, 8, 246),
    ):
        assert (exact_rows is None) != (raw_points is None)
        source_points = exact_rows if exact_rows is not None else raw_points
        assert source_points is not None
        self.ids = sorted(source_points)
        raw = np.stack([[float(z) for z in source_points[i]] for i in self.ids])
        origin = np.mean(raw, axis=0)
        scale = np.sqrt(np.mean(np.sum((raw - origin) ** 2, axis=1)))
        self.X0 = (raw - origin) / scale
        self.id_to_local = {i: j for j, i in enumerate(self.ids)}
        pdict = {i: self.X0[self.id_to_local[i]] for i in self.ids}
        self.faces_ids = orient_faces(pdict, source_faces() if faces_ids is None else faces_ids)
        self.faces = [[self.id_to_local[i] for i in c] for c in self.faces_ids]
        self.face_first3 = np.asarray([c[:3] for c in self.faces], dtype=int)
        self.mass_tris = np.asarray(
            [(c[0], c[j], c[j + 1]) for c in self.faces for j in range(1, len(c) - 1)],
            dtype=int,
        )
        self.face_edge_u = np.asarray([u for c in self.faces for u, v in zip(c, c[1:] + c[:1])], dtype=int)
        self.face_edge_v = np.asarray([v for c in self.faces for u, v in zip(c, c[1:] + c[:1])], dtype=int)
        self.face_edge_f = np.asarray([fi for fi, c in enumerate(self.faces) for _ in c], dtype=int)
        self.face_key = {frozenset(c): fi for fi, c in enumerate(self.faces_ids)}
        self.base_fi = self.face_key[frozenset(range(17))]
        self.extra_fi = self.face_key[frozenset(extra_face)]
        ef: dict[tuple[int, int], list[int]] = defaultdict(list)
        for fi, c in enumerate(self.faces_ids):
            for a, b in zip(c, c[1:] + c[:1]):
                ef[tuple(sorted((a, b)))].append(fi)
        assert len(ef) == 163 and all(len(v) == 2 for v in ef.values())
        self.ef_ids = dict(ef)
        self.edges = [(self.id_to_local[a], self.id_to_local[b]) for a, b in ef]
        self.edges_array = np.asarray(self.edges, dtype=int)
        self.edge_ids = list(ef)
        self.edge_index = {e: k for k, e in enumerate(self.edge_ids)}
        nb: dict[int, set[int]] = defaultdict(set)
        for a, b in ef:
            nb[a].add(b)
            nb[b].add(a)
        self.nb = {self.id_to_local[i]: [self.id_to_local[j] for j in sorted(js)] for i, js in nb.items()}
        self.target_faces = {self.base_fi, self.extra_fi}
        self.target_vertices = {self.id_to_local[1], self.id_to_local[8]}
        self.target_edges = {self.edge_index[(6, 7)], self.edge_index[(9, 10)]}
        self.edge_inc = np.asarray([ef[e] for e in self.edge_ids], dtype=int)

    @staticmethod
    def matrix(theta: np.ndarray) -> np.ndarray:
        a, b, c, d, e = theta[:5]
        S = np.array([[a, b, c], [b, d, e], [c, e, -a - d]], dtype=float)
        return expm(S)

    def transform(self, theta: np.ndarray) -> tuple[np.ndarray | None, float]:
        M = self.matrix(theta)
        ell = theta[5:8]
        den = 1.0 + self.X0 @ ell
        md = float(np.min(den))
        if md <= 0.025 or not np.isfinite(md):
            return None, md
        return (self.X0 @ M.T) / den[:, None], md

    def evaluate(self, theta: np.ndarray, details: bool = False) -> dict:
        P, min_den = self.transform(theta)
        if P is None:
            return {"valid": False, "score": -1.0e9, "min_den": min_den}

        # Fixed-surface mass formula, vectorized over the face fans.
        ta, tb, tz = (P[self.mass_tris[:, k]] for k in range(3))
        dets = np.einsum("ij,ij->i", ta, np.cross(tb, tz))
        D6 = float(np.sum(dets))
        M24 = np.sum(dets[:, None] * (ta + tb + tz), axis=0)
        if not np.isfinite(D6) or D6 <= 1e-12:
            return {"valid": False, "score": -1.0e9, "min_den": min_den}
        C = M24 / (4.0 * D6)
        X = P - C
        radius = float(np.sqrt(np.mean(np.sum(X * X, axis=1))))

        # Outward normal orientation is fixed under positive-denominator
        # projective maps.  All per-feature mechanics are vectorized.
        ia, ib, iz = (self.face_first3[:, k] for k in range(3))
        normals = np.cross(P[ib] - P[ia], P[iz] - P[ia])
        nn = np.linalg.norm(normals, axis=1)
        if float(np.min(nn)) < 1e-20:
            return {"valid": False, "score": -1.0e9, "min_den": min_den}
        normals /= nn[:, None]
        flip = np.einsum("ij,ij->i", normals, C[None, :] - P[ia]) > 0
        normals[flip] *= -1.0
        h = np.einsum("ij,ij->i", normals, X[ia])
        foot = h[:, None] * normals
        eu, ev, eff = self.face_edge_u, self.face_edge_v, self.face_edge_f
        edgevec = X[ev] - X[eu]
        fcomponents = np.einsum(
            "ij,ij->i", np.cross(edgevec, foot[eff] - X[eu]), normals[eff]
        ) / np.maximum(np.linalg.norm(edgevec, axis=1) * radius, 1e-300)
        fdec = np.full(len(self.faces), np.inf)
        np.minimum.at(fdec, eff, fcomponents)

        ea, eb = self.edges_array[:, 0], self.edges_array[:, 1]
        d = X[eb] - X[ea]
        dn = np.linalg.norm(d, axis=1)
        xn = np.linalg.norm(X, axis=1)
        va = -np.einsum("ij,ij->i", X[ea], d) / np.maximum(xn[ea] * dn, 1e-300)
        vb = np.einsum("ij,ij->i", X[eb], d) / np.maximum(xn[eb] * dn, 1e-300)
        vdec = np.full(len(P), np.inf)
        np.minimum.at(vdec, ea, va)
        np.minimum.at(vdec, eb, vb)

        dd = np.einsum("ij,ij->i", d, d)
        t = -np.einsum("ij,ij->i", X[ea], d) / dd
        p = X[ea] + t[:, None] * d
        n1, n2 = normals[self.edge_inc[:, 0]], normals[self.edge_inc[:, 1]]
        bb = np.einsum("ij,ij->i", n1, n2)
        eden = 1.0 - bb * bb
        if float(np.min(eden)) <= 1e-26:
            return {"valid": False, "score": -1.0e9, "min_den": min_den}
        r1 = np.einsum("ij,ij->i", p, n1)
        r2 = np.einsum("ij,ij->i", p, n2)
        l1, l2 = (r1 - r2 * bb) / eden, (r2 - r1 * bb) / eden
        pn = np.maximum(np.linalg.norm(p, axis=1), 1e-300)
        edec = np.minimum.reduce((t, 1.0 - t, l1 / pn, l2 / pn))

        # Combinatorics is projectively invariant while all denominators are
        # positive, so an O(FV) topology rescan is unnecessary in the search.
        topology = 0.25 * min_den

        margins = []
        for i, z in enumerate(fdec.tolist()):
            margins.append(z if i in self.target_faces else -z)
        for i, z in enumerate(vdec.tolist()):
            margins.append(z if i in self.target_vertices else -z)
        for i, z in enumerate(edec.tolist()):
            margins.append(z if i in self.target_edges else -z)
        margins += [topology, 0.25 * (min_den - 0.025)]
        margins = np.asarray(margins)
        hard = float(np.min(margins))
        # A continuation-friendly objective.  The hard minimum dominates near
        # feasibility, while soft minima provide gradient far from it.
        tau = 0.035
        smooth = float(-tau * logsumexp(-margins / tau))
        score = 0.72 * hard + 0.28 * smooth
        out = {"valid": True, "score": score, "hard": hard, "smooth": smooth, "min_den": min_den, "topology": topology}
        if details:
            stable = [self.faces_ids[i] for i, z in enumerate(fdec.tolist()) if z > 1e-9]
            unstable = [self.ids[i] for i, z in enumerate(vdec.tolist()) if z > 1e-9]
            saddles = [list(self.edge_ids[i]) for i, z in enumerate(edec.tolist()) if z > 1e-9]
            out.update({
                "class": [len(stable), len(unstable), len(saddles)],
                "stable": stable,
                "unstable": unstable,
                "saddles": saddles,
                "centroid": C.tolist(),
                "face_decisions": fdec.tolist(),
                "vertex_decisions": {str(self.ids[i]): float(z) for i, z in enumerate(vdec)},
                "edge_decisions": {f"{a},{b}": float(edec[i]) for i, (a, b) in enumerate(self.edge_ids)},
                "points": {str(i): P[self.id_to_local[i]].tolist() for i in self.ids},
            })
        return out


def write_exact_far(rows: dict[int, tuple[Q, Q, Q]]) -> None:
    with open(HERE / "far_side_source_exact.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source_id", "x_exact", "y_exact", "z_exact", "x_decimal", "y_decimal", "z_decimal"])
        for i in sorted(rows):
            q = rows[i]
            w.writerow([i, *(f"{z.numerator}/{z.denominator}" for z in q), *(repr(float(z)) for z in q)])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=57725000)
    ap.add_argument("--maxiter", type=int, default=350)
    ap.add_argument("--popsize", type=int, default=18)
    ap.add_argument("--workers", type=int, default=1)
    ap.add_argument("--out", default="recovered_far_side.json")
    args = ap.parse_args()

    exact = exact_far_side(load_exact_rows())
    write_exact_far(exact)
    sphere = FixedSphere(exact)
    zero = sphere.evaluate(np.zeros(8), details=True)
    print("source", zero["class"], zero["hard"], zero["stable"], zero["unstable"], zero["saddles"], flush=True)

    def fun(x):
        return -sphere.evaluate(np.asarray(x))["score"]

    bounds = [(-3.2, 3.2)] * 5 + [(-1.35, 1.35)] * 3
    best_x = np.zeros(8)
    best = sphere.evaluate(best_x)

    def callback(xk, convergence=0.0):
        nonlocal best_x, best
        z = sphere.evaluate(np.asarray(xk))
        if z.get("valid") and z.get("hard", -1.0e99) > best.get("hard", -1.0e99):
            best_x, best = np.asarray(xk).copy(), z
            print("best", best["hard"], best["score"], "conv", convergence, "x", best_x.tolist(), flush=True)
        return z.get("hard", -1.0) > 2e-4

    res = differential_evolution(
        fun,
        bounds,
        seed=args.seed,
        maxiter=args.maxiter,
        popsize=args.popsize,
        tol=2e-7,
        mutation=(0.45, 1.25),
        recombination=0.82,
        polish=False,
        workers=args.workers,
        updating="immediate" if args.workers == 1 else "deferred",
        callback=callback,
    )
    candidates = [best_x, np.asarray(res.x)]
    for x0 in candidates[:]:
        rr = minimize(fun, x0, method="Nelder-Mead", options={"maxiter": 6000, "xatol": 2e-10, "fatol": 2e-10})
        candidates.append(np.asarray(rr.x))
    best_x = max(candidates, key=lambda x: sphere.evaluate(x).get("hard", -99))
    detail = sphere.evaluate(best_x, details=True)
    detail["theta"] = best_x.tolist()
    detail["source_exact_csv"] = "far_side_source_exact.csv"
    detail["target_signature"] = {
        "stable": [list(range(17)), [7, 8, 246]],
        "unstable": [1, 8],
        "saddles": [[6, 7], [9, 10]],
    }
    json.dump(detail, open(HERE / args.out, "w"), indent=2)
    with open(HERE / "recovered_far_side_points.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source_id", "x", "y", "z"])
        for i in sphere.ids:
            w.writerow([i, *detail["points"][str(i)]])
    print("FINAL", detail["class"], detail["hard"], detail["stable"], detail["unstable"], detail["saddles"], flush=True)


if __name__ == "__main__":
    main()
