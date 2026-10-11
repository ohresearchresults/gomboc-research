#!/usr/bin/env python3
"""Independent exact verifier for the Round-12 FAR event chain.

This verifier does not import the builder.  It reconstructs the rational
moving-base path from the two raw finite-decimal checkpoints, rebuilds both
algebraic event polynomials, rechecks every primitive ledger and every guard,
and compares the resulting proof digests with the frozen certificate.
"""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
GROUPED = HERE.parent
ROOT = HERE.parents[3]
EXACT_DIR = GROUPED / "rigorous_null_bypass"
sys.path.insert(0, str(EXACT_DIR))

import grouped_exact as gx  # noqa: E402


ex = gx.ex
P = ex.P
BASE = frozenset(range(17)) | {54}
STABLE_TRIANGLE = frozenset((7, 8, 245))
EVENT_QUAD = (6, 198, 244, 245)
ALT_ROUTE = (228, 198, 263, 9, 8)
TOPOLOGY_QUADS = (
    ("round4_far", (7, 8, 245, 246), -1),
    ("round8_pre", (9, 198, 263, 264), -1),
    ("round10_far", (8, 264, 246, 198), 1),
    ("round12_far", (198, 263, 262, 11), 1),
)
PROTECTED = {
    "stable": [sorted(BASE), sorted(STABLE_TRIANGLE)],
    "unstable": [8, 54],
    "saddles": [[6, 7], [198, 263]],
}

CERTIFICATE = HERE / "exact_event_chain_certificate.json"
SUMMARY = HERE / "exact_event_chain_verification.json"
PRE_RAW = HERE / "quad_6_198_244_245_event_pre.csv"
FAR_RAW = HERE / "quad_6_198_244_245_event_far.csv"
PRE_FACES = HERE / "quad_6_198_244_245_event_pre_faces.json"
WALL_FACES = HERE / "quad_6_198_244_245_event_wall_faces.json"
FAR_FACES = HERE / "quad_6_198_244_245_event_far_faces.json"


CHECKPOINTS = (
    (
        "round12_buffer_source",
        GROUPED / "row54_round12_far_multiguard_buffer_buffer.csv",
        GROUPED / "row54_round12_far_multiguard_buffer_buffer_faces.json",
    ),
    (
        "guarded_continuation_recovered",
        HERE / "birth6_guard_buffer_source.csv",
        HERE / "guarded_continuation_best_faces.json",
    ),
    (
        "birth6_guard_buffer",
        HERE / "birth6_guard_buffer_buffer.csv",
        HERE / "birth6_guard_buffer_buffer_faces.json",
    ),
    (
        "guarded_after_birth6",
        HERE / "s67245_guard_buffer_source.csv",
        HERE / "guarded_after_birth6_best_faces.json",
    ),
    (
        "s67245_guard_buffer",
        HERE / "s67245_guard_buffer_buffer.csv",
        HERE / "s67245_guard_buffer_buffer_faces.json",
    ),
    (
        "guarded_after_s67245_pre",
        PRE_RAW,
        PRE_FACES,
    ),
    (
        "quad_far",
        FAR_RAW,
        FAR_FACES,
    ),
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def determinant_polynomial(path, quad):
    a, b, c, d = (path[label] for label in quad)
    return ex.det3(ex.sub(b, a), ex.sub(c, a), ex.sub(d, a))


def path_digest(path) -> str:
    return canonical_hash(
        {
            str(label): [coordinate.exact() for coordinate in path[label]]
            for label in sorted(path)
        }
    )


def divide_polynomials(dividend: P, divisor: P):
    coefficients = list(dividend.c)
    divisor_coefficients = list(divisor.c)
    quotient = [Q(0)] * max(1, len(coefficients) - len(divisor_coefficients) + 1)
    while len(coefficients) >= len(divisor_coefficients) and any(coefficients):
        shift = len(coefficients) - len(divisor_coefficients)
        factor = coefficients[-1] / divisor_coefficients[-1]
        quotient[shift] += factor
        for index, value in enumerate(divisor_coefficients):
            coefficients[shift + index] -= factor * value
        while len(coefficients) > 1 and not coefficients[-1]:
            coefficients.pop()
    return P(tuple(quotient)), P(tuple(coefficients))


def factor_power(poly: P, event: P):
    power = 0
    quotient = poly
    while True:
        candidate, remainder = divide_polynomials(quotient, event)
        if remainder != P.zero():
            return power, quotient
        quotient = candidate
        power += 1


def compare_root(poly: P, record):
    if poly.exact() != record["polynomial_exact"]:
        raise AssertionError("event polynomial coefficient mismatch")
    if canonical_hash(poly.exact()) != record["polynomial_digest"]:
        raise AssertionError("event polynomial digest mismatch")
    if poly.degree != record["polynomial_degree"]:
        raise AssertionError("event polynomial degree mismatch")
    verified = gx.verify_root_record(poly, record)
    if verified["hi"] - verified["lo"] > Q(1, 10**30):
        raise AssertionError("event root bracket is too wide")
    return verified


def checkpoint_guard_signs(points, faces):
    ledger = ex.mechanics_primitives(points, faces)
    checks = []
    for _name, quad, expected in TOPOLOGY_QUADS:
        poly_path = {
            i: tuple(P((coordinate,)) for coordinate in xyz)
            for i, xyz in points.items()
        }
        value = determinant_polynomial(poly_path, quad).eval(Q(0))
        checks.append((value, expected))
    face_component = ex.signed_face_components(
        ledger, tuple(sorted((6, 7, 245)))
    )[(7, 245)]
    checks.extend(
        (
            (ledger["vertex"][263][10], -1),
            (ledger["vertex"][1][54], -1),
            (ledger["vertex"][6][5], -1),
            (face_component, -1),
            (ledger["edge"][(7, 245)]["beta1"], -1),
        )
    )
    if ledger["vertex"][263][10] != ledger["edge"][(10, 263)]["one_minus_t"]:
        raise AssertionError("U263/H(10,263) identity mismatch")
    if ledger["vertex"][1][54] != ledger["edge"][(1, 54)]["t"]:
        raise AssertionError("U1/H(1,54) identity mismatch")
    if ledger["vertex"][6][5] != ledger["edge"][(5, 6)]["one_minus_t"]:
        raise AssertionError("U6/H(5,6) identity mismatch")
    edges = set(ledger["incidence"])
    for a, b in zip(ALT_ROUTE, ALT_ROUTE[1:]):
        if tuple(sorted((a, b))) not in edges:
            raise AssertionError("positive-dot route edge missing")
        checks.append((ex.dot(ledger["xscaled"][a], ledger["xscaled"][b]), 1))
    if any(not value or (1 if value > 0 else -1) != expected for value, expected in checks):
        raise AssertionError("checkpoint guard sign mismatch")


def verify_checkpoints(certificate):
    records = certificate["input_manifest"]["checkpoints"]
    if len(records) != len(CHECKPOINTS):
        raise AssertionError("checkpoint manifest length mismatch")
    for expected, (name, csv_path, face_path) in zip(records, CHECKPOINTS):
        if expected["name"] != name:
            raise AssertionError("checkpoint order mismatch")
        if expected["source_csv_sha256"] != sha256(csv_path):
            raise AssertionError((name, "checkpoint source hash mismatch"))
        if expected["face_file_sha256"] != sha256(face_path):
            raise AssertionError((name, "checkpoint face hash mismatch"))
        points, _repair = gx.read_repaired(csv_path)
        faces = json.loads(face_path.read_text())
        audit = gx.point_audit(points, faces)
        if gx.point_hash(points) != expected["coordinate_hash"]:
            raise AssertionError((name, "coordinate hash mismatch"))
        if canonical_hash(audit["support"]) != canonical_hash(expected["support"]):
            raise AssertionError((name, "support reconstruction mismatch"))
        if canonical_hash(audit["mechanics"]) != canonical_hash(expected["mechanics"]):
            raise AssertionError((name, "mechanics reconstruction mismatch"))
        if audit["support"]["f_vector"] != [61, 162, 103]:
            raise AssertionError((name, "wrong f-vector"))
        if audit["mechanics"]["class"] != [2, 2, 2]:
            raise AssertionError((name, "wrong class"))
        checkpoint_guard_signs(points, faces)


def guard_audit(path, faces, lo: Q, hi: Q, include_u6=True):
    ledger = ex.mechanics_primitives(path, faces)
    records = []

    def prove(name, poly, expected):
        packet = gx.exact_sign_record(poly, lo, hi, expected=expected, max_depth=60)
        records.append({"name": name, **packet})

    for name, quad, expected in TOPOLOGY_QUADS:
        prove(f"topology:{name}", determinant_polynomial(path, quad), expected)
    prove("guard:U263_H10_263", ledger["vertex"][263][10], -1)
    prove("guard:U1_H1_54", ledger["vertex"][1][54], -1)
    if include_u6:
        prove("guard:U6_H5_6", ledger["vertex"][6][5], -1)
    face_component = ex.signed_face_components(
        ledger, tuple(sorted((6, 7, 245)))
    )[(7, 245)]
    prove("guard:S6_7_245_component_7_245", face_component, -1)
    prove("guard:H7_245_beta1", ledger["edge"][(7, 245)]["beta1"], -1)
    for a, b in zip(ALT_ROUTE, ALT_ROUTE[1:]):
        prove(
            f"route_dot:{a},{b}",
            ex.dot(ledger["xscaled"][a], ledger["xscaled"][b]),
            1,
        )
    digest = hashlib.sha256()
    for record in records:
        digest.update(
            f"{record['name']}|{record['sign']}|{record['polynomial_digest']}\n".encode()
        )
    return {
        "interval": [ex.qs(lo), ex.qs(hi)],
        "record_count": len(records),
        "digest": digest.hexdigest(),
        "records": records,
    }


def support_event_dependencies(path, faces, event, lo: Q, hi: Q):
    _ledger, primitives = gx.all_primitives(path, faces)
    failed = []
    skipped = set()
    for name, poly, _positive in primitives:
        try:
            ex.bernstein_sign(poly, lo, hi, max_depth=60)
        except AssertionError:
            power, quotient = factor_power(poly, event)
            if not power:
                raise AssertionError(("independent primitive root", name))
            gx.exact_sign_record(quotient, lo, hi, max_depth=60)
            failed.append((name, power, poly.degree, canonical_hash(poly.exact())))
            skipped.add(name)
    audit = gx.audit_every_primitive(
        path, faces, lo, hi, skip=frozenset(skipped), max_depth=60
    )
    return failed, audit


def wall_support_digest(path, faces, event, lo: Q, hi: Q):
    incidence, _neighbors, _face_by_key = ex.edge_data(faces)
    active = set().union(*(set(face) for face in faces))
    if active != set(path):
        raise AssertionError("wall loses active rows")
    event_members = 0
    strict_count = 0
    digest = hashlib.sha256()
    all_labels = set(path)
    for face_index, cycle in enumerate(faces):
        normal = ex.cycle_normal(cycle, path)
        anchor = path[cycle[0]]
        for member in cycle[1:]:
            polynomial = ex.dot(normal, ex.sub(path[member], anchor))
            if polynomial == P.zero():
                continue
            power, quotient = factor_power(polynomial, event)
            if frozenset(cycle) != frozenset(EVENT_QUAD) or not power:
                raise AssertionError("wall coplanarity is not the isolated event")
            gx.exact_sign_record(quotient, lo, hi, max_depth=60)
            event_members += 1
        face_sign = None
        for witness in sorted(all_labels - set(cycle)):
            polynomial = ex.dot(normal, ex.sub(path[witness], anchor))
            packet = gx.exact_sign_record(polynomial, lo, hi, max_depth=60)
            if face_sign is None:
                face_sign = packet["sign"]
            elif packet["sign"] != face_sign:
                raise AssertionError("mixed exact wall support")
            name = f"wall_support:f{face_index}:w{witness}"
            digest.update(
                f"{name}|{packet['sign']}|{packet['polynomial_digest']}\n".encode()
            )
            strict_count += 1
    if event_members != 1:
        raise AssertionError("wrong event-wall member count")
    return {
        "f_vector": [len(active), len(incidence), len(faces)],
        "strict_support_polynomial_count": strict_count,
        "strict_support_digest": digest.hexdigest(),
    }


def assert_exact_csv(path: Path, expected_points):
    actual = ex.read_rows(path)
    if actual != expected_points:
        raise AssertionError(("exact CSV reconstruction mismatch", path.name))


def main() -> None:
    certificate = json.loads(CERTIFICATE.read_text())
    if certificate["verdict"] != (
        "NONWINNER_MATERIAL_EXACT_SUPPORT_EVENT_AND_NEXT_MECHANICS_OBSTRUCTION"
    ):
        raise AssertionError("certificate verdict changed")
    verify_checkpoints(certificate)

    pre, _ = gx.read_repaired(PRE_RAW)
    far, _ = gx.read_repaired(FAR_RAW)
    pre_faces = json.loads(PRE_FACES.read_text())
    wall_faces = json.loads(WALL_FACES.read_text())
    far_faces = json.loads(FAR_FACES.read_text())
    path = gx.planar_morph(pre, far)
    if path_digest(path) != certificate["construction"]["path_polynomial_digest"]:
        raise AssertionError("path reconstruction digest mismatch")
    assert_exact_csv(HERE / "exact_event_chain_pre.csv", pre)
    assert_exact_csv(HERE / "exact_event_chain_far.csv", far)
    recovered, _ = gx.read_repaired(HERE / "birth6_guard_buffer_source.csv")
    assert_exact_csv(HERE / "recovered_guarded_continuation.csv", recovered)

    support = certificate["first_support_event"]
    support_poly = determinant_polynomial(path, EVENT_QUAD)
    support_verified = compare_root(support_poly, support["root"])
    support_lo, support_hi = support_verified["lo"], support_verified["hi"]

    pre_audit = gx.audit_every_primitive(
        path, pre_faces, Q(0), support_lo, max_depth=60
    )
    if pre_audit != certificate["strict_pre_cell"]["all_primitives"]:
        raise AssertionError("strict pre-cell primitive audit mismatch")
    if guard_audit(path, pre_faces, Q(0), support_lo) != certificate[
        "strict_pre_cell"
    ]["guards"]:
        raise AssertionError("strict pre-cell guard audit mismatch")

    pre_failed, pre_other = support_event_dependencies(
        path, pre_faces, support_poly, support_lo, support_hi
    )
    far_failed, far_other = support_event_dependencies(
        path, far_faces, support_poly, support_lo, support_hi
    )
    expected_pre = [
        (
            row["name"],
            row["event_factor_power"],
            row["polynomial_degree"],
            row["polynomial_digest"],
        )
        for row in support["pre_topology_dependent_primitives"]
    ]
    expected_far = [
        (
            row["name"],
            row["event_factor_power"],
            row["polynomial_degree"],
            row["polynomial_digest"],
        )
        for row in support["far_topology_dependent_primitives"]
    ]
    if pre_failed != expected_pre or far_failed != expected_far:
        raise AssertionError("support-event factorization mismatch")
    if pre_other != support["pre_all_other_primitives"]:
        raise AssertionError("pre wall-bracket ledger mismatch")
    if far_other != support["far_all_other_primitives"]:
        raise AssertionError("far wall-bracket ledger mismatch")

    wall = wall_support_digest(path, wall_faces, support_poly, support_lo, support_hi)
    if wall["f_vector"] != support["wall_support"]["f_vector"]:
        raise AssertionError("wall f-vector mismatch")
    if wall["strict_support_polynomial_count"] != support["wall_support"][
        "strict_support_polynomial_count"
    ]:
        raise AssertionError("wall support count mismatch")
    if wall["strict_support_digest"] != support["wall_support"][
        "strict_support_digest"
    ]:
        raise AssertionError("wall support digest mismatch")
    wall_mechanics = ex.certify_mechanics_interval(
        path, wall_faces, PROTECTED, support_lo, support_hi
    )
    if wall_mechanics != support["wall_mechanics"]:
        raise AssertionError("wall mechanics mismatch")
    if guard_audit(path, wall_faces, support_lo, support_hi) != support[
        "wall_guards"
    ]:
        raise AssertionError("wall guard mismatch")

    next_event = certificate["next_mechanics_event"]
    far_ledger = ex.mechanics_primitives(path, far_faces)
    next_poly = far_ledger["vertex"][6][5]
    if next_poly != far_ledger["edge"][(5, 6)]["one_minus_t"]:
        raise AssertionError("next common-numerator identity mismatch")
    next_verified = compare_root(next_poly, next_event["root"])
    next_lo, next_hi = next_verified["lo"], next_verified["hi"]
    if not support_hi < Q(1) < next_lo:
        raise AssertionError("event ordering mismatch")

    far_audit = gx.audit_every_primitive(
        path, far_faces, support_hi, next_lo, max_depth=60
    )
    if far_audit != certificate["strict_far_cell_until_next_event"][
        "all_primitives"
    ]:
        raise AssertionError("strict far-cell primitive audit mismatch")
    if guard_audit(path, far_faces, support_hi, next_lo) != certificate[
        "strict_far_cell_until_next_event"
    ]["guards"]:
        raise AssertionError("strict far-cell guard audit mismatch")

    skipped = frozenset(("vertex:6:5", "edge:5,6:one_minus_t"))
    next_other = gx.audit_every_primitive(
        path, far_faces, next_lo, next_hi, skip=skipped, max_depth=60
    )
    if next_other != next_event["all_other_primitives_on_root_bracket"]:
        raise AssertionError("next-event bracket audit mismatch")
    if guard_audit(path, far_faces, next_lo, next_hi, include_u6=False) != next_event[
        "remaining_guards_on_root_bracket"
    ]:
        raise AssertionError("next-event remaining guards mismatch")

    pre_points = gx.evaluate_path(path, next_lo)
    post_points = gx.evaluate_path(path, next_hi)
    pre_point = gx.point_audit(pre_points, far_faces)
    post_point = gx.point_audit(post_points, far_faces)
    if (
        canonical_hash(pre_point) != canonical_hash(next_event["pre"])
        or canonical_hash(post_point) != canonical_hash(next_event["post"])
    ):
        raise AssertionError("next-event endpoint reconstruction mismatch")
    if pre_point["mechanics"]["class"] != [2, 2, 2]:
        raise AssertionError("wrong next-event pre class")
    if post_point["mechanics"]["class"] != [2, 3, 3]:
        raise AssertionError("wrong next-event post class")
    assert_exact_csv(HERE / "exact_next_event_pre.csv", pre_points)
    assert_exact_csv(HERE / "exact_next_event_post.csv", post_points)
    assert_exact_csv(
        HERE / "exact_support_wall_locator.csv",
        gx.evaluate_path(path, (support_lo + support_hi) / 2),
    )

    for artifact, expected_hash in certificate["artifacts"].items():
        path_on_disk = ROOT / artifact
        if sha256(path_on_disk) != expected_hash:
            raise AssertionError(("artifact hash mismatch", artifact))

    summary = {
        "version": 1,
        "verdict": "INDEPENDENT_EXACT_ROUND12_EVENT_CHAIN_PASS",
        "certificate_sha256": sha256(CERTIFICATE),
        "checkpoint_count": len(CHECKPOINTS),
        "path_polynomial_digest": path_digest(path),
        "support_event": {
            "quad": list(EVENT_QUAD),
            "degree": support_poly.degree,
            "interval": [ex.qs(support_lo), ex.qs(support_hi)],
            "pre_dependent_primitive_count": len(pre_failed),
            "far_dependent_primitive_count": len(far_failed),
            "wall_f_vector": wall["f_vector"],
        },
        "strict_cells": {
            "pre_primitive_count": pre_audit["certified_polynomial_count"],
            "far_primitive_count": far_audit["certified_polynomial_count"],
        },
        "next_event": {
            "degree": next_poly.degree,
            "interval": [ex.qs(next_lo), ex.qs(next_hi)],
            "common_primitives": sorted(skipped),
            "class_transition": [[2, 2, 2], [2, 3, 3]],
        },
    }
    SUMMARY.write_text(json.dumps(summary, indent=2) + "\n")
    print("INDEPENDENT_EXACT_ROUND12_EVENT_CHAIN_PASS")
    print("certificate_sha256", summary["certificate_sha256"])
    print("support_event_degree", support_poly.degree)
    print("next_event_degree", next_poly.degree)
    print("class_transition", summary["next_event"]["class_transition"])


if __name__ == "__main__":
    main()
