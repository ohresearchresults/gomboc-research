#!/usr/bin/env python3
"""Rebuild the guarded four-death first jet in the exact post-flip cell.

The exact t=51/50 point is used only as a rational source.  The script
reconstructs the actual hull and own-centroid primitive ledger, differentiates
the complete planarity chart, enumerates all 16 saddle-component branches,
and traces the best minimum-physical-displacement direction only until the
first actual incidence or mechanics event.  Its line trace is discovery data;
an exact event certificate is required separately.
"""
from __future__ import annotations

import argparse
import ast
import json
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
sys.path.insert(0, str(PARENT))

import build_u54_material_exact_path as exact_path  # noqa: E402
import combined_four_death_lp as four  # noqa: E402
from integrate_four_death_direction import write_csv  # noqa: E402
from predictor_bypass_epoch import candidate_circuits  # noqa: E402


SOURCE = HERE / "first_extrapolated_event_far.csv"


def load_exact_float(path: Path):
    return {
        label: np.asarray([float(value) for value in xyz], dtype=float)
        for label, xyz in exact_path.ex.read_rows(path).items()
    }


def apply_modes(points, modes, coefficients):
    return {
        label: np.asarray(points[label], dtype=float)
        + sum(
            (coefficient * modes[index][label] for index, coefficient in enumerate(coefficients)),
            start=np.zeros(3),
        )
        for label in points
    }


def face_signature(result):
    return tuple(sorted(tuple(sorted(face["cycle"])) for face in result.faces))


def equilibrium_signature(result):
    return (
        tuple(sorted(tuple(sorted(result.faces[index]["cycle"])) for index, _ in result.stable)),
        tuple(sorted(index for index, _ in result.unstable)),
        tuple(sorted(tuple(edge) for edge, _ in result.saddles)),
    )


def json_key(key):
    return repr(key)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=float, default=300.0)
    parser.add_argument("--delta-slack", type=float, default=0.01)
    parser.add_argument("--fd-step", type=float, default=1e-9)
    parser.add_argument("--line-maximum", type=float, default=1.2)
    parser.add_argument("--line-step", type=float, default=0.001)
    parser.add_argument("--plane-tol", type=float, default=1e-11)
    args = parser.parse_args()

    points = load_exact_float(SOURCE)
    four.ACTIVE_PLANE_TOL = args.plane_tol
    result, values = four.primitive_ledger(points, plane_tol=args.plane_tol)
    expected_faces = {four.BASE, four.QUAD}
    stable_faces = {frozenset(result.faces[index]["cycle"]) for index, _ in result.stable}
    if stable_faces != expected_faces:
        raise AssertionError(("stable faces", stable_faces))
    if {index for index, _ in result.unstable} != {8, 54}:
        raise AssertionError(("unstable", result.unstable))
    if {edge for edge, _ in result.saddles} != four.H_EXTRA:
        raise AssertionError(("saddles", result.saddles))
    if [len(result.active), len(result.edges), len(result.faces)] != [60, 158, 100]:
        raise AssertionError("unexpected exact far-cell f-vector")

    modes, mode_meta, chart_meta = four.chart_modes(points)
    keys, key_index, jacobian, failures = four.baseline.finite_difference(
        points, values, modes, h=args.fd_step
    )
    np.savez_compressed(
        HERE / "post_flip_first_jet_jacobian.npz",
        jacobian=jacobian,
        primitive_keys=np.asarray([repr(key) for key in keys], dtype=object),
        primitive_values=np.asarray([values[key] for key in keys]),
        mode_meta=np.asarray([json.dumps(row, sort_keys=True) for row in mode_meta], dtype=object),
    )

    quad = next(
        key
        for key in values
        if key[0] == "face" and frozenset(key[1]) == four.QUAD and key[2] == (8, 246)
    )
    u54 = ("vertex", 54, 1)
    h67 = sorted(key for key in values if key[0] == "edge" and key[1] == (6, 7))
    h910 = sorted(key for key in values if key[0] == "edge" and key[1] == (9, 10))
    guards = four.chosen_guards(values)
    guard_matrix = []
    guard_info = []
    for key, sign, kind in guards:
        scale = max(abs(values[key]), 1e-12)
        guard_matrix.append(-sign * jacobian[key_index[key]] / scale)
        guard_info.append({
            "key": json_key(key),
            "sign": sign,
            "kind": kind,
            "value": float(values[key]),
        })
    guard_matrix = np.asarray(guard_matrix)

    labels = sorted(points)
    displacement_matrix = np.asarray([
        [modes[column][label][axis] for column in range(len(modes))]
        for label in labels
        for axis in range(3)
    ])
    branches = []
    n = len(modes)
    for key67 in h67:
        for key910 in h910:
            deaths = (quad, u54, key67, key910)
            death_matrix = np.asarray([
                jacobian[key_index[key]] / values[key] for key in deaths
            ])
            primary_A = np.vstack((
                np.c_[guard_matrix, -np.ones(len(guards))],
                np.c_[death_matrix, np.zeros(4)],
            ))
            primary_b = np.r_[np.zeros(len(guards)), -np.ones(4)]
            primary = linprog(
                np.r_[np.zeros(n), 1.0],
                A_ub=primary_A,
                b_ub=primary_b,
                bounds=[(-args.bound, args.bound)] * n + [(-1e6, 1e6)],
                method="highs",
            )
            record = {
                "h67_component": key67[2],
                "h910_component": key910[2],
                "deaths": [json_key(key) for key in deaths],
                "primary_success": bool(primary.success),
                "primary_message": primary.message,
            }
            if not primary.success:
                branches.append(record)
                continue
            delta = float(primary.x[-1])
            delta_cap = delta * (1.0 + args.delta_slack) + 1e-10
            secondary_A = np.vstack((
                np.c_[guard_matrix, np.zeros(len(guards))],
                np.c_[death_matrix, np.zeros(4)],
                np.c_[displacement_matrix, -np.ones(displacement_matrix.shape[0])],
                np.c_[-displacement_matrix, -np.ones(displacement_matrix.shape[0])],
            ))
            secondary_b = np.r_[
                np.full(len(guards), delta_cap),
                -np.ones(4),
                np.zeros(2 * displacement_matrix.shape[0]),
            ]
            secondary = linprog(
                np.r_[np.zeros(n), 1.0],
                A_ub=secondary_A,
                b_ub=secondary_b,
                bounds=[(-args.bound, args.bound)] * n + [(0.0, None)],
                method="highs",
            )
            record.update({
                "delta": delta,
                "delta_cap": delta_cap,
                "secondary_success": bool(secondary.success),
                "secondary_message": secondary.message,
            })
            if not secondary.success:
                branches.append(record)
                continue
            coefficients = np.asarray(secondary.x[:n])
            worsening = guard_matrix @ coefficients
            record.update({
                "physical_linf": float(secondary.x[-1]),
                "coefficient_linf": float(np.max(np.abs(coefficients))),
                "coefficient_l2": float(np.linalg.norm(coefficients)),
                "death_fractional_derivatives": (death_matrix @ coefficients).tolist(),
                "max_guard_fractional_worsening": float(np.max(worsening)),
                "coefficients": coefficients.tolist(),
                "top_guard_blockers": [
                    {
                        **guard_info[index],
                        "fractional_worsening": float(worsening[index]),
                    }
                    for index in np.argsort(worsening)[-20:][::-1]
                ],
            })
            branches.append(record)

    successful = [row for row in branches if row.get("secondary_success")]
    successful.sort(key=lambda row: (row["physical_linf"], row["delta"]))
    if not successful:
        raise RuntimeError("no physically regularized four-death branch")
    best = successful[0]
    direction = np.asarray(best["coefficients"], dtype=float)

    baseline_faces = face_signature(result)
    baseline_equilibria = equilibrium_signature(result)
    previous_alpha = 0.0
    previous_result = result
    first_event = None
    alpha = args.line_step
    line_samples = 0
    while alpha <= args.line_maximum + args.line_step * 0.25:
        line_samples += 1
        candidate = apply_modes(points, modes, alpha * direction)
        try:
            candidate_result, candidate_values = four.primitive_ledger(
                candidate, plane_tol=args.plane_tol
            )
        except Exception as error:
            first_event = {
                "type": "evaluator_failure",
                "bracket": [previous_alpha, alpha],
                "error": repr(error),
            }
            break
        faces = face_signature(candidate_result)
        equilibria = equilibrium_signature(candidate_result)
        if faces != baseline_faces or equilibria != baseline_equilibria:
            circuits = candidate_circuits(
                {frozenset(face) for face in baseline_faces},
                {frozenset(face) for face in faces},
            ) if faces != baseline_faces else []
            before_path = HERE / "post_flip_first_jet_event_before.csv"
            after_path = HERE / "post_flip_first_jet_event_after.csv"
            write_csv(before_path, apply_modes(points, modes, previous_alpha * direction))
            write_csv(after_path, candidate)
            first_event = {
                "type": "support_or_incidence" if faces != baseline_faces else "mechanics_only",
                "bracket": [previous_alpha, alpha],
                "candidate_circuits": [list(circuit) for circuit in circuits],
                "before_file": before_path.name,
                "after_file": after_path.name,
                "before_f_vector": [
                    len(previous_result.active), len(previous_result.edges), len(previous_result.faces)
                ],
                "after_f_vector": [
                    len(candidate_result.active), len(candidate_result.edges), len(candidate_result.faces)
                ],
                "before_class": [
                    len(previous_result.stable), len(previous_result.unstable), len(previous_result.saddles)
                ],
                "after_class": [
                    len(candidate_result.stable), len(candidate_result.unstable), len(candidate_result.saddles)
                ],
                "removed_faces": [
                    list(face) for face in sorted(set(baseline_faces) - set(faces))
                ],
                "added_faces": [
                    list(face) for face in sorted(set(faces) - set(baseline_faces))
                ],
                "before_equilibria": {
                    "stable": [list(face) for face in equilibrium_signature(previous_result)[0]],
                    "unstable": list(equilibrium_signature(previous_result)[1]),
                    "saddles": [list(edge) for edge in equilibrium_signature(previous_result)[2]],
                },
                "after_equilibria": {
                    "stable": [list(face) for face in equilibria[0]],
                    "unstable": list(equilibria[1]),
                    "saddles": [list(edge) for edge in equilibria[2]],
                },
            }
            break
        previous_alpha = alpha
        previous_result = candidate_result
        alpha += args.line_step

    payload = {
        "version": 1,
        "scope": "post-exact-flip complete guarded first jet and first-event trace",
        "source": SOURCE.name,
        "baseline": {
            "f_vector": [len(result.active), len(result.edges), len(result.faces)],
            "class": [len(result.stable), len(result.unstable), len(result.saddles)],
            "topology_margin": float(result.topology_margin),
            "chart": chart_meta,
        },
        "mode_count": len(modes),
        "primitive_count": len(keys),
        "guard_count": len(guards),
        "finite_difference_failures": failures,
        "branches": branches,
        "best_branch": best,
        "line_trace": {
            "discovery_only": True,
            "maximum": args.line_maximum,
            "step": args.line_step,
            "samples": line_samples,
            "first_event": first_event,
        },
        "conclusion": (
            "first post-flip actual event bracketed; exact isolation required"
            if first_event is not None
            else "no actual event found on traced segment"
        ),
    }
    output = HERE / "post_flip_first_jet.json"
    output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "baseline": payload["baseline"],
        "best": {
            key: best[key]
            for key in (
                "h67_component",
                "h910_component",
                "delta",
                "physical_linf",
                "death_fractional_derivatives",
                "max_guard_fractional_worsening",
            )
        },
        "first_event": first_event,
        "output": str(output),
    }, indent=2))


if __name__ == "__main__":
    main()
