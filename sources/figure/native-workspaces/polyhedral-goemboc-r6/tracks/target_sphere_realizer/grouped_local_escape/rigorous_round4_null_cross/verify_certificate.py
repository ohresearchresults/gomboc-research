#!/usr/bin/env python3
"""Independent exact verifier for the round-4 three-segment null cross."""

from __future__ import annotations

import concurrent.futures
import json
import os
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cross_exact as cx  # noqa: E402


CERTIFICATE = HERE / "certificate.json"
SUMMARY = HERE / "verification_summary.json"


def load_certificate():
    return json.loads(CERTIFICATE.read_text())


def points_from(packet):
    points = cx.gx.decode_points(packet["coordinates"])
    if cx.gx.point_hash(points) != packet["coordinate_hash"]:
        raise AssertionError("coordinate hash mismatch")
    anchor = points[0]
    normal = cx.ex.cross(cx.ex.sub(points[1], anchor), cx.ex.sub(points[2], anchor))
    for label in cx.BASE:
        if cx.ex.dot(normal, cx.ex.sub(points[label], anchor)):
            raise AssertionError(("base row is not exactly planar", label))
    return points


def faces_from(certificate, name):
    packet = certificate["face_ledgers"][name]
    if cx.gx.canonical_hash(packet["cycles"]) != packet["canonical_hash"]:
        raise AssertionError(("face canonical hash mismatch", name))
    return packet["cycles"]


def expected_stable(lattice):
    local = {
        "pre": (7, 245, 246),
        "wall": (7, 8, 245, 246),
        "far": (7, 8, 245),
    }[lattice]
    return {tuple(sorted(cx.BASE)), local}


def assert_actual_cell(points, faces, lattice):
    audit = cx.gx.point_audit(points, faces)
    expected_f = [61, 161, 102] if lattice == "wall" else [61, 162, 103]
    if audit["support"]["f_vector"] != expected_f or audit["support"]["euler"] != 2:
        raise AssertionError(("actual lattice mismatch", lattice, audit["support"]))
    mechanics = audit["mechanics"]
    if mechanics["class"] != [2, 2, 2]:
        raise AssertionError(("mechanics class mismatch", lattice, mechanics))
    if {tuple(face) for face in mechanics["stable_faces"]} != expected_stable(lattice):
        raise AssertionError(("stable-face transfer mismatch", lattice, mechanics))
    if mechanics["unstable_vertices"] != [8, 54]:
        raise AssertionError(("unstable vertices mismatch", mechanics))
    if mechanics["saddle_edges"] != [[6, 7], [198, 263]]:
        raise AssertionError(("saddle edges mismatch", mechanics))
    edges = {tuple(edge) for edge in audit["support"]["edges"]}
    for rail in (cx.SHORT_RAIL, cx.LONG_RAIL):
        for a, b in zip(rail, rail[1:]):
            if tuple(sorted((a, b))) not in edges:
                raise AssertionError(("forced rail missing", lattice, a, b))
    return audit


def middle_objects(certificate):
    start = points_from(certificate["nodes"]["pre_buffer"])
    end = points_from(certificate["nodes"]["far_good"])
    path = cx.gx.planar_morph(start, end)
    target = cx.circuit_polynomial(path)
    return path, target


def verify_full_interval(task_name):
    certificate = load_certificate()
    root = certificate["circuit"]["unique_root"]
    if task_name == "pre_to_buffer":
        start_name, end_name, lattice, lo, hi = "source", "pre_buffer", "pre", Q(0), Q(1)
    elif task_name == "buffered_cross_pre":
        start_name, end_name, lattice = "pre_buffer", "far_good", "pre"
        lo, hi = Q(0), Q(root["lo"])
    elif task_name == "buffered_cross_far":
        start_name, end_name, lattice = "pre_buffer", "far_good", "far"
        lo, hi = Q(root["hi"]), Q(1)
    elif task_name == "far_deepen":
        start_name, end_name, lattice, lo, hi = "far_good", "deep_far", "far", Q(0), Q(1)
    else:
        raise AssertionError(task_name)
    start = points_from(certificate["nodes"][start_name])
    end = points_from(certificate["nodes"][end_name])
    faces = faces_from(certificate, lattice)
    path = cx.gx.planar_morph(start, end)
    audit = cx.gx.audit_every_primitive(path, faces, lo, hi, max_depth=80)
    if audit["certified_polynomial_count"] != 7904:
        raise AssertionError(("incomplete full primitive audit", task_name, audit))
    guards = cx.four_guard_audit(path, faces, lo, hi)
    if len(guards) != 4:
        raise AssertionError("incomplete old guard audit")
    return {
        "kind": "full_interval",
        "name": task_name,
        "lattice": lattice,
        "audit": audit,
        "four_old_UH_guards": guards,
    }


def verify_root_local(lattice):
    certificate = load_certificate()
    path, target = middle_objects(certificate)
    faces = faces_from(certificate, lattice)
    root = certificate["circuit"]["unique_root"]
    lo, hi = Q(root["lo"]), Q(root["hi"])
    audit = cx.audit_root_neighborhood(path, faces, target, lo, hi)
    guards = cx.four_guard_audit(path, faces, lo, hi)
    return {
        "kind": "root_neighborhood",
        "lattice": lattice,
        "audit": audit,
        "four_old_UH_guards": guards,
    }


def verify_wall():
    certificate = load_certificate()
    path, target = middle_objects(certificate)
    faces = faces_from(certificate, "wall")
    root = certificate["circuit"]["unique_root"]
    lo, hi = Q(root["lo"]), Q(root["hi"])
    support = cx.wall_support_audit(path, faces, target, lo, hi)
    mechanics = cx.wall_mechanics_audit(path, faces, lo, hi)
    guards = cx.four_guard_audit(path, faces, lo, hi)
    if support["f_vector"] != [61, 161, 102] or support["euler"] != 2:
        raise AssertionError(("bad grouped wall", support))
    if mechanics["midpoint_formula_class"]["class"] != [2, 2, 2]:
        raise AssertionError(("bad wall mechanics", mechanics))
    return {
        "kind": "algebraic_wall",
        "support": support,
        "mechanics": mechanics,
        "four_old_UH_guards": guards,
    }


def worker(task):
    if task[0] == "full":
        return task, verify_full_interval(task[1])
    if task[0] == "root_local":
        return task, verify_root_local(task[1])
    if task[0] == "wall":
        return task, verify_wall()
    raise AssertionError(task)


def verify_hashes(certificate):
    for relative, expected in certificate["proof_dependencies"].items():
        if cx.ex.sha256(cx.ROOT / relative) != expected:
            raise AssertionError(("proof dependency hash mismatch", relative))
    for relative, expected in certificate["input_hashes"].items():
        if cx.ex.sha256(cx.ROOT / relative) != expected:
            raise AssertionError(("input hash mismatch", relative))
    for packet in certificate["nodes"].values():
        source = cx.ROOT / packet["source_file"]
        if cx.ex.sha256(source) != packet["source_sha256"]:
            raise AssertionError(("node source hash mismatch", packet["source_file"]))
    for packet in certificate["face_ledgers"].values():
        source = cx.ROOT / packet["source_file"]
        if cx.ex.sha256(source) != packet["source_sha256"]:
            raise AssertionError(("face source hash mismatch", packet["source_file"]))


def verify_face_transition(certificate):
    pre = faces_from(certificate, "pre")
    wall = faces_from(certificate, "wall")
    far = faces_from(certificate, "far")
    pre_faces, pre_edges = cx.face_edge_sets(pre)
    wall_faces, wall_edges = cx.face_edge_sets(wall)
    far_faces, far_edges = cx.face_edge_sets(far)
    removed_faces = sorted(pre_faces - far_faces)
    added_faces = sorted(far_faces - pre_faces)
    removed_edges = sorted(pre_edges - far_edges)
    added_edges = sorted(far_edges - pre_edges)
    if removed_faces != [(7, 8, 246), (7, 245, 246)]:
        raise AssertionError(("unexpected removed faces", removed_faces))
    if added_faces != [(7, 8, 245), (8, 245, 246)]:
        raise AssertionError(("unexpected added faces", added_faces))
    if removed_edges != [(7, 246)] or added_edges != [(8, 245)]:
        raise AssertionError(("unexpected diagonal flip", removed_edges, added_edges))
    expected_wall = (7, 8, 245, 246)
    if expected_wall not in wall_faces:
        raise AssertionError("merged quadrilateral absent")
    if not (pre_faces - set(removed_faces)) == (far_faces - set(added_faces)) == (wall_faces - {expected_wall}):
        raise AssertionError("nonlocal face lattice changed")
    common_rails = set()
    for rail in (cx.SHORT_RAIL, cx.LONG_RAIL):
        common_rails.update(tuple(sorted(e)) for e in zip(rail, rail[1:]))
    if not common_rails <= pre_edges or not common_rails <= wall_edges or not common_rails <= far_edges:
        raise AssertionError("rail lattice changes at flip")
    return {
        "removed_faces": [list(x) for x in removed_faces],
        "added_faces": [list(x) for x in added_faces],
        "removed_diagonal": [7, 246],
        "added_diagonal": [8, 245],
        "merged_wall_face": list(expected_wall),
        "all_other_faces_unchanged": True,
        "base_and_all_rails_in_pre_wall_far": True,
    }


def verify_frozen_nodes(certificate):
    pre_faces = faces_from(certificate, "pre")
    far_faces = faces_from(certificate, "far")
    result = {}
    for name, lattice in (
        ("source", "pre"),
        ("pre_buffer", "pre"),
        ("far_good", "far"),
        ("deep_far", "far"),
    ):
        points = points_from(certificate["nodes"][name])
        audit = assert_actual_cell(points, pre_faces if lattice == "pre" else far_faces, lattice)
        result[name] = {
            "coordinate_hash": audit["coordinate_hash"],
            "f_vector": audit["support"]["f_vector"],
            "class": audit["mechanics"]["class"],
        }
    return result


def verify_circuit(certificate):
    path, target = middle_objects(certificate)
    saved = certificate["circuit"]
    if list(cx.CIRCUIT) != saved["labels"]:
        raise AssertionError("wrong circuit labels")
    if target.degree != saved["polynomial_degree"] or target.exact() != saved["polynomial_coefficients_exact"]:
        raise AssertionError("circuit polynomial mismatch")
    if cx.gx.canonical_hash(target.exact()) != saved["polynomial_digest"]:
        raise AssertionError("circuit digest mismatch")
    derivative = cx.gx.exact_sign_record(target.derivative(), expected=-1, max_depth=80)
    if derivative != saved["whole_segment_derivative"]:
        raise AssertionError("circuit derivative certificate mismatch")
    rebuilt_root = cx.gx.root_record(target)
    if rebuilt_root != saved["unique_root"]:
        raise AssertionError("circuit root record mismatch")
    cx.gx.verify_root_record(target, saved["unique_root"])
    return {
        "degree": target.degree,
        "polynomial_digest": saved["polynomial_digest"],
        "whole_segment_derivative": derivative,
        "unique_root": saved["unique_root"],
    }


def check_factored_families(results):
    expected = {
        "pre": {
            "support:f4:w245": 1,
            "support:f9:w8": 1,
            "edge_gram:7,246": 2,
            "edge:7,246:beta1": 1,
            "edge:7,246:beta2": 1,
        },
        "far": {
            "support:f7:w246": 1,
            "support:f8:w7": 1,
            "edge_gram:8,245": 2,
            "edge:8,245:beta1": 1,
            "edge:8,245:beta2": 1,
        },
    }
    for lattice in ("pre", "far"):
        result = results[repr(("root_local", lattice))]["audit"]
        if result["total_primitive_count"] != 7904 or result["strict_primitive_count"] != 7899:
            raise AssertionError(("root-local primitive coverage", lattice, result))
        actual = {
            item["name"]: item["target_multiplicity"]
            for item in result["target_factored_primitives"]
        }
        if actual != expected[lattice]:
            raise AssertionError(("unexpected target factor family", lattice, actual))


def main():
    certificate = load_certificate()
    if certificate.get("version") != 1:
        raise AssertionError("wrong certificate version")
    verify_hashes(certificate)
    frozen = verify_frozen_nodes(certificate)
    transition = verify_face_transition(certificate)
    circuit = verify_circuit(certificate)
    tasks = [
        ("full", "pre_to_buffer"),
        ("full", "buffered_cross_pre"),
        ("full", "buffered_cross_far"),
        ("full", "far_deepen"),
        ("root_local", "pre"),
        ("root_local", "far"),
        ("wall",),
    ]
    results = {}
    with concurrent.futures.ProcessPoolExecutor(max_workers=min(4, os.cpu_count() or 1)) as pool:
        futures = [pool.submit(worker, task) for task in tasks]
        for future in concurrent.futures.as_completed(futures):
            task, result = future.result()
            results[repr(task)] = result
    check_factored_families(results)
    wall = results[repr(("wall",))]
    if wall["support"]["strict_nonmember_support_polynomial_count"] != 5900:
        raise AssertionError("incomplete wall support audit")
    if wall["mechanics"]["certified_polynomial_count"] != 1933:
        raise AssertionError("incomplete wall mechanics audit")
    for result in results.values():
        if "four_old_UH_guards" in result and len(result["four_old_UH_guards"]) != 4:
            raise AssertionError("four-guard coverage lost")

    summary = {
        "version": 1,
        "verdict": certificate["verdict"],
        "theorem_scope": certificate["theorem_scope"],
        "certificate_sha256": cx.ex.sha256(CERTIFICATE),
        "frozen_nodes": frozen,
        "face_transition": transition,
        "circuit": circuit,
        "continuum_proofs": results,
    }
    SUMMARY.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    root = circuit["unique_root"]["decimal_interval"]
    print("PRE_TO_BUFFER_CONTINUUM_PASS")
    print(f"BUFFERED_CROSS_UNIQUE_CIRCUIT_WALL_PASS root=[{root[0]:.17g},{root[1]:.17g}]")
    print("FAR_DEEPEN_CONTINUUM_PASS")
    print("FOUR_OLD_UH_GUARDS_PASS")
    print("EXACT_DIRECTED_ROUND4_NULL_CROSS_PASS")


if __name__ == "__main__":
    main()

