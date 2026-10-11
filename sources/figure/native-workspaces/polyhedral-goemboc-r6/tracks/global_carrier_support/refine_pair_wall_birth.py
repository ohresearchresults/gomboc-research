#!/usr/bin/env python3
"""Refine the first two births on the saved pair-wall continuation segment."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
from actual_hull_mechanics import evaluate  # noqa: E402
from optimize_base_escape import Search  # noqa: E402
from search_row54_remote228 import load_points, summarize  # noqa: E402


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--continuation", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--iterations", type=int, default=52)
    args = parser.parse_args()

    labels, source = load_points(args.source)
    audit = json.loads(args.audit.read_text())
    rails = {
        tuple(sorted(edge))
        for edge in audit["fresh_hull_audit"]["forced_rail_edges"]
    }
    search = Search(labels, source, rails, report=False)
    continuation = json.loads(args.continuation.read_text())
    p0 = np.asarray(continuation["accepted"][0]["parameters"], dtype=float)
    p1 = np.asarray(continuation["accepted"][1]["parameters"], dtype=float)

    features = (
        ("stable_face", (8, 245, 246)),
        ("saddle_edge", (8, 245)),
    )

    def sample(alpha):
        parameters = p0 + alpha * (p1 - p0)
        points = search.coordinates(parameters)
        mechanics = evaluate(labels, points)
        summary = summarize(labels, points, rails)
        decisions = {
            "stable_face:[8,245,246]": mechanics.face_decisions[(8, 245, 246)],
            "saddle_edge:[8,245]": mechanics.edge_decisions[(8, 245)],
        }
        return parameters, decisions, summary

    roots = []
    for kind, key in features:
        name = f"{kind}:[{','.join(str(x) for x in key)}]"
        lo, hi = 0.0, 0.1
        _, lo_values, _ = sample(lo)
        _, hi_values, _ = sample(hi)
        if not (lo_values[name] < 0.0 < hi_values[name]):
            raise ValueError((name, lo_values[name], hi_values[name]))
        for _ in range(args.iterations):
            mid = (lo + hi) / 2.0
            _, values, _ = sample(mid)
            if values[name] > 0.0:
                hi = mid
            else:
                lo = mid
        alpha = (lo + hi) / 2.0
        parameters, values, summary = sample(alpha)
        roots.append({
            "feature": name,
            "alpha_lo": lo,
            "alpha_hi": hi,
            "alpha": alpha,
            "decision_at_alpha": values[name],
            "all_pair_birth_decisions": values,
            "parameters": parameters.tolist(),
            "summary_at_numerical_root": {
                "class": summary["class"],
                "f_vector": summary["f_vector"],
                "stable_faces": summary["stable_faces"],
                "unstable_vertices": summary["unstable_vertices"],
                "saddle_edges": summary["saddle_edges"],
                "base_face_present": summary["base_face_present"],
                "missing_forced_rails": summary["missing_forced_rails"],
            },
        })

    roots.sort(key=lambda row: row["alpha"])
    for left, right in zip(roots, roots[1:]):
        midpoint = (left["alpha"] + right["alpha"]) / 2.0
        _, values, summary = sample(midpoint)
        left["next_root"] = right["feature"]
        left["open_interval_midpoint"] = {
            "alpha": midpoint,
            "decisions": values,
            "class": summary["class"],
            "stable_faces": summary["stable_faces"],
            "unstable_vertices": summary["unstable_vertices"],
            "saddle_edges": summary["saddle_edges"],
            "base_face_present": summary["base_face_present"],
            "missing_forced_rails": summary["missing_forced_rails"],
        }

    payload = {
        "version": 1,
        "scope": "bisection of first actual-hull birth decisions on continuation segment 1",
        "source": str(args.source.resolve()),
        "continuation": str(args.continuation.resolve()),
        "iterations": args.iterations,
        "roots_in_order": roots,
        "alpha_separation": roots[1]["alpha"] - roots[0]["alpha"],
        "interpretation": (
            "first supporting wall on this template is the first listed birth; "
            "the targeted S(7,8,245)/H(9,10) decisions are still positive there"
        ),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
