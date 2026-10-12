#!/usr/bin/env python3
"""Dynamic actual-cell continuation after the {12,13,261,262} flip.

Each iteration recomputes the full 44-control Jacobian on the *current* face
lattice.  A first LP maximizes the weakest normalized improvement of the six
mechanics defects.  A lexicographic second LP retains half of that rate while
maximizing the weakest inward derivative of all nearby and promoted guards.

Finite steps receive a fresh hull/own-centroid audit.  A step may update the
face lattice only by one clean 2-2 support flip; it must still retain all 61
rows, the original {2,3,88,242} flip, the enlarged stable base, U8, and all 37
forced rail edges.  The row-15 determinant is checked directly to stay > 0.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

import row54_four_residual_search as core
import row54_post_row15_clean_flip as flip_mod
import row54_shared_root_atlas as atlas_mod


HERE = Path(__file__).resolve().parent
START_AUDIT = HERE / "row54_post_row15_clean_flip_audit.json"
START_FACES = HERE / "row54_post_row15_clean_flip_faces.json"
FD_STEP = 8e-6
CONTROL_RADIUS = 0.5
PACKET_FRACTION = 0.5
MECHANICS_NEAR = 5e-4
TOPOLOGY_NEAR = 1e-7
PROMOTED_CIRCUITS = {
    (2, 3, 88, 242),
    (7, 8, 245, 246),
    (9, 198, 263, 264),
    (11, 198, 262, 263),
    (12, 13, 261, 262),
    (14, 15, 16, 72),
    (14, 72, 73, 261),
}


def write_csv(path, ids, points):
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(("source_id", "x", "y", "z"))
        for i, p in zip(ids, points):
            w.writerow([i, *[format(float(v), ".17g") for v in p]])


def feature_key(label):
    kind, value = label
    if kind.startswith("S") or kind.startswith("H"):
        return kind, tuple(sorted(value))
    return kind, int(value)


PACKET_KEYS = (
    ("S-", (7, 8, 246)),
    ("U-", 6),
    ("U-", 54),
    ("H-", (5, 6)),
    ("H-", (6, 7)),
    ("H-", (9, 10)),
)


def packet_indices(atlas):
    by_key = {
        feature_key(label): k
        for k, label in enumerate(atlas.problem.mech_labels)
    }
    indices = np.asarray([by_key[key] for key in PACKET_KEYS], dtype=int)
    if set(indices) != set(np.flatnonzero(atlas.active)):
        wrong = [
            (float(atlas.active_g0[pos]), atlas.problem.mech_labels[k])
            for pos, k in enumerate(np.flatnonzero(atlas.active))
        ]
        raise AssertionError(("unexpected adjacent packet", wrong))
    return indices


def cone_rows(atlas, x, jm, jt, guards, topology):
    rows, scales, labels = [], [], []
    seen = set()

    for k, label in enumerate(atlas.problem.mech_labels):
        if label == ("U-", 0):
            rows.append(jm[k])
            scales.append(max(abs(guards[k]), 1e-4))
            labels.append(("mechanics", k, label))
            seen.add(("mechanics", k))

    for k, label in enumerate(atlas.problem.top_labels):
        circuit = tuple(sorted(set(label[2]) | {label[3]}))
        if label[0] == "support" and circuit in PROMOTED_CIRCUITS:
            rows.append(jt[k])
            scales.append(max(abs(topology[k]), 1e-7))
            labels.append(("topology", k, label))
            seen.add(("topology", k))

    for k in np.flatnonzero(atlas.noncritical):
        if (guards[k] < MECHANICS_NEAR
                and ("mechanics", int(k)) not in seen):
            rows.append(jm[k])
            scales.append(max(abs(guards[k]), 1e-4))
            labels.append(("mechanics", int(k), atlas.problem.mech_labels[k]))
            seen.add(("mechanics", int(k)))
    for k, value in enumerate(topology):
        if value < TOPOLOGY_NEAR and ("topology", k) not in seen:
            rows.append(jt[k])
            scales.append(max(abs(value), 1e-7))
            labels.append(("topology", k, atlas.problem.top_labels[k]))
            seen.add(("topology", k))
    return np.asarray(rows), np.asarray(scales), labels


def lexicographic_direction(atlas, x):
    _, _, guards, topology, _ = atlas.problem.evaluate(x)
    jm, jt = atlas.finite_full(x)
    packet = packet_indices(atlas)
    packet_scales = np.maximum(np.abs(guards[packet]), 2.5e-4)
    jp = jm[packet] / packet_scales[:, None]
    rows, scales, labels = cone_rows(atlas, x, jm, jt, guards, topology)
    normalized_rows = rows / scales[:, None]

    # Stage 1: maximum simultaneous packet rate.
    aub1 = np.vstack((
        np.c_[-jp, np.ones(len(packet))],
        np.c_[-normalized_rows, np.zeros(len(normalized_rows))],
    ))
    c1 = np.zeros(45)
    c1[-1] = -1.0
    lp1 = linprog(
        c1, A_ub=aub1, b_ub=np.zeros(len(aub1)),
        bounds=[(-CONTROL_RADIUS, CONTROL_RADIUS)] * 44 + [(None, None)],
        method="highs",
    )
    if not lp1.success:
        raise RuntimeError(lp1.message)
    packet_maximum = float(lp1.x[-1])
    retained_packet_rate = PACKET_FRACTION * packet_maximum

    # Stage 2: with a useful packet rate retained, move every close wall
    # inward as strongly as possible.
    aub2 = np.vstack((
        np.c_[-normalized_rows, np.ones(len(normalized_rows))],
        np.c_[-jp, np.zeros(len(packet))],
    ))
    bub2 = np.r_[
        np.zeros(len(normalized_rows)),
        -retained_packet_rate * np.ones(len(packet)),
    ]
    c2 = np.zeros(45)
    c2[-1] = -1.0
    lp2 = linprog(
        c2, A_ub=aub2, b_ub=bub2,
        bounds=[(-CONTROL_RADIUS, CONTROL_RADIUS)] * 44 + [(None, None)],
        method="highs",
    )
    if not lp2.success:
        raise RuntimeError(lp2.message)
    direction = lp2.x[:44]
    rates = normalized_rows @ direction
    return direction, {
        "packet_LP_success": bool(lp1.success),
        "packet_maximum_weakest_normalized_rate": packet_maximum,
        "retained_packet_fraction": PACKET_FRACTION,
        "retained_packet_rate": retained_packet_rate,
        "inward_LP_success": bool(lp2.success),
        "maximum_weakest_normalized_guard_rate": float(lp2.x[-1]),
        "packet_normalized_rates": (jp @ direction).tolist(),
        "minimum_normalized_guard_rate": float(np.min(rates)),
        "maximum_absolute_control_rate": float(np.max(np.abs(direction))),
        "weakest_guard_rates": [
            {
                "normalized_rate": float(rates[k]),
                "constraint": labels[int(k)],
            }
            for k in np.argsort(rates)[:20]
        ],
        "direction": direction.tolist(),
    }


def clean_flip(old_faces, new_faces):
    old = {frozenset(face) for face in old_faces}
    new = {frozenset(face) for face in new_faces}
    removed = sorted((sorted(face) for face in old - new), key=tuple)
    added = sorted((sorted(face) for face in new - old), key=tuple)
    if not removed and not added:
        return None
    if len(removed) != 2 or len(added) != 2:
        return False
    union = set().union(*(set(face) for face in removed + added))
    old_diagonal = sorted(set(removed[0]) & set(removed[1]))
    new_diagonal = sorted(set(added[0]) & set(added[1]))
    if len(union) != 4 or len(old_diagonal) != 2 or len(new_diagonal) != 2:
        return False
    return {
        "circuit": sorted(union),
        "old_diagonal": old_diagonal,
        "new_diagonal": new_diagonal,
        "removed_faces": removed,
        "added_faces": added,
        "common_determinant_identity": (
            "the two crossed support guards have the common oriented "
            "four-point determinant numerator of this circuit"
        ),
    }


def required_invariants(state):
    edges, _ = core.edge_lattice(state.fresh_faces)
    stable = {frozenset(face) for face in state.fresh.get("stable_faces", [])}
    saddles = {tuple(sorted(edge)) for edge in state.fresh.get("saddle_edges", [])}
    return {
        "f_vector_61_162_103": state.fresh.get("f_vector") == [61, 162, 103],
        "class_2_3_3": state.fresh.get("class") == [2, 3, 3],
        "stable_faces_exact": stable == {
            core.BASE, frozenset((7, 8, 246))
        },
        "unstable_vertices_exact": set(
            state.fresh.get("unstable_vertices", [])
        ) == {6, 8, 54},
        "saddle_edges_exact": saddles == {(5, 6), (6, 7), (9, 10)},
        "all_61_rows_active": state.fresh.get("all_61_rows_active") is True,
        "enlarged_base_present": state.fresh.get("enlarged_base_present") is True,
        "enlarged_base_stable": state.fresh.get("enlarged_base_stable") is True,
        "U8_unstable": state.fresh.get("U8_unstable") is True,
        "all_forced_rail_edges_present": state.fresh.get(
            "all_forced_rail_edges_present"
        ) is True,
        "edge_0_1_absent": (0, 1) not in edges,
        "original_fixed_flip_new_diagonal_3_88": (3, 88) in edges,
        "original_fixed_flip_old_diagonal_2_242_absent": (2, 242) not in edges,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--iterations", type=int, default=8)
    ap.add_argument("--trust", type=float, default=0.008)
    ap.add_argument("--minimum-step", type=float, default=2e-6)
    ap.add_argument("--resume", help="continue from a prior dynamic JSON")
    ap.add_argument("--output", default="row54_adjacent_dynamic_continuation.json")
    ap.add_argument("--prefix", default="row54_adjacent_dynamic_continuation")
    args = ap.parse_args()

    reference = atlas_mod.Atlas(atlas_mod.DEFAULT_SOURCE, atlas_mod.DEFAULT_FACES,
                                atlas_mod.DEFAULT_START, FD_STEP)
    previous = None
    trajectory = []
    if args.resume:
        previous = json.load((HERE / args.resume).open())
        x = np.asarray(previous["final"]["parameters"], dtype=float)
        faces = json.load((HERE / previous["final"]["faces"]).open())
        trajectory = list(previous.get("trajectory", []))
    else:
        start = json.load(START_AUDIT.open())
        x = np.asarray(start["parameters"], dtype=float)
        faces = json.load(START_FACES.open())
    atlas = flip_mod.adjacent_audit_atlas(reference, faces, x)
    p, den, guards, top, _ = atlas.problem.evaluate(x)
    state = atlas.make_state(0.0, x - atlas.x0, x, p, den, guards, top)
    if not state.valid:
        raise AssertionError(state.invalid_reasons)
    packet = packet_indices(atlas)
    packet_values = guards[packet].copy()
    trust = (
        min(0.02, float(trajectory[-1]["accepted_step"]) * 1.25)
        if trajectory and trajectory[-1].get("accepted_step") is not None
        else args.trust
    )
    verdict = "ITERATION_LIMIT"

    first_iteration = len(trajectory)
    for iteration in range(first_iteration, first_iteration + args.iterations):
        direction, cone = lexicographic_direction(atlas, x)
        row = {
            "iteration": iteration,
            "parameters_before": x.tolist(),
            "packet_before": packet_values.tolist(),
            "row15_determinant_before": flip_mod.circuit_determinant(
                reference, x, flip_mod.ROW15_CIRCUIT
            ),
            "face_count_before": len(faces),
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
                tp, td, _, _, _ = atlas.problem.evaluate(trial_x)
                fresh, trial_faces = atlas.fresh_summary(tp)
                trial_atlas = flip_mod.adjacent_audit_atlas(
                    reference, trial_faces, trial_x
                )
                qp, qd, qg, qt, _ = trial_atlas.problem.evaluate(trial_x)
                trial_state = trial_atlas.make_state(
                    0.0, trial_x - trial_atlas.x0, trial_x,
                    qp, qd, qg, qt,
                )
                trial_packet = packet_indices(trial_atlas)
                trial_packet_values = qg[trial_packet]
                progress = trial_packet_values - packet_values
                flip = clean_flip(faces, trial_faces)
                invariants = required_invariants(trial_state)
                row15_det = flip_mod.circuit_determinant(
                    reference, trial_x, flip_mod.ROW15_CIRCUIT
                )
                admissible_faces = flip is None or isinstance(flip, dict)
                ok = (
                    trial_state.valid
                    and all(invariants.values())
                    and admissible_faces
                    and row15_det > 0.0
                    and bool(np.all(progress > 1e-12))
                )
                if ok:
                    accepted = (
                        h, trial_x, trial_atlas, trial_state,
                        trial_faces, trial_packet, trial_packet_values,
                        progress, flip, invariants, row15_det,
                    )
                    break
                rejection.update({
                    "reason": "finite_actual_cell",
                    "state_valid": trial_state.valid,
                    "invalid_reasons": trial_state.invalid_reasons,
                    "minimum_packet_increment": float(np.min(progress)),
                    "row15_determinant": row15_det,
                    "face_transition": flip,
                    "required_invariants": invariants,
                    "fresh": fresh,
                    "minimum_topology_guard": float(np.min(qt)),
                })
            except Exception as exc:
                rejection.update({
                    "reason": "evaluation_error",
                    "error": repr(exc),
                })
            row["rejected_trials"].append(rejection)
            h *= 0.5
        if accepted is None:
            verdict = "FINITE_ACTUAL_CELL_BLOCKER"
            row["accepted_step"] = None
            trajectory.append(row)
            break

        (h, x, atlas, state, faces, packet, new_packet_values,
         progress, flip, invariants, row15_det) = accepted
        packet_values = new_packet_values
        row.update({
            "accepted_step": h,
            "parameters_after": x.tolist(),
            "packet_after": packet_values.tolist(),
            "packet_increment": progress.tolist(),
            "minimum_normalized_packet_increment": float(np.min(
                progress / np.maximum(np.abs(row["packet_before"]), 2.5e-4)
            )),
            "row15_determinant_after": row15_det,
            "face_transition": flip,
            "required_invariants": invariants,
            "fresh_after": state.fresh,
            "minimum_topology_after": float(np.min(state.topology)),
            "minimum_nonpacket_after": float(np.min(
                state.guards[atlas.noncritical]
            )),
        })
        trajectory.append(row)
        print(json.dumps({
            "iteration": iteration,
            "step": h,
            "packet": packet_values.tolist(),
            "minimum_normalized_packet_increment": row[
                "minimum_normalized_packet_increment"
            ],
            "row15_determinant": row15_det,
            "face_transition": flip,
            "minimum_topology": row["minimum_topology_after"],
        }), flush=True)
        trust = min(0.02, h * 1.25)

    csv_name = args.prefix + ".csv"
    faces_name = args.prefix + "_faces.json"
    audit_name = args.prefix + "_audit.json"
    write_csv(HERE / csv_name, atlas.ids, state.points)
    json.dump(faces, (HERE / faces_name).open("w"), indent=2)
    audit, audited_faces = atlas.complete_audit(
        state, args.prefix,
        certificate={
            "verdict": verdict,
            "source_endpoint": START_AUDIT.name,
            "dynamic_face_lattice": True,
            "row15_circuit_guard_strict": flip_mod.circuit_determinant(
                reference, x, flip_mod.ROW15_CIRCUIT
            ),
            "trajectory_clean_flip_events": [
                row["face_transition"] for row in trajectory
                if isinstance(row.get("face_transition"), dict)
            ],
        },
    )
    if {frozenset(face) for face in audited_faces} != {
            frozenset(face) for face in faces}:
        raise AssertionError("final dynamic faces changed during audit")
    audit.update({
        "coordinates": csv_name,
        "fixed_expected_faces": faces_name,
        "packet": [
            {"value": float(packet_values[j]), "feature": PACKET_KEYS[j]}
            for j in range(6)
        ],
    })
    json.dump(atlas_mod.jsonable(audit),
              (HERE / audit_name).open("w"), indent=2)
    result = {
        "version": 1,
        "verdict": verdict,
        "source_endpoint": START_AUDIT.name,
        "iterations_requested": len(trajectory),
        "trajectory": trajectory,
        "final": {
            "parameters": x.tolist(),
            "packet": audit["packet"],
            "row15_determinant": flip_mod.circuit_determinant(
                reference, x, flip_mod.ROW15_CIRCUIT
            ),
            "fresh": state.fresh,
            "required_invariants": required_invariants(state),
            "coordinates": csv_name,
            "faces": faces_name,
            "audit": audit_name,
        },
    }
    json.dump(atlas_mod.jsonable(result), (HERE / args.output).open("w"), indent=2)
    print(json.dumps({
        "output": args.output,
        "verdict": verdict,
        "accepted_iterations": sum(
            row.get("accepted_step") is not None for row in trajectory
        ),
        "packet": result["final"]["packet"],
        "row15_determinant": result["final"]["row15_determinant"],
        "clean_flips": [
            row["face_transition"] for row in trajectory
            if isinstance(row.get("face_transition"), dict)
        ],
        "coordinates": csv_name,
        "audit": audit_name,
    }, indent=2), flush=True)


if __name__ == "__main__":
    main()
