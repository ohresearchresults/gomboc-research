# minimum-0231

AI research report · 2026-09-25 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# HEPTAGON_TRIANGLE_ALL_RHO_COMPACT_PROJECTIVE_CYLINDER_V1

## 1. New result

**The all-root exclusion now extends over every positive top-size parameter, `0<rho<infinity`, with two independent nonparallel projective directions.** The eight basal parameter intervals are unchanged. In the original H5 coordinates, the new projective domain is

```
|s| <= 1/[25(1+rho)],    |t| <= 1/[25(1+rho)].
```

For every actual uniformly refilled body in this domain, **every nonzero PSD metric fails every complete weak primal rooted escape tree**. In particular, every SPD metric has at least two strict unstable vertices, including metrics outside all covariance caps and configurations with incidental weak contacts. Every complete necessary primal/polar packet is therefore infeasible in the exact capped reciprocal hull.

This is a strict enlargement of the preceding `HEPTAGON_TRIANGLE_FULL_11D_ALL_ROOT_PRIMAL_EXCLUSION_V1`: its entire original `rho in [1/2,7]`, `s,t in [-1/200,1/200]` cylinder is contained, since `(1+7)/200=1/25`. **The claim is not that the fixed original s,t box persists for arbitrarily large rho.** The displayed shrinking width is essential to the stated domain; in the compact coordinates below all eleven parameter intervals are independent.

The decisive new mechanism is a full-dimensional compactification of both ends of the rho-axis, followed by a closed, all-root PSD-stress cover. Neither end is removed by a numerical cutoff. The result also supplies an actual-centred coordinate collar `2^-27` and an **uncentred-vertex, true-refill collar `2^-42`** for the same maximal facet cycles.

The immutable H5 parent remains `minimum-0229`, SHA-256 `325b2943769ef476fd483b07ac9289dcfd2b090aef1847f44a0df8e59eabd187`. Its literal three-arrow identity is still **D28, D43, E86**; it was not a complete U1/S1 witness. Its separately feasible packet and uncapped 233 controls are not contradicted by a complete-tree exclusion. fileciteturn0file2L866-L874 fileciteturn0file2L1163-L1165

The direct completed predecessor is pinned by its verifier SHA-256 `a57134241fed56c8db1c2afbed7656f4a74dc7c2c1de6cd2e3b14c33715c6ec5` and report SHA-256 `011bd02590062b948a4071cb11954fad56068b5983a579bf9dd0f5d3cef71581`. The new verifier is autonomous; it does not import that predecessor's implementation.

## 2. Actual geometry and the complete positive-axis compactification

Keep the closed independent basal intervals:

| Parameter | Interval |
|---|---|
| b | [7/50,4/25] |
| c | [69/100,71/100] |
| p | [79/100,81/100] |
| q | [3/40,17/200] |
| a | [19/100,21/100] |
| d | [39/100,41/100] |
| u | [19/400,21/400] |
| v | [3/80,17/400] |

These retain the original eight variables and labels. fileciteturn0file2L880-L908 Introduce the new independent parameters

```
0 <= lambda <= 1,       -1/25 <= sigma,tau <= 1/25,
r = 1-lambda.

Y0=(r*b,0,0),        Y1=(r*c,0,0),
Y2=(r*(1-p),r*p,0),  Y3=(r*q,r*(1-q),0),
Y4=(0,r*d,0),        Y5=(0,r*a,0),       Y6=(r*u,r*v,0),
Y7=(0,0,1),          Y8=(lambda,0,1),   Y9=(0,lambda,1).

Zi=Yi/(1+sigma*Yi_x+tau*Yi_y).
K=conv(Z0,...,Z9), uniformly filled.
g=the actual volume centroid of K;  Xi=Zi-g.
C=the actual volume covariance of K.
```

For `0<lambda<1`, the unchanged true outward cycles and true edges are

```
FACES=(
 (6,5,4,3,2,1,0), (8,7,0,1), (7,6,0),
 (1,2,8), (9,8,2,3), (9,3,4),
 (4,5,7,9), (6,7,5), (7,8,9)
)
EDGES=01,06,07,12,18,23,28,34,39,45,49,56,57,67,78,79,89.
```

These are the literal H5 incidences, not a projected surrogate or an integration triangulation. fileciteturn0file2L916-L930 The base is z=0 and the top support is `sigma*x+tau*y+z=1`.

### Exact relation to the original unbounded chart

Put

```
lambda=rho/(1+rho),
sigma=(1+rho)*s, tau=(1+rho)*t,
A_rho=diag(1/(1+rho),1/(1+rho),1).
```

If `Z_old` denotes an original H5 vertex after its projectivity, then `Z=A_rho*Z_old`. This is an affine equivalence of the **already refilled actual bodies**. Accordingly

```
g=A_rho*g_old,
C=A_rho*C_old*A_rho^T,
M_compact=A_rho^-T*M_old*A_rho^-1.
```

No old centroid is transported through a projectivity. All positive rho correspond exactly to the open lambda interval; all physical SPD metrics remain covered under this affine change.

### Closed endpoints and geometric fidelity

At lambda=0, labels 7,8,9 coincide at the apex of a genuine heptagonal pyramid: the actual body has `(V,E,F)=(8,14,8)`. At lambda=1, labels 0,...,6 coincide and the actual body is a nondegenerate tetrahedron. They are **not E17 bodies**. The certificate nevertheless includes both endpoints as repeated-label arrays with the same 34 algebraic directed rows. This is what makes the positive-axis conclusion cover every approach to either end, without a missing small- or large-rho interval.

The basal convexity proof checks all 256 basal corners and all 35 oriented edge/other-vertex determinants: 8,960 strictly positive multiaffine coefficients, minimum `171/20000`. For interior lambda, the raw height-z section is

```
(1-z)(1-lambda)*B + z*lambda*Delta,
Delta=conv((0,0),(1,0),(0,1)).
```

Its normal-fan union gives exactly the displayed four triangular side facets and three quadrilateral side facets. Positive-denominator projectivity preserves the lattice. Every denominator lies in `[24/25,26/25]`, because `Yx,Yy>=0` and `Yx+Yy<=1`.

There is no dimension-loss singularity in the compactification. For lambda<=1/2, the genuine tetrahedron with labels 0,1,4,7 has raw volume at least `(53/100)(39/100)/24`. For lambda>=1/2, the tetrahedron 0,7,8,9 has raw volume at least 1/24. The projective Jacobian gives

```
Vol(K) >= 33125/4499456 > 1/144.
```

All image points lie in `x,y>=0`, `x+y<=25/24`, `0<=z<=25/24`; hence

```
diameter(K)^2 <= 625/192 < 4,
|Xi|<2,  |Xj-Xi|<2,  0<C<4I.
```

The moment formulas remain the true positive fan formulas after refilling:

```
V_tet=w,
J_tet=w*(sum zi)/4,
T2_tet=w*((sum zi)(sum zi)^T+sum zi zi^T)/20,
g=J/V, C=T2/V-gg^T.
```

The family stress proof uses the moving actual g. It does not substitute a frozen C or a transported pre-refill centroid. Ten endpoint moment controls independently compare two actual apex fans and the exact pyramid/tetrahedron centroid formulas.

### Corollary: a complete axial projective pencil with transverse width

Fix any original raw top size rho0>0. Apply the full projectivity

```
y -> y/(1+s*y_x+t*y_y+w*y_z),
alpha=1+w>0.
```

The entire domain

```
w>-1,
|s|,|t| <= alpha/[25(alpha+rho0)]
```

is excluded for all SPD metrics after actual uniform refill. Indeed, applying the affine map `diag(1,1,alpha)` gives the preceding chart with `rho=rho0/alpha` and the same s,t. Thus the result covers every positive axial projectivity, together with an explicit independent two-dimensional transverse width. This is not the whole three-parameter positive-projective domain.

## 3. Complete all-root certificate and quantitative gap

Define `Dij(M)=Xi^T M(Xj-Xi)`. A weak true-edge escape obeys

```
|Xj|_M^2-|Xi|_M^2=2*Dij(M)+|Xj-Xi|_M^2>0
```

for SPD M. Under a putative unique strict U, selecting one nonnegative incident arrow at every other vertex therefore gives a rooted true-edge spanning tree, even with incidental weak contacts.

The exact graph census remains:

```
4,879 unrooted true primal spanning trees;
48,790 rooted primal trees: 4,879 for each of all ten roots;
439,110 raw labelled complementary primal/dual root pairs:
4,879 for each of the 10*9 root pairs.
```

The primal count is independently matched by the exact Laplacian cofactor, and every dual complement is checked for all nine dual roots. These are raw labelled selected-tree counts, not canonical orbits. The proof actually excludes any attached polar alternatives, complementary or otherwise, because its primal subsystem is already impossible.

For a stored positive integer weighted arrow support R, set

```
Q_R=-sum_(i,j,w in R) w*sym[Xi*(Xj-Xi)^T],
W_R=sum_(i,j,w in R) w.
```

Then `sum w*Dij(M)=-tr(M Q_R)`. Positive definiteness of Q_R rules out those simultaneous weak arrows for every nonzero PSD M.

The complete new library has **1,252 distinct rows**: 869 three-arrow, 349 four-arrow, 33 five-arrow, and one six-arrow support. All coefficients are integers from 1 through 99. No minimality or optimality of those support sizes is asserted. Exactly 594 weighted rows agree with the previous library and 658 are new; every retained shape application is rechecked on the new actual geometry.

The exact closed cover has:

| Quantity | Value |
|---|---:|
| Initial lambda slabs | 8, endpoints k/8 for k=0,...,8 |
| Binary cover nodes | 108 |
| Closed terminal boxes | 58 |
| Stress/box applications | 3,953 |
| Positive diagonal-dominance guards | 11,859 |
| Bisections in lambda,tau,b,a | 37,6,5,2 |
| Other-coordinate bisections | 0 |

All eleven coordinates vary throughout the proof. In particular, sigma's full interval is retained without subdivision; a zero subdivision count does not mean a fixed coordinate.

Each node certifies supports and removes exactly the rooted alternatives containing them. Both closed children inherit those exclusions and cover all remaining alternatives. Every terminal remainder is empty. Exact relative-volume sums check every initial slab in addition to the recursive two-child coverage. Thus **no root, tree alternative, or closed shape boundary is omitted**.

Each moving matrix is enclosed by a total-degree-two Taylor model in eleven normalized variables, with 78 monomials, a rigorous remainder and 100-bit outward-rounded integer arithmetic. The actual projective denominators, fan volume, first moment, and division J/V all move. Rational centre LDL congruences and rigorous symmetric diagonal dominance prove positivity on whole boxes. Higher-degree product terms, reciprocal-series remainders, and every rounding contribution are bounded; no floating-point number is a proof input.

The certificate supplies the uniform compact-coordinate bound

```
For every rooted primal tree and every compactified shape,
some support R contained in that tree satisfies

(sum w*Dij(M))/W_R < -2^-23*tr(M)

for every nonzero PSD M.
```

The reported exact guard-stream SHA-256 is `dfd648307e65ffdfb8d0baf1fb6830a89072bdfdc9e70fb395be896a3df8b8f4`. The full rational minimum, complete boxes, supports and reconstruction are generated by the embedded verifier; the hash is not used in place of those checks.

### Exact capped-hull implication

At each fixed actual body, genuine normalized atoms use `P=M/tr(CM)` and `Q=M^-1/tr(C^-1 M^-1)`. Their convex combinations retain `Pbar>0` and `tr(C Pbar)=1`. This is the supplied coupled-hull normalization, not independent selection of two alleged physical metrics. fileciteturn0file1L7-L24

Since C<4I, `tr(Pbar)>1/4`. The tree's certified support consequently obeys

```
(sum w*Dij(Pbar))/W_R < -2^-25 = -1/33554432.
```

Thus **no complete packet has an eleven-atom witness, or any other capped-hull witness, anywhere in this domain**. The obstruction is one-sided and remains valid without imposing either cap. This is not an inference from a failed finite atom sample.

## 4. Two explicit stability collars with the actual new centroid

### Actual-centred collar

Let X'i be another body's own-centred labelled vertices, with the same true edge graph, and `max_i |X'i-Xi|<=delta=2^-27` for a compactified source array. For every nonzero PSD M,

```
|D'ij(M)-Dij(M)| <= (6*delta+2*delta^2)*tr(M)
                    < 2^-24*tr(M).
```

The certified weighted mean remains below `-2^-24*tr(M)`. Hence the new actual body also has U>=2 for every SPD M.

### Uncentred input-vertex collar after uniform refilling

A stronger usable input condition is available without requiring a precomputed centroid difference. Let `K'=conv(Z'i)` be a genuine uniformly filled body with the same labelled outward maximal facet cycles, and suppose

```
max_i |Z'i-Zi| <= epsilon=2^-42
```

in the compact coordinate frame. Recompute its own centroid; do not retain g.

Translate the source by its actual g, so its vertices have norm<2. The apex-0 fan has exactly eight tetrahedra. Multilinearity of the determinant, with each edge perturbation at most 2epsilon, gives

```
sum_t |V'_t-V_t|
 <= 8*(4*epsilon+4*epsilon^2+4*epsilon^3/3)
 <= 33*epsilon.
```

Therefore `V'>1/288`. Each source tetrahedral centroid has norm<2 and moves by at most epsilon, so the actual first-moment identity gives

```
|g'-g| <= epsilon + 66*epsilon/V' <= 19009*epsilon,
max_i |(Z'i-g')-(Zi-g)| <= 19010*epsilon < 2^-27.
```

The preceding collar applies. This proves a genuine same-facet-stratum **uncentred-coordinate** exclusion after refilling, including E17 arrays close to the two repeated-label boundary families. It does not permit arbitrary new edges or facet changes.

## 5. Preserved actual nonwinning constructions and a finite-library limit

The six new exact physical controls use

```
theta0=(3/20,7/10,4/5,2/25,1/5,2/5,1/20,1/25),
sigma=1/25, tau=-1/25,
rho in (1/64,1/4,1,8,64,1024), lambda=rho/(1+rho),
u0=(1,2,-1), v0=(7,-4,-1), w0=(1,1,3),
L=2^20,
M=L^2*u0*u0^T+L*v0*v0^T+w0*w0^T, N=M^-1.
```

The three direction vectors are mutually orthogonal, so M is SPD. All six controls are **strict222, physicalweak000, with all 68 primitives nonzero**, giving 408 exact nonzero checks. Their labelled sets are:

| rho | S facets | U vertices | H true edges |
|---|---|---|---|
| 1/64, 1/4 | {0,3} | {3,7} | {18,39} |
| 1 | {4,7} | {3,7} | {18,79} |
| 8 | {7,8} | {7,9} | {79,89} |
| 64, 1024 | {6,8} | {7,9} | {79,89} |

Every true hull, pole, support, volume, centroid, covariance, inverse metric, edge foot and primitive is reconstructed exactly. Two apex fans are compared, and the original-to-compact affine volume/centroid/covariance relations are independently checked. A rational Euclidean realization is obtained with rows `(L*u0,2^10*v0,-w0)` applied to the actual-centred vertices; its Gram matrix is M and its determinant is positive.

These are six exact bodies, not a claim that every intervening parameter has the same census. They attain the sharp conclusion U=2 inside the new family but are **not proper110 candidates or complexity improvements**.

A useful negative diagnostic is preserved. On these same six geometries, the previous finite 842-row PD-stress library leaves respectively

```
(15033,1421,0,0,99,99)
```

rooted primal trees without one of its positive-definite supports. The first uncovered masks at the small and large ends are `4431618632` and `8592368401`; bit i refers to the i-th lexicographically ordered directed true edge. The complete per-root audit regenerates from the source. **These are failures of that old finite PD-certificate list, not feasible trees and not a reciprocal-relaxation obstruction.** The new exact cover closes every one of them.

## 6. Verification status, limits, and continuation

The numerical locator was used only to find integer stresses and select a cover. The rigorous verifier uses Python>=3.11, standard library only, with assertions enabled. Observed execution used CPython 3.13.5. Normal build/check and a fresh reconstruction from the literal recovery capsule both passed, with byte-identical reports and verifier stdout. The optional numerical rediscovery uses NumPy 2.3.5, SciPy 1.17.0 and single-thread OpenBLAS, no random input; it reproduced the complete certificate data byte-for-byte.

These are author executions and a source-only cold reconstruction, not a second-author audit or proof-assistant formalization. All original source dependencies were available; no missing archive object is used to support a new claim.

**Uncovered alternatives in the stated new domain: none.** Outside it, the remaining basal moduli and the rest of the positive-projective domain are not closed. No whole incidence, canonical rooted registry, or full E17 layer is claimed excluded. The accepted global interval remains **34<=C_min<=622**, with attainment separate. fileciteturn0file2L9-L11

A complete capped-hull witness must now be sought outside this enlarged domain and its stated collars. Further rho sampling inside it cannot supply one. The productive continuation is to vary the basal moduli or leave the normalized transverse square, first checking whether any complete actual primal tree cone survives before pursuing nonlinear common-inverse separation.

## 7. Complete durable recovery

The next fence is a complete lossless three-file capsule. It contains the standalone exact verifier with every new row and every closed box, the complete numerical locator, and the exact 842 parent stress rows required by that locator and the finite-library audit. The exact proof itself needs neither the old implementation nor numerical packages.

Save the complete fence as `recover_heptagon_all_rho.py`, UTF-8/LF with its final newline, and run

```
python -B -S recover_heptagon_all_rho.py NEW_DIRECTORY
```

Append `--extract-only` to recover sources without executing. Direct commands after extraction are

```
python -B -S heptagon_all_rho.py build .
python -B -S heptagon_all_rho.py check .
python -B -S heptagon_all_rho.py parent-audit .
OPENBLAS_NUM_THREADS=1 python locate_heptagon_all_rho.py rediscovered_data.json
```

Only the last command needs the pinned numerical packages. Expected exact verifier output is

```
ALL_RHO_CLOSED_COMPACTIFICATION_ALL_ROOT_PASS 4879 48790 439110
EXACT_11D_COMPACT_COVER_PASS 1252 108 58 3953 11859
UNIFORM_COMPACT_MEAN_GAP_EXPONENT 23
ACTUAL_CENTRED_GRAPH_COLLAR_EXPONENT 27
RAW_VERTEX_ACTUAL_REFILL_COLLAR_EXPONENT 42
TRUE_BOUNDARY_PYRAMID_TETRAHEDRON_MOMENTS_PASS 10
ACTUAL_ALL_RHO_COMMON_INVERSE_CONTROLS_PASS 222 222 222 222 222 222 408
HEPTAGON_ALL_RHO_SOURCE_ONLY_PASS 324870 b98ed32fe0b47aab4d2d17774dfe0cbe8e27c160ebe1b4ddc2d1aa70c5861b12
```

The wrapper also verifies the parent-library audit and emits `HEPTAGON_ALL_RHO_COLD_SOURCE_BUILD_CHECK_AND_AUDIT_PASS`. The optional locator emits `ALL_RHO_LOCATOR_EXACT_DATA_REPRODUCED` followed by the certificate-data pin below.

| Object | Bytes | SHA-256 |
|---|---:|---|
| recover_heptagon_all_rho.py | 29112 | cb5f7db96896bf6d299127ed6eb91142ba77bc85b5a5ec801961d5642eb3846c |
| heptagon_all_rho.py | 71461 | 325eb287712ea5d0de8fc1e61550bb53aa857671c46da11454545bccc14b92cb |
| locate_heptagon_all_rho.py | 7106 | 43cd4ab83b2d17af4983466b7ba8f4a29aacb2d6d8db265ddbe3a9bcb919459e |
| parent_stress_rows.json | 20245 | fd185f57c0f49ac3dffe60e8f85ae6048a40dfa35c8a16b1fa83e9d4442fe589 |
| Decoded three-file source map | 99581 | e718971f2cca37c92f4ab4f4f876477c1c80f48b9fc0c99ecdef2bd799576ef5 |
| New embedded certificate data | 47518 | 4a7e1248774f5cde6439f3c3952b029dab07c981916df3ae8fd163fb4e031bd2 |
| heptagon_all_rho.json | 324870 | b98ed32fe0b47aab4d2d17774dfe0cbe8e27c160ebe1b4ddc2d1aa70c5861b12 |
| Exact build/check stdout | 465 | 3b728209d7d431486bb091956421d1cc7e1ed920f80ee92ad9cd4cd83bfdd257 |
| heptagon_parent_pool_audit.json | 1652 | 06950f296e5c580c229c0580e8e23cfe403d28d6771767d5f24fd6f50003b553 |

Supplementary copies: [complete recovery bundle](sandbox:/mnt/data/heptagon_all_rho_recovery.zip), [readable exact verifier](sandbox:/mnt/data/heptagon_all_rho.py), and [complete exact report](sandbox:/mnt/data/heptagon_all_rho.json). None is required by the literal capsule.

### Complete lossless capsule

```python
#!/usr/bin/env python3
"""Complete all-rho heptagon recovery; Python>=3.11 standard library.
python -B -S recover_heptagon_all_rho.py NEW_DIRECTORY [--extract-only]
Default: exact build/check and old-library audit. Numerical rediscovery is optional.
"""
from pathlib import Path
import base64,hashlib,json,lzma,subprocess,sys
assert __debug__ and sys.version_info>=(3,11)
assert len(sys.argv) in (2,3) and (len(sys.argv)==2 or sys.argv[2]=='--extract-only')
MAP_PIN=(99581, 'e718971f2cca37c92f4ab4f4f876477c1c80f48b9fc0c99ecdef2bd799576ef5')
FILE_PINS={'heptagon_all_rho.py': (71461, '325eb287712ea5d0de8fc1e61550bb53aa857671c46da11454545bccc14b92cb'), 'locate_heptagon_all_rho.py': (7106, '43cd4ab83b2d17af4983466b7ba8f4a29aacb2d6d8db265ddbe3a9bcb919459e'), 'parent_stress_rows.json': (20245, 'fd185f57c0f49ac3dffe60e8f85ae6048a40dfa35c8a16b1fa83e9d4442fe589')}
REPORT_PIN=(324870, 'b98ed32fe0b47aab4d2d17774dfe0cbe8e27c160ebe1b4ddc2d1aa70c5861b12')
STDOUT_PIN=(465, '3b728209d7d431486bb091956421d1cc7e1ed920f80ee92ad9cd4cd83bfdd257')
AUDIT_PIN=(1652, '06950f296e5c580c229c0580e8e23cfe403d28d6771767d5f24fd6f50003b553')
DATA=r"""
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;e`BB8eITAh=~T2LKWcLGD%b_nu99e0!raLn%sYHOgxPCmXNm49p0-
o%z55@X7hjD=^_k{>N%M-
`bu2h(cCw@;hj7)PU}#dK#=yd$MCvKq*KWO5pai_4a(A`?n`gT<tIG1?b+*BQD*4bw@mRm((I24B1$7TZinkG)IR>{A&_D3u@tS-
ID|GMc#9ug7HGYAyE)Qa2uR=o=|`t%<D2RW%%l6N`WswfvLwG&yR8RzUB){f4OFJolYbx74Ob~SKR)y!3x0N95Sp1E@H%~UzJdL(
bEe2q#J*^RrQGxIMUd*)zq{mEER#C2G|^wfBES?wf{#pOuD*&k2Ro<F`%6e^#3yb(2J=US2|l4bH5~nv`NJd{AA@;<#GQV|aMvL<
h1z4jaqJvabh>SP+>?Rs$;`6QvN)`57VS#?2kBK~>8OZC&&{)bjicAJa^%mA0`ZNyi*cT#qUV>6Z662lvM4_4#48T97?W$X`Wdm6
-c#gHEF8cyD_r^Zl5h2xcl*_#4!t?t+Bd8Dec4F=RC@XW+}RogQJ2k>9yZ6>4XhEaw}3}{E2a!KD3z}fh8*#Aoj<*wOVD_%f`l6p
0{6(Od$n8aGtik_Fr*hbeZUo8>;s=qj(wHXzG;>P>l+j7rpOT<J1?Xgl|P-
u7^bz4_$LdyeECNDCBubq=(doPM`iw39;W=lsb;QapDmXh_KzGqY-O=@^dTB!)$2wV9kgXV$tA?3Hd_a}g(o;$T%-
sn@e_DuCMkI~c!0009Dj(bW}EL<JwqS3*Pn%p^17QtmlLhkt4ra&uVDZ}@#oWxU*SRy-&P9)Ya#iq%IwFR=at8!t=l)-
NBs6(cgYLOx#F&wf6A1!uSjPw)sXw(T7N%B&mpkh_Y-&Q|FZfy5{i^9{c-F834}IlV3fz8)AY<2l?_^SuZ(6{-
XwuYnvkYx{jm^&s~uIFZ;%o38g9m(Iq`Quy{WvlikjnbXI7F+AyT*|B)VJ&eOd_6#;lIm68<i8kNP8Tz=y`;1pMtLY9DY{80SV?a
Ib4lSmo?NohpgI-
f<Q=4bs5Si#C_siUaq0wn7|eb&ulH8bCrmC56fgFblPUg^7gs<_<Ov1uoF7Q16>Qy`g27z&;zMLNcxB$i+1TN)+<msI_Dyx@fAon
-OHW=o$Gt_gTBv+NE4b111LX8;&oi$!H9*EOXy<OZAU?_>ffM#d|86VAsoaH+*?G-2Qud|CPC4)e;s>(xTPXn!-
hXcV%Wl@WlUmanVU@byE!EVTBBql_<1uM|2l%SW`3-es2=&?q^iCIcyTJwZTg=A9NxX+ODkVjdTIIw)Z-
HE7DY}vGT~2sf+l5U3|Pl(p-
#TbMg{6TZm9C9M^XvWUV3tE+CL~cX@+}#0w!hca(dpeY&>`(DWgFOCZx>6%0A2r!fW>JU0Wg2yXrSi)4I<GndWQK7JohS+~p0k`o
E?Jjgznyw^PHkt{JcTK|oCWjlE1EP|B|l^G%bA-w->V^aC5AX(fGuyDQS#u)6-
ApVt6fq9k0p?K7>(*m|Q>w)YdfqvEBK#{y>#3yc|HnhL4{8ebnIIeHQBIXs|;`6rV`49@Juk@a$FAm<N^w#^SEde>wJd}=w&!vvR
+T;#3eZ9TZAD=^9t_t~44Ey<G3B~)KIE$a}G!<nxkXrsu))=tua~6Me6xmqGE7`@3NpN>%;0=osZWe_9I}*-yetOIo0-
s<F=G#+enp7vXFyahC2}VH5Zt^ITu4-
>ozzh(wL%jO{Liga%=P#Xd1*}uhyxvhS30S7XRt*F`?q7pd3PO9xk*o^+5Cd%Tv3%yMeW$>RP2QIFvL*Q1=lukUM8NAJ2wPoL167
75h??G{EeC4xOH*2`sK+P2F`50y?;GOfbWw=4IWgsnRJmkn5E$x-
nNJ_esG)dK{`Fglz)Bz={sPIrX;KAeAgV8yj8HLjitpy43*;1$LTPFcC@SW^M(%I}vaQ1|j#2@<hZWbUBO`bnpS71m_W31&c1P!p
xb=+s7WI8ho2BN&nz|-<3D3!$A2*>4H~E~xCu180hsE*-koL$<J|XkRD@w5nzR-
j#Y208o^#?IG%xy6YgPMX`yEnV2aMmd=Ov!HDNlk^<*Y7tVQGx-stbN&ey3JuZw!ikQk@1HTRMM=?zv1xV53A5M@>izu5G`IlW$?
$__x)~ZrW7cKhM%nD<oau!sNfCGi1vSdT^&C@49hKi6$Bdq2b>*DU+hMc^#@}<6?U4bch~*yX=xH$JCTcl_fF#UrDt|Yeb&Ro>dl
iy<-
2+&nbJZxRY>Sa%(@VK7c`l==oX1y*MPz<Kl_<rFXcSWs{c`lQaSSIfRP(am+^ZHu^Ge@dcR9>x)sK7o&$S|GGu+>v>vHgwPF6`<b
~JPv;~BiFVoR{(7?5=3<vL5K;StWBCH_5)(JWK|Hu&|nVPmdp)7iFTs@Q<pS`5;yv;pu9pvvINR1$6+f^i8w2Y{K2|hkLr>h-Q-
!tzDX$`_gp5lRFUK*bQRxt6*28vD=bAN$2N$@IVdnn$NJOR3zRfVbY?eVMcp38*CP9QY~!}s1^!Na}C<YWF<<umvq##JLZy87BSY
?NWa`Uj#ZJV6|VyCMHVjh;K8sFPKfn#iTIjgMgbC{4H&4^Cx5>-A<$aveGvkWj2X+oGtLtZ=I2mOHNcKy_sHDjj&#yPDVjN-
%dcxVH~(u%JW3Y@$M%ZMp$E_Ua~~ZqO|H7?A?p6Z^GcoJ&LYINWR3-
%S9=9P<bq%&vbUCF2^f{~}G<cl_mryt@D!v`hETJN|$u(6A&xbok3^8_@qpaBBgw53X@@kV-s-LKu9Z1_|HZ$2@`=<_7xaH%>+=L
`=x9yh}U<VUdN`UP}Gk5)6>aa+2-
KMdO>H2xtbhPPxSeNyXbK&2EF0XtgNa;gDiYBn4oVijrYu3#fEa7Dr=cF9*ePs6swq%Bz7(nru;ba46eb!=8o=S_4~>LA;GfN3Y=
QZey5LGpvIky&{IWuK>B<23=#VeSHP~ViTDvWkFrk%X=|7=Xsqk@jA>rW6@wtcFd>}R9`53ypGLDQ@`Ss0mZq6bh2)jK(iNC=u$=
DZ*G<I7vE8^t<F650I53+uIQ80ey7@mwT`aZ?LGt*VTRL++pufdeuFl@!NpAL>>lYtKSdTnlg)q1+qp7sY6UR*j>5?M6)cKfM9mP
~@<T(2J!1dm<bKWas?f-gOM*@9z5IWdu)bQsL|Qo#GQ5v7#{o4L*kP-
{e(T0|F2#2P1}UJhKNHGGuJWYQ0wHK9s8vbXp}w4+VTuM@K!FI`n91GPrUb7(@uL#56v-
tOaZoLhE3TYVqa=hgnYxh_oaDGyTXIL!OX$v#Hl@|<b8GtEs<-@^(%kE$J8&?X`aN8R@Pd4|d#?=6ZwJyqc}v?R4L^R!&D}5-
<45>>h6W0Sf*0`AP(SyMGiNg+Ig5i}tLhzlY8#ShAqV(+YU90e>aDL}OiL)d5ultD#9+mjTIF%UQK^%7`k)ce6{9VWJzq<V<5=`F
z4r{Sc5<810=$jm_DS_-fn2?|ZWp>FZnE^EyRi5zPouws$|_zm=Pv@m%^qmV8-
yw6({|fih;sK3r%Fkj=y<iR=hYE)7O1?zbxBN^sW)#3YxzyeJKi6|QE)v!k+Cg8N04Lq%4Vb6q<E3LzgJXXCgg0|%h%@)xartboX
opnRXL`a*dQ({2A-
b#dipZ~JolxPt~HX5^{rTQhKLjqac{=!x}bf2ps)GD1Q?!7{Y4)$7pL~%Gg!x$W?8SCjtbEWsmrc6rhS&U2=uWig{S{`7#AGMOAa
uqzIw|Vq(@MGpXu@Eku8~z$)&wkQa5PA1!;yTB2%j9X~KY}agH6F8<CbEuH#$XJ8hmnan_l10$B}rXZ9`sP4$c2uxD8Ji`{hZo2D
83Jwz`fM&mape?IPfaCkr7P>kuikaxR__*QjuhE>IbHB`GUUfjjDYY-&H)yHgDhuP_nd|s2!Nh;5*5H)nk_uf8gO^Da7-
m|JeIl66>{TDW!i{-
)NdBL2tCFK1aBBTjEzhAA{UtJk|i~}$1Q7|}Jlr4cfb>bq?Knw3#b!=>%aM?7w9*uj5i0b0%Le*0Bzz2j4b`hflyiRq}Lh!IN4EN
8R4D5Pb=F@u68oR<?*Udv@ou5i(<97x?ds}Ud1XcbDiYCp#pQM@#3C9NX9fsH11Dv%1+evNzJ~uPDQ;y7&zG^&%pcT>`94kBaeSX
=!N}~u1GK%)vD7vE;xWrVZLwegB7ahDX*ald1|IfxL`J-
96723a{);;k;<|FVcc&~Lke;acnhlP|p$b>ACX>pioq54pE<2GN6EdaxpFKJ|N?%ID7UDNAnhQP8juL!%GXBU+6-
zMR3)7E@EFoxReDA=xt+KB`!6j!Og4E!0HmM#g<N-F;-
+=e6IwsBlZ!IVDbGU1CzwxdA2>8LMa6P{Ht&CJ$^C<zA5(Js_zv*zo}_mA0?I}Lc;&-+3tiu@{e7Nax~=y^n9bt)He-
00Mc&o((g?Jq5{3A-@O`^S}^%(SVIvtR36TRSi4Z6hV<d%NiK15rE1IL$_o`T?dy;7u!-
=+WKf)~WGuog>q1CADkp!{7ttVm2xL^`>Z<m&a$V2-
7f9XYB$~<B`0Nic4OlplR`BLex)`1Uc9XPrUjOsU?+`iM@lg&PR%}zmVcyTZgmG$QqjyBs1woK^w2!2Hg2x-
cMvSEY+=B(3P02lwITF!#t}RRn`x9!s|A<z@!pMTJ+dOA_^ea*7egZfP4sIc$^#k?ztSK<d1TnPB=AkV-A_5>#-
kv5sKuBQq;nO1#|czQsnTv7X0!xtvj(kd6DN34E)<@iEL5pN>^qnQx5sl8DQNPDe;GnDviqV_N)R5cTC5^xAOblaJxY^utBMQ7_@
f)Qknuq`~-rz$2gpF9Cp>w?GHXBvp5GWW-s_Z{I8i>v8J|;rA^Y`HpK$pc4iSFdiO>>YkH>+)7gdwJ#({c!*-
i)df1~F!K4q8vZu`>d?cTQ@$MR5<`OtlDIob00o|oqv`fX9><G8OM3<Yr^EABr0=^Y6uz!N{`*k+NzC+1nQl{KXlNb=@VVnfA)``
goko~3ER2gkh%f)zYti0k5^kYW#R-)Pia<>HSSHcR>@y#{5OfI}{KQ_PHbnuuIb3;?Uo%_riHzeIN%UF=#pFsSmnfhh$1SGn-Civ
|YeCx>z%R^7Vqk%16AI)SZ3eu-T+w%`qzxt#sHdJ{ev$p52<cVARI@^f7Hn{0a<>l$Bz{|-
nsr0bjq=WnoMzXZ6@}HSk4*3k{KA`Sf!1M=R=f(Fh`HS)EdiAe4rqD&<^9xc!l2cCk!&(;;>)1-
r31ujB=FYFG<`}U!y4N8gGUpwYuN7~rP-}1WTuUp92bO}>e9TJyHR{>$=!xYJ{$8qo3X=)mjRrtR9e?@BK-
#eeg)$4BRnVbe1;MZTS*pN{{}7B-
jeT7Kb{9pZiAlSumUWektG9O{T(nH>ya&isE^^APpWbXR?#o5hZ*a3Vi;*vpWrEW<t8qR}`JB*hOtXsmM)8Z+*0yz+`0HqFKsp*i
h2D!GrWhzlp2?+p*QufYmqyl_?wSi;G*ukd`qKQATEKk)o0U%gSw#$8{N96Hy!!q!Pld))7-
7_apBI*glIBPhPW!V!{7aSDprYvAyvrlqcPDq0xcEf!&#KX3ck3JjcQa~6(^aIvP&M9y-Y7C?y>Z+1Ztz!B$K-
Y3R3Uhfe~rk$qbj4IRWqZ~a8S0Dn3Tvl5pI{!b5H;Vb)3g@4+Nr$gOq;|i=Pj^fpaoTo05R6Sr(@;c!+&Qs<WFtZSAFWsDVst^(e
5#@0*1ZqnmDOfyLrN3S7DiLIU-vJ1`1p{yTtn%^DtljT<(YC<RrT`HQ@*>e)(Npv_QP(D?0XJ_VZ_-?cqj-
MIwePCek*;6Yr^q#)^0!Q)HfmSFd@(R7085{;9vHLv!to^jK3&@z0yHX=_eWK23fvR-GNsFeGqpqOe)h=FPG<_rbWB01iB6H!mzc
N9jEm%@<)I`PnBnbG|1Z=5ILy@S)NaiJx!O&=0$elt775}^zJ3qT&;>_sFT`NcPx!c3D{WQ%&Ngu&qLW8x?9E9wmpq55&SQFQ7VD
FKvQGq;5yc0ITfh5(g5#18_8M_#q~TvH~p5J>%Y_QRFsutRE*V^gt;$-NdJZg)mjQ`&1c1EEsL1VGQ-_k;2k{O^o`DpZiJqy>KiK
O@r`91Rw;eD@i$ivwSwds$&=yLCA)IypEXl2niDYD4rW^>|@v9G_~8Kd`~FJ5Mvx1HC0Y0BYqU3c8)jX~;-
+;IRwbPh`G~{9=s%RYoVisDyG4Xjoq*tkipx%j^@+Bz1!?C7>lV>}h>pQFhT{LfuSwUNblRd(H9nraU38@$6he7Hd+o5hx9^$iK9
uj~Zl?v-
L}bS{^0xLHJkhI?t?%gf{vHbp?Quk}~EfTL|;vRsha9JVCHd^jUubW`<mCg;#t{Ol^Y~I(I_1=UJDb*z0XuucrZ{qv_76iScC8J9
=1LG7GiO+}jF3pouQ_b66>e$R-YZ#fOz>ah`|7K|R)j)|a~o_q}W-
mJ0VlP!Dqt)Gzds@MN2Rl!HtoMD0IQ>*tW3oEB=gA?LWl)g}tNFc+H%wl*}fEhak_tiZNrfFx_bo7=V}JU0P#t9f*c;5yP$Z1<it
5Y{Pu2tDb1g|`5mLD#c`iyi5iOU>r3pSe#*FX<dW;%{WvD-kwFdFLekbpx^*e>-
Kq(+|NpXN&q+>Mu*9T*R6b;t_mR#oMoVp>0FE$^*1A3ODJ^ck+^QTr*>SE3dcA?<axtSKM|PY|wZS(su{XzTu72#-
skzszw@L#*lv3Eg;rlu1F0j5J?ALp{No;^oRmBZK+{1K_JBR8kI<)LeFLfpkB-Fld;|WZeuF9bJKR<0+J*^uxD%WE=h%3v>rcPXy
Gkx7(0V9$5B=aYA+IRJoFRCVHidCnUwzSM6X`<C7F3K{X4R)u80p=_jg;n>QEA)>^(I$0K+AXRyy=F&DlAF?oC_T0#~UY-~Sn0)-
F{e7xV+2>-UxHI_xj|-
V%tOi4MzxT!jzh*BSf^yv!=J`{(FITez0P=Fys7NIs4vt1m$U3gf6Qfxpcxo=~*sqm5MYTi%dVOc;|H)K*m<F1L=5zh}R(7>Hei+
inyemd_<6+3G;)!<3Fe%xfvtS!Joie!y^&V(-8Psnc${u!;5x9f7M_6U%MzKd-
AbAMxj6cVRzOoEbir9Y=6UM~+$cJ5y&6b8v@>_dJ$0Xt-imS~~@H!Q~!}fm9M>L%zV~LJRL_%NIC^`=9es5Y1bnCq%$B9G)M`S`V
2PI?c@*u7~HShk8RSiK@`<98)~46GtFKbRw5H=Q7`E@h+4|Cv40c=1Pz-JXxE*8wQt_S@Chk(^R_7Q=&o#dMp=}(Vs#(r+`I;5|%
)qbewI<{+<N8<V#pmi!+@iKR<f>KrL!yvW5YNepQ1j)y+SWU0{JY7niZW2O6mpBHVDTHj&*J5{xXwR$wM7EyeQe*cb_WZV}5PnY~
5%HUgZOOM!wpYg~<&ZTul)zK>N}B2PaY-lw3B&~5XXkdCHS983~ezxiJ=oRWYk=q8GeS45X1_O$=XCybW3yh1%M>nt(N-
ateF60ZhU_s#V2;bUT-H9UzaSXq>pgkfzUI>t9H2yf{B^Ab7t3oA6355-
EnS7~UnOKKSS`gR`7Yu`v)C}ZSt7~FY0JM=zF1E(cc!pqWvm-&=*xppexAQ#nDpVnd9UyoNDce%yCuh`?=jH8=plg*oQ-
8>Q%L0yq9n2F!EGhse*D2*ig`<T~~P^q1kdBJ|M!e52y#1oAk{?1N_{s)r>h3-
jMzOUr*VNJxqQ^#sX$M^rpw%!ddlS9J;UsJ0AlmuTa(7R5Xwmx@Tf8R%ziz#!owETenOA5;%)uDm~3|m5BJvIv~2uG1SK7U)_xqJ
}qKrzi+dSyHOAuHu^7cy%lj1on!1II*2n>L$TXiA$*w6CE9*PtC4-;+t44Th?-
e;@MfPpW_vIcIf#EQE7q9m#F`DO%MBV*NxBS+AoL2y(~0Q#0g~f-
=+KV&y%f_V{a5V;dqa4E#>Z`*M(tiOyuO{}S}$7CRJpEI612@x}oGC~A(auu=x~A0Pe#TCmE#kYVm#G?tWS`TznqhW=Juf|;2A7t
-omaW;GE|5a$`TSGPKss8Yx<BkHf-B~|>GiA9kZy}Ks&tzinJg3=E6@nrd#9;EqgF4rY$h6*o)jeLd^2srQxp#8XB-
{BnLQ$&?VI`}X706|nvkd29S>PGb`Fn+~LN6yVHafC%1bTeqR+#$^fPe-kKg%@eWd*vid}9B|)N{Ok_ACRW!5|tMu}a4=Q(ZLg1x
fh9Pm=0jPfh!;t{}nOcpm}J!W{sgCN9No6qY2(#bXj0imC44I_NLx*+x+kG%Iz~ll*)KYn(qBPV&s#jgBdnlfm<P9(fHzqu>UK+d
>1M+X8i&Rv2eErK{A0Ibdw=iXfH6Lg*_ygy_PWD{7-$0#@n6UG|Oy;!bT|s{BH-U!LpycvAbqjX>Fq-
c=bmY7hoPNqRFCu}7WrdWkrbq5rNC<nH}@sVYubT*!x(Hf3k`w0+8grZvYE$MN)jaKWZOj&Z2fwY!lEIvJD2i=hZ5-
^SZb7PRWoy|!_L6PUQh6va9wJY%3wpZbgS{`@;v8~sbn%|-L8n$K@BDzSUv+%BZ?KyZ!shk@%31I2-
;Ugfh=NbA(FNHe#?+txg2wT(PDJyC|UE<RSfjYno~0d>qZzSx~h13{sXU+ANcPHtvQ_TSg3IkhseH2gB1K6lZFeyY2Y9-
m?`h8lpn&{D=-
r4;)!$#Qrq@B82d)luyyB!CvxWorQ6lICl<WW)%o8Bw)k9>H%fGf;K<8yAhO8JFZ$Bkb%XO>3n>$&5D|I504y(viAzidsd<oXp$E
IancCSU8L+u;KkX8H7@C!i?^O*+f5~I+1WuPSqMvil@B>9T%n|@T;$xL>aIyX)l9@9!Xc6rLi$($$6jKOBym`>kqp9@XeSpx3%I!
^KRFn?2cy&0M19W>0ABazJtO`8@tM;@rBx)L+h<$$lF`pE(iuKORuy^9B9ech)O#CWLn8Y-
c^)n%931E``|4I6%ml2)p7uoy|Jhx>H%_>S^Qpn*HY1-Ye%rDIqxCr4$rGZU`C^?QkyPjj|Dm#4?Odx-qCQ6E0S#5dTof<qt3UIJ
5jxCgz>teoBg&-
ggIjj)Z6+D1{r9$?6x>)B5xu(in4P}WUomjB4lxl_GOXFs&z7VGJAspOm#7pBEiI|)fUxC5xL{(ccjP8So0b8$IHcbaY^LLoxx+X
B&2P<r1`j=@y(jO&-
)PVJ0a2M&xr9&yhOQUyI*F|auT%^_k(HF9p!&o8rSkX9l;nel;GYcds;OMb4CZWOP_&Xr}6lkdB4QAW8+@6nWD|-
jpU2rn81Nl$Jzne&Z8>ws#eGQG0?!}hYKb5z|Df#`I;_BU6`Uw)8V|sZp6q|uduN(!_iRyqK^s+pKqUWn{jb&+U?#l9_YyEqcEX|
q`P>>w3;rL{0)65B9r6K-InmrQ4}Tc3{}0Gi2q9e=2(3AC!a;)L^_!y;SFT-lM0UO%l}}oICobU$JL5uhM>Z?YB3)8R@C$w?-
o)>pL`=u`wgR&b6VOzuNPg=oDQ($T12uaC0f`xxt>4A8<h*$$w`JTsb~EQOCP;c%G%2yP;7%V%%i_|cGL1%*Z5!8_HToMLeQyCd&
P`k2!5t<eQp*5b}8TggrQgT*}Z1D)lvcuKH9z9b`<d(F6dQ@-yrqnD)Uh0In@ZoyC;X(kjhU5bL}c>ON8d-tqKNAK5Gwx)-
^KLpM1}v3?*8iqMGE#-M$uxMMo4M`biRbd=-
e7M90Kg5mY8kuUEo#tTgaSwvy+7s!Gycx0IYW1W%h@qPkT6<J&)btR?iu(=qAUnJuHK@5bWX9nO}dRsEE<<j>$M0u4i3Yw!X;F05
i3ATjG+fMmmkIH2I=Hu%MtCLOvwG)lJjdp$4Wu;(3OFqc^?cC1$^bN2WIM3b{IyqmhlWS{~z5)cGzEV;Q+;QykeQw}pr!U#quJ`W
R;Wq#z}4qJ6+F(XG8Ir-
Y;c!3?UE=|4D1A9yGQgIX+Vcg3t$lGNRb5Y{67J8g$J5yYfqT?#GT$Lqu5pbIz<RgRTA|EdXFN%svM5an<6e?XNh>633J&@N~CRB
LAE`)=}lnjBn*d9^cK5o*-Vq5P19h-j(Gz{GteDUV#rKt7LY8T9+Zf@MJen+t-
Sm0$yU067_dEvs&ESIuq4qc5t;7hAaofM8yln(2L(Q<+4*}=IHqBKu~)=Xcy!WK#&pm3T~Tr37G|Ln)MmN<J)Kc)|ZwZst;#?u<c
EpLo3|LUj{?g_TTa}5#o1?%xpjWIUJ)8C!t+Cs)Nz$RHM7Z7$zRy}G|gFILo$x!q#?hXC#2RL=~#R1Z&;DZBLpx#!?LtnxtyNIj$
v+*LOo|WZpc9Lp@RxjF^$DqTDmbCS%Q|~8_QjC*ZBVCCFxC{ft!Y323KElj|BO41CRo-
t4%U^xKZh9+3jdn3IQ%ogleBkE1UAR^9&UVDeQGU%ci|5SWHXav%P8aT}TkdvhJ|5e{3ODLo<e)fRSg~wS4<qZFNZ5w{^{t@(++(
rY3)`GlHj_$!d!sfBkb9t6Dl<ksXB@Re*9_-3R56KYt#EH}+<uAgkLmA2O2v&Mfj?NJf=!*y#wg0O;H)-
l?vP3UjsIZ^l1x|27H?c&ddgNW2c%FqMJuTOiV87-GBJ2k+m^Uu-e5{^sw2_EHCT{dS=ubc%?Q*XT<f$SzxGq!8c&Ob#tY-N96v-
RC=@6Jy3|w)oprGBjlOow5<>vUKE`8od3m<NuyhT$gZ&@Vr8JTFDv9?>Mxi+Gie2^4eoxIBbc?qQ@l~?HJx{UWEcE-wVLUjrm(*|
GT@#tZu~6<>TSZcZ0Dv?b6^Vdd2vpT;U%xB1O}oG%|FD=U<hecam3osNf2xc{5;09+$3|}UKF%R2@hR!PtbiE%Nx@J3F_0q%8A8M
Pq#0a4VmX{fgdgt72t)oWt%b^aQ+#Ef*AXOQ2!xr25>P=@aaoL;8QEH+t`7Z|i*j~#PaA-;Pb&$wXEg@-a%-
^uTh{1~>Ve;*1MlN{U~Dspei<1>Ax-
>e13;rHJT7z8SXMt<G40Z(n|G!<<s!;$m)>))F*}?+B5qD7zLyTwl%U4a0M6_xsi<=14@cI4z0zTfEu~4H6JINxqHnplR8?zlV)L
@iCMk5zaWT-LT5&zM9bYN2l_iBYA5)Z2>j)@oUl6famrzU+7#d6l=kVzm<%~=rDa+70+P0NQ!f#1F)8nlJ)7PKo1KY~6*+UN_Xpw
HRD*qNIs`4&NvY<1w$sNUmxB|Ul)+pj(*+KU3KiPJlv9ig-
H~0z>cfNZUP?KrYIJihXg8Rftw8?g7F({KTb9fT&zXTh<TKo0QiL2yg6toW}2Lod_O1`~U&RNPY%&gV4YNNDBRB>x8jOtfKO=J;P
bdHBK+@pW@G0w47XDW?*;ZBR;A-y}EY20=-HOJT{<0aL}BH-ABRGzAA{0i3zTSvTVy9!B>QMfFruWm|F#QQr2svj-LEt+r`uk9Mb
e$mSPlY-t*+>!hEL7W|;8Fe~f=s|~u|L_(oVn~Ny5b$ILen*ttG{NMv+>m*F!3V5qo4H!G>V?Uj>UtZ68o(E6-
M5a)2jeYz{Z8A{YdPl=Hcgy-PV8&7gwxOnyXpx-wh9Wt*8PB9z`Vn=PYp9!CXUw=AOU6m?*9Y6izkz&aH3vo;k+_kP`@R2kbF}~m
Wt5QPncVU&Au6AK$*Em!dQPw`XN7ok6Jx=y_5`EAFL1x&>pbBtQpxPCUBUfG`Q_TuxQfJA{wl74<bfaJb$kmmzmh{$UXjihkPD*g
{NE%&nx4w=Va%!>@wQSd0ExFQvJA@Ye>1lHY7k;h4mmC82G6$r~qa*(Bwa_#g0@3tWTPcp47!gY#Qe*aM6D8V-
?L!$@{>Zd*WZCGqLn2nj9=>tsV_xR1HYI50<~v>;q+Hb(KlauXEfJtAo@x+!ZH;q=Y&DB;$}#ih$KU0}6sBatT(E7FmHxB6doXyl
SgE!kf`!j_iOp`AO~w&2>zx<)=+12K`kn=uNsmozK7VeK(o@FVTyIxX_Y5kd*SPVdG+}f43&)gx5ivp#OA+yFt?x9exA=2oSl|<c
<jQDy%^nn<YNeLtAn0@^Qm!ga1bXaTawMv0sd<x)XE2p@ZwDZ-
;dDp!v?aHLZPi%B;PbDaw6JhSKhXT2U9lpzgaItueFQ$(T9SaMRt2p}NoO8|;ere_`v+gtNvaw(tho{GsM-j<Q~#^-L;`b_-
N+S_rZ}F*(M<_4SiDqqRdl6lt5aUQ@`mnkxroN>fx6WZ53>WK<cSzepKy=%XSwZUy<Ig5zRfS2p<2h2a(Xz8N&VQ85QU<@rbA#~S
ooypHOj2wMdYVo&)%hiuV-
K@Izpti>iQEjNLIE<xz#%3Ya=J!XqoxudC!Sqd=VkCqA}0J^oCNMzt7VBUgd6b~;yZM#nsWr_051V)tv|Mv>_0hHH??9ebI<EG((
$eib3|1|SKp9ctnhuVhqLnr`TyVK{4p%km*`tN~M^}p`R7dZ3K#Zs2uNVvsjqPX@SSs`5-
uHF>;h(5INP#B7~$`S}sj_qd=j5oRvXdKUh0$*~c{a{?$dd|NSD3%IPCjhBse+1mRWFVcQBCws<%=UqfU4`s8tnTzqUTa#6+^g8G
Ol<-
n<VJOQ`LLU;Q@*VFE~CDPQ2r`>G4UKcgL}rddLPOsQq8?SE*QKuEF~ClO%y6b@)#KtUQSb})v2UL(XN}aWfpnkfXNIat9d<eK!}<
B<E-6UBjTzg&x0}g56RtR@m#HuEEu})*cDaIGOBH*Q)qy6aK$y4tnDx_yO{iQ%-GWflzK+QH-nmfIuA*kJMeq-
W74zw;!9Q`ds6ip8F+Zhw1K6xDhfH9-
EOr7jSkv*x1GR&L~M^7F$gZd94TM<o^{2Wc@N77$V*1ap9kyVuxJ}up0n=%I_=^txXk7`zMFKvdiF808B5t>@-
H7wqc?HSJ!E{rr0B2)`htmj_6$_`BW@JG04q-
RSFJvVGlNlp!NpB+NQW#qdIs1Ou}10%vxuDRk{|E1A4Z_~PS5<Y5m@gTCr~##eOy*7#~O{uP0HOeLtm1Y)~Q!7IZltRV}a?Pzzjd
&@l<}yJQV2ZP&+g6>Yu^7x|i$~6uEj{+d0Yw@$b9P;}*6$#g21Obl)D-Xon?)Dru$+L{pn@GaBcsD-?<miQaKlD<k%+7A1W-
FuQEsxL|S=rLJUB+0m?W8?|;onUGRXaB+cZAcuSp;?HN<V6s3kc#H_A!emFLc?JX)6=@yKYW*R3Vl`=247X#j{PR%4`pC`<iBtYF
%7iL2vu?-
fh}6Zss2mdp(SHzj%vNIvo0uD9G*1bI;^s+Qa%8Bq7K$o2FLo5Mlg{5t8Qp;@?!VD)tbw%BgTnO_cqT;HHw_tNQ<nfuAtKAfspQK
bClW28ZLL-M4Tn|93l2^YJ}x<DB_iB-|6w82gHYQXGI`-uh#}h_K2-Q#mK|%D37&yz{c-
AacskRz1RZt)H6eAL>E(jt)Ht6Ojm|81p->XmgM|+j2a#p5wg`LjUs*J{P-
46yKfJ0$zBt=Eb3y*5b}Fu7P7jc)U_t*~#lqg1My)p#dr01_CV+=4T<)=)IMImk^)mVzC7igDBevhzdQL!YShdw9FZMbUz(5Pn0!
IIG$2|4K7!LyAxJyV4%sbdj>&#KtCku$NOgH@hQy99jsAmoj5_)aO74$aqXyvCP?louLCqoo%Cm_b5a)cd4NS%^{h7pjU%Zg1Y3W
~Ox=!%aOWZq%wJPdkh>T|*Wr;21QYV#V{;op(-
4lWB%FVha>l3|mjZ5$p@;FoxaGLz9LPIR}s{_W=%CgUsq@7<2qe$1ppzfp9e4eSxI>Q#gzVRE>_+D`8dm*O>+&kbF+{NbsEsE9UN
HTt>*B(z)Xk1>d-k89#j1FPBQ8J?BnG^81GrORBQN2?4sLFFA-
*?=_OWyq{TfW_RpBk!7^J9#Xg#O*K(kcCi*Tyo^j7T}v;#H_N^C8+evAk$$V{bD^~uAs>&UPxcIDi#1f`k>X=MEmFib)7$EqpO6P
W~PeZ@l_03Mvty68yhE;$u+5@R!H+rJG95W1$P%SSp+HpV#hH3Qn92%>8c*`@pcU=*bZ{0-
Xrb{Ns7#IbxRm|?re8Z3JkEzMEMPp0p{mmJ{Lu=3J|itRKby>arjejUen+O?gP5=gCofB`EY$tw7X4ZWYX>+hcpwMV>HRD`GRQLs
BFan&K-
Pp`wD6Ja{|g=z76H?u?ceU0QXWDDfC%%Vha<iJSUxK=q({sNz}bvVNgO{7LZhdLLY#u#>Sy>>4321t{&?64z#)5#Sp#0RrqX6>CU
B2dK%vdGPyLM?;l0iG0JoR-
J($h(r6Z)n=1al$VF0<d6Q&sTYCy0m9@xmgwX>{Pt^wJRXQ{VM~?j~oxHIawSjdA21WzA)pL$}yqZ(YaqGKpWehDsWt4G?*-
tr7wTBMKx=G?%^W<#H)m91cvzD%$bp0};4(%|WCZRY!m)Mh7!I@~XJMEqfD}T_ztBYF;!Zwj&CY-VD!c`B1n%{ux(l^uN&lynr`z
zydmBxd0fXwHBdcyRm8M(SZJoba&s-
MwpZ$oTWg+8cGWJgMp${iJ`$tPl7m8i}x_)SZ~vOn!}2E+{Xi+UVd(K|oQ+%eCFN18eisuA>~+@6C7Yfl!2R8(lK`e@ud$k0R$PX
ae_G!Y3d)>Ca^huRlcACI@t*YF!nJvN$v*bbYNV9ooq3D;5X;iEmeLc4=oL!Bbgma_A0v}FO7#PV&-
WG>Zxg)B%UGkA2D9zbCJt;PNU9#pJ|iM%+^Bm+Gqg(xN^``aUnj^@!ZPLL}Hc<%Kb8lsDlN8~T;PqBUrHBHoL10<+PW)r0>3$y>U
C&`=u4;HL4d)Yjk^-
*6VGQ(P%Q`XFXMl|4B7mjhL!*|xq`8=Ohu*=Kh^R#XdQb(Z*%I*|6^y6VevR`i@_MBY!J%yDaBdf7;q!MhV;^^W{V!+Qxw?Ukp%g
mPRmR+$(-
>8(PFvQ4+=pnssJ}yK}$ivi|I2^J7G#oT1>*|hREQoR+B<_!(na^`#qK0Q&S>JEyw7*%BNgp2_d)WfjoOYiQ&iSn~@ZH-du%NuBY
E4THqXned&RYRtxwnMhjvlM^sK6FmEC4H&7wv`B3K`^%>ESqaKuvt&|M}0wARJw|w_7(unXeBL9oi`Il3Gi3O?S3gpO`jtCkFUPG
Ev65=2xUeyX>TVu&9#JoI{5~t_cK+FB8jSFTygBwdkiILZ6H8UsI3cWp~q3Fwq2~CM%kowL^wPw5uM?(C~_6S=N;9?e;Fcs@L2vM
*~n{&aqR7Pcj!|u%hMtvZdc$>H{SP{$^}P3o$zF)DhXP%b!GoM`JXzkjkZ;mA<pReIXWGh4R-
fsJWew_7Z9q6+H2qh4pZzq7Uf^VYTKy#A(|(n<Rm;0ca;Nh`gx3g~-Tv^VmC}iZ<c_ISX6Ia#82-
IS~pbNXi_PgY!hjPU7bQN7WQCJf^-
Sy8`oM&WlZIy592tY}KmT#mFb#e~W{n#p~TsA=Kb>47ZGMX##d8YE6Ra@Ts+oS~WcFFC(Rf^bWuK0rr<^rVR4}`Du_~In7AUs7TU
)k1QZGX?T~{2QyQFsV^bY8JpQ`=O|=>_iDfHg#=x0rVi-Z5k^|%WVhk%o`A8w;a5MD-
7d_fODH7HZN?Z`1%YqBuk+XC%3?!RA4G7)iGAZhpkLu{4Vi`r7x5sohg7E(Xv5oN#_ce;R|r;U-
JRjOe1ulE>JkMPMZmw@w`H03@n&q!hBu}L_fI{?<P~emTg956C`e^(g3N5(_1o`!rk{=Vb#kpf{xAaOWS=-
r?>1<&tD+VG2JzbO<#Yw`*9EwElmvI_a2hKu;YH3iXcT+8R{^G`ihM;RQST5Y=aO5Asr8VvtW^`l!a0lIbX~qym1T&P&5pNCZ2Ae
X!lmXgiXJ^RXU$#p8JM$1Dq~@-t??Dv?yL+RpWPC2j?lMN3X<)SLjJQKQ-Kn1i>ChW&V;}_GA@(;o|Tc#Pd)n1lre~9{Pw?^+~KB
)&pYezLD{PuqEYLFyh%r}({YZY5X>3L@n?3ZMPp9D9Ov-
H3x!?Q5eU}r4yj=@m;2HD6#EGvr^n^rFJk>bX65C$9?Dbp&Ry;=rq;11i%~(s!(OzIYk*&0PLX_Ky4Pb*{)wI8-
lrp(r#(=xFeC0*FVaLIEVOr3d4lD@<Tck>q{}&yo^mUV_n=Br<PpAp$-
|UA;idL*xt(oTEu=CIL&tD3WTnUAIFmN_+<u5>T!7wTYS_r?wnd8nw@E;>=Y9bgRM+!CJneu+wEpkU(VM1*H#B!3NTYc{fIG}dTC
8yGh2=SXkV6~vb-ruR{Qfq-
;@Nkuql^iLYb;+TUViur<}g@Yy7NVphxZb&zH@eZDbrRwHsVH}sF0FzA{H69Z<}eJ9Es?J_oSKy1LXI%f&Js2m9jMir3LG(3Vhy=
dY%lTJ=oeYS~H<C#bS+{zFn?Fm~t$h@RxMF4lWfpL>|ih!j#diJbb6Qa!^!Hxg;HU-
aM{9X*M8CoV(PtvwM3fJ9*|zZ_*A`XqJI+D~I51TLBj+A&g{4h!bR)IyMJf-di_4@UcQ$8^VU%H68t_>r_yHZTdc<`fZ@J6F6HoQ
P<knWYG`(LeY{^7PJi=#j8f9=3%Itac886vUe{6TC4mLrNR{2D-
H%HmbeGpGT#gF1K>TzT`Gq{JREkJFHUz?+v^mm_O~q#s@3xpw}2Ye9De|{;x&U!4v1g7QI`m&K9)9zXPhY;dp+^2ZT;zL0Ei5raL
v+a9XV=G(ID70bTwh|2@W2sj0U;+*8WJPlvUCuB}xq|)S0aR7wEW7`o0HP{g!%^Xp@B-
BEAk;?O*??*72}A<XR1mkavHpo51ETk0<BV5_>km`KI>jw-Sl&Z0X%6F)cQKXWOi{)MM>u(t<Y%^=4;F09LU5cQ#-*pWK_;#Jk$-
^US~5i2Izlvum@VU?5ateQ;Q+SukrbeV+P<yS`1qsJOx3Cm*)@h7fC)5%JLDX#O^ho)s9dTCR9xL}NWB-szRSTCY-lVkZ)joV@la
PL~`i?}mA9Ov7kJJ=3j4r(4m8H&qCv67xDm3O@Y7>cNd*pYLv+<#`#u0U|w7!aD19{Ap|2(NtA)l4Fx^ENZQKSXQQAW(CkAOB-
X5>)fz7uG%a-
7;&(EO~EdO!Ass{u^*w?C5%BPm6~vbrw;`nQV&NJeLAt$g`#>q>mK5SVtiD*s{RLqN4&uUqt0o_a6;@y%pPDuR{zl)xrIRd8YvYa
T0%QngZg^F0dbOlX*)WiyA9H>5mB@d0f(*;waHwNQ?IkrD=nR#IoJ$O?=2R@8pUyYOWsI&hBV&72mBFX#IgfQq;I0kQ3#MPs8;J)
68fE<e>&%A!1xgzcqH1>V~%Sp>)R~PkZ^U`UNoA(HJ;)PWT>X*(0)YO2765rr<0XJ@F^nRr(eCbG1O`C0Df*#)a_ExyqWY*!V9R#
t9E-QT?yCm;=rg!ggF1xTEDlYU&?#;lU=NC9*bb-
#y5iYjz@!uRre6hAk1u}hxKk$X;0wN+(B&0c0jjG(k(``k`tK6`BLSc&NJf}y5j8#PAwaun;d_gFice^p|j$d#bR3+US4)sOtH^k
>yKhFWD^-BdPHWtDniU;c+-;xO3X&=6gF*yMiT|iTdd-1Wm9FW*%hRM<IgHl%17l*l6uCU4*arWROFL}1>^8=&-
Tu(yo?&w*W1E>F<Cl69ox5V*ww~k^7g;m&VsQ*P--MIb=3%g`K^QM?vYPS=l4I+4iFU;8HEsUOFQ7t!{KT9EtqLLv0~*aES=kMei
x&7ZFyZGo~UGvPfiv8ZkM&fuQk}plU+~!{*$m2`go;aut%C~<Ww+)5}MHKwRMIGoW-
$fvBH!|@B>INyez@a1J4ud2v1~4p*CVApo<9D>p-Be)I)-d4=~2Z$z&l%?DIpLt>im{W9nlevzQFt(svT>XI#@7w-
5Zowx+j{ilYJGt8F)W>*ff78Be-zIlX|SeVSkz!Zp8dl~-ab`}C1cJRy<2<_^%y%}1jA$11b&^VBk*-Bvh)A4|lQ59JvJG{&-
8n{Gx+pi(=f0(jXC{^l21RzQ4P^te0JwHh#6E$hHUm!gpKc@?l`ER+;utOQIEKCBT5Xg5T<O`oRAWcCT1h%sbYSDN>hSQR(|epVX
qY(tosay``(GLkV~$cDT8e`B4#=N(Y2>ub00hZTYI^a|mbLiO4~>Fme)8y0WYi-O?VK;^klTEp#Z)p)PPJl?uOi`6ckKLV-
L%aJ3C2^>2HvD7h~vxcpjmBm4ML9)7gn&M3(V=9E2O43wb3g!EBFl+rmn#qKhiASa?L7X^sq%HLzo!YkY`djFWTAQfs#8@5ce0Ls
tu^)~$TMt>~<;6npsZ)CskKe}qu=_JD%&CGa|Cs0r;}|%VH(Z^T9xK?j!@6!VJOPgTr0yOztDKyUuw0Swo@}h>c0sYTuagdfK+50
M>)d~$TN)%j_F15TC;LtP%Nb8v4ZUE8Cz$%j6xjo&&gCsjY=&_{EeH;g#(!#tjessxPON$zV1DfXh1}OSc|=s)Fev>vvk^1qtpZR
WA0FC!MkxH&)_dyvvCU5o)b=vBHw!oa{)HzOn@znGS12l3JuZ;>TYC}SX-|2VfHAg6#H3Cd8$bT-o-
{>uI819(El6{mXe2xr3&IuEmZlsmYB>#@bMq>UL@oEMOOCgxqo(K?|457GliXv&)x8N}UY;#$WtSl6!@yv`95zLegLZUv%FDdF)&
jC-cDnkva}!_410YB^!;P~LAHH^?g9av8et;J^Zj$6Oto<ssxdG+By*_k3&g4j>S(ZE0DH&GmmDqO&fSa$Uwp^qiLvro?^vp%WJD
*=*bqF^@C3V;yTx~^N+X4pGI_(L*$x!fzBN~#r+qjTJpiOLz%$kA|lCUt3vH@cCpwZhM<3wyq5l%=vUv5CTEi^qW5)@0S8fsix`y
ebp5P+O0>xDgR-{A(zb~P3U2GSB{y6FX@6kaSlhvyhYgmE5jk_DGlQjB!*VJu(Y?AYHF=PlBAB4mC-gApCv0dkhDAYnm|xOId(AT
m@61%}CHQ`B%E@Mv6Eoq{u7g%!U7-<>y4msN&))ud8tDG|HM8{ip9a&cHJ=<Fyia<N6m%26Ad1kPiHw%?-
^If5LDM`BdPxxxn{#TY7bM|T+A267pJKV@<dqz|oYF}r_EN8`p0PQ9t`B%Gy+r|NlhFD<-
BIeQ#gcH|?&V?wnbqxQ`>AAEB_?qR~jc}SKWO7k~iH&du>2x7n}n~!Cgt#B7gs&L@1?81X7q+H^q{Qv+tC0wxQ-
(c#Do!^h7EhRwwVHU4%!z3dOt7xt%o*14l8-AEl6KOGEEtoi{{2zRWaK~5GeGVE&#ag@l6FSGHBTvd-
c@L>B#rI2Arri2Q<m`uWs=dkR^brx&ibbIm;Jtl<F<z!RpH`~2$5SK-
(#aRl2NXEhK)E&UeF@ZW6%OafT5MEiJNHgn;G>b7_%!7!7`a*BnWwd2tXQ&H5k6h9Wne<>giRh%7ixktY)d}ReBo=4Qa{*&Jv0=q
PqASzG<9C}lN+M#v82DR4W(1z5;4a7F2wRI+{RiBvt!Ruq~D2*7KEHuLdVvz+8J<fUn^%>%?<QTNg+c8(PnP!TVXpA5swcjNOF@9
Px{K<me7G}5I?$(rtPnQt#u|hP!s6zjfyAPlnhi1O4klt`NCr$Swtrg?8fV@x|hfy>k*w%Xq%QQ+|{ZG<C9BL{~#XO$B^XLb9WWx
)&IfJ`8!Q*!0ImI4%70_2JGXMVQQ6;TEh61ba20BzwNBiN-
D|oINenFzDbKU!nJE4=g9`u(ou$yN!P~QcReu`<zNUG?V%O=MNZ3^3bi`z-(cM(kWl1_Xmhw=T`2E)y8-
<cngsEvMtXP>*fFjaTAJt&P@VR6`$Vrt99+>8WX4m>-
p_i072pMJ%x%WzgQ@nnhC^bv!vml$1rd6Qp{{#bQM&x*5aU(+Xnopxr{rv8U*dvI7dCp!{@=_e#>wc=o!tOk1n~-Z+|~-
wlJYs_^ANygOg64`XVNcH$jln2+bm!+>$XqSlau-ir6}$fEN2BZ`tNE=^%(e7++-
U&UHJZi8~GcIg+uI2*14%(rEHS)plfl6@p7?=!Ac)2;a+m7eo4~$S?G`#3IIDRBk)GF4~?ClhlGIW78T!Pm8vuE&5s{=`Y}PDKD^
I2pt+Q22q8l`Z|4_-HKau9HZGuWEvzuV$qY1j=jupT)sC}FClv0?YH;ohC-
5u_nvO+gO9Z}=UcvgQF!ax6HspVO2g4R~_B~x_p&%uvZ}*gwI_WFce%LDdj0+aDPJ?{rE>@U@?p2>t7+w06?~L#-
%&ZhX$IPkV(E#hnMvA*up80ln(JfL^ruPD+5H~9xil0Yj&~h|9p_x_i2>0j(YB4z{^Z*rG0ClH2l`hpTD)}4Y$d0uEd$OP}*g)Vp
E0b1<6dfOIw;7L&IECDJ8su8dq(S3sB`upbIdg4q&NJBQQUPO}cN&&2dKmF^>puvn>H5Cql*pIzAfKk;Q`$48C0Dbx3~)R*qfFuE
W}bJSnm+Dw)EfK&uhW~A>T)4>7W`c6RrEG(m(cKCHQ^YT7HxH?vP)*9+|M%z73#e>QDu4+B=Q{F%gC#h696?C>w=Wy7Da{98u}ub
S<ZA5@u1u!{*rP70_=erkr2ZOdUPmkx?AteMMf2Qv%D{vY1FMaXuA64eQ~wVlz<HdeD+qNA$!c5j$ZRbmm<P$>B0+h1`2OQ*VK>q
JQQo+%nv}^>xW>kD{@wYhfQZ;%f?v4W6^kOXx9vZ_M@7!{wnorJ<7p-
WCzO0yEo5e$3KI#*&~XWhrcc_HepA;=#~da=iUp9idfPz4hYM)*P@rYV@`^QWZNpO`wtQv@(16MnqwU+Ahg}~XEN+I)eR|C)V%)r
mkEEl!egbCkV(22mlt;Gg%`CKtctr}k9eoVv6>nv&#e-
ZZ&~!M?$_P;H)*iM=BmYi#75L_e?4)kDQ(hRp21(f1EiW{iU5xiRcP~cDFbbho8uYM<Pe6LaTs8G!ck<SlFQ7FNxVhTs5YZNdg6x
Zt95kjHbN4esT>AK{z4D0Gds`BLu&Qk(=EEdKea{f|8?em>k_EfDEu%<a#~=;Y+tsv8kt-
M66AM&q48@fCIgjp?nNRi?m>7!edl<?Aesqo3t{BFV|S8Qy*>8ph;iX?GIF@+<o5Ka7v2Q3vK*~n5MIhz9J4w)E7fKNRjm0%?iLJ
D{MF6zs1oU|6DAbEhg^>hh3dNlh#axM%VDm9lM%OU{r9*mHCa&*3+eh`+68ETV{z-h=&ue167x0j$TTooR=1lF`KpUqmEbip@-
X;!k=gPJYNxytA?nH1Ao<X@S9$jl>U3F(3&R&l?PxCfCRv}7gWpF)G;MNm+~cn3k^zN#kf&-
>d*qx<YiT+CKKGy!qUOMaE<BW+gP?l@KKp&NN_NhJ0}fvD{SNr9Oa5Y=7NiM?90bf0JedlYIh$i7x$k@Hm}-
_oPLsxNv{9z2_j)F2pScm7|B5y`5k|^HHXHsqbg2lCnBPQLCii_rFSc_D=Nd5V9c5l!I4{p>kLHe~V$}a%QUzEw|EM;f!w5T8V2n
$OL<8hWTCmO))cri+a(N1{yj;#fO)Lu=!VmmWvMw<wHIBqN{7v1a73QbbaH8}y4-BxW=eB1GytlP9FzXO-
9FVxeSwdCw%V)5Z6R$SQ7vhF~??45eimYl>GkCpgdS=H`6;|TQaS_X8CP;^0UZYEWVjb?(X^!7?72(d0+AqJkgAvskpCfbcp;)3i
_U6mwG^~wGYi+FCD<&?dyeQ1cz1EpyRWM=Ir9!wB8i!>CCZ1KQYcy}Y!13y*%$0oFI1xrns^KURM=dwa_VHYIlVNTEwI&-
G;2wl?I2~)t{c`A%5y1w3ay(xVUXXa9wONRByI9zXM&dS1;<r<4N2m^f?~i55r_hg>cD6>bQamb&LetF|ukw4~ZhUjvIL-
g2Ufsqg0$zDMvaoT>@i3B88~?$2da~A9LHY?AjtDOXomI({s{KQ<p5=lQ)H^)OiOkYmlXUPZJn6<>2(3+{GYt0KC0VkMbL)g<uP%
&@u6=4`(%7u!Su2n;*?(kid#n1?{JWoDn}b`iZQ2YL@zyQ<eJ24)x6?2xyBK;=u!OXz^iY4AEl`dDUb2j^C{zyREFRb-
&=CqvhxYN9l!avSTH>#T0}E|6(6cV-
{FJ6j$GZ~A=2KwJcmvh`XYSJg^YcPQYq0qo{wSVa#fLLJJzouwec#A=V50O_o^s{t?#f*Y(O)xhs~Tlb%hfps=U29ffQ`j5mDdQ_
T{#ald$}5S8+6oalj<Tx9m&iNI_Or|034Nge;C*)_8*EWFik7SeflzOpyS&dyf-
9jjS3`uwn+N5K}b~5L7NXwG9Hok>o(n14pS6aAo|uLmv6D#nWQHj{4>(5G8=8PkzKjl9SnQ7IIrT5fxpZp2Ogm#;ZQU$klRBPS*q
pz=I`74lrN5=k{cbhlfJxjSS2!1b;r1BT=NNKZkE8_v*K?Zqi|>VVDK*DTb<Yqj9g3XH5EN>N5OvMX#rN)h-
CEmlMA^`MVxcV7TB;HG-wGl2;E$eEU?~aRL&~r%op~Xbta=qVMQ!@4+jn{HE-
>;5I!?WkD5}GR}gV~;4Q$0{%YoBmkObhl$h42;s5b^Rbv$B+6WnW$$6DL<r)6aTII2PjcC|h`7&L|aIdaIKktjFqi(q`x~SAdG?|
c>F4+KYOoz5<R?HRFb)KJkEF%X&7$;6GHlWxwK>d03p7i}1`moTUb8rs|xbI}oyS=o9S1jQz6MW0mp2Pj#yu)!C`rXA?x%)w!Z}v
nZ>DAGkDlUr!`61oYPkwy|Pdq(DyN_e!;SV9@;41KuJ43`e1ESOlImTeQwn@(ut(B*tp7^F^&AL$TOTXFD00x8hTj~^&f7CkhL0V
eMX-
0k16)yaBog>=?rqA=u`YAldYoPvg3mK+O*||9vyZ&U^z4aHup@94_vgo0~uI)G!;n=S*hHyt?8C!xXwb0n3eU|qG(ingJ^g0o#x}
k5+cfMJw-
2M9o5H`io92zIfpe+7D@H7_OG2=r+O9jX3u4GXC*h761X~jGl&0~rBJ^Cvdc~2KZ>YHV1yp9I!tY?y^rXU`vIfCF!o(3XbPKQcuO
q#=?{9cFu??nq)eW@G{-cp71N|JdpdHCG14o#ba!}%D0@SHC37RG8IeYR-
(e9tWhs*RniL8aZLRJP=I%I!Ktvw1ng*1#rT)S0m`ep=_u><p*aMt&(WIJi)$3ZNG3rH{Q&GJDe8K#hLY+t7$AhuoWUWPoH=c_a>
OB~oo!gf-
D=Wi$9M^_d|0OAV#}wSWR;J#8g5_O#nUl@3b4ESUq)d(U1^USDV&@EQ#tE6|o)W4@mg#sXjh@R%Ho5xg#{UC04TykYbHr9o$}B7n
+{nfzz9S_!=q-KTz#B89~;7oZN>J83lTM8Sw#x6jaJ-GnV%rP$gEj)#q8>3G~UE4R#FFb7-
=A1#w?lQg@05vur0TB1n4P2%xpGG<h-)kw@Nu@}tI8|*=xjX=&|z!G^kV`L{U-
51DSc5PNc86%^78l8}*Z(#IBiJg63zP7u3qDreWT-
H6)T<)+d@3FDNtM`$!50T9qW3<88G9e|A+5kZmWn~=GQ}V_9Ey3{h2@&;58;~Z!oTgApSiM0)j(|r5=y~utPX{Z^4@qIdtY@;c2T
PcfcygYFRFwOccc1aNUjF_1lXsEW+Ghi10)aupVtR}AY00Rl(1An=_`IQtS&yGpO)bJyYrt-l*RO2dJx4Dlzv(EH-mD_&Y?_u7^`
grT1P+P4PyZ|oT0*u9|JCj|wSOyJenMg1%*w0b>$sDf+$td}&v~YW5sjXmkSBJ+y1E3$M3LhP@tf@7RWcG_`#YjpD=N>ten}?>jZ
^be-AE(XT{E3D*s@KcI#{VFiy|n<%`c>QoZ)xrZVedS2y0opiCA|C23h`nWH7I0WBpD~(b+4Z5_^I##fX<qwkGm!h%a<aL@?ob;#
Ec0_sbNCE!ykJ<OdwN8EmaSw`~w3ScTk?j0M5(1{pRIt?R;l#G8a<c<8Rg9H5%1UWjlt?)ACrFTB;2TM(DF8vj|FioGUiq^oRJ$r
P(0s-0K_tZQFd7hJOrFc&Hgc<)os$GVB^c-Igd%3#!8i9B}nS$)7#=z(W~X1Z&xy$RCJ8R)BSE4p-7tA*xgb-Bo;efCE1<F8c>ox
<eg413=Dv<E3vz1#<T5?k`5SNTo8+X)IUqABUwyKP}!+*(?`jhQVwVVaPwX($22z^g&?BMkEm{lQvzFd_g-1tvJ-
^NhN7BJe9%BI=o_iX%nkg>~vR&Ec9<&}Xfc^1NRnSaKNYMJmyTpT665+V!fRHx?TP3mrWf(nI~XBp2&IR@a>Eh+vsDQHNy#kZy<i
)!!=0T{>mx2h1)WdE2QJZGxUXXb4xTbj_C+@+-ldqbwx^GHH6W(!j|(WD_590^6cvN%Z-
y#gO&LT`QGpP(uhBcIPmp$IlsyzFyLTdYdoD3;RA+%4{=gc@Dy#Qkjx!WdFm(wFgKfU71V0KYy8D5?d0lj~#$a`u>+$y9vf<_XL7
7seH3F%ab~hfmUDk%fB*N$ri>*FA~#GS;FT-Kw(3ZSl?UaOoxb3w$PZx<wafqz3kw;^rgT#n_92<?GY-
&=`zHq2k#QW|KTkh1}Moq@-
r2K^Z42%&fun9%j2xS=$o8BP|lw@Q59A8?pr&QSfEn{8D><}Idl^5=#rQIE70T}?k#S=l}ntdYD?Z}Z^^B6J|ER+c5Z*~-
#zG&Fh<B}woY~{bG)WxN0-EwFP3=UA%3obYf>zjO*A?pv-
e<?%fpYXKJL;=%OP)kjYoL~X+;imEjT_}O@ng`kX0wDx+5GI5W}zlQd>z)I@I8%#W)sU6)h}5%juTol|b#6FDBt7OE`J?ocNZgEp
7peAJt!Ck|hTyC1=}$zw~wEsQ)8B*~$@z4rz!;7te$Lw^8&Zum}Ksgx(47N*mW7!#c7a0Kl_DZGjWIjnHvZ!<yo?xAeDA)j8M3+B
^ciN^9Nn)fz~;F+6gZ@tUY{yKLGlry13zhcol)9m3-
j;hoKa2XPP9{7^XM4hk+~uoO?rLmuX$Q?>sK*t$)};tNLW43C=8$hG@0BoS~LT}LPfeSUEBAKIq%WE85kENpe_kNdp(((REBWiM}
jC&GjQ(H)bbaxZw=!u1up%>@wI@s}a9gczDB<;e6v>5f{Br)0bvpRv?NDTv}%`~6VxvC8X={!IQ?T@s0gPi<ZgqZW!i2f5v-
;l73jAxc<r&vwSBu?8_BUUB(e&-
HocT?CP|sP=EH_X!WY6s$c>5=3}IB}stin{x<GUDpu}(TT+}!3g=}0h@+ds|&<mX@tH+A#njDVZ%I^^+M?B*Ub#QJ~Q_TY+)PQ45
1up*Pj_B9DaD*ESqTt+(66M1&xXVF!$!AV(n~^JvZw8-r9c%zg)|;KA-
}M<rfO|tpB0(z&O?563)GitN=$LX+dA}63tAU!W2s%xZG^v8P_7u0`1zJW3pe&NMP59dC>eC&%$b7I$24cpOH-
2BxWf5I9|mbn5PB97DT=}s#z9oS4FB!vqv?TP@k5NV7tg$mz`J4$k_#6UzDuQiE;xxT;AL<jNqX8dXLDNrFhDW4u*2csD>?57Hp;
FjBYKki3-
ulMFvYh<eFa8^r@V7iR7#S)U!l(N*l}YnPY5mUswn4ijuJVSh~tsrg7gEbMog(fs*|#IIc!P;T;*Z)f17eN1F|8!+Ujm`oBi~^Gi
aNtWL<>3F;9Tz;bT9##a(NM7t7N-!wH)r+jS=B9G3=EwZki7h`OsW7ulOHS2a91pjp-ccnNKW#OD*Mn8}E7T558#NwRx&ClB?Qa7
R61_`r#Z2c=4{+}(Qp{^~2&_7t2Ap+S%34UfgWaz@-gii}Xa5WJ`!U1AQPC9*%KP3DTaJ14<u?crPp!>NXAP$v!bn{xa{dC|a0-
DcYcV~Xo#i?yRX&Zn3Q2EPHiio~CP^?&CKpkFj(nbu7mT40hQZ|5lIy_?pRH{1DZR%t+*(hjp_hQSeNI)DqAJ26DXD9veS&t6=FZ
PQ%b9!`nc`|FqFh<OOR@%`2(+9=`*!;eW)@w)Cc_j=TF^A}F9Qd{#@KYQ*A58JayWW@&_J_r#wtR{S&v#)Ip+KXsx)e5_pPy0FO3
KF%?6l|Jk3F$ARE$9c`^(dsINULRbMKkETOL<uaI1s4E&Y6Bp^-
5GJHwa?D<*UfMk85Dn8Zsacl`NMQe5ZRDw*FN)sOYM#ZsHNRqh15s<s4CB;I<GX=HAcY}9%YUfFOi>?3ftar_!+By6N7AYTdNfi(
QRM4#n8DmJ%TUqmu^%N2nh%0ArFMO+9(2C16u4J+Opx(HPA4A48ul%)CO`mC|YyBqc1#!_SY*H;ELp+ATUo<MwZ7)j319`Q6ylZg
=KHW>I7G0Bf*v!jtBiv#CVYSMTj0d?gSX{lk?1&TM{q=aDwGKMBrN&uYb^$Mw{!*vjPp-fC;_fDRIG-
*?Vy=>iy`Le<a&xpl${%MCUW;LVc^L?i#?}=npNz*wz^Cai(j^;_ssk`^il=4h)j$nDV0Cn0VE?NuBunXnLPya);I+fAsu(6#qML
N6o7WvEISM3&EuY?O^AOp%ux+(<hi8vA75BW9jfU)sWfI9WLdZJzd=1#&lNn}g4%dvX<1SD#`xrBEn`pb>q$hJY)gzHs{YK@xug_
ythRw!^(w2Ho)jF<>m!Dl<<@-lKYHh##swiU{l&Kp!T8zfd3u)$~c-
HG5jq;K7s;}iu*Z5q>3611`I4*;Uzm>#uf*yasx&1C9<D@|r+FlO0Wb8NNJGXFsxkym#Q!b5L4S4d=KknbgGfc9o60CM$M!yW`gV
kv72?VTUO00000<hoO0gJHp(00Fk70sV;vG92TKvBYQl0ssI200dcD
"""
def pin(b):return len(b),hashlib.sha256(b).hexdigest()
raw=lzma.decompress(base64.b85decode(''.join(DATA.split())));assert pin(raw)==MAP_PIN
files=json.loads(raw);assert set(files)==set(FILE_PINS)
folder=Path(sys.argv[1]);folder.mkdir(parents=True,exist_ok=True)
for name,text in sorted(files.items()):
 b=text.encode();assert pin(b)==FILE_PINS[name]
 f=folder/name
 if f.exists():assert f.read_bytes()==b
 else:f.write_bytes(b)
print('HEPTAGON_ALL_RHO_COMPLETE_SOURCES_RECOVERED',len(files),*MAP_PIN,flush=True)
if len(sys.argv)==2:
 outputs=[]
 for action in ('build','check','parent-audit'):
  run=subprocess.run([sys.executable,'-B','-S',str(folder/'heptagon_all_rho.py'),action,str(folder)],capture_output=True)
  if run.returncode:
   sys.stdout.buffer.write(run.stdout);sys.stderr.buffer.write(run.stderr)
   raise SystemExit(run.returncode)
  if action!='parent-audit':assert pin(run.stdout)==STDOUT_PIN
  outputs.append(run.stdout)
 assert outputs[0]==outputs[1]
 assert pin((folder/'heptagon_all_rho.json').read_bytes())==REPORT_PIN
 assert pin((folder/'heptagon_parent_pool_audit.json').read_bytes())==AUDIT_PIN
 sys.stdout.buffer.write(outputs[0]);sys.stdout.buffer.write(outputs[2]);sys.stdout.flush()
 print('HEPTAGON_ALL_RHO_COLD_SOURCE_BUILD_CHECK_AND_AUDIT_PASS',*REPORT_PIN)
```
