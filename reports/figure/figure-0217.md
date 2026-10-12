# figure-0217

AI research report · 2026-09-02 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Calm Quartz 90 — exact wall-242 second-support/two-cell determination

## Disposition

**EXACT DELIMITED NONWINNER.** The requested second-support topology was realized as a genuine same-boundary finite-thickness full-hull replacement, but it does not produce a homogeneous polyhedral Gömböc.

The exact endpoint has 17 supplied dyadic rows, 16 active vertices, actual `(V,E,F,C)=(16,42,28,84)`, and strict own-centred `(S,U,H)=(2,2,2)`. It preserves intended stable `[0,1371,C]` and intended unstable `C`. Every predecessor residual carrier is genuinely deleted—forced edge `[2152,2732]`, stable `[3296,D,B]`, unstable status of `2732`, and saddles `[2152,C]`,`[2369,F]`—but a replacement packet appears: stable `[3296,D,G]`, unstable `2369`, saddles `[3290,D]`,`[F,G]`.

The run accepts only a finite uniform-density body evaluated at its own exact volume centroid, with strict `(1,1,0)`, complete H/V/edge mechanics, independent verification, and matching meshes; wall points and near-solutions do not qualify. The supplied journal identifies this exact second-support/double-cell operation as the successor of the accepted one-support `F` endpoint.

## Exact generator

Labels are `A=40001`, `B=40002`, `C=40003`, `D=40004`, `E=40005`, `F=40006`, `G=40007`. Every supplied point is `(X,Y,Z)/2^48`, where `2^48=281474976710656`:

```text
0      (  32978011132480,  -56023656103408,   5949523740432)
1258   (  10820590885040,  -12286329077248,  -1153438187104)
1371   (  81062665693696,  -84009674395088,   -805647705888)
1975   ( 121971335274144, -123892328278928,  -4014242889904)
2152   ( 158876645370576, -155922500222992,  -9441508282848)
2369   ( 159391038075776, -155471726492032,  -8228196322000)
2515   (  83152088222816,  -66278245494448, -10431385407200)
2732   ( 106490310071296, -113655412701680,  -2021239614064)
3290   ( -35190125085520,   14000573961760,   8265772879536)
3296   (  28831969168032,  -24570355865120,  -3860948802848)
A      ( -58482109039568,   45191421302272,   7421682904624)
B      (               2,                1,              -1)  inactive
C      (-200331263112176,  210445850192304,   7822258388240)
D      (-195108016411840,  179615732737696,  13248518915520)
E      (-184097799001584,  190802550363104,   7275073848256)
F      ( -95686790291744,  117385415299152,  -3289062018912)
G      ( -14678550951392,   34668684774672,  -6737161445856)
```

`B=(2,1,-1)/2^48` is exactly the arithmetic mean of the sixteen active rows, hence a strict interior convex combination. Its exact minimum oriented support slack is

```text
1626820153024762085216972808201546219/
43556142965880123323311949751266331066368 > 0.
```

The other sixteen supplied rows are active. The exact generator and supplied/centred V-tables are linked below.

## Exact ordinary volume and centroid

The uncentred volume is

```text
25209617654570724240352475646751155913/
32667107224410092492483962313449748299776
≈ 0.0007717125817535858.
```

The exact ordinary-volume centroid is

```text
cx=-155358903244218241519623771642920282517505164938681/
    1773969135551209234945610979990448755450380636127232
cy= 156493674887911464484213975639646857890151358024015/
    1773969135551209234945610979990448755450380636127232
cz=   7493230367728411759828324749129223194208614615379/
    1773969135551209234945610979990448755450380636127232.
```

Subtracting this one rational vector from all active vertices gives exact first moments `Mx=My=Mz=0`. The positive tetrahedralization file lists all 28 exact volume and moment contributions. No auxiliary centre is substituted.

## Actual irredundant hull

For every oriented triangle `(i,j,k)`, the exact primitive H-row is obtained from `n=(v_j-v_i)×(v_k-v_i)`, `b=n·v_i`, followed by exact outward orientation and primitive integer normalization. The full 28-row H-table is supplied.

The 28 maximal faces are

```text
[0,2732,1371] [0,1371,C]* [0,2152,2369] [0,3290,2152]
[0,2369,2732] [0,A,3290] [0,C,A] [1258,3296,2152]
[1258,2152,D] [1258,D,3296] [1371,1975,2369] [1371,2732,1975]
[1371,2369,C] [1975,2732,2369] [2152,2515,2369] [2152,3296,2515]
[2152,3290,D] [2369,2515,G] [2369,G,C] [2515,3296,G]
[3290,A,C] [3290,C,D] [3296,D,G]* [C,E,D]
[C,F,E] [C,G,F] [D,E,F] [D,F,G]
```

Stars mark the stable faces. Minimum Euclidean nonincident separation is `3.905567216598046e-5`.

The 42 true edges are

```text
[0,1371] [0,2152] [0,2369] [0,2732] [0,3290] [0,A] [0,C]
[1258,2152] [1258,3296] [1258,D]
[1371,1975] [1371,2369] [1371,2732] [1371,C]
[1975,2369] [1975,2732]
[2152,2369] [2152,2515] [2152,3290] [2152,3296] [2152,D]
[2369,2515] [2369,2732] [2369,C] [2369,G]
[2515,3296] [2515,G]
[3290,A] [3290,C] [3290,D]* [3296,D] [3296,G] [A,C]
[C,D] [C,E] [C,F] [C,G] [D,E] [D,F] [D,G] [E,F] [F,G]*
```

Stars mark saddles. Every edge has exactly two incident maximal faces and `16-42+28=2`. No triangulation diagonal is counted as a true edge.

## Exhaustive own-centroid mechanics

Stable face feet:

```text
[0,1371,C]  barycentrics
(0.044944603869219654, 0.5885123252355406, 0.36654307089523963)

[3296,D,G] barycentrics
(0.7587145833729250, 0.2401452826819992, 0.0011401339450758166)
```

The exact global positive stable minimum is

```text
49476108388585714266858503722379447382268229583150729892138810430122410815471727425/
43394996353078188997708823796919777424651652278304622692214130207228699905139504448116.
```

Every other face has an exact negative Cramer witness; the closest is about `-0.0037487363227924893`.

Unstable vertices are exactly `2369,C`. The minimum raw outgoing support at `2369` is

```text
45603789209002847949907686208580198074623514423659428057669/
1835764415862864618277846918998735883329845990801923020198772736
≈ 2.4841852699039106e-5,
```

and the minimum at `C` is about `0.08206205064826574`. Every other vertex has an exact nonpositive outgoing witness; the closest is `2152→2369` at about `-3.565855356850994e-7`.

Saddle edges and their four normalized cone components are

```text
[3290,D] (0.0013756931112144067, 0.9986243068887856,
          5.376496888359316,    5.395528858427614)
[F,G]    (0.9984048822846114,    0.0015951177153886052,
          5.626736470601251,     5.606565411179501)
```

Every other true edge has an exact negative component. The closest normalized nonsaddle edge is `[2515,G]` at approximately `-5.947291580239095e-4`. The complete exact face ledger, all 84 directed vertex primitives, and all four components of all 42 true-edge cones are included. Thus the endpoint is strictly `(2,2,2)` and satisfies `S+U-H=2`.

## Genuine second-support/two-cell replacement

The predecessor and successor are reconstructed independently and share the same six-edge boundary cycle

```text
0–2152–3290–C–2369–2732–0.
```

On each side the replacement is a dual-connected, one-boundary-component 18-triangle disk with `(V,E,F)=(13,30,18)` and Euler characteristic one. Coning each disk to that side’s exact own centroid gives an 18-tetrahedron positive-volume 3-ball. The smallest source cone volume is about `1.6473603338090686e-4`; the smallest target cone volume is about `7.133962558536427e-6`.

Exact removed true edges:

```text
[2152,2732] [2152,C] [2369,D] [2369,F]
[2515,B] [2515,D] [3296,B] [B,D]
```

Exact inserted true edges:

```text
[0,2369] [2369,G] [2515,G] [3290,D]
[3296,G] [C,G] [D,G] [F,G]
```

The source nonflippable terminal disk

```text
[2369,2515,D] [2369,C,F] [2369,D,F]
[2515,3296,B] [2515,B,D] [3296,B,D]
```

is replaced by the target `G` disk

```text
[2369,2515,G] [2369,C,G] [2515,3296,G]
[3296,D,G] [C,F,G] [D,F,G],
```

with common hexagonal boundary `2369–2515–3296–D–F–C–2369`. This resolves both predecessor nonflippable cores in one full-hull event. It also contains the legal exchanges `[2152,2732]→[0,2369]` and `[2152,C]→[3290,D]` in the larger same-boundary disk.

An exact exhaustive bridge search tested 105,725 common-face subsets in increasing cardinality. No bridge using fewer than eight common faces makes both exact changed-face sets dual-connected disks with the same boundary. The first valid bridge uses eight faces. This minimality is restricted to enlarging these exact changed-face sets by common predecessor/successor faces; it is not a classification of every possible two-support topology.

No scalar simultaneous common-wall homotopy is claimed. The theorem-level incidence statement is the exact source hull, exact target hull, and exact same-boundary positive-volume replacement.

## Open perturbation certificate

Independent perturbations of all 51 uncentred supplied coordinates by

```text
|δr_ij| ≤ 2^-43 = 1/8796093022208
```

preserve, after interval recomputation of physical volume, moments, and common centroid:

```text
16 active vertices and strict inactivity of B,
28 maximal faces and 42 true edges,
class (2,2,2),
the complete face/vertex/four-cone sign ledger,
and the residual forcing-edge chamber.
```

Certified box-wide lower clearances are approximately

```text
topology/nonincidence  1.1079813656453779e-7
inactive B             3.734994844429098e-5
chosen face signs      6.357143189820274e-7
chosen vertex signs    3.5615114149802756e-7
chosen edge components 2.475432019634555e-12.
```

The last quantity is an unnormalized determinant-scaled interval clearance; the normalized endpoint edge separation is much larger. Radius `2^-42` fails closed at a dependency-sensitive face-Gram test, so no maximal-radius claim is made.

## Exact residual forcing component

The new endpoint contains true edge `[2152,2369]`, incident to `[0,2152,2369]` and `[2152,2515,2369]`. Every external endpoint support is positive. The exact minimum is

```text
4971146273088678079457687292958713589859581951120626403382634941/
31207995069668698510723397622978510016607381843632691343379136512
≈ 0.15929079269562482.
```

The mutual supports are

```text
σ(2152→2369)=
-654607037622103180560460870341141378483581677170084015865/
1835764415862864618277846918998735883329845990801923020198772736

σ(2369→2152)=
45603789209002847949907686208580198074623514423659428057669/
1835764415862864618277846918998735883329845990801923020198772736.
```

Their exact sum is

```text
7577823148528872087659/309485009821345068724781056
= ||p_2369-p_2152||² > 0.
```

If neither endpoint were unstable while every external support stayed positive, both mutual supports would be nonpositive, contradicting the identity. Therefore one endpoint remains unstable in addition to independently strict `C`; the entire certified chamber has `U≥2`.

This theorem ends when `[2152,2369]` disappears, an endpoint deactivates, or an external support reverses. It is not a global obstruction for larger support complexes.

## First genuinely new successor

The exact endpoint exposes

```text
[2152,2369] -> [0,2515]   legal forcing-edge escape
[3296,D]    -> [1258,G]   legal death sheet of stable [3296,D,G]
[3290,D]    -> [2152,C]   legal saddle exchange
[F,G]       -> [C,D]      ordinary flip illegal: [C,D] already exists.
```

The first nonrepeating successor is a third support `H`, or an equivalent connected double-octahedral/triangular-prismatic three-cell, coupling all four mechanisms in one same-boundary event before another packet is born, while preserving `[0,1371,C]`, `C`, and exact ordinary-volume centring unless a stronger audited reconstruction supersedes them.

A discovery-only determinant-one affine/metric sweep audited 262,144 robust samples and found no winner; its best class remained `(2,2,2)`. This is not used as an exclusion theorem.

## Verification and integrity

Lineage is fixed to predecessor assignment SHA-256 `ae01557481daeb009df65ee9dbce12aaa7ab21ecddbca3b8a96bd9471fc8d63f` and parent archive SHA-256 `45ffb36e6aa1fca5f4d2cd04117416d9a2f4fdef70e1f23c21f08fb7b8ed49b0`.

The package contains a deterministic generator, a primary Fraction verifier, an outward own-centroid interval verifier, a standard-library-only clean-room verifier importing neither construction code nor `exact_core`, a watertight mesh verifier, and the exact 105,725-subset bridge enumerator. A final clean extraction verified all 49 manifested SHA-256 entries and reran every layer. Terminal markers include

```text
PRIMARY_EXACT_SECOND_SUPPORT_NONWINNER_PASS
INDEPENDENT_CLEAN_ROOM_SECOND_SUPPORT_NONWINNER_PASS
WATERTIGHT_SECOND_SUPPORT_ENDPOINT_MESH_PASS
EXACT_MINIMAL_SAME_BOUNDARY_BRIDGE_PASS
ALL_CALM_QUARTZ_90_WALL242_SECOND_SUPPORT_VERIFIERS_PASS
CALM_QUARTZ_90_WALL242_SECOND_SUPPORT_PACKAGE_PASS.
```

OBJ and STL agree: 16 vertices, 28 outward facets, 42 edge classes, every edge multiplicity two.

## Exact scope

Closed: this materialized one-`G` second-support same-boundary topology, its complete `2^-43` open mechanics chamber, all predecessor-carrier deletion claims, its exact residual forcing-edge chamber, and bridge cardinalities below eight for the stated changed-face sets.

Not closed: every possible two-support placement or boundary, every alternate double-octahedral/prismatic pair, the third-support/three-cell successor, or the global existence problem.

## Artifacts

- Complete exact archive (`Calm_Quartz_90_wall242_second_support_exact_NONWINNER.zip`) — SHA-256 `39d06ed21786cdc27d5f572a10e3916949ad58ed682f517f6a32380d7225b861`.
- Full handoff (`Calm_Quartz_90_wall242_second_support_handoff.md`)
- Structured result (`Calm_Quartz_90_wall242_second_support_result.json`)
- Final clean verification receipt (`Calm_Quartz_90_wall242_second_support_clean_verification.json`)
- Exact generator (`generator_exact.json`)
- Supplied V-data (`input_vertices_exact.csv`)
- Own-centred active V-data (`active_vertices_centered_exact.csv`)
- Irredundant H-data (`second_support16_exact_H_irredundant.csv`)
- All face mechanics (`second_support16_exact_faces.csv`)
- All directed vertex primitives (`second_support16_exact_vertex_primitives.csv`)
- All true-edge cones (`second_support16_exact_true_edges_full_cones.csv`)
- Same-boundary replacement certificate (`second_support_shared_terminal_patch.json`)
- Minimal bridge certificate (`minimal_same_boundary_bridge.json`)
- Perturbation certificate (`own_centroid_perturbation_certificate.json`)
- Forcing-edge certificate (`residual_forced_edge_2152_2369.json`)
- Next-topology certificate (`first_successor_topology.json`)
- Independent verifier (`verify_independent.py`)
- Watertight OBJ (`body.obj`)
- Watertight STL (`body.stl`)

## Final statement

**NONWINNER, rigorously delimited.** The second support `G` resolves both predecessor nonflippable cores and deletes the complete old residual packet in one exact finite-thickness same-boundary event. The open target remains `(2,2,2)` because a new packet is born, and external-positive edge `[2152,2369]` forces a second unstable equilibrium. The next mathematically new topology is the third-support/three-cell full-star cancellation above.
