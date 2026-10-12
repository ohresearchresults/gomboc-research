#!/usr/bin/env python3
"""Exact three-segment certificate for the mandatory-rail nullspace bypass."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(PARENT))

import build_u54_material_exact_path as source  # noqa: E402


RAW_FILES = {
    "source": HERE / "post_flip_intrinsic_step_008.csv",
    "pre": HERE / "mandatory_rail_bypass_pre.csv",
    "lifted": HERE / "mandatory_rail_bypass_lifted.csv",
    "endpoint": HERE / "mandatory_rail_bypass_endpoint.csv",
}
EXACT_FILES = {
    name: HERE / f"mandatory_rail_bypass_exact_{name}.csv" for name in RAW_FILES
}
FACE_FILE = HERE / "mandatory_rail_bypass_exact_faces.json"
CERTIFICATE = HERE / "mandatory_rail_bypass_exact_certificate.json"
CIRCUIT = (224, 228, 251, 252)


def parse_circuit(value):
    circuit = tuple(int(item) for item in value.split(","))
    if len(circuit) != 4 or len(set(circuit)) != 4:
        raise argparse.ArgumentTypeError("circuit must contain four distinct labels")
    return circuit


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def repair_snapshots():
    raw = {name: source.ex.read_rows(path) for name, path in RAW_FILES.items()}
    labels = set(raw["source"])
    if any(set(rows) != labels for rows in raw.values()):
        raise AssertionError("snapshot labels differ")
    anchor = raw["source"][0]
    normal = source.ex.cross(
        source.ex.sub(raw["source"][1], anchor),
        source.ex.sub(raw["source"][2], anchor),
    )
    normal_norm2 = source.ex.norm2(normal)
    repaired = {}
    audit = {}
    for name, rows in raw.items():
        points, base = source.project_base(rows, anchor, normal, normal_norm2)
        points, uv, quad = source.repair_quad(points)
        repaired[name] = points
        audit[name] = {
            "base": base,
            "quad": quad,
            "quad_barycentric": [source.ex.qs(uv[0]), source.ex.qs(uv[1])],
        }
    return repaired, audit


def make_path(left, right):
    out = {
        label: tuple(
            source.P((left[label][axis], right[label][axis] - left[label][axis]))
            for axis in range(3)
        )
        for label in left
        if label != 246
    }
    left_uv = source.barycentric(left[246], left[7], left[8], left[245])
    right_uv = source.barycentric(right[246], right[7], right[8], right[245])
    u = source.P((left_uv[0], right_uv[0] - left_uv[0]))
    v = source.P((left_uv[1], right_uv[1] - left_uv[1]))
    out[246] = source.ex.add(
        out[7],
        source.ex.add(
            source.ex.mul(source.ex.sub(out[8], out[7]), u),
            source.ex.mul(source.ex.sub(out[245], out[7]), v),
        ),
    )
    if source.determinant_polynomial(out, source.QUAD) != source.P.zero():
        raise AssertionError("protected quadrilateral is not identically planar")
    return out


def selected_residuals(points, faces):
    ledger = source.ex.mechanics_primitives(points, faces)
    scale = 4 * ledger["d6"]
    face_key = tuple(sorted(source.QUAD))
    face_index = ledger["face_by_key"][face_key]
    face_raw = source.ex.signed_face_components(ledger, face_key)[(8, 246)]
    face_normal = source.ex.cycle_normal(faces[face_index], points)
    face_edge = source.ex.sub(points[246], points[8])
    face_denominator = (
        scale * scale
        * source.ex.norm2(face_normal) ** 3
        * source.ex.norm2(face_edge)
    )
    vertex_raw = ledger["vertex"][54][1]
    vertex_denominator = source.ex.norm2(ledger["xscaled"][54]) * source.ex.norm2(
        source.ex.sub(points[1], points[54])
    )
    values = {
        "S_quad": (face_raw * face_raw / face_denominator, 2),
        "U54": (vertex_raw * vertex_raw / vertex_denominator, 2),
    }
    for name, edge in (("H67_beta2", (6, 7)), ("H910_beta2", (9, 10))):
        component = ledger["edge"][edge]
        dd = component["direction_norm2"]
        t_num = component["t"]
        left = edge[0]
        direction = source.ex.sub(points[edge[1]], points[left])
        projection_numerator = source.ex.add(
            source.ex.mul(ledger["xscaled"][left], dd),
            source.ex.mul(direction, t_num),
        )
        denominator = (
            component["gram"] * component["gram"]
            * source.ex.norm2(projection_numerator)
        )
        numerator = component["beta2"] * component["beta2"] * dd * dd
        values[name] = (numerator / denominator, 2)
    if any(value <= 0 for value, _power in values.values()):
        raise AssertionError(("nonpositive selected residual", values))
    return values


def comparison_packet(reference, endpoint):
    packet = {}
    for name, (left, power) in reference.items():
        right, right_power = endpoint[name]
        if power != right_power or not right < left:
            raise AssertionError(("endpoint residual not improved", name, left, right))
        ratio_power = right / left
        packet[name] = {
            "power": power,
            "exact_ratio_to_power": source.ex.qs(ratio_power),
            "decimal_ratio": math.sqrt(float(ratio_power)),
            "strictly_improved": True,
        }
    return packet


def circuit_clearance_packet(points, faces, circuit):
    d6, m24 = source.ex.exact_centroid_numerators(points, faces)
    if d6 <= 0:
        raise AssertionError("nonpositive exact volume in circuit clearance")
    centroid = tuple(value / (4 * d6) for value in m24)
    radius_squared = sum(
        (source.ex.norm2(source.ex.sub(points[label], centroid)) for label in points),
        Q(0),
    ) / len(points)
    if radius_squared <= 0:
        raise AssertionError("nonpositive exact RMS radius")
    a, b, c, d = circuit
    determinant = source.ex.det3(
        source.ex.sub(points[b], points[a]),
        source.ex.sub(points[c], points[a]),
        source.ex.sub(points[d], points[a]),
    )
    if not determinant:
        raise AssertionError("zero circuit determinant at checkpoint")
    opposite_area_squared = {
        str(a): source.ex.norm2(source.ex.cross(
            source.ex.sub(points[c], points[b]),
            source.ex.sub(points[d], points[b]),
        )),
        str(b): source.ex.norm2(source.ex.cross(
            source.ex.sub(points[c], points[a]),
            source.ex.sub(points[d], points[a]),
        )),
    }
    if any(value <= 0 for value in opposite_area_squared.values()):
        raise AssertionError("degenerate opposite circuit face")
    normalized_squared = {
        label: determinant * determinant / (radius_squared * area_squared)
        for label, area_squared in opposite_area_squared.items()
    }
    minimum = min(normalized_squared.values())
    return {
        "definition": (
            "D^2/(R_sites^2*C_opposite^2) for the two non-rail circuit vertices; "
            "R_sites^2 is the mean squared distance of all 61 stored sites from "
            "the exact volume centroid, and C_opposite^2 is the squared norm of "
            "the opposite-face edge cross product, equal to four times ordinary "
            "triangle area squared"
        ),
        "determinant": source.ex.qs(determinant),
        "rms_radius_squared": source.ex.qs(radius_squared),
        "opposite_area_squared": {
            label: source.ex.qs(value)
            for label, value in opposite_area_squared.items()
        },
        "normalized_opposite_slack_squared": {
            label: source.ex.qs(value)
            for label, value in normalized_squared.items()
        },
        "minimum_normalized_opposite_slack_squared": source.ex.qs(minimum),
        "minimum_normalized_opposite_slack": math.sqrt(float(minimum)),
        "strictly_positive": True,
    }


def main() -> None:
    global RAW_FILES, EXACT_FILES, FACE_FILE, CERTIFICATE, CIRCUIT

    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=str(RAW_FILES["source"]))
    parser.add_argument("--raw-prefix", default="mandatory_rail_bypass")
    parser.add_argument("--output-prefix", default="mandatory_rail_bypass_exact")
    parser.add_argument("--circuit", type=parse_circuit, required=True)
    args = parser.parse_args()

    source_path = Path(args.source)
    if not source_path.is_absolute():
        source_path = HERE / source_path
    RAW_FILES = {
        "source": source_path,
        "pre": HERE / f"{args.raw_prefix}_pre.csv",
        "lifted": HERE / f"{args.raw_prefix}_lifted.csv",
        "endpoint": HERE / f"{args.raw_prefix}_endpoint.csv",
    }
    EXACT_FILES = {
        name: HERE / f"{args.output_prefix}_{name}.csv" for name in RAW_FILES
    }
    FACE_FILE = HERE / f"{args.output_prefix}_faces.json"
    CERTIFICATE = HERE / f"{args.output_prefix}_certificate.json"
    CIRCUIT = tuple(args.circuit)

    snapshots, repair = repair_snapshots()
    for name, points in snapshots.items():
        source.write_exact_csv(EXACT_FILES[name], points)
    segment_names = (("source", "pre"), ("pre", "lifted"), ("lifted", "endpoint"))
    segments = [make_path(snapshots[left], snapshots[right]) for left, right in segment_names]

    representative_faces = []
    segment_records = []
    for index, ((left_name, right_name), path) in enumerate(zip(segment_names, segments)):
        representative = source.evaluate_path(path, Q(1, 2))
        faces, _ = source.fresh_faces(representative)
        support, mechanics = source.assert_cell(representative, faces)
        cover = source.exact_class_cover(path, faces, Q(0), Q(1))
        determinant = source.determinant_polynomial(path, CIRCUIT)
        midpoint_value = determinant.eval(Q(1, 2))
        sign = 1 if midpoint_value > 0 else -1 if midpoint_value < 0 else 0
        if sign == 0:
            raise AssertionError(("zero midpoint circuit", index))
        determinant_sign = source.exact_sign_record(determinant, Q(0), Q(1), sign)
        segment_records.append({
            "index": index,
            "left": left_name,
            "right": right_name,
            "face_hash": canonical_hash(faces),
            "f_vector": support["f_vector"],
            "active_labels": support["active_labels"],
            "mechanics": mechanics,
            "class_cover": cover,
            "class_cover_subinterval_count": len(cover),
            "mandatory_circuit_sign": determinant_sign,
            "mandatory_circuit_endpoint_values": [
                source.ex.qs(determinant.eval(Q(0))),
                source.ex.qs(determinant.eval(Q(1))),
            ],
        })
        representative_faces.append(faces)
    if not all(faces == representative_faces[0] for faces in representative_faces[1:]):
        raise AssertionError("bypass segments use different face lattices")
    faces = representative_faces[0]
    FACE_FILE.write_text(json.dumps(faces, indent=2) + "\n")

    reference_values = selected_residuals(snapshots["source"], faces)
    endpoint_values = selected_residuals(snapshots["endpoint"], faces)
    comparison = comparison_packet(reference_values, endpoint_values)
    clearance = {
        name: circuit_clearance_packet(points, faces, CIRCUIT)
        for name, points in snapshots.items()
    }
    generated = [*EXACT_FILES.values(), FACE_FILE]
    payload = {
        "version": 1,
        "scope": "exact three-segment residual-null bypass of mandatory rail wall",
        "verdict": "EXACT_MANDATORY_RAIL_NULLSPACE_BYPASS_PASS",
        "circuit": list(CIRCUIT),
        "raw_files": {
            name: str(path.relative_to(ROOT)) for name, path in RAW_FILES.items()
        },
        "raw_sha256": {
            name: sha256(path) for name, path in RAW_FILES.items()
        },
        "exact_files": {
            name: str(path.relative_to(ROOT)) for name, path in EXACT_FILES.items()
        },
        "repair": repair,
        "face_file": str(FACE_FILE.relative_to(ROOT)),
        "face_hash": canonical_hash(faces),
        "segments": segment_records,
        "endpoint_material_comparison": comparison,
        "circuit_clearance_at_checkpoints": clearance,
        "generated_sha256": {
            str(path.relative_to(ROOT)): sha256(path) for path in generated
        },
        "conclusion": (
            "All three exact rational polynomial segments remain in the same "
            "strict (60,158,100), own-centroid (2,2,2) cell, retain every rail, "
            "keep the mandatory circuit on its pre-side, and strictly improve "
            "all four selected residuals at the endpoint."
        ),
    }
    CERTIFICATE.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "verdict": payload["verdict"],
        "classes": [row["mechanics"]["class"] for row in segment_records],
        "class_cover_counts": [row["class_cover_subinterval_count"] for row in segment_records],
        "endpoint_ratios": {
            name: row["decimal_ratio"] for name, row in comparison.items()
        },
        "certificate": str(CERTIFICATE),
    }, indent=2))


if __name__ == "__main__":
    main()
