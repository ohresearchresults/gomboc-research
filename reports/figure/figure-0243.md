# figure-0243

AI research report · 2026-09-03 UTC

---

# Calm Quartz 90 — exact wall-242 sixth-support/full-star determination

The durable journal records the fifth-support body as a used exact nonwinner and identifies the required next move: a nonserial sixth-support/full-star event destroying the complete `[2369,2732]` carrier packet while preserving `[0,H,C]` and `C`. The acceptance gate is a finite uniform-density polyhedron at its own exact volume centroid, strict `(S,U,H)=(1,1,0)`, with complete incidence, mechanics, verification, and OBJ/STL; wall points and near-solutions do not count.

## Literal disposition

**EXACT DELIMITED NONWINNER.** No homogeneous convex polyhedral Gömböc occurs in the materialized sixth-support chamber.

The required predecessor packet is genuinely destroyed in one connected same-boundary full-hull surgery: sixth support `K=40011` becomes extreme, while old extra-unstable row `2369` and fifth support `J=40010` become strictly interior. The old forcing edge `[2369,2732]` disappears; old stable face `[1258,G,2152]` remains a face but becomes strictly nonstable; old saddle `[1975,H]` remains an edge but becomes strictly nonsaddle; old saddle `[C,J]` disappears with `J`.

The exact target is

```text
21 supplied dyadic points
16 active vertices; inactive {1371,2369,B,I,J}
(V,E,F,C)=(16,42,28,84)
(S,U,H)=(2,2,2)
```

Protected stable `[0,H,C]` and protected unstable `C` remain strict. The replacement packet is

```text
extra stable    [2152,G,3296]
extra unstable  K
saddles         [3290,C], [H,K]
forcing edge    [2732,K].
```

## Exact supplied generator

Every coordinate is the listed integer triple divided by `2^24=16777216`; `A=40001`, ..., `K=40011`.

```text
0     (   2382238,  -6308946,  46171779) active
1258  (   1620887,   4967418, -20558338) active
1371  (    105592,    109668,    616980) inactive
1975  (  10274573,  12571703,  48854565) active
2152  (    510389,  -7271935,  -5924598) active
2369  (    135538,     76357,    619136) inactive
2515  (   5028442,  -9339607,  26833667) active
2732  (   9156226,   4616735,  61197940) active
3290  (    661958, -10721838,  16427750) active
3296  (   3876214,  -1521484,   3638813) active
A     (   -351024,  -8978438,  25844631) active
B     (         0,         0,         0) inactive
C     ( -19656014, -12570508, -84150451) active
D     (  -2672244,   3411514, -42213909) active
E     (  -6361824,   2058745, -51264980) active
F     (  -4952003,   7634514, -41535864) active
G     (   7707303,   6512003,  11653439) active
H     (  -1678613,  11935619, -25478204) active
I     (     37357,    237671,    -70651) inactive
J     (     -7462,   -116421,     97771) inactive
K     (  20398692,  18092468,  82703156) active
```

Strict inactivity minima are

```text
1371  58266678944827239851/2361183241434822606848
2369  115301756268312958673/4722366482869645213696
B     57814616454008400101/2361183241434822606848
I     58211745611596340529/2361183241434822606848
J     115223418884450101171/4722366482869645213696.
```

All are positive.

## Exact ordinary volume and own centroid

```text
Vol = 11778784432573397890079/4722366482869645213696

centroid = (
355934988857757838904842115023/4742765055425311974139191361536,
203871321721498676388955661353/4742765055425311974139191361536,
110785788432194398360633989679/431160459584119270376290123776
).
```

After subtracting this one rational vector from every active vertex, exact signed tetrahedral integration gives `Mx=My=Mz=0`. No auxiliary mechanical centre is used.

## Actual irredundant incidence

The 28 outward maximal triangular faces are

```text
[0,2732,1975] [0,1975,H] [0,3290,2515] [0,2515,K]
[0,K,2732] [0,A,3290] [0,C,A] [0,H,C]*
[1258,2152,D] [1258,G,2152] [1258,D,K] [1258,K,G]
[1975,2732,K] [1975,K,H] [2152,3296,2515] [2152,2515,C]
[2152,G,3296]* [2152,C,D] [2515,3290,C] [2515,3296,G]
[2515,G,K] [3290,A,C] [C,E,D] [C,F,E]
[C,H,F] [D,E,F] [D,F,H] [D,H,K]
```

Asterisks mark stable faces. Every nonincident supplied point is strictly behind every supporting plane; the minimum Euclidean nonincidence distance is `0.0011764353828210637`.

The 42 physical true edges are

```text
[0,1975] [0,2515] [0,2732] [0,3290] [0,A] [0,C] [0,H] [0,K]
[1258,2152] [1258,D] [1258,G] [1258,K]
[1975,2732] [1975,H] [1975,K]
[2152,2515] [2152,3296] [2152,C] [2152,D] [2152,G]
[2515,3290] [2515,3296] [2515,C] [2515,G] [2515,K]
[2732,K] [3290,A] [3290,C]* [3296,G] [A,C]
[C,D] [C,E] [C,F] [C,H]
[D,E] [D,F] [D,H] [D,K] [E,F] [F,H] [G,K] [H,K]*
```

Asterisks mark saddles. Every edge has exactly two incident maximal faces and `16-42+28=2`; no display triangulation diagonal is counted.

## Exhaustive own-centroid mechanics

Exactly two faces are stable:

```text
[0,H,C], minimum barycentric coordinate
3754437567084090901115494790049431091618327688654865/
54611933398525851020347813012170296664868468942844452
≈ 0.06874756730706470

[2152,G,3296], minimum barycentric coordinate ≈ 0.28903034232125835.
```

Every other face has an exact negative Cramer witness; the closest excluded face is the predecessor face `[1258,G,2152]`, decision `≈-0.022399513604644893`.

Exactly two vertices are unstable: `C` and `K`. The minimum raw outgoing support of `K` is

```text
603576038053419458066328900567322306181/
79570393772122430857519627537823563776
≈ 7.5854348513339005.
```

Every other active vertex has a negative outgoing witness; the closest exclusion is `≈-0.03735587140577185`.

Exactly two edges are saddles:

```text
[3290,C] : (0.11255060949512788, 0.8874493905048721,
            0.3001640685226597, 0.8043039793551345)
[H,K]    : (0.2631907644589607, 0.7368092355410393,
            1.0023741296225466, 1.0297036599560647)
```

The tuples are edge-foot `t`, `1-t`, and the two incident full-normal-cone coefficients. Every other true edge has a negative component; the closest excluded normalized component is `≈-0.04996576718810855`. The supplied ledgers contain all 28 face decisions, all 84 directed vertex primitives, and all four components of all 42 true-edge cones.

## Connected positive-volume source/target surgery

The exact fifth-support source is augmented only by the strictly interior seed `K=(1,-2,3)/2^24`. Source and target hulls are reconstructed independently. Their changed face sets become dual-connected one-boundary-component disks after adding the single common bridge face `[0,2515,3290]`; an exhaustive four-subset replay proves no zero-face bridge works.

The common boundary cycle is

```text
0–2732–1975–H–D–1258–G–2515–C–A–0.
```

Source patch `(V,E,F)=(13,26,14)`:

```text
[0,2369,2515] [0,2369,2732] [0,2515,3290] [0,3290,J]
[0,A,J] [1258,D,H] [1258,G,H] [1975,2369,2732]
[1975,2369,G] [1975,G,H] [2369,2515,G] [2515,3290,J]
[2515,C,J] [A,C,J]
```

Target patch `(V,E,F)=(12,23,12)`:

```text
[0,2515,3290] [0,2515,K] [0,2732,K] [0,3290,A]
[1258,D,K] [1258,G,K] [1975,2732,K] [1975,H,K]
[2515,3290,C] [2515,G,K] [3290,A,C] [D,H,K]
```

Both have Euler characteristic one, one boundary component, connected dual graph, and strictly positive centroid-cone volumes. The exact smallest source and target cone volumes are approximately `0.006359325650825063` and `0.022121980382578017`.

Exact removed edges:

```text
[0,2369] [0,J] [1258,H] [1975,2369] [1975,G]
[2369,2515] [2369,2732] [2369,G]
[2515,J] [3290,J] [A,J] [C,J] [G,H]
```

Exact inserted edges:

```text
[0,K] [1258,K] [1975,K] [2515,K] [2732,K]
[3290,A] [3290,C] [D,K] [G,K] [H,K]
```

Inherited edges with changed incident stars:

```text
[0,2515] [0,2732] [0,3290] [0,A]
[1258,D] [1258,G] [1975,2732] [1975,H]
[2515,3290] [2515,C] [2515,G] [A,C] [D,H]
```

This is an exact full-hull same-boundary surgery, not a frozen-fan count. It does not claim that all supporting circuits vanish at one scalar parameter; the actual coordinate chord and its mechanics chronology are separately certified.

## Complete lineage deletion and anti-carrier census

The source packet is destroyed rather than relabelled:

```text
[2369,2732] absent;
2369 strictly inactive;
[C,J] absent and J strictly inactive;
[1258,G,2152] strictly nonstable;
[1975,H] strictly nonsaddle.
```

The external-arrow census checks all 42 target edges, all 10 inserted edges, and all 13 inherited star-changed edges. Twenty-two of the 23 changed edges have an exact negative external-arrow witness. The unique adverse changed edge is `[2732,K]`; unchanged `[C,E]` is all-positive only inside the protected unstable-`C` star.

For `[2732,K]`, all external endpoint arrows are positive, with exact minimum

```text
93621221252805233524080925440866741809/
39785196886061215428759813768911781888
≈ 2.353167222495398.
```

The mutual arrows are

```text
sigma(2732→K)=
-385773290275497265915492771638959674685/
79570393772122430857519627537823563776

sigma(K→2732)=
603576038053419458066328900567322306181/
79570393772122430857519627537823563776
```

and

```text
sigma(2732→K)+sigma(K→2732)
=||p_K-p_2732||²
=770462736855101/281474976710656>0.
```

Thus both endpoints cannot be nonunstable while their external arrows stay positive. One endpoint is unstable in addition to strict unstable `C`; the full certified chamber has `U>=2`.

## Exact death-before-birth chronology

Along the exact coordinate chord from source to target, three decisive roots are isolated in disjoint rational intervals:

```text
K unstable / [2732,K] saddle birth:
[1699866934199347637484623/2417851639229258349412352,
 10199201605196085824907739/14507109835375550096474112]
≈ 0.7030484859448268

target stable [2152,G,3296] birth:
[91521849545357744719427329/96714065569170333976494080,
 9152184954535774471942733/9671406556917033397649408]
≈ 0.9463137446114382

source stable [1258,G,2152] death:
[92141263308516489052883137/96714065569170333976494080,
 184282526617032978105766277/193428131138340667952988160]
≈ 0.9527183328118560.
```

Hence replacement carrier birth precedes replacement stable birth, which precedes old stable death. Exact rational witnesses also show:

```text
t=329/5000: old [C,J] and new [3290,C] saddles coexist, class (3,2,3)
t=167/250: old [1975,H] and new [H,K] saddles coexist, class (3,2,3)
t=19/20: old and new stable faces coexist, class (3,2,3).
```

The canonical connector therefore has no death-before-birth `(1,1,0)` interval.

## Positive own-centroid chamber

Independent perturbations of all 63 uncentred supplied coordinates by

```text
|delta r_ij|<=2^-29=1/536870912
```

preserve, after outward interval recomputation of volume, all moments, and the dependent centroid, the 16/42/28 incidence, five inactive rows, strict `(2,2,2)` mechanics, all 84 vertex primitives, all 168 true-edge cone components, all 22 anti-carrier witnesses, and the `[2732,K]` forcing theorem.

Box-wide lower clearances are approximately

```text
topology/nonincidence    0.0011044946894903094
inactive rows            0.024399389552787573
chosen face signs        0.0038792198490702405
chosen vertex signs      0.03735579424493932
chosen edge components   0.000033545248226361176
forcing external arrows  2.353166550948349
anti-carrier witnesses   0.008505563445613974.
```

## Exact scope and next topology

Closed exactly: this one-`K`, released-`2369/J` topology; its full `2^-29` chamber; destruction of every fifth-support equilibrium; the complete changed-edge arrow census; the connected source/target disk; the isolated chronology roots; and the `[2732,K]` forcing chamber.

Not closed: every possible sixth-support placement or released-row set, every two-support antiprismatic/double-octahedral cage, or the global existence problem.

The endpoint exposes

```text
[2732,K] -> [0,1975]      illegal ordinary flip: [0,1975] already exists
[G,3296] -> [2152,2515]   illegal ordinary flip: [2152,2515] already exists
[3290,C] -> [2515,A]      legal saddle exchange
[H,K] -> [1975,D]         legal saddle exchange.
```

The first nonrepeating successor is a seventh support `L`, or a two-support antiprismatic/double-octahedral carrier cage, releasing or deactivating one of `{0,1975,2732,K}` while jointly destroying `[2732,K]`, stable `[2152,G,3296]`, and both saddles, preserving `[0,H,C]` and `C`, and imposing negative arrows on every inserted or star-changed nonprotected edge before dependent moment closure.

## Independent clean replay

The package independently reruns deterministic exact generation, chronology augmentation, the directed interval proof, primary Fraction reconstruction, a standard-library-only clean-room reconstruction, exact bridge enumeration, and OBJ/STL verification. It ends with

```text
DETERMINISTIC_EXACT_SIXTH_SUPPORT_GENERATOR_PASS
EXACT_CHRONOLOGY_AUGMENT_PASS
OWN_CENTROID_INTERVAL_SIXTH_SUPPORT_CERTIFICATE_PASS
PRIMARY_EXACT_SIXTH_SUPPORT_NONWINNER_PASS
INDEPENDENT_CLEAN_ROOM_SIXTH_SUPPORT_NONWINNER_PASS
EXACT_MINIMAL_SIXTH_SUPPORT_BRIDGE_PASS
WATERTIGHT_SIXTH_SUPPORT_ENDPOINT_MESH_PASS
ALL_CALM_QUARTZ_90_WALL242_SIXTH_SUPPORT_VERIFIERS_PASS
CALM_QUARTZ_90_WALL242_SIXTH_SUPPORT_PACKAGE_PASS.
```

OBJ and STL agree on 16 vertices, 28 outward triangular faces, 42 edge classes, Euler characteristic two, and edge multiplicity two.

## Final statement

**NONWINNER, rigorously delimited.** Sixth support `K` and release of `2369,J` genuinely destroy the complete fifth-support packet in a connected exact positive-volume full-star surgery. The target remains an open exact own-centred `(2,2,2)` body because inserted edge `[2732,K]` is the unique adverse changed carrier, and the exact connector births replacement features before the old stable component dies.

## Artifacts

- Complete exact archive (`Calm_Quartz_90_wall242_sixth_support_exact_NONWINNER.zip`)
- Full handoff (`Calm_Quartz_90_wall242_sixth_support_handoff.md`)
- Structured result (`Calm_Quartz_90_wall242_sixth_support_result.json`)
- Clean verification receipt (`Calm_Quartz_90_wall242_sixth_support_clean_verification.json`)
- Clean replay (`Calm_Quartz_90_wall242_sixth_support_clean_replay.txt`)
- Exact generator (`generator_exact.json`)
- Exact own-centred V-data (`active_vertices_centered_exact.csv`)
- Primitive H-data (`sixth_support16_exact_H_irredundant.csv`)
- Face ledger (`sixth_support16_exact_faces.csv`)
- Directed vertex ledger (`sixth_support16_exact_vertex_primitives.csv`)
- True-edge full-cone ledger (`sixth_support16_exact_true_edges_full_cones.csv`)
- External-arrow census (`external_arrow_full_ledger.csv`)
- Transition certificate (`sixth_support_shared_global_patch.json`)
- Chronology certificate (`source_to_target_death_before_birth_obstruction.json`)
- Perturbation certificate (`own_centroid_perturbation_certificate.json`)
- Independent verifier (`verify_independent.py`)
- Watertight OBJ (`body.obj`)
- Watertight STL (`body.stl`)
