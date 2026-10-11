#!/usr/bin/env python3
"""Exact certificate for the fifteenth post-C17 safe support flip."""
from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ENGINE_PATH = MAIN / "post_flip_round1" / "certify.py"
SPEC = importlib.util.spec_from_file_location(
    "post_c17_fifteenth_flip_certificate_engine", ENGINE_PATH
)
assert SPEC is not None and SPEC.loader is not None
engine = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(engine)


def main():
    previous = MAIN / "post_transfer_round9"
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
    engine.CIRCUIT = (0, 16, 54, 72)
    engine.REMOVED_FACES = ((0, 16, 54), (16, 72, 54))
    engine.ADDED_FACES = ((0, 72, 54), (0, 16, 72))
    engine.WALL_FACE = (0, 16, 72, 54)
    engine.REMOVED_EDGE = (16, 54)
    engine.ADDED_EDGE = (0, 72)
    engine.TARGET = "support:f74:w72"
    engine.EVENT_MULTIPLICITY = {
        "edge:(16, 54):beta1": 1,
        "edge:(16, 54):beta2": 1,
        "edge:(16, 54):gram": 2,
        "support:f74:w72": 1,
        "support:f81:w0": 1,
    }
    engine.FAR_PARAMETER = engine.Q(26)
    engine.EXPECTED_FIRST_CANDIDATE = "edge:(16, 54):beta1"
    engine.SUPPORT_WITNESSES = (72, 0)
    engine.CERTIFICATE_VERDICT = "EXACT_POST_C17_FIFTEENTH_SAFE_FLIP_PASS"
    engine.NEXT_ACTION = (
        "Rebuild before the (12,261) support circuit above t=26.7216."
    )
    engine.main()


if __name__ == "__main__":
    main()
