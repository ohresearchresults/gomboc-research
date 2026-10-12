#!/usr/bin/env python3
"""Certify a strict post-safe-flip checkpoint before the row-230 wall."""
from __future__ import annotations

import csv
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
HORIZON = Q(4)

sys.path.insert(0, str(TRACK / "rigorous_local_bypass"))
import exact_core as ex  # noqa: E402
sys.path.insert(0, str(ATTACK))
import build_exact_circuit_flip as parent_exact  # noqa: E402


BASE = frozenset(range(17)) | {54}
EXPECTED_ACTIVE = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    54, 69, 72, 73, 88, 198, 224, 228, 229, 230, 231, 232, 233, 234,
    235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247,
    248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260,
    261, 262, 263, 264,
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def primitive_rows(path, faces):
    ledger = ex.mechanics_primitives(path, faces)
    yield "volume_d6", ledger["d6"], "mechanics_denominator"
    for face_index, witness, polynomial in ex.support_polynomials(path, faces):
        yield f"support:f{face_index}:w{witness}", polynomial, "support"
    for face_key, rows in sorted(ledger["reference"].items()):
        for edge, value in sorted(rows.items()):
            yield f"face_reference:{face_key}:{edge}", value, "mechanics_denominator"
    for face_key, rows in sorted(ledger["face"].items()):
        for edge, value in sorted(rows.items()):
            yield f"face_raw:{face_key}:{edge}", value, "face_component"
    for vertex, rows in sorted(ledger["vertex"].items()):
        for neighbor, value in sorted(rows.items()):
            yield f"vertex:{vertex}:{neighbor}", value, "vertex_component"
    for edge, rows in sorted(ledger["edge"].items()):
        for component in (
            "direction_norm2", "gram", "t", "one_minus_t", "beta1", "beta2"
        ):
            yield f"edge:{edge}:{component}", rows[component], "edge_component"


def exhaustive_interval(rows, lo, hi):
    digest = hashlib.sha256()
    count = 0
    leaves = 0
    worst = None
    for name, polynomial, family in rows:
        sign, row_leaves, margin = ex.bernstein_sign(
            polynomial, lo, hi, max_depth=60
        )
        count += 1
        leaves += row_leaves
        worst = margin if worst is None else min(worst, margin)
        digest.update(
            f"{name}|{family}|{sign}|{'|'.join(polynomial.exact())}\n".encode()
        )
    return {
        "lo": ex.qs(lo),
        "hi": ex.qs(hi),
        "primitive_count": count,
        "bernstein_leaf_count": leaves,
        "minimum_bernstein_log10_abs": worst,
        "primitive_digest": digest.hexdigest(),
    }


def write_exact_csv(path, rows):
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(("source_id", "x", "y", "z"))
        for label in sorted(rows):
            writer.writerow((label, *(ex.qs(value) for value in rows[label])))


def selected_residuals(path, source, endpoint, faces):
    result = {}
    for name in parent_exact.SELECTED_COMPONENTS:
        source_record = parent_exact.selected_residual_record(source, faces, name)
        endpoint_record = parent_exact.selected_residual_record(endpoint, faces, name)
        source_value = Q(source_record["squared_value"])
        endpoint_value = Q(endpoint_record["squared_value"])
        assert endpoint_value < source_value
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
    proposal = json.loads(PROPOSAL.read_text())
    scan = json.loads(SCAN.read_text())
    assert proposal["verdict"] == "POST_SAFE_FLIP_FULL_CONTROL_RATIONAL_DESCENT_PROPOSAL_PASS"
    assert scan["verdict"] == "EXHAUSTIVE_EXACT_FIRST_EVENT_LOCATOR_PASS"
    first = scan["first_candidate"]
    assert Q(first["lo"]) > HORIZON

    source = ex.read_rows(SOURCE)
    proposal_endpoint = ex.read_rows(PROPOSAL_ENDPOINT)
    faces = json.loads(FACES_PATH.read_text())
    path = {
        label: tuple(
            ex.P((
                source[label][axis],
                proposal_endpoint[label][axis] - source[label][axis],
            ))
            for axis in range(3)
        )
        for label in source
    }
    endpoint = {
        label: tuple(coordinate.eval(HORIZON) for coordinate in xyz)
        for label, xyz in path.items()
    }
    rows = list(primitive_rows(path, faces))
    assert len(rows) == 7904
    continuum = exhaustive_interval(rows, Q(0), HORIZON)
    scan_horizon = next(row for row in scan["horizon_audits"] if row["horizon"] == "4")
    assert scan_horizon["strict"] and scan_horizon["failure_count"] == 0
    assert scan_horizon["proved_leaf_count"] == continuum["bernstein_leaf_count"]
    assert scan_horizon["minimum_proved_bernstein_log10_abs"] == continuum["minimum_bernstein_log10_abs"]

    support = ex.supporting_cell(endpoint, faces)
    _ledger, mechanics = ex.classify_point(endpoint, faces)
    assert support["f_vector"] == [61, 162, 103]
    assert support["active_labels"] == EXPECTED_ACTIVE
    assert mechanics["class"] == [2, 2, 2]
    assert BASE in {frozenset(face) for face in faces}
    assert parent_exact.forced_rails().issubset(set(support["edges"]))
    d6, m24 = ex.exact_centroid_numerators(endpoint, faces)
    centroid = tuple(value / (4 * d6) for value in m24)

    residuals = selected_residuals(path, source, endpoint, faces)
    edge = ex.mechanics_primitives(path, faces)["edge"][(9, 10)]
    components = ("t", "one_minus_t", "beta1", "beta2")
    witness = min(components, key=lambda item: edge[item].eval(Q(0)))
    assert edge[witness].eval(Q(0)) < 0
    h910_sign, h910_leaves, h910_worst = ex.bernstein_sign(
        edge[witness], Q(0), HORIZON, max_depth=60
    )
    assert h910_sign == -1

    write_exact_csv(ENDPOINT, endpoint)
    certificate = {
        "version": 1,
        "type": "exact strict post-safe-flip rational checkpoint",
        "scope": (
            "Exact for the post-safe-flip full-control path on t in [0,4], "
            "all 7,904 support/mechanics primitives, own uniform-volume centroid, "
            "all selected residuals, H910, 61 rows, enlarged base and 37 rails."
        ),
        "source_hashes": {
            str(file.relative_to(ROOT)): sha256(file)
            for file in (SOURCE, FACES_PATH, PROPOSAL, PROPOSAL_ENDPOINT, SCAN)
        },
        "path": {
            "horizon": ex.qs(HORIZON),
            "endpoint_delta_digest": canonical_hash({
                str(label): [
                    ex.qs(proposal_endpoint[label][axis] - source[label][axis])
                    for axis in range(3)
                ]
                for label in sorted(source)
            }),
            "first_event_after_checkpoint": {
                key: value for key, value in first.items()
                if key not in ("polynomial_exact", "value_lo", "value_hi")
            },
        },
        "exhaustive_continuum": continuum,
        "checkpoint": {
            "file": ENDPOINT.name,
            "sha256": sha256(ENDPOINT),
            "coordinate_hash": canonical_hash({
                str(label): [ex.qs(value) for value in endpoint[label]]
                for label in sorted(endpoint)
            }),
            "exact_centroid": [ex.qs(value) for value in centroid],
            "support": {key: value for key, value in support.items() if key != "edges"},
            "mechanics": mechanics,
            "base_present": True,
            "forced_rail_count": 37,
            "missing_forced_rails": [],
        },
        "directed_residuals": residuals,
        "h910_nonresurrection": {
            "component": witness,
            "sign": h910_sign,
            "bernstein_leaf_count": h910_leaves,
            "minimum_bernstein_log10_abs": h910_worst,
            "polynomial_digest": canonical_hash(edge[witness].exact()),
        },
        "residual_verdict": {
            "winner": False,
            "class": [2, 2, 2],
            "next_action": "rebuild the guarded full-control chart from post_safe_horizon4_exact.csv before the row-230 degeneracy",
        },
        "verdict": "EXACT_POST_SAFE_FLIP_HORIZON4_CHECKPOINT_PASS",
    }
    CERTIFICATE.write_text(json.dumps(certificate, indent=2) + "\n")
    print(certificate["verdict"])


if __name__ == "__main__":
    main()
