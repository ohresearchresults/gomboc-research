#!/usr/bin/env python3
"""Exact shared contract for the post-relay class-reduction front."""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
SIDE = HERE.parent
ATTACK = SIDE.parent
TRACK = ATTACK.parent
sys.path.insert(0, str(SIDE))
import relay_common as rc  # noqa: E402
sys.path.insert(0, str(ATTACK / "continuation" / "main"))
import propose_full_control as chart  # noqa: E402


SOURCE = SIDE / "far_u1.csv"
SOURCE_VERIFICATION = SIDE / "death_verification.json"
FACES = rc.FACES
EXPECTED_SOURCE_SHA256 = "9f6c84382c05502766a17feb0cb9346bd44ec9f889e566e3e102d3d63a29ed77"
EXPECTED_VERIFICATION_SHA256 = "86b1fb7f4e352ec162979620be43d6b02b5d5117d9e3fd305e04d84912a0ed03"
BASE_KEY = tuple(sorted(rc.BASE))

PAIR_SPECS = {
    "U1_H1011": ("U1", "H1011"),
    "U1_H56": ("U1", "H56"),
    "SBASE_H1011": ("SBASE_H1011", "H1011_BASE_BETA"),
    "SBASE_H56": ("SBASE_H56", "H56_BASE_BETA"),
}

PAIR_PRIORITY = (
    "U1_H1011",
    "U1_H56",
    "SBASE_H1011",
    "SBASE_H56",
)


class Jet:
    """Exact first-order dual number, retaining only value and first jet."""

    __slots__ = ("value", "derivative")

    def __init__(self, value=Q(0), derivative=Q(0)):
        self.value = Q(value)
        self.derivative = Q(derivative)

    @staticmethod
    def coerce(other):
        if isinstance(other, Jet):
            return other
        if isinstance(other, rc.ex.P):
            if other.degree:
                raise TypeError("cannot coerce nonconstant polynomial to Jet")
            return Jet(other.c[0])
        return Jet(other)

    def __add__(self, other):
        other = Jet.coerce(other)
        return Jet(self.value + other.value, self.derivative + other.derivative)

    __radd__ = __add__

    def __neg__(self):
        return Jet(-self.value, -self.derivative)

    def __sub__(self, other):
        return self + (-Jet.coerce(other))

    def __rsub__(self, other):
        return Jet.coerce(other) - self

    def __mul__(self, other):
        other = Jet.coerce(other)
        return Jet(
            self.value * other.value,
            self.derivative * other.value + self.value * other.derivative,
        )

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        scalar = Q(scalar)
        return Jet(self.value / scalar, self.derivative / scalar)

    def __eq__(self, other):
        try:
            other = Jet.coerce(other)
        except (TypeError, ValueError):
            return False
        return self.value == other.value and self.derivative == other.derivative

    def __bool__(self):
        return bool(self.value or self.derivative)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def bindings() -> dict:
    if sha256(SOURCE) != EXPECTED_SOURCE_SHA256:
        raise AssertionError("FAR source hash drift")
    if sha256(SOURCE_VERIFICATION) != EXPECTED_VERIFICATION_SHA256:
        raise AssertionError("death verification hash drift")
    verification = json.loads(SOURCE_VERIFICATION.read_text())
    if verification.get("verdict") != "INDEPENDENT_EXACT_U54_DEATH_VERIFICATION_PASS":
        raise AssertionError(("death verification verdict", verification.get("verdict")))
    if not verification.get("relay_complete"):
        raise AssertionError("death verification does not complete relay")
    if verification["source_hashes"][rc.relative(SOURCE)] != EXPECTED_SOURCE_SHA256:
        raise AssertionError("death verification FAR binding drift")
    return {
        rc.relative(SOURCE): sha256(SOURCE),
        rc.relative(SOURCE_VERIFICATION): sha256(SOURCE_VERIFICATION),
        rc.relative(FACES): sha256(FACES),
        rc.relative(rc.EXACT_CORE): sha256(rc.EXACT_CORE),
        rc.relative(Path(chart.__file__)): sha256(Path(chart.__file__)),
        rc.relative(SIDE / "relay_common.py"): sha256(SIDE / "relay_common.py"),
    }


def affine_path(source, velocity):
    return {
        label: tuple(rc.ex.P((source[label][axis], velocity[label][axis])) for axis in range(3))
        for label in source
    }


def evaluate_path(path, parameter: Q):
    return {
        label: tuple(value.eval(parameter) for value in xyz)
        for label, xyz in path.items()
    }


def primitive_first_jets(source, velocity, faces):
    points = {
        label: tuple(Jet(source[label][axis], velocity[label][axis]) for axis in range(3))
        for label in source
    }
    rows = list(rc.primitive_rows(points, faces))
    if len(rows) != 7922:
        raise AssertionError(("primitive first-jet row count", len(rows)))
    out = []
    for name, value, family in rows:
        if not isinstance(value, Jet):
            value = Jet.coerce(value)
        out.append((name, value.value, value.derivative, family))
    return out


def exact_modes(source):
    labels = sorted(source)
    points = np.asarray([[float(value) for value in source[label]] for label in labels])
    modes, names, plane_normal = chart.build_modes(labels, points)
    if len(modes) != 165:
        raise AssertionError(("mode count", len(modes)))
    exact = []
    for mode, name in zip(modes, names):
        velocity, _coefficients = chart.common.exactify_velocity(source, labels, mode)
        moving_label = name[0]
        if any(
            any(component for component in value)
            for label, value in velocity.items()
            if label != moving_label
        ):
            raise AssertionError(("non-sparse exact mode", name))
        exact.append(velocity)
    return labels, modes, names, exact, plane_normal


def combine_velocity(exact_modes_packet, coefficients):
    labels = exact_modes_packet[0].keys()
    return {
        label: tuple(
            sum(
                (coefficient * mode[label][axis] for coefficient, mode in zip(coefficients, exact_modes_packet)),
                Q(0),
            )
            for axis in range(3)
        )
        for label in labels
    }


def target_polynomials(path, faces):
    d6, xscaled = rc.ex.scaled_centered(path, faces)
    incidence, _neighbors, face_by_key = rc.ex.edge_data(faces)
    u1 = rc.ex.vertex_component(path, xscaled, 1, 54)

    h56 = rc.ex.edge_components(path, faces, xscaled, incidence, (5, 6))
    h1011 = rc.ex.edge_components(path, faces, xscaled, incidence, (10, 11))
    h56_one_minus = 4 * d6 * h56["direction_norm2"] - h56["t"]

    base_index = face_by_key[BASE_KEY]
    raw56, ref56 = rc.ex.face_component(path, faces, xscaled, base_index, (5, 6))
    raw1011, ref1011 = rc.ex.face_component(path, faces, xscaled, base_index, (10, 11))
    sign56 = 1 if ref56.eval(Q(0)) > 0 else -1
    sign1011 = 1 if ref1011.eval(Q(0)) > 0 else -1

    if incidence[(5, 6)][1] != base_index or incidence[(10, 11)][1] != base_index:
        raise AssertionError("base face is not beta2 owner for H56/H1011")
    return {
        "U1": u1,
        "H1011": h1011["t"],
        "H56": h56_one_minus,
        "SBASE_H1011": sign1011 * raw1011,
        "H1011_BASE_BETA": h1011["beta2"],
        "SBASE_H56": sign56 * raw56,
        "H56_BASE_BETA": h56["beta2"],
    }


TARGET_ALIASES = {
    "U1": ["edge:(1, 54):t", "vertex:1:54"],
    "H1011": ["edge:(10, 11):t", "vertex:10:11"],
    "H56": ["edge:(5, 6):one_minus_t", "vertex:6:5"],
    "SBASE_H1011": [f"face_raw:{BASE_KEY}:(10, 11)"],
    "H1011_BASE_BETA": ["edge:(10, 11):beta2"],
    "SBASE_H56": [f"face_raw:{BASE_KEY}:(5, 6)"],
    "H56_BASE_BETA": ["edge:(5, 6):beta2"],
}


EXPECTED_ENDPOINT_FEATURES = {
    "U1_H1011": {
        "class": [2, 1, 1],
        "stable_faces": rc.FAR_FEATURES["stable_faces"],
        "unstable_vertices": [8],
        "saddle_edges": [[5, 6]],
    },
    "U1_H56": {
        "class": [2, 1, 1],
        "stable_faces": rc.FAR_FEATURES["stable_faces"],
        "unstable_vertices": [8],
        "saddle_edges": [[10, 11]],
    },
    "SBASE_H1011": {
        "class": [1, 2, 1],
        "stable_faces": [list(rc.PRIMARY)],
        "unstable_vertices": rc.FAR_FEATURES["unstable_vertices"],
        "saddle_edges": [[5, 6]],
    },
    "SBASE_H56": {
        "class": [1, 2, 1],
        "stable_faces": [list(rc.PRIMARY)],
        "unstable_vertices": rc.FAR_FEATURES["unstable_vertices"],
        "saddle_edges": [[10, 11]],
    },
}
