#!/usr/bin/env python3
"""Complete fixed-cell guarded LP for the rail-valid row-54 endpoint.

The endpoint has one protected enlarged base, protected U8, and exactly four
residual equilibria: one stable triangle, U54, H67 and H910.  This script
enumerates every primitive component by which those four features could die,
while guarding every other mechanical witness and every actual support slack.
"""

from __future__ import annotations

import argparse
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

BASE_FACE = frozenset(range(17)) | {54}
EXTRA_FACE = frozenset((8, 245, 246))
TARGET_U = 8
EXTRA_U = 54
EXTRA_H = {(6, 7), (9, 10)}


def load_points():
    out = {}
    with (ROOT / "tracks/circuit_atlas/row54_endpoint_rebuilt.csv").open() as fh:
        for row in csv.DictReader(fh):
            out[int(row["source_id"])] = np.array([float(row[k]) for k in ("x", "y", "z")])
    return out


def graph_modes(base, res, count=16):
    active = sorted(res.active)
    free = [i for i in active if i not in BASE_FACE]
    ix = {v: k for k, v in enumerate(free)}
    lap = np.zeros((len(free), len(free)))
    for i in free:
        ii = ix[i]
        for j in res.neighbors[i]:
            lap[ii, ii] += 1.0
            if j in ix:
                lap[ii, ix[j]] -= 1.0
    values, vectors = np.linalg.eigh(lap)
    modes, meta = [], []
    for rank, col in enumerate(np.argsort(values)[: min(count, len(values))]):
        scalar = vectors[:, col]
        scalar /= max(np.max(np.abs(scalar)), 1e-300)
        for axis in range(3):
            mode = {i: np.zeros(3) for i in base}
            for i in free:
                mode[i][axis] = scalar[ix[i]]
            modes.append(mode)
            meta.append({
                "kind": "dirichlet_laplacian",
                "rank": rank,
                "eigenvalue": float(values[col]),
                "axis": axis,
            })
    return modes, meta


def build_modes(base, res):
    modes, meta = graph_modes(base, res, 16)
    p0, p1, p2 = (base[i] for i in (0, 1, 2))
    tangent_u = p1 - p0
    tangent_u /= np.linalg.norm(tangent_u)
    normal = np.cross(p1 - p0, p2 - p0)
    normal /= np.linalg.norm(normal)
    tangent_v = np.cross(normal, tangent_u)
    tangent_v /= np.linalg.norm(tangent_v)
    local_rows = [
        0, 1, 2, 5, 6, 7, 8, 9, 10, 11, 54,
        69, 198, 224, 228, 229, 232, 245, 246, 247, 248, 258,
    ]
    for i in local_rows:
        if i not in base:
            continue
        directions = (tangent_u, tangent_v) if i in BASE_FACE else tuple(np.eye(3))
        for axis, direction in enumerate(directions):
            mode = {j: np.zeros(3) for j in base}
            mode[i] = np.asarray(direction, dtype=float).copy()
            modes.append(mode)
            meta.append({
                "kind": "base_tangent" if i in BASE_FACE else "row_coordinate",
                "row": i,
                "axis": axis,
            })
    for a in range(3):
        for b in range(3):
            mode = {i: np.eye(3)[a] * base[i][b] for i in base}
            modes.append(mode)
            meta.append({"kind": "linear", "output_axis": a, "input_axis": b})
    for a in range(3):
        mode = {i: -base[i] * base[i][a] for i in base}
        modes.append(mode)
        meta.append({"kind": "projective", "axis": a})
    for mode in modes:
        scale = max(np.linalg.norm(v) for v in mode.values())
        for i in mode:
            mode[i] /= max(scale, 1e-300)
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
    for feature, keys in groups["face"].items():
        if feature == EXTRA_FACE:
            continue
        if feature == BASE_FACE:
            out.extend((key, +1, "protected_base_component") for key in keys)
        else:
            key = min(keys, key=vals.__getitem__)
            assert vals[key] < 0, (feature, vals[key])
            out.append((key, -1, "nonstable_face_witness"))
    for feature, keys in groups["vertex"].items():
        if feature == EXTRA_U:
            continue
        if feature == TARGET_U:
            out.extend((key, +1, "protected_U8_support") for key in keys)
        else:
            key = min(keys, key=vals.__getitem__)
            assert vals[key] < 0, (feature, vals[key])
            out.append((key, -1, "nonunstable_vertex_witness"))
    for feature, keys in groups["edge"].items():
        if feature in EXTRA_H:
            continue
        key = min(keys, key=vals.__getitem__)
        assert vals[key] < 0, (feature, vals[key])
        out.append((key, -1, "nonsaddle_edge_witness"))
    out.extend((key, +1, "support_slack") for key in topology)
    return out


def displacement_matrix(ids, modes):
    rows = []
    for i in ids:
        for axis in range(3):
            rows.append([mode[i][axis] for mode in modes])
    return np.asarray(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bound", type=float, default=20.0)
    ap.add_argument("--trust", type=float, default=None,
                    help="optional max absolute coordinate displacement at unit death time")
    ap.add_argument("--jacobian-only", action="store_true")
    args = ap.parse_args()
    base = load_points()
    res, vals = baseline.primitive_ledger(base)
    assert (len(res.active), len(res.edges), len(res.faces)) == (61, 162, 103)
    assert (len(res.stable), len(res.unstable), len(res.saddles)) == (2, 2, 2)
    assert {frozenset(res.faces[i]["cycle"]) for i, _ in res.stable} == {BASE_FACE, EXTRA_FACE}
    assert {i for i, _ in res.unstable} == {TARGET_U, EXTRA_U}
    assert {e for e, _ in res.saddles} == EXTRA_H

    modes, meta = build_modes(base, res)
    keys, key_index, jac, failures = baseline.finite_difference(base, vals, modes, h=1e-9)
    displacement = displacement_matrix(sorted(base), modes)
    np.savez_compressed(
        HERE / "row54_guarded_jacobian.npz",
        jacobian=jac,
        primitive_keys=np.asarray([repr(key) for key in keys], dtype=object),
        primitive_values=np.asarray([vals[key] for key in keys]),
        mode_meta=np.asarray([json.dumps(record, sort_keys=True) for record in meta], dtype=object),
        displacement=displacement,
    )
    if args.jacobian_only:
        print("saved row54_guarded_jacobian.npz", jac.shape, "failures", failures, flush=True)
        return
    guards = chosen_guards(vals)
    guard_rows, guard_info = [], []
    for key, sign, kind in guards:
        guard_rows.append(-sign * jac[key_index[key]] / max(abs(vals[key]), 1e-12))
        guard_info.append({"key": repr(key), "kind": kind, "value": vals[key], "sign": sign})
    guard_rows = np.asarray(guard_rows)
    n = len(modes)
    common_a = [np.hstack((guard_rows, -np.ones((len(guard_rows), 1))))]
    common_b = [np.zeros(len(guard_rows))]
    if args.trust is not None:
        disp = displacement
        common_a.extend((np.hstack((disp, np.zeros((len(disp), 1)))),
                         np.hstack((-disp, np.zeros((len(disp), 1))))))
        common_b.extend((np.full(len(disp), args.trust), np.full(len(disp), args.trust)))
    common_a = np.vstack(common_a)
    common_b = np.concatenate(common_b)
    objective = np.r_[np.zeros(n), 1.0]
    bounds = [(-args.bound, args.bound)] * n + [(-1000.0, 1000.0)]

    packets = []
    for kind, feature in (("face", EXTRA_FACE), ("vertex", EXTRA_U)):
        if kind == "face":
            packets.append([key for key in vals if key[0] == kind and frozenset(key[1]) == feature])
        else:
            packets.append([key for key in vals if key[0] == kind and key[1] == feature])
    packets.extend([
        [key for key in vals if key[0] == "edge" and key[1] == (6, 7)],
        [key for key in vals if key[0] == "edge" and key[1] == (9, 10)],
    ])
    assert [len(packet) for packet in packets] == [3, 4, 4, 4]
    results = []
    for fkey in packets[0]:
        for ukey in packets[1]:
            for h67 in packets[2]:
                for h910 in packets[3]:
                    deaths = [fkey, ukey, h67, h910]
                    rows = [jac[key_index[key]] / vals[key] for key in deaths]
                    a = np.vstack((common_a, *[np.r_[row, 0.0] for row in rows]))
                    b = np.r_[common_b, np.full(4, -1.0)]
                    lp = linprog(objective, A_ub=a, b_ub=b, bounds=bounds, method="highs")
                    record = {"deaths": [repr(key) for key in deaths], "success": bool(lp.success),
                              "message": lp.message}
                    if lp.success:
                        coeff = lp.x[:n]
                        worsening = guard_rows @ coeff
                        order = np.argsort(worsening)[-20:][::-1]
                        active = np.argsort(np.abs(coeff))[-24:][::-1]
                        record.update(
                            delta=float(lp.x[-1]),
                            fractional_death_derivatives=[float(row @ coeff) for row in rows],
                            coefficients=[float(z) for z in coeff],
                            l1_coefficient=float(np.sum(np.abs(coeff))),
                            max_coordinate_displacement=float(np.max(np.abs(displacement @ coeff))),
                            top_guard_blockers=[{**guard_info[i], "fractional_worsening": float(worsening[i])}
                                                for i in order],
                            active_modes=[{"column": int(i), "coefficient": float(coeff[i]), **meta[i]}
                                          for i in active],
                        )
                        if lp.ineqlin.marginals is not None:
                            dual = -np.asarray(lp.ineqlin.marginals[: len(guards)])
                            order_dual = np.argsort(dual)[-20:][::-1]
                            record["top_dual_guards"] = [
                                {**guard_info[i], "dual_weight": float(dual[i])}
                                for i in order_dual if dual[i] > 1e-10
                            ]
                    results.append(record)
    results.sort(key=lambda item: item.get("delta", 1e100))
    suffix = f"bound{args.bound:g}" + ("" if args.trust is None else f"_trust{args.trust:g}")
    out = {
        "version": 1,
        "scope": "rail-valid row54 endpoint complete four-death guarded LP",
        "baseline": {
            "f_vector": [len(res.active), len(res.edges), len(res.faces)],
            "class": [len(res.stable), len(res.unstable), len(res.saddles)],
            "topology_margin": res.topology_margin,
        },
        "bound": args.bound,
        "trust": args.trust,
        "modes": len(modes),
        "primitive_rows": len(keys),
        "guard_rows": len(guards),
        "finite_difference_failures": failures,
        "atlas": results,
    }
    path = HERE / f"row54_guarded_lp_{suffix}.json"
    path.write_text(json.dumps(out, indent=2))
    best = results[0]
    print("baseline", out["baseline"], flush=True)
    print("modes/primitives/guards/atlas", len(modes), len(keys), len(guards), len(results), flush=True)
    print("best delta", best.get("delta"), "max displacement", best.get("max_coordinate_displacement"), flush=True)
    print("deaths", best["deaths"], flush=True)
    for blocker in best.get("top_guard_blockers", [])[:12]:
        print("blocker", blocker["fractional_worsening"], blocker["kind"], blocker["key"], flush=True)


if __name__ == "__main__":
    main()
