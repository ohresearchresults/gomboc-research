# minimum-0245

AI research report · 2026-09-26 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# H5_BASAL_MAXIMUM_ROOT_CHILD_AND_SHARP_REFLECTION_THRESHOLD_V1

## Result and scope

I obtained a structural common-metric exclusion of **19,554 complete rooted primal trees**, rather than a physical surviving tree. The mechanism is an actual-centroid reflection into the basal facet, followed by a highest-nonroot argument. It does not use the failed quadratic lowering of the arrow stress.

On the requested closed prism, the new exclusions comprise all **14,637 trees rooted at 7, 8, or 9**, and **4,917 trees with a basal root whose only child is its apical neighbour**. The latter family includes roots 0 through 6 and is disjoint from the supplied twenty-tree support. Exactly five of the supplied twenty trees have apical roots. Consequently, the union of this result with that supplied certificate covers **19,569 / 48,790** trees on the requested prism, leaving **29,221** outside this particular union. These are literal labelled-tree counts, not new canonical-orbit or whole-type counts. The supplied certificate's twenty-tree scope and its root distribution are explicit in the source.

The new geometric theorem is substantially wider in shape than the requested prism: it holds for **every x,r in [0,1], the entire physical p/q triangle, and 0 <= lambda <= 1/16**, for every common nonzero PSD metric. A sharper statement extends to the algebraic threshold described below. Thus the independent-r interval is macroscopic, indeed the whole natural interval, for these root families. It is not all-root coverage.

No actual-centred complete-tree PSD or SPD survivor is supplied. In particular, the physical countercontrol below refutes a stronger *basal-maximum trapping principle beyond its sharp threshold*, not the one-sided all-tree exclusion conjecture. General H5/E17 exclusion and the separate attaining construction remain unchanged; no improvement of the notebook's 34 <= C_min <= 622 is claimed.

## Inputs and research route

All four manifested inputs were read through their ends, including the journal's complete shared and branch memories. Their byte counts and SHA-256 values matched the manifest. Both source units were read; applying the supplied repair reproduced the 13,210-byte source with SHA-256 d6755a22a6ac68b9a865ea260113501ddba0abb81dd730f43d1dc533a7f91e4a. No historical 5,982-stress archive, parent sandbox, research connector, or additional exact dependency is used by the new result. The supplied repair changes only the identified search comprehension.

I investigated actual common-metric maximum-vertex and highest-nonroot alternatives. Exploratory feasibility calculations suggested a basal maximum could not escape upwards. I replaced that observation with the exact reflection theorem and scalar polynomial certificate below. Further analysis gave the basal-child obstruction and an exact sharpness construction. No numerical solver infeasibility or finite stress-library gap is an accepted premise.

## 1. Literal body and actual uniform moments

Write s=1-lambda. The unscaled basal vertices, in their cyclic order, are

    B0=(1/4,0), B1=(1-3x/4,0), B2=(1-p,p), B3=(q,1-q),
    B4=(0,1-3r/4), B5=(0,1/4), B6=(1/16,1/16).

Let K=s conv(B0,...,B6). The spatial vertices are z_i=(s B_i,0), i=0,...,6, and

    z7=(0,0,1), z8=(lambda,0,1), z9=(0,lambda,1).

The exact maximal-face cycles are

    (6,5,4,3,2,1,0), (8,7,0,1), (7,6,0), (1,2,8),
    (9,8,2,3), (9,3,4), (4,5,7,9), (6,7,5), (7,8,9).

These are the supplied literal labels and incidence, not another H5 representative. For strict x,r in (0,1), p,q>0, p+q<1, and 0<lambda<1, the body is genuine 10/17/9. Boundary collapses remain indexed limits.

The actual moments used throughout are

    A  = (31-24xp-24rq)/64,
    Bx = 509/3072-3xp/8+3x^2 p/32+xp^2/8-rq^2/8,
    By = 509/3072-3rq/8+3r^2 q/32+rq^2/8-xp^2/8,
    V  = A s^2/3+lambda/6,
    Jx = s^3 Bx/4+s^2 lambda(1-3xp/4)/24+lambda^2/24,
    Jy = s^3 By/4+s^2 lambda(1-3rq/4)/24+lambda^2/24,
    Jz = A s^2/12+lambda/12+lambda^2/24.

Set g=J/V=(c,gamma), where c is horizontal and gamma=Jz/V. These are genuine volume moments, not selectable masses or a frozen centroid. The standalone verifier checks all four fan identities and the three basal area/first-moment identities as polynomial identities. The formulas and positive-volume boundary convention agree with the supplied proof.

On the natural closed shape domain, 7/64 <= A <= 31/64 and 7/192 <= V <= 1/6. Directly,

    Jz-V/4 = (lambda+lambda^2)/24 >= 0,
    3V/4-Jz = A s^2/6+lambda s/24 >= 0.

Thus 1/4 <= gamma <= 3/4. On lambda <= 8/125, one also has gamma<1/2, because

    V/2-Jz = (2A s^2-lambda^2)/24 > 0,
    (7/32)(117/125)^2 > (8/125)^2.

## 2. A basal reflection trap for one common metric

For a basal point b in K and a horizontal top coordinate a in {0,lambda e1,lambda e2}, define

    w(b,a) = 2c-2 gamma a-(1-2 gamma)b.

Suppose w(b,a) belongs to K for every basal vertex b and every top vertex a. Let M be SPD and let b maximize the actual centred M-norm among basal vertices. Put

    X=(b-c,-gamma), Y=(a-c,1-gamma), d=Y-X,
    W=(w(b,a)-c,-gamma).

The exact identity is

    W = -X-2 gamma d.

Since w is in the basal polygon, maximality gives ||W||_M^2 <= ||X||_M^2. Expanding yields

    D(b->a) = X^T M d <= -gamma d^T M d < 0.                 (1)

Every other distinct basal vertex also has a strictly negative outgoing primitive from b, by the norm-difference identity. Therefore **every maximum-norm basal vertex is a strict unstable vertex of the full body**. Neither root stability nor an inverse-metric or conditioning assumption is involved.

For nonzero PSD M, strict interior containment supplies a stronger conclusion: all cross-layer arrows from every basal maximum are strictly negative, including when a particular cross-layer edge lies in the kernel. The quantitative version below proves this uniformly on the requested closed prism. Within the basal maximum fibre, zero projected edges may remain. The fibre nevertheless cannot leave the basal layer by a weak arrow. Hence it cannot reach an apical root in any complete weak rooted tree.

This is a geometric reflection statement about the true centroid. It is not a lowering of the original cubic stress polynomial.

## 3. Exact reflection certificate and its sharp threshold

The seven unscaled basal support normals n_f and heights h_f, with n_f.B <= h_f, are

    n = ((0,-1), (4p,4p-3x), (1,1), (4q-3r,4q),
         (-1,0), (-3,-1), (-1,-3)),
    h = (0, p(4-3x), 1, q(4-3r), 0, -1/4, -1/4).

Define positive normal scales, allowing zero only for a vanished redundant normal,

    sigma = (1, 3x+4p, 2, 3r+4q, 1, 4, 4).

For u_a in {(0,0),(1,0),(0,1)}, define 147 exact scalar guards

    R[f,k,a] = V s h_f - 2 n_f.J_horizontal
               + 2 Jz lambda n_f.u_a
               + (V-2Jz) s n_f.B_k.

Precisely, R[f,k,a]/V is the support slack of w(s B_k,lambda u_a) in the actual basal polygon K.

The key scalar is

    m(lambda) = (1+13lambda-413lambda^2-625lambda^3)/6144.

**Exact certificate:** every polynomial

    R[f,k,a] - sigma_f m(lambda)

has nonnegative coefficients in the tensor Bernstein basis of degrees **(2,2,2,3)** on

    x,r in [0,1], p,q>=0, p+q<=1, lambda in [0,8/125],

where the third degree is total degree two on the physical triangle. There are 216 coefficients per guard and **31,752 scalar coefficients in total: 29,976 positive and 1,776 zero**. The smallest positive coefficient is **31/1152000**. Every one of the 147 guard polynomials has at least one positive coefficient. The verifier additionally checks the 49 basal support polynomials, with exactly the 14 expected identically zero incidences.

These degree reductions are exact cancellations in the new reflection guards. No cubic term of the original mechanical stress has been discarded, bounded by a global envelope, or reinterpreted as a point evaluation.

Let lambda_* be the unique positive root of

    625lambda^3+413lambda^2-13lambda-1 = 0.

A rational isolating interval, checked exactly, is

    6350320820967/10^14 < lambda_* < 6350320820968/10^14.

Thus lambda_* is approximately 0.06350320820967, and 1/16 < lambda_* < 8/125. Descartes' sign rule and the endpoint signs give uniqueness of the positive root. For 0<=lambda<=lambda_*, m(lambda)>=0, so every reflected point belongs to K. Consequently the basal-maximum theorem holds for every SPD M throughout this closed band.

For 0<=lambda<lambda_*, the containment is strict for every nonzero normal, giving the nonzero-PSD tree exclusions even at collapsed shape parameters. At lambda=lambda_* with strict x,r,p,q shape parameters, every Bernstein basis function is positive and every shifted guard has a positive coefficient, so containment is again strict and the PSD exclusions also follow. For degenerate shape parameters exactly at lambda_*, this handoff asserts the SPD conclusion, not a uniform PSD gap. The requested prism lies well inside the strict-gap band.

### A uniform rank-independent gap on the requested prism

For every nonzero normal, ||n_f|| <= 2 sigma_f. Since V<=1/6, the horizontal disk of radius 3m(lambda) centred at each reflection point lies inside K.

Let epsilon=3m(lambda)>0. Testing W plus and minus epsilon e1 and epsilon e2 in the maximum-norm inequality gives

    D(b->a) <= -gamma d^T M d
                -epsilon^2(M11+M22)/(8gamma).

Here d_z=1 and ||d_horizontal||^2<=2. The elementary matrix inequality

    e1 e1^T + e2 e2^T + d d^T >= I/4

follows, for a test vector (u,t) and h=d_horizontal, from

    3/4(t+4h.u/3)^2 + 3|u|^2/4 - (h.u)^2/3 >= 0.

Using 1/4<=gamma<=3/4 and epsilon<1 therefore yields

    D(b->a) <= -3m(lambda)^2 tr(M)/8.                         (2)

The polynomial m is concave on the relevant interval, and its endpoint values show m(lambda)>=1/6144 on [0,1/64]. Hence, **for every x,r in [0,1], every physical p/q point, and lambda in [0,1/64]**, every basal maximum obeys

    D(b->a) <= -tr(M)/100663296 < 0

for all three apices and every nonzero PSD M. This includes the entire requested prism and all its indexed boundary limits.

## 4. A basal-root child is necessary: another 4,917 complete trees

The same reflection provides a highest-nonroot obstruction, not just the existence of one basal unstable vertex.

Suppose a top vertex a has a weak arrow to a basal vertex b and every other basal vertex has M-norm at most that of a. Work in the Euclidean image of M^(1/2), writing the centred vectors as A, B, X_i, and let rho=||A||. Since A.(B-A)>=0,

    A.B >= rho^2,   ||B||^2 >= rho^2.

Put t=2gamma in (0,1). The reflected point has image

    W=-(1-t)B-tA.

It satisfies

    ||W||^2 >= (1-t)^2||B||^2 + [1-(1-t)^2]rho^2 >= rho^2,
    W.B < 0,
    W.X_i <= ||W|| rho <= ||W||^2       for every other basal i.

W is nonzero: otherwise A and B vanish, and the norm assumptions make every centred basal vertex vanish under M^(1/2); those basal vectors span three dimensions because the actual centroid is off the positive-area basal plane, forcing M=0.

In the strict-containment band, the raw reflected point is in the relative interior of K. It therefore has a convex representation using positive weights on all basal labels, including b. Applying the functional W gives a strict contradiction to W.W: the b term is strictly smaller and all the other terms are no larger. Thus the proposed top-to-basal arrow and norm ordering are impossible for nonzero PSD M. For SPD at lambda_*, ||B||>rho makes all support comparisons strict even without interior containment.

Now consider a complete rooted primal tree with basal root b but no basal child. Each basal vertex of this literal H5 graph has exactly one apical neighbour. Therefore b is a leaf of the selected undirected tree and its sole child is that apical neighbour a. Along weak arrows the squared M-norm is nondecreasing, so every other vertex, hence every other basal vertex, has norm at most that of a. The preceding obstruction applies to a->b.

Independent exhaustive enumeration of the 4,879 unrooted spanning trees gives the excluded basal-root counts

    root 0: 693; root 1: 678; root 2: 686; root 3: 686;
    root 4: 678; root 5: 693; root 6: 803.

Their sum is **4,917**. They are disjoint from the 14,637 apical-root trees and from all twenty trees containing the supplied seven-arrow support. The geometric total is **19,554**; adding the fifteen nonoverlapping root-2 trees from the supplied certificate gives **19,569** on its original prism. The remaining count there is **29,221**, not zero.

## 5. Sharpness is physical, but it is not a surviving complete tree

The threshold is sharp for the universal claim that *every basal maximum is trapped*, not merely for this choice of Bernstein coefficients.

At the indexed limit x=1,p=1,q=0, with arbitrary r, let b=s/4 denote the greatest basal x coordinate. The exact identity checked by the code is

    R[4,1,1] = m(lambda)
              = 2V[g_x+gamma(b-lambda)-b/2].

For every lambda in (lambda_*,1), this is negative. Choose

    b-lambda < h < (b/2-g_x)/gamma,
    v=(1,0,h), M0=v v^T.

The interval is nonempty. With beta=g_x+gamma h<b/2, the basal point of x coordinate b maximizes the squared projected norm (x-beta)^2, yet its arrow to top vertex 8 equals

    (b-beta)(lambda-b+h) > 0.

Choose x=1-e, p=1-2e, q=e, r=3/8 with sufficiently small e>0. The actual centroid varies continuously, vertex 1 becomes the unique basal maximizer, and the strict positive escape persists. Adding a sufficiently small positive multiple of I gives an SPD witness on a genuine 10/17/9 body. This proves physical sharpness of the maximum-trapping principle beyond lambda_*, without asserting U=1.

### Three exact actual controls

For the first two controls use

    (x,r,p,q,lambda)=(31/32,3/8,1/4,1/4,1/128),
    V=5984879/50331648,
    g=(82630529815/392225030144,
       6565559545/24514064384,
       6050927/23939516).

**ONE_BASAL_ONE_APICAL:** M=(2,1,0)(2,1,0)^T+I/100. Exact strict (S,U,H)=(4,2,4), U={2,7}, weak000. There is only one basal unstable vertex, so a blanket “two basal U” claim is false even inside the requested prism.

**NO_APICAL_U:** M=(1,-1,0)(1,-1,0)^T+I/100. Exact strict (S,U,H)=(3,2,3), U={2,4}, weak000. There is no apical unstable vertex, so a blanket “one U on each end” claim is also false inside the requested prism.

**BASAL_MAXIMUM_ESCAPES:** use

    (x,r,p,q,lambda)=(99999/100000,3/8,49999/50000,1/100000,8/125),
    v=(1,0,17001/100000), M=v v^T+I/10^8.

This is a proper body just beyond the sharp trapping band, with its newly computed actual centroid. The exact verifier proves that vertex 1 is the unique basal maximum, its squared-norm gap over every other basal vertex exceeds 1/10^6, and

    D(1->8) > 3/10^7.

Nevertheless its actual strict census is **(4,3,5), U={4,5,8}, weak000**. It is not an actual U1 survivor. Its failed reflection slack is exactly

    R[4,1,1]/V = -350933861878984981/3994738250134150000000 < -1/20000.

All three controls use the same physical N=M^(-1), without polar recentering. All 204 true-edge primitives are nonzero and checked exactly. For compact literal sign recovery, order undirected edges lexicographically, primal directions a->b then b->a, and dual directions from the smaller incident facet index to the larger then back. The complete sign strings are:

    ONE_BASAL_ONE_APICAL
    P: -++-+---+--+---+------+-+-+--+-++-
    E: -----+--+------------+-+-+-------+

    NO_APICAL_U
    P: +--+-++--+---++----+--------+--+-+
    E: ----+----+-------+------+-+------+

    BASAL_MAXIMUM_ESCAPES
    P: +----+--+-+---+--------+----+--+-+
    E: ----+--------+-------+-----+---+-+

The complete rational vertices, moments, both metrics, poles, all primitive values, and labelled strict equilibria are regenerated by the source below. These controls are preserved as nonattaining constructions, not discarded because they do not improve C.

## 6. Evidence, recovery, and continuation

The new capsule needs **no external input files**. It embeds the literal body, actual moment formulas, oriented fan, support normals, all polynomial generators, exact Bernstein transform, tree enumeration, and all three control inputs. CPython **3.13.5** was used; the runnable source uses only the standard library and is written for Python >=3.11 with assertions enabled. NumPy/SciPy were used only in exploration, not in this verifier.

A normal run and a separate source-only cold run both passed and produced byte-identical coefficient and report files. This is an executed exact certificate and a mathematical proof above, not a proof-assistant formalization.

Pins, UTF-8 with the final newline:

    h5_basal_maximum_reflection.py
    15502 bytes
    SHA256 020531737c23bfa656f381aa5a620a7ec33eb426f9196b3d2f97158d48427cc8

    h5_basal_reflection_coefficients.json
    418356 bytes
    SHA256 795a5c3aa4d046560da45b0b83741698c2094ca6b2b455334adb072bb118777f

    h5_basal_maximum_report.json
    25750 bytes
    SHA256 9be1e9b55c9d34bf42c4373763ea789b8ace8f9bfed97631193eabd63638315f

    cold receipt.txt
    585 bytes
    SHA256 0efcb94a50c45fe813c166063e327fc5ed30bcd43211735bfa96162d1c0365fb

Reconstruction and verification:

    python -B -S h5_basal_maximum_reflection.py output

A source-only cold reproduction consists of copying only that source into a fresh directory and running the same command. Expected markers are

    H5_ACTUAL_FAN_AND_BASAL_MOMENTS_PASS 4 3
    H5_BASAL_REFLECTION_BERNSTEIN_PASS 147 216 31752 29976 1776
    H5_ROOT_CHILD_EXCLUSION_CENSUS_PASS 4879 14637 4917 19554 5 19569 29221
    H5_BASAL_TRAP_THREE_ACTUAL_CONTROLS_PASS 3 204
    H5_BASAL_MAXIMUM_SHARP_REFLECTION_RECOVERY_PASS

**Most useful continuation:** restrict the requested-prism search to basal roots with at least one selected basal child, and remove the supplied fifteen additional root-2 trees. The resulting 29,221-tree family is the remainder of this explicitly identified union, not a claim that no other inherited result covers any of it. Keep actual centroid motion and allow the extra U to migrate between the two layers: the two interior controls disprove both obvious fixed-layer completion arguments. A genuine surviving complete PSD/SPD tree in this remainder would change the one-sided approach; no such survivor has been established here.

## 7. Complete standalone recovery source

Save the following exact code as h5_basal_maximum_reflection.py. It regenerates every coefficient and control used above; neither the supplementary downloads nor the supplied repaired parent source are runtime dependencies.

```python
#!/usr/bin/env python3
"""Exact H5 basal-maximum trap and sharp reflection threshold.
CPython >= 3.11, standard library only, assertions enabled.
No input files, numerical optimizers, saved matrices, or parent sandbox needed.
Parent geometry: H5_ORIGINAL_CUBIC_MACRO_BAND_20_ROOTED_TREES_V1.md,
SHA256 fe22185a408580130896b80b3c4d8c62fe486c0f6c6220c3635e869094568657.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb, lcm
from pathlib import Path
import hashlib
import json
import sys

TITLE = 'H5_BASAL_MAXIMUM_ROOT_CHILD_AND_SHARP_REFLECTION_THRESHOLD_V1'
ZERO = (0,)*5
LAMBDA_MAX = F(8,125)
FACES = ((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
         (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
FAN = ((0,1,2,8),(0,9,8,2),(0,9,2,3),(0,9,3,4),
       (0,4,5,7),(0,4,7,9),(0,6,7,5),(0,7,8,9))
EDGES = tuple(sorted({tuple(sorted((a,b))) for face in FACES
                     for a,b in zip(face,face[1:]+face[:1])}))
ARROWS = tuple(e for a,b in EDGES for e in ((a,b),(b,a)))
ADJ = tuple(tuple(j for i,j in ARROWS if i==k) for k in range(10))
TRI = tuple((i,j) for i in range(3) for j in range(3-i))
INDICES = tuple(product(range(3),range(3),TRI,range(4)))
PARENT_SUPPORT = {(0,1),(1,2),(3,2),(4,3),(5,6),(6,0),(7,0)}

class P:
    def __init__(self, x=0):
        if isinstance(x,P): self.d=x.d.copy()
        elif isinstance(x,dict): self.d={k:F(v) for k,v in x.items() if v}
        else: self.d={} if not x else {ZERO:F(x)}
    def __add__(self,b):
        d=self.d.copy()
        for k,v in P(b).d.items(): d[k]=d.get(k,F(0))+v
        return P(d)
    __radd__=__add__
    def __neg__(self): return P({k:-v for k,v in self.d.items()})
    def __sub__(self,b): return self+-P(b)
    def __rsub__(self,b): return P(b)+-self
    def __mul__(self,b):
        d={}
        for k,v in self.d.items():
            for j,w in P(b).d.items():
                z=tuple(a+c for a,c in zip(k,j))
                d[z]=d.get(z,F(0))+v*w
        return P(d)
    __rmul__=__mul__
    def __truediv__(self,b): return self*(1/F(b))
    def __pow__(self,n):
        z=P(1)
        for _ in range(n): z=z*self
        return z
    def __eq__(self,b): return self.d==P(b).d

def var(i):
    k=[0]*5; k[i]=1
    return P({tuple(k):1})
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(A): return dot(A[0],cross(A[1],A[2]))
def mv(M,v): return tuple(dot(row,v) for row in M)
def bil(a,M,b): return dot(a,mv(M,b))
def outer(a,b): return tuple(tuple(x*y for y in b) for x in a)
def inverse(A):
    d=det(A); assert d!=0
    return tuple(tuple((A[(j+1)%3][(i+1)%3]*A[(j+2)%3][(i+2)%3]
                       -A[(j+1)%3][(i+2)%3]*A[(j+2)%3][(i+1)%3])/d
                       for j in range(3)) for i in range(3))
def specialize(poly,values):
    d={}
    for k,c in P(poly).d.items():
        z=list(k)
        for i,v in values.items(): c*=v**z[i]; z[i]=0
        key=tuple(z); d[key]=d.get(key,F(0))+c
    return P(d)
def evaluate(poly,pt):
    return sum(c*prod_values(a**b for a,b in zip(pt,k))
               for k,c in P(poly).d.items())
def prod_values(values):
    ans=F(1)
    for v in values: ans*=v
    return ans

def geometry(pt):
    x,r,p,q,l=pt; s=1-l
    B=((F(1,4),0),(1-3*x/4,0),(1-p,p),(q,1-q),
       (0,1-3*r/4),(0,F(1,4)),(F(1,16),F(1,16)))
    Z=tuple((s*a,s*b,0) for a,b in B)+((0,0,1),(l,0,1),(0,l,1))
    area=(31-24*x*p-24*r*q)/64
    bx=F(509,3072)-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8
    by=F(509,3072)-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
    V=area*s*s/3+l/6
    J=(s**3*bx/4+s*s*l*(1-3*x*p/4)/24+l*l/24,
       s**3*by/4+s*s*l*(1-3*r*q/4)/24+l*l/24,
       area*s*s/12+l/12+l*l/24)
    return B,Z,V,J,area,(bx,by)

def polynomial_inputs():
    pt=tuple(var(i) for i in range(5)); x,r,p,q,l=pt; s=1-l
    B,Z,V,J,area,bmom=geometry(pt)
    av=P(0); aj=[P(0) for _ in range(3)]
    for ids in FAN:
        a,b,c,d=(Z[i] for i in ids)
        vol=dot(sub(b,a),cross(sub(c,a),sub(d,a)))/6
        av+=vol
        for k in range(3): aj[k]+=vol*sum(Z[i][k] for i in ids)/4
    assert av==V and all(aj[k]==J[k] for k in range(3))
    ca=P(0); cm=[P(0),P(0)]
    for a,b in zip(B,B[1:]+B[:1]):
        cr=a[0]*b[1]-a[1]*b[0]; ca+=cr/2
        for k in range(2): cm[k]+=(a[k]+b[k])*cr/6
    assert ca==area and all(cm[k]==bmom[k] for k in range(2))
    normals=((0,-1),(4*p,4*p-3*x),(1,1),(4*q-3*r,4*q),
             (-1,0),(-3,-1),(-1,-3))
    heights=(0,p*(4-3*x),1,q*(4-3*r),0,F(-1,4),F(-1,4))
    sigma=(1,3*x+4*p,2,3*r+4*q,1,4,4)
    top=((0,0),(1,0),(0,1))
    Q=(1+13*l-413*l*l-625*l**3)/6144
    guards=[]; shifted=[]; labels=[]; slacks=[]
    for f,k in product(range(7),range(7)):
        slack=P(heights[f])-dot(normals[f],B[k]); slacks.append(slack)
        assert (slack==0)==(k in (f,(f+1)%7))
    for f,k,a in product(range(7),range(7),range(3)):
        n=normals[f]
        R=V*s*heights[f]-2*dot(n,J[:2])+2*J[2]*l*dot(n,top[a])
        R+=(V-2*J[2])*s*dot(n,B[k])
        labels.append((f,k,a)); guards.append(R); shifted.append(R-sigma[f]*Q)
    assert specialize(guards[labels.index((4,1,1))],
                      {0:F(1),2:F(1),3:F(0)})==Q
    return shifted,labels,slacks

def bernstein(polys):
    # Degrees (2,2,total-triangle-2,3), x,r in [0,1], l in [0,8/125].
    polys=list(map(P,polys)); keys=sorted({k for p in polys for k in p.d})
    assert all(k[0]<=2 and k[1]<=2 and k[2]+k[3]<=2 and k[4]<=3 for k in keys)
    C=[[p.d.get(k,F(0)) for p in polys] for k in keys]
    T=[]
    for i,j,(u,v),w in INDICES:
        row=[]
        for a,b,c,d,e in keys:
            if a>i or b>j or c>u or d>v or e>w: row.append(F(0)); continue
            z=F(comb(i,a),comb(2,a))*F(comb(j,b),comb(2,b))
            z*=F(comb(u,c)*comb(v,d),comb(2,c+d)*comb(c+d,c))
            z*=F(comb(w,e),comb(3,e))*LAMBDA_MAX**e
            row.append(z)
        T.append(row)
    dc=lcm(*(v.denominator for row in C for v in row))
    dt=lcm(*(v.denominator for row in T for v in row))
    C=[[int(v*dc) for v in row] for row in C]
    ans=[]
    for row in T:
        nz=[(k,int(v*dt)) for k,v in enumerate(row) if v]
        ans.append([sum(t*C[k][j] for k,t in nz) for j in range(len(polys))])
    return ans,dc*dt

def qvalue(t): return (1+13*t-413*t*t-625*t**3)/6144

def census(pt,v,eps):
    pt=tuple(map(F,pt)); v=tuple(map(F,v)); eps=F(eps)
    B,Z,V,J,_,_=geometry(pt); g=tuple(t/V for t in J); X=tuple(sub(z,g) for z in Z)
    assert V>0
    M=tuple(tuple(v[i]*v[j]+(eps if i==j else 0) for j in range(3)) for i in range(3))
    minors=(M[0][0],M[0][0]*M[1][1]-M[0][1]**2,det(M))
    assert min(minors)>0
    N=inverse(M)
    assert all(sum(M[i][k]*N[k][j] for k in range(3))==int(i==j)
               for i,j in product(range(3),repeat=2))
    vv=F(0); jj=[F(0)]*3
    for ids in FAN:
        a,b,c,d=(Z[i] for i in ids)
        vol=dot(sub(b,a),cross(sub(c,a),sub(d,a)))/6
        assert vol>0
        vv+=vol
        for k in range(3): jj[k]+=vol*sum(Z[i][k] for i in ids)/4
    assert vv==V and tuple(jj)==J
    poles=[]
    for f in FACES:
        a,b,c=(X[i] for i in f[:3]); n=cross(sub(b,a),sub(c,a)); hh=dot(n,a)
        if hh<0: n=tuple(-t for t in n); hh=-hh
        assert hh>0
        pole=tuple(t/hh for t in n)
        assert all(dot(pole,X[i])==1 for i in f)
        assert all(dot(pole,X[i])<1 for i in range(10) if i not in f)
        poles.append(pole)
    pp=[bil(X[i],M,sub(X[j],X[i])) for i,j in ARROWS]
    dual=[]; qq=[]; packets=[]
    for a,b in EDGES:
        inc=[i for i,f in enumerate(FACES) if a in f and b in f]
        assert len(inc)==2; f,h=inc
        for i,j in ((f,h),(h,f)):
            dual.append((i,j)); qq.append(bil(poles[i],N,sub(poles[j],poles[i])))
        packets.append((pp[ARROWS.index((a,b))],pp[ARROWS.index((b,a))],qq[-2],qq[-1]))
    assert len(pp+qq)==68 and all(t!=0 for t in pp+qq)
    U=[i for i in range(10) if all(pp[ARROWS.index((i,j))]<0 for j in ADJ[i])]
    S=[i for i in range(9) if all(t<0 for (a,b),t in zip(dual,qq) if a==i)]
    H=[e for e,packet in zip(EDGES,packets) if max(packet)<0]
    assert len(S)+len(U)-len(H)==2
    norms=[bil(x,M,x) for x in X]
    return {'parameters_x_r_p_q_lambda':pt,'raw_vertices':Z,'volume':V,'first_moment':J,
            'centroid':g,'metric_v':v,'metric_epsilon':eps,'M':M,'N':N,
            'metric_leading_minors':minors,'poles':poles,'primal_order':ARROWS,
            'primal_values':pp,'dual_order':dual,'dual_values':qq,
            'primal_signs':''.join('+' if t>0 else '-' for t in pp),
            'dual_signs':''.join('+' if t>0 else '-' for t in qq),
            'strict_S':S,'strict_U':U,'strict_H_edges':H,
            'weak_points':0,'nonzero_primitives':68,'norms_squared':norms}

def tree_counts():
    assert len(EDGES)==17
    counts=[0]*10; parent=[0]*10; leaf=[0]*10
    apical=0; overlap=0; leaf_overlap=0; ntrees=0
    stream=hashlib.sha256()
    for chosen in combinations(EDGES,9):
        adj=[[] for _ in range(10)]
        for a,b in chosen: adj[a].append(b); adj[b].append(a)
        seen={0}; queue=[0]
        for a in queue:
            for b in adj[a]:
                if b not in seen: seen.add(b); queue.append(b)
        if len(seen)!=10: continue
        ntrees+=1
        for root in range(10):
            out={}; seen={root}; queue=[root]
            for a in queue:
                for b in adj[a]:
                    if b not in seen: seen.add(b); queue.append(b); out[b]=a
            assert len(out)==9
            arrows=tuple(sorted(out.items())); counts[root]+=1
            old=PARENT_SUPPORT.issubset(arrows)
            if old: parent[root]+=1
            if root<7 and len(adj[root])==1 and adj[root][0]>=7:
                leaf[root]+=1; leaf_overlap+=int(old)
            if root in (7,8,9):
                apical+=1; overlap+=int(old)
                stream.update((str(root)+':' + ','.join(str(a)+'>'+str(b) for a,b in arrows)+'\n').encode())
    assert ntrees==4879 and counts==[4879]*10
    assert parent==[0,0,15,0,0,0,0,0,4,1]
    assert apical==14637 and overlap==5
    assert leaf==[693,678,686,686,678,693,803,0,0,0]
    assert sum(leaf)==4917 and leaf_overlap==0
    return {'unrooted_trees':ntrees,'rooted_by_root':counts,'apical_roots':[7,8,9],
            'apical_rooted_trees':apical,'basal_root_apical_only_child_by_root':leaf,
            'basal_root_apical_only_child_total':sum(leaf),'geometric_total':19554,
            'parent_support_by_root':parent,'overlap_with_parent_20':overlap,
            'basal_leaf_overlap_with_parent_20':leaf_overlap,'union_with_parent_20':19569,
            'remaining_after_this_union':29221,'apical_tree_stream_sha256':stream.hexdigest()}

def clean(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {str(k):clean(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [clean(v) for v in x]
    return x

def save(path,obj):
    raw=(json.dumps(clean(obj),sort_keys=True,separators=(',',':'))+'\n').encode()
    path.write_bytes(raw)
    return {'filename':path.name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}

def main(out):
    if not __debug__: raise RuntimeError('Run without -O: exact assertions are required.')
    out.mkdir(parents=True,exist_ok=True)
    polys,labels,slacks=polynomial_inputs()
    nums,den=bernstein(polys)
    assert len(nums)==216 and all(len(row)==147 for row in nums)
    assert all(n>=0 for row in nums for n in row)
    assert all(any(row[j]>0 for row in nums) for j in range(147))
    bn,bd=bernstein(slacks)
    assert all(n>=0 for row in bn for n in row)
    assert sum(all(row[j]==0 for row in bn) for j in range(49))==14
    low=F(6350320820967,10**14); high=F(6350320820968,10**14)
    assert F(1,16)<low<high<LAMBDA_MAX
    assert qvalue(low)>0 and qvalue(high)<0
    assert qvalue(F(1,64))>=qvalue(F(0))==F(1,6144)
    assert qvalue(F(1,16))==F(191,25165824)
    # This gives Jz/V<1/2 throughout the auxiliary lambda interval.
    assert F(7,32)*(1-LAMBDA_MAX)**2>LAMBDA_MAX**2
    base_pt=(F(31,32),F(3,8),F(1,4),F(1,4),F(1,128))
    controls={
        'ONE_BASAL_ONE_APICAL':census(base_pt,(2,1,0),F(1,100)),
        'NO_APICAL_U':census(base_pt,(1,-1,0),F(1,100)),
        'BASAL_MAXIMUM_ESCAPES':census((F(99999,100000),F(3,8),F(49999,50000),
                                      F(1,100000),F(8,125)),
                                     (1,0,F(17001,100000)),F(1,10**8))}
    assert controls['ONE_BASAL_ONE_APICAL']['strict_U']==[2,7]
    assert controls['NO_APICAL_U']['strict_U']==[2,4]
    c=controls['BASAL_MAXIMUM_ESCAPES']; ns=c['norms_squared']
    gap=ns[1]-max(ns[:1]+ns[2:7]); d18=c['primal_values'][ARROWS.index((1,8))]
    assert gap>F(1,10**6) and d18>F(3,10**7)
    assert c['strict_U']==[4,5,8]
    gx,gy,gz=c['centroid']; lam=c['parameters_x_r_p_q_lambda'][4]
    violation=2*gx-2*gz*lam-(1-2*gz)*c['raw_vertices'][1][0]
    assert violation<F(-1,20000)
    c['basal_maximum_vertex']=1; c['basal_norm_gap']=gap
    c['positive_escape_1_to_8']=d18; c['reflection_guard_f4_k1_a1_over_V']=violation
    coeff_record={'title':TITLE,'polynomials':'R[f,k,a]-sigma[f]*Q(lambda)',
                  'x_r_box':[['0','1'],['0','1']],
                  'lambda_box':['0',str(LAMBDA_MAX)],
                  'triangle':'p>=0,q>=0,p+q<=1','degrees':[2,2,2,3],
                  'guard_order':labels,'bernstein_indices':INDICES,
                  'common_denominator':str(den),
                  'coefficient_numerators':[[str(n) for n in row] for row in nums]}
    pin=save(out/'h5_basal_reflection_coefficients.json',coeff_record)
    positive=[n for row in nums for n in row if n>0]
    report={'title':TITLE,'scope':'Basal-maximum trapping, apical-root and basal-root/apical-only-child exclusions; NOT all roots.',
            'parent_proof_sha256':'fe22185a408580130896b80b3c4d8c62fe486c0f6c6220c3635e869094568657',
            'facets':FACES,'edges':EDGES,'fan':FAN,'fan_identities':4,'basal_moment_identities':3,
            'basal_support_polynomials':49,'identically_zero_basal_supports':14,
            'reflection_guards':147,'coefficients_per_guard':216,
            'nonnegative_coefficients':31752,'positive_coefficients':len(positive),
            'zero_coefficients':31752-len(positive),'minimum_positive_coefficient':F(min(positive),den),
            'every_guard_has_a_positive_coefficient':True,
            'threshold_polynomial_ascending':[-1,-13,413,625],
            'positive_threshold_root_interval':[low,high],
            'Q_at_zero':qvalue(F(0)),'Q_at_one_over_16':qvalue(F(1,16)),
            'lambda_le_one_over_64_cross_arrow_gap':F(1,100663296),
            'coefficient_file':pin,'tree_counts':tree_counts(),'controls':controls,
            'verification':'Exact standard-library integer/Fraction arithmetic; no SDP or LP acceptance.'}
    reportpin=save(out/'h5_basal_maximum_report.json',report)
    print('H5_ACTUAL_FAN_AND_BASAL_MOMENTS_PASS 4 3')
    print('H5_BASAL_REFLECTION_BERNSTEIN_PASS 147 216 31752',len(positive),31752-len(positive))
    print('H5_ROOT_CHILD_EXCLUSION_CENSUS_PASS 4879 14637 4917 19554 5 19569 29221')
    print('H5_BASAL_TRAP_THREE_ACTUAL_CONTROLS_PASS 3 204')
    print('H5_BASAL_MAXIMUM_SHARP_REFLECTION_RECOVERY_PASS')
    print(json.dumps({'coefficients':pin,'report':reportpin},sort_keys=True))

if __name__=='__main__':
    main(Path(sys.argv[1] if len(sys.argv)>1 else 'h5-basal-output'))
```

Supplementary copies: standalone source (`h5_basal_maximum_reflection.py`), exact report (`h5_basal_maximum_report.json`), and all scalar Bernstein coefficients (`h5_basal_reflection_coefficients.json`). The complete recovery code is already embedded above.
