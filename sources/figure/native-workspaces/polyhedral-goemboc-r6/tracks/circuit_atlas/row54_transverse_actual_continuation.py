#!/usr/bin/env python3
"""Fresh-hull integration of the full-44 transverse six-packet cone.

The formal square shared-root charts are deliberately abandoned here.  At
each actual-cell point we solve the minimum-L-infinity full-control tangent
which improves all six rawmin defects at the same normalized first-order rate
while holding the discovered U0/H(0,54) numerator and three support circuits
transverse.  A finite step is accepted only if a fresh hull still has all 61
rows, the enlarged stable base, U8, all 37 rails, the fixed flip cell, and every
nonpacket mechanics and topology guard strictly positive.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np

import row54_shared_root_active_set as active_mod
import row54_shared_root_atlas as atlas_mod


HERE = Path(__file__).resolve().parent
DEFAULT_ACTIVE = HERE / "row54_shared_root_active_set_svd.json"


def tuple_key(value):
    return tuple(tuple_key(x) for x in value) if isinstance(value, list) else value


def load_equations(record):
    row = record["stages"][-1]
    return [
        active_mod.Equation(eq["kind"], int(eq["index"]), float(eq["target"]),
                            float(eq["scale"]), tuple_key(eq["key"]))
        for eq in row["equations"]
    ]


def write_csv(path, ids, points):
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(("source_id", "x", "y", "z"))
        for i, p in zip(ids, points):
            w.writerow([i, *[format(float(v), ".17g") for v in p]])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--active-set", default=str(DEFAULT_ACTIVE))
    ap.add_argument("--iterations", type=int, default=24)
    ap.add_argument("--trust", type=float, default=0.006)
    ap.add_argument("--minimum-step", type=float, default=2e-7)
    ap.add_argument("--fd-step", type=float, default=8e-6)
    ap.add_argument("--resume", help="continue from a prior continuation JSON")
    ap.add_argument("--output", default="row54_transverse_actual_continuation.json")
    ap.add_argument("--prefix", default="row54_transverse_actual_continuation")
    args = ap.parse_args()

    atlas = atlas_mod.Atlas(atlas_mod.DEFAULT_SOURCE, atlas_mod.DEFAULT_FACES,
                            atlas_mod.DEFAULT_START, args.fd_step)
    solver = active_mod.ActiveSet(atlas, 32, args.fd_step)
    active_record = json.load(Path(args.active_set).open())
    equations = load_equations(active_record)
    previous = None
    x = atlas.x0.copy()
    if args.resume:
        previous = json.load((HERE / args.resume).open())
        parameters = (previous["final"]["parameters"]
                      if "final" in previous else previous["parameters"])
        x = np.asarray(parameters, dtype=float)
    p, den, guards, top, _ = atlas.problem.evaluate(x)
    state = atlas.make_state(0.0, x - atlas.x0, x, p, den, guards, top)
    trust = args.trust
    trajectory = [] if previous is None else list(previous.get("trajectory", []))
    first_iteration = len(trajectory)
    verdict = "ITERATION_LIMIT"
    final_cone = None

    for iteration in range(first_iteration, first_iteration + args.iterations):
        cone = solver.active_cone(state, equations)
        final_cone = cone
        row = {
            "iteration": iteration,
            "parameters_before": state.x.tolist(),
            "minimum_Linf_cone_norm": cone.get("minimum_Linf_norm"),
            "cone_success": cone["success"],
            "cone_message": cone["message"],
            "trust_before": trust,
            "packet_before": [
                {"value": float(state.guards[k]),
                 "feature": atlas.problem.mech_labels[k]}
                for k in np.flatnonzero(atlas.active)
            ],
            "minimum_nonpacket_before": float(np.min(state.guards[atlas.noncritical])),
            "minimum_topology_before": float(np.min(state.topology)),
            "fresh_before": state.fresh,
        }
        if not cone["success"]:
            verdict = "FULL44_ACTIVE_CONE_BLOCKER"
            trajectory.append(row)
            break
        direction = np.asarray(cone["direction"], dtype=float)
        accepted = None
        rejected_trials = []
        h = trust
        while h >= args.minimum_step:
            trial_x = state.x + h * direction
            trial_error = None
            try:
                tp, td, tg, tt, _ = atlas.problem.evaluate(trial_x)
                trial = atlas.make_state(state.t + h, trial_x - atlas.x0,
                                         trial_x, tp, td, tg, tt)
            except Exception as exc:
                trial = None
                trial_error = repr(exc)
            if trial is not None:
                packet_delta = trial.guards[atlas.active] - state.guards[atlas.active]
                # Strict simultaneous progress in all six walls, not merely a
                # better minimax score.  The tolerance is below the observed
                # fresh mechanics noise by two orders of magnitude.
                progress = bool(np.all(packet_delta > 1e-12))
                if trial.valid and progress:
                    accepted = (h, trial, packet_delta)
                    break
                rejected_trials.append({
                    "step": h,
                    "reason": (
                        "actual_cell" if not trial.valid else
                        "not_simultaneous_packet_progress"
                    ),
                    "invalid_reasons": trial.invalid_reasons,
                    "minimum_packet_increment": float(np.min(packet_delta)),
                    "packet_increment": packet_delta.tolist(),
                    "minimum_nonpacket_guard": float(np.min(
                        trial.guards[atlas.noncritical]
                    )),
                    "closest_nonpacket": atlas.state_record(trial)[
                        "closest_nonpacket_mechanics"
                    ][:6],
                    "minimum_topology_guard": float(np.min(trial.topology)),
                    "closest_topology": atlas.state_record(trial)[
                        "closest_fixed_topology"
                    ][:8],
                    "fresh_hull_audit": trial.fresh,
                })
            else:
                rejected_trials.append({
                    "step": h,
                    "reason": "evaluation_error",
                    "error": trial_error,
                })
            h *= 0.5
        row["rejected_trials"] = rejected_trials
        if accepted is None:
            verdict = "FINITE_STEP_BLOCKER_WITH_FEASIBLE_TANGENT"
            row["accepted_step"] = None
            trajectory.append(row)
            break
        h, state, packet_delta = accepted
        normalized_delta = packet_delta / atlas.active_scales
        row.update({
            "accepted_step": h,
            "parameters_after": state.x.tolist(),
            "packet_after": [
                {"value": float(state.guards[k]),
                 "feature": atlas.problem.mech_labels[k]}
                for k in np.flatnonzero(atlas.active)
            ],
            "normalized_packet_increment": normalized_delta.tolist(),
            "minimum_normalized_packet_increment": float(np.min(normalized_delta)),
            "minimum_nonpacket_after": float(np.min(state.guards[atlas.noncritical])),
            "minimum_topology_after": float(np.min(state.topology)),
            "minimum_projective_denominator_after": float(np.min(state.den)),
            "fresh_after": state.fresh,
        })
        trajectory.append(row)
        print(json.dumps({
            "iteration": iteration, "step": h,
            "packet": state.guards[atlas.active].tolist(),
            "min_normalized_increment": float(np.min(normalized_delta)),
            "nonpacket": float(np.min(state.guards[atlas.noncritical])),
            "topology": float(np.min(state.topology)),
            "cone_norm": cone.get("minimum_Linf_norm"),
        }), flush=True)
        if bool(np.all(state.guards > 0.0)):
            verdict = "TARGET_CELL_REACHED"
            break
        trust = min(0.03, h * 1.35)

    audit, faces = atlas.complete_audit(
        state, args.prefix,
        certificate={
            "verdict": verdict,
            "preserved_equations": [eq.__dict__ for eq in equations],
            "final_full44_cone": final_cone,
        },
    )
    csv_name = args.prefix + ".csv"
    faces_name = args.prefix + "_faces.json"
    audit_name = args.prefix + "_audit.json"
    write_csv(HERE / csv_name, atlas.ids, state.points)
    json.dump(faces, (HERE / faces_name).open("w"), indent=2)
    audit.update({
        "coordinates": csv_name,
        "fixed_expected_faces": faces_name,
        "source_active_set": Path(args.active_set).name,
    })
    json.dump(atlas_mod.jsonable(audit), (HERE / audit_name).open("w"), indent=2)
    result = {
        "version": 1,
        "verdict": verdict,
        "source": atlas_mod.DEFAULT_SOURCE.name,
        "start": atlas_mod.DEFAULT_START.name,
        "active_set": Path(args.active_set).name,
        "preserved_equations": [eq.__dict__ for eq in equations],
        "iterations_requested": args.iterations,
        "trajectory": trajectory,
        "final": {
            "parameters": state.x.tolist(),
            "packet": [
                {"value": float(state.guards[k]),
                 "feature": atlas.problem.mech_labels[k]}
                for k in np.flatnonzero(atlas.active)
            ],
            "minimum_nonpacket_guard": float(np.min(state.guards[atlas.noncritical])),
            "minimum_topology_guard": float(np.min(state.topology)),
            "fresh_hull_audit": state.fresh,
            "coordinates": csv_name,
            "faces": faces_name,
            "complete_audit": audit_name,
        },
        "final_full44_cone": final_cone,
    }
    json.dump(atlas_mod.jsonable(result), (HERE / args.output).open("w"), indent=2)
    print(json.dumps({
        "output": args.output, "verdict": verdict,
        "iterations": len(trajectory),
        "packet": result["final"]["packet"],
        "minimum_nonpacket_guard": result["final"]["minimum_nonpacket_guard"],
        "minimum_topology_guard": result["final"]["minimum_topology_guard"],
        "coordinates": csv_name, "audit": audit_name,
    }, indent=2), flush=True)


if __name__ == "__main__":
    main()
