#!/usr/bin/env python3
"""First actual wall after the exact row-15 nullspace bypass.

Starting at ``row54_row15_exact_nullspace_bypass_audit.json``, solve a
full-44 LP which keeps the six packet derivatives fixed, keeps every nearby
or previously promoted guard inward, and maximizes the inward derivative of
the row-15 circuit determinant.  The resulting ray leaves the row-15 wall
decisively and first meets the clean support circuit {12,13,261,262}.

The script localizes the common determinant zero, materializes the maximal
quad at the wall, and audits a strict point in the adjacent triangulation.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np
from scipy.optimize import brentq, linprog

import row54_four_residual_search as core
import row54_guarded_escape as guarded
import row54_shared_root_active_set as active_mod
import row54_shared_root_atlas as atlas_mod
import row54_transverse_actual_continuation as continuation_mod


HERE = Path(__file__).resolve().parent
START_AUDIT = HERE / "row54_row15_exact_nullspace_bypass_audit.json"
ACTIVE_SET = HERE / "row54_shared_root_active_set_svd.json"
ROW15_CIRCUIT = (14, 15, 16, 72)
FLIP_CIRCUIT = (12, 13, 261, 262)
VALID_STEP = 0.002
FAR_STEP = 0.0025
CONTROL_RADIUS = 0.5
FD_STEP = 8e-6


def write_csv(path, ids, points):
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(("source_id", "x", "y", "z"))
        for i, p in zip(ids, points):
            w.writerow([i, *[format(float(v), ".17g") for v in p]])


def circuit_determinant(atlas, x, circuit):
    points, den = atlas.problem.chart.coordinates(np.asarray(x))
    if points is None:
        raise ValueError(float(np.min(den)))
    ix = atlas.problem.chart.ix
    a, b, c, d = (points[ix[k]] for k in circuit)
    return float(np.dot(np.cross(b - a, c - a), d - a))


def circuit_gradient(atlas, x, circuit, step=1e-6):
    eye = np.eye(len(x))
    return np.asarray([
        (circuit_determinant(atlas, x + step * eye[k], circuit)
         - circuit_determinant(atlas, x - step * eye[k], circuit))
        / (2.0 * step)
        for k in range(len(x))
    ])


def d_inward_direction(atlas, x):
    solver = active_mod.ActiveSet(atlas, 32, FD_STEP)
    active_record = json.load(ACTIVE_SET.open())
    equations = continuation_mod.load_equations(active_record)
    _, _, guards, topology, _ = atlas.problem.evaluate(x)
    jm, jt = atlas.finite_full(x)

    aeq, beq = [], []
    cone_rows, cone_scales, cone_labels = [], [], []
    seen = set()
    for eq in equations:
        row = jm[eq.index] if eq.kind == "mechanics" else jt[eq.index]
        if eq.key[0] == "packet":
            aeq.append(row / eq.scale)
            pos = solver.critical_indices.index(eq.index)
            beq.append(-atlas.active_g0[pos] / eq.scale)
        else:
            cone_rows.append(row)
            cone_scales.append(eq.scale)
            cone_labels.append((eq.kind, eq.index, eq.key))
            seen.add((eq.kind, eq.index))

    for k in np.flatnonzero(atlas.noncritical):
        if guards[k] < 1e-7 and ("mechanics", int(k)) not in seen:
            cone_rows.append(jm[k])
            cone_scales.append(max(abs(guards[k]), 1e-4))
            cone_labels.append(("mechanics", int(k), atlas.problem.mech_labels[k]))
            seen.add(("mechanics", int(k)))
    for k, value in enumerate(topology):
        if value < 1e-8 and ("topology", k) not in seen:
            cone_rows.append(jt[k])
            cone_scales.append(max(abs(value), 1e-7))
            cone_labels.append(("topology", k, atlas.problem.top_labels[k]))
            seen.add(("topology", k))

    cone_rows = np.asarray(cone_rows)
    cone_scales = np.asarray(cone_scales)
    determinant_gradient = circuit_gradient(atlas, x, ROW15_CIRCUIT)
    lp = linprog(
        -determinant_gradient,
        A_ub=-cone_rows / cone_scales[:, None],
        b_ub=np.zeros(len(cone_rows)),
        A_eq=np.asarray(aeq),
        b_eq=np.asarray(beq),
        bounds=[(-CONTROL_RADIUS, CONTROL_RADIUS)] * len(x),
        method="highs",
    )
    if not lp.success:
        raise RuntimeError(lp.message)
    direction = lp.x
    normalized_cone_rates = cone_rows @ direction / cone_scales
    return direction, {
        "success": bool(lp.success),
        "message": str(lp.message),
        "control_radius": CONTROL_RADIUS,
        "maximum_absolute_control_rate": float(np.max(np.abs(direction))),
        "row15_determinant_derivative": float(determinant_gradient @ direction),
        "packet_normalized_derivatives": (
            jm[atlas.active] @ direction / atlas.active_scales
        ).tolist(),
        "minimum_normalized_preserved_guard_derivative": float(
            np.min(normalized_cone_rates)
        ),
        "weakest_preserved_guards": [
            {
                "normalized_derivative": float(normalized_cone_rates[k]),
                "constraint": cone_labels[int(k)],
            }
            for k in np.argsort(normalized_cone_rates)[:20]
        ],
        "direction": direction.tolist(),
    }


def adjacent_audit_atlas(reference_atlas, faces, seed_x):
    """Build an audit-only atlas when the immutable raw source is pre-flip.

    ``guarded.Problem`` normally rejects a face lattice which is not already
    valid at its immutable raw source.  Here the new clean flip is created by
    the 36 base controls, so the raw source is intentionally on the old side.
    The chart and all evaluation routines remain unchanged; only that
    constructor-time source-side assertion is bypassed.  The six packet rows
    are selected freshly at the strict adjacent-cell seed.
    """
    problem = object.__new__(guarded.Problem)
    problem.ids = reference_atlas.ids
    problem.source = reference_atlas.source_points
    problem.faces = faces
    problem.chart = guarded.Chart(problem.ids, problem.source)
    problem.forced = guarded.forced_rail_edges()
    p0, _ = problem.chart.coordinates(np.zeros(44))
    m0 = core.mechanics(problem.ids, p0, faces)
    problem.g0, problem.mech_labels = core.signed_guards(m0, faces, "escape")
    problem.top0, problem.top_labels = guarded.topology_guards(
        problem.ids, p0, faces
    )
    problem.guard_scales = np.maximum(0.03, np.abs(problem.g0))
    problem.top_scales = np.maximum(1e-7, np.abs(problem.top0))
    problem.critical = np.zeros(len(problem.g0), dtype=bool)

    audit_atlas = object.__new__(atlas_mod.Atlas)
    audit_atlas.ids = list(reference_atlas.ids)
    audit_atlas.source_points = reference_atlas.source_points
    audit_atlas.expected_faces = faces
    audit_atlas.problem = problem
    audit_atlas.start_record = reference_atlas.start_record
    audit_atlas.x0 = reference_atlas.x0.copy()
    _, _, seed_guards, _, _ = problem.evaluate(seed_x)
    audit_atlas.g0 = problem.g0
    audit_atlas.top0 = problem.top0
    audit_atlas.active = seed_guards < 0.0
    if int(np.sum(audit_atlas.active)) != 6:
        packet = [
            (float(seed_guards[k]), problem.mech_labels[k])
            for k in np.flatnonzero(seed_guards < 0.0)
        ]
        raise AssertionError(("adjacent cell is not rank-six", packet))
    audit_atlas.noncritical = ~audit_atlas.active
    audit_atlas.active_g0 = seed_guards[audit_atlas.active]
    audit_atlas.active_scales = np.maximum(
        np.abs(audit_atlas.active_g0), 2.5e-4
    )
    audit_atlas.fd_step = FD_STEP
    return audit_atlas


def main():
    atlas = atlas_mod.Atlas(atlas_mod.DEFAULT_SOURCE, atlas_mod.DEFAULT_FACES,
                            atlas_mod.DEFAULT_START, FD_STEP)
    start_record = json.load(START_AUDIT.open())
    x0 = np.asarray(start_record["parameters"], dtype=float)
    p0, d0, g0, t0, _ = atlas.problem.evaluate(x0)
    start_state = atlas.make_state(0.0, x0 - atlas.x0, x0, p0, d0, g0, t0)
    if not start_state.valid:
        raise AssertionError(start_state.invalid_reasons)

    direction, lp_record = d_inward_direction(atlas, x0)
    row15_start = circuit_determinant(atlas, x0, ROW15_CIRCUIT)
    if lp_record["row15_determinant_derivative"] <= 0.0:
        raise AssertionError(lp_record["row15_determinant_derivative"])

    def flip_det_h(h):
        return circuit_determinant(atlas, x0 + h * direction, FLIP_CIRCUIT)

    valid_x = x0 + VALID_STEP * direction
    far_x = x0 + FAR_STEP * direction
    vp, vd, vg, vt, _ = atlas.problem.evaluate(valid_x)
    valid_state = atlas.make_state(0.0, valid_x - atlas.x0, valid_x,
                                   vp, vd, vg, vt)
    fp, fd, fg, ft, _ = atlas.problem.evaluate(far_x)
    far_old_state = atlas.make_state(0.0, far_x - atlas.x0, far_x,
                                     fp, fd, fg, ft)
    if not valid_state.valid:
        raise AssertionError(valid_state.invalid_reasons)
    if flip_det_h(VALID_STEP) * flip_det_h(FAR_STEP) >= 0.0:
        raise AssertionError((flip_det_h(VALID_STEP), flip_det_h(FAR_STEP)))

    wall_step = brentq(flip_det_h, VALID_STEP, FAR_STEP,
                       xtol=5e-16, rtol=4 * np.finfo(float).eps)
    wall_x = x0 + wall_step * direction
    wall_points, wall_den, wall_guards, wall_top, _ = atlas.problem.evaluate(wall_x)
    wall_det = flip_det_h(wall_step)
    wall_hull, wall_faces, _ = core.group_maximal_faces(atlas.ids, wall_points)
    wall_edges, _ = core.edge_lattice(wall_faces)
    wall_face_sets = {frozenset(face) for face in wall_faces}
    if frozenset(FLIP_CIRCUIT) not in wall_face_sets:
        raise AssertionError("wall quad was not grouped")
    if [len(wall_hull.vertices), len(wall_edges), len(wall_faces)] != [61, 161, 102]:
        raise AssertionError((len(wall_hull.vertices), len(wall_edges), len(wall_faces)))

    old_face_sets = {frozenset(face) for face in valid_state.fresh_faces}
    far_face_sets = {frozenset(face) for face in far_old_state.fresh_faces}
    removed_faces = sorted(
        (sorted(face) for face in old_face_sets - far_face_sets),
        key=tuple,
    )
    added_faces = sorted(
        (sorted(face) for face in far_face_sets - old_face_sets),
        key=tuple,
    )
    expected_removed = [[12, 13, 262], [13, 261, 262]]
    expected_added = [[12, 13, 261], [12, 261, 262]]
    if removed_faces != expected_removed or added_faces != expected_added:
        raise AssertionError((removed_faces, added_faces))

    far_faces_name = "row54_post_row15_clean_flip_faces.json"
    far_faces_path = HERE / far_faces_name
    json.dump(far_old_state.fresh_faces, far_faces_path.open("w"), indent=2)
    adjacent = adjacent_audit_atlas(atlas, far_old_state.fresh_faces, far_x)
    ap, ad, ag, at, _ = adjacent.problem.evaluate(far_x)
    far_state = adjacent.make_state(0.0, far_x - adjacent.x0, far_x,
                                    ap, ad, ag, at)
    if not far_state.valid:
        raise AssertionError(far_state.invalid_reasons)
    far_edges, _ = core.edge_lattice(far_state.fresh_faces)
    required = {
        "old_fixed_flip_new_diagonal_3_88": (3, 88) in far_edges,
        "old_fixed_flip_old_diagonal_2_242_absent": (2, 242) not in far_edges,
        "new_diagonal_12_261": (12, 261) in far_edges,
        "old_diagonal_13_262_absent": (13, 262) not in far_edges,
        "all_61_rows_active": far_state.fresh.get("all_61_rows_active"),
        "enlarged_base_present": far_state.fresh.get("enlarged_base_present"),
        "enlarged_base_stable": far_state.fresh.get("enlarged_base_stable"),
        "U8_unstable": far_state.fresh.get("U8_unstable"),
        "all_forced_rail_edges_present": far_state.fresh.get(
            "all_forced_rail_edges_present"
        ),
    }
    if not all(required.values()):
        raise AssertionError(required)

    common_rows = []
    flip_start = circuit_determinant(atlas, x0, FLIP_CIRCUIT)
    for k, label in enumerate(atlas.problem.top_labels):
        circuit = tuple(sorted(set(label[2]) | {label[3]}))
        if label[0] == "support" and circuit == FLIP_CIRCUIT:
            common_rows.append({
                "guard_index": k,
                "label": label,
                "start": float(t0[k]),
                "start_guard_over_common_determinant": float(t0[k] / flip_start),
                "wall": float(wall_top[k]),
                "far_old_cell_value": float(ft[k]),
            })
    if len(common_rows) != 2:
        raise AssertionError(common_rows)

    wall_csv = "row54_post_row15_clean_flip_exact_wall.csv"
    wall_faces_name = "row54_post_row15_clean_flip_exact_wall_faces.json"
    wall_json = "row54_post_row15_clean_flip_exact_wall.json"
    far_csv = "row54_post_row15_clean_flip.csv"
    far_audit_name = "row54_post_row15_clean_flip_audit.json"
    write_csv(HERE / wall_csv, atlas.ids, wall_points)
    json.dump(wall_faces, (HERE / wall_faces_name).open("w"), indent=2)
    write_csv(HERE / far_csv, atlas.ids, far_state.points)

    far_audit, audited_faces = adjacent.complete_audit(
        far_state, "row54_post_row15_clean_flip",
        certificate={
            "source_endpoint": START_AUDIT.name,
            "wall_certificate": wall_json,
            "row15_circuit_guard": {
                "circuit": list(ROW15_CIRCUIT),
                "determinant_start": row15_start,
                "determinant_far": circuit_determinant(
                    atlas, far_x, ROW15_CIRCUIT
                ),
            },
            "full44_D_inward_LP": lp_record,
            "clean_flip": {
                "circuit": list(FLIP_CIRCUIT),
                "old_diagonal": [13, 262],
                "new_diagonal": [12, 261],
                "removed_faces": removed_faces,
                "added_faces": added_faces,
            },
            "required_invariants": required,
        },
    )
    if {frozenset(face) for face in audited_faces} != far_face_sets:
        raise AssertionError("adjacent audit faces changed")
    far_audit.update({
        "coordinates": far_csv,
        "fixed_expected_faces": far_faces_name,
        "wall_certificate": wall_json,
        "packet_at_far_cell": [
            {
                "value": float(ag[k]),
                "feature": adjacent.problem.mech_labels[k],
            }
            for k in np.flatnonzero(adjacent.active)
        ],
    })
    json.dump(atlas_mod.jsonable(far_audit),
              (HERE / far_audit_name).open("w"), indent=2)

    wall_record = {
        "version": 1,
        "verdict": "CLEAN_TRANSVERSE_SUPPORT_FLIP_AFTER_EXACT_ROW15_BYPASS",
        "source_endpoint": START_AUDIT.name,
        "full44_D_inward_LP": lp_record,
        "row15_circuit": {
            "vertices": list(ROW15_CIRCUIT),
            "common_determinant": (
                "det(p15-p14,p16-p14,p72-p14)"
            ),
            "start": row15_start,
            "valid_side": circuit_determinant(atlas, valid_x, ROW15_CIRCUIT),
            "far_side": circuit_determinant(atlas, far_x, ROW15_CIRCUIT),
        },
        "new_wall": {
            "circuit": list(FLIP_CIRCUIT),
            "common_oriented_determinant": (
                "N=det(p13-p12,p261-p12,p262-p12); both crossed "
                "normalized support guards are N divided by a strictly "
                "positive triangle-area denominator"
            ),
            "common_support_rows": common_rows,
            "valid_step": VALID_STEP,
            "far_step": FAR_STEP,
            "wall_step": wall_step,
            "wall_determinant": wall_det,
            "determinant_valid_side": flip_det_h(VALID_STEP),
            "determinant_far_side": flip_det_h(FAR_STEP),
            "old_diagonal": [13, 262],
            "new_diagonal": [12, 261],
            "removed_faces": removed_faces,
            "added_faces": added_faces,
        },
        "wall": {
            "coordinates": wall_csv,
            "maximal_faces": wall_faces_name,
            "f_vector": [len(wall_hull.vertices), len(wall_edges), len(wall_faces)],
            "quad_present": True,
            "minimum_projective_denominator": float(np.min(wall_den)),
        },
        "strict_adjacent_cell": {
            "coordinates": far_csv,
            "maximal_faces": far_faces_name,
            "audit": far_audit_name,
            "fresh": far_state.fresh,
            "required_invariants": required,
            "packet": far_audit["packet_at_far_cell"],
        },
    }
    json.dump(atlas_mod.jsonable(wall_record),
              (HERE / wall_json).open("w"), indent=2)
    print(json.dumps({
        "verdict": wall_record["verdict"],
        "wall_step": wall_step,
        "wall_determinant": wall_det,
        "wall_f_vector": wall_record["wall"]["f_vector"],
        "row15_determinants": [
            wall_record["row15_circuit"][key]
            for key in ("start", "valid_side", "far_side")
        ],
        "removed_faces": removed_faces,
        "added_faces": added_faces,
        "far_fresh": far_state.fresh,
        "packet": far_audit["packet_at_far_cell"],
        "wall": wall_json,
        "far_audit": far_audit_name,
    }, indent=2), flush=True)


if __name__ == "__main__":
    main()
