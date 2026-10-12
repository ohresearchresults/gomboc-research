#!/usr/bin/env python3
"""Materialize the frozen rational proof object for both nullspace bypasses."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import grouped_exact as gx  # noqa: E402

sys.path[:0] = [
    str(gx.SOURCE_DIR),
    str(gx.ROOT / "tracks/circuit_atlas"),
]
from row54_direct_actual_search import DirectActual, read_points  # noqa: E402
import row54_four_residual_search as numeric_core  # noqa: E402


OUT = HERE / "certificate.json"


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(gx.ROOT))


def frozen_point_packet(points, repair):
    encoded = gx.encode_points(points)
    return {
        "coordinates": encoded,
        "coordinate_hash": gx.canonical_hash(encoded),
        "base_repair": repair,
    }


def chart_materializer(round_number: int):
    if round_number == 2:
        source_path = gx.SOURCE_DIR / "row54_combined_hard_slp_best.csv"
    else:
        source_path = gx.SOURCE_DIR / "row54_round2_null_bypass_C_buffered_post.csv"
    ids, source = read_points(source_path)
    direct = DirectActual(ids, source)
    direct_count = len(direct.controls)

    def materialize(parameters):
        z = np.asarray(parameters, dtype=float)
        moved = direct.construct(z[:direct_count])
        transformed, denominator = numeric_core.transform(moved, z[direct_count:])
        if transformed is None or float(np.min(denominator)) <= 0.08:
            raise AssertionError("invalid saved chart point")
        rational = gx.rationalize_float_points(ids, transformed)
        repaired, repair = gx.repair_base(rational)
        return frozen_point_packet(repaired, repair)

    return source_path, materialize


def materialize_round(round_number: int):
    event_run_name = (
        "row54_combined_hard_slp_round2_event.json"
        if round_number == 2
        else "row54_combined_hard_slp_round3.json"
    )
    event_run_path = gx.SOURCE_DIR / event_run_name
    mechanics_path = gx.SOURCE_DIR / f"row54_round{round_number}_mechanical_event.json"
    bypass_path = gx.SOURCE_DIR / f"row54_round{round_number}_null_bypass.json"
    face_path = gx.SOURCE_DIR / f"row54_round{round_number}_null_bypass_endpoint_faces.json"
    event_run = json.loads(event_run_path.read_text())
    mechanics = json.loads(mechanics_path.read_text())
    bypass = json.loads(bypass_path.read_text())
    event = event_run["class_event"]
    pre = np.asarray(event["pre_parameters"], dtype=float)
    post = np.asarray(event["post_parameters"], dtype=float)
    event_t = float(mechanics["event_t"])
    delta = float(mechanics["open_sample_delta"])
    wall = (1.0 - event_t) * pre + event_t * post
    _, materialize = chart_materializer(round_number)

    event_snapshots = {
        "pre_open": materialize((1.0 - (event_t - delta)) * pre + (event_t - delta) * post),
        "post_open": materialize((1.0 - (event_t + delta)) * pre + (event_t + delta) * post),
    }
    tangent = np.asarray(bypass["tangent_direction"], dtype=float)
    transverse = np.asarray(bypass["transverse_direction"], dtype=float)
    radius = float(bypass["quadrant_radius"])
    quadrants = {}
    for tangent_sign in (-1, 1):
        for transverse_sign in (-1, 1):
            name = f"u{tangent_sign:+d}_v{transverse_sign:+d}"
            parameters = wall + radius * (
                tangent_sign * tangent + transverse_sign * transverse
            )
            quadrants[name] = materialize(parameters)

    nodes = {}
    for name in ("A_pre", "B_buffered_pre", "C_buffered_post"):
        path = gx.SOURCE_DIR / f"row54_round{round_number}_null_bypass_{name}.csv"
        points, repair = gx.read_repaired(path)
        nodes[name] = frozen_point_packet(points, repair)

    faces = json.loads(face_path.read_text())
    return {
        "pair": f"round{round_number}",
        "provenance": {
            "event_run": relative(event_run_path),
            "mechanical_event": relative(mechanics_path),
            "null_bypass": relative(bypass_path),
            "event_parameter": repr(event_t),
            "open_sample_delta": repr(delta),
            "quadrant_radius": repr(radius),
            "decimal_freeze": "format(binary64, '.17g') followed by exact Fraction",
            "base_repair": "orthogonal rational projection to plane(rows 0,1,2)",
        },
        "faces": faces,
        "face_ledger_hash": gx.canonical_hash(faces),
        "face_file": relative(face_path),
        "event_snapshots": event_snapshots,
        "quadrants": quadrants,
        "L_nodes": nodes,
    }


def input_hashes():
    names = [
        "actual_grouped.py",
        "row54_direct_actual_search.py",
        "row54_round2_mechanical_event.py",
        "row54_round3_mechanical_event.py",
        "row54_round2_mechanical_event.json",
        "row54_round3_mechanical_event.json",
        "row54_round2_null_bypass.py",
        "row54_round3_null_bypass.py",
        "row54_round2_null_bypass.json",
        "row54_round3_null_bypass.json",
        "row54_combined_hard_slp_round2_event.json",
        "row54_combined_hard_slp_round3.json",
        "row54_combined_hard_slp_best.csv",
        "row54_round2_null_bypass_A_pre.csv",
        "row54_round2_null_bypass_B_buffered_pre.csv",
        "row54_round2_null_bypass_C_buffered_post.csv",
        "row54_round2_null_bypass_endpoint_faces.json",
        "row54_round3_null_bypass_A_pre.csv",
        "row54_round3_null_bypass_B_buffered_pre.csv",
        "row54_round3_null_bypass_C_buffered_post.csv",
        "row54_round3_null_bypass_endpoint_faces.json",
        "row54_combined_hard_slp_round4.json",
        "row54_combined_hard_slp_round4_best.csv",
        "row54_combined_hard_slp_round4_best_faces.json",
        "row54_combined_hard_slp_round4b.json",
        "row54_combined_hard_slp_round4b_best.csv",
        "row54_combined_hard_slp_round4b_best_faces.json",
        "row54_combined_hard_slp_round4c.json",
        "row54_combined_hard_slp_round4c_best.csv",
        "row54_combined_hard_slp_round4c_best_faces.json",
    ]
    paths = [gx.SOURCE_DIR / name for name in names]
    paths.append(gx.ROOT / "tracks/circuit_atlas/row54_four_residual_search.py")
    return {
        relative(path): gx.ex.sha256(path)
        for path in paths
    }


def round4_nodes():
    files = {
        "round3_C": "row54_round3_null_bypass_C_buffered_post.csv",
        "round4": "row54_combined_hard_slp_round4_best.csv",
        "round4b": "row54_combined_hard_slp_round4b_best.csv",
        "round4c": "row54_combined_hard_slp_round4c_best.csv",
    }
    out = {}
    for name, filename in files.items():
        points, repair = gx.read_repaired(gx.SOURCE_DIR / filename)
        out[name] = frozen_point_packet(points, repair)
    return out


def main():
    round2 = materialize_round(2)
    round3 = materialize_round(3)
    if round2["face_ledger_hash"] != round3["face_ledger_hash"]:
        # Cycle rotations/orientations may differ while keys agree.  The proof
        # intentionally keeps each exact outward-oriented ledger separately.
        pass
    certificate = {
        "version": 1,
        "theorem_scope": (
            "Two explicit frozen-rational local event cells and their exact "
            "plane-preserving polynomial L-bypasses; plus the first wall of "
            "the explicit round3_C-to-round4 planar morph. This is not a "
            "global statement about the original nonlinear 27D chart."
        ),
        "proof_arithmetic": "fractions.Fraction plus exact Bernstein subdivision",
        "core_dependency": {
            "path": relative(gx.CORE_PATH),
            "sha256": gx.ex.sha256(gx.CORE_PATH),
        },
        "input_hashes": input_hashes(),
        "rounds": {"round2": round2, "round3": round3},
        "round4_plus": {
            "path_scope": "explicit exact planar morph round3_C -> round4 endpoint",
            "faces": round3["faces"],
            "face_ledger_hash": round3["face_ledger_hash"],
            "nodes": round4_nodes(),
            "first_pair_to_audit": "round2",
        },
    }
    OUT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "certificate": relative(OUT),
        "sha256": gx.ex.sha256(OUT),
        "round2_face_hash": round2["face_ledger_hash"],
        "round3_face_hash": round3["face_ledger_hash"],
        "input_count": len(certificate["input_hashes"]),
    }, indent=2))


if __name__ == "__main__":
    main()

