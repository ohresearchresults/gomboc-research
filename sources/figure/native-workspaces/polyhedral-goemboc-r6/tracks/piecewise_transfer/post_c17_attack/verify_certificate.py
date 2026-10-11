#!/usr/bin/env python3
"""Independent verifier for the post-C17 linked-death/support-flip package.

This verifier never calls the producer.  It reconstructs the two strict face
lattices by exhaustive all-triples supporting-plane enumeration, rebuilds all
six rational cells and own centroids, regenerates both event polynomials and
the complete mechanics/support/in-face guard families, and only then compares
the frozen artifacts and manifest.
"""
from __future__ import annotations

import csv
import json
import math
import time
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path

import post_c17_exact as pc

HERE = Path(__file__).resolve().parent
DATA = HERE / "certificate.json"
MANIFEST = HERE / "manifest.sha256"


def gcd_all(values):
    g = 0
    for value in values:
        g = math.gcd(g, abs(int(value)))
    return g


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def canon_plane(normal, height):
    g = gcd_all((*normal, height))
    assert g
    normal = tuple(z // g for z in normal)
    height //= g
    for z in (*normal, height):
        if z:
            if z < 0:
                normal = tuple(-v for v in normal)
                height = -height
            break
    return (*normal, height)


def integerize(rows):
    scale = 1
    for p in rows.values():
        for z in p:
            scale = lcm(scale, z.denominator)
    out = {i: tuple(int(z * scale) for z in p) for i, p in rows.items()}
    assert all(Q(out[i][k], scale) == rows[i][k] for i in rows for k in range(3))
    return out, scale


def exhaustive_supporting_planes(rows, proposed_faces):
    """All unique triples; proposed cycles are comparison targets only."""
    points, scale = integerize(rows)
    stored = {}
    for face in proposed_faces:
        cycle = face["cycle"]
        assert len(cycle) >= 3 and len(set(cycle)) == len(cycle)
        a, b, c = (points[i] for i in cycle[:3])
        normal = pc.ex.cross(pc.ex.sub(b, a), pc.ex.sub(c, a))
        assert normal != pc.ex.ZERO
        height = pc.ex.dot(normal, a)
        values = {i: pc.ex.dot(normal, p) - height for i, p in points.items()}
        assert not (any(v > 0 for v in values.values()) and any(v < 0 for v in values.values()))
        if any(v > 0 for v in values.values()):
            normal = tuple(-v for v in normal)
            height = -height
            values = {i: -v for i, v in values.items()}
        coplanar = frozenset(i for i, v in values.items() if v == 0)
        assert coplanar == frozenset(cycle)
        area = (0, 0, 0)
        for u, v in zip(cycle, cycle[1:] + cycle[:1]):
            area = pc.ex.add(area, pc.ex.cross(points[u], points[v]))
        assert pc.ex.dot(area, normal) > 0
        for j in range(len(cycle)):
            u = points[cycle[j - 1]]
            v = points[cycle[j]]
            w = points[cycle[(j + 1) % len(cycle)]]
            assert pc.ex.dot(pc.ex.cross(pc.ex.sub(v, u), pc.ex.sub(w, v)), normal) > 0
        key = canon_plane(normal, height)
        assert key not in stored
        stored[key] = coplanar

    coordinate_to_ids = defaultdict(list)
    for i, p in points.items():
        coordinate_to_ids[p].append(i)
    unique_points = list(coordinate_to_ids)
    found = {}
    for ia in range(len(unique_points) - 2):
        a = unique_points[ia]
        for ib in range(ia + 1, len(unique_points) - 1):
            ab = pc.ex.sub(unique_points[ib], a)
            for ic in range(ib + 1, len(unique_points)):
                normal = pc.ex.cross(ab, pc.ex.sub(unique_points[ic], a))
                if normal == pc.ex.ZERO:
                    continue
                height = pc.ex.dot(normal, a)
                sign = 0
                one_sided = True
                for p in unique_points:
                    value = pc.ex.dot(normal, p) - height
                    if value:
                        current = 1 if value > 0 else -1
                        if sign and current != sign:
                            one_sided = False
                            break
                        sign = current
                if not one_sided:
                    continue
                if sign > 0:
                    normal = tuple(-v for v in normal)
                    height = -height
                key = canon_plane(normal, height)
                coplanar = frozenset(
                    i for i, p in points.items() if pc.ex.dot(normal, p) == height
                )
                if key in found:
                    assert found[key] == coplanar
                else:
                    found[key] = coplanar
    assert found == stored, (
        len(found),
        len(stored),
        set(found) - set(stored),
        set(stored) - set(found),
    )
    return {
        "scale_digits": len(str(scale)),
        "unique_input_points": len(unique_points),
        "supporting_planes": len(found),
        "all_triples_exhausted": True,
        "every_coplanar_set_matches_reconstructed_cycle": True,
    }


def compare_cell(name, parameter, frozen, rows0):
    packet, rows, faces, _ = pc.exact_cell(name, parameter, rows0)
    ledger_path = HERE / frozen["ledger"]
    csv_path = HERE / frozen["csv"]
    assert pc.sha256(ledger_path) == frozen["ledger_sha256"]
    assert pc.sha256(csv_path) == frozen["csv_sha256"]
    assert json.loads(ledger_path.read_text()) == packet
    saved_rows = pc.read_rows(csv_path)
    assert saved_rows == rows
    assert packet["f_vector"] == frozen["f_vector"]
    assert packet["class"] == frozen["class"]
    return packet, rows, faces


def main():
    x = json.loads(DATA.read_text())
    assert x["verdict"] == "EXACT_POST_C17_LINKED_U254_H254255_DEATH_AND_FIRST_SUPPORT_FLIP_PASS"
    assert x["winner_status"] == "NONWINNER"
    assert pc.sha256(pc.SOURCE) == pc.SOURCE_SHA256
    source_copy = HERE / x["source"]["local_copy"]
    assert pc.sha256(source_copy) == pc.SOURCE_SHA256
    rows0 = pc.read_rows(source_copy)
    assert rows0 == pc.read_rows(pc.SOURCE)

    specs = [
        ("source", Q(0)),
        ("mechanics_pre", pc.MECH_LEFT),
        ("mechanics_far", pc.MECH_RIGHT),
        ("support_pre", pc.SUPPORT_PRE_SAMPLE),
        ("support_far", pc.SUPPORT_FAR_SAMPLE),
        ("endpoint", pc.END),
    ]
    rebuilt = {}
    for name, parameter in specs:
        rebuilt[name] = compare_cell(name, parameter, x["fresh_exact_cells"][name], rows0)

    assert rebuilt["source"][0]["class"] == [2, 5, 5]
    assert rebuilt["mechanics_pre"][0]["class"] == [2, 5, 5]
    assert rebuilt["mechanics_far"][0]["class"] == [2, 4, 4]
    assert rebuilt["support_pre"][0]["class"] == [2, 4, 4]
    assert rebuilt["support_far"][0]["class"] == [2, 4, 4]
    assert rebuilt["endpoint"][0]["class"] == [2, 4, 4]
    assert all(z[0]["all_37_forced_rails_present"] for z in rebuilt.values())

    t0 = time.time()
    exhaustive_source = exhaustive_supporting_planes(rebuilt["source"][1], rebuilt["source"][2])
    exhaustive_endpoint = exhaustive_supporting_planes(
        rebuilt["endpoint"][1], rebuilt["endpoint"][2]
    )
    exhaustive_seconds = time.time() - t0
    assert exhaustive_source["supporting_planes"] == 91
    assert exhaustive_endpoint["supporting_planes"] == 91

    linked = pc.linked_mechanics_event(rows0, rebuilt["source"][2])
    event0 = x["ordered_events"][0]
    assert event0["common_polynomial"] == linked["common_polynomial"]
    assert event0["isolating_bracket_exact"] == linked["isolating_bracket_exact"]
    assert event0["sturm_root_count"] == 1

    support = pc.support_root_atlas(rows0, rebuilt["source"][2])
    event1 = x["ordered_events"][1]
    assert event1["event_polynomial"] == support["event_polynomial"]
    assert event1["event_support_rows"] == support["event_support_rows"]
    assert event1["strict_in_face_consecutive_turn_polynomials"] == support[
        "strict_in_face_consecutive_turn_polynomials"
    ]
    pre_edges = {tuple(e) for e in rebuilt["support_pre"][0]["true_edges"]}
    far_edges = {tuple(e) for e in rebuilt["support_far"][0]["true_edges"]}
    assert pre_edges - far_edges == {(255, 257)}
    assert far_edges - pre_edges == {(256, 258)}

    old_guards = pc.mechanics_guard_audit(
        rows0,
        rebuilt["source"][2],
        Q(0),
        pc.SUPPORT_RIGHT,
        special_pair=True,
        reference_parameter=Q(0),
    )
    far_guards = pc.mechanics_guard_audit(
        rows0,
        rebuilt["support_far"][2],
        pc.SUPPORT_RIGHT,
        pc.END,
        special_pair=False,
        reference_parameter=pc.SUPPORT_FAR_SAMPLE,
    )
    far_wall_side = pc.one_sided_support_bracket_mechanics_audit(
        rows0,
        rebuilt["support_far"][2],
        pc.SUPPORT_LEFT,
        pc.SUPPORT_RIGHT,
        pc.SUPPORT_RIGHT,
    )
    assert old_guards == x["complete_mechanics_cone_audits"]["old_support_formula"]
    assert far_guards == x["complete_mechanics_cone_audits"]["far_support_formula"]
    assert far_wall_side == x["complete_mechanics_cone_audits"][
        "far_formula_open_algebraic_right_side"
    ]
    assert x["complete_mechanics_cone_audits"][
        "support_bracket_closed_without_hidden_mechanics_zero"
    ]

    far_segment = pc.cont.affine_support_segment_audit(
        rebuilt["support_far"][1], rebuilt["endpoint"][1], rebuilt["support_far"][2]
    )
    assert far_segment == x["far_support_segment_certificate"]

    start_values = pc.exact_named_values(rebuilt["source"][1], rebuilt["source"][2])
    end_values = pc.exact_named_values(rebuilt["endpoint"][1], rebuilt["endpoint"][2])
    for name, record in x["inherited_eight_endpoint_ratios"].items():
        ratio = end_values[name] / start_values[name]
        assert Q(record["endpoint_over_start_exact"]) == ratio < 1
    assert start_values["U254_via_255"] > 0 > end_values["U254_via_255"]
    assert start_values["H254_255_via_t"] > 0 > end_values["H254_255_via_t"]

    # Frozen artifacts are checked only after the mathematics has passed.
    for relative, expected in x["artifact_hashes"].items():
        assert pc.sha256(HERE / relative) == expected
    manifest = {}
    for line in MANIFEST.read_text().splitlines():
        digest, relative = line.split("  ", 1)
        assert relative not in manifest
        manifest[relative] = digest
    required = {
        "post_c17_exact.py",
        "build_certificate.py",
        "verify_certificate.py",
        "certificate.json",
        "REPORT.md",
        "source_endpoint.csv",
    }
    assert required <= set(manifest)
    for relative, expected in manifest.items():
        assert pc.sha256(HERE / relative) == expected

    print("INDEPENDENT_EXACT_POST_C17_LINKED_DEATH_AND_SUPPORT_FLIP_PASS")
    print("winner_status", x["winner_status"])
    print("source_exhaustive", exhaustive_source)
    print("endpoint_exhaustive", exhaustive_endpoint)
    print("exhaustive_seconds", exhaustive_seconds)
    print("mechanics_bracket", event0["isolating_bracket_exact"])
    print("support_bracket", event1["event_bracket_exact"])
    print("endpoint", rebuilt["endpoint"][0]["f_vector"], rebuilt["endpoint"][0]["class"])
    print("certificate_sha256", pc.sha256(DATA))
    print("manifest_entries", len(manifest))


if __name__ == "__main__":
    main()
