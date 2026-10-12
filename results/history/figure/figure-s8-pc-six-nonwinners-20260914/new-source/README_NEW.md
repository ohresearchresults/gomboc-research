# S8 finite-deletion and predictor-corrector research capsule

These are preserved NONWINNERS, not a new Gomboc or a proof of nonexistence.
Canonical strict-own110 threshold remains C624. No C<32 search was performed.

## Required already-durable input
Restore the complete 30-file COORD_CAP_RL_C624_STRONG_G8 source capsule, journal
Recovery capsule parts1/6..6/6 ending2026-09-14T03:09:37.015Z, into ./source.
That normalized base85 has59100chars SHA256
e3c07742531ebe37a1a3332748807c7154f5d7a9c669b57bb78612041dbd1c00;
decoded JSON170010bytes SHA256
44319c99762df191373664c4e89bbeb7fb70db771c7c38e0a19e4e0ea2645fd3.
This is an exact prior journal dependency, not an external download requirement.
REPLAY.sources() checks its complete manifest before and after exact work.

## Exact definitions and evidence
DEL99,DEL117,DEL84 are explicit single-H-row deletions AFTER reconstructing all
137 supports of S8. RECONSTRUCT ignores active_ids; never omit the explicit
selection. Keep n_supports=137 and anchor137; active face labels are positions
in ACTIVE_IDS.json, not unshifted original support IDs.
CONTACT120 is the complete S8 contact stratum described in REPLAY_NEW.definition:
rescale every original integer control by10000 to grid10^12; append mixed
point179, contact group[101,102,120,121], solve179 from101/102/121 in axes0,1,2,
then solve support120 axis0 from179. This changes physical geometry; it is not
an approximation of the old body. No omitted free controls.
PC3 is the frozen DEL99_PC3/GENERATOR.json, and CONTACT_RPC is the frozen
CONTACT120_RPC1/GENERATOR.json. These define physical bodies at their own
exact filled-volume centroids, not at the old centre or at an optimized point.
Each of these six objects has two independently implemented full exact audits,
identical complete outputs, full true-edge weak/strict tests, and third exact
centred integer tetrahedral mass integration. All six are own121/weak000.
The six golden full-output metadata sets are in EXACT_EXPECTED.json.

## Cold exact replay (stdlib only)
For each OBJECT in DEL99 DEL117 DEL84 CONTACT120 PC3 CONTACT_RPC:
  python -B -S REPLAY_NEW.py OBJECT fresh-OBJECT A
  python -B -S REPLAY_NEW.py OBJECT fresh-OBJECT B
  python -B -S REPLAY_NEW.py OBJECT fresh-OBJECT MASS
  python -B -S REPLAY_NEW.py OBJECT fresh-OBJECT FINISH
Do not disable assertions. The finish marker is
S8_PC_SOURCE_ONLY_EXACT_COLD_NONWINNER_PASS OBJECT.
A.json and B.json carry complete rational raw vertices, own centroid/moments,
maximal face cycles, genuine edges and every equilibrium classification.
For complete centred coordinate tables one may run the unchanged source/export.py;
its legacy C624-named marker is just the export code's label, not this body's C.
Interpret every centred coordinate as raw rational vertex minus raw_centroid.

## Numerical method and its scope
Python3.13.5, NumPy2.3.5, SciPy1.17.0. Set OPENBLAS_NUM_THREADS=1 and
OMP_NUM_THREADS=1. Exact acceptance needs neither NumPy nor SciPy.
Full sources of every material new method are included. active_repair.py patches
only active physical support indexing in the hash-checked prior Atlas; the
original contact plan and anchor remain. forest_repair.py replaces the defective
widest-only rooted forest by additive squared-negative-cost shortest paths.
S8 DEL99 has exactly172 vertices with one positive adjacent exit, one with two,
and two with none. Thus most positive-route choices really are forced.
Legacy L2 and L1 methods do not certify success. The 80-step widest L2 endpoint
DEL99_REPAIR has numerical class90/93/181. DEL99_HOM1 has frozen-grid10^8 class
9/12/19 despite positivity at its unrounded iterates: rounding must be checked.
The single minnorm_step NUMERICAL report is an unrounded proposal report only.
All NUMERICAL.json files are discovery records, never exact acceptance reports.

predictor_corrector.py preserves per-identity floors within a phase, uses the
actual filled COM and its analytic derivative, removes SVD null columns, then
solves minimum-geometry-norm linear inequalities for a finite bad-exit increment.
Nonlinear correctors restore good exits and geometry before accepting a step.
A good finite endpoint is not a proof that its entire connecting segment has no
births. There is no interval-certified no-birth homotopy here.
The CONTACT120_RELAX phase explicitly replaces all identity floors by10^-7;
it is a changed objective, not silently decaying floors on witness changes.
Continuation files preserve exact incoming controls, topology, identity floors,
bad/good membership and the next numerical gain. The output grid is10^12.
Minimum-norm proposal solver is the already-durable source/parent/mechanism/
minnorm_qp.py, included via the required S8 source capsule. Its wall-time budget
can affect proposal reproducibility across machines; frozen rational endpoints
are authoritative and cold exact replay is deterministic.

## Actual proposal batches
All commands use the root containing this capsule and the prior ./source.
Initial exact input preparation: python -B -S setup_deletions.py; then run
source/check_A.py DEL99/raw.json DEL99/A.json. CONTACT120 analogously uses
setup_contact.py and its exact A auditor. The exact replay can produce all such
reference reports without loading any old audited output.
DEL99_REPAIR: active_repair.py DEL99 DEL99_REPAIR 80 1e-6 .01 1e-6.
DEL99_HARD3: forest_repair.py DEL99 DEL99_HARD3 --mode hardgood --steps1
--goal1e-7 --trust.01 (supply a space between option and value).
DEL99_QP1: minnorm_step.py DEL99 .0001 DEL99_QP1.
DEL99_HOM1: homotopy_repair.py DEL99 DEL99_HOM1 --steps25 --gain.001
--output-grid100000000, with all other defaults; no nonlinear correctors.
DEL99_PC1: predictor_corrector.py DEL99 DEL99_PC1 --steps3 --gain.001.
DEL99_PC2: same program DEL99_PC1 DEL99_PC2 --steps15 --gain.001;
execution was cut during its fourth iteration; only the three saved completed
iterations are claimed. Its frozen checkpoint is fully included.
DEL99_PC3: same program DEL99_PC2 DEL99_PC3 --steps2 --max-gain.0004
--correctors5. The incoming continuation gain .0016 is read before the cap is
applied at the end of a successful iteration; do not silently pre-cap it.
CONTACT120_PC1: same program CONTACT120 CONTACT120_PC1 --steps3 --gain.0002
--max-gain.0004.
CONTACT120_PC2: same program CONTACT120_PC1 CONTACT120_PC2 --steps10
--gain.0002 --max-gain.0004.
CONTACT120_PC3: same program CONTACT120_PC2 CONTACT120_PC3 --steps12
--max-gain.002; execution cut during iteration12, only11 saved iterations.
CONTACT120_RELAX: exact copy of PC3's generator and reference topology; replace
CONTINUATION.floors by all10^-7 and next_gain by.0004; retain good membership.
CONTACT120_RPC1: same program CONTACT120_RELAX CONTACT120_RPC1 --steps5
--max-gain.001 --correctors5. Every other parameter equals the saved source
argparse default or METHOD.json. No hidden randomness or seeds are used.
Two preliminary long hard-good runs were cut before final reporting; they are
not claimed as completed experiments or promoted endpoints.

## Labels and arithmetic
Continuation TOPOLOGY.json uses inherited vertex labels. The exact full audit
uses freshly lexicographically ordered rational vertices. EXACT_LABEL_MAP.json
records a bijection by full owner sets; every oriented maximal-face cycle was
checked under that bijection. Do not transfer raw vertex numbers without it.
PC3 has exact U[95,145],H[[145,146]],C618, common centred denominator69963bits.
CONTACT_RPC has exact U[95,163],H[[163,165]],C622, common denominator73055bits;
its inherited problematic label162 became exact label163. Both have stable3.
Unmodified DEL99/DEL117 denominators44408/44415bits; DEL84 has44522bits;
CONTACT120 has46207bits. Numerical barrier improvements are not C improvements.
The final C618 bad exit is about-0.02904594619 versus-0.03507345700 initially;
the C622 final worse selected exit is about-0.02553933930 versus-0.04112030527.
These are scoped numerical findings, not exact clearance bounds or exclusions.
