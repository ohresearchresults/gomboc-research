#!/usr/bin/env python3
"""Independent exact verifier for the C5--C17 continuation package."""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import rank5_circuit_escape as esc
import rank5_circuit_escape_continuation as cont
import rank5_exact_jacobian as rj


HERE = Path(__file__).resolve().parent
DATA = HERE / "rank5_circuit_escape_continuation.json"
sys.set_int_max_str_digits(0)


def q(text):
    return esc.qv(text)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    # Regeneration repeats every exact support, Sturm, mechanics and descent
    # assertion rather than trusting the serialized ledger.
    cont.main()
    x = json.loads(DATA.read_text())
    assert x["verdict"] == "EXACT_C5_TO_C17_GORDAN_SUPPORT_BREAK_WITH_STRICT_RESIDUAL_DESCENT"

    events = x["ordered_events"]
    assert [z["name"] for z in events] == [f"C{i}" for i in range(5, 18)]
    roots = []
    for record, (name, ids) in zip(events, cont.CONT_CIRCUITS):
        assert record["name"] == name and record["vertices"] == list(ids)
        root = q(record["parameter_exact"])
        roots.append(root)
        assert esc.det4(root, ids) == 0
        left, right = map(q, record["isolating_bracket_exact"])
        assert left < root < right
        assert esc.det4(left, ids) * esc.det4(right, ids) < 0
        assert record["affine_determinant_unique_root"]
        wall = record["wall_cell"]
        assert wall["f_vector"] == [61, 149, 90]
        assert wall["all_61_active"] and wall["base_stable"] and wall["U8_unstable"]
        assert wall["all_37_forced_rails_present"]
    assert all(roots[i + 1] < roots[i] for i in range(len(roots) - 1))
    assert events[-1]["removed_edge"] == [228, 255]
    assert events[-1]["added_edge"] == [254, 256]

    cells = x["rational_material_cells"]
    assert len(cells) == 14
    assert all(z["f_vector"] == [61, 150, 91] for z in cells)
    assert all(
        z["all_61_active"]
        and z["base_stable"]
        and z["U8_unstable"]
        and z["all_37_forced_rails_present"]
        for z in cells
    )
    assert [z["class"] for z in cells[:8]] == [[2, 4, 4]] * 8
    assert [z["class"] for z in cells[8:]] == [[2, 5, 5]] * 6

    chambers = x["exact_support_chambers"]
    assert len(chambers) == 13
    c4 = esc.circuit_root((54, 255, 257, 258))
    for i, chamber in enumerate(chambers):
        assert q(chamber["lower_exact"]) == roots[i]
        assert q(chamber["upper_exact"]) == (c4 if i == 0 else roots[i - 1])
        assert chamber["strict_support_inequalities_checked"] == 10529
        guard = chamber["continuous_base_U8_guard"]
        assert guard["component_count"] == (
            guard["base_component_count"] + guard["U8_support_count"]
        )
        assert guard["every_numerator_and_denominator_has_zero_roots"]
        assert guard["all_components_positive_at_rational_sample"]
    summary = x["axis_guard_summary"]
    assert summary["chamber_count"] == 13
    assert summary["strict_support_inequalities_checked_total"] == 13 * 10529
    assert summary["continuous_base_U8_components_checked_total"] == sum(
        z["continuous_base_U8_guard"]["component_count"] for z in chambers
    )
    assert summary["all61_base_U8_rails_through_every_cell_and_wall"]

    initial = x["initial_fixed_cell_gordan_blocker"]
    assert q(initial["parameter_exact"]) == Q(-1, 10)
    assert initial["support_indices"] == [0, 1, 2, 3, 4, 5, 8]
    assert initial["support_names"] == [
        "death_S_228_264_246_via_246_228",
        "death_U228_via_251",
        "death_U231_via_232",
        "death_U246_via_245",
        "death_H8_246_via_t",
        "death_H228_254_via_beta2",
        "guard_killed_S_228_254_255_no_rebirth",
    ]
    stationarity = [0] * 6
    for row in initial["support"]:
        multiplier = int(row["positive_integer_multiplier"])
        assert multiplier > 0 and q(row["positive_scale_from_primitive_to_exact_gradient"]) > 0
        for k, z in enumerate(row["primitive_gradient"]):
            stationarity[k] += multiplier * int(z)
    assert stationarity == [0] * 6 and initial["exact_stationarity_zero"]

    pre = x["pre_C17_blocker"]
    assert pre["still_requires_a_no_rebirth_row"]
    assert pre["killed_face_present"] and pre["killed_edge_present"]
    assert any(i >= 8 for i in pre["support_indices"])
    brk = x["C17_break"]
    assert brk["circuit"] == [228, 254, 255, 256]
    assert brk["removed_edge"] == [228, 255] and brk["added_edge"] == [254, 256]
    assert brk["killed_face_S228_254_255_absent_after"]
    assert brk["killed_edge_H228_255_absent_after"]

    post = x["post_C17_residual_cone"]
    assert q(post["parameter_exact"]) == Q(-11, 20)
    assert post["f_vector"] == [61, 150, 91] and post["class"] == [2, 5, 5]
    assert post["residual_gradient_rank_exact"] == 6
    direction = [q(z) for z in post["strict_descent_direction_exact"]]
    assert direction == cont.DESCENT_DIRECTION
    assert len(post["features"]) == 8
    gradients = [[q(z) for z in row["gradient_exact"]] for row in post["features"]]
    assert rj.matrix_rank(gradients) == 6
    for row, gradient in zip(post["features"], gradients):
        derivative = sum((gradient[k] * direction[k] for k in range(6)), Q(0))
        assert derivative == q(row["directed_derivative_exact"]) < 0
    assert post["all_eight_directed_derivatives_strictly_negative_exact"]

    material = x["material_residual_descent"]
    assert q(material["step_exact"]) == Q(1, 125)
    assert q(material["maximum_additional_coordinate_displacement_exact"]) == Q(1, 125)
    endpoint = material["endpoint"]
    assert endpoint["f_vector"] == [61, 150, 91] and endpoint["class"] == [2, 5, 5]
    assert endpoint["all_61_active"] and endpoint["base_stable"] and endpoint["U8_unstable"]
    assert endpoint["all_37_forced_rails_present"]
    ratios = [q(z) for z in material["endpoint_over_start_ratios_exact"]]
    assert len(ratios) == 8 and all(Q(0) < z < 1 for z in ratios)
    assert material["all_eight_exact_values_strictly_decrease"]
    support = material["complete_support_segment_certificate"]
    assert support["persistent_face_count"] == 91
    assert support["strict_outside_support_polynomials"] == 10529
    assert support["strict_cubic_bernstein_coefficients"] == 4 * 10529
    assert support["all_bernstein_coefficients_strictly_inside"]
    guard = material["complete_base_U8_segment_certificate"]
    assert guard["component_count"] == guard["base_component_count"] + guard["U8_support_count"]
    assert guard["every_numerator_and_denominator_has_zero_roots"]
    assert guard["all_components_positive_on_complete_segment"]

    # Every serialized coordinate artifact is exact and hash-bound.
    for relative, expected_hash in x["artifact_hashes"].items():
        path = HERE / relative
        assert path.is_file() and digest(path) == expected_hash
        rows = list(csv.DictReader(path.open()))
        assert len(rows) == 119
        assert set(rows[0]) == {
            "source_id",
            "x_exact",
            "y_exact",
            "z_exact",
            "x",
            "y",
            "z",
        }

    manifest = {}
    for line in cont.MANIFEST.read_text().splitlines():
        hexdigest, relative = line.split("  ", 1)
        assert relative not in manifest
        manifest[relative] = hexdigest
    required = {
        "rank5_circuit_escape_continuation.py",
        "rank5_circuit_escape_continuation.json",
        "RANK5_CIRCUIT_ESCAPE_CONTINUATION_REPORT.md",
        "verify_rank5_circuit_escape_continuation.py",
    }
    assert required <= set(manifest)
    for relative, expected_hash in manifest.items():
        assert digest(HERE / relative) == expected_hash

    print("VERIFIED_EXACT_RANK5_C5_TO_GORDAN_BREAK")
    print("json_sha256", digest(DATA))
    print("events", len(events), "C17", events[-1]["parameter_decimal"])
    print("initial_Gordan_support", initial["support_indices"])
    print("post_rank", post["residual_gradient_rank_exact"])
    print("material_ratios", material["endpoint_over_start_ratios_decimal"])
    print("manifest_entries", len(manifest))


if __name__ == "__main__":
    main()
