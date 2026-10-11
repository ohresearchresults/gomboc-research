#!/usr/bin/env python3
"""Independent fresh-hull audit for the row54 shared-3D endpoint and walls."""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import row54_shared3d_embedding as search  # noqa: E402


def face_sets_at(basis: np.ndarray, coefficient: float) -> set[frozenset[int]]:
    z = basis @ np.array((0.0, 0.0, coefficient))
    _, faces, _ = search.carrier.group_maximal_faces(search.IDS, search.points(z))
    return {frozenset(face) for face in faces}


def flip_audit(basis: np.ndarray, before: float, after: float) -> dict:
    pre = face_sets_at(basis, before)
    post = face_sets_at(basis, after)
    return {
        "before": before,
        "after": after,
        "removed": sorted((sorted(face) for face in pre - post), key=str),
        "added": sorted((sorted(face) for face in post - pre), key=str),
    }


def load_endpoint(path: Path) -> tuple[list[int], np.ndarray]:
    rows = {}
    with path.open() as f:
        for row in csv.DictReader(f):
            rows[int(row["source_id"])] = np.array(
                [float(row[k]) for k in ("x", "y", "z")], dtype=float
            )
    ids = sorted(rows)
    return ids, np.array([rows[row] for row in ids])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--result", type=Path, default=HERE / "row54_shared3d_result.json")
    ap.add_argument("--endpoint", type=Path, default=HERE / "row54_shared3d_endpoint.csv")
    ap.add_argument("--faces", type=Path,
                    default=HERE / "row54_shared3d_endpoint_faces.json")
    ap.add_argument("--output", type=Path, default=HERE / "endpoint_audit.json")
    args = ap.parse_args()

    result = json.load(args.result.open())
    linear = result["linear"]
    nonlinear = result["nonlinear_shared3d"]
    basis = np.asarray(linear["shared3d_basis"], dtype=float)
    z = np.asarray(nonlinear["best_parameters"], dtype=float)
    expected = search.points(z)
    ids, endpoint = load_endpoint(args.endpoint)
    assert ids == list(search.IDS)
    coordinate_error = float(np.max(np.abs(endpoint - expected)))
    assert coordinate_error < 1e-14

    hull, faces, _ = search.carrier.group_maximal_faces(ids, endpoint)
    mechanics, stable, unstable, saddles = search.carrier.classify(ids, endpoint, faces)
    saved_faces = {frozenset(face) for face in json.load(args.faces.open())}
    fresh_faces = {frozenset(face) for face in faces}
    edge_set = set(mechanics["ef"])
    missing_rails = sorted(search.FORCED_RAILS - edge_set)

    base_i = next(i for i, face in enumerate(faces) if frozenset(face) == search.BASE)
    topology_slacks = []
    normals = search.carrier.face_normals(ids, endpoint, faces)
    ix = {row: k for k, row in enumerate(ids)}
    for face, normal in zip(faces, normals):
        normal = normal / np.linalg.norm(normal)
        height = float(normal @ endpoint[ix[face[0]]])
        members = set(face)
        topology_slacks.extend(
            height - float(normal @ endpoint[ix[row]]) for row in ids if row not in members
        )

    stable_sets = {frozenset(face) for face in stable}
    saddle_set = {tuple(sorted(edge)) for edge in saddles}
    assertions = {
        "all_rows_active": mechanics["active"] == ids and len(hull.vertices) == len(ids),
        "faces_match_artifact": fresh_faces == saved_faces,
        "class_is_2_2_2": [len(stable), len(unstable), len(saddles)] == [2, 2, 2],
        "all_forced_rails_present": not missing_rails,
        "original_stable_face_dead": search.EXTRA_STABLE not in stable_sets,
        "stable_transferred_to_245_8_246": frozenset((245, 8, 246)) in stable_sets,
        "U54_dead": 54 not in unstable,
        "U_transferred_to_1": 1 in unstable,
        "U8_preserved": 8 in unstable,
        "H67_persists": (6, 7) in saddle_set,
        "H910_persists": (9, 10) in saddle_set,
        "base_positive": float(mechanics["fdec"][base_i]) > 0.0,
        "U8_positive": float(mechanics["udec"][8]) > 0.0,
        "full13d_farkas_valid": (
            not linear["full13d_lp"]["success"]
            and linear["full13d_lp"]["farkas"]["b_dot_y"] < 0.0
            and linear["full13d_lp"]["farkas"]["at_y_inf"] < 1e-12
        ),
        "shared3d_farkas_valid": (
            not linear["shared3d_lp"]["success"]
            and linear["shared3d_lp"]["farkas"]["b_dot_y"] < 0.0
            and linear["shared3d_lp"]["farkas"]["at_y_inf"] < 1e-12
        ),
    }

    flips = [
        flip_audit(basis, 1.0e-6, 2.0e-6),
        flip_audit(basis, 3.30e-6, 3.40e-6),
    ]
    assertions["first_flip_matches"] = (
        flips[0]["removed"] == [[5, 244, 245], [5, 6, 245]]
        and flips[0]["added"] == [[5, 6, 244], [6, 244, 245]]
    )
    assertions["second_flip_matches"] = (
        flips[1]["removed"] == [[7, 245, 246], [7, 8, 246]]
        and flips[1]["added"] == [[7, 8, 245], [8, 245, 246]]
    )
    assert all(assertions.values()), {k: v for k, v in assertions.items() if not v}

    audit = {
        "status": "PASS",
        "coordinate_roundtrip_max_abs": coordinate_error,
        "f_vector": [len(hull.vertices), len(mechanics["ef"]), len(faces)],
        "class": [len(stable), len(unstable), len(saddles)],
        "topology_support_min": float(min(topology_slacks)),
        "base_margin": float(mechanics["fdec"][base_i]),
        "U8_margin": float(mechanics["udec"][8]),
        "stable_faces": stable,
        "unstable_vertices": unstable,
        "saddle_edges": saddles,
        "missing_forced_rails": [list(edge) for edge in missing_rails],
        "assertions": assertions,
        "shared_h_first_walls": linear["shared_h_first_walls"][:4],
        "shared_h_target_zero_times": linear["shared_h_target_zero_times"],
        "fresh_flip_audit": flips,
        "full13d_farkas": linear["full13d_lp"]["farkas"],
        "shared3d_farkas": linear["shared3d_lp"]["farkas"],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w") as f:
        json.dump(audit, f, indent=2, allow_nan=False)
    print(json.dumps(audit, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
