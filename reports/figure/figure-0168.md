# figure-0168

Historical AI scientific report · saved 2026-08-30 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Sharp Maple 55 — exact joint-component fixed-lattice determination

## Literal verdict

**No strict own-centred `(S,U,H)=(1,1,0)` metric image was certified.** The required target is a literal finite uniform-density polyhedron evaluated at its own exact volume centroid, with exhaustive positive-margin face/vertex/true-edge verification and a materialized mesh; wall points and auxiliary centres do not qualify. :contentReference[oaicite:0]{index=0}

What *was* completed is an exact multidimensional nonwinner atlas plus a new exact closure of the formerly unordered connector:

- 11 genuine rank-2/3/4 wall plaques;
- 76 pairwise-disjoint full-dimensional trace-one SPD boxes and 112 exact plaque-adjacency edges;
- complete 25,932-face-wall, 25,932-vertex-wall, and 12,966 four-component true-edge-cone audits for every primary box;
- exact simultaneous treatment of all four assignment-nominated failures;
- an exact full-dimensional `S>=2` tube from `B8R_ridge_mm` to the isolated `B8_alt` chamber;
- four new exact full-dimensional orthant boxes around the closest subsequent two-death pair, again all with `S>=2`.

The recovered exact atlas’s literal verdict is likewise no winner; every primary box has at least two stable faces, and it explicitly avoids claiming global exclusion of the unresolved compact SPD core. :contentReference[oaicite:1]{index=1}

## Fixed exact body and hard centring

The fixed polar is

```text
Q=conv{q_i},     q_i=Qint_i/2^48,     i=0,...,4323.
```

All 4,324 rows are irredundant. Its unique Santaló point is isolated in

```text
a_* = 2^-120(-39878490350125864373364388380978345,
              88581653811863381217051,
              819441514472273259270856)
      + [-2^-90,2^-90]^3.
```

Set `P_*=(Q-a_*)^∘`. Santaló stationarity gives the exact ordinary first moment

```text
∫_(P_*) x dx = 0.
```

For a trace-one inverse metric `K∈SPD(3)`, put `A=K^(-1/2)` and `P_K=A P_*`. Then

```text
∫_(P_K) y dy = det(A) A ∫_(P_*) x dx = 0,
```

so every reported metric image remains at its own uniform-volume centroid. Translation and the invertible map preserve the actual incidence lattice

```text
(H,V,E)=(4324,8644,12966),     8644-12966+4324=2.
```

The deterministic transformed generator is

```text
h_i(K)=A^(-T)(q_i-a_*),
v_f(K)=A y_f/(1-a_*·y_f),
```

where each exact baseline `y_f` is reconstructed from its three active support rows. The source bundle contains all 8,644 active triples, all 4,324 maximal-face cycles, all 12,966 true edges, and all 17,284 boundary triangles. :contentReference[oaicite:2]{index=2}

## Exact trace-one wall arrangement

Use coordinates

```text
(K00,K11,K01,K02,K12),     K22=1-K00-K11.
```

Every primary centre and box radius is dyadic; all primary boxes have coordinatewise radius `2^-60`. Exact interval Sylvester minors prove positive definiteness throughout each box.

The complete metric mechanics are

```text
S_ij(K)=(q_i-a_*)^T K(q_i-q_j),
W_fg(K)=d_g y_f^T adj(K)y_f-d_f y_f^T adj(K)y_g,
d_f=1-a_*·y_f>0.
```

A face is stable iff every outgoing `S_ij` is positive. A vertex is unstable iff every outgoing `W_fg` is positive. For a true edge with incident faces `(i,j)` and endpoints `(f,g)`, strict saddle status requires all four components

```text
S_ij>0, S_ji>0, W_fg>0, W_gf>0.
```

Thus a primary cell audit contains 51,864 directed signs and the complete four-component ledger for 12,966 actual edges, not triangulation diagonals. :contentReference[oaicite:3]{index=3}

## The four requested certificate failures

The assignment’s two joint transitions were resolved exactly, not serially:

| exact rank-two plaque | two directed failures | four full-dimensional orthants | class in every orthant | surviving strict packet |
|---|---|---:|---|---|
| `O_paired_failure_ridge` | `4633: 796→760@e2316`; `21776: 3618→3619@e10888` | 4 | `(2,2,2)` | stable `{1512,2791}`, unstable `{4409,3885}`, saddles `{2108,10784}` |
| `B_paired_failure_ridge` | `12042: 1984→2055@e6021`; `17162: 2847→2883@e8581` | 4 | `(2,2,2)` | stable `{1309,2974}`, unstable `{7335,2514}`, saddles `{5807,6810}` |

Only the two named primitives vary within each initial plaque; all other 51,862 directed signs are fixed. Every one-wall edge is count- and feature-neutral. Therefore the four first certificate failures are mechanically inert and cannot be the desired two-death chamber. :contentReference[oaicite:4]{index=4}

## Exact multidimensional atlas

| plaque | rank | children | exact class histogram |
|---|---:|---:|---|
| `O_paired_failure_ridge` | 2 | 4 | `(2,2,2)`×4 |
| `B_paired_failure_ridge` | 2 | 4 | `(2,2,2)`×4 |
| `O2_paired_failure_ridge` | 2 | 4 | `(4,4,6)`×1, `(5,4,7)`×2, `(6,4,8)`×1 |
| `B2_paired_failure_ridge` | 2 | 4 | `(3,4,5)`×1, `(4,4,6)`×2, `(5,4,7)`×1 |
| `B3_three_replacement_death_ridge` | 3 | 8 | `(2,5,5)`×1, `(3,5,6)`×3, `(4,5,7)`×3, `(5,5,8)`×1 |
| `B4_rank_3_stable_transfer_ridge` | 3 | 8 | `(2,5,5)`×1, `(3,5,6)`×3, `(4,5,7)`×3, `(5,5,8)`×1 |
| `B5_rank_3_stable_transfer_ridge` | 3 | 8 | `(2,4,4)`×1, `(3,4,5)`×3, `(4,4,6)`×3, `(5,4,7)`×1 |
| `B6_rank_3_stable_transfer_ridge` | 3 | 8 | `(2,3,3)`×1, `(3,3,4)`×3, `(4,3,5)`×3, `(5,3,6)`×1 |
| `B7_rank_3_stable_transfer_ridge` | 3 | 8 | `(2,2,2)`×1, `(3,2,3)`×3, `(4,2,4)`×3, `(5,2,5)`×1 |
| `B8R_rank_2_alternative_ridge` | 2 | 4 | `(4,3,5)`×4 |
| `O3_rank_4_stable_transfer_ridge` | 4 | 16 | `(16,33,47)`×1, `(17,33,48)`×4, `(18,33,49)`×6, `(19,33,50)`×4, `(20,33,51)`×1 |

Every primary box is exactly outside all 289 inherited Löwner-relative cells/balls. Sixty-eight lie in the previously unresolved compact spectral core; the eight B7 boxes instead lie in the earlier spectral `U>=2` exclusion. The exact five-coordinate volume of all 76 disjoint boxes is

```text
19 / 15914343565113172548972231940698266883214596825515126958094847260581103904401068017057792,
```

and the exact volume newly removed from the unresolved compact core is

```text
17 / 15914343565113172548972231940698266883214596825515126958094847260581103904401068017057792.
```

The B-side best orthants form the exact transfer rail

```text
B2_mm   (3,4,5)
B3_mmm  (2,5,5), stable {1309,2974}
B4_mmm  (2,5,5), stable {1274,3009}
B5_mmm  (2,4,4), stable {1239,3044}
B6_mmm  (2,3,3), stable {1204,3079}
B7_mmm  (2,2,2), stable {1169,3114}.
```

It moves both stable components in lockstep but never opens `S=1`; the O-side plaques proliferate the Euler-neutral block instead. :contentReference[oaicite:5]{index=5}

## Strongest exact primary endpoint

The largest-clearance adjacency-certified endpoint is the full-dimensional nonwinner `B_ridge_pp`:

```text
K = 2^-110 *
[ 364193221987698054887785302589440,  156520488794118534439665024368640, -385463157847420813153068023545856 ]
[ 156520488794118534439665024368640,  279152393330315094901727910952960, -148983022891506660761965042860032 ]
[-385463157847420813153068023545856, -148983022891506660761965042860032,  654728599315693757343110868762624 ]

coordinatewise box radius = 2^-60
class                     = (2,2,2)
stable rows               = {1309,2974}
unstable vertices         = {7335,2514}
saddle edges              = {5807,6810}.
```

Exact box-wide Sylvester lower bounds are

```text
K00 > 323468560370530559 / 1152921504606846976,

det(K[0:2,0:2]) >
1902307162909816762367806018707265 /
41538374868278621028243970633760768,

det(K) >
6635090991776893024657573346807202434910086747082319 /
766247770432944429179173513575154591809369561091801088.
```

The minimum complete directed-wall clearance is

```text
25108406876049547998209243109191209396966774129363739414705 /
107839786668602559178668060348078522694548577690162289924414440996864
≈ 2.3283064304651332×10^-10.
```

Its complete sign-payload SHA-256 is

```text
df82fabfe44e9974439aa81f4ec2c058e00d394514c7ecad1dd766f18be08274.
```

The deterministic H/V reconstruction and matching nonwinner OBJ/STL contain 4,324 H rows, 8,644 vertices, 12,966 true edges and 17,284 boundary triangles; every triangulated boundary edge has multiplicity two. :contentReference[oaicite:6]{index=6}

## New exact result: the formerly unordered `B8R→B8_alt` connector is entirely `S>=2`

The inherited result had an exact isolated `B8_alt` box but no ordered all-wall connector from `B8R_ridge_mm`; that was its first unclassified boundary. :contentReference[oaicite:7]{index=7}

I replaced the unnecessary root-ordering obligation by a stronger region certificate. The existing exact connector-domain object covers the complete affine centre segment

```text
x(t)=x_left+t(x_right-x_left),     0≤t≤1,
```

thickened coordinatewise by `2^-60`, using four exact parameter boxes that tile `[0,1]`. Each piece has positive exact Sylvester bounds, lies in the unresolved compact spectral core, and carries positive witnesses against all 289 inherited relative cells.

`CONNECTOR_STABLE_CERTIFICATE.json` independently evaluates all twelve outgoing stable-face primitives for rows `1378` and `2903` over every one of those four boxes, while propagating the complete `a_*±2^-90` uncertainty. Every lower endpoint is positive. The global minima are

```text
row 1378:
21787694382235710358811470288470647219791731214773993421840723573 /
215679573337205118357336120696157045389097155380324579848828881993728
≈ 1.0101881251485809×10^-4,

row 2903:
11131030573003186367794577655653532969957421984374233709423396505 /
53919893334301279589334030174039261347274288845081144962207220498432
≈ 2.0643643532436575×10^-4.
```

Therefore both rows are strictly stable throughout the entire connected full-dimensional tube, proving

```text
S>=2
```

without needing to order its dense mechanically neutral wall packet. The verifier recomputes the four-box tiling, exact trace-one SPD minors, source hashes, and all twelve interval signs and ends in `PASS`.

## New exact result: first nearby two-death pair also transfers both stable components

From `B8_alt`, the closest numerically located pair of outgoing stable-death walls is

```text
8129:  1378→1343 on true edge 4064,
17494: 2903→2938 on true edge 8747.
```

I exactified all four target-sign orthants as rational trace-one SPD boxes of radius `2^-100`. The two wall coefficient rows have a positive exact rank-two Gram determinant at the midpoint of the isolated Santaló box, and the target wall intervals retain their prescribed signs after full root-box propagation.

More decisively, in **every** orthant all six outgoing primitives of row `1343` and all six outgoing primitives of row `2938` are strictly positive. The weakest replacement-row lower margin remains approximately `3.8664×10^-5`. Hence every exact orthant has stable rows containing `{1343,2938}` and therefore `S>=2`.

The complete numerical finite-lattice classifications, included only as discovery evidence rather than exact class claims, are

```text
-- : (2,7,7), stable {1343,2938}
-+ : (3,7,8), stable {1343,2903,2938}
+- : (3,7,8), stable {1343,1378,2938}
++ : (4,7,9), stable {1343,1378,2903,2938}.
```

Thus this first nearby simultaneous death does not cancel the two stable components; it replaces them with rows `1343` and `2938` while the unstable/saddle population proliferates. These four boxes are deliberately reported as isolated exact boxes: I do **not** claim an inherited-cell nonmembership connector from `B8_alt` to their ridge.

A second nearby numerical wall pair, `8342 (1378→1413)` with `17287 (2903→2868)`, similarly has common-death class `(2,6,6)` with replacement stable rows `{1413,2868}`; it remains explicitly noncertifying discovery data.

## Verification and artifact boundary

The recovered clean-room verifier reconstructs the support/vertex lattice, positive projective denominators, actual maximal faces and true edges; it verifies all 11 plaques, all 76 orthants, all 112 adjacency edges, 289 exact nonmembership checks per box, every complete edge cone, disjoint-box volumes, and the endpoint OBJ/STL, and its transcript ends in `PASS`. :contentReference[oaicite:8]{index=8} :contentReference[oaicite:9]{index=9}

The compact transfer archive contains the exact source generator/topology/wall system, the atlas ledgers and ridge equations, the strongest endpoint H/V/incidence/OBJ/STL, the new connector certificate and verifier, the four exact `8129/17494` orthant boxes and verifier, source hashes, and the exact continuation seed:

- [Download the exact Sharp Maple 55 archive](sandbox:/mnt/data/Sharp_Maple_55_exact_joint_SPD_atlas.zip)
- [Read the standalone handoff](sandbox:/mnt/data/sharp_maple55/SHARP_MAPLE55_HANDOFF.md)
- [Connector stable-subset certificate](sandbox:/mnt/data/sharp_maple55/CONNECTOR_STABLE_CERTIFICATE.json)
- [Exact `8129/17494` orthant certificate](sandbox:/mnt/data/sharp_maple55/PAIR_8129_17494_EXACT_ORTHANTS.json)
- [Strongest endpoint exact certificate](sandbox:/mnt/data/sharp_maple55/STRONGEST_ENDPOINT_EXACT_CERTIFICATE.json)

Archive SHA-256:

```text
fcaccb3ddf932c99deef13427fa960a6d99b41787b5865f90a32632065213601
```

Fresh extraction was tested with

```bash
python verify_connector_stable.py
python verify_pair8129_17494.py
python verify_endpoint_materialization.py
```

and all three checks ended in `PASS`.

## Honest exclusion boundary and most useful continuation

Certified facts stop at the following boundary:

1. all 76 primary plaque children are exact nonwinners;
2. all 15 separately audited isolated discovery boxes have `S>=2`;
3. the full-dimensional `B8R_ridge_mm→B8_alt` connector tube has `S>=2`;
4. all four exact isolated orthants around walls `8129/17494` have `S>=2`;
5. no global exclusion of the remaining bounded trace-one SPD core has been proved.

The **first unresolved joint transition** is now the actual all-wall connector from `B8_alt` to the `8129/17494` rank-two neighborhood, including exact avoidance of the inherited 289 cells. Merely exactifying those two deaths further is redundant: their four exact orthants already retain `{1343,2938}`. The next useful plaque must include at least one additional mechanically decisive wall that suppresses `1343` or `2938` in the same event—preferably a rank-three-or-higher intersection—while every intervening affine face root and zero/one/two-root adjugate-quadratic vertex wall is ordered and the full 12,966-edge cone ledger is renewed.

The exact rational wall coefficients and nearest-plane seed are in `FIRST_UNRESOLVED_JOINT_TRANSITION.json`. A serial transfer along either wall is now closed; the only evidence-supported continuation is a higher-codimension shared event that kills a replacement row before another stable–saddle birth.
