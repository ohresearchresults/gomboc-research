#!/usr/bin/env python3
"""Exact obstruction to repairing a point configuration by one projective map.

For every prescribed face, this script evaluates the homogeneous 4x4
determinants against every other labelled point.  If two points occur with
opposite nonzero signs, the proposed face plane cuts the convex hull.  Such a
mixed pair remains mixed after every invertible projective transformation for
which all transformed points lie in one affine chart (all dehomogenising
coordinates have the same sign).  Consequently no affine/projective-only
support synthesis can expose that face.

The input arithmetic is exact: CSV coordinates may be fractions, decimals,
or common-lattice integers with a denominator column.
"""

from __future__ import annotations

import argparse
import csv
import json
from fractions import Fraction
from pathlib import Path
from typing import Iterable


Point = tuple[Fraction, Fraction, Fraction]


def frac(value: str) -> Fraction:
    value = value.strip()
    if not value:
        raise ValueError("empty exact coordinate")
    return Fraction(value)


def first_present(row: dict[str, str], names: Iterable[str]) -> str | None:
    for name in names:
        value = row.get(name)
        if value is not None and value.strip():
            return value
    return None


def load_points(path: Path) -> dict[int, Point]:
    points: dict[int, Point] = {}
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"{path}: missing CSV header")
        for line_number, row in enumerate(reader, 2):
            label_raw = first_present(row, ("source_id", "label", "id", "row"))
            if label_raw is None:
                raise ValueError(f"{path}:{line_number}: missing point label")
            label = int(label_raw)
            exact = [
                first_present(row, (f"{axis}_exact", axis))
                for axis in ("x", "y", "z")
            ]
            ints = [row.get(f"{axis}_int") for axis in ("x", "y", "z")]
            if all(value is not None and value.strip() for value in exact):
                point = tuple(frac(value or "") for value in exact)
            elif all(value is not None and value.strip() for value in ints):
                denominator_raw = first_present(row, ("denominator", "den", "scale"))
                if denominator_raw is None:
                    raise ValueError(
                        f"{path}:{line_number}: lattice integers need denominator"
                    )
                denominator = frac(denominator_raw)
                point = tuple(frac(value or "") / denominator for value in ints)
            else:
                decimals = [row.get(f"{axis}_decimal") for axis in ("x", "y", "z")]
                if not all(value is not None and value.strip() for value in decimals):
                    raise ValueError(
                        f"{path}:{line_number}: no recognized x/y/z coordinate columns"
                    )
                point = tuple(frac(value or "") for value in decimals)
            if label in points:
                raise ValueError(f"{path}:{line_number}: duplicate label {label}")
            points[label] = point  # type: ignore[assignment]
    if len(points) < 4:
        raise ValueError(f"{path}: need at least four labelled points")
    return points


def descend(payload: object, dotted_key: str) -> object:
    value = payload
    if dotted_key:
        for part in dotted_key.split("."):
            if isinstance(value, dict):
                value = value[part]
            elif isinstance(value, list) and part.isdigit():
                value = value[int(part)]
            else:
                raise KeyError(f"cannot descend through {part!r} in {dotted_key!r}")
    return value


def normalize_face(item: object) -> list[int]:
    if isinstance(item, dict):
        for key in ("vertices", "cycle", "face", "labels"):
            if key in item:
                item = item[key]
                break
    if not isinstance(item, list) or len(item) < 3:
        raise ValueError(f"invalid face record: {item!r}")
    face = [int(value) for value in item]
    if len(set(face)) != len(face):
        raise ValueError(f"face repeats a label: {face}")
    return face


def load_faces(path: Path, dotted_key: str) -> list[list[int]]:
    payload = json.loads(path.read_text())
    payload = descend(payload, dotted_key)
    if not isinstance(payload, list):
        raise ValueError(f"{path}:{dotted_key}: expected a list of faces")
    return [normalize_face(item) for item in payload]


def det3(a: Point, b: Point, c: Point) -> Fraction:
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def sub(a: Point, b: Point) -> Point:
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def orient(a: Point, b: Point, c: Point, d: Point) -> Fraction:
    return det3(sub(b, a), sub(c, a), sub(d, a))


def spanning_triple(face: list[int], points: dict[int, Point]) -> tuple[int, int, int]:
    anchor = face[0]
    for i in range(1, len(face) - 1):
        for j in range(i + 1, len(face)):
            triple = (anchor, face[i], face[j])
            pa, pb, pc = (points[label] for label in triple)
            if any(
                orient(pa, pb, pc, point) != 0
                for label, point in points.items()
                if label not in triple
            ):
                return triple
    raise ValueError(f"face {face} has no plane-defining triple")


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def audit_face(face: list[int], points: dict[int, Point]) -> dict[str, object]:
    missing = sorted(set(face) - set(points))
    if missing:
        raise ValueError(f"face {face}: absent labels {missing}")
    triple = spanning_triple(face, points)
    pa, pb, pc = (points[label] for label in triple)
    coplanarity = {
        label: orient(pa, pb, pc, points[label])
        for label in face
        if label not in triple
    }
    noncoplanar_face_labels = {
        str(label): q(value) for label, value in coplanarity.items() if value
    }
    signs: dict[int, Fraction] = {
        label: orient(pa, pb, pc, point)
        for label, point in points.items()
        if label not in face
    }
    positive = [(label, value) for label, value in signs.items() if value > 0]
    negative = [(label, value) for label, value in signs.items() if value < 0]
    zeros = [label for label, value in signs.items() if value == 0]
    if noncoplanar_face_labels:
        status = "prescribed_vertices_not_coplanar"
    elif positive and negative:
        status = "mixed_non_supporting"
    elif positive or negative:
        status = "supporting"
    else:
        status = "all_points_coplanar"
    result: dict[str, object] = {
        "face": face,
        "plane_triple": list(triple),
        "status": status,
        "positive_count": len(positive),
        "negative_count": len(negative),
        "additional_coplanar_labels": zeros,
        "noncoplanar_prescribed_labels": noncoplanar_face_labels,
    }
    if positive and negative:
        pos_label, pos_det = min(positive, key=lambda item: (abs(item[1]), item[0]))
        neg_label, neg_det = min(negative, key=lambda item: (abs(item[1]), item[0]))
        result["exact_mixed_witness"] = {
            "positive_label": pos_label,
            "positive_determinant": q(pos_det),
            "negative_label": neg_label,
            "negative_determinant": q(neg_det),
        }
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("points_csv", type=Path)
    parser.add_argument("faces_json", type=Path)
    parser.add_argument(
        "--face-key",
        default="",
        help="dot-separated path to the face list inside the JSON payload",
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    points = load_points(args.points_csv)
    faces = load_faces(args.faces_json, args.face_key)
    audits = [audit_face(face, points) for face in faces]
    mixed = [record for record in audits if record["status"] == "mixed_non_supporting"]
    supporting = [record for record in audits if record["status"] == "supporting"]
    payload = {
        "theorem": (
            "A mixed homogeneous determinant pair for one prescribed face is "
            "invariant under every invertible projective map whose transformed "
            "points share one affine chart. Such a map cannot expose that face."
        ),
        "points_csv": str(args.points_csv),
        "faces_json": str(args.faces_json),
        "point_count": len(points),
        "face_count": len(faces),
        "mixed_non_supporting_count": len(mixed),
        "supporting_count": len(supporting),
        "projective_only_synthesis_obstructed": bool(mixed),
        "faces": audits,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: payload[key] for key in (
        "point_count",
        "face_count",
        "mixed_non_supporting_count",
        "supporting_count",
        "projective_only_synthesis_obstructed",
    )}, indent=2))


if __name__ == "__main__":
    main()
