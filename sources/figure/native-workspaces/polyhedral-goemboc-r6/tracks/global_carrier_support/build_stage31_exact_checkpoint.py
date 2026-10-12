#!/usr/bin/env python3
"""Build the exact rational audit of the stage-31 terminal checkpoint."""
from pathlib import Path

import build_stage30_exact_checkpoint as shared


HERE = Path(__file__).resolve().parent


if __name__ == "__main__":
    shared.build_checkpoint(
        HERE / "adaptive_stage31_postexact_h56_focus.json",
        HERE / "stage31_exact_checkpoint_raw.csv",
        HERE / "stage31_exact_checkpoint.csv",
        HERE / "stage31_exact_checkpoint_faces.json",
        HERE / "stage31_exact_checkpoint_certificate.json",
        "EXACT_STAGE31_FAR_H56_CHECKPOINT_PASS",
    )
