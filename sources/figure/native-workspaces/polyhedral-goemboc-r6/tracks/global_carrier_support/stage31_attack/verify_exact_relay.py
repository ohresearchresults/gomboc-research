#!/usr/bin/env python3
"""Independent reconstruction of the exact Stage-31 carrier relay."""
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
sys.path.insert(0, str(TRACK / "rigorous_local_bypass"))
import exact_core as ex  # noqa: E402


SOURCE = TRACK / "stage31_exact_checkpoint.csv"
SOURCE_FACES = TRACK / "stage31_exact_checkpoint_faces.json"
PATH_DEFINITION = HERE / "path_definition.json"
CERTIFICATE = HERE / "exact_relay_certificate.json"
GENERATED = {
    "source": HERE / "exact_relay_source.csv",
    "pre": HERE / "exact_relay_pre.csv",
    "middle": HERE / "exact_relay_middle.csv",
    "far": HERE / "exact_relay_far.csv",
    "faces": HERE / "exact_relay_faces.json",
}

BASE = frozenset(range(17)) | {54}
PRIMARY = (7, 8, 245)
ROOT_WIDTH = Q(1, 10**24)
EXPECTED_F_VECTOR = [61, 162, 103]
EXPECTED_ACTIVE = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    54, 69, 72, 73, 88, 198, 224, 228, 229, 230, 231, 232, 233,
    234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245,
    246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
    258, 259, 260, 261, 262, 263, 264,
]

PROTECTED = {
    "pre": {
        "stable": [sorted(BASE), list(PRIMARY)],
        "unstable": [8, 54],
        "saddles": [[5, 6], [9, 10]],
    },
    "middle": {
        "stable": [sorted(BASE), list(PRIMARY)],
        "unstable": [8, 10, 54],
        "saddles": [[5, 6], [9, 10], [10, 11]],
    },
    "far": {
        "stable": [sorted(BASE), list(PRIMARY)],
        "unstable": [8, 54],
        "saddles": [[5, 6], [10, 11]],
    },
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def evaluate_path(path, parameter):
    return {
        label: tuple(coordinate.eval(parameter) for coordinate in xyz)
        for label, xyz in path.items()
    }


def restrict_path(path, lo, hi):
    return {
        label: tuple(coordinate.affine(lo, hi) for coordinate in xyz)
        for label, xyz in path.items()
    }


def forced_rails():
    routes = (
        [228] + list(range(229, 247)) + [8],
        [228] + list(range(247, 265)) + [8],
    )
    rails = {
        tuple(sorted(edge))
        for route in routes
        for edge in zip(route, route[1:])
    }
    rails.remove((228, 229))
    return rails


def primitive_rows(points, faces):
    ledger = ex.mechanics_primitives(points, faces)
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


def proportional(candidate, reference):
    candidate, reference = ex.P.coerce(candidate), ex.P.coerce(reference)
    pivot = next(index for index, value in enumerate(reference.c) if value)
    factor = (
        candidate.c[pivot] / reference.c[pivot]
        if pivot < len(candidate.c)
        else Q(0)
    )
    return factor if candidate == factor * reference else None


def recompute_event_audit(path, faces, event, lo, hi, expected_names):
    midpoint = (lo + hi) / 2
    family = []
    strict = []
    for name, polynomial in primitive_rows(path, faces):
        factor = proportional(polynomial, event)
        if factor is not None:
            family.append({"name": name, "factor": ex.qs(factor)})
            continue
        expected = 1 if polynomial.eval(midpoint) > 0 else -1
        sign, leaves, worst = ex.bernstein_sign(
            polynomial, lo, hi, max_depth=60
        )
        assert sign == expected
        strict.append((name, sign, leaves, worst, polynomial))
    assert sorted(row["name"] for row in family) == sorted(expected_names)
    digest = hashlib.sha256()
    for name, sign, _leaves, _worst, polynomial in strict:
        digest.update(f"{name}|{sign}|{'|'.join(polynomial.exact())}\n".encode())
    return {
        "event_family": family,
        "strict_non_event_primitive_count": len(strict),
        "strict_non_event_bernstein_leaves": sum(row[2] for row in strict),
        "strict_non_event_min_bernstein_log10_abs": min(row[3] for row in strict),
        "strict_non_event_digest": digest.hexdigest(),
    }


def recompute_support(path, faces, end):
    rows = []
    for face_index, witness, polynomial in ex.support_polynomials(path, faces):
        expected = 1 if polynomial.eval(Q(0)) > 0 else -1
        sign, leaves, worst = ex.bernstein_sign(
            polynomial, Q(0), end, max_depth=60
        )
        assert sign == expected
        rows.append((face_index, witness, sign, leaves, worst, polynomial))
    digest = hashlib.sha256()
    for face_index, witness, sign, _leaves, _worst, polynomial in rows:
        digest.update(
            f"{face_index}|{witness}|{sign}|{'|'.join(polynomial.exact())}\n".encode()
        )
    return {
        "strict_support_polynomial_count": len(rows),
        "bernstein_leaf_count": sum(row[3] for row in rows),
        "minimum_bernstein_log10_abs": min(row[4] for row in rows),
        "support_digest": digest.hexdigest(),
    }


def recompute_checkpoint(points, faces, expected_class):
    support = ex.supporting_cell(points, faces)
    _ledger, mechanics = ex.classify_point(points, faces)
    assert support["f_vector"] == EXPECTED_F_VECTOR
    assert support["active_labels"] == EXPECTED_ACTIVE
    assert mechanics["class"] == expected_class
    assert BASE in {frozenset(face) for face in faces}
    assert forced_rails().issubset(set(support["edges"]))
    d6, m24 = ex.exact_centroid_numerators(points, faces)
    centroid = tuple(value / (4 * d6) for value in m24)
    rows = list(primitive_rows(points, faces))
    assert all(value for _name, value in rows)
    digest = hashlib.sha256()
    for name, value in rows:
        digest.update(f"{name}|{ex.qs(value)}\n".encode())
    return {
        "coordinate_hash": canonical_hash(
            {str(label): [ex.qs(x) for x in points[label]] for label in sorted(points)}
        ),
        "exact_centroid": [ex.qs(value) for value in centroid],
        "exact_support": {key: value for key, value in support.items() if key != "edges"},
        "exact_mechanics": mechanics,
        "mechanics_primitive_count": len(rows),
        "mechanics_minimum_log10_abs": min(ex.qlog10(value) for _, value in rows),
        "mechanics_digest": digest.hexdigest(),
        "base_face_present": True,
        "forced_rail_count": len(forced_rails()),
        "missing_forced_rails": [],
    }


def assert_csv(path, expected):
    assert ex.read_rows(path) == expected


def main():
    frozen = json.loads(CERTIFICATE.read_text())
    assert frozen["verdict"] == "EXACT_STAGE31_H910_TO_H1011_CARRIER_RELAY_PASS"
    definition = json.loads(PATH_DEFINITION.read_text())
    source = ex.read_rows(SOURCE)
    faces = json.loads(SOURCE_FACES.read_text())
    velocity = {
        int(label): tuple(Q(value) for value in xyz)
        for label, xyz in definition["velocity"].items()
    }
    path = {
        label: tuple(
            ex.P((source[label][axis], velocity[label][axis]))
            for axis in range(3)
        )
        for label in source
    }
    end = Q(definition["end_parameter"])

    for path_source in (SOURCE, SOURCE_FACES, PATH_DEFINITION):
        key = str(path_source.relative_to(ROOT))
        assert sha256(path_source) == frozen["source_hashes"][key]
    assert canonical_hash(
        {str(label): [ex.qs(x) for x in velocity[label]] for label in sorted(velocity)}
    ) == frozen["path"]["velocity_digest"]

    ledger = ex.mechanics_primitives(path, faces)
    event_r = ledger["vertex"][10][11]
    event_l = ledger["vertex"][10][9]
    assert event_r == ledger["edge"][(10, 11)]["t"]
    assert event_l == ledger["edge"][(9, 10)]["one_minus_t"]

    root_r = ex.isolate_monotone_root(
        event_r, Q(808, 100000), Q(810, 100000), ROOT_WIDTH
    )
    root_l = ex.isolate_monotone_root(
        event_l, Q(810, 100000), Q(812, 100000), ROOT_WIDTH
    )
    r_lo, r_hi = root_r["lo"], root_r["hi"]
    l_lo, l_hi = root_l["lo"], root_l["hi"]
    assert Q(0) < r_lo <= r_hi < l_lo <= l_hi < end
    assert ex.qs(l_lo - r_hi) == frozen["exact_root_order"][
        "strict_rational_gap_lower_bound"
    ]
    for event, root in zip((event_r, event_l), (root_r, root_l)):
        stored = frozen["events"][0 if event is event_r else 1]["root"]
        assert event.exact() == stored["polynomial_exact"]
        assert ex.qs(root["lo"]) == stored["lo"]
        assert ex.qs(root["hi"]) == stored["hi"]
        assert ex.qs(root["value_lo"]) == stored["value_lo"]
        assert ex.qs(root["value_hi"]) == stored["value_hi"]
        assert root["derivative_sign"] == stored["derivative_sign"]

    assert recompute_support(path, faces, end) == frozen["path"]["support_continuum"]
    intervals = {
        "pre": (Q(0), r_lo),
        "middle": (r_hi, l_lo),
        "far": (l_hi, end),
    }
    for name, (lo, hi) in intervals.items():
        actual = ex.certify_path_segment(
            restrict_path(path, lo, hi), faces, PROTECTED[name]
        )
        assert actual == frozen["open_segments"][name]

    assert recompute_event_audit(
        path,
        faces,
        event_r,
        r_lo,
        r_hi,
        ("vertex:10:11", "edge:(10, 11):t"),
    ) == frozen["events"][0]["audit"]
    assert recompute_event_audit(
        path,
        faces,
        event_l,
        l_lo,
        l_hi,
        ("vertex:10:9", "edge:(9, 10):one_minus_t"),
    ) == frozen["events"][1]["audit"]

    parameters = {
        "source": Q(0),
        "pre": Q(definition["rational_samples"]["pre"]),
        "middle": Q(definition["rational_samples"]["middle"]),
        "far": end,
    }
    classes = {
        "source": [2, 2, 2],
        "pre": [2, 2, 2],
        "middle": [2, 3, 3],
        "far": [2, 2, 2],
    }
    for name, parameter in parameters.items():
        points = evaluate_path(path, parameter)
        assert recompute_checkpoint(points, faces, classes[name]) == frozen[
            "rational_checkpoints"
        ][name]
        assert_csv(GENERATED[name], points)
    assert json.loads(GENERATED["faces"].read_text()) == faces

    for generated in GENERATED.values():
        key = str(generated.relative_to(ROOT))
        assert sha256(generated) == frozen["generated_file_sha256"][key]

    assert frozen["residual_verdict"] == {
        "winner": False,
        "far_class": [2, 2, 2],
        "remaining_extra_stable": [7, 8, 245],
        "remaining_extra_unstable": 54,
        "remaining_saddles": [[5, 6], [10, 11]],
        "interpretation": (
            "The first directed event is a strict H910-to-H1011 carrier "
            "transfer through a narrow (2,3,3) cell, not a saddle death."
        ),
    }
    print("INDEPENDENT_EXACT_STAGE31_H910_TO_H1011_CARRIER_RELAY_PASS")


if __name__ == "__main__":
    main()
