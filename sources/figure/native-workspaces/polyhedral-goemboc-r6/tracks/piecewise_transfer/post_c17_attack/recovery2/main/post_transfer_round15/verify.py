#!/usr/bin/env python3
"""Independent clean-engine verifier for the twentieth safe flip."""
from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ENGINE_PATH = MAIN / "verify_safe_flip.py"
SPEC = importlib.util.spec_from_file_location(
    "post_c17_clean_twentieth_flip_engine", ENGINE_PATH
)
assert SPEC is not None and SPEC.loader is not None
clean = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(clean)


def main():
    previous = MAIN / "post_transfer_round14"
    clean.SOURCE = previous / "far.csv"
    clean.CANDIDATE = HERE / "candidate.csv"
    clean.CERTIFICATE = HERE / "certificate.json"
    clean.OUTPUT = HERE / "verification.json"
    clean.PRE_FACES_PATH = previous / "post_faces.json"
    clean.WALL_FACES_PATH = HERE / "wall_faces.json"
    clean.POST_FACES_PATH = HERE / "post_faces.json"
    clean.FAR_PARAMETER = clean.Q(213, 20)
    clean.REMOVED_FACES = ((11, 263, 261), (261, 263, 262))
    clean.ADDED_FACES = ((11, 263, 262), (11, 262, 261))
    clean.WALL_FACE = (11, 263, 262, 261)
    clean.REMOVED_EDGE = (261, 263)
    clean.ADDED_EDGE = (11, 262)
    clean.EVENT_FAMILY = {
        "edge:(261, 263):beta1": 1,
        "edge:(261, 263):beta2": 1,
        "edge:(261, 263):gram": 2,
        "support:f85:w262": 1,
        "support:f86:w11": 1,
    }
    clean.TARGET = "support:f85:w262"
    clean.EXPECTED_CERTIFICATE_VERDICT = "EXACT_POST_C17_TWENTIETH_SAFE_FLIP_PASS"
    clean.VERIFIER_VERDICT = "INDEPENDENT_EXACT_POST_C17_TWENTIETH_SAFE_FLIP_PASS"
    clean.main()


if __name__ == "__main__":
    main()
