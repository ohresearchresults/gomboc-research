#!/usr/bin/env python3
"""Exact rational proof helpers for the two grouped nullspace bypasses.

The proof objects are finite decimal snapshots, projected once onto the exact
base plane through rows 0, 1, 2.  All paths below are explicit rational
polynomial paths.  No floating-point predicate participates in verification.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_DIR = HERE.parent
CORE_PATH = ROOT / "tracks/global_carrier_support/rigorous_local_bypass/exact_core.py"
sys.path.insert(0, str(CORE_PATH.parent))
import exact_core as ex  # noqa: E402


P = ex.P
BASE = ex.BASE
PROTECTED = {
    "stable": [sorted(BASE), [7, 245, 246]],
    "unstable": [8, 54],
    "saddles": [[6, 7], [198, 263]],
}


def canonical_hash(value) -> str:
    payload = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode()
    return hashlib.sha256(payload).hexdigest()


def encode_points(points) -> dict[str, list[str]]:
    return {
        str(i): [ex.qs(x) for x in points[i]]
        for i in sorted(points)
    }


def decode_points(packet) -> dict[int, tuple[Q, Q, Q]]:
    return {
        int(i): tuple(Q(x) for x in xyz)
        for i, xyz in packet.items()
    }


def point_hash(points) -> str:
    return canonical_hash(encode_points(points))


def rationalize_float_points(ids, points):
    return {
        int(i): tuple(ex.q17(x) for x in points[k])
        for k, i in enumerate(ids)
    }


def repair_base(rows):
    """Project all enlarged-base rows onto one exact rational plane."""
    rows = dict(rows)
    a = rows[0]
    normal = ex.cross(ex.sub(rows[1], a), ex.sub(rows[2], a))
    nn = ex.norm2(normal)
    if not nn:
        raise AssertionError("degenerate exact base anchors")
    corrections = {}
    for i in BASE:
        coefficient = ex.dot(normal, ex.sub(rows[i], a)) / nn
        rows[i] = ex.sub(rows[i], ex.mul(normal, coefficient))
        corrections[i] = coefficient
        if ex.dot(normal, ex.sub(rows[i], a)):
            raise AssertionError(("base repair failed", i))
    nonzero = [ex.qlog10(x) for x in corrections.values() if x]
    return rows, {
        "nonzero_correction_count": sum(bool(x) for x in corrections.values()),
        "largest_coefficient_log10_abs": max(nonzero) if nonzero else -math.inf,
    }


def read_repaired(path: Path):
    return repair_base(ex.read_rows(path))


def _barycentric(point, a, b, c):
    e1, e2, w = ex.sub(b, a), ex.sub(c, a), ex.sub(point, a)
    aa, ab, bb = ex.dot(e1, e1), ex.dot(e1, e2), ex.dot(e2, e2)
    wa, wb = ex.dot(w, e1), ex.dot(w, e2)
    determinant = aa * bb - ab * ab
    if not determinant:
        raise AssertionError("degenerate base chart")
    return (
        (wa * bb - wb * ab) / determinant,
        (wb * aa - wa * ab) / determinant,
    )


def planar_morph(start, end):
    """Exact polynomial morph preserving the enlarged base coplanarity.

    Rows 0,1,2 move affinely.  Every other base row is reconstructed from
    linearly interpolated exact barycentric coordinates, hence has degree at
    most two and stays in their moving plane.  Nonbase rows move affinely.
    """
    if set(start) != set(end):
        raise AssertionError("mismatched point labels")

    def linear(a, b):
        return P((a, b - a))

    out = {
        i: tuple(linear(start[i][k], end[i][k]) for k in range(3))
        for i in (0, 1, 2)
    }
    anchor = out[0]
    e1, e2 = ex.sub(out[1], anchor), ex.sub(out[2], anchor)
    for i in BASE - {0, 1, 2}:
        u0, v0 = _barycentric(start[i], start[0], start[1], start[2])
        u1, v1 = _barycentric(end[i], end[0], end[1], end[2])
        u, v = linear(u0, u1), linear(v0, v1)
        out[i] = ex.add(anchor, ex.add(ex.mul(e1, u), ex.mul(e2, v)))
    for i in set(start) - BASE:
        out[i] = tuple(linear(start[i][k], end[i][k]) for k in range(3))
    return out


def evaluate_path(points, parameter: Q):
    return {
        i: tuple(coordinate.eval(parameter) for coordinate in xyz)
        for i, xyz in points.items()
    }


def face_key_text(face_key) -> str:
    return ",".join(str(i) for i in face_key)


def edge_text(edge) -> str:
    return f"{edge[0]},{edge[1]}"


def all_primitives(points, faces):
    """Return every support/incidence/mechanics defining polynomial.

    Unlike a minimal class witness, this ledger includes every component of
    every face, vertex and edge decision, including components that do not
    determine the feature's final Boolean value.
    """
    ledger = ex.mechanics_primitives(points, faces)
    records = [("volume:d6", ledger["d6"], True)]
    for fi, witness, poly in ex.support_polynomials(points, faces):
        records.append((f"support:f{fi}:w{witness}", poly, False))
    for face_key, values in ledger["reference"].items():
        fk = face_key_text(face_key)
        for edge, poly in values.items():
            records.append((f"face_reference:{fk}:{edge_text(edge)}", poly, False))
    for edge, components in ledger["edge"].items():
        et = edge_text(edge)
        records.append((f"edge_direction_norm2:{et}", components["direction_norm2"], True))
        records.append((f"edge_gram:{et}", components["gram"], True))
    for face_key in ledger["face"]:
        fk = face_key_text(face_key)
        for edge, poly in ex.signed_face_components(ledger, face_key).items():
            records.append((f"face:{fk}:{edge_text(edge)}", poly, False))
    for vertex, values in ledger["vertex"].items():
        for neighbor, poly in values.items():
            records.append((f"vertex:{vertex}:{neighbor}", poly, False))
    for edge, components in ledger["edge"].items():
        et = edge_text(edge)
        for component in ("t", "one_minus_t", "beta1", "beta2"):
            records.append((f"edge:{et}:{component}", components[component], False))
    return ledger, records


def audit_every_primitive(
    points,
    faces,
    lo: Q = Q(0),
    hi: Q = Q(1),
    skip=frozenset(),
    max_depth: int = 40,
):
    """Exact Bernstein sign certificate for every non-skipped primitive."""
    _, records = all_primitives(points, faces)
    digest = hashlib.sha256()
    leaves = 0
    worst = None
    count = 0
    for name, poly, intrinsically_positive in records:
        if name in skip:
            continue
        middle = (lo + hi) / 2
        value = poly.eval(middle)
        if not value:
            raise AssertionError(("zero primitive at audit midpoint", name))
        expected = 1 if value > 0 else -1
        if intrinsically_positive and expected != 1:
            raise AssertionError(("nonpositive incidence primitive", name))
        sign, local_leaves, local_worst = ex.bernstein_sign(
            poly, lo, hi, max_depth=max_depth
        )
        if sign != expected:
            raise AssertionError(("wrong primitive sign", name, sign, expected))
        digest.update(name.encode())
        digest.update(b"|")
        digest.update(str(sign).encode())
        digest.update(b"|")
        digest.update("|".join(poly.exact()).encode())
        digest.update(b"\n")
        leaves += local_leaves
        worst = local_worst if worst is None else min(worst, local_worst)
        count += 1
    return {
        "interval": [ex.qs(lo), ex.qs(hi)],
        "certified_polynomial_count": count,
        "bernstein_leaf_count": leaves,
        "min_bernstein_coefficient_log10_abs": worst,
        "primitive_digest": digest.hexdigest(),
        "skipped_primitives": sorted(skip),
    }


def point_audit(points, faces):
    support = ex.supporting_cell(points, faces)
    _, mechanics = ex.classify_point(points, faces)
    return {
        "coordinate_hash": point_hash(points),
        "support": support,
        "mechanics": mechanics,
    }


PAIR_SPECS = {
    "round2": {
        "vertex": (263, 10),
        "edge": (10, 263),
        "edge_component": "one_minus_t",
        "vertex_name": "vertex:263:10",
        "edge_name": "edge:10,263:one_minus_t",
        "identity": (
            "X263_dot_(P263-P10)",
            "(4D6)*norm2(P263-P10)+X10_dot_(P263-P10)",
        ),
    },
    "round3": {
        "vertex": (1, 54),
        "edge": (1, 54),
        "edge_component": "t",
        "vertex_name": "vertex:1:54",
        "edge_name": "edge:1,54:t",
        "identity": (
            "-X1_dot_(P54-P1)",
            "edge_t_numerator",
        ),
    },
}


def pair_polynomials(points, faces, pair_name):
    spec = PAIR_SPECS[pair_name]
    ledger = ex.mechanics_primitives(points, faces)
    v, n = spec["vertex"]
    vertex = ledger["vertex"][v][n]
    edge = ledger["edge"][spec["edge"]][spec["edge_component"]]
    if vertex != edge:
        raise AssertionError(("shared numerator identity failed", pair_name))
    return vertex, edge, spec


def coarse_first_sign_change(poly: P, lo=Q(0), hi=Q(1), pieces=100_000):
    coefficients = np.asarray([float(x) for x in poly.c])
    grid = np.linspace(float(lo), float(hi), pieces + 1)
    values = np.polynomial.polynomial.polyval(grid, coefficients)
    candidates = np.flatnonzero(
        (values[:-1] < 0) != (values[1:] < 0)
    )
    for index in candidates:
        a = lo + (hi - lo) * Q(int(index), pieces)
        b = lo + (hi - lo) * Q(int(index + 1), pieces)
        va, vb = poly.eval(a), poly.eval(b)
        if va and vb and ((va > 0) != (vb > 0)):
            return a, b
    raise AssertionError("no exact sign-change bracket found")


def root_record(poly: P, lo=Q(0), hi=Q(1), width=Q(1, 10**24)):
    a, b = coarse_first_sign_change(poly, lo, hi)
    root = ex.isolate_monotone_root(poly, a, b, width)
    return {
        "lo": ex.qs(root["lo"]),
        "hi": ex.qs(root["hi"]),
        "value_lo": ex.qs(root["value_lo"]),
        "value_hi": ex.qs(root["value_hi"]),
        "derivative_sign": root["derivative_sign"],
        "derivative_bernstein_leaves": root["derivative_bernstein_leaves"],
        "decimal_interval": [float(root["lo"]), float(root["hi"])],
    }


def verify_root_record(poly: P, record):
    lo, hi = Q(record["lo"]), Q(record["hi"])
    vlo, vhi = poly.eval(lo), poly.eval(hi)
    if ex.qs(vlo) != record["value_lo"] or ex.qs(vhi) != record["value_hi"]:
        raise AssertionError("root endpoint value mismatch")
    if not vlo or not vhi or ((vlo > 0) == (vhi > 0)):
        raise AssertionError("root record does not bracket a root")
    sign, leaves, _ = ex.bernstein_sign(poly.derivative(), lo, hi, max_depth=60)
    if sign != record["derivative_sign"]:
        raise AssertionError("root derivative sign mismatch")
    return {
        "lo": lo,
        "hi": hi,
        "derivative_sign": sign,
        "derivative_bernstein_leaves": leaves,
    }


def exact_sign_record(poly: P, lo=Q(0), hi=Q(1), expected=None, max_depth=60):
    sign, leaves, worst = ex.bernstein_sign(poly, lo, hi, max_depth=max_depth)
    if expected is not None and sign != expected:
        raise AssertionError(("unexpected directed guard sign", sign, expected))
    return {
        "interval": [ex.qs(lo), ex.qs(hi)],
        "sign": sign,
        "bernstein_leaf_count": leaves,
        "min_bernstein_coefficient_log10_abs": worst,
        "polynomial_digest": canonical_hash(poly.exact()),
    }

