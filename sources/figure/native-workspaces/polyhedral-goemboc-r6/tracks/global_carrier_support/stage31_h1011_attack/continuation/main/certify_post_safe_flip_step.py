#!/usr/bin/env python3
"""Exact certificate for one curved-bypass material step after the safe flip."""
from __future__ import annotations

import csv
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
OUTPUT = HERE / "post_safe_flip_step_certificate.json"
ENDPOINT_OUT = HERE / "post_safe_flip_step_exact.csv"

sys.path.insert(0, str(TRACK / "rigorous_local_bypass"))
import exact_core as ex  # noqa: E402
sys.path.insert(0, str(ATTACK))
import build_exact_circuit_flip as residual_core  # noqa: E402


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


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def write_rows(path, rows):
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(("source_id", "x", "y", "z"))
        for label in sorted(rows):
            writer.writerow((label, *(ex.qs(value) for value in rows[label])))


def point(path, parameter):
    return {
        label: tuple(polynomial.eval(parameter) for polynomial in xyz)
        for label, xyz in path.items()
    }


def rails():
    result = set()
    for route in (
        [228] + list(range(229, 247)) + [8],
        [228] + list(range(247, 265)) + [8],
    ):
        result.update(tuple(sorted(pair)) for pair in zip(route, route[1:]))
    result.remove((228, 229))
    return result


def primitives(path, faces):
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
    for name, polynomial in primitives(path, faces):
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


def checkpoint(points, faces):
    support = ex.supporting_cell(points, faces)
    _ledger, mechanics = ex.classify_point(points, faces)
    if support["f_vector"] != [61, 162, 103] or mechanics["class"] != [2, 2, 2]:
        raise AssertionError((support, mechanics))
    if support["active_labels"] != sorted(points):
        raise AssertionError("active labels changed")
    if BASE not in {frozenset(face) for face in faces}:
        raise AssertionError("base absent")
    missing = rails() - set(support["edges"])
    if missing:
        raise AssertionError(("rails absent", sorted(missing)))
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
        "forced_rail_count": len(rails()),
        "missing_forced_rails": [],
    }


def residuals(path, faces):
    source = point(path, Q(0))
    endpoint = point(path, Q(1))
    output = {}
    for name in ("S", "U54", "H56", "H1011"):
        source_record = residual_core.selected_residual_record(source, faces, name)
        endpoint_record = residual_core.selected_residual_record(endpoint, faces, name)
        source_value = Q(source_record["squared_value"])
        endpoint_value = Q(endpoint_record["squared_value"])
        if not endpoint_value < source_value:
            raise AssertionError((name, "endpoint did not improve"))
        numerator, denominator = residual_core.selected_fraction_polynomials(
            path, faces, name
        )
        derivative = numerator.derivative() * denominator - numerator * denominator.derivative()
        sign, leaves, worst = ex.bernstein_sign(
            derivative, Q(0), Q(1), max_depth=60
        )
        if sign != -1:
            raise AssertionError((name, "not monotonically decreasing"))
        output[name] = {
            "source": source_record,
            "endpoint": endpoint_record,
            "exact_squared_drop": ex.qs(source_value - endpoint_value),
            "derivative_sign": sign,
            "derivative_degree": derivative.degree,
            "derivative_bernstein_leaf_count": leaves,
            "derivative_minimum_bernstein_log10_abs": worst,
            "derivative_digest": canonical_hash(derivative.exact()),
        }
    return output


def h910(path, faces):
    values = ex.mechanics_primitives(path, faces)["edge"][(9, 10)]
    components = ("t", "one_minus_t", "beta1", "beta2")
    witness = min(components, key=lambda item: values[item].eval(Q(0)))
    polynomial = values[witness]
    if not polynomial.eval(Q(1)) < polynomial.eval(Q(0)) < 0:
        raise AssertionError("H910 did not move strictly outward")
    sign, leaves, worst = ex.bernstein_sign(polynomial, Q(0), Q(1), max_depth=60)
    if sign != -1:
        raise AssertionError("H910 witness crosses zero")
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


def danger_support(path, faces):
    output = {}
    for face_index, witness, polynomial in ex.support_polynomials(path, faces):
        family = (frozenset(faces[face_index]), witness)
        if family not in DANGER:
            continue
        normal = ex.cycle_normal(faces[face_index], path)
        denominator = ex.norm2(normal)
        source_value = polynomial.eval(Q(0)) ** 2 / denominator.eval(Q(0))
        endpoint_value = polynomial.eval(Q(1)) ** 2 / denominator.eval(Q(1))
        if not endpoint_value > source_value:
            raise AssertionError((family, "danger margin did not increase"))
        output[f"{sorted(family[0])}|{witness}"] = {
            "source_squared_normalized_margin": ex.qs(source_value),
            "endpoint_squared_normalized_margin": ex.qs(endpoint_value),
            "strict_increase": ex.qs(endpoint_value - source_value),
            "support_polynomial_digest": canonical_hash(polynomial.exact()),
        }
    if len(output) != 2:
        raise AssertionError(("danger support family incomplete", output))
    return output


def main():
    proposal = json.loads(PROPOSAL.read_text())
    scan = json.loads(SCAN.read_text())
    if proposal["verdict"] != "POST_SAFE_FLIP_FULL_CONTROL_RATIONAL_DESCENT_PROPOSAL_PASS":
        raise AssertionError(proposal["verdict"])
    if scan["verdict"] != "EXHAUSTIVE_EXACT_FIRST_EVENT_LOCATOR_PASS":
        raise AssertionError(scan["verdict"])
    if not Q(scan["first_candidate"]["lo"]) > 1:
        raise AssertionError("locator found an event inside accepted step")
    source = ex.read_rows(SOURCE)
    endpoint = ex.read_rows(CANDIDATE)
    faces = json.loads(FACES_PATH.read_text())
    path = {
        label: tuple(
            ex.P((source[label][axis], endpoint[label][axis] - source[label][axis]))
            for axis in range(3)
        )
        for label in source
    }
    exact_ledger = exhaustive(path, faces)
    if exact_ledger["primitive_count"] != 7904:
        raise AssertionError(exact_ledger)
    class_cover = ex.certify_path_segment(path, faces, PROTECTED)
    if class_cover["start_class"]["class"] != [2, 2, 2]:
        raise AssertionError(class_cover)
    source_checkpoint = checkpoint(source, faces)
    endpoint_checkpoint = checkpoint(endpoint, faces)
    directed = residuals(path, faces)
    dead = h910(path, faces)
    danger = danger_support(path, faces)
    write_rows(ENDPOINT_OUT, endpoint)
    certificate = {
        "version": 1,
        "type": "exact rational material bypass step in fixed post-flip cell",
        "scope": (
            "Exact for all 7,904 support/own-centroid mechanics primitives on "
            "the accepted t in [0,1] step; the first ray event is strictly after "
            "t=1. Base, U8, 61 rows, H910 and all 37 rails are preserved, both "
            "row-230-loss support margins strictly increase, and S/U54/H56/H1011 decrease."
        ),
        "source_hashes": {
            str(file.relative_to(ROOT)): sha256(file)
            for file in (SOURCE, FACES_PATH, PROPOSAL, CANDIDATE, SCAN)
        },
        "path": {
            "endpoint_delta_digest": canonical_hash({
                str(label): [ex.qs(endpoint[label][axis] - source[label][axis]) for axis in range(3)]
                for label in sorted(source)
            }),
            "accepted_interval": ["0", "1"],
            "first_future_event_lower_bound": scan["first_candidate"]["lo"],
            "first_future_event_name": scan["first_candidate"]["name"],
        },
        "exhaustive_interval": exact_ledger,
        "class_cover": class_cover,
        "checkpoints": {
            "source": source_checkpoint,
            "endpoint": endpoint_checkpoint,
        },
        "directed_residuals": directed,
        "h910_nonresurrection": dead,
        "row230_loss_support_bypass": danger,
        "generated_file_sha256": {
            str(ENDPOINT_OUT.relative_to(ROOT)): sha256(ENDPOINT_OUT)
        },
        "residual_verdict": {
            "winner": False,
            "endpoint_class": [2, 2, 2],
            "next_action": "rebuild full-control chart from post_safe_flip_step_exact.csv",
        },
        "verdict": "EXACT_POST_SAFE_FLIP_MATERIAL_BYPASS_STEP_PASS",
    }
    OUTPUT.write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps({
        "verdict": certificate["verdict"],
        "primitive_count": exact_ledger["primitive_count"],
        "first_future_event": certificate["path"],
        "endpoint_decisions": {
            name: row["endpoint"]["decision_value"] for name, row in directed.items()
        },
        "danger_support": danger,
    }, indent=2))


if __name__ == "__main__":
    main()
