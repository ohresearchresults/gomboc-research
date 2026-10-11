#!/usr/bin/env python3
"""Locate and exhaustively order the first stable-carrier circuit flip."""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

import front_common as fc


OUTPUT = fc.HERE / "flip_8245_locator.json"
PRE_CSV = fc.HERE / "flip_8245_pre.csv"
POST_CSV = fc.HERE / "flip_8245_post.csv"
FAR_CSV = fc.HERE / "flip_8245_far.csv"


def poly_divmod(numerator: fc.ex.P, denominator: fc.ex.P):
    if denominator == fc.ex.P.zero():
        raise ZeroDivisionError
    remainder = list(numerator.c)
    quotient = [Q(0)] * max(1, numerator.degree - denominator.degree + 1)
    while len(remainder) - 1 >= denominator.degree and any(remainder):
        degree = len(remainder) - 1 - denominator.degree
        factor = remainder[-1] / denominator.c[-1]
        quotient[degree] += factor
        for offset, value in enumerate(denominator.c):
            remainder[degree + offset] -= factor * value
        while len(remainder) > 1 and remainder[-1] == 0:
            remainder.pop()
    return fc.ex.P(tuple(quotient)), fc.ex.P(tuple(remainder))


def circuit_multiplicity(polynomial, circuit):
    multiplicity = 0
    cofactor = polynomial
    while cofactor.degree >= circuit.degree:
        quotient, remainder = poly_divmod(cofactor, circuit)
        if remainder != fc.ex.P.zero():
            break
        cofactor = quotient
        multiplicity += 1
    return multiplicity, cofactor


def polynomial_digest(rows) -> str:
    digest = hashlib.sha256()
    for name, polynomial, family in rows:
        digest.update(name.encode())
        digest.update(b"|")
        digest.update(family.encode())
        digest.update(b"|")
        digest.update("|".join(polynomial.exact()).encode())
        digest.update(b"\n")
    return digest.hexdigest()


def strict_interval(rows, lo, hi, label):
    digest = hashlib.sha256()
    leaves = 0
    worst = None
    family_counts = {}
    for name, polynomial, family in rows:
        sign, count, margin = fc.ex.bernstein_sign(polynomial, lo, hi, max_depth=40)
        leaves += count
        worst = margin if worst is None else min(worst, margin)
        family_counts[family] = family_counts.get(family, 0) + 1
        digest.update(name.encode())
        digest.update(b"|")
        digest.update(str(sign).encode())
        digest.update(b"|")
        digest.update("|".join(polynomial.exact()).encode())
        digest.update(b"\n")
    return {
        "label": label,
        "lo": fc.ex.qs(lo),
        "hi": fc.ex.qs(hi),
        "strict_polynomial_count": len(rows),
        "family_counts": family_counts,
        "bernstein_leaf_count": leaves,
        "min_bernstein_coefficient_log10_abs": worst,
        "signed_primitive_digest": digest.hexdigest(),
    }


def root_record(root):
    return {
        "lo": fc.ex.qs(root["lo"]),
        "hi": fc.ex.qs(root["hi"]),
        "midpoint_decimal": float((root["lo"] + root["hi"]) / 2),
        "width_decimal": float(root["hi"] - root["lo"]),
        "value_lo_sign": (root["value_lo"] > 0) - (root["value_lo"] < 0),
        "value_hi_sign": (root["value_hi"] > 0) - (root["value_hi"] < 0),
        "value_lo_log10_abs": fc.ex.qlog10(root["value_lo"]),
        "value_hi_log10_abs": fc.ex.qlog10(root["value_hi"]),
        "derivative_sign": root["derivative_sign"],
        "derivative_bernstein_leaves": root["derivative_bernstein_leaves"],
    }


def face_difference(before, after):
    before_faces = {tuple(sorted(face)) for face in before}
    after_faces = {tuple(sorted(face)) for face in after}
    before_edges = fc.edge_set(before)
    after_edges = fc.edge_set(after)
    return {
        "faces_removed": [list(row) for row in sorted(before_faces - after_faces)],
        "faces_added": [list(row) for row in sorted(after_faces - before_faces)],
        "edges_removed": [list(row) for row in sorted(before_edges - after_edges)],
        "edges_added": [list(row) for row in sorted(after_edges - before_edges)],
    }


def main() -> None:
    diagnosis = fc.validate_lineage()
    source = fc.ex.read_rows(fc.SOURCE)
    velocity = fc.selected_velocity(source, diagnosis)
    path = fc.affine_path(source, velocity)

    source_faces, source_hull = fc.fresh.fresh_maximal_faces(source)
    source_checkpoint = fc.checkpoint(source, source_faces, fc.SOURCE_FEATURES)
    if fc.fresh.face_hash(source_faces) != diagnosis["fresh_face_hash"]:
        raise AssertionError("source face hash differs from diagnosis")

    circuit = fc.circuit_polynomial(path)
    root = fc.ex.isolate_monotone_root(
        circuit,
        Q(2_546_739, 10**9),
        Q(2_546_740, 10**9),
        Q(1, 10**30),
    )
    circuit_pre = fc.ex.bernstein_sign(circuit, Q(0), root["lo"], max_depth=40)
    circuit_post = fc.ex.bernstein_sign(circuit, root["hi"], fc.FAR_T, max_depth=40)
    if circuit_pre[0] == circuit_post[0]:
        raise AssertionError("circuit does not change sign")

    old_rows = list(fc.primitive_rows(path, source_faces))
    if len(old_rows) != 7_922:
        raise AssertionError(("old primitive count", len(old_rows)))
    zero_family = []
    strict_old_rows = []
    for name, polynomial, family in old_rows:
        if not polynomial.eval(Q(0)):
            raise AssertionError(("zero source primitive", name))
        multiplicity, cofactor = circuit_multiplicity(polynomial, circuit)
        if multiplicity:
            sign, leaves, margin = fc.ex.bernstein_sign(
                cofactor, Q(0), fc.FAR_T, max_depth=40
            )
            zero_family.append({
                "name": name,
                "family": family,
                "circuit_multiplicity": multiplicity,
                "cofactor_degree": cofactor.degree,
                "cofactor_sign": sign,
                "cofactor_bernstein_leaves": leaves,
                "cofactor_min_log10_abs": margin,
                "cofactor_digest": hashlib.sha256("|".join(cofactor.exact()).encode()).hexdigest(),
            })
        else:
            strict_old_rows.append((name, polynomial, family))
    if not zero_family:
        raise AssertionError("empty first-zero family")
    old_strict = strict_interval(
        strict_old_rows, Q(0), root["hi"], "source_to_just_after_root_nonfamily"
    )

    pre = fc.evaluate_path(path, fc.PRE_T)
    post = fc.evaluate_path(path, fc.POST_T)
    far = fc.evaluate_path(path, fc.FAR_T)
    pre_faces, pre_hull = fc.fresh.fresh_maximal_faces(pre)
    post_faces, post_hull = fc.fresh.fresh_maximal_faces(post)
    far_faces, far_hull = fc.fresh.fresh_maximal_faces(far)
    if {tuple(sorted(face)) for face in pre_faces} != {
        tuple(sorted(face)) for face in source_faces
    }:
        raise AssertionError("pre faces differ from source")
    if {tuple(sorted(face)) for face in post_faces} != {
        tuple(sorted(face)) for face in far_faces
    }:
        raise AssertionError("post and far ledgers differ")

    pre_checkpoint = fc.checkpoint(pre, pre_faces, fc.SOURCE_FEATURES)
    post_checkpoint = fc.checkpoint(post, post_faces, fc.POST_FEATURES)
    far_checkpoint = fc.checkpoint(far, far_faces, fc.POST_FEATURES)
    topology = face_difference(source_faces, post_faces)
    expected_topology = {
        "faces_removed": [[7, 8, 245], [8, 245, 246]],
        "faces_added": [[7, 8, 246], [7, 245, 246]],
        "edges_removed": [[8, 245]],
        "edges_added": [[7, 246]],
    }
    if topology != expected_topology:
        raise AssertionError(("unexpected topology transfer", topology))

    new_rows = list(fc.primitive_rows(path, post_faces))
    if len(new_rows) != 7_922:
        raise AssertionError(("new primitive count", len(new_rows)))
    new_strict = strict_interval(
        new_rows, root["hi"], fc.FAR_T, "just_after_root_to_far_recharted"
    )

    for output, rows in ((PRE_CSV, pre), (POST_CSV, post), (FAR_CSV, far)):
        fc.atomic_write(output, fc.exact_csv_bytes(rows))

    payload = {
        "schema": "stable_first_topology_front.flip_8245_locator",
        "schema_version": 1,
        "report_type": "exact_first_event_locator",
        "scope": (
            "Exact rational ordering of all 7,922 fixed-ledger primitives before and "
            "after the first {7,8,245,246} circuit rechart on the selected stable-first ray."
        ),
        "source_hashes": fc.bindings((Path(__file__).resolve(), fc.HERE / "front_common.py")),
        "source_hull": source_hull,
        "source_face_hash": fc.fresh.face_hash(source_faces),
        "source_checkpoint": source_checkpoint,
        "selected_ray": {
            "origin": fc.relative(fc.SOURCE),
            "diagnosis_pair": "(10, 11)",
            "coefficient_packet_digest": diagnosis["pairs"]["(10, 11)"]["coefficient_digest"],
            "velocity_digest": fc.canonical_hash({
                str(label): [fc.ex.qs(value) for value in velocity[label]]
                for label in sorted(velocity)
            }),
            "pre_t": fc.ex.qs(fc.PRE_T),
            "post_t": fc.ex.qs(fc.POST_T),
            "far_t": fc.ex.qs(fc.FAR_T),
        },
        "first_event": {
            "owner": "circuit:{7,8,245,246}",
            "old_edge": [8, 245],
            "new_edge": [7, 246],
            "circuit_polynomial_degree": circuit.degree,
            "circuit_polynomial_exact": circuit.exact(),
            "circuit_polynomial_digest": hashlib.sha256("|".join(circuit.exact()).encode()).hexdigest(),
            "root": root_record(root),
            "circuit_sign_before": circuit_pre[0],
            "circuit_sign_after": circuit_post[0],
            "complete_zero_family_count": len(zero_family),
            "complete_zero_family": zero_family,
            "old_nonfamily_strict_audit": old_strict,
            "old_complete_primitive_count": len(old_rows),
            "old_complete_primitive_digest": polynomial_digest(old_rows),
        },
        "rechart": {
            "topology_transfer": topology,
            "post_face_hash": fc.fresh.face_hash(post_faces),
            "new_complete_primitive_count": len(new_rows),
            "new_complete_primitive_digest": polynomial_digest(new_rows),
            "new_strict_audit": new_strict,
        },
        "checkpoints": {
            "pre": {"t": fc.ex.qs(fc.PRE_T), "file": PRE_CSV.name, "sha256": fc.sha256(PRE_CSV), "fresh_hull": pre_hull, "exact": pre_checkpoint},
            "post": {"t": fc.ex.qs(fc.POST_T), "file": POST_CSV.name, "sha256": fc.sha256(POST_CSV), "fresh_hull": post_hull, "exact": post_checkpoint},
            "far": {"t": fc.ex.qs(fc.FAR_T), "file": FAR_CSV.name, "sha256": fc.sha256(FAR_CSV), "fresh_hull": far_hull, "exact": far_checkpoint},
        },
        "conclusion": (
            "The first event is the exact (8,245)->(7,246) circuit flip.  It preserves "
            "class (2,2,2), all 61 rows, all 37 rails, strict row230 margins and dead H(9,10), "
            "while transferring the extra stable face from (7,8,245) to (7,8,246)."
        ),
        "verdict": "EXACT_FIRST_8245_STABLE_CARRIER_FLIP_LOCATOR_PASS",
    }
    fc.atomic_write(OUTPUT, (json.dumps(payload, indent=2) + "\n").encode())
    print(json.dumps({
        "verdict": payload["verdict"],
        "root": payload["first_event"]["root"]["midpoint_decimal"],
        "zero_family_count": len(zero_family),
        "zero_family": [row["name"] for row in zero_family],
        "pre_sha256": fc.sha256(PRE_CSV),
        "post_sha256": fc.sha256(POST_CSV),
        "far_sha256": fc.sha256(FAR_CSV),
    }, indent=2))


if __name__ == "__main__":
    main()
