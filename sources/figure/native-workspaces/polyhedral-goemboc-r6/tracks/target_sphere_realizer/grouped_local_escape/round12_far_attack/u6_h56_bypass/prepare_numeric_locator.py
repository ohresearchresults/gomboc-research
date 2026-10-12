#!/usr/bin/env python3
"""Write a binary64 locator copy of the exact t=9/4 pre-wall node."""
from __future__ import annotations

import csv
from fractions import Fraction as Q
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
EXACT_DIR = ROOT / "tracks/target_sphere_realizer/grouped_local_escape/rigorous_null_bypass"
sys.path.insert(0, str(EXACT_DIR))

import grouped_exact as gx  # noqa: E402


PRE = HERE.parent / "exact_event_chain_pre.csv"
FAR = HERE.parent / "exact_event_chain_far.csv"
OUTPUT = HERE / "numeric_pre_locator.csv"
PARAMETER = Q(9, 4)


pre = gx.ex.read_rows(PRE)
far = gx.ex.read_rows(FAR)
points = gx.evaluate_path(gx.planar_morph(pre, far), PARAMETER)
with OUTPUT.open("w", newline="") as output:
    writer = csv.writer(output)
    writer.writerow(("source_id", "x", "y", "z"))
    for label in sorted(points):
        writer.writerow(
            (
                label,
                *(format(float(value), ".17g") for value in points[label]),
            )
        )
