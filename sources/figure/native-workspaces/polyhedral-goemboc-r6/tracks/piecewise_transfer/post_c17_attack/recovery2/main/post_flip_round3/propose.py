#!/usr/bin/env python3
"""Fresh descent proposal after the third safe flip."""
from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROUND1_ENGINE = HERE.parent / "post_flip_round1" / "propose.py"
SPEC = importlib.util.spec_from_file_location("post_c17_round3_proposer_engine", ROUND1_ENGINE)
assert SPEC is not None and SPEC.loader is not None
engine = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(engine)


def main():
    round2 = HERE.parent / "post_flip_round2"
    engine.SOURCE = round2 / "far.csv"
    engine.FACES_PATH = round2 / "post_faces.json"
    engine.SOURCE_CERTIFICATE = round2 / "certificate.json"
    engine.CHART_OUT = HERE / "chart.json"
    engine.OUTPUT = HERE / "proposal.json"
    engine.ENDPOINT = HERE / "candidate.csv"
    engine.EXPECTED_SOURCE_CERTIFICATE_VERDICT = "EXACT_POST_C17_THIRD_SAFE_FLIP_PASS"
    engine.main()


if __name__ == "__main__":
    main()
