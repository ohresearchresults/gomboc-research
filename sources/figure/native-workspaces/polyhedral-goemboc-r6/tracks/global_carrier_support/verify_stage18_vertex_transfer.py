#!/usr/bin/env python3
"""Exact/directed verifier for a base-vertex carrier transfer.

Along the saved affine continuation line the own-centroid projection crosses
the two base edges incident to vertex 10.  For j in {9,11}, with C=M/(4V),

    N_j(t) = <M(t)-4 V(t) p10(t), pj(t)-p10(t)>

    is the cleared numerator shared by the U10 neighbour inequality and the
endpoint inequality of edge (10,j).  N_11=0 simultaneously births U10 and
H(10,11); shortly afterwards N_9=0 kills H(9,10) and U10.  This script
reconstructs both degree-at-most-five dyadic polynomials, isolates their roots
rationally, and audits the pre/middle/far actual hull cells.
"""

from __future__ import annotations

import argparse
import csv
from fractions import Fraction
from functools import reduce
import json
import math
from pathlib import Path
import sys

import numpy as np
from scipy.spatial import ConvexHull


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from actual_hull_mechanics import _merge_coplanar_facets, evaluate  # noqa: E402
from optimize_base_escape import Search  # noqa: E402
from search_row54_remote228 import load_points, summarize  # noqa: E402


BIRTH_FACES = ((8, 245, 246), (9, 10, 263), (8, 9, 263))
BIRTH_EDGES = ((8, 245), (9, 263), (8, 263))


def add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def sub(left, right):
    return tuple(a - b for a, b in zip(left, right))


def scale(value, vector):
    return tuple(value * x for x in vector)


def cross(left, right):
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def det3(rows):
    return dot(rows[0], cross(rows[1], rows[2]))


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
        for index, value in enumerate(falling):
            result[index] += coefficient * value / factorial
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def poly_value(coefficients, value):
    result = Fraction(0)
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def poly_trim(coefficients):
    result = list(coefficients)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def poly_derivative(coefficients):
    return poly_trim([
        degree * coefficient
        for degree, coefficient in enumerate(coefficients)
        if degree
    ] or [Fraction(0)])


def poly_remainder(numerator, denominator):
    numerator = poly_trim(numerator)
    denominator = poly_trim(denominator)
    if denominator == [0]:
        raise ZeroDivisionError("zero polynomial")
    while len(numerator) >= len(denominator) and numerator != [0]:
        shift = len(numerator) - len(denominator)
        factor = numerator[-1] / denominator[-1]
        for index, coefficient in enumerate(denominator):
            numerator[index + shift] -= factor * coefficient
        numerator = poly_trim(numerator)
    return numerator


def sturm_sequence(coefficients):
    sequence = [poly_trim(coefficients), poly_derivative(coefficients)]
    while sequence[-1] != [0]:
        remainder = poly_remainder(sequence[-2], sequence[-1])
        if remainder == [0]:
            break
        sequence.append([-value for value in remainder])
    return sequence


def sturm_variations(sequence, value):
    signs = []
    for polynomial in sequence:
        evaluated = poly_value(polynomial, value)
        if evaluated:
            signs.append(1 if evaluated > 0 else -1)
    return sum(left != right for left, right in zip(signs, signs[1:]))


def sturm_root_count(sequence, left, right):
    return sturm_variations(sequence, left) - sturm_variations(sequence, right)


def primitive_integer_coefficients(coefficients):
    denominator = reduce(math.lcm, (x.denominator for x in coefficients), 1)
    integers = [x.numerator * (denominator // x.denominator) for x in coefficients]
    divisor = reduce(math.gcd, (abs(x) for x in integers if x), 0)
    integers = [x // divisor for x in integers]
    if integers[-1] < 0:
        integers = [-x for x in integers]
    return integers


def rational(value):
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def write_csv(path, labels, points):
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(("source_id", "x", "y", "z"))
        for label, point in zip(labels, points):
            writer.writerow([label, *[format(float(x), ".17g") for x in point]])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--birth-atlas", type=Path, required=True)
    parser.add_argument("--adaptive", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--pre-atlas", type=Path, required=True)
    parser.add_argument("--far-atlas", type=Path, required=True)
    parser.add_argument("--pre-csv", type=Path, required=True)
    parser.add_argument("--middle-csv", type=Path, required=True)
    parser.add_argument("--far-csv", type=Path, required=True)
    parser.add_argument("--isolation-steps", type=int, default=100)
    parser.add_argument("--vertex", type=int, default=10)
    parser.add_argument("--birth-neighbour", type=int, default=11)
    parser.add_argument("--death-neighbour", type=int, default=9)
    parser.add_argument(
        "--atlas-circuit", type=int, nargs=4, default=(9, 10, 11, 263)
    )
    parser.add_argument("--atlas-valid-sign", type=int, choices=(-1, 1), default=-1)
    parser.add_argument(
        "--extra-birth-face", type=int, nargs=3, action="append", default=[]
    )
    parser.add_argument(
        "--extra-birth-edge", type=int, nargs=2, action="append", default=[]
    )
    args = parser.parse_args()
    vertex = args.vertex
    birth_neighbour = args.birth_neighbour
    death_neighbour = args.death_neighbour
    old_edge = tuple(sorted((vertex, death_neighbour)))
    new_edge = tuple(sorted((vertex, birth_neighbour)))
    birth_faces = BIRTH_FACES + tuple(tuple(row) for row in args.extra_birth_face)
    birth_edges = BIRTH_EDGES + tuple(
        tuple(sorted(row)) for row in args.extra_birth_edge
    )

    labels, source = load_points(args.source)
    index = {label: offset for offset, label in enumerate(labels)}
    source_audit = json.loads(args.audit.read_text())
    rails = {
        tuple(sorted(edge))
        for edge in source_audit["fresh_hull_audit"]["forced_rail_edges"]
    }
    atlas = json.loads(args.birth_atlas.read_text())
    adaptive = json.loads(args.adaptive.read_text())
    search = Search(labels, source, rails, report=False)
    remote_basis = np.asarray([
        atlas["remote_basis"]["tangent"], atlas["remote_basis"]["normal"]
    ])
    controls = [
        (int(row["label"]), np.asarray(row["direction"], dtype=float))
        for row in adaptive.get("local_controls", [])
    ]
    start = np.asarray(adaptive["trace"][-1]["parameters"], dtype=float)
    direction = np.asarray(adaptive["wall"]["direction"], dtype=float)

    def coordinates(t):
        parameters = start + float(t) * direction
        points = search.coordinates(parameters[:20])
        points[index[228]] += parameters[20] * remote_basis[0]
        points[index[228]] += parameters[21] * remote_basis[1]
        for offset, (label, control_direction) in enumerate(controls):
            points[index[label]] += parameters[22 + offset] * control_direction
        return points

    points_zero = coordinates(0.0)
    point_slopes = coordinates(1.0) - points_zero
    cycles, _ = _merge_coplanar_facets(points_zero, ConvexHull(points_zero))

    def exact_points(t):
        return [
            tuple(
                Fraction.from_float(float(points_zero[row, axis]))
                + t * Fraction.from_float(float(point_slopes[row, axis]))
                for axis in range(3)
            )
            for row in range(len(labels))
        ]

    def exact_numerators(t):
        points = exact_points(t)
        volume = Fraction(0)
        moment = (Fraction(0), Fraction(0), Fraction(0))
        for cycle in cycles:
            for offset in range(1, len(cycle) - 1):
                triangle = (
                    points[cycle[0]], points[cycle[offset]], points[cycle[offset + 1]]
                )
                determinant = det3(triangle)
                volume += determinant
                moment = add(moment, scale(
                    determinant, add(add(triangle[0], triangle[1]), triangle[2])
                ))
        point_vertex = points[index[vertex]]
        cleared = sub(moment, scale(4 * volume, point_vertex))
        return {
            neighbour: dot(
                cleared, sub(points[index[neighbour]], point_vertex)
            )
            for neighbour in (birth_neighbour, death_neighbour)
        }, volume

    polynomials = {}
    for neighbour, orientation in (
        (birth_neighbour, 1), (death_neighbour, -1)
    ):
        coefficients = interpolate_consecutive([
            orientation * exact_numerators(Fraction(t))[0][neighbour]
            for t in range(6)
        ])
        for check in (Fraction(1, 3), Fraction(-2, 7), Fraction(7, 5)):
            assert (
                orientation * exact_numerators(check)[0][neighbour]
                == poly_value(coefficients, check)
            )
        lo = Fraction(0)
        hi = Fraction.from_float(max(4.0e-4, 2 * adaptive["wall"]["step_hi"]))
        assert poly_value(coefficients, lo) < 0 < poly_value(coefficients, hi)
        for _ in range(args.isolation_steps):
            mid = (lo + hi) / 2
            if poly_value(coefficients, mid) < 0:
                lo = mid
            else:
                hi = mid
        root = float((lo + hi) / 2)
        sturm = sturm_sequence(coefficients)
        assert sturm_root_count(sturm, Fraction(0), lo) == 0
        assert sturm_root_count(sturm, lo, hi) == 1
        polynomials[neighbour] = {
            "orientation": orientation,
            "coefficients": coefficients,
            "integers": primitive_integer_coefficients(coefficients),
            "lo": lo,
            "hi": hi,
            "root": root,
            "sturm_root_count_before_interval": 0,
            "sturm_root_count_in_interval": 1,
        }

    left = polynomials[birth_neighbour]
    right = polynomials[death_neighbour]
    assert left["hi"] < right["lo"]
    centre11 = (left["lo"] + left["hi"]) / 2
    centre9 = (right["lo"] + right["hi"]) / 2
    root_gap = centre9 - centre11
    directed_times = {
        "pre": centre11 - root_gap / 2,
        "middle": (centre11 + centre9) / 2,
        "far": centre9 + root_gap / 2,
    }

    circuit_specs = [
        (tuple(row["circuit"]), int(row["valid_sign"]))
        for row in adaptive["circuit_guards"]
    ]

    def sample(name, t_fraction, path):
        points = coordinates(float(t_fraction))
        mechanics = evaluate(labels, points)
        exact_mechanics = evaluate(labels, points, strict=0.0)
        record = summarize(labels, points, rails)
        write_csv(path, labels, points)
        signed_circuits = {}
        for circuit, sign in circuit_specs:
            rows = np.c_[points[[index[label] for label in circuit]], np.ones(4)]
            determinant = float(np.linalg.det(rows))
            signed_circuits[str(list(circuit))] = {
                "valid_sign": sign,
                "determinant": determinant,
                "signed_determinant": sign * determinant,
            }
        birth_values = {
            **{f"S{face}": mechanics.face_decisions[face] for face in birth_faces},
            **{f"H{edge}": mechanics.edge_decisions[edge] for edge in birth_edges},
        }
        keep_values = {
            "S(7,8,245)": mechanics.face_decisions[(7, 8, 245)],
            "U54": mechanics.vertex_decisions[54],
            "H(6,7)": mechanics.edge_decisions[(6, 7)],
        }
        exact_values, volume = exact_numerators(t_fraction)
        return {
            "name": name,
            "t": rational(t_fraction),
            "coordinates": str(path.resolve()),
            "class": list(mechanics.cls),
            "class_zero_threshold": list(exact_mechanics.cls),
            "f_vector": [mechanics.vertices, mechanics.edges, mechanics.faces],
            "active_labels": list(mechanics.active_labels),
            "stable_faces": sorted(sorted(face) for face in mechanics.stable_faces),
            "unstable_vertices": sorted(mechanics.unstable_vertices),
            "saddle_edges": sorted(sorted(edge) for edge in mechanics.saddle_edges),
            "base_face_present": record["base_face_present"],
            "missing_forced_rails": record["missing_forced_rails"],
            "u8_present": 8 in mechanics.unstable_vertices,
            "centroid": mechanics.centroid.tolist(),
            f"N{death_neighbour}_exact": str(exact_values[death_neighbour]),
            f"N{birth_neighbour}_exact": str(exact_values[birth_neighbour]),
            "volume_sum_exact": str(volume),
            f"U{vertex}": mechanics.vertex_decisions[vertex],
            "H" + str(old_edge): mechanics.edge_decisions[old_edge],
            "H" + str(new_edge): mechanics.edge_decisions[new_edge],
            "keep_decisions": keep_values,
            "linked_birth_guards": birth_values,
            "circuit_guards": signed_circuits,
            "min_nonzero_margin": mechanics.min_nonzero_margin,
        }

    samples = {
        "pre": sample("pre", directed_times["pre"], args.pre_csv),
        "middle": sample("middle", directed_times["middle"], args.middle_csv),
        "far": sample("far", directed_times["far"], args.far_csv),
    }
    assert samples["pre"]["class"] == [2, 2, 2]
    assert samples["middle"]["class"] == [2, 3, 3]
    assert samples["far"]["class"] == [2, 2, 2]
    for row in samples.values():
        assert row["class"] == row["class_zero_threshold"]
        assert row["f_vector"] == [61, 162, 103]
        assert len(row["active_labels"]) == 61
        assert row["base_face_present"] and row["u8_present"]
        assert not row["missing_forced_rails"]
        assert all(value < 0.0 for value in row["linked_birth_guards"].values())
        assert all(
            value["signed_determinant"] > 0.0
            for value in row["circuit_guards"].values()
        )
    assert list(old_edge) in samples["pre"]["saddle_edges"]
    assert vertex not in samples["pre"]["unstable_vertices"]
    assert list(new_edge) not in samples["pre"]["saddle_edges"]
    assert list(old_edge) in samples["middle"]["saddle_edges"]
    assert vertex in samples["middle"]["unstable_vertices"]
    assert list(new_edge) in samples["middle"]["saddle_edges"]
    assert list(old_edge) not in samples["far"]["saddle_edges"]
    assert vertex not in samples["far"]["unstable_vertices"]
    assert list(new_edge) in samples["far"]["saddle_edges"]

    polynomial_payload = {}
    for neighbour, row in polynomials.items():
        polynomial_payload[str(neighbour)] = {
            "formula": (
                f"orientation*dot(M-4*V*p{vertex}, "
                f"p{neighbour}-p{vertex})"
            ),
            "orientation": row["orientation"],
            "maximum_degree": 5,
            "actual_degree": len(row["integers"]) - 1,
            "primitive_integer_polynomial_low_to_high": [
                str(value) for value in row["integers"]
            ],
            "rational_coefficients_low_to_high": [
                rational(value) for value in row["coefficients"]
            ],
            "exact_root_isolating_interval": {
                "lo": rational(row["lo"]),
                "hi": rational(row["hi"]),
                "lo_value": str(poly_value(row["coefficients"], row["lo"])),
                "hi_value": str(poly_value(row["coefficients"], row["hi"])),
                "width": float(row["hi"] - row["lo"]),
            },
            "root_float": row["root"],
            "sturm_root_count_before_interval": row[
                "sturm_root_count_before_interval"
            ],
            "sturm_root_count_in_interval": row[
                "sturm_root_count_in_interval"
            ],
        }

    pre_parameters = (start + float(directed_times["pre"]) * direction).tolist()
    pre_atlas = {
        "version": 1,
        "scope": (
            f"exact pre cell before U{vertex}/H{new_edge} birth"
        ),
        "source": str(args.source.resolve()),
        "certificate": str(args.output.resolve()),
        "circuit": list(args.atlas_circuit),
        "valid_sign": args.atlas_valid_sign,
        "bypass_waypoints": [pre_parameters],
        "local_controls": adaptive.get("local_controls", []),
        "inherited_circuit_guards": adaptive["circuit_guards"],
        "pre_sample": samples["pre"],
    }
    args.pre_atlas.write_text(json.dumps(pre_atlas, indent=2, sort_keys=True) + "\n")

    far_parameters = (start + float(directed_times["far"]) * direction).tolist()
    far_atlas = {
        "version": 1,
        "scope": f"exact far cell after H{old_edge}->H{new_edge} transfer",
        "source": str(args.source.resolve()),
        "certificate": str(args.output.resolve()),
        "circuit": list(args.atlas_circuit),
        "valid_sign": args.atlas_valid_sign,
        "bypass_waypoints": [far_parameters],
        "local_controls": adaptive.get("local_controls", []),
        "inherited_circuit_guards": adaptive["circuit_guards"],
        "far_sample": samples["far"],
    }
    args.far_atlas.write_text(json.dumps(far_atlas, indent=2, sort_keys=True) + "\n")

    payload = {
        "version": 1,
        "scope": (
            f"exact two-numerator, three-cell vertex-{vertex} carrier transfer"
        ),
        "source": str(args.source.resolve()),
        "adaptive": str(args.adaptive.resolve()),
        "centroid_identity": "C=M/(4*V)",
        "shared_numerator_identities": {
            f"N{birth_neighbour}": (
                f"shared by U{vertex} neighbour {birth_neighbour} and "
                f"H{new_edge} endpoint"
            ),
            f"N{death_neighbour}": (
                f"shared by U{vertex} neighbour {death_neighbour} and "
                f"H{old_edge} endpoint"
            ),
        },
        "polynomials": polynomial_payload,
        "exact_root_order": [
            f"N{birth_neighbour}: birth U{vertex},H{new_edge}",
            f"N{death_neighbour}: death H{old_edge},U{vertex}",
        ],
        "root_gap": {
            "exact_directed_centre_gap": rational(root_gap),
            "float": float(root_gap),
        },
        "samples": samples,
        "transition": {
            "classes": [[2, 2, 2], [2, 3, 3], [2, 2, 2]],
            "pre": f"H{old_edge}",
            "middle": f"H{old_edge}+U{vertex}+H{new_edge}",
            "far": f"H{new_edge}",
            "hull_unchanged": True,
            "base_u8_all37_rails_preserved": True,
        },
        "far_atlas": str(args.far_atlas.resolve()),
        "pre_atlas": str(args.pre_atlas.resolve()),
        "passed": True,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "passed": True,
        "roots": {str(k): v["root"] for k, v in polynomials.items()},
        "root_gap": float(root_gap),
        "classes": [samples[name]["class"] for name in ("pre", "middle", "far")],
        "degrees": {str(k): len(v["integers"]) - 1 for k, v in polynomials.items()},
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
