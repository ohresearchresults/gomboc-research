#!/usr/bin/env python3
"""Certify one intrinsic SLP step beyond the mandatory-rail bypass."""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
ROOT = HERE.parents[3]
sys.path[:0] = [str(PARENT), str(HERE)]

import build_u54_material_exact_path as source  # noqa: E402
import combined_four_death_lp as four  # noqa: E402
from integrate_four_death_direction import write_csv  # noqa: E402
import post_flip_trust_slp as slp  # noqa: E402
import certify_mandatory_rail_bypass as bypass  # noqa: E402


START_FILE = HERE / "mandatory_rail_bypass_interior_checkpoint.csv"
REPORT = HERE / "post_bypass_recomputed_event.json"
RAW_ENDPOINT = HERE / "post_bypass_intrinsic_step_raw.csv"
EXACT_ENDPOINT = HERE / "post_bypass_intrinsic_step_exact.csv"
FACE_FILE = HERE / "post_bypass_intrinsic_step_faces.json"
CERTIFICATE = HERE / "post_bypass_intrinsic_step_certificate.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def face_signature(result):
    return tuple(sorted(tuple(sorted(face["cycle"])) for face in result.faces))


def equilibrium_signature(result):
    return (
        tuple(sorted(tuple(sorted(result.faces[index]["cycle"])) for index, _ in result.stable)),
        tuple(sorted(index for index, _ in result.unstable)),
        tuple(sorted(tuple(edge) for edge, _ in result.saddles)),
    )


def repair_pair(start, endpoint):
    anchor = start[0]
    normal = source.ex.cross(source.ex.sub(start[1], anchor), source.ex.sub(start[2], anchor))
    normal_norm2 = source.ex.norm2(normal)
    def project(rows):
        out = dict(rows)
        corrections = {}
        for label in source.BASE:
            coefficient = source.ex.dot(normal, source.ex.sub(out[label], anchor)) / normal_norm2
            out[label] = source.ex.sub(out[label], source.ex.mul(normal, coefficient))
            corrections[label] = coefficient
            if source.ex.dot(normal, source.ex.sub(out[label], anchor)):
                raise AssertionError(("base projection failed", label))
        nonzero = [value for value in corrections.values() if value]
        return out, {
            "nonzero_count": len(nonzero),
            "maximum_log10_abs": (
                max(source.ex.qlog10(value) for value in nonzero) if nonzero else None
            ),
        }

    repaired_start, start_base = project(start)
    repaired_endpoint, endpoint_base = project(endpoint)
    repaired_start, _start_uv, start_quad = source.repair_quad(repaired_start)
    repaired_endpoint, _endpoint_uv, endpoint_quad = source.repair_quad(repaired_endpoint)
    return repaired_start, repaired_endpoint, {
        "start_base": start_base,
        "endpoint_base": endpoint_base,
        "start_quad": start_quad,
        "endpoint_quad": endpoint_quad,
    }


def main() -> None:
    report = json.loads(REPORT.read_text())
    points = slp.load_exact_float(START_FILE)
    modes, _meta, _chart = four.chart_modes(points)
    coefficients = np.asarray(report["best"]["coefficients"], dtype=float)
    baseline = source.actual.evaluate(points, coplanar_rel=2e-12)
    if not baseline.valid:
        raise RuntimeError(baseline.error)
    baseline_faces = face_signature(baseline)
    baseline_equilibria = equilibrium_signature(baseline)
    forced_rails = source.forced_rails()
    minimum_margin = float("inf")
    for parameter in np.linspace(0.0, 1.0, 101):
        candidate = slp.apply_modes(points, modes, parameter * coefficients)
        result = source.actual.evaluate(candidate, coplanar_rel=2e-12)
        if not result.valid:
            raise AssertionError((parameter, result.error))
        if face_signature(result) != baseline_faces:
            raise AssertionError((parameter, "face signature changed"))
        if equilibrium_signature(result) != baseline_equilibria:
            raise AssertionError((parameter, "equilibrium signature changed"))
        if [len(result.active), len(result.edges), len(result.faces)] != [60, 158, 100]:
            raise AssertionError((parameter, "f-vector"))
        if not forced_rails.issubset(set(result.edges)):
            raise AssertionError((parameter, "rail loss"))
        minimum_margin = min(minimum_margin, float(result.topology_margin))
    endpoint_float = slp.apply_modes(points, modes, coefficients)
    write_csv(RAW_ENDPOINT, endpoint_float)

    exact_start_raw = source.ex.read_rows(START_FILE)
    exact_endpoint_raw = source.ex.read_rows(RAW_ENDPOINT)
    exact_start, exact_endpoint, repair = repair_pair(exact_start_raw, exact_endpoint_raw)
    path = bypass.make_path(exact_start, exact_endpoint)
    representative = source.evaluate_path(path, Q(1, 2))
    faces, _ = source.fresh_faces(representative)
    support, mechanics = source.assert_cell(representative, faces)
    cover = source.exact_class_cover(path, faces, Q(0), Q(1))
    determinant = source.determinant_polynomial(path, bypass.CIRCUIT)
    midpoint_value = determinant.eval(Q(1, 2))
    sign = 1 if midpoint_value > 0 else -1 if midpoint_value < 0 else 0
    determinant_sign = source.exact_sign_record(determinant, Q(0), Q(1), sign)
    reference = bypass.selected_residuals(exact_start, faces)
    endpoint_values = bypass.selected_residuals(exact_endpoint, faces)
    comparison = bypass.comparison_packet(reference, endpoint_values)
    source.write_exact_csv(EXACT_ENDPOINT, exact_endpoint)
    FACE_FILE.write_text(json.dumps(faces, indent=2) + "\n")
    generated = [RAW_ENDPOINT, EXACT_ENDPOINT, FACE_FILE]
    payload = {
        "version": 1,
        "scope": "first exact intrinsic SLP step after mandatory-rail bypass",
        "verdict": "EXACT_POST_BYPASS_MATERIAL_STEP_PASS",
        "source": str(START_FILE.relative_to(ROOT)),
        "source_direction_report": str(REPORT.relative_to(ROOT)),
        "sampled_path_count": 101,
        "sampled_minimum_topology_margin": minimum_margin,
        "repair": repair,
        "face_file": str(FACE_FILE.relative_to(ROOT)),
        "face_hash": canonical_hash(faces),
        "f_vector": support["f_vector"],
        "mechanics": mechanics,
        "class_cover": cover,
        "class_cover_subinterval_count": len(cover),
        "mandatory_circuit_sign": determinant_sign,
        "endpoint_material_comparison": comparison,
        "endpoint_file": str(EXACT_ENDPOINT.relative_to(ROOT)),
        "generated_sha256": {
            str(path.relative_to(ROOT)): sha256(path) for path in generated
        },
        "conclusion": (
            "The exact intrinsic segment remains in the same strict (2,2,2) "
            "cell, preserves all rails and the mandatory-circuit side, and "
            "strictly improves every selected residual."
        ),
    }
    CERTIFICATE.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "verdict": payload["verdict"],
        "class": mechanics["class"],
        "class_cover_count": len(cover),
        "sampled_minimum_topology_margin": minimum_margin,
        "endpoint_ratios": {
            name: row["decimal_ratio"] for name, row in comparison.items()
        },
        "certificate": str(CERTIFICATE),
    }, indent=2))


if __name__ == "__main__":
    main()
