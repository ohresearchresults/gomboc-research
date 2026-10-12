#!/usr/bin/env python3
"""Independent clean-engine verifier for the tenth safe flip."""
from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ENGINE_PATH = MAIN / "verify_safe_flip.py"
SPEC = importlib.util.spec_from_file_location(
    "post_c17_clean_tenth_flip_engine", ENGINE_PATH
)
assert SPEC is not None and SPEC.loader is not None
clean = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(clean)


def main():
    previous = MAIN / "post_transfer_round4"
    clean.SOURCE = previous / "far.csv"
    clean.CANDIDATE = HERE / "candidate.csv"
    clean.CERTIFICATE = HERE / "certificate.json"
    clean.OUTPUT = HERE / "verification.json"
    clean.PRE_FACES_PATH = previous / "post_faces.json"
    clean.WALL_FACES_PATH = HERE / "wall_faces.json"
    clean.POST_FACES_PATH = HERE / "post_faces.json"
    clean.FAR_PARAMETER = clean.Q(50)
    clean.REMOVED_FACES = ((11, 263, 12), (12, 263, 262))
    clean.ADDED_FACES = ((11, 262, 12), (11, 263, 262))
    clean.WALL_FACE = (11, 263, 262, 12)
    clean.REMOVED_EDGE = (12, 263)
    clean.ADDED_EDGE = (11, 262)
    clean.EVENT_FAMILY = {
        "edge:(12, 263):beta1": 1,
        "edge:(12, 263):beta2": 1,
        "edge:(12, 263):gram": 2,
        "support:f81:w262": 1,
        "support:f82:w11": 1,
    }
    clean.TARGET = "support:f81:w262"
    clean.EXPECTED_CERTIFICATE_VERDICT = "EXACT_POST_C17_TENTH_SAFE_FLIP_PASS"
    clean.VERIFIER_VERDICT = "INDEPENDENT_EXACT_POST_C17_TENTH_SAFE_FLIP_PASS"
    clean.main()


if __name__ == "__main__":
    main()
