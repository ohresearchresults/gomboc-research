#!/usr/bin/env python3
"""Exact certificate for the tenth post-C17 safe support flip."""
from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ENGINE_PATH = MAIN / "post_flip_round1" / "certify.py"
SPEC = importlib.util.spec_from_file_location(
    "post_c17_tenth_flip_certificate_engine", ENGINE_PATH
)
assert SPEC is not None and SPEC.loader is not None
engine = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(engine)


def main():
    previous = MAIN / "post_transfer_round4"
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
    engine.CIRCUIT = (11, 12, 262, 263)
    engine.REMOVED_FACES = ((11, 263, 12), (12, 263, 262))
    engine.ADDED_FACES = ((11, 262, 12), (11, 263, 262))
    engine.WALL_FACE = (11, 263, 262, 12)
    engine.REMOVED_EDGE = (12, 263)
    engine.ADDED_EDGE = (11, 262)
    engine.TARGET = "support:f81:w262"
    engine.EVENT_MULTIPLICITY = {
        "edge:(12, 263):beta1": 1,
        "edge:(12, 263):beta2": 1,
        "edge:(12, 263):gram": 2,
        "support:f81:w262": 1,
        "support:f82:w11": 1,
    }
    engine.FAR_PARAMETER = engine.Q(50)
    engine.EXPECTED_FIRST_CANDIDATE = "edge:(12, 263):beta1"
    engine.SUPPORT_WITNESSES = (262, 11)
    engine.CERTIFICATE_VERDICT = "EXACT_POST_C17_TENTH_SAFE_FLIP_PASS"
    engine.NEXT_ACTION = (
        "Rebuild before the (256,258) event near t=63.7852 from the tenth-flip FAR."
    )
    engine.main()


if __name__ == "__main__":
    main()
