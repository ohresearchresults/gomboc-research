#!/usr/bin/env python3
"""Materialize and freshly audit one guarded four-death chart step."""
from __future__ import annotations

from pathlib import Path
import argparse
import ast
import csv
import json

import numpy as np

import combined_core
import combined_four_death_lp as four
import combined_rank6_scan as rank6


HERE = Path(__file__).resolve().parent


def write_csv(path, points):
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(("source_id", "x", "y", "z"))
        for i in sorted(points):
            w.writerow((i, *(f"{float(z):.17g}" for z in points[i])))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default=str(four.SOURCE))
    ap.add_argument("--lp-json", default=str(HERE / "combined_four_death_lp.json"))
    ap.add_argument("--alpha", type=float, required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--h67-branch")
    ap.add_argument("--h910-branch")
    args = ap.parse_args()
    source = Path(args.source)
    points = four.load_points(source)
    base_res, base_vals = four.primitive_ledger(points)
    modes, _, _ = four.chart_modes(points)
    lp = json.loads(Path(args.lp_json).read_text())
    candidates = [z for z in lp["atlas"] if z.get("success")]
    if args.h67_branch is not None:
        candidates = [z for z in candidates if ast.literal_eval(z["deaths"][2])[2] == args.h67_branch]
    if args.h910_branch is not None:
        candidates = [z for z in candidates if ast.literal_eval(z["deaths"][3])[2] == args.h910_branch]
    if not candidates:
        raise ValueError("requested saddle-component branch is absent from LP atlas")
    best = min(candidates, key=lambda z: z["delta"])
    coeffs = np.asarray(best["coefficients"], dtype=float)
    candidate = rank6.apply_modes(points, modes, args.alpha * coeffs)
    fresh, vals = four.primitive_ledger(candidate)
    base_faces = {frozenset(f["cycle"]) for f in base_res.faces}
    fresh_faces = {frozenset(f["cycle"]) for f in fresh.faces}
    forced = combined_core.forced_rail_edges()

    deaths = [ast.literal_eval(k) for k in best["deaths"]]
    guards = four.chosen_guards(base_vals)
    common_guards = [(key, sign, kind) for key, sign, kind in guards if key in vals]
    missing_guards = [(key, kind) for key, _sign, kind in guards if key not in vals]
    guard_ratios = [sign * vals[key] / (sign * base_vals[key]) for key, sign, _ in common_guards]
    gi = int(np.argmin(guard_ratios)) if guard_ratios else None
    death_ratios = {
        repr(key): (float(vals[key] / base_vals[key]) if key in vals else None)
        for key in deaths
    }
    removed_faces = sorted((sorted(face) for face in base_faces - fresh_faces), key=lambda x: (len(x), x))
    added_faces = sorted((sorted(face) for face in fresh_faces - base_faces), key=lambda x: (len(x), x))
    lost_vertices = sorted(set(points) - set(fresh.active))
    missing_rails = sorted([list(edge) for edge in forced - set(fresh.edges)])
    payload = {
        "version": 1,
        "source": str(source),
        "lp_json": str(args.lp_json),
        "alpha": args.alpha,
        "lp_delta": best["delta"],
        "lp_deaths": best["deaths"],
        "f_vector": [len(fresh.active), len(fresh.edges), len(fresh.faces)],
        "class": [len(fresh.stable), len(fresh.unstable), len(fresh.saddles)],
        "faces_match": fresh_faces == base_faces,
        "removed_faces": removed_faces,
        "added_faces": added_faces,
        "all_vertices_active": set(fresh.active) == set(points),
        "lost_vertices": lost_vertices,
        "all_forced_rails_present": forced <= set(fresh.edges),
        "missing_forced_rails": missing_rails,
        "topology_margin": fresh.topology_margin,
        "death_ratios": death_ratios,
        "missing_selected_guards": [
            {"key": repr(key), "kind": kind} for key, kind in missing_guards
        ],
        "minimum_signed_guard_ratio": float(guard_ratios[gi]) if gi is not None else None,
        "minimum_signed_guard": ({
            "key": repr(common_guards[gi][0]),
            "kind": common_guards[gi][2],
            "baseline_value": base_vals[common_guards[gi][0]],
            "new_value": vals[common_guards[gi][0]],
        } if gi is not None else None),
    }
    out = HERE / args.output
    write_csv(out.with_suffix(".csv"), candidate)
    out.with_suffix(".json").write_text(json.dumps(payload, indent=2))
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
