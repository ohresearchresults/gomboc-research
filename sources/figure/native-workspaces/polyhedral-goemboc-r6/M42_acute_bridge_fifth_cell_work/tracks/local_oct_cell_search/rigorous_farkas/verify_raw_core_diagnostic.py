#!/usr/bin/env python3
"""Verify that raw sign-primitives do not reproduce the normalized core dual."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--diagnostic", type=Path, default=HERE / "core_beta_exact.json")
    args = ap.parse_args()
    data = json.load(args.diagnostic.open())
    checks = {
        "raw_certificate_absent": data["certificate_pass"] is False,
        "all_163_rows_present": data["feature_count"] == 163,
        "normalized_dual_minimum_positive": data["float_dual_objective"] > 0,
    }
    assert all(checks.values()), checks
    print("CORE RAW-PRIMITIVE DIAGNOSTIC PASS")


if __name__ == "__main__":
    main()
