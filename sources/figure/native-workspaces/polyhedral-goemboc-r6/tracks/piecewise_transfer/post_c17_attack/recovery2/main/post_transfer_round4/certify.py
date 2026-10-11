#!/usr/bin/env python3
"""Exact certificate for the ninth post-C17 safe support flip."""
from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ENGINE_PATH = MAIN / "post_flip_round1" / "certify.py"
SPEC = importlib.util.spec_from_file_location(
    "post_c17_ninth_flip_certificate_engine", ENGINE_PATH
)
assert SPEC is not None and SPEC.loader is not None
engine = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(engine)


def main():
    previous = MAIN / "post_transfer_round3"
    engine.SOURCE = previous / "far.csv"
    engine.SOURCE_FACES = previous / "post_faces.json"
    engine.ENDPOINT = HERE / "candidate.csv"
    engine.PROPOSAL = HERE / "proposal.json"
    engine.SCAN = HERE / "first_event_scan.json"
    engine.CERTIFICATE = HERE / "certificate.json"
    engine.PRE_OUT = HERE / "pre.csv"
    engine.POST_OUT = HERE / "post.csv"
    engine.FAR_OUT = HERE / "far.csv"
    engine.WALL_FACES_OUT = HERE / "wall_faces.json"
    engine.POST_FACES_OUT = HERE / "post_faces.json"
    engine.CIRCUIT = (16, 54, 72, 15)
    engine.REMOVED_FACES = ((16, 15, 54), (54, 15, 72))
    engine.ADDED_FACES = ((16, 15, 72), (16, 72, 54))
    engine.WALL_FACE = (16, 15, 72, 54)
    engine.REMOVED_EDGE = (15, 54)
    engine.ADDED_EDGE = (16, 72)
    engine.TARGET = "support:f85:w72"
    engine.EVENT_MULTIPLICITY = {
        "edge:(15, 54):beta1": 1,
        "edge:(15, 54):beta2": 1,
        "edge:(15, 54):gram": 2,
        "support:f85:w72": 1,
        "support:f86:w16": 1,
    }
    engine.FAR_PARAMETER = engine.Q(11, 2)
    engine.EXPECTED_FIRST_CANDIDATE = "edge:(15, 54):beta1"
    engine.SUPPORT_WITNESSES = (72, 16)
    engine.CERTIFICATE_VERDICT = "EXACT_POST_C17_NINTH_SAFE_FLIP_PASS"
    engine.NEXT_ACTION = "Rebuild the complete chart from the ninth-flip FAR checkpoint."
    engine.main()


if __name__ == "__main__":
    main()
