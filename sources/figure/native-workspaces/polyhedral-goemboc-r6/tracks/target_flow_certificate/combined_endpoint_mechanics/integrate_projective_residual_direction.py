#!/usr/bin/env python3
"""Integrate an LP direction as exact projective macromotion plus residual.

The full-chart LP directions are overwhelmingly common infinitesimal
projective/linear motions.  A direct Euler step needlessly bends the thin
Tutte cap and reaches support walls at alpha around 1e-3.  This integrator
least-squares splits the normalized direction into

  * 8 projective + trace-free symmetric-linear generators,
  * 7 mechanically irrelevant similarity generators, and
  * a pointwise residual.

Only the residual is stepped additively.  The common eight-dimensional part
is exponentiated exactly, so it preserves every projective incidence and the
entire hull lattice whenever all projective denominators remain positive.
The base and q246 wall are projected back to exact planes before the common
map; those corrections are second order in alpha.
"""
from __future__ import annotations

from pathlib import Path
import argparse
import ast
import csv
import json

import numpy as np
from scipy.linalg import expm

import combined_core
import combined_four_death_lp as four


HERE = Path(__file__).resolve().parent


def write_csv(path, points):
    with path.open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(("source_id", "x", "y", "z"))
        for row in sorted(points):
            writer.writerow((row, *(f"{float(x):.17g}" for x in points[row])))


def project_rows_to_plane(points, rows):
    rows = list(rows)
    cloud = points[rows]
    center = cloud.mean(axis=0)
    _u, _s, vh = np.linalg.svd(cloud - center, full_matrices=False)
    normal = vh[-1]
    points[rows] -= ((points[rows] - center) @ normal)[:, None] * normal


def project_point_to_plane(points, row, plane_rows):
    a, b, c = (points[i] for i in plane_rows)
    normal = np.cross(b - a, c - a)
    points[row] -= normal * (np.dot(normal, points[row] - a) / np.dot(normal, normal))


def generator_matrix(z):
    fields, names = [], []
    for axis in range(3):
        fields.append(-z * z[:, axis, None])
        names.append(f"pole_{axis}")
    h_basis = [
        np.asarray([[1, 0, 0], [0, 0, 0], [0, 0, -1]], float),
        np.asarray([[0, 1, 0], [1, 0, 0], [0, 0, 0]], float),
        np.asarray([[0, 0, 1], [0, 0, 0], [1, 0, 0]], float),
        np.asarray([[0, 0, 0], [0, 1, 0], [0, 0, -1]], float),
        np.asarray([[0, 0, 0], [0, 0, 1], [0, 1, 0]], float),
    ]
    for axis, h in enumerate(h_basis):
        fields.append(z @ h.T)
        names.append(f"tracefree_{axis}")
    for axis in range(3):
        field = np.zeros_like(z)
        field[:, axis] = 1.0
        fields.append(field)
        names.append(f"translation_{axis}")
    for axis, unit in enumerate(np.eye(3)):
        fields.append(np.cross(np.broadcast_to(unit, z.shape), z))
        names.append(f"rotation_{axis}")
    fields.append(z.copy())
    names.append("isotropic_scale")
    return np.column_stack([field.ravel() for field in fields]), fields, names


def audit_candidate(source_points, source_result, source_vals, candidate, deaths):
    fresh, vals = four.primitive_ledger(candidate)
    old_faces = {frozenset(face["cycle"]) for face in source_result.faces}
    new_faces = {frozenset(face["cycle"]) for face in fresh.faces}
    forced = combined_core.forced_rail_edges()
    guards = four.chosen_guards(source_vals)
    common = [(key, sign, kind) for key, sign, kind in guards if key in vals]
    ratios = [sign * vals[key] / (sign * source_vals[key]) for key, sign, _ in common]
    index = int(np.argmin(ratios)) if ratios else None
    return fresh, vals, {
        "f_vector": [len(fresh.active), len(fresh.edges), len(fresh.faces)],
        "class": [len(fresh.stable), len(fresh.unstable), len(fresh.saddles)],
        "faces_match": new_faces == old_faces,
        "removed_faces": sorted(
            (sorted(face) for face in old_faces - new_faces), key=lambda face: (len(face), face)
        ),
        "added_faces": sorted(
            (sorted(face) for face in new_faces - old_faces), key=lambda face: (len(face), face)
        ),
        "all_vertices_active": set(fresh.active) == set(source_points),
        "lost_vertices": sorted(set(source_points) - set(fresh.active)),
        "all_forced_rails_present": forced <= set(fresh.edges),
        "missing_forced_rails": sorted([list(edge) for edge in forced - set(fresh.edges)]),
        "topology_margin": fresh.topology_margin,
        "death_ratios": {
            repr(key): (float(vals[key] / source_vals[key]) if key in vals else None)
            for key in deaths
        },
        "minimum_signed_guard_ratio": float(ratios[index]) if index is not None else None,
        "minimum_signed_guard": ({
            "key": repr(common[index][0]),
            "kind": common[index][2],
            "baseline_value": source_vals[common[index][0]],
            "new_value": vals[common[index][0]],
        } if index is not None else None),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--lp-json", required=True)
    parser.add_argument("--alpha", type=float, required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    source = Path(args.source)
    source_points = four.load_points(source)
    source_result, source_vals = four.primitive_ledger(source_points)
    ids = sorted(source_points)
    p = np.asarray([source_points[i] for i in ids])
    modes, _, _ = four.chart_modes(source_points)
    lp = json.loads(Path(args.lp_json).read_text())
    best = min((row for row in lp["atlas"] if row.get("success")), key=lambda row: row["delta"])
    coeffs = np.asarray(best["coefficients"], dtype=float)
    direction = np.asarray([
        sum((coeffs[j] * mode[row] for j, mode in enumerate(modes)), start=np.zeros(3))
        for row in ids
    ])

    origin = p.mean(axis=0)
    scale = float(np.sqrt(np.mean(np.sum((p - origin) ** 2, axis=1))))
    z = (p - origin) / scale
    normalized_direction = direction / scale
    matrix, fields, names = generator_matrix(z)
    split_coeffs = np.linalg.lstsq(matrix, normalized_direction.ravel(), rcond=None)[0]
    fitted = (matrix @ split_coeffs).reshape(z.shape)
    residual = normalized_direction - fitted

    # Euler-step only the small non-common part, then restore both prescribed
    # coplanar faces exactly before applying the finite projective map.
    residual_points = z + args.alpha * residual
    row_index = {row: k for k, row in enumerate(ids)}
    project_rows_to_plane(residual_points, [row_index[row] for row in four.BASE])
    project_point_to_plane(
        residual_points, row_index[246], [row_index[row] for row in (7, 8, 245)]
    )

    theta = args.alpha * split_coeffs[:8]
    pole = theta[:3]
    denominator = 1.0 + residual_points @ pole
    if float(np.min(denominator)) <= 0.08:
        raise ValueError(f"projective denominator crossed: {float(np.min(denominator))}")
    a, b, c, d, e = theta[3:]
    h = np.asarray([[a, b, c], [b, d, e], [c, e, -a - d]], float)
    normalized_candidate = (residual_points / denominator[:, None]) @ expm(h).T
    # Return to the source similarity gauge.  Besides making dimensional face
    # ratios comparable, this keeps the evaluator's absolute grouping
    # tolerance in the same numerical regime as the source audit.
    candidate_array = origin + scale * normalized_candidate
    candidate = {row: candidate_array[k] for k, row in enumerate(ids)}

    deaths = [ast.literal_eval(key) for key in best["deaths"]]
    fresh, vals, fresh_audit = audit_candidate(
        source_points, source_result, source_vals, candidate, deaths
    )
    base_cloud = candidate_array[[row_index[row] for row in four.BASE]]
    base_singular = np.linalg.svd(base_cloud - base_cloud.mean(axis=0), compute_uv=False)
    qa, qb, qc, qq = (candidate[row] for row in (7, 8, 245, 246))
    quad_volume = float(np.linalg.det(np.column_stack((qb - qa, qc - qa, qq - qa))))
    point_displacements = np.linalg.norm(normalized_candidate - z, axis=1)
    payload = {
        "version": 1,
        "method": "exact finite projective+tracefree-linear map after planarity-restored residual Euler step",
        "source": str(source),
        "lp_json": args.lp_json,
        "alpha": args.alpha,
        "lp_delta": best["delta"],
        "lp_deaths": best["deaths"],
        "normalization_scale": scale,
        "split_coefficients": {name: float(value) for name, value in zip(names, split_coeffs)},
        "projective_theta": theta.tolist(),
        "minimum_projective_denominator": float(np.min(denominator)),
        "direction_l2_residual_fraction": float(
            np.linalg.norm(residual) / np.linalg.norm(normalized_direction)
        ),
        "maximum_normalized_full_direction": float(
            np.max(np.linalg.norm(normalized_direction, axis=1))
        ),
        "maximum_normalized_residual_direction": float(
            np.max(np.linalg.norm(residual, axis=1))
        ),
        "maximum_normalized_actual_displacement": float(np.max(point_displacements)),
        "base_planarity_smallest_singular_value": float(base_singular[-1]),
        "quad_oriented_volume": quad_volume,
        **fresh_audit,
    }
    out = HERE / args.output
    write_csv(out.with_suffix(".csv"), candidate)
    out.with_suffix(".json").write_text(json.dumps(payload, indent=2))
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
