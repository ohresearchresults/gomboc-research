#!/usr/bin/env python3
"""Exact rational first-jet certificates for the two row-54 rail cells.

The input coordinates are the finite decimal values in the audited CSV files,
read as exact Fractions.  The supplied maximal-face cycles define an explicit
fixed triangulated volume/centroid ledger.  We use zero-equivalent rational
wall functions (unnormalized face-foot components, vertex support numerator,
and rational saddle components), so every rank and affine statement below is
exact for this explicitly defined rational first-jet template.

Five controls are sparse projective/trace-free-linear coordinates selected by
the numerical QR scan.  A sixth control moves row 54 tangentially in the base
plane along n_base x (q1-q0).  The script proves:

* the five cancellation gradients have exact rank five;
* six selected walls have exact gradient rank five but augmented rank six;
* an exact primitive left null vector annihilates the gradient and has
  nonzero pairing with the wall values (local affine incompatibility);
* the row-54 tangential actuator has nonzero exact left-null response and the
  resulting 6x6 gradient determinant is nonzero.

This does not assert that the nonlinear six-wall event exists or that a path
to it remains in the rail cell.  Those questions are audited separately by
rank6_row54_rail_scan.py.
"""
from __future__ import annotations

import csv
import json
import math
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ATLAS = ROOT / "tracks" / "circuit_atlas"
D = 6


@dataclass(frozen=True)
class J:
    v: Q
    d: tuple[Q, ...]

    @staticmethod
    def c(value):
        if isinstance(value, J):
            return value
        return J(Q(value), (Q(0),) * D)

    def __add__(self, other):
        z = J.c(other)
        return J(self.v + z.v, tuple(self.d[k] + z.d[k] for k in range(D)))

    __radd__ = __add__

    def __neg__(self):
        return J(-self.v, tuple(-z for z in self.d))

    def __sub__(self, other):
        return self + (-J.c(other))

    def __rsub__(self, other):
        return J.c(other) - self

    def __mul__(self, other):
        z = J.c(other)
        return J(
            self.v * z.v,
            tuple(self.d[k] * z.v + self.v * z.d[k] for k in range(D)),
        )

    __rmul__ = __mul__

    def inv(self):
        assert self.v != 0
        return J(1 / self.v, tuple(-z / (self.v * self.v) for z in self.d))

    def __truediv__(self, other):
        return self * J.c(other).inv()

    def __rtruediv__(self, other):
        return J.c(other) / self


def add(a, b):
    return tuple(a[k] + b[k] for k in range(3))


def sub(a, b):
    return tuple(a[k] - b[k] for k in range(3))


def mul(a, scalar):
    return tuple(z * scalar for z in a)


def dot(a, b):
    return sum((a[k] * b[k] for k in range(3)), J.c(0) if isinstance(a[0], J) else Q(0))


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def det3(a, b, c):
    return dot(a, cross(b, c))


def values(a):
    return tuple(z.v for z in a)


def qs(z: Q):
    return str(z.numerator) if z.denominator == 1 else f"{z.numerator}/{z.denominator}"


def qlog10(z: Q):
    if z == 0:
        return -math.inf
    return math.log10(abs(z.numerator)) - math.log10(z.denominator)


def read_rows(stem):
    rows = {}
    with (ATLAS / f"{stem}.csv").open() as f:
        for row in csv.DictReader(f):
            rows[int(row["source_id"])] = tuple(Q(row[k]) for k in ("x", "y", "z"))
    faces = json.loads((ATLAS / f"{stem}_faces.json").read_text())
    checkpoint = json.loads((HERE / f"rank6_{stem}.json").read_text())
    return rows, faces, checkpoint


def projective_velocity(index, z):
    x, y, w = z
    if index == 0:
        return (-x * x, -y * x, -w * x)
    if index == 1:
        return (-x * y, -y * y, -w * y)
    if index == 2:
        return (-x * w, -y * w, -w * w)
    if index == 3:  # H = diag(1,0,-1)
        return (x, Q(0), -w)
    if index == 4:  # xy
        return (y, x, Q(0))
    if index == 5:  # xz
        return (w, Q(0), x)
    if index == 6:  # H = diag(0,1,-1)
        return (Q(0), y, -w)
    if index == 7:  # yz
        return (Q(0), w, y)
    raise ValueError(index)


def build_jets(rows, pivots):
    count = Q(len(rows))
    origin = tuple(sum((p[k] for p in rows.values()), Q(0)) / count for k in range(3))
    centered = {i: sub(p, origin) for i, p in rows.items()}
    base_u = sub(centered[1], centered[0])
    base_n = cross(sub(centered[1], centered[0]), sub(centered[2], centered[0]))
    base_v = cross(base_n, base_u)
    assert dot(base_n, base_v) == 0
    q = {}
    for i, p in centered.items():
        velocities = [projective_velocity(index, p) for index in pivots]
        velocities.append(base_v if i == 54 else (Q(0), Q(0), Q(0)))
        coords = []
        for axis in range(3):
            coords.append(J(p[axis], tuple(v[axis] for v in velocities)))
        q[i] = tuple(coords)
    return q, centered, origin, base_v


def outward_face_normal(cycle, q, centered):
    a = q[cycle[0]]
    n = None
    n0 = None
    for j in range(1, len(cycle) - 1):
        for k in range(j + 1, len(cycle)):
            candidate0 = cross(sub(centered[cycle[j]], centered[cycle[0]]),
                               sub(centered[cycle[k]], centered[cycle[0]]))
            if candidate0 != (Q(0), Q(0), Q(0)):
                n0 = candidate0
                n = cross(sub(q[cycle[j]], a), sub(q[cycle[k]], a))
                break
        if n is not None:
            break
    assert n is not None and n0 is not None
    cset = set(cycle)
    support = [dot(n0, sub(p, centered[cycle[0]])) for i, p in centered.items() if i not in cset]
    # Decimal materialization can perturb coplanar members, but nonface support
    # is strict.  Orient by the sign of the complete nonface support sum.
    if sum(support, Q(0)) > 0:
        n = tuple(-z for z in n)
        n0 = tuple(-z for z in n0)
        support = [-z for z in support]
    assert sum(support, Q(0)) < 0
    return n


def face_normals(faces, q, centered):
    return [outward_face_normal(cyc, q, centered) for cyc in faces]


def exact_centroid(q, faces):
    d6 = J.c(0)
    m24 = [J.c(0), J.c(0), J.c(0)]
    for cyc in faces:
        for j in range(1, len(cyc) - 1):
            a, b, c = q[cyc[0]], q[cyc[j]], q[cyc[j + 1]]
            volume6 = det3(a, b, c)
            d6 += volume6
            for k in range(3):
                m24[k] += volume6 * (a[k] + b[k] + c[k])
    if d6.v < 0:
        d6 = -d6
        m24 = [-z for z in m24]
    assert d6.v > 0
    return tuple(z / (4 * d6) for z in m24), d6 / 6


def edge_incidence(faces):
    out = {}
    for fi, cyc in enumerate(faces):
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            out.setdefault(tuple(sorted((a, b))), []).append(fi)
    assert all(len(v) == 2 for v in out.values())
    return out


def face_wall(spec, faces, normals, q, centroid):
    cyc = faces[spec["face_index"]]
    n = normals[spec["face_index"]]
    h = dot(n, sub(q[cyc[0]], centroid))
    foot = mul(n, h / dot(n, n))
    x = {i: sub(q[i], centroid) for i in cyc}
    ref = tuple(sum((x[i][k] for i in cyc), J.c(0)) / len(cyc) for k in range(3))
    a, b = spec["edge"]
    e = sub(x[b], x[a])
    value = dot(cross(e, sub(foot, x[a])), n)
    reference_sign = dot(cross(sub(values(x[b]), values(x[a])),
                               sub(values(ref), values(x[a]))), values(n))
    if reference_sign < 0:
        value = -value
    return value


def vertex_wall(spec, q, centroid):
    i, j = spec["vertex"], spec["neighbor"]
    xi, xj = sub(q[i], centroid), sub(q[j], centroid)
    return -dot(xi, sub(xj, xi))


def edge_wall(spec, faces, normals, incidence, q, centroid):
    i, j = spec["edge"]
    xi, xj = sub(q[i], centroid), sub(q[j], centroid)
    direction = sub(xj, xi)
    t = -dot(xi, direction) / dot(direction, direction)
    component = spec["component"]
    if component == "t":
        return t
    if component == "one_minus_t":
        return 1 - t
    foot = add(xi, mul(direction, t))
    inc = incidence[tuple(sorted((i, j)))]
    n1, n2 = normals[inc[0]], normals[inc[1]]
    aa, bb, cc = dot(n1, n1), dot(n1, n2), dot(n2, n2)
    r1, r2 = dot(foot, n1), dot(foot, n2)
    den = aa * cc - bb * bb
    if component == "beta1":
        return (r1 * cc - r2 * bb) / den
    if component == "beta2":
        return (r2 * aa - r1 * bb) / den
    raise ValueError(component)


def wall_jet(spec, faces, normals, incidence, q, centroid):
    if spec["kind"] == "face":
        return face_wall(spec, faces, normals, q, centroid)
    if spec["kind"] == "vertex":
        return vertex_wall(spec, q, centroid)
    return edge_wall(spec, faces, normals, incidence, q, centroid)


def matrix_rank(rows):
    a = [[Q(z) for z in row] for row in rows]
    nr, nc = len(a), len(a[0])
    rank = 0
    for col in range(nc):
        pivot = next((r for r in range(rank, nr) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        value = a[rank][col]
        a[rank] = [z / value for z in a[rank]]
        for r in range(nr):
            if r != rank and a[r][col]:
                value = a[r][col]
                a[r] = [a[r][k] - value * a[rank][k] for k in range(nc)]
        rank += 1
        if rank == nr:
            break
    return rank


def determinant(square):
    a = [[Q(z) for z in row] for row in square]
    n = len(a)
    out = Q(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            out = -out
        value = a[col][col]
        out *= value
        for r in range(col + 1, n):
            if not a[r][col]:
                continue
            factor = a[r][col] / value
            for k in range(col, n):
                a[r][k] -= factor * a[col][k]
    return out


def primitive_left_null(rows6x5):
    lam = []
    for i in range(6):
        minor = [rows6x5[j] for j in range(6) if j != i]
        lam.append((Q(-1) if i % 2 else Q(1)) * determinant(minor))
    assert any(lam)
    for k in range(5):
        assert sum((lam[i] * rows6x5[i][k] for i in range(6)), Q(0)) == 0
    lcm = 1
    for z in lam:
        lcm = math.lcm(lcm, z.denominator)
    ints = [int(z * lcm) for z in lam]
    gcd = 0
    for z in ints:
        gcd = math.gcd(gcd, abs(z))
    ints = [z // gcd for z in ints]
    if next(z for z in ints if z) < 0:
        ints = [-z for z in ints]
    return ints


def jet_record(z):
    return {
        "value_exact": qs(z.v),
        "value_decimal": float(z.v),
        "gradient_exact": [qs(t) for t in z.d],
        "gradient_decimal": [float(t) for t in z.d],
    }


def certify(stem):
    rows, faces, checkpoint = read_rows(stem)
    pivots = checkpoint["qr_rank5_theta_pivots"]
    q, centered, origin, actuator = build_jets(rows, pivots)
    normals = face_normals(faces, q, centered)
    centroid, volume = exact_centroid(q, faces)
    incidence = edge_incidence(faces)
    specs = checkpoint["wall_specs"] + [checkpoint["sixth_wall_spec"]]
    walls = [wall_jet(s, faces, normals, incidence, q, centroid) for s in specs]
    gradients5 = [list(z.d[:5]) for z in walls[:5]]
    gradients6x5 = [list(z.d[:5]) for z in walls]
    gradients6x6 = [list(z.d) for z in walls]
    augmented = [list(z.d[:5]) + [z.v] for z in walls]
    ranks = {
        "five_wall_gradient_5x5": matrix_rank(gradients5),
        "six_wall_gradient_6x5": matrix_rank(gradients6x5),
        "six_wall_augmented_value_gradient_6x6": matrix_rank(augmented),
        "six_wall_with_row54_tangent_actuator_6x6": matrix_rank(gradients6x6),
    }
    assert ranks == {
        "five_wall_gradient_5x5": 5,
        "six_wall_gradient_6x5": 5,
        "six_wall_augmented_value_gradient_6x6": 6,
        "six_wall_with_row54_tangent_actuator_6x6": 6,
    }
    lam = primitive_left_null(gradients6x5)
    lambda_gradient = [
        sum((Q(lam[i]) * gradients6x5[i][k] for i in range(6)), Q(0))
        for k in range(5)
    ]
    lambda_value = sum((Q(lam[i]) * walls[i].v for i in range(6)), Q(0))
    lambda_actuator = sum((Q(lam[i]) * walls[i].d[5] for i in range(6)), Q(0))
    det6 = determinant(gradients6x6)
    assert lambda_gradient == [Q(0)] * 5
    assert lambda_value != 0 and lambda_actuator != 0 and det6 != 0

    # Exact inequality-form Farkas subsets in explicit local trust boxes.
    # Each mechanical row is a necessary target inequality wall(x) <= 0,
    # hence grad*x <= -value.  The sparse supports were selected numerically
    # once and are reconstructed here entirely with Fractions.
    basis = [tuple(Q(1) if j == k else Q(0) for j in range(5)) for k in range(5)]
    if stem == "row54_endpoint_rebuilt":
        radius = Q(1, 5)
        trust_rows = [
            ("death_U54 <= 0", tuple(walls[1].d[:5]), -walls[1].v),
            ("death_H67 <= 0", tuple(walls[2].d[:5]), -walls[2].v),
            ("first_crossed_guard <= 0", tuple(walls[5].d[:5]), -walls[5].v),
            ("control_1 <= 1/5", basis[1], radius),
            ("-control_2 <= 1/5", tuple(-z for z in basis[2]), radius),
            ("control_4 <= 1/5", basis[4], radius),
        ]
    else:
        radius = Q(1, 100)
        trust_rows = [
            ("death_U54 <= 0", tuple(walls[1].d[:5]), -walls[1].v),
            ("-control_0 <= 1/100", tuple(-z for z in basis[0]), radius),
            ("control_1 <= 1/100", basis[1], radius),
            ("-control_2 <= 1/100", tuple(-z for z in basis[2]), radius),
            ("-control_3 <= 1/100", tuple(-z for z in basis[3]), radius),
            ("-control_4 <= 1/100", tuple(-z for z in basis[4]), radius),
        ]
    trust_A = [list(z[1]) for z in trust_rows]
    trust_b = [z[2] for z in trust_rows]
    trust_lam = primitive_left_null(trust_A)
    if all(z < 0 for z in trust_lam):
        trust_lam = [-z for z in trust_lam]
    assert all(z > 0 for z in trust_lam)
    trust_gradient = [
        sum((Q(trust_lam[i]) * trust_A[i][k] for i in range(6)), Q(0))
        for k in range(5)
    ]
    trust_rhs = sum((Q(trust_lam[i]) * trust_b[i] for i in range(6)), Q(0))
    assert trust_gradient == [Q(0)] * 5 and trust_rhs < 0
    return {
        "cell": stem,
        "scope": (
            "Exact Fraction first jet of the finite-decimal CSV coordinates, supplied fixed face ledger, "
            "oriented-volume centroid, and explicitly listed zero-equivalent rational wall functions."
        ),
        "five_projective_control_indices": pivots,
        "control_convention": {
            "pole_k": "dq_i/dt = -q_i*q_i[k] after rational arithmetic-mean centering",
            "linear_3_to_7": (
                "trace-free symmetric generators diag(1,0,-1), xy, xz, "
                "diag(0,1,-1), yz"
            ),
            "sixth_actuator": "row54 along n_base x (q1-q0), an exact base-plane tangent",
            "sixth_actuator_direction_exact": [qs(z) for z in actuator],
        },
        "wall_order": [s["name"] for s in specs],
        "wall_specs": specs,
        "walls": [jet_record(z) for z in walls],
        "centroid": [jet_record(z) for z in centroid],
        "volume": jet_record(volume),
        "ranks": ranks,
        "exact_local_affine_certificate": {
            "primitive_integer_left_null_vector": lam,
            "lambda_times_five_control_gradient_exact": [qs(z) for z in lambda_gradient],
            "lambda_times_wall_values_exact": qs(lambda_value),
            "lambda_times_wall_values_sign": 1 if lambda_value > 0 else -1,
            "lambda_times_wall_values_log10_abs": qlog10(lambda_value),
            "conclusion": (
                "No increment in the explicit five-control first jet solves all six affine wall equations."
            ),
        },
        "exact_sixth_actuator_rank_lift": {
            "lambda_times_row54_tangent_column_exact": qs(lambda_actuator),
            "lambda_times_row54_tangent_column_sign": 1 if lambda_actuator > 0 else -1,
            "lambda_times_row54_tangent_column_log10_abs": qlog10(lambda_actuator),
            "six_by_six_gradient_determinant_exact": qs(det6),
            "six_by_six_gradient_determinant_log10_abs": qlog10(det6),
            "conclusion": (
                "The row54 base-tangent actuator removes the exact first-order rank defect. "
                "This is not, by itself, a nonlinear shared-event witness."
            ),
        },
        "exact_trust_box_inequality_farkas": {
            "system_form": "A*x <= b",
            "trust_box": f"abs(each of five controls) <= {qs(radius)}",
            "inequality_order": [z[0] for z in trust_rows],
            "A_exact": [[qs(t) for t in z[1]] for z in trust_rows],
            "b_exact": [qs(z[2]) for z in trust_rows],
            "primitive_positive_integer_multipliers": trust_lam,
            "lambda_times_A_exact": [qs(z) for z in trust_gradient],
            "lambda_times_b_exact": qs(trust_rhs),
            "lambda_times_b_log10_abs": qlog10(trust_rhs),
            "conclusion": (
                "The listed necessary linearized inequalities are infeasible in the stated trust box, "
                "because lambda is strictly positive, lambda^T*A=0, and lambda^T*b<0."
            ),
        },
    }


def main():
    cells = [
        certify("row54_endpoint_rebuilt"),
        certify("row54_far_rebuilt"),
    ]
    out = {
        "version": 1,
        "type": "exact rational rank-5 affine obstruction and rank-6 actuator certificate",
        "cells": cells,
    }
    path = HERE / "rank6_row54_exact_affine.json"
    path.write_text(json.dumps(out, indent=2) + "\n")
    print("ROW54_EXACT_AFFINE_RANK6_PASS")
    for c in cells:
        print(c["cell"], c["ranks"])
        print("lambda*f", c["exact_local_affine_certificate"]["lambda_times_wall_values_log10_abs"])
        print("lambda*actuator", c["exact_sixth_actuator_rank_lift"]["lambda_times_row54_tangent_column_log10_abs"])
        print("det6", c["exact_sixth_actuator_rank_lift"]["six_by_six_gradient_determinant_log10_abs"])
        print("trust Farkas rhs", c["exact_trust_box_inequality_farkas"]["lambda_times_b_log10_abs"])
    print("output", path)


if __name__ == "__main__":
    main()
