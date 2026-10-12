# figure-0210

AI research report · 2026-09-02 UTC

---

# Vivid Atlas 32 — P9-XG6 second-spine/fifth-page exact determination

## Verdict

**Exact finite NONWINNER.** No homogeneous convex polyhedral Gömböc was obtained. The work nevertheless advances beyond the inherited `M-N` forcing chamber in the literal topology requested:

- `M` and `N` become strict interior supplied rows and disappear from every actual face and edge;
- the complete old seven-triangle `M/N` disk, the extra stable `M`, the extra unstable vertex `SU/S102/M`, and saddles `S102-M`, `SA5-N` all disappear;
- a finite-thickness, positive-volume second-spine/fifth-page replacement is realized by four new extreme rows `X0..X3`, with coupled motion of `M,N`;
- five independent shape controls remain after exact ordinary-moment elimination;
- protected stable face `T27` and intended unstable lineage `TR/S102/G` survive;
- a *new*, smaller external-positive component is born on true edge `X2-X3`, forcing `S>=2` in the certified endpoint chamber.

Thus the required topology is realized and the prior component is genuinely deleted, but equilibrium cancellation is not achieved.

## Relation to the supplied journal

The inherited accepted boundary was the exact nine-row P9 two-row terminal `P:(V,E,F)=(14,21,9)`, own-centred `(2,2,2)`, with forcing true edge `M-N`. The journal identified a second-spine/fifth-page octahedral or triangular-prismatic pair with at least three post-centering controls as the first unclassified successor. :contentReference[oaicite:0]{index=0} This package is the first exact realization of that successor in this continuation.

The prior source is reproduced verbatim in `source_p9_xg5_two_row_exact.json`; its SHA-256 is bound by `input_rows_exact.json`.

## Exact primal/polar definition

For each supplied row `q_i`, define

```text
P_raw = {x in R^3 : q_i · x <= 1 for every supplied row i}.
```

Let `c` be the exact ordinary-volume centroid of `P_raw`. The delivered physical body is

```text
P = P_raw - c,
```

and its exact own-centred support rows are

```text
H_i = q_i / (1 - q_i · c).
```

All denominators are strictly positive. The exact endpoint rows are:

```text
T27  (-7125242734162057/140737488355328, 265769074670437/35184372088832, -63255401657691/70368744177664)  [active]
TR   (-892363419092795/281474976710656, -235941426090029/140737488355328, -528766574131575/140737488355328)  [active]
SU   (-544131479513675/140737488355328, -96790958131853/35184372088832, 118288508214145/140737488355328)  [active]
SC1  (-276717838830129/140737488355328, -1302539451900877/140737488355328, -228646779652985/70368744177664)  [active]
SA5  (-1735735365091297/281474976710656, -2190132466616797/281474976710656, -2075306589585777/281474976710656)  [active]
S102 (-1745325229249529/70368744177664, 5268329269809467/281474976710656, 1934562100355505/281474976710656)  [active]
G    (1595031506620615/70368744177664, 69636553284589/35184372088832, 72284311426759/70368744177664)  [active]
M    (1529073462/16777216, -268643187/16777216, 58067364/16777216)  [inactive]
N    (1529492441/16777216, -268486070/16777216, 58329226/16777216)  [inactive]
X0   (1919121502/16777216, -309962234/16777216, 99003968/16777216)  [active]
X1   (1848158428/16777216, -383623901/16777216, 89362767/16777216)  [active]
X2   (2073127498/16777216, -414482154/16777216, 17864224/16777216)  [active]
X3   (1956031545/16777216, -324421554/16777216, 24586561/16777216)  [active]
```

The unchanged old rows are exact rationals inherited from the source. The moved `M,N` and new `X0..X3` are dyadic with denominator `2^24`. `M,N` are deliberately retained as supplied rows so their strict inactivity is mechanically checked rather than assumed.

Machine-readable source: `input_rows_exact.json` and `raw_support_rows_before_after.csv`.

## Complete before-hull reconstruction

The source has nine supplied and nine active rows,

```text
Q_before:(V,E,F)=(9,21,14)
P_before:(V,E,F)=(14,21,9)
complexity = 42
class = (S,U,H)=(2,2,2).
```

Stable faces are `T27,M`; unstable vertices are `TR/S102/G` and `SU/S102/M`; saddle true edges are `SA5-N` and `S102-M`.

### All 14 actual source vertices / Q facets

```text
 0  T27/TR/SA5
 1  T27/TR/S102
 2  T27/SU/SC1
 3  T27/SU/S102
 4  T27/SC1/SA5
 5  TR/SA5/G
 6  TR/S102/G
 7  SU/SC1/M
 8  SU/S102/M
 9  SC1/SA5/N
10  SC1/M/N
11  SA5/G/N
12  S102/G/M
13  G/M/N
```

### All 21 source true edges

```text
T27-TR  T27-SU  T27-SC1  T27-SA5  T27-S102
TR-SA5  TR-S102  TR-G  SU-SC1  SU-S102
SU-M  SC1-SA5  SC1-M  SC1-N  SA5-G
SA5-N  S102-G  S102-M  G-M  G-N
M-N
```

### Source maximal-face cycles

```text
T27   0 4 2 3 1
TR    0 1 6 5
SU    2 7 8 3
SC1   2 4 9 10 7
SA5   0 5 11 9 4
S102  1 3 8 12 6
G     5 6 12 13 11
M     7 10 13 12 8
N     9 11 13 10
```

Every exact source vertex, centered row, cycle, true edge, and full four-component cone is expanded in `before_V_exact.csv`, `before_H_supplied_exact.csv`, `before_maximal_faces.csv`, and `before_true_edges_full_cones.csv`.

## Complete endpoint hull reconstruction

The endpoint has 13 supplied rows, exactly 11 active and irredundant rows, and two strict inactive rows `M,N`:

```text
Q_after:(V,E,F)=(11,27,18)
P_after:(V,E,F)=(18,27,11)
complexity = 54
class = (S,U,H)=(2,2,2).
```

### All 18 actual endpoint vertices / Q facets

```text
 0  T27/TR/SA5
 1  T27/TR/S102
 2  T27/SU/SC1
 3  T27/SU/S102
 4  T27/SC1/SA5
 5  TR/SA5/G
 6  TR/S102/G
 7  SU/SC1/X1
 8  SU/S102/X1
 9  SC1/SA5/X2
10  SC1/X1/X2
11  SA5/G/X3
12  SA5/X2/X3
13  S102/G/X3
14  S102/X0/X1
15  S102/X0/X3
16  X0/X1/X2
17  X0/X2/X3
```

### All 27 endpoint true edges

```text
T27-TR  T27-SU  T27-SC1  T27-SA5  T27-S102
TR-SA5  TR-S102  TR-G  SU-SC1  SU-S102
SU-X1  SC1-SA5  SC1-X1  SC1-X2  SA5-G
SA5-X2  SA5-X3  S102-G  S102-X0  S102-X1
S102-X3  G-X3  X0-X1  X0-X2  X0-X3
X1-X2  X2-X3
```

### Endpoint maximal-face cycles

```text
T27   0 4 2 3 1
TR    0 1 6 5
SU    2 7 8 3
SC1   2 4 9 10 7
SA5   0 5 11 12 9 4
S102  1 3 8 14 15 13 6
G     5 6 13 11
X0    14 16 17 15
X1    7 10 16 14 8
X2    9 12 17 16 10
X3    11 13 15 17 12
```

Every one of the `C(13,3)=286` candidate row triples was solved exactly. Exactly the 18 triples above are feasible. All nonincidences are strict. The minimum exact nonincidence slack is stored at `p9_xg6_second_spine_exact.json#/after/minimum_all_supplied_nonincidence_slack`; its decimal value is `0.021772808049677961`.

Expanded endpoint tables are `H_supplied_exact.csv`, `V_exact.csv`, `maximal_faces.csv`, and `true_edges_full_cones.csv`.

## Exact mass and own centroid

The exact rational ordinary volume, all three raw first moments, and all three raw centroid coordinates are reproduced without truncation in `exact_mass_centroid.json` and in `p9_xg6_second_spine_exact.json#/after/mass`.

For readability:

```text
V = 0.0019170255781429505
M = (-8.4995112354582617e-06,
     1.8217466289781972e-05,
     -4.962594105171368e-05)
c = (-0.004433697355093121,
     0.0095029855091602299,
     -0.025886947789078026).
```

The independent verifier recomputes these values from the maximal-face cycles. It then checks exactly

```text
M_x - V c_x = 0,
M_y - V c_y = 0,
M_z - V c_z = 0.
```

Hence the translated body has exact first moments `(0/1,0/1,0/1)` at its own ordinary-volume centroid.

A strictly positive four-row barycentric certificate places the origin in the interior of the polar row hull, proving boundedness. The exact minimum endpoint projective denominator is positive; decimal `0.68047925529976716`.

## Genuine finite-thickness shared-interior event

The removed and added boundary disks have the same exact five-cycle

```text
G - S102 - SU - SC1 - SA5 - G.
```

Removed source disk:

```text
G/M/N
G/M/S102
G/N/SA5
M/N/SC1
M/S102/SU
M/SC1/SU
N/SA5/SC1
```

Added endpoint disk:

```text
G/S102/X3
G/SA5/X3
S102/SU/X1
S102/X0/X1
S102/X0/X3
SA5/SC1/X2
SA5/X2/X3
SC1/SU/X1
SC1/X1/X2
X0/X1/X2
X0/X2/X3
```

The new disk has four interior extreme rows `X0..X3`. Radial spine `[0,X0]` has four pages; radial spine `[0,X2]` has five pages. The spines communicate through interior page `[0,X0,X2]`, with exact positive tetrahedra

```text
[0,X0,X1,X2]
[0,X0,X2,X3]
```

on opposite sides of that page.

A stronger exact finite-thickness certificate is in `shared_shell_exact_certificate.json`:

- `conv(G,S102,SU,SC1,SA5,M,N)` is an exact convex 3-ball whose boundary is the removed seven-triangle disk plus a common three-triangle complementary cap;
- `conv(G,S102,SU,SC1,SA5,X0,X1,X2,X3)` is an exact convex 3-ball whose boundary is the added eleven-triangle disk plus the same cap;
- old `M,N` lie strictly inside the larger new local hull, with minimum unnormalised inward slacks `465.93916198258984` and `504.30475596246481`;
- the closure of the difference is exactly the following face-to-face 17-tetrahedron shell:

```text
 1  SC1/SA5/X1/X2
 2  S102/SU/M/X1
 3  SU/SC1/M/X1
 4  S102/M/X0/X1
 5  M/X0/X1/X3
 6  X0/X1/X2/X3
 7  G/S102/X0/X3
 8  G/S102/M/X0
 9  G/M/X0/X3
10  G/SA5/N/X3
11  G/M/N/X3
12  SC1/SA5/N/X1
13  SC1/M/N/X1
14  SA5/N/X2/X3
15  SA5/N/X1/X2
16  N/X1/X2/X3
17  M/N/X1/X3
```

Its exact boundary is precisely the old seven-triangle disk union the new eleven-triangle disk. Every interior triangular face has two tetrahedra on strictly opposite sides. Exact shell volume is stored verbatim in the certificate; decimal

```text
V_shell = 4490.6589443513012
```

with minimum tetrahedron volume `20.233200137828607`. This is a genuine positive-volume shared-interior replacement, not a serial page appended along the old spine.

## Exact deletion of the inherited forcing component

After the event:

```text
M minimum support slack = 0.22036324417885272
N minimum support slack = 0.21993381627711797
```

Both exact slacks are positive. Therefore `M,N` are strict interior supplied rows, occur in no actual Q facet or Q edge, and the true edge `M-N` is absent.

The old edge had incident facets

```text
SC1/M/N
G/M/N
```

and link `{SC1,G}`. The later residual edge is `X2-X3`, with incident facets

```text
SA5/X2/X3
X0/X2/X3
```

and link `{SA5,X0}`. Its endpoint set and link are both different. Thus the certified old component is not renamed and is not transported along a surviving `M/N` page. It is deleted; a distinct component is born in the four-vertex replacement disk.

The old extra unstable vertex and both old saddle edges are likewise absent from the complete endpoint incidence.

## Exhaustive exact equilibrium audit

Endpoint equilibria are exactly

```text
stable faces:      T27, X2
unstable vertices: TR/S102/G, SU/S102/X1
saddle true edges: SA5-X2, S102-X0.
```

The audit uses actual maximal faces and true edges only. Stable faces are tested against every directed true-neighbour support. Every P vertex is tested in its full active three-row normal cone. Every true P edge is tested with all four strict components `t`, `1-t`, and the two face-normal cone coefficients.

Exact rational ledgers are in the main JSON/CSVs. Decimal category-clearance minima are

```text
stable positive                         116.49276013100913
nonstable-face exclusion                25.87237581629492
unstable full-cone coefficient          0.019922750726118803
nonunstable-vertex exclusion            0.00771876675578751
saddle full-cone component              0.00066630037334119898
nonsaddle full-cone exclusion           0.00024194474391933885
```

## Five independent shape controls after moment elimination

The three dependent translation controls have exact centroid-residual Jacobian `-I_3`, determinant `-1`.

The endpoint then retains these five independent raw-row controls:

```text
u1 = SU_z
u2 = SA5_z
u3 = X3_z
u4 = SA5_y
u5 = G_z.
```

They act on five separate topology/mechanics functions:

```text
f1 = det(X1-X0, X2-X0, X3-X0)             central diagonal
f2 = H_X2 · (H_X2-H_X3)                   stable-component wall
f3 = X1 cone coefficient at SU/S102/X1    extra-source wall
f4 = X2 cone coefficient on SA5-X2         first saddle wall
f5 = X0 cone coefficient on S102-X0        second saddle wall.
```

The ordinary centroid is recomputed inside the exact dual-number differentiation. The exact `5x5` determinant is nonzero and is stored at `event_controls_obstruction_exact.json#/shape_control_rank_after_moment_elimination/determinant`; decimal `2.4887239622399296e-06`. The normalized singular values are

```text
1.39056276145389, 1.163311512598613, 0.9780033498390196, 0.7852670270168988, 0.3740410072397934.
```

So this is rank five after the three exact moment controls, exceeding the requested rank three.

## Open perturbation certificate

`certify_perturbation.py` uses directed outward-rounded IEEE-754 interval arithmetic, with every exact rational input enclosed before use. It proves that all 39 raw support coordinates may vary independently by

```text
|delta q_ij| <= 2^-22 = 2.384185791015625e-07
```

while preserving:

- all 18 actual vertex triples and excluding all other 268 triples;
- actual `(Q,P)` f-vectors `(11,27,18)` and `(18,27,11)`;
- all 11 maximal-face cycles and 27 true edges;
- strict inactivity of `M,N`;
- positive volume, boundedness, and all projective denominators;
- exact own-centroid recomputation and full-cone class `(2,2,2)`;
- the four/five-page communicating-spine cell;
- the external-positive `X2-X3` component theorem.

Selected rigorous interval lower bounds are

```text
actual nonincidence slack                 0.021771068324999972
nonvertex blocker gap                     0.019095704486096651
positive face-tetra determinant            1.8281616206539984e-05
positive origin-tetra barycentric weight   0.10259133996996055
projective denominator                     0.6804298867282933
inactive M/N support slack                 0.21993133004447971
radial shared-cell tetrahedron volume      360.44523795517534
residual external support                  326.83965309273754
residual squared edge length               7.8614427326969825
```

Larger tested radii `2^-16` through `2^-21` failed closed; `2^-22` is the largest dyadic box found by this verifier.

## Independent clean-room verification and meshes

`verify_independent.py` imports neither the generator nor stored H/V/E/mechanical ledgers. Starting only from `input_rows_exact.json`, it independently reconstructs:

- all 84 source and 286 endpoint row triples;
- source and endpoint actual H/V/E incidence and maximal cycles;
- exact volume, first moments, centroid and own-centred support rows;
- every stable-face, unstable-vertex and four-component true-edge test;
- the old/new boundary disks and 17-tetrahedron shell;
- strict `M,N` inactivity and deletion of `M-N`;
- the exact five-control Jacobian;
- uniqueness of `X2-X3` among non-`T27` external-positive true edges;
- OBJ and STL edge multiplicities.

It ends with

```text
P9_XG6_INDEPENDENT_CLEAN_ROOM_PASS
```

The OBJ has 18 vertices, 27 undirected edges and 11 maximal polygonal faces, Euler characteristic two, with every polygon edge used twice. The STL has 32 triangular facets and every triangle edge used twice. Both are watertight decimal renderings of exact own-centred vertices.

## First remaining exact obstruction

The only non-`T27` true edge whose two endpoints have positive support toward every external true neighbour is `X2-X3`. At the exact endpoint the minimum external support is `327.4771095246744`. The mutual supports are

```text
A(X2 -> X3) = 116.49276013100913
A(X3 -> X2) = -108.60005999229344
```

and satisfy exactly

```text
A(X2 -> X3) + A(X3 -> X2) = ||H_X2-H_X3||^2 > 0.
```

Consequently the larger-radius endpoint has positive mutual support as well as all external supports and must be stable. `T27` is independently strict stable. Hence `S>=2` throughout the certified incidence/external-sign chamber. At the exact point, `X2` is the forced extra stable endpoint.

This is a chamber theorem, not a global exclusion of every second-spine/fifth-page realization.

## Numerical work attempted before exactification

The new topology search rebuilt the actual hull, ordinary-volume centroid, maximal faces, true edges, and all four edge-cone components at each accepted state. It tested:

```text
4 new rows: 16,000 proposals, 738 valid hulls, 229 target-lineage states
5 new rows: 24,000 proposals, 662 valid hulls, 209 target-lineage states
6 new rows: 24,000 proposals, 407 valid hulls, 139 target-lineage states
```

No `(1,1,0)` state occurred. A separate coupled-old-plane four-wall least-squares continuation from the selected topology did not reach a common strict death chamber. These are discovery observations only, not impossibility claims. Exactification selected filtered four-row candidate 14 because it was the smallest found architecture that strictly deactivated both `M,N`, preserved the protected pair, and realized the requested communicating spines.

Full empirical records are in `numerical_exploration.json` and the retained search files.

## Smallest residual component and next topology

The endpoint’s residual Euler-neutral block is

```text
extra stable:   X2
extra unstable: SU/S102/X1
saddles:        SA5-X2 and S102-X0
forcing edge:   X2-X3.
```

The smallest evidence-supported continuation is a **two-row third-spine/sixth-page `2<->3 / 3<->2` pair**:

1. one new row cuts the `SU/S102/X1` source star and the `S102/X0` saddle sector;
2. a second new row deletes `X2-X3` while cutting the `SA5/X2` saddle sector;
3. the two cuts must share a positive-volume tetrahedral/octahedral interior cell before either replacement row joins another external-positive component;
4. `T27` and `TR/S102/G` remain protected;
5. after the three exact moment controls, at least four and generically five independent shape coordinates are required for the diagonal, stable-component death, source death, and two saddle deaths.

Another serial edge split or one-page extension is not the next unclassified topology.

## Scope and uncertainty

The exact result closes the displayed endpoint’s full `2^-22` coordinate chamber and proves a genuine finite-thickness deletion of the inherited `M-N` component. It does **not** prove that every possible second-spine/fifth-page geometry is nonwinning, nor that the proposed third-spine successor is globally minimal among all conceivable support complexes. No strict `(1,1,0)` body is claimed.

## Reproduction

From the extracted directory:

```bash
./RUN_ALL.sh
```

Expected terminal line:

```text
ALL P9-XG6 SECOND-SPINE/FIFTH-PAGE VERIFIERS PASS
```

Primary files:

```text
input_rows_exact.json                     exact supplied rows before/after
p9_xg6_second_spine_exact.json            complete exact H/V/E/mass/mechanics
exact_mass_centroid.json                  exact volume, moments, centroid locator
shared_shell_exact_certificate.json       exact 17-tetrahedron finite-thickness event
perturbation_box_certificate.json         independent 39-coordinate 2^-22 box
independent_verification_report.json      clean-room replay report
verify_independent.py                     clean verifier
p9_xg6_second_spine_centered.obj          watertight polygon mesh
p9_xg6_second_spine_centered.stl          watertight triangulated mesh
RUN_ALL_OUTPUT.txt                         fresh complete transcript
```


## Downloadable artifact links

- [Complete exact bundle](sandbox:/mnt/data/P9_XG6_SECOND_SPINE_FIFTH_PAGE_EXACT_NONWINNER.zip)
- [Archive SHA-256 file](sandbox:/mnt/data/P9_XG6_SECOND_SPINE_FIFTH_PAGE_EXACT_NONWINNER.zip.sha256)
- [Complete Markdown handoff](sandbox:/mnt/data/P9_XG6_SECOND_SPINE_FIFTH_PAGE_EXACT_NONWINNER/RESEARCH_HANDOFF.md)
- [Exact before/after support rows](sandbox:/mnt/data/P9_XG6_SECOND_SPINE_FIFTH_PAGE_EXACT_NONWINNER/input_rows_exact.json)
- [Complete exact H/V/E/mass/mechanics ledger](sandbox:/mnt/data/P9_XG6_SECOND_SPINE_FIFTH_PAGE_EXACT_NONWINNER/p9_xg6_second_spine_exact.json)
- [Exact volume, moments, and centroid](sandbox:/mnt/data/P9_XG6_SECOND_SPINE_FIFTH_PAGE_EXACT_NONWINNER/exact_mass_centroid.json)
- [Exact 17-tetrahedron shared-shell certificate](sandbox:/mnt/data/P9_XG6_SECOND_SPINE_FIFTH_PAGE_EXACT_NONWINNER/shared_shell_exact_certificate.json)
- [Independent 39-coordinate perturbation certificate](sandbox:/mnt/data/P9_XG6_SECOND_SPINE_FIFTH_PAGE_EXACT_NONWINNER/perturbation_box_certificate.json)
- [Independent clean-room verification report](sandbox:/mnt/data/P9_XG6_SECOND_SPINE_FIFTH_PAGE_EXACT_NONWINNER/independent_verification_report.json)
- [Independent verifier](sandbox:/mnt/data/P9_XG6_SECOND_SPINE_FIFTH_PAGE_EXACT_NONWINNER/verify_independent.py)
- [Watertight OBJ](sandbox:/mnt/data/P9_XG6_SECOND_SPINE_FIFTH_PAGE_EXACT_NONWINNER/p9_xg6_second_spine_centered.obj)
- [Watertight STL](sandbox:/mnt/data/P9_XG6_SECOND_SPINE_FIFTH_PAGE_EXACT_NONWINNER/p9_xg6_second_spine_centered.stl)
- [Fresh full verification transcript](sandbox:/mnt/data/P9_XG6_SECOND_SPINE_FIFTH_PAGE_EXACT_NONWINNER/RUN_ALL_OUTPUT.txt)

Archive SHA-256:

```text
3ac113811f9deea24021cd249de55fa9a5b989d73dedc6ec147415bfb75d243a
```
