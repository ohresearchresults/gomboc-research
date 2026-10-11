#!/usr/bin/env python3
"""Exact frozen-cell check for an alternate acute route after round 8.

The round-eight circuit deletes the literal long-rail edge (263,264).  This
verifier asks the weaker, structurally relevant question whether the actual
positive-dot true-edge graph is nevertheless connected on each strict open
side.  All terminating decimals are interpreted as exact rationals.

Scope: the two stored strict pre/far cells and their stored maximal-face
cycles.  This does not certify a monotone directed rail, the algebraic wall
continuum, or every perturbation of either cell.
"""
from __future__ import annotations

import csv
import hashlib
import json
from collections import deque
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
EVENT = HERE / "row54_round8_topology_event.json"
OUTPUT = HERE / "row54_round8_alternate_acute_route.json"
PATH = (228, 198, 263, 9, 8)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def mul(s, a):
    return tuple(s * x for x in a)


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), Fraction(0))


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def det(a, b, c):
    return dot(a, cross(b, c))


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_rows(path):
    rows = {}
    with path.open(newline="") as handle:
        for row in csv.DictReader(handle):
            rows[int(row["source_id"])] = tuple(
                Fraction(row[key]) for key in ("x", "y", "z")
            )
    return rows


def exact_centroid(rows, faces):
    interior = tuple(
        sum((rows[i][k] for i in rows), Fraction(0)) / len(rows)
        for k in range(3)
    )
    volume = Fraction(0)
    moment = (Fraction(0), Fraction(0), Fraction(0))
    for cycle in faces:
        a = rows[cycle[0]]
        for j in range(1, len(cycle) - 1):
            b, c = rows[cycle[j]], rows[cycle[j + 1]]
            normal = cross(sub(b, a), sub(c, a))
            orientation = dot(normal, sub(a, interior))
            assert orientation != 0
            if orientation < 0:
                b, c = c, b
            signed = det(a, b, c)
            assert signed != 0
            volume += signed / 6
            moment = add(moment, mul(signed / 24, add(add(a, b), c)))
    assert volume > 0
    return volume, mul(1 / volume, moment)


def edge_set(faces):
    edges = set()
    for cycle in faces:
        for a, b in zip(cycle, cycle[1:] + cycle[:1]):
            edges.add(tuple(sorted((a, b))))
    return edges


def components(vertices, graph):
    unseen = set(vertices)
    out = []
    while unseen:
        start = min(unseen)
        todo = [start]
        unseen.remove(start)
        comp = []
        while todo:
            node = todo.pop()
            comp.append(node)
            for other in graph.get(node, ()):
                if other in unseen:
                    unseen.remove(other)
                    todo.append(other)
        out.append(sorted(comp))
    return sorted(out, key=lambda z: (-len(z), z))


def shortest_path(graph, start, target):
    todo = deque([start])
    parent = {start: None}
    while todo:
        node = todo.popleft()
        if node == target:
            break
        for other in sorted(graph.get(node, ())):
            if other not in parent:
                parent[other] = node
                todo.append(other)
    assert target in parent
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = parent[node]
    return tuple(reversed(path))


def audit(state):
    csv_path = HERE / f"row54_round8_topology_event_{state}.csv"
    faces_path = HERE / f"row54_round8_topology_event_{state}_faces.json"
    rows = read_rows(csv_path)
    faces = json.loads(faces_path.read_text())
    edges = edge_set(faces)
    volume, centroid = exact_centroid(rows, faces)

    assert len(rows) == 61
    assert [len(rows), len(edges), len(faces)] == [61, 162, 103]
    assert tuple(sorted((263, 264))) in edges if state == "pre" else tuple(sorted((263, 264))) not in edges

    graph = {}
    positive = []
    nonpositive = []
    for a, b in sorted(edges):
        value = dot(sub(rows[a], centroid), sub(rows[b], centroid))
        record = (a, b, value)
        if value > 0:
            positive.append(record)
            graph.setdefault(a, set()).add(b)
            graph.setdefault(b, set()).add(a)
        else:
            nonpositive.append(record)

    comps = components(rows, graph)
    assert len(comps) == 1 and len(comps[0]) == 61
    exact_shortest = shortest_path(graph, PATH[0], PATH[-1])
    assert exact_shortest == PATH

    route = []
    for a, b in zip(PATH, PATH[1:]):
        edge = tuple(sorted((a, b)))
        assert edge in edges
        value = dot(sub(rows[a], centroid), sub(rows[b], centroid))
        assert value > 0
        route.append(
            {
                "edge": [a, b],
                "positive_dot_exact": str(value),
                "positive_dot_decimal": float(value),
            }
        )

    return {
        "state": state,
        "input_sha256": {"csv": sha256(csv_path), "faces": sha256(faces_path)},
        "f_vector": [len(rows), len(edges), len(faces)],
        "volume_exact": str(volume),
        "centroid_exact": [str(x) for x in centroid],
        "positive_dot_true_edges": len(positive),
        "nonpositive_dot_true_edges": len(nonpositive),
        "positive_dot_component_sizes": [len(c) for c in comps],
        "literal_edge_263_264_present": tuple(sorted((263, 264))) in edges,
        "shortest_acute_route_228_to_8": list(exact_shortest),
        "alternate_route": route,
        "minimum_alternate_positive_dot_exact": str(min(z[2] for z in positive if (z[0], z[1]) in {tuple(sorted(e)) for e in zip(PATH, PATH[1:])})),
        "minimum_alternate_positive_dot_decimal": min(z["positive_dot_decimal"] for z in route),
    }


def main():
    event = json.loads(EVENT.read_text())
    assert event["new_quad"] == [9, 198, 263, 264]
    assert event["removed_faces"] == [[9, 263, 264], [198, 263, 264]]
    assert event["added_faces"] == [[9, 198, 263], [9, 198, 264]]

    records = [audit("pre"), audit("far")]
    out = {
        "version": 1,
        "verdict": "EXACT_FROZEN_PRE_FAR_ALTERNATE_ACUTE_ROUTE_PASS",
        "event_sha256": sha256(EVENT),
        "deleted_literal_long_rail_edge": [263, 264],
        "alternate_positive_dot_true_edge_route": list(PATH),
        "states": records,
        "interpretation": (
            "The round-eight flip breaks the stored literal 19-edge long rail, "
            "but it does not disconnect the positive-dot true-edge graph.  In "
            "both exact-decimal strict open cells, 228 and protected vertex 8 "
            "remain joined by the four-edge acute route 228-198-263-9-8."
        ),
        "scope": (
            "Exact for the two frozen terminating-decimal pre/far coordinate "
            "tables and their stored maximal-face cycles.  This is neither a "
            "monotone directed-rail certificate nor a continuum theorem at the "
            "algebraic wall, and it does not by itself improve the (2,2,2) class."
        ),
    }
    OUTPUT.write_text(json.dumps(out, indent=2) + "\n")
    print(out["verdict"])
    for rec in records:
        print(
            rec["state"],
            rec["f_vector"],
            rec["positive_dot_component_sizes"],
            rec["shortest_acute_route_228_to_8"],
            rec["minimum_alternate_positive_dot_decimal"],
        )
    print("output", OUTPUT)


if __name__ == "__main__":
    main()
