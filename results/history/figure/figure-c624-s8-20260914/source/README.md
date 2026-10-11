# Exact C624 stable-cap/RL contact constructions, separate arithmetic variants

Preferred new arithmetic candidate: COORD_CAP_RL_C624_STRONG_G8 (REPLAY object S8).
The run journal independently accepted COORD_CAP_RL_C624_INHERITED_G9 at
2026-09-14T02:27:09.018Z. It is a DIFFERENT generator; do not overwrite its identity.
S8 is an exact co-record with a smaller centred denominator, not C<624.
This source package by itself does not mutate the canonical run journal.

## Exact finite definition and acceptance

S8: exactly round STRONG_G14_GENERATOR.json controls to grid 10^8 using
round(Fraction(v*new_grid,old_grid)). Reconstruct dependent coordinates in the
specified plan using rational linear equations q dot p = 1. All 137 first rows
are physical support covectors. RECONSTRUCT.py returns integer halfspaces.
A constructs the full bounded intersection from all triples, B independently
clips every plane-pair line. They independently recover maximal face cycles,
312 genuine edges, volume/centroid, and all strict and weak equilibria. Their
complete normalized records must be identical. Subtract the actual filled-volume
centroid; this is the centred homogeneous solid. Ordinary density is any positive
constant. No point-mass or reference-centre model is used.

A third centred integer-tetrahedron integration checks 350 positive volumes,
zero first moments, and the same volume. measure.py certifies whole physical
primal and translated-polar positive escape trees. compare.py verifies that
collapsing parent construction edge 87--88 reproduces EVERY actual new maximal
face and true edge, not just an Euler count. Tetrahedron and weak-prism fixtures
are rejected by the acceptance gate. Assertions MUST stay enabled.

Exact reproduction uses CPython 3.13.5 and the standard library only:
python -B -S REPLAY.py --object S8 --out ../cold_S8 --stage ALL --coordinates
Expected terminal: COORD_STABLECAP_RL_C624_COMPLETE_EXACT_PASS S8 WINNER
Stage ALL requires a NEW output directory. It may instead be split into stages
A, B, MASS, DETAILS, FINISH, in that order. Pass --coordinates to DETAILS and FINISH.
All output byte counts and SHA-256 values are in EXPECTED.json.

Other finite objects: G14 and G10 are strict110/weak000 from the weaker numerical
repair; G9 is exact121/weak000 (PRESERVED_NONWINNER); G9P fixes that G9 by the exact
single integer update controls[168][0] += 1, and is strict110/weak000. G9P has
common centred denominator 51276 bits; S8 has 44770 bits. The canonical run's
separate INHERITED_G9 has 51085 bits. The earlier larger C626G8 has 43316 bits.
These are arithmetic comparisons, not proofs of minimal complexity or bit size.

The G14 and STRONG_G14 checkpoints here have SHA-256 3b6ae07ed211a6457d3e69fb3670c13f6fb5dc5bc9f41b75d43735361a19168a
and e13122d3ef125650d8be6e253be422e649730552984e9670eb682ce52ea62be2
respectively. The run's distinct INHERITED_G14 checkpoint has SHA-256
cfa90753ea7a681d2f040ba120830bc8811d9fbfe139cad638d91e4b210a3514.
STRONG_G14 itself is a frozen numerical checkpoint; S8 is the exactly audited endpoint.

## Complete discovery method

Immutable evidence parent: asg_RCec_cSHP9QT7MDzi-ldZ6Dy, SHA-256
e4b02b73abe4b9f212844982334fd28adf447de9a106e47e30a205829a4d33c4,
read completely cursor 0 -> 16000 -> 66000 -> eof. Only its actual BASIN69_96
minimal input and used helpers are copied here. Its complete 45-source capsule
remains in the immutable result. A Library JSON wrapper differed in bytes; the
75845-character base85 source capsule and 229874 decoded bytes matched both
immutable hashes exactly, and every decoded payload hash was checked.

combine.py adds auxiliary node178 = q16 intersect q71 intersect q94; q18 depends
on that node along axis2, with construction87~88. This adds the four-owner
[16,18,71,94] to the six-owner [71,94,109,116,119,126] and nine-owner stable-cap
[3,17,49,57,73,88,134,135,136] already present in the literal parent.
There are 315 free real coordinates, 177 vertices, 137 physical support planes.

Naive witnesses selected AFTER projecting the damaged seed can freeze a directed
cycle. For an edge i,j, the sum of the two opposite exit dot products is
-|p_i-p_j|^2, so both cannot be positive. More generally any positive exit arrow
strictly increases squared radius, hence no directed cycle is possible. The
successful methods inherit compatible complete primal and polar forests from
BASIN69_96 BEFORE the contraction, then remap around the merged vertex. The
physical own-volume centroid and its derivative are recomputed at every step.

repair_parent.py: goal5e-8, trust.03, 40 steps, 30-second overall guard,
QP tolerance2e-13, 8-second QP guard, maxsteps10000. Six accepted updates yielded
G14. repair_stronger.py: same seed and algorithm, goal1e-6 and QP tolerance2e-12;
eight accepted updates yielded STRONG_G14. Exact grid10^8 rounding of the latter
already passes, without a one-coordinate patch. S8P with zero delta is an alias,
not another construction. Full numerical source units, inputs, grids, rounding
and non-default parameters are included here; no optimizer execution is needed
for the exact proof.

Numerical reproposal dependencies: CPython3.13.5, NumPy2.3.5, SciPy1.17.0,
OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1; no randomized seed is used.
python -B REPROPOSE.py --out ../numerical_reproposal
Expected: C624_NUMERICAL_SOURCE_REPROPOSAL_IDENTICAL. Exact output hashes,
not numerical histories or time-dependent log bytes, define replay equality.

EXPERIMENTS.json records every declared finite numerical screen and parameter.
The failed naive and overconditioned numerical endpoints are preserved literally
in numerical_nonwinners/. Other coarse controls are exactly derived by rounding
the stated frozen checkpoint. G8 single-coordinate and MILP failures refer to
WEAKER G14's rounding, not STRONG_G14/S8 or the canonical journal's failed G8.
No finite failed numerical attempt is a geometric impossibility result.

The search did not enter C<32. The supplied V>=9/F>=9 applicability gate remains
separate; C=32 is not asserted as an attained or proved exact minimum here.
