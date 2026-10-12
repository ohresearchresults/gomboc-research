#!/usr/bin/env python3
"""Build the exact Round-12 FAR support-event and next-event certificate.

The exploratory files in this directory are finite-decimal checkpoints.  This
builder reads them as exact rationals, projects only the enlarged-base rows
onto their exact checkpoint base planes, and then defines one explicit
base-planarity-preserving rational polynomial path from the recovered strict
pre checkpoint to the strict far checkpoint.

The proof layer contains no floating-point predicate.  Every support row and
every face/vertex/four-component edge primitive is audited with exact
Fractions and Bernstein signs.  The first support event and the following
U6/H(5,6) mechanics event are isolated algebraically.
"""
from __future__ import annotations

import csv
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
EXPECTED_CLASS = [2, 2, 2]
PROTECTED = {
    "stable": [sorted(BASE), sorted(STABLE_TRIANGLE)],
    "unstable": [8, 54],
    "saddles": [[6, 7], [198, 263]],
}
ALT_ROUTE = (228, 198, 263, 9, 8)
TOPOLOGY_QUADS = (
    ("round4_far", (7, 8, 245, 246), -1),
    ("round8_pre", (9, 198, 263, 264), -1),
    ("round10_far", (8, 264, 246, 198), 1),
    ("round12_far", (198, 263, 262, 11), 1),
)
EVENT_QUAD = (6, 198, 244, 245)
EVENT_SEARCH = (Q(0), Q(1))
NEXT_SEARCH = (Q(11, 5), Q(23, 10))
ROOT_WIDTH = Q(1, 10**30)

PRE_RAW = HERE / "quad_6_198_244_245_event_pre.csv"
FAR_RAW = HERE / "quad_6_198_244_245_event_far.csv"
PRE_FACES = HERE / "quad_6_198_244_245_event_pre_faces.json"
WALL_FACES = HERE / "quad_6_198_244_245_event_wall_faces.json"
FAR_FACES = HERE / "quad_6_198_244_245_event_far_faces.json"
CERTIFICATE = HERE / "exact_event_chain_certificate.json"
EXACT_PRE = HERE / "exact_event_chain_pre.csv"
EXACT_FAR = HERE / "exact_event_chain_far.csv"
SUPPORT_LOCATOR = HERE / "exact_support_wall_locator.csv"
NEXT_PRE = HERE / "exact_next_event_pre.csv"
NEXT_POST = HERE / "exact_next_event_post.csv"
RECOVERED_GUARDED = HERE / "recovered_guarded_continuation.csv"


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


def local(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def write_exact_csv(path: Path, points) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(("source_id", "x", "y", "z"))
        for label in sorted(points):
            writer.writerow((label, *(ex.qs(value) for value in points[label])))


def restrict_path(path, lo: Q, hi: Q):
    return {
        label: tuple(coordinate.affine(lo, hi) for coordinate in xyz)
        for label, xyz in path.items()
    }


def determinant_polynomial(path, quad):
    a, b, c, d = (path[label] for label in quad)
    return ex.det3(ex.sub(b, a), ex.sub(c, a), ex.sub(d, a))


def polynomial_digest(poly: P) -> str:
    return canonical_hash(poly.exact())


def root_packet(poly: P, lo: Q, hi: Q):
    bracket = gx.root_record(poly, lo, hi, ROOT_WIDTH)
    return {
        **bracket,
        "polynomial_degree": poly.degree,
        "polynomial_exact": poly.exact(),
        "polynomial_digest": polynomial_digest(poly),
    }


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


def event_factorization(poly: P, event: P, lo: Q, hi: Q):
    power = 0
    quotient = poly
    while True:
        candidate, remainder = divide_polynomials(quotient, event)
        if remainder != P.zero():
            break
        quotient = candidate
        power += 1
    if not power:
        raise AssertionError("event primitive is not divisible by event polynomial")
    quotient_sign = gx.exact_sign_record(quotient, lo, hi, max_depth=60)
    return {
        "event_factor_power": power,
        "quotient_degree": quotient.degree,
        "quotient_polynomial_digest": polynomial_digest(quotient),
        "quotient_sign": quotient_sign,
    }


def exact_scalar_record(value: Q, expected_sign: int):
    sign = 1 if value > 0 else -1 if value < 0 else 0
    if sign != expected_sign:
        raise AssertionError(("wrong exact checkpoint sign", sign, expected_sign))
    return {
        "sign": sign,
        "exact": ex.qs(value),
        "log10_abs": ex.qlog10(value),
    }


def point_guard_packet(points, faces):
    ledger = ex.mechanics_primitives(points, faces)
    face_component = ex.signed_face_components(
        ledger, tuple(sorted((6, 7, 245)))
    )[(7, 245)]
    topology = {}
    for name, quad, expected in TOPOLOGY_QUADS:
        value = determinant_polynomial(
            {i: tuple(P((x,)) for x in xyz) for i, xyz in points.items()}, quad
        ).eval(Q(0))
        topology[name] = exact_scalar_record(value, expected)
    shared = {
        "U263_H10_263_absent": exact_scalar_record(
            ledger["vertex"][263][10], -1
        ),
        "U1_H1_54_absent": exact_scalar_record(
            ledger["vertex"][1][54], -1
        ),
        "U6_H5_6_absent": exact_scalar_record(
            ledger["vertex"][6][5], -1
        ),
        "S6_7_245_component_7_245_negative": exact_scalar_record(
            face_component, -1
        ),
        "H7_245_beta1_negative": exact_scalar_record(
            ledger["edge"][(7, 245)]["beta1"], -1
        ),
    }
    if ledger["vertex"][263][10] != ledger["edge"][(10, 263)]["one_minus_t"]:
        raise AssertionError("U263/H(10,263) exact identity failed")
    if ledger["vertex"][1][54] != ledger["edge"][(1, 54)]["t"]:
        raise AssertionError("U1/H(1,54) exact identity failed")
    if ledger["vertex"][6][5] != ledger["edge"][(5, 6)]["one_minus_t"]:
        raise AssertionError("U6/H(5,6) exact identity failed")
    edges = set(ledger["incidence"])
    route = []
    for a, b in zip(ALT_ROUTE, ALT_ROUTE[1:]):
        edge = tuple(sorted((a, b)))
        if edge not in edges:
            raise AssertionError(("missing alternate-route edge", edge))
        value = ex.dot(ledger["xscaled"][a], ledger["xscaled"][b])
        route.append({"edge": list(edge), **exact_scalar_record(value, 1)})
    return {
        "topology_sides": topology,
        "accumulated_mechanics_guards": shared,
        "positive_dot_route": route,
    }


def checkpoint_audit(name: str, csv_path: Path, face_path: Path):
    points, repair = gx.read_repaired(csv_path)
    faces = json.loads(face_path.read_text())
    audit = gx.point_audit(points, faces)
    if len(points) != 61:
        raise AssertionError((name, "wrong row count", len(points)))
    if audit["support"]["active_labels"] != sorted(points):
        raise AssertionError((name, "inactive exact row"))
    if audit["support"]["f_vector"] != [61, 162, 103]:
        raise AssertionError((name, "wrong f-vector", audit["support"]["f_vector"]))
    if audit["mechanics"]["class"] != EXPECTED_CLASS:
        raise AssertionError((name, "wrong class", audit["mechanics"]))
    face_keys = {frozenset(face) for face in faces}
    if BASE not in face_keys or STABLE_TRIANGLE not in face_keys:
        raise AssertionError((name, "protected stable face missing"))
    if audit["mechanics"]["unstable_vertices"] != [8, 54]:
        raise AssertionError((name, "U8/U54 not preserved"))
    return points, {
        "name": name,
        "source_csv": local(csv_path),
        "source_csv_sha256": sha256(csv_path),
        "face_file": local(face_path),
        "face_file_sha256": sha256(face_path),
        "face_ledger_digest": gx.canonical_hash(faces),
        "base_repair": repair,
        "coordinate_hash": gx.point_hash(points),
        "support": audit["support"],
        "mechanics": audit["mechanics"],
        "guards": point_guard_packet(points, faces),
    }


def interval_guard_packet(path, faces, lo: Q, hi: Q, include_u6=True):
    ledger = ex.mechanics_primitives(path, faces)
    records = []

    def prove(name: str, poly: P, expected: int):
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


def failed_primitive_factorizations(path, faces, event, lo: Q, hi: Q):
    _ledger, primitives = gx.all_primitives(path, faces)
    failed = []
    skipped = set()
    for name, poly, _intrinsically_positive in primitives:
        try:
            ex.bernstein_sign(poly, lo, hi, max_depth=60)
        except AssertionError:
            skipped.add(name)
            failed.append(
                {
                    "name": name,
                    "polynomial_degree": poly.degree,
                    "polynomial_digest": polynomial_digest(poly),
                    **event_factorization(poly, event, lo, hi),
                }
            )
    if len(failed) != 5:
        raise AssertionError(("unexpected support-event primitive count", failed))
    audit = gx.audit_every_primitive(
        path, faces, lo, hi, skip=frozenset(skipped), max_depth=60
    )
    return failed, audit


def wall_support_audit(path, faces, event, lo: Q, hi: Q):
    incidence, _neighbors, _face_by_key = ex.edge_data(faces)
    active = set().union(*(set(face) for face in faces))
    if active != set(path):
        raise AssertionError("wall ledger loses an input row")
    event_members = []
    support_records = []
    digest = hashlib.sha256()
    all_labels = set(path)
    for face_index, cycle in enumerate(faces):
        normal = ex.cycle_normal(cycle, path)
        anchor = path[cycle[0]]
        local_event_members = []
        for member in cycle[1:]:
            polynomial = ex.dot(normal, ex.sub(path[member], anchor))
            if polynomial == P.zero():
                continue
            factor = event_factorization(polynomial, event, lo, hi)
            local_event_members.append(
                {
                    "face_index": face_index,
                    "face": list(cycle),
                    "member": member,
                    **factor,
                }
            )
        if local_event_members:
            if frozenset(cycle) != frozenset(EVENT_QUAD):
                raise AssertionError(("unexpected algebraic wall face", cycle))
            event_members.extend(local_event_members)
        face_sign = None
        for witness in sorted(all_labels - set(cycle)):
            polynomial = ex.dot(normal, ex.sub(path[witness], anchor))
            packet = gx.exact_sign_record(polynomial, lo, hi, max_depth=60)
            if face_sign is None:
                face_sign = packet["sign"]
            elif packet["sign"] != face_sign:
                raise AssertionError(("mixed wall support", face_index, witness))
            name = f"wall_support:f{face_index}:w{witness}"
            digest.update(
                f"{name}|{packet['sign']}|{packet['polynomial_digest']}\n".encode()
            )
            support_records.append({"name": name, **packet})
    if len(event_members) != 1:
        raise AssertionError(("wrong algebraic wall-member count", event_members))
    quad = next(face for face in faces if frozenset(face) == frozenset(EVENT_QUAD))
    quad_normal = ex.cycle_normal(quad, path)
    noncollinear = gx.exact_sign_record(
        ex.norm2(quad_normal), lo, hi, expected=1, max_depth=60
    )
    return {
        "f_vector": [len(active), len(incidence), len(faces)],
        "euler": len(active) - len(incidence) + len(faces),
        "active_labels": sorted(active),
        "event_quad_cycle": list(quad),
        "event_member_factorization": event_members[0],
        "event_quad_noncollinearity": noncollinear,
        "strict_support_polynomial_count": len(support_records),
        "strict_support_digest": digest.hexdigest(),
        "minimum_support_log10_abs": min(
            record["min_bernstein_coefficient_log10_abs"]
            for record in support_records
        ),
    }


def mechanics_event_packet(path, faces, lo: Q, hi: Q):
    ledger = ex.mechanics_primitives(path, faces)
    vertex = ledger["vertex"][6][5]
    edge = ledger["edge"][(5, 6)]["one_minus_t"]
    if vertex != edge:
        raise AssertionError("U6/H(5,6) common numerator identity failed")
    root = root_packet(vertex, lo, hi)
    root_lo, root_hi = Q(root["lo"]), Q(root["hi"])
    skipped = frozenset(("vertex:6:5", "edge:5,6:one_minus_t"))
    bracket_audit = gx.audit_every_primitive(
        path, faces, root_lo, root_hi, skip=skipped, max_depth=60
    )
    pre_points = gx.evaluate_path(path, root_lo)
    post_points = gx.evaluate_path(path, root_hi)
    pre = gx.point_audit(pre_points, faces)
    post = gx.point_audit(post_points, faces)
    if pre["mechanics"]["class"] != [2, 2, 2]:
        raise AssertionError(("wrong next-event pre class", pre))
    if post["mechanics"]["class"] != [2, 3, 3]:
        raise AssertionError(("wrong next-event post class", post))
    if pre["support"]["f_vector"] != [61, 162, 103]:
        raise AssertionError("next-event pre support changed")
    if post["support"]["f_vector"] != [61, 162, 103]:
        raise AssertionError("next-event post support changed")
    return {
        "type": "simultaneous U6 and H(5,6) birth",
        "common_primitives": sorted(skipped),
        "common_polynomial_identity": True,
        "root": root,
        "all_other_primitives_on_root_bracket": bracket_audit,
        "pre": pre,
        "post": post,
        "class_transition": [[2, 2, 2], [2, 3, 3]],
    }, pre_points, post_points


def main() -> None:
    checkpoint_records = []
    recovered_guarded_points = None
    for name, csv_path, face_path in CHECKPOINTS:
        points, record = checkpoint_audit(name, csv_path, face_path)
        checkpoint_records.append(record)
        if name == "guarded_continuation_recovered":
            recovered_guarded_points = points
    if recovered_guarded_points is None:
        raise AssertionError("recovered guarded checkpoint missing")
    write_exact_csv(RECOVERED_GUARDED, recovered_guarded_points)

    pre, pre_repair = gx.read_repaired(PRE_RAW)
    far, far_repair = gx.read_repaired(FAR_RAW)
    pre_faces = json.loads(PRE_FACES.read_text())
    wall_faces = json.loads(WALL_FACES.read_text())
    far_faces = json.loads(FAR_FACES.read_text())
    path = gx.planar_morph(pre, far)
    write_exact_csv(EXACT_PRE, pre)
    write_exact_csv(EXACT_FAR, far)

    event_polynomial = determinant_polynomial(path, EVENT_QUAD)
    support_root = root_packet(event_polynomial, *EVENT_SEARCH)
    support_lo, support_hi = Q(support_root["lo"]), Q(support_root["hi"])

    pre_every = gx.audit_every_primitive(
        path, pre_faces, Q(0), support_lo, max_depth=60
    )
    pre_guards = interval_guard_packet(path, pre_faces, Q(0), support_lo)
    pre_failed, pre_bracket = failed_primitive_factorizations(
        path, pre_faces, event_polynomial, support_lo, support_hi
    )
    far_failed, far_bracket = failed_primitive_factorizations(
        path, far_faces, event_polynomial, support_lo, support_hi
    )
    wall_support = wall_support_audit(
        path, wall_faces, event_polynomial, support_lo, support_hi
    )
    if wall_support["f_vector"] != [61, 161, 102]:
        raise AssertionError(("wrong exact wall f-vector", wall_support))
    wall_mechanics = ex.certify_mechanics_interval(
        path, wall_faces, PROTECTED, support_lo, support_hi
    )
    wall_guards = interval_guard_packet(
        path, wall_faces, support_lo, support_hi
    )

    mechanics_event, next_pre_points, next_post_points = mechanics_event_packet(
        path, far_faces, *NEXT_SEARCH
    )
    mechanics_lo = Q(mechanics_event["root"]["lo"])
    if not support_hi < Q(1) < mechanics_lo:
        raise AssertionError("event order changed")
    far_every = gx.audit_every_primitive(
        path, far_faces, support_hi, mechanics_lo, max_depth=60
    )
    far_guards = interval_guard_packet(
        path, far_faces, support_hi, mechanics_lo
    )
    next_bracket_guards = interval_guard_packet(
        path,
        far_faces,
        Q(mechanics_event["root"]["lo"]),
        Q(mechanics_event["root"]["hi"]),
        include_u6=False,
    )

    write_exact_csv(
        SUPPORT_LOCATOR,
        gx.evaluate_path(path, (support_lo + support_hi) / 2),
    )
    write_exact_csv(NEXT_PRE, next_pre_points)
    write_exact_csv(NEXT_POST, next_post_points)

    pre_keys = {frozenset(face) for face in pre_faces}
    far_keys = {frozenset(face) for face in far_faces}
    construction_digest = canonical_hash(
        {
            str(label): [coordinate.exact() for coordinate in path[label]]
            for label in sorted(path)
        }
    )
    certificate = {
        "version": 1,
        "verdict": "NONWINNER_MATERIAL_EXACT_SUPPORT_EVENT_AND_NEXT_MECHANICS_OBSTRUCTION",
        "scope": (
            "exact recovery of Round-12 FAR checkpoints, first support event, "
            "and continuation to the next mechanics event"
        ),
        "input_manifest": {
            "checkpoint_count": len(checkpoint_records),
            "checkpoints": checkpoint_records,
        },
        "construction": {
            "type": "exact rational moving-base planar morph",
            "source_raw": local(PRE_RAW),
            "source_raw_sha256": sha256(PRE_RAW),
            "far_raw": local(FAR_RAW),
            "far_raw_sha256": sha256(FAR_RAW),
            "pre_base_repair": pre_repair,
            "far_base_repair": far_repair,
            "pre_coordinate_hash": gx.point_hash(pre),
            "far_coordinate_hash": gx.point_hash(far),
            "path_polynomial_digest": construction_digest,
            "base_coplanarity_exact_for_all_parameters": True,
            "row_count": len(pre),
        },
        "strict_pre_cell": {
            "interval": ["0", support_root["lo"]],
            "all_primitives": pre_every,
            "guards": pre_guards,
        },
        "first_support_event": {
            "quad": list(EVENT_QUAD),
            "root": support_root,
            "pre_topology_dependent_primitives": pre_failed,
            "far_topology_dependent_primitives": far_failed,
            "pre_all_other_primitives": pre_bracket,
            "far_all_other_primitives": far_bracket,
            "wall_support": wall_support,
            "wall_mechanics": wall_mechanics,
            "wall_guards": wall_guards,
            "wall_f_vector": [61, 161, 102],
            "removed_faces": sorted(
                sorted(face) for face in pre_keys - far_keys
            ),
            "added_faces": sorted(
                sorted(face) for face in far_keys - pre_keys
            ),
            "class_transition": [[2, 2, 2], [2, 2, 2]],
        },
        "strict_far_cell_until_next_event": {
            "interval": [support_root["hi"], mechanics_event["root"]["lo"]],
            "all_primitives": far_every,
            "guards": far_guards,
            "class": [2, 2, 2],
            "f_vector": [61, 162, 103],
        },
        "next_mechanics_event": {
            **mechanics_event,
            "remaining_guards_on_root_bracket": next_bracket_guards,
            "obstruction": (
                "the accumulated U6/H(5,6) no-birth guard reaches its unique "
                "common algebraic root; the strict far cell changes to class (2,3,3)"
            ),
        },
        "artifacts": {},
        "nonwinner_reason": (
            "the exact open cells remain (2,2,2); the next event creates U6 and "
            "H(5,6), producing (2,3,3), not (1,1,0)"
        ),
    }
    generated = (
        RECOVERED_GUARDED,
        EXACT_PRE,
        EXACT_FAR,
        SUPPORT_LOCATOR,
        NEXT_PRE,
        NEXT_POST,
        PRE_FACES,
        WALL_FACES,
        FAR_FACES,
    )
    certificate["artifacts"] = {
        local(path): sha256(path) for path in generated
    }
    CERTIFICATE.write_text(json.dumps(certificate, indent=2) + "\n")
    print("EXACT_ROUND12_QUAD_EVENT_AND_U6_H56_OBSTRUCTION_PASS")
    print("support_root", support_root["decimal_interval"])
    print("next_root", mechanics_event["root"]["decimal_interval"])
    print("strict_pre_primitives", pre_every["certified_polynomial_count"])
    print("strict_far_primitives", far_every["certified_polynomial_count"])
    print("checkpoint_count", len(checkpoint_records))


if __name__ == "__main__":
    main()
