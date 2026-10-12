#!/usr/bin/env python3
"""Primary exact certificate for ordered transfer epoch 1 (D resurrection)."""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

import front_common as fc


FAR_PARAMETER = Q(1, 100)
ROOT_WIDTH = Q(1, 10**30)
EXPECTED_ALIASES = {"edge:(1, 54):one_minus_t", "vertex:54:1"}
EXPECTED_FAR = {
    "class": [2, 3, 3],
    "stable_faces": fc.rc.FAR_FEATURES["stable_faces"],
    "unstable_vertices": [1, 8, 54],
    "saddle_edges": [[1, 54], [5, 6], [10, 11]],
}


def reconstruct_velocity(source, audit):
    labels, _float_modes, mode_names, exact_modes, plane_normal = fc.exact_modes(source)
    packet = audit["pairs"]["U1_H1011"]["coefficients"]
    coefficients = [Q(packet.get(repr(name), "0")) for name in mode_names]
    if sum(value != 0 for value in coefficients) != audit["pairs"]["U1_H1011"]["active_mode_count"]:
        raise AssertionError("active coefficient count drift")
    return labels, fc.combine_velocity(exact_modes, coefficients), plane_normal


def strict_receipt(rows, excluded, hi):
    digest = hashlib.sha256()
    family_counts = {}
    leaves = 0
    worst = None
    count = 0
    for index, (name, polynomial, family) in enumerate(rows):
        family_counts[family] = family_counts.get(family, 0) + 1
        if name in excluded:
            continue
        source_value = polynomial.eval(Q(0))
        expected = (source_value > 0) - (source_value < 0)
        sign, row_leaves, margin = fc.rc.ex.bernstein_sign(
            polynomial, Q(0), hi, max_depth=60
        )
        if sign != expected:
            raise AssertionError(("non-target not strict", name, expected, sign))
        count += 1
        leaves += row_leaves
        worst = margin if worst is None else min(worst, margin)
        digest.update(f"{name}|{family}|{sign}|{'|'.join(polynomial.exact())}\n".encode())
        if index and index % 1000 == 0:
            print(json.dumps({"phase": "strict_primitive_audit", "completed": index,
                              "total": len(rows)}), flush=True)
    return {
        "primitive_count": len(rows), "family_counts": family_counts,
        "strict_other_primitive_count": count,
        "strict_other_bernstein_leaf_count": leaves,
        "strict_other_minimum_bernstein_log10_abs": worst,
        "strict_other_primitive_digest": digest.hexdigest(),
    }


def fresh_audit(endpoint, labels, faces):
    sys.path.insert(0, str(fc.TRACK))
    from actual_hull_mechanics import evaluate
    points = np.asarray([[float(value) for value in endpoint[label]] for label in labels])
    mechanics = evaluate(labels, points)
    actual_faces = fc.chart.common.actual_faces(labels, points)
    signature = fc.chart.signature(mechanics)
    checks = {
        "fresh_face_ledger_unchanged": fc.rc.face_sets(actual_faces) == fc.rc.face_sets(faces),
        "fresh_f_vector": signature["f_vector"] == [61, 162, 103],
        "fresh_active_labels": signature["active_labels"] == fc.rc.EXPECTED_ACTIVE,
        "fresh_class": signature["class"] == EXPECTED_FAR["class"],
        "fresh_stable_faces": signature["stable_faces"] == EXPECTED_FAR["stable_faces"],
        "fresh_unstable_vertices": signature["unstable_vertices"] == EXPECTED_FAR["unstable_vertices"],
        "fresh_saddle_edges": signature["saddle_edges"] == EXPECTED_FAR["saddle_edges"],
        "fresh_37_rails": fc.rc.forced_rails().issubset(fc.rc.edge_set(actual_faces)),
    }
    return signature, checks


def main():
    source_hashes = fc.bindings()
    audit_path = fc.HERE / "reachability_audit.json"
    audit = json.loads(audit_path.read_text())
    if audit.get("verdict") != "EXACT_POST_RELAY_FIRST_JET_REACHABILITY_AUDIT_PASS":
        raise AssertionError("reachability audit verdict")
    source = fc.rc.ex.read_rows(fc.SOURCE)
    faces = json.loads(fc.FACES.read_text())
    labels, velocity, plane_normal = reconstruct_velocity(source, audit)
    path = fc.affine_path(source, velocity)
    endpoint = fc.evaluate_path(path, FAR_PARAMETER)
    endpoint_path = fc.HERE / "transfer1_far.csv"
    endpoint_path.write_bytes(fc.rc.exact_csv_bytes(endpoint))
    print(json.dumps({"phase": "endpoint_materialized", "sha256": fc.sha256(endpoint_path)}), flush=True)

    rows = list(fc.rc.primitive_rows(path, faces))
    if len(rows) != 7922:
        raise AssertionError(("primitive count", len(rows)))
    lookup = {name: polynomial for name, polynomial, _family in rows}
    target = lookup["edge:(1, 54):one_minus_t"]
    aliases = {name for name, polynomial, _family in rows if polynomial == target}
    if aliases != EXPECTED_ALIASES:
        raise AssertionError(("complete zero family", sorted(aliases)))
    if target.eval(Q(0)) >= 0 or target.eval(FAR_PARAMETER) <= 0:
        raise AssertionError("target endpoint signs")
    root = fc.rc.ex.isolate_monotone_root(target, Q(0), FAR_PARAMETER, ROOT_WIDTH)
    strict = strict_receipt(rows, aliases, FAR_PARAMETER)

    source_checkpoint = fc.rc.exact_checkpoint(source, faces, fc.rc.FAR_FEATURES)
    endpoint_checkpoint = fc.rc.exact_checkpoint(endpoint, faces, EXPECTED_FAR)
    signature, fresh_checks = fresh_audit(endpoint, labels, faces)
    if not all(fresh_checks.values()):
        raise AssertionError(("fresh endpoint", fresh_checks, signature))
    row230 = {
        "source": fc.rc.row230_values(source, faces),
        "endpoint": fc.rc.row230_values(endpoint, faces),
    }
    if any(Q(value) <= 0 for packet in row230.values() for value in packet.values()):
        raise AssertionError("row230 strictness")
    pre_sign, pre_leaves, pre_margin = fc.rc.ex.bernstein_sign(
        target, Q(0), root["lo"], max_depth=60
    )
    post_sign, post_leaves, post_margin = fc.rc.ex.bernstein_sign(
        target, root["hi"], FAR_PARAMETER, max_depth=60
    )
    if (pre_sign, post_sign) != (-1, 1):
        raise AssertionError(("target open signs", pre_sign, post_sign))

    certificate_path = fc.HERE / "transfer1_certificate.json"
    payload = {
        "version": 1,
        "event": "ordered transfer epoch 1: D reverse U54/H(1,54) resurrection",
        "source_hashes": {
            **source_hashes,
            fc.rc.relative(audit_path): fc.sha256(audit_path),
            fc.rc.relative(fc.HERE / "front_common.py"): fc.sha256(fc.HERE / "front_common.py"),
            fc.rc.relative(Path(__file__)): fc.sha256(Path(__file__)),
        },
        "reachability_ray": {
            "pair": "U1_H1011", "coefficient_digest": audit["pairs"]["U1_H1011"]["coefficient_digest"],
            "far_parameter": fc.rc.ex.qs(FAR_PARAMETER), "base_plane_normal": plane_normal.tolist(),
        },
        "exact_root": {
            "complete_zero_family": sorted(aliases), "lo": fc.rc.ex.qs(root["lo"]),
            "hi": fc.rc.ex.qs(root["hi"]),
            "decimal_interval": [float(root["lo"]), float(root["hi"])],
            "value_lo": fc.rc.ex.qs(root["value_lo"]), "value_hi": fc.rc.ex.qs(root["value_hi"]),
            "polynomial_degree": target.degree, "polynomial_exact": target.exact(),
            "polynomial_digest": fc.canonical_hash(target.exact()),
            "derivative_sign": root["derivative_sign"], "simple_root": True,
            "pre_sign": pre_sign, "post_sign": post_sign,
            "pre_bernstein_leaf_count": pre_leaves, "post_bernstein_leaf_count": post_leaves,
            "pre_minimum_bernstein_log10_abs": pre_margin,
            "post_minimum_bernstein_log10_abs": post_margin,
        },
        "exhaustive_strict_other_primitives": strict,
        "class_transition": {"before": fc.rc.FAR_FEATURES, "after": EXPECTED_FAR,
                             "delta": [0, 1, 1]},
        "source_checkpoint": source_checkpoint, "far_checkpoint": endpoint_checkpoint,
        "fresh_signature": signature, "fresh_checks": fresh_checks,
        "row230_squared_margins": row230,
        "h910_nonresurrection": {
            "edge_one_minus_t_sign": qsign(lookup["edge:(9, 10):one_minus_t"].eval(FAR_PARAMETER)),
            "vertex_10_9_sign": qsign(lookup["vertex:10:9"].eval(FAR_PARAMETER)),
        },
        "generated_file_sha256": {fc.rc.relative(endpoint_path): fc.sha256(endpoint_path)},
        "verdict": "EXACT_ORDERED_TRANSFER1_D_EPOCH_PASS",
    }
    if payload["h910_nonresurrection"] != {"edge_one_minus_t_sign": -1, "vertex_10_9_sign": -1}:
        raise AssertionError(("H910 changed in transfer1", payload["h910_nonresurrection"]))
    certificate_path.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({"verdict": payload["verdict"], "root": payload["exact_root"]["decimal_interval"],
                      "strict_other": strict["strict_other_primitive_count"],
                      "class_transition": payload["class_transition"],
                      "far_sha256": fc.sha256(endpoint_path)}, indent=2), flush=True)


def qsign(value):
    return (value > 0) - (value < 0)


if __name__ == "__main__":
    main()
