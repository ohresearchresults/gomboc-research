#!/usr/bin/env python3
"""Certify the first support flip on the nonlinear coplanarity path."""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path
from types import SimpleNamespace


HERE = Path(__file__).resolve().parent
ATTACK = HERE.parents[1]
PATH_JSON = HERE / "nonlinear_polynomial_path.json"
SCAN_JSON = HERE / "nonlinear_first_event_scan.json"
DIRECTION_JSON = HERE / "exterior_direction.json"
CERTIFICATE = HERE / "nonlinear_first_event_certificate.json"
PRE_OUT = HERE / "nonlinear_flip_pre.csv"
POST_OUT = HERE / "nonlinear_flip_post.csv"
FAR_OUT = HERE / "nonlinear_flip_far.csv"
WALL_FACES_OUT = HERE / "nonlinear_flip_wall_faces.json"
POST_FACES_OUT = HERE / "nonlinear_flip_post_faces.json"
CORE = ATTACK.parents[1] / "global_carrier_support" / "rigorous_local_bypass"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ATTACK))
sys.path.insert(0, str(CORE))

import build_nonlinear_chart as chart  # noqa: E402
import exact_core as ex  # noqa: E402
import locate_nonlinear_first_event as locator  # noqa: E402
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


def evaluate_path(path, parameter):
    return {
        label: tuple(component.eval(parameter) for component in xyz)
        for label, xyz in path.items()
    }


def restrict_path(path, lo, hi):
    return {
        label: tuple(component.affine(lo, hi) for component in xyz)
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


def monic_gcd(left: ex.P, right: ex.P):
    a, b = trim(left.c), trim(right.c)
    while b != [Q(0)]:
        _quotient, remainder = divmod_poly(a, b)
        a, b = b, remainder
    return ex.P(tuple(value / a[-1] for value in a))


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
    expected_multiplicity = {
        "edge:(0, 72):beta1": 1,
        "edge:(0, 72):beta2": 1,
        "edge:(0, 72):gram": 2,
        "support:f59:w16": 1,
        "support:f66:w54": 1,
    }
    shared = {}
    for name in EVENT_FAMILY:
        polynomial, family = by_name[name]
        gcd = monic_gcd(target, polynomial)
        assert gcd == event_factor
        isolated = ex.isolate_monotone_root(gcd, root["lo"], root["hi"], ROOT_WIDTH)
        assert isolated["lo"] <= root["hi"] and isolated["hi"] >= root["lo"]
        multiplicity, quotient = factor_multiplicity(polynomial, event_factor)
        assert multiplicity == expected_multiplicity[name]
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
        "event_factor_degree": event_factor.degree,
        "event_factor_digest": canonical_hash(event_factor.exact()),
        "multiplicity_pattern": expected_multiplicity,
        "gram_even_touch_certified": True,
    }


def exhaustive_strict_interval(rows, lo, hi):
    digest = hashlib.sha256()
    count = 0
    leaves = 0
    worst = None
    family_counts = {}
    for name, polynomial, family in rows:
        sign, row_leaves, margin = ex.bernstein_sign(
            polynomial, lo, hi, max_depth=60
        )
        count += 1
        leaves += row_leaves
        worst = margin if worst is None else min(worst, margin)
        family_counts[family] = family_counts.get(family, 0) + 1
        digest.update(
            f"{name}|{family}|{sign}|{'|'.join(polynomial.exact())}\n".encode()
        )
    return {
        "lo": ex.qs(lo),
        "hi": ex.qs(hi),
        "primitive_count": count,
        "family_counts": family_counts,
        "bernstein_leaf_count": leaves,
        "minimum_bernstein_log10_abs": worst,
        "primitive_digest": digest.hexdigest(),
    }


def checkpoint(points, cycles, expected_f):
    support = ex.supporting_cell(points, cycles)
    _ledger, mechanics = ex.classify_point(points, cycles)
    assert support["f_vector"] == expected_f and support["euler"] == 2
    assert mechanics["class"] == [2, 4, 4]
    assert {tuple(face) for face in mechanics["stable_faces"]} == {
        tuple(sorted(face)) for face in PROTECTED["stable"]
    }
    assert mechanics["unstable_vertices"] == PROTECTED["unstable"]
    assert mechanics["saddle_edges"] == PROTECTED["saddles"]
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


def exact_faces(points, cycles):
    return pc.ex.exactify_faces(
        points,
        SimpleNamespace(faces=[{"cycle": list(cycle)} for cycle in cycles]),
    )


def residual_audit(source, far, pre_cycles, post_cycles):
    source_p, source_t = chart.mechanics_jets(
        source, exact_faces(source, pre_cycles), []
    )
    far_p, far_t = chart.mechanics_jets(
        far, exact_faces(far, post_cycles), []
    )
    source_p, source_t = dict(source_p), dict(source_t)
    far_p, far_t = dict(far_p), dict(far_t)
    p_ratios = {name: far_p[name].v / source_p[name].v for name in source_p}
    t_ratios = {name: far_t[name].v / source_t[name].v for name in source_t}
    assert len(p_ratios) == 30 and len(t_ratios) == 8
    assert all(ratio > 1 for ratio in p_ratios.values())
    assert all(Q(0) < ratio < 1 for ratio in t_ratios.values())
    return {
        "P_ratios_exact": {name: ex.qs(ratio) for name, ratio in p_ratios.items()},
        "P_minimum_ratio_decimal": min(float(ratio) for ratio in p_ratios.values()),
        "T_ratios_exact": {name: ex.qs(ratio) for name, ratio in t_ratios.items()},
        "T_ratio_range_decimal": [
            min(float(ratio) for ratio in t_ratios.values()),
            max(float(ratio) for ratio in t_ratios.values()),
        ],
        "all_30_base_and_U8_components_strictly_larger": True,
        "all_8_targets_positive_and_strictly_smaller": True,
    }


def main():
    path_payload = json.loads(PATH_JSON.read_text())
    scan = json.loads(SCAN_JSON.read_text())
    direction = json.loads(DIRECTION_JSON.read_text())
    assert path_payload["verdict"] == "EXACT_POST_C17_NONLINEAR_POLYNOMIAL_PATH_MATERIALIZED_PASS"
    assert scan["verdict"] == "EXHAUSTIVE_EXACT_POST_C17_NONLINEAR_FIRST_EVENT_LOCATOR_PASS"
    assert direction["outside_fixed_plane_chart_exact"]
    path = locator.load_path(path_payload)
    pre_cycles, wall_cycles, post_cycles = build_face_ledgers(
        json.loads((ATTACK / "cells" / "endpoint.json").read_text())[
            "maximal_face_cycles"
        ]
    )
    pre_rows = list(locator.primitive_rows(path, pre_cycles))
    assert len(pre_rows) == 12363
    by_name = {name: polynomial for name, polynomial, _family in pre_rows}
    assert TARGET in by_name
    support_candidate = next(
        row for row in scan["overlapping_first_candidates"] if row["name"] == TARGET
    )
    target = by_name[TARGET]
    assert target.degree == 4
    root = ex.isolate_monotone_root(
        target, Q(support_candidate["lo"]), Q(support_candidate["hi"]), ROOT_WIDTH
    )
    root_record = {
        "lo": ex.qs(root["lo"]),
        "hi": ex.qs(root["hi"]),
        "width_exact": ex.qs(root["hi"] - root["lo"]),
        "decimal_interval": [float(root["lo"]), float(root["hi"])],
        "value_lo": ex.qs(root["value_lo"]),
        "value_hi": ex.qs(root["value_hi"]),
        "derivative_sign": root["derivative_sign"],
        "derivative_bernstein_leaves": root["derivative_bernstein_leaves"],
        "polynomial_degree": target.degree,
        "polynomial_exact": target.exact(),
        "polynomial_digest": canonical_hash(target.exact()),
        "unique_root_by_strict_derivative_and_opposite_endpoint_signs": True,
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

    print("CERTIFY pre exhaustive", flush=True)
    pre_interval = exhaustive_strict_interval(pre_rows, Q(0), root["lo"])
    print("CERTIFY wall mechanics", flush=True)
    wall_cover = ex.certify_mechanics_interval(
        path, wall_cycles, PROTECTED, root["lo"], root["hi"]
    )
    assert wall_cover["midpoint_class"]["class"] == [2, 4, 4]
    post_rows = list(locator.primitive_rows(path, post_cycles))
    assert len(post_rows) == 12363
    print("CERTIFY post exhaustive", flush=True)
    post_interval = exhaustive_strict_interval(
        post_rows, root["hi"], FAR_PARAMETER
    )

    pre_edges = edge_set(pre_cycles)
    wall_edges = edge_set(wall_cycles)
    post_edges = edge_set(post_cycles)
    assert pre_edges - post_edges == {REMOVED_EDGE}
    assert post_edges - pre_edges == {ADDED_EDGE}
    assert len(pre_edges) == 150 and len(wall_edges) == 149 and len(post_edges) == 150
    for edges in (pre_edges, wall_edges, post_edges):
        assert not (pc.esc.forced_rails() - edges)

    source = evaluate_path(path, Q(0))
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
    result = {
        "version": 1,
        "type": "exact rational degree-two nonlinear post-C17 support flip",
        "scope": (
            "All 12,363 support/in-face/own-centroid primitives on both open cells, "
            "the unique algebraic circuit wall, moving base plane, 61 active rows, "
            "protected base/U8 mechanics and all 37 forced rails."
        ),
        "source_hashes": {
            "nonlinear_polynomial_path.json": sha256(PATH_JSON),
            "nonlinear_first_event_scan.json": sha256(SCAN_JSON),
            "exterior_direction.json": sha256(DIRECTION_JSON),
        },
        "path": {
            "formula": "moving-frame affine-coordinate chart with theta(t)=t*d",
            "maximum_coordinate_degree": 2,
            "outside_fixed_plane_chart_exact": True,
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
        "verdict": "EXACT_POST_C17_NONLINEAR_SAFE_FLIP_PASS",
        "winner_status": "NONWINNER",
        "obstruction_status": "NONE_CLAIMED",
        "next_action": "Rebuild the 156D nonlinear chart in the (16,54)-diagonal cell.",
    }
    CERTIFICATE.write_text(json.dumps(result, indent=2) + "\n")
    print(result["verdict"])
    print("root", root_record["decimal_interval"])
    print("topology", result["event"]["pre_f_vector"], result["event"]["wall_f_vector"], result["event"]["post_f_vector"])
    print("class", result["event"]["class_transition"])
    print("P_minimum_ratio", residuals["P_minimum_ratio_decimal"])
    print("T_ratio_range", residuals["T_ratio_range_decimal"])
    print("certificate_sha256", sha256(CERTIFICATE))


if __name__ == "__main__":
    main()
