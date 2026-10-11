#!/usr/bin/env python3
"""Independently verify the exact cycle-20 topology-guard receipt."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from fractions import Fraction
from pathlib import Path


CERTIFICATE_SCHEMA = "polyhedral-goemboc.cycle20-topology-guard-certificate"
CERTIFICATE_VERDICT = "EXACT_CYCLE20_CLUSTER_TOPOLOGY_GUARDS_PASS"
VERIFICATION_SCHEMA = "polyhedral-goemboc.cycle20-topology-guard-verification"
VERIFICATION_VERDICT = "INDEPENDENT_EXACT_CYCLE20_CLUSTER_TOPOLOGY_GUARDS_PASS"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def circuit_arg(text: str):
    values = tuple(int(part) for part in text.split(","))
    if len(values) != 4 or len(frozenset(values)) != 4:
        raise argparse.ArgumentTypeError("expected four distinct circuit labels")
    return values


def load_fraction_csv(path: Path):
    result = {}
    with path.open(newline="") as stream:
        rows = csv.reader(stream)
        try:
            header = next(rows)
        except StopIteration as error:
            raise AssertionError("empty coordinate file") from error
        if header != ["source_id", "x", "y", "z"]:
            raise AssertionError("coordinate header mismatch")
        for row in rows:
            if len(row) != 4:
                raise AssertionError("coordinate row width mismatch")
            label = int(row[0])
            if label in result:
                raise AssertionError("duplicate coordinate label")
            result[label] = tuple(Fraction(value) for value in row[1:])
    if not result:
        raise AssertionError("no coordinates")
    return result


def vec_sub(a, b):
    return tuple(a[index] - b[index] for index in range(3))


def triple_product(points, labels):
    try:
        a, b, c, d = (points[label] for label in labels)
    except KeyError as error:
        raise AssertionError(("missing circuit label", error.args[0])) from error
    u, v, w = vec_sub(b, a), vec_sub(c, a), vec_sub(d, a)
    cross_uv = (
        u[1] * v[2] - u[2] * v[1],
        u[2] * v[0] - u[0] * v[2],
        u[0] * v[1] - u[1] * v[0],
    )
    value = sum(cross_uv[index] * w[index] for index in range(3))
    if value == 0:
        raise AssertionError(("zero circuit determinant", labels))
    return value


def bound_files(certificate, expected_paths):
    ledger = certificate.get("source_hashes")
    if not isinstance(ledger, dict) or set(ledger) != {str(path) for path in expected_paths}:
        raise AssertionError("certificate file-binding key set mismatch")
    for path in expected_paths:
        if ledger[str(path)] != digest(path):
            raise AssertionError(("certificate file hash mismatch", str(path)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--endpoint", required=True)
    parser.add_argument("--audit", required=True)
    parser.add_argument("--slp", required=True)
    parser.add_argument("--chain", required=True)
    parser.add_argument("--certificate", required=True)
    parser.add_argument("--topology-circuit", type=circuit_arg, action="append", required=True)
    parser.add_argument("--clearance-circuit", type=circuit_arg, required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    source, endpoint, audit_path, slp_path, chain_path, certificate_path = (
        Path(value).resolve()
        for value in (
            args.source,
            args.endpoint,
            args.audit,
            args.slp,
            args.chain,
            args.certificate,
        )
    )
    topology_circuits = tuple(args.topology_circuit)
    if len(topology_circuits) != 4 or len(set(topology_circuits)) != 4:
        raise AssertionError("verification requires four unique topology circuits")

    certificate = json.loads(certificate_path.read_text())
    expected_top_keys = {
        "schema", "version", "scope", "source_hashes", "selection_contract",
        "topology_guards", "clearance_floor_endpoint_tau_exact",
        "all_four_topology_determinants_strictly_inward",
        "clearance_floor_strict_at_exact_endpoint", "verdict",
    }
    if set(certificate) != expected_top_keys:
        raise AssertionError("certificate top-level schema mismatch")
    if (
        certificate["schema"] != CERTIFICATE_SCHEMA
        or certificate["version"] != 1
        or certificate["verdict"] != CERTIFICATE_VERDICT
    ):
        raise AssertionError("certificate envelope mismatch")
    bound_files(certificate, (source, endpoint, audit_path, slp_path, chain_path))

    audit = json.loads(audit_path.read_text())
    if (
        audit.get("schema") != "polyhedral-goemboc.topology-guard-audit"
        or audit.get("version") != 1
        or audit.get("verdict") != "READ_ONLY_NEAR_TOPOLOGY_CIRCUIT_AUDIT_PASS"
        or audit.get("source_sha256") != digest(source)
    ):
        raise AssertionError("audit envelope mismatch")
    rows = audit.get("circuits")
    if not isinstance(rows, list) or len(rows) < 6:
        raise AssertionError("audit prefix missing")
    first_five = {tuple(row["circuit"]) for row in rows[:5]}
    if first_five != set(topology_circuits) | {args.clearance_circuit}:
        raise AssertionError("certificate does not cover the first five audit circuits")
    fifth = float(rows[4]["minimum_normalized_support_slack"])
    sixth = float(rows[5]["minimum_normalized_support_slack"])
    if not 0 < 2 * fifth < sixth:
        raise AssertionError("audit factor-two cluster gap is absent")

    slp = json.loads(slp_path.read_text())
    parameters = slp.get("parameters", {})
    if (
        slp.get("version") != 2
        or slp.get("first_event") is not None
        or tuple(map(tuple, parameters.get("topology_guard_circuit", ())))
        != topology_circuits
        or len(slp.get("history", ())) != 1
        or slp["history"][0].get("accepted") is not True
    ):
        raise AssertionError("numerical guard proposal contract mismatch")

    chain = json.loads(chain_path.read_text())
    if (
        chain.get("version") != 2
        or chain.get("verdict") != "EXACT_POST_BYPASS_MATERIAL_CHAIN_PASS"
        or tuple(chain.get("circuit", ())) != args.clearance_circuit
    ):
        raise AssertionError("exact chain contract mismatch")
    generated = chain.get("generated_sha256", {})
    source_hashes = [value for key, value in generated.items() if key.endswith("checkpoint_000.csv")]
    endpoint_hashes = [value for key, value in generated.items() if key.endswith("checkpoint_001.csv")]
    if source_hashes != [digest(source)] or endpoint_hashes != [digest(endpoint)]:
        raise AssertionError("exact chain checkpoint binding mismatch")
    tau_packet = chain.get("clearance_floor_guard", {}).get("chain_endpoint_tau_ratios")
    expected_tau = {
        label: Fraction(packet["tau_ratio_exact"])
        for label, packet in tau_packet.items()
    }
    if set(expected_tau) != {str(args.clearance_circuit[0]), str(args.clearance_circuit[1])}:
        raise AssertionError("clearance endpoint labels mismatch")
    if any(value <= 1 for value in expected_tau.values()):
        raise AssertionError("clearance floor is not exact-strict")

    source_points = load_fraction_csv(source)
    endpoint_points = load_fraction_csv(endpoint)
    expected_rows = []
    for circuit in topology_circuits:
        source_value = triple_product(source_points, circuit)
        endpoint_value = triple_product(endpoint_points, circuit)
        sign = 1 if source_value > 0 else -1
        if sign * endpoint_value <= 0:
            raise AssertionError(("topology sign changed", circuit))
        ratio = sign * endpoint_value / abs(source_value)
        if ratio <= 1:
            raise AssertionError(("topology guard is not exact-inward", circuit, ratio))
        expected_rows.append({
            "circuit": list(circuit),
            "source_determinant_exact": str(source_value),
            "endpoint_determinant_exact": str(endpoint_value),
            "signed_endpoint_over_source_exact": str(ratio),
            "signed_endpoint_over_source_decimal": float(ratio),
            "strictly_inward": True,
        })
    if certificate["topology_guards"] != expected_rows:
        raise AssertionError("certificate exact topology ledger mismatch")
    if certificate["clearance_floor_endpoint_tau_exact"] != {
        label: str(value) for label, value in expected_tau.items()
    }:
        raise AssertionError("certificate exact clearance ledger mismatch")
    selection = certificate["selection_contract"]
    if selection != {
        "audit_prefix_length": 5,
        "factor_two_gap_after_prefix": True,
        "fifth_slack_decimal": fifth,
        "sixth_slack_decimal": sixth,
        "clearance_circuit": list(args.clearance_circuit),
        "topology_circuits": [list(circuit) for circuit in topology_circuits],
    }:
        raise AssertionError("certificate selection contract mismatch")
    if (
        certificate["all_four_topology_determinants_strictly_inward"] is not True
        or certificate["clearance_floor_strict_at_exact_endpoint"] is not True
    ):
        raise AssertionError("certificate conclusion flags mismatch")

    output = Path(args.output).resolve()
    receipt = {
        "schema": VERIFICATION_SCHEMA,
        "version": 1,
        "certificate": str(certificate_path),
        "certificate_sha256": digest(certificate_path),
        "source_sha256": digest(source),
        "endpoint_sha256": digest(endpoint),
        "recomputed_topology_ratios_exact": {
            ",".join(map(str, row["circuit"])): row["signed_endpoint_over_source_exact"]
            for row in expected_rows
        },
        "recomputed_clearance_tau_exact": {
            label: str(value) for label, value in expected_tau.items()
        },
        "verdict": VERIFICATION_VERDICT,
    }
    output.write_text(json.dumps(receipt, indent=2) + "\n")
    print(VERIFICATION_VERDICT)


if __name__ == "__main__":
    main()
