#!/usr/bin/env python3
"""Clean-room exact verifier for the F21 interior proposal.

This file deliberately does not import ``exact_interior_propose.py`` or any
local geometry/ledger module.  It freezes every authoritative input once,
reconstructs the prescribed cell and the complete source-to-candidate path
with :class:`fractions.Fraction`, and creates PASS artifacts only after all
checks have completed and every frozen path is still the same inode/version.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import os
import stat
import sys
import traceback
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path


sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ATTACK = MAIN.parents[1]
F20 = MAIN / "post_transfer_round15"

SOURCE = F20 / "far.csv"
FACES_FILE = F20 / "post_faces.json"
F20_CERTIFICATE = F20 / "certificate.json"
F20_VERIFICATION = F20 / "verification.json"
CHART = HERE / "chart.json"
PROPOSER = HERE / "exact_interior_propose.py"
CANDIDATE = HERE / "exact_interior_candidate.csv"
PROPOSAL = HERE / "exact_interior_proposal.json"
RECEIPT = HERE / "exact_interior_receipt.json"
SCAN = HERE / "exact_interior_event_scan.json"
OUTPUT = HERE / "exact_interior_verification.json"
LOG = HERE / "F21_INDEPENDENT_LOG.md"

BASE = tuple(range(17))
SHELL = tuple(range(231, 247))
TARGET_NAMES = (
    "S228_264_246_via_246_228",
    "U228_via_251",
    "U231_via_232",
    "U246_via_245",
    "H8_246_via_t",
    "H228_254_via_beta2",
    "H231_247_via_beta1",
    "H236_237_via_beta1",
)
EXPECTED_F_VECTOR = [61, 150, 91]
EXPECTED_CLASS = [2, 4, 4]
EXPECTED_UNSTABLE = [8, 228, 231, 246]
EXPECTED_SADDLES = [[8, 246], [228, 254], [231, 247], [236, 237]]
EXPECTED_FAMILIES = {
    "mechanics_denominator": 301,
    "support": 10529,
    "in_face_turn": 33,
    "face_component": 300,
    "vertex_component": 300,
    "edge_component": 900,
}
EXPECTED_LITERAL_FAMILIES = {
    "target": 8,
    "mechanics_guard": 333,
    "protected": 30,
    "near_support": 278,
    "in_face_turn": 33,
    "physical_plus": 183,
    "physical_minus": 183,
}
EXPECTED_LITERAL_DIGEST = (
    "1e419caf3ee6365fc9fd3b03779f6f7a33f601f28d95c6f2bf842a2e7a44a271"
)
EXPECTED_PATH_DIGEST = (
    "74f8a65a1c4e1c8748658128658d78d9b2b847ca89ec4b21316348cd6846a26e"
)
TRUST = Q(1, 100_000)
MAX_BERNSTEIN_DEPTH = 34


EXPECTED_INPUTS = {
    "f20_far": (SOURCE, 82321, "d34ebac9a1cfe81ce4d782049938ad68f1124eb82e3cd19342c30e5de14f39e3"),
    "f20_faces": (FACES_FILE, 3283, "06b15585bd906ae1ee0cfc5aefff2a46a5e752a02dfb556abde9225e1df81c6b"),
    "f20_certificate": (F20_CERTIFICATE, 121428, "51ceeecf32d32dedc6ae2fe3a05c9fd78d0c88ebbace7047b7be21b195ab77b2"),
    "f20_verification": (F20_VERIFICATION, 86818, "0e9f86e08325aa3272b3ad7c1768ac3270ef29d793c5d22ccc2536156193ff2a"),
    "chart": (CHART, 28897, "29ddf33a8126a2315a09eb6daee77b80b9691f1fd1b91e9a127e87699197b4b8"),
    "proposer": (PROPOSER, 64187, "93b6c983929db92ef9b9898b2a20c4424dfd872e7a5c3369073fb1cbf9de9fc5"),
    "candidate": (CANDIDATE, 343273, "52136b5bef94379e00445a0688865c56936ea7bc31db78e3f9fe90e8f755f110"),
    "proposal": (PROPOSAL, 1160861, "d1a481360259c1e5ecdeafbd9a4b2db38d7581c83ef995e475c295e71f17b30a"),
    "receipt": (RECEIPT, 24180, "8c13b9fbfa3f6d1dc16cb11213adbfac8658827dd19173a384722838ed447f8e"),
    "scan": (SCAN, 8936000, "17cbafcb58c9072947d845409e02d8ae0740a166d89b91c820c057071f56b6d3"),
}

SOURCE_HASHES = {
    "recovery2/main/post_transfer_round15/far.csv": EXPECTED_INPUTS["f20_far"][2],
    "recovery2/main/post_transfer_round15/post_faces.json": EXPECTED_INPUTS["f20_faces"][2],
    "recovery2/main/post_transfer_round15/certificate.json": EXPECTED_INPUTS["f20_certificate"][2],
    "recovery2/main/post_transfer_round15/verification.json": EXPECTED_INPUTS["f20_verification"][2],
}


class VerificationFailure(RuntimeError):
    """A fail-closed contract violation."""


def need(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationFailure(message)


def qslash(value: Q) -> str:
    value = Q(value)
    return f"{value.numerator}/{value.denominator}"


def qcompact(value: Q) -> str:
    value = Q(value)
    return str(value.numerator) if value.denominator == 1 else qslash(value)


def digest_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_hash(value) -> str:
    return digest_bytes(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    )


@dataclass
class FrozenInput:
    name: str
    path: Path
    data: bytes
    size: int
    sha256: str
    fd: int
    fingerprint: tuple[int, int, int, int, int, int]

    def ensure_path_unchanged(self) -> None:
        current = os.lstat(self.path)
        observed = (
            current.st_dev,
            current.st_ino,
            current.st_size,
            current.st_mtime_ns,
            current.st_ctime_ns,
            current.st_mode,
        )
        need(observed == self.fingerprint, f"input changed during verification: {self.path}")

    def close(self) -> None:
        os.close(self.fd)


def freeze_input(name: str, path: Path, expected_size: int, expected_hash: str) -> FrozenInput:
    flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
    try:
        fd = os.open(path, flags)
    except OSError as error:
        raise VerificationFailure(f"cannot freeze required input {path}: {error}") from error
    try:
        before = os.fstat(fd)
        need(stat.S_ISREG(before.st_mode), f"required input is not a regular file: {path}")
        need(before.st_size == expected_size, f"byte-count drift for {path.name}")
        chunks = []
        remaining = before.st_size
        while remaining:
            block = os.read(fd, min(1 << 20, remaining))
            need(bool(block), f"short read while freezing {path}")
            chunks.append(block)
            remaining -= len(block)
        need(os.read(fd, 1) == b"", f"input grew while freezing {path}")
        after = os.fstat(fd)
        fingerprint = (
            before.st_dev,
            before.st_ino,
            before.st_size,
            before.st_mtime_ns,
            before.st_ctime_ns,
            before.st_mode,
        )
        after_fingerprint = (
            after.st_dev,
            after.st_ino,
            after.st_size,
            after.st_mtime_ns,
            after.st_ctime_ns,
            after.st_mode,
        )
        need(fingerprint == after_fingerprint, f"input mutated while freezing {path}")
        data = b"".join(chunks)
        observed_hash = digest_bytes(data)
        need(len(data) == expected_size, f"frozen byte-count drift for {path.name}")
        need(observed_hash == expected_hash, f"sha256 drift for {path.name}")
        return FrozenInput(name, path, data, len(data), observed_hash, fd, fingerprint)
    except Exception:
        os.close(fd)
        raise


def reject_duplicate_pairs(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise VerificationFailure(f"duplicate JSON key: {key!r}")
        out[key] = value
    return out


def strict_json(data: bytes, label: str):
    try:
        return json.loads(data.decode("utf-8"), object_pairs_hook=reject_duplicate_pairs)
    except VerificationFailure:
        raise
    except Exception as error:
        raise VerificationFailure(f"invalid JSON in {label}: {error}") from error


def exact_keys(value: dict, expected, label: str) -> None:
    need(isinstance(value, dict), f"{label} must be an object")
    observed = set(value)
    expected = set(expected)
    need(observed == expected, f"unsupported {label} schema: missing={sorted(expected-observed)}, extra={sorted(observed-expected)}")


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def mul(a, scalar):
    return tuple(x * scalar for x in a)


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), Q(0))


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def det3(a, b, c):
    return dot(a, cross(b, c))


def norm2(a):
    return dot(a, a)


@dataclass(frozen=True, slots=True)
class Jet:
    v: Q
    d: tuple[Q, ...]

    def __post_init__(self):
        object.__setattr__(self, "v", Q(self.v))
        object.__setattr__(self, "d", tuple(Q(x) for x in self.d))

    @staticmethod
    def constant(value, dimension: int):
        return Jet(Q(value), (Q(0),) * dimension)

    def coerce(self, other):
        if isinstance(other, Jet):
            need(len(other.d) == len(self.d), "jet dimension mismatch")
            return other
        return Jet.constant(other, len(self.d))

    def __add__(self, other):
        other = self.coerce(other)
        return Jet(self.v + other.v, tuple(a + b for a, b in zip(self.d, other.d)))

    __radd__ = __add__

    def __neg__(self):
        return Jet(-self.v, tuple(-x for x in self.d))

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        return Jet(
            self.v * other.v,
            tuple(a * other.v + self.v * b for a, b in zip(self.d, other.d)),
        )

    __rmul__ = __mul__

    def inverse(self):
        need(self.v != 0, "division by zero jet")
        square = self.v * self.v
        return Jet(1 / self.v, tuple(-x / square for x in self.d))

    def __truediv__(self, other):
        return self * self.coerce(other).inverse()

    def __rtruediv__(self, other):
        return self.coerce(other) / self


@dataclass(frozen=True, slots=True)
class Poly:
    c: tuple[Q, ...]

    def __post_init__(self):
        coefficients = tuple(Q(x) for x in self.c)
        while len(coefficients) > 1 and coefficients[-1] == 0:
            coefficients = coefficients[:-1]
        object.__setattr__(self, "c", coefficients or (Q(0),))

    @staticmethod
    def zero():
        return Poly((Q(0),))

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Poly) else Poly((Q(value),))

    @property
    def degree(self):
        return len(self.c) - 1

    def __add__(self, other):
        other = Poly.coerce(other)
        width = max(len(self.c), len(other.c))
        return Poly(tuple(
            (self.c[i] if i < len(self.c) else Q(0))
            + (other.c[i] if i < len(other.c) else Q(0))
            for i in range(width)
        ))

    __radd__ = __add__

    def __neg__(self):
        return Poly(tuple(-x for x in self.c))

    def __sub__(self, other):
        return self + (-Poly.coerce(other))

    def __rsub__(self, other):
        return Poly.coerce(other) - self

    def __mul__(self, other):
        other = Poly.coerce(other)
        out = [Q(0)] * (len(self.c) + len(other.c) - 1)
        for i, left in enumerate(self.c):
            for j, right in enumerate(other.c):
                out[i + j] += left * right
        return Poly(tuple(out))

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        scalar = Q(scalar)
        need(scalar != 0, "polynomial scalar division by zero")
        return Poly(tuple(x / scalar for x in self.c))

    def derivative(self):
        return Poly(tuple(i * self.c[i] for i in range(1, len(self.c)))) if self.degree else Poly.zero()

    def eval(self, value: Q):
        out = Q(0)
        for coefficient in reversed(self.c):
            out = out * value + coefficient
        return out

    def affine(self, left: Q, right: Q):
        variable = Poly((Q(left), Q(right) - Q(left)))
        out = Poly.zero()
        for coefficient in reversed(self.c):
            out = out * variable + coefficient
        return out

    def exact(self):
        return [qcompact(x) for x in self.c]


def scalar_value(value):
    if isinstance(value, Jet):
        return value.v
    if isinstance(value, Poly):
        return value.c[0]
    return Q(value)


def nonzero_vector_at_source(vector) -> bool:
    return any(scalar_value(value) != 0 for value in vector)


def cycle_normal(cycle, points):
    anchor = points[cycle[0]]
    for offset in range(1, len(cycle) - 1):
        normal = cross(sub(points[cycle[offset]], anchor), sub(points[cycle[offset + 1]], anchor))
        if nonzero_vector_at_source(normal):
            return normal
    raise VerificationFailure(f"flat face cycle: {cycle}")


def read_rows(data: bytes, label: str):
    header = ["source_id", "x_exact", "y_exact", "z_exact", "x", "y", "z"]
    rows = {}
    try:
        stream = io.StringIO(data.decode("utf-8"), newline="")
        reader = csv.DictReader(stream, strict=True)
        need(reader.fieldnames == header, f"unsupported CSV schema in {label}")
        for line_number, record in enumerate(reader, 2):
            need(None not in record, f"extra CSV field at {label}:{line_number}")
            need(all(record[key] is not None for key in header), f"missing CSV field at {label}:{line_number}")
            row_id = int(record["source_id"])
            need(row_id not in rows, f"duplicate source_id {row_id} in {label}")
            point = tuple(Q(record[key]) for key in ("x_exact", "y_exact", "z_exact"))
            # Decimal columns are presentation-only.  They are parsed solely to reject
            # malformed/non-finite serialization and never enter a proof predicate.
            decimal = tuple(float(record[key]) for key in ("x", "y", "z"))
            need(all(math.isfinite(value) for value in decimal), f"non-finite CSV readback at {label}:{line_number}")
            rows[row_id] = point
    except VerificationFailure:
        raise
    except Exception as error:
        raise VerificationFailure(f"invalid CSV in {label}: {error}") from error
    need(len(rows) == 119, f"expected 119 rows in {label}, got {len(rows)}")
    return rows


def candidate_csv_bytes(rows) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream)
    writer.writerow(["source_id", "x_exact", "y_exact", "z_exact", "x", "y", "z"])
    for row_id, point in sorted(rows.items()):
        writer.writerow([
            row_id,
            *(qslash(value) for value in point),
            *(format(float(value), ".17g") for value in point),
        ])
    return stream.getvalue().encode("utf-8")


def validate_cycles(payload, rows):
    need(isinstance(payload, list) and len(payload) == 91, "post_faces must be a 91-cycle list")
    cycles = []
    signatures = set()
    for index, cycle in enumerate(payload):
        need(isinstance(cycle, list) and len(cycle) >= 3, f"invalid face cycle {index}")
        need(all(type(label) is int for label in cycle), f"non-integer face label at {index}")
        need(len(set(cycle)) == len(cycle), f"duplicate vertex within face {index}")
        need(set(cycle).issubset(rows), f"unknown vertex within face {index}")
        signature = tuple(sorted(cycle))
        need(signature not in signatures, f"duplicate face signature at {index}")
        signatures.add(signature)
        cycles.append(tuple(cycle))
    return cycles


def exactify_faces(rows, cycles):
    faces = []
    for index, original_cycle in enumerate(cycles):
        cycle = list(original_cycle)
        anchor = rows[cycle[0]]
        normal = None
        for left in range(1, len(cycle) - 1):
            for right in range(left + 1, len(cycle)):
                candidate = cross(sub(rows[cycle[left]], anchor), sub(rows[cycle[right]], anchor))
                if candidate != (Q(0), Q(0), Q(0)):
                    normal = candidate
                    break
            if normal is not None:
                break
        need(normal is not None, f"flat prescribed face {index}")
        height = dot(normal, anchor)
        values = {row_id: dot(normal, point) - height for row_id, point in rows.items()}
        positive = any(value > 0 for value in values.values())
        negative = any(value < 0 for value in values.values())
        need(not (positive and negative), f"prescribed face {index} is not supporting")
        if positive:
            normal = tuple(-value for value in normal)
            height = -height
            values = {row_id: -value for row_id, value in values.items()}
        coplanar = {row_id for row_id, value in values.items() if value == 0}
        need(coplanar == set(cycle), f"prescribed maximal face {index} has a changed coplanar set")
        need(all(value < 0 for row_id, value in values.items() if row_id not in coplanar), f"non-strict support at face {index}")
        area = (Q(0), Q(0), Q(0))
        for left, right in zip(cycle, cycle[1:] + cycle[:1]):
            area = add(area, cross(rows[left], rows[right]))
        if dot(area, normal) < 0:
            cycle = [cycle[0], *reversed(cycle[1:])]
        faces.append({"cycle": tuple(cycle), "n": normal, "h": height})
    return faces


def incidence_from_cycles(cycles):
    incidence = defaultdict(list)
    neighbors = defaultdict(set)
    for face_index, cycle in enumerate(cycles):
        for left, right in zip(cycle, cycle[1:] + cycle[:1]):
            edge = tuple(sorted((left, right)))
            incidence[edge].append(face_index)
            neighbors[left].add(right)
            neighbors[right].add(left)
    need(all(len(owners) == 2 for owners in incidence.values()), "nonmanifold prescribed edge ledger")
    return dict(incidence), {key: sorted(value) for key, value in neighbors.items()}


def exact_mass(rows, faces):
    d6 = Q(0)
    m24 = [Q(0), Q(0), Q(0)]
    for face in faces:
        cycle = face["cycle"]
        for offset in range(1, len(cycle) - 1):
            a, b, c = (rows[label] for label in (cycle[0], cycle[offset], cycle[offset + 1]))
            volume6 = det3(a, b, c)
            d6 += volume6
            for axis in range(3):
                m24[axis] += volume6 * (a[axis] + b[axis] + c[axis])
    need(d6 > 0, "non-positive oriented volume")
    return d6 / 6, tuple(value / (4 * d6) for value in m24)


def forced_rails():
    short = [228, *range(229, 247), 8]
    long = [228, *range(247, 265), 8]
    rails = {
        tuple(sorted(edge))
        for route in (short, long)
        for edge in zip(route, route[1:])
    }
    rails.remove((228, 229))
    need(len(rails) == 37, "internal forced-rail definition drift")
    return rails


def mechanics_q(rows, faces):
    volume, centroid = exact_mass(rows, faces)
    incidence, neighbors = incidence_from_cycles([face["cycle"] for face in faces])
    active = sorted(neighbors)
    centered = {row_id: sub(point, centroid) for row_id, point in rows.items()}

    face_components = {}
    stable = []
    face_signs = []
    for face_index, face in enumerate(faces):
        cycle, normal, height = face["cycle"], face["n"], face["h"]
        centered_height = height - dot(normal, centroid)
        need(centered_height > 0, f"centroid outside face {face_index}")
        foot = mul(normal, centered_height / norm2(normal))
        reference = tuple(
            sum((centered[label][axis] for label in cycle), Q(0)) / len(cycle)
            for axis in range(3)
        )
        values = {}
        signs = []
        for left, right in zip(cycle, cycle[1:] + cycle[:1]):
            direction = sub(centered[right], centered[left])
            value = dot(cross(direction, sub(foot, centered[left])), normal)
            ref = dot(cross(direction, sub(reference, centered[left])), normal)
            need(ref != 0 and value != 0, f"zero face mechanics component at face {face_index}")
            if ref < 0:
                value = -value
            edge = tuple(sorted((left, right)))
            values[edge] = value
            signs.append(1 if value > 0 else -1)
        face_components[tuple(sorted(cycle))] = values
        if all(value > 0 for value in values.values()):
            stable.append(face_index)
        face_signs.append((tuple(sorted(cycle)), tuple(signs)))

    vertex_components = {}
    unstable = []
    vertex_signs = []
    for vertex in active:
        values = {
            neighbor: -dot(centered[vertex], sub(centered[neighbor], centered[vertex]))
            for neighbor in neighbors[vertex]
        }
        need(values and all(value != 0 for value in values.values()), f"zero vertex mechanics component at {vertex}")
        vertex_components[vertex] = values
        if all(value > 0 for value in values.values()):
            unstable.append(vertex)
        vertex_signs.append((vertex, tuple((neighbor, 1 if value > 0 else -1) for neighbor, value in values.items())))

    edge_components = {}
    saddles = []
    edge_signs = []
    for edge, owners in sorted(incidence.items()):
        left, right = edge
        direction = sub(centered[right], centered[left])
        dd = norm2(direction)
        need(dd > 0, f"zero edge length at {edge}")
        t = -dot(centered[left], direction) / dd
        foot = add(centered[left], mul(direction, t))
        n1, n2 = faces[owners[0]]["n"], faces[owners[1]]["n"]
        aa, ab, cc = norm2(n1), dot(n1, n2), norm2(n2)
        gram = aa * cc - ab * ab
        need(gram > 0, f"zero edge Gram determinant at {edge}")
        r1, r2 = dot(foot, n1), dot(foot, n2)
        values = {
            "t": t,
            "one_minus_t": Q(1) - t,
            "beta1": (r1 * cc - r2 * ab) / gram,
            "beta2": (r2 * aa - r1 * ab) / gram,
        }
        need(all(value != 0 for value in values.values()), f"zero edge mechanics component at {edge}")
        edge_components[edge] = values
        if all(value > 0 for value in values.values()):
            saddles.append(edge)
        edge_signs.append((edge, tuple((name, 1 if value > 0 else -1) for name, value in values.items())))

    packet = {
        "f_vector": [len(active), len(incidence), len(faces)],
        "class": [len(stable), len(unstable), len(saddles)],
        "active_vertices": active,
        "stable_faces": [list(faces[index]["cycle"]) for index in stable],
        "unstable_vertices": unstable,
        "saddle_edges": [list(edge) for edge in saddles],
    }
    signs = {"faces": face_signs, "vertices": vertex_signs, "edges": edge_signs}
    return {
        "volume": volume,
        "centroid": centroid,
        "incidence": incidence,
        "neighbors": neighbors,
        "active": active,
        "face_components": face_components,
        "vertex_components": vertex_components,
        "edge_components": edge_components,
        "packet": packet,
        "signs": signs,
    }


def centroid_generic(points, faces):
    sample = next(iter(points.values()))[0]
    if isinstance(sample, Jet):
        zero = Jet.constant(0, len(sample.d))
    elif isinstance(sample, Poly):
        zero = Poly.zero()
    else:
        zero = Q(0)
    d6 = zero
    m24 = [zero, zero, zero]
    for face in faces:
        cycle = face["cycle"] if isinstance(face, dict) else face
        for offset in range(1, len(cycle) - 1):
            a, b, c = (points[label] for label in (cycle[0], cycle[offset], cycle[offset + 1]))
            volume6 = det3(a, b, c)
            d6 += volume6
            for axis in range(3):
                m24[axis] += volume6 * (a[axis] + b[axis] + c[axis])
    if isinstance(d6, Jet):
        need(d6.v > 0, "non-positive jet volume")
        centroid = tuple(value / (4 * d6) for value in m24)
    elif isinstance(d6, Poly):
        need(d6.c[0] > 0, "non-positive path start volume")
        centroid = None
    else:
        need(d6 > 0, "non-positive volume")
        centroid = tuple(value / (4 * d6) for value in m24)
    return d6, tuple(m24), centroid


def face_normal_jet(face, points):
    cycle = face["cycle"]
    anchor = points[cycle[0]]
    for left in range(1, len(cycle) - 1):
        for right in range(left + 1, len(cycle)):
            exact = cross(
                sub(tuple(value.v for value in points[cycle[left]]), tuple(value.v for value in anchor)),
                sub(tuple(value.v for value in points[cycle[right]]), tuple(value.v for value in anchor)),
            )
            if exact == (Q(0), Q(0), Q(0)):
                continue
            normal = cross(sub(points[cycle[left]], anchor), sub(points[cycle[right]], anchor))
            if dot(exact, face["n"]) < 0:
                normal = tuple(-value for value in normal)
            return normal
    raise VerificationFailure(f"flat jet face: {cycle}")


def jet_face_components(face, points, centroid):
    cycle = face["cycle"]
    normal = face_normal_jet(face, points)
    height = dot(normal, sub(points[cycle[0]], centroid))
    foot = mul(normal, height / norm2(normal))
    centered = {label: sub(points[label], centroid) for label in cycle}
    dimension = len(points[cycle[0]][0].d)
    reference = tuple(
        sum((centered[label][axis] for label in cycle), Jet.constant(0, dimension)) / len(cycle)
        for axis in range(3)
    )
    out = []
    for left, right in zip(cycle, cycle[1:] + cycle[:1]):
        direction = sub(centered[right], centered[left])
        value = dot(cross(direction, sub(foot, centered[left])), normal)
        ref = dot(
            cross(
                sub(tuple(item.v for item in centered[right]), tuple(item.v for item in centered[left])),
                sub(tuple(item.v for item in reference), tuple(item.v for item in centered[left])),
            ),
            tuple(item.v for item in normal),
        )
        need(ref != 0 and value.v != 0, f"zero jet face component at {(left, right)}")
        if ref < 0:
            value = -value
        out.append(((left, right), value))
    return out


def jet_vertex_component(vertex, neighbor, points, centroid):
    left = sub(points[vertex], centroid)
    right = sub(points[neighbor], centroid)
    return -dot(left, sub(right, left))


def jet_edge_components(edge, owners, faces, points, centroid):
    left, right = edge
    xi, xj = sub(points[left], centroid), sub(points[right], centroid)
    direction = sub(xj, xi)
    t = -dot(xi, direction) / norm2(direction)
    foot = add(xi, mul(direction, t))
    n1, n2 = face_normal_jet(faces[owners[0]], points), face_normal_jet(faces[owners[1]], points)
    aa, ab, cc = norm2(n1), dot(n1, n2), norm2(n2)
    r1, r2 = dot(foot, n1), dot(foot, n2)
    denominator = aa * cc - ab * ab
    need(denominator.v > 0, f"non-positive jet Gram determinant at {edge}")
    return {
        "t": t,
        "one_minus_t": 1 - t,
        "beta1": (r1 * cc - r2 * ab) / denominator,
        "beta2": (r2 * aa - r1 * ab) / denominator,
    }


def build_spec(rows, active):
    def tangent(cycle):
        anchor = rows[cycle[0]]
        first = sub(rows[cycle[1]], anchor)
        need(first != (Q(0), Q(0), Q(0)), f"zero tangent on carrier {cycle}")
        second = None
        for label in cycle[2:]:
            candidate = sub(rows[label], anchor)
            if cross(first, candidate) != (Q(0), Q(0), Q(0)):
                second = candidate
                break
        need(second is not None, f"flat carrier {cycle}")
        normal = cross(first, second)
        need(all(dot(normal, sub(rows[label], anchor)) == 0 for label in cycle), f"nonplanar carrier {cycle}")
        return first, second, normal

    base_u, base_v, base_n = tangent(BASE)
    shell_u, shell_v, shell_n = tangent(SHELL)
    spec = []
    for label in active:
        if label in BASE:
            directions = (("base_u", base_u), ("base_v", base_v))
        elif label in SHELL:
            directions = (("shell_u", shell_u), ("shell_v", shell_v))
        else:
            directions = tuple(
                (axis, tuple(Q(1) if index == offset else Q(0) for index in range(3)))
                for offset, axis in enumerate("xyz")
            )
        for name, direction in directions:
            spec.append((label, f"r{label}_{name}", direction))
    need(len(spec) == 150, f"recomputed chart has {len(spec)} modes")
    need(len({name for _row, name, _direction in spec}) == 150, "duplicate chart mode name")
    return spec, {
        "base_u": base_u,
        "base_v": base_v,
        "base_normal": base_n,
        "shell_u": shell_u,
        "shell_v": shell_v,
        "shell_normal": shell_n,
    }


def make_jets(rows, spec, direction=None):
    dimension = 1 if direction is not None else len(spec)
    by_row = defaultdict(list)
    for column, (row_id, _name, basis) in enumerate(spec):
        by_row[row_id].append((column, basis))
    points = {}
    for row_id, point in rows.items():
        xyz = []
        for axis in range(3):
            derivative = [Q(0)] * dimension
            for column, basis in by_row.get(row_id, []):
                if direction is None:
                    derivative[column] = basis[axis]
                else:
                    derivative[0] += direction[column] * basis[axis]
            xyz.append(Jet(point[axis], tuple(derivative)))
        points[row_id] = tuple(xyz)
    d6, _m24, centroid = centroid_generic(points, []) if False else (None, None, None)
    return points


def displacement_from_coefficients(rows, spec, coefficients):
    need(len(coefficients) == len(spec) == 150, "coefficient count mismatch")
    delta = {row_id: [Q(0), Q(0), Q(0)] for row_id in rows}
    for coefficient, (row_id, _name, direction) in zip(coefficients, spec):
        for axis in range(3):
            delta[row_id][axis] += coefficient * direction[axis]
    return {row_id: tuple(value) for row_id, value in delta.items()}


def raw_ledger(points, cycles):
    d6, m24, _centroid = centroid_generic(points, cycles)
    scale = 4 * d6
    centered_scaled = {
        row_id: tuple(scale * point[axis] - m24[axis] for axis in range(3))
        for row_id, point in points.items()
    }
    incidence, neighbors = incidence_from_cycles(cycles)
    normals = [cycle_normal(cycle, points) for cycle in cycles]
    face = {}
    reference = {}
    for face_index, cycle in enumerate(cycles):
        normal = normals[face_index]
        normal_norm = norm2(normal)
        height = dot(normal, centered_scaled[cycle[0]])
        sample = points[cycle[0]][0]
        zero = Jet.constant(0, len(sample.d)) if isinstance(sample, Jet) else (Poly.zero() if isinstance(sample, Poly) else Q(0))
        center = tuple(
            sum((points[label][axis] for label in cycle), zero) / len(cycle)
            for axis in range(3)
        )
        face_key = tuple(sorted(cycle))
        face[face_key] = {}
        reference[face_key] = {}
        for left, right in zip(cycle, cycle[1:] + cycle[:1]):
            edge_key = tuple(sorted((left, right)))
            direction = sub(points[right], points[left])
            raw = dot(
                cross(direction, sub(mul(normal, height), mul(centered_scaled[left], normal_norm))),
                normal,
            )
            ref = dot(cross(direction, sub(center, points[left])), normal)
            face[face_key][edge_key] = raw
            reference[face_key][edge_key] = ref
    vertex = {
        vertex_id: {
            neighbor: -dot(centered_scaled[vertex_id], sub(points[neighbor], points[vertex_id]))
            for neighbor in neighbors[vertex_id]
        }
        for vertex_id in neighbors
    }
    edge = {}
    for edge_key, owners in incidence.items():
        left, right = edge_key
        direction = sub(points[right], points[left])
        dd = norm2(direction)
        t = -dot(centered_scaled[left], direction)
        n1, n2 = normals[owners[0]], normals[owners[1]]
        aa, ab, cc = norm2(n1), dot(n1, n2), norm2(n2)
        r1, r2 = dot(centered_scaled[left], n1), dot(centered_scaled[left], n2)
        edge[edge_key] = {
            "direction_norm2": dd,
            "gram": aa * cc - ab * ab,
            "t": t,
            "one_minus_t": scale * dd - t,
            "beta1": r1 * cc - r2 * ab,
            "beta2": r2 * aa - r1 * ab,
        }
    return {
        "d6": d6,
        "centered_scaled": centered_scaled,
        "incidence": incidence,
        "neighbors": neighbors,
        "normals": normals,
        "face": face,
        "reference": reference,
        "vertex": vertex,
        "edge": edge,
    }


def support_rows(points, cycles, normals):
    labels = set(points)
    for face_index, cycle in enumerate(cycles):
        anchor = points[cycle[0]]
        normal = normals[face_index]
        for label in cycle[1:]:
            value = dot(normal, sub(points[label], anchor))
            if isinstance(value, Jet):
                need(value.v == 0 and all(item == 0 for item in value.d), f"moving face {face_index} loses affine planarity")
            elif isinstance(value, Poly):
                need(value == Poly.zero(), f"moving face {face_index} loses polynomial planarity")
            else:
                need(value == 0, f"face {face_index} is not planar")
        for witness in sorted(labels - set(cycle)):
            yield face_index, witness, dot(normal, sub(points[witness], anchor))


def raw_primitive_jets(points, cycles):
    ledger = raw_ledger(points, cycles)
    rows = [("volume_d6", ledger["d6"], "mechanics_denominator")]
    support_by_face = defaultdict(list)
    for face_index, witness, value in support_rows(points, cycles, ledger["normals"]):
        support_by_face[face_index].append((witness, value))
    for face_index, cycle in enumerate(cycles):
        for witness, value in support_by_face[face_index]:
            rows.append((f"support:f{face_index}:w{witness}", value, "support"))
        if len(cycle) > 3:
            normal = ledger["normals"][face_index]
            for offset, current in enumerate(cycle):
                previous, following = cycle[offset - 1], cycle[(offset + 1) % len(cycle)]
                turn = dot(
                    cross(sub(points[current], points[previous]), sub(points[following], points[current])),
                    normal,
                )
                rows.append((f"in_face_turn:f{face_index}:v{current}", turn, "in_face_turn"))
    for face_key, values in sorted(ledger["reference"].items()):
        for edge, value in sorted(values.items()):
            rows.append((f"face_reference:{face_key}:{edge}", value, "mechanics_denominator"))
    for face_key, values in sorted(ledger["face"].items()):
        for edge, value in sorted(values.items()):
            rows.append((f"face_raw:{face_key}:{edge}", value, "face_component"))
    for vertex, values in sorted(ledger["vertex"].items()):
        for neighbor, value in sorted(values.items()):
            rows.append((f"vertex:{vertex}:{neighbor}", value, "vertex_component"))
    for edge, values in sorted(ledger["edge"].items()):
        for component in ("direction_norm2", "gram", "t", "one_minus_t", "beta1", "beta2"):
            rows.append((f"edge:{edge}:{component}", values[component], "edge_component"))
    need(len(rows) == 12363, f"raw first-jet count is {len(rows)}")
    need(dict(Counter(family for _name, _value, family in rows)) == {
        "mechanics_denominator": 301,
        "support": 10529,
        "in_face_turn": 33,
        "face_component": 300,
        "vertex_component": 300,
        "edge_component": 900,
    }, "raw first-jet family counts changed")
    return rows


def path_primitives(points, cycles):
    ledger = raw_ledger(points, cycles)
    rows = [("volume_d6", ledger["d6"], "mechanics_denominator")]
    for face_index, witness, value in support_rows(points, cycles, ledger["normals"]):
        rows.append((f"support:f{face_index}:w{witness}", value, "support"))
    for face_index, cycle in enumerate(cycles):
        if len(cycle) <= 3:
            continue
        normal = ledger["normals"][face_index]
        for offset, current in enumerate(cycle):
            previous, following = cycle[offset - 1], cycle[(offset + 1) % len(cycle)]
            turn = dot(
                cross(sub(points[current], points[previous]), sub(points[following], points[current])),
                normal,
            )
            rows.append((f"in_face_turn:f{face_index}:v{current}", turn, "in_face_turn"))
    for face_key, values in sorted(ledger["reference"].items()):
        for edge, value in sorted(values.items()):
            rows.append((f"face_reference:{face_key}:{edge}", value, "mechanics_denominator"))
    for face_key, values in sorted(ledger["face"].items()):
        for edge, value in sorted(values.items()):
            rows.append((f"face_raw:{face_key}:{edge}", value, "face_component"))
    for vertex, values in sorted(ledger["vertex"].items()):
        for neighbor, value in sorted(values.items()):
            rows.append((f"vertex:{vertex}:{neighbor}", value, "vertex_component"))
    for edge, values in sorted(ledger["edge"].items()):
        for component in ("direction_norm2", "gram", "t", "one_minus_t", "beta1", "beta2"):
            rows.append((f"edge:{edge}:{component}", values[component], "edge_component"))
    need(len(rows) == 12363, f"path primitive count is {len(rows)}")
    return rows


def bernstein_coefficients(poly: Poly):
    degree = poly.degree
    return tuple(
        sum(
            (poly.c[index] * Q(math.comb(row, index), math.comb(degree, index)) for index in range(row + 1)),
            Q(0),
        )
        for row in range(degree + 1)
    )


def poly_divmod(dividend: Poly, divisor: Poly):
    need(divisor.c != (Q(0),), "Sturm division by zero polynomial")
    remainder = list(dividend.c)
    quotient = [Q(0)] * max(1, dividend.degree - divisor.degree + 1)
    while len(remainder) - 1 >= divisor.degree and any(remainder):
        shift = len(remainder) - len(divisor.c)
        factor = remainder[-1] / divisor.c[-1]
        quotient[shift] += factor
        for index, value in enumerate(divisor.c):
            remainder[index + shift] -= factor * value
        while len(remainder) > 1 and remainder[-1] == 0:
            remainder.pop()
    return Poly(tuple(quotient)), Poly(tuple(remainder))


def sturm_root_count(poly: Poly, left: Q, right: Q):
    need(poly.eval(left) != 0 and poly.eval(right) != 0, "Sturm interval endpoint is a root")
    sequence = [poly, poly.derivative()]
    if sequence[-1].c == (Q(0),):
        return 0
    while sequence[-1].c != (Q(0),):
        _quotient, remainder = poly_divmod(sequence[-2], sequence[-1])
        if remainder.c == (Q(0),):
            break
        sequence.append(-remainder)

    def variations(value):
        signs = []
        for item in sequence:
            observed = item.eval(value)
            if observed:
                signs.append(1 if observed > 0 else -1)
        return sum(left_sign != right_sign for left_sign, right_sign in zip(signs, signs[1:]))

    return variations(left) - variations(right)


def audit_strict_polynomial(poly: Poly, start_sign: int):
    stack = [(Q(0), Q(1), 0)]
    leaves = 0
    minimum = None
    minimum_interval = None
    minimum_index = None
    while stack:
        left, right, depth = stack.pop()
        normalized = Poly(tuple(start_sign * value for value in poly.affine(left, right).c))
        coefficients = bernstein_coefficients(normalized)
        if all(value > 0 for value in coefficients):
            leaves += 1
            local = min(coefficients)
            if minimum is None or local < minimum:
                minimum = local
                minimum_interval = (left, right)
                minimum_index = coefficients.index(local)
            continue
        if depth < MAX_BERNSTEIN_DEPTH:
            midpoint = (left + right) / 2
            stack.append((midpoint, right, depth + 1))
            stack.append((left, midpoint, depth + 1))
            continue
        # Exact Sturm is a fail-closed fallback, never a numerical tolerance.
        normalized_whole = Poly(tuple(start_sign * value for value in poly.c))
        roots = sturm_root_count(normalized_whole, Q(0), Q(1))
        need(roots == 0 and normalized_whole.eval(0) > 0 and normalized_whole.eval(1) > 0, "Bernstein/Sturm failed to prove strict sign constancy")
        return {
            "strict": True,
            "method": "sturm_fallback",
            "leaves": leaves,
            "minimum": minimum,
            "minimum_interval": minimum_interval,
            "minimum_index": minimum_index,
        }
    return {
        "strict": True,
        "method": "bernstein",
        "leaves": leaves,
        "minimum": minimum,
        "minimum_interval": minimum_interval,
        "minimum_index": minimum_index,
    }


def exhaustive_path_audit(source, candidate, cycles, direction):
    polynomial_points = {
        row_id: tuple(Poly((source[row_id][axis], candidate[row_id][axis] - source[row_id][axis])) for axis in range(3))
        for row_id in source
    }
    scalar_jets = make_jets(source, build_spec(source, sorted(set().union(*map(set, cycles))))[0], direction)
    raw = raw_primitive_jets(scalar_jets, cycles)
    path = path_primitives(polynomial_points, cycles)

    raw_by_key = {}
    for index, (name, value, family) in enumerate(raw):
        key = (name, family)
        need(key not in raw_by_key, f"duplicate raw first-jet key at {index}: {key}")
        need(isinstance(value, Jet) and len(value.d) == 1, f"invalid scalar raw jet at {key}")
        raw_by_key[key] = value

    path_keys = set()
    path_by_key = {}
    family_counts = Counter()
    digest = hashlib.sha256()
    total_leaves = 0
    sturm_fallbacks = 0
    global_minimum = None
    global_owner = None
    for index, (name, poly, family) in enumerate(path):
        need(isinstance(poly, Poly), f"non-polynomial path primitive {name}")
        key = (name, family)
        need(key not in path_keys, f"duplicate path key at {index}: {key}")
        path_keys.add(key)
        path_by_key[key] = poly
        need(key in raw_by_key, f"path primitive absent from raw atlas: {key}")
        jet = raw_by_key.pop(key)
        derivative = poly.c[1] if len(poly.c) > 1 else Q(0)
        need(poly.c[0] == jet.v, f"raw/path source-value mismatch at {key}")
        need(derivative == jet.d[0], f"raw/path derivative mismatch at {key}")
        need(poly.c[0] != 0, f"zero source primitive at {key}")
        sign = 1 if poly.c[0] > 0 else -1
        result = audit_strict_polynomial(poly, sign)
        total_leaves += result["leaves"]
        sturm_fallbacks += result["method"] == "sturm_fallback"
        family_counts[family] += 1
        if result["minimum"] is not None and (global_minimum is None or result["minimum"] < global_minimum):
            global_minimum = result["minimum"]
            global_owner = {
                "index_zero_based": index,
                "name": name,
                "family": family,
                "interval_exact": [qslash(result["minimum_interval"][0]), qslash(result["minimum_interval"][1])],
                "coefficient_index": result["minimum_index"],
            }
        digest.update(f"{name}|{family}|{'|'.join(poly.exact())}\n".encode("utf-8"))
    need(not raw_by_key, f"raw first-jet keys absent from path: {sorted(raw_by_key)[:3]}")
    need(dict(family_counts) == EXPECTED_FAMILIES, f"path family counts changed: {dict(family_counts)}")
    need(digest.hexdigest() == EXPECTED_PATH_DIGEST, "independent path polynomial digest mismatch")
    need(global_minimum is not None and global_minimum > 0, "missing positive path margin")
    return {
        "primitive_count": len(path),
        "family_counts": dict(family_counts),
        "path_primitive_sha256": digest.hexdigest(),
        "unique_raw_path_key_bijection": True,
        "raw_path_value_derivative_correspondence": True,
        "strict_interval_exact": ["0", "1"],
        "all_strict": True,
        "bernstein_leaf_count": total_leaves,
        "sturm_fallback_count": sturm_fallbacks,
        "minimum_normalized_bernstein_coefficient_exact": qcompact(global_minimum),
        "minimum_owner": global_owner,
        "path_by_key": path_by_key,
        "raw_by_order": raw,
    }


def mechanics_records(points, faces, packet):
    _d6, _m24, centroid = centroid_generic(points, faces)
    need(centroid is not None, "jet centroid reconstruction failed")
    incidence, neighbors = incidence_from_cycles([face["cycle"] for face in faces])
    stable = {tuple(sorted(cycle)) for cycle in packet["stable_faces"]}
    unstable = set(packet["unstable_vertices"])
    saddles = {tuple(edge) for edge in packet["saddle_edges"]}
    records = []

    for face in faces:
        face_key = tuple(sorted(face["cycle"]))
        components = [
            (tuple(sorted(edge)), value)
            for edge, value in jet_face_components(face, points, centroid)
        ]
        if face_key in stable:
            selected = components
            present = True
        else:
            negative = [item for item in components if item[1].v < 0]
            need(bool(negative), f"no negative stable-face witness at {face_key}")
            selected = [min(negative, key=lambda item: item[1].v)]
            present = False
        for edge, value in selected:
            records.append({
                "id": ("S", face_key, edge),
                "kind": "present_stable" if present else "absent_stable_witness",
                "value": value,
            })

    for vertex in packet["active_vertices"]:
        components = [
            (neighbor, jet_vertex_component(vertex, neighbor, points, centroid))
            for neighbor in neighbors[vertex]
        ]
        if vertex in unstable:
            selected = components
            present = True
        else:
            negative = [item for item in components if item[1].v < 0]
            need(bool(negative), f"no negative unstable-vertex witness at {vertex}")
            selected = [min(negative, key=lambda item: item[1].v)]
            present = False
        for neighbor, value in selected:
            records.append({
                "id": ("U", vertex, neighbor),
                "kind": "present_unstable" if present else "absent_unstable_witness",
                "value": value,
            })

    for edge, owners in sorted(incidence.items()):
        components = jet_edge_components(edge, owners, faces, points, centroid)
        if edge in saddles:
            selected = list(components.items())
            present = True
        else:
            negative = [(name, value) for name, value in components.items() if value.v < 0]
            need(bool(negative), f"no negative saddle-edge witness at {edge}")
            selected = [min(negative, key=lambda item: item[1].v)]
            present = False
        for component, value in selected:
            records.append({
                "id": ("H", edge, component),
                "kind": "present_saddle" if present else "absent_saddle_witness",
                "value": value,
            })
    need(len(records) == 371, f"mechanics guard atlas has {len(records)} records")
    identifiers = [record["id"] for record in records]
    need(len(set(identifiers)) == len(identifiers), "duplicate mechanics record id")
    need(all(record["value"].v != 0 for record in records), "zero mechanics record")
    return centroid, records


def target_ids():
    return {
        "S228_264_246_via_246_228": ("S", (228, 246, 264), (228, 246)),
        "U228_via_251": ("U", 228, 251),
        "U231_via_232": ("U", 231, 232),
        "U246_via_245": ("U", 246, 245),
        "H8_246_via_t": ("H", (8, 246), "t"),
        "H228_254_via_beta2": ("H", (228, 254), "beta2"),
        "H231_247_via_beta1": ("H", (231, 247), "beta1"),
        "H236_237_via_beta1": ("H", (236, 237), "beta1"),
    }


def support_and_turn_guards(rows, faces, points):
    candidates = []
    all_support_count = 0
    threshold_squared = Q(1, 40_000)
    triples = {}
    for face_index, face in enumerate(faces):
        cycle = face["cycle"]
        anchor = cycle[0]
        triple = None
        for left in range(1, len(cycle) - 1):
            for right in range(left + 1, len(cycle)):
                if cross(sub(rows[cycle[left]], rows[anchor]), sub(rows[cycle[right]], rows[anchor])) != (Q(0), Q(0), Q(0)):
                    triple = (anchor, cycle[left], cycle[right])
                    break
            if triple is not None:
                break
        need(triple is not None, f"flat support-guard face {face_index}")
        triples[face_index] = triple
        normal_squared = norm2(face["n"])
        need(normal_squared > 0, f"zero support normal at {face_index}")
        for witness, point in rows.items():
            if witness in cycle:
                continue
            slack = face["h"] - dot(face["n"], point)
            need(slack > 0, f"non-strict source support at {(face_index, witness)}")
            distance_squared = slack * slack / normal_squared
            candidates.append((distance_squared, face_index, witness))
            all_support_count += 1
    candidates.sort(key=lambda item: item)
    selected = [item for item in candidates if item[0] <= threshold_squared]
    selected = selected[:500] if selected else candidates[:500]
    need(len(selected) == 278, f"exact near-support selection has {len(selected)} rows")

    guards = []
    for distance_squared, face_index, witness in selected:
        anchor, left, right = triples[face_index]
        value = det3(
            sub(points[left], points[anchor]),
            sub(points[right], points[anchor]),
            sub(points[witness], points[anchor]),
        )
        if value.v < 0:
            value = -value
        need(value.v > 0, f"non-positive exact near-support jet at {(face_index, witness)}")
        guards.append({
            "id": ("support", face_index, witness),
            "kind": "near_support",
            "distance_squared": distance_squared,
            "value": value,
        })

    turn_count = 0
    dimension = len(next(iter(points.values()))[0].d)
    for face_index, face in enumerate(faces):
        cycle = face["cycle"]
        if len(cycle) <= 3:
            continue
        normal = tuple(Jet.constant(value, dimension) for value in face["n"])
        for offset, current in enumerate(cycle):
            previous, following = cycle[offset - 1], cycle[(offset + 1) % len(cycle)]
            value = dot(
                cross(sub(points[current], points[previous]), sub(points[following], points[current])),
                normal,
            )
            if value.v < 0:
                value = -value
            need(value.v > 0, f"non-positive turn guard at {(face_index, current)}")
            guards.append({
                "id": ("turn", face_index, current),
                "kind": "in_face_turn",
                "distance_squared": None,
                "value": value,
            })
            turn_count += 1
    need(all_support_count == 10529, f"all-support count is {all_support_count}")
    need(turn_count == 33 and len(guards) == 311, f"turn/guard count drift: {turn_count}/{len(guards)}")
    return guards, {
        "all_support_rows": all_support_count,
        "selected_near_support_rows": len(selected),
        "in_face_turn_rows": turn_count,
        "maximum_selected_distance_squared_exact": qslash(max(item[0] for item in selected)),
    }


@dataclass(frozen=True, slots=True)
class Literal:
    index: int
    name: str
    family: str
    coefficients: tuple[Q, ...]
    tau_coefficient: Q
    rhs: Q

    def directional(self, direction):
        return sum((left * right for left, right in zip(self.coefficients, direction)), Q(0))

    def lhs(self, direction, tau=Q(0)):
        return self.directional(direction) + self.tau_coefficient * tau


def literal_digest(literals):
    digest = hashlib.sha256()
    for row in literals:
        digest.update(
            (
                f"{row.index}|{row.name}|{row.family}|"
                f"{'|'.join(qslash(value) for value in row.coefficients)}|"
                f"{qslash(row.tau_coefficient)}|{qslash(row.rhs)}\n"
            ).encode("utf-8")
        )
    return digest.hexdigest()


def exact_rank(matrix):
    rows = [[Q(value) for value in row] for row in matrix]
    if not rows:
        return 0
    row_count, column_count = len(rows), len(rows[0])
    rank = 0
    for column in range(column_count):
        pivot = next((row for row in range(rank, row_count) if rows[row][column] != 0), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = rows[rank][column]
        rows[rank] = [value / scale for value in rows[rank]]
        for row in range(row_count):
            if row == rank or rows[row][column] == 0:
                continue
            scale = rows[row][column]
            rows[row] = [rows[row][index] - scale * rows[rank][index] for index in range(column_count)]
        rank += 1
        if rank == row_count:
            break
    return rank


def build_literal_contract(rows, faces, packet, spec):
    points = make_jets(rows, spec)
    centroid, mechanics = mechanics_records(points, faces, packet)
    by_id = {record["id"]: record for record in mechanics}
    targets = target_ids()
    need(tuple(targets) == TARGET_NAMES, "target ordering drift")
    need(all(identifier in by_id for identifier in targets.values()), "target mechanics id missing")
    target_jets = {name: by_id[identifier]["value"] for name, identifier in targets.items()}
    need(exact_rank([target_jets[name].d for name in TARGET_NAMES]) == 8, "target gradient rank is not 8")

    base_key = tuple(BASE)
    protected_ids = {
        record["id"]
        for record in mechanics
        if (record["id"][0] == "S" and record["id"][1] == base_key)
        or (record["id"][0] == "U" and record["id"][1] == 8)
    }
    need(len(protected_ids) == 30, f"protected mechanics count is {len(protected_ids)}")
    guards, guard_summary = support_and_turn_guards(rows, faces, points)

    literals = []

    def append(name, family, coefficients, tau_coefficient, rhs):
        literals.append(Literal(
            len(literals), name, family, tuple(Q(value) for value in coefficients), Q(tau_coefficient), Q(rhs)
        ))

    for name, identifier in targets.items():
        value = by_id[identifier]["value"]
        append(f"target:{name}", "target", (item / value.v for item in value.d), 1, 0)
    target_set = set(targets.values())
    for record in mechanics:
        if record["id"] in target_set:
            continue
        value = record["value"]
        if record["id"] in protected_ids:
            append(f"protected:{record['id']!r}", "protected", (-item / value.v for item in value.d), Q(1, 20), 0)
        else:
            sign_value = Q(1) if value.v > 0 else Q(-1)
            append(f"mechanics:{record['id']!r}", "mechanics_guard", (-sign_value * item for item in value.d), 0, abs(value.v) / 5)
    for record in guards:
        value = record["value"]
        append(f"{record['kind']}:{record['id']!r}", record["kind"], (-item for item in value.d), 0, value.v / 5)

    active = tuple(packet["active_vertices"])
    row_index = {row_id: offset for offset, row_id in enumerate(active)}
    physical = [[Q(0)] * len(spec) for _ in range(3 * len(active))]
    physical_names = []
    for row_id in active:
        physical_names.extend((f"r{row_id}_x", f"r{row_id}_y", f"r{row_id}_z"))
    for column, (row_id, _name, direction) in enumerate(spec):
        offset = row_index[row_id]
        for axis in range(3):
            physical[3 * offset + axis][column] = direction[axis]
    for name, coefficients in zip(physical_names, physical):
        append(f"physical_plus:{name}", "physical_plus", coefficients, 0, TRUST)
    for name, coefficients in zip(physical_names, physical):
        append(f"physical_minus:{name}", "physical_minus", (-value for value in coefficients), 0, TRUST)

    counts = dict(Counter(row.family for row in literals))
    need(counts == EXPECTED_LITERAL_FAMILIES, f"literal family counts changed: {counts}")
    need(len(literals) == 1048, f"literal count is {len(literals)}")
    need(all(len(row.coefficients) == 150 for row in literals), "literal width is not 150")
    digest = literal_digest(literals)
    need(digest == EXPECTED_LITERAL_DIGEST, f"independent literal digest mismatch: {digest}")
    return {
        "literals": literals,
        "digest": digest,
        "family_counts": counts,
        "mechanics": mechanics,
        "mechanics_by_id": by_id,
        "target_ids": targets,
        "protected_ids": protected_ids,
        "guard_summary": guard_summary,
        "centroid": centroid,
    }


EXPECTED_OWNER_CODE = {
    "M42_acute_bridge_fifth_cell_work/fourth_cell_endpoint/numeric_hull_proposer.py": ("numeric_hull_proposer", 8454, "35aba4a57d01f5313704476c631bf550dc6fb4718c562ffa9891489a37a1d4e4"),
    "tracks/piecewise_transfer/rank5_exact_reconstruction.py": ("rank5_exact_reconstruction", 9853, "86016a9ce94feb4e24d641b78d4ea46232a6a0ce355af7e2fb8c58df3af19a4d"),
    "tracks/piecewise_transfer/rank5_exact_jacobian.py": ("rank5_exact_jacobian", 16244, "87bf6343c31c79f2b162b1b159c63fc086f7f4dbf2da42fb3ba70dff773b27d9"),
    "tracks/piecewise_transfer/rank5_search.py": ("rank5_search", 8527, "4c224f0e009cc0a6a9ce68620a7798f1cf31c5994994b75543a3ba91ada30844"),
    "tracks/piecewise_transfer/rank5_sixth_control.py": ("rank5_sixth_control", 21445, "f66c380dc97cefc91d029566cb0533777ab24ec7cc56c7faa86d60eab9a84f2b"),
    "tracks/piecewise_transfer/rank5_circuit_escape.py": ("rank5_circuit_escape", 34384, "22061ee4426e59d39faf8eb4d668aaa6205125dca10d77785254b5ef965aaec5"),
    "tracks/piecewise_transfer/rank5_circuit_escape_continuation.py": ("rank5_circuit_escape_continuation", 27713, "a3f840d2913322de529957f3078e54004ec542fe5a9cf51a6be1614471a3bf14"),
    "tracks/piecewise_transfer/post_c17_attack/post_c17_exact.py": ("post_c17_exact", 31496, "799fcf1fc024cf928ca7426b814f351729bc5be8a255be7aca08c1e88671604b"),
    "tracks/piecewise_transfer/post_c17_attack/recovery2/main/build_full_chart.py": ("build_full_chart", 10411, "b1c5cc929168d35791e387c9ed8d2fd0cc2e5ece87b1069a7e5e7f307644f481"),
    "tracks/piecewise_transfer/post_c17_attack/recovery2/main/propose_fixed_plane_descent.py": ("propose_fixed_plane_descent", 18415, "6ca2bab0e2717def0b3ff5c4a2bda33265df9862a2a03acfa34e3a3377105968"),
    "tracks/piecewise_transfer/post_c17_attack/recovery2/transfer_search/build_first_jet_atlas.py": ("build_first_jet_atlas", 28598, "4dc51083c71149db251ad5885712546ea8539b0c7d7ea5c6910ae4d732ba2d1f"),
    "tracks/global_carrier_support/rigorous_local_bypass/exact_core.py": ("exact_core", 37641, "d2d69ce6e4ddefd2ab7171b7e61bd09ae12846eaf509f61dd25be6d9bbb235dd"),
    "tracks/piecewise_transfer/post_c17_attack/recovery2/main/locate_first_event.py": ("post_c17_f21_exact_interior_locator", 10180, "d7a1b7d645904c25cb075e3f08ebe3d4e086984c1ecb75f0111825041fe43e63"),
}


def expected_owner_snapshot():
    return {
        path: {"module": module, "bytes": size, "sha256": sha256, "snapshot_reads": 1}
        for path, (module, size, sha256) in EXPECTED_OWNER_CODE.items()
    }


def validate_artifact_schemas(frozen):
    certificate = strict_json(frozen["f20_certificate"].data, "F20 certificate")
    verification = strict_json(frozen["f20_verification"].data, "F20 verification")
    chart = strict_json(frozen["chart"].data, "F21 chart")
    faces_payload = strict_json(frozen["f20_faces"].data, "F20 faces")
    proposal = strict_json(frozen["proposal"].data, "F21 proposal")
    receipt = strict_json(frozen["receipt"].data, "F21 receipt")
    scan = strict_json(frozen["scan"].data, "F21 locator scan")

    exact_keys(certificate, (
        "version", "type", "scope", "source_hashes", "path", "event",
        "open_intervals", "rational_parameters", "rational_checkpoints",
        "directed_residuals", "generated_file_sha256", "verdict",
        "winner_status", "next_action",
    ), "F20 certificate")
    need(certificate["version"] == 1, "unsupported F20 certificate version")
    need(certificate["scope"] == "All 12,363 support/in-face/own-centroid primitives in both strict cells, algebraic event family and exact checkpoints.", "unexpected F20 certificate scope")
    need(certificate["verdict"] == "EXACT_POST_C17_TWENTIETH_SAFE_FLIP_PASS", "F20 certificate verdict mismatch")
    need(certificate["winner_status"] == "NONWINNER", "F20 certificate winner status mismatch")
    generated = certificate["generated_file_sha256"]
    need(generated.get("recovery2/main/post_transfer_round15/far.csv") == SOURCE_HASHES["recovery2/main/post_transfer_round15/far.csv"], "F20 certificate does not bind far.csv")
    need(generated.get("recovery2/main/post_transfer_round15/post_faces.json") == SOURCE_HASHES["recovery2/main/post_transfer_round15/post_faces.json"], "F20 certificate does not bind post_faces.json")
    far_checkpoint = certificate.get("rational_checkpoints", {}).get("far", {})
    need(far_checkpoint.get("exact_support", {}).get("f_vector") == EXPECTED_F_VECTOR, "F20 support checkpoint f-vector mismatch")
    need(far_checkpoint.get("exact_support", {}).get("strict_support_count") == 10529, "F20 support checkpoint count mismatch")
    need(far_checkpoint.get("exact_mechanics", {}).get("class") == EXPECTED_CLASS, "F20 mechanics checkpoint class mismatch")
    need(far_checkpoint.get("exact_mechanics", {}).get("unstable_vertices") == EXPECTED_UNSTABLE, "F20 unstable checkpoint mismatch")
    need(far_checkpoint.get("exact_mechanics", {}).get("saddle_edges") == EXPECTED_SADDLES, "F20 saddle checkpoint mismatch")
    need(far_checkpoint.get("forced_rail_count") == 37 and far_checkpoint.get("missing_forced_rails") == [], "F20 forced-rail checkpoint mismatch")

    exact_keys(verification, (
        "version", "scope", "certificate_sha256", "primitive_count_each_strict_cell",
        "event_multiplicities", "checkpoints", "target_ratios_exact", "verdict", "winner_status",
    ), "F20 verification")
    need(verification["version"] == 1, "unsupported F20 verification version")
    need(verification["scope"] == "clean reconstruction of exact post-C17 fixed-plane safe flip", "unexpected F20 verification scope")
    need(verification["certificate_sha256"] == SOURCE_HASHES["recovery2/main/post_transfer_round15/certificate.json"], "F20 verification certificate hash mismatch")
    need(verification["primitive_count_each_strict_cell"] == 12363, "F20 verification primitive count mismatch")
    need(verification["verdict"] == "INDEPENDENT_EXACT_POST_C17_TWENTIETH_SAFE_FLIP_PASS", "F20 independent verdict mismatch")
    need(verification["winner_status"] == "NONWINNER", "F20 verification winner status mismatch")

    exact_keys(chart, (
        "version", "scope", "source_hashes", "f_vector", "class", "mode_count",
        "target_rank_exact", "protected_component_count", "mode_names", "basis_exact",
        "source_volume_exact", "source_centroid_exact", "verdict",
    ), "F21 chart")
    need(chart["version"] == 1 and chart["scope"] == "fresh exact fixed-plane chart in post-safe-flip cell", "unsupported F21 chart")
    need(chart["source_hashes"] == {
        "recovery2/main/post_transfer_round15/far.csv": SOURCE_HASHES["recovery2/main/post_transfer_round15/far.csv"],
        "recovery2/main/post_transfer_round15/post_faces.json": SOURCE_HASHES["recovery2/main/post_transfer_round15/post_faces.json"],
        "recovery2/main/post_transfer_round15/certificate.json": SOURCE_HASHES["recovery2/main/post_transfer_round15/certificate.json"],
    }, "F21 chart lineage mismatch")
    need(chart["f_vector"] == EXPECTED_F_VECTOR and chart["class"] == EXPECTED_CLASS, "F21 chart mechanics dimensions mismatch")
    need(chart["mode_count"] == 150 and chart["target_rank_exact"] == 8 and chart["protected_component_count"] == 30, "F21 chart rank/count mismatch")
    need(chart["verdict"] == "EXACT_POST_SAFE_FLIP_FIXED_PLANE_CHART_PASS", "F21 chart verdict mismatch")

    proposal_keys = (
        "version", "scope", "stage", "parent_stage", "source_hashes", "source_bytes",
        "owner_code_snapshot", "chart_sha256", "chart_bytes", "source_certificate_verdict",
        "source_verification_verdict", "chart_verdict", "mode_count", "mode_names",
        "complete_raw_first_jet_primitive_count", "complete_raw_first_jet_family_counts",
        "complete_raw_first_jet_sha256", "mechanics_guard_count", "support_guard_summary",
        "literal_constraint_count", "literal_constraint_family_counts", "literal_matrix_sha256",
        "expected_literal_matrix_sha256", "branches", "selected_branch", "selection_policy",
        "exact_coefficients", "exact_common_fractional_descent", "exact_interior_certificate",
        "exhaustive_same_cell_segment", "locator_contract", "candidate", "verdict",
        "exact_interior_verdict", "proof_status", "winner_status",
    )
    exact_keys(proposal, proposal_keys, "F21 proposal")
    need(proposal["version"] == 1 and proposal["stage"] == "F21" and proposal["parent_stage"] == "F20", "unsupported proposal stage/version")
    need(proposal["scope"] == "strict rational exact-interior F21 proposal in the accepted F20 post-transfer cell", "unexpected proposal scope")
    need(proposal["source_hashes"] == SOURCE_HASHES, "proposal F20 lineage mismatch")
    need(proposal["source_bytes"] == {
        "recovery2/main/post_transfer_round15/far.csv": 82321,
        "recovery2/main/post_transfer_round15/post_faces.json": 3283,
        "recovery2/main/post_transfer_round15/certificate.json": 121428,
        "recovery2/main/post_transfer_round15/verification.json": 86818,
    }, "proposal lineage byte counts mismatch")
    need(proposal["owner_code_snapshot"] == expected_owner_snapshot(), "proposal owner-code snapshot mismatch")
    need(proposal["chart_sha256"] == EXPECTED_INPUTS["chart"][2] and proposal["chart_bytes"] == EXPECTED_INPUTS["chart"][1], "proposal chart binding mismatch")
    need(proposal["source_certificate_verdict"] == certificate["verdict"], "proposal source certificate verdict mismatch")
    need(proposal["source_verification_verdict"] == verification["verdict"], "proposal source verification verdict mismatch")
    need(proposal["chart_verdict"] == chart["verdict"], "proposal chart verdict mismatch")
    need(proposal["mode_count"] == 150 and proposal["mode_names"] == chart["mode_names"], "proposal chart-mode binding mismatch")
    need(proposal["complete_raw_first_jet_primitive_count"] == 12363, "proposal raw primitive count mismatch")
    need(proposal["complete_raw_first_jet_family_counts"] == {
        "edge_component": 900, "face_component": 300, "in_face_turn": 33,
        "mechanics_denominator": 301, "support": 10529, "vertex_component": 300,
    }, "proposal raw family counts mismatch")
    need(proposal["mechanics_guard_count"] == 371, "proposal mechanics guard count mismatch")
    need(proposal["literal_constraint_count"] == 1048 and proposal["literal_constraint_family_counts"] == EXPECTED_LITERAL_FAMILIES, "proposal literal counts mismatch")
    need(proposal["literal_matrix_sha256"] == EXPECTED_LITERAL_DIGEST and proposal["expected_literal_matrix_sha256"] == EXPECTED_LITERAL_DIGEST, "proposal literal digest mismatch")
    need(isinstance(proposal["branches"], list) and len(proposal["branches"]) == 8, "proposal trust branch schema mismatch")
    expected_trusts = [Q(value) for value in ("1e-8", "3e-8", "1e-7", "3e-7", "1e-6", "3e-6", "1e-5", "3e-5")]
    need([Q(row.get("trust_exact")) for row in proposal["branches"]] == expected_trusts, "proposal trust branch sequence mismatch")
    selected = proposal["selected_branch"]
    need(Q(selected.get("trust_exact")) == TRUST and selected.get("literal_matrix_sha256") == EXPECTED_LITERAL_DIGEST, "selected trust branch mismatch")
    transform = selected.get("numerical_transform", {})
    need(transform.get("kind") == "positive diagonal row equilibration only" and transform.get("reversible") is True, "unsupported solver-side transform")
    need(transform.get("original_exact_matrix_retained_for_readback") is True and transform.get("column_equilibration_used") is False, "solver transform is not row-scaling-only")
    need(proposal["selection_policy"] == "exactly the diagnosed trust=1e-5 branch; no fallback branch selection", "proposal selection policy mismatch")
    need(len(proposal["exact_coefficients"]) == 150, "proposal coefficient count mismatch")
    need(proposal["verdict"] == "RATIONAL_POST_SAFE_FLIP_DESCENT_PROPOSAL_PASS", "proposal verdict mismatch")
    need(proposal["exact_interior_verdict"] == "EXACT_POST_C17_F21_INTERIOR_PROPOSAL_PASS", "proposal exact-interior verdict mismatch")
    need(proposal["proof_status"] == "EXACT_STRICT_INTERIOR_ENDPOINT_AND_PRE_EVENT_SEGMENT_ONLY_FIRST_EVENT_NOT_YET_CERTIFIED", "proposal proof boundary mismatch")
    need(proposal["winner_status"] == "NONWINNER_PROPOSAL_ONLY", "proposal winner status mismatch")

    exact_keys(receipt, ("version", "scope", "status", "verdict", "lineage", "owner_code_snapshot", "outputs", "strict_margin_summary", "claim_boundary"), "F21 receipt")
    need(receipt["version"] == 1 and receipt["scope"] == "bounded F21 exact-interior proposer receipt", "unsupported receipt schema")
    need(receipt["status"] == "PASS" and receipt["verdict"] == proposal["exact_interior_verdict"], "receipt verdict mismatch")
    expected_lineage = {
        **{key: {"bytes": proposal["source_bytes"][key], "sha256": value, "snapshot_reads": 1} for key, value in SOURCE_HASHES.items()},
        "recovery2/main/post_transfer_round16/chart.json": {"bytes": 28897, "sha256": EXPECTED_INPUTS["chart"][2], "snapshot_reads": 1},
    }
    need(receipt["lineage"] == expected_lineage, "receipt lineage mismatch")
    need(receipt["owner_code_snapshot"] == expected_owner_snapshot(), "receipt owner-code snapshot mismatch")
    need(receipt["outputs"] == {
        "recovery2/main/post_transfer_round16/exact_interior_candidate.csv": {"bytes": 343273, "sha256": EXPECTED_INPUTS["candidate"][2]},
        "recovery2/main/post_transfer_round16/exact_interior_proposal.json": {"bytes": 1160861, "sha256": EXPECTED_INPUTS["proposal"][2]},
    }, "receipt output hashes mismatch")

    exact_keys(scan, (
        "version", "scope", "source_hashes", "primitive_count", "family_counts",
        "horizon_audits", "search_horizon", "candidate_count", "first_candidate",
        "overlapping_first_candidates", "next_candidates", "verdict", "proof_status",
    ), "F21 locator scan")
    need(scan["version"] == 1 and scan["scope"] == "exact-Bernstein exhaustive first-event locator on post-C17 fixed-plane ray", "unsupported locator scan schema")
    need(scan["source_hashes"] == {
        "recovery2/main/post_transfer_round15/far.csv": EXPECTED_INPUTS["f20_far"][2],
        "recovery2/main/post_transfer_round16/exact_interior_candidate.csv": EXPECTED_INPUTS["candidate"][2],
        "recovery2/main/post_transfer_round16/exact_interior_proposal.json": EXPECTED_INPUTS["proposal"][2],
        "recovery2/main/post_transfer_round15/post_faces.json": EXPECTED_INPUTS["f20_faces"][2],
    }, "stale locator source hashes")
    need(scan["primitive_count"] == 12363 and scan["family_counts"] == EXPECTED_FAMILIES, "locator primitive ledger mismatch")
    need(scan["verdict"] == "EXHAUSTIVE_EXACT_POST_C17_FIXED_PLANE_FIRST_EVENT_LOCATOR_PASS", "locator verdict mismatch")
    need(scan["proof_status"] == "LOCATOR_ONLY_EVENT_CELL_CERTIFICATE_REQUIRED", "locator claim boundary mismatch")

    return {
        "certificate": certificate,
        "verification": verification,
        "chart": chart,
        "faces_payload": faces_payload,
        "proposal": proposal,
        "receipt": receipt,
        "scan": scan,
    }


def mechanics_value_by_id(mechanics, identifier):
    kind = identifier[0]
    if kind == "S":
        return mechanics["face_components"][identifier[1]][identifier[2]]
    if kind == "U":
        return mechanics["vertex_components"][identifier[1]][identifier[2]]
    if kind == "H":
        return mechanics["edge_components"][identifier[1]][identifier[2]]
    raise VerificationFailure(f"unsupported mechanics id {identifier!r}")


def validate_geometry(source, candidate, cycles, chart, proposal):
    source_faces = exactify_faces(source, cycles)
    candidate_faces = exactify_faces(candidate, cycles)
    source_mechanics = mechanics_q(source, source_faces)
    candidate_mechanics = mechanics_q(candidate, candidate_faces)
    expected_packet = {
        "f_vector": EXPECTED_F_VECTOR,
        "class": EXPECTED_CLASS,
        "active_vertices": source_mechanics["packet"]["active_vertices"],
        "stable_faces": [[228, 264, 246], list(BASE)],
        "unstable_vertices": EXPECTED_UNSTABLE,
        "saddle_edges": EXPECTED_SADDLES,
    }
    need(source_mechanics["packet"] == expected_packet, f"independent F20 mechanics packet mismatch: {source_mechanics['packet']}")
    need(candidate_mechanics["packet"] == expected_packet, f"candidate mechanics packet mismatch: {candidate_mechanics['packet']}")
    need(set(source_mechanics["incidence"]) == set(candidate_mechanics["incidence"]), "candidate true-edge ledger changed")
    need(source_mechanics["signs"] == candidate_mechanics["signs"], "candidate mechanics sign cell changed")
    rails = forced_rails()
    need(not (rails - set(source_mechanics["incidence"])), "F20 source is missing a forced rail")
    need(not (rails - set(candidate_mechanics["incidence"])), "candidate is missing a forced rail")

    for carrier in (BASE, SHELL):
        source_face = next((face for face in source_faces if set(face["cycle"]) == set(carrier)), None)
        candidate_face = next((face for face in candidate_faces if set(face["cycle"]) == set(carrier)), None)
        need(source_face is not None and candidate_face is not None, f"carrier face missing: {carrier}")
        need(all(dot(source_face["n"], candidate[label]) == source_face["h"] for label in carrier), f"candidate left frozen carrier plane: {carrier}")

    need(chart["source_volume_exact"] == qslash(source_mechanics["volume"]), "chart source volume mismatch")
    need(chart["source_centroid_exact"] == [qslash(value) for value in source_mechanics["centroid"]], "chart source centroid mismatch")
    candidate_record = proposal["candidate"]
    need(candidate_record.get("csv") == "recovery2/main/post_transfer_round16/exact_interior_candidate.csv", "proposal candidate path mismatch")
    need(candidate_record.get("csv_sha256") == EXPECTED_INPUTS["candidate"][2] and candidate_record.get("csv_bytes") == EXPECTED_INPUTS["candidate"][1], "proposal candidate byte binding mismatch")
    need(candidate_record.get("f_vector") == EXPECTED_F_VECTOR and candidate_record.get("class") == EXPECTED_CLASS, "proposal candidate dimensions mismatch")
    need(candidate_record.get("stable_faces") == expected_packet["stable_faces"], "proposal stable-face ledger mismatch")
    need(candidate_record.get("unstable_vertices") == EXPECTED_UNSTABLE and candidate_record.get("saddle_edges") == EXPECTED_SADDLES, "proposal candidate mechanics ledger mismatch")
    need(candidate_record.get("same_exact_face_edge_combinatorics_and_mechanics_sign_cell") is True, "proposal does not claim same mechanics sign cell")
    need(candidate_record.get("all_37_forced_rails_present") is True, "proposal forced-rail claim missing")
    need(candidate_record.get("volume_exact") == qslash(candidate_mechanics["volume"]), "proposal candidate volume mismatch")
    need(candidate_record.get("centroid_exact") == [qslash(value) for value in candidate_mechanics["centroid"]], "proposal candidate centroid mismatch")
    return source_faces, candidate_faces, source_mechanics, candidate_mechanics


def validate_chart_reconstruction(source, mechanics, chart):
    spec, basis = build_spec(source, mechanics["active"])
    mode_names = [name for _row, name, _direction in spec]
    need(chart["mode_names"] == mode_names, "independent chart mode names mismatch")
    need(chart["basis_exact"] == {
        name: [qslash(value) for value in vector]
        for name, vector in basis.items()
    }, "independent exact chart basis mismatch")
    return spec


def validate_candidate_bytes(source, candidate_from_file, spec, proposal, frozen_candidate):
    coefficients = tuple(Q(value) for value in proposal["exact_coefficients"])
    delta = displacement_from_coefficients(source, spec, coefficients)
    reconstructed = {
        row_id: add(point, delta[row_id])
        for row_id, point in source.items()
    }
    need(reconstructed == candidate_from_file, "candidate exact coordinates do not equal source plus exact chart coefficients")
    rebuilt_bytes = candidate_csv_bytes(reconstructed)
    need(rebuilt_bytes == frozen_candidate.data, "candidate full-byte canonical reconstruction mismatch")
    physical_linf = max(abs(value) for displacement in delta.values() for value in displacement)
    need(physical_linf < TRUST, "candidate displacement is outside strict trust box")
    need(proposal["candidate"].get("physical_linf_exact") == qslash(physical_linf), "proposal physical L-infinity value mismatch")
    return coefficients, delta, physical_linf


def validate_derivatives_and_endpoint(
    source, candidate, source_faces, candidate_faces, source_mechanics,
    candidate_mechanics, spec, direction, literal_contract, proposal,
):
    scalar_points = make_jets(source, spec, direction)
    _centroid, records = mechanics_records(scalar_points, source_faces, source_mechanics["packet"])
    by_id = {record["id"]: record["value"] for record in records}
    target_map = target_ids()
    target_records = []
    for name, identifier in target_map.items():
        value = by_id[identifier]
        derivative = value.d[0]
        need(derivative < 0, f"target derivative is not negative: {name}")
        target_records.append({
            "name": name,
            "source_value_exact": qslash(value.v),
            "derivative_exact": qslash(derivative),
            "fractional_derivative_exact": qslash(derivative / value.v),
        })
    need(len({row["name"] for row in target_records}) == 8, "duplicate target derivative key")

    protected_records = []
    for record in records:
        if record["id"] not in literal_contract["protected_ids"]:
            continue
        value = record["value"]
        derivative = value.d[0]
        need(derivative > 0, f"protected derivative is not positive: {record['id']!r}")
        protected_records.append({
            "name": repr(record["id"]),
            "source_value_exact": qslash(value.v),
            "derivative_exact": qslash(derivative),
            "normalized_derivative_exact": qslash(derivative / value.v),
        })
    need(len(protected_records) == 30 and len({row["name"] for row in protected_records}) == 30, "protected derivative key/count mismatch")

    serialized_targets = proposal["exact_interior_certificate"].get("target_derivatives")
    serialized_protected = proposal["exact_interior_certificate"].get("protected_derivatives")
    need(isinstance(serialized_targets, list) and len(serialized_targets) == 8, "serialized target derivative schema mismatch")
    need(isinstance(serialized_protected, list) and len(serialized_protected) == 30, "serialized protected derivative schema mismatch")
    need(len({row.get("name") for row in serialized_targets}) == 8, "duplicate serialized target derivative key")
    need(len({row.get("name") for row in serialized_protected}) == 30, "duplicate serialized protected derivative key")
    for independent, serialized in zip(target_records, serialized_targets):
        need(serialized.get("name") == independent["name"], "serialized target derivative order/key mismatch")
        need(serialized.get("derivative_exact") == independent["derivative_exact"], f"serialized target derivative mismatch: {independent['name']}")
        need(serialized.get("fractional_derivative_exact") == independent["fractional_derivative_exact"], f"serialized target fractional derivative mismatch: {independent['name']}")
    for independent, serialized in zip(protected_records, serialized_protected):
        need(serialized.get("name") == independent["name"], "serialized protected derivative order/key mismatch")
        need(serialized.get("derivative_exact") == independent["derivative_exact"], f"serialized protected derivative mismatch: {independent['name']}")
        need(serialized.get("normalized_derivative_exact") == independent["normalized_derivative_exact"], f"serialized protected normalized derivative mismatch: {independent['name']}")

    target_ratios = {}
    for name, identifier in target_map.items():
        source_value = mechanics_value_by_id(source_mechanics, identifier)
        candidate_value = mechanics_value_by_id(candidate_mechanics, identifier)
        ratio = candidate_value / source_value
        need(Q(0) < ratio < Q(1), f"target endpoint ratio is not strictly inside (0,1): {name}")
        target_ratios[name] = ratio
    need(proposal["candidate"].get("target_ratios_exact") == {name: qslash(value) for name, value in target_ratios.items()}, "proposal target endpoint ratios mismatch")

    protected_differences = {}
    for identifier in literal_contract["protected_ids"]:
        source_value = mechanics_value_by_id(source_mechanics, identifier)
        candidate_value = mechanics_value_by_id(candidate_mechanics, identifier)
        difference = candidate_value - source_value
        need(difference > 0, f"protected endpoint component did not strictly increase: {identifier!r}")
        protected_differences[repr(identifier)] = difference
    need(len(protected_differences) == 30, "protected endpoint difference count mismatch")
    minimum_difference = min(protected_differences.values())
    need(proposal["candidate"].get("protected_component_count") == 30, "proposal protected endpoint count mismatch")
    need(proposal["candidate"].get("protected_components_increased_strictly_exactly") is True, "proposal protected endpoint claim mismatch")
    need(proposal["candidate"].get("minimum_protected_endpoint_increase_exact") == qslash(minimum_difference), "proposal minimum protected endpoint increase mismatch")
    return {
        "target_records": target_records,
        "protected_records": protected_records,
        "target_ratios": {name: qslash(value) for name, value in target_ratios.items()},
        "minimum_protected_endpoint_increase_exact": qslash(minimum_difference),
    }


def validate_literal_strictness(literal_contract, direction, path_audit, proposal):
    certificate = proposal["exact_interior_certificate"]
    tau = Q(certificate.get("exact_tau"))
    need(qslash(tau) == proposal["exact_common_fractional_descent"], "proposal tau/common-descent mismatch")
    slacks = []
    for row in literal_contract["literals"]:
        slack = row.rhs - row.lhs(direction, tau)
        need(slack > 0, f"literal row is not strict: {row.index} {row.name}")
        slacks.append((slack, row))
    minimum_slack, minimum_owner = min(slacks, key=lambda item: item[0])
    need(certificate.get("literal_constraint_count") == 1048, "serialized strict literal count mismatch")
    need(certificate.get("all_literal_slacks_strictly_positive") is True, "serialized strict literal claim mismatch")
    need(certificate.get("global_minimum_literal_slack_exact") == qslash(minimum_slack), "serialized minimum literal slack mismatch")
    need(certificate.get("global_minimum_literal_owner_index_zero_based") == minimum_owner.index, "serialized minimum literal owner index mismatch")
    need(certificate.get("global_minimum_literal_owner_name") == minimum_owner.name, "serialized minimum literal owner name mismatch")

    family_margins = {}
    for family in sorted(EXPECTED_LITERAL_FAMILIES):
        rows = [(slack, row) for slack, row in slacks if row.family == family]
        minimum, owner = min(rows, key=lambda item: item[0])
        family_margins[family] = {
            "count": len(rows),
            "minimum_slack_exact": qslash(minimum),
            "minimum_owner_index_zero_based": owner.index,
            "minimum_owner_name": owner.name,
        }
    serialized_margins = certificate.get("literal_family_margins", {})
    need(set(serialized_margins) == set(family_margins), "serialized literal margin families mismatch")
    for family, independent in family_margins.items():
        serialized = serialized_margins[family]
        for key, value in independent.items():
            need(serialized.get(key) == value, f"serialized {family} literal margin mismatch at {key}")

    shrink = Q(certificate.get("analytic_shrink_exact"))
    need(shrink > 0, "non-positive serialized analytic shrink")
    raw_direction = tuple(value / shrink for value in direction)
    literal_cap = Q(1)
    literal_owner = None
    for row in literal_contract["literals"]:
        if row.tau_coefficient != 0:
            continue
        lhs = row.directional(raw_direction)
        if lhs > 0:
            cap = row.rhs / lhs
            if cap < literal_cap:
                literal_cap, literal_owner = cap, row

    raw_cap = Q(1)
    raw_owner = None
    raw_linear_minimum = None
    raw_linear_owner = None
    for name, value, family in path_audit["raw_by_order"]:
        raw_derivative = value.d[0] / shrink
        signed_derivative = raw_derivative if value.v > 0 else -raw_derivative
        if signed_derivative < 0:
            cap = abs(value.v) / (-signed_derivative)
            if cap < raw_cap:
                raw_cap, raw_owner = cap, (name, family, value.v, raw_derivative)
        signed_linear = (value.v + value.d[0]) if value.v > 0 else -(value.v + value.d[0])
        need(signed_linear > 0, f"raw linearized endpoint is non-strict: {(name, family)}")
        if raw_linear_minimum is None or signed_linear < raw_linear_minimum:
            raw_linear_minimum, raw_linear_owner = signed_linear, (name, family)
    recomputed_shrink = min(Q(1), literal_cap, raw_cap) / 2
    need(shrink == recomputed_shrink, "analytic shrink algebra mismatch")

    homogeneous = [row for row in literal_contract["literals"] if row.tau_coefficient > 0]
    need(len(homogeneous) == 38, "homogeneous literal row count mismatch")
    tau_cap = Q(1)
    tau_owner = None
    for row in homogeneous:
        directional = row.directional(direction)
        need(directional < 0, f"homogeneous direction is not strict: {row.name}")
        cap = -directional / row.tau_coefficient
        if cap < tau_cap:
            tau_cap, tau_owner = cap, row
    need(tau == min(Q(1), tau_cap) / 2, "exact tau shrink algebra mismatch")

    need(certificate.get("literal_positive_scale_cap_exact") == qslash(literal_cap), "serialized literal scale cap mismatch")
    expected_literal_owner = None if literal_owner is None else {"index_zero_based": literal_owner.index, "name": literal_owner.name}
    need(certificate.get("literal_scale_cap_owner") == expected_literal_owner, "serialized literal cap owner mismatch")
    need(certificate.get("raw_12363_first_jet_scale_cap_exact") == qslash(raw_cap), "serialized raw scale cap mismatch")
    expected_raw_owner = None if raw_owner is None else {
        "name": raw_owner[0], "family": raw_owner[1],
        "source_value_exact": qslash(raw_owner[2]),
        "raw_directional_derivative_exact": qslash(raw_owner[3]),
    }
    need(certificate.get("raw_scale_cap_owner") == expected_raw_owner, "serialized raw cap owner mismatch")
    need(certificate.get("exact_tau_cap") == qslash(tau_cap), "serialized tau cap mismatch")
    expected_tau_owner = None if tau_owner is None else {"index_zero_based": tau_owner.index, "name": tau_owner.name}
    need(certificate.get("tau_cap_owner") == expected_tau_owner, "serialized tau cap owner mismatch")
    need(certificate.get("raw_linearized_minimum_signed_value_exact") == qslash(raw_linear_minimum), "serialized raw linearized margin mismatch")
    need(certificate.get("raw_linearized_minimum_owner") == {"name": raw_linear_owner[0], "family": raw_linear_owner[1]}, "serialized raw linearized owner mismatch")
    return {
        "literal_count": len(slacks),
        "family_counts": literal_contract["family_counts"],
        "literal_matrix_sha256": literal_contract["digest"],
        "all_slacks_strict": True,
        "minimum_slack_exact": qslash(minimum_slack),
        "minimum_owner": {"index_zero_based": minimum_owner.index, "name": minimum_owner.name},
        "analytic_shrink_exact": qslash(shrink),
        "literal_scale_cap_exact": qslash(literal_cap),
        "raw_scale_cap_exact": qslash(raw_cap),
        "tau_exact": qslash(tau),
        "tau_cap_exact": qslash(tau_cap),
    }


def validate_proposal_segment_summary(path_audit, proposal):
    segment = proposal["exhaustive_same_cell_segment"]
    need(segment.get("raw_first_jet_to_path_unique_key_bijection") is True, "proposal raw/path bijection claim missing")
    need(segment.get("raw_first_jet_to_path_value_and_derivative_correspondence") is True, "proposal raw/path correspondence claim missing")
    need(segment.get("primitive_count") == 12363 and segment.get("family_counts") == EXPECTED_FAMILIES, "proposal segment counts mismatch")
    need(segment.get("strict_parameter_interval_exact") == ["0", "1"] and segment.get("exact_pre_event_step") == "1", "proposal segment interval mismatch")
    need(segment.get("all_normalized_bernstein_coefficients_strictly_positive") is True, "proposal segment strictness claim missing")
    need(segment.get("bernstein_leaf_count") == path_audit["bernstein_leaf_count"], "proposal Bernstein leaf count mismatch")
    need(segment.get("minimum_normalized_bernstein_coefficient_exact") == path_audit["minimum_normalized_bernstein_coefficient_exact"], "proposal minimum Bernstein coefficient mismatch")
    need(segment.get("minimum_owner") == path_audit["minimum_owner"], "proposal minimum Bernstein owner mismatch")
    need(segment.get("path_primitive_sha256") == path_audit["path_primitive_sha256"], "proposal path digest mismatch")
    need(segment.get("maximum_subdivision_depth") == MAX_BERNSTEIN_DEPTH, "proposal Bernstein depth mismatch")


def validate_locator(scan, path_audit):
    horizons = scan["horizon_audits"]
    need(isinstance(horizons, list) and len(horizons) == 5, "locator horizon audit schema mismatch")
    expected = [("1", True, 0), ("2", True, 0), ("4", True, 0), ("8", True, 0), ("16", False, 87)]
    for row, (horizon, strict, failures) in zip(horizons, expected):
        exact_keys(row, ("horizon", "strict", "failure_count", "first_failures", "proved_leaf_count", "minimum_proved_bernstein_log10_abs"), "locator horizon row")
        need(row["horizon"] == horizon and row["strict"] is strict and row["failure_count"] == failures, f"locator horizon {horizon} mismatch")
        if strict:
            need(row["first_failures"] == [] and row["proved_leaf_count"] == 12363, f"strict locator horizon {horizon} ledger mismatch")
    need(scan["search_horizon"] == "16" and scan["candidate_count"] == 87, "locator candidate horizon/count mismatch")
    need(isinstance(scan["overlapping_first_candidates"], list) and len(scan["overlapping_first_candidates"]) == 82, "locator overlapping-first count mismatch")
    need(isinstance(scan["next_candidates"], list) and len(scan["next_candidates"]) == 30, "locator next-candidate schema mismatch")

    first = scan["first_candidate"]
    exact_keys(first, ("name", "family", "lo", "hi", "decimal", "degree", "start_sign", "value_lo", "value_hi", "polynomial_exact", "polynomial_digest"), "locator first candidate")
    need(first["name"] == "edge:(0, 16):beta1" and first["family"] == "edge_component", "unexpected locator first primitive")
    key = (first["name"], first["family"])
    need(key in path_audit["path_by_key"], "locator first primitive absent from independent path")
    polynomial = path_audit["path_by_key"][key]
    need(first["polynomial_exact"] == polynomial.exact(), "locator first polynomial differs from independent reconstruction")
    need(first["polynomial_digest"] == digest_bytes("|".join(polynomial.exact()).encode("utf-8")), "locator first polynomial digest mismatch")
    need(first["degree"] == polynomial.degree, "locator first polynomial degree mismatch")
    start_value = polynomial.eval(Q(0))
    need(first["start_sign"] == (1 if start_value > 0 else -1), "locator first primitive start sign mismatch")
    lo, hi = Q(first["lo"]), Q(first["hi"])
    need(Q(1) < lo <= hi, "locator first bracket is not strictly after the certified unit segment")
    need(first["value_lo"] == qcompact(polynomial.eval(lo)) and first["value_hi"] == qcompact(polynomial.eval(hi)), "locator first bracket values mismatch")
    need(scan["overlapping_first_candidates"][0] == first and scan["next_candidates"][0] == first, "locator first-candidate list linkage mismatch")
    # Deliberately no root/event-cell certification beyond t=1 in this task.
    return {
        "scan_sha256": EXPECTED_INPUTS["scan"][2],
        "verdict": scan["verdict"],
        "unit_segment_strict_independently": True,
        "first_candidate": first["name"],
        "first_bracket_exact": [qcompact(lo), qcompact(hi)],
        "first_bracket_strictly_after_one": True,
        "horizon_16_failure_candidate_count": 87,
        "overlapping_first_candidate_count": 82,
        "future_event_certified": False,
    }


def write_exclusive(path: Path, data: bytes) -> None:
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_CLOEXEC", 0)
    fd = os.open(path, flags, 0o644)
    try:
        offset = 0
        while offset < len(data):
            written = os.write(fd, data[offset:])
            need(written > 0, f"short write to {path}")
            offset += written
        os.fsync(fd)
    finally:
        os.close(fd)


def emit_outputs(payload, verifier_sha256, frozen):
    verification_bytes = (json.dumps(payload, indent=2) + "\n").encode("utf-8")
    verification_sha256 = digest_bytes(verification_bytes)
    path_summary = payload["exhaustive_unit_segment"]
    locator = payload["locator_boundary"]
    log_text = f"""# F21 independent exact-interior verification log

- Verdict: `{payload['verdict']}`
- Verifier SHA256: `{verifier_sha256}`
- Authoritative proposer SHA256: `{EXPECTED_INPUTS['proposer'][2]}`
- Candidate SHA256: `{EXPECTED_INPUTS['candidate'][2]}`
- Proposal SHA256: `{EXPECTED_INPUTS['proposal'][2]}`
- Receipt SHA256: `{EXPECTED_INPUTS['receipt'][2]}`
- Final locator SHA256: `{EXPECTED_INPUTS['scan'][2]}`
- Verification JSON SHA256: `{verification_sha256}`

The verifier read each authoritative input once into a held immutable snapshot,
reconstructed the accepted F20 prescribed faces, all 150 true edges, the exact
uniform-volume centroid and mechanics, both frozen carrier planes, and all 37
forced rails.  It rebuilt the exact 150-mode chart and the original 1,048-row
literal matrix (`{EXPECTED_LITERAL_DIGEST}`), then proved every final rational
literal slack strict.  The eight uniquely keyed target raw derivatives are
negative and the thirty uniquely keyed protected raw derivatives are positive.

It independently enumerated and key-matched all {path_summary['primitive_count']:,}
raw/path primitives and proved strict sign constancy on `[0,1]` with exact
Bernstein coefficients (exact Sturm fallback count:
{path_summary['sturm_fallback_count']}).  The independent path digest is
`{path_summary['path_primitive_sha256']}`.

The hash-bound locator's first bracket for `{locator['first_candidate']}` is
strictly after one.  This result does **not** certify or cross the future
87-candidate event family; an event-cell certificate remains out of scope.
"""
    log_bytes = log_text.encode("utf-8")
    created = []
    try:
        for item in frozen.values():
            item.ensure_path_unchanged()
        write_exclusive(OUTPUT, verification_bytes)
        created.append(OUTPUT)
        write_exclusive(LOG, log_bytes)
        created.append(LOG)
        for item in frozen.values():
            item.ensure_path_unchanged()
        directory_fd = os.open(HERE, os.O_RDONLY | getattr(os, "O_CLOEXEC", 0))
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    except Exception:
        for path in reversed(created):
            try:
                path.unlink()
            except FileNotFoundError:
                pass
        raise
    return verification_sha256, digest_bytes(log_bytes)


def run(check_only: bool):
    if not check_only:
        need(not OUTPUT.exists(), f"refusing to overwrite existing {OUTPUT.name}")
        need(not LOG.exists(), f"refusing to overwrite existing {LOG.name}")

    verifier_data = Path(__file__).read_bytes()
    verifier_sha256 = digest_bytes(verifier_data)
    frozen = {}
    try:
        for name, (path, expected_size, expected_hash) in EXPECTED_INPUTS.items():
            frozen[name] = freeze_input(name, path, expected_size, expected_hash)
        artifacts = validate_artifact_schemas(frozen)
        source = read_rows(frozen["f20_far"].data, "F20 far.csv")
        candidate_from_file = read_rows(frozen["candidate"].data, "F21 candidate.csv")
        cycles = validate_cycles(artifacts["faces_payload"], source)

        source_faces, candidate_faces, source_mechanics, candidate_mechanics = validate_geometry(
            source, candidate_from_file, cycles, artifacts["chart"], artifacts["proposal"]
        )
        spec = validate_chart_reconstruction(source, source_mechanics, artifacts["chart"])
        direction, _delta, physical_linf = validate_candidate_bytes(
            source, candidate_from_file, spec, artifacts["proposal"], frozen["candidate"]
        )

        literal_contract = build_literal_contract(
            source, source_faces, source_mechanics["packet"], spec
        )
        path_audit = exhaustive_path_audit(source, candidate_from_file, cycles, direction)
        validate_proposal_segment_summary(path_audit, artifacts["proposal"])
        derivative_summary = validate_derivatives_and_endpoint(
            source, candidate_from_file, source_faces, candidate_faces,
            source_mechanics, candidate_mechanics, spec, direction,
            literal_contract, artifacts["proposal"],
        )
        literal_summary = validate_literal_strictness(
            literal_contract, direction, path_audit, artifacts["proposal"]
        )
        locator_summary = validate_locator(artifacts["scan"], path_audit)

        for item in frozen.values():
            item.ensure_path_unchanged()

        input_snapshot = {
            name: {
                "path": str(item.path.relative_to(ATTACK)),
                "bytes": item.size,
                "sha256": item.sha256,
                "snapshot_reads": 1,
            }
            for name, item in frozen.items()
        }
        payload = {
            "version": 1,
            "scope": "clean-room exact verification of the F21 strict-interior proposal and certified pre-event unit segment",
            "verifier": {
                "path": "recovery2/main/post_transfer_round16/verify_exact_interior.py",
                "sha256": verifier_sha256,
                "imports_authoritative_proposer": False,
                "imports_serialized_owner_ledgers": False,
                "proof_arithmetic": "fractions.Fraction only; floats are presentation readback only",
            },
            "input_snapshots": input_snapshot,
            "lineage": {
                "f20_certificate_verdict": artifacts["certificate"]["verdict"],
                "f20_verification_verdict": artifacts["verification"]["verdict"],
                "chart_verdict": artifacts["chart"]["verdict"],
                "proposal_verdict": artifacts["proposal"]["exact_interior_verdict"],
                "receipt_status": artifacts["receipt"]["status"],
                "locator_verdict": artifacts["scan"]["verdict"],
            },
            "exact_cell_reconstruction": {
                "f_vector": EXPECTED_F_VECTOR,
                "class": EXPECTED_CLASS,
                "active_vertices": source_mechanics["active"],
                "true_edge_count": len(source_mechanics["incidence"]),
                "stable_faces": source_mechanics["packet"]["stable_faces"],
                "unstable_vertices": source_mechanics["packet"]["unstable_vertices"],
                "saddle_edges": source_mechanics["packet"]["saddle_edges"],
                "source_volume_exact": qslash(source_mechanics["volume"]),
                "source_centroid_exact": [qslash(value) for value in source_mechanics["centroid"]],
                "candidate_volume_exact": qslash(candidate_mechanics["volume"]),
                "candidate_centroid_exact": [qslash(value) for value in candidate_mechanics["centroid"]],
                "same_prescribed_faces_true_edges_and_mechanics_sign_cell": True,
                "frozen_carriers": [list(BASE), list(SHELL)],
                "forced_rail_count": 37,
                "all_forced_rails_present": True,
            },
            "candidate_byte_reconstruction": {
                "full_bytes_equal_reconstructed_source_plus_exact_coefficients": True,
                "bytes": frozen["candidate"].size,
                "sha256": frozen["candidate"].sha256,
                "mode_count": 150,
                "physical_linf_exact": qslash(physical_linf),
                "strictly_inside_trust_1e_minus_5": True,
            },
            "literal_contract": literal_summary,
            "raw_derivative_contract": {
                "target_count": len(derivative_summary["target_records"]),
                "target_unique_keys": [row["name"] for row in derivative_summary["target_records"]],
                "all_target_raw_derivatives_strictly_negative": True,
                "protected_count": len(derivative_summary["protected_records"]),
                "protected_unique_keys": [row["name"] for row in derivative_summary["protected_records"]],
                "all_protected_raw_derivatives_strictly_positive": True,
                "target_ratios_exact": derivative_summary["target_ratios"],
                "all_target_endpoint_ratios_strictly_between_zero_and_one": True,
                "minimum_protected_endpoint_increase_exact": derivative_summary["minimum_protected_endpoint_increase_exact"],
                "all_protected_endpoint_components_strictly_increased": True,
            },
            "exhaustive_unit_segment": {
                key: value for key, value in path_audit.items()
                if key not in {"path_by_key", "raw_by_order"}
            },
            "locator_boundary": locator_summary,
            "output_hash_consistency": {
                "candidate_sha256": frozen["candidate"].sha256,
                "proposal_sha256": frozen["proposal"].sha256,
                "receipt_sha256": frozen["receipt"].sha256,
                "scan_sha256": frozen["scan"].sha256,
                "proposal_receipt_locator_links_self_consistent": True,
            },
            "verdict": "INDEPENDENT_EXACT_POST_C17_F21_INTERIOR_VERIFICATION_PASS",
            "proof_status": "EXACT_STRICT_INTERIOR_ENDPOINT_AND_UNIT_PRE_EVENT_SEGMENT_VERIFIED_FIRST_FUTURE_EVENT_NOT_CERTIFIED",
            "winner_status": "NONWINNER_VERIFIED_PROPOSAL_ONLY",
            "claim_boundary": "The F21 candidate and t in [0,1] are verified. The future 87-candidate event family is not certified or crossed.",
        }

        if check_only:
            print(payload["verdict"])
            print("CHECK_ONLY_NO_OUTPUTS_WRITTEN")
            print("verifier_sha256", verifier_sha256)
            print("candidate_sha256", frozen["candidate"].sha256)
            print("scan_sha256", frozen["scan"].sha256)
            return payload, None, None

        verification_sha256, log_sha256 = emit_outputs(payload, verifier_sha256, frozen)
        print(payload["verdict"])
        print("verification_sha256", verification_sha256)
        print("log_sha256", log_sha256)
        return payload, verification_sha256, log_sha256
    finally:
        for item in frozen.values():
            try:
                item.close()
            except OSError:
                pass


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-only", action="store_true", help="run every proof but create no output artifacts")
    args = parser.parse_args()
    try:
        run(args.check_only)
    except Exception as error:
        traceback.print_exc()
        print("INDEPENDENT_EXACT_POST_C17_F21_INTERIOR_VERIFICATION_FAIL", file=sys.stderr)
        print(repr(error), file=sys.stderr)
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()
