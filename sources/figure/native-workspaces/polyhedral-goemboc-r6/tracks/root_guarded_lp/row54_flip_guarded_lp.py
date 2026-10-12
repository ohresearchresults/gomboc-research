#!/usr/bin/env python3
"""Complete fixed-cell guarded LP for the clean row-54 compensating flip.

The materialized adjacent cell has the enlarged base and protected U8, while
its four residual equilibria are S[198,243,244], U2, H(4,5), and H(12,13).
This script differentiates every mechanical primitive and every actual
point/face support slack through graph, complete defect-star, linear, and
projective modes.  It enumerates every primitive component by which all four
residual equilibria could die and minimizes the first normalized guard loss.
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
from collections import defaultdict
from pathlib import Path
from types import SimpleNamespace

import numpy as np
from scipy.optimize import linprog

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

spec = importlib.util.spec_from_file_location("baseline_guarded", HERE / "baseline_guarded_lp.py")
baseline = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(baseline)

core_spec = importlib.util.spec_from_file_location(
    "row54_core", ROOT / "tracks/circuit_atlas/row54_four_residual_search.py"
)
core = importlib.util.module_from_spec(core_spec)
assert core_spec.loader is not None
core_spec.loader.exec_module(core)

BASE_FACE = frozenset(range(17)) | {54}
EXTRA_FACE = frozenset((198, 243, 244))
TARGET_U = 8
EXTRA_U = 2
EXTRA_H = {(4, 5), (12, 13)}


def load_points() -> dict[int, np.ndarray]:
    out: dict[int, np.ndarray] = {}
    path = ROOT / "tracks/circuit_atlas/row54_multiwall_flip.csv"
    with path.open() as fh:
        for row in csv.DictReader(fh):
            out[int(row["source_id"])] = np.asarray(
                [float(row[k]) for k in ("x", "y", "z")], dtype=float
            )
    return out


def load_faces() -> list[list[int]]:
    return json.loads(
        (ROOT / "tracks/circuit_atlas/row54_multiwall_flip_faces.json").read_text()
    )


def primitive_ledger(points: dict[int, np.ndarray], faces: list[list[int]]):
    """Fixed-actual-cell primitive ledger using the independently audited faces.

    The generic fifth-cell evaluator intentionally merges planes at a 1e-8
    search tolerance.  This adjacent cell has a genuine 2.76e-10 support gap,
    so that evaluator merges distinct faces.  Here the already materialized
    103 maximal cycles are held fixed and every primitive is recomputed from
    those cycles.  A fresh Qhull equality check is still made at the baseline.
    """
    ids = sorted(points)
    array = np.asarray([points[i] for i in ids], dtype=float)
    index = {i: k for k, i in enumerate(ids)}
    mechanics = core.mechanics(ids, array, faces)
    edge_faces, neighbors = core.edge_lattice(faces)
    centroid = mechanics["centroid"]
    centered = {i: points[i] - centroid for i in ids}
    normals = core.face_normals(ids, array, faces)
    vals: dict[tuple, float] = {}
    topology_values = []

    for face_index, (cycle, normal0) in enumerate(zip(faces, normals)):
        face_key = tuple(sorted(cycle))
        for edge, value in zip(
            [tuple(sorted((a, b))) for a, b in zip(cycle, cycle[1:] + cycle[:1])],
            mechanics["fcomponents"][face_index],
        ):
            vals[("face", face_key, edge)] = float(value)
        normal = np.asarray(normal0, dtype=float)
        normal /= np.linalg.norm(normal)
        support = float(np.dot(normal, points[cycle[0]]))
        cset = set(cycle)
        for i in ids:
            if i not in cset:
                gap = support - float(np.dot(normal, points[i]))
                vals[("topology", face_key, i)] = gap
                topology_values.append(gap)

    for i in mechanics["active"]:
        xi = centered[i]
        for j in sorted(neighbors[i]):
            direction = centered[j] - xi
            vals[("vertex", i, j)] = -float(np.dot(xi, direction)) / (
                np.linalg.norm(xi) * np.linalg.norm(direction)
            )

    for edge, components in mechanics["ecomponents"].items():
        for label, value in zip(("t", "one_minus_t", "beta1", "beta2"), components):
            vals[("edge", edge, label)] = float(value)

    stable = [(k, float(value)) for k, value in enumerate(mechanics["fdec"]) if value > 0.0]
    unstable = [(i, float(value)) for i, value in mechanics["udec"].items() if value > 0.0]
    saddles = [(edge, float(value)) for edge, value in mechanics["edec"].items() if value > 0.0]
    result = SimpleNamespace(
        active=mechanics["active"],
        edges=sorted(edge_faces),
        faces=[{"cycle": list(cycle)} for cycle in faces],
        neighbors=neighbors,
        stable=stable,
        unstable=unstable,
        saddles=saddles,
        centroid=centroid,
        topology_margin=float(min(topology_values)),
    )
    return result, vals


def finite_difference(base, faces, base_vals, modes, h):
    keys = list(base_vals)
    key_index = {key: i for i, key in enumerate(keys)}
    jacobian = np.zeros((len(keys), len(modes)))
    failures = []
    for column, mode in enumerate(modes):
        plus = {i: base[i] + h * mode[i] for i in base}
        minus = {i: base[i] - h * mode[i] for i in base}
        try:
            _, vp = primitive_ledger(plus, faces)
            _, vm = primitive_ledger(minus, faces)
            if set(vp) != set(base_vals) or set(vm) != set(base_vals):
                raise RuntimeError("primitive key set changed")
            for key in keys:
                jacobian[key_index[key], column] = (vp[key] - vm[key]) / (2.0 * h)
        except Exception as exc:
            failures.append((column, repr(exc)))
    return keys, key_index, jacobian, failures


def graph_modes(base, res, count=16):
    active = sorted(res.active)
    free = [i for i in active if i not in BASE_FACE]
    index = {v: k for k, v in enumerate(free)}
    laplacian = np.zeros((len(free), len(free)))
    for i in free:
        ii = index[i]
        for j in res.neighbors[i]:
            laplacian[ii, ii] += 1.0
            if j in index:
                laplacian[ii, index[j]] -= 1.0
    values, vectors = np.linalg.eigh(laplacian)
    modes, meta = [], []
    for rank, col in enumerate(np.argsort(values)[: min(count, len(values))]):
        scalar = vectors[:, col]
        scalar /= max(np.max(np.abs(scalar)), 1e-300)
        for axis in range(3):
            mode = {i: np.zeros(3) for i in base}
            for i in free:
                mode[i][axis] = scalar[index[i]]
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

    # Span the complete one-rings of all four residual features, plus the
    # established remote carrier controls.  Base vertices move only in-plane.
    local_rows = set(EXTRA_FACE) | {EXTRA_U}
    for a, b in EXTRA_H:
        local_rows.update((a, b))
    for i in tuple(local_rows):
        local_rows.update(res.neighbors[i])
    local_rows.update((54, 69, 88, 224, 228, 232, 242, 245, 246, 248, 258))

    p0, p1, p2 = (base[i] for i in (0, 1, 2))
    tangent_u = p1 - p0
    tangent_u /= np.linalg.norm(tangent_u)
    normal = np.cross(p1 - p0, p2 - p0)
    normal /= np.linalg.norm(normal)
    tangent_v = np.cross(normal, tangent_u)
    tangent_v /= np.linalg.norm(tangent_v)

    for i in sorted(local_rows):
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
    return modes, meta, sorted(local_rows)


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
            assert vals[key] < 0, ("unexpected stable face", feature, vals[key])
            out.append((key, -1, "nonstable_face_witness"))
    for feature, keys in groups["vertex"].items():
        if feature == EXTRA_U:
            continue
        if feature == TARGET_U:
            out.extend((key, +1, "protected_U8_support") for key in keys)
        else:
            key = min(keys, key=vals.__getitem__)
            assert vals[key] < 0, ("unexpected unstable vertex", feature, vals[key])
            out.append((key, -1, "nonunstable_vertex_witness"))
    for feature, keys in groups["edge"].items():
        if feature in EXTRA_H:
            continue
        key = min(keys, key=vals.__getitem__)
        assert vals[key] < 0, ("unexpected saddle edge", feature, vals[key])
        out.append((key, -1, "nonsaddle_edge_witness"))
    out.extend((key, +1, "support_slack") for key in topology)
    return out


def displacement_matrix(ids, modes):
    return np.asarray([
        [mode[i][axis] for mode in modes]
        for i in ids for axis in range(3)
    ])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=float, default=20.0)
    parser.add_argument("--trust", type=float, default=None,
                        help="max absolute coordinate displacement at unit death time")
    parser.add_argument("--fd-step", type=float, default=1e-8)
    parser.add_argument("--jacobian-only", action="store_true")
    parser.add_argument("--reuse-jacobian", action="store_true",
                        help="reuse the audited Jacobian cache instead of redifferentiating")
    parser.add_argument("--branch-mod", type=int, default=1,
                        help="solve only atlas indices congruent to branch-rem modulo this value")
    parser.add_argument("--branch-rem", type=int, default=0)
    parser.add_argument("--progress", action="store_true")
    parser.add_argument("--method", choices=("highs", "highs-ds", "highs-ipm"), default="highs")
    args = parser.parse_args()
    if args.branch_mod < 1 or not 0 <= args.branch_rem < args.branch_mod:
        parser.error("require branch_mod >= 1 and 0 <= branch_rem < branch_mod")

    base = load_points()
    faces = load_faces()
    ids = sorted(base)
    array = np.asarray([base[i] for i in ids])
    fresh_hull, fresh_faces, _ = core.group_maximal_faces(ids, array)
    assert len(fresh_hull.vertices) == 61
    assert {frozenset(cycle) for cycle in fresh_faces} == {frozenset(cycle) for cycle in faces}
    res, vals = primitive_ledger(base, faces)
    assert (len(res.active), len(res.edges), len(res.faces)) == (61, 162, 103)
    assert (len(res.stable), len(res.unstable), len(res.saddles)) == (2, 2, 2)
    assert {frozenset(res.faces[i]["cycle"]) for i, _ in res.stable} == {BASE_FACE, EXTRA_FACE}
    assert {i for i, _ in res.unstable} == {TARGET_U, EXTRA_U}
    assert {e for e, _ in res.saddles} == EXTRA_H

    modes, meta, local_rows = build_modes(base, res)
    displacement = displacement_matrix(sorted(base), modes)
    cache = HERE / "row54_flip_guarded_jacobian.npz"
    if args.reuse_jacobian:
        saved = np.load(cache, allow_pickle=True)
        keys = list(vals)
        expected_keys = [repr(key) for key in keys]
        if list(saved["primitive_keys"]) != expected_keys:
            raise RuntimeError("cached primitive-key order does not match the rebuilt ledger")
        if saved["jacobian"].shape != (len(keys), len(modes)):
            raise RuntimeError("cached Jacobian shape does not match the rebuilt modes")
        jacobian = np.asarray(saved["jacobian"], dtype=float)
        if not np.array_equal(np.asarray(saved["displacement"]), displacement):
            raise RuntimeError("cached displacement matrix does not match rebuilt modes")
        key_index = {key: i for i, key in enumerate(keys)}
        failures = []
    else:
        keys, key_index, jacobian, failures = finite_difference(
            base, faces, vals, modes, h=args.fd_step
        )
        np.savez_compressed(
            cache,
            jacobian=jacobian,
            primitive_keys=np.asarray([repr(key) for key in keys], dtype=object),
            primitive_values=np.asarray([vals[key] for key in keys]),
            mode_meta=np.asarray([json.dumps(record, sort_keys=True) for record in meta], dtype=object),
            displacement=displacement,
        )
    if args.jacobian_only:
        print("saved", cache.name, jacobian.shape, "failures", failures, flush=True)
        return

    guards = chosen_guards(vals)
    guard_rows, guard_info = [], []
    for key, sign, kind in guards:
        guard_rows.append(-sign * jacobian[key_index[key]] / max(abs(vals[key]), 1e-12))
        guard_info.append({"key": repr(key), "kind": kind, "value": vals[key], "sign": sign})
    guard_rows = np.asarray(guard_rows)

    n = len(modes)
    common_a = [np.hstack((guard_rows, -np.ones((len(guard_rows), 1))))]
    common_b = [np.zeros(len(guard_rows))]
    if args.trust is not None:
        common_a.extend((
            np.hstack((displacement, np.zeros((len(displacement), 1)))),
            np.hstack((-displacement, np.zeros((len(displacement), 1)))),
        ))
        common_b.extend((
            np.full(len(displacement), args.trust),
            np.full(len(displacement), args.trust),
        ))
    common_a = np.vstack(common_a)
    common_b = np.concatenate(common_b)

    packets = [
        [key for key in vals if key[0] == "face" and frozenset(key[1]) == EXTRA_FACE],
        [key for key in vals if key[0] == "vertex" and key[1] == EXTRA_U],
        [key for key in vals if key[0] == "edge" and key[1] == (4, 5)],
        [key for key in vals if key[0] == "edge" and key[1] == (12, 13)],
    ]
    assert len(packets[0]) == 3
    assert all(len(packet) == 4 for packet in packets[2:])

    objective = np.r_[np.zeros(n), 1.0]
    bounds = [(-args.bound, args.bound)] * n + [(-1000.0, 1000.0)]
    results = []
    branch_index = 0
    for fkey in packets[0]:
        for ukey in packets[1]:
            for h45 in packets[2]:
                for h1213 in packets[3]:
                    current_branch = branch_index
                    branch_index += 1
                    if current_branch % args.branch_mod != args.branch_rem:
                        continue
                    deaths = [fkey, ukey, h45, h1213]
                    death_rows = [jacobian[key_index[key]] / vals[key] for key in deaths]
                    a_ub = np.vstack((common_a, *[np.r_[row, 0.0] for row in death_rows]))
                    b_ub = np.r_[common_b, np.full(4, -1.0)]
                    solve = linprog(objective, A_ub=a_ub, b_ub=b_ub,
                                    bounds=bounds, method=args.method)
                    record = {
                        "branch_index": current_branch,
                        "deaths": [repr(key) for key in deaths],
                        "success": bool(solve.success),
                        "message": solve.message,
                    }
                    if solve.success:
                        coefficient = solve.x[:n]
                        worsening = guard_rows @ coefficient
                        order = np.argsort(worsening)[-24:][::-1]
                        active = np.argsort(np.abs(coefficient))[-28:][::-1]
                        record.update(
                            delta=float(solve.x[-1]),
                            coefficients=[float(z) for z in coefficient],
                            fractional_death_derivatives=[float(row @ coefficient) for row in death_rows],
                            l1_coefficient=float(np.sum(np.abs(coefficient))),
                            max_coordinate_displacement=float(np.max(np.abs(displacement @ coefficient))),
                            top_guard_blockers=[
                                {**guard_info[i], "fractional_worsening": float(worsening[i])}
                                for i in order
                            ],
                            active_modes=[
                                {"column": int(i), "coefficient": float(coefficient[i]), **meta[i]}
                                for i in active
                            ],
                        )
                        if solve.ineqlin.marginals is not None:
                            dual = -np.asarray(solve.ineqlin.marginals[: len(guards)])
                            dual_order = np.argsort(dual)[-24:][::-1]
                            record["top_dual_guards"] = [
                                {**guard_info[i], "dual_weight": float(dual[i])}
                                for i in dual_order if dual[i] > 1e-10
                            ]
                    results.append(record)
                    if args.progress:
                        print(
                            "branch", current_branch,
                            "success", bool(solve.success),
                            "delta", None if not solve.success else float(solve.x[-1]),
                            flush=True,
                        )

    results.sort(key=lambda item: item.get("delta", 1e100))
    suffix = f"bound{args.bound:g}" + ("" if args.trust is None else f"_trust{args.trust:g}")
    if args.branch_mod != 1:
        suffix += f"_chunk{args.branch_rem}of{args.branch_mod}"
    if args.method != "highs":
        suffix += f"_{args.method}"
    output = {
        "version": 1,
        "scope": "clean row54 compensating-flip cell complete four-death guarded LP",
        "baseline": {
            "coordinates": "tracks/circuit_atlas/row54_multiwall_flip.csv",
            "f_vector": [len(res.active), len(res.edges), len(res.faces)],
            "class": [len(res.stable), len(res.unstable), len(res.saddles)],
            "topology_margin": res.topology_margin,
            "stable_faces": [sorted(feature) for feature in (BASE_FACE, EXTRA_FACE)],
            "unstable_vertices": sorted((TARGET_U, EXTRA_U)),
            "saddle_edges": sorted(EXTRA_H),
        },
        "bound": args.bound,
        "trust": args.trust,
        "fd_step": args.fd_step,
        "modes": len(modes),
        "local_rows": local_rows,
        "primitive_rows": len(keys),
        "guard_rows": len(guards),
        "atlas_total_branches": branch_index,
        "branch_mod": args.branch_mod,
        "branch_rem": args.branch_rem,
        "solver_method": args.method,
        "finite_difference_failures": failures,
        "atlas": results,
    }
    path = HERE / f"row54_flip_guarded_lp_{suffix}.json"
    path.write_text(json.dumps(output, indent=2))
    feasible = [item for item in results if item["success"]]
    print("baseline", output["baseline"], flush=True)
    print("modes/primitives/guards/atlas", len(modes), len(keys), len(guards), len(results), flush=True)
    print("failures", failures, flush=True)
    print("feasible", len(feasible), flush=True)
    if feasible:
        best = feasible[0]
        print("best delta", best["delta"], "max displacement", best["max_coordinate_displacement"], flush=True)
        print("deaths", best["deaths"], flush=True)
        for blocker in best.get("top_dual_guards", [])[:12]:
            print("dual", blocker["dual_weight"], blocker["kind"], blocker["key"], flush=True)


if __name__ == "__main__":
    main()
