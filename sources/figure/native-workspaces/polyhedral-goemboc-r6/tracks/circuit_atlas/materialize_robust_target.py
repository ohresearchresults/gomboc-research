#!/usr/bin/env python3
"""Materialize and independently re-audit the rebuilt strict robust target."""
from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np

import row54_four_residual_search as core

HERE = Path(__file__).resolve().parent


def main():
    rows = {}
    with (HERE / "target_sphere_rebuilt.csv").open() as f:
        for r in csv.DictReader(f):
            rows[int(r["source_id"])] = np.array([float(r[k]) for k in ("x", "y", "z")])
    ids = sorted(rows)
    raw = np.array([rows[i] for i in ids])
    search = json.load((HERE / "robust_rebuilt_fast.json").open())
    theta = np.asarray(search["theta"], dtype=float)
    points, den = core.transform(raw, theta)
    audit, faces, mechanics = core.fresh_audit(ids, points, json.load((HERE / "target_sphere_rebuilt_faces.json").open()))
    assert audit["f_vector"] == [61, 163, 104]
    assert audit["class"] == [2, 2, 2]
    assert {frozenset(c) for c in audit["stable_faces"]} == {
        frozenset(range(17)), frozenset((8, 245, 246))
    }
    assert audit["unstable_vertices"] == [1, 8]
    assert {tuple(e) for e in audit["saddle_edges"]} == {(6, 7), (9, 10)}
    with (HERE / "robust_target_rebuilt.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source_id", "x", "y", "z"])
        for i, p in zip(ids, points):
            w.writerow([i, *[format(float(q), ".17g") for q in p]])
    json.dump(faces, (HERE / "robust_target_rebuilt_faces.json").open("w"), indent=2)
    record = {
        "version": 1,
        "source": "target_sphere_rebuilt.csv",
        "search": "robust_rebuilt_fast.json",
        "transform_convention": "z=(p-mean(p))/rms_radius; d=1+theta[0:3].z; y=expm(H)@(z/d), H=[[a,b,c],[b,d,e],[c,e,-a-d]] from theta[3:8]",
        "theta": theta.tolist(),
        "minimum_projective_denominator": float(np.min(den)),
        "requested_hard_margin": search["requested_hard_margin"],
        "worst_requested_guards": search["worst_requested_guards"],
        "fresh_hull_audit": audit,
        "fixed_expected_faces": "robust_target_rebuilt_faces.json",
    }
    json.dump(record, (HERE / "robust_target_rebuilt_audit.json").open("w"), indent=2)
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
