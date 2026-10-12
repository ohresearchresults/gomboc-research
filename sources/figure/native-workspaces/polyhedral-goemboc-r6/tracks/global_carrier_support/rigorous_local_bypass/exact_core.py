#!/usr/bin/env python3
"""Exact rational core for the carrier local-bypass certificate.

Only finite decimal input and :class:`fractions.Fraction` arithmetic enter the
proof layer.  Floating point is used once, deterministically, to rationalize
the already saved local chart columns; those columns are immediately projected
onto an exact rational base plane.  Every subsequent topology, mechanics,
root-order, and tangent statement is exact for that explicitly frozen chart.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path


CONTROLLED = (0, 1, 5, 6, 7, 8, 9, 10, 11, 54)
BASE_CYCLE = (0, 54) + tuple(range(1, 17))
BASE = frozenset(range(17)) | {54}


def qs(x: Q) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def q17(x: float) -> Q:
    return Q(format(float(x), ".17g"))


def qlog10(x: Q) -> float:
    if not x:
        return -math.inf
    return math.log10(abs(x.numerator)) - math.log10(x.denominator)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def mul(a, s):
    return tuple(x * s for x in a)


def dot(a, b):
    zero = P.zero() if isinstance(a[0], P) or isinstance(b[0], P) else Q(0)
    return sum((x * y for x, y in zip(a, b)), zero)


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def det3(a, b, c):
    return dot(a, cross(b, c))


def norm2(a):
    return dot(a, a)


@dataclass(frozen=True)
class P:
    """Univariate polynomial over Q, coefficients low degree first."""

    c: tuple[Q, ...]

    def __post_init__(self):
        c = tuple(Q(x) for x in self.c)
        while len(c) > 1 and c[-1] == 0:
            c = c[:-1]
        object.__setattr__(self, "c", c or (Q(0),))

    @staticmethod
    def zero():
        return P((Q(0),))

    @staticmethod
    def one():
        return P((Q(1),))

    @staticmethod
    def coerce(x):
        return x if isinstance(x, P) else P((Q(x),))

    @property
    def degree(self):
        return len(self.c) - 1

    def __add__(self, other):
        other = P.coerce(other)
        n = max(len(self.c), len(other.c))
        return P(tuple(
            (self.c[i] if i < len(self.c) else Q(0))
            + (other.c[i] if i < len(other.c) else Q(0))
            for i in range(n)
        ))

    __radd__ = __add__

    def __neg__(self):
        return P(tuple(-x for x in self.c))

    def __sub__(self, other):
        return self + (-P.coerce(other))

    def __rsub__(self, other):
        return P.coerce(other) - self

    def __mul__(self, other):
        other = P.coerce(other)
        out = [Q(0)] * (len(self.c) + len(other.c) - 1)
        for i, x in enumerate(self.c):
            for j, y in enumerate(other.c):
                out[i + j] += x * y
        return P(tuple(out))

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        scalar = Q(scalar)
        if not scalar:
            raise ZeroDivisionError
        return P(tuple(x / scalar for x in self.c))

    def derivative(self):
        if len(self.c) == 1:
            return P.zero()
        return P(tuple(Q(i) * self.c[i] for i in range(1, len(self.c))))

    def eval(self, x: Q) -> Q:
        out = Q(0)
        for a in reversed(self.c):
            out = out * x + a
        return out

    def affine(self, a: Q, b: Q):
        """Return p(a+(b-a)u)."""
        z = P((Q(a), Q(b) - Q(a)))
        out = P.zero()
        for coefficient in reversed(self.c):
            out = out * z + coefficient
        return out

    def exact(self):
        return [qs(x) for x in self.c]


def poly_from_exact(values):
    return P(tuple(Q(x) for x in values))


def bernstein_coefficients(poly: P):
    n = poly.degree
    return tuple(
        sum(
            (poly.c[k] * Q(math.comb(i, k), math.comb(n, k))
             for k in range(i + 1)),
            Q(0),
        )
        for i in range(n + 1)
    )


def bernstein_sign(poly: P, a: Q, b: Q, max_depth: int = 28):
    """Prove a strict constant sign on [a,b] by exact Bernstein subdivision."""
    stack = [(Q(a), Q(b), 0)]
    worst = None
    leaves = 0
    while stack:
        lo, hi, depth = stack.pop()
        coeff = bernstein_coefficients(poly.affine(lo, hi))
        if all(x > 0 for x in coeff):
            sign = 1
        elif all(x < 0 for x in coeff):
            sign = -1
        else:
            if depth >= max_depth:
                raise AssertionError(("Bernstein sign not isolated", poly.degree, qs(lo), qs(hi)))
            mid = (lo + hi) / 2
            stack.append((mid, hi, depth + 1))
            stack.append((lo, mid, depth + 1))
            continue
        leaves += 1
        magnitude = min(abs(x) for x in coeff)
        if worst is None or qlog10(magnitude) < worst:
            worst = qlog10(magnitude)
        if 'expected' not in locals():
            expected = sign
        elif sign != expected:
            raise AssertionError("polynomial changes sign")
    return expected, leaves, worst


def isolate_monotone_root(poly: P, lo: Q, hi: Q, width: Q):
    flo, fhi = poly.eval(lo), poly.eval(hi)
    if not flo or not fhi or (flo > 0) == (fhi > 0):
        raise AssertionError(("bad root bracket", float(flo), float(fhi)))
    derivative_sign, derivative_leaves, _ = bernstein_sign(poly.derivative(), lo, hi)
    while hi - lo > width:
        mid = (lo + hi) / 2
        fm = poly.eval(mid)
        if not fm:
            lo = hi = mid
            break
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi, fhi = mid, fm
    return {
        "lo": lo,
        "hi": hi,
        "value_lo": flo,
        "value_hi": fhi,
        "derivative_sign": derivative_sign,
        "derivative_bernstein_leaves": derivative_leaves,
    }


def determinant(matrix):
    """Leibniz determinant for small polynomial/Fraction matrices."""
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    out = P.zero() if isinstance(matrix[0][0], P) else Q(0)
    for j in range(n):
        minor = [row[:j] + row[j + 1:] for row in matrix[1:]]
        term = matrix[0][j] * determinant(minor)
        out = out + term if j % 2 == 0 else out - term
    return out


def read_rows(path: Path):
    rows = {}
    with path.open(newline="") as handle:
        for row in csv.DictReader(handle):
            rows[int(row["source_id"])] = tuple(Q(row[k]) for k in ("x", "y", "z"))
    return rows


def float_rows(rows):
    return {i: tuple(float(x) for x in p) for i, p in rows.items()}


def distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def unit(a):
    scale = math.sqrt(sum(x * x for x in a))
    return tuple(x / scale for x in a)


def exact_base_chart(source_path: Path):
    """Repair the decimal base to one exact plane and build 20 exact columns."""
    source = read_rows(source_path)
    original = float_rows(source)
    a = source[0]
    plane_normal = cross(sub(source[54], a), sub(source[1], a))
    plane_norm2 = norm2(plane_normal)
    if not plane_norm2:
        raise AssertionError("degenerate base")
    repaired = dict(source)
    repair_log = {}
    for label in BASE:
        correction = dot(plane_normal, sub(repaired[label], a)) / plane_norm2
        repaired[label] = sub(repaired[label], mul(plane_normal, correction))
        repair_log[str(label)] = qlog10(correction) if correction else -math.inf
        if dot(plane_normal, sub(repaired[label], a)) != 0:
            raise AssertionError("base repair failed")

    af = original[0]
    u = unit(sub(original[54], af))
    nf = unit(cross(u, sub(original[1], af)))
    v = cross(nf, u)
    scales = {}
    for k, label in enumerate(BASE_CYCLE):
        previous = BASE_CYCLE[(k - 1) % len(BASE_CYCLE)]
        following = BASE_CYCLE[(k + 1) % len(BASE_CYCLE)]
        scales[label] = min(
            distance(original[label], original[previous]),
            distance(original[following], original[label]),
        )

    columns = []
    names = []
    zero = (Q(0), Q(0), Q(0))
    for label in CONTROLLED:
        for axis, direction in (("u", u), ("v", v)):
            raw = tuple(q17(scales[label] * z) for z in direction)
            raw = sub(raw, mul(plane_normal, dot(plane_normal, raw) / plane_norm2))
            if dot(plane_normal, raw) != 0:
                raise AssertionError("column is not exactly base tangent")
            columns.append({label: raw})
            names.append(f"row{label}_{axis}")
    return repaired, columns, names, plane_normal, repair_log


def combine_columns(columns, coefficients, labels):
    zero = (Q(0), Q(0), Q(0))
    out = {i: zero for i in labels}
    for column, coefficient in zip(columns, coefficients):
        for label, velocity in column.items():
            out[label] = add(out[label], mul(velocity, coefficient))
    return out


def apply_columns(rows, columns, parameters):
    labels = sorted(rows)
    displacement = combine_columns(columns, parameters, labels)
    return {i: add(rows[i], displacement[i]) for i in labels}


def build_charts(source_path: Path, atlas_path: Path, adaptive_path: Path):
    rows, base_columns, names, plane_normal, repair_log = exact_base_chart(source_path)
    atlas = json.loads(atlas_path.read_text())
    adaptive = json.loads(adaptive_path.read_text())
    remote = atlas["remote_basis"]
    columns = list(base_columns)
    columns.append({228: tuple(Q(str(x)) for x in remote["tangent"])})
    columns.append({228: tuple(Q(str(x)) for x in remote["normal"])})
    names += ["row228_tangent", "row228_normal"]
    star_parameters = [Q(str(x)) for x in atlas["star_parameters"]]
    direction_x = [Q(str(x)) for x in atlas["direction_x"]]
    direction_y = [Q(str(x)) for x in atlas["direction_y"]]
    star = apply_columns(rows, columns, star_parameters)
    vx = combine_columns(columns, direction_x, sorted(rows))
    vy = combine_columns(columns, direction_y, sorted(rows))

    start_parameters = [Q(str(x)) for x in adaptive["trace"][-1]["parameters"]]
    wall_direction = [Q(str(x)) for x in adaptive["wall"]["direction"]]
    adaptive_start = apply_columns(rows, columns, start_parameters)
    vt = combine_columns(columns, wall_direction, sorted(rows))
    return {
        "rows": rows,
        "columns": columns,
        "control_names": names,
        "plane_normal": plane_normal,
        "repair_log": repair_log,
        "star": star,
        "vx": vx,
        "vy": vy,
        "adaptive_start": adaptive_start,
        "vt": vt,
        "alpha_star": Q(str(atlas["alpha_star"])),
    }


def line_points(start, velocity):
    return {
        i: tuple(P((start[i][k], velocity[i][k])) for k in range(3))
        for i in start
    }


def point_on_chart(star, vx, vy, x: Q, y: Q):
    return {i: add(star[i], add(mul(vx[i], x), mul(vy[i], y))) for i in star}


def line_on_chart(star, vx, vy, x0: Q, y0: Q, x1: Q, y1: Q):
    start = point_on_chart(star, vx, vy, x0, y0)
    velocity = {i: add(mul(vx[i], x1 - x0), mul(vy[i], y1 - y0)) for i in star}
    return line_points(start, velocity)


def cycle_normal(cycle, points):
    a = points[cycle[0]]
    for j in range(1, len(cycle) - 1):
        n = cross(sub(points[cycle[j]], a), sub(points[cycle[j + 1]], a))
        if any(z != 0 for z in n):
            return n
    raise AssertionError(("flat face", cycle))


def exact_centroid_numerators(points, faces):
    d6 = P.zero() if isinstance(next(iter(points.values()))[0], P) else Q(0)
    m24 = [P.zero() if isinstance(d6, P) else Q(0) for _ in range(3)]
    for cycle in faces:
        for j in range(1, len(cycle) - 1):
            a, b, c = points[cycle[0]], points[cycle[j]], points[cycle[j + 1]]
            volume6 = det3(a, b, c)
            d6 += volume6
            for k in range(3):
                m24[k] += volume6 * (a[k] + b[k] + c[k])
    # Stored face ledgers are outward oriented and give positive d6.  Do not
    # branch on a polynomial; its positivity is separately certified.
    return d6, tuple(m24)


def scaled_centered(points, faces):
    d6, m24 = exact_centroid_numerators(points, faces)
    scale = 4 * d6
    x = {i: tuple(scale * points[i][k] - m24[k] for k in range(3)) for i in points}
    return d6, x


def edge_data(faces):
    incidence = {}
    neighbors = {}
    face_by_key = {}
    for fi, cycle in enumerate(faces):
        face_by_key[tuple(sorted(cycle))] = fi
        for a, b in zip(cycle, cycle[1:] + cycle[:1]):
            edge = tuple(sorted((a, b)))
            incidence.setdefault(edge, []).append(fi)
            neighbors.setdefault(a, set()).add(b)
            neighbors.setdefault(b, set()).add(a)
    if not all(len(v) == 2 for v in incidence.values()):
        raise AssertionError("nonmanifold ledger")
    return incidence, {i: sorted(v) for i, v in neighbors.items()}, face_by_key


def face_component(points, faces, xscaled, face_index, directed_edge):
    cycle = faces[face_index]
    n = cycle_normal(cycle, points)
    a, b = directed_edge
    edge = sub(points[b], points[a])
    nn = norm2(n)
    hbar = dot(n, xscaled[a])
    # (4*d6)*||n||^2 times the unnormalized foot component.
    raw = dot(cross(edge, sub(mul(n, hbar), mul(xscaled[a], nn))), n)
    zero = P.zero() if isinstance(points[cycle[0]][0], P) else Q(0)
    ref = tuple(sum((points[i][k] for i in cycle), zero) / len(cycle) for k in range(3))
    reference = dot(cross(edge, sub(ref, points[a])), n)
    return raw, reference


def face_components(points, faces, xscaled, face_index):
    cycle = faces[face_index]
    return [
        (tuple(sorted((a, b))), *face_component(points, faces, xscaled, face_index, (a, b)))
        for a, b in zip(cycle, cycle[1:] + cycle[:1])
    ]


def vertex_component(points, xscaled, vertex, neighbor):
    return -dot(xscaled[vertex], sub(points[neighbor], points[vertex]))


def edge_components(points, faces, xscaled, incidence, edge):
    i, j = tuple(sorted(edge))
    direction = sub(points[j], points[i])
    dd = norm2(direction)
    # Multiplication by the positive 4*d6 is already absorbed into xscaled.
    t_num = -dot(xscaled[i], direction)
    # one_minus_t numerator after the same positive scaling.
    # xscaled uses 4*d6; recover that factor through the centroid ledger at call sites.
    inc = incidence[(i, j)]
    n1 = cycle_normal(faces[inc[0]], points)
    n2 = cycle_normal(faces[inc[1]], points)
    aa, ab, cc = norm2(n1), dot(n1, n2), norm2(n2)
    r1, r2 = dot(xscaled[i], n1), dot(xscaled[i], n2)
    beta1 = r1 * cc - r2 * ab
    beta2 = r2 * aa - r1 * ab
    gram = aa * cc - ab * ab
    return {
        "t": t_num,
        "direction_norm2": dd,
        "beta1": beta1,
        "beta2": beta2,
        "gram": gram,
        "n1": n1,
        "n2": n2,
    }


def mechanics_primitives(points, faces):
    d6, xscaled = scaled_centered(points, faces)
    incidence, neighbors, face_by_key = edge_data(faces)
    face = {}
    reference = {}
    for fi, cycle in enumerate(faces):
        values = face_components(points, faces, xscaled, fi)
        face[tuple(sorted(cycle))] = {edge: raw for edge, raw, _ in values}
        reference[tuple(sorted(cycle))] = {edge: ref for edge, _, ref in values}
    vertex = {
        i: {j: vertex_component(points, xscaled, i, j) for j in neighbors[i]}
        for i in neighbors
    }
    edge = {}
    scale = 4 * d6
    for e in incidence:
        comp = edge_components(points, faces, xscaled, incidence, e)
        comp["one_minus_t"] = scale * comp["direction_norm2"] - comp["t"]
        edge[e] = comp
    return {
        "d6": d6,
        "xscaled": xscaled,
        "incidence": incidence,
        "neighbors": neighbors,
        "face_by_key": face_by_key,
        "face": face,
        "reference": reference,
        "vertex": vertex,
        "edge": edge,
    }


def signed_face_components(ledger, face_key):
    out = {}
    for edge, raw in ledger["face"][face_key].items():
        ref = ledger["reference"][face_key][edge]
        if isinstance(ref, P):
            # For path polynomials the reference sign is certified separately;
            # its sign at t=0 fixes the directed component in this small cell.
            s = 1 if ref.eval(Q(0)) > 0 else -1
        else:
            if not ref:
                raise AssertionError(("zero face reference", face_key, edge))
            s = 1 if ref > 0 else -1
        out[edge] = s * raw
    return out


def classify_point(points, faces):
    ledger = mechanics_primitives(points, faces)
    if ledger["d6"] <= 0:
        raise AssertionError("nonpositive volume")
    stable = []
    for key in ledger["face"]:
        if all(v > 0 for v in signed_face_components(ledger, key).values()):
            stable.append(key)
    unstable = [i for i, values in ledger["vertex"].items() if all(v > 0 for v in values.values())]
    saddles = []
    for edge, comp in ledger["edge"].items():
        if comp["gram"] <= 0 or comp["direction_norm2"] <= 0:
            raise AssertionError(("degenerate edge", edge))
        if all(comp[name] > 0 for name in ("t", "one_minus_t", "beta1", "beta2")):
            saddles.append(edge)
    return ledger, {
        "class": [len(stable), len(unstable), len(saddles)],
        "stable_faces": [list(x) for x in sorted(stable)],
        "unstable_vertices": sorted(unstable),
        "saddle_edges": [list(x) for x in sorted(saddles)],
    }


def supporting_cell(points, faces):
    """Exact support audit for a supplied maximal-face ledger."""
    all_labels = set(points)
    signs = []
    coplanar = 0
    coplanar_interior = []
    for cycle in faces:
        n = cycle_normal(cycle, points)
        a = points[cycle[0]]
        cset = set(cycle)
        for i in cycle[1:]:
            value = dot(n, sub(points[i], a))
            if value != 0:
                raise AssertionError(("face member not coplanar", cycle, i, qs(value)))
            coplanar += 1
        support_rows = [(i, dot(n, sub(points[i], a))) for i in sorted(all_labels - cset)]
        nonzero = [(i, v) for i, v in support_rows if v]
        zero_rows = [i for i, v in support_rows if not v]
        if not nonzero:
            raise AssertionError(("unsupported face", cycle))
        sign = 1 if nonzero[0][1] > 0 else -1
        if any((v > 0) != (sign > 0) for _, v in nonzero):
            raise AssertionError(("mixed support", cycle))
        signs.extend(sign * v for _, v in nonzero)
        if zero_rows:
            # A supplied input row may become inactive while remaining in the
            # relative interior of a maximal face (row 9 after the hard wall).
            # Prove polygon containment by every exact directed edge test.
            ref = tuple(sum((points[i][k] for i in cycle), Q(0)) / len(cycle) for k in range(3))
            for witness in zero_rows:
                for u, v in zip(cycle, cycle[1:] + cycle[:1]):
                    edge = sub(points[v], points[u])
                    ref_side = dot(cross(edge, sub(ref, points[u])), n)
                    row_side = dot(cross(edge, sub(points[witness], points[u])), n)
                    if not ref_side or row_side * ref_side <= 0:
                        raise AssertionError(("coplanar row not strict face-interior", cycle, witness, u, v))
                coplanar_interior.append((tuple(sorted(cycle)), witness))
    incidence, _, _ = edge_data(faces)
    active = set().union(*(set(c) for c in faces))
    return {
        "f_vector": [len(active), len(incidence), len(faces)],
        "euler": len(active) - len(incidence) + len(faces),
        "active_labels": sorted(active),
        "strict_support_count": len(signs),
        "min_support_log10_abs": min(qlog10(v) for v in signs),
        "coplanarity_equalities": coplanar,
        "coplanar_interior_rows": [[list(face), witness] for face, witness in coplanar_interior],
        "edges": sorted(incidence),
    }


def support_polynomials(points, faces):
    out = []
    all_labels = set(points)
    for fi, cycle in enumerate(faces):
        n = cycle_normal(cycle, points)
        a = points[cycle[0]]
        cset = set(cycle)
        for i in cycle[1:]:
            value = dot(n, sub(points[i], a))
            if value != P.zero():
                raise AssertionError(("moving face loses coplanarity", fi, i, value.exact()))
        for i in sorted(all_labels - cset):
            out.append((fi, i, dot(n, sub(points[i], a))))
    return out


def sign_at_zero(poly: P):
    value = poly.eval(Q(0))
    if not value:
        raise AssertionError("zero primitive at segment start")
    return 1 if value > 0 else -1


def certify_path_segment(points, faces, protected):
    """Certify topology and a selected exhaustive mechanics witness set on t in [0,1]."""
    ledger = mechanics_primitives(points, faces)
    records = []

    def prove(name, poly, expected=None):
        if not isinstance(poly, P):
            poly = P.coerce(poly)
        sign, leaves, worst = bernstein_sign(poly, Q(0), Q(1))
        if expected is not None and sign != expected:
            raise AssertionError((name, sign, expected))
        records.append((name, sign, leaves, worst, poly))

    prove("volume_d6", ledger["d6"], 1)
    for fi, witness, poly in support_polynomials(points, faces):
        prove(f"support:f{fi}:w{witness}", poly, sign_at_zero(poly))

    # Reference orientations and denominator factors used by all rational
    # zero-equivalent mechanics primitives.
    for face_key, refs in ledger["reference"].items():
        for edge, poly in refs.items():
            prove(f"face_reference:{face_key}:{edge}", poly, sign_at_zero(poly))
    for edge, comp in ledger["edge"].items():
        prove(f"edge_direction_norm2:{edge}", comp["direction_norm2"], 1)
        prove(f"edge_gram:{edge}", comp["gram"], 1)

    # Exact classification at t=0 supplies one negative witness for every
    # forbidden stable/unstable/saddle feature.  Protected features instead
    # have every defining component certified positive.
    p0 = {i: tuple(z.eval(Q(0)) for z in p) for i, p in points.items()}
    l0, summary = classify_point(p0, faces)
    stable_keys = {tuple(x) for x in protected["stable"]}
    unstable_keys = set(protected["unstable"])
    saddle_keys = {tuple(x) for x in protected["saddles"]}

    for face_key in ledger["face"]:
        signed = signed_face_components(ledger, face_key)
        signed0 = signed_face_components(l0, face_key)
        if face_key in stable_keys:
            for edge, poly in signed.items():
                prove(f"stable:{face_key}:{edge}", poly, 1)
        else:
            witness = min(signed0, key=signed0.get)
            if signed0[witness] >= 0:
                raise AssertionError(("no negative face witness", face_key))
            prove(f"nonstable:{face_key}:{witness}", signed[witness], -1)

    for vertex, values in ledger["vertex"].items():
        if vertex in unstable_keys:
            for neighbor, poly in values.items():
                prove(f"unstable:{vertex}:{neighbor}", poly, 1)
        else:
            witness = min(l0["vertex"][vertex], key=l0["vertex"][vertex].get)
            if l0["vertex"][vertex][witness] >= 0:
                raise AssertionError(("no negative vertex witness", vertex))
            prove(f"nonunstable:{vertex}:{witness}", values[witness], -1)

    components = ("t", "one_minus_t", "beta1", "beta2")
    for edge, values in ledger["edge"].items():
        if edge in saddle_keys:
            for component in components:
                prove(f"saddle:{edge}:{component}", values[component], 1)
        else:
            witness = min(components, key=lambda z: l0["edge"][edge][z])
            if l0["edge"][edge][witness] >= 0:
                raise AssertionError(("no negative edge witness", edge))
            prove(f"nonsaddle:{edge}:{witness}", values[witness], -1)

    digest = hashlib.sha256()
    for name, sign, leaves, worst, poly in records:
        digest.update(name.encode())
        digest.update(b"|")
        digest.update(str(sign).encode())
        digest.update(b"|")
        digest.update("|".join(poly.exact()).encode())
        digest.update(b"\n")
    return {
        "start_class": summary,
        "certified_polynomial_count": len(records),
        "bernstein_leaf_count": sum(x[2] for x in records),
        "min_bernstein_coefficient_log10_abs": min(x[3] for x in records),
        "primitive_digest": digest.hexdigest(),
    }


def certify_mechanics_interval(points, faces, protected, lo: Q, hi: Q):
    """Exhaustively certify one mechanics class on an arbitrary t interval.

    Unlike :func:`certify_path_segment`, this routine intentionally does not
    audit face support/coplanarity.  It is used at an isolated algebraic flip
    root, where a four-cycle is coplanar only at the unique root while all its
    mechanics signs can be bounded on the containing rational interval.
    """
    ledger = mechanics_primitives(points, faces)
    records = []

    def prove(name, poly, expected=None):
        if not isinstance(poly, P):
            poly = P.coerce(poly)
        sign, leaves, worst = bernstein_sign(poly, lo, hi)
        if expected is not None and sign != expected:
            raise AssertionError((name, sign, expected))
        records.append((name, sign, leaves, worst, poly))

    prove("volume_d6", ledger["d6"], 1)
    for face_key, refs in ledger["reference"].items():
        for edge, poly in refs.items():
            sign0 = 1 if poly.eval((lo + hi) / 2) > 0 else -1
            prove(f"face_reference:{face_key}:{edge}", poly, sign0)
    for edge, comp in ledger["edge"].items():
        prove(f"edge_direction_norm2:{edge}", comp["direction_norm2"], 1)
        prove(f"edge_gram:{edge}", comp["gram"], 1)

    middle = (lo + hi) / 2
    pmid = {i: tuple(z.eval(middle) for z in p) for i, p in points.items()}
    lmid, summary = classify_point(pmid, faces)
    stable_keys = {tuple(sorted(x)) for x in protected["stable"]}
    unstable_keys = set(protected["unstable"])
    saddle_keys = {tuple(sorted(x)) for x in protected["saddles"]}

    def interval_directed_face(face_key):
        out = {}
        for edge, raw in ledger["face"][face_key].items():
            ref = ledger["reference"][face_key][edge]
            out[edge] = (1 if ref.eval(middle) > 0 else -1) * raw
        return out

    for face_key in ledger["face"]:
        signed = interval_directed_face(face_key)
        signed_mid = signed_face_components(lmid, face_key)
        if face_key in stable_keys:
            for edge, poly in signed.items():
                prove(f"stable:{face_key}:{edge}", poly, 1)
        else:
            witness = min(signed_mid, key=signed_mid.get)
            if signed_mid[witness] >= 0:
                raise AssertionError(("no negative face witness", face_key))
            prove(f"nonstable:{face_key}:{witness}", signed[witness], -1)

    for vertex, values in ledger["vertex"].items():
        if vertex in unstable_keys:
            for neighbor, poly in values.items():
                prove(f"unstable:{vertex}:{neighbor}", poly, 1)
        else:
            witness = min(lmid["vertex"][vertex], key=lmid["vertex"][vertex].get)
            if lmid["vertex"][vertex][witness] >= 0:
                raise AssertionError(("no negative vertex witness", vertex))
            prove(f"nonunstable:{vertex}:{witness}", values[witness], -1)

    components = ("t", "one_minus_t", "beta1", "beta2")
    for edge, values in ledger["edge"].items():
        if edge in saddle_keys:
            for component in components:
                prove(f"saddle:{edge}:{component}", values[component], 1)
        else:
            witness = min(components, key=lambda z: lmid["edge"][edge][z])
            if lmid["edge"][edge][witness] >= 0:
                raise AssertionError(("no negative edge witness", edge))
            prove(f"nonsaddle:{edge}:{witness}", values[witness], -1)

    digest = hashlib.sha256()
    for name, sign, leaves, worst, poly in records:
        digest.update(name.encode())
        digest.update(b"|")
        digest.update(str(sign).encode())
        digest.update(b"|")
        digest.update("|".join(poly.exact()).encode())
        digest.update(b"\n")
    return {
        "midpoint_class": summary,
        "certified_polynomial_count": len(records),
        "bernstein_leaf_count": sum(x[2] for x in records),
        "min_bernstein_coefficient_log10_abs": min(x[3] for x in records),
        "primitive_digest": digest.hexdigest(),
    }


@dataclass(frozen=True)
class JP:
    """Polynomial first jet in a fixed small control list."""

    v: P
    d: tuple[P, ...]

    @staticmethod
    def coerce(x, dim):
        if isinstance(x, JP):
            return x
        return JP(P.coerce(x), (P.zero(),) * dim)

    def __add__(self, other):
        other = JP.coerce(other, len(self.d))
        return JP(self.v + other.v, tuple(a + b for a, b in zip(self.d, other.d)))

    __radd__ = __add__

    def __neg__(self):
        return JP(-self.v, tuple(-x for x in self.d))

    def __sub__(self, other):
        return self + (-JP.coerce(other, len(self.d)))

    def __rsub__(self, other):
        return JP.coerce(other, len(self.d)) - self

    def __mul__(self, other):
        other = JP.coerce(other, len(self.d))
        return JP(
            self.v * other.v,
            tuple(a * other.v + self.v * b for a, b in zip(self.d, other.d)),
        )

    __rmul__ = __mul__


def jp_points(star, vx, columns, selected):
    points = {}
    for label in star:
        coords = []
        for k in range(3):
            value = P((star[label][k], vx[label][k]))
            derivatives = tuple(P.coerce(columns[j].get(label, (Q(0),) * 3)[k]) for j in selected)
            coords.append(JP(value, derivatives))
        points[label] = tuple(coords)
    return points


def jp_value_vector(a):
    return tuple(x.v for x in a)


def jp_primitive_values(jpoints, faces):
    """Return value/gradient polynomials for the five tangent primitives."""
    # Generic vector helpers already work because JP overloads arithmetic,
    # but centroid initialization needs an explicit JP zero.
    dim = len(next(iter(jpoints.values()))[0].d)
    zero = JP(P.zero(), (P.zero(),) * dim)
    d6 = zero
    m24 = [zero, zero, zero]
    for cycle in faces:
        for j in range(1, len(cycle) - 1):
            a, b, c = jpoints[cycle[0]], jpoints[cycle[j]], jpoints[cycle[j + 1]]
            vol = det3(a, b, c)
            d6 += vol
            for k in range(3):
                m24[k] += vol * (a[k] + b[k] + c[k])
    scale = 4 * d6
    xscaled = {i: tuple(scale * jpoints[i][k] - m24[k] for k in range(3)) for i in jpoints}
    incidence, neighbors, face_by_key = edge_data(faces)

    def normal(face_key):
        cyc = faces[face_by_key[tuple(sorted(face_key))]]
        return cross(sub(jpoints[cyc[1]], jpoints[cyc[0]]), sub(jpoints[cyc[2]], jpoints[cyc[0]]))

    def face_raw(face_key, directed_edge):
        fi = face_by_key[tuple(sorted(face_key))]
        n = cycle_normal(faces[fi], jpoints)
        a, b = directed_edge
        e = sub(jpoints[b], jpoints[a])
        nn = norm2(n)
        h = dot(n, xscaled[a])
        return dot(cross(e, sub(mul(n, h), mul(xscaled[a], nn))), n)

    def vertex_raw(i, j):
        return -dot(xscaled[i], sub(jpoints[j], jpoints[i]))

    def edge_raw(edge, component):
        i, j = tuple(sorted(edge))
        direction = sub(jpoints[j], jpoints[i])
        if component == "t":
            return -dot(xscaled[i], direction)
        if component == "one_minus_t":
            return scale * norm2(direction) + dot(xscaled[i], direction)
        inc = incidence[(i, j)]
        n1 = cycle_normal(faces[inc[0]], jpoints)
        n2 = cycle_normal(faces[inc[1]], jpoints)
        aa, ab, cc = norm2(n1), dot(n1, n2), norm2(n2)
        r1, r2 = dot(xscaled[i], n1), dot(xscaled[i], n2)
        return r1 * cc - r2 * ab if component == "beta1" else r2 * aa - r1 * ab

    # Directed face signs at x=0 are positive in the fixed cell.  The selected
    # edge occurs as 8->245 in the stored S(7,8,245) cycle.
    keep = [
        face_raw((7, 8, 245), (8, 245)),
        vertex_raw(54, 1),
        edge_raw((6, 7), "t"),
        edge_raw((9, 10), "one_minus_t"),
    ]
    birth = edge_raw((8, 245), "beta1")
    return keep, birth


def exact_antibirth_tangent(star, vx, columns, faces, selected, root_lo, root_hi):
    points = jp_points(star, vx, columns, selected)
    keep, birth = jp_primitive_values(points, faces)
    gradients = [[z.d[k] for k in range(len(selected))] for z in keep]
    tangent = []
    for k in range(len(selected)):
        minor = [row[:k] + row[k + 1:] for row in gradients]
        tangent.append((1 if k % 2 == 0 else -1) * determinant(minor))
    annihilation = [sum((gradients[i][k] * tangent[k] for k in range(len(selected))), P.zero()) for i in range(4)]
    if any(z != P.zero() for z in annihilation):
        raise AssertionError("cofactor tangent does not annihilate keep rows")
    birth_rate = sum((birth.d[k] * tangent[k] for k in range(len(selected))), P.zero())
    sign, leaves, worst = bernstein_sign(birth_rate, root_lo, root_hi)
    if sign > 0:
        tangent = [-z for z in tangent]
        birth_rate = -birth_rate
        sign = -1
    augmented_det = determinant(gradients + [[birth.d[k] for k in range(len(selected))]])
    # Cofactor pairing equals augmented determinant up to the chosen convention.
    if birth_rate != augmented_det and birth_rate != -augmented_det:
        raise AssertionError("tangent/determinant identity failed")
    return {
        "selected_controls": list(selected),
        "tangent_polynomials": [z.exact() for z in tangent],
        "keep_annihilation_polynomials": [z.exact() for z in annihilation],
        "birth_rate_polynomial": birth_rate.exact(),
        "birth_rate_sign_on_root_interval": sign,
        "birth_rate_bernstein_leaves": leaves,
        "birth_rate_min_bernstein_log10_abs": worst,
        "augmented_determinant_polynomial": augmented_det.exact(),
    }


def common_birth_data(points, faces):
    ledger = mechanics_primitives(points, faces)
    f1 = ledger["face_by_key"][(7, 8, 245)]
    f2 = ledger["face_by_key"][(8, 245, 246)]
    edge = (8, 245)
    # Incidence order in the saved ledger is F1,F2.  Make the convention explicit.
    if ledger["incidence"][edge] != [f1, f2]:
        raise AssertionError(("unexpected edge incidence", ledger["incidence"][edge], f1, f2))
    n1 = cycle_normal(faces[f1], points)
    n2 = cycle_normal(faces[f2], points)
    aa, ab, cc = norm2(n1), dot(n1, n2), norm2(n2)
    gram = aa * cc - ab * ab
    r1, r2 = dot(ledger["xscaled"][245], n1), dot(ledger["xscaled"][245], n2)
    shared = r1 * cc - r2 * ab
    face_raw, face_ref = face_component(points, faces, ledger["xscaled"], f2, (245, 8))
    e = sub(points[8], points[245])
    cross_factor = dot(cross(e, n1), n2)
    # D * [(4d6)||n2||^2 face_raw] + ||n2||^2*N*cross(e,n1).n2 = 0.
    identity = gram * face_raw + cc * shared * cross_factor
    if identity != P.zero() if isinstance(identity, P) else identity != 0:
        raise AssertionError(("shared primitive identity failed", getattr(identity, "exact", lambda: identity)()))
    return {
        "shared": shared,
        "face_raw": face_raw,
        "face_reference": face_ref,
        "gram": gram,
        "cc": cc,
        "cross_factor": cross_factor,
        "identity": identity,
    }


def circuit_polynomial(points, circuit=(8, 9, 10, 263)):
    a, b, c, d = (points[i] for i in circuit)
    return det3(sub(b, a), sub(c, a), sub(d, a))


def proportional(a: P, b: P):
    """Return exact nonzero ratio a/b if the polynomials are proportional."""
    pairs = [(x, y) for x, y in zip(a.c + (Q(0),) * max(0, len(b.c) - len(a.c)),
                                     b.c + (Q(0),) * max(0, len(a.c) - len(b.c))) if x or y]
    if not pairs or any((x == 0) != (y == 0) for x, y in pairs):
        return None
    ratio = pairs[0][0] / pairs[0][1]
    return ratio if all(x == ratio * y for x, y in pairs) else None


def certify_first_support_wall(points, faces, root, target_poly):
    support = support_polynomials(points, faces)
    target_family = []
    other_count = 0
    leaves = 0
    worst = None
    # Other supports are required strict through the entire isolated target
    # interval; target-proportional slacks are allowed to vanish together.
    for fi, witness, poly in support:
        ratio = proportional(poly, target_poly)
        if ratio is not None:
            target_family.append({"face_index": fi, "witness": witness, "ratio": qs(ratio)})
            continue
        sign, count, margin = bernstein_sign(poly, Q(0), root["hi"])
        if sign != sign_at_zero(poly):
            raise AssertionError(("support wall before target", fi, witness))
        other_count += 1
        leaves += count
        worst = margin if worst is None else min(worst, margin)
    if not target_family:
        raise AssertionError("target circuit not found in support ledger")
    return {
        "target_support_family": target_family,
        "other_strict_support_polynomial_count": other_count,
        "other_support_bernstein_leaf_count": leaves,
        "other_support_min_bernstein_log10_abs": worst,
    }
