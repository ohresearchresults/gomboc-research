# figure-0261

AI research report · 2026-09-03 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Clear Willow 25 — incomplete two-boundary drainage determination

## Disposition

**NO WINNER AND NO NEW EXACT ENDPOINT PROMOTED.**

I did not obtain the required finite homogeneous convex polyhedral Gömböc, nor did I complete an exact, independently replayable two-boundary drainage successor beyond the immutable twelve-support parent. The required object remains a uniform-density convex polyhedron evaluated at its own exact ordinary-volume centroid with strict `(S,U,H)=(1,1,0)`; auxiliary-centre mechanics, transfer-wall states, numerical near-solutions, and unexpanded constructions do not qualify.

The strongest exact object in this direction therefore remains parent result `figure-0255`, SHA-256 `a1bfb5efa0d7b7fe843cfe6a190c1e42756319d0fae85dd68a0fdce05c458ebe`. Its actual hull is `(V,E,F)=(69,187,120)`, strict own-centred `(2,1,1)`, with extra stable face `[258,259,6301]`, saddle `(248,6310)`, protected stable 17-gon `[0..16]`, and protected unstable vertex `8`. It already contains an exact internally linked positive-volume regular 3-ball and an exact no-birth U–H cancellation, but the final S–H pair survives.

Immutable exact parent archive (`M42_slot1_Clear_Willow_25_tri_prism_exact_complete.zip`) — SHA-256 `95d0e03d0d6ee45f5750be64847aee113c40a34f4af4a97b02582a5dd1ec3ef7`.

No conflict was found between the literal immutable parent payload and the journal summary.

## Work completed in this continuation

### 1. Full local geometry was reconstructed from the exact parent

The parent exact source and full-hull incidence were reopened rather than inferred from the assignment description. The surviving left star is

```text
stable face [258,259,6301]
6301 neighbours:
  257,258,259,260,261,262,263,6300,6302,6303
```

and the surviving right star is

```text
saddle edge (248,6310)
incident faces:
  [248,6309,6310]
  [248,6310,1026].
```

At the exact own centroid, `6301` is a strict radial local minimum. Representative centred radii are

```text
r(3)      ≈  1.1233
r(15)     ≈  1.8604
r(14)     ≈  2.2370
r(6301)   ≈  3.1896
r(6300)   ≈  4.2018
r(6302)   ≈  4.6287
r(72)     ≈  9.967
r(69)     ≈ 17.028
r(6309)   ≈ 31.174
r(6310)   ≈ 31.223
r(1026)   ≈ 31.592
r(248)    ≈ 32.520.
```

The exact parent stable-face decision is controlled by the component opposite edge `(6301,258)`:

```text
stable components for [258,259,6301]
  approximately [38.1863, 0.477426, 0.00663313].
```

The adjacent face `[257,258,6301]` is already nonstable with normalized decision about `-0.0055208743`. On the right, saddle `(248,6310)` has four components approximately

```text
(t,1-t,beta1,beta2)
  = (0.980796, 0.0192040, 0.90115, 0.231124),
```

while adjacent edge `(1026,6310)` is nonsaddle only by about `-0.0046134124`. These values explain why separate left or right polishing repeatedly reaches a transfer wall.

Reconstruction scripts and diagnostics:

- parent analyser (`run11_analyze_parent.py`)
- parent analysis transcript (`run11_analyze_parent.log`)
- dual-route analyser (`run11_dual_paths.py`)
- dual-route transcript (`run11_dual_paths.log`)

### 2. A shorter drainage route into the protected-base basin was found

The journal names the route through rows `69` and `72`. Full dual-graph reconstruction exposes a shorter and radially stronger route through protected base vertex `14`:

```text
[258,259,6301]
 -> [259,260,6301]
 -> [260,261,6301]
 -> [261,262,6301]
 -> [13,262,261]
 -> [13,261,14]
 -> [0..16].
```

This matters because `r(14)≈2.237 < r(6301)≈3.190`. A genuine active interface reaching this route could give the unwanted basin a descending exit without relying on the much more distant rows `69` and `72`.

The discovery also changes the minimum necessary topology. The left operation cannot be confined to rows `6301,258,259`: it must alter the intervening `261/262` circuit or an equivalent old-row diagonal before a new descending chain can become an actual hull path.

### 3. Exact visibility chambers isolate the missing left circuit

I solved the affine visibility inequalities for prospective connector points against the complete parent face set. The certificates and reconstruction code are:

- exact visibility builder (`run11_visibility_exact.py`)
- exact visibility certificate (`run11_visibility_exact.json`)
- exact visibility transcript (`run11_visibility_exact.log`)
- quadratic projection builder (`run12_qp_visibility.py`)
- quadratic projection data (`run12_qp_visibility.json`)
- quadratic projection transcript (`run12_qp_visibility.log`)

Representative feasible connector locations are

```text
qA ≈ (-5.9108047483,  6.4726780963, -0.5740425665)
     centred radius ≈ 6.10
     sees the first four left-page faces

qB ≈ (-4.39967298,    7.44436022,    0.16548918)
     centred radius ≈ 5.78
     sees the two old-row drainage faces

qC ≈ (-2.9451603333,  3.9707307807,  0.1149667937)
     centred radius ≈ 2.237
     lies just outside face [13,261,14]
     and approaches protected base vertex 14.
```

The desired radial order `qA -> qB -> qC -> 14` is therefore geometrically available. However, in the complete actual hull the old true edge `(261,262)` separates the `qA` and `qB` visibility chambers. Adding all three points while keeping `261` and `262` fixed does not create the needed active edge `qA-qB`; `qA` instead closes a new low-radius fan and becomes the carrier of another stable face.

This gives a sharply scoped combinatorial obstruction:

> In the tested fixed-old-row visibility complex, a descending two-boundary page cannot be formed merely by adding connectors in the successive face chambers. The `261/262` circuit must cross, or one of rows `261,262` must move or become nonextreme in the same event.

This is not a global impossibility theorem for all drainage patches.

### 4. The right star also requires a complete boundary replacement

Fixed-face finite-difference continuation reduced the components of `(248,6310)` but created the adjacent stable face `[248,6310,1026]` and saddle edge `(248,1026)` before the original saddle could disappear. The resulting class was `(3,1,2)`, not `(1,1,0)`.

Artifacts:

- first fixed-cell continuation (`run13_scp_fd_parent.json`)
- first continuation transcript (`run13_scp_fd_parent.log`)
- post-transfer continuation (`run13_scp_fd_stage2.json`)
- post-transfer transcript (`run13_scp_fd_stage2.log`)

Large deletion screens gave the same structural outcome. Removing `6310` alone transfers the saddle through the `1026/6008` return channel; removing `6301` alone transfers the stable feature to a neighbouring inserted row, commonly `6302`. Thus the right operation must replace both faces

```text
[248,6309,6310]
[248,6310,1026]
```

and must also control the alternative edges through `1026`, `6008`, `249`, and `230`. At least one of `{248,1026}` must move or become nonextreme together with `6310`; deleting only the inserted endpoint is repetitive.

### 5. Two-boundary point and cap probes did not realize the required active annulus

I tested:

- simultaneous cap points over the complete left drainage face chain;
- simultaneous cap points over both right saddle faces;
- three-point radial chains based on `qA,qB,qC`;
- deletion of selected path rows followed by complete hull rebuilding;
- old-row motion involving `261,262`;
- large deletion subsets spanning both stars;
- base-anchored global cuts intended to remove both carriers in one operation.

Shallow caps remained separate subdivisions and did not open a descending active interface. Deeper caps created new local minima, unstable old boundary vertices, and compensating saddle edges. Coarse base-anchored cuts created large faces and several new U/H features. No sampled full hull had strict `(1,1,0)`.

These are finite empirical screens, not exact family exclusions.

### 6. The strongest multi-cut nearstate remains a transfer-wall object

A simultaneous halfspace-cut search produced a body with reconstructed class `(2,1,1)` and approximately

```text
actual (V,E,F)          (92,209,119)
extra stable carrier    [258,259,10015,10014]
stable margin           6.9e-7
saddle carrier          (10000,10001)
saddle margin           1.18e-6
minimum topology gap    8.31e-7
protected base margin   0.9461
protected U8 margin     0.17135.
```

Files:

- multi-cut search (`run11_multicut_local.py`)
- best multi-cut snapshot (`run11_multicut_local_HS_204.json`)
- multi-cut transcript (`run11_multicut_local_HS_204.log`)

Although it substantially compresses the two residual margins, its topology and equilibrium gaps are too small for promotion. It is another real transfer wall, not an open Gömböc chamber or a suitable exact fallback.

### 7. A topology-preserving projective orbit was opened as a separate escape test

The parent metric-only orbit had already been screened. I extended the search to genuine projective transformations

```text
Y_i = A X_i / (1 + b dot X_i),
```

where `X_i` are parent own-centred coordinates, `b` supplies three projective denominator parameters, and `A` is either the identity or a five-parameter determinant-one positive metric. Positive denominators preserve the complete face lattice while changing the ordinary centroid and Euclidean equilibrium field.

Search and current finite records:

- projective search driver (`run14_projective_search.py`)
- three-parameter projective state (`run14_proj_b_1401.json`)
- three-parameter transcript (`run14_proj_b_1401.log`)
- projective-plus-metric state (`run14_proj_metric_1402.json`)
- projective-plus-metric transcript (`run14_proj_metric_1402.log`)

The best completed three-parameter samples remained `(2,1,1)`. The saddle margin was reduced from the parent value `0.019204...` to roughly `0.0134`, while the stable carrier moved among `[260,261,6301]` and `[261,262,6301]`. The combined projective/metric samples generally opened additional remote U/H features and did not improve on this.

These runs had not reached a completed optimizer termination at the forced return boundary. Their partial files are discovery data only and are not evidence for an exact endpoint or exclusion.

## Strongest combined conclusion

The parent diagnosis can now be sharpened in two places.

### Left boundary

The obstacle is not merely that `6301` is a radial local minimum. The actual boundary diagonal `(261,262)` prevents a sequence of individually feasible connector chambers from becoming one active descending path to the protected base. A successful patch must cross this old-row circuit while eliminating the `6301` fan. At least one of

```text
6301, 258, 259, 261, 262
```

must change extremality or incidence, and merely replacing `6301` repeats the carrier transfer.

### Right boundary

The obstacle is not merely the edge `(248,6310)`. Its complete two-face star and the adjacent `1026/6008` return channel form a transfer complex. A successful patch must simultaneously alter at least one of

```text
6310, 248, 1026
```

and preclude the replacement carriers `(248,1026)`, `(248,6008)`, `(249,6008)`, and their associated exposed faces.

The two obligations must be coupled before exact moment elimination. Independent left and right pages repeatedly reach their respective transfer walls at different times.

## Smallest genuinely nonrepeating successor

The first still-unclassified topology is more specific than a generic two-boundary annulus. It is a **two-interface annular 3-ball with an explicit old-diagonal exchange on the left and a complete two-face-star exchange on the right**.

A minimal robust incidence model should contain three communicating bands:

```text
left outer band:
  attached across [258,259,6301], [259,260,6301],
  [260,261,6301], [261,262,6301]

base-drain band:
  crosses or deletes old edge (261,262),
  then attaches through [13,262,261] and [13,261,14]
  to the protected-base basin

right return band:
  replaces [248,6309,6310] and [248,6310,1026],
  while blocking the 1026/6008/249 transfer channel.
```

The left and right bands must share a positive-volume interior cell or at least two independent interior interfaces. The left band needs an actual monotonically descending edge route ending at row `14` or `15`; graph connectivity among new rows alone is insufficient. The right band needs a separate diagonal/timing control so its saddle death does not expose `(248,1026)`.

The smallest plausible realization is approximately 10–14 new extreme rows **with coordinated motion or deactivation of old rows `261,262` and one of `248,1026`**. Without old-row motion, the connector count is likely larger because separate supports are needed to cross both inherited diagonals.

After the three ordinary-moment equations are imposed, at least four independent physical controls should remain:

```text
1. crossing of the 261/262 left circuit;
2. death of the closed 6301 stable fan;
3. death of the complete right saddle star;
4. external-arrow and replacement-birth timing.
```

A useful constructive parameterization is not another sequence of face caps. It should directly prescribe two overlapping positive-volume cells:

```text
Cell L: an octahedral or triangular-prismatic cell spanning
        {259,261,262,6301,qA,qB,qC}
        with the far triangulation containing qA-qB-qC-14
        as an active descending route;

Cell R: an octahedral or triangular-prismatic cell spanning
        {248,1026,6309,6310,rA,rB,rC}
        with the far triangulation deleting both old saddle faces
        and no edge in the 248/1026/6008 return packet saddle.
```

The cells should overlap through at least one tetrahedron or quadrilateral interface tied to route row `228`. A regular-subdivision search should enumerate their joint circuit signatures before coordinates are optimized. This is the smallest topology not represented by the failed cap, cut, deletion, fixed-lattice, and projective screens above.

## Missing required evidence

Because no new exact endpoint was completed, this continuation does **not** supply:

- a new deterministic exact coordinate source beyond the parent;
- a new exact all-supplied H/V/E reconstruction;
- new exact volume and first-moment identities;
- a new exhaustive exact equilibrium ledger;
- a positive perturbation box for a two-boundary successor;
- an exact death-before-birth chronology for the desired S–H cancellation;
- an independent verifier or watertight OBJ/STL for a new body.

The numerical nearstates must not be promoted. The parent archive remains the last independently verified exact object and retains strict `(2,1,1)`. Its final conclusion—that `6301` remains a closed radial minimum and `(248,6310)` remains an independent saddle—is still valid.

## Reusable continuation boundary

The next copy should begin from the immutable parent archive, use the exact face lattice rather than the near-wall multi-cut state, and enumerate the coupled `261/262` and `248/1026` circuit signatures first. The first promoted endpoint must demonstrate in the rebuilt actual hull:

```text
- one of {6301,258,259} inactive;
- one of {6310,248,1026} inactive;
- old edge (261,262) absent or on the required opposite diagonal;
- an active descending path into base vertex 14 or 15;
- both old right incident faces absent;
- no stable, unstable, or saddle replacement anywhere;
- exact own-centroid class (1,1,0).
```

Anything that retains `(261,262)`, changes only `6301`, changes only `6310`, or connects the unwanted stars without a base-side descending interface repeats a mechanism already exposed here.
