#!/usr/bin/env python3
"""Diagnose near-parallel true-edge cones without invoking the primitive ledger.

The continuation ledger historically aborts when the Gram determinant of two
unit face normals is at most 1e-14.  This diagnostic rebuilds the actual hull,
records the smallest determinants and checks the complete face/equilibrium
signature on both sides of one intrinsic chart column.  It never substitutes
a derivative or changes the continuation state.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import build_u54_material_exact_path as exact_path
import combined_four_death_lp as four
import post_flip_trust_slp as slp


def snapshot(points, plane_tol):
    result = exact_path.actual.evaluate(points, coplanar_rel=plane_tol)
    if not result.valid:
        return {"valid": False, "error": result.error}
    faces = slp.face_signature(result)
    equilibria = slp.equilibrium_signature(result)
    face_by_index = {index: face for index, face in enumerate(result.faces)}
    cones = []
    for edge in result.edges:
        incident = result.edge_faces[edge]
        n1 = np.asarray(face_by_index[incident[0]]["n"], dtype=np.longdouble)
        n2 = np.asarray(face_by_index[incident[1]]["n"], dtype=np.longdouble)
        aa = np.dot(n1, n1)
        bb = np.dot(n1, n2)
        cc = np.dot(n2, n2)
        determinant = aa * cc - bb * bb
        cones.append({
            "edge": list(edge),
            "incident_faces": [
                sorted(face_by_index[index]["cycle"]) for index in incident
            ],
            "gram_determinant": float(determinant),
        })
    cones.sort(key=lambda row: row["gram_determinant"])
    return {
        "valid": True,
        "f_vector": [len(result.active), len(result.edges), len(result.faces)],
        "class": [len(result.stable), len(result.unstable), len(result.saddles)],
        "face_signature": [list(face) for face in faces],
        "equilibrium_signature": equilibria,
        "minimum_cones": cones[:12],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--column", type=int, required=True)
    parser.add_argument("--plane-tol", type=float, default=2e-12)
    parser.add_argument(
        "--steps",
        default="1e-9,2.5e-10,6.25e-11,1.5625e-11,3.90625e-12,9.765625e-13,2.44140625e-13,6.103515625e-14,1.52587890625e-14",
    )
    parser.add_argument("--output", default="intrinsic_fd_conditioning.json")
    args = parser.parse_args()

    source = Path(args.source)
    if not source.is_absolute():
        source = HERE / source
    points = slp.load_exact_float(source)
    modes, metadata, chart = four.chart_modes(points)
    if not 0 <= args.column < len(modes):
        raise ValueError((args.column, len(modes)))

    baseline = snapshot(points, args.plane_tol)
    probes = []
    for step in (float(text) for text in args.steps.split(",")):
        delta = np.zeros(len(modes))
        delta[args.column] = step
        plus = snapshot(slp.apply_modes(points, modes, delta), args.plane_tol)
        minus = snapshot(slp.apply_modes(points, modes, -delta), args.plane_tol)
        probes.append({"step": step, "plus": plus, "minus": minus})

    payload = {
        "version": 1,
        "scope": "intrinsic central-difference conditioning diagnostic",
        "source": str(source),
        "column": args.column,
        "mode": metadata[args.column],
        "chart": chart,
        "baseline": baseline,
        "probes": probes,
    }
    output = HERE / args.output
    output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "mode": payload["mode"],
        "baseline_minimum": baseline.get("minimum_cones", [])[:3],
        "probe_minima": [
            {
                "step": row["step"],
                "plus": row["plus"].get("minimum_cones", [])[:3],
                "minus": row["minus"].get("minimum_cones", [])[:3],
            }
            for row in probes
        ],
        "output": str(output),
    }, indent=2))


if __name__ == "__main__":
    main()
