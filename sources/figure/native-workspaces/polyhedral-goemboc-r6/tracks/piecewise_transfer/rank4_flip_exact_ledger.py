#!/usr/bin/env python3
"""Exact first-jet ledger for the row54 compensating four-wall cell.

The finite decimal coordinates in ``row54_multiwall_flip.csv`` are read as
Fractions.  The supplied maximal-face cycles are treated as a fixed
triangulated boundary ledger.  The 44-coordinate chart is a rationalized
first jet of the chart used by ``row54_guarded_escape.py``:

* three projective pole coordinates and five trace-free symmetric linear
  coordinates, after exact arithmetic-mean centering and a recorded rational
  approximation of the RMS scale;
* two exactly in-base-plane directions at each of the 18 base rows.  Unit and
  local-edge scales are rationalized, but the directions themselves are
  obtained from exact cross products, hence remain exactly in the base plane.

Every mechanical entry below is a rational zero-equivalent primitive.  Its
zero set and sign agree locally with the corresponding normalized mechanics
component, but its magnitude is deliberately free of square roots.  The four
death families are

    S[198,243,244] (3 components), U2 (3 neighbours),
    H[4,5] (4 components), H[12,13] (4 components),

giving 3*3*4*4 = 144 named branches.  The two ultrathin support guards of the
quad {2,3,88,242} reduce identically to one oriented tetrahedral volume.

This file constructs an exact primitive/Jacobian ledger.  It does not claim a
nonlinear path, nor does it replace a guarded LP over the other cell walls.
"""
from __future__ import annotations

import csv
import hashlib
import itertools
import json
import math
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ATLAS = ROOT / "tracks" / "circuit_atlas"
SOURCE = ATLAS / "row54_multiwall_flip.csv"
FACES_SOURCE = ATLAS / "row54_multiwall_flip_faces.json"
OUTPUT = HERE / "rank4_flip_exact_ledger.json"

D = 44
BASE_CYCLE = [0, 54] + list(range(1, 17))


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
        return J(self.v + z.v, tuple(a + b for a, b in zip(self.d, z.d)))

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
            tuple(a * z.v + self.v * b for a, b in zip(self.d, z.d)),
        )

    __rmul__ = __mul__

    def inv(self):
        if self.v == 0:
            raise ZeroDivisionError
        return J(1 / self.v, tuple(-z / (self.v * self.v) for z in self.d))

    def __truediv__(self, other):
        return self * J.c(other).inv()

    def __rtruediv__(self, other):
        return J.c(other) / self


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def mul(a, z):
    return tuple(x * z for x in a)


def dot(a, b):
    zero = J.c(0) if isinstance(a[0], J) or isinstance(b[0], J) else Q(0)
    return sum((x * y for x, y in zip(a, b)), zero)


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def det3(a, b, c):
    return dot(a, cross(b, c))


def values(a):
    return tuple(z.v if isinstance(z, J) else z for z in a)


def qs(z: Q):
    return str(z.numerator) if z.denominator == 1 else f"{z.numerator}/{z.denominator}"


def q17(x: float):
    """Recorded finite-decimal rationalization used only for chart scales."""
    return Q(format(float(x), ".17g"))


def qlog10(z: Q):
    if z == 0:
        return -math.inf
    return math.log10(abs(z.numerator)) - math.log10(z.denominator)


def read_input():
    rows = {}
    with SOURCE.open() as f:
        for row in csv.DictReader(f):
            rows[int(row["source_id"])] = tuple(Q(row[k]) for k in ("x", "y", "z"))
    faces = json.loads(FACES_SOURCE.read_text())
    return rows, faces


def norm_float(v):
    return math.sqrt(sum(float(z) ** 2 for z in v))


def projective_velocity(index, z):
    x, y, w = z
    if index == 0:
        return (-x * x, -y * x, -w * x)
    if index == 1:
        return (-x * y, -y * y, -w * y)
    if index == 2:
        return (-x * w, -y * w, -w * w)
    if index == 3:  # H_xx = diag(1,0,-1)
        return (x, Q(0), -w)
    if index == 4:  # H_xy
        return (y, x, Q(0))
    if index == 5:  # H_xz
        return (w, Q(0), x)
    if index == 6:  # H_yy = diag(0,1,-1)
        return (Q(0), y, -w)
    if index == 7:  # H_yz
        return (Q(0), w, y)
    raise ValueError(index)


def rational_chart(rows):
    count = Q(len(rows))
    origin = tuple(sum((p[k] for p in rows.values()), Q(0)) / count for k in range(3))
    centered = {i: sub(p, origin) for i, p in rows.items()}
    rms2 = sum((dot(p, p) for p in centered.values()), Q(0)) / count
    scale = q17(math.sqrt(float(rms2)))
    z0 = {i: mul(p, 1 / scale) for i, p in centered.items()}

    raw_u = sub(rows[54], rows[0])
    raw_witness = sub(rows[1], rows[0])
    raw_n = cross(raw_u, raw_witness)
    raw_v = cross(raw_n, raw_u)
    if dot(raw_n, raw_n) == 0 or dot(raw_v, raw_v) == 0:
        raise AssertionError("degenerate base-plane basis")
    u = mul(raw_u, q17(1.0 / norm_float(raw_u)))
    v = mul(raw_v, q17(1.0 / norm_float(raw_v)))
    # Cross products, not approximate dot tests, certify exact tangency.
    assert dot(raw_n, u) == 0 and dot(raw_n, v) == 0

    local_scales = {}
    for k, i in enumerate(BASE_CYCLE):
        prev_i = BASE_CYCLE[(k - 1) % len(BASE_CYCLE)]
        next_i = BASE_CYCLE[(k + 1) % len(BASE_CYCLE)]
        local = min(norm_float(sub(rows[i], rows[prev_i])),
                    norm_float(sub(rows[next_i], rows[i])))
        local_scales[i] = q17(local)

    names = (
        [f"pole_{axis}" for axis in "xyz"]
        + ["H_xx", "H_xy", "H_xz", "H_yy", "H_yz"]
        + [f"base_{i}_{axis}" for i in BASE_CYCLE for axis in ("u", "v")]
    )
    if len(names) != D:
        raise AssertionError(len(names))
    base_columns = {i: (8 + 2 * k, 8 + 2 * k + 1) for k, i in enumerate(BASE_CYCLE)}

    jets = {}
    for i, p in z0.items():
        velocities = [projective_velocity(k, p) for k in range(8)]
        velocities += [(Q(0), Q(0), Q(0)) for _ in range(36)]
        if i in base_columns:
            cu, cv = base_columns[i]
            velocities[cu] = mul(u, local_scales[i] / scale)
            velocities[cv] = mul(v, local_scales[i] / scale)
        jets[i] = tuple(
            J(p[axis], tuple(velocity[axis] for velocity in velocities))
            for axis in range(3)
        )
    chart = {
        "control_names": names,
        "origin_exact": [qs(z) for z in origin],
        "rms_scale_rationalized_exact": qs(scale),
        "base_plane_normal_exact": [qs(z) for z in raw_n],
        "base_u_rationalized_exact": [qs(z) for z in u],
        "base_v_rationalized_exact": [qs(z) for z in v],
        "local_scales_rationalized_exact": {str(i): qs(z) for i, z in local_scales.items()},
        "exact_tangency_checks": {
            "normal_dot_u": qs(dot(raw_n, u)),
            "normal_dot_v": qs(dot(raw_n, v)),
        },
    }
    return jets, z0, chart


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
    if d6.v <= 0:
        raise AssertionError("nonpositive volume")
    return tuple(z / (4 * d6) for z in m24), d6 / 6


def cycle_normal(cyc, q):
    a = q[cyc[0]]
    for j in range(1, len(cyc) - 1):
        n = cross(sub(q[cyc[j]], a), sub(q[cyc[j + 1]], a))
        if values(n) != (Q(0), Q(0), Q(0)):
            return n
    raise AssertionError(("flat face", cyc))


def edge_data(faces):
    incidence = {}
    neighbors = {}
    for fi, cyc in enumerate(faces):
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            incidence.setdefault(tuple(sorted((a, b))), []).append(fi)
            neighbors.setdefault(a, set()).add(b)
            neighbors.setdefault(b, set()).add(a)
    if not all(len(z) == 2 for z in incidence.values()):
        raise AssertionError("nonmanifold face ledger")
    return incidence, {i: sorted(z) for i, z in neighbors.items()}


def target_face_components(q, faces, centroid):
    target = frozenset((198, 243, 244))
    fi = next(k for k, cyc in enumerate(faces) if frozenset(cyc) == target)
    cyc = faces[fi]
    n = cycle_normal(cyc, q)
    h = dot(n, sub(q[cyc[0]], centroid))
    foot = mul(n, h / dot(n, n))
    x = {i: sub(q[i], centroid) for i in cyc}
    ref = tuple(sum((x[i][k] for i in cyc), J.c(0)) / len(cyc) for k in range(3))
    out = []
    for edge_index, (a, b) in enumerate(zip(cyc, cyc[1:] + cyc[:1])):
        e = sub(x[b], x[a])
        z = dot(cross(e, sub(foot, x[a])), n)
        reference = dot(cross(sub(values(x[b]), values(x[a])),
                              sub(values(ref), values(x[a]))), values(n))
        if reference < 0:
            z = -z
        if z.v <= 0:
            raise AssertionError(("nonpositive stable-face component", a, b, z.v))
        out.append((f"S[198,243,244]:edge_{a}_to_{b}", z, {
            "kind": "stable_face_death",
            "face_index": fi,
            "cycle": cyc,
            "edge_index": edge_index,
            "edge": [a, b],
        }))
    return out


def target_vertex_components(q, centroid, neighbors):
    i = 2
    xi = sub(q[i], centroid)
    out = []
    for j in neighbors[i]:
        xj = sub(q[j], centroid)
        z = -dot(xi, sub(xj, xi))
        if z.v <= 0:
            raise AssertionError(("nonpositive unstable-vertex component", i, j, z.v))
        out.append((f"U2:neighbor_{j}", z, {
            "kind": "unstable_vertex_death", "vertex": i, "neighbor": j,
        }))
    return out


def target_edge_components(edge, q, faces, centroid, incidence):
    i, j = edge
    xi, xj = sub(q[i], centroid), sub(q[j], centroid)
    direction = sub(xj, xi)
    t = -dot(xi, direction) / dot(direction, direction)
    foot = add(xi, mul(direction, t))
    inc = incidence[tuple(sorted(edge))]
    n1 = cycle_normal(faces[inc[0]], q)
    n2 = cycle_normal(faces[inc[1]], q)
    aa, bb, cc = dot(n1, n1), dot(n1, n2), dot(n2, n2)
    r1, r2 = dot(foot, n1), dot(foot, n2)
    den = aa * cc - bb * bb
    beta1 = (r1 * cc - r2 * bb) / den
    beta2 = (r2 * aa - r1 * bb) / den
    components = [("t", t), ("one_minus_t", 1 - t), ("beta1", beta1), ("beta2", beta2)]
    out = []
    for component, z in components:
        if z.v <= 0:
            raise AssertionError(("nonpositive saddle component", edge, component, z.v))
        out.append((f"H[{i},{j}]:{component}", z, {
            "kind": "saddle_edge_death",
            "edge": [i, j],
            "incident_face_indices": inc,
            "component": component,
        }))
    return out


def ultrathin_guards(q):
    # Both are the support numerator h-n.w of the corresponding triangle.
    a = -det3(sub(q[88], q[3]), sub(q[2], q[3]), sub(q[242], q[3]))
    b = -det3(sub(q[3], q[88]), sub(q[242], q[88]), sub(q[2], q[88]))
    if a.v <= 0 or b.v <= 0 or a != b:
        raise AssertionError((a.v, b.v, a == b))
    return [
        ("Q2388:face_[3,88,2]_witness_242", a, {
            "kind": "ultrathin_support_guard",
            "face": [3, 88, 2], "witness": 242,
        }),
        ("Q2388:face_[88,3,242]_witness_2", b, {
            "kind": "ultrathin_support_guard",
            "face": [88, 3, 242], "witness": 2,
        }),
    ]


def matrix_rank(rows):
    a = [[Q(z) for z in row] for row in rows]
    if not a:
        return 0
    nr, nc = len(a), len(a[0])
    rank = 0
    for col in range(nc):
        pivot = next((r for r in range(rank, nr) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        p = a[rank][col]
        for k in range(col, nc):
            a[rank][k] /= p
        for r in range(rank + 1, nr):
            if a[r][col]:
                f = a[r][col]
                for k in range(col, nc):
                    a[r][k] -= f * a[rank][k]
        rank += 1
        if rank == nr:
            break
    return rank


def jet_record(name, z, metadata):
    digest = hashlib.sha256(
        (qs(z.v) + "|" + "|".join(qs(t) for t in z.d)).encode()
    ).hexdigest()
    return {
        "name": name,
        **metadata,
        "value_exact": qs(z.v),
        "value_decimal": float(z.v),
        "value_log10_abs": qlog10(z.v),
        "gradient_exact": [qs(t) for t in z.d],
        "gradient_decimal": [float(t) for t in z.d],
        "sha256_exact_value_and_gradient": digest,
    }


def main():
    rows, faces = read_input()
    q, _, chart = rational_chart(rows)
    centroid, volume = exact_centroid(q, faces)
    incidence, neighbors = edge_data(faces)

    groups = {
        "stable_face_S198_243_244": target_face_components(q, faces, centroid),
        "unstable_vertex_U2": target_vertex_components(q, centroid, neighbors),
        "saddle_edge_H4_5": target_edge_components((4, 5), q, faces, centroid, incidence),
        "saddle_edge_H12_13": target_edge_components((12, 13), q, faces, centroid, incidence),
    }
    guards = ultrathin_guards(q)
    sizes = [len(z) for z in groups.values()]
    if sizes != [3, 3, 4, 4]:
        raise AssertionError(sizes)

    branches = []
    rank_histogram = {}
    for index, choice in enumerate(itertools.product(*(range(n) for n in sizes))):
        selected = [list(groups.values())[k][choice[k]] for k in range(4)]
        rank4 = matrix_rank([list(z[1].d) for z in selected])
        rank5 = matrix_rank([list(z[1].d) for z in selected] + [list(guards[0][1].d)])
        rank_histogram[f"death_rank_{rank4}_with_guard_rank_{rank5}"] = (
            rank_histogram.get(f"death_rank_{rank4}_with_guard_rank_{rank5}", 0) + 1
        )
        branches.append({
            "branch_index": index,
            "choice_indices": list(choice),
            "death_components": [z[0] for z in selected],
            "death_gradient_rank": rank4,
            "death_plus_ultrathin_guard_gradient_rank": rank5,
        })

    all_primitives = [z for group in groups.values() for z in group]
    records = {z[0]: jet_record(*z) for z in all_primitives + guards}
    result = {
        "version": 1,
        "type": "exact rational primitive/Jacobian ledger for the compensating four-death flip cell",
        "scope": (
            "Exact first jet of the finite-decimal CSV, supplied fixed-face triangulation, "
            "and explicitly recorded rationalized 44-control chart. Zero-equivalent primitives "
            "remove square-root normalizations. No nonlinear reachability claim is made."
        ),
        "source_csv": SOURCE.name,
        "faces_json": FACES_SOURCE.name,
        "fixed_f_vector": [61, 162, 103],
        "source_mechanics_class": [2, 2, 2],
        "source_named_extra_features": {
            "stable_face": [198, 243, 244],
            "unstable_vertex": 2,
            "saddle_edges": [[4, 5], [12, 13]],
        },
        "chart": chart,
        "centroid": [jet_record(f"centroid_{axis}", z, {"kind": "centroid"})
                     for axis, z in zip("xyz", centroid)],
        "volume": jet_record("oriented_volume", volume, {"kind": "volume"}),
        "component_groups": {key: [z[0] for z in value] for key, value in groups.items()},
        "primitives": records,
        "ultrathin_identity": {
            "first_guard": guards[0][0],
            "second_guard": guards[1][0],
            "exact_value_and_gradient_identical": guards[0][1] == guards[1][1],
            "shared_zero_set": "oriented tetrahedral volume of {2,3,88,242} equals zero",
        },
        "branch_count": len(branches),
        "branch_order": [
            "S[198,243,244] component",
            "U2 neighbour component",
            "H[4,5] component",
            "H[12,13] component",
        ],
        "branch_rank_histogram": rank_histogram,
        "branches": branches,
        "directed_affine_convention": {
            "death_inequality": "f_i + grad(f_i).x <= 0 for one selected component in each family",
            "support_survival_inequality": "h_quad + grad(h_quad).x > 0",
            "normalized_form": "a_i.x <= -1 and a_quad.x > -1, where a=gradient/value",
            "gordan_farkas_use": (
                "A selected numerical LP branch can be exactified by retaining its sparse active rows, "
                "replacing every row by this ledger's Fraction row, and checking either a rational "
                "strict-feasible point or nonnegative multipliers lambda with lambda^T A=0 and "
                "lambda^T b<0."
            ),
        },
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    print("RANK4_FLIP_EXACT_LEDGER_PASS")
    print("branches", len(branches), "rank_histogram", rank_histogram)
    print("ultrathin primitive", float(guards[0][1].v), qs(guards[0][1].v))
    print("output", OUTPUT)


if __name__ == "__main__":
    main()
