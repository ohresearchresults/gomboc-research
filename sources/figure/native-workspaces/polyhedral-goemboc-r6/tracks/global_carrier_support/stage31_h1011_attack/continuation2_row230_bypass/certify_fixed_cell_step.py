#!/usr/bin/env python3
"""Fail-closed exact certificate for one row-230-safe fixed-cell segment."""
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
PRIMARY = (7, 8, 245)
PROTECTED = {
    "stable": [sorted(BASE), list(PRIMARY)],
    "unstable": [8, 54],
    "saddles": [[5, 6], [10, 11]],
}
DANGER = {
    (frozenset((198, 230, 231)), 229),
    (frozenset((198, 229, 230)), 231),
}
TARGETS = ("S", "U54", "H56", "H1011")
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


def affine_path(source, endpoint):
    if set(source) != set(endpoint):
        raise AssertionError("source and endpoint labels differ")
    return {
        label: tuple(
            ex.P((source[label][axis], endpoint[label][axis] - source[label][axis]))
            for axis in range(3)
        )
        for label in source
    }


def primitive_rows(path, faces):
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


def exhaustive_interval(rows):
    digest = hashlib.sha256()
    count = 0
    leaves = 0
    worst = None
    family_counts = {}
    for name, polynomial, family in rows:
        source_sign = 1 if polynomial.eval(Q(0)) > 0 else -1
        if polynomial.eval(Q(0)) == 0:
            raise AssertionError(("zero primitive at source", name))
        sign, row_leaves, margin = ex.bernstein_sign(
            polynomial, Q(0), Q(1), max_depth=60
        )
        if sign != source_sign:
            raise AssertionError(("primitive sign changed", name, source_sign, sign))
        count += 1
        leaves += row_leaves
        worst = margin if worst is None else min(worst, margin)
        family_counts[family] = family_counts.get(family, 0) + 1
        digest.update(
            f"{name}|{family}|{sign}|{'|'.join(polynomial.exact())}\n".encode()
        )
    return {
        "primitive_count": count,
        "family_counts": family_counts,
        "bernstein_leaf_count": leaves,
        "minimum_bernstein_log10_abs": worst,
        "primitive_digest": digest.hexdigest(),
    }


def forced_rails():
    result = set()
    for route in (
        [228] + list(range(229, 247)) + [8],
        [228] + list(range(247, 265)) + [8],
    ):
        result.update(tuple(sorted(pair)) for pair in zip(route, route[1:]))
    result.remove((228, 229))
    if len(result) != 37:
        raise AssertionError(len(result))
    return result


def checkpoint(points, faces):
    support = ex.supporting_cell(points, faces)
    _ledger, mechanics = ex.classify_point(points, faces)
    if support["f_vector"] != [61, 162, 103]:
        raise AssertionError(support)
    if support["active_labels"] != EXPECTED_ACTIVE:
        raise AssertionError(("active labels", support["active_labels"]))
    if mechanics["class"] != [2, 2, 2]:
        raise AssertionError(mechanics)
    if BASE not in {frozenset(face) for face in faces}:
        raise AssertionError("enlarged base absent")
    missing = sorted(forced_rails() - set(support["edges"]))
    if missing:
        raise AssertionError(("forced rails absent", missing))
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


def residual_audit(path, faces):
    source = {
        label: tuple(coordinate.eval(Q(0)) for coordinate in xyz)
        for label, xyz in path.items()
    }
    endpoint = {
        label: tuple(coordinate.eval(Q(1)) for coordinate in xyz)
        for label, xyz in path.items()
    }
    output = {}
    for name in TARGETS:
        before = residual_core.selected_residual_record(source, faces, name)
        after = residual_core.selected_residual_record(endpoint, faces, name)
        before_value = Q(before["squared_value"])
        after_value = Q(after["squared_value"])
        if not after_value < before_value:
            raise AssertionError((name, "endpoint did not improve"))
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
        if sign != -1:
            raise AssertionError((name, "not strictly decreasing", sign))
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


def h910_audit(path, faces):
    rows = ex.mechanics_primitives(path, faces)["edge"][(9, 10)]
    components = ("t", "one_minus_t", "beta1", "beta2")
    witness = min(components, key=lambda name: rows[name].eval(Q(0)))
    polynomial = rows[witness]
    if polynomial.eval(Q(0)) >= 0:
        raise AssertionError("H910 is not dead at source")
    sign, leaves, worst = ex.bernstein_sign(
        polynomial, Q(0), Q(1), max_depth=60
    )
    if sign != -1:
        raise AssertionError("H910 resurrects on segment")
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


def danger_audit(path, faces):
    output = {}
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
        if sign != 1:
            raise AssertionError((family, "row-230 margin is not strictly increasing"))
        source_value = square.eval(Q(0)) / norm2.eval(Q(0))
        endpoint_value = square.eval(Q(1)) / norm2.eval(Q(1))
        if not endpoint_value > source_value:
            raise AssertionError((family, source_value, endpoint_value))
        key = f"{sorted(family[0])}|{witness}"
        output[key] = {
            "source_squared_normalized_margin": ex.qs(source_value),
            "endpoint_squared_normalized_margin": ex.qs(endpoint_value),
            "strict_increase": ex.qs(endpoint_value - source_value),
            "derivative_sign": sign,
            "derivative_degree": derivative.degree,
            "derivative_bernstein_leaf_count": leaves,
            "derivative_minimum_bernstein_log10_abs": worst,
            "derivative_digest": canonical_hash(derivative.exact()),
            "support_polynomial_digest": canonical_hash(support.exact()),
        }
    if set(output) != {
        "[198, 230, 231]|229", "[198, 229, 230]|231"
    }:
        raise AssertionError(("incomplete row-230 family", sorted(output)))
    return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--endpoint", required=True)
    parser.add_argument("--faces", required=True)
    parser.add_argument("--proposal", required=True)
    parser.add_argument("--scan", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument(
        "--proposal-verdict",
        default="POST_SAFE_FLIP_FULL_CONTROL_RATIONAL_DESCENT_PROPOSAL_PASS",
    )
    args = parser.parse_args()

    source_path = resolve(args.source)
    endpoint_path = resolve(args.endpoint)
    faces_path = resolve(args.faces)
    proposal_path = resolve(args.proposal)
    scan_path = resolve(args.scan)
    output_path = resolve(args.output)
    proposal = json.loads(proposal_path.read_text())
    scan = json.loads(scan_path.read_text())
    if proposal["verdict"] != args.proposal_verdict:
        raise AssertionError(proposal["verdict"])
    if scan["verdict"] != "EXHAUSTIVE_EXACT_FIRST_EVENT_LOCATOR_PASS":
        raise AssertionError(scan["verdict"])
    if Q(scan["first_candidate"]["lo"]) <= 1:
        raise AssertionError("an exact primitive event lies inside the accepted segment")

    source = ex.read_rows(source_path)
    endpoint = ex.read_rows(endpoint_path)
    faces = json.loads(faces_path.read_text())
    path = affine_path(source, endpoint)
    rows = list(primitive_rows(path, faces))
    exhaustive = exhaustive_interval(rows)
    if exhaustive["primitive_count"] != 7904:
        raise AssertionError(exhaustive)
    class_cover = ex.certify_path_segment(path, faces, PROTECTED)
    if class_cover["start_class"]["class"] != [2, 2, 2]:
        raise AssertionError(class_cover)

    certificate = {
        "version": 1,
        "type": "exact row-230-safe fixed-cell rational segment",
        "scope": (
            "All 7,904 support and own-centroid four-cone primitives on t in [0,1]; "
            "61 active rows, enlarged base, U8, 37 rails and H910<0; both row-230 "
            "loss margins strictly increase while S/U54/H56/H1011 strictly decrease."
        ),
        "source_hashes": {
            relative(file): sha256(file)
            for file in (source_path, endpoint_path, faces_path, proposal_path, scan_path)
        },
        "path": {
            "accepted_interval": ["0", "1"],
            "endpoint_delta_digest": canonical_hash({
                str(label): [
                    ex.qs(endpoint[label][axis] - source[label][axis])
                    for axis in range(3)
                ]
                for label in sorted(source)
            }),
            "first_future_event_lower_bound": scan["first_candidate"]["lo"],
            "first_future_event_name": scan["first_candidate"]["name"],
        },
        "exhaustive_interval": exhaustive,
        "class_cover": class_cover,
        "checkpoints": {
            "source": checkpoint(source, faces),
            "endpoint": checkpoint(endpoint, faces),
        },
        "directed_residuals": residual_audit(path, faces),
        "h910_nonresurrection": h910_audit(path, faces),
        "row230_strict_inward_certificate": danger_audit(path, faces),
        "residual_verdict": {
            "winner": False,
            "endpoint_class": [2, 2, 2],
            "next_action": "rechart from this exact endpoint before its first genuine event",
        },
        "verdict": "EXACT_ROW230_SAFE_FIXED_CELL_STEP_PASS",
    }
    output_path.write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps({
        "verdict": certificate["verdict"],
        "primitive_count": exhaustive["primitive_count"],
        "future_event": certificate["path"]["first_future_event_name"],
        "endpoint_decisions": {
            name: row["endpoint"]["decision_value"]
            for name, row in certificate["directed_residuals"].items()
        },
    }, indent=2))


if __name__ == "__main__":
    main()
