#!/usr/bin/env python3
"""Independent clean-engine verifier for the third safe flip."""
from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ENGINE_PATH = MAIN / "verify_safe_flip.py"
SPEC = importlib.util.spec_from_file_location("post_c17_clean_flip_engine_round2", ENGINE_PATH)
assert SPEC is not None and SPEC.loader is not None
clean = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(clean)


def main():
    round1 = MAIN / "post_flip_round1"
    clean.SOURCE = round1 / "far.csv"
    clean.CANDIDATE = HERE / "candidate.csv"
    clean.CERTIFICATE = HERE / "certificate.json"
    clean.OUTPUT = HERE / "verification.json"
    clean.PRE_FACES_PATH = round1 / "post_faces.json"
    clean.WALL_FACES_PATH = HERE / "wall_faces.json"
    clean.POST_FACES_PATH = HERE / "post_faces.json"
    clean.FAR_PARAMETER = clean.Q(8)
    clean.REMOVED_FACES = ((14, 73, 72), (14, 72, 15))
    clean.ADDED_FACES = ((14, 73, 15), (15, 73, 72))
    clean.WALL_FACE = (14, 73, 72, 15)
    clean.REMOVED_EDGE = (14, 72)
    clean.ADDED_EDGE = (15, 73)
    clean.EVENT_FAMILY = {
        "edge:(14, 72):beta1": 1,
        "edge:(14, 72):beta2": 1,
        "edge:(14, 72):gram": 2,
        "support:f66:w15": 1,
        "support:f67:w73": 1,
    }
    clean.TARGET = "support:f66:w15"
    clean.EXPECTED_CERTIFICATE_VERDICT = "EXACT_POST_C17_THIRD_SAFE_FLIP_PASS"
    clean.VERIFIER_VERDICT = "INDEPENDENT_EXACT_POST_C17_THIRD_SAFE_FLIP_PASS"
    clean.main()


if __name__ == "__main__":
    main()
