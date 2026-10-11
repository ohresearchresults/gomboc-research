#!/usr/bin/env python3
"""Clean verifier for the exact post-C17 fixed-plane safe flip.

This verifier does not import the proposer, locator, or certificate builder.
It reconstructs the ray and both face ledgers from frozen inputs, repeats the
12,363-polynomial interval audit, checks event multiplicities, independently
enumerates all supporting planes at rational checkpoints, and rebuilds every
own-centroid mechanics classification before emitting its terminal marker.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from fractions import Fraction as Q
from pathlib import Path
from types import SimpleNamespace


HERE = Path(__file__).resolve().parent
ATTACK = HERE.parents[1]
SOURCE = ATTACK / "cells" / "endpoint.csv"
CANDIDATE = HERE / "fixed_plane_descent_candidate.csv"
CERTIFICATE = HERE / "safe_flip_certificate.json"
OUTPUT = HERE / "safe_flip_verification.json"
PRE_FACES_PATH = ATTACK / "cells" / "endpoint.json"
WALL_FACES_PATH = HERE / "safe_flip_wall_faces.json"
POST_FACES_PATH = HERE / "safe_flip_post_faces.json"
CORE_DIR = ATTACK.parents[1] / "global_carrier_support" / "rigorous_local_bypass"
sys.path.insert(0, str(ATTACK))
sys.path.insert(0, str(CORE_DIR))

import exact_core as ex  # noqa: E402
import post_c17_exact as pc  # noqa: E402

_FROZEN_SPEC = importlib.util.spec_from_file_location(
    "post_c17_frozen_verify_certificate",
    ATTACK / "verify_certificate.py",
)
assert _FROZEN_SPEC is not None and _FROZEN_SPEC.loader is not None
frozen_verify = importlib.util.module_from_spec(_FROZEN_SPEC)
_FROZEN_SPEC.loader.exec_module(frozen_verify)


FAR_PARAMETER = Q(16)
REMOVED_FACES = ((0, 72, 54), (0, 16, 72))
ADDED_FACES = ((0, 16, 54), (16, 72, 54))
WALL_FACE = (0, 16, 72, 54)
REMOVED_EDGE = (0, 72)
ADDED_EDGE = (16, 54)
EVENT_FAMILY = {
    "edge:(0, 72):beta1": 1,
    "edge:(0, 72):beta2": 1,
    "edge:(0, 72):gram": 2,
    "support:f59:w16": 1,
    "support:f66:w54": 1,
}
TARGET = "support:f59:w16"
EXPECTED_CERTIFICATE_VERDICT = "EXACT_POST_C17_FIXED_PLANE_SAFE_FLIP_PASS"
VERIFIER_VERDICT = "INDEPENDENT_EXACT_POST_C17_FIXED_PLANE_SAFE_FLIP_PASS"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def line_points(source, endpoint):
    return {
        label: tuple(
            ex.P((source[label][axis], endpoint[label][axis] - source[label][axis]))
            for axis in range(3)
        )
        for label in source
    }


def evaluate(path, parameter):
    return {
        label: tuple(value.eval(parameter) for value in xyz)
        for label, xyz in path.items()
    }


def face_ledgers():
    payload = json.loads(PRE_FACES_PATH.read_text())
    pre = payload["maximal_face_cycles"] if isinstance(payload, dict) else payload
    removed = {tuple(sorted(face)) for face in REMOVED_FACES}
    kept = [face for face in pre if tuple(sorted(face)) not in removed]
    assert len(pre) - len(kept) == 2
    wall = kept + [list(WALL_FACE)]
    post = kept + [list(face) for face in ADDED_FACES]
    return pre, wall, post


def edge_set(faces):
    return {
        tuple(sorted((a, b)))
        for cycle in faces
        for a, b in zip(cycle, cycle[1:] + cycle[:1])
    }


def primitive_rows(path, faces):
    ledger = ex.mechanics_primitives(path, faces)
    yield "volume_d6", ledger["d6"], "mechanics_denominator"
    for face_index, witness, polynomial in ex.support_polynomials(path, faces):
        yield f"support:f{face_index}:w{witness}", polynomial, "support"
    for face_index, cycle in enumerate(faces):
        if len(cycle) <= 3:
            continue
        normal = ex.cycle_normal(cycle, path)
        for offset, current in enumerate(cycle):
            previous = cycle[offset - 1]
            following = cycle[(offset + 1) % len(cycle)]
            turn = ex.dot(
                ex.cross(
                    ex.sub(path[current], path[previous]),
                    ex.sub(path[following], path[current]),
                ),
                normal,
            )
            yield f"in_face_turn:f{face_index}:v{current}", turn, "in_face_turn"
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
            "direction_norm2",
            "gram",
            "t",
            "one_minus_t",
            "beta1",
            "beta2",
        ):
            yield f"edge:{edge}:{component}", rows[component], "edge_component"


def trim(values):
    out = list(values)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out or [Q(0)]


def divmod_poly(left, right):
    numerator = trim(left)
    denominator = trim(right)
    assert denominator != [Q(0)]
    quotient = [Q(0)] * max(1, len(numerator) - len(denominator) + 1)
    while len(numerator) >= len(denominator) and numerator != [Q(0)]:
        shift = len(numerator) - len(denominator)
        factor = numerator[-1] / denominator[-1]
        quotient[shift] += factor
        for index, coefficient in enumerate(denominator):
            numerator[index + shift] -= factor * coefficient
        numerator = trim(numerator)
    return trim(quotient), numerator


def multiplicity(polynomial, factor):
    count = 0
    quotient = list(polynomial.c)
    while True:
        divided, remainder = divmod_poly(quotient, factor.c)
        if remainder != [Q(0)]:
            break
        quotient = divided
        count += 1
    return count, ex.P(tuple(quotient))


def strict_interval(rows, lo, hi):
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


def exact_faces(points, cycles):
    return pc.ex.exactify_faces(
        points,
        SimpleNamespace(faces=[{"cycle": list(cycle)} for cycle in cycles]),
    )


def checkpoint(points, cycles, expected_f):
    support = ex.supporting_cell(points, cycles)
    ledger, mechanics = ex.classify_point(points, cycles)
    assert support["f_vector"] == expected_f and support["euler"] == 2
    assert mechanics["class"] == [2, 4, 4]
    assert not (pc.esc.forced_rails() - set(support["edges"]))
    d6, m24 = ex.exact_centroid_numerators(points, cycles)
    assert d6 > 0
    centroid = tuple(value / (4 * d6) for value in m24)
    return support, mechanics, centroid, ledger


def named_values(points, cycles):
    faces = exact_faces(points, cycles)
    q, centroid = pc.make_jets(points, faces, [])
    incidence = pc.esc.incidence(faces)

    def fc(vertices, edge):
        face = pc.esc.face_by_vertices(faces, vertices)
        values = dict(pc.rj.face_components(face, q, centroid))
        return (values[edge] if edge in values else values[edge[::-1]]).v

    def ec(edge, component):
        edge = tuple(sorted(edge))
        return pc.rj.edge_components(edge, incidence[edge], faces, q, centroid)[component].v

    return {
        "S228_264_246_via_246_228": fc([228, 264, 246], (246, 228)),
        "U228_via_251": pc.rj.vertex_support(228, 251, q, centroid).v,
        "U231_via_232": pc.rj.vertex_support(231, 232, q, centroid).v,
        "U246_via_245": pc.rj.vertex_support(246, 245, q, centroid).v,
        "H8_246_via_t": ec((8, 246), "t"),
        "H228_254_via_beta2": ec((228, 254), "beta2"),
        "H231_247_via_beta1": ec((231, 247), "beta1"),
        "H236_237_via_beta1": ec((236, 237), "beta1"),
    }


def main():
    certificate = json.loads(CERTIFICATE.read_text())
    assert certificate["verdict"] == EXPECTED_CERTIFICATE_VERDICT
    assert certificate["winner_status"] == "NONWINNER"
    source = pc.read_rows(SOURCE)
    candidate = pc.read_rows(CANDIDATE)
    path = line_points(source, candidate)
    pre_faces, wall_faces, post_faces = face_ledgers()
    assert json.loads(WALL_FACES_PATH.read_text()) == wall_faces
    assert json.loads(POST_FACES_PATH.read_text()) == post_faces

    pre_rows = list(primitive_rows(path, pre_faces))
    post_rows = list(primitive_rows(path, post_faces))
    assert len(pre_rows) == len(post_rows) == 12363
    by_name = {name: polynomial for name, polynomial, _family in pre_rows}
    target = by_name[TARGET]
    lo = Q(certificate["path"]["root"]["lo"])
    hi = Q(certificate["path"]["root"]["hi"])
    assert pc.root_count(target.c, lo, hi) == 1
    assert target.eval(lo) * target.eval(hi) < 0
    factor = ex.P(tuple(value / target.c[-1] for value in target.c))

    event_records = {}
    for name, expected in EVENT_FAMILY.items():
        count, quotient = multiplicity(by_name[name], factor)
        assert count == expected
        quotient_sign, leaves, margin = ex.bernstein_sign(
            quotient, lo, hi, max_depth=60
        )
        event_records[name] = {
            "multiplicity": count,
            "quotient_sign": quotient_sign,
            "quotient_leaves": leaves,
            "quotient_margin": margin,
        }
    for name, polynomial, _family in pre_rows:
        if name not in EVENT_FAMILY:
            ex.bernstein_sign(polynomial, lo, hi, max_depth=60)

    pre_interval = strict_interval(pre_rows, Q(0), lo)
    post_interval = strict_interval(post_rows, hi, FAR_PARAMETER)
    assert pre_interval == certificate["open_intervals"]["pre"]["exhaustive"]
    assert post_interval == certificate["open_intervals"]["post"]["exhaustive"]

    pre_edges, wall_edges, post_edges = map(edge_set, (pre_faces, wall_faces, post_faces))
    assert pre_edges - post_edges == {REMOVED_EDGE}
    assert post_edges - pre_edges == {ADDED_EDGE}
    assert [len(pre_edges), len(wall_edges), len(post_edges)] == [150, 149, 150]
    assert all(not (pc.esc.forced_rails() - edges) for edges in (pre_edges, wall_edges, post_edges))

    points = {
        "source": source,
        "pre": evaluate(path, lo),
        "post": evaluate(path, hi),
        "far": evaluate(path, FAR_PARAMETER),
    }
    cycles = {
        "source": pre_faces,
        "pre": pre_faces,
        "post": post_faces,
        "far": post_faces,
    }
    checkpoint_records = {}
    for name in points:
        support, mechanics, centroid, _ledger = checkpoint(
            points[name], cycles[name], [61, 150, 91]
        )
        expected = certificate["rational_checkpoints"][name]
        assert [ex.qs(value) for value in centroid] == expected["exact_centroid"]
        assert mechanics == expected["exact_mechanics"]
        checkpoint_records[name] = {
            "centroid": [ex.qs(value) for value in centroid],
            "class": mechanics["class"],
            "support_count": support["strict_support_count"],
        }

    for name in ("pre", "far"):
        faces = exact_faces(points[name], cycles[name])
        audit = frozen_verify.exhaustive_supporting_planes(points[name], faces)
        assert audit["supporting_planes"] == 91
        checkpoint_records[name]["all_triples"] = audit

    source_values = named_values(source, pre_faces)
    far_values = named_values(points["far"], post_faces)
    ratios = {
        name: far_values[name] / source_values[name] for name in source_values
    }
    assert all(Q(0) < ratio < Q(1) for ratio in ratios.values())
    assert {
        name: ex.qs(ratio) for name, ratio in ratios.items()
    } == certificate["directed_residuals"]["target_ratios_exact"]

    for relative, expected in certificate["generated_file_sha256"].items():
        assert sha256(ATTACK / relative) == expected
    for relative, expected in certificate["source_hashes"].items():
        assert sha256(ATTACK / relative) == expected

    payload = {
        "version": 1,
        "scope": "clean reconstruction of exact post-C17 fixed-plane safe flip",
        "certificate_sha256": sha256(CERTIFICATE),
        "primitive_count_each_strict_cell": 12363,
        "event_multiplicities": event_records,
        "checkpoints": checkpoint_records,
        "target_ratios_exact": {name: ex.qs(ratio) for name, ratio in ratios.items()},
        "verdict": VERIFIER_VERDICT,
        "winner_status": "NONWINNER",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(payload["verdict"])
    print("winner_status", payload["winner_status"])
    print("certificate_sha256", payload["certificate_sha256"])
    print("verification_sha256", sha256(OUTPUT))


if __name__ == "__main__":
    main()
