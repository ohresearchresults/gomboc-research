#!/usr/bin/env python3
"""Exact ordered topology/birth/death chain after the first stable transfer."""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

import front_common as fc


START = fc.HERE / "flip_8245_far.csv"
START_CERTIFICATE = fc.HERE / "flip_8245_certificate.json"
START_VERIFICATION = fc.HERE / "flip_8245_verification.json"
OUTPUT = fc.HERE / "ordered_transfer_locator.json"
FINAL_FAR = fc.HERE / "ordered_transfer_far.csv"
FINAL_T = Q(13, 2_500)  # 0.0052


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


def factor_multiplicity(polynomial, factor):
    multiplicity = 0
    cofactor = polynomial
    while cofactor.degree >= factor.degree:
        quotient, remainder = poly_divmod(cofactor, factor)
        if remainder != fc.ex.P.zero():
            break
        multiplicity += 1
        cofactor = quotient
    return multiplicity, cofactor


def signed_digest(records):
    digest = hashlib.sha256()
    for name, sign, polynomial in records:
        digest.update(name.encode())
        digest.update(b"|")
        digest.update(str(sign).encode())
        digest.update(b"|")
        digest.update("|".join(polynomial.exact()).encode())
        digest.update(b"\n")
    return digest.hexdigest()


def complete_digest(records):
    digest = hashlib.sha256()
    for name, polynomial, family in records:
        digest.update(name.encode())
        digest.update(b"|")
        digest.update(family.encode())
        digest.update(b"|")
        digest.update("|".join(polynomial.exact()).encode())
        digest.update(b"\n")
    return digest.hexdigest()


def event_audit(records, factor, lo, root_hi, cofactor_hi):
    zero_family = []
    strict = []
    family_counts = {}
    leaves = 0
    worst = None
    for name, polynomial, family in records:
        multiplicity, cofactor = factor_multiplicity(polynomial, factor)
        if multiplicity:
            sign, count, margin = fc.ex.bernstein_sign(
                cofactor, lo, cofactor_hi, max_depth=40
            )
            zero_family.append({
                "name": name,
                "family": family,
                "factor_multiplicity": multiplicity,
                "cofactor_degree": cofactor.degree,
                "cofactor_sign": sign,
                "cofactor_bernstein_leaves": count,
                "cofactor_min_log10_abs": margin,
                "cofactor_digest": hashlib.sha256("|".join(cofactor.exact()).encode()).hexdigest(),
            })
            continue
        sign, count, margin = fc.ex.bernstein_sign(
            polynomial, lo, root_hi, max_depth=40
        )
        strict.append((name, sign, polynomial))
        leaves += count
        worst = margin if worst is None else min(worst, margin)
        family_counts[family] = family_counts.get(family, 0) + 1
    return {
        "complete_primitive_count": len(records),
        "zero_family_count": len(zero_family),
        "zero_family": zero_family,
        "strict_nonfamily_count": len(strict),
        "strict_nonfamily_family_counts": family_counts,
        "strict_nonfamily_bernstein_leaves": leaves,
        "strict_nonfamily_min_log10_abs": worst,
        "strict_nonfamily_signed_digest": signed_digest(strict),
    }


def strict_interval(records, lo, hi):
    rows = []
    leaves = 0
    worst = None
    family_counts = {}
    for name, polynomial, family in records:
        sign, count, margin = fc.ex.bernstein_sign(polynomial, lo, hi, max_depth=40)
        rows.append((name, sign, polynomial))
        leaves += count
        worst = margin if worst is None else min(worst, margin)
        family_counts[family] = family_counts.get(family, 0) + 1
    return {
        "strict_primitive_count": len(rows),
        "family_counts": family_counts,
        "bernstein_leaf_count": leaves,
        "min_log10_abs": worst,
        "signed_digest": signed_digest(rows),
    }


def circuit(path, labels):
    a, b, c, d = (path[label] for label in labels)
    return fc.ex.det3(fc.ex.sub(b, a), fc.ex.sub(c, a), fc.ex.sub(d, a))


def root_record(root):
    return {
        "lo": fc.ex.qs(root["lo"]),
        "hi": fc.ex.qs(root["hi"]),
        "midpoint_decimal": float((root["lo"] + root["hi"]) / 2),
        "width_decimal": float(root["hi"] - root["lo"]),
        "value_lo_sign": (root["value_lo"] > 0) - (root["value_lo"] < 0),
        "value_hi_sign": (root["value_hi"] > 0) - (root["value_hi"] < 0),
        "derivative_sign": root["derivative_sign"],
        "derivative_bernstein_leaves": root["derivative_bernstein_leaves"],
    }


def topology_difference(before, after):
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


def base_turn_count(points, faces):
    path = {label: tuple(fc.ex.P((value,)) for value in xyz) for label, xyz in points.items()}
    count = 0
    for face_index, cycle in enumerate(faces):
        if len(cycle) <= 3:
            continue
        normal = fc.ex.cycle_normal(cycle, path)
        for offset, current in enumerate(cycle):
            previous = cycle[offset - 1]
            following = cycle[(offset + 1) % len(cycle)]
            value = fc.ex.dot(
                fc.ex.cross(
                    fc.ex.sub(path[current], path[previous]),
                    fc.ex.sub(path[following], path[current]),
                ),
                normal,
            ).eval(Q(0))
            if not value:
                raise AssertionError(("zero in-face turn", face_index, current))
            count += 1
    return count


def checkpoint(path, parameter, expected_features):
    points = fc.evaluate_path(path, parameter)
    faces, hull = fc.fresh.fresh_maximal_faces(points)
    support = fc.ex.supporting_cell(points, faces)
    ledger, mechanics = fc.ex.classify_point(points, faces)
    if support["f_vector"] != [61, 162, 103] or support["active_labels"] != fc.EXPECTED_ACTIVE:
        raise AssertionError(("checkpoint support", parameter, support))
    if mechanics != expected_features:
        raise AssertionError(("checkpoint mechanics", parameter, mechanics, expected_features))
    missing = sorted(fc.forced_rails() - fc.edge_set(faces))
    if missing:
        raise AssertionError(("checkpoint rails", parameter, missing))
    components = {
        "H910": {
            name: fc.ex.qs(ledger["edge"][(9, 10)][name])
            for name in ("t", "one_minus_t", "beta1", "beta2")
        },
        "H1011": {
            name: fc.ex.qs(ledger["edge"][(10, 11)][name])
            for name in ("t", "one_minus_t", "beta1", "beta2")
        },
        "U10": {
            str(neighbor): fc.ex.qs(value)
            for neighbor, value in sorted(ledger["vertex"][10].items())
        },
    }
    return {
        "t": fc.ex.qs(parameter),
        "coordinate_hash": fc.canonical_hash({
            str(label): [fc.ex.qs(value) for value in points[label]]
            for label in sorted(points)
        }),
        "face_hash": fc.fresh.face_hash(faces),
        "fresh_hull": hull,
        "support": {key: value for key, value in support.items() if key != "edges"},
        "mechanics": mechanics,
        "forced_rail_count": 37,
        "missing_forced_rails": [],
        "base_turn_count": base_turn_count(points, faces),
        "row230_squared_margins": fc.row230_values(points, faces),
        "transfer_components": components,
    }, faces


def main() -> None:
    diagnosis = fc.validate_lineage()
    start_certificate = json.loads(START_CERTIFICATE.read_text())
    start_verification = json.loads(START_VERIFICATION.read_text())
    if start_certificate.get("verdict") != "EXACT_STABLE_CARRIER_8245_TRANSFER_CERTIFICATE_PASS":
        raise AssertionError("start certificate verdict")
    if start_verification.get("verdict") != "INDEPENDENT_EXACT_STABLE_CARRIER_8245_TRANSFER_VERIFICATION_PASS":
        raise AssertionError("start verification verdict")
    if fc.sha256(START) != "28323523620c0e8e0daf2d88c2647d6fcd3b2969267579e8e9a1c5eaf668ef20":
        raise AssertionError("start FAR hash")

    source = fc.ex.read_rows(fc.SOURCE)
    velocity = fc.selected_velocity(source, diagnosis)
    path = fc.affine_path(source, velocity)
    if fc.evaluate_path(path, fc.FAR_T) != fc.ex.read_rows(START):
        raise AssertionError("ordered chain does not start at certified FAR")

    feature_222_h1011 = fc.POST_FEATURES
    feature_233 = {
        "class": [2, 3, 3],
        "stable_faces": [sorted(fc.BASE), [7, 8, 246]],
        "unstable_vertices": [1, 8, 10],
        "saddle_edges": [[5, 6], [9, 10], [10, 11]],
    }
    feature_222_h910 = {
        "class": [2, 2, 2],
        "stable_faces": [sorted(fc.BASE), [7, 8, 246]],
        "unstable_vertices": [1, 8],
        "saddle_edges": [[5, 6], [9, 10]],
    }

    ledger_samples = {
        "L1": Q(13, 5_000),
        "L2": Q(3, 1_000),
        "L3": Q(9, 2_000),
        "L4": Q(11, 2_000),
    }
    ledgers = {}
    records = {}
    for name, parameter in ledger_samples.items():
        points = fc.evaluate_path(path, parameter)
        faces, hull = fc.fresh.fresh_maximal_faces(points)
        ledgers[name] = faces
        records[name] = list(fc.primitive_rows(path, faces))
        if len(records[name]) != 7_922:
            raise AssertionError((name, "primitive count"))

    topology_expectations = {
        "circuit_8263": {
            "faces_removed": [[8, 9, 263], [8, 263, 264]],
            "faces_added": [[8, 9, 264], [9, 263, 264]],
            "edges_removed": [[8, 263]],
            "edges_added": [[9, 264]],
        },
        "circuit_198228": {
            "faces_removed": [[198, 228, 229], [198, 228, 258]],
            "faces_added": [[198, 229, 258], [228, 229, 258]],
            "edges_removed": [[198, 228]],
            "edges_added": [[229, 258]],
        },
        "circuit_198235": {
            "faces_removed": [[198, 234, 235], [198, 235, 236]],
            "faces_added": [[198, 234, 236], [234, 235, 236]],
            "edges_removed": [[198, 235]],
            "edges_added": [[234, 236]],
        },
    }
    if topology_difference(ledgers["L1"], ledgers["L2"]) != topology_expectations["circuit_8263"]:
        raise AssertionError("L1/L2 topology")
    if topology_difference(ledgers["L2"], ledgers["L3"]) != topology_expectations["circuit_198228"]:
        raise AssertionError("L2/L3 topology")
    if topology_difference(ledgers["L3"], ledgers["L4"]) != topology_expectations["circuit_198235"]:
        raise AssertionError("L3/L4 topology")

    ledger3 = fc.ex.mechanics_primitives(path, ledgers["L3"])
    ledger4 = fc.ex.mechanics_primitives(path, ledgers["L4"])
    event_specs = [
        {
            "name": "circuit_8263",
            "ledger": "L1",
            "factor": circuit(path, (8, 9, 263, 264)),
            "bracket": (Q(2_679_917, 10**9), Q(2_679_918, 10**9)),
            "segment_start": fc.FAR_T,
            "cofactor_hi": Q(27, 10_000),
            "pre": Q(53, 20_000),
            "post": Q(27, 10_000),
            "pre_features": feature_222_h1011,
            "post_features": feature_222_h1011,
            "topology": topology_expectations["circuit_8263"],
        },
        {
            "name": "circuit_198228",
            "ledger": "L2",
            "factor": circuit(path, (198, 228, 229, 258)),
            "bracket": (Q(3_905_005, 10**9), Q(3_905_006, 10**9)),
            "segment_start": None,
            "cofactor_hi": Q(391, 100_000),
            "pre": Q(39, 10_000),
            "post": Q(391, 100_000),
            "pre_features": feature_222_h1011,
            "post_features": feature_222_h1011,
            "topology": topology_expectations["circuit_198228"],
        },
        {
            "name": "birth_U10_H910",
            "ledger": "L3",
            "factor": ledger3["edge"][(9, 10)]["one_minus_t"],
            "bracket": (Q(4_885_631, 10**9), Q(4_885_632, 10**9)),
            "segment_start": None,
            "cofactor_hi": Q(2_443, 500_000),
            "pre": Q(977, 200_000),
            "post": Q(2_443, 500_000),
            "pre_features": feature_222_h1011,
            "post_features": feature_233,
            "topology": None,
        },
        {
            "name": "circuit_198235",
            "ledger": "L3",
            "factor": circuit(path, (198, 234, 235, 236)),
            "bracket": (Q(4_958_836, 10**9), Q(4_958_837, 10**9)),
            "segment_start": None,
            "cofactor_hi": Q(4_959, 10**6),
            "pre": Q(2_479, 500_000),
            "post": Q(4_959, 10**6),
            "pre_features": feature_233,
            "post_features": feature_233,
            "topology": topology_expectations["circuit_198235"],
        },
        {
            "name": "death_U10_H1011",
            "ledger": "L4",
            "factor": ledger4["edge"][(10, 11)]["t"],
            "bracket": (Q(4_991_152, 10**9), Q(4_991_153, 10**9)),
            "segment_start": None,
            "cofactor_hi": Q(624, 125_000),
            "pre": Q(4_991, 10**6),
            "post": Q(624, 125_000),
            "pre_features": feature_233,
            "post_features": feature_222_h910,
            "topology": None,
        },
    ]

    events = []
    previous_root_hi = fc.FAR_T
    all_checkpoints = {}
    for spec in event_specs:
        segment_start = spec["segment_start"] or previous_root_hi
        root = fc.ex.isolate_monotone_root(
            spec["factor"], spec["bracket"][0], spec["bracket"][1], Q(1, 10**30)
        )
        before = fc.ex.bernstein_sign(spec["factor"], segment_start, root["lo"], max_depth=40)[0]
        after = fc.ex.bernstein_sign(spec["factor"], root["hi"], spec["cofactor_hi"], max_depth=40)[0]
        if before == after:
            raise AssertionError((spec["name"], "factor sign"))
        audit = event_audit(
            records[spec["ledger"]], spec["factor"], segment_start, root["hi"], spec["cofactor_hi"]
        )
        family_names = {row["name"] for row in audit["zero_family"]}
        if spec["name"].startswith("circuit_"):
            if audit["zero_family_count"] != 5:
                raise AssertionError((spec["name"], "circuit family", family_names))
        elif spec["name"] == "birth_U10_H910":
            expected = {"vertex:10:9", "edge:(9, 10):one_minus_t"}
            if family_names != expected:
                raise AssertionError((spec["name"], family_names))
        else:
            expected = {"vertex:10:11", "edge:(10, 11):t"}
            if family_names != expected:
                raise AssertionError((spec["name"], family_names))
        pre_checkpoint, pre_faces = checkpoint(path, spec["pre"], spec["pre_features"])
        post_checkpoint, post_faces = checkpoint(path, spec["post"], spec["post_features"])
        if spec["topology"] is None:
            if topology_difference(pre_faces, post_faces) != {
                "faces_removed": [], "faces_added": [], "edges_removed": [], "edges_added": []
            }:
                raise AssertionError((spec["name"], "unexpected topology"))
        elif topology_difference(pre_faces, post_faces) != spec["topology"]:
            raise AssertionError((spec["name"], "topology mismatch"))
        all_checkpoints[f"{spec['name']}:pre"] = pre_checkpoint
        all_checkpoints[f"{spec['name']}:post"] = post_checkpoint
        events.append({
            "name": spec["name"],
            "ledger": spec["ledger"],
            "factor_degree": spec["factor"].degree,
            "factor_exact": spec["factor"].exact(),
            "factor_digest": hashlib.sha256("|".join(spec["factor"].exact()).encode()).hexdigest(),
            "segment_start": fc.ex.qs(segment_start),
            "root": root_record(root),
            "factor_sign_before": before,
            "factor_sign_after": after,
            "event_audit": audit,
            "topology_transfer": spec["topology"],
            "pre_checkpoint_key": f"{spec['name']}:pre",
            "post_checkpoint_key": f"{spec['name']}:post",
        })
        previous_root_hi = root["hi"]

    final_audit = strict_interval(records["L4"], previous_root_hi, FINAL_T)
    final_checkpoint, final_faces = checkpoint(path, FINAL_T, feature_222_h910)
    all_checkpoints["final_far"] = final_checkpoint
    final_points = fc.evaluate_path(path, FINAL_T)
    fc.atomic_write(FINAL_FAR, fc.exact_csv_bytes(final_points))

    payload = {
        "schema": "stable_first_topology_front.ordered_transfer_locator",
        "schema_version": 1,
        "report_type": "exact_ordered_topology_birth_death_locator",
        "scope": (
            "Exact continuation from the independently verified flip_8245 FAR through three "
            "ordered circuit flips and the linked U10/H910 birth then U10/H1011 death."
        ),
        "source_hashes": fc.bindings((
            fc.HERE / "front_common.py",
            START,
            START_CERTIFICATE,
            START_VERIFICATION,
            Path(__file__).resolve(),
        )),
        "start": {
            "file": START.name,
            "sha256": fc.sha256(START),
            "global_t": fc.ex.qs(fc.FAR_T),
            "class": [2, 2, 2],
            "stable_face": [7, 8, 246],
            "saddles": [[5, 6], [10, 11]],
        },
        "ledger_face_hashes": {
            name: fc.fresh.face_hash(faces) for name, faces in ledgers.items()
        },
        "ledger_complete_primitive_digests": {
            name: complete_digest(rows) for name, rows in records.items()
        },
        "events": events,
        "checkpoints": all_checkpoints,
        "final_open_interval_audit": final_audit,
        "final_far": {
            "file": FINAL_FAR.name,
            "sha256": fc.sha256(FINAL_FAR),
            "global_t": fc.ex.qs(FINAL_T),
            "checkpoint": final_checkpoint,
        },
        "ordered_transfer": {
            "extra_birth": {"unstable": 10, "saddle": [9, 10]},
            "subsequent_death": {"unstable": 10, "saddle": [10, 11]},
            "saddle_before": [10, 11],
            "saddle_after": [9, 10],
            "class_sequence": [[2, 2, 2], [2, 3, 3], [2, 2, 2]],
            "stable_face_preserved": [7, 8, 246],
        },
        "conclusion": (
            "The stable-first ray forces three topology recharts and an explicit ordered "
            "U10-mediated transfer of the second saddle from (10,11) to (9,10); no bounded "
            "sample is promoted to an impossibility statement."
        ),
        "verdict": "EXACT_ORDERED_U10_SADDLE_TRANSFER_LOCATOR_PASS",
    }
    fc.atomic_write(OUTPUT, (json.dumps(payload, indent=2) + "\n").encode())
    print(json.dumps({
        "verdict": payload["verdict"],
        "events": [
            {
                "name": row["name"],
                "root": row["root"]["midpoint_decimal"],
                "zero_family": [item["name"] for item in row["event_audit"]["zero_family"]],
            }
            for row in events
        ],
        "final_far_sha256": fc.sha256(FINAL_FAR),
        "final_class": final_checkpoint["mechanics"]["class"],
        "final_saddles": final_checkpoint["mechanics"]["saddle_edges"],
    }, indent=2))


if __name__ == "__main__":
    main()
