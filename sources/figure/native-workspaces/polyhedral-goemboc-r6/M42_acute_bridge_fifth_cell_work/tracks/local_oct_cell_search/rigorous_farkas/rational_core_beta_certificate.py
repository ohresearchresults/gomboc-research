#!/usr/bin/env python3
"""Exact rational core beta-death versus anti-edge first-order certificate."""
from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
from typing import Iterable

import numpy as np
from scipy.optimize import linprog


HERE = Path(__file__).resolve().parent
TRACK = HERE.parent
WORK = TRACK.parents[1]
ENDPOINT = WORK / "fifth_cell_endpoint"
SOURCE = ENDPOINT / "input_rows_common_lattice.csv"
FACES_SOURCE = ENDPOINT / "face_cycles.json"
DIM = 18
CORE = (198, 224, 258, 229, 247, 228)
SADDLE = (229, 247)

sys.path.insert(0, str(TRACK))
import local_oct_cell_search as numeric  # noqa: E402
sys.path.insert(0, str(HERE))
import rational_shared_certificate as row54_exact  # noqa: E402


@dataclass(frozen=True)
class Dual:
    value: F
    grad: tuple[F, ...]

    @classmethod
    def constant(cls, value: object, dim: int = DIM):
        return cls(F(value), (F(0),) * dim)

    def coerce(self, other: object):
        return other if isinstance(other, Dual) else Dual.constant(other, len(self.grad))

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
        den = z.value * z.value
        return Dual(self.value / z.value,
                    tuple((a * z.value - self.value * b) / den
                          for a, b in zip(self.grad, z.grad)))

    def __rtruediv__(self, other: object):
        return self.coerce(other) / self


Vec = tuple[Dual, Dual, Dual]


def vec(values: Iterable[object]) -> Vec:
    out = tuple(x if isinstance(x, Dual) else Dual.constant(x) for x in values)
    assert len(out) == 3
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


def vsum(values: Iterable[Vec]) -> Vec:
    total = vec((0, 0, 0))
    for value in values:
        total = vadd(total, value)
    return total


def load_points() -> tuple[list[int], dict[int, tuple[F, F, F]]]:
    rows = {}
    with SOURCE.open() as f:
        for row in csv.DictReader(f):
            denominator = F(row["denominator"])
            rows[int(row["source_id"])] = tuple(
                F(row[k]) / denominator for k in ("x_int", "y_int", "z_int")
            )
    return sorted(rows), rows


IDS, RATIONAL_POINTS = load_points()
FACES = tuple(tuple(face) for face in json.load(FACES_SOURCE.open()))


def chart_points() -> dict[int, Vec]:
    p = {row: vec(xyz) for row, xyz in RATIONAL_POINTS.items()}
    col = 0
    for row in CORE:
        coordinates = []
        for k, value in enumerate(RATIONAL_POINTS[row]):
            grad = [F(0)] * DIM
            grad[col + k] = F(1)
            coordinates.append(Dual(value, tuple(grad)))
        p[row] = vec(coordinates)
        col += 3
    return p


def edge_lattice():
    ef = {}
    for fi, cyc in enumerate(FACES):
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            ef.setdefault(tuple(sorted((a, b))), []).append(fi)
    assert all(len(inc) == 2 for inc in ef.values())
    return ef


EDGE_FACES = edge_lattice()


def own_centroid(p: dict[int, Vec]) -> Vec:
    d6 = Dual.constant(0)
    moment = vec((0, 0, 0))
    for cyc in FACES:
        for j in range(1, len(cyc) - 1):
            a, b, c = p[cyc[0]], p[cyc[j]], p[cyc[j + 1]]
            determinant = dot(a, cross(b, c))
            d6 += determinant
            moment = vadd(moment, vscale(vadd(vadd(a, b), c), determinant))
    assert d6.value > 0
    return vscale(moment, F(1, 4) / d6)


def face_normals(p: dict[int, Vec]) -> list[Vec]:
    out = []
    for cyc in FACES:
        a = p[cyc[0]]
        normal = None
        for j in range(1, len(cyc) - 1):
            trial = cross(vsub(p[cyc[j]], a), vsub(p[cyc[j + 1]], a))
            if dot(trial, trial).value:
                normal = trial
                break
        assert normal is not None
        area = vsum(cross(p[u], p[v]) for u, v in zip(cyc, cyc[1:] + cyc[:1]))
        if dot(area, normal).value < 0:
            normal = vscale(normal, -1)
        out.append(normal)
    return out


def edge_primitives(edge, p, centroid, normals):
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
    beta1 = dot(q_num, cross(n2, cross12))
    beta2 = dot(q_num, cross(cross12, n1))
    return [t_num, one_minus_t_num, beta1, beta2]


def build_features():
    p = chart_points()
    centroid = own_centroid(p)
    normals = face_normals(p)
    _, _, _, _, templates = numeric.detailed_features(np.zeros(DIM))
    target = ("target:saddle-beta1-death",
              -edge_primitives(SADDLE, p, centroid, normals)[2])
    guards = [
        (f"guard:antiedge:{edge[0]}-{edge[1]}:c{k}",
         -edge_primitives(edge, p, centroid, normals)[k])
        for edge, k in sorted(templates["edge"].items())
    ]
    return [target, *guards]


def exact_dual(a, b, support):
    sub = [a[row] for row in support]
    kernel = row54_exact.nullspace(row54_exact.mat_transpose(sub))
    if len(kernel) != 1:
        return None, {"nullity": len(kernel)}
    y = kernel[0]
    if all(x <= 0 for x in y):
        y = [-x for x in y]
    if not all(x >= 0 for x in y) or not any(x > 0 for x in y):
        return None, {"nullity": 1, "kernel": [float(x) for x in y]}
    y = [x / sum(y, F(0)) for x in y]
    residual = [sum((sub[i][j] * y[i] for i in range(len(y))), F(0))
                for j in range(DIM)]
    b_dot_y = sum((b[row] * weight for row, weight in zip(support, y)), F(0))
    return y, {"residual": residual, "b_dot_y": b_dot_y}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=HERE / "core_beta_exact.json")
    args = ap.parse_args()
    features = build_features()
    epsilon = F(1, 1_000_000)
    names, a, b, scales = [], [], [], []
    for index, (name, item) in enumerate(features):
        raw_a = [-x for x in item.grad]
        raw_b = item.value - (epsilon if index == 0 else F(0))
        magnitude = max([abs(raw_b), *(abs(x) for x in raw_a)])
        scale = F(1, 1) / magnitude
        names.append(name); a.append([scale * x for x in raw_a])
        b.append(scale * raw_b); scales.append(scale)
    af = np.asarray([[float(x) for x in row] for row in a])
    bf = np.asarray([float(x) for x in b])
    dual_lp = linprog(
        bf,
        A_eq=np.vstack((af.T, np.ones(len(bf)))),
        b_eq=np.r_[np.zeros(DIM), 1.0],
        bounds=[(0, None)] * len(bf), method="highs",
    )
    assert dual_lp.success, dual_lp.message
    candidates = [np.flatnonzero(dual_lp.x > tol).tolist()
                  for tol in (1e-7, 1e-9, 1e-11, 1e-13)]
    diagnostics, chosen = [], None
    for support in candidates:
        y, audit = exact_dual(a, b, support)
        diagnostics.append({
            "support_size": len(support),
            "nullity": audit.get("nullity"),
            "b_dot_y": (float(audit["b_dot_y"]) if "b_dot_y" in audit else None),
        })
        if y is not None and audit["b_dot_y"] < 0:
            chosen = support, y, audit
            break
    out = {
        "statement": "Exact core beta1-death versus fixed anti-edge primitive witnesses",
        "feature_count": len(features),
        "float_dual_objective": float(dual_lp.fun),
        "support_diagnostics": diagnostics,
        "certificate_pass": chosen is not None,
    }
    if chosen:
        support, y, audit = chosen
        out.update({
            "support": [{
                "row": row, "name": names[row],
                "scale": row54_exact.frac_json(scales[row]),
                "A": [row54_exact.frac_json(x) for x in a[row]],
                "b": row54_exact.frac_json(b[row]),
                "y": row54_exact.frac_json(weight),
            } for row, weight in zip(support, y)],
            "A_transpose_y": [row54_exact.frac_json(x) for x in audit["residual"]],
            "b_dot_y": row54_exact.frac_json(audit["b_dot_y"]),
        })
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps({
        "feature_count": len(features),
        "float_dual_objective": float(dual_lp.fun),
        "diagnostics": diagnostics,
        "certificate_pass": out["certificate_pass"],
        "b_dot_y": out.get("b_dot_y", {}).get("decimal"),
        "support_names": [row["name"] for row in out.get("support", [])],
    }, indent=2))


if __name__ == "__main__":
    main()
