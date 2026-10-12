# minimum-0207

AI research report · 2026-09-23 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# HEX6_GLOBAL_FIXED_POLE_ATLAS_AND_COMPACT_METRIC_BOUNDARY_V3

## 1. Result and scope

The prescribed six-pole completion problem now has a **complete global realization atlas**, not merely a chart near the small-cut bodies. Every uniformly filled, own-centred realization with the specified six apex planes and the supplied labelled 10/17/9 lattice is obtained uniquely from the full open five-cut cube by vertex-centred projectivity followed by actual uniform-volume centring.

The virtual-pyramid horizon does **not** create an unbounded branch of actual normalized bodies. For the literal six-pole geometry below, the entire completion class satisfies the explicit bounds

    |c_x|, |c_y|, |c_z| < 23000,
    0 < c_z < 3/4,
    1+c·(Y_i-A) > 1/1000000  for every ACTUAL source vertex,

and every resulting own-centred body P satisfies

    P ⊂ [-25/3,25/3] × [-40/3,40/3] × [-7,5],
    [-10^(-19),10^(-19)]^3 ⊂ P,
    Vol(P) > 4/56953125.

These are deliberately conservative exact bounds. They cover all five independent cut fractions in (0,1), including deep completions and bodies whose released virtual pyramid is unbounded. They do not assume any equilibrium class or any bound on a physical metric.

The bounds yield a new description of the remaining metric boundary. Put

    r=10^(-19), R=18,
    Gamma=(R/r)^2=324·10^38,
    Kappa=(R/r)^4=104976·10^76.

If apex A is the sole strict U under an SPD metric M, then

    lambda_max(M)/lambda_middle(M) < Gamma.

Consequently, a singular limit of normalized sole-U metrics can have rank **two**, but not rank one. If the same physical pair M,N=M^-1 also has exactly one strict S, then

    condition_number(M) < Kappa.

Thus simultaneous S1/U1 has an explicit compact, nonsingular common-metric search envelope over the whole fixed-pole completion class. Sole U1 still has a possible rank-two metric boundary. Neither statement infers H=0 or absence of weak contacts from U1.

A second global consequence concerns the coordinator’s degree-seven direction: after choosing one of its two nonapical facets, every fixed-pole degree-seven E17 realization reduces to a **single plane cut of a fixed bounded seven-gonal pyramid**, even when the given released pyramid was unbounded. Its labelled incidence domains are three-dimensional open polyhedra defined by linear inequalities on the cut-plane coefficients.

No new full-U1 or110 witness is claimed, and no new all-SPD U1 exclusion of the entire five-cut cube is claimed. The mechanical interval remains unchanged. The durable advance here is the global atlas, the effective actual-body compactification, and the precise remaining metric boundary.

## 2. Exact source identity and geometry

The immutable scientific parent is

    minimum-0203
    SHA256 afe1de89443d478069ffce2a0c36375fc3fb7e039137eb7ba4299106211dca19
    HEX6_INDEPENDENT_COMPLETION_NONAPICAL_MAXIMUM_V2.

The fixed planar poles are the parent’s CHANGED hexagon, not its original integer hexagon and not either degree-five pentagon control:

    p = 1/100000 * (
      (60401,-32565),
      (80000,-20000),
      (0,60000),
      (-80000,80000),
      (-483861,-325040),
      (-447814,-355009)).

Set

    A=(0,0,1), q_i=(p_i,1),
    s0=(-1743742,-1088172,1000000)/1000000,
    b=-3s0=(2615613/500000,816129/250000,-3),
    beta0=b/4.

Define the six vertices of the fixed virtual base by

    B_i=[q_i;q_((i+1) mod 6);b]^-1(1,1,1).

For five independent fractions (x,y,z,u,v) in (0,1)^5, the actual source vertices are

    Y0=A,
    Y1=B1, Y2=B2, Y3=B4, Y4=B5,
    Y5=B0+x(A-B0),
    Y6=B0+y(B5-B0),
    Y7=B0+z(B1-B0),
    Y8=B3+u(A-B3),
    Y9=B3+v(B4-B3).

The true maximal facets, in cyclic order, are

    F0=(0,4,6,5), F1=(0,5,7,1), F2=(0,1,2),
    F3=(0,2,8), F4=(0,8,9,3), F5=(0,3,4),
    F6=(4,3,9,2,1,7,6), F7=(5,6,7), F8=(9,8,2).

The true edges are

    01,02,03,04,05,08,12,17,28,29,34,39,46,56,57,67,89.

The partial cut at B3 passes through the EXISTING vertex B2. It is not a generic second truncation. Throughout the open cube the counts are exactly 10/17/9; vertex0 has degree six, vertex2 has degree four, and the other vertices are simple.

Write U_i=Y_i-A. A star projectivity is

    T_c(Y)=A+(Y-A)/(1+c·(Y-A)).

Only positivity at the ten ACTUAL vertices is required. Positivity at removed B0 or B3 is not required.

## 3. A global base-straightening lemma

Let C be a pointed full-dimensional cone with apex at the origin. Suppose a bounded convex body in A-relative coordinates has one genuine nonapical facet

    beta·w=1,

and lies in beta·w≤1. Choose any beta0 strictly positive on C\{0}. Put

    e=beta0-beta.

For every actual w in the body,

    1+e·w=(1-beta·w)+beta0·w>0,

except at w=0, where it equals1. Therefore the projectivity

    w -> w/(1+e·w)

is positive on the entire ACTUAL body. It fixes all planes through the apex and sends the chosen facet to

    beta0·w'=1.

The image is contained in the bounded pyramid C∩{beta0·w'≤1}.

This argument does not evaluate a denominator at any removed virtual vertex. It therefore applies equally to a body with a bounded or an unbounded released virtual pyramid.

For the literal hexagon, beta0=b/4 is strictly positive on the apex cone. One exact way to see this is that (s0_x,s0_y) lies in the interior of the triangle with vertices p1,p2,p4. In particular, with

    t=1715957/4344505,
    mu1=(5/4)(s0_x-p4_x t),
    mu2=1-t-mu1,

all of mu1,mu2,t are positive and

    (s0_x,s0_y)=mu1 p1+mu2 p2+t p4.

Hence beta0 is a negative positive combination of three independent q_i, and is strictly positive on the cone defined by q_i·w≤0.

## 4. Complete five-cube atlas

Consider any actual own-centred body with precisely the fixed q0,...,q5 as its six apex planes and with the labelled maximal facets above. Normalize its F6 plane by the base-straightening lemma.

After normalization, vertices1,2,3,4 are forced to be B1,B2,B4,B5 by their true plane intersections. The other five vertices lie on the following fixed edges:

    5 on B0A,
    6 on B0B5,
    7 on B0B1,
    8 on B3A,
    9 on B3B4.

Their fractions are strictly between0 and1. Reaching either endpoint would change the stipulated true lattice. Thus every normalized realization has exactly the five-cut form in section2.

Conversely, every point of (0,1)^5 gives that actual lattice. The first removed tetrahedron is contained in the apex ear conv(A,B0,B5,B1). The second is contained in conv(A,B2,B3,B4). Those two ears have disjoint interiors. In local edge coordinates at B0, the retained inequality is

    alpha/x+beta/y+gamma/z≥1.

At B3 it is

    alpha+beta/u+gamma/v≥1.

The latter has B2=(1,0,0) on its plane. All other required old vertices and the first cut’s new vertices are strictly retained. This establishes the whole open-cube geometry, not just a sample of cut fractions.

### Actual uniform centring, not transported old mass

For any source member there is a unique c with positive ACTUAL denominators for which T_c(P_source), uniformly refilled, has centroid0.

For completeness, this follows from the star-centering potential. With K=P_source-A and z=-A, let

    V(c)=integral_K (1+c·w)^(-4) dw,
    F(c)=log V(c)+4c·z.

If m_c and Sigma_c are the actual centroid and covariance of the uniformly filled image of K, then

    grad log V=-4m_c,
    Hess log V=20 Sigma_c+4m_c m_c^T>0.

Finite positive-denominator boundaries make V diverge. Along an unbounded sequence of parameters, normalized directions approach the dual cone C*, and z∈int C makes the linear term coercive. The logarithm has the lower bound log Vol(K)-4 log(1+R0|c|). Hence F has a unique interior minimizer, and its equation is exactly m_c=z.

The atlas is injective as well as surjective. Two source members with the same centred image would differ by a star projectivity preserving the fixed base plane beta0·w=1. If its parameter is e, preservation on an open part of this plane requires e·w=0 there, so e=0. The five fractions then coincide. The normalizer is rational in the geometric data; the centring map is analytic by the positive Hessian. Thus the open five-cube is a global analytic realization atlas for this labelled fixed-pole class.

This is a set normalization followed by genuine uniform refill. No claim is made that the first normalization preserves the old centroid, equilibrium signs, or physical density.

## 5. Effective compactification of the WHOLE atlas

### 5.1. A uniform support bound from actual volume

For any uniformly filled full-dimensional polytope with centroid0 and any valid support q·X≤1,

    -3≤q·X≤1  on the entire body.

Indeed, put h=1-q·X≥0. Cone a genuine boundary triangulation from any vertex W. Every tetrahedron in this actual volume fan has mean h at least h(W)/4. Since the actual body mean is h(g)=1, h(W)≤4. Convexity extends the result from vertices to the body.

Use the three fixed supports q1,q2,q3. If a=q1·X, b1=q2·X, c1=q3·X, direct inversion gives

    X_x=-(5/12)a+(25/12)b1-(5/3)c1,
    X_y=-(5/3)a+(10/3)b1-(5/3)c1,
    X_z=a-b1+c1.

With all three support values in [-3,1],

    |X_x|≤25/3, |X_y|≤40/3, -7≤X_z≤5.

In particular |X-A|_infinity<14 and |X|_Euclidean<18. This bound already applies to any actual own-centred completion with these supports; it does not use the two-cut chart.

### 5.2. The sign and upper bound of c_z

The transformed F6 plane is

    (beta0+c)·(X-A)=1.

Its positive absolute support offset is h0=1/4+c_z, and its normalized pole satisfies

    1-q6·A=1/h0.

Coning the actual volume from A and applying the preceding support argument gives h0≥1/4. The inequality is strict in the open five-cube: for example, Y5 is off F6, and the positive-volume cone over F7 contributes a strictly positive additional base-height term. Hence c_z>0.

### 5.3. A common retained tetrahedron and an explicit parameter bound

The source tetrahedron conv(A,B1,B2,B4) is retained for every cut vector. The following formulas prove that0 is strictly inside it and give useful uniform constants.

Write

    a0=2615613/500000, b0=816129/250000,
    R0=29969, S0=36047,
    T0=26217547189/100000,
    K1=a0+b0+9/5,
    K2=a0+4b0+36/5,
    D0=3T0-a0 R0-b0 S0,
    h=(T0+108141/5)^(-1).

Then

    B1-A=(4/K1)(1,1,-3/5),
    B2-A=(4/K2)(1,4,-12/5),
    B4-A=-(4/D0)(R0,S0,T0).

The barycentric weights of0 in the retained tetrahedron are

    lambda0=1/4,
    lambda1=27943 K1 h/4,
    lambda2=2026 K2 h/4,
    lambda4=D0 h/4.

They sum to1; each nonapical weight exceeds1/100. These assertions follow directly from the displayed identities and the rational bounds

    10<K1<12, 25<K2<30,
    262000<T0<263000,
    D0>460000,
    T0+108141/5<285000.

Let d_i=1+c·(B_i-A) for the three retained base vertices. The barycentric identity gives

    lambda1 d1+lambda2 d2+lambda4 d4=3/4-c_z.

Consequently c_z<3/4 and 0<d1,d2,d4<75.

Let U be the matrix with rows B1-A,B2-A,B4-A. Its entries have absolute value less than3, and

    |det U|=192/(K1 K2 D0 h)>8/45.

Cofactor bounds therefore give ||U^-1||_infinity<304. Since Uc=(d1-1,d2-1,d4-1),

    |c|_infinity<304·75<23000.

### 5.4. Uniform ACTUAL denominator, volume and inradius bounds

For every actual source vertex, write X=A+U_i/d_i. The identity

    1=d_i[1-c·(X-A)]

and the preceding bounds imply

    d_i>1/(1+3·23000·14)=1/966001>1/1000000.

The virtual B0 and B3 are intentionally absent from this conclusion.

The retained tetrahedron has source volume greater than4/135. Under the star projectivity its volume is divided by d1 d2 d4, so

    Vol(P)>Vol(T_retained)>4/(135·75^3)=4/56953125.

The barycentric weights of the ACTUAL origin in the transformed retained tetrahedron are exactly

    (1/4+c_z, lambda1 d1, lambda2 d2, lambda4 d4).

All four exceed10^(-8). Every coordinate difference between two vertices is smaller than28. Thus an unnormalized face normal of the retained tetrahedron has l1 norm at most4704. Its value at the origin, on the inward side, exceeds

    10^(-8)·6 Vol(T_retained)>24/(56953125·10^8).

Since

    4704·10^(-19)<24/(56953125·10^8),

the entire cube [-10^(-19),10^(-19)]^3 lies strictly inside that tetrahedron and hence inside P.

In particular every actual polar point satisfies ||q||_1≤10^19. Both primal and polar actual geometry remain bounded through a virtual-pyramid horizon.

The same argument extends the centring map continuously to the closed source cube. The common retained tetrahedron keeps the body full-dimensional and the target strictly inside the appropriate apex cone. Some labelled vertices or maximal facets may merge on this boundary; those boundary objects are not silently counted as10/17/9.

## 6. The exact virtual-horizon geometry

The released body is the intersection of the six fixed apex halfspaces and the transformed F6 halfspace. Its cone has extreme rays B_i-A. Therefore the released body is bounded if and only if

    1+c·(B_i-A)>0  for all six virtual base vertices.

Four of them are actual retained vertices. Thus the only possible virtual horizons in this atlas are

    1+c·(B0-A)=0,
    1+c·(B3-A)=0.

A zero or negative value gives a genuine unbounded ray of the RELEASED body. It does not make the actual clipped body unbounded.

The actual denominators record precisely how a cut protects the body from that horizon:

    d5=x+(1-x)d_B0,
    d6=(1-y)d_B0+y d_B5,
    d7=(1-z)d_B0+z d_B1,
    d8=u+(1-u)d_B3,
    d9=(1-v)d_B3+v d_B4.

Every one of these exceeds10^(-6). For example, if d_B3<0, necessarily

    u>(10^(-6)-d_B3)/(1-d_B3),
    v>(10^(-6)-d_B3)/(d_B4-d_B3).

These are actual positivity restrictions, not a requirement that the removed virtual vertex be projectively admissible. The parent’s horizon countercontrol is therefore a manifestation of an internal atlas wall, rather than an escape to unbounded actual geometry.

## 7. What the global bounds imply for U1 and110

### 7.1. A spectral two-half obstruction

Let a convex polytope contain the Euclidean ball of radius r about0 and be contained in the ball of radius R. Let M have eigenvalues lambda1≥lambda2≥lambda3>0. If

    lambda1 r^2≥lambda2 R^2,

there are at least TWO strict U vertices.

To prove this, cut by the central plane perpendicular to a largest-eigenvalue direction. Every section point has M-norm squared at most lambda2 R^2. Each open half contains a vertex with M-norm squared at least lambda1 r^2. In either half choose a vertex of maximum M-norm among the vertices of that half. Its arrows to vertices in the same half are negative by strict convexity of the quadratic norm. If a true edge crosses the central plane, its section point has no larger norm; the positive quadratic edge term then makes the outgoing derivative at the chosen vertex strictly negative. This proves a strict U in each half. Equality in the displayed spectral condition is included.

For the complete hexagon fibre, sole U therefore requires lambda1/lambda2<Gamma. This is a necessary condition, not a sufficiency test.

### 7.2. Sole U at A: the remaining singular boundary has rank two

A sole strict U must also be the unique global vertex of maximum M-norm. Normalize M by A^T M A=M33=1. The inner ball then gives

    lambda_max(M)≤r^(-2)=10^38.

At the same time lambda1≥1, and the two-half theorem gives lambda2>1/Gamma. Thus a convergent singular sequence of these normalized metrics has rank exactly two. Rank-one limits and unbounded entries are excluded uniformly over the WHOLE completion atlas.

In the supplied reciprocal slice coordinates,

    M=[[K+ff^T,f],[f^T,1]], K SPD,

apex U requires f in the interior of the fixed planar hexagon. The possible singular boundary is therefore a nonzero rank-one limit of K, not K=0. This is the remaining noncompact conditioning mechanism for U1 alone; no positive lower bound on lambda_min(M) is asserted under U1 alone.

### 7.3. Simultaneous strict S1 and U1: an explicit condition bound

A stable primal facet is a strict unstable vertex of the ACTUAL polar under N=M^-1. Indeed its metric foot is Nq/(q^T Nq), and the strict adjacent support inequalities are exactly q^T N(q'-q)<0. The polar is not uniformly refilled or recentered.

The polar contains the ball of radius1/R and is contained in the ball of radius1/r. Applying the two-half theorem to N shows that strict S1 also requires

    lambda2(M)/lambda3(M)<Gamma.

Together with U1,

    condition_number(M)<Kappa.

With M33=1, lambda_min(M)>1/Kappa. In the K,f chart this yields the closed overcover

    Kappa^(-1) I ≤ K ≤ 10^38 I,
    f in the closed fixed hexagon.

All genuine S1/U1 candidates lie in its interior where required. This is ONE physical reciprocal pair, not independently feasible primal and polar metrics. H0 and weak-contact freedom must still be checked separately.

## 8. Exact actual-centroid and mechanical formulation

The seven positive apex-fan tetrahedra have nonapical triples

    (4,3,9), (4,9,2), (4,2,1), (4,1,7), (4,7,6),
    (5,6,7), (9,8,2).

For each triple T={i,j,k}, let a_T=|det(U_i,U_j,U_k)|/6. Define

    d_i(c)=1+c·U_i,
    W(c)=product_(i=1)^9 d_i(c),
    Z(c)=sum_T a_T product_(i not in {0} union T) d_i(c).

The ACTUAL uniformly refilled volume is V(c)=Z(c)/W(c). Its centroid is0 exactly when

    Z_x W-Z W_x=0,
    Z_y W-Z W_y=0,
    Z_z W-Z W_z-4ZW=0.

These three polynomials have degrees at most14,14,15 in c. Their positive-domain solution is unique. The equations do not involve any denominator at removed B0 or B3 and do not use independently assigned tetrahedral masses.

For true primal edge i--j, put X_i=Z_i/d_i with Z_i=d_i A+U_i. The sign of its physical primitive is the sign of

    Z_i^T M(U_j d_i-U_i d_j),

because its omitted denominator d_i^2 d_j is positive. A sole-U0 system is equivalently a union of the true rooted-at-0 weak escape-tree systems. The strict norm growth along a weak arrow is

    |X_j|_M^2-|X_i|_M^2=2D_ij+|X_j-X_i|_M^2>0.

Thus the lower trapped set in the parent’s half-cut control cannot be ignored merely because its highest nonroot vertex has an escape to A.

For any raw facet n·Y≤b_f, write h_f=b_f-n·A. Under the star map its actual pole is

    q_f=(n+h_f c)/(b_f+h_f c·A).

The support denominator is positive at the actual-centred body. For a polar edge f--g, clearing positive support denominators and det M gives the sign polynomial

    (n_f+h_f c)^T adj(M)
      [(b_f+h_f c·A)(n_g+h_g c)
       -(b_g+h_g c·A)(n_f+h_f c)].

Generic nonroot polar constraints therefore retain their cofactor coupling. The fixed-footpoint convex reduction is not promoted to global convexity.

For proper110, an exact formulation must additionally exclude strict saddles and physical weak packets. On each true edge use its two primal and two polar primitives. A strict saddle has all four negative; a physical weak packet has all four nonpositive and at least one zero. A harmless zero with a positive escape is not a weak equilibrium.

The resulting proper E17 candidate system lies in an explicit bounded geometry/common-metric envelope with thirteen independent continuous variables: five cuts, three centring parameters, and five scale-normalized metric variables. The actual system retains the strict open-cube incidence conditions and positive metric conditions. Its compact envelope may contain merged-incidence boundary points, which are not E17 witnesses.

## 9. Degree-seven two-cap consequence

Let an actual10/17/9 body have a specified degree-seven vertex A and fix its seven actual apex planes. There are exactly two nonapical maximal facets. Choose one as the base and apply section3.

The normalized body is a fixed bounded seven-gonal pyramid cut by ONE further plane

    a·(Y-A)≤1.

All other vertices are simple, since the degree excess 2E-3V=4 is entirely consumed by deg(A)-3=4. Hence the cut cannot pass through an old virtual base vertex in a true E17 member.

Let B0,...,B6 be the fixed base polygon. The cut removes a nonempty proper consecutive block I of its vertices. For that labelled block its complete parameter domain is the open polyhedron

    a·(B_i-A)>1  for i in I,
    a·(B_i-A)<1  for i not in I.

If |I|=m, the new cap has m+2 vertices and the remaining base has9-m vertices. There are m new spoke intersections and two new base-edge intersections, so the actual counts are10/17/9. Applying unique actual star centring gives the corresponding complete three-parameter fixed-pole realization class.

For m=1 this is the usual three independent corner fractions in (0,1)^3. For the larger caps it is a cut-plane coefficient domain, not an invented three-independent-fraction cube. Choosing either nonapical facet as base gives overlapping normalizations, not different physical bodies.

This reduction covers a body with an unbounded released virtual pyramid because the normalizing denominator is proved positive on the actual body. It is a geometric theorem for the coordinator’s degree-seven problem, not an all-metric nonroot-U theorem there. No uniform boundary compactness for an arbitrary seven-pole input is inferred from the special retained-tetrahedron estimates proved above for the literal hexagon.

## 10. Computational status and continuation

The whole-fibre atlas and all bounds in this handoff have analytic proofs above. No new full-U1 or110 census is asserted.

A separate attempted two-depth interval/Bernstein and matrix-stencil calculation is not promoted here: its final complete verified row packet and source-only replay receipt are not delivered in this handoff. It remains an ephemeral candidate, not a new all-SPD exclusion. In particular, no finite unsuccessful metric search is being converted into a theorem.

The substantive remaining U1 problem is now precise: solve the actual-centroid equations over the full independent five-cut atlas, with true nonroot escape conditions, including possible rank-two physical-metric limits. For S1/U1 or110 the metric can instead be restricted to the explicit nonsingular compact envelope above. Virtual-horizon sectors are internal parts of this geometry, not missing unbounded completions. The parent’s lower trapped-set mechanism remains a real obstacle; root eligibility and global radius dominance alone do not remove it.

## 11. Exact rational input checker and model generator

The following complete standard-library source generates the actual-centroid polynomial system and the cleared primal/polar arrow tensors for any rational point of the source five-cube. It checks the rational identities used in the global bounds, the complete true source hull, and the actual projective volume/centroid identity. It does not claim to decide the resulting U1 or110 feasibility problem.

Commands, using CPython3.13.5 with assertions enabled:

    python -B -S hex6_global_atlas.py 1/2 1/2 1/2 1/2 1/2
    python -B -S hex6_global_atlas.py 99/100 99/100 99/100 99/100 99/100

The output model specifies the exact algebraic centred member by its unique positive-domain root; a rational locator is never silently declared to have centroid0. The program prints source and output hashes. No cold-execution receipt or precomputed hash is claimed for this newly assembled checker.

```python
#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import combinations
from math import gcd, lcm
from pathlib import Path
import hashlib
import json
import sys

sys.set_int_max_str_digits(0)
PARENT = 'minimum-0203'
PARENT_SHA = 'afe1de89443d478069ffce2a0c36375fc3fb7e039137eb7ba4299106211dca19'
P = tuple(tuple(F(v,100000) for v in row) for row in (
    (60401,-32565),(80000,-20000),(0,60000),
    (-80000,80000),(-483861,-325040),(-447814,-355009)))
A = (F(0),F(0),F(1))
Q = tuple(p+(F(1),) for p in P)
BASE = (F(2615613,500000),F(816129,250000),F(-3))
FAC = ((0,4,6,5),(0,5,7,1),(0,1,2),(0,2,8),(0,8,9,3),
       (0,3,4),(4,3,9,2,1,7,6),(5,6,7),(9,8,2))
TETS = ((4,3,9),(4,9,2),(4,2,1),(4,1,7),(4,7,6),(5,6,7),(9,8,2))
EDGES = tuple(sorted({tuple(sorted((f[k],f[(k+1)%len(f)])))
                     for f in FAC for k in range(len(f))}))

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(a,t): return tuple(t*x for x in a)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def tr(a): return tuple(zip(*a))
def mv(a,b): return tuple(dot(row,b) for row in a)
def mm(a,b): return tuple(tuple(dot(row,col) for col in tr(b)) for row in a)
def det(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
           -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
           +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))
def inv(a):
    n=len(a)
    w=[[F(v) for v in row]+[F(i==j) for j in range(n)]
       for i,row in enumerate(a)]
    for k in range(n):
        j=next(i for i in range(k,n) if w[i][k])
        w[k],w[j]=w[j],w[k]
        p=w[k][k]
        w[k]=[v/p for v in w[k]]
        for i in range(n):
            if i!=k:
                p=w[i][k]
                w[i]=[x-p*y for x,y in zip(w[i],w[k])]
    ans=tuple(tuple(row[n:]) for row in w)
    assert mm(a,ans)==tuple(tuple(F(i==j) for j in range(n)) for i in range(n))
    return ans

B=tuple(mv(inv((Q[i],Q[(i+1)%6],BASE)),(F(1),)*3) for i in range(6))
I0=inv(tr((sub(A,B[0]),sub(B[5],B[0]),sub(B[1],B[0]))))
I3=inv(tr((sub(B[2],B[3]),sub(A,B[3]),sub(B[4],B[3]))))

def check_constants():
    for i in range(6):
        e=sub(P[(i+1)%6],P[i])
        for j in range(6):
            if j not in (i,(i+1)%6):
                v=sub(P[j],P[i])
                assert e[0]*v[1]-e[1]*v[0]>0
    s=(F(-1743742,1000000),F(-1088172,1000000))
    t=F(1715957,4344505)
    m1=F(5,4)*(s[0]-P[4][0]*t)
    m2=1-t-m1
    assert min(t,m1,m2)>0
    assert add(add(scale(P[1],m1),scale(P[2],m2)),scale(P[4],t))==s
    a,b=BASE[:2]
    R,S,T=F(29969),F(36047),F(26217547189,100000)
    K1=a+b+F(9,5)
    K2=a+4*b+F(36,5)
    D=3*T-a*R-b*S
    h=1/(T+F(108141,5))
    U=(sub(B[1],A),sub(B[2],A),sub(B[4],A))
    assert U[0]==scale((F(1),F(1),F(-3,5)),4/K1)
    assert U[1]==scale((F(1),F(4),F(-12,5)),4/K2)
    assert U[2]==scale((R,S,T),-4/D)
    lam=(F(1,4),27943*K1*h/4,2026*K2*h/4,D*h/4)
    assert sum(lam)==1 and min(lam[1:])>F(1,100)
    V=(A,B[1],B[2],B[4])
    assert tuple(sum(lam[i]*V[i][j] for i in range(4)) for j in range(3))==(0,0,0)
    assert 10<K1<12 and 25<K2<30 and 262000<T<263000
    assert D>460000 and T+F(108141,5)<285000
    assert abs(det(U))==192/(K1*K2*D*h)>F(8,45)
    assert max(abs(v) for row in U for v in row)<3
    assert max(sum(abs(v) for v in row) for row in inv(U))<304
    qi=inv((Q[1],Q[2],Q[3]))
    assert qi==((F(-5,12),F(25,12),F(-5,3)),
                (F(-5,3),F(10,3),F(-5,3)),(F(1),F(-1),F(1)))
    assert 1+3*23000*14==966001<1000000
    volume_lower=F(4,135*75**3)
    assert volume_lower==F(4,56953125)
    radius=F(1,10**19)
    assert 4704*radius<F(24,56953125*10**8)
    assert F(2666,9)<18**2
    gamma=(F(18)/radius)**2
    kappa=gamma**2
    assert gamma==324*10**38 and kappa==104976*10**76
    return {'origin_barycentric':lam,'source_retained_volume':abs(det(U))/6,
            'c_bound':23000,'actual_denominator_lower':F(1,1000000),
            'actual_volume_lower':volume_lower,'inner_cube_radius':radius,
            'outer_euclidean_radius':18,'Gamma':gamma,'Kappa':kappa}

def source(cuts):
    x,y,z,u,v=cuts
    assert all(0<t<1 for t in cuts)
    Y=(A,B[1],B[2],B[4],B[5],
       add(B[0],scale(sub(A,B[0]),x)),
       add(B[0],scale(sub(B[5],B[0]),y)),
       add(B[0],scale(sub(B[1],B[0]),z)),
       add(B[3],scale(sub(A,B[3]),u)),
       add(B[3],scale(sub(B[4],B[3]),v)))
    l7=tuple(y*z*I0[0][j]+x*z*I0[1][j]+x*y*I0[2][j] for j in range(3))
    l8=tuple(u*v*I3[0][j]+v*I3[1][j]+u*I3[2][j] for j in range(3))
    planes=tuple((q,F(1)) for q in Q)+((BASE,F(1)),
             (scale(l7,-1),-x*y*z-dot(l7,B[0])),
             (scale(l8,-1),-u*v-dot(l8,B[3])))
    for f,(n,h) in zip(FAC,planes):
        for i,w in enumerate(Y):
            slack=h-dot(n,w)
            assert slack>=0 and (slack==0)==(i in f)
    found=set()
    for ids in combinations(range(9),3):
        rows=tuple(planes[i][0] for i in ids)
        if det(rows)==0:continue
        w=mv(inv(rows),tuple(planes[i][1] for i in ids))
        if all(dot(n,w)<=h for n,h in planes):found.add(w)
    assert found==set(Y) and len(found)==10 and len(EDGES)==17
    for i,j in EDGES:assert sum(i in f and j in f for f in FAC)==2
    U=tuple(sub(w,A) for w in Y)
    vols=tuple(abs(det(tuple(U[i] for i in t)))/6 for t in TETS)
    assert min(vols)>0
    return Y,U,planes,vols

ZERO=(0,0,0)
def pc(x): return {} if x==0 else {ZERO:F(x)}
def pa(p,q):
    z=dict(p)
    for e,v in q.items():
        z[e]=z.get(e,F(0))+v
        if z[e]==0:del z[e]
    return z
ndef ps(p,a): return {e:a*v for e,v in p.items() if a*v}
def pm(p,q):
    z={}
    for e,a in p.items():
        for f,b in q.items():
            k=tuple(e[i]+f[i] for i in range(3))
            z[k]=z.get(k,F(0))+a*b
    return {e:v for e,v in z.items() if v}
def pp(items):
    p=pc(1)
    for q in items:p=pm(p,q)
    return p
ndef pd(p,j):
    z={}
    for e,v in p.items():
        if e[j]:
            f=list(e);f[j]-=1;z[tuple(f)]=v*e[j]
    return z
CVAR=tuple({tuple(int(i==j) for i in range(3)):F(1)} for j in range(3))
def plin(u):
    p=pc(1)
    for j in range(3):p=pa(p,ps(CVAR[j],u[j]))
    return p
ndef pe(p,c):
    return sum((v*c[0]**e[0]*c[1]**e[1]*c[2]**e[2] for e,v in p.items()),F(0))
def pserial(p):return [[list(e),str(v)] for e,v in sorted(p.items())]
def integer_equation(p):
    assert p
    den=1
    for v in p.values():den=lcm(den,v.denominator)
    z={e:int(v*den) for e,v in p.items()}
    g=0
    for v in z.values():g=gcd(g,abs(v))
    return [[list(e),v//g] for e,v in sorted(z.items())]
def sympoly(a,b):
    return [[ps(pa(pm(a[i],b[j]),pm(a[j],b[i])),F(1,2)) for j in range(3)] for i in range(3)]
def tensor_serial(t):return [[pserial(p) for p in row] for row in t]

def model(cuts):
    Y,U,planes,vols=source(cuts)
    d=tuple(plin(w) for w in U)
    W=pp(d[1:]);Z=pc(0)
    for ids,vol in zip(TETS,vols):
        Z=pa(Z,ps(pp(d[i] for i in range(1,10) if i not in ids),vol))
    eq=[]
    for j in range(3):
        z=pa(pm(pd(Z,j),W),ps(pm(Z,pd(W,j)),-1))
        z=pa(z,ps(pm(Z,W),-4*A[j]));eq.append(z)
        assert max(map(sum,z))<=(15 if j==2 else 14)
    # Two exact checks use NEW uniform projective moments, not the image of an old centroid.
    for c in ((F(0),)*3,(F(1,10000),F(-1,20000),F(1,30000))):
        den=tuple(pe(q,c) for q in d);assert min(den)>0
        X=tuple(add(A,scale(U[i],1/den[i])) for i in range(10))
        vv=F(0);J=(F(0),)*3
        for ids,vol in zip(TETS,vols):
            w=vol
            for i in ids:w/=den[i]
            vv+=w
            ss=tuple(A[j]+sum(X[i][j] for i in ids) for j in range(3))
            J=add(J,scale(ss,w/4))
        gg=scale(J,1/vv)
        assert pe(Z,c)/pe(W,c)==vv
        for j in range(3):assert pe(eq[j],c)/(pe(Z,c)*pe(W,c))==-4*gg[j]
    zn=tuple(tuple(pa(ps(d[i],A[j]),pc(U[i][j])) for j in range(3)) for i in range(10))
    primal=[]
    for i,j in EDGES:
        for a,b in ((i,j),(j,i)):
            ee=tuple(pa(ps(d[a],U[b][k]),ps(d[b],-U[a][k])) for k in range(3))
            primal.append({'edge':[a,b],'tensor':tensor_serial(sympoly(zn[a],ee))})
    pn=[];ph=[]
    for n,h in planes:
        z=h-dot(n,A)
        pn.append(tuple(pa(pc(n[j]),ps(CVAR[j],z)) for j in range(3)))
        ph.append(pa(pc(h),ps(CVAR[2],z)))
    pairs=set()
    for i,j in EDGES:
        f=tuple(k for k,FACET in enumerate(FAC) if i in FACET and j in FACET)
        assert len(f)==2;pairs.add(tuple(sorted(f)))
    assert len(pairs)==17
    polar=[]
    for i,j in sorted(pairs):
        for a,b in ((i,j),(j,i)):
            ee=tuple(pa(pm(ph[a],pn[b][k]),ps(pm(ph[b],pn[a][k]),-1)) for k in range(3))
            polar.append({'edge':[a,b],'tensor_against_adjM':tensor_serial(sympoly(pn[a],ee))})
    return {'parent':PARENT,'parent_sha256':PARENT_SHA,
      'cuts':[str(t) for t in cuts],'apex':[str(t) for t in A],
      'source_vertices':[[str(t) for t in w] for w in Y],
      'facets':FAC,'true_edges':EDGES,'actual_apex_fan':TETS,
      'centering_equations':list(map(integer_equation,eq)),
      'actual_denominators':[pserial(p) for p in d],
      'virtual_denominators_NOT_required_positive':{
          'B0':pserial(plin(sub(B[0],A))), 'B3':pserial(plin(sub(B[3],A)))},
      'polar_numerators':[[pserial(p) for p in row] for row in pn],
      'polar_support_denominators':[pserial(p) for p in ph],
      'cleared_primal_tensors':primal,'cleared_polar_tensors':polar,
      'tensor_convention':'Full symmetric matrices; Frobenius contraction counts both off-diagonal entries.',
      'actual_selector':'Unique root with all actual d_i>1/1000000, 0<c_z<3/4 and |c_j|<23000.',
      'metric':'ONE M SPD, N=M^-1. Polar tensors contract with adj(M), not an independent matrix.',
      'equilibrium_status':'No U1 or110 feasibility conclusion is computed by this generator.'}

def main():
    cuts=tuple(F(t) for t in sys.argv[1:]) if len(sys.argv)>1 else (F(1,2),)*5
    assert len(cuts)==5
    constants=check_constants();out=model(cuts)
    out['exact_constants']={k:([str(v) for v in z] if isinstance(z,tuple) else str(z))
                            for k,z in constants.items()}
    blob=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode()
    path=Path('hex6_global_atlas_model.json');path.write_bytes(blob)
    print('CUTS',','.join(map(str,cuts)))
    print('TRUE_COUNTS',10,17,9)
    print('MODEL_BYTES',len(blob),'SHA256',hashlib.sha256(blob).hexdigest())
    print('SOURCE_SHA256',hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    print('HEX6_GLOBAL_ATLAS_MODEL_PASS')
if __name__=='__main__':main()
```

The final unresolved distinction is therefore not bounded versus unbounded actual completion. The actual fixed-pole geometry has an explicit compactification. What remains is the common-metric nonroot escape problem inside it: a possible rank-two boundary for U1 alone, and a bounded nonsingular interior problem for simultaneous S1/U1 and proper110.
