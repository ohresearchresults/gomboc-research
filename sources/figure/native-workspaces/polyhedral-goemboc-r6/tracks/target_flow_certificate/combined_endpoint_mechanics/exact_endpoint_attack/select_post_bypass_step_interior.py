#!/usr/bin/env python3
"""Choose a float-stable rational point on the certified post-bypass step."""
from __future__ import annotations

import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
sys.path[:0] = [str(PARENT), str(HERE)]

import build_u54_material_exact_path as source  # noqa: E402
import combined_four_death_lp as four  # noqa: E402
import certify_mandatory_rail_bypass as bypass  # noqa: E402
import certify_post_bypass_step as builder  # noqa: E402


OUTPUT = HERE / "post_bypass_intrinsic_step_interior.csv"
REPORT = HERE / "post_bypass_intrinsic_step_interior.json"


def main() -> None:
    start_raw = source.ex.read_rows(builder.START_FILE)
    endpoint_raw = source.ex.read_rows(builder.RAW_ENDPOINT)
    start, endpoint, _repair = builder.repair_pair(start_raw, endpoint_raw)
    path = bypass.make_path(start, endpoint)
    certificate = json.loads(builder.CERTIFICATE.read_text())
    faces = json.loads((builder.ROOT / certificate["face_file"]).read_text())
    reference = bypass.selected_residuals(start, faces)
    candidates = []
    chosen_points = None
    selected = None
    for parameter in (Q(1, 4), Q(1, 2), Q(3, 4), Q(7, 8), Q(9, 10), Q(15, 16), Q(31, 32)):
        points = source.evaluate_path(path, parameter)
        comparison = bypass.comparison_packet(reference, bypass.selected_residuals(points, faces))
        float_points = {
            label: np.asarray([float(value) for value in xyz], dtype=float)
            for label, xyz in points.items()
        }
        try:
            result, _values = four.primitive_ledger(float_points, plane_tol=2e-12)
            valid = True
            error = None
            f_vector = [len(result.active), len(result.edges), len(result.faces)]
            klass = [len(result.stable), len(result.unstable), len(result.saddles)]
            margin = float(result.topology_margin)
        except Exception as exc:
            valid = False
            error = repr(exc)
            f_vector = klass = margin = None
        row = {
            "parameter": source.ex.qs(parameter),
            "parameter_decimal": float(parameter),
            "comparison": comparison,
            "evaluator_valid": valid,
            "evaluator_error": error,
            "f_vector": f_vector,
            "class": klass,
            "topology_margin": margin,
        }
        candidates.append(row)
        if valid and f_vector == [60, 158, 100] and klass == [2, 2, 2]:
            if selected is None or parameter > Q(selected["parameter"]):
                selected = row
                chosen_points = points
    if selected is None or chosen_points is None:
        raise RuntimeError("no float-stable exact interior point")
    source.write_exact_csv(OUTPUT, chosen_points)
    payload = {
        "version": 1,
        "scope": "float-stable point on exact post-bypass material segment",
        "source_certificate": builder.CERTIFICATE.name,
        "candidates": candidates,
        "selected": {**selected, "file": OUTPUT.name},
    }
    REPORT.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload["selected"], indent=2))


if __name__ == "__main__":
    main()
