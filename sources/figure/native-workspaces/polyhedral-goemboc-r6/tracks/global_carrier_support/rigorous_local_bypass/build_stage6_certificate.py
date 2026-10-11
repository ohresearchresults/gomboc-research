#!/usr/bin/env python3
"""Exact/directed audit of the stage-6 tetrahedral topology flip."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import numpy as np
from scipy.spatial import ConvexHull


HERE = Path(__file__).resolve().parent
TRACK = HERE.parent
ROOT = HERE.parents[2]
ATLAS_DIR = ROOT / "tracks" / "circuit_atlas"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(TRACK))

import exact_core as ex  # noqa: E402
from actual_hull_mechanics import _merge_coplanar_facets  # noqa: E402
from build_certificate import canonical_hash  # noqa: E402


SOURCE = ATLAS_DIR / "row54_far_rebuilt.csv"
SOURCE_AUDIT = ATLAS_DIR / "row54_far_rebuilt_audit.json"
BIRTH_ATLAS = TRACK / "local_birth_atlas.json"
BASE_ADAPTIVE = TRACK / "adaptive_birth_bypass.json"
STAGE6 = TRACK / "adaptive_five_circuit_stage6.json"
STAGE6_AUDIT = TRACK / "stage6_topology_wall_audit.json"
STAGE6_PRE = TRACK / "stage6_topology_wall_pre.csv"
STAGE6_POST = TRACK / "stage6_topology_wall_post.csv"
OUTPUT = HERE / "stage6_certificate.json"
CIRCUIT = (7, 8, 245, 246)


def numeric_faces(points):
    labels = sorted(points)
    array = np.asarray([[float(x) for x in points[i]] for i in labels])
    cycles, _ = _merge_coplanar_facets(array, ConvexHull(array))
    return [[labels[j] for j in cycle] for cycle in cycles]


def root_record(root):
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
    }


def face_edge_sets(faces):
    face_keys = {tuple(sorted(face)) for face in faces}
    edges = set()
    for cycle in faces:
        for a, b in zip(cycle, cycle[1:] + cycle[:1]):
            edges.add(tuple(sorted((a, b))))
    return face_keys, edges


def exact_wall_support(line, wall_faces, root, target):
    all_labels = set(line)
    support_count = 0
    support_leaves = 0
    member_target_equalities = []
    worst = None
    for fi, cycle in enumerate(wall_faces):
        n = ex.cycle_normal(cycle, line)
        a = line[cycle[0]]
        for label in cycle[1:]:
            value = ex.dot(n, ex.sub(line[label], a))
            if value == ex.P.zero():
                continue
            ratio = ex.proportional(value, target)
            if ratio is None:
                raise AssertionError(("wall member is not coplanar at target root", fi, label))
            member_target_equalities.append({
                "face_index": fi, "member": label, "target_ratio_exact": ex.qs(ratio)
            })
        for witness in sorted(all_labels - set(cycle)):
            value = ex.dot(n, ex.sub(line[witness], a))
            sign, leaves, margin = ex.bernstein_sign(value, root["lo"], root["hi"])
            middle_sign = 1 if value.eval((root["lo"] + root["hi"]) / 2) > 0 else -1
            if sign != middle_sign:
                raise AssertionError(("wall support sign", fi, witness))
            support_count += 1
            support_leaves += leaves
            worst = margin if worst is None else min(worst, margin)
    incidence, _, _ = ex.edge_data(wall_faces)
    active = set().union(*(set(face) for face in wall_faces))
    return {
        "f_vector_at_root": [len(active), len(incidence), len(wall_faces)],
        "euler_at_root": len(active) - len(incidence) + len(wall_faces),
        "target_coplanarity_equalities": member_target_equalities,
        "strict_nonmember_support_polynomial_count": support_count,
        "support_bernstein_leaf_count": support_leaves,
        "min_support_bernstein_log10_abs": worst,
    }


def feature_transition(pre_ledger, pre_summary, post_ledger, post_summary):
    old_faces = ((7, 8, 245), (8, 245, 246))
    new_faces = ((7, 8, 246), (7, 245, 246))
    pre_face_keys = set(pre_ledger["face"])
    post_face_keys = set(post_ledger["face"])
    if not set(old_faces) <= pre_face_keys or set(old_faces) & post_face_keys:
        raise AssertionError("old face-key transition failed")
    if set(new_faces) & pre_face_keys or not set(new_faces) <= post_face_keys:
        raise AssertionError("new face-key transition failed")
    if (8, 245) not in pre_ledger["edge"] or (8, 245) in post_ledger["edge"]:
        raise AssertionError("old diagonal transition failed")
    if (7, 246) in pre_ledger["edge"] or (7, 246) not in post_ledger["edge"]:
        raise AssertionError("new diagonal transition failed")

    post_new_edge = post_ledger["edge"][(7, 246)]
    components = ("t", "one_minus_t", "beta1", "beta2")
    witness = min(components, key=post_new_edge.__getitem__)
    if post_new_edge[witness] >= 0:
        raise AssertionError("new diagonal unexpectedly saddle")
    post_stable = {tuple(x) for x in post_summary["stable_faces"]}
    if (7, 8, 246) not in post_stable or (7, 245, 246) in post_stable:
        raise AssertionError("post stable-face transfer failed")
    return {
        "pre_side": {
            "stable_local_face": [7, 8, 245],
            "nonstable_local_face": [8, 245, 246],
            "nonsaddle_diagonal": [8, 245],
            "class": pre_summary["class"],
        },
        "wall": {
            "merged_face": [7, 8, 245, 246],
            "old_face_keys_and_diagonal_cease_to_be_separate": True,
        },
        "post_side": {
            "stable_local_face_born": [7, 8, 246],
            "nonstable_local_face_born": [7, 245, 246],
            "new_nonsaddle_diagonal": [7, 246],
            "new_diagonal_negative_component": witness,
            "new_diagonal_negative_component_log10_abs": ex.qlog10(post_new_edge[witness]),
            "class": post_summary["class"],
        },
        "no_vertex_or_saddle_birth": (
            pre_summary["unstable_vertices"] == post_summary["unstable_vertices"] == [8, 54]
            and pre_summary["saddle_edges"] == post_summary["saddle_edges"] == [[6, 7], [9, 10]]
        ),
    }


def compute(pre_faces=None, post_faces=None):
    base = ex.build_charts(SOURCE, BIRTH_ATLAS, BASE_ADAPTIVE)
    stage = json.loads(STAGE6.read_text())
    parameters = [ex.Q(str(x)) for x in stage["trace"][-1]["parameters"]]
    direction = [ex.Q(str(x)) for x in stage["wall"]["direction"]]
    start = ex.apply_columns(base["rows"], base["columns"], parameters)
    velocity = ex.combine_columns(base["columns"], direction, sorted(base["rows"]))
    line = ex.line_points(start, velocity)
    if pre_faces is None:
        pre_faces = numeric_faces(start)
    start_support = ex.supporting_cell(start, pre_faces)
    if start_support["f_vector"] != [61, 162, 103]:
        raise AssertionError(start_support["f_vector"])

    target = ex.circuit_polynomial(line, CIRCUIT)
    root = ex.isolate_monotone_root(
        target, ex.Q(74, 10_000), ex.Q(76, 10_000), ex.Q(1, 10**24)
    )
    order = ex.certify_first_support_wall(line, pre_faces, root, target)

    old_keys = {(7, 8, 245), (8, 245, 246)}
    removed = [face for face in pre_faces if tuple(sorted(face)) in old_keys]
    if {tuple(sorted(face)) for face in removed} != old_keys:
        raise AssertionError(("pre flip faces missing", removed))
    wall_faces = [face for face in pre_faces if tuple(sorted(face)) not in old_keys]
    wall_faces.append([245, 7, 8, 246])
    wall_support = exact_wall_support(line, wall_faces, root, target)
    if wall_support["f_vector_at_root"] != [61, 161, 102] or wall_support["euler_at_root"] != 2:
        raise AssertionError(wall_support)
    wall_protected = {
        "stable": [sorted(ex.BASE), [7, 8, 245, 246]],
        "unstable": [8, 54],
        "saddles": [[6, 7], [9, 10]],
    }
    wall_mechanics = ex.certify_mechanics_interval(
        line, wall_faces, wall_protected, root["lo"], root["hi"]
    )
    if wall_mechanics["midpoint_class"]["class"] != [2, 2, 2]:
        raise AssertionError(wall_mechanics["midpoint_class"])

    midpoint = (root["lo"] + root["hi"]) / 2
    pre_t = midpoint - ex.Q(1, 500_000)
    post_t = midpoint + ex.Q(1, 500_000)
    pre_point = {i: tuple(z.eval(pre_t) for z in p) for i, p in line.items()}
    post_point = {i: tuple(z.eval(post_t) for z in p) for i, p in line.items()}
    pre_cell = ex.supporting_cell(pre_point, pre_faces)
    pre_ledger, pre_summary = ex.classify_point(pre_point, pre_faces)
    if post_faces is None:
        post_faces = numeric_faces(post_point)
    post_cell = ex.supporting_cell(post_point, post_faces)
    post_ledger, post_summary = ex.classify_point(post_point, post_faces)
    if pre_cell["f_vector"] != [61, 162, 103] or post_cell["f_vector"] != [61, 162, 103]:
        raise AssertionError((pre_cell["f_vector"], post_cell["f_vector"]))
    if pre_summary["class"] != [2, 2, 2] or post_summary["class"] != [2, 2, 2]:
        raise AssertionError((pre_summary, post_summary))

    rails = {
        tuple(sorted(edge))
        for edge in json.loads(SOURCE_AUDIT.read_text())["fresh_hull_audit"]["forced_rail_edges"]
    }
    _, pre_edges = face_edge_sets(pre_faces)
    _, post_edges = face_edge_sets(post_faces)
    if not rails <= pre_edges or not rails <= post_edges:
        raise AssertionError("rail lost across stage6 flip")
    pre_face_keys, _ = face_edge_sets(pre_faces)
    post_face_keys, _ = face_edge_sets(post_faces)
    transition = feature_transition(pre_ledger, pre_summary, post_ledger, post_summary)
    if not transition["no_vertex_or_saddle_birth"]:
        raise AssertionError("unexpected post-side feature birth")

    numeric = json.loads(STAGE6_AUDIT.read_text())
    numeric_estimate = float(numeric["estimate"])
    exact_midpoint = float(midpoint)
    if abs(numeric_estimate - exact_midpoint) > 1e-8:
        raise AssertionError((numeric_estimate, exact_midpoint))

    source_paths = (
        SOURCE, SOURCE_AUDIT, BIRTH_ATLAS, BASE_ADAPTIVE, STAGE6,
        STAGE6_AUDIT, STAGE6_PRE, STAGE6_POST,
    )
    payload = {
        "version": 1,
        "verdict": "EXACT_DIRECTED_STAGE6_TETRAHEDRAL_FLIP_PASS",
        "scope": (
            "Exact theorem for the nearby rational chart obtained from the saved finite-decimal "
            "stage-6 ray with exact base-plane repair. It certifies this local ray and flip only, "
            "not a global continuation theorem or the unmodified binary64/Qhull tolerance model."
        ),
        "source_hashes_sha256": {path.name: ex.sha256(path) for path in source_paths},
        "chart_note": {
            "construction": (
                "same 22-control rational chart as certificate.json: exact Fraction source, exact "
                "base plane through 0,54,1, 17-digit rationalized tangent columns"
            ),
            "numeric_wall_estimate": numeric_estimate,
            "exact_chart_root_shift_from_numeric": exact_midpoint - numeric_estimate,
        },
        "circuit_root": {
            "circuit": list(CIRCUIT),
            "determinant_polynomial_exact": target.exact(),
            "determinant_degree": target.degree,
            "root": root_record(root),
            "support_order": order,
            "conclusion": (
                "Exactly the two pre-flip support slacks are proportional to det(7,8,245,246); "
                "all other 5957 supporting slacks remain strict through the isolated root."
            ),
        },
        "face_ledgers": {
            "pre_faces": pre_faces,
            "pre_faces_sha256": canonical_hash(pre_faces),
            "wall_faces": wall_faces,
            "wall_faces_sha256": canonical_hash(wall_faces),
            "post_faces": post_faces,
            "post_faces_sha256": canonical_hash(post_faces),
        },
        "exact_wall": {
            "support": wall_support,
            "mechanics": wall_mechanics,
            "merged_supporting_face": [7, 8, 245, 246],
            "class": [2, 2, 2],
        },
        "sides": {
            "pre_t_exact": ex.qs(pre_t),
            "post_t_exact": ex.qs(post_t),
            "pre_support": {k: v for k, v in pre_cell.items() if k != "edges"},
            "post_support": {k: v for k, v in post_cell.items() if k != "edges"},
            "feature_transition": transition,
            "topology_flip": {
                "faces_removed": [list(x) for x in sorted(pre_face_keys - post_face_keys)],
                "faces_added": [list(x) for x in sorted(post_face_keys - pre_face_keys)],
                "edges_removed": [list(x) for x in sorted(pre_edges - post_edges)],
                "edges_added": [list(x) for x in sorted(post_edges - pre_edges)],
                "active_labels_unchanged": pre_cell["active_labels"] == post_cell["active_labels"],
                "base_and_all_37_rails_on_both_sides": True,
            },
        },
    }
    return payload


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    payload = compute()
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("BUILD_STAGE6_EXACT_FLIP_CERTIFICATE_PASS")
    print("root", payload["circuit_root"]["root"]["midpoint_decimal"])
    print("order strict supports", payload["circuit_root"]["support_order"]["other_strict_support_polynomial_count"])
    print("wall mechanics polynomials", payload["exact_wall"]["mechanics"]["certified_polynomial_count"])
    print("output", args.output)


if __name__ == "__main__":
    main()

