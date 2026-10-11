#!/usr/bin/env python3
"""Independent reconstruction and exact audit of the stage-30 checkpoint."""
from __future__ import annotations

import csv
import hashlib
import json
import math
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / "tracks/circuit_atlas/row54_far_rebuilt.csv"
SOURCE_AUDIT = ROOT / "tracks/circuit_atlas/row54_far_rebuilt_audit.json"
ATLAS = HERE / "local_birth_atlas.json"
ADAPTIVE = HERE / "adaptive_stage30_postquad2_h910_focus.json"
RAW = HERE / "stage30_exact_checkpoint_raw.csv"
EXACT = HERE / "stage30_exact_checkpoint.csv"
FACES = HERE / "stage30_exact_checkpoint_faces.json"
CERTIFICATE = HERE / "stage30_exact_checkpoint_certificate.json"

EXACT_DIR = (
    ROOT
    / "tracks/target_sphere_realizer/grouped_local_escape/rigorous_null_bypass"
)
GROUPED_DIR = EXACT_DIR.parent
sys.path[:0] = [str(HERE), str(EXACT_DIR), str(GROUPED_DIR)]

import actual_grouped as actual  # noqa: E402
import grouped_exact as gx  # noqa: E402
from actual_hull_mechanics import evaluate as adaptive_evaluate  # noqa: E402
from optimize_base_escape import Search  # noqa: E402
from search_row54_remote228 import load_points  # noqa: E402


ex = gx.ex
BASE = frozenset(range(17)) | {54}
PRIMARY_FACE = (7, 8, 245)
EXPECTED_CLASS = [2, 2, 2]
EXPECTED_F_VECTOR = [61, 162, 103]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def point_hash(points) -> str:
    return canonical_hash(
        {str(label): [ex.qs(x) for x in points[label]] for label in sorted(points)}
    )


def face_hash(faces) -> str:
    return canonical_hash([list(map(int, face)) for face in faces])


def forced_rails():
    short = [228] + list(range(229, 247)) + [8]
    long = [228] + list(range(247, 265)) + [8]
    edges = {
        tuple(sorted(edge))
        for path in (short, long)
        for edge in zip(path, path[1:])
    }
    edges.remove((228, 229))
    return edges


def reconstruct_float_rows(stage):
    checkpoint = stage["trace"][-1]
    parameters = np.asarray(checkpoint["parameters"], dtype=float)
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
        [atlas["remote_basis"]["tangent"], atlas["remote_basis"]["normal"]],
        dtype=float,
    )
    controls = [
        (int(row["label"]), np.asarray(row["direction"], dtype=float))
        for row in stage["local_controls"]
    ]
    if len(parameters) != 22 + len(controls):
        raise AssertionError("stage-30 parameter/control mismatch")
    points = search.coordinates(parameters[:20])
    points[index[228]] += parameters[20] * remote[0]
    points[index[228]] += parameters[21] * remote[1]
    for offset, (label, direction) in enumerate(controls):
        points[index[label]] += parameters[22 + offset] * direction
    rows = {
        int(label): tuple(Q(format(float(value), ".17g")) for value in point)
        for label, point in zip(labels, points)
    }
    return parameters, rows


def exact_mechanics_digest(points, faces):
    ledger, summary = ex.classify_point(points, faces)
    rows = []
    for key in sorted(ledger["face"]):
        for edge, value in sorted(ex.signed_face_components(ledger, key).items()):
            rows.append(("face", key, edge, ex.qs(value)))
    for vertex, values in sorted(ledger["vertex"].items()):
        for neighbor, value in sorted(values.items()):
            rows.append(("vertex", vertex, neighbor, ex.qs(value)))
    for edge, values in sorted(ledger["edge"].items()):
        for name in ("t", "one_minus_t", "beta1", "beta2", "gram"):
            rows.append(("edge", edge, name, ex.qs(values[name])))
    nonzero = [Q(row[-1]) for row in rows if Q(row[-1])]
    return summary, {
        "primitive_count": len(rows),
        "exact_value_digest": canonical_hash(rows),
        "minimum_nonzero_log10_abs": min(ex.qlog10(value) for value in nonzero),
        "zero_count": len(rows) - len(nonzero),
    }, ledger


def exact_rows_packet(values):
    return [
        {
            "component": name,
            "exact": ex.qs(value),
            "sign": 1 if value > 0 else -1 if value < 0 else 0,
            "log10_abs": ex.qlog10(value),
        }
        for name, value in values
    ]


def feature_packet(points, faces, result, ledger, summary):
    face_components = ex.signed_face_components(ledger, PRIMARY_FACE)
    edge_names = ("t", "one_minus_t", "beta1", "beta2")
    labels = sorted(points)
    adaptive_result = adaptive_evaluate(
        labels,
        np.asarray([[float(value) for value in points[label]] for label in labels]),
    )
    assert list(adaptive_result.cls) == EXPECTED_CLASS
    face_index = next(
        index
        for index, row in enumerate(result.faces)
        if tuple(sorted(row["cycle"])) == PRIMARY_FACE
    )
    return {
        "numerical_display_only": {
            "adaptive_driver_convention": {
                "S(7,8,245)": float(adaptive_result.face_decisions[PRIMARY_FACE]),
                "U54": float(adaptive_result.vertex_decisions[54]),
                "H(5,6)": float(adaptive_result.edge_decisions[(5, 6)]),
                "H(9,10)": float(adaptive_result.edge_decisions[(9, 10)]),
                "U1": float(adaptive_result.vertex_decisions[1]),
                "H(1,54)": float(adaptive_result.edge_decisions[(1, 54)]),
            },
            "grouped_scale_normalized_convention": {
                "S(7,8,245)": float(result.face_decisions[face_index]),
                "U54": float(result.vertex_decisions[54]),
                "H(5,6)": float(result.edge_decisions[(5, 6)]),
                "H(9,10)": float(result.edge_decisions[(9, 10)]),
                "U1": float(result.vertex_decisions[1]),
                "H(1,54)": float(result.edge_decisions[(1, 54)]),
            },
            "normalization_note": (
                "The grouped evaluator divides stable-face distance by the "
                "polyhedron radius; the adaptive driver does not. Other named "
                "decisions use the same dimensionless convention here."
            ),
        },
        "exact_zero_equivalent_components": {
            "S(7,8,245)": exact_rows_packet(
                (f"edge:{edge[0]},{edge[1]}", value)
                for edge, value in sorted(face_components.items())
            ),
            "U54": exact_rows_packet(
                (f"neighbor:{neighbor}", value)
                for neighbor, value in sorted(ledger["vertex"][54].items())
            ),
            "H(5,6)": exact_rows_packet(
                (name, ledger["edge"][(5, 6)][name]) for name in edge_names
            ),
            "H(9,10)": exact_rows_packet(
                (name, ledger["edge"][(9, 10)][name]) for name in edge_names
            ),
            "U1": exact_rows_packet(
                (f"neighbor:{neighbor}", value)
                for neighbor, value in sorted(ledger["vertex"][1].items())
            ),
            "H(1,54)": exact_rows_packet(
                (name, ledger["edge"][(1, 54)][name]) for name in edge_names
            ),
        },
        "classification": summary,
    }


def adaptive_det4(points, quad):
    a, b, c, d = (points[label] for label in quad)
    return -ex.det3(ex.sub(b, a), ex.sub(c, a), ex.sub(d, a))


def circuit_packet(stage, points):
    packet = []
    for spec in stage["circuit_guards"]:
        quad = tuple(int(label) for label in spec["circuit"])
        valid_sign = int(spec["valid_sign"])
        value = adaptive_det4(points, quad)
        assert valid_sign * value > 0
        packet.append(
            {
                "circuit": list(quad),
                "valid_sign": valid_sign,
                "exact_adaptive_determinant": ex.qs(value),
                "log10_abs": ex.qlog10(value),
            }
        )
    return packet


def assert_log_close(actual_value, frozen_value) -> None:
    if not math.isclose(actual_value, frozen_value, rel_tol=0.0, abs_tol=5e-13):
        raise AssertionError((actual_value, frozen_value))


def assert_exact_component_packets(actual_packet, frozen_packet) -> None:
    assert set(actual_packet) == set(frozen_packet)
    for feature in actual_packet:
        actual_rows = actual_packet[feature]
        frozen_rows = frozen_packet[feature]
        assert len(actual_rows) == len(frozen_rows)
        for actual_row, frozen_row in zip(actual_rows, frozen_rows):
            assert actual_row["component"] == frozen_row["component"]
            assert actual_row["exact"] == frozen_row["exact"]
            assert actual_row["sign"] == frozen_row["sign"]
            assert_log_close(actual_row["log10_abs"], frozen_row["log10_abs"])


def assert_circuit_packets(actual_packet, frozen_packet) -> None:
    assert len(actual_packet) == len(frozen_packet)
    for actual_row, frozen_row in zip(actual_packet, frozen_packet):
        assert actual_row["circuit"] == frozen_row["circuit"]
        assert actual_row["valid_sign"] == frozen_row["valid_sign"]
        assert (
            actual_row["exact_adaptive_determinant"]
            == frozen_row["exact_adaptive_determinant"]
        )
        assert_log_close(actual_row["log10_abs"], frozen_row["log10_abs"])


def verify_checkpoint(
    adaptive_path: Path,
    raw_path: Path,
    exact_path: Path,
    faces_path: Path,
    certificate_path: Path,
    expected_verdict: str,
    terminal: str,
) -> None:
    frozen = json.loads(certificate_path.read_text())
    assert frozen["verdict"] == expected_verdict
    stage = json.loads(adaptive_path.read_text())

    for path in (SOURCE, SOURCE_AUDIT, ATLAS, adaptive_path):
        key = str(path.relative_to(ROOT))
        assert sha256(path) == frozen["source_hashes"][key]
    for path in (raw_path, exact_path, faces_path):
        key = str(path.relative_to(ROOT))
        assert sha256(path) == frozen["generated_file_sha256"][key]

    parameters, reconstructed_raw = reconstruct_float_rows(stage)
    stored_raw = ex.read_rows(raw_path)
    assert reconstructed_raw == stored_raw
    assert [format(float(value), ".17g") for value in parameters] == frozen[
        "construction"
    ]["parameter_vector"]
    assert canonical_hash(frozen["construction"]["parameter_vector"]) == frozen[
        "construction"
    ]["parameter_digest"]

    points, repair = gx.read_repaired(raw_path)
    assert points == ex.read_rows(exact_path)
    frozen_repair = frozen["construction"]["base_repair"]
    assert repair["nonzero_correction_count"] == frozen_repair[
        "nonzero_correction_count"
    ]
    assert_log_close(
        repair["largest_coefficient_log10_abs"],
        frozen_repair["largest_coefficient_log10_abs"],
    )
    for label in BASE:
        normal = ex.cross(ex.sub(points[1], points[0]), ex.sub(points[2], points[0]))
        assert ex.dot(normal, ex.sub(points[label], points[0])) == 0

    stored_faces = json.loads(faces_path.read_text())
    result = actual.evaluate(
        {label: np.asarray([float(value) for value in row]) for label, row in points.items()},
        coplanar_rel=2e-12,
    )
    assert result.valid, result.error
    rebuilt_faces = [row["cycle"] for row in result.faces]
    assert {frozenset(face) for face in rebuilt_faces} == {
        frozenset(face) for face in stored_faces
    }

    support = ex.supporting_cell(points, stored_faces)
    summary, mechanics_digest, ledger = exact_mechanics_digest(points, stored_faces)
    assert support["f_vector"] == EXPECTED_F_VECTOR
    assert support["euler"] == 2
    assert summary["class"] == EXPECTED_CLASS
    assert set(forced_rails()).issubset(set(support["edges"]))

    checkpoint = frozen["checkpoint"]
    assert checkpoint["coordinate_hash"] == point_hash(points)
    assert checkpoint["face_hash"] == face_hash(stored_faces)
    for key, value in support.items():
        if key in ("edges", "active_labels"):
            continue
        if key == "min_support_log10_abs":
            assert_log_close(value, checkpoint["exact_support"][key])
        else:
            assert checkpoint["exact_support"][key] == value
    assert checkpoint["active_labels"] == support["active_labels"]
    assert checkpoint["exact_mechanics"] == summary
    for key, value in mechanics_digest.items():
        if key == "minimum_nonzero_log10_abs":
            assert_log_close(value, checkpoint["mechanics_ledger"][key])
        else:
            assert checkpoint["mechanics_ledger"][key] == value
    assert checkpoint["base_face_present"]
    assert checkpoint["missing_forced_rails"] == []

    expected_features = feature_packet(
        points, stored_faces, result, ledger, summary
    )
    frozen_features = frozen["feature_packet"]
    assert expected_features["classification"] == frozen_features["classification"]
    assert_exact_component_packets(
        expected_features["exact_zero_equivalent_components"],
        frozen_features["exact_zero_equivalent_components"],
    )
    for convention in (
        "adaptive_driver_convention",
        "grouped_scale_normalized_convention",
    ):
        for name, value in expected_features["numerical_display_only"][
            convention
        ].items():
            assert math.isclose(
                value,
                frozen_features["numerical_display_only"][convention][name],
                rel_tol=0.0,
                abs_tol=5e-13,
            )
    assert (
        expected_features["numerical_display_only"]["normalization_note"]
        == frozen_features["numerical_display_only"]["normalization_note"]
    )
    assert_circuit_packets(
        circuit_packet(stage, points), frozen["exact_circuit_guards"]
    )
    assert frozen["residual_verdict"]["winner"] is False
    assert frozen["residual_verdict"]["class"] == EXPECTED_CLASS
    print(terminal)


def main() -> None:
    verify_checkpoint(
        ADAPTIVE,
        RAW,
        EXACT,
        FACES,
        CERTIFICATE,
        "EXACT_STAGE30_FAR_H56_CHECKPOINT_PASS",
        "INDEPENDENT_EXACT_STAGE30_FAR_H56_CHECKPOINT_PASS",
    )


if __name__ == "__main__":
    main()
