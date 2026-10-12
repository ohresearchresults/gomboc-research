#!/usr/bin/env python3
"""Build the exact/directed local carrier-bypass certificate.

Qhull is used only as a locator for the two face ledgers.  Both ledgers are
then accepted only after exhaustive exact rational support reconstruction.
All theorem fields in ``certificate.json`` come from ``exact_core``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy.spatial import ConvexHull


HERE = Path(__file__).resolve().parent
TRACK = HERE.parent
ROOT = HERE.parents[2]
ATLAS = ROOT / "tracks" / "circuit_atlas"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(TRACK))

import exact_core as ex  # noqa: E402
from actual_hull_mechanics import _merge_coplanar_facets  # noqa: E402


SOURCE = ATLAS / "row54_far_rebuilt.csv"
SOURCE_AUDIT = ATLAS / "row54_far_rebuilt_audit.json"
ATLAS_JSON = TRACK / "local_birth_atlas.json"
CONTINUATION = TRACK / "pair_wall_continuation.json"
ROOTS = TRACK / "pair_wall_first_birth_roots.json"
ADAPTIVE = TRACK / "adaptive_birth_bypass.json"
NUMERIC_WALL = TRACK / "adaptive_first_wall_audit.json"
OUTPUT = HERE / "certificate.json"


def canonical_hash(value) -> str:
    data = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()


def numeric_faces(points):
    labels = sorted(points)
    array = np.asarray([[float(x) for x in points[i]] for i in labels])
    cycles, _ = _merge_coplanar_facets(array, ConvexHull(array))
    return [[labels[j] for j in cycle] for cycle in cycles]


def exact_root_record(root):
    mid = (root["lo"] + root["hi"]) / 2
    return {
        "lo_exact": ex.qs(root["lo"]),
        "hi_exact": ex.qs(root["hi"]),
        "midpoint_decimal": float(mid),
        "width_decimal": float(root["hi"] - root["lo"]),
        "value_lo_sign": 1 if root["value_lo"] > 0 else -1,
        "value_hi_sign": 1 if root["value_hi"] > 0 else -1,
        "value_lo_log10_abs": ex.qlog10(root["value_lo"]),
        "value_hi_log10_abs": ex.qlog10(root["value_hi"]),
        "derivative_sign": root["derivative_sign"],
        "derivative_bernstein_leaves": root["derivative_bernstein_leaves"],
    }


def face_edge_sets(faces):
    face_keys = {tuple(sorted(face)) for face in faces}
    edge_keys = set()
    for face in faces:
        for a, b in zip(face, face[1:] + face[:1]):
            edge_keys.add(tuple(sorted((a, b))))
    return face_keys, edge_keys


def compute(star_faces=None, post_faces=None):
    charts = ex.build_charts(SOURCE, ATLAS_JSON, ADAPTIVE)
    rails = {
        tuple(sorted(edge))
        for edge in json.loads(SOURCE_AUDIT.read_text())["fresh_hull_audit"]["forced_rail_edges"]
    }
    if len(rails) != 37:
        raise AssertionError(len(rails))

    if star_faces is None:
        star_faces = numeric_faces(charts["star"])
    star_cell = ex.supporting_cell(charts["star"], star_faces)
    if star_cell["f_vector"] != [61, 162, 103] or star_cell["euler"] != 2:
        raise AssertionError(star_cell["f_vector"])
    star_edges = set(map(tuple, star_cell["edges"]))
    if not rails <= star_edges:
        raise AssertionError(("missing star rails", sorted(rails - star_edges)))

    # One exact primitive controls both linked birth decisions.
    xline = ex.line_points(charts["star"], charts["vx"])
    linked = ex.common_birth_data(xline, star_faces)
    if linked["identity"] != ex.P.zero():
        raise AssertionError("linked identity is not exact")
    common_root = ex.isolate_monotone_root(
        linked["shared"], ex.Q(-1, 100_000_000), ex.Q(1, 100_000_000), ex.Q(1, 10**24)
    )
    factor_certificates = {}
    for name, expected in (
        ("gram", 1), ("cc", 1), ("cross_factor", -1), ("face_reference", 1)
    ):
        sign, leaves, margin = ex.bernstein_sign(
            linked[name], common_root["lo"], common_root["hi"]
        )
        if sign != expected:
            raise AssertionError((name, sign, expected))
        factor_certificates[name] = {
            "sign": sign,
            "bernstein_leaves": leaves,
            "min_coefficient_log10_abs": margin,
        }

    # Prove that the shared component is the only vanishing component of each
    # feature in the isolated interval.
    root_ledger = ex.mechanics_primitives(xline, star_faces)
    birth_face = (8, 245, 246)
    active_edge = (8, 245)
    active_face = ex.signed_face_components(root_ledger, birth_face)[active_edge]
    other_feature_components = {}
    for edge, poly in ex.signed_face_components(root_ledger, birth_face).items():
        if edge == active_edge:
            continue
        sign, leaves, margin = ex.bernstein_sign(poly, common_root["lo"], common_root["hi"])
        if sign != 1:
            raise AssertionError(("other birth-face component", edge, sign))
        other_feature_components[f"S_edge_{edge[0]}_{edge[1]}"] = {
            "sign": sign, "leaves": leaves, "margin_log10": margin,
        }
    for component in ("t", "one_minus_t", "beta2"):
        poly = root_ledger["edge"][active_edge][component]
        sign, leaves, margin = ex.bernstein_sign(poly, common_root["lo"], common_root["hi"])
        if sign != 1:
            raise AssertionError(("other birth-edge component", component, sign))
        other_feature_components[f"H_{component}"] = {
            "sign": sign, "leaves": leaves, "margin_log10": margin,
        }
    # The directed face primitive and beta1 numerator are zero-equivalent and
    # have the same sign because gram, cc, reference >0 and cross_factor <0.
    if active_face != linked["face_raw"]:
        raise AssertionError("unexpected face-reference convention")

    # Exact cofactor tangent: four keep gradients vanish identically and the
    # fifth (birth) pairing is strictly negative on the entire root interval.
    selected = [8, 12, 19, 15, 14]
    tangent = ex.exact_antibirth_tangent(
        charts["star"], charts["vx"], charts["columns"], star_faces,
        selected, common_root["lo"], common_root["hi"],
    )
    tangent["selected_control_names"] = [charts["control_names"][i] for i in selected]

    radius = ex.Q(1, 100_000)
    quadrants = []
    for sx in (-1, 1):
        for sy in (-1, 1):
            point = ex.point_on_chart(
                charts["star"], charts["vx"], charts["vy"], sx * radius, sy * radius
            )
            cell = ex.supporting_cell(point, star_faces)
            ledger, summary = ex.classify_point(point, star_faces)
            expected_class = [3, 2, 3] if sy < 0 else [2, 2, 2]
            if summary["class"] != expected_class:
                raise AssertionError(((sx, sy), summary["class"]))
            edges = set(map(tuple, cell["edges"]))
            if not rails <= edges:
                raise AssertionError(("quadrant rail loss", sx, sy))
            shared_value = ledger["edge"][(8, 245)]["beta1"]
            expected_shared_sign = 1 if sy < 0 else -1
            if (1 if shared_value > 0 else -1) != expected_shared_sign:
                raise AssertionError(("quadrant shared sign", sx, sy))
            quadrants.append({
                "quadrant": [sx, sy],
                "f_vector": cell["f_vector"],
                "euler": cell["euler"],
                "strict_support_count": cell["strict_support_count"],
                "min_support_log10_abs": cell["min_support_log10_abs"],
                "class": summary["class"],
                "stable_faces": summary["stable_faces"],
                "unstable_vertices": summary["unstable_vertices"],
                "saddle_edges": summary["saddle_edges"],
                "shared_birth_sign": expected_shared_sign,
                "shared_birth_log10_abs": ex.qlog10(shared_value),
                "all_37_rails": True,
            })

    # Entire continuous L, not a sample list.  The exhaustive witness set
    # proves the class, base, U8, every nonbirth condition, and topology.
    protected = {
        "stable": [sorted(ex.BASE), [7, 8, 245]],
        "unstable": [8, 54],
        "saddles": [[6, 7], [9, 10]],
    }
    l_segments = [
        ex.line_on_chart(charts["star"], charts["vx"], charts["vy"],
                         -radius, ex.Q(0), -radius, radius),
        ex.line_on_chart(charts["star"], charts["vx"], charts["vy"],
                         -radius, radius, radius, radius),
    ]
    l_path = [ex.certify_path_segment(segment, star_faces, protected) for segment in l_segments]
    for row in l_path:
        if row["start_class"]["class"] != [2, 2, 2]:
            raise AssertionError(row["start_class"])

    # First hard support wall on the post-bypass adaptive direction.
    adaptive_line = ex.line_points(charts["adaptive_start"], charts["vt"])
    circuit = ex.circuit_polynomial(adaptive_line)
    circuit_root = ex.isolate_monotone_root(
        circuit, ex.Q(6, 10_000), ex.Q(75, 100_000), ex.Q(1, 10**24)
    )
    wall_order = ex.certify_first_support_wall(
        adaptive_line, star_faces, circuit_root, circuit
    )
    pre_t = circuit_root["lo"] - ex.Q(1, 1_000_000)
    post_t = circuit_root["hi"] + ex.Q(1, 50_000)
    pre_point = {i: tuple(z.eval(pre_t) for z in p) for i, p in adaptive_line.items()}
    post_point = {i: tuple(z.eval(post_t) for z in p) for i, p in adaptive_line.items()}
    pre_cell = ex.supporting_cell(pre_point, star_faces)
    _, pre_class = ex.classify_point(pre_point, star_faces)
    if post_faces is None:
        post_faces = numeric_faces(post_point)
    post_cell = ex.supporting_cell(post_point, post_faces)
    _, post_class = ex.classify_point(post_point, post_faces)
    if pre_cell["f_vector"] != [61, 162, 103] or post_cell["f_vector"] != [60, 160, 102]:
        raise AssertionError((pre_cell["f_vector"], post_cell["f_vector"]))
    if 9 not in pre_cell["active_labels"] or 9 in post_cell["active_labels"]:
        raise AssertionError("row 9 active-order audit failed")
    if pre_class["class"] != [2, 2, 2] or post_class["class"] != [2, 2, 2]:
        raise AssertionError((pre_class, post_class))
    pre_edges = set(map(tuple, pre_cell["edges"]))
    post_edges = set(map(tuple, post_cell["edges"]))
    if not rails <= pre_edges or not rails <= post_edges:
        raise AssertionError("forced rail lost at hard wall")
    pre_face_keys, _ = face_edge_sets(star_faces)
    post_face_keys, _ = face_edge_sets(post_faces)

    numeric_wall = json.loads(NUMERIC_WALL.read_text())
    numeric_root = float(numeric_wall["circuit_determinant_root"])
    exact_mid = float((circuit_root["lo"] + circuit_root["hi"]) / 2)
    if abs(numeric_root - exact_mid) > 2e-15:
        raise AssertionError(("numeric/exact circuit mismatch", numeric_root, exact_mid))

    continuation = json.loads(CONTINUATION.read_text())
    p0 = np.asarray(continuation["accepted"][0]["parameters"], dtype=float)
    p1 = np.asarray(continuation["accepted"][1]["parameters"], dtype=float)
    common_mid = float((common_root["lo"] + common_root["hi"]) / 2)
    alpha_match = float(charts["alpha_star"]) + common_mid / float(np.linalg.norm(p1 - p0))

    source_hashes = {
        path.name: ex.sha256(path)
        for path in (SOURCE, SOURCE_AUDIT, ATLAS_JSON, CONTINUATION, ROOTS, ADAPTIVE, NUMERIC_WALL)
    }
    payload = {
        "version": 1,
        "verdict": "EXACT_DIRECTED_LOCAL_BYPASS_AND_FIRST_HARD_WALL_PASS",
        "scope": (
            "Exact theorem for the explicitly frozen finite-decimal rational 22-control chart, "
            "its supplied exact supporting face ledgers, the two continuous L segments, and the "
            "saved adaptive ray. It is local/fixed-chart only; it is not a global existence theorem."
        ),
        "source_hashes_sha256": source_hashes,
        "chart": {
            "construction": (
                "source decimals read as Fractions; base rows projected to the exact plane through "
                "rows 0,54,1; saved chart columns rationalized at 17 digits then exactly reprojected"
            ),
            "control_names": charts["control_names"],
            "base_plane_normal_exact": [ex.qs(x) for x in charts["plane_normal"]],
            "max_base_repair_coefficient_log10_abs": max(charts["repair_log"].values()),
            "radius_exact": ex.qs(radius),
            "star_faces": star_faces,
            "star_faces_sha256": canonical_hash(star_faces),
            "star_support": {k: v for k, v in star_cell.items() if k != "edges"},
        },
        "linked_common_root": {
            "features": ["S(8,245,246):edge(8,245)", "H(8,245):beta1"],
            "shared_primitive": "N=(X245.n1)||n2||^2-(X245.n2)(n1.n2)",
            "shared_polynomial_exact": linked["shared"].exact(),
            "shared_polynomial_degree": linked["shared"].degree,
            "face_beta_identity_polynomial_exact": linked["identity"].exact(),
            "root_x": exact_root_record(common_root),
            "matched_original_alpha_decimal": alpha_match,
            "original_two_numeric_roots": json.loads(ROOTS.read_text())["roots_in_order"],
            "strict_factor_signs": factor_certificates,
            "strict_other_feature_components": other_feature_components,
            "conclusion": (
                "The two numerical roots are one exact root in the frozen chart: both active "
                "components share N, all denominator/factor signs are strict, and every other "
                "component of the two features stays strictly positive."
            ),
        },
        "independent_antibirth_tangent": tangent,
        "quadrant_cells": quadrants,
        "continuous_L_path": {
            "waypoints": [["-1/100000", "0"], ["-1/100000", "1/100000"],
                          ["1/100000", "1/100000"]],
            "segments": l_path,
            "protected_class": protected,
            "forced_rail_count": len(rails),
            "conclusion": (
                "Every supporting and exhaustive mechanics witness polynomial has a strict "
                "constant sign on both closed segments; hence the complete L path is fresh-hull "
                "valid, remains class (2,2,2), avoids both linked births, and preserves all rails."
            ),
        },
        "first_hard_wall": {
            "circuit": [8, 9, 10, 263],
            "determinant_polynomial_exact": circuit.exact(),
            "determinant_degree": circuit.degree,
            "root_t": exact_root_record(circuit_root),
            "numeric_audit_root": numeric_root,
            "support_order_certificate": wall_order,
            "pre_sample_t_exact": ex.qs(pre_t),
            "post_sample_t_exact": ex.qs(post_t),
            "pre_support": {k: v for k, v in pre_cell.items() if k != "edges"},
            "post_support": {k: v for k, v in post_cell.items() if k != "edges"},
            "pre_class": pre_class,
            "post_class": post_class,
            "post_faces": post_faces,
            "post_faces_sha256": canonical_hash(post_faces),
            "topology_flip": {
                "faces_removed": [list(x) for x in sorted(pre_face_keys - post_face_keys)],
                "faces_added": [list(x) for x in sorted(post_face_keys - pre_face_keys)],
                "edges_removed": [list(x) for x in sorted(pre_edges - post_edges)],
                "edges_added": [list(x) for x in sorted(post_edges - pre_edges)],
                "row9_active_before": True,
                "row9_active_after": False,
            },
            "conclusion": (
                "Exactly two prewall support slacks are proportional to det(8,9,10,263); all "
                "other support polynomials stay strict through the isolated root interval. "
                "Therefore this circuit is the first hard support/active-row wall on the saved ray."
            ),
        },
    }
    return payload


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    payload = compute()
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("BUILD_LOCAL_BYPASS_CERTIFICATE_PASS")
    print("common root x", payload["linked_common_root"]["root_x"]["midpoint_decimal"])
    print("L exact polynomial counts", [x["certified_polynomial_count"] for x in payload["continuous_L_path"]["segments"]])
    print("hard wall t", payload["first_hard_wall"]["root_t"]["midpoint_decimal"])
    print("output", args.output)


if __name__ == "__main__":
    main()

