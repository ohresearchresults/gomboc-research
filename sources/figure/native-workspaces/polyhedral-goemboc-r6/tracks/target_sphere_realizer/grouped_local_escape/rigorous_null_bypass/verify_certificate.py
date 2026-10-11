#!/usr/bin/env python3
"""Clean-room exact verifier for both grouped nullspace bypass certificates."""

from __future__ import annotations

import concurrent.futures
import json
import os
import sys
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import grouped_exact as gx  # noqa: E402


CERTIFICATE = HERE / "certificate.json"
SUMMARY = HERE / "verification_summary.json"
L_NODE_NAMES = ("A_pre", "B_buffered_pre", "C_buffered_post")
SHORT_RAIL = [228] + list(range(229, 247)) + [8]
LONG_RAIL = [228] + list(range(247, 265)) + [8]


def load_certificate():
    return json.loads(CERTIFICATE.read_text())


def points_from(packet):
    points = gx.decode_points(packet["coordinates"])
    if gx.point_hash(points) != packet["coordinate_hash"]:
        raise AssertionError("frozen coordinate hash mismatch")
    a = points[0]
    normal = gx.ex.cross(gx.ex.sub(points[1], a), gx.ex.sub(points[2], a))
    for i in gx.BASE:
        if gx.ex.dot(normal, gx.ex.sub(points[i], a)):
            raise AssertionError(("encoded base is not exactly planar", i))
    return points


def assert_actual_cell(points, faces, expected_class):
    packet = gx.point_audit(points, faces)
    support = packet["support"]
    mechanics = packet["mechanics"]
    if support["f_vector"] != [61, 162, 103] or support["euler"] != 2:
        raise AssertionError(("wrong actual cell", support["f_vector"], support["euler"]))
    if mechanics["class"] != expected_class:
        raise AssertionError(("wrong mechanics class", mechanics["class"], expected_class))
    expected_stable = {tuple(sorted(gx.BASE)), (7, 245, 246)}
    if {tuple(x) for x in mechanics["stable_faces"]} != expected_stable:
        raise AssertionError(("wrong stable faces", mechanics["stable_faces"]))
    edges = {tuple(edge) for edge in support["edges"]}
    for rail in (SHORT_RAIL, LONG_RAIL):
        for a, b in zip(rail, rail[1:]):
            if tuple(sorted((a, b))) not in edges:
                raise AssertionError(("missing forced rail edge", a, b))
    return packet


def verify_l_segment(round_name: str, index: int):
    certificate = load_certificate()
    data = certificate["rounds"][round_name]
    faces = data["faces"]
    start_name, end_name = L_NODE_NAMES[index], L_NODE_NAMES[index + 1]
    start = points_from(data["L_nodes"][start_name])
    end = points_from(data["L_nodes"][end_name])
    assert_actual_cell(start, faces, [2, 2, 2])
    assert_actual_cell(end, faces, [2, 2, 2])
    path = gx.planar_morph(start, end)
    audit = gx.audit_every_primitive(path, faces)
    if audit["certified_polynomial_count"] != 7904:
        raise AssertionError(("unexpected primitive count", audit["certified_polynomial_count"]))

    pairs = ["round2"] if round_name == "round2" else ["round2", "round3"]
    guards = {}
    for pair_name in pairs:
        shared, duplicate, spec = gx.pair_polynomials(path, faces, pair_name)
        if shared != duplicate:
            raise AssertionError("pair identity lost on L path")
        guards[pair_name] = {
            "vertex_primitive": spec["vertex_name"],
            "edge_primitive": spec["edge_name"],
            "directed_nonbirth_guard": gx.exact_sign_record(shared, expected=-1),
        }
    return {
        "kind": "L_segment",
        "round": round_name,
        "segment": f"{start_name}_to_{end_name}",
        "audit": audit,
        "positive_nonbirth_guards": guards,
    }


def verify_event(round_name: str):
    certificate = load_certificate()
    data = certificate["rounds"][round_name]
    faces = data["faces"]
    pre = points_from(data["event_snapshots"]["pre_open"])
    post = points_from(data["event_snapshots"]["post_open"])
    assert_actual_cell(pre, faces, [2, 2, 2])
    assert_actual_cell(post, faces, [2, 3, 3])
    path = gx.planar_morph(pre, post)
    shared, duplicate, spec = gx.pair_polynomials(path, faces, round_name)
    if shared != duplicate:
        raise AssertionError("literal common numerator identity failed")
    if shared.eval(Q(0)) >= 0 or shared.eval(Q(1)) <= 0:
        raise AssertionError("event endpoints do not straddle directed wall")
    derivative = gx.exact_sign_record(shared.derivative(), expected=1)
    root = gx.root_record(shared)
    gx.verify_root_record(shared, root)
    skipped = frozenset((spec["vertex_name"], spec["edge_name"]))
    other = gx.audit_every_primitive(path, faces, skip=skipped)
    if other["certified_polynomial_count"] != 7902:
        raise AssertionError(("wrong event primitive count", other["certified_polynomial_count"]))

    previous = None
    if round_name == "round3":
        old_shared, old_duplicate, old_spec = gx.pair_polynomials(path, faces, "round2")
        if old_shared != old_duplicate:
            raise AssertionError("previous-wall pair identity failed")
        previous = {
            "vertex_primitive": old_spec["vertex_name"],
            "edge_primitive": old_spec["edge_name"],
            "positive_nonbirth_guard": gx.exact_sign_record(old_shared, expected=-1),
        }
    return {
        "kind": "shared_event",
        "round": round_name,
        "identity": {
            "vertex_formula": spec["identity"][0],
            "edge_formula": spec["identity"][1],
            "literal_polynomial_equality": True,
            "degree": shared.degree,
            "common_numerator_coefficients": shared.exact(),
            "common_numerator_digest": gx.canonical_hash(shared.exact()),
        },
        "unique_root": root,
        "whole_event_derivative": derivative,
        "all_other_primitives": other,
        "previous_wall_guard": previous,
    }


def verify_round4_first_wall():
    certificate = load_certificate()
    data = certificate["round4_plus"]
    faces = data["faces"]
    start = points_from(data["nodes"]["round3_C"])
    end = points_from(data["nodes"]["round4"])
    assert_actual_cell(start, faces, [2, 2, 2])
    assert_actual_cell(end, faces, [2, 2, 2])
    path = gx.planar_morph(start, end)
    shared, duplicate, spec = gx.pair_polynomials(path, faces, "round2")
    if shared != duplicate:
        raise AssertionError("round4 shared-pair identity failed")
    root = gx.root_record(shared)
    verified_root = gx.verify_root_record(shared, root)
    lo, hi = verified_root["lo"], verified_root["hi"]
    prefix_guard = gx.exact_sign_record(shared, Q(0), lo, expected=-1, max_depth=80)
    other = gx.audit_every_primitive(
        path,
        faces,
        Q(0),
        hi,
        skip=frozenset((spec["vertex_name"], spec["edge_name"])),
        max_depth=60,
    )
    if other["certified_polynomial_count"] != 7902:
        raise AssertionError("round4 first-wall primitive count mismatch")
    post_parameter = hi + Q(1, 10**8)
    post = gx.evaluate_path(path, post_parameter)
    post_audit = assert_actual_cell(post, faces, [2, 3, 3])
    new_shared, new_duplicate, new_spec = gx.pair_polynomials(path, faces, "round3")
    if new_shared != new_duplicate:
        raise AssertionError("round4 retained pair identity failed")
    retained = gx.exact_sign_record(new_shared, Q(0), post_parameter, expected=-1)
    return {
        "kind": "round4_first_wall",
        "path": "round3_C_to_round4 exact planar morph",
        "identity": {
            "vertex_formula": spec["identity"][0],
            "edge_formula": spec["identity"][1],
            "literal_polynomial_equality": True,
            "degree": shared.degree,
            "common_numerator_coefficients": shared.exact(),
            "common_numerator_digest": gx.canonical_hash(shared.exact()),
        },
        "first_root": root,
        "strict_class222_prefix_guard": prefix_guard,
        "all_other_primitives_through_root": other,
        "post_root_sample": {
            "parameter": gx.ex.qs(post_parameter),
            "coordinate_hash": post_audit["coordinate_hash"],
            "class": post_audit["mechanics"]["class"],
        },
        "retained_round3_nonbirth_guard": {
            "pair": [new_spec["vertex_name"], new_spec["edge_name"]],
            "certificate": retained,
        },
    }


def worker(task):
    if task[0] == "L":
        return task, verify_l_segment(task[1], task[2])
    if task[0] == "event":
        return task, verify_event(task[1])
    if task[0] == "round4":
        return task, verify_round4_first_wall()
    raise AssertionError(task)


def verify_hashes(certificate):
    core = gx.ROOT / certificate["core_dependency"]["path"]
    if gx.ex.sha256(core) != certificate["core_dependency"]["sha256"]:
        raise AssertionError("exact-core source hash mismatch")
    for relative, expected in certificate["input_hashes"].items():
        path = gx.ROOT / relative
        if gx.ex.sha256(path) != expected:
            raise AssertionError(("input source hash mismatch", relative))
    for data in certificate["rounds"].values():
        if gx.canonical_hash(data["faces"]) != data["face_ledger_hash"]:
            raise AssertionError("embedded face-ledger hash mismatch")
    if gx.canonical_hash(certificate["round4_plus"]["faces"]) != certificate["round4_plus"]["face_ledger_hash"]:
        raise AssertionError("round4 face-ledger hash mismatch")


def verify_frozen_cells(certificate):
    summaries = {}
    for round_name, data in certificate["rounds"].items():
        faces = data["faces"]
        event = {}
        for name, expected in (("pre_open", [2, 2, 2]), ("post_open", [2, 3, 3])):
            event[name] = assert_actual_cell(
                points_from(data["event_snapshots"][name]), faces, expected
            )["coordinate_hash"]
        quadrants = {}
        for name, packet in sorted(data["quadrants"].items()):
            expected = [2, 3, 3] if "_v-1" in name else [2, 2, 2]
            audit = assert_actual_cell(points_from(packet), faces, expected)
            quadrants[name] = {
                "coordinate_hash": audit["coordinate_hash"],
                "class": audit["mechanics"]["class"],
            }
        nodes = {}
        for name, packet in data["L_nodes"].items():
            audit = assert_actual_cell(points_from(packet), faces, [2, 2, 2])
            nodes[name] = audit["coordinate_hash"]
        summaries[round_name] = {
            "face_ledger_hash": data["face_ledger_hash"],
            "event_snapshot_hashes": event,
            "four_fresh_quadrant_cells": quadrants,
            "L_node_hashes": nodes,
        }
    return summaries


def main():
    certificate = load_certificate()
    if certificate.get("version") != 1:
        raise AssertionError("wrong certificate version")
    verify_hashes(certificate)
    frozen = verify_frozen_cells(certificate)
    tasks = [
        ("L", "round2", 0),
        ("L", "round2", 1),
        ("L", "round3", 0),
        ("L", "round3", 1),
        ("event", "round2"),
        ("event", "round3"),
        ("round4",),
    ]
    results = {}
    workers = min(4, os.cpu_count() or 1)
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(worker, task) for task in tasks]
        for future in concurrent.futures.as_completed(futures):
            task, result = future.result()
            results[repr(task)] = result
    summary = {
        "version": 1,
        "certificate_sha256": gx.ex.sha256(CERTIFICATE),
        "theorem_scope": certificate["theorem_scope"],
        "frozen_cells": frozen,
        "proofs": results,
    }
    SUMMARY.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")

    for round_name in ("round2", "round3"):
        event = results[repr(("event", round_name))]
        interval = event["unique_root"]["decimal_interval"]
        print(
            f"{round_name.upper()}_COMMON_NUMERATOR_PASS "
            f"root=[{interval[0]:.17g},{interval[1]:.17g}]"
        )
    round4 = results[repr(("round4",))]
    interval = round4["first_root"]["decimal_interval"]
    print(
        "ROUND4_FIRST_HARD_EVENT_PASS "
        f"U263/H(10,263) root=[{interval[0]:.17g},{interval[1]:.17g}]"
    )
    print("EXACT_DIRECTED_GROUPED_NULLSPACE_BYPASS_PASS")


if __name__ == "__main__":
    main()

