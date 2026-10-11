#!/usr/bin/env python3
"""Exact certificate for the thirteenth post-C17 safe support flip."""
from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ENGINE_PATH = MAIN / "post_flip_round1" / "certify.py"
SPEC = importlib.util.spec_from_file_location(
    "post_c17_thirteenth_flip_certificate_engine", ENGINE_PATH
)
assert SPEC is not None and SPEC.loader is not None
engine = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(engine)


def main():
    previous = MAIN / "post_transfer_round7"
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
    engine.CIRCUIT = (255, 256, 257, 258)
    engine.REMOVED_FACES = ((256, 258, 257), (255, 258, 256))
    engine.ADDED_FACES = ((255, 258, 257), (255, 257, 256))
    engine.WALL_FACE = (255, 258, 257, 256)
    engine.REMOVED_EDGE = (256, 258)
    engine.ADDED_EDGE = (255, 257)
    engine.TARGET = "support:f4:w255"
    engine.EVENT_MULTIPLICITY = {
        "edge:(256, 258):beta1": 1,
        "edge:(256, 258):beta2": 1,
        "edge:(256, 258):gram": 2,
        "support:f25:w257": 1,
        "support:f4:w255": 1,
    }
    engine.FAR_PARAMETER = engine.Q(30)
    engine.EXPECTED_FIRST_CANDIDATE = "edge:(256, 258):beta1"
    engine.SUPPORT_WITNESSES = (255, 257)
    engine.CERTIFICATE_VERDICT = "EXACT_POST_C17_THIRTEENTH_SAFE_FLIP_PASS"
    engine.NEXT_ACTION = "Rebuild from FAR 30 in the (255,257)-diagonal cell."
    engine.main()


if __name__ == "__main__":
    main()
