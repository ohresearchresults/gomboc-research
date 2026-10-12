# figure-0125

AI research report · 2026-08-27 UTC

---

# Nimble Finch 54 — continued Fourier/Santaló finite-construction handoff

## Verdict

No finite homogeneous convex polyhedral Gömböc was certified in this continuation. I therefore do **not** present any generated body as the requested target.

The continuation materially strengthens the negative result. I extended the deterministic equilibrium-preserving Fourier refinement ladder through a literal 30,724-row dyadic level, independently reconstructed its Santaló translation and complete numerical mechanics, tested a different helical/Fourier-balanced support family, corrected a scale-dependent Santaló-verifier failure that had produced false winners, and searched determinant-one metric orbits of the resulting exactly centred low-complexity candidates.

The strongest finite endpoint is a 30,724-row polyhedron that is strict `(S,U,H)=(1,1,0)` at its construction centre but becomes `(11035,10333,21366)` after its polar is translated to the numerically isolated Santaló point. The tested refinement sequence therefore does not yet realize the desired premise that the Santaló correction eventually enters the open mechanical chamber.

## Reproducible continuation bundle

The principal artifact is the complete [continuation bundle](sandbox:/mnt/data/fourier_santalo_continuation_bundle.zip), with its [SHA-256 record](sandbox:/mnt/data/fourier_santalo_continuation_bundle.sha256).

It contains:

- all ten materialized exact-dyadic refinement levels;
- the deterministic generators and scan scripts;
- the Santaló solvers and equilibrium auditors;
- refinement logs and fitted scaling evidence;
- the independent reconstruction report and verifier;
- the helical candidates that initially appeared successful;
- the corrected, scale-invariant re-audits proving those candidates were false positives;
- the exact 4,324-row baseline generator and its existing Krawczyk/metric certificates.

## Deterministic refinement ladder

The continued sequence uses the prescribed smooth source

```text
R(theta,phi)^4 = 1 + 4 beta sin(theta) cos(phi-P(theta))
beta = 1/160
P(theta) = eta(theta) - (1/3) sin(3 eta(theta))
eta(theta) = (3 pi/2)(cos(theta)-cos(theta)^3/3)
```

with deterministic ring-and-fan parameters

```text
m approximately 0.3 nr
twist = 20.4/nr
gamma0 = 3/nr
gammaT = 3.6/nr
support profile = exp(kappa(1-2a/pi))
coordinate rounding scale = 2^-48
```

Every saved coordinate is a binary64 number and therefore has a literal exact-dyadic interpretation. Every listed level is strict `(1,1,0)` at its construction centre.

Materialized levels include:

- `nr=40`: [level file](sandbox:/mnt/data/continuation_work/refine_level_40_full.npz)
- `nr=60`: [level file](sandbox:/mnt/data/continuation_work/refine_level_60_full.npz)
- `nr=80`: [level file](sandbox:/mnt/data/continuation_work/refine_level_80_full.npz)
- `nr=100`: [level file](sandbox:/mnt/data/continuation_work/refine_level_100_full.npz)
- `nr=120`: [level file](sandbox:/mnt/data/continuation_work/refine_level_120_full.npz)
- `nr=160`: [level file](sandbox:/mnt/data/continuation_work/refine_level_160_full.npz)
- `nr=200`: [level file](sandbox:/mnt/data/continuation_work/refine_level_200.npz)
- `nr=240`: [level file](sandbox:/mnt/data/continuation_work/refine_level_240.npz)
- `nr=280`: [level file](sandbox:/mnt/data/continuation_work/refine_level_280_threshold.npz)
- `nr=320`: [level file](sandbox:/mnt/data/continuation_work/refine_level_320_threshold.npz)

### Level 200

```text
nr = 200
m = 60
number of Q rows = 12,004
kappa = 0.0244586181640625
raw class = (1,1,0)
raw stable margin = 0.0003452346382
raw centroid x = 0.0183445123264
Santaló x = -0.0183423266174
Santaló-centred class = (6357,6271,12626)
```

### Level 240

```text
nr = 240
m = 72
number of Q rows = 17,284
winner kappa = 0.021952311197916664
nearby lower kappa = 0.021947733561197915 gives raw (1,3,2)
raw stable margin = 0.0002522608086
raw centroid x = 0.0164646432710
Santaló x = -0.0164626602899
Santaló-centred class = (7911,7841,15750)
```

### Level 280

```text
nr = 280
m = 84
number of Q rows = 23,524
nonwinner kappa = 0.02020849609375 gives raw (1,3,2)
winner kappa = 0.020208984375000003 gives raw (1,1,0)
raw stable margin = 0.00019484296171
raw centroid x = 0.0151570786300
Santaló x = -0.0151552542059
Santaló-centred class = (9587,9219,18804)
```

The complete literal level is [refine_level_280_threshold.npz](sandbox:/mnt/data/continuation_work/refine_level_280_threshold.npz).

### Level 320 — strongest endpoint

```text
nr = 320
m = 96
number of Q rows = 30,724
kappa = 0.01895
raw class = (1,1,0)
raw stable margin = 0.00015674376561
raw centroid x = 0.0142128032985
Santaló point approximately
  (-0.0142111006834231,-6.58e-17,5.50e-16)
Santaló-centred class = (11035,10333,21366)
normalized centroid residual approximately 1e-15
```

At `kappa=0.0189`, immediately below the selected value, the raw class is `(1,5,4)`. Thus the construction-centre winner lies close to a genuine finite mechanical threshold, while its Santaló displacement is about ninety times the raw stable-face margin.

The complete literal level is [refine_level_320_threshold.npz](sandbox:/mnt/data/continuation_work/refine_level_320_threshold.npz).

## Independent reconstruction

I wrote a second verifier that does not call the primary equilibrium-audit implementation: [independent_refinement_verifier.py](sandbox:/mnt/data/continuation_work/independent_refinement_verifier.py).

It independently performs the following operations:

1. reconstructs the Q convex hull;
2. derives the polar vertices;
3. enumerates all hull edges;
4. audits raw stable faces, unstable vertices, and saddle edges;
5. computes directed tetrahedral volume and first moments;
6. solves the Santaló equations using the normalized centroid residual;
7. translates Q and independently audits the centred polar.

Its complete output is [independent_refinement_report.json](sandbox:/mnt/data/continuation_work/independent_refinement_report.json).

For level 280 it reproduces

```text
raw class = (1,1,0)
Santaló point =
  (-0.015155254205941838,1.46e-16,-2.01e-16)
centred class = (9587,9219,18804)
normalized centroid residual approximately 1e-16
```

For level 320 it reproduces

```text
raw class = (1,1,0)
Santaló point =
  (-0.014211100683423092,-6.58e-17,5.50e-16)
centred class = (11035,10333,21366)
normalized centroid residual approximately 1e-15
```

These independent results rule out a stale-feature or primary-classifier explanation for the large centred counts.

## Quantified obstruction in this refinement mechanism

The complete numerical ledger is [refinement_scaling_evidence.json](sandbox:/mnt/data/continuation_work/refinement_scaling_evidence.json).

Across all ten materialized levels, the following ratios are exceptionally rigid:

```text
||centroid of raw polar|| / kappa approximately 0.75002
||Santaló translation|| / kappa approximately 0.75002
```

Representative high-level quantities are

```text
nr=160: kappa*nr = 4.8000, stable_margin*nr^2 = 13.63
nr=200: kappa*nr = 4.8917, stable_margin*nr^2 = 13.81
nr=240: kappa*nr = 5.2686, stable_margin*nr^2 = 14.53
nr=280: kappa*nr = 5.6585, stable_margin*nr^2 = 15.28
nr=320: kappa*nr = 6.0640, stable_margin*nr^2 = 16.05
```

A log-log fit over the last five levels gives approximately

```text
kappa slope:                    -0.653
raw centroid/Santaló slope:     -0.653
raw stable-margin slope:        -1.758
```

These finite fits should not be promoted to an asymptotic theorem. They do, however, establish the decisive empirical mismatch for this particular sequence: its open mechanical margin shrinks much faster than its Santaló correction. The correction therefore moves farther outside the mechanical chamber when measured in units of the weakest strict margin, despite tending slowly toward zero in absolute coordinates.

This is stronger than the previous observation that the construction was mass-displaced. It identifies the failure of the tested refinement mechanism itself: the axial cumulative support profile produces an essentially first-order mass/Santaló response while its finite separator margin is closer to a second-order mesh quantity.

## Helical/Fourier-balanced alternative and verifier correction

I also tested a materially different support perturbation based on

```text
g(theta,phi) = sin(theta) cos(phi-P(theta))
f = -g
```

with nonlinear monotone transforms, axial mixing, phase shifts, ring/fan parameters, and exact dyadic coordinates.

Four randomized searches initially appeared to produce raw and Santaló-centred `(1,1,0)` bodies:

- [seed 1](sandbox:/mnt/data/continuation_work/helical_random/raw_seed1_it2415.npz)
- [seed 2](sandbox:/mnt/data/continuation_work/helical_random/raw_seed2_it3277.npz)
- [seed 3](sandbox:/mnt/data/continuation_work/helical_random/raw_seed3_it1953.npz)
- [seed 4](sandbox:/mnt/data/continuation_work/helical_random/raw_seed4_it758.npz)

They are **not** winners.

The old Newton stopping rule accepted `||M||<10^-12`, where `M` is the unnormalized first moment. These bodies had polar volumes between roughly `10^-13` and `10^-23`; consequently an absolute first-moment tolerance was almost vacuous. A tiny absolute `M` did not imply a small centroid `M/V`.

I implemented a corrected affine-whitened, line-searched Santaló solver that stops on the scale-invariant residual `||M||/V` and enforces a positive denominator margin: [robust_santalo.py](sandbox:/mnt/data/continuation_work/robust_santalo.py).

The corrected centred classes are

```text
seed 1: (2,3,3), minimum polar denominator 0.473619
seed 2: (2,4,4), minimum polar denominator 0.439319
seed 3: (3,2,3), minimum polar denominator 0.437747
seed 4: (2,2,2), minimum polar denominator 0.461658
```

The complete correction ledger is [helical_false_positive_correction.json](sandbox:/mnt/data/continuation_work/helical_false_positive_correction.json).

This is a reusable certification rule for all later work:

```text
Never accept a Santaló root using an absolute first-moment tolerance.
Use ||M||/V, enclose all polar denominators away from zero, and audit the translated body only after the normalized root is isolated.
```

## True-centred low-complexity and metric searches

After correcting the Santaló solver, roughly 450 low-count true-centred candidates were evaluated. The common classes were `(2,2,2)`, `(3,2,3)`, `(4,2,4)`, `(2,3,3)`, and larger Euler-compatible variants. No true-centred `(1,1,0)` body occurred.

Some `(2,2,2)` candidates had one stable primitive within about `8e-8` of a transfer wall, but their additional unstable and saddle features remained open at roughly `0.07–0.10`. They were therefore not hidden strict winners.

Two determinant-one SPD metric searches were then run:

- a centred candidate with 44 active Q rows: three million random metrics plus differential evolution;
- a centred candidate with only seven active Q vertices: five million random metrics plus differential evolution.

The first remained at best near score `-0.06687`, class `(2,3,3)`; the second remained near `-0.3219`, class `(2,4,4)` or adjacent cells. Saved metric checkpoints include

- [metric_helical_seed101.npz](sandbox:/mnt/data/continuation_work/metric_helical_seed101.npz)
- [metric_helical_seed102.npz](sandbox:/mnt/data/continuation_work/metric_helical_seed102.npz)

No open SPD chamber with `(1,1,0)` was found.

## Structured contour experiment

A level-set contour construction was also materialized with 20 longitudinal contours and 400 transverse samples per contour:

- [contour20_400.npz](sandbox:/mnt/data/continuation_work/contour20_400.npz)
- [contour20_400.log](sandbox:/mnt/data/continuation_work/contour20_400.log)

It has approximately 8,002 rows and centroid norm only `1.11e-5`, but its construction-centre class is

```text
(4132,4994,9124).
```

Thus fine transverse sampling alone does not supply the required complete common separators; coarse longitudinal normal-cone capture still creates thousands of equilibria. A larger `160 x 100` contour attempt did not complete and is not a materialized endpoint.

## Exact 4,324-row baseline retained

The earlier exact-cover artifacts remain the best exact/directed baseline for the complete finite machinery:

- [exact deterministic generator](sandbox:/mnt/data/exact_cover/generator.json)
- [Santaló Krawczyk certificate](sandbox:/mnt/data/exact_cover/santalo_krawczyk_certificate.json)
- [exact dyadic metric certificate](sandbox:/mnt/data/exact_cover/metric_A_dyadic_certificate.json)

The 4,324-row body is strict `(1,1,0)` at its construction centre. Its exactly centred/metric-audited fallback is `(2,2,2)`, not the target.

## Exactness and acceptance gaps

The continuation does not meet the requested final acceptance gate. In particular:

- the large refinement levels have literal exact-dyadic coordinates, but no outward exact full-incidence/Santaló certificate was completed for their centred forms;
- the Santaló roots for levels 280 and 320 are independently reproduced to normalized residuals near `10^-15`, but are not interval-Krawczyk boxes in the final high-dimensional certificate sense;
- the centred equilibrium counts are exhaustive numerical full-feature audits, not exact rational sign ledgers for tens of thousands of features;
- no positive coordinate perturbation box was proved for a centred `(1,1,0)` member because no such member was found;
- no final winner OBJ/STL exists;
- the supplied bundle is a reproducibility archive for finite nonwinners and the obstruction, not a Gömböc certificate.

## First exact or reproducible obstruction

For the continued sequence, the first obstruction is not merely a single circuit wall. It is the scale separation visible throughout the ladder:

1. A nonzero cumulative support bias is required to suppress the residual raw stable-saddle pairs.
2. That bias produces centroid and Santaló displacement approximately `0.75002 kappa`.
3. The construction-centre equilibrium margin shrinks substantially faster than `kappa` under refinement.
4. The Santaló correction therefore does not enter the raw mechanical chamber.
5. Independent reconstruction confirms that the translated polar contains thousands of actual equilibrium faces, vertices, and true edges rather than triangulation artifacts.

At the strongest level the numerical comparison is

```text
Santaló displacement norm approximately 1.42111e-2
raw weakest stable margin approximately 1.56744e-4
ratio approximately 90.7
centred class = (11035,10333,21366)
```

This invalidates the tested axial-profile refinement ladder as a route to a finite endpoint. It does **not** disprove the broader refinement-plus-Santaló strategy with a differently balanced finite separator field.

## Most useful continuation

The next construction should discard the one-dimensional cumulative axial support profile and solve a balanced local separator problem directly.

A productive generator would have the following structure:

1. Preserve dedicated stable and unstable patches of fixed physical angular size rather than shrinking them according to the same global profile as the noncritical cover.
2. Follow the smooth Fourier gradient field longitudinally and refine transversely only enough to certify a common separator for each complete maximal face and every full vertex/edge normal cone.
3. Assign local dyadic support offsets in separated blocks with zero degree-one/projective response, so their aggregate first-order Santaló displacement cancels instead of accumulating monotonically.
4. Treat three support coefficients as dependent variables solving the normalized Santaló equations at every finite level.
5. Enforce a positive polar-denominator box and use `||M||/V`, never absolute `||M||`, in every root test.
6. Enumerate the local circuit cells reached by the dependent moment correction and accept a level only when the isolated root lies strictly inside one fixed-incidence all-feature sign chamber.
7. Only then exactify the active H/V data, prove inactive separations and a perturbation box, and export the final OBJ/STL.

The strongest practical mathematical target is therefore a **balanced local Fourier-separator field with hard Santaló centering**, not further growth of the present axial ladder. The present artifacts provide the finite counterexample sequence, the corrected root machinery, and independent audit code needed to test that redesigned construction without repeating the verifier and scaling failures found here.
