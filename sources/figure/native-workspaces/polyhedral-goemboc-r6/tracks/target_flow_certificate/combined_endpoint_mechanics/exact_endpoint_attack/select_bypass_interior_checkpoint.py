#!/usr/bin/env python3
"""Choose a well-conditioned exact interior point on the certified bypass."""
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
import certify_mandatory_rail_bypass as builder  # noqa: E402
import combined_four_death_lp as four  # noqa: E402


OUTPUT = HERE / "mandatory_rail_bypass_interior_checkpoint.csv"
REPORT = HERE / "mandatory_rail_bypass_interior_checkpoint.json"


def main() -> None:
    snapshots, _repair = builder.repair_snapshots()
    path = builder.make_path(snapshots["lifted"], snapshots["endpoint"])
    certificate = json.loads(builder.CERTIFICATE.read_text())
    faces = json.loads((builder.ROOT / certificate["face_file"]).read_text())
    reference = builder.selected_residuals(snapshots["source"], faces)
    candidates = []
    for parameter in (Q(1, 2), Q(3, 4), Q(7, 8), Q(9, 10), Q(15, 16), Q(31, 32), Q(63, 64)):
        points = source.evaluate_path(path, parameter)
        residual = builder.selected_residuals(points, faces)
        comparison = builder.comparison_packet(reference, residual)
        float_points = {
            label: np.asarray([float(value) for value in xyz], dtype=float)
            for label, xyz in points.items()
        }
        try:
            result, _values = four.primitive_ledger(float_points, plane_tol=2e-12)
            evaluator_valid = True
            evaluator_error = None
            f_vector = [len(result.active), len(result.edges), len(result.faces)]
            klass = [len(result.stable), len(result.unstable), len(result.saddles)]
            topology_margin = float(result.topology_margin)
        except Exception as error:
            evaluator_valid = False
            evaluator_error = repr(error)
            f_vector = klass = None
            topology_margin = None
        candidates.append({
            "parameter": source.ex.qs(parameter),
            "parameter_decimal": float(parameter),
            "comparison": comparison,
            "evaluator_valid": evaluator_valid,
            "evaluator_error": evaluator_error,
            "f_vector": f_vector,
            "class": klass,
            "topology_margin": topology_margin,
            "points": points,
        })
    usable = [
        row for row in candidates
        if row["evaluator_valid"]
        and row["f_vector"] == [60, 158, 100]
        and row["class"] == [2, 2, 2]
    ]
    if not usable:
        raise RuntimeError("no well-conditioned interior checkpoint")
    selected = max(usable, key=lambda row: row["parameter_decimal"])
    source.write_exact_csv(OUTPUT, selected.pop("points"))
    for row in candidates:
        row.pop("points", None)
    payload = {
        "version": 1,
        "scope": "well-conditioned rational checkpoint on exact bypass segment 3",
        "source_certificate": builder.CERTIFICATE.name,
        "candidates": candidates,
        "selected": {**selected, "file": OUTPUT.name},
        "conclusion": "selected point lies inside the already exact-certified segment",
    }
    REPORT.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload["selected"], indent=2))


if __name__ == "__main__":
    main()
