#!/usr/bin/env python3
"""Independent QQ-gcd and geometric-owner certificate for the first F21 wall.

This is a wall locator/identity certificate only.  It reconstructs the entire
total-parameter ray, proves the hash-bound 82 overlap rows share one rational
linear factor, and identifies the exact coplanarity owner.  It does not build,
certify, or enter a post-wall cell.
"""
from __future__ import annotations

import ast
import hashlib
import json
import os
import stat
import sys
import traceback
from collections import Counter, defaultdict
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
T10_VERIFIER = HERE / "verify_exact_interior_t10.py"
T10_CANDIDATE = HERE / "exact_interior_t10_candidate.csv"
T10_VERIFICATION = HERE / "exact_interior_t10_verification.json"
SOURCE = F20 / "far.csv"
FACES = F20 / "post_faces.json"
UNIT_CANDIDATE = HERE / "exact_interior_candidate.csv"
PROPOSAL = HERE / "exact_interior_proposal.json"
RECEIPT = HERE / "exact_interior_receipt.json"
SCAN = HERE / "exact_interior_event_scan.json"

OUTPUT = HERE / "exact_interior_first_wall_verification.json"
LOG = HERE / "F21_FIRST_WALL_LOG.md"

EXPECTED = {
    "engine": (ENGINE, 105094, "be98869c6cfad29aa0b96ffff2cfe4d5bbee034c2feb6a94a21d0a9b647518da"),
    "unit_verification": (UNIT_VERIFICATION, 227459, "7787d0c8a90346d23abac629d8678b82d504def1161aa4c5914016e81eb71d3b"),
    "t10_verifier": (T10_VERIFIER, 17567, "e7eb52eb5584a3cc85a5148b7b771144b085e8d7e308f28725a94211691d10dd"),
    "t10_candidate": (T10_CANDIDATE, 343066, "0e9a5e84ae7907a1a07e686cc797c74e2840305963c28447199b7976f9eb7688"),
    "t10_verification": (T10_VERIFICATION, 53696, "e705c68a75331cd5775337f50a6ae3ce058cc1f4622854339467780b271bcd60"),
    "source": (SOURCE, 82321, "d34ebac9a1cfe81ce4d782049938ad68f1124eb82e3cd19342c30e5de14f39e3"),
    "faces": (FACES, 3283, "06b15585bd906ae1ee0cfc5aefff2a46a5e752a02dfb556abde9225e1df81c6b"),
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


def sha(data):
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
        need(observed == self.fingerprint, f"first-wall input changed: {self.path}")

    def close(self):
        os.close(self.fd)


def freeze(name, path, expected_size, expected_hash):
    fd = os.open(path, os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0))
    try:
        before = os.fstat(fd)
        need(stat.S_ISREG(before.st_mode) and before.st_size == expected_size, f"first-wall input type/size drift: {path}")
        data = bytearray()
        remaining = before.st_size
        while remaining:
            block = os.read(fd, min(1 << 20, remaining))
            need(block, f"short first-wall snapshot: {path}")
            data.extend(block)
            remaining -= len(block)
        need(os.read(fd, 1) == b"", f"first-wall input grew: {path}")
        after = os.fstat(fd)
        fingerprint = (
            before.st_dev, before.st_ino, before.st_size,
            before.st_mtime_ns, before.st_ctime_ns, before.st_mode,
        )
        need(fingerprint == (
            after.st_dev, after.st_ino, after.st_size,
            after.st_mtime_ns, after.st_ctime_ns, after.st_mode,
        ), f"first-wall input mutated: {path}")
        frozen = bytes(data)
        need(sha(frozen) == expected_hash, f"first-wall sha256 drift: {path.name}")
        return Snapshot(name, path, frozen, fd, fingerprint)
    except Exception:
        os.close(fd)
        raise


def load_engine(snapshot):
    module = ModuleType("frozen_f21_first_wall_engine")
    module.__file__ = str(snapshot.path)
    module.__package__ = ""
    need(module.__name__ not in sys.modules, "first-wall engine already loaded")
    sys.modules[module.__name__] = module
    exec(compile(snapshot.data, str(snapshot.path), "exec"), module.__dict__)
    return module


def monic(clean, polynomial):
    need(polynomial.c != (Q(0),), "cannot normalize zero gcd polynomial")
    return polynomial / polynomial.c[-1]


def polynomial_gcd(clean, left, right):
    left, right = monic(clean, left), monic(clean, right)
    while right.c != (Q(0),):
        _quotient, remainder = clean.poly_divmod(left, right)
        left, right = right, (clean.Poly.zero() if remainder.c == (Q(0),) else monic(clean, remainder))
    return monic(clean, left)


def gcd_many(clean, polynomials):
    need(bool(polynomials), "empty polynomial gcd family")
    result = polynomials[0]
    for polynomial in polynomials[1:]:
        result = polynomial_gcd(clean, result, polynomial)
        if result.degree == 0:
            break
    return monic(clean, result)


def parse_support_name(name):
    need(name.startswith("support:f") and ":w" in name, f"invalid support owner name: {name}")
    face, witness = name.removeprefix("support:f").split(":w", 1)
    return int(face), int(witness)


def parse_edge_name(name):
    need(name.startswith("edge:") and name.count(":") >= 2, f"invalid edge owner name: {name}")
    body, component = name.removeprefix("edge:").rsplit(":", 1)
    edge = ast.literal_eval(body)
    need(isinstance(edge, tuple) and len(edge) == 2 and all(type(value) is int for value in edge), f"invalid edge tuple: {name}")
    return tuple(sorted(edge)), component


def write_exclusive(path, data):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_CLOEXEC", 0), 0o644)
    try:
        offset = 0
        while offset < len(data):
            written = os.write(fd, data[offset:])
            need(written > 0, f"short first-wall output write: {path}")
            offset += written
        os.fsync(fd)
    finally:
        os.close(fd)


def run():
    need(not OUTPUT.exists(), f"refusing to overwrite {OUTPUT.name}")
    need(not LOG.exists(), f"refusing to overwrite {LOG.name}")
    script_bytes = Path(__file__).read_bytes()
    snapshots, created = {}, []
    try:
        for name, (path, size, expected_hash) in EXPECTED.items():
            snapshots[name] = freeze(name, path, size, expected_hash)
        clean = load_engine(snapshots["engine"])
        unit_verification = clean.strict_json(snapshots["unit_verification"].data, "unit verification")
        t10_verification = clean.strict_json(snapshots["t10_verification"].data, "t10 verification")
        proposal = clean.strict_json(snapshots["proposal"].data, "proposal")
        scan = clean.strict_json(snapshots["scan"].data, "scan")
        need(unit_verification.get("verdict") == "INDEPENDENT_EXACT_POST_C17_F21_INTERIOR_VERIFICATION_PASS", "unit verification is not PASS")
        need(t10_verification.get("verdict") == "INDEPENDENT_EXACT_POST_C17_F21_T10_PRE_EVENT_EXTENSION_PASS", "t10 verification is not PASS")
        need(t10_verification.get("locator_boundary", {}).get("future_wall_crossed") is False, "t10 sidecar crossed future wall")

        source = clean.read_rows(snapshots["source"].data, "F20 source")
        unit_candidate = clean.read_rows(snapshots["unit_candidate"].data, "unit candidate")
        t10_candidate = clean.read_rows(snapshots["t10_candidate"].data, "t10 candidate")
        faces_payload = clean.strict_json(snapshots["faces"].data, "F20 faces")
        cycles = clean.validate_cycles(faces_payload, source)
        source_faces = clean.exactify_faces(source, cycles)
        source_mechanics = clean.mechanics_q(source, source_faces)
        spec, _basis = clean.build_spec(source, source_mechanics["active"])
        direction = tuple(Q(value) for value in proposal["exact_coefficients"])
        delta = clean.displacement_from_coefficients(source, spec, direction)
        need({row_id: clean.add(point, delta[row_id]) for row_id, point in source.items()} == unit_candidate, "unit direction relation mismatch")
        need({row_id: clean.add(point, clean.mul(delta[row_id], Q(10))) for row_id, point in source.items()} == t10_candidate, "t10 direction relation mismatch")

        points = {
            row_id: tuple(clean.Poly((source[row_id][axis], unit_candidate[row_id][axis] - source[row_id][axis])) for axis in range(3))
            for row_id in source
        }
        primitives = clean.path_primitives(points, cycles)
        need(len(primitives) == 12363, "first-wall path primitive count mismatch")
        by_key = {}
        path_digest = hashlib.sha256()
        family_counts = Counter()
        for index, (name, polynomial, family) in enumerate(primitives):
            key = (name, family)
            need(key not in by_key, f"duplicate first-wall path key at {index}: {key}")
            by_key[key] = polynomial
            family_counts[family] += 1
            path_digest.update(f"{name}|{family}|{'|'.join(polynomial.exact())}\n".encode())
        need(dict(family_counts) == clean.EXPECTED_FAMILIES, "first-wall path family counts mismatch")
        need(path_digest.hexdigest() == clean.EXPECTED_PATH_DIGEST, "first-wall total-ray path digest mismatch")

        overlap = scan.get("overlapping_first_candidates")
        need(isinstance(overlap, list) and len(overlap) == 82, "first-wall overlap count mismatch")
        overlap_keys = []
        overlap_polynomials = []
        overlap_families = Counter()
        brackets = []
        for index, row in enumerate(overlap):
            key = (row.get("name"), row.get("family"))
            need(key not in overlap_keys, f"duplicate overlap key at {index}: {key}")
            need(key in by_key, f"overlap key absent from independent path: {key}")
            polynomial = by_key[key]
            need(row.get("polynomial_exact") == polynomial.exact(), f"overlap polynomial mismatch: {key}")
            need(row.get("polynomial_digest") == sha("|".join(polynomial.exact()).encode()), f"overlap polynomial digest mismatch: {key}")
            need(row.get("degree") == polynomial.degree, f"overlap degree mismatch: {key}")
            lo, hi = Q(row["lo"]), Q(row["hi"])
            need(lo <= hi and lo > 10, f"overlap bracket is not after t10: {key}")
            need(row.get("value_lo") == clean.qcompact(polynomial.eval(lo)) and row.get("value_hi") == clean.qcompact(polynomial.eval(hi)), f"overlap bracket value mismatch: {key}")
            overlap_keys.append(key)
            overlap_polynomials.append(polynomial)
            overlap_families[row["family"]] += 1
            brackets.append((lo, hi))
        need(dict(overlap_families) == {"edge_component": 21, "support": 61}, f"overlap family counts mismatch: {dict(overlap_families)}")

        common_gcd = gcd_many(clean, overlap_polynomials)
        support_gcd = gcd_many(clean, [polynomial for polynomial, key in zip(overlap_polynomials, overlap_keys) if key[1] == "support"])
        edge_gcd = gcd_many(clean, [polynomial for polynomial, key in zip(overlap_polynomials, overlap_keys) if key[1] == "edge_component"])
        need(common_gcd.degree == support_gcd.degree == edge_gcd.degree == 1, "first-wall gcd is not linear in all families")
        need(common_gcd == support_gcd == edge_gcd, "support/edge gcd factors differ")
        root = -common_gcd.c[0] / common_gcd.c[1]
        need(root > 10, "first-wall rational root is not after t10")
        need(all(lo <= root <= hi for lo, hi in brackets), "common rational root is outside an overlap bracket")
        for key, polynomial in zip(overlap_keys, overlap_polynomials):
            quotient, remainder = clean.poly_divmod(polynomial, common_gcd)
            need(remainder.c == (Q(0),) and quotient * common_gcd == polynomial, f"gcd does not divide overlap polynomial: {key}")
            need(polynomial.eval(root) == 0, f"overlap polynomial is nonzero at common root: {key}")

        zero_keys = [key for key, polynomial in by_key.items() if polynomial.eval(root) == 0]
        need(len(zero_keys) == 82 and set(zero_keys) == set(overlap_keys), "exact first-wall zero set differs from 82 overlap rows")

        support_owners = [parse_support_name(name) for name, family in overlap_keys if family == "support"]
        support_by_face = Counter(face for face, _witness in support_owners)
        need(dict(support_by_face) == {73: 1, 76: 15, 78: 15, 84: 15, 85: 15}, f"support wall face groups mismatch: {dict(support_by_face)}")
        need((73, 73) in support_owners, "base face f73 / witness 73 owner missing")
        expected_fan = {
            76: (14, 13, 73),
            78: (14, 73, 15),
            84: (16, 15, 73),
            85: (0, 16, 73),
        }
        need(tuple(cycles[73]) == clean.BASE, "face f73 is not the frozen base carrier")
        need(all(tuple(cycles[index]) == cycle for index, cycle in expected_fan.items()), "first-wall fan face cycles mismatch")

        edge_owners = [parse_edge_name(name) for name, family in overlap_keys if family == "edge_component"]
        expected_edges = {(0, 16), (13, 14), (14, 15), (14, 73), (15, 16), (15, 73), (16, 73)}
        need({edge for edge, _component in edge_owners} == expected_edges, "first-wall edge-owner set mismatch")
        need(all(Counter(component for owner_edge, component in edge_owners if owner_edge == edge) == {"beta1": 1, "beta2": 1, "gram": 1} for edge in expected_edges), "first-wall edge component multiplicities mismatch")

        root_rows = {
            row_id: clean.add(point, clean.mul(delta[row_id], root))
            for row_id, point in source.items()
        }
        base_face = source_faces[73]
        need(set(base_face["cycle"]) == set(clean.BASE), "source face index 73 is not base")
        need(clean.dot(base_face["n"], root_rows[73]) == base_face["h"], "row 73 is not exactly on the frozen base plane at gcd root")
        for face_index in expected_fan:
            cycle = cycles[face_index]
            normal = clean.cycle_normal(cycle, root_rows)
            anchor = root_rows[cycle[0]]
            need(all(clean.dot(normal, clean.sub(root_rows[label], anchor)) == 0 for label in clean.BASE), f"fan face f{face_index} does not coalesce with base plane at root")

        gcd_exact = common_gcd.exact()
        gcd_sha = sha("|".join(gcd_exact).encode())
        zero_ledger = [[name, family] for name, family in sorted(zero_keys)]
        zero_ledger_sha = sha((json.dumps(zero_ledger, separators=(",", ":")) + "\n").encode())
        inputs = {
            name: {"path": str(item.path.relative_to(ATTACK)), "bytes": item.size, "sha256": item.sha256, "snapshot_reads": 1}
            for name, item in snapshots.items()
        }
        payload = {
            "version": 1,
            "scope": "independent exact QQ-gcd and geometric-owner certificate for the first wall on the verified F21 ray",
            "certifier": {"path": "recovery2/main/post_transfer_round16/verify_exact_interior_first_wall.py", "sha256": sha(script_bytes)},
            "inputs": inputs,
            "total_ray": {"primitive_count": 12363, "family_counts": dict(family_counts), "path_primitive_sha256": path_digest.hexdigest()},
            "overlap_ledger": {
                "row_count": len(overlap_keys),
                "family_counts": dict(overlap_families),
                "all_scan_rows_equal_independent_polynomials": True,
                "all_brackets_contain_common_root": True,
                "exact_zero_set_at_root_count": len(zero_keys),
                "exact_zero_set_equals_overlap_ledger": True,
                "zero_key_ledger_sha256": zero_ledger_sha,
            },
            "common_factor": {
                "qq_monic_polynomial_exact": gcd_exact,
                "qq_monic_polynomial_sha256": gcd_sha,
                "degree": common_gcd.degree,
                "support_family_gcd_equal": True,
                "edge_family_gcd_equal": True,
                "root_exact": clean.qcompact(root),
                "root_decimal_readback": float(root),
                "root_strictly_after_t10": True,
            },
            "geometric_owner": {
                "kind": "row_73_enters_frozen_base_carrier_plane_and_base_fan_coalesces",
                "carrier_face_index": 73,
                "carrier_cycle": list(clean.BASE),
                "entering_witness": 73,
                "fan_faces": {str(index): list(cycle) for index, cycle in expected_fan.items()},
                "support_zero_counts_by_face": {str(key): value for key, value in sorted(support_by_face.items())},
                "edge_zero_owners": [list(edge) for edge in sorted(expected_edges)],
                "edge_zero_components_each": ["beta1", "beta2", "gram"],
                "local_vertex_owner_set": [0, 13, 14, 15, 16, 73],
                "row_73_exactly_on_base_plane_at_root": True,
                "all_four_fan_faces_coalesce_with_base_plane_at_root": True,
            },
            "verdict": "INDEPENDENT_EXACT_POST_C17_F21_FIRST_COMMON_WALL_GCD_PASS",
            "proof_status": "FIRST_WALL_IDENTITY_AND_GEOMETRIC_OWNER_ONLY_NO_POST_WALL_CELL",
            "winner_status": "NONWINNER_WALL_CERTIFICATE_ONLY",
            "claim_boundary": "The common rational first wall is identified exactly. No post-wall combinatorics or crossing is certified.",
        }
        output_bytes = (json.dumps(payload, indent=2) + "\n").encode()
        output_sha = sha(output_bytes)
        log = f"""# F21 first common wall log

- Verdict: `{payload['verdict']}`
- Certifier SHA256: `{sha(script_bytes)}`
- Output SHA256: `{output_sha}`
- Total-ray path SHA256: `{path_digest.hexdigest()}`
- Overlap rows: `82` (`61 support`, `21 edge_component`)
- Common QQ gcd degree: `1`
- Common QQ gcd SHA256: `{gcd_sha}`
- Exact root: `{clean.qcompact(root)}`

Independent reconstruction proves that all 82 hash-bound overlap polynomials,
and no other one of the 12,363 path primitives, vanish at the same rational
root.  The geometric owner is row 73 entering frozen base face f73, while fan
faces f76, f78, f84, and f85 coalesce with that carrier.  This certificate does
not create or certify a post-wall cell.
""".encode()

        for item in snapshots.values():
            item.unchanged()
        write_exclusive(OUTPUT, output_bytes)
        created.append(OUTPUT)
        write_exclusive(LOG, log)
        created.append(LOG)
        for item in snapshots.values():
            item.unchanged()
        directory_fd = os.open(HERE, os.O_RDONLY | getattr(os, "O_CLOEXEC", 0))
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
        print(payload["verdict"])
        print("root_exact", clean.qcompact(root))
        print("gcd_sha256", gcd_sha)
        print("output_sha256", output_sha)
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
        print("INDEPENDENT_EXACT_POST_C17_F21_FIRST_COMMON_WALL_GCD_FAIL", file=sys.stderr)
        print(repr(error), file=sys.stderr)
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()
