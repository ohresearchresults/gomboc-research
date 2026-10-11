# figure-0528

Historical AI scientific report · saved 2026-09-24 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# COMET64: four junior cancellations with exact preservation of the parent's physical volume and first moment

## Disposition

**A new rational, uniformly filled, finite body was constructed and fully audited: V/E/F = 120/207/89, C = 414, strict (S,U,H) = (1,2,1), additional weak = (0,0,0), P has one positive bar, and Q has none. Its actual volume, all three first moments, and centroid equal those of ATLAS62_HPRUNE57_G6 exactly.** It has 42 spare true edges under E <= 249. This is not own110, and no own110 result is claimed.

The four original junior unstable roots 76, 74, 49, and 42 are absent; no new U replaces them. The two remaining U are images of original material vertices 2 and 109. The original stable heptagon remains the stable carrier, disjoint from both U. This is an observed finite endpoint reduction from own165 to own121, not a claim to have certified a continuous path containing exactly four isolated bifurcation events.

The primary body is `NORMALIZED64/RATIONAL_OWN121_PARENT_MASS.audit.json`. Its immediate rational predecessor is `SIMPLE64/OWN121_FIVE_SIMPLE_PARAMETERS.audit.json`. The latter has the same class and complex, and exactly the original centroid, but volume V0 + 1/1024 rather than V0. The last rational normalization removes that volume difference without using a nominated centre or changing density.

## Input authority and a necessary source repair

The literal parent distinguishes its accepted own165 entrance from its unexecuted finite reservoir proposal. :contentReference[oaicite:0]{index=0}

The supplied journal was read through EOF: 1180 lines, 164277 bytes, SHA-256 `60ddefdad06a6cc2740f19ad27b84fe1dae28e633b5030d55d2c6a7300c8f7a8`. The required literal parent is `figure-0524`, advertised immutable SHA-256 `3a2fe93659768c29265f3227ca0398a0e6b4e5eee4fdab9c5eaf7a3767437eed`.

There is an outer-byte identity limitation: the rendered parent heading-through-EOF span available here is 36812 bytes with SHA-256 `e1454f60b03703f04098c3eb2414bb7f5777a92283bffc11ebf7730bf6c70027`, not the advertised immutable digest. I do not equate those two serializations. The complete inner `comet63.py` block is independently recoverable: 18735 bytes, SHA-256 `833e0a0a3949c8b7dea20e6dcaa50851ffdaf25417a232fbed9d18d5d41190a7`. No coordinate, incidence, or class disagreement was found in that inner source. All 57 H rows and every required exact helper are embedded in the recovery capsule below; no old decoder, historical archive, or research connector is needed.

In `complex_from_faces`, the parent line

```python
n=tuple(int(t/g) for t in n);h=int(h/g)
```

must be replaced by

```python
n=tuple(t//g for t in n);h=int(h/g)
```

The original integer true division passes through floating point and overflowed on a reservoir candidate. Here `h` is a Fraction, so the remaining `h/g` is exact. The repaired file has 18731 bytes and SHA-256 `d10b4af88b17e7ee8355cc0ab4de5a5af99da1717d1ee4175cfaaf54baec8702`.

The repaired implementation's tetrahedron, cube, closed-weak, false-weak, parent, and five material-gate controls were actually observed to pass. Its first accepted old reservoir trial was j=10, epsilon=1/1024, with 114/192/80, own165, weak000. This converts the parent's previously analytical reservoir architecture into an observed finite construction. It does not make reservoirs alone a cancellation: all six old U remain in that trial.

## Exact recipe for the selected construction

### 1. A small-integer three-cap corpus

Let K0 be the supplied 57-halfspace body, with the source convention H_i dot x <= 1000000. Compute its actual V0, M0, and g0=M0/V0. Starting with the source's lexicographic parent vertices and canonical maximal facets, clip in the following order:

```text
( 614,  -697,   710) dot x <=   1000
(-46969,-108788,-24662) dot x <= 100000
(-165, -1235,  -118) dot x <=   1000
```

The order matters for the recovery program's labels, although the resulting intersection does not depend on order. This rational corpus has 116/174/60. Its actual class is **(5,2,5)**, not (1,2,1). At the parent's reference centre it is (1,2,1), but that reference census is explicitly stored separately and is not its physical classification.

The exact discarded original vertices are `[42,47,49,74,76]`. In particular, this selected last cap does not discard original 58. The coarser preliminary cap `(-73,-1257,-84) dot x <= 1000` does discard 58; these constructions must not be conflated.

The selected corpus has only 60-bit maximum numerator and denominator lengths in its rational vertex coordinates. Its actual volume is approximately 2.4012135178660876, and its actual centroid is approximately `(-0.00007312475950341558, 0.0002605787670609731, -0.00005238810306476567)`. The centroid displacement really creates four positive Q bars. This is a useful low-coordinate-complexity nonrecord body, not an own121 successor by itself.

### 2. Reallocate real added mass among four actual, clipped bases

Use facets `[0,8,27,37]` **in the clipping-order facet list**, before the final canonical hull sort. Their actual polygon sizes are `[9,5,10,9]`, summing to 33. These are not four guessed old polygons: the polygons on parent carriers 27 and 37 have changed during the critical surgery. The code computes their area centroids and area factors from the actual clipped corpus.

Write the corpus's true volume and moment as Vc, Mc. Set

```text
epsilon = 1/1024
Vstar = V0 + epsilon
Mstar = Vstar*g0
ep = Vstar - Vc
c_added = (Mstar - Mc)/ep
```

For the selected coarse corpus, ep is approximately 0.0018483226764124743 and c_added is approximately `(0.0970361287645736,-0.33495095009986464,0.06102231909055584)`.

For each selected outward base plane n_i dot x=h_i, let c_i be its area centroid and beta_i=area_i/(3|n_i|). The exact code computes beta_i rationally without introducing square roots. Solve the four barycentric equations

```text
sum(lambda_i) = 1
sum(lambda_i*c_i) = c_added.
```

All four weights are strictly positive. Approximately they are

```text
[0.122331483269459, 0.123212772594357,
 0.357961471543735, 0.396494272592449].
```

Next solve the exact rank-seven system in twelve direction coordinates:

```text
n_i dot u_i = lambda_i/beta_i       for i=0,1,2,3
sum(lambda_i*u_i) = (0,0,0).
```

Flatten the coordinates as `(u0x,u0y,u0z,u1x,u1y,u1z,u2x,u2y,u2z,u3x,u3y,u3z)`. The selected simple rational solution fixes the five free coordinates

```text
indices: [5,7,8,10,11]
values:  [-19/5,-4,48/5,1,-7].
```

The seven pivot coordinates `[0,1,2,3,4,6,9]` are then obtained by exact RREF. This is the complete non-default direction input; it does not require the floating optimizer or a missing checkpoint.

Set p_i=c_i+ep*u_i and add the four uniformly filled pyramids on these bases. Their actual volumes are tau_i=ep*lambda_i, and their actual moments are tau_i*(3*c_i+p_i)/4. Consequently,

```text
sum(tau_i) = ep
sum(tau_i*(3*c_i+p_i)/4) = ep*c_added = Mstar-Mc.
```

This is a physical volume-moment identity. The reweighting of the base-centre barycentre, rather than merely using the old lambda values, is the useful extension of the COMET63 architecture.

The result has 120 vertices, 174+33=207 true edges, and 60-4+33=89 maximal facets. It is own121 with no additional weak equilibria, not merely a solution of the rank-seven equations. Every global supporting-face inequality was checked, every apex was checked to be beyond its own old base and strictly inside every other corpus halfspace, and the four pyramids were separately integrated. Their independently integrated moments and volumes agree with the target exactly.

All finite nonincidence and mechanical sign guards are strict at this point. Therefore continuity also supplies a nonempty local five-parameter, actual-volume-and-moment-preserving own121 family. No quantitative radius for that local parameter neighbourhood is asserted.

### 3. Preserve the original parent's volume and moment, not just the scaffold's

The preceding rational solid has volume Vstar. A further rational affine normalization gives the selected primary body with exactly V0 and M0.

Set `r=V0/Vstar`, and let

```text
D = 1000000000000
k = 999864520782
q = k/D
A = diag(q,q,r/q^2)
T(x) = g0 + A*(x-g0).
```

The integer k is recovered without floating point as the largest integer satisfying `k^3*r.denominator <= D^3*r.numerator`. Thus det(A)=r exactly. Since the predecessor's actual centroid is g0, the transformed body's physical volume is V0 and its first moment is M0. The third diagonal scale is approximately 0.9998645207824215. This map is near a similarity but is not treated as one: the complete exact hull, mass, and mechanical audit was rerun after this rational anisotropic transformation.

The observed actual quantities of the primary body are

```text
V0 = 2.402085278042500091809311337796462370794...
M0 = (0.000003764385813739907551110836436380866454690...,
      0.000006605136076622687942955899471403501045341...,
     -0.00001300079966554258537181847293413465077466...)
g0 = (0.000001567132461178717684823756244199310585226...,
      0.000002749750867298651866864725561947337203879...,
     -0.000005412297300342790843937147023878787317714...).
```

These decimal displays are explanatory approximations. The capsule regenerates the full rational values and asserts equality to a fresh integration of the original 57-H body.

An additional exact algebraic companion is also retained: use the positive common scale s with s^3=r, and map x to g0+s*(x-g0). Its mass and class follow exactly from similarity invariance. Its recipe is generated separately; it was not presented as a second independent run through the rational auditor.

## Observed verification and the complete remaining positive interface

The full auditor merges coplanar supports into maximal facets, reconstructs true edges with two oppositely oriented owners, checks connectivity and Euler incidence, and rejects unused/nonvertex input points. Mass is checked by tetrahedral integration from two origins and three coordinate divergence formulas. The additional independent certificate integrates each of the four real pyramids separately and checks the gluing halfspaces. This is one full hull/mechanics implementation with supplementary independent checks, not two independent full hull auditors.

Mechanics uses actual g throughout: physical outgoing dots at vertices; facet-foot relative-interior tests; and all four mixed-edge quantities `(t,1-t,normal_coefficient_1,normal_coefficient_2)`. Closed-weak classification is not replaced by merely finding a zero among otherwise failing inequalities. The primary has additional-weak counts `[0,0,0]` and primitive-zero counts `[0,0,0]`. The polar-U test independently agrees with the stable-facet projection census. The P and Q computations include simultaneous tied levels and full positive interfaces. The separate certificate verifies the cut and attaining-path bottleneck identities.

For the **normalized primary's own audit labels**:

```text
S = [37]
U = [2,104]
H = [[110,111]]
stable polygon = [24,30,31,73,72,58,38]
Q positive interfaces = []
```

The stable polygon consists of the images of original material vertices `[24,30,31,78,77,61,38]`. The number 37 here is a final canonical facet index, not an assertion that this stable polygon is the reservoir base labelled 37 in clipping order. Likewise final vertex 104 is the image of original 109; final path vertex 109 is a different, newly created vertex.

There is exactly one positive P interface, peak 104, elder 2. Its complete current component, cut and path are:

```json
{
  "peak":104,
  "elder":2,
  "component":[58,59,61,68,69,72,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,119],
  "cut":[[3,101],[4,92],[12,85],[15,100],[19,95],[29,89],[31,73],[32,79],[33,87],[38,58],[41,84],[42,75],[42,77],[45,80],[54,68],[55,61],[57,61],[60,69],[60,108],[60,119],[61,118],[63,68],[66,76],[68,118],[74,76],[105,118],[106,118],[110,111],[110,115]],
  "attaining_path":[104,103,78,69,59,110,111,109,39,36,116,13,11,1,0,2]
}
```

Its birth is approximately 4.026525405457943, death approximately 0.6633356672519483, and relative depth approximately 0.8352585416814212. Exact recovery is particularly simple once the rational vertices have been reconstructed: with X_i=v_i-g0, birth is X_104 dot X_104. Put a=X_110 dot X_110, b=X_110 dot X_111, c=X_111 dot X_111. The exact death is `(a*c-b*b)/(a+c-2*b)`, and relative depth is `(birth-death)/birth`. The full rational values are also emitted directly.

**This is now a 43-vertex/29-boundary-edge senior interface, not the parent's 41/25 packet.** Its relative depth has worsened from about 0.8287164863643938 in the parent. :contentReference[oaicite:1]{index=1} No old separator certificate is transferred to it by alias.

## Finite body ledger, including nonrecords

Every row below was actually run through the exact own-mass auditor. All have additional-weak and primitive-zero counts `(0,0,0)`. The capsule reconstructs each body's exact vertices, maximal facets, true edges, volume, all first moments, centroid, complete mixed-edge census, and every positive P/Q interface. The reported audit hashes cover those complete records, not just a summary.

| Body | V/E/F | Strict (S,U,H) | P/Q | Physical mass status |
|---|---:|---:|---:|---|
| Parent | 110/165/57 | (1,6,5) | 5/0 | parent mass |
| Old quartet, j=10 | 114/192/80 | (1,6,5) | 5/0 | scaffold mass |
| Alternate quartet base | 114/188/76 | (1,6,5) | 5/0 | scaffold mass |
| Exact edge cut76 | 112/168/58 | (1,5,4) | 4/0 | own recomputed |
| Coarse H cut76 | 112/168/58 | (1,5,4) | 4/0 | own recomputed |
| Mass-fixed cut76 | 116/195/81 | (1,5,4) | 4/0 | scaffold mass |
| Exact cuts76+42 | 114/171/59 | (1,4,3) | 3/0 | own recomputed |
| Coarse H cuts76+42 | 114/171/59 | (1,4,3) | 3/0 | own recomputed |
| Mass-fixed cuts76+42 | 118/198/82 | (1,4,3) | 3/0 | scaffold mass |
| Pair74 cap | 112/168/58 | (6,4,8) | 3/5 | own recomputed |
| Pair74 cap + cut42 | 114/171/59 | (6,3,7) | 2/5 | own recomputed |
| Alternate quartet + pair74 | 116/191/77 | (2,4,4) | 3/1 | scaffold mass |
| Alternate quartet + pair74 + 42 | 118/194/78 | (2,3,3) | 2/1 | scaffold mass |
| Pair49 coarse control | 112/168/58 | (8,5,11) | 4/7 | own recomputed |
| Pair49 exact-two-vertex control | 112/168/58 | (8,5,11) | 4/7 | own recomputed |
| Three-cap core, exact cut42 | 116/174/60 | (5,2,5) | 1/4 | own recomputed |
| Three-cap core, coarse H cut42 | 116/174/60 | (5,2,5) | 1/4 | own recomputed |
| Four junior removals, exact cut42 | 120/207/89 | (1,2,1) | 1/0 | scaffold mass |
| Four junior removals, coarse cut42 | 120/207/89 | (1,2,1) | 1/0 | scaffold mass |
| Five simple free values | 120/207/89 | (1,2,1) | 1/0 | scaffold mass |
| Rational normalized primary | 120/207/89 | (1,2,1) | 1/0 | parent mass |

Here “scaffold mass” means exactly `(V0+1/1024, (V0+1/1024)*g0)`; “parent mass” means exactly `(V0,M0)`. “Own recomputed” does not mean the centre was held fixed. The two low-grid early root cuts are the extra halfspaces `(64232,-75454,41850) dot x <= 100000` and `(-46969,-108788,-24662) dot x <= 100000`. Their exact-t versions use the edge fractions printed in `surgery64.py`.

The preliminary pair49 controls are important corrections to unsuccessful local searches. A single cap `(-7275,-125689,-8377) dot x <= 100000` removes exactly `[47,49]` and has reference (1,5,4), although its own class is `(8,5,11)`. The coarser `(-73,-1257,-84) dot x <= 1000` additionally removes 58. Neither is an own154 body. Thus the failed one-cap searches were not exclusion proofs.

The alternate reweighted quartet `[21,26,29,46]` gives the useful 114/188/76 own165 scaffold and the larger-cut own244 and own233 bodies. The latter retain one extra positive Q bar. Their complete rational free-coordinate seeds, actual moments, and full interfaces are preserved by `extras64.py`; they are not omitted because a later carrier works better.

Arithmetic remains a substantial cost. The small-integer three-cap corpus has maximum vertex numerator/denominator bit lengths 60/60; the selected simple-parameter scaffold body has 28482/28486; the exact-parent-mass rational body has 31242/31245. Five simple direction parameters do not imply low-height vertex coordinates. The main value of the large rational body is its exact actual-mass mechanism and recoverability, not a claimed global coordinate or edge record.

## What was tried, what worked, and what remains

I first inhabited the literal parent's four-pyramid construction, then made actual critical cuts rather than attempting to cancel roots inside its unchanged root-free cell. The first two exact successes were root76 and root42 cuts with both volume and moment restored to the scaffold. Larger whole-junior caps exposed the central physical issue: an apparent reference improvement can create several actual stable equilibria through its centroid shift.

The useful change of method was to choose the added mass's barycentre from the actual removed volume and moment, recompute bases after clipping, and search real pyramid placements against both convexity and mechanics. Numerical escape-tree and halfspace searches supplied the coarse critical caps; numerical four-facet screening supplied `[0,8,27,37]`. All accepted inputs were then rationalized, reduced to the five displayed simple free values, and fully re-audited. The numerical optimizers are not part of the final certificate. Their complete exploratory sources and the reconstructible 7314-quartet numerical library are supplied in the source archive for continuation; the inline capsule needs no numerical library to reproduce any listed finite body.

No continuous, everywhere-valid deformation between all ledger bodies has been certified. No claim of global impossibility follows from the fixed-weight, alternate-quartet, nullspace, metric, or failed packet searches. The rational endpoint constructions and their mass identities are the established result.

The remaining obstacle is constructive and sharply located. In the selected mass-control family, the two surviving critical stars are not altered by moving these four apices. The current core and these bases therefore cannot yield U1 merely by retuning reservoir parameters while retaining their independent-pyramid complex and actual centre. A further cancellation must change the senior critical geometry. In parent material coordinates, the surviving 109 star uses neighbours `[99,107,108]` and inherited carriers `[33,34,47]`; in the selected final vertex numbering its root is 104 with neighbours `[94,102,103]`. The current 43/29 interface above, rather than an old 41/25 alias, is the appropriate packet to use.

The most useful continuation is to operate on that remaining critical carrier or its whole current basin while using the now-realized moment controller as a physical constraint. A truncation of original 109 alone initially leaves the four selected bases unchanged, but a deeper operation reaching original 108 will affect one of the selected carriers and requires recomputing/replacing that base. The 42-edge headroom and the large surviving P depth should both be retained in any proposed surgery. No such final senior cancellation is demonstrated here.

## Recovery capsule and exact receipts

The capsule is self-contained: it includes the complete 57-row parent input, the repaired full auditor, all listed finite-body generators, the independent physical/interface certificate, and exact output receipts. It decodes nine complete source units; none is an omitted helper or a request to fetch an old file.

Observed execution used CPython 3.13.5, standard library only for every exact construction and verification. The optional numerical exploration used NumPy 2.3.5 and SciPy 1.17.0 with `OPENBLAS_NUM_THREADS=1`. No stochastic computation is needed for the finite recovery below.

Save the following as `COMET64_RECOVERY.py` and execute it. Its decoded source dictionary is 45369 bytes with SHA-256 `74d275f67ff071d79fc918a48f757e599f620149c85ff0413a422a4a076ad35a`. The displayed decoder was actually executed and all nine decoded files were compared byte-for-byte with the observed source units.

```python
import base64,hashlib,json,zlib
from pathlib import Path
DATA="""c-rlKiE<k`vf!_<XJVHu3X<wRNLNRwEy~h7Tb3!w?HQWOs8cG5mw4!~!~edS37`%hlI(u-
cK5~hK~<q}Boc{4W+IXJ{<kQZEwVI=f<-d7&AsW<-&%i5XOmG4e#VO|nb~G78%-y(MXmXD{B;~BX>B+O;>I`_B}(h-
xHbzO{Ig(j%~SSfNe~ahC#bHWv;+TUJ{j*}fq4TmDwsc6ENA0dz<P`2beJ?gH6E2(I+@iTYuUIq<<C=m4tn)_1TRYF^?qNro{bmD
EDfTh5m5UbUsROvqKPP)#8;vmCC{@sVfVMm6HDL+^Yj|^vpTCs$#^kK;z8aN6Gau)sDFaD>0}tp%Aa|H$kay|YG3@kHwzBNV!b!m
dcWW9Y=Jo8pWpjI4}smO4~D@wo=3qnsrTCt{&!KR*V6k+>k~Y{-
=c!|yvu{=dNPX#qin3#`#%si%n^zlVK4)n5XiN+{ybSU!d^X^zyOZ{4fVd#j+P6*mlV}@I<+jVL1StkU*9Uf`S7BNmp;`L%;$ie8
W!EuHEd$J;6qWX#r`L3G){nKu)&!hPZo_YJxH4-!7XHC<rg3#Ui-
}F1;cDc1#5tu+U)nZ48bUPY&`Ume$h5GtoT09G=&y@s3BM^f^3|PuLe_sLAHQz&`saZTc<WCc~|4<$uLf4^-
8w^)zB#K_8cZk5;qzdyHON{!vW6-
$+v9Uz^WM4r?vV@4%j?N#{T!b)gSG}B%b)gY`$pVCxtRSTxY|ihF|#b)s{ZK>`f=r2G3C*G?53#Zdn^oh#Hd`d`I-
W@#9v6(|f#3M812Uk8oPU!S(%REg8-edMRqUr$HyA+{;Q4z!v`O1##TCR|xjKU^-34_*zC3b<=-
a@PLaMw$G>a2!^CV6Z%YLM=E>puLrXPpqwve%V+`21QJhG)=}ByVa$T~#z(pxCXWN;R|Dh-
^9Gew+MiYSL1kB}KZ2%VMkLWKj0*n<Egbl9235)_?ZXEu?n4vzli_ld_)r5ehDjFtS5#;^WogQQp61Z-
ENL7t1Yc=)*_lrqv3`E?;p~0KHupdNd8+B!;OOLYXTTE&X9wMb51orn_k1r{#@S*I8Dl*s?z3KNn2a0KsRFp4PNBJA>Yw#QS}P|}
ObDhxIA;6ov)}8t&pyDfU~#uB&1js*(1RIp^v2P_+s?%~VU=>+u;{6pBTe~N;Kw10d}ytg39_Z>^VDk@FbBteG@H!ljrlTcge*`P
K1A@Kw66eCoWWyC3#Pr>KBkuk9<uzdA_3j_K7dG+1!-?o%oGOm#81;+n)TZ_B6GjD0tDvh@ARnZetYC25-^S0-~-
pA$udizf;o)zEEr!UjS)`4on9|vjci9#{>O-oO0~*7MBn#pv}9LTReB+4IAth+?t-WR>+)r^L?}K-
>_fz^qH1}f82l{I@HyI<FGr2D&oF+U)tyfbjcKZGmU7?}f{N}b+XrM2qvfzs&dWG4O0xM347a-
EbbECU#005#SnmT@d71^I3|2TIZLubb8j97li}hZx3rWqVAG;q8-k<!da|jgOJ-
9geczW=DAV?d?xpR6k_;7H(LeKM6crIWOr*;S9$!ru1vv0v7gRB5ooCQ~taWEXf8aG^l3&4;|$(0J@zB7lPW&=rJmlAjrx5Y>rN@
=k@D^>NWk;4GX2BMxg*rxRwGN##Vz8H)qBfcK`{s(mvwl26RGn(8dvER!Cqn}nM*O{sy)lUmvxu7YIOb#Wc`pM~G=d1%irxzf6aT
M-7%(6u?SR{{&21!rxax|Scl5y1dUKcIG!Zic<3ZbMWKCpTQ+!QGjKd%ma>+JL947|IT;RCBL$21->kkFD6yC@>iW1rRKD3-
ool)nSJ2Hr}E;t>*ot}`5U80!aI;_&Ng8e}^g<OrrLXJrXU3NNrsvHGVXCkNourmR1JPr-sb0KsbRBe!Pr1TYsYCbPNU07;J3TXj
X*sek<nh({hjgK8V~w;zF3+vcG2<>2kbpfpH>vws2`KRFz{dw+Ry`i|&-
aBzAEd4RPew;jCgbT3YhPTn3|bk1R#oS)a39Gi5woL>_h&=%0eV1Od?VBq`p!2s94!Jyva>)_Y%-
`L+^eM=Sq2J*U!WFAC_xVaR}k3<4cY3<Y3F=YZ0nk^=iVV(&p3$roJy*Y!9PGVS9S?y{zSx&<zQ7W1Yhe@^aIJv_`nm(iCGR#8x3
29h-8Ns7WzKUX28%85m%jS2p1$33CUk7t6&1y*1tTum|e;vcm9?S|HO~An807zyKXII%`-
atP0b$nd&YrU^ykiS&bG;Ez&nrXNO+tpkb{<?jJpKRUs9A<d7ZCd!rGc*Ut1j~84=@}NYHP191{ATF3p;0m2vDvPvX`1aZ&9rpYF
+>^L^elrJx@oG|l%cAY>hY$a6jWzAI@AZB9LF_0(G)i1x@^~hid~&)nr^80t+%TK%(ljMEzR?EhiQiGn3l^+8J4G7Sd|W)ux(~yU
#Kz91K1p9K~t8Cpz8pT$4l9+>bU^E>zS$tr9IV94TC_`G*`6%4TfQvh7MU=*HJ}dn&Wy7qDXgj*KwKd0XhjAo&lgC9(2otE|?DBo
0oAMfEm)DamxcZpjR5<-
Ly^9g%27a$JAhCY}avk84F(wra|9S=(lFtj_sLL$a7p*BY+K6XPyP01aOvZcovS4s(FsCF~AW(gN1C@v;lvXYXb(MtffPZR7i&r!
X(XbEz5=m0a>n&Wi04`hiz+y>8Uoe9O#)QTJnI5s38ZC%v{rPbQ&mA*IlLo89{4^5jjY@Y1uY{22~m!^GsdU2r}0LvcXmi(=t>fC
m3r!MjGPKWtOTN_{DZz=ns_9TpL?~F@T{m2%*rtEe6Q*3>#_Af)=q~s;jE_vFB(u)CbgHsJ4qF<XVO!a9~3gtkAMd73Kku3!(t<%
f}jM#DT%EVKgN9IIfD6YFjE!0;tL+>d{ogu^k<;rUE@O$8aRcA?{&z*+8U*$$+*^$3@C<9MeY3>xSk!OxFQxd_K4^jDTdvay_8pT
}Op^>hd-$pf7~SgyFV5%Q85cO~(MlV&kR@UBKQ$)rd2oRTHO_rJ6uiFy^+PXqdhZ_RaKQa^Ud8JVR{3qy~6xoN}s-vJ-
F*gHLZjDa;3(8IFbk(tNRTFfCh0+#9y7YET47&J_d$c=KEn=)?e2LJ1X^4^B~-
m>y6c&=K$)6NniA(0K_MV%37IE>!L@$93QncEm;u!SF$+VHj=I0x+qB1587uE&_uB=sZpoJs1w46u=e`8WN{vtD+--
HXZm4usYx!NHc&~YQzA7_5djk5T1ve0JxOL%jl2?##M7P&NqP5*#?rn4kUq%cp8oX5TWB(g7#sUJRLctq2tU&3O5MJfLs_K>LoB-
lQ;oTpkRj%%vI>3YXiqcG6d??Yy*Y7<3r%;FeLcT*YUsL1>`VQVfl|DwL%n#K{HWWQf1^)+vCm?HyN=fsaj($g%=_{WJ96d=L(^q
y#U2!rO=}JSQw`Qkr&mSN&_gbHy)dt>z6&kl3a_TvV|Jl2tdnjhCRK%8^8}d0Y!)>71LDym5C<}(=`57LX;3hEGl5)K=KChgUCs`
1-G2d{eKC~k@v1O_YvQ7_E@sh&E-%`C&MQY*BfUni|1@iHN>;Y)JLO>6u}vYTK+H?g>g{3Z3W@HF-BP(>&tHZ-tD^3jso)SZ$8$9
axu2__|(XhmPF1O=z_iM2Kw4(@>%O+$0;*rLURkd<%%rVW2p)Tzc=)IORA!*F~_RXY(x^9%5EdaETzjl2zosCg=GgtczCUJG;1|@
dl_|fI6=kyIx7_Od2+`lOHu(ESegwd3TsqVR;*NE*HA^St!G?kxNDW{KdAdcRm$(0P-15E4zsk+=r52?ro8dh7QB^gL-
;0C)(lf3fPT_zLH3>NjQ$o{4z>|JDZl#$rrrBQGMtdkdeKwwhDHJ&8aJp`i|l=&lHC-
eE57jI7t`h*Nau~(ik|jF*9pK|9}-YAd2FCL4GXo!a6vn_t^N*LB5rdd@Fvp_i=HA-BME<pJ_w+VX5(=W^qk2E1z!NIP!G!nXKep
ODw`<(KQ<4ySfoj<41@8l|NVy;TW(O{O_vC;aUw9aiW7sIMxHUKTnlqbKpDlD@T9TwJK0RGd=Rpsdk8H~vV~GoVjImdyH;c~f{pF
(UllpV*a()r-
oK)3Xm1A1oi{R7cCU*rpY%&m;8dr)pciv38b^z#aBB`um0TU3SJh#j4=G^|#rxd&GrsL{fcyR`he5hP%}q=_%&WAI{2mp$?H9ZRb
76H;&;hX@jZHfXw`9ozW_;U&rSMQu*2_;G#z2uUw(ZF*1BJL4<uqHfoE;St6^2}L{OAcXqIH)D7FY?Nyoq1657WXRW+pX?S`ZL+u
pBNL3G4M0Ia||AWFv^SW|K=<Zb=#rY5Lv6Na+M58E-
{n_rY+98#F5g?#cSiA<Y@nJu*b4R0Rj5Tt!C?5wBipqjk22ta5ekl(5xlL9SlVC%bV-WqKih3pR8lKz_u_(_$6hlrm9Md&@B>t}r
X`E#fUlnD+<`X_#1Wr8A}6cb>9~e>%zz{y9RleH{zSy!xX(Uj)&u-y^E!oS0JhjQ8oe;I{dW3-94>)kY3|<@v?Xg)5Md$=~-
mP{l%g#5j4g4&!J>8@S|$E4Fe3>mge}?zw+D87BhsFs+DLl}rI8oE*dYV{&>OkNw_p#RdySX~I6h>}u?4O0$_MO_VyCjqw=x+$x(
hX`bKw=4XO-vhp{o3clmuKK`y2lk`EsJqk*GQ%M$Upx=Ak$JOYeG_fBlyD_v_p)mIV@H2od>u&%6@cS=bqrlSl`fTzrueXr%)E|=
U>KZLu4?o)BED3Il0TTIZ*_@1e0=d%(aML-_m{L$Vi`KAx%naU@*e^sjfefs#x-
SE~h77>Rhm58L{9nj(LbRhbgB5b6BCCsGm5u$~xGihh)fhY~CDe;W1rp!*$A`_B03RdJ#{%KJV??$&Pi1il`B)gMJd-Sdmr&Y#MJ
!|>UTte_jaW6ADpFFwg~$i6B&{HcqL2h^pv5bf6KHkaC`}qE6fiMva=t8P8BhXz5Nupz?*act`ywsf^t+=8^5N|NXqC=2CWIWA6O
}FME8ZP;#3uf~sEzx3A2osYXq3y{S-`T8Wke^dAW1<21p}0O*`!3r4Ox;8_bN5r-
|zVGzKxI28jjv*#E=H!ebAC6Eg`v}Vo>5g_xB`V2z1=vvr<`jn-rQ^b!Uxnm_M@*ex>tR^@OPJlRy=4Ua`MXZg&M^Fz^ki3p3oOx
TByd{ie|#70*9`z_SV?Tfy9RIZQJ0inhXM#eIr968@OBBm#U6@h3u6hhx2V=VN*^|JclPH1TIA$kT#6EtF4G!>H8A9SmD(kW%08e
P-
})zqFGvN^!HI7(Boq4V$*lG0BH*32Q_ULiR7LL%pG;y4Npe^p~ycv|O(8rJ5(uYJG`1&!717Edhl3YMToP1p~;~V|A*3;n)Pe3v0
>^!#V#*=>LL~?@>`o`h;LE*f8*OLePj5&xP36B)Jx<Qh572K9bl1rPP)0f}4zhJ6={aqFOS<bSTpLv-
*MeM5c*K1ePz^pNv{$JXh``BX=WmM9;W<{m9Bf>6d<6EH-6C-
Eh2f8jk!K&i)x7r5y@ii41)tZb&zUH8H>rg}=jJ+F6anYs6n0K{MJ7o1wDb2zH`fy&0DE3iZvy8y|)EK(G!0j_fV<mG3rjhlE02_
yQx;MvsL}AE4AI8HFfL_r7O8R##w=4SE#JMAs2(vk7!B<8;BLEZ#J97$ga?B*_$CJmm@fcIM|VC51l|wd3{$G09<aFF3?T;-
}ZflHDupLCW<VCJ-Z70HFBccaYKUX?868rOjbXxX%-4f4DZCC9(fKXra9DqkXqbmWfY0D-
D=gO3_{VLX$d_n}%4Fx4HD`Gs>C6BwYy2J{QbOb7U#?4(_#4t_gntJb%fdsCsG$q6lSfOq-xXP``cehXt7TW%;L7vMoUO?|sokX#
}dK4zyp;!Z3@InUos}y67mY)|Fj>d!+jgG5{%L0sh(56+$cau^LoowRlmOBjxIf6YSNM(jI2x+c{VBxc3av=+#y36X7=mO%@c~=_
MH-Gm@iz^TQTZQ`XG_MzWwH1^%@RVL1cW^bvvC_===R%3q=j@lAk56ILXFq!j^W<r+%RZ;LN`eBV*jzNWPxJ+0_1C1N4~fR1*fs1
-%hw@20-
XTaNLlvGh=guf3tNfD4yR33{Z4CSncECXupGw~qw;AHAk0u}D(q`fSWb`<S?r_VpCwaSV_zeGjLem(`D(f;o^S%ohXnvV$2f=6Lt
`DxYvt>XTM1<M|A^e#Q5ke5kJeCNJgttk^OW32=px$jyF!C}G!u7xx#DyY?G$q+P!`(zL&Q~cP#th>ms_Nh>wvGCbzN#r0Xj6CgH
@WWQ!+*-u`rVQY~`hF-?6c@OaSmc~^+4m{AEm6hCXKy);aS^W~u%yL)Uz;}-&i@016|GoCzmunD@;I0UakiZ6fFri%&e-
bpnhARl-hG>RGhmf={#*F_L$1ZM1oxkF10l;@SC80fMVt1YGb?iOmaX^*p^V%9;`dN)nX;=@d&ebvxMbfh+4A16NM7*i9J%TP{m$
?4_Y?hoJNMPX=!Ev92AT7!vJ-Y2pclsCxqrRORi>-
lqioJCg?B!e0Z}i479@Gz3GsHaAno9aB*po@v@!}Mipyr0SP02yAo;N~T(wA6!z%bI7JAVdMpNb6`HFb9CY%B1z}Mf^*7=GZj0<V
vJIZPgt2yTP#T-
QF>Meq?j@HKk7t(;bCJ!_Lj*n>+==YlA|2W5gE&y{CtJ?eaqyGh&?ZV&XVqL5d`eJw>)XfO9kBo0D#ULxC8cTJblUt9puYP+BO1b
Wz_EL=;Ti`+Ob1PFVfE=KbaG4MDX$lF+V;zc!M=Z@Xz}OFhW*F`UVKWFN5yUa4f??p3vOk+)EtpNd=?Y{A$Z4q`hDA2~5bTx;71>
J8YS_79K%miMhy`I>W-}o;gK)QC+U|luu3?Di<zs&@$DURj%vc_LdWX?JK3=nL78F34hy*s|x-L-
x@)2OAr0&*%9v0GzX%J14G|i%nJ3sX}j6@ipa+~J&iskmcVhXKVQ>ozHCA$Na;Evr<@AFyz>7IS+lz8ObrSG4Uq<8nH??0TQ4duO
GRU6u$$|<WgkT#wBbPJ2&rLwD4vwT|3a?Y~|i&Nv_oZNyh>GxP^m5QEoW9TI}jUFEhqiD{vk&)J0_{*dRSgXgCe8wd?#*L}Km*3V
~dQ&9g0OgKiJ>C-IEius&U+UH!$0+xM$o?SmKjitRvuu>n0*Xpm?xEKEc8*;5+p)-YUT>YV`enU!$?C^-ATzZ21-
Fp=aLym$8*pxVgbWYIyj(P#fB<`*ues+t2#QF)%#$y75HgW`oF^Y2?*OE{CgG3R`pl{xhpi9dM8YJC>#ZwRoPcPZ2^dz-
E402q9o!M_h}F4~xZXOI#~4~2UXE5%PO)MoZ3<SD^h*x&9f`^7r+F3u-
o?VaNal#i<vqIiAw>_6t;*y%B#*L30E?Otsn_?SuIdSj7Ep5K5Jl^gfU)fG*E)O8DsFwPPw(?3eV&Phny=Bc401)~MN_w_NE<Bff
ubUSR>k&4V^Q=(%;d%&qc>)@Zb!yhlu7*x>ygG+kS*6tN{p`{H{>7v``R98d5@MiEG8PH7yF*%)jQ`V{^`{3p<^%u_S-
<u4EPV8b}>ml;R`Lhm|0kgf@$Luo0k1$r?mM#^M$B1ow6#1rzl#^lB*>S+9FxZg6kxnO}N*jJfKl{eENRRWG1t@eQLJB*%NZ84E}
u?GVZC^pk65q00gnwH(=>Z(~|4^nvst7-O1ob1-Vcww?jWQ=E5EQmK#Y_Wy?NoElpR=%z&J2)@wi$IsEo+p@Z|jv_+TDnx-hChsk
!t+012{{yNN&VIA4;EO=n}na(vK+zr8fsL<fD&X7=`6cLI>e|IsVpb|7-
^CJz6S3n#T1b_jM_cPV#vKBM1<p@^3M4XIzc5ne~ZYFq^@JL=S2_ArzoJID<MvnN@P^sFU;NiIBJ@EaTifgYixaeGT4+d{9|L6?f
zW;dMIUM}iIrtCq<vluhf8OD*Z$F-1bU(fqj=Z@M72R3~A*?MRNVDaX9r~KuY<k?DDwg-
(NsJu%<OAEd+Y>Z0nKciahx_|?Wyb{JAF-VBE%oN8S^4~CrF3hwQ`Vh6HAd_(hwTba@-
+_lNgDs4e1xujh3^IGKyQ)n<@E$dq^py4b%Vi@P6_xW49I*_R`HZjm~eEiy({O&oL8Wx<X>kx844PO2BS2adaj9Z5@**~Cjcu}w?
3a%rFv(&pt|;Zf}FgZ$TMQ|X}q)2{8Qh|2=VG0|J@t^f}XoNNzP=RJlNui-o`D%!g$F635L__Kv)-
jZNH)I@RW8)Z@c1cah)vS`)(uH523>bNw(9u-w1JY^<oEeD$RF0l&{$cAt`9S<Dz~tgrZ%&+0dI%WPi5Ppg)MWvY*rUI<-
}A(H~aFC(w^UIR+^hs|86I|8S#1P6x-qavo1+Y05E+hKo6@`FG0zzoLE)tVnz!P(=CC!GPmIHcqo~ws?Y!j{<=G_tKf-
h5`Pnj1v*ck@klV&-p38U3w8`1>01Q|3`DS-_R|)2`IRz+OjFb8=p?g=q^_WgEaBWLsKe%-+Eg+-
hVS&%exT`eQeP%7{H`7|9JDqzD~pR1bHI4{l2<Np(DH8PP!BDA=rAed8_2c#k*&r<J!Ykpa2eG$`PP^Z#M5hDtwfNquXM4J9jgpo
GZKANKipGE+2GRY#2TScu|bpA|JQk{XhD`nozQjL74%0eAQbwOjyfkw5Q@Uh_IVcnmBeTNDU@7h|h~;0IFcJ$WV^{1H}^#r92!X8
j$B>_(xF#UvCGOgW=>MnMra+T|#D5b~Gu$gQPnf4Un;dpbKOm>Htv)gx3W$H=m=GjpGh84;I(iJf9<!Ou8W<0F{A8$$a_P+I{S8=
u+9BMlO~Qz0F{Ad3E+6j3}rR+hr}StJhmy9q<!82=m%t34;Kry(n}II-Moc-
*IU?8;k7J8kyv<j`tcK)u^{XJRgGiI^^b*!rV3l^aZoVfpBu==k*To3?V(BPh~ssdn@O}po;zuq|L79;@m8xFnE);B&?65#f<DUv
srGZiHd2(-BN3}Twrgk`J2vWY(#{LyRN;cuP~%>DYf4s;nS8z*$X4+&1UF(3o>0mha2&|{mrMpP)C~{{NDZkx56|)Y58W-
P5HoKzJYY}n?K`|H~^&pY7)~GtG*F6-$2F7-EYl%ZmDJWxoa`$5!ebhssUPZ<v{`La1nuw-
!tDIwd734zK@?8<nC3m!2r5@t+6~;4KL&VZ{j<=arbBGlq(p+quh=k=bSxS5s0&UrS%A1;awVY|H*k)+U`u(Mh`%wL?~Pth;Mmw?
Qgxb&pWui*>BkFF14EqXG3UMBI#R6!Fpu$iEIg2R8lgEpo>8qECMnE3#aGc5x^(<+TzYkF3*?|P%d0PNV(75KDPLeJma*m$t^|f{
%-
SM=pmf_{W1Sr;_(mMCWz4O_zw~`vgXkvS@ItCjg5XH0%P2$j8!mRNMZPb&JWV&4sG2}ve_U`=Fu#hg6z6QDm}t?ZoufbPyLdVw<@
rrpap~B_f`ky6#c?g>FBk=RTGOQ!|W;xhe>&-y^%&N1dhLAUdNhqTFiv(c`gGdfH>-
7i|rNrd0B?7n9|#Ker_vIqhjk2=3&{ee&5Hh><*pNXcl4}E1!NZPuU~d(=1OB*~f|l1E0d6#HF)@Y&;D*3(4hW>Qa*AOFJP#)FN$
!MPU@i5vXL*pvM0vJ^^k})lzbHx5@aDB+|K%9DqSQC(~fnJ&*jmT(cUSAdUPU4hSFPs!L)U2e0_7ZSYvcvx%_Uq!DJg?Qd{KT%W~
wYFz6#O<n=4%)VIEpf1*HUNNoM0EVw}*+BHbYflHxX$oACqun>*<M@qlW)6{7tDOX4z~>*@=zMv)v9m#dD_<CL3a+hpMJyn+ZNpi
mrWYH#RU-+qc%zx^z_LbOlG5*}76fHi7idnt0*sJvA5q?uJK$S9q_%-jg|-
9&ulof6R1sBRJeT7^dnEauS1_(PX7Z(VJcse{eTUx2lNeGov<z6h2SXTB&i`lV*$<!F%cV40;8%pPg>V}EZN98)-
lx1jjHqt2|LN6p<(A7A{8mfe(Zp%SMJeB}4%CKPsES-bByK8wU-
7W<K(bs&1O{0TNm;~S5cx=I1z9;5iQVXWoXy0c;d*PiWOcra3bO2YIULTXQ2T)Ji?TeTxz0V613dJLC<plwer0Vrvq7;^JkkkrVO
&OQ^LFkbYgwRhz8F+Y>0;9-
0d+}0OY^Kc$$k`z9G7zVdWOgEABnheMF4q!z6i!q(s*Q_a;XUV)Ob`jWWi`7d9Lr6?N(`FjrZaZ0vGEZ_p(JY!i}U2b#VV%h6ZaT
ud7$8gjdloNi_(2xAV4ha&~b}J}%f1iY|aIIAm61lkg^w;<OTN06)Fz{QMr|p2SH**$L?+JyeGc?DK$7Je&cK2$hF`0%f#LNkZv@
bXK2V2cSaNTjHSj9)G8gd)LWhoT0kKu_L?H!#4UpR49)N!Q;9Ng07*%Ij9imdc@BMZ4pp7<_~j4fMl#3W%Z&I49sFV=P?`D_d0(C
bew*aApkmugQJg^-
2nw*8N5B{c27Fp`j3){2EFt*)tv^TZ1^PVK2%<kndo>Ltiy*rIh8@f8cwbXL8t7P&oobPX|y*9o5PJFY_(@QJrrnQ)+0AU)6Y^EY
$0hWm5;;TDxc`H!(N#Y2(1Kd^wHB+v21nwB$pu8L)nx&$JdzX$v>i~F~L+Eme{$KCVP<1alz>IP@E2?{g)jR2my=P6R*3wVzQTJ<
8J4?)BXJMq&xUWeFrD<jo6fajFRc1);J)x3>fIlW|JBFS2CL%X7@0WMT&wk8Xz-
o1;(hbhun}IB&Q?kiZYoED8R~KmfQexlNjTZQEM1QrL}mPCJlI3_GB~(;n-8rVEJOvEyAGqL{H*n2Zos&J*$TGRoS~#kBs-
>`#nuF@hJDsVXwlZ`^+-
d(zetB%kdjuH$D6c$pB6^#1Jt)JhdUA6zv2sLZ#rNrm3O;NM#Am@BvXG2z%8Mb+*0;LSd5f>f_{L5KK2`5{o<H)vvE`lY#(t>g5n
PRfa)4mLlssJJ`u%5Wz}^CewshUoRr5bW4#`g#BxESG>D1oC-
n3_ve2|6Gy2sI_#y%fzMNMENq#&efKFB<zbAACA;4$M)y+C(4`2MwwaA4L!#=Ok#fvP65z(?Qb*+az6m+?jR9*oGX*4X=C5M9tZW
Yz^Ze+fdwwzaeDMC{P{f0IdvJPqa(Hmjsk0kaZmI+euT<JxaEr0EMg!#~<KXSv&e;X57<uJ`i{tLc%Xi0ve`uc0q1=c-
zO)JSLH){lKsDSLr+7mcZ3X0_dvadnCu(F89w?@r&>RIHFE4155_hFXx4_yPd{PNXAbA8yWH7mv@oY+4)3{zC*L=tpYeC!&{M;K4
`Rc*N`-5{^9~_@`FHbv`Gk9kM?$6#I{L?ndTcigoEJsC_!z`y?$x_-
y)tJpJzKMG9!X|1_o+!4bGZX&vm}4@>W}51)9F5+#9fTSMHHhok!IqFjU-
>rHWX`=*Ksp|ii{|k_oKOM~;Hf&=f}0(SQAX40Jv%;BD#p8h*;IGjS2k5qW>oAzS>F~FalMW%-@oU<jXreV9v_^Zygld9?9K-
N>U2L2KII#twYR?9acq~GOR;mn)0Tj7@|Vn6H02f$yxjl+HFFG-
(n0s_@yXkR_b@juE)OI)Ff+O*@b<2VuOwu)`tEK%E9#_YOKR6!{ni#)upGa101S8t3urZlDO#|Dah8JU2{Nk~3AFfMjk&{4J(yn&
{$sv84s7G#-
Q)1n;rQW74W@UOBSWtX2N+%~8;zFScSef3^;C@`EeK6lGgT`JLm)RNbaXWcJU!B)Sao&XiDS>RLftjfI1QaN(sVs?!qnA6TQ=~tx
JGt~eMXNGpmkV4Cd(N{()tUcHm@D=0>vq4qLjRqA3~5Xjk-jX7+(3hVU+nChv7UuIqIBWV2rG&C&29U7Xf1bb+NKQ;F|^22)6Sjs
DQJll>oLUhv$An2cg$yy2nf#ieJ9-
zXOQ%KMu}2pcC%es;y(3ABXLlx}};HMRI{ec(GNT?P7ct%W*MKlCB%BYuFw}_|YAVf}$Hb22g@D&x3NiFtVnjV`vvccQCpOug!oI
sL*7Frfa&VYK{tzu8F~qC>Btyes*xubxedvH!aPzRnyd<6%8^Nj)|>n9>57-Y@K05DZ|kLXpF|9s<!K45GZI+GhAJDF>Z~cx-Pt8
EFxV~9S`f%G{}jNVN@8;a5T?VJ*GP*#%uzj#ArO0VVbJx@bFj?u7Rm@&@fDs?P0hcT{CrP)}_!rp6%(-
4xrk0AkCrZQW_u){<SG6l%-nGu!nJIbj|ZHKoWvxn9v`<BZB65u5B0?;0J&;O+(iKG))7%xw=V#f-vq7K#H8a<nYZM!jl-LIUXpy
nq@JQ>JG(Gl*bh}`g4C?tcu6&4+|cOaltB5vC>Ya{^!N+=VFOSret4_0^xa`OvxtyVZlBqO8eCBl?>dgRz4ukjYjT@^2Z9*kB&G?
tM^zcH&6>ZCDApS`@Nv7`(SO-Xd144z)lplwO%ih_ELV3dH$TGl=YfXAnc;AFvsC>Mzne2yPAhLMNbe&<xwuUwR3h|IT|;vYK5nz
GlXSp<MZZDVd`A5GeS$-EuEX~oEzJHg^hE2%VgqQsuV?&aj&9cj}*xmFoLHlxd(T^mg<_*eGo9(L?xMQHY=G*XBfy-25W{-
YomjS+**oV9-`rVxwE$QxKtTsR6%WSuNWc&hQ&Y>3b%ko{hR-sc@-
3VvPwv!L~fHPnIxh)Tk=kirvCS7YwP*)A8j;UAW^j^qpajIn#w6CokM%0X|FQ#diTOp_FilW$!VBoT(!N%`ee(|CTj<eO~J!aV9=
a$U|%RLPQ}y^vK=21IIvZ>P%^4K*GO(s!D@=Rvub~#s+HENxkT7fvR4{S76A@tGHpIkeiA={(n~_~X9|0Z`7rwGVkO)y%WdC_eSS
6_pAC#~AbkZFEaKycP+&a_MmvD7c;b0cSUky_7eEilXhY%(w;B1!5`|8QMg_*L5+c?!5EOsUBR&Hs<96<WJe`Z??!vs~0|+a@Reg
dhd7P3uE31a}B2N+<t*{W}6@mH-
A8=axv_!3ZDER;i55vEz+;zTObV1=V>q@)O>(*4czoNaBS|}SSq1Lfu`(;nio{h2+1_%TJf|(#107FsQV^gnY+Xd-DghF&Myrz!w
0p*+q*=(gs4C{!oKpjoxJLFT);ZkTh8UpR0EC66I5CbUq93EhH01V6l%~BpwfB_t(d{mPOAIwrs*uKaEHAPs%axtLA9Wp@qo&h4J
!z>Jz_o-pJ4x_wK#`L`WSrf^9(F(z17VuEBtO@l?eWizz^g;K$GkAM>;eZk#fd;+TVrCz&E+}U}S&fx?iupkDq<likWU`%}4WHc7
Cs8;D3v(FE;TGQ919{3rWwU5F7oNSuMhio#_?`#Xt?yvDo%*1A@Mm4A8U_nR9;<uN7PW43<JDHw-
L5!@O?n8o<Y3FfM7P<D!!{b$(%~ckMW_^1n)P_vN+9k+PV85M|87Ma3@m9OB((}7#>PR?VUWyc2MP2I9AW8&jT4rXB)=jZ%l0qd@
vRi4z1j3_g39)1=j7e-g%~(xn_-z6>D5;_p}0$-yBc77J-
__&lNRY;AepsL=^U1_9b=`_Ra5Uqk`e`eg|6yn`=9Ex{C2mQnB><_o4;0xY`bRueY0)g88gUso56F1s<wnJc7zRqx6eDDJEsG|!O
$mPqP254_~YZ@Ngi7JXG3Zix7xgDDByP|_zji0pmQ?Aff^1^0BnqeKX}(YIrMwGj_c{Lh-ttxEe!Dr$|?rp^$d*v3c5VoH9b&bK{
*Gd-&A$aH9ZHTJsY4CLkZIWZCtlpP-
;CBBd9_i71eIrWu9$Xs^Phi#RQ#SH4RXRAr*9d8)M4CItTT+jz!9^JRd|iQ$!OWh{P{Ee4g7s#6yd)*fd_X=$4j5lrnfjBJRjvUi
;{Bjb7uq6+K^W8Nkd|VAd$ktZv}1=9Y8kOBFv!fDN^P#g^7`c3lY@bwoFPl*3IX<2ee=+@P>-
OZa>3;u^ySEN66I#T@<XxC7z5Hc4v>_{a^JHEeU5kg_!ek&$Het7QV5EUrz4u?)02-
}}$CP_(P|iHBgk*l3}MNHyXnf_|I(Ow3ocBtAK$q9nFqH=m$;@dA;t0HfqFN2+wh!iB%?f(ZcTC%z+v0L?=aEffi`OrpB}ictgcg
l3KQf1Oc7bm70HX#@3|&Bl!?Z(T8SV6m-
+j&{`{tZe0Y)*~#paRfVS)(UKp@o|I(e%fI13r3NjFmkm2Z_v35D@3}*43Xw`2+l5EzNcu5DdKj`6hRz^(JvV!_)~6^c*!0x0KtI
RFmAo^Fhm>##@$*(?82i8D-
)eyRnHe6&_c|T+~a=DYVd+Jf>==5da=oVP@O(6S`uDosZa`wdYa4<^hC>}s9gPg2$dHDrF>)6pa~QN;jR=!k}uz<FGf8nu4j_LPk
ue9L;IXPoFi;25gqO@97DSZAo8lHAtGD|h7Ku53~7sSA(Z~_j~LSa%i%)WuZ$J)_*e}9QVR0%_(&l>o{8`QIkv?2kTLFYO6RmWn2
d){+&h7vn)9z1*SP#mK_-
+wThYP%?a?L9{d0EdU$SHWn3Ytsm4F@W)5cFkDSz2^chvoOdU4X}{yVLA<u>H$DlX#Vu>sO2_{m+O?nQ9r3p<mk*H`rct`WnBc5d
V-
U7p8tD$m=9E{?mM&fx9A8R&xD4k+Q!qJkb_xvqi!5?C!J7K9Ki<RQS4^`PKkvYo1+yv?4_vzRV@NnW%m6cs!V&5E;%4kD&(;H84E
wS(0+VedH$2Ii_W$n=wDi*Dzr&VHiDD`tustZ3<67^f<lmKZ1Cz&V9b)|@`bzxE%Orzan~=sESa^Zq?uRCg{&r8FYvueMR0|D=uT
{B<^}^KC<Z{@jq}EtI^Ubd~9<!(6XiJ#HwSS2nB4vdcL?qT~DDs~cK6?IxEJ(B0`r73x(l&HNz6`F2MrEq8=E-|h&7-
!>ZH&Nof)5@EkE>?<^WUZ!#KB04(xBAv50)xzgMspqUTcI^Cl)7|;Arn~e1_NKe-
V<WDPERDd$pC3tD{Z(sT9&(^!&MRM=w{~}RvG{T{{>1wG3)j1DT;uf(ZRnzn@}-;4ukyGJ#Jf<va=W{F<#zk*<-
4i7m7BKPM}D_BU2x@ZD&4Kxm_DO9th^)g%ssv@T+S=+jP?C1e#HpXy?R~h3=i-?;{NA(n+IRf^!9MVt}|a{hxru^!^xX#9yNI6H-
?j)YrF<_pND5a5wqDenp9OK+KPWzq~~#0TEmGy;=<`XX+b+93Zixg-
G+7#a|Hyl`JU&wHr*%a(j5|XyQvRS;2on{_ZxT3JEhQB=sRBRB%ZYV3C$E#1kss~;}zY9%5xN#qQ34<)ItVCGiI^5vvR*H-
^>u+pr1d!zx=@M@Z1~v1C%<wSn<y-R#$Ps>cRRt`XT>PUNNuKt&YCMQYQ;;UPE8$<NJd9uJ%gz-OU%;`jRydgugl-
58x?^bjBR4dt&nRS2|?M>+0*RE0wKXpxfeqF|_O=nIS!+gDMdaD})z$HbO?AQ`f((grtKUXk#c_5$df&9>{9Io&SfE$!w6%7U<yQ
M|Bx{<qg8zEBWuWgK>=xMbv`fRT9pEEW(&?*)V__pU55`;B7AqX8Hu#JYHvu;p%FmB)W!A(HsbWIGjAx!l#;ax2CCv@r$dVot%HX
=zcsqdAkWV;9c1?Sy_C=k(^%|w8Hlr2Wx;hjPpT~QE;hIJOxArcjiq&Na94xE>BljZ8^^FmI>ND@M@Cl+WdbR{>Bzqy*%LS16(>O
sTL<G4mMrwD<<BCYkkFpqkd#5j0ZoY#Lu^s2QVAo2Y6jWl(hLFX^>xGjfiWd+lg!GayYE<x%A`zZK3Ej?6u5VxdZ;e<>ASN5RJ+M
QR0H^V6%h5&&g5f$6|U?46g`N#fIrKqSVjXG0<TFS`)F=Ubbc&ZIB^Kri`P_mW=gQ%5E3JkeK_?)LC!WG3W|ahwZv%Uu;k|>L{ar
?sP9YUnq~bQPr~X;#=3i`)<X4XvxunZ!2zd+GXWU%Q0<IUMt)EE<{IicNrid*(>fg^HY`&s(WRFuxwAk<8y$VeqQnB`^NiQFYu}K
dh7M)+l~?fU$I?gx&75+Y48=&nWp`F?J(#(^`B#h!O$6aZqP4NP^%2qHq81x(_yB!YRy@pgXhdR6~gIujyk|+@M`jsIyN}{ctPCA
GJnNY<+%?0w^3#P_;_(Fu~?dQzpAbBz?PD`3T|5Bufe=_B(76m=enO5UAIoxrZah!I=QKII~~7aF$cqj;@!m1*yn@ymz{GTRJL8s
V-
|9lU6VX7T>hp}lJnPX(o!dWrA7K^Z=I1J?Y(G~E?U7sDjSoJ_JlcEHg&YO>Z7BI4Qw7L>Mq|w1iUehD5bSp3d3$8Dcm)s+ik^2iL
GuhQ|9~0kHxhL!g5$X8D9j`T$WUm()M!sHa!FrcW?<%417@FYsD7&tW~0{tNkDI*4xbUS5&<2GnVn!sCc-
@bhp|;yFY6OEh&!O*C>wN?TX_zcf)Pl8F-
+2Q0(JIpkc+Rd{HK(iw&8?{RaJlV2<`m4EWWSE54#s%KqQSypQ&tW#7+sR*2x64!WLcgHNj9@jvMo{F4iU^gDd5@v`h;chANN6W3
8aa?cS86UH}>`L6Q=?mFN1<xOf2JZvX&KVFu+@=K0ck9hI;Bf7jW{;G@D;!@&Ac_p^Iq>&nUbKM%}cT8gD-RolRl=A(4UF_Y0l$r
Od?1e|R+3oicpH+?=Eq*IsA;K>hF7D$L{vYje@_?86lKhR^^%45o^eY!QA8}u{NQBmU-L1ZOo(G%k1%15II;z}=N1q$Tcf2-
;zlHcF;$%H@F))@-
r0fh`ke3(1V=w7b$P;<lro5(8G*7f390?=<`}xzZghB?Sm(B@zpBtbicb%hl1T018O36Yjh$6a_lhB)=REkz^s(^~cjpCJjc~Eug
0fSr=FmL6?_3d~2Qe_A@p8C4aPkr52l@g2$RSN9X<E^d5equd5@^xQ2;}t#iOGHAA_1D4+;bHQ_b+=HK(uD|%$s!o~`KI|ckIpM~
B{+97MPHwtl4W)GGxw^>Yvn>1<XSs@nqaUQ@;%{~Kz?Rdcti!A6Aybbh8GVt7swN+bgwdeT?>;%XWOc==Qc;4`$=ELQq;NUL%#i6
Jrs+!cFiW?4Pe?&rYnx4KM`q8%7MZSH2%fYj;qdq^4{HuEm`~%k(gM_IsM;jpV2D!RKq(bp2$lXXc)NY6a2wtX$~YX3LY~UeKahh
9rY^7{gL;6>S(11yu9i+T#DlK>!&P7!2+fZ)P1u#`s>RlEkzCTw50%c#~0~a4_!XV1~*2sy2&G1@%sAh>C`WL5dY2RF#ldVDceqA
5-
*2AEll7k;ilAU_}Q2Cao`?hBkkU+PI4BPM#qW_9y~6HaXdy^D_<v^U&bwo_o2v5&XIHUCnd?jL_c(ze{|IvuGu9g*7gTX_;u&iP4
k4jSqosP1@1!+PslL2oKs@B(tbnGt$N@W>kGHCeV0*;cv*e};EMley+zQ~@jP`NLlMI;t}0|Lf@w|fY9Y`+{<0Q-
*?rgP{`24ISSEz>l~bYZ=i=}QT$fmekEd}kv_G?~*TlDJZ;Y5!v{R0-
7ftbyXi31v)0DP>QGh&yj<9IV*2#LJb0dmTKDjde&pG^ASdUShXd+OhgE4h^+7q*hOMP^BlqW@r?3xG*2y)9pAQT1p89`n`sh&dQ
(ie?Nem<t^npeuP?F^^XWamJmIb)gA#wbAD>h<cjQD=2+AMgm%uUE$tjdgvWzj*k~*hggGdC5A37wOdv50U|S;sazf9Zd1OA_Y`R
s8(j_mu#<jzd5DT^}DY;E!r09<S!l)m8@aYY0*N=lLtr3SFAjHa1=(|fblc(vz!$fv^+|AK*Q3;0x!Bge1%U={V#+wTtjNf)u-
F}N9XND=P<V(6t{sPSn>ih0*|@|>=OUH80@gU?${;U62n$PVEd)0i2tRBS6@DVx`xN?R{zov{{N$=f5m_8<n-
i%j?I(9ONFc`W));Sd*8w6e?M#QA$jWw*Uki%pK7owyqp($CQUxrGpLilh+Z>TxXS^3^I#79D@XlTnOUorqq?T6hUr<bI@NNd*6O
jIx@zJWMr?Rm5SfwfX-
=S8P8zC_r$x3Kx`wI6PONFErH5FBquPcYd#+_@Y5fPQZGq+)P&Cgmpq45qwxh;DWVm*y$FXJ@YGRpTqFS*UTej^5rmCi~8EK)JXo
eZ3S{fROn%b`8#jfQARZ#M?@z0|K)OEx5DsbqDrn-@yghrftVdUy&q*|es>UwBdQRD@x7eu!1Xl|U^aip7p85y3Nn1-
#VrWtR9<9TFw2K-+E0vgc0G<J<3RFfnQ9X)o8Ahw+#(WAtRQay4*HPtj2HY4;L(+cd=g=g1I(<n)*K;&oHF~Yz$I1CL>{HoPK(E-
_JVw$!EI8Gfe3}JK(OY__)a+AP<rab7hm8c$IEP))6o!SNfYsQHKtNdm-
I99ep;<%2knH5Na1Slee!43@=emhJ|S9gujuq^{<Rkc;ahOr84%ZZ#+b3;Q{-8i-
b54z+=M*J)!Kqp&)(RJHY^%b<}sSU#ejiynU1}dOJHFVERHPw!EThr~(2wXd`y*O1Z4RQpr<{5z#2euIgE&)@VxY*zBIxEjuYz5E
JY}HZK3V3b`!<9Ntn8cnP1gV$cpD^|uO-rmWM6w4sVNTns2g4q~7y<_{0e6-f>fY<Y69+xELuXkYP*rs#J;M%D!?WE0=31z_z(-
=uv?4Q&92Yp0lf*`1hJba)voy=q0m?AaVpWSZHC;pA%3+6>Fb0)kEIhXYlj&(lT2|zmFzEn*)YPIV1posFL{MOVaS{Y-
7z5z}Z*+7(ux48TQD}y4lD+`b3uw|^S91-
kI*19(B+GE3$hN#hvw{GqDvdm7(+*VIbwkgzU_OK{a6%YtVAY9XBq8L}Voy^o0_o)RuyfXdpHo=jHZ*K`Fq^8h15?)qwhB|rbhJ2
vX$RBF)DoCimY&!KP>|_30ZcMAwOr3O3@-
{Wo{yF$sUA|ZWoPF7S3B92A+sIVtO5qi78i&ZqY=W~GE7|qBmiHwU<M{Id`^f6GGKMWxQZz(AzG^GmhPl!;CbdcV6SvcEQ4iPFzk
+AC1@+~bkj6~RFA_H!+C~joEoW}028x-SB9wyAXuiI0!EX_L-O%b6==xAFPvHbypQ<`8?b;K>MKO;z|sZmTgB+23Gi%~-
%%37FdD#`0xyY-M2jJZVFGw*lv=5kSV@vZ(9g)>a7hcnelBEe7D_ANn4066x>ZF}Y^7-
!17W41iSmOD=!uLdbX704oltX(1UL}PJ<A4;s+)!tgr=r?F>p^<QnrEf?Ai+CtgUdzI0>OSV2K8<+t}sQjbZXbgSPG3W|V-
a6l<<$#-^RPo~y?u%uvfvRXwtUWFs7}z=>hQLT^<0jv9nI@Ip5-1H-^aU@LJN*#?Y<4pa{9S*jX(KvtfoyH4!rz|0{x5Lf8L-
bPrSMTliNuw+z#2qV=7Li99X%E0Delq?OXSkr?vRwE1>Wu%&wXo(TWz%C+3i%eKvf&IYrOJaKkh;@TZ6#^Zo!>ghJT89<DRbhoxV
R?j!4KrOcQeZ`f13-
8%ODqt4!qhVXQz1xxX>4gp0Q1e&0zS7v*Bu5=uLHo;v?>Zhm>IeajhI2ACcsN02jsjk3Ox|{oH(%}H3~oiChApzYCI1X16Vp8&jH
D`3cy;xcun0dUU;hN+EsKo$abSp)AY!3tUyEV8tAZ0JD#maUSfnv1SkN3OHCcqcFfR@T_6;|iGfQPL9^-xxt}NC`nYu|vONb@-
70~^aqOBPk*2T?+rZg$U}Y+BLYU#WI_oL0H{gmPOdS=Z(I7BE@Bq0P#2r|f)Zkfo3MaYkD>jG_j$V}qqc{P!ka|EUY8)C-
6gbeBml}}<LWhyyj}EL2v>sTfV_>#U5W6<4D*%!f0!%-
?j?cO$9}c?z^c%mxe%UWAChQm2Mz(1w2jvp=&bcr8A%bCpUONhAPnA&E+zKW(R&zD@>sT5BX{Q<MqT9u}1(||<wXgjZ-
5cY!P#hWbI-l-Mrl7>vXJMU8LMgvDg%07Me$4Gdp`VhD-
q4#(UCsB%anmHs?<cI)#yhmP9YUjf%V|tIBqe+B*!QcqzvOYF$>?%jR{Ynq%Ba$0Bl$XBQU1A8$R8gM|2dEag(C<;M3_Ot>EC|*Z
w6Ng4*"""
raw=zlib.decompress(base64.b85decode(''.join(DATA.split())))
assert len(raw)==45369
assert hashlib.sha256(raw).hexdigest()=='74d275f67ff071d79fc918a48f757e599f620149c85ff0413a422a4a076ad35a'
files=json.loads(raw)
assert len(files)==9
root=Path('comet64_recovery');root.mkdir(exist_ok=True)
for name,source in files.items():
 assert Path(name).name==name
 (root/name).write_bytes(source.encode('utf-8'))
print('COMET64_RECOVERY_SOURCES_READY',len(files))
```

Primary reconstruction and independent verification:

```sh
python -B -S COMET64_RECOVERY.py
cd comet64_recovery
python -B -S -c "import comet64_base as c; c.controls()"
python -B -S simple64.py
python -B -S normalize64.py
python -B -S certificates64.py
python -B -S verify_receipts64.py --primary
```

To reconstruct the entire finite ledger as well:

```sh
python -B -S comet64_base.py replay64 --reservoir
python -B -S surgery64.py
python -B -S extras64.py
python -B -S frontier64.py
python -B -S pair49_control64.py
python -B -S verify_receipts64.py
```

The decisive observed terminal markers were:

```text
COMET64_OWN121_FIVE_SIMPLE_PARAMETERS_EXACT_FULL_MASS_MECHANICS_P1_Q0_PASS [120, 207, 89] [1, 2, 1] [0, 0, 0]
COMET64_RATIONAL_OWN121_EXACT_PARENT_VOLUME_FIRST_MOMENT_FULL_AUDIT_PASS [120, 207, 89] [1, 2, 1] [0, 0, 0]
COMET64_EXACT_INDEPENDENT_PYRAMID_GLUING_MASS_AND_INTERFACE_CERTIFICATES_PASS [42, 47, 49, 74, 76]
COMET64_EXACT_BODY_RECEIPTS_PASS 4
COMET64_EXACT_BODY_RECEIPTS_PASS 24
```

Selected exact artifact receipts:

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `SIMPLE64/OWN121_FIVE_SIMPLE_PARAMETERS.audit.json` | 37152832 | `497c054e40bb10e98c7c5ced52e3a69a9ec3e1d54e34a54fcf5f5e5eeec558c7` |
| `NORMALIZED64/RATIONAL_OWN121_PARENT_MASS.audit.json` | 55816727 | `5a92443af2dbf8140bfdf3f6e7215519bf0ffa546f471ec9b7259f025d9f0ffe` |
| `FRONTIER64/THREE_CAP_CORE_COARSE42.audit.json` | 27988018 | `491879b5c84d837edf41ccfa2ea74877d1deaa0bd6be7fb725d816501db4b8ef` |
| `INDEPENDENT64.json` | 259313 | `873460f63b3471dce3082a41e7c752e631e5477a7f10f5896339ca42321fef2b` |
| `COMET64_RECOVERY.py` | 20496 | `f227aff3a53f10b644dbee958d47cacd294d717f79914421d64b2d06ee5373da` |
| `comet64_sources.zip` | 331048 | `704128761679a716cb969397f3cb2858f1ee8fe9a03050254ec1c4b03b8e7960` |
| `comet64_audits.zip` | 267147885 | `5b58955f3bc706912025d5c709b2f0ee9bfe5f532b33fae30598020da967c5d4` |

The replay manifest inside the copied COMET63 main retains that parent's own earlier `figure-0521` ancestry fields. They are historical source metadata, not a relabelling of this assignment's required COMET63 payload.

Convenience artifacts: [complete exact and numerical sources](sandbox:/mnt/data/comet64_sources.zip), [all full exact audits and interfaces](sandbox:/mnt/data/comet64_audits.zip), and [the standalone recovery decoder](sandbox:/mnt/data/COMET64_RECOVERY.py). The inline capsule, not these links, carries the construction's recovery data.
