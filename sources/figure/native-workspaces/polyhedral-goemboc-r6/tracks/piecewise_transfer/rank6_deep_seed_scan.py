#!/usr/bin/env python3
"""Rank-revealing sixth-control scan on the deep robust target sphere.

Input: tracks/circuit_atlas/robust_rebuilt_fast.json.

Five selected wall rows are differentiated through the fixed actual cell:
  * death of stable F0=[8,245,246] through its closest face component;
  * death of U1 through its closest vertex support;
  * one closest death component each for H(6,7) and H(9,10);
  * the closest adjacent anti-transfer face [228,247,258].

Pivoted QR chooses a rank-revealing five-column chart from local/core and
row-54 coordinate directions.  The chart root is used to identify the next
threatened guard.  The resulting 6x5 left null covector ranks every remote
support-slack row/direction by its missing-rank response.

This is a numerical selector.  The selected rational direction is intended
for subsequent exact Fraction-jet certification.
"""
from __future__ import annotations

import csv
import importlib.util
import json
import math
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.linalg import qr

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ATLAS = ROOT / "tracks" / "circuit_atlas"


def load_row54_module():
    path = ATLAS / "row54_four_residual_search.py"
    spec = importlib.util.spec_from_file_location("row54_search", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


R54 = load_row54_module()


def read_target_rows():
    rows = {}
    with (ATLAS / "target_sphere_rebuilt.csv").open() as f:
        for r in csv.DictReader(f):
            rows[int(r["source_id"])] = np.array(
                [float(r[k]) for k in ("x", "y", "z")], dtype=float
            )
    ids = sorted(rows)
    return ids, np.array([rows[i] for i in ids])


def detailed(ids, p, faces):
    ix = {i: k for k, i in enumerate(ids)}
    ef, nbr = R54.edge_lattice(faces)
    active = sorted(set().union(*(set(c) for c in faces)))
    cen = R54.own_centroid(ids, p, faces)
    x = {i: p[ix[i]] - cen for i in active}
    normals = R54.face_normals(ids, p, faces)
    face = {}
    for fi, (cyc, n) in enumerate(zip(faces, normals)):
        h = float(n @ x[cyc[0]])
        foot = n * h / float(n @ n)
        ref = np.mean([x[i] for i in cyc], axis=0)
        vals = {}
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            e = x[b] - x[a]
            z = float(np.dot(np.cross(e, foot - x[a]), n))
            if np.dot(np.cross(e, ref - x[a]), n) < 0:
                z = -z
            vals[(a, b)] = z / (np.linalg.norm(e) * np.linalg.norm(n))
        face[fi] = vals
    vertex = {}
    for i in active:
        vertex[i] = {
            j: -float(x[i] @ (x[j] - x[i]))
            / (np.linalg.norm(x[i]) * np.linalg.norm(x[j] - x[i]))
            for j in sorted(nbr[i])
        }
    edge = {}
    for e, inc in ef.items():
        i, j = e
        d = x[j] - x[i]
        t = -float(x[i] @ d) / float(d @ d)
        q0 = x[i] + t * d
        n1, n2 = normals[inc[0]], normals[inc[1]]
        aa, bb, cc = float(n1 @ n1), float(n1 @ n2), float(n2 @ n2)
        r1, r2 = float(q0 @ n1), float(q0 @ n2)
        den = aa * cc - bb * bb
        b1 = (r1 * cc - r2 * bb) / den
        b2 = (r2 * aa - r1 * bb) / den
        qn = max(float(q0 @ q0), 1e-300)
        edge[e] = {
            "t": t,
            "one_minus_t": 1.0 - t,
            "beta1": b1 * math.sqrt(aa / qn),
            "beta2": b2 * math.sqrt(cc / qn),
        }
    return {"centroid": cen, "face": face, "vertex": vertex, "edge": edge, "ef": ef, "nbr": nbr}


def choose_walls(ids, p, faces):
    d = detailed(ids, p, faces)
    face_index = {frozenset(c): k for k, c in enumerate(faces)}
    f0i = face_index[frozenset((8, 245, 246))]
    reli = face_index[frozenset((228, 247, 258))]
    f0_edge, f0_value = min(d["face"][f0i].items(), key=lambda z: z[1])
    relay_edge, relay_value = min(d["face"][reli].items(), key=lambda z: z[1])
    u1_neighbor, u1_value = min(d["vertex"][1].items(), key=lambda z: z[1])
    h67_name, h67_value = min(d["edge"][(6, 7)].items(), key=lambda z: z[1])
    h910_name, h910_value = min(d["edge"][(9, 10)].items(), key=lambda z: z[1])
    specs = [
        {"kind": "face", "face": f0i, "edge": f0_edge, "name": f"death_F0:{f0_edge}"},
        {"kind": "vertex", "vertex": 1, "neighbor": u1_neighbor, "name": f"death_U1:{u1_neighbor}"},
        {"kind": "edge", "edge": (6, 7), "component": h67_name, "name": f"death_H67:{h67_name}"},
        {"kind": "edge", "edge": (9, 10), "component": h910_name, "name": f"death_H910:{h910_name}"},
        {"kind": "face", "face": reli, "edge": relay_edge, "name": f"relay_228_247_258:{relay_edge}"},
    ]
    return specs, np.array([f0_value, u1_value, h67_value, h910_value, relay_value]), d


def wall_values(detail, specs):
    out = []
    for s in specs:
        if s["kind"] == "face":
            out.append(detail["face"][s["face"]][tuple(s["edge"])])
        elif s["kind"] == "vertex":
            out.append(detail["vertex"][s["vertex"]][s["neighbor"]])
        else:
            out.append(detail["edge"][tuple(s["edge"])][s["component"]])
    return np.array(out, float)


def base_plane_basis(ids, p):
    ix = {i: k for k, i in enumerate(ids)}
    a, b, c = p[ix[0]], p[ix[1]], p[ix[2]]
    u = b - a
    u /= np.linalg.norm(u)
    n = np.cross(b - a, c - a)
    n /= np.linalg.norm(n)
    v = np.cross(n, u)
    v /= np.linalg.norm(v)
    return u, v, n


def direction_catalog(ids, p, local_only=False):
    base = set(range(17))
    active = set(ids)
    u, v, _ = base_plane_basis(ids, p)
    local_rows = {1, 6, 7, 8, 9, 10, 54, 228, 245, 246, 247, 258}
    rows = sorted(local_rows if local_only else active - local_rows)
    out = []
    axes = np.eye(3)
    for i in rows:
        dirs = [("base_u", u), ("base_v", v)] if i in base else [
            ("x", axes[0]), ("y", axes[1]), ("z", axes[2])
        ]
        for name, vec in dirs:
            out.append({"row": i, "axis": name, "vector": np.asarray(vec, float)})
    return out


def perturb(ids, p, direction, eps):
    q = p.copy()
    ix = {i: k for k, i in enumerate(ids)}
    q[ix[direction["row"]]] += eps * direction["vector"]
    return q


def jacobian(ids, p, faces, specs, catalog, eps=2e-6):
    out = np.zeros((len(specs), len(catalog)))
    for k, direction in enumerate(catalog):
        pp = perturb(ids, p, direction, eps)
        pm = perturb(ids, p, direction, -eps)
        out[:, k] = (
            wall_values(detailed(ids, pp, faces), specs)
            - wall_values(detailed(ids, pm, faces), specs)
        ) / (2 * eps)
    return out


def guard_records(ids, p, faces):
    m = R54.mechanics(ids, p, faces)
    guards, labels = R54.signed_guards(m, faces, "robust")
    return guards, labels


def main():
    record = json.loads((ATLAS / "robust_rebuilt_fast.json").read_text())
    ids, p0 = read_target_rows()
    _, faces, _ = R54.group_maximal_faces(ids, p0)
    p, den = R54.transform(p0, np.asarray(record["theta"], float))
    assert p is not None and np.min(den) > 0.08
    specs, w0, detail0 = choose_walls(ids, p, faces)
    local = direction_catalog(ids, p, local_only=True)
    jl = jacobian(ids, p, faces, specs, local)
    # Normalize columns before pivoting so a direction is not selected merely
    # because of coordinate units.  Every catalog direction is unit already,
    # but the explicit normalization also handles roundoff.
    norms = np.maximum(np.linalg.norm(jl, axis=0), 1e-15)
    _, rmat, piv = qr(jl / norms, mode="economic", pivoting=True)
    chosen_idx = list(map(int, piv[:5]))
    chosen = [local[k] for k in chosen_idx]
    j5 = jl[:, chosen_idx]
    rank5 = int(np.linalg.matrix_rank(j5, tol=1e-9))
    assert rank5 == 5
    root = np.linalg.solve(j5, -w0)
    displacement = sum((root[k] * chosen[k]["vector"] for k in range(5)), np.zeros(3))
    qroot = p.copy()
    ix = {i: k for k, i in enumerate(ids)}
    for t, direction in zip(root, chosen):
        qroot[ix[direction["row"]]] += t * direction["vector"]

    # Identify the next threatened nonselected guard by linear prediction in
    # the chosen chart.  Guard derivatives use the same fixed mechanics cell.
    g0, labels = guard_records(ids, p, faces)
    jg = np.zeros((len(g0), 5))
    eps = 2e-6
    for k, direction in enumerate(chosen):
        gp, _ = guard_records(ids, perturb(ids, p, direction, eps), faces)
        gm, _ = guard_records(ids, perturb(ids, p, direction, -eps), faces)
        jg[:, k] = (gp - gm) / (2 * eps)
    gpred = g0 + jg @ root
    excluded_labels = {
        ("S+", frozenset((8, 245, 246))),
        ("U+", 1),
        ("H+", (6, 7)),
        ("H+", (9, 10)),
        ("S-", frozenset((228, 247, 258))),
    }

    def label_key(lab):
        typ, obj = lab
        if typ.startswith("S"):
            return typ, frozenset(obj)
        if typ.startswith("H"):
            return typ, tuple(sorted(obj))
        return typ, int(obj)

    eligible = [k for k, lab in enumerate(labels) if label_key(lab) not in excluded_labels]
    sixth_guard_index = min(eligible, key=lambda k: gpred[k])
    sixth_label = labels[sixth_guard_index]
    # A guard is positive when protected.  Its wall row is the guard itself.
    g6 = jg[sixth_guard_index]
    v6 = g0[sixth_guard_index]
    g6x5 = np.vstack([j5, g6])
    uu, ss, vh = np.linalg.svd(g6x5.T)
    lam = vh[-1]
    lam /= np.linalg.norm(lam)
    assert np.linalg.norm(lam @ g6x5) < 2e-6
    affine_obstruction = float(lam @ np.r_[w0, v6])

    remote_raw = direction_catalog(ids, p, local_only=False)
    # A fixed maximal-face ledger can become exactly singular in binary64 for
    # an otherwise harmless symmetric +/- probe (two such columns occur in
    # this seed).  They are unsuitable numerical selectors, so record and
    # omit them rather than poisoning the entire remote scan.
    remote = []
    rejected_remote = []
    for direction in remote_raw:
        try:
            for sign in (1.0, -1.0):
                probe = perturb(ids, p, direction, sign * eps)
                detailed(ids, probe, faces)
                guard_records(ids, probe, faces)
        except (ArithmeticError, FloatingPointError) as exc:
            rejected_remote.append(
                {
                    "row": direction["row"],
                    "axis": direction["axis"],
                    "reason": repr(exc),
                }
            )
            continue
        remote.append(direction)
    jr = jacobian(ids, p, faces, specs, remote)
    # Sixth guard derivatives for all remote columns.
    g6r = np.zeros(len(remote))
    for k, direction in enumerate(remote):
        gp, _ = guard_records(ids, perturb(ids, p, direction, eps), faces)
        gm, _ = guard_records(ids, perturb(ids, p, direction, -eps), faces)
        g6r[k] = (gp[sixth_guard_index] - gm[sixth_guard_index]) / (2 * eps)
    responses = []
    for k, direction in enumerate(remote):
        col6 = np.r_[jr[:, k], g6r[k]]
        response = float(lam @ col6)
        responses.append(
            {
                "row": direction["row"],
                "axis": direction["axis"],
                "vector": direction["vector"].tolist(),
                "left_null_response": response,
                "absolute_response": abs(response),
                "six_wall_column": col6.tolist(),
            }
        )
    responses.sort(key=lambda z: z["absolute_response"], reverse=True)

    # Solve and actually audit the first twenty rank-six completions.  This is
    # not accepted unless the fresh hull remains well-defined.
    completions = []
    for candidate in responses[:20]:
        col = np.asarray(candidate["six_wall_column"])
        j6 = np.column_stack([g6x5, col])
        if np.linalg.matrix_rank(j6, tol=1e-9) < 6:
            continue
        x6 = np.linalg.solve(j6, -np.r_[w0, v6])
        qc = p.copy()
        for t, direction in zip(x6[:5], chosen):
            qc[ix[direction["row"]]] += t * direction["vector"]
        rv = np.asarray(candidate["vector"])
        qc[ix[candidate["row"]]] += x6[5] * rv
        try:
            audit, fresh_faces, fm = R54.fresh_audit(ids, qc, faces)
            fresh_ok = audit["faces_match_fixed_cell"]
            guards_c, labels_c = guard_records(ids, qc, faces)
            hard = float(np.min(guards_c))
        except Exception as exc:
            audit = {"error": repr(exc)}
            fresh_ok = False
            hard = -1e9
        completions.append(
            {
                "remote": {k: candidate[k] for k in ("row", "axis", "vector", "left_null_response")},
                "parameters": x6.tolist(),
                "max_abs_parameter": float(np.max(np.abs(x6))),
                "fresh_faces_match": fresh_ok,
                "robust_mode_hard_at_nonlinear_completion": hard,
                "fresh_audit": audit,
            }
        )
    completions.sort(
        key=lambda z: (z["fresh_faces_match"], z["robust_mode_hard_at_nonlinear_completion"]),
        reverse=True,
    )

    out = {
        "version": 1,
        "type": "numerical rank-revealing sixth-control scan on deep robust target sphere",
        "source": "tracks/circuit_atlas/robust_rebuilt_fast.json",
        "source_hard_margin": record["requested_hard_margin"],
        "source_class": record["fresh_hull_audit"]["class"],
        "wall_specs": specs,
        "wall_values": w0.tolist(),
        "local_catalog_size": len(local),
        "chosen_rank5_chart": [
            {"row": z["row"], "axis": z["axis"], "vector": z["vector"].tolist()}
            for z in chosen
        ],
        "rank5_jacobian": j5.tolist(),
        "rank5": rank5,
        "rank5_linear_root": root.tolist(),
        "rank5_root_max_abs": float(np.max(np.abs(root))),
        "sixth_threatened_guard": {
            "label": sixth_label,
            "seed_value": float(v6),
            "predicted_at_rank5_root": float(gpred[sixth_guard_index]),
            "gradient_in_rank5_chart": g6.tolist(),
        },
        "left_null_vector": lam.tolist(),
        "left_null_residual_norm": float(np.linalg.norm(lam @ g6x5)),
        "affine_incompatibility": affine_obstruction,
        "remote_catalog_size": len(remote),
        "remote_catalog_raw_size": len(remote_raw),
        "rejected_singular_remote_columns": rejected_remote,
        "top_remote_responses": responses[:40],
        "rank6_nonlinear_completions": completions,
    }
    path = HERE / "rank6_deep_seed_scan.json"
    path.write_text(json.dumps(out, indent=2) + "\n")
    print("DEEP_RANK6_SCAN_PASS")
    print("walls", [(s["name"], float(v)) for s, v in zip(specs, w0)])
    print("chosen", [(z["row"], z["axis"]) for z in chosen], "root", root)
    print("sixth", sixth_label, "pred", gpred[sixth_guard_index])
    print("top remote", [(z["row"], z["axis"], z["absolute_response"]) for z in responses[:10]])
    print("best completion", completions[0] if completions else None)
    print("output", path)


if __name__ == "__main__":
    main()
