#!/usr/bin/env python3
"""Exact shared contract for the stable-first topology sidecar."""
from __future__ import annotations

import csv
import hashlib
import importlib.util
import io
import json
import os
import sys
import tempfile
from fractions import Fraction as Q
from pathlib import Path


sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
BRANCH = HERE.parent
SOURCE = BRANCH / "far_u1.csv"
DEATH_CERTIFICATE = BRANCH / "death_certificate.json"
DEATH_VERIFICATION = BRANCH / "death_verification.json"
DIAGNOSIS = HERE / "stable_pair_diagnosis.json"
DIAGNOSER = HERE / "diagnose_stable_pairs.py"
EXACT_CORE = ROOT / "tracks/global_carrier_support/rigorous_local_bypass/exact_core.py"
FRESH_HULL_OWNER = (
    ROOT
    / "tracks/local_oct_cell_search/clean_flip_topology_escape/far_residual_attack"
    / "verify_exact_event_certificate.py"
)

EXPECTED_HASHES = {
    SOURCE: "9f6c84382c05502766a17feb0cb9346bd44ec9f889e566e3e102d3d63a29ed77",
    DEATH_CERTIFICATE: "f799513eefcd1893b720111a8876f9027bc2b53ff598fbc68d6ff0fe37470996",
    DEATH_VERIFICATION: "86b1fb7f4e352ec162979620be43d6b02b5d5117d9e3fd305e04d84912a0ed03",
    DIAGNOSIS: "891374ef74011e364bcb2cb0b1fe64814904f8517b6d6b7bb932f024f7e53e4f",
    DIAGNOSER: "0706a899751d400c650907fc78a05b15820c7a808869c4d60eeca5db4e5d635f",
    EXACT_CORE: "d2d69ce6e4ddefd2ab7171b7e61bd09ae12846eaf509f61dd25be6d9bbb235dd",
    FRESH_HULL_OWNER: "5498478e54cc26f94ad61888113f0e1af90ba400048614933499559676b6c4ac",
}

sys.path.insert(0, str(EXACT_CORE.parent))
import exact_core as ex  # noqa: E402

spec = importlib.util.spec_from_file_location("stable_first_fresh_hull", FRESH_HULL_OWNER)
fresh = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = fresh
spec.loader.exec_module(fresh)

BASE = frozenset(range(17)) | {54}
BASE_KEY = tuple(sorted(BASE))
TARGET_EDGE = (8, 245)
TARGET_CIRCUIT = (7, 8, 245, 246)
PRE_T = Q(1, 400)
POST_T = Q(51, 20_000)
FAR_T = Q(13, 5_000)
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
SOURCE_FEATURES = {
    "class": [2, 2, 2],
    "stable_faces": [sorted(BASE), [7, 8, 245]],
    "unstable_vertices": [1, 8],
    "saddle_edges": [[5, 6], [10, 11]],
}
POST_FEATURES = {
    "class": [2, 2, 2],
    "stable_faces": [sorted(BASE), [7, 8, 246]],
    "unstable_vertices": [1, 8],
    "saddle_edges": [[5, 6], [10, 11]],
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


def bindings(extra=()) -> dict:
    packet = {relative(path): sha256(path) for path in EXPECTED_HASHES}
    for path, expected in EXPECTED_HASHES.items():
        if packet[relative(path)] != expected:
            raise AssertionError(("binding drift", relative(path), packet[relative(path)], expected))
    for path in extra:
        packet[relative(path)] = sha256(path)
    return packet


def validate_lineage() -> dict:
    bindings()
    certificate = json.loads(DEATH_CERTIFICATE.read_text())
    verification = json.loads(DEATH_VERIFICATION.read_text())
    diagnosis = json.loads(DIAGNOSIS.read_text())
    if certificate.get("verdict") != "EXACT_U54_DEATH_EPOCH_PASS":
        raise AssertionError("death certificate verdict")
    if verification.get("verdict") != "INDEPENDENT_EXACT_U54_DEATH_VERIFICATION_PASS":
        raise AssertionError("death verification verdict")
    if verification.get("far_u1_class") != [2, 2, 2] or verification.get("relay_complete") is not True:
        raise AssertionError("death verification endpoint")
    if diagnosis.get("schema") != "stable_first_topology_front.stable_pair_diagnosis":
        raise AssertionError("diagnosis schema")
    if diagnosis["source_hashes"]["far_u1.csv"] != EXPECTED_HASHES[SOURCE]:
        raise AssertionError("diagnosis source binding")
    return diagnosis


def exact_modes(source):
    e1 = ex.sub(source[1], source[0])
    e2 = ex.sub(source[2], source[0])
    if not any(ex.cross(e1, e2)):
        raise AssertionError("singular base chart")
    units = (
        ("x", (Q(1), Q(0), Q(0))),
        ("y", (Q(0), Q(1), Q(0))),
        ("z", (Q(0), Q(0), Q(1))),
    )
    modes = []
    for label in sorted(source):
        vectors = (("base_e1", e1), ("base_e2", e2)) if label in BASE else units
        for name, vector in vectors:
            modes.append((f"v{label}:{name}", label, vector))
    if len(modes) != 165:
        raise AssertionError(("mode count", len(modes)))
    return modes


def selected_velocity(source, diagnosis):
    packet = diagnosis["pairs"]["(10, 11)"]["coefficient_packet"]
    velocity = {label: [Q(0), Q(0), Q(0)] for label in source}
    seen = set()
    for name, label, vector in exact_modes(source):
        coefficient = Q(packet.get(name, "0"))
        if coefficient:
            seen.add(name)
            for axis in range(3):
                velocity[label][axis] += coefficient * vector[axis]
    if seen != set(packet):
        raise AssertionError(("unknown coefficient modes", sorted(set(packet) - seen)))
    return {label: tuple(xyz) for label, xyz in velocity.items()}


def affine_path(source, velocity):
    return {
        label: tuple(ex.P((source[label][axis], velocity[label][axis])) for axis in range(3))
        for label in source
    }


def evaluate_path(path, parameter: Q):
    return {label: tuple(value.eval(parameter) for value in xyz) for label, xyz in path.items()}


def restrict_path(path, lo: Q, hi: Q):
    return {label: tuple(value.affine(lo, hi) for value in xyz) for label, xyz in path.items()}


def circuit_polynomial(path):
    a, b, c, d = (path[label] for label in TARGET_CIRCUIT)
    return ex.det3(ex.sub(b, a), ex.sub(c, a), ex.sub(d, a))


def primitive_rows(path, faces):
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
        for component in ("direction_norm2", "gram", "t", "one_minus_t", "beta1", "beta2"):
            yield f"edge:{edge}:{component}", values[component], "edge_component"


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


def edge_set(faces):
    return {
        tuple(sorted((first, second)))
        for cycle in faces
        for first, second in zip(cycle, cycle[1:] + cycle[:1])
    }


def row230_values(points, faces) -> dict:
    path = {label: tuple(ex.P((value,)) for value in xyz) for label, xyz in points.items()}
    found = {}
    for face_index, witness, support in ex.support_polynomials(path, faces):
        family = (frozenset(faces[face_index]), witness)
        if family not in DANGER:
            continue
        normal = ex.cycle_normal(faces[face_index], path)
        value = support.eval(Q(0))
        normalized_square = value * value / ex.norm2(normal).eval(Q(0))
        found[f"{sorted(family[0])}|{witness}"] = ex.qs(normalized_square)
    expected = {"[198, 230, 231]|229", "[198, 229, 230]|231"}
    if set(found) != expected or any(Q(value) <= 0 for value in found.values()):
        raise AssertionError(("row230 family", found))
    return found


def checkpoint(points, faces, expected_features) -> dict:
    support = ex.supporting_cell(points, faces)
    ledger, mechanics = ex.classify_point(points, faces)
    if support["f_vector"] != [61, 162, 103] or support["euler"] != 2:
        raise AssertionError(("f-vector", support["f_vector"]))
    if support["active_labels"] != EXPECTED_ACTIVE:
        raise AssertionError(("active labels", support["active_labels"]))
    if mechanics != expected_features:
        raise AssertionError(("mechanics", mechanics, expected_features))
    missing = sorted(forced_rails() - edge_set(faces))
    if missing:
        raise AssertionError(("missing rails", missing))
    h910 = ledger["edge"][(9, 10)]
    witness = min(("t", "one_minus_t", "beta1", "beta2"), key=lambda name: h910[name])
    if h910[witness] >= 0:
        raise AssertionError("H(9,10) is not strictly dead")
    return {
        "support": {key: value for key, value in support.items() if key != "edges"},
        "mechanics": mechanics,
        "forced_rail_count": len(forced_rails()),
        "missing_forced_rails": [],
        "row230_squared_margins": row230_values(points, faces),
        "h910_negative_component": witness,
        "h910_negative_value": ex.qs(h910[witness]),
    }


def exact_csv_bytes(rows) -> bytes:
    handle = io.StringIO(newline="")
    writer = csv.writer(handle, lineterminator="\n")
    writer.writerow(("source_id", "x", "y", "z"))
    for label in sorted(rows):
        writer.writerow((label, *(ex.qs(value) for value in rows[label])))
    return handle.getvalue().encode()


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=False, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary_path = Path(temporary)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_path, path)
        directory_fd = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
        if path.read_bytes() != data:
            raise AssertionError(("atomic readback", path))
    finally:
        if temporary_path.exists():
            temporary_path.unlink()
