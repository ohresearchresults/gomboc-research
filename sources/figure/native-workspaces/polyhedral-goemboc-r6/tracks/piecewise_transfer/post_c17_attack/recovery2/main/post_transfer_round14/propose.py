#!/usr/bin/env python3
"""Fresh descent proposal after the eighteenth post-C17 safe flip."""
from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
MAIN = HERE.parent
ENGINE_PATH = MAIN / "post_flip_round1" / "propose.py"
SPEC = importlib.util.spec_from_file_location(
    "post_c17_transfer_round14_proposer_engine", ENGINE_PATH
)
assert SPEC is not None and SPEC.loader is not None
engine = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(engine)


def main():
    previous = MAIN / "post_transfer_round13"
    engine.SOURCE = previous / "far.csv"
    engine.FACES_PATH = previous / "post_faces.json"
    engine.SOURCE_CERTIFICATE = previous / "certificate.json"
    engine.CHART_OUT = HERE / "chart.json"
    engine.OUTPUT = HERE / "proposal.json"
    engine.ENDPOINT = HERE / "candidate.csv"
    engine.EXPECTED_SOURCE_CERTIFICATE_VERDICT = (
        "EXACT_POST_C17_EIGHTEENTH_SAFE_FLIP_PASS"
    )
    engine.main()


if __name__ == "__main__":
    main()
