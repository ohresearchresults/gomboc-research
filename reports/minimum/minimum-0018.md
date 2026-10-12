# minimum-0018

AI research report · 2026-09-07 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# DEG6_51318223_APEX_ROOT_UNSAT_V1

## Exact determination

**The complete unstable-root class `map 51318223, U=8` is excluded over its entire physical realization space.** No full-dimensional, uniformly filled convex polyhedron with the pinned five-plus-five face lattice can have vertex 8 as its sole unstable vertex. This covers **all eight stable-root choices, every reciprocal physical metric, all twelve of the parent's mixed maximum-choice strata, and norm ties**. It is not a bounded-box result.

The proof is a finite, exact computer-assisted theorem: a new actual-volume inequality closes the last eight escape-tree cases; the supplied standalone checker covers all **1,680** spanning trees. There is no numerical or SMT UNSAT verdict being substituted for the proof.

**No whole combinatorial type is declared closed and no attainer is produced.** The remaining unstable vertices of this type are `{0,1,2,3,4,5,6,7}`. The accepted global bracket remains **30 ≤ C_min ≤ 1374**. The journal's 178,131-record file remains its existing checkpoint, not a newly filtered post-exclusion remainder; I do not claim a new global record count. The inherited status was that all 74 types were globally open. :contentReference[oaicite:0]{index=0}

There is also a new analytic maximum-separation lemma for all three degree-six types. It reduces each of the other two types' twelve apex-root maximum-choice strata to an eight-stratum necessary cover, without claiming those remaining strata feasible or closing their entire apex-root classes.

## 1. Authority and literal incidence

The authoritative parent is `minimum-0013`, SHA-256 `51fed5c8515592d37f8508702b5a42df0fa7bc0586b3b3affe1528d1f0d2b365`. Its literal source and report were authenticated in this continuation:

```
degree6_roof_max_v1.py
11616 bytes
4f8ecf2c2f794cc4d9ace4794f1392b1c1e860f8fa78c935eab21608b70c45fe

degree6_roof_max_v1_report.json
25829 bytes
92d26a38f7380c9327ed4a2b34b906152df249fa32dba2cab4e57571ba375d34
```

No new conflict with the literal parent was found. The discarded identifier `46388460` is not used. The correct third type is `51318223`; its degree-six vertex is the **physical primal vertex 8**, not a polar vertex or a relabelled integration apex. The parent's cap/ridge labels and two-pyramid decomposition are the starting evidence. :contentReference[oaicite:1]{index=1}

The closed root class uses precisely these eight maximal facets:

```
F0=(0,2,3,4,1)       F1=(0,7,6,5,2)
F2=(0,1,8,7)         F3=(2,5,8,3)
F4=(3,8,4)           F5=(5,6,8)
F6=(6,7,8)           F7=(1,4,8)
```

Let `A=v8`. Only `F0,F1` omit A; they meet in the true ridge `{0,2}`. Consequently

`P=conv(A,F0) ∪ conv(A,F1)`,

with disjoint interiors. The shared triangle is `conv(A,v0,v2)`. The segments `A–v0` and `A–v2` are **not true edges**. They will be used only as integration diagonals, never as mechanical escape edges.

## 2. New actual-mass lemma: a paired-apex norm bound

Translate the **actual uniform-volume centroid** to zero. Write `⟨x,y⟩=xᵀMy`, where M is an arbitrary positive-definite physical metric, and `N(x)=⟨x,x⟩`.

Choose either ridge endpoint `r∈{v0,v2}`. Fan-triangulate **both actual caps** from r. Their six triangles have the form `(r,u_t,w_t)`. Cone them to A, orienting each tetrahedron positively, and define

```
d_t = det(r-A,u_t-A,w_t-A) > 0,
D   = Σ_t d_t = 6 Vol_chart(P),
ω_t = d_t/D.
```

These are the actual tetrahedral volumes of the same body. They are not independently selectable cap weights. Their exact first moments give

**`A+r+Σ_t ω_t(u_t+w_t)=0`.**

Every `u_t,w_t` is an actual vertex different from A and r. Therefore, for any b whose physical norm dominates those vertices,

**`N(A+r) ≤ 4N(b)`.**

Indeed,

`||A+r|| = ||Σ_t ω_t(u_t+w_t)|| ≤ Σ_t ω_t(||u_t||+||w_t||) ≤ 2||b||`.

In particular the universally valid geometric statement is

`N(A+r) ≤ 4 max_{i∉{8,r}} N(vi)`.

The maximum need not be guessed. In each of the final eight tree cases, A has a sole tree child b. Strict norm growth along weak escape arrows proves that b is the largest-radius vertex other than A. Hence **both** exact quadratic inequalities

```
h0 = N(v8+v0)-4N(b) ≤ 0,
h2 = N(v8+v2)-4N(b) ≤ 0
```

hold throughout the complete case.

This is the decisive change from the parent. We couple the actual A-apex decompositions around both ridge endpoints to a second complete volume decomposition with integration apex b. No centroid is imposed on an artificial eight-point body or on the polar.

## 3. Complete escape-tree coverage

### 3.1 Why every physical candidate enters the finite list

At a vertex vi that is not strictly unstable, some genuine incident edge `i–j` satisfies

`fi = N(vi)-⟨vi,vj⟩ ≤ 0`.

Otherwise the radial functional is strictly decreasing on every generator of the tangent cone, so vi is a strict unstable vertex. Distinctness gives

`N(vj)-N(vi) ≥ N(vj-vi)>0`.

Thus these weak escape arrows have no cycles. If A is the sole unstable vertex, choosing one arrow at every other vertex gives a genuine spanning tree directed toward A. This argument includes zero escape scores and requires no genericity perturbation.

The checker enumerates every eight-edge subset of the **fifteen true edges**, accepts exactly the spanning trees, and orients each toward vertex 8. There are exactly **1,680**. An independent Matrix-Tree cofactor calculation in the same exact checker confirms the count. Facet intersections, opposite edge uses, vertex links, degree sequence, and the four symmetry maps used below are checked as well.

The complete partition is:

| Certificate family | Rooted trees covered |
|---|---:|
| Root-direction cone certificates | 1,632 |
| Sole-child-direction cone certificates | 32 |
| Two additional shadow-only certificate orbits | 8 |
| **New paired-moment certificate orbits** | **8** |
| **Total** | **1,680** |

The 1,672 shadow-only cases reconstruct the earlier kind of cone exclusion with freshly issued exact matrices. The substantive closure is the last eight cases. The new proof does not require downloading or regenerating the inherited global cone catalogue.

### 3.2 The common-separator quadratic certificate

For a tree parent array π, define the eight weak-shadow forms

`fi=N(vi)-⟨vi,vπ(i)⟩ ≤ 0`.

For an integration apex c and a triangle T in a facet not containing c, put

`w_T=e_c+Σ_{i∈T} e_i`.

A certificate supplies one rational coefficient vector γ, common to **every** triangle of that decomposition, and nonnegative rational multipliers λ. Let

`C=Σ_i γ_i vi`.

If `S_i` represents fi and `H_r` represents a paired-moment form hr, the matrix checked is

`Q_T=(γ w_Tᵀ+w_T γᵀ)/2 + Σ_i λ_(T,i) S_i + Σ_r η_(T,r) H_r`.

The exact polynomial identity is

```
Σ_ij (Q_T)_ij ⟨vi,vj⟩
 = ⟨C,vc+Σ_(i∈T) vi⟩ + Σ_i λ_(T,i) fi + Σ_r η_(T,r) hr.
```

All multipliers are nonnegative. The checker proves **`Q_T-μI` positive definite**, with the exact μ specified below. Applying this matrix to the three physical coordinate columns, or to any factorization of M, shows

**`⟨C,vc+Σ_(i∈T) vi⟩>0`.**

But the actual c-apex tetrahedra cover P and have positive volumes `d_T`. Actual centring requires

`Σ_T d_T(vc+Σ_(i∈T) vi)=0`.

Taking its inner product with that **one common C** contradicts the preceding strict inequalities. Triangle-specific multipliers are allowed; triangle-specific separating directions are not used.

For the 163 canonical root-direction templates, the pruned ancestor tree contains the three marked triangle vertices. Its certificate is for `⟨r,r+Σ_T vi⟩`. The checker searches complete polygon triangulations by dynamic programming; integration diagonals are not inserted into the escape tree. For the sole-child test, r is the sole tree child of A and

`⟨r,A+Σ_T vi⟩ = ⟨r,r+Σ_T vi⟩ + ⟨r,A-r⟩ > 0`.

The physical integration apex remains **A** in that test. This does not assume that the convex hull obtained by deleting A has centroid zero.

### 3.3 The eight newly closed cases

Two complete parent arrays, with `-1` at the mechanical root, represent the new cases:

```
πI  = (7,0,3,4,1,8,5,6,-1)
πII = (7,4,0,2,3,8,5,6,-1)
```

Both have sole root child **b=v5**. Vertex 5 is an **integration apex**, not a replacement unstable root. The corresponding common separating coefficients, all divided by 1000, are

```
γI  = (841,-436,-658,-380,-93,1000,1000,1000,124)/1000
γII = (68,-82,-512,37,-444,1000,1000,1000,15)/1000.
```

Their complete b-apex integration triangles are

```
(0,2,3), (0,3,4), (0,4,1), (0,1,8),
(0,8,7), (3,8,4), (6,7,8), (1,4,8).
```

Every associated 9-by-9 matrix uses the eight shadow forms and the two actual paired-moment forms `h0,h2`. All sixteen matrices satisfy the exact shifted-PD test with **μ=1/1024**. Every multiplier is an integer divided by 1000; the complete arrays are in the inline capsule.

Apply each of the following literal face-lattice automorphisms to each array:

```
(0,1,2,3,4,5,6,7,8)
(0,7,2,5,6,3,4,1,8)
(2,3,0,1,4,7,6,5,8)
(2,5,0,7,6,1,4,3,8).
```

These give eight distinct cases. The exhaustive tree loop proves that, together with the other certified families, they cover **every** physical escape-tree possibility. No norm-order or stable-root choice is left over at `U=8`.

## 4. Continuous-domain, denominator, and physical-metric coverage

**Actual mass.** Both uses of centring come from genuine tetrahedral decompositions of the same uniformly filled solid. The cap-volume fraction is always `Vol(conv(A,F0))/Vol(P)`, with its actual shape dependence. It is never freed. The paired norm bounds are necessary consequences after eliminating the actual weights; they are not claimed to characterize all mass constraints. UNSAT of these necessary consequences is sufficient for the whole physical root exclusion.

**Positive definiteness and reciprocity.** M is any SPD matrix, including arbitrarily ill-conditioned ones. The fixed rational matrices Q are proof certificates on the vertex-index space, not extra physical metrics. Since U=1 at A is already impossible for every M, adding the polar with the **same M inverse**, any stable-root choice, and every four-component true-edge nonsaddle disjunction cannot restore feasibility. No independent dual metric or own-centred-polar assumption enters the argument.

**Denominator signs and gauges.** The proof is written on actual centred vertices and needs no realization chart. In the parent's adapted variables `vi=Zi/K`, `K=4 Delta^4 W_raw>0`, the added forms are simply

`(Z8+Zr)ᵀM(Z8+Zr)-4ZbᵀMZb ≤ 0`.

They differ from their physical versions by the positive factor K². No sign of Delta is selected, and no small nonzero Cramer denominator is discarded. The parent's negative-Delta domain therefore remains covered. Its denominator-sign treatment is explicit in the literal parent. :contentReference[oaicite:2]{index=2}

**Strict incidence and geometric boundaries.** Each facet is assumed to be the stated genuine maximal facet of a convex realization, with strict nonincidence and genuine extreme vertices. Every chosen facet triangulation then has positive area, and coning from a nonincident vertex has positive volume. There is no uniform lower bound on those volumes, angles, or slacks. Arbitrarily close strict realizations are included. A collapsed facet or changed maximal face lattice is not silently counted as this strict type.

**Norm ties and mechanical boundaries.** The tree reduction uses weak inequalities. Unrelated equal radii and zero nonroot scores are allowed. In the final Hamiltonian cases, strict radius ordering follows from distinct vertices and weak escape inequalities; it is not an imposed genericity hypothesis. The paired inequalities are non-strict. Strict positivity comes from the exact PD certificates, not from an unproved mechanical tolerance.

Thus the conclusion covers the original full actual-mass root subsystem, not only a sampled chart or the parent's new roof inequalities.

## 5. Additional analytic progress on the other two apex-root systems

This lemma is not needed by the finite proof above, but gives a genuinely sharper remaining cover for `5675263` and `14858559`.

Use the parent's mixed order `private(L)<ridge<private(H)`. Let r be **any** ridge maximum and p **any** private high-cap maximum, and let `c_L,c_H` be the **actual area centroids** of the planar caps. The true two-pyramid moment is

`a+3λ c_L+3(1-λ)c_H=0`, with `0<λ<1` the actual low-pyramid volume fraction.

Since `p→a` is a true positive escape, `⟨p,a⟩>N(p)`. A high-cap fan from p gives `3c_H=p+Σν(u+w)` with actual positive triangle-area weights and `||u||,||w||≤||p||`. Therefore

`⟨p,a+3c_H⟩>0`,

and the actual moment forces

**`⟨p,a+3c_L⟩<0`.**

A low-cap fan from r has `3c_L=r+Σν'(u+w)` and `||u||,||w||≤||r||`. Combining the two statements yields

**`N(p)+⟨p,r⟩ < 2||p||||r||`.**

In particular,

```
⟨r,p-r⟩ < -(||p||-||r||)^2 < 0,
1 < ||p||/||r|| < 3,
[N(p)+⟨p,r⟩]^2 < 4N(p)N(r).
```

The squared version is legitimate because `N(p)+⟨p,r⟩≥||p||(||p||-||r||)>0`.

Consequently **a high-cap maximum cannot be the high-cap neighbor of a ridge maximum**: the parent requires a positive true escape on that edge, whereas the displayed comparison is negative. For nonadjacent r,p it is expressly a **NONEDGE comparison**, not an added mechanical edge. The result holds for **every pair of maximizers**, so no tie choice is dropped.

The two still-open apex-root systems now have the following necessary maximum-choice cover. Each row represents every listed p separately; retain all original actual geometry, moments, reciprocal metric, root and four-component edge constraints, the parent's actual-volume inequality, and the new cuts for **all** maximizers.

| Map / unstable root | Low facet | High facet | Selected ridge maximum r | Remaining high maxima p |
|---|---:|---:|---:|---|
| 5675263 / 7 | 7 | 0 | 1 | 0,2,3,5 |
| 5675263 / 7 | 7 | 0 | 6 | 2,3,4,5 |
| 14858559 / 6 | 0 | 3 | 0 | 8 |
| 14858559 / 6 | 0 | 3 | 2 | 7 |
| 14858559 / 6 | 3 | 0 | 0 | 1,3,4 |
| 14858559 / 6 | 3 | 0 | 2 | 3,4,5 |

For map `5675263`, the opposite orientation with low heptagon F0 and high triangle F7 is entirely excluded by this lemma. Each map has eight remaining labelled maximum-choice strata in the displayed cover. The cover can overlap at within-group ties, but the universal maximizer cuts remain mandatory; an overlap is not permission to ignore another tied maximizer. No surviving stratum is asserted nonempty.

For self-contained continuation, their complete pinned facet arrays are:

```
5675263:
((0,6,1,4,3,2,5),(0,7,8,6),(1,8,7,4),(2,7,5),
 (2,3,7),(3,4,7),(0,5,7),(1,6,8))

14858559:
((0,5,3,4,1,2),(0,7,6,5),(1,6,8,2),(0,2,8,7),
 (3,6,4),(1,4,6),(3,5,6),(6,7,8))
```

The full remaining root-location status of these three types, relative to this handoff, is:

| Map | Apex-root status | Other unstable-root labels not removed here |
|---|---|---|
| 5675263 | U7 remains in the eight-stratum cover above | 0,1,2,3,4,5,6,8 |
| 14858559 | U6 remains in the eight-stratum cover above | 0,1,2,3,4,5,7,8 |
| 51318223 | **U8 excluded completely; no mixed stratum remains** | 0,1,2,3,4,5,6,7 |

All stable-root choices remain represented at the unclosed locations, subject to already certified inherited exclusions. Other C30 types are unchanged by this handoff.

## 6. What was tried, what is proved, and continuation

I replaced the single-apex maximum-fan attack by coupled actual moment decompositions. Floating-point shape/metric searches and semidefinite-separator locators were exploratory only. In particular, failure to find a shape or a positive numerical separator was never used as an exclusion.

The promoted certificate consists instead of literal integer-over-1000 coefficients and exhaustive standard-library rational verification. Positive definiteness is checked both by Fraction LDL elimination and by integer Bareiss leading principal minors, with their determinants cross-checked. A fresh directory containing only the new source reproduced the report byte-for-byte. This is a replay using two exact PD algorithms, not a claim of a separately authored full geometric verifier.

The proof does not need the journal's Stokes sufficiency theorem: direct actual cone moments are sufficient. Broader exploratory calculations on the other two whole root systems did not yield a complete certificate and are not promoted as exact successors.

Within `51318223`, the explicit automorphisms reduce the remaining vertex locations to representatives **0,1,4**. The most immediate next target is the ridge-root orbit `{0,2}`. The paired-apex identity still applies there, but the bound must use the largest remaining vertex after removing the fixed pair, with correct norm-order coverage. No such additional root class is declared closed here.

## 7. Complete recovery capsule

Save the following source **literally**, UTF-8/LF including the final LF, as `degree6_apex_513_v1.py`. It contains the entire certificate input, all facet data, exact verification, tree enumeration, symmetry coverage, and report reconstruction. It needs **no previous sandbox file, journal, graph library, SDP package, or solver**.

Executed proof environment: **CPython 3.13.5, standard library only, assertions enabled**. Reconstruction and verification command:

```
python3 -S degree6_apex_513_v1.py
```

Exact identities:

| Object | Bytes | SHA-256 |
|---|---:|---|
| Source | 15,920 | `a131e4b3bfc83a4badf4783e31210fa2a5798d8b24d7d2d0592b71fceec712e2` |
| Decoded inline certificate input | 11,249 | `495d0b1a1485870f6f47f5bd481dd56cc530fe464b22a969f7849b07d3eab8f7` |
| Whitespace-stripped base85 input | 4,670 | `caf4f249c0ef1abc8ad2861259926684a2de8551227998c6e89aa18d1dc445b0` |
| `degree6_apex_513_v1_report.json` | 209,265 | `5abb81bd624d7aca213b8a23be758b1cf5d118e7c335607dc243ec19c5469d15` |

The input encoding is base85 of zlib-level-9 compressed JSON. Its 163 canonical template matrices use shift **1/1048576**. The 28 exceptional matrices use shift **1/1024**. All coefficient denominators are **1000**. These are exact proof parameters, not numerical tolerances.

The report reconstructs every spanning-tree proof record, the complete facet/edge and automorphism data, and every shifted-PD leading-minor certificate. The hashes identify the objects; the following complete source reconstructs them.

```python
"""DEG6_51318223_APEX_ROOT_UNSAT_V1. Exact proof; standard library only.
Run CPython 3.13.5 with assertions enabled: python3 -S degree6_apex_513_v1.py
No numerical solver, external checkpoint, or sampled physical domain is used.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
from pathlib import Path
from math import lcm
import base64, hashlib, json, zlib

assert __debug__
PARENT = ('minimum-0013',
 '51fed5c8515592d37f8508702b5a42df0fa7bc0586b3b3affe1528d1f0d2b365')
PARENT_SOURCE = (11616,'4f8ecf2c2f794cc4d9ace4794f1392b1c1e860f8fa78c935eab21608b70c45fe')
PARENT_REPORT = (25829,'92d26a38f7380c9327ed4a2b34b906152df249fa32dba2cab4e57571ba375d34')
MAP = 51318223
FS = ((0,2,3,4,1),(0,7,6,5,2),(0,1,8,7),(2,5,8,3),
      (3,8,4),(5,6,8),(6,7,8),(1,4,8))
ROOT = 8
AUT = ((0,1,2,3,4,5,6,7,8),(0,7,2,5,6,3,4,1,8),
       (2,3,0,1,4,7,6,5,8),(2,5,0,7,6,1,4,3,8))
INPUT_BYTES = 11249
INPUT_SHA = '495d0b1a1485870f6f47f5bd481dd56cc530fe464b22a969f7849b07d3eab8f7'
ENCODED = r'''
c-pm^%Z?<+4Mq3<j9O>I!Fb1P?WO-<P>X>zum#(ifh5BM1pT}3VOHh4S`uJO$ew-#nGt+kUNY+E+vlJD`uXdR-+uY-(?4$?KK^|B
lfL$B(_2n;daI>RZ>fjrZKTOU2-`0)->2K3Zy)@p+g~L3arD|JGb?$jJ?Pt%g6S7wlqpQH#xa#vOy4)VPaj9iX&RxXscAv2u}F2d
GW99Onx|s=dkRwtTHIrf(<rs_`li=Qf5`#G)>@i!9c^l1Vr`D8OeI?7t*wm7dec5yu2bq-Q%fHDQ>yI3YLmLseTyYUeV?V%Vw_^v
mmDndr_SP*e77=3>N<#&VTqBoW78R0koH!GYqy5>7G($QlDkQ$7Oj;28nagDOYFndTS9$nb?T+JDW)`a*=8D8GbUN3Chca#R$Y0#
%lx0de*Wq9p-i`beEZ!uw-2|kpT7P6Hr@X9Z+&lnv=Fm?`YP8nWTrf6%ab%sZ#vBF$M3)W^xfb7`S}NYr!7ou!Poh}TJ8Tz#{caT
2hz6u?{#Yad(*mpzyC7L!J~t|^*Fs1le(rj%J~#I<rFxrCVXI1OZZ6sn`ReTHQA{)?K-+^dsh%eDVKycma-g;g|z)pwDTY({K!&8
l*F`R<dzjXf!N6fTg2QIUm;@p!m(3S3?<@89v=FV+mt;JnnEr&)2ZcW%$QMbu_wh=B<`jv*UL`|nnJ(@G?n6OtJW&!C0%W*Sy~k=
ZK_0kH0`+7Ayc;EvD&e4B~}&rrT3{T4MyU$S{|iFZy3J+NSrIRIKDJ1mSqjY*trpnog^b9M>UV^{5u22Z91j@cfhQ1@wWZiWxq&b
?qcT@IA%lnVAkERp1g^OOTYszl3xWzH6{0%wc!w>6-CY*LBV8tjWVq29KjSkqj=sLW*k{q7=wa3W|>-WAg2o{gfEJ_*}KVoV?coa
nS{?K;moE1h@3mGFNHH1FK=B@UKD3VKsQwZRV0o^4$V<OiJpe=u4W-b8wx%JpyY%_$|^-#8L6%Q?2A8t`1_}CzWnD`A)x<Gk1AmO
-#QilSLZl*@NMJAX6^BFPWe|o7+RMTh*F&icVs0*tc4`hj-p__^c3BHS+?y7hqpnc!J^6?KswEET7%nKe`-{dBHvgd&js@?Vghiz
La8})o>2#Rlq-m@a4{0mJ*r$9Q<qwKRw>X6JJ4nnk~l@FC1X`N#r=^7_(gpiorR^NkwB|KB0@nykzO{}Ek9JQHT-TDu1Wd7aiQeD
|MKNW$^Lu`AJ_j)|KI2T_y#XW04}#MM{kthNE#VZrq=K9N{D*LLC-_S{0(}#S6A88yfO>yf$jl9xyihgzSOhqrwMA`d9LN38}WT4
ydf_N5C)q8bqldYoye4bCH_l2%RYup?>sws+n&QWA!xv;#FI>^xYX$zNmG0~Ib6#xPRRlz(H|HN08}NPjNc96zvx#!$Uk1aIu(9K
MyaIYUR+rPNh&jJqNS7k{l3`;Dzr!j_hci#DjOnH8f7%ev@vCSp=Ps_B=8=IO(P5qFc=f8Zs=dI`$CDWK0!$xa%Tc514hiaxESGC
h+CabJS$)7Sp(F8A8Qz}At;{!CnY?%pZcZravWEn)EMG#;P$|xksX2ZMZX1(Ug%gtTcCgaTnKLb0snFaK5z#nOwE6sb5rq=x^vuD
YL>u+dnm(UCQ&3r9)^^JL7<{iMee1JH8ZGm=5kWPcBqDx#-Pfoy<h5BUFx-^laZ2-8H)x&JA%O?nK?TKl^1HBXYuuk7%~y_E{A~K
MuU=58P~$=A>jL$&qmPJSbijh!Zw!LNNFK*hcg7yw1j?^yKhfiAT*UeAxTL}kOSCBCkXov5o{AXbL5#`QM)4naANcx<U}l2a`&*a
wP7fDw=z}*gfDSsm`Y9fYS`tD?Y%zZ36?Denyc)k0I~pOg`Ko^b@l}T4BUY#M>@9%4L7>Ab}-p}XEP5Hm2x3AjR926oHtT&f%Cdc
w?%xx9cOs>CwiL9gb(a4d$Ict^|VJCTJkLV(exuEM6ef5a_j5#652{2t~=|*UJdSE4~N`3XWgruq4@2hxGk3l%GF3<_*OzaE7?Hg
10zWSCtBL>pz-SD5lImf_G`Ugso9)92~Hg%W0d6wTLGwbIsz_Titk;fP-Xj$GWrfX^yuK&AjR<WS6ZH?G$<tvwFM(Mg^;G|finPa
v!lH2O1OKYlN&~#Nxe^lkP}!(fZ8K43A@jFHrcAkDI|6xc?^8b1BThlS?ru}j8&-g5zaCA(IERW<47Kt?OMxX$3nM5XWNNhPx$Cm
3~#C$Ux`1V4Ol-vM~V9`St&8hDEvi)G5ge>i6Y2HR=tST#tSVgRyBcRB|l?u4|=Od<yTJ}leCOu-fmOkc?2<WhA~F_JA`|ca_bzV
5=f<7s5o$ji2V!JONxf%J+#U5N&}Kh(W#iMmwFaY7K$50-+2bjyZ8(dr0uA2yq4a;w){td*J~>QNXbLIIIT+UT6_}*Op}};XdjI4
>P%SZJ{(i+g@z}vbRyV@n@I4E0AiD%4Cv~4`@2jckpfX$lcOyhD*_1W^c~*{v#!$YQq5vRRTnm)Iz0^gIr$2dLBXn8uB%<FX@Hw%
OmVIdJ(ASQrI0V=*6Kc{i)WFred0V3v{IgA>TI<BAwny~msR0AqXD~;-xYb;ODcluWFqoZsDX^e^nkVjr<Gc+)$CA|acC#ynwR>9
&6q(!%6;gy$!9xuFf#-;N_3+kru0RojYCy8`W!_NwUgiUg)_}Tn4tv8mzsiB;qJ9`9OTyXKa2=w7nvb509LT_N(wh@6A(VhZ|e_s
Z-KA^!D+0cx1n`YHEi!Xk8{H|;-zT-GX_X@f;DV-m2F+N=c41m%rI@Fa5>kg+Q`84wZ>~LPlrVxU5n6Y0~Y5!%i_sLK;kaxO8n`m
K!~YNR87L!S*2RANAbv8W7*EkB|76TWDw|<omZCK`mJTzOl0Jry%%<75OUwI-x6KuV)0C)f)?fjWitk_UFn|D4pJB(msw#KgR?b=
Owa8ow-}C@IgO+akG~r877^^@`h&-!^I?US$4R8AZ$2Y6X6nf<#8)cIw1$C`!=ZmydG*P9TS^j%ebPDxhFT!G$mwSN{YZooY~7o)
NbRUP=b-xJbQW837OGnbf)XL>!rZ<K{0-yUnPd1g>_L|LV7%73lL08ascP3sR-B!=g*&iLm5CYB1(?q<T}dycTEKRGb`o}&vOJ(N
O&yjx&-jYZbQ#t*zpsJyw4<6$d}?P^3E#PoNIuz*`LOzw=RTqG8;J%sC`#c1m61vw?LvC7PxawNBDDzs{l^^z^ztnBG>n4e@a&e}
kNkHAz&3|Tp<aN2KGzJYUl}41N_wH>S@K8p>HzE1JLz1!Kjm@)cs)v=xHBMT3;~^c3Dcry6i5zp;fAd4Bmd03xabmFs`Ch{I~s^j
_vq9ko`n}5weakIjJF5CG%>QOp`OK7rWJg6k;lAYgRK%iJ|Mb~+nC&E1_gt`a|XDOQ4y#;0?RAuhplPIFP^=`ky82mY;NuRTwa$M
j`~@1ybxa_*hk{356m41S#Bl7#$q^0t(B?!?W>P$xVf#2z{@zUf1Zia_ThOfwW}fWvtx5|Nzv8Yl3%0xn2_5r9f>4gnn$}Dx<2sF
*^>;Pd~lqC2M%fjw~pQe^zl;9N_&x}8COZnGZTn?*2s)XFt<(t?BY-}BEr5>fHir6RR$)b;t-ue>XZD5#U<FEIw#N=3g(kCJU`_5
M)9dRzfiNLGjxi*M@Gs62pb%V8E9*5Cw^dY$f~2~!Yp%@QOVupq|6R-dp4!)Pd+K6U$aOhgIvjS<1DwwNk(JlSqpQo!RGl`@ow^3
eDT_RNt+&HDn$(4MViXkitT9-+&0mqsB990#i>->t=}+I4^~JGbUX#3q0x^Ug}20fkXubMxN>atA&vXt3QV=y59{x{dLcql=X+fh
V>MnO9GCAXKMh)}3m7RxD*fh~+jg8AMTYs23xW)T8venB)w6c0xeft}i0D_BOx1vBy12YatHWSPtdX;GU8nrvnw$&m5;yBN=r(Ad
XbdBiRG}I+>sEtCCMt<hZ7PwEK=kdh)s8f7IvW{RY)j|uR61)b7{hP&g^&!eLT&ry&roaRBjdSDxfpR>b}sx8x1@Q<JQ!>#`S;78
&?%m`dDb<jn&aKD!CE>*mM+a>MG$wAT4<KiegABhUSQ#4Q2)+zl3(4}89bezgT&&^E~;^Oc1xe<?yAz8XSZgxVxKmTud(YJ%xC*l
y*X!W>q(ux6MEE;p>CHC0$k`h6dzoXxOY<#2KAv%!>^8+Li^OZl-GKm`zH(Ec@FZ2suP`pgENs~yVp;LDZg$|a^;i!X#`O!)lMOm
ol`@@WB`hQfAE2p=aKAobq(t}{8KF5kxu0+8KsoZD5!kV8JJzmuQrI&i)SOaL-NS&Z0yi4Xk5uY@(6jie!E4kt14Y-pinUn(@)3M
%Z9{y4$rdm2zPl<tBsElQT?iOU+bIo+xZxMbW+vH(VDvbuvxZu3s<SdCx8|oSLEspcgr`SsD3t<nRvIus^v^N_vU%5xeUz*j$>DD
_9LH0GvqRGZA=v-BQF)`aMH66P(FWDxaIRtMI^s|Yd+JYkG6ae-*<e}5FbBz=N)9|%4fqu+DUDl5%`eSV0<43pU0Ayhiz7G>$-|g
F3Dj(tVGea?S+bIV7k}+!-mV>H-R5Ooy@cTbtxOiPrN)Uz^lK%!Y!@Md_E%27oaow;J$&&C$BNX`@C0pb$Zv;mqmV8pWj{guKLHi
7lHAc_j8!izq4-BxL^ML{*K+R)8M!7^SYq^R=Hn4-{CU+;_qu~yZ`;^(Dz?{`NMw!vOH_B
'''

def canonical(obj):
    return (json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode('ascii')

def zero(n): return [[F(0) for _ in range(n)] for _ in range(n)]

def quadratic(C,w):
    n=len(C)
    return [[(C[i]*w[j]+C[j]*w[i])/2 for j in range(n)] for i in range(n)]

def shadow_matrices(p):
    n=len(p); out=[]
    for i,j in enumerate(p):
        if j<0: continue
        Q=zero(n); Q[i][i]=F(1); Q[i][j]=Q[j][i]=F(-1,2)
        out.append(Q)
    return out

def add_matrix(Q,A,t):
    for i in range(len(Q)):
        for j in range(len(Q)): Q[i][j]+=t*A[i][j]

def positive_definite(Q,mu):
    n=len(Q)
    assert all(Q[i][j]==Q[j][i] for i in range(n) for j in range(n))
    A=[[Q[i][j]-(mu if i==j else 0) for j in range(n)] for i in range(n)]
    B=[r[:] for r in A]; piv=[]
    for j in range(n):
        d=B[j][j]; assert d>0
        piv.append(d)
        for i in range(j+1,n):
            for k in range(j+1,n): B[i][k]-=B[i][j]*B[j][k]/d
    den=lcm(*(x.denominator for r in A for x in r))
    B=[[int(x*den) for x in r] for r in A]; last=1; minors=[]
    for k in range(n):
        d=B[k][k]; assert d>0; minors.append(d)
        for i in range(k+1,n):
            for j in range(k+1,n):
                z=B[i][j]*d-B[i][k]*B[k][j]
                assert z%last==0
                B[i][j]=z//last
        last=d
    determinant=F(1)
    for k,d in enumerate(piv):
        determinant*=d
        assert determinant==F(minors[k],den**(k+1))
    return dict(n=n,mu=str(mu),integer_scale=den,leading_minors=minors)

def parse(key):
    p=[]; marked=[]
    def rec(i,parent):
        v=len(p); p.append(parent); marked.append(int(key[i]))
        assert marked[-1] in (0,1) and key[i+1]=='['
        i+=2
        while key[i]!=']': i=rec(i,v)
        return i+1
    assert rec(0,-1)==len(key) and sum(marked)==3
    assert 3<=len(p)<=9
    return p,marked

def tree_key(p,r,T):
    children=[[] for _ in p]
    for i,j in enumerate(p):
        if j>=0: children[j].append(i)
    def rec(i):
        sub=sorted(s for j in children[i] if (s:=rec(j)))
        flag=int(i in T)
        return str(flag)+'['+''.join(sub)+']' if flag or sub or i==r else ''
    return rec(r)

def fan(f,b):
    k=f.index(b); f=f[k:]+f[:k]
    return [(b,f[i],f[i+1]) for i in range(1,len(f)-1)]

def triangulate(f,good):
    n=len(f); dp={(i,i+1):[] for i in range(n-1)}
    for length in range(2,n):
        for i in range(n-length):
            j=i+length
            for k in range(i+1,j):
                T=(f[i],f[k],f[j])
                if (i,k) in dp and (k,j) in dp and good(T):
                    dp[i,j]=dp[i,k]+dp[k,j]+[T]; break
    return dp.get((0,n-1))

def cone_proof(p,r,table):
    # The physical cone apex remains ROOT, including for the sole-child test.
    out=[]
    for f in FS:
        if ROOT in f: continue
        ts=triangulate(f,lambda T:tree_key(p,r,T) in table)
        if ts is None: return None
        out+=ts
    assert len(out)==6
    return out

def edges():
    return sorted({tuple(sorted((a,b))) for f in FS for a,b in zip(f,f[1:]+f[:1])})

def spanning_parents(es):
    for ix in combinations(range(len(es)),8):
        uf=list(range(9)); adj=[[] for _ in range(9)]
        def top(i):
            while uf[i]!=i: i=uf[i]
            return i
        for k in ix:
            a,b=es[k]; u,v=top(a),top(b)
            if u==v: break
            uf[u]=v; adj[a].append(b); adj[b].append(a)
        else:
            p=[-2]*9; p[ROOT]=-1; queue=[ROOT]
            for a in queue:
                for b in sorted(adj[a]):
                    if p[b]==-2: p[b]=a; queue.append(b)
            assert len(queue)==9
            yield tuple(p)

def image(p,perm):
    q=[None]*9
    for i,j in enumerate(p): q[perm[i]]=perm[j] if j>=0 else -1
    return tuple(q)

def verify_template(key,nums):
    p,marked=parse(key); n=len(p)
    assert len(nums)==n-1 and all(type(x)==int and x>=0 for x in nums)
    C=[F(int(i==0)) for i in range(n)]
    w=[F(int(i==0)+marked[i]) for i in range(n)]
    Q=quadratic(C,w)
    for a,N in zip(nums,shadow_matrices(p)): add_matrix(Q,N,F(a,1000))
    return positive_definite(Q,F(1,1048576))

def verify_exception(row):
    p=row['p']; apex=row['apex']; n=9
    assert len(p)==9 and p[ROOT]==-1
    es=set(edges())
    assert all(j<0 or tuple(sorted((i,j))) in es for i,j in enumerate(p))
    for i in range(9):
        seen=set(); j=i
        while j>=0:
            assert j not in seen; seen.add(j); j=p[j]
        assert ROOT in seen
    expected=[t for f in FS if apex not in f for t in fan(f,f[0])]
    assert [tuple(t) for t in row['triangles']]==expected
    assert row['D']==1000 and F(row['mu'])==F(1,1024)
    C=[F(x,1000) for x in row['C']]; assert len(C)==9
    Ns=shadow_matrices(p)
    if row['kind']=='pair':
        assert p.count(ROOT)==1 and p[apex]==ROOT
        # Both caps contain 0 and 2, and no other facet omits ROOT.
        caps=[f for f in FS if ROOT not in f]
        assert caps==[FS[0],FS[1]] and set(caps[0])&set(caps[1])=={0,2}
        for r in (0,2):
            c=[F(int(i in (ROOT,r))) for i in range(9)]
            Q=[[c[i]*c[j] for j in range(9)] for i in range(9)]
            Q[apex][apex]-=4; Ns.append(Q)
    else:
        assert row['kind']=='shadow' and apex==ROOT
    assert len(row['L'])==len(expected)
    ledger=[]
    for t,nums in zip(expected,row['L']):
        assert len(nums)==len(Ns) and all(type(x)==int and x>=0 for x in nums)
        w=[F(int(i==apex)+int(i in t)) for i in range(9)]
        Q=quadratic(C,w)
        # Independently accumulate polynomial coefficients to audit cross terms.
        poly=Counter()
        for i in range(9):
            for j in range(9): poly[tuple(sorted((i,j)))]+=C[i]*w[j]
        for num,N in zip(nums,Ns):
            lam=F(num,1000); add_matrix(Q,N,lam)
            for i in range(9):
                for j in range(9): poly[tuple(sorted((i,j)))]+=lam*N[i][j]
        assert all(poly[i,j]==Q[i][j]*(1 if i==j else 2)
                   for i in range(9) for j in range(i,9))
        ledger.append(positive_definite(Q,F(1,1024)))
    return ledger

def main():
    packed=base64.b85decode(''.join(ENCODED.split()))
    raw=zlib.decompress(packed)
    assert len(raw)==INPUT_BYTES and hashlib.sha256(raw).hexdigest()==INPUT_SHA
    data=json.loads(raw); assert set(data)=={'roots','exceptional'}
    roots=data['roots']; exc=data['exceptional']
    assert len(roots)==163 and len(exc)==4
    root_ledger={k:verify_template(k,v) for k,v in sorted(roots.items())}
    exc_ledger=[verify_exception(r) for r in exc]
    assert sum(map(len,exc_ledger))==28
    print('ROOT_163_SHIFTED_PD_CERTIFICATES_PASS',flush=True)
    print('EXCEPTIONAL_28_SHIFTED_PD_MATRICES_PASS',flush=True)
    es=edges(); assert len(es)==15 and len(FS)==8
    assert sorted(sum(i in e for e in es) for i in range(9))==[3]*8+[6]
    # Independent sphere/incidence audit and Matrix-Tree cofactor count.
    uses={e:[] for e in es}
    links=[[] for _ in range(9)]
    for f in FS:
        for i,a in enumerate(f):
            b=f[(i+1)%len(f)]
            uses[tuple(sorted((a,b)))].append((a,b))
            links[a].append((f[i-1],b))
    assert all(len(v)==2 and v[0]==v[1][::-1] for v in uses.values())
    for pairs in links:
        nxt=dict(pairs); assert len(nxt)==len(pairs)
        start=min(nxt); seen={start}; v=nxt[start]
        while v!=start:
            assert v not in seen; seen.add(v); v=nxt[v]
        assert seen==set(nxt)
    for f,g in combinations(FS,2):
        common=set(f)&set(g); assert len(common)<=2
        if len(common)==2: assert tuple(sorted(common)) in es
    lap=zero(8)
    for a,b in es:
        if a<8: lap[a][a]+=1
        if b<8: lap[b][b]+=1
        if a<8 and b<8: lap[a][b]-=1; lap[b][a]-=1
    assert positive_definite(lap,F(0))['leading_minors'][-1]==1680
    facets={frozenset(f) for f in FS}
    for perm in AUT:
        assert sorted(perm)==list(range(9)) and perm[ROOT]==ROOT
        assert {frozenset(perm[i] for i in f) for f in FS}==facets
    exceptional={}
    for j,row in enumerate(exc):
        for k,perm in enumerate(AUT):
            p=image(row['p'],perm)
            assert p not in exceptional
            exceptional[p]=(j,k)
    assert len(exceptional)==16
    counts=Counter(); proof=[]; allp=list(spanning_parents(es))
    assert len(allp)==len(set(allp))==1680
    for p in allp:
        ts=cone_proof(p,ROOT,roots)
        if ts is not None:
            counts['root_cone']+=1; proof.append([p,'root_cone',ts]); continue
        if p.count(ROOT)==1:
            child=p.index(ROOT); ts=cone_proof(p,child,roots)
            if ts is not None:
                counts['child_cone']+=1; proof.append([p,'child_cone',child,ts]); continue
        assert p in exceptional,p
        j,k=exceptional[p]; kind=exc[j]['kind']; counts[kind]+=1
        proof.append([p,kind,j,k])
    assert dict(counts)=={'root_cone':1632,'child_cone':32,'shadow':8,'pair':8},dict(counts)
    report=dict(name='DEG6_51318223_APEX_ROOT_UNSAT_V1',parent=PARENT,
        parent_source=PARENT_SOURCE,parent_report=PARENT_REPORT,map=MAP,root=ROOT,
        faces=FS,edges=es,automorphisms=AUT,input_bytes=INPUT_BYTES,input_sha256=INPUT_SHA,
        counts=dict(counts),tree_proofs=proof,root_PD=root_ledger,exceptional_PD=exc_ledger,
        conclusion='No genuine homogeneous realization has vertex 8 as its sole unstable vertex; all stable-root choices and all SPD metrics are covered.',
        remaining_unstable_roots=list(range(8)),whole_type_closed=False)
    out=canonical(report);path=Path('degree6_apex_513_v1_report.json');path.write_bytes(out)
    assert path.read_bytes()==out
    print('COUNTS',dict(sorted(counts.items())),flush=True)
    print('SPANNING_TREES_1680_ALL_COVERED_PASS',flush=True)
    print('WHOLE_UNSTABLE_ROOT_MAP51318223_U8_ALL_S_UNSAT_PASS',flush=True)
    print('REPORT',len(out),hashlib.sha256(out).hexdigest(),flush=True)
    source=Path(__file__).read_bytes()
    print('SOURCE',len(source),hashlib.sha256(source).hexdigest(),flush=True)
    print('NO_WHOLE_TYPE_OR_GLOBAL_BOUND_IMPROVEMENT',flush=True)

if __name__=='__main__': main()
```

Expected terminal markers and exact outputs:

```text
ROOT_163_SHIFTED_PD_CERTIFICATES_PASS
EXCEPTIONAL_28_SHIFTED_PD_MATRICES_PASS
COUNTS {'child_cone': 32, 'pair': 8, 'root_cone': 1632, 'shadow': 8}
SPANNING_TREES_1680_ALL_COVERED_PASS
WHOLE_UNSTABLE_ROOT_MAP51318223_U8_ALL_S_UNSAT_PASS
REPORT 209265 5abb81bd624d7aca213b8a23be758b1cf5d118e7c335607dc243ec19c5469d15
SOURCE 15920 a131e4b3bfc83a4badf4783e31210fa2a5798d8b24d7d2d0592b71fceec712e2
NO_WHOLE_TYPE_OR_GLOBAL_BOUND_IMPROVEMENT
```

Convenience copies: [complete source](sandbox:/mnt/data/degree6_apex_513_v1.py) and [reconstructed exact report](sandbox:/mnt/data/degree6_apex_513_v1_report.json). The inline recovery does not require either download.
