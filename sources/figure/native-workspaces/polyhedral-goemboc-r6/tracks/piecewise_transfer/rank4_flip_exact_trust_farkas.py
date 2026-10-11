#!/usr/bin/env python3
"""Exact Farkas audit of branch 4 in the physical trust ball R=0.1.

The cached finite-difference LP is used only to propose nonnegative dual
weights.  Every proposed weight is rationalized, all 6301 guard rows and four
death rows are rebuilt from the analytic exact-dyadic 175-mode first jet, and
the physical displacement rows are the cached binary64 values interpreted as
exact dyadics.

Any residual stationarity in a proposed dual is cancelled *exactly* with the
available coefficient-box inequalities +/-c_j <= 20.  Consequently the final
certificate has nonnegative rational multipliers, zero stationarity in every
one of the 175 columns, and an exact dual lower bound.  If that bound exceeds
one, all four deaths cannot occur while every selected guard survives within
the physical coordinate trust box |D c|_infinity <= 0.1.
"""
from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

import rank4_flip_exact_directed as dr


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ATLAS = ROOT / "tracks" / "circuit_atlas"
ROOT_LP = ROOT / "tracks" / "root_guarded_lp"
CACHE = ROOT_LP / "row54_flip_guarded_jacobian.npz"
SOURCE = ATLAS / "row54_multiwall_flip.csv"
FACES_SOURCE = ATLAS / "row54_multiwall_flip_faces.json"
OUTPUT = HERE / "rank4_flip_exact_trust_farkas.json"
ANALYTIC_CACHE = HERE / "rank4_flip_175_analytic_guard_rows.npz"

# Exact centroid/log-derivative elimination can legitimately create primitive
# integers longer than Python's default human-facing conversion guard.
sys.set_int_max_str_digits(0)

TRUST = Q(1, 10)
BOUND = Q(20)


def qs(z: Q):
    return str(z.numerator) if z.denominator == 1 else f"{z.numerator}/{z.denominator}"


def q17(z: float):
    return Q(format(float(z), ".17g"))


def qbinary64(z: float):
    return Q.from_float(float(z))


def read_rows_faces():
    rows = {}
    with SOURCE.open() as f:
        for row in csv.DictReader(f):
            rows[int(row["source_id"])] = tuple(Q(row[k]) for k in ("x", "y", "z"))
    return rows, json.loads(FACES_SOURCE.read_text())


def add_scaled(acc, row, scale):
    if not scale:
        return
    for k, z in enumerate(row):
        acc[k] += scale * z


def death_packets(keys):
    face = [key for key in keys if key[0] == "face" and frozenset(key[1]) == dr.EXTRA_FACE]
    vertex = [key for key in keys if key[0] == "vertex" and key[1] == dr.EXTRA_U]
    h45 = [key for key in keys if key[0] == "edge" and key[1] == (4, 5)]
    h1213 = [key for key in keys if key[0] == "edge" and key[1] == (12, 13)]
    if [len(face), len(vertex), len(h45), len(h1213)] != [3, 3, 4, 4]:
        raise AssertionError([len(face), len(vertex), len(h45), len(h1213)])
    return face, vertex, h45, h1213


def branch_deaths(keys, branch_index):
    packets = death_packets(keys)
    atlas = []
    for f in packets[0]:
        for u in packets[1]:
            for h1 in packets[2]:
                for h2 in packets[3]:
                    atlas.append([f, u, h1, h2])
    if len(atlas) != 144 or not 0 <= branch_index < 144:
        raise ValueError(branch_index)
    return atlas[branch_index]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--branch", type=int, default=4)
    parser.add_argument("--output")
    args = parser.parse_args()
    output_path = Path(args.output) if args.output else (
        OUTPUT if args.branch == 4 else HERE / f"rank4_flip_exact_trust_farkas_branch{args.branch}.json"
    )
    saved = np.load(CACHE, allow_pickle=True)
    jacobian = np.asarray(saved["jacobian"], dtype=float)
    displacement = np.asarray(saved["displacement"], dtype=float)
    keys = [ast.literal_eval(str(z)) for z in saved["primitive_keys"]]
    values = {key: float(v) for key, v in zip(keys, saved["primitive_values"])}
    key_index = {key: k for k, key in enumerate(keys)}
    mode_meta = [json.loads(str(z)) for z in saved["mode_meta"]]
    guards = dr.selected_guards(keys, values)
    deaths = branch_deaths(keys, args.branch)
    n = displacement.shape[1]

    # Reproduce the branch-4 R=.1 finite-difference solve only to obtain the
    # full dual proposal (the parent JSON intentionally reports only its top
    # guard entries).
    guard_float = np.asarray([
        -sign * jacobian[key_index[key]] / max(abs(values[key]), 1e-12)
        for key, sign, _ in guards
    ])
    death_float = np.asarray([
        jacobian[key_index[key]] / values[key] for key in deaths
    ])
    a_ub = np.vstack((
        np.hstack((guard_float, -np.ones((len(guards), 1)))),
        np.hstack((displacement, np.zeros((len(displacement), 1)))),
        np.hstack((-displacement, np.zeros((len(displacement), 1)))),
        np.hstack((death_float, np.zeros((len(deaths), 1)))),
    ))
    b_ub = np.r_[
        np.zeros(len(guards)),
        np.full(len(displacement), float(TRUST)),
        np.full(len(displacement), float(TRUST)),
        np.full(len(deaths), -1.0),
    ]
    solve = linprog(
        np.r_[np.zeros(n), 1.0], A_ub=a_ub, b_ub=b_ub,
        bounds=[(-float(BOUND), float(BOUND))] * n + [(-1000.0, 1000.0)],
        method="highs-ipm",
    )
    if not solve.success or solve.ineqlin.marginals is None:
        raise RuntimeError(solve.message)
    proposal = np.maximum(0.0, -np.asarray(solve.ineqlin.marginals, dtype=float))
    ng = len(guards)
    nd = len(displacement)
    guard_y0 = proposal[:ng]
    plus_trust_y0 = proposal[ng:ng + nd]
    minus_trust_y0 = proposal[ng + nd:ng + 2 * nd]
    death_y0 = proposal[ng + 2 * nd:]
    print("finite-difference dual proposal delta", solve.x[-1],
          "sum guard", np.sum(guard_y0), "nonzero", np.sum(proposal > 0), flush=True)

    # Exact analytic fractional rows in the frozen exact-dyadic mode chart.
    rows, faces = read_rows_faces()
    q, ids = dr.build_mode_jets(rows, displacement)
    ledger = dr.ExactFractionalLedger(q, faces)
    guard_rows = []
    for count, (key, sign, kind) in enumerate(guards, 1):
        primitive, logrow = ledger.row(key)
        if (primitive > 0) != (sign > 0):
            raise AssertionError(("primitive sign mismatch", key, primitive, sign))
        guard_rows.append(tuple(-z for z in logrow))  # fractional loss
        if count % 1000 == 0:
            print("built exact guard rows", count, "/", ng, flush=True)
    death_rows = [ledger.row(key)[1] for key in deaths]
    displacement_rows = [
        tuple(qbinary64(z) for z in displacement[r]) for r in range(nd)
    ]
    np.savez_compressed(
        ANALYTIC_CACHE,
        guard_loss=np.asarray([[float(z) for z in row] for row in guard_rows]),
        guard_keys=np.asarray([repr(z[0]) for z in guards], dtype=object),
        guard_kinds=np.asarray([z[2] for z in guards], dtype=object),
        displacement=displacement,
    )

    # Rationalize and normalize so the delta stationarity equation is exact:
    # sum guard multipliers = 1.
    guard_y = [q17(z) for z in guard_y0]
    plus_trust_y = [q17(z) for z in plus_trust_y0]
    minus_trust_y = [q17(z) for z in minus_trust_y0]
    death_y = [q17(z) for z in death_y0]
    scale = sum(guard_y, Q(0))
    if scale <= 0:
        raise AssertionError("no positive guard dual mass")
    guard_y = [z / scale for z in guard_y]
    plus_trust_y = [z / scale for z in plus_trust_y]
    minus_trust_y = [z / scale for z in minus_trust_y]
    death_y = [z / scale for z in death_y]
    assert sum(guard_y, Q(0)) == 1

    stationarity = [Q(0)] * n
    for y, row in zip(guard_y, guard_rows):
        add_scaled(stationarity, row, y)
    for y, row in zip(plus_trust_y, displacement_rows):
        add_scaled(stationarity, row, y)
    for y, row in zip(minus_trust_y, displacement_rows):
        add_scaled(stationarity, row, -y)
    for y, row in zip(death_y, death_rows):
        add_scaled(stationarity, row, y)

    # Exact nonnegative box multipliers cancel the residual componentwise.
    plus_box_y = [max(Q(0), -z) for z in stationarity]   # +e_j row
    minus_box_y = [max(Q(0), z) for z in stationarity]   # -e_j row
    for k in range(n):
        stationarity[k] += plus_box_y[k] - minus_box_y[k]
    if stationarity != [Q(0)] * n:
        raise AssertionError("box correction did not annihilate stationarity")

    trust_mass = sum(plus_trust_y, Q(0)) + sum(minus_trust_y, Q(0))
    box_mass = sum(plus_box_y, Q(0)) + sum(minus_box_y, Q(0))
    death_mass = sum(death_y, Q(0))
    lower_bound = death_mass - TRUST * trust_mass - BOUND * box_mass
    decisive = lower_bound > 1

    # Exact postcheck of the finite-difference primal locator in the analytic
    # template.  This is diagnostic only; a strict all-row pass would itself
    # be an exact rational upper witness.
    primal_c = [qbinary64(z) for z in solve.x[:n]]
    primal_death_slacks = [-(Q(1) + dr.dotq(row, primal_c)) for row in death_rows]
    primal_guard_survival = [Q(1) - dr.dotq(row, primal_c) for row in guard_rows]
    primal_trust_slacks = []
    for row in displacement_rows:
        value = dr.dotq(row, primal_c)
        primal_trust_slacks.append(TRUST - abs(value))
    primal_box_slacks = [BOUND - abs(z) for z in primal_c]
    primal_exact_pass = (
        min(primal_death_slacks) >= 0
        and min(primal_guard_survival) > 0
        and min(primal_trust_slacks) >= 0
        and min(primal_box_slacks) >= 0
    )

    nonzero_guard = [k for k, z in enumerate(guard_y) if z]
    guard_order = sorted(nonzero_guard, key=lambda k: guard_y[k], reverse=True)
    nonzero_trust_plus = [k for k, z in enumerate(plus_trust_y) if z]
    nonzero_trust_minus = [k for k, z in enumerate(minus_trust_y) if z]
    nonzero_box_plus = [k for k, z in enumerate(plus_box_y) if z]
    nonzero_box_minus = [k for k, z in enumerate(minus_box_y) if z]
    digest = hashlib.sha256()
    for group in (guard_y, plus_trust_y, minus_trust_y, death_y, plus_box_y, minus_box_y):
        digest.update("|".join(qs(z) for z in group).encode())
        digest.update(b"\n")

    result = {
        "version": 1,
        "type": "exact rational Gordan/Farkas certificate in the physical trust box",
        "verdict": (
            f"EXACT_BRANCH{args.branch}_TRUST_R_0.1_GUARD_BEFORE_ALL_FOUR_DEATHS"
            if decisive else
            f"BRANCH{args.branch}_EXACT_CORRECTED_DUAL_LOWER_BOUND_NOT_DECISIVE"
        ),
        "scope": (
            "Exact analytic first-order theorem for the finite-decimal cell and the frozen "
            "175 cached binary64 modes interpreted as dyadics. It does not assert nonlinear behavior."
        ),
        "branch_index": args.branch,
        "death_components": [repr(key) for key in deaths],
        "selected_guard_count": ng,
        "physical_displacement_row_count": nd,
        "mode_count": n,
        "trust_radius_exact": qs(TRUST),
        "coefficient_bound_exact": qs(BOUND),
        "finite_difference_dual_locator": {
            "delta": float(solve.x[-1]),
            "max_coordinate_displacement": float(np.max(np.abs(displacement @ solve.x[:n]))),
            "sum_guard_dual_before_exact_normalization": float(np.sum(guard_y0)),
            "exact_analytic_postcheck": {
                "all_inequalities_pass": primal_exact_pass,
                "minimum_death_slack_decimal": float(min(primal_death_slacks)),
                "minimum_guard_survival_decimal": float(min(primal_guard_survival)),
                "minimum_trust_slack_decimal": float(min(primal_trust_slacks)),
                "minimum_box_slack_decimal": float(min(primal_box_slacks)),
                "worst_guard": repr(guards[min(range(ng), key=lambda k: primal_guard_survival[k])][0]),
            },
        },
        "exact_certificate": {
            "system": [
                "fractional guard loss <= delta for all 6301 selected guards",
                "fractional selected death derivative <= -1 for all four deaths",
                "abs(D*c) <= 1/10 in all 183 physical coordinate rows",
                "abs(c_j) <= 20 in all 175 mode coefficients",
            ],
            "guard_multiplier_sum_exact": qs(sum(guard_y, Q(0))),
            "death_multiplier_mass_exact": qs(death_mass),
            "trust_multiplier_mass_exact": qs(trust_mass),
            "box_correction_multiplier_mass_exact": qs(box_mass),
            "dual_delta_lower_bound_exact": qs(lower_bound),
            "dual_delta_lower_bound_decimal": float(lower_bound),
            "strictly_greater_than_one": decisive,
            "stationarity_all_175_columns_exact_zero": True,
            "conclusion": (
                "Any first-order coefficient vector satisfying all four named deaths and both trust boxes "
                "has max normalized protected/witness/support guard loss at least the stated lower bound, "
                + ("so some guard reaches zero strictly before all four deaths."
                   if decisive else
                   "but this particular corrected dual does not decide whether that loss reaches one.")
            ),
        },
        "multipliers": {
            "guard_nonzero": [
                {"index": k, "key": repr(guards[k][0]), "kind": guards[k][2],
                 "weight_exact": qs(guard_y[k]), "weight_decimal": float(guard_y[k])}
                for k in guard_order
            ],
            "death": [
                {"death": repr(key), "weight_exact": qs(z), "weight_decimal": float(z)}
                for key, z in zip(deaths, death_y)
            ],
            "trust_plus_nonzero": [
                {"physical_coordinate_row": k, "weight_exact": qs(plus_trust_y[k]),
                 "weight_decimal": float(plus_trust_y[k])}
                for k in nonzero_trust_plus
            ],
            "trust_minus_nonzero": [
                {"physical_coordinate_row": k, "weight_exact": qs(minus_trust_y[k]),
                 "weight_decimal": float(minus_trust_y[k])}
                for k in nonzero_trust_minus
            ],
            "box_plus_corrections_nonzero": [
                {"column": k, "mode": mode_meta[k], "weight_exact": qs(plus_box_y[k]),
                 "weight_decimal": float(plus_box_y[k])}
                for k in nonzero_box_plus
            ],
            "box_minus_corrections_nonzero": [
                {"column": k, "mode": mode_meta[k], "weight_exact": qs(minus_box_y[k]),
                 "weight_decimal": float(minus_box_y[k])}
                for k in nonzero_box_minus
            ],
        },
        "multiplier_sha256": digest.hexdigest(),
    }
    output_path.write_text(json.dumps(result, indent=2) + "\n")
    print(result["verdict"])
    print("exact delta lower bound", float(lower_bound))
    print("death/trust/box masses", float(death_mass), float(trust_mass), float(box_mass))
    print("nonzero guard/trust+/trust-/box+/box-", len(nonzero_guard),
          len(nonzero_trust_plus), len(nonzero_trust_minus),
          len(nonzero_box_plus), len(nonzero_box_minus))
    print("output", output_path)


if __name__ == "__main__":
    main()
