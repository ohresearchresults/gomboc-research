#!/usr/bin/env python3
"""Literal exact Farkas coverage of all 144 clean-flip component branches.

The numerical analytic atlas is used only as an active-set locator.  For each
branch, every positive locator multiplier is converted to an exact decimal
rational and its supported row is rebuilt in the frozen 175-column dyadic
first-jet chart.  The remaining stationarity residual is cancelled exactly by
the already-present +/- coefficient-box rows.  Consequently a negative
repaired RHS is a standalone rational Farkas certificate for that branch.

Branches whose IPM rays are at solver-tolerance scale can be overridden by a
revised-simplex locator.  The output is deliberately a compact coverage
ledger: it records the exact RHS and repair mass for every branch, but not the
large multiplier vectors already preserved in the locator artifacts.
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

import rank4_flip_exact_directed as dr
import rank4_flip_exact_trust_farkas as tf


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ATLAS = ROOT / "tracks" / "circuit_atlas"
ROOT_LP = ROOT / "tracks" / "root_guarded_lp"
CACHE = ROOT_LP / "row54_flip_guarded_jacobian.npz"
ANALYTIC = HERE / "rank4_flip_175_analytic_guard_rows.npz"
LOCATOR_ATLAS = HERE / "rank4_flip_analytic_dual_atlas_ipm_weights.json"
OUTPUT = HERE / "rank4_flip_exact_coverage.json"

TRUST = Q(1, 10)
BOUND = Q(20)
REVISED_OVERRIDES = (9, 13, 54, 55)

# Exact normalized derivatives have legitimately enormous integers.
sys.set_int_max_str_digits(0)


def qs(z: Q) -> str:
    return str(z.numerator) if z.denominator == 1 else f"{z.numerator}/{z.denominator}"


def q17(z: float) -> Q:
    return Q(format(float(z), ".17g"))


def qdecimal(z: Q) -> float:
    """A compact diagnostic decimal; the exact string remains authoritative."""
    return float(z)


def read_rows_faces():
    rows = {}
    with (ATLAS / "row54_multiwall_flip.csv").open() as handle:
        for row in csv.DictReader(handle):
            rows[int(row["source_id"])] = tuple(Q(row[k]) for k in ("x", "y", "z"))
    return rows, json.loads((ATLAS / "row54_multiwall_flip_faces.json").read_text())


def add_scaled(acc: list[Q], row, scale: Q) -> None:
    if not scale:
        return
    for k, value in enumerate(row):
        acc[k] += scale * value


def weights_digest(weights) -> str:
    payload = "\n".join(format(float(z), ".17g") for z in weights).encode()
    return hashlib.sha256(payload).hexdigest()


def load_locators():
    atlas = json.loads(LOCATOR_ATLAS.read_text())
    records = {int(record["branch"]): record for record in atlas["branches"]}
    if set(records) != set(range(144)):
        raise AssertionError("locator atlas does not cover exactly branches 0..143")
    sources = {branch: LOCATOR_ATLAS.name for branch in range(144)}
    methods = {branch: "highs-ipm" for branch in range(144)}
    for branch in REVISED_OVERRIDES:
        path = HERE / f"rank4_flip_analytic_dual_branch{branch}.json"
        override = json.loads(path.read_text())
        if int(override["branch"]) != branch:
            raise AssertionError((path, override["branch"], branch))
        # Retain atlas metadata but replace the multiplier vector and the
        # numerical diagnostics by the more stable revised-simplex locator.
        records[branch] = {**records[branch], **override}
        sources[branch] = path.name
        methods[branch] = str(override["method"])
    return atlas, records, sources, methods


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()

    atlas, locators, locator_sources, locator_methods = load_locators()
    saved = np.load(CACHE, allow_pickle=True)
    displacement = np.asarray(saved["displacement"], dtype=float)
    primitive_keys = [ast.literal_eval(str(z)) for z in saved["primitive_keys"]]
    analytic = np.load(ANALYTIC, allow_pickle=True)
    guard_keys = [ast.literal_eval(str(z)) for z in analytic["guard_keys"]]
    guard_kinds = [str(z) for z in analytic["guard_kinds"]]

    ng = len(guard_keys)
    nd = displacement.shape[0]
    n = displacement.shape[1]
    offsets = {
        "guard": (0, ng),
        "death": (ng, ng + 4),
        "trust_plus": (ng + 4, ng + 4 + nd),
        "trust_minus": (ng + 4 + nd, ng + 4 + 2 * nd),
        "box_plus": (ng + 4 + 2 * nd, ng + 4 + 2 * nd + n),
        "box_minus": (ng + 4 + 2 * nd + n, ng + 4 + 2 * nd + 2 * n),
    }
    total_rows = offsets["box_minus"][1]
    if total_rows != 7021 or (ng, nd, n) != (6301, 183, 175):
        raise AssertionError((ng, nd, n, total_rows))
    for branch, locator in locators.items():
        if len(locator["multipliers_original_decimal"]) != total_rows:
            raise AssertionError((branch, len(locator["multipliers_original_decimal"])))

    # Build only the exact analytic guard rows touched by at least one locator.
    guard_union = set()
    for locator in locators.values():
        weights = locator["multipliers_original_decimal"]
        guard_union.update(k for k in range(ng) if weights[k] > 0.0)
    print("positive guard support union", len(guard_union), "/", ng, flush=True)

    rows, faces = read_rows_faces()
    q, _ = dr.build_mode_jets(rows, displacement)
    ledger = dr.ExactFractionalLedger(q, faces)
    exact_guards = {}
    for count, index in enumerate(sorted(guard_union), 1):
        exact_guards[index] = tuple(-z for z in ledger.row(guard_keys[index])[1])
        if count % 50 == 0 or count == len(guard_union):
            print("rebuilt exact guard rows", count, "/", len(guard_union), flush=True)

    packets = tf.death_packets(primitive_keys)
    death_key_union = {key for packet in packets for key in packet}
    exact_deaths = {key: ledger.row(key)[1] for key in death_key_union}
    exact_displacement = [
        tuple(Q.from_float(float(value)) for value in displacement[row])
        for row in range(nd)
    ]
    print("common exact ledger ready", flush=True)

    results = []
    for branch in range(144):
        locator = locators[branch]
        weights_float = locator["multipliers_original_decimal"]
        deaths = tf.branch_deaths(primitive_keys, branch)
        stationarity = [Q(0)] * n
        rhs = Q(0)
        group_counts = {name: 0 for name in offsets}
        group_masses = {name: Q(0) for name in offsets}

        for index, value in enumerate(weights_float):
            if value <= 0.0:
                continue
            weight = q17(value)
            if weight <= 0:
                continue
            if index < offsets["guard"][1]:
                group = "guard"
                add_scaled(stationarity, exact_guards[index], weight)
                rhs += weight
            elif index < offsets["death"][1]:
                group = "death"
                local = index - offsets[group][0]
                add_scaled(stationarity, exact_deaths[deaths[local]], weight)
                rhs -= weight
            elif index < offsets["trust_plus"][1]:
                group = "trust_plus"
                local = index - offsets[group][0]
                add_scaled(stationarity, exact_displacement[local], weight)
                rhs += TRUST * weight
            elif index < offsets["trust_minus"][1]:
                group = "trust_minus"
                local = index - offsets[group][0]
                add_scaled(stationarity, exact_displacement[local], -weight)
                rhs += TRUST * weight
            elif index < offsets["box_plus"][1]:
                group = "box_plus"
                local = index - offsets[group][0]
                stationarity[local] += weight
                rhs += BOUND * weight
            elif index < offsets["box_minus"][1]:
                group = "box_minus"
                local = index - offsets[group][0]
                stationarity[local] -= weight
                rhs += BOUND * weight
            else:
                raise AssertionError(index)
            group_counts[group] += 1
            group_masses[group] += weight

        # Adding max(0,-r_j)*(+e_j) and max(0,r_j)*(-e_j) cancels the
        # stationarity residual exactly.  Both rows have RHS BOUND.
        repair_plus = [max(Q(0), -value) for value in stationarity]
        repair_minus = [max(Q(0), value) for value in stationarity]
        repair_mass = sum(repair_plus, Q(0)) + sum(repair_minus, Q(0))
        stationarity_repaired = [
            value + plus - minus
            for value, plus, minus in zip(stationarity, repair_plus, repair_minus)
        ]
        if stationarity_repaired != [Q(0)] * n:
            raise AssertionError((branch, "box repair did not exactly cancel stationarity"))
        rhs_repaired = rhs + BOUND * repair_mass
        negative = rhs_repaired < 0
        record = {
            "branch": branch,
            "deaths": [repr(key) for key in deaths],
            "locator_source": locator_sources[branch],
            "locator_method": locator_methods[branch],
            "locator_weights_sha256": weights_digest(weights_float),
            "locator_original_farkas_rhs_decimal": locator.get("original_farkas_rhs"),
            "locator_original_stationarity_inf_norm_decimal": locator.get(
                "original_stationarity_inf_norm"
            ),
            "positive_multiplier_count": sum(group_counts.values()),
            "positive_multiplier_count_by_group": group_counts,
            "positive_multiplier_mass_by_group_decimal": {
                name: qdecimal(value) for name, value in group_masses.items()
            },
            "unrepaired_farkas_rhs_exact": qs(rhs),
            "unrepaired_farkas_rhs_decimal": qdecimal(rhs),
            "box_stationarity_repair_mass_exact": qs(repair_mass),
            "box_stationarity_repair_mass_decimal": qdecimal(repair_mass),
            "repaired_farkas_rhs_exact": qs(rhs_repaired),
            "repaired_farkas_rhs_decimal": qdecimal(rhs_repaired),
            "exact_stationarity_after_box_repair_all_175_columns_zero": True,
            "all_multipliers_exact_nonnegative": True,
            "strictly_negative_farkas_rhs": negative,
        }
        results.append(record)
        print(
            "branch", branch,
            "method", locator_methods[branch],
            "support", record["positive_multiplier_count"],
            "exact repaired rhs", record["repaired_farkas_rhs_decimal"],
            "negative", negative,
            flush=True,
        )

    negative = [record for record in results if record["strictly_negative_farkas_rhs"]]
    failed = [record for record in results if not record["strictly_negative_farkas_rhs"]]
    closest = max(negative, key=lambda record: Q(record["repaired_farkas_rhs_exact"])) if negative else None
    most_negative = min(negative, key=lambda record: Q(record["repaired_farkas_rhs_exact"])) if negative else None
    exact_complete = len(negative) == 144
    result = {
        "version": 1,
        "type": "literal exact rational Farkas coverage of all clean-flip component branches",
        "scope": (
            "Frozen 175 cached binary64 modes interpreted as exact dyadics; finite-decimal source "
            "cell; analytic normalized-dlog primitives; all 6301 selected guard rows; physical "
            "trust |D c|_infinity<=1/10; coefficient box |c|_infinity<=20; fixed delta=1. "
            "This is an exact first-order template theorem, not a nonlinear path theorem."
        ),
        "farkas_convention": (
            "For A*c<=b, each branch record gives exact y>=0 with A^T*y=0 after explicit "
            "+/- coefficient-box repair and b^T*y equal to repaired_farkas_rhs_exact. "
            "A strictly negative RHS proves infeasibility."
        ),
        "source_cell": "tracks/circuit_atlas/row54_multiwall_flip.csv",
        "source_faces": "tracks/circuit_atlas/row54_multiwall_flip_faces.json",
        "analytic_guard_ledger": ANALYTIC.name,
        "ipm_locator_atlas": LOCATOR_ATLAS.name,
        "revised_simplex_overrides": list(REVISED_OVERRIDES),
        "dimensions": {
            "branches": 144,
            "modes": n,
            "analytic_guards": ng,
            "physical_trust_rows_each_sign": nd,
            "coefficient_box_rows_each_sign": n,
            "rows_per_branch": total_rows,
            "exact_guard_support_union": len(guard_union),
        },
        "exact_negative_branch_count": len(negative),
        "failed_branch_indices": [record["branch"] for record in failed],
        "all_144_branches_have_literal_exact_negative_farkas_rhs": exact_complete,
        "verdict": (
            "EXACT_144_OF_144_ANALYTIC_FIRST_ORDER_OBSTRUCTION"
            if exact_complete else
            "EXACT_COVERAGE_INCOMPLETE"
        ),
        "closest_to_zero_exact_branch": closest,
        "most_negative_exact_branch": most_negative,
        "branches": results,
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print("exact negative", len(negative), "/ 144", flush=True)
    print("failed branches", result["failed_branch_indices"], flush=True)
    if closest:
        print(
            "closest exact branch", closest["branch"],
            closest["repaired_farkas_rhs_decimal"], flush=True,
        )
    print("output", args.output, flush=True)


if __name__ == "__main__":
    main()
