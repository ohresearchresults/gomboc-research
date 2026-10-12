# figure-0245

AI research report · 2026-09-03 UTC

---

# Keen Quartz 89 — exact M42 T37 escape continuation

## Verdict

**EXACT NONWINNER. No literal homogeneous convex polyhedral Gömböc was obtained.**

The acceptance gate remains an explicit finite uniform-density convex polyhedron evaluated at its own exact ordinary-volume centroid, with strict `(S,U,H)=(1,1,0)`, complete exact incidence and full-normal-cone mechanics, independent verification, and matching OBJ/STL. Near-solutions and auxiliary-centre bodies do not qualify. :contentReference[oaicite:0]{index=0}

I advanced the supplied T37 state through a certified topology-changing lineage and obtained a new exact open descendant, but the Euler-neutral stable–saddle pair transfers once more. The strongest exact endpoint produced here is

```text
supplied rows        96
active vertices      67
true edges           181
maximal faces        116
Euler characteristic 2
complexity            362
(S,U,H)              (2,1,1)
```

Its strict equilibria are

```text
stable maximal faces:
  [0,1,...,16]
  [258,259,6001]

unstable vertices:
  8

saddle true edges:
  (248,6008)
```

Every T37-labelled residual feature is absent: stable `[198,3000,1025]` is not a maximal face, saddle `(1027,3001)` is not a true edge, and the intermediate row-54 and active-connected pairs have also been replaced. This is therefore a genuine exact advance beyond T37, not a relabelling of its old packet. It is nevertheless not a Gömböc.

## Exact mass and own centring

The endpoint's exact ordinary volume is the positive rational number recorded without truncation in `certificate.json`; numerically,

```text
V = 1333.4468159975213...
```

The full exact value is

```text
1737483977058676422998820091555523013731565098513477848934632502020430699039739816933521883631796755630789005558354553976755958923410863918701765201371994929669444209561804667897362688258437562649797922055735752260651952569535787120906809923559
/
1303002081683253477727980338410408126597782765187261293205023564485331541121872358542421700678491841093577579242663201248873516357890123016571441207887626291770182375376482745247067939708766035112257126400000000000000000000000000000000000000.
```

An exact oriented-boundary tetrahedral sum gives the uncentred first moments and centroid. Translation by the exact negative centroid then gives

```text
translated first moments = (0,0,0) exactly.
```

The finite V- and mass data are in:

- [Principal exact certificate](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/certificate.json)
- [Supplied and active exact V-data](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/vertices_input_exact.csv)
- [Exact own-centred V-data](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/vertices_centered_exact.csv)
- [Exact constructor](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/build_exact_endpoint.py)

Inherited coordinates that were not moved retain the parent's exact rational values. Each genuinely moved binary64 coordinate is interpreted as its exact dyadic rational; after that conversion, hull, mass, incidence, and mechanics calculations use exact rational arithmetic rather than floating labels.

## Complete actual incidence and mechanics

Exhaustive exact reconstruction gives all 96 supplied rows, 67 active extreme vertices, 29 strictly inactive rows, 116 irredundant maximal supporting planes, and 181 true edges. The closed connected boundary satisfies

```text
67 - 181 + 116 = 2.
```

The exact strict margins are

```text
minimum active nonincidence          4.239695467008070e-6
minimum inactive-row separation     3.793098743563745e-4
intended base stability              9.398837936756806e-1
replacement stable margin            4.120806290361034e-6
closest nonstable clearance          1.750526282904896e-8
U8 margin                             1.716917199230891e-1
closest nonunstable clearance        9.955599345804903e-9
replacement saddle margin            4.120336838375030e-6
closest nonsaddle clearance          1.094624045657761e-9
```

Every maximal face, every active vertex, and every true edge is audited. The edge ledger includes both segment components and both incident-normal coefficients for all 181 edges; no edge is classified from a single selected witness.

- [Irredundant exact H-representation](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/H_irredundant.json)
- [Maximal-face cycles](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/face_cycles.json)
- [True-edge incidence](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/true_edges.csv)
- [Complete face-cone mechanics](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/faces_full_cones.json)
- [Complete vertex-cone mechanics](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/vertices_full_cones.json)
- [Every four-component true-edge cone](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/true_edges_full_cones.json)

## Exact transition lineage from T37

The transition lineage was rebuilt from four exact face lattices rather than inferred from equilibrium labels.

### Stage 1 — T37 to row-54 escape

The exact T37 and row-54 lattices have 62 common maximal faces. The exchange removes 102 T37 faces and inserts 70 row-54 faces. Both changed complexes are dual-connected, have Euler characteristic `-1`, and have the same set of 32 boundary edges.

This is a connected pinched multi-boundary whole-component exchange. It is **not** one elementary regular-subdivision wall, and I do not claim otherwise. It removes T37 rows

```text
54,247,1027,1028,1029,3000,3001
```

and inserts rows `5000,...,5006`. The T37 stable face `[198,3000,1025]` and saddle `(1027,3001)` are absent on the row-54 side. The exact row-54 body is `(86,216,132)`, strict `(2,1,1)`, with transferred pair `[258,5000,1025]` and `(248,5006)`. This independently recovered exact result and its radial obstruction were also recorded in the shared journal. :contentReference[oaicite:1]{index=1}

### Stage 2 — row-54 to active connected shared volume

The row-54 and active-connected lattices have 64 common faces. Their removed and inserted portions are connected disks with respectively 68 and 52 faces, Euler characteristic one, and the same simple 38-edge boundary cycle.

All six new rows

```text
6001,6004,6006,6007,6008,6009
```

are active. They form a rank-four positive-volume regular cell, and

```text
6001 - 6004 - 6007 - 6009
```

is a literal true-edge route from the stable side to the saddle side. The old row-54 stable and saddle are absent. The exact shared-volume endpoint is `(68,182,116)`, strict `(2,1,1)`, with transferred pair `[257,258,6001]` and `(248,6009)`. Its full exact construction, 18-coordinate `2^-36` chamber, clean-room reconstruction, and meshes were independently integrated in the later journal. :contentReference[oaicite:2]{index=2}

### Stage 3 — active-connected endpoint to the present endpoint

The present exact descendant deactivates old row `73`, rebuilds the full incidence lattice, and moves the pair to `[258,259,6001]` and `(248,6008)`. It has a separate 18-dimensional exact preserving box. The active-connected and present face lattices have 92 common maximal faces, with 24 removed and 24 inserted.

This third step is certified as an exact open descendant, not promoted as one elementary circuit wall.

Consequently the complete result is an exact **two-stage full-dimensional escape chain plus an exact open descendant**, not the requested single T37-to-winner cancellation wall. The distinction is encoded explicitly in the certificate.

- [Exact transition-lineage certificate](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/transition_lineage_certificate.json)
- [Lineage certificate builder](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/build_transition_lineage_certificate.py)
- [Independent lineage replay](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/verify_transition_lineage.py)
- [Independent lineage replay transcript](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/verify_transition_lineage.log)

The independent replay ends with

```text
INDEPENDENT_EXACT_TRANSITION_LINEAGE_PASS
T37-row54 common/rem/add/boundary 62 102 70 32
row54-active common/rem/add/boundary 64 68 52 38
active-current common/rem/add/boundary 92 24 24 32
```

## Complete external-arrow carrier theorem

I enumerated the exact external-arrow data for all 181 primal true edges, equivalently every adjacent pair of polar vertices. The census finds six all-external-positive forcing edges. Four are incident with the intended base and account for that intended stable feature. Exactly two are nonbase forcing edges:

```text
(258,6001)
(259,6001).
```

For edge `(258,6001)`, the incident primal faces are

```text
[257,258,6001]
[258,259,6001].
```

Every nonmutual outgoing polar support at both endpoints is strictly positive. The two mutual supports satisfy the exact identity

```text
sigma(A→B) + sigma(B→A) = ||q_A-q_B||² > 0.
```

At the endpoint their approximate values are

```text
sigma(A→B)  = +1.4010578706e-10
sigma(B→A)  = -1.0410157857e-10
sum         = +3.600420849e-11.
```

Thus at least one endpoint of the polar true edge is unstable, so at least one of the two corresponding primal maximal faces is stable. The same argument applies to `(259,6001)`, whose mutual-support sum is much more robust, approximately `2.280108993e-4`.

Therefore every strict realization retaining the current incidence and all listed external-arrow signs has an additional stable face besides the protected base:

```text
S >= 2.
```

This is a chamber theorem, not merely an endpoint classification. Coordinate polishing inside this sign cell cannot win.

- [Complete exact external-arrow census](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/complete_external_arrow_census.json)
- [Focused forcing-edge theorem](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/polar_forcing_edge_certificate.json)
- [Independent census builder](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/build_external_arrow_census.py)

The exact census reports

```text
faces 116
edges 181
forcing edges 6
nonbase forcing edges [(258,6001),(259,6001)].
```

This confirms the broader run's strengthened design rule: external-arrow antibirth conditions must cover every inserted edge and every inherited edge whose incident star changes, not only the nominal new carrier. :contentReference[oaicite:3]{index=3}

## Exact perturbation neighbourhood

A nonzero 18-dimensional all-coordinate box is certified. The three coordinates of each of

```text
231,236,241,246,251,256
```

vary independently through

```text
|delta coordinate| <= 2^-140.
```

Outward exact rational interval arithmetic recomputes an enclosure of the body's own centroid and certifies, throughout the complete box:

- the same supplied-versus-active status;
- the same maximal faces and true edges;
- every active nonincidence sign;
- every face component;
- every vertex-cone support;
- all four components of every true-edge cone;
- the exact strict class `(2,1,1)`.

- [Exact perturbation-box certificate](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/perturbation_box_certificate.json)
- [Independent interval verifier](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/verify_interval.py)

The verifier reports

```text
EXACT_18D_PERTURBATION_BOX_PASS radius=2^-140.
```

## Exact local deactivation atlas

The local set

```text
{257,258,259,6001,248,6008,1026,6009}
```

was rebuilt after no deletion, each singleton deletion, and every unordered pair deletion: 37 exact full-hull cases in total. Every case recomputes the active hull, ordinary centroid, maximal faces, true edges, and exhaustive mechanics. None is `(1,1,0)`.

Representative transfers include:

```text
delete 6001:
  stable transfers to [198,244,6004]
  saddle remains (248,6008)

delete 6008:
  stable remains [258,259,6001]
  saddle transfers to (248,1026)

delete 248 or 1026:
  an extra unstable vertex and a second saddle appear

delete 6001 and 6008:
  stable becomes [198,244,6004]
  saddle becomes (248,1026)
```

Deleting one left carrier and one right carrier therefore does not suffice. This closes only the stated 37 actual subhulls, not arbitrary simultaneous row motion or a new prismatic cell.

- [Exact 37-cell deletion atlas](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/exact_local_deletion_atlas.json)
- [Atlas constructor](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/build_exact_local_deletion_atlas.py)
- [Atlas replay transcript](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/build_exact_local_deletion_atlas.log)

The transcript ends with

```text
EXACT_LOCAL_SINGLE_AND_PAIR_DELETION_ATLAS_PASS 37 cases.
```

## Discovery searches and their rigorous scope

Numerical continuation produced the exactified endpoint above after multiple actual-cell changes. A later coherent numerical state reached a `(3,2,3)` block near `3.0e-6`, containing the left stable fan and the right tetrahedral/K4 star, but no open `(1,1,0)` chamber.

The right local set

```text
{248,1026,6008,6009}
```

is a true `K4`: all six pairwise edges are actual true edges. Consequently its obvious internal diagonal exchange is unavailable. The left ordinary crossing of `(258,6001)` transfers the stable feature to a large neighboring face rather than eliminating it.

A direct eight-support double-prism discovery parameterization was also tested. Its broad samples created many new stable, unstable, and saddle features; a tighter differential-evolution run did not finish with a usable candidate. These searches are discovery evidence only. They do not rigorously exclude the next topology.

## First genuinely unclassified topology: `KQ89-DP2`

The smallest evidence-supported nonrepeating topology is a changed-diagonal, non-star, internally linked double-prism/double-octahedral three-ball. It is not another frozen-boundary page.

### Components that must be changed together

Left forcing component:

```text
vertices {257,258,259,6001}
forcing edges (258,6001), (259,6001)
current stable [258,259,6001]
adjacent relay [257,258,6001]
```

Right saddle component:

```text
K4 on {248,1026,6008,6009}
current saddle (248,6008)
incident faces [248,6008,1026] and [248,6009,6008]
```

Route attachment:

```text
{228,6004,6007}
```

### Required event

One rebuilt full-dimensional cell must:

1. delete or change both nonbase forcing edges `(258,6001)` and `(259,6001)`, or reverse a certified external arrow at each surviving forcing channel;
2. move or deactivate at least one member of `{258,259,6001}`;
3. simultaneously move or deactivate at least one member of `{248,1026,6008}` and replace both incident faces of the current saddle;
4. link the left and right pages through an actual interior quadrilateral, interior edge, or shared tetrahedral face—not merely a boundary route;
5. remain attached to the old route sector through `228` and the active rows around `6004,6007`;
6. preserve the stable base `[0,...,16]` and unstable vertex `8`;
7. assign at least one nonpositive external arrow to every new or inherited star-changed internal edge before activation;
8. cross the stable and saddle death sheets before any replacement face, vertex, or edge becomes an equilibrium;
9. reserve the three ordinary first moments as dependent equations and retain at least three independent timing/antibirth controls afterward.

The robust combinatorial budget is eight connected new extreme supports arranged as two triangular prisms sharing an interior quadrilateral. A six-support realization remains plausible only if it simultaneously moves old rows such as `258` and `248` or `1026`. The completed exact evidence excludes leaf buttresses, inactive arcs, one-boundary strips, serial stellar insertions, same-incidence motion of `6001`, and all singleton/pair local deletions; it does not exclude `KQ89-DP2`.

## Independent verification and watertight mesh

The clean-room verifier does not replay asserted equilibrium labels. It reads the final exact V-data, reconstructs supporting planes and incidence, recomputes exact ordinary mass and centroid, audits every face, vertex, and four-component edge cone, rebuilds the complete external-arrow census, and checks mesh parity.

- [Independent exact verifier](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/verify_independent.py)
- [Independent verification transcript](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/verify_independent.log)
- [GMP all-triple hull verifier source](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/verify_exact_hull_gmp.cpp)
- [GMP verification transcript](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/verify_exact_hull_gmp.log)
- [Watertight OBJ](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/body.obj)
- [Watertight STL](sandbox:/mnt/data/Keen_Quartz_89_M42_active_pair_exact_NONWINNER/body.stl)

The independently reconstructed display mesh has 67 vertices, 130 triangles, and 195 mesh edges; every mesh edge has multiplicity two and the mesh Euler characteristic is two.

The clean-room transcript records

```text
PASS exact supplied/active reconstruction: 96 supplied, 67 active, 29 inactive
PASS complete actual boundary incidence: 67 vertices, 181 true edges, 116 maximal faces, Euler 2
PASS exact translated first moments 0 0 0
PASS exhaustive full normal-cone class 2 1 1
PASS complete exact polar external-arrow census
PASS watertight OBJ/STL parity
ALL_INDEPENDENT_EXACT_M42_ACTIVE_PAIR_CHECKS_PASS
```

The GMP checker independently exhausts all `C(96,3)=142880` row triples and more than 2.6 million exact support signs.

## What changed relative to the supplied journal

The supplied journal ended at exact T37 with residual pair `[198,3000,1025]` / `(1027,3001)` and the K7 lower bounds. This continuation adds:

- an exact lineage through the row-54 whole-component exchange;
- an exact one-boundary positive-volume rank-four shared cell with every inserted route row active;
- a smaller exact open descendant `(67,181,116)`;
- literal absence of every T37, row-54, and immediate active-connected residual label;
- a complete external-arrow census identifying the two-edge forcing component that now proves `S>=2` throughout the present chamber;
- an exact 18-dimensional perturbation box;
- an exact 37-cell singleton/pair deletion atlas;
- an independently replayed transition certificate distinguishing the true positive-volume stage from the pinched multi-boundary stage;
- the first sharply delimited non-star double-prism topology not covered by those certificates.

## Honest completion boundary

No strict `(1,1,0)` body was found, so there is no Gömböc completion ticket. The current endpoint is an exact full-dimensional successor and a reusable obstruction object, but its replacement stable face and saddle are strict and positive. The T37-to-current lineage is not one single regular-subdivision cancellation wall; it contains a connected pinched whole-component exchange followed by a genuine one-boundary positive-volume regular cell and an exact open descendant.

The endpoint files and verifiers are materialized individually. A consolidated ZIP, final manifest, and single `RUN_ALL.sh` wrapper for this third continuation were not assembled before the execution boundary. The exact constructors, certificates, independent verifiers, and meshes needed to reproduce and audit the mathematical claims are nevertheless present at the linked paths above.
