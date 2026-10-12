#!/usr/bin/env python3
"""Independent exact audit of a frozen round-eight far-cell endpoint.

Every CSV decimal is interpreted as a literal rational.  The verifier
reconstructs all supporting planes from the stored maximal-face cycles,
rebuilds the exact uniform-volume centroid, enumerates the true edge graph,
and evaluates every face, vertex and four-component edge equilibrium test.
It is intentionally independent of the floating-point SLP evaluator.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
BASE = frozenset([0, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5,
                  4, 3, 2, 1, 54])
ALT_ROUTE = (228, 198, 263, 9, 8)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def mul(a, t):
    return tuple(x * t for x in a)


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), Q(0))


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def det(a, b, c):
    return dot(a, cross(b, c))


def norm2(a):
    return dot(a, a)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def qfloat(x: Q) -> float:
    return x.numerator / x.denominator


def read_rows(path: Path):
    rows = {}
    with path.open(newline="") as handle:
        for row in csv.DictReader(handle):
            rows[int(row["source_id"])] = tuple(
                Q(row[k]) for k in ("x", "y", "z")
            )
    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--coordinates", type=Path,
        default=HERE / "row54_round8_far_guard_buffer2_best.csv")
    ap.add_argument(
        "--faces", type=Path,
        default=HERE / "row54_round8_far_guard_buffer2_best_faces.json")
    ap.add_argument(
        "--output", type=Path,
        default=HERE / "row54_round8_far_buffered_exact_audit.json")
    ap.add_argument(
        "--projected-output", type=Path,
        default=HERE / "row54_round8_far_buffered_exact_projected.json")
    args = ap.parse_args()

    rows = read_rows(args.coordinates)
    cycles = json.loads(args.faces.read_text())
    assert len(rows) == 61 and len(cycles) == 103
    base_cycle = next(c for c in cycles if frozenset(c) == BASE)

    # The identity-chart construction preserves the enlarged base plane
    # algebraically, but writing binary64 coordinates as decimals introduces
    # roundoff of order 1e-15.  Materialise the nearby exact rational body by
    # defining the plane through the first three base vertices and projecting
    # every remaining base vertex onto it along the best-conditioned axis.
    a, b, c = (rows[i] for i in base_cycle[:3])
    base_normal = cross(sub(b, a), sub(c, a))
    assert base_normal != (0, 0, 0)
    base_height = dot(base_normal, a)
    projection_axis = max(range(3), key=lambda k: abs(base_normal[k]))
    corrections = {}
    for i in base_cycle:
        p = list(rows[i])
        old = p[projection_axis]
        other = sum(
            (base_normal[k] * p[k] for k in range(3)
             if k != projection_axis), Q(0))
        p[projection_axis] = (base_height - other) / base_normal[projection_axis]
        rows[i] = tuple(p)
        corrections[i] = p[projection_axis] - old
    args.projected_output.write_text(json.dumps({
        "version": 1,
        "source_coordinates": str(args.coordinates),
        "source_sha256": sha256(args.coordinates),
        "base_cycle": base_cycle,
        "projection_axis": projection_axis,
        "base_plane_normal_exact": [str(v) for v in base_normal],
        "base_plane_height_exact": str(base_height),
        "maximum_absolute_correction_decimal": max(
            abs(qfloat(v)) for v in corrections.values()),
        "coordinates_exact": {
            str(i): [str(v) for v in rows[i]] for i in sorted(rows)
        },
    }, indent=2) + "\n")
    ids = sorted(rows)
    interior = tuple(
        sum((rows[i][k] for i in ids), Q(0)) / len(ids)
        for k in range(3)
    )

    # Rebuild and outward-orient every stored maximal supporting plane.
    planes = []
    coplanar_sets = []
    minimum_nonface_slack = None
    minimum_nonface_record = None
    for fi, cycle in enumerate(cycles):
        assert len(cycle) >= 3 and len(set(cycle)) == len(cycle)
        a, b, c = (rows[i] for i in cycle[:3])
        n = cross(sub(b, a), sub(c, a))
        assert n != (0, 0, 0)
        h = dot(n, a)
        values = {i: dot(n, p) - h for i, p in rows.items()}
        pos = any(v > 0 for v in values.values())
        neg = any(v < 0 for v in values.values())
        assert not (pos and neg), (fi, min(values.values()), max(values.values()))
        if pos:
            n = tuple(-x for x in n)
            h = -h
            values = {i: -v for i, v in values.items()}
        assert all(v <= 0 for v in values.values())
        coplanar = {i for i, v in values.items() if v == 0}
        assert coplanar == set(cycle), (fi, sorted(coplanar), cycle)
        for i, value in values.items():
            if i not in coplanar:
                slack = -value
                if minimum_nonface_slack is None or slack < minimum_nonface_slack:
                    minimum_nonface_slack = slack
                    minimum_nonface_record = {
                        "face_index": fi,
                        "face_cycle": cycle,
                        "opposite_vertex": i,
                        "slack_exact": str(slack),
                    }
        planes.append((n, h))
        coplanar_sets.append(coplanar)

    # True edges and neighbor/incident-face maps.
    edge_faces = defaultdict(list)
    neighbors = defaultdict(set)
    for fi, cycle in enumerate(cycles):
        for a, b in zip(cycle, cycle[1:] + cycle[:1]):
            edge = tuple(sorted((a, b)))
            edge_faces[edge].append(fi)
            neighbors[a].add(b)
            neighbors[b].add(a)
    assert len(edge_faces) == 162
    assert all(len(inc) == 2 for inc in edge_faces.values())
    assert len(rows) - len(edge_faces) + len(cycles) == 2

    # Exact signed-tetrahedron volume and centroid, orienting each fan
    # triangle outward using the strict interior point.
    volume = Q(0)
    moment = (Q(0), Q(0), Q(0))
    for cycle in cycles:
        a = rows[cycle[0]]
        for j in range(1, len(cycle) - 1):
            b, c = rows[cycle[j]], rows[cycle[j + 1]]
            normal = cross(sub(b, a), sub(c, a))
            if dot(normal, sub(a, interior)) < 0:
                b, c = c, b
            signed = det(a, b, c)
            assert signed > 0
            volume += signed / 6
            moment = add(moment, mul(add(add(a, b), c), signed / 24))
    assert volume > 0
    centroid = mul(moment, 1 / volume)
    x = {i: sub(rows[i], centroid) for i in ids}

    # Exhaustive exact face, vertex and four-component edge mechanics.
    stable = []
    stable_margins = {}
    for fi, cycle in enumerate(cycles):
        n = planes[fi][0]
        h = dot(n, x[cycle[0]])
        assert h > 0
        foot = mul(n, h / norm2(n))
        reference = tuple(
            sum((x[i][k] for i in cycle), Q(0)) / len(cycle)
            for k in range(3)
        )
        values = []
        for a, b in zip(cycle, cycle[1:] + cycle[:1]):
            value = dot(cross(sub(x[b], x[a]), sub(foot, x[a])), n)
            ref_value = dot(
                cross(sub(x[b], x[a]), sub(reference, x[a])), n)
            if ref_value < 0:
                value = -value
            assert value != 0
            values.append(value)
        stable_margins[fi] = min(values)
        if min(values) > 0:
            stable.append(fi)

    unstable = []
    unstable_margins = {}
    for i in ids:
        values = [-dot(x[i], sub(x[j], x[i])) for j in sorted(neighbors[i])]
        assert values and all(v != 0 for v in values)
        unstable_margins[i] = min(values)
        if min(values) > 0:
            unstable.append(i)

    saddles = []
    edge_margins = {}
    for edge, incident in sorted(edge_faces.items()):
        i, j = edge
        direction = sub(x[j], x[i])
        t = -dot(x[i], direction) / norm2(direction)
        point = add(x[i], mul(direction, t))
        n1 = planes[incident[0]][0]
        n2 = planes[incident[1]][0]
        aa, bb, cc = norm2(n1), dot(n1, n2), norm2(n2)
        r1, r2 = dot(point, n1), dot(point, n2)
        denominator = aa * cc - bb * bb
        assert denominator > 0
        beta1 = (r1 * cc - r2 * bb) / denominator
        beta2 = (r2 * aa - r1 * bb) / denominator
        values = (t, 1 - t, beta1, beta2)
        assert all(v != 0 for v in values)
        edge_margins[edge] = min(values)
        if min(values) > 0:
            saddles.append(edge)

    stable_sets = {frozenset(cycles[i]) for i in stable}
    assert stable_sets == {BASE, frozenset((7, 8, 245))}
    assert unstable == [8, 54]
    assert saddles == [(6, 7), (198, 263)]

    # Exact positive-dot route and connected component.
    graph = {i: set() for i in ids}
    positive_edges = 0
    route_dots = []
    for a, b in edge_faces:
        value = dot(x[a], x[b])
        if value > 0:
            positive_edges += 1
            graph[a].add(b)
            graph[b].add(a)
    seen = {ids[0]}
    stack = [ids[0]]
    while stack:
        a = stack.pop()
        for b in graph[a]:
            if b not in seen:
                seen.add(b)
                stack.append(b)
    assert seen == set(ids)
    for a, b in zip(ALT_ROUTE, ALT_ROUTE[1:]):
        assert tuple(sorted((a, b))) in edge_faces
        value = dot(x[a], x[b])
        assert value > 0
        route_dots.append(value)

    report = {
        "version": 1,
        "verdict": "EXACT_FROZEN_ROUND8_FAR_BUFFERED_ENDPOINT_PASS",
        "inputs": {
            "coordinates": str(args.coordinates),
            "coordinates_sha256": sha256(args.coordinates),
            "faces": str(args.faces),
            "faces_sha256": sha256(args.faces),
            "projected_coordinates": str(args.projected_output),
            "projected_coordinates_sha256": sha256(args.projected_output),
            "base_projection_axis": projection_axis,
            "maximum_base_projection_correction_decimal": max(
                abs(qfloat(v)) for v in corrections.values()),
        },
        "f_vector": [len(rows), len(edge_faces), len(cycles)],
        "class": [len(stable), len(unstable), len(saddles)],
        "stable_faces": [cycles[i] for i in stable],
        "unstable_vertices": unstable,
        "saddle_edges": [list(edge) for edge in saddles],
        "volume_exact": str(volume),
        "centroid_exact": [str(v) for v in centroid],
        "minimum_nonface_slack_exact": str(minimum_nonface_slack),
        "minimum_nonface_slack_decimal": qfloat(minimum_nonface_slack),
        "minimum_nonface_record": minimum_nonface_record,
        "positive_dot_edges": positive_edges,
        "positive_dot_component_size": len(seen),
        "alternate_route": list(ALT_ROUTE),
        "route_positive_dots_exact": [str(v) for v in route_dots],
        "route_minimum_positive_dot_decimal": min(map(qfloat, route_dots)),
        "minimum_positive_stable_primitive_decimal": min(
            qfloat(stable_margins[i]) for i in stable),
        "minimum_positive_unstable_primitive_decimal": min(
            qfloat(unstable_margins[i]) for i in unstable),
        "minimum_positive_saddle_primitive_decimal": min(
            qfloat(edge_margins[e]) for e in saddles),
        "scope": (
            "Exact for the frozen terminating-decimal endpoint and stored "
            "maximal-face cycles; not an exact certificate for the floating "
            "guard-buffer path or the preceding SLP continuation."
        ),
    }
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(report["verdict"])
    print("f/class", report["f_vector"], report["class"])
    print("route min", report["route_minimum_positive_dot_decimal"])
    print("output", args.output)


if __name__ == "__main__":
    main()
