# minimum-0025

AI research report · 2026-09-08 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# C32_MAP295_WHOLE_TYPE_ACTUAL_SHARED_MOMENTS_V1

## 1. Exact determination

**The whole canonical C32 type 295 is excluded.** Every full-dimensional, uniformly filled convex realization of its stated face lattice has **at least two strict unstable vertices at its own ordinary-volume centroid**, for every positive-definite physical metric. This is a whole-realization theorem, not a bounded search, a representative-coordinate calculation, or merely a new necessary formulation.

All nine incoming tree domains are now exactly inconsistent. The preserved U7 closure is reconstructed in full and incorporated into the same self-contained recovery. Relative to that preserved frontier, this adds the entire root-0 and root-3 domains: **two new unstable-root orbits and ten additional joint-root orbits**. Including U7, all three unstable-root orbits and all thirteen joint-root orbits of map295 are closed. The incoming source had left precisely six root-0 trees and three root-3 trees; it had already closed all 448 root-7 tree orbits.

The exact combined result is:

| Unstable root | Vertex orbit | Tree orbits | Previously closed | Newly closed | Remaining |
|---|---|---:|---:|---:|---:|
| 0 | {0,1,2,5} | 1760 | 1754 | 6 | 0 |
| 3 | {3,4,6,8} | 1760 | 1757 | 3 | 0 |
| 7 | {7} | 448 | 448 | 0 | 0 |
| Total | all vertices | 3968 | 3959 | 9 | 0 |

There are **34,736 exactly positive-definite 9-by-9 certificate matrices**: 34,536 reconstructed inherited matrices and 200 new matrices. Every matrix passes integer Bareiss/Sylvester verification; every new matrix also passes a separate rational LDL factorization, with exactly equal leading principal minors. The independent checker does not import the numerical locator; this is software-independent reconstruction within this work, not external peer review. The inherited verifier is additionally rerun unchanged. The new tree-cover enumeration uses parent-neighbor products rather than the inherited edge-subset enumeration.

This supplies no strict110 attainer and proves neither a universal V>=10 bound nor C_min>=34. The incoming bracket **32<=C_min<=1374** is unchanged. Relative only to the supplied catalogue and its already closed wheel192, the two whole-type exclusions leave **294 of 296 types and 21,662 of 21,682 joint-root orbits unexcluded by these two results**. Other parallel results are not counted or overwritten. The supplied journal is the authority for the inherited bracket and catalogue, not a new audit of the upper construction here.

## 2. Literal geometric input and complete tree coverage

The catalogue identity is `c32_catalogue.json`, 240929 bytes, SHA-256 `efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450930f704d`. The recovery does not need that file: the entire target lattice is embedded. Its maximal facets, in permanent order, are:

```text
F0=(0,1,4,3)  F1=(0,2,5,1)  F2=(0,3,6,2)
F3=(1,5,8,4)  F4=(2,6,8,5)
F5=(3,4,7)    F6=(3,7,6)    F7=(4,8,7)    F8=(6,7,8)
```

The true edges are exactly:

```text
(0,1),(0,2),(0,3),(1,4),(1,5),(2,5),(2,6),(3,4),
(3,6),(3,7),(4,7),(4,8),(5,8),(6,7),(6,8),(7,8)
```

These agree with the literal preserved source. In particular, the ring `(3,4,8,6)` is **not a facet and is not assumed planar**. Integration diagonals are not mechanical escape edges.

Let x_i be centered vertices, M positive definite, N_i=x_i^T M x_i, and suppose exactly one vertex is strictly unstable. At every other vertex choose a true neighbor p(i) with

```text
D_i=x_i^T M(x_p(i)-x_i)>=0.
```

Then

```text
N_p(i)-N_i=2D_i+||x_p(i)-x_i||_M^2>0.
```

Consequently the choices have no cycle and form a rooted tree ending at the unique strict unstable vertex. Weak escape equality is permitted. A global norm-maximizing vertex is always strictly unstable, even when several vertices tie for that norm, since its support toward any distinct vertex j is `(N_i-N_j+||x_i-x_j||_M^2)/2>0`. Thus excluding the unique-root alternatives proves at least two strict unstable vertices, not just failure of one chosen target label.

The eight automorphisms are constructed and face-checked. There are 3509 labeled spanning trees at every labeled root, hence 31581 over the nine labeled roots. Quotienting by the complete root stabilizers yields the 1760,1760,448 rows above. Both enumeration routes reproduce the same lexicographic parent arrays.

All thirteen closed joint-root representatives, written `(unstable vertex, stable facet)`, are:

```text
(0,0),(0,1),(0,3),(0,5),(0,7),
(3,0),(3,1),(3,3),(3,5),(3,7),
(7,0),(7,1),(7,5)
```

The stable-facet choice is unrestricted by the proof: U>=2 alone excludes every one of these strict110 domains.

## 3. The new physical compatibility certificate

### 3.1 Shared tetrahedra, not independent copies of their masses

For each selected vertex apex, triangulate every nonincident maximal facet and cone its triangles to the apex. Convexity makes this a positive tetrahedralization of the entire actual solid. Either diagonal of an actual quadrilateral facet is valid. The common physical facet coplanarities are essential: without them, the different recorded fans need not integrate the same body.

Let t range over the **distinct unordered four-vertex sets** appearing in the union of all selected fans. A tetrahedron occurring in several fans has **one and the same actual determinant mass**

```text
d_t=|det(x_j-x_i,x_k-x_i,x_l-x_i)|>0.
```

Write f_at=1 when fan a contains tetrahedron t and zero otherwise. Let chi_t be its nine-dimensional vertex-indicator vector; X is the 9-by-3 coordinate matrix; G=X M X^T; and C is the actual full material covariance. Put

```text
J_t=chi_t chi_t^T+diag(chi_t).
```

Exact uniform-tetrahedron integration gives, for every fan a,

```text
sum_t f_at d_t = D = 6 Vol(P),
sum_t f_at d_t X^T chi_t = 0,
sum_t f_at d_t X^T J_t X = 20 D C.
```

The second-moment identity follows from `E(lambda_i lambda_j)=(1+delta_ij)/20` on a uniform tetrahedron. These are identities of the same physical vertices, determinant masses, centroid, covariance and metric. The parent's distinction between full material covariance and between-tetrahedron covariance is retained. No independent row masses, false Loewner comparison, or polar-centroid substitution is used.

### 3.2 Exact dual lemma

For each nonroot vertex define

```text
S_i=e_i e_i^T-sym(e_i,e_p(i)),
sym(u,v)=(uv^T+vu^T)/2,
<S_i,G>=-D_i<=0.
```

Take h selected fans, use fan h-1 as reference, and write `h_at=f_at-f_(h-1),t`. Suppose fixed rational vectors gamma_a, arbitrary symmetric rational matrices K_a, arbitrary rational scalars eta_a, and nonnegative rational lambda_ti give

```text
Q_t = sym(sum_a f_at gamma_a, chi_t)
      + sum_i lambda_ti S_i
      + sum_(a<h-1) h_at K_a
      + (sum_(a<h-1) h_at eta_a) J_t
      >= 0
```

for every distinct tetrahedron t. The K terms are exactly the zero-sum cross-fan offsets: the reference offset is minus the sum of the others. The eta terms have the analogous zero-sum second-moment cancellation.

Multiplying by the **actual positive d_t** and summing trace pairings yields

```text
sum_t d_t <Q_t,G>
 = sum_t,i d_t lambda_ti <S_i,G>
 <=0.
```

All gamma terms vanish by the actual first moments. Each K term vanishes because all fans use the same total D. Each eta term vanishes because they integrate the same full covariance C, paired with the same M. The left side is nonnegative because Q_t and G are PSD. It is strictly positive if any Q_t is PD and G is nonzero. This contradiction excludes the complete tree domain.

Every new Q_t is **strictly PD over the rationals**. The inherited per-fan certificates remain valid by their original common-D cancellation. Equivalently, sum their matrices at every repeated tetrahedron; this is the displayed lemma with eta=0 and summed nonnegative tree multipliers. Thus one physical argument covers both the reconstructed U7 block and all nine new exclusions.

This is an actual exclusion, not merely a stronger necessary model: the finite integer coefficients prove that the necessary physical identities and escape signs cannot simultaneously hold.

### 3.3 Complete treatment of exceptional strata

For a merely PSD version of the lemma, equality would force `range(G)` into the common kernel of every Q_t, because every actual d_t is positive. Here every Q_t is PD, so the common kernel is `{0}`. No positive-volume coordinate eigenspace survives; there is no remaining repeated-eigenvalue, singular-projection, Jordan, rank-two-between-cell-variance, or four-dimensional coordinate-kernel case to sample or discard.

No bound on M, its condition number, coordinates, aspect ratio, or tetrahedron mass is imposed. Each positive mass may be arbitrarily small. Norm ties on unchosen pairs and weak escape equalities are included. Extra coplanarities of unselected vertex quadruples are included. A collapsed facet, coincident vertices, or zero-volume whole body is not a full-dimensional realization of this lattice; the proof is not presented as an exclusion of a different type obtained at such a degeneration. Singular physical metrics are not asserted to describe an admissible three-dimensional body.

## 4. Exact nine-case completion and what changed

The complete incoming parent arrays are reproduced below; `p(root)=root`, never -1. Ordinals refer to the independently reproduced lexicographic tree lists.

```text
root ordinal parent
0    667     (0,0,5,0,7,1,2,8,6)
0    706     (0,0,5,0,8,1,2,4,6)
0    708     (0,0,5,0,8,1,2,6,6)
0    709     (0,0,5,0,8,1,2,6,7)
0    711     (0,0,5,0,8,1,2,8,6)
0    1232    (0,0,6,0,7,2,3,8,5)
3    1085    (3,0,5,3,3,1,2,6,6)
3    1086    (3,0,5,3,3,1,2,6,7)
3    1089    (3,0,5,3,3,1,2,8,6)
```

A fan is encoded `[apex,mask]`. Bit f of mask rotates quadrilateral F_f cyclically by one position before triangulating from its first vertex. Mask 0 keeps all original diagonals; mask31 switches all five quadrilateral diagonals. Incident facets are skipped. This uses only the physical facets listed above.

The first five root-0 cases use the ordered pair `[[7,0],[0,0]]`. Identifying the two common tetrahedra `(0,3,4,7)` and `(0,3,6,7)` before imposing PSD is the successful new constraint. Root-0 ordinal1232 uses `[[0,0],[3,31]]`, adding an alternate physical cap triangulation. These six certificates need no second-moment term: eta=0.

Root-3 ordinal1085 uses `[[3,0],[0,0]]` and the actual second-moment cancellation. Its stored eta is 30420. The last two root-3 cases use the same complete ordered thirteen-fan plan:

```text
[[7,0],[3,0],[0,16],[0,8],[7,8],[7,16],[3,16],
 [7,2],[3,2],[7,4],[3,8],[7,1],[0,0]]
```

These are three apices with individually switched physical quadrilateral diagonals. Their 116 tetrahedron occurrences are identified to 44 distinct actual tetrahedra. The seven two-fan certificates each have sixteen matrices and 192 coefficients. The two thirteen-fan certificates each have 44 matrices and 1021 coefficients. This gives 200 new PD matrices and 3386 exact integer coefficients. The source reconstructs all coefficients; no numerical residue is declared to be a kernel.

Coefficient order is: nine gamma coordinates for each fan in order; eight lambda coordinates for each distinct tetrahedron in lexicographic sorted order, nonroot vertices increasing; 45 upper-triangular K coefficients for every nonreference fan, in basis `sym(e_i,e_j)` with i<=j; then the h-1 eta scalars. The verifier constructs **2Q_t with integer entries**. The integer normalization scale is 10^6. All lambda signs and all nine leading principal minors are verified exactly.

The numerical locator follows a fixed log-det barrier schedule; it is not an infeasibility oracle. All nondefault parameters, fan selections, QR order handling, least-norm removal of the free coefficient gauge for the final two cases, and rounding are included in the recovery source. Exact output pins reject altered regeneration rather than silently accepting a different certificate.

## 5. Nonplanar-ring physical control

As an implementation check, not a restriction on the theorem, the exact verifier reconstructs both height choices in this literal control:

```text
P0=(0,0,0)  P1=(2,0,0)  P2=(0,2,0)
P3=(0,0,2)  P4=(2,0,2)  P5=(2,2,0)
P6=(0,2,2)  P7=(1,1,4)  P8=(2,2,height), height in {2,3}.
```

All supporting triples recover exactly the nine stated maximal facets. At height3,

```text
det(P4-P3,P8-P3,P6-P3)=-4,
D=68,
B=sum_t d_t s_t=(280,280,396),
J=sum_t d_t(s_t s_t^T+sum_(i in t) P_i P_i^T)
 =[[1856,1456,2088],[1456,1856,2088],[2088,2088,3944]].
```

All 28 checked fan plans give exactly the same D, B and J. In particular, their centroid is B/(4D). The height2 control gives D64 and B=(256,256,352), reproducing the inherited integration control. These finite tests catch wrong ring coplanarity, determinant orientation and covariance normalization; the all-realization argument is the identity and PD certificate above, not these samples.

## 6. Provenance, authentication, and limits

The named immutable parent is `minimum-0023`, advertised SHA-256 `e98bce6278e66a9d3f6c8f0863d55e65cc1a1ebb3c239742c782107c5cc61815`, titled `C32_COMMON_MASS_VARIANCE_KERNEL_V1`. I used its actual-moment results, not its special movable-corner coordinate family as a universal map295 input.

The preserved later `C32_MAP295_ACTUAL_MULTIFAN_ROOT_AND_NINE_TREE_FRONTIER_V1` is treated as source evidence, not as an already immutable cancelled-turn result. Its complete 12022-byte source, every coefficient batch, its 2540458-byte report, and its original exact verification transcript were reconstructed with the stated hashes. The present capsule incorporates that source literally and reruns it, rather than promoting an alias or an unavailable artifact. The journal explicitly distinguishes preserved mathematics from immutable-result insertion.

There remains an export-level authentication caveat already identified in the preserved response. The uploaded parent-Markdown suffix has 45639 bytes and SHA-256 `7924c974570cac1f64254eaca90b4a0e7337f58f42cabe4237c62e1a55458e19`, which is not the advertised immutable digest. The cause is not established; I do not silently reconcile them. Its embedded Python source does match 15812 bytes and SHA-256 `dea16976288841caf9361815ab1812525ae8d5681f94f0e344e16f58aa5119aa`, and its exact replay reproduces the reported output. No semantic facet, label, incidence, or parent-array conflict was found. The new theorem depends on the fully displayed lattice and self-contained physical identities, not on recovering that export digest or an inaccessible parent object.

The external paper by Bozoki, Domokos, Papp and Regos supplies methodological precedent for numerical SDP discovery followed by independent exact inconsistency certificates. Its published seven-vertex result is not substituted for the project's stronger inherited bounds, and historical priority for the shared-tetrahedron/second-moment construction is not asserted.

## 7. Complete recovery and observed verification

**A clean directory containing only the capsule below was actually run through full reconstruction to `C32_MAP295_WHOLE_TYPE_RECOVERY_ALL_PASS`.** Both old and new coefficient JSONs were reproduced byte-for-byte. A fresh extraction of the supplementary archive was then checked with only the standard library; all twelve manifest entries matched before and after exact replay.

Executed numerical environment: **CPython3.13.5, NumPy2.3.5, SciPy1.17.0, OpenBLAS0.3.30, Linux x86_64**. The sources set `OPENBLAS_NUM_THREADS=1` and `OMP_NUM_THREADS=1`; inherited batch reconstruction uses four forked processes. There is no random seed because there are no random choices. Rational/integer acceptance and frozen-input replay require only the Python standard library, with assertions enabled.

Save the complete code below as `map295_whole_type_recovery.py`, UTF-8/LF with one final LF. Under the stated Python/BLAS environment, install the two numerical dependencies if absent and run:

```sh
python -m pip install numpy==2.3.5 scipy==1.17.0
python -S map295_whole_type_recovery.py
```

The capsule contains the **complete three source files**, compressed losslessly; decoding and each source are hash-checked before execution. It regenerates every exact input from source, with no parent sandbox, catalogue download, coordinate checkpoint, or omitted helper. `extract` only writes the sources for inspection and makes no proof claim. With the frozen JSONs in the supplementary archive, this alternate command avoids numerical generation entirely:

```sh
python -S map295_whole_type_recovery.py check
```

Source and output identities:

| File | Bytes | SHA-256 |
|---|---:|---|
| map295_whole_type_recovery.py | 17357 | 0928b6d133bc6f3f9494fe93bed29fdf4b287eeaefe6c26707da2cb6b2eee54c |
| Decoded three-source JSON | 31933 | 04c29028ca73ee135f7b993e9fde678302b3c1e098174c851472af2d03b2a5fa |
| map295_recover.py | 12022 | 7ca6b8c0f0c8c9185e31dd3052ea97796bcb1f14ee0d22eb8332762f00f71af9 |
| map295_complete.py | 10855 | 749bf2cc3a9c74f41793b07395c74f4e4a58e950649e47727d8657cbfff283a8 |
| map295_shared_locator.py | 8227 | 6fb448556779d6ddaa687853af81a3926b6457e6e70e6fe6e0d784ce3f7eea63 |
| map295_exact.json | 2540458 | f80dce272dc5835c84c192a2cb3d48ece6cad6e662f0a4c211f5c6d3743fd669 |
| map295_completion_coefficients.json | 22813 | 20ba375e6dc2e7473b374c592250eed0af3b804558aff6dd5d39f3408fc906cb |
| map295_whole_type_report.json | 2956 | 054e7b5a4c6162187cc51caac0c42230fc613b6ea1ecb5fd0d953aedee12ab78 |
| CLEAN_REPLAY.log | 3150 | 27ade775e14459380834b93b340c9ebab5590f93538af5d1e8de0f0f0322756b |
| map295_parent_verify.log | 437 | be4023e860675b7e00a38496ab39359c7eeb1ceee068d8c3fb493570b36fa698 |
| map295_whole_verify.log | 547 | 3eae19a0f9504b0268265c54ce12b0f3efab3621fe2b755a150d045fd7450727 |
| map295_locator.log | 679 | 60c09ce3673200899ae02918053fd51a27c71bf7ac34adfa06749542d45808b2 |

The new independent verifier's exact ordered matrix-and-leading-minor trace has SHA-256 `b87d2322bced74a409da649f93ce96e15115238464d1c91ca1c04032540b1cb2`.

The decisive observed markers are:

```text
NINE_SHARED_MOMENT_CERTIFICATES_REGENERATED_BYTE_IDENTICALLY 22813 20ba375e6dc2e7473b374c592250eed0af3b804558aff6dd5d39f3408fc906cb
PRESERVED_3959_CERTIFICATES_AND_U7_CLOSURE_REPLAY_PASS
SHARED_TETRAHEDRA_AND_SAME_SECOND_MOMENT_9_OF_9_PASS
NEW_RATIONAL_LDL_AND_INTEGER_BAREISS_AGREE_PASS 200
NONPLANAR_RING_ACTUAL_FAN_MOMENTS_PASS 28
COMPLETE_TRUE_EDGE_COVER_PASS 3509 1760 1760 448
EXACT_PD_PASS 34736 CERTIFICATES 3968 REMAINING 0
WHOLE_C32_MAP295_EXCLUSION_PASS U_ROOTS 3 JOINT_ROOTS 13
REPORT 2956 054e7b5a4c6162187cc51caac0c42230fc613b6ea1ecb5fd0d953aedee12ab78
SOURCE 10855 749bf2cc3a9c74f41793b07395c74f4e4a58e950649e47727d8657cbfff283a8
NO_UNIVERSAL_C34_OR_V10_ASSERTION
C32_MAP295_WHOLE_TYPE_RECOVERY_ALL_PASS
CAPSULE 17357 0928b6d133bc6f3f9494fe93bed29fdf4b287eeaefe6c26707da2cb6b2eee54c
```

### Entire source-only recovery capsule

```python
"""Complete source-only recovery of the whole map295 exclusion.
Run in an empty directory. Default: reconstruct and check everything.
Numerical generation: CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0,
OpenBLAS 0.3.30, Linux x86_64, one BLAS thread per process.
'check' uses only the standard library and the frozen JSON inputs.
'extract' writes the authenticated sources only and asserts no theorem.
"""
import base64,hashlib,json,os,subprocess,sys,zlib
from pathlib import Path
assert __debug__
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
B="""
c-rlKYkS)^67Ki&E10HPkut1`x?h5{vMnc0e7BRPRa7k{QZj9cR7lE}oo0XgnHd1QNV1c*d%m1!w;P)z?t_`Z0P_y~<%gLyFEy)!
kw2SHoyaN7?|*3h@QME0EtdvIol{Ky_07p)cX0XJX?M`sy?oy}99+EVoOkyIM<++!<I9V|2ea_W>n^QPqy^4=YTdWA-P8N%%J;N#
!7LZ5Oba8+v#r3^rtUDXf_u&PruS{l3PUG|T;B^d$Fqi0$A+2?y!j#uH7jtSx)G#B!D19Swl=)iqAN$UM%ZD?yLY{brut4<Zyl(4
WX;3H)Pah`NIrS)Z0-k<c4dWE&^&V^Xw&znA-fKJ?~^wU{Fycmp!?JjnR{P;fIe#bGSl3Oum+Xo6kb1hVhq|~U^~ObWH9*T9e0kp
JoncqnET}IcXqoMT-S@tWEEC67(A6&m6`NZW;IrVClkIjSOuO+@TI}32K(e`;(vM>3f3X1%<8NLzblXd-)r#RFbtTbz1LkHLgyV@
{}L^Lbh>=g$33^t#y#ELGL08g$J56~-!P1^A82FE^)%|9hOaKZ29`H*bdk^a3RRz<oLoZpv8Q!--9JA$zC7rj(|~HVI*y?TeJ?^+
Oc+-KI!FVn7i&pcgVHLL2E(G{#%gjcDcW35t0zTGb2T|`)hv}uBC$qYDnYlAn4)Z%nZ-sG>4=5P@L#H3O02CX*3*TXtLfA-(B<^t
_=11QNzs#B3zC;>>1L@|DzRLBWYva^QE^-xHAYRdQFY3uZI_GHl4CXN^=5528k%FX;y6XSRC0!ma=BEmmBz*5xNchGW{$d{T5wP<
3&`ovLaACQR;mq_8#jvf$SKuJ_Ndw@S4WM?$ZVFZ(r8$=D-CDl)JB$Fb81+vRT-5`b6g$O>~g(Q9^19rN*huLL0aI^8IRqO>v&NZ
w_0kLWtJ-yhgP{>b!zsg<kTzm@(`*URhy+!wdgo@(HfVB4d`CAVU5Q%+pgN>=D1ubHpZi7u{Ij!jIW<O+ZltZ82L7^?9yljPP7Ps
=GaofUd-m9zGTSJgB#~Q<d?z1VWBg(0xR-^kn1@H|Fv?4v6cJu$;%l9QI~Frn&+;kqmUad7~PPgfQ$D+;8^xxcpo{TZnUMy6Za1d
CKXE|ys}Ew8hj~SIZNA}IANq42In~CJ*=h=waOk3K|N8EW6RSmHnYMTYE)Jo-OnA}GF(tcUZjEU)QT^;^|DEilt?AA>G<hoxdgTN
i-`BIH5AutM)K=;i<tv-aCDMnYE5&;nuUqu7AV@t^%jo&O7*{bb#461Y>oN2XSVuV<6g_eO0oKavy2=M)P@B*qlk)wv<E1UzOkYs
OeVC%wu$_&2mo~`5`_1&nG*%~0~p633LK;{(ZaswJ*l3C)K$)1&6$R<2GGbXHpFI7sbMm<3H=!wt37BM*zHN+FXkcd^;~T&9ZF*-
p+y)6Oqt!sEH-9ArAp<kMdU;Ae%lFo=tMd;YqZB9{{oA{gX7`1@ru6uD(AqRS-=kXIbMAV^T4-ZVbk+^>YEeH7Li3Okv^fyCRj@J
-4K&z@u>@}rTUIUrA8<dqo%OTgFDwnIq@wNrA2?(bta3*VYDn5KEIYcu(Cj48nb%WYE_VRAQ`?s<4%}iA<4%n(qQqJ?rU`7d>m3a
Byz!;&yl$-Ly^6Jok%2)<_f>VR5cQ*Q48A)`9L;D>@D)H&H7g;PNbx@3mYTu<6qRY1->6)0ZJ$8`Cx&7B6);|+-Dq%^xG(aIB26i
@)usji!?Ti_ax)Sog%jGQ6VnMs@WV}`R?d(o)N4XcS7__GKe<kqRM=8(~OI}Og3P&=JBL!x7O6PNo^(tlj=p~TIe{Q7@c^(yK<+F
8oSJ+<dHJBM78@Ch;Dlbs`N%?!o-4Q+q!GCU5@<_2~gMr%2TmcQXum=&21V{d5fEEKNz}F_h~6oTe4f9vxHfn#Mb8?a!#LHJ?xI`
57nx;Qb@&TA$Oz;aRkV7ludk>94Tg>m#amgx{-0A1n`|+sWfmv*d5O6LamwgT9JwqA4;~6T#dz$E$ytnX-Q7ptmKiAuYFh}cv?0<
IBr2(+r3AmlgjqSeM9K-lnBM9rurYI-=+x|%XK1TiGbqpsXIUbvz#mjR5_zTGfIz_hQ*LHx?1Q3?U&p4)bNtsE1o8`FUr_B95!U5
xReDeR9+wU%zl2<EA_XB@B^M;soJ*iBP12GNyWagW#OYrGBL@NNunKOz`&pCu;cMUcICK}tBB<9lx$x3kBoHj8%=rfyGUkyDgIrG
(}j6&O5?tys!Y*Oe4$kd3|35VmU9O;M_jK}SP#q(hX2adQXln^$j^C+*h{Z9AWH+9f`8>^txwA_?4p2T9I1xXKJ8Wd?6g<z8%(@5
vadDyn(CFRf^S#yx@dB{M7(N^<XUN{b&y@No2*I$<8kPEa>-Ln1A`-p1yKiOoAm7(TX*Bm+@xP`#j_E!<Y`|nWT-S?zo=tv#;T=*
0znC{co76$n^{Zo{*o74Gy;<EL{z3Uk}12*3LKSD8Y)d5L4|Kw32y^u%#VG~k(3fPA!$${xx{9IDpAN&W@CGg7u!1=`Lx`A3-%2@
P#uFr4$DToun_-5QkmcK-f3F&VePVs7xF~$CA&q2Ct<_nTQmfXcpbK1(ZZ&|9EFRSehW3h6s;)LikOn?OlR7ATinjBF)B@}>K&*I
^5nyKRamQ~^;R^9*>ubYnc)q)vc$Kg?2PDoMltJqYzLH(5+BJ6I0+gU)i@6=nvu7uGH*G@Z;9HnU090esILY>(Knf6PaOGT))-EG
lD5a8QNF|8QZ+2F?gqDb{DJIo%20|1KzXnLK^&lf6f3r(b4ORs=*F=JzyUyZGGFFI;Q1P}pnwZqHH7yYJywXsBh6JFAu}0s1HTWz
DAzk|!EV`zn=~iSwT^9v+9<CtZvVL4x?TKnX)w(#I0Y@bgF!$F7J?#1L5X{2X;ln(o%z~PbBGn=tli=pvQmD5#-`|!KeY!lD+-WU
I_#RMHd;I3rI*8}T)#aRZ?NBk{U^LXi1!D0w7~SI7i*4nz?bk!d<d`HafBZ_ob1YZm=fL&DO=dU8}a%bUIF8D=+&A|b+XX#M1dxO
-XI4OAWZgP77OE*3heRlDi-8kESHHsXen!F!`@88-B>7gW1$cX*lDlr#;)my+KpX5x*LOD#&!*jTQDn%5Nz&ohs(xbR<^^)3V?_6
ovlWmvSb(a2OtS$*{W3YdIu_x=|j8KrP`{-;`opvGOFN*9#r0<I{K)JA+?KpH80X#&aaI%#_4a|<oV+<XjmYt<oFd9?||m9BGFYf
HL28XGvU&8-d$y0m#KtUVr26@tIxW)UFzaQJoGFWQ+qYfwwcbft#Y9m3zd4l?R<Nmu^>VT4vWI<f;0}3!DMv)85qH^?9T56c>*%<
<Bs>+cU+L2%52_CCnG*%ICEC330sma)9AB1Bc|2JXRcy<nqOd^MN9nF7nGZZxk|+|K^I(rB!S2lH`vG*l`qiLzjvLft(_?q=Q(%(
Ohb^)6tAdTV}&4eX-Xx$0((j+1Gz`OO{@;ejyuba)B)LTbR<?onh;#X^Yf|kmDKk%F5Pbf2h030D}{vz#*v;ULA;?p30Z~i3S!>0
S7gx(w<@(wf_R%2#M{RO5jr8I@VU0<0#RUhJ+h`&unlwz?y10RIK5}E2!^1XAf1lL(|S6Gn<FRKmYY^OKF5{e9i5_p7<%CoGWd>5
5&l~O`A)1V{2lzj?X6y-9VuuMxzjT8Byh33L9dh|d`E_LWO2;V>bJj36y-=3EXqn@q@+*?m6&&F0FuTZ!*pNq-WWu0dyGn913^gS
zDF!4!VtsC@+6mA?pl419FJ)u()w3e6b28!Hgtq01N294g6s1guGACw0Z*>5yQug()FX*4xTy~M-&QFPi~e0)6+LFAsc3w!;{Q7e
=bDZj+Gp5RG&Z3-zIeOtZ*zJk?!jj)u%dB>phVm-9L#O~EPZ&3LU;y3*o;LFzXbjreG}(Oci7Fdl;~}iP?a&Y&-U+DO34m$E_=I1
o;3<$1v_{Wa+h8PWK*CB1LxND7a{0aPzZQ#9@{ZDYce=@Z$ZWGz*Y?YuhbBId{vaim0Z!+P2zmBWwJ*^I-R6}P;sgxzauA!e&6)-
)c&>HC%{f@;jqA&SuV^|z-{+-=G!`yW@>2h4kpQkn<z<1s(=QkC_$|zhQAnBe1tDug$X0<NW&aWsC|Z0wnk!7iF{u-jekmHSyx_k
GENm=3%29=xS@!A7$PaUl}VBLq{8xpzc@jpb9bbcRRnxwdVYG6j5rbE;2+&E8$4u28&(%iuAZrH*`c1!m-2Io&9`kkk7j<-VU^yy
Lxa7XXU&`($XD8>EB&}f?+-5z_B+P|JRu%*j`s$~2glvP<$1R|P##d>-Obbp0}7#WtkfhWL0@UN7~)64J*&qA{gqlqR%A{6$-)^3
&lC0084t~(RjF0$R-<W-Y_mMBjcX-)*sPef%FwP1%f({VX%-vys9Lowr%|_um1?nBE{^NPioM!ZAt107rGC+lR~S_c#b(KUCTuA#
ccOyP8GNRGOB$rQ-qQnRjWKxg0~@$=3NOM;3KHYYNX%23&AvRXSCz)zf%M5C-{ehdr$>ZEW_~cga>E%>o9g)FrOvg*seQ=51g##K
TjDqtEYPC(uOIh}TmyK3W4jZ+;t4d`V3fjMgSL6nzWkz&ZB|xBp{C`T4|>r}LwO-?fYJ=*Ah5~A@98-hNRA06z!L;uV6Zh{Fb30e
&}NPi!Hj;q0f6GvmZ(KY@|tn%i#M9s9IV6GFt8LhhO2QhS8HbUjdRb5FPOB@CBfl49f(OsKs!G0hlF@m#Kg~Gbxa+5_xygkqIud!
60fVSd`E*i<EwJnoX!Fb<sMvH6h${@){Vo{HmkNi?99%h4SI42t3@%^g=bhR))Q|!G*Z|+V;;nQ4Oux(QcE2WX4VgmdR$}&mMSdf
Hky&j=iL)TW}+MHj6r5RkQ49HlogwJMM!hgm`eSPdCQyfRv@paU!6;&2O$TH%&j^rCv<8g`<m3YO434!hFXYHs)dFqcn$Oml#)ki
WJaYbVl*pDnJP)L=AuX)oh7<{wZ;cjH!GfsP4dNgxmitoIYP|9tV>Et)xp0MTRrsWFtc8*uo^R~2svri`mCHJ)Daz0sWsrGSn0ER
t5>Ns82&4=O084@P4ktB8dGjg)Kj2HKm{9FJ+uj)6YDP0C#niMtu5m@Tcsb{mZG5onLi;x7s{1-xrV1g(UkW#Iy|s&?3N&}gg`kU
LW<Lz%EgYG3>Q+4=qPb88gg3JSVkcWZ7g*8068J#^i1=L?~c&w12PM^=rT*qlAPIcv({j9KXfDa))|0(0gD(UW;ljMM-`)pr)Qcg
?qu=$2P&LN3UD9?6>|})HUP^aB#?*VM_hS?Z6jA^j*^@Lg-~IrY&2aEX>whHu8kMd>9+0891p)*Q|$`qGI2ZyOi&=HHFY1zPonu_
ZDe`A2c4a2V3laXu0e>KW+C%hA*j_mUkg!dMcTrH!3?L4rp}u&mm7tef9Gkp{uFFKZG;<p-?bSrkwYC)^xIbS)8<$AA+?HYtUD^?
Xec3UBOIPP@tg#Zr~Ep8;6irX+O%OQfUda65Y+DqD((+vF~I>Aat0x9l)4jqWV8v1qpY{PD}U+?u*QK%mv&p>F2E@kD4iizG!Jmc
oI5@5UUbhtboT}*yo25DIT&pRyPeDK1=(!x>x13HlZ*G~-NAYH^sw{W;IwmbkxSJe@p_lt%k$2g?%sKa%3S~}4=%d9C&voPH)sw{
_Tk5B`Qz@dgY(Yi!O1ZgjfZ=ORQ%xhvilnB!yTym-~zhx8qG#5s+EexO!1Rr=+<%Pd~kkn{8|~GXm=_Ep(xcz7ur2JIz8-OqBZ)y
JHS<NuzT_W+M~SWl14Qoet^nJm+gLpHU_7AGB3)BmL{8q;-#H;k2(in@V?eEy%liBl(F3XxO@2i0tPRtdp{7$s;s>|0UF3Rvz)F2
=HcZ0GRM9PVuiL_FcNUB!C>qHcMMh_TWTIp-k<MwMYT|5tz!JPT6H`JgZIY=K)(whJ@D?}1TFjG07is_IXTAe!`e6)pqd*DV0|16
P<IRlxt7@5eDZ!^KdkL*erWxW%l-YmMd6dTincvo%uesMQh{DBMlQUV1+!i#GVRdy7E5i}s10hB_9u^W{v@)Tz%smZ*tyV(P_PVn
eGq5*5M3cH3tA_E>juu}g&PoF_wvfoX!nKM1r(?g2>VQ&5W<`1I5q)(3BD`)x{3&fihv3+Sa)cJPOZXX&~D-|W*SO6^bVfFd-!o@
1*o6l=>c;7Kf?2BT>D4czf+L$<4dST&spJQ@cH3kwDg15zn6}7k1rSd+r_JQwsXCk%a|`Yr`Z^eoLZ^gaB4NHX~SM_)EE~VwX$8U
I<@L(WLl;(9F|9=a<g73jp~h(S*(vBp=LJBDzYTVD|Y_BurCw{V2<8H0a5O=o`fjV6G4>WNkWw2NkWwS=~49vqzs7!Qik6IQik6I
QbxoLsw!+}GftV19>$8tY~AQf;REqBaLiH|#ssg76QU5yLYv|Eo<b}uRPrOB<);wKs^}x2<);wKqUhtG<tGu#F(~;F(DGA=Wtff~
WS?Aav>n`(U;O&zXz}w-xgK3Ef8TQ#LHPA*Qg2)}zvz3#->cpE-owwkSHJ(!J^FC|q4USby#4b-alZ5O`1zkNUkA^u=-+?(KR^HX
soA*So0<NbBmc(_?~jJNfp;|e*}L-pXaxN1`YiO_>5KOM)C!(``0-)szqt7E?y~vf*PW?R|M%x;=ij>Z=9Ot(HV%LJy_)AIe@=g0
bQasgKc{={<yo=H8|630bKm@Mx!Ak&rq9~HFPqEYl~Wznz0kS&&nq5&KH9BcE`Ph6-5-V@+6RB!n)`gV<Gp^pd~grnRDaZOYqhuU
_Waw%k3)az{kgcYzU=Mp{p!7U$NOKVZ|j3aclxevTK|62sDJ(W)i33r|26T7zdb*Getnm}|Bv~iQ4hU`xp6Z8v%37{`ni8|QF-?8
r*X4*cD7gDtCr5+{}}#WUHbR6yQ>$w7x~%gyYc>S$KL+iD1Y$&XFI>#$rs-__2=Wet;XoXVDRy{7X9|{iy56QN}ne$_8;~d&Wrq;
X8n)oL-6wX^U2wVi}%yY!!PIidwU<QzWgWu@ciuR+<mtDXZ_>nucu$ie@5rcFF&7*pV|5H*?sf=YPqzx?Z`iz@06e2{Odo(^Dm$l
ieJ6g2jL67d$>EuyUpE$y}M!MUk{aox7*{{tKW`({I_-TqVw+Xmlw~Li{s*t?@mc`4}nim0~c%ujljSO!3rZaUKlp2_|bOs9b8gV
d#oYtsG8yw?8#N0^G}};bKV>_t7Fh+V|z3l7VE=?GcMZIp*d{St>Um`S+z#Rs#Kc83TU#LRWA+gMtN9m*yT~9VVMn7#$ZdK=%-Ex
(Of)vPnvT5KoL~Z$J6faWp@wt#eWe*pT)EL8}aP^Kftqx)~%zXIl_DiX;0b`HZ>-$8qRImi|?_$(jayMQcyb?{P_y5VKb~D<WyP)
p0w9M4jUoo3CKZv8s)H#InV4l#i_IHNbebKpdGOdQV8dZ%}z6ziRf`iIn;=!;%PK_;?>n5mGrCTI5D350){?*5-Qft(DoZ3;YWbw
DZCI3K*EM6kKoGZ?6X=%DSLt(-h?iO+(v8i1dbfj*kmJ)`~rdG&NqPMlWzgZ$BJR($<idn0vRxEhXj6w6*B4xatMg|286ll2Lbdk
<G1nUg7?IsG@fO|!Xi$cr`FJ!P92*U+lUpPXzA*al9N@WIPqxs1fY_r${I3o00Sy|{Y|j1%rrV-OTfz&1+Njkat%|aKDfjjbB_M%
e6y`iXYpq{@@-$jtTV18{J!Es60Nl2!_hf3@v_*$U)-gNk{(EAq9ZLxFrM*dhEWvpR#D(F4HXFdv+VUI^dSMjCj<bWqyXTL<G(k<
zZD0m`6K|in(BlD)2I!B3dbi}oqAyu2o~wDo=ScjKEAH*=C<A;9_VB}lPMQVXM_8ZL_lf>n|Fl&QBH)7_*mHzA^RWk8>Z`6cOGU^
wT|>7N=%^oz1@+1L`uKu|70hF6tM~tkxhC@_#sAVk39K4az(SVv%A;bfBohlmsB8*)M5XDyZn(sxM`K2&cEfEdoC$lAP)&<#%)hA
fmsqZGkuV#2Pqg*8ibVcomljmfhDFui4XYpkV`qx)?FclQp%n}|0VCp#b)=2g34NRMwrJmc~_aV7bw3`pBUET%@|K<Jc^+4GGMkD
#qtPTtF$PLHSi>MrQg2EA`}sz1+9d<llQi6^0Retq8Dxv_#|Jc{&heU)S3cBMeb9eyBMTBv1T)Z5J6#r#^t>Pg6(7gc^PDnvxe>Q
B;<~8H&|<ey`eXWzgdwjZw)A;>X}+IPJ`Nt-2AMC4|;@Qzxi3e4G+>Wv<j$!Vp+J}Uxm+TF+g?&>Lrar;V9HYMhO|vs}@eUDMJ85
q3pKJ_Efsz*4au$A+70~BnigG!%6<32dohSTWn4H?Wr2O3}E8?x^<@T$v8Zfh&@PBlA&&?p(<HLj~){ulSl{yzHy?IroK@MWa9Yb
ycQNI9a4>aSVFRAS-a@HAa9&4>`yur*$}Dy=mAJSD<Q)4<lL;0aLD>~svSP7cYVk#BUP_RUtc!LM#}Fz^KTvddqO^L<kZ~Wk~tJ>
qHTH;^%&B+prDOgPz15ho@|1c%Wks<$BHeVicu3m95GKUxC2{@EeGR$Zd07Fpa_CnqRt}i(Qd^a?S+vsSQZ&SxNzCs-coc>@2^G&
iH>ZH5h~GC{+&=MDl`gw*rlh6=@bx!QBd0y|AawLOg<IyTT!Gk`DFIDWeHjasZ!gIGCiSqjQpehfNl1|n*O6OA&-lJJQ*ZptV9EO
Ssf!ojiB$|H^PaYj2IH5SqT{ut4qX|n?r_{oEOt8uB6EK1QuJ_@YGntQb2-WYZV?uxRqE!<PxOTSt$W);Xn=r1X;sSN6HXgkRvE6
h$Te7MV1gB#cNr<8Vc^2L<}XNKN})?c4Rn@h~deE@1*5vkMmlEq;ZGyOxW9B50PwN2N~wO-59iziD_(I2eH);`@q#;%E=SKl<{tH
H7qiqm`ECv3gXe?ZTfW}wns%U`|6Ofr`Jhg)aiDRI;)D)2;r%c&IxoH{&wCuI@lXvAILp{zKY$G<ID4tL*a{SYM}F*TCI{>-y~lL
WY|7Of07fB*VlGKdCdy?a|)X9TZ>|#<x>C)45JEQ-LT;^j!A|sY1R<R7vjMGjH1xJd4V9~^mQwK!)3?#siYRksZXZ0Frdl!W6nI}
rn6mVAd6Inn<bh%PeAx7t065?veDXI4)r_tXf3o4lIJHvFUVRIRlx*5;}n;6!FxCi8K(foPPZ3lNnM3Nb)t!j9iUM2cbS6M{dKEv
gYkmGh&8-3Hk!cL`6(K~ZO~;fBuiE`W!@C+VzQCNWBWL<iR~@3JzMbOZ8UzCSn$CC(bkWR_Odq(``r9Vr_#&bY|-andF^B}?TAdD
5C<i&ZbKJ;My|d5E?apmMCFcm#Xc3b76lw<(P+EN^!XH+)l8bzhOw1OfZ<`g`5BH`$49bkr5-vIRCm~&k=O+Ntqba_vi{J{d<m3k
x$r4nb+~2aZH9ECmTlN{9B%P<RESK%jcSd|+4ZWfWmVUys(RaJ38?Iy(AGm&*%UORfpxD#WjGU1W|l%w#mR?Tz3qd3vdCN0k-lV+
wP06HC{B^%>pxJ1(IgwG{k)7r)y8~#iH9ZIP&N<MPyLC^Op~HkRIF7DeUjme36@26nGl0uEk99l%KIkCs~@vt7|a_;W0*6}n9rBu
V}&I<RHnnwMW~Hhwa!R-T@SmIvzX;xZ@+S{b8Ojjmwk39CLWCH);VUJBCKpu7$Jxxyt!A{JZCv_=8=|UICQ<vbkYq1KUgJ;Hr|Ha
K#C^t%XY1aer}`)lckLIYpU_kpWZt989OlAzaFN0?_M+O`eyr;<=*7jud46b1V^&XWs6Z@!8ZKYLuM`A(BvllF7cAg{H6za+~okc
gt<!tmQz_SCK0qUymq0LAvAIb|EH2l36I%?y)k6x#a?Ty?6N4~YNcsqB%`(9g<>^dFdO;28*K>ntQX~U;UQSUk};{^a~yiRMsMsA
haBzS(@e8vGWZ9K^Lwv#%v#5N{stb!(~kIvPXg?EMH(>}^tLC=+}`<R*^l{R&c%fM&L9_qMHw{Iz~VX36gei&bOiiKTw!5A#r-tX
bm<pZrchHd$<r_jKg&7;urzI4q0EW_i+Egt?TiAxJ^5v>sDK|{qD<0ih7(sP7D0U^mtcTlXcpR@2b*sYke9{yW(?Sdc(`$d40Hj?
logsyoOgWNCUNR{UjL`LdNPvzQtCLkrshdoF8OlHn&#)|lMpi|w1}WWymKE@%ru(SIAOHfkH;_hcncW<%Ih$`^ax-Gd0wa{T2oH<
lD<HrOQ}~#_q>9&osO`87O)D@`Ht}tKE^dB#f5z!p)~{Oj2@|rm1qkNI-bqhh~w8boh9+?nIWxz%D!OVIE6}CaLY9ch`!S->Z)x5
DghxKj#~yas#9@;%U%mg80`l<I|sW-A5VQNf*e0lk-S;V=WDCk32Vt$ptAy)Ph%C({5cb+i<~-+2a7zsVh@~7x;C9zDi2_wNJ_|_
dtG=DlS7IaSHCHwAqkuy0FC^%DQIE0bD4@dNC!fQqYPPe4Y&_xbovSmus8x|hQBf>&mx8z79YLQXFlgChfI6o`?fe%B83M;1V$Jc
8N-F#T=TUvP<4!r2gsb~wsXMPvq#{~YjdQ+CouLPb?_B%e-(qA4O@&)X){q3>Y!;uOa<q9A`1!ypO9;dZ)6B0i)>NRTa8RqM`rfi
V3;wzw~1$mjy+;Pv_PFG6g2H&B=ULnY|7t&!M36l4m&g1NUrn;WRr5GN+9MW<cqR>E3(Di9NFTE$QFSX>OTp$BpldZ#9SU6?{z;S
^75#2d42%guOOJ!bqHp)xemLO0JZmZfk~sn=qpM?Ei*{V7^8`;i&5>V4%f7@wgN;Y%;U+qLO^C3jd7kiV?C&A20I`g-h;IoOz;dr
`tsBl<CQ6FjhxUm=%GRL6ie~kaN$mE5o<7+`a{@>dZ5a1(IzKcSa7^sH}Jh)?&P$4jG)EA@%y8}<(u<vXYT?gIA`YCnQTX=>p5uI
5l5^b>vN29hIUe4!;w3`C*6Q2v-Boc`#6W{lREf=;YrmvaJ{kLYn6f9koU{5X-{Q@b$T#RIT1Wc@Xee!51@v!$pX+xT~+|d!q}aH
L8e~8nw)rk;N*<B#|SxJ1jy8d@d7lw6CWv`20knh;i>OWyGv&Tnl?y{d$yQH?p$QSTUUWDv$+D~GrCOye)@Bc+ffAT$MaljRr^V>
Wm@@e(7iHS@uj$+;U!l2l1t4ZtjzERkGq8eV{`OBth=JzwY_xGL$qr*6nKW}T0~j9(bXnupuIb|^Mf0_{;k4h^8xB<XBqL?yfC3#
Ug%ZNLEASu!vGpNOBrY-qOOD@ah3(7Qp!kSG%R6_QHaD?Vvq_5w<vtUUVbfnp+V4ZfBsbglQbonJMRw;FLM-P!DLhmwrQ|@0s>Os
D87A~NSA`@3IS8SrCadC5tIcqNx&-tj9<tZ1(ZcS)7iX=p-lX}<Xuh&V&XLb1kNUU#m-+5L$+ZR%bp;nLdsN3oQQA3#~!4jXH=BP
e57wd0M?cI+K=59a$t%+0&(<s^vbFYg9gk~AuV91q!F;0K$9RyhnW1$RVZEiN`wn68$`d@f@@Flj-r4QTbw}8{1gs>Qn*69rPxd1
@$(|jDhElOO*1L)O@*pAUYq*8x2C2$Av>SJ>&2M<xNE9}=p61VEEg7(4;aow`*=O~9^Pp!AswV$Tz1a!=gBFH@#+lONsj0LZDhgs
2Ma(QfnyJ7W8w$td%E}Jg;973$4K+ygIbwYoUC0r8nBlmqG&Zy+4c;KcrVH@<60;|I~_{U&V&-QDLf#K8IU0YpS%-=^AE^Z16@&3
0imXDx1u||VaIHFBc}jcCe+e4E>8kiwtjUthUfnG7J0Q)--oHYz~d+aiY}0o_f(v~CPN`>COmB<FghQI%VfhsXoX!(i$kj*Q84Iw
w1Th~zF~CyQ<LL6432+rybmlq0cHnt1Eg^VyRUJ`V4(;sAkLJo$df1g&9;_4#McgZSKepQ*5pZl`0exjr;qYCo#OxP!+Qjeq%Zc-
H{A>*FNI0Y#K)lOqKJQqVn5dU6*J@xj8bP~9VV{{GK~2Aef*94p~kIo)U#L=^;Y}U7pMEr@dk@<4htPcAj*J2&H20#epxL7QFiPF
q>sU@({8Q6#jwLrVHq|F!)IKW2MpFhum(Q|`Zy|FGP)=NS42WQ(;}0@zXjmW+)>VG2REs6Ho4#hcv(<DD-%!xMgrDhE4b<RV`d=4
1x$I&OsVt6DVD$!m2LRFP1jt@qp2y6^9vG)0nR{(H1XF7KwVRKuH4Z;MnTxrpy1m-9+ifDfq(J9;9GnfRNLki(9lnLe;SGRry;yQ
s<+?i0BYcyJkkFy2ax2vh)HMj`mIQbpU261dZ3EK6o4~xe^GqOBG|RR>RZXUhRCZTGv+tAerT7o;+vUnMfrwsA7L#GQOiZ_U}r&g
H1UiRBD1&NBZ3$SZ%-I|d$cXC^)Pq-GgbRJ@%j8CmybFQWjnCMFzG5`Kyo&Y7<P5lj|z%bIZzuZ2Wo}Jv{KE0WA^rvFO{l2CKg-*
bAdumIa1|KW#p&%pCjsjj;Q}RqW<TI`v1!jh3ahz7S@x_DA;p>MNdk0RiDE41B`Q_P-E@P@f*5jZdWXll%j<+d>q}v^FzXi@EvLK
QL>lt5Hat8QTO}pogJC76Q}I-q!VdphY%Y_N6E7N=v9VyJYII5zLC&qzvZ!&e+TRCmeNn+l2C={7`nYhU%0>0NDeSZ82sD9aT!}Z
`AGaqx(ZJ-p<f>Mtv3r*9W3eH2)^at3M4aKaB_>6#!${}vn7z~IP?vxEeP|`k@|j^T30`^9hyNX#*U7dm@c{D0o!isjHm9LZfDko
*G)iq$tt3Nko2{{6qiD|h_cSqow#5y$D5T^n|)RgptTfU8a50n24HM(UP<l~hJMg>Q9zR|RdY+;7@YnS36Hjt24}BdL@W`~*v$H$
h`~0<!1-%e63b4d?<AH)Q(wT4!xsCg8G-$w$P<TQsJl_z2S*3v2Jcl77t2j8kNd-34j*#;LgW*>$$bH46FVXbK}d{GK_4u$nS7)B
@1o!6elr1EqkBHOC;Gv!4FrU*KtcF<Eq*>q!_j?;h<G7W=4xkBabj$<!Uoqi4p8n<kwz4L0$VA39%G;iYA1Yw-|)7i=VeX^ow5ew
tycS8yfsM_m%6VO5mRGVUhgb6n-RKLvyp-eu^}ex_4uoi0*UpLjWS-Bi!<v4GqCer8JZ)s$jZHoV+u$c&1JhdTtx6AXjLx~zEXYx
TM>*!8B_K0W%AjOTq2V6vY9RQqNHvuP2iu{F@k8juy(CzbbFqP#=-}NxxjQw4<Z$!1%$_{K7Nd??*uQM<v<(OxsM-vgfgpCTQSV6
Qtk64es<MoSAI^!X*6daKgO|&P86p9K2;|A^l8QMt-mehKK8ezi0xM|eOOZ>#y8Z+dJx>1xTOt!M{|a=#vWqbOykU_17lGbviC6S
bhU2Cdf0e7K4D6(WKJ0T=BWsznmD59r7i@1gt^68)7o{(gN@fEKXIx5f8hdUx-B`sevR_?T%ep`nkUSP@4w$T!V88Mf8&m0amn#*
KCVK_B0Nb|xbkN`U>M)N^>|Zl`FE)sklDLzt?$5W#M_TE*B{4s-BZPX>EdII&HC2O$KSZX`q4X)q3$HAOT5UiE_hi9wLaS%ek#t)
26!l_OVL}(a8z}}x)LKLXOBpv6uyk0VYQji^?YXq5*#wI0zt{oHzMoi$dUoNe+TqeOh*p-N0LyJlA->nLr<+(iO`C^PQ?@@H@ORV
h(F|V7qH=I+c31}+JP5Fj%Cv|lBt{BU|E251212n-fIi;yps-tTKA7q`_CIt;6nKUCDJFp?#hWTCX2tTla!W}Y2#nq5Q2Oba-k|c
^v`bQ8v2`I+%=RY72z5CN4*xa`n-3R@IFDA&%*RN^_hZ*@A>}GFUuZw3SVJM7dWs%wY(b^!Ul&nt@}spp2b^M(D2sWf=#d;;3aZA
HvuJNZ`>Itkd=J|;hcAl-{le#iB@tahkM7}UynK;b4&s9fD*|wzJRq8x^|KQ`@Gz~hm`Sj5nhQiEIKufPsHSyVEfo!-3=yi80BS8
u5xf0-sniEtkqRjxOwAcb>zOR326n(jZ-Ly_*zwl2{Xm6m<-+?)QiC)XzqbU_iY1E(<F!Tb%v$b3E*Y<*WAz=;&J#lxr9fc!({g|
&10zBUu^zSu@M2k*bSurS}zn5pJGF(6RTS@x~{4&p#^`dIrT^K61=F$zxgONh4gs>E7}l$6h<8d$Qq?TLIXWQ_yAxv28Idc<1#D!
69bL6u%uL}T`=gDeB+)-@)K=*mOQJau@q%k2c)KiWet{^{+nAsu+{@vbNKhyXoE6G^Gu>l(zw<5zSng~B$1y(cO+mn36Ky@(8Bs(
{*aWG>6wdoIhS9vx9+BZFKR8rnv{3{@B}e;dlW-ONV&t`1|PcT2m1%zy&Mx_D-69AwJ=o8B{y0Mj7ciK{yPB?vLgCxvfp))IZj39
;>^c#2M%5`in_-B)>WExzg_09S7)!&Jnz2l9(T`)SUbO6b_WN0kOvYE4}bga+Z?|MjQIM0{x3m^xxD
"""
raw=zlib.decompress(base64.b85decode(''.join(B.split())))
assert [len(raw),hashlib.sha256(raw).hexdigest()]==[31933,'04c29028ca73ee135f7b993e9fde678302b3c1e098174c851472af2d03b2a5fa']
M={'map295_recover.py': [12022, '7ca6b8c0f0c8c9185e31dd3052ea97796bcb1f14ee0d22eb8332762f00f71af9'], 'map295_complete.py': [10855, '749bf2cc3a9c74f41793b07395c74f4e4a58e950649e47727d8657cbfff283a8'], 'map295_shared_locator.py': [8227, '6fb448556779d6ddaa687853af81a3926b6457e6e70e6fe6e0d784ce3f7eea63']}
DATA={'map295_exact.json': [2540458, 'f80dce272dc5835c84c192a2cb3d48ece6cad6e662f0a4c211f5c6d3743fd669'], 'map295_completion_coefficients.json': [22813, '20ba375e6dc2e7473b374c592250eed0af3b804558aff6dd5d39f3408fc906cb'], 'map295_whole_type_report.json': [2956, '054e7b5a4c6162187cc51caac0c42230fc613b6ea1ecb5fd0d953aedee12ab78']}
sources=json.loads(raw);assert set(sources)==set(M)
for name,text in sources.items():
 b=text.encode();assert [len(b),hashlib.sha256(b).hexdigest()]==M[name]
 Path(name).write_bytes(b)
def run(args,log=None):
 r=subprocess.run([sys.executable]+args,check=True,capture_output=True)
 if log:Path(log).write_bytes(r.stdout)
 sys.stdout.buffer.write(r.stdout);sys.stdout.buffer.flush()
def check_data():
 for name,h in DATA.items():
  b=Path(name).read_bytes();assert [len(b),hashlib.sha256(b).hexdigest()]==h
mode=sys.argv[1]if len(sys.argv)>1 else'all'
assert mode in('all','check','extract')
if mode=='all':
 for r,a,b in[(0,0,880),(0,880,1760),(3,0,880),(3,880,1760),(7,0,448)]:
  run(['map295_recover.py','build',str(r),str(a),str(b)])
 run(['-S','map295_recover.py','assemble'])
 run(['map295_shared_locator.py'],'map295_locator.log')
 b=Path('map295_completion_coefficients.regenerated.json').read_bytes()
 assert [len(b),hashlib.sha256(b).hexdigest()]==DATA['map295_completion_coefficients.json']
 Path('map295_completion_coefficients.json').write_bytes(b)
if mode in('all','check'):
 run(['-S','map295_recover.py','verify'],'map295_parent_verify.log')
 run(['-S','map295_complete.py'],'map295_whole_verify.log')
 check_data()
 for name,h in M.items():
  b=Path(name).read_bytes();assert [len(b),hashlib.sha256(b).hexdigest()]==h
 print('C32_MAP295_WHOLE_TYPE_RECOVERY_ALL_PASS')
else:print('C32_MAP295_SOURCES_EXTRACTED_NO_MATHEMATICAL_REPLAY')
src=Path(__file__).read_bytes();print('CAPSULE',len(src),hashlib.sha256(src).hexdigest())
```

## 8. Unclosed domains and continuation

**No root, tree, stable-facet choice, unbounded-metric stratum, or positive-volume PSD-kernel stratum remains unclosed within this map295 theorem.** Other nonwheel C32 types are untouched by this result. The global strict110 minimum and any C32 attainer therefore remain unresolved here.

The reusable next step is the shared-tetrahedron first/second-moment certificate on another complete root frontier, with individually switched actual facet triangulations before adding further arbitrary apices. When exact certificates are genuinely only PSD, use their complete common kernel and the parent's actual-moment eigenspace/Krylov reduction rather than numerical rank estimates. No further map295 bounded samples or alternate-reference-center optimization is needed for this objective.

Supplementary files: complete frozen exact archive (`C32_MAP295_WHOLE_TYPE_ACTUAL_SHARED_MOMENTS_V1.zip`) and readable complete handoff (`C32_MAP295_WHOLE_TYPE_ACTUAL_SHARED_MOMENTS_V1.md`). The archive is **1125625 bytes**, SHA-256 **ee042bbef4a8b7c38800f3fa188dba8236d19762d0d0cf518f2ffd848f218f0e**. Its twelve-member manifest was verified before and after fresh-extraction exact replay. The separate release replay is 1103 bytes, SHA-256 `1fb6bfa7ff7cc1c18c80b44057ff7b66f4adafac9252b22eff741eb727cdc56c`. The inline proof and complete capsule, not these links, are the continuation authority.
