#!/usr/bin/env python3
"""Materialize a saved metric-search theta with a full fresh candidate audit."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import materialize_row54_cells as material
import row54_four_residual_search as core


HERE = Path(__file__).resolve().parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default="row54_multiwall_flip.csv")
    ap.add_argument("--search", required=True)
    ap.add_argument("--prefix")
    args = ap.parse_args()
    source_path = HERE / args.source
    search_path = HERE / args.search
    prefix = args.prefix or search_path.stem
    ids, source = material.load_csv(source_path)
    search = json.load(search_path.open())
    points, den = core.transform(source, search["theta"])
    hull, faces, normals = core.group_maximal_faces(ids, points)
    mechanics, stable, unstable, saddles = core.classify(ids, points, faces)
    edges, _ = core.edge_lattice(faces)
    forced = material.forced_rail_edges()
    assert [len(hull.vertices), len(edges), len(faces)] == [61, 162, 103]
    assert forced <= set(edges)
    assert frozenset(core.BASE) in {frozenset(c) for c in faces}
    assert (0, 1) not in edges
    csv_name = prefix + ".csv"
    faces_name = prefix + "_faces.json"
    audit_name = prefix + "_audit.json"
    material.write_csv(HERE / csv_name, ids, points)
    json.dump(faces, (HERE / faces_name).open("w"), indent=2)
    margins = material.requested_margins(
        mechanics, faces, {core.BASE}, {8}, set()
    )
    topology = material.topology_audit(ids, points, faces, normals)
    record = {
        "version": 1,
        "source": args.source,
        "search": args.search,
        "coordinates": csv_name,
        "fixed_expected_faces": faces_name,
        "theta": search["theta"],
        "transform_convention": (
            "z=(p-mean(source))/rms_radius(source); den=1+pole.z; "
            "y=(z/den)@expm(H).T"
        ),
        "minimum_projective_denominator": float(min(den)),
        "fresh_hull_audit": {
            "f_vector": [len(hull.vertices), len(edges), len(faces)],
            "active": mechanics["active"],
            "centroid": mechanics["centroid"].tolist(),
            "class": [len(stable), len(unstable), len(saddles)],
            "stable_faces": stable,
            "unstable_vertices": unstable,
            "saddle_edges": saddles,
            "all_forced_rail_edges_present": forced <= set(edges),
            "forced_rail_edges": [list(e) for e in sorted(forced)],
            "edge_0_1_present": (0, 1) in edges,
        },
        "all_target_mechanics_margins": margins,
        "topology_audit": topology,
    }
    json.dump(record, (HERE / audit_name).open("w"), indent=2)
    print(json.dumps({
        "coordinates": csv_name,
        "audit": audit_name,
        "f_vector": record["fresh_hull_audit"]["f_vector"],
        "class": record["fresh_hull_audit"]["class"],
        "hard_target_margin": margins["hard_requested_margin"],
        "worst": sorted(
            margins["records"], key=lambda row: row["requested_signed_margin"]
        )[:8],
        "topology_min": topology["minimum_nonface_support_slack"],
    }, indent=2))


if __name__ == "__main__":
    main()
