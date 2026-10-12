# figure-0043

AI research report · 2026-08-23 UTC

---

# Independent theorem audit: the claimed explicit construction has a fatal mixed-feature gap

## Verdict

The claimed smooth-to-polyhedral construction is **not certified**. I found a concrete fatal gap in the proof step that passes from inequalities for individual support planes or individual Thales-chain links to the assertion that **every mixed face, true edge, and vertex** of the final polyhedron is non-equilibrium.

That implication is false without an additional common-separator or full-normal-cone theorem. I constructed an exact rational 16-vertex prism whose **true uniform-volume centroid is exactly the origin** and for which:

- both facets incident to a selected edge pass the claimed style of one-normal exclusion inequality with margin greater than `2^-106`;
- their affine normal slopes differ by only `2^-51 < 2^-48`;
- neither facet is stable;
- nevertheless their common true edge is a strict saddle equilibrium.

Thus the parallel argument does not establish a homogeneous polyhedral Gömböc. This invalidates the supplied **proof/certificate**, not the possibility that a strengthened construction based on the same smooth seed could eventually work.

## 1. Where the proof fails

The materialized effective note first derives a cellwise support estimate and then states, without a branch-complete derivation, that the same estimate and strong monotonicity force all active slopes at a face, edge, or vertex into one tiny ball; from this it concludes that the facet calculation applies simultaneously to every feature. It then uses a one-normal scalar inequality at the apex transition and says that this excludes every other facet, edge, and vertex, before concluding `S=1,U=1,H=0`.

The finite exact audit proposed afterward would in principle be the right test—enumerate the actual face lattice, compute the exact centroid, and test every face, vertex, and true edge—but it was not run. The accompanying lazy builder takes the certified supports as inputs, leaves exact triple intersection as `NotImplementedError`, and publishes no active halfspace list or face lattice.

A separate quantitative dossier in the same project states the mathematically correct weaker conclusion: an explicit Thales link count only controls the links themselves; the convexity and transition-facet signs after gluing remain instance-specific. Its proposed final pipeline explicitly requires tests for every cap edge, transition facet, transition vertex, and adaptive middle-band cell.

The original research transcript had already isolated exactly these unresolved obligations: construct the patch, audit every face and vertex, restore the centroid, rationalize, and repeat the mechanics in exact arithmetic.

## 2. Exact scale-matched counterexample

Set

\[
s=2^{-52},\qquad x_1=1-\frac{s^2}{2},\qquad y_1=\frac{s}{2}.
\]

Take the centrally symmetric octagon

\[
(1,0),(x_1,y_1),(0,1),(-x_1,y_1),(-1,0),(-x_1,-y_1),(0,-1),(x_1,-y_1)
\]

in cyclic order and extrude it through `-1 <= z <= 1`. Exact rational reconstruction gives

\[
(V,E,F)=(16,24,10),\qquad c(P)=(0,0,0).
\]

Consider the vertical edge over `(1,0)`. Its incident side planes, after positive rescaling, are

\[
x+s y=1,\qquad x-s y=1.
\]

### Individual facets pass the claimed style of test

In the affine normal chart the two slopes are `v=+s` and `v=-s`. At the common edge tangent coordinate `y=0`, each one-normal residual is

\[
\left(\frac{v}{1+v^2}-0\right)v
=\frac{s^2}{1+s^2}>2^{-105}>2^{-106}.
\]

Their slope diameter is

\[
2s=2^{-51}<2^{-48}.
\]

The perpendicular foot of the origin on either side plane lies beyond the short boundary edge at exact parameter

\[
\frac{2}{1+s^2}>1,
\]

so neither incident rectangle is stable. The physical projection-exclusion distance is greater than `s/4=2^-54`.

### The mixed edge is still a strict saddle

The perpendicular foot on the vertical edge is its midpoint

\[
q=(1,0,0),\qquad t=\frac12.
\]

For the two incident outward normals

\[
n_+=(1,s,0),\qquad n_-=(1,-s,0),
\]

we have the exact positive-cone identity

\[
q=\frac12n_++\frac12n_-.
\]

Therefore `q` lies in the relative interior of the edge and in the strict interior of its normal cone. The edge is a nondegenerate saddle equilibrium.

This is the exact failure mode: a facetwise calculation uses a different test direction for each normal. Those inequalities are not preserved when incident normal rays are convex-combined. A mixed feature requires either a direct full normal-cone exclusion or **one common linear separator** valid for the whole active set.

The counterexample is not a floating-point stress test. Two independent standard-library verifiers recompute its exact centroid, topology, facet projections, edge parameter, cone coefficients, and strict inequalities.

## 3. Why the Thales spiral does not close the gap

Lángi's Lemma 3 proves that distance decreases along each link of a suitable planar polygonal chain. In the actual existence proof, that local fact is not treated as sufficient. For the saddle patch, Lángi analyzes the mixed intersection as the minimum of two graph functions and then truncates any remaining supporting plane that carries an equilibrium. For the unstable patch, the whole rotated mixed boundary is treated. In Step 3, the remaining compact boundary is separated from the compact family of **all** potentially radial supporting planes before a finite cover is selected.

Lángi's theorem therefore supports existence, but it does not justify replacing those mixed-feature arguments by linkwise monotonicity or per-facet residuals. The theorem itself is qualitative and proves that a centered polyhedron with prescribed equilibrium counts exists; it does not publish the claimed finite list.

An exact gluing experiment elsewhere in this project demonstrates that this distinction is operationally real: every local successor inequality of a rational corridor was strict, yet the actual convex hull deleted intended points, introduced bridge faces, and created four new stable-saddle pairs.

## 4. Polarity and centroid transfer audit

The fatal defect is **not** polarity or the scalar centroid estimate.

### Fixed-origin polarity

For a convex body `P` containing the origin, a nondegenerate equilibrium in a `k`-face maps under polarity to a nondegenerate equilibrium in the dual `(2-k)`-face. Hence, relative to the same origin,

\[
\text{stable face}\leftrightarrow\text{unstable vertex},\qquad
\text{saddle edge}\leftrightarrow\text{saddle edge}.
\]

This duality is exact but reference-point specific. It says nothing about the true uniform centroid until a complete reference-point stability radius is proved.

### Hausdorff and centroid constants

Using the shared values `delta=2^-300` and the conservative seed bounds

\[
\frac{24}{25}B\subset K\subset\frac{26}{25}B,
\]

exact rational arithmetic gives, conditionally on `K subset P subset K+delta B`,

\[
\|c(P)\|<(1+t)\frac{26}{25}((1+t)^3-1)<2^{-298},
\qquad t=\frac{25}{24}2^{-300}.
\]

This is much stronger than the claimed `2^-160`. The corresponding polar Hausdorff amplification is below `2^-299`.

If `2^-106` were a genuine minimum **reference-point displacement radius** over every actual face, vertex, and true edge branch, then a centroid shift below `2^-160` would be safe by the factor `2^-54`. But a margin over sampled normals or individual facets is not such a radius—the exact prism has individual residuals above `2^-106` and still has a mixed saddle.

### Complexity scale

A cube-surface rational normal net at `D=2^304` contains exactly

\[
24D^2+2=24\cdot2^{608}+2<2^{613}
\]

normals. Thus a total bound below `2^616` is arithmetically plausible after adding the collar and spiral. It is not, however, evidence that the mechanics of every active feature have been certified.

## 5. Corrected delicate exponent

The materialized positive-cap estimate has the form

\[
2^{-13}|v|^2,
\qquad |v|\ge2^{-83}.
\]

Its minimum is

\[
2^{-179},
\]

not `2^-96` as stated.

The accompanying cell error `2^-479` is still far smaller, so this arithmetic error alone does not destroy the scale separation. It does show that the displayed constants require machine checking; the provided constant audit does so with exact fractions and outward-rounded interval arithmetic.

## 6. What would repair the construction

A valid replacement for the missing step must partition every possible active set into at least:

1. global-net/global-net;
2. global-net/stable-collar;
3. global-net/spiral;
4. stable-collar/spiral;
5. every boundary feature of the intended stable face;
6. every non-apex feature on the boundary of the apex normal cone;
7. all nonsimplicial support ties.

For every class it must provide an explicit rational or outward-rounded **common separator** proving that the radial slope is outside the convex hull of all active normal slopes, or directly solve the complete normal-cone feasibility problem. After polarity, the final rational face lattice must be reconstructed, the true volume centroid recomputed, and the complete reference-point stability radius audited from all actual faces, vertices, and true edges.

Until one of those branch-complete certificates is supplied, the claimed `S=1,U=1,H=0` figure is unproved.

## 7. Reusable artifacts

- Complete independent audit bundle (`assignment3_independent_audit_bundle.zip`)
- Bundle SHA-256 (`assignment3_independent_audit_bundle.zip.sha256`)
- Full audit report (`AUDIT_RESULT.md`)
- Polarity and centroid derivation (`POLARITY_CENTROID_AUDIT.md`)
- Machine-readable audit summary (`audit_summary.json`)
- Mixed-feature obligation matrix (`mixed_feature_obligation_matrix.json`)
- Exact rational counterexample and complete face lattice (`mixed_transition_prism.json`)
- Primary exact verifier/generator (`verify_mixed_transition_gap.py`)
- Independent exact reader/verifier (`independent_check_mixed_transition.py`)
- Counterexample OBJ (`mixed_transition_prism.obj`)
- Exact/outward-rounded constant audit (`claimed_constants_audit.json`)
- Constant-audit code (`audit_claimed_constants.py`)
- Captured successful verification run (`VERIFICATION.log`)
- Integrity manifest (`MANIFEST.sha256`)
