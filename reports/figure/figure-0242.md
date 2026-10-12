# figure-0242

AI research report · 2026-09-03 UTC

---

# Vivid Atlas 32 — P9-XG10 five-row carrier-free full-star determination

## Verdict

**EXACT FINITE NONWINNER.** I did not obtain the requested strict own-centroid `(S,U,H)=(1,1,0)` homogeneous convex polyhedral Gömböc.

I did obtain and independently verify the first five-row successor in this branch that satisfies the prescribed **edge-level carrier-free condition**: every inserted or inherited star-changed nonprotected true edge has a strictly negative external-arrow witness. The complete P9-XG9 residual packet and its forcing edge are deleted in one connected positive-volume full-star event. The endpoint nevertheless remains strict `(2,2,2)` because the packet reappears as a **singleton/full-row-star carrier at `G`**, rather than another external-positive edge component.

This advances exactly the journal frontier. P9-XG9 was an exact complexity-54 `(2,2,2)` endpoint whose stable `W2` was forced by star-changed edge `W2-W3`; the journal required a five-row carrier-free double-bipyramid or stronger connected full-star replacement with at least six post-moment controls. The global acceptance gate remains a finite uniform-density body at its own exact volume centroid with one stable maximal face, one unstable vertex, no saddle edge, complete actual incidence, positive margins, independent verification, and matching meshes.

## Exact finite construction

For every supplied row `q_i`, define

```text
P_raw = {x in R^3 : q_i·x <= 1 for every i}.
```

Let `c` be the exact ordinary-volume centroid of `P_raw`. The physical homogeneous body is

```text
P = P_raw - c,
```

with exact own-centred support rows

```text
H_i = q_i/(1-q_i·c).
```

The endpoint has 27 supplied rows. Exactly 12 are active and irredundant:

```text
T27, TR, SU, SC1, SA5, S102, G, V0, V1, V2, V3, V4.
```

The 15 strict inactive supplied rows are

```text
M, N, X0, X1, X2, X3, Y0, Y1,
Z0, Z1, Z2, W0, W1, W2, W3.
```

### Active exact raw support rows

```text
T27 = (-7125242734162057/140737488355328,
         265769074670437/35184372088832,
        -63255401657691/70368744177664)

TR   = (-892363419092795/281474976710656,
        -235941426090029/140737488355328,
        -528766574131575/140737488355328)

SU   = (-544131479513675/140737488355328,
         -96790958131853/35184372088832,
          118288508214145/140737488355328)

SC1  = (-119/64, -477/64, -239/64)
SA5  = (-379/64, -497/64, -57/8)
S102 = (-399/16, 567/32, 67/8)

G    = (1595031506620615/70368744177664,
          69636553284589/35184372088832,
          72284311426759/70368744177664)

V0   = (603/1024, -2151/1024, -909/256)
V1   = (-4347/1024, 971/256, 3639/1024)
V2   = (-4609/1024, -13/256, 319/128)
V3   = (-319/32, -7889/1024, -4313/1024)
V4   = (433/512, -4015/1024, 59/256).
```

All 27 rows, including the scaled inactive history rows, are expanded in `input_rows_exact.json`. Its SHA-256 is

```text
22a2cfc94f49f6df3636f40c25e811340eaf2d9fd4fd59afb68b59c512540773.
```

## Exact predecessor reconstruction

The embedded original P9-XG9 source reconstructs from all 22 supplied rows as

```text
Q:(V,E,F)=(11,27,18)
P:(V,E,F)=(18,27,11)
complexity=54
class=(2,2,2).
```

Its equilibria are exactly

```text
stable faces:      T27, W2
unstable vertices: T27/SU/W0, TR/S102/G
saddle true edges: SA5-W2, S102-W0.
```

The external-positive forcing edge is `W2-W3`.

For the connected full-star event I use an exact homothetic pre-event copy with raw support rows scaled by `1/64`. This scales the primal by `64` while preserving the complete face lattice, all equilibrium classifications, and every strict sign. The five future rows `V0..V4` are present but strictly interior in this pre-event system.

This is deliberately a **stronger global full-star replacement**, not a claim of a small local deformation inside the original `2^-22` XG9 box.

## Complete actual endpoint H/V/E incidence

Every one of the `C(27,3)=2925` candidate row triples was solved exactly. Precisely 20 are feasible. The actual endpoint is simple and has

```text
Q:(V,E,F)=(12,30,20)
P:(V,E,F)=(20,30,12)
complexity=60
Euler checks: 12-30+20=2 and 20-30+12=2.
```

### All 20 actual Q facets / primal vertices

```text
 0  T27/TR/SA5
 1  T27/TR/S102
 2  T27/SU/SC1
 3  T27/SU/S102
 4  T27/SC1/SA5
 5  TR/SA5/V0
 6  TR/S102/G
 7  TR/G/V0
 8  SU/SC1/V3
 9  SU/S102/V2
10  SU/V2/V4
11  SU/V3/V4
12  SC1/SA5/G
13  SC1/G/V4
14  SC1/V3/V4
15  SA5/G/V0
16  S102/G/V1
17  S102/V1/V2
18  G/V1/V2
19  G/V2/V4
```

### All 30 true Q edges / dual true primal edges

```text
T27-TR   T27-SU   T27-SC1  T27-SA5  T27-S102
TR-SA5   TR-S102  TR-G      TR-V0
SU-SC1   SU-S102  SU-V2     SU-V3    SU-V4
SC1-SA5  SC1-G    SC1-V3    SC1-V4
SA5-G    SA5-V0
S102-G   S102-V1  S102-V2
G-V0     G-V1     G-V2      G-V4
V1-V2    V2-V4    V3-V4
```

### All 12 maximal primal-face cycles

```text
T27   0 4 2 3 1
TR    0 1 6 7 5
SU    2 8 11 10 9 3
SC1   2 4 12 13 14 8
SA5   0 5 15 12 4
S102  1 3 9 17 16 6
G     6 16 18 19 13 12 15 7
V0    5 7 15
V1    16 17 18
V2    9 10 19 18 17
V3    8 14 11
V4    10 11 14 13 19
```

The exact minimum actual nonincidence slack is positive. Its certified interval lower bound over the endpoint box is

```text
0.006015786216445828.
```

A strictly positive four-row barycentric certificate places the origin inside the polar row hull, proving boundedness. The certified minimum projective denominator is

```text
0.7226210785899857.
```

## Exact ordinary volume, first moments, and own centroid

The exact rational volume, all three exact raw first moments, and all three exact centroid coordinates are expanded without truncation in

```text
exact_mass_centroid.json#/after
p9_xg10_edge_carrier_free_exact.json#/after/mass.
```

Their decimal evaluations are

```text
volume = 0.008366248352170732

raw first moments =
( 0.00011308600330109894,
 -0.0005267948147273295,
  0.0006915852373759193)

raw centroid =
( 0.013516931190759755,
 -0.06296667186441408,
  0.08266372312465223).
```

The exact verifier proves, coordinate by coordinate,

```text
M_x - V*c_x = 0/1
M_y - V*c_y = 0/1
M_z - V*c_z = 0/1.
```

Thus the translated physical body's ordinary-volume first moments are exactly

```text
(0/1,0/1,0/1).
```

## Five-row carrier-free connected event

The exact pre-event is similar to P9-XG9. Its complete row hull lies strictly inside the endpoint row hull. The exact minimum relative inclusion slack is

```text
0.4196545035230448.
```

The exact Q-hull volumes are

```text
pre-event Q volume = 0.37744405119838065
endpoint Q volume  = 2029.7404340159503
connected shell volume = 2029.362989964752 > 0.
```

The five new extreme rows form an exact triangular bipyramid with base

```text
V1-V3-V4
```

and apices

```text
V0, V2.
```

Its six supporting triangles are

```text
V0/V1/V3
V0/V1/V4
V0/V3/V4
V1/V2/V3
V1/V2/V4
V2/V3/V4.
```

A face-to-face positive-volume tetrahedralization is

```text
V0/V2/V3/V4   volume = 114634266117/2147483648
V0/V2/V1/V3   volume =  70365115265/2147483648
V0/V2/V1/V4   volume =  33649734935/2147483648.
```

The total exact bipyramid volume is

```text
218649116317/2147483648
```

or approximately `101.81642897287384`. The minimum tetrahedron volume is approximately `15.669378887396306`.

The three cells communicate around the internal spine `V0-V2`. Exact opposite-side determinants on the three internal pages have absolute minimum approximately

```text
94.01627332437783.
```

Crucially, `V0-V2` is **not** an actual Q true edge. It is an interior diagonal, so the nominal core spine cannot itself become a boundary edge carrier.

## Literal deletion of the complete XG9 packet

After the event all four inherited W rows are strict inactive supplied rows:

```text
W0 minimum support slack = 0.4196545035230448
W1 minimum support slack = 0.4470317023143974
W2 minimum support slack = 0.724974739456298
W3 minimum support slack = 0.6092755634014441.
```

Consequently:

```text
W2-W3 is not a true edge;
W2 is not an active or stable face;
T27/SU/W0 is not an actual vertex;
SA5-W2 and S102-W0 are not actual saddle edges;
no successor facet or edge contains any W row.
```

All four W rows occur only as strict interior supplied points. The old forcing component is therefore deleted, not renamed or carried along a surviving W page.

## Exhaustive full-normal-cone mechanics

At its exact own centroid, the endpoint is precisely

```text
(S,U,H)=(2,2,2).
```

Its equilibria are

```text
stable maximal faces:
  T27
  G

unstable vertices:
  TR/S102/G
  G/V2/V4

saddle true edges:
  SC1-G
  S102-G.
```

Every actual maximal face was tested against every true neighbouring support. Every actual vertex was tested in its full three-generator active normal cone. Every one of the 30 true edges was tested with all four strict components

```text
t, 1-t, alpha, beta.
```

Exact rational ledgers are expanded in `p9_xg10_edge_carrier_free_exact.json`, `H_supplied_exact.csv`, `V_exact.csv`, `maximal_faces.csv`, and `true_edges_full_cones.csv`.

Exact-point category minima, shown in decimal, are

```text
stable directed support:              171.95941885959184
nonstable-face exclusion:               8.676985992647436
unstable full-cone coefficient:          0.019942153053898
nonunstable-vertex exclusion:            0.007066895414546056
saddle full-cone component:              0.0022758976827921547
nonsaddle full-cone exclusion:            0.0004732744336213456.
```

## Complete external-arrow audit

The external-arrow ledger covers every actual true edge, both mutual arrows, every directed external arrow, every inserted or inherited star-changed classification, every active row's complete true-neighbour star, and every new-row vertex cone.

There are exactly 20 inserted or inherited-star-changed nonprotected true edges. **Every one has at least one strictly negative external arrow.** The certified minimum negative-arrow gap is

```text
8.668436807879985.
```

There is no non-`T27` true edge whose two endpoints have all external arrows positive:

```text
nonprotected external-positive edges = [].
```

Thus the requested edge-level carrier-free condition is met. The only external-positive edges in the whole graph are protected-root edges incident with `T27`.

## First remaining exact obstruction: singleton/full-star carrier

The complete row-star audit finds exactly two rows whose outgoing directed supports to **every** true neighbour are positive:

```text
T27
G.
```

For `G`, the exact minimum outgoing support is positive; its decimal value is

```text
942.6740709806943.
```

Therefore `G` is a strict stable maximal face throughout the complete row-star sign chamber. `T27` is independently stable. Hence

```text
S >= 2
```

throughout the certified endpoint chamber.

This breaks the previous edge-component pattern: there is no nonprotected external-positive edge component. The obstruction has contracted to the single all-positive row-star sink `G`. Edge-level anti-carrier inequalities are therefore insufficient; a winning topology must make the complete directed radius-ascent graph have `T27` as its unique sink.

The residual Euler-neutral block is

```text
extra stable:   G
extra unstable: G/V2/V4
saddles:        SC1-G and S102-G.
```

The target unstable lineage `TR/S102/G` survives unchanged.

## Six independent controls after exact moment elimination

The three projective-translation controls have exact centroid-residual Jacobian

```text
-I_3
```

and determinant `-1`.

Six independent shape variables remain:

```text
u1 = S102_z
u2 = V0_z
u3 = V1_z
u4 = V2_y
u5 = V4_x
u6 = V4_y.
```

They control

```text
1. first bipyramid-apex orientation;
2. second bipyramid-apex orientation;
3. G full-star stable-death primitive;
4. V4 coefficient at unstable vertex G/V2/V4;
5. G coefficient on saddle SC1-G;
6. G coefficient on saddle S102-G.
```

The exact `6x6` Jacobian determinant is nonzero; its decimal value is

```text
0.00036444853443529134.
```

Normalized singular values are

```text
1.6244942922774857
1.2454699737276456
0.9342136845208088
0.6630846211722188
0.5710704890761489
0.4138416511493356.
```

Thus neither moment rank nor post-moment shape rank is the remaining obstruction.

## Directed open perturbation chamber

Outward-rounded binary64 interval arithmetic certifies that all 81 endpoint raw support coordinates vary independently by

```text
|delta q_ij| <= 2^-23
             = 1.1920928955078125e-7
```

while preserving:

- all 20 actual vertices and exclusion of every other candidate triple;
- Q/P f-vectors `(12,30,20)` and `(20,30,12)`;
- every maximal cycle and all 30 true edges;
- strict inactivity of all 15 inactive rows;
- boundedness and all positive projective denominators;
- exact own-centroid enclosure and strict `(2,2,2)` mechanics;
- the positive-volume five-row triangular-bipyramid core;
- deletion of `W0..W3` and `W2-W3`;
- the complete edge-level anti-carrier property;
- the all-positive `G` row-star obstruction.

The certified volume interval is

```text
[0.008366147245024524, 0.00836634945931861].
```

Centroid intervals are

```text
cx in [ 0.013516486936603659,  0.013517375455924859]
cy in [-0.06296897535822205,  -0.06296436842619264]
cz in [ 0.08266001884830984,   0.0826674274907225].
```

Larger tested dyadic radii `2^-14` through `2^-22` failed closed. `2^-23` is the largest tested radius certified by this verifier.

## Independent clean-room replay

`verify_independent.py` imports neither the endpoint generator nor `exact_core.py`. Starting only from the exact input rows, it independently reconstructs:

- all 1540 candidate triples of the original 22-row XG9 source;
- all 2925 triples of both 27-row pre-event and endpoint systems;
- complete actual H/V/E incidence and maximal cycles;
- exact ordinary volume, first moments, centroid, and centred support rows;
- every face, vertex, and four-component true-edge equilibrium test;
- exact similarity normalization and strict full-hull nesting;
- the five-row triangular-bipyramid core and its communicating pages;
- strict inactivity of every W row and literal deletion of `W2-W3`;
- every inserted or star-changed edge arrow and every complete row-star arrow;
- the rank-six post-moment Jacobian;
- the directed perturbation certificate;
- OBJ/STL incidence multiplicities.

It ends with

```text
P9_XG10_INDEPENDENT_CLEAN_ROOM_PASS.
```

The OBJ has 20 vertices, 30 undirected edges, and 12 maximal polygonal faces, with Euler characteristic two and every polygon edge used twice. The STL has 36 triangles and 54 undirected triangle edges, each used twice. Both meshes are watertight.

## Numerical search evidence

Discovery campaigns, not promoted as impossibility proofs, included:

- 2,000,000 fixed-topology SPD metric samples: no state with `S=1,U=1`;
- 1000 topology-plus-metric five-row systems, 931 valid, each with 2048 metric samples: no target state;
- 3000 eight-row global proposals: 2628 valid, nine all-new-active edge-carrier-free endpoints, no winner;
- 3000 nested eight-row proposals: 2938 valid, 566 nested, no carrier-free all-new-active target endpoint;
- 70,000 structured five-row proposals: 12,118 valid, no winner;
- coupled-old-plane, great-circle, CMA-ES, differential-evolution, fixed-topology differentiable, and distributed-prism exploratory searches.

These observations guided exact seed selection only. They do not exclude other five-row placements or stronger coupled deformations.

## Smallest nonrepeating successor

The evidence-supported next topology is a **six-row target-star split / nonsimple closed-prism event** that replaces the current `G` star by two communicating descendants:

```text
G_T preserves the intended unstable triple TR/S102/G_T;
G_R absorbs and cancels G/V2/V4, SC1-G, and S102-G.
```

The event must have active positive volume before moment closure and must make `T27` the unique all-positive sink of the complete directed row-star graph. Merely forbidding all-positive edges is now proved insufficient.

A distributed seven-to-nine-row full-star prism is the direct fallback if one additional support cannot split the target and return roles of `G` while keeping both descendant stars connected through a shared interior cell.

## Scope and unresolved uncertainty

The exact theorem closes the displayed five-row triangular-bipyramid/full-star endpoint and its independent `2^-23` coordinate chamber. It does not exclude every five-row topology, every coupled-old-plane deformation, or the proposed six-row target-star split.

The construction uses an exact `1/64` homothetic copy of P9-XG9 as the pre-event boundary and then a stronger global full-star expansion. This is an admissible stronger connected positive-volume equivalent, but it is not a local path certificate from the unscaled XG9 endpoint.

No strict own-centroid `(1,1,0)` body is claimed.

## Artifact state

All core exact artifacts and individual verifiers are materialized. The endpoint generator, directed interval verifier, and independent clean-room verifier pass separately. The combined `RUN_ALL.sh` transcript currently stops after the interval stage because the aggregate invocation exceeded the available execution segment; a final clean-extraction ZIP/checksum pass was not completed. This packaging limitation does not change the individual exact and independent results above, but the directory has not yet been promoted as a clean one-command immutable archive.

### Exact data and certificates

- Exact supplied rows and provenance (`input_rows_exact.json`)
- Embedded exact P9-XG9 parent (`parent_p9_xg9_closed_cell_exact.json`)
- Complete exact endpoint ledger (`p9_xg10_edge_carrier_free_exact.json`)
- Exact volume, moments, and centroid (`exact_mass_centroid.json`)
- Positive connected-event certificate (`shared_event_exact_certificate.json`)
- Inherited-packet deletion certificate (`inherited_component_deletion_certificate.json`)
- Complete external-arrow ledger (`external_arrow_ledger.json`)
- External-arrow table (`external_arrow_table.csv`)
- Singleton/full-star obstruction certificate (`component_obstruction_certificate.json`)
- Rank-six control certificate (`control_rank_certificate.json`)
- Directed perturbation certificate (`perturbation_box_certificate.json`)

### Expanded H/V/E tables

- Exact supplied H table (`H_supplied_exact.csv`)
- Exact V table (`V_exact.csv`)
- Maximal-face cycles (`maximal_faces.csv`)
- True-edge full-cone ledger (`true_edges_full_cones.csv`)
- Before/after raw support rows (`raw_support_rows_before_after.csv`)

### Reproduction and independent verification

- Exact endpoint generator (`generate_endpoint.py`)
- Directed interval verifier (`certify_perturbation.py`)
- Independent clean-room verifier (`verify_independent.py`)
- Independent verification report (`independent_verification_report.json`)
- Independent verifier transcript (`verify_independent_output.txt`)
- Interval verifier transcript (`certify_perturbation_output.txt`)
- Package verifier (`verify_package.py`)
- Aggregate runner (`RUN_ALL.sh`)

### Meshes

- Watertight OBJ (`p9_xg10_edge_carrier_free_centered.obj`)
- Watertight STL (`p9_xg10_edge_carrier_free_centered.stl`)

### Discovery evidence

- Numerical exploration record (`numerical_exploration.json`)
- Promoted exact discovery seed (`discovery_carrierfree_exact_seed.json`)
