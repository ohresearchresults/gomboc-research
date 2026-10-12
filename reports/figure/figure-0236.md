# figure-0236

AI research report · 2026-09-03 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Bright Nova 91 — exact one-boundary two-stage terminal volume

## Determination

**EXACT NONWINNER.** No strict homogeneous convex polyhedral Gömböc was obtained. The materialized object is a finite exact-dyadic uniform-density convex polyhedron evaluated at its own exact ordinary-volume centroid, but its exhaustive strict equilibrium class is

```text
(S,U,H)=(2,2,2).
```

This endpoint nevertheless performs the assigned topology change: one connected one-boundary operation deletes all three true-edge channels of the predecessor forcing triangle `T'=(2775,600000,600002)`, deletes the predecessor extra stable equilibrium and both predecessor saddles, and preserves `S3911` and `U(2024,2377,500004)`. A connected positive-volume two-stage carrier is certified. The failure is replacement birth: a new Euler-neutral packet is strict, and the realized internal-arrow prescription fails exactly on a new forcing triangle.

The result does not supersede the run-wide rational M42 `(61,163,104),(2,1,1)` benchmark.

## 1. What changed relative to the journal endpoint

The exact predecessor has

```text
supplied / active H rows = 3497 / 1624
primal (V,E,F)           = (3244,4866,1624)
strict class             = (2,2,2)
extra packet             = S500004,
                           U(2775,600000,600002),
                           H(1838,500004), H(2627,500004).
```

This continuation leaves all 3,497 parent rows unchanged and appends four connected exact supports. The complete rebuilt endpoint has

```text
supplied / active H rows = 3501 / 1626
strictly inactive rows   = 1875
primal (V,E,F)           = (3248,4872,1626)
surface triangles        = 6492
Euler V-E+F              = 2.
```

All four appended rows are active. Parent row `600000` becomes inactive; `2775`, `600002`, `500004`, `1838`, and `2627` remain active, but none of the predecessor unwanted features survives mechanically.

## 2. Exact source and deterministic generator

The complete predecessor source is

```text
source/parent_terminal_rows.hex
SHA-256 1b9e2bda6ba2742cdc3b9cd00a2819b5848c7da5d2000969f29f3c9cd4cd09b3.
```

Parse each hexadecimal binary64 value as its exact dyadic rational and append

```text
700000 = ( 0x1.cba7d7dd07fdcp-4,
           0x1.3bfeab034e588p-5,
           0x1.7eba500f82651p-2)

700001 = (-0x1.259f8d750e94bp-1,
           0x1.2a2623fa66b41p-1,
           0x1.8f2784bee1bb1p-3)

700002 = (-0x1.442741ad1f924p+0,
           0x1.032eb521ef4a3p-5,
           0x1.6af232dbe05c2p-3)

700003 = (-0x1.044afb99d3302p+1,
           0x1.d90d9a3354cdep-2,
          -0x1.093c093afe7e3p-6).
```

No old-row multiplier or hidden fitting parameter is used. The exact recipe is `source/construction_recipe.json`; the resulting supplied source is

```text
data/supplied_endpoint_rows.hex
SHA-256 50d1f09b31ab6e7e25607a8a22ee08ff2e1cfcc4c8c4f97970cc1248552fe1c5.
```

`data/supplied_endpoint_rows_integer.csv` is the equivalent common-denominator integer source with denominator `2^109`. Exact active rows are supplied in hexadecimal and integer form.

## 3. Complete exact H/V/E incidence

The independent `boost::multiprecision::cpp_int` all-row verifier proves

```text
supplied rows                         3501
active rows / maximal primal faces   1626
strictly inactive rows               1875
Q facets / primal vertices           3248
Q edges / primal true edges          4872
exact nonincident checks         11,361,504
extra coplanar supplied rows             0
outside supplied rows                   0.
```

Complete files are

```text
data/active_rows.hex
data/active_rows_integer.csv
data/active_to_supplied_map.json
geometry/primal_vertices_exact.csv.gz
geometry/maximal_face_cycles.json
geometry/q_facets.csv
geometry/true_edges.csv
geometry/surface_triangles.csv.
```

Every primal vertex is an exact Cramer rational. `geometry/true_edges.csv` records only maximal-face boundary edges. Fan diagonals used to integrate polygonal faces and to write STL are expressly excluded from the true-edge ledger.

The active polar hull is full-dimensional and its facet sphere is closed. After translation to the exact ordinary centroid, every support denominator `1-q_i·c` remains strictly positive; the smallest directed interval is

```text
[0.8501549843734123354342006916075613787116412459,
 0.8501549843734123354342033488558358150455226214].
```

Thus the H intersection is nonempty, full-dimensional, and bounded, and all 1,626 active rows are irredundant.

Exact global separations are

```text
minimum nonincident primal slack
  1.4689227575116868179486308837739759907224637992927916971036166648929600e-9

minimum strictly inactive supplied-row slack
  4.6086039101879198905893571962756910424148480471921048009986360964623681e-4.
```

## 4. Exact ordinary volume and all first moments

The GMP rational engine sums all 6,492 consistently oriented exact boundary triangles. Complete reduced fractions are in `certificates/exact_mass_centroid.json`; decimal readbacks are

```text
V  =  5.3397246467345708681274856613220048709642999904646622751841459740...
Mx = -0.3538163350244168782445607162352725512728206087220819098836179580...
My =  0.1878011172468471272099977459685682702030067309044797457678238974...
Mz =  0.3783930393562874074325799309027108191536831244765711172229134091...

c_x = -0.0662611573502742302953270761940410944489880867601539377962267083...
c_y =  0.0351705620928775990822694210186568638610507579712495403425688308...
c_z =  0.0708637737692500752249673505679295414238431921268701652126318106....
```

Exact integer cross-products prove `M_x=Vc_x`, `M_y=Vc_y`, `M_z=Vc_z`. The accepted own-centred body is `P_raw-c`; equivalently a normalized centred H row is `q_i/(1-q_i·c)`.

The twelve coordinates of the four new supports are independent shape variables, with an exact `12 x 12` identity minor. The three ordinary-centroid variables are dependent hard variables:

```text
F(a,c)=M(P(a))-V(P(a))c=0,
dF/dc=-V I_3,
rank(dF/dc)=3,
det(dF/dc)=-V^3<0.
```

The certified topology/mechanics box therefore remains twelve-dimensional after eliminating the three moment equations.

## 5. Exhaustive own-centroid mechanics

The exact strict endpoint equilibria are

```text
stable maximal faces
  3911
  700003

unstable vertices
  (2024,2377,500004)
  (700000,700001,700002)

saddle true edges
  (1838,700003)
  (2627,700003).
```

Thus the intended stable/unstable pair survives. The predecessor packet is deleted, but the new packet is

```text
S700003,
U(700000,700001,700002),
H(1838,700003),
H(2627,700003).
```

The 768-bit directed MPFR audit reconstructs interval vertices and the ordinary centroid and checks all

```text
stable directed components       9744
unstable vertex-cone components  9744
saddle edge-cone components     19488
ambiguous components                0.
```

Over independent perturbation of every active-row coordinate by `±2^-100`, the decisive margins remain separated:

```text
minimum positive stable component
  [ 2.205289035544089398535447784664143732654545894e-5,
    2.205289035544089398940198051969602641446358608e-5 ]
closest excluded stable component
  [-1.743097055280243391479481843701276062006933965e-5,
   -1.743097055280243391025030173107358174057492332e-5 ]

minimum positive unstable component
  [ 5.359822331559143028070188005602743910458561726e-3,
    5.359822331559224542936855082619863341784166298e-3 ]
closest excluded unstable component
  [-8.330168853216976104995484595450483141763200891e-3,
   -8.330168853216974495222272106791854708076222556e-3 ]

minimum positive saddle component
  [ 2.346202883030814514573250264387867676340220791e-3,
    2.346202883030814514575538815813094009459163357e-3 ]
closest excluded saddle component
  [-1.225888664313512395869980862310866378498738156e-3,
   -1.225888664313512394063809709247567837512299635e-3 ].
```

The compressed midpoint ledgers enumerate every tested component. `certificates/exact_topology_radius_2^-100.json` separately perturbs all 3,501 supplied rows and proves that the same active/inactive H set, every Q facet, every maximal primal face, and every true edge persist. This is an open strict nonwinner, not a bifurcation point.

## 6. One-boundary transition and exact feature genealogy

The parent/final Q-facet symmetric difference is one connected disk exchange. The removed and added disks are

```text
removed: (V,E,F)=(19,38,20), chi=1
added:   (V,E,F)=(21,44,24), chi=1,
```

and share one 16-edge boundary cycle:

```text
1738-1807-1838-1801-1836-1976-2011-2046-
2081-2811-2775-2774-2838-2627-2485-500004-1738.
```

The operation deletes all predecessor edges

```text
(2775,600000), (2775,600002), (600000,600002),
```

and deletes `U(2775,600000,600002)`, `S500004`, `H(1838,500004)`, and `H(2627,500004)` as equilibrium features. The old support `500004` remains extreme but is no longer stable. Exact removed/added triangle lists, star comparisons, and lineage are in `certificates/exact_one_boundary_disk_exchange.json` and `certificates/exact_feature_genealogy.json`.

## 7. Connected positive-volume two-stage three-ball

The valid transition carrier consists of two communicating exact octahedral stages and one transverse return tetrahedron.

Stage 1 is the combinatorial octahedron

```text
O1={2775,600000,600002,700000,700001,700002}.
```

Its old face is exactly `T'=(2775,600000,600002)`; its opposite new face is `(700000,700001,700002)`. It therefore acts on all three predecessor forcing channels in one cell.

Stage 2 is

```text
O2={700003,1838,2627,2775,600000,600002}.
```

It shares `T'` with `O1` from the strict opposite open halfspace and communicates the channel event to the stable/two-saddle side. The transverse return tetrahedron

```text
R=(1838,2627,700003,500004)
```

attaches across `(1838,2627,700003)` and contains the predecessor stable support plus both predecessor saddle edges.

The certified union has

```text
tetrahedra                    9
vertices                     10
edges                        26
all triangular faces         26
Euler of 3-complex            1
boundary (V,E,F)       (10,24,16)
boundary Euler                2
boundary components           1
connected tetrahedral dual  yes.
```

Its exact positive volume is

```text
8360602025925550360130172356701546538872130929210673 /
17958932119522135058886879224417685745532099088089088
=0.4655400427087318165789125003447970506582110852005547344....
```

The smallest exact tetrahedral volume is

```text
67620774796282050218961431056213674551093842009 /
4489733029880533764721719806104421436383024772022272
=1.50612017120495370047129010493502476859391939848517e-5....
```

Exact face multiplicities, orientations, shared-face halfspaces, nonadjacent separation, volumes, boundary component, and dual connectivity are recorded in `certificates/exact_two_stage_transition_volume.json`. The certificate is reconstructed independently from exact integer support coordinates.

## 8. External-arrow sign-first audit

Every true endpoint edge whose two labels are among the four new supports was audited exactly. The complete internal set is

```text
(700000,700001)
(700000,700002)
(700001,700002)
(700001,700003)
(700002,700003).
```

For every endpoint, the ledger records every nonmutual incident-neighbor arrow and the exact mutual identity

```text
sigma(A toward B)+sigma(B toward A)=||A-B||^2>0.
```

The intended sign-first requirement succeeds on neither endpoint simultaneously for the first three edges: all nonmutual external arrows at both endpoints are strictly positive. Those three edges are precisely the boundary of the new forcing triangle

```text
T''=(700000,700001,700002).
```

The two edges joining `700003` to the triangle do not have this all-positive-at-both-endpoints defect. Therefore the realized design fails for a sharply identified three-edge carrier, not for every new edge. The exhaustive rational ledger is `certificates/exact_new_carrier_arrow_ledger.json`.

## 9. Exact death-versus-birth chronology

For the named natural actual-hull path

```text
all parent rows fixed,
q_700000(t)=t q_700000(1), ..., q_700003(t)=t q_700003(1),
0<=t<=1,
```

the exact open checkpoint `t=251/256` has

```text
(S,U,H)=(2,2,2)
S={3911,700003}
U={(2024,2377,500004),(2775,600000,600002)}
H={(1838,500004),(2627,700003)}.
```

At this one checkpoint the replacement `S700003` and `H(2627,700003)` are already strict while inherited `U(2775,600000,600002)` and `H(1838,500004)` remain strict. Hence complete predecessor death does not precede replacement birth on this path. The checkpoint has its own exact H/V/mass/MPFR files in `chronology/t_251_256/`.

This is an exact exclusion of the named chord only. It is not a continuum theorem for every path through the two-stage incidence topology.

## 10. Complete terminal forcing theorem

The three edges of `T''=(700000,700001,700002)` are true. At the exact ordinary centroid, every nonmutual endpoint support on each is a strictly positive rational and each pair of mutual supports sums exactly to a positive squared primal-edge length:

```text
(700000,700001): ||A-B||^2 = 6.1816746537348035047083705530350539032307102973340e-5...
(700000,700002): ||A-B||^2 = 1.2509465591445586788670901809680683589854976403575e-6...
(700001,700002): ||A-B||^2 = 1.1143793855670105553693994785670010814039982860088e-2....
```

If the common owner `T''` is unstable, this component already supplies an unwanted maximum. If it is not, the three distinct opposite endpoints are forced unstable. The protected vertex `(2024,2377,500004)` is disjoint and independently strict. Consequently

```text
U>=2
```

throughout every fixed-incidence/external-positive endpoint chamber retaining these signs. Escape requires deletion of the complete triangle or a simultaneous reversal of at least one external arrow channel; a single diagonal flip does not address all three channels.

## 11. Attempts and limits

The search layer examined 110,900 selected finite proposals across fixed stable/saddle designs, random second-stage cells, local two-stage systems, chain-feasibility tests, old-stable replacement, radius-gap screens, determinant-one metric perturbations, and three-/four-corrector searches. No strict `(1,1,0)` proposal was promoted. These files are retained only as discovery evidence; they do not establish exclusion outside the exact endpoint chamber and named chronology path.

The exact claims are limited to:

1. the materialized 3,501-row endpoint and its `2^-100` open topology/mechanics box;
2. the one-boundary disk exchange between the exact predecessor and endpoint;
3. the exact nine-tetrahedron two-stage 3-ball;
4. the exact five-edge internal-arrow ledger;
5. the exact natural-chord chronology witness; and
6. the fixed-incidence/external-positive forcing theorem for `T''`.

No global nonexistence claim is made.

## 12. First genuinely unclassified successor

The first branch-local nonrepeating successor is a **one-boundary three-stage braided triangular-prismatic/cubical or four-octahedron terminal 3-ball**, or a smaller strictly stronger equivalent. It must in one communicating incidence event:

- delete all three true-edge channels of `T''=(700000,700001,700002)`;
- kill `S700003`, `H(1838,700003)`, and `H(2627,700003)`;
- preserve `S3911` and `U(2024,2377,500004)`;
- include a geometrically distinct antibirth return belt so every potential new internal true edge has at least one preassigned nonpositive external arrow at one endpoint;
- solve the three volume moments only after reserving independent channel, stable/saddle, and timing controls.

The smallest robust realization indicated by this endpoint uses at least one additional connected support beyond the current four, or four supports together with coordinated motion/deactivation of the current triangle and stable-side rows. One cell must break the three-edge forcing component, a second must kill the stable/two-saddle star, and a third communicating return cell must carry an independently tunable antibirth inequality. This is a branch-local frontier, not a proof of global topological minimality.

## 13. Independent verification and mesh

`src/verify_independent.py` is a clean-room verifier: it imports no search evaluator. It regenerates the exact source, checks all Cramer equations, face cycles and true edges, rebuilds the parent/endpoint symmetric difference, verifies exact `M=Vc`, reconstructs the nine-tetrahedron three-ball, binds the complete internal-arrow ledger and forcing theorem, checks the chronology overlap, and binds the mesh hashes. Its marker is

```text
BRIGHT_NOVA91_TWO_STAGE_INDEPENDENT_CLEAN_ROOM_RECONSTRUCTION_PASS.
```

The own-centred OBJ has 3,248 vertices and 1,626 maximal polygon faces. Its polygon boundaries reproduce exactly all 4,872 true edges. The STL has 6,492 consistently oriented triangles. Both reload watertight and connected; the OBJ volume is `5.339724646734571`, and its reconstructed centroid norm is below `7e-16`.

Use

```bash
./verify_all.sh
```

for the bundled fast exact/independent/mesh replay, or

```bash
BN91_RECOMPILE=1 BN91_DEEP=1 ./verify_all.sh
```

for a complete native source rebuild and byte comparison of the canonical exact/MPFR reports.

## Final status

```text
WINNER                                           NO
DISPOSITION                                      EXACT NONWINNER
PARENT SUPPLIED / ACTIVE                         3497 / 1624
ENDPOINT SUPPLIED / ACTIVE                       3501 / 1626
ENDPOINT PRIMAL (V,E,F)                          (3248,4872,1626)
ENDPOINT CLASS                                   (2,2,2)
INTENDED S3911 / U(2024,2377,500004)             PRESERVED
ALL THREE PREDECESSOR T' CHANNELS                DELETED
PREDECESSOR EXTRA STABLE AND TWO SADDLES         DELETED
ONE-BOUNDARY DISK EXCHANGE                       EXACT PASS
CONNECTED POSITIVE-VOLUME TWO-STAGE 3-BALL       EXACT PASS
NEW INTERNAL-EDGE EXTERNAL-ARROW LEDGER          COMPLETE
SIGN-FIRST REQUIREMENT                           FAILS ON T''
NAMED NATURAL-CHORD DEATH-BEFORE-BIRTH           FAILS EXACTLY
NEW FORCING TRIANGLE                             (700000,700001,700002)
FIXED-INCIDENCE TERMINAL CHAMBER                 U>=2
EXACT ORDINARY VOLUME AND THREE MOMENTS          PASS
FULL IRREDUNDANT H/V/E                           PASS
FULL FACE/VERTEX/FOUR-COMPONENT EDGE AUDIT       PASS
OPEN ALL-SUPPLIED-COORDINATE BOX                 2^-100
INDEPENDENT CLEAN-ROOM REPLAY                    PASS
WATERTIGHT OBJ/STL                               PASS
GLOBAL NONEXISTENCE CLAIM                        NONE
NEXT CELL                                        THREE-STAGE BRAIDED PRISMATIC/
                                                 CUBICAL OR FOUR-OCTAHEDRON 3-BALL
```


## 14. Reproducible archive and current-run verification

Download the complete exact archive (`Bright_Nova_91_two_stage_terminal_exact_NONWINNER.zip`)

```text
archive bytes    = 9377181
archive SHA-256  = e5910fb80217d4080726f33cbbc4cf021ca7c42547be5af1919c9f52bf7a0605
manifest SHA-256 = ce6113ba8f439572e6372edf3355371b91fa485435b08ba4f8702dab34b1837a
```

The ZIP passed an independent archive-integrity test. A clean extraction passed every manifest binding and a fresh bundled replay on the extracted copy ended with

```text
BRIGHT_NOVA91_FAST_EXACT_ALL_SUPPLIED_HULL_PASS rows=3501 active=1626 facets=3248 edges=4872 checks=11361504
BRIGHT_NOVA91_TWO_STAGE_INDEPENDENT_CLEAN_ROOM_RECONSTRUCTION_PASS
BRIGHT_NOVA91_TWO_STAGE_WATERTIGHT_DISPLAY_MESH_PASS
ALL_BRIGHT_NOVA91_TWO_STAGE_TERMINAL_VERIFIERS_PASS
```

The fresh fast replay completed in 21.76 seconds. I also attempted a second full native recompilation/deep replay in this continuation, but the current execution environment terminated that run before completion. Accordingly, the newly repeated evidence is the fast exact-hull/clean-room/mesh suite; the archive separately contains the already completed canonical exact-hull, GMP mass, MPFR full-cone, interval, forcing, arrow-ledger, and chronology outputs, their native sources, transcripts, and SHA-256 bindings.
