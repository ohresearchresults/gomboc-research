#!/usr/bin/env python3
"""Independent clean-engine verifier for the fifth safe flip."""
from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ENGINE_PATH = MAIN / "verify_safe_flip.py"
SPEC = importlib.util.spec_from_file_location(
    "post_c17_clean_flip_engine_round4", ENGINE_PATH
)
assert SPEC is not None and SPEC.loader is not None
clean = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(clean)


def main():
    round3 = MAIN / "post_flip_round3"
    clean.SOURCE = round3 / "far.csv"
    clean.CANDIDATE = HERE / "candidate.csv"
    clean.CERTIFICATE = HERE / "certificate.json"
    clean.OUTPUT = HERE / "verification.json"
    clean.PRE_FACES_PATH = round3 / "post_faces.json"
    clean.WALL_FACES_PATH = HERE / "wall_faces.json"
    clean.POST_FACES_PATH = HERE / "post_faces.json"
    clean.FAR_PARAMETER = clean.Q(12)
    clean.REMOVED_FACES = ((14, 13, 255), (14, 255, 73))
    clean.ADDED_FACES = ((14, 13, 73), (73, 13, 255))
    clean.WALL_FACE = (14, 13, 255, 73)
    clean.REMOVED_EDGE = (14, 255)
    clean.ADDED_EDGE = (13, 73)
    clean.EVENT_FAMILY = {
        "edge:(14, 255):beta1": 1,
        "edge:(14, 255):beta2": 1,
        "edge:(14, 255):gram": 2,
        "support:f64:w73": 1,
        "support:f65:w13": 1,
    }
    clean.TARGET = "support:f64:w73"
    clean.EXPECTED_CERTIFICATE_VERDICT = "EXACT_POST_C17_FIFTH_SAFE_FLIP_PASS"
    clean.VERIFIER_VERDICT = "INDEPENDENT_EXACT_POST_C17_FIFTH_SAFE_FLIP_PASS"
    clean.main()


if __name__ == "__main__":
    main()
