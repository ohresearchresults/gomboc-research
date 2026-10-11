#!/usr/bin/env python3
"""Shared reconstruction and first-jet utilities for the far residual attack.

The frozen six-flip certificate is imported as read-only source material.  No
function in this module writes into, regenerates, or verifies that certificate.
All generated artifacts belong to this directory.
"""
from __future__ import annotations

import csv
import json
import sys
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np
from scipy import sparse


HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
ROOT = HERE.parents[3]
GROUPED = ROOT / "tracks/target_sphere_realizer/grouped_local_escape"
CIRCUIT = ROOT / "tracks/circuit_atlas"
sys.path[:0] = [str(PARENT), str(GROUPED), str(CIRCUIT)]

import build_certificate as frozen  # noqa: E402
import row54_four_residual_search as mechanics_core  # noqa: E402
from actual_grouped import evaluate as fresh_evaluate  # noqa: E402
from row54_full_minimax import guards as class_guards  # noqa: E402


BASE = frozenset(range(17)) | {54}
TARGET_FACE = frozenset((198, 243, 245))
TARGET_VERTEX = 1
TARGET_EDGES = ((4, 5), (12, 13))
EDGE_COMPONENT_NAMES = ("t", "one_minus_t", "beta1", "beta2")


def read_float_points(path: Path = PARENT / "far.csv"):
    rows = {}
    with path.open() as stream:
        for row in csv.DictReader(stream):
            rows[int(row["source_id"])] = np.asarray(
                [float(row[k]) for k in ("x", "y", "z")], dtype=float
            )
    ids = sorted(rows)
    return ids, np.asarray([rows[i] for i in ids], dtype=float)


def read_faces(path: Path = PARENT / "far_faces.json"):
    return json.loads(path.read_text())


def reconstruct_exact_far():
    """Rebuild the exact rational far endpoint without invoking frozen main()."""
    source, repair = frozen.gx.read_repaired(frozen.SOURCE)
    e1 = frozen.ex.sub(source[1], source[0])
    e2 = frozen.ex.sub(source[2], source[0])
    buffer_velocity = {i: (Q(0), Q(0), Q(0)) for i in source}
    for i, (a, b) in frozen.BUFFER_COEFFICIENTS.items():
        buffer_velocity[i] = frozen.ex.add(
            frozen.ex.mul(e1, a), frozen.ex.mul(e2, b)
        )
    buffered = frozen.at(frozen.line_points(source, buffer_velocity), Q(1))

    unit_velocity = {i: (Q(0), Q(0), Q(0)) for i in source}
    unit_velocity[244] = (Q(0), Q(0), Q(-1))
    unit_path = frozen.line_points(source, unit_velocity)
    depth = frozen.root_of_line(unit_path, (198, 243, 244, 245))
    cross_velocity = {
        i: frozen.ex.mul(unit_velocity[i], depth) for i in unit_velocity
    }
    post = frozen.at(
        frozen.line_points(buffered, cross_velocity), frozen.CROSS_POST
    )
    far, denominators = frozen.projective_endpoint(post, Q(3, 2))
    return far, read_faces(), {
        "base_repair": repair,
        "target_depth": frozen.ex.qs(depth),
        "minimum_projective_denominator": frozen.ex.qs(
            min(denominators.values())
        ),
    }


def exact_to_float(ids: Sequence[int], points):
    return np.asarray(
        [[float(z) for z in points[i]] for i in ids], dtype=float
    )


@dataclass(frozen=True)
class Control:
    vertex: int
    name: str
    vector: tuple[float, float, float]


def full_controls(ids: Sequence[int], points: np.ndarray):
    """Return the complete 165D affine chart preserving the enlarged base.

    Each of the 18 base vertices has two in-plane controls.  Every other row
    has three free controls.  Directions are scaled to the source RMS radius,
    so one coefficient has a comparable physical meaning across rows.
    """
    ix = {i: k for k, i in enumerate(ids)}
    center = np.mean(points, axis=0)
    scale = float(np.sqrt(np.mean(np.sum((points - center) ** 2, axis=1))))
    a = points[ix[0]]
    u = points[ix[1]] - a
    u /= np.linalg.norm(u)
    normal = np.cross(points[ix[1]] - a, points[ix[2]] - a)
    normal /= np.linalg.norm(normal)
    v = np.cross(normal, u)
    controls: list[Control] = []
    for vertex in ids:
        if vertex in BASE:
            controls.append(
                Control(vertex, f"v{vertex}:base_u", tuple(scale * u))
            )
            controls.append(
                Control(vertex, f"v{vertex}:base_v", tuple(scale * v))
            )
        else:
            for axis, name in enumerate("xyz"):
                direction = np.zeros(3)
                direction[axis] = scale
                controls.append(
                    Control(vertex, f"v{vertex}:{name}", tuple(direction))
                )
    if len(controls) != 165:
        raise AssertionError(("unexpected chart dimension", len(controls)))
    return controls, scale


def construct(points: np.ndarray, ids: Sequence[int], controls, coefficients):
    out = np.asarray(points, dtype=float).copy()
    ix = {i: k for k, i in enumerate(ids)}
    for coefficient, control in zip(coefficients, controls):
        out[ix[control.vertex]] += float(coefficient) * np.asarray(control.vector)
    return out


def _vertex_component(centered, ix, vertex, neighbor):
    x = centered[ix[vertex]]
    direction = centered[ix[neighbor]] - x
    return float(
        -np.dot(x, direction)
        / (np.linalg.norm(x) * np.linalg.norm(direction))
    )


def residual_components(ids, points, faces):
    """Return all 3*3*4*4 normalized edge-cone component families."""
    ix = {i: k for k, i in enumerate(ids)}
    m = mechanics_core.mechanics(ids, points, faces)
    face_index = next(
        k for k, face in enumerate(faces) if frozenset(face) == TARGET_FACE
    )
    face_cycle = faces[face_index]
    face_labels = [
        tuple(sorted(edge))
        for edge in zip(face_cycle, face_cycle[1:] + face_cycle[:1])
    ]
    face_values = {
        label: float(value)
        for label, value in zip(face_labels, m["fcomponents"][face_index])
    }
    _, neighbors = mechanics_core.edge_lattice(faces)
    centered = points - m["centroid"]
    vertex_values = {
        neighbor: _vertex_component(centered, ix, TARGET_VERTEX, neighbor)
        for neighbor in sorted(neighbors[TARGET_VERTEX])
    }
    edge_values = {
        edge: {
            name: float(value)
            for name, value in zip(EDGE_COMPONENT_NAMES, m["ecomponents"][edge])
        }
        for edge in TARGET_EDGES
    }
    return {
        "face": face_values,
        "vertex": vertex_values,
        "edges": edge_values,
    }


def flatten_residual_components(packet):
    labels = []
    values = []
    for edge, value in sorted(packet["face"].items()):
        labels.append(("S198_243_245", edge))
        values.append(value)
    for neighbor, value in sorted(packet["vertex"].items()):
        labels.append(("U1", neighbor))
        values.append(value)
    for edge in TARGET_EDGES:
        for name in EDGE_COMPONENT_NAMES:
            labels.append((f"H{edge[0]}_{edge[1]}", name))
            values.append(packet["edges"][edge][name])
    return labels, np.asarray(values, dtype=float)


def class_guard_packet(ids, points, faces):
    values, labels = class_guards(
        mechanics_core.mechanics(ids, points, faces), faces
    )
    normalized = []
    for kind, item in labels:
        if isinstance(item, list):
            item = tuple(sorted(item))
        normalized.append((kind, item))
    return np.asarray(values, dtype=float), normalized


def finite_difference_jacobian(function, coefficients, epsilon=2e-7):
    base = np.asarray(coefficients, dtype=float)
    f0 = np.asarray(function(base), dtype=float)
    jac = np.zeros((len(f0), len(base)), dtype=float)
    for j in range(len(base)):
        step = np.zeros_like(base)
        step[j] = epsilon
        plus = np.asarray(function(base + step), dtype=float)
        minus = np.asarray(function(base - step), dtype=float)
        jac[:, j] = (plus - minus) / (2.0 * epsilon)
    return f0, jac


@dataclass(frozen=True)
class SupportRow:
    face_index: int
    face: tuple[int, ...]
    witness: int
    triple: tuple[int, int, int]
    orientation: int


def _noncollinear_triple(face, point_map):
    a = face[0]
    for j in range(1, len(face) - 1):
        for k in range(j + 1, len(face)):
            b, c = face[j], face[k]
            if np.linalg.norm(
                np.cross(point_map[b] - point_map[a], point_map[c] - point_map[a])
            ) > 1e-14:
                return a, b, c
    raise ValueError(("degenerate face", face))


def support_first_jet(ids, points, faces, controls, scale):
    """Build every strict face/witness support row and its affine first jet."""
    point_map = {i: points[k] for k, i in enumerate(ids)}
    controls_by_vertex: dict[int, list[tuple[int, np.ndarray]]] = {}
    for j, control in enumerate(controls):
        controls_by_vertex.setdefault(control.vertex, []).append(
            (j, np.asarray(control.vector, dtype=float))
        )

    rows: list[SupportRow] = []
    values = []
    data = []
    row_indices = []
    column_indices = []
    scale3 = scale**3
    all_ids = set(ids)
    for face_index, face0 in enumerate(faces):
        face = tuple(face0)
        a, b, c = _noncollinear_triple(face, point_map)
        pa, pb, pc = point_map[a], point_map[b], point_map[c]
        ab, ac = pb - pa, pc - pa
        raw_values = {
            witness: float(np.dot(ab, np.cross(ac, point_map[witness] - pa)))
            for witness in sorted(all_ids - set(face))
        }
        signs = {1 if value > 0 else -1 for value in raw_values.values() if value}
        if len(signs) != 1 or len(raw_values) != len(all_ids - set(face)):
            raise AssertionError(("nonstrict support source", face_index, signs))
        orientation = signs.pop()
        for witness, raw in raw_values.items():
            row_number = len(rows)
            rows.append(
                SupportRow(face_index, face, witness, (a, b, c), orientation)
            )
            values.append(orientation * raw / scale3)
            relevant = set((a, b, c, witness))
            for vertex in relevant:
                for column, velocity in controls_by_vertex.get(vertex, []):
                    va = velocity if vertex == a else np.zeros(3)
                    vb = velocity if vertex == b else np.zeros(3)
                    vc = velocity if vertex == c else np.zeros(3)
                    vw = velocity if vertex == witness else np.zeros(3)
                    derivative = (
                        np.dot(vb - va, np.cross(ac, point_map[witness] - pa))
                        + np.dot(ab, np.cross(vc - va, point_map[witness] - pa))
                        + np.dot(ab, np.cross(ac, vw - va))
                    )
                    derivative *= orientation / scale3
                    if derivative:
                        row_indices.append(row_number)
                        column_indices.append(column)
                        data.append(float(derivative))
    matrix = sparse.csr_matrix(
        (data, (row_indices, column_indices)),
        shape=(len(rows), len(controls)),
    )
    return rows, np.asarray(values, dtype=float), matrix


def target_guard_indices(labels):
    targets = {
        ("S-", tuple(sorted(TARGET_FACE))),
        ("U-", TARGET_VERTEX),
        ("H-", TARGET_EDGES[0]),
        ("H-", TARGET_EDGES[1]),
    }
    return [k for k, label in enumerate(labels) if label in targets]


def fresh_summary(ids, points, coplanar_rel=2e-12):
    packet = {i: points[k] for k, i in enumerate(ids)}
    result = fresh_evaluate(packet, coplanar_rel=coplanar_rel)
    if not result.valid:
        raise AssertionError(result.error)
    return result


def rational(value: float, digits: int = 14):
    return Q(format(float(value), f".{digits}g"))


def exact_velocity_from_coefficients(exact_points, ids, coefficients):
    """Rationalize a full-chart direction while keeping the base exact."""
    e1 = frozen.ex.sub(exact_points[1], exact_points[0])
    e2raw = frozen.ex.sub(exact_points[2], exact_points[0])
    # e1/e2raw are an exact independent base-plane basis.  Numeric chart
    # directions are re-expanded in this basis below by least squares.
    exact_float = exact_to_float(ids, exact_points)
    float_controls, scale = full_controls(ids, exact_float)
    ix = {i: k for k, i in enumerate(ids)}
    velocity_float = np.zeros_like(exact_float)
    for coefficient, control in zip(coefficients, float_controls):
        velocity_float[ix[control.vertex]] += float(coefficient) * np.asarray(
            control.vector
        )
    basis = np.asarray(
        [[float(z) for z in e1], [float(z) for z in e2raw]], dtype=float
    ).T
    velocity = {i: (Q(0), Q(0), Q(0)) for i in ids}
    for i in ids:
        if i in BASE:
            coeff, *_ = np.linalg.lstsq(basis, velocity_float[ix[i]], rcond=None)
            velocity[i] = frozen.ex.add(
                frozen.ex.mul(e1, rational(coeff[0])),
                frozen.ex.mul(e2raw, rational(coeff[1])),
            )
        else:
            velocity[i] = tuple(rational(z) for z in velocity_float[ix[i]])
    return velocity, scale


def rail_edges():
    return frozen.forced_rails()


def face_keys(faces: Iterable[Sequence[int]]):
    return {frozenset(face) for face in faces}

