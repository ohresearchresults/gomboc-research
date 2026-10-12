# figure-0234

AI research report · 2026-09-03 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Calm Raven 06 — exact second-corrector mixed-cell determination

## Artifact and replay

- Complete exact replay bundle (`Calm_Raven_06_mixedcellE4_exact_NONWINNER.zip`)
- Archive SHA-256 file (`Calm_Raven_06_mixedcellE4_exact_NONWINNER.zip.sha256`)
- Full 52 kB research report (`RESULT.md`)
- 3.1 MB self-contained master certificate (`mixedE4_master_certificate.json`)
- Independent clean-room receipt (`independent_mixedE4_verification.json`)
- Watertight OBJ (`endpoint_centered.obj`) and binary STL (`endpoint_centered.stl`)

Archive SHA-256: `92b2605b8d7f83dada82d6b094a337d0424613f2dc0600a72cab62c9a5130a19`.

A pristine extraction ran `./RUN_ALL_VERIFIERS.sh`, checked all 76 immutable manifest entries, regenerated the exact endpoint and directed boxes, independently recompiled the GMP mixed-moment engine, and ended with:

```text
INDEPENDENT_EXACT_MIXEDE4_PASS
INDEPENDENT_RELEASE_SUMMARY_PASS
ALL_EXACT_MIXEDE4_VERIFIERS_PASS
```

## Literal disposition

**EXACT NONWINNER.** I advanced the exact post-CU10 `closededge21` endpoint with a second independent corrector summand `E` and materialized a genuine full-dimensional, nonboundary `(1,1,1)` mixed three-cell. The positive-scale common fan changes from parent `(V,E,F)=(71,132,63)` to `(110,212,104)`. The physical Minkowski sum has exact ordinary-volume centroid at the origin and exhaustive strict own-centroid class `(S,U,H)=(2,2,2)`, not `(1,1,0)`.

The run requires a finite uniform-density convex polyhedron evaluated at its own exact ordinary-volume centroid, with strict `(1,1,0)`, complete H/V/E incidence, exhaustive positive-margin face/vertex/full-edge-cone audit, an independent verifier and matching OBJ/STL. Artificial-centre, wall, smooth, near and unexpanded objects do not qualify.

## What was attempted

I reconstructed the exact parent, then searched actual D+E common fans rather than polishing a frozen fan. Three million random E directions yielded 1,030 strict covectors; 3,000 support pairs yielded 2,980 LP-feasible cells; 1,500 pair sums and selected three-/four-support extensions were rebuilt and mechanically audited. A separate five-vertex probe evaluated 500 strict candidates. These searches were used only to locate topology and are not continuum exclusions.

The promoted tetrahedral E was exactified at denominator `2^24`. The resulting D+E endpoint was reconstructed independently from rational H rows, and every final common face, vertex, true edge, first moment and equilibrium component was recomputed exactly. Attempts to falsify the endpoint found that all parent mechanical equilibria are deleted, but a new Euler-neutral packet is born. The complete external-arrow audit then gives an exact local obstruction: the new extra maximum and intended maximum are both strict, so the certified cell has `U>=2`.

## 1. Exact finite Minkowski family

```text
P(t1,t2,t3) = B + t1 C1 + t2 C2 + t3 C3
               + (10677075263/4294967296) D + E.
```

`D` is the inherited exact `closededge21` summand with `(V,E,F)=(16,25,11)`. Its complete 21 supplied rows, 16 exact vertices, 25 true edges and 11 maximal facets are embedded in the master certificate and expanded under `endpoint/D_*.csv`. `C1,C2,C3` are retained only as dependent full-rank controls for the three ordinary first moments.

The independent tetrahedral corrector has `(V,E,F)=(4,6,4)` and exact vertices

```text
e0 active(0,1,2) = (0, 0, 0)
e1 active(0,2,3) = (10738565/16777216,
                     -203062521/16777216,
                     -581510341/16777216)
e2 active(0,1,3) = (137690717/4194304,
                      233248965/16777216,
                    -3124960269/16777216)
e3 active(1,2,3) = (310663563/8388608,
                      276007399/16777216,
                      167037829/2097152).
```

Its exact irredundant H rows are

```text
E0: (-1,
      286716714209744003/770198995423025214,
     -38114685207035151/256732998474341738;
      h=0), cycle 2-1-0

E1: (-1174203361665806211/2677608452918225470,
       1,
      -3545358798267871/1338804226459112735;
       h=0), cycle 3-2-0

E2: (-110851824561842213/375658121586213046,
      -1,
       129132175965887081/375658121586213046;
       h=0), cycle 3-0-1

E3: (2055254181650673638/2588667045541756427,
      -1,
      -7697402748245886/2588667045541756427;
      h=552207856215455239309729063/
        43430626175135884595167232), cycle 2-3-1.
```

Exact exhaustive triple reconstruction returns precisely these four vertices and all six edges. Complete supplied and active summand data are in `summands_H.csv`, `summands_V.csv`, `endpoint/E_H.csv`, `E_V.csv`, and `E_edges.csv`.

## 2. Genuine positive-volume nonboundary mixed cell

At exact final common vertex 69, pure summand edges lead to vertices 85, 71 and 70 on the P9-side composite, scaled D, and E respectively. Their exact direction determinant is

```text
18546121773726108050493614658046813734387455112825028154321225605277117171809749417093578766869487587325265870012134295932088021560018095443541057735246347228327541201147167135243399952668380778216436781741
/
177975429074471466866394484913371899561388231906226120070543571603305809718292725310792182679765285361317047371516244435713499462756415559614757906615794482093122508484105099229328901462682548767293440
```

with absolute decimal locator `104206.0798514256`, hence positive volume. All eight exact parallelepiped corners are recorded; five are global common vertices.

In the Cayley embedding, the six selected edge endpoints are affinely independent. Giving those six lift zero and every other Cayley vertex lift one produces a lower simplex, hence a regular full-dimensional `(1,1,1)` mixed cell. Its midpoint lies in the relative interior of all three selected edges. Any boundary supporting normal would have to be perpendicular to three linearly independent directions and therefore be zero. This proves the cell is nonboundary, not another boundary page/cap coincidence.

Certificate: `positive_volume_cubical_mixed_cell_certificate.json`, SHA-256 `cecefa10f88a83aff1c6bf8d1c189d228fe31e36ba71151d7801e8c26094e714`.

## 3. Actual common normal-fan refinement

At E scale `mu=0`, E collapses to a point and the exact parent refinement is `(71,132,63)`. For every `mu>0`, the rebuilt actual common refinement is `(110,212,104)`, Euler two and complexity `424`. The exact changes are `+39` vertices, `+80` true edges and `+41` maximal faces.

Every parent common vertex is refined. The 104 final maximal faces decompose exactly as:

```text
63 parent-face + E-vertex faces
37 parent-edge + E-edge faces
 4 parent-vertex + E-face faces.
```

All 110 exact centred vertices, 104 oriented maximal-face cycles and 212 true edges are in `endpoint/final_centered_V.csv`, `final_centered_H.csv` and `common_edges.csv`, and are embedded verbatim in the master certificate. Minimum exact nonincident slack is positive, with decimal locator `1.3304141045599097e-6`.

Transition atlas SHA-256: `be374a561751650415103ec776f6e392b36aa1dccfaf5ff89f5e097d8edd7edb`.

## 4. Exact ordinary-volume moments

The final actual fan yields 20 mixed-volume coefficients and 35 coefficients in each first-moment polynomial. A freshly compiled GMP implementation independently reproduces every coefficient.

The ordinary first-moment system has the exact positive root

```text
(t1,t2,t3) = (1,1,1).
```

The exact Jacobian determinant is nonzero; decimal locator `-2.327275826473475e14`. A rational Krawczyk proof isolates the root in `[1±2^-22]^3`. Exact tetrahedral integration gives positive volume `1927420.7872868225…` and first moment exactly

```text
(Mx,My,Mz) = (0/1,0/1,0/1).
```

Therefore the uniform-volume centroid used for mechanics is exactly the origin. The full reduced volume fraction, Jacobian, inverse preconditioner, coefficient table and root enclosure are in `endpoint/exact_certificate.json` and `endpoint/root_certificate.json`.

Certificate hashes:

```text
endpoint/exact_certificate.json  2d133dc3e1a66599c2137feec58ac9e7486d800e6f9566b98de8738f6f3a2069
endpoint/root_certificate.json   e4a5cb8b828cc2c56d412fc8dc20181cab87dac66d0b900bb5a9a67513ac3e3e
```

## 5. Exhaustive own-centroid equilibrium audit

Every one of the 104 maximal faces, 110 vertices, 212 true edges and 848 full four-component edge-cone primitives is exact and nonzero. The complete positive equilibrium set is:

| type | id | exact common lineage | normalized margin |
|---|---:|---|---:|
| stable | 12 | `P9edge(13;26)|Dvertex(0;4;8;17;18;20)|Eedge(1;3)` | `0.010014017869396664` |
| intended stable | 65 | `P9face(27)|Dvertex(0;4;5)|Evertex(0;1;2)` | `0.015268019746629734` |
| unstable | 23 | `P9[9;32;103]|D[1;7;17]|E[1;2;3]` | `0.017351473859354944` |
| intended unstable | 71 | `P9[15;26;27]|D[0;4;8;17;18;20]|E[0;1;3]` | `0.2579036860200745` |
| saddle | 5 | `P9edge(13;26)|Dedge(4;5)|Evertex(1;2;3) || P9face(26)|Dvertex(0;4;5)|Evertex(1;2;3)` | `0.015129150513942454` |
| saddle | 189 | `P9edge(27;100)|Dedge(1;15)|Evertex(0;1;3) || P9edge(27;100)|Dedge(1;20)|Evertex(0;1;3)` | `0.0025749583695147205` |

Thus the exact class is `(2,2,2)`.

The complete external-arrow ledger audits all 110 final vertices. The only all-positive vertices are ids `23` and `71`. At extra vertex 23 the four exact outgoing arrows, shown by decimal locators, are

```text
23→11  +4200.821028579394
23→22  +0.8551758018608694
23→26  +2.2666226607086823
23→29  +23.455549881318145.
```

Hence id 23 is a strict extra maximum with minimum raw arrow `0.8551758018608694…`, while intended id 71 is a distinct strict maximum. This proves `U>=2` throughout the certified fixed-incidence/external-sign neighborhood.

External-arrow certificate SHA-256: `2e29222130131bcacadcb1e1e8e66c343ec13fd38230e286477f0ffd6e146c4f`.

## 6. Parent carrier deletion versus geometric survival

All four parent **mechanical equilibrium identities** are absent from the final critical ledger. The old extra-stable face has one exact geometric descendant and it is strict nonstable. Both old saddle families have exact descendants and all are strict nonsaddles.

The old extra-U geometry does not literally disappear. Tetrahedral E splits parent common vertex 32 into four exact common vertices, ids `52,53,54,55`; each has an explicit negative outgoing-arrow witness:

```text
52→48  -1.0952996050512818
53→49  -0.4173453886163165
54→53  -8142.7641486414805
55→25  -86.95762488953497.
```

So the parent unstable *mechanical* carrier is deleted, while its geometric P9+D lineage survives as four noncritical descendants. The topology then births the replacement packet listed above. Intended `D045` and `D048` lineages remain exact.

Lineage certificate SHA-256: `1e3c04492e6f7f145c7a481665fb4d33f325031ee8b413176139bd11f0177116`.

## 7. Positive shape family after centring

Fix E vertices `e0,e1,e2` and vary the three Cartesian coordinates of `e3` independently.

- A directed shape-only box of radius `2^-40` preserves tetrahedral E, actual common fan `(110,212,104)`, protected lineages and strict class `(2,2,2)` after evaluating each body at its own interval-enclosed centroid.
- A shape×control product box with E-shape radius `2^-48` and control radius `2^-42` around each `ti=1` preserves the same fan and class.
- A 150-digit parametric Krawczyk theorem gives E-shape radius `2^-64` and dependent-control radius `2^-42`: for every E shape in the three-dimensional box there is exactly one positive `(t1,t2,t3)` solving all three ordinary first moments.

Therefore three independent physical E-shape coordinates remain after centring; `C1,C2,C3` remain dependent rank-three moment controls and add no shape dimension.

Box hashes:

```text
shape-only      e1ea28fd510708ee8341ce8d66adf726af463b7d443eac42efba02fdce7623ea
shape×control   437e3ecb37886cd1596a45925f21e56f8b05cef4d2b4745ebdd61a8c8bdc30c9
implicit root   f66ce090e9da11d27b7f9b49df2c617628ca085f2713d4bec1e24800744da107
```

## 8. Independent reconstruction and mesh

`verify_mixedE4_cleanroom.py` imports neither the generator, `exact_core.py`, nor search state. It independently:

- exhausts all exact D and E row triples and matches all summand vertices, edges and facets;
- rebuilds the complete common H/V/E lattice and exact affine readback;
- recomputes exact volume, first moments and every face/vertex/full-edge-cone primitive;
- recompiles the GMP mixed-moment engine from source and matches all coefficients;
- verifies the rational Krawczyk root, common-fan transition, parent descendants, external arrows and nonboundary mixed cell;
- checks the directed shape/root boxes and matching OBJ/STL.

The mesh has 110 vertices, 216 outward-oriented triangles and 324 triangulation edges. Every edge has incidence two and `110-324+216=2`.

Independent receipt SHA-256: `642fe026165bbc028018e5fcf9399094c71397c1c591cd6248b7aaa4dcc6b438`.

OBJ SHA-256: `26ceaa46898350c0d24f1440f4ca9e13474cd16e34c005bde48478c1226c15bc`.

STL SHA-256: `e6884b1ac24f038dbd0fcc126b1a62199ca29099048adc14c19f9660414f7cbd`.

## Scope and first genuinely unresolved successor

This run certifies the exact tetrahedral-E endpoint and its open boxes. It does not exclude every tetrahedral E elsewhere, every five-vertex E, or every D+E common-fan component. The finite locator catalogs are not promoted as such an exclusion.

A tetrahedral E has no internal Radon circuit and simply refines every parent common vertex by a simplex. The smallest nonrepeating successor is therefore a **five-vertex triangular-bipyramid E** whose unique five-point Radon circuit supplies an adjacent `2↔3/3↔2` pair of full-dimensional mixed cells. Those cells must jointly deactivate final extra-U carrier `P9[9,32,103]|D[1,7,17]|E[1,2,3]`, remove extra stable `P9edge(13,26)|D048|Eedge(1,3)`, and cross both saddle cones before any replacement birth while preserving intended `D045/D048`.

If the single five-point circuit remains a relay, the next finite type is a six-vertex skew triangular-antiprism E with two coupled Radon circuits. This is the first evidence-supported mixed-cell frontier, not a proof of global support-count minimality.

## Principal immutable hashes

```text
MANIFEST.sha256                    721ab73da5681d83a1591bfe6386da49a40461f61b61bbd39bcafce30906cbae
RESULT.md                          27bd1d313261c835052add7852cf38d6d71f07718d9fb1f5227302da224b8545
mixedE4_master_certificate.json    eed2be99af6898da0c9f9880af02286923ecf24af917e797120750ad84a56e95
independent verification           642fe026165bbc028018e5fcf9399094c71397c1c591cd6248b7aaa4dcc6b438
exact endpoint                     2d133dc3e1a66599c2137feec58ac9e7486d800e6f9566b98de8738f6f3a2069
exact root                         e4a5cb8b828cc2c56d412fc8dc20181cab87dac66d0b900bb5a9a67513ac3e3e
mixed-cell certificate             cecefa10f88a83aff1c6bf8d1c189d228fe31e36ba71151d7801e8c26094e714
common-fan atlas                   be374a561751650415103ec776f6e392b36aa1dccfaf5ff89f5e097d8edd7edb
lineage certificate                1e3c04492e6f7f145c7a481665fb4d33f325031ee8b413176139bd11f0177116
external-arrow certificate         2e29222130131bcacadcb1e1e8e66c343ec13fd38230e286477f0ffd6e146c4f
```
