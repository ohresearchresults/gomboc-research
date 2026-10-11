#!/usr/bin/env python3
"""Locate an exact circuit wall along a predictor with saved nullspace offset."""
from __future__ import annotations

from pathlib import Path
import argparse
import ast
import json

import numpy as np
from scipy.optimize import brentq

import combined_four_death_lp as four
import combined_rank6_scan as rank6
from integrate_four_death_direction import write_csv
from locate_adjacent_wall import audit
from reverse_wall_bypass import oriented_volume


HERE = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--lp-json", required=True)
    parser.add_argument("--offset-json", required=True)
    parser.add_argument("--circuit", required=True)
    parser.add_argument("--left", type=float, required=True)
    parser.add_argument("--right", type=float, required=True)
    parser.add_argument("--epsilon", type=float, default=1e-7)
    parser.add_argument("--after-epsilon", type=float)
    parser.add_argument("--plane-tol", type=float, default=1e-13)
    parser.add_argument("--prefix", required=True)
    args = parser.parse_args()

    circuit = tuple(int(x) for x in args.circuit.split(","))
    if len(circuit) != 4:
        raise ValueError("--circuit requires four ids")
    points = four.load_points(args.source)
    modes, _meta, _chart = four.chart_modes(points)
    lp = json.loads(Path(args.lp_json).read_text())
    candidates = [
        row for row in lp["atlas"]
        if row.get("success")
        and ast.literal_eval(row["deaths"][2])[2] == "one_minus_t"
        and ast.literal_eval(row["deaths"][3])[2] == "t"
    ]
    best = min(candidates, key=lambda row: row["delta"])
    direction = np.asarray(best["coefficients"], dtype=float)
    offset_payload = json.loads(Path(args.offset_json).read_text())
    offset = np.asarray(offset_payload["cumulative_control_coefficients"], dtype=float)

    def candidate(alpha):
        return rank6.apply_modes(points, modes, alpha * direction + offset)

    def volume(alpha):
        return oriented_volume(candidate(alpha), circuit)

    vl, vr = volume(args.left), volume(args.right)
    if vl * vr >= 0:
        raise RuntimeError(f"circuit is not bracketed: {vl}, {vr}")
    root = float(brentq(volume, args.left, args.right, xtol=1e-15, rtol=1e-14))
    after_epsilon = args.epsilon if args.after_epsilon is None else args.after_epsilon
    samples = {
        "before": candidate(root - args.epsilon),
        "at": candidate(root),
        "after": candidate(root + after_epsilon),
    }
    prefix = HERE / args.prefix
    for name, sample in samples.items():
        write_csv(prefix.with_name(prefix.name + f"_{name}.csv"), sample)

    payload = {
        "version": 1,
        "source": args.source,
        "lp_json": args.lp_json,
        "offset_json": args.offset_json,
        "lp_delta": best["delta"],
        "circuit": list(circuit),
        "bracket": [args.left, args.right],
        "volume_bracket": [vl, vr],
        "alpha_wall": root,
        "epsilon": args.epsilon,
        "after_epsilon": after_epsilon,
        "volume_at_wall": volume(root),
        "plane_tolerance": args.plane_tol,
        "before": audit(samples["before"], circuit, args.plane_tol),
        "at": audit(samples["at"], circuit, args.plane_tol),
        "after": audit(samples["after"], circuit, args.plane_tol),
        "csv": {
            name: prefix.name + f"_{name}.csv" for name in samples
        },
    }
    prefix.with_suffix(".json").write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
