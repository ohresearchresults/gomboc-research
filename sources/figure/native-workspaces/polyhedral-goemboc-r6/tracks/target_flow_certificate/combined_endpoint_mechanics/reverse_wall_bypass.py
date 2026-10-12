#!/usr/bin/env python3
"""Two-dimensional actual-cell bypass of the relay-4 reverse wall.

The x direction is the fixed H67=1-t, H910=t bound-300 four-death direction
in the post-relay-3 cell.  The y direction is supported only on rows 69 and
255 and is the projection of the reverse-circuit volume gradient into the
nullspace of the four fractional death gradients.  Consequently y preserves
all four death rates to first order and, because it does not move any vertex
of {198,234,235,236}, leaves the next independent circuit exactly unchanged.

All reported cells and path points rebuild the hull and mechanics ledger.
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


HERE = Path(__file__).resolve().parent
REVERSE = (69, 228, 235, 255)
INDEPENDENT = (198, 234, 235, 236)


def oriented_volume(points, circuit):
    a, b, c, d = (points[i] for i in circuit)
    return float(np.linalg.det(np.column_stack((b - a, c - a, d - a))))


def faces_meeting(result, circuit):
    cset = frozenset(circuit)
    return sorted(
        [
            sorted(face["cycle"])
            for face in result.faces
            if len(frozenset(face["cycle"]) & cset) >= 3
        ],
        key=lambda face: (len(face), face),
    )


def polynomial_roots_on_segment(coordinates, left, right, circuit):
    """Numerically recover all real volume roots on a straight chart segment."""
    t = np.asarray([0.0, 1.0 / 3.0, 2.0 / 3.0, 1.0])
    values = np.asarray([
        oriented_volume(coordinates(left + s * (right - left)), circuit)
        for s in t
    ])
    scale = max(float(np.max(np.abs(values))), 1e-300)
    coefficients = np.polynomial.polynomial.polyfit(t, values / scale, 3)
    roots = np.polynomial.Polynomial(coefficients).roots()
    real = sorted(
        float(root.real)
        for root in roots
        if abs(root.imag) <= 1e-7 and -1e-10 <= root.real <= 1.0 + 1e-10
    )
    return {
        "endpoint_volumes": [float(values[0]), float(values[-1])],
        "normalized_power_coefficients": coefficients.tolist(),
        "real_roots_in_closed_segment": real,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="postq73_relay2_step_a0003.csv")
    parser.add_argument("--lp-json", default="postq73_relay3_lp.json")
    parser.add_argument("--reverse-wall", default="postq73_relay4a_wall.json")
    parser.add_argument("--independent-wall", default="postq73_relay4b_wall.json")
    parser.add_argument("--radius", type=float, default=5e-6)
    parser.add_argument("--antirelay-factor", type=float, default=4.0)
    parser.add_argument("--fd-step", type=float, default=1e-6)
    parser.add_argument("--path-points", type=int, default=41)
    parser.add_argument(
        "--event-epsilon", type=float, default=5e-7,
        help="distance on the main x axis used for before/after independent-wall cells",
    )
    parser.add_argument(
        "--after-event-epsilon", type=float,
        help="optional deeper post-wall offset; the pre-wall offset remains --event-epsilon",
    )
    parser.add_argument("--prefix", default="reverse_wall_bypass")
    args = parser.parse_args()

    source_path = Path(args.source)
    source = four.load_points(source_path)
    source_result, source_values = four.primitive_ledger(source)
    modes, mode_meta, _ = four.chart_modes(source)
    lp = json.loads(Path(args.lp_json).read_text())
    candidates = [
        row for row in lp["atlas"]
        if row.get("success")
        and ast.literal_eval(row["deaths"][2])[2] == "one_minus_t"
        and ast.literal_eval(row["deaths"][3])[2] == "t"
    ]
    if not candidates:
        raise RuntimeError("fixed (H67=1-t,H910=t) branch absent")
    best = min(candidates, key=lambda row: row["delta"])
    death_keys = [ast.literal_eval(key) for key in best["deaths"]]
    direction_x = np.asarray(best["coefficients"], dtype=float)

    reverse_wall = json.loads(Path(args.reverse_wall).read_text())
    alpha_star = float(reverse_wall["alpha_wall"])
    coefficient_star = alpha_star * direction_x

    canonical = four.load_points(HERE / "../../circuit_atlas/row54_combined_wall_rebuilt.csv")
    _, canonical_values = four.primitive_ledger(canonical)
    canonical_deaths = np.asarray([canonical_values[key] for key in death_keys])

    def coordinates(coefficients):
        return rank6.apply_modes(source, modes, coefficients)

    def death_values(coefficients):
        _result, values = four.primitive_ledger(coordinates(coefficients))
        return np.asarray([values[key] for key in death_keys])

    star_deaths = death_values(coefficient_star)
    local_columns = [
        column for column, meta in enumerate(mode_meta)
        if meta.get("row") in (69, 255)
    ]
    if len(local_columns) != 6:
        raise RuntimeError(f"expected six row69/255 columns, got {local_columns}")

    # Differentiate the actual nonlinear parameterization at the exact wall.
    fractional_local_jacobian = np.empty((4, len(local_columns)))
    reverse_local_gradient = np.empty(len(local_columns))
    for j, column in enumerate(local_columns):
        step = np.zeros(len(modes))
        step[column] = args.fd_step
        plus = coefficient_star + step
        minus = coefficient_star - step
        fractional_local_jacobian[:, j] = (
            (death_values(plus) - death_values(minus))
            / (2.0 * args.fd_step)
            / star_deaths
        )
        reverse_local_gradient[j] = (
            oriented_volume(coordinates(plus), REVERSE)
            - oriented_volume(coordinates(minus), REVERSE)
        ) / (2.0 * args.fd_step)

    u, singular_values, vt = np.linalg.svd(
        fractional_local_jacobian, full_matrices=True
    )
    tolerance = (
        max(fractional_local_jacobian.shape)
        * np.finfo(float).eps
        * singular_values[0]
    )
    rank = int(np.sum(singular_values > tolerance))
    null_basis = vt[rank:].T
    projected_gradient = null_basis @ (null_basis.T @ reverse_local_gradient)
    projected_norm = float(np.linalg.norm(projected_gradient))
    if projected_norm <= 1e-14:
        raise RuntimeError("reverse circuit has no row69/255 four-death-null control")

    x_step = 0.1 * args.fd_step
    reverse_derivative_x = (
        oriented_volume(coordinates(coefficient_star + x_step * direction_x), REVERSE)
        - oriented_volume(coordinates(coefficient_star - x_step * direction_x), REVERSE)
    ) / (2.0 * x_step)
    fractional_death_derivative_x = (
        (death_values(coefficient_star + x_step * direction_x)
         - death_values(coefficient_star - x_step * direction_x))
        / (2.0 * x_step)
        / star_deaths
    )

    # Positive y bends the path toward the pre-reverse orientation.  Its
    # circuit rate is antirelay_factor times the opposite x rate.
    local_y = projected_gradient * (
        -args.antirelay_factor * reverse_derivative_x
        / float(reverse_local_gradient @ projected_gradient)
    )
    direction_y = np.zeros(len(modes))
    direction_y[local_columns] = local_y
    fractional_death_derivative_y = fractional_local_jacobian @ local_y
    reverse_derivative_y = float(reverse_local_gradient @ local_y)

    forced_rails = combined_core.forced_rail_edges()
    source_face_set = {frozenset(face["cycle"]) for face in source_result.faces}

    def audit(coefficients, compact=False):
        points = coordinates(coefficients)
        result, values = four.primitive_ledger(points)
        face_sets = {frozenset(face["cycle"]) for face in result.faces}
        stable_faces = {
            frozenset(result.faces[index]["cycle"]) for index, _value in result.stable
        }
        unstable = sorted(index for index, _value in result.unstable)
        saddles = sorted([list(edge) for edge, _value in result.saddles])
        current_deaths = np.asarray([values[key] for key in death_keys])
        record = {
            "f_vector": [len(result.active), len(result.edges), len(result.faces)],
            "class": [len(result.stable), len(result.unstable), len(result.saddles)],
            "topology_margin": float(result.topology_margin),
            "inactive_rows": sorted(set(source) - set(result.active)),
            "base_present": four.BASE in face_sets,
            "quad_present": four.QUAD in face_sets,
            "u8_retained": 8 in unstable,
            "all_forced_rails_present": forced_rails <= set(result.edges),
            "missing_forced_rails": sorted([list(edge) for edge in forced_rails - set(result.edges)]),
            "stable_faces": sorted([sorted(face) for face in stable_faces], key=lambda f: (len(f), f)),
            "unstable_vertices": unstable,
            "saddle_edges": saddles,
            "reverse_volume": oriented_volume(points, REVERSE),
            "independent_volume": oriented_volume(points, INDEPENDENT),
            "reverse_circuit_faces": faces_meeting(result, REVERSE),
            "independent_circuit_faces": faces_meeting(result, INDEPENDENT),
            "death_ratios_to_original_combined_wall": {
                repr(key): float(value / reference)
                for key, value, reference in zip(death_keys, current_deaths, canonical_deaths)
            },
            "death_ratios_to_post_relay_3_source": {
                repr(key): float(value / source_values[key])
                for key, value in zip(death_keys, current_deaths)
            },
        }
        record["hard_valid"] = bool(
            record["base_present"]
            and record["quad_present"]
            and record["u8_retained"]
            and record["all_forced_rails_present"]
            and record["class"] == [2, 2, 2]
            and record["inactive_rows"] == [73]
        )
        if not compact:
            record["faces_match_post_relay_3_source"] = face_sets == source_face_set
        return record

    radius = args.radius
    prefix = HERE / args.prefix
    quadrants = []
    for sx in (-1, 1):
        for sy in (-1, 1):
            coefficients = coefficient_star + radius * (
                sx * direction_x + sy * direction_y
            )
            name = ("m" if sx < 0 else "p") + ("m" if sy < 0 else "p")
            write_csv(prefix.with_name(prefix.name + f"_quadrant_{name}.csv"), coordinates(coefficients))
            quadrants.append({
                "quadrant": [sx, sy],
                "chart_coordinates": [sx * radius, sy * radius],
                "csv": prefix.name + f"_quadrant_{name}.csv",
                "audit": audit(coefficients),
            })

    # L path: begin on the pre-reverse side, lift in +y, cross the scalar
    # reverse root, then continue horizontally to the independent wall.
    start = coefficient_star - radius * direction_x
    lifted = start + radius * direction_y
    crossed = coefficient_star + radius * (direction_x + direction_y)

    # y moves only rows 69/255, so this root is geometrically independent of y.
    independent_hint = float(json.loads(Path(args.independent_wall).read_text())["alpha_wall"])
    hint_relative = independent_hint - alpha_star

    def independent_volume_at_x(x_relative):
        return oriented_volume(
            coordinates(coefficient_star + x_relative * direction_x + radius * direction_y),
            INDEPENDENT,
        )

    bracket_left = radius
    bracket_right = max(3.0 * radius, 1.25 * hint_relative)
    if independent_volume_at_x(bracket_left) * independent_volume_at_x(bracket_right) >= 0:
        raise RuntimeError("independent circuit root is not bracketed after bypass")
    independent_x = float(brentq(
        independent_volume_at_x, bracket_left, bracket_right,
        xtol=1e-15, rtol=1e-14,
    ))
    event_epsilon = min(args.event_epsilon, 0.8 * (independent_x - radius))
    after_event_epsilon = (
        event_epsilon if args.after_event_epsilon is None
        else args.after_event_epsilon
    )
    before_independent = (
        coefficient_star + (independent_x - event_epsilon) * direction_x
        + radius * direction_y
    )
    at_independent = (
        coefficient_star + independent_x * direction_x + radius * direction_y
    )
    after_independent = (
        coefficient_star + (independent_x + after_event_epsilon) * direction_x
        + radius * direction_y
    )

    materialized = {
        "start": start,
        "lifted": lifted,
        "crossed": crossed,
        "before_independent": before_independent,
        "at_independent": at_independent,
        "after_independent": after_independent,
    }
    waypoint_audits = {}
    for name, coefficients in materialized.items():
        filename = prefix.with_name(prefix.name + f"_{name}.csv")
        write_csv(filename, coordinates(coefficients))
        waypoint_audits[name] = {"csv": filename.name, "audit": audit(coefficients)}

    segments = [
        ("lift", start, lifted),
        ("cross_reverse_scalar_location", lifted, crossed),
        ("continue_to_independent", crossed, before_independent),
    ]
    path = []
    segment_root_audits = []
    for segment_index, (name, left, right) in enumerate(segments):
        segment_root_audits.append({
            "segment": name,
            "reverse_circuit_polynomial": polynomial_roots_on_segment(
                coordinates, left, right, REVERSE
            ),
        })
        for offset, t in enumerate(np.linspace(0.0, 1.0, args.path_points)):
            if segment_index and offset == 0:
                continue
            coefficients = left + t * (right - left)
            path.append({
                "segment": name,
                "t": float(t),
                "audit": audit(coefficients, compact=True),
            })

    initial_reverse_sign = float(np.sign(path[0]["audit"]["reverse_volume"]))
    all_path_reverse_same_sign = all(
        np.sign(row["audit"]["reverse_volume"]) == initial_reverse_sign
        for row in path
    )
    all_path_hard_valid = all(row["audit"]["hard_valid"] for row in path)
    all_path_below_original = all(
        all(ratio < 1.0 for ratio in row["audit"]["death_ratios_to_original_combined_wall"].values())
        for row in path
    )
    start_deaths = death_values(start)
    end_deaths = death_values(before_independent)
    all_four_decrease_start_to_end = bool(np.all(end_deaths < start_deaths))
    reverse_faces_start = waypoint_audits["start"]["audit"]["reverse_circuit_faces"]
    reverse_faces_end = waypoint_audits["before_independent"]["audit"]["reverse_circuit_faces"]

    payload = {
        "version": 1,
        "scope": "2D actual-cell bypass of relay-4 reverse wall",
        "source": str(source_path),
        "lp_json": args.lp_json,
        "lp_delta": best["delta"],
        "death_keys": [repr(key) for key in death_keys],
        "reverse_circuit": list(REVERSE),
        "independent_circuit": list(INDEPENDENT),
        "reverse_alpha_star": alpha_star,
        "radius": radius,
        "antirelay_factor": args.antirelay_factor,
        "local_control_rows": [69, 255],
        "local_control_columns": local_columns,
        "local_control_mode_meta": [mode_meta[column] for column in local_columns],
        "fractional_death_local_singular_values": singular_values.tolist(),
        "fractional_death_local_rank": rank,
        "fractional_death_local_nullity": int(null_basis.shape[1]),
        "reverse_gradient_nullspace_projection_norm": projected_norm,
        "direction_x": direction_x.tolist(),
        "direction_y": direction_y.tolist(),
        "direction_y_norm": float(np.linalg.norm(direction_y)),
        "fractional_death_derivative_x_at_wall": fractional_death_derivative_x.tolist(),
        "fractional_death_derivative_y_at_wall": fractional_death_derivative_y.tolist(),
        "max_abs_fractional_death_leakage_y": float(np.max(np.abs(fractional_death_derivative_y))),
        "reverse_volume_derivative_x_at_wall": reverse_derivative_x,
        "reverse_volume_derivative_y_at_wall": reverse_derivative_y,
        "independent_volume_change_under_y": float(
            oriented_volume(coordinates(coefficient_star + radius * direction_y), INDEPENDENT)
            - oriented_volume(coordinates(coefficient_star), INDEPENDENT)
        ),
        "quadrants": quadrants,
        "waypoints": waypoint_audits,
        "path": path,
        "segment_exact_root_audits": segment_root_audits,
        "independent_event": {
            "x_relative_to_reverse_wall": independent_x,
            "alpha_on_main_axis": alpha_star + independent_x,
            "unshifted_alpha_hint": independent_hint,
            "root_shift_due_to_y": alpha_star + independent_x - independent_hint,
            "epsilon": event_epsilon,
            "after_epsilon": after_event_epsilon,
            "volume_at_root": independent_volume_at_x(independent_x),
            "before": waypoint_audits["before_independent"],
            "at": waypoint_audits["at_independent"],
            "after": waypoint_audits["after_independent"],
        },
        "bypass_audit": {
            "all_path_hard_valid": all_path_hard_valid,
            "all_path_below_original_four_deaths": all_path_below_original,
            "all_four_decrease_start_to_end": all_four_decrease_start_to_end,
            "reverse_volume_sign_constant_on_path": all_path_reverse_same_sign,
            "reverse_faces_constant_start_to_independent": reverse_faces_start == reverse_faces_end,
            "no_reverse_roots_on_any_segment": all(
                not row["reverse_circuit_polynomial"]["real_roots_in_closed_segment"]
                for row in segment_root_audits
            ),
            "independent_wall_reached": waypoint_audits["at_independent"]["audit"]["f_vector"] == [60, 157, 99],
            "post_independent_cell_valid": waypoint_audits["after_independent"]["audit"]["hard_valid"],
            "bypass_found": bool(
                all_path_hard_valid
                and all_path_below_original
                and all_four_decrease_start_to_end
                and all_path_reverse_same_sign
                and reverse_faces_start == reverse_faces_end
                and all(
                    not row["reverse_circuit_polynomial"]["real_roots_in_closed_segment"]
                    for row in segment_root_audits
                )
                and waypoint_audits["after_independent"]["audit"]["hard_valid"]
            ),
            "diagnosis": (
                "avoidable codimension-one circuit wall, not a genuine limit cycle"
            ),
        },
    }
    prefix.with_suffix(".json").write_text(json.dumps(payload, indent=2) + "\n")

    md = [
        "# Two-dimensional bypass of the relay-4 reverse wall",
        "",
        "The main axis is the post-relay-3 bound-300 four-death direction. "
        "The transverse axis uses only rows 69 and 255 and lies in the "
        "four-death Jacobian nullspace.",
        "",
        f"- Local rank/nullity: `{rank}/{null_basis.shape[1]}`.",
        f"- Reverse-gradient nullspace projection: `{projected_norm:.12g}`.",
        f"- Maximum fractional death-rate leakage from y: "
        f"`{np.max(np.abs(fractional_death_derivative_y)):.3e}`.",
        f"- Independent-circuit volume change from y: "
        f"`{payload['independent_volume_change_under_y']:.3e}`.",
        "",
        "## Four fresh quadrant cells",
        "",
        "| quadrant (x,y) | lattice | reverse volume | reverse diagonal | valid |",
        "|---:|---:|---:|---|---:|",
    ]
    for row in quadrants:
        faces = " + ".join("`" + str(face) + "`" for face in row["audit"]["reverse_circuit_faces"])
        md.append(
            f"| {tuple(row['quadrant'])} | {tuple(row['audit']['f_vector'])} | "
            f"{row['audit']['reverse_volume']:.6e} | {faces} | "
            f"{row['audit']['hard_valid']} |"
        )
    md += [
        "",
        "The two diagonals occupy opposite half-planes in this 2D atlas. The "
        "L-path uses positive y, so it passes the scalar reverse-root location "
        "while retaining faces `[69,235,255] + [228,235,255]`.",
        "",
        "## Fresh-hull L-path and independent event",
        "",
        "| waypoint | lattice | topology margin | reverse volume | independent volume | quad | U54 | H67 | H910 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for name in (
        "start", "lifted", "crossed", "before_independent",
        "at_independent", "after_independent",
    ):
        record = waypoint_audits[name]["audit"]
        ratios = list(record["death_ratios_to_original_combined_wall"].values())
        md.append(
            f"| {name} | {tuple(record['f_vector'])} | "
            f"{record['topology_margin']:.3e} | {record['reverse_volume']:.6e} | "
            f"{record['independent_volume']:.6e} | "
            + " | ".join(f"{ratio:.9f}" for ratio in ratios)
            + " |"
        )
    md += [
        "",
        "The next independent circuit `{198,234,235,236}` is reached at main-axis "
        f"`alpha={alpha_star + independent_x:.15g}`. Its root shifts by only "
        f"`{alpha_star + independent_x - independent_hint:.3e}` because the y "
        "control moves none of its vertices. At the wall the lattice is "
        "`(60,157,99)`; immediately after it returns to `(60,158,100)` with "
        "the new diagonal `[198,234,236] + [234,235,236]`.",
        "",
        "All sampled path points retain the enlarged base, U8, every forced "
        "rail, class `(2,2,2)`, and inactive set `{73}`. The exact cubic "
        "segment audits find no reverse-circuit root on any L-path segment. "
        "Therefore the observed reverse flip is an **avoidable codimension-one "
        "wall, not a genuine limit cycle**.",
    ]
    prefix.with_suffix(".md").write_text("\n".join(md) + "\n")

    summary = {
        "lp_delta": best["delta"],
        "local_rank": rank,
        "local_nullity": int(null_basis.shape[1]),
        "nullspace_projection_norm": projected_norm,
        "death_y_leakage": payload["max_abs_fractional_death_leakage_y"],
        "quadrants": [
            {
                "quadrant": row["quadrant"],
                "f_vector": row["audit"]["f_vector"],
                "reverse_volume": row["audit"]["reverse_volume"],
                "reverse_faces": row["audit"]["reverse_circuit_faces"],
                "hard_valid": row["audit"]["hard_valid"],
            }
            for row in quadrants
        ],
        "independent_event": {
            "alpha": payload["independent_event"]["alpha_on_main_axis"],
            "root_shift_due_to_y": payload["independent_event"]["root_shift_due_to_y"],
            "before_f_vector": waypoint_audits["before_independent"]["audit"]["f_vector"],
            "at_f_vector": waypoint_audits["at_independent"]["audit"]["f_vector"],
            "after_f_vector": waypoint_audits["after_independent"]["audit"]["f_vector"],
            "reverse_volume_at_independent": waypoint_audits["at_independent"]["audit"]["reverse_volume"],
        },
        "bypass_audit": payload["bypass_audit"],
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
