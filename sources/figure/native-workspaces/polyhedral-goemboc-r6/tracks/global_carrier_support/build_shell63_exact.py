#!/usr/bin/env python3
"""Build and exactly certify the recovered 63-vertex carrier shell.

Only row 228 is changed.  Its orthogonal projection into the supporting plane
of face (224,229,247) is first projected tangentially onto edge (229,247).
The new row is placed a rational distance beyond that edge and a rational
distance on the opposite side of the face plane.  Dormant predecessor rows
226 and 227 then become exposed and prevent the U/H anti-birth seen in the
61-vertex shortcut.
"""

from __future__ import annotations

import csv
import itertools
import json
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
from scipy.spatial import ConvexHull


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / "M42_acute_bridge_fifth_cell_work" / "fifth_cell_endpoint"
SOURCE_ROWS = SOURCE / "input_rows_common_lattice.csv"
SOURCE_FACES = SOURCE / "face_cycles.json"
ROWS_OUT = HERE / "shell63_exact.csv"
FACES_OUT = HERE / "shell63_faces.json"
CERT_OUT = HERE / "shell63_certificate.json"

DELTA = Q(1, 100)
ETA = Q(-1, 100)

Point = tuple[Q, Q, Q]


def add(a: Point, b: Point) -> Point:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def sub(a: Point, b: Point) -> Point:
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def mul(s: Q, a: Point) -> Point:
    return (s * a[0], s * a[1], s * a[2])


def dot(a: Point, b: Point) -> Q:
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def cross(a: Point, b: Point) -> Point:
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def det(a: Point, b: Point, c: Point) -> Q:
    return dot(a, cross(b, c))


def orient(a: Point, b: Point, c: Point, d: Point) -> Q:
    return det(sub(b, a), sub(c, a), sub(d, a))


def norm2(a: Point) -> Q:
    return dot(a, a)


def q(value: Q) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def load_rows() -> dict[int, Point]:
    rows: dict[int, Point] = {}
    with SOURCE_ROWS.open(newline="") as handle:
        for row in csv.DictReader(handle):
            denominator = Q(row["denominator"])
            rows[int(row["source_id"])] = tuple(
                Q(row[column]) / denominator
                for column in ("x_int", "y_int", "z_int")
            )  # type: ignore[assignment]
    return rows


def project_to_plane(x: Point, a: Point, b: Point, c: Point) -> Point:
    normal = cross(sub(b, a), sub(c, a))
    coefficient = dot(normal, sub(x, a)) / norm2(normal)
    return sub(x, mul(coefficient, normal))


def barycentric_in_triangle(x: Point, a: Point, b: Point, c: Point) -> tuple[Q, Q, Q]:
    edge1, edge2, rhs = sub(b, a), sub(c, a), sub(x, a)
    aa, ab, bb = norm2(edge1), dot(edge1, edge2), norm2(edge2)
    ar, br = dot(edge1, rhs), dot(edge2, rhs)
    denominator = aa * bb - ab * ab
    weight_b = (ar * bb - br * ab) / denominator
    weight_c = (br * aa - ar * ab) / denominator
    return Q(1) - weight_b - weight_c, weight_b, weight_c


def construct(rows: dict[int, Point]) -> dict[str, object]:
    a, b, c, old = (rows[label] for label in (224, 229, 247, 228))
    projected = project_to_plane(old, a, b, c)
    bary = barycentric_in_triangle(projected, a, b, c)
    assert min(bary) > 0
    edge_weight_b = bary[1] / (bary[1] + bary[2])
    edge_weight_c = Q(1) - edge_weight_b
    edge_point = add(mul(edge_weight_b, b), mul(edge_weight_c, c))
    wall_point = add(mul(-DELTA, a), mul(Q(1) + DELTA, edge_point))
    new_point = add(wall_point, mul(ETA, sub(old, projected)))
    rows[228] = new_point
    return {
        "delta": q(DELTA),
        "eta": q(ETA),
        "projected_barycentric_in_224_229_247": [q(value) for value in bary],
        "edge_229_weight": q(edge_weight_b),
        "edge_247_weight": q(edge_weight_c),
        "wall_point": [q(value) for value in wall_point],
        "new_row_228": [q(value) for value in new_point],
    }


def propose_faces(rows: dict[int, Point]) -> list[list[int]]:
    labels = sorted(rows)
    points = np.asarray([[float(value) for value in rows[label]] for label in labels])
    hull = ConvexHull(points, qhull_options="Qt Qx")
    face_sets: set[frozenset[int]] = set()
    for simplex in hull.simplices:
        triple = [labels[index] for index in simplex]
        a, b, c = (rows[label] for label in triple)
        coplanar = frozenset(
            label for label in labels if orient(a, b, c, rows[label]) == 0
        )
        values = [orient(a, b, c, rows[label]) for label in labels if label not in coplanar]
        assert all(value > 0 for value in values) or all(value < 0 for value in values)
        face_sets.add(coplanar)

    cycles: list[list[int]] = []
    for face in face_sets:
        if face == frozenset(range(17)):
            cycle = list(range(17))
        else:
            assert len(face) == 3, sorted(face)
            cycle = sorted(face)
        a, b, c = (rows[label] for label in cycle[:3])
        normal = cross(sub(b, a), sub(c, a))
        height = dot(normal, a)
        values = [dot(normal, point) - height for point in rows.values()]
        if any(value > 0 for value in values):
            assert not any(value < 0 for value in values)
            cycle = [cycle[0]] + list(reversed(cycle[1:]))
        cycles.append(cycle)
    cycles.sort(key=lambda cycle: (0 if set(cycle) == set(range(17)) else 1, tuple(sorted(cycle))))
    return cycles


def exact_audit(rows: dict[int, Point], cycles: list[list[int]]) -> dict[str, object]:
    labels = sorted(rows)
    normals: list[Point] = []
    for cycle in cycles:
        a, b, c = (rows[label] for label in cycle[:3])
        normal = cross(sub(b, a), sub(c, a))
        height = dot(normal, a)
        values = {label: dot(normal, point) - height for label, point in rows.items()}
        assert all(value <= 0 for value in values.values())
        assert {label for label, value in values.items() if value == 0} == set(cycle)
        area = (Q(0), Q(0), Q(0))
        for first, second in zip(cycle, cycle[1:] + cycle[:1]):
            area = add(area, cross(rows[first], rows[second]))
        assert dot(area, normal) > 0
        normals.append(normal)

    edge_faces: dict[tuple[int, int], list[int]] = defaultdict(list)
    neighbours: dict[int, set[int]] = defaultdict(set)
    for face_index, cycle in enumerate(cycles):
        for first, second in zip(cycle, cycle[1:] + cycle[:1]):
            edge = tuple(sorted((first, second)))
            edge_faces[edge].append(face_index)
            neighbours[first].add(second)
            neighbours[second].add(first)
    assert all(len(incident) == 2 for incident in edge_faces.values())
    active = sorted(set().union(*(set(cycle) for cycle in cycles)))
    assert len(active) - len(edge_faces) + len(cycles) == 2

    determinant_sum = Q(0)
    moment_sum = [Q(0), Q(0), Q(0)]
    for cycle in cycles:
        for offset in range(1, len(cycle) - 1):
            a, b, c = (rows[label] for label in (cycle[0], cycle[offset], cycle[offset + 1]))
            determinant = det(a, b, c)
            determinant_sum += determinant
            for coordinate in range(3):
                moment_sum[coordinate] += determinant * (
                    a[coordinate] + b[coordinate] + c[coordinate]
                )
    assert determinant_sum > 0
    volume = determinant_sum / 6
    centroid = tuple(value / (4 * determinant_sum) for value in moment_sum)
    centred = {label: sub(rows[label], centroid) for label in active}

    stable_faces: list[list[int]] = []
    unstable_vertices: list[int] = []
    saddle_edges: list[tuple[int, int]] = []
    all_components: list[Q] = []

    for cycle, normal in zip(cycles, normals):
        height = dot(normal, centred[cycle[0]])
        assert height > 0
        foot = mul(height / norm2(normal), normal)
        reference = tuple(
            sum((centred[label][coordinate] for label in cycle), Q(0)) / len(cycle)
            for coordinate in range(3)
        )
        values: list[Q] = []
        for first, second in zip(cycle, cycle[1:] + cycle[:1]):
            value = dot(
                cross(sub(centred[second], centred[first]), sub(foot, centred[first])),
                normal,
            )
            reference_sign = dot(
                cross(sub(centred[second], centred[first]), sub(reference, centred[first])),
                normal,
            )
            if reference_sign < 0:
                value = -value
            assert value != 0
            values.append(value)
        all_components.extend(values)
        if min(values) > 0:
            stable_faces.append(cycle)

    for label in active:
        values = [
            -dot(centred[label], sub(centred[other], centred[label]))
            for other in sorted(neighbours[label])
        ]
        assert values and all(value != 0 for value in values)
        all_components.extend(values)
        if min(values) > 0:
            unstable_vertices.append(label)

    for edge, incident in sorted(edge_faces.items()):
        first, second = edge
        direction = sub(centred[second], centred[first])
        t = -dot(centred[first], direction) / norm2(direction)
        closest = add(centred[first], mul(t, direction))
        normal1, normal2 = normals[incident[0]], normals[incident[1]]
        aa, ab, bb = norm2(normal1), dot(normal1, normal2), norm2(normal2)
        r1, r2 = dot(closest, normal1), dot(closest, normal2)
        denominator = aa * bb - ab * ab
        assert denominator > 0
        beta1 = (r1 * bb - r2 * ab) / denominator
        beta2 = (r2 * aa - r1 * ab) / denominator
        values = (t, Q(1) - t, beta1, beta2)
        assert all(value != 0 for value in values)
        all_components.extend(values)
        if min(values) > 0:
            saddle_edges.append(edge)

    expected_stable = {frozenset(range(17)), frozenset((198, 224, 258))}
    assert {frozenset(face) for face in stable_faces} == expected_stable
    assert unstable_vertices == [8]
    assert saddle_edges == [(228, 229)]
    assert (len(stable_faces), len(unstable_vertices), len(saddle_edges)) == (2, 1, 1)

    source_faces = {frozenset(face) for face in json.loads(SOURCE_FACES.read_text())}
    actual_faces = {frozenset(face) for face in cycles}
    return {
        "f_vector": [len(active), len(edge_faces), len(cycles)],
        "euler": len(active) - len(edge_faces) + len(cycles),
        "active_labels": active,
        "newly_active_source_labels": sorted(set(active) - set().union(*source_faces)),
        "class": [len(stable_faces), len(unstable_vertices), len(saddle_edges)],
        "stable_faces": [face for face in stable_faces],
        "unstable_vertices": unstable_vertices,
        "saddle_edges": [list(edge) for edge in saddle_edges],
        "volume_exact": q(volume),
        "centroid_exact": [q(value) for value in centroid],
        "centroid_decimal": [float(value) for value in centroid],
        "minimum_absolute_raw_mechanics_component": q(min(abs(value) for value in all_components)),
        "minimum_absolute_raw_mechanics_component_decimal": float(
            min(abs(value) for value in all_components)
        ),
        "removed_source_faces": [
            sorted(face) for face in sorted(source_faces - actual_faces, key=lambda face: tuple(sorted(face)))
        ],
        "added_faces": [
            sorted(face) for face in sorted(actual_faces - source_faces, key=lambda face: tuple(sorted(face)))
        ],
    }


def write_rows(rows: dict[int, Point]) -> None:
    with ROWS_OUT.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(("source_id", "x_exact", "y_exact", "z_exact"))
        for label in sorted(rows):
            writer.writerow((label, *(q(value) for value in rows[label])))


def main() -> None:
    rows = load_rows()
    construction = construct(rows)
    cycles = propose_faces(rows)
    audit = exact_audit(rows, cycles)
    write_rows(rows)
    FACES_OUT.write_text(json.dumps(cycles, indent=2) + "\n")
    certificate = {
        "version": 1,
        "construction": construction,
        **audit,
        "scope": (
            "Exact globally supporting carrier shell. It transfers the old saddle "
            "and prevents a compensating U/H birth, but retains the extra stable face."
        ),
    }
    CERT_OUT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print("PASS exact support, closed topology and own-centroid mechanics")
    print("f-vector", audit["f_vector"], "class", audit["class"])
    print("newly active", audit["newly_active_source_labels"])
    print("stable", audit["stable_faces"], "unstable", audit["unstable_vertices"], "saddles", audit["saddle_edges"])


if __name__ == "__main__":
    main()
