#!/usr/bin/env python3
"""Rank-5/6 cancellation scan on the two rail-valid row-54 cells.

For each audited endpoint/far cell we select five scalar walls:

* the closest death component of its non-base stable face;
* the closest death component of U54;
* the closest death component of H(6,7) and H(9,10);
* the closest protected nonstable face (the adjacent transfer/relay wall).

The eight infinitesimal projective/trace-free metric coordinates form the
topology-preserving core chart.  Raw pivoted QR selects five columns.  We
then solve the five nonlinear wall equations, follow the path to that common
root, and select the first additional protected wall actually crossed.

The resulting 6x5 left null covector is a *local first-order obstruction*.
Every actual-cell row direction is ranked by its response to that covector.
Top remote actuators are then tested by solving the full six nonlinear wall
equations and fresh-auditing a one-sided point.  Thus a numerical rank claim
is never confused with an actual shared event.
"""
from __future__ import annotations

import csv
import importlib.util
import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import qr
from scipy.optimize import least_squares


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ATLAS = ROOT / "tracks" / "circuit_atlas"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


DEEP = load_module("rank6_deep_helpers", HERE / "rank6_deep_seed_scan.py")
R54 = DEEP.R54


def forced_rail_edges():
    short = [228] + list(range(229, 247)) + [8]
    long = [228] + list(range(247, 265)) + [8]
    edges = {
        tuple(sorted(edge))
        for path in (short, long)
        for edge in zip(path, path[1:])
    }
    edges.remove((228, 229))
    assert len(edges) == 37
    return edges


def read_cell(stem: str):
    rows = {}
    with (ATLAS / f"{stem}.csv").open() as f:
        for r in csv.DictReader(f):
            rows[int(r["source_id"])] = np.array(
                [float(r[k]) for k in ("x", "y", "z")], dtype=float
            )
    ids = sorted(rows)
    p = np.array([rows[i] for i in ids])
    faces = json.loads((ATLAS / f"{stem}_faces.json").read_text())
    audit = json.loads((ATLAS / f"{stem}_audit.json").read_text())
    return ids, p, faces, audit


def base_face(faces):
    candidates = [frozenset(c) for c in faces if set(range(17)) <= set(c)]
    assert len(candidates) == 1, candidates
    return candidates[0]


def feature_key(label):
    typ, obj = label
    if typ.startswith("S"):
        return typ, frozenset(obj)
    if typ.startswith("H"):
        return typ, tuple(sorted(obj))
    return typ, int(obj)


def target_guards(ids, p, faces):
    """Positive guards for the desired strict row-54 target (1,1,0)."""
    d = DEEP.detailed(ids, p, faces)
    base = base_face(faces)
    vals, labels = [], []
    for fi, cyc in enumerate(faces):
        decision = min(d["face"][fi].values())
        positive = frozenset(cyc) == base
        vals.append(decision if positive else -decision)
        labels.append(("S+" if positive else "S-", list(cyc)))
    for i, comps in d["vertex"].items():
        decision = min(comps.values())
        positive = i == 8
        vals.append(decision if positive else -decision)
        labels.append(("U+" if positive else "U-", i))
    for edge, comps in d["edge"].items():
        decision = min(comps.values())
        vals.append(-decision)
        labels.append(("H-", list(edge)))
    return np.asarray(vals, float), labels


def spec_value(detail, spec):
    if spec["kind"] == "face":
        return detail["face"][spec["face_index"]][tuple(spec["edge"])]
    if spec["kind"] == "vertex":
        return detail["vertex"][spec["vertex"]][spec["neighbor"]]
    return detail["edge"][tuple(spec["edge"])][spec["component"]]


def spec_values(ids, p, faces, specs):
    """Evaluate only the requested scalar components.

    The full detail ledger evaluates every edge of the 103-face cell and is
    useful for audits and guard selection.  A nonlinear six-wall solve calls
    this function thousands of times, so recomputing 162 unrelated saddle
    decompositions is both slow and exposes the solver to irrelevant remote
    singularities.  These are exactly the same component formulae, restricted
    to the requested faces, vertex-neighbor pairs, and edges.
    """
    ix = {i: k for k, i in enumerate(ids)}
    cen = R54.own_centroid(ids, p, faces)
    active = set().union(*(set(c) for c in faces))
    x = {i: p[ix[i]] - cen for i in active}
    normals = R54.face_normals(ids, p, faces)
    ef = None
    out = []
    for spec in specs:
        if spec["kind"] == "face":
            fi = spec["face_index"]
            cyc = faces[fi]
            n = normals[fi]
            h = float(n @ x[cyc[0]])
            foot = n * h / float(n @ n)
            ref = np.mean([x[i] for i in cyc], axis=0)
            a, b = spec["edge"]
            e = x[b] - x[a]
            value = float(np.dot(np.cross(e, foot - x[a]), n))
            if np.dot(np.cross(e, ref - x[a]), n) < 0:
                value = -value
            value /= np.linalg.norm(e) * np.linalg.norm(n)
        elif spec["kind"] == "vertex":
            i, j = spec["vertex"], spec["neighbor"]
            d = x[j] - x[i]
            value = -float(x[i] @ d) / (np.linalg.norm(x[i]) * np.linalg.norm(d))
        else:
            if ef is None:
                ef, _ = R54.edge_lattice(faces)
            i, j = tuple(spec["edge"])
            edge = tuple(sorted((i, j)))
            d = x[j] - x[i]
            dd = float(d @ d)
            t = -float(x[i] @ d) / dd
            component = spec["component"]
            if component == "t":
                value = t
            elif component == "one_minus_t":
                value = 1.0 - t
            else:
                q0 = x[i] + t * d
                inc = ef[edge]
                n1, n2 = normals[inc[0]], normals[inc[1]]
                aa, bb, cc = float(n1 @ n1), float(n1 @ n2), float(n2 @ n2)
                r1, r2 = float(q0 @ n1), float(q0 @ n2)
                den = aa * cc - bb * bb
                if den <= 1e-28 * aa * cc:
                    raise ValueError("parallel incident face normals")
                if component == "beta1":
                    beta = (r1 * cc - r2 * bb) / den
                    value = beta * math.sqrt(aa / max(float(q0 @ q0), 1e-300))
                elif component == "beta2":
                    beta = (r2 * aa - r1 * bb) / den
                    value = beta * math.sqrt(cc / max(float(q0 @ q0), 1e-300))
                else:
                    raise ValueError(component)
        out.append(value)
    return np.asarray(out, float)


def scalar_spec_for_label(ids, p, faces, label, name):
    d = DEEP.detailed(ids, p, faces)
    typ, obj = label
    if typ.startswith("S"):
        target = frozenset(obj)
        fi = next(k for k, cyc in enumerate(faces) if frozenset(cyc) == target)
        edge, value = min(d["face"][fi].items(), key=lambda z: z[1])
        return {
            "kind": "face", "face_index": fi, "face": list(faces[fi]),
            "edge": list(edge), "name": name,
        }, float(value)
    if typ.startswith("U"):
        i = int(obj)
        nbr, value = min(d["vertex"][i].items(), key=lambda z: z[1])
        return {
            "kind": "vertex", "vertex": i, "neighbor": int(nbr), "name": name,
        }, float(value)
    edge = tuple(sorted(obj))
    comp, value = min(d["edge"][edge].items(), key=lambda z: z[1])
    return {
        "kind": "edge", "edge": list(edge), "component": comp, "name": name,
    }, float(value)


def choose_five_walls(ids, p, faces, audit):
    stable = [frozenset(c) for c in audit["fresh_hull_audit"]["stable_faces"]]
    base = base_face(faces)
    extra = next(c for c in stable if c != base)
    specs = []
    s, _ = scalar_spec_for_label(ids, p, faces, ("S+", list(extra)), "death_extra_S")
    specs.append(s)
    s, _ = scalar_spec_for_label(ids, p, faces, ("U+", 54), "death_U54")
    specs.append(s)
    s, _ = scalar_spec_for_label(ids, p, faces, ("H+", [6, 7]), "death_H67")
    specs.append(s)
    s, _ = scalar_spec_for_label(ids, p, faces, ("H+", [9, 10]), "death_H910")
    specs.append(s)

    # The tightest nonstable face is the mechanically strongest adjacent
    # transfer/relay guard in the audited target-sign ledger.
    stable_set = set(stable)
    detail = DEEP.detailed(ids, p, faces)
    candidates = []
    for fi, cyc in enumerate(faces):
        if frozenset(cyc) in stable_set:
            continue
        edge, decision = min(detail["face"][fi].items(), key=lambda z: z[1])
        candidates.append((-float(decision), fi, edge, float(decision)))
    signed_margin, fi, edge, decision = min(candidates, key=lambda z: z[0])
    assert signed_margin > 0.0
    specs.append({
        "kind": "face", "face_index": fi, "face": list(faces[fi]),
        "edge": list(edge), "name": "protected_transfer_relay",
    })
    return specs, spec_values(ids, p, faces, specs)


def projective_cell(p0, theta):
    p, den = R54.transform(p0, np.asarray(theta, float))
    if p is None:
        raise ValueError(f"projective pole: min denominator {float(np.min(den))}")
    return p, den


def theta_jacobian(fun, theta, eps=1e-6):
    eye = np.eye(len(theta))
    return np.column_stack([
        (fun(theta + eps * eye[k]) - fun(theta - eps * eye[k])) / (2.0 * eps)
        for k in range(len(theta))
    ])


def local_feature_rows(specs):
    rows = set()
    for s in specs:
        if s["kind"] == "face":
            rows.update(s["face"])
        elif s["kind"] == "vertex":
            rows.add(s["vertex"])
            rows.add(s["neighbor"])
        else:
            rows.update(s["edge"])
    return rows


def direction_catalog(ids, p, selected_rows):
    u, v, _ = DEEP.base_plane_basis(ids, p)
    base = set(range(17)) | {54}
    axes = np.eye(3)
    out = []
    rail_vertices = {8, 228} | set(range(229, 265))
    for row in ids:
        directions = [("base_u", u), ("base_v", v)] if row in base else [
            ("x", axes[0]), ("y", axes[1]), ("z", axes[2])
        ]
        for axis, vector in directions:
            out.append({
                "row": int(row), "axis": axis, "vector": np.asarray(vector, float),
                "touches_forced_rail_vertex": row in rail_vertices,
                "touches_selected_feature": row in selected_rows,
            })
    return out


def apply_direction(ids, p, direction, amount):
    q = p.copy()
    q[ids.index(direction["row"])] += amount * direction["vector"]
    return q


def rail_audit(ids, p):
    try:
        _, faces, _ = R54.group_maximal_faces(ids, p)
        edges, _ = R54.edge_lattice(faces)
        forced = forced_rail_edges()
        return {
            "fresh_f_vector": [len(set().union(*map(set, faces))), len(edges), len(faces)],
            "all_37_forced_rails_present": forced <= set(edges),
            "missing_forced_rails": [list(e) for e in sorted(forced - set(edges))],
            "fresh_faces": faces,
        }
    except Exception as exc:
        return {"error": repr(exc), "all_37_forced_rails_present": False}


def analyze_cell(stem):
    ids, original, faces, audit = read_cell(stem)
    theta0 = np.zeros(8)
    p, den0 = projective_cell(original, theta0)
    specs5, w0 = choose_five_walls(ids, p, faces, audit)

    def five_at(theta):
        q, _ = projective_cell(original, theta)
        return spec_values(ids, q, faces, specs5)

    j8 = theta_jacobian(five_at, theta0)
    # Keep literal QR pivots as a sparse rank witness, but use the five right
    # singular row-space vectors as the actual controls.  This is a genuine
    # five-dimensional chart and avoids an arbitrary coordinate subset that
    # can have no finite nonlinear root despite the full rank-five family.
    _, rmat, piv = qr(j8, mode="economic", pivoting=True)
    qr_pivots = list(map(int, piv[:5]))
    _, singular8, vh8 = np.linalg.svd(j8, full_matrices=False)
    control_basis = vh8.T
    j5 = j8 @ control_basis
    assert np.linalg.matrix_rank(j5, tol=1e-9) == 5
    linear_root = np.linalg.solve(j5, -w0)

    def theta_from_chart(x):
        return theta0 + control_basis @ np.asarray(x, float)

    def safe_five_chart(x):
        try:
            values = five_at(theta_from_chart(x))
            if not np.all(np.isfinite(values)):
                raise FloatingPointError("nonfinite wall value")
            return values
        except (ArithmeticError, FloatingPointError, ValueError):
            # Trust-region barrier for a projective pole or a degenerate
            # fixed-face trial.  Returning a finite vector lets the solver
            # retreat to the valid cell instead of aborting the full scan.
            return np.ones(5) * (1e4 + np.linalg.norm(x))

    nonlinear = least_squares(
        safe_five_chart, linear_root,
        max_nfev=3000, xtol=2e-13, ftol=2e-13, gtol=2e-13,
    )
    theta_root = theta_from_chart(nonlinear.x)
    p_root, den_root = projective_cell(original, theta_root)
    root_residual = five_at(theta_root)
    fresh_root, _, _ = R54.fresh_audit(ids, p_root, faces)

    # Find the first additional desired-sign guard crossed along the actual
    # nonlinear path.  All guards for each alpha are evaluated together.
    selected_keys = {
        ("S-", frozenset(specs5[0]["face"])),
        ("U-", 54),
        ("H-", (6, 7)),
        ("H-", (9, 10)),
        ("S-", frozenset(specs5[4]["face"])),
    }
    alphas = np.linspace(0.0, 1.0, 121)
    guard_path = []
    labels = None
    path_singularity = None
    for alpha in alphas:
        q, _ = projective_cell(original, theta_from_chart(alpha * nonlinear.x))
        try:
            guards, labels = target_guards(ids, q, faces)
        except (ArithmeticError, FloatingPointError, ValueError) as exc:
            path_singularity = {"alpha": float(alpha), "reason": repr(exc)}
            break
        guard_path.append(guards)
    alphas = alphas[:len(guard_path)]
    guard_path = np.asarray(guard_path)
    crossings = []
    for k, label in enumerate(labels):
        if feature_key(label) in selected_keys:
            continue
        z = guard_path[:, k]
        hits = np.where((z[:-1] > 1e-9) & (z[1:] <= 1e-9))[0]
        if not len(hits):
            continue
        h = int(hits[0])
        frac = float(z[h] / (z[h] - z[h + 1]))
        alpha = float(alphas[h] + frac * (alphas[h + 1] - alphas[h]))
        crossings.append({
            "alpha": alpha, "guard_index": k, "label": label,
            "seed_guard": float(z[0]), "root_guard": float(z[-1]),
        })
    crossings.sort(key=lambda z: z["alpha"])
    if crossings:
        selected_crossing = crossings[0]
        alpha6 = selected_crossing["alpha"]
        q6pick, _ = projective_cell(original, theta_from_chart(alpha6 * nonlinear.x))
        spec6, _ = scalar_spec_for_label(
            ids, q6pick, faces, selected_crossing["label"], "first_crossed_guard"
        )
    else:
        # A fully guarded five-wall event needs no actuator.  Still define the
        # tightest protected row at the root so rank six can be audited.
        eligible = [
            (float(guard_path[-1, k]), k, label)
            for k, label in enumerate(labels) if feature_key(label) not in selected_keys
        ]
        _, k, label = min(eligible)
        selected_crossing = {
            "alpha": None, "guard_index": k, "label": label,
            "seed_guard": float(guard_path[0, k]),
            "root_guard": float(guard_path[-1, k]),
        }
        spec6, _ = scalar_spec_for_label(ids, p_root, faces, label, "tightest_root_guard")
    specs6 = specs5 + [spec6]
    v6 = spec_values(ids, p, faces, [spec6])[0]

    def six_at_theta(theta):
        q, _ = projective_cell(original, theta)
        return spec_values(ids, q, faces, specs6)

    j6theta = theta_jacobian(six_at_theta, theta0)
    g6x5 = j6theta @ control_basis
    _, singular5, vh = np.linalg.svd(g6x5.T)
    lam = vh[-1]
    lam /= np.linalg.norm(lam)
    values6 = np.r_[w0, v6]
    affine_obstruction = float(lam @ values6)

    selected_rows = local_feature_rows(specs6)
    remote = direction_catalog(ids, p, selected_rows)
    responses = []
    eps = 2e-6
    for direction in remote:
        try:
            fp = spec_values(ids, apply_direction(ids, p, direction, eps), faces, specs6)
            fm = spec_values(ids, apply_direction(ids, p, direction, -eps), faces, specs6)
        except (ArithmeticError, FloatingPointError, ValueError):
            continue
        column = (fp - fm) / (2.0 * eps)
        response = float(lam @ column)
        responses.append({
            "row": direction["row"], "axis": direction["axis"],
            "vector": direction["vector"].tolist(),
            "touches_forced_rail_vertex": direction["touches_forced_rail_vertex"],
            "touches_selected_feature": direction["touches_selected_feature"],
            "six_wall_column": column.tolist(),
            "left_null_response": response,
            "absolute_response": abs(response),
        })
    responses.sort(key=lambda z: z["absolute_response"], reverse=True)

    # Prefer rail-safe actuators but also test the globally strongest two.
    test_pool = []
    preferred = [
        r for r in responses
        if not r["touches_forced_rail_vertex"] and not r["touches_selected_feature"]
    ]
    for z in preferred[:3] + responses[:1]:
        key = (z["row"], z["axis"])
        if key not in {(q["row"], q["axis"]) for q in test_pool}:
            test_pool.append(z)
    completions = []
    ix = {i: k for k, i in enumerate(ids)}
    for candidate in test_pool:
        print(
            stem, "testing actuator", candidate["row"], candidate["axis"],
            "response", candidate["absolute_response"], flush=True,
        )
        remote_col = np.asarray(candidate["six_wall_column"], float)
        j6 = np.column_stack([g6x5, remote_col])
        rank6 = int(np.linalg.matrix_rank(j6, tol=1e-9))
        if rank6 < 6:
            continue
        xlin6 = np.linalg.solve(j6, -values6)
        vector = np.asarray(candidate["vector"], float)

        def event_points(x):
            q, den = projective_cell(original, theta_from_chart(x[:5]))
            q = q.copy()
            q[ix[candidate["row"]]] += x[5] * vector
            return q, den

        def event_fun(x):
            try:
                q, _ = event_points(x)
                return spec_values(ids, q, faces, specs6)
            except Exception:
                return np.ones(6) * 1e4

        try:
            sol = least_squares(
                event_fun, xlin6, max_nfev=600,
                xtol=3e-12, ftol=3e-12, gtol=3e-12,
            )
            qevent, den_event = event_points(sol.x)
            residual = event_fun(sol.x)
            # The event itself may merge faces.  Audit the original-cell side
            # at 1-1e-5, which is the correct rail-survival witness.
            qinside, _ = event_points(sol.x * (1.0 - 1e-5))
            inside_fresh, _, _ = R54.fresh_audit(ids, qinside, faces)
            inside_rails = rail_audit(ids, qinside)
            event_rails = rail_audit(ids, qevent)
            shared = bool(np.max(np.abs(residual)) < 2e-7)
        except Exception as exc:
            sol = None
            residual = np.ones(6) * 1e100
            den_event = np.array([-1e100])
            inside_fresh = {"error": repr(exc), "faces_match_fixed_cell": False}
            inside_rails = {"error": repr(exc), "all_37_forced_rails_present": False}
            event_rails = inside_rails
            shared = False
        completions.append({
            "remote": {
                k: candidate[k] for k in (
                    "row", "axis", "vector", "touches_forced_rail_vertex",
                    "touches_selected_feature",
                    "left_null_response", "absolute_response",
                )
            },
            "rank6": rank6,
            "linear_parameters": xlin6.tolist(),
            "nonlinear_parameters": None if sol is None else sol.x.tolist(),
            "nonlinear_max_abs_parameter": None if sol is None else float(np.max(np.abs(sol.x))),
            "nonlinear_residuals": residual.tolist(),
            "nonlinear_max_abs_residual": float(np.max(np.abs(residual))),
            "minimum_projective_denominator": float(np.min(den_event)),
            "actual_shared_event": shared,
            "one_sided_faces_match_fixed_cell": bool(inside_fresh.get("faces_match_fixed_cell", False)),
            "one_sided_fresh_audit": inside_fresh,
            "one_sided_rail_audit": inside_rails,
            "event_rail_audit": event_rails,
        })
    completions.sort(key=lambda z: (
        z["actual_shared_event"],
        z["one_sided_rail_audit"].get("all_37_forced_rails_present", False),
        z["one_sided_faces_match_fixed_cell"],
        -z["nonlinear_max_abs_residual"],
        -(z["nonlinear_max_abs_parameter"] or 1e100),
    ), reverse=True)

    return {
        "cell": stem,
        "source_f_vector": audit["fresh_hull_audit"]["f_vector"],
        "source_class": audit["fresh_hull_audit"]["class"],
        "source_hard_margin": audit["all_mechanics_margins"]["hard_requested_margin"],
        "source_all_37_forced_rails_present": audit["fresh_hull_audit"]["all_forced_rail_edges_present"],
        "wall_specs": specs5,
        "wall_values": w0.tolist(),
        "projective_theta_jacobian_5x8": j8.tolist(),
        "projective_theta_singular_values": np.linalg.svd(j8, compute_uv=False).tolist(),
        "qr_rank5_theta_pivots": qr_pivots,
        "rank5_control_basis_8x5": control_basis.tolist(),
        "chosen_rank5_jacobian": j5.tolist(),
        "chosen_rank5_condition_number": float(np.linalg.cond(j5)),
        "rank5_linear_root": linear_root.tolist(),
        "rank5_nonlinear_root": nonlinear.x.tolist(),
        "rank5_nonlinear_residuals": root_residual.tolist(),
        "rank5_nonlinear_max_abs_residual": float(np.max(np.abs(root_residual))),
        "rank5_root_minimum_projective_denominator": float(np.min(den_root)),
        "rank5_root_fresh_audit": fresh_root,
        "rank5_path_first_singularity": path_singularity,
        "protected_guard_crossings": crossings[:20],
        "sixth_guard_selection": selected_crossing,
        "sixth_wall_spec": spec6,
        "six_wall_seed_values": values6.tolist(),
        "six_by_five_jacobian": g6x5.tolist(),
        "six_by_five_rank": int(np.linalg.matrix_rank(g6x5, tol=1e-9)),
        "six_by_five_singular_values": singular5.tolist(),
        "left_null_vector": lam.tolist(),
        "left_null_residual_norm": float(np.linalg.norm(lam @ g6x5)),
        "local_affine_obstruction": affine_obstruction,
        "local_affine_obstruction_absolute": abs(affine_obstruction),
        "remote_catalog_size": len(responses),
        "top_remote_responses": responses[:50],
        "nonlinear_rank6_completions": completions,
    }


def main():
    cells = []
    for stem in ("row54_endpoint_rebuilt", "row54_far_rebuilt"):
        print("analyzing", stem, flush=True)
        cell = analyze_cell(stem)
        cells.append(cell)
        checkpoint = HERE / f"rank6_{stem}.json"
        checkpoint.write_text(json.dumps(cell, indent=2) + "\n")
        print("checkpoint", checkpoint, flush=True)
    out = {
        "version": 1,
        "type": "rank-5/6 cancellation and rail-preserving actuator scan",
        "cells": cells,
    }
    path = HERE / "rank6_row54_rail_scan.json"
    path.write_text(json.dumps(out, indent=2) + "\n")
    print("ROW54_RAIL_RANK6_SCAN_PASS")
    for cell in cells:
        print("\n", cell["cell"])
        print("walls", [(z["name"], v) for z, v in zip(cell["wall_specs"], cell["wall_values"])])
        print("QR pivots", cell["qr_rank5_theta_pivots"], "condition", cell["chosen_rank5_condition_number"])
        print("rank5 residual", cell["rank5_nonlinear_max_abs_residual"],
              "den", cell["rank5_root_minimum_projective_denominator"])
        print("sixth", cell["sixth_guard_selection"])
        print("affine obstruction", cell["local_affine_obstruction"])
        print("top remote", [
            (z["row"], z["axis"], z["absolute_response"], z["touches_forced_rail_vertex"])
            for z in cell["top_remote_responses"][:10]
        ])
        best = cell["nonlinear_rank6_completions"][0] if cell["nonlinear_rank6_completions"] else None
        print("best completion", best)
    print("output", path)


if __name__ == "__main__":
    main()
