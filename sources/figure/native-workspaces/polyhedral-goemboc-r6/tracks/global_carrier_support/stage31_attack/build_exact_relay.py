#!/usr/bin/env python3
"""Build the exact directed certificate for the Stage-31 carrier relay."""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
TRACK = HERE.parent
ROOT = HERE.parents[2]
EXACT_DIR = TRACK / "rigorous_local_bypass"
sys.path.insert(0, str(EXACT_DIR))
import exact_core as ex  # noqa: E402


SOURCE = TRACK / "stage31_exact_checkpoint.csv"
SOURCE_FACES = TRACK / "stage31_exact_checkpoint_faces.json"
PATH_DEFINITION = HERE / "path_definition.json"
CERTIFICATE = HERE / "exact_relay_certificate.json"
SOURCE_OUT = HERE / "exact_relay_source.csv"
PRE_OUT = HERE / "exact_relay_pre.csv"
MIDDLE_OUT = HERE / "exact_relay_middle.csv"
FAR_OUT = HERE / "exact_relay_far.csv"
FACES_OUT = HERE / "exact_relay_faces.json"

BASE = frozenset(range(17)) | {54}
PRIMARY = (7, 8, 245)
OLD_QUAD = (7, 8, 245, 246)
EXPECTED_F_VECTOR = [61, 162, 103]
EXPECTED_ACTIVE = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    54, 69, 72, 73, 88, 198, 224, 228, 229, 230, 231, 232, 233,
    234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245,
    246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
    258, 259, 260, 261, 262, 263, 264,
]
ROOT_WIDTH = Q(1, 10**24)

PRE_PROTECTED = {
    "stable": [sorted(BASE), list(PRIMARY)],
    "unstable": [8, 54],
    "saddles": [[5, 6], [9, 10]],
}
MIDDLE_PROTECTED = {
    "stable": [sorted(BASE), list(PRIMARY)],
    "unstable": [8, 10, 54],
    "saddles": [[5, 6], [9, 10], [10, 11]],
}
FAR_PROTECTED = {
    "stable": [sorted(BASE), list(PRIMARY)],
    "unstable": [8, 54],
    "saddles": [[5, 6], [10, 11]],
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def write_exact_csv(path: Path, rows) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(("source_id", "x", "y", "z"))
        for label in sorted(rows):
            writer.writerow([label, *[ex.qs(value) for value in rows[label]]])


def load_path():
    definition = json.loads(PATH_DEFINITION.read_text())
    source = ex.read_rows(SOURCE)
    velocity = {
        int(label): tuple(Q(value) for value in xyz)
        for label, xyz in definition["velocity"].items()
    }
    if set(source) != set(velocity):
        raise AssertionError("path labels differ from exact checkpoint")
    path = {
        label: tuple(
            ex.P((source[label][axis], velocity[label][axis]))
            for axis in range(3)
        )
        for label in source
    }
    faces = json.loads(SOURCE_FACES.read_text())
    end = Q(definition["end_parameter"])
    return definition, source, velocity, path, faces, end


def evaluate_path(path, parameter: Q):
    return {
        label: tuple(coordinate.eval(parameter) for coordinate in xyz)
        for label, xyz in path.items()
    }


def restrict_path(path, lo: Q, hi: Q):
    return {
        label: tuple(coordinate.affine(lo, hi) for coordinate in xyz)
        for label, xyz in path.items()
    }


def forced_rails():
    short = [228] + list(range(229, 247)) + [8]
    long = [228] + list(range(247, 265)) + [8]
    rails = {
        tuple(sorted(edge))
        for route in (short, long)
        for edge in zip(route, route[1:])
    }
    rails.remove((228, 229))
    return rails


def proportional_factor(candidate: ex.P, reference: ex.P):
    candidate = ex.P.coerce(candidate)
    reference = ex.P.coerce(reference)
    pivot = next((index for index, value in enumerate(reference.c) if value), None)
    if pivot is None:
        raise AssertionError("zero reference polynomial")
    factor = (
        candidate.c[pivot] / reference.c[pivot]
        if pivot < len(candidate.c)
        else Q(0)
    )
    return factor if candidate == factor * reference else None


def primitive_rows(path, faces):
    ledger = ex.mechanics_primitives(path, faces)
    yield "volume_d6", ledger["d6"]
    for face_key, rows in sorted(ledger["reference"].items()):
        for edge, value in sorted(rows.items()):
            yield f"face_reference:{face_key}:{edge}", value
    for face_key, rows in sorted(ledger["face"].items()):
        for edge, value in sorted(rows.items()):
            yield f"face_raw:{face_key}:{edge}", value
    for vertex, rows in sorted(ledger["vertex"].items()):
        for neighbor, value in sorted(rows.items()):
            yield f"vertex:{vertex}:{neighbor}", value
    for edge, rows in sorted(ledger["edge"].items()):
        for component in (
            "direction_norm2", "gram", "t", "one_minus_t", "beta1", "beta2"
        ):
            yield f"edge:{edge}:{component}", rows[component]


def event_audit(path, faces, event_poly, lo: Q, hi: Q, expected_family):
    strict = []
    family = []
    midpoint = (lo + hi) / 2
    for name, polynomial in primitive_rows(path, faces):
        factor = proportional_factor(polynomial, event_poly)
        if factor is not None:
            family.append({"name": name, "factor": ex.qs(factor)})
            continue
        expected = 1 if polynomial.eval(midpoint) > 0 else -1
        sign, leaves, worst = ex.bernstein_sign(
            polynomial, lo, hi, max_depth=60
        )
        if sign != expected:
            raise AssertionError(("event primitive sign", name, sign, expected))
        strict.append((name, sign, leaves, worst, polynomial))
    family_names = sorted(row["name"] for row in family)
    if family_names != sorted(expected_family):
        raise AssertionError(("unexpected event family", family_names, expected_family))
    digest = hashlib.sha256()
    for name, sign, _leaves, _worst, polynomial in strict:
        digest.update(
            f"{name}|{sign}|{'|'.join(polynomial.exact())}\n".encode()
        )
    return {
        "event_family": family,
        "strict_non_event_primitive_count": len(strict),
        "strict_non_event_bernstein_leaves": sum(row[2] for row in strict),
        "strict_non_event_min_bernstein_log10_abs": min(row[3] for row in strict),
        "strict_non_event_digest": digest.hexdigest(),
    }


def support_continuum(path, faces, end):
    records = []
    for face_index, witness, polynomial in ex.support_polynomials(path, faces):
        value0 = polynomial.eval(Q(0))
        expected = 1 if value0 > 0 else -1
        sign, leaves, worst = ex.bernstein_sign(
            polynomial, Q(0), end, max_depth=60
        )
        if sign != expected:
            raise AssertionError(("support changes", face_index, witness))
        records.append((face_index, witness, sign, leaves, worst, polynomial))
    digest = hashlib.sha256()
    for face_index, witness, sign, _leaves, _worst, polynomial in records:
        digest.update(
            f"{face_index}|{witness}|{sign}|{'|'.join(polynomial.exact())}\n".encode()
        )
    return {
        "strict_support_polynomial_count": len(records),
        "bernstein_leaf_count": sum(row[3] for row in records),
        "minimum_bernstein_log10_abs": min(row[4] for row in records),
        "support_digest": digest.hexdigest(),
    }


def exact_checkpoint(points, faces, expected_class):
    support = ex.supporting_cell(points, faces)
    ledger, mechanics = ex.classify_point(points, faces)
    if support["f_vector"] != EXPECTED_F_VECTOR:
        raise AssertionError(support)
    if support["active_labels"] != EXPECTED_ACTIVE:
        raise AssertionError(("active labels", support["active_labels"]))
    if mechanics["class"] != expected_class:
        raise AssertionError(mechanics)
    if BASE not in {frozenset(face) for face in faces}:
        raise AssertionError("base face absent")
    if not forced_rails().issubset(set(support["edges"])):
        raise AssertionError("forced rail absent")
    d6, m24 = ex.exact_centroid_numerators(points, faces)
    centroid = tuple(value / (4 * d6) for value in m24)
    raw_rows = []
    for name, value in primitive_rows(points, faces):
        if not value:
            raise AssertionError(("zero checkpoint primitive", name))
        raw_rows.append((name, value))
    digest = hashlib.sha256()
    for name, value in raw_rows:
        digest.update(f"{name}|{ex.qs(value)}\n".encode())
    return {
        "coordinate_hash": canonical_hash(
            {str(label): [ex.qs(x) for x in points[label]] for label in sorted(points)}
        ),
        "exact_centroid": [ex.qs(value) for value in centroid],
        "exact_support": {key: value for key, value in support.items() if key != "edges"},
        "exact_mechanics": mechanics,
        "mechanics_primitive_count": len(raw_rows),
        "mechanics_minimum_log10_abs": min(ex.qlog10(value) for _, value in raw_rows),
        "mechanics_digest": digest.hexdigest(),
        "base_face_present": True,
        "forced_rail_count": len(forced_rails()),
        "missing_forced_rails": [],
    }


def exact_root_record(polynomial, lo, hi):
    root = ex.isolate_monotone_root(polynomial, lo, hi, ROOT_WIDTH)
    return {
        "lo": ex.qs(root["lo"]),
        "hi": ex.qs(root["hi"]),
        "value_lo": ex.qs(root["value_lo"]),
        "value_hi": ex.qs(root["value_hi"]),
        "decimal_interval": [float(root["lo"]), float(root["hi"])],
        "derivative_sign": root["derivative_sign"],
        "derivative_bernstein_leaves": root["derivative_bernstein_leaves"],
        "polynomial_degree": polynomial.degree,
        "polynomial_exact": polynomial.exact(),
        "polynomial_digest": canonical_hash(polynomial.exact()),
    }


def main():
    definition, source, velocity, path, faces, end = load_path()
    if definition["verdict"] != "DIRECTED_STAGE31_H910_TO_H1011_RELAY_PROPOSAL_PASS":
        raise AssertionError(definition["verdict"])
    if len(faces) != 103:
        raise AssertionError(len(faces))

    path_ledger = ex.mechanics_primitives(path, faces)
    event_r = path_ledger["vertex"][10][11]
    event_l = path_ledger["vertex"][10][9]
    if event_r != path_ledger["edge"][(10, 11)]["t"]:
        raise AssertionError("N10R/H1011 exact identity failed")
    if event_l != path_ledger["edge"][(9, 10)]["one_minus_t"]:
        raise AssertionError("N10L/H910 exact identity failed")

    root_r = exact_root_record(event_r, Q(808, 100000), Q(810, 100000))
    root_l = exact_root_record(event_l, Q(810, 100000), Q(812, 100000))
    r_lo, r_hi = Q(root_r["lo"]), Q(root_r["hi"])
    l_lo, l_hi = Q(root_l["lo"]), Q(root_l["hi"])
    if not Q(0) < r_lo <= r_hi < l_lo <= l_hi < end:
        raise AssertionError((root_r, root_l, end))

    support_proof = support_continuum(path, faces, end)
    pre_segment = ex.certify_path_segment(
        restrict_path(path, Q(0), r_lo), faces, PRE_PROTECTED
    )
    middle_segment = ex.certify_path_segment(
        restrict_path(path, r_hi, l_lo), faces, MIDDLE_PROTECTED
    )
    far_segment = ex.certify_path_segment(
        restrict_path(path, l_hi, end), faces, FAR_PROTECTED
    )
    event_r_audit = event_audit(
        path,
        faces,
        event_r,
        r_lo,
        r_hi,
        ("vertex:10:11", "edge:(10, 11):t"),
    )
    event_l_audit = event_audit(
        path,
        faces,
        event_l,
        l_lo,
        l_hi,
        ("vertex:10:9", "edge:(9, 10):one_minus_t"),
    )

    pre_parameter = Q(definition["rational_samples"]["pre"])
    middle_parameter = Q(definition["rational_samples"]["middle"])
    if not pre_parameter < r_lo < r_hi < middle_parameter < l_lo:
        raise AssertionError((pre_parameter, root_r, middle_parameter, root_l))

    source_points = evaluate_path(path, Q(0))
    pre_points = evaluate_path(path, pre_parameter)
    middle_points = evaluate_path(path, middle_parameter)
    far_points = evaluate_path(path, end)
    checkpoints = {
        "source": exact_checkpoint(source_points, faces, [2, 2, 2]),
        "pre": exact_checkpoint(pre_points, faces, [2, 2, 2]),
        "middle": exact_checkpoint(middle_points, faces, [2, 3, 3]),
        "far": exact_checkpoint(far_points, faces, [2, 2, 2]),
    }

    write_exact_csv(SOURCE_OUT, source_points)
    write_exact_csv(PRE_OUT, pre_points)
    write_exact_csv(MIDDLE_OUT, middle_points)
    write_exact_csv(FAR_OUT, far_points)
    FACES_OUT.write_text(json.dumps(faces, indent=2) + "\n")
    generated = (SOURCE_OUT, PRE_OUT, MIDDLE_OUT, FAR_OUT, FACES_OUT)

    certificate = {
        "version": 1,
        "type": "exact rational affine own-centroid mechanics relay",
        "scope": (
            "Exact for the literal Stage-31 affine path, all 5,959 support "
            "polynomials, all open-cell mechanics witnesses, both exhaustive "
            "root-bracket primitive ledgers, and the rational far checkpoint. "
            "This is a strict nonwinner, not a Goemboc."
        ),
        "source_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (SOURCE, SOURCE_FACES, PATH_DEFINITION)
        },
        "path": {
            "end_parameter": ex.qs(end),
            "velocity_digest": canonical_hash(
                {str(label): [ex.qs(x) for x in velocity[label]] for label in sorted(velocity)}
            ),
            "support_continuum": support_proof,
        },
        "events": [
            {
                "name": "N10R simultaneous U10/H(10,11) birth",
                "root": root_r,
                "exact_identity": "vertex:10:11 == edge:(10,11):t",
                "audit": event_r_audit,
            },
            {
                "name": "N10L simultaneous U10/H(9,10) death",
                "root": root_l,
                "exact_identity": "vertex:10:9 == edge:(9,10):one_minus_t",
                "audit": event_l_audit,
            },
        ],
        "exact_root_order": {
            "N10R_birth_before_N10L_death": True,
            "strict_rational_gap_lower_bound": ex.qs(l_lo - r_hi),
            "decimal_gap_lower_bound": float(l_lo - r_hi),
            "class_sequence": [[2, 2, 2], [2, 3, 3], [2, 2, 2]],
            "carrier_sequence": ["H(9,10)", "H(9,10)+H(10,11)+U10", "H(10,11)"],
        },
        "open_segments": {
            "pre": pre_segment,
            "middle": middle_segment,
            "far": far_segment,
        },
        "rational_checkpoints": checkpoints,
        "generated_file_sha256": {
            str(path.relative_to(ROOT)): sha256(path) for path in generated
        },
        "residual_verdict": {
            "winner": False,
            "far_class": [2, 2, 2],
            "remaining_extra_stable": list(PRIMARY),
            "remaining_extra_unstable": 54,
            "remaining_saddles": [[5, 6], [10, 11]],
            "interpretation": (
                "The first directed event is a strict H910-to-H1011 carrier "
                "transfer through a narrow (2,3,3) cell, not a saddle death."
            ),
        },
        "verdict": "EXACT_STAGE31_H910_TO_H1011_CARRIER_RELAY_PASS",
    }
    CERTIFICATE.write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps({
        "verdict": certificate["verdict"],
        "support_polynomials": support_proof["strict_support_polynomial_count"],
        "root_intervals": [root_r["decimal_interval"], root_l["decimal_interval"]],
        "gap_lower_bound": certificate["exact_root_order"]["decimal_gap_lower_bound"],
        "classes": certificate["exact_root_order"]["class_sequence"],
        "far_class": checkpoints["far"]["exact_mechanics"]["class"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
