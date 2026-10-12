# minimum-0254

AI research report · 2026-09-26 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# H5_ACTUAL_COVARIANCE_CAP48_ALLROOT_MACRO_EXCLUSION_V1

## 1. Result

**A new four-dimensional basal box is excluded from proper110 for the entire taper, using the full actual-covariance-conditioned common-metric cone.** The new exact atlas covers all 48,790 rooted true-edge trees, not just trees containing a particular packet.

Define the basal domain

```text
B_new:
  3/5  <= x <= 7/10,
  7/10 <= r <= 4/5,
  3/4  <= p <= 17/20,
  1/20 <= q <= 3/20,
  p+q < 1.
```

The newly certified statement is:

> For every literal actual-centroid H5 body with basal parameters in B_new and 0<lambda<=3/5, every SPD metric M satisfying
> `condition(Sigma^(1/2) M Sigma^(1/2)) <= 48`
> has at least two **strict** unstable vertices. Sigma is that same body's actual uniform-volume covariance. Incidental weak contacts are allowed.

The certificate is quantitative. Normalize `tr(Sigma M)=1`. For **every** rooted true-edge tree, one of the atlas's positive-weight packets contained in that tree satisfies

```text
sum_e w_e D_e(M) / sum_e w_e <= -2^(-33),
D_(i,j)(M) = (Z_i-g)^T M (Z_j-Z_i).
```

Thus every rooted tree has an original arrow with derivative at most `-2^(-33)`.

The supplied finite-height theorem puts every joint S1/U1 candidate inside the strict covariance-weighted cap48; this is not a restriction on arbitrary U1 metrics. Consequently the atlas excludes S=U=1, even with additional weak rests, on its stated region. Combining it with the accepted all-basal, all-metric `lambda>=3/5` exclusion removes **all 0<lambda<1** over B_new. The upper-taper result is an inherited premise, not a new replay.

The coordinate reflection `(x,r,p,q)->(r,x,q,p)` gives the reflected basal box as well. Its vertex permutation is `(5,4,3,2,1,0,6,7,9,8)`, together with interchange of the first two spatial coordinates. This preserves the covariance-weighted condition number and the actual mechanics. Reflection is a theorem consequence, not a second independently counted atlas.

Both boxes are outside the named all-taper macro/reflection and the off-macro tiny tube in the assignment. The central shape A is now covered as part of a complete common-metric regional exclusion, rather than only through the parent's four- or five-arrow containment counts.

**No whole-H5 or whole-E17 exclusion, proper110 construction, canonical-registry subtraction, or global minimum-bound improvement follows.** The accepted bounds remain `34<=C_min<=622`.

## 2. Source authority and reading

I read all supplied new sources and the entire 362170-byte journal through EOF, including the complete branch memory and both literal parents. The four new file manifests matched:

```text
H5_CONDITIONED_FIVE_ARROW_AND_INDEFINITE_STRESS_V1.md
12381 bytes
38da6f51cf9c20311135a3485de074668c1e230d613e4cea7f8d3ec5960baa97

h5_conditioned_packet.py.txt
7819 bytes
e4a124f9605d1af7d05e74a4c12bf5044fb9ac20b2d18b42d50bffd89484bad0

H5_CONDITIONED_PACKET_DISCOVERY_V1.md
5101 bytes
913791c4e5632e54d7ba099157688b8e8433e76bc25630558398d8b19c8442dd

research-journal(20260926-202706).md
362170 bytes
86b2bb989531536618508261c8fcbdd86dffa69e32b8321fd1ea22ddd67a76be
```

The literal parent envelopes also reproduced their registered hashes:

```text
minimum-0251
41387-byte version-2 envelope
c6740ff1f093f61efe88b3be1e4fbc19f4163ffa98e8ce686fb621ac0237d252

minimum-0252
34704-byte version-2 envelope
c166ef43daf3b0236b4e6c5360246aaf15fec13adfb79c3a1f22541c4d49bce9
```

For this check, each titled parent Markdown payload was stripped of trailing whitespace, given one final LF, and serialized with `json.dumps({'version':2,'result_markdown':text},ensure_ascii=False,separators=(',',':'))`. No incidence, centroid, or source-identity conflict was found. There is no missing computational dependency for the new result. Earlier exclusion theorems and the necessary finite-height cap are used as the supplied accepted premises.

## 3. The actual geometry and a linear conditioned-stress certificate

### 3.1 One body supplies every quantity

For `s=1-lambda`, the ten vertices are

```text
Z0 = (s/4,0,0)
Z1 = (s*(1-3*x/4),0,0)
Z2 = (s*(1-p),s*p,0)
Z3 = (s*q,s*(1-q),0)
Z4 = (0,s*(1-3*r/4),0)
Z5 = (0,s/4,0)
Z6 = (s/16,s/16,0)
Z7 = (0,0,1)
Z8 = (lambda,0,1)
Z9 = (0,lambda,1).
```

The nine maximal facet cycles are

```text
(6,5,4,3,2,1,0), (8,7,0,1), (7,6,0), (1,2,8),
(9,8,2,3), (9,3,4), (4,5,7,9), (6,7,5), (7,8,9).
```

Only consecutive pairs in these cycles define the seventeen mechanical edges. The boundary fan triangulations are used for integration, not for adding mechanical edges.

For each oriented integration triangle `(a,b,c)`, put `d=a dot (b cross c)` and `u=a+b+c`. The exact moment sums are

```text
D = sum d,
K = sum d*u/4,
J = sum d*(u*u^T+a*a^T+b*b^T+c*c^T)/20,
Volume = D/6,
g = K/D,
Sigma = J/D-g*g^T.
```

They integrate the full uniformly filled body. Every occurrence of g, Sigma, an arrow tensor, or a pole in the recovery uses these same moments. Signed boundary integration remains valid after the fixed translation used to condition a cell's arithmetic.

### 3.2 A certificate subclass that separates the entire conditioned metric cone

Let

```text
A_e = sym((Z_i-g)(Z_j-Z_i)^T),
Q = -sum_e w_e A_e,     w_e>=0,
t = tr(Sigma^-1 Q),
P_minus = (t/144)*Sigma,
P_plus = Q+P_minus.
```

**Lemma. If P_plus is positive definite, these weights reject all selected weak arrows for every metric in the closed actual-covariance cap48.**

Proof: the exact trace identity is

```text
tr(Sigma^-1 P_plus) = (49/48)*t.
```

Its left side is positive, so `t>0` and `P_minus>0`. Moreover

```text
tr(Sigma^-1(P_plus-48*P_minus)) = t/48 > 0.
```

For any metric in the closed cap, some `tau>0` satisfies

```text
tau*Sigma^-1 <= M <= 48*tau*Sigma^-1.
```

Therefore

```text
tr(MQ)
 = tr(MP_plus)-tr(MP_minus)
 >= tau*tr(Sigma^-1(P_plus-48*P_minus))
 = tau*t/48 > 0.
```

Selected weak exits instead imply `tr(MQ)=-sum w_e D_e<=0`. This is a contradiction.

The lemma is a convenient subclass of the supplied complete `P-N` dual certificate system. It does **not** restrict the physical metric to an isotropic metric. Only the certificate's negative part is chosen proportional to the actual covariance. That negative part is unrelated to the physical inverse metric used for equilibrium censuses.

The useful implementation point is linearity in the arrow weights:

```text
B_e(theta) = -A_e(theta)
             - tr(Sigma(theta)^-1 A_e(theta))*Sigma(theta)/144,
P_plus(theta) = sum_e w_e B_e(theta).
```

Individual B_e need not be positive and their individual trace coefficients need not be positive. Positivity is required only for the selected weighted sum. The original common G, shear and positive normal height are all retained through the full SPD metric cone; no eta contraction or fixed-G slice is used.

## 4. Exact five-variable certification and complete tree coverage

### 4.1 The certified object is not a collection of corner samples

Each of the four basal intervals is bisected once, giving sixteen closed basal subboxes. The taper interval `[0,3/5]` is adaptively bisected separately above each subbox. The resulting atlas has **501 closed five-dimensional boxes**.

On each box, the source first computes its exact midpoint covariance and an invertible rational congruence C using exact LDL and 24-bit dyadic inverse-square-root approximations. The approximation's accuracy is not a proof premise: invertibility is sufficient. It is a certificate-coordinate change, not a chosen physical metric. The source then recomputes the **moving** volume, centroid, covariance and arrows on `C*(Z-g_mid)`.

Every scalar is enclosed by an 80-bit outward-dyadic affine Taylor model

```text
f(xi) = c + sum_j a_j*xi_j + R(xi),     -1<=xi_j<=1,
```

with interval coefficients and an interval remainder. Addition and multiplication retain complete remainder bounds. Reciprocals use the exact identity

```text
1/(c+z) = 1/c - z/c^2 + z^2/(c^2*(c+z)).
```

Every divisor interval used is checked away from zero; the volume and covariance-determinant bounds are strictly positive. Thus these models include all higher-order dependence on the five physical shape parameters.

For each symmetric B_e, the interval remainders and coefficient-rounding errors give entrywise error bounds. Their maximum absolute row sum supplies a scalar `r_e` such that the exact field dominates an affine symmetric model minus `r_e I`. Evaluating that **lower affine model** at its 32 normalized corners gives integer matrices with common scale `2^80`.

For every accepted packet, all 32 positive-weight corner sums are PD by exact Sylvester minors. Since an affine function on a box is the convex interpolation of its corner values, the lower model is PD everywhere; the exact moving P_plus is then PD everywhere too. These are corners of a rigorous Taylor lower model, **not 32 samples of the nonlinear body**.

The labelled endpoint matrices at `lambda=0` and at `p+q=1` are included in the enclosures. They are not asserted to be genuine ten-vertex H5 bodies. The theorem on mechanics uses `lambda>0` and `p+q<1`, where the stated chart has its true nine facets and seventeen edges.

### 4.2 Quantitative trace guard

For an integer PD corner matrix R, the source uses

```text
lambda_min(R) >= 4*det(R)/(tr(R))^2.
```

After division by the dyadic scale and weight sum, let delta be the minimum resulting bound for a cell. Let R_Sigma be its rigorously enclosed covariance operator-norm upper bound in the same congruence. For every used packet throughout that cell,

```text
P_plus / sum w >= delta*I,
tr(Sigma^-1(P_plus-48*P_minus)) / sum w
    >= 3*delta/(49*R_Sigma) > 0.
```

With `tr(Sigma M)=1` and covariance-weighted condition at most48, the smallest eigenvalue of `Sigma^(1/2) M Sigma^(1/2)` is at least `1/97`. Consequently the normalized negative arrow mean is bounded away from zero by

```text
3*delta/(49*97*R_Sigma).
```

Taking the exact minimum over the entire atlas proves the advertised dyadic guard `2^(-33)`. Neither floating eigenvalues nor a numerical feasibility tolerance enters this guard.

### 4.3 Coverage and executed totals

The verifier enumerates all nine-edge subsets of the actual seventeen-edge graph, retains the connected subsets, and orients each toward every root. It independently checks the Kirchhoff cofactor count4879. The resulting 48790 rooted trees are covered in **every** cell by literal support inclusion. No tree is dropped using a historical canonical catalogue, a norm-only rule, or a feasibility guess.

If U=1, every other vertex has a nonnegative true-edge exit. Every such exit strictly increases squared metric norm, because `|Z_j-g|_M^2-|Z_i-g|_M^2=2D_(i,j)+|Z_j-Z_i|_M^2>0`. Selecting one exit per nonroot therefore gives a rooted tree directed to the unique U. The atlas rejects that tree. A farthest vertex always supplies a strict U, so the conclusion is U>=2 rather than merely U!=1.

The verifier also reconstructs the sixteen basal subboxes and checks that each one's taper intervals abut exactly from0 to3/5. All shared walls are included. It does not trust the generator's coverage counters or subdivision-success flags.

```text
Closed five-dimensional cells                 501
Fixed basal subboxes                          16
Distinct positive-integer weight certificates 1728
Certificate uses                              152170
PD Taylor-corner matrices                     4869440
Positive leading principal minors            14608320
Rooted trees checked per cell                 48790
Raw rooted-tree/cell combinations              24443790
Maximum integer weight                        3786
Maximum weight sum                            10000
Uniform normalized negative-arrow guard       2^(-33)
```

The taper-cell counts, in lexicographic order of the four binary basal subdivision indices, are the complete tuple

```text
(24,29,30,31,25,29,30,32,27,32,34,40,27,34,35,42).
```

The distinct-certificate support histogram is

```text
3 arrows:405, 4 arrows:761, 5 arrows:483, 6 arrows:76, 7 arrows:3.
```

The uniform six- and seven-row certificates do not contradict the pointwise five-arrow theorem. A single certificate valid on a shape box need not inherit the smallest support available separately at each shape.

The proposal generator made3067 LP calls and processed986 subdivision nodes. Its174 enclosure splits and311 locator splits are subdivisions, not infeasibility verdicts. Complete coverage is established solely by the independently recomputed exact guards and graph enumeration.

## 5. A retained actual three-arrow countercontrol

The atlas method has a genuine conditioned-versus-unrestricted distinction. At the parent's exact shape A,

```text
theta=(13/20,3/4,4/5,1/10,3/10),
Volume=22241/240000,
g=(18537583/142342400,13363403/71171200,37841/88964),
```

take the three arrows and weights

```text
7->0 :31,
8->7 :24,
9->4 :45.
```

For their actual centered stress Q and actual covariance Sigma, define P_plus and P_minus by Section3. Both are exactly PD. The stress is genuinely indefinite, for example

```text
Q_yy = -71891613/2277478400 < 0,
Q_zz = 971337/22241 > 0.
```

The exact cap48 trace gap is

```text
1054167029231844234504783125045 /
56058839549688184339881355743 > 0.
```

Nevertheless the unrestricted physical metric

```text
M_star = [[4,17,1],[17,9993,26],[1,26,4]]/10000
```

is SPD and realizes all three arrows strictly. Its leading principal minors are

```text
1/2500, 39683/100000000, 146919/1000000000000.
```

Its three derivatives, in the packet order, are

```text
6161464461/28468480000000,
413847531/7117120000000,
1983267197/9902080000000.
```

The exact pairing is

```text
tr(M_star Q) = -3898559639031/227747840000000 < 0.
```

Thus no nonzero PSD negative weighted stress can reject this unrestricted three-arrow packet. The conditioned certificate does reject it. In particular `M_star` has actual-covariance-weighted condition greater than48; that strict conclusion follows without estimating its eigenvalues.

The full physical audit uses its **actual inverse**, all nine maximal facets and all seventeen true edges:

```text
strict (S,U,H) = (3,2,3),
S facets = (0,3,6),
U vertices = (0,3),
H edges = ((1,2),(4,5),(8,9)),
physical weak points = 0,
zero primitives = 0 of68.
```

The recovery produces all coordinates, volume moments, poles, inverse entries, 68 signed primitives, P/N minors and the trace gap. This is a new metric/control at the unchanged shape A, **not** a U1 body, a conditioned full-tree survivor, or a proper110 example. No minimal-three-packet claim is made.

## 6. Execution, recovery pins, and remaining scope

The numerical program only proposes integer weights. The exact verifier uses CPython3.13.5's standard library, asserts every accepted matrix and guard, reconstructs actual moments, and proves complete cell/tree coverage. I executed the build and verification, then regenerated from a fresh directory containing only the four sources below and verified again. The atlas, exact report, physical countercontrol and optional rationalized-control output were byte-identical. The analytic certificate/Taylor argument is not claimed to be proof-assistant formalized.

Save all four source blocks with their final LF in a fresh directory. Required reconstruction commands are

```sh
OPENBLAS_NUM_THREADS=1 python -B h5_cap48_search.py build
python -B -S h5_cap48_verify.py
```

The search uses NumPy2.3.5 and SciPy1.17.0, with one OpenBLAS thread and no random seed. Its exact input domain, dyadic precisions, LP limits, rounding denominators and traversal order are all in the source. For bounded execution batches, repeat `python -B h5_cap48_search.py step 20`; the saved stack resumes the same deterministic computation. Batching does not change the final data. No historical certificate file or parent import is needed.

The optional fourth source reproduces the new metric proposal from its literal three-arrow input:

```sh
OPENBLAS_NUM_THREADS=1 python -B h5_cap48_control_locator.py
```

Numerical choices need not be byte-identical on other solver stacks. The exact acceptance test remains authoritative; the pinned stack was cold-rebuilt successfully.

```text
SOURCE PINS
h5_cap48_core.py 7925 bytes
f557083d51b3db6a72359276741764450fb1c79bf188a8f2b409aacf5361f32b
h5_cap48_search.py 5413 bytes
411a531db55df959d723a5f4e28674b5bde127d44d9208bc53982a54040528e9
h5_cap48_verify.py 9794 bytes
7658197ea6e0911bfe9b0ae6ad9d82cce14ff7467456101a7a37665c2b9fda8a
h5_cap48_control_locator.py 2083 bytes
271d446808dc803f266ffb944f384dcf9aea7d11771376dc72840dec041a9678

OUTPUT PINS
h5_cap48_atlas.json 712720 bytes
93ce334dae0174b0cbc647a7d5eae8acb33a90f71dd2cb3c92320f5519da3edb
h5_cap48_report.json 741377 bytes
55c42065441dadf6838c17e884ebaefa4ee795c4c021d0e7a6569e9f243cd925
h5_cap48_countercontrol.json 12954 bytes
39e172b283544c93221c3aec38a0360e92efae53df1c2eefb7c72ce96269fdef
h5_cap48_control_proposal.json 297 bytes
ddcb12439cdf094e8ed30b7ac16a09ca8202b28d584a62d46bd4a35813d5c9b8

EXACT RECOMPUTED INTEGER TAYLOR-TABLE STREAM SHA256
ad6f80df739cbd3d36fd5986e8e700f00120ae8ef2ea695ba1d13bad05a78543

EXPECTED MARKERS
CHECKPOINT COMPLETE_UNVERIFIED 501 1728 712720
H5_ACTUAL_COVARIANCE_CAP48_ALLROOT_MACRO_EXACT_PASS
H5_CAP48_COUNTERCONTROL_RATIONALIZED_PASS
```

The generator deliberately labels its output `COMPLETE_UNVERIFIED`; only the independent verifier's report carries `EXACT_PASS`. Timing lines are not pinned.

Relative to the exclusion map supplied in the assignment, the remaining region is `1/400000<lambda<3/5` outside the inherited exclusions **and outside B_new and its reflection**. Nothing here decides the remaining actual shapes. The most useful continuation is to reuse the complete integer library and moving-covariance verifier on adjacent basal boxes, or enlarge the dual class beyond covariance-proportional negative parts when that conservative class stalls. Such a stall is not evidence for a surviving physical tree.

## 7. Complete runnable source

### h5_cap48_core.py

```python
"""Exact H5 moving-covariance/cap48 atlas core; CPython 3.13.5 stdlib.
Geometry authority: minimum-0251,
c6740ff1f093f61efe88b3be1e4fbc19f4163ffa98e8ce686fb621ac0237d252.
Conditioned dual authority: H5_CONDITIONED_FIVE_ARROW_AND_INDEFINITE_STRESS_V1,
38da6f51cf9c20311135a3485de074668c1e230d613e4cea7f8d3ec5960baa97.
"""
from fractions import Fraction as F
from itertools import combinations,product
from pathlib import Path
from math import gcd,lcm,isqrt
import hashlib,json
FACETS=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
        (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
EDGES=tuple(sorted({tuple(sorted((f[k],f[(k+1)%len(f)])))
                    for f in FACETS for k in range(len(f))}))
ARROWS=tuple(sorted(e for i,j in EDGES for e in ((i,j),(j,i))))
ADJ=tuple(tuple(j for a,j in ARROWS if a==i) for i in range(10))
EF=tuple(tuple(k for k,f in enumerate(FACETS) if i in f and j in f)
         for i,j in EDGES)
DUAL=tuple(sorted(e for i,j in EF for e in ((i,j),(j,i))))
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def mv(M,a):return tuple(dot(r,a) for r in M)
def bil(a,M,b):return dot(a,mv(M,b))
def mat(r):
 a,b,c,d,e,f=r;return ((a,b,c),(b,d,e),(c,e,f))
def minors(M):
 a,b,c=M[0];_,d,e=M[1];_,_,f=M[2]
 return a,a*d-b*b,a*d*f+2*b*c*e-a*e*e-d*c*c-f*b*b

def inv(M):
 a,b,c=M[0];_,d,e=M[1];_,_,f=M[2];det=minors(M)[2]
 assert det>0
 N=tuple(tuple(x/det for x in r) for r in
         ((d*f-e*e,c*e-b*f,b*e-c*d),(c*e-b*f,a*f-c*c,b*c-a*e),
          (b*e-c*d,b*c-a*e,a*d-b*b)))
 assert all(sum(M[i][k]*N[k][j] for k in range(3))==int(i==j)
            for i in range(3) for j in range(3))
 return N

def trees():
 ai={e:k for k,e in enumerate(ARROWS)};out=[]
 for es in combinations(EDGES,9):
  adj=[[] for _ in range(10)]
  for i,j in es:adj[i].append(j);adj[j].append(i)
  for root in range(10):
   p={root:root};queue=[root]
   for j in queue:
    for i in adj[j]:
     if i not in p:p[i]=j;queue.append(i)
   if len(p)!=10:break
   out.append((root,tuple(sorted(ai[i,p[i]] for i in range(10) if i!=root))))
 assert len(out)==48790 and len(set(out))==48790
 return out

BITS=80; UNIT=1<<BITS; DIM=5; CAP=48

def floorq(x):return x.numerator//x.denominator

def ceilq(x):return -((-x.numerator)//x.denominator)
class I:
 __slots__=('lo','hi')
 def __init__(self,x=0,hi=None,raw=False):
  if raw:self.lo,self.hi=int(x),int(hi)
  else:
   x=F(x)*UNIT;self.lo,self.hi=floorq(x),ceilq(x)
 def __add__(a,b):
  if not isinstance(b,I):b=I(b)
  return I(a.lo+b.lo,a.hi+b.hi,True)
 __radd__=__add__
 def __neg__(a):return I(-a.hi,-a.lo,True)
 def __sub__(a,b):return a+-b if isinstance(b,I) else a+I(-b)
 def __rsub__(a,b):return I(b)+-a
 def __mul__(a,b):
  if not isinstance(b,I):b=I(b)
  v=(a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi)
  return I(min(v)//UNIT,-((-max(v))//UNIT),True)
 __rmul__=__mul__
 def rec(a):
  assert a.lo*a.hi>0,('zero denominator',a.lo,a.hi)
  return I((UNIT*UNIT)//a.hi,-((-UNIT*UNIT)//a.lo),True)
 def __truediv__(a,b):return a*(b.rec() if isinstance(b,I) else I(b).rec())
 def __rtruediv__(a,b):return I(b)*a.rec()
 def square(a):
  v=max(a.lo*a.lo,a.hi*a.hi);m=0 if a.lo<=0<=a.hi else min(a.lo*a.lo,a.hi*a.hi)
  return I(m//UNIT,-((-v)//UNIT),True)
 def mag(a):return max(abs(a.lo),abs(a.hi))

class T:
 __slots__=('c','lin','rem')
 def __init__(self,c=0,lin=None,rem=None):
  self.c=c if isinstance(c,I) else I(c);self.lin=[I(0) for _ in range(DIM)] if lin is None else lin;self.rem=I(0) if rem is None else rem
 @classmethod
 def variable(cls,c,r,j):
  a=cls(c);a.lin[j]=I(r);return a
 def __add__(a,b):
  if not isinstance(b,T):b=T(b)
  return T(a.c+b.c,[x+y for x,y in zip(a.lin,b.lin)],a.rem+b.rem)
 __radd__=__add__
 def __neg__(a):return T(-a.c,[-x for x in a.lin],-a.rem)
 def __sub__(a,b):return a+(-b if isinstance(b,T) else -T(b))
 def __rsub__(a,b):return T(b)+-a
 def lbound(a):
  m=sum(x.mag() for x in a.lin);return I(-m,m,True)
 def bound(a):return a.c+a.lbound()+a.rem
 def __mul__(a,b):
  if not isinstance(b,T):b=T(b)
  return T(a.c*b.c,[a.c*y+b.c*x for x,y in zip(a.lin,b.lin)],a.c*b.rem+b.c*a.rem+(a.lbound()+a.rem)*(b.lbound()+b.rem))
 __rmul__=__mul__
 def rec(a):
  c2=a.c.square();z=a.lbound()+a.rem
  return T(1/a.c,[-x/c2 for x in a.lin],-a.rem/c2+z.square()/(c2*a.bound()))
 def __truediv__(a,b):return a*(b.rec() if isinstance(b,T) else T(b).rec())
 def __rtruediv__(a,b):return T(b)*a.rec()

PAIRS=((0,0),(0,1),(0,2),(1,1),(1,2),(2,2))
def rawverts(theta):
 x,r,p,q,la=theta;s=1-la
 B=((F(1,4),0),(1-3*x/4,0),(1-p,p),(q,1-q),(0,1-3*r/4),(0,F(1,4)),(F(1,16),F(1,16)))
 return tuple((s*a,s*b,0*la) for a,b in B)+((0*la,0*la,0*la+1),(la,0*la,0*la+1),(0*la,la,0*la+1))

def generic_moments(Z):
 D=0;K=[0]*3;J=[[0]*3 for _ in range(3)]
 for f in FACETS:
  for k in range(1,len(f)-1):
   a,b,c=(Z[j] for j in (f[0],f[k],f[k+1]));d=dot(a,cross(b,c));t=tuple(a[j]+b[j]+c[j] for j in range(3));D+=d
   for i in range(3):
    K[i]+=d*t[i]/4
    for j in range(3):J[i][j]+=d*(t[i]*t[j]+a[i]*a[j]+b[i]*b[j]+c[i]*c[j])/20
 g=tuple(x/D for x in K);S=tuple(tuple(J[i][j]/D-g[i]*g[j] for j in range(3)) for i in range(3))
 return D,g,S

def whiten(S):
 # Exact LDL with deterministic dyadic inverse-square-root approximations.
 L=[[F(i==j) for j in range(3)] for i in range(3)];d=[]
 for j in range(3):
  dj=S[j][j]-sum(L[j][k]**2*d[k] for k in range(j));assert dj>0;d.append(dj)
  for i in range(j+1,3):L[i][j]=(S[i][j]-sum(L[i][k]*L[j][k]*d[k] for k in range(j)))/dj
 Li=((F(1),F(0),F(0)),(-L[1][0],F(1),F(0)),(L[2][1]*L[1][0]-L[2][0],-L[2][1],F(1)))
 scales=[F(isqrt(((1<<24)**2*x.denominator)//x.numerator),1<<24) for x in d]
 assert min(scales)>0
 return tuple(tuple(scales[i]*Li[i][j] for j in range(3)) for i in range(3))

def adj(M):
 a,b,c=M[0];_,d,e=M[1];_,_,f=M[2]
 return ((d*f-e*e,c*e-b*f,b*e-c*d),(c*e-b*f,a*f-c*c,b*c-a*e),(b*e-c*d,b*c-a*e,a*d-b*b))

def compile_box(lo,hi):
 from itertools import product
 lo,hi=tuple(map(F,lo)),tuple(map(F,hi));mid=tuple((a+b)/2 for a,b in zip(lo,hi));rad=tuple((b-a)/2 for a,b in zip(lo,hi))
 assert min(rad)>0 and all(0<=lo[k]<hi[k]<=1 for k in range(5)) and hi[2]+hi[3]<=1
 Z0=rawverts(mid);D0,g0,S0=generic_moments(Z0);C=whiten(S0)
 theta=tuple(T.variable(a,r,j) for j,(a,r) in enumerate(zip(mid,rad)));raw=rawverts(theta)
 Z=tuple(mv(C,sub(a,g0)) for a in raw);D,g,S=generic_moments(Z);assert D.bound().lo>0
 A=adj(S);det=dot(S[0],tuple(A[j][0] for j in range(3)));assert det.bound().lo>0
 SI=tuple(tuple(a/det for a in row) for row in A);X=tuple(sub(a,g) for a in Z)
 rows=[];errors=[];corners=tuple(product((-1,1),repeat=5))
 for i,j in ARROWS:
  a=X[i];d=sub(Z[j],Z[i]);Q=tuple(tuple(-(a[k]*d[l]+a[l]*d[k])/2 for l in range(3)) for k in range(3));tau=sum(SI[k][l]*Q[k][l] for k in range(3) for l in range(3))/(3*CAP)
  P=tuple(tuple(Q[k][l]+tau*S[k][l] for l in range(3)) for k in range(3));coef=[];ee=[]
  for k,l in PAIRS:
   p=P[k][l];cs=[p.c]+p.lin;cc=[(x.lo+x.hi)//2 for x in cs];err=p.rem.mag()+sum(max(abs(x.lo-c),abs(x.hi-c)) for x,c in zip(cs,cc));coef.append(cc);ee.append(err)
  ermat=mat(ee);err=max(sum(row) for row in ermat);errors.append(err)
  blocks=[]
  for corner in corners:
   vals=[c[0]+sum(x*y for x,y in zip(c[1:],corner)) for c in coef]
   for k in (0,3,5):vals[k]-=err
   blocks.append(vals)
  rows.append(blocks)
 return rows,{'lo':list(map(str,lo)),'hi':list(map(str,hi)),'max_error':str(F(max(errors),UNIT)),'D_lower':str(F(D.bound().lo,UNIT)),'covariance_det_lower':str(F(det.bound().lo,UNIT)),'covariance_norm_upper':str(F(max(sum(S[i][j].bound().mag() for j in range(3)) for i in range(3)),UNIT))}

def ints_pd(row):
 a,b,c,d,e,f=row;return a>0 and a*d-b*b>0 and a*d*f+2*b*c*e-a*e*e-d*c*c-f*b*b>0

def exact_cert(rows,cert):
 return all(ints_pd([sum(w*rows[i][k][h] for i,w in cert) for h in range(6)]) for k in range(32))

```

### h5_cap48_search.py

```python
"""Checkpointed deterministic proposal generator. Exact verification is separate."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
from h5_cap48_core import *
import numpy as np
from scipy.optimize import linprog
from functools import reduce
from itertools import product
from time import monotonic
import sys

LOW=('3/5','7/10','3/4','1/20','0')
HIGH=('7/10','4/5','17/20','3/20','3/5')
OUT='h5_cap48_atlas.json'

def pdloc(B):
 n=len(B);planes=np.concatenate([B[:,:,k,k].T for k in range(3)])
 for it in range(70):
  res=linprog(np.r_[np.zeros(n),-1],A_ub=np.c_[-planes,np.ones(len(planes))],b_ub=np.zeros(len(planes)),A_eq=[np.r_[np.ones(n),0]],b_eq=[1],bounds=[(0,None)]*n+[(None,None)],method='highs')
  if not res.success or res.x[-1]<1e-10:return None
  w=res.x[:-1];P=np.einsum('i,ijkl->jkl',w,B);ev,U=np.linalg.eigh(P)
  if ev[:,0].min()>1e-8:return w
  for k in np.where(ev[:,0]<max(1e-8,res.x[-1]*.5))[0]:
   u=U[k,:,0];planes=np.r_[planes,np.einsum('j,ijk,k->i',u,B[:,k],u)[None,:]]
 return None

def canonical(c):
 c=[(int(i),int(w)) for i,w in c if w];g=reduce(gcd,(w for i,w in c));return tuple((i,w//g) for i,w in c)

def initial():
 lo,hi=tuple(map(F,LOW)),tuple(map(F,HIGH));stack=[]
 for ix in product(range(2),repeat=4):
  a=tuple(lo[k]+(hi[k]-lo[k])*ix[k]/2 for k in range(4))+(lo[4],)
  b=tuple(lo[k]+(hi[k]-lo[k])*(ix[k]+1)/2 for k in range(4))+(hi[4],)
  stack.append([list(map(str,a)),list(map(str,b)),0])
 return {'identity':'H5_ACTUAL_COVARIANCE_CAP48_ALLROOT_MACRO_ATLAS_V1','domain_lo':LOW,'domain_hi':HIGH,'bits':BITS,'K':CAP,'stack':list(reversed(stack)),'certificates':[],'cells':[],'nodes':0,'locator_calls':0,'splits_enclosure':0,'splits_locator':0,'status':'PARTIAL'}

def save(data):
 raw=(json.dumps(data,sort_keys=True,separators=(',',':'))+'\n').encode();Path(OUT).write_bytes(raw)
 return len(raw),hashlib.sha256(raw).hexdigest()

def step(limit=20):
 start=monotonic();data=json.loads(Path(OUT).read_text()) if Path(OUT).exists() else initial()
 assert tuple(data['domain_lo'])==LOW and tuple(data['domain_hi'])==HIGH and data['bits']==BITS and data['K']==CAP
 if data['status']=='COMPLETE_UNVERIFIED':print('ALREADY_COMPLETE');return True
 TR=trees();masks=np.array([sum(1<<i for i in tr) for r,tr in TR],np.uint64)
 lib=[tuple(map(tuple,c)) for c in data['certificates']];ids={c:j for j,c in enumerate(lib)};cm=[np.uint64(sum(1<<i for i,w in c)) for c in lib]
 for node in range(limit):
  if not data['stack']:break
  slo,shi,depth=data['stack'].pop();lo,hi=tuple(map(F,slo)),tuple(map(F,shi));data['nodes']+=1
  try:rows,info=compile_box(lo,hi)
  except AssertionError:rows=None
  failure='enclosure' if rows is None else None
  if rows is not None:
   fl=np.array(rows,float)/UNIT;B=np.zeros((34,32,3,3))
   for h,(i,j) in enumerate(PAIRS):B[:,:,i,j]=B[:,:,j,i]=fl[:,:,h]
   covered=np.zeros(len(TR),bool);chosen=[]
   if lib:
    WW=np.zeros((len(lib),34))
    for j,c in enumerate(lib):
     for i,w in c:WW[j,i]=w
    pp=(WW@B.reshape(34,-1)).reshape(len(lib),32,3,3)
    passed=np.where(np.linalg.eigvalsh(pp)[:,:,0].min(axis=1)>0)[0]
    for j0 in passed:
     j=int(j0);hit=(masks&cm[j])==cm[j]
     if np.any(hit&~covered) and exact_cert(rows,lib[j]):chosen.append(j);covered|=hit
   for k in range(2000):
    left=np.where(~covered)[0]
    if not len(left):break
    ti=int(left[0]);r,ks=TR[ti];data['locator_calls']+=1;w=pdloc(B[list(ks)])
    if w is None:failure='locator';break
    cc=None
    for den in (100,300,1000,3000,10000,30000,100000,300000,1000000,10000000,100000000):
     c=canonical([(i,round(x*den)) for i,x in zip(ks,w)])
     if exact_cert(rows,c):cc=c;break
    if cc is None:failure='locator';break
    if cc not in ids:ids[cc]=len(lib);lib.append(cc);cm.append(np.uint64(sum(1<<i for i,w in cc)))
    j=ids[cc];chosen.append(j);covered|=(masks&cm[j])==cm[j]
   else:raise RuntimeError('call limit, no conclusion')
  if failure is not None:
   if depth>=14:raise RuntimeError('taper subdivision exhausted, no conclusion')
   data['splits_'+failure]+=1;m=(lo[4]+hi[4])/2
   data['stack'].append([slo[:4]+[str(m)],shi,depth+1]);data['stack'].append([slo,shi[:4]+[str(m)],depth+1])
  else:
   assert np.all(covered)
   counts=np.zeros(len(TR),np.int32)
   for j in chosen:counts+=((masks&cm[j])==cm[j])
   keep=[]
   for j in reversed(chosen):
    hit=(masks&cm[j])==cm[j]
    if np.all(counts[hit]>1):counts[hit]-=1
    else:keep.append(j)
   assert np.all(counts>0)
   data['cells'].append({'lo':slo,'hi':shi,'certificates':sorted(keep)})
   print('CELL',len(data['cells']),'nodes',data['nodes'],'lib',len(lib),'calls',data['locator_calls'],'pending',len(data['stack']),flush=True)
 data['certificates']=lib
 if not data['stack']:
  used=sorted({j for c in data['cells'] for j in c['certificates']});remap={j:k for k,j in enumerate(used)};data['certificates']=[lib[j] for j in used]
  for c in data['cells']:c['certificates']=[remap[j] for j in c['certificates']]
  data['status']='COMPLETE_UNVERIFIED'
 count,digest=save(data);print('CHECKPOINT',data['status'],len(data['cells']),len(data['certificates']),count,digest,'seconds',monotonic()-start,flush=True)
 return not data['stack']

if __name__=='__main__':
 mode=sys.argv[1] if len(sys.argv)>1 else 'build'
 if mode=='step':step(int(sys.argv[2]) if len(sys.argv)>2 else 20)
 elif mode=='build':
  while not step(20):pass
 else:raise SystemExit('use build or step [maximum_nodes]')
```

### h5_cap48_verify.py

```python
"""Independent exact acceptance: recompute moving moments and every certificate.
CPython 3.13.5 stdlib only. No optimizer, float, saved Taylor table, or author
coverage bookkeeping is trusted. This is not proof-assistant formalization.
"""
from h5_cap48_core import *
from collections import Counter
from time import monotonic
LOW=tuple(map(F,('3/5','7/10','3/4','1/20','0')))
HIGH=tuple(map(F,('7/10','4/5','17/20','3/20','3/5')))
CONTROL_THETA=tuple(map(F,('13/20','3/4','4/5','1/10','3/10')))
CONTROL_PACKET=((21,31),(28,24),(31,45))
CONTROL_METRIC=(4,17,1,9993,26,4)


def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [enc(v) for v in x]
 return x


def write(name,x):
 raw=(json.dumps(enc(x),indent=2,sort_keys=True)+'\n').encode();Path(name).write_bytes(raw)
 return {'file':name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}


def determinant(A):
 A=[list(map(F,r)) for r in A];out=F(1)
 for k in range(len(A)):
  j=next(j for j in range(k,len(A)) if A[j][k])
  if j!=k:A[k],A[j]=A[j],A[k];out=-out
  p=A[k][k];out*=p
  for i in range(k+1,len(A)):
   a=A[i][k]/p
   for j in range(k+1,len(A)):A[i][j]-=a*A[k][j]
 return out


def supports(Z,g):
 poles=[]
 for f in FACETS:
  a,b,c=(Z[i] for i in f[:3]);n=cross(sub(b,a),sub(c,a));h=dot(n,a)
  assert n!=(0,0,0)
  assert all(dot(n,Z[j])==h if j in f else dot(n,Z[j])<h for j in range(10))
  height=h-dot(n,g);assert height>0;poles.append(tuple(a/height for a in n))
 return poles


def moment_check(theta):
 Z=rawverts(theta);D,g,S=generic_moments(Z);x,r,p,q,la=theta;s=1-la
 A=(31-24*x*p-24*r*q)/64
 bx=F(509,3072)-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8
 by=F(509,3072)-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
 K=(3*s**3*bx/2+s*s*la*(1-3*x*p/4)/4+la*la/4,
    3*s**3*by/2+s*s*la*(1-3*r*q/4)/4+la*la/4,
    A*s*s/2+la/2+la*la/4)
 assert D==la+2*A*s*s and tuple(D*a for a in g)==K
 assert min(minors(S))>0
 supports(Z,g)
 C=whiten(S);ZZ=tuple(mv(C,sub(z,g)) for z in Z);DD,gg,SS=generic_moments(ZZ)
 assert gg==(0,0,0) and DD==determinant(C)*D
 assert all(SS[i][j]==sum(C[i][h]*S[h][k]*C[j][k] for h in range(3) for k in range(3)) for i in range(3) for j in range(3))
 return Z,D,g,S


def packet_tensors(Z,g):
 return tuple(mat(tuple(((Z[i][k]-g[k])*(Z[j][l]-Z[i][l])+(Z[i][l]-g[l])*(Z[j][k]-Z[i][k]))/2 for k,l in PAIRS)) for i,j in ARROWS)


def control():
 Z,D,g,Sigma=moment_check(CONTROL_THETA);poles=supports(Z,g);AT=packet_tensors(Z,g);SI=inv(Sigma)
 Q=tuple(tuple(-sum(w*AT[k][i][j] for k,w in CONTROL_PACKET) for j in range(3)) for i in range(3))
 t=sum(SI[i][j]*Q[i][j] for i in range(3) for j in range(3));N=tuple(tuple(t*a/144 for a in row) for row in Sigma)
 P=tuple(tuple(Q[i][j]+N[i][j] for j in range(3)) for i in range(3))
 assert t>0 and min(minors(P))>0 and min(minors(N))>0 and minors(Q)[1]<0
 gap=sum(SI[i][j]*(P[i][j]-48*N[i][j]) for i in range(3) for j in range(3));assert gap==t/48>0
 M=mat(tuple(F(n,10000) for n in CONTROL_METRIC));MI=inv(M);assert min(minors(M))>0
 primal={(i,j):sum(M[k][l]*A[k][l] for k in range(3) for l in range(3)) for (i,j),A in zip(ARROWS,AT)}
 polar={(i,j):dot(poles[i],mv(MI,sub(poles[j],poles[i]))) for i,j in DUAL}
 assert all(primal[ARROWS[i]]>0 for i,w in CONTROL_PACKET)
 pairing=sum(M[i][j]*Q[i][j] for i in range(3) for j in range(3));assert pairing==-sum(w*primal[ARROWS[i]] for i,w in CONTROL_PACKET)<0
 uu=tuple(i for i in range(10) if all(primal[i,j]<0 for j in ADJ[i]))
 ss=tuple(i for i in range(9) if all(polar[i,j]<0 for a,j in DUAL if a==i))
 hh=tuple(e for e,(a,b) in zip(EDGES,EF) if max(primal[e],primal[e[::-1]],polar[a,b],polar[b,a])<0)
 assert all(v for v in tuple(primal.values())+tuple(polar.values()))
 assert (len(ss),len(uu),len(hh))==(3,2,3) and len(ss)+len(uu)-len(hh)==2
 return {'theta':CONTROL_THETA,'vertices':Z,'volume':D/6,'centroid':g,'covariance':Sigma,'poles':poles,
         'facets':FACETS,'edges':EDGES,'packet':[(ARROWS[i],w) for i,w in CONTROL_PACKET],
         'Q':Q,'P':P,'negative_part_N':N,'P_leading_minors':minors(P),'N_leading_minors':minors(N),
         'Q_leading_minors':minors(Q),'trace_gap_cap48':gap,'M':M,'inverse_metric':MI,'M_leading_minors':minors(M),
         'Q_pairing_M':pairing,'S':ss,'U':uu,'H':hh,'strict_counts':(len(ss),len(uu),len(hh)),
         'physical_weak_points':[],'zero_primitives':0,'primal':[(i,j,primal[i,j]) for i,j in ARROWS],
         'polar':[(i,j,polar[i,j]) for i,j in DUAL],
         'scope':'Unrestricted-SPD feasible three-arrow packet, cap48 impossible. Physical metric has condition greater than 48 in actual covariance and is a nonattaining 323 control, not U1.'}


def partition(data):
 assert tuple(map(F,data['domain_lo']))==LOW and tuple(map(F,data['domain_hi']))==HIGH
 groups={}
 for c in data['cells']:
  lo,hi=tuple(map(F,c['lo'])),tuple(map(F,c['hi']));assert all(a<b for a,b in zip(lo,hi))
  key=(lo[:4],hi[:4]);groups.setdefault(key,[]).append((lo[4],hi[4]))
 expected=set()
 for ix in product(range(2),repeat=4):
  a=tuple(LOW[k]+(HIGH[k]-LOW[k])*ix[k]/2 for k in range(4))
  b=tuple(LOW[k]+(HIGH[k]-LOW[k])*(ix[k]+1)/2 for k in range(4));expected.add((a,b))
 assert set(groups)==expected
 for ranges in groups.values():
  previous=LOW[4]
  for a,b in sorted(ranges):assert a==previous and a<b;previous=b
  assert previous==HIGH[4]
 return [len(groups[k]) for k in sorted(groups)]


def verify():
 start=monotonic();raw=Path('h5_cap48_atlas.json').read_bytes();data=json.loads(raw)
 assert data['K']==CAP==48 and data['bits']==BITS==80 and data['status']=='COMPLETE_UNVERIFIED' and data['stack']==[]
 group_counts=partition(data);certs=data['certificates'];assert len({tuple(map(tuple,c)) for c in certs})==len(certs)
 for c in certs:assert c and len({i for i,w in c})==len(c) and all(type(i) is int and 0<=i<34 and type(w) is int and w>0 for i,w in c)
 TR=trees();L=[[F(0)]*10 for _ in range(10)]
 for i,j in EDGES:L[i][i]+=1;L[j][j]+=1;L[i][j]-=1;L[j][i]-=1
 assert determinant([r[:-1] for r in L[:-1]])==4879
 assert len(TR)==48790 and len(EDGES)==17 and len(FACETS)==9 and len(DUAL)==34 and all(len(f)==2 for f in EF)
 allbits=(1<<len(TR))-1;arrowbits=[0]*34
 for j,(r,tr) in enumerate(TR):
  for i in tr:arrowbits[i]|=1<<j
 hits=[]
 for c in certs:
  hit=allbits
  for i,w in c:hit&=arrowbits[i]
  assert hit;hits.append(hit)
 cells=[];uses=0;global_gap=None;small=[None]*3;seen=set();tablehash=hashlib.sha256()
 for ci,c in enumerate(data['cells']):
  lo,hi=tuple(map(F,c['lo'])),tuple(map(F,c['hi']));rows,info=compile_box(lo,hi)
  midpoint=tuple((a+b)/2 for a,b in zip(lo,hi));moment_check(midpoint)
  tablehash.update((json.dumps(rows,separators=(',',':'))+'\n').encode())
  chosen=c['certificates'];assert chosen and len(set(chosen))==len(chosen);covered=0;nmin=dmin=None
  for j in chosen:
   assert type(j) is int and 0<=j<len(certs);cert=certs[j];W=sum(w for i,w in cert);covered|=hits[j];seen.add(j)
   for k in range(32):
    row=[sum(w*rows[i][k][h] for i,w in cert) for h in range(6)]
    mm=minors(mat(row));assert min(mm)>0
    for h,v in enumerate(mm):small[h]=v if small[h] is None else min(small[h],v)
    tr=row[0]+row[3]+row[5];num=4*mm[2];den=UNIT*tr*tr*W
    if nmin is None or num*dmin<nmin*den:nmin,dmin=num,den
  assert covered==allbits;uses+=len(chosen);delta=F(nmin,dmin);R=F(info['covariance_norm_upper'])
  # P/W >=delta I, Sigma <=R I, hence t/(48W)>=3delta/(49R).
  dual_gap=3*delta/(49*R);arrow_gap=dual_gap/97
  assert dual_gap>0 and arrow_gap>0;global_gap=arrow_gap if global_gap is None else min(global_gap,arrow_gap)
  cells.append({'lo':lo,'hi':hi,'certificate_uses':len(chosen),'covered_rooted_trees':len(TR),
                'normalized_P_eigenvalue_lower':delta,'normalized_dual_trace_gap_lower':dual_gap,
                'normalized_negative_arrow_gap_lower':arrow_gap,'compiler':info})
  if ci%25==0:print('VERIFIED_CELLS',ci+1,'USES',uses,flush=True)
 assert seen==set(range(len(certs)))
 power=0
 while F(1,1<<power)>global_gap:power+=1
 dyadic=F(1,1<<power);ctrlpin=write('h5_cap48_countercontrol.json',control())
 out={'identity':'H5_ACTUAL_COVARIANCE_CAP48_ALLROOT_MACRO_EXACT_V1','status':'EXACT_PASS',
      'atlas_bytes':len(raw),'atlas_sha256':hashlib.sha256(raw).hexdigest(),'domain_lo':LOW,'domain_hi':HIGH,
      'K':CAP,'bits':BITS,'raw_spanning_trees':4879,'rooted_trees_per_cell':len(TR),'basal_subboxes':16,
      'taper_cells_by_basal_subbox':group_counts,'cells':cells,'distinct_certificates':len(certs),
      'certificate_uses':uses,'positive_Taylor_corner_matrices':32*uses,'positive_leading_minors':96*uses,
      'raw_tree_cell_checks':len(TR)*len(cells),'minimum_integer_leading_minors':small,
      'support_histogram':dict(sorted(Counter(len(c) for c in certs).items())),
      'maximum_integer_weight':max(w for c in certs for i,w in c),'maximum_weight_sum':max(sum(w for i,w in c) for c in certs),
      'exact_uniform_normalized_negative_arrow_gap':global_gap,'dyadic_uniform_negative_arrow_gap':dyadic,
      'exact_integer_Taylor_tables_sha256':tablehash.hexdigest(),'countercontrol':ctrlpin,
      'scope':'All genuine actual H5 shapes in the stated closed basal box with p+q<1 and 0<lambda<=3/5: U>=2 for every SPD metric with actual covariance-weighted condition <=48, including incidental weak contacts. No unrestricted-U1 exclusion. Combining the accepted lambda>=3/5 all-U theorem gives proper110 exclusion for the entire taper 0<lambda<1 on this basal box and its coordinate reflection. Indexed degenerate endpoints certify matrices only; no global H5 or minimum-bound change.'}
 print(json.dumps(write('h5_cap48_report.json',out),sort_keys=True));print('H5_ACTUAL_COVARIANCE_CAP48_ALLROOT_MACRO_EXACT_PASS');print('SECONDS',monotonic()-start)
 return out

if __name__=='__main__':verify()
```

### h5_cap48_control_locator.py

```python
"""Optional all-metric subpacket witness locator, never a negative oracle."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
from h5_cap48_core import *
import numpy as np
from scipy.optimize import linprog
THETA=tuple(map(F,('13/20','3/4','4/5','1/10','3/10')))

def symmetric_tensors(Z,g):
 return [mat(tuple(((Z[i][k]-g[k])*(Z[j][l]-Z[i][l])+(Z[i][l]-g[l])*(Z[j][k]-Z[i][k]))/2 for k,l in PAIRS)) for i,j in ARROWS]

def vv(u):return np.array([u[0]**2,2*u[0]*u[1],2*u[0]*u[2],u[1]**2,2*u[1]*u[2],u[2]**2])

def propose(A):
 rows=np.array([[float(a[i][j])*(1 if i==j else 2) for i,j in PAIRS] for a in A]);rows/=np.linalg.norm(rows,axis=1)[:,None]
 planes=np.eye(3);planes=np.array([vv(v) for v in planes])
 for k in range(80):
  R=np.r_[rows,planes]
  res=linprog(np.r_[np.zeros(6),-1],A_ub=np.c_[-R,np.ones(len(R))],b_ub=np.zeros(len(R)),A_eq=[[1,0,0,1,0,1,0]],b_eq=[1],bounds=[(None,None)]*7,method='highs')
  if not res.success or res.x[-1]<=1e-9:return None
  ev,U=np.linalg.eigh(np.array(mat(res.x[:6])))
  if ev[0]>1e-9:return res.x[:6]
  planes=np.r_[planes,vv(U[:,0])[None,:]]
 return None

def main():
 Z=rawverts(THETA);D,g,S=generic_moments(Z);AT=symmetric_tensors(Z,g)
 packet=((21,31),(28,24),(31,45));A=[AT[k] for k,w in packet]
 mp=propose(A)
 if mp is None:raise RuntimeError('locator failed; no feasibility conclusion')
 for den in (1000,10000,100000,1000000,10000000,100000000,1000000000):
  nums=tuple(round(float(x)*den) for x in mp);M=mat(tuple(F(x,den) for x in nums))
  vals=[sum(M[i][j]*a[i][j] for i in range(3) for j in range(3)) for a in A]
  if min(minors(M))>0 and min(vals)>0:break
 else:raise RuntimeError('rationalization failed; no feasibility conclusion')
 assert nums==(4,17,1,9993,26,4) and den==10000
 out={'theta':list(map(str,THETA)),'packet':packet,'M_six_integer_entries':nums,'denominator':den}
 raw=(json.dumps(out,sort_keys=True,indent=2)+'\n').encode();Path('h5_cap48_control_proposal.json').write_bytes(raw)
 print('H5_CAP48_COUNTERCONTROL_RATIONALIZED_PASS',len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__':main()
```

Convenience copy: complete source-and-output capsule (`h5_cap48_macro_capsule.zip`). The four inline sources, exact inputs and commands above are sufficient without this archive.
