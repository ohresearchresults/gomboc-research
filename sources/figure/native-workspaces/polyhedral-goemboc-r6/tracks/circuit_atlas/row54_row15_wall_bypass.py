#!/usr/bin/env python3
"""Materialize the exact row-15 loss wall and its full-44 nullspace bypass.

The first newly observed invalid finite step of the transverse continuation
collapses base vertex 15.  Four normalized fixed-cell guards share the same
oriented determinant of rows {14,15,16,72}.  This script locates that common
zero along the rejected direction, then certifies the subsequent fresh path
which turns the determinant inward while all six packet guards keep improving.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

import row54_four_residual_search as core
import row54_shared_root_atlas as atlas_mod


HERE = Path(__file__).resolve().parent
TRAJECTORY = HERE / "row54_transverse_inward_continuation.json"
APPROACH_ITERATION = 72
TURN_ITERATION = 74
BYPASS_ITERATION = 75
CIRCUIT = (14, 15, 16, 72)
TOPOLOGY_ROWS = (6282, 6298, 1783, 1600)


def write_csv(path, ids, points):
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(("source_id", "x", "y", "z"))
        for i, p in zip(ids, points):
            w.writerow([i, *[format(float(v), ".17g") for v in p]])


def main():
    atlas = atlas_mod.Atlas(atlas_mod.DEFAULT_SOURCE, atlas_mod.DEFAULT_FACES,
                            atlas_mod.DEFAULT_START, 8e-6)
    record = json.load(TRAJECTORY.open())
    trajectory = record["trajectory"]
    approach = trajectory[APPROACH_ITERATION]
    turn = trajectory[TURN_ITERATION]
    bypass = trajectory[BYPASS_ITERATION]
    x_before = np.asarray(approach["parameters_before"], dtype=float)
    x_after = np.asarray(approach["parameters_after"], dtype=float)
    approach_step = float(approach["accepted_step"])
    approach_direction = (x_after - x_before) / approach_step
    ix = atlas.problem.chart.ix

    def points_at(x):
        points, den = atlas.problem.chart.coordinates(np.asarray(x))
        if points is None:
            raise ValueError(float(np.min(den)))
        return points

    def determinant_x(x):
        p = points_at(x)
        a, b, c, w = (p[ix[k]] for k in CIRCUIT)
        return float(np.dot(np.cross(b - a, c - a), w - a))

    def determinant_h(h):
        return determinant_x(x_before + h * approach_direction)

    valid_h = approach_step
    invalid_h = min(
        float(row["step"]) for row in approach["rejected_trials"]
        if row["reason"] == "actual_cell" and float(row["step"]) > valid_h
    )
    d_valid = determinant_h(valid_h)
    d_invalid = determinant_h(invalid_h)
    if d_valid * d_invalid >= 0.0:
        raise AssertionError((d_valid, d_invalid))
    wall_h = brentq(determinant_h, valid_h, invalid_h,
                    xtol=5e-16, rtol=4 * np.finfo(float).eps)
    wall_x = x_before + wall_h * approach_direction
    wall_points, wall_den, wall_guards, wall_top, _ = atlas.problem.evaluate(wall_x)
    wall_det = determinant_x(wall_x)

    p14, p15, p16, p72 = (wall_points[ix[k]] for k in CIRCUIT)
    chord = p16 - p14
    chord_parameter = float(np.dot(p15 - p14, chord) / np.dot(chord, chord))
    collinearity_residual = float(np.linalg.norm(
        p15 - (p14 + chord_parameter * chord)
    ))

    pre_points, pre_den, pre_guards, pre_top, _ = atlas.problem.evaluate(x_before)
    common_rows = []
    pre_det = determinant_x(x_before)
    for k in TOPOLOGY_ROWS:
        common_rows.append({
            "guard_index": k,
            "label": atlas.problem.top_labels[k],
            "before": float(pre_top[k]),
            "before_guard_over_determinant": float(pre_top[k] / pre_det),
            "wall": float(wall_top[k]),
        })

    # At iteration 73 the old direction is closest to the wall.  Iteration 74
    # is the first recomputed cone direction with positive determinant rate.
    x_turn = np.asarray(turn["parameters_before"], dtype=float)
    v_turn = (
        np.asarray(turn["parameters_after"], dtype=float) - x_turn
    ) / float(turn["accepted_step"])
    previous = trajectory[TURN_ITERATION - 1]
    v_previous = (
        np.asarray(previous["parameters_after"], dtype=float)
        - np.asarray(previous["parameters_before"], dtype=float)
    ) / float(previous["accepted_step"])

    def directional_det(x, v):
        h = 2e-6 / max(1.0, float(np.max(np.abs(v))))
        return (determinant_x(x + h * v) - determinant_x(x - h * v)) / (2 * h)

    jm, _ = atlas.finite_full(x_turn)
    packet_scales = atlas.active_scales
    packet_previous = jm[atlas.active] @ v_previous / packet_scales
    packet_turn = jm[atlas.active] @ v_turn / packet_scales
    packet_correction = jm[atlas.active] @ (v_turn - v_previous) / packet_scales
    old_det_rate = directional_det(x_turn, v_previous)
    new_det_rate = directional_det(x_turn, v_turn)

    # Project the observed direction change onto the exact numerical kernel of
    # the normalized six-row Jacobian.  Scaling this kernel correction just
    # past the determinant-rate zero gives a literal transverse nullspace
    # bypass: packet derivatives are unchanged to solver precision while the
    # row-15 circuit turns from outward to inward.
    jpacket = jm[atlas.active] / packet_scales[:, None]
    observed_correction = v_turn - v_previous
    nullspace_correction = observed_correction - jpacket.T @ np.linalg.solve(
        jpacket @ jpacket.T, jpacket @ observed_correction
    )
    nullspace_residual = jpacket @ nullspace_correction
    nullspace_det_rate = directional_det(x_turn, nullspace_correction)
    nullspace_scale = (-old_det_rate + 1e-10) / nullspace_det_rate
    exact_bypass_direction = v_previous + nullspace_scale * nullspace_correction
    exact_det_rate = directional_det(x_turn, exact_bypass_direction)
    exact_packet_rates = jpacket @ exact_bypass_direction
    turn_points, turn_den, turn_guards, turn_top, _ = atlas.problem.evaluate(x_turn)
    exact_state = None
    exact_step = 1e-3
    exact_rejections = []
    while exact_step >= 1e-7:
        ex = x_turn + exact_step * exact_bypass_direction
        ep, ed, eg, et, _ = atlas.problem.evaluate(ex)
        candidate = atlas.make_state(0.0, ex - atlas.x0, ex, ep, ed, eg, et)
        packet_increment = eg[atlas.active] - turn_guards[atlas.active]
        if candidate.valid and np.all(packet_increment > 1e-12) \
                and determinant_x(ex) > determinant_x(x_turn):
            exact_state = candidate
            break
        exact_rejections.append({
            "step": exact_step,
            "valid_actual_cell": candidate.valid,
            "invalid_reasons": candidate.invalid_reasons,
            "packet_increment": packet_increment.tolist(),
            "determinant": determinant_x(ex),
        })
        exact_step *= 0.5
    if exact_state is None:
        raise AssertionError("no finite exact-nullspace bypass step")

    bypass_x = np.asarray(bypass["parameters_after"], dtype=float)
    bp, bd, bg, bt, _ = atlas.problem.evaluate(bypass_x)
    bypass_state = atlas.make_state(
        sum(float(r.get("accepted_step") or 0.0) for r in trajectory[:BYPASS_ITERATION + 1]),
        bypass_x - atlas.x0, bypass_x, bp, bd, bg, bt,
    )
    if not bypass_state.valid:
        raise AssertionError(bypass_state.invalid_reasons)
    bypass_det = determinant_x(bypass_x)
    if not bypass_det > pre_det:
        raise AssertionError((pre_det, bypass_det))
    wall_hull_summary = None
    wall_faces = []
    try:
        wh, wall_faces, _ = core.group_maximal_faces(atlas.ids, wall_points)
        we, _ = core.edge_lattice(wall_faces)
        wall_hull_summary = {
            "f_vector": [len(wh.vertices), len(we), len(wall_faces)],
            "active_ids": [atlas.ids[int(k)] for k in wh.vertices],
            "row15_active": 15 in {atlas.ids[int(k)] for k in wh.vertices},
        }
    except Exception as exc:
        wall_hull_summary = {"qhull_at_degeneracy_error": repr(exc)}

    wall_csv = "row54_row15_exact_wall.csv"
    wall_faces_name = "row54_row15_exact_wall_faces.json"
    wall_json = "row54_row15_exact_wall.json"
    exact_csv = "row54_row15_exact_nullspace_bypass.csv"
    exact_faces_name = "row54_row15_exact_nullspace_bypass_faces.json"
    exact_audit_name = "row54_row15_exact_nullspace_bypass_audit.json"
    write_csv(HERE / wall_csv, atlas.ids, wall_points)
    json.dump(wall_faces, (HERE / wall_faces_name).open("w"), indent=2)
    exact_audit, exact_faces = atlas.complete_audit(
        exact_state, "row54_row15_exact_nullspace_bypass",
        certificate={
            "circuit": list(CIRCUIT),
            "normalized_packet_jacobian_nullspace_residual": nullspace_residual.tolist(),
            "maximum_absolute_nullspace_residual": float(np.max(np.abs(nullspace_residual))),
            "approach_determinant_derivative": old_det_rate,
            "nullspace_correction_determinant_derivative": nullspace_det_rate,
            "nullspace_scale": nullspace_scale,
            "exact_bypass_determinant_derivative": exact_det_rate,
            "approach_packet_normalized_derivatives": packet_previous.tolist(),
            "exact_bypass_packet_normalized_derivatives": exact_packet_rates.tolist(),
            "finite_step": exact_step,
            "determinant_before": determinant_x(x_turn),
            "determinant_after": determinant_x(exact_state.x),
            "rejected_larger_steps": exact_rejections,
        },
    )
    write_csv(HERE / exact_csv, atlas.ids, exact_state.points)
    json.dump(exact_faces, (HERE / exact_faces_name).open("w"), indent=2)
    exact_audit.update({
        "coordinates": exact_csv,
        "fixed_expected_faces": exact_faces_name,
        "wall_certificate": wall_json,
    })
    json.dump(atlas_mod.jsonable(exact_audit),
              (HERE / exact_audit_name).open("w"), indent=2)
    wall_record = {
        "version": 1,
        "verdict": "EXACT_COMMON_DETERMINANT_ROW15_LOSS_WALL_WITH_FRESH_NULLSPACE_BYPASS",
        "source_trajectory": TRAJECTORY.name,
        "approach_iteration": APPROACH_ITERATION,
        "valid_step": valid_h,
        "invalid_step": invalid_h,
        "wall_step": wall_h,
        "wall_bracket_width": invalid_h - valid_h,
        "parameters": wall_x.tolist(),
        "coordinates": wall_csv,
        "qhull_faces_at_degeneracy": wall_faces_name,
        "minimum_projective_denominator": float(np.min(wall_den)),
        "circuit": list(CIRCUIT),
        "common_oriented_determinant": wall_det,
        "determinant_valid_side": d_valid,
        "determinant_invalid_side": d_invalid,
        "row15_chord_parameter_14_to_16": chord_parameter,
        "row15_collinearity_residual": collinearity_residual,
        "common_guard_rows": common_rows,
        "wall_hull_summary": wall_hull_summary,
        "observed_path_turn": {
            "turn_iteration": TURN_ITERATION,
            "bypass_iteration": BYPASS_ITERATION,
            "determinant_before_approach": pre_det,
            "determinant_at_turn": determinant_x(x_turn),
            "determinant_after_bypass": bypass_det,
            "previous_determinant_derivative": old_det_rate,
            "bypass_determinant_derivative": new_det_rate,
            "previous_packet_normalized_derivatives": packet_previous.tolist(),
            "bypass_packet_normalized_derivatives": packet_turn.tolist(),
            "packet_derivative_of_direction_correction": packet_correction.tolist(),
            "fresh_audit_summary": bypass_state.fresh,
        },
        "canonical_exact_nullspace_bypass": {
            "maximum_absolute_packet_jacobian_residual": float(
                np.max(np.abs(nullspace_residual))
            ),
            "approach_determinant_derivative": old_det_rate,
            "nullspace_correction_determinant_derivative": nullspace_det_rate,
            "nullspace_scale": nullspace_scale,
            "bypass_determinant_derivative": exact_det_rate,
            "approach_packet_normalized_derivatives": packet_previous.tolist(),
            "bypass_packet_normalized_derivatives": exact_packet_rates.tolist(),
            "finite_step": exact_step,
            "determinant_before": determinant_x(x_turn),
            "determinant_after": determinant_x(exact_state.x),
            "coordinates": exact_csv,
            "faces": exact_faces_name,
            "audit": exact_audit_name,
        },
    }
    json.dump(atlas_mod.jsonable(wall_record), (HERE / wall_json).open("w"), indent=2)
    print(json.dumps({
        "verdict": wall_record["verdict"],
        "wall_step": wall_h,
        "wall_determinant": wall_det,
        "collinearity_residual": collinearity_residual,
        "chord_parameter": chord_parameter,
        "wall_hull": wall_hull_summary,
        "determinant_sequence": [pre_det, determinant_x(x_turn), bypass_det],
        "determinant_derivatives": [old_det_rate, new_det_rate],
        "packet_correction": packet_correction.tolist(),
        "exact_nullspace": {
            "residual": nullspace_residual.tolist(),
            "scale": nullspace_scale,
            "determinant_derivatives": [old_det_rate, exact_det_rate],
            "finite_step": exact_step,
            "determinant_after": determinant_x(exact_state.x),
            "fresh": exact_state.fresh,
            "audit": exact_audit_name,
        },
        "bypass_fresh": bypass_state.fresh,
        "wall": wall_json,
        "canonical_exact_bypass_audit": exact_audit_name,
    }, indent=2), flush=True)


if __name__ == "__main__":
    main()
