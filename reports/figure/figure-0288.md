# figure-0288

AI research report · 2026-09-04 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Keen Quartz 73 — exact FAN17 cross-family determination

## Determination

**EXACT NONWINNER; genuinely new exact intervening incidence layer.** No homogeneous convex polyhedral Gömböc was obtained. I constructed one robust exact own-centred polyhedron of strict class `(S,U,H)=(1,2,1)`, exhaustively constructed all 17 one-root coherent triangulation chambers adjacent to literal parent B, and proved that every one of those chambers transfers the residual `U-H` packet rather than annihilating it.

A formal injective common 50-row support family was also constructed. A fully authenticated numerical A-to-B path cannot honestly be claimed because the recovered parent-A archive omits the exact affine matrix that its immutable payload says defines its promoted `(2,1,1)` endpoint. That conflict is preserved rather than repaired by invented coordinates.

## 1. Immutable parents remain literal and distinct

**Parent A:** assignment `figure-0275`; SHA-256 `0f7bb810ecc8015121db8968b288d5d4087780b1e029e9a8c48babcfc5d412d2`; exact own-centred simplicial `(V,E,F)=(8,18,12)`; strict `(S,U,H)=(2,1,1)`; stable faces `[0,H,C]` and `[C,AG,AD]`; unique unstable vertex `C`; sole saddle `[C,AD]`.

With `D=2^24`, its literal uncentred source rows are

```text
0  = ( 2382238,  -6308946,  46171779)/D
C  = (-19656014, -12570508, -84150451)/D
H  = ( -1678613,  11935619, -25478204)/D
Z  = (  8010895, -10409701,  39298476)/D
AB = (  1683954,  13081292, -39025397)/D
AD = (  2466433, -19765281,  18154812)/D
AE = (  5834590,  17237355, -20273721)/D
AG = (  7455840,   3175317, -13504557)/D.
```

Its maximal faces are

```text
[0,H,C] [0,C,AD] [0,AE,H] [0,AD,Z] [0,Z,AE] [C,H,AB]
[C,AB,AG] [C,AG,AD] [H,AE,AB] [Z,AD,AG] [Z,AG,AE] [AB,AE,AG].
```

**Parent B:** assignment `figure-0266`; SHA-256 `49545ef8d787bb7886f19249253131f72ee0f35f1bb499c3bce73e75cbf23fd1`; exact own-centred 38-supplied/18-active support body; primal `(V,E,F)=(18,34,18)`; strict `(1,2,1)`; sole stable `[2475]`; protected unstable `[2475,5000,5003]`; residual unstable polygon `[14000,14001,14002,14003,14004,14005,14006,14007,2475,5000,14008,14009,14010,14011,14012,14013,14014]`; sole saddle `(14001,14014)`.

No label identification, renaming, or coordinate conflation between these bodies is used.

## 2. Injective common support architecture

Use 50 common IDs. IDs `0..11` are

```text
A:F00[0,H,C] A:F01[0,C,AD] A:F02[0,AE,H] A:F03[0,AD,Z]
A:F04[0,Z,AE] A:F05[C,H,AB] A:F06[C,AB,AG] A:F07[C,AG,AD]
A:F08[H,AE,AB] A:F09[Z,AD,AG] A:F10[Z,AG,AE] A:F11[AB,AE,AG].
```

IDs `12..49` are namespace-`B` labels, in this injective order:

```text
14000,14001,14002,14003,14004,14005,14006,14007,2475,5000,
14008,14009,14010,14011,14012,14013,14014,5003,
12000,12001,12002,12003,12004,0,7001,7002,7003,8000,8001,8002,
9000,9001,9002,10000,10001,11000,11001,11002.
```

Define

```text
K(alpha,beta)={x:
  (alpha_f q^A_f)·x <= 1, f=0..11,
  (beta_j q^B_j)·x <= 1, j=0..37}.
```

All 50 controls vary independently in `[0,1]`. A connected bounded schedule is

```text
0 <= s <= 1/2: alpha_f=1, beta_j=2s;
1/2 <= s <= 1: alpha_f=2-2s, beta_j=1.
```

The A block preserves boundedness on the first half and the B block on the second. At either endpoint every opposite-family row is exactly zero, so its inequality has exact slack `1`. For any bounded member with exact ordinary centroid `c`, polarity-aware own-centering is

```text
q -> q/(1-q·c),     p -> p-c,
```

with zero rows unchanged.

For A, `q_f^A=q_f^0 A_*^{-1}`, where `q_f^0·(r_i-c_A)=1` on the listed source face and `p_i=A_*(r_i-c_A)`. The immutable payload says `A_*` is stored in `affine_map_exact.csv` and `frozen_source.json`. The recovered A archive has SHA-256 `02f56ecb307fcb3f7bbbfa7fcd8354fae75438bdd0681d2723fef94d1d4b1cc2`, contains neither file, and its archived builder ends with `AssertionError: dedicated strict C-pattern affine search did not materialize`. Therefore this is an exact formal common architecture, but no numerical A endpoint or complete A-to-B incidence chronology is claimed.

## 3. Promoted exact body

The promoted body is `J55_ROOT8_full_polygon_fan`. Let `N=2^24`. In local order

```text
[14000,14001,14002,14003,14004,14005,14006,14007,
 2475,5000,14008,14009,14010,14011,14012,14013,14014,5003]
```

take the following uncentred exact active support rows:

```text
 0 14000 = (11653197/16777216, -13937873/16777216, -1/140)
 1 14001 = (2881939/8388608, -16027135/16777216, -1/140)
 2 14002 = (16793753/16777216, -4845199/8388608, -1/140)
 3 14003 = (20394447/16777216, -1777173/8388608, -1/140)
 4 14004 = (21762407/16777216, 3910885/16777216, -1/140)
 5 14005 = (10204443/8388608, 1486601/2097152, -1/140)
 6 14006 = (2017591/2097152, 19400855/16777216, -1/140)
 7 14007 = (285131/524288, 25373787/16777216, -1/140)
 8 2475  = (-22537/4194304, 14404513/8388608, -547/71680)
 9 5000  = (-9304549/16777216, 25373787/16777216, -1/140)
10 14008 = (-2040149/2097152, 19400855/16777216, -1/140)
11 14009 = (-20589485/16777216, 1486601/2097152, -1/140)
12 14010 = (-21943151/16777216, 3910885/16777216, -1/140)
13 14011 = (-5143831/4194304, -1777173/8388608, -1/140)
14 14012 = (-16974741/16777216, -4845199/8388608, -1/140)
15 14013 = (-5917131/8388608, -13937873/16777216, -1/140)
16 14014 = (-1486245/4194304, -16027135/16777216, -1/140)
17 5003  = (33885/2097152, -7804601/8388608, 5625/262144).
```

This is literal parent B with raw support `2475` moved by `-(0,0,2^-11)`. The cyclic base order is

```text
[1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16].
```

Cone all 17 consecutive base edges to apex `17`, and triangulate the lower 17-gon by the full star rooted at local row `8`. Solve `q_i·p=1` on every dual triangular face. Compute ordinary volume and moments by the oriented tetrahedral boundary sum, set `c=M/V`, and apply the exact projective centering above. No decimal is an input.

The exact volume is

```text
225173994243014234371516712962284491912004431596348604654114764643143117724165066773603009262817514139869403593987963007077065838232065351827919048969945795258102628829129550338791531852992438271093867645784665001458083417149342652136518978089434933138937061372699936463234949921913993722708527759013861073984558004792402604079117822433787533698316814618661714993580472459778222230403102617414584848533279733625877205955708527038774910623098102390222998366641835126159021387995152810895073145592058717514610096137838017960000406163554304
/
1117469202079418326647140601834803477079210887020685083962865306276022622881229790712893035979302422519213175988300296071059623351573560600952107805505437959251359930568681360704511416213099450737805105516857662243311913044637269714459994488582757372285041856185071734765212549461389860295545230786450529619748274495631692651208133309849977514388464463067816726067231955131923887964819617597029102113920175974102405700558115669078132530697916933263804451872082330647026946606971439825218990374179200753510132391825528537231110050961365
```

or approximately `201.5035347945197`. The final ordinary centroid is exactly `(0,0,0)` and all three ordinary first moments are exactly zero. The raw centroid is computed from the displayed source and is approximately `(2.9176743938622543e-6,0.001724588742879939,0.34662886605260385)`. The minimum projective denominator is approximately `0.9941666287989871` and is exactly positive.

## 4. Full active H/V/E lattice

The 32 maximal dual faces, equivalently primal vertices, are

```text
(14000,14001,2475) (14000,14001,5003)
(14000,14002,2475) (14000,14002,5003)
(14001,2475,14014) (14001,14014,5003)
(14002,14003,2475) (14002,14003,5003)
(14003,14004,2475) (14003,14004,5003)
(14004,14005,2475) (14004,14005,5003)
(14005,14006,2475) (14005,14006,5003)
(14006,14007,2475) (14006,14007,5003)
(14007,2475,5003)
(2475,5000,14008) (2475,5000,5003)
(2475,14008,14009) (2475,14009,14010) (2475,14010,14011)
(2475,14011,14012) (2475,14012,14013) (2475,14013,14014)
(5000,14008,5003)
(14008,14009,5003) (14009,14010,5003) (14010,14011,5003)
(14011,14012,5003) (14012,14013,5003) (14013,14014,5003).
```

All 48 true dual edges are

```text
(14000,14001) (14000,14002) (14000,2475) (14000,5003)
(14001,2475) (14001,14014) (14001,5003)
(14002,14003) (14002,2475) (14002,5003)
(14003,14004) (14003,2475) (14003,5003)
(14004,14005) (14004,2475) (14004,5003)
(14005,14006) (14005,2475) (14005,5003)
(14006,14007) (14006,2475) (14006,5003)
(14007,2475) (14007,5003)
(2475,5000) (2475,14008) (2475,14009) (2475,14010)
(2475,14011) (2475,14012) (2475,14013) (2475,14014) (2475,5003)
(5000,14008) (5000,5003)
(14008,14009) (14008,5003)
(14009,14010) (14009,5003)
(14010,14011) (14010,5003)
(14011,14012) (14011,5003)
(14012,14013) (14012,5003)
(14013,14014) (14013,5003)
(14014,5003).
```

The 18 maximal primal face cycles, using primal-vertex indices `0..31` in the face order above, are

```text
14000: 2,3,1,0
14001: 0,1,5,4
14002: 6,7,3,2
14003: 8,9,7,6
14004: 10,11,9,8
14005: 12,13,11,10
14006: 14,15,13,12
14007: 16,15,14
2475: 4,24,23,22,21,20,19,17,18,16,14,12,10,8,6,2,0
5000: 25,18,17
14008: 17,19,26,25
14009: 19,20,27,26
14010: 20,21,28,27
14011: 21,22,29,28
14012: 22,23,30,29
14013: 23,24,31,30
14014: 4,5,31,24
5003: 1,3,7,9,11,13,15,16,18,25,26,27,28,29,30,31,5.
```

Thus dual `(V,E,F)=(18,48,32)`, primal `(32,48,18)`, and both Euler checks equal `2`. Every active row owns a maximal primal face and is irredundant. The minimum active nonincidence gap is exactly positive, approximately `0.0030972963590750278`, attained by row `14013` at vertex `[14001,2475,14014]`.

The full candidate supplied ledger has 50 rows: 12 zero A rows with exact gap `1`; the 18 displayed B rows active; and all 20 transformed literal-B inactive rows nonzero and strictly inactive. Their minimum gap is exactly positive, approximately `0.9999999999727996`, attained by literal row `12003` at the same primal vertex.

## 5. Exhaustive equilibrium classification

For a support row `i`, evaluate every incident primitive

```text
sigma(i->j)=||q_i||²-q_j·q_i.
```

It is stable iff every such value is positive. For a dual triangular face `F` with primal vertex `p`, solve

```text
sum_{r in F} lambda_r q_r=p/||p||²;
```

and classify it unstable iff all `lambda_r>0`. For every true edge `(i,j)` incident to primal vertices `u,v`, solve

```text
q_i+t(q_j-q_i)=alpha p_u+beta p_v
```

and classify it as a saddle iff `(t,1-t,alpha,beta)` is componentwise positive.

All 18 row cones, all 32 full incident-vertex cones, and all 48 four-component true-edge cones were evaluated exactly. The complete classification is

```text
stable:   [2475]
unstable: [14001,2475,14014], [2475,5000,5003]
saddles:  [14001,14014]
class:    (1,2,1).
```

Strict rational signs have the following decimal summaries:

```text
stable   positive +0.11840225070807478; excluded upper -0.0018024065397749104
unstable positive +0.015718039773023523; excluded upper -0.015681363070716072
saddle   positive +0.003809076348641434; excluded upper -0.01338471210612803.
```

## 6. Full external-arrow and anti-carrier audit

All 96 directed row-star arcs and every external-neighbour primitive of all 48 edges were checked exactly. The sole row-star sink is `2475`. The only all-external-positive edges are

```text
(14007,2475), (2475,5000),
```

both incident to the protected sink. The 14 inserted star diagonals are

```text
(14000,2475) (14001,2475) (14002,2475) (14003,2475)
(14004,2475) (14005,2475) (14006,2475)
(2475,14008) (2475,14009) (2475,14010) (2475,14011)
(2475,14012) (2475,14013) (2475,14014).
```

None is an all-external-positive carrier.

For closure edge `(1,16)=(14001,14014)`, let `a=q_1`, `b=q_16`, `d=b-a`, `t=-(a·d)/(d·d)`, and `x=a+td`. The denominator-free event function is

```text
G_r=(d·d)²(x·q_r-||x||²).
```

Exact arithmetic gives `G_7<0` and `G_8<0`; the corresponding values before denominator clearing are approximately `-2.3441425200601103` and `-2.5392602312653794`. Thus both nearby root choices lie strictly on the noncancelling side of the fixed-closure event wall.

## 7. Exact FAN17 atlas

At common lift `delta=2^-11`, every possible one-root coherent full-star triangulation of the old 17-gon was freshly reconstructed and exactly classified. All 17 cells have dual `(18,48,32)` and strict `(1,2,1)`, preserve sole stable `2475`, protected unstable `[2475,5000,5003]`, and saddle `(14001,14014)`. Their transferred residual unstable triangles are

```text
root 14001 -> [14001,2475,5000]
root 14000 -> [14000,5000,14008]
root 14002 -> [14002,14009,14010]
root 14003 -> [14003,14010,14011]
root 14004 -> [14004,14011,14012]
root 14005 -> [14005,14012,14013]
root 14006 -> [14006,14013,14014]
root 14007 -> [14001,14007,14014]
root 2475  -> [14001,2475,14014]
root 5000  -> [14000,14001,5000]
root 14008 -> [14000,14002,14008]
root 14009 -> [14000,14002,14009]
root 14010 -> [14002,14003,14010]
root 14011 -> [14003,14004,14011]
root 14012 -> [14004,14005,14012]
root 14013 -> [14005,14006,14013]
root 14014 -> [14006,14007,14014].
```

Across the atlas, the weakest exact positive margins remain positive: nonincidence approximately `0.00309729635907503`, stable `0.117886276964443`, unstable `0.000624742379618`, and saddle `0.003809076348641434`. Every selected exclusion upper bound remains negative.

## 8. Connected incidence chronology

The root-`2475` path is

```text
q_8(delta)=q_8(0)-(0,0,delta),
```

with all other raw B rows fixed and exact own-centering recomputed at each `delta`. Fresh exact checkpoints give

```text
delta=0:      dual (18,34,18), one 17-gon, class (1,2,1);
              residual U is the full 17-gon, H=(14001,14014).
delta=2^-24: dual (18,48,32), class (1,2,1).
delta=2^-12: dual (18,48,32), class (1,2,1).
delta=2^-11: dual (18,48,32), class (1,2,1).
delta=2^-10: dual (18,48,32), class (1,2,1);
              residual U=[14001,2475,14014], same H.
delta=2^-9:  dual (18,48,32), class (3,2,3);
              residual U survives while additional S/H features exist.
delta=2^-8:  dual (18,48,32), class (4,2,4).
```

Therefore the wall at `delta=0` is an exact transfer, not annihilation: the nonsimplicial unstable polygon becomes an unstable triangle while the closure saddle survives. The displayed ray is not a death-before-birth bridge.

## 9. Positive perturbation chamber

For every `x` with

```text
|x-1| <= 2^-24,
```

apply

```text
P(x)=diag(x,1,1)P,
Q(x)=Q diag(1/x,1,1).
```

All `q·p` incidences and inactive gaps are invariant, the ordinary centroid remains exactly zero by linear covariance, and volume is `xV>0`. Exact interval-polynomial certificates preserve every row-arrow, vertex-cone, and four-component edge-cone sign, so the entire chamber is strict `(1,2,1)`. Conservative unnormalised clearances are approximately `0.0910004757554522` for required positive arrows and `0.00184243684633021` for required negative exclusions.

## 10. Surviving obstruction and first unrepresented cell

This closes the complete one-root coherent-fan layer, not every triangulation or support motion. Every triangulation confined to the old planar 17-gon retains boundary edge `(1,16)=(14001,14014)` as a true edge. The first unrepresented adjacent combinatorial cell is the closure-sector nonstar flip on circuit `[1,16,0,8]`:

```text
delete diagonal (1,8) and triangles (1,8,16),(0,1,8);
insert diagonal (0,16) and triangles (0,1,16),(0,8,16).
```

A planar flip still leaves closure edge `(1,16)`. The first mechanically credible continuation is therefore a **closure-turnover double circuit** combining a closure-adjacent nonstar flip with genuine three-dimensional deactivation or turnover of support `14001` or `14014`, so `(14001,14014)` is absent before a substitute unstable triangle or saddle becomes strict. It must preserve stable `2475` and protected unstable `[2475,5000,5003]`, introduce no new sink or row-disjoint carrier, and retain at least two controls after the three exact moment equations. This is distinct from the separately assigned eight-vertex QCAD gate and J55 zipper.

Empirical cap, random-height, affine-metric, 6/9/15-dimensional closure-sector, and partial two-root searches found no robust `(1,1,0)` point. Those nonhits are not exact exclusions.

## 11. Independent replay and immutable artifacts

The clean-room verifier begins from the rational generator, freshly enumerates the hull, rebuilds all primal vertices and cycles, recomputes exact volume and zero moments, verifies all 50 supplied rows, all normal cones and arrows, all 17 fan cells, all chronology checkpoints, the perturbation chamber, and mesh topology. A pristine archive extraction passed.

Terminal markers include

```text
KQ73_IMMUTABLE_MANIFEST_PASS
KQ73_DETERMINISTIC_REBUILD_PASS
KQ73_FRESH_EXACT_HULL_PASS
KQ73_EXACT_VOLUME_CENTROID_PASS
KQ73_FULL_NORMAL_CONES_1_2_1_PASS
KQ73_EXTERNAL_ARROW_ANTI_CARRIER_PASS
KQ73_COMMON_50_ROW_FULL_SUPPLIED_PASS
KQ73_EXACT_FAN17_TRANSFER_ATLAS_PASS
KQ73_CONNECTED_INCIDENCE_CHRONOLOGY_PASS
KQ73_PARENT_A_ARTIFACT_CONFLICT_AUDIT_PASS
KQ73_FAN17_ALL_INDEPENDENT_CHECKS_PASS
KQ73_CLEAN_EXTRACTION_ALL_PASS.
```

The triangulated mesh has 32 vertices, 60 coherently oriented triangles, 90 mesh edges each with multiplicity two, and Euler `32-90+60=2`. The maximal-face OBJ contains the 18 true primal polygons.

Artifacts:

- [Complete exact replay archive](sandbox:/mnt/data/Keen_Quartz_73_cross_family_FAN17_exact_NONWINNER.zip), SHA-256 `31aa1dfdab125daa85cc343486cc21de4a22ad1c6b211e8601446c5a7ba47bcc`.
- [Archive SHA-256](sandbox:/mnt/data/Keen_Quartz_73_cross_family_FAN17_exact_NONWINNER.zip.sha256).
- [Standalone handoff](sandbox:/mnt/data/Keen_Quartz_73_cross_family_FAN17_exact_NONWINNER/RESEARCH_HANDOFF.md).
- [Exact active source and complete mechanics](sandbox:/mnt/data/Keen_Quartz_73_cross_family_FAN17_exact_NONWINNER/source/root8_exact_source.json).
- [Common 50-row ledger](sandbox:/mnt/data/Keen_Quartz_73_cross_family_FAN17_exact_NONWINNER/source/common_family_ledger.json).
- [Exact FAN17 atlas](sandbox:/mnt/data/Keen_Quartz_73_cross_family_FAN17_exact_NONWINNER/certificates/fan17_exact_atlas.json).
- [Exact chronology](sandbox:/mnt/data/Keen_Quartz_73_cross_family_FAN17_exact_NONWINNER/certificates/root8_incidence_chronology.json).
- [Independent verifier](sandbox:/mnt/data/Keen_Quartz_73_cross_family_FAN17_exact_NONWINNER/verifier/verify_cleanroom.py).
- [Deterministic rebuild](sandbox:/mnt/data/Keen_Quartz_73_cross_family_FAN17_exact_NONWINNER/construction/rebuild_from_source.py).
- [Maximal-face OBJ](sandbox:/mnt/data/Keen_Quartz_73_cross_family_FAN17_exact_NONWINNER/body/root8_maximal_faces.obj), [triangulated OBJ](sandbox:/mnt/data/Keen_Quartz_73_cross_family_FAN17_exact_NONWINNER/body/root8_triangulated.obj), and [STL](sandbox:/mnt/data/Keen_Quartz_73_cross_family_FAN17_exact_NONWINNER/body/root8.stl).

## Bottom line

No exact `(1,1,0)` body and no certified numerical A-to-B path were reached. The substantive new result is that all 17 coherent one-root resolution chambers of parent B’s residual 17-gon are now exactly constructed and independently proved strict `(1,2,1)`. Every chamber preserves the protected pair but transfers the unwanted unstable equilibrium and closure saddle. The next justified cell is a nonstar, genuinely three-dimensional closure turnover removing `14001` or `14014`; another one-root fan, fixed-incidence affine interpolation, QCAD repetition, or J55 zipper repetition is unsupported.
