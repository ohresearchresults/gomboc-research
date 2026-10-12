#!/usr/bin/env python3
"""Build the frozen rational certificate for the round-4 null cross."""

from __future__ import annotations

import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cross_exact as cx  # noqa: E402


OUT = HERE / "certificate.json"


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(cx.ROOT))


def point_packet(path: Path):
    points, repair = cx.gx.read_repaired(path)
    encoded = cx.gx.encode_points(points)
    return {
        "source_file": relative(path),
        "source_sha256": cx.ex.sha256(path),
        "coordinates": encoded,
        "coordinate_hash": cx.gx.canonical_hash(encoded),
        "base_repair": repair,
    }, points


def source_hashes():
    names = [
        "row54_round4_null_cross.py",
        "row54_round4_null_cross.json",
        "row54_round4_topology_event.py",
        "row54_round4_topology_event.json",
        "row54_combined_hard_slp_round4c_best.csv",
        "row54_combined_hard_slp_round4c_best_faces.json",
        "row54_round4_null_cross_pre_good.csv",
        "row54_round4_null_cross_pre_good_faces.json",
        "row54_round4_null_cross_far_good.csv",
        "row54_round4_null_cross_far_good_faces.json",
        "row54_round4_null_cross_wall_buffered.csv",
        "row54_round4_null_cross_wall_buffered_faces.json",
        "row54_round4_null_cross_deep_far.csv",
        "row54_round4_null_cross_deep_far_faces.json",
    ]
    return {
        relative(cx.SOURCE_DIR / name): cx.ex.sha256(cx.SOURCE_DIR / name)
        for name in names
    }


def main():
    node_files = {
        "source": "row54_combined_hard_slp_round4c_best.csv",
        "pre_buffer": "row54_round4_null_cross_pre_good.csv",
        "far_good": "row54_round4_null_cross_far_good.csv",
        "deep_far": "row54_round4_null_cross_deep_far.csv",
    }
    nodes = {}
    exact_points = {}
    for name, filename in node_files.items():
        nodes[name], exact_points[name] = point_packet(cx.SOURCE_DIR / filename)

    face_files = {
        "pre": cx.SOURCE_DIR / "row54_round4_null_cross_pre_good_faces.json",
        "wall": cx.SOURCE_DIR / "row54_round4_null_cross_wall_buffered_faces.json",
        "far": cx.SOURCE_DIR / "row54_round4_null_cross_far_good_faces.json",
    }
    faces = {}
    for name, path in face_files.items():
        ledger = json.loads(path.read_text())
        faces[name] = {
            "source_file": relative(path),
            "source_sha256": cx.ex.sha256(path),
            "canonical_hash": cx.gx.canonical_hash(ledger),
            "cycles": ledger,
        }

    middle = cx.gx.planar_morph(exact_points["pre_buffer"], exact_points["far_good"])
    target = cx.circuit_polynomial(middle)
    root = cx.gx.root_record(target)
    derivative = cx.gx.exact_sign_record(target.derivative(), expected=-1, max_depth=80)

    certificate = {
        "version": 1,
        "verdict": "EXACT_DIRECTED_ROUND4_NULL_CROSS_PASS",
        "theorem_scope": (
            "Exact theorem for four explicitly frozen rational coordinate nodes "
            "and three exact plane-preserving polynomial morphs. It certifies "
            "the complete actual lattice and mechanics along these morphs, "
            "including one algebraic quadrilateral flip. It is not a theorem "
            "about every path in the original nonlinear binary64 27D chart."
        ),
        "proof_arithmetic": "fractions.Fraction and exact Bernstein subdivision",
        "proof_dependencies": {
            relative(cx.gx.CORE_PATH): cx.ex.sha256(cx.gx.CORE_PATH),
            relative(cx.NULL_RIGOR / "grouped_exact.py"): cx.ex.sha256(
                cx.NULL_RIGOR / "grouped_exact.py"
            ),
        },
        "input_hashes": source_hashes(),
        "nodes": nodes,
        "face_ledgers": faces,
        "segments": [
            {"name": "pre_to_buffer", "start": "source", "end": "pre_buffer", "lattice": "pre"},
            {"name": "buffered_cross", "start": "pre_buffer", "end": "far_good", "lattices": ["pre", "wall", "far"]},
            {"name": "far_deepen", "start": "far_good", "end": "deep_far", "lattice": "far"},
        ],
        "circuit": {
            "labels": list(cx.CIRCUIT),
            "polynomial_degree": target.degree,
            "polynomial_coefficients_exact": target.exact(),
            "polynomial_digest": cx.gx.canonical_hash(target.exact()),
            "whole_segment_derivative": derivative,
            "unique_root": root,
            "wall_face": [7, 8, 246, 245],
        },
    }
    OUT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "certificate": relative(OUT),
        "certificate_sha256": cx.ex.sha256(OUT),
        "pre_face_hash": faces["pre"]["canonical_hash"],
        "wall_face_hash": faces["wall"]["canonical_hash"],
        "far_face_hash": faces["far"]["canonical_hash"],
        "circuit_root": root["decimal_interval"],
    }, indent=2))


if __name__ == "__main__":
    main()

