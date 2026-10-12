# minimum-0146

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# PARALLEL_ROOT_MINKOWSKI_SECTION_DOMINANCE_201_V1

## 1. Determination

A complete free-shape, nonaxial mixed-canonical sector is now excluded below the target. Let

    A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
    T0=conv(A,B,C,D), H>1,
    F subset {x+y+z=H, x,y,z>=0}

be any compact convex positive-area root, and put P=conv(T0,F). With the ORIGINAL endpoint data and integrals

    q=1-1/H,
    ell=1-(x+y+z)/H,       endpoints (1,q,q,q),
    n=(1+2q)(x+y),
    V=integral_P 1, Bell=integral_P ell, N=integral_P n,
    T=N/(6 V Bell),

the whole class satisfies

    T < 201/100 < 51/25.

There is no restriction on the root's number of vertices, edge directions or coordinate complexity. Compact nonpolygonal roots are included. H is unrestricted, so this is not a bounded-height collar. Root projections may extend beyond x+y=1, and the class includes genuine four-canonical nonaxial bodies with nine maximal facets, directly inside the remaining terminal geometry.

The main mechanism is stronger than a scalar estimate. Every body in this class has an explicitly reconstructed root-band successor that preserves its **entire volume distribution under x+y+z**, its positive root area, its original V and Bell, and has no smaller original N. For a proper input, the successor is also a proper triangular-pair body, with at most eight true vertices and seven maximal facets. It need not preserve the full first moment or the actual centroid. This is a global replacement of one real root by another, not an assertion that the parent's single-chord motion preserves denominator moments.

The endpoint restriction is important: ell(B)=ell(C)=ell(D)=q, while ell(A)=1 differs. Thus this is a genuinely tilted common-edge problem, but not the full unequal-endpoint problem. It does not contain the parent extremal sequences with b near 0.236 and c,d tending to zero. Unequal b,c,d and roots extending outside the positive simplicial cone remain open.

A second analytic result gives an exact weighted parallel-root normal form for the entire positive-octant, unequal-endpoint root-only class. It identifies precisely why the new section replacement does not yet settle that larger class: the transformed original density varies horizontally. No uniformly refilled image inequality is applied to those weights.

An exact proper 8/13/7 control below has T=2031/1015>2. Therefore the new whole-class ceiling cannot simply be strengthened to T<=2. A separate homothetic-triangular-root subfamily does satisfy T<2. None of these controls is a threshold counterexample or a claimed 110 construction. No global complexity bound or incidence-registry count changes.

## 2. Authority, reading and verification status

The complete current journal and literal parent were read through EOF in the resumed work. The journal research-journal(20260920-204552).md has 343345 bytes and SHA-256 a8746c299b2d776ec83789a67137ea6d35ea5fe2b6203da488d32882f5621ff8. The required parent is minimum-0138, immutable SHA-256 d3a03675e4faafe1c0e0d0444bc49583eb3905305917c6b62d637247253fc8fb, literal title COORDINATE_SATURATED_ROOT_SHARP_TRACE_V1.

Its complete axial theorem is a working premise, not a new result here. Its proper contraction and mixed-canonical chord counterexamples remain valid; neither false monotonicity nor false moment invariance is used below.  The new numerical ceiling has its own short sum-of-squares proof and does not depend on replaying an older Bernstein certificate.

The new theorem and the three literal controls are supported by the explicit section formulas, polynomial identities and facet descriptions below. A complete independent exact audit was written and build/verify commands were submitted, but their terminal output was not retained in readable form in this resumed execution. Accordingly, **no observed new computer-pass receipt, report digest or cold replay is claimed**. The final section contains the entire runnable audit, exact inputs, expected terminal markers and commands. The distinction is between the analytic proof presented here and the unobserved execution status of that additional audit.

## 3. Actual geometric domain and proper-versus-patch status

Write t=x+y+z and let R be the xy projection of F. The cone assumption is exactly

    R subset H Delta,
    Delta=conv((0,0),(1,0),(0,1)).

The lift of a point (x,y) in R is (x,y,H-x-y). Since all four canonical points have t<=1<H, the actual maximal zero-root face of P is exactly F. No auxiliary support or zero-area set is substituted for it.

The theorem is valid for the marked functional on all these bodies, including coordinate patches. When min_F x>0 and min_F y>0, the entire maximal coordinate facets are exactly ABC and ABD. Every canonical point is then a true vertex, and the theorem is a bound for the requested genuine triangular pair. If the root meets a coordinate plane, that support can be a larger patch and must be labelled accordingly.

The volume coordinate change (x,y,z) to (x,y,t) has determinant one. Equivalently, a section in t=constant has physical area sqrt(3) times its xy area, while the coarea factor is 1/sqrt(3). Thus all the integrals below are the original uniform volume integrals, with no omitted geometric factor.

## 4. Exact section identity, including every root-controller change

Put k=H-1 and tau=(t-1)/k. The actual sections of P are

    P intersect {t=s}, projected to xy:
      s Delta,                              0<=s<=1,
      (1-tau) Delta + tau R,                 1<=s<=H.
                                                        (1)

Here the plus sign is the Minkowski sum of the two actual filled planar sets.

To prove the second identity without assuming a prismatoid formula, take an arbitrary convex representation using A, a base point u in Delta at height one, and a root point v in R at height H. If the root coefficient is tau+epsilon, its base coefficient is 1-tau-H epsilon. Since v/H belongs to Delta, the extra term epsilon v can be absorbed as H epsilon times v/H into the base coefficient. This gives a point of (1-tau)Delta+tau R. The reverse inclusion is directly contained in conv(BCD,F). For heights below one, the same cone containment gives s Delta exactly.

Identity (1) is global. It survives changes of the root's normal fan, coplanar mergers and canonical status changes. It is not a formula continued past a single local triangulation chamber.

### Intrinsic data of the root

Let

    xi=min_R x, eta=min_R y, sigma=xi+eta,
    K=R-(xi,eta),
    a=max_K(x+y), A_r=Area(K),
    J_r=integral_K(x+y).

Then

    K subset a Delta,
    min_K x=min_K y=0,
    0<2 A_r<=a^2,
    a+sigma<=H.                               (2)

The parameter a here is the size of the root's minimal translated coordinate triangle; it is not a density endpoint.

There is one more genuine mixed first moment, denoted B_r. For a counterclockwise polygon K it is

    B_r = sum_edges [max(0,dy,-dx) * (s_left+s_right)/2],
    s_left=x_left+y_left, s_right=x_right+y_right.        (3)

The root data satisfy the exact Minkowski formulas

    Area(u Delta+v K)=u^2/2+a*u*v+A_r*v^2,

    integral_(u Delta+v K)(x+y)
      =u^3/3+a*u^2*v+B_r*u*v^2+J_r*v^3.        (4)

One direct proof is to use the common refinement of the two polygonal normal fans. Every vertex is affine in u,v, so area and first moment are homogeneous polynomials of degrees two and three. At Delta, the support values of K on the two negative coordinate normals are zero, and on the diagonal normal the value is a. Boundary differentiation gives the displayed mixed coefficients a. Differentiation at K in the Delta direction gives (3).

Approximation by inscribed polygons retaining the three support values extends (3)–(4), and the inequalities that follow, to arbitrary compact convex K. No polyhedral-attainment premise is needed.

## 5. A simultaneous, real-root maximizer for the mixed data

Two coupled planar inequalities are decisive:

    B_r<=a^2,
    J_r<=a^3*(1-r^3)/3,
    r=sqrt(1-2 A_r/a^2),  0<=r<1.              (5)

Both bounds are attained by the SAME real convex set

    K_star={x,y>=0, a*r<=x+y<=a}.               (6)

They are not independently optimized scalar moments.

For the first inequality, split the boundary of K by the three normal cones of Delta. The cone selecting the origin contributes zero. On the cone selecting (1,0), the contribution is integral (x+y)dy, with dy>=0, from a point with y=0 to a diagonal support point p. The cone selecting (0,1) contributes -integral (x+y)dx, with -dx>=0, from p to x=0. Since x+y<=a, the sum is at most a(p_y+p_x)=a^2. A diagonal support edge can be split at any point p; the two formulas agree there.

For the second inequality, K and the band (6) have the same area A_r. Subtract a*r from the integrand. The portion of K outside the band has nonpositive integrand, while the portion of the band outside K has nonnegative integrand. Consequently the band has at least as large an integral of x+y. Direct integration gives its value in (5). This also proves the equality statement without choosing an artificial density.

### The actual successor

Set delta=H-a>=sigma and define

    R_star=(delta/2,delta/2)+K_star,
    F_star={(x,y,H-x-y):(x,y) in R_star},
    P_star=conv(T0,F_star).                    (7)

The two roots have identical xy area A_r and identical mixed-area parameter a. Their section areas in (1) therefore agree at EVERY height. Moreover, their section first moments in x+y differ by

    (a^2-B_r)*tau^2*(1-tau)
      +[a^3*(1-r^3)/3-J_r]*tau^3
      +(delta-sigma)*tau*Area((1-tau)Delta+tau K),        (8)

which is nonnegative on the entire interval 0<=tau<=1.

Consequently, for every integrable height function psi,

    integral_P psi(t)=integral_Pstar psi(t),

and for every nonnegative height function psi,

    integral_P psi(t)*(x+y)
      <= integral_Pstar psi(t)*(x+y).           (9)

In particular, V, Bell, all height moments and the positive physical root area sqrt(3)A_r are preserved exactly, while N and T do not decrease. The full vector first moment generally changes.

For a proper input, xi,eta>0, so delta>=sigma>0. All vertices of F_star then have positive x,y. Thus P_star has genuine full ABC and ABD, not merely a proper approximation of a patch. If 0<r<1 it has exactly eight vertices and seven facets; if r=0 its root is triangular and it has seven vertices and six facets. Patch inputs can lead to delta=0, in which case the root-band successor is correctly treated as a coordinate patch.

This controls arbitrary root-coordinate complexity by one actual body replacement. It does not claim a fixed-face-lattice monotone homotopy from K to K_star, and does not rely on the false single-chord denominator invariant.

## 6. Complete analytic bound on the successor

The root-band successor has the four projected generators

    (delta/2+a*r,delta/2), (delta/2+a,delta/2),
    (delta/2,delta/2+a), (delta/2,delta/2+a*r).

For r=0 the repeated near generator is removed. Set

    w=1-r^2, f=(1-r)^2*(1+2r),
    S=1+a+a^2*w,
    A0=3+2a+a^2*w,
    C0=1+2a+3a^2*w,
    U=1+k*S,
    E=1+4k+k^2*A0,
    M=2+k*(3S-a^3*f)+k^2*C0.

Direct integration of (1) and (4) gives the ORIGINAL data

    V=U/6,
    Bell=E/(24H),
    integral_Pstar(x+y)=M/24,
    N_star=(1+3k)*M/(24H),
    T_star=(1+3k)*M/(U*E).                     (10)

Here k>0, 0<a<=H=1+k, and 0<=r<1. There is no bounded-height or bounded-root-size assumption.

### A short sum-of-squares certificate

The exact difference at threshold two is

    2UE-(1+3k)M=k F1+k^2 F2+k^3 F3,

    F1=1-a-a^2*w+a^3*f,
    F2=4+a-2a^2*w+3a^3*f,
    F3=3+4a+4a^2+a^2*w*(6a-1)+2a^4*w^2.

Put

    D=f-(3/4)w^2=(1-r)^3*(1+3r)/4>=0.

The following are exact identities:

    F1=1-4a/3 + (a/12)(3aw-2)^2 + a^3 D,
    F2=4+5a/9 + (a/36)(9aw-4)^2 + 3a^3 D,
    F3=3+4a+3a^2+a^2(1-w)+6a^3w+2a^4w^2.

Therefore

    F1>=-1/3-4k/3, F2>=4, F3>=3,
    UE>=1+5k,

where the first bound uses a<=1+k. Taking tau=201/100 yields

    tau UE-(1+3k)M
      >=1/100-(17/60)k+(8/3)k^2+3k^3
       =(8/3)(k-17/320)^2+19/7680+3k^3>0.       (11)

This proves the whole-class strict bound. There is no numerical positivity sampling, unlisted parameter cell, feasibility pruning or asymptotic exception.

It also supplies an original-body quantitative margin:

    201/100-T(P)
      >=[19/7680+3(H-1)^3]/[144 H V Bell]>0.    (12)

The same original V and Bell occur in (12), because the root replacement preserves them.

### Homothetic-triangular roots

When r=0, the root itself is a translated homothetic copy of the coordinate triangle. In that entire subfamily the stronger bound T<2 follows from

    2UE-(1+3k)M
      =k(1-a)^2(1+a)
       +k^2[(a-1)^2(3a+4)+6a]
       +k^3[3+4a+3a^2+6a^3+2a^4]>0.

The general root class cannot satisfy this stronger bound, as the exact control in Section 8 shows.

## 7. An exact nonaxial terminal body and its volume-preserving successor

Use the canonical labels 0=A,1=B,2=C,3=D. The first body has H=3/2, so b=c=d=1/3, and root vertices

    4=(1/50,3/100,29/20),
    5=(31/50,3/100,17/20),
    6=(31/50,83/100,1/20),
    7=(1/50,83/100,13/20).

Every root coordinate is strictly positive. This is a genuine proper four-canonical body, with true V/E/F=8/15/9. Its complete maximal facet vertex sets are

    012, 013, 023, 1247, 1345, 356, 267, 236, 4567.

The nine supporting planes can be written as

    x,y,z>=0, x+y+z<=3/2,
    24x-y-z+1>=0, -3x+47y-3z+3>=0,
    44x+19y+19z<=44,
    17x+67y+17z<=67,
    x+y-9z<=1.

Thus the two coordinate facets used by the trace are actual triangles. Its root projection has max(x+y)=29/20>1, so it is not in the already closed prism domain. It also has b=c=d=1/3, outside the old small-endpoint chamber.

Its intrinsic root data are

    xi=1/50, eta=3/100, a=7/5, A_r=12/25,
    B_r=73/50, J_r=42/125, r=5/7.

The root-band successor (7) has root vertices

    4=(21/20,1/20,2/5),
    5=(29/20,1/20,0),
    6=(1/20,29/20,0),
    7=(1/20,21/20,2/5).

It is also proper, with true 8/13/7 and maximal facet sets

    012, 013, 02356, 1267, 1345, 147, 4567.

The pentagon 02356 is one genuine maximal facet, not a triangulated collection of faces. Its noncoordinate supporting planes are

    x+y+z<=3/2,
    9x-y-z+1>=0, -x+9y-z+1>=0,
    6(x+y)+11z<=11.

The exact ORIGINAL data are:

|Quantity|Initial nonaxial rectangle root|Dominating nonaxial band root|
|---|---|---|
|V|67/150|67/150|
|Bell|469/3600|469/3600|
|Jx|2799/20000|4219/24000|
|Jy|6127/40000|4219/24000|
|Jz|871/4800|123/1000|
|N|469/960|4219/7200|
|T|375/268|105475/62846|
|Physical root area|12 sqrt(3)/25|12 sqrt(3)/25|

The numerator gain is exactly 1403/14400. The sum Jx+Jy+Jz remains 1139/2400, but the full first moment and own centroid change. This is a substantial actual root replacement, not a small collar or a fixed-center computation.

No mechanical census or 110 status is asserted from these trace data. The standalone audit computes all own-centroid edge primitives for continuation, separately from the analytic trace proof.

## 8. A genuine control with T>2, and the refill warning in the new chart

Take H=21/20, so b=c=d=1/21, and the root generators

    4=(83/120,1/40,1/3),
    5=(41/40,1/40,0),
    6=(1/40,41/40,0),
    7=(1/40,83/120,1/3).

The body is genuine proper 8/13/7, with the same seven maximal facet sets as the preceding band body. Its noncoordinate support inequalities are

    x+y+z<=21/20,
    x-y-z+1>=0, -x+y-z+1>=0,
    40(x+y)+43z<=43.

The root area is 5 sqrt(3)/18. Original uniform integration gives

    V=203/1080,
    J=(12863/259200,12863/259200,77/1620),
    Bell=437/9072,
    N=295849/2721600,
    T=2031/1015=2+1/1015.

This proves that T<=2 is false in the new free-root class, even for a proper nonaxial four-canonical body. It does not challenge 201/100 or 51/25 and is not presented as a record.

For the exact parallelizing projectivity in the next section, this body's image has root height two and the same actual 8/13/7 lattice. The image filled UNIFORMLY is a different density problem. At its own uniform moments, with normalized endpoints (1,1/2,1/2,1/2), it has

    V_image=11749/11907,
    Bell_image=6859/23814,
    N_image=3228841/1500282,
    T_uniform_image=1627335864/1289382256<2.

The correctly weighted image integrals recover the original value 2031/1015>2. The source evaluates both using actual tetrahedra. This is a new-chart instance of the same density distinction that remains mandatory throughout the branch.

## 9. Exact weighted parallelization for unequal endpoints

There is a useful extension of the formulation, but not yet of the numerical bound. Let P=conv(T0,F) lie in x,y,z>=0, with genuine positive-area root

    ell=1+(d-1)x+(c-1)y+(b-1)z,
    0<b<1, c,d>0.

No equality among b,c,d is assumed. Define

    f=(1-x-y-z)/2+d*x+c*y+b*z,
    Phi(x,y,z)=(d*x,c*y,b*z)/f.

This is a positive projectivity on the ENTIRE actual body. At the four canonical vertices f equals 1/2,b,c,d. At a root point,

    f=(x+y+z-1)/2=(d*x+c*y+b*z)/2>0.

Thus no projective horizon is crossed. The map fixes A,B,C,D, preserves the actual face lattice and proper coordinate triangles, and sends the root to

    x'+y'+z'=2, x',y',z'>=0.

Every positive-octant unequal-endpoint root-only body therefore has an actual root-parallel representative of the same geometry type.

The ORIGINAL density and ratio become

    L=2*(1-x'-y'-z')+x'/d+y'/c+z'/b>0,
    Jp=b*c*d/2,
    ell'=2-x'-y'-z',
    m'=(1+b+c)*x'/d+(1+b+d)*y'/c,

    I4=integral_(P') L^-4,
    Iell=integral_(P') ell'*L^-5,
    In=integral_(P') m'*L^-5,

    V=I4/Jp, Bell=Iell/Jp, N=In/Jp,
    T=Jp*In/(6*I4*Iell).                       (13)

The inverse is x=x'/(dL), y=y'/(cL), z=z'/(bL). These identities derive directly from the diagonal barycentric weights (1/2,b,c,d).

When b=c=d, L depends only on total height. The section-law preservation (9) is compatible with these original weights. When the endpoint values differ, L generally varies horizontally and m' is anisotropic. Equal section AREA and an increased unweighted x'+y' first moment then do not preserve I4 or Iell and do not order In. The uniform-image theorem is therefore not applied to (13).

This locates the missing unequal-endpoint connection in a concrete bounded geometric chart: control the horizontally weighted Minkowski sections of one root and one canonical base. A uniform refill, independent selection of the three integrals, or transport of the old centroid would lose the original problem.

## 10. Boundaries, uncovered complement and continuation

The main numerical theorem includes every root-combinatorial boundary through global section formulas. Triangular roots, root-axis contacts and maximal-facet mergers are evaluated as their actual hulls. For proper inputs the successor remains proper, so no strict-violation approximation is needed to use the new bound. Patch inputs are bounded as marked patches, not relabelled as triangles.

The cases r=0 and delta=0 are covered explicitly. Root-area-zero limits have a well-defined limiting functional but are not called root facets. At H down to one the body limit is T0 and the limiting functional is two. The inequality is uniform for arbitrarily large H; no singular-coordinate evaluation at q=1 is asserted. The strict positive remainder in (11), rather than a limit of strict signs, gives the gap for every actual finite-H body.

The principal remaining cases are root planes not parallel to BCD, equivalently unequal ell(B),ell(C),ell(D), and roots outside the positive simplicial cone, notably negative-z root points. For the latter, the lower sections are no longer s Delta: the convex hull of Delta with the radial root projection enters the base. The fixed-base mixed-area argument cannot be used unchanged.

The result therefore does not prove the unrestricted root-only threshold, a universal root-to-axis reduction, polyhedral attainment in the all-auxiliary class, or the removal of positive-ell auxiliaries. The parent's general f<=9, root-count<=8 and proper<=12 reductions remain separate.

The most useful continuation is the weighted section problem (13). The present replacement preserves all height-dependent masses exactly, and the failure point is specifically horizontal density variation. A successful anisotropic replacement would need to control the SAME weighted volume, weighted ell-integral and weighted numerator, not merely the unweighted root area and first moments.

## 11. Complete standalone recovery

The literal coordinate sets, maximal facet sets and exact original moments are given above. The following complete source supplies an independent audit by actual supporting-plane reconstruction, two positive volume fans, planar Minkowski identities, exact symbolic verification of the sum-of-squares certificate, original own-centroid primitive packets, and two correctly weighted image fans.

Save it as parallel_root_201_v1.py. Dependencies are CPython3.13.5 and SymPy1.14.0, assertions enabled; there are no random seeds, tolerances, external inputs or parent-code imports. Run

    python parallel_root_201_v1.py build parallel_root_201_v1.json
    python parallel_root_201_v1.py verify parallel_root_201_v1.json

Expected terminal markers are PARALLEL_ROOT_201_SOURCE and PARALLEL_ROOT_201_EXACT_PASS. Both commands print the exact source/report byte counts and SHA-256 values. No unseen output digest or observed pass is asserted here. A convenience source copy was written at parallel_root_201_v1.py; the entire recovery is inline and does not require that file.

```python
# PARALLEL_ROOT_MINKOWSKI_SECTION_DOMINANCE_201_V1
# Parent minimum-0138
# d3a03675e4faafe1c0e0d0444bc49583eb3905305917c6b62d637247253fc8fb
# CPython 3.13.5; SymPy 1.14.0; assertions enabled; no external inputs.
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib, json, sys
assert __debug__

def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(c,a): return tuple(c*x for x in a)
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def average(P,weights=None):
    weights=[F(1)]*len(P) if weights is None else weights
    return tuple(sum(w*p[j] for w,p in zip(weights,P))/sum(weights) for j in range(len(P[0])))
def solve3(rows,rhs):
    cols=list(zip(*rows)); d=det(*cols); assert d
    return (det(rhs,cols[1],cols[2])/d,det(cols[0],rhs,cols[2])/d,det(cols[0],cols[1],rhs)/d)

def hull2(ids,P):
    order=sorted(set(ids),key=lambda i:(P[i][0],P[i][1],i))
    def turn(i,j,k):
        a,b,c=(P[z] for z in (i,j,k))
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    def half(seq):
        out=[]
        for i in seq:
            while len(out)>1 and turn(out[-2],out[-1],i)<=0: out.pop()
            out.append(i)
        return out
    return half(order)[:-1]+half(order[::-1])[:-1]

def hull3(P):
    assert len(set(P))==len(P)
    faces={}
    for i,j,k in combinations(range(len(P)),3):
        n=cross(sub(P[j],P[i]),sub(P[k],P[i]))
        if not any(n): continue
        d=dot(n,P[i]); sl=[dot(n,p)-d for p in P]
        if min(sl)<0<max(sl): continue
        if max(sl)>0: n=scale(-1,n); d=-d; sl=[-v for v in sl]
        on=[v for v,x in enumerate(sl) if x==0]
        drop=max(range(3),key=lambda v:abs(n[v])); axes=[v for v in range(3) if v!=drop]
        pp=[tuple(p[v] for v in axes) for p in P]
        cy=hull2(on,pp)
        if dot(cross(sub(P[cy[1]],P[cy[0]]),sub(P[cy[2]],P[cy[0]])),n)<0: cy.reverse()
        start=cy.index(min(cy)); cy=tuple(cy[start:]+cy[:start])
        faces.setdefault(tuple(sorted(cy)),(cy,n,d))
    faces=[faces[k] for k in sorted(faces)]; edges={}
    assert {i for cy,n,d in faces for i in cy}==set(range(len(P)))
    for fi,(cy,n,d) in enumerate(faces):
        assert all(dot(n,p)<=d for p in P)
        assert {i for i,p in enumerate(P) if dot(n,p)==d}==set(cy)
        for i,j in zip(cy,cy[1:]+cy[:1]): edges.setdefault(tuple(sorted((i,j))),[]).append(fi)
    assert all(len(fs)==2 for fs in edges.values())
    assert len(P)-len(edges)+len(faces)==2
    recovered=set()
    for ids in combinations(range(len(faces)),3):
        rows=[faces[i][1] for i in ids]
        if det(*rows)==0: continue
        v=solve3(rows,[faces[i][2] for i in ids])
        if all(dot(n,v)<=d for cy,n,d in faces): recovered.add(v)
    assert recovered==set(P)
    fans=[]; moments=[]
    for ref in (average(P),average(P,[F(i+1) for i in range(len(P))])):
        assert all(dot(n,ref)<d for cy,n,d in faces)
        V=F(0); J=[F(0)]*3; cells=[]
        for cy,n,d in faces:
            for j in range(1,len(cy)-1):
                ids=(cy[0],cy[j],cy[j+1]); a,b,c=[P[i] for i in ids]
                vol=det(sub(a,ref),sub(b,ref),sub(c,ref))/6; assert vol>0
                V+=vol
                for k in range(3): J[k]+=vol*(ref[k]+a[k]+b[k]+c[k])/4
                cells.append((ids,vol))
        moments.append((V,tuple(J))); fans.append((ref,cells))
    assert moments[0]==moments[1]
    V,J=moments[0]
    return dict(points=P,faces=faces,edges=sorted(edges),edge_faces=[edges[e] for e in sorted(edges)],
                f_vector=(len(P),len(edges),len(faces)),V=V,J=J,g=tuple(x/V for x in J),fans=fans)

def planar(P):
    cy=hull2(range(len(P)),P); Q=[P[i] for i in cy]
    A=F(0); J=[F(0),F(0)]
    for p,q in zip(Q,Q[1:]+Q[:1]):
        z=p[0]*q[1]-p[1]*q[0]; A+=z/2
        for j in range(2): J[j]+=z*(p[j]+q[j])/6
    assert A>0
    return A,tuple(J),Q

def root_data(R):
    xi=min(p[0] for p in R); eta=min(p[1] for p in R)
    K=[(p[0]-xi,p[1]-eta) for p in R]
    A,J,K=planar(K); a=max(sum(p) for p in K)
    mixed=[F(0),F(0)]
    for p,q in zip(K,K[1:]+K[:1]):
        dx,dy=q[0]-p[0],q[1]-p[1]; support=max(F(0),dy,-dx)
        for j in range(2): mixed[j]+=support*(p[j]+q[j])/2
    assert 0<2*A<=a*a and sum(mixed)<=a*a
    return dict(xi=xi,eta=eta,K=K,a=a,A=A,J=J,B=tuple(mixed))

def section_check(R,D):
    delta=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]; out=[]
    a,A=D['a'],D['A']; xi,eta=D['xi'],D['eta']
    for t in (F(0),F(1,3),F(2,3),F(1)):
        raw=[((1-t)*p[0]+t*q[0],(1-t)*p[1]+t*q[1]) for p in delta for q in R]
        area,mom,cy=planar(raw)
        expected=F(1,2)*(1-t)**2+a*t*(1-t)+A*t*t
        jj=tuple(F(1,6)*(1-t)**3+(a/2)*t*(1-t)**2+D['B'][j]*t*t*(1-t)
                 +D['J'][j]*t**3+t*(xi,eta)[j]*expected for j in range(2))
        assert (area,mom)==(expected,jj)
        out.append((t,area,mom,cy))
    return out

def weighted_parallel(P,b,c,d,V,Bell,N):
    h=1+b; jac=b*c*d/2
    den=[F(1,2)*(1-sum(p))+d*p[0]+c*p[1]+b*p[2] for p in P]
    assert min(den)>0
    image=[(d*p[0]/f,c*p[1]/f,b*p[2]/f) for p,f in zip(P,den)]
    H=hull3(image)
    L=lambda p:2*(1-sum(p))+p[0]/d+p[1]/c+p[2]/b
    ell=lambda p:2-sum(p)
    numer=lambda p:(h+c)*p[0]/d+(h+d)*p[1]/c
    rows=[]
    for ref,cells in H['fans']:
        row=[F(0)]*3
        for ids,vol in cells:
            tet=[ref]+[image[i] for i in ids]; ls=[L(p) for p in tet]
            assert min(ls)>0
            prod=F(1)
            for value in ls: prod*=value
            w=vol/prod; row[0]+=w
            row[1]+=w*sum(ell(p)/l for p,l in zip(tet,ls))/4
            row[2]+=w*sum(numer(p)/l for p,l in zip(tet,ls))/4
        rows.append(tuple(row))
    assert rows[0]==rows[1]==(jac*V,jac*Bell,jac*N)
    assert jac*rows[0][2]/(6*rows[0][0]*rows[0][1])==N/(6*V*Bell)
    return dict(Jp=jac,weighted=rows[0],actual_image=H)

def primitive_audit(H):
    P=H['points']; g=H['g']; v=[sub(p,g) for p in P]
    poles=[scale(1/(d-dot(n,g)),n) for cy,n,d in H['faces']]
    packets=[]
    for (i,j),(f,k) in zip(H['edges'],H['edge_faces']):
        values=(dot(v[i],sub(v[j],v[i])),dot(v[j],sub(v[i],v[j])),
                dot(poles[f],sub(poles[k],poles[f])),dot(poles[k],sub(poles[f],poles[k])))
        packets.append(((i,j),(f,k),values))
    return dict(M='identity',poles=poles,packets=packets)

BAND_FACES={(0,1,2),(0,1,3),(0,2,3,5,6),(1,2,6,7),(1,3,4,5),(1,4,7),(4,5,6,7)}
RECT_FACES={(0,1,2),(0,1,3),(0,2,3),(1,2,4,7),(1,3,4,5),(3,5,6),(2,6,7),(2,3,6),(4,5,6,7)}

def body(H,R,expected_faces,expected):
    H=F(H); R=[tuple(map(F,p)) for p in R]; assert H>1
    assert all(p[0]>0 and p[1]>0 and sum(p)<=H for p in R)
    P=[tuple(map(F,p)) for p in ((0,0,0),(0,0,1),(0,1,0),(1,0,0))]
    P += [(x,y,H-x-y) for x,y in R]
    Q=hull3(P); V,J=Q['V'],Q['J']; b=1-1/H; Bell=V-sum(J)/H; N=(1+2*b)*(J[0]+J[1]); T=N/(6*V*Bell)
    assert {tuple(sorted(cy)) for cy,n,d in Q['faces']}==expected_faces
    assert [i for i,p in enumerate(P) if p[0]==0]==[0,1,2]
    assert [i for i,p in enumerate(P) if p[1]==0]==[0,1,3]
    assert (V,J,Bell,N,T)==expected
    D=root_data(R); a,A=D['a'],D['A']; k=H-1
    I0=(1+a+2*A)/6; I1=(1+2*a+6*A)/24
    Jx=F(1,24)+k*((1+a)/24+D['B'][0]/12+D['J'][0]/4+D['xi']*I1)
    Jy=F(1,24)+k*((1+a)/24+D['B'][1]/12+D['J'][1]/4+D['eta']*I1)
    Js=F(1,8)+k*I0+k*k*I1
    assert V==F(1,6)+k*I0 and J==(Jx,Jy,Js-Jx-Jy)
    U=1+k*(1+a+2*A); E=1+4*k+k*k*(3+2*a+2*A)
    assert U==6*V and E==24*H*Bell and T<F(201,100)
    Q.update(H=H,b=b,Bell=Bell,N=N,T=T,root_xy_area=A,root_data=D,
             sections=section_check(R,D),mechanics=primitive_audit(Q),
             image=weighted_parallel(P,b,b,b,V,Bell,N))
    return Q

def certificate():
    import sympy as s
    assert s.__version__=='1.14.0'
    k,a,r=s.symbols('k a r'); rat=s.Rational; w=1-r*r; f=(1-r)**2*(1+2*r)
    D=(1-r)**3*(1+3*r)/4; assert s.expand(D-f+rat(3,4)*w*w)==0
    S=1+a+a*a*w; C=1+2*a+3*a*a*w; A=3+2*a+a*a*w
    U=1+k*S; E=1+4*k+k*k*A; M=2+k*(3*S-a**3*f)+k*k*C
    F1=1-a-a*a*w+a**3*f
    F2=4+a-2*a*a*w+3*a**3*f
    F3=3+4*a+4*a*a+a*a*w*(6*a-1)+2*a**4*w*w
    assert s.expand(2*U*E-(1+3*k)*M-k*F1-k*k*F2-k**3*F3)==0
    assert s.expand(F1-(1-rat(4,3)*a+a*(3*a*w-2)**2/12+a**3*D))==0
    assert s.expand(F2-(4+rat(5,9)*a+a*(9*a*w-4)**2/36+3*a**3*D))==0
    assert s.expand(F3-(3+4*a+3*a*a+a*a*(1-w)+6*a**3*w+2*a**4*w*w))==0
    remainder=(rat(8,3)*(k-rat(17,320))**2+rat(19,7680)+3*k**3
       +rat(1,100)*(k*(S-1)+k*k*(A+4*S)+k**3*S*A)
       +rat(4,3)*k*(1+k-a)+k*a*(3*a*w-2)**2/12+k*a**3*D
       +rat(5,9)*k*k*a+k*k*a*(9*a*w-4)**2/36+3*k*k*a**3*D
       +k**3*(4*a+3*a*a+a*a*(1-w)+6*a**3*w+2*a**4*w*w))
    G=rat(201,100)*U*E-(1+3*k)*M
    assert s.expand(G-remainder)==0
    triangular=k*(1-a)**2*(1+a)+k*k*((a-1)**2*(3*a+4)+6*a)+k**3*(3+4*a+3*a*a+6*a**3+2*a**4)
    assert s.expand((2*U*E-(1+3*k)*M).subs(r,0)-triangular)==0
    terms=[(powers,str(c)) for powers,c in s.Poly(s.expand(G),k,a,r).terms()]
    return dict(tau='201/100',positive_constant='19/7680',domain='k>0,0<a<=1+k,0<=r<1',G_terms=terms)

def clean(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {str(k):clean(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [clean(v) for v in x]
    return x

def report():
    rect=body(F(3,2),[(F(1,50),F(3,100)),(F(31,50),F(3,100)),(F(31,50),F(83,100)),(F(1,50),F(83,100))],RECT_FACES,
        (F(67,150),(F(2799,20000),F(6127,40000),F(871,4800)),F(469,3600),F(469,960),F(375,268)))
    band=body(F(3,2),[(F(21,20),F(1,20)),(F(29,20),F(1,20)),(F(1,20),F(29,20)),(F(1,20),F(21,20))],BAND_FACES,
        (F(67,150),(F(4219,24000),F(4219,24000),F(123,1000)),F(469,3600),F(4219,7200),F(105475,62846)))
    high=body(F(21,20),[(F(83,120),F(1,40)),(F(41,40),F(1,40)),(F(1,40),F(41,40)),(F(1,40),F(83,120))],BAND_FACES,
        (F(203,1080),(F(12863,259200),F(12863,259200),F(77,1620)),F(437,9072),F(295849,2721600),F(2031,1015)))
    assert rect['V']==band['V'] and rect['Bell']==band['Bell'] and rect['root_xy_area']==band['root_xy_area']
    assert band['N']-rect['N']==F(1403,14400) and band['T']>rect['T']
    assert high['T']>2 and rect['f_vector']==(8,15,9) and band['f_vector']==high['f_vector']==(8,13,7)
    I=high['image']['actual_image']; Vi,Ji=I['V'],I['J']
    Bi=Vi-sum(Ji)/2; Ni=2*(Ji[0]+Ji[1]); Ti=Ni/(6*Vi*Bi)
    assert (Vi,Bi,Ni,Ti)==(F(11749,11907),F(6859,23814),F(3228841,1500282),F(1627335864,1289382256))
    assert Ti<2<high['T']
    high['image']['uniform_refill_comparison']=dict(V=Vi,Bell=Bi,N=Ni,T=Ti)
    return dict(tag='PARALLEL_ROOT_MINKOWSKI_SECTION_DOMINANCE_201_V1',
        parent='minimum-0138',
        parent_sha256='d3a03675e4faafe1c0e0d0444bc49583eb3905305917c6b62d637247253fc8fb',
        certificate=certificate(),rectangle=rect,dominator=band,above_two=high)

if __name__=='__main__':
    assert len(sys.argv)==3 and sys.argv[1] in ('build','verify')
    raw=(json.dumps(clean(report()),sort_keys=True,separators=(',',':'))+'\n').encode()
    p=Path(sys.argv[2])
    if sys.argv[1]=='build': p.write_bytes(raw)
    else: assert p.read_bytes()==raw
    source=Path(__file__).read_bytes()
    print('PARALLEL_ROOT_201_SOURCE',len(source),hashlib.sha256(source).hexdigest())
    print('PARALLEL_ROOT_201_EXACT_PASS',len(raw),hashlib.sha256(raw).hexdigest())
```
