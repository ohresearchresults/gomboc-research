#!/usr/bin/env python3
"""Clean-room exact crossing certificate for the first common F21 wall.

Qhull is used only to propose a fresh post-wall maximal-face ledger.  Every
accepted face, support, path primitive, centroid, mechanics sign, event factor,
root ordering, and rail statement is then reconstructed with Fraction.
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

import numpy as np
from scipy.spatial import ConvexHull


sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ATTACK = MAIN.parents[1]
F20 = MAIN / "post_transfer_round15"

ENGINE = HERE / "verify_exact_interior.py"
UNIT_VERIFICATION = HERE / "exact_interior_verification.json"
T10_VERIFICATION = HERE / "exact_interior_t10_verification.json"
WALL_CERTIFIER = HERE / "verify_exact_interior_first_wall.py"
WALL_VERIFICATION = HERE / "exact_interior_first_wall_verification.json"
SOURCE = F20 / "far.csv"
FACES = F20 / "post_faces.json"
UNIT_CANDIDATE = HERE / "exact_interior_candidate.csv"
PROPOSAL = HERE / "exact_interior_proposal.json"
SCAN = HERE / "exact_interior_event_scan.json"

PRE_OUT = HERE / "exact_interior_first_wall_pre.csv"
POST_OUT = HERE / "exact_interior_first_wall_post.csv"
FAR_OUT = HERE / "exact_interior_first_wall_far.csv"
POST_FACES_OUT = HERE / "exact_interior_first_wall_post_faces.json"
OUTPUT = HERE / "exact_interior_first_wall_transfer_verification.json"
LOG = HERE / "F21_FIRST_WALL_TRANSFER_LOG.md"

EXPECTED = {
    "engine": (ENGINE, 105094, "be98869c6cfad29aa0b96ffff2cfe4d5bbee034c2feb6a94a21d0a9b647518da"),
    "unit_verification": (UNIT_VERIFICATION, 227459, "7787d0c8a90346d23abac629d8678b82d504def1161aa4c5914016e81eb71d3b"),
    "t10_verification": (T10_VERIFICATION, 53696, "e705c68a75331cd5775337f50a6ae3ce058cc1f4622854339467780b271bcd60"),
    "wall_certifier": (WALL_CERTIFIER, 20401, "4f6c07b161b172871a0e0295071ee5973a6ead606aeb4c7e0c8591ffce554095"),
    "wall_verification": (WALL_VERIFICATION, 8675, "e68c9007d9d9dfb45b5a6b266d2337a8d3fecb756d10b99fbeac1cac010960ac"),
    "source": (SOURCE, 82321, "d34ebac9a1cfe81ce4d782049938ad68f1124eb82e3cd19342c30e5de14f39e3"),
    "faces": (FACES, 3283, "06b15585bd906ae1ee0cfc5aefff2a46a5e752a02dfb556abde9225e1df81c6b"),
    "unit_candidate": (UNIT_CANDIDATE, 343273, "52136b5bef94379e00445a0688865c56936ea7bc31db78e3f9fe90e8f755f110"),
    "proposal": (PROPOSAL, 1160861, "d1a481360259c1e5ecdeafbd9a4b2db38d7581c83ef995e475c295e71f17b30a"),
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
        need(observed == self.fingerprint, f"transfer input changed: {self.path}")

    def close(self):
        os.close(self.fd)


def freeze(name, path, expected_size, expected_hash):
    fd = os.open(path, os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0))
    try:
        before = os.fstat(fd)
        need(stat.S_ISREG(before.st_mode) and before.st_size == expected_size, f"transfer input type/size drift: {path}")
        data = bytearray()
        remaining = before.st_size
        while remaining:
            block = os.read(fd, min(1 << 20, remaining))
            need(block, f"short transfer snapshot: {path}")
            data.extend(block)
            remaining -= len(block)
        need(os.read(fd, 1) == b"", f"transfer input grew: {path}")
        after = os.fstat(fd)
        fingerprint = (
            before.st_dev, before.st_ino, before.st_size,
            before.st_mtime_ns, before.st_ctime_ns, before.st_mode,
        )
        need(fingerprint == (
            after.st_dev, after.st_ino, after.st_size,
            after.st_mtime_ns, after.st_ctime_ns, after.st_mode,
        ), f"transfer input mutated: {path}")
        frozen = bytes(data)
        need(sha(frozen) == expected_hash, f"transfer sha256 drift: {path.name}")
        return Snapshot(name, path, frozen, fd, fingerprint)
    except Exception:
        os.close(fd)
        raise


def load_engine(snapshot):
    module = ModuleType("frozen_f21_wall_transfer_engine")
    module.__file__ = str(snapshot.path)
    module.__package__ = ""
    need(module.__name__ not in sys.modules, "transfer engine already loaded")
    sys.modules[module.__name__] = module
    exec(compile(snapshot.data, str(snapshot.path), "exec"), module.__dict__)
    return module


def monic(clean, polynomial):
    need(polynomial.c != (Q(0),), "cannot make zero polynomial monic")
    return polynomial / polynomial.c[-1]


def divide_factor(clean, polynomial, factor):
    quotient, remainder = clean.poly_divmod(polynomial, factor)
    need(remainder.c == (Q(0),) and quotient * factor == polynomial, "non-exact wall factor division")
    return quotient


def factor_multiplicity(clean, polynomial, factor):
    multiplicity = 0
    cofactor = polynomial
    while cofactor.degree >= factor.degree:
        quotient, remainder = clean.poly_divmod(cofactor, factor)
        if remainder.c != (Q(0),):
            break
        cofactor = quotient
        multiplicity += 1
    need(multiplicity > 0, "wall polynomial lacks common factor")
    return multiplicity, cofactor


def strict_on_interval(clean, polynomial, left, right, expected_sign=None):
    need(left < right, "empty strictness interval")
    mapped = polynomial.affine(left, right)
    value = mapped.eval(Q(0))
    need(value != 0, "strictness interval starts on a root")
    sign = (1 if value > 0 else -1) if expected_sign is None else expected_sign
    result = clean.audit_strict_polynomial(mapped, sign)
    need(result["strict"], "exact Bernstein/Sturm interval proof failed")
    return result


def strict_horizon_or_failure(clean, polynomial, horizon, start_sign, max_depth=34):
    stack = [(Q(0), Q(horizon), 0)]
    while stack:
        left, right, depth = stack.pop()
        mapped = polynomial.affine(left, right)
        normalized = clean.Poly(tuple(start_sign * value for value in mapped.c))
        coefficients = clean.bernstein_coefficients(normalized)
        if all(value > 0 for value in coefficients):
            continue
        if depth >= max_depth:
            return False
        middle = (left + right) / 2
        stack.append((middle, right, depth + 1))
        stack.append((left, middle, depth + 1))
    return True


def isolate_first_root(clean, polynomial, left, right, iterations=52):
    need(polynomial.eval(left) != 0 and polynomial.eval(right) != 0, "root-search endpoint is a root")
    count = clean.sturm_root_count(polynomial, left, right)
    need(count > 0, "root-search polynomial has no root")
    lo, hi = left, right
    for _ in range(iterations):
        middle = (lo + hi) / 2
        value = polynomial.eval(middle)
        if value == 0:
            return {"exact": middle, "lo": middle, "hi": middle, "root_count": 1}
        left_count = clean.sturm_root_count(polynomial, lo, middle)
        if left_count:
            hi = middle
        else:
            lo = middle
    need(polynomial.eval(lo) != 0 and polynomial.eval(hi) != 0, "isolated root bracket endpoint is a root")
    bracket_count = clean.sturm_root_count(polynomial, lo, hi)
    need(bracket_count == 1, f"isolated next-root bracket has {bracket_count} roots")
    return {"exact": None, "lo": lo, "hi": hi, "root_count": 1}


def cycle_from_boundary(triangles, face_key):
    edge_counts = Counter()
    for triangle in triangles:
        for left, right in ((triangle[0], triangle[1]), (triangle[1], triangle[2]), (triangle[2], triangle[0])):
            edge_counts[tuple(sorted((left, right)))] += 1
    boundary = [edge for edge, count in edge_counts.items() if count == 1]
    adjacency = defaultdict(list)
    for left, right in boundary:
        adjacency[left].append(right)
        adjacency[right].append(left)
    need(set(adjacency) == set(face_key), f"Qhull face boundary omits/adds exact coplanar rows: {face_key}")
    need(all(len(neighbors) == 2 for neighbors in adjacency.values()), f"non-cycle Qhull face boundary: {face_key}")
    start = min(face_key)
    first = min(adjacency[start])
    cycle = [start, first]
    while True:
        previous, current = cycle[-2], cycle[-1]
        following = adjacency[current][0] if adjacency[current][1] == previous else adjacency[current][1]
        if following == start:
            break
        need(following not in cycle, f"repeated vertex in Qhull face cycle: {face_key}")
        cycle.append(following)
    need(len(cycle) == len(face_key), f"incomplete Qhull face cycle: {face_key}")
    return tuple(cycle)


def fresh_exact_hull(clean, rows):
    labels = sorted(rows)
    array = np.asarray([[float(value) for value in rows[label]] for label in labels], dtype=float)
    need(bool(np.all(np.isfinite(array))), "non-finite numerical hull proposal")
    hull = ConvexHull(array)
    groups = defaultdict(list)
    rejected_non_supporting_simplices = 0
    for simplex in hull.simplices:
        triangle = tuple(labels[int(index)] for index in simplex)
        anchor, left, right = (rows[label] for label in triangle)
        normal = clean.cross(clean.sub(left, anchor), clean.sub(right, anchor))
        need(normal != (Q(0), Q(0), Q(0)), f"flat numerical hull simplex: {triangle}")
        height = clean.dot(normal, anchor)
        values = {label: clean.dot(normal, point) - height for label, point in rows.items()}
        positive = any(value > 0 for value in values.values())
        negative = any(value < 0 for value in values.values())
        if positive and negative:
            # Near a high-multiplicity wall Qhull may triangulate the former
            # coplanar carrier numerically.  Such triangles are proposals only
            # and are rejected here; they can never enter the exact ledger.
            rejected_non_supporting_simplices += 1
            continue
        key = tuple(sorted(label for label, value in values.items() if value == 0))
        need(len(key) >= 3, f"invalid exact Qhull coplanar key: {triangle}")
        groups[key].append(triangle)
    cycles = [cycle_from_boundary(groups[key], key) for key in sorted(groups)]
    faces = clean.exactify_faces(rows, cycles)
    signatures = {tuple(sorted(face["cycle"])) for face in faces}
    need(signatures == set(groups), "fresh exact hull signature/group mismatch")
    mechanics = clean.mechanics_q(rows, faces)
    need(set(mechanics["active"]) == {labels[int(index)] for index in hull.vertices}, "fresh exact/numerical active hull vertices mismatch")
    need(mechanics["packet"]["f_vector"][0] - mechanics["packet"]["f_vector"][1] + mechanics["packet"]["f_vector"][2] == 2, "fresh exact hull Euler relation failed")
    return cycles, faces, mechanics, rejected_non_supporting_simplices


def path_rows(clean, source, delta, parameter):
    return {row_id: clean.add(point, clean.mul(delta[row_id], parameter)) for row_id, point in source.items()}


def audit_new_cell_path(clean, start_rows, end_rows, cycles):
    points = {
        row_id: tuple(clean.Poly((start_rows[row_id][axis], end_rows[row_id][axis] - start_rows[row_id][axis])) for axis in range(3))
        for row_id in start_rows
    }
    primitives = clean.path_primitives(points, cycles)
    keys = set()
    families = Counter()
    digest = hashlib.sha256()
    leaves = 0
    sturm = 0
    minimum = None
    owner = None
    for index, (name, polynomial, family) in enumerate(primitives):
        key = (name, family)
        need(key not in keys, f"duplicate post-wall path key: {key}")
        keys.add(key)
        value = polynomial.eval(Q(0))
        need(value != 0, f"zero post-wall path start primitive: {key}")
        result = clean.audit_strict_polynomial(polynomial, 1 if value > 0 else -1)
        leaves += result["leaves"]
        sturm += result["method"] == "sturm_fallback"
        families[family] += 1
        if result["minimum"] is not None and (minimum is None or result["minimum"] < minimum):
            minimum = result["minimum"]
            owner = {
                "index_zero_based": index, "name": name, "family": family,
                "interval_exact": [clean.qslash(result["minimum_interval"][0]), clean.qslash(result["minimum_interval"][1])],
                "coefficient_index": result["minimum_index"],
            }
        digest.update(f"{name}|{family}|{'|'.join(polynomial.exact())}\n".encode())
    need(minimum is not None and minimum > 0, "missing post-wall path margin")
    return {
        "primitive_count": len(primitives),
        "family_counts": dict(families),
        "all_strict": True,
        "bernstein_leaf_count": leaves,
        "sturm_fallback_count": sturm,
        "minimum_normalized_bernstein_coefficient_exact": clean.qcompact(minimum),
        "minimum_owner": owner,
        "path_primitive_sha256": digest.hexdigest(),
    }


def write_exclusive(path, data):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_CLOEXEC", 0), 0o644)
    try:
        offset = 0
        while offset < len(data):
            written = os.write(fd, data[offset:])
            need(written > 0, f"short transfer output write: {path}")
            offset += written
        os.fsync(fd)
    finally:
        os.close(fd)


def run():
    outputs = (PRE_OUT, POST_OUT, FAR_OUT, POST_FACES_OUT, OUTPUT, LOG)
    for path in outputs:
        need(not path.exists(), f"refusing to overwrite {path.name}")
    script_bytes = Path(__file__).read_bytes()
    snapshots, created = {}, []
    try:
        for name, (path, size, expected_hash) in EXPECTED.items():
            snapshots[name] = freeze(name, path, size, expected_hash)
        clean = load_engine(snapshots["engine"])
        unit_verification = clean.strict_json(snapshots["unit_verification"].data, "unit verification")
        t10_verification = clean.strict_json(snapshots["t10_verification"].data, "t10 verification")
        wall_verification = clean.strict_json(snapshots["wall_verification"].data, "wall verification")
        proposal = clean.strict_json(snapshots["proposal"].data, "proposal")
        scan = clean.strict_json(snapshots["scan"].data, "scan")
        need(unit_verification.get("verdict") == "INDEPENDENT_EXACT_POST_C17_F21_INTERIOR_VERIFICATION_PASS", "unit verification is not PASS")
        need(t10_verification.get("verdict") == "INDEPENDENT_EXACT_POST_C17_F21_T10_PRE_EVENT_EXTENSION_PASS", "t10 verification is not PASS")
        need(wall_verification.get("verdict") == "INDEPENDENT_EXACT_POST_C17_F21_FIRST_COMMON_WALL_GCD_PASS", "wall identity is not PASS")

        source = clean.read_rows(snapshots["source"].data, "F20 source")
        unit_candidate = clean.read_rows(snapshots["unit_candidate"].data, "unit candidate")
        cycles_payload = clean.strict_json(snapshots["faces"].data, "F20 faces")
        old_cycles = clean.validate_cycles(cycles_payload, source)
        source_faces = clean.exactify_faces(source, old_cycles)
        source_mechanics = clean.mechanics_q(source, source_faces)
        spec, _basis = clean.build_spec(source, source_mechanics["active"])
        direction = tuple(Q(value) for value in proposal["exact_coefficients"])
        delta = clean.displacement_from_coefficients(source, spec, direction)
        need(path_rows(clean, source, delta, Q(1)) == unit_candidate, "unit endpoint relation mismatch")

        points = {
            row_id: tuple(clean.Poly((source[row_id][axis], delta[row_id][axis])) for axis in range(3))
            for row_id in source
        }
        primitives = clean.path_primitives(points, old_cycles)
        need(len(primitives) == 12363, "total-ray primitive count mismatch")
        by_key = {}
        path_digest = hashlib.sha256()
        family_counts = Counter()
        for index, (name, polynomial, family) in enumerate(primitives):
            key = (name, family)
            need(key not in by_key, f"duplicate total-ray key at {index}: {key}")
            by_key[key] = polynomial
            family_counts[family] += 1
            path_digest.update(f"{name}|{family}|{'|'.join(polynomial.exact())}\n".encode())
        need(dict(family_counts) == clean.EXPECTED_FAMILIES, "total-ray family counts mismatch")
        need(path_digest.hexdigest() == clean.EXPECTED_PATH_DIGEST, "total-ray path digest mismatch")

        common_factor = clean.Poly(tuple(Q(value) for value in wall_verification["common_factor"]["qq_monic_polynomial_exact"]))
        root = Q(wall_verification["common_factor"]["root_exact"])
        need(common_factor.degree == 1 and common_factor.eval(root) == 0, "wall factor/root binding mismatch")
        overlap_rows = scan.get("overlapping_first_candidates")
        need(isinstance(overlap_rows, list) and len(overlap_rows) == 82, "overlap ledger count mismatch")
        overlap_keys = [(row["name"], row["family"]) for row in overlap_rows]
        need(len(set(overlap_keys)) == 82 and all(key in by_key for key in overlap_keys), "overlap key ledger mismatch")

        cofactor_ledger = []
        deflated = {}
        multiplicities = Counter()
        combined_cofactor_digest = hashlib.sha256()
        for key in overlap_keys:
            multiplicity, cofactor = factor_multiplicity(clean, by_key[key], common_factor)
            need(cofactor.eval(root) != 0, f"incomplete wall-factor deflation at {key}")
            multiplicities[multiplicity] += 1
            deflated[key] = cofactor
            record = {
                "name": key[0],
                "family": key[1],
                "wall_factor_multiplicity": multiplicity,
                "cofactor_degree": cofactor.degree,
                "cofactor_exact": cofactor.exact(),
                "cofactor_sha256": sha("|".join(cofactor.exact()).encode()),
                "cofactor_value_at_root_exact": clean.qcompact(cofactor.eval(root)),
            }
            cofactor_ledger.append(record)
            combined_cofactor_digest.update((json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n").encode())
        need(dict(multiplicities) == {1: 75, 2: 7}, f"unexpected wall multiplicities: {dict(multiplicities)}")

        epsilon = Q(1, 1_000_000)
        pre_parameter = root - epsilon
        post_parameter = root + epsilon
        far_parameter = root + 2 * epsilon
        need(Q(10) < pre_parameter < root < post_parameter < far_parameter, "bounded pre/post/FAR ordering failure")

        # The accepted t=10 sidecar proves the old cell through t=10.  Prove
        # every non-wall primitive, plus every fully deflated wall cofactor,
        # strictly root-free from 10 through post.  The only zero in this
        # bounded crossing is therefore the explicit linear common factor.
        crossing_leaves = 0
        crossing_sturm = 0
        for key, polynomial in by_key.items():
            proof_polynomial = deflated[key] if key in deflated else polynomial
            result = strict_on_interval(clean, proof_polynomial, Q(10), post_parameter)
            crossing_leaves += result["leaves"]
            crossing_sturm += result["method"] == "sturm_fallback"

        pre_rows = path_rows(clean, source, delta, pre_parameter)
        post_rows = path_rows(clean, source, delta, post_parameter)
        far_rows = path_rows(clean, source, delta, far_parameter)
        pre_faces = clean.exactify_faces(pre_rows, old_cycles)
        pre_mechanics = clean.mechanics_q(pre_rows, pre_faces)
        need(pre_mechanics["packet"] == source_mechanics["packet"] and pre_mechanics["signs"] == source_mechanics["signs"], "pre-event old cell/mechanics changed")

        post_cycles, post_faces, post_mechanics, post_rejected_qhull = fresh_exact_hull(clean, post_rows)
        far_cycles, far_faces_fresh, far_mechanics_fresh, far_rejected_qhull = fresh_exact_hull(clean, far_rows)
        post_signatures = {tuple(sorted(cycle)) for cycle in post_cycles}
        far_signatures = {tuple(sorted(cycle)) for cycle in far_cycles}
        need(post_signatures == far_signatures, "fresh post/FAR hull face signatures differ")
        far_faces = clean.exactify_faces(far_rows, post_cycles)
        far_mechanics = clean.mechanics_q(far_rows, far_faces)
        need(far_mechanics["packet"] == far_mechanics_fresh["packet"], "prescribed/fresh FAR mechanics packet mismatch")
        need(post_mechanics["packet"] == far_mechanics["packet"], "post/FAR mechanics packet changed")
        need(post_mechanics["signs"] == far_mechanics["signs"], "post/FAR mechanics sign cell changed")
        need(post_mechanics["active"] == source_mechanics["active"], "post-wall active row ledger changed unexpectedly")
        rails = clean.forced_rails()
        need(not (rails - set(post_mechanics["incidence"])) and not (rails - set(far_mechanics["incidence"])), "post-wall forced rails missing")
        post_path = audit_new_cell_path(clean, post_rows, far_rows, post_cycles)

        old_signatures = {tuple(sorted(cycle)) for cycle in old_cycles}
        removed_faces = sorted(old_signatures - post_signatures)
        added_faces = sorted(post_signatures - old_signatures)
        need(bool(removed_faces) and bool(added_faces), "wall crossing did not change maximal-face ledger")
        need(tuple(clean.BASE) in removed_faces, "old base carrier face was not removed at crossing")
        need(all(tuple(sorted(old_cycles[index])) in removed_faces for index in (76, 78, 84, 85)), "old four-face fan was not fully removed")

        pre_bytes = clean.candidate_csv_bytes(pre_rows)
        post_bytes = clean.candidate_csv_bytes(post_rows)
        far_bytes = clean.candidate_csv_bytes(far_rows)
        faces_payload = {
            "version": 1,
            "scope": "fresh exact maximal-face ledger in first post-F21-common-wall cell",
            "parameter_source": "exact_interior_first_wall_transfer_verification.json",
            "maximal_face_cycles": [list(face["cycle"]) for face in post_faces],
            "f_vector": post_mechanics["packet"]["f_vector"],
            "class": post_mechanics["packet"]["class"],
            "active_vertices": post_mechanics["active"],
            "true_edges": [list(edge) for edge in sorted(post_mechanics["incidence"])],
            "all_37_forced_rails_present": True,
            "verdict": "FRESH_EXACT_F21_FIRST_WALL_POST_CELL_FACE_LEDGER_PASS",
        }
        faces_bytes = (json.dumps(faces_payload, indent=2) + "\n").encode()

        inputs = {
            name: {"path": str(item.path.relative_to(ATTACK)), "bytes": item.size, "sha256": item.sha256, "snapshot_reads": 1}
            for name, item in snapshots.items()
        }
        output_records = {
            "pre": {"path": "recovery2/main/post_transfer_round16/exact_interior_first_wall_pre.csv", "bytes": len(pre_bytes), "sha256": sha(pre_bytes)},
            "post": {"path": "recovery2/main/post_transfer_round16/exact_interior_first_wall_post.csv", "bytes": len(post_bytes), "sha256": sha(post_bytes)},
            "far": {"path": "recovery2/main/post_transfer_round16/exact_interior_first_wall_far.csv", "bytes": len(far_bytes), "sha256": sha(far_bytes)},
            "post_faces": {"path": "recovery2/main/post_transfer_round16/exact_interior_first_wall_post_faces.json", "bytes": len(faces_bytes), "sha256": sha(faces_bytes)},
        }
        payload = {
            "version": 1,
            "scope": "clean-room exact crossing of the first common F21 wall into the next strict cell",
            "verifier": {"path": "recovery2/main/post_transfer_round16/verify_exact_interior_first_wall_transfer.py", "sha256": sha(script_bytes), "qhull_role": "face proposal only; every accepted statement is exact"},
            "inputs": inputs,
            "event": {
                "common_factor_exact": common_factor.exact(),
                "root_exact": clean.qcompact(root),
                "zero_family_count": 82,
                "zero_family_counts": {"support": 61, "edge_component": 21},
                "wall_factor_multiplicity_counts": {str(key): value for key, value in sorted(multiplicities.items())},
                "complete_cofactor_count": len(cofactor_ledger),
                "complete_cofactor_ledger_sha256": combined_cofactor_digest.hexdigest(),
                "complete_cofactors": cofactor_ledger,
                "all_other_12363_minus_82_primitives_strict_across_pre_post": True,
                "all_82_deflated_cofactors_strict_across_pre_post": True,
                "bounded_crossing_exact_bernstein_leaf_count": crossing_leaves,
                "bounded_crossing_exact_sturm_fallback_count": crossing_sturm,
                "accepted_t0_to_t10_unit_primitive_count": 12363,
                "geometric_owner": wall_verification["geometric_owner"],
            },
            "ordering": {
                "locator_horizon_16_failure_count": scan["horizon_audits"][-1]["failure_count"],
                "first_wall_exact_zero_count": 82,
                "horizon_failures_are_not_claimed_as_first_wall_zero_family": True,
                "bounded_epsilon_exact": clean.qcompact(epsilon),
                "pre_parameter_exact": clean.qcompact(pre_parameter),
                "post_parameter_exact": clean.qcompact(post_parameter),
                "far_parameter_exact": clean.qcompact(far_parameter),
                "strict_order": "10 < pre < first_root < post < FAR",
                "post_to_far_fresh_cell_has_no_next_root": True,
            },
            "pre_cell": {
                "all_12363_old_cell_primitives_strict_from_0_through_pre": True,
                "proof_decomposition": "accepted exact t0-to-t10 sidecar plus full bounded exact nonwall/deflated proof t10-to-post",
                "f_vector": pre_mechanics["packet"]["f_vector"],
                "class": pre_mechanics["packet"]["class"],
            },
            "topology_change": {
                "old_f_vector": source_mechanics["packet"]["f_vector"],
                "new_f_vector": post_mechanics["packet"]["f_vector"],
                "removed_face_count": len(removed_faces),
                "removed_faces": [list(face) for face in removed_faces],
                "added_face_count": len(added_faces),
                "added_faces": [list(face) for face in added_faces],
                "fresh_post_and_far_hulls_equal": True,
                "qhull_non_supporting_simplices_rejected": {
                    "post": post_rejected_qhull,
                    "far": far_rejected_qhull,
                },
                "all_accepted_faces_exact_supporting_and_closed_manifold": True,
            },
            "post_cell": {
                "f_vector": post_mechanics["packet"]["f_vector"],
                "class": post_mechanics["packet"]["class"],
                "active_vertices": post_mechanics["active"],
                "stable_faces": post_mechanics["packet"]["stable_faces"],
                "unstable_vertices": post_mechanics["packet"]["unstable_vertices"],
                "saddle_edges": post_mechanics["packet"]["saddle_edges"],
                "volume_exact": clean.qslash(post_mechanics["volume"]),
                "centroid_exact": [clean.qslash(value) for value in post_mechanics["centroid"]],
                "same_exact_hull_and_mechanics_sign_cell_post_to_far": True,
                "forced_rail_count": 37,
                "all_forced_rails_present": True,
                "post_to_far_path": post_path,
            },
            "outputs": output_records,
            "verdict": "INDEPENDENT_EXACT_POST_C17_F21_FIRST_COMMON_WALL_TRANSFER_PASS",
            "proof_status": "EXACT_FIRST_WALL_CROSSING_AND_NEXT_STRICT_CELL_THROUGH_FAR",
            "winner_status": "NONWINNER_TRANSFER_ONLY",
            "claim_boundary": "The first common wall and the strict post-wall cell through FAR are certified. The next root is not crossed.",
        }
        output_bytes = (json.dumps(payload, indent=2) + "\n").encode()
        output_sha = sha(output_bytes)
        log = f"""# F21 first common wall transfer log

- Verdict: `{payload['verdict']}`
- Verifier SHA256: `{sha(script_bytes)}`
- Verification SHA256: `{output_sha}`
- First root: `{clean.qcompact(root)}`
- Pre/Post/FAR: `{clean.qcompact(pre_parameter)}` / `{clean.qcompact(post_parameter)}` / `{clean.qcompact(far_parameter)}`
- Bounded exact epsilon: `{clean.qcompact(epsilon)}`
- Old/new f-vector: `{source_mechanics['packet']['f_vector']}` / `{post_mechanics['packet']['f_vector']}`
- New class: `{post_mechanics['packet']['class']}`
- Removed/added maximal faces: `{len(removed_faces)}` / `{len(added_faces)}`
- Post-to-FAR primitive count: `{post_path['primitive_count']}`

The 82-row wall family has exact complete cofactors and multiplicities; the
other 12,281 total-ray primitives and all deflated cofactors are strict across
the chosen pre/post bracket.  The post-wall hull was proposed afresh and then
verified exactly through FAR with fresh centroid/mechanics and all 37 rails.
The next root remains strictly beyond FAR.
""".encode()

        for item in snapshots.values():
            item.unchanged()
        for path, data in (
            (PRE_OUT, pre_bytes), (POST_OUT, post_bytes), (FAR_OUT, far_bytes),
            (POST_FACES_OUT, faces_bytes), (OUTPUT, output_bytes), (LOG, log),
        ):
            write_exclusive(path, data)
            created.append(path)
        for item in snapshots.values():
            item.unchanged()
        directory_fd = os.open(HERE, os.O_RDONLY | getattr(os, "O_CLOEXEC", 0))
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
        print(payload["verdict"])
        print("verification_sha256", output_sha)
        print("pre_sha256", sha(pre_bytes))
        print("post_sha256", sha(post_bytes))
        print("far_sha256", sha(far_bytes))
        print("faces_sha256", sha(faces_bytes))
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
        print("INDEPENDENT_EXACT_POST_C17_F21_FIRST_COMMON_WALL_TRANSFER_FAIL", file=sys.stderr)
        print(repr(error), file=sys.stderr)
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()
