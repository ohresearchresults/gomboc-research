#!/usr/bin/env python3
"""Combined 19 direct-geometry + 8 metric hard-minimum SLP."""
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
from row54_full_minimax import guards, SHORT_RAIL, LONG_RAIL, BASE  # noqa: E402
from row54_joint_actual_search import write_csv  # noqa: E402
import row54_four_residual_search as core  # noqa: E402

ALT_ROUTE = (228, 198, 263, 9, 8)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path,
                    default=HERE / "row54_metric_hard_slp_best.csv")
    ap.add_argument("--iterations", type=int, default=55)
    ap.add_argument("--trust", type=float, default=0.001)
    ap.add_argument("--epsilon", type=float, default=2e-6)
    ap.add_argument("--stop-on-class-change", action="store_true",
                    help="stop and save the first accepted mechanics-class event")
    ap.add_argument("--protect-u263-wall", action="store_true",
                    help="keep U263 and H(10,263) on their excluded side")
    ap.add_argument("--wall-floor", type=float, default=1e-8)
    ap.add_argument("--protect-u1-wall", action="store_true",
                    help="keep U1 and H(1,54) on their excluded side")
    ap.add_argument("--u1-wall-floor", type=float, default=1e-8)
    ap.add_argument("--directed-endpoint-signs", action="store_true",
                    help="enforce both shared endpoint numerators in long double")
    ap.add_argument("--deduplicate-endpoint-constraints", action="store_true",
                    help="LP uses one vertex row per exact endpoint identity")
    ap.add_argument("--identity-chart", action="store_true",
                    help="undo fixed normalization so theta=0 preserves source coordinates")
    ap.add_argument("--lp-guard-cutoff", type=float, default=None,
                    help="omit safely positive guards from the linearized LP only")
    ap.add_argument("--protect-quad-wall", action="store_true",
                    help="remain on the {7,8,245,246} far-diagonal side")
    ap.add_argument("--quad-wall-floor", type=float, default=5e-11,
                    help="minimum normalized directed four-point determinant")
    ap.add_argument("--quad-wall-tangent", action="store_true",
                    help="linearized steps are tangent to the far quad level")
    ap.add_argument("--new-quad-side", choices=("pre", "far"), default=None,
                    help="protect a side of det(9,198,263,264)=0")
    ap.add_argument("--new-quad-floor", type=float, default=5e-11,
                    help="minimum normalized directed new-quad determinant")
    ap.add_argument("--new-quad-tangent", action="store_true",
                    help="linearized steps are tangent to the new quad level")
    ap.add_argument("--round10-quad-side", choices=("pre", "far"), default=None,
                    help="protect a side of det(8,264,246,198)=0")
    ap.add_argument("--round10-quad-floor", type=float, default=5e-11,
                    help="minimum normalized round-10 quad determinant")
    ap.add_argument("--round10-quad-tangent", action="store_true",
                    help="linearized steps are tangent to the round-10 quad level")
    ap.add_argument("--round12-quad-side", choices=("pre", "far"), default=None,
                    help="protect a side of det(198,263,262,11)=0")
    ap.add_argument("--round12-quad-floor", type=float, default=5e-11,
                    help="minimum normalized round-12 quad determinant")
    ap.add_argument("--round12-quad-tangent", action="store_true",
                    help="linearized steps are tangent to the round-12 quad level")
    ap.add_argument("--allow-long-rail-loss", action="store_true",
                    help="require only the short literal rail")
    ap.add_argument("--require-alternate-route-positive", action="store_true",
                    help="preserve the positive-dot path 228-198-263-9-8")
    ap.add_argument("--output", type=Path,
                    default=HERE / "row54_combined_hard_slp.json")
    args = ap.parse_args()

    ids, source = read_points(args.source)
    direct = DirectActual(ids, source)
    _, faces, _ = core.group_maximal_faces(ids, source)
    source_keys = {frozenset(c) for c in faces}
    n_direct = len(direct.controls)
    n = n_direct + 8
    lower = np.r_[np.full(n_direct, -1.0),
                  np.full(3, -0.75), np.full(5, -1.6)]
    upper = -lower
    _, guard_labels = guards(core.mechanics(ids, source, faces), faces)

    def label_key(label):
        kind, item = label
        if isinstance(item, list):
            item = tuple(sorted(item))
        return kind, item

    guard_lookup = {label_key(label): k
                    for k, label in enumerate(guard_labels)}
    protected_indices = []
    protected_floors = []
    if args.protect_u263_wall:
        protected_indices.append(guard_lookup[("U-", 263)])
        protected_floors.append(args.wall_floor)
        if not args.deduplicate_endpoint_constraints:
            protected_indices.append(guard_lookup[("H-", (10, 263))])
            protected_floors.append(args.wall_floor)
    if args.protect_u1_wall:
        protected_indices.append(guard_lookup[("U-", 1)])
        protected_floors.append(args.u1_wall_floor)
        if not args.deduplicate_endpoint_constraints:
            protected_indices.append(guard_lookup[("H-", (1, 54))])
            protected_floors.append(args.u1_wall_floor)
    protected_floors = np.asarray(protected_floors, float)
    local = {i: k for k, i in enumerate(ids)}

    def centroid_longdouble(points):
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

    def directed_endpoint_numerators(points):
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

    def quad_far_guard(points):
        """Positive on the post-flip (8,245)-diagonal side."""
        p = np.asarray(points, float)
        q = [p[local[i]] for i in (7, 8, 245, 246)]
        det = float(np.dot(q[1] - q[0],
                           np.cross(q[2] - q[0], q[3] - q[0])))
        scale = max(float(np.sqrt(np.mean(np.sum(
            (p - np.mean(p, axis=0)) ** 2, axis=1)))), 1e-300)
        return -det / scale**3

    def new_quad_guard(points):
        """Positive on the selected side of det(9,198,263,264)=0."""
        p = np.asarray(points, float)
        q = [p[local[i]] for i in (9, 198, 263, 264)]
        det = float(np.dot(q[1] - q[0],
                           np.cross(q[2] - q[0], q[3] - q[0])))
        scale = max(float(np.sqrt(np.mean(np.sum(
            (p - np.mean(p, axis=0)) ** 2, axis=1)))), 1e-300)
        sign = -1.0 if args.new_quad_side == "pre" else 1.0
        return sign * det / scale**3

    def round10_quad_guard(points):
        """Positive on the selected side of det(8,264,246,198)=0."""
        p = np.asarray(points, float)
        q = [p[local[i]] for i in (8, 264, 246, 198)]
        det = float(np.dot(q[1] - q[0],
                           np.cross(q[2] - q[0], q[3] - q[0])))
        scale = max(float(np.sqrt(np.mean(np.sum(
            (p - np.mean(p, axis=0)) ** 2, axis=1)))), 1e-300)
        sign = -1.0 if args.round10_quad_side == "pre" else 1.0
        return sign * det / scale**3

    def round12_quad_guard(points):
        """Positive on the selected side of det(198,263,262,11)=0."""
        p = np.asarray(points, float)
        q = [p[local[i]] for i in (198, 263, 262, 11)]
        det = float(np.dot(q[1] - q[0],
                           np.cross(q[2] - q[0], q[3] - q[0])))
        scale = max(float(np.sqrt(np.mean(np.sum(
            (p - np.mean(p, axis=0)) ** 2, axis=1)))), 1e-300)
        sign = -1.0 if args.round12_quad_side == "pre" else 1.0
        return sign * det / scale**3

    def construct(z):
        q = direct.construct(z[:n_direct])
        if args.identity_chart:
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
            p = origin + scale * transformed
        else:
            p, den = core.transform(q, z[n_direct:])
        return p, den

    def fixed_values(z):
        p, den = construct(z)
        if p is None or np.min(den) <= 0.08:
            return None
        try:
            return guards(core.mechanics(ids, p, faces), faces)[0], p, den
        except Exception:
            return None

    def actual_valid(z):
        packet = fixed_values(z)
        if packet is None:
            return None
        g, p, den = packet
        if protected_indices and np.any(g[protected_indices] < protected_floors):
            return None
        if (args.protect_quad_wall
                and quad_far_guard(p) < args.quad_wall_floor):
            return None
        if (args.new_quad_side is not None
                and new_quad_guard(p) < args.new_quad_floor):
            return None
        if (args.round10_quad_side is not None
                and round10_quad_guard(p) < args.round10_quad_floor):
            return None
        if (args.round12_quad_side is not None
                and round12_quad_guard(p) < args.round12_quad_floor):
            return None
        actual = evaluate({i: p[k] for k, i in enumerate(ids)},
                          coplanar_rel=1e-11)
        if not actual.valid:
            return None
        keys = {frozenset(f["cycle"]) for f in actual.faces}
        edges = set(actual.edges)
        required_rails = (SHORT_RAIL,) if args.allow_long_rail_loss else (
            SHORT_RAIL, LONG_RAIL
        )
        rails = all(tuple(sorted(e)) in edges for path in required_rails
                    for e in zip(path, path[1:]))
        alt_positive = all(
            tuple(sorted(e)) in edges
            for e in zip(ALT_ROUTE, ALT_ROUTE[1:])
        ) and min(
            float(np.dot(p[local[a]] - actual.centroid,
                         p[local[b]] - actual.centroid))
            for a, b in zip(ALT_ROUTE, ALT_ROUTE[1:])
        ) > 0
        if (set(actual.active) != set(ids) or keys != source_keys
                or BASE not in keys or not rails
                or actual.topology_margin <= 1e-12
                or (args.require_alternate_route_positive and not alt_positive)):
            return None
        if (args.directed_endpoint_signs
                and np.any(directed_endpoint_numerators(p) > 0)):
            return None
        return g, p, den, actual

    z = np.zeros(n)
    base = actual_valid(z)
    if base is None:
        raise RuntimeError("invalid source")
    g = base[0]
    hard = float(np.min(g))
    best_z, best = z.copy(), base
    previous_z, previous = z.copy(), base
    previous_signature = (
        tuple(tuple(base[3].faces[i]["cycle"]) for i, _ in base[3].stable),
        tuple(i for i, _ in base[3].unstable),
        tuple(e for e, _ in base[3].saddles),
    )
    class_event = None
    trust = args.trust
    history = [{"iteration": -1, "hard": hard, "trust": trust}]
    print("start", hard, "variables", n, flush=True)

    for iteration in range(args.iterations):
        jac = np.zeros((len(g), n))
        quad_jac = np.zeros(n)
        new_quad_jac = np.zeros(n)
        round10_quad_jac = np.zeros(n)
        round12_quad_jac = np.zeros(n)
        for j in range(n):
            step = np.zeros(n)
            step[j] = args.epsilon
            pp, pm = fixed_values(z + step), fixed_values(z - step)
            if pp is None or pm is None:
                raise RuntimeError(f"finite difference failed {j}")
            jac[:, j] = (pp[0] - pm[0]) / (2 * args.epsilon)
            if args.protect_quad_wall:
                quad_jac[j] = (
                    quad_far_guard(pp[1]) - quad_far_guard(pm[1])
                ) / (2 * args.epsilon)
            if args.new_quad_side is not None:
                new_quad_jac[j] = (
                    new_quad_guard(pp[1]) - new_quad_guard(pm[1])
                ) / (2 * args.epsilon)
            if args.round10_quad_side is not None:
                round10_quad_jac[j] = (
                    round10_quad_guard(pp[1]) - round10_quad_guard(pm[1])
                ) / (2 * args.epsilon)
            if args.round12_quad_side is not None:
                round12_quad_jac[j] = (
                    round12_quad_guard(pp[1]) - round12_quad_guard(pm[1])
                ) / (2 * args.epsilon)
        step_bounds = [
            (max(-trust, lower[j] - z[j]), min(trust, upper[j] - z[j]))
            for j in range(n)
        ]
        objective_indices = np.arange(len(g))
        if args.lp_guard_cutoff is not None:
            objective_indices = np.flatnonzero(g <= args.lp_guard_cutoff)
        a_ub = [np.c_[-jac[objective_indices],
                      np.ones(len(objective_indices))]]
        b_ub = [g[objective_indices]]
        if protected_indices:
            a_ub.append(np.c_[-jac[protected_indices],
                              np.zeros(len(protected_indices))])
            b_ub.append(g[protected_indices] - protected_floors)
        if args.protect_quad_wall and not args.quad_wall_tangent:
            a_ub.append(np.c_[-quad_jac[None, :], np.zeros((1, 1))])
            b_ub.append(np.asarray([
                quad_far_guard(base[1]) - args.quad_wall_floor
            ]))
        if args.new_quad_side is not None and not args.new_quad_tangent:
            a_ub.append(np.c_[-new_quad_jac[None, :], np.zeros((1, 1))])
            b_ub.append(np.asarray([
                new_quad_guard(base[1]) - args.new_quad_floor
            ]))
        if (args.round10_quad_side is not None
                and not args.round10_quad_tangent):
            a_ub.append(np.c_[-round10_quad_jac[None, :], np.zeros((1, 1))])
            b_ub.append(np.asarray([
                round10_quad_guard(base[1]) - args.round10_quad_floor
            ]))
        if (args.round12_quad_side is not None
                and not args.round12_quad_tangent):
            a_ub.append(np.c_[-round12_quad_jac[None, :],
                              np.zeros((1, 1))])
            b_ub.append(np.asarray([
                round12_quad_guard(base[1]) - args.round12_quad_floor
            ]))
        equality_rows = []
        if args.protect_quad_wall and args.quad_wall_tangent:
            equality_rows.append(quad_jac)
        if args.new_quad_side is not None and args.new_quad_tangent:
            equality_rows.append(new_quad_jac)
        if args.round10_quad_side is not None and args.round10_quad_tangent:
            equality_rows.append(round10_quad_jac)
        if args.round12_quad_side is not None and args.round12_quad_tangent:
            equality_rows.append(round12_quad_jac)
        a_eq = (None if not equality_rows else
                np.c_[np.vstack(equality_rows),
                      np.zeros((len(equality_rows), 1))])
        b_eq = None if not equality_rows else np.zeros(len(equality_rows))
        lp = linprog(
            np.r_[np.zeros(n), -1.0],
            A_ub=np.vstack(a_ub), b_ub=np.concatenate(b_ub),
            A_eq=a_eq, b_eq=b_eq,
            bounds=step_bounds + [(None, None)], method="highs",
        )
        if not lp.success:
            trust *= 0.45
            history.append({"iteration": iteration, "hard": hard,
                            "trust": trust, "accepted": False,
                            "reason": lp.message})
            continue
        direction = lp.x[:-1]
        chosen = None
        trial_summary = []
        quad_target = (quad_far_guard(base[1])
                       if args.protect_quad_wall and args.quad_wall_tangent
                       else None)
        new_quad_target = (new_quad_guard(base[1])
                           if (args.new_quad_side is not None
                               and args.new_quad_tangent) else None)
        round10_quad_target = (round10_quad_guard(base[1])
                               if (args.round10_quad_side is not None
                                   and args.round10_quad_tangent) else None)
        round12_quad_target = (round12_quad_guard(base[1])
                               if (args.round12_quad_side is not None
                                   and args.round12_quad_tangent) else None)
        projection_gradients = []
        projection_targets = []
        projection_functions = []
        if quad_target is not None:
            projection_gradients.append(quad_jac)
            projection_targets.append(quad_target)
            projection_functions.append(quad_far_guard)
        if new_quad_target is not None:
            projection_gradients.append(new_quad_jac)
            projection_targets.append(new_quad_target)
            projection_functions.append(new_quad_guard)
        if round10_quad_target is not None:
            projection_gradients.append(round10_quad_jac)
            projection_targets.append(round10_quad_target)
            projection_functions.append(round10_quad_guard)
        if round12_quad_target is not None:
            projection_gradients.append(round12_quad_jac)
            projection_targets.append(round12_quad_target)
            projection_functions.append(round12_quad_guard)
        for alpha in (1.0, 0.7, 0.5, 0.3, 0.2, 0.1, 0.05,
                      0.02, 0.01, 0.005):
            candidate = z + alpha * direction
            if projection_gradients:
                # The LP step is tangent only to first order.  Project its
                # small nonlinear drift back to the same directed determinant
                # level, otherwise repeated steps silently consume the guard
                # buffer and look like a false obstruction.
                gradient_matrix = np.vstack(projection_gradients)
                gram = gradient_matrix @ gradient_matrix.T
                for _ in range(7):
                    projected, _ = construct(candidate)
                    if projected is None:
                        break
                    error = np.asarray([
                        target - fun(projected)
                        for target, fun in zip(projection_targets,
                                               projection_functions)
                    ])
                    if float(np.max(np.abs(error))) < 1e-16:
                        break
                    correction = gradient_matrix.T @ np.linalg.solve(gram, error)
                    candidate = candidate + correction
            packet = actual_valid(candidate)
            h = float("-inf") if packet is None else float(np.min(packet[0]))
            trial_summary.append([alpha, h])
            if chosen is None or h > chosen[0]:
                chosen = (h, alpha, candidate, packet)
        if chosen[0] <= hard + 2e-11:
            trust *= 0.45
            history.append({"iteration": iteration, "hard": hard,
                            "trust": trust, "accepted": False,
                            "predicted": float(lp.x[-1]),
                            "trials": trial_summary})
            print("reject", iteration, hard, "pred", lp.x[-1],
                  "trust", trust, flush=True)
            if trust < 5e-8:
                break
            continue
        hard, alpha, z, base = chosen
        g = base[0]
        best_z, best = z.copy(), base
        effective = max(alpha * trust, 1e-8)
        trust = min(0.05, max(trust * 0.72, effective * 1.7))
        order = np.argsort(g)[:8]
        history.append({"iteration": iteration, "hard": hard,
                        "trust": trust, "accepted": True,
                        "predicted": float(lp.x[-1]), "alpha": alpha,
                        "worst": g[order].tolist(),
                        "trials": trial_summary})
        print("accept", iteration, hard, "alpha", alpha,
              "trust", trust, "worst", g[order].tolist(), flush=True)
        signature = (
            tuple(tuple(base[3].faces[i]["cycle"]) for i, _ in base[3].stable),
            tuple(i for i, _ in base[3].unstable),
            tuple(e for e, _ in base[3].saddles),
        )
        if signature != previous_signature:
            class_event = {
                "iteration": iteration,
                "pre_parameters": previous_z.tolist(),
                "post_parameters": z.tolist(),
                "pre_actual": summarize(previous[3]),
                "post_actual": summarize(base[3]),
            }
            write_csv(args.output.with_name(args.output.stem + "_event_pre.csv"),
                      ids, previous[1])
            write_csv(args.output.with_name(args.output.stem + "_event_post.csv"),
                      ids, base[1])
            print("CLASS_EVENT", json.dumps(class_event), flush=True)
            if args.stop_on_class_change:
                break
        previous_z, previous = z.copy(), base
        previous_signature = signature
        if hard > 0:
            print("OPEN_TARGET", hard, flush=True)
            break

    g, points, den, actual = best
    _, labels = guards(core.mechanics(ids, points, faces), faces)
    order = np.argsort(g)
    output = {
        "version": 1,
        "method": "27D combined direct-geometry/projective-SPD hard SLP",
        "identity_chart": args.identity_chart,
        "lp_guard_cutoff": args.lp_guard_cutoff,
        "source": str(args.source),
        "direct_parameters": best_z[:n_direct].tolist(),
        "additional_metric_theta": best_z[n_direct:].tolist(),
        "hard_margin": float(np.min(g)),
        "minimum_projective_denominator": float(np.min(den)),
        "worst_guards": [
            {"value": float(g[k]), "feature": labels[k]}
            for k in order[:30]
        ],
        "fresh_actual": summarize(actual),
        "fresh_faces_match_source": {
            frozenset(f["cycle"]) for f in actual.faces
        } == source_keys,
        "rail_edges_present": {
            name: all(tuple(sorted(e)) in set(actual.edges)
                      for e in zip(path, path[1:]))
            for name, path in (("short", SHORT_RAIL), ("long", LONG_RAIL))
        },
        "base_face_present": BASE in {
            frozenset(f["cycle"]) for f in actual.faces
        },
        "protected_wall": {
            "enabled": args.protect_u263_wall,
            "floor": args.wall_floor,
            "u1_enabled": args.protect_u1_wall,
            "u1_floor": args.u1_wall_floor,
            "guards": [
                {"value": float(g[k]), "feature": labels[k]}
                for k in protected_indices
            ],
            "directed_endpoint_signs_enabled": args.directed_endpoint_signs,
            "deduplicated_endpoint_constraints": (
                args.deduplicate_endpoint_constraints
            ),
            "longdouble_decision_numerators": [
                float(x) for x in directed_endpoint_numerators(points)
            ],
            "quad_far_enabled": args.protect_quad_wall,
            "quad_far_tangent": args.quad_wall_tangent,
            "quad_far_floor": args.quad_wall_floor,
            "quad_far_guard": quad_far_guard(points),
            "new_quad_side": args.new_quad_side,
            "new_quad_tangent": args.new_quad_tangent,
            "new_quad_floor": args.new_quad_floor,
            "new_quad_guard": (None if args.new_quad_side is None
                               else new_quad_guard(points)),
            "round10_quad_side": args.round10_quad_side,
            "round10_quad_tangent": args.round10_quad_tangent,
            "round10_quad_floor": args.round10_quad_floor,
            "round10_quad_guard": (None if args.round10_quad_side is None
                                   else round10_quad_guard(points)),
            "round12_quad_side": args.round12_quad_side,
            "round12_quad_tangent": args.round12_quad_tangent,
            "round12_quad_floor": args.round12_quad_floor,
            "round12_quad_guard": (None if args.round12_quad_side is None
                                   else round12_quad_guard(points)),
            "literal_long_rail_required": not args.allow_long_rail_loss,
            "alternate_positive_route_required": (
                args.require_alternate_route_positive
            ),
        },
        "class_event": class_event,
        "history": history,
    }
    write_csv(args.output.with_name(args.output.stem + "_best.csv"), ids, points)
    with args.output.with_name(args.output.stem + "_best_faces.json").open("w") as f:
        json.dump([face["cycle"] for face in actual.faces], f, indent=2)
    args.output.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
