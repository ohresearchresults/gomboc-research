# figure-0067

AI research report · 2026-08-25 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Verdict

No strict homogeneous polyhedral Gömböc was found in this direction. The strongest reproducible endpoint is an **exact rational, full-active, unequal-cardinality six-level tower** with

\[
(V,E,F,C)=(27,41,16,82),\qquad (S,U,H)=(2,2,2)
\]

at its own uniform-volume centroid. It is therefore a fallback, not a winner. Unlike the inherited tower, however, its **five-vertex lower cap is now stable**, its **apex is unstable**, neither inherited apex-side stable quadrilateral survives as a stable face, and all 27 reconstructed vertices remain extreme. The residual defect is one side stable face, one side unstable vertex, and two saddle edges.

The journal supplied only the durable description of the prior `(26,40,16,80)` body—not its worker-local coordinate artifact—and records its nonstable lower cap, two stable apex-side quadrilaterals, unstable vertices `3,25`, saddles `(5,9),(23,25)`, and active circuit `{3,10,11,20}`. I therefore opened a new exact H-combinatorial family rather than pretending to perform a literal coordinate edit of unavailable bytes.

## What changed relative to the supplied journal

- The requested unequal section sizes are realized exactly as **`5 / 8 / 5 / 4 / 4 / 1`**: five lower-cap vertices, an eight-vertex first rail, two staggered middle sections of five and four vertices, a four-vertex terminal ring, and one apex.
- Fivefold symmetry was broken at initialization through unequal cardinalities, unequal plane slopes/supports, and nonuniform twists. No rotational orbit constraints were imposed.
- The old `10-11` direction survives as the true edge `(10,11)`. The old `3-20` diagonal is deliberately no longer a true edge; its connected replacement strip is the true-edge path `3-14-15-20`. Thus both transfer directions are covered by one extended strip rather than polished independently.
- Every apex-incident maximal face is nonstable, while the apex is the target unstable vertex. The old pair of stable apex-side quadrilaterals is gone.
- The lower cap is face/plane `0` and is strictly stable with normalized margin `+0.23415601603497222784`.
- The apex is vertex `26=(0,0,1)` in the canonical gauge and is strictly unstable with normalized margin `+0.86601009033075543651` and height gap `+0.0019971851196789510881`.
- No macroscopic lower-layer expansion was used. Five independently verified true-edge routes connect every lower-cap vertex to the apex.

## Exact rational H-description

The body is

```text
P = {x in R^3 : (A_num[i]/D)·x <= b_num[i]/D, i=0,...,15},  D=10,000,000.
```

Equivalently, the following integer inequalities define exactly the same body:

```text
 i     A_num[i]                                      b_num[i]
 0     (        0,         0,  -10000000)                    0
 1     (  9012388,  -4333229,   15052038)             62893420
 2     (  9694145,  -2454294,  -38543601)            -11144089
 3     ( -8490424,   5283248, -117178570)            -60400468
 4     ( -9460308,   3240766,    -775249)             24325585
 5     ( -7343652,  -6787545,  -15993928)            535101323
 6     ( -7788861,   6271654, -106548553)            -65468613
 7     ( -9434539,   3315036,   19073959)             26205632
 8     ( -9695287,   2449776,   82692020)             90442498
 9     (  8320235,  -5547404,   35563698)            152717195
10     (  9515343,  -3075425,   14070416)             21259715
11     (  8084533,   5885603, -123450312)            -89331254
12     ( -9722939,   2337616,  130843238)            130843238
13     (  9715897,  -2366718,   15534570)             15534570
14     ( -8910028,   4539977,  -23947327)            -23947327
15     ( -9296580,   3684237,   24583381)             24583381
```

The canonical gauge has lower plane `z>=0`, apex `(0,0,1)`, and concurrent top planes `12,13,14,15`. All 16 planes are active. Exact reconstruction produces 27—and only 27—vertices; no inactive V-row is being counted as a layer vertex.

## Exact volume and centroid constraint

The exact volume is a positive rational number whose decimal value is

```text
94.71112035844875773271
```

and the canonical-gauge own centroid is

```text
c = (-10.06662453571699265264,
     -28.86324310064464813385,
       0.3927107123828277905313).
```

The exact numerator/denominator of the volume and all three exact centroid coordinates are embedded verbatim in the audit and verifier transcript. Translating by this exact rational `c` gives the centered H-description in the bundle, and independent Fraction integration returns

```text
(M_x,M_y,M_z) = (0,0,0) exactly.
```

Thus the three first-moment equations are not residual tolerances in the returned object. Search states were always rebuilt and evaluated at their own integrated uniform-volume centroid; the final reconstruction is exactly centered.

## Layer membership and active side routes

Layer assignment is made only after exact hull reconstruction:

```text
L0 lower cap       (5):  0 1 2 3 4
L1 first rail      (8):  14 16 18 5 17 6 10 19
L2 middle A        (5):  15 7 11 20 13
L3 middle B        (4):  12 25 22 8
L4 terminal ring   (4):  21 23 9 24
L5 apex            (1):  26
```

The two middle sections are staggered rather than coplanar rings. Their unshifted `z` ranges are respectively `0.3244867333..0.5004493538` and `0.5080417501..0.7425944053`; the terminal ring spans `0.7946638748..0.9980028149`.

Each lower-cap vertex has a route to the apex consisting entirely of reconstructed true edges:

```text
0 -> 5  -> 9  -> 24 -> 26
1 -> 6  -> 7  -> 8  -> 23 -> 26
2 -> 10 -> 11 -> 13 -> 25 -> 26
3 -> 14 -> 18 -> 22 -> 26
4 -> 16 -> 17 -> 18 -> 22 -> 26
```

This is the active-side gate used in rejecting row/vertex deletions: no obsolete vertex was allowed to disappear when doing so disconnected a cap-to-apex route.

## Reconstructed maximal faces

Face index equals defining-plane index; cycles are outward-oriented:

```text
 0:  0 1 4 3 2
 1:  5 9 8 7 6 1 0
 2:  0 2 10 11 13 12 5
 3:  2 3 14 15 10
 4:  3 4 16 17 18 14
 5:  6 19 16 4 1
 6:  15 20 11 10
 7:  21 22 18 17
 8:  7 8 23 21 17 16 19
 9:  6 7 19
10:  12 24 9 5
11:  20 25 13 11
12:  8 9 24 26 23
13:  12 13 25 26 24
14:  18 22 26 25 20 15 14
15:  23 26 22 21
```

There are no additional maximal coplanar faces.

## Reconstructed true edges

```text
(0,1) (0,2) (0,5) (1,4) (1,6) (2,3) (2,10) (3,4) (3,14)
(4,16) (5,9) (5,12) (6,7) (6,19) (7,8) (7,19) (8,9) (8,23)
(9,24) (10,11) (10,15) (11,13) (11,20) (12,13) (12,24) (13,25)
(14,15) (14,18) (15,20) (16,17) (16,19) (17,18) (17,21) (18,22)
(20,25) (21,22) (21,23) (22,26) (23,26) (24,26) (25,26)
```

Euler checks: `27-41+16=2`, and `C=27+41+16-2=82`.

## Exhaustive own-centroid mechanics

The standalone exact verifier classifies every maximal face, every actual vertex using its complete incident normal cone, and every true edge using both endpoint and both incident-normal conditions.

### Surviving equilibria

```text
STABLE FACES
face 0 / plane 0, cycle [0,1,4,3,2]
  normalized margin = +0.23415601603497222784       (target)
face 8 / plane 8, cycle [7,8,23,21,17,16,19]
  normalized margin = +0.0085483932905749471702     (unwanted)

UNSTABLE VERTICES
vertex 6, incident planes [1,5,9]
  normalized margin = +0.0024587195908432793653     (unwanted)
vertex 26, incident planes [12,13,14,15]
  normalized margin = +0.86601009033075543651       (target apex)

SADDLE EDGES
edge (5,12), incident planes [2,10]
  normalized margin = +0.010843019336966307585
  four normalized conditions =
  [+0.010843019336966307585, +0.98915698066303369242,
   +1.1095300395427073351,   +1.242722310969983991]
edge (18,22), incident planes [7,14]
  normalized margin = +0.0098725896729249675194
  four normalized conditions =
  [+0.0098725896729249675194, +0.99012741032707503248,
   +1.1603197729425646182,    +1.1953018652087269162]
```

With the search convention `hard defect = -max(unwanted positive margin)`, the final hard defect is

```text
-0.010843019336966307585.
```

Every other maximal face, vertex, and true edge is strictly non-equilibrial. The nearest exact opposite-side gates are:

```text
face 4       -0.000051626848808442087958
vertex 19    -0.00018106457658577020947
vertex 5     -0.00042078515728954765677
edge (0,5)   -0.00016527807207278216393
edge (17,18) -0.00020465852978136566421
edge (14,18) -0.0020198398996133281491
```

The full score for all 16 faces, all 27 vertices, and all 41 edges is in `tower_unequal_audit.json`; none of the exact face, vertex, or edge primitives vanishes.

### Incidence/support gate

```text
minimum normalized nonincident support separation
  = 0.0010795245511117388657
  witness = plane 12 versus vertex 21

minimum raw nonincident slack
  = 3766302529733049919688903 / 174086600559523042016875000
  = 0.021634649178213401827...
  witness = plane 7 versus vertex 23
```

The normalized support gate is about `6.58×` the journal fallback's approximately `1.64e-4`. Every nonincidence slack is exactly positive. This is not a support/circuit wall; the mechanical result is nevertheless wrong because four unwanted equilibria survive.

## Realized topology and Morse transitions

Every checkpoint below was rebuilt from the complete H-hull and evaluated at its own integrated centroid. The first three are numerical search checkpoints; the last is the exact seven-decimal rational reconstruction.

| state | `(V,E,F)` | `(S,U,H)` | stable faces/planes | unstable vertices | saddles | support separation | hard defect |
|---|---:|---:|---|---|---|---:|---:|
| initial unequal full-active family | `(27,41,16)` | `(3,2,3)` | `0,4,12` | `19,26` | `(12,13),(3,14),(17,18)` | `3.8079e-4` | `-6.77825e-2` |
| centroid-coupled fixed cell | `(27,41,16)` | `(3,2,3)` | `0,4,12` | `6,26` | `(5,12),(3,14),(17,18)` | `1.93568e-3` | `-2.32089e-2` |
| apex-separated pre-crossing cell | `(27,41,16)` | `(3,3,4)` | `0,4,12` | `5,6,26` | `(0,5),(5,12),(14,18),(17,18)` | `1.72750e-3` | `-1.08940e-2` |
| coupled `UAB` crossing, exactified | `(27,41,16)` | `(2,2,2)` | `0,8` | `6,26` | `(5,12),(18,22)` | `1.07952e-3` | `-1.08430e-2` |

The coupled crossing removes unstable vertex `5` with saddle `(0,5)` and removes stable plane `4` with the two-edge saddle fan `(14,18),(17,18)`. The Euler-balanced residue transfers rather than disappears: stable equilibrium `12 -> 8`, while the second saddle transfers `(17,18) -> (18,22)`. The target lower cap and apex stay strict throughout.

After that crossing I tested, with a full dynamic hull rebuild after every accepted point:

- direct branches forcing all four residual signs;
- connected one- and two-plane truncation cells, reaching 17–18 active planes and up to 31 reconstructed vertices;
- multi-row strip differential evolution over the complete residual corridor;
- independent row support/slope/twist sweeps;
- deletion candidates gated by the five connected side routes.

No strict `(1,1,0)` chamber appeared. The added-plane cells remained `(2,2,2)` and reduced or relayed individual saddle margins rather than cancelling the complete block. These are empirical branch-search results, not an exact global exclusion.

## Sharply delimited obstruction

The final residual block has four coupled members:

```text
stable face 8  <-> transfer edge (8,23) <-> near-stable face 12
unstable v6    <-> transfer edge (6,19) <-> near-unstable v19
saddle (5,12)
saddle (18,22)
```

For edge `(6,19)`, the endpoint condition is already negative,

```text
-0.079495791879266391429,
```

but the two normal-cone coefficients stay strongly positive, approximately

```text
+1.89475, +1.66648.
```

Changing only the endpoint direction therefore births saddle `(6,19)` before the unstable vertex can be removed. Similarly, moving stable face `8` alone transfers stability across `(8,23)` toward face `12`; suppressing either current saddle alone produces the Euler-required partner elsewhere. This is the precise local conflict observed between the fully connected active side routes and the unique-lower-cap chamber.

The evidence supports a **local/architectural obstruction**, not a theorem for all unequal-cardinality towers: within the tested 16–18-plane neighborhood, preserving all five cap-to-apex routes compresses the remaining defect into one coupled `S/U/2H` transfer block. Single-diagonal polishing cannot cross it.

## Reproducible artifact set

- Complete ZIP bundle (`unequal_tower_fallback_bundle.zip`) — SHA-256 `dfd5d8ce2b1860320b6d8823ff5de316527c7286aa5702fdd7ce5ae5c3cf9ca4`
- Exact canonical H-description (`tower_unequal_H_rational.json`)
- Exact own-centered H-description (`tower_unequal_H_centered_rational.json`)
- Exact centered V-coordinates (`tower_unequal_V_centered.csv`)
- Complete exact audit (`tower_unequal_audit.json`)
- Standalone Fraction verifier (`verify_tower_exact.py`)
- Verifier transcript (`verifier_transcript.json`)
- Topology record (`topology.txt`)
- Transition record (`search_transitions.md`)
- OBJ mesh (`tower_unequal.obj`)
- ASCII STL mesh (`tower_unequal.stl`)
- SHA-256 manifest (`MANIFEST.sha256`)

Run from the extracted bundle:

```bash
python verify_tower_exact.py
```

Expected terminal status is `PASS`, with `(V,E,F,C)=(27,41,16,82)`, exact centered moments `(0,0,0)`, class `(2,2,2)`, stable faces `[0,8]`, unstable vertices `[6,26]`, and saddle edges `[(5,12),(18,22)]`. The exact verifier's semantic certificate hash is

```text
06fb68b454426c4eba26138590ae0e1731875d1f28e2ec45301082007b9034d4.
```

The verifier uses only Python `fractions.Fraction`: it enumerates exact triple intersections, filters exact feasible vertices, reconstructs exact incidences/maximal faces/true edges, integrates exact tetrahedral volume and first moments, and classifies all complete normal cones. It does not depend on SciPy/JAX, floating hull tolerances, or search-time incidence thresholds.

The OBJ/STL are the centered fallback mesh, not winner files. Seven-decimal rationalization preserves the exact topology and all signs; six-decimal rounding was rejected because it can merge incidences. No numerical coordinate perturbation radius is claimed for acceptance, because this is not a winner. Exact nonzero feature primitives and positive nonincidence slacks prove the reported finite geometry itself, while a separate quantitative radius remains to be derived.

## Most useful continuation

Open one new bifurcated combinatorial family that replaces **both** transfer corridors simultaneously:

1. replace the face-8 corridor through `(8,23)` by a 3–4-vertex branch toward the top fan;
2. replace the vertex-6 corridor through `(6,19)` by a staggered 3–4-vertex branch toward the lower/first rail;
3. include at least three independent, mechanically inactive controls and eliminate the three exact moment equations at every accepted state;
4. enumerate the resulting circuit cells before any metric polishing;
5. allow old rail vertices to deactivate only when all five cap-to-apex routes remain connected.

A plausible next cell has about 30–32 actual vertices and 17–18 active planes, still comfortably below complexity 120. The key test is whether one coupled crossing can annihilate the full `S/U/2H` block instead of producing the observed transfers `8->12`, `6->19`, and saddle relay.
