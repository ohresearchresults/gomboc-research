#!/usr/bin/env python3
"""Exact proof helpers for the three-segment round-4 null cross."""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE_DIR = HERE.parent
ROOT = HERE.parents[3]
NULL_RIGOR = SOURCE_DIR / "rigorous_null_bypass"
sys.path.insert(0, str(NULL_RIGOR))
import grouped_exact as gx  # noqa: E402


ex = gx.ex
P = gx.P
BASE = gx.BASE
CIRCUIT = (7, 8, 245, 246)
SHORT_RAIL = [228] + list(range(229, 247)) + [8]
LONG_RAIL = [228] + list(range(247, 265)) + [8]


def circuit_polynomial(points):
    a, b, c, d = (points[i] for i in CIRCUIT)
    return ex.det3(ex.sub(b, a), ex.sub(c, a), ex.sub(d, a))


def polynomial_divmod(dividend: P, divisor: P):
    if divisor == P.zero():
        raise ZeroDivisionError
    remainder = list(dividend.c)
    divisor_coefficients = list(divisor.c)
    if len(remainder) < len(divisor_coefficients):
        return P.zero(), dividend
    quotient = [Q(0)] * (len(remainder) - len(divisor_coefficients) + 1)
    while len(remainder) >= len(divisor_coefficients) and any(remainder):
        degree = len(remainder) - len(divisor_coefficients)
        coefficient = remainder[-1] / divisor_coefficients[-1]
        quotient[degree] = coefficient
        for j, value in enumerate(divisor_coefficients):
            remainder[degree + j] -= coefficient * value
        while len(remainder) > 1 and remainder[-1] == 0:
            remainder.pop()
    return P(tuple(quotient)), P(tuple(remainder))


def remove_target_factors(poly: P, target: P):
    multiplicity = 0
    quotient = poly
    while True:
        candidate, remainder = polynomial_divmod(quotient, target)
        if remainder != P.zero():
            break
        multiplicity += 1
        quotient = candidate
    return multiplicity, quotient


def _digest_record(digest, name, sign, poly, multiplicity=0):
    digest.update(name.encode())
    digest.update(b"|")
    digest.update(str(multiplicity).encode())
    digest.update(b"|")
    digest.update(str(sign).encode())
    digest.update(b"|")
    digest.update("|".join(poly.exact()).encode())
    digest.update(b"\n")


def audit_root_neighborhood(points, faces, target, lo: Q, hi: Q):
    """Certify all primitives through a circuit bracket by exact factorization.

    Strict primitives receive a direct Bernstein sign.  Every primitive that
    vanishes at the circuit wall must be exactly divisible by the target;
    its quotient is strictly signed on the whole bracket.
    """
    _, records = gx.all_primitives(points, faces)
    strict_count = 0
    factored = []
    leaves = 0
    worst = None
    digest = hashlib.sha256()
    for name, poly, intrinsically_positive in records:
        multiplicity, quotient = remove_target_factors(poly, target)
        sign, local_leaves, local_worst = ex.bernstein_sign(
            quotient if multiplicity else poly, lo, hi, max_depth=80
        )
        if intrinsically_positive:
            if multiplicity % 2 or sign != 1:
                raise AssertionError(("positive primitive has bad target factor", name))
        leaves += local_leaves
        worst = local_worst if worst is None else min(worst, local_worst)
        if multiplicity:
            packet = {
                "name": name,
                "target_multiplicity": multiplicity,
                "quotient_sign": sign,
                "quotient_degree": quotient.degree,
                "quotient_digest": gx.canonical_hash(quotient.exact()),
            }
            factored.append(packet)
            _digest_record(digest, name, sign, quotient, multiplicity)
        else:
            strict_count += 1
            _digest_record(digest, name, sign, poly)
    return {
        "interval": [ex.qs(lo), ex.qs(hi)],
        "total_primitive_count": len(records),
        "strict_primitive_count": strict_count,
        "target_factored_primitive_count": len(factored),
        "target_factored_primitives": factored,
        "bernstein_leaf_count": leaves,
        "min_bernstein_coefficient_log10_abs": worst,
        "factor_ledger_digest": digest.hexdigest(),
    }


def wall_support_audit(points, wall_faces, target, lo: Q, hi: Q):
    all_labels = set(points)
    equalities = []
    support_count = 0
    leaves = 0
    worst = None
    digest = hashlib.sha256()
    for fi, cycle in enumerate(wall_faces):
        normal = ex.cycle_normal(cycle, points)
        anchor = points[cycle[0]]
        for member in cycle[1:]:
            value = ex.dot(normal, ex.sub(points[member], anchor))
            if value == P.zero():
                continue
            ratio = ex.proportional(value, target)
            if ratio is None:
                raise AssertionError(("wall member not target-coplanar", fi, member))
            equalities.append({
                "face_index": fi,
                "member": member,
                "target_ratio_exact": ex.qs(ratio),
            })
        face_sign = None
        for witness in sorted(all_labels - set(cycle)):
            value = ex.dot(normal, ex.sub(points[witness], anchor))
            sign, local_leaves, local_worst = ex.bernstein_sign(
                value, lo, hi, max_depth=80
            )
            if face_sign is None:
                face_sign = sign
            elif sign != face_sign:
                raise AssertionError(("mixed wall support", fi, witness))
            _digest_record(digest, f"support:f{fi}:w{witness}", sign, value)
            support_count += 1
            leaves += local_leaves
            worst = local_worst if worst is None else min(worst, local_worst)
    incidence, _, _ = ex.edge_data(wall_faces)
    active = set().union(*(set(face) for face in wall_faces))
    edges = set(incidence)
    for rail in (SHORT_RAIL, LONG_RAIL):
        for a, b in zip(rail, rail[1:]):
            if tuple(sorted((a, b))) not in edges:
                raise AssertionError(("rail missing at wall", a, b))
    if tuple(sorted(BASE)) not in {tuple(sorted(face)) for face in wall_faces}:
        raise AssertionError("base face absent at wall")
    return {
        "f_vector": [len(active), len(incidence), len(wall_faces)],
        "euler": len(active) - len(incidence) + len(wall_faces),
        "target_coplanarity_equalities": equalities,
        "strict_nonmember_support_polynomial_count": support_count,
        "support_bernstein_leaf_count": leaves,
        "min_support_bernstein_log10_abs": worst,
        "support_digest": digest.hexdigest(),
        "base_and_all_rails": True,
    }


def wall_mechanics_records(points, faces):
    ledger = ex.mechanics_primitives(points, faces)
    records = [("volume:d6", ledger["d6"], True)]
    for face_key, values in ledger["reference"].items():
        fk = gx.face_key_text(face_key)
        for edge, poly in values.items():
            records.append((f"face_reference:{fk}:{gx.edge_text(edge)}", poly, False))
    for edge, components in ledger["edge"].items():
        et = gx.edge_text(edge)
        records.append((f"edge_direction_norm2:{et}", components["direction_norm2"], True))
        records.append((f"edge_gram:{et}", components["gram"], True))
    for face_key in ledger["face"]:
        fk = gx.face_key_text(face_key)
        for edge, poly in ex.signed_face_components(ledger, face_key).items():
            records.append((f"face:{fk}:{gx.edge_text(edge)}", poly, False))
    for vertex, values in ledger["vertex"].items():
        for neighbor, poly in values.items():
            records.append((f"vertex:{vertex}:{neighbor}", poly, False))
    for edge, components in ledger["edge"].items():
        et = gx.edge_text(edge)
        for component in ("t", "one_minus_t", "beta1", "beta2"):
            records.append((f"edge:{et}:{component}", components[component], False))
    return ledger, records


def wall_mechanics_audit(points, faces, lo: Q, hi: Q):
    _, records = wall_mechanics_records(points, faces)
    digest = hashlib.sha256()
    leaves = 0
    worst = None
    middle = (lo + hi) / 2
    for name, poly, intrinsically_positive in records:
        value = poly.eval(middle)
        if not value:
            raise AssertionError(("zero wall mechanics primitive", name))
        expected = 1 if value > 0 else -1
        if intrinsically_positive and expected != 1:
            raise AssertionError(("nonpositive wall incidence primitive", name))
        sign, local_leaves, local_worst = ex.bernstein_sign(
            poly, lo, hi, max_depth=80
        )
        if sign != expected:
            raise AssertionError(("wall mechanics sign mismatch", name))
        _digest_record(digest, name, sign, poly)
        leaves += local_leaves
        worst = local_worst if worst is None else min(worst, local_worst)
    point = gx.evaluate_path(points, middle)
    _, mechanics = ex.classify_point(point, faces)
    return {
        "interval": [ex.qs(lo), ex.qs(hi)],
        "certified_polynomial_count": len(records),
        "bernstein_leaf_count": leaves,
        "min_bernstein_coefficient_log10_abs": worst,
        "primitive_digest": digest.hexdigest(),
        "midpoint_formula_class": mechanics,
    }


def four_guard_audit(points, faces, lo=Q(0), hi=Q(1)):
    out = {}
    for pair_name in ("round2", "round3"):
        shared, duplicate, spec = gx.pair_polynomials(points, faces, pair_name)
        if shared != duplicate:
            raise AssertionError(("old U/H identity failed", pair_name))
        sign = gx.exact_sign_record(shared, lo, hi, expected=-1, max_depth=80)
        out[spec["vertex_name"]] = {
            "requested_guard_sign": 1,
            "raw_numerator_sign": -1,
            "certificate": sign,
            "identical_to": spec["edge_name"],
        }
        out[spec["edge_name"]] = {
            "requested_guard_sign": 1,
            "raw_numerator_sign": -1,
            "certificate": sign,
            "identical_to": spec["vertex_name"],
        }
    return out


def face_edge_sets(faces):
    face_keys = {tuple(sorted(face)) for face in faces}
    edges = set()
    for cycle in faces:
        for a, b in zip(cycle, cycle[1:] + cycle[:1]):
            edges.add(tuple(sorted((a, b))))
    return face_keys, edges

