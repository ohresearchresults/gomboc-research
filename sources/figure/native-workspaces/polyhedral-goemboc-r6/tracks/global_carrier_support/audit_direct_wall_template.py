#!/usr/bin/env python3
"""Exact first-wall audit for the two natural carrier flattenings.

The fifth M42 sphere has two immediate candidate 2<->2 walls:

* flatten the two faces at the stable limiting edge (198,224), whose four
  labels are {198,224,258,241};
* flatten the two faces at the saddle edge (229,247), whose four labels are
  {224,229,247,228}.

The most economical synthesis template moves one label of a circuit along the
straight orthogonal projection to the plane of the other three, keeping every
other row fixed.  This script checks all eight possible choices of moving
label.  Exact supporting determinants of every old maximal face against every
active vertex give the first hull wall on each segment.
"""

from __future__ import annotations

import csv
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ENDPOINT = ROOT / "M42_acute_bridge_fifth_cell_work" / "fifth_cell_endpoint"
POINTS_CSV = ENDPOINT / "input_rows_common_lattice.csv"
FACES_JSON = ENDPOINT / "face_cycles.json"
OUTPUT = Path(__file__).with_name("direct_wall_template_obstruction.json")

Point = tuple[Fraction, Fraction, Fraction]


def sub(a: Point, b: Point) -> Point:
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def add(a: Point, b: Point) -> Point:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def mul(s: Fraction, a: Point) -> Point:
    return (s * a[0], s * a[1], s * a[2])


def dot(a: Point, b: Point) -> Fraction:
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def cross(a: Point, b: Point) -> Point:
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def orient(a: Point, b: Point, c: Point, d: Point) -> Fraction:
    return dot(cross(sub(b, a), sub(c, a)), sub(d, a))


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def load() -> tuple[dict[int, Point], list[list[int]], list[int]]:
    points: dict[int, Point] = {}
    with POINTS_CSV.open(newline="") as handle:
        for row in csv.DictReader(handle):
            denominator = Fraction(row["denominator"])
            points[int(row["source_id"])] = tuple(
                Fraction(row[column]) / denominator
                for column in ("x_int", "y_int", "z_int")
            )  # type: ignore[assignment]
    faces = json.loads(FACES_JSON.read_text())
    active = sorted(set().union(*(set(face) for face in faces)))
    return points, faces, active


def face_triple(
    face: list[int], points: dict[int, Point], active: list[int]
) -> tuple[int, int, int]:
    for triple in combinations(face, 3):
        if any(
            orient(
                points[triple[0]],
                points[triple[1]],
                points[triple[2]],
                points[label],
            )
            for label in active
            if label not in triple
        ):
            return triple
    raise AssertionError(f"degenerate maximal face {face}")


def project_to_plane(x: Point, a: Point, b: Point, c: Point) -> Point:
    normal = cross(sub(b, a), sub(c, a))
    normal_squared = dot(normal, normal)
    assert normal_squared > 0
    coefficient = dot(normal, sub(x, a)) / normal_squared
    return sub(x, mul(coefficient, normal))


def segment_point(a: Point, b: Point, t: Fraction) -> Point:
    return add(a, mul(t, sub(b, a)))


def main() -> None:
    points, faces, active = load()
    triples = [face_triple(face, points, active) for face in faces]
    orientations: list[int] = []
    for face, triple in zip(faces, triples):
        values = [
            orient(
                points[triple[0]],
                points[triple[1]],
                points[triple[2]],
                points[label],
            )
            for label in active
            if label not in face
        ]
        assert all(value >= 0 for value in values) or all(value <= 0 for value in values)
        orientations.append(1 if any(value > 0 for value in values) else -1)
        if any(value < 0 for value in values):
            orientations[-1] = -1

    target_circuits = {
        "stable_limiting_edge": (198, 224, 258, 241),
        "saddle_edge": (224, 229, 247, 228),
    }
    records: list[dict[str, object]] = []
    for target_name, circuit in target_circuits.items():
        for moving in circuit:
            fixed = tuple(label for label in circuit if label != moving)
            start = points[moving]
            endpoint = project_to_plane(start, *(points[label] for label in fixed))

            roots: list[tuple[Fraction, int, int]] = []
            endpoint_violations = 0
            endpoint_target_zeros: list[tuple[int, int]] = []
            for face_index, (face, triple, side) in enumerate(
                zip(faces, triples, orientations)
            ):
                for test_label in active:
                    if test_label in face:
                        continue

                    def signed_at(position: Point) -> Fraction:
                        local = dict(points)
                        local[moving] = position
                        return side * orient(
                            local[triple[0]],
                            local[triple[1]],
                            local[triple[2]],
                            local[test_label],
                        )

                    value0 = signed_at(start)
                    value1 = signed_at(endpoint)
                    assert value0 >= 0
                    if value1 < 0:
                        endpoint_violations += 1
                    if value1 == 0 and set(face) | {test_label} == set(circuit):
                        endpoint_target_zeros.append((face_index, test_label))
                    if value0 > 0 and value1 <= 0:
                        root = value0 / (value0 - value1)
                        assert 0 < root <= 1
                        roots.append((root, face_index, test_label))

            assert endpoint_target_zeros, (target_name, moving)
            first_root = min(root for root, _, _ in roots)
            first_walls = [
                (face_index, test_label)
                for root, face_index, test_label in roots
                if root == first_root
            ]
            first_circuits = sorted(
                {
                    tuple(sorted(set(faces[face_index]) | {test_label}))
                    for face_index, test_label in first_walls
                }
            )
            target_is_first = any(set(labels) == set(circuit) for labels in first_circuits)
            first_point = segment_point(start, endpoint, first_root)
            displacement_squared = dot(sub(endpoint, start), sub(endpoint, start))
            records.append(
                {
                    "target": target_name,
                    "target_circuit": list(circuit),
                    "moving_label": moving,
                    "fixed_plane_labels": list(fixed),
                    "target_parameter": "1",
                    "first_wall_parameter": q(first_root),
                    "first_wall_parameter_decimal": float(first_root),
                    "first_wall_circuits": [list(labels) for labels in first_circuits],
                    "target_is_first_wall": target_is_first,
                    "strictly_earlier_wall": first_root < 1 and not target_is_first,
                    "endpoint_support_violations": endpoint_violations,
                    "target_zero_face_tests": [list(item) for item in endpoint_target_zeros],
                    "orthogonal_displacement_squared": q(displacement_squared),
                    "first_wall_moving_point": [q(value) for value in first_point],
                }
            )

    assert all(record["strictly_earlier_wall"] for record in records)
    payload = {
        "result": (
            "Every one-row orthogonal realization of either natural carrier "
            "flattening hits an unrelated exact hull circuit before the intended wall."
        ),
        "scope": (
            "This excludes the fixed-other-rows, straight orthogonal projection "
            "template. It does not exclude coordinated multi-row preconditioning."
        ),
        "source_points": str(POINTS_CSV.relative_to(ROOT)),
        "source_faces": str(FACES_JSON.relative_to(ROOT)),
        "active_vertex_count": len(active),
        "face_count": len(faces),
        "all_eight_variants_obstructed": True,
        "records": records,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    for record in records:
        print(
            record["target"],
            "move", record["moving_label"],
            "first", f"{record['first_wall_parameter_decimal']:.12g}",
            "circuit", record["first_wall_circuits"][0],
        )
    print("PASS all eight direct-wall variants are pre-empted")


if __name__ == "__main__":
    main()
