#!/usr/bin/env python3
"""Certify the first safe support flip on the post-C17 descent ray."""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path
from types import SimpleNamespace


HERE = Path(__file__).resolve().parent
ATTACK = HERE.parents[1]
SOURCE = ATTACK / "cells" / "endpoint.csv"
PROPOSAL_ENDPOINT = HERE / "fixed_plane_descent_candidate.csv"
PROPOSAL = HERE / "fixed_plane_descent_proposal.json"
SCAN = HERE / "first_event_scan.json"
CERTIFICATE = HERE / "safe_flip_certificate.json"
PRE_OUT = HERE / "safe_flip_pre.csv"
POST_OUT = HERE / "safe_flip_post.csv"
FAR_OUT = HERE / "safe_flip_far.csv"
WALL_FACES_OUT = HERE / "safe_flip_wall_faces.json"
POST_FACES_OUT = HERE / "safe_flip_post_faces.json"
CORE_DIR = ATTACK.parents[1] / "global_carrier_support" / "rigorous_local_bypass"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ATTACK))
sys.path.insert(0, str(CORE_DIR))

import build_full_chart as chart  # noqa: E402
import exact_core as ex  # noqa: E402
import post_c17_exact as pc  # noqa: E402


ROOT_WIDTH = Q(1, 10**30)
FAR_PARAMETER = Q(16)
CIRCUIT = (0, 16, 54, 72)
REMOVED_FACES = ((0, 72, 54), (0, 16, 72))
ADDED_FACES = ((0, 16, 54), (16, 72, 54))
WALL_FACE = (0, 16, 72, 54)
REMOVED_EDGE = (0, 72)
ADDED_EDGE = (16, 54)
TARGET = "support:f59:w16"
EVENT_FAMILY = (
    "edge:(0, 72):beta1",
    "edge:(0, 72):beta2",
    "edge:(0, 72):gram",
    "support:f59:w16",
    "support:f66:w54",
)
EVENT_MULTIPLICITY = {
    "edge:(0, 72):beta1": 1,
    "edge:(0, 72):beta2": 1,
    "edge:(0, 72):gram": 2,
    "support:f59:w16": 1,
    "support:f66:w54": 1,
}
PROTECTED = {
    "stable": [sorted((228, 264, 246)), list(range(17))],
    "unstable": [8, 228, 231, 246],
    "saddles": [[8, 246], [228, 254], [231, 247], [236, 237]],
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def path_from_endpoints(source, endpoint):
    assert set(source) == set(endpoint)
    return {
        label: tuple(
            ex.P((source[label][axis], endpoint[label][axis] - source[label][axis]))
            for axis in range(3)
        )
        for label in source
    }


def evaluate_path(path, parameter):
    return {
        label: tuple(value.eval(parameter) for value in xyz)
        for label, xyz in path.items()
    }


def restrict_path(path, lo, hi):
    return {
        label: tuple(value.affine(lo, hi) for value in xyz)
        for label, xyz in path.items()
    }


def edge_set(faces):
    return {
        tuple(sorted((a, b)))
        for cycle in faces
        for a, b in zip(cycle, cycle[1:] + cycle[:1])
    }


def build_face_ledgers(pre_faces):
    removed = {tuple(sorted(face)) for face in REMOVED_FACES}
    kept = [face for face in pre_faces if tuple(sorted(face)) not in removed]
    assert len(pre_faces) - len(kept) == 2
    return pre_faces, kept + [list(WALL_FACE)], kept + [list(face) for face in ADDED_FACES]


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


def trim(coefficients):
    out = list(coefficients)
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


def monic_gcd(a: ex.P, b: ex.P):
    left, right = trim(a.c), trim(b.c)
    while right != [Q(0)]:
        _quotient, remainder = divmod_poly(left, right)
        left, right = right, remainder
    return ex.P(tuple(value / left[-1] for value in left))


def factor_multiplicity(polynomial: ex.P, factor: ex.P):
    multiplicity = 0
    quotient = list(polynomial.c)
    while True:
        candidate, remainder = divmod_poly(quotient, list(factor.c))
        if remainder != [Q(0)]:
            break
        multiplicity += 1
        quotient = candidate
    return multiplicity, ex.P(tuple(quotient))


def exact_event_audit(rows, root, target):
    by_name = {name: (polynomial, family) for name, polynomial, family in rows}
    assert set(EVENT_FAMILY).issubset(by_name)
    strict_count = 0
    leaves = 0
    worst = None
    for name, polynomial, _family in rows:
        if name in EVENT_FAMILY:
            continue
        _sign, count, margin = ex.bernstein_sign(
            polynomial, root["lo"], root["hi"], max_depth=60
        )
        strict_count += 1
        leaves += count
        worst = margin if worst is None else min(worst, margin)
    event_factor = ex.P(tuple(value / target.c[-1] for value in target.c))
    expected_multiplicity = EVENT_MULTIPLICITY
    shared = {}
    for name in EVENT_FAMILY:
        polynomial, family = by_name[name]
        gcd = monic_gcd(target, polynomial)
        assert gcd.degree >= 1
        isolated = ex.isolate_monotone_root(
            gcd, root["lo"], root["hi"], ROOT_WIDTH
        )
        assert isolated["lo"] <= root["hi"] and isolated["hi"] >= root["lo"]
        multiplicity, quotient = factor_multiplicity(polynomial, event_factor)
        assert multiplicity == expected_multiplicity[name], (name, multiplicity)
        quotient_sign, quotient_leaves, quotient_margin = ex.bernstein_sign(
            quotient, root["lo"], root["hi"], max_depth=60
        )
        shared[name] = {
            "family": family,
            "polynomial_degree": polynomial.degree,
            "polynomial_digest": canonical_hash(polynomial.exact()),
            "gcd_degree": gcd.degree,
            "gcd_exact": gcd.exact(),
            "gcd_digest": canonical_hash(gcd.exact()),
            "gcd_root_interval": [ex.qs(isolated["lo"]), ex.qs(isolated["hi"])],
            "event_factor_multiplicity": multiplicity,
            "crosses_sign": multiplicity % 2 == 1,
            "quotient_sign": quotient_sign,
            "quotient_bernstein_leaf_count": quotient_leaves,
            "quotient_minimum_bernstein_log10_abs": quotient_margin,
        }
    return {
        "allowed_zero_family": list(EVENT_FAMILY),
        "strict_other_primitive_count": strict_count,
        "strict_other_bernstein_leaf_count": leaves,
        "strict_other_minimum_bernstein_log10_abs": worst,
        "shared_algebraic_factor": shared,
        "event_factor_exact": event_factor.exact(),
        "event_factor_digest": canonical_hash(event_factor.exact()),
        "multiplicity_pattern": expected_multiplicity,
        "gram_even_touch_certified": True,
    }


def exhaustive_strict_interval(rows, lo, hi):
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
    _ledger, mechanics = ex.classify_point(points, cycles)
    assert support["f_vector"] == expected_f
    assert support["euler"] == 2
    assert mechanics["class"] == [2, 4, 4]
    missing = sorted(pc.esc.forced_rails() - set(support["edges"]))
    assert not missing
    d6, m24 = ex.exact_centroid_numerators(points, cycles)
    assert d6 > 0
    centroid = tuple(value / (4 * d6) for value in m24)
    return {
        "coordinate_hash": canonical_hash({
            str(label): [ex.qs(value) for value in points[label]]
            for label in sorted(points)
        }),
        "exact_centroid": [ex.qs(value) for value in centroid],
        "exact_support": {key: value for key, value in support.items() if key != "edges"},
        "exact_mechanics": mechanics,
        "forced_rail_count": len(pc.esc.forced_rails()),
        "missing_forced_rails": [],
    }


def residual_audit(source, far, pre_cycles, post_cycles):
    source_values, source_base, source_u8 = chart.target_jets(
        source, exact_faces(source, pre_cycles), []
    )
    far_values, far_base, far_u8 = chart.target_jets(
        far, exact_faces(far, post_cycles), []
    )
    ratios = {
        name: far_values[name].v / source_values[name].v
        for name in chart.TARGET_NAMES
    }
    assert all(Q(0) < ratio < Q(1) for ratio in ratios.values())
    return {
        "target_ratios_exact": {name: ex.qs(ratio) for name, ratio in ratios.items()},
        "target_ratios_decimal": {name: float(ratio) for name, ratio in ratios.items()},
        "base_component_minimum_ratio_decimal": min(
            float(far_base[edge].v / source_base[edge].v) for edge in source_base
        ),
        "U8_component_minimum_ratio_decimal": min(
            float(far_u8[neighbor].v / source_u8[neighbor].v) for neighbor in source_u8
        ),
        "all_eight_targets_strictly_smaller": True,
        "base_and_U8_remain_strict_equilibria": True,
    }


def main():
    proposal = json.loads(PROPOSAL.read_text())
    scan = json.loads(SCAN.read_text())
    assert proposal["verdict"] == "RATIONAL_POST_C17_FIXED_PLANE_DESCENT_PROPOSAL_PASS"
    assert scan["verdict"] == "EXHAUSTIVE_EXACT_POST_C17_FIXED_PLANE_FIRST_EVENT_LOCATOR_PASS"
    source = pc.read_rows(SOURCE)
    proposal_endpoint = pc.read_rows(PROPOSAL_ENDPOINT)
    path = path_from_endpoints(source, proposal_endpoint)
    pre_cycles, wall_cycles, post_cycles = build_face_ledgers(
        json.loads((ATTACK / "cells" / "endpoint.json").read_text())["maximal_face_cycles"]
    )
    pre_rows = list(primitive_rows(path, pre_cycles))
    by_name = {name: polynomial for name, polynomial, _family in pre_rows}
    assert TARGET in by_name
    candidate = scan["first_candidate"]
    assert candidate["name"] == "edge:(0, 72):beta1"
    target = by_name[TARGET]
    assert len(pre_rows) == 12363
    assert pc.root_count(target.c, Q(candidate["lo"]), Q(candidate["hi"])) == 1
    root = ex.isolate_monotone_root(
        target,
        Q(candidate["lo"]),
        Q(candidate["hi"]),
        ROOT_WIDTH,
    )
    root_record = {
        "lo": ex.qs(root["lo"]),
        "hi": ex.qs(root["hi"]),
        "decimal_interval": [float(root["lo"]), float(root["hi"])],
        "value_lo": ex.qs(root["value_lo"]),
        "value_hi": ex.qs(root["value_hi"]),
        "derivative_sign": root["derivative_sign"],
        "derivative_bernstein_leaves": root["derivative_bernstein_leaves"],
        "polynomial_degree": target.degree,
        "polynomial_exact": target.exact(),
        "polynomial_digest": canonical_hash(target.exact()),
        "sturm_root_count": 1,
    }
    event_audit = exact_event_audit(pre_rows, root, target)
    first_support = ex.certify_first_support_wall(path, pre_cycles, root, target)
    expected_support_family = {
        (tuple(sorted(REMOVED_FACES[0])), 16),
        (tuple(sorted(REMOVED_FACES[1])), 54),
    }
    actual_support_family = {
        (tuple(sorted(pre_cycles[row["face_index"]])), row["witness"])
        for row in first_support["target_support_family"]
    }
    assert actual_support_family == expected_support_family

    pre_interval = {
        "exhaustive": exhaustive_strict_interval(pre_rows, Q(0), root["lo"]),
        "class_cover": ex.certify_path_segment(
            restrict_path(path, Q(0), root["lo"]), pre_cycles, PROTECTED
        ),
    }
    wall_cover = ex.certify_mechanics_interval(
        path, wall_cycles, PROTECTED, root["lo"], root["hi"]
    )
    assert wall_cover["midpoint_class"]["class"] == [2, 4, 4]
    post_rows = list(primitive_rows(path, post_cycles))
    post_interval = {
        "exhaustive": exhaustive_strict_interval(
            post_rows, root["hi"], FAR_PARAMETER
        ),
        "class_cover": ex.certify_path_segment(
            restrict_path(path, root["hi"], FAR_PARAMETER), post_cycles, PROTECTED
        ),
    }

    pre_edges = edge_set(pre_cycles)
    wall_edges = edge_set(wall_cycles)
    post_edges = edge_set(post_cycles)
    assert pre_edges - post_edges == {REMOVED_EDGE}
    assert post_edges - pre_edges == {ADDED_EDGE}
    assert len(pre_edges) == 150 and len(wall_edges) == 149 and len(post_edges) == 150
    for edges in (pre_edges, wall_edges, post_edges):
        assert not (pc.esc.forced_rails() - edges)

    pre_points = evaluate_path(path, root["lo"])
    post_points = evaluate_path(path, root["hi"])
    far_points = evaluate_path(path, FAR_PARAMETER)
    checkpoints = {
        "source": checkpoint(source, pre_cycles, [61, 150, 91]),
        "pre": checkpoint(pre_points, pre_cycles, [61, 150, 91]),
        "post": checkpoint(post_points, post_cycles, [61, 150, 91]),
        "far": checkpoint(far_points, post_cycles, [61, 150, 91]),
    }
    residuals = residual_audit(source, far_points, pre_cycles, post_cycles)

    pc.write_rows(PRE_OUT, pre_points)
    pc.write_rows(POST_OUT, post_points)
    pc.write_rows(FAR_OUT, far_points)
    WALL_FACES_OUT.write_text(json.dumps(wall_cycles, indent=2) + "\n")
    POST_FACES_OUT.write_text(json.dumps(post_cycles, indent=2) + "\n")
    generated = (PRE_OUT, POST_OUT, FAR_OUT, WALL_FACES_OUT, POST_FACES_OUT)
    payload = {
        "version": 1,
        "type": "exact rational-affine post-C17 safe support flip",
        "scope": (
            "All 12,363 pre-cell and complete post-cell support/in-face/own-centroid mechanics "
            "primitives, unique algebraic circuit wall, exact rational checkpoints, "
            "61 active rows, two polygon faces, protected equilibria and 37 rails."
        ),
        "source_hashes": {
            str(path.relative_to(ATTACK)): sha256(path)
            for path in (SOURCE, PROPOSAL_ENDPOINT, PROPOSAL, SCAN)
        },
        "path": {
            "formula": "q_i(t)=source_i+t*(proposal_endpoint_i-source_i)",
            "root": root_record,
            "far_parameter": ex.qs(FAR_PARAMETER),
        },
        "event": {
            "circuit": list(CIRCUIT),
            "removed_faces": [list(face) for face in REMOVED_FACES],
            "wall_face": list(WALL_FACE),
            "added_faces": [list(face) for face in ADDED_FACES],
            "removed_edge": list(REMOVED_EDGE),
            "added_edge": list(ADDED_EDGE),
            "pre_f_vector": [61, 150, 91],
            "wall_f_vector": [61, 149, 90],
            "post_f_vector": [61, 150, 91],
            "class_transition": [[2, 4, 4], [2, 4, 4], [2, 4, 4]],
            "first_support_wall": first_support,
            "exact_zero_family_audit": event_audit,
            "wall_mechanics_cover": wall_cover,
            "all_37_forced_rails_preserved": True,
        },
        "open_intervals": {"pre": pre_interval, "post": post_interval},
        "rational_parameters": {
            "source": "0",
            "pre": ex.qs(root["lo"]),
            "post": ex.qs(root["hi"]),
            "far": ex.qs(FAR_PARAMETER),
        },
        "rational_checkpoints": checkpoints,
        "directed_residuals": residuals,
        "generated_file_sha256": {
            str(path.relative_to(ATTACK)): sha256(path) for path in generated
        },
        "verdict": "EXACT_POST_C17_FIXED_PLANE_SAFE_FLIP_PASS",
        "winner_status": "NONWINNER",
        "next_action": "Rebuild the full-control chart from safe_flip_far.csv in the (16,54)-diagonal cell.",
    }
    CERTIFICATE.write_text(json.dumps(payload, indent=2) + "\n")
    print(payload["verdict"])
    print("root", root_record["decimal_interval"])
    print("topology", payload["event"]["pre_f_vector"], payload["event"]["wall_f_vector"], payload["event"]["post_f_vector"])
    print("class", payload["event"]["class_transition"])
    print("target_ratios", residuals["target_ratios_decimal"])
    print("certificate_sha256", sha256(CERTIFICATE))


if __name__ == "__main__":
    main()
