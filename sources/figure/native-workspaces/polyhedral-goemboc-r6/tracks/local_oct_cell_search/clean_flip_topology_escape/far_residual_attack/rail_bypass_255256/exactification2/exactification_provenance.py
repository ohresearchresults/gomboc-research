#!/usr/bin/env python3
"""Fail-closed provenance schema and local trust anchor for exactification2.

This module is the explicit local trust boundary for the four exactification
entrypoints.  It pins their byte hashes and the clean verifier dependency,
loads files from immutable byte snapshots, rejects aliases/hard links and path
escapes, and supplies fixed artifact schemas.

The anchor is intentionally honest about its limit: a party able to modify this
file *and* the consuming entrypoint can replace the pins and policy.  Preventing
that requires an external signature or immutable checkout outside this mutable
workspace.  Within that boundary, changing only an entrypoint, verifier module,
artifact, alias, or path is fail-closed.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import stat
import sys
import tempfile
import types
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path


TRUST_SCHEMA = "polyhedral-goemboc.exactification.local-trust/v2"
TRUST_VERSION = 2
TRUST_BOUNDARY = (
    "Read-once local byte snapshots rooted in exactification_provenance.py pin the "
    "complete transitive local executable closure for each role. Dependencies are "
    "compiled and executed from the same bytes that are hashed. The mutable workspace "
    "must remain quiescent for the process lifetime; metadata checks detect ordinary "
    "concurrent replacement. This is not a signature against coordinated replacement "
    "of the helper, callers, pins, and artifacts in the whole mutable workspace."
)

HELPER_RELATIVE = (
    "tracks/local_oct_cell_search/clean_flip_topology_escape/far_residual_attack/"
    "rail_bypass_255256/exactification2/exactification_provenance.py"
)
ROLE_ENTRYPOINTS = {
    "search": (
        "tracks/local_oct_cell_search/clean_flip_topology_escape/far_residual_attack/"
        "rail_bypass_255256/exactification2/search_exact_first_jet_full_chart.py"
    ),
    "diagnose": (
        "tracks/local_oct_cell_search/clean_flip_topology_escape/far_residual_attack/"
        "rail_bypass_255256/exactification2/diagnose_full_chart_derivative_horizon.py"
    ),
    "builder": (
        "tracks/local_oct_cell_search/clean_flip_topology_escape/far_residual_attack/"
        "rail_bypass_255256/exactification2/build_exactification_certificate.py"
    ),
    "verifier": (
        "tracks/local_oct_cell_search/clean_flip_topology_escape/far_residual_attack/"
        "rail_bypass_255256/exactification2/verify_exactification_certificate.py"
    ),
}

ROLE_DEPENDENCIES = {
    "search": (
        ("exact_core", "tracks/global_carrier_support/rigorous_local_bypass/exact_core.py"),
        (
            "grouped_exact",
            "tracks/target_sphere_realizer/grouped_local_escape/rigorous_null_bypass/"
            "grouped_exact.py",
        ),
        (
            "actual_grouped",
            "tracks/target_sphere_realizer/grouped_local_escape/actual_grouped.py",
        ),
        (
            "row54_four_residual_search",
            "tracks/circuit_atlas/row54_four_residual_search.py",
        ),
        (
            "row54_full_minimax",
            "tracks/target_sphere_realizer/grouped_local_escape/row54_full_minimax.py",
        ),
        (
            "build_certificate",
            "tracks/local_oct_cell_search/clean_flip_topology_escape/build_certificate.py",
        ),
        (
            "attack_common",
            "tracks/local_oct_cell_search/clean_flip_topology_escape/far_residual_attack/"
            "attack_common.py",
        ),
        ("build_exactification_certificate", ROLE_ENTRYPOINTS["builder"]),
    ),
    "diagnose": (
        ("exact_core", "tracks/global_carrier_support/rigorous_local_bypass/exact_core.py"),
        ("build_exactification_certificate", ROLE_ENTRYPOINTS["builder"]),
    ),
    "builder": (
        ("exact_core", "tracks/global_carrier_support/rigorous_local_bypass/exact_core.py"),
    ),
    "verifier": (
        (
            "clean_local_oct_exact",
            "tracks/local_oct_cell_search/clean_flip_topology_escape/far_residual_attack/"
            "verify_exact_event_certificate.py",
        ),
    ),
}

# The helper is the deliberately non-circular local anchor. Every other local
# executable byte file is pinned here. Entry-point placeholders are replaced only
# after the five owned files reach their final reviewed bytes.
EXPECTED_CODE_SHA256 = {
    ROLE_ENTRYPOINTS["search"]: "4a053239642a09f1dd2236e9cc8c8fd28152cf0ba4b81b7965c27858276c32e2",
    ROLE_ENTRYPOINTS["diagnose"]: "40c78f9981990ee5ad29b79d0ba47872d6dda05d686082dd4f52f4fb28a78d7b",
    ROLE_ENTRYPOINTS["builder"]: "bfbe9e9b6fbe400089238500a52c854b1a01803f61a4f35c91673f155a26ac5d",
    ROLE_ENTRYPOINTS["verifier"]: "b418b537087e0464a1fcb4d500fec38f1bd4e8a9e8b731645b86b1a003e23407",
    "tracks/global_carrier_support/rigorous_local_bypass/exact_core.py": (
        "d2d69ce6e4ddefd2ab7171b7e61bd09ae12846eaf509f61dd25be6d9bbb235dd"
    ),
    "tracks/target_sphere_realizer/grouped_local_escape/rigorous_null_bypass/"
    "grouped_exact.py": "bb6c4615ff4a37888cf0bfbd102f31757ac9315b938dc039261c20a7b0dd135a",
    "tracks/target_sphere_realizer/grouped_local_escape/actual_grouped.py": (
        "a5b605dc3b8b836e1443f086d10e85c3f16f2fe5beb60eb81ad04c9692b6a532"
    ),
    "tracks/circuit_atlas/row54_four_residual_search.py": (
        "beca7d3302c553b45bdff13fe23fe71e010990f447ce6602efefa43d93b5be4f"
    ),
    "tracks/target_sphere_realizer/grouped_local_escape/row54_full_minimax.py": (
        "91793ff236237221d219f9475e5d47127cced655817b7f1e4b02a211f0e634c3"
    ),
    "tracks/local_oct_cell_search/clean_flip_topology_escape/build_certificate.py": (
        "a2075f9fa7c8354942b47daaff176cc1bc1379d81bfe2739c2c3a15cd73bee62"
    ),
    "tracks/local_oct_cell_search/clean_flip_topology_escape/far_residual_attack/"
    "attack_common.py": "47306a4e2f5c5c967278ff665b3d78c0d576a312507fcb63e590e88e58e5fbc4",
    "tracks/local_oct_cell_search/clean_flip_topology_escape/far_residual_attack/"
    "verify_exact_event_certificate.py": (
        "5498478e54cc26f94ad61888113f0e1af90ba400048614933499559676b6c4ac"
    ),
}

FIRST_JET_PATH_SCHEMA = "polyhedral-goemboc.exactification.first-jet-path/v3"
FIRST_JET_PATH_VERSION = 3
FIRST_JET_PATH_TYPE = (
    "exact rational full-chart velocity with seven strict analytic first jets"
)
FIRST_JET_PATH_VERDICT = "EXACT_TARGET_FIRST_JET_FULL_CHART_PATH_PASS"
FIRST_JET_SEARCH_VERDICT = "EXACT_TARGET_FIRST_JET_FULL_CHART_PRIMAL_FOUND"

FIRST_JET_CONTRACT_SCHEMA = "polyhedral-goemboc.exactification.first-jet-contract/v1"
FIRST_JET_CONTRACT_VERSION = 1

DIAGNOSTIC_SCHEMA = "polyhedral-goemboc.exactification.derivative-horizon/v3"
DIAGNOSTIC_VERSION = 3
DIAGNOSTIC_TYPE = "exact seven-row derivative-horizon diagnostic"
DIAGNOSTIC_VERDICT = "EXACT_FULL_CHART_FIRST_DERIVATIVE_HORIZON_ISOLATED"

CERTIFIED_PATH_SCHEMA = "polyhedral-goemboc.exactification.certified-path/v4"
CERTIFIED_PATH_VERSION = 4
CERTIFIED_PATH_TYPE = (
    "exact rational full-chart velocity with certified seven-derivative substep"
)
CERTIFIED_PATH_VERDICT = "EXACT_FULL_CHART_CERTIFIED_SUBSTEP_PATH_PASS"

CERTIFICATE_SCHEMA = "polyhedral-goemboc.exactification.material-step-certificate/v3"
CERTIFICATE_VERSION = 3
CERTIFICATE_TYPE = "exact nonzero material-step certificate"
CERTIFICATE_VERDICT = "EXACT_LOCAL_OCT_RAIL255256_FULL_CONTROL_MATERIAL_STEP_PASS"

VERIFICATION_SCHEMA = "polyhedral-goemboc.exactification.material-step-receipt/v3"
VERIFICATION_VERSION = 3
VERIFICATION_TYPE = "independent clean-room verification of exactified rail-bypass step"
VERIFICATION_VERDICT = (
    "INDEPENDENT_EXACT_LOCAL_OCT_RAIL255256_FULL_CONTROL_MATERIAL_STEP_PASS"
)

LINEAGE_SCHEMA = "polyhedral-goemboc.exactification.dynamic-source-lineage/v3"
LINEAGE_VERSION = 3

SEARCH_RESULT_SCHEMA = "polyhedral-goemboc.exactification.first-jet-search-result/v1"
SEARCH_RESULT_VERSION = 1
SEARCH_SUCCESS_TYPE = "exact first-jet full-chart search success"
SEARCH_FAILURE_TYPE = "exact first-jet full-chart search failure"
SEARCH_FAILURE_VERDICT = "NO_EXACT_TARGET_FIRST_JET_PRIMAL_IN_DECLARED_TRUST_GRID"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_hash(value) -> str:
    return sha256_bytes(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    )


@dataclass(frozen=True)
class Snapshot:
    path: Path
    data: bytes
    sha256: str
    device: int
    inode: int
    size: int
    mtime_ns: int
    nlink: int


_EXECUTABLE_SNAPSHOTS: dict[Path, Snapshot] = {}


def _fingerprint(row) -> tuple[int, int, int, int, int]:
    return (row.st_dev, row.st_ino, row.st_size, row.st_mtime_ns, row.st_nlink)


def _assert_regular_single_link(path: Path, row) -> None:
    if not stat.S_ISREG(row.st_mode):
        raise ValueError(f"not a regular file: {path}")
    if row.st_nlink != 1:
        raise ValueError(f"unexpected hard-link count {row.st_nlink}: {path}")


def read_snapshot(path: Path) -> Snapshot:
    path = Path(path)
    flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
    try:
        descriptor = os.open(path, flags)
    except OSError as exc:
        raise ValueError(f"cannot open immutable regular-file snapshot: {path}") from exc
    try:
        before = os.fstat(descriptor)
        _assert_regular_single_link(path, before)
        chunks = []
        while True:
            chunk = os.read(descriptor, 1024 * 1024)
            if not chunk:
                break
            chunks.append(chunk)
        after = os.fstat(descriptor)
        if _fingerprint(before) != _fingerprint(after):
            raise RuntimeError(f"file changed during snapshot read: {path}")
        data = b"".join(chunks)
        if len(data) != after.st_size:
            raise RuntimeError(f"short snapshot read: {path}")
        return Snapshot(
            path=path,
            data=data,
            sha256=sha256_bytes(data),
            device=after.st_dev,
            inode=after.st_ino,
            size=after.st_size,
            mtime_ns=after.st_mtime_ns,
            nlink=after.st_nlink,
        )
    finally:
        os.close(descriptor)


def _absolute(path: Path) -> Path:
    return Path(os.path.abspath(Path(path)))


def _assert_snapshot_metadata_current(snapshot: Snapshot) -> None:
    flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
    try:
        descriptor = os.open(snapshot.path, flags)
    except OSError as exc:
        raise RuntimeError(f"snapshotted file is no longer openable: {snapshot.path}") from exc
    try:
        current = os.fstat(descriptor)
        _assert_regular_single_link(snapshot.path, current)
    finally:
        os.close(descriptor)
    if _fingerprint(current) != (
        snapshot.device,
        snapshot.inode,
        snapshot.size,
        snapshot.mtime_ns,
        snapshot.nlink,
    ):
        raise RuntimeError(f"file changed after immutable snapshot: {snapshot.path}")


def assert_snapshot_current(snapshot: Snapshot) -> None:
    executable = _EXECUTABLE_SNAPSHOTS.get(_absolute(snapshot.path))
    if executable is not None:
        if executable != snapshot:
            raise RuntimeError(f"executable snapshot identity drift: {snapshot.path}")
        _assert_snapshot_metadata_current(snapshot)
        return
    current = read_snapshot(snapshot.path)
    if current != snapshot:
        raise RuntimeError(f"file changed after immutable snapshot: {snapshot.path}")


def assert_snapshots_current(snapshots) -> None:
    seen = set()
    for snapshot in snapshots:
        key = (snapshot.device, snapshot.inode, snapshot.path)
        if key in seen:
            continue
        seen.add(key)
        assert_snapshot_current(snapshot)


def _reject_parent_segments(path: Path, context: str) -> None:
    if ".." in path.parts:
        raise ValueError(f"{context}: parent traversal is forbidden: {path}")


def contained_path(value, *, base: Path, root: Path, context: str) -> Path:
    raw = Path(value)
    _reject_parent_segments(raw, context)
    candidate = raw if raw.is_absolute() else Path(base) / raw
    absolute = Path(os.path.abspath(candidate))
    resolved = candidate.resolve(strict=False)
    if resolved != absolute:
        raise ValueError(f"{context}: symlink or noncanonical path: {candidate}")
    root = Path(root).resolve(strict=True)
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"{context}: path escapes ROOT: {resolved}") from exc
    return resolved


def stored_path(value, *, root: Path, context: str, must_exist: bool = True) -> Path:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{context}: stored path must be a nonempty string")
    relative = Path(value)
    if relative.is_absolute():
        raise ValueError(f"{context}: stored path must be relative")
    _reject_parent_segments(relative, context)
    path = contained_path(relative, base=root, root=root, context=context)
    canonical = path.relative_to(Path(root).resolve(strict=True)).as_posix()
    if canonical != value:
        raise ValueError(f"{context}: stored path is not canonical: {value}")
    if must_exist and not path.is_file():
        raise ValueError(f"{context}: stored file is missing: {path}")
    return path


def relative_name(path: Path, root: Path) -> str:
    path = contained_path(path, base=root, root=root, context="relative path")
    return path.relative_to(Path(root).resolve(strict=True)).as_posix()


def assert_isolated(paths, context: str) -> None:
    paths = [Path(path) for path in paths]
    if len(set(paths)) != len(paths):
        raise ValueError(f"{context}: duplicate canonical path")
    existing = []
    for path in paths:
        if path.is_symlink():
            raise ValueError(f"{context}: symlink is forbidden: {path}")
        if path.exists():
            row = path.stat()
            _assert_regular_single_link(path, row)
            existing.append(path)
    for index, left in enumerate(existing):
        for right in existing[index + 1:]:
            if left.samefile(right):
                raise ValueError(f"{context}: same-inode alias: {left} == {right}")


def _json_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def parse_json(snapshot: Snapshot):
    try:
        return json.loads(snapshot.data.decode("utf-8"), object_pairs_hook=_json_object)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"invalid UTF-8 JSON: {snapshot.path}") from exc


def json_bytes(value) -> bytes:
    return (json.dumps(value, indent=2) + "\n").encode("utf-8")


def parse_exact_csv(snapshot: Snapshot):
    rows = {}
    stream = io.StringIO(snapshot.data.decode("utf-8"), newline="")
    reader = csv.DictReader(stream)
    if reader.fieldnames != ["source_id", "x", "y", "z"]:
        raise ValueError(f"invalid exact CSV header: {snapshot.path}")
    for row in reader:
        label = int(row["source_id"])
        if label in rows:
            raise ValueError(f"duplicate exact CSV source_id {label}: {snapshot.path}")
        rows[label] = tuple(Q(row[key]) for key in ("x", "y", "z"))
    if not rows:
        raise ValueError(f"empty exact CSV: {snapshot.path}")
    return rows


def exact_csv_bytes(points) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerow(("source_id", "x", "y", "z"))
    for label in sorted(points):
        writer.writerow((label, *(fraction_string(value) for value in points[label])))
    return stream.getvalue().encode("utf-8")


def fraction_string(value: Q) -> str:
    value = Q(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def atomic_write_bytes(path: Path, data: bytes) -> Snapshot:
    path = Path(path)
    if not path.parent.is_dir():
        raise ValueError(f"output parent directory is missing: {path.parent}")
    if path.is_symlink():
        raise ValueError(f"refusing to replace symlink output: {path}")
    if path.exists():
        _assert_regular_single_link(path, path.stat())
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        offset = 0
        while offset < len(data):
            offset += os.write(descriptor, data[offset:])
        os.fsync(descriptor)
        os.close(descriptor)
        descriptor = -1
        os.chmod(temporary, 0o644)
        os.replace(temporary, path)
        directory = os.open(path.parent, os.O_RDONLY | getattr(os, "O_CLOEXEC", 0))
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        if temporary.exists():
            temporary.unlink()
    snapshot = read_snapshot(path)
    if snapshot.data != data:
        raise RuntimeError(f"atomic output readback mismatch: {path}")
    return snapshot


def atomic_write_json(path: Path, value) -> Snapshot:
    return atomic_write_bytes(path, json_bytes(value))


def require_header(document, *, schema: str, version: int, type_name: str, verdict: str) -> None:
    if not isinstance(document, dict):
        raise AssertionError("artifact must be a JSON object")
    expected = {
        "schema": schema,
        "version": version,
        "type": type_name,
        "verdict": verdict,
    }
    got = {key: document.get(key) for key in expected}
    if got != expected:
        raise AssertionError(("fixed artifact header mismatch", got, expected))


def require_search_result(document, *, root: Path) -> None:
    if not isinstance(document, dict):
        raise AssertionError("search result must be a JSON object")
    common = {
        "schema",
        "version",
        "type",
        "verdict",
        "source_sha256",
        "faces_sha256",
        "exact_target_jacobian_digest",
        "scenarios",
        "producer_trust",
    }
    verdict = document.get("verdict")
    if verdict == FIRST_JET_SEARCH_VERDICT:
        type_name = SEARCH_SUCCESS_TYPE
        fields = common | {
            "proof_status",
            "mode_count",
            "selected",
            "exact_selected_coefficients",
            "exact_first_jet_good_margins",
            "exact_endpoint",
            "path_definition",
            "next_action",
        }
        if document.get("proof_status") != (
            "FIRST_JET_ONLY_COMPLETE_INTERVAL_CERTIFICATE_REQUIRED"
        ):
            raise AssertionError("search success proof-status mismatch")
        if document.get("next_action") != (
            "Run the complete exact 7904-primitive interval builder and clean verifier."
        ):
            raise AssertionError("search success next-action mismatch")
    elif verdict == SEARCH_FAILURE_VERDICT:
        type_name = SEARCH_FAILURE_TYPE
        fields = common
    else:
        raise AssertionError(("unknown search result verdict", verdict))
    if "source_lineage" in document:
        fields = fields | {"source_lineage"}
    if set(document) != fields:
        raise AssertionError(
            ("search result exact field schema mismatch", sorted(document), sorted(fields))
        )
    require_header(
        document,
        schema=SEARCH_RESULT_SCHEMA,
        version=SEARCH_RESULT_VERSION,
        type_name=type_name,
        verdict=verdict,
    )
    require_trust_packet(document.get("producer_trust"), root=root, role="search")


def require_paired_fields(document, left: str, right: str) -> bool:
    has_left = left in document
    has_right = right in document
    if has_left != has_right:
        raise AssertionError(f"{left} and {right} must appear together")
    return has_left


def require_exact_document(got, expected, context: str) -> None:
    if got != expected:
        raise AssertionError(f"{context}: exact document mismatch")


def _helper_directory() -> Path:
    return Path(__file__).resolve().parent


def role_path(root: Path, role: str) -> Path:
    if role not in ROLE_ENTRYPOINTS:
        raise ValueError(f"unknown trust role: {role}")
    return contained_path(
        Path(root) / ROLE_ENTRYPOINTS[role],
        base=root,
        root=root,
        context=f"{role} entrypoint",
    )


def clean_module_path(root: Path) -> Path:
    relative = dict(ROLE_DEPENDENCIES["verifier"])["clean_local_oct_exact"]
    return contained_path(
        Path(root) / relative,
        base=root,
        root=root,
        context="clean verifier module",
    )


def _code_path(root: Path, relative: str, context: str) -> Path:
    return contained_path(
        Path(root) / relative,
        base=root,
        root=root,
        context=context,
    )


@dataclass(frozen=True)
class TrustedCodeContext:
    root: Path
    role: str
    anchor: Snapshot
    entrypoint: Snapshot
    dependencies: tuple[tuple[str, Snapshot], ...]
    modules: dict[str, types.ModuleType]

    @property
    def snapshots(self) -> tuple[Snapshot, ...]:
        return (
            self.anchor,
            self.entrypoint,
            *(snapshot for _name, snapshot in self.dependencies),
        )

    def dependency_snapshot(self, name: str) -> Snapshot:
        for module_name, snapshot in self.dependencies:
            if module_name == name:
                return snapshot
        raise KeyError(name)


_ACTIVE_CONTEXTS: dict[tuple[Path, str], TrustedCodeContext] = {}


def _register_executable(snapshot: Snapshot) -> None:
    key = _absolute(snapshot.path)
    prior = _EXECUTABLE_SNAPSHOTS.get(key)
    if prior is not None and prior != snapshot:
        raise RuntimeError(f"executable byte snapshot changed in-process: {snapshot.path}")
    _EXECUTABLE_SNAPSHOTS[key] = snapshot


def _local_module_paths(root: Path) -> set[Path]:
    paths = set()
    for module in tuple(sys.modules.values()):
        value = getattr(module, "__file__", None)
        if not value:
            continue
        try:
            path = Path(value).resolve(strict=False)
            path.relative_to(root)
        except (OSError, ValueError):
            continue
        if path.suffix == ".py":
            paths.add(path)
    return paths


def activate_role(root: Path, role: str) -> TrustedCodeContext:
    root = Path(root).resolve(strict=True)
    if role not in ROLE_ENTRYPOINTS:
        raise ValueError(f"unknown trust role: {role}")
    key = (root, role)
    if key in _ACTIVE_CONTEXTS:
        return _ACTIVE_CONTEXTS[key]
    if _ACTIVE_CONTEXTS:
        active = next(iter(_ACTIVE_CONTEXTS.values()))
        raise RuntimeError(
            f"process already bound to {active.role}; refusing second trust role {role}"
        )

    helper_path = _code_path(root, HELPER_RELATIVE, "provenance helper")
    if helper_path != Path(__file__).resolve():
        raise RuntimeError("imported provenance helper is outside the authoritative closure")
    anchor = read_snapshot(helper_path)
    entrypoint = read_snapshot(role_path(root, role))
    dependency_rows = []
    for module_name, relative in ROLE_DEPENDENCIES[role]:
        dependency_rows.append(
            (
                module_name,
                read_snapshot(_code_path(root, relative, f"{role} dependency {module_name}")),
            )
        )

    expected_entrypoint = EXPECTED_CODE_SHA256[ROLE_ENTRYPOINTS[role]]
    if entrypoint.sha256 != expected_entrypoint:
        raise RuntimeError(
            f"untrusted {role} entrypoint hash {entrypoint.sha256}; "
            f"expected {expected_entrypoint}"
        )
    for (module_name, relative), (_loaded_name, snapshot) in zip(
        ROLE_DEPENDENCIES[role], dependency_rows
    ):
        expected = EXPECTED_CODE_SHA256.get(relative)
        if expected is None or snapshot.sha256 != expected:
            raise RuntimeError(
                f"untrusted {role} dependency {module_name} hash {snapshot.sha256}; "
                f"expected {expected}"
            )

    snapshots = (anchor, entrypoint, *(row[1] for row in dependency_rows))
    assert_isolated((snapshot.path for snapshot in snapshots), f"{role} code closure")
    for snapshot in snapshots:
        _register_executable(snapshot)
        _assert_snapshot_metadata_current(snapshot)

    before_local = _local_module_paths(root)
    modules: dict[str, types.ModuleType] = {}
    inserted = []
    try:
        for module_name, snapshot in dependency_rows:
            if module_name in sys.modules:
                raise RuntimeError(f"local dependency was imported before trust binding: {module_name}")
            module = types.ModuleType(module_name)
            module.__file__ = str(snapshot.path)
            module.__package__ = ""
            module.__loader__ = None
            module.__spec__ = None
            modules[module_name] = module
            sys.modules[module_name] = module
            inserted.append(module_name)
        for module_name, snapshot in dependency_rows:
            module = modules[module_name]
            module.__dict__["__provenance_trusted_load__"] = True
            module.__dict__["__provenance_dependency_modules__"] = modules
            code = compile(snapshot.data, str(snapshot.path), "exec", dont_inherit=True)
            exec(code, module.__dict__)
    except BaseException:
        for module_name in reversed(inserted):
            if sys.modules.get(module_name) is modules.get(module_name):
                del sys.modules[module_name]
        raise

    expected_loaded = {snapshot.path.resolve() for _name, snapshot in dependency_rows}
    unexpected = _local_module_paths(root) - before_local - expected_loaded
    if unexpected:
        raise RuntimeError(
            "unpinned local executable dependency loaded: "
            + ", ".join(sorted(path.as_posix() for path in unexpected))
        )
    context = TrustedCodeContext(
        root=root,
        role=role,
        anchor=anchor,
        entrypoint=entrypoint,
        dependencies=tuple(dependency_rows),
        modules=modules,
    )
    _ACTIVE_CONTEXTS[key] = context
    return context


def trusted_code_snapshots(root: Path, role: str) -> tuple[Snapshot, ...]:
    root = Path(root).resolve(strict=True)
    context = _ACTIVE_CONTEXTS.get((root, role))
    if context is None:
        raise RuntimeError(f"trust role {role} was not activated before use")
    return context.snapshots


def _active_anchor(root: Path) -> Snapshot:
    root = Path(root).resolve(strict=True)
    contexts = [context for context in _ACTIVE_CONTEXTS.values() if context.root == root]
    if len(contexts) != 1:
        raise RuntimeError("exactly one active trust role is required")
    return contexts[0].anchor


def _expected_role_records(root: Path, role: str):
    if role not in ROLE_ENTRYPOINTS:
        raise ValueError(f"unknown trust role: {role}")
    entrypoint = {
        "file": ROLE_ENTRYPOINTS[role],
        "sha256": EXPECTED_CODE_SHA256[ROLE_ENTRYPOINTS[role]],
    }
    dependencies = {
        module_name: {
            "file": relative,
            "sha256": EXPECTED_CODE_SHA256[relative],
        }
        for module_name, relative in ROLE_DEPENDENCIES[role]
    }
    for record in (entrypoint, *dependencies.values()):
        _code_path(root, record["file"], f"{role} expected code record")
    return entrypoint, dependencies


def expected_trust_packet(root: Path, role: str) -> dict:
    root = Path(root).resolve(strict=True)
    anchor_snapshot = _active_anchor(root)
    entrypoint, dependencies = _expected_role_records(root, role)
    closure = {
        "anchor": {
            "file": HELPER_RELATIVE,
            "sha256": anchor_snapshot.sha256,
        },
        "entrypoint": entrypoint,
        "dependencies": dependencies,
    }
    pinset = {"entrypoint": entrypoint, "dependencies": dependencies}
    return {
        "schema": TRUST_SCHEMA,
        "version": TRUST_VERSION,
        "role": role,
        **closure,
        "closure_sha256": canonical_hash(closure),
        "pinset_sha256": canonical_hash(pinset),
        "trust_boundary": TRUST_BOUNDARY,
    }


def expected_code_manifest(root: Path, role: str) -> dict[str, str]:
    root = Path(root).resolve(strict=True)
    packet = expected_trust_packet(root, role)
    records = [packet["anchor"], packet["entrypoint"], *packet["dependencies"].values()]
    manifest = {record["file"]: record["sha256"] for record in records}
    if len(manifest) != len(records):
        raise AssertionError(f"{role} executable closure contains duplicate paths")
    return manifest


def role_code_paths(root: Path, role: str) -> tuple[Path, ...]:
    packet = expected_trust_packet(root, role)
    records = [packet["anchor"], packet["entrypoint"], *packet["dependencies"].values()]
    return tuple(
        _code_path(root, record["file"], f"{role} executable closure path")
        for record in records
    )


def require_trust_packet(packet, *, root: Path, role: str) -> None:
    expected = expected_trust_packet(root, role)
    if packet != expected:
        raise AssertionError((f"{role} trust packet mismatch", packet, expected))


@dataclass(frozen=True)
class LineageEvidence:
    payload: dict
    certificate: Snapshot
    verification: Snapshot
    parent_source: Snapshot

    @property
    def snapshots(self):
        return (self.certificate, self.verification, self.parent_source)


def validate_dynamic_lineage(
    *,
    root: Path,
    current_source: Snapshot,
    certificate_snapshot: Snapshot,
    verification_snapshot: Snapshot,
) -> LineageEvidence:
    certificate = parse_json(certificate_snapshot)
    verification = parse_json(verification_snapshot)
    require_header(
        certificate,
        schema=CERTIFICATE_SCHEMA,
        version=CERTIFICATE_VERSION,
        type_name=CERTIFICATE_TYPE,
        verdict=CERTIFICATE_VERDICT,
    )
    require_header(
        verification,
        schema=VERIFICATION_SCHEMA,
        version=VERIFICATION_VERSION,
        type_name=VERIFICATION_TYPE,
        verdict=VERIFICATION_VERDICT,
    )
    require_trust_packet(certificate.get("producer_trust"), root=root, role="builder")
    require_trust_packet(verification.get("producer_trust"), root=root, role="verifier")
    if certificate.get("winner_status") != "NONWINNER":
        raise AssertionError("parent certificate winner status mismatch")
    if (
        verification.get("winner") is not False
        or verification.get("open_neighborhood_reconstructed") is not True
        or verification.get("endpoint_class") != [2, 2, 2]
        or verification.get("endpoint_f_vector") != [61, 162, 103]
        or verification.get("missing_forced_rails") != []
    ):
        raise AssertionError("parent receipt fixed PASS result mismatch")
    verifier_trust = verification["producer_trust"]
    if verification.get("verifier_script_sha256") != verifier_trust["entrypoint"]["sha256"]:
        raise AssertionError("parent receipt verifier hash mismatch")
    if verification.get("clean_exact_module_sha256") != verifier_trust[
        "dependencies"
    ]["clean_local_oct_exact"]["sha256"]:
        raise AssertionError("parent receipt clean-module hash mismatch")

    current_relative = relative_name(current_source.path, root)
    source_record = certificate.get("source")
    if not isinstance(source_record, dict) or set(source_record) != {"file", "sha256"}:
        raise AssertionError("parent certificate source record schema mismatch")
    parent_source_path = stored_path(
        source_record["file"], root=root, context="parent certificate source"
    )
    parent_source = read_snapshot(parent_source_path)
    if parent_source.sha256 != source_record["sha256"]:
        raise AssertionError("parent certificate source hash mismatch")
    if parent_source.path == current_source.path or parent_source.sha256 == current_source.sha256:
        raise AssertionError("dynamic lineage parent step is not nonzero and distinct")

    parent_source_relative = relative_name(parent_source.path, root)
    source_manifest = certificate.get("source_file_sha256")
    if not isinstance(source_manifest, dict):
        raise AssertionError("parent certificate lacks source manifest")
    if source_manifest.get(parent_source_relative) != parent_source.sha256:
        raise AssertionError("parent certificate manifest does not bind parent source")
    generated = certificate.get("generated_file_sha256")
    if generated != {current_relative: current_source.sha256}:
        raise AssertionError("parent certificate did not generate the exact dynamic-source path")

    if verification.get("certificate_sha256") != certificate_snapshot.sha256:
        raise AssertionError("parent receipt/certificate hash mismatch")
    if verification.get("certificate_file") != relative_name(certificate_snapshot.path, root):
        raise AssertionError("parent receipt certificate path mismatch")
    if verification.get("path_definition_sha256") != certificate.get("path", {}).get(
        "path_definition_sha256"
    ):
        raise AssertionError("parent receipt/path-definition hash mismatch")
    if verification.get("path_definition_file") != certificate.get("path", {}).get(
        "path_definition_file"
    ):
        raise AssertionError("parent receipt/path-definition file mismatch")
    if verification.get("source_file") != parent_source_relative:
        raise AssertionError("parent receipt source path mismatch")
    if verification.get("source_sha256") != parent_source.sha256:
        raise AssertionError("parent receipt does not bind parent certificate source")
    if verification.get("endpoint_file") != current_relative:
        raise AssertionError("parent receipt endpoint path mismatch")
    if verification.get("endpoint_sha256") != current_source.sha256:
        raise AssertionError("parent receipt endpoint does not bind new source")

    payload = {
        "schema": LINEAGE_SCHEMA,
        "version": LINEAGE_VERSION,
        "parent_source": {
            "file": parent_source_relative,
            "sha256": parent_source.sha256,
        },
        "literal_source_endpoint": {
            "file": current_relative,
            "sha256": current_source.sha256,
        },
        "certificate": {
            "file": relative_name(certificate_snapshot.path, root),
            "sha256": certificate_snapshot.sha256,
        },
        "verification": {
            "file": relative_name(verification_snapshot.path, root),
            "sha256": verification_snapshot.sha256,
        },
    }
    return LineageEvidence(payload, certificate_snapshot, verification_snapshot, parent_source)


def lineage_paths(payload, *, root: Path) -> tuple[Path, Path]:
    if not isinstance(payload, dict):
        raise AssertionError("missing dynamic-source lineage packet")
    if payload.get("schema") != LINEAGE_SCHEMA or payload.get("version") != LINEAGE_VERSION:
        raise AssertionError("dynamic-source lineage schema mismatch")
    certificate = stored_path(
        payload.get("certificate", {}).get("file"),
        root=root,
        context="lineage certificate",
    )
    verification = stored_path(
        payload.get("verification", {}).get("file"),
        root=root,
        context="lineage verification",
    )
    return certificate, verification
