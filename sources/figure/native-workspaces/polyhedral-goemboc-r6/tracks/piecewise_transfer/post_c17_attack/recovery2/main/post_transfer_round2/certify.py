#!/usr/bin/env python3
"""Exact certificate for the seventh post-C17 safe support flip."""
from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ENGINE_PATH = MAIN / "post_flip_round1" / "certify.py"
SPEC = importlib.util.spec_from_file_location(
    "post_c17_seventh_flip_certificate_engine", ENGINE_PATH
)
assert SPEC is not None and SPEC.loader is not None
engine = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(engine)


def main():
    previous = MAIN / "post_transfer_round1"
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
    engine.CIRCUIT = (14, 15, 72, 73)
    engine.REMOVED_FACES = ((14, 73, 15), (15, 73, 72))
    engine.ADDED_FACES = ((14, 73, 72), (14, 72, 15))
    engine.WALL_FACE = (14, 73, 72, 15)
    engine.REMOVED_EDGE = (15, 73)
    engine.ADDED_EDGE = (14, 72)
    engine.TARGET = "support:f83:w72"
    engine.EVENT_MULTIPLICITY = {
        "edge:(15, 73):beta1": 1,
        "edge:(15, 73):beta2": 1,
        "edge:(15, 73):gram": 2,
        "support:f83:w72": 1,
        "support:f84:w14": 1,
    }
    engine.FAR_PARAMETER = engine.Q(10)
    engine.EXPECTED_FIRST_CANDIDATE = "edge:(15, 73):beta1"
    engine.SUPPORT_WITNESSES = (72, 14)
    engine.CERTIFICATE_VERDICT = "EXACT_POST_C17_SEVENTH_SAFE_FLIP_PASS"
    engine.NEXT_ACTION = (
        "Rebuild before the (15,54) support circuit near t=10.10705 in the "
        "restored (14,72)-diagonal cell."
    )
    engine.main()


if __name__ == "__main__":
    main()
