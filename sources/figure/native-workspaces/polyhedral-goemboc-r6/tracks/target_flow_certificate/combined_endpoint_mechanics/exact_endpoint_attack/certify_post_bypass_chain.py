#!/usr/bin/env python3
"""Exactify every accepted segment of a post-bypass intrinsic SLP run."""
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
import certify_mandatory_rail_bypass as bypass  # noqa: E402


BYPASS_VERDICT = "EXACT_MANDATORY_RAIL_NULLSPACE_BYPASS_PASS"
CHAIN_VERDICT = "EXACT_POST_BYPASS_MATERIAL_CHAIN_PASS"
HISTORICAL_FLOOR_MODE = "historical_no_clearance_floor"
GUARDED_FLOOR_MODE = "guarded_by_exact_clearance_floor"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def display_path(path: Path) -> str:
    path = path.resolve()
    try:
        return str(path.relative_to(ROOT.resolve()))
    except ValueError:
        return str(path)


def resolve_root_path(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


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


def exact_fraction_map(packet, field: str, expected_labels) -> dict[str, Q]:
    if not isinstance(packet, dict) or set(packet) != set(expected_labels):
        raise AssertionError((field, "wrong vertex labels"))
    return {
        label: exact_fraction(packet[label], f"{field}.{label}")
        for label in expected_labels
    }


def valid_sha256(value) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    )


def validated_certificate_faces(certificate, field: str):
    face_value = certificate.get("face_file")
    if not isinstance(face_value, str) or not face_value:
        raise AssertionError((field, "certificate has no face file"))
    face_file = resolve_root_path(face_value)
    if not face_file.is_file():
        raise FileNotFoundError(face_file)
    generated_sha256 = certificate.get("generated_sha256")
    if not isinstance(generated_sha256, dict):
        raise AssertionError((field, "certificate has no generated hashes"))
    face_file_sha256 = generated_sha256.get(face_value)
    if not valid_sha256(face_file_sha256):
        raise AssertionError((field, "face-file SHA is malformed"))
    if sha256(face_file) != face_file_sha256:
        raise AssertionError((field, "face-file SHA mismatch"))
    faces = json.loads(face_file.read_text())
    face_hash = certificate.get("face_hash")
    if not valid_sha256(face_hash) or canonical_hash(faces) != face_hash:
        raise AssertionError((field, "face ledger hash mismatch"))
    return {
        "value": face_value,
        "file": face_file,
        "file_sha256": face_file_sha256,
        "face_hash": face_hash,
        "faces": faces,
    }


def exact_checkpoint_clearance(endpoint_file: Path, faces, circuit):
    points = source.ex.read_rows(endpoint_file)
    if any(label not in points for label in circuit):
        raise AssertionError("clearance circuit label absent from checkpoint")
    site_count = len(points)
    if site_count <= 0:
        raise AssertionError("clearance checkpoint has no stored sites")
    d6, centroid_numerator = source.ex.exact_centroid_numerators(points, faces)
    if d6 <= 0:
        raise AssertionError("nonpositive checkpoint volume in clearance geometry")
    scale = 4 * d6
    radius_numerator = sum(
        (
            source.ex.norm2(tuple(
                scale * points[label][axis] - centroid_numerator[axis]
                for axis in range(3)
            ))
            for label in points
        ),
        Q(0),
    )
    if radius_numerator <= 0:
        raise AssertionError("nonpositive checkpoint clearance radius numerator")
    radius_squared = radius_numerator / (site_count * scale * scale)
    a, b, c, d = circuit
    determinant = source.ex.det3(
        source.ex.sub(points[b], points[a]),
        source.ex.sub(points[c], points[a]),
        source.ex.sub(points[d], points[a]),
    )
    opposite_cross_squared = {
        str(a): source.ex.norm2(source.ex.cross(
            source.ex.sub(points[c], points[b]),
            source.ex.sub(points[d], points[b]),
        )),
        str(b): source.ex.norm2(source.ex.cross(
            source.ex.sub(points[c], points[a]),
            source.ex.sub(points[d], points[a]),
        )),
    }
    if not determinant or any(
        value <= 0 for value in opposite_cross_squared.values()
    ):
        raise AssertionError("degenerate checkpoint circuit-clearance geometry")
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
    for label in labels:
        row = packet[label]
        if not isinstance(row, dict) or set(row) != {
            "clearance_squared_exact",
            "tau_ratio_exact",
            "tau_ratio_decimal",
            "clearance_over_kappa_decimal",
        }:
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


def validated_clearance_floor_certificate(
    value: str,
    circuit,
    source_file: Path,
):
    certificate_file = Path(value)
    if not certificate_file.is_absolute():
        certificate_file = HERE / certificate_file
    if not certificate_file.is_file():
        raise FileNotFoundError(certificate_file)
    certificate = json.loads(certificate_file.read_text())
    if certificate.get("verdict") == CHAIN_VERDICT:
        return validated_parent_chain_clearance_floor_certificate(
            certificate_file,
            certificate,
            circuit,
            source_file,
        )
    if certificate.get("verdict") != BYPASS_VERDICT:
        raise AssertionError("clearance-floor certificate has wrong verdict")
    if certificate.get("version") != 1:
        raise AssertionError("clearance-floor bypass certificate is not version 1")

    certified_circuit = tuple(certificate.get("circuit", ()))
    if certified_circuit != tuple(circuit):
        raise AssertionError((
            "clearance-floor certificate circuit mismatch",
            certified_circuit,
            tuple(circuit),
        ))

    exact_files = certificate.get("exact_files")
    if not isinstance(exact_files, dict):
        raise AssertionError("clearance-floor certificate has no exact files")
    endpoint_value = exact_files.get("endpoint")
    if not isinstance(endpoint_value, str) or not endpoint_value:
        raise AssertionError("clearance-floor certificate has no exact endpoint")
    endpoint_file = resolve_root_path(endpoint_value)
    if not endpoint_file.is_file():
        raise FileNotFoundError(endpoint_file)

    generated_sha256 = certificate.get("generated_sha256")
    if not isinstance(generated_sha256, dict):
        raise AssertionError("clearance-floor certificate has no generated hashes")
    endpoint_sha256 = generated_sha256.get(endpoint_value)
    if not valid_sha256(endpoint_sha256):
        raise AssertionError("clearance-floor endpoint SHA is malformed")
    if sha256(endpoint_file) != endpoint_sha256:
        raise AssertionError("clearance-floor endpoint SHA mismatch")
    if sha256(source_file) != endpoint_sha256:
        raise AssertionError(
            "guarded chain source is not the certified clearance-floor endpoint"
        )

    checkpoint_clearance = certificate.get("circuit_clearance_at_checkpoints")
    if not isinstance(checkpoint_clearance, dict):
        raise AssertionError("clearance-floor certificate has no checkpoint clearance")
    endpoint_clearance = checkpoint_clearance.get("endpoint")
    if not isinstance(endpoint_clearance, dict):
        raise AssertionError("clearance-floor certificate has no endpoint clearance")
    if endpoint_clearance.get("strictly_positive") is not True:
        raise AssertionError("clearance-floor source is not strictly positive")

    labels = tuple(str(label) for label in circuit[:2])
    determinant = exact_fraction(
        endpoint_clearance.get("determinant"),
        "endpoint_clearance.determinant",
    )
    radius_squared = exact_fraction(
        endpoint_clearance.get("rms_radius_squared"),
        "endpoint_clearance.rms_radius_squared",
    )
    opposite_area_squared = exact_fraction_map(
        endpoint_clearance.get("opposite_area_squared"),
        "endpoint_clearance.opposite_area_squared",
        labels,
    )
    tau_squared = exact_fraction_map(
        endpoint_clearance.get("normalized_opposite_slack_squared"),
        "endpoint_clearance.normalized_opposite_slack_squared",
        labels,
    )
    if not determinant or radius_squared <= 0 or any(
        value <= 0 for value in opposite_area_squared.values()
    ):
        raise AssertionError("nonpositive clearance-floor source denominator")
    for label in labels:
        reconstructed = (
            determinant * determinant
            / (radius_squared * opposite_area_squared[label])
        )
        if tau_squared[label] != reconstructed:
            raise AssertionError((label, "clearance-floor exact identity mismatch"))

    kappa_squared = exact_fraction(
        endpoint_clearance.get("minimum_normalized_opposite_slack_squared"),
        "endpoint_clearance.minimum_normalized_opposite_slack_squared",
    )
    if kappa_squared <= 0 or kappa_squared != min(tau_squared.values()):
        raise AssertionError("clearance-floor minimum is not the exact endpoint minimum")
    floor_vertices = [
        label for label in labels if tau_squared[label] == kappa_squared
    ]
    if not floor_vertices:
        raise AssertionError("clearance-floor source has no attaining vertex")

    source_faces = validated_certificate_faces(
        certificate,
        "clearance-floor bypass source",
    )
    source_geometry = exact_checkpoint_clearance(
        endpoint_file,
        source_faces["faces"],
        circuit,
    )
    if (
        source_geometry["determinant"] != determinant
        or source_geometry["radius_squared"] != radius_squared
        or source_geometry["opposite_cross_squared"] != opposite_area_squared
        or source_geometry["clearance_squared"] != tau_squared
    ):
        raise AssertionError("clearance-floor bypass endpoint geometry mismatch")

    return {
        "kappa_squared": kappa_squared,
        "source_clearance_squared": tau_squared,
        "source_floor_vertices": floor_vertices,
        "source_faces": source_faces,
        "source_geometry": source_geometry,
        "record": {
            "mode": GUARDED_FLOOR_MODE,
            "enabled": True,
            "definition": (
                "clearance_v^2 = n*s^2*D^2/(N_R*C_opposite,v^2), s=4*d6, "
                "and tau_v = clearance_v^2/kappa^2; the guarded floor is "
                "tau_v >= 1 for both non-rail circuit vertices"
            ),
            "source_certificate": display_path(certificate_file),
            "source_certificate_sha256": sha256(certificate_file),
            "source_verdict": BYPASS_VERDICT,
            "circuit": list(circuit),
            "source_endpoint_file": endpoint_value,
            "source_endpoint_sha256": endpoint_sha256,
            "chain_source_sha256": sha256(source_file),
            "kappa_squared_exact": source.ex.qs(kappa_squared),
            "source_clearance_squared_exact": {
                label: source.ex.qs(tau_squared[label]) for label in labels
            },
            "source_floor_vertices": floor_vertices,
        },
    }


def validated_parent_chain_clearance_floor_certificate(
    certificate_file: Path,
    certificate,
    circuit,
    source_file: Path,
):
    if certificate.get("verdict") != CHAIN_VERDICT:
        raise AssertionError("parent chain clearance verdict mismatch")
    if certificate.get("version") != 2:
        raise AssertionError("parent chain clearance certificate is not version 2")
    if tuple(certificate.get("circuit", ())) != tuple(circuit):
        raise AssertionError("parent chain clearance circuit mismatch")
    guard = certificate.get("clearance_floor_guard")
    if not isinstance(guard, dict):
        raise AssertionError("parent chain has no clearance-floor guard")
    if guard.get("mode") == HISTORICAL_FLOOR_MODE:
        raise AssertionError("historical parent chain cannot supply a clearance floor")
    if guard.get("mode") != GUARDED_FLOOR_MODE or guard.get("enabled") is not True:
        raise AssertionError("parent chain clearance-floor mode is malformed")
    if guard.get("all_segments_floor_safe") is not True:
        raise AssertionError("parent chain does not certify all floor segments safe")
    if tuple(guard.get("circuit", ())) != tuple(circuit):
        raise AssertionError("parent chain guard circuit mismatch")

    original_certificate_value = guard.get("source_certificate")
    original_endpoint_value = guard.get("source_endpoint_file")
    if (
        not isinstance(original_certificate_value, str)
        or not original_certificate_value
        or not isinstance(original_endpoint_value, str)
        or not original_endpoint_value
    ):
        raise AssertionError("parent chain has no original bypass lineage")
    original_certificate_file = resolve_root_path(original_certificate_value)
    original_endpoint_file = resolve_root_path(original_endpoint_value)
    original_certificate = json.loads(original_certificate_file.read_text())
    if (
        original_certificate.get("version") != 1
        or original_certificate.get("verdict") != BYPASS_VERDICT
    ):
        raise AssertionError("parent original source is not a version-1 bypass")
    original_source = validated_clearance_floor_certificate(
        str(original_certificate_file),
        circuit,
        original_endpoint_file,
    )
    for key, expected in original_source["record"].items():
        if key == "chain_source_sha256":
            continue
        if guard.get(key) != expected:
            raise AssertionError((key, "parent original bypass lineage mismatch"))

    segment_count = certificate.get("segment_count")
    if (
        isinstance(segment_count, bool)
        or not isinstance(segment_count, int)
        or segment_count <= 0
    ):
        raise AssertionError("parent chain segment count is malformed")
    if certificate.get("accepted_checkpoint_count") != segment_count:
        raise AssertionError("parent accepted-checkpoint count mismatch")
    material_segments = certificate.get("segments")
    floor_segments = guard.get("segments")
    if (
        not isinstance(material_segments, list)
        or len(material_segments) != segment_count
        or not isinstance(floor_segments, list)
        or len(floor_segments) != segment_count
        or guard.get("certified_segment_count") != segment_count
    ):
        raise AssertionError("parent chain material/floor segment count mismatch")

    exact_checkpoint_values = certificate.get("exact_checkpoint_files")
    if not isinstance(exact_checkpoint_values, list) or any(
        not isinstance(value, str) or not value
        for value in exact_checkpoint_values
    ):
        raise AssertionError("parent exact checkpoint chain is malformed")
    if (
        len(exact_checkpoint_values) != segment_count + 1
        or len(set(exact_checkpoint_values)) != len(exact_checkpoint_values)
    ):
        raise AssertionError("parent exact checkpoint chain is malformed")
    generated_sha256 = certificate.get("generated_sha256")
    if not isinstance(generated_sha256, dict):
        raise AssertionError("parent chain has no generated hashes")
    checkpoint_sha256 = []
    for value in exact_checkpoint_values:
        checkpoint_file = resolve_root_path(value)
        if not checkpoint_file.is_file():
            raise FileNotFoundError(checkpoint_file)
        expected_sha256 = generated_sha256.get(value)
        if not valid_sha256(expected_sha256):
            raise AssertionError((value, "parent checkpoint SHA is malformed"))
        if sha256(checkpoint_file) != expected_sha256:
            raise AssertionError((value, "parent checkpoint SHA mismatch"))
        checkpoint_sha256.append(expected_sha256)

    parent_source_value = certificate.get("source")
    if not isinstance(parent_source_value, str) or not parent_source_value:
        raise AssertionError("parent chain has no declared source")
    parent_source_file = resolve_root_path(parent_source_value)
    parent_source_sha256 = sha256(parent_source_file)
    if (
        not valid_sha256(guard.get("chain_source_sha256"))
        or guard.get("chain_source_sha256") != parent_source_sha256
        or checkpoint_sha256[0] != parent_source_sha256
    ):
        raise AssertionError("parent chain source junction is malformed")

    kappa_squared = original_source["kappa_squared"]
    labels = tuple(str(label) for label in circuit[:2])
    previous_right = None
    for index, (material_segment, floor_segment) in enumerate(
        zip(material_segments, floor_segments)
    ):
        expected_left = f"checkpoint_{index:03d}"
        expected_right = f"checkpoint_{index + 1:03d}"
        if (
            not isinstance(material_segment, dict)
            or material_segment.get("left") != expected_left
            or material_segment.get("right") != expected_right
            or not isinstance(floor_segment, dict)
            or floor_segment.get("left") != expected_left
            or floor_segment.get("right") != expected_right
            or (previous_right is not None and expected_left != previous_right)
        ):
            raise AssertionError((index, "parent segment junction is malformed"))
        if exact_fraction(
            floor_segment.get("kappa_squared_exact"),
            f"parent.floor_segments[{index}].kappa_squared_exact",
        ) != kappa_squared:
            raise AssertionError((index, "parent segment resets the exact floor"))
        exact_endpoint_tau_ratios(
            floor_segment.get("endpoint_tau_ratios"),
            labels,
            kappa_squared,
            f"parent.floor_segments[{index}].endpoint_tau_ratios",
        )
        previous_right = expected_right

    parent_endpoint_tau_ratios = guard.get("chain_endpoint_tau_ratios")
    if parent_endpoint_tau_ratios != floor_segments[-1].get(
        "endpoint_tau_ratios"
    ):
        raise AssertionError("parent chain endpoint tau does not match final segment")
    parent_endpoint_clearance = exact_endpoint_tau_ratios(
        parent_endpoint_tau_ratios,
        labels,
        kappa_squared,
        "parent.chain_endpoint_tau_ratios",
    )

    parent_faces = validated_certificate_faces(certificate, "parent chain")
    parent_endpoint_value = exact_checkpoint_values[-1]
    parent_endpoint_file = resolve_root_path(parent_endpoint_value)
    parent_endpoint_sha256 = checkpoint_sha256[-1]
    if sha256(source_file) != parent_endpoint_sha256:
        raise AssertionError(
            "new guarded chain source is not the parent final checkpoint"
        )
    parent_endpoint_geometry = exact_checkpoint_clearance(
        parent_endpoint_file,
        parent_faces["faces"],
        circuit,
    )
    if (
        parent_endpoint_geometry["site_count"]
        != original_source["source_geometry"]["site_count"]
        or parent_endpoint_geometry["clearance_squared"]
        != parent_endpoint_clearance
    ):
        raise AssertionError("parent endpoint exact clearance geometry mismatch")

    parent_certificate_sha256 = sha256(certificate_file)
    record = dict(original_source["record"])
    record["chain_source_sha256"] = parent_endpoint_sha256
    record.update({
        "floor_source_kind": "inherited_version_2_guarded_chain",
        "parent_chain_certificate": display_path(certificate_file),
        "parent_chain_certificate_sha256": parent_certificate_sha256,
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
        "original_source_face_file": original_source["source_faces"]["value"],
        "original_source_face_file_sha256": original_source["source_faces"][
            "file_sha256"
        ],
        "original_source_face_hash": original_source["source_faces"][
            "face_hash"
        ],
        "original_source_site_count": original_source["source_geometry"][
            "site_count"
        ],
    })
    return {
        "kappa_squared": kappa_squared,
        "source_clearance_squared": parent_endpoint_clearance,
        "source_floor_vertices": [],
        "source_faces": original_source["source_faces"],
        "source_geometry": original_source["source_geometry"],
        "parent_endpoint_geometry": parent_endpoint_geometry,
        "record": record,
    }


def positive_interval_receipt(poly, name: str):
    endpoint_values = [poly.eval(Q(0)), poly.eval(Q(1))]
    if any(value <= 0 for value in endpoint_values):
        raise AssertionError((name, "nonpositive interval endpoint"))
    try:
        sign, leaves, worst = source.ex.bernstein_sign(
            poly, Q(0), Q(1), max_depth=60
        )
    except AssertionError as error:
        raise AssertionError((name, "strict positivity not Bernstein-certified")) from error
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
        raise AssertionError((name, "clearance-floor polynomial is identically zero"))
    if not multiplicity:
        raise AssertionError((name, "requested source factor without source zero"))
    return multiplicity, source.P(poly.c[multiplicity:])


def clearance_floor_segment_record(path, faces, circuit, kappa_squared):
    if kappa_squared <= 0:
        raise AssertionError("nonpositive exact clearance floor")
    labels = tuple(str(label) for label in circuit[:2])
    if any(label not in path for label in circuit):
        raise AssertionError("clearance circuit label absent from exact path")

    d6, centroid_numerator = source.ex.exact_centroid_numerators(path, faces)
    scale = 4 * d6
    site_count = len(path)
    if site_count <= 0:
        raise AssertionError("clearance path has no stored sites")
    radius_numerator = sum(
        (
            source.ex.norm2(tuple(
                scale * path[label][axis] - centroid_numerator[axis]
                for axis in range(3)
            ))
            for label in path
        ),
        source.P.zero(),
    )
    a, b, c, d = circuit
    determinant = source.determinant_polynomial(path, circuit)
    opposite_cross_squared = {
        str(a): source.ex.norm2(source.ex.cross(
            source.ex.sub(path[c], path[b]),
            source.ex.sub(path[d], path[b]),
        )),
        str(b): source.ex.norm2(source.ex.cross(
            source.ex.sub(path[c], path[a]),
            source.ex.sub(path[d], path[a]),
        )),
    }
    numerator = site_count * scale * scale * determinant * determinant

    scale_receipt = positive_interval_receipt(scale, "clearance scale s=4*d6")
    radius_receipt = positive_interval_receipt(
        radius_numerator,
        "clearance radius numerator N_R",
    )
    shared = {
        "site_count": site_count,
        "scale_polynomial_digest": canonical_hash(scale.exact()),
        "scale_interval_receipt": scale_receipt,
        "determinant_polynomial_digest": canonical_hash(determinant.exact()),
        "tau_numerator_polynomial_digest": canonical_hash(numerator.exact()),
        "radius_numerator_polynomial_digest": canonical_hash(
            radius_numerator.exact()
        ),
        "radius_numerator_interval_receipt": radius_receipt,
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
        floor_polynomial = numerator - kappa_squared * denominator
        source_value = floor_polynomial.eval(Q(0))
        if source_value < 0:
            raise AssertionError((label, "clearance floor already recrossed at source"))
        if source_value == 0:
            multiplicity, positive_polynomial = factor_exact_source_zero(
                floor_polynomial,
                f"clearance floor at vertex {label}",
            )
            proof_kind = "positive_quotient_after_exact_source_factor"
        else:
            multiplicity = 0
            positive_polynomial = floor_polynomial
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
        source_clearance = numerator.eval(Q(0)) / source_denominator
        endpoint_clearance = numerator.eval(Q(1)) / endpoint_denominator
        endpoint_tau_ratio = endpoint_clearance / kappa_squared
        if endpoint_tau_ratio <= 1:
            raise AssertionError((label, "clearance floor not strict at endpoint"))

        source_clearance_squared[label] = source_clearance
        endpoint_clearance_squared[label] = endpoint_clearance
        endpoint_tau_ratios[label] = {
            "clearance_squared_exact": source.ex.qs(endpoint_clearance),
            "tau_ratio_exact": source.ex.qs(endpoint_tau_ratio),
            "tau_ratio_decimal": float(endpoint_tau_ratio),
            "clearance_over_kappa_decimal": math.sqrt(float(endpoint_tau_ratio)),
        }
        vertices[label] = {
            "source_equality": source_value == 0,
            "source_zero_multiplicity": multiplicity,
            "source_floor_polynomial_value_exact": source.ex.qs(source_value),
            "floor_polynomial_degree": floor_polynomial.degree,
            "floor_polynomial_digest": canonical_hash(floor_polynomial.exact()),
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
            "denominator_polynomial_digest": canonical_hash(denominator.exact()),
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


def accepted_raw_files(report):
    files = []
    for record in report["history"]:
        if record.get("accepted"):
            files.append(HERE / record["endpoint_file"])
    if not files:
        raise AssertionError("SLP report has no accepted checkpoints")
    if len(files) != sum(bool(row.get("accepted")) for row in report["history"]):
        raise AssertionError("accepted checkpoint accounting mismatch")
    for path in files:
        if not path.is_file():
            raise FileNotFoundError(path)
    return files


def repair_snapshots(raw_snapshots):
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
        points = dict(rows)
        corrections = {}
        for label in source.BASE:
            coefficient = source.ex.dot(
                normal, source.ex.sub(points[label], anchor)
            ) / normal_norm2
            points[label] = source.ex.sub(
                points[label], source.ex.mul(normal, coefficient)
            )
            corrections[label] = coefficient
            if source.ex.dot(normal, source.ex.sub(points[label], anchor)):
                raise AssertionError(("base projection failed", label))
        nonzero = [value for value in corrections.values() if value]
        base = {
            "nonzero_count": len(nonzero),
            "maximum_log10_abs": (
                max(source.ex.qlog10(value) for value in nonzero)
                if nonzero else None
            ),
            "exact_digest": canonical_hash({
                str(label): source.ex.qs(value)
                for label, value in sorted(corrections.items())
            }),
        }
        points, uv, quad = source.repair_quad(points)
        repaired.append(points)
        audit.append({
            "base": base,
            "quad": quad,
            "quad_barycentric": [source.ex.qs(uv[0]), source.ex.qs(uv[1])],
        })
    return repaired, audit


def segment_record(
    left_name,
    right_name,
    left,
    right,
    circuit,
    expected_faces=None,
    clearance_floor=None,
):
    path = bypass.make_path(left, right)
    representative = source.evaluate_path(path, Q(1, 2))
    candidate_faces, _ = source.fresh_faces(representative)
    if expected_faces is not None:
        expected_sets = {frozenset(face) for face in expected_faces}
        candidate_sets = {frozenset(face) for face in candidate_faces}
        if candidate_sets != expected_sets:
            raise AssertionError((left_name, right_name, "face lattice changed"))
        # Boundary-cycle rotations are representational, not support events.
        # Use one canonical oriented face list for the entire fixed-cell proof.
        faces = expected_faces
    else:
        faces = candidate_faces
    support, mechanics = source.assert_cell(representative, faces)
    cover = source.exact_class_cover(path, faces, Q(0), Q(1))
    determinant = source.determinant_polynomial(path, circuit)
    midpoint_value = determinant.eval(Q(1, 2))
    sign = 1 if midpoint_value > 0 else -1 if midpoint_value < 0 else 0
    if not sign:
        raise AssertionError((left_name, right_name, "circuit vanishes"))
    sign_record = source.exact_sign_record(
        determinant, Q(0), Q(1), sign
    )
    comparison = bypass.comparison_packet(
        bypass.selected_residuals(left, faces),
        bypass.selected_residuals(right, faces),
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
    floor_result = None
    if clearance_floor is not None:
        floor_result = clearance_floor_segment_record(
            path,
            faces,
            circuit,
            clearance_floor,
        )
    return faces, record, floor_result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--slp-prefix", required=True)
    parser.add_argument("--output-prefix", required=True)
    parser.add_argument(
        "--source",
        help="optional exact source checkpoint replacing the numerical report source",
    )
    parser.add_argument("--circuit", type=bypass.parse_circuit, required=True)
    parser.add_argument(
        "--clearance-floor-certificate",
        help=(
            "optional version-1 exact mandatory-rail bypass certificate, or a "
            "version-2 guarded post-bypass chain certificate inheriting that "
            "same floor; omit only for the explicit historical no-floor mode"
        ),
    )
    args = parser.parse_args()

    report_file = HERE / f"{args.slp_prefix}_slp.json"
    report = json.loads(report_file.read_text())
    circuit = tuple(args.circuit)
    source_file = Path(args.source) if args.source else Path(report["source"])
    if not source_file.is_absolute():
        source_file = HERE / source_file
    if not source_file.is_file():
        raise FileNotFoundError(source_file)
    floor_source = (
        validated_clearance_floor_certificate(
            args.clearance_floor_certificate,
            circuit,
            source_file,
        )
        if args.clearance_floor_certificate is not None
        else None
    )
    raw_files = [source_file, *accepted_raw_files(report)]
    raw_snapshots = [source.ex.read_rows(path) for path in raw_files]
    snapshots, repair = repair_snapshots(raw_snapshots)

    exact_files = [
        HERE / f"{args.output_prefix}_checkpoint_{index:03d}.csv"
        for index in range(len(snapshots))
    ]
    for path, points in zip(exact_files, snapshots):
        source.write_exact_csv(path, points)

    faces = None
    segments = []
    floor_segments = []
    previous_floor_endpoint = None
    chain_endpoint_tau_ratios = None
    for index, (left, right) in enumerate(zip(snapshots, snapshots[1:])):
        left_name = f"checkpoint_{index:03d}"
        right_name = f"checkpoint_{index + 1:03d}"
        candidate_faces, record, floor_result = segment_record(
            left_name,
            right_name,
            left,
            right,
            circuit,
            faces,
            floor_source["kappa_squared"] if floor_source is not None else None,
        )
        if faces is None:
            faces = candidate_faces
        if floor_source is not None:
            if floor_result is None:
                raise AssertionError("guarded segment omitted its clearance proof")
            if index == 0:
                if (
                    floor_result["source_clearance_squared"]
                    != floor_source["source_clearance_squared"]
                ):
                    raise AssertionError(
                        "chain source clearance differs from certified exact floor source"
                    )
                source_equalities = sorted(
                    label
                    for label, vertex in floor_result["record"]["vertices"].items()
                    if vertex["source_equality"]
                )
                if source_equalities != sorted(
                    floor_source["source_floor_vertices"]
                ):
                    raise AssertionError(
                        "chain source does not attain the certified exact floor"
                    )
            elif (
                floor_result["source_clearance_squared"]
                != previous_floor_endpoint
            ):
                raise AssertionError("clearance-floor segment junction mismatch")
            previous_floor_endpoint = floor_result["endpoint_clearance_squared"]
            chain_endpoint_tau_ratios = floor_result["endpoint_tau_ratios"]
            floor_segments.append({
                "left": left_name,
                "right": right_name,
                **floor_result["record"],
            })
        segments.append(record)
    if faces is None:
        raise AssertionError("empty exact chain")

    faces_file = HERE / f"{args.output_prefix}_faces.json"
    faces_file.write_text(json.dumps(faces, indent=2) + "\n")
    final_comparison = bypass.comparison_packet(
        bypass.selected_residuals(snapshots[0], faces),
        bypass.selected_residuals(snapshots[-1], faces),
    )
    generated = [*exact_files, faces_file]
    certificate_file = HERE / f"{args.output_prefix}_certificate.json"
    if floor_source is None:
        clearance_floor_guard = {
            "mode": HISTORICAL_FLOOR_MODE,
            "enabled": False,
            "source_certificate": None,
            "statement": (
                "The optional --clearance-floor-certificate was not supplied; "
                "this certificate intentionally preserves the historical chain "
                "contract and makes no circuit-clearance-floor claim."
            ),
        }
        conclusion_suffix = (
            " This is the explicit historical no-clearance-floor mode."
        )
    else:
        if chain_endpoint_tau_ratios is None:
            raise AssertionError("guarded chain has no endpoint clearance ratios")
        if len(floor_segments) != len(segments):
            raise AssertionError("guarded chain clearance segment count mismatch")
        clearance_floor_guard = dict(floor_source["record"])
        clearance_floor_guard.update({
            "certified_segment_count": len(segments),
            "all_segments_floor_safe": True,
            "segments": floor_segments,
            "chain_endpoint_tau_ratios": chain_endpoint_tau_ratios,
        })
        conclusion_suffix = (
            " Both normalized opposite-circuit clearances stay above the exact "
            "certified source floor, with only the permitted initial source "
            "equalities."
        )
    payload = {
        "version": 2,
        "scope": (
            "piecewise exact post-bypass intrinsic material chain with an exact "
            "circuit-clearance floor"
            if floor_source is not None
            else "piecewise exact post-bypass intrinsic material chain"
        ),
        "verdict": "EXACT_POST_BYPASS_MATERIAL_CHAIN_PASS",
        "circuit": list(circuit),
        "clearance_floor_guard": clearance_floor_guard,
        "slp_report": str(report_file.relative_to(ROOT)),
        "slp_report_sha256": sha256(report_file),
        "source": str(source_file.relative_to(ROOT)),
        "accepted_checkpoint_count": len(raw_files) - 1,
        "first_numerical_event": report.get("first_event"),
        "repair": repair,
        "exact_checkpoint_files": [
            str(path.relative_to(ROOT)) for path in exact_files
        ],
        "face_file": str(faces_file.relative_to(ROOT)),
        "face_hash": canonical_hash(faces),
        "segments": segments,
        "segment_count": len(segments),
        "overall_material_comparison": final_comparison,
        "generated_sha256": {
            str(path.relative_to(ROOT)): sha256(path) for path in generated
        },
        "conclusion": (
            "Every accepted numerical SLP step has been replaced by a connected "
            "exact rational-polynomial segment.  Every complete support and "
            "own-centroid primitive keeps its certified sign, all 37 rails "
            "survive, the mandatory circuit stays on the protected side, and "
            "all four selected residuals decrease on every segment."
            + conclusion_suffix
        ),
    }
    certificate_file.write_text(json.dumps(payload, indent=2) + "\n")
    summary = {
        "verdict": payload["verdict"],
        "segments": len(segments),
        "clearance_floor_mode": clearance_floor_guard["mode"],
        "class_cover_subintervals": sum(
            row["class_cover_subinterval_count"] for row in segments
        ),
        "overall_endpoint_ratios": {
            name: row["decimal_ratio"]
            for name, row in final_comparison.items()
        },
        "certificate": str(certificate_file),
    }
    if chain_endpoint_tau_ratios is not None:
        summary["clearance_floor_endpoint_tau_ratios"] = {
            label: row["tau_ratio_decimal"]
            for label, row in chain_endpoint_tau_ratios.items()
        }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
