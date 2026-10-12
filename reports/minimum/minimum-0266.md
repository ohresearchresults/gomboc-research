# minimum-0266

AI research report · 2026-09-27 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# WILLOW_H5_ROOT_PACKET_AND_COMPLETE_W_ONLY_ORBIT_V1

## 1. Strongest findings and scope

**A genuine whole-facet-root exclusion now holds on a five-dimensional H5 box.** Throughout the box specified below, the three true weak arrows forming the exterior path

`4 -> 9 -> 7 -> 0`

are incompatible with the physical normal foot of the actual facet `F2=(7,6,0)` lying anywhere in its **closed** triangle. The certificate has fixed integer arrow weights, fixed rational edge multipliers, and a uniform positive margin. An explicit rational SPD metric on the literal W_ONLY_RESIDUAL body makes all three arrows strictly positive. Consequently this packet cannot be excluded by any nonzero negative-semidefinite nonnegative combination of its primal arrow tensors. The root hypothesis is genuinely doing work.

**The literal W_ONLY_RESIDUAL whole metric orbit is also closed:** at its actual uniform volume centroid, every SPD metric has at least two strict unstable vertices. The new whole-facet method covers all nine facet-root choices and all 48,790 labelled primal rooted trees. However, an independently generated ordinary-PSD cover also closes this point. Therefore the complete point exclusion is not evidence that root conditioning is necessary once complete primal trees are used. The strict improvement over ordinary PSD is established by the local packets with physical strict-primal controls, not by the mere presence of indefinite stresses.

A further result gives an explicit same-lattice, genuinely refilled geometric collar around this body. A two-arrow control shows why a rank-two PSD margin reference is useful at the normal boundary of the root dual.

These results do not close whole H5 or E17, do not change a canonical incidence registry, and do not provide an attainer. The inherited bracket remains `34 <= C_min <= 622`. The wide five-dimensional theorem excludes one specified root-and-arrow packet, not every metric throughout that box.

## 2. Input audit and exact physical geometry

All four supplied files were read completely, including the journal consecutively through line 2563/EOF and both literal parent payloads. The native attachment byte counts and SHA-256 values match the manifest. The two parent payloads were additionally reconstructed as compact UTF-8 version-2 JSON envelopes, retaining the Markdown's final LF:

- CWN: 38,001 bytes, SHA-256 `9d6d4bb7467bce10452f7713b241cc60dbd441bea84f7100c4bc37c967d53825`.
- LjZ: 37,862 bytes, SHA-256 `c858f67518fd87fccd41d8bf201b5d9b2be0d809750afdcaeb410696e568b021`.

The exact H5 source is SHA-256 `54374c6e67c89467a37f68dca0c076ee20a8581acc2791d228f0c8e8f6d9aad8`. The whole-root proof is SHA-256 `c9db1bd5bf6233a7336f5a268c0270c5617a7a4ffe6c7f7ce09abf3b8ba498a2`; its supplied executable is SHA-256 `a720b725ff3670fb37e7f900638a183d2ef4f7e16cafb0a8ea7c45e4cf6afc47`. No alias or geometry conflict was found.

CWN's optional old extension requires `h5_seven_turn_reflection.py`, 18,109 bytes, SHA-256 `125da77daa965228d1486bad45fdf6dce556a54e6269aa08c0242d9741170d97`. Those source bytes are not in this pack. I did not execute that extension or treat its unobserved execution as evidence. The new sources below do not depend on it. LjZ's covariance theorem was read, but no covariance floor or spectral cap is used in these exclusions. The old extension's dependency and execution qualification are explicit in the parent.

### Geometry and actual moments

Write `theta=(x,r,p,q,lambda)` and `s=1-lambda`. The basal vertices are `z_i=(s*b_i,0)` for

```
b0=(1/4,0)
b1=(1-3*x/4,0)
b2=(1-p,p)
b3=(q,1-q)
b4=(0,1-3*r/4)
b5=(0,1/4)
b6=(1/16,1/16)
```

and the top vertices are

```
z7=(0,0,1), z8=(lambda,0,1), z9=(0,lambda,1).
```

The true outward maximal facet cycles, indexed 0 through 8, are

```
(6,5,4,3,2,1,0)
(8,7,0,1)
(7,6,0)
(1,2,8)
(9,8,2,3)
(9,3,4)
(4,5,7,9)
(6,7,5)
(7,8,9)
```

The complete true edge list is

```
(0,1),(0,6),(0,7),(1,2),(1,8),(2,3),(2,8),(3,4),
(3,9),(4,5),(4,9),(5,6),(5,7),(6,7),(7,8),(7,9),(8,9).
```

These agree with the exact supplied realization; integration diagonals never enter the mechanical graph.

The actual moment formulas are

```
a  = (31-24*x*p-24*r*q)/64
bx = 509/3072-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8
by = 509/3072-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
D  = lambda+2*a*s*s
Kx = 3*s**3*bx/2+s*s*lambda*(1-3*x*p/4)/4+lambda**2/4
Ky = 3*s**3*by/2+s*s*lambda*(1-3*r*q/4)/4+lambda**2/4
Kz = a*s*s/2+lambda/2+lambda**2/4
g  = K/D
```

Here `D=6 Vol(P)` and `K=6 integral_P z dz`. Both new geometry implementations compare these formulas with actual oriented-boundary integration. Set `v_i=z_i-g`, `T_ij=sym(v_i(v_j-v_i)^T)`, and `D_ij(M)=tr(T_ij M)`. Every pole is normalized from this same actual centroid. Its physical metric is always the inverse of the primal metric.

## 3. Wide five-parameter closed-root theorem

Define the closed box

```
x      in [1/100,79/100]
r      in [89/100,91/100]
p      in [1/100,7/20]
q      in [29/50,31/50]
lambda in [1/20,1/4].
```

Every point is a genuine 10/17/9 realization with the displayed maximal cycles and edges. Put

```
A = 4*T70 + 5*T49 + 2*T97
delta = 1/2000.
```

For the cyclic root triangle `F2=(7,6,0)`, use edge multipliers

```
edge (7,6): 9/2
edge (6,0): 10
edge (0,7): 7/2.
```

Throughout the entire box the exact certificate proves

\[
q_2^T(A+\delta I)q_2<0,
\qquad
\lambda_{ij}\operatorname{sym}(v_i v_j^T)-A-\delta I\succ0
\]

for all three genuine root edges. Hence, for every SPD metric whose actual normal foot of `q2` lies in **closed F2**,

\[
\boxed{4D_{70}(M)+5D_{49}(M)+2D_{97}(M)
\le-\operatorname{tr}(M)/2000<0.}
\]

All three arrows cannot be weakly nonnegative. This tests the whole facet, not a chosen or sampled foot. The accepted whole-facet representation supplies the general dual theorem.

The sufficiency needed here also has a direct self-contained proof. For a physical foot `p` in the closed facet,

\[
M=\alpha qq^T+L,\quad \alpha=p^TMp>0,\quad L\succeq0,\quad Lp=0.
\]

This follows from `Mp=alpha*q` and Cauchy-Schwarz in the M-inner product. Spectrally decompose `L` into `w*w^T` terms with `w.p=0`. Since p is a convex combination of the facet vertices, the values `w.p_i` straddle zero; some true boundary edge has `(w.p_i)(w.p_next)<=0`. Its LMI gives `w^T(A+delta*C)w<=0`. Together with the normal inequality, this proves `tr((A+delta*C)M)<=0`. For any nonzero PSD C and SPD M, `tr(CM)>0`. Thus the margin conclusion includes edge and vertex feet without a proper-root limiting argument.

A retained stronger inner result has the same first four intervals and `lambda in [3/25,9/50]`, where the margin improves to `delta=1/1000`.

### Exact continuum certificate

The root's raw normal and offset are

```
n2=(-1,-3,-s/4), h2=-s/4,
q2=n2/(h2-n2.g).
```

The centered height is certified positive. Put `R_i=D*z_i-K` and

\[
U=\sum w_{ij}\operatorname{sym}(R_i(z_j-z_i)^T),\qquad A=U/D.
\]

The cleared polynomial tests are exactly

\[
-n_2^T(U+\delta D I)n_2>0,
\quad
P_{ij}=\lambda_{ij}\operatorname{sym}(R_iR_j^T)-DU-\delta D^2I\succ0.
\]

No centroid or pole is frozen.

Each edge polynomial has multidegree `(4,4,4,4,6)`. Edges 7-6 and 0-7 use the two closed taper intervals `[1/20,3/20]` and `[3/20,1/4]`; edge 6-0 uses the whole taper interval. The wide certificate contains **21,875 PD Bernstein coefficient matrices and 153,125 strictly positive principal-minor checks**. All seven principal minors are checked for each matrix.

The normal polynomial has multidegree `(2,3,2,2,4)`, with 540 coefficients per leaf. Its three closed taper leaves have these exact positive coefficient lower bounds:

```
[1/20,1/10]: 132706025707/6400000000000
[1/10,3/20]: 138236951979/51200000000000
[3/20,1/4]:  670310328427/102400000000000.
```

The stronger inner box separately has 13,125 PD coefficient matrices, 91,875 positive minor checks, and two normal-polynomial leaves. All coefficients regenerate from the literal polynomials.

Geometry is verified on the same continuum: positive volume, all 56 nonincident support slacks, all nine centered heights, all 34 oriented facet corners, independent incident normals at all ten vertices, and opposite-sign witnesses for every one of the 68 noncofacial triples. This excludes hidden supporting facets. There is no infeasible-cell pruning or free mass assignment.

The theorem is not confined to the old `gamma<=1/3` W-only setting. The corner

```
theta=(79/100,91/100,7/20,31/50,1/4)
```

has actual volume `281761/3840000` and actual centroid height `481761/1127044`, with `gamma-1/3=318239/3381132>0`. It remains covered by the root-packet theorem.

### A strict primal control proves genuine improvement over NSD stresses

At the literal W_ONLY_RESIDUAL point

```
theta0=(1/10,9/10,3/25,3/5,3/20),
```

take

\[
M_1=\frac1{1000}
\begin{pmatrix}466&907&108\\907&1993&256\\108&256&36\end{pmatrix}\succ0.
\]

The exact arrow values in order `(70,49,97)` are

```
2862867316043/2256104960000000
6603274786539/5640262400000000
176339726607/141006560000000.
```

All are positive. Therefore no nonzero nonnegative combination of these same three tensors can be NSD: its contraction with M1 would be positive. The specified A has

```
tr(A)  = -4202296088839/902441984000
det(A) = 618557049357495852350551/25450047952683008000000000 > 0,
```

hence inertia `(+--)`.

The full census uses the actual inverse M1^-1 and has all 68 primitives nonzero:

```
S=[0,4], U=[3,6], H=[(0,1),(3,9)]
strict (S,U,H)=(2,2,2), physical weak points=0.
```

F2 is not stable in this control. It is a genuine local-packet witness, not a U1 or S1/U1 survivor.

Exactly **1,212** labelled primal rooted trees contain the three-arrow packet. Their root counts are

```
0:488, 1:232, 2:120, 3:40, 5:61, 6:183, 8:88.
```

The complementary dual root F2 has degree one in 970 cases and degree two in **242**. Thus the packet is not confined to triangular-root-leaf cases. These are labelled overlap counts, not canonical registry increments.

Reflection `(x,r,p,q,lambda)->(r,x,q,p,lambda)`, with vertex exchanges `0<->5,1<->4,2<->3,8<->9`, gives the F7 theorem with stress `4*T75+5*T18+2*T87`. This is transport of the proved domain, not an additional independent census.

## 4. Complete W_ONLY_RESIDUAL metric-orbit exclusion

The literal body has

```
Vol = 881291/9600000
g = (7368835529/28201312000,
     3427883561/28201312000,
     50317/153268).
```

This is the whole-shape challenge identified in the supplied branch memory.

For numerical scaling only, the complete cover uses the rational gauge `X=L*v`, `L=diag(1,2,1)`. Its metric is `M_X=L^-T*M_raw*L^-1`, and its inverse is `L*M_raw^-1*L^T`; they are not independently chosen. All tensors in this cover are expressed in X-coordinates.

For each root pole q_f use

\[
C_f=I-q_fq_f^T/(q_f^Tq_f)\succeq0,\qquad \operatorname{tr}C_f=2.
\]

Each row supplies nonnegative integer weights and rational `delta>0` with `A+delta*C_f` in the root dual. Rational edge multipliers are reconstructed by the exact Schur formula, and every principal minor is checked. Since `tr(C_f M)>0` for every SPD M, this gives a strict contradiction to the selected weak arrows even at a closed root foot. A PSD margin reference does not enlarge the accepted dual cone; it makes useful normal-boundary packets accessible to a positive-margin search.

The exhaustive enumeration finds 4,879 unrooted trees and 48,790 primal rooted trees. The certificate counts for facet roots 0 through 8 are

```
478,513,510,361,390,512,437,452,199.
```

Totals are **3,852 certificate rows, 14,808 PSD edge blocks, 103,656 exact principal-minor checks, and 439,110 facet-root/primal-tree cases**. The minimum `delta/sum(weights)` is `2584021/2048000000`. There are 340 indefinite stresses, distributed by root as

```
3,4,94,79,19,9,56,36,40.
```

That indefinite count alone is not evidence of strict enlargement; the explicit physical controls establish it only for their designated packets.

### Mechanical implication

For every SPD metric, a pole maximizing squared inverse-metric norm has strictly negative derivatives toward all other poles. Its actual normal foot lies in the relative interior of its true facet, so at least one strict stable facet supplies a root choice.

If there were a unique strict U, every other vertex would have a true nonnegative outgoing edge. Along such an edge,

`||v_j||_M^2-||v_i||_M^2 = 2*D_ij(M)+||v_j-v_i||_M^2 > 0`.

Selecting outgoing edges produces a true rooted tree toward the unique U. The exact certificate for the actual stable facet contradicts its weak arrows. Since a maximum-norm vertex always supplies at least one strict U, **U>=2 follows for every SPD metric**, with incidental weak contacts allowed. This includes all invertible affine images with their actual uniform centroids.

### Independent ordinary-PSD control

The same source independently generates **562 ordinary-PSD stresses** covering all 48,790 rooted trees, with 3,934 principal-minor checks and minimum normalized margin

`9359849/8192008192 > 1/1000`.

These exclude the selected weak trees even for nonzero PSD matrices. Thus root conditioning is not necessary for the complete point exclusion. This useful control is retained rather than hidden.

It yields a separate actual-refill collar. Any genuine uniformly filled polytope with the same nine outward maximal cycles and

`max_i ||diag(1,2,1)*(z_i'-z_i)|| <= 2^-23`

has U>=2 for every SPD metric after recomputing its actual centroid.

In this gauge the reference raw norms are below 3/2, its centroid norm is below 1, and its six-volume exceeds 1. Perturbed raw norms are below 2. From the 16 oriented boundary triangles, a matched displacement epsilon gives

```
|Delta D| <= 192*epsilon
||Delta K|| <= 384*epsilon
||Delta g|| <= 1152*epsilon
centered-vertex error <= 1153*epsilon
arrow-tensor operator error <= 4620*epsilon.
```

Each determinant changes by at most `12*epsilon`, and each first-moment term `d*(a+b+c)/4` by at most `24*epsilon`. The new six-volume stays above 1/2, yielding the centroid bound. Finally `4620*2^-23<1/1000` preserves the global stress margin. The identical true-cycle hypothesis is essential; arbitrary point perturbations or graph changes are not covered.

## 5. Boundary-aware control and meaningful failures

At theta0, the top root F8 has the exact two-arrow certificate

```
A8=2*T10+3*T32
C8=diag(1,1,0)
delta8=1/100
multipliers on (7,8),(8,9),(9,7): 8,9/2,13/4.
```

All three edge LMIs are PD, with 21 exact positive principal-minor checks, but `q8^T*A8*q8=q8^T*C8*q8=0`. No positive margin with a PD reference can certify this fixed stress. The rank-two reference does certify it. This is a limitation of the PD-margin formulation, not of the full supplied dual theorem.

Both arrows are strictly positive in the physical metric

\[
M_2=\frac1{100}\begin{pmatrix}3&7&10\\7&46&58\\10&58&86\end{pmatrix},
\]

with

```
D10=16561896608403/1128052480000000
D32=4190762819201/282013120000000.
```

Its actual same-inverse census is

```
S=[1,2,4,5,7], U=[0,9]
H=[(0,7),(1,8),(3,9),(4,9),(6,7)]
strict (S,U,H)=(5,2,5), physical weak points=0; all 68 rows nonzero.
```

Thus this packet also cannot have a nonzero NSD nonnegative primal stress. It is retained as a boundary-search control, not advertised as a new joint-root sector beyond earlier W/A reasoning.

A failed novelty test is made exact: the candidate packet `(0->1,1->8,8->2)` is already globally excluded. In the fixed gauge, ordinary-PSD weights `(190902,386770,422329)` have shifted margin `4618947/2048`. The diagnostics source locates, rationalizes and verifies that certificate. An indefinite eigenvalue signature by itself is not sufficient evidence of a stronger mechanism.

The initial single-box Bernstein tests for the wider taper failed for two edge polynomials. They were not treated as physical counterexamples; the two-child closed partitions above passed exact coefficient tests. LP directional cuts are discovery only. Every accepted numerical result is rationally checked. A solver failure or iteration limit is an unresolved case, not a physical survivor or an exclusion.

No convex-root-hull feasible point is used as one physical metric. The supplied warning that an average of strict-root metrics can have a foot anywhere in the facet plane remains applicable.

## 6. Recovery and verification status

There is no external geometry file, old atlas, parent executable, random seed, or hidden certificate input. The three complete readable source units below reconstruct every claimed object and check. Save them using the displayed filenames and final LF.

Observed environment: CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0 with HiGHS 1.8.0, SymPy 1.14.0, OpenBLAS 0.3.30. Numerical runs use `OPENBLAS_NUM_THREADS=1`. Root/global checking requires only the Python standard library. The locator uses LP primal/dual tolerances 1e-9, eigenvalue cut threshold 1e-7, at most 70 iterations per packet, and rounding denominators 10^6 through 10^10. The physical-witness locator's separate 100-iteration/1e-8 settings are also explicit in source. Floating computations select candidates, not proof acceptance.

Normal and source-only cold executions completed for the root, independent global, wide region, inner region and diagnostic computations. All seven generated outputs were byte-identical, and all cold-run stderr files were empty. The source-only capsule was extracted and its regenerated outputs compared with the normal outputs. This is observed exact computational verification plus the analytic proof above, not proof-assistant formalization or an independent coordinator replay. A different platform producing different LP weights must validate them exactly and record its own output pins rather than assuming byte identity.

Run with assertions enabled:

```sh
OPENBLAS_NUM_THREADS=1 python -B willow_root_cover.py build
python -B -S willow_root_cover.py check
OPENBLAS_NUM_THREADS=1 python -B willow_root_cover.py global
python -B -S willow_root_cover.py global-check
OPENBLAS_NUM_THREADS=1 python -B willow_root_region.py
OPENBLAS_NUM_THREADS=1 python -B willow_root_region.py inner
OPENBLAS_NUM_THREADS=1 python -B willow_root_diagnostics.py
```

Expected terminal markers:


[Encoded source block omitted; the code in this passage is incomplete.]


Exact pins:

| File | Bytes | SHA-256 |
|---|---:|---|
| willow_root_cover.py | 12008 | fb8bdcb79580924c4f7e1f5988f098e7614a693c74d3e0168bcbab3fbafd436b |
| willow_root_region.py | 11634 | 762f229c97f04deee611db0df260d1d10370a9551762febfdf2747a31c36cc8a |
| willow_root_diagnostics.py | 4475 | 591002f52ea0fa02c01cb77da7cdbd678f9fa8606eac383699890f70e9901a77 |
| willow_root_cover.json | 268556 | 2f2ba771744e24f2a28bba66f6db2762cebf12a8ace226b5fc1223aba2b5331d |
| willow_root_report.json | 2162 | 13cc30d700b590a08fa96a7c61d198c1a09ea9d909d5416a8ef561348082d754 |
| willow_global_cover.json | 42402 | 61630c467a258f099b4371102c9f6a894764b8605668dd21ff784a2beb4145c9 |
| willow_global_report.json | 1919 | 5da88f4fdae4e8019a906d6db1dbd79e5df8b994e9a30ee5c160ea8d02eb1568 |
| willow_taper_report.json | 111435 | 3d27e9c641008774cb1891ab33f27503a4ef89c93102058186b2888cb886a9f5 |
| willow_region_report.json | 108563 | 8ddd77cf8301bfb263ca2e1421443d80963da41779ffda9820635d57b60c55ff |
| willow_diagnostics_report.json | 2972 | ffdc41c29ef3dcb736f8a01ffaefbb1a4e31ea5163120840919e93de0848d6c1 |

### Most useful continuation

Do not restart the named W_ONLY_RESIDUAL whole-orbit challenge: it is excluded, also independently by ordinary PSD. The wide box still needs the other actual root/escape alternatives. Start with the genuine exterior path 4->9->7->0 at F2, including its 242 nonleaf complementary cases, and its reflection. Extend those mechanically literal alternatives using the actual moving centroid and cleared polynomial LMIs. Use rank-two root-normal projectors when useful packets satisfy q^TAq=0, and distinguish strict-primal-feasible supports from supports already excluded globally. Any whole-box theorem still requires exact coverage of all remaining alternatives; neither the present regional stencil nor convex-root-hull feasibility supplies that coverage.

## 7. Complete source units

### willow_root_cover.py

```python
#!/usr/bin/env python3
"""WILLOW_H5_W_ONLY_ROOT_COVER_V1. Exact acceptance, numerical discovery only.
Build: OPENBLAS_NUM_THREADS=1 python -B willow_root_cover.py build
Check: python -B -S willow_root_cover.py check
Optional independent ordinary-PSD control: replace build/check by global/global-check.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import gcd
import hashlib, json, sys
from pathlib import Path
THETA=tuple(map(Q,('1/10','9/10','3/25','3/5','3/20')))
FACES=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
       (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
I=tuple(tuple(Q(i==j) for j in range(3)) for i in range(3))
ZERO=tuple(tuple(Q(0) for j in range(3)) for i in range(3))
def dot(a,b): return sum((x*y for x,y in zip(a,b)),Q(0))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(t,a): return tuple(t*x for x in a)
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def tr(A): return sum(A[i][i] for i in range(3))
def transpose(A): return tuple(zip(*A))
def mv(A,v): return tuple(dot(row,v) for row in A)
def mm(A,B): return tuple(tuple(dot(row,col) for col in transpose(B)) for row in A)
def det(A): return dot(A[0],cross(A[1],A[2]))
def inv(A):
 d=det(A); assert d
 return tuple(tuple(x/d for x in row) for row in transpose((cross(A[1],A[2]),cross(A[2],A[0]),cross(A[0],A[1]))))
def plus(A,B): return tuple(add(a,b) for a,b in zip(A,B))
def times(t,A): return tuple(scale(t,a) for a in A)
def sym(a,b): return tuple(tuple((a[i]*b[j]+b[i]*a[j])/2 for j in range(3)) for i in range(3))
def quad(a,A): return dot(a,mv(A,a))
def minors(A):
 return tuple(A[i][i] for i in range(3))+tuple(A[i][i]*A[j][j]-A[i][j]**2 for i,j in combinations(range(3),2))+(det(A),)
def psd(A): return min(minors(A))>=0

def geometry(theta=THETA):
 x,r,p,q,lam=map(Q,theta);s=1-lam
 basal=((Q(1,4),0),(1-3*x/4,0),(1-p,p),(q,1-q),(0,1-3*r/4),(0,Q(1,4)),(Q(1,16),Q(1,16)))
 z=tuple((s*a,s*b,Q(0)) for a,b in basal)+((Q(0),Q(0),Q(1)),(lam,Q(0),Q(1)),(Q(0),lam,Q(1)))
 area=(31-24*x*p-24*r*q)/64
 bx=Q(509,3072)-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8
 by=Q(509,3072)-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
 D=lam+2*area*s*s
 K=(3*s**3*bx/2+s*s*lam*(1-3*x*p/4)/4+lam*lam/4,
    3*s**3*by/2+s*s*lam*(1-3*r*q/4)/4+lam*lam/4,
    area*s*s/2+lam/2+lam*lam/4)
 dd=Q(0);kk=(Q(0),)*3
 for face in FACES:
  a=z[face[0]]
  for j in range(1,len(face)-1):
   b,c=z[face[j]],z[face[j+1]];d=dot(a,cross(b,c))
   dd+=d;kk=add(kk,scale(d/4,add(add(a,b),c)))
 assert dd==D>0 and kk==K
 g=scale(1/D,K);v=tuple(sub(a,g) for a in z)
 planar=(((Q(0),Q(-1)),Q(0),Q(0),1),((p,p-3*x/4),s*p*(1-3*x/4),lam*p,3),
         ((Q(1),Q(1)),s,lam,4),((q-3*r/4,q),s*q*(1-3*r/4),lam*q,5),
         ((Q(-1),Q(0)),Q(0),Q(0),6),((Q(-3),Q(-1)),-s/4,Q(0),7),((Q(-1),Q(-3)),-s/4,Q(0),2))
 ns=[None]*9;hs=[None]*9;ns[0]=(Q(0),Q(0),Q(-1));hs[0]=Q(0);ns[8]=(Q(0),Q(0),Q(1));hs[8]=Q(1)
 for n,h,t,f in planar: ns[f]=n+(h-t,);hs[f]=h
 poles=tuple(scale(1/(h-dot(n,g)),n) for n,h in zip(ns,hs))
 for f in range(9):
  assert hs[f]-dot(ns[f],g)>0
  for i in range(10):
   slack=hs[f]-dot(ns[f],z[i]);assert slack==0 if i in FACES[f] else slack>0
 for i in range(10):
  incident=[f for f in range(9) if i in FACES[f]]
  assert any(det(tuple(ns[f] for f in t)) for t in combinations(incident,3))
 recovered=set()
 for i,j,k in combinations(range(10),3):
  n=cross(sub(z[j],z[i]),sub(z[k],z[i]));vals=[dot(n,sub(a,z[i])) for a in z]
  if any(n) and (min(vals)>=0 or max(vals)<=0): recovered.add(tuple(l for l,t in enumerate(vals) if not t))
 assert recovered=={tuple(sorted(f)) for f in FACES}
 ef={}
 for f,face in enumerate(FACES):
  for i,j in zip(face,face[1:]+face[:1]):ef.setdefault(tuple(sorted((i,j))),[]).append(f)
 edges=tuple(sorted(ef));assert len(edges)==17 and all(len(fs)==2 for fs in ef.values())
 return dict(z=z,v=v,g=g,D=D,K=K,q=poles,edges=edges,ef=ef)

def tables(B):
 # The fixed rational change X -> diag(1,2,1) X is only a coordinate gauge.
 L=(Q(1),Q(2),Q(1));v=tuple(tuple(a[i]*L[i] for i in range(3)) for a in B['v'])
 qs=tuple(tuple(a[i]/L[i] for i in range(3)) for a in B['q'])
 arrows=tuple(e for ij in B['edges'] for e in (ij,ij[::-1]))
 T=tuple(sym(v[i],sub(v[j],v[i])) for i,j in arrows)
 return v,qs,arrows,T

def trees(edges):
 out=[];unrooted=0
 for E in combinations(range(17),9):
  adj=[[] for _ in range(10)];parent=list(range(10));good=True
  def find(i):
   while parent[i]!=i:i=parent[i]
   return i
  for k in E:
   i,j=edges[k];a,b=find(i),find(j)
   if a==b:good=False;break
   parent[a]=b;adj[i].append((j,2*k));adj[j].append((i,2*k+1))
  if not good:continue
  unrooted+=1
  for r in range(10):
   queue=[r];seen={r};mask=0
   for j in queue:
    for i,k in adj[j]:
     if i not in seen:seen.add(i);queue.append(i);mask|=1<<(k^1)
   assert len(seen)==10 and mask.bit_count()==9
   out.append((r,mask))
 assert unrooted==4879 and len(out)==48790
 return out

def edge_multiplier(A,p,r):
 H=inv((p,r,cross(p,r)));U=mm(transpose(H),mm(A,H));c=U[2][2]
 assert c<=0
 if not c:
  assert U[0][2]==U[1][2]==0
  h=U[0][1]
 else:h=U[0][1]-U[0][2]*U[1][2]/c
 lam=2*max(h,Q(0));L=plus(times(lam,sym(p,r)),times(-1,A))
 assert psd(L)
 return lam

def accept(root,pairs,delta,v,qs,T):
 assert delta>0 and pairs and all(w>0 for k,w in pairs)
 A=ZERO
 for k,w in pairs:A=plus(A,times(w,T[k]))
 if root is None:
  C=I;assert psd(times(-1,plus(A,times(delta,C))));lams=()
 else:
  q=qs[root];C=plus(I,times(-1/dot(q,q),sym(q,q)))
  assert psd(C) and tr(C)==2 and mv(C,q)==(0,0,0)
  U=plus(A,times(delta,C));assert quad(q,U)<=0
  f=FACES[root]
  lams=tuple(edge_multiplier(U,v[i],v[j]) for i,j in zip(f,f[1:]+f[:1]))
 return A,lams

class Locator:
 def __init__(self,root,v,qs,T):
  import numpy as np
  self.np=np;self.root=root;self.Texact=T;self.qexact=None if root is None else qs[root]
  self.T=np.array(T,float);self.edges=[]
  if root is None:self.C=np.eye(3);self.q=None
  else:
   q=qs[root];CC=plus(I,times(-1/dot(q,q),sym(q,q)));self.C=np.array(CC,float)
   self.q=np.array(q,float);self.q/=np.linalg.norm(self.q)
   f=FACES[root];self.edges=[np.array(sym(v[i],v[j]),float) for i,j in zip(f,f[1:]+f[:1])]
  self.dirs=[]
  for d in product((-1,0,1),repeat=3):
   if any(d) and next(x for x in d if x)==1:self.dirs.append(np.array(d,float)/np.linalg.norm(d))
 def solve(self,idx):
  from scipy.optimize import linprog
  np=self.np;tt=self.T[idx];n=len(idx);m=len(self.edges);rows=[]
  def row(d,k):
   rr=np.zeros(n+m+1);rr[:n]=np.einsum('i,aij,j->a',d,tt,d);rr[-1]=d@self.C@d
   if k is not None:rr[n+k]=-d@self.edges[k]@d
   return rr
  for k in (range(m) if m else [None]):
   rows.extend(row(d,k) for d in self.dirs)
  if m:
   rr=np.zeros(n+m+1);qq=dot(self.qexact,self.qexact)
   rr[:n]=[float(quad(self.qexact,self.Texact[k])/qq) for k in idx];rows.append(rr)
  c=np.zeros(n+m+1);c[-1]=-1;eq=np.zeros((1,n+m+1));eq[0,:n]=1
  for it in range(70):
   res=linprog(c,A_ub=np.array(rows),b_ub=np.zeros(len(rows)),A_eq=eq,b_eq=[1.],bounds=[(0,None)]*(n+m)+[(None,None)],method='highs',options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
   if not res.success or res.x[-1]<1e-7:raise ArithmeticError(('unresolved locator',self.root,idx,res.message))
   A=np.einsum('a,aij->ij',res.x[:n],tt)+res.x[-1]*self.C;bad=False
   for k in (range(m) if m else [None]):
    L=(res.x[n+k]*self.edges[k] if m else np.zeros((3,3)))-A
    ev,vec=np.linalg.eigh(L)
    if ev[0]<-1e-7:rows.append(row(vec[:,0],k));bad=True
   if not bad:return res.x[:n],res.x[-1]
  raise ArithmeticError(('iteration limit',self.root,idx))

def rationalize(root,idx,weights,margin,v,qs,T):
 for power in (6,7,8,9,10):
  R=10**power;ww={k:int(round(float(w)*R)) for k,w in zip(idx,weights)};ww={k:w for k,w in ww.items() if w>0}
  if root is not None:
   qq={k:quad(qs[root],T[k]) for k in idx};a=sum((ww.get(k,0)*qq[k] for k in idx),Q(0))
   if a>0:
    k=min(idx,key=lambda k:qq[k])
    if qq[k]>=0:continue
    u=a/(-qq[k]);ww[k]=ww.get(k,0)+(u.numerator//u.denominator)+1
  pairs=tuple(sorted(ww.items()));delta=Q(int(float(margin)*R*1024),8192)
  try:accept(root,pairs,delta,v,qs,T)
  except AssertionError:continue
  return pairs,delta
 raise ArithmeticError(('rationalization failed',root,idx))

def serial(x):
 if isinstance(x,Q):return str(x)
 if isinstance(x,dict):return {str(k):serial(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [serial(t) for t in x]
 return x

def certificate_file(global_mode=False):return Path('willow_global_cover.json' if global_mode else 'willow_root_cover.json')

def build(global_mode=False):
 import numpy,scipy
 assert numpy.__version__=='2.3.5' and scipy.__version__=='1.17.0'
 B=geometry();v,qs,ar,T=tables(B);alltrees=trees(B['edges']);certs=[]
 for root in ([None] if global_mode else range(9)):
  rem=alltrees[:];loc=Locator(root,v,qs,T);n=0
  while rem:
   idx=[k for k in range(34) if rem[0][1]>>k&1];w,d=loc.solve(idx)
   pairs,delta=rationalize(root,idx,w,d,v,qs,T)
   mask=sum(1<<k for k,z in pairs);certs.append([root,pairs,str(delta)])
   rem=[(r,s) for r,s in rem if s&mask!=mask];n+=1
  print('ROOT_BUILT',root,n,flush=True)
 payload={'object':'WILLOW_H5_W_ONLY_ROOT_COVER_V1','theta':serial(THETA),'g':serial(B['g']),
          'volume':str(B['D']/6),'gauge':[1,2,1],'global_control':global_mode,'certificates':certs}
 raw=(json.dumps(payload,sort_keys=True,separators=(',',':'))+'\n').encode();certificate_file(global_mode).write_bytes(raw)
 check(global_mode)

def check(global_mode=False):
 B=geometry();assert B['D']/6==Q(881291,9600000)
 assert B['g']==(Q(7368835529,28201312000),Q(3427883561,28201312000),Q(50317,153268))
 v,qs,ar,T=tables(B);alltrees=trees(B['edges']);path=certificate_file(global_mode);raw=path.read_bytes();payload=json.loads(raw)
 assert payload['theta']==serial(THETA) and payload['g']==serial(B['g']) and payload['gauge']==[1,2,1] and payload['global_control']==global_mode
 roots=[None] if global_mode else list(range(9));counts={r:0 for r in roots};indef={r:0 for r in roots};masks={r:[] for r in roots};minimum=None;blocks=0;hist={}
 for root,pairs,d in payload['certificates']:
  assert root in roots;pairs=tuple((int(k),int(w)) for k,w in pairs);delta=Q(d)
  assert len({k for k,w in pairs})==len(pairs) and all(0<=k<34 for k,w in pairs)
  A,ls=accept(root,pairs,delta,v,qs,T);counts[root]+=1;blocks+=len(ls) if ls else 1
  if not psd(times(-1,A)):
   assert det(A)>0 and tr(A)<0;indef[root]+=1
  hist[len(pairs)]=hist.get(len(pairs),0)+1
  normalized=delta/sum(w for k,w in pairs);minimum=normalized if minimum is None else min(minimum,normalized)
  masks[root].append(sum(1<<k for k,w in pairs))
 for root in roots:
  for r,mask in alltrees:assert any(mask&m==m for m in masks[root]),('uncovered actual tree',root,r,mask)
 report={'object':payload['object'],'global_control':global_mode,'geometry':{'volume':B['D']/6,'centroid':B['g'],'edges':B['edges'],'faces':FACES},
         'unrooted_trees':4879,'rooted_trees':48790,'root_tree_cases':48790*len(roots),'counts':counts,'indefinite_counts':indef,
         'support_histogram':hist,'psd_blocks':blocks,'all_principal_minors_checked':7*blocks,'minimum_delta_per_weight':minimum,
         'certificate_bytes':len(raw),'certificate_sha256':hashlib.sha256(raw).hexdigest()}
 out=Path('willow_global_report.json' if global_mode else 'willow_root_report.json');out.write_text(json.dumps(serial(report),sort_keys=True,indent=2)+'\n')
 print(json.dumps(serial(report),sort_keys=True))
 print('WILLOW_GLOBAL_PSD_CONTROL_PASS' if global_mode else 'WILLOW_ALL_9_ROOTS_439110_CLOSED_ROOT_CASES_PASS')

if __name__=='__main__':
 if not __debug__:raise RuntimeError('Assertions must remain enabled')
 command=sys.argv[1] if len(sys.argv)>1 else 'check'
 if command in ('build','global'):build(command=='global')
 elif command in ('check','global-check'):check(command=='global-check')
 else:raise SystemExit('Use build, check, global, or global-check')
```

### willow_root_region.py

```python
#!/usr/bin/env python3
"""Exact moving-centroid H5 root-packet box; imports the complete companion.
python -B willow_root_region.py       # wide taper [1/20,1/4]
python -B willow_root_region.py inner # stronger margin on [3/25,9/50]
"""
import sympy as S
from itertools import combinations, product
from fractions import Fraction as Q
from math import comb, gcd, lcm
import json,hashlib,sys
from pathlib import Path
import willow_root_cover as W
R=S.Rational
BOX=((R(1,100),R(79,100)),(R(89,100),R(91,100)),(R(1,100),R(7,20)),(R(29,50),R(31,50)),(R(1,20),R(1,4)))
ROOT=2;ARROWS=((7,0),(4,9),(9,7));WEIGHTS=(4,5,2);LAM=(R(9,2),R(10),R(7,2));DELTA=R(1,2000)

def symbolic():
 x,r,p,q,la=S.symbols('x r p q la');var=(x,r,p,q,la);s=1-la
 b=((R(1,4),0),(1-3*x/4,0),(1-p,p),(q,1-q),(0,1-3*r/4),(0,R(1,4)),(R(1,16),R(1,16)))
 z=tuple(S.Matrix((s*a,s*b,0)) for a,b in b)+(S.Matrix((0,0,1)),S.Matrix((la,0,1)),S.Matrix((0,la,1)))
 area=(31-24*x*p-24*r*q)/64
 bx=R(509,3072)-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8
 by=R(509,3072)-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
 D=la+2*area*s*s
 K=S.Matrix((3*s**3*bx/2+s*s*la*(1-3*x*p/4)/4+la*la/4,
             3*s**3*by/2+s*s*la*(1-3*r*q/4)/4+la*la/4,
             area*s*s/2+la/2+la*la/4))
 dd=S.S(0);kk=S.zeros(3,1)
 for f in W.FACES:
  a=z[f[0]]
  for j in range(1,len(f)-1):
   b,c=z[f[j]],z[f[j+1]];d=a.dot(b.cross(c));dd+=d;kk+=d*(a+b+c)/4
 assert S.expand(dd-D)==0 and all(S.expand(t)==0 for t in kk-K)
 planar=(((0,-1),0,0,1),((p,p-3*x/4),s*p*(1-3*x/4),la*p,3),((1,1),s,la,4),
         ((q-3*r/4,q),s*q*(1-3*r/4),la*q,5),((-1,0),0,0,6),((-3,-1),-s/4,0,7),((-1,-3),-s/4,0,2))
 ns=[None]*9;hs=[None]*9;ns[0]=S.Matrix((0,0,-1));hs[0]=S.S(0);ns[8]=S.Matrix((0,0,1));hs[8]=S.S(1)
 for n,h,t,f in planar:ns[f]=S.Matrix((*n,h-t));hs[f]=h
 for f in range(9):
  for i in W.FACES[f]:assert S.expand(hs[f]-ns[f].dot(z[i]))==0
 return var,z,D,K,ns,hs

def tensor_bernstein(expressions,var,box):
 """Integer scaled tensor Bernstein coefficients; one positive scale for all entries."""
 pol=[S.Poly(S.expand(e),*var,domain=S.QQ) for e in expressions]
 deg=tuple(max(P.degree(v) if P else 0 for P in pol) for v in var)
 deg=tuple(max(0,int(n)) for n in deg)
 den=1
 for P in pol:
  for c in P.coeffs():den=lcm(den,int(c.q))
 a={powers+(i,):int(c*den) for i,P in enumerate(pol) for powers,c in P.terms() if c}
 factor=den
 for axis,(n,(lo,hi)) in enumerate(zip(deg,box)):
  lo,hi=Q(lo),Q(hi);width=hi-lo
  mat=[[sum((Q(comb(j,k)*comb(i,k),comb(n,k))*lo**(j-k)*width**k for k in range(min(i,j)+1)),Q(0)) for j in range(n+1)] for i in range(n+1)]
  den=1
  for row in mat:
   for c in row:den=lcm(den,c.denominator)
  mat=[[int(c*den) for c in row] for row in mat];factor*=den;out={}
  for key,c in a.items():
   j=key[axis]
   for i in range(n+1):
    d=mat[i][j]
    if d:
     k=key[:axis]+(i,)+key[axis+1:];out[k]=out.get(k,0)+c*d
  a=out
 return deg,a,factor

def bisect_tensor(a,deg,axis):
 n=deg[axis];left={};right={}
 other=[i for i in range(5) if i!=axis]
 for rest in product(*(range(deg[i]+1) for i in other)):
  key=[0]*5
  for i,v in zip(other,rest):key[i]=v
  row=[]
  for j in range(n+1):key[axis]=j;row.append(a.get(tuple(key)+(0,),0))
  for i in range(n+1):
   key[axis]=i;k=tuple(key)+(0,)
   left[k]=sum(comb(i,j)*row[j] for j in range(i+1))*2**(n-i)
   right[k]=sum(comb(n-i,j)*row[i+j] for j in range(n-i+1))*2**i
 return left,right,2**n

def curvature_axis(a,deg):
 scores=[]
 for axis,n in enumerate(deg):
  if n<2:scores.append(0);continue
  best=0
  for t in product(*(range(d+1) for d in deg)):
   if t[axis]>n-2:continue
   u=list(t);u[axis]+=1;v=list(t);v[axis]+=2
   best=max(best,(n*(n-1))*(a.get(tuple(v)+(0,),0)-2*a.get(tuple(u)+(0,),0)+a.get(t+(0,),0)))
  scores.append(best)
 assert max(scores)>0,('nonpositive multi-affine endpoint',scores)
 return scores.index(max(scores))

def scalar_certificate(name,expr,var,box,strict=True):
 deg,a,scale=tensor_bernstein([expr],var,box);todo=[(a,scale,box,0)];leaves=[];nodes=0
 while todo:
  a,scale,bb,depth=todo.pop();nodes+=1
  vals=[a.get(t+(0,),0) for t in product(*(range(d+1) for d in deg))]
  if min(vals)>0 or (not strict and min(vals)>=0):
   leaves.append({'box':[[str(u),str(v)] for u,v in bb],'minimum':str(Q(min(vals),scale))});continue
  assert depth<24 and nodes<50000,(name,'unclosed Bernstein scalar',depth,min(vals))
  axis=curvature_axis(a,deg);left,right,factor=bisect_tensor(a,deg,axis)
  l,h=bb[axis];mid=(l+h)/2;b0=list(bb);b1=list(bb);b0[axis]=(l,mid);b1[axis]=(mid,h)
  todo.append((right,scale*factor,tuple(b1),depth+1));todo.append((left,scale*factor,tuple(b0),depth+1))
 return {'name':name,'degrees':deg,'coefficients_per_leaf':len(vals),'nodes':nodes,'leaves':leaves}

def matrix_certificate(name,P,var,box):
 deg,a,scale=tensor_bernstein(list(P),var,box);count=0;mins=None
 for t in product(*(range(d+1) for d in deg)):
  A=tuple(tuple(a.get(t+(3*i+j,),0) for j in range(3)) for i in range(3))
  assert A==W.transpose(A)
  minors=W.minors(A)
  if min(minors)<=0:
   print('FAILED_MATRIX_COEFFICIENT',name,deg,t,flush=True)
   raise ArithmeticError((name,t))
  count+=1
  normalized=tuple(Q(v,scale**(1 if k<3 else 2 if k<6 else 3)) for k,v in enumerate(minors))
  mins=normalized if mins is None else tuple(min(x,y) for x,y in zip(mins,normalized))
 return {'name':name,'degrees':deg,'matrices':count,'principal_minors':7*count,'minimum_principal_minors':list(map(str,mins))}

def physical_control(B,M,arrows):
 assert min(W.minors(M))>0;N=W.inv(M);assert W.mm(M,N)==W.I
 dp={(i,j):W.dot(B['v'][i],W.mv(M,W.sub(B['v'][j],B['v'][i]))) for e in B['edges'] for i,j in (e,e[::-1])}
 dual=tuple(sorted(tuple(sorted(fs)) for fs in B['ef'].values()))
 dq={(i,j):W.dot(B['q'][i],W.mv(N,W.sub(B['q'][j],B['q'][i]))) for e in dual for i,j in (e,e[::-1])}
 assert len(dp)==len(dq)==34 and min(dp[e] for e in arrows)>0 and all(dp.values()) and all(dq.values())
 uu=[i for i in range(10) if all(d<0 for (a,b),d in dp.items() if a==i)]
 ss=[i for i in range(9) if all(d<0 for (a,b),d in dq.items() if a==i)]
 hh=[e for e in B['edges'] if max(dp[e],dp[e[::-1]],dq[tuple(B['ef'][e])],dq[tuple(B['ef'][e][::-1])])<0]
 assert len(ss)+len(uu)-len(hh)==2
 return {'M':W.serial(M),'N':W.serial(N),'arrows':W.serial([dp[e] for e in arrows]),'S':ss,'U':uu,'H':hh,'zero_primitives':0,
         'all_primal_rows':[[i,j,str(d)] for (i,j),d in dp.items()],'all_polar_rows':[[i,j,str(d)] for (i,j),d in dq.items()]}

def main():
 global BOX,DELTA
 inner=len(sys.argv)>1 and sys.argv[1]=='inner'
 assert len(sys.argv)==1 or (len(sys.argv)==2 and inner)
 if inner:BOX=BOX[:4]+((R(3,25),R(9,50)),);DELTA=R(1,1000)
 assert S.__version__=='1.14.0' and __debug__
 var,z,D,K,ns,hs=symbolic();RR=tuple(D*a-K for a in z)
 U=S.zeros(3)
 for w,(i,j) in zip(WEIGHTS,ARROWS):
  e=z[j]-z[i];U+=w*(RR[i]*e.T+e*RR[i].T)/2
 report={'object':'WILLOW_ROOT2_THREE_ARROW_BOX_V1','box':[[str(a),str(b)] for a,b in BOX],
         'root':ROOT,'arrows':ARROWS,'weights':WEIGHTS,'edge_multipliers':list(map(str,LAM)),'delta':str(DELTA),'certificates':[]}
 cert=report['certificates']
 cert.append(scalar_certificate('six_volume',D,var,BOX))
 for f in range(9):
  cert.append(scalar_certificate('centred_height_'+str(f),D*hs[f]-ns[f].dot(K),var,BOX))
  for i in range(10):
   if i not in W.FACES[f]:cert.append(scalar_certificate('support_%d_%d'%(f,i),hs[f]-ns[f].dot(z[i]),var,BOX))
 # True cyclic corners and exposed vertex intersections, uniformly on the box.
 for f,face in enumerate(W.FACES):
  for a,b,c in zip(face,face[1:]+face[:1],face[2:]+face[:2]):
   cert.append(scalar_certificate('corner_%d_%d'%(f,b),ns[f].dot((z[b]-z[a]).cross(z[c]-z[b])),var,BOX))
 midpoint=dict(zip(var,[(a+b)/2 for a,b in BOX]))
 for i in range(10):
  incident=[f for f in range(9) if i in W.FACES[f]];done=False
  for triple in combinations(incident,3):
   expr=S.Matrix.hstack(*(ns[f] for f in triple)).det();sgn=S.sign(expr.subs(midpoint))
   if not sgn:continue
   try:cc=scalar_certificate('vertex_rank_'+str(i),sgn*expr,var,BOX)
   except AssertionError:continue
   cert.append(cc);done=True;break
  assert done,('vertex rank not certified',i)
 # Every supporting triple is either cofacial or has two uniformly opposite witness signs.
 midpoint=dict(zip(var,[(a+b)/2 for a,b in BOX]))
 triple_checks=0
 for tri in combinations(range(10),3):
  if any(set(tri)<=set(f) for f in W.FACES):continue
  i,j,k=tri;n=(z[j]-z[i]).cross(z[k]-z[i]);vals=[S.expand(n.dot(a-z[i])) for a in z]
  found=[]
  for sign in (1,-1):
   candidates=sorted(range(10),key=lambda a:float(sign*vals[a].subs(midpoint)),reverse=True)
   for a in candidates:
    if sign*vals[a].subs(midpoint)<=0:break
    try:cc=scalar_certificate('triple_'+str(tri)+'_'+str(sign),sign*vals[a],var,BOX)
    except AssertionError:continue
    found.append((a,cc));break
  assert len(found)==2,('unclosed nonfacet triple',tri)
  triple_checks+=1
 report['nonfacet_triples_with_exact_opposite_sign_witnesses']=triple_checks
 n=ns[ROOT]
 cert.append(scalar_certificate('root_normal',-(n.T*(U+DELTA*D*S.eye(3))*n)[0],var,BOX))
 f=W.FACES[ROOT]
 for lam,i,j in zip(LAM,f,f[1:]+f[:1]):
  P=lam*(RR[i]*RR[j].T+RR[j]*RR[i].T)/2-D*U-DELTA*D**2*S.eye(3)
  print('CHECKING_EDGE',i,j,flush=True)
  boxes=[BOX] if inner or (i,j)==(6,0) else [BOX[:4]+((R(1,20),R(3,20)),),BOX[:4]+((R(3,20),R(1,4)),)]
  for k,box in enumerate(boxes):
   name='edge_%d_%d'%(i,j)+(('_taper'+str(k)) if len(boxes)>1 else '')
   cert.append(matrix_certificate(name,P,var,box))
 # Strict physical controls, always with the actual inverse of M.
 B=W.geometry()
 M=((Q(233,500),Q(907,1000),Q(27,250)),(Q(907,1000),Q(1993,1000),Q(32,125)),(Q(27,250),Q(32,125),Q(9,250)))
 control=physical_control(B,M,ARROWS)
 assert control['S']==[0,4] and control['U']==[3,6] and control['H']==[(0,1),(3,9)]
 A=W.ZERO
 for w,(i,j) in zip(WEIGHTS,ARROWS):A=W.plus(A,W.times(w,W.sym(B['v'][i],W.sub(B['v'][j],B['v'][i]))))
 assert W.det(A)>0 and W.tr(A)<0
 control.update(stress_det=str(W.det(A)),stress_trace=str(W.tr(A)))
 report['strict_primal_control']=control
 # Rank-two reference is essential to a positive-margin search for this packet.
 C=((Q(1),Q(0),Q(0)),(Q(0),Q(1),Q(0)),(Q(0),Q(0),Q(0)))
 A=W.plus(W.times(2,W.sym(B['v'][1],W.sub(B['v'][0],B['v'][1]))),W.times(3,W.sym(B['v'][3],W.sub(B['v'][2],B['v'][3]))))
 q=B['q'][8];assert W.quad(q,A)==0 and W.quad(q,C)==0 and W.psd(C) and W.tr(C)==2
 lams=(Q(8),Q(9,2),Q(13,4));pmn=[]
 for lam,i,j in zip(lams,(7,8,9),(8,9,7)):
  L=W.plus(W.plus(W.times(lam,W.sym(B['v'][i],B['v'][j])),W.times(-1,A)),W.times(-Q(1,100),C))
  mins=W.minors(L);assert min(mins)>0;pmn.append(mins)
 M2=((Q(3,100),Q(7,100),Q(1,10)),(Q(7,100),Q(23,50),Q(29,50)),(Q(1,10),Q(29,50),Q(43,50)))
 second=physical_control(B,M2,((1,0),(3,2)))
 assert second['S']==[1,2,4,5,7] and second['U']==[0,9] and second['H']==[(0,7),(1,8),(3,9),(4,9),(6,7)]
 report['tangent_boundary_packet']={'root':8,'arrows':[(1,0),(3,2)],'weights':[2,3],'C':W.serial(C),'delta':'1/100','multipliers':W.serial(lams),'all_principal_minors':W.serial(pmn),'qAq':'0','physical_control':second}
 report['region_scope']='The three displayed weak arrows are excluded whenever the physical foot of true facet 2 lies in its CLOSED triangle. This is not all root choices throughout the box.'
 raw=(json.dumps(W.serial(report),sort_keys=True,indent=2)+'\n').encode();path=Path('willow_region_report.json' if inner else 'willow_taper_report.json');path.write_bytes(raw)
 print(path.name,len(raw),hashlib.sha256(raw).hexdigest())
 print('WILLOW_TRUE_CENTROID_ROOT2_FIVE_PARAMETER_BOX_PASS' if inner else 'WILLOW_TRUE_CENTROID_ROOT2_WIDE_TAPER_BOX_PASS')
if __name__=='__main__':main()
```

### willow_root_diagnostics.py

```python
#!/usr/bin/env python3
"""Reproduce strict primal packet locators, a failed novelty test, and tree overlap.
Numerical discovery is not acceptance. Exact Fraction checks accept each output.
OPENBLAS_NUM_THREADS=1 python -B willow_root_diagnostics.py
"""
from itertools import product
from collections import Counter
from fractions import Fraction as Q
import hashlib,json
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import linprog
import willow_root_cover as W
assert np.__version__=='2.3.5' and scipy.__version__=='1.17.0' and __debug__
B=W.geometry();v,qs,ar,T=W.tables(B);TT=np.array(T,float)
BASIS=[]
for i,j in ((0,0),(1,1),(2,2),(0,1),(0,2),(1,2)):
 A=np.zeros((3,3));A[i,j]=1;A[j,i]=1;BASIS.append(A)
BASIS=np.array(BASIS)

def locate(packet,den):
 idx=[ar.index(e) for e in packet];rows=[]
 for k in idx:
  row=np.zeros(7);row[:6]=-np.einsum('ij,aij->a',TT[k],BASIS);row[-1]=1;rows.append(row)
 def cut(d):
  row=np.zeros(7);row[:6]=-np.einsum('i,aij,j->a',d,BASIS,d);row[-1]=1;return row
 for d in product((-1,0,1),repeat=3):
  if any(d):rows.append(cut(np.array(d)/np.linalg.norm(d)))
 eq=np.zeros((1,7));eq[0,:3]=1
 for iteration in range(100):
  res=linprog([0]*6+[-1],A_ub=rows,b_ub=np.zeros(len(rows)),A_eq=eq,b_eq=[1],bounds=[(None,None)]*7,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
  assert res.success and res.x[-1]>1e-8,(packet,res.message)
  M=np.einsum('a,aij->ij',res.x[:6],BASIS);ev,vec=np.linalg.eigh(M)
  if ev[0]>=res.x[-1]-1e-8:break
  rows.append(cut(vec[:,0]))
 else:raise ArithmeticError('Packet locator did not converge')
 L=np.diag((1,2,1));raw=L@M@L
 exact=tuple(tuple(Q(round(float(x)*den),den) for x in row) for row in raw)
 assert min(W.minors(exact))>0
 vals=[W.dot(B['v'][i],W.mv(exact,W.sub(B['v'][j],B['v'][i]))) for i,j in packet]
 assert min(vals)>0
 return {'packet':packet,'denominator':den,'M':W.serial(exact),'positive_arrows':W.serial(vals),'iterations':iteration+1}

report={'object':'WILLOW_ROOT_DIAGNOSTICS_V1','physical_locators':[locate(((7,0),(4,9),(9,7)),1000),locate(((1,0),(3,2)),100)]}
assert report['physical_locators'][0]['M']==W.serial(((Q(233,500),Q(907,1000),Q(27,250)),(Q(907,1000),Q(1993,1000),Q(32,125)),(Q(27,250),Q(32,125),Q(9,250))))
assert report['physical_locators'][1]['M']==W.serial(((Q(3,100),Q(7,100),Q(1,10)),(Q(7,100),Q(23,50),Q(29,50)),(Q(1,10),Q(29,50),Q(43,50))))
# A candidate indefinite root-stress packet can already be globally impossible.
packet=((0,1),(1,8),(8,2));idx=[ar.index(e) for e in packet]
w,d=W.Locator(None,v,qs,T).solve(idx)
pairs,delta=W.rationalize(None,idx,w,d,v,qs,T)
A,lams=W.accept(None,pairs,delta,v,qs,T)
report['globally_excluded_candidate']={'packet':packet,'weights':[(ar[k],w) for k,w in pairs],'delta':str(delta),'all_psd_minors':W.serial(W.minors(W.times(-1,W.plus(A,W.times(delta,W.I)))))}
# Exact combinatorial overlap, not a registry delta and not a feasibility census.
mask=sum(1<<ar.index(e) for e in ((7,0),(4,9),(9,7)))
covered=[(r,m) for r,m in W.trees(B['edges']) if m&mask==mask]
degrees=Counter()
for r,m in covered:
 deg=sum(not (m>>ar.index((a,b))&1 or m>>ar.index((b,a))&1) for a,b in ((7,6),(6,0),(0,7)))
 degrees[deg]+=1
assert len(covered)==1212 and degrees=={1:970,2:242}
report['root2_packet_tree_coverage']={'total':len(covered),'primal_roots':dict(Counter(r for r,m in covered)),'complementary_dual_root_degrees':dict(degrees)}
# Independent exact global-control perturbation budget, in X=diag(1,2,1)z.
z=tuple(tuple(a[i]*(1,2,1)[i] for i in range(3)) for a in B['z'])
g=tuple(B['g'][i]*(1,2,1)[i] for i in range(3))
assert max(W.dot(a,a) for a in z)<Q(9,4) and W.dot(g,g)<1 and 2*B['D']>1
radius=Q(1,2**23)
assert 192*radius<Q(1,2) and 4620*radius<Q(1,1000)
report['same_lattice_refill_collar']={'gauge':[1,2,1],'matched_euclidean_radius':str(radius),'volume_change_coefficient':192,'first_moment_change_coefficient':384,'centroid_change_coefficient':1152,'centred_vertex_change_coefficient':1153,'arrow_change_coefficient':4620,'margin_used':'1/1000','hypothesis':'Requires the independently verified global certificate with minimum delta/weight > 1/1000, and the identical true maximal facet cycles.'}
raw=(json.dumps(W.serial(report),sort_keys=True,indent=2)+'\n').encode()
path=Path('willow_diagnostics_report.json');path.write_bytes(raw)
print(path.name,len(raw),hashlib.sha256(raw).hexdigest())
print('WILLOW_STRICT_PRIMAL_LOCATORS_AND_OVERLAP_PASS')
```

Convenience files: all sources and exact outputs (`willow_handoff.zip`), root locator/checker (`willow_root_cover.py`), regional verifier (`willow_root_region.py`), and diagnostics (`willow_root_diagnostics.py`). The complete inline source units are sufficient without these links.
