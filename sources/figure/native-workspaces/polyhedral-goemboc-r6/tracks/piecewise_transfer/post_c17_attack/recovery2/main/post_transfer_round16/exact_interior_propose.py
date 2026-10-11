#!/usr/bin/env python3
"""Fail-closed exact-interior F21 proposer from the accepted F20 lineage.

HiGHS is used only on a reversibly row-equilibrated floating-point copy of
the literal first-order problem.  A proposal is emitted only after a rational
direction is analytically shrunk into the strict interior of every original
literal row and the complete 12,363-primitive source-to-candidate segment is
proved strict with exact Bernstein coefficients.
"""
from __future__ import annotations

import csv
import gc
import hashlib
import io
import json
import math
import os
import sys
import traceback
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path
from types import ModuleType, SimpleNamespace


HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ATTACK = MAIN.parents[1]
TRANSFER = ATTACK / "recovery2" / "transfer_search"
PIECEWISE = ATTACK.parent
TRACKS = ATTACK.parents[1]
WORKSPACE = ATTACK.parents[2]
SOURCE = MAIN / "post_transfer_round15" / "far.csv"
FACES_PATH = MAIN / "post_transfer_round15" / "post_faces.json"
SOURCE_CERTIFICATE = MAIN / "post_transfer_round15" / "certificate.json"
SOURCE_VERIFICATION = MAIN / "post_transfer_round15" / "verification.json"
CHART_PATH = HERE / "chart.json"
OUTPUT = HERE / "exact_interior_proposal.json"
ENDPOINT = HERE / "exact_interior_candidate.csv"
RECEIPT = HERE / "exact_interior_receipt.json"

# Remove every prior PASS-like output before third-party or local executable
# imports.  An import failure must never leave a stale candidate visible.
if __name__ == "__main__":
    for _bootstrap_output in (OUTPUT, ENDPOINT, RECEIPT):
        _bootstrap_output.unlink(missing_ok=True)

import numpy as np
from scipy.optimize import linprog

EXPECTED_FILES = {
    SOURCE: (
        82321,
        "d34ebac9a1cfe81ce4d782049938ad68f1124eb82e3cd19342c30e5de14f39e3",
    ),
    FACES_PATH: (
        3283,
        "06b15585bd906ae1ee0cfc5aefff2a46a5e752a02dfb556abde9225e1df81c6b",
    ),
    SOURCE_CERTIFICATE: (
        121428,
        "51ceeecf32d32dedc6ae2fe3a05c9fd78d0c88ebbace7047b7be21b195ab77b2",
    ),
    SOURCE_VERIFICATION: (
        86818,
        "0e9f86e08325aa3272b3ad7c1768ac3270ef29d793c5d22ccc2536156193ff2a",
    ),
    CHART_PATH: (
        28897,
        "29ddf33a8126a2315a09eb6daee77b80b9691f1fd1b91e9a127e87699197b4b8",
    ),
}
EXPECTED_SOURCE_VERDICT = "EXACT_POST_C17_TWENTIETH_SAFE_FLIP_PASS"
EXPECTED_SOURCE_VERIFICATION_VERDICT = (
    "INDEPENDENT_EXACT_POST_C17_TWENTIETH_SAFE_FLIP_PASS"
)
EXPECTED_CHART_VERDICT = "EXACT_POST_SAFE_FLIP_FIXED_PLANE_CHART_PASS"
PROPOSAL_VERDICT = "RATIONAL_POST_SAFE_FLIP_DESCENT_PROPOSAL_PASS"
EXACT_INTERIOR_VERDICT = "EXACT_POST_C17_F21_INTERIOR_PROPOSAL_PASS"
NO_PROPOSAL_VERDICT = "NO_EXACT_POST_C17_F21_INTERIOR_PROPOSAL"
TRUSTS = tuple(Q(value) for value in (
    "1e-8", "3e-8", "1e-7", "3e-7", "1e-6", "3e-6", "1e-5", "3e-5"
))
PREFERRED_TRUST = Q("1e-5")
MAX_BERNSTEIN_DEPTH = 34
EXPECTED_LITERAL_MATRIX_SHA256 = (
    "1e419caf3ee6365fc9fd3b03779f6f7a33f601f28d95c6f2bf842a2e7a44a271"
)

OWNER_MODULES = (
    (
        "numeric_hull_proposer",
        WORKSPACE / "M42_acute_bridge_fifth_cell_work" / "fourth_cell_endpoint"
        / "numeric_hull_proposer.py",
        8454,
        "35aba4a57d01f5313704476c631bf550dc6fb4718c562ffa9891489a37a1d4e4",
    ),
    (
        "rank5_exact_reconstruction",
        PIECEWISE / "rank5_exact_reconstruction.py",
        9853,
        "86016a9ce94feb4e24d641b78d4ea46232a6a0ce355af7e2fb8c58df3af19a4d",
    ),
    (
        "rank5_exact_jacobian",
        PIECEWISE / "rank5_exact_jacobian.py",
        16244,
        "87bf6343c31c79f2b162b1b159c63fc086f7f4dbf2da42fb3ba70dff773b27d9",
    ),
    (
        "rank5_search",
        PIECEWISE / "rank5_search.py",
        8527,
        "4c224f0e009cc0a6a9ce68620a7798f1cf31c5994994b75543a3ba91ada30844",
    ),
    (
        "rank5_sixth_control",
        PIECEWISE / "rank5_sixth_control.py",
        21445,
        "f66c380dc97cefc91d029566cb0533777ab24ec7cc56c7faa86d60eab9a84f2b",
    ),
    (
        "rank5_circuit_escape",
        PIECEWISE / "rank5_circuit_escape.py",
        34384,
        "22061ee4426e59d39faf8eb4d668aaa6205125dca10d77785254b5ef965aaec5",
    ),
    (
        "rank5_circuit_escape_continuation",
        PIECEWISE / "rank5_circuit_escape_continuation.py",
        27713,
        "a3f840d2913322de529957f3078e54004ec542fe5a9cf51a6be1614471a3bf14",
    ),
    (
        "post_c17_exact",
        ATTACK / "post_c17_exact.py",
        31496,
        "799fcf1fc024cf928ca7426b814f351729bc5be8a255be7aca08c1e88671604b",
    ),
    (
        "build_full_chart",
        MAIN / "build_full_chart.py",
        10411,
        "b1c5cc929168d35791e387c9ed8d2fd0cc2e5ece87b1069a7e5e7f307644f481",
    ),
    (
        "propose_fixed_plane_descent",
        MAIN / "propose_fixed_plane_descent.py",
        18415,
        "6ca2bab0e2717def0b3ff5c4a2bda33265df9862a2a03acfa34e3a3377105968",
    ),
    (
        "build_first_jet_atlas",
        TRANSFER / "build_first_jet_atlas.py",
        28598,
        "4dc51083c71149db251ad5885712546ea8539b0c7d7ea5c6910ae4d732ba2d1f",
    ),
    (
        "exact_core",
        TRACKS / "global_carrier_support" / "rigorous_local_bypass"
        / "exact_core.py",
        37641,
        "d2d69ce6e4ddefd2ab7171b7e61bd09ae12846eaf509f61dd25be6d9bbb235dd",
    ),
    (
        "post_c17_f21_exact_interior_locator",
        MAIN / "locate_first_event.py",
        10180,
        "d7a1b7d645904c25cb075e3f08ebe3d4e086984c1ecb75f0111825041fe43e63",
    ),
)

sys.set_int_max_str_digits(0)
sys.path.insert(0, str(MAIN))
sys.path.insert(0, str(ATTACK))
sys.path.insert(0, str(TRANSFER))

atlas = None
chart = None
pc = None
proposer = None
locator = None
OWNER_CODE_SNAPSHOT = None


def qs(value: Q) -> str:
    return pc.qs(Q(value))


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def relative(path: Path) -> str:
    return str(path.relative_to(ATTACK))


def canonical_hash(value) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode()).hexdigest()


class ContractFailure(RuntimeError):
    def __init__(self, stage: str, message: str, primitive=None, details=None):
        super().__init__(message)
        self.stage = stage
        self.primitive = primitive
        self.details = details


def require(condition: bool, stage: str, message: str, primitive=None, details=None):
    if not condition:
        raise ContractFailure(stage, message, primitive, details)


def workspace_relative(path: Path) -> str:
    return str(path.resolve().relative_to(WORKSPACE))


def _load_frozen_module(name: str, path: Path, source: bytes):
    require(name not in sys.modules, "owner_snapshot", f"preloaded owner module: {name}")
    module = ModuleType(name)
    module.__file__ = str(path)
    module.__package__ = ""
    sys.modules[name] = module
    try:
        exec(compile(source, str(path), "exec"), module.__dict__)
    except Exception:
        sys.modules.pop(name, None)
        raise
    return module


def load_frozen_owners():
    global atlas, chart, pc, proposer, locator, OWNER_CODE_SNAPSHOT
    if OWNER_CODE_SNAPSHOT is not None:
        return OWNER_CODE_SNAPSHOT

    frozen = []
    packet = {}
    for name, path, expected_bytes, expected_hash in OWNER_MODULES:
        resolved = path.resolve()
        require(
            resolved == path and path.is_file() and not path.is_symlink(),
            "owner_snapshot",
            f"invalid trusted owner path: {path}",
        )
        source = path.read_bytes()
        observed_hash = sha256_bytes(source)
        require(
            len(source) == expected_bytes and observed_hash == expected_hash,
            "owner_snapshot",
            f"trusted owner drift: {workspace_relative(path)}",
            details={
                "expected_bytes": expected_bytes,
                "observed_bytes": len(source),
                "expected_sha256": expected_hash,
                "observed_sha256": observed_hash,
            },
        )
        frozen.append((name, path, source))
        packet[workspace_relative(path)] = {
            "module": name,
            "bytes": len(source),
            "sha256": observed_hash,
            "snapshot_reads": 1,
        }

    for name, _path, _source in frozen:
        require(name not in sys.modules, "owner_snapshot", f"owner already loaded: {name}")
    for name, path, source in frozen:
        _load_frozen_module(name, path, source)

    atlas = sys.modules["build_first_jet_atlas"]
    chart = sys.modules["build_full_chart"]
    pc = sys.modules["post_c17_exact"]
    proposer = sys.modules["propose_fixed_plane_descent"]
    locator = sys.modules["post_c17_f21_exact_interior_locator"]
    OWNER_CODE_SNAPSHOT = packet
    return packet


@dataclass(frozen=True)
class LiteralRow:
    index: int
    name: str
    family: str
    coefficients: tuple[Q, ...]
    tau_coefficient: Q
    rhs: Q

    def lhs(self, direction: tuple[Q, ...], tau: Q = Q(0)) -> Q:
        return sum(
            (a * b for a, b in zip(self.coefficients, direction)), Q(0)
        ) + self.tau_coefficient * tau

    def slack(self, direction: tuple[Q, ...], tau: Q) -> Q:
        return self.rhs - self.lhs(direction, tau)


def atomic_bytes(path: Path, data: bytes) -> None:
    temporary = path.parent / f".{path.name}.{os.getpid()}.tmp"
    try:
        with temporary.open("xb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        temporary.replace(path)
        directory = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    finally:
        temporary.unlink(missing_ok=True)


def atomic_json(path: Path, payload) -> bytes:
    data = (json.dumps(payload, indent=2) + "\n").encode()
    atomic_bytes(path, data)
    return data


def clear_candidate_outputs() -> None:
    for path in (OUTPUT, ENDPOINT):
        path.unlink(missing_ok=True)


def lineage_snapshot():
    snapshot = {}
    frozen_bytes = {}
    for path, (expected_bytes, expected_hash) in EXPECTED_FILES.items():
        require(
            path.is_file() and not path.is_symlink(),
            "lineage",
            f"missing or aliased lineage file: {path}",
        )
        data = path.read_bytes()
        observed_bytes = len(data)
        observed_hash = sha256_bytes(data)
        primitive = {
            "name": relative(path),
            "family": "lineage_file",
            "expected_bytes": expected_bytes,
            "observed_bytes": observed_bytes,
            "expected_sha256": expected_hash,
            "observed_sha256": observed_hash,
        }
        require(
            observed_bytes == expected_bytes,
            "lineage",
            f"byte count drift for {path.name}",
            primitive,
        )
        require(
            observed_hash == expected_hash,
            "lineage",
            f"sha256 drift for {path.name}",
            primitive,
        )
        snapshot[relative(path)] = {
            "bytes": observed_bytes,
            "sha256": observed_hash,
            "snapshot_reads": 1,
        }
        frozen_bytes[path] = data
    return snapshot, frozen_bytes


def strict_read_rows(path: Path, data: bytes):
    expected_header = [
        "source_id", "x_exact", "y_exact", "z_exact", "x", "y", "z"
    ]
    rows = {}
    with io.StringIO(data.decode("utf-8"), newline="") as stream:
        reader = csv.DictReader(stream)
        require(
            reader.fieldnames == expected_header,
            "source_schema",
            "unexpected source CSV schema",
            details={"observed_header": reader.fieldnames},
        )
        for line_number, record in enumerate(reader, start=2):
            try:
                label = int(record["source_id"])
                point = tuple(Q(record[key]) for key in ("x_exact", "y_exact", "z_exact"))
                decimals = tuple(float(record[key]) for key in ("x", "y", "z"))
            except Exception as error:
                raise ContractFailure(
                    "source_schema",
                    f"invalid source row {line_number}: {error!r}",
                ) from error
            require(
                label not in rows,
                "source_schema",
                f"duplicate source_id {label}",
            )
            require(
                all(math.isfinite(value) for value in decimals),
                "source_schema",
                f"non-finite decimal readback at source_id {label}",
            )
            rows[label] = point
    require(len(rows) == 119, "source_schema", f"expected 119 rows, got {len(rows)}")
    return rows


def exact_sign(value) -> int:
    rational = Q(value)
    return (rational > 0) - (rational < 0)


def mechanics_sign_ledger(face_ledger, vertex_ledger, edge_ledger):
    return {
        "faces": [
            {
                "face": record["face"],
                "cycle": record["cycle"],
                "stable": record["stable"],
                "component_signs": [
                    exact_sign(value) for value in record["components_exact"]
                ],
            }
            for record in face_ledger
        ],
        "vertices": [
            {
                "vertex": record["vertex"],
                "unstable": record["unstable"],
                "support_signs": {
                    neighbor: exact_sign(value)
                    for neighbor, value in record["supports_exact"].items()
                },
            }
            for record in vertex_ledger
        ],
        "edges": [
            {
                "edge": record["edge"],
                "incident_faces": record["incident_faces"],
                "saddle": record["saddle"],
                "component_signs": [
                    exact_sign(value) for value in record["components_exact"]
                ],
            }
            for record in edge_ledger
        ],
    }


def load_context():
    owner_code_snapshot = load_frozen_owners()
    lineage, lineage_bytes = lineage_snapshot()
    try:
        certificate = json.loads(lineage_bytes[SOURCE_CERTIFICATE])
        verification = json.loads(lineage_bytes[SOURCE_VERIFICATION])
        cycles = json.loads(lineage_bytes[FACES_PATH])
        chart_payload = json.loads(lineage_bytes[CHART_PATH])
    except Exception as error:
        raise ContractFailure("schema", f"invalid JSON input: {error!r}") from error

    require(certificate.get("version") == 1, "certificate_schema", "certificate version")
    require(
        certificate.get("verdict") == EXPECTED_SOURCE_VERDICT,
        "certificate_provenance",
        "unexpected F20 certificate verdict",
    )
    require(
        certificate.get("winner_status") == "NONWINNER",
        "certificate_schema",
        "unexpected F20 winner status",
    )
    require(
        certificate.get("scope")
        == "All 12,363 support/in-face/own-centroid primitives in both strict cells, algebraic event family and exact checkpoints.",
        "certificate_schema",
        "unexpected F20 certificate scope",
    )
    generated = certificate.get("generated_file_sha256")
    require(isinstance(generated, dict), "certificate_schema", "missing generated hashes")
    require(
        generated.get(relative(SOURCE)) == EXPECTED_FILES[SOURCE][1],
        "certificate_provenance",
        "F20 certificate does not bind far.csv",
    )
    require(
        generated.get(relative(FACES_PATH)) == EXPECTED_FILES[FACES_PATH][1],
        "certificate_provenance",
        "F20 certificate does not bind post_faces.json",
    )
    checkpoint = certificate.get("rational_checkpoints", {}).get("far", {})
    support_checkpoint = checkpoint.get("exact_support", {})
    mechanics_checkpoint = checkpoint.get("exact_mechanics", {})
    require(
        support_checkpoint.get("f_vector") == [61, 150, 91]
        and support_checkpoint.get("strict_support_count") == 10529
        and checkpoint.get("forced_rail_count") == 37
        and checkpoint.get("missing_forced_rails") == [],
        "certificate_schema",
        "F20 far support checkpoint mismatch",
    )
    require(
        mechanics_checkpoint.get("class") == [2, 4, 4]
        and mechanics_checkpoint.get("unstable_vertices") == [8, 228, 231, 246]
        and mechanics_checkpoint.get("saddle_edges")
        == [[8, 246], [228, 254], [231, 247], [236, 237]],
        "certificate_schema",
        "F20 far mechanics checkpoint mismatch",
    )
    require(
        verification.get("version") == 1
        and verification.get("verdict") == EXPECTED_SOURCE_VERIFICATION_VERDICT
        and verification.get("scope")
        == "clean reconstruction of exact post-C17 fixed-plane safe flip"
        and verification.get("certificate_sha256")
        == EXPECTED_FILES[SOURCE_CERTIFICATE][1]
        and verification.get("primitive_count_each_strict_cell") == 12363
        and verification.get("winner_status") == "NONWINNER",
        "certificate_provenance",
        "accepted F20 independent verification mismatch",
    )

    expected_source_hashes = {
        relative(SOURCE): EXPECTED_FILES[SOURCE][1],
        relative(FACES_PATH): EXPECTED_FILES[FACES_PATH][1],
        relative(SOURCE_CERTIFICATE): EXPECTED_FILES[SOURCE_CERTIFICATE][1],
    }
    require(chart_payload.get("version") == 1, "chart_schema", "chart version")
    require(
        chart_payload.get("verdict") == EXPECTED_CHART_VERDICT,
        "chart_schema",
        "unexpected F21 chart verdict",
    )
    require(
        chart_payload.get("source_hashes") == expected_source_hashes,
        "chart_provenance",
        "F21 chart lineage mismatch",
    )
    require(
        chart_payload.get("f_vector") == [61, 150, 91]
        and chart_payload.get("class") == [2, 4, 4]
        and chart_payload.get("mode_count") == 150
        and chart_payload.get("target_rank_exact") == 8
        and chart_payload.get("protected_component_count") == 30,
        "chart_schema",
        "F21 chart dimensions mismatch",
    )

    require(isinstance(cycles, list) and len(cycles) == 91, "faces_schema", "faces count")
    rows = strict_read_rows(SOURCE, lineage_bytes[SOURCE])
    canonical_faces = set()
    for index, cycle in enumerate(cycles):
        require(
            isinstance(cycle, list)
            and len(cycle) >= 3
            and all(isinstance(label, int) for label in cycle)
            and len(set(cycle)) == len(cycle)
            and set(cycle).issubset(rows),
            "faces_schema",
            f"invalid face cycle {index}",
        )
        key = tuple(sorted(cycle))
        require(key not in canonical_faces, "faces_schema", f"duplicate face {index}")
        canonical_faces.add(key)

    faces = pc.ex.exactify_faces(
        rows, SimpleNamespace(faces=[{"cycle": list(cycle)} for cycle in cycles])
    )
    volume, centroid = pc.ex.exact_mass(rows, faces)
    ef, active, fl, vl, el, stable, unstable, saddles = pc.ex.exact_mechanics(
        rows, faces, centroid
    )
    packet = {
        "f_vector": [len(active), len(ef), len(faces)],
        "class": [len(stable), len(unstable), len(saddles)],
        "active_vertices": active,
        "stable_faces": [faces[index]["cycle"] for index in stable],
        "unstable_vertices": unstable,
        "saddle_edges": [list(edge) for edge in saddles],
    }
    require(packet["f_vector"] == [61, 150, 91], "source_exact", "F20 f-vector")
    require(packet["class"] == [2, 4, 4], "source_exact", "F20 mechanics class")
    require(
        packet["unstable_vertices"] == [8, 228, 231, 246],
        "source_exact",
        "F20 unstable ledger",
    )
    require(
        packet["saddle_edges"] == [[8, 246], [228, 254], [231, 247], [236, 237]],
        "source_exact",
        "F20 saddle ledger",
    )
    require(
        {tuple(sorted(face)) for face in packet["stable_faces"]}
        == {tuple(range(17)), (228, 246, 264)},
        "source_exact",
        "F20 stable ledger",
    )
    require(
        not (pc.esc.forced_rails() - set(ef)),
        "source_exact",
        "F20 forced rails missing",
    )

    spec, basis = chart.build_spec(rows, tuple(active))
    require(len(spec) == 150, "chart_exact", "recomputed mode count")
    mode_names = [name for _row, name, _direction in spec]
    require(
        chart_payload.get("mode_names") == mode_names,
        "chart_exact",
        "recomputed mode names mismatch",
    )
    recomputed_basis = {
        name: [qs(value) for value in vector] for name, vector in basis.items()
    }
    require(
        chart_payload.get("basis_exact") == recomputed_basis,
        "chart_exact",
        "recomputed exact basis mismatch",
    )
    return {
        "lineage": lineage,
        "owner_code_snapshot": owner_code_snapshot,
        "certificate": certificate,
        "verification": verification,
        "chart_payload": chart_payload,
        "cycles": cycles,
        "rows": rows,
        "faces": faces,
        "volume": volume,
        "centroid": centroid,
        "edges": set(ef),
        "packet": packet,
        "mechanics_sign_ledger": mechanics_sign_ledger(fl, vl, el),
        "spec": spec,
    }


def exact_displacement_rows(active, spec):
    row_index = {label: offset for offset, label in enumerate(active)}
    matrix = [[Q(0)] * len(spec) for _ in range(3 * len(active))]
    labels = []
    for label in active:
        labels.extend((f"r{label}_x", f"r{label}_y", f"r{label}_z"))
    for column, (label, _name, direction) in enumerate(spec):
        offset = row_index[label]
        for axis in range(3):
            matrix[3 * offset + axis][column] = Q(direction[axis])
    return tuple(tuple(row) for row in matrix), tuple(labels)


def build_literal_problem(context, trust: Q):
    rows = context["rows"]
    faces = context["faces"]
    packet = context["packet"]
    spec = context["spec"]
    targets0, base0, u80 = chart.target_jets(rows, faces, spec)
    target_rank = pc.rj.matrix_rank([targets0[name].d for name in chart.TARGET_NAMES])
    require(target_rank == 8, "literal_matrix", "target exact rank drift")
    q, jet_centroid, mechanics = proposer.mechanics_records(rows, faces, packet, spec)
    require(
        tuple(value.v for value in jet_centroid) == context["centroid"],
        "literal_matrix",
        "jet centroid value mismatch",
    )
    require(len(mechanics) == 371, "literal_matrix", f"mechanics count {len(mechanics)}")
    by_id = {record["id"]: record for record in mechanics}
    require(len(by_id) == len(mechanics), "literal_matrix", "duplicate mechanics id")
    target_ids = proposer.target_ids()
    require(tuple(target_ids) == chart.TARGET_NAMES, "literal_matrix", "target order")
    for name, identifier in target_ids.items():
        require(identifier in by_id, "literal_matrix", f"missing target {name}")
        require(
            by_id[identifier]["value"].v == targets0[name].v,
            "literal_matrix",
            f"target jet mismatch {name}",
        )
    protected_ids = {
        record["id"]
        for record in mechanics
        if (record["id"][0] == "S" and record["id"][1] == tuple(chart.BASE))
        or (record["id"][0] == "U" and record["id"][1] == 8)
    }
    protected0 = {
        **{("S", tuple(sorted(edge))): value.v for edge, value in base0.items()},
        **{("U8", neighbor): value.v for neighbor, value in u80.items()},
    }
    require(
        len(protected_ids) == len(protected0) == 30,
        "literal_matrix",
        "protected component count",
    )
    support_guards, support_summary = proposer.support_and_turn_guards(
        rows, faces, q
    )
    require(
        support_summary["all_support_rows"] == 10529
        and support_summary["selected_near_support_rows"] == 278
        and support_summary["in_face_turn_rows"] == 33
        and len(support_guards) == 311,
        "literal_matrix",
        "support guard selection drift",
    )

    literals = []
    protected_source_by_name = {}

    def add(name, family, coefficients, tau_coefficient, rhs):
        literals.append(LiteralRow(
            len(literals),
            name,
            family,
            tuple(Q(value) for value in coefficients),
            Q(tau_coefficient),
            Q(rhs),
        ))

    for name, identifier in target_ids.items():
        value = by_id[identifier]["value"]
        add(
            f"target:{name}",
            "target",
            (item / value.v for item in value.d),
            Q(1),
            Q(0),
        )
    target_id_set = set(target_ids.values())
    for record in mechanics:
        if record["id"] in target_id_set:
            continue
        value = record["value"]
        if record["id"] in protected_ids:
            protected_name = f"protected:{record['id']!r}"
            add(
                protected_name,
                "protected",
                (-item / value.v for item in value.d),
                Q(1, 20),
                Q(0),
            )
            protected_source_by_name[protected_name] = value.v
        else:
            sign = Q(1) if value.v > 0 else Q(-1)
            add(
                f"mechanics:{record['id']!r}",
                "mechanics_guard",
                (-sign * item for item in value.d),
                Q(0),
                abs(value.v) / 5,
            )
    for record in support_guards:
        value = record["value"]
        add(
            f"{record['kind']}:{record['id']!r}",
            record["kind"],
            (-item for item in value.d),
            Q(0),
            value.v / 5,
        )
    physical, physical_names = exact_displacement_rows(
        tuple(packet["active_vertices"]), spec
    )
    for name, coefficients in zip(physical_names, physical):
        add(f"physical_plus:{name}", "physical_plus", coefficients, Q(0), trust)
    for name, coefficients in zip(physical_names, physical):
        add(
            f"physical_minus:{name}",
            "physical_minus",
            (-value for value in coefficients),
            Q(0),
            trust,
        )

    counts = Counter(row.family for row in literals)
    expected_counts = {
        "target": 8,
        "protected": 30,
        "mechanics_guard": 333,
        "near_support": 278,
        "in_face_turn": 33,
        "physical_plus": 183,
        "physical_minus": 183,
    }
    require(counts == expected_counts, "literal_matrix", f"family counts {dict(counts)}")
    require(len(literals) == 1048, "literal_matrix", f"literal count {len(literals)}")
    require(
        all(len(row.coefficients) == 150 for row in literals),
        "literal_matrix",
        "literal width mismatch",
    )
    observed_literal_digest = literal_digest(literals)
    require(
        observed_literal_digest == EXPECTED_LITERAL_MATRIX_SHA256,
        "literal_matrix",
        "original 1,048-row literal digest drift",
        details={
            "expected_sha256": EXPECTED_LITERAL_MATRIX_SHA256,
            "observed_sha256": observed_literal_digest,
        },
    )
    return {
        "literals": tuple(literals),
        "literal_matrix_sha256": observed_literal_digest,
        "family_counts": dict(counts),
        "mechanics": mechanics,
        "protected_ids": protected_ids,
        "protected_source_by_name": protected_source_by_name,
        "targets0": targets0,
        "protected0": protected0,
        "support_summary": support_summary,
        "q": q,
    }


def problem_with_trust(problem, trust: Q):
    physical_families = {"physical_plus", "physical_minus"}
    clone = dict(problem)
    clone["literals"] = tuple(
        LiteralRow(
            row.index,
            row.name,
            row.family,
            row.coefficients,
            row.tau_coefficient,
            trust if row.family in physical_families else row.rhs,
        )
        for row in problem["literals"]
    )
    return clone


def literal_digest(literals) -> str:
    digest = hashlib.sha256()
    for row in literals:
        digest.update(
            (
                f"{row.index}|{row.name}|{row.family}|"
                f"{'|'.join(qs(value) for value in row.coefficients)}|"
                f"{qs(row.tau_coefficient)}|{qs(row.rhs)}\n"
            ).encode()
        )
    return digest.hexdigest()


def solve_literal_problem(problem, trust: Q):
    literals = problem["literals"]
    matrix = np.empty((len(literals), 151), dtype=float)
    rhs = np.empty(len(literals), dtype=float)
    maximum = None
    for row in literals:
        exact_row = row.coefficients + (row.tau_coefficient,)
        for column, value in enumerate(exact_row):
            converted = float(value)
            require(
                math.isfinite(converted),
                "numerical_transform",
                f"non-finite float at literal {row.index}, column {column}",
            )
            matrix[row.index, column] = converted
            magnitude = abs(converted)
            if maximum is None or magnitude > maximum[0]:
                maximum = (magnitude, row, column, value)
        rhs[row.index] = float(row.rhs)
        require(
            math.isfinite(rhs[row.index]),
            "numerical_transform",
            f"non-finite rhs at literal {row.index}",
        )
    row_scales = np.maximum.reduce((
        np.max(np.abs(matrix), axis=1),
        np.abs(rhs),
        np.full(len(rhs), 1e-300),
    ))
    require(
        bool(np.all(np.isfinite(row_scales))) and bool(np.all(row_scales > 0)),
        "numerical_transform",
        "invalid row scale",
    )
    scaled_matrix = matrix / row_scales[:, None]
    scaled_rhs = rhs / row_scales
    require(
        float(np.max(np.abs(scaled_matrix))) <= 1.0,
        "numerical_transform",
        "row equilibration failed",
    )
    objective = np.r_[np.zeros(150), -1.0]
    lp = linprog(
        objective,
        A_ub=scaled_matrix,
        b_ub=scaled_rhs,
        bounds=[(None, None)] * 150 + [(0.0, 1.0)],
        method="highs-ds",
        options={
            "primal_feasibility_tolerance": 1e-9,
            "dual_feasibility_tolerance": 1e-9,
        },
    )
    scale_digest = hashlib.sha256(
        "\n".join(value.hex() for value in row_scales).encode()
    ).hexdigest()
    max_magnitude, max_row, max_column, max_exact = maximum
    record = {
        "trust_exact": qs(trust),
        "trust_decimal": float(trust),
        "solver_success": bool(lp.success),
        "solver_status": int(lp.status),
        "solver_message": str(lp.message),
        "constraint_count": len(literals),
        "literal_matrix_sha256": literal_digest(literals),
        "numerical_transform": {
            "kind": "positive diagonal row equilibration only",
            "formula": "A'_i=A_i/s_i, b'_i=b_i/s_i, s_i=max(max_j(abs(float(A_ij))),abs(float(b_i)),1e-300)",
            "reversible": True,
            "row_scale_float_hex_sha256": scale_digest,
            "minimum_row_scale": float(np.min(row_scales)),
            "maximum_row_scale": float(np.max(row_scales)),
            "scaled_maximum_absolute_coefficient": float(np.max(np.abs(scaled_matrix))),
            "original_exact_matrix_retained_for_readback": True,
            "column_equilibration_used": False,
        },
        "unscaled_maximum_coefficient": {
            "absolute_decimal": max_magnitude,
            "exact": qs(max_exact),
            "literal_index_zero_based": max_row.index,
            "literal_name": max_row.name,
            "column_index_zero_based": max_column,
            "column_name": (
                context_mode_name(problem, max_column)
                if max_column < 150 else "tau"
            ),
        },
    }
    if not lp.success:
        record["proof_status"] = "NUMERICAL_FAILURE_IS_NOT_AN_OBSTRUCTION"
        return record, None
    direction = tuple(Q.from_float(float(value)) for value in lp.x[:150])
    exact_target = []
    exact_protected = []
    for row in literals:
        if row.family not in {"target", "protected"}:
            continue
        directional_lhs = row.lhs(direction, Q(0))
        entry = {
            "literal_index_zero_based": row.index,
            "literal_name": row.name,
            "directional_lhs_exact": qs(directional_lhs),
        }
        (exact_target if row.family == "target" else exact_protected).append(entry)
    signs_pass = (
        all(Q(item["directional_lhs_exact"]) < 0 for item in exact_target)
        and all(Q(item["directional_lhs_exact"]) < 0 for item in exact_protected)
    )
    record.update({
        "solver_common_fractional_descent": float(lp.x[-1]),
        "binary_rational_readback": True,
        "nonzero_rational_coefficients": sum(value != 0 for value in direction),
        "exact_homogeneous_sign_readback": signs_pass,
        "target_literal_count": len(exact_target),
        "protected_literal_count": len(exact_protected),
    })
    return record, direction if signs_pass else None


def context_mode_name(problem, column: int) -> str:
    return problem["mode_names"][column]


def dot(left, right) -> Q:
    return sum((a * b for a, b in zip(left, right)), Q(0))


def raw_jet_atlas(context, q):
    jets, counts = atlas.raw_primitive_jets(q, context["faces"])
    require(len(jets) == 12363, "raw_jets", f"raw jet count {len(jets)}")
    require(
        counts == {
            "edge_component": 900,
            "face_component": 300,
            "in_face_turn": 33,
            "mechanics_denominator": 301,
            "support": 10529,
            "vertex_component": 300,
        },
        "raw_jets",
        f"raw jet family counts {counts}",
    )
    digest = hashlib.sha256()
    for name, value, family in jets:
        digest.update(
            f"{name}|{family}|{qs(value.v)}|{'|'.join(qs(item) for item in value.d)}\n".encode()
        )
    return jets, counts, digest.hexdigest()


def construct_strict_direction(problem, raw_jets, raw_direction):
    require(any(raw_direction), "exact_interior", "zero rationalized direction")
    homogeneous = [
        row for row in problem["literals"] if row.tau_coefficient > 0
    ]
    inhomogeneous = [
        row for row in problem["literals"] if row.tau_coefficient == 0
    ]
    require(len(homogeneous) == 38, "exact_interior", "homogeneous row count")

    literal_cap = Q(1)
    literal_cap_owner = None
    for row in inhomogeneous:
        lhs = row.lhs(raw_direction)
        if lhs > 0:
            cap = row.rhs / lhs
            if cap < literal_cap:
                literal_cap = cap
                literal_cap_owner = row

    raw_cap = Q(1)
    raw_cap_owner = None
    raw_records = []
    for name, value, family in raw_jets:
        derivative = dot(value.d, raw_direction)
        signed_derivative = derivative if value.v > 0 else -derivative
        signed_value = abs(value.v)
        if signed_derivative < 0:
            cap = signed_value / (-signed_derivative)
            if cap < raw_cap:
                raw_cap = cap
                raw_cap_owner = (name, family, value.v, derivative)
        raw_records.append((name, family, value.v, derivative))

    shrink = min(Q(1), literal_cap, raw_cap) / 2
    require(shrink > 0, "exact_interior", "non-positive analytic shrink")
    direction = tuple(shrink * value for value in raw_direction)
    tau_cap = Q(1)
    tau_cap_owner = None
    for row in homogeneous:
        directional_lhs = row.lhs(direction)
        primitive = {
            "index_zero_based": row.index,
            "name": row.name,
            "family": row.family,
            "directional_lhs_exact": qs(directional_lhs),
        }
        require(
            directional_lhs < 0,
            "exact_interior",
            "homogeneous direction is not strict",
            primitive,
        )
        cap = -directional_lhs / row.tau_coefficient
        if cap < tau_cap:
            tau_cap = cap
            tau_cap_owner = row
    tau = min(Q(1), tau_cap) / 2
    require(tau > 0, "exact_interior", "non-positive exact tau")

    raw_directional = []
    raw_linear_minimum = None
    raw_linear_owner = None
    for name, family, value, derivative in raw_records:
        final_derivative = shrink * derivative
        signed_linear = (value + final_derivative) if value > 0 else -(value + final_derivative)
        primitive = {
            "name": name,
            "family": family,
            "source_value_exact": qs(value),
            "directional_derivative_exact": qs(final_derivative),
            "signed_linearized_endpoint_exact": qs(signed_linear),
        }
        require(
            signed_linear > 0,
            "raw_jet_interior",
            "raw first-jet linearized endpoint is non-strict",
            primitive,
        )
        if raw_linear_minimum is None or signed_linear < raw_linear_minimum:
            raw_linear_minimum = signed_linear
            raw_linear_owner = (name, family)
        raw_directional.append((name, family, value, final_derivative))

    slacks = []
    for row in problem["literals"]:
        slack = row.slack(direction, tau)
        primitive = {
            "index_zero_based": row.index,
            "name": row.name,
            "family": row.family,
            "lhs_exact": qs(row.lhs(direction, tau)),
            "rhs_exact": qs(row.rhs),
            "slack_exact": qs(slack),
        }
        require(
            slack > 0,
            "literal_exact_readback",
            "literal row is not strict",
            primitive,
        )
        slacks.append((slack, row))

    groups = {}
    for family in sorted({row.family for _slack, row in slacks}):
        values = [(slack, row) for slack, row in slacks if row.family == family]
        minimum, owner = min(values, key=lambda item: item[0])
        groups[family] = {
            "count": len(values),
            "minimum_slack_exact": qs(minimum),
            "minimum_slack_decimal": float(minimum),
            "minimum_owner_index_zero_based": owner.index,
            "minimum_owner_name": owner.name,
        }
    global_minimum, global_owner = min(slacks, key=lambda item: item[0])
    return {
        "direction": direction,
        "tau": tau,
        "shrink": shrink,
        "raw_directional": raw_directional,
        "summary": {
            "rationalization": "exact Fraction.from_float of each HiGHS coefficient",
            "analytic_shrink_exact": qs(shrink),
            "literal_positive_scale_cap_exact": qs(literal_cap),
            "literal_scale_cap_owner": (
                None if literal_cap_owner is None else {
                    "index_zero_based": literal_cap_owner.index,
                    "name": literal_cap_owner.name,
                }
            ),
            "raw_12363_first_jet_scale_cap_exact": qs(raw_cap),
            "raw_scale_cap_owner": (
                None if raw_cap_owner is None else {
                    "name": raw_cap_owner[0],
                    "family": raw_cap_owner[1],
                    "source_value_exact": qs(raw_cap_owner[2]),
                    "raw_directional_derivative_exact": qs(raw_cap_owner[3]),
                }
            ),
            "exact_tau": qs(tau),
            "exact_tau_cap": qs(tau_cap),
            "tau_cap_owner": (
                None if tau_cap_owner is None else {
                    "index_zero_based": tau_cap_owner.index,
                    "name": tau_cap_owner.name,
                }
            ),
            "literal_constraint_count": len(slacks),
            "all_literal_slacks_strictly_positive": True,
            "global_minimum_literal_slack_exact": qs(global_minimum),
            "global_minimum_literal_slack_decimal": float(global_minimum),
            "global_minimum_literal_owner_index_zero_based": global_owner.index,
            "global_minimum_literal_owner_name": global_owner.name,
            "literal_family_margins": groups,
            "raw_linearized_minimum_signed_value_exact": qs(raw_linear_minimum),
            "raw_linearized_minimum_owner": {
                "name": raw_linear_owner[0],
                "family": raw_linear_owner[1],
            },
        },
    }


def exact_derivative_records(problem, direction):
    targets = []
    protected = []
    for row in problem["literals"]:
        if row.family not in {"target", "protected"}:
            continue
        normalized_derivative = dot(row.coefficients, direction)
        if row.family == "target":
            derivative = normalized_derivative * problem["targets0"][
                row.name.removeprefix("target:")
            ].v
            require(
                derivative < 0,
                "target_derivatives",
                "target derivative is not negative",
                {"name": row.name, "derivative_exact": qs(derivative)},
            )
            targets.append({
                "name": row.name.removeprefix("target:"),
                "derivative_exact": qs(derivative),
                "fractional_derivative_exact": qs(normalized_derivative),
                "fractional_derivative_decimal": float(normalized_derivative),
            })
        else:
            positive_normalized = -normalized_derivative
            identifier = row.name.removeprefix("protected:")
            source_value = problem["protected_source_by_name"][row.name]
            raw_derivative = positive_normalized * source_value
            require(
                positive_normalized > 0 and raw_derivative > 0,
                "protected_derivatives",
                "protected derivative is not positive",
                {
                    "name": identifier,
                    "normalized_derivative_exact": qs(positive_normalized),
                    "raw_derivative_exact": qs(raw_derivative),
                },
            )
            protected.append({
                "name": identifier,
                "derivative_exact": qs(raw_derivative),
                "derivative_decimal": float(raw_derivative),
                "normalized_derivative_exact": qs(positive_normalized),
                "normalized_derivative_decimal": float(positive_normalized),
            })
    require(len(targets) == 8, "target_derivatives", "target derivative count")
    require(len(protected) == 30, "protected_derivatives", "protected derivative count")
    return targets, protected


def displacement(spec, coefficients, labels):
    delta = {label: [Q(0), Q(0), Q(0)] for label in labels}
    for coefficient, (label, _name, direction) in zip(coefficients, spec):
        for axis in range(3):
            delta[label][axis] += coefficient * direction[axis]
    return {label: tuple(values) for label, values in delta.items()}


def verify_candidate(context, problem, direction):
    delta = displacement(context["spec"], direction, context["packet"]["active_vertices"])
    candidate = {
        label: pc.ex.add(point, delta.get(label, pc.ex.ZERO))
        for label, point in context["rows"].items()
    }
    prescribed_faces = pc.ex.exactify_faces(
        candidate,
        SimpleNamespace(faces=[{"cycle": list(cycle)} for cycle in context["cycles"]]),
    )
    expected_signature = pc.face_signature(context["faces"])
    require(
        pc.face_signature(prescribed_faces) == expected_signature,
        "candidate_faces",
        "prescribed candidate face signature changed",
    )
    volume, centroid = pc.ex.exact_mass(candidate, prescribed_faces)
    ef, active, fl, vl, el, stable, unstable, saddles = pc.ex.exact_mechanics(
        candidate, prescribed_faces, centroid
    )
    packet = {
        "f_vector": [len(active), len(ef), len(prescribed_faces)],
        "class": [len(stable), len(unstable), len(saddles)],
        "active_vertices": active,
        "stable_faces": [prescribed_faces[index]["cycle"] for index in stable],
        "unstable_vertices": unstable,
        "saddle_edges": [list(edge) for edge in saddles],
    }
    require(packet == context["packet"], "candidate_ledger", "mechanics packet changed")
    require(set(ef) == context["edges"], "candidate_ledger", "true edge ledger changed")
    candidate_sign_ledger = mechanics_sign_ledger(fl, vl, el)
    require(
        candidate_sign_ledger == context["mechanics_sign_ledger"],
        "candidate_ledger",
        "mechanics component sign ledger changed",
    )
    missing_rails = sorted(pc.esc.forced_rails() - set(ef))
    require(not missing_rails, "candidate_ledger", "forced rails missing", details=missing_rails)

    candidate_targets, candidate_base, candidate_u8 = chart.target_jets(
        candidate, prescribed_faces, []
    )
    target_ratios = {
        name: candidate_targets[name].v / problem["targets0"][name].v
        for name in chart.TARGET_NAMES
    }
    for name, ratio in target_ratios.items():
        require(
            Q(0) < ratio < Q(1),
            "candidate_targets",
            "candidate target did not decrease strictly",
            {"name": name, "ratio_exact": qs(ratio)},
        )
    protected = {
        **{("S", tuple(sorted(edge))): value.v for edge, value in candidate_base.items()},
        **{("U8", neighbor): value.v for neighbor, value in candidate_u8.items()},
    }
    require(set(protected) == set(problem["protected0"]), "candidate_protected", "keys")
    protected_differences = {}
    for key, value in protected.items():
        difference = value - problem["protected0"][key]
        require(
            difference > 0,
            "candidate_protected",
            "candidate protected component did not increase strictly",
            {"name": repr(key), "difference_exact": qs(difference)},
        )
        protected_differences[repr(key)] = difference
    physical_linf = max(abs(value) for xyz in delta.values() for value in xyz)
    return {
        "candidate": candidate,
        "volume": volume,
        "centroid": centroid,
        "packet": packet,
        "target_ratios": target_ratios,
        "protected_differences": protected_differences,
        "physical_linf": physical_linf,
        "face_signature_sha256": canonical_hash(
            [list(face) for face in sorted(expected_signature)]
        ),
        "mechanics_value_ledger_sha256": canonical_hash([fl, vl, el]),
        "mechanics_sign_ledger_sha256": canonical_hash(candidate_sign_ledger),
    }


def audit_polynomial(polynomial, start_sign: int):
    stack = [(Q(0), Q(1), 0)]
    leaves = 0
    minimum = None
    minimum_interval = None
    minimum_index = None
    while stack:
        left, right, depth = stack.pop()
        coefficients = locator.normalized_coefficients(
            polynomial, left, right, start_sign
        )
        if all(value > 0 for value in coefficients):
            leaves += 1
            local_minimum = min(coefficients)
            if minimum is None or local_minimum < minimum:
                minimum = local_minimum
                minimum_interval = (left, right)
                minimum_index = coefficients.index(local_minimum)
            continue
        if depth >= MAX_BERNSTEIN_DEPTH:
            return {
                "strict": False,
                "left": left,
                "right": right,
                "depth": depth,
                "coefficients": coefficients,
            }
        middle = (left + right) / 2
        stack.append((middle, right, depth + 1))
        stack.append((left, middle, depth + 1))
    return {
        "strict": True,
        "leaves": leaves,
        "minimum": minimum,
        "minimum_interval": minimum_interval,
        "minimum_index": minimum_index,
    }


def exhaustive_segment_audit(context, candidate, raw_directional, raw_jet_digest):
    path = locator.line_points(context["rows"], candidate)
    primitives = list(locator.primitive_rows(path, context["cycles"]))
    require(len(primitives) == 12363, "segment_audit", "path primitive count")
    require(len(raw_directional) == len(primitives), "segment_audit", "jet/path count")
    raw_by_key = {}
    for raw_index, raw in enumerate(raw_directional):
        raw_name, raw_family, _raw_value, _raw_derivative = raw
        key = (raw_name, raw_family)
        require(
            key not in raw_by_key,
            "segment_correspondence",
            "duplicate raw first-jet primitive key",
            details={"raw_index_zero_based": raw_index, "key": list(key)},
        )
        raw_by_key[key] = raw
    path_digest = hashlib.sha256()
    total_leaves = 0
    global_minimum = None
    global_owner = None
    family_counts = Counter()
    path_keys = set()
    for index, (name, polynomial, family) in enumerate(primitives):
        key = (name, family)
        require(
            key not in path_keys,
            "segment_correspondence",
            "duplicate path primitive key",
            details={"index_zero_based": index, "key": list(key)},
        )
        path_keys.add(key)
        require(
            key in raw_by_key,
            "segment_correspondence",
            "path primitive is absent from raw first-jet atlas",
            details={"index_zero_based": index, "key": list(key)},
        )
        raw = raw_by_key.pop(key)
        raw_name, raw_family, raw_value, raw_derivative = raw
        primitive = {
            "index_zero_based": index,
            "name": name,
            "family": family,
        }
        require((name, family) == (raw_name, raw_family), "segment_correspondence", "raw jet/path key mismatch", primitive)
        require(
            polynomial.c[0] == raw_value,
            "segment_correspondence",
            "raw jet/path source value mismatch",
            {
                **primitive,
                "jet_value_exact": qs(raw_value),
                "path_value_exact": qs(polynomial.c[0]),
            },
        )
        path_derivative = polynomial.c[1] if len(polynomial.c) > 1 else Q(0)
        require(
            path_derivative == raw_derivative,
            "segment_correspondence",
            "raw jet/path derivative mismatch",
            {
                **primitive,
                "jet_derivative_exact": qs(raw_derivative),
                "path_derivative_exact": qs(path_derivative),
            },
        )
        start_sign = 1 if raw_value > 0 else -1
        result = audit_polynomial(polynomial, start_sign)
        if not result["strict"]:
            failed = {
                **primitive,
                "start_sign": start_sign,
                "failed_interval_exact": [qs(result["left"]), qs(result["right"])],
                "depth": result["depth"],
                "normalized_bernstein_coefficients_exact": [
                    qs(value) for value in result["coefficients"]
                ],
            }
            raise ContractFailure(
                "segment_audit",
                "12,363-primitive segment is not strictly certified",
                failed,
            )
        total_leaves += result["leaves"]
        family_counts[family] += 1
        if global_minimum is None or result["minimum"] < global_minimum:
            global_minimum = result["minimum"]
            global_owner = {
                **primitive,
                "interval_exact": [
                    qs(result["minimum_interval"][0]),
                    qs(result["minimum_interval"][1]),
                ],
                "coefficient_index": result["minimum_index"],
            }
        path_digest.update(
            f"{name}|{family}|{'|'.join(polynomial.exact())}\n".encode()
        )
    require(
        not raw_by_key,
        "segment_correspondence",
        "raw first-jet atlas contains primitives absent from the path enumeration",
        details={"remaining_keys": [list(key) for key in sorted(raw_by_key)]},
    )
    require(
        dict(family_counts)
        == {
            "mechanics_denominator": 301,
            "support": 10529,
            "in_face_turn": 33,
            "face_component": 300,
            "vertex_component": 300,
            "edge_component": 900,
        },
        "segment_audit",
        f"path primitive family counts {dict(family_counts)}",
    )
    return {
        "raw_first_jet_sha256": raw_jet_digest,
        "raw_first_jet_to_path_unique_key_bijection": True,
        "raw_first_jet_to_path_value_and_derivative_correspondence": True,
        "primitive_count": len(primitives),
        "family_counts": dict(family_counts),
        "strict_parameter_interval_exact": ["0", "1"],
        "exact_pre_event_step": "1",
        "all_normalized_bernstein_coefficients_strictly_positive": True,
        "bernstein_leaf_count": total_leaves,
        "minimum_normalized_bernstein_coefficient_exact": qs(global_minimum),
        "minimum_normalized_bernstein_coefficient_decimal": float(global_minimum),
        "minimum_owner": global_owner,
        "path_primitive_sha256": path_digest.hexdigest(),
        "maximum_subdivision_depth": MAX_BERNSTEIN_DEPTH,
    }


def candidate_csv_bytes(candidate) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream)
    writer.writerow(["source_id", "x_exact", "y_exact", "z_exact", "x", "y", "z"])
    for label, point in sorted(candidate.items()):
        writer.writerow([
            label,
            *(qs(value) for value in point),
            *(format(float(value), ".17g") for value in point),
        ])
    return stream.getvalue().encode()


def run():
    clear_candidate_outputs()
    context = load_context()
    branch_records = []
    selected_problem = build_literal_problem(context, PREFERRED_TRUST)
    selected_problem["mode_names"] = [
        name for _row, name, _direction in context["spec"]
    ]
    selected_direction = None
    for trust in TRUSTS:
        problem = problem_with_trust(selected_problem, trust)
        record, direction = solve_literal_problem(problem, trust)
        branch_records.append(record)
        if trust == PREFERRED_TRUST:
            selected_direction = direction
    preferred_record = next(
        record for record in branch_records
        if Q(record["trust_exact"]) == PREFERRED_TRUST
    )
    require(
        preferred_record["solver_success"],
        "solver",
        "row-equilibrated preferred branch did not solve",
        details=preferred_record,
    )
    require(
        selected_direction is not None,
        "solver_exact_readback",
        "preferred branch failed exact homogeneous sign readback",
        details=preferred_record,
    )

    raw_jets, raw_counts, raw_jet_digest = raw_jet_atlas(
        context, selected_problem["q"]
    )
    strict = construct_strict_direction(
        selected_problem, raw_jets, selected_direction
    )
    targets, protected = exact_derivative_records(
        selected_problem, strict["direction"]
    )
    candidate_record = verify_candidate(
        context, selected_problem, strict["direction"]
    )
    raw_directional = strict.pop("raw_directional")
    del raw_jets
    del selected_problem["q"]
    gc.collect()
    segment = exhaustive_segment_audit(
        context,
        candidate_record["candidate"],
        raw_directional,
        raw_jet_digest,
    )

    csv_data = candidate_csv_bytes(candidate_record["candidate"])
    csv_hash = sha256_bytes(csv_data)
    source_hashes = {
        relative(path): EXPECTED_FILES[path][1]
        for path in (SOURCE, FACES_PATH, SOURCE_CERTIFICATE, SOURCE_VERIFICATION)
    }
    proposal = {
        "version": 1,
        "scope": "strict rational exact-interior F21 proposal in the accepted F20 post-transfer cell",
        "stage": "F21",
        "parent_stage": "F20",
        "source_hashes": source_hashes,
        "source_bytes": {
            relative(path): EXPECTED_FILES[path][0]
            for path in (SOURCE, FACES_PATH, SOURCE_CERTIFICATE, SOURCE_VERIFICATION)
        },
        "owner_code_snapshot": context["owner_code_snapshot"],
        "chart_sha256": EXPECTED_FILES[CHART_PATH][1],
        "chart_bytes": EXPECTED_FILES[CHART_PATH][0],
        "source_certificate_verdict": EXPECTED_SOURCE_VERDICT,
        "source_verification_verdict": EXPECTED_SOURCE_VERIFICATION_VERDICT,
        "chart_verdict": EXPECTED_CHART_VERDICT,
        "mode_count": 150,
        "mode_names": [name for _row, name, _direction in context["spec"]],
        "complete_raw_first_jet_primitive_count": 12363,
        "complete_raw_first_jet_family_counts": raw_counts,
        "complete_raw_first_jet_sha256": raw_jet_digest,
        "mechanics_guard_count": len(selected_problem["mechanics"]),
        "support_guard_summary": selected_problem["support_summary"],
        "literal_constraint_count": 1048,
        "literal_constraint_family_counts": selected_problem["family_counts"],
        "literal_matrix_sha256": selected_problem["literal_matrix_sha256"],
        "expected_literal_matrix_sha256": EXPECTED_LITERAL_MATRIX_SHA256,
        "branches": branch_records,
        "selected_branch": preferred_record,
        "selection_policy": "exactly the diagnosed trust=1e-5 branch; no fallback branch selection",
        "exact_coefficients": [qs(value) for value in strict["direction"]],
        "exact_common_fractional_descent": qs(strict["tau"]),
        "exact_interior_certificate": {
            **strict["summary"],
            "target_derivatives": targets,
            "target_derivative_count": len(targets),
            "all_target_derivatives_strictly_negative": True,
            "protected_derivatives": protected,
            "protected_derivative_count": len(protected),
            "all_protected_derivatives_strictly_positive": True,
        },
        "exhaustive_same_cell_segment": segment,
        "locator_contract": {
            "formula": "q_i(t)=source_i+t*(endpoint_i-source_i)",
            "source": relative(SOURCE),
            "endpoint": relative(ENDPOINT),
            "proposal": relative(OUTPUT),
            "faces": relative(FACES_PATH),
            "expected_proposal_verdict": PROPOSAL_VERDICT,
            "exact_certified_pre_event_step": "1",
            "main_agent_must_still_run_first_event_locator_and_event_certificate": True,
        },
        "candidate": {
            "csv": relative(ENDPOINT),
            "csv_sha256": csv_hash,
            "csv_bytes": len(csv_data),
            "f_vector": candidate_record["packet"]["f_vector"],
            "class": candidate_record["packet"]["class"],
            "stable_faces": candidate_record["packet"]["stable_faces"],
            "unstable_vertices": candidate_record["packet"]["unstable_vertices"],
            "saddle_edges": candidate_record["packet"]["saddle_edges"],
            "face_signature_sha256": candidate_record["face_signature_sha256"],
            "mechanics_value_ledger_sha256": candidate_record[
                "mechanics_value_ledger_sha256"
            ],
            "mechanics_sign_ledger_sha256": candidate_record[
                "mechanics_sign_ledger_sha256"
            ],
            "same_exact_face_edge_combinatorics_and_mechanics_sign_cell": True,
            "volume_exact": qs(candidate_record["volume"]),
            "centroid_exact": [qs(value) for value in candidate_record["centroid"]],
            "physical_linf_exact": qs(candidate_record["physical_linf"]),
            "physical_linf_decimal": float(candidate_record["physical_linf"]),
            "target_ratios_exact": {
                name: qs(value) for name, value in candidate_record["target_ratios"].items()
            },
            "target_ratios_decimal": {
                name: float(value) for name, value in candidate_record["target_ratios"].items()
            },
            "protected_component_count": len(candidate_record["protected_differences"]),
            "protected_components_increased_strictly_exactly": True,
            "minimum_protected_endpoint_increase_exact": qs(
                min(candidate_record["protected_differences"].values())
            ),
            "all_37_forced_rails_present": True,
        },
        "verdict": PROPOSAL_VERDICT,
        "exact_interior_verdict": EXACT_INTERIOR_VERDICT,
        "proof_status": "EXACT_STRICT_INTERIOR_ENDPOINT_AND_PRE_EVENT_SEGMENT_ONLY_FIRST_EVENT_NOT_YET_CERTIFIED",
        "winner_status": "NONWINNER_PROPOSAL_ONLY",
    }
    proposal_data = (json.dumps(proposal, indent=2) + "\n").encode()
    atomic_bytes(ENDPOINT, csv_data)
    atomic_bytes(OUTPUT, proposal_data)
    require(
        ENDPOINT.read_bytes() == csv_data,
        "writeback",
        "candidate byte readback mismatch",
    )
    require(
        OUTPUT.read_bytes() == proposal_data,
        "writeback",
        "proposal byte readback mismatch",
    )
    receipt_payload = {
        "version": 1,
        "scope": "bounded F21 exact-interior proposer receipt",
        "status": "PASS",
        "verdict": EXACT_INTERIOR_VERDICT,
        "lineage": context["lineage"],
        "owner_code_snapshot": context["owner_code_snapshot"],
        "outputs": {
            relative(ENDPOINT): {
                "bytes": ENDPOINT.stat().st_size,
                "sha256": sha256(ENDPOINT),
            },
            relative(OUTPUT): {
                "bytes": OUTPUT.stat().st_size,
                "sha256": sha256(OUTPUT),
            },
        },
        "strict_margin_summary": {
            "target_derivatives_strictly_negative": len(targets),
            "protected_derivatives_strictly_positive": len(protected),
            "literal_constraints_strict": strict["summary"]["literal_constraint_count"],
            "minimum_literal_slack_exact": strict["summary"]["global_minimum_literal_slack_exact"],
            "minimum_literal_slack_owner": strict["summary"]["global_minimum_literal_owner_name"],
            "raw_primitives_strict_on_exact_step_0_to_1": segment["primitive_count"],
            "minimum_bernstein_coefficient_exact": segment[
                "minimum_normalized_bernstein_coefficient_exact"
            ],
            "exact_pre_event_step": segment["exact_pre_event_step"],
            "same_exact_face_edge_combinatorics_and_mechanics_sign_cell": True,
            "all_37_forced_rails_present": True,
        },
        "claim_boundary": (
            "Valid exact-interior proposal candidate only. F21 is not accepted; "
            "the independent first-event locator and event-cell certificate remain required."
        ),
    }
    atomic_json(RECEIPT, receipt_payload)
    print(EXACT_INTERIOR_VERDICT)
    print("candidate_sha256", sha256(ENDPOINT))
    print("proposal_sha256", sha256(OUTPUT))
    print("receipt_sha256", sha256(RECEIPT))


def main():
    RECEIPT.unlink(missing_ok=True)
    try:
        run()
    except Exception as error:
        clear_candidate_outputs()
        if isinstance(error, ContractFailure):
            failure = {
                "stage": error.stage,
                "message": str(error),
                "first_violated_exact_primitive": error.primitive,
                "details": error.details,
            }
        else:
            failure = {
                "stage": "unexpected_exception",
                "message": repr(error),
                "first_violated_exact_primitive": None,
                "details": {"traceback": traceback.format_exc()},
            }
        receipt_payload = {
            "version": 1,
            "scope": "bounded F21 exact-interior proposer receipt",
            "status": "FAIL",
            "verdict": NO_PROPOSAL_VERDICT,
            "candidate_created": False,
            "failure": failure,
            "claim_boundary": "Fail closed; no proposal candidate was retained.",
        }
        atomic_json(RECEIPT, receipt_payload)
        print(NO_PROPOSAL_VERDICT, file=sys.stderr)
        print(json.dumps(failure, indent=2), file=sys.stderr)
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()
