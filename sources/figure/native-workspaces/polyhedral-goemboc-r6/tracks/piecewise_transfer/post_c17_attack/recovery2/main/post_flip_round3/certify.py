#!/usr/bin/env python3
"""Exact certificate for the fourth recovery2 safe support flip."""
from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROUND1_ENGINE = HERE.parent / "post_flip_round1" / "certify.py"
SPEC = importlib.util.spec_from_file_location("post_c17_round4_certificate_engine", ROUND1_ENGINE)
assert SPEC is not None and SPEC.loader is not None
engine = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(engine)


def main():
    round2 = HERE.parent / "post_flip_round2"
    engine.SOURCE = round2 / "far.csv"
    engine.SOURCE_FACES = round2 / "post_faces.json"
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
    engine.REMOVED_FACES = ((11, 262, 12), (11, 263, 262))
    engine.ADDED_FACES = ((11, 263, 12), (12, 263, 262))
    engine.WALL_FACE = (11, 263, 262, 12)
    engine.REMOVED_EDGE = (11, 262)
    engine.ADDED_EDGE = (12, 263)
    engine.TARGET = "support:f55:w263"
    engine.EVENT_MULTIPLICITY = {
        "edge:(11, 262):beta1": 1,
        "edge:(11, 262):beta2": 1,
        "edge:(11, 262):gram": 2,
        "support:f55:w263": 1,
        "support:f62:w12": 1,
    }
    engine.FAR_PARAMETER = engine.Q(100)
    engine.EXPECTED_FIRST_CANDIDATE = "edge:(11, 262):beta1"
    engine.SUPPORT_WITNESSES = (263, 12)
    engine.CERTIFICATE_VERDICT = "EXACT_POST_C17_FOURTH_SAFE_FLIP_PASS"
    engine.NEXT_ACTION = "Rebuild before the linked face/edge birth near t=112.46 in the (12,263)-diagonal cell."
    engine.main()


if __name__ == "__main__":
    main()
