#!/usr/bin/env python3
"""Exact certificate for the nineteenth post-C17 safe support flip."""
from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ENGINE_PATH = MAIN / "post_flip_round1" / "certify.py"
SPEC = importlib.util.spec_from_file_location(
    "post_c17_nineteenth_flip_certificate_engine", ENGINE_PATH
)
assert SPEC is not None and SPEC.loader is not None
engine = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(engine)


def main():
    previous = MAIN / "post_transfer_round13"
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
    engine.CIRCUIT = (11, 12, 255, 261)
    engine.REMOVED_FACES = ((12, 261, 255), (11, 261, 12))
    engine.ADDED_FACES = ((11, 261, 255), (11, 255, 12))
    engine.WALL_FACE = (11, 261, 255, 12)
    engine.REMOVED_EDGE = (12, 261)
    engine.ADDED_EDGE = (11, 255)
    engine.TARGET = "support:f78:w11"
    engine.EVENT_MULTIPLICITY = {
        "edge:(12, 261):beta1": 1,
        "edge:(12, 261):beta2": 1,
        "edge:(12, 261):gram": 2,
        "support:f78:w11": 1,
        "support:f79:w255": 1,
    }
    engine.FAR_PARAMETER = engine.Q(23, 2)
    engine.EXPECTED_FIRST_CANDIDATE = "edge:(12, 261):beta1"
    engine.SUPPORT_WITNESSES = (11, 255)
    engine.CERTIFICATE_VERDICT = "EXACT_POST_C17_NINETEENTH_SAFE_FLIP_PASS"
    engine.NEXT_ACTION = "Rebuild before the next support event above t=11.949."
    engine.main()


if __name__ == "__main__":
    main()
