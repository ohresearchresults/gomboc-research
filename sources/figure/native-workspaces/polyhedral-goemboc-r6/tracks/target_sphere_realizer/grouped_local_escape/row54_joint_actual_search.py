#!/usr/bin/env python3
"""Joint actual-hull escape search in the row54/q246/metric chart.

Unlike the fixed-lattice searches, every objective call rebuilds the convex
hull, groups maximal faces, recomputes the volume centroid, and then evaluates
all face/vertex/edge decisions.  The only combinatorial guards are all 61
active vertices, the enlarged base, U8, and both complete rail paths.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution, minimize

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CIRCUIT = ROOT / "tracks/circuit_atlas"
sys.path[:0] = [str(HERE), str(CIRCUIT)]

from actual_grouped import evaluate as actual_evaluate, summarize  # noqa: E402
import materialize_row54_cells as mat  # noqa: E402
import row54_four_residual_search as core  # noqa: E402


BASE = frozenset(range(17)) | {54}
SHORT_RAIL = [228] + list(range(229, 247)) + [8]
LONG_RAIL = [228] + list(range(247, 265)) + [8]
RAIL_EDGES = {
    tuple(sorted(edge))
    for path in (SHORT_RAIL, LONG_RAIL)
    for edge in zip(path, path[1:])
}


def write_csv(path: Path, ids, points):
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(("source_id", "x", "y", "z"))
        for i, p in zip(ids, points):
            w.writerow([i, *[format(float(x), ".17g") for x in p]])


def feature_guards(actual):
    """Positive exactly for target class: base stable, U8, no saddles."""
    values, labels = [], []
    for k, face in enumerate(actual.faces):
        keep = frozenset(face["cycle"]) == BASE
        z = float(actual.face_decisions[k])
        values.append(z if keep else -z)
        labels.append(("S+" if keep else "S-", list(face["cycle"])))
    for i, z0 in actual.vertex_decisions.items():
        keep = i == 8
        z = float(z0)
        values.append(z if keep else -z)
        labels.append(("U+" if keep else "U-", int(i)))
    for edge, z0 in actual.edge_decisions.items():
        values.append(-float(z0))
        labels.append(("H-", list(edge)))
    return np.asarray(values), labels


class JointActual:
    def __init__(self, ids, raw, robust_theta):
        self.ids = list(ids)
        self.raw = np.asarray(raw)
        self.robust_theta = np.asarray(robust_theta)
        self.ix = {i: k for k, i in enumerate(ids)}
        self.robust, self.robust_den = mat.robust_transform_with_fixed_reference(
            self.raw, self.raw, self.robust_theta
        )

        a = self.raw[self.ix[7]]
        self.n = np.cross(self.raw[self.ix[8]] - a,
                          self.raw[self.ix[245]] - a)
        self.n /= np.linalg.norm(self.n)
        self.original_depth = float(np.dot(
            self.n, self.raw[self.ix[246]] - a
        ))
        self.wall_projection = (
            self.raw[self.ix[246]] - self.original_depth * self.n
        )
        self.u = self.raw[self.ix[8]] - a
        self.u /= np.linalg.norm(self.u)
        self.v = np.cross(self.n, self.u)

        self.calls = 0
        self.feasible_calls = 0
        self.best_score = (-np.inf, None, None)
        self.best_hard = (-np.inf, None, None)
        self.best_by_class = {}

    def construct(self, x):
        exterior, fraction, tangent_a, tangent_b, normal_depth = x[:5]
        moved = self.raw.copy()
        moved[self.ix[246]] = (
            self.wall_projection + tangent_a * self.u + tangent_b * self.v
            - np.sign(self.original_depth) * normal_depth * self.n
        )
        robust_moved, den0 = mat.robust_transform_with_fixed_reference(
            moved, self.raw, self.robust_theta
        )

        # q54 is placed in the post-robust base plane; build_wall_rows also
        # touches q246, so restore the independently moved robust q246.
        points = core.build_wall_rows(
            self.ids, self.robust, 0.0, exterior, fraction
        )
        points[self.ix[246]] = robust_moved[self.ix[246]]
        transformed, den1 = core.transform(points, np.asarray(x[5:13]))
        return transformed, den0, den1

    def audit(self, x):
        points, den0, den1 = self.construct(np.asarray(x))
        if points is None:
            return None, None, None, {
                "reason": "additional projective pole",
                "minimum_denominator": float(np.min(den1)),
            }
        actual = actual_evaluate(
            {i: points[k] for k, i in enumerate(self.ids)},
            coplanar_rel=1e-11,
        )
        if not actual.valid:
            return points, actual, None, {"reason": actual.error}
        edges = set(actual.edges)
        face_keys = {frozenset(f["cycle"]) for f in actual.faces}
        required = {
            "all61": len(actual.active) == 61 and set(actual.active) == set(self.ids),
            "base": BASE in face_keys,
            "u8_active": 8 in actual.vertex_decisions,
            "rails": RAIL_EDGES <= edges,
            "topology_open": actual.topology_margin > 1e-12,
            "robust_den": float(np.min(den0)) > 0.05,
            "metric_den": float(np.min(den1)) > 0.08,
        }
        if not all(required.values()):
            return points, actual, None, {
                "reason": "required guard failed", "required": required,
                "minimum_robust_denominator": float(np.min(den0)),
                "minimum_metric_denominator": float(np.min(den1)),
            }
        guards, labels = feature_guards(actual)
        return points, actual, (guards, labels), {
            "reason": None, "required": required,
            "minimum_robust_denominator": float(np.min(den0)),
            "minimum_metric_denominator": float(np.min(den1)),
        }

    def objective(self, x, report=False):
        self.calls += 1
        points, actual, packet, meta = self.audit(x)
        if packet is None:
            # Keep invalid cells strictly below every feasible sign score.
            return 3.0
        self.feasible_calls += 1
        guards, labels = packet
        # All decisions emitted by actual_grouped are dimensionless.  This
        # monotone balancing keeps large correct face margins from drowning
        # the few sign walls that still obstruct escape.
        balanced = guards / (0.02 + np.abs(guards))
        order = np.argsort(balanced)
        score = (
            0.56 * float(balanced[order[0]])
            + 0.25 * float(np.mean(balanced[order[:6]]))
            + 0.12 * float(np.mean(balanced[order[:20]]))
            + 0.07 * float(np.mean(balanced))
        )
        hard = float(np.min(guards))
        worst = [
            {"value": float(guards[k]), "feature": labels[k]}
            for k in np.argsort(guards)[:16]
        ]
        key = tuple((len(actual.stable), len(actual.unstable), len(actual.saddles)))
        if key not in self.best_by_class or hard > self.best_by_class[key][0]:
            self.best_by_class[key] = (hard, np.asarray(x).copy())
        if hard > self.best_hard[0]:
            self.best_hard = (hard, np.asarray(x).copy(), worst)
            print("hard", self.calls, hard, "class", key,
                  "f", (len(actual.active), len(actual.edges), len(actual.faces)),
                  "worst", worst[:5], flush=True)
        if score > self.best_score[0]:
            self.best_score = (score, np.asarray(x).copy(), worst)
            if report:
                print("score", self.calls, score, "hard", hard,
                      "class", key, "worst", worst[:5], flush=True)
        if hard > 0.0:
            print("OPEN_TARGET", self.calls, hard, key, flush=True)
        return -score


def encode_audit(search, x):
    points, actual, packet, meta = search.audit(x)
    out = {
        "parameters": np.asarray(x).tolist(),
        "chart": {
            "row54_exterior": float(x[0]),
            "row54_edge_fraction": float(x[1]),
            "row246_tangent_a": float(x[2]),
            "row246_tangent_b": float(x[3]),
            "row246_far_signed_depth": float(x[4]),
            "additional_projective_spd_theta": np.asarray(x[5:13]).tolist(),
        },
        "meta": meta,
        "fresh_actual": None if actual is None else summarize(actual),
    }
    if packet is not None:
        guards, labels = packet
        order = np.argsort(guards)
        out["hard_margin"] = float(guards[order[0]])
        out["worst_guards"] = [
            {"value": float(guards[k]), "feature": labels[k]}
            for k in order[:30]
        ]
        out["rail_edges_present"] = RAIL_EDGES <= set(actual.edges)
        out["base_face_present"] = BASE in {
            frozenset(f["cycle"]) for f in actual.faces
        }
    return points, out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=831571)
    ap.add_argument("--generations", type=int, default=18)
    ap.add_argument("--popsize", type=int, default=6)
    ap.add_argument("--local-iters", type=int, default=550)
    ap.add_argument("--start", type=Path,
                    default=HERE / "row54_full_minimax_guarded.json")
    ap.add_argument("--output", type=Path,
                    default=HERE / "row54_joint_actual.json")
    args = ap.parse_args()

    ids, raw = mat.load_csv(CIRCUIT / "target_sphere_rebuilt.csv")
    robust_theta = np.asarray(
        json.load((CIRCUIT / "robust_rebuilt_fast.json").open())["theta"]
    )
    start_record = json.load(args.start.open())
    metric_start = np.asarray(
        start_record.get("best_raw_hard_theta", start_record["theta"])
    )
    x0 = np.r_[0.01, 0.9, -0.21, 0.0, 1.0e-5, metric_start]
    bounds = [
        (0.0015, 0.055),       # row54 exterior
        (0.58, 0.985),         # row54 edge fraction
        (-0.34, -0.08),        # q246 tangent u
        (-0.14, 0.14),         # q246 tangent v
        (-0.0025, 0.006),      # signed far depth; includes the quad wall
        (-0.72, 0.72), (-0.72, 0.72), (-0.72, 0.72),
        (-1.58, 1.58), (-1.58, 1.58), (-1.58, 1.58),
        (-1.58, 1.58), (-1.58, 1.58),
    ]
    search = JointActual(ids, raw, robust_theta)
    search.objective(x0, report=True)

    # First exploit the known near-minimax cell.  This cheaply reveals
    # whether the four residual walls have a local common positive side.
    local0 = None
    if args.local_iters:
        local0 = minimize(
            lambda z: search.objective(z, report=True), x0,
            method="Nelder-Mead", bounds=bounds,
            options={"maxiter": args.local_iters,
                     "xatol": 2e-10, "fatol": 2e-10},
        )
    de_start = (search.best_score[1]
                if search.best_score[1] is not None else x0)
    de = differential_evolution(
        lambda z: search.objective(z, report=True), bounds,
        x0=de_start, seed=args.seed, maxiter=args.generations,
        popsize=args.popsize, polish=False, tol=1e-8,
        updating="immediate", workers=1,
    )

    candidates = [
        ("best_hard", search.best_hard[1]),
        ("best_score", search.best_score[1]),
        ("de", de.x),
    ]
    audited = []
    for name, x in candidates:
        if x is None:
            continue
        points, rec = encode_audit(search, x)
        rec["name"] = name
        audited.append(rec)
        if name == "best_hard" and points is not None:
            write_csv(args.output.with_name(args.output.stem + "_best.csv"),
                      ids, points)
            with args.output.with_name(args.output.stem + "_best_faces.json").open("w") as f:
                json.dump([face["cycle"] for face in
                           search.audit(x)[1].faces], f, indent=2)

    by_class = {
        str(k): {"hard_margin": float(v[0]), "parameters": v[1].tolist()}
        for k, v in sorted(search.best_by_class.items())
    }
    output = {
        "version": 1,
        "method": "joint q54/q246/projective-SPD; fresh actual hull every call",
        "robust_theta": robust_theta.tolist(),
        "start_parameters": x0.tolist(),
        "calls": search.calls,
        "feasible_calls": search.feasible_calls,
        "best_raw_hard_seen": float(search.best_hard[0]),
        "best_score_seen": float(search.best_score[0]),
        "best_by_actual_class": by_class,
        "audited_candidates": audited,
        "local_message": None if local0 is None else str(local0.message),
        "de_message": str(de.message),
    }
    args.output.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
