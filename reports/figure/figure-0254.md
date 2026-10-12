# figure-0254

AI research report · 2026-09-03 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Bright Nova 91 — exact asymmetric open-V fifth-stage determination

## Journal basis

The run accepts only an explicit finite uniform-density convex polyhedron at its own exact ordinary-volume centroid with strict `(S,U,H)=(1,1,0)`, complete maximal-face and true-edge incidence, exhaustive positive-margin mechanics, independent verification, and matching OBJ/STL.

The accepted forked four-stage parent had supplied/active `3513/1577`, primal `(V,E,F)=(3150,4725,1577)`, replacement packet `S500004`, `U(2846,730000,730001)`, `H(1838,500004)`, `H(500004,730004)`, and the exact unique nonforcing exit `(730000,730001)` prescribed for this physical fifth-stage continuation.

## Immutable result

**EXACT NONWINNER.** No homogeneous convex polyhedral Gömböc was obtained. The materialized object is a finite exact-dyadic, uniform-density convex polyhedron evaluated at its own exact ordinary-volume centroid. Its exhaustive strict equilibrium class is

```text
(S,U,H)=(2,2,2).
```

The construction is nevertheless the requested physical fifth-stage branch advance. One exact one-boundary incidence exchange deletes all three edges of the forked-parent forcing triangle

```text
(2846,730000), (2846,730001), (730000,730001),
```

deletes inherited `S500004`, `U(2846,730000,730001)`, `H(1838,500004)`, and `H(500004,730004)`, and preserves intended `S3911` and `U(2024,2377,500004)`. A connected exact positive-volume five-substage open-V/prismatic return carrier contains the complete inherited packet.

The terminal replacement packet is

```text
S740001,
U(1871,2361,740002),
H(730003,740001),
H(730004,740001).
```

Its forcing structure is strictly smaller than the parent's: only arms `(1871,740002)` and `(2361,740002)` are all-positive at both endpoints. Base edge `(1871,2361)` has an exact negative external arrow and is the unique immediate nonforcing exit. The branch remains open, but this endpoint is not the target.

The exact rational M42 body `(V,E,F)=(61,163,104)`, strict `(S,U,H)=(2,1,1)`, remains the stronger run-wide equilibrium-count benchmark.

## 1. Deterministic exact source

Normative parent:

```text
source/parent_forked_four_stage_rows.hex
rows       3513
SHA-256    de92a87e1bae7415cb3170eba7c54513fc64cfe420ce466fddd95d42466a12f7
```

`source/construction_recipe.json` replaces rows

```text
1807, 1838, 1871, 1872, 2810, 2846, 2880, 2988, 500004, 710001, 730000, 730001, 730002, 730003, 730004, 730005
```

and appends five exact dyadic supports:

```text
740000=(-0x1.33ce5d1d29799p+1, 0x1.1312160b0698dp-1, -0x1.ad72e4e46f5b8p-6)
740001=(-0x1.33d199f39992ap+1, 0x1.131dc039f73d8p-1, -0x1.aa042be0107a8p-6)
740002=(-0x1.b20966c0c0765p-7, 0x1.377029704697bp-3, 0x1.9c0a83f9665dap-2)
740003=(-0x1.c043fe8e4ff7dp-2, 0x1.e814a2c131befp-4, 0x1.8063775ab87dbp-2)
740004=(-0x1.2f0c471ef5957p+0, 0x1.4a487976ff7b7p-2, 0x1.01ce33450c476p-2)
```

Every hexadecimal binary64 coordinate is interpreted as the corresponding exact dyadic rational. `src/build_endpoint.py` deterministically regenerates

```text
data/supplied_endpoint_rows.hex
rows       3518
SHA-256    bb3e8e442a4e18d47dee71aee61b4a3ddaa2ca47c4b58b0f5159f6c29aa55c44
```

and byte-identically reconstructs the stored active incidence, exact Cramer vertices, maximal-face cycles, true edges, display meshes, and one-boundary disk certificate. The equivalent common-denominator integer source is `data/supplied_endpoint_rows_integer.csv`, with denominator `2^109`.

## 2. Exact boundedness, irredundancy, H/V/E incidence

The independent all-row integer verifier proves

```text
supplied H rows                         3518
active irredundant H rows / primal F    1505
strictly inactive supplied rows         2013
primal vertices V                       3006
true primal edges E                     4509
oriented boundary triangles             6008
Euler V-E+F                              2
exact nonincident determinant checks    10566090
extra coplanar supplied rows             0
outside supplied rows                    0.
```

Complete exact data:

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

Every primal vertex is a Cramer rational. `geometry/true_edges.csv` contains maximal-face boundary edges only; polygon-fan triangulation diagonals are excluded.

Exact separation lower bounds:

```text
minimum nonincident primal slack
  1.4689227575116868179486308837739759907224637992927916971036166648929600e-09

minimum strictly inactive supplied-row slack
  8.3010062021788075851158804482258346406764110959645983568294119276372049e-05.
```

Throughout the full `2^-100` coordinate box, the minimum centred support denominator lies in

```text
[9.383350934004577386410553493553027168250557363e-01, 9.383350934004577386410623863074916411122874371e-01],
```

so the translated H-polytope remains bounded and full-dimensional.

## 3. Exact ordinary volume, moments, and own centroid

The GMP rational engine sums all 6,008 exact oriented boundary triangles. Complete reduced fractions are in `certificates/exact_mass_centroid.json`; high-precision readbacks are

```text
V  = 4.608178684139145053047549011047844831781766894013431981564383953969111188480464862915681071e+00
Mx = -9.240893970492927386342453349344818975750685203664919200833074986389110199924383151534863263e-02
My = 1.222567930928753467529365131986696780504197500119144813152118155016923073529903396268124690e-01
Mz = 1.445380465622851139556648963211052279223269099020131067201524346624463758464847150094453700e-01

cx = -2.005324576995915897018806411067653175813636108745563439820887931580437466486939491898096498e-02
cy = 2.653039334470038396705882532488232394046551153372229897669150270140533424682999464980328331e-02
cz = 3.136554731694096634781962743111194071020519248930593607380088982214612049512464032123793615e-02.
```

Exact integer cross-products prove `M_x=Vc_x`, `M_y=Vc_y`, and `M_z=Vc_z`. The own-centred body is `P_raw-c`; equivalently a centred normalized row is `q_i/(1-q_i·c)`.

The construction has 63 formal endpoint-coordinate controls and an exact `63×63` identity Jacobian minor. The three ordinary moments are dependent closure equations,

```text
F(a,c)=M(P(a))-V(P(a))c=0,
dF/dc=-V I_3,
rank=3,
det=-V^3<0.
```

Thus all 63 shape dimensions remain after moment elimination. This is a rank certificate, not a simultaneous-feasibility claim.

## 4. Exhaustive own-centroid mechanics

The zero-width 768-bit MPFR audit and the independent `±2^-100` interval audit agree exactly:

```text
stable maximal faces
  3911
  740001

unstable vertices
  (1871,2361,740002)
  (2024,2377,500004)

saddle true edges
  (730003,740001)
  (730004,740001).
```

The interval audit checks

```text
stable directed components       9018
unstable full-cone components    9018
saddle four-component cones     18036
ambiguous components                0.
```

Strict margin enclosures:

```text
minimum positive stable   [7.529756386138783531708344827156644070892641686e-06, 7.529756386138783540498089101898585690866383963e-06]
closest excluded stable   [-1.133679036889457749628949425348966363799271942e-05, -1.133679036889457748665208318233784665184412610e-05]
minimum positive unstable [7.589099155276881286836328185082816992803710614e-04, 7.589099155277309535549358470374229709588584724e-04]
closest excluded unstable [-2.499203586836787864286348856414022124348057553e-03, -2.499203586836787863870906692715164771975657109e-03]
minimum positive saddle   [5.951637152985165396201099513937228487790991515e-04, 5.951637152985165408317289804411795500603870665e-04]
closest excluded saddle   [-4.289387735368049043503369943714531195318573579e-03, -4.289387735368049013545706269418748264391385819e-03].
```

A separate exact determinant theorem independently perturbs every coordinate of all 3,518 supplied rows by `±2^-100` and preserves the supplied/active split, every Q facet, every maximal primal face, every true edge, and the strict `(2,2,2)` mechanics. This is an open nonwinner, not a wall point.

## 5. Exact one-boundary feature genealogy

The parent/final Q-facet symmetric difference is one connected disk-to-disk exchange:

```text
removed disk (V,E,F)=(147,376,230), chi=1
added disk   (V,E,F)=(75,160,86), chi=1
common boundary edges=62
boundary components=1.
```

Rows `730000` and `730001` become inactive; row `2846` remains active but loses both old forcing arms. All five appended rows `740000..740004` are active. The complete removed and added triangles, common boundary, support activity, and mechanical genealogy are recorded in

```text
certificates/exact_one_boundary_disk_exchange.json
certificates/exact_feature_genealogy.json
certificates/exact_relevant_support_activity.json.
```

## 6. Connected positive-volume fifth-stage carrier

`certificates/exact_openV_fifth_stage_transition_volume.json` independently reconstructs a convex placing triangulation seeded by a triangular bipyramid around the complete inherited owner face `(P2846,P730000,P730001)`. Its five communicating substages are:

```text
1. asymmetric open-V gate and first return supports;
2. forced-arm separation and quadrilateral/prismatic belt;
3. stable-side return communication;
4. two-saddle communication;
5. protected-target closure.
```

The final exact complex has

```text
vertices                    23
edges                       128
all triangular faces        195
tetrahedra                  89
Euler characteristic        1
boundary (V,E,F)            (19,51,34)
boundary Euler              2
boundary components         1
tetrahedral dual connected  true.
```

Exact carrier volume:

```text
3350199918610575234970769757797586051130145131452647 / 2244866514940266882360859903052210718191512386011136
= 1.4923826857026819278376843262015132666707426577356649378070275709986150651408389306E+0.
```

Every one of the 89 tetrahedra has strictly positive exact volume. The minimum is

```text
4337241805390220922054877244765 / 11692013098647223345629478661730264157247460343808
= 3.7095765877067344224920431755816787329514276151715291686155688886271157236998619484E-19.
```

Every placing attachment sees one connected visible boundary disk, every internal shared face has strict opposite-side orientation, the tetrahedral dual is connected, and the boundary is one sphere. The exact clean replay rebuilds all 89 tetrahedra from raw integer point and tetrahedron tables. Scope: this is a selected-state positive-volume carrier; it is not asserted to be the complete full-cloud regular subdivision. The actual full 3,513-to-3,518 body transition is separately established by the exact one-boundary Q-facet exchange.

## 7. Complete changed-edge external-arrow audit

The directed 768-bit ledger audits every endpoint true edge that is new, star-changed, geometry-changed, or incident to a moved/appended support:

```text
audited true edges       196
moved supports           21
appended supports        5
ambiguous arrow intervals 0.
```

Outside the protected intended triangle, exactly two changed edges are all-positive at both endpoints:

```text
(1871,740002)
(2361,740002).
```

The base edge `(1871,2361)` has the exact negative external-arrow witness

```text
[1871, 2361, 2502] -> [2361, 2502, 2537]
interval [-1.066477974813963934418084002851073050362834e-02, -1.066477974813963934418084002851073050362834e-02].
```

Hence the endpoint is an **open V**, not another three-edge forcing triangle.

## 8. Exact residual theorem

The owner `(1871,2361,740002)` is strictly unstable throughout the `2^-100` endpoint box. On each forced arm all nonmutual endpoint arrows are strictly positive, while the two mutual arrows satisfy exactly

```text
sigma(A->B)+sigma(B->A)=||A-B||^2>0.
```

Loss of the owner through either forced arm therefore transfers instability to the distinct opposite endpoint while fixed incidence and external signs persist. The base `(1871,2361)` is the only immediate owner-wall exit not covered by that transfer argument.

This is deliberately not a three-edge forcing theorem, does not prove `U>=2` after crossing the base-edge wall, and is not a global nonexistence result.

## 9. Exact death-before-birth chronology

For the named IEEE-754-rounded dyadic parent-to-endpoint chord, exact checkpoints bracket the first sampled signature change:

```text
t=69/256: class (2,2,2), exactly the inherited packet
t=70/256: class (2,3,3).
```

At `70/256`, inherited `S500004`, `U(2846,730000,730001)`, `H(1838,500004)`, and `H(500004,730004)` are still strict, while replacement `U(2846,2988,730000)` and `H(2846,730000)` are already strict. Thus complete inherited death does not precede replacement birth on this path.

The exact witness excludes only the named rounded dyadic chord. It does not locate the exact continuous first wall or exclude every path through the fifth-stage topology.

## 10. Empirical search scope

The retained primary finite searches contain 12,100 proposals and no sampled `(1,1,0)` winner. The raw compressed records and scripts are under `discovery_nonproof/`. They are discovery evidence only and carry no continuum-exclusion force. The promoted object was accepted only after deterministic exactification, one-boundary screening, all-row reconstruction, full-cone mechanics, arrow audit, chronology, and independent replay.

## 11. First genuinely unclassified successor

The first branch-local nonrepeating continuation is a **one-boundary sixth-stage split-arm open-quadrilateral/cubical gate with a dual return belt**, or a smaller strictly stronger equivalent. It must in one communicating positive-volume event:

1. cross the exact nonforcing base wall through `(1871,2361)`;
2. break or reverse both forced arms `(1871,740002)` and `(2361,740002)`;
3. kill `S740001`, `H(730003,740001)`, and `H(730004,740001)` before any replacement equilibrium becomes strict;
4. preserve `S3911` and `U(2024,2377,500004)`;
5. preassign a nonpositive external arrow on every new or star-changed edge; and
6. retain independent channel, stable/saddle, antibirth-timing, and moment controls.

Two connected supports plus coordinated motion of the owner/base/stable rows may suffice; three connected supports forming two arm-specific cells and an independently tunable return cell are the robust indicated realization. This is branch-local guidance, not a proof of global minimality.

## 12. Independent replay and display mesh

`src/verify_independent.py` imports no discovery or construction evaluator. It independently reconstructs the exact endpoint source from the declarative recipe, validates all 3,006 Cramer vertices, all 1,505 maximal-face cycles and 4,509 true edges, replays the exact GMP mass engine, rebuilds the one-boundary exchange and 89-tetrahedron ball, validates every changed-edge arrow record, binds both chronology checkpoints, checks all mechanics ledgers and hashes, and verifies the display mesh.

The own-centred OBJ has

```text
vertices                 3006
maximal polygon faces    1505
true polygon edges       4509
fan triangles            6008
reconstructed centroid norm 4.4240334218367806e-16.
```

The STL has 6008 consistently oriented triangles and is watertight. Mesh SHA-256 values:

```text
OBJ c430dc19e6c94364f4d20b60ae61fb9f7a88d27cb442afca6102a0024a5de802
STL 6c44e96c0b140c86000c8a0a2056b0136d14158439683165fcf0fe8cd8c14689.
```

Run

```bash
./verify_all.sh
BN91_RECOMPILE=1 BN91_DEEP=1 ./verify_all.sh
BN91_REPLAY_CARRIER=1 ./verify_all.sh
sha256sum -c MANIFEST.sha256
```

## Final status

```text
WINNER                                      NO
DISPOSITION                                 EXACT NONWINNER
PARENT SUPPLIED / ACTIVE                    3513 / 1577
ENDPOINT SUPPLIED / ACTIVE                  3518 / 1505
ENDPOINT PRIMAL (V,E,F)                     (3006,4509,1505)
ENDPOINT CLASS                              (2,2,2)
INTENDED S3911 / U(2024,2377,500004)        PRESERVED
ALL THREE INHERITED OWNER EDGES             DELETED
INHERITED STABLE / UNSTABLE / SADDLES       DELETED
ONE-BOUNDARY DISK EXCHANGE                  EXACT PASS
OPEN-V FIFTH-STAGE 89-TET 3-BALL            EXACT POSITIVE-VOLUME PASS
COMPLETE CHANGED-EDGE ARROW LEDGER          196 EDGES, ZERO AMBIGUITY
SIGN-FIRST ANTIBIRTH                        PARTIAL: BASE EXIT IS NONFORCING
NAMED-CHORD DEATH-BEFORE-BIRTH              FAILS BETWEEN 69/256 AND 70/256
REPLACEMENT OWNER                           (1871,2361,740002)
FORCED ARMS                                 (1871,740002),(2361,740002)
UNIQUE IMMEDIATE NONFORCING EXIT            (1871,2361)
EXACT ORDINARY VOLUME / MOMENTS             PASS
FULL IRREDUNDANT H/V/E                      PASS
FULL FACE/VERTEX/FOUR-COMPONENT EDGE AUDIT PASS
OPEN ALL-SUPPLIED COORDINATE BOX            2^-100
POST-MOMENT SHAPE RANK                      63
INDEPENDENT CLEAN REPLAY                    PASS
WATERTIGHT OBJ/STL                          PASS
GLOBAL NONEXISTENCE CLAIM                   NONE
NEXT CELL                                   SIXTH-STAGE SPLIT-ARM OPEN-QUADRILATERAL GATE
```

## Immutable archive and clean-extraction replay

Download the complete exact archive (`Bright_Nova_91_openV_fifth_stage_exact_NONWINNER.zip`)

```text
archive files       161
archive bytes       20,502,167
archive SHA-256     b1258a23a5776e352422970ba1088c28b4a78830afe2178473f4e01b3bb7788e
manifest entries    160
manifest SHA-256    44df330c04406c2ef3b047b7659da0ff07b8412a8023f04a0b1a86ac98ed62de
result-summary SHA  659c5d4879dfe2321f9b37e6f6b8f138050bea579ce6980f1a2c7007b25fc06a
handoff SHA-256     d6864c1d6b2c9efecc588f3fc064c9017e05ec690df04f509a3220d554e4c10a
```

The frozen ZIP passed CRC testing and was extracted with standard `unzip`, preserving executable modes. The clean extraction passed all 160 manifest bindings. From that extracted copy, the exact all-row verifier regenerated the canonical `3518/1505`, `(3006,4509,1505)` report byte-for-byte; the clean-room reconstruction, mesh verifier, result-binding verifier, and full 89-tetrahedron placing-carrier replay likewise regenerated byte-identical outputs.

Before freezing the archive, I found and corrected one metadata-only reproducibility defect: the source for the `t=70/256` MPFR chronology verifier emitted the stale report-mode literal `forked_four_stage`, while the canonical certificate used `openV_fifth_stage_chord_t_70_256`. After correcting only that literal and recompiling, the complete `t=70/256` report reproduced byte-for-byte. No coordinate, incidence, mass, mechanics, arrow, chronology, or topology datum changed. `logs/DEEP_RECOMPILE_TRANSCRIPT.txt` records fresh native compilation and byte-identical replay of the exact hull, GMP mass, zero-width mechanics, interval mechanics, changed-edge arrow audit, both chronology checkpoints, topology, ledgers, forcing theorem, control report, meta certificates, and the positive-volume carrier.
