#!/usr/bin/env python3
"""Numerical proposer for actual convex-hull/own-centroid mechanics.

This is deliberately not an exact verifier.  It rebuilds the hull at every
call, merges Qhull's triangulation of coplanar maximal faces, computes the
ordinary-volume centroid, and then evaluates the complete S/U/H classification
on that actual hull.  Exactification is done separately once a chamber is
selected.
"""

from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.spatial import ConvexHull


@dataclass
class Mechanics:
    vertices: int
    edges: int
    faces: int
    stable_faces: list[tuple[int, ...]]
    unstable_vertices: list[int]
    saddle_edges: list[tuple[int, int]]
    centroid: np.ndarray
    active_labels: tuple[int, ...]
    min_nonzero_margin: float
    face_decisions: dict[tuple[int, ...], float]
    vertex_decisions: dict[int, float]
    edge_decisions: dict[tuple[int, int], float]

    @property
    def cls(self) -> tuple[int, int, int]:
        return (
            len(self.stable_faces),
            len(self.unstable_vertices),
            len(self.saddle_edges),
        )


def load_common_lattice(path: Path) -> tuple[list[int], np.ndarray]:
    labels: list[int] = []
    points: list[list[float]] = []
    with path.open(newline="") as handle:
        for row in csv.DictReader(handle):
            denominator = float(row["denominator"])
            labels.append(int(row["source_id"]))
            points.append(
                [float(row[column]) / denominator for column in ("x_int", "y_int", "z_int")]
            )
    return labels, np.asarray(points)


def _merge_coplanar_facets(
    points: np.ndarray, hull: ConvexHull, plane_digits: int = 9
) -> tuple[list[list[int]], list[np.ndarray]]:
    buckets: dict[tuple[float, ...], list[int]] = {}
    for index, equation in enumerate(hull.equations):
        key = tuple(np.round(equation, plane_digits))
        buckets.setdefault(key, []).append(index)

    cycles: list[list[int]] = []
    normals: list[np.ndarray] = []
    for facet_indices in buckets.values():
        vertices = sorted(
            set().union(*(set(hull.simplices[index]) for index in facet_indices))
        )
        normal = np.mean(hull.equations[facet_indices, :3], axis=0)
        normal /= np.linalg.norm(normal)
        centre = points[vertices].mean(axis=0)
        direction_u = points[vertices[0]] - centre
        direction_u -= normal * np.dot(direction_u, normal)
        direction_u /= np.linalg.norm(direction_u)
        direction_v = np.cross(normal, direction_u)
        cycle = sorted(
            vertices,
            key=lambda index: math.atan2(
                np.dot(points[index] - centre, direction_v),
                np.dot(points[index] - centre, direction_u),
            ),
        )
        area = np.zeros(3)
        for first, second in zip(cycle, cycle[1:] + cycle[:1]):
            area += np.cross(points[first], points[second])
        if np.dot(area, normal) < 0:
            cycle.reverse()
        cycles.append(cycle)
        normals.append(normal)
    return cycles, normals


def evaluate(labels: list[int], points: np.ndarray, strict: float = 1e-9) -> Mechanics:
    hull = ConvexHull(points)
    cycles, normals = _merge_coplanar_facets(points, hull)

    edge_faces: dict[tuple[int, int], list[int]] = {}
    neighbours: dict[int, set[int]] = {index: set() for index in range(len(points))}
    for face_index, cycle in enumerate(cycles):
        for first, second in zip(cycle, cycle[1:] + cycle[:1]):
            edge = tuple(sorted((first, second)))
            edge_faces.setdefault(edge, []).append(face_index)
            neighbours[first].add(second)
            neighbours[second].add(first)
    if not all(len(incident) == 2 for incident in edge_faces.values()):
        raise ValueError("facet merge did not produce a closed two-manifold")
    active = sorted(set().union(*(set(cycle) for cycle in cycles)))

    determinant_sum = 0.0
    moment_sum = np.zeros(3)
    for cycle in cycles:
        for offset in range(1, len(cycle) - 1):
            a, b, c = points[[cycle[0], cycle[offset], cycle[offset + 1]]]
            determinant = np.linalg.det(np.stack((a, b, c)))
            determinant_sum += determinant
            moment_sum += determinant * (a + b + c)
    if determinant_sum <= 0:
        raise ValueError("nonpositive oriented volume")
    centroid = moment_sum / (4 * determinant_sum)
    centred = points - centroid

    stable_faces: list[tuple[int, ...]] = []
    unstable_vertices: list[int] = []
    saddle_edges: list[tuple[int, int]] = []
    nonzero_margins: list[float] = []
    face_decisions: dict[tuple[int, ...], float] = {}
    vertex_decisions: dict[int, float] = {}
    edge_decisions: dict[tuple[int, int], float] = {}

    for face_index, cycle in enumerate(cycles):
        normal = normals[face_index]
        height = np.dot(normal, centred[cycle[0]])
        foot = height * normal
        reference = centred[cycle].mean(axis=0)
        values: list[float] = []
        for first, second in zip(cycle, cycle[1:] + cycle[:1]):
            value = np.dot(
                np.cross(centred[second] - centred[first], foot - centred[first]),
                normal,
            )
            if np.dot(
                np.cross(
                    centred[second] - centred[first], reference - centred[first]
                ),
                normal,
            ) < 0:
                value = -value
            values.append(value)
        normalized = [
            value
            / (
                np.linalg.norm(centred[second] - centred[first])
                * np.linalg.norm(normal)
            )
            for value, first, second in zip(values, cycle, cycle[1:] + cycle[:1])
        ]
        face_key = tuple(sorted(labels[index] for index in cycle))
        face_decisions[face_key] = min(normalized)
        nonzero_margins.extend(abs(value) for value in normalized if abs(value) > strict)
        if min(values) > strict:
            stable_faces.append(tuple(labels[index] for index in cycle))

    for index in active:
        values = [
            -np.dot(centred[index], centred[other] - centred[index])
            / (
                np.linalg.norm(centred[index])
                * np.linalg.norm(centred[other] - centred[index])
            )
            for other in neighbours[index]
        ]
        vertex_decisions[labels[index]] = min(values)
        nonzero_margins.extend(abs(value) for value in values if abs(value) > strict)
        if values and min(values) > strict:
            unstable_vertices.append(labels[index])

    for edge, incident in edge_faces.items():
        first, second = edge
        direction = centred[second] - centred[first]
        t = -np.dot(centred[first], direction) / np.dot(direction, direction)
        closest = centred[first] + t * direction
        normal1, normal2 = normals[incident[0]], normals[incident[1]]
        aa = np.dot(normal1, normal1)
        ab = np.dot(normal1, normal2)
        bb = np.dot(normal2, normal2)
        r1 = np.dot(closest, normal1)
        r2 = np.dot(closest, normal2)
        denominator = aa * bb - ab * ab
        beta1 = (r1 * bb - r2 * ab) / denominator
        beta2 = (r2 * aa - r1 * ab) / denominator
        closest_norm_squared = max(float(np.dot(closest, closest)), 1e-300)
        values = (
            t,
            1 - t,
            beta1 * np.sqrt(aa / closest_norm_squared),
            beta2 * np.sqrt(bb / closest_norm_squared),
        )
        edge_key = tuple(sorted((labels[first], labels[second])))
        edge_decisions[edge_key] = min(values)
        nonzero_margins.extend(abs(value) for value in values if abs(value) > strict)
        if min(values) > strict:
            saddle_edges.append(tuple(sorted((labels[first], labels[second]))))

    return Mechanics(
        vertices=len(active),
        edges=len(edge_faces),
        faces=len(cycles),
        stable_faces=stable_faces,
        unstable_vertices=unstable_vertices,
        saddle_edges=saddle_edges,
        centroid=centroid,
        active_labels=tuple(labels[index] for index in active),
        min_nonzero_margin=min(nonzero_margins),
        face_decisions=face_decisions,
        vertex_decisions=vertex_decisions,
        edge_decisions=edge_decisions,
    )
