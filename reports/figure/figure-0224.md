# figure-0224

Historical AI scientific report · saved 2026-09-02 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: unreviewed-encoded-blocks-omitted.

---

The attached journal's acceptance gate requires a finite uniform-density body evaluated at its own exact volume centroid, with strict `(S,U,H)=(1,1,0)`, complete H/V/edge evidence, independent verification, and matching OBJ/STL; wall points and near-solutions do not qualify. :contentReference[oaicite:0]{index=0}

The accepted starting point was the exact second-support `(16,42,28)`, `(2,2,2)` body with forced edge `[2152,2369]`; the journal explicitly named the third-support `H` event coupling `[2152,2369]→[0,2515]`, `[3296,D]→[1258,G]`, `[3290,D]→[2152,C]`, and the blocked `[F,G]` route. :contentReference[oaicite:1]{index=1}

# Calm Quartz 90 — exact wall-242 third-support/full-star determination

## Literal disposition

**EXACT DELIMITED NONWINNER.** No homogeneous convex polyhedral Gömböc was obtained in this topology.

The prescribed third-support event was nevertheless realized as a literal exact finite full-hull replacement. A new extreme support `H=40008` couples all four predecessor mechanisms in one dual-connected, same-boundary, positive-volume disk replacement:

```text
[2152,2369] -> [0,2515]      forcing-edge escape
[3296,D]    -> [1258,G]      predecessor extra-stable death sheet
[3290,D]    -> [2152,C]      predecessor saddle exchange
[F,G]       -> H-star        resolution of the nonflippable core
```

The exact target has 18 supplied dyadic rows, 17 active vertices, actual

```text
(V,E,F,C)=(17,45,30,90),
(S,U,H)=(2,2,2).
```

It preserves intended stable face `[0,1371,C]` and intended unstable vertex `C`. Every named predecessor carrier is genuinely absent or mechanically dead, but the Euler-neutral packet is transferred to extra stable `[2152,3290,C]`, extra unstable `2732`, and saddle edges `[0,C]`, `[G,H]`.

This result closes the materialized one-`H` full-star topology and its certified open chamber. It does not exclude every possible placement of a third support or every larger multi-cell.

## What changed relative to the exact predecessor

The exact predecessor was the 17-supplied-row, 16-active-vertex `G` endpoint with `(V,E,F)=(16,42,28)` and strict `(2,2,2)`. Its unwanted block was

```text
stable    [3296,D,G]
unstable  2369
saddles   [3290,D], [F,G]
forced    true edge [2152,2369].
```

The new full-hull incidence has all of the following exact facts:

- `[2152,2369]` is not a true edge;
- `[3296,D,G]` is not a maximal face;
- vertex `2369` remains extreme but is not unstable;
- `[3290,D]` and `[F,G]` are not true edges;
- the H-star uses edges `[C,H]`, `[D,H]`, `[F,H]`, `[G,H]` and faces `[C,G,H]`, `[D,G,H]`, `[D,F,H]`, `[C,H,F]`;
- protected `[0,1371,C]` and `C` remain strict equilibria.

Thus the predecessor forcing component was crossed, not merely renamed. The negative conclusion arises from a newly born packet in a different actual incidence.

## Exact dyadic generator

All supplied coordinates have common denominator `2^24=16777216`; `A=40001`, `B=40002`, `C=40003`, `D=40004`, `E=40005`, `F=40006`, `G=40007`, `H=40008`.

```text
0     (     45159,   -1563851,    513718) / 16777216
1258  (   -462699,     739174,   -121108) / 16777216
1371  (   5627399,   -5682536,    -84806) / 16777216
1975  (   6134422,   -5917246,   -343918) / 16777216
2152  (    434354,    -485254,    -65327) / 16777216
2369  (   5962653,   -5678114,   -390765) / 16777216
2515  (   4220495,   -3965847,   -317464) / 16777216
2732  (   7096471,   -7079745,   -327651) / 16777216
3290  (     37913,    -896244,    259770) / 16777216
3296  (   2356905,   -2146041,   -232012) / 16777216
A     (    -46094,    -972577,    326308) / 16777216
B     (         0,          0,         0) / 16777216  inactive
C     ( -17491869,   18081289,    707574) / 16777216
D     (  -4453759,    4907137,     24194) / 16777216
E     (  -6744044,    7233331,    139900) / 16777216
F     (  -8337969,    8888372,    210445) / 16777216
G     (    906193,    -502545,   -199075) / 16777216
H     (  -6852164,    7385569,    139433) / 16777216
```

`B=(0,0,0)` is supplied but strictly interior. Its exact minimum oriented supporting-plane slack is

```text
121571974084445/147573952589676412928 > 0.
```

Every other supplied row is active. `data/generator_exact.json` is authoritative; the floating discovery path recorded there is provenance only, while the rounded dyadic rows and exact reconstruction are the theorem object.

## Exact ordinary volume and own centroid

The uncentred volume is

```text
12344159703567225265/28334198897217871282176
```

approximately `0.0004356629156287632`.

The exact ordinary-volume centroid is

```text
cx = -81354779372152679979128293/828402534740973235166248960
cy = 73983010350868114906645599/828402534740973235166248960
cz = 4112816322707991902364561/414201267370486617583124480
```

approximately

```text
(-0.098206820911757434,
 0.089308044396558123,
 0.0099295116811635459).
```

Subtracting this one exact rational vector from every active vertex gives exact tetrahedral first moments

```text
Mx=My=Mz=0.
```

`data/positive_tetrahedralization.csv` records all 30 signed volume and moment contributions. No auxiliary mechanical point, point mass, or Santaló surrogate is used.

## Complete actual maximal-face lattice

The 30 outward-oriented irredundant maximal triangles are:

- [0,2732,1371]
- [0,1371,C]  **stable**
- [0,2152,2515]
- [0,3290,2152]
- [0,2515,2369]
- [0,2369,2732]
- [0,A,3290]
- [0,C,A]
- [1258,3296,2152]
- [1258,2152,D]
- [1258,G,3296]
- [1258,D,G]
- [1371,1975,2369]
- [1371,2732,1975]
- [1371,2369,C]
- [1975,2732,2369]
- [2152,3296,2515]
- [2152,3290,C]  **stable**
- [2152,C,D]
- [2369,2515,G]
- [2369,G,C]
- [2515,3296,G]
- [3290,A,C]
- [C,E,D]
- [C,F,E]
- [C,H,F]
- [C,G,H]
- [D,E,F]
- [D,F,H]
- [D,H,G]

Every active vertex lies on its listed incident planes and every nonincident active vertex is strictly behind them. The minimum Euclidean nonincidence separation is

```text
2.2106710308014541e-06.
```

Primitive integer H-data are in `data/third_support17_exact_H_irredundant.csv`.

## Complete true-edge incidence

The 45 actual physical true edges are:

```text
[0,1371]  [0,2152]  [0,2369]  [0,2515]  [0,2732]
[0,3290]  [0,A]  [0,C]  **saddle**  [1258,2152]  [1258,3296]
[1258,D]  [1258,G]  [1371,1975]  [1371,2369]  [1371,2732]
[1371,C]  [1975,2369]  [1975,2732]  [2152,2515]  [2152,3290]
[2152,3296]  [2152,C]  [2152,D]  [2369,2515]  [2369,2732]
[2369,C]  [2369,G]  [2515,3296]  [2515,G]  [3290,A]
[3290,C]  [3296,G]  [A,C]  [C,D]  [C,E]
[C,F]  [C,G]  [C,H]  [D,E]  [D,F]
[D,G]  [D,H]  [E,F]  [F,H]  [G,H]  **saddle**
```

Every edge has exactly two incident maximal faces, and

```text
17-45+30=2.
```

No display-mesh diagonal is counted as a physical edge. `data/third_support17_exact_true_edges_full_cones.csv` contains both incident faces and all four exact equilibrium-cone components for every edge.

## Exhaustive mechanics at the exact own centroid

### Stable maximal faces

Exactly two maximal faces are stable:

```text
[0,1371,C]
[2152,3290,C].
```

The minimum positive perpendicular-foot barycentric coordinate over both stable faces is

```text
52860171994024729500868554716175663221039011/473634561976707217246281273088702095825639620
≈ 0.11160539419550283.
```

Every other maximal face has a fixed exact negative Cramer witness. The closest excluded-face witness is

```text
-15853634086894655167442378343906793601022112/45090074464142426939579365553997256080025785
≈ -0.35159919949793272.
```

### Unstable vertices

Exactly two vertices are unstable:

```text
2732
C.
```

The smallest positive raw outgoing support among them is

```text
56709798706608447971293019863419/868643016268550751037684669480960
≈ 0.06528550583439674.
```

Every other active vertex has an exact nonpositive outgoing witness. The closest excluded-vertex witness is

```text
-16141398579820566237160639894995/2779657652059362403320590942339072
≈ -0.0058069735918241236.
```

### Saddle true edges

Exactly two true edges are saddles. Their normalized four-component tuples—edge-foot `t`, `1-t`, and the two incident normal-cone coefficients—are

```text
[0,C]  (0.1294511408706433, 0.8705488591293568,
        6.16452637969469,   6.166938556555152)
[G,H]  (0.29152696581212345, 0.7084730341878765,
        0.6572431795993764, 1.005791714342781)
```

The global positive normalized saddle minimum is `0.1294511408706433`. Every other true edge has at least one exact negative full-cone component. The closest raw determinant-scaled excluded component is

```text
-424043659622193946280804247594801274775575067616397672789401/18473993849075356603420658440802299224467347176990711236239037940367360
≈ -2.2953545567160497e-11.
```

Therefore the complete strict class is exactly

```text
(S,U,H)=(2,2,2),
S+U-H=2.
```

## Genuine connected third-support/full-star replacement

The predecessor and successor hulls were independently reconstructed. Their exact changed-face sets become dual-connected, one-boundary-component disks after adjoining the minimal four common bridge faces

```text
[0,2152,3290]
[C,D,E]
[C,E,F]
[D,E,F].
```

Both disks have the same decagonal boundary cycle

```text
0–2369–2515–2152–D–1258–3296–G–C–3290–0.
```

### Predecessor-side disk

```text
- [0,2152,2369]
- [0,2152,3290]
- [1258,3296,D]
- [2152,2369,2515]
- [2152,3290,D]
- [3290,C,D]
- [3296,D,G]
- [C,D,E]
- [C,E,F]
- [C,F,G]
- [D,E,F]
- [D,F,G]
```

It has `(V,E,F)=(12,23,12)`, Euler characteristic one, one boundary component, and a connected dual graph.

### Successor-side disk

```text
- [0,2152,2515]
- [0,2152,3290]
- [0,2369,2515]
- [1258,3296,G]
- [1258,D,G]
- [2152,3290,C]
- [2152,C,D]
- [C,D,E]
- [C,E,F]
- [C,F,H]
- [C,G,H]
- [D,E,F]
- [D,F,H]
- [D,G,H]
```

It has `(V,E,F)=(13,26,14)`, Euler characteristic one, one boundary component, and a connected dual graph.

The exact true-edge changes implementing the assignment are

```text
removed [2152,2369], [3290,D], [3296,D], [F,G]
inserted [0,2515], [1258,G], [2152,C], [C,H], [D,H], [F,H], [G,H].
```

Coning each patch triangle to that side's exact own centroid yields a positive-volume 3-ball. The smallest predecessor-side cone is face `[1258,3296,D]` with exact volume

```text
4443017614214982527525762409165752451511708462530230494162425409004023285/549016855338829011592973918587686251037233651263842693760105256746022959316992
```

approximately `8.0926797984607379e-06`. The smallest successor-side cone is face `[D,E,F]` with exact volume

```text
530309248879491664354410760866868397/1399047505039583035883660144617984685506560
```

approximately `3.7905020878078598e-07`.

The bridge enumerator tested exactly `3816` common-face subsets in increasing cardinality. No subset of fewer than `4` common faces makes both exact changed-face sets dual-connected disks with the same boundary. This minimality is restricted to enlarging these particular exact source/target changed-face sets by common faces; it is not a classification of all third-support topologies.

No scalar simultaneous common-wall homotopy is claimed. The theorem-level event is the pair of exact full hulls and their connected same-boundary positive-volume replacement.

## Positive own-centroid perturbation chamber

Independent perturbations of all 54 supplied uncentred coordinates by

```text
|delta r_ij| <= 2^-50 = 1/1125899906842624
```

preserve after outward interval recomputation of volume, all three moments, the common ordinary centroid, hull incidence, and mechanics:

```text
18 supplied rows; B strictly inactive; 17 active vertices;
30 maximal faces; 45 true edges;
strict class (2,2,2);
all 90 directed vertex primitives;
all four components of all 45 true-edge cones;
the residual forced-edge sign chamber.
```

Certified lower clearances on the whole box are approximately

```text
topology/nonincidence  2.3090882636173052e-08
inactive B             8.2380371911908796e-07
chosen face signs      7.1087264079081453e-07
chosen vertex signs    0.0058069735907540793
chosen edge components 2.2953508620221585e-11
forced external signs  0.010964046548965581.
```

The certified volume interval is

```text
[310899445562888497878528109270282697091753/713623846352979940529142984724747568191373312,
 932698336697445220875962528697935841984517/2140871539058939821587428954174242704574119936].
```

Larger tested radii through `2^-49` fail closed in dependency-sensitive interval topology/face-Gram tests; no maximal-radius claim is made.

## Exact residual forcing component

The target contains true edge `[1975,2732]`, incident to

```text
[1371,2732,1975]
[1975,2732,2369].
```

Every external directed support at both endpoints is strictly positive. The exact minimum is

```text
152381479488561135207333078592691/13898288260296812016602954711695360
≈ 0.010964046552687264.
```

The two mutual supports are

```text
sigma(1975->2732) = -198728990178459833235207270025561/3474572065074203004150738677923840
sigma(2732->1975) = 56709798706608447971293019863419/868643016268550751037684669480960.
```

They satisfy the exact energy identity

```text
sigma(1975->2732)+sigma(2732->1975)
= ||p_2732-p_1975||^2
= 2277206818691/281474976710656 > 0.
```

If neither endpoint were unstable while every external support stayed positive, both mutual supports would have to be nonpositive, contradicting this identity. Hence at least one of `1975,2732` is unstable throughout the certified sign chamber. Since `C` is independently strict unstable, the complete `2^-50` chamber has `U>=2` and cannot contain a Gömböc.

The theorem ends if `[1975,2732]` disappears, an endpoint deactivates, or an external support reverses. It is not promoted to a global obstruction for larger support complexes.

## First genuinely new successor topology

The exact endpoint exposes:

```text
[1975,2732] -> [1371,2369]  illegal ordinary flip: [1371,2369] already exists
[2152,3290] -> [0,C]        illegal ordinary flip: [0,C] already exists
[0,C]       -> [1371,A]     legal saddle exchange
[G,H]       -> [C,D]        illegal ordinary flip: [C,D] already exists.
```

The extra stable face `[2152,3290,C]` has its minimum barycentric coordinate at `C`, so its limiting edge is `[2152,3290]`. Three of the four successor mechanisms are therefore nonflippable in the exact target graph.

The smallest evidence-supported nonrepeating continuation is a fourth shared support `I`, or an equivalent connected multi-cell, that jointly deletes the full `[1975,2732]` forcing component, resolves the nonflippable stable limiting edge `[2152,3290]`, crosses the legal saddle `[0,C]→[1371,A]`, and resolves the nonflippable `[G,H]` core before another packet is born, while preserving intended `[0,1371,C]`, `C`, and exact ordinary-volume centring unless a stronger fully audited reconstruction supersedes them.

## Independent verification

The package contains six replay layers:

1. `scripts/generate_candidate.py` — deterministic exact generation from the dyadic table;
2. `scripts/verify_exact.py` — primary exact reconstruction of predecessor/target hulls, moments, incidence, mechanics, patch, obstruction, and exports;
3. `scripts/verify_interval_own_centroid.py` — outward interval proof of the `2^-50` physical input-coordinate box;
4. `scripts/verify_independent.py` — standard-library-only clean-room exact reconstruction importing neither construction code nor `exact_core.py`;
5. `scripts/verify_mesh.py` — OBJ/STL orientation, incidence, Euler, and watertightness verification;
6. `scripts/find_minimal_bridge_patch.py` — exact exhaustive `3816`-subset bridge replay.

The aggregate deterministic replay ends with


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]


The OBJ contains 17 vertices and 30 outward triangles; its 45 edge classes each have multiplicity two. The STL has the same 30 facets.

## Exact scope

Closed exactly:

- this materialized one-`H` third-support/full-star same-boundary replacement;
- the complete `2^-50` own-centroid mechanics chamber around it;
- deletion of every predecessor carrier named by the assignment;
- the external-positive `[1975,2732]` forcing chamber;
- common-face bridge cardinalities below four for the stated source/target changed-face sets.

Not closed:

- every placement of a third support;
- every alternate triple-octahedral/triangular-prismatic three-cell;
- the fourth-support/multi-cell successor above;
- the global existence problem.

## Artifact map

- `candidate.json` — concise exact disposition.
- `data/generator_exact.json` — authoritative 18-row dyadic generator and active/inactive labels.
- `data/input_vertices_exact.csv` — all supplied uncentred rational V-data.
- `data/active_vertices_centered_exact.csv` — all 17 exact own-centred active vertices.
- `data/inactive_rows_exact.csv` — exact strict-interiority certificate for `B`.
- `data/third_support17_exact_H_irredundant.csv` — complete primitive 30-row H-data.
- `data/third_support17_exact_faces.csv` — every maximal face and exact face-foot mechanics.
- `data/third_support17_exact_vertex_primitives.csv` — all 90 directed vertex supports.
- `data/third_support17_exact_true_edges_full_cones.csv` — all 45 true edges and every four-component cone.
- `data/positive_tetrahedralization.csv` — exact volume and moment contributions.
- `certificates/third_support_shared_terminal_patch.json` — exact same-boundary full-star replacement.
- `certificates/minimal_same_boundary_bridge.json` — exact bridge-minimality certificate.
- `certificates/own_centroid_perturbation_certificate.json` — directed `2^-50` open-box proof.
- `certificates/residual_forced_edge_1975_2732.json` — exact `U>=2` chamber theorem.
- `certificates/first_successor_topology.json` — fourth-support successor specification.
- `scripts/verify_independent.py` — clean-room verifier.
- `mesh/body.obj`, `mesh/body.stl` — matching watertight display meshes.

## Final statement

**NONWINNER, rigorously delimited.** The third support `H` genuinely crosses the predecessor `[2152,2369]` chamber boundary, resolves the blocked `[F,G]` core, and deletes the entire predecessor equilibrium packet in one connected full-hull event. The target remains a strict open own-centred `(2,2,2)` body because a new packet is born. External-positive true edge `[1975,2732]` forces a second unstable equilibrium throughout the certified chamber. The first mathematically new topology is the fourth-support/multi-cell full-star operation above.

## Delivered artifacts

- [Complete exact NONWINNER archive](sandbox:/mnt/data/Calm_Quartz_90_wall242_third_support_exact_NONWINNER.zip) — SHA-256 `a9a9cd35dc31c9650cfb2535828589695c31f14cb1093f0d420699fd963321af`, 488,089 bytes.
- [Full Markdown handoff](sandbox:/mnt/data/Calm_Quartz_90_wall242_third_support_handoff.md)
- [Structured result](sandbox:/mnt/data/Calm_Quartz_90_wall242_third_support_result.json)
- [Final clean-extraction receipt](sandbox:/mnt/data/Calm_Quartz_90_wall242_third_support_clean_verification.json)
- [Clean replay transcript](sandbox:/mnt/data/Calm_Quartz_90_wall242_third_support_clean_replay.txt)
- [Exact 18-row generator](sandbox:/mnt/data/Calm_Quartz_90_wall242_third_support_exact_NONWINNER/data/generator_exact.json)
- [Supplied exact V-data](sandbox:/mnt/data/Calm_Quartz_90_wall242_third_support_exact_NONWINNER/data/input_vertices_exact.csv)
- [Exact own-centred active V-data](sandbox:/mnt/data/Calm_Quartz_90_wall242_third_support_exact_NONWINNER/data/active_vertices_centered_exact.csv)
- [Primitive irredundant H-data](sandbox:/mnt/data/Calm_Quartz_90_wall242_third_support_exact_NONWINNER/data/third_support17_exact_H_irredundant.csv)
- [All maximal-face mechanics](sandbox:/mnt/data/Calm_Quartz_90_wall242_third_support_exact_NONWINNER/data/third_support17_exact_faces.csv)
- [All directed vertex primitives](sandbox:/mnt/data/Calm_Quartz_90_wall242_third_support_exact_NONWINNER/data/third_support17_exact_vertex_primitives.csv)
- [All true edges and four-component cones](sandbox:/mnt/data/Calm_Quartz_90_wall242_third_support_exact_NONWINNER/data/third_support17_exact_true_edges_full_cones.csv)
- [Same-boundary full-star certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_third_support_exact_NONWINNER/certificates/third_support_shared_terminal_patch.json)
- [Minimal bridge certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_third_support_exact_NONWINNER/certificates/minimal_same_boundary_bridge.json)
- [Own-centroid perturbation certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_third_support_exact_NONWINNER/certificates/own_centroid_perturbation_certificate.json)
- [Residual forced-edge certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_third_support_exact_NONWINNER/certificates/residual_forced_edge_1975_2732.json)
- [Next-topology certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_third_support_exact_NONWINNER/certificates/first_successor_topology.json)
- [Independent clean-room verifier](sandbox:/mnt/data/Calm_Quartz_90_wall242_third_support_exact_NONWINNER/scripts/verify_independent.py)
- [Aggregate replay script](sandbox:/mnt/data/Calm_Quartz_90_wall242_third_support_exact_NONWINNER/RUN_ALL_VERIFIERS.sh)
- [Package verifier](sandbox:/mnt/data/Calm_Quartz_90_wall242_third_support_exact_NONWINNER/verify_package.py)
- [SHA-256 manifest](sandbox:/mnt/data/Calm_Quartz_90_wall242_third_support_exact_NONWINNER/SHA256SUMS.txt) — 43 manifested entries, manifest SHA-256 `5c4aa07b28398d24d97ecf1c1958fc7197eafc256334515b817360153406c540`.
- [Watertight OBJ](sandbox:/mnt/data/Calm_Quartz_90_wall242_third_support_exact_NONWINNER/mesh/body.obj)
- [Watertight STL](sandbox:/mnt/data/Calm_Quartz_90_wall242_third_support_exact_NONWINNER/mesh/body.stl)
