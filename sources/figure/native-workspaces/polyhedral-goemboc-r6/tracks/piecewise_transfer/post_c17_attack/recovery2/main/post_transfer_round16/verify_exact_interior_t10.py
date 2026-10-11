#!/usr/bin/env python3
"""Isolated exact pre-event extension of the verified F21 ray to total t=10.

The frozen clean-room unit verifier is executed from one hash-bound byte
snapshot as a proof engine.  No proposer or serialized geometry ledger is
imported.  This sidecar certifies only the closed pre-event segment [0,10]; it
does not certify or cross the first future wall near t=10.01168.
"""
from __future__ import annotations

import hashlib
import json
import os
import stat
import sys
import traceback
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path
from types import ModuleType


sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ATTACK = MAIN.parents[1]
F20 = MAIN / "post_transfer_round15"

ENGINE = HERE / "verify_exact_interior.py"
UNIT_VERIFICATION = HERE / "exact_interior_verification.json"
SOURCE = F20 / "far.csv"
FACES = F20 / "post_faces.json"
CHART = HERE / "chart.json"
PROPOSER = HERE / "exact_interior_propose.py"
UNIT_CANDIDATE = HERE / "exact_interior_candidate.csv"
PROPOSAL = HERE / "exact_interior_proposal.json"
RECEIPT = HERE / "exact_interior_receipt.json"
SCAN = HERE / "exact_interior_event_scan.json"

T10_CANDIDATE = HERE / "exact_interior_t10_candidate.csv"
T10_VERIFICATION = HERE / "exact_interior_t10_verification.json"
T10_LOG = HERE / "F21_T10_EXTENSION_LOG.md"

EXPECTED = {
    "engine": (ENGINE, 105094, "be98869c6cfad29aa0b96ffff2cfe4d5bbee034c2feb6a94a21d0a9b647518da"),
    "unit_verification": (UNIT_VERIFICATION, 227459, "7787d0c8a90346d23abac629d8678b82d504def1161aa4c5914016e81eb71d3b"),
    "source": (SOURCE, 82321, "d34ebac9a1cfe81ce4d782049938ad68f1124eb82e3cd19342c30e5de14f39e3"),
    "faces": (FACES, 3283, "06b15585bd906ae1ee0cfc5aefff2a46a5e752a02dfb556abde9225e1df81c6b"),
    "chart": (CHART, 28897, "29ddf33a8126a2315a09eb6daee77b80b9691f1fd1b91e9a127e87699197b4b8"),
    "proposer": (PROPOSER, 64187, "93b6c983929db92ef9b9898b2a20c4424dfd872e7a5c3369073fb1cbf9de9fc5"),
    "unit_candidate": (UNIT_CANDIDATE, 343273, "52136b5bef94379e00445a0688865c56936ea7bc31db78e3f9fe90e8f755f110"),
    "proposal": (PROPOSAL, 1160861, "d1a481360259c1e5ecdeafbd9a4b2db38d7581c83ef995e475c295e71f17b30a"),
    "receipt": (RECEIPT, 24180, "8c13b9fbfa3f6d1dc16cb11213adbfac8658827dd19173a384722838ed447f8e"),
    "scan": (SCAN, 8936000, "17cbafcb58c9072947d845409e02d8ae0740a166d89b91c820c057071f56b6d3"),
}


class Failure(RuntimeError):
    pass


def need(condition, message):
    if not condition:
        raise Failure(message)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class Snapshot:
    def __init__(self, name, path, data, fd, fingerprint):
        self.name, self.path, self.data, self.fd, self.fingerprint = name, path, data, fd, fingerprint
        self.size, self.sha256 = len(data), sha(data)

    def unchanged(self):
        current = os.lstat(self.path)
        observed = (
            current.st_dev, current.st_ino, current.st_size,
            current.st_mtime_ns, current.st_ctime_ns, current.st_mode,
        )
        need(observed == self.fingerprint, f"input changed during t=10 verification: {self.path}")

    def close(self):
        os.close(self.fd)


def freeze(name, path, expected_size, expected_hash):
    flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
    fd = os.open(path, flags)
    try:
        before = os.fstat(fd)
        need(stat.S_ISREG(before.st_mode), f"non-regular input: {path}")
        need(before.st_size == expected_size, f"byte-count drift: {path.name}")
        data = bytearray()
        remaining = before.st_size
        while remaining:
            block = os.read(fd, min(1 << 20, remaining))
            need(block, f"short snapshot read: {path}")
            data.extend(block)
            remaining -= len(block)
        need(os.read(fd, 1) == b"", f"input grew during snapshot: {path}")
        after = os.fstat(fd)
        fingerprint = (
            before.st_dev, before.st_ino, before.st_size,
            before.st_mtime_ns, before.st_ctime_ns, before.st_mode,
        )
        need(fingerprint == (
            after.st_dev, after.st_ino, after.st_size,
            after.st_mtime_ns, after.st_ctime_ns, after.st_mode,
        ), f"input mutated during snapshot: {path}")
        frozen = bytes(data)
        need(sha(frozen) == expected_hash, f"sha256 drift: {path.name}")
        return Snapshot(name, path, frozen, fd, fingerprint)
    except Exception:
        os.close(fd)
        raise


def load_engine(snapshot):
    module = ModuleType("frozen_f21_clean_room_engine")
    module.__file__ = str(snapshot.path)
    module.__package__ = ""
    need(module.__name__ not in sys.modules, "clean-room engine module name is already loaded")
    sys.modules[module.__name__] = module
    exec(compile(snapshot.data, str(snapshot.path), "exec"), module.__dict__)
    return module


def path_audit(clean, source, endpoint, cycles, direction):
    polynomial_points = {
        row_id: tuple(
            clean.Poly((source[row_id][axis], endpoint[row_id][axis] - source[row_id][axis]))
            for axis in range(3)
        )
        for row_id in source
    }
    active = sorted(set().union(*(set(cycle) for cycle in cycles)))
    spec, _basis = clean.build_spec(source, active)
    jets = clean.make_jets(source, spec, direction)
    raw = clean.raw_primitive_jets(jets, cycles)
    path = clean.path_primitives(polynomial_points, cycles)
    need(len(raw) == len(path) == 12363, "t=10 primitive count mismatch")

    raw_by_key = {}
    for index, (name, value, family) in enumerate(raw):
        key = (name, family)
        need(key not in raw_by_key, f"duplicate t=10 raw key at {index}: {key}")
        raw_by_key[key] = value

    keys = set()
    families = Counter()
    digest = hashlib.sha256()
    minimum = None
    minimum_owner = None
    leaves = 0
    sturm_fallbacks = 0
    path_by_key = {}
    for index, (name, polynomial, family) in enumerate(path):
        key = (name, family)
        need(key not in keys, f"duplicate t=10 path key at {index}: {key}")
        keys.add(key)
        path_by_key[key] = polynomial
        need(key in raw_by_key, f"t=10 path key absent from raw atlas: {key}")
        jet = raw_by_key.pop(key)
        derivative = polynomial.c[1] if len(polynomial.c) > 1 else Q(0)
        need(polynomial.c[0] == jet.v and derivative == jet.d[0], f"t=10 raw/path first-jet mismatch: {key}")
        need(polynomial.c[0] != 0, f"zero source primitive: {key}")
        result = clean.audit_strict_polynomial(polynomial, 1 if polynomial.c[0] > 0 else -1)
        need(result["strict"], f"non-strict t=10 primitive: {key}")
        leaves += result["leaves"]
        sturm_fallbacks += result["method"] == "sturm_fallback"
        families[family] += 1
        if result["minimum"] is not None and (minimum is None or result["minimum"] < minimum):
            minimum = result["minimum"]
            minimum_owner = {
                "index_zero_based": index,
                "name": name,
                "family": family,
                "interval_exact": [clean.qslash(result["minimum_interval"][0]), clean.qslash(result["minimum_interval"][1])],
                "coefficient_index": result["minimum_index"],
            }
        digest.update(f"{name}|{family}|{'|'.join(polynomial.exact())}\n".encode())
    need(not raw_by_key, "raw t=10 atlas has keys absent from path")
    need(dict(families) == clean.EXPECTED_FAMILIES, f"t=10 family counts changed: {dict(families)}")
    need(minimum is not None and minimum > 0, "missing t=10 strict margin")
    return {
        "primitive_count": 12363,
        "family_counts": dict(families),
        "unique_raw_path_key_bijection": True,
        "raw_path_value_derivative_correspondence": True,
        "strict_total_parameter_interval_exact": ["0", "10"],
        "all_primitives_strict": True,
        "bernstein_leaf_count": leaves,
        "sturm_fallback_count": sturm_fallbacks,
        "minimum_normalized_bernstein_coefficient_exact": clean.qcompact(minimum),
        "minimum_owner": minimum_owner,
        "path_primitive_sha256": digest.hexdigest(),
        "path_by_key": path_by_key,
    }


def write_exclusive(path, data):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_CLOEXEC", 0), 0o644)
    try:
        offset = 0
        while offset < len(data):
            written = os.write(fd, data[offset:])
            need(written > 0, f"short write: {path}")
            offset += written
        os.fsync(fd)
    finally:
        os.close(fd)


def run():
    for output in (T10_CANDIDATE, T10_VERIFICATION, T10_LOG):
        need(not output.exists(), f"refusing to overwrite existing {output.name}")
    sidecar_bytes = Path(__file__).read_bytes()
    snapshots = {}
    created = []
    try:
        for name, (path, size, expected_hash) in EXPECTED.items():
            snapshots[name] = freeze(name, path, size, expected_hash)
        clean = load_engine(snapshots["engine"])
        unit_verification = clean.strict_json(snapshots["unit_verification"].data, "unit verification")
        need(unit_verification.get("verdict") == "INDEPENDENT_EXACT_POST_C17_F21_INTERIOR_VERIFICATION_PASS", "unit verifier is not accepted PASS")
        need(unit_verification.get("exhaustive_unit_segment", {}).get("primitive_count") == 12363, "unit verification primitive count mismatch")
        source = clean.read_rows(snapshots["source"].data, "F20 source")
        unit_candidate = clean.read_rows(snapshots["unit_candidate"].data, "unit candidate")
        faces_payload = clean.strict_json(snapshots["faces"].data, "F20 faces")
        cycles = clean.validate_cycles(faces_payload, source)
        proposal = clean.strict_json(snapshots["proposal"].data, "F21 proposal")
        scan = clean.strict_json(snapshots["scan"].data, "F21 locator")

        source_faces = clean.exactify_faces(source, cycles)
        source_mechanics = clean.mechanics_q(source, source_faces)
        spec, _basis = clean.build_spec(source, source_mechanics["active"])
        unit_direction = tuple(Q(value) for value in proposal["exact_coefficients"])
        unit_delta = clean.displacement_from_coefficients(source, spec, unit_direction)
        need({row_id: clean.add(point, unit_delta[row_id]) for row_id, point in source.items()} == unit_candidate, "unit candidate/direction relation drift")
        direction10 = tuple(10 * value for value in unit_direction)
        delta10 = clean.displacement_from_coefficients(source, spec, direction10)
        endpoint10 = {row_id: clean.add(point, delta10[row_id]) for row_id, point in source.items()}
        endpoint10_bytes = clean.candidate_csv_bytes(endpoint10)
        endpoint10_sha = sha(endpoint10_bytes)

        endpoint_faces = clean.exactify_faces(endpoint10, cycles)
        endpoint_mechanics = clean.mechanics_q(endpoint10, endpoint_faces)
        need(endpoint_mechanics["packet"] == source_mechanics["packet"], "t=10 mechanics packet changed")
        need(set(endpoint_mechanics["incidence"]) == set(source_mechanics["incidence"]), "t=10 true-edge ledger changed")
        need(endpoint_mechanics["signs"] == source_mechanics["signs"], "t=10 mechanics sign cell changed")
        rails = clean.forced_rails()
        need(not (rails - set(endpoint_mechanics["incidence"])), "t=10 endpoint is missing forced rails")
        for carrier in (clean.BASE, clean.SHELL):
            source_face = next(face for face in source_faces if set(face["cycle"]) == set(carrier))
            need(all(clean.dot(source_face["n"], endpoint10[label]) == source_face["h"] for label in carrier), f"t=10 endpoint left carrier plane {carrier}")

        audit = path_audit(clean, source, endpoint10, cycles, direction10)
        first = scan["first_candidate"]
        first_lo = Q(first["lo"])
        need(first_lo > 10, "hash-bound locator first bracket is not after t=10")
        first_key = (first["name"], first["family"])
        need(first_key in audit["path_by_key"], "locator first primitive absent from t=10 reconstruction")
        # p_10(u) = p_total(t=10u); compare coefficients after exact scaling.
        total_polynomial_exact = [Q(value) for value in first["polynomial_exact"]]
        expected_scaled = clean.Poly(tuple(value * (Q(10) ** index) for index, value in enumerate(total_polynomial_exact)))
        need(audit["path_by_key"][first_key] == expected_scaled, "t=10 first-wall polynomial scaling mismatch")

        audit_public = {key: value for key, value in audit.items() if key != "path_by_key"}
        snapshots_public = {
            name: {
                "path": str(item.path.relative_to(ATTACK)),
                "bytes": item.size,
                "sha256": item.sha256,
                "snapshot_reads": 1,
            }
            for name, item in snapshots.items()
        }
        payload = {
            "version": 1,
            "scope": "isolated exact extension of the verified F21 ray from total parameter t=0 through t=10",
            "sidecar": {"path": "recovery2/main/post_transfer_round16/verify_exact_interior_t10.py", "sha256": sha(sidecar_bytes)},
            "inputs": snapshots_public,
            "endpoint": {
                "total_parameter_exact": "10",
                "csv": "recovery2/main/post_transfer_round16/exact_interior_t10_candidate.csv",
                "csv_bytes": len(endpoint10_bytes),
                "csv_sha256": endpoint10_sha,
                "f_vector": endpoint_mechanics["packet"]["f_vector"],
                "class": endpoint_mechanics["packet"]["class"],
                "stable_faces": endpoint_mechanics["packet"]["stable_faces"],
                "unstable_vertices": endpoint_mechanics["packet"]["unstable_vertices"],
                "saddle_edges": endpoint_mechanics["packet"]["saddle_edges"],
                "volume_exact": clean.qslash(endpoint_mechanics["volume"]),
                "centroid_exact": [clean.qslash(value) for value in endpoint_mechanics["centroid"]],
                "same_exact_prescribed_hull_true_edges_and_mechanics_sign_cell": True,
                "frozen_carriers": [list(clean.BASE), list(clean.SHELL)],
                "forced_rail_count": 37,
                "all_forced_rails_present": True,
            },
            "exhaustive_segment": audit_public,
            "locator_boundary": {
                "scan_sha256": snapshots["scan"].sha256,
                "first_candidate": first["name"],
                "first_bracket_exact": [first["lo"], first["hi"]],
                "exact_lower_gap_after_t10": clean.qcompact(first_lo - 10),
                "first_bracket_strictly_after_t10": True,
                "future_87_candidate_wall_certified": False,
                "future_wall_crossed": False,
            },
            "verdict": "INDEPENDENT_EXACT_POST_C17_F21_T10_PRE_EVENT_EXTENSION_PASS",
            "proof_status": "EXACT_STRICT_PRE_EVENT_SEGMENT_T0_TO_T10_ONLY",
            "winner_status": "NONWINNER_EXTENSION_ONLY",
            "claim_boundary": "All 12,363 primitives are strict through total t=10. The future common wall is neither certified nor crossed here.",
        }
        verification_bytes = (json.dumps(payload, indent=2) + "\n").encode()
        verification_sha = sha(verification_bytes)
        log = f"""# F21 exact t=10 extension log

- Verdict: `{payload['verdict']}`
- Sidecar SHA256: `{sha(sidecar_bytes)}`
- Endpoint SHA256: `{endpoint10_sha}`
- Verification SHA256: `{verification_sha}`
- Primitive count: `12,363`
- Path polynomial SHA256: `{audit_public['path_primitive_sha256']}`
- Exact first-bracket lower gap after t=10: `{clean.qcompact(first_lo - 10)}`

The F20 source-to-total-t=10 segment is strict for every independently rebuilt
support, in-face turn, centroid denominator, face, vertex, and edge primitive.
The exact endpoint retains the `[61,150,91]` hull, class `[2,4,4]`, both frozen
carrier planes, the same mechanics sign cell, and all 37 rails.  No claim is
made about crossing or certifying the future 87-candidate wall.
""".encode()

        for item in snapshots.values():
            item.unchanged()
        write_exclusive(T10_CANDIDATE, endpoint10_bytes)
        created.append(T10_CANDIDATE)
        write_exclusive(T10_VERIFICATION, verification_bytes)
        created.append(T10_VERIFICATION)
        write_exclusive(T10_LOG, log)
        created.append(T10_LOG)
        for item in snapshots.values():
            item.unchanged()
        directory_fd = os.open(HERE, os.O_RDONLY | getattr(os, "O_CLOEXEC", 0))
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
        print(payload["verdict"])
        print("endpoint_sha256", endpoint10_sha)
        print("verification_sha256", verification_sha)
        print("log_sha256", sha(log))
    except Exception:
        for path in reversed(created):
            try:
                path.unlink()
            except FileNotFoundError:
                pass
        raise
    finally:
        for item in snapshots.values():
            try:
                item.close()
            except OSError:
                pass


def main():
    try:
        run()
    except Exception as error:
        traceback.print_exc()
        print("INDEPENDENT_EXACT_POST_C17_F21_T10_PRE_EVENT_EXTENSION_FAIL", file=sys.stderr)
        print(repr(error), file=sys.stderr)
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()
