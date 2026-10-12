#!/usr/bin/env python3
"""Fresh-hull summary of the nonlinear four-death integration path."""
from __future__ import annotations

from pathlib import Path
import argparse
import json

import numpy as np

import combined_core
import combined_four_death_lp as four


HERE = Path(__file__).resolve().parent


def face_set(result):
    return {frozenset(face["cycle"]) for face in result.faces}


def mechanics(result, values):
    quad_index = next(
        i for i, face in enumerate(result.faces)
        if frozenset(face["cycle"]) == four.QUAD
    )
    out = {
        "quad": float(result.face_decisions[quad_index]),
        "quad_edge_8_246": float(values[("face", tuple(sorted(four.QUAD)), (8, 246))]),
        "u54": float(result.vertex_decisions[54]),
        "u54_neighbor1": float(values[("vertex", 54, 1)]),
        "h67": float(result.edge_decisions[(6, 7)]),
        "h910": float(result.edge_decisions[(9, 10)]),
        "base": float(result.face_decisions[next(
            i for i, face in enumerate(result.faces)
            if frozenset(face["cycle"]) == four.BASE
        )]),
        "u8": float(result.vertex_decisions[8]),
    }
    for edge, label in [((6, 7), "h67"), ((9, 10), "h910")]:
        out[label + "_components"] = {
            component: float(values[("edge", edge, component)])
            for component in ("t", "one_minus_t", "beta1", "beta2")
        }
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="combined_nonlinear_path_summary")
    parser.add_argument("files", nargs="+")
    args = parser.parse_args()

    forced = combined_core.forced_rail_edges()
    rows = []
    reference_points = None
    reference_faces = None
    reference_mechanics = None
    for filename in args.files:
        path = Path(filename)
        points = four.load_points(path)
        try:
            result, values = four.primitive_ledger(points)
        except Exception as exc:
            rows.append({"file": str(path), "valid": False, "error": repr(exc)})
            continue
        current_faces = face_set(result)
        current_mechanics = mechanics(result, values)
        if reference_points is None:
            reference_points = points
            reference_faces = current_faces
            reference_mechanics = current_mechanics
        displacement = {
            i: float(np.linalg.norm(points[i] - reference_points[i])) for i in points
        }
        h67_ratios = {
            key: current_mechanics["h67_components"][key] / reference_mechanics["h67_components"][key]
            for key in current_mechanics["h67_components"]
        }
        h910_ratios = {
            key: current_mechanics["h910_components"][key] / reference_mechanics["h910_components"][key]
            for key in current_mechanics["h910_components"]
        }
        residual_ratios = {
            "quad": current_mechanics["quad"] / reference_mechanics["quad"],
            "u54": current_mechanics["u54"] / reference_mechanics["u54"],
            "h67": min(h67_ratios.values()),
            "h910": min(h910_ratios.values()),
        }
        rows.append({
            "file": str(path),
            "valid": True,
            "f_vector": [len(result.active), len(result.edges), len(result.faces)],
            "class": [len(result.stable), len(result.unstable), len(result.saddles)],
            "all_vertices_active": len(result.active) == len(points),
            "all_forced_rails_present": forced <= set(result.edges),
            "topology_margin": result.topology_margin,
            "faces_match_reference": current_faces == reference_faces,
            "removed_faces": sorted(
                (sorted(face) for face in reference_faces - current_faces),
                key=lambda face: (len(face), face),
            ),
            "added_faces": sorted(
                (sorted(face) for face in current_faces - reference_faces),
                key=lambda face: (len(face), face),
            ),
            "mechanics": current_mechanics,
            "h67_component_ratios": h67_ratios,
            "h910_component_ratios": h910_ratios,
            "h67_best_branch": min(h67_ratios, key=h67_ratios.get),
            "h910_best_branch": min(h910_ratios, key=h910_ratios.get),
            "residual_ratios": residual_ratios,
            "largest_residual_ratio": max(residual_ratios.values()),
            "max_point_displacement_from_reference": max(displacement.values()),
            "max_displacement_row": max(displacement, key=displacement.get),
        })

    payload = {
        "version": 1,
        "scope": "fresh-hull nonlinear four-death integration audit",
        "reference": args.files[0],
        "rows": rows,
    }
    prefix = HERE / args.output
    prefix.with_suffix(".json").write_text(json.dumps(payload, indent=2))

    md = [
        "# Nonlinear four-death path audit",
        "",
        "All rows below are rebuilt with a fresh hull; residual ratios are relative to the first row.",
        "",
        "| file | f-vector | class | topology margin | quad | U54 | H67 | H910 | worst ratio | max displacement |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        if not row.get("valid"):
            md.append(f"| {Path(row['file']).name} | invalid |  |  |  |  |  |  |  |  |")
            continue
        ratio = row["residual_ratios"]
        md.append(
            f"| {Path(row['file']).name} | {tuple(row['f_vector'])} | {tuple(row['class'])} | "
            f"{row['topology_margin']:.3e} | {ratio['quad']:.9f} | {ratio['u54']:.9f} | "
            f"{ratio['h67']:.9f} | {ratio['h910']:.9f} | {row['largest_residual_ratio']:.9f} | "
            f"{row['max_point_displacement_from_reference']:.5g} |"
        )
    prefix.with_suffix(".md").write_text("\n".join(md) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
