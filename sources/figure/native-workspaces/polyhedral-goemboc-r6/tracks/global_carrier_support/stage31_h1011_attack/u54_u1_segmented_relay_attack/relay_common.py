#!/usr/bin/env python3
"""Shared exact contract for the isolated U54 -> U1 relay sidecar."""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
ATTACK = HERE.parent
TRACK = ATTACK.parent
REPO = HERE.parents[3]
ROOT = REPO.parent
SOURCE = ATTACK / "continuation2_row230_bypass" / "step15_transfer_far.csv"
FACES = ATTACK / "continuation" / "main" / "exact_full_control_chain_post_faces.json"
EXACT_CORE = TRACK / "rigorous_local_bypass" / "exact_core.py"
SELECTED_OWNER = ATTACK / "build_exact_circuit_flip.py"
CHART_OWNER = ATTACK / "continuation" / "main" / "propose_full_control.py"
HULL_OWNER = TRACK / "actual_hull_mechanics.py"

EXPECTED_SOURCE_SHA256 = "7f16c070aeba30199758815215774877bf759554d5dca1c6d875b85f27c8b94d"
EXPECTED_FACES_SHA256 = "c1d74d638df21a0492645aa39e4d3943b8401ed0732393505c838ec2f1c0ed77"
BASE = frozenset(range(17)) | {54}
BASE_CYCLE = (0, 54, *range(1, 17))
PRIMARY = (7, 8, 245)
EXPECTED_ACTIVE = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    54, 69, 72, 73, 88, 198, 224, 228, 229, 230, 231, 232, 233, 234,
    235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247,
    248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260,
    261, 262, 263, 264,
]
DANGER = {
    (frozenset((198, 230, 231)), 229),
    (frozenset((198, 229, 230)), 231),
}
PRE_FEATURES = {
    "class": [2, 2, 2],
    "stable_faces": [sorted(BASE), list(PRIMARY)],
    "unstable_vertices": [8, 54],
    "saddle_edges": [[5, 6], [10, 11]],
}
MIDDLE_FEATURES = {
    "class": [2, 3, 3],
    "stable_faces": [sorted(BASE), list(PRIMARY)],
    "unstable_vertices": [1, 8, 54],
    "saddle_edges": [[1, 54], [5, 6], [10, 11]],
}
FAR_FEATURES = {
    "class": [2, 2, 2],
    "stable_faces": [sorted(BASE), list(PRIMARY)],
    "unstable_vertices": [1, 8],
    "saddle_edges": [[5, 6], [10, 11]],
}
ALIASES = {
    "birth": ("edge:(1, 54):t", "vertex:1:54"),
    "death": ("edge:(1, 54):one_minus_t", "vertex:54:1"),
}

sys.path.insert(0, str(TRACK / "rigorous_local_bypass"))
import exact_core as ex  # noqa: E402


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


def bindings() -> dict:
    if sha256(SOURCE) != EXPECTED_SOURCE_SHA256:
        raise AssertionError("step15 source hash drift")
    if sha256(FACES) != EXPECTED_FACES_SHA256:
        raise AssertionError("face-ledger hash drift")
    return {
        relative(path): sha256(path)
        for path in (SOURCE, FACES, EXACT_CORE, SELECTED_OWNER, CHART_OWNER, HULL_OWNER)
    }


def exact_csv_bytes(rows) -> bytes:
    import io

    handle = io.StringIO(newline="")
    writer = csv.writer(handle)
    writer.writerow(("source_id", "x", "y", "z"))
    for label in sorted(rows):
        writer.writerow((label, *(ex.qs(value) for value in rows[label])))
    return handle.getvalue().encode()


def write_exact_csv(path: Path, rows) -> None:
    if path.parent.resolve() != HERE:
        raise ValueError("relay artifacts must stay in the sidecar")
    path.write_bytes(exact_csv_bytes(rows))


def affine_path(source, endpoint):
    if set(source) != set(endpoint):
        raise AssertionError("path labels differ")
    return {
        label: tuple(
            ex.P((source[label][axis], endpoint[label][axis] - source[label][axis]))
            for axis in range(3)
        )
        for label in source
    }


def evaluate_path(path, parameter: Q):
    return {
        label: tuple(value.eval(parameter) for value in xyz)
        for label, xyz in path.items()
    }


def restrict_path(path, lo: Q, hi: Q):
    return {
        label: tuple(value.affine(lo, hi) for value in xyz)
        for label, xyz in path.items()
    }


def forced_rails() -> set[tuple[int, int]]:
    rails = set()
    for route in (
        [228] + list(range(229, 247)) + [8],
        [228] + list(range(247, 265)) + [8],
    ):
        rails.update(tuple(sorted(edge)) for edge in zip(route, route[1:]))
    rails.remove((228, 229))
    if len(rails) != 37:
        raise AssertionError(len(rails))
    return rails


def edge_set(faces) -> set[tuple[int, int]]:
    return {
        tuple(sorted((first, second)))
        for cycle in faces
        for first, second in zip(cycle, cycle[1:] + cycle[:1])
    }


def face_sets(faces) -> set[tuple[int, ...]]:
    return {tuple(sorted(face)) for face in faces}


def primitive_rows(path, faces):
    """All 7,922 exact event primitives, including 18 base turns."""
    ledger = ex.mechanics_primitives(path, faces)
    yield "volume_d6", ledger["d6"], "mechanics_denominator"
    for face_index, witness, polynomial in ex.support_polynomials(path, faces):
        yield f"support:f{face_index}:w{witness}", polynomial, "support"
    for face_index, cycle in enumerate(faces):
        if len(cycle) <= 3:
            continue
        normal = ex.cycle_normal(cycle, path)
        for offset, current in enumerate(cycle):
            previous = cycle[offset - 1]
            following = cycle[(offset + 1) % len(cycle)]
            turn = ex.dot(
                ex.cross(
                    ex.sub(path[current], path[previous]),
                    ex.sub(path[following], path[current]),
                ),
                normal,
            )
            yield f"in_face_turn:f{face_index}:v{current}", turn, "in_face_turn"
    for face_key, values in sorted(ledger["reference"].items()):
        for edge, polynomial in sorted(values.items()):
            yield f"face_reference:{face_key}:{edge}", polynomial, "mechanics_denominator"
    for face_key, values in sorted(ledger["face"].items()):
        for edge, polynomial in sorted(values.items()):
            yield f"face_raw:{face_key}:{edge}", polynomial, "face_component"
    for vertex, values in sorted(ledger["vertex"].items()):
        for neighbor, polynomial in sorted(values.items()):
            yield f"vertex:{vertex}:{neighbor}", polynomial, "vertex_component"
    for edge, values in sorted(ledger["edge"].items()):
        for component in (
            "direction_norm2", "gram", "t", "one_minus_t", "beta1", "beta2"
        ):
            yield f"edge:{edge}:{component}", values[component], "edge_component"


def base_turn_rows(path, faces):
    return [row for row in primitive_rows(path, faces) if row[2] == "in_face_turn"]


def mechanics_identity(points, faces) -> dict:
    ledger = ex.mechanics_primitives(points, faces)
    birth = ledger["vertex"][1][54]
    death = ledger["vertex"][54][1]
    edge = ledger["edge"][(1, 54)]
    rhs = 4 * ledger["d6"] * ex.norm2(ex.sub(points[54], points[1]))
    if birth != edge["t"] or death != edge["one_minus_t"]:
        raise AssertionError("mechanics alias identity failed")
    if birth + death != rhs or rhs <= 0:
        raise AssertionError("positive ordering identity failed")
    return {
        "birth": ex.qs(birth),
        "death": ex.qs(death),
        "positive_gap": ex.qs(rhs),
        "birth_equals_edge_t": True,
        "death_equals_edge_one_minus_t": True,
        "sum_identity": True,
    }


def exact_checkpoint(points, faces, expected_features: dict) -> dict:
    support = ex.supporting_cell(points, faces)
    ledger, mechanics = ex.classify_point(points, faces)
    if support["f_vector"] != [61, 162, 103] or support["euler"] != 2:
        raise AssertionError(("f-vector", support))
    if support["active_labels"] != EXPECTED_ACTIVE:
        raise AssertionError(("active labels", support["active_labels"]))
    for key, expected in expected_features.items():
        if mechanics[key] != expected:
            raise AssertionError((key, mechanics[key], expected))
    if BASE not in {frozenset(face) for face in faces}:
        raise AssertionError("enlarged base absent")
    missing = sorted(forced_rails() - set(support["edges"]))
    if missing:
        raise AssertionError(("forced rails absent", missing))
    turns = base_turn_rows(
        {label: tuple(ex.P((value,)) for value in xyz) for label, xyz in points.items()},
        faces,
    )
    if len(turns) != 18 or any(polynomial.eval(Q(0)) == 0 for _, polynomial, _ in turns):
        raise AssertionError("base-turn contract failed")
    d6, m24 = ex.exact_centroid_numerators(points, faces)
    centroid = tuple(value / (4 * d6) for value in m24)
    h910 = ledger["edge"][(9, 10)]
    h910_witness = min(
        ("t", "one_minus_t", "beta1", "beta2"), key=lambda name: h910[name]
    )
    if h910[h910_witness] >= 0:
        raise AssertionError("H910 is not strictly dead")
    return {
        "coordinate_hash": canonical_hash({
            str(label): [ex.qs(value) for value in points[label]]
            for label in sorted(points)
        }),
        "exact_uniform_volume_centroid": [ex.qs(value) for value in centroid],
        "support": {key: value for key, value in support.items() if key != "edges"},
        "mechanics": mechanics,
        "identity": mechanics_identity(points, faces),
        "base_face_present": True,
        "base_turn_count": 18,
        "forced_rail_count": 37,
        "missing_forced_rails": [],
        "h910_negative_component": h910_witness,
        "h910_negative_value": ex.qs(h910[h910_witness]),
    }


def row230_values(points, faces) -> dict:
    path = {
        label: tuple(ex.P((value,)) for value in xyz)
        for label, xyz in points.items()
    }
    found = {}
    for face_index, witness, support in ex.support_polynomials(path, faces):
        family = (frozenset(faces[face_index]), witness)
        if family not in DANGER:
            continue
        normal = ex.cycle_normal(faces[face_index], path)
        value = support.eval(Q(0))
        normalized_square = value * value / ex.norm2(normal).eval(Q(0))
        found[f"{sorted(family[0])}|{witness}"] = ex.qs(normalized_square)
    if set(found) != {"[198, 230, 231]|229", "[198, 229, 230]|231"}:
        raise AssertionError(("row230 family", found))
    return found
