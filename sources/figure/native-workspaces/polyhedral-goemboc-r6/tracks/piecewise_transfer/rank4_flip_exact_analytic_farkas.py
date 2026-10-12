#!/usr/bin/env python3
"""Exactify a scaled analytic Farkas active set for the trust-R=.1 LP.

Unlike the finite-difference dual repair, this script starts from the analytic
dlog dual proposed by ``rank4_flip_analytic_dual_search.py``.  Only its sparse
positive support is rebuilt as exact Fraction rows in the frozen 175-column
dyadic chart.  Decimalized nonnegative multipliers are applied, their complete
175-column residual is cancelled with additional available coefficient-box
rows, and the resulting exact Farkas right-hand side is tested for negativity.
"""
from __future__ import annotations

import argparse
import ast
import csv
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

import rank4_flip_exact_directed as dr
import rank4_flip_exact_trust_farkas as tf


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ATLAS = ROOT / "tracks" / "circuit_atlas"
ROOT_LP = ROOT / "tracks" / "root_guarded_lp"
CACHE = ROOT_LP / "row54_flip_guarded_jacobian.npz"
ANALYTIC = HERE / "rank4_flip_175_analytic_guard_rows.npz"
TRUST = Q(1, 10)
BOUND = Q(20)
sys.set_int_max_str_digits(0)


def qs(z):
    return str(z.numerator) if z.denominator == 1 else f"{z.numerator}/{z.denominator}"


def q17(z):
    return Q(format(float(z), ".17g"))


def read_rows_faces():
    rows = {}
    with (ATLAS / "row54_multiwall_flip.csv").open() as f:
        for row in csv.DictReader(f):
            rows[int(row["source_id"])] = tuple(Q(row[k]) for k in ("x", "y", "z"))
    return rows, json.loads((ATLAS / "row54_multiwall_flip_faces.json").read_text())


def add_scaled(acc, row, scale):
    for k, z in enumerate(row):
        acc[k] += scale * z


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--branch", type=int, default=102)
    args = parser.parse_args()
    locator_path = HERE / f"rank4_flip_analytic_dual_branch{args.branch}.json"
    locator = json.loads(locator_path.read_text())
    y0 = locator["multipliers_original_decimal"]
    offsets = {key: tuple(value) for key, value in locator["offsets"].items()}

    saved = np.load(CACHE, allow_pickle=True)
    displacement = np.asarray(saved["displacement"], dtype=float)
    primitive_keys = [ast.literal_eval(str(z)) for z in saved["primitive_keys"]]
    mode_meta = [json.loads(str(z)) for z in saved["mode_meta"]]
    analytic = np.load(ANALYTIC, allow_pickle=True)
    guard_keys = [ast.literal_eval(str(z)) for z in analytic["guard_keys"]]
    guard_kinds = [str(z) for z in analytic["guard_kinds"]]
    deaths = tf.branch_deaths(primitive_keys, args.branch)

    rows, faces = read_rows_faces()
    q, _ = dr.build_mode_jets(rows, displacement)
    ledger = dr.ExactFractionalLedger(q, faces)
    n = displacement.shape[1]
    stationarity = [Q(0)] * n
    rhs = Q(0)
    records = []

    positive_indices = [k for k, z in enumerate(y0) if z > 0.0]
    for count, index in enumerate(positive_indices, 1):
        weight = q17(y0[index])
        if not weight > 0:
            continue
        if offsets["guard"][0] <= index < offsets["guard"][1]:
            local = index - offsets["guard"][0]
            primitive, logrow = ledger.row(guard_keys[local])
            row = tuple(-z for z in logrow)
            b = Q(1)
            label = {"group": "guard", "key": repr(guard_keys[local]), "kind": guard_kinds[local]}
        elif offsets["death"][0] <= index < offsets["death"][1]:
            local = index - offsets["death"][0]
            row = ledger.row(deaths[local])[1]
            b = Q(-1)
            label = {"group": "death", "key": repr(deaths[local])}
        elif offsets["trust_plus"][0] <= index < offsets["trust_plus"][1]:
            local = index - offsets["trust_plus"][0]
            row = tuple(Q.from_float(float(z)) for z in displacement[local])
            b = TRUST
            label = {"group": "trust_plus", "physical_coordinate_row": local}
        elif offsets["trust_minus"][0] <= index < offsets["trust_minus"][1]:
            local = index - offsets["trust_minus"][0]
            row = tuple(-Q.from_float(float(z)) for z in displacement[local])
            b = TRUST
            label = {"group": "trust_minus", "physical_coordinate_row": local}
        elif offsets["box_plus"][0] <= index < offsets["box_plus"][1]:
            local = index - offsets["box_plus"][0]
            row = tuple(Q(1) if k == local else Q(0) for k in range(n))
            b = BOUND
            label = {"group": "box_plus", "column": local, "mode": mode_meta[local]}
        elif offsets["box_minus"][0] <= index < offsets["box_minus"][1]:
            local = index - offsets["box_minus"][0]
            row = tuple(Q(-1) if k == local else Q(0) for k in range(n))
            b = BOUND
            label = {"group": "box_minus", "column": local, "mode": mode_meta[local]}
        else:
            raise AssertionError(index)
        add_scaled(stationarity, row, weight)
        rhs += b * weight
        records.append({**label, "weight_exact": qs(weight), "weight_decimal": float(weight)})
        if count % 40 == 0:
            print("rebuilt exact supported rows", count, "/", len(positive_indices), flush=True)

    # Exact stationarity repair with available +/- coefficient-box rows.
    repair_plus = [max(Q(0), -z) for z in stationarity]
    repair_minus = [max(Q(0), z) for z in stationarity]
    repair_mass = sum(repair_plus, Q(0)) + sum(repair_minus, Q(0))
    rhs_repaired = rhs + BOUND * repair_mass
    for k in range(n):
        stationarity[k] += repair_plus[k] - repair_minus[k]
    assert stationarity == [Q(0)] * n
    decisive = rhs_repaired < 0

    result = {
        "version": 1,
        "type": "exact rational analytic-dlog Farkas certificate",
        "verdict": (
            f"EXACT_ANALYTIC_BRANCH{args.branch}_TRUST_R_0.1_INFEASIBLE_AT_DELTA_1"
            if decisive else
            f"ANALYTIC_BRANCH{args.branch}_EXACT_ACTIVE_SET_REPAIR_NOT_DECISIVE"
        ),
        "scope": (
            "Exact first-order theorem in the frozen 175 cached binary64 modes interpreted as dyadics, "
            "finite-decimal source cell, analytic normalized dlog primitives, physical trust 1/10, "
            "and coefficient box 20. No nonlinear claim."
        ),
        "branch": args.branch,
        "deaths": [repr(z) for z in deaths],
        "locator": locator_path.name,
        "supported_multiplier_count": len(records),
        "exact_stationarity_all_175_columns_zero": True,
        "unrepaired_farkas_rhs_exact": qs(rhs),
        "unrepaired_farkas_rhs_decimal": float(rhs),
        "box_stationarity_repair_mass_exact": qs(repair_mass),
        "box_stationarity_repair_mass_decimal": float(repair_mass),
        "repaired_farkas_rhs_exact": qs(rhs_repaired),
        "repaired_farkas_rhs_decimal": float(rhs_repaired),
        "strictly_negative_farkas_rhs": decisive,
        "conclusion": (
            "The complete analytic directed system A*c<=b at delta=1 is exactly infeasible; "
            "hence some selected guard reaches zero no later than all four named deaths."
            if decisive else
            "This decimalized analytic active set does not retain a negative exact RHS after stationarity repair."
        ),
        "multipliers": records,
        "stationarity_repair": {
            "box_plus": [
                {"column": k, "weight_exact": qs(z), "weight_decimal": float(z), "mode": mode_meta[k]}
                for k, z in enumerate(repair_plus) if z
            ],
            "box_minus": [
                {"column": k, "weight_exact": qs(z), "weight_decimal": float(z), "mode": mode_meta[k]}
                for k, z in enumerate(repair_minus) if z
            ],
        },
    }
    output = HERE / f"rank4_flip_exact_analytic_farkas_branch{args.branch}.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(result["verdict"])
    print("rhs unrepaired/repaired", float(rhs), float(rhs_repaired), "repair mass", float(repair_mass))
    print("output", output)


if __name__ == "__main__":
    main()
