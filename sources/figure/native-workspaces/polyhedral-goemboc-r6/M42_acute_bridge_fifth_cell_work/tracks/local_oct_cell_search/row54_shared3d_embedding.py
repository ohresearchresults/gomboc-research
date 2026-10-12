#!/usr/bin/env python3
"""Embed a shared three-control replacement in the rail-valid row-54 far cell.

The source cell is the independently rebuilt row54_far_rebuilt realization:

    S = base, [7,8,246]
    U = 8, 54
    H = (6,7), (9,10).

Local coordinates have 13 DOF: q246 moves in R^3, while rows 54,6,7,9,10
move in the two-dimensional base plane.  Four minimum-norm target actuators
are computed from the finite Jacobian.  The requested shared 3-D replacement
keeps the S actuator, the U54 actuator, and couples the two H actuators into a
single column which has unit first derivative on both H67 and H910.

Both the complete 13-D linearized system and its shared 3-D restriction are
tested against every support slack, base/U8/rail guard and fixed anti-birth
witness.  A fresh-hull nonlinear search then permits bistellar transitions.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution, linprog, minimize
from scipy.spatial import ConvexHull


HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[2]
ATLAS = PROJECT / "tracks" / "circuit_atlas"
sys.path.insert(0, str(ATLAS))
import row54_four_residual_search as carrier  # noqa: E402
import materialize_row54_cells as materializer  # noqa: E402

SOURCE = ATLAS / "row54_far_rebuilt.csv"
FACES_SOURCE = ATLAS / "row54_far_rebuilt_faces.json"
BASE = frozenset(range(17)) | {54}
EXTRA_STABLE = frozenset((7, 8, 246))
TARGET_U = 54
PROTECTED_U = 8
TARGET_H = ((6, 7), (9, 10))
LOCAL_ROWS = (246, 54, 6, 7, 9, 10)
BASE_MOVED = (54, 6, 7, 9, 10)


def load_cell():
    rows = {}
    with SOURCE.open() as f:
        for row in csv.DictReader(f):
            rows[int(row["source_id"])] = np.array(
                [float(row[k]) for k in ("x", "y", "z")], dtype=float
            )
    ids = tuple(sorted(rows))
    p = np.array([rows[i] for i in ids])
    faces = tuple(tuple(x) for x in json.load(FACES_SOURCE.open()))
    return ids, p, faces


IDS, P0, FACES = load_cell()
IX = {i: k for k, i in enumerate(IDS)}
EF, NBR = carrier.edge_lattice(FACES)
ACTIVE = sorted(set().union(*(set(c) for c in FACES)))
BASE_I = next(i for i, c in enumerate(FACES) if frozenset(c) == BASE)
SF_I = next(i for i, c in enumerate(FACES) if frozenset(c) == EXTRA_STABLE)
FORCED_RAILS = materializer.forced_rail_edges()


def local_coordinate_map() -> tuple[np.ndarray, dict]:
    """Map 13 parameters to all coordinate displacements."""
    normals = carrier.face_normals(IDS, P0, FACES)
    n = normals[BASE_I] / np.linalg.norm(normals[BASE_I])
    u = P0[IX[1]] - P0[IX[0]]
    u = u / np.linalg.norm(u)
    v = np.cross(n, u)
    v = v / np.linalg.norm(v)
    m = np.zeros((len(IDS) * 3, 13))
    # q246: free xyz.
    for k in range(3):
        m[3 * IX[246] + k, k] = 1.0
    col = 3
    for row in BASE_MOVED:
        m[3 * IX[row]:3 * IX[row] + 3, col] = u
        m[3 * IX[row]:3 * IX[row] + 3, col + 1] = v
        col += 2
    return m, {"base_normal": n.tolist(), "base_u": u.tolist(), "base_v": v.tolist()}


COORD_MAP, COORD_CHART = local_coordinate_map()


def points(z: np.ndarray) -> np.ndarray:
    return P0 + (COORD_MAP @ np.asarray(z, dtype=float)).reshape((-1, 3))


def normalized_supports(p: np.ndarray, centroid: np.ndarray, row: int) -> dict[int, float]:
    x = p - centroid
    i = IX[row]
    out = {}
    for jrow in sorted(NBR[row]):
        j = IX[jrow]
        d = x[j] - x[i]
        out[jrow] = -float(np.dot(x[i], d)) / (np.linalg.norm(x[i]) * np.linalg.norm(d))
    return out


def directed_rail_guards(p: np.ndarray, centroid: np.ndarray) -> dict[str, float]:
    x = p - centroid
    out = {}
    short = [228] + list(range(229, 247)) + [8]
    long = [228] + list(range(247, 265)) + [8]
    for name, path in (("short", short), ("long", long)):
        for a, b in zip(path, path[1:]):
            edge = tuple(sorted((a, b)))
            if edge not in FORCED_RAILS:
                continue
            xa, xb = x[IX[a]], x[IX[b]]
            d = xb - xa
            out[f"rail:{name}:{a}->{b}"] = float(np.dot(xa, d)) / (
                np.linalg.norm(xa) * np.linalg.norm(d)
            )
    return out


def mechanics_fixed(z: np.ndarray):
    p = points(z)
    m = carrier.mechanics(IDS, p, FACES)
    return p, m


def make_templates():
    _, m = mechanics_fixed(np.zeros(13))
    u54 = normalized_supports(P0, m["centroid"], 54)
    target = {
        "stable_component": int(np.argmin(m["fcomponents"][SF_I])),
        "u54_neighbor": min(u54, key=u54.get),
        "h_components": {e: int(np.argmin(m["ecomponents"][e])) for e in TARGET_H},
    }
    anti = {
        "face": {fi: int(np.argmin(vals)) for fi, vals in enumerate(m["fcomponents"])
                 if fi not in (BASE_I, SF_I)},
        "vertex": {},
        "edge": {e: int(np.argmin(vals)) for e, vals in m["ecomponents"].items()
                 if e not in TARGET_H},
    }
    for row in ACTIVE:
        if row in (PROTECTED_U, TARGET_U):
            continue
        vals = normalized_supports(P0, m["centroid"], row)
        anti["vertex"][row] = min(vals, key=vals.get)
    return target, anti


TARGET_TEMPLATE, ANTI_TEMPLATE = make_templates()


def detailed_features(z: np.ndarray):
    """All inequalities in good-positive convention, deterministically ordered."""
    p, m = mechanics_fixed(z)
    target_names = ["S[7,8,246]-death", "U54-death", "H67-death", "H910-death"]
    u54 = normalized_supports(p, m["centroid"], 54)
    target = np.array([
        -m["fcomponents"][SF_I][TARGET_TEMPLATE["stable_component"]],
        -u54[TARGET_TEMPLATE["u54_neighbor"]],
        -m["ecomponents"][(6, 7)][TARGET_TEMPLATE["h_components"][(6, 7)]],
        -m["ecomponents"][(9, 10)][TARGET_TEMPLATE["h_components"][(9, 10)]],
    ], dtype=float)

    names, guards = [], []
    normals = carrier.face_normals(IDS, p, FACES)
    # Every support-plane slack.  Base coplanarity is exact by construction.
    for fi, (cyc, n0) in enumerate(zip(FACES, normals)):
        n = n0 / np.linalg.norm(n0)
        h = float(np.dot(n, p[IX[cyc[0]]]))
        cset = set(cyc)
        for row in IDS:
            if row in cset:
                continue
            names.append(f"topology:f{fi}:row{row}")
            guards.append(h - float(np.dot(n, p[IX[row]])))
    for k, value in enumerate(m["fcomponents"][BASE_I]):
        names.append(f"base:c{k}"); guards.append(float(value))
    for row, value in normalized_supports(p, m["centroid"], 8).items():
        names.append(f"U8:to{row}"); guards.append(float(value))
    # The rebuilt row54 certificate calls these rails in the structural sense:
    # all forced true edges are present.  Several inherited directions are no
    # longer monotone after the robust projective/SPD map, so their dot-product
    # signs are not imposed.  The complete support-slack list above is the
    # fixed-chamber edge-preservation guard.
    for fi, k in sorted(ANTI_TEMPLATE["face"].items()):
        names.append(f"antiface:f{fi}:c{k}"); guards.append(-float(m["fcomponents"][fi][k]))
    for row, nbr in sorted(ANTI_TEMPLATE["vertex"].items()):
        vals = normalized_supports(p, m["centroid"], row)
        names.append(f"antivertex:v{row}:to{nbr}"); guards.append(-float(vals[nbr]))
    for edge, k in sorted(ANTI_TEMPLATE["edge"].items()):
        names.append(f"antiedge:{edge[0]}-{edge[1]}:c{k}")
        guards.append(-float(m["ecomponents"][edge][k]))
    return target_names, target, names, np.asarray(guards)


def finite_jacobian(fun, x0, h=1e-7):
    y0 = np.asarray(fun(x0), dtype=float)
    j = np.empty((len(y0), len(x0)))
    for k in range(len(x0)):
        xp, xm = x0.copy(), x0.copy(); xp[k] += h; xm[k] -= h
        j[:, k] = (np.asarray(fun(xp)) - np.asarray(fun(xm))) / (2 * h)
    return y0, j


def farkas(A: np.ndarray, b: np.ndarray, names: list[str]):
    dual = linprog(b, A_eq=np.vstack((A.T, np.ones(len(b)))),
                   b_eq=np.r_[np.zeros(A.shape[1]), 1.0],
                   bounds=[(0, None)] * len(b), method="highs")
    out = {"success": bool(dual.success), "message": dual.message}
    if dual.success:
        support = np.flatnonzero(dual.x > 1e-9)
        out.update({
            "b_dot_y": float(b @ dual.x),
            "at_y_inf": float(np.max(np.abs(A.T @ dual.x))),
            "sum_y": float(dual.x.sum()),
            "support": [{"name": names[int(i)], "weight": float(dual.x[i]),
                         "rhs": float(b[i])} for i in support],
        })
    return out


def solve_affine_lp(y0, jac, names, nt, basis=None, epsilon=1e-6):
    if basis is None:
        basis = np.eye(jac.shape[1])
    j = jac @ basis
    requested = np.r_[np.full(nt, epsilon), np.zeros(len(y0) - nt)]
    A = -j; b = y0 - requested
    sol = linprog(np.zeros(basis.shape[1]), A_ub=A, b_ub=b,
                  bounds=[(None, None)] * basis.shape[1], method="highs")
    out = {"success": bool(sol.success), "message": sol.message,
           "variables": basis.shape[1], "constraints": len(y0)}
    if sol.success:
        out["coefficients"] = sol.x.tolist()
        out["parameters"] = (basis @ sol.x).tolist()
        out["predicted_min"] = float(np.min(y0 + jac @ (basis @ sol.x) - requested))
    else:
        out["farkas"] = farkas(A, b, names)
    return out


def linear_analysis():
    x0 = np.zeros(13)
    tn, t0, gn, g0 = detailed_features(x0)
    def vec(z):
        tn1, t, gn1, g = detailed_features(z)
        assert tn1 == tn and gn1 == gn
        return np.r_[t, g]
    y0, jac = finite_jacobian(vec, x0)
    jt = jac[:4]
    sv = np.linalg.svd(jt, compute_uv=False)
    four = jt.T @ np.linalg.inv(jt @ jt.T)
    shared = np.column_stack((four[:, 0], four[:, 1], four[:, 2] + four[:, 3]))
    response = jt @ shared
    shared_h_derivative = jac @ shared[:, 2]
    first_walls = []
    for name, value, derivative in zip(gn, g0, shared_h_derivative[4:]):
        if value > 0.0 and derivative < -1e-12:
            first_walls.append({
                "name": name,
                "baseline_value": float(value),
                "directional_derivative": float(derivative),
                "linearized_coefficient": float(-value / derivative),
            })
    first_walls.sort(key=lambda item: item["linearized_coefficient"])
    target_zero_times = {}
    for name, value, derivative in zip(tn, t0, shared_h_derivative[:4]):
        target_zero_times[name] = (
            float(-value / derivative) if derivative > 1e-12 else None
        )
    names = ["target:" + x for x in tn] + ["guard:" + x for x in gn]
    full = solve_affine_lp(y0, jac, names, 4)
    shared_lp = solve_affine_lp(y0, jac, names, 4, shared)
    return {
        "coordinate_chart": COORD_CHART,
        "local_rows": LOCAL_ROWS,
        "degrees_of_freedom": 13,
        "target_template": {
            "stable_component": TARGET_TEMPLATE["stable_component"],
            "u54_neighbor": TARGET_TEMPLATE["u54_neighbor"],
            "h_components": {f"{a}-{b}": k for (a, b), k in TARGET_TEMPLATE["h_components"].items()},
        },
        "target_baseline_good_values": dict(zip(tn, t0.tolist())),
        "guard_count": len(g0),
        "guard_min": float(g0.min()),
        "guard_arg": gn[int(np.argmin(g0))],
        "target_jacobian_rank": int(np.linalg.matrix_rank(jt, tol=1e-8)),
        "target_jacobian_singular_values": sv.tolist(),
        "four_independent_actuators": four.tolist(),
        "shared3d_basis": shared.tolist(),
        "shared3d_target_response": response.tolist(),
        "shared_h_target_zero_times": target_zero_times,
        "shared_h_first_walls": first_walls[:12],
        "full13d_lp": full,
        "shared3d_lp": shared_lp,
    }


def fresh_score(z: np.ndarray):
    p = points(z)
    try:
        hull, faces, _ = carrier.group_maximal_faces(IDS, p)
        m = carrier.mechanics(IDS, p, faces)
    except Exception as exc:
        return -100.0, {"valid": False, "error": repr(exc)}
    fsets = [frozenset(c) for c in faces]
    base_i = next((i for i, c in enumerate(fsets) if c == BASE), None)
    base = -10.0 if base_i is None else float(m["fdec"][base_i])
    u8 = float(m["udec"].get(8, -10.0))
    fbad = max((float(v) for i, v in enumerate(m["fdec"]) if i != base_i), default=-10.0)
    ubad = max((float(v) for i, v in m["udec"].items() if i != 8), default=-10.0)
    hbad = max((float(v) for v in m["edec"].values()), default=-10.0)
    edge_set = set(m["ef"])
    missing = sorted(FORCED_RAILS - edge_set)
    rail = 1.0 if not missing else -10.0
    all_active = 1.0 if len(hull.vertices) == len(IDS) and m["active"] == list(IDS) else -10.0
    components = {
        "base": base, "U8": u8, "no_extra_stable": -fbad,
        "no_extra_unstable": -ubad, "no_saddle": -hbad,
        "rails": rail, "all_rows_active": all_active,
    }
    hard = min(components.values())
    stable = [list(faces[k]) for k, x in enumerate(m["fdec"]) if x > 1e-9]
    unstable = [i for i, x in m["udec"].items() if x > 1e-9]
    saddles = [list(e) for e, x in m["edec"].items() if x > 1e-9]
    return float(hard), {
        "valid": True, "hard": float(hard), "components": components,
        "f_vector": [len(hull.vertices), len(m["ef"]), len(faces)],
        "class": [len(stable), len(unstable), len(saddles)],
        "stable_faces": stable, "unstable_vertices": unstable, "saddle_edges": saddles,
        "missing_forced_rails": [list(e) for e in missing],
    }


def cross3(a, b):
    return np.array((a[1] * b[2] - a[2] * b[1],
                     a[2] * b[0] - a[0] * b[2],
                     a[0] * b[1] - a[1] * b[0]))


def fast_fresh_score(z: np.ndarray):
    """Allocation-light equivalent of fresh_score for global optimization."""
    p = points(z)
    try:
        hull = ConvexHull(p, qhull_options="Qt Qx")
    except Exception as exc:
        return -100.0, {"valid": False, "error": repr(exc)}
    eqs = np.asarray([eq / np.linalg.norm(eq[:3]) for eq in hull.equations])
    parent = list(range(len(hull.simplices)))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        return a
    def union(a, b):
        a, b = find(a), find(b)
        if a != b: parent[b] = a
    edge_tri = defaultdict(list)
    for k, tri in enumerate(hull.simplices):
        a, b, c = map(int, tri)
        for e in ((a, b), (b, c), (c, a)): edge_tri[tuple(sorted(e))].append(k)
    for inc in edge_tri.values():
        if len(inc) == 2:
            a, b = inc
            if np.max(np.abs(eqs[a] - eqs[b])) < 1e-10: union(a, b)
    groups = {}
    for k, tri in enumerate(hull.simplices):
        g = groups.setdefault(find(k), [eqs[k], set(), []])
        g[1].update(map(int, tri)); g[2].append(tuple(map(int, tri)))
    faces = []
    for eq, vertices, tris in groups.values():
        n = eq[:3]
        counts = defaultdict(int)
        for a, b, c in tris:
            for e in ((a, b), (b, c), (c, a)): counts[tuple(sorted(e))] += 1
        adj = defaultdict(list)
        for (a, b), count in counts.items():
            if count == 1: adj[a].append(b); adj[b].append(a)
        if not adj or any(len(v) != 2 for v in adj.values()):
            return -100.0, {"valid": False, "error": "bad boundary"}
        start = min(adj); cyc = [start]; prev = None; cur = start
        while True:
            a, b = adj[cur]; nxt = a if a != prev else b
            if nxt == start: break
            cyc.append(nxt); prev, cur = cur, nxt
            if len(cyc) > len(adj) + 1:
                return -100.0, {"valid": False, "error": "bad cycle"}
        area = np.zeros(3)
        for a, b in zip(cyc, cyc[1:] + cyc[:1]): area += cross3(p[a], p[b])
        if np.dot(area, n) < 0: cyc = [cyc[0]] + list(reversed(cyc[1:]))
        faces.append((cyc, n, float(eq[3])))

    d6 = 0.0; mint = np.zeros(3)
    for cyc, _, _ in faces:
        for j in range(1, len(cyc) - 1):
            a, b, c = p[cyc[0]], p[cyc[j]], p[cyc[j + 1]]
            d = float(np.dot(a, cross3(b, c))); d6 += d; mint += d * (a + b + c)
    if d6 < 0: d6 = -d6; mint = -mint
    if d6 <= 1e-14: return -100.0, {"valid": False, "error": "bad volume"}
    centroid = mint / (4 * d6); x = p - centroid

    ef = defaultdict(list); nbr = defaultdict(set)
    for fi, (cyc, _, _) in enumerate(faces):
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            e = tuple(sorted((a, b))); ef[e].append(fi); nbr[a].add(b); nbr[b].add(a)
    if any(len(v) != 2 for v in ef.values()):
        return -100.0, {"valid": False, "error": "nonmanifold"}
    fdec = []; base_i = None
    for fi, (cyc, n, off) in enumerate(faces):
        ids_set = frozenset(IDS[i] for i in cyc)
        if ids_set == BASE: base_i = fi
        h = -(off + float(np.dot(n, centroid))); foot = h * n
        ref = np.mean(x[cyc], axis=0); vals = []
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            e = x[b] - x[a]
            q = float(np.dot(cross3(e, foot - x[a]), n))
            if np.dot(cross3(e, ref - x[a]), n) < 0: q = -q
            vals.append(q / np.linalg.norm(e))
        fdec.append(min(vals))
    active = set(hull.vertices.tolist()); udec = {}
    for i in active:
        vals = []
        for j in nbr[i]:
            d = x[j] - x[i]
            vals.append(-float(np.dot(x[i], d)) / (np.linalg.norm(x[i]) * np.linalg.norm(d)))
        udec[i] = min(vals)
    edec = {}
    for (a, b), inc in ef.items():
        d = x[b] - x[a]; t = -float(np.dot(x[a], d)) / float(np.dot(d, d)); q = x[a] + t * d
        n1, n2 = faces[inc[0]][1], faces[inc[1]][1]
        aa, bb, cc = float(n1 @ n1), float(n1 @ n2), float(n2 @ n2)
        r1, r2 = float(q @ n1), float(q @ n2); den = aa * cc - bb * bb
        if den <= 1e-14 * aa * cc:
            return -100.0, {"valid": False, "error": "parallel faces"}
        b1 = (r1 * cc - r2 * bb) / den; b2 = (r2 * aa - r1 * bb) / den
        qn = max(float(q @ q), 1e-300)
        edec[(a, b)] = min(t, 1 - t, b1 * math.sqrt(aa / qn), b2 * math.sqrt(cc / qn))

    base = -10.0 if base_i is None else float(fdec[base_i])
    i8 = IX[8]; u8 = float(udec.get(i8, -10.0))
    fbad = max((v for i, v in enumerate(fdec) if i != base_i), default=-10.0)
    ubad = max((v for i, v in udec.items() if i != i8), default=-10.0)
    hbad = max(edec.values(), default=-10.0)
    edge_ids = {tuple(sorted((IDS[a], IDS[b]))) for a, b in ef}
    missing = sorted(FORCED_RAILS - edge_ids)
    components = {
        "base": base, "U8": u8, "no_extra_stable": -float(fbad),
        "no_extra_unstable": -float(ubad), "no_saddle": -float(hbad),
        "rails": 1.0 if not missing else -10.0,
        "all_rows_active": 1.0 if len(active) == len(IDS) else -10.0,
    }
    hard = min(components.values())
    stable = [[IDS[i] for i in faces[k][0]] for k, v in enumerate(fdec) if v > 1e-9]
    unstable = [IDS[i] for i, v in udec.items() if v > 1e-9]
    saddles = [[IDS[a], IDS[b]] for (a, b), v in edec.items() if v > 1e-9]
    return float(hard), {
        "valid": True, "hard": float(hard), "components": components,
        "f_vector": [len(active), len(ef), len(faces)],
        "class": [len(stable), len(unstable), len(saddles)],
        "stable_faces": stable, "unstable_vertices": unstable, "saddle_edges": saddles,
        "missing_forced_rails": [list(e) for e in missing],
    }


def nonlinear_shared3d(linear: dict, maxiter=35, seed=54246247):
    basis = np.asarray(linear["shared3d_basis"])
    bounds = [(-0.8, 1.5), (-0.8, 1.8), (-1.0, 2.5)]
    best = {"score": -math.inf}
    history = []
    def objective(a):
        z = basis @ np.asarray(a)
        score, detail = fast_fresh_score(z)
        if score > best["score"]:
            best.update(score=float(score), a=np.asarray(a).tolist(), z=z.tolist(), detail=detail)
            history.append({"score": float(score), "coefficients": np.asarray(a).tolist(), **detail})
        return -score
    de = differential_evolution(objective, bounds, seed=seed, popsize=12,
                                maxiter=maxiter, polish=False, workers=1,
                                updating="immediate", tol=1e-8, atol=1e-10,
                                x0=np.zeros(3))
    local = minimize(objective, de.x, method="Powell", bounds=bounds,
                     options={"maxiter": 800, "xtol": 1e-9, "ftol": 1e-11})
    z = np.asarray(best["z"])
    p = points(z)
    hull, faces, _ = carrier.group_maximal_faces(IDS, p)
    m, stable, unstable, saddles = carrier.classify(IDS, p, faces)
    return {
        "seed": int(seed),
        "maxiter": int(maxiter),
        "evaluations": int(de.nfev + local.nfev),
        "bounds": bounds,
        "best_score": float(best["score"]),
        "best_coefficients": best["a"],
        "best_parameters": best["z"],
        "best_summary": best["detail"],
        "fresh_audit": {
            "f_vector": [len(hull.vertices), len(m["ef"]), len(faces)],
            "active": m["active"], "centroid": m["centroid"].tolist(),
            "class": [len(stable), len(unstable), len(saddles)],
            "stable_faces": stable, "unstable_vertices": unstable,
            "saddle_edges": saddles,
        },
        "improvement_history": history,
    }


def pure_shared_h_scan(linear: dict):
    basis = np.asarray(linear["shared3d_basis"])
    records = []
    for coefficient in (0.0, 1.0e-6, 1.3e-6, 3.4e-6, 1.0e-3,
                        1.0e-2, 1.0e-1, 4.0e-1, 5.0e-1):
        z = basis @ np.array((0.0, 0.0, coefficient))
        score, detail = fast_fresh_score(z)
        # Qhull can split an almost coplanar polygon for a few ulps near a
        # wall.  The slower atlas grouping is the authoritative fallback.
        if not detail.get("valid", False):
            score, detail = fresh_score(z)
        records.append({"shared_h_coefficient": coefficient, "score": score, **detail})
    return {
        "interpretation": (
            "The shared H actuator has first-order response (0,0,1,1). "
            "Tiny coefficients expose the two carrier diagonal flips; large "
            "coefficients show H67/H910 transfer after the forced rails fail."
        ),
        "records": records,
    }


def write_endpoint(parameters: list[float], csv_path: Path, faces_path: Path):
    p = points(np.asarray(parameters, dtype=float))
    _, faces, _ = carrier.group_maximal_faces(IDS, p)
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(("source_id", "x", "y", "z"))
        for row, xyz in zip(IDS, p):
            writer.writerow((row, *map(float, xyz)))
    with faces_path.open("w") as f:
        json.dump([list(face) for face in faces], f, indent=2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=("linear", "search", "all"), default="all")
    ap.add_argument("--output", type=Path, default=HERE / "row54_shared3d_result.json")
    ap.add_argument("--endpoint-csv", type=Path,
                    default=HERE / "row54_shared3d_endpoint.csv")
    ap.add_argument("--endpoint-faces", type=Path,
                    default=HERE / "row54_shared3d_endpoint_faces.json")
    ap.add_argument("--seed", type=int, default=54246247)
    ap.add_argument("--maxiter", type=int, default=35)
    args = ap.parse_args()
    out = {"source": str(SOURCE), "faces_source": str(FACES_SOURCE)}
    linear = linear_analysis()
    out["linear"] = linear
    if args.mode in ("search", "all"):
        out["nonlinear_shared3d"] = nonlinear_shared3d(
            linear, maxiter=args.maxiter, seed=args.seed
        )
        out["pure_shared_h_scan"] = pure_shared_h_scan(linear)
        write_endpoint(out["nonlinear_shared3d"]["best_parameters"],
                       args.endpoint_csv, args.endpoint_faces)
        out["endpoint_csv"] = str(args.endpoint_csv.resolve())
        out["endpoint_faces"] = str(args.endpoint_faces.resolve())
    with args.output.open("w") as f:
        json.dump(out, f, indent=2, allow_nan=False)
    print(json.dumps(out, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
