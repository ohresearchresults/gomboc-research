# figure-0195

AI research report · 2026-09-02 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Steady Quartz 25 — topology-first nonannular polar bridge

## Literal disposition

**EXACT NONWINNER.** I did not obtain a homogeneous convex polyhedral Gömböc. The strongest fully materialized object from this direction is an exact-dyadic nonannular-bridge endpoint at its own exact ordinary-volume centroid with strict class `(S,U,H)=(2,2,2)`, not `(1,1,0)`.

This applies the journal’s required successor topology rather than another annulus-preserving `K×[0,1]` transfer: the exact 335-row residual annulus and its 78-cycle-side complementary disk are removed together and replaced by a single connected seven-hub disk spanning the surviving 158-cycle interface. The former 78-cycle is internalized and deleted. The journal had left precisely this topology-first bridge open.

The result does not pass the global acceptance gate because it retains one Euler-neutral extra block. The gate requires strict own-centroid `(1,1,0)`, complete finite H/V data, exhaustive face/vertex/edge mechanics, positive strictness margins, independent verification, and a matching mesh.

## Materialized artifacts

- Compact result certificate (`result_summary.json`)
- Exact bridge-topology certificate (`nonannular_bridge_topology.json`)
- Six-packet coupling routes (`packet_coupling_routes.json`)
- Seven-shape-plus-three-moment control definition (`control_space.json`)
- Exact active polar H rows (`raw_polar_rows_integer.csv`)
- Deterministic supplied 3,488-row H representation (`supplied_endpoint_rows_integer.csv`)
- Exact rational primal vertices (`primal_vertices_exact.csv.gz`)
- All maximal-face cycles (`maximal_face_cycles.json`)
- Every true edge (`true_edges.csv`)
- Exact ordinary mass and centroid (`exact_mass_centroid.json`)
- Full directed-interval equilibrium audit (`full_interval_mechanics_radius_2^-100.json`)
- Exact all-supplied-row hull certificate (`exact_supplied_hull_report.json`)
- Exact topology-radius certificate (`exact_topology_radius_2^-100.json`)
- Independent reconstruction report (`independent_verifier_report.json`)
- Independent verifier source (`verify_independent.py`)
- Exact `cpp_int` hull verifier source (`verify_exact_supplied_hull.cpp`)
- Own-centred OBJ (`nonannular_bridge_own_centered.obj`)
- Watertight own-centred STL (`nonannular_bridge_own_centered.stl`)

## 1. Exact reconstruction of the source

The independent verifier reconstructs the supplied source as

```text
H rows / primal maximal faces: 3481
Q triangles / primal vertices: 6958
Q edges / primal true edges:   10437
primal surface triangles:      13912
Euler:                         3481 - 10437 + 6958 = 2
```

Its ordinary-volume centroid reconstructs numerically within `7.2e-16` of the source origin, consistently with the predecessor’s isolated moment certificate. Its exhaustive reconstructed mechanics are exactly

```text
stable rows:
  424
  3736

unstable facets:
  (2288,2394,2603)
  (1744,1779,2025)

saddle edges:
  (1490,1805)
  (2629,2910)
```

hence strict source class `(2,2,2)`.

The residual subcomplex has 335 rows, 434 triangular Q faces, 769 induced surface edges, Euler characteristic zero, and boundary cycles of lengths 78 and 158. The original 771-edge certificate consists of those 769 induced edges plus its two recorded graph chords `(3349,3524)` and `(3594,3769)`.

## 2. Explicit nonannular bridge combinatorics

Write the source Q sphere as

```text
D78 ∪ K ∪ D158,
```

where `K` is the 335-row annulus, `D78` is the complementary disk on the 78-cycle side, and `D158` is the complementary disk on the 158-cycle side.

The operation freezes `D158` and removes the connected union

```text
R = D78 ∪ K.
```

The exact removed complex has

```text
V = 2015
E = 5884
F = 3870
chi = 1
boundary = the complete former 158-cycle.
```

It contains every assignment packet and every original unwanted or protected equilibrium carrier involved in the residual block. The complete two old cycles and every packet-row membership are listed in `nonannular_bridge_topology.json`.

The replacement is one disk `B` with

```text
V = 165
E = 334
F = 170
chi = 1
boundary length = 158
new interior hub labels = 500000,...,500006.
```

Of its 170 triangles, 31 meet a new hub and 139 triangulate the remaining boundary-chord regions. The hub graph is connected. The endpoint Q sphere is therefore

```text
D158 ∪ B.
```

This is a genuine topology change relative to the prescribed residual patch: the annulus with two boundary components is absent, the old 78-cycle is no longer a boundary or an endpoint subcomplex, and only the 158-cycle remains as the gluing interface.

The six packet routes all enter the common replacement and then reach shared hub `500000`. Their short interface entries are:

```text
packet 1 -> 2775 -> 500001 -> 500000
packet 2 -> 3808 -> ... -> 1836 -> 500001 -> 500000
packet 3 -> 1807 -> 500005 -> 500000
packet 4 -> 2838 -> 2592 -> 500002 -> 500000
packet 5 -> outer interface -> new cap -> 500000
packet 6 -> old 78-cycle side -> outer interface -> new cap -> 500000.
```

The full exact graph paths are supplied in `packet_coupling_routes.json`.

## 3. Seven genuinely independent shape controls and three dependent moment variables

The deterministic supplied representation contains all 3,481 source rows plus seven new hub rows. Let `a=(a0,...,a6)`.

For each of the 1,857 rows in the removed source disk,

```text
q_r(a) = (1 - (3/28) sum_j a_j) q_r_source.
```

For each new hub,

```text
q_hj(a) = a_j q_hj_endpoint.
```

All 1,624 rows of the frozen `D158` component remain fixed.

Consequently:

```text
a=(0,...,0): exact 3,481-row source; the seven zero hub rows are inactive.
a=(1,...,1): every removed old row is scaled to 1/4 and is strictly inactive;
             all seven new hubs are active.
```

Every `a_j` acts on every removed source row and uniquely acts on hub `j`. Projection to the seven disjoint hub coordinate blocks proves that the supplied-row Jacobian has exact rank seven. Thus these are not seven serial local-star repairs hidden inside one parameterization.

The three dependent ordinary-centroid variables are `m=(mx,my,mz)` and satisfy

```text
F(a,m) = M(P_raw(a)) - V(P_raw(a)) m = 0.
```

They have the unique exact solution

```text
m(a) = M(P_raw(a)) / V(P_raw(a)).
```

Moreover

```text
dF/dm = -V I_3,
det(dF/dm) = -V^3 != 0,
rank(dF/dm) = 3.
```

The resulting moment-null shape manifold therefore retains all seven independent shape dimensions. The exact own-centred normalized H representation is

```text
qhat_i = q_i / (1 - q_i dot m),
qhat_i dot y <= 1.
```

## 4. Strongest exact endpoint

The irredundant active endpoint has

```text
(F,V,E) = (1631,3258,4887)
surface triangles = 6512
Euler = 1631 - 4887 + 3258 = 2
mechanical complexity C = 9774.
```

The active raw polar rows are exact dyadics

```text
q_i = (nx_i,ny_i,nz_i) / 2^69.
```

The supplied active-plus-inactive table uses a common denominator `2^109`. The exact `cpp_int` audit proves:

```text
supplied rows:                    3488
active rows:                      1631
strictly inactive old rows:       1857
Q support triangles:              3258
Q edges:                          4887
exact nonincident checks:         11,354,130
extra coplanar rows:              0
outside rows:                     0
connected facet dual:             all 3258 facets reached.
```

The smallest exact nonincident primal slack is

```text
1.4689227575116868179486308837739759907e-9.
```

The smallest exact inactive-row slack is

```text
0.6025649388414267213792261872409571420...
```

Every primal vertex is materialized as an exact Cramer rational in `primal_vertices_exact.csv.gz`. Every maximal polygon cycle and every true edge is listed separately.

## 5. Exact ordinary-volume centroid

The exact mass computation uses the exact dyadic H rows, exact Cramer vertices, and all 6,512 oriented boundary triangles. It performs exact arbitrary-precision rational tetrahedral summation, not floating recentering.

The exact volume has decimal readback

```text
5.3268546344578023827007792459667577704913147804652716826363701024429439457726311...
```

The exact ordinary-volume centroid of the raw body is

```text
cx = -0.066385933478035674687709495160990546352572931268341949321644794680280770143916765...
cy =  0.032165903343717409036211678185006205331246769697563962321069789815970170198149834...
cz =  0.060647765329432014210622849433424752597399742751668777876826754934720336138027341...
```

The complete reduced numerator and denominator of `V`, all three first moments, all three centroid coordinates, and `-V^3` are stored in `exact_mass_centroid.json`. The exact identities

```text
Mx - V cx = 0
My - V cy = 0
Mz - V cz = 0
```

are checked directly. Translation by this exact rational centroid therefore gives a uniform-density polyhedron whose ordinary-volume centroid is exactly the origin.

## 6. Exhaustive equilibrium audit

The directed outward interval audit perturbs every active raw H coordinate independently by `±2^-100`, recomputes interval vertices, mass, centroid, normalized supports, and all complete normal-cone tests, and finds no ambiguous feature.

The exact endpoint class is

```text
stable rows:
  3911
  500000

unstable facets:
  (1836,2775,500001)
  (2024,2377,500004)

saddle edges:
  (1802,500005)
  (2592,500003)
```

Thus

```text
(S,U,H) = (2,2,2).
```

The original two stable equilibria, both original unstable facets, and both original saddle edges are absent as equilibrium features. The operation cancels the complete original block but creates a new Euler-neutral block on the nonannular cap and its frozen interface.

The decisive interval margins throughout the full `±2^-100` box are:

```text
smallest positive stable margin:
  S500000 against 500001
  [0.00048668103019226908679604100227846,
   0.00048668103019226908680112833334115]

closest excluded stable margin:
  row 3912 against 3911
  [-0.00033576744188121358957404466106769,
   -0.00033576744188121358956939036935270]

smallest positive unstable component:
  facet (1836,2775,500001)
  [0.114636505816608137404786571682179,
   0.114636505816608137404789179493141]

closest excluded unstable component:
  facet (1807,1838,500005)
  [-0.026325672969637201426465038036682,
   -0.026325672969637201426429852968996]

smallest positive saddle component:
  edge (1802,500005)
  [0.0223623220584884875394351239847580,
   0.0223623220584884875394554316657935]

closest excluded saddle component:
  edge (1802,500006)
  [-0.00184415837610903545389165747101732,
   -0.00184415837610903545388423111019703].
```

The complete individual ledgers contain all 1,631 face tests, all 3,258 vertex-cone tests, and all 4,887 four-component true-edge tests:

- Stable ledger (`stable_margin_ledger.csv.gz`)
- Unstable ledger (`unstable_margin_ledger.csv.gz`)
- Saddle ledger (`saddle_margin_ledger.csv.gz`)

## 7. Positive strictness and topology radius

The exact determinant perturbation certificate proves that all 3,488 supplied row coordinates may vary independently by

```text
r = 2^-100 = 7.888609052210118054e-31
```

without changing the active set or H/V/E lattice. Its exact determinant safety factors are approximately

```text
facet-orientation safety: 2.776367369916583e24
nonincident-sign safety:   5.097836516104171e14.
```

The directed mechanics audit proves that after ordinary-volume recentering, the same coordinate box preserves strict class `(2,2,2)`. This gives a certified open nonwinner cell, not a point on or near an equilibrium wall.

## 8. Independent reconstruction and mesh

`verify_independent.py` imports no construction or search evaluator. It independently:

1. reconstructs the original 3,481-row source and its `(2,2,2)` mechanics;
2. reconstructs the 3,488-row supplied Q hull and its exact active set;
3. checks every exact Cramer vertex against its three exact H equations;
4. rebuilds all incidence cycles and all true edges;
5. independently recomputes volume, centroid, stable faces, unstable vertices, and saddle edges;
6. verifies the exact mass identities and interval enclosures;
7. reconstructs the source annulus complements and the 170-triangle nonannular cap;
8. validates the materialized all-row `cpp_int` certificate;
9. reruns the directed interval full-cone audit;
10. reloads and checks the meshes.

It ends with

```text
INDEPENDENT_NONANNULAR_BRIDGE_RECONSTRUCTION_PASS
```

The separate exact C++ verifier ends with

```text
INDEPENDENT_EXACT_SUPPLIED_HULL_PASS
rows=3488 active=1631 facets=3258 edges=4887 checks=11354130.
```

The OBJ has 3,258 vertices and 1,631 maximal polygon faces. The STL has 6,512 consistently oriented triangles, 9,768 undirected triangle edges, every triangle edge has incidence two, triangle Euler characteristic is two, and the reloaded mesh is watertight.

Principal mesh hashes are

```text
OBJ dcd1d58d19ea554116dc07d7e9692fa3bfee4549e1ab2568a9136a314d2c88a6
STL 1146e4054dca76bd6a2f9a649c4bbc30c883b4ff26c5393f53919774c6eb7783
```

## 9. Attempts to break the conclusion

### Global supplied-control path

Along the exact diagonal path `a0=...=a6=t`, the source and endpoint have different exact active sets and facet lattices, so continuity of the determinant polynomials forces combinatorial-wall crossings. A 101-point actual-hull scan observed 70 distinct topology signatures. Selected rebuilt mechanics were

```text
t=0.00  (2,2,2)
t=0.05  (7,3,8)
t=0.10  (8,3,9)
t=0.20  (7,4,9)
t=0.40  (5,4,7)
t=0.60  (9,2,9)
t=0.80  (3,2,3)
t=1.00  (2,2,2).
```

The sample count is numerical evidence; the necessity of crossing at least one wall follows rigorously from the distinct certified endpoint lattices.

### Broad seven-hub search

A deterministic 50,000-proposal search produced 12,484 valid all-active nonannular caps. Its class histogram began

```text
(2,2,2): 9332
(2,3,3): 1685
(2,4,4): 705
(3,2,3): 346
(3,3,4): 169
```

and contained no `(1,1,0)`, `(1,2,1)`, or `(2,1,1)` candidate. This is discovery evidence, not an exclusion theorem.

### Variable eight-to-twelve-hub search

A second deterministic 60,000-proposal search varied between eight and twelve connected cap hubs. It produced 6,069 valid all-active caps:

```text
(2,2,2): 4535
(2,3,3): 1259
(3,2,3): 156
(3,3,4): 68
(2,4,4): 34
other higher classes: 17.
```

Again there was no `(1,1,0)`, `(1,2,1)`, or `(2,1,1)` candidate. This also remains empirical evidence only.

### Moment-null differential test and post-wall rebuilding

At the accepted endpoint, the Jacobian of the four unwanted wall functions

```text
S500000,
U(1836,2775,500001),
H(1802,500005),
H(2592,500003)
```

with respect to the seven shape controls has numerical rank four, with singular values

```text
392.1811075828
44.3351508642
1.4286489980
0.2452131814.
```

Thus lack of first-order control rank is not the obstruction. The least-norm linear common-zero direction has norm about `0.45994`, but an actual hull rebuild reaches a topology event before any equilibrium-count reduction. Between sampled parameters `lambda=0.0375` and `lambda=0.04`, hubs `500002` and `500006` simultaneously become inactive. The class remains `(2,2,2)` and the saddle `(1802,500005)` transfers to `(1802,500001)`. Soon afterward the second saddle transfers from `(2592,500003)` to `(2592,500000)`, followed by additional U-H and S-H births.

A rebuilt-hull scan through `lambda=2`—allowing all those hub deactivations rather than rejecting them—still had componentwise minimum counts `(2,2,2)` and no winner sample. The complete diagnostic is here (`common_descent_postwall_scan.json`). It is not a global exclusion.

## 10. Residual obstruction

The exact statement is local and architecture-specific:

1. The accepted endpoint lies in a rigorously certified `±2^-100` open H-coordinate cell of strict class `(2,2,2)`. No object in that box is a winner.
2. The seven moment-null shape directions act independently, and the four unwanted equilibrium walls have full numerical differential rank four.
3. The common descent needed to approach those four walls is macroscopic relative to the certified cell.
4. Before the equilibrium walls can meet, the cap loses the two supports `500002` and `500006`, which are the local buttresses of the two terminal saddle channels.
5. Rebuilding after those incidence changes transports both saddle channels and then creates further pairs instead of reducing the Morse class.

Therefore the obstruction is **incidence preemption**, not insufficient moment-null dimension. No global theorem rules out a Gömböc in every nonannular replacement or in every continuation of this source.

## 11. Evidence-forced next volumetric topology

The smallest nonrepeating continuation is not another one-disk retriangulation and not a fixed-cell motion of the seven existing hubs. It must add a second finite-thickness cross-cap cell that keeps the two first-lost saddle buttresses in one common incidence circuit while the four equilibrium deaths are crossed.

The required terminal complex should contain a nonsimplicial triangular-prismatic or octahedral `2↔3 / 3↔2` bridge spanning

```text
saddle side A: 1802, 500006, 500005, 500001
saddle side B: 2592, 500002, 500003, 500000
```

and should share an interior edge or quadrilateral circuit directly between the `500006` and `500002` sides. At least two new extreme polar supports are needed so that loss of either old buttress does not collapse the cell into a serial carrier transfer.

The control budget should include, at minimum:

```text
1. death control for S500000;
2. death control for U(1836,2775,500001);
3. discriminator for H(1802,500005);
4. discriminator for H(2592,500003);
5. anti-inactivity control for the 500006 side;
6. anti-inactivity control for the 500002 side;
7. protected-channel discriminator retaining S3911 and U(2024,2377,500004);
8–10. the same three dependent ordinary-moment variables.
```

The actual hull, exact centroid, maximal-face lattice, and all four true-edge cone components must be rebuilt after each circuit crossing. This successor is evidence-forced by the first actual topology event; it is not claimed to be a theorem of minimality over arbitrary polyhedral constructions.

## Final determination

```text
WINNER:                         NO
DISPOSITION:                    EXACT NONWINNER
SOURCE:                         (F,V,E)=(3481,6958,10437), class (2,2,2)
SOURCE PATCH:                   335 rows, 771 certified graph edges,
                                434 triangles, annulus boundaries 78 and 158
NONANNULAR OPERATION:           remove K∪D78; insert one seven-hub disk on C158
SHAPE-CONTROL RANK:             7 exact
DEPENDENT MOMENT RANK:          3 exact
ENDPOINT:                       (F,V,E)=(1631,3258,4887)
ENDPOINT CLASS:                 (2,2,2)
EXACT OWN CENTROID:             materialized as reduced rational M/V
STRICTNESS RADIUS:              2^-100 in every supplied H coordinate
INACTIVE SEPARATION:            >0.6025649388414267
MINIMUM NONINCIDENT SLACK:      >1.4689227575116868e-9
INDEPENDENT VERIFICATION:       PASS
WATERTIGHT MESH:                PASS
GLOBAL NONEXISTENCE OBSTRUCTION: NOT PROVED
NEXT CELL:                      finite-thickness cross-cap nonsimplicial bridge
                                coupling the 500006 and 500002 saddle buttresses.
```
