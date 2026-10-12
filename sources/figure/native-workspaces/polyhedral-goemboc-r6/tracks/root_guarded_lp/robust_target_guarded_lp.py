#!/usr/bin/env python3
"""Guarded four-death Jacobian atlas on the reconstructed deep target sphere.

The robust cell has exactly base+F0 stable, U1+U8 unstable and H67+H910
saddle.  We select the transfer-informed F0 edge (8,245) and U1->2 death
components, enumerate all 4x4 saddle component pairs, and guard the complete
actual hull plus one strict exclusion witness for every other feature.
"""

from __future__ import annotations

import csv
import importlib.util
import json
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
spec = importlib.util.spec_from_file_location("baseline_guarded", HERE / "baseline_guarded_lp.py")
baseline = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(baseline)

BASE_FACE = frozenset(range(17))
F0 = frozenset((8, 245, 246))
U_TARGET = 8
U_EXTRA = 1
H_EXTRA = {(6, 7), (9, 10)}


def load_points():
    path = ROOT / "tracks" / "circuit_atlas" / "robust_target_rebuilt.csv"
    out = {}
    with path.open() as fh:
        for row in csv.DictReader(fh):
            out[int(row["source_id"])] = np.array([float(row[k]) for k in ("x", "y", "z")])
    return out


def build_modes(base, res):
    modes, meta = baseline.graph_modes(base, res, 16)
    # Rows 0..16 form one exact maximal polygon.  Independent Cartesian
    # perturbations of one of those rows leave its supporting plane and make
    # the four-component edge ledger singular before the derivative is even
    # evaluated.  Give base rows only the two genuine in-plane controls.
    p0, p1, p2 = (base[i] for i in (0, 1, 2))
    tangent_u = p1 - p0
    tangent_u /= np.linalg.norm(tangent_u)
    base_normal = np.cross(p1 - p0, p2 - p0)
    base_normal /= np.linalg.norm(base_normal)
    tangent_v = np.cross(base_normal, tangent_u)
    tangent_v /= np.linalg.norm(tangent_v)
    local_rows = [0, 1, 2, 5, 6, 7, 8, 9, 10, 11, 54, 69, 198, 224, 228, 232, 245, 246, 247, 248, 258]
    for i in local_rows:
        if i not in base:
            continue
        directions = (tangent_u, tangent_v) if i in BASE_FACE else tuple(np.eye(3))
        for axis, direction in enumerate(directions):
            m = {j: np.zeros(3) for j in base}
            m[i] = np.asarray(direction, dtype=float).copy()
            modes.append(m)
            meta.append({
                "kind": "base_tangent" if i in BASE_FACE else "row_coordinate",
                "row": i,
                "axis": axis,
            })
    for a in range(3):
        for b in range(3):
            m = {i: np.eye(3)[a] * base[i][b] for i in base}
            modes.append(m)
            meta.append({"kind": "linear", "output_axis": a, "input_axis": b})
    for a in range(3):
        m = {i: -base[i] * base[i][a] for i in base}
        modes.append(m)
        meta.append({"kind": "projective", "axis": a})
    for m in modes:
        scale = max(np.linalg.norm(v) for v in m.values())
        for i in m:
            m[i] = m[i] / max(scale, 1e-300)
    return modes, meta


def chosen_guards(vals):
    groups = {"face": defaultdict(list), "vertex": defaultdict(list), "edge": defaultdict(list)}
    topology = []
    for key in vals:
        if key[0] == "face":
            groups["face"][frozenset(key[1])].append(key)
        elif key[0] == "vertex":
            groups["vertex"][key[1]].append(key)
        elif key[0] == "edge":
            groups["edge"][key[1]].append(key)
        elif key[0] == "topology":
            topology.append(key)
    out = []
    for fset, keys in groups["face"].items():
        if fset == F0:
            continue
        if fset == BASE_FACE:
            out.extend((k, +1, "protected_base_component") for k in keys)
        else:
            k = min(keys, key=vals.__getitem__)
            assert vals[k] < 0, (fset, vals[k])
            out.append((k, -1, "nonstable_face_witness"))
    for vertex, keys in groups["vertex"].items():
        if vertex == U_EXTRA:
            continue
        if vertex == U_TARGET:
            out.extend((k, +1, "protected_U8_support") for k in keys)
        else:
            k = min(keys, key=vals.__getitem__)
            assert vals[k] < 0, (vertex, vals[k])
            out.append((k, -1, "nonunstable_vertex_witness"))
    for edge, keys in groups["edge"].items():
        if edge in H_EXTRA:
            continue
        k = min(keys, key=vals.__getitem__)
        assert vals[k] < 0, (edge, vals[k])
        out.append((k, -1, "nonsaddle_edge_witness"))
    out.extend((k, +1, "support_slack") for k in topology)
    return out


def main():
    base = load_points()
    res, vals = baseline.primitive_ledger(base)
    assert (len(res.active), len(res.edges), len(res.faces)) == (61, 163, 104)
    assert (len(res.stable), len(res.unstable), len(res.saddles)) == (2, 2, 2)
    assert {frozenset(res.faces[i]["cycle"]) for i, _ in res.stable} == {BASE_FACE, F0}
    assert {i for i, _ in res.unstable} == {1, 8}
    assert {e for e, _ in res.saddles} == H_EXTRA
    modes, meta = build_modes(base, res)
    keys, key_index, J, failures = baseline.finite_difference(base, vals, modes, h=1e-9)
    np.savez_compressed(
        HERE / "robust_target_guarded_jacobian.npz",
        jacobian=J,
        primitive_keys=np.asarray([repr(k) for k in keys], dtype=object),
        primitive_values=np.asarray([vals[k] for k in keys]),
        mode_meta=np.asarray([json.dumps(m, sort_keys=True) for m in meta], dtype=object),
    )

    guards = chosen_guards(vals)
    G, info = [], []
    for key, sign, kind in guards:
        G.append(-sign * J[key_index[key]] / max(abs(vals[key]), 1e-12))
        info.append({"key": repr(key), "kind": kind, "value": vals[key], "sign": sign})
    G = np.asarray(G)
    n = len(modes)
    A_guard = np.hstack((G, -np.ones((len(G), 1))))
    objective = np.r_[np.zeros(n), 1.0]
    bounds = [(-20.0, 20.0)] * n + [(-1000.0, 1000.0)]

    fkey = next(k for k in vals if k[0] == "face" and frozenset(k[1]) == F0 and k[2] == (8, 245))
    ukey = ("vertex", 1, 2)
    assert fkey in vals and ukey in vals and vals[fkey] > 0 and vals[ukey] > 0
    h67 = [k for k in vals if k[0] == "edge" and k[1] == (6, 7)]
    h910 = [k for k in vals if k[0] == "edge" and k[1] == (9, 10)]
    assert len(h67) == len(h910) == 4
    results = []
    for k67 in h67:
        for k910 in h910:
            deaths = [fkey, ukey, k67, k910]
            rows = [J[key_index[k]] / vals[k] for k in deaths]
            A = np.vstack((A_guard, *[np.r_[r, 0.0] for r in rows]))
            b = np.r_[np.zeros(len(G)), np.full(len(rows), -1.0)]
            lp = linprog(objective, A_ub=A, b_ub=b, bounds=bounds, method="highs")
            rec = {"deaths": [repr(k) for k in deaths], "success": bool(lp.success), "message": lp.message}
            if lp.success:
                c = lp.x[:n]
                worsening = G @ c
                order = np.argsort(worsening)[-20:][::-1]
                active = np.argsort(np.abs(c))[-24:][::-1]
                rec.update(
                    delta=float(lp.x[-1]),
                    fractional_death_derivatives=[float(r @ c) for r in rows],
                    coefficients=[float(z) for z in c],
                    l1_coefficient=float(np.sum(np.abs(c))),
                    top_guard_blockers=[{**info[i], "fractional_worsening": float(worsening[i])} for i in order],
                    active_modes=[{"column": int(i), "coefficient": float(c[i]), **meta[i]} for i in active],
                )
                if lp.ineqlin.marginals is not None:
                    dual = -np.asarray(lp.ineqlin.marginals[: len(G)])
                    di = np.argsort(dual)[-20:][::-1]
                    rec["top_dual_guards"] = [{**info[i], "dual_weight": float(dual[i])} for i in di if dual[i] > 1e-10]
            results.append(rec)
    results.sort(key=lambda r: r.get("delta", 1e100))
    out = {
        "version": 1,
        "scope": "deep robust target-sphere four-death fixed-cell guarded LP",
        "baseline": {
            "f_vector": [len(res.active), len(res.edges), len(res.faces)],
            "class": [len(res.stable), len(res.unstable), len(res.saddles)],
            "topology_margin": res.topology_margin,
            "mechanical_seed": "base+F0, U1+U8, H67+H910",
        },
        "modes": len(modes),
        "primitive_rows": len(keys),
        "guard_rows": len(guards),
        "finite_difference_failures": failures,
        "atlas": results,
    }
    (HERE / "robust_target_guarded_lp.json").write_text(json.dumps(out, indent=2))
    best = results[0]
    print("baseline", out["baseline"], flush=True)
    print("modes/primitives/guards", len(modes), len(keys), len(guards), flush=True)
    print("best delta", best.get("delta"), "deaths", best["deaths"], flush=True)
    for b in best.get("top_guard_blockers", [])[:12]:
        print("blocker", b["fractional_worsening"], b["kind"], b["key"], flush=True)


if __name__ == "__main__":
    main()
