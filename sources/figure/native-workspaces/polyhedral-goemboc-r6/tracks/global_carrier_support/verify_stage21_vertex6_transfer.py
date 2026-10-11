#!/usr/bin/env python3
"""Rebuild and verify the exact stage-21 H(6,7)->H(5,6) transfer."""

from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))

from verify_stage18_vertex_transfer import main  # noqa: E402


if __name__ == "__main__":
    sys.argv = [
        sys.argv[0],
        "--source", str(ROOT / "tracks/circuit_atlas/row54_far_rebuilt.csv"),
        "--audit", str(ROOT / "tracks/circuit_atlas/row54_far_rebuilt_audit.json"),
        "--birth-atlas", str(HERE / "local_birth_atlas.json"),
        "--adaptive", str(HERE / "adaptive_stage20_pre_postcircuit_guarded_h67.json"),
        "--vertex", "6",
        "--birth-neighbour", "5",
        "--death-neighbour", "7",
        "--atlas-circuit", "9", "10", "11", "263",
        "--atlas-valid-sign", "-1",
        "--extra-birth-edge", "10", "11",
        "--output", str(HERE / "stage21_vertex6_transfer_certificate.json"),
        "--pre-atlas", str(HERE / "stage21_vertex6_pre_cell_atlas.json"),
        "--far-atlas", str(HERE / "stage21_vertex6_far_cell_atlas.json"),
        "--pre-csv", str(HERE / "stage21_vertex6_transfer_pre.csv"),
        "--middle-csv", str(HERE / "stage21_vertex6_transfer_middle.csv"),
        "--far-csv", str(HERE / "stage21_vertex6_transfer_far.csv"),
    ]
    main()
    print("EXACT_DIRECTED_STAGE21_VERTEX6_CARRIER_TRANSFER_PASS")
