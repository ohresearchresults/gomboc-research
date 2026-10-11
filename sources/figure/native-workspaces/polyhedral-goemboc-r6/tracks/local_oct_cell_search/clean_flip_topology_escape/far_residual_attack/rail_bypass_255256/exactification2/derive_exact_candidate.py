#!/usr/bin/env python3
"""Deterministically exactify the saved 165-control numerical candidate.

The numerical proposer works in a 165-dimensional affine chart.  This script
reconstructs its physical velocity, rationalizes it once, and projects every
enlarged-base velocity into the exact source base plane.  The output is only a
path definition; all geometric claims are proved by the builder and the
independent verifier.
"""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np


sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
RAIL = HERE.parent
PARENT = RAIL.parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(PARENT))

import attack_common as common  # noqa: E402


SOURCE = PARENT / "exact_event_source.csv"
FACES = PARENT / "exact_event_source_faces.json"
REJECTED_CERTIFICATE = PARENT / "exact_event_certificate.json"
REJECTED_PATH = PARENT / "exact_event_path.json"
PROPOSAL = RAIL / "full_control_search.json"
CANDIDATE = RAIL / "full_control_candidate_float.csv"
OUTPUT = HERE / "exact_candidate_path.json"

BASE = frozenset(range(17)) | {54}
ROUND_DIGITS = 14


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def qs(value: Q) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def read_exact_csv(path: Path):
    rows = {}
    with path.open() as stream:
        for row in csv.DictReader(stream):
            rows[int(row["source_id"])] = tuple(Q(row[key]) for key in ("x", "y", "z"))
    return rows


def read_float_csv(path: Path):
    rows = {}
    with path.open() as stream:
        for row in csv.DictReader(stream):
            rows[int(row["source_id"])] = np.asarray(
                [float(row[key]) for key in ("x", "y", "z")], dtype=float
            )
    return rows


def add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def sub(left, right):
    return tuple(a - b for a, b in zip(left, right))


def mul(vector, scalar):
    return tuple(scalar * value for value in vector)


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def cross(left, right):
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def rationalize(value: float) -> Q:
    return Q(format(float(value), f".{ROUND_DIGITS}g"))


def main() -> None:
    proposal = json.loads(PROPOSAL.read_text())
    rejected = json.loads(REJECTED_CERTIFICATE.read_text())
    faces = json.loads(FACES.read_text())
    source = read_exact_csv(SOURCE)
    candidate = read_float_csv(CANDIDATE)
    ids = sorted(source)

    if proposal["verdict"] != "FULL_CONTROL_RAIL_SEPARATING_PRIMAL_WITNESS_FOUND":
        raise AssertionError(proposal["verdict"])
    if proposal["source_sha256"] != sha256(SOURCE):
        raise AssertionError("proposal/source hash mismatch")
    if proposal["faces_sha256"] != sha256(FACES):
        raise AssertionError("proposal/faces hash mismatch")
    if proposal["endpoint_sha256"] != sha256(CANDIDATE):
        raise AssertionError("proposal/candidate hash mismatch")
    if rejected["event"]["circuit"] != [69, 224, 255, 256]:
        raise AssertionError("rejected circuit drift")
    if rejected["obstruction"]["forced_rail_lost_at_wall"] != [255, 256]:
        raise AssertionError("rejected rail drift")
    if len(ids) != 61 or set(candidate) != set(ids):
        raise AssertionError("active row mismatch")
    if sorted(len(face) for face in faces).count(18) != 1:
        raise AssertionError("enlarged base face missing or duplicated")
    nontriangles = [frozenset(face) for face in faces if len(face) != 3]
    if nontriangles != [BASE]:
        raise AssertionError(("unexpected planarity invariants", nontriangles))

    selected = proposal["selected"]
    if not selected.get("linear_primal_valid") or not selected.get("actual_valid"):
        raise AssertionError("saved selected scenario was not numerically validated")
    coefficients = np.asarray(selected["direction"], dtype=float)
    source_float = np.asarray(
        [[float(value) for value in source[label]] for label in ids], dtype=float
    )
    controls, chart_scale = common.full_controls(ids, source_float)
    if len(coefficients) != len(controls) or len(controls) != proposal["control_count"]:
        raise AssertionError("chart dimension drift")

    index = {label: offset for offset, label in enumerate(ids)}
    physical_float = np.zeros_like(source_float)
    for coefficient, control in zip(coefficients, controls):
        physical_float[index[control.vertex]] += coefficient * np.asarray(
            control.vector, dtype=float
        )
    reconstructed_float_endpoint = source_float + physical_float
    candidate_array = np.asarray([candidate[label] for label in ids], dtype=float)
    proposer_endpoint_error = float(
        np.max(np.abs(reconstructed_float_endpoint - candidate_array))
    )
    if proposer_endpoint_error > 2e-12:
        raise AssertionError(("candidate reconstruction drift", proposer_endpoint_error))

    e1 = sub(source[1], source[0])
    e2 = sub(source[2], source[0])
    exact_basis_float = np.asarray(
        [[float(value) for value in e1], [float(value) for value in e2]], dtype=float
    ).T
    velocity = {}
    base_coefficients = {}
    nonbase_velocity = {}
    for label in ids:
        displacement = physical_float[index[label]]
        if label in BASE:
            fitted, *_ = np.linalg.lstsq(exact_basis_float, displacement, rcond=None)
            a = rationalize(fitted[0])
            b = rationalize(fitted[1])
            base_coefficients[str(label)] = [qs(a), qs(b)]
            velocity[label] = add(mul(e1, a), mul(e2, b))
        else:
            xyz = tuple(rationalize(value) for value in displacement)
            nonbase_velocity[str(label)] = [qs(value) for value in xyz]
            velocity[label] = xyz

    common_velocity, common_scale = common.exact_velocity_from_coefficients(
        source, ids, coefficients
    )
    if velocity != common_velocity or chart_scale != common_scale:
        raise AssertionError("independent candidate projection disagrees with shared chart")

    normal = cross(e1, e2)
    source_planarity = {
        str(label): qs(dot(normal, sub(source[label], source[0])))
        for label in sorted(BASE)
    }
    velocity_planarity = {
        str(label): qs(dot(normal, velocity[label])) for label in sorted(BASE)
    }
    if any(Q(value) for value in source_planarity.values()):
        raise AssertionError("source enlarged base is not exactly planar")
    if any(Q(value) for value in velocity_planarity.values()):
        raise AssertionError("projected enlarged-base velocity is not exactly planar")

    exact_endpoint_float = np.asarray(
        [
            [float(source[label][axis] + velocity[label][axis]) for axis in range(3)]
            for label in ids
        ],
        dtype=float,
    )
    exactification_error = float(np.max(np.abs(exact_endpoint_float - candidate_array)))
    if exactification_error > 5e-12:
        raise AssertionError(("exactified witness left candidate", exactification_error))

    velocity_packet = {
        str(label): [qs(value) for value in velocity[label]] for label in ids
    }
    payload = {
        "version": 1,
        "type": "exact rational projection of saved 165-control primal candidate",
        "method": (
            "Reconstruct the selected chart displacement; round physical non-base "
            "velocities to 14 significant decimal digits; round two exact-base-plane "
            "coordinates for every enlarged-base row; then rebuild those velocities "
            "as exact rational combinations of source rows 1-0 and 2-0."
        ),
        "source_sha256": sha256(SOURCE),
        "faces_sha256": sha256(FACES),
        "rejected_event_certificate_sha256": sha256(REJECTED_CERTIFICATE),
        "rejected_event_path_sha256": sha256(REJECTED_PATH),
        "proposal_sha256": sha256(PROPOSAL),
        "candidate_sha256": sha256(CANDIDATE),
        "selected_scenario_index": selected["index"],
        "control_count": len(controls),
        "round_significant_digits": ROUND_DIGITS,
        "chart_scale_diagnostic": chart_scale,
        "proposer_endpoint_max_abs_error": proposer_endpoint_error,
        "exactification_endpoint_max_abs_error": exactification_error,
        "direction_l2_diagnostic": selected["direction_l2"],
        "candidate_circuit_slopes_diagnostic": selected["circuit_slopes"],
        "base_face": sorted(BASE),
        "base_plane_basis": {
            "e1_row1_minus_row0": [qs(value) for value in e1],
            "e2_row2_minus_row0": [qs(value) for value in e2],
        },
        "base_plane_coefficients": base_coefficients,
        "nonbase_physical_velocity": nonbase_velocity,
        "source_base_planarity_determinants": source_planarity,
        "velocity_base_planarity_determinants": velocity_planarity,
        "velocity": velocity_packet,
        "velocity_digest": canonical_hash(velocity_packet),
        "parameter_semantics": "point(t) = exact_source + t * exact_velocity",
        "certified_step_parameter": "1/4",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print("EXACT_165_CONTROL_CANDIDATE_PROJECTION_PASS")
    print("velocity_digest", payload["velocity_digest"])
    print("proposer_endpoint_max_abs_error", proposer_endpoint_error)
    print("exactification_endpoint_max_abs_error", exactification_error)
    print("path_sha256", sha256(OUTPUT))


if __name__ == "__main__":
    main()
