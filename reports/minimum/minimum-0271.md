# minimum-0271

AI research report · 2026-09-27 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# H5_FIVE_PARAMETER_FULL_DOMAIN_U2_V1
## Complete primal exclusion of the supplied five-parameter family, at every taper and every affine metric

### 1. Main theorem and exact scope

**The entire five-parameter family implemented by the supplied compact H5 core has U>=2 at its actual uniform-volume centroid under every SPD metric.** The restrictions to the W-only calibration, its small parameter box, a fixed shear, a fixed tangential metric, or a spectral window are removed.

More precisely, choose independently

```
0 < x < 1,   0 < r < 1,
p > 0,       q > 0,       p+q < 1,
rho > 0.
```

Let B be the heptagon whose counterclockwise vertices are

```
(1/4,0), (1-3x/4,0), (1-p,p), (q,1-q),
(0,1-3r/4), (0,1/4), (1/16,1/16),
```

and set

```
P = conv((B,0), (0,0,1), (rho,0,1), (0,rho,1)).
```

Then P, uniformly filled and centered at its own volume centroid, has **at least two proper unstable equilibria for every M>0**, with no restriction on additional weak contacts. Every nonsingular affine image has the same all-metric conclusion. In common-height notation, every shear v, every tangential G>0, and every eta>0 are allowed. W, A, R7, and gamma<=1/3 are not premises. In particular, no complete proper U1 system, and hence no joint S1/U1 system, exists anywhere in this family.

Geometrically, the base is a triangle with the two fixed origin-corner cuts `X+3Y>=1/4` and `3X+Y>=1/4`, and arbitrary nonoverlapping cuts at its other two corners. The upper triangle can have any positive size. Thus this is an all-taper, variable-cut-direction family theorem, not another small neighborhood.

**Scope boundary.** This closes the full five-parameter family of the supplied core. It does not close the full nine-affine-modulus parallel heptagon/triangle realization space, its eleven-modulus nonparallel extension, or all E17 incidences. The general chart allows independent basal parameters that remain fixed here. The notebook distinguishes those larger spaces explicitly. fileciteturn10file0L49-L55 No canonical incidence or root-orbit count is subtracted, and **34<=Cmin<=622 remains unchanged**. fileciteturn6file0L9-L11

### 2. Input authority and preserved checkpoint

The complete new journal was read through EOF: 325522 bytes, 1520 logical lines, SHA-256

```
307680fa061e437d79d00f7cd84f984442ea372597b5d898154d75be35b63eb4.
```

The required literal parent was read in full and its compact JSON envelope reconstructed at 35254 bytes:

```
minimum-0267
5a922d28cd755d0663a8a7a286ea0f8f56f38a0bdd5540c44c1f56a0220bcbae.
```

Earlier unchanged supplied sources and the readable parent builder remained available. No missing archival program is used. There is no unresolved source-identity or geometry conflict; the earlier open-calibration paragraphs are explicitly superseded by the accepted parent. fileciteturn12file0L48-L61

The parent's 671-row certificate is unchanged: 25502 bytes, SHA-256 `eb610ab904f7760da34492cee44348ea16699025805b678e84b8ae2c482f1115`. Its stronger local margin 2^-25 and local refill collar 2^-43 remain valid on its smaller box. The successor below has a much larger domain and a separately certified uniform margin; it is not a renamed parent certificate.

### 3. Compact actual geometry and moving volume moments

Set

```
lambda = rho/(1+rho),   s=1-lambda.
```

Apply the genuine affine map `diag(s,s,1)` to P. The compact raw vertices are

```
Z_i=(s B_i,0), i=0,...,6,
Z7=(0,0,1), Z8=(lambda,0,1), Z9=(0,lambda,1).
```

An arbitrary SPD metric before this map corresponds to an arbitrary SPD metric after it. The actual uniform centroid transforms by this affine map; it is not independently prescribed.

The true outward maximal facet cycles are

```
(6,5,4,3,2,1,0), (8,7,0,1), (7,6,0), (1,2,8),
(9,8,2,3), (9,3,4), (4,5,7,9), (6,7,5), (7,8,9).
```

The 17 true edges, in lexicographic order, are

```
01, 06, 07, 12, 18, 23, 28, 34, 39,
45, 49, 56, 57, 67, 78, 79, 89.
```

The checker proves 56 nonincident support inequalities and 19 corner-turn inequalities for the nontriangular facets. Their Bernstein coefficients are nonnegative on the closed parameter cube and at least one coefficient of each polynomial is positive; therefore every guard is strictly positive in the physical open domain. The 15 triangular corner expressions are identically the squared normal norm and are strictly positive there. Every listed face is consequently a maximal supporting polygon, with its displayed true boundary. The cycles form a closed connected sphere, every edge belongs to two faces, and `10-17+9=2`; there is no unfilled boundary to accommodate additional facets. Integration diagonals are never used as escape edges.

Write **D=6 Vol** and **J=6 integral Z**, so the actual centroid is `g=J/D`. The exact formulas are

```
A=(31-24*x*p-24*r*q)/64,
bx=509/3072-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8,
by=509/3072-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8,
D=lambda+2*A*s*s,
Jx=3*s**3*bx/2+s*s*lambda*(1-3*x*p/4)/4+lambda**2/4,
Jy=3*s**3*by/2+s*s*lambda*(1-3*r*q/4)/4+lambda**2/4,
Jz=A*s*s/2+lambda/2+lambda**2/4.
```

These identities are independently checked against all 16 oriented boundary integration triangles. No free fan or vertex masses occur.

To cover the complete p/q triangle, substitute

```
p=u*t,   q=(1-u)*t,
(x,r,u,t,lambda) in [0,1]^5.
```

The physical family is the open cube. Its closed boundary consists of full-dimensional indexed limits, sometimes with fewer true vertices or merged facets, not always genuine 10/17/9 bodies. The exact volume bound throughout the closed cube is

```
7/32 <= D <= 1.
```

Thus this compactification never loses three-dimensional volume. The 75 geometric guards and two volume bounds use 999 scalar Bernstein coefficients, 209 positive and the rest zero. A zero boundary coefficient is not discarded as an infeasible parameter cell.

### 4. Complete weak-tree exclusion

#### 4.1 Why every proper U1 body would supply one of the enumerated trees

Put `X_i=Z_i-g`. On a true directed edge `(i,j)`, let

```
d_ij(M)=X_i^T M(X_j-X_i).
```

A vertex is proper unstable precisely when all its genuine outgoing derivatives are strictly negative. Every other vertex has a genuine outgoing derivative that is nonnegative. For SPD M, even a zero derivative gives strict norm growth:

```
X_j^T M X_j-X_i^T M X_i
 =2*d_ij(M)+(X_j-X_i)^T M(X_j-X_i)>0.
```

A global norm maximum is proper unstable. Under U1, choosing one weak escape at every other vertex therefore yields a spanning tree directed to that sole root. This reasoning retains proper roots, weak arrows, norm ties, and incidental physical weak equilibria.

The source enumerates every nine-edge subset of the 17 true edges, retains exactly the connected ones, and roots each at all ten vertices. It obtains **4879 unrooted and 48790 labelled rooted trees**. An exact Laplacian cofactor independently verifies 4879. These are local labelled counts for this graph, not global registry counts.

#### 4.2 Exact actual-centroid tensors and one common stress per cell

For each directed true edge a=(i,j), define

```
Q_a=-sym(D*Z_i-J, Z_j-Z_i),
sym(v,w)=(v*w^T+w*v^T)/2.
```

The moving centroid is retained exactly, and

```
tr(M Q_a)=-D*d_ij(M).
```

After the cube substitution, all six independent matrix entries have tensor degree bounded by `(3,3,3,3,4)`. Their common tensor Bernstein grid has 1280 entries. The initial common integer denominator is **31850496**. The exact inverse Bernstein transform reconstructs all **261120** original coefficient entries, including zeros, before any certificate is accepted.

A certificate row assigns nonnegative integer multipliers w_a to genuine arrows; these are inequality multipliers, not physical masses. The **same weight vector** is used at every Bernstein coefficient of that cell. With `W=sum w_a` and

```
epsilon=2^-32=1/4294967296,
```

epsilon is a certificate margin, not an assumed eigenvalue floor for M. The checker proves, for every coefficient matrix of every applied row,

```
sum_a w_a Q_{a,coefficient} - W*epsilon*I > 0.
```

The inequalities are checked by exact integer leading principal minors of the symmetric 3x3 matrix. Midpoint de Casteljau subdivision is performed with common integer denominators; there is no floating-point sign acceptance.

Since Bernstein basis functions are nonnegative and sum to one, throughout the entire closed cell

```
sum_a w_a Q_a > W*epsilon*I.
```

Consequently, for every nonzero PSD M,

```
(sum_a w_a d_a(M))/W
 < -epsilon*tr(M)/D
 <= -epsilon*tr(M)<0.
```

Thus those arrows cannot all be weak escapes. The actual edge-energy terms remain in Q_a; a system of norm comparisons is not substituted for the arrow system.

#### 4.3 Exact reflection and exhaustive parameter/root coverage

The family has the involution

```
(x,r,u,t,lambda) -> (r,x,1-u,t,lambda),
vertex permutation (5,4,3,2,1,0,6,7,9,8),
physical coordinate map (X,Y,Z) -> (Y,X,Z).
```

The source checks the raw vertices, D, J, all directed-edge labels, and a bijection of the complete 48790 rooted-tree set under this map. It is a true affine reflection of one uniformly filled body, not a new centering convention.

The complete directly certified quarter `lambda in [0,1/2], u in [0,1/2]`, with all x,r,t, reflects to the complementary u-quarter. This replaces exactly one quarter of the cube by an exact theorem transport. The upper lambda half is independently covered. Reflection includes the shared boundaries.

At each direct certificate node, a row removes only rooted trees containing its forbidden support. Every remaining tree is passed to **both closed children**. A leaf is accepted only when none remain. A reflected leaf is accepted only after the entire source quarter has been checked. The checker rejects omitted children, incorrect remaining-tree counts, unused/orphan nodes, or any failed minor. The accepted dyadic parameter-cell volumes sum exactly to one; this is parameter-space coverage, not physical body volume.

The observed complete certificate has

| Exact item | Count |
|---|---:|
| Distinct integer stress rows | 26278 |
| Nonzero integer weights | 162674 |
| Maximum weight | 100000 |
| Binary cover nodes | 297 |
| Closed leaves, including one reflected quarter | 149 |
| Maximum subdivision depth | 16 |
| Stress applications | 117401 |
| Positive-definite Bernstein coefficient checks | 150273280 |
| Strictly positive leading-minor checks | 450819840 |
| Missing cells or rooted-tree alternatives | 0 |

Supports have three through nine arrows. The coefficients/checks are counted as executed applications, not asserted to be distinct matrices or canonical classes. Exact rational minimum leading minors among the explicitly checked shifted coefficient matrices are

```
5255559/536870912,
24977648817537737/41505174165846491136,
2712847063182187772834752139/19252443490966234035231179931648.
```

The finite computation proves the asserted weak-tree infeasibility even for nonzero PSD M. The norm-growth argument then proves the physical U>=2 theorem for SPD M. It does not assign a physical equilibrium census to a singular metric.

### 5. Actual controls, an old-stress exit, and a secondary refill collar

#### 5.1 Three exact, unbounded-metric nonwinners

Let

```
u=(1,3,-2),  v=(3,-1,0),  w=(-1,-3,-5),
M_L=L^2*u*u^T+L*v*v^T+w*w^T.
```

The three vectors are orthogonal, with squared norms 14,10,35. The literal inverse satisfies

```
L^2*N_L=u*u^T/14^2+L*v*v^T/10^2+L^2*w*w^T/35^2,
M_L*N_L=I.
```

For each following compact-coordinate body, every L in the indicated entire ray has own strict `(S,U,H)=(2,2,2)`, physical weak000, and all 68 primitives nonzero:

| theta=(x,r,p,q,lambda) | L range | S facets | U vertices | H edges |
|---|---|---|---|---|
| (19/20,17/20,13/20,3/10,1/40) | L>=512 | 0,4 | 3,7 | 12,49 |
| (3/20,4/5,3/5,3/10,3/10) | L>=128 | 2,4 | 3,7 | 18,49 |
| (49/50,1/25,1/100,49/50,7/8) | L>=256 | 1,8 | 7,9 | 28,79 |

Their exact volumes are respectively

```
829063/15360000, 52273/480000, 14233/96000,
```

and their actual centroid heights are

```
894663/3316252, 6421/16084, 40483/56932.
```

The source reconstructs both horizontal centroid coordinates, actual covariance, all poles at that same origin, and every primitive polynomial. After substituting `L=L_min+z`, z>=0, the constant coefficient is strictly signed and the other coefficients have the same sign or are zero. This proves the **entire ray**, not three sampled metrics. The polar rows are multiplied only by the common positive scalar L^2. The condition number of M_L in the displayed raw frame is exactly `2*L^2/5`, so no conditioning cutoff is hidden in either the theorem or these controls.

These controls show U>=2 is sharp as a uniform conclusion for the family. They are not U1 or own110 attainers.

#### 5.2 A genuine physical countercontrol to extrapolating the old row library

On the first control, the parent's zero-based row 94 is

```
8*d_01 + 49*d_18 + 100*d_32 + 88*d_43.
```

For L=512+z, z>=0, it is exactly

```
(120502905263359418873
 +471068629445597417*z
 +460359102261497*z^2)/6791684096000 > 0.
```

Thus that old forbidden-support stress does not transport unchanged to this actual body, even though the full body remains own222. This is a physical failure of a proposed uniform old-row extrapolation, not a counterexample to the correctly scoped parent theorem. It does not assert simultaneous feasibility of those four arrows. The new complete certificate uses other supports/weights rather than assembling separately passing ports.

#### 5.3 Uniform true-refill collar of the whole compact family

As a secondary corollary, let an actual uniformly filled body P' have the displayed true maximal facet cycles and matched vertices satisfying

```
max_i ||Z'_i-Z_i||_2 <= 2^-50
```

for a compact reference configuration above. Then P', centered at its **newly integrated** volume centroid, also has U>=2 for every SPD metric. Nonparallel perturbations are allowed when the stated true cycles hold. This is not a whole nonparallel realization theorem; the main advance is the full five-parameter domain, not this thin collar.

The estimates are explicit. Reference vertex norms are below 2; for perturbation delta<=1, new norms are below 3. For the same 16 boundary triangles, determinant telescoping gives

```
|D'-D|<=304*delta,   ||J'-J||<=780*delta.
```

Indeed each determinant changes by at most `(4+6+9)delta`, and each triangle's first moment by at most `(19*6+27*3)delta/4`. At delta=2^-50, `D'>7/64`; hence

```
||g'-g|| <= (64/7)*(780+2*304)*delta <12800*delta,
max_i ||X'_i-X_i|| <12801*delta.
```

Writing d=12801*delta<1, each true arrow tensor changes by at most `12d+2d^2<=14d`, hence by less than `179214*delta<2^-32`. Every normalized positive-definite stress remains positive definite. The complete tree cover is unchanged. The proof uses actual volume refill, not a frozen centroid. The old parent's larger local collar is not replaced by this smaller but uniformly applicable one.

### 6. What was tried and what the result does not claim

The useful change was to stop extending isolated ports and to keep **all original primal arrows with the exact moving centroid**. I converted their complete five-variable polynomials to common matrix Bernstein form, located positive stresses by eigenvector-cut linear programs, and recursively subdivided only when that common coefficient stress was not found. A support certified on a node excludes every tree containing it throughout that node; only the true remaining alternatives are sent to both children. Exact geometric reflection removes one redundant quarter of the parameter space.

The numerical locator made 46864 calls. Its failures only caused subdivision and never accepted an exclusion. The proof is the complete rational coefficient/minor and rooted-tree verification described above. No numerical near-U1 point, failed LP, separately passing root fan, or relaxed determinant lift is promoted to a physical survivor.

No polar feasibility problem needs to be solved inside this family: the complete primal U1 premise is already impossible. Outside the stated family, no full U1 or inverse-compatible survivor is asserted, and no global H5/E17 decision follows. The proof also does not assert S>=2 for every metric; the S2 statements above concern the explicitly audited controls.

Observed executions completed: the exploratory build and its exact verification; a separate fresh-directory exact check using the source and certificate; and an independent no-resume build starting from an empty certificate state, followed by its complete exact verification. The no-resume run regenerated the same certificate and report byte-for-byte. The exploratory build was resumed once, but no checkpoint is required by the complete source-only recovery. The two readable code blocks were also extracted from this Markdown and matched their source pins. These are observed author executions, not a claimed coordinator replay, peer review, or proof-assistant formalization.

### 7. Complete deterministic recovery

The two complete readable source blocks below are the durable recovery. The first regenerates the full certificate from scratch, verifies it exactly, reconstructs the actual geometry, and audits the three infinite metric rays. It reads no external source, old certificate, cached tensor array, or random seed. The optional H5_RESUME environment variable is only for resuming discovery; **leave it unset for source-only recovery**.

Observed environment: CPython 3.13.5, SymPy 1.14.0, NumPy 2.3.5; discovery additionally SciPy 1.17.0 with single-thread OpenBLAS 0.3.30, pthreads, Linux x86_64 (SkylakeX). All nondefault parameters, tolerances, integer rounding denominators, tree orders, subdivision budgets, and exact inputs are in the source. Exact checking uses integer/rational arithmetic and invokes no numerical optimizer. Numerical discovery is deterministic in the recorded stack; exact acceptance never depends on trusting its floating-point signs.

Save the blocks as `h5_full_domain.py` and `h5_stress_exit_and_collar.py`, in the same directory, and run with assertions enabled:

```
env -u H5_RESUME OPENBLAS_NUM_THREADS=1 python -B h5_full_domain.py build exact_h5
OPENBLAS_NUM_THREADS=1 python -B h5_full_domain.py check exact_h5/certificate.json
OPENBLAS_NUM_THREADS=1 python -B h5_stress_exit_and_collar.py > stress_exit_and_collar.out
```

Expected terminal markers:

```
H5_FIVE_PARAMETER_FULL_DOMAIN_U2_V1_ALL_48790_ROOTED_TREES_ALL_SPD_PASS
H5_STRESS_EXIT_AND_TRUE_REFILL_COLLAR_PASS
```

Exact pins:

| File | Bytes | SHA-256 |
|---|---:|---|
| h5_full_domain.py | 24778 | d0fcdca44d0be572fceb00c658e919ae31ae5fc21473b14bd2f9400d366bfd6d |
| certificate.json | 1958864 | 90f828f0dece4f5203ef96e25429f01438d791d7a102715e851e92c9a95e50f2 |
| report.json | 43379 | 2be6f6ad3bfedf94b918b468ff3df4bc7c8c334c7325b3eb4ce212b7d64bd471 |
| h5_stress_exit_and_collar.py | 1679 | fe39088ba9070febf6fb16b7eee95cc6014161f5aacf4bf5896ea1358dbbb7fe |
| stress_exit_and_collar.out | 725 | c23391f71718e210f8c2db1682a0ad8b118377d90d6dee1920bc597321f3a36c |

The full certificate is regenerated by the source; its hash is not offered in place of recovery. The source reports full coverage and refuses to promote a budget-limited or failed build. Convenience copies: [complete bundle](sandbox:/mnt/data/H5_FIVE_PARAMETER_FULL_DOMAIN_U2_V1.zip), [readable source](sandbox:/mnt/data/H5_FIVE_PARAMETER_FULL_DOMAIN_U2_V1/h5_full_domain.py), and [exact report](sandbox:/mnt/data/H5_FIVE_PARAMETER_FULL_DOMAIN_U2_V1/report.json).

#### Source 1: h5_full_domain.py

```python
#!/usr/bin/env python3
"""H5_FIVE_PARAMETER_FULL_DOMAIN_U2_V1: actual geometry, complete discovery/check.
Python 3.13.5, SymPy 1.14.0, NumPy 2.3.5. Discovery: SciPy 1.17.0.
Set OPENBLAS_NUM_THREADS=1. No external source, seed, or data is needed to build.
Assertions must be enabled. A numerical build is not accepted until exact check.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import hashlib
import itertools
import json
import math
import sys
import time
from fractions import Fraction
from itertools import combinations, product
from math import comb
from pathlib import Path
import numpy as np
import sympy as S
R=S.Rational
NAME='H5_FIVE_PARAMETER_FULL_DOMAIN_U2_V1'
PARENT='minimum-0267'
PARENT_SHA256='5a922d28cd755d0663a8a7a286ea0f8f56f38a0bdd5540c44c1f56a0220bcbae'
FACES = ((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
         (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
PAIRS = ((0,0),(0,1),(0,2),(1,1),(1,2),(2,2))
x,r,p,q,l = S.symbols('x r p q l')
VARS = (x,r,p,q,l)
s = 1-l
basal = ((R(1,4),0),(1-3*x/4,0),(1-p,p),(q,1-q),
         (0,1-3*r/4),(0,R(1,4)),(R(1,16),R(1,16)))
Z = tuple(S.Matrix((s*u,s*w,0)) for u,w in basal) + (
    S.Matrix((0,0,1)),S.Matrix((l,0,1)),S.Matrix((0,l,1)))
area = (31-24*x*p-24*r*q)/64
bx = R(509,3072)-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8
by = R(509,3072)-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
D = l+2*area*s*s
J = S.Matrix((3*s**3*bx/2+s*s*l*(1-3*x*p/4)/4+l*l/4,
              3*s**3*by/2+s*s*l*(1-3*r*q/4)/4+l*l/4,
              area*s*s/2+l/2+l*l/4))
EF = {}
for f,face in enumerate(FACES):
    for i,j in zip(face,face[1:]+face[:1]):
        EF.setdefault(tuple(sorted((i,j))),[]).append(f)
EDGES = tuple(sorted(EF))
ARROWS = tuple((i,j) for e in EDGES for i,j in (e,e[::-1]))
DUAL_EDGES = tuple(sorted(tuple(sorted(fs)) for fs in EF.values()))
DUAL = tuple((i,j) for e in DUAL_EDGES for i,j in (e,e[::-1]))
assert len(EDGES)==len(DUAL_EDGES)==17 and all(len(v)==2 for v in EF.values())

def sym(a,b):
    return (a*b.T+b*a.T)/2

def pd(A):
    return all(A[:i,:i].det()>0 for i in range(1,4))

def enc(a):
    if isinstance(a,S.MatrixBase): return [[enc(v) for v in row] for row in a.tolist()]
    if isinstance(a,S.Basic): return str(a)
    if isinstance(a,dict): return {str(k):enc(v) for k,v in a.items()}
    if isinstance(a,(list,tuple)): return [enc(v) for v in a]
    return a

def wire(a):
    return (json.dumps(enc(a),sort_keys=True,separators=(',',':'))+'\n').encode()

def sha(b):
    return hashlib.sha256(b).hexdigest()

def geometry(theta):
    sub = dict(zip(VARS,theta)); z = tuple(a.subs(sub) for a in Z)
    d = S.S(0); j = S.zeros(3,1); second = S.zeros(3); planes = []
    for face in FACES:
        a,b,c = (z[i] for i in face[:3]); n = (b-a).cross(c-a); h = n.dot(a)
        assert all(h-n.dot(v)==0 if i in face else h-n.dot(v)>0 for i,v in enumerate(z))
        planes.append((n,h))
        for k in range(1,len(face)-1):
            b,c = z[face[k]],z[face[k+1]]; dd = a.dot(b.cross(c)); sm = a+b+c
            d += dd; j += dd*sm/4
            second += dd*(sm*sm.T+a*a.T+b*b.T+c*c.T)/20
    assert d==D.subs(sub)>0 and j==J.subs(sub)
    g = j/d; cov = (second/d-g*g.T).applyfunc(S.factor); assert pd(cov)
    poles = tuple(n/(h-n.dot(g)) for n,h in planes)
    recovered = set()
    for i,j,k in combinations(range(10),3):
        n = (z[j]-z[i]).cross(z[k]-z[i])
        if n==S.zeros(3,1): continue
        vv = [n.dot(v-z[i]) for v in z]
        if max(vv)<=0 or min(vv)>=0: recovered.add(tuple(t for t,v in enumerate(vv) if v==0))
    assert recovered=={tuple(sorted(f)) for f in FACES}
    return dict(theta=theta,z=z,g=g,volume=d/6,covariance=cov,poles=poles)

def treepack():
    idx = {a:k for k,a in enumerate(ARROWS)}; out = []; count = 0
    for edges in combinations(EDGES,9):
        nb = [[] for _ in range(10)]
        for a,b in edges: nb[a].append(b); nb[b].append(a)
        seen = {0}; todo = [0]
        for a in todo:
            for b in nb[a]:
                if b not in seen: seen.add(b); todo.append(b)
        if len(seen)<10: continue
        count += 1
        for root in range(10):
            par = {root:root}; todo = [root]
            for a in todo:
                for b in nb[a]:
                    if b not in par: par[b]=a; todo.append(b)
            ids = tuple(sorted(idx[v,par[v]] for v in range(10) if v!=root))
            out.append((root,ids,sum(1<<k for k in ids)))
    lap = S.zeros(10)
    for i,j in EDGES: lap[i,i]+=1; lap[j,j]+=1; lap[i,j]-=1; lap[j,i]-=1
    assert lap[:9,:9].det()==count==4879 and len(out)==48790
    assert len({(r,m) for r,a,m in out})==48790
    return out

NS=(3,3,3,3,4); NN=np.prod([n+1 for n in NS]); EPS=2**-32

def polynomial():
 u,t=S.symbols('u t'); sub={p:u*t,q:(1-u)*t}; vv=(x,r,u,t,l)
 fs=[];den=1
 for i,j in ARROWS:
  mat=-sym(D*Z[i]-J,Z[j]-Z[i])
  vals=[]
  for a,b in PAIRS:
   po=S.Poly(S.expand(mat[a,b].subs(sub)),*vv)
   den=S.ilcm(den,*[c.q for e,c in po.terms()]); vals.append(po)
  fs.append(vals)
 shape=(34,6)+tuple(n+1 for n in NS); data=np.zeros(shape,dtype=object)
 for i,polys in enumerate(fs):
  for j,po in enumerate(polys):
   for e,c in po.terms():data[(i,j)+e]=int(c*den)
 for a,n in enumerate(NS):
  L=math.lcm(*[math.comb(n,k) for k in range(n+1)])
  T=np.array([[math.comb(i,k)*L//math.comb(n,k) if k<=i else 0 for k in range(n+1)] for i in range(n+1)],object)
  data=np.moveaxis(np.tensordot(T,data,axes=(1,2+a)),0,2+a);den*=L
 return data,int(den)

def matarray(data):
 # data = (34,6,4,4,4,4,5), to (34,1280,3,3)
 a=data.reshape(34,6,-1).transpose(0,2,1)
 out=np.empty((34,a.shape[1],3,3),dtype=data.dtype)
 for k,(i,j) in enumerate(PAIRS):out[:,:,i,j]=out[:,:,j,i]=a[:,:,k]
 return out

def split(data,axis):
 axis+=2;n=data.shape[axis]-1
 x=np.moveaxis(data,axis,-1)
 levels=[x]
 for k in range(n): levels.append((levels[-1][...,:-1]+levels[-1][...,1:])/2)
 left=np.stack([r[...,0] for r in levels],-1);right=np.stack([r[...,-1] for r in levels[::-1]],-1)
 return np.moveaxis(left,-1,axis),np.moveaxis(right,-1,axis)

def locate(aa,ids,eps=1e-9,maxiter=80):
 # all Bernstein coefficient matrices of one physical stress, common weights.
 A=aa[list(ids)].copy();scale=np.max(np.abs(A));A/=scale
 n=len(ids);nc=A.shape[1]
 vecs=np.array([(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,-1,0),(1,0,1),(1,0,-1),(0,1,1),(0,1,-1)],float)
 vecs/=np.linalg.norm(vecs,axis=1)[:,None]
 # retain corner/equidistant coefficient locations at first, add violated actual coefficients.
 cinds=np.unique(np.linspace(0,nc-1,min(16,nc)).astype(int))
 rows=np.einsum('vi,ncij,vj->cvn',vecs,A[:,cinds],vecs).reshape(-1,n)
 for it in range(maxiter):
  from scipy.optimize import linprog
  ans=linprog(np.r_[np.zeros(n),-1.],A_ub=np.c_[-rows,np.ones(len(rows))],b_ub=np.zeros(len(rows)),
   A_eq=[np.r_[np.ones(n),0]],b_eq=[1.],bounds=[(0,None)]*n+[(None,None)],method='highs')
  if not ans.success:return None,('LP_FAIL',ans.message)
  w=ans.x[:-1];d=ans.x[-1]
  if d<-eps:return None,('NO_COMMON_BERNSTEIN_STRESS',float(d),it)
  vals,axes=np.linalg.eigh(np.einsum('n,ncij->cij',w,A))
  if vals.min()>eps:
   for den in [100,1000,10000,100000,1000000]:
    wi=np.rint(w/w.max()*den).astype(int)
    if np.linalg.eigvalsh(np.einsum('n,ncij->cij',wi,A)).min()>wi.sum()*EPS/scale:
     return [(int(k),int(j)) for k,j in zip(ids,wi) if j],('LOCATED',it,float(vals.min()*scale))
  gap=d-vals[:,0]
  if gap.max()<eps:return None,('NUMERIC_TOUCH',float(vals.min()),it)
  sel=np.argsort(-gap)[:min(32,nc)]
  v=axes[sel,:,0];new=np.einsum('ci,ncij,cj->cn',v,A[:,sel],v)
  rows=np.concatenate((rows,new),axis=0)
 return None,('ITER_LIMIT',it)

def scalar_bernstein(f,variables):
 po=S.Poly(S.expand(f),*variables); ns=po.degree_list();ns=tuple(max(0,int(n)) for n in ns);den=1
 for e,c in po.terms():den=math.lcm(den,int(c.q))
 a=np.zeros(tuple(n+1 for n in ns),object)
 for e,c in po.terms():a[e]=int(c*den)
 for axis,n in enumerate(ns):
  L=math.lcm(*[math.comb(n,k) for k in range(n+1)])
  B=np.array([[math.comb(i,k)*L//math.comb(n,k) if k<=i else 0 for k in range(n+1)]for i in range(n+1)],object)
  a=np.moveaxis(np.tensordot(B,a,axes=(1,axis)),0,axis);den*=L
 return ns,a,int(den)

def build(outfile,exact,den,maxnodes=5000,maxdepth=24,resume=None):
 data=np.array(exact,float)/den
 trees=treepack(); masks=np.array([m for r,ids,m in trees],np.uint64)
 rows=[];rowindex={};nodes=[];uses=0;lpcount=0;done=0;start=time.time()
 corners=np.ravel_multi_index(np.array(list(itertools.product(*[(0,n) for n in NS]))).T,[n+1 for n in NS])
 presel=np.unique(np.r_[corners,np.arange(0,NN,max(1,NN//31))])
 todo=[('',0,data,np.arange(len(trees)),[(0.,1.)]*5)]
 bestfail=None
 if resume is not None:
  previous=json.loads(Path(resume).read_bytes())
  assert not previous['complete'] and '4021' in previous['frontier']
  rows=previous['rows'];rowindex={tuple(map(tuple,row)):i for i,row in enumerate(rows)}
  nodes=previous['nodes'];usednodes={n['path']:n for n in nodes}
  uses=sum(len(n['rows']) for n in nodes);done=sum(bool(n.get('leaf')) for n in nodes)
  lpcount=previous['lp_calls'];todo=[]
  for target in previous['frontier']:
   arr=data;left=np.arange(len(trees));box=[(0.,1.)]*5
   for depth in range(len(target)//2):
    ancestor=usednodes[target[:2*depth]]
    for ri in ancestor['rows']:
     mask=np.uint64(sum(1<<k for k,w in rows[ri]))
     left=left[(masks[left]&mask)!=mask]
    axis,child=map(int,target[2*depth:2*depth+2]);assert ancestor['split']==axis
    arr=split(arr,axis)[child];lo,hi=box[axis];mid=(lo+hi)/2
    box[axis]=(mid,hi) if child else (lo,mid)
   todo.append((target,len(target)//2,arr,left,box))
 while todo:
  path,depth,arr,left,box=todo.pop();ni=len(nodes)
  if ni>=maxnodes or depth>maxdepth:
   bestfail={'path':path,'box':box,'left':left.tolist(),'reason':'BUDGET'};break
  if path=='4021':
   # The COMPLETE preceding quarter has all x/r values. Reflect x<->r,
   # u<->1-u and the labelled true graph to cover this quarter without a grid.
   assert any(n['path']=='4020' for n in nodes)
   node={'path':path,'rows':[],'leaf':True,'reflection':'4020'}
   nodes.append(node);done+=1
   print('REFLECT',path,'FROM 4020',flush=True)
   rec={'object':'H5_FULL_CUBE_PRIMAL_V1','rows':rows,'nodes':nodes,
        'frontier':[p for p,d,a,l,b in todo],'complete':not todo,'lp_calls':lpcount}
   Path(outfile).write_text(json.dumps(rec,separators=(',',':'))+'\n')
   continue
  aa=matarray(arr);used=[]
  if rows:
   good=[]
   # cheap necessary positivity filter over corners and some other coefficients
   weights=np.zeros((len(rows),34))
   for ri,row in enumerate(rows):
    for k,w in row:weights[ri,k]=w
   vv=(weights@aa[:,presel].reshape(34,-1)).reshape(len(rows),len(presel),3,3)
   val=np.linalg.eigvalsh(vv)
   candid=np.where(val.min(axis=(1,2))>weights.sum(axis=1)*EPS)[0]
   for ri in candid:
    mask=np.uint64(sum(1<<k for k,w in rows[ri]))
    hit=(masks[left]&mask)==mask
    if not hit.any():continue
    B=np.einsum('n,ncij->cij',weights[ri],aa)
    if np.linalg.eigvalsh(B).min()>weights[ri].sum()*EPS:
     used.append(int(ri));left=left[~hit]
     if not len(left):break
  nfail=0;last=0;attempts=0
  while len(left):
   # consecutive failures try up to 12 spaced tree packets before subdivision
   idx=left[(nfail*193)%len(left)] if nfail else left[0]
   row,st=locate(aa,trees[idx][1]);lpcount+=1;attempts+=1
   if attempts%100==0:print("IN_NODE",ni,path,"LP",lpcount,"rows",len(rows),"left",len(left),"time",round(time.time()-start,2),flush=True)
   if row is None:
    nfail+=1;last=int(idx)
    if nfail>=12:break
    continue
   nfail=0
   key=tuple(map(tuple,row))
   if key not in rowindex:rowindex[key]=len(rows);rows.append(row)
   ri=rowindex[key];used.append(ri)
   mask=np.uint64(sum(1<<k for k,w in row));left=left[(masks[left]&mask)!=mask]
   if attempts>=300:break
  uses+=len(used)
  if not len(left):
   node={'path':path,'rows':used,'leaf':True};done+=1
  else:
   # split the dimension with greatest exact-Bernstein control variation.
   ids=trees[last][1]
   variations=[]
   for axis,n in enumerate(NS):
    delta=np.diff(arr[list(ids)],axis=axis+2)*n
    variations.append(np.max(np.abs(delta)))
   # Width already encoded in coefficients; avoid excessive depth in one dimension.
   axis=int(np.argmax(variations))
   a,b=split(arr,axis);b0=box.copy();b1=box.copy();lo,hi=box[axis];mid=(lo+hi)/2
   b0[axis]=(lo,mid);b1[axis]=(mid,hi)
   todo.append((path+str(axis)+'1',depth+1,b,left.copy(),b1));todo.append((path+str(axis)+'0',depth+1,a,left.copy(),b0))
   node={'path':path,'rows':used,'split':axis,'left':int(len(left))}
  nodes.append(node)
  if ni%1==0 or not todo:
   print('node',ni,'depth',depth,'open',len(todo),'leaves',done,'rows',len(rows),'uses',uses,'LP',lpcount,'left',len(left),'time',round(time.time()-start,2),flush=True)
   rec={'object':'H5_FULL_CUBE_PRIMAL_V1','rows':rows,'nodes':nodes,'frontier':[p for p,d,a,l,b in todo],'complete':not todo,'lp_calls':lpcount}
   Path(outfile).write_text(json.dumps(rec,separators=(',',':'))+'\n')
 rec={'object':'H5_FULL_CUBE_PRIMAL_V1','rows':rows,'nodes':nodes,'frontier':[p for p,d,a,l,b in todo],'complete':not todo and bestfail is None,'lp_calls':lpcount,'failed':bestfail}
 Path(outfile).write_text(json.dumps(rec,separators=(',',':'))+'\n')
 print('FINAL',len(nodes),len(rows),uses,done,rec['complete'],bestfail,flush=True)
 return rec
def split_exact(data,axis):
 axis+=2;n=data.shape[axis]-1;x=np.moveaxis(data,axis,-1);levels=[x]
 for k in range(n):levels.append(levels[-1][...,:-1]+levels[-1][...,1:])
 left=np.stack([row[...,0]*2**(n-k) for k,row in enumerate(levels)],-1)
 right=np.stack([row[...,-1]*2**(n-k) for k,row in list(enumerate(levels))[::-1]],-1)
 return np.moveaxis(left,-1,axis),np.moveaxis(right,-1,axis)

def verify(cert,data,den,partial=False):
 assert cert['complete'] or partial
 rows=cert['rows'];nodes={p['path']:p for p in cert['nodes']};assert len(nodes)==len(cert['nodes'])
 trees=treepack();masks=np.array([m for r,ids,m in trees],np.uint64)
 for row in rows:
  assert len({k for k,w in row})==len(row) and len(row)>0
  assert all(type(k)==type(w)==int and 0<=k<34 and w>0 for k,w in row)
 todo=[('',data,den,np.arange(48790),0)];seen=set();completed=set();uses=0;leaves=0;volume=Fraction(0);missing=[];reflections=[]
 start=time.time();mins=[None]*3
 while todo:
  path,arr,dd,left,depth=todo.pop()
  if arr is None:
   axis=nodes[path]['split']
   assert path+str(axis)+'0' in completed and path+str(axis)+'1' in completed
   completed.add(path);continue
  if path not in nodes:
   if partial:missing.append(path);continue
   raise ValueError('Missing closed child '+path)
  node=nodes[path];seen.add(path)
  if 'reflection' in node:
   assert path=='4021' and node['reflection']=='4020' and '4020' in completed
   assert not node['rows'] and node['leaf']
   reflections.append((path,node['reflection']));completed.add(path)
   leaves+=1;volume+=Fraction(1,2**depth);continue
  for ri in node['rows']:
   assert type(ri)==int and 0<=ri<len(rows)
   row=rows[ri];W=sum(w for k,w in row)
   Q=sum((w*arr[k] for k,w in row),np.zeros(arr.shape[1:],dtype=object)).reshape(6,-1)
   Q=Q*2**32;Q[[0,3,5]]-=W*dd
   a,b,c,d,e,f=Q
   m2=a*d-b*b;m3=a*d*f+2*b*c*e-a*e*e-d*c*c-f*b*b
   assert min(a)>0 and min(m2)>0 and min(m3)>0,(path,ri)
   for j,vec in enumerate((a,m2,m3)):
    mm=Fraction(int(min(vec)),(dd*2**32)**(j+1))
    mins[j]=mm if mins[j] is None else min(mins[j],mm)
   mask=np.uint64(sum(1<<k for k,w in row));hit=(masks[left]&mask)==mask
   assert hit.any(),('REDUNDANT',path,ri)
   left=left[~hit];uses+=1
  if node.get('leaf'):
   assert not len(left);leaves+=1;volume+=Fraction(1,2**depth);completed.add(path)
  else:
   assert len(left)==node['left']>0 and node['split'] in range(5)
   axis=node['split'];a,b=split_exact(arr,axis);den2=dd*2**NS[axis]
   todo.append((path,None,None,None,depth))
   todo.append((path+str(axis)+'1',b,den2,left.copy(),depth+1));todo.append((path+str(axis)+'0',a,den2,left.copy(),depth+1))
  if len(seen)%10==0:print('CHECK',len(seen),uses,leaves,'V',volume,'time',round(time.time()-start,2),flush=True)
 assert seen==set(nodes)
 if not partial:assert not missing and volume==1 and '' in completed and reflections==[('4021','4020')]
 out={'checked_nodes':len(seen),'checked_uses':uses,'strict_coefficients':uses*int(NN),'strict_minors':3*uses*int(NN),'leaves':leaves,'volume':str(volume),'missing':missing,'minima':[str(x) for x in mins],'reflected_quarters':reflections}
 print(json.dumps(out),flush=True)
 return out

def geometry_proof():
    # Strict interior positivity follows from nonnegative Bernstein coefficients
    # with at least one positive coefficient. Cube walls may be indexed limits.
    u,t=S.symbols('u t'); variables=(x,r,u,t,l); sub={p:u*t,q:(1-u)*t}
    guards={}; triangle_identities=0
    for f,face in enumerate(FACES):
        a,b,c=(Z[i] for i in face[:3]); n=(b-a).cross(c-a); h=n.dot(a)
        for i,z in enumerate(Z):
            sl=S.expand((h-n.dot(z)).subs(sub))
            if i in face: assert sl==0
            else: guards['support_%d_%d'%(f,i)]=sl
        for pos,i in enumerate(face):
            nxt=Z[face[(pos+1)%len(face)]]; prv=Z[face[(pos-1)%len(face)]]
            turn=S.expand(n.dot((nxt-Z[i]).cross(prv-Z[i])))
            if len(face)==3:
                assert S.expand(turn-n.dot(n))==0
                triangle_identities+=1
            else: guards['corner_%d_%d'%(f,i)]=S.expand(turn.subs(sub))
    guards['D_lower']=S.expand((D-R(7,32)).subs(sub))
    guards['D_upper']=S.expand((1-D).subs(sub))
    result={}
    for name,sl in guards.items():
        degrees,coeff,den=scalar_bernstein(sl,variables)
        assert min(coeff.flat)>=0 and max(coeff.flat)>0,(name,degrees)
        result[name]={'degrees':degrees,'coefficients':coeff.size,
                      'positive':sum(a>0 for a in coeff.flat),
                      'minimum':str(R(int(min(coeff.flat)),den))}
    dd=S.S(0);jj=S.zeros(3,1);triangles=0
    for face in FACES:
        a=Z[face[0]]
        for k in range(1,len(face)-1):
            b,c=Z[face[k]],Z[face[k+1]];v=a.dot(b.cross(c))
            dd+=v;jj+=v*(a+b+c)/4;triangles+=1
    assert S.expand(dd-D)==0 and all(S.expand(z)==0 for z in jj-J)
    assert triangles==16 and triangle_identities==15 and len(guards)==77
    return {'guards':result,'triangle_corner_identities':triangle_identities,
            'actual_boundary_triangles':triangles,'D_interval':['7/32','1']}

def power_audit(data,den):
    # Independent inverse Bernstein transform recovers ALL polynomial entries.
    arr=data.copy()
    for axis,n in enumerate(NS):
        T=np.array([[comb(n,i)*comb(i,k)*(-1)**(i-k) if k<=i else 0
                     for k in range(n+1)] for i in range(n+1)],object)
        arr=np.moveaxis(np.tensordot(T,arr,axes=(1,axis+2)),0,axis+2)
    u,t=S.symbols('u t'); variables=(x,r,u,t,l)
    for a,(i,k) in enumerate(ARROWS):
        Q=-sym(D*Z[i]-J,Z[k]-Z[i])
        for b,(ii,jj) in enumerate(PAIRS):
            original=S.Poly(S.expand(Q[ii,jj].subs({p:u*t,q:(1-u)*t})),*variables).as_dict()
            for e in product(*(range(n+1) for n in NS)):
                assert R(int(arr[(a,b)+e]),den)==original.get(e,0)
    return 34*6*int(NN)

def controls():
    # Three genuine nonwinning bodies and complete unbounded common-metric rays.
    configs=[(('19/20','17/20','13/20','3/10','1/40'),512,[3,7],[0,4],[(1,2),(4,9)]),
             (('3/20','4/5','3/5','3/10','3/10'),128,[3,7],[2,4],[(1,8),(4,9)]),
             (('49/50','1/25','1/100','49/50','7/8'),256,[7,9],[1,8],[(2,8),(7,9)])]
    u=S.Matrix((1,3,-2));v=S.Matrix((3,-1,0));w=S.Matrix((-1,-3,-5))
    assert u.dot(v)==u.dot(w)==v.dot(w)==0
    L,t=S.symbols('L t')
    M=L**2*u*u.T+L*v*v.T+w*w.T
    W=u*u.T/u.dot(u)**2+L*v*v.T/v.dot(v)**2+L**2*w*w.T/w.dot(w)**2
    assert (M*W-L**2*S.eye(3)).applyfunc(S.expand)==S.zeros(3)
    records=[]
    for theta,L0,uu,ss,hh in configs:
        B=geometry(tuple(map(R,theta)));X=[z-B['g'] for z in B['z']];poles=B['poles']
        pp={(i,j):S.expand((X[i].T*M*(X[j]-X[i]))[0]) for i,j in ARROWS}
        qq={(i,j):S.expand((poles[i].T*W*(poles[j]-poles[i]))[0]) for i,j in DUAL}
        polys={};sg={}
        for side,rows in [('primal',pp),('polar_scaled_by_L_squared',qq)]:
            for (i,j),f in rows.items():
                coeff=[S.expand(f.subs(L,L0+t)).coeff(t,k) for k in range(3)]
                sign=S.sign(coeff[0]);assert sign and all(sign*c>=0 for c in coeff)
                assert S.Poly(f,L).degree()<=2
                sg[side,i,j]=int(sign)
                polys[side+':'+str(i)+'>'+str(j)]=coeff
        sgnp=lambda i,j:sg['primal',i,j]
        sgnq=lambda i,j:sg['polar_scaled_by_L_squared',i,j]
        U=[i for i in range(10) if all(sgnp(a,b)<0 for a,b in ARROWS if a==i)]
        St=[i for i in range(9) if all(sgnq(a,b)<0 for a,b in DUAL if a==i)]
        H=[]
        for i,j in EDGES:
            f,g=EF[i,j]
            if max(sgnp(i,j),sgnp(j,i),sgnq(f,g),sgnq(g,f))<0:H.append((i,j))
        assert U==uu and St==ss and H==hh and len(U)+len(St)-len(H)==2
        records.append(dict(theta=theta,raw_vertices=B['z'],volume=B['volume'],centroid=B['g'],
            covariance=B['covariance'],poles=poles,L_min=L0,S=St,U=U,H=H,weak_points=0,
            zero_primitives=0,shifted_primitive_coefficients=polys))
    return dict(orthogonal_vectors=(u,v,w),M_polynomial=M,scaled_inverse_polynomial=W,controls=records)

def reflection_proof():
    # Involutive coordinate and true-label bijections; actual moments included.
    permutation=(5,4,3,2,1,0,6,7,9,8)
    A=S.Matrix(((0,1,0),(1,0,0),(0,0,1)))
    substitution={x:r,r:x,p:q,q:p}
    transform=lambda a:a.subs(substitution, simultaneous=True).applyfunc(S.expand)
    assert S.expand(D.subs(substitution, simultaneous=True)-D)==0
    assert transform(J)==(A*J).applyfunc(S.expand)
    assert all(transform(Z[i])==(A*Z[permutation[i]]).applyfunc(S.expand) for i in range(10))
    idx={a:i for i,a in enumerate(ARROWS)}
    arrows=[idx[permutation[i],permutation[j]] for i,j in ARROWS]
    assert sorted(arrows)==list(range(34)) and all(arrows[arrows[i]]==i for i in range(34))
    trees=treepack();registered={(r,m) for r,ids,m in trees}
    reflected={(permutation[r],sum(1<<arrows[i] for i in ids)) for r,ids,m in trees}
    assert reflected==registered
    # In compact cube coordinates, p<->q is u<->1-u with t unchanged.
    u,t=S.symbols('u t')
    assert (u*t).subs(u,1-u)==(1-u)*t
    return dict(vertex_permutation=permutation,arrow_permutation=arrows,
                exact_rooted_tree_bijection=len(reflected),
                source_box=('x[0,1]','r[0,1]','u[0,1/2]','t[0,1]','lambda[0,1/2]'),
                target_box=('x[0,1]','r[0,1]','u[1/2,1]','t[0,1]','lambda[0,1/2]'))

def main():
    if not __debug__:raise RuntimeError('Assertions must be enabled')
    assert sys.version_info[:2]==(3,13) and S.__version__=='1.14.0' and np.__version__=='2.3.5'
    if len(sys.argv)!=3 or sys.argv[1] not in ('build','check'):
        raise SystemExit('Use: python -B h5_full_domain.py build DIRECTORY, or check CERTIFICATE_JSON')
    data,den=polynomial();assert den==31850496
    reconstructed=power_audit(data,den);gp=geometry_proof();cc=controls();rp=reflection_proof()
    if sys.argv[1]=='build':
        import scipy
        assert scipy.__version__=='1.17.0'
        directory=Path(sys.argv[2]);directory.mkdir(parents=True,exist_ok=False)
        cert=build(directory/'certificate.json',data,den,resume=os.environ.get('H5_RESUME'))
    else:
        directory=Path(sys.argv[2]).parent;cert=json.loads(Path(sys.argv[2]).read_bytes())
    assert cert['object']=='H5_FULL_CUBE_PRIMAL_V1' and cert['complete']
    proof=verify(cert,data,den)
    report=dict(object=NAME,parent=PARENT,parent_sha256=PARENT_SHA256,
        certificate_sha256=sha((directory/'certificate.json').read_bytes()),
        geometry=gp,reflection=rp,complete_power_reconstruction_checks=reconstructed,
        cube_variables=('x','r','u','t','lambda'),map_p='u*t',map_q='(1-u)*t',
        D_interval=('7/32','1'),epsilon='1/4294967296',
        distinct_stresses=len(cert['rows']),weight_terms=sum(len(a) for a in cert['rows']),
        maximum_weight=max(w for row in cert['rows'] for k,w in row),
        tree_counts=(4879,48790),proof=proof,physical_controls=cc,status='EXACT_PASS')
    raw=wire(report);out=directory/'report.json'
    if sys.argv[1]=='check' and out.exists():assert out.read_bytes()==raw
    else:out.write_bytes(raw)
    for name in ('certificate.json','report.json'):
        b=(directory/name).read_bytes();print(name,len(b),sha(b))
    src=Path(__file__).read_bytes();print(Path(__file__).name,len(src),sha(src))
    print(NAME+'_ALL_48790_ROOTED_TREES_ALL_SPD_PASS')

if __name__=='__main__':main()
```

#### Source 2: h5_stress_exit_and_collar.py

```python
#!/usr/bin/env python3
"""Exact parent-row countercontrol and arithmetic for the true-refill collar.
Dependency: the complete h5_full_domain.py supplied in the same handoff.
The accompanying proof, not these scalar checks alone, bounds volume/COM changes.
"""
import h5_full_domain as H
ROW=((0,1,8),(1,8,49),(3,2,100),(4,3,88))
EXPECTED=(120502905263359418873,471068629445597417,460359102261497)
DEN=6791684096000

def main():
    B=H.controls()['controls'][0]
    assert B['theta']==('19/20','17/20','13/20','3/10','1/40') and B['L_min']==512
    coeff=[sum(w*B['shifted_primitive_coefficients'][f'primal:{i}>{j}'][k]
               for i,j,w in ROW) for k in range(3)]
    assert coeff==[H.R(n,DEN) for n in EXPECTED] and min(coeff)>0
    delta=H.R(1,2**50);epsilon=H.R(1,2**32)
    assert 16*19==304 and 16*H.R(195,4)==780
    assert 304*delta<H.R(7,64)
    assert H.R(64,7)*(780+2*304)<12800
    assert 12801*delta<1 and 14*12801==179214
    assert 179214*delta<epsilon
    report={'parent':'minimum-0267',
            'parent_certificate_sha256':'eb610ab904f7760da34492cee44348ea16699025805b678e84b8ae2c482f1115',
            'zero_based_row':94,'row':ROW,'theta':B['theta'],'L_min':512,
            'positive_coefficients_in_L_minus_512':coeff,'S':B['S'],'U':B['U'],
            'H':B['H'],'weak_points':0,'raw_refill_collar':delta,
            'arrow_error_upper':179214*delta,'reference_margin':epsilon,
            'scope':'Actual own222, not U1. Collar requires displayed true cycles and newly integrated centroid.'}
    print(H.wire(report).decode(),end='')
    print('H5_STRESS_EXIT_AND_TRUE_REFILL_COLLAR_PASS')

if __name__=='__main__':
    main()
```

### 8. Most useful continuation

In the larger literal basal chart

```
(b,0), (c,0), (1-p,p), (q,1-q), (0,d), (0,a), (u_B,v_B),
```

where u_B,v_B are basal coordinates rather than the compact p/q parameter u, the theorem fixes `b=a=1/4` and `u_B=v_B=1/16`, while allowing all `c=1-3x/4`, `d=1-3r/4`, p, q and positive taper. A genuine full U1 search must therefore free those remaining basal parameters, or leave the parallel model, rather than retune the already exhausted taper/shear/metric directions. The true-refill collar must also be respected. Any proposed survivor still needs one actual volume centroid, the complete true-edge U census, and then the literal inverse metric for its full S/H/weak census. Neither this exclusion nor the nonwinning controls supply an own110weak000 attainer outside the domain.
