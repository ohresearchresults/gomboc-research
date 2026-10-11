#!/usr/bin/env python3
"""Numerical/exactable local six-row search at the fifth-cell residual packet.

The moved rows form an octahedron with opposite pairs

    (198,247), (224,228), (258,229).

We use three genuinely different local objectives:

* kill the limiting foot component of stable face [198,224,258];
* kill a beta component of saddle edge (229,247), not an endpoint t component;
* put the own centroid strictly inside the six-row octahedron (relay overlap).

All reported candidates are audited against the fresh global hull.  The fixed-
chamber routines are also used to locate the first wall and to distinguish a
metric obstruction from a topology obstruction.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from collections import defaultdict
from dataclasses import asdict, dataclass
from itertools import combinations
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution, linprog, minimize
from scipy.spatial import ConvexHull


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ENDPOINT = ROOT / "fifth_cell_endpoint"
sys.path.insert(0, str(ROOT / "fourth_cell_endpoint"))
from numeric_hull_proposer import evaluate  # noqa: E402

CORE = (198, 224, 258, 229, 247, 228)
OPPOSITE = ((198, 247), (224, 228), (258, 229))
STABLE_FACE = frozenset((198, 224, 258))
SADDLE_EDGE = (229, 247)
BASE_FACE = frozenset(range(17))
TARGET_VERTEX = 8
SHORT_RAIL = (228, *range(229, 247), 8)
LONG_RAIL = (228, *range(247, 265), 8)


def read_points() -> dict[int, np.ndarray]:
    out: dict[int, np.ndarray] = {}
    with open(ENDPOINT / "input_rows_common_lattice.csv", newline="") as f:
        for row in csv.DictReader(f):
            scale = float(row["denominator"])
            out[int(row["source_id"])] = np.array(
                [float(row[k]) / scale for k in ("x_int", "y_int", "z_int")],
                dtype=float,
            )
    return out


POINTS0 = read_points()
IDS = tuple(sorted(POINTS0))
FACE_CYCLES = tuple(tuple(x) for x in json.load(open(ENDPOINT / "face_cycles.json")))
EDGE_FACES: dict[tuple[int, int], list[int]] = defaultdict(list)
NEIGHBORS: dict[int, set[int]] = defaultdict(set)
for fi, cyc in enumerate(FACE_CYCLES):
    for a, b in zip(cyc, cyc[1:] + cyc[:1]):
        edge = tuple(sorted((a, b)))
        EDGE_FACES[edge].append(fi)
        NEIGHBORS[a].add(b)
        NEIGHBORS[b].add(a)


def unit(v: np.ndarray) -> np.ndarray:
    return v / np.linalg.norm(v)


def points_from_x(x: np.ndarray) -> dict[int, np.ndarray]:
    pts = {i: p.copy() for i, p in POINTS0.items()}
    dx = np.asarray(x, dtype=float).reshape((len(CORE), 3))
    for i, d in zip(CORE, dx):
        pts[i] += d
    return pts


def oriented_plane(cyc: tuple[int, ...], pts: dict[int, np.ndarray]) -> tuple[np.ndarray, float]:
    a = pts[cyc[0]]
    normal = None
    for j in range(1, len(cyc) - 1):
        for k in range(j + 1, len(cyc)):
            trial = np.cross(pts[cyc[j]] - a, pts[cyc[k]] - a)
            if np.linalg.norm(trial) > 1e-14:
                normal = unit(trial)
                break
        if normal is not None:
            break
    if normal is None:
        raise ValueError("degenerate face")
    off = -float(np.dot(normal, a))
    # Baseline face cycles are outward.  Keep the side containing a fixed
    # reference row negative; this also remains meaningful near a wall.
    ref = next(i for i in IDS if i not in cyc and i not in CORE)
    if float(np.dot(normal, pts[ref]) + off) > 0:
        normal = -normal
        off = -off
    return normal, off


def fixed_faces(pts: dict[int, np.ndarray]) -> list[dict]:
    faces = []
    for cyc in FACE_CYCLES:
        n, off = oriented_plane(cyc, pts)
        # No moved core row belongs to a nonsimplicial face, so no hidden
        # coplanarity condition is being discarded here.
        err = max(abs(float(np.dot(n, pts[i]) + off)) for i in cyc)
        if err > 1e-8:
            raise ValueError(f"face coplanarity lost: {cyc}, {err}")
        faces.append({"cycle": cyc, "n": n, "off": off})
    return faces


def mass_centroid(pts: dict[int, np.ndarray], faces: list[dict]) -> tuple[float, np.ndarray]:
    d6 = 0.0
    m24 = np.zeros(3)
    for face in faces:
        cyc = face["cycle"]
        for j in range(1, len(cyc) - 1):
            a, b, c = (pts[i] for i in (cyc[0], cyc[j], cyc[j + 1]))
            d = float(np.dot(a, np.cross(b, c)))
            d6 += d
            m24 += d * (a + b + c)
    if d6 <= 0:
        raise ValueError("nonpositive oriented volume")
    return d6 / 6.0, m24 / (4.0 * d6)


def face_components(cyc: tuple[int, ...], n: np.ndarray, off: float,
                    pts: dict[int, np.ndarray], centroid: np.ndarray) -> np.ndarray:
    x = {i: pts[i] - centroid for i in cyc}
    h = -(off + float(np.dot(n, centroid)))
    foot = h * n
    ref = sum((x[i] for i in cyc), np.zeros(3)) / len(cyc)
    values = []
    for a, b in zip(cyc, cyc[1:] + cyc[:1]):
        edge = x[b] - x[a]
        z = float(np.dot(np.cross(edge, foot - x[a]), n))
        if float(np.dot(np.cross(edge, ref - x[a]), n)) < 0:
            z = -z
        values.append(z / np.linalg.norm(edge))
    return np.array(values)


def edge_components(edge: tuple[int, int], faces: list[dict], pts: dict[int, np.ndarray],
                    centroid: np.ndarray) -> np.ndarray:
    a, b = edge
    xa, xb = pts[a] - centroid, pts[b] - centroid
    direction = xb - xa
    t = -float(np.dot(xa, direction)) / float(np.dot(direction, direction))
    p = xa + t * direction
    f1, f2 = (faces[i] for i in EDGE_FACES[tuple(sorted(edge))])
    n1, n2 = f1["n"], f2["n"]
    aa, bb, cc = float(np.dot(n1, n1)), float(np.dot(n1, n2)), float(np.dot(n2, n2))
    r1, r2 = float(np.dot(p, n1)), float(np.dot(p, n2))
    den = aa * cc - bb * bb
    beta1 = (r1 * cc - r2 * bb) / den
    beta2 = (r2 * aa - r1 * bb) / den
    pn = max(float(np.linalg.norm(p)), 1e-300)
    return np.array((t, 1.0 - t, beta1 / pn, beta2 / pn))


def octahedron(pts: dict[int, np.ndarray], centroid: np.ndarray) -> dict:
    local = np.array([pts[i] - centroid for i in CORE])
    hull = ConvexHull(local, qhull_options="Qt Qx")
    facets = []
    inward = []
    for simplex, eq in zip(hull.simplices, hull.equations):
        ids = tuple(sorted(CORE[i] for i in simplex))
        slack = -float(eq[3])  # value at the origin, inward positive
        facets.append({"face": ids, "origin_inward_slack": slack})
        inward.append(slack)
    return {
        "vertices": tuple(CORE[i] for i in hull.vertices),
        "facets": tuple(sorted(facets, key=lambda z: z["face"])),
        "origin_inward_min": min(inward),
        "origin_inward": tuple(inward),
        "volume": float(hull.volume),
    }


BASE_OCT_FACETS = tuple(
    sorted(tuple(sorted(CORE[i] for i in s)) for s in ConvexHull(
        np.array([POINTS0[i] for i in CORE]), qhull_options="Qt Qx").simplices)
)


def octa_facet_slacks(pts: dict[int, np.ndarray], centroid: np.ndarray) -> np.ndarray:
    """Inward origin slacks for the eight baseline octahedron facets."""
    values = []
    for facet in BASE_OCT_FACETS:
        a, b, c = (pts[i] - centroid for i in facet)
        n = unit(np.cross(b - a, c - a))
        off = -float(np.dot(n, a))
        others = [pts[i] - centroid for i in CORE if i not in facet]
        if float(np.mean([np.dot(n, p) + off for p in others])) > 0:
            n, off = -n, -off
        values.append(-off)
    return np.array(values)


@dataclass
class FixedAudit:
    valid: bool
    error: str | None
    centroid: list[float]
    volume: float
    topology_min: float
    topology_arg: list | None
    stable_components: list[float]
    stable_foot: float
    saddle_components: list[float]
    saddle_beta1: float
    saddle_beta2: float
    relay_min: float
    relay_arg: list | None
    base_min: float
    u8_min: float
    short_rail_min: float
    long_rail_min: float
    nonbirth_face: float
    nonbirth_vertex: float
    nonbirth_edge: float


def fixed_audit(x: np.ndarray) -> FixedAudit:
    try:
        pts = points_from_x(x)
        faces = fixed_faces(pts)
        volume, centroid = mass_centroid(pts, faces)
        topology_min = math.inf
        topology_arg = None
        for fi, face in enumerate(faces):
            cyc = set(face["cycle"])
            for i in IDS:
                if i in cyc:
                    continue
                slack = -float(np.dot(face["n"], pts[i]) + face["off"])
                if slack < topology_min:
                    topology_min, topology_arg = slack, [fi, list(face["cycle"]), i]

        sf_i = next(i for i, c in enumerate(FACE_CYCLES) if frozenset(c) == STABLE_FACE)
        base_i = next(i for i, c in enumerate(FACE_CYCLES) if frozenset(c) == BASE_FACE)
        sf = face_components(FACE_CYCLES[sf_i], faces[sf_i]["n"], faces[sf_i]["off"], pts, centroid)
        base = face_components(FACE_CYCLES[base_i], faces[base_i]["n"], faces[base_i]["off"], pts, centroid)
        saddle = edge_components(SADDLE_EDGE, faces, pts, centroid)

        xcen = {i: pts[i] - centroid for i in IDS}
        u8 = []
        for j in NEIGHBORS[TARGET_VERTEX]:
            d = xcen[j] - xcen[TARGET_VERTEX]
            u8.append(-float(np.dot(xcen[TARGET_VERTEX], d)) /
                      (np.linalg.norm(xcen[TARGET_VERTEX]) * np.linalg.norm(d)))

        def rail_min(path: tuple[int, ...]) -> float:
            return min(float(np.dot(xcen[a], xcen[b] - xcen[a])) for a, b in zip(path, path[1:]))

        octa = octahedron(pts, centroid)
        relay_arg = min(octa["facets"], key=lambda z: z["origin_inward_slack"])

        # Fixed-chamber anti-birth decisions.  Positive means an unwanted
        # equilibrium already exists; the target base/U8 and residual S/H are excluded.
        fbad = -math.inf
        for fi, face in enumerate(faces):
            cycset = frozenset(face["cycle"])
            if cycset in (BASE_FACE, STABLE_FACE):
                continue
            fbad = max(fbad, min(face_components(face["cycle"], face["n"], face["off"], pts, centroid)))
        vbad = -math.inf
        for i in set().union(*(set(c) for c in FACE_CYCLES)):
            if i == TARGET_VERTEX:
                continue
            vals = []
            for j in NEIGHBORS[i]:
                d = xcen[j] - xcen[i]
                vals.append(-float(np.dot(xcen[i], d)) /
                            (np.linalg.norm(xcen[i]) * np.linalg.norm(d)))
            vbad = max(vbad, min(vals))
        ebad = -math.inf
        for edge in EDGE_FACES:
            if edge == SADDLE_EDGE:
                continue
            ebad = max(ebad, min(edge_components(edge, faces, pts, centroid)))

        return FixedAudit(
            True, None, centroid.tolist(), volume, topology_min, topology_arg,
            sf.tolist(), float(sf[0]), saddle.tolist(), float(saddle[2]), float(saddle[3]),
            float(octa["origin_inward_min"]), list(relay_arg["face"]), float(min(base)),
            float(min(u8)), rail_min(SHORT_RAIL), rail_min(LONG_RAIL),
            float(fbad), float(vbad), float(ebad),
        )
    except Exception as exc:
        return FixedAudit(False, repr(exc), [math.nan] * 3, math.nan, -math.inf, None,
                          [math.nan] * 3, math.inf, [math.nan] * 4, math.inf, math.inf,
                          -math.inf, None, -math.inf, -math.inf, -math.inf, -math.inf,
                          math.inf, math.inf, math.inf)


def finite_jacobian(fun, x0: np.ndarray, h: float = 1e-6) -> tuple[np.ndarray, np.ndarray]:
    y0 = np.asarray(fun(x0), dtype=float)
    jac = np.empty((len(y0), len(x0)))
    for j in range(len(x0)):
        xp, xm = x0.copy(), x0.copy()
        xp[j] += h
        xm[j] -= h
        jac[:, j] = (np.asarray(fun(xp)) - np.asarray(fun(xm))) / (2 * h)
    return y0, jac


def key_vector(x: np.ndarray) -> np.ndarray:
    a = fixed_audit(x)
    if not a.valid:
        raise ValueError(a.error)
    # Larger is always better.  S and H targets are negated because they must die.
    return np.array([
        -a.stable_foot,
        -a.saddle_beta1,
        -a.saddle_beta2,
        a.relay_min,
        a.topology_min,
        a.base_min,
        a.u8_min,
        a.short_rail_min,
        a.long_rail_min,
        -a.nonbirth_face,
        -a.nonbirth_vertex,
        -a.nonbirth_edge,
    ])


KEY_NAMES = (
    "stable_foot_dead", "saddle_beta1_dead", "saddle_beta2_dead", "relay_overlap",
    "topology", "base", "U8", "short_rail", "long_rail",
    "no_face_birth", "no_vertex_birth", "no_edge_birth",
)


def detailed_features(x: np.ndarray, templates: dict | None = None) -> tuple[list[str], np.ndarray, list[str], np.ndarray, dict]:
    """Return target and guard inequalities in the convention value >= 0.

    ``templates`` freezes a particular negative witness for every unwanted
    face/vertex/edge at the baseline.  This turns anti-birth into honest
    simultaneous linear inequalities instead of differentiating a global min.
    """
    pts = points_from_x(x)
    faces = fixed_faces(pts)
    _, centroid = mass_centroid(pts, faces)
    xcen = {i: pts[i] - centroid for i in IDS}

    fcomps = [face_components(face["cycle"], face["n"], face["off"], pts, centroid)
              for face in faces]
    ecomps = {edge: edge_components(edge, faces, pts, centroid) for edge in EDGE_FACES}
    vsupports = {}
    for i in set().union(*(set(c) for c in FACE_CYCLES)):
        vals = {}
        for j in sorted(NEIGHBORS[i]):
            d = xcen[j] - xcen[i]
            vals[j] = -float(np.dot(xcen[i], d)) / (
                np.linalg.norm(xcen[i]) * np.linalg.norm(d))
        vsupports[i] = vals

    sf_i = next(i for i, c in enumerate(FACE_CYCLES) if frozenset(c) == STABLE_FACE)
    base_i = next(i for i, c in enumerate(FACE_CYCLES) if frozenset(c) == BASE_FACE)
    saddle = ecomps[SADDLE_EDGE]
    relay = octa_facet_slacks(pts, centroid)
    target_names = ["stable-foot-death", "saddle-beta1-death"] + [
        "relay:" + ",".join(map(str, facet)) for facet in BASE_OCT_FACETS
    ]
    target = np.r_[-fcomps[sf_i][0], -saddle[2], relay]

    if templates is None:
        templates = {
            "face": {fi: int(np.argmin(v)) for fi, v in enumerate(fcomps)
                     if fi not in (sf_i, base_i)},
            "vertex": {i: min(vsupports[i], key=vsupports[i].get) for i in vsupports
                       if i != TARGET_VERTEX},
            "edge": {edge: int(np.argmin(v)) for edge, v in ecomps.items()
                     if edge != SADDLE_EDGE},
        }

    guard_names, guard = [], []
    # Every individual supporting-plane slack, not merely the current minimum.
    for fi, face in enumerate(faces):
        cyc = set(face["cycle"])
        for i in IDS:
            if i in cyc:
                continue
            guard_names.append(f"topology:f{fi}:row{i}")
            guard.append(-float(np.dot(face["n"], pts[i]) + face["off"]))
    for k, value in enumerate(fcomps[base_i]):
        guard_names.append(f"base:c{k}")
        guard.append(float(value))
    for j, value in sorted(vsupports[TARGET_VERTEX].items()):
        guard_names.append(f"U8:to{j}")
        guard.append(float(value))
    for name, path in (("short", SHORT_RAIL), ("long", LONG_RAIL)):
        for a, b in zip(path, path[1:]):
            guard_names.append(f"rail:{name}:{a}->{b}")
            guard.append(float(np.dot(xcen[a], xcen[b] - xcen[a])))
    for fi, k in sorted(templates["face"].items()):
        guard_names.append(f"antiface:f{fi}:c{k}")
        guard.append(-float(fcomps[fi][k]))
    for i, j in sorted(templates["vertex"].items()):
        guard_names.append(f"antivertex:v{i}:to{j}")
        guard.append(-float(vsupports[i][j]))
    for edge, k in sorted(templates["edge"].items()):
        guard_names.append(f"antiedge:{edge[0]}-{edge[1]}:c{k}")
        guard.append(-float(ecomps[edge][k]))
    return target_names, np.asarray(target), guard_names, np.asarray(guard), templates


def fully_guarded_linear_lp(event_epsilon: float = 1e-6) -> dict:
    """Minimum-L-infinity first-order displacement for the complete event.

    The LP contains every baseline face/row support slack, each base and U8
    component, all 38 directed rail inequalities, and a frozen negative witness
    for every unwanted equilibrium.  Hence an infeasible result is a concrete
    first-order obstruction, not an artefact of differentiating only the active
    minimum.
    """
    x0 = np.zeros(18)
    tn, t0, gn, g0, templates = detailed_features(x0)

    def vec(x):
        tn1, t, gn1, g, _ = detailed_features(x, templates)
        assert tn1 == tn and gn1 == gn
        return np.r_[t, g]

    y0, jac = finite_jacobian(vec, x0, h=2e-7)
    nt = len(t0)
    # x(18), radius r.  All affine features must be >= their requested margin.
    c = np.zeros(19)
    c[-1] = 1.0
    Aub, bub = [], []
    requested = np.r_[np.full(nt, event_epsilon), np.zeros(len(g0))]
    for y, row, req in zip(y0, jac, requested):
        z = np.zeros(19)
        z[:18] = -row
        Aub.append(z)
        bub.append(y - req)
    for j in range(18):
        z = np.zeros(19); z[j] = 1; z[-1] = -1
        Aub.append(z); bub.append(0)
        z = np.zeros(19); z[j] = -1; z[-1] = -1
        Aub.append(z); bub.append(0)
    sol = linprog(c, A_ub=np.asarray(Aub), b_ub=np.asarray(bub),
                  bounds=[(None, None)] * 18 + [(0, None)], method="highs")
    out = {
        "success": bool(sol.success),
        "status": int(sol.status),
        "message": sol.message,
        "target_count": nt,
        "guard_count": len(g0),
        "baseline_targets": dict(zip(tn, t0.tolist())),
        "baseline_guard_min": float(g0.min()),
        "baseline_guard_arg": gn[int(np.argmin(g0))],
        "event_epsilon": event_epsilon,
    }
    if not sol.success:
        # Farkas alternative for A x <= b.  Normalizing sum(y)=1 makes the
        # certificate bounded; b.y<0 and A.T y=0 prove infeasibility.
        names = ["target:" + z for z in tn] + ["guard:" + z for z in gn]
        A = -jac
        b = y0 - requested
        Aeq = np.vstack((A.T, np.ones(len(b))))
        beq = np.r_[np.zeros(18), 1.0]
        dual = linprog(b, A_eq=Aeq, b_eq=beq, bounds=[(0, None)] * len(b), method="highs")
        out["farkas_success"] = bool(dual.success)
        if dual.success:
            support = np.flatnonzero(dual.x > 1e-9)
            out["farkas_b_dot_y"] = float(np.dot(b, dual.x))
            out["farkas_at_y_inf"] = float(np.max(np.abs(A.T @ dual.x)))
            out["farkas_sum_y"] = float(dual.x.sum())
            out["farkas_support"] = [
                {
                    "name": names[int(i)],
                    "weight": float(dual.x[i]),
                    "rhs": float(b[i]),
                    "baseline_value": float(y0[i]),
                    "requested": float(requested[i]),
                }
                for i in support
            ]
        # Stronger reduced subsystem: beta1 death by itself versus only the
        # frozen non-saddle witnesses.  No topology/base/U8/rail/face/vertex
        # row is used here.
        beta_i = tn.index("saddle-beta1-death")
        selected = [beta_i] + [nt + i for i, name in enumerate(gn) if name.startswith("antiedge:")]
        reduced_names = ["target:" + tn[beta_i]] + [
            "guard:" + gn[i] for i, name in enumerate(gn) if name.startswith("antiedge:")
        ]
        A2 = -jac[selected]
        b2 = y0[selected] - requested[selected]
        primal2 = linprog(np.zeros(18), A_ub=A2, b_ub=b2,
                          bounds=[(None, None)] * 18, method="highs")
        reduced = {
            "success": bool(primal2.success),
            "constraint_count": len(selected),
            "message": primal2.message,
        }
        if not primal2.success:
            dual2 = linprog(b2, A_eq=np.vstack((A2.T, np.ones(len(b2)))),
                            b_eq=np.r_[np.zeros(18), 1.0],
                            bounds=[(0, None)] * len(b2), method="highs")
            reduced["farkas_success"] = bool(dual2.success)
            if dual2.success:
                support2 = np.flatnonzero(dual2.x > 1e-10)
                reduced["farkas_b_dot_y"] = float(np.dot(b2, dual2.x))
                reduced["farkas_at_y_inf"] = float(np.max(np.abs(A2.T @ dual2.x)))
                reduced["farkas_sum_y"] = float(dual2.x.sum())
                reduced["farkas_support"] = [
                    {"name": reduced_names[int(i)], "weight": float(dual2.x[i]), "rhs": float(b2[i])}
                    for i in support2
                ]
        out["beta_only_vs_antiedges"] = reduced
        return out
    x = sol.x[:18]
    pred = y0 + jac @ x
    out.update({
        "linf_radius": float(sol.x[-1]),
        "displacements": x.tolist(),
        "predicted_target_min": float(pred[:nt].min()),
        "predicted_target_arg": tn[int(np.argmin(pred[:nt]))],
        "predicted_guard_min": float(pred[nt:].min()),
        "predicted_guard_arg": gn[int(np.argmin(pred[nt:]))],
        "actual_fixed": asdict(fixed_audit(x)),
        "actual_fresh": fresh_audit(x),
        "first_wall": first_wall(x),
    })
    # Store the tight first-order rows.  These diagnose which carrier wall is
    # actually paying for the formal endpoint.
    order = np.argsort(pred[nt:])[:20]
    out["smallest_predicted_guards"] = [
        {"name": gn[int(i)], "value": float(pred[nt + i])} for i in order
    ]
    return out


def linearized_common_direction(radius: float = 1.0) -> dict:
    x0 = np.zeros(18)
    y0, jac = finite_jacobian(key_vector, x0)
    # Find the best common first-order improvement of the three event functions
    # and the currently negative relay overlap, while not decreasing guards.
    primary = (0, 1, 3)  # beta1 is the face-224 side of the saddle.
    guards = tuple(range(4, 12))
    n = len(x0)
    c = np.zeros(n + 1)
    c[-1] = -1.0
    Aub, bub = [], []
    for i in primary:
        row = np.zeros(n + 1)
        row[:n] = -jac[i]
        row[-1] = 1.0
        Aub.append(row)
        bub.append(y0[i])
    for i in guards:
        row = np.zeros(n + 1)
        row[:n] = -jac[i]
        Aub.append(row)
        bub.append(y0[i])
    bounds = [(-radius, radius)] * n + [(None, None)]
    sol = linprog(c, A_ub=np.array(Aub), b_ub=np.array(bub), bounds=bounds, method="highs")
    if not sol.success:
        return {"success": False, "message": sol.message, "baseline": dict(zip(KEY_NAMES, y0))}
    d, lam = sol.x[:-1], sol.x[-1]
    return {
        "success": True,
        "lambda": float(lam),
        "direction": d.tolist(),
        "baseline": dict(zip(KEY_NAMES, y0.tolist())),
        "derivative": dict(zip(KEY_NAMES, (jac @ d).tolist())),
        "jacobian_singular_values": np.linalg.svd(jac[[0, 1, 3]], compute_uv=False).tolist(),
    }


def fresh_audit(x: np.ndarray) -> dict:
    pts = points_from_x(x)
    res = evaluate(pts, plane_tol=2e-8, qhull_options="Qt Qx", strict_tol=1e-9)
    if not res.valid:
        return {"valid": False, "error": res.error}
    base = next((d for fi, d in res.stable if frozenset(res.faces[fi]["cycle"]) == BASE_FACE), None)
    u8 = next((d for i, d in res.unstable if i == TARGET_VERTEX), None)
    stable_face_present = next((fi for fi, f in enumerate(res.faces)
                                if frozenset(f["cycle"]) == STABLE_FACE), None)
    stable_dec = None if stable_face_present is None else res.face_decisions[stable_face_present]
    saddle_dec = res.edge_decisions.get(SADDLE_EDGE)
    octa = octahedron(pts, res.centroid)
    xcen = {i: pts[i] - res.centroid for i in pts}

    def rail_record(path: tuple[int, ...]) -> dict:
        edgeset = set(res.edges)
        missing = [list(tuple(sorted((a, b)))) for a, b in zip(path, path[1:])
                   if tuple(sorted((a, b))) not in edgeset]
        support = [float(np.dot(xcen[a], xcen[b] - xcen[a])) for a, b in zip(path, path[1:])]
        return {"missing_edges": missing, "directed_support_min": min(support)}

    return {
        "valid": True,
        "f_vector": [len(res.active), len(res.edges), len(res.faces)],
        "class": [len(res.stable), len(res.unstable), len(res.saddles)],
        "active": res.active,
        "centroid": res.centroid.tolist(),
        "topology_margin": res.topology_margin,
        "inactive_margin": res.inactive_margin,
        "base_margin": base,
        "U8_margin": u8,
        "residual_stable_face_present": stable_face_present is not None,
        "residual_stable_decision": stable_dec,
        "residual_saddle_edge_present": SADDLE_EDGE in res.edge_decisions,
        "residual_saddle_decision": saddle_dec,
        "stable_faces": [{"cycle": res.faces[fi]["cycle"], "decision": d} for fi, d in res.stable],
        "unstable_vertices": [{"vertex": i, "decision": d} for i, d in res.unstable],
        "saddle_edges": [{"edge": list(e), "decision": d} for e, d in res.saddles],
        "relay_origin_inward_min": octa["origin_inward_min"],
        "relay_facets": list(octa["facets"]),
        "short_rail": rail_record(SHORT_RAIL),
        "long_rail": rail_record(LONG_RAIL),
    }


def first_wall(direction: np.ndarray, max_t: float = 10.0) -> dict:
    base = fixed_audit(np.zeros(18))
    if not base.valid:
        raise RuntimeError(base.error)
    lo, hi = 0.0, 1e-8
    while hi < max_t and fixed_audit(hi * direction).topology_min > 0:
        lo, hi = hi, hi * 2
    if hi >= max_t and fixed_audit(hi * direction).topology_min > 0:
        return {"found": False, "max_t": max_t}
    for _ in range(70):
        mid = (lo + hi) / 2
        if fixed_audit(mid * direction).topology_min > 0:
            lo = mid
        else:
            hi = mid
    before = fixed_audit(lo * direction)
    after = fixed_audit(hi * direction)
    return {
        "found": True,
        "t": hi,
        "wall": after.topology_arg,
        "before": asdict(before),
        "fresh_before": fresh_audit(lo * direction),
        "fresh_after": fresh_audit((1 + 1e-7) * hi * direction),
    }


def optimize_three_mode(direction: np.ndarray) -> dict:
    """Refine in a 3-space: LP direction plus pure 228 and pure beta actuators."""
    x0 = np.zeros(18)
    _, jac = finite_jacobian(key_vector, x0)
    # Minimum-norm independent actuators for stable-foot, beta1, relay.
    rows = jac[[0, 1, 3]]
    actuators = rows.T @ np.linalg.inv(rows @ rows.T)
    # First axis is the guarded LP direction.  Orthogonalize the two missing
    # local actuators against it to obtain an explicit shared 3-D cell search.
    basis = np.column_stack((direction, actuators[:, 1], actuators[:, 2]))
    q, _ = np.linalg.qr(basis)

    def objective(a: np.ndarray) -> float:
        x = q @ a
        audit = fixed_audit(x)
        if not audit.valid:
            return 1e6
        # Soft maximum: all three local objectives should be positive in key convention.
        key = key_vector(x)
        primary = key[[0, 1, 3]]
        guards = key[4:]
        loss = float(np.log(np.exp(-20 * primary).sum()) / 20)
        loss += 200 * float(np.maximum(0, -guards).sum())
        loss += 1e-4 * float(np.dot(a, a))
        return loss

    de = differential_evolution(objective, [(-8, 8)] * 3, seed=20260831,
                                popsize=18, maxiter=220, polish=False, workers=1,
                                updating="immediate")
    sls = minimize(objective, de.x, method="Nelder-Mead",
                   options={"maxiter": 4000, "xatol": 1e-10, "fatol": 1e-12})
    a = sls.x
    x = q @ a
    return {
        "basis": q.tolist(),
        "coefficients": a.tolist(),
        "displacements": x.tolist(),
        "objective": float(sls.fun),
        "fixed": asdict(fixed_audit(x)),
        "fresh": fresh_audit(x),
        "first_wall": first_wall(x),
    }


def dynamic_hard_score(x: np.ndarray) -> tuple[float, dict]:
    """Fresh-hull target score; positive is a strict (1,1,0) local winner."""
    pts = points_from_x(x)
    res = evaluate(pts, plane_tol=2e-8, qhull_options="Qt Qx", strict_tol=1e-9)
    if not res.valid:
        return -100.0, {"valid": False, "error": res.error}
    base_idx = next((fi for fi, f in enumerate(res.faces)
                     if frozenset(f["cycle"]) == BASE_FACE), None)
    base = -10.0 if base_idx is None else float(res.face_decisions[base_idx])
    u8 = float(res.vertex_decisions.get(TARGET_VERTEX, -10.0))
    face_bad = max((d for fi, d in enumerate(res.face_decisions) if fi != base_idx), default=-10.0)
    vertex_bad = max((d for i, d in res.vertex_decisions.items() if i != TARGET_VERTEX), default=-10.0)
    edge_bad = max(res.edge_decisions.values(), default=-10.0)
    relay = float(octahedron(pts, res.centroid)["origin_inward_min"])
    edges = set(res.edges)
    xcen = {i: pts[i] - res.centroid for i in pts}

    rail_values = []
    missing = []
    for name, path in (("short", SHORT_RAIL), ("long", LONG_RAIL)):
        for a, b in zip(path, path[1:]):
            edge = tuple(sorted((a, b)))
            if edge not in edges:
                missing.append((name, edge))
            rail_values.append(float(np.dot(xcen[a], xcen[b] - xcen[a])) / 20.0)
    rail = -10.0 if missing else min(rail_values)
    components = {
        "base": base,
        "U8": u8,
        "no_extra_stable": -float(face_bad),
        "no_extra_unstable": -float(vertex_bad),
        "no_saddle": -float(edge_bad),
        "relay_overlap": relay,
        "rails": rail,
    }
    hard = min(components[k] for k in (
        "base", "U8", "no_extra_stable", "no_extra_unstable", "no_saddle",
        "relay_overlap", "rails", "core_on_global_hull",
    ))
    return float(hard), {
        "valid": True,
        "hard": float(hard),
        "components": components,
        "f_vector": [len(res.active), len(res.edges), len(res.faces)],
        "class": [len(res.stable), len(res.unstable), len(res.saddles)],
        "missing_rails": [(name, list(edge)) for name, edge in missing],
    }


ID_TO_LOCAL = {i: k for k, i in enumerate(IDS)}
P0_ARRAY = np.array([POINTS0[i] for i in IDS])


def cross3(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.array((a[1] * b[2] - a[2] * b[1],
                     a[2] * b[0] - a[0] * b[2],
                     a[0] * b[1] - a[1] * b[0]))


def fast_dynamic_hard_score(x: np.ndarray) -> tuple[float, dict]:
    """Allocation-light fresh hull score used for the 3-D global search."""
    P = P0_ARRAY.copy()
    for row, d in zip(CORE, np.asarray(x).reshape((6, 3))):
        P[ID_TO_LOCAL[row]] += d
    try:
        hull = ConvexHull(P, qhull_options="Qt Qx")
    except Exception as exc:
        return -100.0, {"valid": False, "error": repr(exc)}

    groups = []
    for tri, eq0 in zip(hull.simplices, hull.equations):
        n = eq0[:3].copy(); off = float(eq0[3]); ln = float(np.linalg.norm(n)); n /= ln; off /= ln
        found = None
        for g in groups:
            if float(np.dot(n, g[0])) > 1 - 2e-8 and abs(off - g[1]) < 2e-8:
                found = g; break
        if found is None:
            groups.append([n, off, [tuple(map(int, tri))]])
        else:
            found[2].append(tuple(map(int, tri)))

    faces = []
    for n, off, tris in groups:
        counts = defaultdict(int)
        for a, b, c in tris:
            counts[tuple(sorted((a, b)))] += 1
            counts[tuple(sorted((b, c)))] += 1
            counts[tuple(sorted((c, a)))] += 1
        adj = defaultdict(list)
        for (a, b), count in counts.items():
            if count == 1:
                adj[a].append(b); adj[b].append(a)
        if not adj or any(len(v) != 2 for v in adj.values()):
            return -100.0, {"valid": False, "error": "bad boundary"}
        start = min(adj); cyc = [start]; prev = None; cur = start
        while True:
            u, v = adj[cur]
            nxt = u if u != prev else v
            if nxt == start:
                break
            cyc.append(nxt); prev, cur = cur, nxt
            if len(cyc) > len(adj) + 1:
                return -100.0, {"valid": False, "error": "bad cycle"}
        area = np.zeros(3)
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            area += cross3(P[a], P[b])
        if float(np.dot(area, n)) < 0:
            cyc = [cyc[0]] + list(reversed(cyc[1:]))
        faces.append((cyc, n, off))

    d6 = 0.0; m24 = np.zeros(3)
    for cyc, _, _ in faces:
        for j in range(1, len(cyc) - 1):
            a, b, c = P[cyc[0]], P[cyc[j]], P[cyc[j + 1]]
            d = float(np.dot(a, cross3(b, c)))
            d6 += d; m24 += d * (a + b + c)
    if d6 <= 1e-12:
        return -100.0, {"valid": False, "error": "bad volume"}
    centroid = m24 / (4 * d6); X = P - centroid

    EF = defaultdict(list); neighbors = defaultdict(set)
    for fi, (cyc, _, _) in enumerate(faces):
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            edge = tuple(sorted((a, b))); EF[edge].append(fi)
            neighbors[a].add(b); neighbors[b].add(a)
    if any(len(v) != 2 for v in EF.values()):
        return -100.0, {"valid": False, "error": "nonmanifold"}

    face_dec = []
    base_idx = None
    residual_face_idx = None
    for fi, (cyc, n, off) in enumerate(faces):
        ids = frozenset(IDS[i] for i in cyc)
        if ids == BASE_FACE:
            base_idx = fi
        if ids == STABLE_FACE:
            residual_face_idx = fi
        h = -(off + float(np.dot(n, centroid))); foot = h * n
        ref = np.mean(X[cyc], axis=0); vals = []
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            edge = X[b] - X[a]
            z = float(np.dot(cross3(edge, foot - X[a]), n))
            if float(np.dot(cross3(edge, ref - X[a]), n)) < 0:
                z = -z
            vals.append(z / np.linalg.norm(edge))
        face_dec.append(min(vals))

    active_local = set(hull.vertices.tolist())
    vdec = {}
    for i in active_local:
        vals = []
        for j in neighbors[i]:
            d = X[j] - X[i]
            vals.append(-float(np.dot(X[i], d)) / (np.linalg.norm(X[i]) * np.linalg.norm(d)))
        vdec[i] = min(vals)

    edec = {}
    edge_beta_min = {}
    for (a, b), inc in EF.items():
        d = X[b] - X[a]; dd = float(np.dot(d, d)); t = -float(np.dot(X[a], d)) / dd
        p = X[a] + t * d
        n1, n2 = faces[inc[0]][1], faces[inc[1]][1]
        bb = float(np.dot(n1, n2)); r1, r2 = float(np.dot(p, n1)), float(np.dot(p, n2))
        den = 1 - bb * bb
        if den <= 1e-14:
            return -100.0, {"valid": False, "error": "parallel incident faces"}
        b1 = (r1 - r2 * bb) / den; b2 = (r2 - r1 * bb) / den
        pn = max(float(np.linalg.norm(p)), 1e-300)
        edge_beta_min[(a, b)] = min(b1 / pn, b2 / pn)
        edec[(a, b)] = min(t, 1 - t, b1 / pn, b2 / pn)

    base = -10.0 if base_idx is None else float(face_dec[base_idx])
    i8 = ID_TO_LOCAL[TARGET_VERTEX]
    u8 = float(vdec.get(i8, -10.0))
    face_bad = max((d for fi, d in enumerate(face_dec) if fi != base_idx), default=-10.0)
    vertex_bad = max((d for i, d in vdec.items() if i != i8), default=-10.0)
    edge_bad = max(edec.values(), default=-10.0)
    residual_edge_local = tuple(sorted((ID_TO_LOCAL[SADDLE_EDGE[0]], ID_TO_LOCAL[SADDLE_EDGE[1]])))
    original_stable_dead = 1.0 if residual_face_idx is None else -float(face_dec[residual_face_idx])
    original_saddle_dead = 1.0 if residual_edge_local not in edec else -float(edec[residual_edge_local])
    original_saddle_beta_dead = 1.0 if residual_edge_local not in edec else -float(edge_beta_min[residual_edge_local])

    # The relay octahedron is only six points, so a second tiny Qhull call is cheap.
    core_local = np.array([P[ID_TO_LOCAL[i]] - centroid for i in CORE])
    try:
        oh = ConvexHull(core_local, qhull_options="Qt Qx")
    except Exception as exc:
        return -100.0, {"valid": False, "error": "degenerate relay: " + repr(exc)}
    relay = min(-float(eq[3]) for eq in oh.equations)

    missing = []; rail_values = []
    edge_ids = {tuple(sorted((IDS[a], IDS[b]))) for a, b in EF}
    for name, path in (("short", SHORT_RAIL), ("long", LONG_RAIL)):
        for a_id, b_id in zip(path, path[1:]):
            edge = tuple(sorted((a_id, b_id)))
            if edge not in edge_ids:
                missing.append((name, edge))
            a, b = ID_TO_LOCAL[a_id], ID_TO_LOCAL[b_id]
            rail_values.append(float(np.dot(X[a], X[b] - X[a])) / 20.0)
    rail = -10.0 if missing else min(rail_values)
    components = {
        "base": base, "U8": u8, "no_extra_stable": -float(face_bad),
        "no_extra_unstable": -float(vertex_bad), "no_saddle": -float(edge_bad),
        "relay_overlap": float(relay), "rails": float(rail),
        "core_on_global_hull": 1.0 if all(ID_TO_LOCAL[i] in active_local for i in CORE) else -10.0,
        "original_stable_dead": original_stable_dead,
        "original_saddle_dead": original_saddle_dead,
        "original_saddle_beta_dead": original_saddle_beta_dead,
    }
    hard = min(components.values())
    cls = [int(sum(d > 1e-9 for d in face_dec)), int(sum(d > 1e-9 for d in vdec.values())),
           int(sum(d > 1e-9 for d in edec.values()))]
    return float(hard), {
        "valid": True, "hard": float(hard), "components": components,
        "f_vector": [len(active_local), len(EF), len(faces)], "class": cls,
        "missing_rails": [(name, list(edge)) for name, edge in missing],
    }


def dynamic_three_mode_search(maxiter: int = 60) -> dict:
    """Search the fresh global hull in the independent S/H/relay 3-space."""
    x0 = np.zeros(18)
    _, jac = finite_jacobian(key_vector, x0)
    rows = jac[[0, 1, 3]]
    actuators = rows.T @ np.linalg.inv(rows @ rows.T)
    bounds = [(-2.0, 3.5), (-4.0, 9.0), (-0.25, 0.55)]

    best = {"score": -math.inf, "a": None, "x": None, "detail": None}
    history = []

    def objective(a):
        x = actuators @ np.asarray(a)
        score, detail = fast_dynamic_hard_score(x)
        if score > best["score"]:
            best.update(score=float(score), a=np.asarray(a).tolist(), x=x.tolist(), detail=detail)
            history.append({"score": float(score), "coefficients": np.asarray(a).tolist(), **detail})
        return -score

    de = differential_evolution(objective, bounds, seed=42060831, popsize=16,
                                maxiter=maxiter, polish=False, workers=1,
                                updating="immediate", tol=1e-8, atol=1e-10)
    # Powell copes better than a gradient method with hull walls.
    local = minimize(objective, de.x, method="Powell", bounds=bounds,
                     options={"maxiter": 1200, "xtol": 1e-9, "ftol": 1e-11})
    a = np.asarray(best["a"])
    x = np.asarray(best["x"])
    return {
        "actuators": actuators.tolist(),
        "actuator_norms": np.linalg.norm(actuators, axis=0).tolist(),
        "coefficient_bounds": bounds,
        "evaluations": int(de.nfev + local.nfev),
        "best_coefficients": a.tolist(),
        "best_displacements": x.tolist(),
        "best_score": float(best["score"]),
        "best_summary": best["detail"],
        "fresh_audit": fresh_audit(x),
        "improvement_history": history,
    }


def relay_support_supremum_search(maxiter: int = 60) -> dict:
    """Maximize relay overlap while base/U8/rails and all six core rows survive."""
    x0 = np.zeros(18)
    _, jac = finite_jacobian(key_vector, x0)
    rows = jac[[0, 1, 3]]
    actuators = rows.T @ np.linalg.inv(rows @ rows.T)
    bounds = [(-2.0, 3.5), (-4.0, 9.0), (-0.25, 0.55)]
    best = {"score": -math.inf}

    def objective(a):
        x = actuators @ np.asarray(a)
        _, detail = fast_dynamic_hard_score(x)
        if not detail.get("valid"):
            return 100.0
        c = detail["components"]
        score = min(c["relay_overlap"], c["base"], c["U8"], c["rails"], c["core_on_global_hull"])
        if score > best["score"]:
            best.update(score=float(score), a=np.asarray(a).tolist(), x=x.tolist(), detail=detail)
        return -score

    de = differential_evolution(objective, bounds, seed=198224258, popsize=16,
                                maxiter=maxiter, polish=False, workers=1,
                                updating="immediate", tol=1e-9, atol=1e-11)
    local = minimize(objective, de.x, method="Powell", bounds=bounds,
                     options={"maxiter": 1000, "xtol": 1e-10, "ftol": 1e-12})
    x = np.asarray(best["x"])
    return {
        "evaluations": int(de.nfev + local.nfev),
        "best_score": float(best["score"]),
        "best_coefficients": best["a"],
        "best_displacements": best["x"],
        "best_summary": best["detail"],
        "fresh_audit": fresh_audit(x),
    }


def original_pair_escape_search(maxiter: int = 60) -> dict:
    """Kill the named S/H pair, allowing births, and report the transfer target."""
    x0 = np.zeros(18)
    _, jac = finite_jacobian(key_vector, x0)
    rows = jac[[0, 1, 3]]
    actuators = rows.T @ np.linalg.inv(rows @ rows.T)
    bounds = [(-2.0, 3.5), (-4.0, 9.0), (-0.25, 0.55)]
    best = {"score": -math.inf}

    def objective(a):
        x = actuators @ np.asarray(a)
        _, detail = fast_dynamic_hard_score(x)
        if not detail.get("valid"):
            return 100.0
        c = detail["components"]
        score = min(c["original_stable_dead"], c["original_saddle_beta_dead"],
                    c["relay_overlap"], c["base"], c["U8"], c["rails"],
                    c["core_on_global_hull"])
        if score > best["score"]:
            best.update(score=float(score), a=np.asarray(a).tolist(), x=x.tolist(), detail=detail)
        return -score

    de = differential_evolution(objective, bounds, seed=229247, popsize=16,
                                maxiter=maxiter, polish=False, workers=1,
                                updating="immediate", tol=1e-9, atol=1e-11)
    local = minimize(objective, de.x, method="Powell", bounds=bounds,
                     options={"maxiter": 1000, "xtol": 1e-10, "ftol": 1e-12})
    x = np.asarray(best["x"])
    return {
        "evaluations": int(de.nfev + local.nfev),
        "best_score": float(best["score"]),
        "best_coefficients": best["a"],
        "best_displacements": best["x"],
        "best_summary": best["detail"],
        "fresh_audit": fresh_audit(x),
    }


def beta_transfer_search(maxiter: int = 45) -> dict:
    """Force the named saddle to die with hard base/U8/rail/core guards."""
    x0 = np.zeros(18)
    _, jac = finite_jacobian(key_vector, x0)
    rows = jac[[0, 1, 3]]
    actuators = rows.T @ np.linalg.inv(rows @ rows.T)
    bounds = [(-2.0, 3.5), (-4.0, 9.0), (-0.25, 0.55)]
    best = {"score": -math.inf}

    def objective(a):
        x = actuators @ np.asarray(a)
        _, detail = fast_dynamic_hard_score(x)
        if not detail.get("valid"):
            return 100.0
        c = detail["components"]
        score = min(c["original_saddle_beta_dead"], c["base"], c["U8"],
                    c["rails"], c["core_on_global_hull"])
        if score > best["score"]:
            best.update(score=float(score), a=np.asarray(a).tolist(), x=x.tolist(), detail=detail)
        return -score

    de = differential_evolution(objective, bounds, seed=247229, popsize=16,
                                maxiter=maxiter, polish=False, workers=1,
                                updating="immediate", tol=1e-9, atol=1e-11)
    local = minimize(objective, de.x, method="Powell", bounds=bounds,
                     options={"maxiter": 900, "xtol": 1e-10, "ftol": 1e-12})
    x = np.asarray(best["x"])
    return {
        "evaluations": int(de.nfev + local.nfev),
        "best_score": float(best["score"]),
        "best_coefficients": best["a"],
        "best_displacements": best["x"],
        "best_summary": best["detail"],
        "fresh_audit": fresh_audit(x),
    }


def pure_beta_actuator_scan() -> dict:
    """Deterministic scan showing the first actual beta death and its births."""
    _, jac = finite_jacobian(key_vector, np.zeros(18))
    rows = jac[[0, 1, 3]]
    actuators = rows.T @ np.linalg.inv(rows @ rows.T)
    records = []
    first = None
    for coefficient in np.linspace(0.0, 9.0, 19):
        x = actuators @ np.array((0.0, coefficient, 0.0))
        _, detail = fast_dynamic_hard_score(x)
        record = {"beta_coefficient": float(coefficient), **detail}
        records.append(record)
        if first is None and detail.get("valid") and detail["components"]["original_saddle_beta_dead"] > 0:
            first = {
                "beta_coefficient": float(coefficient),
                "displacements": x.tolist(),
                "summary": detail,
                "fresh_audit": fresh_audit(x),
            }
    return {"actuators": actuators.tolist(), "records": records, "first_beta_dead": first}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=("baseline", "linear", "guarded", "search", "dynamic", "relay", "escape", "beta", "scan", "all"), default="all")
    ap.add_argument("--output", type=Path, default=HERE / "result.json")
    args = ap.parse_args()
    output: dict = {"core": CORE, "opposite_pairs": OPPOSITE}
    if args.mode in ("baseline", "all"):
        output["baseline_fixed"] = asdict(fixed_audit(np.zeros(18)))
        output["baseline_fresh"] = fresh_audit(np.zeros(18))
    linear = None
    if args.mode in ("linear", "search", "all"):
        linear = linearized_common_direction()
        output["linearized"] = linear
        if linear.get("success"):
            output["linear_first_wall"] = first_wall(np.array(linear["direction"]))
    if args.mode in ("guarded", "all"):
        output["fully_guarded_linear_lp"] = fully_guarded_linear_lp()
    if args.mode in ("search", "all"):
        if not linear or not linear.get("success"):
            raise RuntimeError("linearized search failed")
        output["three_mode_search"] = optimize_three_mode(np.array(linear["direction"]))
    if args.mode in ("dynamic", "all"):
        output["dynamic_three_mode_search"] = dynamic_three_mode_search()
    if args.mode in ("relay", "all"):
        output["relay_support_supremum_search"] = relay_support_supremum_search()
    if args.mode in ("escape", "all"):
        output["original_pair_escape_search"] = original_pair_escape_search()
    if args.mode in ("beta", "all"):
        output["beta_transfer_search"] = beta_transfer_search()
    if args.mode in ("scan", "all"):
        output["pure_beta_actuator_scan"] = pure_beta_actuator_scan()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2, allow_nan=False)
    print(json.dumps(output, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
