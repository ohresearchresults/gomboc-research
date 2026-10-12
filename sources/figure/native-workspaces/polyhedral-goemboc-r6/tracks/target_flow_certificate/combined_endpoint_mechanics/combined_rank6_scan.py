#!/usr/bin/env python3
"""Rank-five left-null scan for a remote sixth combined-wall actuator."""
from __future__ import annotations

from pathlib import Path
import ast
import itertools
import json

import numpy as np
from scipy.linalg import qr

import combined_four_death_lp as four


HERE = Path(__file__).resolve().parent
NPZ = HERE / "combined_four_death_jacobian.npz"
LOCAL_ROWS = {1, 6, 7, 8, 9, 10, 54, 228, 245, 246, 247, 258}


def apply_modes(points, modes, coeffs):
    out = {i: np.asarray(p, float).copy() for i, p in points.items()}
    for t, mode in zip(coeffs, modes):
        if t:
            for i in out:
                out[i] += float(t) * mode[i]
    # Restore the exact q246 wall equation; the chart derivative omits only
    # second-order cross terms between its affine coordinates and plane rows.
    a, b, c, q = out[7], out[8], out[245], out[246]
    n = np.cross(b - a, c - a)
    out[246] = q - n * (np.dot(n, q - a) / np.dot(n, n))
    return out


def main():
    points = four.load_points()
    res, vals = four.primitive_ledger(points)
    modes, meta, _ = four.chart_modes(points)
    data = np.load(NPZ, allow_pickle=True)
    J = data["jacobian"]
    keys = [ast.literal_eval(str(z)) for z in data["primitive_keys"]]
    key_index = {k: i for i, k in enumerate(keys)}

    fkey = next(k for k in vals if k[0] == "face" and frozenset(k[1]) == four.QUAD and k[2] == (8, 246))
    ukey = ("vertex", 54, 1)
    h67 = ("edge", (6, 7), "one_minus_t")
    h910 = ("edge", (9, 10), "t")
    relay_candidates = [
        k for k in vals if k[0] == "face" and frozenset(k[1]) == frozenset((228, 247, 258))
    ]
    relay = min(relay_candidates, key=vals.__getitem__)
    wall_keys = [fkey, ukey, h67, h910, relay]
    w0 = np.asarray([vals[k] for k in wall_keys])
    JW = np.vstack([J[key_index[k]] for k in wall_keys])

    local = [i for i, m in enumerate(meta) if m.get("row") in LOCAL_ROWS]
    JL = JW[:, local]
    # The QR chart is rank revealing, but on this thin cap it can have a very
    # large affine root.  The local catalog is only 28 columns, so exhaust the
    # 5-column charts and minimize max |parameter| before the left-null scan.
    chosen_local = None
    root = None
    best_root_key = None
    for cols in itertools.combinations(local, 5):
        trial = JW[:, cols]
        if np.linalg.matrix_rank(trial, tol=1e-9) < 5:
            continue
        try:
            trial_root = np.linalg.solve(trial, -w0)
        except np.linalg.LinAlgError:
            continue
        key = (float(np.max(np.abs(trial_root))), float(np.linalg.norm(trial_root)))
        if best_root_key is None or key < best_root_key:
            best_root_key, chosen_local, root = key, list(cols), trial_root
    if chosen_local is None:
        raise RuntimeError("no rank-five local chart")
    J5 = JW[:, chosen_local]
    rank5 = int(np.linalg.matrix_rank(J5, tol=1e-9))
    if rank5 != 5:
        raise ValueError(f"local chart rank {rank5}")

    # Signed protected guards are positive at the seed.
    guards = four.chosen_guards(vals)
    gkeys, gsigns, gkind = zip(*guards)
    g0 = np.asarray([s * vals[k] for k, s in zip(gkeys, gsigns)])
    JG = np.vstack([s * J[key_index[k]] for k, s in zip(gkeys, gsigns)])
    predicted = g0 + JG[:, chosen_local] @ root
    # The relay wall is intentionally driven to zero and must not select itself.
    eligible = [i for i, k in enumerate(gkeys) if k != relay]
    sixth_i = min(eligible, key=lambda i: predicted[i])
    sixth_key = gkeys[sixth_i]
    sixth_value = g0[sixth_i]
    sixth_row = JG[sixth_i]

    six_by_five = np.vstack((J5, sixth_row[chosen_local]))
    _, _, vh = np.linalg.svd(six_by_five.T)
    left_null = vh[-1]
    left_null /= np.linalg.norm(left_null)
    residual = float(np.linalg.norm(left_null @ six_by_five))
    affine_incompatibility = float(left_null @ np.r_[w0, sixth_value])

    # Remote means outside the entire residual/core catalog, not merely an
    # unselected direction on one of the same rows.
    remote = [i for i, m in enumerate(meta) if m.get("row") not in LOCAL_ROWS]
    responses = []
    for col in remote:
        col6 = np.r_[JW[:, col], sixth_row[col]]
        response = float(left_null @ col6)
        responses.append({
            "column": col,
            **meta[col],
            "left_null_response": response,
            "absolute_response": abs(response),
            "six_wall_column": col6.tolist(),
        })
    responses.sort(key=lambda z: z["absolute_response"], reverse=True)

    completions = []
    for candidate in responses[:30]:
        col = int(candidate["column"])
        J6 = np.column_stack((six_by_five, np.r_[JW[:, col], sixth_row[col]]))
        if np.linalg.matrix_rank(J6, tol=1e-9) < 6:
            continue
        x6 = np.linalg.solve(J6, -np.r_[w0, sixth_value])
        selected_modes = [modes[i] for i in chosen_local] + [modes[col]]
        try:
            candidate_points = apply_modes(points, selected_modes, x6)
            rr, vv = four.primitive_ledger(candidate_points)
            fresh = {
                "valid": True,
                "f_vector": [len(rr.active), len(rr.edges), len(rr.faces)],
                "class": [len(rr.stable), len(rr.unstable), len(rr.saddles)],
                "topology_margin": rr.topology_margin,
                "active": sorted(rr.active),
                "faces_match": {frozenset(f["cycle"]) for f in rr.faces}
                == {frozenset(f["cycle"]) for f in res.faces},
            }
        except Exception as exc:
            fresh = {"valid": False, "error": repr(exc)}
        completions.append({
            "remote": {k: candidate[k] for k in (
                "column", "kind", "row", "axis", "left_null_response"
            )},
            "parameters": x6.tolist(),
            "max_abs_parameter": float(np.max(np.abs(x6))),
            "l2_parameter": float(np.linalg.norm(x6)),
            "fresh_audit": fresh,
        })
    completions.sort(
        key=lambda z: (
            bool(z["fresh_audit"].get("faces_match")),
            bool(z["fresh_audit"].get("valid")),
            -z["max_abs_parameter"],
        ), reverse=True,
    )

    out = {
        "version": 1,
        "scope": "combined wall rank-five left-null remote sixth-actuator scan",
        "source": str(four.SOURCE.relative_to(four.ROOT)),
        "wall_keys": [repr(k) for k in wall_keys],
        "wall_values": w0.tolist(),
        "local_catalog_columns": local,
        "chosen_rank5_columns": chosen_local,
        "chosen_rank5_chart": [{"column": i, **meta[i]} for i in chosen_local],
        "rank5_jacobian": J5.tolist(),
        "rank5": rank5,
        "rank5_linear_root": root.tolist(),
        "rank5_root_max_abs": float(np.max(np.abs(root))),
        "sixth_threatened_guard": {
            "key": repr(sixth_key),
            "kind": gkind[sixth_i],
            "seed_signed_value": float(sixth_value),
            "predicted_at_rank5_root": float(predicted[sixth_i]),
            "gradient_in_rank5_chart": sixth_row[chosen_local].tolist(),
        },
        "left_null_vector": left_null.tolist(),
        "left_null_residual_norm": residual,
        "affine_incompatibility": affine_incompatibility,
        "remote_catalog_size": len(remote),
        "top_remote_responses": responses[:60],
        "rank6_nonlinear_completions": completions,
    }
    (HERE / "combined_rank6_scan.json").write_text(json.dumps(out, indent=2))
    print("rank5 chart", out["chosen_rank5_chart"])
    print("root", out["rank5_linear_root"])
    print("sixth", out["sixth_threatened_guard"])
    print("left-null residual/affine", residual, affine_incompatibility)
    for z in responses[:15]:
        print("remote", z["absolute_response"], z.get("row"), z.get("axis"), z["column"])


if __name__ == "__main__":
    main()
