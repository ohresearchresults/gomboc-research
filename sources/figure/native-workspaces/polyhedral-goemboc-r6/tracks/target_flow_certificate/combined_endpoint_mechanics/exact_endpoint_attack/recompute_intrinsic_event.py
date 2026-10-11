#!/usr/bin/env python3
"""Recompute and resolve the first intrinsic post-flip SLP event."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
sys.path.insert(0, str(PARENT))
sys.path.insert(0, str(HERE))

import build_u54_material_exact_path as exact_path  # noqa: E402
import combined_four_death_lp as four  # noqa: E402
from integrate_four_death_direction import write_csv  # noqa: E402
from predictor_bypass_epoch import candidate_circuits  # noqa: E402
import post_flip_trust_slp as slp  # noqa: E402


SOURCE = HERE / "post_flip_intrinsic_step_008.csv"
TRUST = 2.562890625e-6
PLANE_TOL = 2e-12


def face_signature(result):
    return tuple(sorted(tuple(sorted(face["cycle"])) for face in result.faces))


def equilibrium_signature(result):
    return (
        tuple(sorted(tuple(sorted(result.faces[index]["cycle"])) for index, _ in result.stable)),
        tuple(sorted(index for index, _ in result.unstable)),
        tuple(sorted(tuple(edge) for edge, _ in result.saddles)),
    )


def snapshot(result):
    return {
        "valid": bool(result.valid),
        "error": result.error,
        "f_vector": [len(result.active), len(result.edges), len(result.faces)],
        "class": [len(result.stable), len(result.unstable), len(result.saddles)],
        "stable": [
            sorted(result.faces[index]["cycle"]) for index, _ in result.stable
        ],
        "unstable": [index for index, _ in result.unstable],
        "saddles": [list(edge) for edge, _ in result.saddles],
        "topology_margin": float(result.topology_margin),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=str(SOURCE))
    parser.add_argument("--trust", type=float, default=TRUST)
    parser.add_argument("--prefix", default="recomputed_intrinsic")
    parser.add_argument("--maximum-fraction", type=float, default=1.5)
    parser.add_argument("--plane-tol", type=float, default=PLANE_TOL)
    args = parser.parse_args()
    source_path = Path(args.source)
    if not source_path.is_absolute():
        source_path = HERE / source_path
    plane_tol = args.plane_tol
    four.ACTIVE_PLANE_TOL = plane_tol
    points = slp.load_exact_float(source_path)
    result, values, _faces, _equilibria = slp.state(points, plane_tol)
    modes, best, solve = slp.solve_step(
        points,
        result,
        values,
        args.trust,
        0.15,
        1e-9,
        300.0,
        plane_tol,
    )
    coefficients = np.asarray(best["coefficients"], dtype=float)
    baseline = exact_path.actual.evaluate(points, coplanar_rel=plane_tol)
    if not baseline.valid:
        raise RuntimeError(baseline.error)
    baseline_faces = face_signature(baseline)
    baseline_equilibria = equilibrium_signature(baseline)

    last_same = (0.0, points, baseline)
    first_changed = None
    invalid = []
    for fraction in np.linspace(0.0, args.maximum_fraction, 3001)[1:]:
        fraction = float(fraction)
        candidate = slp.apply_modes(points, modes, fraction * coefficients)
        candidate_result = exact_path.actual.evaluate(candidate, coplanar_rel=plane_tol)
        if not candidate_result.valid:
            invalid.append({"fraction": fraction, "error": candidate_result.error})
            continue
        same = (
            face_signature(candidate_result) == baseline_faces
            and equilibrium_signature(candidate_result) == baseline_equilibria
        )
        if same:
            last_same = (fraction, candidate, candidate_result)
            continue
        first_changed = (fraction, candidate, candidate_result)
        break

    event = None
    if first_changed is not None:
        left, left_points, left_result = last_same
        right, right_points, right_result = first_changed
        for _ in range(80):
            midpoint = (left + right) / 2.0
            candidate = slp.apply_modes(points, modes, midpoint * coefficients)
            candidate_result = exact_path.actual.evaluate(candidate, coplanar_rel=plane_tol)
            same = (
                candidate_result.valid
                and face_signature(candidate_result) == baseline_faces
                and equilibrium_signature(candidate_result) == baseline_equilibria
            )
            if same:
                left, left_points, left_result = midpoint, candidate, candidate_result
            elif candidate_result.valid:
                right, right_points, right_result = midpoint, candidate, candidate_result
            else:
                # Keep an open valid point on each side; the thin invalid band
                # is part of the numerical locator, never accepted as a wall.
                right = midpoint
            if right - left < 1e-12:
                break
        left_file = HERE / f"{args.prefix}_event_before.csv"
        right_file = HERE / f"{args.prefix}_event_after.csv"
        write_csv(left_file, left_points)
        write_csv(right_file, right_points)
        post_faces = face_signature(right_result)
        circuits = candidate_circuits(
            {frozenset(face) for face in baseline_faces},
            {frozenset(face) for face in post_faces},
        )
        event = {
            "fraction_bracket": [left, right],
            "physical_displacement_bracket": [
                left * best["physical_linf"], right * best["physical_linf"]
            ],
            "candidate_circuits": [list(circuit) for circuit in circuits],
            "before_file": left_file.name,
            "after_file": right_file.name,
            "before": snapshot(left_result),
            "after": snapshot(right_result),
            "removed_faces": [
                list(face) for face in sorted(set(baseline_faces) - set(post_faces))
            ],
            "added_faces": [
                list(face) for face in sorted(set(post_faces) - set(baseline_faces))
            ],
        }

    payload = {
        "version": 1,
        "scope": "recomputed intrinsic trust-SLP event locator",
        "source": str(source_path),
        "trust": args.trust,
        "baseline": snapshot(baseline),
        "best": best,
        "solver_summary": {key: value for key, value in solve.items() if key != "branches"},
        "invalid_probe_count": len(invalid),
        "first_invalid_probes": invalid[:20],
        "event": event,
        "conclusion": (
            "first valid adjacent actual cell resolved"
            if event is not None
            else f"no actual signature event through fraction {args.maximum_fraction}"
        ),
    }
    output = HERE / f"{args.prefix}_event.json"
    output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "best": {
            "branch": [best["h67_component"], best["h910_component"]],
            "descent": best["common_fractional_descent"],
            "physical_linf": best["physical_linf"],
        },
        "event": event,
        "invalid_probe_count": len(invalid),
        "output": str(output),
    }, indent=2))


if __name__ == "__main__":
    main()
