#!/usr/bin/env python3
"""Thicken the near-zero guards in the strict round-eight far cell.

The ordinary hard-minimum SLP stalls because the old round-four determinant,
the two previously bypassed U-H identities, and the new round-eight
determinant are simultaneously tiny.  This script uses the same 19 direct
geometry plus eight projective/trace-free-metric coordinates, but keeps the
four current target defects and the new round-eight determinant tangent while
maximising the old round-four determinant.  Nonlinear drift is projected back
to those five levels and every accepted point is rebuilt as an actual hull.

This is a discovery/materialisation step.  Any useful endpoint still needs an
exact/directed path certificate before it is treated as a theorem.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CIRCUIT = ROOT / "tracks/circuit_atlas"
sys.path[:0] = [str(HERE), str(CIRCUIT)]

from actual_grouped import evaluate, summarize  # noqa: E402
from row54_direct_actual_search import DirectActual, read_points  # noqa: E402
from row54_full_minimax import BASE, SHORT_RAIL, guards  # noqa: E402
from row54_joint_actual_search import write_csv  # noqa: E402
import row54_four_residual_search as core  # noqa: E402


ALT_ROUTE = [228, 198, 263, 9, 8]
KEEP_KEYS = [
    ("U-", 54),
    ("H-", (6, 7)),
    ("S-", (7, 8, 245)),
    ("H-", (198, 263)),
]
OLD_GUARD_KEYS = [("U-", 263), ("U-", 1)]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--source",
        type=Path,
        default=HERE / "row54_round8_far_route_slp_tangent_best.csv",
    )
    ap.add_argument("--epsilon", type=float, default=2e-8)
    ap.add_argument("--objective", choices=("old_quad", "support230"),
                    default="old_quad")
    ap.add_argument("--old-quad-target", type=float, default=2e-9)
    ap.add_argument("--support-target", type=float, default=2e-9)
    ap.add_argument("--output", type=Path,
                    default=HERE / "row54_round8_far_guard_buffer.json")
    args = ap.parse_args()

    ids, source = read_points(args.source)
    direct = DirectActual(ids, source)
    if args.objective == "support230":
        # The original direct chart moves only base/mechanics vertices.  The
        # circuit (198,228,229,230) is consequently invariant up to the
        # projective/linear factor and cannot be thickened.  Vertex 230 has a
        # purely triangular star in this cell, so add its three physical
        # coordinates as the minimal genuine support-circuit actuator.
        direct.controls.extend(
            (230, 0.005 * axis) for axis in np.eye(3)
        )
    _, faces, _ = core.group_maximal_faces(ids, source)
    source_keys = {frozenset(c) for c in faces}
    local = {i: k for k, i in enumerate(ids)}
    n_direct = len(direct.controls)
    n = n_direct + 8

    _, labels = guards(core.mechanics(ids, source, faces), faces)

    def label_key(label):
        kind, item = label
        if isinstance(item, list):
            item = tuple(sorted(item))
        return kind, item

    lookup = {label_key(label): k for k, label in enumerate(labels)}
    keep_indices = np.asarray([lookup[key] for key in KEEP_KEYS], int)
    old_guard_indices = np.asarray([lookup[key] for key in OLD_GUARD_KEYS], int)

    def construct(z: np.ndarray):
        q = direct.construct(z[:n_direct])
        origin = source.mean(axis=0)
        scale = float(np.sqrt(np.mean(np.sum((source - origin) ** 2,
                                             axis=1))))
        qn = (q - origin) / scale
        theta = z[n_direct:]
        den = 1.0 + qn @ theta[:3]
        if np.min(den) <= 0.08:
            return None, den
        a, b, c, d, e = theta[3:]
        h = np.array([[a, b, c], [b, d, e],
                      [c, e, -a - d]], dtype=float)
        transformed = (qn / den[:, None]) @ core.expm(h).T
        return origin + scale * transformed, den

    def centroid_longdouble(points: np.ndarray) -> np.ndarray:
        p = np.asarray(points, dtype=np.longdouble)
        origin = np.mean(p, axis=0)
        d6 = np.longdouble(0)
        moment24 = np.zeros(3, dtype=np.longdouble)
        for cycle in faces:
            c = [local[i] for i in cycle]
            a = p[c[0]] - origin
            for j in range(1, len(c) - 1):
                b = p[c[j]] - origin
                q = p[c[j + 1]] - origin
                det = np.dot(a, np.cross(b, q))
                d6 += det
                moment24 += det * (a + b + q)
        return origin + moment24 / (4 * d6)

    def endpoint_numerators(points: np.ndarray) -> np.ndarray:
        p = np.asarray(points, dtype=np.longdouble)
        centroid = centroid_longdouble(p)
        x10 = p[local[10]] - centroid
        x263 = p[local[263]] - centroid
        x1 = p[local[1]] - centroid
        x54 = p[local[54]] - centroid
        return np.asarray([
            np.dot(x263, x263 - x10),
            -np.dot(x1, x54 - x1),
        ], dtype=np.longdouble)

    def normalized_det(points: np.ndarray, quad: tuple[int, ...],
                       sign: float) -> float:
        p = np.asarray(points, float)
        q = [p[local[i]] for i in quad]
        det = float(np.dot(q[1] - q[0],
                           np.cross(q[2] - q[0], q[3] - q[0])))
        scale = max(float(np.sqrt(np.mean(np.sum(
            (p - np.mean(p, axis=0)) ** 2, axis=1)))), 1e-300)
        return sign * det / scale**3

    def old_quad(points: np.ndarray) -> float:
        # Positive on the (8,245) diagonal side used by the far endpoint.
        return normalized_det(points, (7, 8, 245, 246), -1.0)

    def new_quad(points: np.ndarray) -> float:
        # Positive on the round-eight far side.
        return normalized_det(points, (9, 198, 263, 264), 1.0)

    support_source = np.asarray(source, float)
    support_quad = [support_source[local[i]]
                    for i in (198, 228, 229, 230)]
    support_raw_source = float(np.dot(
        support_quad[1] - support_quad[0],
        np.cross(support_quad[2] - support_quad[0],
                 support_quad[3] - support_quad[0])))
    assert support_raw_source != 0
    support_sign = 1.0 if support_raw_source > 0 else -1.0

    def support230(points: np.ndarray) -> float:
        """Directed normalized circuit det(198,228,229,230)."""
        return normalized_det(points, (198, 228, 229, 230), support_sign)

    def fixed(z: np.ndarray):
        p, den = construct(z)
        if p is None:
            return None
        try:
            g = guards(core.mechanics(ids, p, faces), faces)[0]
        except Exception:
            return None
        return g, p, den

    rejection = {"reason": None}

    def actual(z: np.ndarray):
        rejection["reason"] = None
        packet = fixed(z)
        if packet is None:
            rejection["reason"] = "fixed-evaluation"
            return None
        g, p, den = packet
        if np.any(endpoint_numerators(p) > 0):
            rejection["reason"] = "old-u-h-numerator"
            return None
        if old_quad(p) <= 0 or new_quad(p) <= 0:
            rejection["reason"] = "prior-quad-side"
            return None
        rebuilt = evaluate({i: p[k] for k, i in enumerate(ids)},
                           coplanar_rel=1e-11)
        if not rebuilt.valid:
            rejection["reason"] = "fresh-hull-invalid"
            return None
        keys = {frozenset(f["cycle"]) for f in rebuilt.faces}
        edges = set(rebuilt.edges)
        rail_ok = all(
            tuple(sorted(edge)) in edges
            for path in (SHORT_RAIL, ALT_ROUTE)
            for edge in zip(path, path[1:])
        )
        if set(rebuilt.active) != set(ids):
            rejection["reason"] = (
                "active-row-change:missing="
                f"{sorted(set(ids) - set(rebuilt.active))}:extra="
                f"{sorted(set(rebuilt.active) - set(ids))}"
            )
            return None
        if keys != source_keys:
            rejection["reason"] = "face-lattice-change"
            return None
        if BASE not in keys:
            rejection["reason"] = "base-loss"
            return None
        if not rail_ok:
            rejection["reason"] = "route-loss"
            return None
        if rebuilt.topology_margin <= 1e-12:
            rejection["reason"] = "topology-floor"
            return None
        return g, p, den, rebuilt

    z0 = np.zeros(n)
    base = actual(z0)
    if base is None:
        raise RuntimeError("source is not the expected strict far cell")
    g0, p0 = base[0], base[1]

    # Central finite-difference first jet in the identity chart.
    jac = np.zeros((len(g0), n))
    old_jac = np.zeros(n)
    new_jac = np.zeros(n)
    support_jac = np.zeros(n)
    for j in range(n):
        step = np.zeros(n)
        step[j] = args.epsilon
        plus = fixed(z0 + step)
        minus = fixed(z0 - step)
        if plus is None or minus is None:
            raise RuntimeError(f"finite difference failed in column {j}")
        jac[:, j] = (plus[0] - minus[0]) / (2 * args.epsilon)
        old_jac[j] = (old_quad(plus[1]) - old_quad(minus[1])) / (
            2 * args.epsilon)
        new_jac[j] = (new_quad(plus[1]) - new_quad(minus[1])) / (
            2 * args.epsilon)
        support_jac[j] = (support230(plus[1]) - support230(minus[1])) / (
            2 * args.epsilon)

    # Preserve all four target residuals and the round-eight far determinant
    # to first order.  Keep the two old U-H identities from shrinking.  The
    # objective maximises the old round-four determinant derivative.
    if args.objective == "old_quad":
        equality = np.vstack([jac[keep_indices], new_jac])
        objective_jac = old_jac
    else:
        equality = np.vstack([jac[keep_indices], old_jac, new_jac,
                              jac[old_guard_indices]])
        objective_jac = support_jac
    lp = linprog(
        -objective_jac,
        A_ub=-jac[old_guard_indices],
        b_ub=np.zeros(len(old_guard_indices)),
        A_eq=equality,
        b_eq=np.zeros(equality.shape[0]),
        bounds=[(-1.0, 1.0)] * n,
        method="highs",
    )
    if not lp.success:
        raise RuntimeError(f"buffer LP failed: {lp.message}")
    direction = lp.x

    # Projection uses the source first jet, which is sufficient for the tiny
    # buffer step.  Retain exactly the levels used by the selected equality
    # system: four target defects plus the new quad for the old-quad buffer;
    # four defects plus both prior quads for the support-230 buffer.
    if args.objective == "old_quad":
        target_levels = np.r_[g0[keep_indices], new_quad(p0)]
    else:
        target_levels = np.r_[g0[keep_indices], old_quad(p0), new_quad(p0),
                              g0[old_guard_indices]]
    gram = equality @ equality.T

    def project(candidate: np.ndarray) -> np.ndarray | None:
        out = candidate.copy()
        for _ in range(12):
            packet = fixed(out)
            if packet is None:
                return None
            if args.objective == "old_quad":
                levels = np.r_[packet[0][keep_indices], new_quad(packet[1])]
            else:
                levels = np.r_[packet[0][keep_indices],
                               old_quad(packet[1]), new_quad(packet[1]),
                               packet[0][old_guard_indices]]
            error = target_levels - levels
            if float(np.max(np.abs(error))) < 2e-14:
                break
            out += equality.T @ np.linalg.solve(gram, error)
        return out

    old0 = old_quad(p0)
    new0 = new_quad(p0)
    support0 = support230(p0)
    objective0 = old0 if args.objective == "old_quad" else support0
    objective_target = (args.old_quad_target if args.objective == "old_quad"
                        else args.support_target)
    target_alpha = max((objective_target - objective0)
                       / max(float(objective_jac @ direction), 1e-300), 0.0)
    scales = sorted(set([
        target_alpha * f for f in
        (0.05, 0.1, 0.2, 0.35, 0.5, 0.7, 0.85, 1.0, 1.2, 1.5, 2.0)
    ] + [10.0**k for k in range(-10, -1)]))
    records = []
    best = (objective0, z0, base)
    for alpha in scales:
        if not np.isfinite(alpha) or alpha <= 0:
            continue
        candidate = project(z0 + alpha * direction)
        if candidate is None:
            records.append({"alpha": alpha, "valid": False,
                            "reason": "projection"})
            continue
        packet = actual(candidate)
        if packet is None:
            records.append({"alpha": alpha, "valid": False,
                            "reason": rejection["reason"] or "actual"})
            continue
        g, p, _, rebuilt = packet
        entry = {
            "alpha": alpha,
            "valid": True,
            "old_quad": old_quad(p),
            "new_quad": new_quad(p),
            "support230": support230(p),
            "old_u_h_guards": g[old_guard_indices].tolist(),
            "keep_values": g[keep_indices].tolist(),
            "topology_margin": rebuilt.topology_margin,
            "class": [len(rebuilt.stable), len(rebuilt.unstable),
                      len(rebuilt.saddles)],
            "maximum_point_displacement": float(np.max(np.abs(p - p0))),
        }
        records.append(entry)
        objective_value = (entry["old_quad"] if args.objective == "old_quad"
                           else entry["support230"])
        if objective_value > best[0]:
            best = (objective_value, candidate, packet)

    if best[0] <= objective0:
        raise RuntimeError("no strict actual-cell buffer endpoint found")
    _, best_z, best_packet = best
    best_g, best_points, _, best_actual = best_packet
    write_csv(args.output.with_name(args.output.stem + "_best.csv"),
              ids, best_points)
    args.output.with_name(args.output.stem + "_best_faces.json").write_text(
        json.dumps([face["cycle"] for face in best_actual.faces], indent=2)
        + "\n"
    )

    report = {
        "version": 1,
        "method": "27D tangent guard buffer in the round-eight far cell",
        "objective": args.objective,
        "source": str(args.source),
        "keep_keys": [[kind, item] for kind, item in KEEP_KEYS],
        "old_guard_keys": [[kind, item] for kind, item in OLD_GUARD_KEYS],
        "initial": {
            "old_quad": old0,
            "new_quad": new0,
            "support230": support0,
            "old_u_h_guards": g0[old_guard_indices].tolist(),
            "keep_values": g0[keep_indices].tolist(),
            "actual": summarize(base[3]),
        },
        "first_jet": {
            "rank_equalities": int(np.linalg.matrix_rank(equality)),
            "nullity": int(n - np.linalg.matrix_rank(equality)),
            "old_quad_derivative": float(old_jac @ direction),
            "new_quad_derivative": float(new_jac @ direction),
            "support230_derivative": float(support_jac @ direction),
            "objective_derivative": float(objective_jac @ direction),
            "keep_derivatives": (jac[keep_indices] @ direction).tolist(),
            "old_u_h_derivatives": (
                jac[old_guard_indices] @ direction).tolist(),
            "direction": direction.tolist(),
            "target_alpha": target_alpha,
        },
        "records": records,
        "best": {
            "parameters": best_z.tolist(),
            "old_quad": old_quad(best_points),
            "new_quad": new_quad(best_points),
            "support230": support230(best_points),
            "old_u_h_guards": best_g[old_guard_indices].tolist(),
            "keep_values": best_g[keep_indices].tolist(),
            "actual": summarize(best_actual),
            "topology_margin": best_actual.topology_margin,
            "endpoint_numerators": [float(x) for x in
                                    endpoint_numerators(best_points)],
            "coordinates": args.output.with_name(
                args.output.stem + "_best.csv").name,
            "faces": args.output.with_name(
                args.output.stem + "_best_faces.json").name,
        },
        "scope": (
            "floating-point materialisation in one frozen 27D identity chart; "
            "not an exact continuum certificate"
        ),
    }
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report["first_jet"], indent=2))
    print(json.dumps(report["best"], indent=2))


if __name__ == "__main__":
    main()
