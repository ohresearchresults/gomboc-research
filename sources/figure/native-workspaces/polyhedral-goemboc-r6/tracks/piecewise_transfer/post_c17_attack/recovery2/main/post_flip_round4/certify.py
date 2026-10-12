#!/usr/bin/env python3
"""Exact certificate for the fifth recovery2 safe support flip."""
from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROUND1_ENGINE = HERE.parent / "post_flip_round1" / "certify.py"
SPEC = importlib.util.spec_from_file_location(
    "post_c17_round5_certificate_engine", ROUND1_ENGINE
)
assert SPEC is not None and SPEC.loader is not None
engine = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(engine)


def main():
    round3 = HERE.parent / "post_flip_round3"
    engine.SOURCE = round3 / "far.csv"
    engine.SOURCE_FACES = round3 / "post_faces.json"
    engine.ENDPOINT = HERE / "candidate.csv"
    engine.PROPOSAL = HERE / "proposal.json"
    engine.SCAN = HERE / "first_event_scan.json"
    engine.CERTIFICATE = HERE / "certificate.json"
    engine.PRE_OUT = HERE / "pre.csv"
    engine.POST_OUT = HERE / "post.csv"
    engine.FAR_OUT = HERE / "far.csv"
    engine.WALL_FACES_OUT = HERE / "wall_faces.json"
    engine.POST_FACES_OUT = HERE / "post_faces.json"
    engine.CIRCUIT = (14, 73, 255, 13)
    engine.REMOVED_FACES = ((14, 13, 255), (14, 255, 73))
    engine.ADDED_FACES = ((14, 13, 73), (73, 13, 255))
    engine.WALL_FACE = (14, 13, 255, 73)
    engine.REMOVED_EDGE = (14, 255)
    engine.ADDED_EDGE = (13, 73)
    engine.TARGET = "support:f64:w73"
    engine.EVENT_MULTIPLICITY = {
        "edge:(14, 255):beta1": 1,
        "edge:(14, 255):beta2": 1,
        "edge:(14, 255):gram": 2,
        "support:f64:w73": 1,
        "support:f65:w13": 1,
    }
    engine.FAR_PARAMETER = engine.Q(12)
    engine.EXPECTED_FIRST_CANDIDATE = "edge:(14, 255):beta1"
    engine.SUPPORT_WITNESSES = (73, 13)
    engine.CERTIFICATE_VERDICT = "EXACT_POST_C17_FIFTH_SAFE_FLIP_PASS"
    engine.NEXT_ACTION = (
        "Rebuild before the linked (229,231) mechanics transfer near t=12.5411 "
        "in the (13,73)-diagonal cell."
    )
    engine.main()


if __name__ == "__main__":
    main()
