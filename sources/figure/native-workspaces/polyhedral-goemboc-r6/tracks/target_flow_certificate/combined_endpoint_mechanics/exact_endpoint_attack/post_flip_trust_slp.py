#!/usr/bin/env python3
"""Fail-closed one-step cycle-11 proposal from a certified exact endpoint.

The LP maximizes common fractional descent under physical trust, complete
actual-cell guards, the exact certificate's normalized circuit-clearance
floor, and any explicitly requested topology-circuit inward guards.  A
proposed endpoint is accepted only after fresh nonlinear mechanics,
cell/signature, rail, residual, strict-clearance, and actual topology-guard
checks all pass.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(PARENT))

import build_u54_material_exact_path as exact_path  # noqa: E402
import combined_four_death_lp as four  # noqa: E402
from integrate_four_death_direction import write_csv  # noqa: E402
from predictor_bypass_epoch import candidate_circuits  # noqa: E402


SOURCE = HERE / "first_extrapolated_event_far.csv"
EXPECTED_CLEARANCE_VERDICT = "EXACT_MANDATORY_RAIL_NULLSPACE_BYPASS_PASS"
EXPECTED_CHAIN_VERDICT = "EXACT_POST_BYPASS_MATERIAL_CHAIN_PASS"
GUARDED_FLOOR_MODE = "guarded_by_exact_clearance_floor"
INHERITED_FLOOR_SOURCE_KIND = "inherited_version_2_guarded_chain"
GUARDED_FLOOR_DEFINITION = (
    "clearance_v^2 = n*s^2*D^2/(N_R*C_opposite,v^2), s=4*d6, "
    "and tau_v = clearance_v^2/kappa^2; the guarded floor is "
    "tau_v >= 1 for both non-rail circuit vertices"
)
ROOT_GUARD_LINEAGE_FIELDS = (
    "mode",
    "enabled",
    "definition",
    "source_certificate",
    "source_certificate_sha256",
    "source_verdict",
    "circuit",
    "source_endpoint_file",
    "source_endpoint_sha256",
    "kappa_squared_exact",
    "source_clearance_squared_exact",
    "source_floor_vertices",
)


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


def valid_sha256(value) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    )


def resolve_root_path(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def validated_file_binding(value, expected_sha, field: str) -> Path:
    if not isinstance(value, str) or not value:
        raise ValueError((field, "path is malformed"))
    if not valid_sha256(expected_sha):
        raise ValueError((field, "SHA-256 is malformed"))
    path = resolve_root_path(value)
    if not path.is_file():
        raise ValueError((field, "bound file is absent", value))
    actual_sha = sha256(path)
    if actual_sha != expected_sha:
        raise ValueError((field, "SHA-256 mismatch", actual_sha, expected_sha))
    return path


def validated_face_binding(certificate, field: str):
    face_value = certificate.get("face_file")
    generated_sha256 = certificate.get("generated_sha256")
    if not isinstance(generated_sha256, dict):
        raise ValueError((field, "certificate has no generated hashes"))
    face_path = validated_file_binding(
        face_value,
        generated_sha256.get(face_value),
        f"{field}.face_file",
    )
    faces = json.loads(face_path.read_text())
    face_hash = certificate.get("face_hash")
    if not valid_sha256(face_hash) or canonical_hash(faces) != face_hash:
        raise ValueError((field, "face-ledger canonical hash mismatch"))
    return {
        "value": face_value,
        "file_sha256": generated_sha256[face_value],
        "face_hash": face_hash,
    }


def exact_fraction(value, field: str) -> Q:
    if not isinstance(value, str):
        raise ValueError((field, "exact rational is not a string"))
    try:
        parsed = Q(value)
    except (ValueError, ZeroDivisionError) as error:
        raise ValueError((field, "invalid exact rational")) from error
    if str(parsed) != value:
        raise ValueError((field, "noncanonical exact rational"))
    return parsed


def exact_fraction_map(packet, field: str, labels) -> dict[str, Q]:
    if not isinstance(packet, dict) or set(packet) != set(labels):
        raise ValueError((field, "wrong vertex labels"))
    return {
        label: exact_fraction(packet[label], f"{field}.{label}")
        for label in labels
    }


def endpoint_tau_ratios(packet, field: str, labels, exact_floor):
    if not isinstance(packet, dict) or set(packet) != set(labels):
        raise ValueError((field, "wrong vertex labels"))
    result = {}
    expected_keys = {
        "clearance_squared_exact",
        "tau_ratio_exact",
        "tau_ratio_decimal",
        "clearance_over_kappa_decimal",
    }
    for label in labels:
        vertex = packet[label]
        if not isinstance(vertex, dict) or set(vertex) != expected_keys:
            raise ValueError((f"{field}.{label}", "malformed endpoint tau packet"))
        clearance = exact_fraction(
            vertex.get("clearance_squared_exact"),
            f"{field}.{label}.clearance_squared_exact",
        )
        tau = exact_fraction(
            vertex.get("tau_ratio_exact"),
            f"{field}.{label}.tau_ratio_exact",
        )
        if clearance <= exact_floor or tau <= 1:
            raise ValueError((label, "chain endpoint clearance is not strict"))
        reconstructed_tau = clearance / exact_floor
        if tau != reconstructed_tau:
            raise ValueError((
                label,
                "chain endpoint tau/clearance identity mismatch",
                str(tau),
                str(reconstructed_tau),
            ))
        tau_decimal = vertex["tau_ratio_decimal"]
        clearance_decimal = vertex["clearance_over_kappa_decimal"]
        if (
            isinstance(tau_decimal, bool)
            or not isinstance(tau_decimal, (int, float))
            or not math.isfinite(tau_decimal)
            or tau_decimal != float(tau)
            or isinstance(clearance_decimal, bool)
            or not isinstance(clearance_decimal, (int, float))
            or not math.isfinite(clearance_decimal)
            or clearance_decimal != math.sqrt(float(tau))
        ):
            raise ValueError((f"{field}.{label}", "endpoint tau decimal mismatch"))
        result[label] = (clearance, tau)
    return result


def load_inherited_guarded_chain_source(
    guard,
    circuit,
    exact_floor,
    visited,
):
    parent_value = guard.get("parent_chain_certificate")
    parent_path = validated_file_binding(
        parent_value,
        guard.get("parent_chain_certificate_sha256"),
        "inherited.parent_chain_certificate",
    )
    parent = json.loads(parent_path.read_text())
    if not isinstance(parent, dict):
        raise ValueError("inherited parent chain certificate is not an object")

    parent_checkpoints = parent.get("exact_checkpoint_files")
    if (
        not isinstance(parent_checkpoints, list)
        or len(parent_checkpoints) < 2
        or any(
            not isinstance(value, str) or not value
            for value in parent_checkpoints
        )
    ):
        raise ValueError("inherited parent checkpoint chain is malformed")
    parent_endpoint = parent_checkpoints[-1]
    if guard.get("parent_chain_endpoint_file") != parent_endpoint:
        raise ValueError("inherited parent endpoint path mismatch")

    parent_floor, parent_contract = load_guarded_chain_clearance_floor(
        parent,
        parent_path,
        resolve_root_path(parent_endpoint),
        circuit,
        _visited=visited,
    )
    if parent_floor != exact_floor:
        raise ValueError("inherited parent resets the exact clearance floor")
    parent_guard = parent.get("clearance_floor_guard")
    if not isinstance(parent_guard, dict):
        raise ValueError("inherited parent has no clearance-floor guard")
    for key in ROOT_GUARD_LINEAGE_FIELDS:
        if guard.get(key) != parent_guard.get(key):
            raise ValueError((key, "inherited original bypass lineage mismatch"))

    parent_source = parent.get("source")
    if guard.get("parent_chain_source_file") != parent_source:
        raise ValueError("inherited parent source path mismatch")
    parent_source_path = validated_file_binding(
        parent_source,
        guard.get("parent_chain_source_sha256"),
        "inherited.parent_chain_source_file",
    )
    if (
        parent_contract.get("chain_source") != parent_source
        or parent_contract.get("chain_source_sha256") != sha256(parent_source_path)
    ):
        raise ValueError("inherited parent source contract mismatch")

    parent_endpoint_sha = parent_contract.get("generated_endpoint_sha256")
    if (
        parent_contract.get("generated_endpoint") != parent_endpoint
        or guard.get("parent_chain_endpoint_sha256") != parent_endpoint_sha
    ):
        raise ValueError("inherited parent generated endpoint binding mismatch")

    parent_segment_count = parent.get("segment_count")
    declared_parent_segment_count = guard.get("parent_chain_segment_count")
    if (
        isinstance(parent_segment_count, bool)
        or not isinstance(parent_segment_count, int)
        or parent_segment_count <= 0
        or isinstance(declared_parent_segment_count, bool)
        or not isinstance(declared_parent_segment_count, int)
        or declared_parent_segment_count != parent_segment_count
    ):
        raise ValueError("inherited parent segment count mismatch")
    if (
        guard.get("parent_chain_all_segments_floor_safe") is not True
        or parent_guard.get("all_segments_floor_safe") is not True
    ):
        raise ValueError("inherited parent floor-safe verdict mismatch")

    labels = tuple(str(label) for label in circuit[:2])
    declared_parent_clearance = exact_fraction_map(
        guard.get("parent_chain_endpoint_clearance_squared_exact"),
        "guard.parent_chain_endpoint_clearance_squared_exact",
        labels,
    )
    expected_parent_clearance = exact_fraction_map(
        parent_contract.get("chain_endpoint_clearance_squared_exact"),
        "parent_contract.chain_endpoint_clearance_squared_exact",
        labels,
    )
    if declared_parent_clearance != expected_parent_clearance:
        raise ValueError("inherited parent endpoint clearance mismatch")
    if guard.get("parent_chain_endpoint_tau_ratios") != parent_guard.get(
        "chain_endpoint_tau_ratios"
    ):
        raise ValueError("inherited parent endpoint tau lineage mismatch")

    original_face_fields = {
        "original_source_face_file": "source_floor_face_file",
        "original_source_face_file_sha256": "source_floor_face_file_sha256",
        "original_source_face_hash": "source_floor_face_hash",
        "original_source_site_count": "source_floor_site_count",
    }
    for guard_key, contract_key in original_face_fields.items():
        if guard.get(guard_key) != parent_contract.get(contract_key):
            raise ValueError((guard_key, "inherited original trust root mismatch"))

    return parent_endpoint, parent_endpoint_sha, {
        "floor_source_kind": INHERITED_FLOOR_SOURCE_KIND,
        "parent_chain_certificate": parent_value,
        "parent_chain_certificate_sha256": sha256(parent_path),
        "parent_chain_source": parent_source,
        "parent_chain_source_sha256": sha256(parent_source_path),
        "parent_chain_endpoint": parent_endpoint,
        "parent_chain_endpoint_sha256": parent_endpoint_sha,
        "parent_chain_segment_count": parent_segment_count,
    }


def load_guarded_chain_clearance_floor(
    certificate,
    path: Path,
    source_path: Path,
    circuit,
    _visited=None,
):
    certificate_identity = path.resolve()
    visited = frozenset() if _visited is None else frozenset(_visited)
    if certificate_identity in visited:
        raise ValueError("cyclic inherited clearance-floor lineage")
    visited |= {certificate_identity}

    if type(certificate.get("version")) is not int or certificate["version"] != 2:
        raise ValueError("post-bypass chain certificate is not version 2")
    if certificate.get("verdict") != EXPECTED_CHAIN_VERDICT:
        raise ValueError("post-bypass chain certificate verdict mismatch")
    certificate_circuit = tuple(certificate.get("circuit", ()))
    if certificate_circuit != tuple(circuit):
        raise ValueError((
            "clearance-floor certificate circuit mismatch",
            certificate_circuit,
            tuple(circuit),
        ))

    guard = certificate.get("clearance_floor_guard")
    if not isinstance(guard, dict):
        raise ValueError("version-2 chain has no clearance-floor schema")
    if guard.get("mode") != GUARDED_FLOOR_MODE:
        raise ValueError((
            "post-bypass chain is not in guarded clearance-floor mode",
            guard.get("mode"),
        ))
    if guard.get("enabled") is not True:
        raise ValueError("guarded clearance floor is not enabled")
    if guard.get("definition") != GUARDED_FLOOR_DEFINITION:
        raise ValueError("guarded clearance-floor definition mismatch")
    if tuple(guard.get("circuit", ())) != tuple(circuit):
        raise ValueError("clearance-floor guard circuit mismatch")
    if guard.get("source_verdict") != EXPECTED_CLEARANCE_VERDICT:
        raise ValueError("clearance-floor source verdict mismatch")
    if guard.get("all_segments_floor_safe") is not True:
        raise ValueError("chain does not assert all segments floor-safe")

    checkpoint_files = certificate.get("exact_checkpoint_files")
    if (
        not isinstance(checkpoint_files, list)
        or len(checkpoint_files) < 2
        or any(not isinstance(value, str) or not value for value in checkpoint_files)
        or len(set(checkpoint_files)) != len(checkpoint_files)
    ):
        raise ValueError("invalid exact checkpoint file schema")
    segment_count = certificate.get("segment_count")
    accepted_count = certificate.get("accepted_checkpoint_count")
    certified_count = guard.get("certified_segment_count")
    if (
        isinstance(segment_count, bool)
        or not isinstance(segment_count, int)
        or segment_count <= 0
        or segment_count != len(checkpoint_files) - 1
        or isinstance(accepted_count, bool)
        or not isinstance(accepted_count, int)
        or accepted_count != segment_count
    ):
        raise ValueError("chain checkpoint/segment count mismatch")
    if (
        isinstance(certified_count, bool)
        or not isinstance(certified_count, int)
        or certified_count != segment_count
    ):
        raise ValueError("clearance-floor certified segment count mismatch")

    generated_sha256 = certificate.get("generated_sha256")
    face_value = certificate.get("face_file")
    expected_generated_files = [*checkpoint_files, face_value]
    if (
        not isinstance(generated_sha256, dict)
        or not isinstance(face_value, str)
        or not face_value
        or len(expected_generated_files) != len(set(expected_generated_files))
        or set(generated_sha256) != set(expected_generated_files)
    ):
        raise ValueError("post-bypass chain generated-file ledger mismatch")
    checkpoint_sha256 = []
    for index, checkpoint in enumerate(checkpoint_files):
        validated_file_binding(
            checkpoint,
            generated_sha256.get(checkpoint),
            f"exact_checkpoint_files.{index}",
        )
        checkpoint_sha256.append(generated_sha256[checkpoint])
    validated_face_binding(certificate, "post_bypass_chain")

    final_checkpoint = checkpoint_files[-1]
    expected_source_sha = checkpoint_sha256[-1]
    generated_endpoint_path = resolve_root_path(final_checkpoint)
    if source_path.resolve() != generated_endpoint_path.resolve():
        raise ValueError((
            "--source path is not the chain's generated exact final checkpoint",
            str(source_path),
            final_checkpoint,
        ))
    actual_source_sha = sha256(source_path)
    if actual_source_sha != expected_source_sha:
        raise ValueError((
            "--source bytes are not the chain's generated exact final checkpoint",
            actual_source_sha,
            expected_source_sha,
        ))

    source_certificate_value = guard.get("source_certificate")
    source_certificate_path = validated_file_binding(
        source_certificate_value,
        guard.get("source_certificate_sha256"),
        "guard.source_certificate",
    )
    actual_source_certificate_sha = sha256(source_certificate_path)
    source_certificate = json.loads(source_certificate_path.read_text())
    if not isinstance(source_certificate, dict):
        raise ValueError("source bypass certificate is not an object")
    if (
        type(source_certificate.get("version")) is not int
        or source_certificate["version"] != 1
    ):
        raise ValueError("unsupported source bypass certificate version")
    if source_certificate.get("verdict") != EXPECTED_CLEARANCE_VERDICT:
        raise ValueError("source bypass certificate verdict mismatch")
    if tuple(source_certificate.get("circuit", ())) != tuple(circuit):
        raise ValueError("source bypass certificate circuit mismatch")

    source_exact_files = source_certificate.get("exact_files")
    if (
        not isinstance(source_exact_files, dict)
        or set(source_exact_files) != {"source", "pre", "lifted", "endpoint"}
        or any(
            not isinstance(value, str) or not value
            for value in source_exact_files.values()
        )
        or len(set(source_exact_files.values())) != len(source_exact_files)
    ):
        raise ValueError("source bypass certificate has malformed exact files")
    source_endpoint = source_exact_files["endpoint"]
    source_face_value = source_certificate.get("face_file")
    source_hashes = source_certificate.get("generated_sha256")
    source_generated_files = [*source_exact_files.values(), source_face_value]
    if (
        not isinstance(source_hashes, dict)
        or not isinstance(source_face_value, str)
        or not source_face_value
        or len(source_generated_files) != len(set(source_generated_files))
        or set(source_hashes) != set(source_generated_files)
    ):
        raise ValueError("source bypass generated-file ledger mismatch")
    for value in source_generated_files:
        validated_file_binding(
            value,
            source_hashes.get(value),
            f"source_bypass.generated_sha256.{value}",
        )
    source_endpoint_path = resolve_root_path(source_endpoint)
    source_endpoint_sha = source_hashes[source_endpoint]
    source_faces = validated_face_binding(source_certificate, "source_bypass")
    source_site_count = len(exact_path.ex.read_rows(source_endpoint_path))
    if source_site_count <= 0:
        raise ValueError("source bypass endpoint has no sites")
    if guard.get("source_endpoint_file") != source_endpoint:
        raise ValueError("guard source endpoint path mismatch")
    if guard.get("source_endpoint_sha256") != source_endpoint_sha:
        raise ValueError("guard source endpoint SHA-256 mismatch")

    checkpoint_clearance = source_certificate.get(
        "circuit_clearance_at_checkpoints"
    )
    if not isinstance(checkpoint_clearance, dict):
        raise ValueError("source bypass certificate has no checkpoint clearances")
    source_endpoint_clearance = checkpoint_clearance.get("endpoint")
    if not isinstance(source_endpoint_clearance, dict):
        raise ValueError("source bypass certificate has no endpoint clearance")
    if source_endpoint_clearance.get("strictly_positive") is not True:
        raise ValueError("source bypass endpoint clearance is not strictly positive")

    labels = tuple(str(label) for label in circuit[:2])
    determinant = exact_fraction(
        source_endpoint_clearance.get("determinant"),
        "source_endpoint_clearance.determinant",
    )
    radius_squared = exact_fraction(
        source_endpoint_clearance.get("rms_radius_squared"),
        "source_endpoint_clearance.rms_radius_squared",
    )
    opposite_area_squared = exact_fraction_map(
        source_endpoint_clearance.get("opposite_area_squared"),
        "source_endpoint_clearance.opposite_area_squared",
        labels,
    )
    source_clearance_squared = exact_fraction_map(
        source_endpoint_clearance.get("normalized_opposite_slack_squared"),
        "source_endpoint_clearance.normalized_opposite_slack_squared",
        labels,
    )
    if (
        determinant == 0
        or radius_squared <= 0
        or any(value <= 0 for value in opposite_area_squared.values())
        or any(value <= 0 for value in source_clearance_squared.values())
    ):
        raise ValueError("nonpositive source clearance geometry")
    for label in labels:
        reconstructed_clearance = determinant * determinant / (
            radius_squared * opposite_area_squared[label]
        )
        if source_clearance_squared[label] != reconstructed_clearance:
            raise ValueError((label, "source clearance exact identity mismatch"))

    exact_floor = exact_fraction(
        source_endpoint_clearance.get(
            "minimum_normalized_opposite_slack_squared"
        ),
        "source_endpoint_clearance.minimum_normalized_opposite_slack_squared",
    )
    if exact_floor <= 0 or exact_floor != min(source_clearance_squared.values()):
        raise ValueError("source clearance floor is not the exact minimum")
    floor_vertices = [
        label for label in labels if source_clearance_squared[label] == exact_floor
    ]
    if exact_fraction(
        guard.get("kappa_squared_exact"), "guard.kappa_squared_exact"
    ) != exact_floor:
        raise ValueError("guard kappa does not match the source floor")
    declared_source_clearance = exact_fraction_map(
        guard.get("source_clearance_squared_exact"),
        "guard.source_clearance_squared_exact",
        labels,
    )
    if declared_source_clearance != source_clearance_squared:
        raise ValueError("guard source clearances do not match the source certificate")
    if guard.get("source_floor_vertices") != floor_vertices:
        raise ValueError("guard source floor vertices mismatch")

    inherited_contract = {}
    if "floor_source_kind" not in guard:
        chain_source = source_endpoint
        chain_source_sha = source_endpoint_sha
    elif guard.get("floor_source_kind") == INHERITED_FLOOR_SOURCE_KIND:
        chain_source, chain_source_sha, inherited_contract = (
            load_inherited_guarded_chain_source(
                guard,
                circuit,
                exact_floor,
                visited,
            )
        )
    else:
        raise ValueError((
            "unknown guarded floor source kind",
            guard.get("floor_source_kind"),
        ))

    if certificate.get("source") != chain_source:
        raise ValueError("chain source path does not match its guarded lineage")
    validated_file_binding(
        chain_source,
        chain_source_sha,
        "post_bypass_chain.source",
    )
    if guard.get("chain_source_sha256") != chain_source_sha:
        raise ValueError("guard chain source SHA-256 mismatch")
    if checkpoint_sha256[0] != chain_source_sha:
        raise ValueError("exact chain source checkpoint SHA-256 mismatch")

    material_segments = certificate.get("segments")
    guard_segments = guard.get("segments")
    if (
        not isinstance(material_segments, list)
        or len(material_segments) != segment_count
        or not isinstance(guard_segments, list)
        or len(guard_segments) != segment_count
    ):
        raise ValueError("material/clearance-floor segment schema mismatch")
    final_segment_endpoint = None
    for index, (material_segment, segment) in enumerate(
        zip(material_segments, guard_segments)
    ):
        left = f"checkpoint_{index:03d}"
        right = f"checkpoint_{index + 1:03d}"
        if (
            not isinstance(material_segment, dict)
            or material_segment.get("left") != left
            or material_segment.get("right") != right
            or not isinstance(segment, dict)
            or segment.get("left") != left
            or segment.get("right") != right
        ):
            raise ValueError((index, "material/clearance-floor segment chain mismatch"))
        if exact_fraction(
            segment.get("kappa_squared_exact"),
            f"clearance_floor_guard.segments.{index}.kappa_squared_exact",
        ) != exact_floor:
            raise ValueError((index, "clearance-floor segment kappa mismatch"))
        final_segment_endpoint = endpoint_tau_ratios(
            segment.get("endpoint_tau_ratios"),
            f"clearance_floor_guard.segments.{index}.endpoint_tau_ratios",
            labels,
            exact_floor,
        )
    chain_endpoint = endpoint_tau_ratios(
        guard.get("chain_endpoint_tau_ratios"),
        "clearance_floor_guard.chain_endpoint_tau_ratios",
        labels,
        exact_floor,
    )
    if chain_endpoint != final_segment_endpoint:
        raise ValueError("chain endpoint clearance/tau record mismatch")

    contract = {
        "certificate": str(path),
        "verdict": certificate["verdict"],
        "version": certificate["version"],
        "clearance_floor_mode": guard["mode"],
        "circuit": list(circuit),
        "chain_source": chain_source,
        "chain_source_sha256": chain_source_sha,
        "generated_endpoint": final_checkpoint,
        "generated_endpoint_sha256": expected_source_sha,
        "source_sha256": actual_source_sha,
        "source_floor_certificate": source_certificate_value,
        "source_floor_certificate_sha256": actual_source_certificate_sha,
        "source_floor_endpoint": source_endpoint,
        "source_floor_endpoint_sha256": source_endpoint_sha,
        "source_floor_face_file": source_faces["value"],
        "source_floor_face_file_sha256": source_faces["file_sha256"],
        "source_floor_face_hash": source_faces["face_hash"],
        "source_floor_site_count": source_site_count,
        "source_floor_clearance_squared_exact": {
            label: str(source_clearance_squared[label]) for label in labels
        },
        "source_floor_vertices": floor_vertices,
        "exact_minimum_floor_squared": str(exact_floor),
        "numeric_minimum_floor_squared": float(exact_floor),
        "chain_endpoint_clearance_squared_exact": {
            label: str(chain_endpoint[label][0]) for label in labels
        },
        "chain_endpoint_tau_ratio_exact": {
            label: str(chain_endpoint[label][1]) for label in labels
        },
    }
    contract.update(inherited_contract)
    return exact_floor, contract


def load_clearance_floor_certificate(path: Path, source_path: Path, circuit):
    certificate = json.loads(path.read_text())
    if not isinstance(certificate, dict):
        raise ValueError("clearance-floor certificate is not an object")
    if certificate.get("verdict") == EXPECTED_CHAIN_VERDICT:
        return load_guarded_chain_clearance_floor(
            certificate,
            path,
            source_path,
            circuit,
        )
    if certificate.get("verdict") != EXPECTED_CLEARANCE_VERDICT:
        raise ValueError((
            "wrong clearance-floor certificate verdict",
            certificate.get("verdict"),
            (EXPECTED_CLEARANCE_VERDICT, EXPECTED_CHAIN_VERDICT),
        ))
    try:
        certificate_circuit = tuple(certificate["circuit"])
        endpoint_file = certificate["exact_files"]["endpoint"]
        expected_source_sha = certificate["generated_sha256"][endpoint_file]
        endpoint_clearance = certificate["circuit_clearance_at_checkpoints"]["endpoint"]
        exact_by_vertex = endpoint_clearance["normalized_opposite_slack_squared"]
        exact_floor_text = endpoint_clearance[
            "minimum_normalized_opposite_slack_squared"
        ]
    except (KeyError, TypeError) as error:
        raise ValueError("incomplete clearance-floor certificate") from error
    if certificate_circuit != tuple(circuit):
        raise ValueError((
            "clearance-floor certificate circuit mismatch",
            certificate_circuit,
            tuple(circuit),
        ))
    if (
        not isinstance(expected_source_sha, str)
        or len(expected_source_sha) != 64
        or any(character not in "0123456789abcdef" for character in expected_source_sha)
    ):
        raise ValueError("malformed generated endpoint SHA-256")
    actual_source_sha = sha256(source_path)
    if actual_source_sha != expected_source_sha:
        raise ValueError((
            "--source is not the certificate's generated exact endpoint",
            actual_source_sha,
            expected_source_sha,
        ))

    expected_vertices = {str(circuit[0]), str(circuit[1])}
    if not isinstance(exact_by_vertex, dict) or set(exact_by_vertex) != expected_vertices:
        raise ValueError((
            "clearance-floor certificate has the wrong opposite vertices",
            sorted(exact_by_vertex) if isinstance(exact_by_vertex, dict) else None,
            sorted(expected_vertices),
        ))
    if not isinstance(exact_floor_text, str):
        raise ValueError("clearance floor is not an exact rational string")
    try:
        exact_values = {
            int(label): Q(value)
            for label, value in exact_by_vertex.items()
            if isinstance(value, str)
        }
        exact_floor = Q(exact_floor_text)
    except (ValueError, ZeroDivisionError) as error:
        raise ValueError("invalid exact rational clearance floor") from error
    if set(exact_values) != {circuit[0], circuit[1]}:
        raise ValueError("opposite-vertex clearances are not exact rational strings")
    if any(value <= 0 for value in exact_values.values()) or exact_floor <= 0:
        raise ValueError("clearance floor is not strictly positive")
    reconstructed_floor = min(exact_values.values())
    if exact_floor != reconstructed_floor:
        raise ValueError((
            "certificate minimum clearance floor mismatch",
            str(exact_floor),
            str(reconstructed_floor),
        ))
    if endpoint_clearance.get("strictly_positive") is not True:
        raise ValueError("clearance-floor certificate does not assert strict positivity")
    return exact_floor, {
        "certificate": str(path),
        "verdict": certificate["verdict"],
        "circuit": list(circuit),
        "generated_endpoint": endpoint_file,
        "generated_endpoint_sha256": expected_source_sha,
        "source_sha256": actual_source_sha,
        "exact_minimum_floor_squared": str(exact_floor),
        "numeric_minimum_floor_squared": float(exact_floor),
    }


def clearance_tau(points, result, circuit, exact_floor):
    missing = set(circuit) - set(points)
    if missing:
        raise ValueError(("circuit labels absent from points", sorted(missing)))
    floor = np.longdouble(float(exact_floor))
    if not np.isfinite(floor) or floor <= 0:
        raise ValueError("clearance floor is not numerically representable")
    centroid = np.asarray(result.centroid, dtype=np.longdouble)
    long_points = {
        label: np.asarray(point, dtype=np.longdouble)
        for label, point in points.items()
    }
    radius_squared = sum(
        np.dot(point - centroid, point - centroid)
        for point in long_points.values()
    ) / np.longdouble(len(long_points))
    a, b, c, d = circuit
    determinant = np.dot(
        long_points[b] - long_points[a],
        np.cross(
            long_points[c] - long_points[a],
            long_points[d] - long_points[a],
        ),
    )
    opposite_cross = {
        a: np.cross(
            long_points[c] - long_points[b],
            long_points[d] - long_points[b],
        ),
        b: np.cross(
            long_points[c] - long_points[a],
            long_points[d] - long_points[a],
        ),
    }
    if radius_squared <= 0 or determinant == 0:
        raise ValueError("degenerate circuit-clearance geometry")
    tau = {}
    for label, cross in opposite_cross.items():
        area_squared = np.dot(cross, cross)
        if area_squared <= 0:
            raise ValueError(("degenerate opposite circuit face", label))
        normalized_squared = determinant * determinant / (
            radius_squared * area_squared
        )
        value = normalized_squared / floor
        if not np.isfinite(value) or value <= 0:
            raise ValueError(("invalid dimensionless squared clearance ratio", label))
        tau[label] = float(value)
    return tau


def objective_residual_keys(values):
    quad_keys = [
        key
        for key in values
        if key[0] == "face"
        and frozenset(key[1]) == four.QUAD
        and key[2] == (8, 246)
    ]
    if len(quad_keys) != 1:
        raise ValueError(("wrong S_quad primitive count", len(quad_keys)))
    residuals = {
        "S_quad": quad_keys[0],
        "U54": ("vertex", 54, 1),
        "H67_beta2": ("edge", (6, 7), "beta2"),
        "H910_beta2": ("edge", (9, 10), "beta2"),
    }
    for name, key in residuals.items():
        if key not in values:
            raise ValueError(("missing objective residual", name, key))
        if not np.isfinite(values[key]) or values[key] <= 0:
            raise ValueError(("nonpositive objective residual", name, values[key]))
    return residuals


def primitive_sign_signature(values):
    signature = {}
    for key, value in values.items():
        if not np.isfinite(value) or value == 0:
            raise ValueError(("nonstrict primitive", key, value))
        signature[key] = 1 if value > 0 else -1
    return signature


def forced_rails_retained(result):
    edges = {tuple(sorted(edge)) for edge in result.edges}
    return exact_path.forced_rails().issubset(edges)


def load_exact_float(path: Path):
    return {
        label: np.asarray([float(value) for value in xyz], dtype=float)
        for label, xyz in exact_path.ex.read_rows(path).items()
    }


def apply_modes(points, modes, coefficients):
    out = {label: np.asarray(point, dtype=float).copy() for label, point in points.items()}
    for column, coefficient in enumerate(coefficients):
        if coefficient == 0:
            continue
        for label in out:
            out[label] += coefficient * modes[column][label]
    # The linear chart is tangent to the protected quadrilateral manifold.
    # Finite steps otherwise accumulate a second-order normal component at
    # row 246 and falsely split the exact face.  Enforce the stated geometry
    # invariant explicitly after every nonlinear materialization.
    anchor = out[7]
    normal = np.cross(out[8] - anchor, out[245] - anchor)
    normal_norm2 = float(np.dot(normal, normal))
    if normal_norm2 <= 1e-30:
        raise ValueError("degenerate protected quadrilateral plane")
    coefficient = float(np.dot(normal, out[246] - anchor) / normal_norm2)
    out[246] -= coefficient * normal
    return out


def topology_guard_determinants(points, circuits):
    """Return signed circuit determinants in the caller-declared orientation."""
    values = {}
    for circuit in circuits:
        missing = set(circuit) - set(points)
        if missing:
            raise ValueError(("topology-guard labels absent from points", sorted(missing)))
        a, b, c, d = (
            np.asarray(points[label], dtype=np.longdouble) for label in circuit
        )
        determinant = np.dot(np.cross(b - a, c - a), d - a)
        value = float(determinant)
        if not np.isfinite(value) or value == 0.0:
            raise ValueError(("nonstrict topology-guard determinant", circuit, value))
        values[circuit] = value
    return values


def face_signature(result):
    return tuple(sorted(tuple(sorted(face["cycle"])) for face in result.faces))


def equilibrium_signature(result):
    return (
        tuple(sorted(tuple(sorted(result.faces[index]["cycle"])) for index, _ in result.stable)),
        tuple(sorted(index for index, _ in result.unstable)),
        tuple(sorted(tuple(edge) for edge, _ in result.saddles)),
    )


def robust_primitive_ledger(points, plane_tol):
    """Complete primitive ledger with a stable two-normal cone solve.

    The historical baseline evaluator forms ``aa*cc-bb*bb`` for unit face
    normals and rejects values below 1e-14.  The protected rail geometry has a
    legitimate true edge (250,251) whose exact shallow dihedral gives a Gram
    determinant around 1e-14, so binary64 cancellation can alternately reject
    either side of an otherwise strict central probe.  Rebuild the same full
    ledger on the current actual-hull evaluator and use the algebraically
    identical squared-cross-product determinant plus cross-product Cramer
    numerators in long double.  No primitive, mode, or failed side is dropped.
    """
    result = exact_path.actual.evaluate(points, coplanar_rel=plane_tol)
    if not result.valid:
        raise RuntimeError(result.error)
    P = {label: np.asarray(point, dtype=float) for label, point in points.items()}
    X = {label: point - result.centroid for label, point in P.items()}
    values = {}

    for face in result.faces:
        cycle = list(face["cycle"])
        face_key = tuple(sorted(cycle))
        normal = np.asarray(face["n"], dtype=float)
        height = -(float(face["off"]) + float(np.dot(normal, result.centroid)))
        foot = height * normal
        reference = np.mean([X[label] for label in cycle], axis=0)
        for a, b in zip(cycle, cycle[1:] + cycle[:1]):
            edge_vector = X[b] - X[a]
            edge_norm = float(np.linalg.norm(edge_vector))
            if not edge_norm > 1e-300:
                raise RuntimeError(("zero face edge", a, b))
            value = float(
                np.dot(np.cross(edge_vector, foot - X[a]), normal) / edge_norm
            )
            if np.dot(np.cross(edge_vector, reference - X[a]), normal) < 0:
                value = -value
            values[("face", face_key, tuple(sorted((a, b))))] = value
        face_set = set(cycle)
        for label in sorted(P):
            if label not in face_set:
                values[("topology", face_key, label)] = -float(
                    np.dot(P[label], normal) + face["off"]
                )

        reference_world = np.mean([P[label] for label in cycle], axis=0)
        for a, b in zip(cycle, cycle[1:] + cycle[:1]):
            edge_vector = P[b] - P[a]
            edge_norm = float(np.linalg.norm(edge_vector))
            side = float(
                np.dot(np.cross(edge_vector, reference_world - P[a]), normal)
            )
            sign = 1.0 if side >= 0 else -1.0
            edge = tuple(sorted((a, b)))
            for witness in cycle:
                if witness in (a, b):
                    continue
                value = sign * float(
                    np.dot(np.cross(edge_vector, P[witness] - P[a]), normal)
                ) / edge_norm
                values[("incidence", face_key, edge, witness)] = value

    for label in result.active:
        point = X[label]
        point_norm = float(np.linalg.norm(point))
        if not point_norm > 1e-300:
            raise RuntimeError(("centroid at active vertex", label))
        for neighbor in sorted(result.neighbors[label]):
            direction = X[neighbor] - point
            direction_norm = float(np.linalg.norm(direction))
            if not direction_norm > 1e-300:
                raise RuntimeError(("zero true edge", label, neighbor))
            values[("vertex", label, neighbor)] = -float(
                np.dot(point, direction) / (point_norm * direction_norm)
            )

    face_by_index = {index: face for index, face in enumerate(result.faces)}
    for edge in result.edges:
        a, b = edge
        incident = result.edge_faces[edge]
        if len(incident) != 2:
            raise RuntimeError(("nonmanifold true edge", edge, incident))
        direction = np.asarray(X[b] - X[a], dtype=np.longdouble)
        dd = np.dot(direction, direction)
        if not dd > np.longdouble("1e-30"):
            raise RuntimeError(("degenerate true edge", edge))
        xa = np.asarray(X[a], dtype=np.longdouble)
        t = -np.dot(xa, direction) / dd
        foot = xa + t * direction
        n1 = np.asarray(face_by_index[incident[0]]["n"], dtype=np.longdouble)
        n2 = np.asarray(face_by_index[incident[1]]["n"], dtype=np.longdouble)
        cross12 = np.cross(n1, n2)
        determinant = np.dot(cross12, cross12)
        if not determinant > np.longdouble("1e-26"):
            raise RuntimeError(("geometrically parallel face normals", edge, str(determinant)))
        beta1 = np.dot(np.cross(foot, n2), cross12) / determinant
        beta2 = np.dot(np.cross(n1, foot), cross12) / determinant
        foot_norm = np.sqrt(np.dot(foot, foot))
        if not foot_norm > np.longdouble("1e-30"):
            raise RuntimeError(("centroid line meets true edge", edge))
        values[("edge", edge, "t")] = float(t)
        values[("edge", edge, "one_minus_t")] = float(1 - t)
        values[("edge", edge, "beta1")] = float(beta1 / foot_norm)
        values[("edge", edge, "beta2")] = float(beta2 / foot_norm)
    return result, values


def state(points, plane_tol):
    result, values = robust_primitive_ledger(points, plane_tol)
    return result, values, face_signature(result), equilibrium_signature(result)


def displacement_matrix(points, modes):
    return np.asarray([
        [modes[column][label][axis] for column in range(len(modes))]
        for label in sorted(points)
        for axis in range(3)
    ])


def adaptive_finite_difference(
    points,
    values,
    clearance_values,
    topology_values,
    modes,
    initial_step,
    plane_tol,
    circuit,
    exact_floor,
):
    """Central derivatives on the intrinsic quadrilateral manifold.

    Each column is retried at explicitly recorded smaller scales.  No
    one-sided or zero-column substitution is allowed: failure at every scale
    aborts the solve.
    """
    keys = list(values)
    key_index = {key: index for index, key in enumerate(keys)}
    jacobian = np.empty((len(keys), len(modes)))
    clearance_labels = list(clearance_values)
    clearance_jacobian = np.empty((len(clearance_labels), len(modes)))
    topology_circuits = list(topology_values)
    topology_jacobian = np.empty((len(topology_circuits), len(modes)))
    diagnostics = []
    for column in range(len(modes)):
        errors = []
        accepted = None
        for reduction in range(9):
            step = initial_step / (4.0 ** reduction)
            delta = np.zeros(len(modes))
            delta[column] = step
            plus = apply_modes(points, modes, delta)
            minus = apply_modes(points, modes, -delta)
            try:
                rp, vp = robust_primitive_ledger(plus, plane_tol)
                rm, vm = robust_primitive_ledger(minus, plane_tol)
                if set(vp) != set(values) or set(vm) != set(values):
                    raise RuntimeError("primitive key set changed")
                tau_plus = clearance_tau(plus, rp, circuit, exact_floor)
                tau_minus = clearance_tau(minus, rm, circuit, exact_floor)
                if (
                    set(tau_plus) != set(clearance_values)
                    or set(tau_minus) != set(clearance_values)
                ):
                    raise RuntimeError("clearance-ratio key set changed")
                topology_plus = topology_guard_determinants(
                    plus, topology_circuits
                )
                topology_minus = topology_guard_determinants(
                    minus, topology_circuits
                )
                jacobian[:, column] = np.asarray([
                    (vp[key] - vm[key]) / (2.0 * step) for key in keys
                ])
                clearance_jacobian[:, column] = np.asarray([
                    (tau_plus[label] - tau_minus[label]) / (2.0 * step)
                    for label in clearance_labels
                ])
                topology_jacobian[:, column] = np.asarray([
                    (topology_plus[circuit] - topology_minus[circuit])
                    / (2.0 * step)
                    for circuit in topology_circuits
                ])
                accepted = step
                break
            except Exception as error:
                errors.append({"step": step, "error": repr(error)})
        if accepted is None:
            raise RuntimeError(("intrinsic central derivative failed", column, errors))
        if errors:
            diagnostics.append({
                "column": column,
                "accepted_step": accepted,
                "rejected_scales": errors,
            })
    return (
        keys,
        key_index,
        jacobian,
        clearance_labels,
        clearance_jacobian,
        topology_circuits,
        topology_jacobian,
        diagnostics,
    )


def solve_step(
    points,
    result,
    values,
    trust,
    guard_budget,
    fd_step,
    bound,
    plane_tol,
    circuit,
    exact_floor,
    clearance_linear_buffer,
    topology_guard_circuits,
    topology_guard_linear_buffer,
):
    modes, mode_meta, chart_meta = four.chart_modes(points)
    clearance_values = clearance_tau(points, result, circuit, exact_floor)
    topology_values = topology_guard_determinants(
        points, topology_guard_circuits
    )
    (
        keys,
        key_index,
        jacobian,
        clearance_labels,
        clearance_jacobian,
        topology_circuits,
        topology_jacobian,
        failures,
    ) = adaptive_finite_difference(
        points,
        values,
        clearance_values,
        topology_values,
        modes,
        fd_step,
        plane_tol,
        circuit,
        exact_floor,
    )
    residuals = objective_residual_keys(values)
    deaths = tuple(residuals.values())
    death_matrix = np.asarray([
        jacobian[key_index[key]] / values[key] for key in deaths
    ])
    guards = four.chosen_guards(values)
    guard_matrix = np.asarray([
        -sign * jacobian[key_index[key]] / max(abs(values[key]), 1e-12)
        for key, sign, _kind in guards
    ])
    topology_source = np.asarray([
        topology_values[circuit] for circuit in topology_circuits
    ])
    topology_signs = np.sign(topology_source)
    topology_fractional_jacobian = (
        topology_signs[:, None]
        * topology_jacobian
        / np.abs(topology_source)[:, None]
    )
    D = displacement_matrix(points, modes)
    matrices = {
        "jacobian": jacobian,
        "clearance_jacobian": clearance_jacobian,
        "topology_jacobian": topology_jacobian,
        "topology_fractional_jacobian": topology_fractional_jacobian,
        "death_matrix": death_matrix,
        "guard_matrix": guard_matrix,
        "displacement_matrix": D,
    }
    for name, matrix in matrices.items():
        if not np.all(np.isfinite(matrix)):
            raise RuntimeError(("nonfinite continuation matrix", name))
    n = len(modes)
    if not np.isfinite(clearance_linear_buffer) or clearance_linear_buffer <= 0:
        raise ValueError("clearance linear buffer must be strictly positive")
    if (
        topology_circuits
        and (
            not np.isfinite(topology_guard_linear_buffer)
            or topology_guard_linear_buffer <= 0
        )
    ):
        raise ValueError("topology-guard linear buffer must be strictly positive")
    clearance_rhs = np.asarray([
        clearance_values[label] - 1.0 - clearance_linear_buffer
        for label in clearance_labels
    ])
    topology_rhs = np.full(
        len(topology_circuits), -topology_guard_linear_buffer
    )
    # Variables are chart coefficients c and common fractional descent q.
    # Clearance and topology rows are literal, unbudgeted linearizations.
    # For a topology circuit, -sign(D) grad(D)c/|D| <= -buffer forces
    # strict inward motion in the caller-declared orientation.
    A = np.vstack((
        np.c_[guard_matrix, np.zeros(len(guards))],
        np.c_[-clearance_jacobian, np.zeros(len(clearance_labels))],
        np.c_[
            -topology_fractional_jacobian,
            np.zeros(len(topology_circuits)),
        ],
        np.c_[death_matrix, np.ones(4)],
        np.c_[D, np.zeros(D.shape[0])],
        np.c_[-D, np.zeros(D.shape[0])],
    ))
    b = np.r_[
        np.full(len(guards), guard_budget),
        clearance_rhs,
        topology_rhs,
        np.zeros(4),
        np.full(2 * D.shape[0], trust),
    ]
    # Positive row scaling leaves the LP polyhedron exactly unchanged.  Every
    # original row and scale remains reconstructible from the recorded data.
    row_scale = np.maximum(
        np.maximum(np.max(np.abs(A), axis=1), np.abs(b)),
        1e-300,
    )
    clearance_rows = slice(len(guards), len(guards) + len(clearance_labels))
    topology_rows = slice(
        clearance_rows.stop,
        clearance_rows.stop + len(topology_circuits),
    )
    # Keep the two clearance inequalities in their literal dimensionless tau
    # units.  Scaling them by a huge Jacobian coefficient makes HiGHS' absolute
    # feasibility tolerance permit a macroscopically false floor crossing.
    row_scale[clearance_rows] = 1.0
    row_scale[topology_rows] = 1.0
    solver_A = A / row_scale[:, None]
    solver_b = b / row_scale
    zero_violation = float(np.max(-solver_b))
    lp = linprog(
        np.r_[np.zeros(n), -1.0],
        A_ub=solver_A,
        b_ub=solver_b,
        bounds=[(-bound, bound)] * n + [(0.0, 1.0)],
        method="highs-ds",
        options={
            "presolve": False,
            "primal_feasibility_tolerance": 1e-9,
            "dual_feasibility_tolerance": 1e-9,
        },
    )
    record = {
        "h67_component": "beta2",
        "h910_component": "beta2",
        "objective_residuals": list(residuals),
        "success": bool(lp.success),
        "status": int(lp.status),
        "message": lp.message,
        "row_scale_minimum": float(np.min(row_scale)),
        "row_scale_maximum": float(np.max(row_scale)),
        "zero_step_maximum_violation": zero_violation,
        "source_clearance_tau": {
            str(label): clearance_values[label] for label in clearance_labels
        },
        "clearance_floor_rhs": clearance_rhs.tolist(),
        "topology_guard_source_determinants": {
            ",".join(str(label) for label in circuit): topology_values[circuit]
            for circuit in topology_circuits
        },
        "topology_guard_linear_buffer": topology_guard_linear_buffer,
        "topology_guard_rhs": topology_rhs.tolist(),
    }
    if not lp.success:
        ranges = {
            name: (
                {
                    "minimum": float(np.min(matrix)),
                    "maximum": float(np.max(matrix)),
                    "maximum_absolute": float(np.max(np.abs(matrix))),
                }
                if matrix.size
                else {
                    "minimum": None,
                    "maximum": None,
                    "maximum_absolute": None,
                }
            )
            for name, matrix in matrices.items()
        }
        raise RuntimeError((
            "no trust-bounded fixed-residual descent",
            ranges,
            {"status": record["status"], "message": record["message"]},
        ))
    coefficients = np.asarray(lp.x[:n])
    raw_clearance_slack = clearance_rhs + clearance_jacobian @ coefficients
    linearized_clearance = np.asarray([
        clearance_values[label] for label in clearance_labels
    ]) + clearance_jacobian @ coefficients
    if np.min(raw_clearance_slack) < -1e-10:
        raise RuntimeError((
            "solver returned clearance-infeasible coefficients",
            raw_clearance_slack.tolist(),
        ))
    if np.min(linearized_clearance) <= 1.0 + clearance_linear_buffer - 1e-10:
        raise RuntimeError((
            "linearized clearance endpoint lacks the required inward buffer",
            linearized_clearance.tolist(),
            clearance_linear_buffer,
        ))
    topology_inward_slack = (
        topology_fractional_jacobian @ coefficients
        - topology_guard_linear_buffer
    )
    linearized_topology_ratios = (
        1.0 + topology_fractional_jacobian @ coefficients
    )
    if topology_circuits and np.min(topology_inward_slack) < -1e-10:
        raise RuntimeError((
            "solver returned topology-guard-infeasible coefficients",
            topology_inward_slack.tolist(),
        ))
    if (
        topology_circuits
        and np.min(linearized_topology_ratios)
        <= 1.0 + topology_guard_linear_buffer - 1e-10
    ):
        raise RuntimeError((
            "linearized topology-guard endpoint lacks the required inward buffer",
            linearized_topology_ratios.tolist(),
            topology_guard_linear_buffer,
        ))
    record.update({
        "common_fractional_descent": float(lp.x[-1]),
        "physical_linf": float(np.max(np.abs(D @ coefficients))),
        "coefficient_linf": float(np.max(np.abs(coefficients))),
        "coefficients": coefficients.tolist(),
        "deaths": [repr(key) for key in deaths],
        "death_fractional_derivatives": (death_matrix @ coefficients).tolist(),
        "clearance_tau_derivatives": (
            clearance_jacobian @ coefficients
        ).tolist(),
        "clearance_linear_buffer": clearance_linear_buffer,
        "raw_clearance_constraint_slack": raw_clearance_slack.tolist(),
        "linearized_endpoint_clearance_tau": {
            str(label): float(linearized_clearance[index])
            for index, label in enumerate(clearance_labels)
        },
        "topology_guard_fractional_derivatives": (
            topology_fractional_jacobian @ coefficients
        ).tolist(),
        "raw_topology_guard_constraint_slack": topology_inward_slack.tolist(),
        "linearized_endpoint_topology_guard_ratios": {
            ",".join(str(label) for label in circuit): float(
                linearized_topology_ratios[index]
            )
            for index, circuit in enumerate(topology_circuits)
        },
        "max_guard_fractional_worsening": float(
            np.max(guard_matrix @ coefficients)
        ),
        "active_modes": [
            {
                "column": int(index),
                "coefficient": float(coefficients[index]),
                **mode_meta[index],
            }
            for index in np.argsort(np.abs(coefficients))[-20:][::-1]
        ],
    })
    return modes, record, {
        "chart": chart_meta,
        "mode_count": len(modes),
        "primitive_count": len(keys),
        "guard_count": len(guards),
        "clearance_row_count": len(clearance_labels),
        "topology_guard_row_count": len(topology_circuits),
        "finite_difference_failures": failures,
    }


def event_at_fraction(points, modes, coefficients, fraction, plane_tol):
    candidate = apply_modes(points, modes, fraction * coefficients)
    try:
        return candidate, state(candidate, plane_tol), None
    except Exception as error:
        return candidate, None, repr(error)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fail-closed one-step cycle-11 actual-cell proposal"
    )
    parser.add_argument("--source", default=str(SOURCE))
    parser.add_argument("--circuit", type=parse_circuit, required=True)
    parser.add_argument("--clearance-floor-certificate", required=True)
    parser.add_argument(
        "--require-accepted-step",
        action="store_true",
        required=True,
        help="exit nonzero unless the one proposed step passes every actual-endpoint check",
    )
    parser.add_argument("--prefix", default="post_flip_trust")
    parser.add_argument("--iterations", type=int, choices=(1,), default=1)
    parser.add_argument("--trust", type=float, default=1e-7)
    parser.add_argument("--trust-maximum", type=float, default=2e-5)
    parser.add_argument("--guard-budget", type=float, default=0.15)
    parser.add_argument("--fd-step", type=float, default=1e-9)
    parser.add_argument("--clearance-linear-buffer", type=float, default=1e-5)
    parser.add_argument(
        "--require-clearance-inward",
        action="store_true",
        help=(
            "accept only if both actual nonlinear endpoint clearance ratios "
            "strictly exceed their source values"
        ),
    )
    parser.add_argument(
        "--topology-guard-circuit",
        type=parse_circuit,
        action="append",
        default=[],
        help=(
            "repeat for each signed circuit determinant that must move "
            "strictly inward"
        ),
    )
    parser.add_argument(
        "--topology-guard-linear-buffer",
        type=float,
        default=1e-2,
        help="required fractional inward motion for every topology guard",
    )
    parser.add_argument("--bound", type=float, default=300.0)
    parser.add_argument("--plane-tol", type=float, default=1e-11)
    args = parser.parse_args()

    if len(set(args.topology_guard_circuit)) != len(args.topology_guard_circuit):
        raise ValueError("duplicate topology-guard circuit")

    four.ACTIVE_PLANE_TOL = args.plane_tol
    source_path = Path(args.source)
    if not source_path.is_absolute():
        source_path = HERE / source_path
    certificate_path = Path(args.clearance_floor_certificate)
    if not certificate_path.is_absolute():
        certificate_path = HERE / certificate_path
    exact_floor, clearance_contract = load_clearance_floor_certificate(
        certificate_path,
        source_path,
        args.circuit,
    )
    points = load_exact_float(source_path)
    initial_result, initial_values, initial_faces, initial_equilibria = state(
        points, args.plane_tol
    )
    if [len(initial_result.active), len(initial_result.edges), len(initial_result.faces)] != [60, 158, 100]:
        raise AssertionError("wrong source lattice")
    if [len(initial_result.stable), len(initial_result.unstable), len(initial_result.saddles)] != [2, 2, 2]:
        raise AssertionError("wrong source class")
    initial_residuals = objective_residual_keys(initial_values)
    initial_primitive_signs = primitive_sign_signature(initial_values)
    if not forced_rails_retained(initial_result):
        raise AssertionError("source does not retain all 37 forced rails")
    initial_clearance_tau = clearance_tau(
        points, initial_result, args.circuit, exact_floor
    )
    initial_topology_determinants = topology_guard_determinants(
        points, args.topology_guard_circuit
    )

    trust = args.trust
    history = []
    first_event = None
    for iteration in range(args.iterations):
        result, values, faces, equilibria = state(points, args.plane_tol)
        modes, best, solve = solve_step(
            points,
            result,
            values,
            trust,
            args.guard_budget,
            args.fd_step,
            args.bound,
            args.plane_tol,
            args.circuit,
            exact_floor,
            args.clearance_linear_buffer,
            args.topology_guard_circuit,
            args.topology_guard_linear_buffer,
        )
        coefficients = np.asarray(best["coefficients"], dtype=float)
        candidate, candidate_state, error = event_at_fraction(
            points, modes, coefficients, 1.0, args.plane_tol
        )
        changed = error is not None
        if candidate_state is not None:
            changed = candidate_state[2] != faces or candidate_state[3] != equilibria
        record = {
            "iteration": iteration,
            "trust": trust,
            "best": {key: value for key, value in best.items() if key != "coefficients"},
            "solver": {key: value for key, value in solve.items() if key != "branches"},
            "event_at_full_step": changed,
            "full_step_error": error,
        }
        if changed:
            record.update({
                "accepted": False,
                "acceptance": {
                    "same_face_and_equilibrium_signature": False,
                },
                "rejection_reasons": ["full-step signature change or invalid endpoint"],
            })
            left, right = 0.0, 1.0
            left_state = (result, values, faces, equilibria)
            for _ in range(70):
                midpoint = (left + right) / 2.0
                _midpoints, mid_state, mid_error = event_at_fraction(
                    points, modes, coefficients, midpoint, args.plane_tol
                )
                same = (
                    mid_error is None
                    and mid_state is not None
                    and mid_state[2] == faces
                    and mid_state[3] == equilibria
                )
                if same:
                    left = midpoint
                    left_state = mid_state
                else:
                    right = midpoint
                if right - left < 1e-12:
                    break
            before_points, before_state, before_error = event_at_fraction(
                points, modes, coefficients, left, args.plane_tol
            )
            after_points, after_state, after_error = event_at_fraction(
                points, modes, coefficients, right, args.plane_tol
            )
            before_file = HERE / f"{args.prefix}_event_before.csv"
            after_file = HERE / f"{args.prefix}_event_after.csv"
            write_csv(before_file, before_points)
            write_csv(after_file, after_points)
            before_faces = before_state[2] if before_state is not None else faces
            after_faces = after_state[2] if after_state is not None else ()
            circuits = candidate_circuits(
                {frozenset(face) for face in before_faces},
                {frozenset(face) for face in after_faces},
            ) if after_faces else []
            first_event = {
                "iteration": iteration,
                "fraction_bracket": [left, right],
                "coordinate_displacement_bracket": [
                    left * best["physical_linf"], right * best["physical_linf"]
                ],
                "candidate_circuits": [list(circuit) for circuit in circuits],
                "before_file": before_file.name,
                "after_file": after_file.name,
                "before_error": before_error,
                "after_error": after_error,
                "before_f_vector": (
                    [len(before_state[0].active), len(before_state[0].edges), len(before_state[0].faces)]
                    if before_state is not None else None
                ),
                "after_f_vector": (
                    [len(after_state[0].active), len(after_state[0].edges), len(after_state[0].faces)]
                    if after_state is not None else None
                ),
                "before_class": (
                    [len(before_state[0].stable), len(before_state[0].unstable), len(before_state[0].saddles)]
                    if before_state is not None else None
                ),
                "after_class": (
                    [len(after_state[0].stable), len(after_state[0].unstable), len(after_state[0].saddles)]
                    if after_state is not None else None
                ),
                "removed_faces": [
                    list(face) for face in sorted(set(before_faces) - set(after_faces))
                ] if after_faces else [],
                "added_faces": [
                    list(face) for face in sorted(set(after_faces) - set(before_faces))
                ] if after_faces else [],
            }
            record["first_event"] = first_event
            history.append(record)
            break

        candidate_result, candidate_values, candidate_faces, candidate_equilibria = candidate_state
        if candidate_faces != initial_faces or candidate_equilibria != initial_equilibria:
            raise AssertionError("undetected signature change")
        candidate_residuals = objective_residual_keys(candidate_values)
        if candidate_residuals != initial_residuals:
            raise AssertionError("objective residual keys changed")
        ratios = {
            name: float(candidate_values[key] / values[key])
            for name, key in initial_residuals.items()
        }
        candidate_clearance_tau = clearance_tau(
            candidate, candidate_result, args.circuit, exact_floor
        )
        candidate_topology_determinants = topology_guard_determinants(
            candidate, args.topology_guard_circuit
        )
        candidate_topology_ratios = {
            circuit: (
                (1.0 if initial_topology_determinants[circuit] > 0 else -1.0)
                * value
                / abs(initial_topology_determinants[circuit])
            )
            for circuit, value in candidate_topology_determinants.items()
        }
        same_face_signature = candidate_faces == faces
        same_equilibrium_signature = candidate_equilibria == equilibria
        same_active_labels = set(candidate_result.active) == set(result.active)
        same_primitive_cell = (
            primitive_sign_signature(candidate_values) == initial_primitive_signs
        )
        rails_retained = forced_rails_retained(candidate_result)
        residuals_improved = all(
            0.0 < value < 1.0 for value in ratios.values()
        )
        clearance_strict = all(
            value > 1.0 for value in candidate_clearance_tau.values()
        )
        clearance_strictly_inward = all(
            candidate_clearance_tau[label] > initial_clearance_tau[label]
            for label in initial_clearance_tau
        )
        topology_guards_strictly_inward = all(
            value > 1.0 for value in candidate_topology_ratios.values()
        )
        acceptance = {
            "all_four_residual_ratios_strictly_below_one": residuals_improved,
            "both_actual_clearance_tau_strictly_above_one": clearance_strict,
            "both_actual_clearance_tau_strictly_inward_if_required": (
                clearance_strictly_inward or not args.require_clearance_inward
            ),
            "same_face_signature": same_face_signature,
            "same_equilibrium_signature": same_equilibrium_signature,
            "same_active_labels": same_active_labels,
            "same_primitive_sign_cell": same_primitive_cell,
            "all_37_forced_rails_retained": rails_retained,
            "all_actual_topology_guard_ratios_strictly_above_one": (
                topology_guards_strictly_inward
            ),
        }
        accepted = all(acceptance.values())
        record.update({
            "accepted": accepted,
            "acceptance": acceptance,
            "ratios": ratios,
            "clearance_tau": {
                str(label): value
                for label, value in candidate_clearance_tau.items()
            },
            "clearance_tau_over_source": {
                str(label): candidate_clearance_tau[label] / initial_clearance_tau[label]
                for label in initial_clearance_tau
            },
            "topology_guard_determinants": {
                ",".join(str(label) for label in circuit): value
                for circuit, value in candidate_topology_determinants.items()
            },
            "topology_guard_ratios": {
                ",".join(str(label) for label in circuit): value
                for circuit, value in candidate_topology_ratios.items()
            },
        })
        if not accepted:
            record["rejection_reasons"] = [
                name for name, passed in acceptance.items() if not passed
            ]
            history.append(record)
            continue
        points = candidate
        endpoint_path = HERE / f"{args.prefix}_step_{iteration + 1:03d}.csv"
        write_csv(endpoint_path, points)
        record.update({
            "endpoint_file": endpoint_path.name,
            "endpoint_f_vector": [
                len(candidate_result.active), len(candidate_result.edges), len(candidate_result.faces)
            ],
            "endpoint_class": [
                len(candidate_result.stable), len(candidate_result.unstable), len(candidate_result.saddles)
            ],
            "endpoint_topology_margin": float(candidate_result.topology_margin),
        })
        history.append(record)
        trust = min(trust * 1.5, args.trust_maximum)

    final_result, final_values, _final_faces, _final_equilibria = state(
        points, args.plane_tol
    )
    final_clearance_tau = clearance_tau(
        points, final_result, args.circuit, exact_floor
    )
    final_topology_determinants = topology_guard_determinants(
        points, args.topology_guard_circuit
    )
    final_topology_ratios = {
        circuit: (
            (1.0 if initial_topology_determinants[circuit] > 0 else -1.0)
            * value
            / abs(initial_topology_determinants[circuit])
        )
        for circuit, value in final_topology_determinants.items()
    }
    final_file = HERE / f"{args.prefix}_final.csv"
    write_csv(final_file, points)
    accepted_steps = sum(bool(row.get("accepted")) for row in history)
    parameters = vars(args).copy()
    parameters["circuit"] = list(args.circuit)
    parameters["topology_guard_circuit"] = [
        list(circuit) for circuit in args.topology_guard_circuit
    ]
    payload = {
        "version": 2,
        "scope": "fail-closed one-step cycle-11 actual-cell proposal",
        "source": str(source_path),
        "parameters": parameters,
        "clearance_floor_contract": clearance_contract,
        "initial": {
            "f_vector": [len(initial_result.active), len(initial_result.edges), len(initial_result.faces)],
            "class": [len(initial_result.stable), len(initial_result.unstable), len(initial_result.saddles)],
            "topology_margin": float(initial_result.topology_margin),
            "objective_residuals": {
                name: float(initial_values[key])
                for name, key in initial_residuals.items()
            },
            "clearance_tau": {
                str(label): value
                for label, value in initial_clearance_tau.items()
            },
            "topology_guard_determinants": {
                ",".join(str(label) for label in circuit): value
                for circuit, value in initial_topology_determinants.items()
            },
            "all_37_forced_rails_retained": True,
        },
        "history": history,
        "first_event": first_event,
        "final": {
            "file": final_file.name,
            "f_vector": [len(final_result.active), len(final_result.edges), len(final_result.faces)],
            "class": [len(final_result.stable), len(final_result.unstable), len(final_result.saddles)],
            "topology_margin": float(final_result.topology_margin),
            "objective_residuals": {
                name: float(final_values[key])
                for name, key in initial_residuals.items()
            },
            "clearance_tau": {
                str(label): value
                for label, value in final_clearance_tau.items()
            },
            "clearance_tau_over_source": {
                str(label): final_clearance_tau[label] / initial_clearance_tau[label]
                for label in initial_clearance_tau
            },
            "topology_guard_determinants": {
                ",".join(str(label) for label in circuit): value
                for circuit, value in final_topology_determinants.items()
            },
            "topology_guard_ratios": {
                ",".join(str(label) for label in circuit): value
                for circuit, value in final_topology_ratios.items()
            },
            "all_37_forced_rails_retained": forced_rails_retained(final_result),
        },
        "conclusion": (
            "required one-step cycle-11 proposal accepted"
            if accepted_steps == 1
            else "required one-step cycle-11 proposal rejected"
        ),
    }
    output = HERE / f"{args.prefix}_slp.json"
    output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "accepted_steps": accepted_steps,
        "required_step_accepted": accepted_steps == 1,
        "first_event": first_event,
        "final": payload["final"],
        "output": str(output),
    }, indent=2))
    if args.require_accepted_step and accepted_steps != 1:
        print("required cycle-11 step was not accepted", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
