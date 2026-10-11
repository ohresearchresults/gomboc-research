#!/usr/bin/env python3
"""Independent clean-engine verifier for the second safe flip."""
from __future__ import annotations

import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
sys.path.insert(0, str(MAIN))

import verify_safe_flip as clean  # noqa: E402


def main():
    clean.SOURCE = MAIN / "safe_flip_far.csv"
    clean.CANDIDATE = HERE / "candidate.csv"
    clean.CERTIFICATE = HERE / "certificate.json"
    clean.OUTPUT = HERE / "verification.json"
    clean.PRE_FACES_PATH = MAIN / "safe_flip_post_faces.json"
    clean.WALL_FACES_PATH = HERE / "wall_faces.json"
    clean.POST_FACES_PATH = HERE / "post_faces.json"
    clean.FAR_PARAMETER = clean.Q(16)
    clean.REMOVED_FACES = ((3, 237, 4), (3, 88, 237))
    clean.ADDED_FACES = ((3, 88, 4), (4, 88, 237))
    clean.WALL_FACE = (3, 88, 237, 4)
    clean.REMOVED_EDGE = (3, 237)
    clean.ADDED_EDGE = (4, 88)
    clean.EVENT_FAMILY = {
        "edge:(3, 237):beta1": 1,
        "edge:(3, 237):beta2": 1,
        "edge:(3, 237):gram": 2,
        "support:f71:w88": 1,
        "support:f72:w4": 1,
    }
    clean.TARGET = "support:f71:w88"
    clean.EXPECTED_CERTIFICATE_VERDICT = "EXACT_POST_C17_SECOND_SAFE_FLIP_PASS"
    clean.VERIFIER_VERDICT = "INDEPENDENT_EXACT_POST_C17_SECOND_SAFE_FLIP_PASS"
    clean.main()


if __name__ == "__main__":
    main()
