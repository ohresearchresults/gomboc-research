#!/usr/bin/env python3
"""Exact certificate for the fourteenth post-C17 safe support flip."""
from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ENGINE_PATH = MAIN / "post_flip_round1" / "certify.py"
SPEC = importlib.util.spec_from_file_location(
    "post_c17_fourteenth_flip_certificate_engine", ENGINE_PATH
)
assert SPEC is not None and SPEC.loader is not None
engine = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(engine)


def main():
    previous = MAIN / "post_transfer_round8"
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
    engine.CIRCUIT = (1, 2, 54, 88)
    engine.REMOVED_FACES = ((1, 88, 2), (1, 54, 88))
    engine.ADDED_FACES = ((2, 54, 88), (2, 1, 54))
    engine.WALL_FACE = (1, 54, 88, 2)
    engine.REMOVED_EDGE = (1, 88)
    engine.ADDED_EDGE = (2, 54)
    engine.TARGET = "support:f60:w54"
    engine.EVENT_MULTIPLICITY = {
        "edge:(1, 88):beta1": 1,
        "edge:(1, 88):beta2": 1,
        "edge:(1, 88):gram": 2,
        "support:f60:w54": 1,
        "support:f61:w2": 1,
    }
    engine.FAR_PARAMETER = engine.Q(13)
    engine.EXPECTED_FIRST_CANDIDATE = "edge:(1, 88):beta1"
    engine.SUPPORT_WITNESSES = (54, 2)
    engine.CERTIFICATE_VERDICT = "EXACT_POST_C17_FOURTEENTH_SAFE_FLIP_PASS"
    engine.NEXT_ACTION = "Rebuild before the next (11,262) event above t=13.361."
    engine.main()


if __name__ == "__main__":
    main()
