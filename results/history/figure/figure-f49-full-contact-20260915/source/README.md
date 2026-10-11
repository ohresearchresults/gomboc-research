# F49_50 reference-chamber full-contact continuation: exact C622 nonwinners

## Status and identities

The accepted run record is still the distinct S8 COORD_CAP_RL_C624_STRONG_G8,
V177/E312/F137, own strict110/weak000. No new homogeneous Gömböc is claimed here.
All three principal bodies in this capsule have V177/E311/F136, C622. They have
strict110/weak000 about an explicitly provided rational interior reference g,
but not about their own filled-volume centroid c.

* seed: COORD_S8_F49_50_SWITCH_REF110_C622_G8, own (41,61,100).
* pc3: COORD_F49_50_PC3_REF110_C622_G14, own (42,61,101).
* slsqp3: COORD_F49_50_SLSQP3_REF110_C622_G14, own (65,76,139).

Weak counts are (0,0,0) in both centres for all three. The names denote the
literal checkpoint generators; they are not aliases of other C622 objects.
In particular these are NOT the canonical 10:29 radial-corrector point with
r=3.891772914946268e-5, reference floor near2e-7 and own (64,75,137), nor its
reference g=(-.0125336502350,.0062797755078,-.0088891805791). The independently
used local LM1 point r=3.891011257058487e-5, own numerical(63,72,133), is yet
another checkpoint. Do not merge those identities because their distances are close.

## Exact seed construction and source authority

inputs/S8/GENERATOR.json is the complete exact input, copied unchanged from
S8. Its SHA256 is bf9fdaf05231ceb11fba9fde10c8a638e664b52233b2da5cb11977b2f4ff27b2.
inputs/S8/FACES.json is an explicitly named projection of the exact S8 audit,
not a substitute or alias for the full S8 A.json. No originating sandbox is
needed to reconstruct the new bodies. Their independent exact hull audits
also establish all physical incidence without trusting the supplied cycles.

fusion.py replaces original support49 by the plane through original S8
raw-lex vertices23,38,69 and removes support50. The merged maximal cycle is
[23,31,44,64,69,38,27]. Original vertices27,31,44,64 move initially. In the
alternating contact generator, new49 uses original auxiliary nodes144,148,154;
original auxiliary147 remains on supports0/131 but is no longer a physical
vertex. This leaves315 free chart coordinates, one auxiliary null direction,
and314 sampled physical modes. Adding three reference coordinates gives317
physical augmented modes. These rank counts are floating diagnostics, not
formal interval certificates.

The seed reference is exactly [-12533688566502676,6279895492828624,
-8889061183282553]/10^18. The final reference is exactly
[-119473573074789,66210766571512,-72646944328917]/10^16.
Every other reference, generator, face cycle, free control, and plan is literal
in checkpoints. Dependent zero input controls are intentional: RECONSTRUCT
solves them exactly. The anchor is (0,0,1). Do not use the inherited Atlas.save
method: its int64 conversion can overflow; the included proposer save functions
instead use arbitrary-precision Python integers.

## Reusable method and finite scope

The first continuation preserves positive primal and centred-polar escape
witnesses at a variable reference, with all filled-volume derivatives computed
from the physical geometry. Its equations are x=P-g, n=q/(1-q dot g), and
r=c(u)-g. The corrected analytic Jacobians, preconditioner, predictor/corrector,
SLSQP and regularized least-squares variants are preserved as full runnable
source units, including all helpers and the exact input of every experiment.
RUNS.json supplies versions, all non-default parameters, seeds, rounding,
input checkpoints, commands, and actual finite termination scope.

Straight closure of the full residual vector made finite progress but became
slow. Permitting its direction to change in a soft constrained objective
reduced its norm much further. This is numerical continuation, not a global
exclusion and not an own-centroid equilibrium certificate. All SLSQP successes
in the summary mean retained positive-chamber checkpoints, not a solver report
of convergence: the recorded finite runs reached their iteration limits.
Interrupted experiments preserve only explicitly saved accepted states.

TANGENT_DIAGNOSTIC fixes197 selected reference outputs as EQUALITIES. The
remaining120-dimensional tangent slice has sampled mass singular values
[.030815663341961088,.02532227168765354,4.0940788318648624e-5]. Its full-closure
minimum-norm step would be large and violate other escape inequalities. This
is NOT the whole feasible inequality cone and NOT a proof that the contact
family cannot close. Three fixed-witness derivative tests, seed14094950 and
step1e-7, passed the preserved tolerances. No below32 body search was made.

## Exact tests and the volume correction

For each principal body, check_A and check_B independently enumerate the full
true maximal complex and all own-centroid face/vertex/four-edge equilibrium
primitives. Their complete JSON outputs agree bytewise. CENSUS_AT independently
classifies all features at the provided rational g, including weak cases and
all four edge tests. It does not infer H from Euler. It also compares face
stability with unstable centred-polar vertices. This is one extra all-feature
reference checker over an independently twice-enumerated physical hull, not
an assertion of two independent reference-checker implementations.

centred_mass.py performs a third exact integration over350 positive tetrahedra,
with a different face fan and the actual own centroid as origin. It confirms
zero first moments and the same ordinary volume. STATS uses exact rational
and integer comparisons only.

The distances lie in these strict-upper grid intervals (denominator10^16):
seed [990183459201,990183459202),
pc3 [652910712328,652910712329),
slsqp3 [367971833150,367971833151).
The final/seed distance ratio lies in
[3716198546144190,3716198546144191)/10^16.

A preliminary claim of increasing volume applied to an earlier checkpoint,
NOT to the final slsqp3. Exact scalar verification caught that overextension.
The final/seed volume ratio is
[9986806929400666,9986806929400667)/10^16, a decrease of about0.132%.
The correct scale-independent comparison also passes: for d=||c-g|| and V=volume,
(d_final/V_final^(1/3))/(d_seed/V_seed^(1/3)) < 3/8.
It is proved without irrational arithmetic by cubing the squared distances:
(D_final/D_seed)^3*(V_seed/V_final)^2 < (3/8)^6.
Thus the improvement exceeds62.5% even after scale normalization, but D_final
is strictly positive and the own-centroid equilibrium census is worse.
No moment closure, winner, or impossibility theorem follows.

Arithmetic costs also worsened. Maximum reduced raw-vertex bits / integer-plane
bits / raw-centroid bits are seed440/216/44827, pc3 822/385/83077,
slsqp3 838/392/83403. Common centred denominator bits are44881,83164,83499.
These sizes are compared for the final physical objects, not merely the small
input grids.

## Recovery and verification

Run from this source directory with an initially absent output path:

    python -B -S REPLAY.py --out NEW_EXACT_OUTPUT

Assertions must be enabled. Exact replay uses CPython3.13.5 standard library
only; numerical libraries are not imported. The replay verifies the complete
SOURCE_MANIFEST, reconstructs every frozen contact checkpoint, independently
re-audits the three principal bodies with both checkers, rechecks references,
performs all three third integrations and exact scale comparisons, and compares
every deterministic output file with EXPECTED.json. Its terminal marker is:

    COORD_F49_50_C622_REFERENCE_CHAMBER_EXACT_NONWINNERS_PASS

Numerical reproposal uses NumPy2.3.5, SciPy1.17.0 and single BLAS/OMP threads.
Start from the exact included checkpoints and execute the literal commands in
RUNS.json. Floating optimization subject to elapsed-time budgets is not promised
bitwise reproducible; exact frozen input recovery is deterministic.

SOURCE_MANIFEST.json hashes every source/input file except itself. EXPECTED.json
contains filenames, byte counts and SHA256 of the deterministically reproduced
outputs. Compressed source transport is a UTF-8 JSON dictionary encoded as
base64(LZMA(bytes)); its whole decoded and encoded hashes are provided outside
this directory. Hashes identify bytes, not a substitute for the literal capsule.

## Continuation / persistence boundary

These are preserved non-record constructions and methods, not a new accepted
endpoint. The current coordinator interface exposed only read/state/wait tools,
not canonical append or dispatch. The literal source capsule must be retained
in the coordinator output and reconciled into the canonical journal when write
access exists. A supplementary download link alone is not durable run state.
Do not discard the independently reconstructible accepted S8/C624 parent.
