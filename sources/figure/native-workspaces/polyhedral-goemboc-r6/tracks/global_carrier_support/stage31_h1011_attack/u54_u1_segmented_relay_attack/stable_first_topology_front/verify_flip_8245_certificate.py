#!/usr/bin/env python3
"""Clean-room verifier for the exact stable-carrier circuit certificate.

This file imports neither ``front_common``, the locator, nor the builder.  It
implements its own rational polynomial,
centroid, support, incidence, mechanics, and Bernstein routines.  SciPy/Qhull
is used only to propose maximal-face sets independently; every proposed plane,
cycle, edge incidence, centroid, and mechanics predicate is then checked with
exact :class:`fractions.Fraction` arithmetic.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
from scipy.spatial import ConvexHull


sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
BRANCH = HERE.parent

SOURCE = BRANCH / "far_u1.csv"
DEATH_CERTIFICATE = BRANCH / "death_certificate.json"
DEATH_VERIFICATION = BRANCH / "death_verification.json"
DIAGNOSIS = HERE / "stable_pair_diagnosis.json"
LOCATOR = HERE / "flip_8245_locator.json"
CERTIFICATE = HERE / "flip_8245_certificate.json"
PRE = HERE / "flip_8245_pre.csv"
POST = HERE / "flip_8245_post.csv"
FAR = HERE / "flip_8245_far.csv"
OUTPUT = HERE / "flip_8245_verification.json"

BASE = frozenset(range(17)) | {54}
EVENT_CIRCUIT = (7, 8, 245, 246)
PRE_DIAGONAL = (8, 245)
POST_DIAGONAL = (7, 246)
PRE_T = Q(1, 400)
POST_T = Q(51, 20_000)
FAR_T = Q(13, 5_000)
EXPECTED_F_VECTOR = [61, 162, 103]
SOURCE_FEATURES = {
    "class": [2, 2, 2],
    "stable_faces": [sorted(BASE), [7, 8, 245]],
    "unstable_vertices": [1, 8],
    "saddle_edges": [[5, 6], [10, 11]],
}
POST_FEATURES = {
    "class": [2, 2, 2],
    "stable_faces": [sorted(BASE), [7, 8, 246]],
    "unstable_vertices": [1, 8],
    "saddle_edges": [[5, 6], [10, 11]],
}
EXPECTED_ZERO_FAMILY = {
    "support:f15:w246",
    "support:f17:w7",
    "edge:(8, 245):gram",
    "edge:(8, 245):beta1",
    "edge:(8, 245):beta2",
}
DANGER = {
    (frozenset((198, 230, 231)), 229),
    (frozenset((198, 229, 230)), 231),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def qs(value: Q) -> str:
    return (
        str(value.numerator)
        if value.denominator == 1
        else f"{value.numerator}/{value.denominator}"
    )


def qlog10(value: Q) -> float:
    if not value:
        return -math.inf
    return math.log10(abs(value.numerator)) - math.log10(value.denominator)


@dataclass(frozen=True)
class Poly:
    """Independent univariate polynomial over the rationals, low first."""

    c: tuple[Q, ...]

    def __post_init__(self):
        values = tuple(Q(value) for value in self.c)
        while len(values) > 1 and not values[-1]:
            values = values[:-1]
        object.__setattr__(self, "c", values or (Q(0),))

    @staticmethod
    def zero():
        return Poly((Q(0),))

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Poly) else Poly((Q(value),))

    @property
    def degree(self):
        return len(self.c) - 1

    def __add__(self, other):
        other = Poly.coerce(other)
        size = max(len(self.c), len(other.c))
        return Poly(
            tuple(
                (self.c[k] if k < len(self.c) else Q(0))
                + (other.c[k] if k < len(other.c) else Q(0))
                for k in range(size)
            )
        )

    __radd__ = __add__

    def __neg__(self):
        return Poly(tuple(-value for value in self.c))

    def __sub__(self, other):
        return self + (-Poly.coerce(other))

    def __rsub__(self, other):
        return Poly.coerce(other) - self

    def __mul__(self, other):
        other = Poly.coerce(other)
        out = [Q(0)] * (len(self.c) + len(other.c) - 1)
        for i, left in enumerate(self.c):
            for j, right in enumerate(other.c):
                out[i + j] += left * right
        return Poly(tuple(out))

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        scalar = Q(scalar)
        if not scalar:
            raise ZeroDivisionError
        return Poly(tuple(value / scalar for value in self.c))

    def derivative(self):
        if self.degree == 0:
            return Poly.zero()
        return Poly(tuple(Q(k) * self.c[k] for k in range(1, len(self.c))))

    def eval(self, parameter: Q):
        out = Q(0)
        for coefficient in reversed(self.c):
            out = out * parameter + coefficient
        return out

    def affine(self, lo: Q, hi: Q):
        variable = Poly((lo, hi - lo))
        out = Poly.zero()
        for coefficient in reversed(self.c):
            out = out * variable + coefficient
        return out

    def exact(self):
        return [qs(value) for value in self.c]


def add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def sub(left, right):
    return tuple(a - b for a, b in zip(left, right))


def mul(vector, scalar):
    return tuple(value * scalar for value in vector)


def dot(left, right):
    zero = Poly.zero() if isinstance(left[0], Poly) or isinstance(right[0], Poly) else Q(0)
    return sum((a * b for a, b in zip(left, right)), zero)


def cross(left, right):
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def det3(a, b, c):
    return dot(a, cross(b, c))


def norm2(vector):
    return dot(vector, vector)


def bernstein_coefficients(poly: Poly):
    degree = poly.degree
    return tuple(
        sum(
            (
                poly.c[k] * Q(math.comb(index, k), math.comb(degree, k))
                for k in range(index + 1)
            ),
            Q(0),
        )
        for index in range(degree + 1)
    )


def bernstein_sign(poly: Poly, lo: Q, hi: Q, max_depth: int = 60):
    stack = [(Q(lo), Q(hi), 0)]
    expected = None
    leaves = 0
    worst = None
    while stack:
        left, right, depth = stack.pop()
        coefficients = bernstein_coefficients(poly.affine(left, right))
        if all(value > 0 for value in coefficients):
            sign = 1
        elif all(value < 0 for value in coefficients):
            sign = -1
        else:
            if depth >= max_depth:
                raise AssertionError(
                    ("Bernstein sign not isolated", poly.degree, qs(left), qs(right))
                )
            middle = (left + right) / 2
            stack.append((middle, right, depth + 1))
            stack.append((left, middle, depth + 1))
            continue
        if expected is None:
            expected = sign
        elif sign != expected:
            raise AssertionError("polynomial changes sign")
        leaves += 1
        magnitude = min(abs(value) for value in coefficients)
        local = qlog10(magnitude)
        worst = local if worst is None else min(worst, local)
    if expected is None:
        raise AssertionError("empty Bernstein proof")
    return expected, leaves, worst


def polynomial_hash(poly: Poly) -> str:
    return canonical_hash(poly.exact())


def read_exact_csv(path: Path):
    rows = {}
    with path.open(newline="") as stream:
        for row in csv.DictReader(stream):
            rows[int(row["source_id"])] = tuple(Q(row[key]) for key in ("x", "y", "z"))
    return rows


def point_hash(points) -> str:
    return canonical_hash(
        {str(label): [qs(value) for value in points[label]] for label in sorted(points)}
    )


def face_hash(faces) -> str:
    return canonical_hash(sorted(sorted(int(label) for label in face) for face in faces))


def evaluate_path(path, parameter: Q):
    return {
        label: tuple(coordinate.eval(parameter) for coordinate in xyz)
        for label, xyz in path.items()
    }


def cycle_normal(cycle, points):
    anchor = points[cycle[0]]
    for j in range(1, len(cycle) - 1):
        normal = cross(sub(points[cycle[j]], anchor), sub(points[cycle[j + 1]], anchor))
        if any(value != 0 for value in normal):
            return normal
    raise AssertionError(("degenerate face", cycle))


def edge_data(faces):
    incidence = {}
    neighbors = {}
    for face_index, cycle in enumerate(faces):
        for a, b in zip(cycle, cycle[1:] + cycle[:1]):
            edge = tuple(sorted((a, b)))
            incidence.setdefault(edge, []).append(face_index)
            neighbors.setdefault(a, set()).add(b)
            neighbors.setdefault(b, set()).add(a)
    if not all(len(face_indices) == 2 for face_indices in incidence.values()):
        raise AssertionError("nonmanifold face ledger")
    return incidence, {label: sorted(values) for label, values in neighbors.items()}


def fresh_maximal_faces(points):
    """Independent Qhull proposal, exact plane grouping, and exact closure."""
    labels = sorted(points)
    array = np.asarray([[float(value) for value in points[label]] for label in labels])
    hull = ConvexHull(array)
    groups = defaultdict(list)
    for simplex_indices in hull.simplices:
        simplex = tuple(labels[int(index)] for index in simplex_indices)
        a, b, c = (points[label] for label in simplex)
        normal = cross(sub(b, a), sub(c, a))
        if not any(normal):
            raise AssertionError(("Qhull proposed a flat triangle", simplex))
        values = {label: dot(normal, sub(points[label], a)) for label in labels}
        signs = {1 if value > 0 else -1 for value in values.values() if value}
        if len(signs) != 1:
            raise AssertionError(("Qhull triangle is not exactly supporting", simplex))
        coplanar = frozenset(label for label, value in values.items() if not value)
        if len(coplanar) < 3:
            raise AssertionError(("bad coplanar hull set", simplex, coplanar))
        groups[coplanar].append(simplex)

    faces = []
    for coplanar, triangles in groups.items():
        counts = Counter()
        for triangle in triangles:
            for k in range(3):
                counts[tuple(sorted((triangle[k], triangle[(k + 1) % 3])))] += 1
        boundary = [edge for edge, count in counts.items() if count == 1]
        adjacency = defaultdict(list)
        for a, b in boundary:
            adjacency[a].append(b)
            adjacency[b].append(a)
        if set(adjacency) != set(coplanar) or any(
            len(values) != 2 for values in adjacency.values()
        ):
            raise AssertionError(("maximal-face boundary is not one cycle", sorted(coplanar)))
        start = min(coplanar)
        cycle = [start]
        previous = None
        current = start
        while True:
            following = adjacency[current][0]
            if following == previous:
                following = adjacency[current][1]
            if following == start:
                break
            cycle.append(following)
            previous, current = current, following
            if len(cycle) > len(coplanar):
                raise AssertionError("boundary walk did not close")
        if set(cycle) != set(coplanar):
            raise AssertionError(("boundary cycle misses coplanar rows", cycle, coplanar))

        normal = cycle_normal(cycle, points)
        anchor = points[cycle[0]]
        nonface = [
            dot(normal, sub(points[label], anchor))
            for label in labels
            if label not in coplanar
        ]
        signs = {1 if value > 0 else -1 for value in nonface if value}
        if len(signs) != 1:
            raise AssertionError(("reconstructed face has mixed support", cycle))
        # Outward orientation puts every nonface point on the negative side.
        if signs == {1}:
            normal = tuple(-value for value in normal)
        area = (Q(0), Q(0), Q(0))
        for left, right in zip(cycle, cycle[1:] + cycle[:1]):
            area = add(area, cross(points[left], points[right]))
        if dot(area, normal) < 0:
            cycle = [cycle[0], *reversed(cycle[1:])]
        faces.append(cycle)

    faces.sort(key=lambda face: tuple(sorted(face)))
    incidence, _neighbors = edge_data(faces)
    active = set().union(*(set(face) for face in faces))
    if active != set(points):
        raise AssertionError(("independent hull has inactive rows", set(points) - active))
    if len(active) - len(incidence) + len(faces) != 2:
        raise AssertionError("independent hull fails Euler closure")
    return faces, {
        "qhull_triangle_count": len(hull.simplices),
        "exact_maximal_face_count": len(faces),
        "exact_true_edge_count": len(incidence),
        "active_row_count": len(active),
        "euler": 2,
        "all_qhull_planes_exactly_supporting": True,
        "all_coplanar_sets_merged": True,
    }


def supporting_cell(points, faces):
    all_labels = set(points)
    strict = []
    coplanar_equalities = 0
    for cycle in faces:
        normal = cycle_normal(cycle, points)
        anchor = points[cycle[0]]
        for label in cycle[1:]:
            value = dot(normal, sub(points[label], anchor))
            if value:
                raise AssertionError(("noncoplanar face member", cycle, label, qs(value)))
            coplanar_equalities += 1
        values = [
            dot(normal, sub(points[label], anchor))
            for label in sorted(all_labels - set(cycle))
        ]
        if any(not value for value in values):
            raise AssertionError(("maximal face omitted a coplanar row", cycle))
        signs = {1 if value > 0 else -1 for value in values}
        if len(signs) != 1:
            raise AssertionError(("mixed exact support", cycle))
        orientation = signs.pop()
        strict.extend(orientation * value for value in values)
    incidence, _neighbors = edge_data(faces)
    active = set().union(*(set(face) for face in faces))
    return {
        "f_vector": [len(active), len(incidence), len(faces)],
        "euler": len(active) - len(incidence) + len(faces),
        "active_labels": sorted(active),
        "strict_support_count": len(strict),
        "min_support_log10_abs": min(qlog10(value) for value in strict),
        "coplanarity_equalities": coplanar_equalities,
        "coplanar_interior_rows": [],
        "edges": sorted(incidence),
    }


def exact_centroid_numerators(points, faces):
    polynomial = isinstance(next(iter(points.values()))[0], Poly)
    zero = Poly.zero() if polynomial else Q(0)
    d6 = zero
    m24 = [zero, zero, zero]
    for cycle in faces:
        for j in range(1, len(cycle) - 1):
            a, b, c = points[cycle[0]], points[cycle[j]], points[cycle[j + 1]]
            volume6 = det3(a, b, c)
            d6 += volume6
            for axis in range(3):
                m24[axis] += volume6 * (a[axis] + b[axis] + c[axis])
    return d6, tuple(m24)


def mechanics_primitives(points, faces):
    d6, m24 = exact_centroid_numerators(points, faces)
    scale = 4 * d6
    centered = {
        label: tuple(scale * points[label][axis] - m24[axis] for axis in range(3))
        for label in points
    }
    incidence, neighbors = edge_data(faces)
    face = {}
    reference = {}
    for face_index, cycle in enumerate(faces):
        normal = cycle_normal(cycle, points)
        nn = norm2(normal)
        zero = Poly.zero() if isinstance(points[cycle[0]][0], Poly) else Q(0)
        refpoint = tuple(
            sum((points[label][axis] for label in cycle), zero) / len(cycle)
            for axis in range(3)
        )
        face_key = tuple(sorted(cycle))
        face[face_key] = {}
        reference[face_key] = {}
        for a, b in zip(cycle, cycle[1:] + cycle[:1]):
            edge = tuple(sorted((a, b)))
            direction = sub(points[b], points[a])
            height = dot(normal, centered[a])
            raw = dot(
                cross(direction, sub(mul(normal, height), mul(centered[a], nn))),
                normal,
            )
            ref = dot(cross(direction, sub(refpoint, points[a])), normal)
            face[face_key][edge] = raw
            reference[face_key][edge] = ref
    vertex = {
        label: {
            neighbor: -dot(centered[label], sub(points[neighbor], points[label]))
            for neighbor in neighbors[label]
        }
        for label in neighbors
    }
    edge = {}
    for pair, face_indices in incidence.items():
        i, j = pair
        direction = sub(points[j], points[i])
        direction_norm2 = norm2(direction)
        t = -dot(centered[i], direction)
        n1 = cycle_normal(faces[face_indices[0]], points)
        n2 = cycle_normal(faces[face_indices[1]], points)
        aa, ab, cc = norm2(n1), dot(n1, n2), norm2(n2)
        r1, r2 = dot(centered[i], n1), dot(centered[i], n2)
        beta1 = r1 * cc - r2 * ab
        beta2 = r2 * aa - r1 * ab
        edge[pair] = {
            "direction_norm2": direction_norm2,
            "gram": aa * cc - ab * ab,
            "t": t,
            "one_minus_t": scale * direction_norm2 - t,
            "beta1": beta1,
            "beta2": beta2,
        }
    return {
        "d6": d6,
        "face": face,
        "reference": reference,
        "vertex": vertex,
        "edge": edge,
    }


def signed_face_components(ledger, face_key):
    out = {}
    for edge, raw in ledger["face"][face_key].items():
        reference = ledger["reference"][face_key][edge]
        if isinstance(reference, Poly):
            value = reference.eval(Q(0))
        else:
            value = reference
        if not value:
            raise AssertionError(("zero face reference", face_key, edge))
        out[edge] = (1 if value > 0 else -1) * raw
    return out


def classify_point(points, faces):
    ledger = mechanics_primitives(points, faces)
    if ledger["d6"] <= 0:
        raise AssertionError("nonpositive exact volume")
    stable = [
        face_key
        for face_key in ledger["face"]
        if all(value > 0 for value in signed_face_components(ledger, face_key).values())
    ]
    unstable = [
        vertex
        for vertex, values in ledger["vertex"].items()
        if all(value > 0 for value in values.values())
    ]
    saddles = []
    for edge, values in ledger["edge"].items():
        if values["direction_norm2"] <= 0 or values["gram"] <= 0:
            raise AssertionError(("degenerate true edge", edge))
        if all(values[name] > 0 for name in ("t", "one_minus_t", "beta1", "beta2")):
            saddles.append(edge)
    return ledger, {
        "class": [len(stable), len(unstable), len(saddles)],
        "stable_faces": [list(face) for face in sorted(stable)],
        "unstable_vertices": sorted(unstable),
        "saddle_edges": [list(edge) for edge in sorted(saddles)],
    }


def support_polynomials(points, faces):
    out = []
    all_labels = set(points)
    for face_index, cycle in enumerate(faces):
        normal = cycle_normal(cycle, points)
        anchor = points[cycle[0]]
        for label in cycle[1:]:
            if dot(normal, sub(points[label], anchor)) != Poly.zero():
                raise AssertionError(("moving face loses coplanarity", face_index, label))
        for witness in sorted(all_labels - set(cycle)):
            out.append(
                (face_index, witness, dot(normal, sub(points[witness], anchor)))
            )
    return out

import os
import tempfile


def all_primitive_records(path, faces):
    ledger = mechanics_primitives(path, faces)
    records = [("volume_d6", ledger["d6"], "mechanics_denominator")]
    for face_index, witness, poly in support_polynomials(path, faces):
        records.append((f"support:f{face_index}:w{witness}", poly, "support"))
    for face_index, cycle in enumerate(faces):
        if len(cycle) <= 3:
            continue
        normal = cycle_normal(cycle, path)
        for offset, current in enumerate(cycle):
            previous = cycle[offset - 1]
            following = cycle[(offset + 1) % len(cycle)]
            turn = dot(
                cross(
                    sub(path[current], path[previous]),
                    sub(path[following], path[current]),
                ),
                normal,
            )
            records.append(
                (f"in_face_turn:f{face_index}:v{current}", turn, "in_face_turn")
            )
    for face_key, values in sorted(ledger["reference"].items()):
        for edge, poly in sorted(values.items()):
            records.append(
                (f"face_reference:{face_key}:{edge}", poly, "mechanics_denominator")
            )
    for face_key, values in sorted(ledger["face"].items()):
        for edge, poly in sorted(values.items()):
            records.append((f"face_raw:{face_key}:{edge}", poly, "face_component"))
    for vertex, values in sorted(ledger["vertex"].items()):
        for neighbor, poly in sorted(values.items()):
            records.append(
                (f"vertex:{vertex}:{neighbor}", poly, "vertex_component")
            )
    for edge, values in sorted(ledger["edge"].items()):
        for name in (
            "direction_norm2",
            "gram",
            "t",
            "one_minus_t",
            "beta1",
            "beta2",
        ):
            records.append((f"edge:{edge}:{name}", values[name], "edge_component"))
    if len(records) != 7_922:
        raise AssertionError(("primitive count", len(records)))
    return records


def affine_path(source, velocity):
    return {
        label: tuple(
            Poly((source[label][axis], velocity[label][axis]))
            for axis in range(3)
        )
        for label in source
    }


def evaluate_affine_path(path, parameter):
    return {
        label: tuple(poly.eval(parameter) for poly in xyz)
        for label, xyz in path.items()
    }


def circuit_polynomial(path):
    a, b, c, d = (path[label] for label in EVENT_CIRCUIT)
    return det3(sub(b, a), sub(c, a), sub(d, a))


def poly_divmod(numerator, denominator):
    numerator = Poly.coerce(numerator)
    denominator = Poly.coerce(denominator)
    if denominator == Poly.zero():
        raise ZeroDivisionError
    remainder = list(numerator.c)
    quotient = [Q(0)] * max(1, numerator.degree - denominator.degree + 1)
    while len(remainder) - 1 >= denominator.degree and any(remainder):
        degree = len(remainder) - 1 - denominator.degree
        factor = remainder[-1] / denominator.c[-1]
        quotient[degree] += factor
        for offset, value in enumerate(denominator.c):
            remainder[degree + offset] -= factor * value
        while len(remainder) > 1 and remainder[-1] == 0:
            remainder.pop()
    return Poly(tuple(quotient)), Poly(tuple(remainder))


def circuit_multiplicity(polynomial, circuit):
    multiplicity = 0
    cofactor = Poly.coerce(polynomial)
    while cofactor.degree >= circuit.degree:
        quotient, remainder = poly_divmod(cofactor, circuit)
        if remainder != Poly.zero():
            break
        multiplicity += 1
        cofactor = quotient
    return multiplicity, cofactor


def complete_polynomial_digest(records):
    digest = hashlib.sha256()
    for name, polynomial, family in records:
        digest.update(name.encode())
        digest.update(b"|")
        digest.update(family.encode())
        digest.update(b"|")
        digest.update("|".join(polynomial.exact()).encode())
        digest.update(b"\n")
    return digest.hexdigest()


def strict_interval(records, lo, hi):
    digest = hashlib.sha256()
    leaves = 0
    worst = None
    family_counts = {}
    for name, polynomial, family in records:
        sign, count, margin = bernstein_sign(polynomial, lo, hi, max_depth=40)
        leaves += count
        worst = margin if worst is None else min(worst, margin)
        family_counts[family] = family_counts.get(family, 0) + 1
        digest.update(name.encode())
        digest.update(b"|")
        digest.update(str(sign).encode())
        digest.update(b"|")
        digest.update("|".join(polynomial.exact()).encode())
        digest.update(b"\n")
    return {
        "strict_polynomial_count": len(records),
        "family_counts": family_counts,
        "bernstein_leaf_count": leaves,
        "min_bernstein_coefficient_log10_abs": worst,
        "signed_primitive_digest": digest.hexdigest(),
    }


def forced_rails():
    rails = set()
    for route in (
        [228, *range(229, 247), 8],
        [228, *range(247, 265), 8],
    ):
        rails.update(tuple(sorted(edge)) for edge in zip(route, route[1:]))
    rails.remove((228, 229))
    if len(rails) != 37:
        raise AssertionError(len(rails))
    return rails


def edge_set(faces):
    return {
        tuple(sorted((first, second)))
        for cycle in faces
        for first, second in zip(cycle, cycle[1:] + cycle[:1])
    }


def row230_values(points, faces):
    constant_path = {
        label: tuple(Poly((value,)) for value in xyz)
        for label, xyz in points.items()
    }
    found = {}
    for face_index, witness, support in support_polynomials(constant_path, faces):
        family = (frozenset(faces[face_index]), witness)
        if family not in DANGER:
            continue
        normal = cycle_normal(faces[face_index], constant_path)
        value = support.eval(Q(0))
        normalized_square = value * value / norm2(normal).eval(Q(0))
        found[f"{sorted(family[0])}|{witness}"] = qs(normalized_square)
    expected = {"[198, 230, 231]|229", "[198, 229, 230]|231"}
    if set(found) != expected or any(Q(value) <= 0 for value in found.values()):
        raise AssertionError(("row230", found))
    return found


def checkpoint(points, faces, expected_features):
    support = supporting_cell(points, faces)
    ledger, mechanics = classify_point(points, faces)
    if support["f_vector"] != EXPECTED_F_VECTOR or support["euler"] != 2:
        raise AssertionError(("f-vector", support["f_vector"]))
    if support["active_labels"] != sorted(points):
        raise AssertionError("inactive input row")
    if mechanics != expected_features:
        raise AssertionError(("mechanics", mechanics, expected_features))
    if BASE not in {frozenset(face) for face in faces}:
        raise AssertionError("missing enlarged base")
    missing = sorted(forced_rails() - edge_set(faces))
    if missing:
        raise AssertionError(("missing rails", missing))
    constant_path = {
        label: tuple(Poly((value,)) for value in xyz)
        for label, xyz in points.items()
    }
    turns = [
        row
        for row in all_primitive_records(constant_path, faces)
        if row[2] == "in_face_turn"
    ]
    if len(turns) != 18 or any(not poly.eval(Q(0)) for _name, poly, _family in turns):
        raise AssertionError("base turn contract")
    h910 = ledger["edge"][(9, 10)]
    witness = min(
        ("t", "one_minus_t", "beta1", "beta2"),
        key=lambda name: h910[name],
    )
    if h910[witness] >= 0:
        raise AssertionError("H(9,10) is not dead")
    return {
        "support": {key: value for key, value in support.items() if key != "edges"},
        "mechanics": mechanics,
        "forced_rail_count": 37,
        "missing_forced_rails": [],
        "row230_squared_margins": row230_values(points, faces),
        "h910_negative_component": witness,
        "h910_negative_value": qs(h910[witness]),
    }


def topology_difference(before, after):
    before_faces = {tuple(sorted(face)) for face in before}
    after_faces = {tuple(sorted(face)) for face in after}
    before_edges = edge_set(before)
    after_edges = edge_set(after)
    return {
        "faces_removed": [list(row) for row in sorted(before_faces - after_faces)],
        "faces_added": [list(row) for row in sorted(after_faces - before_faces)],
        "edges_removed": [list(row) for row in sorted(before_edges - after_edges)],
        "edges_added": [list(row) for row in sorted(after_edges - before_edges)],
    }


def verify_hash_packet(packet):
    checked = {}
    for relative, expected in packet.items():
        path = ROOT / relative
        if not path.is_file():
            raise AssertionError(("missing bound file", relative))
        actual = sha256(path)
        if actual != expected:
            raise AssertionError(("hash mismatch", relative, actual, expected))
        checked[relative] = actual
    return checked


def compare_float(actual, expected, name):
    if not math.isclose(float(actual), float(expected), rel_tol=0.0, abs_tol=5e-13):
        raise AssertionError((name, actual, expected))


def atomic_write(path, data):
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary_path = Path(temporary)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_path, path)
        directory = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
        if path.read_bytes() != data:
            raise AssertionError("verification readback")
    finally:
        if temporary_path.exists():
            temporary_path.unlink()


def main():
    expected_static_hashes = {
        SOURCE: "9f6c84382c05502766a17feb0cb9346bd44ec9f889e566e3e102d3d63a29ed77",
        DEATH_CERTIFICATE: "f799513eefcd1893b720111a8876f9027bc2b53ff598fbc68d6ff0fe37470996",
        DEATH_VERIFICATION: "86b1fb7f4e352ec162979620be43d6b02b5d5117d9e3fd305e04d84912a0ed03",
        DIAGNOSIS: "891374ef74011e364bcb2cb0b1fe64814904f8517b6d6b7bb932f024f7e53e4f",
    }
    for path, expected in expected_static_hashes.items():
        if sha256(path) != expected:
            raise AssertionError(("static binding", path.name, sha256(path), expected))
    death_certificate = json.loads(DEATH_CERTIFICATE.read_text())
    death_verification = json.loads(DEATH_VERIFICATION.read_text())
    if death_certificate.get("verdict") != "EXACT_U54_DEATH_EPOCH_PASS":
        raise AssertionError("death certificate verdict")
    if death_verification.get("verdict") != "INDEPENDENT_EXACT_U54_DEATH_VERIFICATION_PASS":
        raise AssertionError("death verification verdict")

    locator = json.loads(LOCATOR.read_text())
    certificate = json.loads(CERTIFICATE.read_text())
    if locator.get("verdict") != "EXACT_FIRST_8245_STABLE_CARRIER_FLIP_LOCATOR_PASS":
        raise AssertionError("locator verdict")
    if certificate.get("verdict") != "EXACT_STABLE_CARRIER_8245_TRANSFER_CERTIFICATE_PASS":
        raise AssertionError("certificate verdict")
    locator_bindings = verify_hash_packet(locator["source_hashes"])
    certificate_bindings = verify_hash_packet(certificate["source_hashes"])
    if certificate["exact_locator"]["sha256"] != sha256(LOCATOR):
        raise AssertionError("certificate locator hash")
    for name, path in (("pre", PRE), ("post", POST), ("far", FAR)):
        expected = locator["checkpoints"][name]["sha256"]
        if sha256(path) != expected:
            raise AssertionError((name, "checkpoint hash"))

    source = read_exact_csv(SOURCE)
    pre = read_exact_csv(PRE)
    post = read_exact_csv(POST)
    far = read_exact_csv(FAR)
    if not (set(source) == set(pre) == set(post) == set(far)):
        raise AssertionError("point label drift")
    velocity = {
        label: tuple((far[label][axis] - source[label][axis]) / FAR_T for axis in range(3))
        for label in source
    }
    path = affine_path(source, velocity)
    if evaluate_affine_path(path, PRE_T) != pre:
        raise AssertionError("pre is not on certified ray")
    if evaluate_affine_path(path, POST_T) != post:
        raise AssertionError("post is not on certified ray")
    if evaluate_affine_path(path, FAR_T) != far:
        raise AssertionError("far is not on certified ray")

    source_faces, source_hull = fresh_maximal_faces(source)
    pre_faces, pre_hull = fresh_maximal_faces(pre)
    post_faces, post_hull = fresh_maximal_faces(post)
    far_faces, far_hull = fresh_maximal_faces(far)
    source_keys = {tuple(sorted(face)) for face in source_faces}
    if {tuple(sorted(face)) for face in pre_faces} != source_keys:
        raise AssertionError("pre ledger drift")
    post_keys = {tuple(sorted(face)) for face in post_faces}
    if {tuple(sorted(face)) for face in far_faces} != post_keys:
        raise AssertionError("far ledger drift")
    topology = topology_difference(source_faces, post_faces)
    expected_topology = {
        "faces_removed": [[7, 8, 245], [8, 245, 246]],
        "faces_added": [[7, 8, 246], [7, 245, 246]],
        "edges_removed": [[8, 245]],
        "edges_added": [[7, 246]],
    }
    if topology != expected_topology:
        raise AssertionError(("topology", topology))

    checkpoints = {
        "source": checkpoint(source, source_faces, SOURCE_FEATURES),
        "pre": checkpoint(pre, pre_faces, SOURCE_FEATURES),
        "post": checkpoint(post, post_faces, POST_FEATURES),
        "far": checkpoint(far, far_faces, POST_FEATURES),
    }
    for name in ("pre", "post", "far"):
        if checkpoints[name] != locator["checkpoints"][name]["exact"]:
            raise AssertionError((name, "exact checkpoint differs"))
    hulls = {"pre": pre_hull, "post": post_hull, "far": far_hull}
    for name, hull in hulls.items():
        if hull != locator["checkpoints"][name]["fresh_hull"]:
            raise AssertionError((name, "fresh hull differs"))

    circuit = circuit_polynomial(path)
    event = locator["first_event"]
    if circuit.exact() != event["circuit_polynomial_exact"]:
        raise AssertionError("circuit polynomial differs")
    lo = Q(event["root"]["lo"])
    hi = Q(event["root"]["hi"])
    value_lo, value_hi = circuit.eval(lo), circuit.eval(hi)
    if not value_lo or not value_hi or value_lo * value_hi >= 0:
        raise AssertionError("bad algebraic bracket")
    derivative_sign, derivative_leaves, _ = bernstein_sign(
        circuit.derivative(), lo, hi, max_depth=40
    )
    if derivative_sign != event["root"]["derivative_sign"]:
        raise AssertionError("root derivative sign")
    if hi - lo > Q(1, 10**30):
        raise AssertionError("root bracket too wide")
    before_sign = bernstein_sign(circuit, Q(0), lo, max_depth=40)[0]
    after_sign = bernstein_sign(circuit, hi, FAR_T, max_depth=40)[0]
    if before_sign != event["circuit_sign_before"] or after_sign != event["circuit_sign_after"]:
        raise AssertionError("circuit side signs")

    old_records = all_primitive_records(path, source_faces)
    zero_family = []
    strict_old = []
    for name, polynomial, family in old_records:
        multiplicity, cofactor = circuit_multiplicity(polynomial, circuit)
        if multiplicity:
            sign, leaves, margin = bernstein_sign(cofactor, Q(0), FAR_T, max_depth=40)
            zero_family.append(
                {
                    "name": name,
                    "family": family,
                    "circuit_multiplicity": multiplicity,
                    "cofactor_degree": cofactor.degree,
                    "cofactor_sign": sign,
                    "cofactor_bernstein_leaves": leaves,
                    "cofactor_min_log10_abs": margin,
                    "cofactor_digest": hashlib.sha256(
                        "|".join(cofactor.exact()).encode()
                    ).hexdigest(),
                }
            )
        else:
            strict_old.append((name, polynomial, family))
    if {row["name"] for row in zero_family} != EXPECTED_ZERO_FAMILY:
        raise AssertionError(("zero family", zero_family))
    if zero_family != event["complete_zero_family"]:
        raise AssertionError("zero family details differ")
    old_audit = strict_interval(strict_old, Q(0), hi)
    primary_old = event["old_nonfamily_strict_audit"]
    for key in (
        "strict_polynomial_count",
        "family_counts",
        "bernstein_leaf_count",
        "signed_primitive_digest",
    ):
        if old_audit[key] != primary_old[key]:
            raise AssertionError(("old audit", key))
    compare_float(
        old_audit["min_bernstein_coefficient_log10_abs"],
        primary_old["min_bernstein_coefficient_log10_abs"],
        "old margin",
    )
    if complete_polynomial_digest(old_records) != event["old_complete_primitive_digest"]:
        raise AssertionError("old primitive digest")

    new_records = all_primitive_records(path, post_faces)
    new_audit = strict_interval(new_records, hi, FAR_T)
    primary_new = locator["rechart"]["new_strict_audit"]
    for key in (
        "strict_polynomial_count",
        "family_counts",
        "bernstein_leaf_count",
        "signed_primitive_digest",
    ):
        if new_audit[key] != primary_new[key]:
            raise AssertionError(("new audit", key))
    compare_float(
        new_audit["min_bernstein_coefficient_log10_abs"],
        primary_new["min_bernstein_coefficient_log10_abs"],
        "new margin",
    )
    if complete_polynomial_digest(new_records) != locator["rechart"]["new_complete_primitive_digest"]:
        raise AssertionError("new primitive digest")

    payload = {
        "schema": "stable_first_topology_front.flip_8245_verification",
        "schema_version": 1,
        "report_type": "independent_clean_room_exact_verification",
        "scope": (
            "Independent reconstruction without importing front_common, locator or builder; "
            "all old/new primitive rows, hulls, mechanics, hashes and circuit factors are rebuilt."
        ),
        "source_hashes": {
            str(path.resolve().relative_to(ROOT)): sha256(path)
            for path in (
                SOURCE,
                DEATH_CERTIFICATE,
                DEATH_VERIFICATION,
                DIAGNOSIS,
                LOCATOR,
                CERTIFICATE,
                PRE,
                POST,
                FAR,
                Path(__file__).resolve(),
            )
        },
        "bound_locator_files": locator_bindings,
        "bound_certificate_files": certificate_bindings,
        "fresh_hulls": {
            "source": source_hull,
            "pre": pre_hull,
            "post": post_hull,
            "far": far_hull,
        },
        "face_hashes": {
            "source": face_hash(source_faces),
            "pre": face_hash(pre_faces),
            "post": face_hash(post_faces),
            "far": face_hash(far_faces),
        },
        "topology_transfer": topology,
        "root": {
            "lo": qs(lo),
            "hi": qs(hi),
            "value_lo_sign": 1 if value_lo > 0 else -1,
            "value_hi_sign": 1 if value_hi > 0 else -1,
            "derivative_sign": derivative_sign,
            "derivative_bernstein_leaves": derivative_leaves,
        },
        "complete_zero_family": zero_family,
        "old_nonfamily_strict_audit": old_audit,
        "old_complete_primitive_digest": complete_polynomial_digest(old_records),
        "new_strict_audit": new_audit,
        "new_complete_primitive_digest": complete_polynomial_digest(new_records),
        "checkpoints": checkpoints,
        "invariants": {
            "class_before_after": [[2, 2, 2], [2, 2, 2]],
            "stable_face_transfer": [[7, 8, 245], [7, 8, 246]],
            "active_row_count": 61,
            "forced_rail_count": 37,
            "row230_strict": True,
            "h910_strictly_dead": True,
            "old_complete_primitive_count": 7_922,
            "old_strict_nonfamily_count": 7_917,
            "new_strict_primitive_count": 7_922,
        },
        "verdict": "INDEPENDENT_EXACT_STABLE_CARRIER_8245_TRANSFER_VERIFICATION_PASS",
    }
    atomic_write(OUTPUT, (json.dumps(payload, indent=2) + "\n").encode())
    print(
        json.dumps(
            {
                "verdict": payload["verdict"],
                "verification": OUTPUT.name,
                "sha256": sha256(OUTPUT),
                "zero_family_count": len(zero_family),
                "topology_transfer": topology,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
