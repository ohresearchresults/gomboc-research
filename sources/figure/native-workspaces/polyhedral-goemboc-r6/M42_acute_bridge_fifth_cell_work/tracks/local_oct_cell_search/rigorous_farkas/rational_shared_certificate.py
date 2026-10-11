#!/usr/bin/env python3
"""Construct an exact rational first-order certificate for the row54 carrier.

The normalized mechanics used by the numerical search contain square roots.
For a rigorous sign-cell statement we replace them by their sign-equivalent
primitive numerators: oriented support determinants, vertex dot products, and
edge-foot / dual-normal numerators.  Decimal CSV coordinates are interpreted
as exact rationals.  Values and derivatives are evaluated by forward-mode AD
over fractions.Fraction; no finite differences or floating arithmetic enter
the certificate.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
from typing import Iterable


HERE = Path(__file__).resolve().parent
TRACK = HERE.parent
SOURCE = HERE / "fixed_cell.csv"
FACES_SOURCE = HERE / "fixed_cell_faces.json"
ACTUAL_ENDPOINT = HERE / "actual_endpoint.csv"
ACTUAL_ENDPOINT_FACES = HERE / "actual_endpoint_faces.json"
DIM = 13
ZERO_GRAD = (F(0),) * DIM


@dataclass(frozen=True)
class Dual:
    value: F
    grad: tuple[F, ...] = ZERO_GRAD

    @staticmethod
    def coerce(x: object) -> "Dual":
        return x if isinstance(x, Dual) else Dual(F(x))

    def __add__(self, other: object) -> "Dual":
        z = self.coerce(other)
        return Dual(self.value + z.value,
                    tuple(a + b for a, b in zip(self.grad, z.grad)))

    __radd__ = __add__

    def __neg__(self) -> "Dual":
        return Dual(-self.value, tuple(-a for a in self.grad))

    def __sub__(self, other: object) -> "Dual":
        return self + (-self.coerce(other))

    def __rsub__(self, other: object) -> "Dual":
        return self.coerce(other) - self

    def __mul__(self, other: object) -> "Dual":
        z = self.coerce(other)
        return Dual(self.value * z.value,
                    tuple(self.value * b + z.value * a
                          for a, b in zip(self.grad, z.grad)))

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> "Dual":
        z = self.coerce(other)
        if z.value == 0:
            raise ZeroDivisionError
        den = z.value * z.value
        return Dual(self.value / z.value,
                    tuple((a * z.value - self.value * b) / den
                          for a, b in zip(self.grad, z.grad)))

    def __rtruediv__(self, other: object) -> "Dual":
        return self.coerce(other) / self


Vec = tuple[Dual, Dual, Dual]


def variable(value: F, index: int, coefficient: F = F(1)) -> Dual:
    grad = [F(0)] * DIM
    grad[index] = coefficient
    return Dual(value, tuple(grad))


def vec(values: Iterable[object]) -> Vec:
    a = tuple(Dual.coerce(x) for x in values)
    assert len(a) == 3
    return a  # type: ignore[return-value]


def vadd(a: Vec, b: Vec) -> Vec:
    return tuple(x + y for x, y in zip(a, b))  # type: ignore[return-value]


def vsub(a: Vec, b: Vec) -> Vec:
    return tuple(x - y for x, y in zip(a, b))  # type: ignore[return-value]


def vscale(a: Vec, s: object) -> Vec:
    return tuple(x * s for x in a)  # type: ignore[return-value]


def dot(a: Vec, b: Vec) -> Dual:
    return sum((x * y for x, y in zip(a, b)), Dual(F(0)))


def cross(a: Vec, b: Vec) -> Vec:
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def vsum(values: Iterable[Vec]) -> Vec:
    out = vec((0, 0, 0))
    for value in values:
        out = vadd(out, value)
    return out


def load_points() -> tuple[list[int], dict[int, tuple[F, F, F]]]:
    rows = {}
    with SOURCE.open() as f:
        for row in csv.DictReader(f):
            rows[int(row["source_id"])] = tuple(
                F(row[k]) for k in ("x", "y", "z")
            )
    return sorted(rows), rows


IDS, RATIONAL_POINTS = load_points()
FACES = tuple(tuple(face) for face in json.load(FACES_SOURCE.open()))
IX = {row: k for k, row in enumerate(IDS)}


def rational_chart_points() -> dict[int, Vec]:
    """Exact affine 13-DOF chart: q246 free, five rows in the base plane."""
    p = {row: vec(xyz) for row, xyz in RATIONAL_POINTS.items()}
    xyz246 = []
    for k, value in enumerate(RATIONAL_POINTS[246]):
        xyz246.append(variable(value, k))
    p[246] = vec(xyz246)

    u = tuple(RATIONAL_POINTS[1][k] - RATIONAL_POINTS[0][k] for k in range(3))
    v = tuple(RATIONAL_POINTS[2][k] - RATIONAL_POINTS[0][k] for k in range(3))
    col = 3
    for row in (54, 6, 7, 9, 10):
        p[row] = tuple(
            Dual(RATIONAL_POINTS[row][k], tuple(
                (u[k] if j == col else v[k] if j == col + 1 else F(0))
                for j in range(DIM)
            )) for k in range(3)
        )  # type: ignore[assignment]
        col += 2
    return p


def edge_lattice() -> tuple[dict[tuple[int, int], list[int]], dict[int, set[int]]]:
    ef: dict[tuple[int, int], list[int]] = {}
    nbr: dict[int, set[int]] = {}
    for fi, cyc in enumerate(FACES):
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            edge = tuple(sorted((a, b)))
            ef.setdefault(edge, []).append(fi)
            nbr.setdefault(a, set()).add(b)
            nbr.setdefault(b, set()).add(a)
    assert all(len(inc) == 2 for inc in ef.values())
    return ef, nbr


EDGE_FACES, NEIGHBORS = edge_lattice()


def own_centroid(p: dict[int, Vec]) -> Vec:
    d6 = Dual(F(0))
    moment = vec((0, 0, 0))
    for cyc in FACES:
        for j in range(1, len(cyc) - 1):
            a, b, c = p[cyc[0]], p[cyc[j]], p[cyc[j + 1]]
            det = dot(a, cross(b, c))
            d6 += det
            moment = vadd(moment, vscale(vadd(vadd(a, b), c), det))
    if d6.value < 0:
        d6 = -d6
        moment = vscale(moment, -1)
    assert d6.value > 0
    return vscale(moment, F(1, 4) / d6)


def face_normals(p: dict[int, Vec]) -> list[Vec]:
    normals = []
    for cyc in FACES:
        a = p[cyc[0]]
        normal = None
        for j in range(1, len(cyc) - 1):
            trial = cross(vsub(p[cyc[j]], a), vsub(p[cyc[j + 1]], a))
            if dot(trial, trial).value != 0:
                normal = trial
                break
        assert normal is not None
        area = vsum(cross(p[u], p[v]) for u, v in zip(cyc, cyc[1:] + cyc[:1]))
        if dot(area, normal).value < 0:
            normal = vscale(normal, -1)
        normals.append(normal)
    return normals


def stable_primitives(face_index: int, p: dict[int, Vec], centroid: Vec,
                      normals: list[Vec]) -> list[Dual]:
    """Positive raw numerators for stable-foot-in-polygon components."""
    cyc = FACES[face_index]
    n = normals[face_index]
    n2 = dot(n, n)
    x = {row: vsub(p[row], centroid) for row in cyc}
    h = dot(n, x[cyc[0]])
    ref = vscale(vsum(x[row] for row in cyc), F(1, len(cyc)))
    values = []
    for a, b in zip(cyc, cyc[1:] + cyc[:1]):
        edge = vsub(x[b], x[a])
        # n2 times the usual unnormalized component; n2 is positive.
        foot_minus_a_scaled = vsub(vscale(n, h), vscale(x[a], n2))
        value = dot(cross(edge, foot_minus_a_scaled), n)
        interior = dot(cross(edge, vsub(ref, x[a])), n)
        if interior.value < 0:
            value = -value
        values.append(value)
    return values


def vertex_primitive(row: int, neighbor: int, p: dict[int, Vec], centroid: Vec) -> Dual:
    x = vsub(p[row], centroid)
    direction = vsub(p[neighbor], p[row])
    return -dot(x, direction)


def edge_primitives(edge: tuple[int, int], p: dict[int, Vec], centroid: Vec,
                    normals: list[Vec]) -> list[Dual]:
    """Positive sign primitives for t, 1-t, beta1 and beta2."""
    a, b = tuple(sorted(edge))
    xa = vsub(p[a], centroid)
    direction = vsub(p[b], p[a])
    d2 = dot(direction, direction)
    t_num = -dot(xa, direction)
    one_minus_t_num = d2 - t_num
    q_num = vadd(vscale(xa, d2), vscale(direction, t_num))
    f1, f2 = EDGE_FACES[(a, b)]
    n1, n2 = normals[f1], normals[f2]
    cross12 = cross(n1, n2)
    beta1_num = dot(q_num, cross(n2, cross12))
    beta2_num = dot(q_num, cross(cross12, n1))
    return [t_num, one_minus_t_num, beta1_num, beta2_num]


def topology_primitive(face_index: int, row: int, p: dict[int, Vec],
                       normals: list[Vec]) -> Dual:
    cyc = FACES[face_index]
    n = normals[face_index]
    return dot(n, vsub(p[cyc[0]], p[row]))


def mat_transpose(a: list[list[F]]) -> list[list[F]]:
    return [list(row) for row in zip(*a)]


def matmul(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    bt = mat_transpose(b)
    return [[sum((x * y for x, y in zip(row, col)), F(0)) for col in bt]
            for row in a]


def inverse(a: list[list[F]]) -> list[list[F]]:
    n = len(a)
    aug = [row[:] + [F(int(i == j)) for j in range(n)] for i, row in enumerate(a)]
    for col in range(n):
        pivot = next(row for row in range(col, n) if aug[row][col] != 0)
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for row in range(n):
            if row == col:
                continue
            scale = aug[row][col]
            if scale:
                aug[row] = [x - scale * y for x, y in zip(aug[row], aug[col])]
    return [row[n:] for row in aug]


def nullspace(a: list[list[F]]) -> list[list[F]]:
    """Exact rational nullspace basis of an m-by-n matrix."""
    m, n = len(a), len(a[0])
    r = [row[:] for row in a]
    pivots = []
    row = 0
    for col in range(n):
        pivot = next((k for k in range(row, m) if r[k][col]), None)
        if pivot is None:
            continue
        r[row], r[pivot] = r[pivot], r[row]
        scale = r[row][col]
        r[row] = [x / scale for x in r[row]]
        for k in range(m):
            if k != row and r[k][col]:
                scale = r[k][col]
                r[k] = [x - scale * y for x, y in zip(r[k], r[row])]
        pivots.append(col)
        row += 1
        if row == m:
            break
    free = [col for col in range(n) if col not in pivots]
    basis = []
    for free_col in free:
        x = [F(0)] * n
        x[free_col] = F(1)
        for pivot_row in range(len(pivots) - 1, -1, -1):
            pivot_col = pivots[pivot_row]
            x[pivot_col] = -sum((r[pivot_row][j] * x[j]
                                 for j in free), F(0))
        basis.append(x)
    return basis


def frac_json(x: F) -> dict:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator),
            "decimal": float(x)}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=HERE / "row54_shared_exact.json")
    args = ap.parse_args()

    p = rational_chart_points()
    centroid = own_centroid(p)
    normals = face_normals(p)
    stable_face = next(i for i, face in enumerate(FACES)
                       if frozenset(face) == frozenset((7, 8, 246)))

    # Good-positive target primitives: death is the negative of the feature.
    targets = [
        ("S[7,8,246]-death", -stable_primitives(stable_face, p, centroid, normals)[1]),
        ("U54-death", -vertex_primitive(54, 1, p, centroid)),
        ("H67-death", -edge_primitives((6, 7), p, centroid, normals)[0]),
        ("H910-death", -edge_primitives((9, 10), p, centroid, normals)[1]),
    ]
    selected = [
        targets[1],
        targets[2],
        ("topology:f15:row8", topology_primitive(15, 8, p, normals)),
        ("antiedge:263-264:c3",
         -edge_primitives((263, 264), p, centroid, normals)[3]),
    ]

    jt = [list(item.grad) for _, item in targets]
    gram = matmul(jt, mat_transpose(jt))
    four = matmul(mat_transpose(jt), inverse(gram))
    shared = [[row[0], row[1], row[2] + row[3]] for row in four]

    y0 = [item.value for _, item in selected]
    jac = [list(item.grad) for _, item in selected]
    reduced_jac = matmul(jac, shared)
    a = [[-x for x in row] for row in reduced_jac]
    epsilon = F(1, 1_000_000)
    requested = [epsilon, epsilon, F(0), F(0)]
    b = [value - need for value, need in zip(y0, requested)]
    kernel = nullspace(mat_transpose(a))
    assert len(kernel) == 1, len(kernel)
    dual = kernel[0]
    if all(x <= 0 for x in dual):
        dual = [-x for x in dual]
    nonnegative = all(x >= 0 for x in dual) and any(x > 0 for x in dual)
    total = sum(dual, F(0))
    if total:
        dual = [x / total for x in dual]
    residual = [sum((a[i][j] * dual[i] for i in range(len(dual))), F(0))
                for j in range(3)]
    b_dot_y = sum((x * y for x, y in zip(b, dual)), F(0))

    out = {
        "statement": (
            "Exact rational Farkas certificate for the sign-primitive shared-3D "
            "first-order model at row54_far_rebuilt."
        ),
        "source": str(SOURCE),
        "faces_source": str(FACES_SOURCE),
        "frozen_artifacts": {
            path.name: sha256(path) for path in (
                SOURCE, FACES_SOURCE, ACTUAL_ENDPOINT, ACTUAL_ENDPOINT_FACES
            )
        },
        "chart": (
            "q246 standard xyz; rows 54,6,7,9,10 use exact base-plane "
            "directions p1-p0 and p2-p0"
        ),
        "dimension": DIM,
        "epsilon": frac_json(epsilon),
        "target_names": [name for name, _ in targets],
        "selected_names": [name for name, _ in selected],
        "selected_values": [frac_json(x) for x in y0],
        "A": [[frac_json(x) for x in row] for row in a],
        "b": [frac_json(x) for x in b],
        "dual_y": [frac_json(x) for x in dual],
        "dual_nonnegative": nonnegative,
        "A_transpose_y": [frac_json(x) for x in residual],
        "b_dot_y": frac_json(b_dot_y),
        "certificate_pass": nonnegative and all(x == 0 for x in residual) and b_dot_y < 0,
        "primitive_definitions": {
            "topology": "n.(p_face-p_row), with exact oriented raw face normal n",
            "vertex": "-(p_i-C).(p_j-p_i)",
            "edge_t": "-(p_i-C).(p_j-p_i)",
            "edge_one_minus_t": "|d|^2+(p_i-C).d",
            "edge_beta1": "q_num.(n2 x (n1 x n2))",
            "edge_beta2": "q_num.((n1 x n2) x n1)",
            "stable": "oriented raw foot-in-polygon numerator multiplied by |n|^2",
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps({
        "certificate_pass": out["certificate_pass"],
        "dual_nonnegative": nonnegative,
        "b_dot_y": float(b_dot_y),
        "dual": [float(x) for x in dual],
        "residual": [float(x) for x in residual],
    }, indent=2))


if __name__ == "__main__":
    main()
