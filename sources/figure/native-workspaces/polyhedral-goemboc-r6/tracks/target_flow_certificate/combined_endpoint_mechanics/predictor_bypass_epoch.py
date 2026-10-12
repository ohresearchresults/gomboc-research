#!/usr/bin/env python3
"""Event-driven four-death predictor with local nullspace reverse bypasses.

Each ``--reverse`` specification is ``c0,c1,c2,c3:r0,r1,...``.  The first
part is a known ping-pong circuit and the second part selects local chart rows
used to push that circuit into the four-death Jacobian nullspace.  Controls are
installed sequentially by an L lift before the scalar root and retained while
the main predictor advances.  A dense fresh-hull scan then locates the first
new support event or structural/mechanical failure.
"""
from __future__ import annotations

from pathlib import Path
import argparse
import ast
import json

import numpy as np
from scipy.optimize import brentq

import combined_core
import combined_four_death_lp as four
import combined_rank6_scan as rank6
from integrate_four_death_direction import write_csv
from reverse_wall_bypass import oriented_volume, polynomial_roots_on_segment


HERE = Path(__file__).resolve().parent


def parse_reverse(text):
    circuit_text, rows_text = text.split(":", 1)
    circuit = tuple(int(x) for x in circuit_text.split(","))
    rows = tuple(int(x) for x in rows_text.split(","))
    if len(circuit) != 4:
        raise argparse.ArgumentTypeError("reverse circuit must have four rows")
    return circuit, rows


def circuit_faces(faces, circuit):
    cset = frozenset(circuit)
    return sorted(
        [sorted(face) for face in faces if len(face & cset) >= 3],
        key=lambda face: (len(face), face),
    )


def candidate_circuits(left_faces, right_faces):
    removed = left_faces - right_faces
    added = right_faces - left_faces
    candidates = set()
    removed_triangles = [face for face in removed if len(face) == 3]
    added_triangles = [face for face in added if len(face) == 3]
    for i, first in enumerate(removed_triangles):
        for second in removed_triangles[i + 1:]:
            union = first | second
            if len(union) != 4:
                continue
            if (
                sum(face <= union for face in added_triangles) >= 2
                or union in added
            ):
                candidates.add(tuple(sorted(union)))
    for i, first in enumerate(added_triangles):
        for second in added_triangles[i + 1:]:
            union = first | second
            if len(union) != 4:
                continue
            if (
                sum(face <= union for face in removed_triangles) >= 2
                or union in removed
            ):
                candidates.add(tuple(sorted(union)))
    return sorted(candidates)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--lp-json", required=True)
    parser.add_argument("--prefix", required=True)
    parser.add_argument("--horizon", type=float, default=2e-4)
    parser.add_argument("--scan-points", type=int, default=401)
    parser.add_argument("--fd-step", type=float, default=1e-6)
    parser.add_argument("--plane-tol", type=float, default=1e-11)
    parser.add_argument("--lift-epsilon", type=float, default=1e-6)
    parser.add_argument("--protection-factor", type=float, default=2.0)
    parser.add_argument("--reverse", type=parse_reverse, action="append", default=[])
    args = parser.parse_args()

    source_path = Path(args.source)
    points = four.load_points(source_path)
    source_result, source_values = four.primitive_ledger(points, plane_tol=args.plane_tol)
    source_faces = {frozenset(face["cycle"]) for face in source_result.faces}
    modes, mode_meta, _ = four.chart_modes(points)
    lp = json.loads(Path(args.lp_json).read_text())
    candidates = [
        row for row in lp["atlas"]
        if row.get("success")
        and ast.literal_eval(row["deaths"][2])[2] == "one_minus_t"
        and ast.literal_eval(row["deaths"][3])[2] == "t"
    ]
    if not candidates:
        raise RuntimeError("fixed H67=1-t,H910=t LP branch absent")
    best = min(candidates, key=lambda row: row["delta"])
    direction_x = np.asarray(best["coefficients"], dtype=float)
    death_keys = [ast.literal_eval(key) for key in best["deaths"]]
    canonical = four.load_points(HERE / "../../circuit_atlas/row54_combined_wall_rebuilt.csv")
    _, canonical_values = four.primitive_ledger(canonical, plane_tol=args.plane_tol)
    canonical_deaths = np.asarray([canonical_values[key] for key in death_keys])
    forced_rails = combined_core.forced_rail_edges()

    def coordinates(coefficients):
        return rank6.apply_modes(points, modes, coefficients)

    def mechanics(coefficients):
        return four.primitive_ledger(coordinates(coefficients), plane_tol=args.plane_tol)

    def death_values(coefficients):
        _result, values = mechanics(coefficients)
        return np.asarray([values[key] for key in death_keys])

    def volume(coefficients, circuit):
        return oriented_volume(coordinates(coefficients), circuit)

    def state(coefficients):
        result, values = mechanics(coefficients)
        faces = {frozenset(face["cycle"]) for face in result.faces}
        stable_faces = {
            frozenset(result.faces[index]["cycle"]) for index, _value in result.stable
        }
        unstable = sorted(index for index, _value in result.unstable)
        current_deaths = np.asarray([values[key] for key in death_keys])
        record = {
            "f_vector": [len(result.active), len(result.edges), len(result.faces)],
            "class": [len(result.stable), len(result.unstable), len(result.saddles)],
            "topology_margin": float(result.topology_margin),
            "inactive_rows": sorted(set(points) - set(result.active)),
            "base_present": four.BASE in faces,
            "quad_present": four.QUAD in faces,
            "u8_retained": 8 in unstable,
            "all_forced_rails_present": forced_rails <= set(result.edges),
            "missing_forced_rails": sorted([list(edge) for edge in forced_rails - set(result.edges)]),
            "stable_faces": sorted([sorted(face) for face in stable_faces], key=lambda f: (len(f), f)),
            "unstable_vertices": unstable,
            "saddle_edges": sorted([list(edge) for edge, _value in result.saddles]),
            "death_ratios_to_original": {
                repr(key): float(value / reference)
                for key, value, reference in zip(death_keys, current_deaths, canonical_deaths)
            },
        }
        record["hard_valid"] = bool(
            record["class"] == [2, 2, 2]
            and record["inactive_rows"] == [73]
            and record["base_present"]
            and record["quad_present"]
            and record["u8_retained"]
            and record["all_forced_rails_present"]
        )
        return result, values, faces, record

    def find_first_root(circuit, offset, left, right):
        grid = np.linspace(left, right, 801)
        values = np.asarray([volume(alpha * direction_x + offset, circuit) for alpha in grid])
        for i in range(len(grid) - 1):
            if values[i] == 0:
                return float(grid[i])
            if values[i] * values[i + 1] < 0:
                return float(brentq(
                    lambda alpha: volume(alpha * direction_x + offset, circuit),
                    float(grid[i]), float(grid[i + 1]), xtol=1e-15, rtol=1e-14,
                ))
        raise RuntimeError(f"no root for {circuit} in [{left},{right}]")

    offset = np.zeros(len(modes))
    installed = []
    previous_alpha = 0.0
    for reverse_index, (circuit, control_rows) in enumerate(args.reverse):
        root = find_first_root(circuit, offset, previous_alpha, args.horizon)
        wall_coefficients = root * direction_x + offset
        wall_deaths = death_values(wall_coefficients)
        local_columns = [
            column for column, meta in enumerate(mode_meta)
            if meta.get("row") in control_rows
        ]
        if len(local_columns) <= 4:
            raise RuntimeError(f"insufficient local columns for {circuit}: {local_columns}")
        fractional_jacobian = np.empty((4, len(local_columns)))
        circuit_gradient = np.empty(len(local_columns))
        for j, column in enumerate(local_columns):
            step = np.zeros(len(modes))
            step[column] = args.fd_step
            fractional_jacobian[:, j] = (
                (death_values(wall_coefficients + step)
                 - death_values(wall_coefficients - step))
                / (2.0 * args.fd_step)
                / wall_deaths
            )
            circuit_gradient[j] = (
                volume(wall_coefficients + step, circuit)
                - volume(wall_coefficients - step, circuit)
            ) / (2.0 * args.fd_step)
        _u, singular_values, vt = np.linalg.svd(fractional_jacobian, full_matrices=True)
        tolerance = max(fractional_jacobian.shape) * np.finfo(float).eps * singular_values[0]
        rank = int(np.sum(singular_values > tolerance))
        null_basis = vt[rank:].T
        projected = null_basis @ (null_basis.T @ circuit_gradient)
        projection_norm = float(np.linalg.norm(projected))
        if projection_norm <= 1e-14:
            raise RuntimeError(f"circuit {circuit} has no chosen local null control")
        x_step = 0.1 * args.fd_step
        derivative_x = (
            volume(wall_coefficients + x_step * direction_x, circuit)
            - volume(wall_coefficients - x_step * direction_x, circuit)
        ) / (2.0 * x_step)
        target_shift = (
            -args.protection_factor * derivative_x * (args.horizon - root)
        )
        local_delta = projected * (target_shift / float(circuit_gradient @ projected))
        delta = np.zeros(len(modes))
        delta[local_columns] = local_delta

        before = (root - args.lift_epsilon) * direction_x + offset
        lifted = before + delta
        desired_sign = int(np.sign(volume(before, circuit)))
        lift_polynomial = polynomial_roots_on_segment(coordinates, before, lifted, circuit)
        horizontal_end = args.horizon * direction_x + offset + delta
        horizontal_polynomial = polynomial_roots_on_segment(
            coordinates, lifted, horizontal_end, circuit
        )
        _br, _bv, _bf, before_record = state(before)
        _lr, _lv, _lf, lifted_record = state(lifted)
        if (
            lift_polynomial["real_roots_in_closed_segment"]
            or horizontal_polynomial["real_roots_in_closed_segment"]
            or int(np.sign(volume(horizontal_end, circuit))) != desired_sign
        ):
            raise RuntimeError(f"protection factor failed for reverse {circuit}")
        offset += delta
        previous_alpha = root + args.lift_epsilon
        installed.append({
            "circuit": list(circuit),
            "control_rows": list(control_rows),
            "root_alpha": root,
            "local_columns": local_columns,
            "local_rank": rank,
            "local_nullity": int(null_basis.shape[1]),
            "local_singular_values": singular_values.tolist(),
            "nullspace_projection_norm": projection_norm,
            "circuit_derivative_x": derivative_x,
            "target_volume_shift": target_shift,
            "control_norm": float(np.linalg.norm(delta)),
            "control_coefficients": delta.tolist(),
            "max_abs_fractional_death_leakage": float(np.max(np.abs(fractional_jacobian @ local_delta))),
            "before_volume": volume(before, circuit),
            "lifted_volume": volume(lifted, circuit),
            "horizon_volume": volume(horizontal_end, circuit),
            "lift_polynomial": lift_polynomial,
            "horizontal_polynomial": horizontal_polynomial,
            "before_audit": before_record,
            "lifted_audit": lifted_record,
        })

    scan_start = previous_alpha
    start_coefficients = scan_start * direction_x + offset
    _start_result, _start_values, start_faces, start_record = state(start_coefficients)
    if start_faces != source_faces:
        removed = sorted([sorted(face) for face in source_faces - start_faces], key=lambda x: (len(x), x))
        added = sorted([sorted(face) for face in start_faces - source_faces], key=lambda x: (len(x), x))
        raise RuntimeError(
            f"reverse bypasses did not preserve the source face lattice; removed={removed}; added={added}"
        )
    if not start_record["hard_valid"]:
        raise RuntimeError("reverse bypass start is not hard-valid")

    scan = []
    event_bracket = None
    failure_bracket = None
    previous = (scan_start, start_faces, start_record)
    for alpha in np.linspace(scan_start, args.horizon, args.scan_points)[1:]:
        coefficients = alpha * direction_x + offset
        try:
            _result, _values, faces, record = state(coefficients)
        except Exception as error:
            failure_bracket = {
                "left_alpha": previous[0],
                "right_alpha": float(alpha),
                "type": "mechanics_evaluation_failure",
                "error": repr(error),
            }
            break
        scan.append({
            "alpha": float(alpha),
            "f_vector": record["f_vector"],
            "class": record["class"],
            "topology_margin": record["topology_margin"],
            "inactive_rows": record["inactive_rows"],
            "hard_valid": record["hard_valid"],
            "death_ratios_to_original": record["death_ratios_to_original"],
        })
        if faces != start_faces:
            event_bracket = {
                "left_alpha": previous[0],
                "right_alpha": float(alpha),
                "left_faces": previous[1],
                "right_faces": faces,
                "left_audit": previous[2],
                "right_audit": record,
            }
            break
        if not record["hard_valid"]:
            failure_bracket = {
                "left_alpha": previous[0],
                "right_alpha": float(alpha),
                "type": "mechanical_or_structural_wall",
                "left_audit": previous[2],
                "right_audit": record,
            }
            break
        previous = (float(alpha), faces, record)

    exact_event = None
    if event_bracket is not None:
        left = event_bracket["left_alpha"]
        right = event_bracket["right_alpha"]
        circuits = candidate_circuits(event_bracket["left_faces"], event_bracket["right_faces"])
        roots = []
        for circuit in circuits:
            left_value = volume(left * direction_x + offset, circuit)
            right_value = volume(right * direction_x + offset, circuit)
            if left_value * right_value < 0:
                root = float(brentq(
                    lambda alpha: volume(alpha * direction_x + offset, circuit),
                    left, right, xtol=1e-15, rtol=1e-14,
                ))
                roots.append((root, circuit))
            else:
                # The face grouper deliberately reports a maximal quad in a
                # thin band around exact coplanarity.  Continue past that band
                # to bracket the determinant zero itself.
                grid = np.linspace(right, args.horizon, 801)
                previous_alpha = left
                previous_value = left_value
                for alpha in grid:
                    current_value = volume(alpha * direction_x + offset, circuit)
                    if previous_value * current_value < 0:
                        root = float(brentq(
                            lambda x: volume(x * direction_x + offset, circuit),
                            previous_alpha, float(alpha), xtol=1e-15, rtol=1e-14,
                        ))
                        roots.append((root, circuit))
                        break
                    previous_alpha = float(alpha)
                    previous_value = current_value
        if roots:
            root, circuit = min(roots)
            epsilon = min(3e-6, max(1e-6, 0.1 * (right - left)))
            before_coefficients = (root - epsilon) * direction_x + offset
            at_coefficients = root * direction_x + offset
            after_coefficients = (root + epsilon) * direction_x + offset
            before_points = coordinates(before_coefficients)
            at_points = coordinates(at_coefficients)
            after_points = coordinates(after_coefficients)
            prefix = HERE / args.prefix
            write_csv(prefix.with_name(prefix.name + "_before.csv"), before_points)
            write_csv(prefix.with_name(prefix.name + "_at.csv"), at_points)
            write_csv(prefix.with_name(prefix.name + "_after.csv"), after_points)
            _r0, _v0, faces0, audit0 = state(before_coefficients)
            _r1, _v1, faces1, audit1 = state(at_coefficients)
            _r2, _v2, faces2, audit2 = state(after_coefficients)
            exact_event = {
                "circuit": list(circuit),
                "alpha_root": root,
                "epsilon": epsilon,
                "volume_at_root": volume(at_coefficients, circuit),
                "known_reverse": circuit in {item[0] for item in args.reverse},
                "before_faces": circuit_faces(faces0, circuit),
                "at_faces": circuit_faces(faces1, circuit),
                "after_faces": circuit_faces(faces2, circuit),
                "before_audit": audit0,
                "at_audit": audit1,
                "after_audit": audit2,
                "csv": {
                    "before": prefix.name + "_before.csv",
                    "at": prefix.name + "_at.csv",
                    "after": prefix.name + "_after.csv",
                },
            }

    endpoint_alpha = (
        exact_event["alpha_root"] - exact_event["epsilon"]
        if exact_event is not None
        else (
            failure_bracket["left_alpha"] if failure_bracket is not None
            else args.horizon
        )
    )
    endpoint_coefficients = endpoint_alpha * direction_x + offset
    endpoint_points = coordinates(endpoint_coefficients)
    endpoint_path = HERE / f"{args.prefix}_endpoint.csv"
    write_csv(endpoint_path, endpoint_points)
    _endpoint_result, _endpoint_values, _endpoint_faces, endpoint_audit = state(endpoint_coefficients)

    def serializable_bracket(bracket):
        if bracket is None:
            return None
        return {
            key: value
            for key, value in bracket.items()
            if key not in ("left_faces", "right_faces")
        }

    payload = {
        "version": 1,
        "scope": "event-driven predictor with local four-death-null reverse bypasses",
        "source": args.source,
        "lp_json": args.lp_json,
        "lp_delta": best["delta"],
        "death_keys": [repr(key) for key in death_keys],
        "horizon": args.horizon,
        "installed_reverse_bypasses": installed,
        "cumulative_control_norm": float(np.linalg.norm(offset)),
        "cumulative_control_coefficients": offset.tolist(),
        "scan_start_alpha": scan_start,
        "scan_start_audit": start_record,
        "scan": scan,
        "event_bracket": serializable_bracket(event_bracket),
        "failure_bracket": serializable_bracket(failure_bracket),
        "exact_event": exact_event,
        "endpoint": {
            "alpha": endpoint_alpha,
            "csv": endpoint_path.name,
            "audit": endpoint_audit,
        },
        "materially_below_0_9": bool(
            exact_event is not None
            and max(exact_event["after_audit"]["death_ratios_to_original"].values()) < 0.9
        ),
    }
    (HERE / f"{args.prefix}.json").write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "lp_delta": best["delta"],
        "installed_reverse_bypasses": [
            {
                "circuit": item["circuit"],
                "root_alpha": item["root_alpha"],
                "control_rows": item["control_rows"],
                "nullity": item["local_nullity"],
                "death_leakage": item["max_abs_fractional_death_leakage"],
                "horizon_volume": item["horizon_volume"],
            }
            for item in installed
        ],
        "failure_bracket": payload["failure_bracket"],
        "exact_event": exact_event,
        "materially_below_0_9": payload["materially_below_0_9"],
    }, indent=2))


if __name__ == "__main__":
    main()
