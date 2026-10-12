#!/usr/bin/env python3
"""Exact/directed verifier for a linked stable-face/saddle-edge birth wall.

For triangle (8,245,246), loss of the face-foot inequality at edge (8,245)
and loss of the corresponding edge-cone coefficient share one geometric
numerator.  With V the oriented-volume sum and M its first-moment numerator,
the own centroid is C=M/(4V).  After clearing 4V, the common numerator is

  < (p245-p8) x (M-4 V p8),
    (p245-p8) x (p246-p8) >.

Along the saved affine continuation line this is an exact dyadic polynomial
of degree at most seven.  The script reconstructs that polynomial, isolates
its root rationally, and audits fresh hulls on both directed sides.
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
from scipy.optimize import brentq
from scipy.spatial import ConvexHull


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from actual_hull_mechanics import _merge_coplanar_facets, evaluate  # noqa: E402
from optimize_base_escape import Search  # noqa: E402
from search_row54_remote228 import load_points, summarize  # noqa: E402


DEFAULT_FACE = (8, 245, 246)
DEFAULT_EDGE = (8, 245)
KEEP = (("face", (7, 8, 245)), ("vertex", 54), ("edge", (6, 7)), ("edge", (9, 10)))


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
    """Power coefficients from f(0),...,f(n) using forward differences."""
    differences = list(values)
    forward = []
    while differences:
        forward.append(differences[0])
        differences = [
            right - left for left, right in zip(differences, differences[1:])
        ]
    result = [Fraction(0)]
    falling = [Fraction(1)]
    factorial = 1
    for degree, coefficient in enumerate(forward):
        if degree:
            falling = poly_mul(falling, [Fraction(-(degree - 1)), Fraction(1)])
            factorial *= degree
        term_scale = coefficient / factorial
        if len(result) < len(falling):
            result.extend([Fraction(0)] * (len(falling) - len(result)))
        for index, value in enumerate(falling):
            result[index] += term_scale * value
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def primitive_integer_coefficients(coefficients):
    denominator = reduce(
        math.lcm, (value.denominator for value in coefficients), 1
    )
    integers = [
        value.numerator * (denominator // value.denominator)
        for value in coefficients
    ]
    divisor = reduce(math.gcd, (abs(value) for value in integers if value), 0)
    integers = [value // divisor for value in integers]
    if integers[-1] < 0:
        integers = [-value for value in integers]
    return integers


def polynomial_value(coefficients, value):
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
    parser.add_argument(
        "--face", type=int, nargs=3, default=DEFAULT_FACE,
        metavar=("A", "B", "C"),
        help="stable face born at the common own-centroid numerator",
    )
    parser.add_argument(
        "--edge", type=int, nargs=2, default=DEFAULT_EDGE,
        metavar=("A", "B"),
        help="saddle edge born at the same numerator",
    )
    parser.add_argument("--isolation-steps", type=int, default=90)
    parser.add_argument("--directed-power", type=int, default=26)
    args = parser.parse_args()
    face = tuple(args.face)
    edge = tuple(args.edge)
    if not set(edge) <= set(face):
        raise ValueError(("edge must lie in face", edge, face))
    a_label, b_label = edge
    c_label = next(label for label in face if label not in edge)

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

    def decision_pair(t):
        mechanics = evaluate(labels, coordinates(t))
        return (
            mechanics.face_decisions[face],
            mechanics.edge_decisions[edge],
        )

    points_zero = coordinates(0.0)
    points_one = coordinates(1.0)
    point_slopes = points_one - points_zero
    hull = ConvexHull(points_zero)
    cycles, _ = _merge_coplanar_facets(points_zero, hull)

    def exact_points(t):
        return [
            tuple(
                Fraction.from_float(float(points_zero[row, axis]))
                + t * Fraction.from_float(float(point_slopes[row, axis]))
                for axis in range(3)
            )
            for row in range(len(labels))
        ]

    def exact_common_numerator(t):
        points = exact_points(t)
        volume = Fraction(0)
        moment = (Fraction(0), Fraction(0), Fraction(0))
        for cycle in cycles:
            for offset in range(1, len(cycle) - 1):
                triangle = (
                    points[cycle[0]],
                    points[cycle[offset]],
                    points[cycle[offset + 1]],
                )
                determinant = det3(triangle)
                volume += determinant
                moment = add(moment, scale(
                    determinant,
                    add(add(triangle[0], triangle[1]), triangle[2]),
                ))
        # Orient the formula from the requested edge, with the remaining face
        # vertex providing the normal.  This is the shared cleared numerator
        # for the face-foot and edge-cone inequalities.
        a, b, c = (
            points[index[a_label]], points[index[b_label]], points[index[c_label]]
        )
        edge_direction = sub(b, a)
        face_normal = cross(edge_direction, sub(c, a))
        cleared_centroid = sub(moment, scale(4 * volume, a))
        numerator = dot(
            cross(edge_direction, cleared_centroid), face_normal
        )
        return numerator, volume

    exact_samples = [
        exact_common_numerator(Fraction(t))[0] for t in range(8)
    ]
    rational_coefficients = interpolate_consecutive(exact_samples)
    orientation = -1 if exact_samples[0] > 0 else 1
    rational_coefficients = [orientation * value for value in rational_coefficients]
    integer_coefficients = primitive_integer_coefficients(rational_coefficients)

    # Independent exact interpolation checks away from its construction nodes.
    interpolation_checks = []
    for t in (Fraction(1, 3), Fraction(7, 5), Fraction(-2, 7)):
        direct = orientation * exact_common_numerator(t)[0]
        interpolated = polynomial_value(rational_coefficients, t)
        interpolation_checks.append({
            "t": {"numerator": t.numerator, "denominator": t.denominator},
            "residual": str(direct - interpolated),
        })
        assert direct == interpolated

    estimate = 0.5 * (
        adaptive["wall"]["step_lo"] + adaptive["wall"]["step_hi"]
    )
    lo = Fraction.from_float(max(0.0, estimate - 1e-4))
    hi = Fraction.from_float(estimate + 1e-4)
    lo_sign = polynomial_value(rational_coefficients, lo)
    hi_sign = polynomial_value(rational_coefficients, hi)
    if not (lo_sign < 0 < hi_sign):
        raise ValueError(("common numerator not bracketed", lo_sign, hi_sign))
    for _ in range(args.isolation_steps):
        mid = (lo + hi) / 2
        value = polynomial_value(rational_coefficients, mid)
        if value > 0:
            hi = mid
        else:
            lo = mid
    root_float = brentq(
        lambda t: float(polynomial_value(
            rational_coefficients, Fraction.from_float(float(t))
        )),
        float(lo - Fraction(1, 2 ** 40)),
        float(hi + Fraction(1, 2 ** 40)),
        xtol=5e-15,
        rtol=1e-14,
    )

    centre = (lo + hi) / 2
    directed_epsilon = Fraction(1, 2 ** args.directed_power)
    minus_t, plus_t = centre - directed_epsilon, centre + directed_epsilon
    exact_minus = polynomial_value(rational_coefficients, minus_t)
    exact_plus = polynomial_value(rational_coefficients, plus_t)
    assert exact_minus < 0 < exact_plus

    circuit_specs = [
        (tuple(row["circuit"]), int(row["valid_sign"]))
        for row in adaptive["circuit_guards"]
    ]

    def directed_sample(name, t_fraction, csv_path):
        t = float(t_fraction)
        points = coordinates(t)
        mechanics = evaluate(labels, points)
        record = summarize(labels, points, rails)
        write_csv(csv_path, labels, points)
        circuit_values = {}
        for circuit, sign in circuit_specs:
            rows = np.c_[
                points[[index[label] for label in circuit]], np.ones(4)
            ]
            circuit_values[str(list(circuit))] = {
                "valid_sign": sign,
                "determinant": float(np.linalg.det(rows)),
                "signed_determinant": sign * float(np.linalg.det(rows)),
            }
        keep_values = {}
        for kind, key in KEEP:
            if kind == "face":
                value = mechanics.face_decisions[key]
            elif kind == "vertex":
                value = mechanics.vertex_decisions[key]
            else:
                value = mechanics.edge_decisions[key]
            keep_values[f"{kind}:{key}"] = value
        return {
            "name": name,
            "t": {
                "numerator": t_fraction.numerator,
                "denominator": t_fraction.denominator,
            },
            "coordinates": str(csv_path.resolve()),
            "exact_common_numerator_value": str(
                polynomial_value(rational_coefficients, t_fraction)
            ),
            "face_birth_decision": mechanics.face_decisions[face],
            "edge_birth_decision": mechanics.edge_decisions[edge],
            "keep_decisions": keep_values,
            "class": record["class"],
            "f_vector": record["f_vector"],
            "active_labels": record["active_labels"],
            "centroid": record["centroid"],
            "stable_faces": sorted(sorted(face) for face in record["stable_faces"]),
            "unstable_vertices": sorted(record["unstable_vertices"]),
            "saddle_edges": sorted(sorted(edge) for edge in record["saddle_edges"]),
            "base_face_present": record["base_face_present"],
            "missing_forced_rails": record["missing_forced_rails"],
            "circuit_guards": circuit_values,
            "min_nonzero_margin": mechanics.min_nonzero_margin,
        }

    minus = directed_sample("minus", minus_t, args.minus_csv)
    plus = directed_sample("plus", plus_t, args.plus_csv)
    assert minus["class"] == [2, 2, 2]
    assert plus["class"] == [3, 2, 3]
    assert minus["f_vector"] == [61, 162, 103] == plus["f_vector"]
    assert len(minus["active_labels"]) == 61 == len(plus["active_labels"])
    assert minus["base_face_present"] and plus["base_face_present"]
    assert not minus["missing_forced_rails"] and not plus["missing_forced_rails"]
    assert minus["face_birth_decision"] < 0 < plus["face_birth_decision"]
    assert minus["edge_birth_decision"] < 0 < plus["edge_birth_decision"]
    assert all(
        row["signed_determinant"] > 0
        for sample in (minus, plus)
        for row in sample["circuit_guards"].values()
    )
    faces_added = sorted(
        set(map(tuple, plus["stable_faces"]))
        - set(map(tuple, minus["stable_faces"]))
    )
    edges_added = sorted(
        set(map(tuple, plus["saddle_edges"]))
        - set(map(tuple, minus["saddle_edges"]))
    )
    assert faces_added == [face]
    assert edges_added == [edge]

    # Numerical roots of the two conditioned decisions independently.
    decision_roots = []
    for offset, name in enumerate(("S(8,245,246)", "H(8,245)")):
        root = brentq(
            lambda t, i=offset: decision_pair(t)[i],
            estimate - 1e-6,
            estimate + 1e-6,
            xtol=5e-15,
            rtol=1e-14,
        )
        decision_roots.append({"feature": name, "root": root})

    payload = {
        "version": 1,
        "scope": "exact common-numerator and directed fresh-hull audit of stage-8 linked birth",
        "source": str(args.source.resolve()),
        "adaptive": str(args.adaptive.resolve()),
        "common_numerator_geometry": {
            "face": list(face),
            "edge": list(edge),
            "formula": (
                f"dot(cross(p{b_label}-p{a_label}, M-4*V*p{a_label}), "
                f"cross(p{b_label}-p{a_label}, p{c_label}-p{a_label}))"
            ),
            "centroid_identity": "C=M/(4*V)",
            "maximum_degree": 7,
            "actual_degree": len(integer_coefficients) - 1,
        },
        "primitive_integer_polynomial_low_to_high": [
            str(value) for value in integer_coefficients
        ],
        "rational_coefficients_low_to_high": [
            {"numerator": str(value.numerator), "denominator": str(value.denominator)}
            for value in rational_coefficients
        ],
        "interpolation_checks": interpolation_checks,
        "exact_root_isolating_interval": {
            "lo": {"numerator": lo.numerator, "denominator": lo.denominator},
            "hi": {"numerator": hi.numerator, "denominator": hi.denominator},
            "lo_value": str(polynomial_value(rational_coefficients, lo)),
            "hi_value": str(polynomial_value(rational_coefficients, hi)),
            "width": float(hi - lo),
        },
        "root_float": root_float,
        "independent_conditioned_roots": decision_roots,
        "conditioned_root_separation": abs(
            decision_roots[1]["root"] - decision_roots[0]["root"]
        ),
        "directed_epsilon": {
            "numerator": directed_epsilon.numerator,
            "denominator": directed_epsilon.denominator,
        },
        "minus": minus,
        "plus": plus,
        "mechanical_transition": {
            "class": [[2, 2, 2], [3, 2, 3]],
            "stable_faces_added": [list(face) for face in faces_added],
            "saddle_edges_added": [list(edge) for edge in edges_added],
            "hull_unchanged": True,
        },
        "passed": True,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "passed": True,
        "degree": len(integer_coefficients) - 1,
        "root_float": root_float,
        "conditioned_root_separation": payload["conditioned_root_separation"],
        "mechanical_transition": payload["mechanical_transition"],
        "isolation_width": payload["exact_root_isolating_interval"]["width"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
