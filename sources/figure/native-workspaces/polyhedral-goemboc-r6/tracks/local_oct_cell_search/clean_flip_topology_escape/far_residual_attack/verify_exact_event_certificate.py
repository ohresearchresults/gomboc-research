#!/usr/bin/env python3
"""Clean-room verifier for the exact sparse-ray first-event certificate.

This file imports neither the producer, ``attack_common``, the frozen six-flip
builder, nor the numerical scan.  It implements its own rational polynomial,
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
ROOT = HERE.parents[3]
PARENT = HERE.parent

CERTIFICATE = HERE / "exact_event_certificate.json"
PATH_DEFINITION = HERE / "exact_event_path.json"
MANIFEST = HERE / "exact_event_manifest.sha256"
UPSTREAM_CERTIFICATE = PARENT / "certificate.json"
UPSTREAM_FACES = PARENT / "far_faces.json"
RAY = HERE / "active_sparse_ray.json"
NUMERIC_SCAN = HERE / "active_sparse_scan.json"

POINT_FILES = {
    "source": HERE / "exact_event_source.csv",
    "pre": HERE / "exact_event_pre.csv",
    "wall": HERE / "exact_event_wall.csv",
    "post": HERE / "exact_event_post.csv",
}
FACE_FILES = {
    "source": HERE / "exact_event_source_faces.json",
    "pre": HERE / "exact_event_pre_faces.json",
    "wall": HERE / "exact_event_wall_faces.json",
    "post": HERE / "exact_event_post_faces.json",
}

BASE = frozenset(range(17)) | {54}
TARGET_FACE = (198, 243, 245)
EVENT_CIRCUIT = frozenset((69, 224, 255, 256))
PRE_DIAGONAL = (255, 256)
POST_DIAGONAL = (69, 224)
EXPECTED_F_VECTOR = {
    "source": [61, 162, 103],
    "pre": [61, 162, 103],
    "wall": [61, 161, 102],
    "post": [61, 162, 103],
}
EXPECTED_CLASS = [2, 2, 2]
EXPECTED_ZERO_FAMILIES = {
    "pre": {
        "support:f57:w69",
        "support:f58:w224",
        "edge_gram:255,256",
        "edge:255,256:beta1",
        "edge:255,256:beta2",
    },
    "post": {
        "support:f65:w255",
        "support:f74:w256",
        "edge_gram:69,224",
        "edge:69,224:beta1",
        "edge:69,224:beta2",
    },
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


def comma(values):
    return ",".join(str(value) for value in values)


def all_primitive_records(path, faces):
    ledger = mechanics_primitives(path, faces)
    records = [("volume:d6", ledger["d6"], True)]
    for face_index, witness, poly in support_polynomials(path, faces):
        records.append((f"support:f{face_index}:w{witness}", poly, False))
    for face_key, values in ledger["reference"].items():
        for edge, poly in values.items():
            records.append((f"face_reference:{comma(face_key)}:{comma(edge)}", poly, False))
    for edge, values in ledger["edge"].items():
        records.append((f"edge_direction_norm2:{comma(edge)}", values["direction_norm2"], True))
        records.append((f"edge_gram:{comma(edge)}", values["gram"], True))
    for face_key in ledger["face"]:
        for edge, poly in signed_face_components(ledger, face_key).items():
            records.append((f"face:{comma(face_key)}:{comma(edge)}", poly, False))
    for vertex, values in ledger["vertex"].items():
        for neighbor, poly in values.items():
            records.append((f"vertex:{vertex}:{neighbor}", poly, False))
    for edge, values in ledger["edge"].items():
        for name in ("t", "one_minus_t", "beta1", "beta2"):
            records.append((f"edge:{comma(edge)}:{name}", values[name], False))
    return records


def divide_linear_root(poly, root: Q):
    poly = Poly.coerce(poly)
    if poly.degree < 1:
        return Poly.zero(), poly.c[0]
    quotient = [Q(0)] * poly.degree
    quotient[-1] = poly.c[-1]
    for k in range(poly.degree - 1, 0, -1):
        quotient[k - 1] = poly.c[k] + root * quotient[k]
    return Poly(tuple(quotient)), poly.c[0] + root * quotient[0]


def root_factorization(poly, root: Q):
    quotient = Poly.coerce(poly)
    order = 0
    while quotient.degree > 0:
        candidate, remainder = divide_linear_root(quotient, root)
        if remainder:
            break
        quotient = candidate
        order += 1
    if not order or not quotient.eval(root):
        raise AssertionError(("bad exact event factorization", poly.degree, order))
    return order, quotient


def event_aware_interval_audit(path, faces, lo, hi, root, expected_zero_names):
    strict_rows = []
    zero_rows = []
    middle = (lo + hi) / 2
    for name, poly, intrinsically_positive in all_primitive_records(path, faces):
        if not poly.eval(root):
            order, quotient = root_factorization(poly, root)
            sign, leaves, worst = bernstein_sign(quotient, lo, hi)
            left_value = poly.eval((lo + root) / 2) if lo < root else None
            right_value = poly.eval((root + hi) / 2) if root < hi else None
            zero_rows.append(
                {
                    "name": name,
                    "degree": poly.degree,
                    "root_order": order,
                    "quotient_sign": sign,
                    "quotient_bernstein_leaves": leaves,
                    "quotient_min_bernstein_log10_abs": worst,
                    "left_sign": None if left_value is None else (1 if left_value > 0 else -1),
                    "right_sign": None if right_value is None else (1 if right_value > 0 else -1),
                    "polynomial_digest": polynomial_hash(poly),
                    "quotient_digest": polynomial_hash(quotient),
                }
            )
            continue
        expected = 1 if poly.eval(middle) > 0 else -1
        sign, leaves, worst = bernstein_sign(poly, lo, hi)
        if sign != expected:
            raise AssertionError(("primitive sign mismatch", name, sign, expected))
        if intrinsically_positive and sign != 1:
            raise AssertionError(("nonpositive intrinsic primitive", name))
        strict_rows.append((name, sign, leaves, worst, poly))
    got = {row["name"] for row in zero_rows}
    if got != expected_zero_names:
        raise AssertionError(("wrong event family", sorted(got), sorted(expected_zero_names)))
    digest = hashlib.sha256()
    for name, sign, _leaves, _worst, poly in strict_rows:
        digest.update(f"{name}|{sign}|{'|'.join(poly.exact())}\n".encode())
    return {
        "interval": [qs(lo), qs(hi)],
        "complete_primitive_count": len(strict_rows) + len(zero_rows),
        "strict_non_event_primitive_count": len(strict_rows),
        "strict_non_event_bernstein_leaves": sum(row[2] for row in strict_rows),
        "strict_non_event_min_bernstein_log10_abs": min(row[3] for row in strict_rows),
        "strict_non_event_digest": digest.hexdigest(),
        "event_family": sorted(zero_rows, key=lambda row: row["name"]),
    }


def residual_polynomials(path, faces):
    ledger = mechanics_primitives(path, faces)
    face = signed_face_components(ledger, tuple(sorted(TARGET_FACE)))
    vertex = ledger["vertex"][1]
    return {
        **{
            f"S[198,243,245]:edge({edge[0]},{edge[1]})": poly
            for edge, poly in sorted(face.items())
        },
        **{f"U1:neighbor({neighbor})": poly for neighbor, poly in sorted(vertex.items())},
        **{
            f"H(4,5):{name}": ledger["edge"][(4, 5)][name]
            for name in ("t", "one_minus_t", "beta1", "beta2")
        },
        **{
            f"H(12,13):{name}": ledger["edge"][(12, 13)][name]
            for name in ("t", "one_minus_t", "beta1", "beta2")
        },
    }


def residual_packet_audit(path, faces, root):
    active_names = {
        "S[198,243,245]:edge(198,243)",
        "U1:neighbor(2)",
        "H(4,5):one_minus_t",
        "H(12,13):one_minus_t",
    }
    records = {}
    for name, poly in sorted(residual_polynomials(path, faces).items()):
        sign, leaves, worst = bernstein_sign(poly, Q(0), root)
        if sign != 1:
            raise AssertionError(("residual component lost positivity", name))
        source_value, wall_value = poly.eval(Q(0)), poly.eval(root)
        delta = wall_value - source_value
        record = {
            "degree": poly.degree,
            "polynomial_digest": polynomial_hash(poly),
            "positive_bernstein_leaves": leaves,
            "positive_min_bernstein_log10_abs": worst,
            "source_log10_abs": qlog10(source_value),
            "wall_log10_abs": qlog10(wall_value),
            "wall_over_source_decimal": float(wall_value / source_value),
            "delta_sign": 0 if not delta else (1 if delta > 0 else -1),
            "delta_digest": canonical_hash(qs(delta)),
            "active": name in active_names,
        }
        if name in active_names:
            derivative_sign, derivative_leaves, derivative_worst = bernstein_sign(
                poly.derivative(), Q(0), root
            )
            if derivative_sign != -1 or delta >= 0:
                raise AssertionError(("active component is not directed down", name))
            record.update(
                {
                    "derivative_sign": derivative_sign,
                    "derivative_bernstein_leaves": derivative_leaves,
                    "derivative_min_bernstein_log10_abs": derivative_worst,
                    "relative_decrease_decimal": float(
                        (source_value - wall_value) / source_value
                    ),
                }
            )
        records[name] = record
    return {
        "component_count": len(records),
        "active_component_count": len(active_names),
        "components": records,
    }


def forced_rails():
    paths = (
        [228, *range(229, 247), 8],
        [228, *range(247, 265), 8],
    )
    rails = {
        tuple(sorted(edge))
        for path in paths
        for edge in zip(path, path[1:])
    }
    rails.remove((228, 229))
    return rails


def point_mechanics_rows(ledger):
    yield "volume:d6", ledger["d6"]
    for face_key, values in sorted(ledger["reference"].items()):
        for edge, value in sorted(values.items()):
            yield f"face_reference:{face_key}:{edge}", value
    for face_key, values in sorted(ledger["face"].items()):
        for edge, value in sorted(values.items()):
            yield f"face_raw:{face_key}:{edge}", value
    for vertex, values in sorted(ledger["vertex"].items()):
        for neighbor, value in sorted(values.items()):
            yield f"vertex:{vertex}:{neighbor}", value
    for edge, values in sorted(ledger["edge"].items()):
        for name in ("direction_norm2", "gram", "t", "one_minus_t", "beta1", "beta2"):
            yield f"edge:{edge}:{name}", values[name]


def checkpoint(name, points, faces):
    support = supporting_cell(points, faces)
    ledger, mechanics = classify_point(points, faces)
    if support["f_vector"] != EXPECTED_F_VECTOR[name]:
        raise AssertionError((name, support["f_vector"]))
    if mechanics["class"] != EXPECTED_CLASS:
        raise AssertionError((name, mechanics))
    if support["active_labels"] != sorted(points):
        raise AssertionError((name, "inactive row"))
    if BASE not in {frozenset(face) for face in faces}:
        raise AssertionError((name, "missing base"))
    edges = set(map(tuple, support["edges"]))
    missing = sorted(forced_rails() - edges)
    d6, m24 = exact_centroid_numerators(points, faces)
    if d6 <= 0:
        raise AssertionError((name, "nonpositive volume"))
    centroid = tuple(value / (4 * d6) for value in m24)
    rows = list(point_mechanics_rows(ledger))
    if any(not value for _label, value in rows):
        raise AssertionError((name, "zero true-feature primitive"))
    digest = hashlib.sha256()
    for label, value in rows:
        digest.update(f"{label}|{qs(value)}\n".encode())
    return {
        "coordinate_hash": point_hash(points),
        "face_hash": face_hash(faces),
        "exact_support": {key: value for key, value in support.items() if key != "edges"},
        "true_edge_count": len(edges),
        "true_edge_digest": canonical_hash(sorted(map(list, edges))),
        "exact_mechanics": mechanics,
        "mechanics_primitive_count": len(rows),
        "mechanics_min_nonzero_log10_abs": min(qlog10(value) for _label, value in rows),
        "mechanics_digest": digest.hexdigest(),
        "exact_centroid": [qs(value) for value in centroid],
        "exact_centroid_digest": canonical_hash([qs(value) for value in centroid]),
        "base_face_present": True,
        "forced_rail_count": len(forced_rails()),
        "missing_forced_rails": [list(edge) for edge in missing],
    }


def compare_with_diagnostics(got, expected, path="root"):
    """Exact comparison except explicitly human-readable floating diagnostics."""
    if isinstance(expected, dict):
        if got.keys() != expected.keys():
            raise AssertionError((path, got.keys(), expected.keys()))
        for key in expected:
            compare_with_diagnostics(got[key], expected[key], f"{path}.{key}")
        return
    if isinstance(expected, list):
        if len(got) != len(expected):
            raise AssertionError((path, len(got), len(expected)))
        for index, value in enumerate(expected):
            compare_with_diagnostics(got[index], value, f"{path}[{index}]")
        return
    diagnostic = any(
        marker in path
        for marker in (
            "log10_abs",
            "log10",
            "_decimal",
            "chart_scale_diagnostic",
        )
    )
    if diagnostic and isinstance(expected, float):
        if not math.isclose(float(got), expected, rel_tol=0.0, abs_tol=5e-13):
            raise AssertionError((path, got, expected))
        return
    if got != expected:
        raise AssertionError((path, got, expected))


def face_key_set(faces):
    return {frozenset(face) for face in faces}


def main():
    frozen = json.loads(CERTIFICATE.read_text())
    if frozen["verdict"] != "EXACT_ACTIVE_FOUR_RESIDUAL_RAY_FIRST_EVENT_RAIL_OBSTRUCTION_PASS":
        raise AssertionError("unexpected certificate verdict")
    if frozen["winner_status"] != "NONWINNER":
        raise AssertionError("local obstruction was mislabeled as a winner")

    provenance_paths = (UPSTREAM_CERTIFICATE, UPSTREAM_FACES, RAY, NUMERIC_SCAN)
    for path in provenance_paths:
        key = str(path.relative_to(ROOT))
        if frozen["provenance"][key] != sha256(path):
            raise AssertionError(("provenance hash mismatch", key))
    for name, expected in frozen["generated_file_sha256"].items():
        if sha256(HERE / name) != expected:
            raise AssertionError(("generated data changed", name))

    definition = json.loads(PATH_DEFINITION.read_text())
    source = read_exact_csv(POINT_FILES["source"])
    velocity = {
        int(label): tuple(Q(value) for value in xyz)
        for label, xyz in definition["velocity"].items()
    }
    if set(source) != set(velocity):
        raise AssertionError("source/velocity labels differ")
    if point_hash(source) != definition["source_coordinate_hash"]:
        raise AssertionError("exact source hash mismatch")
    upstream = json.loads(UPSTREAM_CERTIFICATE.read_text())
    if point_hash(source) != upstream["projective_continuation"]["far"]["coordinate_hash"]:
        raise AssertionError("local source is not the frozen exact far checkpoint")
    if canonical_hash(
        {str(label): [qs(value) for value in velocity[label]] for label in sorted(velocity)}
    ) != definition["velocity_digest"]:
        raise AssertionError("velocity digest mismatch")

    path = {
        label: tuple(Poly((source[label][axis], velocity[label][axis])) for axis in range(3))
        for label in source
    }
    root = Q(definition["event_root_exact"])
    pre_parameter = Q(definition["pre_parameter"])
    post_parameter = Q(definition["post_parameter"])
    parameters = {
        "source": Q(0),
        "pre": pre_parameter,
        "wall": root,
        "post": post_parameter,
    }
    points = {name: evaluate_path(path, parameter) for name, parameter in parameters.items()}
    faces = {name: json.loads(FACE_FILES[name].read_text()) for name in parameters}
    for name in parameters:
        if read_exact_csv(POINT_FILES[name]) != points[name]:
            raise AssertionError(("saved exact point file changed", name))

    fresh_reports = {}
    for name in parameters:
        fresh_faces, report = fresh_maximal_faces(points[name])
        if face_key_set(fresh_faces) != face_key_set(faces[name]):
            raise AssertionError(
                (
                    "independent maximal-face reconstruction mismatch",
                    name,
                    face_key_set(fresh_faces) - face_key_set(faces[name]),
                    face_key_set(faces[name]) - face_key_set(fresh_faces),
                )
            )
        if face_hash(fresh_faces) != face_hash(faces[name]):
            raise AssertionError(("canonical face hash mismatch", name))
        fresh_reports[name] = report

    support_lookup = {
        (face_index, witness): poly
        for face_index, witness, poly in support_polynomials(path, faces["pre"])
    }
    event_poly = support_lookup[(57, 69)]
    if event_poly.degree != 1:
        raise AssertionError("event polynomial is not linear")
    derived_root = -event_poly.c[0] / event_poly.c[1]
    if derived_root != root or support_lookup[(58, 224)].eval(root):
        raise AssertionError("exact paired support root mismatch")
    expected_root = frozen["event"]["root"]
    actual_root = {
        "exact": qs(root),
        "decimal": float(root),
        "polynomial_degree": event_poly.degree,
        "polynomial_exact": event_poly.exact(),
        "polynomial_digest": polynomial_hash(event_poly),
        "source_sign": 1 if event_poly.eval(Q(0)) > 0 else -1,
        "derivative_sign": 1 if event_poly.c[1] > 0 else -1,
    }
    compare_with_diagnostics(actual_root, expected_root, "event.root")

    print("clean-room complete pre-event primitive audit", flush=True)
    pre_audit = event_aware_interval_audit(
        path, faces["pre"], Q(0), root, root, EXPECTED_ZERO_FAMILIES["pre"]
    )
    print("clean-room complete post-event primitive audit", flush=True)
    post_audit = event_aware_interval_audit(
        path, faces["post"], root, post_parameter, root, EXPECTED_ZERO_FAMILIES["post"]
    )
    compare_with_diagnostics(
        pre_audit,
        frozen["event"]["complete_pre_interval_audit"],
        "event.complete_pre_interval_audit",
    )
    compare_with_diagnostics(
        post_audit,
        frozen["event"]["complete_post_interval_audit"],
        "event.complete_post_interval_audit",
    )

    print("clean-room full fourteen-component residual audit", flush=True)
    residual = residual_packet_audit(path, faces["pre"], root)
    compare_with_diagnostics(residual, frozen["residual_packet"], "residual_packet")

    rebuilt_checkpoints = {}
    for name in parameters:
        print("clean-room checkpoint", name, flush=True)
        rebuilt_checkpoints[name] = checkpoint(name, points[name], faces[name])
        compare_with_diagnostics(
            rebuilt_checkpoints[name], frozen["checkpoints"][name], f"checkpoints.{name}"
        )

    pre_edges = set(edge_data(faces["pre"])[0])
    wall_edges = set(edge_data(faces["wall"])[0])
    post_edges = set(edge_data(faces["post"])[0])
    if pre_edges - wall_edges != {PRE_DIAGONAL}:
        raise AssertionError("wrong unique pre diagonal")
    if post_edges - wall_edges != {POST_DIAGONAL}:
        raise AssertionError("wrong unique post diagonal")
    wall_quads = [face for face in faces["wall"] if frozenset(face) == EVENT_CIRCUIT]
    if len(wall_quads) != 1 or len(wall_quads[0]) != 4:
        raise AssertionError("event wall is not one convex quadrilateral")
    if rebuilt_checkpoints["source"]["missing_forced_rails"]:
        raise AssertionError("source lost a forced rail")
    if rebuilt_checkpoints["pre"]["missing_forced_rails"]:
        raise AssertionError("strict pre-cell lost a forced rail")
    if rebuilt_checkpoints["wall"]["missing_forced_rails"] != [[255, 256]]:
        raise AssertionError("wall obstruction rail mismatch")
    if rebuilt_checkpoints["post"]["missing_forced_rails"] != [[255, 256]]:
        raise AssertionError("post-cell obstruction rail mismatch")
    if any(
        rebuilt_checkpoints[name]["exact_mechanics"]["class"] != EXPECTED_CLASS
        for name in ("pre", "wall", "post")
    ):
        raise AssertionError("event changed the equilibrium class")

    manifest = {}
    for line in MANIFEST.read_text().splitlines():
        digest, name = line.split("  ", 1)
        if name in manifest:
            raise AssertionError(("duplicate manifest entry", name))
        manifest[name] = digest
    required = {
        "attack_common.py",
        "build_exact_event_certificate.py",
        "verify_exact_event_certificate.py",
        "exact_event_certificate.json",
        "exact_event_path.json",
        "exact_event_source.csv",
        "exact_event_pre.csv",
        "exact_event_wall.csv",
        "exact_event_post.csv",
        "exact_event_source_faces.json",
        "exact_event_pre_faces.json",
        "exact_event_wall_faces.json",
        "exact_event_post_faces.json",
    }
    if not required <= set(manifest):
        raise AssertionError(("manifest is incomplete", sorted(required - set(manifest))))
    for name, digest in manifest.items():
        if sha256(HERE / name) != digest:
            raise AssertionError(("manifest hash mismatch", name))

    print("INDEPENDENT_EXACT_ACTIVE_FOUR_RESIDUAL_RAY_RAIL_OBSTRUCTION_PASS")
    print("winner_status", frozen["winner_status"])
    print("event_root", qs(root))
    print("event_root_decimal", float(root))
    print("fresh_hulls", fresh_reports)
    print("classes", [rebuilt_checkpoints[name]["exact_mechanics"]["class"] for name in ("pre", "wall", "post")])
    print("post_missing_rails", rebuilt_checkpoints["post"]["missing_forced_rails"])
    print("certificate_sha256", sha256(CERTIFICATE))
    print("manifest_sha256", sha256(MANIFEST))


if __name__ == "__main__":
    main()
