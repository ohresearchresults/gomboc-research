#!/usr/bin/env python3
"""Exact 165D first-jet and linearized-ordering audit for four cancellation pairs."""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

import front_common as fc


def sign(value):
    return (value > 0) - (value < 0)


def q17(value: float) -> Q:
    return Q(format(float(value), ".17g"))


def exact_corrected_minimum_norm(values, jacobian, pivot):
    normalized = np.asarray([
        [float(value / source) for value in row]
        for source, row in zip(values, jacobian)
    ])
    gram = normalized @ normalized.T
    coefficients_float = -normalized.T @ np.linalg.solve(gram, np.ones(2))
    coefficients = [q17(value) for value in coefficients_float]
    residual = [
        source + sum((derivative * coefficient for derivative, coefficient in zip(row, coefficients)), Q(0))
        for source, row in zip(values, jacobian)
    ]
    first, second = pivot
    a, b = jacobian[0][first], jacobian[0][second]
    c, d = jacobian[1][first], jacobian[1][second]
    determinant = a * d - b * c
    correction_first = (-residual[0] * d + b * residual[1]) / determinant
    correction_second = (-a * residual[1] + residual[0] * c) / determinant
    coefficients[first] += correction_first
    coefficients[second] += correction_second
    final_residual = [
        source + sum((derivative * coefficient for derivative, coefficient in zip(row, coefficients)), Q(0))
        for source, row in zip(values, jacobian)
    ]
    if final_residual != [Q(0), Q(0)]:
        raise AssertionError(("first-jet correction failed", final_residual))
    singular_values = np.linalg.svd(normalized, compute_uv=False)
    return coefficients, singular_values.tolist(), determinant


def best_pivot(values, jacobian):
    best = None
    for first in range(len(jacobian[0])):
        for second in range(first + 1, len(jacobian[0])):
            determinant = (
                jacobian[0][first] * jacobian[1][second]
                - jacobian[0][second] * jacobian[1][first]
            )
            if not determinant:
                continue
            score = abs(float(
                determinant / (values[0] * values[1])
            ))
            if best is None or score > best[0]:
                best = (score, first, second, determinant)
    if best is None:
        raise AssertionError("target first-jet rank is below two")
    return best


def main() -> None:
    output = fc.HERE / "reachability_audit.json"
    source_hashes = fc.bindings()
    source = fc.rc.ex.read_rows(fc.SOURCE)
    faces = json.loads(fc.FACES.read_text())
    source_checkpoint = fc.rc.exact_checkpoint(source, faces, fc.rc.FAR_FEATURES)
    labels, _float_modes, mode_names, exact_modes, plane_normal = fc.exact_modes(source)

    zero_velocity = {label: (Q(0), Q(0), Q(0)) for label in source}
    source_targets = fc.target_polynomials(fc.affine_path(source, zero_velocity), faces)
    source_values = {name: polynomial.eval(Q(0)) for name, polynomial in source_targets.items()}
    if any(value <= 0 for value in source_values.values()):
        raise AssertionError({name: sign(value) for name, value in source_values.items()})

    jets = {name: [] for name in source_targets}
    for mode in exact_modes:
        polynomials = fc.target_polynomials(fc.affine_path(source, mode), faces)
        for name, polynomial in polynomials.items():
            if polynomial.eval(Q(0)) != source_values[name]:
                raise AssertionError(("target source drift", name))
            jets[name].append(polynomial.c[1] if polynomial.degree else Q(0))

    pair_records = {}
    for pair_name in fc.PAIR_PRIORITY:
        first_name, second_name = fc.PAIR_SPECS[pair_name]
        values = [source_values[first_name], source_values[second_name]]
        jacobian = [jets[first_name], jets[second_name]]
        score, first_pivot, second_pivot, determinant = best_pivot(values, jacobian)
        coefficients, singular_values, corrected_determinant = exact_corrected_minimum_norm(
            values, jacobian, (first_pivot, second_pivot)
        )
        if corrected_determinant != determinant:
            raise AssertionError("pivot determinant drift")
        velocity = fc.combine_velocity(exact_modes, coefficients)
        path = fc.affine_path(source, velocity)
        target_path = fc.target_polynomials(path, faces)
        for target_name in (first_name, second_name):
            polynomial = target_path[target_name]
            if polynomial.c[0] + polynomial.c[1] != 0:
                raise AssertionError(("target first jet is not zero", pair_name, target_name))

        coordinate_linf = max(
            abs(float(component))
            for xyz in velocity.values()
            for component in xyz
        )
        rows = fc.primitive_first_jets(source, velocity, faces)
        linearized = []
        for row_name, value, derivative, family in rows:
            if not value:
                raise AssertionError(("zero source primitive", row_name))
            if derivative and value * derivative < 0:
                root = -value / derivative
                if root > 0:
                    linearized.append({
                        "name": row_name,
                        "family": family,
                        "root": fc.rc.ex.qs(root),
                        "decimal": float(root),
                    })
        linearized.sort(key=lambda row: (Q(row["root"]), row["name"]))
        target_aliases = set(
            fc.TARGET_ALIASES[first_name] + fc.TARGET_ALIASES[second_name]
        )
        preceding = [row for row in linearized if Q(row["root"]) < Q(1) and row["name"] not in target_aliases]
        at_wall = [row for row in linearized if Q(row["root"]) == Q(1)]

        coefficient_packet = {
            repr(mode_names[index]): fc.rc.ex.qs(value)
            for index, value in enumerate(coefficients)
            if value
        }
        pair_records[pair_name] = {
            "targets": [first_name, second_name],
            "target_aliases": sorted(target_aliases),
            "source_values": {
                first_name: fc.rc.ex.qs(values[0]),
                second_name: fc.rc.ex.qs(values[1]),
            },
            "exact_rank": 2,
            "pivot_modes": [list(mode_names[first_pivot]), list(mode_names[second_pivot])],
            "pivot_determinant": fc.rc.ex.qs(determinant),
            "normalized_pivot_score": score,
            "normalized_singular_values": singular_values,
            "coordinate_linf": coordinate_linf,
            "active_mode_count": len(coefficient_packet),
            "coefficient_digest": fc.canonical_hash(coefficient_packet),
            "coefficients": coefficient_packet,
            "primitive_count": len(rows),
            "linearized_positive_root_count": len(linearized),
            "preceding_non_target_count": len(preceding),
            "preceding_non_target_events": preceding[:40],
            "linearized_wall_family": at_wall,
            "first_linearized_events": linearized[:40],
            "endpoint_trials_deferred_to_conditioned_proposer": True,
        }

    eligible = [
        name for name in fc.PAIR_PRIORITY
        if pair_records[name]["exact_rank"] == 2
        and pair_records[name]["preceding_non_target_count"] == 0
    ]
    selected = eligible[0] if eligible else min(
        fc.PAIR_PRIORITY,
        key=lambda name: (
            pair_records[name]["preceding_non_target_count"],
            fc.PAIR_PRIORITY.index(name),
        ),
    )
    payload = {
        "version": 1,
        "scope": (
            "Exact 2x165 first-jet reachability and full 7,922-row linearized "
            "ordering audit for four post-relay codimension-two cancellations."
        ),
        "source_hashes": {
            **source_hashes,
            fc.rc.relative(Path(__file__)): fc.sha256(Path(__file__)),
            fc.rc.relative(fc.HERE / "front_common.py"): fc.sha256(fc.HERE / "front_common.py"),
        },
        "source_checkpoint": source_checkpoint,
        "mode_count": len(exact_modes),
        "base_plane_normal": plane_normal.tolist(),
        "target_source_values": {
            name: fc.rc.ex.qs(value) for name, value in source_values.items()
        },
        "pairs": pair_records,
        "eligible_without_linearized_predecessor": eligible,
        "selected_target": selected,
        "selection_rule": (
            "First semantic-priority pair with exact rank two and no earlier "
            "non-target first-jet root; otherwise fewest exact predecessors."
        ),
        "verdict": "EXACT_POST_RELAY_FIRST_JET_REACHABILITY_AUDIT_PASS",
    }
    output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "verdict": payload["verdict"],
        "eligible": eligible,
        "selected_target": selected,
        "pair_summary": {
            name: {
                "rank": row["exact_rank"],
                "preceding": row["preceding_non_target_count"],
                "coordinate_linf": row["coordinate_linf"],
                "endpoint_trials_deferred": row[
                    "endpoint_trials_deferred_to_conditioned_proposer"
                ],
            }
            for name, row in pair_records.items()
        },
        "output": output.name,
    }, indent=2))


if __name__ == "__main__":
    main()
