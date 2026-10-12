# minimum-0229

AI research report · 2026-09-24 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# HEPTAGON_TRIANGLE_CAPPED_RECIPROCAL_2P1Q_CYLINDER_V1

## 1. New result and exact scope

**An actual eleven-parameter, uniformly refilled heptagon–triangle cylinder is now excluded from the joint S1/U1 packet**

`primal 2→8; primal 4→3; polar 8→6`, all three arrows weakly nonnegative.

The exclusion uses **one physical metric and its actual inverse**, together with the accepted joint S1/U1 covariance caps. It is a continuous geometry result, not a fixed-point separation or a formal spectral control. Its main parallel slice has `1/2 ≤ rho ≤ 7`; five of the six old corner-tenth inequalities fail throughout. Two independent horizontal projective parameters produce genuinely nonparallel, uniformly refilled bodies.

More precisely, the theorem excludes this packet for every reciprocal metric satisfying the **closed** caps, whether or not that metric has S1/U1. The joint S1/U1 statement follows because every such physical candidate must satisfy the stricter accepted caps. Incidental physical weak contacts do not invalidate the exclusion. **It does not exclude U1 alone, every orientation on this cylinder, an entire combinatorial type, or proper110.** No global minimum bound or canonical registry count changes.

The result is genuinely joint at the packet level: at an exact body in this cylinder, the two primal signs and the polar sign are separately feasible under strictly capped independent metrics lying inside the recorded cofactor blind cone. Conversely, an explicit uncapped **same-inverse** metric realizes all three signs, both on a parallel body and on a newly refilled nonparallel body. Thus neither a one-sided packet obstruction nor an all-SPD packet claim describes the result.

The source authority is literal parent `minimum-0226`, SHA-256 `cf8ddaa5aae98ac90b2315d8789415d1d8766915cfed139d27a69ac1201a3539`, and the supplied two-part `RECIPROCAL_ONE_CURVE_HULL_V1`. The parent supplies the actual chart and true incidence; the new recovery below has no computational dependency on its implementation. No necessary exact input is missing. The supplied exclusions and branch residual are recorded explicitly. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

## 2. The complete actual shape cylinder

Use the parent's labels and `theta=(b,c,p,q,a,d,u,v)`. All the following intervals are **closed and independent**:

| Parameter | Interval |
|---|---|
| b | [7/50, 4/25] |
| c | [69/100, 71/100] |
| p | [79/100, 81/100] |
| q | [3/40, 17/200] |
| a | [19/100, 21/100] |
| d | [39/100, 41/100] |
| u | [19/400, 21/400] |
| v | [3/80, 17/400] |
| rho | [1/2, 7] |
| s, t | independently [-1/200, 1/200] |

First construct

```
Y0=(b,0,0),       Y1=(c,0,0),
Y2=(1-p,p,0),     Y3=(q,1-q,0),
Y4=(0,d,0),       Y5=(0,a,0),       Y6=(u,v,0),
Y7=(0,0,1),       Y8=(rho,0,1),     Y9=(0,rho,1).
```

Then define the **actual uniformly filled solid**

`K=conv{Zi},  Zi=Yi/(1+s Yi_x+t Yi_y)`.

Integrate its true uniform volume centroid `g` and covariance `C`, and use `Xi=Zi-g`. In particular, do not transport the old centroid through the projectivity. The base remains `z=0`, while the top becomes `s x+t y+z=1`; these planes are nonparallel whenever `(s,t)≠(0,0)`.

The whole cylinder is inside the strict chart. For example,

`u_max/b_min + v_max/a_min = 91/152 < 1`,

and `p_max+q_max=179/200<1`. Every projective denominator is at least `193/200`, because every raw point has `x+y≤7`.

The maximal outward cycles, in order F0 through F8, are

```
(6,5,4,3,2,1,0), (8,7,0,1), (7,6,0),
(1,2,8), (9,8,2,3), (9,3,4),
(4,5,7,9), (6,7,5), (7,8,9).
```

The 17 true edges are

```
01,06,07,12,18,23,28,34,39,45,49,56,57,67,78,79,89.
```

Thus all three packet arrows are genuine: `28` and `34` are primal edges, and F8/F6 meet at `79`. No integration diagonal or projected eight-corner surrogate is used.

For clarity about new coverage, `p≥79/100`, `1-c≥29/100`, and `1-d≥59/100`. The whole cylinder is outside the corner-tenth sector and outside the literal old fixed-slope relation `c=1-p`. Its `rho=7` boundary overlaps the earlier expansion theorem and is not counted as new; `rho<7` is the substantive residual range. The theorem includes all affine images with their carried metric/inverse and actual moments. It does not assert that no other historical certificate could overlap a portion of this cylinder. :contentReference[oaicite:2]{index=2}

### Actual moment reconstruction

The complete verifier integrates a genuine apex fan. For a tetrahedron with vertices `x0,x1,x2,x3`, positive volume `w`, and `h=x0+x1+x2+x3`, its contributions are

```
volume:       w
first moment: w h/4
second moment:w [h h^T + sum_i xi xi^T]/20.
```

Summing gives `V,J,T2`; then `g=J/V` and `C=T2/V-g g^T`. These formulas are applied **after** each projective refill. Two different true apex fans, the full primal and polar hulls, all support incidences, and complete same-inverse mechanics are independently compared on the four exact controls below.

The two poles needed by the certificate have particularly simple actual-centroid formulas:

```
q6=(-1/g_x,0,0),
q8=(s,t,1)/(1-(s,t,1)·g).
```

No polar volume centroid is introduced.

## 3. Quantitative common-inverse theorem

Write

```
Dij = Xi^T M(Xj-Xi),
Efg = qf^T N(qg-qf),             N=M^-1,
tau_M=tr(CM),                   tau_N=tr(C^-1 N).
```

Let the ordered eigenvalues of `C^(1/2) M C^(1/2)` be `h1≥h2≥h3>0`. The theorem assumes

```
h1/h2 ≤ Pcap = 7024915/1000000,
h2/h3 ≤ Qcap = 6832329/1000000.
```

These are used only as a joint S1/U1 necessary restriction, never as an U1-only fact. The supplied finite-height statement and exact reciprocal hull retain this distinction. :contentReference[oaicite:3]{index=3} :contentReference[oaicite:4]{index=4}

There are explicitly specified, piecewise-linear nonnegative weights `lambda(rho),mu(rho)` such that throughout the entire eleven-parameter cylinder,

**`-(D28+lambda(rho) D43)/tau_M - mu(rho) E86/tau_N > 1/8`.**

Their endpoint values are as follows; both numeric columns are **integers divided by 1000**, with linear interpolation between consecutive rows:

| rho | 1000 lambda | 1000 mu |
|---|---:|---:|
| 1/2 | 1281 | 32876 |
| 3/4 | 1512 | 35869 |
| 1 | 1568 | 31657 |
| 3/2 | 2474 | 31986 |
| 2 | 2474 | 25379 |
| 3 | 1993 | 23371 |
| 4 | 1880 | 30359 |
| 5 | 552 | 14781 |
| 7 | 0 | 14046 |

The zero weight at `rho=7` is intentional. The inequality still excludes all three weak signs there.

A useful stronger subcylinder is preserved: with exactly the same basal and projective intervals but `29/20≤rho≤31/20`, the **constant** weights

`lambda=1237/500, mu=15993/500`

give the same left side **greater than 1/3**. This is an additional verified continuous result, not merely the midpoint of the wide cylinder.

### Reflection

Interchanging x and y carries the theorem to the reflected cylinder

`theta'=(a,d,q,p,b,c,v,u), (s',t')=(t,s)`.

The corresponding excluded packet is **primal `3→9`, primal `1→2`, polar `8→1`**. The vertex permutation is `(0 5)(1 4)(2 3)(8 9)` and the facet permutation is `(1 6)(2 7)(3 5)`. This is exact relabelling, not a separately claimed registry increment.

## 4. Why the certificate retains reciprocity and the moving covariance

For the actual shape put

```
Q=-sym[X2(Z8-Z2)^T]-lambda sym[X4(Z3-Z4)^T],
R=-mu sym[q8(q6-q8)^T],
sym(uv^T)=(uv^T+vu^T)/2.
```

The normalized reciprocal pair is

```
A=C^(1/2) M C^(1/2)/tau_M,
B=C^(-1/2) N C^(-1/2)/tau_N.
```

The desired left side is precisely the associated linear pair functional. Both terms use the same actual C and the same inverse pair.

The supplied one-curve theorem reduces its minimum to the simultaneous orthogonal orbits with spectral parameter `xi∈[Qcap,Pcap]` and paired eigenvalue coefficients

```
a=(xi Qcap,Qcap,1)/Pxi,
b=(1,xi,xi Qcap)/Qxi,
Pxi=xi Qcap+Qcap+1,
Qxi=xi Qcap+xi+1.
```

This is the **entire asymmetric reciprocal hull**, not a single asymmetric corner approximation. Its three-effect dual and square-root-free covariance congruence are the accepted inputs. :contentReference[oaicite:5]{index=5}

### Reusable moving-covariance witness transport

For any constant real matrix H, not necessarily symmetric, define

`W(C)=(C H+H^T C)/2`.

Then exactly

`tr(C^-1 W(C))=tr(H)`.

Therefore the dual objective `tr(H)+z1+z2+z3` is independent of the changing covariance, while every dual slack still contains that changing C. Endpoint witnesses can be joined by linearly interpolating **H**, rather than freezing W or freezing C.

At each of the nine body-rho endpoints, the literal recovery table supplies a rational symmetric `W*`, two rational scalars `z1,z2`, and `z3=0`. Compute the endpoint's **actual** covariance `C*` at the central basal shape and zero projective parameters, and set `H=(C*)^-1 W*`. Interpolate H, z and the arrow weights linearly in body rho. All nine exact endpoint objectives are greater than `1/8`; hence their interpolated objective is greater than `1/8` as well. There is no interpolation of the actual body's centroid or covariance.

### Complete spectral and shape verification

Multiply the dual inequalities by `Pxi Qxi`. The three costs are

```
xi Qcap Qxi Q + Pxi C R C,
Qcap Qxi Q + xi Pxi C R C,
Qxi Q + xi Qcap Pxi C R C.
```

After rescaling the spectral interval to `[0,1]`, each is quadratic in xi. The verifier exactly reconstructs every degree-two Bernstein polynomial. If `d_h>0` is a Bernstein coefficient of `Pxi Qxi`, divide the corresponding cost coefficients by `d_h`, calling the resulting two scalar coefficients `alpha_ih,beta_ih`. The nine matrices that must be positive definite are

`alpha_ih Q + beta_ih C R C - W(C) - z_i C`,

for `i=1,2,3` and `h=0,1,2`.

The source proves these **throughout the actual eleven-dimensional cylinder** using order-two multivariate Taylor models with integer outward rounding at 100-bit precision. All eleven coordinates vary; the actual fan moments, projective denominators, volume divisions, centroid, covariance and both poles are evaluated within those models.

For reproducibility, a model represents a polynomial of total degree at most two on `[-1,1]^11`, plus a rigorously bounded remainder. Product terms of higher degree and every rational rounding error are bounded outward. For reciprocals, writing `f=c(1+u)` with a verified `|u|<1` uses `(1-u+u²)/c` and the exact geometric-series remainder bound `|u|³/(|c|(1-|u|))`. No floating-point arithmetic enters the proof.

At each candidate shape box, exact rational LDL gives a congruence which diagonalizes its centre matrices. Power-of-two row scaling places the centre diagonals in `[1,4)`. The interval/Taylor enclosures then prove strict symmetric diagonal dominance of all nine congruent matrices. Failed enclosures cause subdivision into **both** closed children; no feasibility pruning or discarded boundary is used.

Observed complete coverage:

```
8 initial body-rho strips;
196 tested binary-tree nodes;
102 accepted closed leaves;
918 positive-definite Bernstein coefficient matrix boxes;
2754 strictly positive diagonal-dominance guards.

Leaves per consecutive rho strip: 8,3,9,10,11,10,17,34.
Maximum depths:                 5,2,6,4,4,4,5,6.
```

The separate stronger subcylinder needs three leaves. Every leaf path, split coordinate, minimum guard, exact endpoint objective and guard-stream hash is regenerated in the report. Coverage follows from the actual two-child construction, and the verifier also checks the exact sum of leaf dyadic volumes and the full binary-tree node count.

For the stronger subcylinder its exact dual objective is

`10558806110837989144249554111 / 28474908771446185502590000000 > 1/3`.

Thus the numerical search is only a witness locator. The result itself is an exact continuous matrix-positivity proof at actual moving uniform moments.

## 5. A genuine actual capped independent pair in the cofactor blind cone

Use the central raw body

```
theta0=(3/20,7/10,4/5,2/25,1/5,2/5,1/20,1/25),
rho=3/2, s=t=0.
V=741/1000,
g=(365173/889200,7747/17784,1741/2964).
```

At this **same true centroid**, take the independent matrices

```
M = [[993011484,402529630,-777435114],
     [402529630,281613235,-289632959],
     [-777435114,-289632959,715201310]] / 10^8,

N = [[1502712,-2475081,-318174],
     [-2475081,7749678,782257],
     [-318174,782257,318384]] / 10^8.
```

Both are SPD. Exact packet values are

```
D28(M)=5666998109/3473437500000 >1/1000,
D43(M)=274496967779/555750000000000 >1/2500,
E86(N)=32450698630701/426718629778906250 >1/20000.
```

Each separately has both actual-gauge adjacent eigenvalue ratios **less than 683/100**, hence strictly below both required cap values. This is proved without numerical eigenvalues: the two exact cubic characteristic polynomials change sign in three disjoint rational intervals. The certified eigenvalue intervals are

```
CM:
(517/10000,518/10000),
(1215/10000,1217/10000),
(8266/10000,8269/10000).

C^-1 N:
(2775/100000,2778/100000),
(12494/100000,12499/100000),
(84724/100000,84731/100000).
```

For `T=tr(MN)` and `U=tr(MNMN)`,

```
(T²-2U)/T²
 =15660278987478985029544730983/
  951920632354549493802526814224
 >1/100,

(3U-T²)/T²
 =904939795392112538713892621275/
  1903841264709098987605053628448
 >0.
```

The positive first quantity places the pair inside the recorded aggregate/cofactor blind cone; the second confirms that it is not a scalar reciprocal pair. The supplied blind-cone theorem, rather than an asserted body construction from formal rows, is the relevant comparison. :contentReference[oaicite:6]{index=6}

**The independent pair has no physical census.** The verifier instead computes two distinct, legitimate physical inverse-pair controls on this same body:

| Physical metric | Strict S | Strict U | Strict H |
|---|---|---|---|
| M above, inverse M^-1 | {1,4,5,8} | {1,6,7,8,9} | {06,18,39,67,78,79,89} |
| N above inverted, inverse N | {1,4,5,6} | {3,5,7,8} | {18,34,39,49,67,78} |

They have strict counts **457** and **446**, respectively, both physical weak000 with all 68 primitives nonzero.

This establishes separate feasibility only for the displayed two-primal/one-polar packet, **not** complete independently feasible U1 and S1 trees. The result therefore does not claim that a full primal-only relaxation survives.

## 6. Genuine same-inverse controls: the cap is essential

On the same central body, put

```
beta=(2,21),
v=(beta-g_xy)/g_z,
G=[[100001,-10000],[-10000,1001]]/1000,
M_U=[[G,Gv],[v^T G,v^T Gv+1]],  N_U=M_U^-1.
```

These are small rational defining data for an exact physical metric. The packet is now **actually realized by one inverse pair**:

```
D28=7468863351139/645040500000 >11,
D43=19641/125000 >3/20,
E86=9598906022666688/950933932089697 >10.
```

Its complete census is

`S={1,4}, U={1,8,9}, H={18,49,89}`, strict **233**, weak000, all 68 primitives nonzero.

A second control uses the actual projective refill `s=1/200,t=-1/200`, with the same theta/rho and the same physical `M_U`. Its new volume, centroid, covariance and poles are integrated afresh. This **nonparallel** body again has strict233 with the same labelled sets, weak000, and the three inequalities `D28>11,D43>3/20,E86>10`.

For both bodies, an exact comparison of two generalized Rayleigh quotients proves

`condition(C^(1/2) M_U C^(1/2)) > 80`.

The implemented rational test is

`M_U[0,0]*(C^-1)[1,1] > 80*M_U[1,1]*(C^-1)[0,0]`.

Thus these controls lie outside the joint covariance-conditioned region. They establish that the selected packet is not intrinsically incompatible with actual homogeneous geometry or reciprocity. They do **not** establish U1, S1, or proper110. All four physical controls together contribute **272 verified nonzero true-edge primitives**.

## 7. Legitimate selected-tree coverage, without a registry claim

A complete independent graph enumeration gives 4879 unrooted primal spanning trees, matching an exact Laplacian cofactor. Among all rooted complementary primal/dual tree pairs, **13159 raw labelled pairs contain the forbidden packet**. These include 16 directed primal Hamiltonian paths with 65 permitted dual-root choices.

One explicit complementary extension has `U=9,S=6` and primal Hamiltonian path

`6→0→1→2→8→7→5→4→3→9`.

Its complete parent arrays are

```
primal, indexed 0..9:
(1,2,8,9,3,4,0,5,7,9)

dual, indexed 0..8:
(4,2,7,1,8,6,6,0,6).
```

Here the selected dual root F6 is not a leaf. This is a real complementary **incidence** extension, not a claim that its full mechanical inequalities are feasible. The new certificate already contradicts its three displayed arrows throughout the stated capped cylinder.

The entire 10-by-9 count table and all 16 Hamiltonian paths regenerate from the source. **13159 is not a canonical orbit count or a newly closed registry delta.** Some selected pairs may overlap earlier abstract or geometric closures; no unavailable catalogue mapping has been inferred.

## 8. What was tried, what is proved, and the continuation

I searched actual residual chart geometries for small primal/polar packets whose separately feasible metrics were incompatible with reciprocal coupling. After locating this two-primal/one-polar packet, I built square-root-free reciprocal-hull dual witnesses at nine body-rho endpoints. Directly freezing covariance was avoided: the transport `W(C)=sym(CH)` made the dual objective independent of the actual moving C, and enabled interpolation over the full rho range. The exact outward-rounded shape verification then certified the independent basal/projective variations, rather than reporting an endpoint grid as coverage.

The independent capped control and the uncapped common-inverse controls were retained to distinguish the mechanism's boundaries. Numerical witness search is not used as evidence of infeasibility; every affirmative geometric, arithmetic and census claim above is reconstructed by the complete standard-library verifier.

The surviving task is now sharply defined: force this packet, its reflection, or a covering collection of analogous genuine packets from the remaining common-inverse orientations. The top facet has three possible exits, so varying its actual exit while retaining outside-facet primal obligations is a concrete next step. The moving-covariance witness transport can also be reused to widen these cells or treat other nonparallel regions without freezing the COM.

No whole heptagon–triangle S1/U1 exclusion, actual U1/S1 candidate, weak110 candidate or attaining construction is claimed. The accepted interval remains **34≤C_min≤622**; the lower prohibition and an attaining example remain separate. :contentReference[oaicite:7]{index=7}

## 9. Complete recovery and observed verification

The capsule below contains the **entire** deterministic 22016-byte exact verifier, including all nine complete rational endpoint witness records, the stronger narrow witness, all actual moment and hull routines, 100-bit Taylor arithmetic, adaptive closed covers, the four physical controls, and the complete selected-tree census. It imports no parent source, saved report, numerical optimizer or external dataset.

Exact dependency: **Python ≥3.11, standard library only, assertions enabled**. Observed execution used **CPython 3.13.5**. All positive findings are reproduced from the literal inputs. Exploratory numerical optimization is not a runtime or proof dependency.

Save the full fenced capsule as `recover_heptagon.py`, UTF-8/LF with its final newline. Run

```
python -B -S recover_heptagon.py fresh_heptagon
```

It reconstructs the complete readable source, runs build and check, compares their stdout and verifies the report hash. To reconstruct without executing the proof, append `--extract-only`. The equivalent direct commands after extraction are

```
python -B -S heptagon_reciprocal.py build .
python -B -S heptagon_reciprocal.py check .
```

Observed exact source build/check and a fresh source-only directory build/check agreed byte-for-byte. The capsule was separately decoded and its recovered source matched exactly. These are author executions and a cold reconstruction, not a second-author audit or proof-assistant formalization.

```
recover_heptagon.py
13321 bytes
SHA256 975fca1e900d1b52dd51ab3c390daa7512a7e677c6dbea169552bfd62b46404f

heptagon_reciprocal.py
22016 bytes
SHA256 0efccbbbce21edbac90530e5940da6e2e50cafde42549cdb6f8b09f9b1e52055

heptagon_reciprocal.json
90063 bytes
SHA256 177888e8a36e9ac5a472b84c8b12201237dc25a12f8e25ff32fd769747dc1da1

identical build/check stdout
338 bytes
SHA256 4d80ad17a76cb3ae5498f563baff055f60b6b72dd48f97c7100689d8d18c804a
```

Expected verifier output:

```
HEPTAGON_RECIPROCAL_WIDE_11D_PASS 102 918 2754
HEPTAGON_RECIPROCAL_NARROW_GAP_1_OVER_3_PASS 3
ACTUAL_CAPPED_BLIND_AND_UNCAPPED_CONTROLS_PASS 457 446 233 233 272_NONZERO_PRIMITIVES
SELECTED_PAIR_PACKET_CENSUS_PASS 4879 13159 16 65
HEPTAGON_TRIANGLE_2P1Q_RECOVERY_PASS 90063 177888e8a36e9ac5a472b84c8b12201237dc25a12f8e25ff32fd769747dc1da1
```

Supplementary convenience copies: [readable exact verifier](sandbox:/mnt/data/heptagon_reciprocal.py), [complete exact report](sandbox:/mnt/data/heptagon_recovery/heptagon_reciprocal.json), [recovery bundle](sandbox:/mnt/data/heptagon_reciprocal_recovery.zip). The literal capsule below is sufficient without those links.

### Complete lossless source capsule

```python
#!/usr/bin/env python3
"""Lossless complete HEPTAGON_RECIPROCAL_2P1Q recovery. Python>=3.11 stdlib.
python -B -S recover_heptagon.py NEW_DIRECTORY [--extract-only]
Without the last flag, run the entire exact build/check and verify all pins.
"""
from pathlib import Path
import base64,hashlib,subprocess,sys,zlib
assert __debug__ and sys.version_info>=(3,11)
assert len(sys.argv) in (2,3) and (len(sys.argv)==2 or sys.argv[2]=='--extract-only')
SOURCE=(22016,'0efccbbbce21edbac90530e5940da6e2e50cafde42549cdb6f8b09f9b1e52055')
REPORT=(90063,'177888e8a36e9ac5a472b84c8b12201237dc25a12f8e25ff32fd769747dc1da1')
STDOUT=(338,'4d80ad17a76cb3ae5498f563baff055f60b6b72dd48f97c7100689d8d18c804a')
DATA=r"""
c-qB$dw1H%^5Fk`3eCM|4-zz3FOYzA&N_Z1Gn+VeY-c9JvK%1^BO4?v2^)Jh-+im9TSCH4=I)&H+sy+>{iv?4S65ZH^zUB|Hd%Tw
i{gVYeo)p=`67v}#=rjcuMa2ZSBLLEpG~j6{Cary{^QB?=<xjf<aqk!<mlJ)FQ1PNKTgea<6?UB?c=X!$0uK=UyW|#=$s%ZZ@JYq
45nnc7YAM%D9dP;dg+sr#LFk9cv%*vd6dMN62{(a83tYDEK$O39;UIkRHAsj$-9l~%)1GP5-X+iPU&1Ki*TKLH%UBALqA%liSI4D
>nCNliI&0t_7|alr;L+L4*fep1a0ypeVR0`7NG)-lex0VLKt-G`MHvMhyn~3#=$y?;#_%*@;J<}1)vRB<l#-2Dgf>g=Fmx#O&o*)
Yb0q9rk(sTQLenFWs)kZBnX!o%^}{b!ZZS`lw_SptLT{qQJ_)gt=7vZzEL6oFR_sm1$sB;X|hu0DIi94iB{_*&6QJG03=gRMVknS
lqbouY~v>@U?7c?i6(0=UjW662IuhDkoOBO!zy;0B{9pMvWDP=GMxtDY;!Z6($t}%`w*rXfSgA0JOPF(s>KXLYn&f`IXS!HYSYVZ
rq{i%-#$Mb_bzS2azCZt{HN_Z&r1GmvZg<GgTV88o)->W&mZVB(=vL2>$n3Ot_Ixo`varr&%?m527&2#{ekBjrfzsv&l)tf#_8eF
$t73SKI<`?S<GYx(>12L%wak+;Lc%vDlwqWh3kO1aA(n-#ca6R(AQxDxa-5UM}1s))*2_r?*V$gSuaC11JZ<n`d95qosXjln~&9~
ZD{{(8OG{dn`oM*%z>N8JB1LW#|R%&FTM#?(NO!2L!3(Z;`ff4-ZAPMlB9Tfs1g)SiRK^{P%$SC%;;8(<uQ69goy!PKL5UldHA9s
6@>Vxs!$FSpD_=x*BTdp58(92z26;Pp2)5%Z>^p(wP_ugI&j=MFz{j@^x)S#F!5r@2XRl$3{eA};8&;r2=~k3@g7(M;E4|VSMvwu
_TJU3H^(aubq=PCUBC}NRUO^5K?<3nw_1ITovMA;GA(l;3xL{3{{uu&mtuxOXEGChg#hYw58?-4gAiC31Vpc48s?icR>X|9?I$AW
mOUX!pQAN35?!**?6oePpLOw<>K*W--sP^f6<x4{Ct3zcUIU(OR_eC(6VQH|WLd3?>Wz&_Yc@6~9S?rs&X_QHr(>BeYMHz<u*?v(
0%o47hcyfiL9yW9zUEk3(cX)*N*6Ib#ItoMo2&o`d$-p@{Nj|;<dONwQm7By6!UDolj;i%u<TGmL$<wyS1_}x8VChj%8tmqmmLe1
{;VS~aDRpcTSd1De%aIN6%i4?z@7++eLHE-@Xmuf?Z6}$w>8@Sh}=;S#<}_`@KY5QK{ew1R(Ai-AO>MxVIMN&5QKpV**Zk|IRt?z
ggIG0gg_dYUPFmFn$JURbiv2tQ+2EDBpO&YX+znwHYr%ho_Ca;X_JPquRDBV1gWff44#FmM*HaAv6#&61&ZU{L}O=39BL!EBCc_v
j+0!$QUG%SP1wbFJ>mGn@Nx9O@q%}F<>T$a!wz9A0-W|o6-eQ@(J%at?iGX+NjMS0={&qtQmmq3ai%q90V&2EV^Wpu3(4E~0Xb12
ENDZ<#|6>HC4XO{IeEeI_{GTL7h!_f6)Iip@e1HlNWydlj!T>i6yNdjGRksk|6v|`x;hzwCk7@PoRED+<J>^C{)XGK6_Wm4jpYqu
2QeI<3&A~A^`Z(n^$rE#9SQ*cFnlD8I`9L{0{%|Q0z9{P@RIX)ZG%-XReUbdIKamHq^q{3cDIub_ggf`?T!yPIFfS{uRZ@xT_b3)
70hP=3)!5nM}-{+69PrBTm?`)hbvSwUvgs|2qwtJsITzvtxnE}d}^WUqJ5`lF!3!@HV_K`R&Nlj)O!?oAQtO2yJtA^hCQ&9ugf7+
a4E#H>dULqfyVF;@9&w>xu-iF`iiSZSA-*;#S)ydVku7HDrWP5;e{V&>e@>Yk#D?i)v9*oN!&jP%0FV4@o<3F38odxjz$}c2b0zl
Or7ox9Ur99QRi=^=>Vx#p)V3dd12v=gMbxdvY=4zZwxyK?B`w#&)z!RBJN+gKKhN*baicXWeRTuNuaf?#-1}e6!MCF$$=dDNt{RV
CX~`x(HS9KbFE_tY23=Geygp_DuMzhSVvFzj(*w(5N9N1jBl~;L$c&(=5gUeM^T!3eDv`VZvt{45Bk_XE1XYo2A+%Y$e3?mTU170
+Z=`fGT@T@8$&X}^MTDWsJ!R6K4x%VXpw+4yyvvA-!rU#X3rWm018s^mC0ZgMlhz%?y*j?>MQ$=U713Zfqc+ngRzxZfg7N;V>Aqt
7FiunYvW~xWE9MZ*tYK9dqiK-Zeh%KRRGW*M{QWUIe29y20o2FgJ3wz!zeZd2#=F_gb@n_td2lI8_l?i?icxBZFIj5Ooqhua9&a>
RrJW1*;2_zBlnDv3ulto)<!2z<B~Jpjvh0yOs^rBPQB&SPr~^;@*{8>G8ORx1?QzpJxVzceBHU%M(23jx^LfuA-iv>SO)8QrBH<*
O;!kHt4z5{`SX-rq}r?M<t^6>kJnnGblkI4!#+$rT!<&INMR1G0baF3%FdzwRS@SmEE@T-^e!si91YD7A~D#5`x&n>ja8mzD0~2^
i&>5sqD#*kFTnDLF<hYM?m=k4qV87J?Fhip8b_b`517*Uw~{WBkpgj%-dcLAS>R1=OFpkQQ@4-z|I2ORk^#Zr?=4LhsLuv_Hnnc!
%gNE_FUJ^tW8l<eieb72Q!Eq0cBZHuw{Msb^fRSn8qUD!;hkZ@0JiNyv%X~wEC+fSZm$OqQ0v%wUw6S$E2`b^nNWkp23#F$VCouH
KvZbsSUtl8AU(G~z_I#0%j~%hj%8U+f6zl{&<#pVb6^@h7!gJ`dVTB$%?%5%M0lp@>W*#=0A<J3O|#$YiE#`XrH`l@{houPI7Z*>
JBX=m4+a)aqo=z)*TQM{0gP)S6%0Vd!eJcChM74C&TuTpb^BP{H*M3k^+7QmB%NtHHV!m!iF7?1^BXP_%y3NG(s3TTZt1$K6G5Co
&xSi2W@Ha^AVFu)?*nmNglXCRz5|pui1a|1o~v78wB1-{&vKA-hTV4z$Dy%$eSM%K$t~M~nGOJeF>qYd(Se?Q9T+=sarVdz*C0Nb
R?l|LzKbZ>Kzr9VbxA-A2?%6@v4AH4OC9tEgPz{&BM999YTGcco@qKg9XZx>dzNmwKqBbn+I^Icfo>N=b&Njz0bxJ}4gdfURLTTN
gp0HR06m<RJ8%K6g>6Cd44@5^+7PuH2Fa8OR2|qZ$)Dr&4I9~Nz+|9?<ifQEJzzVER8Kc`i1;lzSPus4^#DuggaWS`1Kk`rb|2~8
w?XO%bCB-7Wta%o?m1>p7vuJH$8?CYt`3YGm||)`P(V({(fW?=SXR#vqd71d^4!*K6b;7(8sJ<yhGX;wj%gAieH#XYW*~bolz~#@
n!4?h{6bSH>>W_f0Wcg9)$QKEL}Aw&CuhfKy~vYZBy7o6Oa@L;$I<Hpw;C$7(KlYYPMGK!58X){>?5u>^n+_LEstC{Dd3UZaN*TJ
xi&iD6cWS2iUn6Ne_VTS*bSPn-??;BOE-+NEN;aa1D}8NfkSkUfy<G`e%D6N&-};jpS8A1$nBQ7JXJqvZSpLhwYLy1Fc&I;3SDo#
Cd->L6{854(2}7^#JiQa)7S_0jE=&;l`mk}VT61UDp{T;F{XmED85;S9Uo}~<`$N4OyBrV%P0=QlwksSq1<?D<*jjGbsJxG_M6VG
bRt%buo_bCy<U(G+X3<PD)q3VAm4kPy$949zh7P*et{;4Jy8OTj|w^tBH8b=ejjA6&up*<HqJ?v1)xrjp&JZLHb^p7$R<Szvt0NC
G6X|>IFl$y4nT7nRbw=)i5XOxFM!s6o^iybXMoj*6+ohNs)DiTftl9rT@m0v`du`~M^GJy^#tib(!q}4gVw0<@JulA&ojY9OZvu9
xC}BBR(6NWE;ze)oOg^OX8Zk&eK=!(o`Fp3>``Y6ojvOuxQ~HZYOqIxEntZ=L=m{MqnsnOPO57MYHHxMTx`)zBo1|QfF+y>xI^V7
7ZMo-RSTWS12<Sx?etuBddAS?&yz2o(UaF&hS7NU>(wO(p&P;Pn>YB>IQirJl8>>~q&*fwUysi#;USpK7p^jt)j9%YBCRd&B#67e
1+hO;gn9o-19y4;;D3cf8CkQi?#m+b+V{r!m(O5t#?-od199OGQ=kxj0=YUyC83TmCcE4-JqkZOjFz<&SVvVmo_25mZk4|TsZp+m
=t9nw=`@O?d^%OLa5-mNu9I`N<rwshV!rK4gp;&&IRYP#2hqbS3DlTvyCB#JW+b3e8)5&h&;Qbg_uo;>?v-$vh00&wMNP<&uCpXr
swo<`|4wME!hDeg0+Tp=RQ+WJQBp`a<Q$$<ZImO_yWxY}4S2wr`rRlGL53(f@$enmggh)F_q>=Hh*mK%3Plv~Hz|<>b_uuIe26I6
l_n6q0+(~-b1{vspRAu$t%w4}ptEi{EQBF<6Ydkk?!Y#+AE2om{;EqeVPe|tSr-!~(`icBaEVocVjSK`6iZf#{xIWCZORfciNJRW
UMm2B6{^g&NFKvuyE7}=q^~yWP^+@hYO|~p4G4y5y*;8;hv;U$M+?r3LPlWM_fe20Ypxeb9TDTzr!Xv&I6}r}dsSelP&q^@XY?Q<
K9LE$d!r9=fHwDL5R+1zN?d%EFJYQ;QV8lI=+;78iJ3D1z;NUTZ@GcR2Fx^atX3`2uC$Oapdq`IaSF`2E-m%RR5a%S`e2NNnBI>7
xi*(-u`ff=h(Wy&AL0v_{1MC&WG7aUaaUp%@VlMHvb(B^j)*TMF_3bx))G@;fmX8W;Rmd$PN4-Ofwo}s_2*OY<pe0t75Y-rNl4@n
$SO+J$hFLe$_=N69jOZX(EkoCv{KG4F%LId@G6%!brx;9p^)9hTYfoAy$DqND^{PRX_Bf<xfQ+J78llAZ0LlU@*Ji~lcvLAY1*_m
t<C=UDQLH#<)YQH7!uTn`24c7&?<CD3&qOQO$hXRT}wfhkUZKC%~M6sj034@QmcOoSb%Lw^~OE=6sWZ0LrO#xYV>1sLrPc3{pcm{
ibPB&Wqw=Ec;(&5VPGK=J<8$B9xHE4gG2C-m)Yw}!-JPbc<w>058zIvAzOGb*GQxiXr&P4nA^c8tS(29a@1;hU7tm5V>qiI|DAb-
nHEW`HIOWcgNRZal;xG8dB}OO*G6evN&+{OkF@vlvz?z;w(cgQpiGj~DsVzU#O0n}2f6c6q`g}$vlYN~-!F-Fsh%KutB-=ha}T0I
tE=uw8=b@9N3j9H)kASp8;C05`h(H5gCHu2B68WB2bl2=FwGr|O_<m<N00bpndN(^yFUR<lmuGtQ7Dg#Xc>y4miT>mV+_R|H(zh?
mfNDm0kyd1yTmaS)4m8w?=ARtLX&WRL@YaUr(}oJHHzOc##8X`njLCP@cX)w7W9@&RW3@L>o58DlKXP+>b4HUc*BnckKfp@Z44In
<66ih9=O3=JG*0|VtT_*J($lw&exB=@oJX+CpmkKRe^j1-2Q1$JNkp~wtSzUqz?8mjBXZrhCwBlkqhGCPGEf-U2s*#u3&7-Tt2wl
w;FpaoMcrMCtGZWNgfGL8(s*ME->zRBy|43-9aq-28?8w#HZsL;Oe9+Z^>0b3ns~cVHc*(U0x8YgZX>W7$?TWEi~zKwPPIIjHy$R
252Z0h;}4Gxc!ev+`ELreV^UCm@7E?awLWCh(Qc_1TkO{znVo1g>@g`VWkS${DAFnghM`-bjKeVZ+Yy3f~^??*cv7X@acJcdvIV)
u%lE3vHxCEhNI7w?Mw9#nH9~ILimI(9SVz?hjEsq*)(5)hrb08y-7n_UVwa(;aA<#h*PE{nzU7~J<|?Mrp_=lF~OKiQ}GHi02b$1
7xeAkYPqdA^Z&&vu<I!V8Rz?R70DLSJeQqr55Dfq1ZhllT34npF9%;c)CrF%h@0EVe|D+>^bz@wSTX9kuXv*H|5Ev`{(mXo)jv@_
!uIO_mGVh7`7h8w5zpgE%~HKkvmQa;a*o^YBUl#wg}BZ9Bn>&P#D+1t*?4J?k(VKSBPjxV`u8_VH#%ICcyqA?N$=~9U4hpL6JM_-
)IG0>pdQjegthbmV2+3EdT$Jro7c?;Td&2&|GOV7$glfO$}(Y#NE{W2CRLa7##{4cLXHmAK2N&nqiVZ7(CUi){0omXNyEaS0tlKs
j6(D;PC(#!Rj7MIg+sv_c$S<|Z&_5|Yb|p}Lt+?U(k|U_LTxdT4(f9o&v5>9i;IS1G!!FnOdwr)v&lm^1-e3D6nhZ-JnsAkO#MWl
aPnvrc<-q^LqhrP!(;TI0i=|o(i2qa_zWfn2%z+<%A+MGXUDj|E15^TuyQ1MKIHBfOhLW_+rm|mYs7t3l1nf*MXIq<rV%75zS<~H
f`pINW|O@GM|v50bHHzuhglv5TpvNe8?81gsS+Tr-iphEyxnZ!nY}(pL$+Q<`P5G~ah{3bUAUJBTO2n@f{+2-IF@wR$r^J}G(?*l
*dR}zhQQ@lNYD556<dc}KV0XP7!>>R&ShO^g**UVF01NGM1$sUb&(mt8JFpK!V@J^D<_UAb?6}<ODQEb;cl?3V1+y@f=J!XIzXND
y*P>SP`0YxF#(=%(Zq=WO0-b7TaNKtDb4IIeBxsNRJk3hVlH6dJGbHh1P5whE@#E1>5-Fxb&-Sw?ae4fBVBpMYV@_iKCNUeJ+9bH
;$C4S)>NNKhi)+uL>wdLmOIKsx%M2_4s6uiHnleHbjm|wIFg3PZC+`m7p)LGP12=E#*>V^;ie9MSo17VAfAm@pgqfF@|Y=f<lKvu
O*{uSWQ#BWQF{o}ZnIIsKx04)PfHw|KpeD#15+!GXbP62E}|?z_+>Qq5a8TwVOOf}7?hA8Ro+F1ehvZp%?d0!$J1WkLzr=F&LjkJ
fu(Od4M27m#O*3NuOq{}ZIn%k4OxvFtdP&sQUWhEAzM=+fm5NLT*~7j+y>DNV4+qQSve13-oUg+D74ccS$QDZXmpkdFHQxgGK-!T
J_;HXhL%km!75QC+keum4BGTJ%LKHPBL77Mcld0S&&K49QEzLPbvCu_mCwCuTc|OMlVfmi75C82oV4NB+H2jfw00`3`;!C05c@cE
Z$pTBstych^i1u=kYZa*D?k~Ow?>C*%64dp=_nh5K{trnVrj<^#ZKAQ=r}DP82D|}cwjM5fa;MhlDC<cc}rN0HgQlKYC>|uutTu?
fH+)0>C#0~G%6ghQ`LbASj}!jKaXfhdkJJPBp`6Xwn-LI%Sxw8K6DD&7^W3mH6c-p&2l-Nd${%Z4W$W_yBU~~GLv!3Xc4TwN22Z)
zi%+I@I+$1JJz*xbfw>WSNOd$!_JE%Yt<uYAl$G3kh3ehf#1B<DxuA{iRh139b0Q}xsKilYAQXy;rbAd(V#afO&0ZD?k8lZHEpMG
u2-}T4@?S2V)2yGqVSD<!ufrw1uZ`~h5BiCJ~&X};f%6EyHarLKCv^fUvii9W!zMp#uDYwQq&BDEPh1+t7RX4mSOm5YGQ}y5&E^s
GTeDR^%H}2#?C==kePVsuVn8W)M!_TxoW}1qGV^SF&DJx6txi^Dbp#g6)(5Ynq8}Z`y%ON=%qV+_u|DGTB&jImFE%hpltbiPG#9b
Jj5u~$<1&QUOBB>`KT3G+zKo)!6tTz@CYOm`#=(Kf&2~h84+2F6-b72y9N-+Vb6;qq`<}{V`_TIdHv<1`HT0AzL%D%((z)~vDlXV
;oC(Il~;-$YQzT6!J7X?(eDs(r+BvhIt9|}52V*0q~&#;C=wk+J^6wX0==&Sy?7ny1p>Wz0rad6^r8fMUF1ZgSHy-6zXIbQ-UxOA
?;xP3*#_%s^54U)abV5m<&U5ZehTdVHDDh;pxgc!dUv=pMThJ1oz98mf;wjltyq=mO)YkEN<#ho%++8$hE@{>R|vA;dOwEtbX~Cd
L>q;?&WKUYJF?ROQZ?M8aJbK@(UwvvB4a^E6GAAIiHdsP?OtEN@g{}PLsbPk=g2oeid7yLxKOF}0$IN(>S<5a=i(g%gjneyGatJy
vS4S=it`n|k696cfP6NJ5jYp!c1o+_0`mN<z0oyXncn1Y46?Vl&iFoPvRt>yX2TC3%7_FRw^z@Fm!cCVpNAE@qrc(#8(xP_8^_9B
6bD>wem!j#D;(6JbtIeE{Cd(PX%a>U54FpRlT-Ah6_l$kEZnemd7EXfZrOOEl{gCN!XXG%DSXu_Fpwnn{LFIZ`xQ43^yxoPsDES?
-smq*tq6#>zX*jXE!?G8hwk?zkhoj73Zr?F<Z^x7NzJ{6{~Iri|2@Oz;3|rQ1G}#q#|y${@e7|rU)&+3ti`t22O*C{Vzl0E#<peA
ePw^PQ5-8kE)5H}6c(k+OL0Q{`dXvY+8;gu%gwqISsV@H-{fXsFfEJzU}Whz*>M&I5It~VHt@9aD&$|;JW8{Cx=JYU`AvXGqJZB(
tV>Di*bn&;6CS_?`^3RR;b#nD5*U1X$uBR9`)huEUEF_=ya0q*;VMnZw#g-m<WX8djUn~GF^yK_qGlYQ89swqksWpx7=78LmzEXx
y9%7)v@o6Ws+EWFVPZ?Mf4_H9QA7W&ax@Opw(0;6k{Y&aGg~)%<^WGob{xmCtsWF(Vz(?dT|7o=T0Pb=T_`aJJ$z|+*Sb>990)&j
Jnc-3KYKB*(bG-GFrka>^mNx?9m{YH2S+T60PdjgxXf`)vxf)yWE)w);K_1r8sMDQT-DJ<^%>pIGtBn#^Ko;>@8)E56mfBias-Pz
$r-c|9BIPB0gE#gUO*u-qdD2x1Xxi_<`xl^E@LVvwV5SK&0bl0KXzGPmSTzkS#idtBMj?Po~obVW`j3add5B>!a=yqJ)XDnj@jD4
(;OliZnZWYD5`A6LZi1(g75gsSB<bCddWp56hbQ8NNeg{y=OR0jI6}H+r+hqo($9I6*X}0>}p)I-!E$5et>TXvjU#!IAu3{s6n&`
_70>y7*t@|j#<{hgJm>DPK9#FY*xNPAQJGOC;@*I0l73*&Pr^YQ?5Kxx4X9~A#y8x{%v^{lO1Y%)(?AmS_?0;!Vt@s7iP0c+Zn$0
fx$k#`i$JxS~Gkfq(}{jhZhYfjK)v}#ZFor5IXUK#i>dGu8G?m4@EY1*73E28yJmnnK8eh0`?Ingx}MaC`z1elt*(rsAou7ykS%=
E3wPt-jeZ9TQA<DFkS=H_X1(|Uc9=-9_jTLC^lrVA&YTqOvPHdXGR+VKd?s{?7F6j*BbbE;J#GiaV}0x4<>C@>Vueph{s3Q6;-aj
qgI2VA!H#d$K(oJv+Hvq4Qp0t?QunwSy@u*@xCG(#-0XahM=y$2Kp#|6qC_7uG^B*`TBG%Uj>AQf@E)9y#=LoPo+{YcIcn83nr!@
fdKHm)uKs94-gxiMRl>kn(;1yGo~mI8WoEdPQPAs{j%sov+zy!Fhbzs6A`q_XR|)N-*3?;B*b+$HVC>{a+{P9a_p*YtZ4y94Y2xP
jV$K611SYy@g0V5W7s6c*dNv&8|CWX$`O6K1P_~ge!lUR__>g<lcdoN25kwRmh<rACG^4|Hj`PE%}S}9M(+x`<FN`cQ<3*OhuQ2)
8BSkjbzVOkaKn$QbK1$25Hw^O=JogXFlEqN@=`YJBTb5(Ow0<^9UweDkA5nQHbwWO`i!p13=h~(#fm|{xNYW#u*~E#K!~2fX`*JL
!GQ{khE}bVD~!0vYG@ukL;=uy8b&uEe(a=JQ_4H(#7tKq3e!|NA^e<Cx4qH}wuyc8xq~SZe7Ovl{CZawC-JWMoK+sF`3hf&Mz3ej
AdvS1vVgWe7Cs<L(XYj$T){0LkA+R0?!BsAvH8?#2#v?yqzDRTpw>_@D+}<YKRn^^7XlyR&-W31?1qo=p@4|+sJM8qkwy@(i+9^+
MfL>X4N<UW6YdFMyW#iVYJ+C9zY&#(!t1Y%BV1H$e5n^AJP{qy+xgNx+<>?UmyujVDgfeuxf<-#2bPk_XaT`21nkgAAB9`|K2Ie@
2C|X;AT4Tuxfqc0ghjrVT=LqRv)Eq-jgobS&VX?k0m=8wE1A(a7n^X<nhqTl<O?&*eyaE}o4q3Zs*QN8!U>8^@srb6zOVs^i&UHh
Rp1D#%2-XA#B;!ckfmB>=d{R(Ohy$CW9?PHkRTefwI|Xe2=yN2X0M#yruWEj^e5o;-K1g2#~5`Hn&Iy7f0${n#G}Or6*jd}lDhSp
*9g5Swzk)>2u^<CE|LxIZMe6pG$Vk->-%&_LNne>#@R$}i^`~9;EKVU^h5Cx8gg!k%|noB@$G>h#nG}$gk8iJrhefY^da&EA46}-
UdmltEW}L-Xfee5LTLd1qG}?x3qgo$J75G3e}sWT#m)GADz@~*RN4Jna6=%DxXI~@uRj4dvOR7Dq4t)W!$M1HBVO|jyX2*z1ogx~
biEb`$jAFND=|Y{mfjjv^EJkc?;Mewa(*kcyn{zI>R)G~q>NVSu$O8Wyga2ksI2CI60d%O0`LLe+O9KbR5vYg8vw41!~zpb5cc&3
Vv7k(5fC5C`X$}4a64}9NZ*`Pb~i-xey_gzZDMQ*%L7FIU{K;5Pw0c`r$q!}dod<i{9=EfE)2j$%RGs}OXG0QBzJhhCHevn*~T#T
)vbJAs&>Haba%KK!n3XRvW1FU*COqsm5s*;@VRo*WIK7;6DL>p_zU6RX+!K-KbgHP-vKGfvK0os+_v9^KPrB>tQ%}r>r54sVki*P
yYMOFc!URNhwEpa0NvCkgTF(F#KJh+q~X-d{3xPkTD$o_<EGXH7)cPS@*@}#zR6z>C0^`jdnYYsT5TJ*A-^Cbw`wbyAN+`#m)<;(
jG{NGmETswV%%!QiY9%#4!@X&E+8J!#|=9CW?KmXV<x%wl|VVSWO}gMq}MOHtGggdRiSQ@7U33nH%;!iJlrJql=+K2=FuYrlDvAd
MjOeqHPu3bGV*=C%fyU)B&`(4a`9~_@guLOgV>9&sRE7&gT#N+OklCgOaNSN=w_*J&`a#<Hz#|rq1~X55{2Kr6G0P2%TfNsoB!nV
hD|0-nfL@Alf)DkwtE%dTZ814A4Jf0HRaa;ru6B-j30ew#kU8i<+lg9d@XlZmCU3gSU4M?NelUkt6ZenBj$F=7@i$#3<)sB<2d5=
SMf}TGC1BcLDgxxNGMhxU@!=7zlCus`tPE;0AQ6R^x?!EKD_>(X3<IvBpz5!@1;y<cy<C`ax4mjUum-Q<Lbu?grM<3D}LN<cLx!E
@ev3Z&{j7Xm#I8UWIEWekVfwNRm+K@I4#7JE_kMC9rEU(2(dPCgpt+q34~-GffpWtMuiVy+$o)LrFge@gy)@>n*g1!7<wF=?pv<2
W81>ZiQ9iGbH>8cN3U^}po4{<Q4AFkCS*)mfWZ-K-7S4`^3piCHt@@lxpHlE<mWM$%g*KbvCQE!@CYD^0#H86uOBk<V^Ww&Y8W~O
f?!%V^qI)6^3j`xG?Ri5!VAt65MA=s((ndsLi!|9Ygrc!PU=1Kov{@fBmELEEC<ckKDvo^xJfp@V$e93R;&p1$#qFX4`Q>Y9L);n
FjzwzxuVL)6s*6jg({3dQe5nJDq2y=-+w(mnHt9N^!)JhvdMt=Bq<~YKks=)`-ju_hv!pc`uQs;v{e9!cRde}uCAf6v<2@_^{0pM
|N2Z89eqB#`tteXrR>|ZdyZn;ef$Ul{>N_}I_C83^BKOxJ3asM>!)9@e*JoK+1!nBdGhh(=;{RL@avZ;eqZq9YI<~Xc6nVuMJI%b
HQ(s7e(#l;m1c{K6j}_J(l^<^h3gp7Qfox?PA16mbPBwgPSI3Nr_G@-`;GqtDZX4s
"""
def pin(b):return len(b),hashlib.sha256(b).hexdigest()
b=zlib.decompress(base64.b85decode(''.join(DATA.split())))
assert pin(b)==SOURCE
folder=Path(sys.argv[1]);folder.mkdir(parents=True,exist_ok=True)
f=folder/'heptagon_reciprocal.py'
if f.exists():assert f.read_bytes()==b
else:f.write_bytes(b)
print('HEPTAGON_COMPLETE_EXACT_SOURCE_RECOVERED',*SOURCE,flush=True)
if len(sys.argv)==2:
 outputs=[]
 for action in ('build','check'):
  run=subprocess.run([sys.executable,'-B','-S',str(f),action,str(folder)],capture_output=True)
  if run.returncode:
   sys.stdout.buffer.write(run.stdout);sys.stderr.buffer.write(run.stderr)
   raise SystemExit(run.returncode)
  assert pin(run.stdout)==STDOUT;outputs.append(run.stdout)
 assert outputs[0]==outputs[1]
 assert pin((folder/'heptagon_reciprocal.json').read_bytes())==REPORT
 sys.stdout.buffer.write(outputs[0]);sys.stdout.flush()
 print('HEPTAGON_SOURCE_ONLY_BUILD_CHECK_PINS_PASS',*REPORT)
```
