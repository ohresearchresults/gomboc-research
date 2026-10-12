#!/usr/bin/env python3
"""Fresh-hull nonlinear sweep of the radius-1 guarded baseline direction."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("guarded", HERE / "baseline_guarded_lp.py")
guarded = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(guarded)


def signature(res):
    if not res.valid:
        return ("INVALID", res.error)
    stable = tuple(sorted(tuple(sorted(res.faces[i]["cycle"])) for i, _ in res.stable))
    unstable = tuple(sorted(i for i, _ in res.unstable))
    saddles = tuple(sorted(e for e, _ in res.saddles))
    return (
        (len(res.active), len(res.edges), len(res.faces)),
        (len(stable), len(unstable), len(saddles)),
        stable,
        unstable,
        saddles,
    )


def main():
    base = guarded.load_points()
    r0, _ = guarded.primitive_ledger(base)
    modes, _ = guarded.build_modes(base, r0)
    trust = json.loads((HERE / "trust_region_sensitivity.json").read_text())
    rec = next(r for r in trust["records"] if r.get("radius_linf_coordinate") == 1.0)
    coeff = np.asarray(rec["coefficients"])
    direction = {i: sum((coeff[j] * modes[j][i] for j in range(len(modes))), start=np.zeros(3)) for i in base}
    records = []
    previous = None
    transitions = []
    for t in np.linspace(0.0, 1.3, 521):
        pts = {i: base[i] + float(t) * direction[i] for i in base}
        res = guarded.evaluate(pts, plane_tol=1e-8, qhull_options="Qt Qx", strict_tol=1e-10)
        sig = signature(res)
        if sig != previous:
            transitions.append({"t": float(t), "signature": repr(sig), "error": res.error})
            previous = sig
        if res.valid:
            score, detail = guarded.score_target(res)
            records.append(
                {
                    "t": float(t),
                    "f_vector": [len(res.active), len(res.edges), len(res.faces)],
                    "class": [len(res.stable), len(res.unstable), len(res.saddles)],
                    "hard_score": score,
                    "detail": detail,
                    "topology_margin": res.topology_margin,
                    "stable_faces": [res.faces[i]["cycle"] for i, _ in res.stable],
                    "unstable_vertices": [i for i, _ in res.unstable],
                    "saddle_edges": [list(e) for e, _ in res.saddles],
                }
            )
        else:
            records.append({"t": float(t), "valid": False, "error": res.error})
    out = {
        "version": 1,
        "source_record": rec,
        "maximum_coordinate_displacement_at_t1": max(float(np.max(np.abs(v))) for v in direction.values()),
        "transitions": transitions,
        "samples": records,
    }
    (HERE / "baseline_trust_path.json").write_text(json.dumps(out, indent=2))
    print("max displacement", out["maximum_coordinate_displacement_at_t1"])
    for tr in transitions:
        print("transition", tr["t"], tr["signature"][:1000])
    best = max((r for r in records if r.get("valid", True)), key=lambda r: r.get("hard_score", -1e100))
    print("best", best["t"], best["hard_score"], best["class"], best["detail"])


if __name__ == "__main__":
    main()
