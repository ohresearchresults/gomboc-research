#!/usr/bin/env python3
"""Propose a denominator-bounded post-transfer ROW230 continuation.

The accepted transfer FAR is at ray parameter 1/32.  This proposer advances
to the still pre-event parameter 1/16, snaps all coordinates to one rational
lattice, and reconstructs the only non-triangular carrier (the enlarged base)
exactly.  It is only a proposer: a complete 7,904-primitive path certificate
and an independent verifier remain mandatory.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
ATTACK = PARENT.parent
ROOT = HERE.parents[4]

sys.path.insert(0, str(PARENT))
import certify_fixed_cell_step as fixed  # noqa: E402


ex = fixed.ex
BASE = frozenset(range(17)) | {54}
ANCHORS = (0, 5, 11)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def resolve(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else HERE / path


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


def nearest_lattice(value: Q, denominator: int) -> Q:
    scaled = value.numerator * denominator
    sign = -1 if scaled < 0 else 1
    quotient, remainder = divmod(abs(scaled), value.denominator)
    if 2 * remainder >= value.denominator:
        quotient += 1
    return Q(sign * quotient, denominator)


def cross(left, right):
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def sub(left, right):
    return tuple(left[i] - right[i] for i in range(3))


def dot(left, right):
    return sum(left[i] * right[i] for i in range(3))


def add(left, right):
    return tuple(left[i] + right[i] for i in range(3))


def scale(value: Q, vector):
    return tuple(value * vector[i] for i in range(3))


def determinant(first, second, third):
    return dot(first, cross(second, third))


def plane_alignment(source, target):
    """Return one global rational affine map sending source anchors to target."""
    source_anchor = source[ANCHORS[0]]
    source_u = sub(source[ANCHORS[1]], source_anchor)
    source_v = sub(source[ANCHORS[2]], source_anchor)
    source_w = cross(source_u, source_v)
    target_anchor = target[ANCHORS[0]]
    target_u = sub(target[ANCHORS[1]], target_anchor)
    target_v = sub(target[ANCHORS[2]], target_anchor)
    target_w = cross(target_u, target_v)
    frame_determinant = determinant(source_u, source_v, source_w)
    if frame_determinant == 0:
        raise AssertionError("source alignment frame is singular")

    def linear(vector):
        coefficients = (
            determinant(vector, source_v, source_w) / frame_determinant,
            determinant(source_u, vector, source_w) / frame_determinant,
            determinant(source_u, source_v, vector) / frame_determinant,
        )
        return add(
            add(scale(coefficients[0], target_u), scale(coefficients[1], target_v)),
            scale(coefficients[2], target_w),
        )

    translation = sub(target_anchor, linear(source_anchor))
    aligned = {
        label: add(linear(point), translation)
        for label, point in source.items()
    }
    for label in ANCHORS:
        if aligned[label] != target[label]:
            raise AssertionError(("alignment anchor mismatch", label))
    return aligned, {
        "source_frame_determinant": ex.qs(frame_determinant),
        "source_u": [ex.qs(value) for value in source_u],
        "source_v": [ex.qs(value) for value in source_v],
        "source_w": [ex.qs(value) for value in source_w],
        "target_u": [ex.qs(value) for value in target_u],
        "target_v": [ex.qs(value) for value in target_v],
        "target_w": [ex.qs(value) for value in target_w],
        "translation": [ex.qs(value) for value in translation],
    }


def point_on_ray(source, endpoint, parameter: Q):
    if set(source) != set(endpoint):
        raise AssertionError("ray endpoints have different labels")
    return {
        label: tuple(
            source[label][axis]
            + parameter * (endpoint[label][axis] - source[label][axis])
            for axis in range(3)
        )
        for label in source
    }


def quantize_with_exact_base(target, denominator: int):
    candidate = {
        label: tuple(nearest_lattice(value, denominator) for value in xyz)
        for label, xyz in target.items()
    }

    a, b, c = (candidate[label] for label in ANCHORS)
    normal = cross(sub(b, a), sub(c, a))
    if normal == (Q(0), Q(0), Q(0)):
        raise AssertionError("rounded base anchors are collinear")
    solve_axis = max(range(3), key=lambda axis: abs(normal[axis]))
    if normal[solve_axis] == 0:
        raise AssertionError("base projection has zero solve coefficient")

    for label in sorted(BASE - frozenset(ANCHORS)):
        xyz = list(candidate[label])
        rhs = dot(normal, a) - sum(
            normal[axis] * xyz[axis]
            for axis in range(3)
            if axis != solve_axis
        )
        xyz[solve_axis] = rhs / normal[solve_axis]
        candidate[label] = tuple(xyz)

    for label in BASE:
        if dot(normal, sub(candidate[label], a)) != 0:
            raise AssertionError(("base projection failed", label))
    return candidate, normal, solve_axis


def write_rows(path: Path, rows) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(("source_id", "x", "y", "z"))
        for label in sorted(rows):
            writer.writerow((label, *(ex.qs(value) for value in rows[label])))


def size_receipt(rows):
    numerator_digits = 0
    denominator_digits = 0
    numerator_bits = 0
    denominator_bits = 0
    for xyz in rows.values():
        for value in xyz:
            numerator_digits = max(numerator_digits, len(str(abs(value.numerator))))
            denominator_digits = max(denominator_digits, len(str(value.denominator)))
            numerator_bits = max(numerator_bits, abs(value.numerator).bit_length())
            denominator_bits = max(denominator_bits, value.denominator.bit_length())
    return {
        "maximum_numerator_decimal_digits": numerator_digits,
        "maximum_denominator_decimal_digits": denominator_digits,
        "maximum_numerator_bits": numerator_bits,
        "maximum_denominator_bits": denominator_bits,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ray-source", default=str(PARENT / "step22_transfer_far.csv"))
    parser.add_argument("--ray-endpoint", default=str(PARENT / "step23_strict_candidate.csv"))
    parser.add_argument("--accepted-source", default=str(PARENT / "step23_transfer_far.csv"))
    parser.add_argument("--faces", default=str(ATTACK / "continuation/main/exact_full_control_chain_post_faces.json"))
    parser.add_argument("--transfer-certificate", default=str(PARENT / "step23_transfer_certificate.json"))
    parser.add_argument("--transfer-verification", default=str(PARENT / "step23_transfer_verification.json"))
    parser.add_argument("--aligned-output", default=str(HERE / "rebase_aligned_source.csv"))
    parser.add_argument("--output", default=str(HERE / "rebase_candidate.csv"))
    parser.add_argument("--proposal", default=str(HERE / "rebase_proposal.json"))
    parser.add_argument("--denominator", type=int, default=10**24)
    parser.add_argument("--accepted-parameter", default="1/32")
    parser.add_argument("--target-parameter", default="1/16")
    args = parser.parse_args()

    ray_source_path = resolve(args.ray_source)
    ray_endpoint_path = resolve(args.ray_endpoint)
    accepted_source_path = resolve(args.accepted_source)
    faces_path = resolve(args.faces)
    transfer_certificate_path = resolve(args.transfer_certificate)
    transfer_verification_path = resolve(args.transfer_verification)
    aligned_output_path = resolve(args.aligned_output)
    output_path = resolve(args.output)
    proposal_path = resolve(args.proposal)
    accepted_parameter = Q(args.accepted_parameter)
    target_parameter = Q(args.target_parameter)
    if args.denominator <= 0:
        raise ValueError("denominator must be positive")
    if not Q(0) < accepted_parameter < target_parameter < Q(1):
        raise ValueError("expected 0 < accepted < target < 1")

    transfer_certificate = json.loads(transfer_certificate_path.read_text())
    transfer_verification = json.loads(transfer_verification_path.read_text())
    if transfer_certificate.get("verdict") != "EXACT_ROW230_BYPASS_ELEVENTH_MECHANICS_TRANSFER_PASS":
        raise AssertionError(transfer_certificate.get("verdict"))
    if transfer_verification.get("verdict") != "INDEPENDENT_EXACT_ROW230_BYPASS_ELEVENTH_MECHANICS_TRANSFER_PASS":
        raise AssertionError(transfer_verification.get("verdict"))
    if transfer_verification.get("certificate_sha256") != sha256(transfer_certificate_path):
        raise AssertionError("transfer certificate hash mismatch")
    if transfer_verification.get("far_sha256") != sha256(accepted_source_path):
        raise AssertionError("accepted FAR hash mismatch")
    if Q(transfer_certificate["path"]["far_parameter"]) != accepted_parameter:
        raise AssertionError("accepted FAR parameter mismatch")

    ray_source = ex.read_rows(ray_source_path)
    ray_endpoint = ex.read_rows(ray_endpoint_path)
    accepted_source = ex.read_rows(accepted_source_path)
    expected_accepted = point_on_ray(ray_source, ray_endpoint, accepted_parameter)
    if accepted_source != expected_accepted:
        raise AssertionError("accepted FAR is not the declared exact ray point")

    target = point_on_ray(ray_source, ray_endpoint, target_parameter)
    candidate, normal, solve_axis = quantize_with_exact_base(
        target, args.denominator
    )
    aligned_source, alignment = plane_alignment(accepted_source, candidate)
    faces = json.loads(faces_path.read_text())
    source_checkpoint = fixed.checkpoint(accepted_source, faces)
    aligned_checkpoint = fixed.checkpoint(aligned_source, faces)
    endpoint_checkpoint = fixed.checkpoint(candidate, faces)
    alignment_path = fixed.affine_path(accepted_source, aligned_source)
    compression_path = fixed.affine_path(aligned_source, candidate)
    segment_receipts = {}
    for name, path in (
        ("plane_alignment", alignment_path),
        ("lattice_compression", compression_path),
    ):
        segment_receipts[name] = {
            "directed_residuals": fixed.residual_audit(path, faces),
            "row230_strict_inward_certificate": fixed.danger_audit(path, faces),
            "h910_nonresurrection": fixed.h910_audit(path, faces),
        }

    max_error = max(
        abs(candidate[label][axis] - target[label][axis])
        for label in target
        for axis in range(3)
    )
    aligned_output_path.parent.mkdir(parents=True, exist_ok=True)
    write_rows(aligned_output_path, aligned_source)
    write_rows(output_path, candidate)

    proposal = {
        "version": 1,
        "type": "source-bound exact common-lattice ROW230 rebase proposal",
        "scope": (
            "A short post-transfer continuation from exact ray parameter 1/32 "
            "toward 1/16, snapped to one finite rational lattice while preserving "
            "the enlarged base plane exactly. This proposal is not a path certificate."
        ),
        "source_hashes": {
            relative(path): sha256(path)
            for path in (
                ray_source_path,
                ray_endpoint_path,
                accepted_source_path,
                faces_path,
                transfer_certificate_path,
                transfer_verification_path,
                Path(__file__).resolve(),
            )
        },
        "ray": {
            "accepted_parameter": ex.qs(accepted_parameter),
            "unrounded_target_parameter": ex.qs(target_parameter),
            "unrounded_target_coordinate_hash": canonical_hash({
                str(label): [ex.qs(value) for value in target[label]]
                for label in sorted(target)
            }),
        },
        "lattice": {
            "requested_denominator": args.denominator,
            "base_labels": sorted(BASE),
            "base_anchors": list(ANCHORS),
            "base_plane_normal": [ex.qs(value) for value in normal],
            "base_projection_solve_axis": solve_axis,
            "maximum_absolute_coordinate_error": ex.qs(max_error),
            "source_coordinate_size": size_receipt(accepted_source),
            "endpoint_coordinate_size": size_receipt(candidate),
        },
        "alignment": alignment,
        "generated_endpoints": {
            "aligned_source": {
                "path": relative(aligned_output_path),
                "sha256": sha256(aligned_output_path),
                "checkpoint": aligned_checkpoint,
                "coordinate_size": size_receipt(aligned_source),
            },
            "compressed_endpoint": {
                "path": relative(output_path),
                "sha256": sha256(output_path),
                "checkpoint": endpoint_checkpoint,
                "coordinate_size": size_receipt(candidate),
            },
        },
        "source_checkpoint": source_checkpoint,
        "segment_receipts": segment_receipts,
        "next_gate": (
            "separate exhaustive exact first-event locators and 7,904-primitive "
            "certificates for both segments, followed by independent reconstruction"
        ),
        "verdict": "ROW230_COMMON_LATTICE_REBASE_PROPOSAL_PASS",
    }
    proposal_path.write_text(json.dumps(proposal, indent=2) + "\n")
    print(json.dumps({
        "verdict": proposal["verdict"],
        "endpoint": str(output_path),
        "aligned_source_sha256": proposal["generated_endpoints"]["aligned_source"]["sha256"],
        "endpoint_sha256": proposal["generated_endpoints"]["compressed_endpoint"]["sha256"],
        "maximum_absolute_coordinate_error": float(max_error),
        "source_coordinate_size": proposal["lattice"]["source_coordinate_size"],
        "endpoint_coordinate_size": proposal["lattice"]["endpoint_coordinate_size"],
        "residual_ratios": {
            segment: {
                name: float(Q(row["endpoint"]["squared_value"]) / Q(row["source"]["squared_value"]))
                for name, row in receipt["directed_residuals"].items()
            }
            for segment, receipt in segment_receipts.items()
        },
    }, indent=2))


if __name__ == "__main__":
    main()
