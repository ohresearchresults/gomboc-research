#!/usr/bin/env python3
"""Build an exact rational audit of the last accepted stage-30 checkpoint.

The adaptive continuation itself is numerical.  This builder independently
reconstructs its last accepted coordinates from the frozen source, chart,
local controls, and parameter vector; writes the resulting finite-decimal
object; projects only the enlarged base onto one exact rational plane; and
then audits the complete face lattice and every S/U/H primitive with rational
arithmetic.
"""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / "tracks/circuit_atlas/row54_far_rebuilt.csv"
SOURCE_AUDIT = ROOT / "tracks/circuit_atlas/row54_far_rebuilt_audit.json"
ATLAS = HERE / "local_birth_atlas.json"
ADAPTIVE = HERE / "adaptive_stage30_postquad2_h910_focus.json"
RAW_OUT = HERE / "stage30_exact_checkpoint_raw.csv"
EXACT_OUT = HERE / "stage30_exact_checkpoint.csv"
FACES_OUT = HERE / "stage30_exact_checkpoint_faces.json"
CERT_OUT = HERE / "stage30_exact_checkpoint_certificate.json"

LOCAL_CERT_DIR = (
    ROOT / "tracks/local_oct_cell_search/clean_flip_topology_escape"
)
sys.path[:0] = [str(HERE), str(LOCAL_CERT_DIR)]

import build_certificate as exact_certificate  # noqa: E402
from actual_hull_mechanics import evaluate as adaptive_evaluate  # noqa: E402
from optimize_base_escape import Search  # noqa: E402
from search_row54_remote228 import load_points  # noqa: E402


ex = exact_certificate.ex
EXPECTED_CLASS = [2, 2, 2]
EXPECTED_F_VECTOR = [61, 162, 103]
PRIMARY_FACE = (7, 8, 245)
TARGET_VERTEX = 54
TARGET_EDGES = ((5, 6), (9, 10))
ANTI_BIRTH_VERTEX = 1
ANTI_BIRTH_EDGE = (1, 54)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def write_float_csv(path: Path, labels, points) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(("source_id", "x", "y", "z"))
        for label, point in zip(labels, points):
            writer.writerow(
                [label, *[format(float(value), ".17g") for value in point]]
            )


def write_exact_csv(path: Path, points) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(("source_id", "x", "y", "z"))
        for label in sorted(points):
            writer.writerow([label, *[ex.qs(value) for value in points[label]]])


def reconstruct_last_checkpoint(adaptive_path: Path = ADAPTIVE):
    stage = json.loads(adaptive_path.read_text())
    if not stage["trace"]:
        raise AssertionError("stage-30 trace is empty")
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
    remote_basis = np.asarray(
        [atlas["remote_basis"]["tangent"], atlas["remote_basis"]["normal"]],
        dtype=float,
    )
    controls = [
        (int(row["label"]), np.asarray(row["direction"], dtype=float))
        for row in stage["local_controls"]
    ]
    expected_parameter_count = 22 + len(controls)
    if parameters.shape != (expected_parameter_count,):
        raise AssertionError(
            ("unexpected parameter vector", parameters.shape, expected_parameter_count)
        )

    points = search.coordinates(parameters[:20])
    points[index[228]] += parameters[20] * remote_basis[0]
    points[index[228]] += parameters[21] * remote_basis[1]
    for offset, (label, direction) in enumerate(controls):
        points[index[label]] += parameters[22 + offset] * direction
    return stage, checkpoint, parameters, labels, points


def exact_rows_packet(values) -> list[dict]:
    packet = []
    for name, value in values:
        packet.append(
            {
                "component": name,
                "exact": ex.qs(value),
                "sign": 1 if value > 0 else -1 if value < 0 else 0,
                "log10_abs": ex.qlog10(value),
            }
        )
    return packet


def feature_packet(points, faces, float_result) -> dict:
    ledger, summary = ex.classify_point(points, faces)
    face_components = ex.signed_face_components(ledger, PRIMARY_FACE)
    edge_component_names = ("t", "one_minus_t", "beta1", "beta2")

    labels = sorted(points)
    adaptive_result = adaptive_evaluate(
        labels,
        np.asarray([[float(value) for value in points[label]] for label in labels]),
    )
    if list(adaptive_result.cls) != EXPECTED_CLASS:
        raise AssertionError(("adaptive evaluator class mismatch", adaptive_result.cls))

    face_index = next(
        index
        for index, row in enumerate(float_result.faces)
        if tuple(sorted(row["cycle"])) == PRIMARY_FACE
    )
    scale_normalized = {
        "S(7,8,245)": float(float_result.face_decisions[face_index]),
        "U54": float(float_result.vertex_decisions[TARGET_VERTEX]),
        "H(5,6)": float(float_result.edge_decisions[(5, 6)]),
        "H(9,10)": float(float_result.edge_decisions[(9, 10)]),
        "U1": float(float_result.vertex_decisions[ANTI_BIRTH_VERTEX]),
        "H(1,54)": float(float_result.edge_decisions[ANTI_BIRTH_EDGE]),
    }
    adaptive_convention = {
        "S(7,8,245)": float(adaptive_result.face_decisions[PRIMARY_FACE]),
        "U54": float(adaptive_result.vertex_decisions[TARGET_VERTEX]),
        "H(5,6)": float(adaptive_result.edge_decisions[(5, 6)]),
        "H(9,10)": float(adaptive_result.edge_decisions[(9, 10)]),
        "U1": float(adaptive_result.vertex_decisions[ANTI_BIRTH_VERTEX]),
        "H(1,54)": float(adaptive_result.edge_decisions[ANTI_BIRTH_EDGE]),
    }
    exact = {
        "S(7,8,245)": exact_rows_packet(
            (f"edge:{edge[0]},{edge[1]}", value)
            for edge, value in sorted(face_components.items())
        ),
        "U54": exact_rows_packet(
            (f"neighbor:{neighbor}", value)
            for neighbor, value in sorted(ledger["vertex"][TARGET_VERTEX].items())
        ),
        "H(5,6)": exact_rows_packet(
            (name, ledger["edge"][(5, 6)][name])
            for name in edge_component_names
        ),
        "H(9,10)": exact_rows_packet(
            (name, ledger["edge"][(9, 10)][name])
            for name in edge_component_names
        ),
        "U1": exact_rows_packet(
            (f"neighbor:{neighbor}", value)
            for neighbor, value in sorted(
                ledger["vertex"][ANTI_BIRTH_VERTEX].items()
            )
        ),
        "H(1,54)": exact_rows_packet(
            (name, ledger["edge"][ANTI_BIRTH_EDGE][name])
            for name in edge_component_names
        ),
    }
    if summary["class"] != EXPECTED_CLASS:
        raise AssertionError(("wrong exact mechanics class", summary))
    return {
        "numerical_display_only": {
            "adaptive_driver_convention": adaptive_convention,
            "grouped_scale_normalized_convention": scale_normalized,
            "normalization_note": (
                "The grouped evaluator divides stable-face distance by the "
                "polyhedron radius; the adaptive driver does not. Other named "
                "decisions use the same dimensionless convention here."
            ),
        },
        "exact_zero_equivalent_components": exact,
        "classification": summary,
    }


def circuit_packet(stage, points) -> list[dict]:
    packet = []
    for spec in stage["circuit_guards"]:
        quad = tuple(int(label) for label in spec["circuit"])
        valid_sign = int(spec["valid_sign"])
        # The adaptive driver uses det([x,y,z,1]); exact_certificate.det4 uses
        # det([b-a,c-a,d-a]), which has the opposite orientation.
        value = -exact_certificate.det4(points, quad)
        if valid_sign * value <= 0:
            raise AssertionError(("invalid exact circuit", quad, valid_sign, value))
        packet.append(
            {
                "circuit": list(quad),
                "valid_sign": valid_sign,
                "exact_adaptive_determinant": ex.qs(value),
                "log10_abs": ex.qlog10(value),
            }
        )
    return packet


def build_checkpoint(
    adaptive_path: Path,
    raw_out: Path,
    exact_out: Path,
    faces_out: Path,
    certificate_out: Path,
    verdict: str,
) -> None:
    stage, checkpoint, parameters, labels, float_points = reconstruct_last_checkpoint(
        adaptive_path
    )
    write_float_csv(raw_out, labels, float_points)

    points, base_repair = exact_certificate.gx.read_repaired(raw_out)
    faces, float_result = exact_certificate.qhull_faces(points)
    exact_record = exact_certificate.endpoint_record(
        "stage30_exact_checkpoint", points, faces, write=False
    )
    if exact_record["exact_support"]["f_vector"] != EXPECTED_F_VECTOR:
        raise AssertionError(exact_record["exact_support"])
    if exact_record["exact_mechanics"]["class"] != EXPECTED_CLASS:
        raise AssertionError(exact_record["exact_mechanics"])
    if not exact_record["base_face_present"]:
        raise AssertionError("enlarged exact base is absent")
    if exact_record["missing_forced_rails"]:
        raise AssertionError(exact_record["missing_forced_rails"])

    write_exact_csv(exact_out, points)
    faces_out.write_text(json.dumps(faces, indent=2) + "\n")
    features = feature_packet(points, faces, float_result)
    circuits = circuit_packet(stage, points)

    source_paths = (SOURCE, SOURCE_AUDIT, ATLAS, adaptive_path)
    generated_paths = (raw_out, exact_out, faces_out)
    certificate = {
        "version": 1,
        "type": "exact rational audit of a numerical adaptive checkpoint",
        "verdict": verdict,
        "scope": (
            "One explicit rational polyhedron obtained from the last accepted "
            "stage-30 finite-decimal checkpoint by projecting only the enlarged "
            "base onto its exact rational plane. Complete support, incidence, "
            "and own-centroid S/U/H classification are exact. This is not a "
            "continuum certificate and not a (1,1,0) winner."
        ),
        "source_hashes": {
            str(path.relative_to(ROOT)): sha256(path) for path in source_paths
        },
        "construction": {
            "adaptive_trace_length": len(stage["trace"]),
            "adaptive_iteration": int(checkpoint["iteration"]),
            "parameter_count": len(parameters),
            "parameter_vector": [format(float(value), ".17g") for value in parameters],
            "parameter_digest": canonical_hash(
                [format(float(value), ".17g") for value in parameters]
            ),
            "base_repair": base_repair,
            "base_repair_rule": (
                "orthogonal exact-rational projection of labels 0..16 and 54 "
                "onto the plane through repaired finite-decimal rows 0,1,2"
            ),
        },
        "checkpoint": exact_record,
        "feature_packet": features,
        "exact_circuit_guards": circuits,
        "residual_verdict": {
            "winner": False,
            "class": EXPECTED_CLASS,
            "remaining_defects": [
                "S(7,8,245)",
                "U54",
                "H(5,6)",
                "H(9,10)",
            ],
            "anti_birth_guards": ["U1<0", "H(1,54)<0"],
        },
        "generated_file_sha256": {
            str(path.relative_to(ROOT)): sha256(path) for path in generated_paths
        },
    }
    certificate_out.write_text(json.dumps(certificate, indent=2) + "\n")
    print(verdict)
    print(
        json.dumps(
            {
                "class": exact_record["exact_mechanics"]["class"],
                "f_vector": exact_record["exact_support"]["f_vector"],
                "base_repair": base_repair,
                "features": features["numerical_display_only"][
                    "adaptive_driver_convention"
                ],
            },
            indent=2,
        )
    )


def main() -> None:
    build_checkpoint(
        ADAPTIVE,
        RAW_OUT,
        EXACT_OUT,
        FACES_OUT,
        CERT_OUT,
        "EXACT_STAGE30_FAR_H56_CHECKPOINT_PASS",
    )


if __name__ == "__main__":
    main()
