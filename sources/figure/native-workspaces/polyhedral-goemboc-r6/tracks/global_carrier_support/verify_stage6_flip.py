#!/usr/bin/env python3
"""Standalone verifier for the stage-6 carrier diagonal flip.

The common event numerator is the oriented affine determinant of rows
(7,8,245,246).  Its coefficients are reconstructed as exact dyadic rationals
from the saved affine path, normalized to a primitive integer polynomial, and
paired with a rational isolating interval.  Directed samples on both sides
receive independent fresh-hull/own-centroid audits.
"""

from __future__ import annotations

import argparse
import csv
from fractions import Fraction
from functools import reduce
import itertools
import json
import math
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import brentq


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
from actual_hull_mechanics import evaluate  # noqa: E402
from optimize_base_escape import Search  # noqa: E402
from search_row54_remote228 import load_points, summarize  # noqa: E402


CIRCUIT = (7, 8, 245, 246)
BASE = list(range(17)) + [54]


def parity(permutation):
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def poly_mul(left, right):
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def determinant_polynomial(affine_rows):
    result = [Fraction(0)]
    for permutation in itertools.permutations(range(4)):
        term = [Fraction(parity(permutation))]
        for row, column in enumerate(permutation):
            if column == 3:
                factor = [Fraction(1)]
            else:
                intercept, slope = affine_rows[row][column]
                factor = [intercept, slope]
            term = poly_mul(term, factor)
        if len(result) < len(term):
            result.extend([Fraction(0)] * (len(term) - len(result)))
        for degree, coefficient in enumerate(term):
            result[degree] += coefficient
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def primitive_integer_coefficients(coefficients):
    denominator = reduce(math.lcm, (value.denominator for value in coefficients), 1)
    integers = [value.numerator * (denominator // value.denominator) for value in coefficients]
    divisor = reduce(math.gcd, (abs(value) for value in integers if value), 0)
    integers = [value // divisor for value in integers]
    if integers[-1] < 0:
        integers = [-value for value in integers]
    return integers


def integer_poly_value(coefficients, value):
    result = Fraction(0)
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


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
    parser.add_argument("--minus-csv", type=Path, required=True)
    parser.add_argument("--plus-csv", type=Path, required=True)
    parser.add_argument("--dyadic-power", type=int, default=20)
    args = parser.parse_args()

    labels, source = load_points(args.source)
    index = {label: offset for offset, label in enumerate(labels)}
    source_audit = json.loads(args.audit.read_text())
    rails = {
        tuple(sorted(edge))
        for edge in source_audit["fresh_hull_audit"]["forced_rail_edges"]
    }
    birth_atlas = json.loads(args.birth_atlas.read_text())
    adaptive = json.loads(args.adaptive.read_text())
    search = Search(labels, source, rails, report=False)
    remote_basis = np.asarray([
        birth_atlas["remote_basis"]["tangent"],
        birth_atlas["remote_basis"]["normal"],
    ])
    start = np.asarray(adaptive["trace"][-1]["parameters"], dtype=float)
    direction = np.asarray(adaptive["wall"]["direction"], dtype=float)
    estimate = 0.5 * (
        adaptive["wall"]["step_lo"] + adaptive["wall"]["step_hi"]
    )

    def coordinates(t):
        parameters = start + t * direction
        points = search.coordinates(parameters[:20])
        points[index[228]] += parameters[20] * remote_basis[0]
        points[index[228]] += parameters[21] * remote_basis[1]
        return points

    def determinant(t):
        points = coordinates(t)
        rows = np.c_[points[[index[label] for label in CIRCUIT]], np.ones(4)]
        return float(np.linalg.det(rows))

    lo, hi = estimate - 1e-3, estimate + 1e-3
    while determinant(lo) * determinant(hi) > 0.0:
        lo -= hi - lo
        hi += hi - lo
    root = brentq(determinant, lo, hi, xtol=5e-15, rtol=1e-14)

    points_zero = coordinates(0.0)
    points_one = coordinates(1.0)
    affine_rows = []
    for label in CIRCUIT:
        row = []
        for coordinate in range(3):
            intercept = Fraction.from_float(float(points_zero[index[label], coordinate]))
            slope = Fraction.from_float(float(
                points_one[index[label], coordinate] - points_zero[index[label], coordinate]
            ))
            row.append((intercept, slope))
        affine_rows.append(row)
    rational_coefficients = determinant_polynomial(affine_rows)
    integer_coefficients = primitive_integer_coefficients(rational_coefficients)

    centre = Fraction.from_float(root)
    epsilon = Fraction(1, 2 ** args.dyadic_power)
    minus_t, plus_t = centre - epsilon, centre + epsilon
    minus_sign = integer_poly_value(integer_coefficients, minus_t)
    plus_sign = integer_poly_value(integer_coefficients, plus_t)
    assert minus_sign * plus_sign < 0

    def directed_sample(name, t_fraction, csv_path):
        t = float(t_fraction)
        points = coordinates(t)
        mechanics = evaluate(labels, points)
        record = summarize(labels, points, rails)
        write_csv(csv_path, labels, points)
        return {
            "name": name,
            "t": {"numerator": t_fraction.numerator, "denominator": t_fraction.denominator},
            "determinant_double": determinant(t),
            "exact_integer_numerator_value": str(
                integer_poly_value(integer_coefficients, t_fraction)
            ),
            "coordinates": str(csv_path.resolve()),
            "f_vector": record["f_vector"],
            "class": record["class"],
            "active_labels": record["active_labels"],
            "inactive_labels": sorted(set(labels) - set(record["active_labels"])),
            "stable_faces": sorted(sorted(face) for face in record["stable_faces"]),
            "unstable_vertices": sorted(record["unstable_vertices"]),
            "saddle_edges": sorted(sorted(edge) for edge in record["saddle_edges"]),
            "centroid": record["centroid"],
            "base_face_present": record["base_face_present"],
            "stable_base": record["stable_base"],
            "missing_forced_rails": record["missing_forced_rails"],
            "min_nonzero_margin": mechanics.min_nonzero_margin,
            "face_decisions_local": {
                str(list(face)): value
                for face, value in mechanics.face_decisions.items()
                if set(face) <= set(CIRCUIT) and len(face) == 3
            },
            "edge_decisions_local": {
                str(list(edge)): value
                for edge, value in mechanics.edge_decisions.items()
                if set(edge) <= set(CIRCUIT)
            },
            "all_face_keys": [list(face) for face in sorted(mechanics.face_decisions)],
            "all_edge_keys": [list(edge) for edge in sorted(mechanics.edge_decisions)],
        }

    minus = directed_sample("minus", minus_t, args.minus_csv)
    plus = directed_sample("plus", plus_t, args.plus_csv)
    expected_base = sorted(BASE)
    assert minus["class"] == [2, 2, 2] == plus["class"]
    assert minus["f_vector"] == [61, 162, 103] == plus["f_vector"]
    assert minus["inactive_labels"] == [] == plus["inactive_labels"]
    assert minus["base_face_present"] and plus["base_face_present"]
    assert minus["stable_base"] and plus["stable_base"]
    assert not minus["missing_forced_rails"] and not plus["missing_forced_rails"]
    assert minus["unstable_vertices"] == [8, 54] == plus["unstable_vertices"]
    assert minus["saddle_edges"] == [[6, 7], [9, 10]] == plus["saddle_edges"]
    assert minus["stable_faces"] == [expected_base, [7, 8, 245]]
    assert plus["stable_faces"] == [expected_base, [7, 8, 246]]

    minus_faces, plus_faces = set(map(tuple, minus["all_face_keys"])), set(map(tuple, plus["all_face_keys"]))
    minus_edges, plus_edges = set(map(tuple, minus["all_edge_keys"])), set(map(tuple, plus["all_edge_keys"]))
    topology = {
        "faces_removed": [list(face) for face in sorted(minus_faces - plus_faces)],
        "faces_added": [list(face) for face in sorted(plus_faces - minus_faces)],
        "edges_removed": [list(edge) for edge in sorted(minus_edges - plus_edges)],
        "edges_added": [list(edge) for edge in sorted(plus_edges - minus_edges)],
    }
    assert topology == {
        "faces_removed": [[7, 8, 245], [8, 245, 246]],
        "faces_added": [[7, 8, 246], [7, 245, 246]],
        "edges_removed": [[8, 245]],
        "edges_added": [[7, 246]],
    }

    discriminant = (
        integer_coefficients[1] ** 2
        - 4 * integer_coefficients[2] * integer_coefficients[0]
        if len(integer_coefficients) == 3 else None
    )
    payload = {
        "version": 1,
        "scope": "standalone exact-dyadic numerator plus directed actual-hull verifier",
        "event": "diagonal flip transfers extra stable face; it is not an S-H annihilation",
        "circuit": list(CIRCUIT),
        "common_event_numerator": {
            "variable": "t",
            "coefficient_order": "constant_to_highest",
            "primitive_integer_coefficients": [str(value) for value in integer_coefficients],
            "degree": len(integer_coefficients) - 1,
            "discriminant": None if discriminant is None else str(discriminant),
            "root_double": root,
            "root_residual_double": determinant(root),
            "isolating_interval": {
                "lo": {"numerator": minus_t.numerator, "denominator": minus_t.denominator},
                "hi": {"numerator": plus_t.numerator, "denominator": plus_t.denominator},
            },
        },
        "minus": minus,
        "plus": plus,
        "topology_change": topology,
        "replacement_feature": [7, 8, 246],
        "verdict": {
            "all_assertions_passed": True,
            "post_is_211_or_111": False,
            "post_is_strict_transfer_222": True,
            "base_U8_all37rails_all61_preserved": True,
        },
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "root": root,
        "root_residual": determinant(root),
        "integer_polynomial_degree": len(integer_coefficients) - 1,
        "minus": {key: minus[key] for key in (
            "f_vector", "class", "stable_faces", "unstable_vertices",
            "saddle_edges", "missing_forced_rails", "inactive_labels",
        )},
        "plus": {key: plus[key] for key in (
            "f_vector", "class", "stable_faces", "unstable_vertices",
            "saddle_edges", "missing_forced_rails", "inactive_labels",
        )},
        "topology_change": topology,
        "verdict": payload["verdict"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
