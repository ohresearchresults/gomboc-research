#!/usr/bin/env python3
"""Independent clean-engine verifier for the sixth post-C17 safe flip."""
from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ENGINE_PATH = MAIN / "verify_safe_flip.py"
SPEC = importlib.util.spec_from_file_location(
    "post_c17_clean_sixth_flip_engine", ENGINE_PATH
)
assert SPEC is not None and SPEC.loader is not None
clean = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(clean)


def main():
    transfer = MAIN / "post_flip_round5"
    round4 = MAIN / "post_flip_round4"
    clean.SOURCE = transfer / "transfer_far.csv"
    clean.CANDIDATE = HERE / "candidate.csv"
    clean.CERTIFICATE = HERE / "certificate.json"
    clean.OUTPUT = HERE / "verification.json"
    clean.PRE_FACES_PATH = round4 / "post_faces.json"
    clean.WALL_FACES_PATH = HERE / "wall_faces.json"
    clean.POST_FACES_PATH = HERE / "post_faces.json"
    clean.FAR_PARAMETER = clean.Q(24)
    clean.REMOVED_FACES = ((16, 15, 72), (16, 72, 54))
    clean.ADDED_FACES = ((16, 15, 54), (54, 15, 72))
    clean.WALL_FACE = (16, 15, 72, 54)
    clean.REMOVED_EDGE = (16, 72)
    clean.ADDED_EDGE = (15, 54)
    clean.EVENT_FAMILY = {
        "edge:(16, 72):beta1": 1,
        "edge:(16, 72):beta2": 1,
        "edge:(16, 72):gram": 2,
        "support:f63:w54": 1,
        "support:f82:w15": 1,
    }
    clean.TARGET = "support:f63:w54"
    clean.EXPECTED_CERTIFICATE_VERDICT = "EXACT_POST_C17_SIXTH_SAFE_FLIP_PASS"
    clean.VERIFIER_VERDICT = "INDEPENDENT_EXACT_POST_C17_SIXTH_SAFE_FLIP_PASS"
    clean.main()


if __name__ == "__main__":
    main()
