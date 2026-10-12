#!/usr/bin/env python3
"""Independent reconstruction of an exact row-230-safe fixed-cell segment."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
ATTACK = HERE.parent
TRACK = ATTACK.parent
ROOT = HERE.parents[4]

sys.path.insert(0, str(TRACK / "rigorous_local_bypass"))
import exact_core as ex  # noqa: E402
sys.path.insert(0, str(ATTACK))
import build_exact_circuit_flip as residual_core  # noqa: E402


BASE = frozenset(range(17)) | {54}
PROTECTED = {
    "stable": [sorted(BASE), [7, 8, 245]],
    "unstable": [8, 54],
    "saddles": [[5, 6], [10, 11]],
}
TARGETS = ("S", "U54", "H56", "H1011")
DANGER = {
    (frozenset((198, 230, 231)), 229),
    (frozenset((198, 229, 230)), 231),
}
EXPECTED_ACTIVE = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    54, 69, 72, 73, 88, 198, 224, 228, 229, 230, 231, 232, 233, 234,
    235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247,
    248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260,
    261, 262, 263, 264,
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def resolve(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else HERE / path


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


def build_path(source, endpoint):
    assert set(source) == set(endpoint)
    return {
        label: tuple(
            ex.P((source[label][axis], endpoint[label][axis] - source[label][axis]))
            for axis in range(3)
        )
        for label in source
    }


def enumerate_primitives(path, faces):
    ledger = ex.mechanics_primitives(path, faces)
    yield "volume_d6", ledger["d6"], "mechanics_denominator"
    for face_index, witness, polynomial in ex.support_polynomials(path, faces):
        yield f"support:f{face_index}:w{witness}", polynomial, "support"
    for face_key, rows in sorted(ledger["reference"].items()):
        for edge, polynomial in sorted(rows.items()):
            yield f"face_reference:{face_key}:{edge}", polynomial, "mechanics_denominator"
    for face_key, rows in sorted(ledger["face"].items()):
        for edge, polynomial in sorted(rows.items()):
            yield f"face_raw:{face_key}:{edge}", polynomial, "face_component"
    for vertex, rows in sorted(ledger["vertex"].items()):
        for neighbor, polynomial in sorted(rows.items()):
            yield f"vertex:{vertex}:{neighbor}", polynomial, "vertex_component"
    for edge, rows in sorted(ledger["edge"].items()):
        for component in (
            "direction_norm2", "gram", "t", "one_minus_t", "beta1", "beta2"
        ):
            yield f"edge:{edge}:{component}", rows[component], "edge_component"


def interval_receipt(rows):
    digest = hashlib.sha256()
    count = 0
    leaves = 0
    worst = None
    families = {}
    for name, polynomial, family in rows:
        value = polynomial.eval(Q(0))
        assert value != 0
        expected = 1 if value > 0 else -1
        sign, row_leaves, margin = ex.bernstein_sign(
            polynomial, Q(0), Q(1), max_depth=60
        )
        assert sign == expected
        count += 1
        leaves += row_leaves
        worst = margin if worst is None else min(worst, margin)
        families[family] = families.get(family, 0) + 1
        digest.update(
            f"{name}|{family}|{sign}|{'|'.join(polynomial.exact())}\n".encode()
        )
    return {
        "primitive_count": count,
        "family_counts": families,
        "bernstein_leaf_count": leaves,
        "minimum_bernstein_log10_abs": worst,
        "primitive_digest": digest.hexdigest(),
    }


def rails():
    result = set()
    for route in (
        [228] + list(range(229, 247)) + [8],
        [228] + list(range(247, 265)) + [8],
    ):
        result.update(tuple(sorted(edge)) for edge in zip(route, route[1:]))
    result.remove((228, 229))
    assert len(result) == 37
    return result


def point_receipt(points, faces):
    support = ex.supporting_cell(points, faces)
    _raw, mechanics = ex.classify_point(points, faces)
    assert support["f_vector"] == [61, 162, 103]
    assert support["euler"] == 2
    assert support["active_labels"] == EXPECTED_ACTIVE
    assert mechanics["class"] == [2, 2, 2]
    assert BASE in {frozenset(face) for face in faces}
    assert rails().issubset(set(support["edges"]))
    d6, m24 = ex.exact_centroid_numerators(points, faces)
    centroid = tuple(value / (4 * d6) for value in m24)
    return {
        "coordinate_hash": canonical_hash({
            str(label): [ex.qs(value) for value in points[label]]
            for label in sorted(points)
        }),
        "exact_uniform_volume_centroid": [ex.qs(value) for value in centroid],
        "support": {key: value for key, value in support.items() if key != "edges"},
        "mechanics": mechanics,
        "base_face_present": True,
        "forced_rail_count": 37,
        "missing_forced_rails": [],
    }


def residual_receipt(path, faces):
    source = {
        label: tuple(poly.eval(Q(0)) for poly in xyz)
        for label, xyz in path.items()
    }
    endpoint = {
        label: tuple(poly.eval(Q(1)) for poly in xyz)
        for label, xyz in path.items()
    }
    output = {}
    for name in TARGETS:
        before = residual_core.selected_residual_record(source, faces, name)
        after = residual_core.selected_residual_record(endpoint, faces, name)
        before_value = Q(before["squared_value"])
        after_value = Q(after["squared_value"])
        assert after_value < before_value
        numerator, denominator = residual_core.selected_fraction_polynomials(
            path, faces, name
        )
        derivative = (
            numerator.derivative() * denominator
            - numerator * denominator.derivative()
        )
        sign, leaves, worst = ex.bernstein_sign(
            derivative, Q(0), Q(1), max_depth=60
        )
        assert sign == -1
        output[name] = {
            "source": before,
            "endpoint": after,
            "exact_squared_drop": ex.qs(before_value - after_value),
            "derivative_sign": sign,
            "derivative_degree": derivative.degree,
            "derivative_bernstein_leaf_count": leaves,
            "derivative_minimum_bernstein_log10_abs": worst,
            "derivative_digest": canonical_hash(derivative.exact()),
        }
    return output


def dead_h910(path, faces):
    rows = ex.mechanics_primitives(path, faces)["edge"][(9, 10)]
    names = ("t", "one_minus_t", "beta1", "beta2")
    witness = min(names, key=lambda name: rows[name].eval(Q(0)))
    polynomial = rows[witness]
    assert polynomial.eval(Q(0)) < 0
    sign, leaves, worst = ex.bernstein_sign(
        polynomial, Q(0), Q(1), max_depth=60
    )
    assert sign == -1
    return {
        "component": witness,
        "source": ex.qs(polynomial.eval(Q(0))),
        "endpoint": ex.qs(polynomial.eval(Q(1))),
        "sign": sign,
        "bernstein_leaf_count": leaves,
        "minimum_bernstein_log10_abs": worst,
        "polynomial_degree": polynomial.degree,
        "polynomial_digest": canonical_hash(polynomial.exact()),
    }


def row230_receipt(path, faces):
    found = {}
    for face_index, witness, support in ex.support_polynomials(path, faces):
        family = (frozenset(faces[face_index]), witness)
        if family not in DANGER:
            continue
        normal = ex.cycle_normal(faces[face_index], path)
        norm2 = ex.norm2(normal)
        square = support * support
        derivative = square.derivative() * norm2 - square * norm2.derivative()
        sign, leaves, worst = ex.bernstein_sign(
            derivative, Q(0), Q(1), max_depth=60
        )
        assert sign == 1
        before = square.eval(Q(0)) / norm2.eval(Q(0))
        after = square.eval(Q(1)) / norm2.eval(Q(1))
        assert after > before
        found[f"{sorted(family[0])}|{witness}"] = {
            "source_squared_normalized_margin": ex.qs(before),
            "endpoint_squared_normalized_margin": ex.qs(after),
            "strict_increase": ex.qs(after - before),
            "derivative_sign": sign,
            "derivative_degree": derivative.degree,
            "derivative_bernstein_leaf_count": leaves,
            "derivative_minimum_bernstein_log10_abs": worst,
            "derivative_digest": canonical_hash(derivative.exact()),
            "support_polynomial_digest": canonical_hash(support.exact()),
        }
    assert set(found) == {"[198, 230, 231]|229", "[198, 229, 230]|231"}
    return found


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--endpoint", required=True)
    parser.add_argument("--faces", required=True)
    parser.add_argument("--proposal", required=True)
    parser.add_argument("--scan", required=True)
    parser.add_argument("--certificate", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    source_path = resolve(args.source)
    endpoint_path = resolve(args.endpoint)
    faces_path = resolve(args.faces)
    proposal_path = resolve(args.proposal)
    scan_path = resolve(args.scan)
    certificate_path = resolve(args.certificate)
    output_path = resolve(args.output)
    frozen = json.loads(certificate_path.read_text())
    assert frozen["verdict"] == "EXACT_ROW230_SAFE_FIXED_CELL_STEP_PASS"
    for path in (source_path, endpoint_path, faces_path, proposal_path, scan_path):
        assert sha256(path) == frozen["source_hashes"][relative(path)]

    scan = json.loads(scan_path.read_text())
    assert scan["verdict"] == "EXHAUSTIVE_EXACT_FIRST_EVENT_LOCATOR_PASS"
    assert Q(scan["first_candidate"]["lo"]) > 1
    assert scan["first_candidate"]["lo"] == frozen["path"]["first_future_event_lower_bound"]
    assert scan["first_candidate"]["name"] == frozen["path"]["first_future_event_name"]

    source = ex.read_rows(source_path)
    endpoint = ex.read_rows(endpoint_path)
    faces = json.loads(faces_path.read_text())
    path = build_path(source, endpoint)
    assert canonical_hash({
        str(label): [
            ex.qs(endpoint[label][axis] - source[label][axis])
            for axis in range(3)
        ]
        for label in sorted(source)
    }) == frozen["path"]["endpoint_delta_digest"]

    rows = list(enumerate_primitives(path, faces))
    assert len(rows) == 7904
    assert interval_receipt(rows) == frozen["exhaustive_interval"]
    cover = ex.certify_path_segment(path, faces, PROTECTED)
    assert cover == frozen["class_cover"]
    assert point_receipt(source, faces) == frozen["checkpoints"]["source"]
    assert point_receipt(endpoint, faces) == frozen["checkpoints"]["endpoint"]
    actual_residuals = residual_receipt(path, faces)
    assert actual_residuals == frozen["directed_residuals"]
    assert dead_h910(path, faces) == frozen["h910_nonresurrection"]
    assert row230_receipt(path, faces) == frozen["row230_strict_inward_certificate"]

    receipt = {
        "version": 1,
        "certificate_sha256": sha256(certificate_path),
        "source_sha256": sha256(source_path),
        "endpoint_sha256": sha256(endpoint_path),
        "primitive_count": len(rows),
        "own_centroid_reconstructed": True,
        "active_rows": 61,
        "forced_rails": 37,
        "class": [2, 2, 2],
        "row230_margins_strictly_increasing": True,
        "h910_strictly_negative": True,
        "endpoint_decisions": {
            name: row["endpoint"]["decision_value"]
            for name, row in actual_residuals.items()
        },
        "verdict": "INDEPENDENT_EXACT_ROW230_SAFE_FIXED_CELL_STEP_PASS",
    }
    output_path.write_text(json.dumps(receipt, indent=2) + "\n")
    print(receipt["verdict"])


if __name__ == "__main__":
    main()
