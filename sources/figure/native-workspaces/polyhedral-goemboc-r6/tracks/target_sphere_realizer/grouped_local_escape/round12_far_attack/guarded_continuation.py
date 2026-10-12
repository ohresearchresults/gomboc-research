#!/usr/bin/env python3
"""Guard-level continuation in the strict round-12 far cell.

Unlike the older endpoint-only SLP, every accepted segment is sampled after a
Newton projection onto all six accumulated directed guard levels.  A segment
is rejected if any sample changes the actual hull, mechanics signature, base,
protected route, active-row set, or strict guard signs.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
from scipy.linalg import expm
from scipy.optimize import linprog

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
ROOT = PARENT.parents[2]
sys.path[:0] = [str(PARENT), str(ROOT / "tracks/circuit_atlas")]

from actual_grouped import evaluate, summarize  # noqa: E402
from row54_direct_actual_search import DirectActual, read_points  # noqa: E402
from row54_full_minimax import BASE, SHORT_RAIL, guards  # noqa: E402
from row54_joint_actual_search import write_csv  # noqa: E402
import row54_four_residual_search as core  # noqa: E402


SOURCE = PARENT / "row54_round12_far_multiguard_buffer_buffer.csv"
OUTPUT = HERE / "guarded_continuation.json"
ALT_ROUTE = (228, 198, 263, 9, 8)
TOPOLOGY_QUADS = (
    ("round4_far", (7, 8, 245, 246), -1.0),
    ("round8_pre", (9, 198, 263, 264), -1.0),
    ("round10_far", (8, 264, 246, 198), 1.0),
    ("round12_far", (198, 263, 262, 11), 1.0),
)
PROTECTED_KEYS = (
    ("U-", 263), ("H-", (10, 263)),
    ("U-", 1), ("H-", (1, 54)),
)


def label_key(label):
    kind, item = label
    return kind, tuple(sorted(item)) if isinstance(item, list) else item


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, default=SOURCE)
    ap.add_argument("--output", type=Path, default=OUTPUT)
    ap.add_argument("--iterations", type=int, default=400)
    ap.add_argument("--trust", type=float, default=8e-4)
    ap.add_argument("--epsilon", type=float, default=2e-6)
    ap.add_argument("--segment-samples", type=int, default=8)
    ap.add_argument("--protect-u6-birth", action="store_true",
                    help="hold the U6/H(5,6) no-birth numerator positive")
    ap.add_argument("--protect-s67245-birth", action="store_true",
                    help="hold the S[6,7,245]/H(7,245) no-birth guard positive")
    args = ap.parse_args()

    ids, source = read_points(args.source)
    ix = {i: k for k, i in enumerate(ids)}
    direct = DirectActual(ids, source)
    nd = len(direct.controls)
    nvar = nd + 8
    origin = source.mean(axis=0)
    scale0 = float(np.sqrt(np.mean(np.sum((source - origin) ** 2, axis=1))))
    _, source_faces, _ = core.group_maximal_faces(ids, source)
    source_keys = {frozenset(f) for f in source_faces}
    lower = np.r_[np.full(nd, -1.0), np.full(3, -0.75), np.full(5, -1.6)]
    upper = -lower

    def construct(z):
        q = direct.construct(z[:nd])
        qn = (q - origin) / scale0
        theta = z[nd:]
        den = 1.0 + qn @ theta[:3]
        if np.min(den) <= 0.08:
            return None, den
        a, b, c, d, e = theta[3:]
        h = np.array([[a, b, c], [b, d, e], [c, e, -a - d]])
        points = origin + scale0 * ((qn / den[:, None]) @ expm(h).T)
        return points, den

    def centroid_longdouble(points):
        p = np.asarray(points, dtype=np.longdouble)
        shift = np.mean(p, axis=0)
        d6 = np.longdouble(0)
        m24 = np.zeros(3, dtype=np.longdouble)
        for cycle in source_faces:
            c = [ix[i] for i in cycle]
            a = p[c[0]] - shift
            for j in range(1, len(c) - 1):
                b = p[c[j]] - shift
                q = p[c[j + 1]] - shift
                det = np.dot(a, np.cross(b, q))
                d6 += det
                m24 += det * (a + b + q)
        return shift + m24 / (4 * d6)

    def directed(points):
        p = np.asarray(points, dtype=np.longdouble)
        centered = p - np.mean(p, axis=0)
        scale = np.sqrt(np.mean(np.sum(centered * centered, axis=1)))
        values = []
        for _, quad, sign in TOPOLOGY_QUADS:
            q = [p[ix[i]] for i in quad]
            det = np.dot(q[1] - q[0], np.cross(q[2] - q[0], q[3] - q[0]))
            values.append(np.longdouble(sign) * det / scale**3)
        centroid = centroid_longdouble(p)
        x10, x263 = p[ix[10]] - centroid, p[ix[263]] - centroid
        x1, x54 = p[ix[1]] - centroid, p[ix[54]] - centroid
        values.extend((-np.dot(x263, x263 - x10), np.dot(x1, x54 - x1)))
        if args.protect_u6_birth:
            x5, x6 = p[ix[5]] - centroid, p[ix[6]] - centroid
            values.append(np.dot(x6, x5 - x6))
        return np.asarray(values, dtype=np.longdouble)

    def fixed(z):
        points, den = construct(z)
        if points is None:
            return None
        try:
            values, labels = guards(core.mechanics(ids, points, source_faces), source_faces)
        except Exception:
            return None
        dvals = list(np.asarray(directed(points), float))
        if args.protect_s67245_birth:
            local_lookup = {label_key(label): k for k, label in enumerate(labels)}
            dvals.append(float(values[local_lookup[("S-", (6, 7, 245))]]))
        return values, labels, points, den, np.asarray(dvals, float)

    zero = np.zeros(nvar)
    initial = fixed(zero)
    if initial is None:
        raise RuntimeError("invalid source")
    guard_target = initial[4].copy()
    lookup = {label_key(label): k for k, label in enumerate(initial[1])}
    protected_indices = np.asarray([lookup[k] for k in PROTECTED_KEYS])
    protected_floor = np.asarray([3e-9, 3e-9, 3e-9, 3e-9])

    def graph_record(points, actual):
        edges = set(actual.edges)
        x = {i: points[ix[i]] - actual.centroid for i in ids}
        pairs = list(zip(ALT_ROUTE, ALT_ROUTE[1:]))
        return {
            "all_edges_present": all(tuple(sorted(e)) in edges for e in pairs),
            "positive_dot_min": min(float(np.dot(x[a], x[b])) for a, b in pairs),
        }

    source_signature = None

    def audit(z):
        nonlocal source_signature
        packet = fixed(z)
        if packet is None:
            return {"valid": False, "reason": "fixed_evaluation"}
        values, labels, points, den, dvals = packet
        actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
        if not actual.valid:
            return {"valid": False, "reason": actual.error}
        keys = {frozenset(f["cycle"]) for f in actual.faces}
        edges = set(actual.edges)
        graph = graph_record(points, actual)
        signature = (
            tuple(tuple(actual.faces[i]["cycle"]) for i, _ in actual.stable),
            tuple(i for i, _ in actual.unstable),
            tuple(e for e, _ in actual.saddles),
        )
        if source_signature is None:
            source_signature = signature
        failures = []
        if set(actual.active) != set(ids): failures.append("active_rows")
        if keys != source_keys: failures.append("face_cell")
        if signature != source_signature: failures.append("mechanics_signature")
        if BASE not in keys: failures.append("base")
        if not all(tuple(sorted(e)) in edges for e in zip(SHORT_RAIL, SHORT_RAIL[1:])):
            failures.append("short_rail")
        if not graph["all_edges_present"] or graph["positive_dot_min"] <= 0:
            failures.append("alternate_route")
        if actual.topology_margin <= 1e-12: failures.append("topology_margin")
        if np.any(values[protected_indices] <= protected_floor):
            failures.append("protected_mechanics")
        if np.any(dvals <= 0): failures.append("directed_guards")
        return {
            "valid": not failures,
            "failures": failures,
            "parameters": np.asarray(z).tolist(),
            "hard": float(np.min(values)),
            "fresh_actual": summarize(actual),
            "minimum_denominator": float(np.min(den)),
            "directed_guards": dvals.tolist(),
            "guard_target_error": (dvals - guard_target).tolist(),
            "protected_mechanics": values[protected_indices].tolist(),
            "route": graph,
        }

    def derivatives(z):
        packet = fixed(z)
        if packet is None:
            raise RuntimeError("derivative base invalid")
        values = packet[0]
        jac = np.empty((len(values), nvar))
        djac = np.empty((len(guard_target), nvar))
        for j in range(nvar):
            step = np.zeros(nvar)
            step[j] = args.epsilon
            plus, minus = fixed(z + step), fixed(z - step)
            if plus is None or minus is None:
                raise RuntimeError(f"finite difference failed at {j}")
            jac[:, j] = (plus[0] - minus[0]) / (2 * args.epsilon)
            djac[:, j] = (plus[4] - minus[4]) / (2 * args.epsilon)
        return values, jac, djac

    def project(z, djac):
        candidate = np.asarray(z, float).copy()
        gram = djac @ djac.T
        for _ in range(12):
            points, _ = construct(candidate)
            if points is None:
                return None
            projected_guards = list(np.asarray(directed(points), float))
            if args.protect_s67245_birth:
                values, labels = guards(core.mechanics(ids, points, source_faces),
                                        source_faces)
                local_lookup = {label_key(label): k
                                for k, label in enumerate(labels)}
                projected_guards.append(float(
                    values[local_lookup[("S-", (6, 7, 245))]]
                ))
            error = guard_target - np.asarray(projected_guards, float)
            if np.max(np.abs(error)) < 2e-16:
                break
            candidate += djac.T @ np.linalg.solve(gram, error)
        return candidate

    z = zero.copy()
    current = audit(z)
    if not current["valid"]:
        raise RuntimeError(f"source audit failed: {current}")
    hard = current["hard"]
    trust = args.trust
    trace = [current]
    history = [{"iteration": -1, "hard": hard, "trust": trust}]
    best_rejected = None

    for iteration in range(args.iterations):
        values, jac, djac = derivatives(z)
        objective = np.flatnonzero(values <= 0.03)
        step_bounds = [
            (max(-trust, lower[j] - z[j]), min(trust, upper[j] - z[j]))
            for j in range(nvar)
        ]
        a_ub = [np.c_[-jac[objective], np.ones(len(objective))],
                np.c_[-jac[protected_indices], np.zeros(len(protected_indices))]]
        b_ub = [values[objective], values[protected_indices] - protected_floor]
        lp = linprog(
            np.r_[np.zeros(nvar), -1.0],
            A_ub=np.vstack(a_ub), b_ub=np.concatenate(b_ub),
            A_eq=np.c_[djac, np.zeros((len(guard_target), 1))],
            b_eq=np.zeros(len(guard_target)),
            bounds=step_bounds + [(None, None)], method="highs",
        )
        if not lp.success:
            trust *= 0.45
            history.append({"iteration": iteration, "hard": hard, "trust": trust,
                            "accepted": False, "reason": lp.message})
            if trust < 5e-8: break
            continue

        direction = lp.x[:-1]
        chosen = None
        trials = []
        for alpha in (1.0, 0.7, 0.5, 0.3, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005):
            endpoint = project(z + alpha * direction, djac)
            if endpoint is None:
                trials.append([alpha, None, ["projection"]])
                continue
            samples = []
            valid = True
            for fraction in np.linspace(0.0, 1.0, args.segment_samples + 1)[1:]:
                sample_z = project((1.0 - fraction) * z + fraction * endpoint, djac)
                rec = ({"valid": False, "failures": ["projection"]}
                       if sample_z is None else audit(sample_z))
                samples.append(rec)
                if not rec["valid"]:
                    valid = False
                    break
            endpoint_hard = samples[-1].get("hard", float("-inf")) if samples else float("-inf")
            trials.append([alpha, endpoint_hard, samples[-1].get("failures", [])])
            if not valid:
                rejected = {"iteration": iteration, "alpha": alpha,
                            "direction": direction.tolist(), "samples": samples}
                if best_rejected is None or alpha < best_rejected["alpha"]:
                    best_rejected = rejected
                continue
            if chosen is None or endpoint_hard > chosen[0]:
                chosen = (endpoint_hard, alpha, endpoint, samples)
            # Alphas are tried from largest to smallest.  Once the largest
            # path-safe trial is genuinely improving, smaller trials only
            # repeat the same certified segment at much higher cost.
            if endpoint_hard > hard + 2e-11:
                break

        if chosen is None or chosen[0] <= hard + 2e-11:
            trust *= 0.45
            history.append({"iteration": iteration, "hard": hard, "trust": trust,
                            "accepted": False, "predicted": float(lp.x[-1]),
                            "trials": trials})
            print("reject", iteration, hard, "trust", trust, flush=True)
            if trust < 5e-8: break
            continue

        hard, alpha, z, samples = chosen
        trace.extend(samples)
        effective = max(alpha * trust, 1e-8)
        trust = min(0.02, max(trust * 0.72, effective * 1.7))
        history.append({"iteration": iteration, "hard": hard, "trust": trust,
                        "accepted": True, "alpha": alpha,
                        "predicted": float(lp.x[-1]), "trials": trials})
        print("accept", iteration, hard, "alpha", alpha, "trust", trust,
              "topology", samples[-1]["fresh_actual"]["topology_margin"], flush=True)
        if hard > 0:
            break

    final = audit(z)
    points, _ = construct(z)
    write_csv(args.output.with_name(args.output.stem + "_best.csv"), ids, points)
    actual = evaluate(dict(zip(ids, points)), coplanar_rel=1e-11)
    args.output.with_name(args.output.stem + "_best_faces.json").write_text(
        json.dumps([f["cycle"] for f in actual.faces], indent=2) + "\n"
    )
    out = {
        "version": 1,
        "method": "six-guard projected actual-cell SLP with sampled accepted segments",
        "source": str(args.source),
        "guard_names": ([q[0] for q in TOPOLOGY_QUADS] +
                        ["U263_H10_263", "U1_H1_54"] +
                        (["U6_H5_6"] if args.protect_u6_birth else []) +
                        (["S67245_H7_245"] if args.protect_s67245_birth else [])),
        "guard_target": guard_target.tolist(),
        "protected_keys": [[k, list(v) if isinstance(v, tuple) else v]
                           for k, v in PROTECTED_KEYS],
        "segment_samples": args.segment_samples,
        "final_parameters": z.tolist(),
        "final": final,
        "trace": trace,
        "history": history,
        "best_rejected": best_rejected,
    }
    args.output.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({
        "final_hard": final["hard"],
        "final_class": final["fresh_actual"]["class"],
        "final_topology_margin": final["fresh_actual"]["topology_margin"],
        "trace_samples": len(trace),
        "iterations": len(history) - 1,
        "best_rejected_failures": None if best_rejected is None else
                                  best_rejected["samples"][-1].get("failures"),
    }, indent=2))


if __name__ == "__main__":
    main()
