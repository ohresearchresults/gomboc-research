#!/usr/bin/env python3
"""Independent verifier for the exact post-safe-flip material bypass step."""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
ATTACK = HERE.parents[1]
TRACK = ATTACK.parent
ROOT = HERE.parents[4]
SOURCE = HERE / "exact_full_control_chain_far.csv"
FACES_PATH = HERE / "exact_full_control_chain_post_faces.json"
PROPOSAL = HERE / "post_safe_flip_proposal.json"
CANDIDATE = HERE / "post_safe_flip_candidate.csv"
SCAN = HERE / "post_safe_flip_first_event_scan.json"
CERTIFICATE = HERE / "post_safe_flip_step_certificate.json"
GENERATED = HERE / "post_safe_flip_step_exact.csv"

sys.path.insert(0, str(TRACK / "rigorous_local_bypass"))
import exact_core as ex  # noqa: E402
sys.path.insert(0, str(ATTACK))
import verify_exact_circuit_flip as residual_verify  # noqa: E402


BASE = frozenset(range(17)) | {54}
PRIMARY = (7, 8, 245)
PROTECTED = {
    "stable": [sorted(BASE), list(PRIMARY)],
    "unstable": [8, 54],
    "saddles": [[5, 6], [10, 11]],
}
DANGER = {
    (frozenset((198, 230, 231)), 229),
    (frozenset((198, 229, 230)), 231),
}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def rows(path, faces):
    ledger = ex.mechanics_primitives(path, faces)
    yield "volume_d6", ledger["d6"]
    for face_index, witness, polynomial in ex.support_polynomials(path, faces):
        yield f"support:f{face_index}:w{witness}", polynomial
    for face_key, values in sorted(ledger["reference"].items()):
        for edge, polynomial in sorted(values.items()):
            yield f"face_reference:{face_key}:{edge}", polynomial
    for face_key, values in sorted(ledger["face"].items()):
        for edge, polynomial in sorted(values.items()):
            yield f"face_raw:{face_key}:{edge}", polynomial
    for vertex, values in sorted(ledger["vertex"].items()):
        for neighbor, polynomial in sorted(values.items()):
            yield f"vertex:{vertex}:{neighbor}", polynomial
    for edge, values in sorted(ledger["edge"].items()):
        for component in (
            "direction_norm2", "gram", "t", "one_minus_t", "beta1", "beta2"
        ):
            yield f"edge:{edge}:{component}", values[component]


def exhaustive(path, faces):
    digest = hashlib.sha256()
    count = 0
    leaves = 0
    worst = None
    for name, polynomial in rows(path, faces):
        sign, row_leaves, margin = ex.bernstein_sign(
            polynomial, Q(0), Q(1), max_depth=60
        )
        count += 1
        leaves += row_leaves
        worst = margin if worst is None else min(worst, margin)
        digest.update(f"{name}|{sign}|{'|'.join(polynomial.exact())}\n".encode())
    return {
        "primitive_count": count,
        "bernstein_leaf_count": leaves,
        "minimum_bernstein_log10_abs": worst,
        "primitive_digest": digest.hexdigest(),
    }


def rail_set():
    result = set()
    for route in (
        [228] + list(range(229, 247)) + [8],
        [228] + list(range(247, 265)) + [8],
    ):
        result.update(tuple(sorted(pair)) for pair in zip(route, route[1:]))
    result.remove((228, 229))
    return result


def checkpoint(points, faces):
    support = ex.supporting_cell(points, faces)
    _ledger, mechanics = ex.classify_point(points, faces)
    assert support["f_vector"] == [61, 162, 103]
    assert support["active_labels"] == sorted(points)
    assert mechanics["class"] == [2, 2, 2]
    assert BASE in {frozenset(face) for face in faces}
    assert rail_set().issubset(set(support["edges"]))
    d6, m24 = ex.exact_centroid_numerators(points, faces)
    centroid = tuple(value / (4 * d6) for value in m24)
    return {
        "coordinate_hash": canonical_hash({
            str(label): [ex.qs(value) for value in points[label]]
            for label in sorted(points)
        }),
        "exact_centroid": [ex.qs(value) for value in centroid],
        "support": {key: value for key, value in support.items() if key != "edges"},
        "mechanics": mechanics,
        "base_face_present": True,
        "forced_rail_count": len(rail_set()),
        "missing_forced_rails": [],
    }


def residuals(path, faces):
    source = {
        label: tuple(polynomial.eval(Q(0)) for polynomial in xyz)
        for label, xyz in path.items()
    }
    endpoint = {
        label: tuple(polynomial.eval(Q(1)) for polynomial in xyz)
        for label, xyz in path.items()
    }
    result = {}
    for name in ("S", "U54", "H56", "H1011"):
        source_record = residual_verify.residual_record(source, faces, name)
        endpoint_record = residual_verify.residual_record(endpoint, faces, name)
        source_value = Q(source_record["squared_value"])
        endpoint_value = Q(endpoint_record["squared_value"])
        assert endpoint_value < source_value
        numerator, denominator = residual_verify.fractions(path, faces, name)[
            residual_verify.SELECTED[name]
        ]
        derivative = numerator.derivative() * denominator - numerator * denominator.derivative()
        sign, leaves, worst = ex.bernstein_sign(derivative, Q(0), Q(1), max_depth=60)
        assert sign == -1
        result[name] = {
            "source": source_record,
            "endpoint": endpoint_record,
            "exact_squared_drop": ex.qs(source_value - endpoint_value),
            "derivative_sign": sign,
            "derivative_degree": derivative.degree,
            "derivative_bernstein_leaf_count": leaves,
            "derivative_minimum_bernstein_log10_abs": worst,
            "derivative_digest": canonical_hash(derivative.exact()),
        }
    return result


def dead_h910(path, faces):
    values = ex.mechanics_primitives(path, faces)["edge"][(9, 10)]
    components = ("t", "one_minus_t", "beta1", "beta2")
    witness = min(components, key=lambda item: values[item].eval(Q(0)))
    polynomial = values[witness]
    assert polynomial.eval(Q(1)) < polynomial.eval(Q(0)) < 0
    sign, leaves, worst = ex.bernstein_sign(polynomial, Q(0), Q(1), max_depth=60)
    assert sign == -1
    return {
        "component": witness,
        "source": ex.qs(polynomial.eval(Q(0))),
        "endpoint": ex.qs(polynomial.eval(Q(1))),
        "sign": sign,
        "bernstein_leaf_count": leaves,
        "minimum_bernstein_log10_abs": worst,
        "polynomial_degree": polynomial.degree,
        "polynomial_digest": canonical_hash(polynomial.exact()),
    }


def danger(path, faces):
    result = {}
    for face_index, witness, polynomial in ex.support_polynomials(path, faces):
        family = (frozenset(faces[face_index]), witness)
        if family not in DANGER:
            continue
        normal = ex.cycle_normal(faces[face_index], path)
        denominator = ex.norm2(normal)
        first = polynomial.eval(Q(0)) ** 2 / denominator.eval(Q(0))
        second = polynomial.eval(Q(1)) ** 2 / denominator.eval(Q(1))
        assert second > first
        result[f"{sorted(family[0])}|{witness}"] = {
            "source_squared_normalized_margin": ex.qs(first),
            "endpoint_squared_normalized_margin": ex.qs(second),
            "strict_increase": ex.qs(second - first),
            "support_polynomial_digest": canonical_hash(polynomial.exact()),
        }
    assert len(result) == 2
    return result


def main():
    frozen = json.loads(CERTIFICATE.read_text())
    assert frozen["verdict"] == "EXACT_POST_SAFE_FLIP_MATERIAL_BYPASS_STEP_PASS"
    for file in (SOURCE, FACES_PATH, PROPOSAL, CANDIDATE, SCAN):
        key = str(file.relative_to(ROOT))
        assert sha256(file) == frozen["source_hashes"][key]
    source = ex.read_rows(SOURCE)
    endpoint = ex.read_rows(CANDIDATE)
    assert ex.read_rows(GENERATED) == endpoint
    faces = json.loads(FACES_PATH.read_text())
    path = {
        label: tuple(
            ex.P((source[label][axis], endpoint[label][axis] - source[label][axis]))
            for axis in range(3)
        )
        for label in source
    }
    assert canonical_hash({
        str(label): [ex.qs(endpoint[label][axis] - source[label][axis]) for axis in range(3)]
        for label in sorted(source)
    }) == frozen["path"]["endpoint_delta_digest"]
    scan = json.loads(SCAN.read_text())
    assert Q(scan["first_candidate"]["lo"]) > 1
    assert scan["first_candidate"]["lo"] == frozen["path"]["first_future_event_lower_bound"]
    assert exhaustive(path, faces) == frozen["exhaustive_interval"]
    assert ex.certify_path_segment(path, faces, PROTECTED) == frozen["class_cover"]
    assert checkpoint(source, faces) == frozen["checkpoints"]["source"]
    assert checkpoint(endpoint, faces) == frozen["checkpoints"]["endpoint"]
    assert residuals(path, faces) == frozen["directed_residuals"]
    assert dead_h910(path, faces) == frozen["h910_nonresurrection"]
    assert danger(path, faces) == frozen["row230_loss_support_bypass"]
    key = str(GENERATED.relative_to(ROOT))
    assert sha256(GENERATED) == frozen["generated_file_sha256"][key]
    print("INDEPENDENT_EXACT_POST_SAFE_FLIP_MATERIAL_BYPASS_STEP_PASS")


if __name__ == "__main__":
    main()
