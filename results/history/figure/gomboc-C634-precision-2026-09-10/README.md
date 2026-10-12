# C634 precision variants — 10 September 2026

## Completed local check

GRID8_MIP6 was reconstructed from the literal delta and locally replayed with
both supplied exact auditors. Both returned V182/E317/F137, strict110, weak000;
both complete A/B outputs matched the author's SHA-256
`b14f8204ebab71ae30b6cae50a51070db8190f21a0e86103dadbd09c40714cd9`.
Transcript: [LOCAL_REPLAY.log](C634_GRID8_MIP6_COORD/LOCAL_REPLAY.log).
Local description confirms plane/raw-coordinate/centroid sizes211/433/42913bits.
GRID9's generator was authenticated, but its mathematical replay was not run
locally in this monitoring pass. The rank certificate was not locally replayed.

Two new definitions were preserved from the completed coordinator handoff:
`C634_GRID9_COORD` and `C634_GRID8_MIP6_COORD`. Both are reported to retain
V182/E317/F137, strict(1,1,0), weak(0,0,0), so this is an arithmetic-size
improvement, not a lower mechanical-complexity record.

`RECONSTRUCT.py` implements the complete literal delta against the authenticated
C634_SOC parent: exact ties-to-even rounding and six specified integer corrections
for GRID8. Both reconstructed generator byte counts and SHA-256 values matched
the coordinator's originals locally. The two original supplied exact checkers
and reconstruction code were copied from the preserved parent capsule.

Author-reported maximum bit lengths (not decimal places):

| Variant | Integer plane coefficients | Raw coordinate numerator/denominator | Centroid numerator/denominator |
| --- | ---: | ---: | ---: |
| Original C634_SOC | 335 | 706 | 68320 |
| GRID9 | 245 | 512 | 49874 |
| GRID8_MIP6 | 211 | 433 | 42913 |

Final centered coordinates are exact differences p-g; raw coordinate size is
not their denominator bound. Some mechanical margins decrease, so all variants
and the original must be retained. These margins are not manufacturing tolerances.

The full literal handoff is saved at
`../research-results-2026-09-09/figure-precision-rank-handoff-20260910-0753.json`.
It includes the exact derivative/minor recipe for a claimed rank316 mechanical
Jacobian certificate, plus failed grid7 and conditioning experiments. That rank
is local to the specified parameterization; it does not obstruct C632 globally.

Preservation boundary: the supplementary 86-file archive and new modular-rank
implementation remain sandbox-linked, not downloaded here. The two figure
definitions themselves are fully reconstructed and authenticated. A local
endpoint replay, when completed, is recorded separately; newly generated
FROZEN_OUTPUTS.json is a local output manifest, not an independently retrieved
author pin set.
