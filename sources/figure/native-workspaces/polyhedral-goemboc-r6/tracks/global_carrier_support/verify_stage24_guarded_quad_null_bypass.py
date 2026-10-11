#!/usr/bin/env python3
"""Clean-room rerun of the frozen stage-24 guarded nullspace bypass."""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))

from actual_hull_mechanics import evaluate  # noqa: E402
from optimize_base_escape import Search  # noqa: E402
from search_row54_remote228 import load_points, summarize  # noqa: E402


CERTIFICATE = HERE / "stage24_guarded_quad_null_bypass.json"
SOURCE = ROOT / "tracks/circuit_atlas/row54_far_rebuilt.csv"
SOURCE_AUDIT = ROOT / "tracks/circuit_atlas/row54_far_rebuilt_audit.json"
ATLAS = HERE / "local_birth_atlas.json"
STAGE24 = HERE / "adaptive_stage24_far_u54_u1h154_guarded.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    frozen = json.loads(CERTIFICATE.read_text())
    assert frozen["verdict"] == "FRESH_HULL_GUARDED_STAGE24_QUAD_NULL_BYPASS_PASS"
    for path in (SOURCE, SOURCE_AUDIT, ATLAS, STAGE24):
        key = str(path.relative_to(ROOT))
        assert digest(path) == frozen["source_hashes"][key]

    stage = json.loads(STAGE24.read_text())
    labels, source = load_points(SOURCE)
    index = {label: offset for offset, label in enumerate(labels)}
    audit = json.loads(SOURCE_AUDIT.read_text())
    rails = {
        tuple(sorted(edge))
        for edge in audit["fresh_hull_audit"]["forced_rail_edges"]
    }
    search = Search(labels, source, rails, report=False)
    atlas = json.loads(ATLAS.read_text())
    remote = np.asarray(
        [atlas["remote_basis"]["tangent"], atlas["remote_basis"]["normal"]]
    )
    controls = [
        (int(row["label"]), np.asarray(row["direction"], dtype=float))
        for row in stage["local_controls"]
    ]

    def coordinates(parameters):
        points = search.coordinates(parameters[:20])
        points[index[228]] += parameters[20] * remote[0]
        points[index[228]] += parameters[21] * remote[1]
        for offset, (label, direction) in enumerate(controls):
            points[index[label]] += parameters[22 + offset] * direction
        return points

    def det4(parameters, quad):
        points = coordinates(parameters)
        rows = np.c_[points[[index[label] for label in quad]], np.ones(4)]
        return float(np.linalg.det(rows))

    def feature_values(mechanics):
        return np.asarray(
            [
                mechanics.face_decisions[(7, 8, 245)],
                mechanics.vertex_decisions[54],
                mechanics.edge_decisions[(5, 6)],
                mechanics.edge_decisions[(9, 10)],
                mechanics.vertex_decisions[1],
                mechanics.edge_decisions[(1, 54)],
            ]
        )

    start = np.asarray(frozen["start_parameters"], dtype=float)
    buffered = np.asarray(frozen["buffered_parameters"], dtype=float)
    endpoint = np.asarray(frozen["endpoint_parameters"], dtype=float)
    transverse = np.asarray(frozen["transverse_direction"], dtype=float)
    assert np.max(
        np.abs(
            buffered
            - start
            - frozen["transverse_amplitude"] * transverse
        )
    ) < 2e-16
    expected_endpoint = (
        start
        + frozen["advance_multiplier"]
        * frozen["wall_step"]
        * np.asarray(stage["wall"]["direction"], dtype=float)
        + frozen["transverse_amplitude"] * transverse
    )
    assert np.max(np.abs(endpoint - expected_endpoint)) < 2e-16

    initial_mechanics = evaluate(labels, coordinates(start))
    initial_faces = set(initial_mechanics.face_decisions)
    initial_values = feature_values(initial_mechanics)
    assert np.max(
        np.abs(initial_values - np.asarray(frozen["initial_feature_values"]))
    ) < 5e-13
    circuit_specs = [
        (tuple(row["circuit"]), int(row["valid_sign"]))
        for row in stage["circuit_guards"]
    ]

    sample_index = 0
    for leg, first, second in (
        ("start_to_buffer", start, buffered),
        ("buffer_to_endpoint", buffered, endpoint),
    ):
        for offset, t in enumerate(np.linspace(0.0, 1.0, 101)):
            if leg == "buffer_to_endpoint" and offset == 0:
                continue
            stored = frozen["path"][sample_index]
            sample_index += 1
            assert stored["leg"] == leg and stored["offset"] == offset
            parameters = (1.0 - t) * first + t * second
            points = coordinates(parameters)
            mechanics = evaluate(labels, points)
            record = summarize(labels, points, rails)
            values = feature_values(mechanics)
            signed = [sign * det4(parameters, quad) for quad, sign in circuit_specs]
            assert mechanics.cls == (2, 2, 2)
            assert (mechanics.vertices, mechanics.edges, mechanics.faces) == (61, 162, 103)
            assert set(mechanics.face_decisions) == initial_faces
            assert record["base_face_present"] and not record["missing_forced_rails"]
            assert min(signed) > 0.0 and values[4] < 0.0 and values[5] < 0.0
            assert np.max(
                np.abs(values - np.asarray(stored["feature_values"]))
            ) < 5e-10
    assert sample_index == frozen["path_sample_count"] == 201

    endpoint_points = coordinates(endpoint)
    endpoint_path = ROOT / frozen["endpoint"]["coordinates"]
    _, frozen_points = load_points(endpoint_path)
    assert np.max(np.abs(endpoint_points - frozen_points)) < 5e-14
    endpoint_mechanics = evaluate(labels, endpoint_points)
    endpoint_record = summarize(labels, endpoint_points, rails)
    assert list(endpoint_mechanics.cls) == frozen["endpoint"]["class"]
    assert endpoint_record["f_vector"] == frozen["endpoint"]["f_vector"]
    assert endpoint_record["base_face_present"]
    assert not endpoint_record["missing_forced_rails"]
    print("INDEPENDENT_STAGE24_GUARDED_QUAD_NULL_BYPASS_PASS")


if __name__ == "__main__":
    main()
