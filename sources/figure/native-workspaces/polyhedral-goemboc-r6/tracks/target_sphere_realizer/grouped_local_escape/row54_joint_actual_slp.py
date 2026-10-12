#!/usr/bin/env python3
"""Sequential linear programming on fresh actual-hull feature guards."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from row54_joint_actual_search import (  # noqa: E402
    JointActual, feature_guards, write_csv, BASE,
)
import materialize_row54_cells as mat  # noqa: E402

ROOT = HERE.parents[2]
CIRCUIT = ROOT / "tracks/circuit_atlas"


GLOBAL_BOUNDS = np.asarray([
    (0.0015, 0.055), (0.58, 0.985), (-0.34, -0.08), (-0.14, 0.14),
    (-0.0025, 0.006),
    (-0.72, 0.72), (-0.72, 0.72), (-0.72, 0.72),
    (-1.58, 1.58), (-1.58, 1.58), (-1.58, 1.58),
    (-1.58, 1.58), (-1.58, 1.58),
], dtype=float)

# Natural local units.  SLP trust radii are dimensionless multiples of these.
SCALES = np.asarray([
    0.003, 0.03, 0.015, 0.01, 5.0e-6,
    0.03, 0.03, 0.03, 0.08, 0.08, 0.08, 0.08, 0.08,
])


def key(label):
    kind, feature = label
    if kind.startswith("S"):
        return kind, tuple(sorted(feature))
    if kind.startswith("H"):
        return kind, tuple(sorted(feature))
    return kind, int(feature)


def packet(search, x, expected_keys=None):
    points, actual, guard_packet, meta = search.audit(x)
    if guard_packet is None:
        return None
    guards, labels = guard_packet
    by_key = {key(lab): float(z) for z, lab in zip(guards, labels)}
    keys = sorted(by_key, key=str) if expected_keys is None else expected_keys
    if set(keys) != set(by_key):
        return None
    return np.asarray([by_key[k] for k in keys]), keys, points, actual, meta


def finite_jacobian(search, x, keys, epsilon):
    base = packet(search, x, keys)
    if base is None:
        raise RuntimeError("base actual packet invalid")
    g = base[0]
    jac = np.zeros((len(g), len(x)))
    for j in range(len(x)):
        step = epsilon * SCALES[j]
        xp, xm = x.copy(), x.copy()
        xp[j] = min(GLOBAL_BOUNDS[j, 1], xp[j] + step)
        xm[j] = max(GLOBAL_BOUNDS[j, 0], xm[j] - step)
        pp, pm = packet(search, xp, keys), packet(search, xm, keys)
        if pp is not None and pm is not None and xp[j] != xm[j]:
            jac[:, j] = (pp[0] - pm[0]) / ((xp[j] - xm[j]) / SCALES[j])
        elif pp is not None and xp[j] != x[j]:
            jac[:, j] = (pp[0] - g) / ((xp[j] - x[j]) / SCALES[j])
        elif pm is not None and x[j] != xm[j]:
            jac[:, j] = (g - pm[0]) / ((x[j] - xm[j]) / SCALES[j])
        else:
            raise RuntimeError(f"no valid finite difference for variable {j}")
    return g, jac, base


def solve_step(g, jac, x, trust):
    # g + J dy >= margin  <=>  -J dy + margin <= g.
    c = np.r_[np.zeros(len(x)), -1.0]
    aub = np.c_[-jac, np.ones(len(g))]
    bounds = []
    for j in range(len(x)):
        lo = max(-trust, (GLOBAL_BOUNDS[j, 0] - x[j]) / SCALES[j])
        hi = min(trust, (GLOBAL_BOUNDS[j, 1] - x[j]) / SCALES[j])
        bounds.append((lo, hi))
    bounds.append((None, None))
    return linprog(c, A_ub=aub, b_ub=g, bounds=bounds, method="highs")


def encode(search, x, history):
    rec = packet(search, x)
    if rec is None:
        raise RuntimeError("final packet invalid")
    guards, keys, points, actual, meta = rec
    order = np.argsort(guards)
    labels = []
    for k in keys:
        kind, feature = k
        labels.append([kind, list(feature) if isinstance(feature, tuple) else feature])
    return points, {
        "version": 1,
        "method": "fresh-actual sequential linear programming",
        "parameters": x.tolist(),
        "hard_margin": float(np.min(guards)),
        "fresh_f_vector": [len(actual.active), len(actual.edges), len(actual.faces)],
        "fresh_class": [len(actual.stable), len(actual.unstable), len(actual.saddles)],
        "stable": [actual.faces[i]["cycle"] for i, _ in actual.stable],
        "unstable": [i for i, _ in actual.unstable],
        "saddles": [list(e) for e, _ in actual.saddles],
        "centroid": actual.centroid.tolist(),
        "topology_margin": actual.topology_margin,
        "meta": meta,
        "base_face_present": BASE in {frozenset(f["cycle"]) for f in actual.faces},
        "worst_guards": [
            {"value": float(guards[j]), "feature": labels[j]}
            for j in order[:30]
        ],
        "history": history,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path,
                    default=HERE / "row54_joint_actual.json")
    ap.add_argument("--iterations", type=int, default=22)
    ap.add_argument("--epsilon", type=float, default=0.006)
    ap.add_argument("--trust", type=float, default=0.35)
    ap.add_argument("--output", type=Path,
                    default=HERE / "row54_joint_actual_slp.json")
    args = ap.parse_args()

    source = json.load(args.source.open())
    audited = {r["name"]: r for r in source["audited_candidates"]}
    x = np.asarray(audited["best_hard"]["parameters"], dtype=float)
    ids, raw = mat.load_csv(CIRCUIT / "target_sphere_rebuilt.csv")
    robust_theta = np.asarray(
        json.load((CIRCUIT / "robust_rebuilt_fast.json").open())["theta"]
    )
    search = JointActual(ids, raw, robust_theta)
    first = packet(search, x)
    if first is None:
        raise RuntimeError("source candidate is invalid")
    keys = first[1]
    hard = float(np.min(first[0]))
    best_x, best_hard = x.copy(), hard
    trust = args.trust
    history = [{"iteration": -1, "hard": hard, "trust": trust,
                "class": [len(first[3].stable), len(first[3].unstable),
                          len(first[3].saddles)]}]
    print("start", hard, flush=True)

    for iteration in range(args.iterations):
        g, jac, base = finite_jacobian(search, x, keys, args.epsilon)
        lp = solve_step(g, jac, x, trust)
        if not lp.success:
            history.append({"iteration": iteration, "hard": hard,
                            "trust": trust, "lp": lp.message})
            trust *= 0.5
            continue
        dy = lp.x[:-1]
        predicted = float(lp.x[-1])
        accepted = None
        trials = []
        for alpha in (1.0, 0.5, 0.25, 0.1):
            proposal = np.clip(x + alpha * SCALES * dy,
                               GLOBAL_BOUNDS[:, 0], GLOBAL_BOUNDS[:, 1])
            p = packet(search, proposal, keys)
            actual_hard = float("-inf") if p is None else float(np.min(p[0]))
            trials.append({"alpha": alpha, "hard": actual_hard})
            if actual_hard > hard + 2e-10:
                accepted = (proposal, p, actual_hard, alpha)
                break
        if accepted is None:
            trust *= 0.45
            history.append({
                "iteration": iteration, "hard": hard, "trust": trust,
                "predicted": predicted, "accepted": False, "trials": trials,
            })
            print("reject", iteration, hard, "pred", predicted,
                  "trust", trust, flush=True)
            if trust < 2e-5:
                break
            continue

        x, current, hard, alpha = accepted
        if hard > best_hard:
            best_x, best_hard = x.copy(), hard
        trust = min(1.0, trust * (1.3 if alpha == 1.0 else 0.8))
        cls = [len(current[3].stable), len(current[3].unstable),
               len(current[3].saddles)]
        history.append({
            "iteration": iteration, "hard": hard, "trust": trust,
            "predicted": predicted, "accepted": True, "alpha": alpha,
            "class": cls, "trials": trials,
        })
        print("accept", iteration, hard, "pred", predicted,
              "alpha", alpha, "trust", trust, "class", cls, flush=True)
        if hard > 0.0:
            print("OPEN_TARGET", hard, flush=True)
            break

    points, output = encode(search, best_x, history)
    output["fresh_actual_calls"] = search.calls
    write_csv(args.output.with_name(args.output.stem + "_best.csv"), ids, points)
    final = packet(search, best_x)
    with args.output.with_name(args.output.stem + "_best_faces.json").open("w") as f:
        json.dump([face["cycle"] for face in final[3].faces], f, indent=2)
    args.output.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
