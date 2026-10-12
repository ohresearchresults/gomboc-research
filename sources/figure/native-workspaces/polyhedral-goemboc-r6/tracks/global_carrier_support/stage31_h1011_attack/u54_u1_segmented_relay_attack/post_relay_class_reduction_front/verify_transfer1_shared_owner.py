#!/usr/bin/env python3
"""Independent exact verification of ordered transfer epoch 1."""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

import front_common as fc


FAR_PARAMETER = Q(1, 100)
EXPECTED_ALIASES = {"edge:(1, 54):one_minus_t", "vertex:54:1"}
EXPECTED_FAR = {
    "class": [2, 3, 3],
    "stable_faces": fc.rc.FAR_FEATURES["stable_faces"],
    "unstable_vertices": [1, 8, 54],
    "saddle_edges": [[1, 54], [5, 6], [10, 11]],
}


def main():
    source_hashes = fc.bindings()
    endpoint_path = fc.HERE / "transfer1_far.csv"
    certificate_path = fc.HERE / "transfer1_certificate.json"
    certificate = json.loads(certificate_path.read_text())
    if certificate.get("verdict") != "EXACT_ORDERED_TRANSFER1_D_EPOCH_PASS":
        raise AssertionError("primary verdict")
    if fc.sha256(endpoint_path) != certificate["generated_file_sha256"][fc.rc.relative(endpoint_path)]:
        raise AssertionError("endpoint binding")
    source = fc.rc.ex.read_rows(fc.SOURCE)
    endpoint = fc.rc.ex.read_rows(endpoint_path)
    faces = json.loads(fc.FACES.read_text())
    velocity = {
        label: tuple((endpoint[label][axis] - source[label][axis]) / FAR_PARAMETER for axis in range(3))
        for label in source
    }
    path = fc.affine_path(source, velocity)
    if fc.evaluate_path(path, FAR_PARAMETER) != endpoint:
        raise AssertionError("affine endpoint reconstruction")
    rows = list(fc.rc.primitive_rows(path, faces))
    if len(rows) != 7922:
        raise AssertionError(("primitive count", len(rows)))
    lookup = {name: polynomial for name, polynomial, _family in rows}
    target = lookup["edge:(1, 54):one_minus_t"]
    aliases = {name for name, polynomial, _family in rows if polynomial == target}
    if aliases != EXPECTED_ALIASES:
        raise AssertionError(("zero family", aliases))
    root_packet = certificate["exact_root"]
    if fc.canonical_hash(target.exact()) != root_packet["polynomial_digest"]:
        raise AssertionError("target polynomial digest")
    lo, hi = Q(root_packet["lo"]), Q(root_packet["hi"])
    if not (Q(0) < lo < hi < FAR_PARAMETER):
        raise AssertionError("root interval bounds")
    root = fc.rc.ex.isolate_monotone_root(target, lo, hi, Q(1, 10**30))
    if root["lo"] != lo or root["hi"] != hi:
        raise AssertionError("root interval not canonical")
    if target.eval(Q(0)) >= 0 or target.eval(FAR_PARAMETER) <= 0:
        raise AssertionError("target orientation")

    digest = hashlib.sha256()
    leaves = 0
    worst = None
    strict_count = 0
    family_counts = {}
    for index, (name, polynomial, family) in enumerate(rows):
        family_counts[family] = family_counts.get(family, 0) + 1
        if name in aliases:
            continue
        source_value = polynomial.eval(Q(0))
        expected_sign = (source_value > 0) - (source_value < 0)
        sign, row_leaves, margin = fc.rc.ex.bernstein_sign(
            polynomial, Q(0), FAR_PARAMETER, max_depth=60
        )
        if sign != expected_sign:
            raise AssertionError(("non-target sign", name, expected_sign, sign))
        strict_count += 1; leaves += row_leaves
        worst = margin if worst is None else min(worst, margin)
        digest.update(f"{name}|{family}|{sign}|{'|'.join(polynomial.exact())}\n".encode())
        if index and index % 1000 == 0:
            print(json.dumps({"phase": "independent_strict_audit", "completed": index,
                              "total": len(rows)}), flush=True)
    strict = {
        "primitive_count": len(rows), "family_counts": family_counts,
        "strict_other_primitive_count": strict_count,
        "strict_other_bernstein_leaf_count": leaves,
        "strict_other_minimum_bernstein_log10_abs": worst,
        "strict_other_primitive_digest": digest.hexdigest(),
    }
    if strict != certificate["exhaustive_strict_other_primitives"]:
        raise AssertionError("strict receipt mismatch")

    source_checkpoint = fc.rc.exact_checkpoint(source, faces, fc.rc.FAR_FEATURES)
    endpoint_checkpoint = fc.rc.exact_checkpoint(endpoint, faces, EXPECTED_FAR)
    if source_checkpoint != certificate["source_checkpoint"]:
        raise AssertionError("source checkpoint mismatch")
    if endpoint_checkpoint != certificate["far_checkpoint"]:
        raise AssertionError("FAR checkpoint mismatch")
    sys.path.insert(0, str(fc.TRACK))
    from actual_hull_mechanics import evaluate
    labels = sorted(endpoint)
    points = np.asarray([[float(value) for value in endpoint[label]] for label in labels])
    signature = fc.chart.signature(evaluate(labels, points))
    actual_faces = fc.chart.common.actual_faces(labels, points)
    fresh_checks = {
        "fresh_face_ledger_unchanged": fc.rc.face_sets(actual_faces) == fc.rc.face_sets(faces),
        "fresh_f_vector": signature["f_vector"] == [61, 162, 103],
        "fresh_active_labels": signature["active_labels"] == fc.rc.EXPECTED_ACTIVE,
        "fresh_class": signature["class"] == EXPECTED_FAR["class"],
        "fresh_stable_faces": signature["stable_faces"] == EXPECTED_FAR["stable_faces"],
        "fresh_unstable_vertices": signature["unstable_vertices"] == EXPECTED_FAR["unstable_vertices"],
        "fresh_saddle_edges": signature["saddle_edges"] == EXPECTED_FAR["saddle_edges"],
        "fresh_37_rails": fc.rc.forced_rails().issubset(fc.rc.edge_set(actual_faces)),
        "row230_strict": all(Q(v) > 0 for v in fc.rc.row230_values(endpoint, faces).values()),
    }
    if not all(fresh_checks.values()):
        raise AssertionError(("fresh checks", fresh_checks, signature))
    packet = {
        "version": 1,
        "source_hashes": {
            **source_hashes, fc.rc.relative(endpoint_path): fc.sha256(endpoint_path),
            fc.rc.relative(certificate_path): fc.sha256(certificate_path),
            fc.rc.relative(Path(__file__)): fc.sha256(Path(__file__)),
        },
        "independent_reconstruction": "source plus endpoint-derived exact affine velocity",
        "complete_zero_family": sorted(aliases), "exact_root": root_packet,
        "exhaustive_strict_other_primitives": strict,
        "source_checkpoint": source_checkpoint, "far_checkpoint": endpoint_checkpoint,
        "fresh_signature": signature, "fresh_checks": fresh_checks,
        "verdict": "INDEPENDENT_EXACT_ORDERED_TRANSFER1_D_VERIFICATION_PASS",
    }
    output = fc.HERE / "transfer1_verification.json"
    output.write_text(json.dumps(packet, indent=2) + "\n")
    print(json.dumps({"verdict": packet["verdict"], "strict_other": strict_count,
                      "endpoint_sha256": fc.sha256(endpoint_path)}, indent=2), flush=True)


if __name__ == "__main__":
    main()
