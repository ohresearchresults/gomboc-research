#!/usr/bin/env python3
"""Drive H(9,10) to its literal mechanics wall with five no-givebacks.

The start is the independently audited endpoint of
``row54_adjacent_dynamic_continuation``.  At each step a mechanics-only
full-44 finite Jacobian is recomputed.  An LP maximizes the requested signed
H(9,10) derivative while requiring positive normalized derivatives for the
other five residuals, nonnegative derivatives for every nearby ordinary
mechanics guard, and inward derivatives for every nearby support circuit.
Every finite step is nevertheless checked against the complete topology and
a fresh hull/own-centroid audit.

The event has the exact common numerator

    N10L = (p10-c) dot (p10-p9),

where c is the polyhedron's own volume centroid.  It is simultaneously the
numerator of the active ``1-t`` component of H(9,10) and of row 10's radial
component toward row 9.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np
from scipy.optimize import brentq, linprog

import row54_adjacent_dynamic_continuation as dynamic_mod
import row54_four_residual_search as core
import row54_post_row15_clean_flip as flip_mod
import row54_shared_root_atlas as atlas_mod


HERE = Path(__file__).resolve().parent
START_JSON = HERE / "row54_adjacent_dynamic_continuation.json"
FD_STEP = 3e-6
CONTROL_RADIUS = 0.5
OTHER_PACKET_FRACTION = 0.5
MECHANICS_NEAR = 5e-4
SUPPORT_NEAR = 1e-7
H910_KEY = ("H-", (9, 10))


def write_csv(path, ids, points):
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(("source_id", "x", "y", "z"))
        for i, p in zip(ids, points):
            w.writerow([i, *[format(float(v), ".17g") for v in p]])


def packet_indices(problem):
    by_key = {
        dynamic_mod.feature_key(label): k
        for k, label in enumerate(problem.mech_labels)
    }
    return np.asarray([by_key[key] for key in dynamic_mod.PACKET_KEYS], dtype=int)


def finite_mechanics(problem, x, step=FD_STEP):
    _, _, g0, _, _ = problem.evaluate(x, include_topology=False)
    jac = np.zeros((len(g0), len(x)))
    for k in range(len(x)):
        h = step
        got = {}
        for _ in range(7):
            for sign in (1.0, -1.0):
                trial = x.copy()
                trial[k] += sign * h
                try:
                    _, _, guards, _, _ = problem.evaluate(
                        trial, include_topology=False
                    )
                    got[sign] = guards
                except (ValueError, FloatingPointError):
                    pass
            if got:
                break
            h *= 0.2
        if 1.0 in got and -1.0 in got:
            jac[:, k] = (got[1.0] - got[-1.0]) / (2.0 * h)
        elif 1.0 in got:
            jac[:, k] = (got[1.0] - g0) / h
        elif -1.0 in got:
            jac[:, k] = (g0 - got[-1.0]) / h
        else:
            raise RuntimeError(("mechanics finite difference failed", k))
    return jac


def determinant_from_points(ids, points, circuit):
    ix = {i: k for k, i in enumerate(ids)}
    a, b, c, d = (points[ix[k]] for k in circuit)
    return float(np.dot(np.cross(b - a, c - a), d - a))


def support_circuits(problem, x, topology):
    points, den = problem.chart.coordinates(x)
    if points is None:
        raise ValueError(float(np.min(den)))
    records = {}
    for k, (value, label) in enumerate(zip(topology, problem.top_labels)):
        if label[0] != "support":
            continue
        circuit = tuple(sorted(set(label[2]) | {label[3]}))
        if value >= SUPPORT_NEAR and circuit not in dynamic_mod.PROMOTED_CIRCUITS:
            continue
        if circuit in records:
            continue
        determinant = determinant_from_points(problem.ids, points, circuit)
        if abs(determinant) <= 1e-25:
            continue
        records[circuit] = {
            "representative_guard_index": k,
            "representative_label": label,
            "guard": float(value),
            "determinant": determinant,
            "admissible_sign": float(np.sign(value / determinant)),
        }
    # Row-15 must stay on D>0 even after it moves away from the numerical
    # support-near threshold.
    circuit = flip_mod.ROW15_CIRCUIT
    determinant = determinant_from_points(problem.ids, points, circuit)
    records.setdefault(circuit, {
        "representative_guard_index": None,
        "representative_label": "explicit row15 determinant",
        "guard": determinant,
        "determinant": determinant,
        "admissible_sign": 1.0,
    })
    return records


def circuit_gradients(problem, x, circuits, step=1e-6):
    gradients = {circuit: np.zeros(len(x)) for circuit in circuits}
    for k in range(len(x)):
        xp = x.copy(); xp[k] += step
        xm = x.copy(); xm[k] -= step
        pp, _ = problem.chart.coordinates(xp)
        pm, _ = problem.chart.coordinates(xm)
        if pp is None or pm is None:
            raise ValueError(("projective finite difference", k))
        for circuit in circuits:
            gradients[circuit][k] = (
                determinant_from_points(problem.ids, pp, circuit)
                - determinant_from_points(problem.ids, pm, circuit)
            ) / (2.0 * step)
    return gradients


def event_numerators(ids, points, faces):
    mechanics = core.mechanics(ids, points, faces)
    ix = {i: k for k, i in enumerate(ids)}
    c = mechanics["centroid"]
    x10 = points[ix[10]] - c
    left = points[ix[10]] - points[ix[9]]
    right = points[ix[11]] - points[ix[10]]
    return {
        "N10L": float(np.dot(x10, left)),
        "N10R": float(np.dot(x10, right)),
        "left_edge_squared": float(np.dot(left, left)),
        "right_edge_squared": float(np.dot(right, right)),
        "x10_norm": float(np.linalg.norm(x10)),
        "left_edge_norm": float(np.linalg.norm(left)),
        "mechanics": mechanics,
    }


def target_direction(atlas, x, guards, topology, packet):
    jm = finite_mechanics(atlas.problem, x)
    packet_scales = np.maximum(np.abs(guards[packet]), 2.5e-4)
    jp = jm[packet] / packet_scales[:, None]
    hpos = list(dynamic_mod.PACKET_KEYS).index(H910_KEY)

    rows, labels = [], []
    packet_set = set(packet.tolist())
    for k, value in enumerate(guards):
        if k in packet_set or value >= MECHANICS_NEAR:
            continue
        scale = max(abs(value), 1e-4)
        rows.append(jm[k] / scale)
        labels.append(("mechanics", k, atlas.problem.mech_labels[k]))

    circuit_records = support_circuits(atlas.problem, x, topology)
    circuit_jac = circuit_gradients(atlas.problem, x, circuit_records)
    for circuit, record in circuit_records.items():
        row = record["admissible_sign"] * circuit_jac[circuit]
        scale = max(abs(record["determinant"]), 1e-10)
        rows.append(row / scale)
        labels.append(("support_circuit", circuit))

    rows = np.asarray(rows)
    other = np.delete(jp, hpos, axis=0)
    # First find the largest common no-giveback rate compatible with all
    # nearby mechanics/support walls.  Retaining half of it leaves transverse
    # nullspace freedom for the H910 objective without guessing a rate that
    # can become infeasible after an active-component change.
    aub_rate = np.vstack((
        np.c_[-other, np.ones(len(other))],
        np.c_[-rows, np.zeros(len(rows))],
    ))
    c_rate = np.zeros(len(x) + 1)
    c_rate[-1] = -1.0
    rate_lp = linprog(
        c_rate, A_ub=aub_rate, b_ub=np.zeros(len(aub_rate)),
        bounds=[(-CONTROL_RADIUS, CONTROL_RADIUS)] * len(x) + [(None, None)],
        method="highs",
    )
    if not rate_lp.success:
        raise RuntimeError(rate_lp.message)
    maximum_other_rate = float(rate_lp.x[-1])
    retained_other_rate = OTHER_PACKET_FRACTION * maximum_other_rate

    objective = -jp[hpos]
    aub = np.vstack((-other, -rows))
    bub = np.r_[
        -retained_other_rate * np.ones(len(other)),
        np.zeros(len(rows)),
    ]
    lp = linprog(
        objective, A_ub=aub, b_ub=bub,
        bounds=[(-CONTROL_RADIUS, CONTROL_RADIUS)] * len(x),
        method="highs",
    )
    if not lp.success:
        raise RuntimeError(lp.message)
    direction = lp.x
    rates = rows @ direction
    return direction, {
        "success": bool(lp.success),
        "message": str(lp.message),
        "maximum_other_packet_common_rate": maximum_other_rate,
        "retained_other_packet_fraction": OTHER_PACKET_FRACTION,
        "retained_other_packet_rate": retained_other_rate,
        "packet_normalized_rates": (jp @ direction).tolist(),
        "H910_normalized_rate": float(jp[hpos] @ direction),
        "minimum_near_guard_rate": float(np.min(rates)),
        "maximum_absolute_control_rate": float(np.max(np.abs(direction))),
        "support_circuits": [
            {"circuit": list(circuit), **record}
            for circuit, record in circuit_records.items()
        ],
        "weakest_constraints": [
            {"normalized_rate": float(rates[k]), "constraint": labels[int(k)]}
            for k in np.argsort(rates)[:20]
        ],
        "direction": direction.tolist(),
    }


def strict_common_invariants(atlas, state, expected_class, expected_saddles):
    base = dynamic_mod.required_invariants(state)
    # Replace the class/saddle assertions with the requested side of H910.
    base["class_2_3_3"] = state.fresh.get("class") == expected_class
    base["saddle_edges_exact"] = {
        tuple(sorted(edge)) for edge in state.fresh.get("saddle_edges", [])
    } == set(expected_saddles)
    return base


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--iterations", type=int, default=90)
    ap.add_argument("--trust", type=float, default=0.001)
    ap.add_argument("--minimum-step", type=float, default=2e-7)
    ap.add_argument("--resume", help="continue from a prior H910 JSON")
    ap.add_argument("--output", default="row54_h910_event_continuation.json")
    args = ap.parse_args()

    reference = atlas_mod.Atlas(atlas_mod.DEFAULT_SOURCE, atlas_mod.DEFAULT_FACES,
                                atlas_mod.DEFAULT_START, 8e-6)
    start = json.load(START_JSON.open())
    previous = None
    trajectory = []
    if args.resume:
        previous = json.load((HERE / args.resume).open())
        x = np.asarray(previous["final"]["parameters"], dtype=float)
        trajectory = list(previous.get("trajectory", []))
    else:
        x = np.asarray(start["final"]["parameters"], dtype=float)
    faces = json.load((HERE / start["final"]["faces"]).open())
    atlas = flip_mod.adjacent_audit_atlas(reference, faces, x)
    points, den, guards, topology, _ = atlas.problem.evaluate(x)
    packet = packet_indices(atlas.problem)
    packet_values = guards[packet].copy()
    nonpacket = np.ones(len(guards), dtype=bool)
    nonpacket[packet] = False
    hpos = list(dynamic_mod.PACKET_KEYS).index(H910_KEY)
    if packet_values[hpos] >= 0.0:
        raise AssertionError(packet_values.tolist())
    trust = (
        min(0.004, float(trajectory[-1]["accepted_step"]) * 1.35)
        if trajectory and trajectory[-1].get("accepted_step") is not None
        else args.trust
    )
    verdict = "ITERATION_LIMIT"
    event = None

    first_iteration = len(trajectory)
    for iteration in range(first_iteration, first_iteration + args.iterations):
        direction, cone = target_direction(
            atlas, x, guards, topology, packet
        )
        row = {
            "iteration": iteration,
            "parameters_before": x.tolist(),
            "packet_before": packet_values.tolist(),
            "H910_before": float(packet_values[hpos]),
            "event_numerators_before": {
                k: v for k, v in event_numerators(
                    atlas.ids, points, faces
                ).items() if k != "mechanics"
            },
            "cone": cone,
            "trust_before": trust,
            "rejected_trials": [],
        }
        accepted = None
        h = trust
        while h >= args.minimum_step:
            trial_x = x + h * direction
            rejection = {"step": h}
            try:
                tp, td, tg, tt, _ = atlas.problem.evaluate(trial_x)
                trial_state = atlas.make_state(
                    0.0, trial_x - atlas.x0, trial_x, tp, td, tg, tt
                )
                trial_faces = trial_state.fresh_faces
                same_faces = {
                    frozenset(face) for face in trial_faces
                } == {frozenset(face) for face in faces}
                trial_packet = tg[packet]
                progress = trial_packet - packet_values
                numerators = event_numerators(atlas.ids, tp, faces)
                crossed = bool(trial_packet[hpos] >= 0.0)
                expected_class = [2, 3, 2] if crossed else [2, 3, 3]
                expected_saddles = (
                    {(5, 6), (6, 7)} if crossed
                    else {(5, 6), (6, 7), (9, 10)}
                )
                invariants = strict_common_invariants(
                    atlas, trial_state, expected_class, expected_saddles
                )
                five_progress = np.delete(progress, hpos)
                negatives = {
                    dynamic_mod.feature_key(atlas.problem.mech_labels[k])
                    for k in np.flatnonzero(tg < 0.0)
                }
                expected_negatives = set(dynamic_mod.PACKET_KEYS)
                if crossed:
                    expected_negatives.remove(H910_KEY)
                ok = (
                    trial_state.valid
                    and same_faces
                    and all(invariants.values())
                    and bool(np.all(five_progress > 1e-12))
                    and trial_packet[hpos] > packet_values[hpos]
                    and float(np.min(tg[nonpacket])) > 0.0
                    and negatives == expected_negatives
                    and numerators["N10R"] > 0.0
                )
                if ok:
                    accepted = (
                        h, trial_x, tp, td, tg, tt, trial_state,
                        trial_packet, progress, numerators, crossed,
                        invariants,
                    )
                    break
                rejection.update({
                    "reason": "finite_actual_cell",
                    "state_valid": trial_state.valid,
                    "same_faces": same_faces,
                    "packet": trial_packet.tolist(),
                    "packet_increment": progress.tolist(),
                    "minimum_nonpacket": float(np.min(tg[nonpacket])),
                    "negative_features": [list(key) for key in sorted(negatives)],
                    "event_numerators": {
                        k: v for k, v in numerators.items() if k != "mechanics"
                    },
                    "required_invariants": invariants,
                    "fresh": trial_state.fresh,
                })
            except Exception as exc:
                rejection.update({"reason": "evaluation_error", "error": repr(exc)})
            row["rejected_trials"].append(rejection)
            h *= 0.5

        if accepted is None:
            verdict = "FINITE_STEP_BLOCKER_BEFORE_H910_WALL"
            row["accepted_step"] = None
            trajectory.append(row)
            break

        (h, trial_x, tp, td, tg, tt, trial_state, trial_packet,
         progress, numerators, crossed, invariants) = accepted
        row.update({
            "accepted_step": h,
            "parameters_after": trial_x.tolist(),
            "packet_after": trial_packet.tolist(),
            "packet_increment": progress.tolist(),
            "H910_after": float(trial_packet[hpos]),
            "event_numerators_after": {
                k: v for k, v in numerators.items() if k != "mechanics"
            },
            "crossed_H910_wall": crossed,
            "required_invariants": invariants,
            "fresh_after": trial_state.fresh,
            "minimum_nonpacket_after": float(np.min(tg[nonpacket])),
            "minimum_topology_after": float(np.min(tt)),
        })
        trajectory.append(row)
        print(json.dumps({
            "iteration": iteration,
            "step": h,
            "H910": float(trial_packet[hpos]),
            "other_packet": np.delete(trial_packet, hpos).tolist(),
            "N10L": numerators["N10L"],
            "N10R": numerators["N10R"],
            "minimum_nonpacket": row["minimum_nonpacket_after"],
            "minimum_topology": row["minimum_topology_after"],
            "crossed": crossed,
        }), flush=True)

        if crossed:
            before_x = x.copy()
            before_h910 = float(packet_values[hpos])
            far_x = trial_x.copy()
            far_state = trial_state
            far_packet = trial_packet.copy()

            def numerator_h(s):
                xx = before_x + s * direction
                pp, _ = atlas.problem.chart.coordinates(xx)
                return event_numerators(atlas.ids, pp, faces)["N10L"]

            wall_h = brentq(numerator_h, 0.0, h,
                            xtol=5e-16, rtol=4 * np.finfo(float).eps)
            wall_x = before_x + wall_h * direction
            wp, wd, wg, wt, _ = atlas.problem.evaluate(wall_x)
            wall_state = atlas.make_state(
                0.0, wall_x - atlas.x0, wall_x, wp, wd, wg, wt
            )
            wall_num = event_numerators(atlas.ids, wp, faces)
            event = {
                "iteration": iteration,
                "bracket_step": [0.0, h],
                "H910_before": before_h910,
                "H910_far": float(far_packet[hpos]),
                "wall_step": wall_h,
                "wall_parameters": wall_x.tolist(),
                "wall_H910_guard": float(wg[packet[hpos]]),
                "wall_N10L": wall_num["N10L"],
                "wall_N10R": wall_num["N10R"],
                "wall_U10_components": wall_num["mechanics"]["ucomponents"][10],
                "wall_H910_components": wall_num["mechanics"]["ecomponents"][(9, 10)],
                "wall_H1011_components": wall_num["mechanics"]["ecomponents"][(10, 11)],
                "wall_fresh": wall_state.fresh,
                "far_parameters": far_x.tolist(),
                "far_packet": far_packet.tolist(),
                "far_fresh": far_state.fresh,
            }
            x, points, den, guards, topology = (
                far_x, far_state.points, far_state.den,
                far_state.guards, far_state.topology,
            )
            packet_values = far_packet
            verdict = "CLEAN_H910_DEATH_TO_FIVE_RESIDUAL_CELL"
            break

        x, points, den, guards, topology = (
            trial_x, tp, td, tg, tt
        )
        packet_values = trial_packet
        trust = min(0.004, h * 1.35)

    result = {
        "version": 1,
        "verdict": verdict,
        "source": START_JSON.name,
        "trajectory": trajectory,
        "event": event,
        "final": {
            "parameters": x.tolist(),
            "packet": [
                {"value": float(packet_values[j]), "feature": dynamic_mod.PACKET_KEYS[j]}
                for j in range(6)
            ],
        },
    }

    if event is not None:
        wall_x = np.asarray(event["wall_parameters"])
        wp, wd, wg, wt, _ = atlas.problem.evaluate(wall_x)
        wall_state = atlas.make_state(0.0, wall_x - atlas.x0, wall_x, wp, wd, wg, wt)
        far_x = np.asarray(event["far_parameters"])
        fp, fd, fg, ft, _ = atlas.problem.evaluate(far_x)
        far_state = atlas.make_state(0.0, far_x - atlas.x0, far_x, fp, fd, fg, ft)
        pre = trajectory[-1]
        pre_x = np.asarray(pre["parameters_before"])
        pp, pd, pg, pt, _ = atlas.problem.evaluate(pre_x)
        pre_state = atlas.make_state(0.0, pre_x - atlas.x0, pre_x, pp, pd, pg, pt)

        stems = {
            "pre": "row54_h910_pre_wall",
            "wall": "row54_h910_exact_wall",
            "far": "row54_h910_far_cell",
        }
        states = {"pre": pre_state, "wall": wall_state, "far": far_state}
        for side, state in states.items():
            stem = stems[side]
            write_csv(HERE / (stem + ".csv"), atlas.ids, state.points)
            json.dump(state.fresh_faces,
                      (HERE / (stem + "_faces.json")).open("w"), indent=2)
            audit, audited_faces = atlas.complete_audit(
                state, stem,
                certificate={
                    "event": "H910 common-numerator wall",
                    "side": side,
                    "wall_certificate": "row54_h910_exact_wall.json",
                },
            )
            audit.update({
                "coordinates": stem + ".csv",
                "fixed_expected_faces": stem + "_faces.json",
                "event_side": side,
                "signed_mechanics_packet": [
                    {
                        "value": float(state.guards[k]),
                        "feature": atlas.problem.mech_labels[k],
                    }
                    for k in packet
                ],
            })
            json.dump(atlas_mod.jsonable(audit),
                      (HERE / (stem + "_audit.json")).open("w"), indent=2)

        wall_record = {
            "version": 1,
            "verdict": verdict,
            "source": START_JSON.name,
            "common_numerator_identity": {
                "N10L": "(p10-c) dot (p10-p9)",
                "H910_active_component": "1-t = N10L / ||p10-p9||^2",
                "U10_toward_9_component": (
                    "N10L / (||p10-c|| ||p10-p9||)"
                ),
                "centroid": "c is the fresh polyhedron volume centroid",
            },
            "event": event,
            "sides": {
                side: {
                    "coordinates": stems[side] + ".csv",
                    "faces": stems[side] + "_faces.json",
                    "audit": stems[side] + "_audit.json",
                }
                for side in states
            },
            "residual_transition": {
                "before_class": [2, 3, 3],
                "far_class": [2, 3, 2],
                "removed_saddle": [9, 10],
                "remaining_negative_packet": [
                    list(key) for key in dynamic_mod.PACKET_KEYS
                    if key != H910_KEY
                ],
            },
        }
        json.dump(atlas_mod.jsonable(wall_record),
                  (HERE / "row54_h910_exact_wall.json").open("w"), indent=2)
        result["artifacts"] = wall_record["sides"]
        result["wall_certificate"] = "row54_h910_exact_wall.json"

    json.dump(atlas_mod.jsonable(result), (HERE / args.output).open("w"), indent=2)
    print(json.dumps({
        "output": args.output,
        "verdict": verdict,
        "iterations": len(trajectory),
        "event": event,
        "final_packet": result["final"]["packet"],
        "wall_certificate": result.get("wall_certificate"),
    }, indent=2), flush=True)


if __name__ == "__main__":
    main()
