# figure-0532

AI research report · 2026-09-24 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# RESERVE junior-carrier release: three exact finite non-target controls

## Outcome

**No own110 endpoint was established.** This closeout supplies three new, exactly reconstructed and independently cross-checked finite carrier/root modifications of literal **RESERVE19_G5**. They remove the old junior stable carrier and saddle carrier; the final modification also destroys the old elder stable carrier and replaces the terminal unstable vertex. Nevertheless, replacement equilibria remain.

These are bounded exact constructions, **not outputs from a completed numerical guard-release optimization**. No unobserved continuation trajectory or solver result is credited. The useful own211 starting objects remain the parent's RESERVE19_G5/G6.

| Body | True V/E/F | C | Strict S/U/H | Additional weak | Positive P/Q bars |
|---|---|---:|---|---|---|
| RESERVE19_G5, reproduced parent | 31/87/58 | 174 | 2/1/1 | 000 | 0/1 |
| RESERVE_RELEASE_CORE | 27/75/50 | 150 | 12/17/27 | 000 | 16/11 |
| RESERVE_RELEASE_ROOT1 | 28/78/52 | 156 | 6/17/21 | 000 | 16/5 |
| RESERVE_RELEASE_ROOT2 | 27/75/50 | 150 | 4/7/9 | 000 | 6/3 |

All three new bodies have **primitive-zero counts 000**, positive filled volume, and their own homogeneous volume centroid. Their complete landscapes contain **57 positive bars**, all retained with exact birth/death values, complete components, cuts, and attaining paths. The capsule below reconstructs every maximal facet, true edge, mass quantity, equilibrium, and landscape. ROOT2 has 28 input rows but only **27 extreme vertices**; its name must not be interpreted as the parent's distinct coarse-grid own479 control.

## Input reading and identity

The updated journal was read through line 1044, including the entire immutable parent. The parent Markdown, serialized as compact UTF-8 JSON with `version=2` and `result_markdown`, reproduces exactly **49,663 bytes** and SHA-256 **068561478600e3762da427d542c3e881ba409c91eb7fb963ded6c7071474b37f**. Its recovery program also matches the advertised 28,725-byte source and reconstructs the 73,054-byte dictionary. There is no unresolved parent-identity conflict in this closeout.

The parent's two-stable restriction was real: its `Surgery` program deliberately protected both stable carriers. Its terminal insertion mechanism was also real, but belonged to that different retained corpus. Neither the old two-stable constraint nor the old terminal insertion's census is assumed for the new constructions.

## Exact finite construction and the restriction removed

Let `P` be the filled convex hull of the literal RESERVE19_G5 input. **Sort its extreme vertices lexicographically** and denote them by `p0,...,p30`. These are the parent's canonical hull indices, not its input material-order indices.

The old stable carriers are face 30 with triangle `[10,29,28]` and face 54 with triangle `[24,27,26]`; the old saddle is edge `[25,30]`. Define

```text
J = [24,26,27]
D = [24,25,26,27,30]

b = (p24+p26+p27)/3
  = (97984,55285,236597)/300000

a = p30
  = (493239,227334,39141)/300000

a2 = 2*a-b
   = (888494,399383,-158315)/300000.
```

The three new bodies are exactly

```text
W  = conv({pi : i not in D} union {b})
K1 = conv(W,a)
K2 = conv(W,a2).
```

They are named CORE, ROOT1, and ROOT2 respectively. All parameters are literal; **there is no rounding or floating optimization** in their construction.

This removes the former stable-guard restriction geometrically rather than merely deleting a line from the optimizer. All three vertices of the junior triangle are removed from the retained vertex set and replaced by one point, while the nonroot endpoint of the old saddle carrier is also removed. No constraint requiring either old face to remain stable is imposed. The subsequent root extension is allowed to destroy the elder carrier as well.

The exact carrier audit shows:

* In W, the old junior face is absent. The old elder triangle remains maximal but is **not stable at W's actual centroid**.
* In K1, the old junior face remains absent. The unchanged elder triangle becomes stable again, solely through the changed actual mass distribution.
* In K2, **neither old stable triangle is a maximal facet**. The old saddle cannot remain its original true edge. The new point a2 is a strict unstable vertex, but six additional strict unstable vertices remain.

Thus the endpoint's S4 is not an accidental consequence of retaining both old S guards. It is a genuine replacement landscape after destroying both old stable carriers.

Since b lies in P and all retained points lie in P, W and K1 are inner bodies of P. Since `a=(b+a2)/2`, **K1 is contained in K2**. The old root a remains material in K2, specifically the midpoint of the true edge joining b to a2, but is no longer an extreme vertex. The new a2 violates 14 old supporting halfspaces, so K2 genuinely leaves P.

## Actual mass and terminal insertion ledger

The actual centroids, shown here only for orientation, are

```text
W:  (-0.11526017231717518, 0.04152853659850793, 0.17748546750773025)
K1: ( 0.021415010876237744,0.07787305201214616, 0.16118933987402354)
K2: ( 0.3564224269702064,  0.23433900996051488, 0.06971312501853197).
```

No old reference point or old centroid is reused. Exact values for all bodies are regenerated in both their audits and the mass ledger.

For K2, the exact density-one mass quantities are

```text
Volume = 3316089200918363/1800000000000000

First moment = (
  1772892841561522817479/2700000000000000000000,
  373002748936302752531/864000000000000000000,
  138704964621735375017/1080000000000000000000
)

Centroid = (
  1772892841561522817479/4974133801377544500000,
  373002748936302752531/1591722816440814240000,
  138704964621735375017/1989653520551017800000
).
```

The finite mass changes are exactly:

```text
P -> W, removed volume:
37506247286587/93750000000000

W -> K1, added volume:
1733916747662017/9000000000000000

K1 -> K2, added volume:
3760667862942617/6000000000000000.
```

For every outward triangle `(u,v,w)` of the body before an insertion p, the constructor uses

```text
s = ((v-u) cross (w-u)) dot (p-u)
DeltaV = max(0,s)/6
DeltaM = DeltaV*(p+u+v+w)/4.
```

Coordinates in this formula are physical coordinates. The implementation clears the common integer denominator explicitly. The sum of visible tetrahedral increments is checked against a separate complete re-hull and volume/first-moment integration.

Insertion of a into W sees exactly CORE facets `[41,43,47,48]`. It preserves all 27 existing extreme vertices, creates one new extreme vertex, and changes own `(12,17,27)` to `(6,17,21)`: six positive Q bars disappear, but the number of positive P bars remains 16.

Insertion of a2 into K1 sees exactly ROOT1 facets

```text
[18,25,26,27,28,38,41,45,47,49,51].
```

Two old extreme vertices, ROOT1 indices `[25,27]`, cease to be extreme. The second is the old root. The true edge count decreases from 78 to 75. The census changes from `(6,17,21)` to `(4,7,9)`: ten positive P bars and two positive Q bars disappear, but complete cancellation does not occur.

The full three-component removed and added first moments are retained in `RELEASE_MASS_LEDGER.json`. The program checks both the two insertion identities and the aggregate final volume/moment identities exactly.

## Final endpoint: strict mechanics and complete residual hierarchy

For K2, using its own lexicographic hull and sorted maximal-facet convention:

```text
S = [18,37,42,46]
U = [1,3,4,6,9,12,26]
H = [[1,3],[1,4],[4,6],[6,9],[9,12],
     [16,26],[21,26],[22,25],[23,26]]

additional_weak = [0,0,0]
primitive_zero = [0,0,0].
```

The six positive P bars have relative depths approximately

```text
[0.003906400338547654,
 0.002292657197398906,
 0.0010644653350309812,
 0.003922669206564117,
 0.00024765527234090184,
 0.3604749349915561].
```

The large P bar is `1 -> 26`, with a **20-vertex component and 15-edge cut**, attaining path

```text
[1,4,6,9,12,15,19,22,25,26].
```

The three positive Q bars are `37 -> 18`, `46 -> 18`, and `42 -> 18`, with relative depths approximately

```text
[0.022193553744114587,
 0.02024306640259593,
 0.8330108694717805].
```

The first two have singleton components and three-edge cuts. The largest has an **eight-face component and eight-edge cut**, with attaining path

```text
[42,40,46,37,26,18].
```

The smaller interface does not make this a better cancellation than RESERVE19_G5: the dominant Q depth is worse and there are now nine positive bars. All displayed decimals are summaries of exact rational values, not zero tolerances. Every component and every cut, including those of the two intermediate bodies, is regenerated completely by the capsule.

Three additional exact margin summaries are computed for each body: minimum absolute projected face barycentric coordinate; minimum absolute actual-centred directed true-edge dot product in physical squared-length units; and minimum absolute primal/polar edge-foot parameter among `t,1-t,s,1-s`. For K2 they are approximately `0.044790385646351`, `0.0018739834212774962`, and `0.019600588155188052`. Their complete rational values are in the ledger. These are explicitly defined primitive margins, **not** a certified deformation-radius claim.

## Verification and a relevant auditor limitation

Verification used exhaustive integer supporting-triple enumeration, maximal triangular facets, true edges, and actual filled moments. The second route checks inverse halfspace vertices and edges, three different tetrahedral origins, face projection by barycentric coordinates, U inequalities against every other extreme vertex, and mixed edges by both primal and polar feet. Every closed weak test is included. Complete-chord bottleneck domination, exact barcode equality, and each reported cut and attaining path are checked. This is not advertised as two unrelated black-box hull implementations.

A useful implementation boundary was encountered and corrected without changing geometry. Explicitly appending the old root a to K2's input adds a redundant point on a true edge. The inherited simplicial auditor rejects such an input because its supporting-plane row set then contains more than three input points, even though the maximal geometric facet is still triangular. The final constructor instead proves `a=(b+a2)/2`, verifies all K2 supporting inequalities at a, and verifies that b--a2 is a true edge. It does **not** feed that redundant boundary row into the simplicial-only auditor. This is an input-handling limitation, not a mechanical obstruction or a reason to invent a new facet.

Both the working run and a fresh-directory cold replay completed. The parent input and audit byte-matched their immutable identities.

## Scope and continuation

Only the three specified finite modifications have been audited. There is **no exclusion theorem for every root position, every point replacing the junior face, or the wider RESERVE family**. In particular, the ray `a(t)=b+t(a-b)` has not received an interval-complete equilibrium atlas. The fixed-reference-centre exclusion for the older K is neither reused nor strengthened here.

For this fixed W, there is an exact continuation model without prescribed centres: each old facet's visibility numerator along a(t) is affine in t; its added volume is the positive part of that affine numerator divided by six, and its first moment is that volume times an affine tetrahedral centroid. Hence the complete actual volume is piecewise affine and the complete first moment piecewise quadratic, with rational visibility events. This follows directly from the executed insertion formula and the exact W supplied here; it is not a claim that the intervening equilibria have been checked.

The next constructive question is **coupled motion or replacement of b and the terminal root direction**, rather than just a farther extension of this ray. The current collapse breaks too many physical escape connections: even restoring the original root leaves U17. At K2, the explicit P20/cut15 packet and Q8/cut8 packet identify the transferred defects. A useful successor must repair those physical connections while eliminating the full Q hierarchy, not simply remove the old face labels. RESERVE19_G5/G6 remain the better own211 entrances for such a coupled construction.

## Recovery capsule, commands, and observed identities

The following complete program contains four literal source/input units: the exact RESERVE19_G5 input, the full exact auditor, the full independent verifier, and the complete producing constructor. **No earlier decoder, numerical optimizer, external library, or sandbox download is required.** Python **3.13.5 standard library** was used. All non-default inputs and parameters are embedded.

Save as `RECOVER_RESERVE_RELEASE_CLOSEOUT.py` and run

```bash
python -B -S RECOVER_RESERVE_RELEASE_CLOSEOUT.py RELEASE_OUT
```

Observed terminal markers:

```text
RELEASE_EXACT_INDEPENDENT_PASS RESERVE19_G5 31 87 58 [2, 1, 1] 0 1
RELEASE_EXACT_INDEPENDENT_PASS RESERVE_RELEASE_CORE 27 75 50 [12, 17, 27] 16 11
RELEASE_EXACT_INDEPENDENT_PASS RESERVE_RELEASE_ROOT1 28 78 52 [6, 17, 21] 16 5
RELEASE_EXACT_INDEPENDENT_PASS RESERVE_RELEASE_ROOT2 27 75 50 [4, 7, 9] 6 3
RESERVE_RELEASE_THREE_CONTROLS_57_BARS_PASS 13 48631 7c11a2517ada4a3bfd8b11bc91cec5535132fc62eb56a0753c3bea637b6aa016
RESERVE_RELEASE_CLOSEOUT_COLD_PASS
```

The 13-file stream hashes sorted filename, newline, and exact file bytes. `RELEASE_MANIFEST.json` supplies every individual byte count and digest.

```text
CORE input: 691 bytes
4de07915a393d555ee8714b90d5e75f95a418324a2bc55f0c348043a20a77dbc
ROOT1 input: 714 bytes
fe33abe087b1de570b5bcc7ac30972e8eaf0742351f96666bafe4a5c019fb134
ROOT2 input: 716 bytes
64dc8eb52568feb1814b1e1c04d1417b74393e5cd7fcf5b76016553306bc53a7
ROOT2 audit: 6656 bytes
7006dbb28ea9eec837b456638736ad6e1e6cd10632cf031c2a4dba455ee7dbbd
Mass ledger: 6404 bytes
8aaf6baac5b63453a85d0383be21ef7efcc91cff2094a72ae640ac8ed452d3b6

finish_release.py: 6925 bytes
b4d6eac71a726024f20bb978446254c1b4c527c63bd8242491872cc2f8d51b9c
exact_poly.py: 6134 bytes
898f77989193886996d6f2dc121ccdfdf611b8a9ac52fd3207557eac6a69c0c4
verify_finite.py: 6296 bytes
7672f102c36a35e16bd82c418d6fbec7eef1edd85b2ee9e64d54d3dd04dde606

Recovery dictionary: 20557 bytes
f32a1e177619b3ae89cb6bada09a2e6cfa5bf0e72d887306b038236a0c9779a1
Recovery program: 11202 bytes
86c62c4b761cca9f9d0372341651b43c1a4d5e6320b52a4d97bfab6c7904c2a9
```

Convenience copies: recovery program (`RECOVER_RESERVE_RELEASE_CLOSEOUT.py`) and expanded sources and exact reports (`RESERVE_RELEASE_CLOSEOUT.zip`).

## Complete runnable source capsule

```python
"""Self-contained exact RESERVE three-control closeout. Python 3.13.5 stdlib.
Run: python -B -S RECOVER_RESERVE_RELEASE_CLOSEOUT.py OUTPUT_DIRECTORY
No optimizer or external source is needed. Not an own110 claim.
"""
import base64,hashlib,json,subprocess,sys,zlib
from pathlib import Path
PAYLOAD = """
c-oyj*>c;svhVjRcyb;@+K{7Nwl$b4JCP@z$|UiUNm8;(MT(R~TOt{flI`T?-)}Df2}*J%bLZ5NK`f01y3rdN`TpW^cs0EId)Pdh
{LwwQ%i`$8@r&;_FZ>{imto}QaeDLOxY@w}#LbJyT?X)dQyF&i0$P$djPeZHMx**sx7%!qX6L9OTHRK&Jr+>c?i?P8dgrL$6P<4V
@Q5l~y=EUikD8+0=p0g2vwPSS&Bh`0hHl+1_v<#=qTW1gcRQlpJUk+hhlkB(SJc~$!&X}~4?E2!)pncBL(x2H_l`ur)$I1TveE8~
RtGR>_S+4r>mMC<I)G6V&;_79g4yphVES(72myBvd)%|z>vu&9rx%C)R*Ncoop!e;>fHt)3{ZQAeOgkl*=fTp{X=N$^Z{|Igmtz=
>+pz{);MAaox?^C5a@Q>uu=8aQNQ1!>VCJ=5P*KSA)3u*tKG-iHf%*t93J%rOwsFdUH7ns-$&hcOVkg0E!qG8)Bx<e{SE-Aw>8*S
uhDLZP6z&qCJ?1Vo#8J`R)+-wf^|Ush^WxRrPjMg?Jm-+4gW#yVXN7Ml{K3EK91-r0I*%nqYlu!)jRB9Kg0+385Rot4tWm%=Ofzf
P7g=70A;9c9RVf+T3{W`R`;-hv-be=wt!iItgxDH7kl;^T|m4Ci|E3x^Z;w9Jn9`mpFWVZCyv^O{WeY1=>W`rx8Dag0JiFn$3JeO
7ve?m=uY!V5-*+(k|$vE8~Wc6YpvAH!#Hvmmb>!9+=^$GYh~dwS%lLNYK!J+9Ib;#t6fJh^T1Ez=-?(gSuCuj`xq{v$IP7undPQ|
6-29L03!o`U`271r=c6&t`=@;_Iac!^2L*t26w>}Is?2{0rZYT-wHD;p9dCTxI)n3ViEY(JYL4PK@`NR%v#3_n8cc@0m6!cb&vw`
>i9x;I+*~JmwOY<(s*fwd64FDyvQtAWSr)(u%(9sV40cfGh0Q|N}n|FSJObXF5P^t8*Zn*9+LvD2tzlWsS3-@tTWXqfuW1g(_KEm
=S`$OPy~tWDHC%y!%jDmAIvO2&TUtC&T$&#t2DB*)zW_4d$MM6YCVc4D~zmfVM1LT9+9oQ%7}cGECTzn{<ASraBI68BkGSl0K2=Y
-!zT0tODJ3N6qn`H)@URF8n|V4u>i=u&%+aLY10W*W^|OG)co{n1}0t0pCOx{C6vP&u!RYVY^;tKRP8o_8uWG8V>h%vn)Vr@K<%=
FJIo83lSbv08h}=d@$y##llYA2R*mDSR^t7ngqU`1-ZR+6Pthu=rpRaz^{!R#~Ea+1c{f)?>~4f&J>C}agVc^tOXN9w}HI~A{*fY
@@+jI{ufE!TcRGckM3a0@NYPFL{WKPRyyU_5C|COmK#0Uk#h_OH4mdzP`1w{a#2(a9r&3XaaH2f=Y(@Yy8|7@6}WJeY(H~;Yy1YM
97{XEV>fR6y>T2#<fX_N%w>H}6V=x=!5Sy<vz_3jZ0v#yqnU=G+EyQ76v72ZA`l;j8@useiv?R2uhMCNf}|8@10`#4r8^`O2m?0@
vV#(sVl1RuNQkz}Hck5xw2WoR#gUjRbZ`X*AMr9~xClL#7lt)6;HG6FzlX<nRCy=D>S}R*#bk*bDO#4}5s3jU0``1dGUH4TLgu6g
AOn|~ZL;4?<GHLtomJTknWp5^WHf`LJQn!3F;;wvA1$NO5fQM@G4>SLBJoGyr!hOBec&cZ5c#$}6Ns^zS+ya0_I>aq7w*#YU2Ar%
5XM<x>jM8asGh=mp#W94k>QzZS2TtlwfRu2o!{iVWLi3|2C`5O(nm|t8Ls7cygwTqH^<H~;c)=e2Jzyq7C8$JTOrFb*Ab(!qgQ)h
6=8@4a@!hstySW{VAt+q6#(I?L$EuXWBfzioP8{+bpn)%P)r0j2<ockVCwpCI_%F}t2gJ8rNpB!MepbF02FPs!DVVgXt=SpzC@Pz
Jo3ik^T<WX6GSA8eBp0!7Bqkq$mN-B9_C<?1yG6d1senkj5E9Gh%>v6a1bhh5-{8`MPi~P2et!4@8^4dg|Ar{w~=vZF$M1-&;-Py
P}-4zxpEO^xgo(nqwG%t_g*IM=y*I>21_qUVN1S;KgvlGcRcW1tR4^YGzjEq#3)R7BN;mG|15;LLz5{V=HVg$2!Qo}WOz&koQw+N
K`5zE_E+Q$OOnimB8uWYUZ^n6P;hM512{e+z{459xpYhvR$?s)F;JTH*Q=6jCFOdzI<PNCxH+R0$^kAozv;@gu3W=$!8z7qRgT7e
0-9-hcn<9xFp#cs4J5oU&F8X&TS0;vf1eu*BD*4uSBX^gf-wivIC-+2K`IrHL9p-x^|cxgvH%$KdwTpXj)EV9JoaNbO2<{0B(8C%
v3X-Yh0L9l1ozlW0q}Mg5?BNRS9>?!0YyQ&CtZ(Z1<a1|2dn~lN2qPel;Sjiohe6zzy|7?&GI=oG{9-;F_twPg036KJAfXfXmn?R
jVC*SNo?Bn`rLU*h3W`A3mUW^PT`>82}%X;IQ<GHX_lu92~W1GD(E9oA5>Bmli4D6b4kCt0Zgw1NEYQ<u@T{+ewE7+o#udrT2RO>
;#@orSi{}_BW*kzWd+z@dG3Z$7~M{A5GZ2dnU%EF_*0QaE-;o{X)ytO^}hxSR^&78k(SEjk(q|+xfb3-xna2uUQ4n~jp#*fJoqFV
gTLgcA>e-%lK|8rX?KEVszTw3sT`eGZGiE>m+XhI?uR}g{yyzXzp54QP04!v7w{!?*#i#&3LgGU;isy*KK<Spe32s-)}6gidu!-Y
$D!L0ol+g1tJOrF9HC|9lw$RKTPqEZBadW?PXYx#JpRzK<O(J9)hGP@NIz73LqAmf7NoJ>$H7HK^Zl}!F%QDqd9F<HFUmR^sD0o@
*o+H(KzK{eK>Ko=p@Jimw{BTUGi4$&!OqcnI437Tpf&!5irO{VZMYb60T&C%?Mw7E*PxZleZO_K%=cTg`mc6Lp0Wcd_Nz~uT{d(v
s@3y~{!uGK>^GNHid=QNfu>N;gn|S6E4YJ6af_DeM~zsxvjgD%@zZ7(1Zu-xI)W@Z1CgONuAMD2=nLXcv>3cCjG)1_tQV_<&##fP
T(AO;!QR{bYp`8*o`*psna$A1X@V7^KfQ6qygpG(2VU8!DlVPDD=IFr=m)tx*?Uz#-8<C`301#048h>aS9{q1D}sTJstkiY55^Xs
WmDvAnb^FtuX_NTmh%;t^ECn^m0MhQFCt;#?JajNxxyXS;%)s}xIh6<QNH!Bxb}@E>j+3WevWhBeA?9wbP#ATwhJ*n0PHJ9SK_01
gWkvkDz=TbPvYYz@#YgYgX{@8tOoj{?rpjhI9l)o`dk7=#vm<<j@7<$Up%v_)Ew7U2^=o%0VJMOcK%2UmnS|+6cSn+^7RXxIK|I^
?$=`Ag-}CP=X<f<$@_Yjlu{#Qj}dfKQU|vnuxt2L6Sa@;-ktn4d|h+I-;yN&=r$}2!Niw_A0uAL)}CrGl$?AmI2<F-1xEzQIykdG
iQeApy**$Vp+khADyV5GP|>_rQe=q>_zOJJFwOGGGG3z1Q1ond5K3pGuOdGG5kzdFSxKS^RhHkP2oFq1m*9`MlE5$$SVq1f#SV_b
Y?p!_vs<R@mV2i>7X^{V;=_bojl>fdT>6UUIvWy8Fir}0Kam)Aw6iC$#nRg~@CsPJ?t@Igm~;J!_mrcHIe3&9kURjJ%Fo!uh{1GX
ljM;;Mzt_XR{12GyRB}oHkK-IdB7Dk=wKc^`XL|>I(m>XNPo3VG8+I8k4?ZK$>epq3PctpZi-aRqz$|wYR5Il*{|K)M72Q<xPp{Q
4jw`<_>g<-<RAlf+pkSdKE6J`rYoG9qdFcuq`-@lJb29QOuKO@Fp6Cpem;41J^Aqd?H3+6`EYV|RTH!z;>xkG>EmxGQDLYHXSK1z
B_=)8*Gd{A$rYRpM!<dr10d;Dw<=R$uMaOTka#tLtWJHHt~hZ~bx~B+E<oDV1c^K}{t9EbHZBiybxdV5)Mnwb34C@CMAO&@d)^Tn
)HIq*q5?ROO%tNXWFlp4GC^*eOlrr>b#ws%?qitECuy(<+$=CJA+G1(@NgVfShp)T_3JaNnYw8j2I<Q*jxqe6EZ`*I(ZqWQIL(U;
Zx$>vx5BBr0B^`mr}KlG=yDYuTgg*Ck0YyoYSpi-t;r9p58U29Xtoc!AU@s5hnX!{ZtA8_Rvay!0MrLJg&B`Qd)-dnH2jN;x9>mA
@AI?p_EY-{aPhmRPitYB7lOiy)9^OL`;sMCfhpdg#3}eS0PT7nSTnHKt;%hT1yft#Lxr=a2_l*!f>t&ULFM=sGP{+}F^0*}OuRWs
gRiSFrR$Q)&Bjk}ATED)1Mw>tBdStyg}~FM2A1p5BS}h#(nS$q5}*mk{(~A;S+pL>m162fafEb5kt&v}1<>{V`)ih56Bx4qW^+Jb
W$|JSEP0R+seoiBm&140ldCr;vex%neYe%>w1UG<^U$06t~YbNMyuPOHG*EZ)AGG(zuWY^*3|X;?cQOp7X-a&zt?m-e!t_@ZlXUw
zB_+^DMzi2X!S&^58C*0_}BZthp)M=%hjTd?$ztzJK3iD;+qJy8h8~o#T=8%;oITK)o}9a{pAn@+h#Q`uK7%Tt2Qp>IN12-;!M0I
Vg3N_U2eE{71eP@;{G{@ZoR{yd)Sw29JB4p<>bn(ce!#(!(ZADTHy+|5H7)U(b}_gU2;PwrEpM4wFsA%gA4mb$95`<Nu0gc#`Vsq
rnP;I(EALk9D~xZ!19{ooPD@Kw#MHT{m$3y)$Q2B!X*Pfw3{#Od7W+ODaE!)o+bhVS@y;@JA;4>|CLCb!7UZnSWKxn6&zJQ5vPJ}
@jwKQ;KD5zZlM6qx3bNNpo?VgN}G-G6b2}RJB6OkOMl=6IW(UXbwzW4%?Ke|Tl>-)5g>uxMYB#Hb^OqKpd7^^?ZAqMaKLrj8+!>v
ZV7I^)2$)4-sx5iRyj>Gz>L6Gt|D}__zt7R=qBZ|Ud-tO`bOZGclKg*I~EtC*%*xr>Wd$+)|YxevG1JG&tah;hTxZOp^Sk0`ah<-
kgfMu>;3uKU~e*Df&C_~mrc+pLv8v*tQJnm;zWM|ZGGq<vNgu|ab`UvnLlMH&L%zxZoKNI;L!w-+#0;v9-QL!Ito}f<#97miW9Vz
mH`OuEf8}AQ5-ZlWUx*U;<gvS8Ux|ZU=T3h&NIh-@Yr!_^W>>rdo3k_*=PocYq6AuoEogdEc6xuo-uzdFYN{}^itYb5YAp(@x?Py
lr!h2QtZLFH1$A=2tHRX2(xc=q8|843TqG!SSsJZ?;{Jy4;FAzF70nxZUK7xl4`kqiRQcQFH!y2RR7WjdFG%>LXa3gqF<7pcp;#c
S_yRgDgFTa-q>K;Hs}lcq&5n>ymm^CT!Z(z-uKsJ8bBw)V=4UQCPS+EChFEteIic4V1_s3uN_rcadHa(6#5`^=DK(RW07INADKk)
WD$cB0KR+7Q!v2fNZ-YNty1cou42EI!Rg%olia{f55xo7gI0T4+sePHIaLothsLUQs8=yRr7Sf*08dP(#d8K*?41-~lMU9Dl5@Ri
*Vz@7vfV7nay9}j4?Z?{-_3?-9f{WAm^z=0x*gSkHbEb30z3$(N=Kn_j*?IZG)S(pVd3nKaGa=-?L8v};~b}V1}7~Ne8`h6apH(m
9B>~5i4LM}3<3#U&Z;J960Pnut&~MG-XEPJ-sIF_f<WQ4lY3Bcx`*$y+l^E2+oLf;%rWYMH+G<1fMrkV<dETKgOYPFEWpU*0zp<8
h%6=wcPvoGrIK$5$gZ21j;29z5dw2PPAD}gLJ=oxJOE%khST^qb(48GWee3p2B;B_!)Xps2rK9d*8{Aj+6QsBio!VEXk>zkD0rCA
$^oT3Kr~MYBDyKfqV7cCcdPtvZEas#5#bqHaZS;}&_a;lg&~qP_AplgzLN1iQ)K|25T%=dG({sgD~%SglE~TPF(l)3#6|nH1G=1`
(?^8euc>pVWFz&Lm4jJ3&ZKwX2kiNg;>8=;OcoY8TWNF|wB>UXidq~}7o38cTv^_34BUSTB|PJN5+J3<$xZ)FwmL_2DBT@Sco8?#
JvRMsY2KB9q7K3&m+X=#J5}4q*=jZm9|i0-Zu-cs1R+opLCyKQ*TWA(_<5)66-Y;2@8R~C<Y1r<QP$kda<5@Nhue#7rOw5+D*mWm
mTK!me%Ds>T5KEDM)>cmQ-){VGU4e5pPd<nr6%At=c~-7BdB6apgXh}!Z}!=n%6c}adbAK!6-X9%n3g8bdF4YuZ)6ORYm|V6emMu
fnR@hImQyI2+V#+iJA)VR)JPiy($5KGfF~KB;asjm77ge(j)6$>4D#DE9@OHorj=AG5JSTsemDF8Ja?vsCBOpyQ&#sZViD+89&Gk
8T_|&IV?4l%<tk13um<=B<UKVsVm9w#YZfBgu)vvynzC(Rapp7#U-dOLZuZ)su~+bA{gJ$tXw%+b?JDL4-~|8%{bPDt}5eLXms%A
OmraBV6irsispB><ESMl66sh=X{FpfqxAlfIWcWR9TyH_vo^wQ1;Jb^(hz_;e6~2Ks2z3=E*d9aMHh*Dig=22if|^y04QvfE?nTw
FIL%{qN9d^s17+Cn{q4~AD}^+hG#P}K=Ty?ZHF4%JRakq5$3D+F|;8@Jt|>xb4T>W5gkh2;lBm{{R<3cb9T)*+UZAY@=};Rs;oks
Jq5SoZ-KuixaL2CYwiZ82?T_X*J$IW@lq*o*cLXFOIuj2r%p&X;(3FZ90y)B<H|l&F&(>A6H@#zPw8c`rpB}yRe}vY!IA&9uEJ;<
fO%)1?w_=rmo3smr<kIMp^<q&TO%xr24Ss>$-E$-Fe{rvK?fyuPozZi>e2?Yfqjxw0YG^oj5WfUBC~`6VK!~#yI>lTD70dp5bPQ2
v|c}HQ3}KX4SpSyWthN3#xO6&Li&VqDYNpJhL@R@b&Q#E;4j8#r}ZbeHGha<#rjqo(kk!0%cQ%LBI&LOzx?rs!SvNUx<CIsAdzgJ
I-)4!@*R#V3=K+wP=FK5l$zu*6<WJU)+|T{h8O@t%L-$;e+&9!a%=sc*|q)*zk(NxF2SX(@Vg(AsZzLXT6K{|*x)nq++qmu((pKT
fUn|GXu^Lt&z4+u3>xunNlAxGd$4Nn$cv?eq&(UGTEKNN>~`n}#7v0}w=WjfI*b>b!_W4-PF)qsmRFWFe1W#0gxx|6kmaougBmtr
a2Uu2x{pTpLh)S7skis$<DZ8hbmA-Z{~i06EB@tKiI=pwSE!4>Ksij_4qyK<ykrycC$=9?^;7e2=|<rUEMxio#{ewnO)J_N<Z%vW
U_-eK+6mK{v<R0iIqjqq;Hp=igkZ#yIa1i<`ySoV?Rz-s!7A}_->9FOai26k*HC0j;W<JuKoD&8wr-rNp8nWaAL+HgU26Hxt`OZ8
(;5UJD`{?_yhcQ=dT(Xfo5Xl`em1<)H;KEcpiwZ{9?#pRm9xKT<LuPHj+EU#YFTYXRKx$*Z!U*;XYlU&^8MSZNw+^aJ-NJ6CWW!w
Vxi^=tG2^0T+(gcLKSy(=OA5?+3+Bi?}6sQ^gct)q;7B&^7`fub|nRV4Jn=eYU74YRBzx8tdCicnHNc<O(@WmXV!G#hD(qIn9~Q2
{Y}JT1*91(oPiaV7{WM(S{PAoqV>ko@hkyyCJll*U((Ta3fPfoT3SXt*O~=EE>H~BabWOheFRv+*Oj{fXAz-rME0eRPm}Oe@`#&g
x`;EpwF7UnGJ@nFW1k20={$y=@X1vHd*CHZjpxWx{h$6{_j<qbtm$X3kIZ{Le1-Jv-JWr)$Jcz7yFI~)B1Hxx1xdHwBJKa|EfNQf
HeVy<dpn*Z`2jtS64Rpd)~%L$w^W?p$D*r|i}3g_G7%KO2TIC=kxwKsIYO<o<pmd>xbOr8jH}Ho?|13y>D{7gs;j2veVV&Bt$TZ(
aQCP6)?S&*u>fAmrfw2Uh|P7*zCbZUsHj|#ioFy#o5`-@0k0sF--Bbln$IIlf5qDu%z7Pfj`>me13UBKpGk4w%x~8z#|Wp$ZdV^t
m5K_^bXOl7;3)FkjjSoXOxlT!40pB8QGoYCjKVXS?YnZ?)#R(OTn~ONH{DPQI{6E`IrtP~PwiH{NsbT_Fz^d~>{hcOKPzlG=^Wn@
#CZ-T#CMmo(RD1!tEQe~)wD<@_jD>bERJd!$VT4&gVeiJHM99@L(e>#j^zU}Eq{7r^eqq<j{4#qRM8|JoJvmm)Qr~Q@~{#1gjZTw
3vYqD-xTIH=&>cUy2z>C7#xRU)`8m7ec4o-3g?2B4abAP@B;vh`aspFR^*9;iXLEc`1j!dkrw{LSQ`S-k+xmOkEdPbMLdmyvWyLV
ASUW%1J}|A)>8bIs;UX+WM1m|F>kfx`Ep*E61JOWFnUvVKi*vs*o5Mwq^@+@ziOfE{OUYF?VVf$t2L%Y>5i}j0YsZ;2Nt|s$(Owb
CPZN4)7c(FPY?AaF<l#%SA<L)S`NPk*_^l7_JlTA>h}xOuYALxRktkONs;_}=6NSDtY~qtAaTJ;(Zc9dKUo9k%qyuX=u1=HDUZRa
Ax#L7t?>Xvxq^g#sWlYyYgJ)HuE}CapZ;y0MWm84$z3~F_SD>6%(4WHChaAmEkZ$z(oO`skOK|M83I-XffObSeqO09GCGJTN2#Td
gfmynJTaSYJ)%9+uVz`{&Rlv{NRN(ZQ_O*;2WEv?pf5IJOlXcOLJv?Umy|A7!Q`0Xqh-@_pxdjNSJu+SvZ|hz)%>JS%>=Xj);LBa
fQO<1PJ;dGO#wyS3FE)yP^MJ-`+N`j>d;53QctQcZS{W9vxPE<iO=532qpq6_L3!_zEalPP5VvsRMzptcsOY&)Mr@xj98lp06ms*
wDCYU*>x$5OFiQhb&&w;Qn|%ahTA-&&BHdmQ#dD2gxd4Cg7b(Q#{2}QxSBFFj2iiyxf9i8%OQu$f;@Hc-!yPRI->>e=Ikk0emI*2
6oFu$0gV3;%zQ9>fuF&q#Cs#%ba2BiMR_L|^W_lTDLLXCV}j@Ol!|r`U*}v))v6U>=w~GlD7{ClzL8vnuYvJd4v>={{KuUA;OW8?
3dSRyYhw0mPG+ERVZ0-Sft~ZLd=B|ZT$`RQwvo1=LQ@x7;{kM(s&!Dl?Lpb8uM{-b=9qr1?tyV7*9LsbyH;I_3~lZOb15NaUQHPG
7L6>^zK!lWuC`;IYJT_jOx2hf0QkZQWw?!iBR&+pu4I-$mkaX_Or7&D_(+`JLmTHcb+&1a5a@n4d!Xzz`k~@{PQO$xZZ0>{|L%pY
q3uqkN$^$ZPG;haDi;&fW|CPcQEVCK9KF;3)&>WjRUTYg+!{H0wXiUUepIR(Liky>+l&h{D3Ac(dW#bATNF-yyWExiHsd$Iod0%N
B*4wg1UTwp-WeB(Jh&iEhznT2Q(oN6K{i6<Nd&u#Og@`7S5oAer&Bmwi#0Tz===A^aaMg7RcV#b{7`A%cr+C;Q5m($W2vO_Qfjwg
z60NDtS1FCiY5j1wW>aMs<Z-1tA}cPx$@>uS577&h+PpsL?DBoe>4?}JBb|!$g13Vu=Rv02P&H{r-aT91g1-fU8#Yi2|kOqwMrWF
Fli8<qkq#t@KdZA$QlX&<SPN81_bgAYYpas_TmDD7%UMf{;M7-^Es1*Qx3nu?>Cb}TK|ee=EZwlezyuc<Lu;>`NQsxh0qf#F`whD
pO$at8!Nmk7PXJ?|2MU<8RD)yW6B=H>OssO#uW+6`4z@g^qAm*|51XBpDwJ_=ZZh)>T^DKOo6+Vv|-r5h0HUAUXsYoh{%`n?UE?q
7J*q9^L2a7FF$N5Azl~|cfE5eUXy5(gM*2aX}rP!3jP}p$|`fjEO0rMF9F1Yi8hDTU%KlyjB8E;E#Xvb8jxSGUlV1M$hOW57@4F{
B$%sv^v!om|B`&0kDH250<N5r$%hFAJ~NplLf2jBy03{y;*4Q%%D^_|${rWh9_HJY&2+;wn9>A=O;%ib6z`vo*&HM1njRR?t;fKV
>V>;;`GN1Gsu_m=E|1CEN?*c9Rh&FkzH7qIT~C{!@9s+pmEM|GbCrrWQ_q9nN>SSNe#%JoLb=ErTI4~PSrBLE@6NA>JJKJ_<B*yO
515&w$-eQuo&Hdr<!bnL`09H2dh+W1UmxBMp{BeSQAj%UGHPRz{f$XDdyX$=)Tn=VbMoVV{tq}&gMa
"""
def main():
 raw=zlib.decompress(base64.b85decode(''.join(PAYLOAD.split())))
 assert len(raw)==20557 and hashlib.sha256(raw).hexdigest()=="f32a1e177619b3ae89cb6bada09a2e6cfa5bf0e72d887306b038236a0c9779a1"
 files=json.loads(raw);assert len(files)==4
 root=Path(sys.argv[1] if len(sys.argv)>1 else 'RESERVE_RELEASE_CLOSEOUT').resolve()
 root.mkdir(parents=True,exist_ok=True)
 for name,text in files.items():
  assert Path(name).name==name
  p=root/name;b=text.encode()
  if p.exists():assert p.read_bytes()==b,('different existing file',name)
  p.write_bytes(b)
 subprocess.run([sys.executable,'-B','-S',str(root/'finish_release.py')],check=True)
 manifest=json.loads((root/'RELEASE_MANIFEST.json').read_text())
 assert manifest['stream']=={'bytes':48631,'files':13,'sha256':'7c11a2517ada4a3bfd8b11bc91cec5535132fc62eb56a0753c3bea637b6aa016'}
 print('RESERVE_RELEASE_CLOSEOUT_COLD_PASS')
if __name__=='__main__':main()
```
