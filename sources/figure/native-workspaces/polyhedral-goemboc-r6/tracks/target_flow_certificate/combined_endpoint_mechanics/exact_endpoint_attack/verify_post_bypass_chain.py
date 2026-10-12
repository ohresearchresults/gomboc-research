#!/usr/bin/env python3
"""Independent reconstruction of a piecewise exact post-bypass material chain."""
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
sys.path[:0] = [str(PARENT), str(HERE)]

import build_u54_material_exact_path as source  # noqa: E402


RESIDUAL_NAMES = ("S_quad", "U54", "H67_beta2", "H910_beta2")
BYPASS_VERDICT = "EXACT_MANDATORY_RAIL_NULLSPACE_BYPASS_PASS"
CHAIN_VERDICT = "EXACT_POST_BYPASS_MATERIAL_CHAIN_PASS"
HISTORICAL_FLOOR_MODE = "historical_no_clearance_floor"
GUARDED_FLOOR_MODE = "guarded_by_exact_clearance_floor"
INHERITED_FLOOR_SOURCE_KIND = "inherited_version_2_guarded_chain"
HISTORICAL_FLOOR_STATEMENT = (
    "The optional --clearance-floor-certificate was not supplied; "
    "this certificate intentionally preserves the historical chain "
    "contract and makes no circuit-clearance-floor claim."
)
GUARDED_FLOOR_DEFINITION = (
    "clearance_v^2 = n*s^2*D^2/(N_R*C_opposite,v^2), s=4*d6, "
    "and tau_v = clearance_v^2/kappa^2; the guarded floor is "
    "tau_v >= 1 for both non-rail circuit vertices"
)


def parse_expected_circuit(value: str) -> tuple[int, int, int, int]:
    try:
        circuit = tuple(int(item) for item in value.split(","))
    except ValueError as error:
        raise argparse.ArgumentTypeError(
            "expected circuit must contain four integer labels"
        ) from error
    if len(circuit) != 4 or len(set(circuit)) != 4:
        raise argparse.ArgumentTypeError(
            "expected circuit must contain four distinct labels"
        )
    return circuit


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def display_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(ROOT.resolve()))
    except ValueError:
        return str(resolved)


def resolve_from(base: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else base / path


def exact_fraction(value, field: str) -> Q:
    if not isinstance(value, str):
        raise AssertionError((field, "exact rational is not a string"))
    try:
        parsed = Q(value)
    except (ValueError, ZeroDivisionError) as error:
        raise AssertionError((field, "invalid exact rational")) from error
    if source.ex.qs(parsed) != value:
        raise AssertionError((field, "noncanonical exact rational"))
    return parsed


def exact_fraction_map(packet, field: str, labels) -> dict[str, Q]:
    if not isinstance(packet, dict) or set(packet) != set(labels):
        raise AssertionError((field, "wrong vertex labels"))
    return {
        label: exact_fraction(packet[label], f"{field}.{label}")
        for label in labels
    }


def valid_sha256(value) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    )


def historical_floor_guard():
    return {
        "mode": HISTORICAL_FLOOR_MODE,
        "enabled": False,
        "source_certificate": None,
        "statement": HISTORICAL_FLOOR_STATEMENT,
    }


def validated_generated_files(certificate, values, field: str):
    if len(values) != len(set(values)):
        raise AssertionError((field, "generated file list contains duplicates"))
    generated = certificate.get("generated_sha256")
    if not isinstance(generated, dict) or set(generated) != set(values):
        raise AssertionError((field, "generated file ledger mismatch"))
    hashes = {}
    for value in values:
        if not isinstance(value, str) or not value:
            raise AssertionError((field, "generated path is malformed"))
        expected = generated[value]
        if not valid_sha256(expected):
            raise AssertionError((field, value, "generated SHA is malformed"))
        path = resolve_from(ROOT, value)
        if not path.is_file():
            raise FileNotFoundError(path)
        if sha256(path) != expected:
            raise AssertionError((field, value, "generated SHA mismatch"))
        hashes[value] = expected
    return hashes


def validated_certificate_faces(certificate, field: str):
    value = certificate.get("face_file")
    if not isinstance(value, str) or not value:
        raise AssertionError((field, "certificate has no face file"))
    path = resolve_from(ROOT, value)
    if not path.is_file():
        raise FileNotFoundError(path)
    generated = certificate.get("generated_sha256")
    if not isinstance(generated, dict):
        raise AssertionError((field, "certificate has no generated hashes"))
    file_sha256 = generated.get(value)
    if not valid_sha256(file_sha256) or sha256(path) != file_sha256:
        raise AssertionError((field, "face-file SHA mismatch"))
    faces = json.loads(path.read_text())
    face_hash = certificate.get("face_hash")
    if not valid_sha256(face_hash) or canonical_hash(faces) != face_hash:
        raise AssertionError((field, "face ledger hash mismatch"))
    return {
        "value": value,
        "file": path,
        "file_sha256": file_sha256,
        "face_hash": face_hash,
        "faces": faces,
    }


def exact_checkpoint_clearance(checkpoint_file: Path, faces, circuit):
    points = source.ex.read_rows(checkpoint_file)
    if any(label not in points for label in circuit):
        raise AssertionError("clearance circuit label absent from checkpoint")
    site_count = len(points)
    if site_count <= 0:
        raise AssertionError("clearance checkpoint has no stored sites")
    d6, centroid_numerator = source.ex.exact_centroid_numerators(points, faces)
    if d6 <= 0:
        raise AssertionError("nonpositive checkpoint volume")
    scale = 4 * d6
    radius_numerator = sum(
        (
            source.ex.norm2(
                tuple(
                    scale * points[label][axis] - centroid_numerator[axis]
                    for axis in range(3)
                )
            )
            for label in points
        ),
        Q(0),
    )
    if radius_numerator <= 0:
        raise AssertionError("nonpositive checkpoint radius numerator")
    radius_squared = radius_numerator / (site_count * scale * scale)
    a, b, c, d = circuit
    determinant = source.ex.det3(
        source.ex.sub(points[b], points[a]),
        source.ex.sub(points[c], points[a]),
        source.ex.sub(points[d], points[a]),
    )
    opposite_cross_squared = {
        str(a): source.ex.norm2(
            source.ex.cross(
                source.ex.sub(points[c], points[b]),
                source.ex.sub(points[d], points[b]),
            )
        ),
        str(b): source.ex.norm2(
            source.ex.cross(
                source.ex.sub(points[c], points[a]),
                source.ex.sub(points[d], points[a]),
            )
        ),
    }
    if not determinant or any(
        value <= 0 for value in opposite_cross_squared.values()
    ):
        raise AssertionError("degenerate checkpoint clearance geometry")
    clearance_squared = {
        label: determinant * determinant / (radius_squared * cross_squared)
        for label, cross_squared in opposite_cross_squared.items()
    }
    return {
        "site_count": site_count,
        "determinant": determinant,
        "radius_squared": radius_squared,
        "opposite_cross_squared": opposite_cross_squared,
        "clearance_squared": clearance_squared,
    }


def exact_endpoint_tau_ratios(packet, labels, kappa_squared, field: str):
    if not isinstance(packet, dict) or set(packet) != set(labels):
        raise AssertionError((field, "wrong endpoint tau vertices"))
    clearances = {}
    expected_keys = {
        "clearance_squared_exact",
        "tau_ratio_exact",
        "tau_ratio_decimal",
        "clearance_over_kappa_decimal",
    }
    for label in labels:
        row = packet[label]
        if not isinstance(row, dict) or set(row) != expected_keys:
            raise AssertionError((field, label, "malformed endpoint tau packet"))
        clearance = exact_fraction(
            row["clearance_squared_exact"],
            f"{field}.{label}.clearance_squared_exact",
        )
        tau_ratio = exact_fraction(
            row["tau_ratio_exact"],
            f"{field}.{label}.tau_ratio_exact",
        )
        if clearance <= kappa_squared or tau_ratio != clearance / kappa_squared:
            raise AssertionError((field, label, "endpoint tau identity mismatch"))
        tau_decimal = row["tau_ratio_decimal"]
        clearance_decimal = row["clearance_over_kappa_decimal"]
        if (
            isinstance(tau_decimal, bool)
            or not isinstance(tau_decimal, (int, float))
            or not math.isfinite(tau_decimal)
            or tau_decimal != float(tau_ratio)
            or isinstance(clearance_decimal, bool)
            or not isinstance(clearance_decimal, (int, float))
            or not math.isfinite(clearance_decimal)
            or clearance_decimal != math.sqrt(float(tau_ratio))
        ):
            raise AssertionError((field, label, "endpoint tau decimal mismatch"))
        clearances[label] = clearance
    return clearances


def accepted_raw_files(report_file: Path, report) -> list[Path]:
    history = report.get("history")
    if not isinstance(history, list):
        raise AssertionError("SLP report history is not a list")
    accepted = [record for record in history if bool(record.get("accepted"))]
    if not accepted:
        raise AssertionError("SLP report has no accepted checkpoints")

    files = []
    for record in accepted:
        endpoint = record.get("endpoint_file")
        if not isinstance(endpoint, str) or not endpoint:
            raise AssertionError("accepted checkpoint has no endpoint file")
        path = resolve_from(report_file.parent, endpoint)
        if not path.is_file():
            raise FileNotFoundError(path)
        files.append(path)
    return files


def project_base(rows, anchor, normal, normal_norm2):
    points = dict(rows)
    corrections = {}
    for label in source.BASE:
        coefficient = (
            source.ex.dot(normal, source.ex.sub(points[label], anchor))
            / normal_norm2
        )
        points[label] = source.ex.sub(
            points[label], source.ex.mul(normal, coefficient)
        )
        corrections[label] = coefficient
        if source.ex.dot(normal, source.ex.sub(points[label], anchor)):
            raise AssertionError(("base projection failed", label))
    nonzero = [value for value in corrections.values() if value]
    return points, {
        "nonzero_count": len(nonzero),
        "maximum_log10_abs": (
            max(source.ex.qlog10(value) for value in nonzero)
            if nonzero
            else None
        ),
        "exact_digest": canonical_hash(
            {
                str(label): source.ex.qs(value)
                for label, value in sorted(corrections.items())
            }
        ),
    }


def quad_barycentric(point, a, b, c):
    first = source.ex.sub(b, a)
    second = source.ex.sub(c, a)
    offset = source.ex.sub(point, a)
    first2 = source.ex.dot(first, first)
    mixed = source.ex.dot(first, second)
    second2 = source.ex.dot(second, second)
    offset_first = source.ex.dot(offset, first)
    offset_second = source.ex.dot(offset, second)
    determinant = first2 * second2 - mixed * mixed
    if not determinant:
        raise AssertionError("degenerate exact quadrilateral chart")
    return (
        (offset_first * second2 - offset_second * mixed) / determinant,
        (offset_second * first2 - offset_first * mixed) / determinant,
    )


def repair_quad(rows):
    points = dict(rows)
    u, v = quad_barycentric(
        points[246], points[7], points[8], points[245]
    )
    repaired = source.ex.add(
        points[7],
        source.ex.add(
            source.ex.mul(source.ex.sub(points[8], points[7]), u),
            source.ex.mul(source.ex.sub(points[245], points[7]), v),
        ),
    )
    displacement = source.ex.sub(repaired, points[246])
    displacement_norm2 = source.ex.norm2(displacement)
    points[246] = repaired
    return points, (u, v), {
        "barycentric": [source.ex.qs(u), source.ex.qs(v)],
        "displacement_norm2_exact": source.ex.qs(displacement_norm2),
        "displacement_norm_decimal": math.sqrt(float(displacement_norm2)),
    }


def repair_snapshots(raw_snapshots):
    if not raw_snapshots:
        raise AssertionError("empty raw chain")
    labels = set(raw_snapshots[0])
    if any(set(rows) != labels for rows in raw_snapshots[1:]):
        raise AssertionError("raw checkpoint labels differ")

    first = raw_snapshots[0]
    anchor = first[0]
    normal = source.ex.cross(
        source.ex.sub(first[1], anchor), source.ex.sub(first[2], anchor)
    )
    normal_norm2 = source.ex.norm2(normal)
    if not normal_norm2:
        raise AssertionError("degenerate common base plane")

    repaired = []
    audit = []
    for rows in raw_snapshots:
        points, base = project_base(rows, anchor, normal, normal_norm2)
        points, uv, quad = repair_quad(points)
        repaired.append(points)
        audit.append(
            {
                "base": base,
                "quad": quad,
                "quad_barycentric": [
                    source.ex.qs(uv[0]),
                    source.ex.qs(uv[1]),
                ],
            }
        )
    return repaired, audit


def affine_exact_path(left, right):
    if set(left) != set(right):
        raise AssertionError("segment endpoint labels differ")
    path = {
        label: tuple(
            source.P((left[label][axis], right[label][axis] - left[label][axis]))
            for axis in range(3)
        )
        for label in left
        if label != 246
    }
    left_uv = quad_barycentric(left[246], left[7], left[8], left[245])
    right_uv = quad_barycentric(right[246], right[7], right[8], right[245])
    u = source.P((left_uv[0], right_uv[0] - left_uv[0]))
    v = source.P((left_uv[1], right_uv[1] - left_uv[1]))
    path[246] = source.ex.add(
        path[7],
        source.ex.add(
            source.ex.mul(source.ex.sub(path[8], path[7]), u),
            source.ex.mul(source.ex.sub(path[245], path[7]), v),
        ),
    )
    if source.determinant_polynomial(path, source.QUAD) != source.P.zero():
        raise AssertionError("protected quadrilateral is not identically planar")
    if source.evaluate_path(path, Q(0)) != left:
        raise AssertionError("exact path misses left endpoint")
    if source.evaluate_path(path, Q(1)) != right:
        raise AssertionError("exact path misses right endpoint")
    return path


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

    if tuple(values) != RESIDUAL_NAMES:
        raise AssertionError("selected residual set changed")
    if any(value <= 0 for value, _power in values.values()):
        raise AssertionError(("nonpositive selected residual", values))
    return values


def comparison_packet(reference, endpoint):
    if set(reference) != set(RESIDUAL_NAMES) or set(endpoint) != set(
        RESIDUAL_NAMES
    ):
        raise AssertionError("four-residual comparison set mismatch")
    packet = {}
    for name in RESIDUAL_NAMES:
        left, power = reference[name]
        right, right_power = endpoint[name]
        if power != right_power or not right < left:
            raise AssertionError(
                ("endpoint residual not improved", name, left, right)
            )
        ratio_power = right / left
        packet[name] = {
            "power": power,
            "exact_ratio_to_power": source.ex.qs(ratio_power),
            "decimal_ratio": math.sqrt(float(ratio_power)),
            "strictly_improved": True,
        }
    return packet


def validate_floor_guard_envelope(guard, circuit) -> str:
    if not isinstance(guard, dict):
        raise AssertionError("version-2 certificate has no clearance-floor schema")
    mode = guard.get("mode")
    if mode == HISTORICAL_FLOOR_MODE:
        if guard != historical_floor_guard():
            raise AssertionError("invalid explicit historical no-floor schema")
        return mode
    if mode != GUARDED_FLOOR_MODE:
        raise AssertionError(("unknown clearance-floor mode", mode))
    if guard.get("enabled") is not True:
        raise AssertionError("guarded clearance floor is not enabled")
    if tuple(guard.get("circuit", ())) != tuple(circuit):
        raise AssertionError("clearance-floor guard circuit mismatch")
    if guard.get("source_verdict") != BYPASS_VERDICT:
        raise AssertionError("clearance-floor source verdict mismatch")
    return mode


def reconstruct_floor_source(guard, circuit, source_file: Path):
    source_kind = guard.get("floor_source_kind")
    if source_kind is not None:
        if source_kind != INHERITED_FLOOR_SOURCE_KIND:
            raise AssertionError(("unknown guarded floor source kind", source_kind))
        return reconstruct_inherited_floor_source(
            guard,
            circuit,
            source_file,
        )

    certificate_value = guard.get("source_certificate")
    if not isinstance(certificate_value, str) or not certificate_value:
        raise AssertionError("guarded mode has no source bypass certificate")
    certificate_file = resolve_from(ROOT, certificate_value)
    if not certificate_file.is_file():
        raise FileNotFoundError(certificate_file)

    certificate_sha256 = sha256(certificate_file)
    declared_certificate_sha256 = guard.get("source_certificate_sha256")
    if not valid_sha256(declared_certificate_sha256):
        raise AssertionError("source bypass certificate SHA is malformed")
    if declared_certificate_sha256 != certificate_sha256:
        raise AssertionError("source bypass certificate SHA mismatch")

    certificate = json.loads(certificate_file.read_text())
    if certificate.get("version") != 1:
        raise AssertionError("unsupported source bypass certificate version")
    if certificate.get("verdict") != BYPASS_VERDICT:
        raise AssertionError("source bypass certificate verdict mismatch")
    if tuple(certificate.get("circuit", ())) != tuple(circuit):
        raise AssertionError("source bypass certificate circuit mismatch")

    exact_files = certificate.get("exact_files")
    if not isinstance(exact_files, dict) or set(exact_files) != {
        "source",
        "pre",
        "lifted",
        "endpoint",
    }:
        raise AssertionError("source bypass certificate has no exact files")
    endpoint_value = exact_files.get("endpoint")
    if not isinstance(endpoint_value, str) or not endpoint_value:
        raise AssertionError("source bypass certificate has no exact endpoint")
    endpoint_file = resolve_from(ROOT, endpoint_value)
    if not endpoint_file.is_file():
        raise FileNotFoundError(endpoint_file)

    generated_sha256 = certificate.get("generated_sha256")
    if not isinstance(generated_sha256, dict):
        raise AssertionError("source bypass certificate has no generated hashes")
    face_value = certificate.get("face_file")
    if not isinstance(face_value, str) or not face_value:
        raise AssertionError("source bypass certificate has no face file")
    validated_generated_files(
        certificate,
        [*exact_files.values(), face_value],
        "source bypass",
    )
    endpoint_sha256 = generated_sha256.get(endpoint_value)
    if not valid_sha256(endpoint_sha256):
        raise AssertionError("source bypass endpoint SHA is malformed")
    if sha256(endpoint_file) != endpoint_sha256:
        raise AssertionError("source bypass endpoint SHA mismatch")
    chain_source_sha256 = sha256(source_file)
    if chain_source_sha256 != endpoint_sha256:
        raise AssertionError(
            "guarded chain source is not the source bypass endpoint"
        )

    checkpoint_clearance = certificate.get("circuit_clearance_at_checkpoints")
    if not isinstance(checkpoint_clearance, dict):
        raise AssertionError("source bypass certificate has no clearances")
    endpoint_clearance = checkpoint_clearance.get("endpoint")
    if not isinstance(endpoint_clearance, dict):
        raise AssertionError("source bypass certificate has no endpoint clearance")
    if endpoint_clearance.get("strictly_positive") is not True:
        raise AssertionError("source bypass endpoint clearance is not positive")

    labels = tuple(str(label) for label in circuit[:2])
    determinant = exact_fraction(
        endpoint_clearance.get("determinant"),
        "source_endpoint_clearance.determinant",
    )
    radius_squared = exact_fraction(
        endpoint_clearance.get("rms_radius_squared"),
        "source_endpoint_clearance.rms_radius_squared",
    )
    opposite_area_squared = exact_fraction_map(
        endpoint_clearance.get("opposite_area_squared"),
        "source_endpoint_clearance.opposite_area_squared",
        labels,
    )
    source_clearance_squared = exact_fraction_map(
        endpoint_clearance.get("normalized_opposite_slack_squared"),
        "source_endpoint_clearance.normalized_opposite_slack_squared",
        labels,
    )
    if not determinant or radius_squared <= 0 or any(
        value <= 0 for value in opposite_area_squared.values()
    ):
        raise AssertionError("nonpositive source clearance denominator")
    for label in labels:
        reconstructed = (
            determinant * determinant
            / (radius_squared * opposite_area_squared[label])
        )
        if source_clearance_squared[label] != reconstructed:
            raise AssertionError((label, "source clearance identity mismatch"))

    kappa_squared = exact_fraction(
        endpoint_clearance.get("minimum_normalized_opposite_slack_squared"),
        "source_endpoint_clearance.minimum_normalized_opposite_slack_squared",
    )
    if (
        kappa_squared <= 0
        or kappa_squared != min(source_clearance_squared.values())
    ):
        raise AssertionError("source clearance floor is not the exact minimum")
    floor_vertices = [
        label
        for label in labels
        if source_clearance_squared[label] == kappa_squared
    ]
    if not floor_vertices:
        raise AssertionError("source clearance floor has no attaining vertex")

    source_faces = validated_certificate_faces(certificate, "source bypass")
    source_geometry = exact_checkpoint_clearance(
        endpoint_file,
        source_faces["faces"],
        circuit,
    )
    if (
        source_geometry["determinant"] != determinant
        or source_geometry["radius_squared"] != radius_squared
        or source_geometry["opposite_cross_squared"] != opposite_area_squared
        or source_geometry["clearance_squared"] != source_clearance_squared
    ):
        raise AssertionError("source bypass endpoint geometry mismatch")

    if guard.get("source_endpoint_file") != endpoint_value:
        raise AssertionError("guard source endpoint path mismatch")
    if guard.get("source_endpoint_sha256") != endpoint_sha256:
        raise AssertionError("guard source endpoint SHA mismatch")
    if guard.get("chain_source_sha256") != chain_source_sha256:
        raise AssertionError("guard chain source SHA mismatch")
    if exact_fraction(
        guard.get("kappa_squared_exact"), "guard.kappa_squared_exact"
    ) != kappa_squared:
        raise AssertionError("guard kappa mismatch")
    declared_source_clearance = exact_fraction_map(
        guard.get("source_clearance_squared_exact"),
        "guard.source_clearance_squared_exact",
        labels,
    )
    if declared_source_clearance != source_clearance_squared:
        raise AssertionError("guard source clearances mismatch")
    if guard.get("source_floor_vertices") != floor_vertices:
        raise AssertionError("guard source floor vertices mismatch")

    return {
        "kappa_squared": kappa_squared,
        "source_clearance_squared": source_clearance_squared,
        "source_floor_vertices": floor_vertices,
        "source_faces": source_faces,
        "source_geometry": source_geometry,
        "record": {
            "mode": GUARDED_FLOOR_MODE,
            "enabled": True,
            "definition": GUARDED_FLOOR_DEFINITION,
            "source_certificate": display_path(certificate_file),
            "source_certificate_sha256": certificate_sha256,
            "source_verdict": BYPASS_VERDICT,
            "circuit": list(circuit),
            "source_endpoint_file": endpoint_value,
            "source_endpoint_sha256": endpoint_sha256,
            "chain_source_sha256": chain_source_sha256,
            "kappa_squared_exact": source.ex.qs(kappa_squared),
            "source_clearance_squared_exact": {
                label: source.ex.qs(source_clearance_squared[label])
                for label in labels
            },
            "source_floor_vertices": floor_vertices,
        },
    }


def reconstruct_inherited_floor_source(guard, circuit, source_file: Path):
    parent_value = guard.get("parent_chain_certificate")
    if not isinstance(parent_value, str) or not parent_value:
        raise AssertionError("inherited floor has no parent chain certificate")
    parent_file = resolve_from(ROOT, parent_value)
    if not parent_file.is_file():
        raise FileNotFoundError(parent_file)
    parent_sha256 = sha256(parent_file)
    declared_parent_sha256 = guard.get("parent_chain_certificate_sha256")
    if not valid_sha256(declared_parent_sha256):
        raise AssertionError("parent chain certificate SHA is malformed")
    if declared_parent_sha256 != parent_sha256:
        raise AssertionError("parent chain certificate SHA mismatch")

    parent = json.loads(parent_file.read_text())
    if parent.get("version") != 2:
        raise AssertionError("parent chain certificate is not version 2")
    if parent.get("verdict") != CHAIN_VERDICT:
        raise AssertionError("parent chain verdict mismatch")
    if tuple(parent.get("circuit", ())) != tuple(circuit):
        raise AssertionError("parent chain circuit mismatch")
    parent_guard = parent.get("clearance_floor_guard")
    if not isinstance(parent_guard, dict):
        raise AssertionError("parent chain has no clearance-floor guard")
    if parent_guard.get("mode") == HISTORICAL_FLOOR_MODE:
        raise AssertionError("historical parent cannot supply a floor")
    if (
        parent_guard.get("mode") != GUARDED_FLOOR_MODE
        or parent_guard.get("enabled") is not True
    ):
        raise AssertionError("parent guarded mode is malformed")
    if parent_guard.get("all_segments_floor_safe") is not True:
        raise AssertionError("parent does not certify all floor segments safe")
    if tuple(parent_guard.get("circuit", ())) != tuple(circuit):
        raise AssertionError("parent guard circuit mismatch")

    original_endpoint_value = parent_guard.get("source_endpoint_file")
    if not isinstance(original_endpoint_value, str) or not original_endpoint_value:
        raise AssertionError("parent has no original bypass endpoint")
    original_endpoint_file = resolve_from(ROOT, original_endpoint_value)
    if not original_endpoint_file.is_file():
        raise FileNotFoundError(original_endpoint_file)
    original_guard = dict(parent_guard)
    original_guard.pop("floor_source_kind", None)
    original_guard["chain_source_sha256"] = parent_guard.get(
        "source_endpoint_sha256"
    )
    original_source = reconstruct_floor_source(
        original_guard,
        circuit,
        original_endpoint_file,
    )
    for key, expected in original_source["record"].items():
        if key == "chain_source_sha256":
            continue
        if parent_guard.get(key) != expected:
            raise AssertionError((key, "parent bypass lineage mismatch"))

    segment_count = parent.get("segment_count")
    if (
        isinstance(segment_count, bool)
        or not isinstance(segment_count, int)
        or segment_count <= 0
    ):
        raise AssertionError("parent segment count is malformed")
    if parent.get("accepted_checkpoint_count") != segment_count:
        raise AssertionError("parent accepted-checkpoint count mismatch")
    material_segments = parent.get("segments")
    floor_segments = parent_guard.get("segments")
    if (
        not isinstance(material_segments, list)
        or len(material_segments) != segment_count
        or not isinstance(floor_segments, list)
        or len(floor_segments) != segment_count
        or parent_guard.get("certified_segment_count") != segment_count
    ):
        raise AssertionError("parent material/floor segment count mismatch")

    checkpoint_values = parent.get("exact_checkpoint_files")
    if not isinstance(checkpoint_values, list) or any(
        not isinstance(value, str) or not value for value in checkpoint_values
    ):
        raise AssertionError("parent checkpoint chain is malformed")
    if (
        len(checkpoint_values) != segment_count + 1
        or len(set(checkpoint_values)) != len(checkpoint_values)
    ):
        raise AssertionError("parent checkpoint chain is malformed")
    parent_faces = validated_certificate_faces(parent, "parent chain")
    generated_hashes = validated_generated_files(
        parent,
        [*checkpoint_values, parent_faces["value"]],
        "parent chain",
    )
    checkpoint_files = [resolve_from(ROOT, value) for value in checkpoint_values]
    checkpoint_sha256 = [generated_hashes[value] for value in checkpoint_values]

    parent_source_value = parent.get("source")
    if not isinstance(parent_source_value, str) or not parent_source_value:
        raise AssertionError("parent chain has no source")
    parent_source_file = resolve_from(ROOT, parent_source_value)
    if not parent_source_file.is_file():
        raise FileNotFoundError(parent_source_file)
    parent_source_sha256 = sha256(parent_source_file)
    if (
        parent_guard.get("chain_source_sha256") != parent_source_sha256
        or checkpoint_sha256[0] != parent_source_sha256
    ):
        raise AssertionError("parent source/checkpoint junction mismatch")

    labels = tuple(str(label) for label in circuit[:2])
    kappa_squared = original_source["kappa_squared"]
    checkpoints = [source.ex.read_rows(path) for path in checkpoint_files]
    geometries = [
        exact_checkpoint_clearance(path, parent_faces["faces"], circuit)
        for path in checkpoint_files
    ]
    if any(
        geometry["site_count"]
        != original_source["source_geometry"]["site_count"]
        for geometry in geometries
    ):
        raise AssertionError("parent checkpoint site count changed")

    previous_endpoint = None
    reconstructed_floor_segments = []
    for index, (material_segment, floor_segment) in enumerate(
        zip(material_segments, floor_segments)
    ):
        left_name = f"checkpoint_{index:03d}"
        right_name = f"checkpoint_{index + 1:03d}"
        if (
            not isinstance(material_segment, dict)
            or material_segment.get("left") != left_name
            or material_segment.get("right") != right_name
            or not isinstance(floor_segment, dict)
            or floor_segment.get("left") != left_name
            or floor_segment.get("right") != right_name
        ):
            raise AssertionError((index, "parent segment junction is malformed"))
        if exact_fraction(
            floor_segment.get("kappa_squared_exact"),
            f"parent.floor_segments[{index}].kappa_squared_exact",
        ) != kappa_squared:
            raise AssertionError((index, "parent segment resets kappa"))

        path = affine_exact_path(checkpoints[index], checkpoints[index + 1])
        result = clearance_floor_segment_record(
            path,
            parent_faces["faces"],
            circuit,
            kappa_squared,
        )
        reconstructed = {
            "left": left_name,
            "right": right_name,
            **result["record"],
        }
        packet_clearance = exact_endpoint_tau_ratios(
            floor_segment.get("endpoint_tau_ratios"),
            labels,
            kappa_squared,
            f"parent.floor_segments[{index}].endpoint_tau_ratios",
        )
        if floor_segment != reconstructed:
            raise AssertionError((index, "parent G_v proof mismatch"))
        if result["source_clearance_squared"] != geometries[index][
            "clearance_squared"
        ]:
            raise AssertionError((index, "parent source clearance mismatch"))
        if result["endpoint_clearance_squared"] != geometries[index + 1][
            "clearance_squared"
        ]:
            raise AssertionError((index, "parent endpoint clearance mismatch"))
        if previous_endpoint is not None and (
            result["source_clearance_squared"] != previous_endpoint
        ):
            raise AssertionError((index, "parent clearance junction mismatch"))
        if packet_clearance != result["endpoint_clearance_squared"]:
            raise AssertionError((index, "parent endpoint tau/geometry mismatch"))
        previous_endpoint = result["endpoint_clearance_squared"]
        reconstructed_floor_segments.append(reconstructed)

    parent_endpoint_tau_ratios = parent_guard.get("chain_endpoint_tau_ratios")
    if parent_endpoint_tau_ratios != reconstructed_floor_segments[-1].get(
        "endpoint_tau_ratios"
    ):
        raise AssertionError("parent final tau packet is not the final segment")
    parent_endpoint_clearance = exact_endpoint_tau_ratios(
        parent_endpoint_tau_ratios,
        labels,
        kappa_squared,
        "parent.chain_endpoint_tau_ratios",
    )
    if parent_endpoint_clearance != geometries[-1]["clearance_squared"]:
        raise AssertionError("parent endpoint tau/geometry identity mismatch")

    parent_endpoint_value = checkpoint_values[-1]
    parent_endpoint_sha256 = checkpoint_sha256[-1]
    if sha256(source_file) != parent_endpoint_sha256:
        raise AssertionError("new chain source is not the parent endpoint")
    if guard.get("chain_source_sha256") != parent_endpoint_sha256:
        raise AssertionError("flattened chain source SHA mismatch")

    record = dict(original_source["record"])
    record["chain_source_sha256"] = parent_endpoint_sha256
    record.update(
        {
            "floor_source_kind": INHERITED_FLOOR_SOURCE_KIND,
            "parent_chain_certificate": display_path(parent_file),
            "parent_chain_certificate_sha256": parent_sha256,
            "parent_chain_source_file": parent_source_value,
            "parent_chain_source_sha256": parent_source_sha256,
            "parent_chain_endpoint_file": parent_endpoint_value,
            "parent_chain_endpoint_sha256": parent_endpoint_sha256,
            "parent_chain_segment_count": segment_count,
            "parent_chain_all_segments_floor_safe": True,
            "parent_chain_endpoint_clearance_squared_exact": {
                label: source.ex.qs(parent_endpoint_clearance[label])
                for label in labels
            },
            "parent_chain_endpoint_tau_ratios": parent_endpoint_tau_ratios,
            "original_source_face_file": original_source["source_faces"][
                "value"
            ],
            "original_source_face_file_sha256": original_source[
                "source_faces"
            ]["file_sha256"],
            "original_source_face_hash": original_source["source_faces"][
                "face_hash"
            ],
            "original_source_site_count": original_source["source_geometry"][
                "site_count"
            ],
        }
    )
    return {
        "kappa_squared": kappa_squared,
        "source_clearance_squared": parent_endpoint_clearance,
        "source_floor_vertices": [],
        "source_faces": original_source["source_faces"],
        "source_geometry": original_source["source_geometry"],
        "parent_endpoint_geometry": geometries[-1],
        "record": record,
    }


def positive_interval_receipt(poly, name: str):
    endpoint_values = (poly.eval(Q(0)), poly.eval(Q(1)))
    if any(value <= 0 for value in endpoint_values):
        raise AssertionError((name, "nonpositive interval endpoint"))
    try:
        sign, leaves, worst = source.ex.bernstein_sign(
            poly, Q(0), Q(1), max_depth=60
        )
    except AssertionError as error:
        raise AssertionError(
            (name, "strict positivity not Bernstein-certified")
        ) from error
    if sign != 1:
        raise AssertionError((name, "unexpected Bernstein sign", sign))
    return {
        "interval": ["0", "1"],
        "sign": sign,
        "degree": poly.degree,
        "bernstein_leaf_count": leaves,
        "minimum_bernstein_log10_abs": worst,
        "polynomial_digest": canonical_hash(poly.exact()),
    }


def factor_exact_source_zero(poly, name: str):
    multiplicity = 0
    while multiplicity < len(poly.c) and poly.c[multiplicity] == 0:
        multiplicity += 1
    if multiplicity == len(poly.c):
        raise AssertionError((name, "clearance-floor polynomial is zero"))
    if not multiplicity:
        raise AssertionError((name, "source-zero factor is absent"))
    return multiplicity, source.P(poly.c[multiplicity:])


def clearance_floor_segment_record(path, faces, circuit, kappa_squared):
    if kappa_squared <= 0:
        raise AssertionError("nonpositive exact clearance floor")
    if any(label not in path for label in circuit):
        raise AssertionError("clearance circuit label is absent from path")

    labels = tuple(str(label) for label in circuit[:2])
    d6, centroid_numerator = source.ex.exact_centroid_numerators(path, faces)
    scale = 4 * d6
    site_count = len(path)
    if site_count <= 0:
        raise AssertionError("clearance path has no stored sites")
    radius_numerator = sum(
        (
            source.ex.norm2(
                tuple(
                    scale * path[label][axis] - centroid_numerator[axis]
                    for axis in range(3)
                )
            )
            for label in path
        ),
        source.P.zero(),
    )

    a, b, c, d = circuit
    determinant = source.determinant_polynomial(path, circuit)
    opposite_cross_squared = {
        str(a): source.ex.norm2(
            source.ex.cross(
                source.ex.sub(path[c], path[b]),
                source.ex.sub(path[d], path[b]),
            )
        ),
        str(b): source.ex.norm2(
            source.ex.cross(
                source.ex.sub(path[c], path[a]),
                source.ex.sub(path[d], path[a]),
            )
        ),
    }
    tau_numerator = (
        site_count * scale * scale * determinant * determinant
    )
    shared = {
        "site_count": site_count,
        "scale_polynomial_digest": canonical_hash(scale.exact()),
        "scale_interval_receipt": positive_interval_receipt(
            scale, "clearance scale s=4*d6"
        ),
        "determinant_polynomial_digest": canonical_hash(determinant.exact()),
        "tau_numerator_polynomial_digest": canonical_hash(
            tau_numerator.exact()
        ),
        "radius_numerator_polynomial_digest": canonical_hash(
            radius_numerator.exact()
        ),
        "radius_numerator_interval_receipt": positive_interval_receipt(
            radius_numerator,
            "clearance radius numerator N_R",
        ),
    }

    vertices = {}
    source_clearance_squared = {}
    endpoint_clearance_squared = {}
    endpoint_tau_ratios = {}
    for label in labels:
        cross_squared = opposite_cross_squared[label]
        cross_receipt = positive_interval_receipt(
            cross_squared,
            f"clearance opposite cross norm squared at vertex {label}",
        )
        denominator = radius_numerator * cross_squared
        denominator_receipt = positive_interval_receipt(
            denominator,
            f"clearance denominator at vertex {label}",
        )
        guard_polynomial = (
            tau_numerator - kappa_squared * denominator
        )
        source_value = guard_polynomial.eval(Q(0))
        if source_value < 0:
            raise AssertionError((label, "clearance floor is crossed at source"))
        if source_value == 0:
            multiplicity, positive_polynomial = factor_exact_source_zero(
                guard_polynomial,
                f"clearance floor at vertex {label}",
            )
            proof_kind = "positive_quotient_after_exact_source_factor"
        else:
            multiplicity = 0
            positive_polynomial = guard_polynomial
            proof_kind = "strictly_positive_floor_polynomial"
        try:
            floor_receipt = positive_interval_receipt(
                positive_polynomial,
                f"clearance floor proof at vertex {label}",
            )
        except AssertionError as error:
            raise AssertionError((label, "clearance floor recrossing")) from error

        source_denominator = denominator.eval(Q(0))
        endpoint_denominator = denominator.eval(Q(1))
        if source_denominator <= 0 or endpoint_denominator <= 0:
            raise AssertionError((label, "nonpositive clearance denominator"))
        source_clearance = (
            tau_numerator.eval(Q(0)) / source_denominator
        )
        endpoint_clearance = (
            tau_numerator.eval(Q(1)) / endpoint_denominator
        )
        endpoint_tau_ratio = endpoint_clearance / kappa_squared
        if endpoint_tau_ratio <= 1:
            raise AssertionError((label, "endpoint clearance tau is not strict"))

        source_clearance_squared[label] = source_clearance
        endpoint_clearance_squared[label] = endpoint_clearance
        endpoint_tau_ratios[label] = {
            "clearance_squared_exact": source.ex.qs(endpoint_clearance),
            "tau_ratio_exact": source.ex.qs(endpoint_tau_ratio),
            "tau_ratio_decimal": float(endpoint_tau_ratio),
            "clearance_over_kappa_decimal": math.sqrt(
                float(endpoint_tau_ratio)
            ),
        }
        vertices[label] = {
            "source_equality": source_value == 0,
            "source_zero_multiplicity": multiplicity,
            "source_floor_polynomial_value_exact": source.ex.qs(source_value),
            "floor_polynomial_degree": guard_polynomial.degree,
            "floor_polynomial_digest": canonical_hash(
                guard_polynomial.exact()
            ),
            "proof_kind": proof_kind,
            "positive_polynomial_degree": positive_polynomial.degree,
            "positive_polynomial_digest": canonical_hash(
                positive_polynomial.exact()
            ),
            "positive_interval_receipt": floor_receipt,
            "opposite_cross_squared_polynomial_digest": canonical_hash(
                cross_squared.exact()
            ),
            "opposite_cross_squared_interval_receipt": cross_receipt,
            "denominator_polynomial_digest": canonical_hash(
                denominator.exact()
            ),
            "denominator_interval_receipt": denominator_receipt,
        }

    return {
        "record": {
            "kappa_squared_exact": source.ex.qs(kappa_squared),
            "shared_polynomials": shared,
            "vertices": vertices,
            "endpoint_tau_ratios": endpoint_tau_ratios,
        },
        "source_clearance_squared": source_clearance_squared,
        "endpoint_clearance_squared": endpoint_clearance_squared,
        "endpoint_tau_ratios": endpoint_tau_ratios,
    }


def verify_clearance_floor_guard(
    guard,
    source_file,
    segment_paths,
    faces,
    circuit,
):
    mode = validate_floor_guard_envelope(guard, circuit)
    if mode == HISTORICAL_FLOOR_MODE:
        return

    floor_source = reconstruct_floor_source(guard, circuit, source_file)
    floor_segments = []
    previous_endpoint = None
    final_tau_ratios = None
    for index, path in enumerate(segment_paths):
        result = clearance_floor_segment_record(
            path,
            faces,
            circuit,
            floor_source["kappa_squared"],
        )
        if index == 0:
            if (
                result["source_clearance_squared"]
                != floor_source["source_clearance_squared"]
            ):
                raise AssertionError(
                    "chain source clearances differ from bypass endpoint"
                )
            source_equalities = sorted(
                label
                for label, vertex in result["record"]["vertices"].items()
                if vertex["source_equality"]
            )
            if source_equalities != sorted(
                floor_source["source_floor_vertices"]
            ):
                raise AssertionError("chain source floor equalities mismatch")
        elif result["source_clearance_squared"] != previous_endpoint:
            raise AssertionError("clearance-floor segment junction mismatch")

        previous_endpoint = result["endpoint_clearance_squared"]
        final_tau_ratios = result["endpoint_tau_ratios"]
        floor_segments.append(
            {
                "left": f"checkpoint_{index:03d}",
                "right": f"checkpoint_{index + 1:03d}",
                **result["record"],
            }
        )

    if not floor_segments or previous_endpoint is None or final_tau_ratios is None:
        raise AssertionError("guarded chain has no clearance-floor segments")
    if any(
        clearance <= floor_source["kappa_squared"]
        for clearance in previous_endpoint.values()
    ):
        raise AssertionError("chain endpoint clearance tau is not strictly above one")

    reconstructed = dict(floor_source["record"])
    reconstructed.update(
        {
            "certified_segment_count": len(segment_paths),
            "all_segments_floor_safe": True,
            "segments": floor_segments,
            "chain_endpoint_tau_ratios": final_tau_ratios,
        }
    )
    if guard != reconstructed:
        raise AssertionError("clearance-floor guard reconstruction mismatch")


def segment_record(
    left_name,
    right_name,
    left,
    right,
    circuit,
    expected_faces=None,
):
    path = affine_exact_path(left, right)
    representative = source.evaluate_path(path, Q(1, 2))
    candidate_faces, _ = source.fresh_faces(representative)
    if expected_faces is None:
        faces = candidate_faces
    else:
        expected_sets = {frozenset(face) for face in expected_faces}
        candidate_sets = {frozenset(face) for face in candidate_faces}
        if (
            len(candidate_faces) != len(expected_faces)
            or candidate_sets != expected_sets
        ):
            raise AssertionError((left_name, right_name, "face lattice changed"))
        faces = expected_faces

    support, mechanics = source.assert_cell(representative, faces)
    cover = source.exact_class_cover(path, faces, Q(0), Q(1))
    determinant = source.determinant_polynomial(path, circuit)
    midpoint_value = determinant.eval(Q(1, 2))
    sign = 1 if midpoint_value > 0 else -1 if midpoint_value < 0 else 0
    if not sign:
        raise AssertionError((left_name, right_name, "circuit vanishes"))
    sign_record = source.exact_sign_record(determinant, Q(0), Q(1), sign)
    comparison = comparison_packet(
        selected_residuals(left, faces),
        selected_residuals(right, faces),
    )
    record = {
        "left": left_name,
        "right": right_name,
        "support": {
            "f_vector": support["f_vector"],
            "active_labels": support["active_labels"],
            "all_37_forced_rails_retained": source.forced_rails().issubset(
                set(support["edges"])
            ),
        },
        "mechanics": mechanics,
        "class_cover": cover,
        "class_cover_subinterval_count": len(cover),
        "mandatory_circuit_sign": sign_record,
        "material_comparison": comparison,
    }
    return faces, record, path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--slp-prefix", required=True)
    parser.add_argument("--output-prefix", required=True)
    parser.add_argument(
        "--expected-circuit",
        type=parse_expected_circuit,
        required=True,
    )
    args = parser.parse_args()

    report_file = HERE / f"{args.slp_prefix}_slp.json"
    certificate_file = HERE / f"{args.output_prefix}_certificate.json"
    certificate = json.loads(certificate_file.read_text())
    if certificate["verdict"] != "EXACT_POST_BYPASS_MATERIAL_CHAIN_PASS":
        raise AssertionError("unexpected verdict")

    expected_circuit = tuple(args.expected_circuit)
    certified_circuit = tuple(certificate.get("circuit", ()))
    if certified_circuit != expected_circuit:
        raise AssertionError(
            (
                "certificate circuit mismatch",
                list(certified_circuit),
                list(expected_circuit),
            )
        )
    if certificate.get("version") != 2:
        raise AssertionError("post-bypass chain certificate is not version 2")
    clearance_floor_guard = certificate.get("clearance_floor_guard")
    validate_floor_guard_envelope(clearance_floor_guard, expected_circuit)

    certified_report = resolve_from(ROOT, certificate["slp_report"])
    if certified_report.resolve() != report_file.resolve():
        raise AssertionError("certificate SLP report path mismatch")
    if sha256(report_file) != certificate["slp_report_sha256"]:
        raise AssertionError("SLP report hash mismatch")

    report = json.loads(report_file.read_text())
    source_file = resolve_from(ROOT, certificate["source"])
    if not source_file.is_file():
        raise FileNotFoundError(source_file)
    raw_files = [source_file, *accepted_raw_files(report_file, report)]
    if len(raw_files) - 1 != certificate["accepted_checkpoint_count"]:
        raise AssertionError("checkpoint count mismatch")

    raw_snapshots = [source.ex.read_rows(path) for path in raw_files]
    snapshots, repair = repair_snapshots(raw_snapshots)
    if repair != certificate["repair"]:
        raise AssertionError("repair reconstruction mismatch")

    exact_files = [
        resolve_from(ROOT, relative)
        for relative in certificate["exact_checkpoint_files"]
    ]
    if len(exact_files) != len(snapshots):
        raise AssertionError("exact checkpoint file count mismatch")
    for path, points in zip(exact_files, snapshots):
        if source.ex.read_rows(path) != points:
            raise AssertionError(("exact checkpoint mismatch", path.name))

    face_file = resolve_from(ROOT, certificate["face_file"])
    stored_faces = json.loads(face_file.read_text())
    if canonical_hash(stored_faces) != certificate["face_hash"]:
        raise AssertionError("stored face hash mismatch")

    reconstructed_segments = []
    segment_paths = []
    faces = None
    for index, (left, right) in enumerate(zip(snapshots, snapshots[1:])):
        candidate_faces, record, path = segment_record(
            f"checkpoint_{index:03d}",
            f"checkpoint_{index + 1:03d}",
            left,
            right,
            expected_circuit,
            faces,
        )
        if faces is None:
            faces = candidate_faces
        reconstructed_segments.append(record)
        segment_paths.append(path)
    if faces is None:
        raise AssertionError("empty exact chain")
    if faces != stored_faces:
        raise AssertionError("face reconstruction mismatch")
    if reconstructed_segments != certificate["segments"]:
        raise AssertionError("segment reconstruction mismatch")
    if len(reconstructed_segments) != certificate["segment_count"]:
        raise AssertionError("segment count mismatch")

    verify_clearance_floor_guard(
        clearance_floor_guard,
        source_file,
        segment_paths,
        faces,
        expected_circuit,
    )

    overall = comparison_packet(
        selected_residuals(snapshots[0], faces),
        selected_residuals(snapshots[-1], faces),
    )
    if overall != certificate["overall_material_comparison"]:
        raise AssertionError("overall material comparison mismatch")
    for relative, expected in certificate["generated_sha256"].items():
        if sha256(resolve_from(ROOT, relative)) != expected:
            raise AssertionError(("SHA mismatch", relative))
    print("INDEPENDENT_EXACT_POST_BYPASS_MATERIAL_CHAIN_PASS")


if __name__ == "__main__":
    main()
