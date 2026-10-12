#!/usr/bin/env python3
"""Directed-rational interval certificate for normalized core beta obstruction.

All rational operations are exact intervals.  Square roots are enclosed by
integer square-root bounds with a fixed decimal denominator.  A Krawczyk
inclusion then proves existence of a positive dual solving A^T y=0 exactly
for the analytic (not finite-difference) normalized Jacobian.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import rational_core_beta_certificate as base  # noqa: E402


SQRT_DIGITS = 90
SQRT_SCALE = 10 ** SQRT_DIGITS
SERIAL_DIGITS = 80
SERIAL_SCALE = 10 ** SERIAL_DIGITS
DIM = base.DIM


def sqrt_lower(x: F) -> F:
    assert x >= 0
    k = math.isqrt((x.numerator * SQRT_SCALE * SQRT_SCALE) // x.denominator)
    return F(k, SQRT_SCALE)


def sqrt_upper(x: F) -> F:
    assert x >= 0
    low = sqrt_lower(x)
    return low if low * low == x else low + F(1, SQRT_SCALE)


@dataclass(frozen=True)
class Interval:
    lo: F
    hi: F

    def __post_init__(self):
        assert self.lo <= self.hi

    @classmethod
    def point(cls, x: object):
        value = F(x)
        return cls(value, value)

    def coerce(self, other: object):
        return other if isinstance(other, Interval) else Interval.point(other)

    def __add__(self, other: object):
        z = self.coerce(other)
        return Interval(self.lo + z.lo, self.hi + z.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other: object):
        return self + (-self.coerce(other))

    def __rsub__(self, other: object):
        return self.coerce(other) - self

    def __mul__(self, other: object):
        z = self.coerce(other)
        products = (self.lo * z.lo, self.lo * z.hi,
                    self.hi * z.lo, self.hi * z.hi)
        return Interval(min(products), max(products))

    __rmul__ = __mul__

    def reciprocal(self):
        assert not (self.lo <= 0 <= self.hi), (self.lo, self.hi)
        return Interval(min(F(1, 1) / self.lo, F(1, 1) / self.hi),
                        max(F(1, 1) / self.lo, F(1, 1) / self.hi))

    def __truediv__(self, other: object):
        return self * self.coerce(other).reciprocal()

    def __rtruediv__(self, other: object):
        return self.coerce(other) / self

    def sqrt(self):
        assert self.lo >= 0
        return Interval(sqrt_lower(self.lo), sqrt_upper(self.hi))

    def midpoint(self) -> F:
        return (self.lo + self.hi) / 2

    def max_abs(self) -> F:
        return max(abs(self.lo), abs(self.hi))


@dataclass(frozen=True)
class Dual:
    value: Interval
    grad: tuple[Interval, ...]

    @classmethod
    def constant(cls, x: object):
        return cls(Interval.point(x), (Interval.point(0),) * DIM)

    def coerce(self, other: object):
        return other if isinstance(other, Dual) else Dual.constant(other)

    def __add__(self, other: object):
        z = self.coerce(other)
        return Dual(self.value + z.value,
                    tuple(a + b for a, b in zip(self.grad, z.grad)))

    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.value, tuple(-x for x in self.grad))

    def __sub__(self, other: object):
        return self + (-self.coerce(other))

    def __rsub__(self, other: object):
        return self.coerce(other) - self

    def __mul__(self, other: object):
        z = self.coerce(other)
        return Dual(self.value * z.value,
                    tuple(self.value * b + z.value * a
                          for a, b in zip(self.grad, z.grad)))

    __rmul__ = __mul__

    def __truediv__(self, other: object):
        z = self.coerce(other)
        return Dual(self.value / z.value,
                    tuple((a * z.value - self.value * b) / (z.value * z.value)
                          for a, b in zip(self.grad, z.grad)))

    def __rtruediv__(self, other: object):
        return self.coerce(other) / self

    def sqrt(self):
        root = self.value.sqrt()
        return Dual(root, tuple(g / (2 * root) for g in self.grad))


Vec = tuple[Dual, Dual, Dual]


def vec(values) -> Vec:
    out = tuple(x if isinstance(x, Dual) else Dual.constant(x) for x in values)
    return out  # type: ignore[return-value]


def vadd(a: Vec, b: Vec) -> Vec:
    return tuple(x + y for x, y in zip(a, b))  # type: ignore[return-value]


def vsub(a: Vec, b: Vec) -> Vec:
    return tuple(x - y for x, y in zip(a, b))  # type: ignore[return-value]


def vscale(a: Vec, s: object) -> Vec:
    return tuple(x * s for x in a)  # type: ignore[return-value]


def dot(a: Vec, b: Vec) -> Dual:
    return sum((x * y for x, y in zip(a, b)), Dual.constant(0))


def cross(a: Vec, b: Vec) -> Vec:
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def vsum(values) -> Vec:
    total = vec((0, 0, 0))
    for value in values:
        total = vadd(total, value)
    return total


def chart_points():
    p = {row: vec(xyz) for row, xyz in base.RATIONAL_POINTS.items()}
    col = 0
    for row in base.CORE:
        coords = []
        for k, value in enumerate(base.RATIONAL_POINTS[row]):
            grad = [Interval.point(0)] * DIM
            grad[col + k] = Interval.point(1)
            coords.append(Dual(Interval.point(value), tuple(grad)))
        p[row] = vec(coords)
        col += 3
    return p


def centroid(p):
    d6 = Dual.constant(0)
    moment = vec((0, 0, 0))
    for cyc in base.FACES:
        for j in range(1, len(cyc) - 1):
            a, b, c = p[cyc[0]], p[cyc[j]], p[cyc[j + 1]]
            determinant = dot(a, cross(b, c))
            d6 += determinant
            moment = vadd(moment, vscale(vadd(vadd(a, b), c), determinant))
    assert d6.value.lo > 0
    return vscale(moment, F(1, 4) / d6)


def unit_normals(p):
    normals = []
    for cyc in base.FACES:
        a = p[cyc[0]]
        normal = None
        for j in range(1, len(cyc) - 1):
            trial = cross(vsub(p[cyc[j]], a), vsub(p[cyc[j + 1]], a))
            if dot(trial, trial).value.lo > 0:
                normal = trial
                break
        assert normal is not None
        area = vsum(cross(p[u], p[v]) for u, v in zip(cyc, cyc[1:] + cyc[:1]))
        orientation = dot(area, normal).value
        assert orientation.lo > 0 or orientation.hi < 0
        if orientation.hi < 0:
            normal = vscale(normal, -1)
        normal = vscale(normal, 1 / dot(normal, normal).sqrt())
        normals.append(normal)
    return normals


def normalized_edge_components(edge, p, center, normals):
    a, b = tuple(sorted(edge))
    xa = vsub(p[a], center)
    direction = vsub(p[b], p[a])
    d2 = dot(direction, direction)
    t = -dot(xa, direction) / d2
    q = vadd(xa, vscale(direction, t))
    f1, f2 = base.EDGE_FACES[(a, b)]
    n1, n2 = normals[f1], normals[f2]
    aa, bb, cc = dot(n1, n1), dot(n1, n2), dot(n2, n2)
    r1, r2 = dot(q, n1), dot(q, n2)
    den = aa * cc - bb * bb
    assert den.value.lo > 0
    beta1 = (r1 * cc - r2 * bb) / den
    beta2 = (r2 * aa - r1 * bb) / den
    qnorm = dot(q, q).sqrt()
    return [t, 1 - t, beta1 / qnorm, beta2 / qnorm]


def interval_features():
    p = chart_points()
    center = centroid(p)
    normals = unit_normals(p)
    _, _, _, _, templates = base.numeric.detailed_features(np.zeros(DIM))
    target = ("target:saddle-beta1-death",
              -normalized_edge_components(base.SADDLE, p, center, normals)[2])
    guards = [
        (f"guard:antiedge:{edge[0]}-{edge[1]}:c{k}",
         -normalized_edge_components(edge, p, center, normals)[k])
        for edge, k in sorted(templates["edge"].items())
    ]
    return [target, *guards]


def matvec(matrix, vector):
    return [sum((entry * value for entry, value in zip(row, vector)), Interval.point(0))
            for row in matrix]


def krawczyk(matrix, rhs, center_float):
    midpoint = np.asarray([[float(x.midpoint()) for x in row] for row in matrix])
    inverse = np.linalg.inv(midpoint)
    center = [F(format(x, ".17g")) for x in center_float]
    preconditioner = [[F(format(x, ".17g")) for x in row] for row in inverse]
    center_i = [Interval.point(x) for x in center]
    residual = [Interval.point(c) - z for c, z in zip(rhs, matvec(matrix, center_i))]
    correction = [sum((Interval.point(r) * z for r, z in zip(row, residual)),
                      Interval.point(0)) for row in preconditioner]
    rm = [[sum((Interval.point(r) * matrix[k][j]
               for k, r in enumerate(row)), Interval.point(0))
           for j in range(len(matrix))] for row in preconditioner]
    error = [[Interval.point(int(i == j)) - rm[i][j]
              for j in range(len(matrix))] for i in range(len(matrix))]
    radii = [abs(value) / 4 for value in center]
    assert all(radius > 0 for radius in radii)
    delta_box = [Interval(-radius, radius) for radius in radii]
    image = [correction[i] + sum((error[i][j] * delta_box[j]
                                  for j in range(len(matrix))), Interval.point(0))
             for i in range(len(matrix))]
    inclusion = all(-radius < value.lo and value.hi < radius
                    for radius, value in zip(radii, image))
    # Strict inclusion gives a unique fixed point in X.  A fixed point lies
    # in K(X), so center+image is a sharper certified enclosure than X itself.
    solution_box = [Interval.point(value) + delta
                    for value, delta in zip(center, image)]
    return inclusion, solution_box, image


def interval_json(x: Interval):
    # Outward rounding to a fixed rational decimal grid prevents harmless
    # dependency-denominator growth from producing multi-megabyte integers.
    lo = F((x.lo.numerator * SERIAL_SCALE) // x.lo.denominator, SERIAL_SCALE)
    hi = F(-((-x.hi.numerator * SERIAL_SCALE) // x.hi.denominator), SERIAL_SCALE)
    assert lo <= x.lo <= x.hi <= hi
    return {
        "lo_numerator": str(lo.numerator), "lo_denominator": str(lo.denominator),
        "hi_numerator": str(hi.numerator), "hi_denominator": str(hi.denominator),
        "lo_decimal": float(lo), "hi_decimal": float(hi),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=HERE / "core_beta_interval.json")
    args = ap.parse_args()
    features = interval_features()
    epsilon = F(1, 1_000_000)
    names, a, b, scales = [], [], [], []
    for index, (name, item) in enumerate(features):
        raw_a = [-x for x in item.grad]
        raw_b = item.value - (epsilon if index == 0 else F(0))
        magnitude = max([raw_b.max_abs(), *(x.max_abs() for x in raw_a)])
        scale = F(1, 1) / magnitude
        names.append(name); a.append([x * scale for x in raw_a])
        b.append(raw_b * scale); scales.append(scale)
    af = np.asarray([[float(x.midpoint()) for x in row] for row in a])
    bf = np.asarray([float(x.midpoint()) for x in b])
    dual_lp = linprog(
        bf, A_eq=np.vstack((af.T, np.ones(len(bf)))),
        b_eq=np.r_[np.zeros(DIM), 1.0], bounds=[(0, None)] * len(bf), method="highs",
    )
    assert dual_lp.success, dual_lp.message
    support = np.flatnonzero(dual_lp.x > 1e-10).tolist()
    sub_a, sub_b = [a[row] for row in support], [b[row] for row in support]
    matrix = [[sub_a[col][row] for col in range(len(support))]
              for row in range(DIM)]
    matrix.append([Interval.point(1) for _ in support])
    rhs = [F(0)] * DIM + [F(1)]
    assert len(support) == len(matrix), (len(support), len(matrix))
    mid_matrix = np.asarray([[float(x.midpoint()) for x in row] for row in matrix])
    center = np.linalg.solve(mid_matrix, np.asarray([float(x) for x in rhs]))
    inclusion, y_box, image = krawczyk(matrix, rhs, center)
    b_dot_y = sum((value * weight for value, weight in zip(sub_b, y_box)),
                  Interval.point(0))
    positive = all(weight.lo > 0 for weight in y_box)
    certificate_pass = inclusion and positive and b_dot_y.hi < 0
    out = {
        "statement": (
            "Directed-rational interval/Krawczyk certificate for analytic normalized "
            "core beta1-death versus fixed anti-edge witnesses"
        ),
        "sqrt_digits": SQRT_DIGITS,
        "source_hashes": {
            base.SOURCE.name: base.row54_exact.sha256(base.SOURCE),
            base.FACES_SOURCE.name: base.row54_exact.sha256(base.FACES_SOURCE),
        },
        "feature_count": len(features),
        "support_size": len(support),
        "float_dual_objective": float(dual_lp.fun),
        "krawczyk_strict_inclusion": inclusion,
        "dual_box_strictly_positive": positive,
        "b_dot_y": interval_json(b_dot_y),
        "certificate_pass": certificate_pass,
        "support": [{
            "row": row, "name": names[row], "scale": str(scales[row]),
            "A_intervals": [interval_json(x) for x in a[row]],
            "b_interval": interval_json(b[row]),
            "y_interval": interval_json(weight),
            "krawczyk_delta_image": interval_json(delta),
        } for row, weight, delta in zip(support, y_box, image)],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps({
        "feature_count": len(features), "support_size": len(support),
        "float_dual_objective": float(dual_lp.fun),
        "krawczyk_strict_inclusion": inclusion,
        "dual_box_strictly_positive": positive,
        "b_dot_y": [float(b_dot_y.lo), float(b_dot_y.hi)],
        "certificate_pass": certificate_pass,
        "support_names": [names[row] for row in support],
    }, indent=2))


if __name__ == "__main__":
    main()
