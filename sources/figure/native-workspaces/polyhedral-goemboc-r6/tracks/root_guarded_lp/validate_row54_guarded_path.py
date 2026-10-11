#!/usr/bin/env python3
"""Fresh-hull nonlinear validation of the best row54 guarded-LP direction."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

import numpy as np
from scipy.linalg import expm

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("row54_lp", HERE / "row54_guarded_lp.py")
lpmod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(lpmod)


def decompose(base, modes, meta, coefficients):
    additive = {i: np.zeros(3) for i in base}
    linear = np.zeros((3, 3))
    pole = np.zeros(3)
    for mode, record, coefficient in zip(modes, meta, coefficients):
        if record["kind"] == "linear":
            a, b = record["output_axis"], record["input_axis"]
            ratios = [mode[i][a] / base[i][b] for i in base if abs(base[i][b]) > 1e-9]
            factor = float(np.median(ratios))
            assert max(abs(z - factor) for z in ratios) < 1e-10 * max(1.0, abs(factor))
            linear[a, b] += coefficient * factor
        elif record["kind"] == "projective":
            a = record["axis"]
            ratios = []
            for i in base:
                if abs(base[i][a]) <= 1e-9:
                    continue
                k = int(np.argmax(np.abs(base[i])))
                if abs(base[i][k]) <= 1e-9:
                    continue
                ratios.append(-mode[i][k] / (base[i][k] * base[i][a]))
            factor = float(np.median(ratios))
            assert max(abs(z - factor) for z in ratios) < 1e-10 * max(1.0, abs(factor))
            pole[a] += coefficient * factor
        else:
            for i in base:
                additive[i] += coefficient * mode[i]
    return additive, linear, pole


def realize(base, additive, linear, pole, t):
    q = {i: base[i] + t * additive[i] for i in base}
    den = {i: 1.0 + t * float(np.dot(pole, q[i])) for i in base}
    if min(den.values()) <= 0:
        raise ValueError(("projective denominator", min(den.values())))
    transform = expm(t * linear)
    return {i: transform @ (q[i] / den[i]) for i in base}, min(den.values())


def forced_rails():
    short = [228] + list(range(229, 247)) + [8]
    long = [228] + list(range(247, 265)) + [8]
    edges = {
        tuple(sorted(edge))
        for path in (short, long)
        for edge in zip(path, path[1:])
    }
    edges.remove((228, 229))
    return edges


def record(t, points, denominator):
    try:
        result, _ = lpmod.baseline.primitive_ledger(points)
    except Exception as exc:
        return {"t": float(t), "valid": False, "error": repr(exc),
                "minimum_projective_denominator": float(denominator)}
    stable = [sorted(result.faces[i]["cycle"]) for i, _ in result.stable]
    unstable = [i for i, _ in result.unstable]
    saddles = [list(edge) for edge, _ in result.saddles]
    return {
        "t": float(t),
        "valid": True,
        "f_vector": [len(result.active), len(result.edges), len(result.faces)],
        "class": [len(stable), len(unstable), len(saddles)],
        "stable_faces": stable,
        "unstable_vertices": unstable,
        "saddle_edges": saddles,
        "topology_margin": float(result.topology_margin),
        "all_forced_rails": forced_rails() <= set(result.edges),
        "base_present": lpmod.BASE_FACE in {frozenset(face["cycle"]) for face in result.faces},
        "minimum_projective_denominator": float(denominator),
    }


def signature(item):
    if not item["valid"]:
        return ("invalid", item["error"])
    return (
        tuple(item["f_vector"]), tuple(item["class"]),
        tuple(tuple(face) for face in item["stable_faces"]),
        tuple(item["unstable_vertices"]), tuple(tuple(edge) for edge in item["saddle_edges"]),
        item["all_forced_rails"], item["base_present"],
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="row54_guarded_lp_bound20.json")
    ap.add_argument("--tmax", type=float, default=1.2)
    ap.add_argument("--steps", type=int, default=121)
    ap.add_argument("--output", default="row54_guarded_path.json")
    args = ap.parse_args()
    source = json.loads((HERE / args.input).read_text())
    best = source["atlas"][0]
    base = lpmod.load_points()
    result, _ = lpmod.baseline.primitive_ledger(base)
    modes, meta = lpmod.build_modes(base, result)
    coefficients = np.asarray(best["coefficients"], dtype=float)
    additive, linear, pole = decompose(base, modes, meta, coefficients)
    times = np.unique(np.r_[
        0.0,
        np.geomspace(1e-9, 1e-2, 22),
        np.linspace(0.0125, args.tmax, args.steps),
    ])
    samples = []
    events = []
    old = None
    for t in times:
        try:
            points, denominator = realize(base, additive, linear, pole, float(t))
            item = record(t, points, denominator)
        except Exception as exc:
            item = {"t": float(t), "valid": False, "error": repr(exc)}
        samples.append(item)
        sig = signature(item)
        if sig != old:
            events.append(item)
            old = sig
            print("EVENT", json.dumps(item, sort_keys=True), flush=True)
    winners = [item for item in samples if item.get("class") == [1, 1, 0]]
    output = {
        "version": 1,
        "source": args.input,
        "linear_lp_delta": best["delta"],
        "linear_lp_deaths": best["deaths"],
        "linear_lp_max_coordinate_displacement": best["max_coordinate_displacement"],
        "integrated_linear_generator": linear.tolist(),
        "integrated_projective_pole": pole.tolist(),
        "events": events,
        "samples": samples,
        "winner_samples": winners,
    }
    (HERE / args.output).write_text(json.dumps(output, indent=2))
    print("events", len(events), "winners", len(winners), flush=True)


if __name__ == "__main__":
    main()
