#!/usr/bin/env python3
"""Enumerate the exact support-event chain of the selected full-control line.

The numerical LP is used only to choose coefficients.  This script rebuilds
the exact rational source, rationalizes all 165 controls, isolates every next
support root in the *current* maximal-face cell, and reconstructs the adjacent
cell independently from a rational post-wall sample.  It stops fail-closed on
a non-simple wall, lost mandatory rail, changed equilibrium class, inactive
row, or hull mismatch.

This is still a topology/path-definition stage.  The separate exact builder
must audit every support and own-centroid mechanics polynomial on all open
cells and algebraic wall intervals.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import sys
from collections import Counter, defaultdict
from fractions import Fraction as Q
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(PARENT))

import attack_common as c  # noqa: E402
import scan_directed_path as scan  # noqa: E402


ex = c.frozen.ex
SOURCE = PARENT / "exact_event_source.csv"
SOURCE_FACES = PARENT / "exact_event_source_faces.json"
PROPOSAL = HERE / "full_control_search.json"
PATH_DEFINITION = HERE / "exact_full_control_path.json"
SCAN_OUTPUT = HERE / "exact_support_chain_scan.json"
ROOT_WIDTH = Q(1, 10**30)
MAXIMUM = Q(1)
EXPECTED_CLASS = [2, 2, 2]
EXPECTED_F = [61, 162, 103]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def read_exact_csv(path: Path):
    rows = {}
    with path.open(newline="") as stream:
        for row in csv.DictReader(stream):
            rows[int(row["source_id"])] = tuple(
                Q(row[key]) for key in ("x", "y", "z")
            )
    return rows


def write_exact_csv(path: Path, points) -> None:
    with path.open("w", newline="") as stream:
        out = csv.writer(stream)
        out.writerow(("source_id", "x", "y", "z"))
        for label in sorted(points):
            out.writerow((label, *(ex.qs(value) for value in points[label])))


def face_key_set(faces):
    return {frozenset(face) for face in faces}


def edge_set(faces):
    return set(ex.edge_data(faces)[0])


def oriented_wall_cycle(removed_faces):
    counts = Counter()
    directed = []
    for face in removed_faces:
        for left, right in zip(face, face[1:] + face[:1]):
            counts[tuple(sorted((left, right)))] += 1
            directed.append((left, right))
    boundary = [(left, right) for left, right in directed if counts[tuple(sorted((left, right)))] == 1]
    following = {}
    incoming = {}
    for left, right in boundary:
        if left in following or right in incoming:
            raise AssertionError(("non-cycle oriented boundary", boundary))
        following[left] = right
        incoming[right] = left
    if set(following) != set(incoming) or len(following) != 4:
        raise AssertionError(("wall boundary is not a quadrilateral", boundary))
    start = min(following)
    cycle = [start]
    while following[cycle[-1]] != start:
        cycle.append(following[cycle[-1]])
        if len(cycle) > len(following):
            raise AssertionError("wall cycle failed to close")
    if len(cycle) != 4:
        raise AssertionError(("wrong wall cycle", cycle))
    return cycle


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


def next_support_group(path, faces, after: Q):
    grouped = {}
    metadata = {}
    for face_index, witness, polynomial in ex.support_polynomials(path, faces):
        label = f"support:f{face_index}:w{witness}"
        key = scan.polynomial_key(polynomial)
        packet = grouped.setdefault(key, {"polynomial": polynomial, "labels": []})
        packet["labels"].append(label)
        metadata[label] = {
            "face_index": face_index,
            "face": faces[face_index],
            "witness": witness,
        }
    approximate = []
    lower = float(after) + 2e-10
    for packet in grouped.values():
        siblings = scan.positive_real_roots(packet["polynomial"], float(MAXIMUM))
        for value in siblings:
            if value > lower:
                approximate.append(
                    (value, packet["polynomial"], packet["labels"], siblings)
                )
    approximate.sort(key=lambda item: item[0])
    if not approximate:
        return None, len(grouped)

    isolated = []
    for value, polynomial, labels, siblings in approximate[:80]:
        rough = scan.isolate_near(polynomial, value, siblings, float(MAXIMUM))
        root = ex.isolate_monotone_root(
            polynomial, rough["lo"], rough["hi"], ROOT_WIDTH
        )
        if root["lo"] > after:
            isolated.append((root["lo"], polynomial, labels, root))
    if not isolated:
        raise AssertionError("numeric candidates did not yield a later exact root")
    isolated.sort(key=lambda item: item[0])
    first = isolated[0]
    # Any exactly coincident support rows for a four-point circuit are scalar
    # multiples and therefore share the normalized polynomial key/label group.
    return {
        "polynomial": first[1],
        "labels": first[2],
        "root": first[3],
        "support_rows": [metadata[label] for label in first[2]],
        "next_distinct_lower": (
            isolated[1][0] if len(isolated) > 1 else MAXIMUM
        ),
    }, len(grouped)


def checkpoint(points, faces):
    support = ex.supporting_cell(points, faces)
    _ledger, mechanics = ex.classify_point(points, faces)
    edges = set(map(tuple, support["edges"]))
    missing = sorted(c.rail_edges() - edges)
    if support["f_vector"] != EXPECTED_F:
        raise AssertionError(("checkpoint f-vector", support["f_vector"]))
    if support["active_labels"] != sorted(points):
        raise AssertionError("checkpoint has inactive rows")
    if mechanics["class"] != EXPECTED_CLASS:
        raise AssertionError(("checkpoint class", mechanics))
    if c.BASE not in {frozenset(face) for face in faces}:
        raise AssertionError("checkpoint lost enlarged base")
    if missing:
        raise AssertionError(("checkpoint lost rails", missing))
    d6, m24 = ex.exact_centroid_numerators(points, faces)
    if d6 <= 0:
        raise AssertionError("checkpoint has nonpositive volume")
    centroid = tuple(value / (4 * d6) for value in m24)
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
        "f_vector": support["f_vector"],
        "active_row_count": len(support["active_labels"]),
        "class": mechanics["class"],
        "stable_faces": mechanics["stable_faces"],
        "unstable_vertices": mechanics["unstable_vertices"],
        "saddle_edges": mechanics["saddle_edges"],
        "exact_centroid": [ex.qs(value) for value in centroid],
        "forced_rail_count": len(c.rail_edges()),
        "missing_forced_rails": [],
    }


def main() -> None:
    proposal = json.loads(PROPOSAL.read_text())
    if proposal["verdict"] != "FULL_CONTROL_RAIL_SEPARATING_PRIMAL_WITNESS_FOUND":
        raise AssertionError(proposal["verdict"])
    source = read_exact_csv(SOURCE)
    source_faces = json.loads(SOURCE_FACES.read_text())
    ids = sorted(source)
    direction = proposal["selected"]["direction"]
    velocity, chart_scale = c.exact_velocity_from_coefficients(
        source, ids, direction
    )
    path = c.frozen.line_points(source, velocity)
    velocity_packet = {
        str(label): [ex.qs(value) for value in velocity[label]] for label in ids
    }
    path_definition = {
        "version": 1,
        "type": "exact rational-affine full-control line",
        "source_sha256": sha256(SOURCE),
        "source_faces_sha256": sha256(SOURCE_FACES),
        "proposal_sha256": sha256(PROPOSAL),
        "chart_scale_diagnostic": chart_scale,
        "control_count": len(direction),
        "velocity": velocity_packet,
        "velocity_digest": canonical_hash(velocity_packet),
        "parameter_interval": ["0", "1"],
    }
    PATH_DEFINITION.write_text(json.dumps(path_definition, indent=2) + "\n")

    current_faces = source_faces
    current_after = Q(0)
    cells = []
    events = []
    generated = [PATH_DEFINITION]
    cell_index = 0
    while current_after < MAXIMUM:
        faces_path = HERE / f"exact_support_cell_{cell_index}_faces.json"
        faces_path.write_text(json.dumps(current_faces, indent=2) + "\n")
        generated.append(faces_path)
        event, group_count = next_support_group(path, current_faces, current_after)
        if event is None or event["root"]["lo"] >= MAXIMUM:
            endpoint = c.frozen.at(path, MAXIMUM)
            fresh_faces, _support, _tol = scan.exact_hull(endpoint)
            if face_key_set(fresh_faces) != face_key_set(current_faces):
                raise AssertionError("unrecorded support event before endpoint")
            endpoint_file = HERE / "exact_support_chain_endpoint.csv"
            write_exact_csv(endpoint_file, endpoint)
            generated.append(endpoint_file)
            cells.append(
                {
                    "index": cell_index,
                    "lo": ex.qs(current_after),
                    "hi": ex.qs(MAXIMUM),
                    "face_file": faces_path.name,
                    "face_sha256": sha256(faces_path),
                    "unique_support_polynomial_count": group_count,
                    "terminal_checkpoint": checkpoint(endpoint, current_faces),
                }
            )
            break

        root = event["root"]
        if not current_after < root["lo"] < root["hi"] < MAXIMUM:
            raise AssertionError(("bad ordered root", current_after, root))
        available = min(
            event["next_distinct_lower"] - root["hi"],
            MAXIMUM - root["hi"],
        )
        if available <= 0:
            raise AssertionError("no strict post-event sample interval")

        pre_t = root["lo"] - (root["lo"] - current_after) / 5
        post_t = root["hi"] + available / 20
        pre_points = c.frozen.at(path, pre_t)
        if face_key_set(scan.exact_hull(pre_points)[0]) != face_key_set(current_faces):
            raise AssertionError("pre sample left current cell")

        # Shrink deterministically until a single 2--2 simplicial flip is
        # reconstructed.  Every attempted parameter is explicit in the result.
        attempts = []
        post_faces = None
        post_points = None
        removed_keys = added_keys = None
        for shrink in range(8):
            candidate_t = root["hi"] + (post_t - root["hi"]) / (10**shrink)
            candidate_points = c.frozen.at(path, candidate_t)
            candidate_faces, _support, _tol = scan.exact_hull(candidate_points)
            removed = face_key_set(current_faces) - face_key_set(candidate_faces)
            added = face_key_set(candidate_faces) - face_key_set(current_faces)
            attempts.append(
                {
                    "parameter": ex.qs(candidate_t),
                    "removed_face_count": len(removed),
                    "added_face_count": len(added),
                }
            )
            if len(removed) == 2 and len(added) == 2:
                post_t = candidate_t
                post_points = candidate_points
                post_faces = candidate_faces
                removed_keys, added_keys = removed, added
                break
        if post_faces is None:
            raise AssertionError(("event is not an isolated 2--2 flip", attempts))

        removed_faces = [
            face for face in current_faces if frozenset(face) in removed_keys
        ]
        added_faces = [face for face in post_faces if frozenset(face) in added_keys]
        wall_cycle = oriented_wall_cycle(removed_faces)
        kept = [face for face in current_faces if frozenset(face) not in removed_keys]
        wall_faces = kept + [wall_cycle]
        pre_edges = edge_set(current_faces)
        wall_edges = edge_set(wall_faces)
        post_edges = edge_set(post_faces)
        removed_edges = sorted(pre_edges - post_edges)
        added_edges = sorted(post_edges - pre_edges)
        if len(removed_edges) != 1 or len(added_edges) != 1:
            raise AssertionError(("event is not a one-edge flip", removed_edges, added_edges))
        if wall_edges != pre_edges - set(removed_edges):
            raise AssertionError("wall edge ledger mismatch on pre side")
        if wall_edges != post_edges - set(added_edges):
            raise AssertionError("wall edge ledger mismatch on post side")
        missing_pre = sorted(c.rail_edges() - pre_edges)
        missing_wall = sorted(c.rail_edges() - wall_edges)
        missing_post = sorted(c.rail_edges() - post_edges)
        if missing_pre or missing_wall or missing_post:
            raise AssertionError(
                ("mandatory rail obstruction", missing_pre, missing_wall, missing_post)
            )
        post_checkpoint = checkpoint(post_points, post_faces)

        pre_file = HERE / f"exact_support_event_{cell_index}_pre.csv"
        post_file = HERE / f"exact_support_event_{cell_index}_post.csv"
        wall_file = HERE / f"exact_support_event_{cell_index}_wall_faces.json"
        post_faces_file = HERE / f"exact_support_cell_{cell_index + 1}_faces.json"
        write_exact_csv(pre_file, pre_points)
        write_exact_csv(post_file, post_points)
        wall_file.write_text(json.dumps(wall_faces, indent=2) + "\n")
        post_faces_file.write_text(json.dumps(post_faces, indent=2) + "\n")
        generated.extend((pre_file, post_file, wall_file, post_faces_file))

        cells.append(
            {
                "index": cell_index,
                "lo": ex.qs(current_after),
                "hi": ex.qs(root["lo"]),
                "face_file": faces_path.name,
                "face_sha256": sha256(faces_path),
                "unique_support_polynomial_count": group_count,
            }
        )
        events.append(
            {
                "index": cell_index,
                "root": root_record(event["polynomial"], root),
                "support_rows": event["support_rows"],
                "pre_parameter": ex.qs(pre_t),
                "post_parameter": ex.qs(post_t),
                "post_sampling_attempts": attempts,
                "circuit": sorted(set().union(*removed_keys)),
                "removed_maximal_faces": [list(face) for face in removed_faces],
                "wall_maximal_face": wall_cycle,
                "added_maximal_faces": [list(face) for face in added_faces],
                "removed_true_edge": list(removed_edges[0]),
                "added_true_edge": list(added_edges[0]),
                "pre_f_vector": EXPECTED_F,
                "wall_f_vector": [61, 161, 102],
                "post_f_vector": EXPECTED_F,
                "pre_missing_rails": [],
                "wall_missing_rails": [],
                "post_missing_rails": [],
                "post_checkpoint": post_checkpoint,
                "pre_file": pre_file.name,
                "pre_sha256": sha256(pre_file),
                "post_file": post_file.name,
                "post_sha256": sha256(post_file),
                "wall_faces_file": wall_file.name,
                "wall_faces_sha256": sha256(wall_file),
                "post_faces_file": post_faces_file.name,
                "post_faces_sha256": sha256(post_faces_file),
            }
        )
        print(
            "event",
            cell_index,
            events[-1]["root"]["decimal_interval"],
            events[-1]["circuit"],
            removed_edges[0],
            "->",
            added_edges[0],
            flush=True,
        )
        current_faces = post_faces
        current_after = root["hi"]
        cell_index += 1
        if cell_index > 20:
            raise AssertionError("unexpectedly long support chain")

    output = {
        "version": 1,
        "type": "exact full-control dynamic support-event enumeration",
        "verdict": "EXACT_FULL_CONTROL_SAFE_SUPPORT_CHAIN_ENUMERATED",
        "scope": (
            "Exact rational line and algebraically isolated dynamic support "
            "walls. Complete mechanics/centroid interval certification is a "
            "separate mandatory stage."
        ),
        "source_sha256": sha256(SOURCE),
        "source_faces_sha256": sha256(SOURCE_FACES),
        "proposal_sha256": sha256(PROPOSAL),
        "path_definition_sha256": sha256(PATH_DEFINITION),
        "event_count": len(events),
        "cell_count": len(cells),
        "cells": cells,
        "events": events,
        "generated_file_sha256": {
            path.name: sha256(path) for path in dict.fromkeys(generated)
        },
    }
    SCAN_OUTPUT.write_text(json.dumps(output, indent=2) + "\n")
    print(output["verdict"])
    print("event_count", len(events))
    print("scan_sha256", sha256(SCAN_OUTPUT))


if __name__ == "__main__":
    main()
