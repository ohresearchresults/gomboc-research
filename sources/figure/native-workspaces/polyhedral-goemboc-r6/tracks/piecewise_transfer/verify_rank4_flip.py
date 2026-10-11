#!/usr/bin/env python3
"""Verify the materialized exact flip ledgers and 144-branch coverage record."""
from __future__ import annotations

import json
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
sys.set_int_max_str_digits(0)


def load(name):
    return json.loads((HERE / name).read_text())


def q(text):
    return Q(text)


def main():
    ledger = load("rank4_flip_exact_ledger.json")
    assert ledger["branch_count"] == 144
    assert ledger["branch_rank_histogram"] == {"death_rank_4_with_guard_rank_5": 144}
    assert ledger["ultrathin_identity"]["exact_value_and_gradient_identical"] is True
    assert [len(ledger["component_groups"][key]) for key in (
        "stable_face_S198_243_244", "unstable_vertex_U2",
        "saddle_edge_H4_5", "saddle_edge_H12_13",
    )] == [3, 3, 4, 4]

    # The floating atlas is an active-set locator only.  The theorem is based
    # on the literal per-branch exact rational coverage ledger below.
    atlas = load("rank4_flip_analytic_dual_atlas.json")
    assert atlas["branch_count"] == 144
    assert {row["branch"] for row in atlas["branches"]} == set(range(144))

    coverage = load("rank4_flip_exact_coverage.json")
    assert coverage["verdict"] == "EXACT_144_OF_144_ANALYTIC_FIRST_ORDER_OBSTRUCTION"
    assert coverage["dimensions"] == {
        "branches": 144,
        "modes": 175,
        "analytic_guards": 6301,
        "physical_trust_rows_each_sign": 183,
        "coefficient_box_rows_each_sign": 175,
        "rows_per_branch": 7021,
        "exact_guard_support_union": 980,
    }
    assert coverage["exact_negative_branch_count"] == 144
    assert coverage["failed_branch_indices"] == []
    assert coverage["all_144_branches_have_literal_exact_negative_farkas_rhs"] is True
    branches = coverage["branches"]
    assert len(branches) == 144
    assert {row["branch"] for row in branches} == set(range(144))
    assert all(len(row["deaths"]) == 4 for row in branches)
    assert len({tuple(row["deaths"]) for row in branches}) == 144
    for row in branches:
        unrepaired_rhs = q(row["unrepaired_farkas_rhs_exact"])
        repair_mass = q(row["box_stationarity_repair_mass_exact"])
        exact_rhs = q(row["repaired_farkas_rhs_exact"])
        assert exact_rhs == unrepaired_rhs + 20 * repair_mass
        assert exact_rhs < 0
        assert row["strictly_negative_farkas_rhs"] is True
        assert row["exact_stationarity_after_box_repair_all_175_columns_zero"] is True
        assert row["all_multipliers_exact_nonnegative"] is True
        assert row["positive_multiplier_count"] > 0
        assert row["positive_multiplier_count"] == sum(
            row["positive_multiplier_count_by_group"].values()
        )
        assert repair_mass >= 0

    exact_closest = max(branches, key=lambda row: q(row["repaired_farkas_rhs_exact"]))
    recorded_closest = coverage["closest_to_zero_exact_branch"]
    assert exact_closest["branch"] == recorded_closest["branch"] == 55
    assert q(exact_closest["repaired_farkas_rhs_exact"]) == q(
        recorded_closest["repaired_farkas_rhs_exact"]
    )
    revised = {row["branch"] for row in branches if row["locator_method"] == "revised simplex"}
    assert revised == {9, 13, 54, 55}

    branch13 = load("rank4_flip_exact_analytic_farkas_branch13.json")
    assert branch13["branch"] == 13
    assert branch13["verdict"] == "EXACT_ANALYTIC_BRANCH13_TRUST_R_0.1_INFEASIBLE_AT_DELTA_1"
    assert branch13["exact_stationarity_all_175_columns_zero"] is True
    assert branch13["strictly_negative_farkas_rhs"] is True
    assert q(branch13["repaired_farkas_rhs_exact"]) < 0
    assert branch13["supported_multiplier_count"] >= 1
    assert all(q(row["weight_exact"]) > 0 for row in branch13["multipliers"])
    assert all(q(row["weight_exact"]) > 0 for side in (
        "box_plus", "box_minus"
    ) for row in branch13["stationarity_repair"][side])

    branch102 = load("rank4_flip_exact_analytic_farkas_branch102.json")
    assert branch102["branch"] == 102
    assert branch102["exact_stationarity_all_175_columns_zero"] is True
    assert branch102["strictly_negative_farkas_rhs"] is True
    assert q(branch102["repaired_farkas_rhs_exact"]) < 0

    pilot = load("rank4_flip_exact_trust_farkas.json")
    assert pilot["branch_index"] == 4
    assert pilot["exact_certificate"]["stationarity_all_175_columns_exact_zero"] is True
    assert q(pilot["exact_certificate"]["dual_delta_lower_bound_exact"]) > 1

    print("ALL_RANK4_FLIP_LITERAL_EXACT_144_OF_144_COVERAGE_VERIFIERS_PASS")


if __name__ == "__main__":
    main()
