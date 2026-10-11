#!/usr/bin/env python3
"""Locate and audit the first actual-cell wall along a saved LP direction.

The observed transition at step002 is the diagonal exchange on the four
vertices {198, 228, 229, 258}.  Its exact wall parameter is the zero of their
oriented volume; this is numerically much better conditioned than asking
Qhull to classify a nearly coplanar quadruple during bisection.
"""
from __future__ import annotations

from pathlib import Path
import argparse
import ast
import csv
import json

import numpy as np
from scipy.optimize import brentq
from scipy.spatial import ConvexHull

import combined_four_death_lp as four
import combined_rank6_scan as rank6


HERE = Path(__file__).resolve().parent
CIRCUIT = (198, 228, 229, 258)


def face_sets(result):
    return {frozenset(face["cycle"]) for face in result.faces}


def audit(points, circuit, plane_tol):
    result = four.baseline.evaluate(
        points, plane_tol=plane_tol, qhull_options="Qt Qx", strict_tol=1e-12
    )
    if not result.valid:
        # Near a true support wall the mechanical evaluator can reject an
        # otherwise perfectly good hull because adjacent face normals are
        # almost parallel.  Preserve a fresh hull-only audit in that band.
        ids = sorted(points)
        cloud = np.asarray([points[i] for i in ids])
        hull = ConvexHull(cloud, qhull_options="Qt Qx")
        namespace = four.baseline.evaluate.__globals__
        groups = namespace["_group_facets"](hull, cloud, plane_tol)
        faces = []
        for group in groups:
            cycle_local = namespace["_boundary_cycle"](
                group["tris"], group["n"], cloud
            )
            faces.append([ids[i] for i in cycle_local])
        edges = {
            tuple(sorted((a, b)))
            for face in faces
            for a, b in zip(face, face[1:] + face[:1])
        }
        active = {ids[i] for i in hull.vertices}
        topology = []
        for group, face in zip(groups, faces):
            values = -(cloud @ group["n"] + group["off"])
            face_set = set(face)
            topology.extend(values[k] for k, row in enumerate(ids) if row not in face_set)
        cset = frozenset(circuit)
        return {
            "valid": True,
            "mechanics_valid": False,
            "mechanics_error": result.error,
            "f_vector": [len(active), len(edges), len(faces)],
            "class": None,
            "circuit_faces": sorted(
                [sorted(face) for face in map(frozenset, faces) if len(face & cset) >= 3]
            ),
            "topology_margin": float(min(topology)),
        }
    faces = face_sets(result)
    return {
        "valid": True,
        "mechanics_valid": True,
        "f_vector": [len(result.active), len(result.edges), len(result.faces)],
        "class": [len(result.stable), len(result.unstable), len(result.saddles)],
        "circuit_faces": sorted(
            [sorted(face) for face in faces if len(face & frozenset(circuit)) >= 3]
        ),
        "topology_margin": result.topology_margin,
    }


def write_csv(path, points):
    with path.open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(("source_id", "x", "y", "z"))
        for row in sorted(points):
            writer.writerow((row, *(f"{float(x):.17g}" for x in points[row])))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--lp-json", required=True)
    parser.add_argument("--left", type=float, required=True)
    parser.add_argument("--right", type=float, required=True)
    parser.add_argument("--prefix", required=True)
    parser.add_argument("--epsilon", type=float)
    parser.add_argument("--plane-tol", type=float, default=1e-8)
    parser.add_argument("--h67-branch")
    parser.add_argument("--h910-branch")
    parser.add_argument(
        "--circuit",
        default=",".join(map(str, CIRCUIT)),
        help="four comma-separated vertex ids",
    )
    args = parser.parse_args()

    circuit = tuple(int(x) for x in args.circuit.split(","))
    if len(circuit) != 4:
        raise ValueError("--circuit must contain four ids")
    points = four.load_points(args.source)
    modes, _, _ = four.chart_modes(points)
    lp = json.loads(Path(args.lp_json).read_text())
    candidates = [row for row in lp["atlas"] if row.get("success")]
    if args.h67_branch is not None:
        candidates = [
            row for row in candidates
            if ast.literal_eval(row["deaths"][2])[2] == args.h67_branch
        ]
    if args.h910_branch is not None:
        candidates = [
            row for row in candidates
            if ast.literal_eval(row["deaths"][3])[2] == args.h910_branch
        ]
    if not candidates:
        raise ValueError("requested saddle-component branch is absent from LP atlas")
    best = min(candidates, key=lambda row: row["delta"])
    coeffs = np.asarray(best["coefficients"], dtype=float)

    def candidate(alpha):
        return rank6.apply_modes(points, modes, alpha * coeffs)

    def volume(alpha):
        p = candidate(alpha)
        a, b, c, d = (p[i] for i in circuit)
        return float(np.linalg.det(np.column_stack((b - a, c - a, d - a))))

    vl, vr = volume(args.left), volume(args.right)
    if vl * vr >= 0:
        raise ValueError(f"wall not bracketed: volume(left)={vl}, volume(right)={vr}")
    root = float(brentq(volume, args.left, args.right, xtol=1e-15, rtol=1e-14))
    width = args.right - args.left
    # Move far enough away that the evaluator's deliberate plane grouping
    # tolerance no longer reports the wall quad on both sides.
    epsilon = args.epsilon if args.epsilon is not None else max(1e-2 * width, 1e-7)
    before = candidate(root - epsilon)
    at = candidate(root)
    after = candidate(root + epsilon)
    prefix = HERE / args.prefix
    write_csv(prefix.with_name(prefix.name + "_before.csv"), before)
    write_csv(prefix.with_name(prefix.name + "_at.csv"), at)
    write_csv(prefix.with_name(prefix.name + "_after.csv"), after)
    payload = {
        "version": 1,
        "source": args.source,
        "lp_json": args.lp_json,
        "lp_deaths": best["deaths"],
        "circuit": list(circuit),
        "bracket": [args.left, args.right],
        "volume_bracket": [vl, vr],
        "alpha_wall": root,
        "epsilon": epsilon,
        "volume_at_wall": volume(root),
        "plane_tolerance": args.plane_tol,
        "before": audit(before, circuit, args.plane_tol),
        "at": audit(at, circuit, args.plane_tol),
        "after": audit(after, circuit, args.plane_tol),
    }
    prefix.with_suffix(".json").write_text(json.dumps(payload, indent=2))
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
