"""Shared numerical helpers for the Stage-31 H1011 attack proposer."""
from __future__ import annotations

import csv
from fractions import Fraction as Q

import numpy as np
from scipy.spatial import ConvexHull

from actual_hull_mechanics import _merge_coplanar_facets, evaluate


BASE = (0, 54, *range(1, 17))
BASE_SET = set(BASE)
CARRIER_ROWS = (198, 228, 245, 246, 263, 264)
PRIMARY = (7, 8, 245)


def read_exact_rows(path):
    rows = {}
    with path.open(newline="") as handle:
        for row in csv.DictReader(handle):
            rows[int(row["source_id"])] = tuple(
                Q(row[column]) for column in ("x", "y", "z")
            )
    return rows


def qadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def qsub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def qmul(a, scalar):
    return tuple(x * scalar for x in a)


def qdot(a, b):
    return sum(x * y for x, y in zip(a, b))


def qcross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def mechanics_vector(mechanics, face_keys, vertex_keys, edge_keys):
    return np.asarray(
        [mechanics.face_decisions[key] for key in face_keys]
        + [mechanics.vertex_decisions[key] for key in vertex_keys]
        + [mechanics.edge_decisions[key] for key in edge_keys]
    )


def support_specs(labels, points, faces, centroid, threshold=1e-4):
    index = {label: offset for offset, label in enumerate(labels)}
    near = []
    all_rows = []
    for face_index, face in enumerate(faces):
        offsets = [index[label] for label in face]
        a, b, c = points[offsets[:3]]
        normal = np.cross(b - a, c - a)
        orientation = -1 if np.dot(normal, centroid - a) > 0 else 1
        incident = set(offsets)
        for witness in range(len(labels)):
            if witness in incident:
                continue
            value = -orientation * np.dot(normal, points[witness] - a)
            value /= np.linalg.norm(normal)
            if value <= 0:
                raise AssertionError(("bad source support", face_index, labels[witness], value))
            row = (face_index, witness, orientation, float(value))
            all_rows.append(row)
            if value < threshold:
                near.append(row)
    return near, all_rows


def support_values(labels, points, faces, specs):
    index = {label: offset for offset, label in enumerate(labels)}
    values = []
    for face_index, witness, orientation, _source in specs:
        offsets = [index[label] for label in faces[face_index]]
        a, b, c = points[offsets[:3]]
        normal = np.cross(b - a, c - a)
        value = -orientation * np.dot(normal, points[witness] - a)
        values.append(value / np.linalg.norm(normal))
    return np.asarray(values)


def exactify_velocity(exact_rows, labels, float_velocity):
    p0 = exact_rows[0]
    basis_u = qsub(exact_rows[1], p0)
    basis_v = qsub(exact_rows[2], p0)
    basis_float = np.column_stack(
        ([float(x) for x in basis_u], [float(x) for x in basis_v])
    )
    velocity = {}
    coefficients_packet = {}
    for offset, label in enumerate(labels):
        raw = float_velocity[offset]
        if label in BASE_SET:
            coefficients, *_ = np.linalg.lstsq(basis_float, raw, rcond=None)
            alpha = Q(format(float(coefficients[0]), ".17g"))
            beta = Q(format(float(coefficients[1]), ".17g"))
            velocity[label] = qadd(qmul(basis_u, alpha), qmul(basis_v, beta))
            coefficients_packet[str(label)] = [str(alpha), str(beta)]
        else:
            velocity[label] = tuple(Q(format(float(value), ".17g")) for value in raw)
    normal = qcross(basis_u, basis_v)
    for label in BASE:
        if qdot(normal, velocity[label]):
            raise AssertionError(("base velocity left exact plane", label))
    return velocity, coefficients_packet


def signature(mechanics):
    return {
        "f_vector": [mechanics.vertices, mechanics.edges, mechanics.faces],
        "class": list(mechanics.cls),
        "stable_faces": sorted(sorted(face) for face in mechanics.stable_faces),
        "unstable_vertices": sorted(mechanics.unstable_vertices),
        "saddle_edges": sorted(sorted(edge) for edge in mechanics.saddle_edges),
        "active_labels": list(mechanics.active_labels),
    }


def actual_faces(labels, points):
    hull = ConvexHull(points)
    cycles, _normals = _merge_coplanar_facets(points, hull)
    return [[labels[offset] for offset in cycle] for cycle in cycles]


def full_signature(labels, points, mechanics=None):
    if mechanics is None:
        mechanics = evaluate(labels, points)
    result = signature(mechanics)
    result["maximal_faces"] = sorted(sorted(face) for face in actual_faces(labels, points))
    return result
