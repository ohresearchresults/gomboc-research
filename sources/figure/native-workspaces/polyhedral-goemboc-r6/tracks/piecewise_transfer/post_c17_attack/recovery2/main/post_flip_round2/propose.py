#!/usr/bin/env python3
"""Fresh descent proposal after the second safe flip."""
from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROUND1 = HERE.parent / "post_flip_round1"
ENGINE_PATH = ROUND1 / "propose.py"
SPEC = importlib.util.spec_from_file_location("post_c17_round_proposer_engine", ENGINE_PATH)
assert SPEC is not None and SPEC.loader is not None
engine = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(engine)


def main():
    engine.SOURCE = ROUND1 / "far.csv"
    engine.FACES_PATH = ROUND1 / "post_faces.json"
    engine.SOURCE_CERTIFICATE = ROUND1 / "certificate.json"
    engine.CHART_OUT = HERE / "chart.json"
    engine.OUTPUT = HERE / "proposal.json"
    engine.ENDPOINT = HERE / "candidate.csv"
    engine.EXPECTED_SOURCE_CERTIFICATE_VERDICT = "EXACT_POST_C17_SECOND_SAFE_FLIP_PASS"
    engine.main()


if __name__ == "__main__":
    main()
