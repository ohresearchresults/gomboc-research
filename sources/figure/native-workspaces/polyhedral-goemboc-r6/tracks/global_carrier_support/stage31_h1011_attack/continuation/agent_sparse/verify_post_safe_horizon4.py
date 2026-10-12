#!/usr/bin/env python3
"""Independent reconstruction of the exact post-safe-flip horizon-4 cell."""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
MAIN = HERE.parent / "main"
ATTACK = HERE.parents[1]
TRACK = ATTACK.parent
ROOT = HERE.parents[4]

SOURCE = MAIN / "exact_full_control_chain_far.csv"
FACES_PATH = MAIN / "exact_full_control_chain_post_faces.json"
PROPOSAL = MAIN / "post_safe_flip_proposal.json"
PROPOSAL_ENDPOINT = MAIN / "post_safe_flip_candidate.csv"
SCAN = MAIN / "post_safe_flip_first_event_scan.json"
ENDPOINT = HERE / "post_safe_horizon4_exact.csv"
CERTIFICATE = HERE / "post_safe_horizon4_certificate.json"
OUTPUT = HERE / "post_safe_horizon4_verification.json"
HORIZON = Q(4)

sys.path.insert(0, str(TRACK / "rigorous_local_bypass"))
import exact_core as ex  # noqa: E402
sys.path.insert(0, str(ATTACK))
import build_exact_circuit_flip as parent_exact  # noqa: E402
sys.path.insert(0, str(HERE))
import verify_integrated_full_control_chain as clean  # noqa: E402


BASE = frozenset(range(17)) | {54}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def residuals(path, source, endpoint, faces):
    result = {}
    for name in parent_exact.SELECTED_COMPONENTS:
        source_record = parent_exact.selected_residual_record(source, faces, name)
        endpoint_record = parent_exact.selected_residual_record(endpoint, faces, name)
        assert Q(endpoint_record["squared_value"]) < Q(source_record["squared_value"])
        numerator, denominator = parent_exact.selected_fraction_polynomials(
            path, faces, name
        )
        derivative = (
            numerator.derivative() * denominator
            - numerator * denominator.derivative()
        )
        sign, leaves, worst = ex.bernstein_sign(
            derivative, Q(0), HORIZON, max_depth=60
        )
        assert sign == -1
        result[name] = {
            "source": source_record,
            "endpoint": endpoint_record,
            "strict_endpoint_improvement": True,
            "derivative_sign": sign,
            "derivative_degree": derivative.degree,
            "derivative_bernstein_leaf_count": leaves,
            "derivative_minimum_bernstein_log10_abs": worst,
            "derivative_digest": canonical_hash(derivative.exact()),
        }
    return result


def main():
    frozen = json.loads(CERTIFICATE.read_text())
    assert frozen["verdict"] == "EXACT_POST_SAFE_FLIP_HORIZON4_CHECKPOINT_PASS"
    proposal = json.loads(PROPOSAL.read_text())
    scan = json.loads(SCAN.read_text())
    assert proposal["verdict"] == "POST_SAFE_FLIP_FULL_CONTROL_RATIONAL_DESCENT_PROPOSAL_PASS"
    assert scan["verdict"] == "EXHAUSTIVE_EXACT_FIRST_EVENT_LOCATOR_PASS"
    assert Q(scan["first_candidate"]["lo"]) > HORIZON

    for file in (SOURCE, FACES_PATH, PROPOSAL, PROPOSAL_ENDPOINT, SCAN):
        key = str(file.relative_to(ROOT))
        assert sha256(file) == frozen["source_hashes"][key]

    source = ex.read_rows(SOURCE)
    proposal_endpoint = ex.read_rows(PROPOSAL_ENDPOINT)
    faces = json.loads(FACES_PATH.read_text())
    path = {
        label: tuple(
            ex.P((source[label][axis], proposal_endpoint[label][axis] - source[label][axis]))
            for axis in range(3)
        )
        for label in source
    }
    delta_digest = canonical_hash({
        str(label): [
            ex.qs(proposal_endpoint[label][axis] - source[label][axis])
            for axis in range(3)
        ]
        for label in sorted(source)
    })
    assert delta_digest == frozen["path"]["endpoint_delta_digest"]
    assert frozen["path"]["horizon"] == "4"

    rows = list(clean.primitive_rows(path, faces))
    assert len(rows) == 7904
    continuum = clean.exhaustive_interval(rows, Q(0), HORIZON)
    assert continuum == frozen["exhaustive_continuum"]

    endpoint = {
        label: tuple(coordinate.eval(HORIZON) for coordinate in xyz)
        for label, xyz in path.items()
    }
    assert ex.read_rows(ENDPOINT) == endpoint
    assert sha256(ENDPOINT) == frozen["checkpoint"]["sha256"]
    assert canonical_hash({
        str(label): [ex.qs(value) for value in endpoint[label]]
        for label in sorted(endpoint)
    }) == frozen["checkpoint"]["coordinate_hash"]

    support = ex.supporting_cell(endpoint, faces)
    _ledger, mechanics = ex.classify_point(endpoint, faces)
    assert {key: value for key, value in support.items() if key != "edges"} == frozen["checkpoint"]["support"]
    assert mechanics == frozen["checkpoint"]["mechanics"]
    assert support["f_vector"] == [61, 162, 103]
    assert mechanics["class"] == [2, 2, 2]
    assert BASE in {frozenset(face) for face in faces}
    assert parent_exact.forced_rails().issubset(set(support["edges"]))
    d6, m24 = ex.exact_centroid_numerators(endpoint, faces)
    centroid = tuple(value / (4 * d6) for value in m24)
    assert [ex.qs(value) for value in centroid] == frozen["checkpoint"]["exact_centroid"]

    actual_residuals = residuals(path, source, endpoint, faces)
    assert actual_residuals == frozen["directed_residuals"]
    edge = ex.mechanics_primitives(path, faces)["edge"][(9, 10)]
    components = ("t", "one_minus_t", "beta1", "beta2")
    witness = min(components, key=lambda item: edge[item].eval(Q(0)))
    sign, leaves, worst = ex.bernstein_sign(
        edge[witness], Q(0), HORIZON, max_depth=60
    )
    h910 = {
        "component": witness,
        "sign": sign,
        "bernstein_leaf_count": leaves,
        "minimum_bernstein_log10_abs": worst,
        "polynomial_digest": canonical_hash(edge[witness].exact()),
    }
    assert sign == -1
    assert h910 == frozen["h910_nonresurrection"]

    receipt = {
        "version": 1,
        "certificate_sha256": sha256(CERTIFICATE),
        "endpoint_sha256": sha256(ENDPOINT),
        "primitive_count": len(rows),
        "horizon": "4",
        "class": mechanics["class"],
        "forced_rails": 37,
        "h910_strictly_dead": True,
        "endpoint_decisions": {
            name: row["endpoint"]["decision_value"]
            for name, row in actual_residuals.items()
        },
        "verdict": "INDEPENDENT_EXACT_POST_SAFE_FLIP_HORIZON4_CHECKPOINT_PASS",
    }
    OUTPUT.write_text(json.dumps(receipt, indent=2) + "\n")
    print(receipt["verdict"])


if __name__ == "__main__":
    main()
