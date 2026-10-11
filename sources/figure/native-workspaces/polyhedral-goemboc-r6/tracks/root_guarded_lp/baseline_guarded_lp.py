#!/usr/bin/env python3
"""Linearized, support-slack-guarded escape audit for the exact M42 fifth cell.

This is deliberately a *fixed actual-cell* diagnostic.  It enumerates the
primitive signs that certify the current hull and mechanics, differentiates
them through low Dirichlet graph modes plus local/affine/projective modes, and
asks whether one stable-face component and one saddle-edge component can die
before any selected guard is consumed.

The LP is normalized in event time: both selected death primitives must have
fractional derivative <= -1.  ``delta`` is the largest fractional guard loss
at that same unit time.  Hence delta < 1 is the useful first-order gate;
delta <= 0 would be a genuinely non-worsening direction.
"""

from __future__ import annotations

import csv
import json
import sys
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BUNDLE = ROOT / "M42_acute_bridge_fifth_cell_work"
sys.path.insert(0, str(BUNDLE / "fourth_cell_endpoint"))
from numeric_hull_proposer import evaluate, score_target  # noqa: E402


BASE_FACE = frozenset(range(17))
EXTRA_FACE = frozenset((198, 224, 258))
TARGET_VERTEX = 8
SADDLE_EDGE = (229, 247)


def load_points() -> dict[int, np.ndarray]:
    out: dict[int, np.ndarray] = {}
    path = BUNDLE / "fifth_cell_endpoint" / "coordinates_all_exact.csv"
    with path.open() as fh:
        for row in csv.DictReader(fh):
            out[int(row["source_id"])] = np.array(
                [float(Fraction(row["x_exact"])), float(Fraction(row["y_exact"])), float(Fraction(row["z_exact"]))],
                dtype=float,
            )
    return out


def cycle_edges(cycle):
    return [tuple(sorted((a, b))) for a, b in zip(cycle, cycle[1:] + cycle[:1])]


def primitive_ledger(points: dict[int, np.ndarray]):
    """Return actual result and a canonical primitive-value dictionary."""
    res = evaluate(points, plane_tol=1e-8, qhull_options="Qt Qx", strict_tol=1e-12)
    if not res.valid:
        raise RuntimeError(res.error)
    ids = sorted(points)
    P = {i: np.asarray(points[i], float) for i in ids}
    X = {i: P[i] - res.centroid for i in ids}
    vals: dict[tuple, float] = {}

    # Maximal-face projection components and every point/plane support slack.
    for face in res.faces:
        cyc = face["cycle"]
        fkey = tuple(sorted(cyc))
        n = np.asarray(face["n"], float)
        h = -(float(face["off"]) + float(np.dot(n, res.centroid)))
        foot = h * n
        ref = np.mean([X[i] for i in cyc], axis=0)
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            e = X[b] - X[a]
            z = float(np.dot(np.cross(e, foot - X[a]), n) / np.linalg.norm(e))
            if np.dot(np.cross(e, ref - X[a]), n) < 0:
                z = -z
            vals[("face", fkey, tuple(sorted((a, b))))] = z
        cset = set(cyc)
        for i in ids:
            if i not in cset:
                vals[("topology", fkey, i)] = -float(np.dot(P[i], n) + face["off"])

    # Vertex directed supports.
    for i in res.active:
        xi = X[i]
        for j in sorted(res.neighbors[i]):
            d = X[j] - xi
            z = -float(np.dot(xi, d) / (np.linalg.norm(xi) * np.linalg.norm(d)))
            vals[("vertex", i, j)] = z

    # True-edge four-component normal cones.
    face_by_index = {k: f for k, f in enumerate(res.faces)}
    for e in res.edges:
        a, b = e
        inc = res.edge_faces[e]
        d = X[b] - X[a]
        dd = float(np.dot(d, d))
        t = -float(np.dot(X[a], d) / dd)
        p = X[a] + t * d
        n1 = np.asarray(face_by_index[inc[0]]["n"], float)
        n2 = np.asarray(face_by_index[inc[1]]["n"], float)
        aa = float(np.dot(n1, n1))
        bb = float(np.dot(n1, n2))
        cc = float(np.dot(n2, n2))
        r1 = float(np.dot(p, n1))
        r2 = float(np.dot(p, n2))
        den = aa * cc - bb * bb
        beta1 = (r1 * cc - r2 * bb) / den / np.linalg.norm(p)
        beta2 = (r2 * aa - r1 * bb) / den / np.linalg.norm(p)
        vals[("edge", e, "t")] = t
        vals[("edge", e, "one_minus_t")] = 1.0 - t
        vals[("edge", e, "beta1")] = beta1
        vals[("edge", e, "beta2")] = beta2
    return res, vals


def graph_modes(base: dict[int, np.ndarray], res, count=16):
    active = sorted(res.active)
    fixed = set(range(17))
    free = [i for i in active if i not in fixed]
    ix = {v: k for k, v in enumerate(free)}
    L = np.zeros((len(free), len(free)))
    for i in free:
        ii = ix[i]
        for j in res.neighbors[i]:
            L[ii, ii] += 1.0
            if j in ix:
                L[ii, ix[j]] -= 1.0
    w, U = np.linalg.eigh(L)
    order = np.argsort(w)
    modes = []
    meta = []
    for rank, col in enumerate(order[: min(count, len(order))]):
        scalar = U[:, col]
        scalar /= max(np.max(np.abs(scalar)), 1e-300)
        for axis in range(3):
            m = {i: np.zeros(3) for i in base}
            for i in free:
                m[i][axis] = scalar[ix[i]]
            modes.append(m)
            meta.append({"kind": "dirichlet_laplacian", "rank": rank, "eigenvalue": float(w[col]), "axis": axis})
    return modes, meta


def build_modes(base, res):
    modes, meta = graph_modes(base, res, 16)

    # Full local controls on the six-row core and known remote control rows.
    local_rows = [198, 224, 228, 229, 247, 258, 232, 248, 257, 54, 69]
    for i in local_rows:
        if i not in base:
            continue
        for axis in range(3):
            m = {j: np.zeros(3) for j in base}
            m[i][axis] = 1.0
            modes.append(m)
            meta.append({"kind": "row_coordinate", "row": i, "axis": axis})

    # All linear deformation generators.  These move inactive rows as well and
    # therefore preserve every exact coplanarity to first order.
    for a in range(3):
        for b in range(3):
            m = {i: np.eye(3)[a] * base[i][b] for i in base}
            modes.append(m)
            meta.append({"kind": "linear", "output_axis": a, "input_axis": b})

    # Infinitesimal projective generators x -> x/(1+a.x).
    for a in range(3):
        m = {i: -base[i] * base[i][a] for i in base}
        modes.append(m)
        meta.append({"kind": "projective", "axis": a})

    # Normalize each geometric column to unit maximum point displacement.
    for m in modes:
        scale = max(np.linalg.norm(v) for v in m.values())
        for i in m:
            m[i] = m[i] / max(scale, 1e-300)
    return modes, meta


def chosen_guards(res, vals):
    guards: list[tuple[tuple, int, str]] = []
    # sign = +1 means keep positive; sign = -1 means keep negative.
    face_keys = defaultdict(list)
    vertex_keys = defaultdict(list)
    edge_keys = defaultdict(list)
    topo_keys = []
    for key, value in vals.items():
        if key[0] == "face":
            face_keys[frozenset(key[1])].append(key)
        elif key[0] == "vertex":
            vertex_keys[key[1]].append(key)
        elif key[0] == "edge":
            edge_keys[key[1]].append(key)
        elif key[0] == "topology":
            topo_keys.append(key)

    for fset, keys in face_keys.items():
        if fset == EXTRA_FACE:
            continue
        if fset == BASE_FACE:
            for key in keys:
                guards.append((key, +1, "protected_base_component"))
        else:
            key = min(keys, key=lambda k: vals[k])
            if vals[key] >= 0:
                raise AssertionError(("unexpected stable face", fset))
            guards.append((key, -1, "nonstable_face_witness"))

    for vertex, keys in vertex_keys.items():
        if vertex == TARGET_VERTEX:
            for key in keys:
                guards.append((key, +1, "protected_U8_support"))
        else:
            key = min(keys, key=lambda k: vals[k])
            if vals[key] >= 0:
                raise AssertionError(("unexpected unstable vertex", vertex))
            guards.append((key, -1, "nonunstable_vertex_witness"))

    for edge, keys in edge_keys.items():
        if edge == SADDLE_EDGE:
            continue
        key = min(keys, key=lambda k: vals[k])
        if vals[key] >= 0:
            raise AssertionError(("unexpected saddle", edge))
        guards.append((key, -1, "nonsaddle_edge_witness"))

    # Every point/plane gap guards the complete actual face lattice.  Very large
    # gaps are still retained: the LP dual will tell us whether they matter.
    for key in topo_keys:
        guards.append((key, +1, "support_slack"))
    return guards


def finite_difference(base, base_vals, modes, h=1e-7):
    keys = list(base_vals)
    J = np.zeros((len(keys), len(modes)))
    key_index = {k: i for i, k in enumerate(keys)}
    failures = []
    for col, mode in enumerate(modes):
        plus = {i: base[i] + h * mode[i] for i in base}
        minus = {i: base[i] - h * mode[i] for i in base}
        try:
            rp, vp = primitive_ledger(plus)
            rm, vm = primitive_ledger(minus)
            if set(vp) != set(base_vals) or set(vm) != set(base_vals):
                raise RuntimeError("primitive key set changed")
            for key in keys:
                J[key_index[key], col] = (vp[key] - vm[key]) / (2.0 * h)
        except Exception as exc:  # pragma: no cover - diagnostic path
            failures.append((col, repr(exc)))
            # One-sided fallback is useful for columns tangent to a tiny qhull
            # grouping tolerance.
            try:
                _, vp = primitive_ledger(plus)
                if set(vp) != set(base_vals):
                    raise RuntimeError("one-sided key set changed")
                for key in keys:
                    J[key_index[key], col] = (vp[key] - base_vals[key]) / h
            except Exception as exc2:
                raise RuntimeError((col, exc, exc2))
    return keys, key_index, J, failures


def solve_atlas(vals, key_index, J, guards, mode_meta):
    extra_face_keys = [k for k in vals if k[0] == "face" and frozenset(k[1]) == EXTRA_FACE]
    saddle_keys = [k for k in vals if k[0] == "edge" and k[1] == SADDLE_EDGE]
    assert len(extra_face_keys) == 3 and len(saddle_keys) == 4
    n = J.shape[1]

    # Guard rows are fractional worsening rates.  Cap tiny denominators only to
    # avoid numerical overflow; all named baseline margins are much larger.
    G = []
    guard_info = []
    for key, sign, kind in guards:
        v = vals[key]
        scale = max(abs(v), 1e-12)
        worsening = -sign * J[key_index[key]] / scale
        G.append(worsening)
        guard_info.append({"key": repr(key), "kind": kind, "sign": sign, "value": v})
    G = np.asarray(G)

    results = []
    # Variables are c[0:n], delta.  Each guard has worsening <= delta.
    A_guard = np.hstack((G, -np.ones((len(G), 1))))
    b_guard = np.zeros(len(G))
    objective = np.r_[np.zeros(n), 1.0]
    bounds = [(-20.0, 20.0)] * n + [(-1000.0, 1000.0)]

    for fk in extra_face_keys:
        for ek in saddle_keys:
            d1 = J[key_index[fk]] / vals[fk]
            d2 = J[key_index[ek]] / vals[ek]
            A = np.vstack((A_guard, np.r_[d1, 0.0], np.r_[d2, 0.0]))
            b = np.r_[b_guard, -1.0, -1.0]
            lp = linprog(objective, A_ub=A, b_ub=b, bounds=bounds, method="highs")
            rec = {
                "face_death": repr(fk),
                "saddle_death": repr(ek),
                "success": bool(lp.success),
                "message": lp.message,
            }
            if lp.success:
                c = lp.x[:n]
                worsening = G @ c
                top = np.argsort(worsening)[-20:][::-1]
                chosen = np.argsort(np.abs(c))[-20:][::-1]
                rec.update(
                    delta=float(lp.x[-1]),
                    face_fractional_derivative=float(d1 @ c),
                    saddle_fractional_derivative=float(d2 @ c),
                    max_abs_coefficient=float(np.max(np.abs(c))),
                    l1_coefficient=float(np.sum(np.abs(c))),
                    coefficients=[float(z) for z in c],
                    top_guard_blockers=[
                        {**guard_info[i], "fractional_worsening": float(worsening[i])} for i in top
                    ],
                    active_modes=[
                        {"column": int(i), "coefficient": float(c[i]), **mode_meta[i]} for i in chosen
                    ],
                )
                if hasattr(lp, "ineqlin") and lp.ineqlin.marginals is not None:
                    dual = -np.asarray(lp.ineqlin.marginals[: len(G)])
                    di = np.argsort(dual)[-20:][::-1]
                    rec["top_dual_guards"] = [
                        {**guard_info[i], "dual_weight": float(dual[i])} for i in di if dual[i] > 1e-10
                    ]
            results.append(rec)
    return results, guard_info


def main():
    base = load_points()
    res, vals = primitive_ledger(base)
    assert (len(res.active), len(res.edges), len(res.faces)) == (61, 163, 104)
    assert (len(res.stable), len(res.unstable), len(res.saddles)) == (2, 1, 1)
    modes, meta = build_modes(base, res)
    keys, key_index, J, failures = finite_difference(base, vals, modes)
    np.savez_compressed(
        HERE / "baseline_guarded_jacobian.npz",
        jacobian=J,
        primitive_keys=np.asarray([repr(k) for k in keys], dtype=object),
        primitive_values=np.asarray([vals[k] for k in keys]),
        mode_meta=np.asarray([json.dumps(m, sort_keys=True) for m in meta], dtype=object),
    )
    guards = chosen_guards(res, vals)
    atlas, guard_info = solve_atlas(vals, key_index, J, guards, meta)
    atlas.sort(key=lambda r: r.get("delta", 1e100))
    out = {
        "version": 1,
        "scope": "linearized fixed-actual-cell support-slack-guarded audit",
        "baseline": {
            "f_vector": [len(res.active), len(res.edges), len(res.faces)],
            "class": [len(res.stable), len(res.unstable), len(res.saddles)],
            "topology_margin": res.topology_margin,
            "inactive_margin": res.inactive_margin,
        },
        "modes": len(modes),
        "primitive_rows": len(keys),
        "guard_rows": len(guards),
        "finite_difference_failures": failures,
        "interpretation": "delta<1 predicts both named deaths before every selected guard; delta<=0 is non-worsening. This is first-order evidence only.",
        "atlas": atlas,
    }
    (HERE / "baseline_guarded_lp.json").write_text(json.dumps(out, indent=2))
    best = atlas[0]
    print("baseline", out["baseline"])
    print("modes", len(modes), "primitives", len(keys), "guards", len(guards))
    print("best", best.get("delta"), best["face_death"], best["saddle_death"])
    for b in best.get("top_guard_blockers", [])[:10]:
        print("blocker", b["fractional_worsening"], b["kind"], b["key"])


if __name__ == "__main__":
    main()
