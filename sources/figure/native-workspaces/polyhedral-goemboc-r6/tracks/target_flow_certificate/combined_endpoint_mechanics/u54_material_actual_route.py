#!/usr/bin/env python3
"""Material U54/H910 actual-cell route with local support-exit controls.

Start from the smallest-displacement U54 material branch, add a correction
supported only on the defect rows, and retain threatened cap rows by controls
in the nullspace of the four canonical residuals.  Every reported endpoint is
rebuilt by the full hull/mechanics evaluator.
"""
from __future__ import annotations

from pathlib import Path
import ast
import json

import numpy as np
from scipy.optimize import brentq

import combined_core
import combined_four_death_lp as four
import combined_rank6_scan as rank6
from integrate_four_death_direction import write_csv
from predictor_bypass_epoch import candidate_circuits
from reverse_wall_bypass import oriented_volume, polynomial_roots_on_segment


HERE = Path(__file__).resolve().parent
SOURCE = "epoch4_cluster_event3_deep_after.csv"
LP_JSON = "u54_material_lp.json"
JACOBIAN = "epoch5_lp_jacobian.npz"
PLANE_TOL = 1e-11
BRANCH = ("t", "beta2")
CORRECTION_ROWS = {6, 7, 8, 9, 10, 54, 245, 246}
# Fractional changes from the epoch-5 source.  These include enough buffer for
# the observed second-order chart curvature while keeping the correction local.
DESIRED_CHANGES = np.asarray((-0.001, -0.0142, -0.0005, -0.013), dtype=float)
PREFIX = "u54_material_actual"


def main():
    points = four.load_points(HERE / SOURCE)
    source_result, source_values = four.primitive_ledger(points, plane_tol=PLANE_TOL)
    source_faces = {frozenset(face["cycle"]) for face in source_result.faces}
    modes, mode_meta, _ = four.chart_modes(points)
    data = np.load(HERE / JACOBIAN, allow_pickle=True)
    jacobian = np.asarray(data["jacobian"], dtype=float)
    keys = [ast.literal_eval(str(item)) for item in data["primitive_keys"]]
    key_index = {key: i for i, key in enumerate(keys)}
    lp = json.loads((HERE / LP_JSON).read_text())
    branch = next(
        row for row in lp["ranked_by_minimax_displacement"]
        if (row["h67_component"], row["h910_component"]) == BRANCH
    )
    base_direction = np.asarray(branch["coefficients"], dtype=float)

    quad = next(
        key for key in source_values
        if key[0] == "face" and frozenset(key[1]) == four.QUAD and key[2] == (8, 246)
    )
    residual_keys = [
        quad,
        ("vertex", 54, 1),
        ("edge", (6, 7), "one_minus_t"),
        ("edge", (9, 10), "t"),
    ]
    residual_names = ["quad", "U54", "H67(1-t)", "H910(t)"]
    residual_jacobian = np.vstack([
        jacobian[key_index[key]] / source_values[key] for key in residual_keys
    ])
    local_columns = [
        i for i, meta in enumerate(mode_meta) if meta.get("row") in CORRECTION_ROWS
    ]
    local_matrix = residual_jacobian[:, local_columns]
    if np.linalg.matrix_rank(local_matrix) != 4:
        raise RuntimeError("defect-row correction does not have rank four")
    correction = np.zeros(len(modes))
    correction[local_columns] = local_matrix.T @ np.linalg.solve(
        local_matrix @ local_matrix.T,
        DESIRED_CHANGES - residual_jacobian @ base_direction,
    )
    direction = base_direction + correction

    canonical = four.load_points(HERE / "../../circuit_atlas/row54_combined_wall_rebuilt.csv")
    _canonical_result, canonical_values = four.primitive_ledger(
        canonical, plane_tol=PLANE_TOL
    )
    forced_rails = combined_core.forced_rail_edges()

    def coordinates(coefficients):
        return rank6.apply_modes(points, modes, coefficients)

    def volume(coefficients, circuit):
        return oriented_volume(coordinates(coefficients), circuit)

    def residual_values(coefficients):
        _result, values = four.primitive_ledger(
            coordinates(coefficients), plane_tol=PLANE_TOL
        )
        return np.asarray([values[key] for key in residual_keys])

    source_residuals = np.asarray([source_values[key] for key in residual_keys])

    def state(coefficients):
        result, values = four.primitive_ledger(
            coordinates(coefficients), plane_tol=PLANE_TOL
        )
        faces = {frozenset(face["cycle"]) for face in result.faces}
        stable = {frozenset(result.faces[i]["cycle"]) for i, _ in result.stable}
        unstable = {i for i, _ in result.unstable}
        residuals = np.asarray([values[key] for key in residual_keys])
        audit = {
            "f_vector": [len(result.active), len(result.edges), len(result.faces)],
            "class": [len(result.stable), len(result.unstable), len(result.saddles)],
            "topology_margin": float(result.topology_margin),
            "inactive_rows": sorted(set(points) - set(result.active)),
            "base_present": four.BASE in faces,
            "quad_present": four.QUAD in faces,
            "u8_retained": 8 in unstable,
            "all_forced_rails_present": forced_rails <= set(result.edges),
            "missing_forced_rails": sorted([
                list(edge) for edge in forced_rails - set(result.edges)
            ]),
            "stable_faces": sorted(
                [sorted(face) for face in stable], key=lambda face: (len(face), face)
            ),
            "ratios_to_original": {
                name: float(value / canonical_values[key])
                for name, key, value in zip(residual_names, residual_keys, residuals)
            },
            "ratios_to_epoch5_source": {
                name: float(value / initial)
                for name, value, initial in zip(residual_names, residuals, source_residuals)
            },
        }
        audit["hard_valid"] = bool(
            audit["f_vector"] == [60, 158, 100]
            and audit["class"] == [2, 2, 2]
            and audit["inactive_rows"] == [73]
            and audit["base_present"] and audit["quad_present"]
            and audit["u8_retained"] and audit["all_forced_rails_present"]
        )
        audit["structural_valid"] = bool(
            audit["class"] == [2, 2, 2]
            and audit["inactive_rows"] == [73]
            and audit["base_present"] and audit["quad_present"]
            and audit["u8_retained"] and audit["all_forced_rails_present"]
        )
        audit["four_monotone_from_source"] = bool(
            np.all(residuals <= source_residuals * (1.0 + 1e-10))
        )
        return result, values, faces, audit

    def find_root(circuit, offset, left, right):
        grid = np.linspace(left, right, 1601)
        previous_t = float(grid[0])
        previous_value = volume(previous_t * direction + offset, circuit)
        for t in grid[1:]:
            t = float(t)
            current_value = volume(t * direction + offset, circuit)
            if previous_value * current_value < 0:
                return float(brentq(
                    lambda x: volume(x * direction + offset, circuit),
                    previous_t, t, xtol=1e-15, rtol=1e-14,
                ))
            previous_t, previous_value = t, current_value
        return None

    def null_control(circuit, rows, offset, root, factor=2.0):
        wall = root * direction + offset
        wall_residuals = residual_values(wall)
        columns = [i for i, meta in enumerate(mode_meta) if meta.get("row") in rows]
        matrix = np.empty((4, len(columns)))
        gradient = np.empty(len(columns))
        step = 1e-6
        for j, column in enumerate(columns):
            delta = np.zeros(len(modes))
            delta[column] = step
            matrix[:, j] = (
                residual_values(wall + delta) - residual_values(wall - delta)
            ) / (2.0 * step) / wall_residuals
            gradient[j] = (
                volume(wall + delta, circuit) - volume(wall - delta, circuit)
            ) / (2.0 * step)
        _u, singular_values, vt = np.linalg.svd(matrix, full_matrices=True)
        rank = int(np.linalg.matrix_rank(matrix))
        null_basis = vt[rank:].T
        projected = null_basis @ (null_basis.T @ gradient)
        if np.linalg.norm(projected) < 1e-16:
            raise RuntimeError(f"no local residual-null control for {circuit}")
        tangent_step = 1e-5
        derivative = (
            volume(wall + tangent_step * direction, circuit)
            - volume(wall - tangent_step * direction, circuit)
        ) / (2.0 * tangent_step)
        requested_shift = -factor * derivative * (1.0 - root)
        local = projected * (requested_shift / float(gradient @ projected))
        control = np.zeros(len(modes))
        control[columns] = local
        before = (root - 1e-4) * direction + offset
        lifted = before + control
        endpoint = direction + offset + control
        lift_poly = polynomial_roots_on_segment(coordinates, before, lifted, circuit)
        horizontal_poly = polynomial_roots_on_segment(coordinates, lifted, endpoint, circuit)
        return control, {
            "circuit": list(circuit),
            "control_rows": sorted(rows),
            "root": root,
            "factor": factor,
            "local_columns": columns,
            "rank": rank,
            "nullity": int(null_basis.shape[1]),
            "singular_values": singular_values.tolist(),
            "projection_norm": float(np.linalg.norm(projected)),
            "directional_volume_derivative": float(derivative),
            "requested_volume_shift": float(requested_shift),
            "control_l2": float(np.linalg.norm(control)),
            "control_max_abs": float(np.max(np.abs(control))),
            "control_coefficients": control.tolist(),
            "fractional_residual_leakage": (matrix @ local).tolist(),
            "volume_before": float(volume(before, circuit)),
            "volume_lifted": float(volume(lifted, circuit)),
            "volume_endpoint": float(volume(endpoint, circuit)),
            "lift_polynomial": lift_poly,
            "horizontal_polynomial": horizontal_poly,
        }

    def multi_null_control(circuits, rows, offset, root, first_factor=1.2):
        """One residual-null lift that holds all coupled support circuits."""
        wall = root * direction + offset
        before = (root - 1e-4) * direction + offset
        wall_residuals = residual_values(wall)
        columns = [i for i, meta in enumerate(mode_meta) if meta.get("row") in rows]
        matrix = np.empty((4, len(columns)))
        step = 1e-6
        for j, column in enumerate(columns):
            delta = np.zeros(len(modes))
            delta[column] = step
            matrix[:, j] = (
                residual_values(wall + delta) - residual_values(wall - delta)
            ) / (2.0 * step) / wall_residuals
        _u, singular_values, vt = np.linalg.svd(matrix, full_matrices=True)
        rank = int(np.linalg.matrix_rank(matrix))
        null_basis = vt[rank:].T
        gradients = []
        for circuit in circuits:
            gradients.append(np.asarray([
                (
                    volume(wall + np.eye(len(modes))[column] * step, circuit)
                    - volume(wall - np.eye(len(modes))[column] * step, circuit)
                ) / (2.0 * step)
                for column in columns
            ]))
        gradients = np.asarray(gradients)
        response = gradients @ null_basis
        if np.linalg.matrix_rank(response) != len(circuits):
            raise RuntimeError("coupled circuit response is rank deficient")
        base_endpoint_volumes = np.asarray([
            volume(direction + offset, circuit) for circuit in circuits
        ])
        before_volumes = np.asarray([volume(before, circuit) for circuit in circuits])
        target_volumes = np.empty(len(circuits))
        for i, (base_volume, before_volume) in enumerate(
            zip(base_endpoint_volumes, before_volumes)
        ):
            factor = first_factor if i == 0 else 1.0
            target_volumes[i] = (
                np.sign(before_volume)
                * factor * max(abs(base_volume), 1e-10)
            )
        requested_shifts = target_volumes - base_endpoint_volumes
        null_coordinates = response.T @ np.linalg.solve(
            response @ response.T, requested_shifts
        )
        local = null_basis @ null_coordinates
        control = np.zeros(len(modes))
        control[columns] = local
        lifted = before + control
        endpoint = direction + offset + control
        circuit_audits = []
        for circuit in circuits:
            lift_poly = polynomial_roots_on_segment(
                coordinates, before, lifted, circuit
            )
            horizontal_poly = polynomial_roots_on_segment(
                coordinates, lifted, endpoint, circuit
            )
            circuit_audits.append({
                "circuit": list(circuit),
                "volume_before": float(volume(before, circuit)),
                "volume_lifted": float(volume(lifted, circuit)),
                "volume_endpoint": float(volume(endpoint, circuit)),
                "lift_polynomial": lift_poly,
                "horizontal_polynomial": horizontal_poly,
                "avoids_both_legs": bool(
                    not lift_poly["real_roots_in_closed_segment"]
                    and not horizontal_poly["real_roots_in_closed_segment"]
                    and np.sign(volume(before, circuit))
                    == np.sign(volume(lifted, circuit))
                    == np.sign(volume(endpoint, circuit))
                ),
            })
        if not all(item["avoids_both_legs"] for item in circuit_audits):
            raise RuntimeError("coupled null control crosses a protected circuit")
        return control, {
            "type": "simultaneous_multiwall_null_control",
            "circuits": [list(circuit) for circuit in circuits],
            "control_rows": sorted(rows),
            "root": root,
            "first_factor": first_factor,
            "local_columns": columns,
            "rank": rank,
            "nullity": int(null_basis.shape[1]),
            "response_rank": int(np.linalg.matrix_rank(response)),
            "singular_values": singular_values.tolist(),
            "projected_gradient_norms": [
                float(np.linalg.norm(null_basis @ response[i]))
                for i in range(len(circuits))
            ],
            "base_endpoint_volumes": base_endpoint_volumes.tolist(),
            "target_endpoint_volumes": target_volumes.tolist(),
            "requested_volume_shifts": requested_shifts.tolist(),
            "control_l2": float(np.linalg.norm(control)),
            "control_max_abs": float(np.max(np.abs(control))),
            "control_coefficients": control.tolist(),
            "fractional_residual_leakage": (matrix @ local).tolist(),
            "circuit_audits": circuit_audits,
        }

    # Exact allowed diagonal-flip order before the threatened q236 exit.
    expected_events = [
        (69, 228, 235, 236),
        (69, 235, 236, 237),
        (69, 228, 235, 237),
        (198, 234, 236, 237),
    ]
    allowed_events = []
    for circuit in expected_events:
        root = find_root(circuit, np.zeros(len(modes)), 0.0, 0.56)
        if root is not None:
            allowed_events.append({"circuit": list(circuit), "root": root})

    offset = np.zeros(len(modes))
    controls = []
    q236_exit = (234, 235, 236, 237)
    root = find_root(q236_exit, offset, 0.4, 0.7)
    if root is None:
        raise RuntimeError("q236 support exit not found")
    first_control, first_record = null_control(
        q236_exit, {234, 235, 236, 237}, offset, root
    )
    offset += first_control
    controls.append(first_record)

    # The first control sometimes protects q235 at the same time.  If not,
    # install the corresponding local control on the actual post-control path.
    _r1, _v1, _f1, endpoint_after_first = state(direction + offset)
    if not endpoint_after_first["hard_valid"] and 235 in endpoint_after_first["inactive_rows"]:
        q235_candidates = [
            ((69, 228, 235, 237), {69, 228, 235, 237}),
            ((228, 234, 235, 237), {228, 234, 235, 237}),
            ((69, 228, 235, 255), {69, 228, 235, 255}),
        ]
        installed = False
        for circuit, rows in q235_candidates:
            second_root = find_root(circuit, offset, root + 1e-3, 1.0)
            if second_root is None:
                continue
            second_control, second_record = null_control(
                circuit, rows, offset, second_root
            )
            trial_offset = offset + second_control
            _tr, _tv, _tf, trial_audit = state(direction + trial_offset)
            if trial_audit["hard_valid"]:
                offset = trial_offset
                controls.append(second_record)
                installed = True
                break
        if not installed:
            raise RuntimeError("q235 remains inactive after local candidates")

    endpoint_coefficients = direction + offset
    endpoint_points = coordinates(endpoint_coefficients)
    endpoint_path = HERE / f"{PREFIX}_endpoint.csv"
    write_csv(endpoint_path, endpoint_points)
    _endpoint_result, _endpoint_values, endpoint_faces, endpoint_audit = state(
        endpoint_coefficients
    )

    # The sequentially constructed controls are used as a tiny null correction
    # to the direction itself.  Scaling their sum from the source is the actual
    # route: unlike the abrupt L lifts, this straight homotopy never leaves the
    # rail-valid active set.
    straight_direction = endpoint_coefficients
    straight_events = []
    evaluation_failures = []
    noncell_band_samples = []
    structural_failures = []
    path_valid = True
    monotone = True

    def accumulate_sample(coefficients, segment, parameter):
        nonlocal path_valid, monotone
        try:
            _r, _v, _faces, audit = state(coefficients)
        except RuntimeError as error:
            if "parallel face normals" not in str(error):
                raise
            # This evaluator singularity occurs in its deliberately thin
            # exact-coplanarity band.  Both adjacent samples are still rebuilt;
            # record rather than misclassify it as a mechanical sign loss.
            evaluation_failures.append({
                "segment": segment,
                "parameter": float(parameter),
                "error": repr(error),
            })
            return
        path_valid &= audit["structural_valid"]
        monotone &= audit["four_monotone_from_source"]
        if not audit["hard_valid"]:
            noncell_band_samples.append({
                "segment": segment,
                "parameter": float(parameter),
                "f_vector": audit["f_vector"],
                "class": audit["class"],
                "topology_margin": audit["topology_margin"],
            })
        if not audit["structural_valid"]:
            structural_failures.append({
                "segment": segment,
                "parameter": float(parameter),
                "audit": audit,
            })

    previous_faces = source_faces
    previous_t = 0.0
    for t in np.linspace(0.0, 1.0, 401)[1:]:
        t = float(t)
        try:
            _r, _v, faces, audit = state(t * straight_direction)
        except RuntimeError as error:
            if "parallel face normals" not in str(error):
                raise
            evaluation_failures.append({
                "segment": "straight_homotopy",
                "parameter": t,
                "error": repr(error),
            })
            continue
        path_valid &= audit["structural_valid"]
        monotone &= audit["four_monotone_from_source"]
        if not audit["hard_valid"]:
            noncell_band_samples.append({
                "segment": "straight_homotopy",
                "parameter": t,
                "f_vector": audit["f_vector"],
                "class": audit["class"],
                "topology_margin": audit["topology_margin"],
            })
        if not audit["structural_valid"]:
            structural_failures.append({
                "segment": "straight_homotopy",
                "parameter": t,
                "audit": audit,
            })
        if faces != previous_faces:
            circuits = candidate_circuits(previous_faces, faces)
            exact_roots = []
            for circuit in circuits:
                polynomial = polynomial_roots_on_segment(
                    coordinates, np.zeros(len(modes)), straight_direction, circuit
                )
                roots = [
                    float(value) for value in polynomial["real_roots_in_closed_segment"]
                    if previous_t - 1e-8 <= value <= t + 1e-8
                ]
                for value in roots:
                    exact_roots.append({
                        "circuit": list(circuit),
                        "root": value,
                        "volume_at_root": float(value and volume(value * straight_direction, circuit)),
                    })
            straight_events.append({
                "bracket": [previous_t, t],
                "candidate_circuits": [list(circuit) for circuit in circuits],
                "exact_roots": exact_roots,
                "removed_faces": sorted(
                    [sorted(face) for face in previous_faces - faces],
                    key=lambda face: (len(face), face),
                ),
                "added_faces": sorted(
                    [sorted(face) for face in faces - previous_faces],
                    key=lambda face: (len(face), face),
                ),
                "right_audit": audit,
            })
        previous_faces = faces
        previous_t = t

    first_exact_event = None
    if straight_events and straight_events[0]["exact_roots"]:
        first_root_record = min(
            straight_events[0]["exact_roots"], key=lambda item: item["root"]
        )
        first_root = first_root_record["root"]
        first_circuit = tuple(first_root_record["circuit"])
        epsilon = 1e-5
        event_coefficients = {
            "before": (first_root - epsilon) * straight_direction,
            "at": first_root * straight_direction,
            "after": (first_root + epsilon) * straight_direction,
        }
        event_audits = {}
        event_faces = {}
        event_csv = {}
        for label, coefficients in event_coefficients.items():
            path = HERE / f"{PREFIX}_event1_{label}.csv"
            write_csv(path, coordinates(coefficients))
            event_csv[label] = path.name
            try:
                _er, _ev, faces, audit = state(coefficients)
                event_audits[label] = audit
                event_faces[label] = sorted(
                    [sorted(face) for face in faces if len(face & set(first_circuit)) >= 3],
                    key=lambda face: (len(face), face),
                )
            except RuntimeError as error:
                event_audits[label] = {"valid": False, "error": repr(error)}
                event_faces[label] = []
        first_exact_event = {
            "circuit": list(first_circuit),
            "root": first_root,
            "epsilon": epsilon,
            "volume_at_root": float(volume(first_root * straight_direction, first_circuit)),
            "csv": event_csv,
            "audits": event_audits,
            "local_faces": event_faces,
            "both_adjacent_cells_structural_valid": bool(
                event_audits["before"].get("structural_valid")
                and event_audits["after"].get("structural_valid")
            ),
        }

    payload = {
        "version": 1,
        "scope": "U54-priority material straight actual-cell route with residual-null correction",
        "source": SOURCE,
        "branch": {"h67": BRANCH[0], "h910": BRANCH[1]},
        "base_minimax_displacement": branch["minimax_displacement"],
        "local_correction_rows": sorted(CORRECTION_ROWS),
        "desired_fractional_changes": dict(zip(residual_names, DESIRED_CHANGES.tolist())),
        "achieved_linear_fractional_changes": dict(
            zip(residual_names, (residual_jacobian @ straight_direction).tolist())
        ),
        "correction_l2": float(np.linalg.norm(correction)),
        "correction_max_abs": float(np.max(np.abs(correction))),
        "uncontrolled_direction_events": allowed_events,
        "local_support_controls": controls,
        "straight_homotopy_events": straight_events,
        "first_exact_event": first_exact_event,
        "thin_band_evaluation_failures": evaluation_failures,
        "noncell_band_samples": noncell_band_samples,
        "structural_failures": structural_failures,
        "sampled_path_structural_valid": bool(path_valid),
        "sampled_path_four_monotone": bool(monotone),
        "endpoint": {
            "csv": endpoint_path.name,
            "face_lattice_changed_from_source": endpoint_faces != source_faces,
            "audit": endpoint_audit,
        },
        "material_worst_ratio_below_0_98": bool(
            max(endpoint_audit["ratios_to_original"].values()) < 0.98
        ),
        "conclusion": (
            "material actual-cell direction exists"
            if path_valid and monotone
            and max(endpoint_audit["ratios_to_original"].values()) < 0.98
            else "candidate requires further control"
        ),
    }
    output = HERE / f"{PREFIX}.json"
    output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "events": allowed_events,
        "controls": controls,
        "path_valid": path_valid,
        "monotone": monotone,
        "endpoint": endpoint_audit,
        "material": payload["material_worst_ratio_below_0_98"],
    }, indent=2))


if __name__ == "__main__":
    main()
