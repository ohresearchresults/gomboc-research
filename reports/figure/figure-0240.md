# figure-0240

AI research report · 2026-09-03 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Bright Nova 91 — exact braided-antibirth terminal-volume handoff

## Determination and journal delta

The governing gate is a materialized finite uniform-density convex polyhedron at its own exact ordinary-volume centroid with strict `(S,U,H)=(1,1,0)`, complete H/V/true-edge mechanics, independent exact or directed verification, and matching OBJ/STL; auxiliary-centre, smooth, wall, near-solution, and unexpanded-generator results do not qualify. :contentReference[oaicite:0]{index=0}

The accepted input was the exact 3,501-row two-stage endpoint with replacement packet `S700003`, `U(700000,700001,700002)`, `H(1838,700003)`, `H(2627,700003)`. Its three unstable-triangle channels were external-positive, so the journal prescribed a one-boundary three-stage braid with an independently tunable antibirth return belt. :contentReference[oaicite:1]{index=1}

**EXACT NONWINNER.** No literal homogeneous convex polyhedral Gömböc was obtained. I materialized a genuinely nonrepeating exact endpoint whose connected one-boundary operation deletes all three inherited triangle edges, the inherited stable face, both inherited saddles, and then also deletes its intermediate relay triangle. The intended `S3911` and `U(2024,2377,500004)` survive. The final exact own-centroid class is nevertheless

```text
(S,U,H)=(2,2,2),
```

with replacement packet

```text
S710005,
U(2431,720000,720001),
H(1874,710005),
H(2662,710004).
```

The rational M42 `(V,E,F)=(61,163,104)`, strict `(2,1,1)`, therefore remains the stronger run-wide near-object.

## Exact deterministic source

Normative parent:

```text
source/parent_terminal_rows.hex
rows = 3501
SHA-256 = 50d1f09b31ab6e7e25607a8a22ee08ff2e1cfcc4c8c4f97970cc1248552fe1c5
```

Every hexadecimal binary64 coordinate is interpreted as its exact dyadic rational. `source/construction_recipe.json` and `src/build_endpoint.py` reproduce the endpoint without hidden search state.

Stage 1 replaces the exact triples of rows

```text
1801,1807,1838,2485,2627,2774,2775,2811,2838,
3770,3808,3874,3911,3912,3913,4053,4086,600000,600001,600002,
```

multiplies `700000..700003` by `1/2`, and appends

```text
710000=( 0x1.07f309aeb040ep-3, 0x1.04dcd5e21666ep-2, 0x1.6049f6fad2531p-2)
710001=(-0x1.502ec28c98618p-4, 0x1.316a4c917ceb5p-1, 0x1.0cd9737bde217p-2)
710004=(-0x1.c459ddbedf3b3p-2, 0x1.9214dd5c3e388p-1,-0x1.8e507f7f639f4p-3)
710005=(-0x1.077bffec44ecdp+1, 0x1.c44f4e9881a5cp-3, 0x1.40733c07d0898p-6).
```

The frozen intermediate has `3505/1620` supplied/active rows, primal `(3236,4854,1620)`, source SHA-256 `1b114b92e93470416494a6f91c8186b7111f0705189ed55816a6708e03bd1427`, and

```text
S={3911,710005}
U={(1836,600002,710000),(2024,2377,500004)}
H={(1874,710005),(2662,710004)}.
```

Stage 2 multiplies `1836,600002,710000` by `1/2` and appends

```text
720000=(-0x1.6bdf42b987af9p-2, 0x1.7399f16ea6bc1p-4, 0x1.a7d570cfe0f84p-2)
720001=(-0x1.9a910376b7260p-4, 0x1.483bf869ecd16p-2, 0x1.9c99830cdc1f3p-2).
```

Final source:

```text
data/supplied_endpoint_rows.hex
SHA-256 = 7cd16ffc1913c2d8e357e840a88e706c76a6b59dfa8960277a487688ae9cc28d
```

`data/supplied_endpoint_rows_integer.csv` is the equivalent common-`2^109` integer source.

## Exact boundedness and complete H/V/E incidence

The independent all-row reconstruction proves

```text
supplied / active / inactive H rows   3507 / 1621 / 1886
primal (V,E,F)                        (3238,4857,1621)
oriented boundary triangles          6472
Euler V-E+F                           2
exact nonincident determinant checks 11345952
extra coplanar or outside rows        0.
```

Every primal vertex is an exact Cramer rational. Complete data are in

```text
data/active_rows.hex
data/active_rows_integer.csv
data/active_to_supplied_map.json
geometry/primal_vertices_exact.csv.gz
geometry/maximal_face_cycles.json
geometry/q_facets.csv
geometry/q_facets_supplied_indices.csv
geometry/true_edges.csv
geometry/surface_triangles.csv.
```

`true_edges.csv` contains maximal-face boundary edges only; mass/STL fan diagonals are excluded. Exact lower separations are

```text
minimum nonincident primal slack = 1.4689227575116868179486308837739759907224637992927916971036166648929600e-9
minimum inactive-row slack       = 3.5600153193227252283471926512767206041090307200862730225577843060163893e-2.
```

The active polar hull is closed and full-dimensional. The `2^-100` enclosure keeps every centred support denominator above `0.87204017508681779344`, proving a bounded full-dimensional primal throughout the certified box.

## Exact ordinary volume, moments, and centroid

The GMP engine sums all 6,472 exact oriented triangles. Complete reduced fractions are in `certificates/exact_mass_centroid.json`; readbacks are

```text
V  =  5.1860080662892741721688536222115505867400502659552131368878754503388...
Mx = -0.2797385886613425348448627255959505714662463742083325475139290305022...
My =  0.2542294574242421934872390177771271162492109162450133299338248048556...
Mz =  0.1792039528152892718055636571339859892650627064379307558884392356970...

c = (-0.0539410245964971836217678631189600657123653651537565530768911595168...,
      0.0490221870414771817119092391573298161851550297445346797500505627495...,
      0.0345552784578513847293357597687965056022658861400557956437197290466...).
```

Exact integer cross-products prove `M_i=Vc_i`. The accepted body is `P_raw-c`; equivalently its centred normalized rows are `q_i/(1-q_i·c)`. Directed radius-`2^-100` enclosures for `V` and all three centroid coordinates are included.

The layered construction has 85 formal controls; three endpoint-redundant scale columns leave exact endpoint-coordinate rank 82. After imposing the three moment equations,

```text
F(a,c)=M(P(a))-V(P(a))c,
dF/dc=-V I_3,
rank=3,
det=-V^3<0,
```

so all 82 independent shape controls persist locally.

## Exhaustive full-normal-cone mechanics

Zero-width 768-bit MPFR and the full independent `±2^-100` active-coordinate audit agree exactly:

```text
S = {3911,710005}
U = {(2024,2377,500004),(2431,720000,720001)}
H = {(1874,710005),(2662,710004)}.
```

The audit checks 9,714 directed stable components, 9,714 full unstable-cone components, and 19,428 four-component saddle cones, with zero ambiguity. Strict interval margins are

```text
minimum positive stable   [9.403939588021376228791943128934647628692284788e-6,
                           9.403939588021376233627090239185091113581838753e-6]
closest excluded stable   [-1.250106394006851654476510998485595843656875820e-5,
                           -1.250106394006851654031000365853136549326381640e-5]
minimum positive unstable [3.041448559488908489585076843125322353429833183e-3,
                           3.041448559488911771759798539396602103799200370e-3]
closest excluded unstable [-5.564868721189517768232838417532788763570587716e-3,
                           -5.564868721189457706729585991842340489095558902e-3]
minimum positive saddle   [7.705282435012352387166490045661665565205541280e-4,
                           7.705282435012352398476393839702241598036031683e-4]
closest excluded saddle   [-3.935967846755513747090378825786448543345685741e-3,
                           -3.935967846755513737778572079428464991970708239e-3].
```

A separate exact determinant theorem perturbs all 3,507 supplied rows, including inactive rows, by `±2^-100` and preserves the entire active set and H/V/E lattice. This is an open nonwinner, not a wall.

## One-boundary genealogy and connected finite thickness

Parent-to-final Q-facet difference:

```text
removed disk (V,E,F)=(64,138,75), chi=1
added disk   (V,E,F)=(59,123,65), chi=1
common boundary length=51, boundary components=1.
```

It deletes all edges `(700000,700001)`, `(700000,700002)`, `(700001,700002)`, plus `S700003`, `U(700000,700001,700002)`, and both inherited saddles. All four `700xxx` supports are endpoint-inactive.

Intermediate-to-final difference is another disk inside the same global operation:

```text
removed disk (V,E,F)=(25,51,27), chi=1
added disk   (V,E,F)=(26,54,29), chi=1
common boundary length=21, boundary components=1.
```

It deletes intermediate triangle `(1836,600002,710000)` and all three of its edges. Final new-row activity is

```text
active:   710001,710004,710005,720000,720001
inactive: 1836,600002,710000,700000,700001,700002,700003.
```

The exact embedded three-stage carrier has

```text
18 tetrahedra, 16 vertices, 47 edges, 50 triangular faces,
Euler=1; boundary (V,E,F)=(16,42,28), boundary Euler=2,
one boundary component, connected tetrahedral dual,
volume = 269300392151312475612916761384436222826838850388057 /
         561216628735066720590214975763052679547878096502784
       = 0.4798510563706781924408197660988387336545002445046863401....
```

Stage 1 acts on the inherited triangle, Stage 2 communicates to the stable/two-saddle star, and Stage 3 is a geometrically distinct return belt rather than an opposite-face serial relay.

A larger exact 43-tetrahedron selected-state carrier spans parent, intermediate, and final representatives:

```text
17 vertices, 71 edges, 98 triangular faces, Euler=1;
boundary (V,E,F)=(14,36,24), one component, connected dual,
volume = 144250683474146143659183517963709618385950552900101 /
         187072209578355573530071658587684226515959365500928
       = 0.7710962723927545902479377673595290128106572870964616709....
```

All 559 nonvertex lower-lift gaps and all 74 internal shared-face opposite-side tests are exact and strict. This selected carrier is not asserted to be the full-cloud regular subdivision; the actual full-body transition is independently established by the exact one-boundary facet exchanges.

## External-arrow audit, forcing theorem, and chronology

Every terminal true edge that is new, star-changed, or incident to a moved/new-support star was audited:

```text
196 audited edges; 68 new; 123 star-changed; 74 new-support-star edges; 0 ambiguous.
```

For every endpoint the ledger includes every nonmutual arrow and verifies exactly

```text
sigma(A→B)+sigma(B→A)=||A-B||^2>0.
```

Every audited changed edge has a nonpositive external arrow at one endpoint except exactly

```text
(2431,720000), (2431,720001), (720000,720001),
```

the boundary of `T_final=(2431,720000,720001)`. All nonmutual arrows on those three channels are strictly positive. Hence, whether their common owner is unstable or not, this connected component contributes an unwanted unstable endpoint. Since protected `U(2024,2377,500004)` is disjoint and strict, `U≥2` throughout the fixed-incidence/external-positive terminal chamber.

The named direct parent-to-final hull chord fails death-before-birth at its first positive dyadic checkpoint `t=1/256`:

```text
supplied/active=3507/1629; primal=(3254,4881,1629); class=(2,2,2)
S={3911,700003}
U={(2024,2377,500004),(600000,700000,700001)}
H={(1838,700003),(2627,700003)}.
```

Thus replacement `U(600000,700000,700001)` is already strict while inherited `S700003` and both inherited saddles remain strict. This is an exact exclusion of that chord, not every path through the topology.

Finite metric, linear-control, row-ablation, one-/two-cap, face-chain, quadratic-stage, and iterative return-belt searches found no `(1,1,0)` sample. They are preserved under `discovery_nonproof/` only as empirical evidence, not an exclusion theorem.

## First genuinely unclassified successor

The first branch-local nonrepeating continuation is a **one-boundary forked four-stage triangular-prismatic/cubical or multi-octahedral volume with a second independently tunable antibirth return belt**, or a smaller strictly stronger equivalent. It must jointly:

- delete all three channels of `(2431,720000,720001)`;
- kill `S710005`, `H(1874,710005)`, and `H(2662,710004)`;
- preserve `S3911` and `U(2024,2377,500004)`;
- avoid exposing any next carrier as an opposite triangular face;
- preassign a nonpositive external arrow at one endpoint of every new or star-changed edge;
- keep every replacement equilibrium nonstrict until inherited death is complete;
- retain independent channel, stable/saddle, timing, and moment controls.

At least three connected new supports plus coordinated deactivation of the final triangle and `710005/710004` return rows are indicated; a five-support bifurcated belt is the robust version. This is not a global minimality or nonexistence claim.

## Independent replay, mesh, and immutable archive

`src/verify_independent.py` imports no discovery evaluator. It regenerates both stages, checks every active Cramer equality, every maximal-face cycle and true edge, both exact disk exchanges, exact `M=Vc`, both positive-volume carriers, every 43-tet lift gap, the arrow/forcing/chronology/control certificates, and mesh hashes.

The OBJ has 3,238 exact-centred display vertices, 1,621 maximal polygon faces, and exactly 4,857 polygon-boundary true edges. The STL has 6,472 consistently oriented triangles. Both reload watertight and connected; the OBJ reconstructed centroid norm is below `3.4e-16`.

The final packaging pass rebuilt every native C++ verifier from included source and regenerated byte-identical full-hull, GMP, zero-width/interval MPFR, arrow, forcing, and chronology reports. The Python clean-room, carrier, topology/ledger, and mesh verifiers were also replayed. Details are in `logs/DEEP_RECOMPILE_TRANSCRIPT.txt` and `logs/FAST_REPLAY_TRANSCRIPT.txt`.

[Download the complete exact archive](sandbox:/mnt/data/Bright_Nova_91_braided_antibirth_final_exact_NONWINNER.zip)

```text
archive bytes       17,931,053
archive SHA-256     221244bd6fa63d7ce504b508908e0eda9ff196e8af2749a047147a101e47f759
manifest SHA-256    e78a2aed0e4144059aa5945bf5ded57de40fa0bfc9ef70733937d0c422586a62
manifest entries    143 canonical files
archive files       159
```

The final ZIP was unpacked into a fresh directory. `sha256sum -c MANIFEST.sha256` passed every canonical entry, and `./verify_all.sh` ended with


[Encoded source block omitted; the code in this passage is incomplete.]


## Final status

```text
WINNER                                      NO
DISPOSITION                                 EXACT NONWINNER
FINAL SUPPLIED / ACTIVE                     3507 / 1621
FINAL PRIMAL (V,E,F)                        (3238,4857,1621)
FINAL CLASS                                 (2,2,2)
INTENDED S / U                              PRESERVED
INHERITED AND INTERMEDIATE TRIANGLE CHANNELS DELETED
ONE-BOUNDARY / FINITE-THICKNESS CERTIFICATES PASS
EXACT OWN CENTROID / FULL H-V-E / FULL CONES PASS
OPEN ALL-SUPPLIED BOX                       2^-100
SIGN-FIRST ANTIBIRTH                        FAILS ONLY ON FINAL TRIANGLE
DIRECT-CHORD DEATH-BEFORE-BIRTH             FAILS AT t=1/256
FINAL FORCING COMPONENT                     (2431,720000,720001), U>=2 LOCALLY
GLOBAL NONEXISTENCE CLAIM                   NONE
NEXT CELL                                   FORKED FOUR-STAGE VOLUME WITH SECOND RETURN BELT
```
