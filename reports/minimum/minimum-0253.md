# minimum-0253

AI research report · 2026-09-26 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# H5_PAIRED_END_REFLECTION_JOINT_REGION_V1

## 1. Result: a nonperturbative joint theorem and four certified regions

**For every genuine homogeneous H5 body in the union of the four regions below, every physical SPD metric has S ≥ 2 or U ≥ 2. Additional weak equilibria are allowed.** In particular, none is proper110.

| Region | x and r | p and q | Taper |
|---|---|---|---|
| DEEP | each in [2/5, 3/5] | each in [3/10, 1/2], with p+q<1 | 0<lambda≤3/40 |
| WIDE | each in [1/5, 4/5] | each in [1/5, 1/2] | 0<lambda≤1/40 |
| BROAD | each in [1/10, 9/10] | each in [1/5, 1/2] | 0<lambda≤1/100 |
| FULL_BASAL | arbitrary 0<x,r<1 | arbitrary p,q>0, p+q<1 | 0<lambda≤1/300 |

The genuine-domain condition p+q<1 applies to every row. Upper taper endpoints and the displayed nondegenerate basal-box endpoints are included. Algebraic faces at lambda=0, p+q=1, or other collapsed parameter boundaries are used only for coefficient verification, not claimed as ten-vertex bodies.

The main extension is **not a recalibration of the parent Hausdorff estimate**. An exact centroid-coupled reflection condition gives a strict basal U and forces the basal facet to be strictly stable under U1. A second exact reflection in the **actual same-origin polar under the same inverse** forces a nonbasal strict S. These arguments work for arbitrary SPD metrics without a condition-number hypothesis. They do **not** prove U≥2 for every metric.

The three boxed basal regions are disjoint from the named x≥15/16 macro, its reflection, and the radius-2^-28 tubes: their x,r are at most 9/10 and their p,q at most 1/2. Their taper is below 3/5. Their portions above 1/400000 therefore supply new coverage beyond those accepted exclusions and the parent's apex-cluster theorem. DEEP also has p+q≥3/5 and avoids the historical x=1/3 and r=1/3 slices. Other previously closed lower-dimensional slices may intersect BROAD or WIDE; no disjoint catalogue subtraction is claimed. The supplied exclusion map distinguishes these domains. fileciteturn9file0L86-L95

Combining FULL_BASAL with the accepted lambda≥3/5 exclusion leaves the universal taper interval

    1/300 < lambda < 3/5,

with the three larger regional exclusions and all earlier exclusions removed as well. **Whole H5 and the minimum problem remain open; 34≤C_min≤622 is unchanged.** No new attainer or canonical incidence/root count is claimed. The original bound is a working premise from the supplied memory. fileciteturn4file0L9-L11

## 2. Reading and authority

I read the complete new journal, including the entire literal parent and its source block, consecutively through line 1604/EOF. The mounted journal has 325022 bytes and SHA-256 `cd57923031a0a59ac549d0e904f6571dfda559ebeb86787fab50aa2d08343dee`. The four earlier standalone geometry/covariance/finite-height sources remain available and unchanged; their completed reading was retained rather than restarted.

The immediate parent is `minimum-0252`, registered envelope SHA-256 `c166ef43daf3b0236b4e6c5360246aaf15fec13adfb79c3a1f22541c4d49bce9`. Its source pin remains 11918 bytes, `d956d2609f5406319a1dbd6e7ecd88ac411d0b606d36fd39a75ba68ca97115c2`. The earlier Markdown-versus-registered-hash qualification is resolved: the registered digest identifies the JSON envelope. There is no semantic source conflict. The update explicitly preserves that correction and the parent's actual control counts. fileciteturn10file0L29-L36

No unavailable archive or research connector was used. The new proof and reconstruction below are self-contained and do not import a parent source or saved certificate. Historical exclusions are accepted inputs for comparison, not newly replayed results. The executable checks exact algebra, whole parameter regions, and actual controls; it is not a proof-assistant formalization of the geometric argument.

## 3. General paired-end reflection theorem

This theorem is about one actual polytope at one specified interior reference. Its H5 application uses the actual uniform-volume centroid, not an inherited comparison centroid.

Let

    P = conv((B,0),(T,1)),     g=(c,gamma),

where B and T are full-dimensional planar convex polygons. Suppose 1/4≤gamma<1/3. Write B_g and T_g for the two centered end polygons in P-g. Assume:

**Paired-end containment (C):** for every b∈B and a∈T,

    [c - gamma(b+a)]/(1-2gamma) ∈ B.

Equivalently, with k=gamma/(1-2gamma),

    -k(B_g+T_g) ⊂ B_g.

This containment may be non-strict.

**Opposite-top pole condition (A):** every nonbasal true pole q of P-g satisfies

    q·a > -1    for every a∈T_g.

Poles are normalized by q·X≤1 on P-g. They are not recentered at a polar volume centroid.

Then, for every SPD metric M and its actual inverse N:

1. A strict unstable basal vertex exists.
2. A strict stable nonbasal facet exists.
3. U=1 implies that the basal facet is strictly stable.

Thus S=U=1 is impossible, including when additional physical weak contacts occur.

For fixed B,T, these hypotheses are affine inequalities in the reference coordinates (c,gamma), after multiplication by the positive 1-2gamma and the true support denominators. They therefore give a convex, metric-independent sufficient reference region. In the homogeneous application, the reference is fixed by the actual moment equations; it is not a free variable chosen to satisfy these inequalities.

### Proof: one physical frame throughout

Apply a physical map L with L^T L=M, then rotate so the end planes are horizontal. Center at Lg. This transports poles by L^-T, hence uses N=M^-1, not an independently reset polar metric. Let the total physical height be h>0. Centered basal points have height -K, top points height H, with

    K=gamma h,     H=(1-gamma)h.

All containments, pole incidences, and gamma are preserved. The rest of the proof uses the resulting Euclidean scalar product.

### 3.1 An unavoidable strict basal U

Choose b of maximum norm on the basal polygon. It is a true basal vertex. If its derivative toward any top vertex a were D_ba=b·(a-b)≥0, then

    |b+a|² = 4|b|² + 4D_ba + |a-b|² > 4|b|².

But -k(b+a) lies in the basal polygon by (C), and k≥1/2. It would have norm greater than |b|, a contradiction. Thus every top derivative is strictly negative.

Every same-layer incident derivative is strictly negative as well: maximality and the positive squared edge length give

    2D_bv = |v|²-|b|²-|v-b|² < 0.

So b is a strict U of the actual three-dimensional body, even at norm ties elsewhere.

### 3.2 U1 forces the basal foot into the relative interior

Assume U=1. The preceding basal U is then the unique root. Choose a top vertex a=(t,H) of maximum top norm, and set d=|t|>0. Its same-layer derivatives are all strictly negative. Since it is not the unique U, some true spoke to a basal vertex b=(u,-K) has a nonnegative derivative. Therefore

    t·u ≥ d²+Hh > d².

Choose horizontal coordinates with t=(d,0). Then b_x>d.

For this fixed a, the map F_a(b)=-k(b+a) takes the basal polygon into itself. Since k<1, its fixed point

    c_a = -[gamma/(1-gamma)]a

belongs to the basal polygon. It is in its relative interior. Indeed, after translation to this fixed point, invariance is -kB'⊂B'; a supporting line through 0 would force all of B' into that line, contradicting its positive area.

Suppose the basal foot of the origin is not interior. On the horizontal line through t, the basal chord contains the negative interior point -[gamma/(1-gamma)]t. Its right endpoint R must therefore be ≤0. If L is the left endpoint, invariance gives

    -k(L+d) ≤ R ≤ 0,    hence L≥-d.

Thus every point of that chord has horizontal norm at most d. The vertex b_x>d is off the chord. Its reflected point F_a(b) lies on the opposite side of the chord and has first coordinate

    -k(b_x+d) < -2kd ≤ -d.

Both points have horizontal norm greater than d, on opposite sides of the separating line.

Maximize horizontal norm separately in the two closed halves of the basal polygon. Both maxima are off the separating chord, so they are distinct true basal vertices. All their same-layer incident derivatives are strictly negative: a short initial segment of each edge stays in the same half. If either maximum has horizontal radius rho>d, its derivative to every top vertex is at most

    rho d - rho² - Kh < 0,

because all top horizontal radii are at most d. Thus both are strict U, contradicting U=1.

The basal foot is therefore interior, making the basal facet strictly stable. In the original Schur chart this foot is exactly c+gamma v.

### 3.3 An exact nonbasal polar reflection

First derive a weaker reflection that will also be useful for continuation. Put

    theta=(1-2gamma)²/gamma.

For 1/4≤gamma<1/3, 0<theta≤1, since

    1-theta=(1-gamma)(4gamma-1)/gamma.

The convex combination of F_a(b) and its fixed point c_a gives

    theta F_a(b)+(1-theta)c_a
      = -(1-2gamma)b-2gamma a ∈ B_g.                    (W)

Let q_B be the actual basal pole. Thus q_B·b=1 on B_g and q_B·a=-(1-gamma)/gamma on T_g. Choose q of maximum norm among all nonbasal true poles. Set

    m=min_{a∈T_g} q·a > -1,
    delta=1-gamma+gamma m,
    alpha=(1-2gamma)/delta,
    beta=gamma(1+m)/delta.

Here delta>0, alpha>0, beta>0, and alpha+beta=1. Define the actual polar comparison point

    r = -alpha q-beta q_B.

For every top a, the definition of m gives r·a≤1, with equality at a minimizing top vertex. For every basal b, apply q to (W) with a top minimizer:

    (1-2gamma)q·b+2gamma m ≥ -1.

Substitution gives r·b≤1. Thus r lies in the actual polar and on a face dual to a true top vertex. That face contains no basal pole. Consequently r is in the convex hull of nonbasal poles and |r|≤|q|.

If q·(q_B-q)≥0, however, then

    |r|² = |q|² + 2beta q·(q_B-q) + beta²|q_B-q|² > |q|².

This contradiction proves q·(q_B-q)<0. Every derivative from q to another nonbasal pole is strictly negative by norm maximality and distinctness. Therefore q is a strict U of the actual polar, hence a strict nonbasal S of the primal under the same inverse pair. Explicitly, q/|q|² has equality on its own primal facet and strict slack against every other actual pole, so it lies in that facet’s relative interior. In the original frame the same foot is Nq/(q^T Nq).

Under U1, this nonbasal S coexists with the basal S from Section 3.2. The theorem follows. None of these arguments discards a zero nonroot primitive or presumes weak freedom.

## 4. Literal H5 and the exact scalar certificate

Put s=1-lambda. The unscaled basal polygon is

    B0=conv((1/4,0),(1-3x/4,0),(1-p,p),(q,1-q),
            (0,1-3r/4),(0,1/4),(1/16,1/16)).

Here B=sB0, T=lambda conv((0,0),(1,0),(0,1)). The true oriented maximal facets are

    (6,5,4,3,2,1,0), (8,7,0,1), (7,6,0), (1,2,8),
    (9,8,2,3), (9,3,4), (4,5,7,9), (6,7,5), (7,8,9).

The source independently recovers the actual boundary-fan moments. With D=6Vol(P), K=6 integral_P X, define

    A=(31-24xp-24rq)/64,
    bx=509/3072-3xp/8+3x²p/32+xp²/8-rq²/8,
    by=509/3072-3rq/8+3r²q/32+rq²/8-xp²/8.

Then

    D=lambda+2As²,
    Kx=3s³bx/2+s²lambda(1-3xp/4)/4+lambda²/4,
    Ky=3s³by/2+s²lambda(1-3rq/4)/4+lambda²/4,
    Kz=As²/2+lambda/2+lambda²/4,
    g=K/D.

In particular D>0, and 4Kz-D=lambda(1+lambda)>0 on every genuine body. No comparison-body centroid appears.

For the seven basal edges, the following triples (n,h,t) specify n·b≤h on B and t=max_T n·a:

| Edge index | n | h | t |
|---|---|---|---|
| 0 | (0,-1) | 0 | 0 |
| 1 | (p,p-3x/4) | sp(1-3x/4) | lambda p |
| 2 | (1,1) | s | lambda |
| 3 | (q-3r/4,q) | sq(1-3r/4) | lambda q |
| 4 | (-1,0) | 0 | 0 |
| 5 | (-3,-1) | -s/4 | 0 |
| 6 | (-1,-3) | -s/4 | 0 |

The corresponding actual side plane is (n,h-t)·X≤h. Its positively cleared support denominator is

    H_e=D h-n·K_xy-(h-t)Kz.

For every one of the 7×7×3 actual edge/basal-vertex/top-vertex choices, paired-end containment is exactly

    C_eij=(D-2Kz)h-n·K_xy+Kz n·(b_i+a_j) ≥ 0.

For each of the 7×3 side/top-vertex pairs, condition (A) is exactly

    T_ej=2H_e-D(t-n·a_j) > 0.

Indeed q_e·(a_j-g)=1-D(t-n·a_j)/H_e. The top pole has value 1 on all top vertices automatically.

Thus the theorem follows from **177 scalar polynomials**: 147 C, 21 T, seven H, and the two height guards 4Kz-D and D-3Kz. All are computed with the actual moving centroid. There is no metric variable, semidefinite atlas, selected-tree assumption, or separately feasible polar system in this certificate.

### Exact whole-region verification

For BROAD, WIDE, and DEEP, all coefficients except the single lambda=0 coefficient of 4Kz-D are strictly positive in the tensor Bernstein basis on the displayed closed boxes. For FULL_BASAL, substitute q=(1-p)w and use x,r,p,w∈[0,1], lambda∈[0,1/300]. All coefficients are nonnegative. The executable checks a positive coefficient on the upper-taper face for every polynomial. Since x,r,p,w are strictly interior on every genuine basal shape, this proves strict positivity there for 0<lambda≤1/300. Zero coefficients do not require throwing away weak mechanical cases.

| Region | Polynomial/box checks | Bernstein coefficients | Positive | Zero |
|---|---:|---:|---:|---:|
| FULL_BASAL | 177 | 41679 | 39434 | 2245 |
| BROAD | 177 | 40179 | 40178 | 1 |
| WIDE | 177 | 40179 | 40178 | 1 |
| DEEP | 177 | 40179 | 40178 | 1 |
| Total | 708 | 162216 | 159968 | 2248 |

All 708 expansions are independently expanded back into their complete power coefficients. Each region is one tensor box; there is no recursive pruning or unresolved cell. The minimum C coefficient in BROAD, WIDE, and DEEP is respectively

    10610214557/10240000000000,
    223963049/163840000000,
    487657/3276800000.

FULL_BASAL has zero boundary coefficients, not a uniform positive margin over collapsed basal limits. Its minimum positive C coefficient is 1668577/49152000000; the interior/upper-face argument above, not that number alone, establishes strictness. The complete coefficient arrays are deterministically regenerated by the source and retained in the report.

## 5. Exact actual controls and a substantive limit of extension

These are controls, not U1 or 110 constructions. Every one has an independently checked nine-tetrahedron positive apex fan, actual covariance, exhaustive maximal-facet verification from all 120 vertex triples, all 17 true edges, one exact M/N pair, and all 68 physical primitives. Across the three controls there are 204 nonzero primitives and no physical weak points.

The first two use

    theta=(9/20,11/20,9/25,11/25,3/40),
    Vol=4125647/38400000,
    g=(57773902879/264041408000,
       51390622771/264041408000,
       4641647/16502588).

Their metrics are

    M_REGION=((5,1,2),(1,3,-1),(2,-1,4)),
    M_OUTSIDE=((20,5,45),(5,40,50),(45,50,141))/20.

| Control | Strict (S,U,H) | Stable facet labels | Unstable vertex labels | Weak points |
|---|---|---|---|---:|
| REGION | (5,4,7) | 0,1,3,5,6 | 2,3,4,8 | 0 |
| REGION_OUTSIDE_BASAL_FOOT | (2,3,3) | 4,7 | 6,8,9 | 0 |
| RESIDUAL_NO_BASAL_U | (4,2,4) | 0,4,6,8 | 8,9 | 0 |

For M_OUTSIDE, v=(2,1), eta=1/20, and the actual basal foot is

    (206306606879,125656974771)/264041408000.

Its coordinate sum exceeds s=37/40, so the base is not stable. Its covariance-weighted condition number is certified to exceed 1000. This checks both that basal stability is conditional on U1 and that the new geometric theorem is not silently restricted to the covariance-conditioned cone.

### A capped actual residual body with no basal U

The third control is

    theta=(1/10,9/10,3/25,3/5,2/5),
    M=((149,-455,64),(-455,4030,-340),(64,-340,104)),
    Vol=59971/600000,
    g=(91899491/479768000,
       61855619/479768000,
       115971/239884).

Its M leading minors are 149, 393445, 26988600. The three covariance-weighted eigenvalues lie respectively in

    (9/10,1), (5,6), (33,34),

as certified by exact characteristic-polynomial signs. Thus the two descending adjacent ratios are less than 34/5 and 20/3, respectively, both inside the supplied strict finite-height bounds. Those bounds are necessary for joint S1/U1, not sufficient. fileciteturn4file3L47-L53

Nevertheless **its only unstable vertices are the two top vertices 8 and 9**. Its strict saddles are edges (2,3), (5,6), (7,9), (8,9). Therefore the parent's stronger intermediate assertion, an unavoidable basal U throughout the necessary covariance cone, cannot be extended across the whole residual taper domain without an additional geometric hypothesis. This is not a counterexample to U1⇒basal stability, because this control has U=2; nor is it a counterexample to the joint exclusion target.

The failure is visible in the actual paired-end geometry, not merely in a failed coefficient test. Taking basal vertex 1 and top vertex 8 gives the core point

    (-129605119/15884000, 61855619/15884000, 0).

It violates the true basal support (-3,-1,0)·X≤-3/20 by exactly

    164671169/7942000 > 0.

All seven basal vertices have explicit positive true-edge exits in the report. The source recovers their exact values, the complete inverse, and the entire census without a numerical hull or a floating centroid.

## 6. What succeeded, what remains limited, and continuation

The successful replacement for the coarse Hausdorff comparison is **exact reflected-point membership in the actual basal polygon, coupled to actual opposite-top polar slacks**. The polar comparison point is constructed inside a genuine top-vertex dual face, rather than estimated near an auxiliary pyramid. This removes all metric-conditioning estimates from the regional proof.

The new method has a genuine geometric boundary. For fixed a, condition (C) maps a full basal polygon into itself by a planar homothety of magnitude k=gamma/(1-2gamma). Area comparison requires k≤1. At gamma=1/3, equality would make B centrally symmetric about -a/2 for every a in the top polygon, impossible for two distinct top vertices in a bounded body. Thus this particular paired-end containment cannot simply cover gamma≥1/3. The exact residual control also shows that retaining an unconditional basal U is not generally available even inside the necessary spectral cone.

The weaker relation (W), together with condition (A), already forces a basal U and a nonbasal S: for the basal statement, (W) is the negative of a convex combination of b and a, and its norm strictly increases whenever D_ba≥0. The remaining issue under that weaker hypothesis is the U1⇒basal-foot implication. That is the useful continuation target below gamma=1/3; above it, a different allocation of the necessary stable/unstable equilibria is needed. Both routes should retain the actual moment equations and the exact inverse.

Exploratory wider sufficient-test boxes and numerical metric proposals were not interpreted as infeasibility. No U1 or proper110 body was found or claimed. The retained negative construction is the fully exact residual control above. Neither failure of (C)/(A) nor negative Bernstein coefficients outside the listed boxes imply existence of a 110 body.

## 7. Complete recovery capsule and executed verification

Save the complete source below, with its final LF, as `h5_paired_end_reflection.py`. Dependencies: CPython 3.13.5 and SymPy 1.14.0. It has no parent imports, input files, random seeds, numerical optimizers, or omitted helpers. All four parameter regions and all three control metrics are literal inputs.

Run:

    python -B h5_paired_end_reflection.py > h5_paired_end_reflection.out

Expected source:

    15802 bytes
    SHA-256 700e65539e5b42ab1894200bbf58a68f414d66d87a0315d0c9dd573ec538a190

Expected report `h5_paired_end_reflection_report.json`:

    5483141 bytes
    SHA-256 1b7c0c591d80042c94e582ce6a0951541ac67ab39a5cce8cdd52510c7f1d08af

Expected stdout `h5_paired_end_reflection.out`:

    479 bytes
    SHA-256 32b2c36085a018c8e4ca7ee81f7d401995b9e9d6aa0c60c39d6d1293f71ef6e9

The final marker is `H5_PAIRED_END_REFLECTION_JOINT_REGION_V1_PASS`. I executed the source and a second build in a fresh directory containing only that source; report and stdout were byte-identical. The earlier combined command timed out during its second build; the fresh second build was then rerun to completion and compared, so no unfinished run is counted as verification.

Convenience copies: [source](sandbox:/mnt/data/h5_paired_end_reflection.py), [complete exact report](sandbox:/mnt/data/h5_paired_end_reflection_report.json), [verification output](sandbox:/mnt/data/h5_paired_end_reflection.out). These links supplement the complete embedded recovery source, not replace it.

```python
#!/usr/bin/env python3
"""H5_PAIRED_END_REFLECTION_JOINT_REGION_V1.
CPython 3.13.5, SymPy 1.14.0; no input files, random choices, or solvers.
Exact moving moments, scalar Bernstein certificates with inverse power checks,
and complete same-inverse physical audits. The geometric proof is in the handoff.
"""
import hashlib
import itertools
import json
import sys
from fractions import Fraction as F
from math import comb
from pathlib import Path
import sympy as S

R = S.Rational
FACETS = ((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
          (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
EDGES = tuple(sorted({tuple(sorted((f[i],f[(i+1)%len(f)])))
                      for f in FACETS for i in range(len(f))}))
EF = tuple(tuple(k for k,f in enumerate(FACETS) if a in f and b in f)
           for a,b in EDGES)
ARROWS = tuple(sorted((i,j) for a,b in EDGES for i,j in ((a,b),(b,a))))
DUAL = tuple(sorted((i,j) for a,b in EF for i,j in ((a,b),(b,a))))
SIDE_FACETS = (1,3,4,5,6,7,2)
x,r,p,q,l = VARS = S.symbols('x r p q l')
CASES = (
    ('FULL_BASAL','triangle',('0','1'),('0','1'),'1/300'),
    ('BROAD','direct',('1/10','9/10'),('1/5','1/2'),'1/100'),
    ('WIDE','direct',('1/5','4/5'),('1/5','1/2'),'1/40'),
    ('DEEP','direct',('2/5','3/5'),('3/10','1/2'),'3/40'),
)
REGION_THETA = ('9/20','11/20','9/25','11/25','3/40')
COUNTER_THETA = ('1/10','9/10','3/25','3/5','2/5')
CONTROLS = (
    ('REGION',REGION_THETA,((5,1,2),(1,3,-1),(2,-1,4)),1,None),
    ('REGION_OUTSIDE_BASAL_FOOT',REGION_THETA,
     ((20,5,45),(5,40,50),(45,50,141)),20,
     (('1/10000','1/5000'),('1/50','3/100'),('6/25','1/4'))),
    ('RESIDUAL_NO_BASAL_U',COUNTER_THETA,
     ((149,-455,64),(-455,4030,-340),(64,-340,104)),1,
     (('9/10','1'),('5','6'),('33','34'))),
)


def enc(v):
    if isinstance(v,S.MatrixBase):
        return [[str(v[i,j]) for j in range(v.cols)] for i in range(v.rows)]
    if isinstance(v,(S.Basic,F)):
        return str(v)
    if isinstance(v,dict):
        return {str(k):enc(a) for k,a in v.items()}
    if isinstance(v,(list,tuple)):
        return [enc(a) for a in v]
    return v


def pd(A):
    assert A == A.T
    mm=[S.factor(A[:k,:k].det()) for k in range(1,A.rows+1)]
    assert all(a>0 for a in mm)
    return mm


def vertices(theta):
    xx,rr,pp,qq,la=theta; ss=1-la
    B=((ss/4,0),(ss*(1-3*xx/4),0),(ss*(1-pp),ss*pp),
       (ss*qq,ss*(1-qq)),(0,ss*(1-3*rr/4)),(0,ss/4),(ss/16,ss/16))
    return tuple(S.Matrix((a,b,0)) for a,b in B)+(S.Matrix((0,0,1)),
           S.Matrix((la,0,1)),S.Matrix((0,la,1)))


def moments(z,apex=None):
    D=S.Integer(0); K=S.zeros(3,1); L=S.zeros(3); cells=[]
    o=S.zeros(3,1) if apex is None else z[apex]
    for f in FACETS:
        if apex is not None and apex in f:
            continue
        for j in range(1,len(f)-1):
            a,b,c=(z[k] for k in (f[0],f[j],f[j+1]))
            d=(a-o).dot((b-o).cross(c-o))
            if apex is not None:
                assert d>0
                cells.append((apex,f[0],f[j],f[j+1],d))
            t=o+a+b+c
            D+=d; K+=d*t/4
            L+=d*(t*t.T+sum((u*u.T for u in (o,a,b,c)),S.zeros(3)))/20
    return S.expand(D),K.applyfunc(S.expand),L.applyfunc(S.expand),cells


def polynomial_model():
    ss=1-l; area=(31-24*x*p-24*r*q)/64
    bx=R(509,3072)-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8
    by=R(509,3072)-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
    D=l+2*area*ss*ss
    K=S.Matrix((3*ss**3*bx/2+ss*ss*l*(1-3*x*p/4)/4+l*l/4,
                3*ss**3*by/2+ss*ss*l*(1-3*r*q/4)/4+l*l/4,
                area*ss*ss/2+l/2+l*l/4))
    z=vertices(VARS); DD,KK,LL,_=moments(z)
    assert S.expand(D-DD)==0 and (K-KK).applyfunc(S.expand)==S.zeros(3,1)
    assert S.expand(4*K[2]-D-l*(1+l))==0
    nh=(((0,-1),0,0),((p,p-3*x/4),ss*p*(1-3*x/4),l*p),
        ((1,1),ss,l),((q-3*r/4,q),ss*q*(1-3*r/4),l*q),
        ((-1,0),0,0),((-3,-1),-ss/4,0),((-1,-3),-ss/4,0))
    polys={'gamma_quarter':S.expand(4*K[2]-D),
           'gamma_third':S.expand(D-3*K[2])}
    for e,(n,h,t) in enumerate(nh):
        n3=S.Matrix((n[0],n[1],h-t))
        for j in FACETS[SIDE_FACETS[e]]:
            assert S.expand(n3.dot(z[j])-h)==0
        H=S.expand(D*h-n3.dot(K)); polys[f'H{e}']=H
        for i in range(7):
            for j in range(3):
                w=z[i]+z[7+j]
                polys[f'C{e}_{i}_{j}']=S.expand((D-2*K[2])*h-n[0]*K[0]
                              -n[1]*K[1]+K[2]*(n[0]*w[0]+n[1]*w[1]))
        for j in range(3):
            a=z[7+j]
            polys[f'T{e}_{j}']=S.expand(2*H-D*(t-n[0]*a[0]-n[1]*a[1]))
    assert len(polys)==177
    return z,S.expand(D),K,LL,nh,polys


def bernstein(f,box):
    """Tensor conversion, then independently expand the full Bernstein basis."""
    po=S.Poly(f,*VARS); deg=tuple(map(int,po.degree_list()))
    cur={e:F(int(c.p),int(c.q)) for e,c in po.terms()}
    for i,(lo,hi) in enumerate(box):
        nxt={}
        for e,c in cur.items():
            for j in range(e[i]+1):
                ee=e[:i]+(j,)+e[i+1:]
                v=c*comb(e[i],j)*lo**(e[i]-j)*(hi-lo)**j
                nxt[ee]=nxt.get(ee,F(0))+v
        cur={e:c for e,c in nxt.items() if c}
    powers=cur.copy()
    for i,n in enumerate(deg):
        nxt={}
        for e,c in cur.items():
            for j in range(e[i],n+1):
                ee=e[:i]+(j,)+e[i+1:]
                v=c*F(comb(j,e[i]),comb(n,e[i]))
                nxt[ee]=nxt.get(ee,F(0))+v
        cur=nxt
    inds=tuple(itertools.product(*(range(n+1) for n in deg)))
    coeff=tuple(cur.get(e,F(0)) for e in inds)
    back=dict(zip(inds,coeff))
    for i,n in enumerate(deg):
        nxt={}
        for e,c in back.items():
            for j in range(e[i],n+1):
                ee=e[:i]+(j,)+e[i+1:]
                v=c*comb(n,e[i])*comb(n-e[i],j-e[i])*(-1)**(j-e[i])
                nxt[ee]=nxt.get(ee,F(0))+v
        back={e:c for e,c in nxt.items() if c}
    assert back==powers
    return deg,inds,coeff


def certificates(polys):
    results=[]
    triangle={n:S.expand(f.subs(q,(1-p)*q)) for n,f in polys.items()}
    for name,mode,xr,pq,hi in CASES:
        box=[tuple(map(F,xr))]*2+[tuple(map(F,pq))]*2+[(F(0),F(hi))]
        use=triangle if mode=='triangle' else polys
        records=[]; groups={}
        for n,f in use.items():
            deg,inds,co=bernstein(f,box)
            assert min(co)>=0 and max(co)>0
            if mode=='direct' and n!='gamma_quarter':
                assert min(co)>0
            # In the full basal chart the first four variables are OPEN.
            # This explicitly checks strict positivity on the taper's upper face.
            top=[c for e,c in zip(inds,co) if e[-1]==deg[-1]]
            assert max(top)>0
            group=n if n.startswith('gamma') else n[0]
            if group not in groups:
                groups[group]={'polynomials':0,'coefficients':0,'zero':0,
                               'minimum':None,'minimum_positive':None}
            gg=groups[group]; gg['polynomials']+=1; gg['coefficients']+=len(co)
            gg['zero']+=sum(c==0 for c in co)
            a=min(co); b=min(c for c in co if c>0)
            gg['minimum']=a if gg['minimum'] is None else min(gg['minimum'],a)
            gg['minimum_positive']=b if gg['minimum_positive'] is None else min(gg['minimum_positive'],b)
            records.append({'polynomial':n,'degree':deg,'coefficients':co,
                            'upper_taper_face_has_positive_coefficient':True})
        results.append({'name':name,'chart':mode,'box':box,'groups':groups,
                        'strict_scope':'Genuine H5 only; lambda>0. In triangle chart x,r,p,w are open and q=(1-p)w.',
                        'coefficient_order':'lexicographic product(range(degree[i]+1), i=0..4)',
                        'records':records,'inverse_power_reconstructions':len(records)})
    return results


def geometric_identities():
    ga,m=S.symbols('ga m'); k=ga/(1-2*ga); theta=(1-2*ga)**2/ga
    al=(1-2*ga)/(1-ga+ga*m); be=ga*(1+m)/(1-ga+ga*m)
    checks=(theta*k-(1-2*ga),theta*k+(1-theta)*ga/(1-ga)-2*ga,
            1-theta-(1-ga)*(4*ga-1)/ga,al+be-1,
            -al*m+be*(1-ga)/ga-1,
            -al*(-1-2*ga*m)/(1-2*ga)-be-1)
    assert all(S.factor(t)==0 for t in checks)
    a=S.Matrix(S.symbols('a0:3')); b=S.Matrix(S.symbols('b0:3'))
    assert S.expand((a+b).dot(a+b)-4*b.dot(b)-4*b.dot(a-b)-(a-b).dot(a-b))==0
    beta=S.symbols('beta')
    w=b+beta*(a-b)
    assert S.expand(w.dot(w)-b.dot(b)-2*beta*b.dot(a-b)-beta**2*(a-b).dot(a-b))==0
    return {'identities_checked':8,'k':k,'theta':theta,'alpha':al,'beta':be}


def audit(z,g,poles,M,N):
    assert M*N==S.eye(3)
    X=tuple(a-g for a in z)
    P={(i,j):(X[i].T*M*(X[j]-X[i]))[0] for i,j in ARROWS}
    Q={(i,j):(poles[i].T*N*(poles[j]-poles[i]))[0] for i,j in DUAL}
    U=[i for i in range(10) if all(v<0 for (a,b),v in P.items() if a==i)]
    stable=[i for i in range(9) if all(v<0 for (a,b),v in Q.items() if a==i)]
    saddles=[]; weak={}
    for (i,j),(a,b) in zip(EDGES,EF):
        vals=(P[i,j],P[j,i],Q[a,b],Q[b,a])
        if max(vals)<0:
            saddles.append((i,j))
        if max(vals)<=0 and any(v==0 for v in vals):
            pp=next((X[k] for k,ll in ((i,j),(j,i)) if P[k,ll]==0),None)
            qq=next((N*poles[k]/(poles[k].T*N*poles[k])[0]
                     for k,ll in ((a,b),(b,a)) if Q[k,ll]==0),None)
            if pp is not None and qq is not None:
                assert pp==qq
            w=pp if pp is not None else qq; assert w is not None
            kind='VF' if pp is not None and qq is not None else ('VE' if pp is not None else 'EF')
            key=tuple(w)
            if key not in weak:
                weak[key]={'point':w,'kind':kind,'edges':[]}
            weak[key]['edges'].append((i,j))
            if kind=='VF':
                weak[key]['kind']='VF'
    assert len(stable)+len(U)-len(saddles)==2
    return {'S':stable,'U':U,'H':saddles,'weak':list(weak.values()),
            'counts':(len(stable),len(U),len(saddles)),
            'primal':[(i,j,P[i,j]) for i,j in ARROWS],
            'polar':[(i,j,Q[i,j]) for i,j in DUAL],
            'zero_primitives':sum(v==0 for v in tuple(P.values())+tuple(Q.values()))}


def control(data,polys,nh):
    name,th,nums,den,brackets=data; th=tuple(map(R,th)); subs=dict(zip(VARS,th))
    xx,rr,pp,qq,la=th
    assert 0<xx<1 and 0<rr<1 and pp>0 and qq>0 and pp+qq<1 and 0<la<1
    z=vertices(th)
    assert len(set(map(tuple,z)))==10
    hull=set()
    for i,j,k in itertools.combinations(range(10),3):
        n=(z[j]-z[i]).cross(z[k]-z[i])
        if n==S.zeros(3,1):
            continue
        hh=[n.dot(a-z[i]) for a in z]
        if max(hh)<=0 or min(hh)>=0:
            hull.add(tuple(a for a in range(10) if hh[a]==0))
    assert hull=={tuple(sorted(f)) for f in FACETS}
    assert 10-len(EDGES)+len(FACETS)==2
    D,K,L,_=moments(z); d2,k2,l2,cells=moments(z,7)
    assert D==d2 and K==k2 and L==l2 and len(cells)==9 and D>0
    g=K/D; C=(L/D-g*g.T).applyfunc(S.factor); pd(C)
    poles=[]; supports=[]
    for f in FACETS:
        a,b,c=(z[j] for j in f[:3]); n=(b-a).cross(c-a); h=n.dot(a)
        assert n!=S.zeros(3,1)
        for j in range(len(f)):
            u=z[f[(j+1)%len(f)]]-z[f[j]]
            v0=z[f[(j+2)%len(f)]]-z[f[(j+1)%len(f)]]
            assert n.dot(u.cross(v0))>0
        slacks=[h-n.dot(z[j]) for j in range(10)]
        assert all(slacks[j]==0 if j in f else slacks[j]>0 for j in range(10))
        H=h-n.dot(g); assert H>0
        poles.append(n/H); supports.append({'normal':n,'offset':h,'vertex_slacks':slacks})
    for e,(n,h,t) in enumerate(nh):
        n3=S.Matrix((n[0],n[1],h-t)).subs(subs); hh=S.sympify(h).subs(subs)
        assert n3/(hh-n3.dot(g))==poles[SIDE_FACETS[e]]
    M=S.Matrix(nums)/den; mmin=pd(M); N=M.inv(); pd(N)
    cc=audit(z,g,poles,M,N)
    assert not cc['weak'] and cc['zero_primitives']==0
    vals={n:S.factor(f.subs(subs)) for n,f in polys.items()}
    G=M[:2,:2]; v=G.inv()*M[:2,2]; eta=M[2,2]-(v.T*G*v)[0]
    beta=g[:2,0]+g[2]*v
    assert eta>0
    spectrum=None
    if brackets:
        brackets=tuple(tuple(map(R,b)) for b in brackets); Z=C*M
        signs=[]
        for a,b in brackets:
            fa=S.factor((Z-a*S.eye(3)).det()); fb=S.factor((Z-b*S.eye(3)).det())
            assert fa*fb<0; signs.append((fa,fb))
        spectrum={'ordered_eigenvalue_intervals':brackets,'characteristic_endpoint_determinants':signs}
    extra={}
    if name=='RESIDUAL_NO_BASAL_U':
        assert cc['S']==[0,4,6,8] and cc['U']==[8,9] and cc['counts']==(4,2,4)
        assert brackets[2][1]/brackets[1][0]<R(7024915,1000000)
        assert brackets[1][1]/brackets[0][0]<R(6832329,1000000)
        exits=[next((i,j,d) for i,j,d in cc['primal'] if i==a and d>0) for a in range(7)]
        nameC=min((n for n in vals if n.startswith('C')),key=vals.get)
        assert vals[nameC]<0 and R(1,3)<g[2]<R(1,2)
        e,i,j=map(int,nameC[1:].split('_')); a=z[7+j]
        point=(g-g[2]*(z[i]+a))/(1-2*g[2]); nn,hh,tt=nh[e]
        nn=S.Matrix((nn[0],nn[1],0)).subs(subs); hh=S.sympify(hh).subs(subs)
        assert point[2]==0 and nn.dot(point)>hh
        extra={'positive_basal_exits':exits,'failed_core_guard':nameC,
               'failed_core_guard_value':vals[nameC],'core_point_outside_base':point,
               'violated_basal_support_normal':nn,'violated_basal_support_offset':hh,
               'support_excess':nn.dot(point)-hh,'inside_strict_joint_spectral_caps':True}
    else:
        assert min(vals.values())>0 and any(i<7 for i in cc['U']) and any(i!=0 for i in cc['S'])
        if name=='REGION_OUTSIDE_BASAL_FOOT':
            assert sum(beta)>1-la and 0 not in cc['S'] and len(cc['U'])>=2
            assert brackets[2][0]/brackets[0][1]>1000
            extra['covariance_weighted_condition_exceeds']=1000
        else:
            assert cc['counts']==(5,4,7)
    return {'name':name,'theta':th,'vertices':z,'facets':FACETS,'edges':EDGES,
            'exhaustive_supporting_triple_hull':sorted(hull),
            'supports':supports,'volume':D/6,'actual_centroid':g,'actual_covariance':C,
            'positive_apex_fan_six_volumes':cells,'poles':poles,'M':M,'N':N,
            'metric_leading_minors':mmin,'G':G,'v':v,'eta':eta,'basal_foot':beta,
            'census':cc,'geometric_guard_values':vals,'spectral_certificate':spectrum,'extra':extra}


def main():
    assert S.__version__=='1.14.0'
    assert len(EDGES)==17 and len(ARROWS)==len(DUAL)==34 and all(len(a)==2 for a in EF)
    z,D,K,L,nh,polys=polynomial_model()
    certs=certificates(polys); controls=[control(c,polys,nh) for c in CONTROLS]
    report={'identity':'H5_PAIRED_END_REFLECTION_JOINT_REGION_V1',
            'environment':{'python':sys.version.split()[0],'sympy':S.__version__},
            'scope':'No S=U=1 for every SPD on the four stated genuine-H5 regions; incidental weak contacts allowed. Not an all-metric U>=2 theorem or whole-H5 exclusion.',
            'geometry_algebra':geometric_identities(),'actual_six_volume':D,
            'actual_six_first_moment':K,'actual_six_second_moment':L,
            'scalar_polynomial_count':len(polys),'certificates':certs,'controls':controls,'status':'PASS'}
    raw=(json.dumps(enc(report),sort_keys=True,indent=2)+'\n').encode()
    out=Path('h5_paired_end_reflection_report.json'); out.write_bytes(raw)
    for c in certs:
        ng=sum(g['coefficients'] for g in c['groups'].values())
        nz=sum(g['zero'] for g in c['groups'].values())
        print(c['name'],'POLYNOMIALS',len(c['records']),'COEFFICIENTS',ng,'ZERO',nz)
    for c in controls:
        print(c['name'],c['census']['counts'],'WEAK',len(c['census']['weak']),'ZERO',c['census']['zero_primitives'])
    print(out.name,len(raw),hashlib.sha256(raw).hexdigest())
    print('H5_PAIRED_END_REFLECTION_JOINT_REGION_V1_PASS')


if __name__=='__main__':
    main()
```
