#!/usr/bin/env python3
"""Exact two-face/trust Farkas reduction for the weakest analytic branch 13.

Branch 13 is dominated by the selected death component
S[198,243,244] at edge (198,243) and the protected nonstable witness on the
adjacent face [198,242,243] at the same edge.  Work directly in the 183
physical coordinate velocities.  With death multiplier 1 and adjacent-guard
multiplier x>=0, exact stationarity is repaired by the +/- physical trust rows
with total mass ||p_death - x p_guard||_1.  The Farkas right-hand side is

    F(x) = x - 1 + (1/10) ||p_death - x p_guard||_1.

This convex piecewise-linear function attains its minimum at x=0 or at one of
the exact rational component ratios.  Exhausting those breakpoints gives an
exact global certificate without an LP solver or numerical active set.
"""
from __future__ import annotations

import csv
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import rank4_flip_exact_directed as dr
import rank4_flip_exact_ledger as ex


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ATLAS = ROOT / "tracks" / "circuit_atlas"
OUTPUT = HERE / "rank4_flip_exact_pair_farkas_branch13.json"
TRUST = Q(1, 10)
sys.set_int_max_str_digits(0)


def qs(z):
    return str(z.numerator) if z.denominator == 1 else f"{z.numerator}/{z.denominator}"


def read_rows_faces():
    rows = {}
    with (ATLAS / "row54_multiwall_flip.csv").open() as f:
        for row in csv.DictReader(f):
            rows[int(row["source_id"])] = tuple(Q(row[k]) for k in ("x", "y", "z"))
    return rows, json.loads((ATLAS / "row54_multiwall_flip_faces.json").read_text())


def physical_identity_jets(rows):
    ids = sorted(rows)
    n = 3 * len(ids)
    ex.D = n
    q = {}
    for ii, i in enumerate(ids):
        q[i] = tuple(
            ex.J(rows[i][axis], tuple(
                Q(1) if k == 3 * ii + axis else Q(0) for k in range(n)
            ))
            for axis in range(3)
        )
    return q, ids


def main():
    rows, faces = read_rows_faces()
    q, ids = physical_identity_jets(rows)
    ledger = dr.ExactFractionalLedger(q, faces)
    death_key = ("face", (198, 243, 244), (198, 243))
    adjacent_key = ("face", (198, 242, 243), (198, 243))
    p_death = ledger.row(death_key)[1]
    p_adjacent = ledger.row(adjacent_key)[1]
    # Guard loss row is -p_adjacent.  The combined non-trust stationarity row
    # at multipliers (death=1, guard=x) is p_death - x*p_adjacent.
    candidates = {Q(0)}
    for a, b in zip(p_death, p_adjacent):
        if b and a / b >= 0:
            candidates.add(a / b)

    def objective(x):
        residual = tuple(a - x * b for a, b in zip(p_death, p_adjacent))
        return x - 1 + TRUST * sum((abs(z) for z in residual), Q(0)), residual

    best_x = None
    best_value = None
    best_residual = None
    for x in candidates:
        value, residual = objective(x)
        if best_value is None or value < best_value:
            best_x, best_value, best_residual = x, value, residual
    assert best_x is not None and best_value is not None
    decisive = best_value < 0

    trust_plus = [max(Q(0), -z) for z in best_residual]   # +u_k row
    trust_minus = [max(Q(0), z) for z in best_residual]  # -u_k row
    stationarity = [
        p_death[k] - best_x * p_adjacent[k] + trust_plus[k] - trust_minus[k]
        for k in range(len(p_death))
    ]
    assert stationarity == [Q(0)] * len(stationarity)
    rhs_check = best_x - 1 + TRUST * (
        sum(trust_plus, Q(0)) + sum(trust_minus, Q(0))
    )
    assert rhs_check == best_value

    result = {
        "version": 1,
        "type": "exact one-dimensional adjacent-face/trust Farkas certificate",
        "verdict": (
            "EXACT_BRANCH13_ADJACENT_FACE_GUARD_BEFORE_FOUR_DEATH_PACKET"
            if decisive else
            "BRANCH13_TWO_FACE_TRUST_REDUCTION_NOT_NEGATIVE"
        ),
        "scope": (
            "Exact analytic first-order certificate in all 183 physical coordinate velocities "
            "with |u_k|<=1/10. Because every frozen 175-mode displacement maps into these "
            "physical velocities, the certificate also applies to the requested 175-column chart; "
            "coefficient-box rows are not needed."
        ),
        "branch": 13,
        "branch_deaths": [
            repr(death_key),
            "('vertex', 2, 1)",
            "('edge', (4, 5), 'beta2')",
            "('edge', (12, 13), 'one_minus_t')",
        ],
        "used_necessary_death": repr(death_key),
        "used_adjacent_guard": repr(adjacent_key),
        "candidate_breakpoint_count": len(candidates),
        "death_multiplier_exact": "1",
        "adjacent_guard_multiplier_exact": qs(best_x),
        "adjacent_guard_multiplier_decimal": float(best_x),
        "trust_multiplier_mass_exact": qs(sum(abs(z) for z in best_residual)),
        "trust_multiplier_mass_decimal": float(sum(abs(z) for z in best_residual)),
        "farkas_rhs_exact": qs(best_value),
        "farkas_rhs_decimal": float(best_value),
        "strictly_negative_rhs": decisive,
        "stationarity_all_183_physical_columns_exact_zero": True,
        "conclusion": (
            "The selected face death alone is incompatible with survival of its adjacent anti-face "
            "guard inside the physical R=.1 trust box. Therefore the full four-death branch is infeasible."
            if decisive else
            "This exact two-row reduction does not by itself obstruct the branch."
        ),
        "trust_plus_nonzero": [
            {"physical_coordinate_row": k, "source_id": ids[k // 3], "axis": k % 3,
             "weight_exact": qs(z), "weight_decimal": float(z)}
            for k, z in enumerate(trust_plus) if z
        ],
        "trust_minus_nonzero": [
            {"physical_coordinate_row": k, "source_id": ids[k // 3], "axis": k % 3,
             "weight_exact": qs(z), "weight_decimal": float(z)}
            for k, z in enumerate(trust_minus) if z
        ],
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    print(result["verdict"])
    print("breakpoints", len(candidates), "x", float(best_x), "rhs", float(best_value))
    print("output", OUTPUT)


if __name__ == "__main__":
    main()
