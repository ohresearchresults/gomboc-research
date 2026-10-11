# minimum-0250

Historical AI scientific report · saved 2026-09-26 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# H5_PHYSICAL_NORMAL_CONE_AND_OFF_MACRO_ALL_TAPER_V1

## Result and scope

**No genuine U1 body was found.** The strongest positive result is a new all-metric, all-taper exclusion outside the supplied closed macro and its reflection. A second result is an exact elimination of the normal metric parameter, together with a complete rational fixed-shear test for U1 and a physical height-stratified equilibrium auditor.

The new excluded basal domain is

\[
\left\|(x,r,p,q)-(9/20,1/50,4/5,1/10)\right\|_\infty\le 2^{-28},
\qquad 0<\lambda<1.
\]

**Every genuine homogeneous H5 body in this domain has at least two strict unstable vertices under every SPD metric, including arbitrary conditioning and incidental weak contacts.** Its reflected domain is excluded as well. More strongly, every complete rooted true-edge weak-arrow cone is empty for every nonzero PSD metric. The collapsed taper endpoints assert indexed matrix limits, not ten-vertex bodies.

This does not close all H5, any complete E17 incidence class, or the proper110 problem. The supplied accepted interval **34 <= C_min <= 622 remains unchanged**. fileciteturn0file3L9-L11 The new work is not an extension of the coordinator's full-basal high-lambda collar: the new basal centre lies outside both all-taper macros, and its exclusion covers every taper, including the lower/middle frontier. It is nevertheless a local basal tube, not a full-basal theorem.

## Input authority and reading

I read the complete single assignment fragment and all four supplied files through EOF, including the entire 282584-byte journal. The mounted bytes matched the supplied SHA-256 values:

- Geometry/source: 14478 bytes, `4b54ee5513f10959876b1be674b1269a9679e837c3c1ef19a09d39f7780901d8`.
- Three-quarters atlas: 10743 bytes, `937c60eccc01a8d6496c35b7808bc12031248fd7f54c3e1abb8d8239521a959c`.
- Three-quarters proof/verifier: 9887 bytes, `03b93a1aba81c8e48f9557af603bb072d4c426b8dcfcd0bbc03312552e153d8f`.
- Journal: 282584 bytes, `cdcc565ed833295d0f294c6eb0129aa894085eb78fc85d9203f82d1f14f92f0b`.

The literal geometry and actual moment convention are those of the supplied source, not an arithmetic vertex centre. fileciteturn0file0L76-L100 The supplied full-basal lambda >= 3/4 theorem and the all-taper macro/reflection determine the starting boundary. fileciteturn0file2L3-L6 fileciteturn0file3L910-L921 Archived sources mentioned in the journal were not treated as accessible computational inputs. No missing archived dependency is needed to reconstruct the results below. I did not independently replay the supplied 332-certificate atlas; the new atlas has its own independent exact checker.

## 1. Exact physical normal-metric elimination

Normal contraction was already recorded in the notebook; I do not count that observation alone as new. fileciteturn0file3L758-L761 The useful additions are an exact necessary-and-sufficient threshold criterion, correct treatment of zero cross-layer derivatives, a complete fixed-shear tangential-metric decision, and the physical inverse-metric census.

Fix an actual body with vertices on z=0 and z=1 and its actual interior centre g=(c,gamma), 0<gamma<1. Every SPD metric is uniquely

\[
M(G,v,\eta)=\begin{pmatrix}G&Gv\\v^TG&v^TGv+\eta\end{pmatrix},
\quad G>0,\quad\eta>0,
\]
\[
N=M^{-1}=\begin{pmatrix}G^{-1}+vv^T/\eta&-v/\eta\\-v^T/\eta&1/\eta\end{pmatrix}.
\]

Here eta is a **metric Schur complement**, not the body's geometric height or taper. It is named `y` in the code. Put Y_i=z_i,xy-c+(z_i,z-gamma)v. Within-layer derivatives are independent of eta. Every basal-to-top spoke has

\[
D_{ij}(\eta)=Y_i^TG(Y_j-Y_i)-\gamma\eta,
\]

and every top-to-basal spoke has the same form with gamma replaced by 1-gamma. Thus increasing eta can only add strict unstable vertices.

Let L consist of vertices for which **all same-layer true-edge derivatives are strictly negative**. Each layer supplies at least one such vertex, so |L|>=2. For i in L define

\[
t_i=\max_{j\text{ across a true spoke}}\frac{Y_i^TG(Y_j-Y_i)}{c_i},
\quad c_i=\gamma\ (i<7),\quad c_i=1-\gamma\ (i\ge7).
\]

Then, exactly,

\[
U(\eta)=\{i\in L:\eta>t_i\}.
\]

Sort the thresholds with multiplicities. Necessarily t_(1)<=0, since an SPD body always has a farthest strict unstable vertex. Therefore

\[
\boxed{\exists\eta>0:\ |U(\eta)|=1\quad\Longleftrightarrow\quad t_{(2)}>0.}
\]

When this holds, the entire U1 interval is **0<eta<=t_(2)**. At its upper endpoint additional weak contacts are possible; that endpoint is not automatically proper110.

Equivalently, at eta=0, every nonroot must have a same-layer derivative >=0 or a **strictly positive** cross-layer derivative. Allowing a zero spoke here would be wrong: it becomes negative for every eta>0. Every allowed arrow strictly increases projected squared norm, including zero same-layer derivatives because the same-layer edge has positive G-length. These arrows therefore give a complete genuine rooted tree when exactly one vertex has no allowed exit. Choosing a positive eta below the threshold and rechecking all true arrows gives an actual SPD witness, not merely a compatible quotient support.

This proves that a primal U1 component in this parallel two-layer class cannot exist only at full rank while avoiding the rank-two normal boundary. **It does not preserve S, H, or weak freedom**, and makes no analogous assertion about connected components of the joint proper110 set.

### Exact fixed-shear decision and the remaining dimensions

Normalize tr(G)=1:

\[
G=\tfrac12\begin{pmatrix}1+t&u\\u&1-t\end{pmatrix},\qquad t^2+u^2<1.
\]

All 34 projected true-arrow derivatives are affine functions C+A t+B u. For rational shape and shear, the complete open-disk arrangement can be inspected exactly using rational pair intersections, one rational point in each open line segment, rational points on both sides of every segment, and the origin. Tangencies to the disk boundary are not SPD points. Constant and identically-zero rows are retained in the sign test.

`decide(theta,v)` implements this complete fixed-shear U1 decision. It samples **sign strata**, not a feasibility grid. A successful return constructs a positive eta, a complete tree using arrows rechecked at that eta, and the actual full equilibrium census. The routine can return weak tree arrows; it does not silently upgrade them to nine strict arrows or weak-free mechanics.

For each fixed G,v, all primal derivatives and all positively scaled polar derivatives are affine in eta:

\[
D_{ij}=a_{ij}+b_{ij}\eta,\qquad \eta E_{FG}=c_{FG}+d_{FG}\eta.
\]

There are 14 nonconstant primal rows and at most 24 nonconstant polar rows, hence **at most 38 positive rational event heights**. Testing every open interval, every event itself, and the unbounded tail decides the complete physical census on that pencil. Four edge primitives, the actual N=M^-1, and physical-point deduplication are used. Harmless zero primitives are not rejected.

This eliminates eta from U1 feasibility and supplies exact G elimination at a fixed shear. It is **not** a complete joint proper110 decision over an entire G sign cell: polar event order can vary continuously within that cell.

### A separate analytic exclusion of the entire triangular-shadow sector

For literal H5, the projected upper triangle is v+lambda*Delta and the basal polygon is contained in (1-lambda)*Delta. The upper triangle contains the basal polygon exactly when

\[
v_1\le0,\quad v_2\le0,\quad v_1+v_2\ge1-2\lambda.
\]

This sector is nonempty for lambda>=1/2. In any G metric, a triangle has at least two nonobtuse corners. At such a corner a, write the interior projected centre as a+alpha e+beta f with alpha,beta>0 and e^TGf>=0. Both corner derivatives, and hence the derivative toward every other projected point, are strictly negative. A coincident cross-layer projection receives the strictly negative normal contribution instead. Consequently **U>=2 throughout this entire shear sector for every G and eta>0**, for every admissible basal shape. This is an analytic true-vertex obstruction, not a sampled stress atlas.

## 2. New all-taper, all-metric original-arrow obstruction

At the basal centre b*=(9/20,1/50,4/5,1/10), define D=6V, K=6J by the complete oriented boundary. For every literal directed edge form

\[
P_{ij}(\lambda)=\operatorname{sym}[(Dz_i-K)(z_i-z_j)^T].
\]

These matrices have degree at most four in lambda. For a positive-weight certificate C, P_C=sum w_ij P_ij. Exact degree-four Bernstein coefficient matrices are positive definite on each of three closed intervals:

| Taper interval | Certificates | PD coefficient matrices | Uncovered rooted trees |
|---|---:|---:|---:|
| [0,1/3] | 805 | 4025 | 0 |
| [1/3,2/3] | 1110 | 5550 | 0 |
| [2/3,1] | 401 | 2005 | 0 |

There are **2316 distinct certificates, 11580 PD matrices, and 34740 positive leading principal minors**. Every interval independently covers all 48790 orientations of the 4879 spanning trees of the actual 17-edge graph. The maximum integer weight is 651 and maximum weight sum is 1001. This is literal original-arrow containment; no connected basal quotient or norm-only substitute is used.

The independent standard-library checker constructs the volume and first-moment polynomials directly from all true facet cycles, verifies all four polynomial identities, reconstructs every Bernstein expansion back into power coefficients, checks all Sylvester minors with arbitrary integers, and re-enumerates coverage without using the locator's `covered_including_failed` field. All three final failure lists are empty.

For W=sum w, the exact common lower bound obtained from 4det/tr^2 is

\[
P_C/W\succeq\gamma_* I,\qquad
\gamma_*=\frac{303561732257186712559}{189722434302921655863000000}>2^{-20}.
\]

Throughout the full basal parameter domain, 7/32<=D<=1. Thus the reference physical stress P_C/D has the same dyadic lower bound. For any nonzero PSD M,

\[
\operatorname{tr}(MP_C)=-D\sum w_{ij}D_{ij}.
\]

A complete weak rooted tree would contain a certificate whose left-hand trace is positive but whose right-hand side is nonpositive. This contradiction excludes every such tree, including the weak-arrow boundary. A genuine U1 body necessarily supplies one: each nonroot has a nonnegative true-edge derivative, and the exact norm increment is 2D_ij+|z_j-z_i|_M^2>0. Choosing those exits is acyclic and leads to the unique strict unstable vertex. Incidental weak contacts therefore do not evade the contradiction.

### Actual-centroid extension to the closed four-dimensional basal tube

Let epsilon be the maximum change in the four basal parameters, with lambda held fixed. The basal formulas satisfy |Delta A|<=3epsilon/2, |Delta b_x|,|Delta b_y|<=57epsilon/32, and |Delta(1-3xp/4)|,|Delta(1-3rq/4)|<=3epsilon/2. Substitution in the literal moment formulas gives

\[
|\Delta D|\le3\epsilon,\quad
|\Delta K_x|,|\Delta K_y|\le195\epsilon/64,\quad
|\Delta K_z|\le3\epsilon/4.
\]

Using D>=7/32 and 0<=g_j<=1 yields

\[
|\Delta g_x|,|\Delta g_y|\le387\epsilon/14,
\qquad |\Delta g_z|\le120\epsilon/7,
\qquad\|\Delta g\|_2<43\epsilon.
\]

Matched raw vertices move by at most sqrt(2)*epsilon. Centred vertices therefore move by less than 45epsilon, while true edge vectors move by less than 3epsilon. Raw vertices and their centroid remain in [0,1]^3. Each unscaled physical arrow matrix changes in operator norm by less than 48sqrt(3)*epsilon<84epsilon, safely bounded by 90epsilon.

For epsilon=2^-28, this loss is less than half the dyadic reference gap. Hence every covered tree contains a certificate with

\[
\frac{1}{W}\sum w_{ij}D_{ij}<-2^{-21}\operatorname{tr}M.
\]

The tube stays strictly inside 0<x,r<1, p,q>0, p+q<1. The seven basal corners remain strict; their three unchanged edge directions match the upper triangle, retaining exactly the stated nine maximal facet cycles and 17 true edges for 0<lambda<1. No frozen-centre approximation enters this extension.

Reflection swaps x/r and p/q, interchanges the horizontal coordinates, and permutes labels by (5,4,3,2,1,0,6,7,9,8). It yields the reflected tube without a new tree count.

## 3. Retained actual ten-shadow control and its full physical pencil

Take theta=(9/20,1/50,4/5,1/10,3/11), v=(-1/50,9/20). The literal vertices are

\[
(2/11,0,0),(53/110,0,0),(8/55,32/55,0),(4/55,36/55,0),
(0,197/275,0),(0,2/11,0),(1/22,1/22,0),
(0,0,1),(3/11,0,1),(0,3/11,1).
\]

The **actual** volume and centroid are

\[
V=9703/90750,\qquad
 g=(76658/533665,536644/2668325,14953/38812).
\]

All ten projected vertices are strictly exposed, in cycle (0,1,8,2,3,4,9,7,5,6), with minimum exact oriented support guard 117/151250. The top foot has negative second coordinate:

\[
\beta_{\rm top}=(3328769/21346600,-3223901/42693200).
\]

Thus this is not the trivial triangular-shadow case or a case where both end facets are stable. At this fixed shear the exact G-disk decision checks 969 distinct sign strata using 1678 rational representatives and still proves U>=2 for every G and eta>0. Its projected sink-count histogram is {2:264,3:321,4:219,5:111,6:46,7:8}. This is a useful nonattaining calibration, not a U1 witness.

For G=diag(1,2), the layer thresholds are

\[
(t_1,1)=(-888607431/822415000,1),\quad
(t_9,9)=(-644747/52489800,9),\quad
(t_4,4)=(166011133/9046565000,4).
\]

At eta0=677085939/307895830000,

\[
M=\begin{pmatrix}1&0&-1/50\\0&2&9/10\\-1/50&9/10&2027/5000+\eta_0\end{pmatrix},
\]

with the **actual inverse** N from the Schur formula above. Its leading minors are 1,2,2eta0>0. Exact census:

**S={0,1}; U={1,9}; H={(1,8),(5,7)}; physical weak points=0; all 68 true-edge primitives nonzero.**

The complete eta>0 pencil has ten event heights, in increasing order:

```text
677085939/153947915000
8209963/1603855000
2901837/411207500
257709126069/28831402655000
173287987/14434695000
166011133/9046565000
312640365101/11924681285000
27094247897/633525145000
94034499/822415000
407282023593/989937905000
```

The eleven open-interval strict censuses are, in order,

```text
222,222,222,323,424,424,435,536,435,435,536.
```

Events 1,2,5,9 have a harmless zero only. Events 3,4,7,8,10 have one EF point, respectively on edges 45,12,67,57,07. Event 6 has one VE point on edge 49. All ten walls are explicitly audited; no VF point occurs in this pencil. Consequently its minimum S and minimum U are both two. The recovered portrait contains every wall/open-stratum census, every weak point coordinate, the exact M/N, and all 68 primitives at eta0. This is not an all-M S>=2 claim for the basal ray.

## 4. What was tried and what remains unresolved

I searched actual full-tree feasibility, not just three-arrow compatibility. Exploratory metric and projected-tree searches did not produce a verifiable U1 object; their failure supplies no exclusion. The retained exact work consists of the fixed-shear disk decision, the complete physical pencil, and the three-cell all-root atlas with its actual-centroid tube. A single larger taper interval failed the restricted certificate search before subdivision; that failure was not interpreted as a feasible cone.

The next decisive question has the concrete form

\[
\exists\,(x,r,p,q,\lambda,v,G):\quad t_{(2)}(x,r,p,q,\lambda,v,G)>0
\]

outside the supplied exclusions and the new tubes, preferably 0<lambda<=2/3. This is a nine-variable primal feasibility problem after normal-height elimination; at a fixed shape and shear, the remaining G search is the exact two-dimensional arrangement decision. A successful rational result must then be lifted to eta>0 and audited on all true edges. The finite physical height census determines whether that particular G,v pencil ever gives proper110. Failure of its S1 test does not exclude other G values in the same primal sign cell.

No bound, canonical registry count, or attaining construction is changed. There is no claim of external novelty priority or proof-assistant formalization.

## 5. Source-only recovery and executed evidence

The three complete source units below require no parent files, saved atlas, archive path, or previous sandbox. The literal geometry, basal centre, graph, cells, numerical proposal parameters, integer rounding ladder, independent polynomial checker, and physical controls are all included.

Tested environment: CPython 3.13.5. Atlas proposal uses NumPy 2.3.5 and SciPy 1.17.0 with OPENBLAS_NUM_THREADS=1. Acceptance and the independent checker use exact integers/Fractions; the independent checker and normal-cone unit run with the standard library alone. Solver output is only a proposal. On a different numerical stack, a different proposed atlas must pass the exact checker; the pins below identify the executed object, not every possible valid atlas.

Save the three source blocks under their displayed filenames in a new empty directory, then run:

```sh
OPENBLAS_NUM_THREADS=1 python -B h5_taper_atlas.py 0 1/3 5000
OPENBLAS_NUM_THREADS=1 python -B h5_taper_atlas.py 1/3 2/3 5000
OPENBLAS_NUM_THREADS=1 python -B h5_taper_atlas.py 2/3 1 5000
python -B -S h5_verify_taper.py
python -B -S h5_normal_cone.py cone 6
python -B -S h5_normal_cone.py portrait
```

The explicit 5000 limit matters: the middle cell needs 1110 proposals that become certificates, exceeding the locator's default limit. Final atlas files retain their historical `progress` filenames but have no failed entries and independently verified complete coverage.

Source pins:

```text
h5_normal_cone.py 11669 3ee5d85e8d3489286a3afbe3704f25250849036ec79328b759d4aae68a0a7f76
h5_taper_atlas.py 5309 ef1abbd36b9d78c35aed1cf2e2adb5f34788fa2d689990688eccbe05703cee10
h5_verify_taper.py 6488 a50817ce6f03a99fabc54085f477d87282f55aa2c23d7a8b917e1db75e6bffd6
```

Expected output pins:

```text
h5_taper_progress_0_1_3.json 28997 d042cbdeff75902df802e698a77a6be13fa031ef6fb1efa1316c35540d735145
h5_taper_progress_1_3_2_3.json 41134 898f83eac41375ad80e3e1446e240fbb040de52d54f76a6ec6ae70ef44587eee
h5_taper_progress_2_3_1.json 12162 a850afe044ebb06564e5dea8974de109dd9e3783edcb14982adf78af110219a8
h5_taper_report.json 2529 d4b76cfc21c351e28956d62910c381ff99865b59bb893754ad83231790fabafe
h5_cone_6.json 480 a8b832f680b3e5811e19af04ffbe45bf072bdf027969b61e966a0fe7b8c725d7
h5_normal_portrait.json 25947 e7bc6afdea2bd739b8cec0c91db74c2e2bdf8bd9ca3df6bb1d8aa0f471c00b6a
```

Expected exact markers:

```text
H5_OFF_MACRO_ALL_TAPER_ACTUAL_CENTROID_TUBE_EXACT_PASS
H5_NORMAL_CONE_EXACT_PASS
```

I executed the independent checker, a fresh source-only reconstruction, and a second reconstruction from a lossless wrapper containing only these sources. All six output files were byte-identical and passed their pins. The second reconstruction ended with `H5_FRONTIER_WRAPPER_SOURCE_ONLY_SIX_OUTPUTS_BYTE_IDENTICAL_PASS`. This is this worker's execution, not a claimed coordinator replay.

The optional wrapper `recover_h5_frontier.py` is 14270 bytes, SHA-256 `b323b17b2a226ec00d8e839d2f178912c8d38821a1e63a8ab2a82b7a1bdb073c`; its decoded three-source JSON map is 23977 bytes, SHA-256 `af7459c5c800ab6bf3a43e73c75db2b6b4d7ca5675fee24ec7d81cce61eb7d95`. The readable sources below, rather than that optional wrapper, are the continuation-critical recovery unit.

### h5_normal_cone.py

```python
"""Exact H5 normal-height elimination and complete tangential-cone decision.
CPython 3.13.5, standard library only. No numerical optimization in this unit.
"""
from fractions import Fraction as F
from itertools import combinations
from math import gcd,lcm
from functools import reduce
from pathlib import Path
import json,hashlib,sys,time

FACETS=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),(9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
EDGES=tuple(sorted({tuple(sorted((f[i],f[(i+1)%len(f)]))) for f in FACETS for i in range(len(f))}))
ARROWS=tuple(sorted((i,j) for a,b in EDGES for i,j in ((a,b),(b,a))))
ADJ=tuple(tuple(j for a,j in ARROWS if a==i) for i in range(10))
EF=tuple(tuple(k for k,f in enumerate(FACETS) if a in f and b in f) for a,b in EDGES)
DUAL=tuple(sorted((i,j) for a,b in EF for i,j in ((a,b),(b,a))))
DADJ=tuple(tuple(j for a,j in DUAL if a==i) for i in range(9))

def vec(x):return tuple(map(F,x))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(a,t):return tuple(t*x for x in a)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def matvec(A,x):return tuple(dot(r,x) for r in A)
def bil(a,A,b):return dot(a,matvec(A,b))
def inv2(G):
 a,b=G[0];bb,c=G[1];assert b==bb and a>0 and a*c-b*b>0
 d=a*c-b*b;return ((c/d,-b/d),(-b/d,a/d))
def sign(x):return (x>0)-(x<0)
def encoded(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):encoded(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [encoded(v) for v in x]
 return x

def body(theta):
 x,r,p,q,la=map(F,theta);assert 0<x<1 and 0<r<1 and p>0 and q>0 and p+q<1 and 0<la<1
 s=1-la;B=((F(1,4),F(0)),(1-3*x/4,F(0)),(1-p,p),(q,1-q),(F(0),1-3*r/4),(F(0),F(1,4)),(F(1,16),F(1,16)))
 z=tuple((s*a,s*b,F(0)) for a,b in B)+((F(0),F(0),F(1)),(la,F(0),F(1)),(F(0),la,F(1)))
 D=F(0);K=(F(0),)*3
 for f in FACETS:
  for k in range(1,len(f)-1):
   a,b,c=(z[i] for i in (f[0],f[k],f[k+1]));d=dot(a,cross(b,c));D+=d;K=add(K,scale(add(add(a,b),c),d/4))
 A=(31-24*x*p-24*r*q)/64
 bx=F(509,3072)-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8
 by=F(509,3072)-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
 assert D==la+2*A*s*s
 assert K==(3*s**3*bx/2+s*s*la*(1-3*x*p/4)/4+la*la/4,3*s**3*by/2+s*s*la*(1-3*r*q/4)/4+la*la/4,A*s*s/2+la/2+la*la/4)
 assert D>0;g=scale(K,1/D);X=tuple(sub(a,g) for a in z);poles=[]
 for f in FACETS:
  a,b,c=(z[i] for i in f[:3]);n=cross(sub(b,a),sub(c,a));h=dot(n,a)
  assert n!=(0,0,0)
  for j in range(10):assert dot(n,z[j])==h if j in f else dot(n,z[j])<h
  H=h-dot(n,g);assert H>0;poles.append(scale(n,1/H))
 assert len(set(z))==10 and len(EDGES)==17 and len(set(EF))==17 and all(len(e)==2 for e in EF)
 return z,g,tuple(poles),D/6

def pencil(theta,v,G):
 v=vec(v);G=tuple(vec(r) for r in G);GI=inv2(G);z,g,q,V=body(theta);gamma=g[2];h=1-gamma;Y=tuple(add(sub(a[:2],g[:2]),scale(v,a[2]-gamma)) for a in z)
 P={};Q={};u=(-v[0],-v[1],F(1))
 for i,j in ARROWS:P[i,j]=(bil(Y[i],G,sub(Y[j],Y[i])),(z[i][2]-gamma)*(z[j][2]-z[i][2]))
 for i,j in DUAL:Q[i,j]=(dot(q[i],u)*dot(sub(q[j],q[i]),u),bil(q[i][:2],GI,sub(q[j][:2],q[i][:2])))
 assert sum(b!=0 for a,b in P.values())==14
 assert sum(b!=0 for a,b in Q.values())<=24
 L=[]
 for i in range(10):
  inner=[P[i,j][0] for j in ADJ[i] if z[i][2]==z[j][2]]
  assert inner
  if max(inner)<0:
   c=gamma if i<7 else h
   assert c>0
   thresholds=[P[i,j][0]/c for j in ADJ[i] if z[i][2]!=z[j][2]]
   L.append((max(thresholds),i))
 L.sort();assert len(L)>=2 and L[0][0]<=0
 return {'z':z,'g':g,'q':q,'volume':V,'v':v,'G':G,'GI':GI,'P':P,'Q':Q,'thresholds':L,'u1_upper':L[1][0]}

def metrics(v,G,y):
 assert y>0;GI=inv2(G);b=matvec(G,v);M=((G[0][0],G[0][1],b[0]),(G[1][0],G[1][1],b[1]),(b[0],b[1],bil(v,G,v)+y))
 N=((GI[0][0]+v[0]**2/y,GI[0][1]+v[0]*v[1]/y,-v[0]/y),(GI[1][0]+v[0]*v[1]/y,GI[1][1]+v[1]**2/y,-v[1]/y),(-v[0]/y,-v[1]/y,1/y))
 assert all(sum(M[i][k]*N[k][j] for k in range(3))==int(i==j) for i in range(3) for j in range(3))
 return M,N

def census(data,y,full=False):
 y=F(y);M,N=metrics(data['v'],data['G'],y);P={e:a+b*y for e,(a,b) in data['P'].items()};Q={e:(a+b*y)/y for e,(a,b) in data['Q'].items()};X=tuple(sub(a,data['g']) for a in data['z'])
 assert all(P[i,j]==bil(X[i],M,sub(X[j],X[i])) for i,j in ARROWS)
 assert all(Q[i,j]==bil(data['q'][i],N,sub(data['q'][j],data['q'][i])) for i,j in DUAL)
 U=tuple(i for i in range(10) if all(P[i,j]<0 for j in ADJ[i]));S=tuple(i for i in range(9) if all(Q[i,j]<0 for j in DADJ[i]));H=[];weak={};zero=sum(t==0 for t in P.values())+sum(t==0 for t in Q.values())
 for (i,j),(a,b) in zip(EDGES,EF):
  vals=(P[i,j],P[j,i],Q[a,b],Q[b,a])
  if max(vals)<0:H.append((i,j))
  if max(vals)<=0 and min(map(abs,vals))==0:
   pp=next((X[k] for k,l in ((i,j),(j,i)) if P[k,l]==0),None)
   qq=next((scale(matvec(N,data['q'][k]),1/bil(data['q'][k],N,data['q'][k])) for k,l in ((a,b),(b,a)) if Q[k,l]==0),None)
   if pp is not None and qq is not None:assert pp==qq
   point=pp if pp is not None else qq;assert point is not None
   kind='VF' if pp is not None and qq is not None else 'VE' if pp is not None else 'EF'
   if point not in weak:weak[point]={'point':point,'kind':kind,'edges':[]}
   weak[point]['edges'].append((i,j))
   if kind=='VF':weak[point]['kind']='VF'
 assert len(S)+len(U)-len(H)==2
 assert U==tuple(sorted(i for t,i in data['thresholds'] if y>t))
 out={'height':y,'S':S,'U':U,'H':H,'weak':list(weak.values()),'zero_primitives':zero,'counts':(len(S),len(U),len(H))}
 if full:out.update({'M':M,'N':N,'primal':[(i,j,P[i,j]) for i,j in ARROWS],'polar':[(i,j,Q[i,j]) for i,j in DUAL]})
 return out

def portrait(data):
 events=sorted({-a/b for a,b in tuple(data['P'].values())+tuple(data['Q'].values()) if b and -a/b>0});assert len(events)<=38
 rows=[];left=F(0)
 for right in events:
  rows.append({'stratum':('open',left,right),'census':census(data,(left+right)/2)})
  rows.append({'stratum':('wall',right),'census':census(data,right)});left=right
 rows.append({'stratum':('open',left,'infinity'),'census':census(data,left+1)})
 return {'events':events,'strata':rows,'minimum_U':min(len(r['census']['U']) for r in rows),'minimum_S':min(len(r['census']['S']) for r in rows)}

def arrow_lines(theta,v):
 z,g,q,V=body(theta);v=vec(v);Y=tuple(add(sub(a[:2],g[:2]),scale(v,a[2]-g[2])) for a in z);out=[]
 for i,j in ARROWS:
  a,b=Y[i],sub(Y[j],Y[i]);out.append((dot(a,b),a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]))
 return out

def canonical_line(cab):
 C,A,B=cab
 if A==B==0:return None
 den=lcm(*(x.denominator for x in cab));integers=tuple(int(x*den) for x in cab);d=reduce(gcd,(abs(i) for i in integers));integers=tuple(i//d for i in integers)
 C,A,B=integers
 if (A if A else B)<0:C,A,B=-C,-A,-B
 return C,A,B

def arrangement_samples(lines):
 # Every zero-, one-, and two-dimensional sign stratum in the OPEN SPD disk.
 lines=sorted({r for c in lines if (r:=canonical_line(c)) is not None and r[1]*r[1]+r[2]*r[2]>r[0]*r[0]})
 points={(F(0),F(0))};counts={'lines':len(lines),'line_segments':0,'crossing_points':0}
 for C,A,B in lines:
  N=A*A+B*B;R2=N-C*C;events=set()
  for CC,AA,BB in lines:
   den=BB*A-AA*B
   if den:
    t=F(C*(AA*A+BB*B)-N*CC,den)
    if t*t<R2:events.add(t)
  events=sorted(events)
  def point(t):return (F(-A*C-B*t,N),F(-B*C+A*t,N))
  for t in events:points.add(point(t));counts['crossing_points']+=1
  mids=[]
  if not events:mids=[F(0)]
  else:
   eps=F(1)
   while (events[0]-eps)**2>=R2:eps/=2
   mids.append(events[0]-eps)
   mids.extend((a+b)/2 for a,b in zip(events,events[1:]))
   eps=F(1)
   while (events[-1]+eps)**2>=R2:eps/=2
   mids.append(events[-1]+eps)
  for t in mids:
   p=point(t);points.add(p);counts['line_segments']+=1;n=(F(A,N),F(B,N));margin=1-dot(p,p);assert margin>0
   eps=min(F(1),margin/(4*(1+abs(dot(p,n))+dot(n,n))))
   for CC,AA,BB in lines:
    value=CC+AA*p[0]+BB*p[1];der=AA*n[0]+BB*n[1]
    if value and der:eps=min(eps,abs(value)/(2*abs(der)))
   for sgn in (-1,1):
    pp=add(p,scale(n,sgn*eps));assert dot(pp,pp)<1
    assert all(sign(CC+AA*pp[0]+BB*pp[1])==sign(CC+AA*p[0]+BB*p[1]) for CC,AA,BB in lines if CC+AA*p[0]+BB*p[1])
    points.add(pp)
 points=sorted(points);assert all(dot(p,p)<1 for p in points);counts['distinct_samples']=len(points)
 return points,counts

def decide(theta,v):
 lines=arrow_lines(theta,v);points,counts=arrangement_samples(lines);seen=set();hist={};witness=None
 for t,u in points:
  vals=tuple(C+A*t+B*u for C,A,B in lines);sg=tuple(sign(x) for x in vals)
  if sg in seen:continue
  seen.add(sg);outs=[[] for _ in range(10)]
  for (i,j),d in zip(ARROWS,vals):
   if (d>=0 if (i<7)==(j<7) else d>0):outs[i].append(j)
  roots=[i for i in range(10) if not outs[i]];assert roots
  hist[len(roots)]=hist.get(len(roots),0)+1
  if len(roots)==1:
   G=((F(1,2)*(1+t),u/2),(u/2,F(1,2)*(1-t)));data=pencil(theta,v,G);assert data['u1_upper']>0;y=data['u1_upper']/2;tree=tuple((i,min(j for j in ADJ[i] if data['P'][i,j][0]+data['P'][i,j][1]*y>=0)) for i in range(10) if i!=roots[0])
   par=dict(tree)
   for i in range(10):
    cur=i;visited=set()
    while cur!=roots[0]:assert cur not in visited;visited.add(cur);cur=par[cur]
   cc=census(data,y,True);assert len(cc['U'])==1
   assert all(data['P'][i,j][0]+data['P'][i,j][1]*y>=0 for i,j in tree)
   witness={'G':G,'normal_height':y,'tree':tree,'census':cc};break
 counts.update({'sign_strata_checked':len(seen),'projected_sink_count_histogram':hist})
 return {'theta':theta,'shear':v,'verdict':'EXACT_U1_WITNESS' if witness else 'ALL_G_SPD_ALL_POSITIVE_HEIGHTS_U2','counts':counts,'witness':witness}

CONTROLS=(
 (('1/2','1/2','3/10','3/10','2/5'),('1/50','2/25')),
 (('1/2','1/2','3/10','3/10','2/5'),('2/25','1/50')),
 (('1/10','9/10','1/10','4/5','3/10'),('1/20','1/20')),
 (('4/5','1/10','4/5','1/10','1/10'),('3/10','1/20')),
 (('9/10','9/10','2/5','2/5','3/10'),('1/10','1/10')),
 (('4/5','4/5','1/20','9/10','3/5'),('-1/10','1/5')),
 (('9/20','1/50','4/5','1/10','3/11'),('-1/50','9/20')),
)

def main():
 mode=sys.argv[1] if len(sys.argv)>1 else 'build'
 if mode=='cone':
  k=int(sys.argv[2]);out=decide(*CONTROLS[k]);path=Path(f'h5_cone_{k}.json')
 elif mode=='portrait':
  theta,v=CONTROLS[6];G=((F(1),F(0)),(F(0),F(2)));data=pencil(theta,v,G);out={'theta':theta,'shear':v,'G':G,'volume':data['volume'],'centroid':data['g'],'local_layer_thresholds':data['thresholds'],'portrait':portrait(data)};out['first_stratum_complete_census']=census(data,out['portrait']['events'][0]/2,True)
  Y=tuple(add(a[:2],scale(data['v'],a[2])) for a in data['z']);cy=(0,1,8,2,3,4,9,7,5,6)
  cross2=lambda a,b:a[0]*b[1]-a[1]*b[0]
  shadow_guards=[cross2(sub(Y[cy[(k+1)%10]],Y[cy[k]]),sub(Y[j],Y[cy[k]])) for k in range(10) for j in range(10) if j not in (cy[k],cy[(k+1)%10])]
  assert min(shadow_guards)>0
  foot=data['g'][:2];basefoot=add(foot,scale(data['v'],data['g'][2]));topfoot=sub(foot,scale(data['v'],1-data['g'][2]));la=F(theta[4])
  out['shadow']={'cycle':cy,'minimum_strict_support_guard':min(shadow_guards),'basal_foot':basefoot,'top_foot':topfoot,'top_facet_stable':min(topfoot)>0 and sum(topfoot)<la}
  assert not out['shadow']['top_facet_stable']
  path=Path('h5_normal_portrait.json')
 else:raise SystemExit('use cone INDEX or portrait')
 raw=(json.dumps(encoded(out),indent=2,sort_keys=True)+'\n').encode();path.write_bytes(raw);print(path.name,len(raw),hashlib.sha256(raw).hexdigest());print(json.dumps(encoded(out.get('counts',{'minimum_U':out['portrait']['minimum_U'],'minimum_S':out['portrait']['minimum_S'],'events':len(out['portrait']['events'])}) if mode=='portrait' else out['counts']),sort_keys=True));print('H5_NORMAL_CONE_EXACT_PASS')
if __name__=='__main__':main()
```

### h5_taper_atlas.py

```python
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
from h5_normal_cone import *
import numpy as np
from scipy.optimize import linprog
from time import monotonic
from math import comb

def get_trees():
 # Literal enumeration; no prior catalogue file is needed.
 from itertools import combinations
 out=[];ai={e:k for k,e in enumerate(ARROWS)}
 for es in combinations(EDGES,9):
  adj=[[] for _ in range(10)]
  for a,b in es:adj[a].append(b);adj[b].append(a)
  for root in range(10):
   p={root:root};queue=[root]
   for j in queue:
    for i in adj[j]:
     if i not in p:p[i]=j;queue.append(i)
   if len(p)!=10:break
   out.append([ai[i,p[i]] for i in range(10) if i!=root])
 assert len(out)==48790
 return np.array(out,dtype=np.int64)


def solve_square(A,b):
 A=[list(row)+[bb] for row,bb in zip(A,b)];n=len(b)
 for k in range(n):
  j=next(j for j in range(k,n) if A[j][k]);A[k],A[j]=A[j],A[k];d=A[k][k];A[k]=[a/d for a in A[k]]
  for j in range(n):
   if j!=k:
    d=A[j][k];A[j]=[a-d*c for a,c in zip(A[j],A[k])]
 return [row[-1] for row in A]

B4=[[F(comb(4,k))*F(j,4)**k*(1-F(j,4))**(4-k) for k in range(5)]for j in range(5)]
INV4=np.array([solve_square(B4,[F(i==j)for i in range(5)])for j in range(5)],dtype=object).T

def raw(theta):
 x,r,p,q,la=map(F,theta);s=1-la;B=((F(1,4),F(0)),(1-3*x/4,F(0)),(1-p,p),(q,1-q),(F(0),1-3*r/4),(F(0),F(1,4)),(F(1,16),F(1,16)))
 z=tuple((s*a,s*b,F(0))for a,b in B)+((F(0),F(0),F(1)),(la,F(0),F(1)),(F(0),la,F(1)))
 D=F(0);K=(F(0),)*3
 for f in FACETS:
  for j in range(1,len(f)-1):
   a,b,c=(z[i]for i in(f[0],f[j],f[j+1]));d=dot(a,cross(b,c));D+=d;K=add(K,scale(add(add(a,b),c),d/4))
 A=(31-24*x*p-24*r*q)/64;bx=F(509,3072)-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8;by=F(509,3072)-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
 assert D==la+2*A*s*s and D>0
 assert K==(3*s**3*bx/2+s*s*la*(1-3*x*p/4)/4+la*la/4,3*s**3*by/2+s*s*la*(1-3*r*q/4)/4+la*la/4,A*s*s/2+la/2+la*la/4)
 return z,D,K

def table_for(basal,lo,hi):
 values=[]
 for k in range(5):
  la=lo+(hi-lo)*F(k,4);z,D,K=raw(tuple(basal)+(la,));rows=[]
  for i,j in ARROWS:
   a=sub(scale(z[i],D),K);b=sub(z[i],z[j]);rows.append(tuple((a[r]*b[s]+a[s]*b[r])/2 for r,s in ((0,0),(0,1),(0,2),(1,1),(1,2),(2,2))))
  values.append(rows)
 vals=np.array(values,dtype=object);tab=np.einsum('ij,jkl->kil',INV4,vals);L=lcm(*(v.denominator for v in tab.flat));ints=[int(L*v)for v in tab.flat];assert max(map(abs,ints))<2**63;T=np.array(ints,dtype=np.int64).reshape(34,5,6)
 return T,L

def pd(row):
 a,b,c,d,e,f=map(int,row);return a>0 and a*d-b*b>0 and a*d*f+2*b*c*e-a*e*e-d*c*c-f*b*b>0

def locator(B,inds,T):
 BB=B[inds];n=len(inds);A=np.concatenate([BB[:,:,i,i].T for i in range(3)]);eq=np.r_[np.ones(n),0][None,:]
 for it in range(40):
  res=linprog(np.r_[np.zeros(n),-1],A_ub=np.c_[-A,np.ones(len(A))],b_ub=np.zeros(len(A)),A_eq=eq,b_eq=[1],bounds=[(0,None)]*n+[(None,None)],method='highs')
  if not res.success or res.x[-1]<1e-11:return None
  w=res.x[:-1];C=np.einsum('i,ijkl->jkl',w,BB);ev,Q=np.linalg.eigh(C)
  if ev[:,0].min()>1e-11:
   for den in (100,300,1000,3000,10000,30000,100000,300000):
    wi=np.rint(w*den).astype(np.int64);assert int(np.abs(T[inds]).max())*int(sum(wi))<2**63
    P=np.einsum('i,ijk->jk',wi,T[inds])
    if all(pd(row)for row in P):return [(int(inds[k]),int(wi[k]))for k in range(n)if wi[k]]
  bad=np.where(ev[:,0]<max(res.x[-1]*.95,1e-11))[0]
  if not len(bad):bad=np.argsort(ev[:,0])[:1]
  U=Q[bad,:,0];A=np.r_[A,np.einsum('jk,ijkl,jl->ji',U,BB[:,bad],U)]
 return None

def run(basal,lo,hi,limit=1000):
 lo,hi=F(lo),F(hi);assert 0<=lo<hi<=1;basal=tuple(basal);T,L=table_for(basal,lo,hi);fl=T.astype(float)/L;B=np.zeros((34,5,3,3));B[:,:,0,0]=fl[:,:,0]*9;B[:,:,0,1]=B[:,:,1,0]=fl[:,:,1]*9;B[:,:,0,2]=B[:,:,2,0]=fl[:,:,2]*3;B[:,:,1,1]=fl[:,:,3]*9;B[:,:,1,2]=B[:,:,2,1]=fl[:,:,4]*3;B[:,:,2,2]=fl[:,:,5];TR=get_trees();masks=np.sum(np.uint64(1)<<TR.astype(np.uint64),axis=1);covered=np.zeros(48790,bool);certs=[];failed=[];path=Path('h5_taper_progress_'+str(lo).replace('/','_')+'_'+str(hi).replace('/','_')+'.json');start=monotonic()
 if path.exists():
  old=json.loads(path.read_text());assert old['basal']==list(basal) and old['interval']==[str(lo),str(hi)] and old['scale']==L;certs=old['certificates'];failed=old['failed']
  for cert in certs:
   inds=np.array([i for i,w in cert]);weights=np.array([w for i,w in cert]);assert all(pd(row)for row in np.einsum('i,ijk->jk',weights,T[inds]));cm=sum(1<<int(i)for i,w in cert);covered|=(masks&np.uint64(cm))==np.uint64(cm)
  covered[failed]=True
 for k in range(limit):
  left=np.where(~covered)[0]
  if not len(left):break
  ti=int(left[0]);cert=locator(B,TR[ti],T)
  if cert is None:failed.append(ti);covered[ti]=True
  else:
   certs.append(cert);cm=sum(1<<i for i,w in cert);covered|=(masks&np.uint64(cm))==np.uint64(cm)
  out={'basal':basal,'interval':[str(lo),str(hi)],'scale':L,'certificates':certs,'failed':failed,'covered_including_failed':int(sum(covered))};path.write_text(json.dumps(out,separators=(',',':'))+'\n')
  if k%50==0:print('cert',len(certs),'fail',len(failed),'covered',sum(covered),'seconds',monotonic()-start,flush=True)
 print('END',path,len(certs),len(failed),sum(covered),monotonic()-start,flush=True)
if __name__=='__main__':run(('9/20','1/50','4/5','1/10'),sys.argv[1],sys.argv[2],int(sys.argv[3])if len(sys.argv)>3 else 1000)
```

### h5_verify_taper.py

```python
"""Independent exact polynomial/all-tree verifier; CPython 3.13.5 stdlib.
Needs h5_normal_cone.py and the three regenerated literal certificate JSONs.
It does not import the numerical locator or trust its coverage bookkeeping.
"""
from h5_normal_cone import *
from math import comb
BASAL=tuple(map(F,('9/20','1/50','4/5','1/10')))
CELLS=((F(0),F(1,3)),(F(1,3),F(2,3)),(F(2,3),F(1)))

def trim(p):
 p=list(p)
 while len(p)>1 and p[-1]==0:p.pop()
 return tuple(p)
def pc(x):return (F(x),)
def pa(*ps):
 n=max(map(len,ps));return trim([sum((p[k] if k<len(p) else 0 for p in ps),F(0)) for k in range(n)])
def ps(p,a):return trim([a*x for x in p])
def pm(p,q):
 out=[F(0)]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  for j,b in enumerate(q):out[i+j]+=a*b
 return trim(out)
def padd(a,b):return tuple(pa(x,y) for x,y in zip(a,b))
def psub(a,b):return tuple(pa(x,ps(y,-1)) for x,y in zip(a,b))
def pdot(a,b):return pa(*(pm(x,y) for x,y in zip(a,b)))
def pcross(a,b):return tuple(pa(pm(a[i],b[j]),ps(pm(a[j],b[i]),-1)) for i,j in ((1,2),(2,0),(0,1)))
def pscale(a,b):return tuple(pm(x,b) for x in a)

def polynomials():
 x,r,p,q=BASAL;zero=pc(0);one=pc(1);la=(F(0),F(1));s=(F(1),F(-1))
 basal=((F(1,4),0),(1-3*x/4,0),(1-p,p),(q,1-q),(0,1-3*r/4),(0,F(1,4)),(F(1,16),F(1,16)))
 z=tuple((ps(s,a),ps(s,b),zero) for a,b in basal)+((zero,zero,one),(la,zero,one),(zero,la,one))
 D=zero;K=(zero,zero,zero)
 for f in FACETS:
  for j in range(1,len(f)-1):
   a,b,c=(z[i] for i in (f[0],f[j],f[j+1]));d=pdot(a,pcross(b,c));D=pa(D,d);K=padd(K,pscale(padd(padd(a,b),c),ps(d,F(1,4))))
 A=(31-24*x*p-24*r*q)/64;bx=F(509,3072)-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8;by=F(509,3072)-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
 ss=pm(s,s);lll=pm(la,la);sss=pm(ss,s);ssl=pm(ss,la)
 assert D==pa(la,ps(ss,2*A))
 assert K==(pa(ps(sss,3*bx/2),ps(ssl,(1-3*x*p/4)/4),ps(lll,F(1,4))),pa(ps(sss,3*by/2),ps(ssl,(1-3*r*q/4)/4),ps(lll,F(1,4))),pa(ps(ss,A/2),ps(la,F(1,2)),ps(lll,F(1,4))))
 out=[]
 for i,j in ARROWS:
  a=psub(pscale(z[i],D),K);b=psub(z[i],z[j])
  rows=tuple(ps(pa(pm(a[h],b[k]),pm(a[k],b[h])),F(1,2)) for h,k in ((0,0),(0,1),(0,2),(1,1),(1,2),(2,2)))
  assert max(map(len,rows))<=5;out.append(rows)
 return out

def bern(p,lo,hi):
 powers=[sum((p[j]*comb(j,k)*lo**(j-k)*(hi-lo)**k for j in range(k,len(p))),F(0)) for k in range(5)]
 coeff=tuple(sum((powers[k]*F(comb(i,k),comb(4,k)) for k in range(i+1)),F(0)) for i in range(5))
 # Independent full power reconstruction in the normalized interval variable.
 back=[F(0)]*5
 for i,c in enumerate(coeff):
  for j in range(5-i):back[i+j]+=c*comb(4,i)*comb(4-i,j)*(-1)**j
 assert back==powers
 return coeff

def exact_table(polys,lo,hi):
 table=[]
 for row in polys:
  cols=[bern(p,lo,hi) for p in row];table.append(tuple(tuple(c[k] for c in cols) for k in range(5)))
 L=lcm(*(v.denominator for rows in table for row in rows for v in row))
 return tuple(tuple(tuple(int(L*v) for v in row) for row in rows) for rows in table),L

def sylvester(row):
 a,b,c,d,e,f=row;return (a,a*d-b*b,a*d*f+2*b*c*e-a*e*e-d*c*c-f*b*b)

def rooted_masks():
 ai={e:k for k,e in enumerate(ARROWS)};masks=[];unrooted=0
 for es in combinations(EDGES,9):
  adj=[[] for _ in range(10)]
  for i,j in es:adj[i].append(j);adj[j].append(i)
  for root in range(10):
   par={root:root};queue=[root]
   for j in queue:
    for i in adj[j]:
     if i not in par:par[i]=j;queue.append(i)
   if len(par)!=10:break
   if root==0:unrooted+=1
   masks.append(sum(1<<ai[i,par[i]] for i in range(10) if i!=root))
 assert (unrooted,len(masks),len(set(masks)))==(4879,48790,48790)
 return masks

def verify():
 polys=polynomials();trees=rooted_masks();rows=[];gap=None;total=0;unique=set();max_weight=0;max_sum=0
 for lo,hi in CELLS:
  name='h5_taper_progress_'+str(lo).replace('/','_')+'_'+str(hi).replace('/','_')+'.json';raw=Path(name).read_bytes();data=json.loads(raw)
  assert tuple(map(F,data['basal']))==BASAL and tuple(map(F,data['interval']))==(lo,hi)
  table,L=exact_table(polys,lo,hi);assert data['scale']==L
  masks=[];small=[None]*3;cellgap=None
  for cert in data['certificates']:
   assert cert and len({i for i,w in cert})==len(cert) and all(type(i) is int and 0<=i<34 and type(w) is int and w>0 for i,w in cert)
   W=sum(w for i,w in cert);max_sum=max(max_sum,W);max_weight=max(max_weight,max(w for i,w in cert));unique.add(tuple(map(tuple,cert)))
   for k in range(5):
    row=tuple(sum(w*table[i][k][h] for i,w in cert) for h in range(6));mm=sylvester(row);assert min(mm)>0
    for h,v in enumerate(mm):small[h]=v if small[h] is None else min(small[h],v)
    tr=row[0]+row[3]+row[5];delta=F(4*mm[2],L*tr*tr*W);cellgap=delta if cellgap is None else min(cellgap,delta)
   masks.append(sum(1<<i for i,w in cert))
  uncovered=sum(not any(t&m==m for m in masks) for t in trees);assert uncovered==0
  assert data['failed']==[] # Extra consistency check; not used to prove coverage.
  total+=len(masks);gap=cellgap if gap is None else min(gap,cellgap)
  rows.append({'interval':(lo,hi),'certificates':len(masks),'coefficient_scale':L,'minimum_leading_minors':small,'normalized_stress_gap':cellgap,'uncovered_rooted_trees':uncovered,'file':name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
 power=0
 while F(1,2**power)>gap:power+=1
 dyadic=F(1,2**power);radius=dyadic/256
 assert radius<=F(1,1000) and 90*radius<gap/2
 # Exact constants used in the actual-volume-centroid perturbation proof.
 assert 2*F(387,14)**2+F(120,7)**2<43**2
 assert F(7,32)>0 and 48**2*3<84**2
 out={'identity':'H5_OFF_MACRO_ALL_TAPER_ACTUAL_CENTROID_TUBE_V1','basal_center':BASAL,'cells':rows,'unrooted_trees':4879,'rooted_trees_per_cell':48790,'certificate_uses':total,'distinct_certificates':len(unique),'positive_coefficient_matrices':5*total,'positive_leading_minors':15*total,'maximum_weight':max_weight,'maximum_weight_sum':max_sum,'exact_normalized_cleared_stress_gap':gap,'dyadic_gap':dyadic,'basal_maxnorm_radius':radius,'actual_physical_stress_gap_after_perturbation':dyadic/2,'verdict':'PASS','scope':'All four basal parameters in the stated closed cube; every 0<lambda<1; every common SPD metric; genuine U>=2 even allowing weak contacts. Endpoint indexed matrices only. No entire-H5 or E17 claim.'}
 raw=(json.dumps(encoded(out),indent=2,sort_keys=True)+'\n').encode();Path('h5_taper_report.json').write_bytes(raw);print(raw.decode());print('REPORT',len(raw),hashlib.sha256(raw).hexdigest());print('H5_OFF_MACRO_ALL_TAPER_ACTUAL_CENTROID_TUBE_EXACT_PASS')
 return out
if __name__=='__main__':verify()
```

Convenience copy: [complete source-and-output capsule](sandbox:/mnt/data/h5_frontier_capsule.zip).
