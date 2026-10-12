#!/usr/bin/env python3
"""Exact reconstruction and mechanics audit of the rank-five shell seed.

No floating coordinate is authoritative.  The source fifth-cell lattice is
read as Fractions, rows 231..246 are projected exactly onto

    100 x + 20 y - 6 z = 3700,

and row 228 is replaced by (-19,-35,-12).  Qhull is used only to propose the
maximal-face cycles.  Every proposed plane, incidence, mass, centroid and
mechanical sign is then checked with exact rational arithmetic.
"""
from __future__ import annotations

import csv
import json
import math
import sys
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
WORK = ROOT / "M42_acute_bridge_fifth_cell_work"
sys.path.insert(0, str(WORK / "fourth_cell_endpoint"))
from numeric_hull_proposer import evaluate  # type: ignore

N = (Q(100), Q(20), Q(-6))
H = Q(3700)
N2 = sum(z * z for z in N)
ZERO = (Q(0), Q(0), Q(0))


def add(a, b):
    return tuple(a[k] + b[k] for k in range(3))


def sub(a, b):
    return tuple(a[k] - b[k] for k in range(3))


def mul(a, t):
    return tuple(a[k] * t for k in range(3))


def dot(a, b):
    return sum(a[k] * b[k] for k in range(3))


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def det(a, b, c):
    return dot(a, cross(b, c))


def n2(a):
    return dot(a, a)


def qs(x):
    x = Q(x)
    return f"{x.numerator}/{x.denominator}"


def read_exact_rows():
    path = WORK / "fifth_cell_endpoint" / "input_rows_common_lattice.csv"
    rows = {}
    for row in csv.DictReader(path.open()):
        den = int(row["denominator"])
        rows[int(row["source_id"])] = tuple(
            Q(int(row[k]), den) for k in ("x_int", "y_int", "z_int")
        )
    for i in range(231, 247):
        a = (H - dot(N, rows[i])) / N2
        rows[i] = add(rows[i], mul(N, a))
        assert dot(N, rows[i]) == H
    rows[228] = (Q(-19), Q(-35), Q(-12))
    return rows


def numeric_faces(rows):
    fp = {i: np.array([float(z) for z in p]) for i, p in rows.items()}
    res = evaluate(fp, plane_tol=1e-7, strict_tol=1e-10)
    assert res.valid, res.error
    return res


def exactify_faces(rows, proposal):
    out = []
    seen = set()
    for face in proposal.faces:
        c = list(face["cycle"])
        a = rows[c[0]]
        nn = ZERO
        for j in range(1, len(c) - 1):
            for k in range(j + 1, len(c)):
                nn = cross(sub(rows[c[j]], a), sub(rows[c[k]], a))
                if nn != ZERO:
                    break
            if nn != ZERO:
                break
        assert nn != ZERO
        h = dot(nn, a)
        vals = {i: dot(nn, p) - h for i, p in rows.items()}
        pos = any(z > 0 for z in vals.values())
        neg = any(z < 0 for z in vals.values())
        assert not (pos and neg), (c, min(vals.values()), max(vals.values()))
        if pos:
            nn = tuple(-z for z in nn)
            h = -h
            vals = {i: -z for i, z in vals.items()}
        cop = sorted(i for i, z in vals.items() if z == 0)
        assert set(cop) == set(c), (c, cop)
        area = ZERO
        for u, v in zip(c, c[1:] + c[:1]):
            area = add(area, cross(rows[u], rows[v]))
        if dot(area, nn) < 0:
            c = [c[0]] + list(reversed(c[1:]))
        # Divide by the integer gcd after clearing rational denominators only
        # for compact output; mechanics itself is scale invariant.
        key = (tuple(cop),)
        assert key not in seen
        seen.add(key)
        out.append({"cycle": c, "n": nn, "h": h})
    return out


def exact_mass(rows, faces):
    d6 = Q(0)
    m24 = [Q(0), Q(0), Q(0)]
    for f in faces:
        c = f["cycle"]
        for j in range(1, len(c) - 1):
            a, b, z = (rows[i] for i in (c[0], c[j], c[j + 1]))
            d = det(a, b, z)
            d6 += d
            for k in range(3):
                m24[k] += d * (a[k] + b[k] + z[k])
    assert d6 > 0
    volume = d6 / 6
    centroid = tuple(m24[k] / (4 * d6) for k in range(3))
    return volume, centroid


def exact_mechanics(rows, faces, centroid):
    ef = defaultdict(list)
    for fi, f in enumerate(faces):
        c = f["cycle"]
        for a, b in zip(c, c[1:] + c[:1]):
            ef[tuple(sorted((a, b)))].append(fi)
    assert all(len(v) == 2 for v in ef.values())
    active = sorted(set().union(*(set(f["cycle"]) for f in faces)))
    x = {i: sub(rows[i], centroid) for i in rows}
    neigh = defaultdict(set)
    for a, b in ef:
        neigh[a].add(b)
        neigh[b].add(a)

    face_ledger = []
    stable = []
    for fi, f in enumerate(faces):
        nn, h0 = f["n"], f["h"]
        hc = h0 - dot(nn, centroid)
        assert hc > 0
        foot = mul(nn, hc / n2(nn))
        c = f["cycle"]
        ref = tuple(sum((x[i][k] for i in c), Q(0)) / len(c) for k in range(3))
        comps = []
        for a, b in zip(c, c[1:] + c[:1]):
            e = sub(x[b], x[a])
            z = dot(cross(e, sub(foot, x[a])), nn)
            rz = dot(cross(e, sub(ref, x[a])), nn)
            if rz < 0:
                z = -z
            assert z != 0
            comps.append(z)
        yes = min(comps) > 0
        if yes:
            stable.append(fi)
        face_ledger.append(
            {
                "face": fi,
                "cycle": c,
                "stable": yes,
                "components_exact": [qs(z) for z in comps],
                "minimum_component_decimal": float(min(comps)),
            }
        )

    vertex_ledger = []
    unstable = []
    for i in active:
        vals = {j: -dot(x[i], sub(x[j], x[i])) for j in sorted(neigh[i])}
        assert vals and all(z != 0 for z in vals.values())
        yes = min(vals.values()) > 0
        if yes:
            unstable.append(i)
        vertex_ledger.append(
            {
                "vertex": i,
                "unstable": yes,
                "supports_exact": {str(j): qs(z) for j, z in vals.items()},
                "minimum_support_decimal": float(min(vals.values())),
            }
        )

    edge_ledger = []
    saddles = []
    for e, inc in sorted(ef.items()):
        i, j = e
        d = sub(x[j], x[i])
        t = -dot(x[i], d) / n2(d)
        p = add(x[i], mul(d, t))
        n1 = faces[inc[0]]["n"]
        n2v = faces[inc[1]]["n"]
        aa, bb, cc = n2(n1), dot(n1, n2v), n2(n2v)
        r1, r2 = dot(p, n1), dot(p, n2v)
        den = aa * cc - bb * bb
        assert den > 0
        b1 = (r1 * cc - r2 * bb) / den
        b2 = (r2 * aa - r1 * bb) / den
        vals = (t, Q(1) - t, b1, b2)
        assert all(z != 0 for z in vals)
        yes = min(vals) > 0
        if yes:
            saddles.append(e)
        edge_ledger.append(
            {
                "edge": list(e),
                "incident_faces": inc,
                "saddle": yes,
                "components_exact": [qs(z) for z in vals],
                "minimum_component_decimal": float(min(vals)),
            }
        )
    return ef, active, face_ledger, vertex_ledger, edge_ledger, stable, unstable, saddles


def main():
    rows = read_exact_rows()
    proposal = numeric_faces(rows)
    faces = exactify_faces(rows, proposal)
    volume, centroid = exact_mass(rows, faces)
    ef, active, fl, vl, el, stable, unstable, saddles = exact_mechanics(
        rows, faces, centroid
    )
    fvec = [len(active), len(ef), len(faces)]
    klass = [len(stable), len(unstable), len(saddles)]
    stable_cycles = [faces[i]["cycle"] for i in stable]
    assert fvec == [61, 150, 91], fvec
    assert klass == [3, 4, 5], klass
    assert any(set(c) == set(range(17)) for c in stable_cycles)
    assert 8 in unstable
    assert set(unstable) == {8, 228, 231, 246}
    assert set(saddles) == {
        (228, 254),
        (228, 255),
        (8, 246),
        (231, 247),
        (236, 237),
    }
    shell = next(f for f in faces if set(f["cycle"]) == set(range(231, 247)))
    assert dot(N, rows[231]) == H and set(shell["cycle"]) == set(range(231, 247))
    out = {
        "version": 1,
        "verdict": "EXACT_RECONSTRUCTED_RANK5_SHELL_SEED_IS_STRICT_345",
        "source": "exact fifth-cell common lattice plus exact rational shell/row228 controls",
        "shell_plane": {"normal": [100, 20, -6], "height": 3700, "normal_squared": int(N2)},
        "shell_rows": list(range(231, 247)),
        "row228": [-19, -35, -12],
        "f_vector": fvec,
        "euler": fvec[0] - fvec[1] + fvec[2],
        "class": klass,
        "active": active,
        "volume_exact": qs(volume),
        "volume_decimal": float(volume),
        "centroid_exact": [qs(z) for z in centroid],
        "centroid_decimal": [float(z) for z in centroid],
        "stable_faces": [{"face": i, "cycle": faces[i]["cycle"]} for i in stable],
        "unstable_vertices": unstable,
        "saddle_edges": [list(e) for e in saddles],
        "face_ledger": fl,
        "vertex_ledger": vl,
        "edge_ledger": el,
        "exact_checks": {
            "all_proposed_maximal_planes_support_all_119_rows": True,
            "each_exact_coplanar_set_equals_proposed_cycle": True,
            "all_true_edges_have_two_incident_maximal_faces": True,
            "mass_and_centroid_recomputed_from_exact_oriented_face_fans": True,
            "all_mechanical_components_nonzero": True,
            "base_stable": True,
            "vertex8_unstable": True,
        },
    }
    path = HERE / "rank5_reconstruction.json"
    path.write_text(json.dumps(out, indent=2) + "\n")
    print(out["verdict"])
    print("f_vector", fvec, "class", klass)
    print("stable", stable_cycles)
    print("unstable", unstable)
    print("saddles", saddles)
    print("output", path)


if __name__ == "__main__":
    main()
