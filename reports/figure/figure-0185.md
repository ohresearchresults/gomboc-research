# figure-0185

AI research report · 2026-09-01 UTC

---

# Quiet Raven 13 — exact AQ32 outlet handoff

## Literal disposition

**EXACT NONWINNER. No homogeneous convex polyhedral Gömböc was obtained.**

The strongest defensible endpoint is `AQ32-OUTLET-METRIC-EXACT`. It is a completely materialized exact-dyadic point polytope `Q` together with the interval-isolated own-centred polar

`P=(Q-s(Q))°`.

Its strict classes are

```text
Q relative to its unique Santaló point: (S,U,H)=(2,2,2)
P at its own uniform-volume centroid:    (S,U,H)=(2,2,2)
```

and therefore it does **not** meet `(1,1,0)`. The outlet-wide shared-cell cancellation was not completed as an exact endpoint; none of the numerical topology probes below is promoted to a Gömböc claim. The important advance over the durable journal is that the previously provisional robust numerical chamber is now an actual finite irredundant incidence cell with exact source rows, exact metric, grouped maximal faces, true edges, an isolated Santaló zero, exhaustive directed mechanics, inactive-row separation, a positive preserving box, independent verification, and watertight meshes. 

## 1. Exact parent and the true outlet-spanning lineage

The certified parent `AQ32-CR3D580` is already a genuine rank-three support-connected volumetric event, not a visual or surface-only interpolation. Its displacement field has exact rank three, 206 old candidates become interior, all 898 inserted rows are extreme, its volume changes by a nonzero exact rational, and the changed one-ring contains literal cross-sector true-edge paths. Two canonical paths are

```text
A: 11778 -> 22344 -> 11779 -> 22405 -> 11812 -> 22471
B: 11786 -> 22649 -> 11787 -> 22711 -> 11820 -> 22776
```

with every consecutive pair an actual true edge. 

That event removed the predecessor sectors `2/10` U–H packet and the predecessor terminal sectors `4/5` and `12/13` S–H packet, but left a new support-connected outlet union:

```text
direct changed-region packet: (S,U,H)_Q=(12,0,10)
first coarse-background packet: sectors 7/15 U–H ladder
```

The first direct stable face was face `57`, cycle `(14613,14880,14628)`, with margin about `0.006283919704543244`. The weakest direct saddle was `(14693,14888)` in sector `13`, with half-turn mate `(14686,14882)` in sector `5`. The first coarse unstable row was `13115` in sector `7`, margin `2.8077380615201448e-5`, paired with saddle `(13099,13115)`; row `13123` and edge `(13107,13123)` are the sector-`15` copies. 

The exact outlet-metric successor spans that residual union and compresses the global mechanics to two stable faces, two unstable vertices, and two saddles. It does not cancel the final Euler-neutral pair system.

## 2. Deterministic exact outlet generator

The endpoint is regenerated from the exact `AQ32-CR3D580` parent, whose coordinates have denominator `2^118`. The deterministic outlet recurrence uses the following half-sector ray starts:

```text
0.5:448, 1:448, 1.5:560, 2:559, 2.5:480,
3:545, 3.5:480, 4:497, 4.5:480, 5:550,
5.5:480, 6:556, 6.5:448, 7:448, 7.5:448
```

and ends:

```text
0.5:600, 1:745, 1.5:600, 2:700, 2.5:590,
3:620, 3.5:580, 4:620, 4.5:590, 5:620,
5.5:590, 6:620, 6.5:590, 7:730, 7.5:600.
```

The separator factor is `1.1`; the common post-radial coefficient is `-0.075`; the sector-`2` coefficient is `-0.005`. The complete supplied-versus-active ledger is

| layer | count |
|---|---:|
| certified parent rows | 23,799 |
| parent rows modified by the outlet recurrence | 1,898 |
| inserted candidate rows | 2,038 |
| total supplied Q candidates | 25,837 |
| final active/extreme Q rows | 22,033 |
| inactive Q candidates | 3,804 |
| active P halfspaces dual to Q rows | 22,033 |
| actual P vertices dual to Q maximal faces | 44,061 |

All final transformed Q coordinates are dyadic with common denominator

```text
2^150 = 1427247692705959881058285969449495136382746624.
```

`generate_AQ32_OUTLET_METRIC_exact.py` regenerates every candidate coordinate and the exact active selector rather than loading an unexplained floating hull. 

## 3. Exact dyadic SPD metric

The common linear map is the symmetric positive-definite rational matrix

```text
A = 2^-32 *
[[  1232442050,  -2997712012, -13328199580],
 [ -2997712012,   9338404416,  25704283391],
 [-13328199580,  25704283391, 197566781565]].
```

Its exact leading principal minors are

```text
1232442050
2522764975295004656
79228162239523321379821576910
```

and its determinant is

```text
79228162239523321379821576910 /
79228162514264337593543950336 > 0.
```

Sylvester’s criterion therefore proves strict positive definiteness. Approximate eigenvalues are

```text
0.014884594433381186
1.4289201361841837
47.01701317242988
```

with condition number about `3158.770189`. The covariance identities

```text
s(AQ)=A s(Q)
(AQ-A s(Q))°=A^-T (Q-s(Q))°
```

preserve exact incidence and hard-wire own-centredness rather than repairing the final body after scoring. 

## 4. Actual irredundant incidence cell

A floating hull is used only to seed a triangulation. Exact integer four-point predicates then perform `510` local `2↔2` repairs. The canonical exact boundary has

```text
Q: (V,E,F)=(22033,66092,44061)
P: (V,E,F)=(44061,66092,22033)
mechanical complexity V+E+F-2 = 132184.
```

The Q triangulation has `44,062` triangles. Exactly one triangulation diagonal, `(19609,19610)`, lies inside a coplanar stable square; it is removed from the true-edge list, leaving `44,061` grouped maximal faces and `66,092` actual true edges. Euler’s relation is exactly `2`.

The minimum nonzero adjacent exact orientation determinant is

```text
127147975046385277374519693584517482939106762318038021311082705465281036499853312.
```

Every one of the `22,033` selected rows is extreme. Complete expansions are stored in

```text
AQ32_OUTLET_METRIC_Q_vertices_exact.csv
AQ32_OUTLET_METRIC_Q_maximal_faces_exact.jsonl
AQ32_OUTLET_METRIC_Q_true_edges.csv
AQ32_OUTLET_METRIC_P_H_rows_root_box.csv.gz
AQ32_OUTLET_METRIC_P_vertices_root_midpoint_exact.csv.gz
AQ32_OUTLET_METRIC_P_maximal_faces.jsonl
AQ32_OUTLET_METRIC_P_true_edges.csv
```

so the result is not an unexpanded symbolic generator. 

## 5. Exact inactive-row separation

Every one of the

```text
3804 × 44061 = 167608044
```

inactive-candidate/maximal-face pairs was screened with directed error allowance, and the closest pair was checked exactly. The directed base-space boundary-distance lower bound is

```text
2.0746452679695718e-5.
```

The closest inactive candidate is source index `25140`, against maximal face `38`, cycle `[14219,14436,22004]`; its exact slack numerator is positive. Combining this with the exact metric eigenvalue bound gives transformed separation

```text
3.533640470250234e-8 > 0.
```

Thus no omitted supplied row becomes active and no claimed maximal face is an incidence-tolerance merge. 

## 6. Isolated normalized Santaló root and directed zero moments

Before the metric map, the unique Santaló point lies in a coordinate-radius `1e-50` box around

```text
(-0.000234926542667867094967708393703335020074732888481951433397544597236322850314183220655894810998132409,
  9.620940829881592940164834419631899943825797453232530943675890017284128484012824717326072045535058602e-17,
  1.486945817612702535006117400421781062077835178904573098117204960383007335570371389161412153116679782e-16).
```

After applying `A`, the exact transformed root lies in a coordinate-radius `1e-48` box around

```text
(-0.00006741223620420061769211916890644070601907218751762092007216931917923240927206962817287927160459085275126921275573039,
  0.000163969145831143541037072549607727254096259288290506636434931430460747274422659062219800852959973895418774978617176,
  0.0007290271686735955063474719020371877154102274478352416823050397618873792947693998622141271305634759308287117916322687).
```

At the recorded high-precision midpoint the directed ledger gives

```text
polar volume = 4.3017952080639279098106432130712745585525482875237435879505119471409586873718926419569043628544779831230089616
||M||/V      = 2.9091750312582468487027259673317461e-88
||F||        = 5.0058700835543815933008559750296741e-87
lambda_min(DF) >= 0.0526339591828357411426677807578372
root-ball radius <= 9.5107230413075722e-86.
```

Every projective denominator is directed positive throughout the root box:

```text
[0.0147853899086874700725357203350068,
 3.1664782717190501822193906968241820].
```

Positive definiteness of the Santaló Jacobian proves uniqueness. Hence there is a unique exact point inside the box at which all three first moments are exactly zero; the displayed midpoint residual is only the numerical enclosure used to locate it. An independent 80-digit implementation obtains normalized residual `4.8534347520311353e-76` and root-radius `1.5866929019276268e-73`, still deep inside the certified box. 

## 7. Exhaustive face, vertex, and full true-edge-cone audit

Every one of the `44,061` actual maximal Q faces, `22,033` full Q vertex tangent cones, and `66,092` true-edge normal cones was evaluated over the complete Santaló box. Edge classification uses all four directed cone components, not only an edge projection or one incident triangle.

### Positive Q features

| type | exact incidence | directed minimum margin |
|---|---|---:|
| stable face | face `5293`, cycle `[18760,18761,18776]` | `0.0012299184518639722` |
| stable face | face `15955`, cycle `[9784,9801,9817]` | `0.0006510066872722448` |
| unstable vertex | row `14432` | `37.41264640539945` |
| unstable vertex | row `14437` | `42.05606273485051` |
| saddle true edge | `(13283,14192)`, incident faces `(1342,1343)` | `0.5671949434331944` |
| saddle true edge | `(14645,15596)`, incident faces `(4058,8155)` | `0.2906126720486022` |

### Global decisive minima

```text
positive equilibrium minima:
  faces    0.0006510066872722448
  vertices 37.41264640539945
  edges    0.2906126720486022

closest excluded-feature clearances:
  faces    0.0006509163671786233
  vertices 0.014085305673904987
  edges    0.3040178910453721
```

Strict polarity gives the rigorous own-centred classification of `P`. A separate direct binary64 P reconstruction independently returns stable P faces `14432,14437`, unstable P vertices `5293,15955`, and saddle P edges `(1342,1343)` and `(4058,8155)`; that direct reconstruction is a consistency check, while the root-box Q audit plus strict polarity is the rigorous statement. 

## 8. Positive preserving neighborhood

All six independent entries of the symmetric metric may vary independently within

```text
|ΔA_ij| <= 2^-600.
```

The exact lower eigenvalue bound on the complete metric box is

```text
0.00170325044228335082389079149814894046912935276125880487352769448083438647507900082627268756896020176190641827409095062018.
```

The complete geometric denominator ledger has

```text
minimum true-edge length           3.201678077398692e-5
minimum face cross-normal norm     6.279733427554046e-8
minimum full edge-cone determinant 1.2197274440461925e-19.
```

Using the recorded conservative operation-count Lipschitz envelope `1e65`, the largest directed mechanical-score change on the box is at most `7.274e-116`, compared with the smallest decisive score of approximately `6.509e-4`. Incidence, active/inactive status, coplanar grouping, true edges, root inclusion, and the entire `(2,2,2)` class therefore persist on a nonzero six-dimensional neighborhood. 

## 9. Exact obstruction to a one-apex Morse relay

For each natural pairing of a residual stable face with a residual saddle edge, the normal of a fourth actual maximal face is an exact positive linear combination of the stable-face normal and the two saddle-incident face normals. The associated support gap is strictly positive. Therefore any one new hull vertex visible to the stable face and both saddle incident faces must also expose the listed fourth face.

| stable face | saddle edge | forced face | directed unit-normal gap |
|---:|---|---:|---:|
| `5293` | `(13283,14192)` | `6576` | `>=0.011246047371835374` |
| `5293` | `(14645,15596)` | `24111` | `>=0.006658015288232818` |
| `15955` | `(13283,14192)` | `16497` | `>=0.006428847697583524` |
| `15955` | `(14645,15596)` | `2218` | `>=0.011076083410896503` |

All coefficients, normal identities, and support gaps are exact rationals in `AQ32_OUTLET_METRIC_single_vertex_relay_obstruction.json`. This is an exact obstruction to every one-new-vertex relay in those four channels; it is not a global obstruction to a multi-cell surgery. 

## 10. Exact outlet graph width

The actual true-edge graphs give

```text
minimum Q stable-face to saddle distance      158 edges
maximum local Q unstable-to-saddle distance     5 edges
minimum P stable-face to saddle distance        13 edges
minimum P unstable-vertex to saddle distance   369 edges.
```

Consequently, an outlet surgery constrained to existing Q boundary edges needs at least 158 edges to contain a stable face and saddle. In the dual P, an existing-boundary surgery containing a residual unstable vertex and saddle needs at least 369 edges. The economical topology must therefore introduce a genuinely new cross-gap true edge or an actual finite-thickness volumetric cell rather than following the inherited surface lattice. 

## 11. Complete attempted continuation path and evidentiary status

### 11.1 Exact endpoint path

The fully exact path that was actually completed is

```text
AQ32-CR3D580 exact parent
  -> deterministic outlet recurrence on 1,898 parent rows
  -> insertion of 2,038 exact candidate rows
  -> exact active selector: 22,033 of 25,837 rows
  -> exact hull canonicalization by 510 integer-predicate 2↔2 repairs
  -> grouping of the stable square and deletion of diagonal (19609,19610)
  -> exact dyadic SPD map A
  -> isolated transformed Santaló root
  -> exhaustive root-box mechanics
  -> exact (2,2,2) NONWINNER.
```

The 510 repairs canonicalize the endpoint incidence; they are not claimed to be a continuous Morse-cancellation homotopy from the parent to a target chamber.

### 11.2 Exact double-cap incidence probe, numerical mechanics only

Two dyadic cap candidates were inserted and the hull rebuilt exactly:

```text
candidate rows 22035
active rows    22026
Q f-vector     (22026,66071,44047)
exact repairs  2050
old rows deactivated [51,100,124,262,263,264,305,306,307].
```

The two cap vertices are not adjacent; their graph distance is `297`. A fresh numerical Santaló solve had residuals of order `1e-11` and returned `(2,2,2)`: the stable equilibria moved to cap-adjacent faces while both U–H channels survived. Because no interval Santaló enclosure and full directed mechanics certificate were produced for this probe, it remains search evidence only. 

### 11.3 Connected existing-surface deletions

Connected S–H/U–H corridors deleting `164`, `944`, and `1,853` rows were rebuilt and rescored. All three numerical endpoints remained `(2,2,2)`, with minimum positive margins about `0.0012483`, `0.0010466`, and `0.0006419`. These probes show transport of the Euler-neutral block across broad inherited surface patches, but they are not continuum exclusions or exact endpoint certificates. 

### 11.4 Fixed-topology metric minimax

The strongest recorded fixed-topology metric state had parameters

```text
(-0.62543662157198,
  1.183240586443055,
  1.0492493278612183,
  1.0065948097657968,
 -0.3513071432561904)
```

and class `(2,5,5)`, with hard winner score `-0.001655945037382145`. It opens a five-channel U–H transfer ladder rather than cancelling the residual packets. This is discovery evidence only. 

## 12. Topology compelled by the obstruction

The smallest evidence-supported successor is not another cap, scalar return belt, isolated rail, metric deformation, or deletion corridor. It must be one whole-outlet event with two edge-sharing nonsimplicial cells, or an equivalent finite-thickness three-cell complex, sharing a new interior relay edge.

A concrete first branch should use the lowest-gap exact S–H channel

```text
stable face 15955
saddle edge (13283,14192)
forced face 16497
```

and pair it with one of the local unstable vertices `14432` or `14437` and the other saddle `(14645,15596)`. The alternate three S–H channel choices remain legitimate branches and are listed in the obstruction table.

The replacement must satisfy all of the following in the **same actual circuit event**:

1. Replace the complete star of the selected stable face, both incident faces of its saddle edge, and the exact forced fourth face—or make that forced face inactive before any outer vertex sees all three original constraint faces.
2. Replace the complete star of one residual unstable vertex and the complete star of the other saddle edge.
3. Insert a genuine short cross-gap true edge, rather than route the event along the 158-edge Q or 369-edge P inherited paths.
4. Permit the obsolete stable face, unstable vertex, both saddle edges, the forced face, and their relay rows to become non-extreme simultaneously; sequential deactivation is precisely what the probes show transports the packet.
5. Use an evidence-supported minimum template of three event vertices: one outer vertex for each cell and one shared terminal/relay vertex. The exact theorem rules out one vertex; the three-vertex count is the smallest practical shared-cell template, not a proved global lower bound.
6. Carry at least six independent geometric parameters: two transverse cell-depth modes and one axial/shared-relay mode must remain free after three additional mechanically inactive support coordinates are solved as dependent variables for the three normalized Santaló equations. The moment-control Jacobian must be nonsingular in the rebuilt incidence cell.
7. Absorb temporary half-sector rails, especially `6.5/14.5` and, if used, `1.5/9.5`, into the shared terminal cells rather than attaching them separately to the coarse background.
8. If the changed region reaches the next remote stable band, include the complete sectors `2/3` and `10/11` stars in the same event rather than repairing them sequentially. These are the outlet-wide requirements inherited from the exact CR3D580 packet localization. 

After **every** substantive circuit crossing, the actual hull must be rebuilt and the following gate rerun: active/inactive selector, grouped maximal-face cycles, true edges, positive projective denominators, interval Santaló isolation, all maximal-face projection tests, every full vertex tangent cone, all four components of every true-edge normal cone, positive perturbation box, independent reconstruction, and watertight mesh agreement.

## 13. Reproduction and immutable artifacts

Run from the exact outlet archive directory:

```bash
python generate_AQ32_OUTLET_METRIC_exact.py
python verify_inactive_rows.py
python verify_AQ32_OUTLET_METRIC_exact.py
python verify_direct_p_midpoint.py
```

The first three are the rigorous generator/inactive/full verifier chain; the fourth is the independent direct-P numerical consistency check. The archive records clean `PASS` outcomes with the f-vectors, root enclosure, classes, margins, perturbation proof, obstruction, and mesh audits. 

Core files:

```text
AQ32_OUTLET_candidate_rows_exact.npz
AQ32_OUTLET_METRIC_exact_data.npz
AQ32_OUTLET_METRIC_matrix.json
AQ32_OUTLET_METRIC_santalo.json
AQ32_OUTLET_METRIC_rootbox_audit.json
AQ32_OUTLET_METRIC_faces_rootbox_ledger.csv.gz
AQ32_OUTLET_METRIC_vertices_rootbox_ledger.csv.gz
AQ32_OUTLET_METRIC_edges_rootbox_ledger.csv.gz
AQ32_OUTLET_METRIC_inactive_separation.json
AQ32_OUTLET_METRIC_perturbation_proof.json
AQ32_OUTLET_METRIC_single_vertex_relay_obstruction.json
AQ32_OUTLET_METRIC_residual_basin_graph.json
AQ32_OUTLET_METRIC_certificate.json
```

The SHA-256 ledger authenticates, among others, the exact endpoint, candidate selector, matrix, Santaló certificate, root-box audit, inactive separation, perturbation proof, obstruction, and residual graph.

Materialized archives:

- AQ32 outlet exact archive (`AQ32_OUTLET_METRIC_EXACT_archive.zip`)
- AQ32-CR3D580 parent archive (`AQ32-CR3D580-exact-archive.zip`)

## 14. Mesh audit

```text
Q: 22,033 vertices, 44,062 triangles,
   signed volume about 3.9843338210032506

P: 44,061 vertices, 88,118 triangles,
   signed volume about 4.301795208063975
```

Every triangulation edge in both meshes has incidence exactly two. The Q OBJ/STL, Q exact row/face/edge files, certificate, and exact-data hashes are recorded in the archive checksum ledger.

## Final research judgment

`AQ32-OUTLET-METRIC-EXACT` is the strongest exact finite outlet cell supported by the durable evidence. It conclusively closes the chamber-exactification obligation and proves that the robust numerical `(2,2,2)` state was not a floating-incidence artefact, centring error, triangulation-diagonal error, or wall point. It also proves that a single-apex relay is impossible in every natural stable–saddle channel and quantifies why inherited-surface coupling is too wide.

It does **not** complete the topology-changing obligation. The exact result is therefore:

```text
winner: false
disposition: EXACT NONWINNER
object: AQ32-OUTLET-METRIC-EXACT
own-centred class: (2,2,2)
remaining task: one shared volumetric two-cell/three-cell whole-outlet cancellation with a new cross-gap edge and three independent dependent Santaló controls
```

Disconnected caps and broad surface deletions transport the pair; metric motion multiplies it. The next genuinely untested topology is the shared volumetric terminal described above. No stronger winner claim is supported.
