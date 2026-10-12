# minimum-0267

AI research report · 2026-09-27 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# W_ONLY_MACRO_U2_V1
## Complete exclusion of the literal affine orbit, and a closed five-parameter W-only family

**Main result.** The literal W_ONLY_RESIDUAL body has at least two proper unstable equilibria at its actual uniform-volume centroid under **every SPD metric**. More strongly, the same statement holds throughout the following closed, independent five-parameter box in the supplied H5 coordinates:

```
9/100  <= x      <= 11/100
89/100 <= r      <= 91/100
11/100 <= p      <= 13/100
59/100 <= q      <= 61/100
7/50   <= lambda <= 4/25.
```

Consequently, every body in this box, and every nonsingular affine image of each body, excludes joint proper S=U=1, including configurations with additional weak contacts. This is an **unconditional U>=2 theorem on the stated actual-shape domain**, not just an S1/U1 implication using a spectral restriction.

In the common-height coordinates, the conclusion permits **every shear v in R^2, every tangential G>0, and every eta>0**. It decides the complete affine orbit of the specified literal body. It does not decide the entire H5 family, the entire W/A class, or all E17 realizations.

The obstruction was found in the complete primal escape system. There is no full U1 primal survivor on this domain to which an inverse-polar compatibility test still needs to be applied. This bypasses the common-inverse difficulty by proving a stronger necessary subsystem impossible; it does **not** replace the polar metric by an independent variable.

## 1. Input audit and relation to the supplied frontier

I read all seven supplied files in full, including the complete 365809-byte, 2680-line journal and both literal parent payloads. All seven native-file byte counts and SHA-256 values matched the manifest. Reconstructed compact UTF-8 parent envelopes matched:

```
minimum-0262
9d6d4bb7467bce10452f7713b241cc60dbd441bea84f7100c4bc37c967d53825

minimum-0264
bfcc1a56683308cd9ba36d337656a9bbebb9065375f6d531d489c9f28c03c4b5
```

No source-authority conflict was found. The older optional `h5_seven_turn_reflection.py` is not attached and was not imported or needed. The new recovery is autonomous. The chord parent's qualification about its original unobserved probe executions remains unchanged.

The supplied regional theorem had excluded only a specified shear rectangle on the literal body, while expressly leaving its complete affine orbit undecided. The present theorem supersedes that restricted-shear decision on this body and adds the five-parameter family above. The older theorem and its diagnostic controls remain valid.

The supplied common-height reduction correctly identifies dropping det(K)=ac-b^2 with two independent heights. I did not make that relaxation. Neither the old nor the new covariance trace floor is used as an assumption of the new exclusion; actual covariance appears only as a numerical preconditioner during optional certificate discovery.

## 2. One actual body and its true geometry

Put s=1-lambda. The seven unscaled basal points are

```
b0=(1/4,0)
b1=(1-3x/4,0)
b2=(1-p,p)
b3=(q,1-q)
b4=(0,1-3r/4)
b5=(0,1/4)
b6=(1/16,1/16).
```

The ten raw vertices are Z_i=(s*b_i,0), i=0,...,6, followed by

```
Z7=(0,0,1), Z8=(lambda,0,1), Z9=(0,lambda,1).
```

The true maximal facet cycles, in their fixed outward order, are

```
(6,5,4,3,2,1,0)
(8,7,0,1)
(7,6,0)
(1,2,8)
(9,8,2,3)
(9,3,4)
(4,5,7,9)
(6,7,5)
(7,8,9).
```

The 17 true edges are

```
01, 06, 07, 12, 18, 23, 28, 34, 39,
45, 49, 56, 57, 67, 78, 79, 89.
```

These are exactly the supplied compact core's geometry and indexing, not a replacement incidence. The source reconstructs actual volume moments and independently recovers the supporting facets from all vertex triples at the controls.

For the whole box, the new checker proves 56 strict nonincident support inequalities and 34 strict polygon-corner turn inequalities. Together with the prescribed two-facet incidence at every edge, these certify the listed maximal facets and true edges throughout the closed domain. Triangulation diagonals occur only in volume integration.

Write **D=6 Vol(P)** and **J=6 integral_P Z dV** in this handoff, so g=J/D. This J convention is explicit because other journal sections use differently scaled first moments. The code symbolically verifies D and all three components of J against the complete oriented boundary integration. It proves the exact enclosure

```
54053037/100000000 <= D <= 28054169/50000000,
```

in particular 1/2<D<1.

At the literal center theta=(1/10,9/10,3/25,3/5,3/20), it recovers

```
Vol(P)=881291/9600000

g=(7368835529/28201312000,
   3427883561/28201312000,
   50317/153268).
```

### The entire box really lies beyond the stronger reflection test

The checker additionally proves all 147 strict W support inequalities and all 24 strict A products over the whole box. It proves 1/4<gamma<1/2 and verifies failure of the stronger R7 containment using the **same fixed offending support throughout**: basal vertex 3, top vertex 9, basal edge 0->1.

Here W is `-k B_g-2 gamma T_g subset B_g`, k=1-2 gamma, and A is `1+q_f.(Z_j-g)>0` for every nonbasal pole and each top vertex. For the R7 test, alpha=gamma+1/4 and beta=gamma(1+alpha)/(1-gamma); the tested reflected raw point is `(1+alpha+beta)g-alpha Z3-beta Z9`. Its edge-01 support slack is strictly negative throughout the box. Thus no R7 premise is being smuggled into the proof. These are the same W/A/R7 conventions as the supplied regional source.

The positive-upper corner has gamma=4548897/13555588>1/3. Therefore this family theorem is not confined to the gamma<=1/3 range of the inherited chord argument. W/A and R7 failure identify the domain; they are not needed to justify the new primal stress contradiction.

## 3. Complete proof of the all-metric exclusion

### 3.1 Proper instability and complete weak escape trees

Set X_i=Z_i-g. For a true directed edge a=(i,j), define

```
d_a(M)=X_i^T M (X_j-X_i).
```

A vertex is proper unstable exactly when every incident outgoing d_a is strictly negative. At any other vertex there is at least one true outgoing edge with d_a>=0.

For SPD M, every such weak escape strictly increases squared norm:

```
X_j^T M X_j-X_i^T M X_i
 =2 d_a(M)+(X_j-X_i)^T M (X_j-X_i)>0.
```

A global norm-maximizing vertex is proper unstable, including norm ties. If there were exactly one proper U, selecting one weak outgoing edge at every other vertex would therefore give a directed spanning tree towards that root. This argument includes zero escape derivatives and additional physical weak contacts.

The program enumerates every nine-edge subset of the 17 true edges, retains exactly the connected subsets, and roots each at all ten vertices. There are exactly **4879 spanning trees and 48790 labelled rooted trees**, with 4879 for each root. An exact integer Laplacian-cofactor determinant independently checks the unrooted count. These are local labelled counts for this one incidence, not a change to any global catalogue.

### 3.2 Polynomial tensors with the actual moving centroid

Let sym(u,v)=(uv^T+vu^T)/2. For each true directed edge define the polynomial symmetric tensor

```
Q_a(theta)=-sym(D Z_i-J, Z_j-Z_i).
```

Since J=Dg,

```
tr(M Q_a)=-D d_a(M).
```

There are no free vertex or fan masses. Every entry is an explicitly reconstructed rational polynomial in the five actual shape parameters.

Substitute theta=theta0+(1/100)t with each t_nu in [-1,1], and expand exactly:

```
Q_a(t)=Q_a,0 + sum_nu Q_a,e_nu t_nu + R_a(t).
```

For every matrix entry put

```
E_a,ij=sum_{|alpha|>=2} |(Q_a,alpha)_ij|,
r_a=max_i sum_j E_a,ij.
```

The complete higher-order expansion is retained. Hence the symmetric remainder satisfies `||R_a(t)||op<=r_a` everywhere on the closed cube. For each of its 32 sign corners c define

```
B_a,c=Q_a,0+sum_nu Q_a,e_nu c_nu-r_a I.
```

These are **affine-Taylor lower matrices**, not a claim that testing the physical bodies at 32 parameter corners alone proves a polynomial inequality.

### 3.3 The exact finite certificate

The embedded certificate supplies **671 sparse nonnegative integer weight rows**, totaling 3014 nonzero weights. Each weight is at most 100; supports have three through seven true directed edges. For a row w put W=sum_a w_a. With

```
epsilon=2^-25=1/33554432,
```

the exact checker verifies

```
sum_a w_a B_a,c-W epsilon I > 0
```

for every one of the 32 corners. Positive definiteness is checked by exact rational Sylvester minors. There are **21472 strictly positive-definite lower matrices and 64416 strictly positive leading minors**.

The affine part at an arbitrary t is a convex combination of its corner values. Combining this with the complete remainder bound gives

```
sum_a w_a Q_a(theta) > W epsilon I
```

throughout the entire closed five-parameter box. Therefore, for every nonzero PSD M,

```
(sum_a w_a d_a(M))/W
 < -epsilon tr(M)/D
 < -epsilon tr(M) < 0.
```

In particular, the directed edges in the support of w cannot all be weak escapes.

Finally, the exact checker confirms that **every one of the 48790 rooted trees contains at least one of these forbidden supports**. Thus no weak rooted primal tree exists, even for nonzero PSD matrices. For SPD matrices, the escape-tree argument proves U>=2.

This is a complete whole-domain certificate. No failed numerical optimization, fixed shear, fixed G, selected root, or individually passing port is used as an exclusion. The proof covers proper-root and weak-escape boundaries by strict positive-definite contradictions.

## 4. Explicit true-refill collar, including nonparallel perturbations

The uniform stress margin also gives a reusable extension beyond the five-parameter parallel family.

Let P be any box member in the displayed raw coordinates, and let P' be another uniformly filled polyhedron with the **same true maximal facet cycles and matched vertices**, with

```
max_i ||Z_i'-Z_i||_2 <= 2^-43.
```

Then P', centered at its own newly computed volume centroid, also has U>=2 for every SPD metric. Nonparallel end-plane perturbations are permitted when they preserve the stated true lattice. This is an explicit thin transverse collar, not a claim to cover all nonparallel moduli.

Here is the full bound. The reference raw vertices have norm below 2. For perturbation delta<=1, the new vertices have norm below 3. The common 16-triangle boundary integration gives

```
|D'-D| <= 304 delta,
||J'-J|| <= 780 delta.
```

For delta<=1/1216, D'>1/4. Since ||g||<2,

```
||g'-g|| <= 4(780+2*304)delta=5552 delta,
max_i ||X_i'-X_i|| <= 5553 delta.
```

If d=5553 delta<=1, each physical arrow tensor changes in operator norm by at most `12d+2d^2<=14d`, hence by at most 77742 delta. At delta=2^-43 this is smaller than 2^-25, because 77742<2^18. Every normalized forbidden-support stress remains positive definite. The same complete tree cover applies. This argument recomputes the actual uniform centroid; it does not freeze g or transport the old centroid through a non-affine shape change.

## 5. Preserved actual controls

The report reconstructs three actual bodies: theta0 and the all-lower and all-upper corners of the five-box. All use exactly

```
M=((5,1,2),(1,3,-1),(2,-1,4)),
N=((11,-6,-7),(-6,16,7),(-7,7,14))/35,
M N=I.
```

Their exact data include:

| Control | Volume | Actual centroid height | Own (S,U,H) |
|---|---:|---:|---:|
| Literal center | 881291/9600000 | 50317/153268 | (2,6,6) |
| All-lower corner | 559723/6000000 | 719323/2238892 | (2,6,6) |
| All-upper corner | 3388897/37500000 | 4548897/13555588 | (2,6,6) |

All three have stable facets [1,5], unstable vertices [1,2,3,4,7,8], and saddles [12,18,23,34,67,78]. Every one of their 204 total true-edge primitive evaluations is nonzero, and all three are physical weak000. The source and report retain both horizontal centroid coordinates, all actual poles, and every primal/polar primitive. The two corner controls are new nonwinning actual objects; they are not 110 attainers or aliases for the earlier 233/435 controls.

## 6. Search, verification, and uncertainty

I first tested the complete primal rooted-tree systems on the literal shape, rather than extending another fixed-height ray. Positive-definite stresses were available for every tree. I then retained the actual moving-centroid polynomials, built the whole-box affine-Taylor lower matrices, and sought one common stress vector across all 32 lower-matrix corners for each uncovered tree.

Numerical eigenvector cutting planes and linear programming located integer weight proposals. Acceptance was entirely separate: exact moment identities, complete polynomial remainder bounds, rational positive-definite tests, and exhaustive combinatorial coverage. The promoted 671-row object is the whole-box certificate. The decoded source contains the complete numerical locator as well as the independent exact checker; no external seed rows or saved exploratory checkpoint are needed.

Observed executions completed successfully: the autonomous discovery/build, a fresh directory containing only that source followed by build and check, and a second fresh directory containing only the recovery capsule below. All reproduced the same certificate and report bytes. These are observed exact executions, not a proof-assistant formalization.

The result does **not** prove W/A=>U2 for arbitrary actual shapes. Outside this five-box and its stated collar, neither full U1 feasibility nor common-inverse feasibility has been decided here. No whole incidence, canonical orbit count, or global lower bound is changed. The supplied global bracket remains **34<=Cmin<=622**.

## 7. Complete deterministic recovery capsule

Save the complete Python block below, including its final LF, as `recover_w_only_u2.py`. It embeds losslessly both the full autonomous builder/checker and **all 671 exact integer stress rows**. Exact recovery and acceptance require CPython 3.13.5 and SymPy 1.14.0; no numerical solver is invoked by the capsule.

```
python -B recover_w_only_u2.py w_only_exact
python -B w_only_exact/w_only_macro_u2.py check w_only_exact/certificate.json
```

Optional full numerical rediscovery, whose complete implementation is also recovered:

```
OPENBLAS_NUM_THREADS=1 python -B w_only_exact/w_only_macro_u2.py build w_only_rediscovered
```

The observed discovery stack was NumPy 2.3.5, SciPy 1.17.0, OpenBLAS 0.3.30, CPython 3.13.5, Linux x86_64. Exact acceptance depends only on the embedded rational certificate and SymPy. All nondefault tolerances, iteration limits, integer-rounding denominators, graph orders, and shape parameters are in the recovered source.

Exact pins:

```
recover_w_only_u2.py
18341 bytes
dc00bd9decc1431d8222de87dff6203b7b93702a080767140fee579113f22704

decoded two-file JSON map
40625 bytes
a06c5909d8d1994f5a95baa7430027ecfcd61ba3880e41ec9ad28a95e793bcc8

w_only_macro_u2.py
14714 bytes
3aa4d11717561bec576fe0c04087f12cd4aab64e744ede9b4d12e829da4dcf6b

certificate.json
25502 bytes
eb610ab904f7760da34492cee44348ea16699025805b678e84b8ae2c482f1115

report.json
29978 bytes
781531caa4f16f6a67cff553cf8623f3047369e320c4260ed621e1a97a701c25
```

Expected final marker:

```
W_ONLY_MACRO_U2_V1_ALL_48790_ROOTS_ALL_SPD_CLOSED_FIVE_BOX_PASS
```

Convenience copies: complete bundle (`W_ONLY_MACRO_U2_V1.zip`), readable builder/checker (`w_only_macro_u2.py`), and exact report (`report.json`). The embedded capsule, not those links, supplies the full recovery.

```python
#!/usr/bin/env python3
"""Complete W_ONLY_MACRO_U2_V1 source and exact-certificate recovery.
Run: python -B recover_w_only_u2.py NEW_DIRECTORY
Acceptance uses Python 3.13.5 and SymPy 1.14.0; no numerical solver is invoked.
"""
import base64
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import zlib

PAYLOAD = r"""
c-p0X4RaeelIUOI`sz+3HIfIwU_N9sRZgtDODeImwzGRLG>bJNM-pv{q)AG$oyvcI4WJv-z>wa(dd@C6oN0VD`nwyWKcCE+?S65+
nAQ8{{KIa&dUEmP&-YL2?RNdRd;jEOJWdlaNyZ{c;WJHg_{{OTfX~8Si$ubwM9308OM5L71)mC^y8F`J$>1}?rxkow_Bu;6d}@5^
?q~Ln8`nK`<7#`yUFY`G_3!SuwuQapuFJ_JdH-a6^`V*VVPWr|{B!#H)i3{d`s<4y-n^dvE~ozx@1Fp~rrtKI{dBh8Hq+g0Ep=|8
Ygy_dzrGS>mZ@twPiv7jX<o~^l-G6Dq@_@@kyTyP&Gl7Q2mngwbu}+^QHV<0zPI&!alf<uiKik>?alpdv#$-R-A#M1q6_s@YP_It
2~W&Y9-GC@?cQw?U|ppSjdnjo0==6HohXAAQ6!=O1eooVc?3}w4k9NAr7Uh80PKMIDN@)8^H?N><Q+(nXo(F=3$Jm2qH_HkIQKl0
ZhM8@7adPEqY<*w!U-Hdp0I7Ngn8iLD`^QPbK_@O3-6xW1;NC0)RDcRl);e$v{TZF)D~W-V4=VXIW9zCPlZC{5=2Hl<-+!)WjGh$
AnY_ltQWSWWDufs5P2SS4(rpjK?3oE7?hRkBPRf<Lja2a=t0pIdko{e^U|TTsw@DoPT^XX?zt`<rrKFnZV0=a(*5Ezk<oH<H&AB5
$}+;J$5&Q4(y-Xc2tXzojVEzyG6$eVh&EWGBQ8ttQn3exlQq)qsc`L86}Qg>AKKu(a!4y2(%_Muq<NCNCv9WxC@?p(lbSt{%1v7m
FPQJ#Y^B9F0Xhi>0FJqGhgTI4v6G6nrEoG&rR=%IZH7CMvz{eMf{c&N_fl7OcPvq;0H>+LNg>>>TI{ohw;N_zTa+yUNW@-FOs%tE
13d|p8FI59v}hOVWO%Sn;npcp*x+^w<WLWWbXOs{sP?&Cd{y8A5FkSUyMv08kI*6E6)g(vyj4X#;asvbf&j|Gu5vqd`$gg<bMh^q
CdUg>92`*@GIS#nG3UtMWgbu7?yTAK%Iyl1#Y86s-&)DGRwIPv93$pcJWt!!scQp=D3l^5UEu&^;Q&-enB>?)c^Ci%7z$>yoHQK5
s}_mu<F-?_dyvbhCq#@&J9BZuRpOka2zmm_QLd-F70eFrz=AqlPlh~@W$_?c&QvVuRyS`&s#KU!tUXi&DodG#p_V``XC=3JAX{zg
w%Sp6j#T3NkSNBqQ5P0cc^NAhmWAVbq0ofTEiy&Q6g~(R9S@*!0K|(T13{wlD{wVV8EQt_ifdTy#B|WLz^;)*GU{45{h(yrfONeK
=A0wGHR_?x4wa~HxGe<zIwqHfu^e1cwStCiDCxBlO_RWs0P&r9Q=$r0bxBrP85%cv5nB?d@N!(SB_Si?WXwF3Q-HW+5*k^@@F43)
@})?pKR_*L5@X6qU}wRo0}>hs#7#abq7hCanF*AzS<%t1u0NEQWYKmsxL{@=JlAQg&YWT)NuCj-=#D9Y8VI#sbwmZZi6CZ!m1%|{
GlGg|BAq5ssC|^`tR-)!V01tg;slNK5_?D;yx_ZTw+-zcL1up-gPhjSWAoa{c_+1{Che6vldE*{F)+t19*Y*x;sXFXt_Ud-A|#8S
3Y8S^5v?PgMnjkJR3*+)5xb=w7XScqQkf|_iCH|N=eE*W9U4a}RclQ;3p(enLWLW|ELtf8)$5;FeTt?@fEa^08oh9iN|)EG)H&58
CGraU^qb@6EwN=5^LAB+9aOm+I`?YNQ9~6wcZEQYpmioB+QqJ^N=o#wbzox&GbZzSN~b0{u5`xLVTrPuTMiBrS&PJsnt0nsa{Vkd
DI45?cJDO#PXa9)=4D94hW9o|7FjxIdoK(mlM!w2h0%h6w@IdF8BQ=amMbm}-O}us&!Yr4t_u|Lfz#r)J?l6<j)`?UYEB$rwSJit
I&xJs3Rp7av=eiICXuLp1zL2@i^7R<lTV}ZkUMb!AjLs{#yC^LvuGq{i?VfPEQlsAl~7%xp;Z+Q;J{*>C0HC-OyT28qBV9c(Xe?|
-Z8_W@+>wzQ8<xv=x~v8-pe@eX;h3k8-v`#43TC9BcE*M<c+b@BW+cA9pSi#xnPz!WJc&J(Xh)f=8!R}CV(87DpEI9f~qb<C7$b!
g<f)Pnmd{ewo~V^=Z9M(5$8JK+{!yZVT0D8D$xYV0?`xjme6q*5-FwRR#e$KNL9Rh)?BDOYMc|pJPXgQ$XK3fV-cKTM>HiBITpI$
nwz<G?KUBzP+wFwn94jv-SxaMl9h2UH)}acl-zdm;*^hxJFO`)RD~9a+Y`k|MMy@(oF0j)3Q}67<cyKKP=K@+A#*UfYl)N6F%Jq<
Ajm%&Ei%=SI)ZUMxwdIXexdo#rzX8~i}X%TEt(**BNzN+bflpqx<x)TLVXFz0RmgC4874jJtm?RV&Cbf!Z|R9=Otp@CSzY2`y%z&
ofnBsiXK>zZ6MQw@}X*{R~?)dF@5gT1LrgEaaBdQHI+vrW)cWjoiKxTbC9SSIviLE9!m?{?h>_V$fMk5#Za&h()uuNhQ6+dyl5q&
XtMXXoYkWp5z02;T`BG~@)nxhV&x6u$URoEUyM$@TbU-q79HuJZ&Xe$xLG)6<X*ifj`ZyU3<a_wpG_wufm&9RG38x^JlY9Dqednw
Xx<WWVk0NeWhuk-gKz}F`_edSj{A?HJc>_X6yJqqA~(R#FO3{~g{sIKin)v+e3agbZ5CT_^TU~&Eg=FShe2aJM#ie8&|yy*qP0L}
MRuAZ0<w}ecb18PN1PQXshvj~xXu(4qQD7->axi46yERW;V~9p;@e)*c&NV!u);wyjLt;TM4{oQP~N1T8kk1N;;~RC<S2POE-ZFA
@&rd-VV1~TBpwSQc16Edl5ikDwamEmNWK2<=6d`r3+)pw+*jeE2$A9>sA|1wq7ubN4Mr>6u6N>fc^=WdAIz(2cPB^WVEPAWwDP*#
MKmi4Hz37DaaA7j#PpV(u1bk5;0Xo=v;440j_VL<D}05w%~^6P#|$Kz0S6*NY3nanar6|$BDv<N4?j6ENb$BTb_9IlPPdBH`(Bj$
%cIepV`KRkm7x<25>u~v#rTq0r>MkRR8XoWZKE+6l30<&gA%uCw{;S+s*#*sT&Hvm1FR_&%Bl#uM5nLitzcfr<3+|J_68X;?gV48
KE3N1u0X4mGIC6GqBrim5DYdd(dui<t6YNTw0g^|j4pFDD+mpg$ZF*U5*20Y&@xo&pbgpL0O`@l0WO6(K!v7(r-MR95P1;2BN2%v
WEes8xXD9Nttea3ffQuqVmP6aC~jK_wCVGbBgZ=NZG4TxlLZha%TliuNiw1<*fB7j`P#-tR2JIMK8`NQj_D+H%Bt0##&j;ZVH{+B
kW+BOkIYH<z&8bwt161{C|@dpqFAR<Zdvg#jn@z==CL>mkD^Z6{1r>}GdN1fN);IqT16dZ-0GJUA|=z7mZw`MEYc?!`sYdOPFhYC
;h<<3qOI&Qg(=lvVB(K~7ZDt>pj&h0fJDktLLzt8a~PpXqot$#^#QMn79>&ksGNCGp(mCd+Lyw|_^F6RB^WT!aacxSSf)Vw!nknm
=*UkmLtB8DC<_pe@t88~lEpvJa+SrA7)oAJdXQE^fr}h9h$g3)s5wXbQ*`>o5S~;l`ECGn7Qd7z5E(Xe42DP_%_Xzat4@L3SLIw|
vsnvDW-`64(l#)zqP-Vo80hhSPt>n0d7(+#O0FzsOw`SkCM!adS)mYM@m&&zSs9dMDPL~Ui7|NwDGFcqW_X=8q9goC@RTx+bW^ZN
2S$rR_vt`b3U!fC|1#Pnk$u9FhE|4(HcunUh(hAPl=N&w@utk%4-pNyc$4(8J{=D(P}1vmo)zQGpqL|%xgx_=SLDoibmS-_1hQ#d
$B{a7C`V^S`T`tJf*lL;pwO487y9KfIA8RGVIdt5wF=~3?o+Wx!ef-PW$`i55$x3gZQ{#GQksGAX=lZYK*GQe>OfkAifcD~nuweb
UGd07j`dj5?+qHJ%8PN)DS0AUMkwi!y-!{hZlx|uLp+xsr~#vJbwPD|Wt{lQ1Dr5(Kx44Whkz-Wpfhf^Dw|5f(O9Zfw5bs`or0Hl
`Yehfm#sD5OCGuKV@XmG<PjI>5pW2K6pD;Ppj#5=-jV1tTv632VDqj*iBw;ZHJrr|n)|>~wcc`$Df<lbwpOL`d1Od5TpyEUktnM&
0?pAGr$|5*<G6}b8cz1)E%}$>gex+-L?^*RN>bxsoycw$XIQ%BdPOAdorz(SaI|_P+l<1)2QvnQCN7b+M+=4ii;R5yPR$(BoZqK3
9)?(#Q0x**tdHEUH!CA~jzy{_DqqDZ=Zcq{rO36aYnoFeOJb^DGycH2N)MU&nx7C-`rJ6W7?`GT$Ss)!^BK5;)qw`t;}RjLBt#-N
W-<(<RAg6@nN~!}kkVn>PeXCLkrWE~_HBKfLdBO;cqYz~mq<&c;@Rog5|b35D#%5_pmdJ*P}-$Z3`7L=7$`$s&`yzF)@1%E%xj@9
PDY@JR;(k_KlNF8bpNR=DouEX%n0u&#_Fp!izx12pa?Gugv&7KM1^PMAUHQ%^B&PWKw2%!sMY}^Vpu;|qO2$Np^-FrkA=gu>j_;x
R{7ha1+$(-TnCe*E|Az^u7jfhE|pbMSTIXmH=V-zyz=S*vFsc>sd=@M#_s~dH7Q$(c3Rib3RSCO)vqAuJ>^_MF`}Zw&bVYOK~K9&
Ml8G98y(i+wNt|Ut)K{J$-<Ou7fKX5oiZisb09hptu7g<R7f$-TH)A0swed2R8mJFsyuF>3YPax+frlQp=y^*Q=KywL;;x!ddev$
U&fJ0Dl{uoRw%(rjs=D}`Edy<(V?0h3WyijI%V6K@`7#59gEyoB&a-O{miH6bP<nAYip}9QIBL4G@*?u9U11hwki#5sg#O-N}ow-
ePYe!0UDTsYI+J3&X_!7h$NkWx!snzvLc+dK-aBsF?X}81+NP)eFd8HP%EB3!2={Y3)YjyWvT?t1(EuiOO=MR#aZ$QrOdqILWn$q
pg>Yiqm*$UnCPUnmOixZ1iWqmWLVZlB`=y*N=JiaSXkGQ?qv~nM6nmN7qE`0Y88p9*nt75NQt$qMAf717*)x-phGtjwU%)?bjWiQ
+s~=Kw2axD&_joc&}l($-irZ=JD^3pdss#4xvW5&5(PXKV3$Em%~}4Wkaf=LP?=J%yeLXT&02NN8KnN;9!1^)6;6w!vKZ9y8S!YA
vf@FMo`F2}ZbO9#$BKc>p{Z;mof$=EBRuDhp%kg|j<#}Sn4=jYBYo=!(kzIpIQgMIrpTWt*+4Q@1XRd{6UO{$DF3m}m5x*C!_`fg
C@I@8A;t9%4qSz&Wr77bLP9G_MS4cjCiBxtuC|)CqQv+>5wRv#D*7iPa1l_5W}aw5PbBlDr#cqg#I7YTap|U-Gk=z&U@9U2puLrC
tVYS>@?3J?s4ZsHcv_XJR}}deStz^-j;eSZs;kzLN3&ZwYWJod)!pRr^pOH$k6k+hr^IYAO{i)kBuYk7h|&O+3{jV-JYdK}cM1&}
iSZgrjLIrj<|3}$pt4NTfdMCBcqYhkOV&VYI?Ji!6SEYi(<IUHfC5?7DmYq;Nmw+FDy&;5S;QB+=#<|mc0|UdILJt<SW1ZJYf<jW
Dza}Vl*QA|ZfS_KBRwiiz0+Y$Z=m6^m@cF;Rtz(S4^{Bwu`?&V{?cAzJA|r?+r6s8oQ!qQhQb9)A9D;WqSTi@w58M~w;F}dH)yKs
*D-fd`IEvJyN)1G-=Og>sGP2QL?H9wN~L&_0mc!mhN2z|mVhT0Mz%c`gpb0V3h~<%Mi|T1-)e0{#iATkX(K6<rg0yY7jHh`7-v0&
k0SE|0xL4mM#98UM%6nx7tVpm@rco!K-)qZq2gtfxaH^)6SlLqb}nZTU#jR=iqdg(5|s86aTmxtDuSwHWb0IdyO24W%gl>Kv!Un+
t?EdyfU0LarKlr*c<G(fyiIwgB>d2#%BzFsL|Yt^rR)@}x8h~T#uCDx$SbhoO?oR$glngWi;5TRkL;mASEX^3f@+8ee>y&jAiBa&
qnlKC(=7`pqEwgwWS!+17yTj#ezDFlt(MY}0HK)NEt%=7S->E7aWR38fH6;z)8b+yIxpsuG6xRe@x)AZ(2g;bgMP7Av6+GDp8PR+
IDzf5cyxFVPYb%D#E2v`n=F;%a_vu8p!Z2+S@gOBEyMU<TTqHtX{Ces9|p8Af!`JjND+Gkog94TGk<803s#IKeZZ_6f|F5pI4^k)
QL_LRzJUbw2OWfw;)q93x(H96^BEj~QxR@dctj-2xl2e<1nDGaNL&sl8gWM_N~AdAA>afl3Qj>;s{QIjpj42`^cYXWgBO`EJtc2V
c0x{VeJDTg$;+^bQlo9Ikft>rt1K(Dzp{)SYz~4(GEV1`GeLDzj$11#DQk(($0F!th?hLs!D^D+9|QI3u&P>)Bx^^u!InIJ1%wpw
(0S+sR9L&AgFugvzGf{;BWIvchn$c+K{67dkf<nDibsHz2&XJcZ-PcvQ^`w6^1x|vsrT3>@>Sa8+=)P(pa|sFwjhr!%XoBKvAm(+
%u@P8^||N}Y0g|Rg@Pz!j!7k0;U$mBQ*}q`wTcf4i0HUs;mH$at#03Q!(^)J99?Wv0$CoHj#R<1P3)tM@KF5{4<PU~lh7eUkjb3+
lN;J6f+&wcndXWg8{w%dnsw&RU*wc~E8`ccplhE~Os#a2*AzMC$Ap6l4@^Il2uLT%Fy|5&PC1W>`U6f#@hmGtM=I0koTScT4CT08
CFWg=!!ch<d$eWt?Zk6DKBCef%NNgEYHC{Hs9_$$rG2rB&hhHXV<Xq`Yl$#-Cql=nM2u2aUeoDiI);-b!CQ*Z0b!g{qA*rox4JM$
#UV;&qEqQ+0MU9YWIAL#*O~g0pq+CV8C9s3LE4hSA{cz;nP(oUMoOlrKc;7bP_^bET7NXEMIhC&X1PCRO1`uVHi6u}oZR3RF|uTN
^e|4J@>~-;%=)cW<$P8C#b3dyDlZM(ssz$&5yrTwR)cD<N}>**;fg9;+?XZhPgr1?2+VUpnR%HPdRu}HcZP=%-0|P&D7v6vbLmm*
)J++WuS<W_-i{)PiKz-x#Sw0wv+oGuG7Ur}y#a!XK!ZwPMcj&tq(UpXq%e475tf)oqvF)UA2csS3`wOLS^GvP!y9FwdsDU<!P{1R
`GoS-@)ex}R#^mDAY>WRF1>E5zytvg+fs~LQV}n%qby@cEg~75WqckIbBn>+%Pc+{P9<tN-!_TSmtZ_PH69aI>3!DVRap{)2Vso`
xfF`OK1pHxn9r2_Ldpkad1uGD(w4$kG2}9yc~-Jlp!lkPiq`N$;o^Xk=~MvGxnFb6=f}&{=)|w5v(B3gR1gWKvpO6^SCPP^+(;%u
$y!w$U%^QYOj?vgotffgj9B{1j9%qkV$B7;?p9sV>k06!I1&rB7)a?)j#QFWPKCP?RbRS!abG!ByW}!x8Orm@ClL>30WieGRc9u-
Em?d67lnT<r!VX*@YJ$8(4nLPu`*tafBzM!g$xZN-3b|X-@+8u2H~3<1fH_zg<2$B#eq`q)JsM(crf~xXOXcaeG!)~j)k^KaEQR0
<Y)3EJ8~*1>z4a>!EjJIor=0%l^qbOBJ+oPai_}sDAwq0FIjX>6|4FEOP$C8OgnEuWJhxHjJd6jDFTm1`J9T(BTj4!wPea1Pl>g=
Qg=)kfd{{R;1zw=5Tptt%gVonpz?F0bEm{O>X;!IMKZBAI<U-S79{~##pSo=j=AfKpI<;)sj4Vsugj1|QlCDm$|G1+XiKA`C{>4{
@PvTNuD4o`g)(z*HIaiIo;r}ewnF)rAZ1k)*Khes#gC{!Sz&-U^(W)wH<qy7)Z`HB=uvx$JNGAWDh%Kk=)mRb8y(}e6c`PYEeqwr
#0x)=cg@ISj)VB3iriZ%1I(uWwO`(^r8oRgag0AiK#nbW<@C;1itAK5E}|;R(8Kj(RB3!lmd>|RRICuO+gzzI{O>y}Fkzrc3YWYN
Nc$=~9an@`UPhLDWmL^X6-0bRRQFUeJMmC~xbUO5+lvw^_tjw(izw14a#CfXD$xGrGA!AQ8(#8YFyCnJC}l<X!ZM0TXxZ5>s@+5*
k6x*mNAXrxFQ^LsA|KTz?=+sX_2H4K49opW#d9G6?(#G`M5|FJ3ok(>kK+W^wqG}$i<1RA(j@83MzE`Ckcgr>6rorHo---@fnZ-A
sJZ-598;RALS-DA@gh7*HYhYFGa_k``qu#F@yXu|xla3aQ|(D!#Gp7};p)RA9;j+h49UdPW{@ax>5~Kb66GzPpnjw1CS0Q)i{wZK
hN|9z)Jq=3n|S=Y;BR=+ZMd&Zfe8LiCFv*V17noa5P=KSt!3v~4XV1P7vA|mC*>20SVZaImDW7m&MZkId2sX+Qx;XI2r;9=Du>g^
J(e_rWM@wC-6aQJ#LRL)u{%wkOX+h7GRzkFDoPd0RecO&MaHOD`FF!{NGyrWD<6YF@e!nU@Z@mr$)7PZraYAL0wItuJaxyTr<5CM
-=f>4H<CK4;s?fCQQFPWPzo-iR1^xIHZU#1b;&Yx!He?f^mEA%w_qmNh}^0(?>u~Qv?6<sD-&8?oWqhi9lOS;F}<NjrXFQ^eEvy#
voDe{{>}T+A6OR1y|HiR6*^I#4$dfc-^rpV4=5!+?ijx|kCT5uR?_jK%sXKXp2wmv1xYgE!3@JHWVcEGzG`(KBpN2PDpwLDzb!?n
_(uAm0p+k%-t}(@%M?k~9lwAlv-k=nz2%UO)3hs!Pqxy=7gZ2|X-@%XNAlifTSJ~l&ayceI{EAU>PhnCak^eDzfAAy*>*j>m*<-=
PcEMP$KRgb@3v2`7OSVt>Y=y!vcFxg)ce)@C+5HIU&1)=z1`QVdA(e(nqKp{p6z?vX10E4wqJU1zXuoYkA^JPtMm7(-)w(9buQGo
PI_;@-2L{YC(cE7o<8f%7dvV>pD#>{db#}4dv$Ms<T<o>`gXQ(4T|#=y8Hfqv7BG@UjKIa>ib__yq&)K{nzQc|9*4%;^o_sz{&T{
zVCIH+PgAMd#`_g_uKF9rZ0bb^M3WiZ8Q6L@$FVK1H)Q9jsGgj`_;SK#(_24-u<rG^|rNJO0V87_P2M<elhErj?a59c01F2z1sEe
?so=rclBb`YgYBuvYDR~*59wLx9hv!Vh_OU^>Wu++-=s|eQ&nDgMG5S?~>kTyPn_A_6U4e?{7IA-rm6N<>HE-{02YYukgohy))1J
Z?_!$vHP-P*LQ%5de?jVe)Xm|>b*UGgG+qBdiCPhOSpB?rIZuc{TFX8U%fMr|9}5T3Uv14iytoELSOwpDB2`TR03R<q=TeiCPf0`
1+G9F+B+aPl5&u|U-jr;ze-BDso-G+O*8lg5e^M2xB`<P(YARBzX!0V|9$!Hg&FHj-w3!t@}^(mw~1)DZ~T&}Y4PU8OMrLaDg3_t
?JfS6!y&W)a(n&e)#V#=cYnWGHhtW`e*a9Exo?|IQ}0LGboR&Po7ZOaG#L!_`_=ESelkcLyLOA!zP}iaJ`8%->uqn*0|MICtDB||
P3^4@{MN+m!cT7;;!=wohboXN7E!{X3qC<$o54RP+hmh`N|tt~VehYi1p6nSd)wZo_o=r$0hoWha6NihxVM8F;tWXQs@~O0JDyoS
VA}4;nHqk6n&I^(*}(UwM4WvJcM0YOfZL~;ouO+Fmlm)2Ai-~oBag_p=fBqb?c#I4zZ>2syWt}Y;xKWaJQ`fs2@QIuy}lc&ZID{J
86@qUW#>+sEX^GlvfeheS(g%LG8=v#Zp_zq_-XJo&tTb~?S|{r{HdKn4$Ojwo2TWe`8HQdp2C;8bq0-wpPrV`=u4;3);u{i-{uM$
A@CVCe!nu5wmg+XGoRsZ2#or(-7A{0f}2A%y!!l9p2Fkda_G<xt+T<?>~uL?!cH)>+ke#ROW4Xx;v21K4$x?6{%?Q`t}cIsDg6nG
$Lzy(a$V1wo)vZXcMS;0rf=DKaN+v1l$=<?{kqun4YX}C78jFKdvPHq1Z@6Y{&>D?_VebtzF+S9jt+JptD1Sg4;{gFCF9B9yxwe@
)x3XgCiL?ET(-=Iu$MoYxxRSw=Jh|@XSM@7B|Bx;kj=2)Bru<gGnf%He);>0U#15;4}M(lkS4Epw$mTaAL`|Ov+ED2lVjtv0gg_h
wu+^<Y*u{>IT(%1b=wqfh{7spP_cdU>;Y~`+v7t#A<#oBK&_Gc{W`fKyl<QR{T4>9hgawCPOpab`MbeWNx++V|3w68hI%o+SR@yV
$@#q5_XpplvCy&%PJJ}1S-+-E7T3MSZn4^dxiM>C9z@^Y*SltLL1T=^rqRQoUCDO+II+Lr!u+n!_v__i2cu7pbqrlDW^JFl{T8Ni
7<j&z?OVt{4d}<g1)Iai<iU*!>iZ6``Pboo`esUr-S7chO}v<T5@M7v^|;tJEvjf|j0QiS-`{O^eTT}#P~Y@p^JO=Bx4mzYU9+iy
`_|jtsDF~ce-|f%!Rg8S_p6h^IW$?%n|{0fw{<_>e6$(P-QPch$LF`r=lSBMG5Bp8F0S{$blB7xHJ8>_oUNN{u$~spYQO8%*I?oF
>|Z$>S&e%NT6DNiVBxdn{d}>y={43oyj!o<cZ+&?PWF-Mc74A`5knHBX_A>i+S~Kr*2^#b>tty3)ZiROF+0J;hk>qZ14~+X*mv~U
oC?N!joF+~<UPQkv+$N<OW??lgHXm9Sq77;>rOAOr{T!jYPRLjVqm<O42S*Z41OD23_pg=V9n#Yp1>5~>ih;+sy6idwhtQb^dZ=(
KkJK`Tc<;cX@DeYh;jB8?bg-$el_2<+cksUX$Re%X1g`_?m-${?T9>UN9Qx%Y5lj6F<l11L}qrL=051<Gw3S`?wrCMnhF@Pd55Z7
z1FYC;MLS)VLs#p>;k-2<|A`Aq`QU>JsGs3Wx0NAwqV*rPqU^a2Dq^U)9cQdSKu&BI_k*j2DW>D2hcMk8D9?nfZaO#Ir(G!VRB}!
2aLdsH8gf;e0$z}-hk-s|9yO)JWRZ8V)18<vq{^~Se+IP<7<v3r#ei7>m47*XpJ$4zwZFM(abMnN3x+V{ZNOu_L^_41sQxdl1Hav
iR7;S+&7??W5C}eHb>Q<W3;LP@1nUQmA&1v`(~Hu!T80g8KA!(-rBzQ$t{@;v*Z_RxqWT6>z(QOY`Yx-_P>~6y8P#P*YXFN=aZ0l
i9U#oZkjbXblWe}oBMh@Z|MlQE7>gTRkO1)DWIf(Y5iC`D!EDw=k*OCwMcTdkK%Y<8K|qXdT<VI>TcJc!R52wE!+j!zXpi_zuZ&^
W&Krh%hBw}`)fF(KVlKJ*;u2}ic(L)w`XpUuYhPLUBgC3&C$FsdT5qxHs_1o)a*(K+$?thWMtaO?tWuj&FO#6;eRLp39@@JFk%jc
(`GXO)(=;(S?`iXxCS$7yo}Xn*qN=7+JB5KHv7;Jg#3RRBgi(GOcM6!EPT|JzbCWxb_KHJ$W$GE`Y^1M3Ajrz1^0W<u4E2`Y;kPl
_cQRn@h8$RcpZ$0kc2GZaJp$1mQErJec)!6UlS}aLXo39?Bzp?jt{3IM!<XykhNXn717@S=5CjAI)dl84tqW9*QZyfGw>c<FGvrb
noO&+mtcsd-Zb^k9_(#z2$@dLeja#k8=t(K-t4Eh_44|JVgKcsb-5Xm5q7zsu2&5Q6)<uLbyMHn)uz`^z}#RoaOiCKGpLp$O_qly
B5jKn9=y=Ts+o3Ef$2$h{V~2M4B`cRo&FKKJEq~)_(CS><g9kz&#WM5m1AR6;hCWVvma(K#{MW7T+6|L(G?TLMQkBCN5ch0V&Sk}
tc>{ui#%)B>NKMJF*Is1Y!q+5?ZmW$o$gvx9}_FLLJq&O#(!6q+s*i=<4MPspnt%s;yW@V;pN6fT=@NQqWZv?PM8{3G!g#`6xk`g
U}EA!IGg_Mshf^L6zD2BbU%M)bNY|o>s8acUVLumy;XBl?-vhE?@iG|ae3iF8z$(wZ$9@_(%Y{$y(+=m&HSe6rDxxXbJrUz%}fAL
=m(&E?DzHX<!Of72z%--PhSp(u)VaoD%#MVeKHK%{xPm5oK0!k(>KLbO{-~o(h-(?KhCn@%XY}y78T6Jg?^3mn&(z(+%4>#)_wgh
CFH%SA1!W-$p@|r;O_E%wp`4cdevL4w|Bj(2JFI~?5$VehAeh4t<UGda7HAN1UUOjst+cGo~%`(e++2AAJ*2x1K-A)Cbvy*SKl>f
%X)9-0NVpj*x9zZUM!cr4fKD%y|R&1a09mM<+9#>35OT?P*kIlN;A7u_zB{z(%>_XMn#zhu-UK=w@&2{py9FBTDnHr5Uv$8D2hx5
P3)cL5<HGfok=~g@EEhq)Zn=dw@HzQHW45@Hi!Dwi6ai!-Cw~L8&BDKK*mf+8~{kBuRhLEp9A0y%*87-J2@`rTroyk@mX)z%+{+p
zwM2lNW>o1n`Cc&J#241`#0<?)>}(0BxIca;`WfWcY5t}3Whjqn|Y1gR{PhM+{gcwmjCKh`$y37bZNBwv!j}QXKWIy#v@C>t9#V-
yE{_z^bdClO@ZAVfSkWOtxe$Q^vVX2X2Y2cB88MZAB|qNwDFxY4nB-VKesm>{0&U)!&8{UY;6p@z8moA{Oo3U1N|DTEx%mfuV!FY
z*_g~Ei8zP(s>_R4M+?wE#)}ETs`%>c!M6x%6S=XH#|Go>{VkBw`*+tgE^0h-4~v+!3cv%BPhN(D@TUlM1Exk<5$=tccX;_YFdp(
oE0u$gw=krx^G&j2ZM_-Qkm<bwWGdHg6@pJ_V6%x4x|bYMwG&@??&lGySnpwPO;2AdR!5~LKD;10}wnBCnDK*G8+9EhC>I;kF>n`
S0H1o@NkhK`<Z+leNApgH_5|#3B!)&PxA!2uD1&lPaDByV)t-lKfTv)l;pNv?EBvn!ha2nroK)D=0Q|)CTtSq%!VX^P+kG(ujh-^
LqA*;P|mMTRQ@`AWwwJmm=^b6&%OuK@MO}e2>AW=#IV^Xcn&}8G*3tg8&B&`8}_~EKfr#SzZ?EKgexG42kSF{!s!Mj5M!S{vDTkl
>sLd#g4Ul7wKh><Y<quirn~3_Wm6Z<0dY2e?xd6r1SfOL1e+k{Ga4-@vbx(H?5_G&Z=XIL>+SY7d2H&BM?*6<u+8nU#K?ooA8qL2
Sr6<1JDttO-bmp4L$a78pFWKN(th70*OLSM01XGvfdy`Fz1+1q1!j*gIqb;ri<#;na3mTVbKmU-Rzlz3yYE{N=A#kNT%P11_-ehk
J$k=r{x|f7EYkWz*aR|ok|E%bXA=(d5m24IIGH5d`f*Bj(a4b|F&6xCS8(fQ<j6Sb+S`oxzBe8*{Q_Xeho6#PN53YoMz4~$qunm~
eRO}H{Pzg9wA+_i=hWD$yOFsBZ+&rBFGrh=>8jq2K7C4zz?+);3u8*|MycoU{kCZ~_3WdM#4P3}5BFz%@e#d<IuurpcLskw!vOMl
V${dIwSrR?OE&ZANN`JXp{c(zw$6C$IBXj5P~?uIw`Y64fOg}0LIiVV?2W7OmA}D_i(S(g74c^ZbKbA#YcpOP46%ze4==iolpWO$
cffH1I=-^h1~6uz3;SthzL}KivYlkWDwd!DcJN%Jht!ZmDky&uPIbF>qj@yNu4QckiGLcf3-iHNZGKL=3p}>?e+vOI5@7fX^8uSN
s*fYUk=icK`2qEfK@~yshslKHq_|jp_}j=VWH9LXi(Y=1=LvM5m{6y9{`_NW>A_vk<jZ=)Y+#WNj>t#@2tsf%IUR{-_Qwa1i2jEW
k7w<Zh4~RWU2y-RN-io)<Bdjkb4R1BEGjFaTDQ#HN;@vwpZ#re=T!bSsgpa*Nc<Hx=sFn7wW+k38VP7av0jg3X$r8lD@|E#g8RGK
V)F&DVd`M)@ALI$4<h7iLr}}bYO`J6gpzl2J~hH|2Mj-*jz%Z85b4CO()AKPcC|?-t`AeD0UbcU_43A=4(+emtr3hLznEL~c3Xex
$CC4UxvuwqbL-l5=3vKTe|d+17Mpj6Ql17?lc<|!u`<MTviOj!W*<H#%a3Q@t!9hmN%AhK>*QSv{?x)7?bc4-c*`c&RDWLVjKWfW
nh(v)s#!CHwSxkGih}%I?R~&9Rs*obq5zAP!DCY*Gr6#1wXP5w@N_q9e}0&NM=>0pYjPz$9rX?KM8VU#9^34&c{DNnZc0~Vb5^mm
#QM>I&?*U$$qI1!0kC+IJS6q_BAI~}9kdw*T$E(iw^=|Wx$jr^yJpUWMBb5z*244KkF$xSM{VnGkf052wo@}%Cm9R}TDbwn?fD^f
{$hH6H3IP2bbJQt7OvLd=h$|iJ`Dzw<O%`W{>=S@JvE<3V?Vy{#tm=E6|XGB;d!`F%V^wBlULAmFd0(Y({bP2!Q07Qv%g)>M<=(7
o7>$<Hwj^cIiLg_#u?Z+pl-nn0O$LKugJUHZr9ts0l9<c^-UA?@n}c`o_-#i8jEK(9^rn&&nP1dHXtyDbs$@gX<%l3MlLI0y9H1S
e4HeYNj>OJ+H`boe6YcHK!!(@*&K`k!xAF36}9dIKk3VVr|B`3_qcGg-I{W;$ES~$-v>kJ9o**K{>#P|nhlQX%V42q;@?>8!mQRU
?D^=Rt-${o83vqY>)bvL67#i3Z*lLOY7<m~P7PU@sl+A$o2Ahk;I3i9(1=Cws>iblnudE6o<Y*^5C;#AV38>;=%%xw^WO8`nUN@F
-_F|YeSUa*57X$$t91{nPC-uWz~J4v@Z!m-sXnoc)wPMj`5&RBAT@j3HZl_*&%j7{K0g!98JK&=v0?mQ!wUd^VcjqkS0uLowE*S$
;KK;{Y2UaSTab6)5rFBu?lqrh%X_1gdo^(U25d2s3d`o&i0;-=cxKVb1BH*bi)CX0F9NA=B&t&!<{22>V__nLclGWg7DTkRnJYCk
#KcTsGmg(_!=q<3n=yt`OdEU4(D7JK{>$|Jw~_grbRD_%)rV%bADNn4V`Da}{dBh8Hd9xPGjip&F4Q_Q1wgi>WB~5od~v@U8ESd+
;^iT!4Vq>BxEnd&2)u5PUHje0PTzZ4wzB(6-`q?nEuOeEIMEK8PzGdt;wF1C8QJ+-`^i1%&fEaG$sgzkoz@Xs5$nvY%{->%1zkAf
{I1@(2v*`6x#gZrjQ8!<jJSroro6`jAr?+1&$uCLK%iA#2r3}iecYiN3A_!StNCHH)MTi@oG_(Fp=XIUn(64G6G67Na!gTwVL4w&
TrB2n#kDCuGS<@GVkdn*`uJSAw1Iv67(9N&;PXMU{U;LlV+=y;0jI7zABzbh_G7#e#jd|8rT&i7=s$KP_v0bSefH1c<!^6~RDAq9
^3H_1|31F>a4Hh>f!>ba|GV$f18wZ4gVAZKUu+1;-vE5Svd1J$+}{X({|I~`*OQS-yI4B;sPfp#&-LDVTRZ3X4@E#r=qFl{WV~S0
A6wb&!bqD{^LgLze{eW(&Q}`{vHLb~!LQxN|GFEE?gq}x>d>0$4HjjLD+A!CO1lov2YklPVLy$$$@ckZG&bI!S(Eo7O(Y$=9dJf7
M#FZEAw3G~viuX72qsS7-6bbD5)5OXnQDD6e^E-}v(p3524N18reYL=kCu%_Z~A2^WM$sfVNI{W@kTcWz70da=@%+5OQp4}5?RVr
C?QP`=72#a3-c%!@e`dYbFxz_nU{mXk<o-34OEMnU?D1H-pL?USyu8$6B#tgbOx~I1x6bFmF3_&lND5hZ)>OBzTSh%Il26w7eBn4
{`TVS+mnPHogs~7N=$7jt9f?NpRm$@Is=8#Y+aEksWaH8q}l8i%k^pmY@fWGE({PDD<jIWAL<Z>+%#CeHF95xJBKrGwo`OKjA}a&
^lTTf8+m1b>T+sD<H&v<XuDbOZ0vFx79zIY43$h;pr$tEuTu~hrdGEFs`BKB2)e(ETRCZy7<QW?zqPD)2s4{{wKDCk5V3I?+qjvt
JL!Rj*Ng4W3;|5r-B@Dfgy?HT7s(+D_;G47=2Og=PhGBjN?Yzz(}T8T)ELxl$+(eC)9Jjqy1$uD$?basD_-0+Xg;!2SYU|&34gkW
nR<KCSE+R3JeiO4Q26r;D7@{>!{BctWo&%<4O~az#Quprcy^MU*fU}$T<y5Yz5TM=H+PqxL7biZ4!`4rYNlg%4DE-@H}8J>@uweN
yt|zK{Py)LnlUS4jmuo0^&E-AqfY6fUkaNxEY!`HO>+*|F}YK7RK*-1^UF3R8qeCt=XW3By6?<8EI4mIgY7?Ef3&|M%h+4jZFtYi
bCkQC2DZX|xvpXUOm1MAvMDEInR9a@?%Okl#|G-$P5Ie@LG0r#@YVF{%N`F$IJsv7h@)>>#jT!R0Zk|KdT%4u<Nir}iqJU8trYB^
xbFEQcLy|4cZGgAPt7nvj6U31M}ciwX1uo1$V`!ExlDbg1$zV^tU)*f#48kR2*Iw<@PvJu82-0clwh|&Mm3zCOke!+%hbw}>6_QD
-@UcJ-~RS;`ok};-(J3){`k{BE~nqW{vW3{ET_X#rc*P7WyR^#aQ$=&OL6S~e)Z(9{|8}km}v
"""

def digest(data):
    return hashlib.sha256(data).hexdigest()

def main():
    if not __debug__:
        raise RuntimeError('Assertions must be enabled')
    if len(sys.argv)!=2:
        raise SystemExit('Use: python -B recover_w_only_u2.py NEW_DIRECTORY')
    raw=zlib.decompress(base64.b85decode(''.join(PAYLOAD.split())))
    assert len(raw)==40625 and digest(raw)=='a06c5909d8d1994f5a95baa7430027ecfcd61ba3880e41ec9ad28a95e793bcc8'
    data=json.loads(raw)
    pins={
        'w_only_macro_u2.py':(14714,'3aa4d11717561bec576fe0c04087f12cd4aab64e744ede9b4d12e829da4dcf6b'),
        'certificate.json':(25502,'eb610ab904f7760da34492cee44348ea16699025805b678e84b8ae2c482f1115')}
    assert set(data)==set(pins)
    out=Path(sys.argv[1]); out.mkdir(parents=True,exist_ok=False)
    for name,text in data.items():
        b=text.encode(); size,h=pins[name]
        assert len(b)==size and digest(b)==h
        (out/name).write_bytes(b)
    spec=importlib.util.spec_from_file_location('exact_w_only_u2',out/'w_only_macro_u2.py')
    module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    assert module.S.__version__=='1.14.0'
    matrices,remainders=module.lower_matrices()
    guards=module.geometry_guards()
    report=module.verify(json.loads(data['certificate.json']),matrices,remainders,guards)
    b=module.wire(report)
    assert len(b)==29978 and digest(b)=='781531caa4f16f6a67cff553cf8623f3047369e320c4260ed621e1a97a701c25'
    (out/'report.json').write_bytes(b)
    for name in ('w_only_macro_u2.py','certificate.json','report.json'):
        b=(out/name).read_bytes(); print(name,len(b),digest(b))
    print('W_ONLY_MACRO_U2_V1_ALL_48790_ROOTS_ALL_SPD_CLOSED_FIVE_BOX_PASS')

if __name__=='__main__':
    main()
```

## 8. Most useful continuation

The literal W_ONLY_RESIDUAL affine orbit should now be treated as an excluded calibration, not as a surviving common-inverse test case. A productive continuation leaves the explicit box/collar and first produces an exact **complete** primal U1 escape packet, or enlarges this all-root stress-positive actual-shape domain. Only a genuine full one-sided survivor warrants further common-height conic and inverse-polar compatibility work. Separate successful local ports, or the known 233/435 controls, do not supply that survivor.
