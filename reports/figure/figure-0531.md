# figure-0531

AI research report · 2026-09-24 UTC

---

# W49 — finite reconstruction of the R3 landscape

## Outcome

**No own110 body is claimed.** This work produced 24 new rational endpoint controls, a general exact maximal-facet H auditor, three exact structural results about the original R3 basin, and an executed change from the original U1 architecture to physical **S1/U2 bodies**.

The last retained continuation inputs are `R3_H44_GROWN_S1_G6` and `G8`: **V84/E126/F44, C252, own121, additionalweak000, primitivezero000, P1/Q0**. Their remaining P bar has 54 vertices, 22 cut edges, and normalized depths **0.7379371658078545 / 0.7379370989585050**. These do not dominate R3: the residual bar is deeper than R3's Q bar. Their value is the genuine change to S1, substantially changed geometry and root carriers, and **123 edges of actual headroom**.

A separate compact endpoint, `R3_HBRIDGE_S1_G3`, is **V44/E66/F24, C132, own121**. Every numerator and denominator of its actual vertex coordinates fits in 32 bits. Its centroid denominators do not: the largest has 2121 bits. This is an arithmetic/control alternative, not a minimum or record claim.

All 26 entries of the exact receipt ledger—24 new endpoints, original R3, and a cube control—were regenerated from the recovered source package. Observed aggregate marker:

```text
W49_EXACT_HANDOFF_PASS 26 64 58
```

The 64/58 totals count all positive P/Q bar records across those inputs, including different grids and controls; they are not counts of distinct defects across lineages. A separate H-versus-V crosscheck also audits the supplied JB control.

## Input authority

The entire four-file input pack was available and read through EOF. R3 was recovered without old R2/SQP trajectories. Its rerun receipt matches the supplied exact identity: input2177 bytes, SHA256 `43d6adb06bc3a027dac4257de57455692b3fb964e1ef4e872c6e16d32d965a2b`; audit6631 bytes, SHA256 `4ebb493fd0d11a0a2d4d166841586969e24d78c34f5a1cb1feaad0a0e9cbc3d5`. It is V58/E168/F112, own211, P0/Q1, S52/105, U57, H38–57 and Q33/cut21. These are sorted exact labels, not input-row or R2 labels. :contentReference[oaicite:0]{index=0}

The supplied `exact_poly.py` has SHA256 `898f77989193886996d6f2dc121ccdfdf611b8a9ac52fd3207557eac6a69c0c4`; it explicitly rejects nontriangular maximal facets. Consequently it could not certify the new H bodies unchanged. The supplied numerical core provided actual-volume centroid and live radial-forest conventions. :contentReference[oaicite:1]{index=1} :contentReference[oaicite:2]{index=2}

No missing historical dependency is needed for the constructions below. The mounted journal wrapper had170978 bytes, SHA256 `b9432b21a2ed16838b8316355905c16992605126ad79b856a33e307559fd3b39`; that is the wrapper-file hash, not its internal memory hash.

## 1. Exact finite access results for original Q33

### The fixed visibility-cover number is exactly two

Let T be the original Q component and C its79-facet complement. Exact visibility means `n_i·p>h_i`; complementary nonvisibility means `n_j·p<=h_j`.

One point cannot see all T while seeing none of C. An exact five-plane dependence uses packet facets **11,89** and complementary facets **10,82,86**. For their primitive raw rows `(n,h)`, alternating4×4 cofactors, divided by their gcd and oriented positively, have signs `(+,+,-,-,-)` and satisfy `sum z_j(n_j,h_j)=0`. Applied to `(p,-1)`, this contradicts the required visibility inequalities. The complete coefficients are reconstructed and checked by `finite_certificate.py`; no floating LP flag is used as proof.

Two rational pairs attain the upper bound:

```text
Small:
A=(112281,-78374,200000)/100000
B=(200000,-15419,9762)/100000

Acute:
A=(331339,-45201,500000)/100000
B=(500000,70174,169665)/100000
```

Each pair strictly avoids all79 complementary facets and jointly sees exactly all33 packet facets. Their actual homogeneous hulls are:

| Pair | Actual V/E/F | Strict S/U/H | P/Q bars |
|---|---:|---:|---:|
| Small |53/153/102|16/9/23|8/15|
| Acute |53/153/102|4/5/7|4/3|

Both are additionalweak000/primitivezero000. Each removes old vertices `[40,43,49,51,52,54,55]`, retains precisely79 old facets, and replaces33 by23 new facets. Old elder facet52 survives as new facet50 but is **not stable at the new actual centroid**. Thus complete packet access does not preserve even the presumed elder mechanism.

In the acute body the new tips are canonical51/52 and both are U. Original U57 survives geometrically as canonical50 but ceases to be U: actual mechanical root change, not a labeling artifact.

### Retained-normal height changes alone cannot close the deleted basin

Every complementary primitive outward normal satisfies `n_i·(4,1,5)<0`; the largest raw dot is exactly `-169787429110491188`. Therefore **every nonempty intersection using only these79 normal directions is unbounded, for every finite assignment of heights**. From any feasible point, the ray in direction `(4,1,5)` remains feasible.

This closes the retained-normal height-only direction, not changed normals or additional supports. An early diagnostic hull of finite intersections from this unbounded system was rejected: that finite hull was not the intended H-body and is not an endpoint.

### An acute-tip inner-material family has two persistent U

Let W be the acute-pair hull. At each tip a, take the59 vectors to the other supplied points. The certificate checks all **6962 ordered direction pairs** and proves

`u·v-(1/128)||u||_1||v||_1>0`.

The minimum distinct-direction ratio is exactly `25686418633979/2629691372957828`; the minimum metric residual in physical coordinates is `493627659143613/8000000000000000`.

For every SPD G with entrywise `|G-I|<=1/128`, all these `u^T G v` are positive. Consequently, every full-dimensional convex `L⊂W` retaining both tips has both tips strict U at **every interior reference centre**, hence at its own homogeneous centroid. Indeed `c-a` and `y-a` are nonzero nonnegative combinations of those directions, giving `(a-c)^T G(y-a)<0`. The equivalent affine statement uses `G=A^T A`.

Scope is this particular W, both retained tips, and this metric box—not all two-point covers, other tip positions, bodies outside W, or all metrics.

Observed:

```text
R3_FULL_Q33_MINIMUM_VISIBILITY_COVER_EXACTLY_TWO_PASS
R3_RETAINED79_NORMALS_ALL_HEIGHTS_UNBOUNDED_PASS (4, 1, 5)
R3_ACUTE_TWO_ROOT_ALL_INNER_MATERIAL_GRAM_PASS 1/128 6962
```

`FINITE_CERTIFICATE.json`:2557 bytes, SHA256 `4c45941adf85a52124651e0c8f863028050cd8b86408f8029cdb276adb1de8a6`.

## 2. Constructive physical H-side change

The representation was `K(q)={x:q_i·x<=1}`. Initially the centred R3 polar points represent the same translated physical body. Subsequent q motion changes its supporting planes. **Every integrated and audited body was K(q), not a separately uniformly filled polar hull.** Its filled-volume centroid and both centred landscapes were rebuilt at every numerical evaluation.

The productive route replaced all33 packet directions, initially kept79 complementary directions, added a replacement direction, and freely moved supports. Root-free optimization yielded an exact29-support own211 body. An11-point normal bridge along a12-link spherical/log-radius route, followed by further actual-mass support changes, yielded exact H24 own121. H-side nonlinear feasibility retraction then produced H27; whole-P22 truncation and further support changes produced H44.

| Exact endpoint | V/E/F | Own class | P/Q | Single remaining bar |
|---|---:|---:|---:|---|
|`R3_HREMODEL_G4`|54/81/29|211|0/1|Q10/cut25, .7941676731144435|
|`R3_HBRIDGE_S1_G3`|44/66/24|121|1/0|P17/cut17, .9668955428814634|
|`R3_HS1_RETRACT_G6`|50/75/27|121|1/0|P22/cut20, .7915900949045496|
|`R3_HS1_RETRACT_G8`|50/75/27|121|1/0|P22/cut20, .7915899742430361|
|`R3_H49_TRUNC_SMALL_G8`|94/141/49|121|1/0|P66/cut20, .7910156301372002|
|`R3_H49_TRUNC_MED_G8`|94/141/49|738|2/6|Six positive Q bars below1e-8|
|`R3_H44_GROWN_S1_G6`|84/126/44|121|1/0|P54/cut22, .7379371658078545|
|`R3_H44_GROWN_S1_G8`|84/126/44|121|1/0|P54/cut22, .7379370989585050|

All have additionalweak000/primitivezero000. Depth always means `(birth-death)/birth`. Complete rational masses, moments, centroids, polygons, edges, positive bars, components, cuts and paths regenerate exactly.

Some actual volumes and centres, approximately:

```text
H29 G4: V=2.6591040388988025,
g=(.21940456835,.01822971191,.14074009249)
H24 S1 G3: V=3.4009272368985033,
g=(-.26348079509,-.20145320106,-.04619446286)
H27 G8: V=2.029977154683927,
g=(-.38652519949,-.24219551675,-.04303365439)
H44 G6: V=2.1793307601767844,
g=(-.43963506203,-.26176005308,-.05543678906)
```

The H29 bridge generator recentres its starting representation. Centre differences crossing that coordinate-frame change are not physical mass-displacement measurements. H27/truncation/H44 share the later frame.

H24 G3 has S3, U0/43, H7–23; its stable octagon `[1,4,7,11,33,39,40,43]` contains junior U43. Later H27 and H44 stable faces contain elder U0. **No detached-stable S1 claim is made.**

Nonwinning arithmetic controls remain preserved. H29 G3 is exact222 with a positive P bar about5.51e-6; G4/G5/G6 are211. H24 S1 G3/G4/G5/G6 are121. H27 G4 is8/5/11, not coarse121. The four historical `H23_REMODEL_Gk` filenames actually have F24/V44/E66: G3 is367 and G4/G5/G6 are356. Four acute-pair grids are457. Filename suffixes do not override actual geometry.

## 3. Whole-P22 removal transfers the defect

The small exact H27 truncation appends22 halfspaces. Their removed old-vertex sets, in added-plane order, are:

```text
[[16],[26],[29],[31],[27],[35],[39],[42],[44],[48],
[40,41],[43],[45],[46],[47],[49],[33,34],[36],
[33,34],[38],[37],[40,41]]
```

Their union is exactly the old P22 component:

```text
[16,26,27,29,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
```

All28 complementary old vertices remain. All22 packet vertices disappear. There are66 genuine new vertices and actual `Δ(V,E,F)=(44,66,22)`. Four planes cut close pairs, so this is not justified by pretending there are22 independent single-vertex stars; the count comes from the rebuilt hull.

Old U49 is physically absent. Elder U0 remains and new junior92 replaces49. The result is still exact121, with P66/cut20. This is a finite exact demonstration that removing the entire old material component can transfer rather than annihilate the defect.

The certificate also proves, in the common input frame:

```text
0<Vol(parent)-Vol(small)<1/200000
0<||g_small-g_parent||_infinity<1/400000
```

The actual centre was not held fixed. The medium truncation is exact738 with two P bars and six Q bars, each strictly between0 and1e-8. Every positive bar remains in the audit.

Observed:

```text
WHOLE_P22_EXACT_TRUNCATION_ROOT_REPLACEMENT_OWN121_PASS 22 [0, 92]
FINITE_TRUNCATION_MASS_MOVE_AND_SIX_REAL_Q_BIRTHS_PASS
```

`TRUNCATION_CERTIFICATE.json`:1084 bytes, SHA256 `cb0c3d8c92d9c362ca2d7d0a54cf9792c17f55a09d5314890140d0d4d7f4cd2e`.

## 4. Last exact continuation body

Use `R3_H44_GROWN_S1_G6` for simpler arithmetic, or the independently audited G8 grid. G6 has maximum vertex numerator/denominator complexity62 bits and largest centroid denominator8748 bits; G8 has82/12023 bits. These are not the small support-row bit counts.

```text
G6 input1505B SHA c8817ebe0366e8da2da16a2886e6d2f6fc1a8bc0ac3b44578fe12c55aed94a94
G6 audit79844B SHA 0f8c198d1e9123e92adc0eed5f95af17ebcaafaca77d036fceb44abdcd5f32ad
G8 input1857B SHA 70869ec303f23c0fced740e0468d86a8be25e942be2f19593e2aa998bdb6ba85
G8 audit107935B SHA 6be59a01f955468412c13b7f98a64ed176016c5248d4cd882970909831045df9
```

Complete literal G6 input, also in the recovery package; each `[a,b,c,h]` means `a*x+b*y+c*z<=h`:

```json
{"name":"R3_H44_GROWN_S1_G6","halfspaces":[[-910728,789910,-290980,1000000],[-815027,1495305,26495,1000000],[-862516,479207,-458064,1000000],[-893470,1111850,-141095,1000000],[-617519,2021021,650689,1000000],[-655450,1962149,248395,1000000],[-142760,-912800,-734235,1000000],[-333584,937912,-1102726,1000000],[-100531,-157666,-955666,1000000],[449937,1176903,-1530338,1000000],[-440133,1910662,1460261,1000000],[-241218,2053446,-733049,1000000],[-71846,1705776,-1150719,1000000],[414758,-1541987,-70898,1000000],[142699,-1250380,-512623,1000000],[838678,-1819380,829457,1000000],[-474041,2104433,-226173,1000000],[-545740,2008697,1050447,1000000],[-292461,1740742,1851404,1000000],[-97947,1497603,2214614,1000000],[-133899,1592168,1834462,1000000],[129678,1158344,2515502,1000000],[379534,726572,2717864,1000000],[622488,207097,2771305,1000000],[822136,-360098,2633928,1000000],[944206,-932947,2275965,1000000],[947991,-1421527,1702571,1000000],[-616338,233717,-655870,1000000],[-366546,-122629,-788911,1000000],[-48051,-192200,-969504,1000000],[191867,-689682,-879888,1000000],[-131202,514325,-1099556,1000000],[39829,1634533,-1166733,1000000],[35281,1605926,-168952,1000000],[310924,-837450,-624566,1000000],[567816,-1018677,-104222,1000000],[961592,-748577,476916,1000000],[353858,1009696,1191052,1000000],[566062,692408,1277821,1000000],[844972,298639,1185414,1000000],[990151,-6950,874001,1000000],[1014262,-472136,664725,1000000],[-178306,1616491,1964304,1000000],[-34361,1418442,2181920,1000000]]}
```

Both fine grids have S2, U0/82, H4–17 and stable octagon `[0,4,5,79,80,81,75,73]`. Complete continuation-critical P data:

```text
peak=82, elder=0, attaining_edge=[4,17]
component=[17,18,20,29,30,31,32,33,34,35,38,39,42,43,44,45,46,47,48,49,
50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,
73,74,75,76,77,78,79,80,81,82,83]
cut=[[0,73],[1,72],[2,69],[3,67],[4,17],[5,79],[6,58],[7,59],[9,53],
[10,48],[12,47],[13,49],[14,46],[17,19],[19,20],[25,44],[27,43],[32,36],
[36,42],[39,41],[40,43],[41,49]]
path=[82,83,81,80,78,76,71,39,38,35,33,31,30,29,20,18,17,4,0]
```

An executed exact index check gives:

```text
Junior82 neighbours=[74,77,83]
Junior-star canonical facets=[28,39,41], input rows=[9,40,41]
Saddle4--17 owner facets=[0,6], input rows=[2,6]
Stable facet2 input row=15
```

Thus **input rows `[2,6,9,40,41]`** are a concrete joint junior/saddle-carrier block for the next finite experiment. Row9 carries a nineteen-gon: moving it changes a macroscopic boundary region and the actual volume moment. Row15 is an optional stable guard; neither its permanence nor preservation of root0 is required. This is a proposed frontier, **not an executed cancellation or proof that five rows suffice**.

The exact44-row input permits41 additional halfspaces under `F<=85 => E<=249`. The floating checkpoint still has49 rows, five inactive; only36 additional rows are safe under that bound unless they are explicitly pruned. Inactive rows can reactivate. Actual final edges remain controlling.

The P22 experiment shows why shallow removal of a whole old packet is not itself success. A next operation should change the remaining root star and saddle/interface geometry together, recompute own mass, and track both complete landscapes through any temporary extra extrema. The original acute-tip and retained-normal obstructions do not apply to this H44 body.

## 5. Verification, numerical methods and limits

The new `exact_h.py` exhausts plane triples with integer Cramer's rule, checks all inequalities, reconstructs exact maximal polygonal facets and takes edges only from polygon boundaries. Oriented facet-area vectors sum exactly to zero, are positive multiples of their supporting normals, and span rank3; this proves boundedness rather than inferring it from finite intersections.

Fans are used only for filled-volume integration. With oriented determinants d, `V=sum(d)/6`, `M=sum[d*(a+b+c)]/24`, `g=M/V`. The auditor checks g strictly inside every halfspace, all strict/closed-weak facet-foot and vertex-cone inequalities, and all mixed-edge normal-cone inequalities. For an edge foot `y_i+t*d`, strict H needs `0<t<1` and positive coefficients of both incident outward normals; weak tests close all conditions jointly. Euler is only a post-check. Every polar denominator `h-n·g` is positive and every exact positive P/Q bar is kept.

R3 and JB_CONT211_G6 were independently reconstructed by H and V enumeration, agreeing exactly on geometry, mass, census and normalized forests. A six-quadrilateral cube control gave8/12/6, volume8 and6/8/12. New H endpoints have **one complete exact H hull engine**, not two independent hull audits; shared mechanics formulas are not advertised as independent implementations.

Exact work used CPython3.13.5 standard library. Numerical work used NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, CPUfloat64, BLAS/OMP/torch threads1 and no RNG. All runnable producing modules, inputs and parameters are in the inline package, with complete commands in `README_W49.md`.

Large support replacements used root-free square-root relative-bar Adam. H retraction used direct escape margin1e-5, feasibility tolerance1e-8,20 nonlinear corrections, row-normalized SLSQP, ftol1e-11/maxiter150, and live root/witness/hull/centroid reselection. Numerical forests suppress depths<=1e-14 only for guidance; exact audits do not.

The requested50-step first growth retraction was interrupted by a tool wall limit. Only iterations0 and10 were printed. Its surviving complete pin `HGROW_RET_BEST.json` is2970 bytes, SHA256 `15613248e1c85cad0c84febfa40091a255a0581bf61fcd0fec8a9d0407827f27`, depth.7517280223800529; its exact iteration is not asserted. Subsequent8-step and12-step runs completed8 and12 accepted steps, ending at.7448990224688827 and.7379370969916236. The full final49-row pin is preserved. Six executed pin-freeze checks reproduce all four H24 and both H44 integer grids byte-for-byte. No cross-version optimizer byte identity is promised.

Finite negative methods are preserved:24 original-R3 normal-chain samples, nine later primal bridges, a650-case twisted-chain ledger, and2200-step small-cover reconsolidation. The twist grid is `m={24,32}`, `gamma=-4,-3.875,...,4`, `k={-.08,-.04,0,.04,.08}`. No numerical own110 or reference110 was found; best observed own S/U was3/2 and reference S/U2/1. These are finite observations, not continuous-family exclusions or weak certificates.

## 6. Complete recovery capsule

Write the following source as `RECOVER_W49.py` with LF endings:

```sh
python -B -S RECOVER_W49.py W49_SOURCE
cd W49_SOURCE
python -B -S REPLAY_W49.py
python -B -S CONTINUATION_INDEX.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B FREEZE_KNOWN_PINS.py
```

Exact replay can be split into consecutive batches `--start 0 --stop 10`, `--start 10 --stop 12`, `--start 12 --stop 14`, `--start 14 --stop 22`, `--start 22 --stop 26`, then `--finish`. These batches were actually executed in a recovered directory. Pin-freezing is optional for exact endpoint verification and requires the numerical dependencies; the other commands use only standard library.

```text
60 files; sum decoded file bytes147189
Decoded source dictionary151541 bytes
Dictionary SHA256216c04b45a65fdf0791ea06cabae5edcdf6c8f9a833ffc8c0c648b8141b71dfb
RECOVER_W49.py51501 bytes
Source SHA256ec89b9ef3b7daeb409a6bd1ed2cecfd2592b2b6c5435f60e7507c92c0026d670
W49_SOURCE_RECOVERY_PASS 60 151541 216c04b45a65fdf0791ea06cabae5edcdf6c8f9a833ffc8c0c648b8141b71dfb
W49_EXACT_HANDOFF_PASS 26 64 58
W49_EXACT_CONTINUATION_CARRIERS_PASS
Six W49_RETAINED_PIN_EXACT_GRID_PASS markers
```

The capsule contains every rational endpoint, original R3/JB dependencies, both auditors, complete proofs and producing/search modules, exact audit byte/hash manifest, the650-case ledger and all critical retained pins. `FILES_SHA256.json` binds every other decoded file. No earlier sandbox, external library, optimizer replay or downloaded audit is required for exact recovery.

Convenience copies: [recovery source](sandbox:/mnt/data/RECOVER_W49.py), [source archive](sandbox:/mnt/data/W49_SOURCE.zip), [observed exact audits](sandbox:/mnt/data/W49_OBSERVED_AUDITS.zip). They supplement the complete inline source below.

```python
"""Recover all W49 exact inputs, auditors, proofs, and complete producing sources.
Only the Python standard library is needed; no network or earlier sandbox.
"""
import base64,hashlib,json,lzma,sys
from pathlib import Path
DATA = """\
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;!pIO=v@Fkh=e6lGu?3D1AQJj4sx7r_TCl8*8Hxizhd`Q)O8fO(a48UE4wMi7i19Sl~;n)
bmXa<K&(Re1t6tkUqrt@27Kxq-)vgew8vc>5ui?iwXKje?T;k6`9hKwEmW6<HOXS&?C>UmdGMR5gPFJIFRreJ%7txYZa?bKEFuFl
=O-Elw7{b?5atSMI3<`jzUsbUKbq#FNNox0-Lmbm7*HNlW*xhTgQy%`cusSgY@k$i4iv@Hxgq(%7-{8RCZ(S|gPEGQEQ{#R?D-TE
hJ5~nSheqBiu~v5shBLZpc_yyM8kTu_X{@6Nx$i=x+9Q29vnb+Cw1&wC2G~~;TD<+-~FZ)e5CESuWER%eq0}_UzU-z+wF8C6z%=p
m8f0>-R##~By`RWb4rsPuhmVp5Z~==|K3fv7GdfEUu`lx>_a$%r^{jzwa73yg9m*pDH&qBjMIX7<J)Zbq~qzokBUu&BU&GCkH+D#
iTM<@jPZAcO;zzo#9kWj#=gEss0==tLNneQ1Op7eO{ywu*in_t$iPQa-v-RaAFe`Zfa($0BuO!}b~<{x<Rq<PA^%^rhMe$bbmYRZ
!bB1Q$p)Z7s{ofh&(tAA);WGh`A8d;fnWf{tx9bJJZB3`10M>rPii8B@0NtoAtZxT0?_2=$m4ODFdgVq*ig><^1~-q(`a%H66w@0
FM|gKMT^yYhF5m(tweI)<nF$zh8u}IkI$O@9RAFaRg2!I@MT&iN~}wDpX~bVeIK_NUWW4w%swT+ZJ<=5BZfN`;l7qFooIh48TAXH
ea`b?t4ZDgK6fE2Uf3Vn|2cc`v{aYt<L7{)FlMjncWLT1P!SNIW5&^I*s7Br%XE_de?xK$NqISS_=JxH=L@!VDD~Mq?G%1ve5^Su
P=8i|O`r0L`fXkL{4|P$bpiz?uI>9B;BBjM*9BZ3o0xD&|3y)agF=vR9id?s>=N(-n>#UoMxNtftE!y}tQI2V)_3gw7~P6KpOov7
z)%4`Fy7&kj}QiSGD}45t=z%H%7JmaFX3zK&B*?2;c1}J#yS*W`gY{zsCAp;%oXSLaUbT^i}%71Xg8?`07o9Vf}y)RT8mPN=aG;(
`6VYz#sl|ubJ53Uhg6Xa3O+2-gOxUBTD-hoTZC`)00sOD{vf@uLj@TC^t6k5VpeY~*`FZ0tUi(VtoQm@+3h~D;}kj@2!Ti$Ou)^a
1Bo80n9kSJR83SJG`fNRPW|-c{pddLTo(#GX0T?^%1h*I72u3?#?8E~c<<&?25HpC!NOIQO!e<CPb$V+;VV!t1h&u8ww?o)NVr@r
bW`2X*kFII@YVGhJm^}Ca>L&NB})h)?%?by`j?OnAN-}4BfH^PGx~{L6$5XFoy@>Oc-!jk_*4|9m7<+P8^5E><Oo$8Nq6%3X`rdQ
%n4Cvz^vPR_PIwZc4W90*U*buVi#DE(+_OW_A;!|$MZM^|7SG5Xf9}Yrh>P_Yn_cVNZKk@|GiWEw|ME|bai_2)~jBc+f3t{Q>ySC
Xfl1TE!arE|1tir&#boiyRW+9V6sr4ZUf2>I;laeeU7r!r)Vfu9J$zkCF!W)N4<ozEo?gS`WgjdrVY6bTxKAF|3{W!uxS+_cqB9E
Z{O59lCXCeIAMp*pwe-gcLswoWWbXDUq{sxLcZkty)RG;oN|taf)iJE=$DWbr<EO5J!u#Zm$(;KUjpnL0#UK4gfhU8C#1pI?*f!I
7Cx$^yf;SOw&FGFa4t;5ZOvG`Wxv6Ux$%pAOoCfVTRe_zQ<Q@$X1EF?!>7I|nqz9YF*Wi(A&d75jUUe0BerH4%YxeVjswI_PCtNw
AN2!`ep!3+w?AK-9m)TY_qB7W9}6h=!d0;z-a{LCT26CDhKj>I#OKp?Rb(vvt`QV_A1Xf<cf06|XZXMAEz@R9(r^Y_xAy=BVly>*
fy`;FMf31!1fG60;F~_--6b>L@7BTs&`srMR9IV?VYoe{7iom5?K_RNw+}6_kDUESkz-cgUX%P?YYzO-h6_x>M`om%sZLatOkW-a
liKs9162NJ&dB<M<mSU?OL5yMLaXwt74B1K01fx8^mm~WkShVrB$PZeFqr0c2X(99pgR1k{(Wp-aC{~A(aAFfWB^s@HOcve@}=^P
Il^n9_J`N2&(5#Y1g4sWbMG@y7oNoA&a3QBoWdAv0Xv{d3-%3y*>=faeI>$FDn)I014tP8Fe7}Iff{?|ow5H1^NDQ)ig^^TDkz><
Y#?7&_A(N;D`}3%t;|NiRSAvmQp1tw0Tzh%_`o6_F;XS5?`uw$8yY)P1gjDM67N{)AaR@_s*RBr|LrrzTkfAa!GPHEq8;wxPh;+4
Ov1LkEkGDzy=*xpC$h&a5qQj~Lp6YFzBY&L9NIq=)Y(ex9PHy+huk}T)08~ILZhh|pYNhk5(Ii2q5!RLa(isNu?d8WuI_V5cTyDg
kqS|tGuuO~dV|kT?mI>pSu>=KLqPsBZ)}4IE*sFwDY*`I`T_y%A2=3%iWHK(&oU$#*M>hc7mu;_CV70mzZH9e&%_|N;3ejndp!oj
X&E?~nYhEI=7nsV5WHwEx?0B7;YmLi3oVRwVJqXedE*`0I2P_SyIK94MGUu}V_L%YV-&HR>ZnZj&<W_+I)uIP;Gkb7I-Hp39q}Sy
QP>CS%0x^WZ$DrxC8b!E=EBo@=?5dZ=e=1TT1jU#<B@&!nKF6e4W2r<&!cbH+j&mJH8*b7{O`bPtZPdwcDRt-hCMvjJ3zvJ<Z&6#
$af;~y~?{Ltv_)Mt4WVOBHW?*ZiNI~D$<X+KNi~9bW_zLa8x04B6!~7^DYr`pAI6v%)m~y@OV8_oNG!uA^*;x!JU7G<W6muXI5{{
1~hOWM!Vym@81?<AjE9Zp5vPJ$WofYLiw)EJDlo~CXw3py3%j83rc$l+>#j_AqqwR5GPiave;}4I8LFW^4v8p*CjR@uKKoVQDs$R
{3{0e%Y8{MasZwCsYdt+;tc)neaJt;t*$oMrl!CdL<JESeHCIcjCqzITBT%ksNBDRR4QnQ6A`bd3+lUhQ5|!B(ZBF5%Dk@G*}=J6
DBK;_=yL62^8p0Po%n^~^L%u(kK?*Ab~%H8yb(0DEoGWdFR`S>E~3SH=HH``>6AzA%|8;~ENsG2SM4cf=#bQS<U|l|>G$+T7=Hou
8YxDRFRaHz@fas%@yZGe*#W6kzKz`_WTQq%@~8<EA<~QHaS3tD8Jg8b0O&;?LAG@ql|FuGuOw~{iF<kynRzG?uW3ZtE2=zf#I|2z
oUUJZV0v%etbe?5>Y$VfF4Y*JD7w)sFXIXqFz-nM=ci_t2i(dG@Zk4sn|rPRlGyB)q9n5pp@Q6u$S2qdC}Ysz7w5UnaV{NKrp4?Y
V-YXw4%j52O2ICL|7Xvh&Z7Zm+NUGx<eK7UT6()b#&~x7KPi9fgJ8qhgb6`X`GGZZlXG=VCPl#pE(S)rS*bRHyCwDWI0A_uZ?cEE
y+3mr|HtZA<G?!&%9#W)JE|kQi^?4y8y3TcF_?@gzMq|mWiZM@dUlQ8xyLuHbCTWyjk$L9u>6mmP3lG}_^(cPy}e4A1kI5myQDu9
Ckkx0^~IyCJh0{PmYY^P6pi4S6Uz7%c8K_^>ztLVc%z*7ICL4i1eA(PcJo|zv2v(-sQjsV5A9~%kv^->%y@5xA%&*lcA^hsGhWn5
1ipu(P5H_O498v40f_{kBDpBRbL?FehEV#>s6JLtLY1yncbohZ4^8_EQ4pRH{7K=yeM3G=A1+`pDL+8iRo=3g*wXi+t)kD&i-OaU
$IQ*R0*{)#T(dk~JSX%<L&yge3KbKnLi1lA^|$s9M2H2C?`N9>xr!o93~>$p=A-D7MCxM>tiR8%9iHcLLAd-vrao>H@<AbJ0;(&a
Xm%%4n+N7KU0CDp1Q1qCnSY!#2vz5V2Y_jyU^-QT?q}<wyiEn1iMHp*q3%shpHq0wU*&zZ<kJ%8XjD#=r)<k<XtnPKU9cfnHn*^W
=##TgP)@lOd_NA`@8IIM>AwORHF?}1)Mp9D%xN_1BUma$Z~WJG<YnLNac*wn`A#4Y>ZKBtcU$aU_!v6?>_ryDf5j2OTv#SO6CT>J
H<VBOk}{~dL^nXST?o4dKRA48cU9`PevTau?fG|Guv{?oJvkiJodkZ>0a*28{h+R4Vwcv5FE27|$Bw$W7G-#Iubfa{#LHh!2gysG
+g+-KQJ=o*BLV-^m7OYZv}kH@^I=)~>iM|0r3#CfVT}V~ZVMje#C}_c{+w3*81rLT_a2?|8s&qPaEMw*1R^Z-?0APjZY1S_be7HY
?<@m@gIPA2h(4Xj=Z05U%)HSnQ4m*UmnSow@IE__xh{8&DRgTCK^<wCl61fe$p$v{=qD*Vsbe;g&cLOy|8S@q6lx|{BER+CLFm2D
Jx2;$5{S;*FW`}RLtt7mvJSuN8c`;Z@VW|Rzn==<cXHX*&wP5cGbvfXSjq_ip2G<Ftd!P831dLlYFR+#M59LMGd3AfPtOM$@bq)K
u}k^=6WG>Sy-<tVkc5v3&KKoen}+9PV-Rr*vYPrNdS(i!2Fy37u)O$)G#iIFe1%_rSaW9Fd}CloO9`KGRibvqend6!kXFbE1M@W4
TbTD=JDUiwgYT(&pM&f!Y5VqK<6BHNM6yHO04K;UBPfkeK}R&6*496fD<r3U%CpVM$90vbO;xliNoqh?o|`?n1~AqI&G84JX1zoR
vLfH&AP6+F6CYQl__x971joJfT3Fk%_DL|??YI|q#vIG|M(3}aF`w?wDYFVNSAVsjG>zc~2aeO8!;iufX9vUv9yX{Sw>J_ur_(bP
n(fO<CP1r%onNAM)bYU4opD=j?b=lUBDzN6NKo`Z2iISNvOj{5f_L)f^a_);L9^6mQb9l{6xx<CTUP?QA37R5!U_u)a=@JakG8ia
^s_MjEfJKFS?(g1cM~4gmHa;nmWs5!D|e7~@D2)VA>5x7VzQ6on8oHgJGs(rYyE5AeI?q&{mowp;u*ze9t)N7l`$KE6VBQscuQ%g
+j9aIK5Uc(T3f@WI}Cfs&}&byb`p&h%x^+AYYUIB{B(mR$F0iX%<Na^f)hkd+Ua89$S@g^u?zZmWAq#n=T54ej4#cHZc+j82ZKGt
lUBdf#1AOmuA!~Uyca9AFbT1*&24U_M&EY5|896mA^Qg;ojw*9c6Y2xS%x;Mzdo#8rZ}a|yq7gAOGYMT7@dRaKDu-;%JMLpwJK%b
Y3;!_RX)F>03jGOt~TthJmed&)>_gHY>}@@vS+flc5?H<Y~-WFxvM6T%8eT>LyGD0u@!slR-3bfa$m_QOmK%L3imL+?Tfpksbbg#
mq!J|)7-IgzT`S%k8qCQ&}P(v8wRP#=pZXsyl_2JA{3dKuxLyQ+x)cReLplIU-_3q-i;yxV1ZlmXM#(atg*L~le`RGYII`nzUjo~
-I7lxvT4{JN2QW7x1QIUpOJQ_ew~zlKOS~Ar^>q%U8JDdX#73-jYgA}HQ=S8j|r+k6Sjg8)-^qEAyTpZxQnEtjsO)ztjX>9J#aK1
^3&s{S7gt@IW@(pQZ7J)W}quM)S-c42-7_u9lcBs)dQjd!+93(yPkwY|MYjjo_CuwF;;+Gz#^zSHl)I|3TUBK_-@&@%fTIS+!)Gg
l%~8{vKL}P5SU@E{hV$6k7t_3!j-s_f7qrQ^bl5oEjA8&1I@rrwG9$Zb`q<iZt6D^Uon`+Z&oup8#`TG<GZZxN(pQL-?kEFZA(5t
(l`*!>Cg?q?9cJc<{ZFKLcV7EwDYDmCgVN|<o-MG*+jTehX1*xlW2azK212JaL(Td-X*H%%PK736o=J2e|cvt!`y#pky%?A{e`3s
*m*#KMEo6_!9;a6k6$_6>lb2hT6&O^z-E6y%I|W0;?yVUMCCJr{kEO~3vz7$BrG*99;<@|M8|tSHBtN+%QTzb(Q+ah9WA0}M^`r-
dzaA(dLYLMjBC(Dq#3b80olq2GVeTVtbdJ`Kl5ESehM1MNh!MWPJh`P%{ts|ujn8;$p&Q<9Fl-htl@Hh2@QrnrM(PMBfIi*E#ls`
TWrAz&*|ZI<^rD*k%dI8NoyKFGrLyVO{O4>e?JifE<Ahn-**0?0Ya_rB=_$buHQxq?PCcDk{AUBQ@>B>XsefD>Eztg#=*=`n)xUA
_K<uWk7i!J0w!dFe>W2+MHko0ri^!j1-o^qsRvo}b5B@07+~!nB^ivuCk^}TEWs5J*l$bfjwo3+9mIebX9b~2VX|jC$}Z>=z3!B!
>7O@?N&e)!U+w2+zPJU_^7omh$UY#);<J)s6F0o_RlEFLLr!jaFI#cdDW7q69C}6e-#K+p$6=rmCEaPxmfM`$IYw%xfe+hl)Xl?%
nc1^b#L2gOa8m|-x1?Y)VQ|ymGLu<ZMay+_>}8bh4G(ylana)pW;VBoQ2}NMr3tmvP}btu6ZOZ+3Y|FFwY;j?;NSvh&36{JinSlV
r++zZ3mRKbaH+yEW$zC615WI<$W!|Ld3bO`Dj!rRrI#P-p==$Eej^{3!%_99?SxM|W63z$6o*1+yX@Phg|%@0BqHz?|7S-ql_i+K
-SojD<|H-$^HNP99LeS@*Am>4L)WaSJFVx7li~^XeCT|M#LIp_A$Aed2~U)b+FD8UZCg>jhOb6g>?%qlJFAOJ*}O5J8hkW!hv~&9
QI#p%O#ok>&A5g2VYat5Nu(TBS>X8$2npFJ8&pCp+j0pjCU4a_`%C35Cn`rNgyR)EDmE)#226)%yYK$Kp0q9dr2#)d5{jgj<2uB^
xgFCJ66vXg0r(jjdr3($y|$o{rdT-6*S2%P!ymznJ!g+Fxag2N5omLVBL`NYoNDL7tS&CsG`bZrGwArKi)TiI=>CmpHx1tAW!K-g
%o>bpwZ`1YFchn599LWXjjN6|PrAS7$m)eeoIe1(ykJo-ASSL;#eXFY144l|s$TA*Z*jZ6zYubJuM3gR5CGJIRP>HzG$@5MpDb&f
yKh|e%2o$VKpV^eeWXJRJ%n+~6;~cbZAHp&sHg!HdKAn1Y<1kA_T;Ru=LUSD6Z6eN9exYqiD2k0hxb8F)>J<<Z4?RLo2r$?Br>8|
O23QuC^U+BpQDZ9VMz3Oe9{}~D_ovuUvvKMu*>&uzZGp>C<nF#nzXdGd<Uh=4?C|?bS(Jq5b5~DVXBb16o5qY1<=>r-lSVT;-v^q
1vV<$>;9}*&1K|_+^PPQ5^+lYk_!8kCr!*a_yY!oHXTr|!++M;&ZR?fSSEbPL)qN7QN(0&%eBKl9~y&v3(YNpZE^m%4gzYMU)Mf=
^~={#v>>l319I<ws~tbOF-TWr0R$F@NR-tVVOC+x6V@}=4Gpgzxf7Xq;0~)YX~BoNU4m4y3cWb-2@-&xJ@^983RbrDufR2%-_2RM
s&U1va|p3OT&xxTokDygHqq3(uvPUits=fxWK1tBNjmGcE{`bVbVsMNad9wq3Mpk4=@=TyrTI^_DmIMee^B{t`UBivJAArE<Sqz^
BNXINkK(G}`2r$aM*06e3Um#MTHfigJtc$xuU|W6nqnick7DxH31QVkP4>S#qo8AfiyH&dLB1TE&w!JqrS6sKu>l0@A;h&cG(v7%
*EF6OH_*h#i{0|0m0{r*e<5I4ocqCmN!e&s-tjtyYU5&b>34c<hveLW=`&+EKEez+@)VRmj-=dl8+()|tZF=}99yar!2r^<8O%go
C@S1$f$-~+c_F3U`+7yXN0Ol7&hljJ5b5j7KMWEgbYJxbfFcJulligZWi5Z;G=&tW9f8ddy(R9dCt~pV9f*CDb*PxqXK@l@r6U7d
pXOp~&-Tmg2;Y=aWmI$#UgrnK^F}m|Q*nd`Do{=3GVqE(Fw7=yh|jhzJDoym{BxzU`TfUExu~PvAuEEIcE6y$>ODKFHy{-}5q7_G
c*+B7JhLV&*DQ?SxD<L>K{+3u|J~;TgHvtY+ara7$&3rKrdj!3kxJ$4`u?bif;dnue}S<@|MI2FjxZIUMyNGqVM7iHC+z(`2m4|%
fhCq`_A}_rIpykEbDAqKcn$iCv`l9UfMsEHOE1N6Y<+D_d|@c~GRV>YMFpAep0I}YPlH|apLHPNesvL6(Sr^$n;l%>L7tNthaQg)
pt7<c!Oky%H(G;>QBg+p{qTgVx0B-0GM8;aX{(B(1jVY8Z&hGlcHN(S?B3me%XyqKF7R~oG|x^#ZjCa`cQ;N!&fsXLFf3j#7^K!<
Nw5yB1&k#7x`T80?8t6FX>WMi>g533Wx%FWE{A?|rab2Ob$U9B6iz01XM1QlGaP}+962x9ql$M0K4w`RmvN!7>NzeR&(|0n_XqJx
CQ2WGYcFW~B+pc5Z8U&M80?8h6kX8}Y=9=Wvevky6b$4{<Hsm=y&-~0#MmZR?puFhjzM#w-ZBk)L9nGTBx)d2nWCSlB(ZMgU$9R$
Lw0t$w-$n1TN)aDFweH`YN{dI#ASH8>3rF6fl!sS2ytAi!ue_ijCl-akp~~Ao(MAFmOzw>m5O8#@(>6vY|)S_DdShYaN>1bz2^Qm
@Z2ByCMG`4oal6miocSVWTq=q#V2gOHG?8N8kkd)$gJYWMJL5K_FbB94`*HiMs7n=spPkUNm`$Z+$gA9nbYwsk-Zz3;wiMtI!e89
s<&y~L<aymEh=TS#nPJ64!gAmt5#vus6H-7Xxb9*pCu9d=8YyhLYIa28DnKU!Sft8BbA4mRlwF_@{|#0Fg#}#d{q(VbR!FCB36wr
Fcv~I>Dv&51!vkl`|;5ID&7;{-q_^@LpRMaDbl-N9eUdsk;cUpOUkF-m%ub6<d;Ou8OMe(&%J|+HU$(xh$P;RAY&mRt$gHl!b8+5
^yyzkV+Wz5GXcw%r#83>iOLDDh<VB5Ptj+JIjvm3VJ8nIQAAL7Dp1krmZ={2MBF@=Nq$KMJr5r3cuNb#sf--mb~h-cJBO{)e&F#y
o+@4Ov_PiQ)SVvA-b1e9fzn5-Cm~^?)RF>E&%L>x#3M|PqW}s|5~x-a9*2}vFI<3zJ52ge;LEj5w{}cX@NJu|9VWO)vJt1k-Itd6
vO>4)fbzLDSQ}Od?TJG-3HJ3--y2~GYI4)r*UF3NlTtg2bsHtw9P|D@eXtL_JZ=xUFmct4mY_{RlG-ja^B|Bnvh6MA+SPazIIkT~
6O^})%y@uJ^&8LA&fcs9d_s1FycraJuXR*QVjSq2@K*!5UMKo!!O6g7X5G&FJ3-{8?7kmkE$EgCoGL@=3Hd9W^w^mtQh28g%<E4!
usLm~Z4xyQ9uVM!%Y)Dq#|Wd8cdP!MWG#+(X>ZK&Orof$p*lgnB~^7Klt&pOghNtpQ~_G?h)NufrH#K(p_Z=D{JClQo!oOB5@TQQ
XTPg++ZT+lFb1_(Irg15VegERI$oi7?*C&dIncVZK=y8m(Gln)d|#s0F^=pb6z@zlg1!Z@_CAO7A<Uk&^Cs|-%<X-}z-7KDg69Nz
$QRhl*Ea|o)a4)A?4e3riP%W>CRX($EFtz}_xBF5h5Ai{7eW@>#D?m~&19f_m(y0fbA!#7O)Uwr-VI!=L<eVL@{%Ey^ai2Vhu;oK
5Ti|3DH44twEqg;OSZgjh?vLR&?BKSoR2Q2`__oH)BKvyoTEiok{%YG`z_X}olINC^Mv(DQmttfodpz~)SVJ$;Bz?7zG@r0Jf3+N
KW_nyQ5yUiX)$d{ioD84y<j#?VEhT7xxw3AnYkx4N0HmPq0Atos7~SGMkvxc53c#lxhFby+m%Y{w*1Ics2=%&_fv61q)!NvR2T;b
KQuY6Trry}nV5kOU83Zu5pfuv;7p(_T|Z))#MD9)_=gL0riq@y8c2y0imh2$#wIInt7ay0k*1O`*kKGPtktx)RZRvp7olu!`uG{3
v3!%u%RsU-7fANJR1t;qD`g`ZJ0_}I09@$)xZ&Nv!6)wa6B8yUPgQN%IB@%jW#1{=9f4uEo#4|Rbwyhl?2x<daozLJ_dL>#V^6i|
nd+);iqO|$DUU4W_lX&8f`;S;(GDY<6eg-t{r75PGuu~~B8OB&v#>zpJn{=VM0Car&N%uLDRt;QW`Z>~Jrw8dcntdPof@YzS$LBS
4n)O(q)?|Ps?qseg@}>rO4V|g(f+8Q;>%U9X%374&*?)Z24E@vA43|@Ct@Wk3Sdf<lwabLNv|*MOTbx-mW1X<(#72t1^*jt)GJ>?
2Bsq;y(9Xi!~~0*C<y1wVW;{1J&s*>XxFAcW2qs-%rLOR#-wC&RblkTOHJy+&3|%JWi$p3_N_w-JO8E|V&n>2RyGg%-fg~Zv@ppW
SbR}w0a`n}Bt&e`w{hL8tQdiE{(bdb)%HH5R7P5D5+D(2M(bgbGwG4h@v*Wnywc}ec-1_x12BMM>Dh6O7pM;!wNJ0@mJRRJ#3`aP
QV74$p(LF^0`<-vG1}dlh6C1+z&^L>R=t&(5W&xXLDij-EyCK=1u-Z1Up7(^6@c8E4PW?uRywE6V}>^Za2$Y&pB)hKOu&M6zPNxV
tCH>Ufp&ijZ)mRR32^LwG$ekdfonWXR_by!j?uc?(9H!T8)*?EdqTqs@~op<4F!pcBQ)eTLk31d>F>^N;CI4+oRU`H1r^gweK%e~
QzG9m#X7rkyiM)IV1eLL>mAkb>ui70mG{7N4ubI7JI+HbMDc~kHn^V<DLU}2o)_t9f>l8A%*-c%%V`I5^k&7Way5D-OqrdnM#OGb
n6%VV>zo7U5IZQJ0a7NNo<2IoLw_IJy<k$9m$i9%966C1u*VcT=7<F9D-i>`{Mh$tc{LwZ%yjd%1V?;blFa3RX;FoW>1UR5D1QFg
vq$bWx3ix(t!%7*aAcuiRaoSHYeP>U0iPzoCAy0{pwT&qr9)@lvr31!(o0#)F9AJ{&Xb#`v5k{74pNKy9!fiFpu=Uh6|_wE&to&O
M>z7;cFmh5$yR?gI(bYZhP(1Cg~E7YZO!zT__*fuIuIrRr5yL30$N%XYwa^kFd`E&a^c{(gy>z+d_bvsXd~~oBNFug678N}RqBfe
mRa-*(N@sLH@tgQxW~*P_#67`qTFMZV<dz8J(+Ufj&)pTJC)CMMG?g8#Vmn+)GG(2qk@;57Oj5)UZ(2xds@|pAwI+Nw}saridCJw
p(#ZTn+WzzI=z~`7$n*Ng*jbxgL+8giNTJn+n-?D@`Ii!a&z8e@@m-*qoqJ!K@+m>1%~5@1U}Gz>W^w~D4>OgH@KP^s-}ZD;{l>O
$8^2%MkFT35o!Ic`lNZ~{S}*l2XJI)Sp)o4Wyx&;U2<AX$EnpiG5=60;^wMgCpLe22j#vN_<A3<G6t)RkzEQaS`)};T}~JT;j1?e
o9Ghvm6u!Z-bD$wckPOj%j0iIj^e33dw^SB9GWCC;w#v)8~>nkbs>M_JA*d10VX+)U9EN@g>lSss2fvmFp}TCtq%=Go_}WFW9IVH
4rI8rq5MfX(a49TC{E+=(Zg6D%J0T|*M=fgWej-?9K?<06e!y{SSfkXGV^%&*$|W5Dd8P)1ZB0=y_G>@rSlftl<*z-ujamt$5~6m
2*Bl?<}uawz~9q0EUe1od{gYYB_WJGDMk5hCd8?-B|I<U>}<t{eLh?Dfp*85ve_DxyDPsT#MV|5I|IELcEU|Y<Q^~aztx-4LXpE>
aetbL4rm@g*{QCqG1$fm_2u*Vg2NyVr|;a&WKia4PdF(5otb$vl*KFl7)P*9F=7b{p$>Lg#11lgdZ$eom=trG>U;y28ZXu+-A+M(
DzqMap6m?uwQ=GzZMat(z%fhmua6Ps`lVZKd(%H`v?M$kaxfJ`mEC27p_rOb*rcvQV$M*F5u}#^SH&66Y4$gMzsnW<^xAfjYTDLe
o6e0CYoBn4Y$#Jjmk>Csa)?TtiPME6`W7iert_zILR|cwd{I-`LB(#Cb$>=*iP-|pAf=w4e|_<>S^5Gv>{z7>Me<>XWOK6Zd1R;T
pBE~wG*PQjX@eBfI&7w*%NLLm#0>2#1Quxhj*CH|R_#;$Tp&VgA!p}4n{;iK2bPI-g4_JlhuM5q1`NCjz*zH{G?q}Jn_fH@yYhA|
`{EW^eT}F|tS(;rA=Qm{DWm@$7}H!E304Q!@XF!z!*U)~l#B>;zbcR2<+>8_UNBWfZtgpdC@hM)EK`Un0CHLAwG{ku={89ijFa}X
7Ns~r!aK2EF!k}cy2d3%IMMtmhT*ZvG-jg1C9P9vwXY|VQE|Ft{AeIEvPwh|kXuiNywnX&&U;yCkmYBMfW3XY)37P{ne3R<gXUXZ
w(4TLq#bx;m4;Z&exTSmqiR80K>_-1*FM)MY!fh3-nMGXc#4`1?0+h*$<8Cna!~xv?u!E<J?46qMLyA9%PX|&FmC6)B;op7KU%H#
a#cy-rAmEd+kF;!+Zgfjl(cw<@)Ff28Oy&oGZjUuksTz!g$~8UAOaBq#`Xu}mDtv4VC<~Em^5TA5Og1@WmuDfO*Bw-?r!L2SkRIc
=S9nN6#I9IrFaHe!lGsS;N0z8m66U^c}3<8q#h+A;YvhlbOu*)_0|N{PK+B+eAcoqSJcXP$ip#*cu90|8nFhTJ~DYqRsX00zjmgu
X6OJW_F2X^>D_AQiWrIowDb-JOwPNm+zSg!wbwDKQI%P9X*NL$(gUw;^t4k-iMd#>as!5qA-umyzL$fsk$C(U3P`@ZGl%&nR!}UY
0&@QKKmbV-sGwHcP?w=z#hb6ege|>zTiCDC_~DT1;NyPP7>oJ@>1EL&aD?`H9yDaKn7W}AZU`f$EV1tys+O6&8QerIhNV>BF_+My
sX>3VQ1V#a3XaJEgM`OZl<y6P2c(+Ax?YG!&Z#ih)*?!AedqBxK^5yC5=oT~#Lc%M$`^-wqYOHasl?q_vXq>1)y8B&?Q?Ka>l96w
q75s`ECA)zv@hE=k!=v|y_SZRu#aiK3Bcbk#h(vi?u#Qd`tEHCjJKyKm_`?{))D4^#7*Pqxi{+Y*rHZIdVj&Ey(!~vRD+3iE@bE7
Gs5ZABCh+xSs!d1+%p+y$vho5Sm<G9?cxO<yG`qMju3NePQ{XbR-0(N&T7y7QWe`BU9lss<R&3_1UMR4f>_-fUw)pZwNCO?;1LJu
`5?p8?8ofa8zC;q{p%kJ^v^99XDQK4{_;vWDm-57rU>t;Fc1LkG&x;Z*riJ{tnY~nFk0K<&Xp54KJycVD2wClc;G0ys8cSl+MS-5
sk(|)$;c)U*XWWo(&BD`%xI(+V9k?Z1CXgz>&aUg4|43Pdy6r+V`fKDOr&M=*)xikZRvXy_Qf+Fff|O`qkVvduMS;~x|S9&g+zZc
mCK+Cdr#J2ICo4~^mJUO?34#!!_ZS36DgjIDKezt6P)sVLF2M9o<JmD`?MaM(D1LgCACoD`~}vrDobUU)Dp}Dqz(GoP?4L?TC9PB
9?E%qL;9DEbBE2gKnk_63hu7=#wIgrEnQC6yF9KJ0z+`J&*UIFMxJ&bXXSQ7mr&n}z$k{dC<*O&#I;0{{B4#+kD@|9^=N?6L7jL_
;L28PgDQSE#vxv2Gvyu15+GmUn<HZJ_7Tl)QM!H54Y;TcmN||apI*2b;5$8o*J#O&USUMx86zcWxRS}LmboQ|B(3+Q^N4Jtp({pJ
k0~F>wAQk!zrXm}B~NJ1A!vU975o-k!t_3=0nVf5D|LonXoCjw`PbT;6_Tu<3uds)85``O|EIfYe%~U2<oT4|q%}FCk(sFX{gy~v
90Bg8;a|3g#DwWB1FW_I^EhRFAfO!!9=c*$A7;?ST(Ivt8d{R!^Wm|f@$!<>jEhog>zfY8F{k-$wm=HSGrkOTqKnl3mkIUTR;Ct+
gWe_6fxt?&mQwb@D9lI7svLtgNRz%`ynqJnRDYh#Uk&dFfC<{l)=pwerl{Yr4JMJRfsl|2^?9vx5_zD9Eefhdnsv2pu@SgYuSWFv
WT9~+Jt}JShnn`kS?GH{1NaeARb&s&rc`*5V>WsW%0UHQscYk98bV(poZ!c!mAvqU-t168v*@Mvd*vcihr0x5N|@yGFXV|bdy9DR
BSubSC1C`sy*p)VC@FmHcgOT7A7KgjRuFwU`k6N#kJ*K-RFwm2wjK-#DU{}Zz%44==t*tq>h3U6g5POX)3k4(F)$CgF~jXQ_77gl
z|cPhi+sg(BC_GIue$(!E8Ky&6MSs`)h65>PrSJD-`QIdC_7<V8He)Sh0;CIgDl71K2sm-`SsGJmD<~?Iu154%tWo4io?if-QqC6
)jV&A?WbB_H(*bQ3@!xWcj=S`t{9JM!<A!o#)oChEj4e6@(M|!RWIK&t;{O@ry&%n1lyQh`eI`Y;1z&d3{3MeI;nzYv4`%qvo*ND
+xNET8)b7SjY4yfNQGN0DF@78<1xBe_0ll>ypyqnCpKiUhw%DpQ{3M}0`h1?Uu!D4coV*WBASUx-7u!mc23l_kO4Z0bveHLKbOrd
y{yD#9_O@Tcw!K5GiSzd_7XP3hxA-lhC0CgDSaqkY>dV#I*L|De2>J-K~A7}W8?vE49c5P_~z;>%$PG3NBQZG8%X}`ygpRU4=;Kg
C1t->t|a51K!7lN=VWZ*lI`Z@Q&>zE^1u#cB$hqmpA+cP?K;(X1?1(Kr6sv9Cr743bz_=p`IF+5p@VQsbynB;Q3Hk_9mC>Mto{5!
e|Kox)hn*Z2k$w0?MdSEP4~`6Cs}jE{51aHK^tQ-c-mlLN%z9ce(&eewP#(XcNX4lg$Clokjdh|OZ~a&ySz0rmooWldXi?X%1BYW
Sm~he?>nmX?LbkvR$O$EQSKdXLl^bL23tD09)w}ZIfVG0VWASdr5lnteR@Jf04h|;dJtsznJ3Z3PT`-#N5u4OeM$jteP;l#rHqo#
MzrC>zsQHFFwbp!8`h7y)*e*(nVCKung}3$AS>DXLI_H>?w3hlhv$O;PIDVp|CTMd+R}*8s|7OCNlVTwK^zeThGt;m|DPiOGGr`o
jShMcWM7KHcp1YOKaPk5lU5RXVKX}W)#wYg0K(YM&ICsbQcuuyU#!rJ0acA*xCMv-oB&=o%5LDUY0Ok23?%CV{uOjd<0xL0*|}dF
!hMj_Pta12v};t8!=F#*gk6U@uOu&+V953n4NPH(Oo=O<D{Q8`R7gF}X$c7T>jb|X#c-r`xc@0F7ZrISc}RQTVObi*$vvo?8pLx0
*CvS`0KMhB;!R){Cl^)W3NxMN;29s@7pGj)pC?v?J?==2(5%4L-F*fab}3vWAoWRFt<9@zCNxtT(ffy&A7gyw0~xJ3mv_V1UoFkc
BDTY@$TOj{9lG?dSi%Vt%1T0k#8>PH{DW(48$15@+4UVtj;POkKT=gSmd&Acz(G~t2jO_FTDk}23t7|`0sYT*DGr-4LnKm_+&a(~
#D3KVdW3CIAQO^`MGrxU@NU#lG>rj20ro^ks;Ee^=lW2!+bb4|Rf+uk`@W@45MlZp1rJF@{7aV^u=6M1h?LF<RZO--3&25jIKWMo
2y^6L`Z*QJBWVrl8mJfNh*hegMHM$F_Ni#khgV8c0I=Vlw=#xq8SU)cLY$zVTmC*w!e%7tJ2@;01Fth(kJ){=QNG?%)n1nX5+;YW
8{Ulg4_QeL_WqAv(wR$GhKsV3VV%Jm6<@e7qu$~HZ7`ykz}YaXk|uICjLed-TQwC2CckpPT7mn+tssCls@{j94&CdYeO2BCN`F4)
v9w~2UpYOSSRICO1Dv^6@VJBGZrIvM?P8)C%ZG>*Pa1h(#)x(IXugTLq-R2x@eK`lU68KLW;x_$2N8vGyTHb9v|LI0)>7@MIU#b;
1TDNQF<JxiR5ld26FyRqtmn5{%gLHUYobYJqE^fkz5ji2o&9Ep(A-utPViy;sf23w7##)m^9{jEeTfofwznI?-EDBI9eugybHsAD
MG2`OH<&Ont|VK8P3|&$H`88?Ts0TE&Je8@)?odki_66X41-NL{AUC`WQv7Ya90$Z3@yOTfOr6q(QPe6&bce|KMPL`osy@!l6`8A
@Yb3)HK=9NxG>202yg|cpnl*L9MFI=>y<_#FCM~}@GR#}ZQ?+$4sD{JZceG=rH>9J5FQC#L~Rv<iFS&T{el)A>Z{QaoTND85y-&6
iQ=%msDoyiD4gGJFSLrJO9%NlKSWE?gR!D%6b@El>ZF-znR#~$)mS}>lIJ4Wc~Z5yL+mNzn{}Pu%QO8sIqQ{UetOuHi(l+2VgEXz
pO#4YS6@x)LS4Y&tfcWv)69yvI$G1Wq!+A^Z~bB|`}LtJS%s~xMV&bl)B0GSO(j0EbvfDPHuFNRA4W`tvVncGJEQ^Y)j*%6L3~CA
<Xisb&jY`V?tIr0dRHLI4-tkM(L?e^PMge3E2uScD=K*>WO!#Xe|cGdiR!utS2;OnVd{5a0vV6rG`3}TM{&KIf7y5gq?RhpACfKb
MNA!ARtVfj-$Y|(IyOu&#F5-CMc6cQ$lYuDC^!2Zr;Sr(uXZCF!X|Rt=A|9vS&CABF+;`x?GW18VjiDA{k{Q%DS)atT?w}QL8_3?
?yv^xUwfcHQa^6!R2}rf=VAY8J&t9NL)J6;JLtuto!W3jRc48~gPU=#U|4*|r$K0?9lM*_rsE8sf-n0rIz;$P&T=g|0k)rDxp^jU
fzYx;0WIJv|Enarr^$$l_jDS1=F~+%aD%7OHl66#Ix(C6F+Z`!2U?Qw5GY0Sl^cud#>UaVAiW1Dmmx`^PzEb(SXZ~8+@Wie0eqX2
R{ThXK_hu1MEUTameGv$KfHmC8yd$F@(cZ6KbUjXko?#Alh#H3gcvQVQ)mi33%Y+lpmt)r^c8=rz(D^{O4X?&ETMP}8h{OK%O}%`
Pa?*!F&I<Z)$Y_^t{zB@z^)%^Bjh*%LeUzuO=27bIxr*d32E&6eBS#Nl4h0pO*AnSmx)5Ll6{*2I9!@a?pVH!=>JQOXcWFWlQVs~
(}wyU7$&<qb&nb~fUV~OHVN}G2+%r{IRo7=5@5yS5Lz-Yvd^Dpzal1-_&zwn=5|zkf)K2C=97v1kCfdUNr@YBl?hf4DOHzs`}asE
Odf>i#{>~Awi|Chaylk}rECis)|ghs-Vq=VEmxPFtV#U-8BIEw>>I%g!}>R&!fYPtKia%#ma{VS=ft}GCcM2ZkFt49a|_^uVGm8F
0D=2NV!DXW^r`T@kmue(Q|TltmsSQWxIx!ub=NQrG?jigUkfmLi|EK}6=qNGjAUzjKpdJC+=5s^n|SLbYJtaC-8_W2-e+~A5DrvE
_Kgoq#%`GmZC!FU-Y_$K>TD1!v{?KD6<JNwVQyCEFxtoMU_yb-s4&{iJ*0@Z>MydbE<klxo>szNjF-*3*Zpd_!-P+a?wb87ngGZG
X#1VlxzrL=M(6?#1tL~qp%p)ms5jc?jGAo59|T#p@&Zvkfv!1sRFQ}5B3gRQMzzV)DA-bjh}iMk0;SUc6nZv4Q!*%M-i$f+%kh2X
R!Q_c(JZbqXSI1<Ht0S4-~q%Jw)4+iD}1VJKM^n>A8eH`1%(xsDbnfp9ad>`{wUq?>UEQkE|R}LAki(_nPvx48aL73m(0f33^rC}
+Drv`0K{@(NU=ha)tQDU_``_&sV#;nE6?lomgkJR-nI*=afs5wm<A(CT8EYGIX-p?`pE9bvJR&Stz@!zBnb7{(K5<A@IrL;;W9k4
$G?o7iovTuU597=qZ-zfhge@KjJ&Hg(ft~MUPAWId9JYL2&q-_A_y;@WmL&M;1>Zr28RcRXEI=-EA(SIEOc`IT1>n5(-x*8Zf3*V
2gLst8rQ2pGZ`Cs1Xj=Fer0L^w-jJLPeIy%=PUXYOI}72t;J$Ssp>d}2X;IpJXmSrU^EFK4|)iUXk|4spaoX{{B-#7;U`Q}a=Qm7
E$+Zsp=#p)u51(d*Bj!xsH6#Pu))`vGjz((REWlsk4)4UZj&49Rtli;jLJImZQAp!t!nB@hWDV|RcXWLoOLV<l<Z)v<EWo8+0xBm
X5LNXC+!ZKB@EA7%mR(g)Euoij>&xiiEuO2f;J<;!D~z+j{Q1|k|K+eeS^B!na%AN?q>!xLQtiyUH5RWc)If05k;GoG$iVY<Fn)O
HQ2E8-8(VX%fK?Qajo!~l)TOc&+E<%khlVO?(l0~l_|{edAVpSfx-5_Yhd~4vqqDhv*6VYvntSL@X^o8p$`Y7xH0}!v1!AQJo<7)
rh>Mng9!W5&V~=cnX08E=;lzMQOaY>u%ajxVVn<d8o90;uk*l}%AnDL)e-+DX#w(+A$*}csy2C>;Kd_)^P-h)&C<80nv8ZI=(^>P
wq(va>{!&1XHYwWuI_2sW5E^}n^DxP_h(;XL6k((B6=&GT7Zjf*c^=iQPcTr(GP9&key_b!1Z@h<{%KZ<Cx38*-E6+Z)Pa|OUqI(
Ifw&pbZwpa8JbkX<drY3OyHYvIDTNZvXo_fwD=}QR0Wf)27&=7d`2ijK>DiQ$RBmC+lNNAwv_tkVpYZCSZoG}*sn?Qg**r|n)5Lg
bmb6Ms2yoo<=A(=gpl3F68`XW?!dyjo>-%z2!XiuMb&fP*#wZw%!Z%5*Z#zjK5le900<3sHQdOFN(BEnt=VG)qC4w=e=G0^;$<~R
%q~zj<8!C?5gFAz@o&D$vx7wpS9JJS!nwpw>j-8L$~l4{G)B%y(5a(K3ErVOJPYNZbwxc$){NWC#XiSu2D2Fl+^&uKUaJ2h%ndu9
RuSD4LK{1;>PT4JAPB0yz`Bq|8?0ik0$<g}Mzp-|oiH20?z(vPDvtrLYhf*TyF>toeQwL^aN&drdLnFT9;6T`MlVp7NSPv)Njgc?
j;#h|<%8_LfJt}ey#ujDBf{Vjc|8I3R|`XZP=<j}a~@K}w;h1L?V4GVyZ4u5kE}Y8T}?CqoN)9^&1TcVBZhSvXYk&5ryRXR^9#jc
zRjk!M&NcqB%Vy;rq(r}R+hv?d1zq!Z}nc-h3Pvlr-T{?IU0sfreYG{{2S-rjRDSZns7>#v$1nOq_N(AoUzMQ?snq(8z)tXkqq8?
MyfS+a2m&{UQ~bHcqk#IvBwvp(Q1==<q9oil4T5iylksabL@QqgAXY#58P`;K_@GV=jzm<HcnM+1am{#g*c$^lch!uGm*Z602cCx
_pT$iQzaSnT9BCz9?cPzNJG(0@!99lU8*P$5_)Fjmw+1boZSX}n2jgXAjVwi12BE^xNx4K(a^E}K~DA=_Uy;c4{-;(Fk-zVHUKMW
C+0}wdH1~6=FX}JhuS^=R**X{upz-m0k!0YvF$h?_%p4UZzLRV$ym1@?RROmxnJPt-_g7WpM??eZ&~SZQd_bYV%A>2A({KH_l(!U
N6--E!a`HJ3oG0K5?e)tM0=$gEYNz3rV`ZotEOsmV__{jfQ?>z*fsV`=Jn1OiUU(F)q=RtQfdx}jV_s)Eq`Y-1*YY!;s3HNWX1v$
px!hGGD<zmL>*h^F@1a@>Hf+*Wn+PQ0FQE~6u;mQhWcCrk&kvwl#Wuln-ce$gfvn2VThrEA60*~13g4K`_n`=^bN?bius?&+;29-
wrEM6eX-aNY%0=2NLHe7tk*Cji7;>V66s>8t&tD^yMtSy&e>Csk@Sk3H(0g)W{#j+aG@lnyS<-}<DKpVzbSM86HR<6<>RSc3Ra%y
XYmjwD>iW_vFB`hMEVVTlqYm6l6|S3k=K%SDDE1_3~tr;FhbwJZb-%&p{xXj$$mxP7yWuNl><CRthOlK5ZOn_$h2sY0qv8MVy+1(
LPuwI;E`<qmwiQ56yDk$;dD3Uye{}n6r^N!<iEf+5Sub8NmuL7unZB+7uXu|0|!%kiNC9KS_Z4(IXw4G_t%Q+^3h-PKK6fvFPzru
!k%TB-|w$`sPG)@5kN&6?uW;*r6CeV6E~#2dM2I`D@=VIT=D)AMI@T6@M3IZp$i*|3_3=zf;gidgE<3`$I4-X6YIYO;=qcupgn_8
6Q1L1WUl4AL_xtfV+y5<1^s_0eoAk}bSz>&;VFeEMIDnu_DFX9oF9L1>r3uQW^AI%h|UL|0p2uYNmC$ZqCqbg7w`JRFUZ+v8o#q9
bF;C@sY`Z_YI2^^!M#@8&T&-8$zasslQvAhJ-gyPgQScoEnWm*8;lQrje|0QBjMD8FJ<ZFr1F|JQG045wXqQ8SnR6!K&zoQ4Z!C}
Co9g~;a<_q;MnggQgy%=^=j=Ud=|jeg1a!urKHX`!k%1Acnz)VBf;m!0fZpz4f`EDAuBEQ*+{@JhzyX!^Xqp33vkmQPv^}jOQoYD
wW%p^dviXoFA@oPyoUQo2{QwS9faTx74VmI^FVyCmNv5iP*;#C)@e(BS`nS|e513@)TwzSVC2^fhao<aySPKNR85+04O)iYCBhV3
A$^Ye+sN*TB9uc@*KQfrDC9fJoKq*jxjT3p*9r2mN!Zq#1iqjX==5%YE@z?Vu<8^;dsBM<Ur%m^64xT1)GE&OjJic(ARZ^nXzmLX
%b~^Bm&Wx}a9T#(Eh)7!XO(^N;P@2$^elY1i6d<8h3aB+pLZ*{rCrILs?2T_X8dgO!Wy_aSPC9Cw>j`hUJruHh)klV@#i9C3U6OD
ww2hCH`o>@^#^SP_9dX~O~o~N_b5{5a~rL$1o(68-PMG6_kXYg9k%klX!lfLxMYJF^P!|^`t9!t7uFhrhXy|5t<89bA-E#ISr&0h
%Hpri%6A|V^ZT(l0S{-0nO`Q%w52J=2}%4?GLa?R!Olv98Ae&ayw#v7e5AE<xU5bVpBS1mf1$H@Cth#8qs&qilEQ!e)0<Lx?h><y
d%4`mm@EQAfT4Eb5OnO<?Rhu;td%PC;V_pICERwSN5eBX{|rj70&X@k^oSVQ1ie!lqstzk(^D)i56gPJcIDKjP>ibOQ|~ydM8Ub~
$Ay#a6=Ml{kCA!M5!38*cD<nw((Lg@;3c%P0-Uc6nlav~UV0d%j!SOWRD&C+g3)`?0nlo0c>GlSND5(UyjGOlfrIm~96Ze)I%u{6
41I;Ir}eb(T^5F>!ETWh|6O-Pa_S3-sL1CQOmI8OFE&D@p~onkzQUIm0A=sa(qaH!UP5r8ZAD#aLdVbcq<>J(K#Qn3kT0(iUJTxU
$NJ3D7&iZj4%i7O5!C!F6G)d;CzlXAI6&r_MGuXG?>}=>Lt=791*=Zs=2(Cc4kdg%M6DK<rX7bJ2iS>&NQq0cN0o&<g|EOZ4urr(
Nq+N2LA47b=LN$>L7j~rqlC<mYfN!H9F50SAi$o}bS5j!xk+T!k!YM84&;#lIp$BZ{2F{@asSIuzlz>x7|t5l6-73DY2hO31~MBP
=!<S5RG?~DJDVuS#d|8#!#Jd?EaaO623hM|qb%L1G01F)6rTO0nh`(7g*O;oo_2ihpMsky!|xPlp#1Es%*}HatNSXJhQzS9<VBdr
T2MDhg8@y%ZQI_N4Z@-mEM+|J_xl<zm{j_2GFElF%*A}sJ&5z?J=iHdM;bNI*ab5*P<iN$zdHy=8m+^~`8uvywFPwb+E2E=AF+mD
Anv>=ZLjjYavxeZ)|Il(H&dHm1QcggbysM<L_EKDz1)nH^Rsc;2WFc<ZdHpP5(r8?CvrN^FV`N>;PemaokIZAi$e9x*Z-H%KGdV+
RsgOB(UTG`=AvbQ_sL{n!RYZlWj35AEw9$Em<(w(Z6GVkTbl;%FOSZ6(1dZ23-&gj&Y%+)eGC5K3o{9P4V_bHlhZj+%#wYnfBVaF
TiuhKfDl3gxXa0KIblCv{ZN<+#3Mr&aZ$O+V{2=mB!ph}sf|?ZACJGDcpP{chutZ)I%=P=LVxMCjjdk+XDgC)eOnM0wUrRy1a)J)
In4GE;|iTJglG_=u+mXxI<<BR&%WX7tnR)Fe7=bT;ZR9^+=Tf);c{`p$`Tcfm9`OOFUh?u!>{2|^oY)(e=_k`f1Rf<_tSCTExaA?
qd7P1P|3@Q&sa)4g~kfuA~dr7P?VZ1XC2DBBKwx!WTO2~`PN$&WWop8pWU`-gX|f_cs)#n*;f9liYSB!VuGcFerz2oI&qAd9cH-a
Z-|AsbQMw0sSKzkd?ce#%LVDNlYrU}Rert?I|DkQK@R<2m<IhG@vqnY#LPly;OoWpWWulI_*sT&=JvS&{XjLnJz#~_TfLZobcf0H
Q7J{~A|5$H)_;5m=B-cFgXDffv$yEpPAS-cA2Q|xCxq^jY0_N=Nfs<1Y91}k$cPO)6jf@2g3zqy&5Wq$KO1cY>FiY)N<^ozyY#<c
MDLOUw3CskN`th7YRP=Lk`dILrrBNiGw5}+exJKu^3Zvk%_ntLU|LD4Ck{}3AT|9XLy+<Ql=Wk_4Wla-%LZ2HKET_`#6-D@nW4N`
8Eqluts<-3;XK^E(vKifPX+>znsmVA6^j6%%@LZVlo#?xM6w}v7M?S<NE{Ve5|*qQBpPL)p8ox5Ut)H0|MsArp829=v);Z{q00M-
5W_RHnmu5W63jwI$)JhoRVb+w6>dixxQyWE042(2*>YyikmtWmcuI$>AY;HKz-#DB+`}qQ99*5Z^9f5RKG*_HA{})&)duB|D57>7
&shxRvu!?lS}`n6G@F4Ir7qJ1c>8J9z}T)m-^)HRl-W5bly#Ip<ClQDxrP=QbnuOZ52}b(J7eIb*sx|4tG}_OaMWk)e_>Ntg28Jw
#E4%U5O9KX|FuKP!Q2AN%8*~~L?Q0^460s9%fo!i)=v7V*c0gTqB!H(C+-wu7#SGOitm<my5i8B$cE(kW^quaWxwy(v~Mb3N}M~u
JS|`L)$iuLeY>sJqk0yt<%g=cR|f2`BQ9Z3Mfq0vh?2?os39x<Smm<x9xi2rDnpY`!LP{+XW#CO<!btpT!Qs6+yxETf)xQtM|3^F
s@iCX3I4P}zg%hdA*ofuLZnW+$=uM3cJe}7Iwg=&>9A)tQ*|gY>kt&QkSX+>(fI|&UeDKl?88MQsfe$hmNpTMKu>STV+NDw%<yL~
Xm}RmB=GA*9*8048bfD3m26h9kML<&AT_qDM$6wDqz&5(YHO_;xF>Cd!UtQf?Z>GKf1Y~qGhCOBp3Y;MS~iKq{>#_Hy%Ee)Hkqmh
6j@ah%JNtSs{Y8&BiH3!m$*k!)#GQ*>YvzfX<w)`joUlok2~x#%(X$5^OVVC!|Zox3Ib=-xAijpbuEWg74z%7y1n|DTd#YWblZOb
Vk;q6fWaAo1H5R;i*)Va#2ZQ@wnml0;J@ml`A2?8x3=gvk98v9QDBKqz-UiS%QwB578(XDSt$4?FX}@aaw-R{1N-kU>drZfPYSgf
=U}Qg=N30oGT*9whgb*xCd0M0NxB>48uD#*3bMIaCwgP*F-e&T1=rIBI&$xOk11~BrhC|hdlNH()utGRcsqu}qLj8HuIfaZ!nG(Y
XEeD-?HUDDY~v}tuJh_ZiCn&(XkqD~9Q50i`U}9Tx>?F~ibr*ODBvZhmzi(cqdrz-Q0P-B#>u2AFdnIw^Je8w6^KH;CS%yketlud
oXZ*?R~$~;Vp3!-t;X+G$PPq<`E|QG%n%OA1c$5IZnMeMaj=u?Id5I$y9|MrWo$sxx(mLGi8`IU(>fa;hz3Uo@-jk_EM$_UCOvuL
{GXNNrfVJSjK%d6Q(q|FI~Frz<Mxdm1{XKp1J1sZQ=eIE!+AvE*R>@MM~IO9s?P*A%3LTnJDJk)p}V2fD<;ZyLq<;LjIn>!-c5aN
Ku<VA5KJxJkP_net`F#(9M-FsGc9vlE)`fHfkyuk&(%DHABl2$)WL5-i`JPTcEf1oI+^W)tod#6Zm6aG<G$hfG^$4g)2NUpcc-}#
P$>{MPysiCAvGqf1(`A8|A@RTa19W-9gyjY&_+vs(F=g*V`e_$-Mqr`aeB6BIcty_qt$nV%Jl=T?6H8Tu=;h~XL^Bs%;tr>fMSj<
>hk~sbSxnRywlv{Z2&&DX{!!Kn}X%pn;R%&uWt%M{ecD<O98D~Cu8`oh`CD=Jolv0MCXAO<v#*)&}#HCWxG0nbAT5Fdh!VD6nd#r
6R<E&rogE13~Q@hey})El>oKM+K@`W)3w0{SFlJ25$3}Q3Jn8J54T$BBB{lES@eZcn*yomhK&(c&}v@svYj4Go-hBD0a%Z62}1r;
NQFNEs#J~rHz3tyg7%^RGp!LA(E;;__k?hp3a1XIXkP#00%5K`BdHXj=i%GFubqD_;`6JMXwYrO940GlmgtvdDd8ln2DEn89*e=h
*FdD~@>##;Y2~4R&IyM>m@bOpjEEuaN%mV#CuB(OD4_s(X_sQL#oGPi?+jNxdMP@G$$XBf&eNOk+ISoMTac<Uv#e-Pa@pCeO(bMb
wa4aB^R9$5e@&LL6QVu@dRXK#@VN_gxk86$^OgE?0#p4PXAasd{X8vuF3##cWpu|*T45X^_P~Y@-N>DvW(-z@Au^;jv_}(YZ&0bO
QJ#N_$PEtgx)x94&96NM*<TyrkN&}|PE#{rQ*vo!k5bA2Q#{Pe?>gAiMv3RzhPL}B`}J;Hgj6gb6y_0rLe5;Ya_`9X*#I}p-l?nO
gJA3i@vC2rXIlwnc#Bz<K1eE9UmhOcM0=!+Es<@rivhc>gymfiv9xCem+THn#d%kLBmUsC^rX-7(*9k(RMHjp8pw>NbLwk23(h1)
d=UvZ{oG&x{bMU^t0QPT2<-UV^_)NuEW{lyhK%l6xf%yy?1Kh`K8r7JIt~YU<B2+ji~#M#;RTEizI7i1ZJFmug&ySu@0bQWHbVW$
9TEK<viqI>+#n{_e@_Hn7%KUU6BOQ23^1#K&Q>@(gt3t6Yq*gW*Z4~OcUIXeiG55_GB6;d+GqB_<uzO5|1Aj$?51s2{hi8QLY{bx
l=)?=iZ4fmx*-eh>$+#UIV~{6&C{c}9IyhP@52m{)ZHK`b)|a9`cpVLVvu~H;>9hDy6yZH8;^q-oIOmr?weft&NX{74Hhg8oPV4F
<W+}>!vy3x1ciSZ@!?ami8Yx6F8p=pgI%-xxAQr}HG`P4KRTuU*+F;L(N)x-72Y*j%#P>ea3>T=dV&q?F2B7!;}kEG?3qkiDu?A=
zkU+9NXIp4rev-C`TvghRdQ@ZFW80lV_<|F*4dG-XAzXOhQ-uRP>FF$fa9gknJncFs>qfravEWI_`Nul2p0(l8N{T3Hd%wQJCvlb
i3rFyARs5!mb|Lh0L#FfKR77HAISS=dz$-BXqE-M_ELprY7`-I>s6-gW5fFB3jBjhQwR4FfiX+F?hc{y&OMn#m&&X-m`4iVv7U5E
qBlhrRnO-^({)_W5tYD_9UlXeKB_DsctKyNqlc;s)xD8B43eZXB)1zx15W_IU4{%yH>vaVEQI(Va4dVeCrBd10w0RV5b(k~%WWD;
kdD@>iqCUjPViq@B_4tI^GW_r#0$QT0sU2k)|Lrh-`M4JPBg8-dwq^5Q%_&F?sRSW!N0b35F@HR&{7OM$LEQFVw7Cms<hF=&cRK6
3jq7cW6^W!dGa9`SmKcAyRdntc(Nb(;n}ppGp)@oM4fmpA>g_ltH`yv16BG9;UgG*<pnIv<^tyMfVq&54D)`IC2r4jlPdbJO(q`_
cm#2NCjXwOLU4ZgGv2f4F6cgDUWCz5jp<v2NKC4U%waYtnl!qt{uPy(Mcd|HSv0Ua?8AH9c_W*x&`u_=RNy=Xvuly9OkQge!xKt6
aXIA*3xp060)>aZ#yRrh8Ht)28F{vIe+?t8!sqKn0h~p_l5e6~qO&7;H4BdlkL(pnDkxB^o_*X9%e+w~i*loN_tGi}(f^5v#>*`*
!B9U5bMK|IE78CZ+?_#jULtcFTzl1s57fZ^%IYgeR^W_8mYswxy8^E|MMwcKc!5zz9v3P`F8VVEnW-wGP9zVi;#;8!c4L^&V#`9;
U%%Fga%}9M|Fs4y^zu!3{%x1B>WhI&&YUg;oxv*+BM&um<*zOXr9fTQQJE>Oj3$@*$aE}2V7KmPILRYkt}c>UeTYKrK5|7c25=ZA
_L*KL)sO1o5(cQoD$=%aPPDnr3Y&|YLuc7}+u~Jj+a()?<qFy&r^5Upw}08$vC3xu&h-)*L*n(DPzl;(`GPfTWvFmsz~xBuZ7IXu
t<7c}yHtks$aGwOZ`<8KzUM&?)uxuF-c`f(2&=5y@6$4YT(dco%=sSqU4`O6n`s+%oRPBXac@m$_@LrEXJFlQOv!&=N_;rUGU>aj
CdwNH=(F_4@lvf2Nks^V&8|D+^as&T$Y*lJyt`gW!>ZBQx;?GkEdA+B6_6_d3bJ!z=`tDr8!4X{FycXjcbGaPWf?bw=IPnKe3bh!
BtT}MwQE|Z0h1=LGC(3S#icr=IRN>uEpy!Ed7%<n?2f6E&!Vg{sG1x7dcmGpaA%-qTbP>W-CLSAKO{OZzbEWc%DwLSv8+?Dbx`#)
X_z#4JymvjpMtAPY6#Bg?LIGYm3|$;&<lC9fCd!mq66(&B?;nPnZnd0PsY`=eov){`1oekyX^z3rub=)!zL`at!<}MPzv(8I~_U-
;Z`#7Szwpf2X2h*)B#3g0{z^0@m$I|J~)8AVFysDwT!`?ua3C3N35CWcA5WdGeN1c<rCY8Y0c}Xj)hmgj|n1#&Z=fAn>%v=9*|Q5
`~#gwlR3yn#Rvh>y;4h2KDtHDsXA*>Wg+ya^Dt6pdG74*9b(swaT}kCIWWq6Hw=?>ki$Y&404y0Enyde4}Ctu-gU?{v{NfQqRRZR
A}c&ADVWeJ#};_oIN=5Y0?wgA+lfSp9s#^FP_N0aK&;~POd2lSF3Z~;^bt0r#}}h^heM5KL0k=fP0N#=xA6-&B#B!hIaBrzbdaDj
;ZHedr?AVJ!43w{M5H(BgoA?ysf)ZUo&0Hyl&v<2kwp~Ewz>tPAe|MY-@sUWoU^6epBs^HTZq@%1jFgMhNAClGqYeSsKD?GA?%&u
{(fM}nLlho@*-mg8iM@Q<N2Li`@_U8tsIx~7@ksS`b}UKx)b7ApJ@<)%?y^u)3(sdQ2l!|aw}v{5Xe%m?ePM;2X-b;y^hFaA)2rm
F6=$D{LhREy^7xqUx(f&*UCFsu*Se@8nodz;Ot}v+Dl_Z+dfy4zh#dz;G}QTJ5ns`kY?0rJVGH_a3D&j9*3yu>L>~u2l#!bP~6+V
0~W#BuVuy%OdykqL?qOyT^>@l$UBGVX>@RQ0tCjiWs}>pE6Ecqr_sSoYJa8;0Fb*{a@VwqsMx|@yKKUmLHtahm)YMqHk=CP<??AF
ob<8Q#YFbnlyKE@F-X}h7a@~`8CmK8w(K1NL?zkre(SuJmV8DLwJEn^CDlgJgqDJWcaL-lO$XllDM=LFB|9Gq2EjL>CAgCjU{b~t
p|wt~pS~mpbWhUoq`~fJxS6EY1bQyas)!Ov#u}>%HJ^yS2}}+%vXcQ|>A$b_C`kTE$j`VB$K2<SCwQ5+UOS~~FQ%_;l2U6C$DHMF
bIz#wgO~ASqI<PDiV%EDigE7~xb6-DSu3%V56uuKCSXJ;>&UgSepf8ionJd*JM+Zu0BgoDAfmNNr@|6aL<Ep<=@tm|pP5T2lHjR~
+@{Wzws`|yyvWj?_`_;!U+i5YY$l`%K^oiBcDCxf>+gS4l;If*VcCQ^>#9B4>Y1DbMbW52B!?|$I~@%2J`6&00KYEhpEE+6^vnJp
l<tR<#-$tLc6GuiyGtMtl9W01<)%5^)?=MMPVG_n6DcqU|HhF3JELORP{<V8_wZx4sE;5N@V?{T6^|}2=GdF`AggChLaA-_<+=_~
KmX-O`U~)H!R>H`rm96!8^Fa51>jn1Ex;j!;|K+som)<yKDH2^-01DCeOII&rLuNM^r*&w_J5D1JL0C8dh@I15ZbC;+zQ4!5%d%l
kTu*O!B^u~6syQr+INDM>4ixoK)tRA7M-iHtOkjk(aVy$$y)pH#qjR0BluR%(Az>}N2D>*fXz~)&OJsUG#8Q<O(ym^iu~Vgc5Ryw
3A<lh0tPFcofRkWaw9%psxfYd?e8qz*oDrfEN^NuNck5#733HqQegiYAVJlnr=svz6U+K+T=kJ(ChtI!2K5usWLr=BxuK;5xPfX7
5w4RP&j?3V<b*zDTcZSXPQ4jIwQkeTV0fD@b~hh=cmvI^;}2Zs?OnrrS-AIGt}!Xg3<19~9ZnO;R-pynttgtd4~t|=o^uop<$+@y
sN3&uIiuH(=P(}F(%zNTz*3ETmT5<G4Xn%xaGFu)TvzJ0XmH&+I@whL)5qM;B4=Q>zrJPODhYxdb`ko&yz|&Nhfv@2?W<~+(&j@w
*dstkB=bv*ZNPjaSMpG&&uJGyLgFQlHhVhn(5*F6#B`c@qhO|?4LMY;($By(RO9I)=OLDnm+fk!gr@FEC%=+uo|wqt_~U93w*$}|
4gR-Y+^{Tlx<ZI{w<QDCUy-hp#RVDcWEODo$HVEpl~?yw*OZ{VOwFWeQPbLCz7!Z@K3_TOv)DxoQGvvvl0_8LY>Ik@GtLATgr*$}
iwL3rV|1viZ*yrJo3IM;O#KPy8!sAC=(W9$QEJzf2z{k5wmreJAyea=+uZP%3ooa~Y;B>4vAVOOhKPFn(Ri|h(Njal6qa7Z|4BTI
6OPz2-pd;#SDcjrUVtS*A^BJDG)<iHsuGu~_jG>S3Zq9&@JYE>Bv8%N`L34cfSSR-E(a{t<#O$PA3hm%!N|zu@k0Vv^EIcDW#0%_
pH&zZV6p2BhhF>gN#e=}?j-j7I6gGA>y2S3pwA0xT|V$qfOVN#%W#>qIajO+fA-d;w{hfcK_e^o>P+lqZ-O*D3HD{E^*3f0BVG32
jUWS4r^-mr^38Bpl@hQ~(K-UEPTGTnpt~ARA%C?GayW{$)sRtrOyUt}zzQ`Zym>xTcF&N|xKjS;_Xjhx=|BOJDmRo4V^>y-?_EE&
m9@9I_{t`*P!GLEe9-3g3-Lq?WxL0w=bcv0a8ELgNac;o6`k4-iS0Qn^6tJjNg6-Q{>M}K->TgYO%QU<?K*`yU60@T=CcF`fvf4@
(-`AE@Tttesw>KgGyk@b+Nm2T@c_TEnHu$qYcQ*!1VQ-ZT!DyDoIb5eod`C^I%Xy!d3t>=U4LK|cC@dIBA2l6ZJhnLOShfYw6>e@
{+!G3vY~ygu-bq)a|H|<*q{-y1fK!OZV<`*Zh6=_Bq(JX-~$t1N9|+<+O3niFZf=EVBFE4&w+xX3@i*!(6OwcyPfl}vTzxpYD@k_
2h22*bY7WnK|`cNd@pzA^h(z(wy7=Fs9&XP>o%<vnDF3(!~ZjHA0*TP7GM`@j|SDwmd=!U7N3>oBi5<ojV2#3Al;4)h-1jnYGy7m
UeAKN(}!fmZp}D5We3s`Gk}#&)eb5QnL|3`aN>vlA1Mt=wv)(DMz>=Yf3%GL)aCY((u7hv>>T|vt=;pYLY!=37JU!*eku;TZ*paE
#3HjLg!0OHE-F3c-r<r+k%@z7t~_n<F;!=ybhIv*Ab^?5vs}YK=t@GQB`q)1Ios}v;rL&cZeit0ozBL1qzomwlPHPyrh$=Du}i)C
-o5S(+OTaPQ)6XVo_5He;c$c<Ow%L|{J<1s{>kZ(r?kb)Na?c0cJyh=tcb&F@PnV0r3z8QwNl7!AG33KAo@!|5dv1!v}@|oaI~DX
kLKkgbpi&es_Em<WgOf7ZR9K2>bB0cqN1}f&a4BJ3><>=d%~3LO6n>95$y~ETl!=VZKt%6&dfry#&2t*g_IjZgr?Gc^fi4}O?#Fo
H-$IHCX@y~0D(dtXv1d{t}*&k%>S2?^vq;7SVPgC<143)#{IuiE*T+=;9RFrKd)l~A61^b4*KR|)R{h3J+fL3oh?u4biG6xTAoY0
*WxsP4HPS&ygXK?eB`dR;0=&ee?!>RD-!FoALyLW%6(mJ$kjSNAdlNGJKfA=mbViIz=#c)m5P?&SzUF-G*x3xGY0L;;^~>tLU|W4
2_dcISnoqV%PahJw}T7`B>WRkJLdd8`598i&E{RhfUQV1ut$f^(ffW98YMX1JO5~$x3wPh7wE3(OX=@i^l@rDKJFq^(Qfithch;l
Q{TWXwBdNS6pV(Dj=^GJ|Nlfu;oZA4U5adeu@nuqyyz+V3YXP5my(&itV%&+LRGUr{<!e1o8Ygj6{4#VWs7Er_Sz|(iXbYET>Xg{
qHgMos|0+&>E9G^3wErDnVAvO^BF}9?m_^Zc~XRXU$2vIDF#amva@{)M(F92XFfdQVm=~{3KfA?McY~XOc-^SQuy_EBjc9y+)~Rc
nW9X%T~w(>mT)N@LsXhep!O6*oo58>_>IH-rr06SEIc8xEMe3Hp2L^$u}SRAXJQplziG3j;A-n5IZ0ZapyOmsu)MROI4g<0Z-H)G
nw(%jJ!JbH{<>0y{%FhR9TPS46{6Me6W8f%Z;e#&dLS$%GSnmUw|`);7BdWcIL50hFu2!Xj|gQJIhRdpI~KO&NqYF<qkt@~+1rSS
If==+fF?QFP;a9j@lpC%I3PsDKefdIj|iP!dEzw#)gTSSy%R)4Y$5Lv(R?&(RdsJ@p0Ab|yWJ(ucw9Z<{AQ%gx2E*GL@#u#4@o{^
T+-PR(|PQ_4)W=Dt-SCXASXfJv@?Sw7M(V*hV=&&h1^-W!7_zy6FI^OC+Wt>s7K2iPk&(sfXR6j>&myOMr;sfS$@j*?C2Mb$lmUq
KKdW^-59Ib9J|!t-rEo;mmGHxEV(^oEv15R?XYjiJyAHhC_yb=S!;e$U<bES&!1_m$8Dk6bzM^#k|3VJX)q+*&o3Ozs10*|PpT|>
E%@0PGWKI#l!yzmA)B;JU<$R<6R3`EzYW@0%jbGkhS2xHJlncx!b_?Eb+2ew(kRS#_5{hy3?kZ*)05l6V=8r#zlcAr)agAk1aNig
a1ZR0={M318_^Vpu4V!KWs+Tx{@saTt;ybUu5kQl&FW#33cVN*T^Hd32gg{Y#!jBa)JI9MX|W@`btune$uLnp>^z9+OOuE#K7y{U
6{TXeBr$>R@jd1!G2USIo5x-zuOq5MBXO=1yXsMrf{SK+6K>75eP0XaaoLc#uBux>X%??L+|0)dMp@B3J@g&qy0>8nJzQpzL=beU
RT@US%sw((z7c%Ub5wMFZ#PIPP`yzCwzy3os%7<LG^s?MN;dI|6DR7_%ds+E!Kz<wIwNul*LO<K$OqkY^Bqrh5S2TqpF2XiSy`5w
`psheX-h@GAkhD*f2-V{PYe0MNqgm`ub~j~8162yMe56>E+}+&Pflh&h$l4kJuld?UC8vN$ZO#tF!WSFzJb6_!UB#wQf<5(4W<Q4
n)%-Fb5sQ8s$n|?gv?T?;>q}U><RfDG(u})MYzou>l`}`IRaLn$ZF~0cZN6<Y~3l>RJ@9z3ooT9J^>VfGcMp|VcY}L=gf<WP2nj5
c8eml^Am9_g{L2B&t_AT17i$mi@B_eQC%?tr_SB6?XgY&wZSpkGA!v~=BYF(qm+JVe>}rK8|4LG(QTSd_2)`bs#bq>fXj77UJdcC
9%^^MCe-7;{}{$L+KCl~d^aR*1_BjFC6^j@rH+jID?doIBd9Da>>X++n&YGSzh|X`R+stHNb0z?E4a-d-qoyF?Dj}+)l5mzD4sN-
JSpK7O*wB2^`#}WL|E=~ZDEfEVvj&(!s2Sd!0uT%;|`b<IC4^Y;`?6F^;!sS4NX&IVf7M{JU`lw2~bc04WZ^+V7{dB4lax0;V29A
fA|MT!gO+K4YV~Iq;@(L$L<Jsx*_L!LEtx60Oq9vWc{S3fQprzWjstyPX}vg+WDJ-e1|J}JOeFf*0}G8dH>T#rJncPPuUHA?maUT
V99<vQnUK@Yx9cApNc2*uy+}$|3tZdZ;|m~7XYSY-31(+O(?puuV=N+I`HBXK2^BHTQCE@2z?H+!kQ<3!~9bdN>cEW5Kg+iLu|f{
ot7HYK2@U*t;~p%Z7~p)`U%~knxrhnFfb@exyp`PAz#YeiIcAt<FaV+$kyA0Y7|BXdM5h|`+Ss-A>tX+hRaC^#eAl*5JMd`D<G%e
J~@9p*KJ}tKME*%iCewumiCwuJi|JGPsJrPN_;u%630J!+E^XFk|r^Meq_bC3H3Vf){rtS!bK{A(7bfz`tb@=3k{*;p5AQHrEptR
W^Hdj-xWoVSw;kq;A^o@>$rJU55b1p3tGFl88=Md4rzD!ebpx0Y5=(8ZL>vkMN;?GiT#?l_~S(!K_Bk(@xxNAcAIxE@9<ONhx7Nf
vno<v1OkE1mQ1)fi(hH2js)z{euDAbRFK(Bx5ik^C)|d4h<-CM!&}XMc)(E_%W9gMJ?nZ+!O1+DmEhs&(mh<FKEI)BXWx-lpuJDC
sXlmFw-tC+IbAxJvZ2EupSAv!ri8V{_Eo9+;?L^37}#)U(^Euaa00PjZ3HS+Wk&q2e%Q;{3D3bNA;H8Bzve<;^$Ec{fnI^;xSduW
?iRU6&n7V5g#413q`k&!I^oI%1hb%Kqe8~*7@2t(`Ul)Hf5OF1mjb?9cT~@En{X7U_ESaL8%|Q=IOiT)l7v3GXcaqw!hx>in~{cb
{{WG<a~C+^74JS{w6;m_FKhn~QtRt~YqqG7<9)E68$)24>)t`QJXpIh#zN`bCfq}Kc`f3hw_aYc4pYk=7LY2US}ka)DrFysx%f&D
1mCv9dNj;?1;jg+6mJn}DCW<JqfIQn(>D|kp8IWk#^Sbs&daKDaNKgN@fuk^s8iF?C84sq2a^BM)q70rp3r6$2iw7;!R98if}ES{
kIgrX(qSQVP{{Lbx=4x(4<`?xe;JYn5!2CRQ1lzmwx7bosc6aHLb(kW);BS+P5|%}of%dE6j>3L7k4j5fG?PY104?tF~d~Xxal+G
7q&6&b%yO%Ppt+{>2&!%CRzvd%@Io~rJDJnggW_lr@tYAZFNh#Wk~ZeutH^jS_c$!*v&M=z!g;g0T)k>^l@t3EX2BtK)3OOBmWLb
Ln%inDk!1gqTO6^6bw!=z=@4hHwBv2@h96YWz5d>4C2Q~a)^XJA11p>V^I}tAT&MGr57a2Sek6PV8IvO5X`|QgD2}uoY1ZXM`K31
A5&_dKNWnCn#xV+53jqyeO4^t8Ym0Y$D0FckW=HgR7?0iDmb5!hD^rMrjOD?M9FKEN!lBlB(;-}{a|Fjdx6NAM^Q1u^wq*j8w%X1
=bS~K1{Z9m(7~F>IK(cTbQ#pbf9-O*`?Dn(k`lN5g+InlW_dYmAEh#{A2E0VUVmeKF2E5<f-JWghIu&bCG`y;iyalDopQsZUQC^@
A)dE9p8NuYxa$rYbc2_wd}uxsrJ`gZY390fN5&mI^$l}y10l;@jKg0+8Ndb1&)gjBUgtANIn?muR^Ou@0R>Ze=J*POl>1*4$OIr;
Qm=ee5$RbRHe#PHpqS2)F#cr;G_*!1x?98-w<CE-8i{d%SQf!-L^_8l;OCL{J}bJB)p&_3xi9k%qP}7s+c?@_5Q<HJhiJQ5_|2=M
)z!33VQ_U>a2!p#KW0VeBccs_CuMy?ku8ER-^!B)vdFwziJ4taTp>T#D%Y6<d<pnb=?G^$jj_7w#U|8b5V%W{X*l5Wbm2_ic=pCp
RXj;tE%p+>*u$y32gG%}C&oSS!;S7FP}*=-zp|{sHGQ|FloJCx8#xaE6^*qhgL4j2hMO6ou1)s5IfGp=YK*xy)N#a!_>fjo7m0wL
-bX-(HMR*YVPZTvX%jO@+sBE&7|hqiuyv!$w0ZhmBaC6fX^Gi*Y{D!eIwsRo>f$)<m%Q9Lpy>B^!3jX46yGcCQ(Gr9YGBpi7q?Ft
4lasp<KBck&G%6gry14A;$EP(P>sxtL*hhipcO_bO0Y|6&xMZ?U)|waGT;QAM-oHmogt<;x8B?_np$Zd@-jqcf&cLAQHsp93ZDAL
lsVziv=fVe6mHVrNQ8aAHPQSAY`V0`*ui5-SOx@>4;NWAh{jKR+Z2L<*@mlZKrzd-H61bqg>wv<_k|rE@}5}MDM?PGO1(?Fj<^r-
FKL_FCx)^XI})NOqli=(=D=RdIi;k*Zzl$7=2Nj<Ph=aoIw(&+v@bg9-h=uph=6{$$J(d|_U^*FgIUBt<FDC7eF2kj4<oe@BJP>9
+y+j==HH^PbvgZo02pc>ZQ25n*_}jU5G=4mTg1-f99q%!r64k|B^N*1r;xDs(0QtGqjx|LJ+(Y2^J2~P33Lo#f|NGfY7%fD#awN|
o%BJFxAwWOe$N38-6jiF2J<cgg{p_!K=P4J(ClJ!(;>t7_SnDRq81&zPRpixO0fbC+0*O06?3bZ;W7@L3gm1I0nr_(cm&U5mzN%i
MG9s6AvS36eFMX>!xoku!Kwuo0-sY*j4pm{)se@P;bK>a3{}i6vwvFQZ-!=jMIMIQS=#f&zQQM~Mroje3HY*Gky0A%1#nTJJ@;h7
TWDmWxP9FS1J+Oi-;LRsXpDaGvLZ|x^61$>UxhlL_KUiftLN>1#Byk7)&nhv2fj=~g;Q?EOEs5`u0Wq50@G2VP>@D@;x*-#9aeS3
PRf1(lpon5cqh@00OptMQ|F8ec*V^o=&J0gbiFX}`@Qy#2oUX5^%hEavI;DS6x+f^GLWkXPYPmHRhF-IF>oC(4-%8x0p3+!JJiG6
^_k%dPN1zL^nEV@I_o#VR;zi|-)WrK7VFidu0c**vFh-~i48GI*5(3twx;2eGbixP5R&E!-vcxcaZMwk$0l(|h@-m!9!z9Mn?NAd
=vc!6b}q$qJWZaZBuy6}*PC@s)rpa=LjxED?cH44>Y?>qrkH%IJWZTt9?DZoH^ZJHvBiPpy8TJN$K8|M&csjH)<GilK$eqNQ2p4U
o}z&oFc%fciQq*e|8iHF-f6LcVZ)IgQ-nJIZ#e=ErrJ>5EBdRW<23AbXOP@`XI2Km2XU#wYSXD>QNrR&x03j5B))(l!$cT>%lP5#
N3{o%|Hh8+s{sQ@vuBT&yn4dK2iPsYUk95Hh31M7p+OHpn~nn_v$SWb;0l(2n@pc{XP?Msc~rVW>JXK{ECW{Jc+*HuUQ*x;P`~dw
j5jEm?1E<{+<Q|^Qd}oyo=^~@ArhCmmKXs5u9}w#2Z-0FT_|eP7b9)vFH$Av7^}`vQbGCMkxo>Lgq$b8w@&r4_Ipj;k0&RaaoWCu
YwkRL(*!s7;|GX*9EhZaEG>VDz#N+?-~E?@v*0mr;zc5Gve-3K46O{)3#j%Z#^0kJqe*ep>#I?6$Toe08GbBWl(>-ve7M8%smE^?
*R*+@Y%^FR@fm`vkpAYl1t<ML+=J|}VZbU8y{qD1s-+BBiE7y$`t1C~6jfj;IBv!lu;QRrjrW!%UDVu#i}zj%{EHBNG6N?vNW>hI
G1-MZAbiVXf2;wbm-%eHz%$fbG9wPD!VNJ3XR?3}efK01#M5Sn#A+Tf8RJN@d!up8bR*p^D@<A(Fq|tJ(r*XRk@wWloG)&9=1L(J
3V<zrP~2lRl_L_#(V<s_%_E=kU%|}4wYA=7VtKX0qMoj9Pj5=nId|2$X2Lo5&>?9ILDABf$uyFKPMSoT?N&YuY@vVClsjAJ<;H5K
=MEGDHEYb3W6kD;#y%+&D6Dl6R;BuY3fkp6A^t-<e?`4=#Ieq-v)b61h&hZGQ>yqcE~5;|Yfmdtj3MVKgxe}4$37#GFcCc7!DIy{
tlm=lBBetra$ln>X-XJUAez@0|0Ewrfe}DIUND1nHFB!2YJAfNa{R4qw|evt^Q_Fvj(Tw!3M-zCua!HkU<;-lVr(4qqC0avlpZot
-)kRgGb3noh}#^BkHGQeh%5ID?;=AYM4FA!EuOMTo97L2^Q1Km-E;dh9vw!6NP>)-AG7-LH8aWDezMnsG_Q?cY!<zxT>|OrZZr4&
pL*)2jTc#L&79bXJ#xoMF}*sw0%<4EOec>=9$DT>r-z3%)8ukBZm|tbuFz-!t4Po|iHu-^OTq#OOUEeNSEuRYI#Pz8=Ejc!*)Lu2
N_oV1j^3sRz1fzX&wEd!i+ev@2S^MS&JjGFulRDqmMxbrppsKE50drAxPA<|c!TFxqG>NU3w{_PKAaI|H!ATz3JL?$>Exd#y`76_
dm+2~&7^)OAycqmRY;aThK_I7#{>}Wy)etP>EvPouPZGA<rqp~wTMplFyiTl?+Qk`IAFnNd5T&1wXdr9I_W8Xry9Se=RU~d12}LS
?YEH_u=-yJ;qO1;`pPSe)yvZ-x7DC!t&o82;<rFUf}3&69)uC}k4kIPA{xM!soQ*ki^W<*pvfosv^8>Q;fe8%?g`OAivf$z#+PXM
vE@^I)Pr3QfK<U2${EJh05U<1E>c?ojZ5DHh5m-&xBuJO0-9+bS2Ld8b;`CcMAdV2KU|iRh+T+Ki6Z7akoNR;Ix3FP__V<)22e=W
BLW(C9PSKz-jH|R6<<%L4qcmnQUeiyr2f?qVk+^meg}Elk-9Z>Ete&<_@APqvt~8^-5WgIdq$VAuTGj=+3D((3#6_W-V#fVks+al
z6!UwkH($q>1<pSsU5MPq`PK2KLJZ9H{(K|lEYe{#*lEhWEI1~g5kq}ST?+kux`Vo>8iUd>eFQIVlM3*bLi<7vlEV_Jdtxd7!eG;
Ntz<lkL@uCxqOGPw1KE`op%FagzPD1&-<9!+m<y&UdR|zaY=aeg8Oq}BdXM(=abFATgA7h<bsd~OXcUp*|w6t`t32c4gHCY4)cfP
^2OW9D7z0nv?A6Bj>Neyo=eY27J8jO1MYyh+k#)3PsXrAu&*#iwfBa{cvq+oh&FYXJYFB$sY98k!)wlcPqPyF$~-rKN#%51zEbLJ
@f@I^3P3n(OY)k~E^y`ry7HQu5ZMcd-~92RdxR1FPEj?L+=Y5PhZZqK9{2b$X-Kd@KFJRNL!-Qx2qWdu2z#Rc2|vZw>a`P|5Ba=i
KKDm6`JKY8b8l@GnH+DGI6V?g5N!UK8I-`@XO0&{=Z=lxk=z!|pnnl0U*FH3+$u3yJLn(t6Ss~XDN&HYdJhh~Ej5V2)y}hKe+!J6
WNFyx%LYng9KM)@!?}~or!G@^kO8^gOr1|$)lWz}=wZRkE?jKZD{eihBov>(;5((&YnuBfV8>x!<`}hNz%^sar<38#|8PS^6et!t
>yWICq0nA0I=&ATPbqx!pd>ghv_<9#BA`*I=v(Vgx;dyPtSyTvYPy#gBJZPI`?m8@Ii(2jlGo5TNwZn`HNhD->x8#nC0zmm9bO1V
ipyJ?&mFw<2_dn@+>4wZ_h~=~6~?C%0jjt3IpvTY!nLr>S>KT#-bYJ>mASE*`vU{x#*9z_rdU(LBbgk3WbpAIJ89%k{0$gHByd<>
SFMJ9{)OK{s1C^o7)xRpJ#E@mT+KF?v=c0=L3KP2g{E{3$4jcDyv4&*Sy47Ut7gNgNq?Gw{#|KNqcwC;L5#ltzXc!}2#dGHvDOT$
(AYs~Kog;#$`_pq04I+{6)H%co0sDKLlfHug_UB)k+d$3w9SA5xa(xAzZh|m7?lhGe62QF=Cw5)VWYGXI_rS*FX5i-TdvFLJ!U~p
fS=Z?x%=!1%PXy!3+##)fQnKFb$oSe($;GHMtU0of3`Uz6dB4Dl${}0BK^o{&fJl6Yc_ObXCEr&h=rA#KFL$}cX3)c)=SvIFzThl
9T0}kv|33KH^V_l)mdmcy)jSjI&6!fkWW&Xvc-7nH^TQahqqYVFd#y7bL42|(XW#EKU0M+XVgH1zak<yx1X<z)hx?!PYJ{YDdT>B
oJpzy+oXz<-GuL<fWJ#Z)Ft(4^-_{s6ua%5`PGb%?I^Bq$=gouXbj2Pdxv-yaS8OApcC<h<>1O+hD4FU$TpcAjoA2nOpRqr1kM*v
AAKtt)bIw&E1dSLFCe@>?-oHE!_CB@D$FDWky8+0RMGL<Yn*S<6~LnvOHx4L8(FvPU!}^sCeC$G9xxQI%|PJyacs>3+UyZ|?i7~>
q4AVV#1^=NYqR^~+SI=8Xl~dd*~t9o>w~|SH%~7YHi*)smSY$jnU>3^WcnKqc+;;~(?ip2>xRu6e)h4_IYb*RS5M#Uq4GE{l1shx
2XiT&k+wUN=(9xz`G&gj0|d%WKZ@p?9T(Q~<00cNm3``Hl}v2vWKmq0O|)w*t6k9dMPmxov5KxuB_D!|hQr<e<l+$hfoX&ptmrhQ
<pNn!B=F8FSWFm`Kk-pj{MnTkPFt@8hUvtZne4!8_@>O;7~ce)o{Iy*6|zqK#a8+irK|L1`*1?U1pX-&7mNazcI9j<;a!dlQ{1@)
jPWtsKc5V-7W*~LQ*`#K6@h7{gLHWd6<88ripikc)wImpujbO}cS$p}rPoU<BK<CB!_{FP94zZoOa3bZ()QY4RS0X0^xe6lrDI>f
_lQ{ee_oIA0!pEPL$T+0!eM_4SWTePtLEAki22%LHXVhfN9-Q?ERff|B-t{VoK`#mWZ3b1$xu3&#|+t2S<HfDqUV^`XsZVHZ#STW
NsoXUrW7gF&YF0{wU4<%U--|!C`=Xwz?z<lmCSiA?yftfI;(3qC26YurPy7Bky8}>3wumd&~Y`A`fhFsYz6{JTm57?@HO;K`XO<O
cpmd2q79s2anW?M6pFs}tsp3mP$0)|vK;<WH@4v)py()Iid+Aa{<G(Zhk_F(j90k-u?{qu<>N>t{5~F44+w>DuE{)Vov1AlIw{8G
xt)NGnR>IMkCN5$Ujr1=bT8-8pm?D@pb6fef2nr<Nxy(JYf}zM%ll24NIq{CtT%Nk*D?a-%=fok!6UEc&kf6G#gA9Tib#A{UR~S9
m)Ao%Z<uTUs;}mpSXr1Oi<5)>jK+D<gg3!E-zr}+Q$fLm_Q?vkJkr2Be;RHF3I<+vT%`p`cK-7R7s<L<>c?=nrx`gz?<wo(1$2T#
=!xDNuWHzM-}vUHwB;7(dPF>(W^v%JDI-hLdsT|c5o=>s!_!HKGiEG|xqDE9+Ni%h8w)_5o=kkUUZBv(m$KDtQ$pVV=A#%hZ65<~
Fi7MbdDq@<-OE=k@)+^)(7dyWx^JCOpKUFP+DZqDCT<inB0Je)@UQ0dSbmCV{9~Ne7&@o1O0i{@<-00B^8Ruu^m$Jc;531XQg9X1
k6_A3waTZYs>)&&2%M%y&ajP}0Nua^yU)IHl(%JlP4b&8JYxHS71<1u@QLp>p>a6S{ksI#j{}GCR3@Oav14KdBLpsDPk>CLHyUmk
QQQ**W>(7gLa|5vN3Nj1kFMUks!-riW}RNbARj+7n=J02MbNa{>|3Kl(BMHsF-<_Jt2eAIE+Yk1;^DXTlK$sI*mAEbOR)x>LOpI-
lyve;Q7oJGS=}4e{`k&1`hb5>t{UdviqmWMXB1V$^;zztxyx=iFP=GyvL>;#`wRg0Ix|S?oTCgRIm3mSuNc4407EoR)HT1#)Eh#e
joCy`jj1-vRnISpCA(`Nc{X3t0qQ?%GoYp~mwf&EfP`O_AvAiDIO=0G>n*}^mM(@GDi|D|ySdzFL7Fr#_rw&Y1bP<6{)C>nhh^wh
LD}kgKwzgquvx;V+vxZ?nT_R|>QLh&PA$aTz#Vp|3^p6AyBb;?-$8_-3qZ21z0F`ALV3abG)(R}$((WrAA&2T4=UmW6`PuW5VTHi
cc%XvVwp9ZvN%r4HoOxgM!PrHjI32if``_YyFR+PNO{Mg_v}H01C^G$R2oUqcBu{=Ii<}WqSql2S(+~jYz5FOd+01m+ddjQQLx{S
|2f84>FEjvjYn;ElNt&>_1S~Ov>7ZZohvwlY;bo)#P7TH&K;`UOb^?(S*#h3TtAXi;}4*-*o<w?Gu_=rWn`))1*BvUJu5r<|C1+r
3A`yEG;T-h1=H_w@#PXB8ZtP$w}&Uo3w+k7IlG*QSI;DDFe~OtMa-n@vRF}4^n{Xae8+~XX?r0c<Efrm<y1C#d82kqLmvBZv2h6w
;JVyLh<Sn=6)dAEaaY-Vx5N@s?K-)D;+Q3v32wXGf{|zh<5~qm*nbnz5VDq#clQ8Yhf1W?Jfpo9wf_*S#FTUb`#e@cEI?6!jC;;E
#;XjMgSbBfYz96J^c%puee!)@D!78D&Ock&>Y=hR3)+e*Qhbyx3Oky#2n>yey!>_s35bCFgF~L3QcBTR#2U31JA%;|5Zy(HNXws`
of-3z{qDy1cb6eB5)y2{S?`Zc30w;Jbr|=&iKJ+o@}X|JM*7vdeQ{W5eP3=%6l2vNS5-Zf*0fE>#-+f`vqJU2&zNl>7v4ar7q&8y
0|%`b$L-QktD$30TqRac8$rDOH9-U3l$o1Q!k#85TdMpQ9M<imVF7V@^}5$8w9cya9JFf_2e8@~ugP!)?hYNDA$R%5nXrfI@LEL_
*|JDFVHKjI^(=!7K9A1$>w3K)R2N7ql|n%4Zoo2QMoo7=!-tL7O<V_f(NHR})2u3mTtPE_IwcBaAyXBcK!Sn{1BQ(-?|Nea_&|M~
st_uxpVWtN-@a_-F$y%iE!1%aF;Nv1V;WageQ&SuWhs|juX*{`z(v?uI@A%De^@R}OggkZ6C9MY>0+Ony7KqvfsNh`%AoU->2Lee
`-NbZLc-TAH-v?Ak^Xd7ct?4HEGZhOafy)E7K8S{$pT~MVf$@#lC6;sku3T|9}Kx#Ax!FG6tcC3U!_XuQ@dgF;A%+xP%3YreJQ4<
qlSJOUbjFEZ>r%qf0xyO^WGp;<?w{(wY5k8YqttD?C?v|&zN}Z8LV&&4*j6A(_D;apIVwB_PPjMWC9ta<b(kNK@4TABo1Mps9@PS
h2apdnXT>-`H*BV=_`J|YAK;ex6iCNdo1GsDZzt67zHk6)6QZ?+KXqSU{ix+tch@EW&49I*EAqFQf>CcbsbScM8)Pe;lKtFI*Rb;
?KDIC8p}hN=}E>7_?hCQu|BU6v66t3h*RA>Um(rriR}9yb~B=DO2vIvM>zJ+bIasA1d`kd(1P+HW!K6@(pxzY6*kKcmi7JNdG`e@
69)SndI#|Pa^lNFfcqWM6_-jb4CaE4tKC<iWwCLoqg#xjHmyC`1>aM>(j!E>%2yV`s2zk?cQ)F&eZ7)s=A_n_PT8Oo`ArUmyd4H{
)}wnSIAFj!ei+(Rw9&b9jrtRUbw~97kdbQj3N%CK8i>B&RZUZJG1-W9FrR}(@9J~m#7_)C0jcD(8xvJ3fK%rcAn}>;w}#fBu7Sk$
!-||^%~ISU&`spR9LCl9jCT!@Le%V<qX=^zUF%QKls?1CG|x;8LTa<TO%dDPSblqaJw^osKJdj=l`BoV3TjV+BPYgY`;J^6@$f55
pi-Fy6a8cB^Tl!E(1Go?{?pEP56Oj3y-#R)JvTsCJ!vN6O((CNLcA#KTO=o|E4b|OiJWYD2i!Wi4MGx}i(TLM7-pW`!9+oxume&`
90e;sgWDr@4%4WwMAQsZ**y6CC6qT7ee}kZ0Y!po?-kRMhR~~M=4b`gzqf^*vO!#bX<7_Iyim&Jq$w(sKdKa-&2a@qro667FuV_)
Wk=X<p|!RfGEcq|D!#FB0C>wgX@j^Hho%Zg03uPjh9V_D9wYD#Q)Ktwwt1Vd*HK&<_)r$c2G*!QfOyEZv0Rlai-^o2Q-JaA5(_gq
sDC>Dx@utihEdHnjng<Ly(&*sya*=%r)29dQh0c@eVfIaKvS7iK~o-+Ax0da*Y!MoXZVl<)5m}Xr%ne_R^4I7$b9F7o1tyvOhujt
U&SQpt^16bizb-7!NuSVi#b(EQD`??yPqdL0Kyk`!L1B+(jXe2xxh;(H&T#w`TyoKBIIz;f-gwgA8k9%46U56Yy9cd7dO;ZwFQaW
dXQ!ML27nbHRY#Ym$Bb$W?wnefSUn%OJ@H$U7P)A5?Y>VXuS)FABW{v&eiE9owciXq?I_w-22if#T3R_-&7{=p#<WETjUNYeOQJR
xVg0QbcF2nhHrfElMyMH#%?+QHgIx(<_z_9W<XNy!i$}Ns7ICwTTvJdE}az5fq8UDZ?h9m+)_^AiB~Ke(l(^ou$z&I`Au^HpR2Y_
TOTDZ5B!J}6^I6OY052aKFh7FBFtAAeHM!=Qy9sU8Xi)1no>TEzZ<_Fl)Rwyj)WuUQJ9gknQQU|i>5vGfHk{hw(_4byrIogj&hF$
LFbtIXA5@gk3plH%GjF!q}hAh4+jYg6r9z0=7F|e{pDi6L8TI~mBmK8?5T91z$!i>7BXv)EsND;H(B#po_V~P8;|(zFFvbLGO#Up
9NI=q71a?}STb4<8o%!L1b07ua&-;-WP6=oe3|6lja~bOp7Z^PL94n80`|rLR@*)WEktiycMO*z7pRKj88)hMPH~9X<_4RceG&U8
ZNt~#YuUVaDOUxzl83-6EiOR_D3(4P4{|9$e4cAnht*fkZ4goLU7){+wFRqi_Dngdp`H(@bkkEG{-Nkk7Eq!z@L!u8R+Run5(TL9
l3{^kG=2WNRuKn8G!a9wJrtqu{MCG^qqokVf-37V4KZ&t{GfxFk~uPGW@EG&N7-$j(;lGao>7BMC`K^S-7>M-(^yPS!MbaHn<Y!|
2n33D=W8N$F{q9lqrlzH5GD1cErsM*%Ob^%9mvP^bCu~5au9fd$`*rr_ezbXohsKcEzc6H@~n4rKjRI_SS2}X2u~}m8FYB*kw}lA
&6)>K)Otw#{OvJFaUCclaY+JaD!U~P&)<!zQ0q>)&_^y$X+oK2_w-?p0IuIr3`ZYp{Al1$nJk*Mf@7C_J}WNxQ<;wN-<i4Lv(z4r
$=r@=`&z2>Zf5>2-oUh=E0#J}ry)^;{0XCNvpdSdM2Dp@p_Pdo4}7!x7p{kPy(NK)5fPItm`KoHGw%Jdo+uuo0sEz{b<(v<Zi9(;
N>nxuvxfs31!0QC;7||$)M?-qB$%W<qq%<vBXH44PTgM&?#~mOdpACb8l2hR?N$eGB7+nKj~cLkDYx>tzyrFsI*ecsMQ9Hw*!z!Q
HB#M2UD$r)$<;RT7>l%sy^x-ryD^aaqc#?pm0y-YRVu@qb`Aie=-f_=>x$~!F0X?3dcPiJsz2&m&7{p}O%&AmyT3hmrmDOE62A^1
K%D&C)NbfJ5)>_z^L{0Tbew;wlZ6NC*Vb96I2H5<9)(u1y?`wV>_MFyELkL?xrjb^vu9iKub)uz&2f3CW=jIY<xfQF$)n7^OYP`S
H7OLDBr>^t0esE7TM1Ewm1YR3#*}X&*4<@MahbTXyMlPx0UW=Lss0rPGg%DMe8y91NqQV*7KsC<XuP(0JyvccHTRW1tv%5JQNfi1
+m?hoBol+A)=^TwzQB8YkP{p1ncQ$CBdRJU{{rX4A3<Q-R!&6EAm|Z^rh%Bm{Y6<s^WM^p)jg7J$S#Wm=KH4b2U9@1q%*D`@5Qb0
Q8DIl@=*#7dcfaLfyP!)gupsKU{P;8k%cb}!52S=lPxRqiv#9SwdBSbHN2pO6S?y)YX&cEgN58d@?#4e2LlYg?+)&TkE@jklvRG@
Y9xF8HPTbSh{MSc_l`%JByqO4uLIQuGwKdj<}nR&70kD`EFRIST;SZ-%w$0%X4j4%{dMZemh@5)ipUmh3eftgStmnxAyl0wWK3oH
JxMqCsOi<}(T_p|Fo-4TEQt&xRM>}>e)0_LbY}hQf}umamy^s0HZqqj-!X;LkXwE?>Sq2X&p<0lRz+y#XZN4uZ&7aUvw$*vm_NGE
;4oo1X`h4lhsTR^-LB2qtumOKx@>rU7$kA`{it*6(9%ydmEJIZmWJ$w;tVIf=V4q_Hr%e@o1kpcH%8(uFDMcx!xRE)wfn4<u6#(B
$uc&*U9^$K_e*~@`(5@lf*_i^=Tih%^gcxCx%#)8jnyS5F!Rs!jIyuYrezOb9r(E}A?~KlG48F(nfb_AiElZE4Mpa)fK44u$o6ZJ
EmaYNk&M9-+Wtkjn`0+Q@4jn+vZzlXwW<beSx;25{11N|SoC2!iv|;>JxBjlsD(+t)h*Lmq`xKR4!P<{X<6-Grg;jVG47=!1rk*`
J}Vvv5(2(TUM_|JQjLi&T2>FXKide?eZFWwexdC8Czk~RES>i%L98OUXMZ-mkRT^<0xW4aKVNqL8(R!~7kMYITcM8g$KfCf0u*^z
I)bTmGyagvE)?fsr;>-~_EWQ%!~~pz+g-FpHToDe>xGs4SpnpdzSc~57Nlc$i^-oYh>^6;sY#Z#=>aT9`n|LTqU@DDX&q*9XF0;g
Sn4*Y;O>~&zw1#Hyo^#e#Gd{B%8bSi-n3yKpsr8i{IB>tm)6ew^!D$Sbv-OJzn3T<HPtnqd~7!R`_+Lf|37f!5Il$I3*y$Yc<Bj;
7PURGuw9rjE|T=13)_CHqUNx?9F~^<F^Eb$H1u);BGy7>`)@Jy!~wc$EU*`J3<er;9zXFaW?3N0hiGLERR1}i<*BzvV%3{sJi-L?
CGYf*aO|Yv^m{3SdC&XcHr)Z?y_OU;c`c117+Zc-H9ff!cFvT_LH<8EecA9m-D^c2Ud<H;>|fJ$5jn0lAV85+e)2H{hDD(uq@{1Q
E0T|@n1W0B4NAy`7o;WO*;;ddY>yc@RVGjOSd<}Sz=BC`6(RTM&Pj}YEHoX9qAI+kSb0U=(R1lmTXEc{!~7i6D<8C}<CfIb?u{Oi
q{Usqjcsh*U0V-V;#%+!Y7r_EtzA$`Vpq>qRSq%2!3fv2YJKh|wex~YGMze(W7ogf;0n;K8ROR1yzQz}A-5xKJ6;T0d=XdYNFP)b
_bKe`is>Zsz%Ji|Mne(z&||(lB#1?6KR8p#e|y}dN{ChkN<E`AmMhllHY@+RFju3j8@U|C_jA68?-RsN+uBF193qJ*kp6bVE39Kf
BYIFCyvU_+&3eWQ;0MdE3?vOZvmn%_<Z?52+8}dB$q6Yz!lp?X3-dwee1wN)X}pS5nwMIgpCLVlVyo?_|2<7r!H1Dj?7TLv|GGSh
xRt8zX^1t1Oweh;kWszkCTB=82|>&1GT{Oj3-KHC>sE6(KtI<!&g~SLt!fGiQJ%S{nHox$BJb04t=`e?&%M_NLjo}T1f~x?+MSXF
&&8+s`|tq$ydNiUC`z#rV^8ZXE#;6418N0oo~<siRmKZS80(X)rfj2ghwn%!!zfR@?ljCAoh?!xs!bE^$zPxeiu95zhnAF-X8=gX
k?uj*UHlzhrqCNFCc%=3AaMS2D@wy3x|ZG3T)efy)<!fEEU^+fH~7k@6{{B8Kztv)`!*ICD!Yy9?8NZ$^iC_LbB>?3yu-)Vza_Yr
Ua0yf&!3WkGx?NgtyaFq09FnOqooO`)bh_F7LA4U0UB|{NMv{L5)<SzvvtpU*gvn{!NgX}Myf&|3Zu;<D6ec(qOeH+ac0&Xs&D@n
Uie-H`=f5d4%IR6l&FU`DS%zDR~#iIB*<gKF7PZo_s_!MC7q-jX(LvZW_AMGl8|6Z!-D#3mDdS%46E$0+<Pa*Hns8U%}k~rN3xD0
LMeFxhb<Yqp&2y5oJ*{5cQH6$6F<JxSvQYQkAr1FJD1<Hk0SQeRvEZL2tM9_l4Pi*6M={#v2rNZ(zEWe9Z2;{TG;5;(jU(sOI1~m
;Jh)$F&G7>Rg?)yMqM{RkFVJlcryU4XTSUEy!bC{D0~jsCH<`Y{d|;9k$PJ=B#5$tVDy14GG+rH-72Bxd;lBQZJ?!jzVDh7PbgpV
Yca@F(6SMANakeOmM-bZ4ROa0NE0^cy3;G!Ze=Cu&vU|e5-7i+*8qo(BX?O2Zd?kW#{u$VC*@F3hQwgu$}w#d1uFE(NR{B0Rzls`
VHXIvGeNPn0U;q)&VBga#ZG<%2$4Hl0tC(DD@{#Ca4RCd)#y-6&#_e{rM%r*8k;eg&}ZO<JMm1w{H|_aBQP+r{;QRL-CG;j^9q=j
G1f(greQg!YF%%|XUt@WHDolrbWlqZ;Nvd@0=&+Zs$_`qfxbN>?#pu|Oy!~9;Za__mstBgr3m&+caD7iJ)<2hG-k5SQ#|&Egs+De
wIV2h7w;-9)H@7A0D(X=zt*qCO@5kTA(&#XdBW8%+F9TrwRh4yXy188N2(bp`S8B@M{zvY;ILSEYok@ErE>Gobjs&9DIjm7Et6JE
q=$IUw+e>C8wbJa+lK2-Rv2s?nlM{M;eD1>2B`S%-dlO0X>gU3Y4JmPGEpA(hZlME&orfV3$huUjN?^rB?i^8ldIsZT#da?<Pew#
2s`2a4M)F=9$s@1+n)o(1h}lH^5lp7K4ng8N2TnJ54MnX)Ne;%6W70`(x7m>Cucojr`A2O%91~_la5JBL(1+=nSfNrC^Xd5N#z@f
Hy-7}T#>Ika}~YCzl(M>Pczlx+YqaaU$w%FPFYs-*{)MiCJVPfxcMA6H6~u;Gxq3W?Xd5Hfl26Xy?kTPPz|NsXT(#sT?PRa-?>Ij
@{)xU)frY{@2PcaqU`6?)0=kUjF>x2eN!_PdW$=apVE#U`66W-8$q#5n_5iA1rY}eWMvj0oJaqPyO-gJ{0Jy`?v#p&?Z^vDL&mzz
teuds`+$Jc<JqVBf~fBYyR&IVHxWRxGx4?gB@RQ9M%*ErDJX-dhTF*rkmaz_ChXG(TxxnXr<Q$wdt>b7-9@hv#_hvb9Y*T%Y(1(s
0raKAZNpe?n$%)OTaFsVRb%0^Lva9T2eg6>4P7Q(CZf&a&c|;3<xgL!k@+LNWGk+oR4?~hv5I4f_+ShYFMDlAmvFV6xlN&8x#EqU
s&I`x;nQ2$Kcex*MeGb$jW?X&n!3cZOvVy>a&|P3{6lOc??~G(jhoDI54q~R5xb(}ebIHk=!qqAhdB|gPUX%89%%o(TfiFDnTc8F
!<gya`ndAl9Uf@ngl3#Z!9uR2D<8{)oj+XmtSXGDFB-DCks0Nmk?yQoRcoPcLAdwsMH7cCn*RrlOor=}H82HIw_6K>!QX0=&~Xi;
2^nd7%ss+EQ7dh{A8=kMLd(lR&8q_FLBmk^^A}sWi!a}CcOwV&S&ATot_HLw;>KU7h+XT6)$J0Fe8K8mwEyL7uZYA(po%aYvAOfK
wWd*ShV)CsMvJk=xjSLJUce{kCfN8;eiH^3{2I&XsfL?M{5ice4sJBhNXN;2JQ?tvOI+W-prKMFY9)m&t{89D4^jQE;z7Pqw+>&B
WfmZU7ksjUL`38UJXm8DyO#O!3eL&i-4OM%`POw;l^}|&^j!TAU$Qm9!~EgaOH4y(q`Jk+F-SGcPq8wldBp=j_QECSD^s_Rp$j$r
jf`;4rojk)_7%z+hlqGY;|)czgT%O-an2~z^an^(CJcIv`n@`$Njtu-G2LtjV?m*yp+0gE-zG2>((OwZz-o)&wGy5mp+Tm@OQ-84
c>~D-Q$vqSTm36XlBRA(zake)*8Ij~`ue^WiEr!*?FS$UK6rOWnsJ~XTL;<i|KDtJbVjI59Sii#l9mOQS$T{CiHt@;svsK_sJUrh
@R$@FZ%|eE6dNUz$o64vVmPO;Y4brjdyuZ(xUpPLLs)z?QMuH}(Al$4Nq`y^?!ynv*)Irg;$M)w0{QCEkxGH7X_%z+poQU5-6u6=
Xo+NNh?wzRwC&fR^<HYtz>_y`*EeU4T@TdCF#E{UUpuz*eEdbXg;Pyk1->ad$43kC!7PNB9Q7$AS0l#;55a|0M7&r?+QlH6*jG0~
!1wmM%ZN)iEb&~l%-#VBVzcr$15Y~b6d*t&&C7aiX<bosichgG7^KxeSw_FXAkk3(;5e0(nZ+oYYRCqb)IisCR#LoSP{h24>fvX`
1MvP#&&-GY-kWZUHhZI^<PBuk9>R2aW&A}9#bgWM+k3T*SILgdF!b=UXWO>fGb?qHw>GAI5abE*4{NR8Rm!T&uPhb8U{MN!{8QnY
aJRW$hL$?;(sfPv`yb8pp3QLtH-H}`MGwN^79Ky<g=|aw@W&+^|Hd!-!2O>L{UvaSc6Yvn6nw)UP6tiH*dH!1<q{-33ak>?|G`zj
V|efO14@hy5Z;P3Z&<pJRQy``sZx>QZZtBG;aFYo0AZgKe0LtAEhztJT5x!K+)fNz@%LPUcxem}5*s?0)5|Gkjx(?`gK&t@<x?=H
WRP^%1KapREC`HZsvW>>-`kdLijv$~y8~|@1Ua4_mouwgv^MOiy*f|U<y|-=@I=PD)|qx5ov38PVYW+$ESUMiNx-vyV5bUd*;(qh
PF@Kkqh=)GDnt-*608VFo#Rjj%yj))G6vv8KbfO%gGnZa=+8OdI}cgO3TTl%A#{(UwsdBWm;Ud9L5JHgA+*{6{vS?&-Es_hjN9to
O3S(Qg<=d5BW}>vF;Sq(x_tE39rm3Rx3dZT(UexBra(eN2R?e^Gcg&XYG9=NuD$d-GUsCd6kAPNh=U@e?w7kd2C2>nT=a5H=aRK5
S@!s6P3(rCVEJ>%?!{H@9$PKZqaeT8j_D@g%|G$C88dhZ3Tmlod-;v|rcgShX#AfqlZ<Tj6hR#zO)t407zb|YU>Y?gFQva(XEzUn
-xH#qUXWt2gE_4&$c$&8FF)`@jgkkcewRupPlwHQ((FlfRu$7j#x_Y~=MS$?>6hTTqNqx<ij5ze5Wr+@Sm(FYhJ&0l2HzE}v%u+m
E8v+r=t|QWAN=g`3LUbOueo<$SksAUtD|>k&Mg!+ckIr&pIM1n+fbmDC+kqdcQ#QAL|0EIR$9^_TwVOlr=&^_65Sr-I|duAgf4f}
A21&`4%UZz{y<kRNzY}z8HtQHPcb;uxr>R=cSHzIZvE5V9t;-S{G|J`8K!_vIuFbS;VYU)9h^&XQ8iAyjE)GtVa+Gb8A&n6lwMwP
oA(DX7LuitFoS+q!o<iTJkZ?jB-zfeVNLmE`y5v@_hUyMG<oi2{kW47$Eot8r1UhTzR>i*zz}mLeZ^BVms%{wN`%rpZUQenZ`(;e
l^B!=NHb~!4L9iTCm2sCIBm$V=a&on@c})k`6m}PDyyifEa{x*4%h)J!_pm@aW-DaxR$n}zjC8L0%O@Ie|*4>bfQ8p^wRulEX~A?
94!I=Lpj^%rl<7qG1D`qamSPW?vHx>RkIYq)5Ev~DK^pfS$esJx<LOLTy*GY>;oEh(<G7H-MOujbPfbTvTE4&f;ZT*dyVL9$B6x!
lkSY+&<`U-OL({A8r6~FXhnDyfpya`B70bL2S9-Ta-LIJ0TkWHkbgT7ZK1dZ4hPrwGo+`LhXScw+{Z|&ZVQ2?++DX$v`q}bjhDLx
;3BmD>%>^7Dn`~g62k~q=-Dq7#&R}$yH1=kO5L<8dkI~L{XftGu57Pbr3t-V!0O4`&yg2~E%&5a@x-3tz$E&v+EZMTX`6Up;IhUZ
!tgUhdE$WqFJ6~x{T21@>lM@SOnVuy>L>|yD}4E&-PE=DZ}-Hh&jdNqCiYbhu;$Crj9}hc=j4*$j=vGjIVK>174X@yQ}eb?(f)MH
=^6=X8|rTB|7>8Z&xRTw+4);Nf!>x+>Olw`Mz97kSr23id*_`Ms&_}r>)xDPoZ*j#wZeafOC)>0kMyj)l!4oXbTgzI@)chu#I;5D
>HCj+#VDvo2lO~V&I}CEA0_&Ya|RJ7KZW48keL4x-L=x(M)2ij`*{reL^Cylp#y^xLZS3B>J__LI~0ED)ItG-;0uq?GT2Xvr2f2+
won%i!Ij6F1TNk7_UK>h1Lexa?1cH%ozy;?FJF`%`t%rgyO$(%6a1|7D~cS`+JVI9H?o<%$Sq}J0a}lCmn#QjMwgLCD3f_c9Cl;L
3hi8-O|*0<+48@x@~tXKZ~LVZU|kgZX7BZ{^}2R4K&kSkp}vnz6N;2+a}Lb}i$f%VD`h~zjI;+h)YWVE8lA;4x`%M__Ga2csgq&i
l(b|x*-gD6tb`VnpmmXo%oJ`rIV`A7J`PaPNLBxrw1}XDAH@+f5F}BW6^UkT0alrkw!HTgdDI^0!}sAU;aD$(dL=K)ufi$KQ`3iM
zMu?8!$}lRQbNvgNdP!Q<HE-F*-A`q!+6>iIpx#5P|QPLoE0ab;>DmA;<d5*kz^IB?lw|2du#Ip<ld6(`gDR1)E!vF7vA-JrrJc@
xF6C)>-KaMxz50QI{`NWB=!f#GBW^$H#L@9^v9Kr36uTbNoHi^Xh3E)v&n^ePc-~QUprQRq_cb*ta|BHB>O);LF`QIjT{@g<INxk
KX#bND-?ROPa<J5_F9_QJLYXV6QYGlfcO^6S+0pX?Qpmo><Se3?@yZrT`!)O`Ap=}Aq*&3ePOoK&K_Wys)H*XQ%@`haI=bf#1u9Z
`OBgxa;WiGgl>hlcXA*<L{r$`5{Swivxz+evrl5o=sEi{z#gpDntD2^JFs4DXrYp!4|VcyOD9@fk==%aS9i%{`o0wmoSe61>58Si
rM-1i#%VB0df^W9%^=ZrPvAPS4Kknhro#Shp86=X9e22T+>@Dp6Z*BQ_0YTfpprSY=;h$Vs_H`9Cbq4xuNnq^?%NNKFYH+rdi~Lw
v+El7;sQ@c)a1~T3J9qkq7zte1P{b<6@6pm)QF@2t_%PbXjMB?*YZfezG29$p0CN@uXNC$U?aRheme3iWp{@dKTOQ04~mi-W<<Gp
SC(Tu#B0zVPFjOXm<C$LfV2lV>dsV1YyBoNk+cma_ja)1j2ZM~B!|IuM4M2ky2ti(mwbfB3VKx(f+uv995fXj2H|k>b*zsaDGn{9
dGYRWZASBzyW9qkALC`6%#OSTZQ7d74C1fZN062Ui!17;4Ei%p0TX%HbbsuD<x#4{$gQH|*$uqM#BxpC4v?N}D!0xY^@C07foebd
r)_Rb8}Ss?dY6zE3mA&;hIY^-8QJ`1H3-XnS^q<e{Y!5KdT?qtWsLpwof>)Rzy5(m#yD9F`)s=Li_2j(b2B1v1QjMy9UH_iSJ?BC
cA#c>T^D}{cx~iJR39wXR>x0>_KIGq*3AucD_dm2Lr_d^_AnN;CswgRDbu+tc+jegeunE9nx9>_dhf@?fTX{`p-$V%Beci#-z@ww
rNj6Ki*^!@Gq#awW{nbs|36ll8z2AVH~)m);Iy+*weI2|u8Ti}d!(*vR6*R!<GB3c7vXJs-zcq&%w9gKgV+=)5fT(0)um{PK`1-4
Co$%51JCQGnesf)tmRHFt&pExX4_V(%BE!<kW-SZ3WE2`S@{hyCDQ+R30^tG(Di&m*`KIRUJ@|e@!Fb&fs}S|!izVeN98ELZxX;w
3d;Oor#v{R{pgAa^4j+BNjPN&%|H}ddFPpVlSUYW<1{yFQ0~_xBK6|@qxGIEGIrd-f5`d!Z1`EAd(s>~LG>>xZCG>E^Wh^+C6@$t
C4UpZxVTVP+5<XQ#O3?8PX7Y|??w5jJlwN5t5=AtR_dx^H&<WXmENemIM1cx*GqQJ&zWqj4o<C0pQ;JQ+C&Rh>2l1tN@K~j9&+Il
Rm~L6)N7t@CVfMLyrFWP&*Pc9=-2z}5>6fA!*ulBBZ}lyks<n$;(FzKajz;>uxJ>+_g3J0eftPv0~jG-IbmeL!<7#dF59P!TGL;-
IGy$;lqI+u#>pyF45&7#w)2hJevaw-84YzLMlzbyZAdI~E-sx7$y9vi=QYW$PJxiNCD4+p6soMbvf13(q&|+2AYYW`&4Io0bv$R;
m<eE)$sjiX1w*tQKfHr8i?#d6RWVxFO&n@?F6TG2W10wmA}G(2S51u#CsavYtD(Ix2Mv~{Z!!r4C527U=ljz4qYY`_H3%m&a&BP_
*dJkskt^SA!~|l<@szX!6A*{qbc2_(T$S#DNy`#m6}}bk`Nr(G7(%1SP61;*NjiRZnGN_pX_O;s4C{@MeWkVJb{EhE!bZ_EMm$K`
d-w8(V9>F-J!AeW(7~EMz$-MO-iQDI6aarq6B*|%00D%!0`;E>2bRF_vBYQl0ssI200dcD
"""
RAW_SIZE=151541
RAW_SHA='216c04b45a65fdf0791ea06cabae5edcdf6c8f9a833ffc8c0c648b8141b71dfb'
def main():
 raw=lzma.decompress(base64.b85decode(''.join(DATA.split())))
 assert len(raw)==RAW_SIZE and hashlib.sha256(raw).hexdigest()==RAW_SHA
 files=json.loads(raw);manifest=json.loads(files['FILES_SHA256.json'])
 out=Path(sys.argv[1] if len(sys.argv)>1 else 'W49_SOURCE');out.mkdir(parents=True,exist_ok=True)
 for name,text in sorted(files.items()):
  assert Path(name).name==name and name not in ('.','..')
  b=text.encode('utf-8')
  if name in manifest:
   r=manifest[name];assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256']
  (out/name).write_bytes(b)
 print('W49_SOURCE_RECOVERY_PASS',len(files),len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__':main()
```
