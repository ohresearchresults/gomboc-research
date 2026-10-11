#!/usr/bin/env python3
"""Independent literal verifier for rank5_circuit_escape.json."""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import rank5_circuit_escape as esc


HERE = Path(__file__).resolve().parent
DATA = HERE / "rank5_circuit_escape.json"
sys.set_int_max_str_digits(0)


def q(text):
    return esc.qv(text)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    # Clean deterministic regeneration executes every exact assertion in the
    # producer, including fresh hull/mass/mechanics audits for all cells.
    esc.main()
    x = json.loads(DATA.read_text())
    assert x["verdict"] == "EXACT_SMALL_PHYSICAL_ACTUAL_CELL_ESCAPE_345_TO_244_WITH_GUARDED_CONTINUATION"

    atlas = x["ordered_topology_circuit_atlas"]
    assert [z["name"] for z in atlas] == ["C1", "C2", "C3", "C4", "C5"]
    roots = {z["name"]: q(z["parameter_exact"]) for z in atlas}
    assert roots["C5"] < roots["C4"] < Q(-3, 40) < Q(-71, 1000) < Q(-7, 100) < roots["C3"] < roots["C2"] < roots["C1"] < 0
    for record, (_, ids, removed, added) in zip(atlas, esc.CIRCUITS):
        t = q(record["parameter_exact"])
        assert esc.det4(t, ids) == 0
        left, right = map(q, record["isolating_bracket_exact"])
        assert left < t < right
        assert esc.det4(left, ids) * esc.det4(right, ids) < 0
        assert record["affine_determinant_unique_root"]
        assert record["wall_cell"]["f_vector"] == [61, 149, 90]
        assert record["wall_cell"]["all_61_active"]
        assert record["wall_cell"]["base_stable"]
        assert record["wall_cell"]["U8_unstable"]
        assert record["wall_cell"]["all_37_forced_rails_present"]
        assert record["removed_edge"] == list(removed)
        assert record["added_edge"] == list(added)

    chambers = x["exact_support_chambers"]
    expected = [
        (roots["C1"], None),
        (roots["C2"], roots["C1"]),
        (roots["C3"], roots["C2"]),
        (roots["C4"], roots["C3"]),
        (roots["C5"], roots["C4"]),
    ]
    assert len(chambers) == len(expected)
    for chamber, (lower, upper) in zip(chambers, expected):
        assert q(chamber["lower_exact"]) == lower
        if upper is not None:
            assert q(chamber["upper_exact"]) == upper
        assert chamber["strict_support_inequalities_checked"] == 10529

    wall = x["mechanics_wall"]
    p = [Q(int(z)) for z in wall["common_primitive_polynomial_coefficients_ascending"]]
    left, right = map(q, wall["isolating_interval_exact"])
    count, sturm = esc.sturm_root_count(p, left, right)
    assert count == 1
    assert esc.peval(p, left) * esc.peval(p, right) < 0
    assert [len(z) - 1 for z in sturm] == [3, 2, 1, 0]
    assert wall["stable_component_numerator_divisible_by_common_exact"]
    assert wall["saddle_component_numerator_divisible_by_common_exact"]
    guard = wall["all61_base_U8_rails_to_wall"]
    assert guard["every_numerator_has_zero_roots_in_open_chamber"]
    assert guard["all_components_positive_at_far_exact"]
    assert guard["base_and_U8_component_count"] == 30

    far = x["far_exact_cell"]
    assert q(far["parameter_exact"]) == Q(-3, 40)
    assert far["f_vector"] == [61, 150, 91]
    assert far["class"] == [2, 4, 4]
    assert far["all_61_active"] and far["base_stable"] and far["U8_unstable"]
    assert far["forced_rails_present"] == 37
    assert far["exact_rank"] == {
        "remaining_original_five": 5,
        "all_eight_residual_deaths": 6,
        "with_two_no_rebirth_guards": 6,
    }
    block = far["residual_feature_block"]
    assert len(block) == 10
    assert all(q(z["value_exact"]) > 0 for z in block[:8])
    assert all(q(z["value_exact"]) < 0 for z in block[8:])

    cert = far["exact_no_rebirth_gordan_certificate"]
    assert cert["full_system_row_count"] == 10
    assert cert["eight_death_gradient_rank_exact"] == 6
    assert cert["exact_stationarity_zero"]
    support = cert["support"]
    assert len(support) == 7
    stationarity = [0] * 6
    has_death = False
    for row in support:
        multiplier = int(row["positive_integer_multiplier"])
        assert multiplier > 0
        has_death |= row["kind"] == "death"
        for k, z in enumerate(row["primitive_gradient"]):
            stationarity[k] += multiplier * int(z)
        # This is a positive row rescaling, so derivative signs are unchanged.
        assert q(row["positive_scale_from_primitive_to_exact_gradient"]) > 0
    assert has_death and stationarity == [0] * 6
    assert stationarity == cert["exact_stationarity_six_columns"]

    # Hashes and literal row255 displacement in every rational coordinate file.
    for relative, expected_hash in x["artifact_hashes"].items():
        path = HERE / relative
        assert path.is_file() and digest(path) == expected_hash
        if path.name == "mechanics_wall_algebraic_locator.csv":
            continue
        # Every exact CSV uses the authoritative seven-column schema.
        rows = list(csv.DictReader(path.open()))
        assert len(rows) == 119
        assert set(rows[0]) == {"source_id", "x_exact", "y_exact", "z_exact", "x", "y", "z"}

    nxt = x["next_event"]
    assert nxt["name"] == "C4" and q(nxt["parameter_exact"]) == roots["C4"]
    assert all(nxt["guards_after"].values()) and nxt["class_after"] == [2, 4, 4]
    assert q(nxt["following_topology_endpoint_C5_exact"]) == roots["C5"]

    manifest = {}
    for line in esc.MANIFEST.read_text().splitlines():
        hexdigest, relative = line.split("  ", 1)
        assert relative not in manifest
        manifest[relative] = hexdigest
    required = {
        "rank5_circuit_escape.py",
        "rank5_circuit_escape.json",
        "RANK5_CIRCUIT_ESCAPE_REPORT.md",
        "verify_rank5_circuit_escape.py",
    }
    assert required <= set(manifest)
    for relative, expected_hash in manifest.items():
        assert digest(HERE / relative) == expected_hash

    print("VERIFIED_EXACT_RANK5_ACTUAL_CELL_ESCAPE")
    print("json_sha256", digest(DATA))
    print("circuits", [z["parameter_decimal"] for z in atlas[:4]])
    print("mechanics_root_locator", wall["root_decimal_locator"])
    print("far", far["f_vector"], far["class"], far["forced_rails_present"])
    print("Gordan_support", cert["support_indices"])
    print("manifest_entries", len(manifest))


if __name__ == "__main__":
    main()
