# figure-0211

AI research report · 2026-09-02 UTC

---

# Calm Quartz 90 — exact wall-242 fifth-circuit shared-terminal handoff

## Disposition

**EXACT DELIMITED NONWINNER.** No homogeneous convex polyhedral Gömböc was obtained in this topology.

The first unclassified successor was nevertheless realized literally: one new extreme support `F=40006` and one rebuilt, same-boundary, dual-connected full-hull disk jointly implement

```text
[2515,2732] -> [2152,2369]
[1258,B]     -> [3296,D]
[3290,D]     -> [2152,C]
```

and replace the nonflippable `{2369,E,C,D}` core by the four-face `F` star `[2369,C,F]`, `[2369,D,F]`, `[C,E,F]`, `[D,E,F]`. The strict target is exact own-centred `(V,E,F,C)=(16,42,28,84)`, `(S,U,H)=(2,2,2)`. It preserves intended stable `[0,1371,C]` and intended unstable `C`, but the unwanted block transfers to stable `[3296,D,B]`, unstable `2732`, and saddles `[2152,C]`, `[2369,F]`.

The journal requires a finite own-centred strict `(1,1,0)` body with complete incidence, margins, independent verification, and OBJ/STL; a wall point or near-object is not completion. The accepted four-circuit endpoint and this exact fifth-circuit frontier are recorded in the supplied state.

## Exact dyadic generator

All input coordinates use denominator `2^36=68719476736`; `A=40001`, `B=40002`, `C=40003`, `D=40004`, `E=40005`, `F=40006`.

```text
0     (  9378388933,-11594645177,  2638057617) / 68719476736
1258  (  -791616963, -5186033776, -1954151339) / 68719476736
1371  ( 20533807260,-19231841783,  1984449931) / 68719476736
1975  ( 31422685368,-28549279635,   534698749) / 68719476736
2152  ( 22940876470,-39536912493, -1275861574) / 68719476736
2369  ( 35069233435,-24855026299, -1070552959) / 68719476736
2515  ( 20221544736,-14321724831, -2268922457) / 68719476736
2732  ( 34449492888,-40241432189,   316281769) / 68719476736
3290  ( -4129247193, -3233468353,  1671812652) / 68719476736
3296  (  4592632445, -7417252247, -2510768383) / 68719476736
A     (-14118820976, 12012781769,  2576465504) / 68719476736
B     ( -1119466790,  3655657888, -2311537929) / 68719476736
C     (-48419990772, 52592465268,  2960041282) / 68719476736
D     (-44052640793, 49701083109, -1276610693) / 68719476736
E     (-43138791274, 49531829471,   672193144) / 68719476736
F     (-21968674046, 30793393044,   197883587) / 68719476736
```

Exact volume:

```text
22697888073191491144419817279943/1947111321950560360698936123457536
```

Exact uncentred ordinary-volume centroid:

```text
cx=26854135592001754727540294305605/6239147965608058163888430599145655151624192
cy=-20939166268284047087506565204547/3119573982804029081944215299572827575812096
cz=4241276796759904114636341803477/3119573982804029081944215299572827575812096
```

Subtracting this one rational vector from all vertices gives exact centred first moments `(0,0,0)`. No auxiliary mechanical centre is used.

## Actual hull and mechanics

All 16 supplied points are active. The complete maximal-face list is:

```text
[0,2732,1371] [0,1371,C] *S* [0,2152,2732] [0,3290,2152]
[0,A,3290] [0,C,A] [1258,3296,2152] [1258,2152,D]
[1258,D,3296] [1371,1975,2369] [1371,2732,1975] [1371,2369,C]
[1975,2732,2369] [2152,2515,2369] [2152,2369,2732] [2152,3296,2515]
[2152,3290,C] [2152,C,D] [2369,2515,D] [2369,F,C]
[2369,D,F] [2515,3296,B] [2515,B,D] [3290,A,C]
[3296,D,B] *S* [C,E,D] [C,F,E] [D,E,F]
```

The complete true-edge list is:

```text
[0,1371] [0,2152] [0,2732] [0,3290] [0,A] [0,C]
[1258,2152] [1258,3296] [1258,D] [1371,1975] [1371,2369] [1371,2732]
[1371,C] [1975,2369] [1975,2732] [2152,2369] [2152,2515] [2152,2732]
[2152,3290] [2152,3296] [2152,C] *H* [2152,D] [2369,2515] [2369,2732]
[2369,C] [2369,D] [2369,F] *H* [2515,3296] [2515,B] [2515,D]
[3290,A] [3290,C] [3296,B] [3296,D] [A,C] [B,D]
[C,D] [C,E] [C,F] [D,E] [D,F] [E,F]
```

Each edge has exactly two incident maximal faces and `16-42+28=2`. Minimum Euclidean nonincidence separation is `0.0068516545196972718`.

The exhaustive own-centroid equilibrium ledger is:

```text
stable   [0,1371,C], [3296,D,B]
unstable 2732, C
saddles  [2152,C], [2369,F]
```

Stable-face foot minima are `0.23240886478769626` and `0.04049226993941756`. Unstable raw directed-support minima are `0.0900651079214214` at `2732` and `0.07963647623810949` at `C`. Saddle normalized four-component tuples are

```text
[2152,C] (0.38865587484937497,0.6113441251506251,0.5352910333976949,0.5920351427851055)
[2369,F] (0.532894824887004,0.46710517511299593,0.659277787173778,0.8311591723167231).
```

Closest exclusions are: face `[2515,3296,B]` at `-0.054039163952644145`; vertex `3290` raw `-0.0009592046565531278` (normalized about `-0.011545605969649618`); edge `[3296,B]` has a negative normalized cone component about `-5.08884671798031`. Full exact values are in the H/face/vertex/edge ledgers.

## Exact higher-valence full-hull replacement

The source and target replace one disk with the same five-edge boundary

```text
[2152,2732], [2152,3290], [2369,2732], [2369,C], [3290,C].
```

Source patch: `(V,E,F)=(11,25,15)`, `chi=1`, one boundary component, dual-connected:

```text
[1258,2152,3296]
[1258,2152,D]
[1258,3296,B]
[1258,B,D]
[2152,2515,2732]
[2152,2515,3296]
[2152,3290,D]
[2369,2515,2732]
[2369,2515,D]
[2369,C,E]
[2369,D,E]
[2515,3296,B]
[2515,B,D]
[3290,C,D]
[C,D,E]
```

Target patch: `(V,E,F)=(12,28,17)`, `chi=1`, one boundary component, dual-connected:

```text
[1258,2152,3296]
[1258,2152,D]
[1258,3296,D]
[2152,2369,2515]
[2152,2369,2732]
[2152,2515,3296]
[2152,3290,C]
[2152,C,D]
[2369,2515,D]
[2369,C,F]
[2369,D,F]
[2515,3296,B]
[2515,B,D]
[3296,B,D]
[C,D,E]
[C,E,F]
[D,E,F]
```

The two hulls share exactly 11 exterior faces. Removed true edges are `[1258,B]`, `[2369,E]`, `[2515,2732]`, `[3290,D]`; inserted true edges are `[2152,2369]`, `[2152,C]`, `[2369,F]`, `[3296,D]`, `[C,F]`, `[D,F]`, `[E,F]`. Every source and target patch triangle has strictly positive exact centroid-cone volume. This proves a genuine finite-thickness same-boundary whole-disk event, not a frozen-lattice or serial-flip count. No scalar simultaneous common-wall homotopy is claimed.

## Positive open neighbourhood

Independent perturbations of all 48 uncentred coordinates by

```text
|delta r_ij| <= 2^-32 = 1/4294967296
```

preserve the exact `(16,42,28)` hull and `(2,2,2)` class after interval recomputation of ordinary volume, all three first moments, and the common centroid `M/V`. The interval proof audits every maximal face, every directed vertex primitive, and all four components of all 42 true-edge cones. Its global lower clearances are approximately

```text
topology             0.00023370432081882742
face signs           4.3351364832428027e-05
vertex signs         0.00095917302507136904
edge-cone components 1.4060740766359909e-08
```

## Exact residual obstruction

True edge `[2152,2732]` has incident faces `[0,2152,2732]` and `[2152,2369,2732]`. Every external endpoint support is positive; the exact minimum is

```text
27464740198181622941928429604228899538218619482062043/428750983475064681087465881857540390667517214758797312
```

The mutual supports are

```text
-3289388455961350631677850187948890408922828461297687/53593872934383085135933235232192548833439651844849664
9653875899524316676865500245878855257875890089484401/107187745868766170271866470464385097666879303689699328
```

and their exact sum is

```text
||p_2732-p_2152||^2=135479520283370298789/4722366482869645213696>0.
```

Thus both endpoints cannot be nonunstable while all external supports remain positive. At least one endpoint is unstable in addition to strict unstable `C`, so `U>=2` throughout the certified chamber.

## First new topology

The forcing edge can legally exchange `[2152,2732] -> [0,2369]`, and saddle `[2152,C]` can legally exchange to `[3290,D]`. But the extra-stable limiting edge `[3296,B]` is nonflippable because opposite edge `[2515,D]` already exists, while saddle `[2369,F]` is nonflippable because opposite `[C,D]` already exists.

The smallest evidenced successor is therefore a second support `G`, or an equivalent double-octahedral/triangular-prismatic two-cell, that simultaneously deletes `[2152,2732]`, resolves both nonflippable cores, crosses `[2152,C]`, and suppresses replacement birth. A provisional 17-vertex/30-face two-support sphere was numerically realized and searched through 500,000 metric trials without a winner, but it was not exactified and is not part of the theorem.

## Verification

A deterministic exact generator, primary exact verifier, directed own-centroid interval verifier, standard-library-only independent clean-room verifier, and mesh verifier all pass. Clean extraction checks all 41 manifested files before and after replay. OBJ: 16 vertices, 28 faces, 42 edge classes, every edge multiplicity two. STL: 28 matching facets.

**Final statement:** the one-support fifth-circuit topology is an exact open nonwinner. It genuinely deletes the predecessor carriers but transfers the Euler-neutral block. The second-support/two-cell topology above is the first unclassified successor.

## Artifacts

- Complete exact archive (`Calm_Quartz_90_wall242_fifth_circuit_exact_NONWINNER.zip`)
- Full detailed handoff (`Calm_Quartz_90_wall242_fifth_circuit_handoff.md`)
- Structured result (`Calm_Quartz_90_wall242_fifth_circuit_result.json`)
- Clean verification receipt (`Calm_Quartz_90_wall242_fifth_circuit_clean_verification.json`)
- Exact generator (`generator_exact.json`)
- Own-centred V-data (`vertices_centered_exact.csv`)
- Irredundant H-data (`postterminal16_exact_H_irredundant.csv`)
- All face mechanics (`postterminal16_exact_faces.csv`)
- All directed vertex primitives (`postterminal16_exact_vertex_primitives.csv`)
- All true-edge cones (`postterminal16_exact_true_edges_full_cones.csv`)
- Whole-disk certificate (`higher_valence_shared_terminal_patch.json`)
- Perturbation certificate (`own_centroid_perturbation_certificate.json`)
- Forced-edge certificate (`residual_forced_edge_2152_2732.json`)
- Next-topology certificate (`first_successor_topology.json`)
- Independent verifier (`verify_independent.py`)
- Watertight OBJ (`body.obj`)
- Watertight STL (`body.stl`)

```text
archive SHA-256  45ffb36e6aa1fca5f4d2cd04117416d9a2f4fdef70e1f23c21f08fb7b8ed49b0
archive bytes    141222
manifest entries 41
clean extraction PASS
```
