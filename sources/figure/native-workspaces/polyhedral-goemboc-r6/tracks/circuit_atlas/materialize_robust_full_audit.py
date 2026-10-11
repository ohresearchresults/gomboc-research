#!/usr/bin/env python3
"""Write the complete mechanics/topology audit for robust_target_rebuilt.csv."""
from __future__ import annotations

import json

import numpy as np

import materialize_row54_cells as material
import row54_four_residual_search as core


HERE = material.HERE


def main():
    ids, points = material.load_csv(HERE / "robust_target_rebuilt.csv")
    hull, faces, normals = core.group_maximal_faces(ids, points)
    mechanics, stable, unstable, saddles = core.classify(ids, points, faces)
    edges, _ = core.edge_lattice(faces)
    expected_stable = {core.BASE_ORIGINAL, core.F0}
    expected_unstable = {1, 8}
    expected_saddles = {(6, 7), (9, 10)}
    assert [len(hull.vertices), len(edges), len(faces)] == [61, 163, 104]
    assert {frozenset(c) for c in stable} == expected_stable
    assert set(unstable) == expected_unstable
    assert {tuple(e) for e in saddles} == expected_saddles
    fixed_faces = json.load((HERE / "robust_target_rebuilt_faces.json").open())
    assert {frozenset(c) for c in faces} == {frozenset(c) for c in fixed_faces}
    theta_record = json.load((HERE / "robust_target_rebuilt_audit.json").open())
    topology = material.topology_audit(ids, points, faces, normals)
    margins = material.requested_margins(
        mechanics, faces, expected_stable, expected_unstable, expected_saddles
    )
    record = {
        "version": 1,
        "coordinates": "robust_target_rebuilt.csv",
        "fixed_expected_faces": "robust_target_rebuilt_faces.json",
        "source": theta_record["source"],
        "search": theta_record["search"],
        "transform_convention": theta_record["transform_convention"],
        "theta": theta_record["theta"],
        "minimum_projective_denominator": theta_record["minimum_projective_denominator"],
        "fresh_hull_audit": {
            "f_vector": [len(hull.vertices), len(edges), len(faces)],
            "active": mechanics["active"],
            "centroid": mechanics["centroid"].tolist(),
            "class": [len(stable), len(unstable), len(saddles)],
            "stable_faces": stable,
            "unstable_vertices": unstable,
            "saddle_edges": saddles,
            "faces_match_fixed_cell": True,
        },
        "all_mechanics_margins": margins,
        "topology_audit": topology,
    }
    json.dump(record, (HERE / "robust_target_rebuilt_full_audit.json").open("w"), indent=2)
    print(json.dumps({
        "f_vector": record["fresh_hull_audit"]["f_vector"],
        "class": record["fresh_hull_audit"]["class"],
        "hard_requested_margin": margins["hard_requested_margin"],
        "topology_support_min": topology["minimum_nonface_support_slack"],
        "topology_polygon_min": topology["minimum_polygon_edge_slack"],
    }, indent=2))


if __name__ == "__main__":
    main()
