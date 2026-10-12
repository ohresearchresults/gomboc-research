# C96 independent research log

## Contract and baseline

All writes are confined to the assigned temp directory. No other research runs,
runtime, sources, or canonical journal have been altered. The original C96
generator and all three exact auditors were read completely. A fresh baseline
run reproduced all five published hashes and strict own211/weak000 with
V25/E48/F25. See `baseline-check/`.

## Reading and tactic choice

The current synthesis and C282/C138/C96 source entries were read, together with
the early-method digest. The literal earlier-material attachment is predominantly
recovery code/payload; its first spans are encoded material and are not treated
as having been scientifically decoded. Historical negative search statements are
not impossibility proofs. The applicable lessons are: use the true volume centroid;
test complete feature stars; broad shape change may be needed; a good affine score
or moment closure alone does not prove the intended census.

Chosen first experiments: a small independent numerical hull/mass/census screen;
finite affine/projective pyramid changes, then nonpyramidal additions/deformations
and direct whole-body shape searches. Positive proposals require the complete
unchanged exact A/B/third-mass audit before any own110 claim.

## Exact tilted disk/slab result

The complete literal 2026-09-15T20:43:37 C182 disk/slab capsule was read,
including proof and code. The theorem was then evaluated on C96, independently
reconstructing and auditing C96 first. `python3 -B -S work/shape_certificate.py`
passes. At the exact own centroid the central disk normal to (89,229,-10) of
radius 45400 lies strictly inside the body, which lies strictly inside the slab
of halfwidth 4100. Thus every affine image with Euclidean singular-value condition
number strictly below 454/41 has at least two strict stable maximal facets.
This is stronger than the original-plane direction's numerical ratio 7.0271.
It does not exclude more distorted affine transforms, projective transforms,
non-affine geometry changes, or general pyramids.

## Early basin-barrier objective recovered and used

The full literal entries 2026-09-05T20:07:37.692Z and 20:17:52.808Z were read.
The complete spherical-cap graph objective avoids a false descent caused by
splitting nearly identical facet poles. Independently implemented in geometry.py.
For C96, B(Q)=0.11674996203913103, B(V)=0.0 in the numerical chart;
the independent saddle-energy minus larger stable-face-energy calculation gives
0.11674996203913113. Numerical agreement is an objective consistency check,
not a replacement equilibrium proof. Full-vertex descent can split the 24-gon
and can change all vertices and the actual volume centroid.

## Completed constructive search milestones

- Apex: 7,524 evaluations; affine: 87,559; projective: 105,136;
  cubic transverse deformation: 174,591; two added vertices plus affine:
  111,500. These are bounded numerical searches; none produced own110.
- Ten unrestricted whole-vertex cap-barrier descents: 216,980 evaluations.
  Their lower scores came with extra equilibria and are not accepted solutions.
- Four SLSQP attempts preserving U1 witness inequalities: 119,465 evaluations.
  Larger low-cost endpoints violated constraints and were rejected.
- 320 physical polar-chain cuts with actual mass closure were evaluated. Some
  produce own121 or own132 numerically; none is own110. Small moment residual
  alone was never treated as a success.
- 24 bounded alternating primal-addition/polar-cut runs, each at most 25 stages
  and with an explicit complexity stop, produced no numerical own110.

## New exact retained bodies

1. `polar-exact/`: C96, V25/E48/F25, own121/weak000. This is the polar of the
   original C96 about its exact own centre, then classified at the polar's own
   separately recomputed uniform centroid. Exact A/B and third mass agree.
2. `flow25-exact/`: C138, V25/E69/F46, own211/weak000. A finite lifted-face,
   full-coordinate U1-preserving deformation, integer grid 10^8; exact A/B and
   third mass agree. Not the historical C138 parent.
3. `pyramid-101-exact/`: C80, V21/E40/F21, own211/weak000. Obtained by 101
   accepted/search iterations of planar-base full-coordinate continuation,
   selecting its 21 numerically exposed input points, then integer rounding and
   independent exact re-hull. Every accepted count is from the new exact audit.
   This is the best exact one-pair descendant here; it is not a Gömböc.
4. `pyramid-final-exact/`: C76, V20/E38/F20, own312/weak000. A smaller but
   mechanically worse descendant after 700 iterations. Exact A/B/mass agree.

Analytic active-hull volume-centroid, facet-pole, and cap-barrier derivatives were
implemented and compared to independent finite directional differences. Twelve
directions on the retained lifted endpoint had maximum absolute error below
8e-7 with step 1e-9. Finite steps always reconstruct the actual convex hull and
recompute its own centroid. Linear predictions are not used as acceptance.

## Limits and failed hypotheses

The full floating loading-point MILP (246 variables, 461 constraints) returned
optimum common strict margin zero after 990 nodes. This is numerical evidence
only, not an exact all-centres impossibility certificate. A tempting simpler
right-pyramid proof does NOT apply: the exact apex projection violates one
nonbase supporting plane (raw facet24), while lying inside the other 23.

The cap-barrier objective can reward a flatter pyramid while retaining a pair.
Its reduction is not a monotone measure of distance to a Gömböc. The current
continuation therefore also tests finite volume/thickness changes while guarding
against new stable equilibria. Neither small scores, successful mass closure,
nor the count improvement C96 to C80 is represented as own110.

## Restart and completed continuation

The application restart left no live research process. `thick-basin-flow/BEST.json`
had accepted step980, one step beyond the flushed SEARCH history. The continuation
resumed from precisely that saved geometry, inherited trust and original volume
reference, with a separate `RESUMPTION.json`, and completed steps981--1199 without
duplicating the first981 iterations. Final numerical S11/U1, normalized stable
barrier0.16982063493569774, centred radius ratio0.2500006312715055. No own110.

The finite lift plus 53 guarded thickening attempts produced `rounder25-exact/`:
C138,25/69/46,own211,weak000. Its exact centred inradius/circumradius exceeds1/10,
whereas baseline C96 and the smaller C80 are below1/40. Twelve literal noncritical
cap insertions and further homogeneous deformations produced `capped-bulk-exact/`:
C174,31/87/58,own817,weak000, with exact centred radius ratio greater than1/4.
Its added seven stable/saddle pairs are genuine defects, not discarded tiny bars.

## Free support normals, conditioning and polar-side trials

The literal journal passage around lines9535--9590 was read. A new independently
implemented physical-support chart fixes the unique-U root contact plane while
releasing other normals. Physical vertices are support-plane intersections;
their true volume and first moments, not the support hull's centroid, are used.
Active-chart analytic derivatives include the physical centroid derivative.
Directional tests on C96, the rounder seed, and the own polar agreed to below
4e-7 absolute objective derivative error. Every finite accepted step rebuilds
and classifies the body; numerical merging remains only screening.

The initial C96 support run lowered the bar but exhausted its U-exclusion margin.
A separate max-min conditioning run restored that minimum numerical cosine from
about1e-9 to0.000990142454881399, using a bounded0.02 increase in the normalized
barrier. Its rounded support definition is exactly verified in
`support-conditioned-exact/`: C138,46/69/25,own211,weak000. A floor mismatch in the
first constrained continuation was corrected explicitly; subsequent runs enforce
the same reserve in the LP and the true finite-step check. Corrected continuation
still stalled without cancellation. No failed or infeasible endpoint was promoted.

The own-centred polar branch instead preserved S1 and minimized physical unstable
persistence. Both preserved-apex and nonpyramidal root charts were tried, including
explicit guards against new unstable vertices. `support-polar-exact/` is a genuine
smaller nonwinner: C88,23/44/23,own121,weak000. Its support table is on grid10^12.
All nine retained exact bodies, including the original baseline, have no weak
features and zero face, vertex-max or true-edge primitive zero counts.

## Exact all-reference-centre exclusion for the unchanged C96 geometry

`loading_certificate.py` used LPs solely to propose a finite covering tree.
For an oriented face edge i->j, set e=p_j-p_i and k=n cross e. The face-foot
side condition is k dot g > k dot p_i. Therefore excluding a stable-or-weak face
requires some edge with k dot g < k dot p_i. Add a common strict slack t>0 to
every selected inequality and to all interior supporting inequalities. Enumerate
each of25 possible surviving faces; at every branch, split on ALL edges of one
other face. A leaf is closed only by nonnegative rational multipliers whose sum
of left coefficients is (0,0,0,1) and whose weighted right side is <=0.

The completed tree has2293 nodes,1698 leaves, maximum depth10. Of the1698 rational
dual bounds,462 are strictly negative; the others are exactly zero. Independent
standard-library-only `loading_verify.py` recomputes every integer inequality,
checks coverage and every rational dual identity, and passes. The proof is stored
both as the full search tree and a651-node DAG of exact row-basis hints. The latter
is15266bytes SHA256f75b5187e8c5110945f91308a905d0719b748b97555739ee04d01292625d677d.
The verifier solves those tiny rational systems itself; no optimizer is needed.

Conclusion: for this FIXED C96 shape, every interior reference point has at least
two stable-or-weak maximal facets. In particular, changing density or choosing
a different interior reference cannot produce nondegenerate S1 on this shape.
This does NOT exclude changing geometry, general pyramids, or arbitrary affine
images. The independent disk/slab result covers the stated affine condition bound.

## Exact reference110 on the C80 descendant, explicitly not own110

The same bounded loading search returned10 S1 candidates for the C80 descendant.
All10 screened as reference110. At the literal integer reference
g=(7695683,168054,-75622586), `reference_certificate.py` exactly checks S1/U1/H0,
weak000, all primitive signs nonzero, by paired face/vertex/edge formulas. The
retained reference stable face is13 and unstable vertex14 in the exact raw order.
This g is NOT the uniform centroid. The exact physical first moment about g is
nonzero and is included in the certificate. Thus C80 remains own211, not a Gömböc.
The reference shift is about0.58446 of the maximum absolute coordinate scale.

This gives a real contrast: deformation from C96 to C80 opened a reference110
region, but did not place the actual homogeneous centroid there. The remaining
task is genuine shape/mass co-design, not free recentring. The corresponding
rounder/thick loading trees were incomplete or contained reference proposals;
they are NOT exclusion certificates.

Broad physical cuts of the C80 seed were then actually tested with one and two
planes plus two anisotropic scale parameters. Each case used4 seeded differential
evolution runs with unstable-bar weights1,10,100,1000 and at most180 generations.
The runs completed10395 and29880 actual candidate evaluations, respectively.
They produced no numerical own110 and often collapsed to smaller222/233 bodies;
these low objective values are failures, not approaching-success evidence.

## Scope and remaining task

No homogeneous own110 body has been found at any count. The accepted C622 record
is unchanged. All numerical checkpoints, search configurations and useful failures
are retained; exact reconstruction needs no floating optimizer. The most useful
seeds are C80/own211 for count and its reference110-region geometry, and the
C138/own211 radius>1/10 body for genuine three-dimensional thickness. Closing the
stable/saddle pair with the actual filled-volume centroid remains unresolved.
