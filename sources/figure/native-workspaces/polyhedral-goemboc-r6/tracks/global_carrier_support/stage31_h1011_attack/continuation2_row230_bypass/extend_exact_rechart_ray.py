#!/usr/bin/env python3
"""Materialize an exact bounded continuation of a certified rechart ray."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ATTACK = HERE.parent
TRACK = ATTACK.parent
sys.path.insert(0, str(TRACK / "rigorous_local_bypass"))
import exact_core as ex  # noqa: E402
import certify_fixed_cell_step as fixed  # noqa: E402


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve(value):
    path = Path(value)
    return path if path.is_absolute() else HERE / path


def write_rows(path, points):
    with path.open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(("source_id", "x", "y", "z"))
        for label in sorted(points):
            writer.writerow((label, *(ex.qs(value) for value in points[label])))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--unit-source", required=True)
    parser.add_argument("--unit-endpoint", required=True)
    parser.add_argument("--faces", required=True)
    parser.add_argument("--parent-proposal", required=True)
    parser.add_argument("--parent-scan", required=True)
    parser.add_argument(
        "--expected-parent-verdict",
        default="ROW230_FULL_CONTROL_RATIONAL_RECHART_PROPOSAL_PASS",
    )
    parser.add_argument("--extension", required=True)
    parser.add_argument("--endpoint", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument(
        "--verdict", default="ROW230_EXACT_RECHART_RAY_EXTENSION_PROPOSAL_PASS"
    )
    args = parser.parse_args()

    unit_source_path = resolve(args.unit_source)
    unit_endpoint_path = resolve(args.unit_endpoint)
    faces_path = resolve(args.faces)
    parent_proposal_path = resolve(args.parent_proposal)
    parent_scan_path = resolve(args.parent_scan)
    endpoint_path = resolve(args.endpoint)
    output_path = resolve(args.output)
    extension = Q(args.extension)
    if extension <= 0:
        raise ValueError("extension must be positive")

    parent_proposal = json.loads(parent_proposal_path.read_text())
    parent_scan = json.loads(parent_scan_path.read_text())
    if parent_proposal["verdict"] != args.expected_parent_verdict:
        raise AssertionError("unexpected parent proposal")
    if parent_scan["verdict"] != "EXHAUSTIVE_EXACT_FIRST_EVENT_LOCATOR_PASS":
        raise AssertionError("unexpected parent event scan")
    total_parameter = Q(1) + extension
    first_event_lower = Q(parent_scan["first_candidate"]["lo"])
    if first_event_lower <= total_parameter:
        raise AssertionError(("extension reaches the first exact event", total_parameter))

    unit_source = ex.read_rows(unit_source_path)
    unit_endpoint = ex.read_rows(unit_endpoint_path)
    if set(unit_source) != set(unit_endpoint):
        raise AssertionError("unit ray labels differ")
    endpoint = {
        label: tuple(
            unit_endpoint[label][axis]
            + extension * (unit_endpoint[label][axis] - unit_source[label][axis])
            for axis in range(3)
        )
        for label in unit_source
    }
    faces = json.loads(faces_path.read_text())
    checkpoint = fixed.checkpoint(endpoint, faces)
    write_rows(endpoint_path, endpoint)
    payload = {
        "version": 1,
        "verdict": args.verdict,
        "scope": (
            "Exact rational continuation of one already located full-support rechart "
            "ray, bounded strictly before its first exhaustive primitive event."
        ),
        "source_hashes": {
            path.name: sha256(path)
            for path in (
                unit_source_path,
                unit_endpoint_path,
                faces_path,
                parent_proposal_path,
                parent_scan_path,
            )
        },
        "ray": {
            "unit_source": unit_source_path.name,
            "unit_endpoint": unit_endpoint_path.name,
            "extension_from_unit_endpoint": ex.qs(extension),
            "total_parameter_from_unit_source": ex.qs(total_parameter),
            "first_event_lower_bound_from_unit_source": ex.qs(first_event_lower),
            "strictly_before_first_event": True,
        },
        "candidate": {
            "file": endpoint_path.name,
            "csv_sha256": sha256(endpoint_path),
            "checkpoint": checkpoint,
        },
    }
    output_path.write_text(json.dumps(payload, indent=2) + "\n")
    print(payload["verdict"])
    print("total_parameter", payload["ray"]["total_parameter_from_unit_source"])
    print("first_event_lower_bound", payload["ray"]["first_event_lower_bound_from_unit_source"])
    print("endpoint_sha256", payload["candidate"]["csv_sha256"])


if __name__ == "__main__":
    main()
