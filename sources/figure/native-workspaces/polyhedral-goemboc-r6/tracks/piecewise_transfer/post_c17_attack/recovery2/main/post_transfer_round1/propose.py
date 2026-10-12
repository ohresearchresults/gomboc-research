#!/usr/bin/env python3
"""Fresh descent proposal after the first post-C17 mechanics transfer."""
from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ENGINE_PATH = MAIN / "post_flip_round1" / "propose.py"
SPEC = importlib.util.spec_from_file_location(
    "post_c17_transfer_round1_proposer_engine", ENGINE_PATH
)
assert SPEC is not None and SPEC.loader is not None
engine = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(engine)


def main():
    transfer = MAIN / "post_flip_round5"
    round4 = MAIN / "post_flip_round4"
    engine.SOURCE = transfer / "transfer_far.csv"
    engine.FACES_PATH = round4 / "post_faces.json"
    engine.SOURCE_CERTIFICATE = transfer / "transfer_certificate.json"
    engine.CHART_OUT = HERE / "chart.json"
    engine.OUTPUT = HERE / "proposal.json"
    engine.ENDPOINT = HERE / "candidate.csv"
    engine.EXPECTED_SOURCE_CERTIFICATE_VERDICT = (
        "EXACT_POST_C17_FIRST_MECHANICS_TRANSFER_PASS"
    )
    engine.main()


if __name__ == "__main__":
    main()
