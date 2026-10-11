#!/usr/bin/env python3
"""Exact certificate for the sixth post-C17 safe support flip."""
from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ENGINE_PATH = MAIN / "post_flip_round1" / "certify.py"
SPEC = importlib.util.spec_from_file_location(
    "post_c17_sixth_flip_certificate_engine", ENGINE_PATH
)
assert SPEC is not None and SPEC.loader is not None
engine = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(engine)


def main():
    transfer = MAIN / "post_flip_round5"
    round4 = MAIN / "post_flip_round4"
    engine.SOURCE = transfer / "transfer_far.csv"
    engine.SOURCE_FACES = round4 / "post_faces.json"
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
    engine.REMOVED_FACES = ((16, 15, 72), (16, 72, 54))
    engine.ADDED_FACES = ((16, 15, 54), (54, 15, 72))
    engine.WALL_FACE = (16, 15, 72, 54)
    engine.REMOVED_EDGE = (16, 72)
    engine.ADDED_EDGE = (15, 54)
    engine.TARGET = "support:f63:w54"
    engine.EVENT_MULTIPLICITY = {
        "edge:(16, 72):beta1": 1,
        "edge:(16, 72):beta2": 1,
        "edge:(16, 72):gram": 2,
        "support:f63:w54": 1,
        "support:f82:w15": 1,
    }
    engine.FAR_PARAMETER = engine.Q(24)
    engine.EXPECTED_FIRST_CANDIDATE = "edge:(16, 72):beta1"
    engine.SUPPORT_WITNESSES = (54, 15)
    engine.CERTIFICATE_VERDICT = "EXACT_POST_C17_SIXTH_SAFE_FLIP_PASS"
    engine.NEXT_ACTION = (
        "Rebuild before the (255,262) support circuit near t=26.4292 in the "
        "(15,54)-diagonal cell."
    )
    engine.main()


if __name__ == "__main__":
    main()
