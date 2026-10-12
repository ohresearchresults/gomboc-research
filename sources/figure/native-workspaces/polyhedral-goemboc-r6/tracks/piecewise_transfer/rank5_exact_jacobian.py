#!/usr/bin/env python3
"""Exact first-jet certificate for an explicit five-control shell template.

This script works inside the strict actual cell of rank5_reconstruction.json.
It differentiates the exact oriented-face volume, ordinary-volume centroid and
selected mechanical wall numerators with Fraction-valued forward jets.

The five controls are:
  r228 : row 228 along q* - q_original;
  r229 : row 229 along (41,-16,2);
  r254 : row 254 along (-18,-36,-9);
  r255 : row 255 along (-18,-36,-9);
  t231 : row 231 tangentially in the shell plane along (-24,132,40).

The output records exact values, exact gradients and exact ranks of selected
wall systems.  It is a local, explicitly scoped rank certificate, not a global
nonexistence claim.
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path

import rank5_exact_reconstruction as ex

HERE = Path(__file__).resolve().parent
M = 5
CONTROL_NAMES = ["r228", "r229", "r254", "r255", "t231"]


@dataclass(frozen=True)
class J:
    v: Q
    d: tuple[Q, ...]

    @staticmethod
    def c(x):
        if isinstance(x, J):
            return x
        return J(Q(x), (Q(0),) * M)

    def __add__(self, other):
        o = J.c(other)
        return J(self.v + o.v, tuple(self.d[k] + o.d[k] for k in range(M)))

    __radd__ = __add__

    def __neg__(self):
        return J(-self.v, tuple(-z for z in self.d))

    def __sub__(self, other):
        return self + (-J.c(other))

    def __rsub__(self, other):
        return J.c(other) - self

    def __mul__(self, other):
        o = J.c(other)
        return J(
            self.v * o.v,
            tuple(self.d[k] * o.v + self.v * o.d[k] for k in range(M)),
        )

    __rmul__ = __mul__

    def inv(self):
        assert self.v != 0
        return J(
            1 / self.v,
            tuple(-self.d[k] / (self.v * self.v) for k in range(M)),
        )

    def __truediv__(self, other):
        return self * J.c(other).inv()

    def __rtruediv__(self, other):
        return J.c(other) / self


def jadd(a, b):
    return tuple(a[k] + b[k] for k in range(3))


def jsub(a, b):
    return tuple(a[k] - b[k] for k in range(3))


def jmul(a, t):
    return tuple(a[k] * t for k in range(3))


def jdot(a, b):
    return sum((a[k] * b[k] for k in range(3)), J.c(0))


def jcross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def jdet(a, b, c):
    return jdot(a, jcross(b, c))


def jn2(a):
    return jdot(a, a)


def qj(x, control=None, direction=None):
    out = []
    for k in range(3):
        d = [Q(0)] * M
        if control is not None:
            d[control] = Q(direction[k])
        out.append(J(Q(x[k]), tuple(d)))
    return tuple(out)


def build_jets(rows0):
    original = ex.read_exact_rows()
    # read_exact_rows already changes row228, so recover the authoritative
    # original row228 directly from the common-lattice file.
    import csv

    p = ex.WORK / "fifth_cell_endpoint" / "input_rows_common_lattice.csv"
    q228_original = None
    for row in csv.DictReader(p.open()):
        if int(row["source_id"]) == 228:
            den = int(row["denominator"])
            q228_original = tuple(Q(int(row[k]), den) for k in ("x_int", "y_int", "z_int"))
            break
    assert q228_original is not None
    dirs = {
        228: (0, ex.sub(rows0[228], q228_original)),
        229: (1, (Q(41), Q(-16), Q(2))),
        254: (2, (Q(-18), Q(-36), Q(-9))),
        255: (3, (Q(-18), Q(-36), Q(-9))),
        231: (4, (Q(-24), Q(132), Q(40))),
    }
    assert ex.dot(ex.N, dirs[231][1]) == 0
    return {
        i: qj(p, *(dirs[i] if i in dirs else (None, None))) for i, p in rows0.items()
    }, dirs


def face_normal(face, q):
    c = face["cycle"]
    a = q[c[0]]
    for j in range(1, len(c) - 1):
        for k in range(j + 1, len(c)):
            # The exact seed certifies noncollinearity for the selected triple.
            nv = ex.cross(
                ex.sub(tuple(z.v for z in q[c[j]]), tuple(z.v for z in a)),
                ex.sub(tuple(z.v for z in q[c[k]]), tuple(z.v for z in a)),
            )
            if nv != ex.ZERO:
                n = jcross(jsub(q[c[j]], a), jsub(q[c[k]], a))
                # Match the exact outward orientation stored by reconstruction.
                if ex.dot(nv, face["n"]) < 0:
                    n = tuple(-z for z in n)
                return n
    raise AssertionError("collinear face")


def exact_centroid(q, faces):
    d6 = J.c(0)
    m24 = [J.c(0), J.c(0), J.c(0)]
    for f in faces:
        c = f["cycle"]
        for j in range(1, len(c) - 1):
            a, b, z = (q[i] for i in (c[0], c[j], c[j + 1]))
            dd = jdet(a, b, z)
            d6 += dd
            for k in range(3):
                m24[k] += dd * (a[k] + b[k] + z[k])
    assert d6.v > 0
    return tuple(m24[k] / (4 * d6) for k in range(3)), d6 / 6


def face_components(face, q, c):
    cyc = face["cycle"]
    n = face_normal(face, q)
    h = jdot(n, jsub(q[cyc[0]], c))
    foot = jmul(n, h / jn2(n))
    x = {i: jsub(q[i], c) for i in cyc}
    ref = tuple(sum((x[i][k] for i in cyc), J.c(0)) / len(cyc) for k in range(3))
    out = []
    for a, b in zip(cyc, cyc[1:] + cyc[:1]):
        e = jsub(x[b], x[a])
        z = jdot(jcross(e, jsub(foot, x[a])), n)
        rz = ex.dot(
            ex.cross(
                ex.sub(tuple(t.v for t in x[b]), tuple(t.v for t in x[a])),
                ex.sub(tuple(t.v for t in ref), tuple(t.v for t in x[a])),
            ),
            tuple(t.v for t in n),
        )
        if rz < 0:
            z = -z
        out.append(((a, b), z))
    return out


def vertex_support(i, j, q, c):
    xi, xj = jsub(q[i], c), jsub(q[j], c)
    return -jdot(xi, jsub(xj, xi))


def edge_components(edge, inc, faces, q, c):
    i, j = edge
    xi, xj = jsub(q[i], c), jsub(q[j], c)
    d = jsub(xj, xi)
    t = -jdot(xi, d) / jn2(d)
    p = jadd(xi, jmul(d, t))
    n1, n2v = (face_normal(faces[k], q) for k in inc)
    aa, bb, cc = jn2(n1), jdot(n1, n2v), jn2(n2v)
    r1, r2 = jdot(p, n1), jdot(p, n2v)
    den = aa * cc - bb * bb
    b1 = (r1 * cc - r2 * bb) / den
    b2 = (r2 * aa - r1 * bb) / den
    return {"t": t, "one_minus_t": 1 - t, "beta1": b1, "beta2": b2}


def rec(z):
    return {
        "value_exact": ex.qs(z.v),
        "value_decimal": float(z.v),
        "gradient_exact": [ex.qs(t) for t in z.d],
        "gradient_decimal": [float(t) for t in z.d],
    }


def matrix_rank(rows):
    a = [[Q(z) for z in row] for row in rows]
    if not a:
        return 0
    nr, nc = len(a), len(a[0])
    rank = 0
    for col in range(nc):
        pivot = next((r for r in range(rank, nr) if a[r][col] != 0), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        z = a[rank][col]
        a[rank] = [x / z for x in a[rank]]
        for r in range(nr):
            if r != rank and a[r][col] != 0:
                z = a[r][col]
                a[r] = [a[r][k] - z * a[rank][k] for k in range(nc)]
        rank += 1
        if rank == nr:
            break
    return rank


def determinant(square):
    a = [[Q(z) for z in row] for row in square]
    n = len(a)
    out = Q(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col] != 0), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            out = -out
        z = a[col][col]
        out *= z
        for r in range(col + 1, n):
            if a[r][col] == 0:
                continue
            t = a[r][col] / z
            for k in range(col, n):
                a[r][k] -= t * a[col][k]
    return out


def primitive_left_null_6x5(rows):
    assert len(rows) == 6 and all(len(r) == 5 for r in rows)
    lam = []
    for i in range(6):
        minor = [rows[j] for j in range(6) if j != i]
        lam.append((Q(-1) if i % 2 else Q(1)) * determinant(minor))
    assert any(z != 0 for z in lam)
    for k in range(5):
        assert sum(lam[i] * rows[i][k] for i in range(6)) == 0
    lcm = 1
    for z in lam:
        lcm = math.lcm(lcm, z.denominator)
    ints = [int(z * lcm) for z in lam]
    g = 0
    for z in ints:
        g = math.gcd(g, abs(z))
    ints = [z // g for z in ints]
    if next(z for z in ints if z) < 0:
        ints = [-z for z in ints]
    return ints


def main():
    rows0 = ex.read_exact_rows()
    proposal = ex.numeric_faces(rows0)
    faces = ex.exactify_faces(rows0, proposal)
    ef = {}
    from collections import defaultdict

    dd = defaultdict(list)
    for fi, f in enumerate(faces):
        cyc = f["cycle"]
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            dd[tuple(sorted((a, b)))].append(fi)
    ef = dict(dd)
    q, dirs = build_jets(rows0)
    c, volume = exact_centroid(q, faces)

    def get_face(vertices):
        return next(f for f in faces if set(f["cycle"]) == set(vertices))

    base = get_face(range(17))
    f1 = get_face([228, 254, 255])
    f2 = get_face([228, 264, 246])
    f1c = dict(face_components(f1, q, c))
    f2c = dict(face_components(f2, q, c))
    basec = dict(face_components(base, q, c))

    walls = {
        "protect_base_edge_15_16": basec[(15, 16)],
        "protect_U8_via_246": vertex_support(8, 246, q, c),
        "kill_S_228_254_255_via_255_228": f1c[(255, 228)],
        "kill_S_228_264_246_via_246_228": f2c[(246, 228)],
        "kill_U228_via_254": vertex_support(228, 254, q, c),
        "kill_U231_via_229": vertex_support(231, 229, q, c),
        "kill_U246_via_231": vertex_support(246, 231, q, c),
    }
    # Record every component of the five current saddle edges; this lets later
    # branch solvers choose a wall without redoing exact differentiation.
    saddle_components = {}
    for edge in [(8, 246), (228, 254), (228, 255), (231, 247), (236, 237)]:
        saddle_components[f"{edge[0]}-{edge[1]}"] = {
            k: rec(v) for k, v in edge_components(edge, ef[edge], faces, q, c).items()
        }

    cancellation_names = [
        "kill_S_228_254_255_via_255_228",
        "kill_S_228_264_246_via_246_228",
        "kill_U228_via_254",
        "kill_U231_via_229",
        "kill_U246_via_231",
    ]
    grad5 = [walls[n].d for n in cancellation_names]
    # Add the strongest current saddle wall as a sixth independent demand.
    h8246 = edge_components((8, 246), ef[(8, 246)], faces, q, c)
    sixth_name, sixth = min(h8246.items(), key=lambda kv: kv[1].v)
    grad6 = grad5 + [sixth.d]
    six_names = cancellation_names + [f"H8-246:{sixth_name}"]
    six_jets = [walls[n] for n in cancellation_names] + [sixth]
    augmented6 = [list(z.d) + [z.v] for z in six_jets]
    ranks = {
        "five_selected_cancellation_gradients": matrix_rank(grad5),
        "six_selected_cancellation_gradients": matrix_rank(grad6),
        "six_selected_augmented_value_gradient_rows": matrix_rank(augmented6),
    }
    lam = primitive_left_null_6x5(grad6)
    lambda_gradient = [sum(Q(lam[i]) * grad6[i][k] for i in range(6)) for k in range(5)]
    lambda_value = sum(Q(lam[i]) * six_jets[i].v for i in range(6))
    assert lambda_gradient == [Q(0)] * 5
    assert lambda_value != 0
    lambda_value_log10 = (
        math.log10(abs(lambda_value.numerator)) - math.log10(lambda_value.denominator)
    )

    # A stronger inequality-form Farkas certificate in the explicit local
    # trust box |control_k| <= 10.  The six-row support was found numerically
    # once, but is reconstructed and checked here with exact Fractions:
    #   S(228,264,246) <= 0,
    #   U228 <= 0,
    #   U246 <= 0,
    #   protected U8 >= 0,
    #   r229 <= 10,
    #  -r255 <= 10.
    # Any solution of the full target system in the box would satisfy this
    # subset, so infeasibility of the subset is sufficient.
    zgrad = (Q(0),) * 5
    e_r229 = (Q(0), Q(1), Q(0), Q(0), Q(0))
    minus_e_r255 = (Q(0), Q(0), Q(0), Q(-1), Q(0))
    trust_rows = [
        (
            "kill_S_228_264_246_via_246_228 <= 0",
            walls["kill_S_228_264_246_via_246_228"].d,
            -walls["kill_S_228_264_246_via_246_228"].v,
        ),
        (
            "kill_U228_via_254 <= 0",
            walls["kill_U228_via_254"].d,
            -walls["kill_U228_via_254"].v,
        ),
        (
            "kill_U246_via_231 <= 0",
            walls["kill_U246_via_231"].d,
            -walls["kill_U246_via_231"].v,
        ),
        (
            "protect_U8_via_246 >= 0",
            tuple(-z for z in walls["protect_U8_via_246"].d),
            walls["protect_U8_via_246"].v,
        ),
        ("r229 <= 10", e_r229, Q(10)),
        ("-r255 <= 10", minus_e_r255, Q(10)),
    ]
    trust_A = [r[1] for r in trust_rows]
    trust_b = [r[2] for r in trust_rows]
    trust_lam = primitive_left_null_6x5(trust_A)
    if not all(z > 0 for z in trust_lam):
        trust_lam = [-z for z in trust_lam]
    assert all(z > 0 for z in trust_lam)
    trust_grad = [sum(Q(trust_lam[i]) * trust_A[i][k] for i in range(6)) for k in range(5)]
    trust_rhs = sum(Q(trust_lam[i]) * trust_b[i] for i in range(6))
    assert trust_grad == [Q(0)] * 5
    assert trust_rhs < 0
    trust_rhs_log10 = math.log10(abs(trust_rhs.numerator)) - math.log10(trust_rhs.denominator)

    out = {
        "version": 1,
        "type": "exact Fraction forward-jet certificate in the strict reconstructed shell cell",
        "scope": "local first-order rank only; no claim outside this explicit five-control actual cell",
        "controls": CONTROL_NAMES,
        "directions": {
            str(i): {"control": CONTROL_NAMES[k], "direction": [ex.qs(z) for z in d]}
            for i, (k, d) in dirs.items()
        },
        "volume": rec(volume),
        "centroid": [rec(z) for z in c],
        "walls": {k: rec(v) for k, v in walls.items()},
        "saddle_components": saddle_components,
        "selected_sixth_wall": f"H8-246:{sixth_name}",
        "ranks": ranks,
        "exact_affine_farkas_certificate": {
            "wall_order": six_names,
            "primitive_integer_left_null_vector": lam,
            "lambda_times_gradient_exact": [ex.qs(z) for z in lambda_gradient],
            "lambda_times_wall_values_exact": ex.qs(lambda_value),
            "lambda_times_wall_values_sign": 1 if lambda_value > 0 else -1,
            "lambda_times_wall_values_log10_abs": lambda_value_log10,
            "conclusion": (
                "No five-control increment solves all six selected first-order wall equations, "
                "because lambda^T G=0 but lambda^T value is nonzero."
            ),
        },
        "trust_box_10_inequality_farkas_certificate": {
            "system_form": "A x <= b",
            "scope": "first jet at reconstructed shell seed with |each of five controls| <= 10",
            "inequality_order": [r[0] for r in trust_rows],
            "A_exact": [[ex.qs(z) for z in r[1]] for r in trust_rows],
            "b_exact": [ex.qs(r[2]) for r in trust_rows],
            "primitive_positive_integer_multipliers": trust_lam,
            "lambda_times_A_exact": [ex.qs(z) for z in trust_grad],
            "lambda_times_b_exact": ex.qs(trust_rhs),
            "lambda_times_b_sign": -1,
            "lambda_times_b_log10_abs": trust_rhs_log10,
            "conclusion": (
                "Because lambda is strictly positive, lambda^T A=0 and lambda^T b<0, "
                "this necessary six-inequality subset is infeasible. Therefore the full "
                "linearized strict-target system is infeasible throughout the stated trust box."
            ),
        },
        "interpretation": (
            "The five designated face/vertex cancellation walls use all five local control directions. "
            "Adding the selected H(8,246) wall produces an exact affine Farkas inconsistency."
        ),
    }
    path = HERE / "rank5_exact_jacobian.json"
    path.write_text(json.dumps(out, indent=2) + "\n")
    print("EXACT_RANK5_JACOBIAN_PASS")
    print("ranks", ranks)
    print("sixth", out["selected_sixth_wall"])
    print("output", path)


if __name__ == "__main__":
    main()
