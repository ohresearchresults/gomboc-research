#!/usr/bin/env python3
"""Full-chart guarded first jet for the four residual combined-wall deaths.

The canonical wall has exactly two stable faces (base and q246 quad), two
unstable vertices (8 and 54), and two saddle edges (6,7) and (9,10).  This
script differentiates the complete 164-dimensional planarity chart and asks
whether the four extra features can die together before any protected
mechanical witness, point/plane support slack, or maximal-face incidence
guard is exhausted.
"""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import argparse
import csv
import importlib.util
import json

import numpy as np
from scipy.optimize import linprog


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
GUARDED = ROOT / "tracks" / "root_guarded_lp"
spec = importlib.util.spec_from_file_location("baseline_guarded", GUARDED / "baseline_guarded_lp.py")
baseline = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(baseline)
_primitive_base = baseline.primitive_ledger

SOURCE = ROOT / "tracks" / "circuit_atlas" / "row54_combined_wall_rebuilt.csv"
BASE = frozenset(range(17)) | {54}
QUAD = frozenset((7, 8, 245, 246))
U_TARGET = 8
U_EXTRA = 54
H_EXTRA = {(6, 7), (9, 10)}
ACTIVE_PLANE_TOL = None


def load_points(path=SOURCE):
    out = {}
    with Path(path).open() as f:
        for r in csv.DictReader(f):
            out[int(r["source_id"])] = np.asarray(
                [float(r[k]) for k in ("x", "y", "z")], dtype=float
            )
    return out


def primitive_ledger(points, plane_tol=None):
    """Baseline primitive ledger plus within-face incidence/orientation rows."""
    if plane_tol is None:
        plane_tol = ACTIVE_PLANE_TOL
    if plane_tol is None:
        res, vals = _primitive_base(points)
    else:
        # The baseline ledger deliberately uses a generous facet-grouping
        # tolerance.  Event-driven continuation sometimes needs the exact
        # adjacent triangulations in a much thinner band; override only for
        # this call without changing the shared evaluator globally afterward.
        evaluator_globals = _primitive_base.__globals__
        original_evaluate = evaluator_globals["evaluate"]

        def evaluate_with_tolerance(candidate, **kwargs):
            kwargs["plane_tol"] = plane_tol
            return original_evaluate(candidate, **kwargs)

        evaluator_globals["evaluate"] = evaluate_with_tolerance
        try:
            res, vals = _primitive_base(points)
        finally:
            evaluator_globals["evaluate"] = original_evaluate
    P = {i: np.asarray(p, dtype=float) for i, p in points.items()}
    for face in res.faces:
        cyc = list(face["cycle"])
        fkey = tuple(sorted(cyc))
        n = np.asarray(face["n"], dtype=float)
        ref = np.mean([P[i] for i in cyc], axis=0)
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            e = P[b] - P[a]
            en = np.linalg.norm(e)
            side = float(np.dot(np.cross(e, ref - P[a]), n))
            sign = 1.0 if side >= 0 else -1.0
            edge = tuple(sorted((a, b)))
            for w in cyc:
                if w in (a, b):
                    continue
                value = sign * float(np.dot(np.cross(e, P[w] - P[a]), n)) / en
                vals[("incidence", fkey, edge, w)] = value
    return res, vals


# Make the shared central-difference routine call the extended ledger.
baseline.primitive_ledger = primitive_ledger


def chart_modes(points):
    """The exact 164-coordinate base+quad planarity chart first jet."""
    ids = sorted(points)
    p0, p1, p2 = (points[i] for i in (0, 1, 2))
    e1 = p1 - p0
    e1 /= np.linalg.norm(e1)
    normal = np.cross(p1 - p0, p2 - p0)
    normal /= np.linalg.norm(normal)
    e2 = np.cross(normal, e1)
    e2 /= np.linalg.norm(e2)
    a = points[7]
    M = np.column_stack((points[8] - a, points[245] - a))
    alpha, beta = np.linalg.lstsq(M, points[246] - a, rcond=None)[0]
    weights = {7: 1.0 - alpha - beta, 8: alpha, 245: beta}

    modes, meta = [], []

    def add(row, direction, label, induced=0.0):
        m = {i: np.zeros(3) for i in ids}
        m[row] = np.asarray(direction, dtype=float).copy()
        if row in weights:
            m[246] += weights[row] * np.asarray(direction, dtype=float)
        if induced:
            m[246] += induced * np.asarray(direction, dtype=float)
        scale = max(np.linalg.norm(v) for v in m.values())
        for i in m:
            m[i] /= max(scale, 1e-300)
        modes.append(m)
        meta.append(label)

    for i in sorted(BASE):
        add(i, e1, {"kind": "chart", "row": i, "axis": "base_u"})
        add(i, e2, {"kind": "chart", "row": i, "axis": "base_v"})
    free = [i for i in ids if i not in BASE and i != 246]
    for i in free:
        for k, name in enumerate("xyz"):
            add(i, np.eye(3)[k], {"kind": "chart", "row": i, "axis": name})
    # Independent affine coordinates of q246 in plane(7,8,245).
    add(246, points[8] - points[7], {"kind": "chart", "row": 246, "axis": "quad_a"})
    add(246, points[245] - points[7], {"kind": "chart", "row": 246, "axis": "quad_b"})
    if len(modes) != 164:
        raise ValueError(f"chart dimension {len(modes)} != 164")
    return modes, meta, {"quad_alpha": float(alpha), "quad_beta": float(beta)}


def chosen_guards(vals):
    groups = {"face": defaultdict(list), "vertex": defaultdict(list), "edge": defaultdict(list)}
    topology, incidence = [], []
    for key in vals:
        if key[0] in groups:
            group = frozenset(key[1]) if key[0] == "face" else key[1]
            groups[key[0]][group].append(key)
        elif key[0] == "topology":
            topology.append(key)
        elif key[0] == "incidence":
            incidence.append(key)
    out = []
    for fset, keys in groups["face"].items():
        if fset == QUAD:
            continue
        if fset == BASE:
            out.extend((k, +1, "protected_base_component") for k in keys)
        else:
            k = min(keys, key=vals.__getitem__)
            if vals[k] >= 0:
                raise ValueError(("unexpected stable face", sorted(fset), vals[k]))
            out.append((k, -1, "nonstable_face_witness"))
    for vertex, keys in groups["vertex"].items():
        if vertex == U_EXTRA:
            continue
        if vertex == U_TARGET:
            out.extend((k, +1, "protected_U8_support") for k in keys)
        else:
            k = min(keys, key=vals.__getitem__)
            if vals[k] >= 0:
                raise ValueError(("unexpected unstable vertex", vertex, vals[k]))
            out.append((k, -1, "nonunstable_vertex_witness"))
    for edge, keys in groups["edge"].items():
        if edge in H_EXTRA:
            continue
        k = min(keys, key=vals.__getitem__)
        if vals[k] >= 0:
            raise ValueError(("unexpected saddle edge", edge, vals[k]))
        out.append((k, -1, "nonsaddle_edge_witness"))
    out.extend((k, +1, "support_slack") for k in topology)
    out.extend((k, +1, "incidence_slack") for k in incidence)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default=str(SOURCE))
    ap.add_argument("--prefix", default="combined_four_death_lp")
    ap.add_argument("--bound", type=float, default=100.0)
    ap.add_argument(
        "--plane-tol", type=float,
        help="optional tight maximal-face grouping tolerance used by the full ledger and FD",
    )
    ap.add_argument(
        "--expected-fvector", default="61,161,102",
        help="comma-separated fresh f-vector, or 'any' for an adjacent relay cell",
    )
    args = ap.parse_args()
    global ACTIVE_PLANE_TOL
    ACTIVE_PLANE_TOL = args.plane_tol
    source = Path(args.source).resolve()
    points = load_points(source)
    res, vals = primitive_ledger(points)
    actual_fvector = (len(res.active), len(res.edges), len(res.faces))
    if args.expected_fvector != "any":
        expected_fvector = tuple(int(x) for x in args.expected_fvector.split(","))
        if actual_fvector != expected_fvector:
            raise ValueError(f"fresh f-vector {actual_fvector} != expected {expected_fvector}")
    assert {frozenset(res.faces[i]["cycle"]) for i, _ in res.stable} == {BASE, QUAD}
    assert {i for i, _ in res.unstable} == {8, 54}
    assert {e for e, _ in res.saddles} == H_EXTRA
    modes, meta, chart_meta = chart_modes(points)
    keys, key_index, J, failures = baseline.finite_difference(points, vals, modes, h=1e-9)
    np.savez_compressed(
        HERE / f"{args.prefix}_jacobian.npz",
        jacobian=J,
        primitive_keys=np.asarray([repr(k) for k in keys], dtype=object),
        primitive_values=np.asarray([vals[k] for k in keys]),
        mode_meta=np.asarray([json.dumps(m, sort_keys=True) for m in meta], dtype=object),
    )

    guards = chosen_guards(vals)
    G, info = [], []
    for key, sign, kind in guards:
        scale = max(abs(vals[key]), 1e-12)
        G.append(-sign * J[key_index[key]] / scale)
        info.append({"key": repr(key), "kind": kind, "value": vals[key], "sign": sign})
    G = np.asarray(G)
    n = len(modes)
    A_guard = np.hstack((G, -np.ones((len(G), 1))))
    objective = np.r_[np.zeros(n), 1.0]
    bounds = [(-args.bound, args.bound)] * n + [(-1e6, 1e6)]

    fkey = next(
        k for k in vals
        if k[0] == "face" and frozenset(k[1]) == QUAD and k[2] == (8, 246)
    )
    ukey = ("vertex", 54, 1)
    if not (vals[fkey] > 0 and vals[ukey] > 0):
        raise ValueError((fkey, vals[fkey], ukey, vals[ukey]))
    h67 = [k for k in vals if k[0] == "edge" and k[1] == (6, 7)]
    h910 = [k for k in vals if k[0] == "edge" and k[1] == (9, 10)]
    results = []
    for k67 in h67:
        for k910 in h910:
            deaths = [fkey, ukey, k67, k910]
            rows = [J[key_index[k]] / vals[k] for k in deaths]
            A = np.vstack((A_guard, *[np.r_[r, 0.0] for r in rows]))
            b = np.r_[np.zeros(len(G)), np.full(4, -1.0)]
            lp = linprog(objective, A_ub=A, b_ub=b, bounds=bounds, method="highs")
            rec = {"deaths": [repr(k) for k in deaths], "success": bool(lp.success), "message": lp.message}
            if lp.success:
                c = lp.x[:n]
                worsening = G @ c
                order = np.argsort(worsening)[-30:][::-1]
                active = np.argsort(np.abs(c))[-30:][::-1]
                D = np.vstack(rows)
                rec.update(
                    delta=float(lp.x[-1]),
                    death_rank=int(np.linalg.matrix_rank(D, tol=1e-8)),
                    death_singular_values=np.linalg.svd(D, compute_uv=False).tolist(),
                    fractional_death_derivatives=[float(r @ c) for r in rows],
                    coefficients=[float(z) for z in c],
                    max_abs_coefficient=float(np.max(np.abs(c))),
                    l1_coefficient=float(np.sum(np.abs(c))),
                    top_guard_blockers=[
                        {**info[i], "fractional_worsening": float(worsening[i])} for i in order
                    ],
                    active_modes=[
                        {"column": int(i), "coefficient": float(c[i]), **meta[i]} for i in active
                    ],
                )
                if lp.ineqlin.marginals is not None:
                    dual = -np.asarray(lp.ineqlin.marginals[: len(G)])
                    di = np.argsort(dual)[-30:][::-1]
                    rec["top_dual_guards"] = [
                        {**info[i], "dual_weight": float(dual[i])}
                        for i in di if dual[i] > 1e-10
                    ]
            results.append(rec)
    results.sort(key=lambda r: r.get("delta", 1e100))
    out = {
        "version": 1,
        "scope": "combined wall full-164-chart guarded four-death first jet",
        "baseline": {
            "source": str(source.relative_to(ROOT)) if source.is_relative_to(ROOT) else str(source),
            "f_vector": [len(res.active), len(res.edges), len(res.faces)],
            "class": [len(res.stable), len(res.unstable), len(res.saddles)],
            "topology_margin": res.topology_margin,
            **chart_meta,
        },
        "modes": len(modes),
        "primitive_rows": len(keys),
        "guard_rows": len(guards),
        "support_guard_rows": sum(k == "support_slack" for _, _, k in guards),
        "incidence_guard_rows": sum(k == "incidence_slack" for _, _, k in guards),
        "finite_difference_failures": failures,
        "interpretation": "delta<1 reaches all four selected walls before every normalized guard; delta>=1 is a sharp first-jet obstruction for that branch and trust box.",
        "atlas": results,
    }
    (HERE / f"{args.prefix}.json").write_text(json.dumps(out, indent=2))
    best = results[0]
    print("baseline", out["baseline"])
    print("modes/primitives/guards", len(modes), len(keys), len(guards))
    print("best", best.get("delta"), best["deaths"])
    for b in best.get("top_guard_blockers", [])[:15]:
        print("blocker", b["fractional_worsening"], b["kind"], b["key"])


if __name__ == "__main__":
    main()
