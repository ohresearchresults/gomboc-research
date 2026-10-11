# figure-0173

Historical AI scientific report · saved 2026-09-01 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Calm Quartz 90 — exact fixed-lattice determination

## Literal disposition

**RIGOROUS DELIMITED NONWINNER.** No open trace-one SPD metric box with strict own-centred `(S,U,H)=(1,1,0)` was found. The first genuinely open joint transition beyond `B8_alt` was nevertheless resolved exactly: the actual all-wall connector, a rank-two coupled stable-death plaque, all four adjacent full-dimensional orthants, and the first rank-three extension were materialized on the unchanged Santaló-centred lattice. Every certified connector chamber and every certified positive-radius box has at least two stable equilibria. This closes the exact frontier left open in the supplied journal, but it does **not** exclude the remaining compact SPD core globally. :contentReference[oaicite:0]{index=0}

## Recovery and independent rerun

The transport-interrupted continuation had left a complete immutable archive in the user library. I materialized it, verified the outer archive SHA-256, checked all 133 internally manifested files byte-for-byte, and ran the independent verifier from a fresh extraction. It returned `PASS`, reconstructed the complete lattice, replayed all 2,101 ordered wall roots, and audited all sixteen open metric boxes. The recovered handoff gives the exact family and complete wall system. :contentReference[oaicite:1]{index=1}

```text
bundle SHA-256 = ea0ed57c24a3063eb4f1850249b9a8a75f7497194a9bc60c95e60f7efc373a42
zip members = 134
manifest entries verified = 133
independent exact verifier = PASS
ordered simple disjoint roots = 2101
positive-radius boxes audited = 16
winner_found = false
```

## Exact Santaló-centred family

Let

```text
q_i = Q_i/2^48,  i=0,...,4323,
Q = conv{q_i},
P_* = (Q-a_*)^polar.
```

The integer rows `Q_i` are fully expanded in `generator.json`. The unique Santaló point is isolated by

```text
a_* ∈ a_c + [-2^-90,2^-90]^3,
a_c = 2^-120 * (
 -39878490350125864373364388380978345,
  88581653811863381217051,
  819441514472273259270856
).
```

All polar denominators are strictly positive on this box. Santaló stationarity gives the exact ordinary-volume centroid of `P_*` as zero. For every invertible `A`, `A P_*` remains exactly centred.

Use trace-one inverse-metric coordinates

```text
x=(K00,K11,K01,K02,K12),
K22=1-K00-K11,
K=[[K00,K01,K02],[K01,K11,K12],[K02,K12,K22]],
K ≻ 0,
K=A^-1 A^-T.
```

The transformed finite H/V representation is deterministic:

```text
h_i^A=A^-T(q_i-a_*),
N_t=Q_j×Q_k+Q_k×Q_i+Q_i×Q_j,
delta_t=det(Q_i,Q_j,Q_k)>0,
y_0,t=2^48 N_t/delta_t,
v_t^A=A y_0,t/(1-a_*·y_0,t).
```

The complete actual lattice is

```text
(H,V,E)=(4324,8644,12966),
boundary triangles=17284,
8644-12966+4324=2.
```

Every certified connector/box lies in the trace-one SPD core

```text
lambda2/lambda1>1/32,
lambda3/lambda2>19/64,
17179/16384<cond(K)<2048/19,
lambda_min(K)>19/4115.
```

Exact Weyl/Sylvester interval bounds certify positive definiteness throughout each open set; trace one is an identity. The rank-two plaque collar has `det(K)>0.008231552348311645`, and the rank-three collar has `det(K)>0.008287581251834953`.

## Complete mechanical walls

For every directed pair of adjacent maximal faces,

```text
S_ij(K)=(q_i-a_*)^T K(q_i-q_j).
```

A maximal face is stable iff all its outgoing `S_ij` are positive. There are 25,932 directed face primitives.

For adjacent vertices `f→g`, with baseline vertices `y_f,y_g` and `d_f=1-a_*·y_f`, define

```text
W_fg(K)=d_g y_f^T adj(K)y_f-d_f y_f^T adj(K)y_g.
```

A vertex is unstable iff all outgoing `W_fg` are positive. There are 25,932 directed vertex primitives.

A true edge with incident faces `(i,j)` and endpoints `(f,g)` is a saddle iff

```text
S_ij>0, S_ji>0, W_fg>0, W_gf>0.
```

All four components of all 12,966 true-edge cones are audited; triangulation diagonals are excluded.

## Exact all-wall connector beyond `B8_alt`

Each piece is an affine metric segment `x(t)=(1-t)x_0+t x_1`. Face walls are affine and vertex walls quadratic in `t`. Every root has an exact dyadic isolating bracket, a derivative margin dominating the full Santaló box, and a bracket disjoint from every other event.

| Piece | face roots | vertex roots | total | exact endpoint classes |
|---|---:|---:|---:|---|
| `B8_to_pair_minus` | 397 | 381 | 778 | `(2,3,3), S={1378,2903}` → `(2,7,7), S={1343,2938}` |
| `pair_minus_to_post7919` | 330 | 398 | 728 | `(2,7,7), S={1343,2938}` → `(2,4,4), S={1308,2938}` |
| `post7919_to_joint7919_17700_mm` | 121 | 73 | 194 | `(2,4,4), S={1308,2938}` → `(2,4,4), S={1308,2973}` |
| `joint7919_17700_mm_to_rank3_11193_mmm` | 99 | 302 | 401 | `(2,4,4), S={1308,2973}` → `(2,4,4), S={1308,2973}` |

There are 2,101 simple disjoint roots and 2,105 open path chambers. Minimum adjacent-root gaps on the four pieces are respectively

```text
2.0179171593321303e-7,
1.2995099676420216e-6,
2.3547875670213793e-8,
7.961929030909463e-7.
```

No connector chamber has `(1,1,0)`. The fourth piece contains fifteen one-dimensional `(2,2,2)` chambers, but no full-dimensional winner.

Exact key metric centres, in coordinate order `(K00,K11,K01,K02,K12)`, are:

```text
B8_alt=(
4568965091790763/18014398509481984,
836692543844195/4503599627370496,
802367913848253/9007199254740992,
-1328939388696825/4503599627370496,
-2337042999103599/36028797018963968)

post7919=(
4895883847143125/18014398509481984,
6893981048592413/36028797018963968,
1491458061409209/18014398509481984,
-5503541905433287/18014398509481984,
-1805795383728931/36028797018963968)

rank2-mm=(
361748209225068833699937879881121129/1329227995784915872903807060280344576,
252845294672865416888594918820350217/1329227995784915872903807060280344576,
105389594742455425809690677990368619/1329227995784915872903807060280344576,
-203695331119034374759334207499792953/664613997892457936451903530140172288,
-60442460602687179658846980118334101/1329227995784915872903807060280344576)

rank3-mmm=(
11278613093941581675137347121305889/41538374868278621028243970633760768,
254798268272983571084026719990540413/1329227995784915872903807060280344576,
50996316635262688249156836805009031/664613997892457936451903530140172288,
-408584038730915079551754535168983171/1329227995784915872903807060280344576,
-62705473451446037216424128989600233/1329227995784915872903807060280344576).
```

The stable-component ordering is decisive: row 1308 is born at wall 7918 seventy-four ordered events before row 1343 dies at wall 7919; row 2973 is born at wall 17701 one hundred ninety ordered events before row 2938 dies at wall 17700. Thus the two intended deaths are pre-empted by replacement births.

## Rank-two plaque and rank-three extension

The genuine coupled plaque is

```text
wall 7919: 1343→1308, true edge 3959,
wall 17700: 2938→2973, true edge 8850.
```

Its exact coefficient Gram determinant is positive. A coordinatewise `2^-31` collar proves that only these two walls can vanish; every other one of the 51,862 directed walls remains strict, all 289 inherited-cell exclusions remain strict, and the compact-core margin stays positive.

| signs `(7919,17700)` | class | exhaustive stable rows |
|---|---|---|
| `--` | `(2,4,4)` | `{1308,2973}` |
| `-+` | `(3,4,5)` | `{1308,2938,2973}` |
| `+-` | `(3,4,5)` | `{1308,1343,2973}` |
| `++` | `(4,4,6)` | `{1308,1343,2938,2973}` |

The reverse-wall identity

```text
S_ij+S_ji=(q_i-q_j)^T K(q_i-q_j)>0
```

forces the replacement-row transfer.

The first genuine rank-three plaque adds wall 11193, `1878→1843` at edge 5596. A coordinatewise `2^-34` collar proves that only these three walls can vanish. Its eight orthants are:

```text
--- (2,4,4) S={1308,2973}
--+ (3,4,5) S={1308,1878,2973}
-+- (3,4,5) S={1308,2938,2973}
-++ (4,4,6) S={1308,1878,2938,2973}
+-- (3,4,5) S={1308,1343,2973}
+-+ (4,4,6) S={1308,1343,1878,2973}
++- (4,4,6) S={1308,1343,2938,2973}
+++ (5,4,7) S={1308,1343,1878,2938,2973}.
```

The third wall is adverse: its positive side births stable row 1878. Hence neither the rank-two nor rank-three local arrangement contains a winner. The exact plaque data and interval proof are in the recovered handoff. :contentReference[oaicite:2]{index=2}

## Exhaustive positive-radius box ledger

Every unlisted feature is strictly excluded on the whole box; the archive contains all individual wall intervals and every edge's four-component cone.

| box | radius | class | stable rows | unstable vertices | saddle edges |
|---|---:|---|---|---|---|
| `pair_minus` | `2^-104` | `(2,7,7)` | 1343,2938 | 931,2514,3704,4340,4812,6221,7335 | 2336,2440,5702,7333,7438,10487,10589 |
| `pre7919` | `2^-50` | `(3,4,5)` | 1308,1343,2938 | 1759,4341,6223,8010 | 2441,3959,5807,7228,7333 |
| `post7919` | `2^-50` | `(2,4,4)` | 1308,2938 | 1759,4341,6223,8010 | 2441,5807,7228,7333 |
| `post7919_endpoint` | `2^-60` | `(2,4,4)` | 1308,2938 | 1759,4341,6223,8010 | 2441,5807,7228,7333 |
| rank2 `--` | `2^-100` | `(2,4,4)` | 1308,2973 | 3706,4341,6223,8010 | 2441,5807,7228,7333 |
| rank2 `-+` | `2^-100` | `(3,4,5)` | 1308,2938,2973 | 3706,4341,6223,8010 | 2441,5807,7228,7333,8850 |
| rank2 `+-` | `2^-100` | `(3,4,5)` | 1308,1343,2973 | 3706,4341,6223,8010 | 2441,3959,5807,7228,7333 |
| rank2 `++` | `2^-100` | `(4,4,6)` | 1308,1343,2938,2973 | 3706,4341,6223,8010 | 2441,3959,5807,7228,7333,8850 |
| rank3 `---` | `2^-100` | `(2,4,4)` | 1308,2973 | 402,4341,7695,8010 | 5912,6017,7018,7123 |
| rank3 `--+` | `2^-100` | `(3,4,5)` | 1308,1878,2973 | 402,4341,7695,8010 | 5596,5912,6017,7018,7123 |
| rank3 `-+-` | `2^-100` | `(3,4,5)` | 1308,2938,2973 | 402,4341,7695,8010 | 5912,6017,7018,7123,8850 |
| rank3 `-++` | `2^-100` | `(4,4,6)` | 1308,1878,2938,2973 | 402,4341,7695,8010 | 5596,5912,6017,7018,7123,8850 |
| rank3 `+--` | `2^-100` | `(3,4,5)` | 1308,1343,2973 | 402,4341,7695,8010 | 3959,5912,6017,7018,7123 |
| rank3 `+-+` | `2^-100` | `(4,4,6)` | 1308,1343,1878,2973 | 402,4341,7695,8010 | 3959,5596,5912,6017,7018,7123 |
| rank3 `++-` | `2^-100` | `(4,4,6)` | 1308,1343,2938,2973 | 402,4341,7695,8010 | 3959,5912,6017,7018,7123,8850 |
| rank3 `+++` | `2^-100` | `(5,4,7)` | 1308,1343,1878,2938,2973 | 402,4341,7695,8010 | 3959,5596,5912,6017,7018,7123,8850 |

The smallest certified absolute directed-face clearance is `1.13686838e-13`; the smallest directed-vertex clearance is `4.62667119e-10`. These are interval lower bounds on positive-radius boxes, not point samples.

## Inherited-cell exclusion and verifier

All four connector segments remain outside every one of the 289 inherited relative-condition cells. The exact minimum separation lower bounds are

```text
8743377003624220416796107762987521405/576460752303423488
5211803670445244432683632648777906714779789274422892173/332306998946228968225951765070086144
153355950397630254295960747045362426337/9223372036854775808
5683438210257271341818531686427809504257764044079351342469/340282366920938463463374607431768211456.
```

The independent verifier reconstructs all 8,644 vertices from active triples, validates all H/V/E incidence, recomputes every path polynomial and Santaló perturbation bound, checks every root bracket and chamber replay, recomputes all sixteen box ledgers and both plaque collars, checks all edge cones and 289 nonmembership inequalities, verifies plaque ranks and energy identities, and checks the compact-core covers. It ends in `PASS`. :contentReference[oaicite:3]{index=3}

Artifacts:

- [Complete exact bundle](sandbox:/mnt/data/Calm_Quartz_90_fixed_lattice_NONWINNER.zip)
- [Fresh wrapper verifier](sandbox:/mnt/data/Calm_Quartz_90_verifier.py)
- [Fresh verification receipt](sandbox:/mnt/data/Calm_Quartz_90_fresh_verification.json)
- [Full expanded handoff](sandbox:/mnt/data/Calm_Quartz_90_full_handoff.md)
- [Structured result file](sandbox:/mnt/data/Calm_Quartz_90_result.json)

No winner mesh is emitted. The bundle supplies the complete fixed H/V representation, all maximal-face cycles, all true edges, deterministic transforms, box ledgers, verifier, and watertight endpoint meshes used for the nonwinner atlas.

## Next unresolved joint transition

The surviving replacement stable rows have nonreverse outgoing death candidates

```text
row 1308: 7705,7709,7911,7916,7920
row 2973: 17697,17901,17906,17908,17910.
```

Reverse walls 7918 and 17701 are excluded by the positive SPD energy identity. The next exact frontier is therefore the 25 rank-four arrangements

```text
[7919,17700,bA,bB].
```

A discovery-only double-precision sweep over these 25 systems enumerated 711,630 non-target root groups and found no numerical `(1,1,0)` interval; nineteen systems reached no better than `(2,2,2)`, one no better than `(4,2,4)`, and five had no numerical SPD interval. This is not an exact exclusion. The rigorous continuation is an adaptive exact per-cell all-wall atlas with direct inherited-cell membership/separation and full face/vertex/edge interval ledgers. A successful child must make rows 1308 and 2973 nonstable before any other stable birth and then expand to a positive-radius trace-one SPD box. The recovered handoff identifies this boundary explicitly. :contentReference[oaicite:4]{index=4}

## Final statement

**NONWINNER, rigorously delimited.** No homogeneous polyhedral Gömböc exists in the certified connector/rank-two/rank-three atlas beyond `B8_alt`. The broader fixed-lattice trace-one SPD family remains unresolved only beyond the stated rank-four frontier; no global impossibility claim is made.
