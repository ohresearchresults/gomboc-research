#!/usr/bin/env python3
"""Exact actual-cell escape along the normalized physical row255 actuator.

Starting from the reconstructed supporting shell, move only row 255 by

    q_255(t) = q_255(0) + t*(-1/2, -1, -1/4),   t <= 0.

Thus |t| is literally the largest moved coordinate.  The script builds the
ordered exact support-circuit atlas, rebuilds every named rational cell, and
derives the common algebraic mechanics wall at which S[228,254,255] and
H(228,255) disappear.  It also computes the exact far-cell residual rank and
a homogeneous Gordan certificate excluding simultaneous strict descent of
the residual block without rebirth of the killed stable face.

Floating hulls are proposal/locator machinery only.  Supporting planes,
mass, centroid, mechanics, chamber endpoints, circuit roots, polynomial
identities, ranks and the Gordan certificate are all checked with Fractions.
"""
from __future__ import annotations

import csv
import hashlib
import itertools
import json
import math
import sys
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
from scipy.optimize import brentq, linprog

import rank5_exact_jacobian as rj
import rank5_exact_reconstruction as ex
import rank5_sixth_control as sx


HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "rank5_circuit_escape.json"
CELL_DIR = HERE / "rank5_escape_cells"
REPORT = HERE / "RANK5_CIRCUIT_ESCAPE_REPORT.md"
VERIFIER = HERE / "verify_rank5_circuit_escape.py"
MANIFEST = HERE / "rank5_circuit_escape_artifacts.sha256"
sys.set_int_max_str_digits(0)

M = 6
CONTROL_NAMES = ["r228", "r229", "r254", "r255", "t231", "t246"]
D255 = (Q(-1, 2), Q(-1), Q(-1, 4))
FAR_T = Q(-3, 40)
MECH_LEFT = Q(-71, 1000)
MECH_RIGHT = Q(-7, 100)

CIRCUITS = [
    ("C1", (54, 69, 255, 256), (69, 256), (54, 255)),
    ("C2", (54, 255, 256, 257), (54, 256), (255, 257)),
    ("C3", (69, 253, 254, 255), (69, 254), (253, 255)),
    ("C4", (54, 255, 257, 258), (54, 257), (255, 258)),
    ("C5", (69, 252, 253, 255), (69, 253), (252, 255)),
]


def qs(z: Q) -> str:
    return ex.qs(Q(z))


def qv(text: str) -> Q:
    a, b = text.split("/")
    return Q(int(a), int(b))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def moved_rows(t: Q):
    rows = ex.read_exact_rows()
    rows[255] = ex.add(rows[255], ex.mul(D255, Q(t)))
    return rows


def forced_rails():
    return sx.forced_rails()


def edge_set(faces):
    edges = set()
    for face in faces:
        c = face["cycle"]
        edges.update(tuple(sorted((a, b))) for a, b in zip(c, c[1:] + c[:1]))
    return edges


def incidence(faces):
    out = defaultdict(list)
    for fi, face in enumerate(faces):
        c = face["cycle"]
        for a, b in zip(c, c[1:] + c[:1]):
            out[tuple(sorted((a, b)))].append(fi)
    assert all(len(v) == 2 for v in out.values())
    return dict(out)


def face_by_vertices(faces, vertices):
    target = set(vertices)
    ans = [f for f in faces if set(f["cycle"]) == target]
    assert len(ans) == 1, (vertices, len(ans))
    return ans[0]


def audit_rational_cell(name: str, t: Q, expected_f=None, expected_class=None):
    rows = moved_rows(t)
    faces = ex.exactify_faces(rows, ex.numeric_faces(rows))
    volume, centroid = ex.exact_mass(rows, faces)
    ef, active, fl, vl, el, stable, unstable, saddles = ex.exact_mechanics(
        rows, faces, centroid
    )
    fvec = [len(active), len(ef), len(faces)]
    klass = [len(stable), len(unstable), len(saddles)]
    base = any(set(faces[i]["cycle"]) == set(range(17)) for i in stable)
    rails = forced_rails()
    missing = sorted(rails - set(ef))
    if expected_f is not None:
        assert fvec == expected_f, (name, fvec)
    if expected_class is not None:
        assert klass == expected_class, (name, klass)
    assert len(active) == 61 and base and 8 in unstable and not missing

    CELL_DIR.mkdir(exist_ok=True)
    path = CELL_DIR / f"{name}.csv"
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source_id", "x_exact", "y_exact", "z_exact", "x", "y", "z"])
        for row, point in sorted(rows.items()):
            w.writerow([row, *(qs(z) for z in point), *(format(float(z), ".17g") for z in point)])

    return {
        "name": name,
        "parameter_exact": qs(t),
        "parameter_decimal": float(t),
        "max_abs_coordinate_displacement_exact": qs(abs(t)),
        "f_vector": fvec,
        "class": klass,
        "active_count": len(active),
        "all_61_active": len(active) == 61,
        "base_stable": base,
        "U8_unstable": 8 in unstable,
        "forced_rails_present": len(rails) - len(missing),
        "all_37_forced_rails_present": not missing,
        "stable_faces": [faces[i]["cycle"] for i in stable],
        "unstable_vertices": unstable,
        "saddle_edges": [list(e) for e in saddles],
        "volume_exact": qs(volume),
        "centroid_exact": [qs(z) for z in centroid],
        "csv": str(path.relative_to(HERE)),
        "csv_sha256": sha256(path),
        "faces": faces,
        "incidence": ef,
        "face_ledger": fl,
        "vertex_ledger": vl,
        "edge_ledger": el,
    }


def det4(t: Q, ids):
    rows = moved_rows(t)
    a, b, c, d = (rows[i] for i in ids)
    return ex.det(ex.sub(b, a), ex.sub(c, a), ex.sub(d, a))


def circuit_root(ids):
    a = det4(Q(0), ids)
    b = det4(Q(1), ids) - a
    assert b != 0
    root = -a / b
    assert det4(root, ids) == 0
    return root


def topology_chamber(sample_t: Q):
    """Exact maximal interval on which every sampled support plane persists."""
    rows = moved_rows(sample_t)
    faces = ex.exactify_faces(rows, ex.numeric_faces(rows))
    rows0, rows1 = moved_rows(Q(0)), moved_rows(Q(1))
    lower = None
    upper = None
    lower_witnesses = []
    upper_witnesses = []
    all_ids = sorted(rows)
    inequalities = 0
    for face in faces:
        cycle = face["cycle"]
        a = cycle[0]
        tri = None
        for j in range(1, len(cycle) - 1):
            for k in range(j + 1, len(cycle)):
                if ex.cross(ex.sub(rows[cycle[j]], rows[a]), ex.sub(rows[cycle[k]], rows[a])) != ex.ZERO:
                    tri = (a, cycle[j], cycle[k])
                    break
            if tri:
                break
        assert tri is not None
        aa, bb, cc = tri

        def slack(rr, i):
            return ex.det(ex.sub(rr[bb], rr[aa]), ex.sub(rr[cc], rr[aa]), ex.sub(rr[i], rr[aa]))

        outside = [slack(rows, i) for i in all_ids if i not in cycle]
        assert all(z <= 0 for z in outside) or all(z >= 0 for z in outside)
        orient = Q(1) if all(z <= 0 for z in outside) else Q(-1)
        for i in all_ids:
            if i in cycle:
                continue
            a0 = orient * slack(rows0, i)
            slope = orient * slack(rows1, i) - a0
            assert a0 + slope * sample_t < 0
            inequalities += 1
            if slope > 0:
                root = -a0 / slope
                witness = sorted(set(cycle) | {i})
                if upper is None or root < upper:
                    upper, upper_witnesses = root, [witness]
                elif root == upper and witness not in upper_witnesses:
                    upper_witnesses.append(witness)
            elif slope < 0:
                root = -a0 / slope
                witness = sorted(set(cycle) | {i})
                if lower is None or root > lower:
                    lower, lower_witnesses = root, [witness]
                elif root == lower and witness not in lower_witnesses:
                    lower_witnesses.append(witness)
    assert lower is not None and upper is not None and lower < sample_t < upper
    return {
        "sample_exact": qs(sample_t),
        "lower_exact": qs(lower),
        "upper_exact": qs(upper),
        "lower_decimal": float(lower),
        "upper_decimal": float(upper),
        "lower_circuit_witnesses": lower_witnesses,
        "upper_circuit_witnesses": upper_witnesses,
        "strict_support_inequalities_checked": inequalities,
    }


# ---------- exact rational functions in one polynomial variable ----------


def ptrim(a):
    a = [Q(z) for z in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def padd(a, b):
    out = [Q(0)] * max(len(a), len(b))
    for i, z in enumerate(a):
        out[i] += z
    for i, z in enumerate(b):
        out[i] += z
    return ptrim(out)


def pneg(a):
    return [-z for z in a]


def psub(a, b):
    return padd(a, pneg(b))


def pmul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, z in enumerate(a):
        for j, w in enumerate(b):
            out[i + j] += z * w
    return ptrim(out)


def pscale(a, z):
    return ptrim([Q(z) * x for x in a])


def pdivmod(a, b):
    a, b = ptrim(a), ptrim(b)
    assert b != [Q(0)]
    if len(a) < len(b):
        return [Q(0)], a
    q = [Q(0)] * (len(a) - len(b) + 1)
    r = list(a)
    while r != [Q(0)] and len(r) >= len(b):
        k = len(r) - len(b)
        z = r[-1] / b[-1]
        q[k] += z
        r = psub(r, [Q(0)] * k + pscale(b, z))
    return ptrim(q), ptrim(r)


def pexact_div(a, b):
    q, r = pdivmod(a, b)
    assert r == [Q(0)]
    return q


def pgcd(a, b):
    a, b = ptrim(a), ptrim(b)
    while b != [Q(0)]:
        _, r = pdivmod(a, b)
        a, b = b, r
    if a == [Q(0)]:
        return a
    return pscale(a, 1 / a[-1])


def peval(a, x):
    out = Q(0)
    for z in reversed(a):
        out = out * x + z
    return out


def pderivative(a):
    return ptrim([Q(i) * a[i] for i in range(1, len(a))] or [Q(0)])


def primitive_integer_polynomial(a):
    a = ptrim(a)
    lcm = 1
    for z in a:
        lcm = math.lcm(lcm, z.denominator)
    ints = [int(z * lcm) for z in a]
    g = 0
    for z in ints:
        g = math.gcd(g, abs(z))
    ints = [z // g for z in ints]
    if ints[-1] < 0:
        ints = [-z for z in ints]
    return ints


def sturm_sequence(p):
    seq = [ptrim(p), pderivative(p)]
    while seq[-1] != [Q(0)]:
        _, r = pdivmod(seq[-2], seq[-1])
        if r == [Q(0)]:
            break
        seq.append(pneg(r))
    return seq


def sign_variations(values):
    signs = [1 if z > 0 else -1 for z in values if z != 0]
    return sum(signs[i] != signs[i - 1] for i in range(1, len(signs)))


def sturm_root_count(p, left, right):
    assert left < right and peval(p, left) != 0 and peval(p, right) != 0
    seq = sturm_sequence(p)
    return sign_variations([peval(z, left) for z in seq]) - sign_variations([peval(z, right) for z in seq]), seq


@dataclass(frozen=True)
class RP:
    n: tuple[Q, ...]
    d: tuple[Q, ...]

    @staticmethod
    def c(z):
        if isinstance(z, RP):
            return z
        return RP((Q(z),), (Q(1),))

    @staticmethod
    def make(n, d):
        n, d = ptrim(n), ptrim(d)
        assert d != [Q(0)]
        if n == [Q(0)]:
            return RP((Q(0),), (Q(1),))
        g = pgcd(n, d)
        if len(g) > 1 or g[0] != 1:
            n, d = pexact_div(n, g), pexact_div(d, g)
        if d[-1] < 0:
            n, d = pneg(n), pneg(d)
        return RP(tuple(n), tuple(d))

    def __add__(self, other):
        o = RP.c(other)
        return RP.make(padd(pmul(self.n, o.d), pmul(o.n, self.d)), pmul(self.d, o.d))

    __radd__ = __add__

    def __neg__(self):
        return RP(tuple(pneg(self.n)), self.d)

    def __sub__(self, other):
        return self + (-RP.c(other))

    def __rsub__(self, other):
        return RP.c(other) - self

    def __mul__(self, other):
        o = RP.c(other)
        return RP.make(pmul(self.n, o.n), pmul(self.d, o.d))

    __rmul__ = __mul__

    def __truediv__(self, other):
        o = RP.c(other)
        return RP.make(pmul(self.n, o.d), pmul(self.d, o.n))

    def __rtruediv__(self, other):
        return RP.c(other) / self

    def at(self, t):
        return peval(self.n, t) / peval(self.d, t)


def vadd(a, b):
    return tuple(a[k] + b[k] for k in range(3))


def vsub(a, b):
    return tuple(a[k] - b[k] for k in range(3))


def vmul(a, t):
    return tuple(a[k] * t for k in range(3))


def vdot(a, b):
    return sum((a[k] * b[k] for k in range(3)), RP.c(0))


def vcross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def symbolic_rows():
    rows = ex.read_exact_rows()
    out = {i: tuple(RP.c(z) for z in p) for i, p in rows.items()}
    out[255] = tuple(RP.make([rows[255][k], D255[k]], [Q(1)]) for k in range(3))
    return out


def symbolic_face_normal(face, q, t_ref=FAR_T):
    c = face["cycle"]
    a = q[c[0]]
    far = moved_rows(t_ref)
    for j in range(1, len(c) - 1):
        for k in range(j + 1, len(c)):
            if ex.cross(ex.sub(far[c[j]], far[c[0]]), ex.sub(far[c[k]], far[c[0]])) != ex.ZERO:
                n = vcross(vsub(q[c[j]], a), vsub(q[c[k]], a))
                nv = tuple(z.at(t_ref) for z in n)
                if ex.dot(nv, face["n"]) < 0:
                    n = tuple(-z for z in n)
                return n
    raise AssertionError("collinear symbolic face")


def symbolic_centroid(q, faces):
    d6 = RP.c(0)
    m24 = [RP.c(0), RP.c(0), RP.c(0)]
    for f in faces:
        c = f["cycle"]
        for j in range(1, len(c) - 1):
            a, b, z = (q[i] for i in (c[0], c[j], c[j + 1]))
            dd = vdot(a, vcross(b, z))
            d6 += dd
            for k in range(3):
                m24[k] += dd * (a[k] + b[k] + z[k])
    return tuple(m24[k] / (4 * d6) for k in range(3)), d6 / 6


def symbolic_face_components(face, q, centroid, t_ref=FAR_T):
    cyc = face["cycle"]
    n = symbolic_face_normal(face, q, t_ref)
    h = vdot(n, vsub(q[cyc[0]], centroid))
    foot = vmul(n, h / vdot(n, n))
    x = {i: vsub(q[i], centroid) for i in cyc}
    ref = tuple(sum((x[i][k] for i in cyc), RP.c(0)) / len(cyc) for k in range(3))
    out = {}
    for a, b in zip(cyc, cyc[1:] + cyc[:1]):
        e = vsub(x[b], x[a])
        z = vdot(vcross(e, vsub(foot, x[a])), n)
        rz = vdot(vcross(e, vsub(ref, x[a])), n).at(t_ref)
        if rz < 0:
            z = -z
        out[(a, b)] = z
    return out


def symbolic_vertex_support(i, j, q, centroid):
    xi, xj = vsub(q[i], centroid), vsub(q[j], centroid)
    return -vdot(xi, vsub(xj, xi))


def symbolic_edge_components(edge, inc, faces, q, centroid):
    i, j = edge
    xi, xj = vsub(q[i], centroid), vsub(q[j], centroid)
    d = vsub(xj, xi)
    t = -vdot(xi, d) / vdot(d, d)
    p = vadd(xi, vmul(d, t))
    n1, n2 = (symbolic_face_normal(faces[k], q) for k in inc)
    aa, bb, cc = vdot(n1, n1), vdot(n1, n2), vdot(n2, n2)
    r1, r2 = vdot(p, n1), vdot(p, n2)
    den = aa * cc - bb * bb
    b1 = (r1 * cc - r2 * bb) / den
    b2 = (r2 * aa - r1 * bb) / den
    return {"t": t, "one_minus_t": 1 - t, "beta1": b1, "beta2": b2}


def shared_mechanics_polynomial(far_faces):
    q = symbolic_rows()
    centroid, _ = symbolic_centroid(q, far_faces)
    sface = face_by_vertices(far_faces, [228, 254, 255])
    scomp = symbolic_face_components(sface, q, centroid)[(255, 228)]
    inc = incidence(far_faces)
    hcomp = symbolic_edge_components((228, 255), inc[(228, 255)], far_faces, q, centroid)["beta2"]
    common = pgcd(scomp.n, hcomp.n)
    primitive = primitive_integer_polynomial(common)
    assert len(primitive) == 4
    p = [Q(z) for z in primitive]
    roots, sturm = sturm_root_count(p, MECH_LEFT, MECH_RIGHT)
    assert roots == 1 and peval(p, MECH_LEFT) * peval(p, MECH_RIGHT) < 0
    approx = brentq(lambda x: float(peval(p, Q(format(x, ".17g")))), float(MECH_LEFT), float(MECH_RIGHT), xtol=1e-15)
    return {
        "stable_face_component": scomp,
        "saddle_beta2_component": hcomp,
        "common_monic": common,
        "primitive": primitive,
        "sturm": sturm,
        "root_decimal": approx,
    }, q, centroid


def normalized_control_directions(rows):
    raw = sx.control_directions(ex.read_exact_rows())
    out = {}
    for row, (control, direction) in raw.items():
        scale = max(abs(z) for z in direction)
        out[row] = (control, tuple(z / scale for z in direction))
    assert out[255][1] == D255
    return out


def far_feature_jets(rows, faces):
    directions = normalized_control_directions(rows)
    rj.M = M
    q = {
        row: rj.qj(point, *(directions[row] if row in directions else (None, None)))
        for row, point in rows.items()
    }
    c, _ = rj.exact_centroid(q, faces)
    inc = incidence(faces)

    def fc(vertices, edge):
        z = dict(rj.face_components(face_by_vertices(faces, vertices), q, c))
        return z[edge] if edge in z else z[edge[::-1]]

    def ec(edge, component):
        e = tuple(sorted(edge))
        return rj.edge_components(e, inc[e], faces, q, c)[component]

    features = [
        ("death_S_228_264_246_via_246_228", fc([228, 264, 246], (246, 228)), "death"),
        ("death_U228_via_251", rj.vertex_support(228, 251, q, c), "death"),
        ("death_U231_via_232", rj.vertex_support(231, 232, q, c), "death"),
        ("death_U246_via_245", rj.vertex_support(246, 245, q, c), "death"),
        ("death_H8_246_via_t", ec((8, 246), "t"), "death"),
        ("death_H228_254_via_beta2", ec((228, 254), "beta2"), "death"),
        ("death_H231_247_via_beta1", ec((231, 247), "beta1"), "death"),
        ("death_H236_237_via_beta1", ec((236, 237), "beta1"), "death"),
        ("guard_killed_S_228_254_255_no_rebirth", fc([228, 254, 255], (255, 228)), "guard"),
        ("guard_killed_H228_255_no_rebirth", ec((228, 255), "beta2"), "guard"),
    ]
    assert all(z.v > 0 for _, z, _ in features[:8])
    assert all(z.v < 0 for _, z, _ in features[8:])
    return features, directions


def primitive_row(row):
    lcm = 1
    for z in row:
        lcm = math.lcm(lcm, z.denominator)
    ints = [int(z * lcm) for z in row]
    g = 0
    for z in ints:
        g = math.gcd(g, abs(z))
    ints = [z // g for z in ints]
    scale = Q(g, lcm)
    assert all(row[k] == scale * ints[k] for k in range(len(row)))
    return ints, scale


def exact_gordan(features):
    primitive = []
    scales = []
    for _, jet, _ in features:
        row, scale = primitive_row(jet.d)
        primitive.append(row)
        scales.append(scale)
    candidates = []
    for subset in itertools.combinations(range(len(features)), M + 1):
        matrix = [primitive[i] for i in subset]
        if rj.matrix_rank(matrix) != M:
            continue
        lam = []
        for i in range(M + 1):
            minor = [matrix[j] for j in range(M + 1) if j != i]
            lam.append((Q(-1) if i % 2 else Q(1)) * rj.determinant(minor))
        if all(z < 0 for z in lam):
            lam = [-z for z in lam]
        if not all(z > 0 for z in lam):
            continue
        ints = [int(z) for z in lam]
        g = 0
        for z in ints:
            g = math.gcd(g, abs(z))
        ints = [z // g for z in ints]
        if not any(i < 8 for i in subset):
            continue
        score = sum(len(str(abs(z))) for z in ints)
        candidates.append((score, subset, ints))
    assert candidates
    _, subset, multipliers = min(candidates)
    matrix = [primitive[i] for i in subset]
    stationarity = [sum(multipliers[j] * matrix[j][k] for j in range(M + 1)) for k in range(M)]
    assert stationarity == [0] * M and all(z > 0 for z in multipliers)
    assert any(features[i][2] == "death" for i in subset)
    return {
        "theorem": (
            "No direction can make all eight residual death derivatives strictly negative "
            "while both killed-wall derivatives are nonpositive.  The displayed positive "
            "combination already uses a necessary subset and sums identically to zero."
        ),
        "full_system_row_count": len(features),
        "full_system_rank_exact": rj.matrix_rank([z.d for _, z, _ in features]),
        "eight_death_gradient_rank_exact": rj.matrix_rank([z.d for _, z, _ in features[:8]]),
        "support_indices": list(subset),
        "support": [
            {
                "name": features[index][0],
                "kind": features[index][2],
                "primitive_gradient": primitive[index],
                "positive_scale_from_primitive_to_exact_gradient": qs(scales[index]),
                "positive_integer_multiplier": str(multipliers[j]),
            }
            for j, index in enumerate(subset)
        ],
        "all_multipliers_strictly_positive": True,
        "exact_stationarity_six_columns": stationarity,
        "exact_stationarity_zero": True,
        "contains_strict_death_row": True,
        "candidate_positive_circuits_found": len(candidates),
    }


def numeric_death_cone(features, columns):
    """Locator only: maximize uniform normalized death decrease."""
    a = np.asarray([[float(z) for z in jet.d] for _, jet, _ in features[:8]])[:, columns]
    scale = np.max(np.abs(a), axis=1)
    an = a / scale[:, None]
    n = len(columns)
    # an*c + rho <= 0, |c|<=1, maximize rho
    cobj = np.r_[np.zeros(n), -1.0]
    aub = np.c_[an, np.ones(len(an))]
    solve = linprog(cobj, A_ub=aub, b_ub=np.zeros(len(an)), bounds=[(-1, 1)] * n + [(None, None)], method="highs")
    assert solve.success
    return {
        "controls": [CONTROL_NAMES[i] for i in columns],
        "uniform_normalized_decrease_locator": float(solve.x[-1]),
        "direction_locator": [float(z) for z in solve.x[:-1]],
        "authoritative": False,
    }


def mechanics_guard_root_audit(far_faces, q, symbolic_centroid, interval_left, interval_right):
    """Prove base and U8 have no zero in the complete C3--C4 chamber."""
    base = face_by_vertices(far_faces, list(range(17)))
    base_components = symbolic_face_components(base, q, symbolic_centroid)
    inc = incidence(far_faces)
    u8_neighbors = sorted({b if a == 8 else a for a, b in inc if 8 in (a, b)})
    checks = []
    for edge, z in base_components.items():
        count, _ = sturm_root_count(list(z.n), interval_left, interval_right)
        assert count == 0 and z.at(FAR_T) > 0
        checks.append({"guard": f"base_edge_{edge[0]}_{edge[1]}", "root_count": count})
    for j in u8_neighbors:
        z = symbolic_vertex_support(8, j, q, symbolic_centroid)
        count, _ = sturm_root_count(list(z.n), interval_left, interval_right)
        assert count == 0 and z.at(FAR_T) > 0
        checks.append({"guard": f"U8_via_{j}", "root_count": count})
    return {
        "interval_exact": [qs(interval_left), qs(interval_right)],
        "base_and_U8_component_count": len(checks),
        "every_numerator_has_zero_roots_in_open_chamber": True,
        "all_components_positive_at_far_exact": True,
        "checks": checks,
    }


def strip_cell(cell):
    return {k: v for k, v in cell.items() if k not in {"faces", "incidence", "face_ledger", "vertex_ledger", "edge_ledger"}}


def main():
    CELL_DIR.mkdir(exist_ok=True)

    # Literal exact circuit roots and full supporting-plane chamber proof.
    roots = {name: circuit_root(ids) for name, ids, _, _ in CIRCUITS}
    assert roots["C5"] < roots["C4"] < FAR_T < MECH_LEFT < MECH_RIGHT < roots["C3"] < roots["C2"] < roots["C1"] < 0
    samples = [Q(0), Q(-1, 100), Q(-7, 200), Q(-1, 20), Q(-1, 10)]
    chambers = [topology_chamber(t) for t in samples]
    expected_bounds = [
        (roots["C1"], None),
        (roots["C2"], roots["C1"]),
        (roots["C3"], roots["C2"]),
        (roots["C4"], roots["C3"]),
        (roots["C5"], roots["C4"]),
    ]
    for chamber, (lo, hi) in zip(chambers, expected_bounds):
        assert qv(chamber["lower_exact"]) == lo
        if hi is not None:
            assert qv(chamber["upper_exact"]) == hi

    source_edges = edge_set(ex.exactify_faces(moved_rows(0), ex.numeric_faces(moved_rows(0))))
    circuit_records = []
    circuit_brackets = {
        "C1": (Q(-1, 100), Q(0)),
        "C2": (Q(-7, 200), Q(-1, 100)),
        "C3": (Q(-1, 20), Q(-7, 200)),
        "C4": (Q(-1, 10), FAR_T),
        "C5": (Q(-7, 50), Q(-1, 10)),
    }
    for name, ids, removed, added in CIRCUITS:
        t = roots[name]
        before_t = (t + (Q(0) if name == "C1" else roots[f"C{int(name[1:]) - 1}"])) / 2
        if name == "C5":
            # only C1..C4 are crossed by the delivered nearby path; C5 is the
            # exact next chamber endpoint after t=-1/10.
            before_t = Q(-1, 10)
        after_t = (t + (roots.get(f"C{int(name[1:]) + 1}", t - Q(1, 100)))) / 2
        wall = audit_rational_cell(f"{name.lower()}_wall", t, [61, 149, 90], [3, 4, 5] if name in {"C1", "C2", "C3"} else [2, 4, 4])
        eb = edge_set(ex.exactify_faces(moved_rows(before_t), ex.numeric_faces(moved_rows(before_t))))
        ea = edge_set(ex.exactify_faces(moved_rows(after_t), ex.numeric_faces(moved_rows(after_t))))
        assert tuple(sorted(removed)) in eb - ea
        assert tuple(sorted(added)) in ea - eb
        bracket_left, bracket_right = circuit_brackets[name]
        assert bracket_left < t < bracket_right
        bracket_values = [det4(bracket_left, ids), det4(bracket_right, ids)]
        assert bracket_values[0] * bracket_values[1] < 0
        circuit_records.append({
            "name": name,
            "vertices": list(ids),
            "parameter_exact": qs(t),
            "parameter_decimal": float(t),
            "determinant_zero_exact": True,
            "affine_determinant_unique_root": True,
            "isolating_bracket_exact": [qs(bracket_left), qs(bracket_right)],
            "bracket_determinant_signs": [1 if z > 0 else -1 for z in bracket_values],
            "removed_edge": list(removed),
            "added_edge": list(added),
            "wall_cell": strip_cell(wall),
            "crossed_in_delivered_path": name in {"C1", "C2", "C3", "C4"},
        })

    cells_spec = [
        ("source", Q(0), [61, 150, 91], [3, 4, 5]),
        ("c1_far", Q(-1, 100), [61, 150, 91], [3, 4, 5]),
        ("c2_far", Q(-7, 200), [61, 150, 91], [3, 4, 5]),
        ("c3_far", Q(-1, 20), [61, 150, 91], [3, 4, 5]),
        ("mechanics_pre", MECH_RIGHT, [61, 150, 91], [3, 4, 5]),
        ("mechanics_far", FAR_T, [61, 150, 91], [2, 4, 4]),
        ("c4_far", Q(-1, 10), [61, 150, 91], [2, 4, 4]),
    ]
    cells = [audit_rational_cell(*spec) for spec in cells_spec]
    far_cell = next(z for z in cells if z["name"] == "mechanics_far")
    far_rows = moved_rows(FAR_T)
    far_faces = far_cell["faces"]

    mechanics, symbolic_q, symbolic_centroid = shared_mechanics_polynomial(far_faces)
    p = [Q(z) for z in mechanics["primitive"]]
    assert mechanics["stable_face_component"].at(MECH_RIGHT) > 0
    assert mechanics["stable_face_component"].at(FAR_T) < 0
    assert mechanics["saddle_beta2_component"].at(MECH_RIGHT) > 0
    assert mechanics["saddle_beta2_component"].at(FAR_T) < 0

    # Write an explicitly labelled algebraic-wall locator CSV.  Its topology
    # is certified by the exact C3--C4 chamber, not by rounded coordinates.
    wall_approx = mechanics["root_decimal"]
    wall_path = CELL_DIR / "mechanics_wall_algebraic_locator.csv"
    rows_approx = moved_rows(Q(format(wall_approx, ".17g")))
    with wall_path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source_id", "x", "y", "z"])
        for row, point in sorted(rows_approx.items()):
            w.writerow([row, *(format(float(z), ".17g") for z in point)])

    c3c4_guard = mechanics_guard_root_audit(
        far_faces, symbolic_q, symbolic_centroid, roots["C4"], roots["C3"]
    )

    features, directions = far_feature_jets(far_rows, far_faces)
    gordan = exact_gordan(features)
    feature_records = [
        {
            "name": name,
            "kind": kind,
            "value_exact": qs(jet.v),
            "value_decimal": float(jet.v),
            "gradient_exact": [qs(z) for z in jet.d],
            "gradient_decimal": [float(z) for z in jet.d],
        }
        for name, jet, kind in features
    ]

    out = {
        "version": 1,
        "type": "exact ordered actual-cell escape and far-cell Gordan cone",
        "source": {
            "seed": "rank5_reconstruction.json",
            "f_vector": [61, 150, 91],
            "class": [3, 4, 5],
            "path": "q255(t)=q255(0)+t*(-1/2,-1,-1/4), t decreases",
            "largest_coordinate_displacement_equals_abs_t": True,
        },
        "ordered_topology_circuit_atlas": circuit_records,
        "ordered_passage": [
            {"event": "C1", "pre": "source", "wall": "c1_wall", "far": "c1_far"},
            {"event": "C2", "pre": "c1_far", "wall": "c2_wall", "far": "c2_far"},
            {"event": "C3", "pre": "c2_far", "wall": "c3_wall", "far": "c3_far"},
            {
                "event": "shared_S_H_mechanics_wall",
                "pre": "mechanics_pre",
                "wall": "mechanics_wall_algebraic_locator",
                "far": "mechanics_far",
            },
            {"event": "C4", "pre": "mechanics_far", "wall": "c4_wall", "far": "c4_far"},
        ],
        "exact_support_chambers": chambers,
        "rational_open_cells": [strip_cell(z) for z in cells],
        "mechanics_wall": {
            "coupled_components": [
                "S[228,254,255] face component via directed edge 255->228",
                "H(228,255) beta2",
            ],
            "common_primitive_polynomial_coefficients_ascending": [str(z) for z in mechanics["primitive"]],
            "polynomial_degree": 3,
            "isolating_interval_exact": [qs(MECH_LEFT), qs(MECH_RIGHT)],
            "endpoint_signs": [int(math.copysign(1, peval(p, MECH_LEFT))), int(math.copysign(1, peval(p, MECH_RIGHT)))],
            "sturm_sequence_degrees": [len(z) - 1 for z in mechanics["sturm"]],
            "sturm_root_count_in_interval": 1,
            "root_decimal_locator": wall_approx,
            "stable_component_numerator_divisible_by_common_exact": pdivmod(list(mechanics["stable_face_component"].n), list(mechanics["common_monic"]))[1] == [Q(0)],
            "saddle_component_numerator_divisible_by_common_exact": pdivmod(list(mechanics["saddle_beta2_component"].n), list(mechanics["common_monic"]))[1] == [Q(0)],
            "algebraic_wall_locator_csv": str(wall_path.relative_to(HERE)),
            "algebraic_wall_locator_csv_sha256": sha256(wall_path),
            "class_before": [3, 4, 5],
            "class_after": [2, 4, 4],
            "all61_base_U8_rails_to_wall": c3c4_guard,
        },
        "far_exact_cell": {
            "parameter_exact": qs(FAR_T),
            "f_vector": far_cell["f_vector"],
            "class": far_cell["class"],
            "base_stable": far_cell["base_stable"],
            "U8_unstable": far_cell["U8_unstable"],
            "all_61_active": far_cell["all_61_active"],
            "forced_rails_present": far_cell["forced_rails_present"],
            "killed_without_rebirth": ["S[228,254,255]", "H(228,255)"],
            "controls": {
                str(row): {
                    "name": CONTROL_NAMES[control],
                    "normalized_direction_exact": [qs(z) for z in direction],
                }
                for row, (control, direction) in directions.items()
            },
            "residual_feature_block": feature_records,
            "exact_rank": {
                "remaining_original_five": rj.matrix_rank([z.d for _, z, _ in features[:5]]),
                "all_eight_residual_deaths": rj.matrix_rank([z.d for _, z, _ in features[:8]]),
                "with_two_no_rebirth_guards": rj.matrix_rank([z.d for _, z, _ in features]),
            },
            "numerical_sparse_death_cones_locator_only": [
                numeric_death_cone(features, [2, 4, 5]),
                numeric_death_cone(features, [2, 5]),
            ],
            "exact_no_rebirth_gordan_certificate": gordan,
        },
        "next_event": {
            "name": "C4",
            "type": "support-circuit flip",
            "parameter_exact": qs(roots["C4"]),
            "parameter_decimal": float(roots["C4"]),
            "circuit": [54, 255, 257, 258],
            "removed_edge": [54, 257],
            "added_edge": [255, 258],
            "fresh_cell_after_exact": "c4_far at t=-1/10",
            "guards_after": {"all61": True, "base": True, "U8": True, "rails37": True},
            "class_after": [2, 4, 4],
            "following_topology_endpoint_C5_exact": qs(roots["C5"]),
        },
        "artifact_hashes": {
            z["csv"]: z["csv_sha256"] for z in map(strip_cell, cells)
        } | {
            record["wall_cell"]["csv"]: record["wall_cell"]["csv_sha256"] for record in circuit_records
        } | {
            str(wall_path.relative_to(HERE)): sha256(wall_path)
        },
        "verdict": "EXACT_SMALL_PHYSICAL_ACTUAL_CELL_ESCAPE_345_TO_244_WITH_GUARDED_CONTINUATION",
        "conclusion": (
            "A sequence whose largest total moved coordinate is only 3/40 crosses three exact "
            "support circuits and then one isolated common mechanics wall, preserving all 61 active "
            "rows, the base, U8 and all 37 rails.  The far exact cell has class (2,4,4).  Its full "
            "residual death block has rank six, but an exact positive Gordan circuit proves that "
            "strict simultaneous residual descent cannot keep the killed stable face from rebirth. "
            "Continuing the same physical axis safely crosses C4 at displacement about 0.09113."
        ),
    }
    OUTPUT.write_text(json.dumps(out, indent=2) + "\n")
    package = [Path(__file__), OUTPUT, REPORT, VERIFIER] + sorted(CELL_DIR.glob("*.csv"))
    assert all(path.is_file() for path in package)
    MANIFEST.write_text(
        "".join(f"{sha256(path)}  {path.relative_to(HERE)}\n" for path in package)
    )
    print(out["verdict"])
    print("C1,C2,C3,M,C4", *(float(roots[f"C{i}"]) for i in range(1, 4)), wall_approx, float(roots["C4"]))
    print("far", far_cell["f_vector"], far_cell["class"], far_cell["base_stable"], far_cell["U8_unstable"], far_cell["forced_rails_present"])
    print("far ranks", out["far_exact_cell"]["exact_rank"])
    print("Gordan support", gordan["support_indices"])
    print("output", OUTPUT)
    print("manifest", MANIFEST)


if __name__ == "__main__":
    main()
