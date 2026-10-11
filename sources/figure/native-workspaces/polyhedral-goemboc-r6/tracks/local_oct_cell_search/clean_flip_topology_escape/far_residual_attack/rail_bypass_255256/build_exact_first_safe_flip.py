#!/usr/bin/env python3
"""Certify the first rail-preserving boundary of the full-control route.

The certificate is exact for the rational-affine 165-control line from the
frozen own-centroid source through the algebraic circuit wall
{224,248,249,250}.  It proves complete support and mechanics ledgers on both
strict cells, the exact wall zero family, own uniform-volume centroids, the
unchanged (2,2,2) class, all 61 active rows, the enlarged base, all 37 rails,
strict active-residual descent, and strict separation from the rejected
{69,224,255,256} rail wall.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import sys
from fractions import Fraction as Q
from pathlib import Path


sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
ROOT = HERE.parents[4]
EXACT_CORE = ROOT / "tracks/global_carrier_support/rigorous_local_bypass"
sys.path.insert(0, str(EXACT_CORE))

import exact_core as ex  # noqa: E402


SOURCE = PARENT / "exact_event_source.csv"
SOURCE_FACES = PARENT / "exact_event_source_faces.json"
REJECTED_EVENT_CERTIFICATE = PARENT / "exact_event_certificate.json"
PROPOSAL = HERE / "full_control_search.json"
PATH_DEFINITION = HERE / "exact_full_control_path.json"
PRE_FACES_PATH = HERE / "exact_support_cell_0_faces.json"
WALL_FACES_PATH = HERE / "exact_support_event_0_wall_faces.json"
POST_FACES_PATH = HERE / "exact_support_cell_1_faces.json"

CERTIFICATE = HERE / "exact_first_safe_flip_certificate.json"
PRE_OUT = HERE / "exact_first_safe_flip_pre.csv"
POST_OUT = HERE / "exact_first_safe_flip_post.csv"
FAR_OUT = HERE / "exact_first_safe_flip_far.csv"

ROOT_WIDTH = Q(1, 10**30)
ROOT_BRACKET = (Q("0.3267"), Q("0.3268"))
FAR_PARAMETER = Q(7, 20)
BASE = frozenset(range(17)) | {54}
TARGET_FACE = (198, 243, 245)
PROTECTED = {
    "stable": [sorted(BASE), list(TARGET_FACE)],
    "unstable": [1, 8],
    "saddles": [[4, 5], [12, 13]],
}
EXPECTED_ACTIVE = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    54, 69, 72, 73, 88, 198, 224, 228, 229, 230, 231, 232, 233, 234,
    235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247,
    248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260,
    261, 262, 263, 264,
]
EVENT_CIRCUIT = (224, 248, 249, 250)
REMOVED_FACES = {(224, 249, 248), (224, 250, 249)}
ADDED_FACES = {(224, 250, 248), (248, 250, 249)}
REMOVED_EDGE = (224, 249)
ADDED_EDGE = (248, 250)
TARGET_SUPPORT = (94, 250)
EXPECTED_EVENT_FAMILY = {
    "support:f94:w250",
    "support:f101:w248",
    "edge:(224, 249):gram",
    "edge:(224, 249):beta1",
    "edge:(224, 249):beta2",
}
ACTIVE_RESIDUALS = {
    "S[198,243,245]": ("face", (198, 243)),
    "U1": ("vertex", 2),
    "H(4,5)": ("edge45", "one_minus_t"),
    "H(12,13)": ("edge1213", "one_minus_t"),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def write_exact_csv(path: Path, points) -> None:
    with path.open("w", newline="") as stream:
        out = csv.writer(stream)
        out.writerow(("source_id", "x", "y", "z"))
        for label in sorted(points):
            out.writerow((label, *(ex.qs(value) for value in points[label])))


def evaluate_path(path, parameter: Q):
    return {
        label: tuple(coordinate.eval(parameter) for coordinate in xyz)
        for label, xyz in path.items()
    }


def restrict_path(path, lo: Q, hi: Q):
    return {
        label: tuple(coordinate.affine(lo, hi) for coordinate in xyz)
        for label, xyz in path.items()
    }


def forced_rails():
    rails = set()
    for route in (
        [228, *range(229, 247), 8],
        [228, *range(247, 265), 8],
    ):
        rails.update(tuple(sorted(edge)) for edge in zip(route, route[1:]))
    rails.remove((228, 229))
    if len(rails) != 37:
        raise AssertionError(len(rails))
    return rails


def edge_set(faces):
    return set(ex.edge_data(faces)[0])


def face_key_set(faces):
    return {tuple(sorted(face)) for face in faces}


def primitive_rows(path, faces):
    ledger = ex.mechanics_primitives(path, faces)
    yield "volume_d6", ledger["d6"], "mechanics_denominator", True
    for face_index, witness, polynomial in ex.support_polynomials(path, faces):
        yield f"support:f{face_index}:w{witness}", polynomial, "support", False
    for face_key, values in sorted(ledger["reference"].items()):
        for edge, polynomial in sorted(values.items()):
            yield (
                f"face_reference:{face_key}:{edge}",
                polynomial,
                "mechanics_denominator",
                False,
            )
    for face_key, values in sorted(ledger["face"].items()):
        for edge, polynomial in sorted(values.items()):
            yield f"face_raw:{face_key}:{edge}", polynomial, "face_component", False
    for vertex, values in sorted(ledger["vertex"].items()):
        for neighbor, polynomial in sorted(values.items()):
            yield f"vertex:{vertex}:{neighbor}", polynomial, "vertex_component", False
    for edge, values in sorted(ledger["edge"].items()):
        for component in (
            "direction_norm2",
            "gram",
            "t",
            "one_minus_t",
            "beta1",
            "beta2",
        ):
            intrinsic = component in {"direction_norm2", "gram"}
            yield (
                f"edge:{edge}:{component}",
                values[component],
                "edge_component",
                intrinsic,
            )


def trim(coefficients):
    out = list(coefficients)
    while len(out) > 1 and not out[-1]:
        out.pop()
    return out or [Q(0)]


def divmod_poly(left, right):
    numerator = trim(left)
    denominator = trim(right)
    if denominator == [Q(0)]:
        raise ZeroDivisionError
    quotient = [Q(0)] * max(1, len(numerator) - len(denominator) + 1)
    while len(numerator) >= len(denominator) and numerator != [Q(0)]:
        shift = len(numerator) - len(denominator)
        factor = numerator[-1] / denominator[-1]
        quotient[shift] += factor
        for index, coefficient in enumerate(denominator):
            numerator[index + shift] -= factor * coefficient
        numerator = trim(numerator)
    return trim(quotient), numerator


def monic_gcd(first: ex.P, second: ex.P):
    left, right = trim(first.c), trim(second.c)
    while right != [Q(0)]:
        _quotient, remainder = divmod_poly(left, right)
        left, right = right, remainder
    leading = left[-1]
    return ex.P(tuple(value / leading for value in left))


def root_record(polynomial, root):
    return {
        "lo": ex.qs(root["lo"]),
        "hi": ex.qs(root["hi"]),
        "decimal_interval": [float(root["lo"]), float(root["hi"])],
        "value_lo": ex.qs(root["value_lo"]),
        "value_hi": ex.qs(root["value_hi"]),
        "derivative_sign": root["derivative_sign"],
        "derivative_bernstein_leaves": root["derivative_bernstein_leaves"],
        "polynomial_degree": polynomial.degree,
        "polynomial_exact": polynomial.exact(),
        "polynomial_digest": canonical_hash(polynomial.exact()),
    }


def strict_interval(rows, lo: Q, hi: Q):
    digest = hashlib.sha256()
    count = 0
    leaves = 0
    worst = None
    sign_counts = {"positive": 0, "negative": 0}
    family_counts = {}
    for name, polynomial, family, intrinsic_positive in rows:
        sign, row_leaves, margin = ex.bernstein_sign(
            polynomial, lo, hi, max_depth=60
        )
        if intrinsic_positive and sign != 1:
            raise AssertionError(("nonpositive intrinsic primitive", name))
        count += 1
        leaves += row_leaves
        worst = margin if worst is None else min(worst, margin)
        sign_counts["positive" if sign > 0 else "negative"] += 1
        family_counts[family] = family_counts.get(family, 0) + 1
        digest.update(
            f"{name}|{family}|{sign}|{'|'.join(polynomial.exact())}\n".encode()
        )
    return {
        "lo": ex.qs(lo),
        "hi": ex.qs(hi),
        "primitive_count": count,
        "family_counts": family_counts,
        "sign_counts": sign_counts,
        "bernstein_leaf_count": leaves,
        "minimum_bernstein_log10_abs": worst,
        "primitive_digest": digest.hexdigest(),
    }


def event_audit(rows, target, root):
    lookup = {
        name: (polynomial, family)
        for name, polynomial, family, _intrinsic in rows
    }
    if not EXPECTED_EVENT_FAMILY.issubset(lookup):
        raise AssertionError(
            ("missing expected wall family", sorted(EXPECTED_EVENT_FAMILY - set(lookup)))
        )
    shared = {}
    for name in sorted(EXPECTED_EVENT_FAMILY):
        polynomial, family = lookup[name]
        gcd = monic_gcd(target, polynomial)
        if gcd.degree < 1:
            raise AssertionError((name, "does not share event factor"))
        isolated = ex.isolate_monotone_root(
            gcd, root["lo"], root["hi"], ROOT_WIDTH
        )
        shared[name] = {
            "family": family,
            "polynomial_degree": polynomial.degree,
            "polynomial_digest": canonical_hash(polynomial.exact()),
            "gcd_degree": gcd.degree,
            "gcd_exact": gcd.exact(),
            "gcd_digest": canonical_hash(gcd.exact()),
            "gcd_root_interval": [ex.qs(isolated["lo"]), ex.qs(isolated["hi"])],
        }

    strict_count = 0
    strict_leaves = 0
    worst = None
    accidental = []
    for name, polynomial, _family, _intrinsic in rows:
        if name in EXPECTED_EVENT_FAMILY:
            continue
        try:
            _sign, leaves, margin = ex.bernstein_sign(
                polynomial, root["lo"], root["hi"], max_depth=60
            )
        except AssertionError:
            gcd = monic_gcd(target, polynomial)
            if gcd.degree >= 1:
                accidental.append(name)
            raise
        strict_count += 1
        strict_leaves += leaves
        worst = margin if worst is None else min(worst, margin)
    if accidental:
        raise AssertionError(("unexpected event family", accidental))
    return {
        "allowed_zero_family": sorted(EXPECTED_EVENT_FAMILY),
        "shared_algebraic_factor": shared,
        "strict_other_primitive_count": strict_count,
        "strict_other_bernstein_leaf_count": strict_leaves,
        "strict_other_minimum_bernstein_log10_abs": worst,
    }


def checkpoint(points, faces):
    support = ex.supporting_cell(points, faces)
    _ledger, mechanics = ex.classify_point(points, faces)
    if support["f_vector"] != [61, 162, 103]:
        raise AssertionError(support)
    if support["active_labels"] != EXPECTED_ACTIVE:
        raise AssertionError(("active rows", support["active_labels"]))
    if mechanics["class"] != [2, 2, 2]:
        raise AssertionError(mechanics)
    if BASE not in {frozenset(face) for face in faces}:
        raise AssertionError("enlarged base missing")
    edges = set(map(tuple, support["edges"]))
    missing = sorted(forced_rails() - edges)
    if missing:
        raise AssertionError(("rails missing", missing))
    d6, m24 = ex.exact_centroid_numerators(points, faces)
    if d6 <= 0:
        raise AssertionError("nonpositive exact volume")
    centroid = tuple(value / (4 * d6) for value in m24)
    constant = {
        label: tuple(ex.P((value,)) for value in xyz)
        for label, xyz in points.items()
    }
    rows = list(primitive_rows(constant, faces))
    if any(not polynomial.eval(Q(0)) for _name, polynomial, _family, _intrinsic in rows):
        raise AssertionError("checkpoint has zero primitive")
    digest = hashlib.sha256()
    for name, polynomial, family, _intrinsic in rows:
        digest.update(f"{name}|{family}|{ex.qs(polynomial.eval(Q(0)))}\n".encode())
    return {
        "coordinate_hash": canonical_hash(
            {
                str(label): [ex.qs(value) for value in points[label]]
                for label in sorted(points)
            }
        ),
        "face_hash": canonical_hash(
            sorted(sorted(int(label) for label in face) for face in faces)
        ),
        "exact_centroid": [ex.qs(value) for value in centroid],
        "exact_centroid_digest": canonical_hash([ex.qs(value) for value in centroid]),
        "exact_support": {key: value for key, value in support.items() if key != "edges"},
        "exact_mechanics": mechanics,
        "true_edge_count": len(edges),
        "primitive_count": len(rows),
        "primitive_digest": digest.hexdigest(),
        "base_face_present": True,
        "forced_rail_count": len(forced_rails()),
        "missing_forced_rails": [],
    }


def residual_polynomials(path, faces):
    ledger = ex.mechanics_primitives(path, faces)
    face = ex.signed_face_components(ledger, tuple(sorted(TARGET_FACE)))
    return {
        "S[198,243,245]": face[(198, 243)],
        "U1": ledger["vertex"][1][2],
        "H(4,5)": ledger["edge"][(4, 5)]["one_minus_t"],
        "H(12,13)": ledger["edge"][(12, 13)]["one_minus_t"],
    }


def directed_residual_audit(path, pre_faces, post_faces, root, far):
    pre = residual_polynomials(path, pre_faces)
    post = residual_polynomials(path, post_faces)
    records = {}
    for name in ACTIVE_RESIDUALS:
        if pre[name].exact() != post[name].exact():
            raise AssertionError((name, "triangulation-dependent mechanics polynomial"))
        polynomial = pre[name]
        segments = {}
        for segment, lo, hi in (
            ("pre", Q(0), root["lo"]),
            ("wall_bracket", root["lo"], root["hi"]),
            ("post", root["hi"], far),
        ):
            positive = ex.bernstein_sign(polynomial, lo, hi, max_depth=60)
            derivative = ex.bernstein_sign(
                polynomial.derivative(), lo, hi, max_depth=60
            )
            if positive[0] != 1 or derivative[0] != -1:
                raise AssertionError((name, segment, positive, derivative))
            segments[segment] = {
                "positive_sign": positive[0],
                "positive_bernstein_leaves": positive[1],
                "positive_minimum_log10_abs": positive[2],
                "derivative_sign": derivative[0],
                "derivative_bernstein_leaves": derivative[1],
                "derivative_minimum_log10_abs": derivative[2],
            }
        source_value = polynomial.eval(Q(0))
        far_value = polynomial.eval(far)
        if not 0 < far_value < source_value:
            raise AssertionError((name, "not strictly improved"))
        records[name] = {
            "degree": polynomial.degree,
            "polynomial_digest": canonical_hash(polynomial.exact()),
            "segments": segments,
            "source_value": ex.qs(source_value),
            "far_value": ex.qs(far_value),
            "far_over_source_decimal": float(far_value / source_value),
            "strict_delta": ex.qs(source_value - far_value),
        }
    return records


def rejected_rail_guard(path, pre_faces, far):
    lookup = {
        (face_index, witness): polynomial
        for face_index, witness, polynomial in ex.support_polynomials(path, pre_faces)
    }
    records = {}
    for key in ((57, 69), (58, 224)):
        polynomial = lookup[key]
        sign0 = 1 if polynomial.eval(Q(0)) > 0 else -1
        oriented = ex.P(tuple(sign0 * value for value in polynomial.c))
        positive = ex.bernstein_sign(oriented, Q(0), far, max_depth=60)
        increasing = ex.bernstein_sign(
            oriented.derivative(), Q(0), far, max_depth=60
        )
        if positive[0] != 1 or increasing[0] != 1:
            raise AssertionError((key, "rejected rail wall not separated"))
        records[f"support:f{key[0]}:w{key[1]}"] = {
            "degree": oriented.degree,
            "polynomial_digest": canonical_hash(oriented.exact()),
            "source_value": ex.qs(oriented.eval(Q(0))),
            "far_value": ex.qs(oriented.eval(far)),
            "far_over_source_decimal": float(
                oriented.eval(far) / oriented.eval(Q(0))
            ),
            "positive_sign": positive[0],
            "positive_bernstein_leaves": positive[1],
            "derivative_sign": increasing[0],
            "derivative_bernstein_leaves": increasing[1],
        }
    return {
        "circuit": [69, 224, 255, 256],
        "mandatory_rail": [255, 256],
        "guard_type": "exact oriented circuit support strictly increasing",
        "support_representatives": records,
    }


def main() -> None:
    proposal = json.loads(PROPOSAL.read_text())
    if proposal["verdict"] != "FULL_CONTROL_RAIL_SEPARATING_PRIMAL_WITNESS_FOUND":
        raise AssertionError(proposal["verdict"])
    path_definition = json.loads(PATH_DEFINITION.read_text())
    source = ex.read_rows(SOURCE)
    velocity = {
        int(label): tuple(Q(value) for value in xyz)
        for label, xyz in path_definition["velocity"].items()
    }
    if set(source) != set(velocity):
        raise AssertionError("source/velocity labels differ")
    path = {
        label: tuple(
            ex.P((source[label][axis], velocity[label][axis])) for axis in range(3)
        )
        for label in source
    }
    pre_faces = json.loads(PRE_FACES_PATH.read_text())
    wall_faces = json.loads(WALL_FACES_PATH.read_text())
    post_faces = json.loads(POST_FACES_PATH.read_text())

    pre_rows = list(primitive_rows(path, pre_faces))
    post_rows = list(primitive_rows(path, post_faces))
    support_lookup = {
        (face_index, witness): polynomial
        for face_index, witness, polynomial in ex.support_polynomials(path, pre_faces)
    }
    target = support_lookup[TARGET_SUPPORT]
    root = ex.isolate_monotone_root(
        target, ROOT_BRACKET[0], ROOT_BRACKET[1], ROOT_WIDTH
    )
    if not root["hi"] < FAR_PARAMETER:
        raise AssertionError("empty post-wall interval")
    pre_parameter = root["lo"] - root["lo"] / 5
    post_parameter = root["hi"] + (FAR_PARAMETER - root["hi"]) / 3

    print("complete pre-cell primitive audit", flush=True)
    pre_interval = strict_interval(pre_rows, Q(0), root["lo"])
    pre_class_cover = ex.certify_path_segment(
        restrict_path(path, Q(0), root["lo"]), pre_faces, PROTECTED
    )
    print("exact algebraic wall audit", flush=True)
    first_support = ex.certify_first_support_wall(path, pre_faces, root, target)
    event = event_audit(pre_rows, target, root)
    wall_class_cover = ex.certify_mechanics_interval(
        path, wall_faces, PROTECTED, root["lo"], root["hi"]
    )
    if wall_class_cover["midpoint_class"]["class"] != [2, 2, 2]:
        raise AssertionError(wall_class_cover)
    print("complete post-cell primitive audit", flush=True)
    post_interval = strict_interval(post_rows, root["hi"], FAR_PARAMETER)
    post_class_cover = ex.certify_path_segment(
        restrict_path(path, root["hi"], FAR_PARAMETER), post_faces, PROTECTED
    )

    pre_edges = edge_set(pre_faces)
    wall_edges = edge_set(wall_faces)
    post_edges = edge_set(post_faces)
    if face_key_set(pre_faces) - face_key_set(post_faces) != {
        tuple(sorted(face)) for face in REMOVED_FACES
    }:
        raise AssertionError("wrong removed maximal faces")
    if face_key_set(post_faces) - face_key_set(pre_faces) != {
        tuple(sorted(face)) for face in ADDED_FACES
    }:
        raise AssertionError("wrong added maximal faces")
    if pre_edges - post_edges != {REMOVED_EDGE}:
        raise AssertionError(("wrong removed edge", pre_edges - post_edges))
    if post_edges - pre_edges != {ADDED_EDGE}:
        raise AssertionError(("wrong added edge", post_edges - pre_edges))
    if len(wall_edges) != 161 or len(wall_faces) != 102:
        raise AssertionError("wrong wall f-vector")
    for name, faces, edges in (
        ("pre", pre_faces, pre_edges),
        ("wall", wall_faces, wall_edges),
        ("post", post_faces, post_edges),
    ):
        if BASE not in {frozenset(face) for face in faces}:
            raise AssertionError((name, "base missing"))
        missing = sorted(forced_rails() - edges)
        if missing:
            raise AssertionError((name, "rails missing", missing))

    points = {
        "source": source,
        "pre": evaluate_path(path, pre_parameter),
        "post": evaluate_path(path, post_parameter),
        "far": evaluate_path(path, FAR_PARAMETER),
    }
    checkpoint_records = {
        "source": checkpoint(points["source"], pre_faces),
        "pre": checkpoint(points["pre"], pre_faces),
        "post": checkpoint(points["post"], post_faces),
        "far": checkpoint(points["far"], post_faces),
    }
    write_exact_csv(PRE_OUT, points["pre"])
    write_exact_csv(POST_OUT, points["post"])
    write_exact_csv(FAR_OUT, points["far"])

    residuals = directed_residual_audit(
        path, pre_faces, post_faces, root, FAR_PARAMETER
    )
    rail_guard = rejected_rail_guard(path, pre_faces, FAR_PARAMETER)
    generated = (PRE_OUT, POST_OUT, FAR_OUT)
    source_files = (
        SOURCE,
        SOURCE_FACES,
        REJECTED_EVENT_CERTIFICATE,
        PROPOSAL,
        PATH_DEFINITION,
        PRE_FACES_PATH,
        WALL_FACES_PATH,
        POST_FACES_PATH,
    )
    certificate = {
        "version": 1,
        "type": "exact full-control rail-preserving algebraic safe flip",
        "verdict": "EXACT_FULL_CONTROL_RAIL255256_FIRST_SAFE_FLIP_PASS",
        "winner_status": "NONWINNER",
        "scope": (
            "Exact for the selected 165-control rational-affine line from the "
            "frozen exact source through its first algebraic support wall and "
            "to rational parameter 7/20 in the adjacent safe cell."
        ),
        "source_file_sha256": {
            str(path.relative_to(ROOT)): sha256(path) for path in source_files
        },
        "path": {
            "path_definition_sha256": sha256(PATH_DEFINITION),
            "velocity_digest": path_definition["velocity_digest"],
            "event_root": root_record(target, root),
            "pre_parameter": ex.qs(pre_parameter),
            "post_parameter": ex.qs(post_parameter),
            "far_parameter": ex.qs(FAR_PARAMETER),
        },
        "open_cells": {
            "pre": {
                "complete_primitive_audit": pre_interval,
                "class_cover": pre_class_cover,
            },
            "post": {
                "complete_primitive_audit": post_interval,
                "class_cover": post_class_cover,
            },
        },
        "event": {
            "circuit": list(EVENT_CIRCUIT),
            "target_support": {
                "face_index": TARGET_SUPPORT[0],
                "witness": TARGET_SUPPORT[1],
            },
            "first_support_wall": first_support,
            "complete_wall_event_audit": event,
            "wall_class_cover": wall_class_cover,
            "pre_f_vector": [61, 162, 103],
            "wall_f_vector": [61, 161, 102],
            "post_f_vector": [61, 162, 103],
            "removed_maximal_faces": [list(face) for face in REMOVED_FACES],
            "wall_maximal_face": next(
                face for face in wall_faces if set(face) == set(EVENT_CIRCUIT)
            ),
            "added_maximal_faces": [list(face) for face in ADDED_FACES],
            "removed_true_edge": list(REMOVED_EDGE),
            "added_true_edge": list(ADDED_EDGE),
            "forced_rails_preserved_pre_wall_post": [37, 37, 37],
            "class_pre_wall_post": [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
        },
        "rational_checkpoints": checkpoint_records,
        "directed_active_residuals": residuals,
        "rejected_rail255256_circuit_guard": rail_guard,
        "generated_file_sha256": {
            str(path.relative_to(ROOT)): sha256(path) for path in generated
        },
        "residual_verdict": {
            "winner": False,
            "far_class": [2, 2, 2],
            "remaining_stable_faces": [sorted(BASE), list(TARGET_FACE)],
            "remaining_unstable_vertices": [1, 8],
            "remaining_saddle_edges": [[4, 5], [12, 13]],
            "next_action": (
                "Continue from exact_first_safe_flip_far.csv in the "
                "(248,250)-diagonal cell to the next exact support/mechanics event."
            ),
        },
    }
    CERTIFICATE.write_text(json.dumps(certificate, indent=2) + "\n")
    print(certificate["verdict"])
    print("event_root_interval", certificate["path"]["event_root"]["decimal_interval"])
    print("primitive_counts", pre_interval["primitive_count"], post_interval["primitive_count"])
    print("far_class", checkpoint_records["far"]["exact_mechanics"]["class"])
    print("far_missing_rails", checkpoint_records["far"]["missing_forced_rails"])
    print("certificate_sha256", sha256(CERTIFICATE))


if __name__ == "__main__":
    main()
