#!/usr/bin/env python3
"""Global MILP for the desired centre cell of the deep target geometry.

With the boundary geometry fixed, every unnormalised face-foot, vertex-support
and edge four-component sign is affine in the proposed centre c.  Positive
features are intersections of halfspaces; excluding a feature is the finite
disjunction that at least one component is negative.  Binary selectors encode
all such disjunctions.  Maximising a common normalized margin therefore gives
a global answer for the entire fixed-geometry centre-shift template.
"""

from __future__ import annotations

import csv
import argparse
import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix

import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CIRCUIT = ROOT / "tracks" / "circuit_atlas"
sys.path.insert(0, str(CIRCUIT))
import row54_four_residual_search as core  # noqa: E402


POINTS = CIRCUIT / "robust_target_rebuilt.csv"
FACES = CIRCUIT / "robust_target_rebuilt_faces.json"
OUTPUT = HERE / "fixed_geometry_center_milp.json"
BASE = tuple(range(17))


@dataclass(frozen=True)
class Affine:
    coefficients: np.ndarray
    constant: float

    def maximum_on_box(self, lower: np.ndarray, upper: np.ndarray) -> float:
        return self.constant + float(
            np.sum(np.where(self.coefficients >= 0, self.coefficients * upper,
                            self.coefficients * lower))
        )


def affine(function) -> Affine:
    zero = np.zeros(3)
    constant = float(function(zero))
    coefficients = np.asarray(
        [float(function(np.eye(3)[coordinate])) - constant for coordinate in range(3)]
    )
    return Affine(coefficients, constant)


def load(points_path: Path = POINTS, faces_path: Path = FACES):
    rows = {}
    with points_path.open(newline="") as handle:
        for row in csv.DictReader(handle):
            rows[int(row["source_id"])] = np.asarray(
                [float(row[column]) for column in ("x", "y", "z")]
            )
    labels = sorted(rows)
    points = np.asarray([rows[label] for label in labels])
    faces = json.loads(faces_path.read_text())
    normals = core.face_normals(labels, points, faces)
    edge_faces, neighbours = core.edge_lattice(faces)
    scale = float(np.sqrt(np.mean(np.sum((points - points.mean(axis=0)) ** 2, axis=1))))
    return rows, labels, points, faces, normals, edge_faces, neighbours, scale


def component_system(
    points_path: Path = POINTS,
    faces_path: Path = FACES,
    base: tuple[int, ...] = BASE,
    target_unstable: tuple[int, ...] = (8,),
):
    rows, labels, points, faces, normals, edge_faces, neighbours, scale = load(
        points_path, faces_path
    )
    direct: list[tuple[str, Affine]] = []
    exclusions: list[tuple[str, list[Affine]]] = []

    # The centre of a positive-density convex body is strictly inside every face.
    for face, normal in zip(faces, normals):
        denominator = np.linalg.norm(normal) * scale
        direct.append((
            f"inside:{sorted(face)}",
            affine(lambda centre, face=face, normal=normal, denominator=denominator:
                   np.dot(normal, rows[face[0]] - centre) / denominator),
        ))

    for face, normal in zip(faces, normals):
        reference = np.mean([rows[label] for label in face], axis=0)
        components: list[Affine] = []
        for first, second in zip(face, face[1:] + face[:1]):
            edge = rows[second] - rows[first]
            denominator = np.linalg.norm(edge) * np.linalg.norm(normal) * scale
            reference_sign = float(np.dot(np.cross(edge, reference - rows[first]), normal))

            def face_component(
                centre, first=first, edge=edge, normal=normal,
                denominator=denominator, reference_sign=reference_sign
            ):
                height = np.dot(normal, rows[first] - centre)
                foot = normal * height / np.dot(normal, normal)
                value = float(np.dot(np.cross(edge, foot - (rows[first] - centre)), normal))
                return (value if reference_sign > 0 else -value) / denominator

            components.append(affine(face_component))
        if tuple(sorted(face)) == tuple(sorted(base)):
            direct.extend((f"base_stable:{first}", component) for first, component in enumerate(components))
        else:
            exclusions.append((f"nonstable:{sorted(face)}", components))

    for label in labels:
        components = []
        for neighbour in sorted(neighbours[label]):
            direction = rows[neighbour] - rows[label]
            denominator = np.linalg.norm(direction) * scale
            components.append(affine(
                lambda centre, label=label, direction=direction, denominator=denominator:
                np.dot(centre - rows[label], direction) / denominator
            ))
        if label in target_unstable:
            direct.extend((f"U{label}:{offset}", component) for offset, component in enumerate(components))
        else:
            exclusions.append((f"nonunstable:{label}", components))

    for edge, incident in sorted(edge_faces.items()):
        first, second = edge
        direction = rows[second] - rows[first]
        normal1, normal2 = normals[incident[0]], normals[incident[1]]
        aa, ab, bb = (
            float(np.dot(normal1, normal1)),
            float(np.dot(normal1, normal2)),
            float(np.dot(normal2, normal2)),
        )
        denominator = aa * bb - ab * ab

        def all_edge_components(centre):
            t = float(np.dot(centre - rows[first], direction) / np.dot(direction, direction))
            closest = rows[first] - centre + t * direction
            r1, r2 = float(np.dot(closest, normal1)), float(np.dot(closest, normal2))
            beta1 = (r1 * bb - r2 * ab) / denominator
            beta2 = (r2 * aa - r1 * ab) / denominator
            return (t, 1 - t, beta1 * np.sqrt(aa) / scale, beta2 * np.sqrt(bb) / scale)

        components = []
        for offset in range(4):
            components.append(affine(
                lambda centre, offset=offset: all_edge_components(centre)[offset]
            ))
        exclusions.append((f"nonsaddle:{list(edge)}", components))

    return points, direct, exclusions


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--points", type=Path, default=POINTS)
    parser.add_argument("--faces", type=Path, default=FACES)
    parser.add_argument("--base", default=",".join(map(str, BASE)))
    parser.add_argument("--unstable", default="8")
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--time-limit", type=float, default=180.0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    base = tuple(int(value) for value in args.base.split(",") if value)
    target_unstable = tuple(int(value) for value in args.unstable.split(",") if value)
    points, direct, exclusions = component_system(
        args.points, args.faces, base, target_unstable
    )
    lower_centre = points.min(axis=0)
    upper_centre = points.max(axis=0)
    margin_lower, margin_upper = -2.0, 2.0
    binary_count = sum(len(components) for _, components in exclusions)
    variable_count = 4 + binary_count

    lower = np.concatenate((lower_centre, [margin_lower], np.zeros(binary_count)))
    upper = np.concatenate((upper_centre, [margin_upper], np.ones(binary_count)))
    integrality = np.concatenate((np.zeros(4), np.ones(binary_count)))
    objective = np.zeros(variable_count)
    objective[3] = -1.0

    row_indices: list[int] = []
    column_indices: list[int] = []
    data: list[float] = []
    bounds: list[float] = []
    row = 0

    # Direct positive component: a.c+b >= margin.
    for _, component in direct:
        for coordinate in range(3):
            row_indices.append(row)
            column_indices.append(coordinate)
            data.append(-component.coefficients[coordinate])
        row_indices.append(row)
        column_indices.append(3)
        data.append(1.0)
        bounds.append(component.constant)
        row += 1

    binary_offset = 4
    selector_metadata = []
    for feature, components in exclusions:
        selector_columns = []
        for component in components:
            selector = binary_offset
            binary_offset += 1
            selector_columns.append(selector)
            # f(c)+margin <= M(1-y).
            maximum = component.maximum_on_box(lower_centre, upper_centre) + margin_upper
            big_m = max(1.0, maximum + 1.0)
            for coordinate in range(3):
                row_indices.append(row)
                column_indices.append(coordinate)
                data.append(component.coefficients[coordinate])
            row_indices.extend((row, row))
            column_indices.extend((3, selector))
            data.extend((1.0, big_m))
            bounds.append(big_m - component.constant)
            row += 1
        # At least one component is selected as the strict negative witness.
        for selector in selector_columns:
            row_indices.append(row)
            column_indices.append(selector)
            data.append(-1.0)
        bounds.append(-1.0)
        selector_metadata.append((feature, selector_columns))
        row += 1

    matrix = coo_matrix((data, (row_indices, column_indices)), shape=(row, variable_count)).tocsr()
    constraint = LinearConstraint(matrix, -np.inf, np.asarray(bounds))
    result = milp(
        objective,
        integrality=integrality,
        bounds=Bounds(lower, upper),
        constraints=constraint,
        options={"time_limit": args.time_limit, "mip_rel_gap": 1e-10, "presolve": True},
    )
    record = {
        "version": 1,
        "points": str(args.points.resolve()),
        "faces": str(args.faces.resolve()),
        "target_base": list(base),
        "target_unstable_vertices": list(target_unstable),
        "status": int(result.status),
        "success": bool(result.success),
        "message": str(result.message),
        "direct_component_count": len(direct),
        "exclusion_feature_count": len(exclusions),
        "binary_selector_count": binary_count,
        "constraint_count": row,
        "mip_gap": None if getattr(result, "mip_gap", None) is None else float(result.mip_gap),
        "mip_node_count": None if getattr(result, "mip_node_count", None) is None else int(result.mip_node_count),
    }
    if result.x is not None:
        record["centre"] = result.x[:3].tolist()
        record["maximum_common_margin"] = float(result.x[3])
        record["strict_target_centre_cell_exists"] = bool(result.x[3] > 1e-9)
        selected = []
        for feature, columns in selector_metadata:
            choice = [offset for offset, column in enumerate(columns) if result.x[column] > 0.5]
            selected.append({"feature": feature, "selected_components": choice})
        record["selected_negative_witnesses"] = selected
    args.output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    print(json.dumps(record, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
