#!/usr/bin/env python3
"""Rank-revealing guarded SLP for the rail-valid four-defect row54 cell.

Controls are the eight projective/trace-free-SPD parameters plus two
in-base-plane coordinates for each of the 18 base rows.  The LP maximizes the
minimum normalized target mechanics guard while retaining every linearized
support/convexity guard of the fixed maximal-face cell.  Every accepted
nonlinear step receives a fresh Qhull/maximal-face/own-centroid audit and a
forced-rail check.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Sequence

import numpy as np
from scipy.linalg import expm
from scipy.optimize import linprog

import row54_four_residual_search as core


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "row54_far_rebuilt.csv"
FACES_SOURCE = HERE / "row54_far_rebuilt_faces.json"
BASE_CYCLE = [0, 54] + list(range(1, 17))


def load_problem(source_path=SOURCE, faces_path=FACES_SOURCE):
    rows = {}
    source_path = Path(source_path)
    faces_path = Path(faces_path)
    with source_path.open() as f:
        for row in csv.DictReader(f):
            rows[int(row["source_id"])] = np.asarray(
                [float(row[k]) for k in ("x", "y", "z")], dtype=float
            )
    ids = sorted(rows)
    points = np.asarray([rows[i] for i in ids])
    faces = json.load(faces_path.open())
    return ids, points, faces


def forced_rail_edges():
    short = [228] + list(range(229, 247)) + [8]
    long = [228] + list(range(247, 265)) + [8]
    edges = {
        tuple(sorted(edge))
        for path in (short, long)
        for edge in zip(path, path[1:])
    }
    edges.remove((228, 229))
    return edges


class Chart:
    def __init__(self, ids: Sequence[int], source: np.ndarray):
        self.ids = list(ids)
        self.ix = {i: k for k, i in enumerate(ids)}
        self.source = np.asarray(source, dtype=float)
        self.origin = self.source.mean(axis=0)
        self.scale = float(np.sqrt(np.mean(np.sum((self.source - self.origin) ** 2, axis=1))))

        a = self.source[self.ix[BASE_CYCLE[0]]]
        e1 = self.source[self.ix[BASE_CYCLE[1]]] - a
        e1 = e1 / np.linalg.norm(e1)
        witness = self.source[self.ix[BASE_CYCLE[2]]] - a
        n = np.cross(e1, witness)
        n = n / np.linalg.norm(n)
        e2 = np.cross(n, e1)
        self.base_u = e1
        self.base_v = e2

        self.base_scales = {}
        for k, i in enumerate(BASE_CYCLE):
            prev_i = BASE_CYCLE[(k - 1) % len(BASE_CYCLE)]
            next_i = BASE_CYCLE[(k + 1) % len(BASE_CYCLE)]
            local = min(
                np.linalg.norm(self.source[self.ix[i]] - self.source[self.ix[prev_i]]),
                np.linalg.norm(self.source[self.ix[next_i]] - self.source[self.ix[i]]),
            )
            self.base_scales[i] = float(local)
        self.names = (
            [f"pole_{axis}" for axis in "xyz"]
            + ["H_xx", "H_xy", "H_xz", "H_yy", "H_yz"]
            + [f"base_{i}_{axis}" for i in BASE_CYCLE for axis in ("u", "v")]
        )
        if len(self.names) != 44:
            raise AssertionError(len(self.names))

    def coordinates(self, x: np.ndarray):
        x = np.asarray(x, dtype=float)
        q = self.source.copy()
        for k, i in enumerate(BASE_CYCLE):
            du, dv = x[8 + 2 * k: 8 + 2 * k + 2]
            q[self.ix[i]] += self.base_scales[i] * (du * self.base_u + dv * self.base_v)
        z = (q - self.origin) / self.scale
        den = 1.0 + z @ x[:3]
        if float(np.min(den)) <= 0.06:
            return None, den
        a, b, c, d, e = x[3:8]
        h = np.asarray([[a, b, c], [b, d, e], [c, e, -a - d]], dtype=float)
        return (z / den[:, None]) @ expm(h).T, den


def topology_guards(ids, points, faces):
    """All fixed-cell face-support and polygon-convexity guards."""
    ix = {i: k for k, i in enumerate(ids)}
    center = points.mean(axis=0)
    values = []
    labels = []
    for fi, cyc in enumerate(faces):
        area = sum(
            (
                np.cross(points[ix[u]], points[ix[v]])
                for u, v in zip(cyc, cyc[1:] + cyc[:1])
            ),
            np.zeros(3),
        )
        if np.dot(area, points[ix[cyc[0]]] - center) < 0:
            area = -area
        normal_norm = float(np.linalg.norm(area))
        if normal_norm <= 1e-15:
            raise ValueError(("degenerate face", fi, cyc))
        n = area / normal_norm
        h = float(np.dot(n, points[ix[cyc[0]]]))
        cset = set(cyc)
        for j in ids:
            if j not in cset:
                values.append(h - float(np.dot(n, points[ix[j]])))
                labels.append(("support", fi, list(cyc), j))
        # Align the polygon normal with the cycle, independently of the
        # outward support orientation.  The supplied cycles are coherently
        # oriented, so all edge-to-other-vertex guards start positive.
        cycle_n = sum(
            (
                np.cross(points[ix[u]], points[ix[v]])
                for u, v in zip(cyc, cyc[1:] + cyc[:1])
            ),
            np.zeros(3),
        )
        cycle_n = cycle_n / np.linalg.norm(cycle_n)
        for u, v in zip(cyc, cyc[1:] + cyc[:1]):
            edge = points[ix[v]] - points[ix[u]]
            en = float(np.linalg.norm(edge))
            for j in cyc:
                if j in (u, v):
                    continue
                values.append(
                    float(np.dot(np.cross(edge, points[ix[j]] - points[ix[u]]), cycle_n)) / en
                )
                labels.append(("polygon", fi, [u, v], j))
    return np.asarray(values), labels


class Problem:
    def __init__(self, ids, source, faces):
        self.ids = ids
        self.source = source
        self.faces = faces
        self.chart = Chart(ids, source)
        self.forced = forced_rail_edges()
        p0, _ = self.chart.coordinates(np.zeros(44))
        m0 = core.mechanics(ids, p0, faces)
        self.g0, self.mech_labels = core.signed_guards(m0, faces, "escape")
        self.top0, self.top_labels = topology_guards(ids, p0, faces)
        if not np.all(self.top0 > 0.0):
            worst = sorted(zip(self.top0.tolist(), self.top_labels), key=lambda z: z[0])[:10]
            raise ValueError(("source has nonpositive fixed topology guard", worst))
        self.guard_scales = np.maximum(0.03, np.abs(self.g0))
        self.top_scales = np.maximum(1e-7, self.top0)
        self.critical = np.asarray([
            (lab[0] == "S-" and frozenset(lab[1]) == core.SFAR)
            or (lab[0] == "U-" and lab[1] == 54)
            or (lab[0] == "H-" and tuple(sorted(lab[1])) in core.TARGET_H)
            for lab in self.mech_labels
        ], dtype=bool)
        if int(np.sum(self.critical)) != 4:
            raise AssertionError(int(np.sum(self.critical)))

    def evaluate(self, x, include_topology=True):
        points, den = self.chart.coordinates(x)
        if points is None:
            raise ValueError(("projective denominator", float(np.min(den))))
        mechanics = core.mechanics(self.ids, points, self.faces)
        guards, labels = core.signed_guards(mechanics, self.faces, "escape")
        if labels != self.mech_labels:
            raise AssertionError("mechanics guard labels changed")
        topology = None
        if include_topology:
            topology, labels = topology_guards(self.ids, points, self.faces)
            if labels != self.top_labels:
                raise AssertionError("topology guard labels changed")
        return points, den, guards, topology, mechanics

    def fresh(self, points):
        audit, faces, mechanics = core.fresh_audit(self.ids, points, self.faces)
        edges, _ = core.edge_lattice(faces)
        audit["all_forced_rail_edges_present"] = self.forced <= set(edges)
        audit["missing_forced_rail_edges"] = [
            list(e) for e in sorted(self.forced - set(edges))
        ]
        audit["edge_0_1_present"] = (0, 1) in edges
        return audit, faces, mechanics


def finite_jacobian(problem: Problem, x: np.ndarray, step: float):
    _, _, g0, t0, _ = problem.evaluate(x)
    jm = np.zeros((len(g0), len(x)))
    jt = np.zeros((len(t0), len(x)))
    for k in range(len(x)):
        samples = {}
        h = step
        for _ in range(8):
            for sign in (1, -1):
                if sign in samples:
                    continue
                trial = x.copy()
                trial[k] += sign * h
                try:
                    _, _, gs, ts, _ = problem.evaluate(trial)
                    samples[sign] = (h, gs, ts)
                except (ValueError, FloatingPointError):
                    pass
            if samples:
                break
            h *= 0.1
        if 1 in samples and -1 in samples and samples[1][0] == samples[-1][0]:
            h = samples[1][0]
            jm[:, k] = (samples[1][1] - samples[-1][1]) / (2.0 * h)
            jt[:, k] = (samples[1][2] - samples[-1][2]) / (2.0 * h)
        elif 1 in samples:
            h, gs, ts = samples[1]
            jm[:, k] = (gs - g0) / h
            jt[:, k] = (ts - t0) / h
        elif -1 in samples:
            h, gs, ts = samples[-1]
            jm[:, k] = (g0 - gs) / h
            jt[:, k] = (t0 - ts) / h
        else:
            raise ValueError(("no finite-difference side available", k, problem.chart.names[k]))
    return g0, t0, jm, jt


def rank_record(problem: Problem, jm: np.ndarray, mask=None):
    if mask is None:
        mask = problem.critical
    mask = np.asarray(mask, dtype=bool)
    j = jm[mask]
    scales = problem.guard_scales[mask]
    jn = j / scales[:, None]
    names = [problem.mech_labels[k] for k in np.flatnonzero(mask)]
    out = {"critical_labels": names}
    for label, cols in (
        ("metric_projective_8", np.arange(8)),
        ("base_in_plane_36", np.arange(8, 44)),
        ("joint_44", np.arange(44)),
    ):
        block = jn[:, cols]
        singular = np.linalg.svd(block, compute_uv=False)
        tol = (float(singular[0]) * 1e-9) if len(singular) else 0.0
        out[label] = {
            "shape": list(block.shape),
            "rank_tolerance": tol,
            "rank": int(np.sum(singular > tol)),
            "singular_values": singular.tolist(),
        }
    out["normalized_critical_jacobian"] = jn.tolist()
    out["control_names"] = problem.chart.names
    return out


def packet(guards, labels, limit=24):
    rows = [
        {"value": float(v), "feature": lab}
        for v, lab in sorted(zip(guards, labels), key=lambda z: z[0])
    ]
    return rows[:limit]


def solve_lp(problem: Problem, x, guards, topology, jm, jt, rho,
             topology_retention, topology_reference):
    n = len(x)
    # (g + J dx)/scale >= tau for every target mechanics guard.
    aub_mech = np.hstack((
        -jm / problem.guard_scales[:, None],
        np.ones((len(guards), 1)),
    ))
    bub_mech = guards / problem.guard_scales

    floor = topology_retention * topology_reference
    aub_top = np.hstack((
        -jt / problem.top_scales[:, None],
        np.zeros((len(topology), 1)),
    ))
    bub_top = (topology - floor) / problem.top_scales
    aub = np.vstack((aub_mech, aub_top))
    bub = np.concatenate((bub_mech, bub_top))
    objective = np.zeros(n + 1)
    objective[-1] = -1.0

    total_low = np.asarray([-0.8] * 3 + [-1.8] * 5 + [-2.5] * 36)
    total_high = -total_low
    bounds = []
    for k in range(n):
        bounds.append((max(-rho, total_low[k] - x[k]), min(rho, total_high[k] - x[k])))
    bounds.append((-10.0, 1.0))
    lp = linprog(objective, A_ub=aub, b_ub=bub, bounds=bounds, method="highs")
    return lp


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--iterations", type=int, default=28)
    ap.add_argument("--fd-step", type=float, default=2e-5)
    ap.add_argument("--trust", type=float, default=0.22)
    ap.add_argument("--topology-retention", type=float, default=0.01)
    ap.add_argument("--start-json", help="initialize the first eight controls from a theta JSON")
    ap.add_argument("--source-csv", default=str(SOURCE))
    ap.add_argument("--faces-json", default=str(FACES_SOURCE))
    ap.add_argument("--output", default="row54_guarded_escape.json")
    ap.add_argument("--csv-output", default="row54_guarded_escape_best.csv")
    args = ap.parse_args()

    ids, source, faces = load_problem(args.source_csv, args.faces_json)
    problem = Problem(ids, source, faces)
    x = np.zeros(44)
    if args.start_json:
        start_record = json.load(open(args.start_json))
        x[:8] = np.asarray(start_record["theta"], dtype=float)
    _, _, start_guards, topology_reference, _ = problem.evaluate(x)
    rho = args.trust
    trajectory = []
    best = None
    rank = None
    active_rank = None

    for iteration in range(args.iterations):
        guards, topology, jm, jt = finite_jacobian(problem, x, args.fd_step)
        if rank is None:
            rank = rank_record(problem, jm)
            active_rank = rank_record(problem, jm, guards <= 0.0)
        points, den, _, _, _ = problem.evaluate(x)
        fresh, _, _ = problem.fresh(points)
        normalized_min = float(np.min(guards / problem.guard_scales))
        critical_min = float(np.min(guards[problem.critical] / problem.guard_scales[problem.critical]))
        state = {
            "iteration": iteration,
            "trust": rho,
            "normalized_min": normalized_min,
            "critical_normalized_min": critical_min,
            "hard_raw_margin": float(np.min(guards)),
            "minimum_topology_guard": float(np.min(topology)),
            "minimum_projective_denominator": float(np.min(den)),
            "negative_guard_count": int(np.sum(guards <= 0.0)),
            "worst_packet": packet(guards, problem.mech_labels),
            "fresh_hull_audit": fresh,
        }
        if best is None or normalized_min > best[0]:
            best = (normalized_min, x.copy(), state, points.copy())
        if np.min(guards) > 0.0 and fresh["faces_match_fixed_cell"] \
                and fresh["all_forced_rail_edges_present"]:
            state["verdict"] = "TARGET_FOUND"
            trajectory.append(state)
            break

        lp = solve_lp(
            problem, x, guards, topology, jm, jt, rho, args.topology_retention,
            topology_reference,
        )
        state["lp_success"] = bool(lp.success)
        state["lp_status"] = int(lp.status)
        state["lp_message"] = str(lp.message)
        state["lp_predicted_tau"] = None if not lp.success else float(lp.x[-1])
        accepted = False
        if lp.success:
            dx = lp.x[:-1]
            for alpha in (1.0, 0.5, 0.25, 0.125, 0.0625, 0.03125):
                trial = x + alpha * dx
                try:
                    tp, tden, tg, tt, _ = problem.evaluate(trial)
                    taudit, _, _ = problem.fresh(tp)
                except Exception:
                    continue
                trial_score = float(np.min(tg / problem.guard_scales))
                topology_ok = float(np.min(tt)) > 0.0
                hull_ok = (
                    taudit["f_vector"] == [61, 162, 103]
                    and taudit["faces_match_fixed_cell"]
                    and taudit["all_forced_rail_edges_present"]
                    and not taudit["edge_0_1_present"]
                )
                if topology_ok and hull_ok and trial_score > normalized_min + 1e-7:
                    x = trial
                    state["accepted_alpha"] = alpha
                    state["accepted_normalized_min"] = trial_score
                    state["accepted_minimum_topology_guard"] = float(np.min(tt))
                    state["accepted_minimum_projective_denominator"] = float(np.min(tden))
                    accepted = True
                    rho = min(0.45, rho * 1.15)
                    break
        if not accepted:
            state["accepted_alpha"] = None
            rho *= 0.5
        trajectory.append(state)
        print(json.dumps({
            "iteration": iteration,
            "score": normalized_min,
            "critical": critical_min,
            "negative": state["negative_guard_count"],
            "topology": state["minimum_topology_guard"],
            "rho": rho,
            "lp_tau": state.get("lp_predicted_tau"),
            "alpha": state.get("accepted_alpha"),
            "worst": state["worst_packet"][:6],
        }), flush=True)
        if rho < 1e-5:
            break

    best_score, best_x, best_state, best_points = best
    _, best_den, best_guards, best_topology, _ = problem.evaluate(best_x)
    best_audit, best_faces, _ = problem.fresh(best_points)
    verdict = (
        "TARGET_FOUND" if float(np.min(best_guards)) > 0.0
        and best_audit["faces_match_fixed_cell"]
        and best_audit["all_forced_rail_edges_present"]
        else "NO_TARGET_BEST_GUARDED_PACKET"
    )
    with (HERE / args.csv_output).open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(("source_id", "x", "y", "z"))
        for i, p in zip(ids, best_points):
            w.writerow([i, *[format(float(v), ".17g") for v in p]])
    faces_output = Path(args.csv_output).with_suffix("").name + "_faces.json"
    json.dump(best_faces, (HERE / faces_output).open("w"), indent=2)
    record = {
        "version": 1,
        "verdict": verdict,
        "source": str(args.source_csv),
        "faces_source": str(args.faces_json),
        "chart": {
            "dimension": 44,
            "controls": problem.chart.names,
            "base_cycle": BASE_CYCLE,
            "base_control_scales": problem.chart.base_scales,
            "base_u": problem.chart.base_u.tolist(),
            "base_v": problem.chart.base_v.tolist(),
            "transform": (
                "move each base row in its common plane; then fixed-source-normalized "
                "projective + trace-free SPD map"
            ),
        },
        "rank_revealing_jacobian_at_source": rank,
        "rank_revealing_active_packet_at_start": active_rank,
        "guarded_lp": {
            "topology_retention": args.topology_retention,
            "finite_difference_step": args.fd_step,
            "initial_trust": args.trust,
            "start_json": args.start_json,
            "start_negative_guard_count": int(np.sum(start_guards <= 0.0)),
        },
        "best": {
            "normalized_min": best_score,
            "parameters": best_x.tolist(),
            "hard_raw_margin": float(np.min(best_guards)),
            "minimum_topology_guard": float(np.min(best_topology)),
            "minimum_projective_denominator": float(np.min(best_den)),
            "negative_guard_count": int(np.sum(best_guards <= 0.0)),
            "worst_packet": packet(best_guards, problem.mech_labels, limit=40),
            "critical_guards": [
                {"value": float(best_guards[k]), "feature": problem.mech_labels[k]}
                for k in np.flatnonzero(problem.critical)
            ],
            "fresh_hull_audit": best_audit,
            "coordinates": args.csv_output,
            "fixed_expected_faces": faces_output,
        },
        "trajectory": trajectory,
    }
    json.dump(record, (HERE / args.output).open("w"), indent=2)
    print(json.dumps({
        "verdict": verdict,
        "rank": {k: v["rank"] for k, v in rank.items() if isinstance(v, dict) and "rank" in v},
        "best_normalized_min": best_score,
        "best_hard_raw_margin": float(np.min(best_guards)),
        "negative_guard_count": int(np.sum(best_guards <= 0.0)),
        "critical_guards": record["best"]["critical_guards"],
        "worst_packet": record["best"]["worst_packet"][:12],
        "fresh": best_audit,
    }, indent=2), flush=True)


if __name__ == "__main__":
    main()
