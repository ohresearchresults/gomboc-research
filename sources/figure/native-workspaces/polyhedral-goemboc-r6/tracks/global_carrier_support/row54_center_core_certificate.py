#!/usr/bin/env python3
"""Small exhaustive fixed-geometry obstruction for the row-54 carrier cell.

The target asks that row 54 cease to be an unstable vertex while the enlarged
base stays stable, row 8 stays unstable, every other face/vertex is nonpositive
and every edge is nonsaddle.  Row 54 has four incident edges, hence precisely
four possible negative support witnesses.  For each witness this script solves
the remaining (small) disjunctive linear problem and maximises one common,
dimensionless strict margin.  Every branch has optimum zero.

This is a numerical certificate for the supplied floating-point geometry, not
an exact rational theorem and not an obstruction to changing the boundary.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, linprog, milp
from scipy.sparse import coo_matrix


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
import fixed_geometry_center_milp as model  # noqa: E402


DEFAULT_POINTS = ROOT / "tracks/circuit_atlas/row54_endpoint_rebuilt.csv"
DEFAULT_FACES = ROOT / "tracks/circuit_atlas/row54_endpoint_rebuilt_faces.json"
DEFAULT_OUTPUT = HERE / "row54_endpoint_center_core.json"
BASE = tuple(range(17)) + (54,)

# These cores were found by constraint generation and deletion.  Together
# with the direct conditions, each list is sufficient for its row-54 witness.
BRANCH_CORES = {
    0: (
        "nonsaddle:[2, 3]",
        "nonstable:[1, 2, 88]",
        "nonstable:[1, 54, 88]",
    ),
    1: (
        "nonunstable:1",
        "nonsaddle:[0, 16]",
        "nonstable:[0, 54, 257]",
    ),
    2: (),
    3: (),
}


def solve_branch(points, direct, exclusions, witness, names):
    by_name = dict(exclusions)
    selected = [(name, by_name[name]) for name in names]
    lower_centre, upper_centre = points.min(axis=0), points.max(axis=0)
    binary_count = sum(len(components) for _, components in selected)
    variable_count = 4 + binary_count
    lower = np.r_[lower_centre, -2.0, np.zeros(binary_count)]
    upper = np.r_[upper_centre, 2.0, np.ones(binary_count)]
    integrality = np.r_[np.zeros(4), np.ones(binary_count)]
    objective = np.zeros(variable_count)
    objective[3] = -1.0

    row_indices, column_indices, data, right = [], [], [], []
    row = 0

    # Positive direct component a.c+b >= m.
    for component in [item for _, item in direct]:
        for coordinate in range(3):
            row_indices.append(row)
            column_indices.append(coordinate)
            data.append(-component.coefficients[coordinate])
        row_indices.append(row)
        column_indices.append(3)
        data.append(1.0)
        right.append(component.constant)
        row += 1

    # The chosen row-54 component must be negative: a.c+b <= -m.
    for coordinate in range(3):
        row_indices.append(row)
        column_indices.append(coordinate)
        data.append(witness.coefficients[coordinate])
    row_indices.append(row)
    column_indices.append(3)
    data.append(1.0)
    right.append(-witness.constant)
    row += 1

    binary_offset = 4
    for _, components in selected:
        selectors = []
        for component in components:
            selector = binary_offset
            binary_offset += 1
            selectors.append(selector)
            big_m = max(
                1.0,
                component.maximum_on_box(lower_centre, upper_centre) + 3.0,
            )
            for coordinate in range(3):
                row_indices.append(row)
                column_indices.append(coordinate)
                data.append(component.coefficients[coordinate])
            row_indices.extend((row, row))
            column_indices.extend((3, selector))
            data.extend((1.0, big_m))
            right.append(big_m - component.constant)
            row += 1
        for selector in selectors:
            row_indices.append(row)
            column_indices.append(selector)
            data.append(-1.0)
        right.append(-1.0)
        row += 1

    matrix = coo_matrix(
        (data, (row_indices, column_indices)),
        shape=(row, variable_count),
    ).tocsr()
    result = milp(
        objective,
        integrality=integrality,
        bounds=Bounds(lower, upper),
        constraints=LinearConstraint(matrix, -np.inf, np.asarray(right)),
        options={"mip_rel_gap": 1e-12, "presolve": True},
    )
    assert result.x is not None
    return {
        "status": int(result.status),
        "message": str(result.message),
        "mip_gap": None if result.mip_gap is None else float(result.mip_gap),
        "maximum_common_margin": float(result.x[3]),
        "centre": result.x[:3].tolist(),
        "binary_count": binary_count,
    }


def negative(component):
    return model.Affine(-component.coefficients, -component.constant)


def gordan_certificate_atlas(direct, exclusions, witness, names):
    """Enumerate every disjunct and certify that its strict cone is empty.

    For signed affine guards h_k(c)>0, a nonnegative vector lambda with
    sum(lambda)=1 and sum(lambda_k h_k) identically zero is a direct Gordan
    alternative: all h_k cannot be strictly positive simultaneously.
    """
    by_name = dict(exclusions)
    choices = itertools.product(
        *(range(len(by_name[name])) for name in names)
    ) if names else [()]
    certificates = []
    for choice in choices:
        affine_rows = list(direct)
        affine_rows.append(("kill_U54_branch", negative(witness)))
        selected = []
        for feature, offset in zip(names, choice):
            selected.append({"feature": feature, "component": offset})
            affine_rows.append((
                f"{feature}:component:{offset}",
                negative(by_name[feature][offset]),
            ))
        matrix = np.asarray([
            [*component.coefficients, component.constant]
            for _, component in affine_rows
        ]).T
        equalities = np.vstack((matrix, np.ones(len(affine_rows))))
        target = np.r_[np.zeros(4), 1.0]
        result = linprog(
            np.zeros(len(affine_rows)),
            A_eq=equalities,
            b_eq=target,
            bounds=(0.0, None),
            method="highs",
        )
        terms = []
        residual = None
        if result.x is not None:
            for offset in np.flatnonzero(result.x > 1e-9):
                terms.append({
                    "guard": affine_rows[int(offset)][0],
                    "weight": float(result.x[offset]),
                })
            residual = (equalities @ result.x - target).tolist()
        certificates.append({
            "selected_negative_components": selected,
            "success": bool(result.success),
            "message": str(result.message),
            "positive_terms": terms,
            "identity_residual_coefficients_constant_and_weight_sum": residual,
            "maximum_absolute_residual": None if residual is None else float(
                np.max(np.abs(residual))
            ),
        })
    return certificates


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--points", type=Path, default=DEFAULT_POINTS)
    parser.add_argument("--faces", type=Path, default=DEFAULT_FACES)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    rows, _, points, _, _, _, neighbours, _ = model.load(args.points, args.faces)
    points2, direct, exclusions = model.component_system(
        args.points, args.faces, BASE, (8,)
    )
    assert np.array_equal(points, points2)
    row54_neighbours = sorted(neighbours[54])
    witnesses = dict(exclusions)["nonunstable:54"]
    assert len(row54_neighbours) == len(witnesses) == 4

    branches = []
    for offset, witness in enumerate(witnesses):
        core = BRANCH_CORES[offset]
        result = solve_branch(points, direct, exclusions, witness, core)
        gordan = gordan_certificate_atlas(
            direct, exclusions, witness, core
        )
        deletion_checks = []
        for name in core:
            reduced = tuple(other for other in core if other != name)
            deletion_checks.append({
                "removed": name,
                "maximum_common_margin": solve_branch(
                    points, direct, exclusions, witness, reduced
                )["maximum_common_margin"],
            })
        branches.append({
            "component_offset": offset,
            "neighbour": row54_neighbours[offset],
            "meaning": f"dot(c-x54, x{row54_neighbours[offset]}-x54) < 0",
            "core_exclusions": list(core),
            "solve": result,
            "single_deletion_checks": deletion_checks,
            "gordan_alternative": {
                "combination_count": len(gordan),
                "every_combination_certified": all(
                    certificate["success"] for certificate in gordan
                ),
                "maximum_absolute_identity_residual": max(
                    certificate["maximum_absolute_residual"]
                    for certificate in gordan
                    if certificate["maximum_absolute_residual"] is not None
                ),
                "certificates": gordan,
            },
        })

    maximum = max(branch["solve"]["maximum_common_margin"] for branch in branches)
    record = {
        "version": 1,
        "scope": "fixed boundary geometry and arbitrary proposed centre",
        "points": str(args.points.resolve()),
        "faces": str(args.faces.resolve()),
        "target_base": list(BASE),
        "target_unstable_vertices": [8],
        "row54_neighbours": row54_neighbours,
        "branches": branches,
        "maximum_over_all_row54_negative_witness_branches": maximum,
        "strict_target_centre_cell_exists": bool(maximum > 1e-9),
        "interpretation": (
            "Every possible strict witness that kills U54 has optimum zero; "
            "therefore no strict target centre exists for this fixed geometry."
        ),
    }
    args.output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "strict_target_centre_cell_exists": record["strict_target_centre_cell_exists"],
        "maximum_over_branches": maximum,
        "branches": [
            {
                "neighbour": branch["neighbour"],
                "maximum_common_margin": branch["solve"]["maximum_common_margin"],
                "gordan_combinations": branch["gordan_alternative"]["combination_count"],
                "all_gordan_certified": branch["gordan_alternative"]["every_combination_certified"],
                "maximum_gordan_residual": branch["gordan_alternative"]["maximum_absolute_identity_residual"],
            }
            for branch in branches
        ],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
