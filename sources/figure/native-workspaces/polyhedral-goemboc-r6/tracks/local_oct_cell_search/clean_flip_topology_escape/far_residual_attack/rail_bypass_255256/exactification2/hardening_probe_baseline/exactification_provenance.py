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
import tempfile
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path


TRUST_SCHEMA = "polyhedral-goemboc.exactification.local-trust/v1"
TRUST_VERSION = 1
TRUST_BOUNDARY = (
    "Local byte pins rooted in exactification_provenance.py. They detect changes "
    "to pinned entrypoints and dependencies while this helper and its caller are "
    "trusted; they are not a signature against coordinated mutation of the whole "
    "mutable workspace."
)

ROLE_FILENAMES = {
    "search": "search_exact_first_jet_full_chart.py",
    "diagnose": "diagnose_full_chart_derivative_horizon.py",
    "builder": "build_exactification_certificate.py",
    "verifier": "verify_exactification_certificate.py",
}

# Filled only after all four entrypoints reach their final reviewed bytes.  The
# helper is the non-circular anchor: changing these constants changes the anchor,
# not any pinned entrypoint.
EXPECTED_ENTRYPOINT_SHA256 = {
    "search": "2caf72466ee7f3c58d124d7db1d191a17bdb96ea1982a5f9a070fd58af44d381",
    "diagnose": "009618e6a68fe7327895e070480763a4ec77abb35ef9b3025bfaf8e9828ebba0",
    "builder": "8497c8c59799c22392bf1ed9b68ca37ceeccdf329ef5785e4aa6fefb36fa345d",
    "verifier": "191994f2a7d508c0b22347e33c9ee95824be756a320277bad6c9601189f1fb51",
}
EXPECTED_CLEAN_MODULE_SHA256 = "5498478e54cc26f94ad61888113f0e1af90ba400048614933499559676b6c4ac"

FIRST_JET_PATH_SCHEMA = "polyhedral-goemboc.exactification.first-jet-path/v2"
FIRST_JET_PATH_VERSION = 2
FIRST_JET_PATH_TYPE = (
    "exact rational full-chart velocity with seven strict analytic first jets"
)
FIRST_JET_PATH_VERDICT = "EXACT_TARGET_FIRST_JET_FULL_CHART_PATH_PASS"
FIRST_JET_SEARCH_VERDICT = "EXACT_TARGET_FIRST_JET_FULL_CHART_PRIMAL_FOUND"

FIRST_JET_CONTRACT_SCHEMA = "polyhedral-goemboc.exactification.first-jet-contract/v1"
FIRST_JET_CONTRACT_VERSION = 1

DIAGNOSTIC_SCHEMA = "polyhedral-goemboc.exactification.derivative-horizon/v2"
DIAGNOSTIC_VERSION = 2
DIAGNOSTIC_TYPE = "exact seven-row derivative-horizon diagnostic"
DIAGNOSTIC_VERDICT = "EXACT_FULL_CHART_FIRST_DERIVATIVE_HORIZON_ISOLATED"

CERTIFIED_PATH_SCHEMA = "polyhedral-goemboc.exactification.certified-path/v3"
CERTIFIED_PATH_VERSION = 3
CERTIFIED_PATH_TYPE = (
    "exact rational full-chart velocity with certified seven-derivative substep"
)
CERTIFIED_PATH_VERDICT = "EXACT_FULL_CHART_CERTIFIED_SUBSTEP_PATH_PASS"

CERTIFICATE_SCHEMA = "polyhedral-goemboc.exactification.material-step-certificate/v2"
CERTIFICATE_VERSION = 2
CERTIFICATE_TYPE = "exact nonzero material-step certificate"
CERTIFICATE_VERDICT = "EXACT_LOCAL_OCT_RAIL255256_FULL_CONTROL_MATERIAL_STEP_PASS"

VERIFICATION_SCHEMA = "polyhedral-goemboc.exactification.material-step-receipt/v2"
VERIFICATION_VERSION = 2
VERIFICATION_TYPE = "independent clean-room verification of exactified rail-bypass step"
VERIFICATION_VERDICT = (
    "INDEPENDENT_EXACT_LOCAL_OCT_RAIL255256_FULL_CONTROL_MATERIAL_STEP_PASS"
)

LINEAGE_SCHEMA = "polyhedral-goemboc.exactification.dynamic-source-lineage/v2"
LINEAGE_VERSION = 2


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


def assert_snapshot_current(snapshot: Snapshot) -> None:
    current = read_snapshot(snapshot.path)
    if (
        current.device,
        current.inode,
        current.size,
        current.mtime_ns,
        current.sha256,
    ) != (
        snapshot.device,
        snapshot.inode,
        snapshot.size,
        snapshot.mtime_ns,
        snapshot.sha256,
    ):
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
    expected = {
        "schema": schema,
        "version": version,
        "type": type_name,
        "verdict": verdict,
    }
    got = {key: document.get(key) for key in expected}
    if got != expected:
        raise AssertionError(("fixed artifact header mismatch", got, expected))


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
    if role not in ROLE_FILENAMES:
        raise ValueError(f"unknown trust role: {role}")
    return contained_path(
        _helper_directory() / ROLE_FILENAMES[role],
        base=root,
        root=root,
        context=f"{role} entrypoint",
    )


def clean_module_path(root: Path) -> Path:
    return contained_path(
        _helper_directory().parents[1] / "verify_exact_event_certificate.py",
        base=root,
        root=root,
        context="clean verifier module",
    )


def trusted_code_snapshots(root: Path, role: str) -> tuple[Snapshot, ...]:
    helper_snapshot = read_snapshot(Path(__file__).resolve())
    entrypoint_snapshot = read_snapshot(role_path(root, role))
    expected_entrypoint = EXPECTED_ENTRYPOINT_SHA256[role]
    if entrypoint_snapshot.sha256 != expected_entrypoint:
        raise RuntimeError(
            f"untrusted {role} entrypoint hash {entrypoint_snapshot.sha256}; "
            f"expected {expected_entrypoint}"
        )
    snapshots = [helper_snapshot, entrypoint_snapshot]
    if role == "verifier":
        clean_snapshot = read_snapshot(clean_module_path(root))
        if clean_snapshot.sha256 != EXPECTED_CLEAN_MODULE_SHA256:
            raise RuntimeError(
                f"untrusted clean module hash {clean_snapshot.sha256}; "
                f"expected {EXPECTED_CLEAN_MODULE_SHA256}"
            )
        snapshots.append(clean_snapshot)
    return tuple(snapshots)


def expected_trust_packet(root: Path, role: str) -> dict:
    root = Path(root).resolve(strict=True)
    snapshots = trusted_code_snapshots(root, role)
    helper_snapshot, entrypoint_snapshot = snapshots[:2]
    entrypoint = entrypoint_snapshot.path
    dependencies = {}
    if role == "verifier":
        clean_snapshot = snapshots[2]
        clean_path = clean_snapshot.path
        dependencies["clean_exact_module"] = {
            "file": relative_name(clean_path, root),
            "sha256": clean_snapshot.sha256,
        }
    pinset = {
        "entrypoints": EXPECTED_ENTRYPOINT_SHA256,
        "clean_exact_module": EXPECTED_CLEAN_MODULE_SHA256,
    }
    return {
        "schema": TRUST_SCHEMA,
        "version": TRUST_VERSION,
        "role": role,
        "anchor": {
            "file": relative_name(Path(__file__).resolve(), root),
            "sha256": helper_snapshot.sha256,
        },
        "entrypoint": {
            "file": relative_name(entrypoint, root),
            "sha256": entrypoint_snapshot.sha256,
        },
        "dependencies": dependencies,
        "pinset_sha256": canonical_hash(pinset),
        "trust_boundary": TRUST_BOUNDARY,
    }


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
    ]["clean_exact_module"]["sha256"]:
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
