#!/usr/bin/env python3
"""Run the 27D actual-cell SLP with the round-eight alternate acute route.

The parent engine normally insists on the literal 19-edge long rail.  After
the {9,198,263,264} flip that edge list is no longer present, while the exact
positive-dot graph remains connected through 228-198-263-9-8.  This thin
entry point substitutes that true-edge route without changing any mechanical,
base, active-row, topology, short-rail, or fresh-hull check in the engine.

Every output endpoint must still be checked by
``verify_round8_alternate_acute_route.py`` or an equivalent exact audit; the
engine itself checks the route's true edges, not their positive-dot signs.
"""
from __future__ import annotations

import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import row54_combined_hard_slp as engine  # noqa: E402


engine.LONG_RAIL = [228, 198, 263, 9, 8]


if __name__ == "__main__":
    engine.main()
