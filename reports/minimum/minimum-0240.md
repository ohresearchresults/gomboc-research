# minimum-0240

AI research report · 2026-09-25 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# H5_FULL_RATIO_Q_CUT_FOUR_CUBE_ALLROOT_NONZERO_PSD_V1

## 1. Result

**The full compact ratio interval is excluded, with the entire cut/q cube retained.** For every `(x,y,q,lambda) in [0,1]^4`, every one of the **48,790 labelled rooted primal trees** is infeasible for every **nonzero PSD matrix M**. Every genuine interior member consequently has **at least two strict unstable vertices under every SPD metric**. There is no coordinate condition-number restriction, covariance cap, stable-root premise, or weak-contact regularization assumption.

The complete certificate contains **5,982 distinct positive integer stresses**, **28,840 stress/domain applications**, and **239 closed all-root leaf cells**. Its **5,191,200 shifted positive-definite Bernstein matrices** pass **15,573,600 exact leading-minor tests**. On every complete rooted tree there is an applicable stress with

\[
\boxed{\frac{\sum w_{ij}D_{ij}(M)}{\sum w_{ij}}
<-\frac{3}{134217728}\operatorname{tr}M.}
\]

This is a full positive-ratio result: `rho=lambda/(1-lambda)` ranges over every positive real number. The ratio endpoints themselves are included only as their actual positive-volume, collapsed-label limits. No complete one-sided PSD surviving cone remains on the stated four-dimensional domain.

The exact predecessor is `minimum-0238`, SHA256 `d3964294432974c93c8579efb0406ab475aa488fc7524e04ed40baad8ab5d185`. Its 646 stresses were reused as search seeds, not as presumed ratio-valid inequalities. The supplied moving-ratio reduction was an input to the new computation, not an already completed all-root theorem.

## 2. Exact physical domain and actual moments

Keep `b=a=1/4`, `d=3/4`, `u=v=1/16`. Set

\[
s=1-\lambda,\qquad c=1-3x/4,\qquad p=(1-q)y.
\]

The seven unscaled basal vertices, in order, are

\[
B=((1/4,0),(c,0),(1-p,p),(q,1-q),(0,3/4),(0,1/4),(1/16,1/16)).
\]

Use `z_i=(s B_i,0)` for `i=0,...,6`, and

\[
z_7=(0,0,1),\quad z_8=(\lambda,0,1),\quad z_9=(0,\lambda,1).
\]

Thus the genuine raw domain is the whole `1/4<c<1`, `p>0`, `q>0`, `p+q<1`, `rho>0`, at the other fixed parameters. The maximal outward facet cycles and true edges are

```text
FACES = (
 (6,5,4,3,2,1,0), (8,7,0,1), (7,6,0),
 (1,2,8), (9,8,2,3), (9,3,4),
 (4,5,7,9), (6,7,5), (7,8,9)
)
EDGES = 01,06,07,12,18,23,28,34,39,45,49,56,57,67,78,79,89.
```

Every interior member is genuinely `10/17/9`. The checker verifies the 34 incident identities and all 56 strictly inward nonincident support polynomials on the open four-cube, seven strict basal turns, the top triangle, and the complete two-facet intersections defining all 17 edges. Integration diagonals are not mechanical edges.

At `lambda=0`, the three top labels coincide and the body is a pyramid with at most eight true vertices. At `lambda=1`, all basal labels coincide and the body is a tetrahedron. The cut/q walls likewise retain their actual lower-vertex or cofacial limits. None is called a genuine E17 body. The matrix/tree certificate includes every closed wall without deleting a small endpoint interval.

### Uniform moments, not transported centroids

The containing triangular frustum loses the four actual tetrahedral defects from the supplied reduction: the A corner, the R corner, and the two triangles of the O corner, each coned to its corresponding top vertex. Their interiors are disjoint. Their volumes and moments are subtracted from those of that same uniformly filled frustum; no independent physical masses are introduced.

For this family, write

\[
\begin{aligned}
d_A&=3xp/8,&d_R&=q/8,&d_0=d_1&=1/128,\\
A_B&=(31-8q-24xp)/64,\\
B_x&=509/3072-3xp/8+3x^2p/32+xp^2/8-q^2/24,\\
B_y&=509/3072-xp^2/8-11q/96+q^2/24.
\end{aligned}
\]

The actual solid moments are

\[
\begin{aligned}
V&=A_Bs^2/3+\lambda/6,\\
J_x&=s^3B_x/4+s^2\lambda(1-2d_A)/24+\lambda^2/24,\\
J_y&=s^3B_y/4+s^2\lambda(1-2d_R)/24+\lambda^2/24,\\
J_z&=A_Bs^2/12+\lambda/12+\lambda^2/24,\qquad g=J/V.
\end{aligned}
\]

Throughout the closed four-cube,

\[
7/192\le V\le1/6.
\]

The eight actual apex-0 fan tetrahedra have, in order,

| Tetrahedron | Volume |
|---|---:|
| 0128 | `s^2(1-q)y(1-x)/8` |
| 0982 | `s lambda/8` |
| 0923 | `s^2(1-q)(1-y)/8` |
| 0934 | `s^2(1+8q)/96` |
| 0457 | `s^2/48` |
| 0479 | `s lambda/24` |
| 0675 | `s^2/192` |
| 0789 | `lambda^2/6` |

These nonnegative polynomials reproduce V and J identically. The new checker also compares the **whole second-moment tensor** from this fan with the four-defect subtraction. For a tetrahedron of volume w and vertex sum S, it uses `w(SS^T+sum z_i z_i^T)/20`. For the containing frustum, its `xx,xy,xz,zz` moments are respectively `H4/60,H4/120,K3/120,L2/120`, where

\[
H_4=\sum_{k=0}^4s^{4-k}\lambda^k,\quad
K_3=\sum_{k=0}^3(k+1)s^{3-k}\lambda^k,\quad
L_2=\sum_{k=0}^2(k+1)(k+2)s^{2-k}\lambda^k.
\]

## 3. Exact 180-block stresses

For `X_i=z_i-g`, define

\[
D_{ij}(M)=X_i^TM(z_j-z_i),\qquad
G=-\sum w_{ij}\operatorname{sym}[(Vz_i-J)(z_j-z_i)^T],\quad W=\sum w_{ij}>0.
\]

Then `sum w D=-tr(MG)/V`. Every occurrence of V and J is the moving body's actual value.

Let `out_i,in_i` be the stress-weight totals, and put

\[
e=(-3s/4,0,0),\quad f=s(1-q)(-1,1,0),\quad k=s^2(1-q)/8.
\]

The two corrections are

\[
B_1=k(3out_1+in_1)ee^T/4\succeq0,\quad
B_2=k(3out_2+in_2)ff^T/4\succeq0,
\]

\[
G=R+yx^2(1-x)B_1+xy^2(1-y)B_2.
\]

R has multidegree `(2,2,3,4)` in `(x,y,q,lambda)`. The generally indefinite mixed `x^2 y^2` term is retained. The supplied source checks these identities on all 34 directed true edges.

On `x=a+hX`, `y=c+jY`, the discarded PSD terms are instead `h^3 y X^2(1-X)B1` and `j^3 x Y^2(1-Y)B2`. The implementation folds each negative local cubic coefficient into its quadratic coefficient. Its exact univariate transform, for a global monomial `u^m`, is

\[
T_{im}=\sum_{k=0}^{\min(i,m)}
\frac{\binom{i}{k}}{\binom{2}{k}}\binom{m}{k}a^{m-k}h^k
+\mathbf1_{i=2,m=3}h^3.
\]

The x/y folds commute: there is no `x^3 y^2` or `x^2 y^3` coefficient. Ordinary degree-three and degree-four Bernstein transforms handle q and lambda. Thirteen symbolic monomial identities verify the transforms with symbolic endpoint and width; this is not positivity inferred from sampled parameter values.

Every retained stress/application passes all 180 matrices H through

\[
\boxed{H-2^{-28}WI\succ0.}
\]

The final verifier uses **only arbitrary-precision integer and Fraction arithmetic**. It clears the exact positive denominators, represents symmetric matrices by their six upper entries, and checks all three leading principal minors. Numerical eigenvalues are used only for searching or screening; they cannot accept a certificate.

The Bernstein basis is nonnegative and sums to one on each closed box. The corrections are PSD, so `G>2^-28 W I`. For every nonzero PSD M, `tr(M)>0`, and `V<=1/6` gives the stated strict mean-arrow bound. No normalization or conditioning of M is assumed.

## 4. All 48,790 rooted trees on every certified leaf

The exact graph enumerator tests every nine-edge subset of the 17 true edges, finds 4,879 connected subsets, and orients each toward each of ten roots. It verifies 48,790 distinct directed masks and every complementary eight-edge dual tree.

A stress covers a tree only when **every positive arrow in that stress belongs to the same complete tree**. The 431 stress domains can individually cover only some trees. Their 239 closed leaf cells, using all containing stress domains, each cover **all 48,790**:

| Closed lambda slab | All-root leaves | Stress domains | Applications | Exact PD matrix tests |
|---|---:|---:|---:|---:|
| `[0,1/4]` | 158 | 301 | 19,999 | 3,599,820 |
| `[1/4,1/2]` | 52 | 92 | 6,696 | 1,205,280 |
| `[1/2,3/4]` | 16 | 21 | 1,596 | 287,280 |
| `[3/4,1]` | 13 | 17 | 549 | 98,820 |
| **Total** | **239** | **431** | **28,840** | **5,191,200** |

Each leaf has exactly **4,879 covered trees at each root 0 through 9**: **11,660,810 tree/leaf alternatives**. The verifier checks pairwise disjoint leaf interiors, total four-volume one, and containment in the unit cube. Their finite closed union is therefore the whole closed cube, including every shared wall. The exact cells, all stress weights, and their assignments are reconstructed by the inline recovery unit.

The retained stresses have 31,413 positive weight terms, maximum integer weight 3,008 and maximum support size nine. These are certificate statistics, not minimality claims or new graph-orbit counts.

For SPD M, every non-U vertex has a nonnegative true-edge escape and

\[
\|X_j\|_M^2-\|X_i\|_M^2
=2D_{ij}+\|z_j-z_i\|_M^2>0.
\]

A unique strict U would yield one of the enumerated complete rooted trees, contradicting its contained positive stress. Incidental weak contacts do not change this implication. Every raw complementary primal/polar rooted pair on this domain is excluded already on the primal side; no reciprocal or polar-density argument is needed.

## 5. What failed, and preserved actual controls

### Search failures were not surviving geometry

Starting with the 646 parent stresses, the locator made **9,312 calls**, accepted **8,785** new integer stresses, and recorded **527 failures**. It finished with 9,431 stresses, 242 certified discovery leaves and no unfinished box. Reduction selected the final 239-leaf atlas and removed 7,429 redundant applications. Every retained application was then independently rechecked by the standard-library verifier.

The locator uses eigenvector cutting planes and SciPy's HiGHS dual-simplex interface; a numerical failure is only a search outcome. The exact positive-definiteness and full-tree coverage checks supply the proof.

Three diagnosed failed-tree alternatives, enumeration IDs 16085, 19665 and 23895, all rooted at label 5, have exact three-arrow positive stresses both at `(x,y,q,lambda)=(1,1,0,0)` and at `(15/16,15/16,1/64,1/64)`. The former is the real five-vertex pyramid limit, with `V=7/192`, `g=(29/448,125/448,1/4)`; the latter is a genuine interior body. The complete trees, exact centred geometry and all six stress matrices are regenerated and checked. They are point alternatives, not substitutes for the whole-cell atlas. The final closed cover eliminates all the original failures.

### A real ratio change reverses a positive stress

At `x=y=1/2,q=1/4`, take the same physical metric

\[
v=(3,-2,0),\qquad M=vv^T+I/1000,
\]

and the stress `D70+D82+D94`. At lambda=1/2 its G is SPD; after actual ratio variation its weighted mean changes sign:

| lambda | Actual V | Actual g | Weighted mean | Strict `(S,U,H)` |
|---|---|---|---|---|
| `1/2` | `59/512` | `(601/3776,953/5664,123/236)` | `-11699831/21749760` | `(4,2,4)` |
| `1/4` | `697/6144` | `(15161/89216,8611/44608,1017/2788)` | `+71751423/570982400` | `(3,2,3)` |

Both bodies have the genuine lattice and all 68 true-edge primitives nonzero. The strict U labels change from 8,9 to 1,4. This disproves automatic transport of a fixed positive stress through actual ratio refill. It does not exhibit a complete feasible tree; the new all-root theorem excludes both bodies.

### Unbounded-conditioning controls

For orthogonal vectors `a=(1,2,-1)`, `b=(7,-4,-1)`, `c=(1,1,3)`, set

\[
M_L=L^2aa^T+Lbb^T+cc^T,\quad
N_L=\frac{aa^T}{36L^2}+\frac{bb^T}{4356L}+\frac{cc^T}{121},\quad L\ge2^{24}.
\]

Orthogonality gives the exact inverse and condition number `6L^2/11`, which is unbounded. At `x=y=1/2`, the whole-half-line strict censuses are

| q | lambda=`1/100,1/4,1/2,3/4,99/100`, respectively |
|---|---|
| `1/4` | `222,222,222,222,222` |
| `1/2` | `233,233,233,222,222` |
| `3/4` | `222,222,222,222,222` |

All physical weak counts are zero. The checker proves **1,020 primitive sign polynomials** on the entire half-line by shifting their exact quadratic coefficients to `L=2^24+t`, `t>=0`; polar rows are first multiplied by positive `L^2`. These are nonattaining physical controls, not a metric restriction on the theorem.

## 6. Actual-refill collar

For a genuine same-labelled-lattice uniformly filled body, matched uncentred vertex distance

\[
\varepsilon\le2^{-41}
\]

from any reference four-cube member, including a collapsed-label reference, preserves all-root exclusion after recomputing its own centroid. The eight actual fan tetrahedra give

\[
\sum|V'_t-V_t|\le33\varepsilon,\quad V'>1/32,\quad
\|g'-g\|\le2113\varepsilon,\quad
\max_i\|X'_i-X_i\|\le\delta=2114\varepsilon.
\]

Every arrow changes by at most `(6 delta+2 delta^2)tr(M)`, strictly less than half the certified gap. The residual weighted gap is `3/268435456`. These numerical constants are checked as exact rational inequalities.

An explicit full eleven-parameter cylinder retains free `(x,y,q,lambda) in (0,1)^4` and independently allows

\[
b-1/4,\ a-1/4,\ d-3/4,\ u-1/16,\ v-1/16,\ \sigma,\ \tau
\]

in `[-2^-44,2^-44]`, with `c=1-(1-b)x`, `p=(1-q)y`. Form the compact vertices, apply `Z=Y/(1+sigma Y_x+tau Y_y)`, uniformly refill and recenter. The denominator exceeds `1-2^-44` on the released frustum; matched-vertex displacement is less than `6*2^-44<2^-41`. All genuine basal guards persist. This collar is secondary to the full four-dimensional ratio theorem, not its replacement.

## 7. New continuation mechanism: independent d and a physical-cut simplex

Two additional exact reductions were derived and executed. **Neither asserts all-root exclusion on a free-d domain.** They preserve a smaller continuation route rather than leaving only an unspecified next parameter.

### Rectangular five-cube: 540 blocks

Set `d=1-3r/4`, `r in [0,1]`, retaining the whole `(x,y,q,lambda)` cube. The present theorem is the slice **r=1/3**, not r=1/4. The actual basal area becomes

\[
A_B=(31-24x(1-q)y-24qr)/64,
\]

\[
A_B-7/64=\frac38[(1-q)(1-xy)+q(1-r)]\ge0.
\]

The volume bounds remain `7/192<=V<=1/6`. Actual fan V,J, all 34 incident identities, all 56 strictly inward supports and seven basal turns pass polynomial checks. The r=1/3 pullback equals the parent full-ratio moments identically.

Only label 4 moves with r. For `e4=(0,-3s/4,0)` and `k4=s^2 q/8`, its cubic coefficient is

\[
[r^3]G=-B_4,\qquad B_4=k_4(3out_4+in_4)e_4e_4^T/4\succeq0.
\]

Subtracting `r^2(1-r)B4` in addition to the two cut corrections leaves multidegree `(2,2,3,2,4)` in `(x,y,q,r,lambda)`: **540 blocks**, not 720.

### Stronger physical coordinates: 150 or 450 blocks

The rectangular q-cubic difficulty is partly a parameterization effect. For example, in that chart the corrected arrow 2->3 has

\[
[q^3]R_{23}=\frac{s^4(4y-1)(1-y)}{96}(1,-1,0)(1,-1,0)^T,
\]

whose sign changes within the y interval. A blanket additional PSD q-fold there is invalid.

Instead retain **physical p,q** on the triangle `p>=0,q>=0,p+q<=1`. Use x,r,lambda independently and the same true vertex formulas. Then

\[
A_B=(31-24xp-24qr)/64,
\]

\[
A_B-7/64=\frac38[1-p-q+p(1-x)+q(1-r)]\ge0.
\]

The exact actual-moment pullback `r=1/3,p=(1-q)y` recovers the main four-cube. Define `f=s(-1,1,0)`, `e1=(-3s/4,0,0)`, and the preceding e4. The four cubic coefficients are negative PSD matrices:

\[
\begin{aligned}
[x^3]G&=-s^2p(3out_1+in_1)e_1e_1^T/32,\\
[p^3]G&=-s^2x(3out_2+in_2)ff^T/32,\\
[q^3]G&=-s^2r(3out_3+in_3)ff^T/32,\\
[r^3]G&=-s^2q(3out_4+in_4)e_4e_4^T/32.
\end{aligned}
\]

All **136** directed-edge/cubic identities are verified. Only the x/r folds are needed: the remaining polynomial has degree two in x and r, **total degree three in (p,q)**, and degree four in lambda. A degree-three triangle has ten Bernstein coefficients. Therefore the same physical domain needs **150 blocks at fixed d**, or **450 blocks with free d**. The source also preserves the optional four-fold residual.

The exact triangle coefficient for `p^i q^j` at Bernstein index `(K,L)`, `K+L<=3`, is

\[
\frac{\binom K i\binom L j}{\binom3i\binom{3-i}j},
\]

with zero when an upper index is too small. Ten complete monomial identities verify this basis. For refined cells, use box-local x/r corrections and ordinary affine triangle subdivision; optional global p/q corrections are not required and should not be mistaken for a completeness guarantee. The reduction is a sufficient certificate mechanism, not an already located 150/450-block all-root atlas.

The independent d release is now available in both rectangular and simplex forms, with actual moments, true incidence and exact reconstruction. The existing 5,982 stresses are useful seeds; their signs must be recomputed on the released shapes.

## 8. Recovery and execution evidence

The entire supplied 352,868-byte journal was read through EOF, including the literal parent; SHA256 `8442e05b8b00b017f8cb4f9969b329216d895d03b30735ab724a147c25925831`. Both supplied exact ratio materials were also read completely and matched their manifest hashes. No coordinate/incidence alias conflict or missing exact dependency was found.

The inline capsule below contains the **complete thirteen-file generator, verifier and exact input**. It regenerates the final 399,211-byte integer certificate from the literal 646-stress parent seed. It includes every numerical search/reduction rule, exact geometry/controls, both continuation reductions and all inherited helpers. Neither a saved final certificate nor a sandbox file is required for reconstruction.

Save it as `recover_h5_ratio_from_sources.py` and run:

```sh
python -B -S recover_h5_ratio_from_sources.py fresh
```

Complete weight reconstruction uses the observed **CPython 3.13.5, NumPy 2.3.5 and SciPy 1.17.0**, with single-thread **OpenBLAS 0.3.30**. The mathematical verification stages require only Python >=3.11 with assertions enabled and standard-library arithmetic. The master script launches numerical stages with site packages and exact stages with `-S`.

The supplemental bundle also contains a **fast replay capsule**, `recover_h5_full_ratio.py`, with the complete literal final certificate. Its command `python -B -S recover_h5_full_ratio.py fresh` needs only standard-library modules, including lzma. A directory initially containing only that fast capsule was actually used for the complete exact replay; all four certificate/report pins matched. The compact inline generator is the independent reconstruction route, not a hash-only reference to that convenience copy.

Observed markers:

```text
H5_FULL_RATIO_Q_CUT_CUBE_ALLROOT_NONZERO_PSD_PASS 5982 28840 5191200 15573600 48790 239
CERT_BYTES_SHA256 399211 9e535ce9a0622c721a1be80bc6e1a03228b8c83a3337e224b617571fad08ebb4
REPORT_BYTES_SHA256 279755 968cf95e7644c9a2279cfcd09136c3e7d6e77eb10f0f587b934328fb651e7445
MATRIX_STREAM_SHA256 2bbcf8d7d572931b768937af76e4b6434625e2b7106a5f20fad8ee8bcb54823e
H5_RATIO_TRUE_LATTICE_SECOND_MOMENTS_1020_FLAG_POLYNOMIALS_6_POINT_STRESSES_PASS
H5_INDEPENDENT_D_FIVE_CUBE_540_BLOCK_REDUCTION_PASS 34 56 540
H5_PHYSICAL_CUT_SIMPLEX_150_450_REDUCTION_PASS 34 136 150 450
H5_FULL_RATIO_SOURCE_ONLY_ALL_EXACT_RECOVERY_PASS
```

The exact continuation reports are 259,475 bytes/SHA256 `f3d0ef3bac23283c000148540974da4fee69cb9d15aa82dac67857da52fda61a` and 334,274 bytes/SHA256 `d1385460bf2568f32a34ac089bc7ed462c677b328dace35e77784ef630643d62`, respectively. The supplied four-defect reduction is also regenerated unchanged: 196,956 bytes/SHA256 `e3bbf10c36418e7462ddec6ba43b6c8a317cabbf6fee1ca6fbc12dff95a8ff88`.

The **inline source-recovery wrapper** is 38,570 bytes, SHA256 `b5abad746aa3e40b608d1f60c60c1fd0412b5104a6075e51e509a310d2a3cffb`. Its decoded thirteen-file archive is 85,482 bytes, SHA256 `170f14c25c9986dca8984e8a411c2a2c6117dc51479edb6d65e36b6d041d6659`. Every input file's byte count and SHA256 is checked in the wrapper.

The supplemental fast wrapper is 97,438 bytes/SHA256 `109ee8d944b362c6c5c4083980a5dce97088fcb4d931513c5f07d8a932ffda9e`; its lossless fourteen-file archive is 172,506 bytes/SHA256 `121e563ecdb5950d2bfe824d0c537f5362c6854507b7f67db24d31eb88636822`.

### Staged reconstruction and observed rediscovery

Observed numerical stack: CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, single-thread OpenBLAS 0.3.30. In an extracted source directory with no existing `ratio_discovery.json`, run

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B ratio_locate.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B ratio_reduce.py
python -B -S ratio_verify.py independently_verified
```

The complete source fixes the 13 initial directions, `diag(2,2,1)` congruence, scale 4096, 80 cutting-plane iterations, both LP feasibility tolerances `1e-9`, all acceptance thresholds and rounding denominators `10,30,100,300,1000,3000,10000,100000,1000000,10000000`. Initial lambda quarters are visited in order 2,1,3,0. Subdivision maximizes width times `(1,1,2,2)`, breaking ties toward the higher axis, with depth limit 16; three unsuccessful calls trigger subdivision. There is no random seed or time-dependent acceptance. The locator supports explicitly saved checkpoints.

A fresh source-only numerical discovery was actually completed using the included generator and exact seed. The final numerical inputs were compared byte-for-byte with the decoded inline sources. It reproduced all **9,431 integer rows**, all **242 discovery leaves**, the **178 subdivision nodes**, and all **9,312 call outcomes**. The fresh reducer regenerated the canonical final certificate byte-for-byte, and the fresh exact verifier reproduced the report and matrix-stream hash above. The unreduced library and complete discovery/reduction source are preserved, even though 3,449 of its stresses were not retained in the final atlas.

The fresh discovery checkpoint is 1,344,667 bytes, SHA256 `cc9e5fab9172854bcc97df1ffd8ace4434b558f86b782e30b4e0003604bb26d9`. Earlier matching-use metadata were not asserted byte-identical; they are not mathematical inputs to the reduction. The complete final-source execution, not a failed preliminary search, supplies the reconstruction receipt.

The expected final marker for the compact source-only master command is `H5_FULL_RATIO_FROM_SOURCES_RECONSTRUCTION_PASS`. The full staged reconstruction and the separately bundled fast cold replay were observed; no numerical solver is part of the final mathematical acceptance test.

Different numerical builds may change locator choices. The fixed-certificate standard-library proof does not depend on them. The evidence is an analytical reduction plus executed exhaustive rational certificates, not proof-assistant formalization.

## 9. Scope and continuation

This settles the entire specified cut/q/compact-ratio domain, and the stated actual-refill cylinder, under unrestricted nonzero PSD tree tests. It does **not** settle arbitrary remaining basal parameters, the whole positive-projective domain, the entire H5 incidence or the first E17 layer. It makes no all-family `S>=2` assertion and supplies no 110 attainer. The accepted global interval remains **34<=Cmin<=622**.

The most useful continuation is the **actual independent d release in physical (p,q) triangle coordinates**, with the 450-block mechanism and current exact stress library, or further genuine basal/projective geometry outside the closed class. There is no complete one-sided survivor on the settled four-cube that would justify escalating to reciprocal coupling there.

Supplemental copies: recovery bundle (`h5_full_ratio_recovery.zip`), exact main report (`h5_full_ratio_report.json`). The complete source and exact inputs below reconstruct every continuation-critical certificate and datum.

### Complete autonomous recovery unit

```python
#!/usr/bin/env python3
"""Complete source-only generator/verifier recovery of the full H5 ratio theorem.
Reconstruction: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, OpenBLAS0.3.30.
The mathematical acceptance stages use only exact standard-library arithmetic.
"""
import base64,hashlib,json,subprocess,sys,zlib
from pathlib import Path
if not __debug__ or sys.version_info<(3,11):
 raise RuntimeError('Python >=3.11 with assertions enabled is required')
ARCHIVE_BYTES=85482
ARCHIVE_SHA='170f14c25c9986dca8984e8a411c2a2c6117dc51479edb6d65e36b6d041d6659'
FILES={'h5_common.py': (6398, 'fbd425826da4bbd1b3ed91558718bdfb3ba4dec1c963154bb24f35dd730df1c1'), 'h5_ratio_exact.py': (10103, '035a7fef8c842e81fe97d06409370bd02686a0fba4874a38a59fd8d0863a2eda'), 'ratio_controls.py': (3971, 'f2fb12f1ae7a2b81d5cee24727bb91dce59132792a2edd7fe08ce177938a5476'), 'ratio_core.py': (3820, '063144501706ed675cb81f4c07a2f5711c6974845e46a51c511766ae776121a6'), 'ratio_d_next.py': (4695, '1b108c858b9bb99fbd40cd067969a9a8bda32c82305314e8caff99e44fb98312'), 'ratio_geometry.py': (4199, '91c9bb1c65b91e3db5fa62fafaaf32906c68100c65c26b9892f68e2bf07711d4'), 'ratio_locate.py': (4159, '187b0cc7b194badf9827ad4769364c4342266db57cbbe06e5c31fe9dba6d9421'), 'ratio_point_search.py': (1045, '64f541c32a432f3503751047d372a3a68c0eff3ea7f30eb454baecbd3a6d2684'), 'ratio_reduce.py': (4648, 'b3536bcb9b0d757981a91fa327f20d4ac120ca89c319b25ef0c16337a7c7ad97'), 'ratio_simplex_next.py': (6198, 'e0b4fb479a9ba7ece04123e76fd28cd9e52560f3f14893cf74b9ef4bb00fd56b'), 'ratio_verify.py': (5010, '3b8ce477de976bb3c3cf41399a96bd4c1d8e7cf5e5571922db994bb1dd5d1eca'), 'stress_locator.py': (1510, '6267d47a1d45c64928dc6eca0d2ae027e863c3765cdeafe1bcb8723c83c9e719'), 'qcertificate.json': (27865, '7d7d504bbedde84966a63894a6040679bdda0b22af267e6337bb06365fd1b084')}
PAYLOAD=(
 'c-riJ33uB#(%@gw^t^9G+OSRV&>7}!4kw*VcanA7na-zZ^(cw5Y3s5``RdL7_N^)aBtTNO(=+q!?t42uv3LLlpinmo;2%Go2cyYq'
 'u~;n+*LOele){WQj<)IMXq+sM;^lQ?eV3iDmfpAJx1aF8<J)MGHAMNwS-e`r+2-!(Y!j`|8`~_ICs`7wjZK_I$ugccW}DTbk)6j4'
 'coA=+dE@7xadj}+j^oBU+QiH3@Z0heT{NH@SJ0774BhB)kGtN>#^;}3xIwGo$E|7XPkg7{^4wPJcE{aGXX<t0AZ`aOC>sYn>iSa;'
 '9<|!D*0jrGr#tO9ey8JiI{`HE+j5&?f0EmHda#MIWYrkYSCdN^$}-J1+X*~bHlpRUv6@dCX$)njQ5H4MqwBaaj^ibaX|cMFr-up?'
 '-<CAE*(Rd8X(L&zSDUQyMm}gnY2%G7goDpkt9f1s5C{m4s3Kc$R#WJ}x21e}k*=03y-VT2tg&2WjnQZtkGE%|QDe1fz>CA{c#}fa'
 'QL>z^o>?B_-0p3nB#j#<+hvw4;^WO`wXvF?X!07*L+_At20colAJo}+8I9-hv}u1^zIpNL_;YAkEfz4JdCX;;IX1I8tj!$8;i}DA'
 '^n}B^j?KO;8{&Ufmv!Kg2d}zN(T86jfV5c`u3GRLP~{HXLp$G=$FJW)OWAfkkF69&8c(f1j5}*KNQP`Su#$al|HnLDS~GiSW93H8'
 '|7L)VStD6CXasbd;O!<_p2e1^ZGRU{zc@Mh_>WTCR>Cf9sur;^R;2z3IP3x+SQfm2F^pMc+j0zV!aw4kfOAP@FBx?rUTzma;#q7_'
 'cglT+sf?C)){}-ChVkwZSBGeeLB#nGzGFw<$-#=hZ>%H?<!CPo2%fB)7>}^}f0n8{KTvlX&l=Ye;jRawV7pm11en|XJF0Ta?y%B*'
 'vZg{srL?Zn!6TIxRtocDR!aA7MJ22f<z=U<%xEFqF09+Vhv82)tJLh56%F`sZ#-~^2NC>%D?ViM%E4!jc+2D!$7fu;&B3O3HDeWj'
 '0e*s|FNXVLyo%t;K5~C-0v6Fu_y}GBhu<HBo7SMa2I-sCjQ|4|<|Hf@J9~!nLA|@g@n7b>yR7!^=^ehVX$}biItI_{`#6n(Q0yMC'
 ';W9)v!#Bvo%P`~$63#CC{~PLtoSLiyZtv|~?9t1M;T{62;Qq2Qs-=z4FaH8OTF?5A3IooTb`>?t0uSqSY8CSq&F5Ba-*kFNZZ*Wh'
 'jr}}yc6ATSElFr{(g~s>k%F%6EHyt&@7fRdEFWDN4Tyy2PNg?_Q_1pLPV7xMm?vpQu<d=ie214+Qo<>&kQ{<&T!zc|HdBhAczuBg'
 'fC;@3G;H^8;4j0w5dSc|#rjtvUcvvVKsdNQx*|~52nrujsY-{aZG@iy!H63Il}JztfVw@nstPuIMUC4U+3JV}Mi_X#p}`e51uKEQ'
 'x6D%OEA`+@h-#t#J|y+P>^-l4>W2R*kyU7B>L7I1!6&mGSX^1M+{S8T7dj0Kl?FT{Ms+W>&{ybpfd<O~rRkvNyr4h(9JFR1n4C@6'
 'G`y#pHzBe(C=}G)OvrG!o8TS%PD!I5wWzGHiyAkIy3??bM%Suknv(l^K?8M8LJ;UFOT}GLp?4C3Bt8Lq&bnsTvhbJv@CNV(I`TaO'
 '^>uUPLq!|02W3xP1~T^M$aUBWm6zT7^4uxr><fF(PTgW&rt#c5XE4)*IQWIRxwY9F>kbej>O0TE+h-vsBNwjk;2Mg44T<v42hFcd'
 'pwq9Qr?6je|Drj>&fPM&j+=<#ub|V+mv{JbhA#osXMBhMUw}y}%GmgOiofD{4$Q1<6Fb7)WplU(`ndlEZ@xIq;Q`?(#U|f7qD{os'
 'XR1Ot|IEnNLX6)Name1`NEr55bwQhndv;F%1j6yXi@*Wx2MX`~I;=}#w3&&1@E_vQESkiMGh|&P<`g8^S2XFkQ_mR7FelEhgBf%h'
 'dyV8hBtpe&S9_LsZ26ZE_yGPRk~$}HU*^T|nJh^1RK5i97KY~}Ifxk>@f@56?d`Mkie7OF;R&8n3|;+7<G+cMv-2#a0q;=d2RD0`'
 '^<@ts52E40d-!AT!H_`YjfV&HcszVm;q5CBV+1kIK|~S+00rylVJOn5XF{OKp3~ED)sBd2?TFPT0pSOTil=9B$~LQ2CMJ7&5e^2!'
 'sv=TqLpl>wtp}x{&xg@^9WSTW1xzPAxX2$Qhz;QyhksxbJ^b^%pJvhIG92Iyg1tFU=5d1_3h5fs_2GK8wroSNiuQ7aaX}7cqT1+*'
 'AJjdGXrt(vFnExLMIrky;Zo`7536Ndo_27jB(xeOD(o9jSA@1)@1NhL$s|J2^(*1>tK_UuNwhbpzis(r_YF>i@@F9k1bzgS?EWj{'
 'Wnf{vJ%u{R%^bP?jGfs9-+-<0$|fNQSHB{V4<Q-_zv?AEh!S9_{>nZ8%e;ePzyB`P0&wL$fGk7~b>(&V2RW2I<fh+$M@0*k=dXf?'
 'FNT7>l)WM-LO7-0amH8kI1LBGf02kdSK>gvg{O!EHNf+85^ADVHQ|KF^K)UAHLjvidFW(4i*B(qPEO{V!|Q0ig-I~nXYgmC0JzI%'
 'oRQ}ZaE<{h^pwy-4Gw06nGe`G@!$+3wR)vcq}sZQ5I?_3)F(C4iCk-tajyq}*5NZpc1go9l?cN`YAFF~R$y9y>gJG+2iST6O7%p-'
 'nGu|y!<_6dj9C>?1PSU|0wH5Sc9FdvTrePy<H7M8dZ1kndc6ZalqyjTEXTH>O6p?qtfy(4&tS;H&u{ht{`?G->lSP}O(tLwVFU>H'
 'Cj?dtfp0=$H?TR*!ZY?Ne8qkZf#kyvVnRat%Sy8KwKjAn##BSscDdTIs)pEQ63OM+w%KptZ|rmUnf)C8T!wHTZ&suACRs%D&<w#4'
 'eqSFZS-e211k7EBp<~wrSk0qNUH#)q{ajMT%L&+1JuxXsnk+$BE+;V<G;fMvLbic2HAN8dd8t3J*rnY=h}X8>{H<#KdkqYsRT&y<'
 'b`EQx0TCcHv;H;@U_{H+Quba&Ffhh=INdJRsU?QSklja@@m(68f{<lt48lChR+}`mnhgHyHEnyp`R&`XX&*urkk6J~7(j76!g#4A'
 'G-84=GRdnfHlt&bIKKC>63V>(c8N+Mo`%XoisOpcNKD1Lw(=#UGUg78V}>#yC7onA7Ygn^8M=+>RL(iDT0AU;%n)X*bYmRr_7if_'
 'bPBB05%FQsa+gh~vSF+x6{2vP4DlpXZ<d8dmp67lxt0Bi5~Dv^X6s%FHV>|M7<Q?7y!|85xh>1S<6F@T;#5g=GQs$>XNlp%GxXyN'
 '8#PCM=y%#h69mW>51pdn3{(k0BRo-|@2Zq$58(5h`c@!vqBBV!0&Wpk5%>M^I2?@cvN+moqC3l4?ziouqmCf#Q6W;4e!OJX2*+Vk'
 'RsmZdaBoauu1kP7{GTD9!@B&Bj$Jlhl4W*?q52W_0-eU@Jjt?o+|-Q3@i-@V@Qg=lU=&A+#%#8o&#Cosh?lwXcO#==z470|2>VjB'
 'Jw|xiJQFFRuh7l~JwCohIbJZirhcJAKQUavp(Tw`jH@$GU&i@40HE8=0gNbyTj||X)4byxhy@a1^FxoPVvz(_Y|Lc^lu^@Y10<4+'
 'H__&<v0BdW>Q)<|>W3AK;5^=dq?<M-_<jZkU=|;xt2v<a2;~a$)F!^#CeY?#<4d$juy)!*x0YS8`M-V%MwVGe**T0smG}g=`J&8u'
 'l;S%kR%aRuc*hz~UZiO}Ysh69p^zS3tP%5H!C;OTT)6oV`rnrSd3^E_9YK5VL(XyYIKqf!Pm$Rli{6CDXTc`q6X<$w@?F~E)&vw@'
 'QRjO@4s0Tv#6Pg5-WzLTe^(Ly4Y(_EKyiqn?hpM&jKL?~&%p@xifyRLRn2HR6(L!Pj4(Q!tk!py^aQn@j#W>gUxURk+#H^PKfPcW'
 'aI*I&vc70a40~gXHkR>O2?YoBIFNlxw`0*KRYP<V!O&U&g;}<9v)_Mwuk<*F+bc{D3P!T2IUv(AiKQ-B0Q&ZqMzl+4k`Luouni~;'
 'iH}&}V{iHZM$!pIzk23dKn%|5-nAUWwTT>AcYOl`zbpp6hRH03J}SC-iSR>2)P_a2(VLA5LxWaI<0~DQ28(=ec-;f4fEm~Y<vN~N'
 '6!0r-A-Wybu09QDGSMX)?~L%)tUnEiD4tMFVm7aa_nBQN%4nD`RT%{lPxU3WMJHqU)Fq-r3~%8g6F9nb>*6g2LRnFSo;i6DN7m4b'
 'II<ekfI<y5wDN)(&7LT_8!d|9?#zXr0U|~^^f)0Jm<!nf1juN)t8SHNxN`<di(P|!!qM}V%UnMOFfDgolER+`SfY_Ck${OXG!~<V'
 '`Er?Avr09)s!roGu!&$KNnU*s-C87N1iy<_F9wC9?K}$)xDs{xip&5jNmv=cGMX}aVOPbL>`II#3tDLrTW2MrrggK)9_rLXOop)5'
 '7(?3IThz<JT5)R&87LZ?K~L{#+${THX&sA*_`;UT%;_uP9BU%DR{Un7&kqRU$ts@BsAHEu+%eF{2t5ohE6PLlSax_bP#qqI4=G77'
 'FOq1UAgVO_+FLO6Q74j`WshVys6e=!*m1l8FEviU;$VVCQq}2t!z)jBX*A3jbwRApLJ8?1MY!5#2Igq_O#-*}<T~SWpWDS^pz5EF'
 'RRDv_auphUW6?F5iPj}W^HA8a;$hK6@ydQwW$X4pohgP`Kv2)Z%ld)mM6S&!^j|VNc=Oh3d{Lw+Xih#n|I;46G`quru=r|Nybs<l'
 '*#!MGL_rC+Y;N~4+9I_3IE+G+{J!0v!Ug6E^|#?QJ>xAXFv;tIT;vC122N^!y(UXSy}7d49Ta^T4y-j8WemaF3`C*4Q03NZoBml>'
 'tf&gNSd6W$sdgRV_1fA(1@N+vr0-#vU|UeTY<w%!5?tNM_Jlil3l9(jFNgb7oWRi^Xw7E$XkNOfyE)wt|3uQ&kL6m4Oe@P0pd8ks'
 'zik1I{vt>LPJkC6Jp$(wFrTgisvA(<7X58gdC{<J?)AHq<5#E0uPY(ZxIV2aX0Zr#V&&80Q`uEHQisu4<(23pUWqO`jK(dmL^oi7'
 '5(6;EBHv6Va$K+G*8P1ErV~a83`?#M-`}Iz1Aoy{$|LP?@8(a%y{GPNrD(D^1FxB&3#Np&!lKE3BU@z=a1NPGnPO_vmiPBNG7SpW'
 '1}M1TDLV{<hX*zzkXo7#NZx6j=6de0jkoa<<T|)*<m5veK*Hb&r|Wnkr2UjU^hPuT(Tv%d$wsAeLaiy(y^f@(j{v7pSlDekKTe3v'
 'V35-dmH@V$+D9(%nyj~SfWOCk*HEuNU2(XH_O@^%CI2Rli0Ri7_5oCYe_R-cQ_v<GCF;hvTFI7uU_sG6YrMa;_o2ex);<Cnk)8Ak'
 ';}T$y*#@_33py`5OoNziP$=XL+|@L2O~9?|eUK768$dxL;Ry)t{?rzrCG0Qc$P|^y?1jNIaH>*V)yg3QNzPTR_aV7BXvP+`eNme#'
 '0wfSmd0kh&%ip^QjA>HUWmC#xG^#++x#)wgsvc?f?gyLQ{JCbi`w+4?wNwvPVSW~()a}2Yg@Zyu<DX&wIvvfTrC4&ql#gfuk}FhX'
 'ZtwYpVUbKz<WZDUn%#iRd2ta+2{5=fG&WSx*R}uJIHeru6r*0yEJl;ia>i_A8BivU1HPne>9csbO_nG;fkTtk=CA;jCTGi#Q@C1L'
 ')Yuczf6RQMV9fzHI*ROx6-j{fq1V^){z6YTleSnrTn!#!E?+i8h=6FEw=Xl%0N@)_TV@4#l}s@U!!H!tf+FF2iQ;HEif=(UVH8@q'
 'h#igON@C|q+}`Cxb}PuM&ek%ar9?1~m)p^*y1aX=xo*pZgSe60&=I2Hq1t}O&Z)i3W{-}5cin33R>2xWV?HDkg!&XHErJy5`9Ok`'
 'WQzIuvw3uuHm;*(lAbr{5w6^$8WEA|M$l@kfOt3H&aKhVPZcEKUyLFrlWdMg(+!4-C83M(bFzq+7%GkCjTI181NR3=lE+p@WJl7~'
 'dX*+waviHQL|QwHCb79*F8-&jn%@tw5G|a`OSN_`Z(Z|^ZN}~{Y8G_z|7lC@1q1+gF)W+^lzxF(H&CcookNw^v&tIh{bJy9^-A;h'
 'fWd33gFB*Ph~TX|(igMN!JT@VXEGiOH?nZ(&Jl>MFE;Gx^8yNw$Cw=|(k7q-c<V3=$I9w*T8-(<$0*@h`RJKZ&JIJ%1M{zCE83Eq'
 'N93N8+}1&o+r+d&0}|Gt)~qoP`H?H>>x;~_k(|<Qbp)RaUEU4soM}my`NV~{WJctgT7p1*t;`JqA%#K5b9`GF2aYd5a<_v#c_q|U'
 '&Zv^jWdq`|$GGDbD)<&9ig=B|X(b?nR$leSTCWA%T2WE$o9eOFKfmLsLDzS+zQNk|q~+tZT^+Z)%O6CpsX1gs=L<LiG8YImi9ozj'
 'ZXgS0MZv=4em?}IqgVQC<F{pkL<3y66rwFzo}tFvE@B1-^m#I-l`0@9MT3|%bGKYAz?4pv7}Eq68Y`o-XdM<RMVd6;E`1_KeW$SN'
 'l8P|HBMK;4slpxt=xrnzRrLC7hn<NPHS-A{&zZ1^k+{5EQM85jm{*VwpsC?6vQ;dWHw(;O)39#X0|uZQcCEdeE45OK2-PsjZT2N+'
 '`ul?kOyOpg;CdK3Kxu9%f%O6k1ekmbx+tHs12LlwFj&?rD4HG`tzkRw(c3HR-7iRBCFMKM6?vt<IZt__GDC0xK|@UIA!F9i?+;ME'
 'qjk%Zczu9Ruyl^Vhxnw-C4;r<mdz@co!pH0Yva`l?ZYf?Op^_n4+og$s1}XKQJSQEU@l4tIQsPYbz>I8voUTIyu)?gHI##ynI5WT'
 'M3SNt>i~m5fF8TB+0`Nu6+zJ_5T=EA6b|*Mk5=<idZ}aksAbq^I*1~+s9XaraG~NHn)-bkE+!(+aDkQvxa(ioJw*!NO9SI#C?4qg'
 'Ged9K+rv#++}^h?@CRdJnVUa%#d8;*7ZqRfa6u7)jI&FdT8&u@PWVe#y>Qiw8JiiFOf<<>8y+fm?T$%pV(XT4xxAZ~CqaK_l)ux<'
 'pM;AP^Do~r=!k5Lz2rD6>fU89UA+q0EQ_giQguQ^?p!!tZNZ+P%m*f}<wgdmiIFRpf<n+lgL2W(Tq!^;(7g%=0}*o<e>3LbjH6iE'
 'y?pX^sD+0Y@fpT0MNEsb97PDtWiT}R0N&8-9cXjuio4R(<vxy>Cjwl|p)pmtS%m`#RYgX9Fe2B=3;UyqY}f3G{KBTN{hB?*QWH2V'
 'nQo&wyd4w)|A&^3PKMueSt~L{GBD8L{YzyUg4{*U&HYxi`hX~=$#sH;yb#BjXQ#!H(4_#57si<2{_QfsED5yxRdBwsWMl%Pcf17M'
 '+aQ76n4HIx%f@P^L^=RCEZ9@*^by2RT6bTsZelGV3)cfm#`ESpr7(f{lvWh99X$kx)l?@C8zGdn6@yDgHSE3O*^*se>I(=<Swu7K'
 'umDP>oFCcp0G`#E-q>wgAwN&qW>YF42?)!C1X#4BqKoLBg?}``bXkD{ZT6Z!2ctJ1e>)kyK7IoNZgleE^xenNuOELs{&4zv#5>OD'
 '<u4y!{e5(D{Q9?7@an_p3vZTez2>z_)B!?k-ZokD4*p%izj?G6Pow6rT!F$L&E6l)G4y~R`A{^<ui!<~qpK}F<1M(nR+rz)u%;`t'
 '1K{<*VSM;M{Js`LAqN(GL<)MYX!{Vi|A${0z?ab+u>?TcM_}SWdtXN2%F+{lMD3Fq(d-p$^rdX_Hs8bW>)Gr*a3*@%0!q5Gobbvk'
 '=t2%3O+W}{%^qfjDP?4{X6~|$C}#^m!<?1t=ZGN3s@W@itfutXN6L!I9WGf)-IhTr(E<&EFe<-IC*aKk?t}=D*=0wP&GURRnwG=H'
 'hmR=p4=@=KB;{njB{_oby=E|gNSK0we%O@Dei-)-F-=QE!29_3aB&H?h}^Rvm%8FxaBN4bOS)5B5Z#2dWG2|b?$4GX)<0_I>2yWT'
 '8?K}^p~T@0X0FL3L4Y7(tv7%<>#1Dy>BZ;IO=eCZyftB+9Dn+FayokX_4N4jNSuQp>R_u(W}_XZ=MlW1XNTwU?KC-q5s;^z%o?N7'
 'GFrr=Q5ZHyBV>=!sM(|S0!&YfHfPrZK2&==)Fb;j7a_#vVN+xmUTJB1govMdKmGCTC&6*)x1V|gxErr-@#@=8&bOb~x1Tuut-S`i'
 '{t5I9RSaCtxX)ZSVB7_+>~tA#`OE{Cx9hX6$2#C_w0-#3Wv++UEyja@LA3y5U7*XMh70B3c^CAu2fu9q*6u(#c-3w**Kt`8K#>kq'
 'Ye8E8-*H&01wYVui{TO+)D1AO04+mP(2#>S00ewr*YC2H#{!r64hx(BnufM{hjjzi0TaXvaP|Nc{DWS#+Tc=km=FJ;1JJMwS02K`'
 'YEGL4*g*gYW9b4+=ta;*9CUFZ(CM<Eg`L6WFy4Z`;268`0!HSxSqJQX4z-{N)N|os3k(qt(Br$T<-l8?VP|06E#?D)0v|>bz_@+5'
 'CD)DlFvL~|T5U5QM$^J>LU{n<dw@egyAQy43tEP5Ln)7nLC+Bz@Do6HpaU*|0>p6y1w-UGL}&pf)5At#<S<a^cgsiA!CN0^17{q%'
 '3Ek^J!2l-|pu)I4m{kuN^??F7&Nqw#Dni$MM1spY0MUoCfOp@=I4L#=ok#FMMSdGP4?_n;x(<Q{bOQbOfV}{U1T91~zK13W6e0x%'
 '2jliy0c*MF<Ty|d8^vdU2N&lZ(TT_gc=)`H2*>%xNkbUeZ5TgLtdG;{fgJ*b3}gX+VFq{$XA+4QkqZq1(fH6f_mK{en867Lq;nu%'
 '4?60>7<~Zl!+Re9`#>E&bl3+X_n<>w2RhQlfnj;LMvg(c=pY=Jb)a3EQ{)?Xgap~f*8r-Ea|1<yXyB3Ga)#g84{-01Z}Kma3DO+!'
 '6<`_Y+T(bKzwm$TCXf`60dNVBtB+L4VJcxJa9A)+fIcJ}c;5jYgAQ|?dqgrk1)6ZXP!RCqBD-^(5WpE=)@|Vg;ypYEgmb`|M-u@9'
 '=ZJHt1C!yph$nat`1Oz?9SnFN*8yCZ7eF8Pklg?Rq6|qMNB}Vnz3@SFxPVO;Ij-G#BCZHa^y`+S9Y8`ha1d)q(I^i9I1UZw1d#-N'
 '0MZ3Y0;vvs<H0|C>oR0r#57z%&w<0;0B0L|4`o4Wxf}=T5xM~=vK0>q)5wZ0Vl|+NKz2ghI5Z`Ib)S*2gld3p>>|)R^aB}<cW4%U'
 'WK^7B=p{~!>v}XH9!eN!BVcV5*nn*S&Vf2PRKVE*B)2%tVGD&j)WqIGivi9#3IdO28Tx_q;L+4_56dBobj8$mS~QI)MLA8X57nVj'
 '9=KwjQG?(skV^qjQ~(T0LXp#S2k@`k67vh(#5)MGP4f(M3a@cSIyA>Fq5;|3N7O-e0OO+w>7Z10pFICA{d#3?k@Fw4y)q4y=HCyV'
 'LIAESW*@;w3UE6_0Wd6|BO+Qf?LkY-dLZT((1ufhQZ^teLGqy4&u2aWM77|~#fc=v2`vMIf=B~UT{-gsqP64GthTUqAEhNtJ5oY`'
 'iUB5}h1w8{7n6>XAmAw8#LR264x<YY4oqwd`qe^d%?16m1mz(u&;XF7i9`aB3IXav7-G=DL9~e)h)_@(LQ{%hXf%Rg0%Q~rgF(BX'
 '77sg0R0I9!av~(1YLNVdG=LV-u)vn#8io;cg9j<eb2>UTL7g`Ato1~y@|0Am&{WIAIPgx|LK%&APk^l2A^JkvLe4^wfHToXnnD^<'
 'gy#8z#5&k>sM|(z@QBoqr~**2h=7(P6lfo1DhU&}9SE}FXf?GIQ4ylxHb4Uh+Qc{5iV*byNRt4Dg0$5FG2Ma*MG9`A#f9^YHXx!H'
 'JK_68Rsjq<=mbPw9?k$!2hk679j6`XiD(Ju7-T9@9~xpnNkkeR(li<r01<odNOnUCg`VLg6OAF~;1AL`l<^S-NFyCZBREuO(^Dd*'
 'O%pE&1bPW_8HuBXW+xIeV7bLRL|dpDfj&IXD`*3;3@j1gK#8^h5okv79okyToBF$w4D!%ALF6MBdyXIpl<RIFrWzEe$AuVbc|!EG'
 'unt;5XgwgGv{7`T<pjFJr71<q5Sqk80})j}8l1p2FiVJDK~y;Nyu)cOJqHc_fCvVa2Tq_bC#g${!$WA$m2Qis(sP8OK@|rx?Vv;w'
 '97n<fnYxRmT*>Hd$%O&YzK8AuiV%VA2QiudK7>icpu!j@d$TP#3b2EAEA|-1<RSMX@8Kx0{Wd;FqJ&$xL}|{^$U%yCa*6H}Qxihb'
 '+(qXA`Ll(If*cJ@v{C}XFp{DVOhfjkkdcTg4=n<mNirAFHv!@1koJHnk{a75GNw83(5y#$5h&WH9-zI;X;OT$tC4%!G&%6&Ba@&#'
 '&?4?b`yE{iH1BbO)tsU23MB8Nuy?UI3M5x50k?J%32A7?qAW1x5$DiDNs8TVqkV=@{bF97HgS^IZkOh_en$T}P9dM?aZY)VOK3uo'
 '3%s`C5f7(C@=3Qt)7SQOF7e6RGdRUZzokPa)PEJnm>7K;$8?D^&`2RI1pQD<L)?H&0%JjA994s4AeR(TTPQKfM93*9p>^&-rgC%M'
 'LDhv?pRlc12XKMb3^I$`@kx#gW)dbBat|^SA`~W=U<>|1D+yUe;~WningF|t^w`EZ@_dtfaH5cdkZOaVm@~;lf`hPW{MS+wh=f8G'
 '8S*jCYYkf!EQKe)5L2}UQ{lw<=(!?`AcLw2Z;1)_ePmr|oVqVK4S5*3jSQO>T8gOqyc(kD2o{v=S7N&#P)<8tBowATSsfi>G9(x5'
 '5yo*ST;XXhB1u2QCUFvCv@0YLqRB_Yl-zv)fxa$kA;<XvxxcfMXyLTFdLKpqoV;(?Pr_E47+3YvCEDpwf5@b9guy}{D@+RZ8+_0o'
 'kX=8DNQJ}z0~P2`lm74xEC!C7V-m3#a4ds8ZV@&EG>y>GcAOuO2@hctJBJZC<WZCYlH>K+Mt()Rx<D%VI%qx>sO1v99Zuc_x&)|y'
 '${2RM8Z19dt~)$BK?cGgCbV)v76HcR(6YvOB&u1o1d$mro`jYu_7H8`Kv<puTFB7*0If#kF!W5&hey~RTF>ntBHX8Tx9d`O{Z4&%'
 '1>!kP0(G|&P?rJM)MMx^#ws!HBx5eJv%)m)w0?+^f3VX!j&=ODFleLjD?6-k+#=oT<vk~v&?QvoJx9yC+xa2NeqzseQ3jDc7ai+h'
 '6c>BY70RF^I;tVPgJuziP(=S**ncvW+#K^Q;O>^wA!mce1A;oBD9n#~5xcz3E_yOu!nwe`BXCMyWt;3FK<E$9?7y_3hv@82G=voO'
 'l!pGf5#c|*A*^&3Efx{fLfE|3Zns_DBA^P|U;x5o$Od3hz+W`+;RgfR_yc4$gkM?_rKg^Fia!`Ik}t6=nm7bT)^CfFEh++?#2N&p'
 'Ma8@Hmt))>-@sf@K~V$;SKA98egg4OzU#`00I6L(&f&RKML=}}1<upka;PmX%ZT1#a9-B;^7>rXcNG?lE^}&0;l`C+7G=2@KXpJ1'
 'Bp{4+bcEpz#z8coEj3h6ysHD<QJ__CT&n03j_FlL4M{cbQR7}d=?a$}HE1p#cj!mMr7OllFMaXStJHCI+7N}+XuN#l6>QJIGXM?5'
 'q`C^IC+>aG5ns%;r--Me^+Zisi*CCDJA$^0B4XybubT5sLiPzWSf!&d!*wbXC{V+ZM8P$pXdC0^j_PQjBND??0tcQxF+lb0n%Pi5'
 'B%MiEYP4KXxX!oqSYocDSk>33&{L%2E94k`=Aw*m%%>>RRh{rPW^)WF5oqE>jioKy?<jn<b)Y#TwlxkkTa;5p_|;nM$hr0fVamBS'
 'IJhIljc>4mPIYb7f~R-2tDx!aa!EiPoyKz7l|}MtYiTvTygOc{JNcxEE+~@Xiab0e;XFZU+#FvWxw}TqKw#D_iOjB$IVBob9q*QS'
 'M#wNlXi5tC61_SKTdLz+(IOXkYH3n5FeYEg22%!m21EM>vU!OMq!jc_f^2JY))!)$ODWd!M2(g<j<zA_JvAIxA;#0Vr>$5)a=esX'
 'B?S;jd2EP2Lq!FeH0df4>ub|k6wDDPq13eNJ=(6KL?KpcTX*XOd|)UzPfm{Bj>214zB6=;tE#&d1!qn>mkcPRi2<WDA%Zt^_N}p4'
 'lvUuGV-fl{SLd#-bA;S$32TN77^>K<f$BW~)iZfbA=}f~q+2spg{tF*NcA-PMWL5-T@C8mg=^X|P@Li_DbgzXS5)#9$w}(<46DjD'
 'OY5XlC}UrvnjIy1wWPux7o$*?8rMxMu32$~6=oI*1RJ<Y@41>eq(oZF97bC;rkhu$)WIbv@sd|Hof?T}Y88x43LDHRL_Nm9Bm`e;'
 'oJ+29i$2t7b;Z<e!;Y05R{WwHnYvN|-+++kQJ-1`pJM<-!08y0q;1kbN7|BHvnSk={&lN*&@IW0wkbEn?01yh@U&T1e9_en9z}xO'
 'U<_SqD+$vsC_T_-hnED8XQ*}G@MPSI$Z6*yM|wGmgq@vMyH~Q>6>*4p;J&IzNNH;Vvs04uzM7pnJgP2xh0W@lqNh_5EN*3}W`o_D'
 '5&}<Lcy-9f`h4X?>*><5f^gTEBLgWImM-~+yv&@wD(ROk@Rl%R95o8l5D!XDkY`}CTe7jZZqg}3%r_OMvS%b@-_#%agye+j>M}_='
 'V4A_vDXAj9%Tx1A-$3EPFSLBOEU9)i<~`P!9H$i2c|p@)^E78p&3LQUI_5h2mZpW*PYW;nHC<SiFfL#EN~-xa#OzhgA*a?FQ`V1D'
 '5@z0RFucy6bqsy#86gM5*zKC)$(R7YBniA76ejUg=KQLREJ4iuY`50oulAO=Ymrt^xW9X}I#=h|lA^k8_$@i3wGACy8ePFHo*o=1'
 '2@$u(s46DcH?ZI-Nm&9Y48l$^XO61K9i2Lqsw-1(?l5T9U*Wn)N82gh?wC8S+gqA6kuOavtX5)~CZXvFl$tWh#OP{iAiP8^lFodC'
 'PTZ;;=j-tk-Zc!rjuFc#{9<FiR1_yLsZPyKP((l^F_{)_PI?kZP@+i9p)5$mc}kPrqDfbb&98CX4177t^m0p{vsd_o((=`P12J(y'
 'VM%oiHQUYYnsQ)^ca%OcXV_G)t`;9HDPlorDr(v>^|>NmUbOe1mw*fH<z~4t=ehpphTd=sz3m&U>lqO>&!nm%qUISg$>bR`F6@**'
 'cqRR%&uPc>YW+uIWSUJ>Sct-S&0z>ZgX?I9tJx|7$etK#TY9R28QL<UaGqv+tNwY$2nvzQt4=%TwKdhqBt83vtg7(_wJ?(bTbmjc'
 'Y~Y5&CTpshX_rDlj2Cju97fx4qZBE%%QC8^&3BHu2Rq=_cCu|iSG@~zp6D9>Y)SH|IAL3c+#SQ>^v#f>2F*1hF@Z_bp6PVe8A=^9'
 'Vr0aW3OVc=fk@B9s$ZR)+($Jbc%?X{ug5uXS4&AmOU3DzWU*PAaAaDrj-gy~2Qkn?A!RLB*5ck1tV~51?Lw;RW=9@UH|z^#c9e`K'
 '#UD;BEJw|@uSJS^X`M_X2o<XL%=$)@z6gsu`Vw2gS#9GnH{(r82bQMV<>uN)-ms?%8!xqvw~Z*cX{;!N*D=7DgUc7sxZyUtm36^Z'
 'DXLOk3^Erpx}~*6VIFpgZREO6U@p{E*TA?DE_JoV8P$)Du_{xu<ixv0aLDMlm+RhQ#=M&KmaZNj$pdMw9#kzk(}5AR^$Z2bHD9b<'
 'T5mOiEQaHPN%^8opet^}7<Gho0Cd*T=%SSy$`uC}9w`~r76AfJx@v8ux5|AjmTzkUoh8$_D`ES3H`>Zr;>w&g%%wbl63DkwIRua3'
 ')yZT3o<=<_sT5p|ib_f$&;^7FWR%o_nhDu8&W&|&Urbt8Y1LLWJfMl?9ILM6n|eCX9V%auoe`GO-5y_K^&qe96}8)ChqchI#Z;P$'
 '1)kBP8bmlHaiD{48CuOP`Rtyia!S>M5`ET$&jK^jR*v-Q6dRQAq75a`id4toR_s1EM}g77zzn}j^IV`HsIBhnop+5OzFTECrwFTy'
 '7QC|k-&LX~?}MvJ+m5Ch+w~)<>53`G+7;KU(ojbYwo_e*+tGq&B)oJ4(Ky;#l3Od-jfqmPwBT&3tSP<9f?Y{3w=}b`NFgyyw%UXo'
 '-_ZGik!n#|NAqfItrA1$W~p1vE-G2>=86b65!!wz6$ZMetz_#ioLR}QrY)5h8H^q|y0-3=Y}UGbo4R3{;W|@B@KW5!FozYxc$y{;'
 'ih%15{p1;eHa~ZHT+J=>Yi&x;&=pQ$jp&Pw`9ub#0Fzg@1Y|72nPKy8dDep(W2UW=4eDmSUBAwvyQ=x3zgr`=6?wQN@+i4+h8S|B'
 'Tkh7Tzv!+jFS5ic#8BkexK%67F@!+3g!VeO&ghh9cFJ6vE3FNxFoJ0ulq$M4=|ygCE*Vm(tBiBKv!!7f9V%y&)V?fMKZ9a2wFHYD'
 '2@E@s)m7S45j!^+zf(I9Ut8`kFzeT(oG7N%bVJ2i)U^mNukGu!q>rjdhOAkMHiq9(b5)|e!k_7u(m6{7xfY^ujfAB79=PT5<sRss'
 'NhxK^7v;N}tEe0WBk!jpO=ef=C$F}QX_316oEk$f7x8vs-7Dd!>Ky70R0WNti81L&w^z7p2>8~6D{2xNZy7w@QX1PYB_vjQ<?9h6'
 'bA8<@<x_Y&z_?W~UX6OJBv<%#kIfl3lXjHU_RJ-L`V<^p8y7CWX~Ea5L%F3$nig%((d?QdC>52#cdp^AQZ$fdd?RYr)_9|wOZotx'
 '`FevnQv@}PR!gJRKvCCNV6L@cI_7-W5p!<t@ltMbm8LuOG~KSDX^}6>om%h9Q5h9Fw7RfXmAiLX&NT)762x6nx)il?jJ)9*F3t_K'
 '8Y#M~bAEYpAMKS|Dt%CQlpSM3F1ECSn&j5A`lyec-Q~TykPzp)<eOTh<fUnL^$3WR6W!X-jaN<2Zq=ng8ZJsn;G2P<!Xl}MRwl%<'
 '$xxU(ru5^6<n~IrNqh%^RA$wy(ccfuYG9fwb%{A9v9*dUUe`4;>Ub`BTBWvkPQ1G_k-B1}>H}{-I`IXP{kjF1S|ppXgKlXnOr4cf'
 'r;)XtDOz4iP}<8<qs_|ZrYS;pi_21jh3o9qkGxfNzP*yZ=Y<2dd$i^%P-(R09vROxb@)y$dO}lPy*0#llX$CUe?VYL%Tg5B)gt4q'
 'n%G#W*Jc|0gRx}aP>p3gxwU1ynylxRX_<SaWLRVLf|@%<4n^DWciIL_nV{bh&HBdrb$i$DnqqnkVfO^RQUb<}>8UBwt}W74X@G(8'
 '(p->e$q0nxjJC0#sMcimN_^wh@=fP)&gks+O}%>N<~4NMshT4^FtZn*AoDwqqm%0~DxU8l<3?DeCYsc$OCFQaE5}$AZWU1@*I1$~'
 '>7G{MV>vR0Dpx5gxl3M2?$ya(uP!&vtGL6RI`>QkJSv%v+G@F9Yh;;gJAQS8g-NOUCPmGMcoa&p04GASZDWF3HSuS)Ev9RfG$Z$c'
 'A>2G|OIvBxFn{S)W039A3QVU+k5GAHdGx$x2rk_mbc}6>wc4U>L?4~f>P$_vzO&oCF15#vl_HhtoTn`sq*Z4cv}>Uid3k}673EeI'
 'MGDN8Hbw--I%!?9!|n-korlW!h9%(E87yvT72d0H1zV*uLEZW)-yH_6Ml4FJ{!Xz2)z_lh+}Lv1Ek&?OVV`2-PDwyY(IL{W9Ajrv'
 'P_?ri702Rcvbna>Q-pqNmAYq0_nO_6rG$i1tXfZc;^yR57DLMU@SdUVtLyNtZ_=KbFm9+br?kYcIV<h5aj&o5dqzQCmnP{~6R(`o'
 'enz*PukPx}jJ!(!r6^D#;(Vh}O#)3&w}rg4tWutwz=&<RW*N8Y9y;YRX7UEF%})z<C&-l)b4?Cf+pukl1Or~PZe#3;EN4l&=B9XF'
 'GPyk?;m<W<MCR_onjOjI<z9U_Mrv_6vrffsxtl9WDV820ZEjMfp2_HPBN@RA!{}?p1xp&+xqM^&$uU>#Ojp1+7e)0&Mb|f%&Uhum'
 'skC#hU9-8aWmu=}y7g|ilo)9&&zeKwyD{OK%W8ox04kt^(gLWc5fpa4%(^M)w{0Y7$zYVHQf_u`anQ_fEuGWby((Q@+s$RNc>;h}'
 'N?YcobjYBZpXG8RkEOC%zQ*?UD#=JCccdCta(7FEk|6FHDTlrhqvoZ}_T{BRxwD4XS<=3-%TTAWlCiC8G-HCy)n&glSYtButmJMf'
 '@i(`7JVPmz-<ro)_%*s&?@uYr>pzO_R$Us4Q`(nqX6)sTN1)5jn!JNt74t_*lrzM<l7CaS-OP<{t@4&8UO~$f#>^iYbJcE8NfmDG'
 'F(-NnGu6EaVS8pKzh*VmD<_#;@SqCStyjZ=+Evh)bk~TB@Lk(7ozf<-@^KC((Q{MFn3Py&ft6{{Hw+KAq7UosxT+G+iOtZ8HT+y@'
 'uC48VXc?31=_<ghvr<~72=o{?VrXXcCqFC2)q-4wz|~V4HS<&^d~sgCrKB##Y9^f2o6Dx1Xhx)XIS-##lUsOs2ZU$z$AD8H&ELIZ'
 'TB0t;*wg41W}vwTw<iBKKk>=*ZylAbVIF<t8kzLD6XTUmdGTtF!l;Y!6#ExVh2zz#sw%vS!ZLNMzdNn8W-q5>X#e)3+jA=gI~r^F'
 '8oA^JJC!Bp+8u@!z;0>hQl$spjxA0#KH!sj;6AknZhh{4R}^#%B>1Kt;XAYhuh|B#asbQOly$It9Z1JqXw(+aOY3`e@{yO5S55oE'
 'GxiymjMjRu!L5*`Uq+x?a)3%R<CiqHZ|oO0V0rpBz;3Z@sB>7$%mdMnoZxQhbeQT+yF#w}RhyRA9t)u6%CDqc^Kz7fmoed#j2*rU'
 'qN(2=fXJT;ksC=Gt;bA)dL8UPq=O&W_fQY9Fk4Jlo_9)zYE&hcXTmD=%PSc_H7<Os$cA_HRjy(qZe6URTZ%b9YH#!Uq}!_5%uRQr'
 'Wc!!0K0C(AGG5u(@(eG_u-16V+4de70I%7`S=aT_@k#ZTxCzYLx%r{uDd-CpZh6~yo3v@W$dSqq3Jc7*Rk8iR^e}T1f(JWtvbkH1'
 'fd$1WEM0v+MJb7@Zc|3d7Bw95k`?Ke%hZ^mnuqC^B$aub952Q6Oe4*$+jwXao*5W!nI>E*C6X7mTU}sSH%Ih+aWzI&X??#G5ozV?'
 'ye(rA;3*zoir@B3R?BZc_4s%Cl$`ji-eiRzZ=R=z>${(NKYgSBUQDuWG;dIWgH1e3=JR;kP$e7N<uu+jB6zS^td@=S`CW?Nb8jr-'
 'Y?Dmr^P@?IUxCIZ<3j=S+j6#9EgG{;L?7{k*9-j8U*nB@fM4}~^KB`go(Cfd9Uh<Sk43Lz`idcb2>jdf8+2!efETfK#pd)$Q1}hs'
 'SXVZCW6kY;8uEiVJpCGG+x0xQ#NYK{d>zfVQ5IVfv+#4y^i5}mFvJHSBl^ItxW32h_2E5!81O~-b-;)HI6ObRPOYy4u!>&T{h7M;'
 '==Kx}b%y=RFx^Y{EPilhA9bMa7xtc=x=>Vpg3<bF_vHsdzl8X`VSdoryP~gpL%no=e$@JgUwF;7n`L8~Ofu_h_?5i~U$8ig*({u~'
 ')9{pChL`M%69RB2MEFj4>auwh&g~pO^XM$K2ssfOvq`v!)|U7fXydvkFoKWXuxs09^j%$cz~QRR4t#M1gv>ng`BT~B^TX*X1MH3M'
 'FjUu*{CZ5+4i<+Za5sS$=^d1bY(`gOs41={P!<X<m!SoyNyRs{TQ-ZRsC?ji_?`RlSbM}>=-FgKo%$tI$MW`nMFdBd`jc9}?EO-}'
 '`UPQ7HK>(;T^eWkioRVdKRYfyn9js^#Ko6pvCKR#!yQMIDi?+yJTn?z%MaAvLw^*XSOuxFU+w<a@P5#|#;-a~;<P#J{~ivAj;<Lz'
 'KWh#J`CVh9Ux)qmY96OpgD#+Wnw%|D^?7VLE%?b^D1x689j!OXBAPdc#Foa3)jZlXhm1O+*M<Tgn!~V+K^!1p(Pqmf5WF@8;t?O('
 '^y>}<FzrL#=Z7y&PCowQb5DI%T=L1qkbT8(arY-H95a&4?{JThudSE(A#H;4lJGs5APK<~%FjX5xYZYzt>&jD!*5PcR<_YRBfP<g'
 'j+;ZXdBPudL0p*KP|s?+vRu}8;lI~(Ax)++J+&f-MVv)0eYTov%KoJ1$t(-u{r)d|5r;qU<3ibeS6;awz|NK-$B%<jVL<<LM|>Cb'
 'fEyo@SFdTZ@vGfXaW8uwI>q;FsfbOp&hp-ghXhLdjx|Y}s}M?(m>8k7jKet_ucmk5J-gaQQ<TP&k)T2P%jlc9K#=$u)BC}tBwzY='
 'v(^0EWX<2;-_K2ZNLbS4+ApI;vJ8PuZ-K%GB&3E+DV-2MX$vD7ok#Q8JXyxnC=&7Aa<xbzDADTdVWUvc&ZS<qiIypSO;-XE67V|I'
 '1s<^Mfy;nb?LuyVNV*0|s0kVenf?6mo#^-KCJil+jSezC3QX{y)Fpm9lrHVQAzTW<;VQ8q!~-F;A|Rw-At`~S-lFu(HgTF-SV0#W'
 'Og#9KU%iJb>?2iN#L+T5NVf~?SD<O2`MtN|S8z%3S#3{D)`kAWKC-;M96Z6pkJO^7!g2I+O|YI?Z|QZJg6gOT|1dF_@GZNEle6<I'
 'o{p%e_(xYV01rrd&@@V+fI5IK@K(3mL06Wy{cgMEl<M)idT*>YZwH*dC)#$p9oKjCdIL$jP3&ZI_z(>jmH{*dkjdJYOJ%eHzkrI|'
 'D8;XYyIVe+1%#Y7nkuu-ZP?^TZj;@~->Xo3xSPln|1e>jg})jMRTu|R0v6tAyt>WpLBS~Mlk?)c@6kMqH_He=KAj4Qa*kh*hG~TR'
 'oAVV2q{%7*n-BP7yiK#ld^L$O{A@JA$8W@w5tsm&Y=x$zwCmQJ6@J_q-pdEdHr>Q%<Za*uH3A%fzoTiCMV8(Fg6z-U)8A3JIV_~X'
 'XdI;pi~%ZQ*>GSXI}z7OD-ZwJ_+8yj0M?F=oMvH+6n@aG2j(rlpuMYdx7EVR0rGQRxs7c7cxBh?bgM15>RQGx(-MIEg0=koS098+'
 '_F8-A7#@XWj0od>Vnp7LgDS?SbxI6xShl*>8OxF>QY+FoP8f;B2h8<#_OOKxwzO7W&<WJ(zYiY+M$|+ga>-U$>VuvOTyBAxEd*<n'
 'Ub5siB-$Ln5Qcq?+exq{x6%}$p}`2tqWmjEk3jUw+Eb<y+8%GL8)<fEwauP^%q4yGR_LjN&EeY@zyA7S4`uyLxvEfJwIZ6>JH%-~'
 '?n*!=z@T78zz2hVW$_4~qj8k?u23Dx?NCbck&v_`aRjw|L5~C+k~6fq78XB3%(3lq0{Gm3z)>0uJQ@jN5rLe#4d3e40rXZ0s>yjg'
 'xdhRq3%~7hyh4|BIwBt@l%5WY$cr5nCICvI?IsRujDmu=EB_OsOjRBcsz$mb3~Qz517CfIw(dhYlD_!D{Q2P|TCPCr*oV`2vYN&K'
 'pkI8*UVOa%#jDfbUi>n8_3^{$$;V$lkGSJHqfZ}y`TF7GukT*KgBIMq`*1q?e0p;H`SbB-@o{_G@b))xji>)}&{(XlljYd~6~oWo'
 'FA^MFgXE}i>6cl227Z4QFH<yyVf<+pBW=YfyTOJ3F;D*yO+c@K8qU=lpv5tpPZkdc19rp@KD~H%@)-;^hoMAs7^lCkaBAr<Uc2xY'
 'uqB8*RMh@$NlYaSp1nP{ldH|DzQMUg(X+Nt)(q%^X@8Z(OQxxiR;S0O!Y{hMW)~MwGmA5jHx^XAH`#2O=GK=cy`Y-1DD6Gpe&+P9'
 'uK~(3K7&_wpFmzutOE|vbHNx*ry#@d{d;^JS?}drLn=$}P4nH}Lg@toTZ4hT04a)&6ms?#Ci-h5f6K@B<Xwr!hTKBo2!POD1mo&i'
 '2=+Jr=i^;rX$b?=uhc{v$y%Tf6naFM3$XH@hi(HZic9qvi?~99O4ahVkn{KiZx(nHm8Ig~?I0Qs#-cmmieMq4p`j+1P;hIqDY^v;'
 'STb~6W~=!$d;?BNtO71TJrQchvE84B<AX>k3g=lEJqyRrLUiO7i|967?vtm7AcT*%tV~RS9w;na2pEnG0_1}dB@m`61Y!p@0}u={'
 'la;Vbo6*%0uIxR!T)^dCw6|w14&Y+Cw|7~d67bTX>cZYfXNQa#g01>YvLXzZViH0ePw##|1W43dDhs_;n7%KgUh2qcybOWctv%}='
 'L?Uw8Qkas(Y(k|%@hjyh=VmZK*?GSQRc)itumoYqpa@RkUmG8`i%)kA5_gT&8buX|#%MB$=kW&H?l**_0j-tH5)g&wAY7tG8m}XG'
 'A2-qrh8%6C2lHgSi8gnQHHfc6K^!C>M$7GDeJ7-Z6jbyCh17B_gM;gJSd}aN0v*@8(6L?{11-Wv_lM+rp;96@CtLzof@_gl7Je9$'
 '{tFlwantN>9fzy&MLZ!FLr4J$K8CI$9>9277s0R#c5lAKdFbWwkA)1t9D<-<pnQx5Ks)ySV&A%8_Atarx~54grY=%5LU;og;!+`w'
 'kO2<l?QRTG<&X->0bH`B*+UfbtO)6Wj$zYKGB3a$xO<mFb+ONf?DCmQ_}>esB#IDyLJ4B12yUXyCc3i-j*dW(1Qf~u>3oU2(x;lB'
 'XJcwCVh%mm27U-8(0R0uaauTjH`~@xktVlb@4YBOxNOQW0{lXQ@Z1rhpS|h9cyFBFS<}7QLA)2+@YEW^^#rc>CwLvh_0)dus8(S9'
 'MypFp;GL=21m;G$i==>o4DgTtNJ{qQcl$3PzQ8J2C|cfGhz=`(7wA2rzlirY#XZ6V379<de7wDRCL>jv)v8QAlBUv~6LU;G?EfRI'
 'HFo<j-E2AyNp&B}xnFIVxYsyHQAr`+0P}(}UW5aJy@yna?G8X<vWsEGDBqh-%Yl=YoeN`nYT@^O1H1PEl;S}M{n`7+9?fk-;WnS%'
 '(tzdd>1G=jvHVq(jRXSZOg+jG0$Y<Xr`JeQD*>~QpiqB|Z{x)}yR#4r3_pO3zF*Esz`GZ=$xWmc?cR9MV?B%|4nuKy!IEJ(q07tR'
 ';b}3Dan9N#64Pud&8Ghf*|%7Pz_(dEwf<N<R-csU{dc=RU#%{;>+p|7Ptp9s#KB@=e=i0Iw`?#NSfbisF=U05vumZ|aJPn9uZMPx'
 'JVdOS($E59R|G-<i*_Le`yiLn!gl!ANJE6F^fg>-;_);b4Dc;R?7)IbhI@3!(U`)>Bi*^f!35)K;?5fmro+K}n8)ld8AVF-0m*Q?'
 'G{sQv5oUy^V5vYQD_!{NBG4iZ1LElGy)3t_<y6!e2^23sEl-Exmm2a}s(({_GWu+!kV9;moW*GtepoHz8nH?xpE>`JNZ6+cP9ZdL'
 's`F^GCN*ii6^?$g5Ea#P(f(wCitoilpsj}`aXxzD(cyMICAMg?=HUhS`m{!nW*hdxw)dOgzAc;fVZ4+sdRaW@e)e><jBhjHY5(;v'
 'N85CBG)|UB@$$N{zRS*6OAn}qyybU5JIF^d%-0m4&EqJId(zUJfeU^x*^cAJS-ip!?wwHRjlg#fXnG3oyYcbEFJHmh{IEhd>0q;3'
 '5dp|W`S^A+-{Sf|*|+3-#M1`cX6N8x#5ba;X|e#rMi{=>?4j!AkNEUx^@0VgihP3G!Y_|fe8<we^iTQmW)!F{UW}T=XYYLs2x}pa'
 'y2vm(Y3sue;G_QM@ySPuG2apW!ox7=i^m}loxK;}<6CyeuGogn(XqddHo$jfe=M+veIO=^0B}q^07rQ{w%`$)+x>e-ga#1UM0*8S'
 '6HBff-`eOQ*1y|eP-u-#_!d2ARpiQMB4YV699Y<ZTw7xI80?sc9}Oa?2mEJUF&#!81GDZOHig&lqX8oj;*Pg$o9Q=#P4DjsFY&|@'
 '9ZYeVUtNx=H@Z9ha=0&xLqqU?l!;6{n3wM1Zcg_@6~WjUU+Je2hAhJ(C=w_UQjNJZu9+Tkx!)0SDTiE`XoG?+D%N86wMdICgP(b%'
 'MGv%yc*Z7<<RlA3dNORDPj?5evAV$Et(Z2tzCuC}UiVpq<WOJ5AP}9P1iU-jE&vv<bI>wCA>Lqr<&?Lnqjm`LcdeEC5{9aA>JFxg'
 'Nbsui4bXvW7lY*J;LJs9)2K9#e9*uSo0@lo1X?`3H4urP-}aogt2g7Bh?z!A)esNY7EsEBxI%%SZjdEp3wM8}g|!B%ra9m+YJggZ'
 'Z`a^4B0Y-|1|EF{NTLwh%JjBft$<d{rKRJNAaU7rLammoLzOvAj<9^77%5z9e9NZ5#@6_bO*fL!MQ@e;SKDXqK0f)JdbqnMIu*VT'
 'L(wXQO3!wZ8qj2^F?>2_1?rKAJZ<jUlxl??F&cz6<fMPe=^hJ;Lf06m+tml1R!|1n3~^xZ<Nzfi=cOKC8=(md1@9NZFBpCXxXWym'
 '&XY-O(Xy40YSJY6V=?G?!~Mm;?+ts`y5q4voNeOxUQ_~;N_5{=?#OqY{q;7!0M~!<$pje~FCu*bZ5W2{ed3!ajpj-xpygiC0J&%`'
 'G-z860*3&jpKMlXDgw;}ZeS(*-2RU?_#||TA!qZgtG!i)Z5w<J0z00B^CZmx;#e(USlAR(2_d%@s=aA^1{e}=F6>HL1h^D-;aKX)'
 'Qy3f_Pi#!Nq4+1j!&`^!&gCRr&1RGlM-XSxBo_1W=EbXHsgp{h2Bn0>2AJ}xuAQM8wR+-~-WC~1TCce@&oPFzraY&m3B?gmE>wL~'
 'd{iIb_O#@(s1IY=4`uQZMyVy>TKq=!$c<QH*BDSbX8Vs|wGZf&-9Vd5*dD-H2hw0l(dt05>(BDnsIC>u8TL=XiKba}?+6*a33F?t'
 '+KAo140ERLlq9xmms;vyZXPUsl`qq3LH*inx`&oz?#&e$npyc!PVh^P)fY;Ld3#n8hTPt_F7O8jcWFz&F($!@N^VUhS5$J%N;5W7'
 'mHe7YzNqAjN}If?4U0D>TMa;pOjhx122_I~DPtYS@X+55!yF|qeF5YIpCDS)pSMhQ2GM?}qyN^NtXm|Dmt4<&&}!c5HSf%tWL~`#'
 'iYBi>1vh5F4VLrG;o>?ME(__>@;+IMRkIVZQpqsI$X7F2UeS-IXK^^dcpMY#7OJ|NI8CNo6wH8AXbpU#<lYqFWt^T24b5Z$^E2Q)'
 '&;}T(4qEh5Uy=u>61=WOh-=sHKD<8ubPRt!oQ__P-n{#AJbLxp%i|Hau%nm1e0=ry(aG`a-(H=*`}kpmF6`(FZ!++%l4y*nu7l<+'
 'xZ-#4?+X5H;Gf7RYYxSfOv5HW@b)&C?xgFau(=8Okq4kw^X&qMUySvO&1T6a%|<e_BixCJ_p%io@+d)PJ<0Aubozy+8KvlDXCp*G'
 '8n#K}kEC&)1BQEBc4tH>3pl#=5ttP)Dt^>zVx(|_(4i4rpa~Jt5^}m-qo<pq1`&M%uN@rc<>d&d2)*1*EPV42=0wanz|RQ<RH72d'
 'GIAWk4CK@x5-bUBI$5m&eIoHoBvItyha-uxBhi4i_TTvMQ43e(5r`u0fch>5-+P?Q0e2WJ18W0d9X2VHlq{jnU9a%RLvYWP!;hI0'
 '))Yf$O(<?AP;8=`ut=ZiQz?u&P<e5GxVW4q8%s=LDyA*I1vNEVUDBQ1r_x7F6}>6Ob&;+x<a4tD<7hO#%Rnzdi`eBNJ>y46oKi9v'
 'u?>Uw8laQoPajWCM=!sg9)BKv{`rL)w3>|KeGw+_h{(xddLF?GdUkjo--@W!gXt!Oy!0+Tj5cT2U`J5?W?Ve7pL4O$+&naLMbw<@'
 '`6B-~U(I7+kL^ax^Z9l@7a=J@Cuuxcp@J4v(re5%+ceuQP=Rk#s@DK-dlQ|<(@pdz@<qxCA%7}}v@6F@rVP{4-UzyBsq`ddTB5pa'
 'l?jV>jq%NU71X4#u_|1XLp!8BBSN_m2u6QZ2-T?G!-9**dLfnJJ-gTAjJgs9=fWX@VzU>vo`s+!R1)WDoS*L&<JBAkfy=2(=7f2='
 'Nv7F36DD1QBB`{I2UC4En0HF(&ya%v$nWe0`x!ciS`Q-z^S;dWcH}sgl=mR~Mwby^VQ#g^gJ6~~uZqRvg`UXZma-o5q=n6ST7=DZ'
 'CO|YAr=gq|iJm;ip-61dvK@5Q{eoe#gK*G(#+UX(IS;vMyffY5RQiUe3goh=_fi;svLlJnkKe^TTq(B?4TRrqwme9bqL=7E@Ngw-'
 'pR$+o^;{t9Mmpp#WPzUniVgj*WNOGB&vT&j9H{KOSL$MJyr|yUrtO0L3jvCx4q={4>J^V_!nj1W^fs&zFwyUeMh5hR)O&!=2qj@;'
 '@ht#G@rG#_^1*6GA?+CoCd{Ko%9W0&O8u11FPX!h$Y80-dpB}Q2fa2Wa|``mmx&|&R`T5b^?oa;+pyM&qIT+BRIm*Db<UWm0JTdF'
 '>|>r5jl78Y6jluZ)bsU?!6WWEA`PrP)KbH``7<11sAv`=Kl=8v<JWJGKjT}vkXVlyI2LENaE6ZG6uBjG6HJWxl;lwlW<&dL`u*7u'
 'j8=RQ3$psG>no(4sBykptbl?*7z4>AfXnSX+T@CCd?%M?Qekb0v`A7VOC+_F&5^-TJR;dgQ^1m62qw+V^K+3iN0C#OIDwG*_l8ir'
 '+~=iOpb5mTPoKLtp&%H05B|Dk&+`#zA{9XBc;P<CAeMt`tu$04zW2c6dwZzo+zuYA)%x?W?rSQPp4<Zn<g<^pOA5H0X+Ako<<cUp'
 'vxs1G=9XiDA^<xf0A@&A`u|rV=WPa51@grjydd`Af=gWSgNKb!Fm`Z4_nvs{iy!>D;B;eVGFyX>^v)4QT8in0#qy2Yp|u@ZP?iXG'
 '6;y%`g>6b+4rT0%ev3TT)jX_=iK@^B#X{}ABqH+0#WgD#Uc%}k8!1{6wE?1QY^&-frU#O25pGzUTiX{MpT-$nhz``H+pgx7d|RqV'
 'i$E)}krMk$HXK~+9+i|<SU40IP)RVW`CYneH_KleZ_xM_7*{46iRx5Ycv6^Q?*2B5gh>rv1DLr$g~e{|DX#Qpq#upE+&ntx+0Vj2'
 '4+BW!UJnz9F8#KgCzmnl-Rx%7m~1m#Jx(Smqi2(7v%z#pdPYf;%T*)VW~&A69&CL2{F*jIVowrw5rV@CSN~+L@$8|1pW?@wpr7_i'
 'ur>m_d`fIj2MTq{Q8Ef~6@jrCn~BiaiR*>cn3S-x^JdnEch!dS2ovsi_d-2H<~|rAgC<E}IYNqYG13FB<*27XA(1Adx~<Z%{j!9E'
 'f<ASMQUB^Xt5H4lSD;5UB(XAe*wisiiJbFf!D9QQqwTq-WfoiP2xL6)T2F$33@r9B(sEvDPo3hYQOO_;3tP1s`!P18lF0<F-g-pg'
 'pzH?2Qo89>EOwF9MhiFJ5;FqleFetW2>tAkJB;39ST7BEn}K15`vym345wk200;&xqFPT5@QI4UDv%Mn>?0v<N^vjA)uXEs@wMxX'
 '3Zlsy6^|a-3}bGAkzT<=8)4pj{Ox4)`uNT9tJBfv<5wR)ydM4f@z>)Ir=LeJ;QI9Bx8u<-FHTS2y*jRLfuTK#aubY<1gyX%S*3^Z'
 '@;ce9mV@TUPsbl#{_^7U=)-Tnj!u6*Iezi_b8{Frd9!a6`}I?`#J_3x%h_c5g!CE=R$*=p%aTRR&f{o(mA^BxLU)Bgc0^35VYx#~'
 '?dg<71v=U5B7b-b)FUP_zGcZR6B)!vZ9qR19l)bj@G}JXL%(z(uH;|!lmE)KtD76lQ6+l7oWmRYFiJ%Z+%mJZ<gc5XLrjmed$=Pj'
 'S#Bxu>#SIMqjk`mo8DOnn6=JCil*>{a4Ut}kC({jM@MJ2kuI35Egad6jqP2lhBt>Ydm09=XV$@WAzU!otcYu7lXEQnlD6uy$qJ85'
 'Vd%WlaN~J$mW=0d;c;e#q2n-_44B%?4O((5IYOi@zk{ro?Zfk7Uv0}P(*Cg`m9&{BmmYTH`ioLULjPr+zt@vsF)4Z&-iW+EOFnG;'
 'x5mpuxz8?*LBcwulk^04&^N`s)*(tfhOz|kK%^&Ia$}>tC*dEWGlPOS<o2M)5U0hT;U1<j-=Qf;3wIKUhw*KO&TF=hld9)#LGhdO'
 'coSnX{~QC+XNS-XXpQvTdSM@;PfTqIJ@cH$2i&*u5DWm1Oa=z~ftWh5KMu!9Ce#D?2YM^2AHzN|<{|z~W_K3;A|z-p0k>+{Cs6T}'
 'i1p??na9)!8F}*6UqU1inia5aSP~Wx*Q>RF*gpda8(Mk4{`S9QWn1r|#xhvmU>A6f&;AlN4xp8u*2WePgBQ#?z!JES+b`8D@dBN&'
 '(W4=%AVOlRk^avx@1@vt4mWoV(4rY8DU!cEzZ3Xr$aN4*W5gDr^_W7AWN4!9oF(vJy980&CtzZCru5n|mYHJq6>uYN(uk)b`U#>f'
 '!nUGRpg20i+(*T-)N(H1wsgh>9*VKrOyf;xxp*!PlV`nTS!t7cG{)r#2~<4HGP{ox2n6-)8InFcu<0ld+OR(;4yT|ii~twWD3tMs'
 'z!cNeqGgWel^iyyHMv{?!<mB5af>ShgC;_4l7kEVz-_!ZHL6S2J&VRd<QO^7;1ZGB0iKAlc?qq}ZL|T^1!VsQL?rF{PWCBFu<VTa'
 ';4Gg<bKE6sS(?peYla*bmSMJ<u5h2e+S;;Z*KAL=geeKk(Y!x}e0s7KLRps8*Gxsz^h9Qjizgz9JKfGHHNHPzozd?S><zleoDenW'
 'A^xEe13?qA@z8`rS~`-E^~P#^5tgTfO6gP3f5N;1pnRtKKQvEb^;L|9piJWV9M1-#anTdJYN`R!6S{;)67BkVD0nu~R5UUcSfd(P'
 'Qc#f)N_a1iFS%vYc%7Yx_~;NNkYo4bTcn)&?OXkq@Xpx965oo%Dw2UUYEcZ_5RC<`QLUaXOoSv+D{G%mU!0saStX?#yJCy3vnJS7'
 'O--XV38;8Nm+(lo&}8z$5cN$Y7Cdrei#n#Do`Z}w8qek+G{s^grRshNeW%+ZO_eNBn>CXQ@Fy-V+2#D;`51&&lf4E6ycW?}kc5jh'
 'uC?@0o@rSjxJ}<0ft^*_mjfcDr=tC`yU(9P;lFW1#^;dtL*Bn(xGK9%Lt)feFFzn$1?2{1E~Uz27xHtDumhr+TnEt7fzXtyGYIn~'
 '6tXvVLA9DxH(8!FnZ0kcVdNa)gz39S`;+Ui#5=eVLvarhkt#m9w)=)s$_W6>6HPr`D<mj%{Rfz(Vd(TEh5h5>$={nyy{x4Vgp5P1'
 'kb+u|rI*h`uQvwKaVeM@O!H|-?kLcz2<Dr_OM-<)pc)Np8mD$p1{gUaJ3!{NmJf$Wj=HDp1=W_YL!|J@=YYB`Z7(%VByVa;&~6Om'
 'z~>=v$r+VM{q4h>cOTw;{`vSdID4N?e+K5FdU!z2ZF8vOk;K>`FcPRjFpRBSB;hKELMN><g}9`V?-06-??QP9-eu3SihWK8YVVW1'
 'XVJ>!C2ldNl}U~XPNMG%5LU7h!XEAy*8syla{FU0P)t&9?CLkXC>a7Ec&otRtw@4|Q4M;|Fc;8cF6Greo?0NExy7@gQb{zyV(Ssi'
 'Y;HemCjya@2<6l<QWf}z2^~RynN$uYkyNw;mJ*rrh4$0)C6s3m{StVS^LzZ^HHhS8d}GMnhlQ-7NsZZ>!oq869M+u25vX|yR}2v)'
 'G-@z<hF9<)jVDi)*vgd?z;?$o&^&xnvV}}FNm3f;owVGvK!rGIB#ooZ<Xq3e_?+CTbPKVPKTV>u<tojR37EDS9n6V`Fd+#`r~N=b'
 'h-tei&gA?*8~}MJmho?oS5P56CX{a`Dm0dnfJ6$l)+X*(tbQS>QvHl0kr+{X7}OIER1(^Jmr*4o!F>_oTWd!n(1DxwZlmi5Z4qg8'
 'h)50{JtdBfq7$E_(J`W9kuq^6Qq`;&^!N}>3$%-AH>6=-2nN|{H>f-VVLGV&douH#uwHYvks-p?xPPK_)X}3S9MK5Gk2<+dojD=='
 'Fr8~PmaNMlQxZ}3*EZA1M3D3IyWfrDd`7R|y?FcK<LA?NuZn|x9?bdDg$X6J8At!Tj=@=4B+CSQ**H(YPy#_iOG9a#iFk&#yAapL'
 '!M?nWCtGxs3%T`g6(x$lG4#NU=;lKb<VQ{#{%6FDkPT#gjYOPEI4r~j#*r=mKWz8IVLSbZ3+n|PB;YVSX<1(K;?h-@ym-osr+9j{'
 '$fv&yt?0R9|INw|$e`;d9FLKoQuBBaadmk}`P*WcDo$8E%Zx0A%_OY11ei#7m84jS@Q57Pa^L~Ll>!guiNL~zS8*nF5<)pFL1Il`'
 '9=cb7iSIR<?uX)Alk2n+*U)`4z14?fP?yWq%`*H$k6TQnV*t8xB4R$W^D-W?f1igvzW2dGoIz<Yb$7t1gMd4urYp)gqqq@SnRtbI'
 'p+0g%5+X?xvijK~NmKA=K?GdK^M_UX&NxXwUlpj4JP1*Rq`|wTz^`o7el#*oo}E!=SFE}*!P7pMa_E~Zl;z8z<x==smJ)JFM2>4i'
 '*WeR`5A|L-j!4!}){JQ2^Y{j%))djM4_iZtO4K?(j-f7eZ4?xv*8<tHlYa~Um*}-}lc`)!lFU<_Z(>YQO$d0Rtf$n>sR9{J-PmlK'
 '0)^ru36zP9N$70doEiQZC9NL|hl#pjvzm5k{?WH;vKoM_i5(CyR1bc{?NW21C`Yhd9<8Z#2Q6<DwCbE<<TH76gh~`9!R+O4!%&{3'
 '?aHZ5=F<(4cA-7>fVPZLjCEH&cii7tm&`97plknzvi9Jif~-0(y?0wJQsw<|dpmm~<Ju3#(tE{mDKhB&aPe}#R0Q6pXolY#mLfS)'
 'rJ#42NI6W*jSq0DFg&k>E3=y0rF7&A4L8E~O{NLNO0eqxsaQ?Fn5rU7lLu$=P%V{0^r+%Jp&01aR1M->F!4H{Jlo#$Nlh}x*3M>D'
 '2Xk&>`rZa;oOvv^<eXw6G_Ge>kEYAduuF>bN9K0~6`T@uy3$5W%W$ac8_^6`R<d(&xbl<nv~xejj9=+19JGueqC}D+<hqNZhFp27'
 '<N(Sf6p~UcD;USLPjl5w3djJHpW8SWhvv)^!6=1AOdX`<dNj@y#XJkg^eYHh(i1$)X{#oomiPhM0~I?>lpckvso9_$il%0#`bwPS'
 'B9w~&%YNqW?Ri|Da}B=pA4v}k%Go^1z)wW;AJ?Y0%XKul1XfA$4!xZ5b~cMQQdJ&iE9qZa(&*Z6+eb$oT-(U9dE8Vd{2?fynvTr?'
 'mRQ8hiwt_Q?ojKwJc<a1OUGrd*WbT?Q|bIA2SrSXh<BsiSF{ODdal~^qQNS@tU*uAnH@}%VNWy!lgk8pV6a26u|T3x6rh!QvDuoK'
 'KrR&N%}FMi64I$*d44ki?Ssu)ZC>gU%qPLq)8MD*PjU<7!fmbln7W}G3;LU$QSm_RT$Y4_Ehz#48y?RIM9V@B<dM-Tn{--XC5o@>'
 'gqJJ#FUKdJk4LYMe>pxqevSSHHB{2SpuMNLqmWdgSBd*Os^BFO@P#}fGBFtgLDCrm6|T==s1^Z`5sAqQVAs$o5^-+%X`_%cedFny'
 '-+uW;#!~+K=+$qhB5jN|=Dqmkmy?elPe&g<e!#7Uqfeh-)3#G_q)H`d9&N}hQ^6r&qz$BLSo97DHe_lp<S&zQPO^oH7SZO!+L#ay'
 '3(Ocjrj$$Ck+23Ih$sm=P2W{W2q^X+zW(?@nshV|3_WtZD^OdR7s1PluWQ5N*y)F3;(J<Dyhk!Tk4>cs9;b8r<Rh~_sT5{w%|N7!'
 'T^jSaC-xU&I<d$!*7n4*1`nJgKd79Vm4fm*MYV><V$nfZB2h#Od@bj9a*N!uc3&%g)BsfE^iLg@^@9gs|Cb%HrRD@T4i#sMpol4L'
 'K%yf=jQuNgN}Eq+&oUzu&cbt<_ZI_qSZw<vm>_g!(RQAN;`<xM)~Z{UY*;eakNVrQicNoF#~}q?Qf*6NvexznX8GnodUa*KI!M;a'
 'Rt85pL@TSXobxmkaG|bMfAgJ2a^V@3!m|*UW6*klE19GPS66g3g{uu+#c(xO^{~DD@On?}QM|>Ivc!%+JU9`f_4&Is*im8wV{(OO'
 '6p3P4{&blg;CHr)3L89HNCD#@kF<Al9FBVD4)Y@&5cSH0x)vK#)rqpp^#Ay&YuP_}>Kg8(|7Xu#t36%~0E+|G#6?j#!y}p=IA9IR'
 'izC+X;$M5n8g^yJF>BZu{V|VPD?Oom<G3|^f~Tz&0PxSSPy2EzC$4GVL-Wfi`VSq&RyzOwsfV!{r?EYJ^gSL<W5_iu_JnhL9yl`}'
 'aZtA@@>=E+|A}+nvYKPwqO;ml-sH}Ug6OVHV3~Q6$*$Ahj1%_rbFZpLzWv)zd&~YS4|~i0b!WY0KXB9=kmZw)d5iwd$Gk-k9`kl_'
 '@n3z!+r<Um|F!XPlbj_Y#4yS79k^Sxz3B5KvuKgb>7;(l`jrM7p7z4lA$@7{uCa#FV{n!aDTcZor&*G1(fA4nx2)!TL}VURGDCH^'
 '8mOu2$!hl`3(Ke5KXRO!cIMXFy4Gxrq<j|h!tO=#bWep)t>^enprumS_mcnaS!6%$(6{@#<K2o;>SwzZPwNkMQwN!e-SEY6W=}cG'
 'EI-Jsbc$JigxQ}wzwCj-%bt94nV}q_A31%jdemK24?l3&UG(oc>F!6zL-Q#|^w-8K`SB;|O%*%fm~ga=$f5jxkT|7*y409QW56#l'
 'V9a-&&Zevh5o30ZO`9q1ucnv%*vpl9?82=dYQ{<(P`MFzlC3tlpW0!!461T6%iu3_0S@RyJW1;cST^=R!{A{h8|Jgv2Z=EJcOSsk'
 'KMCLVPaHRVTSWJ7**z2ISg@GkDFhpN`W_BL66(WyQK^#RfWOzAxhBAigV*Hsj&t7X&R&BaKK1amze^~E7ao>RLc2FlLc0e|p=!w^'
 '+fG<fy<qF;R{5EB4>2f;I&P)#Vycck>u1wCS5)nY-T7T0(?cze$(Vw?c^0~Yfu;kl-?;jXr{DN+BV=p_uAwLUC`K^F5nw;z_JN){'
 '?vMA?agE->t!Liq{c>E@v&YYr!^%ua8Tkw${Ha6c99JFVpq3cK?o$#!qkrPqI^3Y1V2qG<y<;a2#D^<o&$VxvsV%PJoDo|8P@f?n'
 'K?ZI}q3@#VvS7a6As-(^N@d}(IJxmq)&mjC*A>f3Z_NCIB!AhMOv3zRqezATF7jZ2#}ajQfS>AM@@bSm#cy@n3K%AUg%z7J%TFP?'
 '!h>bZ1Bpy$16nz_DBzWkCc<-$CJb9Ci4-~`$Y?Ukn}q)L0nJhkm5v-_Vox=^&krAD^qI<sP9XgB^ViSsUg4MXemfm~e)sFAUygqt'
 '@xU4R!4DikxZZsPA%#i9<}DhKVu2E-Z-6OE{l=PIfud#W{i|moKs^I%55Hcl>NwAeTF*EXf9^m9Q67rxryB}4`JX(^5d77VfPvpF'
 'T-F~{7@gUAYyae7g<_MuuocDh3F#z0&nQn;RQ9^uTTU#m?YZY(E0;4O6G(dr)F430vo^HD59QH^3tasK9eOvygRj(#;@8hLQ6pZ6'
 'X$G@OWaP|}TU@ygfn4%Ol>8I|@jP&P;tTWKM3SvVIIQ&5hCUvMK_6j2*)%Pp%v#<To}ZX*H`mGaYV&{Lk%?+@e(d1H2RXCm%tRyu'
 'oC$dSfAPVIw6=ctl$8uxz-N`!d4?ZTp39>&#Y+7oQdzjP(N&q|KL;WR+laDxl>RF|z=?VSzs7<UAI-7VmnSetUs;4uDZ4+MTKj~B'
 '3-gpprXY(Cu+pre!#4tPFy5YxM#Mlcb8@k8lq_efXP_H7w|ko?foVM1E-@47c(Yk;tmY@0s>busJLH^6MMUU~m#7z}&HT*8WC>yb'
 'k04ma8~h?9Sm0{wKPDT{lYzUJfR#mM#C3j2DF=BWm2{AlPVu6zKdo*B538>}X;}pLC=5H|G)`#MQE3d&l)RvZcn$Qv`Zm|<wpM;H'
 '6hue{4=1GlIYB~6CntF72xyP(M4U`X!z5ZqT{2Jd9o#eR_@hFKM)c9fWVzmExebQ~8y>?X$8pqDC%QD%GDP|LQ8TBviX5Y?S|P@?'
 '!)0jc6hKwP3_df&445mt+v<Y7(u}?Fc*dQH*YbHMZu>2FI*li-apZgB)}#}8ygiAaNNX0yd=j;0;|X`CvspKYI<r})(-iA7Q$76`'
 '+v|V%!rs5%{U!9`iynpTfMFj1HE0S|FTX>-+k(I#5S4%5)UsH_5qrWdmIv&u4`07KIev9|Oq)g&mxiUIWtB$Cze;a%v3jo`l&anh'
 'nxzjvH;03!df6QA7v*++2->V5a*o1#%rctZHS<q-7vKLL1D53JJWV`D5FdO&Q-QF7Kc}vinov&8Ry<Unp^a||J_@HMV3`X(pvRPx'
 'fDiSw1T7zg3W+QQEH$9aHGSUH<P3M7F;GeR7C>tgmT-P4+Zd3LZ)T8lq$O|nGy@(V<9K#_*er)r{@SnnzF8QmBWvXc&WZ=>>t=MG'
 '?Q^H*Gi55%ESH|8EHy1nO$=J@9;_R-%z}^|E|NMFBj6c}pa`w8l(z?TQ76&Mxp4rJOB~9Op{|N$Q_Rhexx_rAD3|K883dU>i*_|F'
 'PgDg1GQsfPe3i!H``(*m1;RB+FKAyOCUnw48fbRVfvQ4CG~z3?d4(k+D$9?B{gbC()SY_p;O>CRemwe`WM6(}uOyP;IXPWm-=&w7'
 'tWUYoj(n_A_*G)k@_+YsZM|*VQ22enBHP1c$+Y5I($<awI88eQNZO#;fDM{UD2m!Bv1Hehl}pk8-g6--%68H|3<ClvmMC7tbI8NP'
 '?|fVb^s#KH#GvN}q_|bCYP2FPX9I(;8Cw#?>sT#Ysfq-9R{lxcjnXwXNZs{tg61ia7#2^yi{?ppdLi&bR6149ZFsTaRs$2f^zB0s'
 'YxulA_>eEIXk8&^45OSYP1r!)(Y7&h+*1aZjCkR=a$UQ_eg+wDAn@3NI!wOW0KRLXtEE7JoLTvp;1@pPSgmgxzF{`=aN}(o4wRcx'
 'Q!*%%5u2n8M*I+0vCg`VEwBUv%BFyOp+3b1YI>0@aoxzrFJ6LK--@fl!}50pm$9PIFqwvEqW?te*1T-&w@mG$fK=u|IDGly)zs^C'
 '4GtISa(<#CC~ca5mKr0c8Y?hgsnDdV7-~?mD2Si0?|H)>VIj*X==XX<51x$CZL#mE>98Jy^-)co!2pvT(srCpD?I4q{Wf1buit*#'
 '8eo_k{~R3fdv*GKj|y)0`3i3wK+(H>JB6<0&^_RHmkCKo!x_aRi2CJds9@lbtLWnpzdWBYsQgPC-Xe-(_^5nAFf>D-W%79^4Z|7L'
 'M-o{Q<&q2qa{AzLSv(>XWtyYoh5}oax^RqQgyuIdKZ^iWNfg)VrxL8L^J9=|boiiy=4IEThoCCR*dent$E}yWp}Nn^YIA(AB<~Cg'
 'QCF<;jhi)MvIZT}l!6d$8O=aja8g`L;&Fa_hV8xfK#?aMg%DD5fRu~WiIU?H>FM42tg>!FFgGI-_RGb*NU>z~zC_n%LC2$RlmXx6'
 'o<3)kNuGez=x47Agf-Uj{9_Gm!VE|HA7RXBv+6a5v;IekMhq4!qL`P-r*t+0-I^gaBZ#J;C-W3Tt5M4(t-GSUM7<ga{oa;`Lq$>v'
 'Ry1L#W&AM1J;0?zV&+w?sYBFsEKhEV+isspCY6^AYzl>MC)_3pfj*U#P6)XoUk5Jy(8L(;T$~^8{Dt8ib6ixAb{Na0@ORYVrxcyK'
 'i*x7h>kh^^XR8ctqYHeKDIC~`W_!X|V_}+H1`RB3)6vDLp7L%r({3T=vR{aoO>fu+VEIX`GCRa-9VHDjDrj_0kMEY6SS7xGv(;$^'
 'wOU`y!mTxz*?;AF)A^iD{`_$AH$}Qn&P+y|3bQRxzCri7MhDvK_Pg@!>EsW2{{Hlzckj<mCZ`v2zY$pfrVgjCSw66nf8ZJ1ifC?<'
 'PT2AG@67QUoMuO*87s#|1d?%`A@97Rq(fA4F`t313Bznx>_l;#EI=jW|AWNiX>{^4(ep)|E*>-o2mbG)lRZlx4Z#Ks8<5fGe{&7Y'
 'Sol(EzZ`z)zCZBy9HzCV9GZ`Ne(#0fg-RY{SP611w8FkG;IHT7`uq6g1DR%q=u-oTabFszPyrpBL}f70r*MN|1#@c`Ipz>nj7#&V'
 'UOiW|>FoX*G`O=Kv2YmNqK8(cf?OyR*Bw9Z1~ro;OoJJE*`ZR}MtW3rH1ER?<>Av58OV15QwYp)>QL>Yqu?kU;q8$aaU4}np*Nbc'
 'qe{hPl-`KyrgL~%f$;#DilZaE)B*d@elmpbmAwl#Int@h(8TcQ$D#w@5>2o#bu~kicAh6z(yl+9>h*tW8IaTfws}F21J&&<ELKe9'
 '>JoE~W!S-{2s>B2;kr|CsS?#y<0rh;GLcZZ<O`&NYY5d9+6IEYq%+p1o~mOzY#E*b$QRV?dVUo+*D#A0ovT7^uJLA25qx!UQ%73I'
 'RmpNbgDDua&KdQR&MV=-D3m>)=9?YA3hnoc73gkJj4UEp(Q;1D9b%cK6wGlZQs%O~3-IQBIO_DK<5F=d@GZEbvo8;zwEeYQ=}S1G'
 ')LDVOBB~?~8Vsk`ElYkP5+9JA^u`f)AUUwm%5qgGB<64<U1*jcqVWVJ?}^g$k@!Vb;0{Wk-#Q}8>(bffWEM+SJRSBA7B$)i_!{Va'
 'ZzvFI5Z;QL=>ZmtC4!L;%{DvZRRGO{6eCD8wi)4URvUo|0&N8CsGx=6?Nn5*-A&}SvKmrAAJ5iXqcsmyfh1SEBAPvbV<%h9>TT8r'
 '^soQ+?U(PxsZ(+'
)

def sha(b):return hashlib.sha256(b).hexdigest()
def main(dest,extract_only=False):
 raw=zlib.decompress(base64.b85decode(PAYLOAD))
 assert len(raw)==ARCHIVE_BYTES and sha(raw)==ARCHIVE_SHA
 files=json.loads(raw);assert set(files)==set(FILES)
 dest=Path(dest).resolve();dest.mkdir(parents=True,exist_ok=True)
 for name,text in files.items():
  assert Path(name).name==name
  b=text.encode();assert (len(b),sha(b))==FILES[name]
  p=dest/name
  if p.exists() and p.read_bytes()!=b:raise RuntimeError('Refusing to overwrite '+str(p))
  p.write_bytes(b)
 if extract_only:
  print('H5_FULL_RATIO_SOURCE_INPUTS_RECOVERED');return
 # Discovery and reduction use numerical solvers only to propose integer weights.
 for script in ('ratio_locate.py','ratio_reduce.py'):
  subprocess.run([sys.executable,'-B',script],cwd=dest,check=True)
 # These stages accept only complete exact identities, positive minors and tree covers.
 for script in ('ratio_verify.py','ratio_d_next.py','ratio_simplex_next.py'):
  subprocess.run([sys.executable,'-B','-S',script,'.'],cwd=dest,check=True)
 expected={
  'ratio_certificate.json':(399211,'9e535ce9a0622c721a1be80bc6e1a03228b8c83a3337e224b617571fad08ebb4'),
  'ratio_report.json':(279755,'968cf95e7644c9a2279cfcd09136c3e7d6e77eb10f0f587b934328fb651e7445'),
  'ratio_d_reduction.json':(259475,'f3d0ef3bac23283c000148540974da4fee69cb9d15aa82dac67857da52fda61a'),
  'ratio_simplex_reduction.json':(334274,'d1385460bf2568f32a34ac089bc7ed462c677b328dace35e77784ef630643d62')}
 for name,pin in expected.items():
  b=(dest/name).read_bytes();assert (len(b),sha(b))==pin
 discovery=json.loads((dest/'ratio_discovery.json').read_text())
 assert not discovery['todo'] and len(discovery['rows'])==9431 and len(discovery['cells'])==242
 print('H5_FULL_RATIO_FROM_SOURCES_RECONSTRUCTION_PASS')
if __name__=='__main__':
 args=sys.argv[1:];extract='--extract-only' in args;args=[a for a in args if a!='--extract-only']
 if len(args)>1:raise SystemExit('Usage: recover_h5_ratio_from_sources.py [destination] [--extract-only]')
 main(args[0] if args else 'h5_ratio_from_sources',extract)
```
