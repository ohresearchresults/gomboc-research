#!/usr/bin/env python3
"""Exact certificate for the eighth post-C17 safe support flip."""
from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ENGINE_PATH = MAIN / "post_flip_round1" / "certify.py"
SPEC = importlib.util.spec_from_file_location(
    "post_c17_eighth_flip_certificate_engine", ENGINE_PATH
)
assert SPEC is not None and SPEC.loader is not None
engine = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(engine)


def main():
    previous = MAIN / "post_transfer_round2"
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
    engine.CIRCUIT = (12, 255, 261, 262)
    engine.REMOVED_FACES = ((12, 262, 255), (255, 262, 261))
    engine.ADDED_FACES = ((12, 262, 261), (12, 261, 255))
    engine.WALL_FACE = (12, 262, 261, 255)
    engine.REMOVED_EDGE = (255, 262)
    engine.ADDED_EDGE = (12, 261)
    engine.TARGET = "support:f55:w261"
    engine.EVENT_MULTIPLICITY = {
        "edge:(255, 262):beta1": 1,
        "edge:(255, 262):beta2": 1,
        "edge:(255, 262):gram": 2,
        "support:f55:w261": 1,
        "support:f61:w12": 1,
    }
    engine.FAR_PARAMETER = engine.Q(15, 2)
    engine.EXPECTED_FIRST_CANDIDATE = "edge:(255, 262):beta1"
    engine.SUPPORT_WITNESSES = (261, 12)
    engine.CERTIFICATE_VERDICT = "EXACT_POST_C17_EIGHTH_SAFE_FLIP_PASS"
    engine.NEXT_ACTION = "Rebuild the complete chart from the eighth-flip FAR checkpoint."
    engine.main()


if __name__ == "__main__":
    main()
