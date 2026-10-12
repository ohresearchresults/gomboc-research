#!/usr/bin/env python3
"""Build an exact source/endpoint receipt for the cycle-20 circuit guards."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


SCHEMA = "polyhedral-goemboc.cycle20-topology-guard-certificate"
VERDICT = "EXACT_CYCLE20_CLUSTER_TOPOLOGY_GUARDS_PASS"
AUDIT_SCHEMA = "polyhedral-goemboc.topology-guard-audit"
AUDIT_VERDICT = "READ_ONLY_NEAR_TOPOLOGY_CIRCUIT_AUDIT_PASS"
CHAIN_VERDICT = "EXACT_POST_BYPASS_MATERIAL_CHAIN_PASS"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_circuit(text: str) -> tuple[int, int, int, int]:
    circuit = tuple(int(item) for item in text.split(","))
    if len(circuit) != 4 or len(set(circuit)) != 4:
        raise argparse.ArgumentTypeError("circuit must contain four distinct labels")
    return circuit


def read_exact_points(path: Path):
    points = {}
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != ["source_id", "x", "y", "z"]:
            raise ValueError("unexpected exact CSV header")
        for row in reader:
            label = int(row["source_id"])
            if label in points:
                raise ValueError(("duplicate label", label))
            points[label] = tuple(Q(row[axis]) for axis in ("x", "y", "z"))
    if not points:
        raise ValueError("empty exact CSV")
    return points


def subtract(left, right):
    return tuple(a - b for a, b in zip(left, right))


def cross(left, right):
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def determinant(points, circuit):
    missing = set(circuit) - set(points)
    if missing:
        raise ValueError(("circuit labels absent", sorted(missing)))
    a, b, c, d = (points[label] for label in circuit)
    value = dot(cross(subtract(b, a), subtract(c, a)), subtract(d, a))
    if value == 0:
        raise ValueError(("zero circuit determinant", circuit))
    return value


def exact_ratio(source_value, endpoint_value):
    sign = 1 if source_value > 0 else -1
    if sign * endpoint_value <= 0:
        raise ValueError("topology determinant changed sign")
    ratio = sign * endpoint_value / abs(source_value)
    if ratio <= 1:
        raise ValueError(("topology determinant did not move strictly inward", ratio))
    return ratio


def require_chain_binding(chain, source, endpoint, clearance_circuit):
    if chain.get("version") != 2 or chain.get("verdict") != CHAIN_VERDICT:
        raise ValueError("wrong exact-chain envelope")
    if tuple(chain.get("circuit", ())) != clearance_circuit:
        raise ValueError("clearance circuit mismatch")
    generated = chain.get("generated_sha256")
    if not isinstance(generated, dict):
        raise ValueError("exact chain has no generated hash ledger")
    source_matches = [
        value for key, value in generated.items() if key.endswith("checkpoint_000.csv")
    ]
    endpoint_matches = [
        value for key, value in generated.items() if key.endswith("checkpoint_001.csv")
    ]
    if source_matches != [sha256(source)] or endpoint_matches != [sha256(endpoint)]:
        raise ValueError("exact-chain source/endpoint binding mismatch")
    tau = chain.get("clearance_floor_guard", {}).get("chain_endpoint_tau_ratios")
    if not isinstance(tau, dict) or set(tau) != {
        str(clearance_circuit[0]), str(clearance_circuit[1])
    }:
        raise ValueError("exact-chain clearance endpoint packet mismatch")
    exact_tau = {label: Q(packet["tau_ratio_exact"]) for label, packet in tau.items()}
    if any(value <= 1 for value in exact_tau.values()):
        raise ValueError("clearance floor is not strict at the exact endpoint")
    return exact_tau


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--endpoint", required=True)
    parser.add_argument("--audit", required=True)
    parser.add_argument("--slp", required=True)
    parser.add_argument("--chain", required=True)
    parser.add_argument("--topology-circuit", type=parse_circuit, action="append", required=True)
    parser.add_argument("--clearance-circuit", type=parse_circuit, required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    source = Path(args.source).resolve()
    endpoint = Path(args.endpoint).resolve()
    audit_path = Path(args.audit).resolve()
    slp_path = Path(args.slp).resolve()
    chain_path = Path(args.chain).resolve()
    output = Path(args.output).resolve()
    topology_circuits = tuple(args.topology_circuit)
    if len(set(topology_circuits)) != len(topology_circuits):
        raise ValueError("duplicate topology circuit")
    if args.clearance_circuit in topology_circuits:
        raise ValueError("clearance circuit duplicated as topology guard")

    audit = json.loads(audit_path.read_text())
    if (
        audit.get("schema") != AUDIT_SCHEMA
        or audit.get("version") != 1
        or audit.get("verdict") != AUDIT_VERDICT
        or audit.get("source_sha256") != sha256(source)
    ):
        raise ValueError("wrong topology-audit envelope")
    audit_rows = audit.get("circuits")
    if not isinstance(audit_rows, list) or len(audit_rows) < 6:
        raise ValueError("topology audit does not expose the first gap")
    first_five = {tuple(row["circuit"]) for row in audit_rows[:5]}
    expected_cluster = set(topology_circuits) | {args.clearance_circuit}
    if first_five != expected_cluster:
        raise ValueError(("guard cluster is not the five-row audit prefix", first_five))
    fifth_slack = float(audit_rows[4]["minimum_normalized_support_slack"])
    sixth_slack = float(audit_rows[5]["minimum_normalized_support_slack"])
    if not fifth_slack > 0 or not sixth_slack > 2.0 * fifth_slack:
        raise ValueError("top-five topology cluster has no factor-two separation")

    slp = json.loads(slp_path.read_text())
    if slp.get("version") != 2 or slp.get("first_event") is not None:
        raise ValueError("numerical SLP is not a one-cell cycle-20 proposal")
    parameters = slp.get("parameters", {})
    if tuple(map(tuple, parameters.get("topology_guard_circuit", ()))) != topology_circuits:
        raise ValueError("SLP topology-guard order mismatch")
    history = slp.get("history")
    if not isinstance(history, list) or len(history) != 1 or history[0].get("accepted") is not True:
        raise ValueError("SLP does not contain exactly one accepted step")

    chain = json.loads(chain_path.read_text())
    endpoint_tau = require_chain_binding(
        chain, source, endpoint, args.clearance_circuit
    )
    source_points = read_exact_points(source)
    endpoint_points = read_exact_points(endpoint)
    rows = []
    for circuit in topology_circuits:
        source_value = determinant(source_points, circuit)
        endpoint_value = determinant(endpoint_points, circuit)
        ratio = exact_ratio(source_value, endpoint_value)
        rows.append({
            "circuit": list(circuit),
            "source_determinant_exact": str(source_value),
            "endpoint_determinant_exact": str(endpoint_value),
            "signed_endpoint_over_source_exact": str(ratio),
            "signed_endpoint_over_source_decimal": float(ratio),
            "strictly_inward": True,
        })

    bindings = {
        str(path): sha256(path)
        for path in (source, endpoint, audit_path, slp_path, chain_path)
    }
    payload = {
        "schema": SCHEMA,
        "version": 1,
        "scope": "exact cycle-20 near-topology cluster endpoint guard receipt",
        "source_hashes": bindings,
        "selection_contract": {
            "audit_prefix_length": 5,
            "factor_two_gap_after_prefix": True,
            "fifth_slack_decimal": fifth_slack,
            "sixth_slack_decimal": sixth_slack,
            "clearance_circuit": list(args.clearance_circuit),
            "topology_circuits": [list(circuit) for circuit in topology_circuits],
        },
        "topology_guards": rows,
        "clearance_floor_endpoint_tau_exact": {
            label: str(value) for label, value in endpoint_tau.items()
        },
        "all_four_topology_determinants_strictly_inward": len(rows) == 4,
        "clearance_floor_strict_at_exact_endpoint": True,
        "verdict": VERDICT,
    }
    output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "verdict": VERDICT,
        "topology_ratios": {
            ",".join(map(str, row["circuit"])): row["signed_endpoint_over_source_decimal"]
            for row in rows
        },
        "clearance_tau": {label: float(value) for label, value in endpoint_tau.items()},
        "output": str(output),
    }, indent=2))


if __name__ == "__main__":
    main()
