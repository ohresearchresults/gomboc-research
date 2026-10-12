#!/usr/bin/env python3
"""Independent clean-engine verifier for the fourth safe flip."""
from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ENGINE_PATH = MAIN / "verify_safe_flip.py"
SPEC = importlib.util.spec_from_file_location("post_c17_clean_flip_engine_round3", ENGINE_PATH)
assert SPEC is not None and SPEC.loader is not None
clean = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(clean)


def main():
    round2 = MAIN / "post_flip_round2"
    clean.SOURCE = round2 / "far.csv"
    clean.CANDIDATE = HERE / "candidate.csv"
    clean.CERTIFICATE = HERE / "certificate.json"
    clean.OUTPUT = HERE / "verification.json"
    clean.PRE_FACES_PATH = round2 / "post_faces.json"
    clean.WALL_FACES_PATH = HERE / "wall_faces.json"
    clean.POST_FACES_PATH = HERE / "post_faces.json"
    clean.FAR_PARAMETER = clean.Q(100)
    clean.REMOVED_FACES = ((11, 262, 12), (11, 263, 262))
    clean.ADDED_FACES = ((11, 263, 12), (12, 263, 262))
    clean.WALL_FACE = (11, 263, 262, 12)
    clean.REMOVED_EDGE = (11, 262)
    clean.ADDED_EDGE = (12, 263)
    clean.EVENT_FAMILY = {
        "edge:(11, 262):beta1": 1,
        "edge:(11, 262):beta2": 1,
        "edge:(11, 262):gram": 2,
        "support:f55:w263": 1,
        "support:f62:w12": 1,
    }
    clean.TARGET = "support:f55:w263"
    clean.EXPECTED_CERTIFICATE_VERDICT = "EXACT_POST_C17_FOURTH_SAFE_FLIP_PASS"
    clean.VERIFIER_VERDICT = "INDEPENDENT_EXACT_POST_C17_FOURTH_SAFE_FLIP_PASS"
    clean.main()


if __name__ == "__main__":
    main()
