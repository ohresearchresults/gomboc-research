#!/usr/bin/env python3
"""Alternating support-interiorization / mechanical SLP for the 164D chart."""
from __future__ import annotations

from pathlib import Path
import argparse
import json
import math
import time

import numpy as np
from scipy.optimize import linprog

import combined_core as core


HERE = Path(__file__).resolve().parent


def eval_all(x, problem):
    chart, faces, incidence, pv, pf = problem
    vals, guards, geom, labels = core.evaluate_chart(x, chart, faces, incidence, pv, pf)
    return vals, guards, geom, labels


def stats(x, problem):
    vals, guards, geom, labels = eval_all(x, problem)
    stable, unstable, saddles = core.class_counts(geom, problem[1], problem[2])
    return {
        "positive": int(np.sum(vals > 0)),
        "mechanical_positive": int(np.sum(vals[:-1] > 0)),
        "hard": float(np.min(vals)),
        "mechanical_hard": float(np.min(vals[:-1])),
        "guard_min": float(np.min(guards)),
        "guard_q001": float(np.quantile(guards, 0.001)),
        "class": [len(stable), len(unstable), len(saddles)],
        "stable_faces": stable,
        "unstable_vertices": unstable,
        "saddle_edges": [list(e) for e in saddles],
        "centroid": geom["centroid"].tolist(),
        "volume_normalized": geom["volume"],
        "worst": [
            {"label": labels[int(i)], "value": float(vals[int(i)])}
            for i in np.argsort(vals)[:20]
        ],
    }


def finite_jacobian(x, f0, problem, eps):
    """Forward Jacobian of 163 target rows and every topology guard."""
    n = len(x)
    jt = np.empty((163, n))
    jg = np.empty((len(f0[1]), n))
    for j in range(n):
        h = eps * max(1.0, abs(float(x[j])))
        y = x.copy()
        y[j] += h
        try:
            vals, guards, *_ = eval_all(y, problem)
        except Exception:
            y[j] = x[j] - h
            vals, guards, *_ = eval_all(y, problem)
            h = -h
        jt[:, j] = (vals[:163] - f0[0][:163]) / h
        jg[:, j] = (guards - f0[1]) / h
    return jt, jg


def mechanical_lp(vals, guards, jt, jg, trust, guard_floor):
    n = jt.shape[1]
    # Variables are dx[0:n] and common mechanical margin t.
    c = np.zeros(n + 1)
    c[-1] = -1.0
    A = []
    b = []
    # vals + J dx >= t
    A.append(np.column_stack((-jt, np.ones(len(vals)))))
    b.append(vals.copy())
    # guards + J dx >= guard_floor
    A.append(np.column_stack((-jg, np.zeros(len(guards)))))
    b.append(guards - guard_floor)
    A = np.vstack(A)
    b = np.concatenate(b)
    bounds = [(-trust, trust)] * n + [(-5.0, 2.0)]
    return linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")


def interior_lp(vals, guards, jt, jg, trust, floor, drop, active_count):
    n = jt.shape[1]
    order = np.argsort(guards)
    active = order[: min(active_count, len(order))]
    inactive = order[min(active_count, len(order)):]
    # Variables dx and common active support margin s.
    c = np.zeros(n + 1)
    c[-1] = -1.0
    A = []
    b = []
    # Do not reduce any selected mechanical row by more than drop.
    A.append(np.column_stack((-jt, np.zeros(len(vals)))))
    b.append(np.full(len(vals), drop))
    # Tight guards >= s.
    A.append(np.column_stack((-jg[active], np.ones(len(active)))))
    b.append(guards[active])
    # All other guards remain above a strict floor.
    if len(inactive):
        A.append(np.column_stack((-jg[inactive], np.zeros(len(inactive)))))
        b.append(guards[inactive] - floor)
    A = np.vstack(A)
    b = np.concatenate(b)
    bounds = [(-trust, trust)] * n + [(0.0, 0.05)]
    return linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")


def rank_key(vals, guards):
    # Mechanical hard margin is primary; then number strict and hinge energy.
    mech = vals[:163]
    return (
        float(np.min(mech)),
        int(np.sum(mech > 0)),
        -float(np.sum(np.minimum(mech, 0.0) ** 2)),
        float(np.min(guards)),
    )


def nonlinear_line_search(x, dx, problem, old_key, floor, mode):
    trials = (1.0, 0.75, 0.5, 0.35, 0.25, 0.125, 0.0625, 0.03125)
    best = None
    for alpha in trials:
        y = x + alpha * dx
        try:
            vals, guards, geom, labels = eval_all(y, problem)
        except Exception:
            continue
        if np.min(guards) <= floor:
            continue
        key = rank_key(vals, guards)
        if mode == "mechanical":
            accept = key > old_key
        else:
            # Interiorization may spend a very small mechanical amount but must
            # materially thicken the support chamber.
            accept = (
                np.min(guards) > old_key[3] * 1.05
                and key[0] >= old_key[0] - 2.5e-3
            )
        if accept and (best is None or (key if mode == "mechanical" else (key[3], key[0])) > best[0]):
            best = ((key if mode == "mechanical" else (key[3], key[0])), y, vals, guards, geom, labels, alpha)
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--iterations", type=int, default=20)
    ap.add_argument("--trust", type=float, default=2e-3)
    ap.add_argument("--fd-eps", type=float, default=2e-6)
    ap.add_argument("--interior-every", type=int, default=3)
    ap.add_argument("--active-guards", type=int, default=160)
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--output", default="combined_slp_best.npy")
    args = ap.parse_args()

    chart, faces, incidence, pv, pf, x0 = core.load_problem()
    problem = (chart, faces, incidence, pv, pf)
    out = HERE / args.output
    x = np.load(out) if args.resume and out.exists() else x0.copy()
    log_path = out.with_suffix(".jsonl")
    trust = args.trust
    s0 = stats(x, problem)
    print("START", json.dumps({k: s0[k] for k in ("positive", "hard", "mechanical_hard", "guard_min", "class")}))

    for it in range(args.iterations):
        started = time.time()
        vals, guards, geom, labels = eval_all(x, problem)
        old_key = rank_key(vals, guards)
        f0 = (vals, guards)
        jt, jg = finite_jacobian(x, f0, problem, args.fd_eps)
        mode = "interior" if args.interior_every > 0 and it % args.interior_every == args.interior_every - 1 else "mechanical"
        floor = max(1e-10, min(1e-6, float(np.min(guards)) * 0.10))
        if mode == "mechanical":
            lp = mechanical_lp(vals[:163], guards, jt, jg, trust, floor)
        else:
            lp = interior_lp(vals[:163], guards, jt, jg, trust, floor, 2e-3, args.active_guards)
        accepted = False
        alpha = 0.0
        lp_margin = None
        if lp.success:
            dx = lp.x[:-1]
            lp_margin = float(lp.x[-1])
            found = nonlinear_line_search(x, dx, problem, old_key, floor, mode)
            if found is not None:
                _, x, vals, guards, geom, labels, alpha = found
                accepted = True
                np.save(out, x)
                trust = min(trust * 1.20, 0.04)
            else:
                trust = max(trust * 0.45, 1e-6)
        else:
            trust = max(trust * 0.35, 1e-6)

        rec = {
            "iteration": it,
            "mode": mode,
            "accepted": accepted,
            "alpha": alpha,
            "trust_next": trust,
            "lp_success": bool(lp.success),
            "lp_status": int(lp.status),
            "lp_message": lp.message,
            "lp_margin": lp_margin,
            "elapsed": time.time() - started,
            "positive": int(np.sum(vals > 0)),
            "mechanical_positive": int(np.sum(vals[:163] > 0)),
            "hard": float(np.min(vals)),
            "mechanical_hard": float(np.min(vals[:163])),
            "guard_min": float(np.min(guards)),
            "guard_q001": float(np.quantile(guards, 0.001)),
            "worst": [
                {"label": labels[int(i)], "value": float(vals[int(i)])}
                for i in np.argsort(vals)[:15]
            ],
        }
        with log_path.open("a") as f:
            f.write(json.dumps(rec) + "\n")
        print("ITER", json.dumps({k: rec[k] for k in ("iteration", "mode", "accepted", "alpha", "trust_next", "lp_margin", "mechanical_positive", "mechanical_hard", "guard_min", "elapsed")}))
        if rec["mechanical_hard"] > 1e-6 and rec["guard_min"] > 1e-7:
            print("STRICT TARGET LEDGER REACHED")
            break

    final = stats(x, problem)
    final["hull_rebuild"] = core.rebuild_hull(chart.unpack(x), faces)
    final["chart_file"] = out.name
    final["log_file"] = log_path.name
    report = out.with_suffix(".json")
    report.write_text(json.dumps(final, indent=2))
    print("FINAL", json.dumps({k: final[k] for k in ("positive", "mechanical_positive", "mechanical_hard", "guard_min", "class")}))


if __name__ == "__main__":
    main()
