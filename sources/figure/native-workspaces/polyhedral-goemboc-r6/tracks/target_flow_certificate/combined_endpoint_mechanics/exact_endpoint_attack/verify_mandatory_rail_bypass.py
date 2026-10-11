#!/usr/bin/env python3
"""Independent reconstruction of the exact mandatory-rail nullspace bypass."""
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


CHECKPOINT_CLEARANCE_DEFINITION = (
    "D^2/(R_sites^2*C_opposite^2) for the two non-rail circuit vertices; "
    "R_sites^2 is the mean squared distance of all 61 stored sites from "
    "the exact volume centroid, and C_opposite^2 is the squared norm of "
    "the opposite-face edge cross product, equal to four times ordinary "
    "triangle area squared"
)


def parse_circuit(value: str):
    try:
        circuit = tuple(int(item) for item in value.split(","))
    except ValueError as error:
        raise argparse.ArgumentTypeError(
            "circuit must contain four comma-separated integer labels"
        ) from error
    if len(circuit) != 4 or len(set(circuit)) != 4:
        raise argparse.ArgumentTypeError("circuit must contain four distinct labels")
    return circuit


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def barycentric(point, a, b, c):
    e1, e2, w = source.ex.sub(b, a), source.ex.sub(c, a), source.ex.sub(point, a)
    aa = source.ex.dot(e1, e1)
    ab = source.ex.dot(e1, e2)
    bb = source.ex.dot(e2, e2)
    wa = source.ex.dot(w, e1)
    wb = source.ex.dot(w, e2)
    determinant = aa * bb - ab * ab
    if not determinant:
        raise AssertionError("degenerate independent quadrilateral chart")
    return (
        (wa * bb - wb * ab) / determinant,
        (wb * aa - wa * ab) / determinant,
    )


def project_base(rows, anchor, normal, normal_norm2):
    out = dict(rows)
    corrections = {}
    for label in source.BASE:
        coefficient = (
            source.ex.dot(normal, source.ex.sub(out[label], anchor)) / normal_norm2
        )
        out[label] = source.ex.sub(out[label], source.ex.mul(normal, coefficient))
        corrections[label] = coefficient
        if source.ex.dot(normal, source.ex.sub(out[label], anchor)):
            raise AssertionError(("independent base projection failed", label))
    nonzero = [value for value in corrections.values() if value]
    return out, {
        "nonzero_count": len(nonzero),
        "maximum_log10_abs": (
            max(source.ex.qlog10(value) for value in nonzero) if nonzero else None
        ),
        "exact_digest": canonical_hash({
            str(label): source.ex.qs(value)
            for label, value in sorted(corrections.items())
        }),
    }


def repair_quad(rows):
    out = dict(rows)
    u, v = barycentric(out[246], out[7], out[8], out[245])
    repaired = source.ex.add(
        out[7],
        source.ex.add(
            source.ex.mul(source.ex.sub(out[8], out[7]), u),
            source.ex.mul(source.ex.sub(out[245], out[7]), v),
        ),
    )
    displacement = source.ex.sub(repaired, out[246])
    displacement_norm2 = source.ex.norm2(displacement)
    out[246] = repaired
    return out, (u, v), {
        "barycentric": [source.ex.qs(u), source.ex.qs(v)],
        "displacement_norm2_exact": source.ex.qs(displacement_norm2),
        "displacement_norm_decimal": math.sqrt(float(displacement_norm2)),
    }


def repair_snapshots(raw_files):
    names = ("source", "pre", "lifted", "endpoint")
    if set(raw_files) != set(names):
        raise AssertionError(("unexpected raw snapshot set", sorted(raw_files)))
    raw = {name: source.ex.read_rows(raw_files[name]) for name in names}
    labels = set(raw["source"])
    if any(set(rows) != labels for rows in raw.values()):
        raise AssertionError("snapshot labels differ")
    anchor = raw["source"][0]
    normal = source.ex.cross(
        source.ex.sub(raw["source"][1], anchor),
        source.ex.sub(raw["source"][2], anchor),
    )
    normal_norm2 = source.ex.norm2(normal)
    if not normal_norm2:
        raise AssertionError("degenerate independent common base plane")
    repaired = {}
    audit = {}
    for name, rows in raw.items():
        points, base = project_base(rows, anchor, normal, normal_norm2)
        points, uv, quad = repair_quad(points)
        repaired[name] = points
        audit[name] = {
            "base": base,
            "quad": quad,
            "quad_barycentric": [source.ex.qs(uv[0]), source.ex.qs(uv[1])],
        }
    return repaired, audit


def evaluate_path(path, parameter: Q):
    return {
        label: tuple(coordinate.eval(parameter) for coordinate in xyz)
        for label, xyz in path.items()
    }


def determinant_polynomial(path, circuit):
    a, b, c, d = (path[label] for label in circuit)
    return source.ex.det3(
        source.ex.sub(b, a),
        source.ex.sub(c, a),
        source.ex.sub(d, a),
    )


def make_path(left, right):
    if set(left) != set(right):
        raise AssertionError("independent path endpoint labels differ")
    out = {
        label: tuple(
            source.P((left[label][axis], right[label][axis] - left[label][axis]))
            for axis in range(3)
        )
        for label in left
        if label != 246
    }
    left_uv = barycentric(left[246], left[7], left[8], left[245])
    right_uv = barycentric(right[246], right[7], right[8], right[245])
    u = source.P((left_uv[0], right_uv[0] - left_uv[0]))
    v = source.P((left_uv[1], right_uv[1] - left_uv[1]))
    out[246] = source.ex.add(
        out[7],
        source.ex.add(
            source.ex.mul(source.ex.sub(out[8], out[7]), u),
            source.ex.mul(source.ex.sub(out[245], out[7]), v),
        ),
    )
    if determinant_polynomial(out, source.QUAD) != source.P.zero():
        raise AssertionError("independent protected quadrilateral is not planar")
    if evaluate_path(out, Q(0)) != left or evaluate_path(out, Q(1)) != right:
        raise AssertionError("independent exact path misses a repaired endpoint")
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
    vertex_denominator = source.ex.norm2(
        ledger["xscaled"][54]
    ) * source.ex.norm2(source.ex.sub(points[1], points[54]))
    values = {
        "S_quad": (face_raw * face_raw / face_denominator, 2),
        "U54": (vertex_raw * vertex_raw / vertex_denominator, 2),
    }
    for name, edge in (("H67_beta2", (6, 7)), ("H910_beta2", (9, 10))):
        component = ledger["edge"][edge]
        direction_norm2 = component["direction_norm2"]
        direction = source.ex.sub(points[edge[1]], points[edge[0]])
        projection_numerator = source.ex.add(
            source.ex.mul(ledger["xscaled"][edge[0]], direction_norm2),
            source.ex.mul(direction, component["t"]),
        )
        denominator = (
            component["gram"] * component["gram"]
            * source.ex.norm2(projection_numerator)
        )
        numerator = (
            component["beta2"] * component["beta2"]
            * direction_norm2 * direction_norm2
        )
        values[name] = (numerator / denominator, 2)
    if any(value <= 0 for value, _power in values.values()):
        raise AssertionError(("independent nonpositive selected residual", values))
    return values


def comparison_packet(reference, endpoint):
    packet = {}
    if set(reference) != set(endpoint):
        raise AssertionError("independent selected residual sets differ")
    for name, (left, power) in reference.items():
        right, right_power = endpoint[name]
        if power != right_power or not right < left:
            raise AssertionError(
                ("independent endpoint residual not improved", name, left, right)
            )
        ratio_power = right / left
        packet[name] = {
            "power": power,
            "exact_ratio_to_power": source.ex.qs(ratio_power),
            "decimal_ratio": math.sqrt(float(ratio_power)),
            "strictly_improved": True,
        }
    return packet


def circuit_segment_packet(path, circuit):
    determinant = determinant_polynomial(path, circuit)
    midpoint_value = determinant.eval(Q(1, 2))
    sign = 1 if midpoint_value > 0 else -1 if midpoint_value < 0 else 0
    if sign == 0:
        raise AssertionError("independent zero midpoint circuit determinant")
    certified_sign, leaves, worst = source.ex.bernstein_sign(
        determinant, Q(0), Q(1), max_depth=60
    )
    if certified_sign != sign:
        raise AssertionError(
            ("independent circuit sign proof failed", certified_sign, sign)
        )
    return {
        "sign_record": {
            "sign": certified_sign,
            "degree": determinant.degree,
            "bernstein_leaf_count": leaves,
            "minimum_bernstein_log10_abs": worst,
            "polynomial_digest": canonical_hash(determinant.exact()),
        },
        "endpoint_values": [
            source.ex.qs(determinant.eval(Q(0))),
            source.ex.qs(determinant.eval(Q(1))),
        ],
    }


def circuit_clearance_packet(points, faces, circuit):
    if len(points) != 61:
        raise AssertionError(("independent checkpoint site count", len(points)))
    d6, m24 = source.ex.exact_centroid_numerators(points, faces)
    if d6 <= 0:
        raise AssertionError("independent nonpositive volume in clearance audit")
    centroid = tuple(value / (4 * d6) for value in m24)
    radius_squared = sum(
        (source.ex.norm2(source.ex.sub(points[label], centroid)) for label in points),
        Q(0),
    ) / len(points)
    a, b, c, d = circuit
    determinant = source.ex.det3(
        source.ex.sub(points[b], points[a]),
        source.ex.sub(points[c], points[a]),
        source.ex.sub(points[d], points[a]),
    )
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
    if radius_squared <= 0 or not determinant or any(
        value <= 0 for value in opposite_area_squared.values()
    ):
        raise AssertionError("independent degenerate circuit-clearance geometry")
    normalized_squared = {
        label: determinant * determinant / (radius_squared * area_squared)
        for label, area_squared in opposite_area_squared.items()
    }
    minimum = min(normalized_squared.values())
    return {
        "definition": CHECKPOINT_CLEARANCE_DEFINITION,
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--prefix", required=True)
    parser.add_argument("--expected-circuit", type=parse_circuit, required=True)
    args = parser.parse_args()
    certificate_path = HERE / f"{args.prefix}_certificate.json"
    certificate = json.loads(certificate_path.read_text())
    if certificate["verdict"] != "EXACT_MANDATORY_RAIL_NULLSPACE_BYPASS_PASS":
        raise AssertionError("unexpected bypass verdict")
    certificate_circuit = tuple(certificate["circuit"])
    if certificate_circuit != args.expected_circuit:
        raise AssertionError((
            "certificate circuit mismatch",
            certificate_circuit,
            args.expected_circuit,
        ))
    raw_files = {
        name: ROOT / relative for name, relative in certificate["raw_files"].items()
    }
    exact_files = {
        name: ROOT / relative for name, relative in certificate["exact_files"].items()
    }
    for name, path in raw_files.items():
        if sha256(path) != certificate["raw_sha256"][name]:
            raise AssertionError((name, "raw SHA mismatch"))
    snapshots, repair = repair_snapshots(raw_files)
    if repair != certificate["repair"]:
        raise AssertionError("independent snapshot repair audit mismatch")
    for name, points in snapshots.items():
        if source.ex.read_rows(exact_files[name]) != points:
            raise AssertionError((name, "exact point table mismatch"))
    names = (("source", "pre"), ("pre", "lifted"), ("lifted", "endpoint"))
    paths = [make_path(snapshots[left], snapshots[right]) for left, right in names]
    stored_faces = json.loads((ROOT / certificate["face_file"]).read_text())
    if canonical_hash(stored_faces) != certificate["face_hash"]:
        raise AssertionError("stored face hash mismatch")
    if len(certificate["segments"]) != len(names):
        raise AssertionError("unexpected segment count")

    for index, (record, path, (left_name, right_name)) in enumerate(
        zip(certificate["segments"], paths, names)
    ):
        if (
            record["index"] != index
            or record["left"] != left_name
            or record["right"] != right_name
        ):
            raise AssertionError("segment order mismatch")
        midpoint = evaluate_path(path, Q(1, 2))
        faces, _ = source.fresh_faces(midpoint)
        if faces != stored_faces or canonical_hash(faces) != record["face_hash"]:
            raise AssertionError((record["index"], "face reconstruction"))
        support, mechanics = source.assert_cell(midpoint, faces)
        if support["f_vector"] != [60, 158, 100] or mechanics["class"] != [2, 2, 2]:
            raise AssertionError((support["f_vector"], mechanics["class"]))
        if (
            record["f_vector"] != support["f_vector"]
            or record["active_labels"] != support["active_labels"]
            or record["mechanics"] != mechanics
        ):
            raise AssertionError((record["index"], "cell ledger mismatch"))
        cover = source.exact_class_cover(path, faces, Q(0), Q(1))
        if (
            cover != record["class_cover"]
            or len(cover) != record["class_cover_subinterval_count"]
        ):
            raise AssertionError((record["index"], "class cover mismatch"))
        circuit_packet = circuit_segment_packet(path, certificate_circuit)
        if circuit_packet["sign_record"] != record["mandatory_circuit_sign"]:
            raise AssertionError((record["index"], "circuit sign mismatch"))
        if (
            circuit_packet["endpoint_values"]
            != record["mandatory_circuit_endpoint_values"]
        ):
            raise AssertionError((record["index"], "circuit endpoint mismatch"))

    reference = selected_residuals(snapshots["source"], stored_faces)
    endpoint = selected_residuals(snapshots["endpoint"], stored_faces)
    comparison = comparison_packet(reference, endpoint)
    if comparison != certificate["endpoint_material_comparison"]:
        raise AssertionError("endpoint material comparison mismatch")
    clearance = {
        name: circuit_clearance_packet(points, stored_faces, certificate_circuit)
        for name, points in snapshots.items()
    }
    if clearance != certificate["circuit_clearance_at_checkpoints"]:
        raise AssertionError("circuit clearance reconstruction mismatch")
    for relative, expected in certificate["generated_sha256"].items():
        if sha256(ROOT / relative) != expected:
            raise AssertionError(("SHA mismatch", relative))

    print("INDEPENDENT_EXACT_MANDATORY_RAIL_NULLSPACE_BYPASS_PASS")


if __name__ == "__main__":
    main()
