#!/usr/bin/env python3
"""Exact/interval audit of the row-230-loss wall; no integration output."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path

import numpy as np


sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
ATTACK = HERE.parents[1]
TRACK = ATTACK.parent
ROOT = HERE.parents[4]
MAIN = ATTACK / "continuation" / "main"

SOURCE = MAIN / "exact_full_control_chain_far.csv"
FACES_PATH = MAIN / "exact_full_control_chain_post_faces.json"
PARENT_BUILDER = MAIN / "build_exact_full_control_chain.py"
PARENT_VERIFIER = MAIN / "verify_exact_full_control_chain.py"
PARENT_CERTIFICATE = MAIN / "exact_full_control_chain_certificate.json"
PARENT_MANIFEST = MAIN / "PACKAGE_MANIFEST.json"
PARENT_RAY_SOURCE = ATTACK / "exact_circuit_far.csv"
PARENT_RAY_ENDPOINT = MAIN / "full_control_candidate.csv"
OUTPUT = HERE / "row230_chart_audit.json"
REPORT = HERE / "AUDIT.md"

sys.path.insert(0, str(TRACK / "rigorous_local_bypass"))
import exact_core as ex  # noqa: E402


BASE = frozenset(range(17)) | {54}
PRIMARY = (7, 8, 245)
TARGETS = {
    "S": ("face", PRIMARY, (8, 245)),
    "U54": ("vertex", 54, 1),
    "H56": ("edge", (5, 6), "one_minus_t"),
    "H1011": ("edge", (10, 11), "t"),
}
PROTECTED = {
    "stable": [sorted(BASE), list(PRIMARY)],
    "unstable": [8, 54],
    "saddles": [[5, 6], [10, 11]],
}
EXPECTED_ACTIVE = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    54, 69, 72, 73, 88, 198, 224, 228, 229, 230, 231, 232, 233,
    234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245,
    246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
    258, 259, 260, 261, 262, 263, 264,
]

CIRCUIT = (198, 229, 230, 231)
CURRENT_DANGER = (
    (83, (198, 230, 231), 229),
    (97, (198, 229, 230), 231),
    (102, (229, 231, 230), 198),
)
INCIDENT_FACES = {83, 97, 102}
COLLAPSING_SPOKES = {(198, 230), (229, 230), (230, 231)}
BOUNDARY_CYCLE = (198, 229, 231)
LOCAL_INTERVAL_EPSILON = Q(1, 10**20)
ROOT_WIDTH = Q(1, 10**30)


def qs(value: Q) -> str:
    return ex.qs(Q(value))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def polynomial_digest(polynomial: ex.P) -> str:
    return canonical_hash(polynomial.exact())


def exact_scalar_record(value: Q, include_exact=False):
    value = Q(value)
    text = qs(value)
    record = {
        "sign": 0 if not value else (1 if value > 0 else -1),
        "decimal": float(value),
        "exact_digest": hashlib.sha256(text.encode()).hexdigest(),
        "numerator_decimal_digits": len(str(abs(value.numerator))),
        "denominator_decimal_digits": len(str(value.denominator)),
    }
    if include_exact:
        record["exact"] = text
    return record


def rail_set() -> set[tuple[int, int]]:
    rails = set()
    for route in (
        [228] + list(range(229, 247)) + [8],
        [228] + list(range(247, 265)) + [8],
    ):
        rails.update(tuple(sorted(edge)) for edge in zip(route, route[1:]))
    rails.remove((228, 229))
    return rails


def edge_set(faces) -> set[tuple[int, int]]:
    return {
        tuple(sorted((a, b)))
        for cycle in faces
        for a, b in zip(cycle, cycle[1:] + cycle[:1])
    }


def primitive_rows(path, faces):
    ledger = ex.mechanics_primitives(path, faces)
    yield "volume_d6", ledger["d6"], "mechanics_denominator"
    for face_index, witness, polynomial in ex.support_polynomials(path, faces):
        yield f"support:f{face_index}:w{witness}", polynomial, "support"
    for face_key, rows in sorted(ledger["reference"].items()):
        for edge, polynomial in sorted(rows.items()):
            yield f"face_reference:{face_key}:{edge}", polynomial, "face_reference"
    for face_key, rows in sorted(ledger["face"].items()):
        for edge, polynomial in sorted(rows.items()):
            yield f"face_raw:{face_key}:{edge}", polynomial, "face_raw"
    for vertex, rows in sorted(ledger["vertex"].items()):
        for neighbor, polynomial in sorted(rows.items()):
            yield f"vertex:{vertex}:{neighbor}", polynomial, "vertex"
    for edge, rows in sorted(ledger["edge"].items()):
        for component in (
            "direction_norm2", "gram", "t", "one_minus_t", "beta1", "beta2"
        ):
            yield f"edge:{edge}:{component}", rows[component], "edge"


def trim(coefficients):
    result = list(coefficients)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result or [Q(0)]


def divmod_poly(numerator, denominator):
    numerator = trim(numerator)
    denominator = trim(denominator)
    if denominator == [Q(0)]:
        raise ZeroDivisionError
    quotient = [Q(0)] * max(1, len(numerator) - len(denominator) + 1)
    while len(numerator) >= len(denominator) and numerator != [Q(0)]:
        shift = len(numerator) - len(denominator)
        factor = numerator[-1] / denominator[-1]
        quotient[shift] += factor
        for index, coefficient in enumerate(denominator):
            numerator[index + shift] -= factor * coefficient
        numerator = trim(numerator)
    return trim(quotient), numerator


def factor_multiplicity(polynomial: ex.P, factor: ex.P):
    multiplicity = 0
    cofactor = polynomial
    while cofactor.degree >= factor.degree:
        quotient, remainder = divmod_poly(cofactor.c, factor.c)
        if remainder != [Q(0)]:
            break
        multiplicity += 1
        cofactor = ex.P(tuple(quotient))
    return multiplicity, cofactor


def sign_record(polynomial: ex.P, lo: Q, hi: Q):
    sign, leaves, worst = ex.bernstein_sign(polynomial, lo, hi, max_depth=60)
    return {
        "sign": sign,
        "bernstein_leaf_count": leaves,
        "minimum_bernstein_log10_abs": worst,
        "degree": polynomial.degree,
        "digest": polynomial_digest(polynomial),
    }


def rational_rank(rows) -> tuple[int, list[int]]:
    matrix = [list(row) for row in rows]
    rank = 0
    pivots = []
    if not matrix:
        return 0, []
    for column in range(len(matrix[0])):
        pivot = next(
            (index for index in range(rank, len(matrix)) if matrix[index][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        scale = matrix[rank][column]
        matrix[rank] = [value / scale for value in matrix[rank]]
        for index in range(len(matrix)):
            if index == rank or not matrix[index][column]:
                continue
            scale = matrix[index][column]
            matrix[index] = [
                value - scale * pivot_value
                for value, pivot_value in zip(matrix[index], matrix[rank])
            ]
        pivots.append(column)
        rank += 1
        if rank == len(matrix):
            break
    return rank, pivots


@dataclass(frozen=True)
class QJet:
    value: Q
    derivative: tuple[Q, ...]

    @staticmethod
    def constant(value, dimension):
        return QJet(Q(value), (Q(0),) * dimension)

    def coerce(self, other):
        return other if isinstance(other, QJet) else QJet.constant(other, len(self.derivative))

    def __add__(self, other):
        other = self.coerce(other)
        return QJet(
            self.value + other.value,
            tuple(a + b for a, b in zip(self.derivative, other.derivative)),
        )

    __radd__ = __add__

    def __neg__(self):
        return QJet(-self.value, tuple(-value for value in self.derivative))

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        return QJet(
            self.value * other.value,
            tuple(
                a * other.value + self.value * b
                for a, b in zip(self.derivative, other.derivative)
            ),
        )

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        denominator = other.value * other.value
        return QJet(
            self.value / other.value,
            tuple(
                (a * other.value - self.value * b) / denominator
                for a, b in zip(self.derivative, other.derivative)
            ),
        )


def jet_value(value):
    return value.value if isinstance(value, QJet) else value.v


def jet_derivatives(value):
    return value.derivative if isinstance(value, QJet) else value.d


def chart_modes(points):
    base_u = ex.sub(points[1], points[0])
    base_v = ex.sub(points[2], points[0])
    normal = ex.cross(base_u, base_v)
    if not any(normal):
        raise AssertionError("degenerate base chart basis")
    for label in BASE:
        if ex.dot(normal, ex.sub(points[label], points[0])):
            raise AssertionError(("base row outside exact plane", label))
    names = []
    vectors = []
    for label in sorted(points):
        if label in BASE:
            directions = (("u", base_u), ("v", base_v))
        else:
            directions = tuple(
                (axis_name, tuple(Q(int(axis == index)) for axis in range(3)))
                for index, axis_name in enumerate("xyz")
            )
        for axis_name, direction in directions:
            names.append((label, axis_name))
            vectors.append((label, direction))
    if len(names) != 165:
        raise AssertionError(("unexpected chart dimension", len(names)))
    return names, vectors, base_u, base_v, normal


def qjet_points(points, mode_vectors):
    dimension = len(mode_vectors)
    by_label = {}
    for index, (label, direction) in enumerate(mode_vectors):
        by_label.setdefault(label, []).append((index, direction))
    result = {}
    for label, point in points.items():
        coordinates = []
        for axis, value in enumerate(point):
            derivative = [Q(0)] * dimension
            for index, direction in by_label[label]:
                derivative[index] = direction[axis]
            coordinates.append(QJet(value, tuple(derivative)))
        result[label] = tuple(coordinates)
    return result


def local_context(points, faces):
    d6, m24 = ex.exact_centroid_numerators(points, faces)
    scale = 4 * d6
    xscaled = {
        label: tuple(scale * point[axis] - m24[axis] for axis in range(3))
        for label, point in points.items()
    }
    incidence, neighbors, face_by_key = ex.edge_data(faces)
    return {
        "points": points,
        "faces": faces,
        "d6": d6,
        "scale": scale,
        "xscaled": xscaled,
        "incidence": incidence,
        "neighbors": neighbors,
        "face_by_key": face_by_key,
    }


def face_cycle(context, face_key):
    return context["faces"][context["face_by_key"][tuple(sorted(face_key))]]


def face_normal(context, face_key):
    return ex.cycle_normal(face_cycle(context, face_key), context["points"])


def directed_cycle_edge(cycle, edge):
    edge = tuple(sorted(edge))
    for a, b in zip(cycle, cycle[1:] + cycle[:1]):
        if tuple(sorted((a, b))) == edge:
            return a, b
    raise KeyError((cycle, edge))


def face_fraction(context, face_key, edge):
    points = context["points"]
    cycle = face_cycle(context, face_key)
    normal = face_normal(context, face_key)
    nn = ex.norm2(normal)
    a, b = directed_cycle_edge(cycle, edge)
    direction = ex.sub(points[b], points[a])
    dd = ex.norm2(direction)
    hbar = ex.dot(normal, context["xscaled"][a])
    raw = ex.dot(
        ex.cross(
            direction,
            ex.sub(ex.mul(normal, hbar), ex.mul(context["xscaled"][a], nn)),
        ),
        normal,
    )
    numerator = raw * raw
    denominator = context["scale"] * context["scale"] * dd * nn * nn * nn
    return numerator, denominator


def vertex_fraction(context, vertex, neighbor):
    points = context["points"]
    direction = ex.sub(points[neighbor], points[vertex])
    raw = -ex.dot(context["xscaled"][vertex], direction)
    numerator = raw * raw
    denominator = ex.norm2(context["xscaled"][vertex]) * ex.norm2(direction)
    return numerator, denominator


def edge_quantities(context, edge, include_beta=True):
    points = context["points"]
    i, j = tuple(sorted(edge))
    direction = ex.sub(points[j], points[i])
    dd = ex.norm2(direction)
    t_value = -ex.dot(context["xscaled"][i], direction)
    one_minus_t = context["scale"] * dd - t_value
    components = {
        "direction_norm2": dd,
        "t": t_value,
        "one_minus_t": one_minus_t,
    }
    fractions = {
        "t": (
            t_value * t_value,
            context["scale"] * context["scale"] * dd * dd,
        ),
        "one_minus_t": (
            one_minus_t * one_minus_t,
            context["scale"] * context["scale"] * dd * dd,
        ),
    }
    if not include_beta:
        return components, fractions
    face_a, face_b = context["incidence"][(i, j)]
    n1 = ex.cycle_normal(context["faces"][face_a], points)
    n2 = ex.cycle_normal(context["faces"][face_b], points)
    aa, ab, cc = ex.norm2(n1), ex.dot(n1, n2), ex.norm2(n2)
    r1 = ex.dot(context["xscaled"][i], n1)
    r2 = ex.dot(context["xscaled"][i], n2)
    beta1 = r1 * cc - r2 * ab
    beta2 = r2 * aa - r1 * ab
    gram = aa * cc - ab * ab
    closest = ex.add(
        ex.mul(context["xscaled"][i], dd), ex.mul(direction, t_value)
    )
    closest_norm2 = ex.norm2(closest)
    gram2 = gram * gram
    components.update({"beta1": beta1, "beta2": beta2, "gram": gram})
    fractions.update({
        "beta1": (
            beta1 * beta1 * dd * dd * aa,
            gram2 * closest_norm2,
        ),
        "beta2": (
            beta2 * beta2 * dd * dd * cc,
            gram2 * closest_norm2,
        ),
    })
    return components, fractions


def fraction_value(pair):
    return pair[0] / pair[1]


def source_selectors(points, faces):
    context = local_context(points, faces)
    face_rows = {}
    for name, face_key in (("S", PRIMARY), ("base", tuple(sorted(BASE)))):
        cycle = face_cycle(context, face_key)
        rows = {
            tuple(sorted((a, b))): fraction_value(
                face_fraction(context, face_key, (a, b))
            )
            for a, b in zip(cycle, cycle[1:] + cycle[:1])
        }
        selected = min(rows, key=rows.get)
        if list(rows.values()).count(rows[selected]) != 1:
            raise AssertionError((name, "non-strict selected component"))
        face_rows[name] = (selected, rows)
    vertex_rows = {}
    for name, vertex in (("U54", 54), ("U8", 8)):
        rows = {
            neighbor: fraction_value(vertex_fraction(context, vertex, neighbor))
            for neighbor in context["neighbors"][vertex]
        }
        selected = min(rows, key=rows.get)
        if list(rows.values()).count(rows[selected]) != 1:
            raise AssertionError((name, "non-strict selected component"))
        vertex_rows[name] = (selected, rows)
    edge_rows = {}
    for name, edge in (("H56", (5, 6)), ("H1011", (10, 11))):
        components, rows = edge_quantities(context, edge, include_beta=True)
        del components
        values = {key: fraction_value(value) for key, value in rows.items()}
        selected = min(values, key=values.get)
        if list(values.values()).count(values[selected]) != 1:
            raise AssertionError((name, "non-strict selected component"))
        edge_rows[name] = (selected, values)
    h910_components, _ = edge_quantities(context, (9, 10), include_beta=True)
    h910_key = min(
        ("t", "one_minus_t", "beta1", "beta2"),
        key=lambda key: h910_components[key],
    )
    if h910_components[h910_key] >= 0:
        raise AssertionError("H910 is not strictly dead")
    expected = {
        "S": (8, 245),
        "U54": 1,
        "H56": "one_minus_t",
        "H1011": "t",
        "base": (10, 11),
        "U8": 7,
        "H910": "one_minus_t",
    }
    actual = {
        "S": face_rows["S"][0],
        "U54": vertex_rows["U54"][0],
        "H56": edge_rows["H56"][0],
        "H1011": edge_rows["H1011"][0],
        "base": face_rows["base"][0],
        "U8": vertex_rows["U8"][0],
        "H910": h910_key,
    }
    if actual != expected:
        raise AssertionError(("unexpected source selectors", actual))
    return actual, {
        "S": face_rows["S"][1],
        "base": face_rows["base"][1],
        "U54": vertex_rows["U54"][1],
        "U8": vertex_rows["U8"][1],
        "H56": edge_rows["H56"][1],
        "H1011": edge_rows["H1011"][1],
        "H910": h910_components,
    }


def support_expression(points, face, witness):
    a, b, c = (points[label] for label in face[:3])
    return ex.det3(
        ex.sub(b, a), ex.sub(c, a), ex.sub(points[witness], a)
    )


def support_orientation(points, faces, face_index):
    cycle = faces[face_index]
    values = []
    for witness in sorted(set(points) - set(cycle)):
        value = support_expression(points, cycle, witness)
        scalar = value.value if isinstance(value, QJet) else value
        if scalar:
            values.append(scalar)
    if not values or any((value > 0) != (values[0] > 0) for value in values):
        raise AssertionError(("mixed support orientation", face_index))
    return 1 if values[0] > 0 else -1


def selected_fraction(context, name, selectors):
    if name == "S":
        return face_fraction(context, PRIMARY, selectors[name])
    if name == "base":
        return face_fraction(context, tuple(sorted(BASE)), selectors[name])
    if name == "U54":
        return vertex_fraction(context, 54, selectors[name])
    if name == "U8":
        return vertex_fraction(context, 8, selectors[name])
    edge = (5, 6) if name == "H56" else (10, 11)
    _components, fractions = edge_quantities(context, edge, include_beta=False)
    return fractions[selectors[name]]


def pairing(row, vector):
    return sum((a * b for a, b in zip(row, vector)), Q(0))


def physical_velocity(coefficients, mode_vectors, labels):
    velocity = {label: [Q(0), Q(0), Q(0)] for label in labels}
    for coefficient, (label, direction) in zip(coefficients, mode_vectors):
        if not coefficient:
            continue
        for axis in range(3):
            velocity[label][axis] += coefficient * direction[axis]
    return {label: tuple(value) for label, value in velocity.items()}


def rational_direction(relative_rows, desired, project_wall=False):
    matrix = np.asarray(
        [[float(value) for value in row] for row in relative_rows], dtype=float
    )
    norms = np.linalg.norm(matrix, axis=1)
    if np.any(norms == 0):
        raise AssertionError("zero tangent row")
    scaled = matrix / norms[:, None]
    candidate, _residuals, rank, _singular = np.linalg.lstsq(
        scaled, np.asarray(desired, dtype=float), rcond=None
    )
    if rank != len(relative_rows):
        raise AssertionError(("numerical proposer row rank", rank))
    denominator = 10**12
    exact = [Q(int(round(value * denominator)), denominator) for value in candidate]
    pivot = None
    if project_wall:
        wall = relative_rows[4]
        pivot = max(range(len(wall)), key=lambda index: abs(float(wall[index])))
        if not wall[pivot]:
            raise AssertionError("wall projection pivot vanished")
        exact[pivot] -= pairing(wall, exact) / wall[pivot]
        if pairing(wall, exact):
            raise AssertionError("wall projection is not exact")
    rates = [pairing(row, exact) for row in relative_rows]
    expected_signs = (-1, -1, -1, -1, 0 if project_wall else 1, 1, 1, -1)
    for name, rate, expected in zip(
        ("S", "U54", "H56", "H1011", "wall", "base", "U8", "H910"),
        rates,
        expected_signs,
    ):
        if expected == 0 and rate != 0:
            raise AssertionError((name, "nonzero projected rate", qs(rate)))
        if expected > 0 and rate <= 0:
            raise AssertionError((name, "nonpositive rate", qs(rate)))
        if expected < 0 and rate >= 0:
            raise AssertionError((name, "nonnegative rate", qs(rate)))
    return exact, rates, pivot


def rational_tangent_audit(points, faces, mode_names, mode_vectors, selectors):
    jet_points = qjet_points(points, mode_vectors)
    context = local_context(jet_points, faces)
    selected = {}
    for name in ("S", "U54", "H56", "H1011", "base", "U8"):
        numerator, denominator = selected_fraction(context, name, selectors)
        selected[name] = numerator / denominator
    h910_components, _ = edge_quantities(context, (9, 10), include_beta=False)
    h910 = h910_components[selectors["H910"]]
    orientations = [support_orientation(points, faces, row[0]) for row in CURRENT_DANGER]
    wall_rows = [
        orientation * support_expression(jet_points, face, witness)
        for orientation, (_index, face, witness) in zip(orientations, CURRENT_DANGER)
    ]
    if any(row != wall_rows[0] for row in wall_rows[1:]):
        raise AssertionError("three current dangerous support jets are not identical")
    wall = wall_rows[0]
    if wall.value <= 0:
        raise AssertionError("source is not on the current safe side")
    rows = [selected[name].derivative for name in ("S", "U54", "H56", "H1011")]
    rows.extend((wall.derivative, selected["base"].derivative, selected["U8"].derivative, h910.derivative))
    scales = [
        selected["S"].value,
        selected["U54"].value,
        selected["H56"].value,
        selected["H1011"].value,
        wall.value,
        selected["base"].value,
        selected["U8"].value,
        abs(h910.value),
    ]
    relative_rows = [
        tuple(value / scale for value in row) for row, scale in zip(rows, scales)
    ]
    inward, inward_rates, _ = rational_direction(
        relative_rows, (-1, -1, -1, -1, 1, 1, 1, -1)
    )
    tangent, tangent_rates, tangent_pivot = rational_direction(
        relative_rows, (-1, -1, -1, -1, 0, 1, 1, -1), project_wall=True
    )
    target_rank, _ = rational_rank(rows[:4])
    augmented_rank, _ = rational_rank(rows[:5])
    cone_rank, cone_pivots = rational_rank(rows)
    wall_rank, wall_pivots = rational_rank([row.derivative for row in wall_rows])
    if (target_rank, augmented_rank, cone_rank, wall_rank) != (4, 5, 8, 1):
        raise AssertionError((target_rank, augmented_rank, cone_rank, wall_rank))
    inward_velocity = physical_velocity(inward, mode_vectors, points)
    tangent_velocity = physical_velocity(tangent, mode_vectors, points)
    for velocity in (inward_velocity, tangent_velocity):
        for label in BASE:
            if ex.dot(ex.cross(ex.sub(points[1], points[0]), ex.sub(points[2], points[0])), velocity[label]):
                raise AssertionError(("base velocity leaves plane", label))
    def direction_record(coefficients, rates, velocity, pivot=None):
        coefficient_rows = [
            {
                "column": index,
                "mode": [mode_names[index][0], mode_names[index][1]],
                "coefficient": qs(value),
            }
            for index, value in enumerate(coefficients) if value
        ]
        velocity_exact = {
            str(label): [qs(value) for value in velocity[label]]
            for label in sorted(velocity)
        }
        return {
            "nonzero_coefficient_count": len(coefficient_rows),
            "coefficients": coefficient_rows,
            "coefficient_digest": canonical_hash(coefficient_rows),
            "physical_velocity_digest": canonical_hash(velocity_exact),
            "physical_linf_decimal": max(
                abs(float(value)) for row in velocity.values() for value in row
            ),
            "exact_relative_rates": {
                name: exact_scalar_record(value)
                for name, value in zip(
                    ("S", "U54", "H56", "H1011", "wall", "base", "U8", "H910"), rates
                )
            },
            "projection_pivot": pivot,
        }
    source_values = {
        name: exact_scalar_record(selected[name].value)
        for name in ("S", "U54", "H56", "H1011", "base", "U8")
    }
    source_values["wall_signed_support"] = exact_scalar_record(
        wall.value, include_exact=True
    )
    source_values["H910_one_minus_t"] = exact_scalar_record(h910.value)
    nonzero_wall_gradient = [
        {
            "column": index,
            "mode": [mode_names[index][0], mode_names[index][1]],
            "coefficient": qs(value),
        }
        for index, value in enumerate(wall.derivative) if value
    ]
    return {
        "dimension": len(mode_names),
        "base_mode_count": 2 * len(BASE),
        "nonbase_mode_count": 3 * (len(points) - len(BASE)),
        "basis": "exact fixed-base-plane u/v modes plus Cartesian nonbase modes",
        "mode_names_digest": canonical_hash([list(row) for row in mode_names]),
        "source_selectors": {
            key: list(value) if isinstance(value, tuple) else value
            for key, value in selectors.items()
        },
        "source_exact_values": source_values,
        "wall_family_row_rank": wall_rank,
        "wall_tangent_nullity": len(mode_names) - wall_rank,
        "target_row_rank": target_rank,
        "wall_plus_target_row_rank": augmented_rank,
        "eight_guard_row_rank": cone_rank,
        "eight_guard_common_kernel_nullity": len(mode_names) - cone_rank,
        "wall_pivot_columns": wall_pivots,
        "eight_guard_pivot_columns": cone_pivots,
        "wall_gradient_nonzero": nonzero_wall_gradient,
        "wall_gradient_digest": canonical_hash([qs(value) for value in wall.derivative]),
        "relative_row_digest": canonical_hash(
            [[qs(value) for value in row] for row in relative_rows]
        ),
        "inward_rational_witness": direction_record(
            inward, inward_rates, inward_velocity
        ),
        "far_level_tangent_rational_witness": direction_record(
            tangent, tangent_rates, tangent_velocity, tangent_pivot
        ),
        "gordan_farkas_required": False,
        "gordan_farkas_reason": "exact strict primal witnesses exist",
    }, {
        "rows": rows,
        "relative_rows": relative_rows,
        "wall": wall,
        "inward_coefficients": inward,
        "tangent_coefficients": tangent,
        "inward_velocity": inward_velocity,
        "tangent_velocity": tangent_velocity,
    }


def evaluate_path(path, parameter):
    return {
        label: tuple(polynomial.eval(parameter) for polynomial in point)
        for label, point in path.items()
    }


def replacement_face_ledger(faces):
    removed = {tuple(sorted(face)) for _index, face, _witness in CURRENT_DANGER}
    kept = [face for face in faces if tuple(sorted(face)) not in removed]
    if len(faces) - len(kept) != 3:
        raise AssertionError("row-230 star is not exactly three faces")
    return kept + [list(BOUNDARY_CYCLE)]


def parent_ray_path(points):
    parent = json.loads(PARENT_CERTIFICATE.read_text())
    ray_source = ex.read_rows(PARENT_RAY_SOURCE)
    ray_endpoint = ex.read_rows(PARENT_RAY_ENDPOINT)
    far_parameter = Q(parent["path"]["far_parameter"])
    velocity = {
        label: tuple(
            ray_endpoint[label][axis] - ray_source[label][axis]
            for axis in range(3)
        )
        for label in points
    }
    reconstructed = {
        label: tuple(
            ray_source[label][axis] + far_parameter * velocity[label][axis]
            for axis in range(3)
        )
        for label in points
    }
    if reconstructed != points:
        raise AssertionError("far checkpoint is not on the parent exact ray")
    path = {
        label: tuple(ex.P((points[label][axis], velocity[label][axis])) for axis in range(3))
        for label in points
    }
    stored = parent["path"]["next_forbidden_event"]
    lo = Q(stored["lo"]) - far_parameter
    hi = Q(stored["hi"]) - far_parameter
    return parent, path, velocity, far_parameter, lo, hi


def support_family_on_path(path, faces):
    family = []
    target = support_expression(path, CURRENT_DANGER[0][1], CURRENT_DANGER[0][2])
    for face_index, witness, polynomial in ex.support_polynomials(path, faces):
        ratio = ex.proportional(polynomial, target)
        if ratio is not None:
            family.append({
                "name": f"support:f{face_index}:w{witness}",
                "face_index": face_index,
                "face": faces[face_index],
                "witness": witness,
                "ratio_to_raw_delta": qs(ratio),
            })
    return target, family


def incident_primitive_records(rows_by_name, target, root):
    records = []
    names = []
    for face_index, face, witness in CURRENT_DANGER:
        names.append(f"support:f{face_index}:w{witness}")
        key = tuple(sorted(face))
        for edge in (
            tuple(sorted((face[0], face[1]))),
            tuple(sorted((face[1], face[2]))),
            tuple(sorted((face[2], face[0]))),
        ):
            names.append(f"face_reference:{key}:{edge}")
            names.append(f"face_raw:{key}:{edge}")
    for vertex, neighbor in (
        (230, 198), (230, 229), (230, 231),
        (198, 230), (229, 230), (231, 230),
    ):
        names.append(f"vertex:{vertex}:{neighbor}")
    for edge in sorted(COLLAPSING_SPOKES):
        for component in (
            "direction_norm2", "gram", "t", "one_minus_t", "beta1", "beta2"
        ):
            names.append(f"edge:{edge}:{component}")
    for name in names:
        polynomial, family = rows_by_name[name]
        multiplicity, cofactor = factor_multiplicity(polynomial, target)
        bounded = cofactor if multiplicity else polynomial
        records.append({
            "name": name,
            "family": family,
            "degree": polynomial.degree,
            "delta_factor_multiplicity": multiplicity,
            "polynomial_digest": polynomial_digest(polynomial),
            "bounded_factor": sign_record(bounded, root["lo"], root["hi"]),
        })
    return records


def barycentric_wall_audit(path, root):
    origin = 198
    u = ex.sub(path[229], path[origin])
    v = ex.sub(path[231], path[origin])
    w = ex.sub(path[230], path[origin])
    candidates = []
    for first, second in ((0, 1), (0, 2), (1, 2)):
        denominator = u[first] * v[second] - u[second] * v[first]
        alpha_numerator = w[first] * v[second] - w[second] * v[first]
        beta_numerator = u[first] * w[second] - u[second] * w[first]
        denominator_sign = sign_record(denominator, root["lo"], root["hi"])["sign"]
        if denominator_sign < 0:
            denominator = -denominator
            alpha_numerator = -alpha_numerator
            beta_numerator = -beta_numerator
        gamma_numerator = denominator - alpha_numerator - beta_numerator
        records = {
            "alpha_for_229": sign_record(alpha_numerator, root["lo"], root["hi"]),
            "beta_for_231": sign_record(beta_numerator, root["lo"], root["hi"]),
            "gamma_for_198": sign_record(gamma_numerator, root["lo"], root["hi"]),
            "denominator": sign_record(denominator, root["lo"], root["hi"]),
        }
        if any(record["sign"] != 1 for record in records.values()):
            raise AssertionError(("nonpositive wall barycentric coordinate", first, second))
        midpoint = (root["lo"] + root["hi"]) / 2
        decimal = {
            "alpha_for_229": float(alpha_numerator.eval(midpoint) / denominator.eval(midpoint)),
            "beta_for_231": float(beta_numerator.eval(midpoint) / denominator.eval(midpoint)),
            "gamma_for_198": float(gamma_numerator.eval(midpoint) / denominator.eval(midpoint)),
        }
        candidates.append({
            "coordinate_axes": [first, second],
            "positive_interval_proofs": records,
            "decimal_at_bracket_midpoint": decimal,
            "polynomial_exact": {
                "alpha_numerator": alpha_numerator.exact(),
                "beta_numerator": beta_numerator.exact(),
                "gamma_numerator": gamma_numerator.exact(),
                "denominator": denominator.exact(),
            },
        })
    first = candidates[0]["decimal_at_bracket_midpoint"]
    for candidate in candidates[1:]:
        other = candidate["decimal_at_bracket_midpoint"]
        if max(abs(first[key] - other[key]) for key in first) > 1e-12:
            raise AssertionError("barycentric projections disagree")
    return {
        "identity_at_delta_zero": (
            "p230 = gamma*p198 + alpha*p229 + beta*p231; "
            "alpha,beta,gamma are all strictly positive and sum to one"
        ),
        "projections": candidates,
        "conclusion": "row 230 is strict interior to replacement triangle [198,229,231]",
    }


def polynomial_chart_points(path, mode_vectors):
    dimension = len(mode_vectors)
    zero = ex.P.zero()
    by_label = {}
    for index, (label, direction) in enumerate(mode_vectors):
        by_label.setdefault(label, []).append((index, direction))
    result = {}
    for label, point in path.items():
        coordinates = []
        for axis, polynomial in enumerate(point):
            derivative = [zero] * dimension
            for index, direction in by_label[label]:
                derivative[index] = ex.P((direction[axis],))
            coordinates.append(ex.JP(polynomial, tuple(derivative)))
        result[label] = tuple(coordinates)
    return result


def parent_wall_audit(points, faces, mode_names, mode_vectors):
    parent, path, parent_velocity, far_parameter, lo, hi = parent_ray_path(points)
    target, support_family = support_family_on_path(path, faces)
    root = ex.isolate_monotone_root(target, lo, hi, ROOT_WIDTH)
    if len(support_family) != 3:
        raise AssertionError(("incomplete exact support family", support_family))
    expected_family = {
        (face_index, tuple(face), witness)
        for face_index, face, witness in CURRENT_DANGER
    }
    actual_family = {
        (row["face_index"], tuple(row["face"]), row["witness"])
        for row in support_family
    }
    if actual_family != expected_family:
        raise AssertionError((actual_family, expected_family))

    all_rows = list(primitive_rows(path, faces))
    if len(all_rows) != 7904:
        raise AssertionError(("unexpected primitive count", len(all_rows)))
    rows_by_name = {
        name: (polynomial, family) for name, polynomial, family in all_rows
    }
    expected_zero = {
        f"support:f{face_index}:w{witness}": 1
        for face_index, _face, witness in CURRENT_DANGER
    }
    for edge in COLLAPSING_SPOKES:
        expected_zero[f"edge:{edge}:gram"] = 2
        expected_zero[f"edge:{edge}:beta1"] = 1
        expected_zero[f"edge:{edge}:beta2"] = 1
    zero_records = {}
    for name, multiplicity in expected_zero.items():
        polynomial, family = rows_by_name[name]
        actual_multiplicity, cofactor = factor_multiplicity(polynomial, target)
        if actual_multiplicity != multiplicity:
            raise AssertionError((name, actual_multiplicity, multiplicity))
        zero_records[name] = {
            "family": family,
            "degree": polynomial.degree,
            "delta_factor_multiplicity": actual_multiplicity,
            "polynomial_digest": polynomial_digest(polynomial),
            "cofactor": sign_record(cofactor, root["lo"], root["hi"]),
        }
    strict_digest = hashlib.sha256()
    strict_count = 0
    strict_leaves = 0
    strict_worst = None
    for name, polynomial, family in all_rows:
        if name in expected_zero:
            continue
        sign, leaves, worst = ex.bernstein_sign(
            polynomial, Q(0), root["hi"], max_depth=60
        )
        source_sign = 1 if polynomial.eval(Q(0)) > 0 else -1
        if sign != source_sign:
            raise AssertionError(("unexpected pre-wall sign change", name))
        strict_count += 1
        strict_leaves += leaves
        strict_worst = worst if strict_worst is None else min(strict_worst, worst)
        strict_digest.update(
            f"{name}|{family}|{sign}|{'|'.join(polynomial.exact())}\n".encode()
        )
    if strict_count != 7892:
        raise AssertionError(("strict primitive count", strict_count))

    incident = incident_primitive_records(rows_by_name, target, root)
    incident_support_names = {
        f"support:f{face_index}:w{witness}"
        for face_index in INCIDENT_FACES
        for witness in sorted(set(points) - set(faces[face_index]))
    }
    if len(incident_support_names) != 174:
        raise AssertionError(("incident support count", len(incident_support_names)))
    incident_support_digest = hashlib.sha256()
    incident_support_strict = 0
    for name in sorted(incident_support_names):
        polynomial, family = rows_by_name[name]
        multiplicity, cofactor = factor_multiplicity(polynomial, target)
        if multiplicity:
            if name not in expected_zero:
                raise AssertionError(("unexpected incident support factor", name))
        else:
            sign, _leaves, _worst = ex.bernstein_sign(
                polynomial, root["lo"], root["hi"], max_depth=60
            )
            incident_support_strict += 1
            incident_support_digest.update(
                f"{name}|{family}|{sign}|{'|'.join(polynomial.exact())}\n".encode()
            )
    if incident_support_strict != 171:
        raise AssertionError(incident_support_strict)

    wall_faces = replacement_face_ledger(faces)
    if edge_set(faces) - edge_set(wall_faces) != COLLAPSING_SPOKES:
        raise AssertionError("wrong edge loss at row-230 wall")
    if rail_set() - edge_set(wall_faces) != {(229, 230), (230, 231)}:
        raise AssertionError("wrong rail loss at row-230 wall")
    wall_support = list(ex.support_polynomials(path, wall_faces))
    replacement_index = next(
        index for index, face in enumerate(wall_faces)
        if tuple(face) == BOUNDARY_CYCLE
    )
    replacement_target = next(
        polynomial for index, witness, polynomial in wall_support
        if index == replacement_index and witness == 230
    )
    replacement_ratio = ex.proportional(replacement_target, target)
    if replacement_ratio != -1:
        raise AssertionError(("replacement support ratio", replacement_ratio))
    wall_support_digest = hashlib.sha256()
    wall_support_strict = 0
    for index, witness, polynomial in wall_support:
        if index == replacement_index and witness == 230:
            continue
        sign, _leaves, _worst = ex.bernstein_sign(
            polynomial, root["lo"], root["hi"], max_depth=60
        )
        wall_support_strict += 1
        wall_support_digest.update(
            f"support:f{index}:w{witness}|{sign}|{'|'.join(polynomial.exact())}\n".encode()
        )
    wall_mechanics = ex.certify_mechanics_interval(
        path, wall_faces, PROTECTED, root["lo"], root["hi"]
    )

    chart_points = polynomial_chart_points(path, mode_vectors)
    signed_wall = support_orientation(points, faces, 83) * support_expression(
        chart_points, faces[83], 229
    )
    wall_gradient = signed_wall.d
    nonzero_gradient = []
    midpoint = (root["lo"] + root["hi"]) / 2
    for index, polynomial in enumerate(wall_gradient):
        if polynomial == ex.P.zero():
            continue
        record = sign_record(polynomial, root["lo"], root["hi"])
        nonzero_gradient.append({
            "column": index,
            "mode": [mode_names[index][0], mode_names[index][1]],
            "polynomial_exact": polynomial.exact(),
            "interval": record,
            "midpoint_decimal": float(polynomial.eval(midpoint)),
        })
    if len(nonzero_gradient) != 12:
        raise AssertionError(("wall gradient support", len(nonzero_gradient)))
    if not any(row["interval"]["sign"] for row in nonzero_gradient):
        raise AssertionError("wall gradient vanishes")

    return {
        "parent_far_parameter": qs(far_parameter),
        "root_from_far": {
            "lo": qs(root["lo"]),
            "hi": qs(root["hi"]),
            "decimal_interval": [float(root["lo"]), float(root["hi"])],
            "raw_delta_value_lo": qs(root["value_lo"]),
            "raw_delta_value_hi": qs(root["value_hi"]),
            "raw_delta_derivative_sign": root["derivative_sign"],
            "raw_delta_polynomial_exact": target.exact(),
            "raw_delta_polynomial_digest": polynomial_digest(target),
        },
        "equation": (
            "Delta = det(p230-p198, p231-p198, p229-p198) = 0; "
            "the current-cell signed slack is sigma=-Delta"
        ),
        "current_support_family": support_family,
        "current_support_family_size": len(support_family),
        "replacement_support": {
            "face": list(BOUNDARY_CYCLE),
            "witness": 230,
            "ratio_to_raw_delta": qs(replacement_ratio),
            "interpretation": "opposite side of the same four-point determinant",
        },
        "four_orientations": {
            "current_support_rows": 3,
            "replacement_support_rows": 1,
            "current_signed_relation": "sigma=-Delta>=0",
            "replacement_signed_relation": "-sigma=Delta>=0",
        },
        "barycentric_interior": barycentric_wall_audit(path, root),
        "topology": {
            "current_f_vector": [61, 162, 103],
            "wall_f_vector": [60, 159, 101],
            "removed_faces": [list(face) for _index, face, _witness in CURRENT_DANGER],
            "replacement_face": list(BOUNDARY_CYCLE),
            "removed_spokes": [list(edge) for edge in sorted(COLLAPSING_SPOKES)],
            "removed_forced_rails": [[229, 230], [230, 231]],
            "remaining_forced_rails": 35,
            "inactive_row_at_and_beyond_wall": 230,
        },
        "complete_event_ledger": {
            "primitive_count": len(all_rows),
            "allowed_zero_primitive_count": len(expected_zero),
            "allowed_zero_primitives": zero_records,
            "strict_other_primitive_count": strict_count,
            "strict_other_bernstein_leaf_count": strict_leaves,
            "strict_other_minimum_bernstein_log10_abs": strict_worst,
            "strict_other_digest": strict_digest.hexdigest(),
        },
        "incident_closure": {
            "faces": [faces[index] for index in sorted(INCIDENT_FACES)],
            "collapsing_spokes": [list(edge) for edge in sorted(COLLAPSING_SPOKES)],
            "support_row_count_on_incident_faces": len(incident_support_names),
            "strict_incident_support_row_count": incident_support_strict,
            "strict_incident_support_digest": incident_support_digest.hexdigest(),
            "mechanics_and_zero_support_rows": incident,
            "factor_summary": (
                "each spoke gram has Delta^2; each spoke beta1/beta2 has Delta; "
                "direction_norm2,t,one_minus_t, face and directed vertex rows stay nonzero"
            ),
        },
        "replacement_wall_ledger": {
            "support_primitive_count": len(wall_support),
            "strict_support_count_excluding_interior_row230": wall_support_strict,
            "strict_support_digest": wall_support_digest.hexdigest(),
            "mechanics_interval": wall_mechanics,
        },
        "wall_gradient": {
            "ambient_chart_dimension": len(mode_names),
            "nonzero_component_count": len(nonzero_gradient),
            "nonzero_gradient_polynomials": nonzero_gradient,
            "gradient_polynomial_digest": canonical_hash(
                [polynomial.exact() for polynomial in wall_gradient]
            ),
            "rank_on_root_interval": 1,
            "nullity_on_root_interval": len(mode_names) - 1,
        },
        "parent_velocity_digest": canonical_hash({
            str(label): [qs(value) for value in parent_velocity[label]]
            for label in sorted(parent_velocity)
        }),
        "parent_next_forbidden_name": parent["path"]["next_forbidden_event"]["name"],
    }, {
        "path": path,
        "root": root,
        "target": target,
        "wall_faces": wall_faces,
        "wall_gradient": wall_gradient,
    }


def fraction_map(context, name):
    if name in ("S", "base"):
        face_key = PRIMARY if name == "S" else tuple(sorted(BASE))
        cycle = face_cycle(context, face_key)
        return {
            tuple(sorted((a, b))): face_fraction(context, face_key, (a, b))
            for a, b in zip(cycle, cycle[1:] + cycle[:1])
        }
    if name in ("U54", "U8"):
        vertex = 54 if name == "U54" else 8
        return {
            neighbor: vertex_fraction(context, vertex, neighbor)
            for neighbor in context["neighbors"][vertex]
        }
    edge = (5, 6) if name == "H56" else (10, 11)
    _components, fractions = edge_quantities(context, edge, include_beta=True)
    return fractions


def fraction_direction_numerator(pair, direction_index):
    numerator, denominator = pair
    return (
        jet_derivatives(numerator)[direction_index] * jet_value(denominator)
        - jet_value(numerator) * jet_derivatives(denominator)[direction_index]
    )


def polynomial_fraction_stability(context, selectors, lo, hi):
    digest = hashlib.sha256()
    count = 0
    records = {}
    for name in ("S", "U54", "H56", "H1011", "base", "U8"):
        rows = fraction_map(context, name)
        selected_key = selectors[name]
        selected_numerator, selected_denominator = rows[selected_key]
        numerator_record = sign_record(selected_numerator, lo, hi)
        denominator_record = sign_record(selected_denominator, lo, hi)
        if numerator_record["sign"] != 1 or denominator_record["sign"] != 1:
            raise AssertionError((name, "selected fraction is not positive"))
        minimum_gap = None
        for key, (numerator, denominator) in rows.items():
            denominator_sign = sign_record(denominator, lo, hi)["sign"]
            if denominator_sign != 1:
                raise AssertionError((name, key, "nonpositive denominator"))
            if key == selected_key:
                continue
            difference = (
                numerator * selected_denominator
                - selected_numerator * denominator
            )
            record = sign_record(difference, lo, hi)
            if record["sign"] != 1:
                raise AssertionError((name, selected_key, key, "selector changes"))
            minimum_gap = (
                record["minimum_bernstein_log10_abs"]
                if minimum_gap is None
                else min(minimum_gap, record["minimum_bernstein_log10_abs"])
            )
            count += 1
            digest.update(
                f"{name}|{selected_key}|{key}|{'|'.join(difference.exact())}\n".encode()
            )
        records[name] = {
            "selected_component": list(selected_key) if isinstance(selected_key, tuple) else selected_key,
            "competitor_count": len(rows) - 1,
            "minimum_cross_product_log10_abs": minimum_gap,
            "selected_numerator": numerator_record,
            "selected_denominator": denominator_record,
        }
    return {
        "records": records,
        "strict_competitor_count": count,
        "strict_competitor_digest": digest.hexdigest(),
    }


def directional_polynomial_points(path, directions):
    dimension = len(directions)
    result = {}
    for label, point in path.items():
        coordinates = []
        for axis, polynomial in enumerate(point):
            derivatives = tuple(
                ex.P((direction[label][axis],)) for direction in directions
            )
            if len(derivatives) != dimension:
                raise AssertionError("direction dimension mismatch")
            coordinates.append(ex.JP(polynomial, derivatives))
        result[label] = tuple(coordinates)
    return result


def mode_velocity(mode_vector, labels):
    label, direction = mode_vector
    result = {row: (Q(0), Q(0), Q(0)) for row in labels}
    result[label] = tuple(direction)
    return result


def directional_rows(context, selectors):
    rows = {}
    for name in ("S", "U54", "H56", "H1011", "base", "U8"):
        pair = selected_fraction(context, name, selectors)
        rows[name] = tuple(
            fraction_direction_numerator(pair, index)
            for index in range(len(jet_derivatives(pair[0])))
        )
    h910_components, _fractions = edge_quantities(
        context, (9, 10), include_beta=False
    )
    h910 = h910_components[selectors["H910"]]
    rows["H910"] = tuple(jet_derivatives(h910))
    rows["H910_value"] = jet_value(h910)
    return rows


def actual_wall_cone_audit(
    path,
    root,
    faces,
    mode_names,
    mode_vectors,
    selectors,
    inward_velocity,
    tangent_velocity,
    wall_gradient,
):
    polynomial_context = local_context(path, faces)
    selector_stability = polynomial_fraction_stability(
        polynomial_context, selectors, root["lo"], root["hi"]
    )
    orientation = support_orientation(evaluate_path(path, Q(0)), faces, 83)

    inward_points = directional_polynomial_points(path, [inward_velocity])
    inward_context = local_context(inward_points, faces)
    inward_rows = directional_rows(inward_context, selectors)
    inward_wall = orientation * support_expression(
        inward_points, faces[83], 229
    )
    inward_signs = {}
    desired = {
        "S": -1,
        "U54": -1,
        "H56": -1,
        "H1011": -1,
        "wall": 1,
        "base": 1,
        "U8": 1,
        "H910": -1,
    }
    for name in ("S", "U54", "H56", "H1011", "base", "U8"):
        record = sign_record(inward_rows[name][0], root["lo"], root["hi"])
        if record["sign"] != desired[name]:
            raise AssertionError(("inward wall-cone sign", name, record))
        inward_signs[name] = record
    wall_record = sign_record(
        inward_wall.d[0], root["lo"], root["hi"]
    )
    if wall_record["sign"] != 1:
        raise AssertionError(("inward support derivative", wall_record))
    inward_signs["wall"] = wall_record
    h910_record = sign_record(inward_rows["H910"][0], root["lo"], root["hi"])
    h910_value_record = sign_record(
        inward_rows["H910_value"], root["lo"], root["hi"]
    )
    if h910_record["sign"] != -1 or h910_value_record["sign"] != -1:
        raise AssertionError(("H910 wall interval", h910_record, h910_value_record))
    inward_signs["H910"] = h910_record
    inward_signs["H910_value"] = h910_value_record

    midpoint = (root["lo"] + root["hi"]) / 2
    candidate_columns = sorted(
        (index for index, polynomial in enumerate(wall_gradient) if polynomial != ex.P.zero()),
        key=lambda index: abs(float(wall_gradient[index].eval(midpoint))),
        reverse=True,
    )
    tangent_result = None
    checked = []
    for pivot in candidate_columns:
        pivot_velocity = mode_velocity(mode_vectors[pivot], path)
        tangent_points = directional_polynomial_points(
            path, [tangent_velocity, pivot_velocity]
        )
        tangent_context = local_context(tangent_points, faces)
        tangent_rows = directional_rows(tangent_context, selectors)
        tangent_wall = orientation * support_expression(
            tangent_points, faces[83], 229
        )
        a = tangent_wall.d[0]
        b = tangent_wall.d[1]
        try:
            b_record = sign_record(b, root["lo"], root["hi"])
        except AssertionError as error:
            checked.append({"pivot": pivot, "result": f"pivot-not-separated:{error}"})
            continue
        factor = 1 if b_record["sign"] > 0 else -1
        capital_a = factor * a
        capital_b = factor * b
        identity = capital_b * a - capital_a * b
        if identity != ex.P.zero():
            raise AssertionError("algebraic tangent fails wall annihilation identity")
        records = {}
        failed = None
        for name in ("S", "U54", "H56", "H1011", "base", "U8", "H910"):
            row = tangent_rows[name]
            polynomial = capital_b * row[0] - capital_a * row[1]
            try:
                record = sign_record(polynomial, root["lo"], root["hi"])
            except AssertionError as error:
                failed = f"{name}:unseparated:{error}"
                break
            if record["sign"] != desired[name]:
                failed = f"{name}:sign={record['sign']}"
                break
            records[name] = record
        checked.append({
            "pivot": pivot,
            "mode": [mode_names[pivot][0], mode_names[pivot][1]],
            "result": failed or "pass",
        })
        if failed is None:
            tangent_result = {
                "pivot_column": pivot,
                "pivot_mode": [mode_names[pivot][0], mode_names[pivot][1]],
                "positive_B_polynomial_exact": capital_b.exact(),
                "A_polynomial_exact": capital_a.exact(),
                "wall_annihilation_polynomial_exact": identity.exact(),
                "direction_definition": "v_tan(alpha)=B(alpha)*v_seed-A(alpha)*e_pivot",
                "directional_rows": records,
                "pivot_B_interval": sign_record(
                    capital_b, root["lo"], root["hi"]
                ),
            }
            break
    if tangent_result is None:
        raise AssertionError(("no algebraic wall-tangent pivot", checked))

    return {
        "selected_component_stability": selector_stability,
        "rational_inward_direction": {
            "interval_directional_signs": inward_signs,
            "conclusion": (
                "strictly decreases S,U54,H56,H1011, moves into sigma>0, "
                "does not worsen base/U8, and pushes H910 farther negative"
            ),
        },
        "algebraic_wall_tangent_direction": tangent_result,
        "pivot_candidates_checked": checked,
        "wall_equation_rank": 1,
        "wall_tangent_nullity": len(mode_names) - 1,
        "safe_tangent_cone_feasible": True,
        "wall_tangent_slice_feasible": True,
        "gordan_farkas_required": False,
        "gordan_farkas_reason": (
            "a rational strict inward primal witness and an exact algebraic "
            "wall-annihilating primal witness are both certified"
        ),
    }


def interval_primitive_audit(path, faces, lo, hi):
    digest = hashlib.sha256()
    count = 0
    leaves = 0
    worst = None
    for name, polynomial, family in primitive_rows(path, faces):
        sign, row_leaves, margin = ex.bernstein_sign(
            polynomial, lo, hi, max_depth=60
        )
        source_sign = 1 if polynomial.eval(lo) > 0 else -1
        if sign != source_sign:
            raise AssertionError(("local primitive sign changed", name))
        count += 1
        leaves += row_leaves
        worst = margin if worst is None else min(worst, margin)
        digest.update(
            f"{name}|{family}|{sign}|{'|'.join(polynomial.exact())}\n".encode()
        )
    return {
        "primitive_count": count,
        "bernstein_leaf_count": leaves,
        "minimum_bernstein_log10_abs": worst,
        "primitive_digest": digest.hexdigest(),
    }


def local_interval_audit(points, faces, selectors, velocity):
    path = {
        label: tuple(
            ex.P((points[label][axis], velocity[label][axis]))
            for axis in range(3)
        )
        for label in points
    }
    exhaustive = interval_primitive_audit(
        path, faces, Q(0), LOCAL_INTERVAL_EPSILON
    )
    if exhaustive["primitive_count"] != 7904:
        raise AssertionError(exhaustive)
    restricted = {
        label: tuple(polynomial.affine(Q(0), LOCAL_INTERVAL_EPSILON) for polynomial in point)
        for label, point in path.items()
    }
    class_cover = ex.certify_path_segment(restricted, faces, PROTECTED)
    endpoint = evaluate_path(path, LOCAL_INTERVAL_EPSILON)
    support = ex.supporting_cell(endpoint, faces)
    _ledger, mechanics = ex.classify_point(endpoint, faces)
    if support["f_vector"] != [61, 162, 103]:
        raise AssertionError(support)
    if support["active_labels"] != EXPECTED_ACTIVE:
        raise AssertionError(support["active_labels"])
    if mechanics["class"] != [2, 2, 2]:
        raise AssertionError(mechanics)
    missing_rails = rail_set() - set(support["edges"])
    if missing_rails:
        raise AssertionError(("local witness loses rails", sorted(missing_rails)))

    context = local_context(path, faces)
    selector_stability = polynomial_fraction_stability(
        context, selectors, Q(0), LOCAL_INTERVAL_EPSILON
    )
    directed = {}
    for name in ("S", "U54", "H56", "H1011", "base", "U8"):
        numerator, denominator = selected_fraction(context, name, selectors)
        derivative = (
            numerator.derivative() * denominator
            - numerator * denominator.derivative()
        )
        record = sign_record(derivative, Q(0), LOCAL_INTERVAL_EPSILON)
        expected = -1 if name in TARGETS else 1
        if record["sign"] != expected:
            raise AssertionError(("local directional sign", name, record))
        directed[name] = record
    h910_components, _fractions = edge_quantities(
        context, (9, 10), include_beta=False
    )
    h910 = h910_components[selectors["H910"]]
    h910_value = sign_record(h910, Q(0), LOCAL_INTERVAL_EPSILON)
    h910_derivative = sign_record(
        h910.derivative(), Q(0), LOCAL_INTERVAL_EPSILON
    )
    if h910_value["sign"] != -1 or h910_derivative["sign"] != -1:
        raise AssertionError((h910_value, h910_derivative))
    directed["H910_value"] = h910_value
    directed["H910_derivative"] = h910_derivative

    orientations = [support_orientation(points, faces, row[0]) for row in CURRENT_DANGER]
    danger = {}
    danger_polynomials = []
    for orientation, (face_index, face, witness) in zip(orientations, CURRENT_DANGER):
        polynomial = orientation * support_expression(path, face, witness)
        derivative_record = sign_record(
            polynomial.derivative(), Q(0), LOCAL_INTERVAL_EPSILON
        )
        value_record = sign_record(polynomial, Q(0), LOCAL_INTERVAL_EPSILON)
        if derivative_record["sign"] != 1 or value_record["sign"] != 1:
            raise AssertionError((face_index, witness, value_record, derivative_record))
        danger[f"support:f{face_index}:w{witness}"] = {
            "value": value_record,
            "derivative": derivative_record,
        }
        danger_polynomials.append(polynomial)
    if any(polynomial != danger_polynomials[0] for polynomial in danger_polynomials[1:]):
        raise AssertionError("local dangerous family ceases to be identical")

    endpoint_hash = canonical_hash({
        str(label): [qs(value) for value in endpoint[label]]
        for label in sorted(endpoint)
    })
    return {
        "purpose": "local existence/readback only; no candidate geometry is written",
        "epsilon": qs(LOCAL_INTERVAL_EPSILON),
        "exhaustive_support_and_mechanics": exhaustive,
        "class_cover": class_cover,
        "selected_component_stability": selector_stability,
        "directed_rows": directed,
        "dangerous_support_family": danger,
        "endpoint_readback": {
            "coordinate_hash": endpoint_hash,
            "f_vector": support["f_vector"],
            "class": mechanics["class"],
            "active_rows": len(support["active_labels"]),
            "base_present": BASE in {frozenset(face) for face in faces},
            "forced_rails": len(rail_set()),
            "missing_forced_rails": [],
            "H910_strictly_negative": True,
        },
    }


def source_checkpoint(points, faces):
    support = ex.supporting_cell(points, faces)
    ledger, mechanics = ex.classify_point(points, faces)
    if support["f_vector"] != [61, 162, 103]:
        raise AssertionError(support)
    if support["active_labels"] != EXPECTED_ACTIVE:
        raise AssertionError(support["active_labels"])
    if mechanics["class"] != [2, 2, 2]:
        raise AssertionError(mechanics)
    if BASE not in {frozenset(face) for face in faces}:
        raise AssertionError("base face absent")
    missing = rail_set() - set(support["edges"])
    if missing:
        raise AssertionError(("source rails absent", sorted(missing)))
    d6, m24 = ex.exact_centroid_numerators(points, faces)
    centroid = tuple(value / (4 * d6) for value in m24)
    h910 = ledger["edge"][(9, 10)]["one_minus_t"]
    if h910 >= 0:
        raise AssertionError("source H910 is not strictly negative")
    return {
        "coordinate_hash": canonical_hash({
            str(label): [qs(value) for value in points[label]]
            for label in sorted(points)
        }),
        "exact_centroid": [qs(value) for value in centroid],
        "f_vector": support["f_vector"],
        "class": mechanics["class"],
        "active_rows": len(support["active_labels"]),
        "strict_support_count": support["strict_support_count"],
        "minimum_support_log10_abs": support["min_support_log10_abs"],
        "base_present": True,
        "forced_rail_count": len(rail_set()),
        "missing_forced_rails": [],
        "H910_one_minus_t": qs(h910),
    }


def parent_readback():
    certificate = json.loads(PARENT_CERTIFICATE.read_text())
    manifest = json.loads(PARENT_MANIFEST.read_text())
    if certificate["verdict"] != "EXACT_FULL_CONTROL_THREE_TRANSFER_SAFE_FLIP_CHAIN_PASS":
        raise AssertionError(certificate["verdict"])
    if manifest["chain_verdict"] != certificate["verdict"]:
        raise AssertionError("manifest/certificate verdict mismatch")
    for path in (
        PARENT_BUILDER,
        PARENT_VERIFIER,
        PARENT_CERTIFICATE,
        SOURCE,
        FACES_PATH,
    ):
        key = str(path.relative_to(ROOT))
        if manifest["sha256"][key] != sha256(path):
            raise AssertionError(("parent manifest hash mismatch", key))
    return {
        "builder_sha256": sha256(PARENT_BUILDER),
        "verifier_sha256": sha256(PARENT_VERIFIER),
        "certificate_sha256": sha256(PARENT_CERTIFICATE),
        "manifest_sha256": sha256(PARENT_MANIFEST),
        "certificate_verdict": certificate["verdict"],
        "manifest_verdict": manifest["verdict"],
        "manifest_winner": manifest["winner"],
        "parent_declared_next_forbidden": certificate["path"]["next_forbidden_event"]["name"],
        "parent_independent_verifier_expected_terminal": (
            "INDEPENDENT_EXACT_FULL_CONTROL_THREE_TRANSFER_SAFE_FLIP_CHAIN_PASS"
        ),
    }


def build_audit():
    points = ex.read_rows(SOURCE)
    faces = json.loads(FACES_PATH.read_text())
    if sorted(points) != EXPECTED_ACTIVE:
        raise AssertionError(sorted(points))
    mode_names, mode_vectors, base_u, base_v, base_normal = chart_modes(points)
    selectors, selector_values = source_selectors(points, faces)
    tangent, tangent_aux = rational_tangent_audit(
        points, faces, mode_names, mode_vectors, selectors
    )
    wall, wall_aux = parent_wall_audit(points, faces, mode_names, mode_vectors)
    actual_cone = actual_wall_cone_audit(
        wall_aux["path"],
        wall_aux["root"],
        faces,
        mode_names,
        mode_vectors,
        selectors,
        tangent_aux["inward_velocity"],
        tangent_aux["tangent_velocity"],
        wall_aux["wall_gradient"],
    )
    local = local_interval_audit(
        points, faces, selectors, tangent_aux["inward_velocity"]
    )
    source_gap_records = {}
    for name, rows in selector_values.items():
        if name == "H910":
            source_gap_records[name] = {
                "selected": selectors[name],
                "components": {
                    key: exact_scalar_record(value) for key, value in rows.items()
                    if key in ("t", "one_minus_t", "beta1", "beta2")
                },
            }
            continue
        selected_key = selectors[name]
        selected_value = rows[selected_key]
        gaps = [value - selected_value for key, value in rows.items() if key != selected_key]
        source_gap_records[name] = {
            "selected": list(selected_key) if isinstance(selected_key, tuple) else selected_key,
            "selected_squared_value": exact_scalar_record(selected_value),
            "strict_competitor_count": len(gaps),
            "strict_competitor_minimum_decimal": min(float(value) for value in gaps),
            "strict_competitor_digest": canonical_hash([qs(value) for value in gaps]),
        }
    input_paths = (
        SOURCE,
        FACES_PATH,
        PARENT_BUILDER,
        PARENT_VERIFIER,
        PARENT_CERTIFICATE,
        PARENT_MANIFEST,
        PARENT_RAY_SOURCE,
        PARENT_RAY_ENDPOINT,
    )
    result = {
        "version": 1,
        "type": "exact rational chart plus algebraic-root interval audit of row-230 loss",
        "scope": (
            "Independent audit from exact_full_control_chain_far/post_faces. "
            "It reconstructs the complete four-point support family, incident "
            "own-centroid mechanics, exact chart ranks and first-order cones. "
            "It does not integrate a continuation or write candidate coordinates."
        ),
        "source_hashes": {
            str(path.relative_to(ROOT)): sha256(path) for path in input_paths
        },
        "parent_readback": parent_readback(),
        "source_checkpoint": source_checkpoint(points, faces),
        "chart_basis": {
            "dimension": len(mode_names),
            "base_labels": sorted(BASE),
            "base_u": [qs(value) for value in base_u],
            "base_v": [qs(value) for value in base_v],
            "base_normal": [qs(value) for value in base_normal],
            "base_plane_identity": "normal dot every base row displacement is exactly zero",
            "mode_names": [list(row) for row in mode_names],
            "mode_names_digest": canonical_hash([list(row) for row in mode_names]),
        },
        "source_selected_components": source_gap_records,
        "rational_far_chart": tangent,
        "exact_parent_ray_wall": wall,
        "actual_algebraic_wall_cone": actual_cone,
        "local_exact_interval_witness": local,
        "reconciliation": {
            "parent_material_scripts_recorded_danger_rows": 2,
            "complete_current_support_family_rows": 3,
            "missing_from_parent_material_DANGER_set": "support:f102:w198",
            "impact": (
                "the omitted row is not independent: it is exactly the same signed "
                "Delta polynomial and first jet as f83:w229 and f97:w231"
            ),
        },
        "conclusion": {
            "first_order_joint_descent_exists": True,
            "safe_inward_direction_exists": True,
            "wall_tangent_direction_exists": True,
            "all_61_rows_locally_preserved": True,
            "base_and_U8_not_worsened": True,
            "all_37_rails_locally_preserved": True,
            "H910_remains_strictly_negative": True,
            "declared_rational_cone_infeasible": False,
            "farkas_or_gordan_certificate_needed": False,
            "winner": False,
            "final_integration_attempted": False,
        },
        "verdict": "EXACT_ROW230_WALL_CHART_AUDIT_FEASIBLE_NONINTEGRATED",
    }
    return result


def report_text(audit):
    wall = audit["exact_parent_ray_wall"]
    bary = wall["barycentric_interior"]["projections"][0]["decimal_at_bracket_midpoint"]
    local = audit["local_exact_interval_witness"]
    chart = audit["rational_far_chart"]
    return f"""# Exact row-230-loss wall chart audit

Verdict: **FEASIBLE, non-integrated** (`{audit['verdict']}`).

The exact wall is

`Delta = det(p230-p198, p231-p198, p229-p198) = 0`,

with current-cell signed slack `sigma=-Delta>0`.  The complete current support
family has three identical rows, not two:

- `support:f83:w229` for `[198,230,231]`;
- `support:f97:w231` for `[198,229,230]`;
- `support:f102:w198` for `[229,231,230]`.

The fourth orientation is replacement face `[198,229,231]` with witness 230
and the opposite inequality `Delta>=0`.  On the isolated parent-ray wall,
row 230 is strictly inside that triangle with barycentric weights approximately
`(198,229,231)=({bary['gamma_for_198']:.12g}, {bary['alpha_for_229']:.12g}, {bary['beta_for_231']:.12g})`.

The exact physical chart has dimension {chart['dimension']}.  The wall row has
rank {chart['wall_family_row_rank']} and tangent nullity {chart['wall_tangent_nullity']}.
The four target rows have rank {chart['target_row_rank']}; wall plus targets have
rank {chart['wall_plus_target_row_rank']}; all eight audited target/guard rows
have rank {chart['eight_guard_row_rank']}.

Each of the three collapsing spokes `(198,230)`, `(229,230)`, `(230,231)` has
`gram = Delta^2 * positive_cofactor` and `beta1,beta2 = Delta * nonzero_cofactor`.
All other incident face, directed-vertex, `t`, `one_minus_t`, and edge-length
primitives stay nonzero on the root interval.  Crossing removes row 230 and
the two forced rails `(229,230)` and `(230,231)`.

Both required first-order witnesses exist:

- an exact rational direction strictly decreases `S,U54,H56,H1011`, increases
  `sigma`, does not worsen base/U8, and pushes `H910` farther negative;
- an exact algebraic wall-tangent direction annihilates `dDelta` and has the
  same strict target/guard signs on the entire isolated root interval.

Therefore no Gordan/Farkas infeasibility certificate is applicable: exact
primal witnesses certify feasibility.  A separate local interval of
`epsilon={local['epsilon']}` checks all
{local['exhaustive_support_and_mechanics']['primitive_count']} support and
own-uniform-volume-centroid mechanics primitives, all 61 rows, base/U8, all 37
rails, and `H910<0`.  No continuation endpoint file, final integration, winner
claim, OBJ, or STL is produced.
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--verify", action="store_true",
        help="recompute and compare with the frozen audit instead of writing",
    )
    args = parser.parse_args()
    audit = build_audit()
    if args.verify:
        frozen = json.loads(OUTPUT.read_text())
        if audit != frozen:
            raise AssertionError("recomputed audit differs from frozen JSON")
        if REPORT.read_text() != report_text(audit):
            raise AssertionError("AUDIT.md differs from recomputed report")
        print("INDEPENDENT_RECOMPUTE_EXACT_ROW230_WALL_CHART_AUDIT_PASS")
        return
    OUTPUT.write_text(json.dumps(audit, indent=2) + "\n")
    REPORT.write_text(report_text(audit))
    print(json.dumps({
        "verdict": audit["verdict"],
        "complete_support_family": audit["exact_parent_ray_wall"]["current_support_family_size"],
        "chart_dimension": audit["rational_far_chart"]["dimension"],
        "wall_rank": audit["rational_far_chart"]["wall_family_row_rank"],
        "wall_nullity": audit["rational_far_chart"]["wall_tangent_nullity"],
        "local_primitive_count": audit["local_exact_interval_witness"]["exhaustive_support_and_mechanics"]["primitive_count"],
        "output": str(OUTPUT),
    }, indent=2))


if __name__ == "__main__":
    main()
