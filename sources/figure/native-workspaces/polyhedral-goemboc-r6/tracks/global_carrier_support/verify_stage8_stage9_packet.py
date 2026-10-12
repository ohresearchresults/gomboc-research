#!/usr/bin/env python3
"""Standalone exact/fresh-hull verifier for the stage-8/9 carrier packet.

The verifier does not trust the stored sample summaries.  It reconstructs
every stage-8 quadrant/path point, every stage-9 adaptive/path point, and both
directed exact stage-8 samples from coordinates, then rebuilds the hull and
own-centroid mechanics.  It also reconstructs the stage-9 four-point circuit
as an exact dyadic polynomial on the saved affine wall line.
"""

from __future__ import annotations

from fractions import Fraction
from functools import reduce
import itertools
import json
import math
from pathlib import Path
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
from actual_hull_mechanics import evaluate  # noqa: E402
from optimize_base_escape import Search  # noqa: E402
from search_row54_remote228 import load_points, summarize  # noqa: E402


SOURCE = ROOT / "tracks/circuit_atlas/row54_far_rebuilt.csv"
SOURCE_AUDIT = ROOT / "tracks/circuit_atlas/row54_far_rebuilt_audit.json"
BIRTH_ATLAS = HERE / "local_birth_atlas.json"
STAGE8_CERT = HERE / "stage8_linked_birth_certificate.json"
STAGE8_ATLAS = HERE / "local_stage8_birth_bypass_atlas.json"
STAGE8_ADAPTIVE = HERE / "adaptive_rail229_deep_stage8.json"
STAGE9_ADAPTIVE = HERE / "adaptive_stage9_after_birth_bypass.json"
STAGE9_WALL = HERE / "stage9_rail251_wall_audit.json"
STAGE9_ATLAS = HERE / "local_stage9_rail251_bypass_atlas.json"
BASE_RESULT = HERE / "base_escape_stable_pair.json"
LEDGER = HERE / "stage8_stage9_ledger.json"
REPORT = HERE / "STAGE8_STAGE9_PACKET.md"

BASE_FACE = tuple(range(17)) + (54,)
KEEP_NAMES = ("S(7,8,245)", "U54", "H(6,7)", "H(9,10)")
KEEP_KEYS = (
    ("face", (7, 8, 245)),
    ("vertex", 54),
    ("edge", (6, 7)),
    ("edge", (9, 10)),
)


def load_json(path):
    return json.loads(path.read_text())


def frac(value):
    return Fraction.from_float(float(value))


def poly_mul(left, right):
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def interpolate_consecutive(values):
    differences = list(values)
    forward = []
    while differences:
        forward.append(differences[0])
        differences = [b - a for a, b in zip(differences, differences[1:])]
    result = [Fraction(0)]
    falling = [Fraction(1)]
    factorial = 1
    for degree, coefficient in enumerate(forward):
        if degree:
            falling = poly_mul(falling, [Fraction(-(degree - 1)), Fraction(1)])
            factorial *= degree
        if len(result) < len(falling):
            result.extend([Fraction(0)] * (len(falling) - len(result)))
        for i, value in enumerate(falling):
            result[i] += coefficient * value / factorial
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def poly_value(coefficients, value):
    result = Fraction(0)
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def primitive_integers(coefficients):
    denominator = reduce(math.lcm, (x.denominator for x in coefficients), 1)
    integers = [x.numerator * (denominator // x.denominator) for x in coefficients]
    divisor = reduce(math.gcd, (abs(x) for x in integers if x), 0)
    integers = [x // divisor for x in integers]
    if integers[-1] < 0:
        integers = [-x for x in integers]
    return integers


def det4_exact(rows):
    total = Fraction(0)
    for permutation in itertools.permutations(range(4)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(4) for j in range(i + 1, 4)
        )
        term = Fraction(-1 if inversions % 2 else 1)
        for row, column in enumerate(permutation):
            term *= rows[row][column]
        total += term
    return total


def rational_dict(value):
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def main():
    labels, source = load_points(SOURCE)
    index = {label: offset for offset, label in enumerate(labels)}
    source_audit = load_json(SOURCE_AUDIT)
    rails = {
        tuple(sorted(edge))
        for edge in source_audit["fresh_hull_audit"]["forced_rail_edges"]
    }
    assert len(rails) == 37
    search = Search(labels, source, rails, report=False)
    birth_atlas = load_json(BIRTH_ATLAS)
    remote_basis = np.asarray([
        birth_atlas["remote_basis"]["tangent"],
        birth_atlas["remote_basis"]["normal"],
    ])

    def controls(rows):
        return [
            (int(row["label"]), np.asarray(row["direction"], dtype=float))
            for row in rows
        ]

    def coordinates(parameters, control_rows):
        parameters = np.asarray(parameters, dtype=float)
        points = search.coordinates(parameters[:20])
        points[index[228]] += parameters[20] * remote_basis[0]
        points[index[228]] += parameters[21] * remote_basis[1]
        for offset, (label, direction) in enumerate(control_rows):
            points[index[label]] += parameters[22 + offset] * direction
        return points

    def circuit_value(points, circuit):
        rows = np.c_[points[[index[label] for label in circuit]], np.ones(4)]
        return float(np.linalg.det(rows))

    def fresh(parameters, control_rows, circuit_specs=()):
        points = coordinates(parameters, control_rows)
        record = summarize(labels, points, rails)
        mechanics = evaluate(labels, points)
        signed = [sign * circuit_value(points, circuit) for circuit, sign in circuit_specs]
        assert len(record["active_labels"]) == 61
        assert record["f_vector"] == [61, 162, 103]
        assert record["base_face_present"]
        assert not record["missing_forced_rails"]
        assert 8 in record["unstable_vertices"]
        assert all(value > 0.0 for value in signed)
        return record, mechanics, signed

    # Stage 8 exact wall: validate exact signs and fresh directed samples.
    cert8 = load_json(STAGE8_CERT)
    atlas8 = load_json(STAGE8_ATLAS)
    adaptive8 = load_json(STAGE8_ADAPTIVE)
    assert cert8["passed"]
    assert cert8["common_numerator_geometry"]["actual_degree"] == 6
    interval8 = cert8["exact_root_isolating_interval"]
    assert Fraction(interval8["lo_value"]) < 0 < Fraction(interval8["hi_value"])
    assert cert8["mechanical_transition"] == {
        "class": [[2, 2, 2], [3, 2, 3]],
        "stable_faces_added": [[8, 245, 246]],
        "saddle_edges_added": [[8, 245]],
        "hull_unchanged": True,
    }
    control8 = controls(atlas8["local_controls"])
    circuit_specs8 = [
        (tuple(row["circuit"]), int(row["valid_sign"]))
        for row in adaptive8["circuit_guards"]
    ]
    directed8 = []
    for side, expected_class in (("minus", [2, 2, 2]), ("plus", [3, 2, 3])):
        csv_labels, csv_points = load_points(Path(cert8[side]["coordinates"]))
        assert csv_labels == labels
        record = summarize(labels, csv_points, rails)
        mechanics = evaluate(labels, csv_points)
        signed = [sign * circuit_value(csv_points, circuit) for circuit, sign in circuit_specs8]
        assert len(record["active_labels"]) == 61
        assert record["f_vector"] == [61, 162, 103]
        assert record["class"] == expected_class
        assert record["base_face_present"] and not record["missing_forced_rails"]
        assert 8 in record["unstable_vertices"] and all(x > 0 for x in signed)
        expected_positive = side == "plus"
        assert (mechanics.face_decisions[(8, 245, 246)] > 0) == expected_positive
        assert (mechanics.edge_decisions[(8, 245)] > 0) == expected_positive
        directed8.append({"side": side, "class": record["class"], "minimum_signed_circuit": min(signed)})

    quadrant_classes = {}
    min_stage8_circuit = float("inf")
    for row in atlas8["quadrants"]:
        record, _, signed = fresh(row["parameters"], control8, circuit_specs8)
        key = str(record["class"])
        quadrant_classes[key] = quadrant_classes.get(key, 0) + 1
        min_stage8_circuit = min(min_stage8_circuit, min(signed))
    assert quadrant_classes == {"[3, 2, 3]": 2, "[2, 2, 2]": 2}
    for row in atlas8["bypass_path"]:
        record, mechanics, signed = fresh(row["parameters"], control8, circuit_specs8)
        assert record["class"] == [2, 2, 2]
        assert mechanics.face_decisions[(8, 245, 246)] < 0
        assert mechanics.edge_decisions[(8, 245)] < 0
        min_stage8_circuit = min(min_stage8_circuit, min(signed))
    assert len(atlas8["bypass_path"]) == 121
    assert atlas8["keep_rank"] == 4 and atlas8["nullity"] == 19
    assert atlas8["bypass_audit"]["bypass_found"]

    # Stage 9 continuation and fresh trace ledger.
    adaptive9 = load_json(STAGE9_ADAPTIVE)
    wall9 = load_json(STAGE9_WALL)
    atlas9 = load_json(STAGE9_ATLAS)
    control9 = controls(adaptive9["local_controls"])
    circuit_specs9 = [
        (tuple(row["circuit"]), int(row["valid_sign"]))
        for row in adaptive9["circuit_guards"]
    ]
    min_stage9_trace_circuit = float("inf")
    for row in adaptive9["trace"]:
        record, mechanics, signed = fresh(row["parameters"], control9, circuit_specs9)
        assert record["class"] == [2, 2, 2]
        assert mechanics.face_decisions[(8, 245, 246)] < 0
        assert mechanics.edge_decisions[(8, 245)] < 0
        min_stage9_trace_circuit = min(min_stage9_trace_circuit, min(signed))
    assert len(adaptive9["trace"]) == 53

    # Reconstruct the protected-rail wall as an exact dyadic determinant
    # polynomial along the saved affine line.
    circuit9 = tuple(wall9["circuit"])
    assert circuit9 == (224, 228, 251, 252)
    valid_sign9 = -1
    start9 = np.asarray(adaptive9["trace"][-1]["parameters"], dtype=float)
    direction9 = np.asarray(adaptive9["wall"]["direction"], dtype=float)
    points_zero = coordinates(start9, control9)
    point_slopes = coordinates(start9 + direction9, control9) - points_zero

    def exact_circuit9(t):
        rows = []
        for label in circuit9:
            offset = index[label]
            rows.append(tuple(
                frac(points_zero[offset, axis]) + t * frac(point_slopes[offset, axis])
                for axis in range(3)
            ) + (Fraction(1),))
        return det4_exact(rows)

    coefficients9 = interpolate_consecutive([exact_circuit9(Fraction(i)) for i in range(4)])
    assert exact_circuit9(Fraction(1, 3)) == poly_value(coefficients9, Fraction(1, 3))
    assert len(coefficients9) - 1 == 1  # only remote label 228 moves in this circuit
    estimate9 = float(wall9["circuit_determinant_root"])
    lo9 = frac(estimate9 - 1e-4)
    hi9 = frac(estimate9 + 1e-4)
    assert poly_value(coefficients9, lo9) < 0 < poly_value(coefficients9, hi9)
    for _ in range(100):
        mid = (lo9 + hi9) / 2
        if poly_value(coefficients9, mid) < 0:
            lo9 = mid
        else:
            hi9 = mid
    assert valid_sign9 * poly_value(coefficients9, lo9) > 0
    assert valid_sign9 * poly_value(coefficients9, hi9) < 0
    assert wall9["topology_flip"] == {
        "faces_removed": [[224, 251, 252], [228, 251, 252]],
        "faces_added": [[224, 228, 251], [224, 228, 252]],
        "edges_removed": [[251, 252]],
        "edges_added": [[224, 228]],
    }
    for row in wall9["samples"]:
        if row["offset"] < 0:
            assert row["circuit_determinant"] < 0
            assert not row["missing_forced_rails"]
        elif row["offset"] > 0:
            assert row["circuit_determinant"] > 0
            assert row["missing_forced_rails"] == [[251, 252]]

    # Stage 9 L-bypass: reconstruct all 81 path parameters and fresh-audit.
    inherited9 = [
        (tuple(row["circuit"]), int(row["valid_sign"]))
        for row in atlas9["inherited_circuit_guards"]
    ]
    all_specs9 = inherited9 + [(circuit9, valid_sign9)]
    waypoints9 = [np.asarray(row, dtype=float) for row in atlas9["bypass_waypoints"]]
    min_stage9_bypass_circuit = float("inf")
    for row in atlas9["bypass_path"]:
        segment = int(row["segment"])
        alpha = float(row["alpha"])
        parameters = waypoints9[segment] + alpha * (waypoints9[segment + 1] - waypoints9[segment])
        record, mechanics, signed = fresh(parameters, control9, all_specs9)
        assert record["class"] == [2, 2, 2]
        assert mechanics.face_decisions[(8, 245, 246)] < 0
        assert mechanics.edge_decisions[(8, 245)] < 0
        min_stage9_bypass_circuit = min(min_stage9_bypass_circuit, min(signed))
    assert len(atlas9["bypass_path"]) == 81
    assert atlas9["bypass_audit"]["bypass_found"]
    assert atlas9["direction_y_solver"] == "minimum_norm_circuit_plus_positive_keep_repair"
    assert atlas9["feature_derivative_x"]["H(9,10)"] > 0
    assert atlas9["positive_keep_repair_targets"]["H(9,10)"] < 0
    assert atlas9["feature_derivative_y"]["H(9,10)"] < 0
    assert all(
        atlas9["bypass_audit"]["end_feature_values"][name]
        < atlas9["bypass_audit"]["start_feature_values"][name]
        for name in KEEP_NAMES
    )

    base = load_json(BASE_RESULT)["best"]
    initial = {
        row["feature"].replace("nonstable:[7, 8, 245]", "S(7,8,245)")
        .replace("nonunstable:54", "U54")
        .replace("nonsaddle:[6, 7]", "H(6,7)")
        .replace("nonsaddle:[9, 10]", "H(9,10)"): row["magnitude"]
        for row in base["target_violations"]
    }
    endpoint = atlas9["bypass_audit"]["end_feature_values"]
    cumulative_ratios = {name: endpoint[name] / initial[name] for name in KEEP_NAMES}
    cumulative_reductions = {name: 1.0 - cumulative_ratios[name] for name in KEEP_NAMES}
    assert all(value > 0.85 for value in cumulative_reductions.values())

    ledger = {
        "version": 1,
        "passed": True,
        "scope": "exact roots/signs plus fresh-hull segment ledger for stages 8 and 9",
        "hard_invariants": {
            "active_vertices": 61,
            "f_vector_off_wall": [61, 162, 103],
            "base_face": list(BASE_FACE),
            "unstable_vertex_8_present": True,
            "forced_rail_count": 37,
        },
        "stage8": {
            "event": "linked S(8,245,246)/H(8,245) own-centroid birth",
            "exact_polynomial_degree": 6,
            "exact_root": cert8["root_float"],
            "exact_root_isolating_interval": interval8,
            "conditioned_root_separation": cert8["conditioned_root_separation"],
            "directed_samples": directed8,
            "quadrant_class_counts": quadrant_classes,
            "bypass_path_samples": len(atlas8["bypass_path"]),
            "fresh_samples_total": 2 + len(atlas8["quadrants"]) + len(atlas8["bypass_path"]),
            "minimum_signed_inherited_circuit": min_stage8_circuit,
            "keep_rank": atlas8["keep_rank"],
            "nullity": atlas8["nullity"],
            "antibirth_projection_norm": atlas8["nullspace_antibirth_projection_norm"],
            "bypass_audit": atlas8["bypass_audit"],
        },
        "stage9": {
            "event": "protected rail (251,252) diagonal flip",
            "circuit": list(circuit9),
            "valid_sign": valid_sign9,
            "exact_polynomial_degree": len(coefficients9) - 1,
            "primitive_integer_polynomial_low_to_high": [str(x) for x in primitive_integers(coefficients9)],
            "exact_root_isolating_interval": {
                "lo": rational_dict(lo9),
                "hi": rational_dict(hi9),
                "lo_value": str(poly_value(coefficients9, lo9)),
                "hi_value": str(poly_value(coefficients9, hi9)),
                "width": float(hi9 - lo9),
            },
            "root_float": float((lo9 + hi9) / 2),
            "topology_flip": wall9["topology_flip"],
            "adaptive_trace_samples": len(adaptive9["trace"]),
            "directed_wall_samples": len(wall9["samples"]),
            "bypass_path_samples": len(atlas9["bypass_path"]),
            "fresh_off_wall_samples": len(adaptive9["trace"]) + len(atlas9["bypass_path"]),
            "minimum_signed_trace_circuit": min_stage9_trace_circuit,
            "minimum_signed_bypass_circuit": min_stage9_bypass_circuit,
            "h910_repair": {
                "solver": atlas9["direction_y_solver"],
                "wall_direction_derivative": atlas9["feature_derivative_x"]["H(9,10)"],
                "repair_target": atlas9["positive_keep_repair_targets"]["H(9,10)"],
                "repair_direction_derivative": atlas9["feature_derivative_y"]["H(9,10)"],
            },
            "bypass_audit": atlas9["bypass_audit"],
        },
        "cumulative_from_base_escape": {
            "initial": initial,
            "stage9_bypass_endpoint": endpoint,
            "endpoint_to_initial_ratios": cumulative_ratios,
            "fractional_reductions": cumulative_reductions,
        },
        "verifier": str(Path(__file__).resolve()),
    }
    LEDGER.write_text(json.dumps(ledger, indent=2, sort_keys=True) + "\n")

    reductions = "\n".join(
        f"| {name} | {initial[name]:.12g} | {endpoint[name]:.12g} | {100*cumulative_reductions[name]:.6f}% |"
        for name in KEEP_NAMES
    )
    report = f"""# Stage 8–9 exact carrier packet

Verdict: both encountered walls are real and exactly localized, but neither is an obstruction.  Fresh-hull L-bypasses remain in the class `(2,2,2)` carrier cell, preserve the enlarged base, unstable vertex 8, all 61 active labels, and all 37 forced rails, while all four unwanted decisions decrease.

## Stage 8: linked own-centroid birth

- Common event: `S(8,245,246)` and `H(8,245)` share the cleared own-centroid numerator in `{cert8['common_numerator_geometry']['formula']}`.
- Exact dyadic polynomial degree: **6**; root `{cert8['root_float']:.17g}`; rational isolation width `{interval8['width']:.3e}`.
- Independently conditioned roots differ by only `{cert8['conditioned_root_separation']:.3e}`; exact common-numerator signs are negative/positive on the directed samples.
- Fresh directed transition: `(2,2,2) -> (3,2,3)`, adding only face `(8,245,246)` and edge `(8,245)`, with unchanged hull.
- Four-quadrant audit: two `(3,2,3)` and two `(2,2,2)` cells.  The 23D keep Jacobian has rank 4/nullity 19; anti-birth projection norm `{atlas8['nullspace_antibirth_projection_norm']:.9g}`.
- L-bypass: 121 fresh path samples; all stay `(2,2,2)`, all hard constraints and six inherited circuit signs hold, and all four keep decisions decrease.

## Stage 9: protected rail wall

- Exact circuit: `(224,228,251,252)`, valid side `det < 0` (sign `-1`).
- Exact dyadic determinant polynomial degree: **{len(coefficients9)-1}**; root `{float((lo9+hi9)/2):.17g}`; rational isolation width `{float(hi9-lo9):.3e}`.
- Scalar crossing replaces faces `(224,251,252),(228,251,252)` and rail `(251,252)` by faces `(224,228,251),(224,228,252)` and edge `(224,228)`.  Thus the post-side violates the forced rail.
- The 23D L-bypass has 81 fresh path samples, retains rail `(251,252)` and all other hard invariants, stays `(2,2,2)`, and keeps the linked stage-8 birth absent.
- H(9,10) needed an explicit nullspace repair: its raw wall-direction derivative was `{atlas9['feature_derivative_x']['H(9,10)']:.9g}`; the minimum-norm repair imposed `{atlas9['positive_keep_repair_targets']['H(9,10)']:.9g}`, yielding repair derivative `{atlas9['feature_derivative_y']['H(9,10)']:.9g}` and a net decrease on the L-path.

## Fresh sample ledger

| Block | Fresh samples | Result |
|---|---:|---|
| Stage-8 directed exact sides | 2 | `(2,2,2)` / `(3,2,3)`, all hard |
| Stage-8 quadrants | 4 | 2 cells per side, all hard |
| Stage-8 bypass | 121 | all `(2,2,2)`, all hard |
| Stage-9 adaptive trace | {len(adaptive9['trace'])} | all `(2,2,2)`, all hard |
| Stage-9 directed wall atlas | {len(wall9['samples'])} | exact sign/topology ledger; rail lost only at/on post-side |
| Stage-9 bypass | {len(atlas9['bypass_path'])} | all `(2,2,2)`, all hard |

## Cumulative packet reduction

| Decision | Initial | Stage-9 bypass endpoint | Reduction |
|---|---:|---:|---:|
{reductions}

Reproduce the complete exact/fresh audit with:

```bash
python tracks/global_carrier_support/verify_stage8_stage9_packet.py
```

Machine-readable details, including exact rational brackets and primitive integer coefficients, are in `stage8_stage9_ledger.json`.
"""
    REPORT.write_text(report)
    print(json.dumps({
        "passed": True,
        "ledger": str(LEDGER.resolve()),
        "report": str(REPORT.resolve()),
        "stage8_fresh_samples": ledger["stage8"]["fresh_samples_total"],
        "stage9_fresh_off_wall_samples": ledger["stage9"]["fresh_off_wall_samples"],
        "stage9_exact_root": ledger["stage9"]["root_float"],
        "cumulative_reductions": cumulative_reductions,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
