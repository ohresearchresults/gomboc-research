#!/usr/bin/env python3
"""Materialize a strict post-diagonal cell for the intrinsic SLP event."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
sys.path[:0] = [str(PARENT), str(HERE)]

import build_u54_material_exact_path as exact_path  # noqa: E402
import combined_four_death_lp as four  # noqa: E402
from integrate_four_death_direction import write_csv  # noqa: E402
import post_flip_trust_slp as slp  # noqa: E402


SOURCE = HERE / "post_flip_intrinsic_step_008.csv"
REPORT = HERE / "recomputed_intrinsic_event.json"


def face_signature(result):
    return tuple(sorted(tuple(sorted(face["cycle"])) for face in result.faces))


def snapshot(result):
    return {
        "valid": bool(result.valid),
        "error": result.error,
        "f_vector": [len(result.active), len(result.edges), len(result.faces)],
        "class": [len(result.stable), len(result.unstable), len(result.saddles)],
        "stable": [sorted(result.faces[index]["cycle"]) for index, _ in result.stable],
        "unstable": [index for index, _ in result.unstable],
        "saddles": [list(edge) for edge, _ in result.saddles],
        "topology_margin": float(result.topology_margin),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=str(SOURCE))
    parser.add_argument("--report", default=str(REPORT))
    parser.add_argument("--prefix", default="intrinsic_event")
    args = parser.parse_args()
    source_file = Path(args.source)
    if not source_file.is_absolute():
        source_file = HERE / source_file
    report_file = Path(args.report)
    if not report_file.is_absolute():
        report_file = HERE / report_file
    report = json.loads(report_file.read_text())
    points = slp.load_exact_float(source_file)
    modes, _meta, _chart = four.chart_modes(points)
    coefficients = np.asarray(report["best"]["coefficients"], dtype=float)
    root = sum(report["event"]["fraction_bracket"]) / 2.0
    baseline = exact_path.actual.evaluate(points, coplanar_rel=2e-12)
    if not baseline.valid:
        raise RuntimeError(baseline.error)
    baseline_faces = face_signature(baseline)

    probes = []
    far = None
    for offset in (
        1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4,
        1e-3, 1e-2, 5e-2, 1e-1, 2e-1, 5e-1,
    ):
        parameter = root + offset
        candidate = slp.apply_modes(points, modes, parameter * coefficients)
        result = exact_path.actual.evaluate(candidate, coplanar_rel=2e-12)
        signature = face_signature(result) if result.valid else ()
        record = {
            "offset": offset,
            "parameter": parameter,
            "snapshot": snapshot(result),
            "removed_faces": [
                list(face) for face in sorted(set(baseline_faces) - set(signature))
            ] if signature else [],
            "added_faces": [
                list(face) for face in sorted(set(signature) - set(baseline_faces))
            ] if signature else [],
        }
        probes.append(record)
        if (
            result.valid
            and [len(result.active), len(result.edges), len(result.faces)] == [60, 158, 100]
            and signature != baseline_faces
            and (far is None or result.topology_margin > far[1].topology_margin)
        ):
            far = (candidate, result, record)
    if far is None:
        raise RuntimeError("strict post-diagonal cell not found")
    far_points, far_result, far_record = far
    far_file = HERE / f"{args.prefix}_far.csv"
    write_csv(far_file, far_points)
    payload = {
        "version": 1,
        "scope": "strict post-diagonal materialization for one resolved intrinsic circuit",
        "source": source_file.name,
        "report": report_file.name,
        "root_locator": report["event"]["fraction_bracket"],
        "probes": probes,
        "selected_far": {**far_record, "file": far_file.name},
        "conclusion": "strict post-diagonal (60,158,100) cell materialized",
    }
    output = HERE / f"{args.prefix}_far.json"
    output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "selected_far": payload["selected_far"],
        "output": str(output),
    }, indent=2))


if __name__ == "__main__":
    main()
