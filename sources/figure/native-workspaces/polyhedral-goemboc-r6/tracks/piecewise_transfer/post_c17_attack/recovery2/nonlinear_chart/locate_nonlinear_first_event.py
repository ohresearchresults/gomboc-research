#!/usr/bin/env python3
"""Exhaustive exact first-primitive locator on the nonlinear degree-two path.

All frozen-face support rows, every non-triangular in-face turn, volume and
all own-centroid face/vertex/edge primitives are scanned.  This is a locator;
the first wall still requires a separate event-cell certificate.
"""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ATTACK = HERE.parents[1]
PATH_JSON = HERE / "nonlinear_polynomial_path.json"
DIRECTION_JSON = HERE / "exterior_direction.json"
OUTPUT = HERE / "nonlinear_first_event_scan.json"
CORE = ATTACK.parents[1] / "global_carrier_support" / "rigorous_local_bypass"
sys.path.insert(0, str(ATTACK))
sys.path.insert(0, str(CORE))

import exact_core as ex  # noqa: E402


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_path(payload):
    return {
        int(label): tuple(
            ex.P(tuple(Q(value) for value in component))
            for component in xyz
        )
        for label, xyz in payload["coordinate_polynomials_exact_ascending"].items()
    }


def primitive_rows(path, faces):
    ledger = ex.mechanics_primitives(path, faces)
    yield "volume_d6", ledger["d6"], "mechanics_denominator"
    for face_index, witness, polynomial in ex.support_polynomials(path, faces):
        yield f"support:f{face_index}:w{witness}", polynomial, "support"
    for face_index, cycle in enumerate(faces):
        if len(cycle) <= 3:
            continue
        normal = ex.cycle_normal(cycle, path)
        for offset, current in enumerate(cycle):
            previous = cycle[offset - 1]
            following = cycle[(offset + 1) % len(cycle)]
            turn = ex.dot(
                ex.cross(
                    ex.sub(path[current], path[previous]),
                    ex.sub(path[following], path[current]),
                ),
                normal,
            )
            yield f"in_face_turn:f{face_index}:v{current}", turn, "in_face_turn"
    for face_key, rows in sorted(ledger["reference"].items()):
        for edge, value in sorted(rows.items()):
            yield f"face_reference:{face_key}:{edge}", value, "mechanics_denominator"
    for face_key, rows in sorted(ledger["face"].items()):
        for edge, value in sorted(rows.items()):
            yield f"face_raw:{face_key}:{edge}", value, "face_component"
    for vertex, rows in sorted(ledger["vertex"].items()):
        for neighbor, value in sorted(rows.items()):
            yield f"vertex:{vertex}:{neighbor}", value, "vertex_component"
    for edge, rows in sorted(ledger["edge"].items()):
        for component in (
            "direction_norm2",
            "gram",
            "t",
            "one_minus_t",
            "beta1",
            "beta2",
        ):
            yield f"edge:{edge}:{component}", rows[component], "edge_component"


def normalized_coefficients(polynomial, lo, hi, start_sign):
    return tuple(
        start_sign * value
        for value in ex.bernstein_coefficients(polynomial.affine(lo, hi))
    )


def strictly_same_sign(polynomial, lo, hi, start_sign, max_depth=40):
    stack = [(Q(lo), Q(hi), 0)]
    leaves = 0
    worst = None
    while stack:
        left, right, depth = stack.pop()
        coefficients = normalized_coefficients(polynomial, left, right, start_sign)
        if all(value > 0 for value in coefficients):
            leaves += 1
            margin = min(coefficients)
            log10 = ex.qlog10(margin)
            worst = log10 if worst is None else min(worst, log10)
            continue
        if depth >= max_depth:
            return False, leaves, worst
        middle = (left + right) / 2
        stack.append((middle, right, depth + 1))
        stack.append((left, middle, depth + 1))
    return True, leaves, worst


def first_non_strict_bracket(polynomial, horizon, start_sign, depth=80):
    stack = [(Q(0), Q(horizon), 0)]
    while stack:
        left, right, level = stack.pop()
        coefficients = normalized_coefficients(polynomial, left, right, start_sign)
        if all(value > 0 for value in coefficients):
            continue
        if level >= depth:
            return left, right
        middle = (left + right) / 2
        stack.append((middle, right, level + 1))
        stack.append((left, middle, level + 1))
    return None


def main():
    payload = json.loads(PATH_JSON.read_text())
    direction = json.loads(DIRECTION_JSON.read_text())
    assert payload["verdict"] == "EXACT_POST_C17_NONLINEAR_POLYNOMIAL_PATH_MATERIALIZED_PASS"
    assert direction["verdict"] == "EXACT_POST_C17_EXTERIOR_DIRECTION_PASS"
    path = load_path(payload)
    faces = json.loads((ATTACK / "cells" / "endpoint.json").read_text())[
        "maximal_face_cycles"
    ]
    primitives = list(primitive_rows(path, faces))
    assert len(primitives) == 12363
    starts = []
    for name, polynomial, _family in primitives:
        value = polynomial.eval(Q(0))
        if not value:
            raise AssertionError(("zero primitive at source", name))
        starts.append(1 if value > 0 else -1)

    horizon = Q(1)
    horizon_audits = []
    while horizon <= Q(2**20):
        failures = []
        leaves = 0
        worst = None
        for (name, polynomial, family), sign in zip(primitives, starts):
            strict, count, margin = strictly_same_sign(polynomial, Q(0), horizon, sign)
            leaves += count
            if margin is not None:
                worst = margin if worst is None else min(worst, margin)
            if not strict:
                failures.append({"name": name, "family": family})
        horizon_audits.append({
            "horizon": ex.qs(horizon),
            "strict": not failures,
            "failure_count": len(failures),
            "first_failures": failures[:30],
            "proved_leaf_count": leaves,
            "minimum_proved_bernstein_log10_abs": worst,
        })
        print("HORIZON", ex.qs(horizon), "failures", len(failures), flush=True)
        if failures:
            break
        horizon *= 2
    else:
        raise RuntimeError("no primitive event through configured horizon")

    candidates = []
    for (name, polynomial, family), sign in zip(primitives, starts):
        strict, _leaves, _margin = strictly_same_sign(polynomial, Q(0), horizon, sign)
        if strict:
            continue
        bracket = first_non_strict_bracket(polynomial, horizon, sign)
        assert bracket is not None
        lo, hi = bracket
        candidates.append({
            "name": name,
            "family": family,
            "lo": ex.qs(lo),
            "hi": ex.qs(hi),
            "decimal": [float(lo), float(hi)],
            "degree": polynomial.degree,
            "start_sign": sign,
            "value_lo": ex.qs(polynomial.eval(lo)),
            "value_hi": ex.qs(polynomial.eval(hi)),
            "polynomial_exact": polynomial.exact(),
            "polynomial_digest": hashlib.sha256(
                "|".join(polynomial.exact()).encode()
            ).hexdigest(),
        })
    candidates.sort(key=lambda row: (Q(row["lo"]), Q(row["hi"]), row["name"]))
    assert candidates
    first_lo = Q(candidates[0]["lo"])
    first_hi = Q(candidates[0]["hi"])
    tied = [
        row for row in candidates
        if Q(row["lo"]) <= first_hi and Q(row["hi"]) >= first_lo
    ]
    family_counts = {
        family: sum(1 for _name, _poly, item in primitives if item == family)
        for family in sorted({family for _name, _poly, family in primitives})
    }
    result = {
        "version": 1,
        "scope": "exhaustive exact-Bernstein first-event locator on nonlinear degree-two path",
        "source_hashes": {
            "nonlinear_polynomial_path.json": sha256(PATH_JSON),
            "exterior_direction.json": sha256(DIRECTION_JSON),
            "cells/endpoint.json": sha256(ATTACK / "cells" / "endpoint.json"),
        },
        "primitive_count": len(primitives),
        "family_counts": family_counts,
        "horizon_audits": horizon_audits,
        "search_horizon": ex.qs(horizon),
        "candidate_count": len(candidates),
        "first_candidate": candidates[0],
        "overlapping_first_candidates": tied,
        "next_candidates": candidates[:30],
        "verdict": "EXHAUSTIVE_EXACT_POST_C17_NONLINEAR_FIRST_EVENT_LOCATOR_PASS",
        "proof_status": "LOCATOR_ONLY_EVENT_CELL_CERTIFICATE_REQUIRED",
        "winner_status": "NONWINNER",
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    print(result["verdict"])
    print("primitive_count", len(primitives))
    print("family_counts", family_counts)
    print("first_candidate", json.dumps(candidates[0], indent=2))
    print("output_sha256", sha256(OUTPUT))


if __name__ == "__main__":
    main()
