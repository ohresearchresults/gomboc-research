#!/usr/bin/env python3
"""Independent clean-engine verifier for the ninth safe flip."""
from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ENGINE_PATH = MAIN / "verify_safe_flip.py"
SPEC = importlib.util.spec_from_file_location(
    "post_c17_clean_ninth_flip_engine", ENGINE_PATH
)
assert SPEC is not None and SPEC.loader is not None
clean = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(clean)


def main():
    previous = MAIN / "post_transfer_round3"
    clean.SOURCE = previous / "far.csv"
    clean.CANDIDATE = HERE / "candidate.csv"
    clean.CERTIFICATE = HERE / "certificate.json"
    clean.OUTPUT = HERE / "verification.json"
    clean.PRE_FACES_PATH = previous / "post_faces.json"
    clean.WALL_FACES_PATH = HERE / "wall_faces.json"
    clean.POST_FACES_PATH = HERE / "post_faces.json"
    clean.FAR_PARAMETER = clean.Q(11, 2)
    clean.REMOVED_FACES = ((16, 15, 54), (54, 15, 72))
    clean.ADDED_FACES = ((16, 15, 72), (16, 72, 54))
    clean.WALL_FACE = (16, 15, 72, 54)
    clean.REMOVED_EDGE = (15, 54)
    clean.ADDED_EDGE = (16, 72)
    clean.EVENT_FAMILY = {
        "edge:(15, 54):beta1": 1,
        "edge:(15, 54):beta2": 1,
        "edge:(15, 54):gram": 2,
        "support:f85:w72": 1,
        "support:f86:w16": 1,
    }
    clean.TARGET = "support:f85:w72"
    clean.EXPECTED_CERTIFICATE_VERDICT = "EXACT_POST_C17_NINTH_SAFE_FLIP_PASS"
    clean.VERIFIER_VERDICT = "INDEPENDENT_EXACT_POST_C17_NINTH_SAFE_FLIP_PASS"
    clean.main()


if __name__ == "__main__":
    main()
