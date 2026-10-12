# minimum-0123

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# ROOT_ONLY_MOMENT_REDUCTION_AND_FIXED_ROOT_DELETION_OBSTRUCTION_V1

## 1. Determination

This continuation gives a **finite-vertex variational reduction for the entire root-only class**, including arbitrary nonconstant root deficits, arbitrary convex root polygons, unequal positive opposite endpoints, and arbitrary overhang. It preserves the original trace integrals of one actual body. It is not a determination of the unrestricted weighted maximum.

Write T0=conv(A,B,C,D), with A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0). A root-only body means

    P=conv(T0,F),  F=P∩{ell=0},

where F is a genuine two-dimensional root facet and ABC, ABD are the entire maximal coordinate facets. Assume normalized endpoints a=1, 0<b<1, c,d>0. The reduction produces another genuine root-only body with the same endpoint data, root plane, root area, and projected root span. The following bounds count TRUE VERTICES, not edges or an incidence-registry layer.

| Domain | Preserve original Vol, N, Bell and root area exactly | Preserve Vol, Bell and root area, and do not decrease T |
|---|---:|---:|
| Arbitrary root F; unequal c,d permitted | At most 38 vertices | At most 37 vertices |
| c=d>0; reflection symmetry not required of the successor | At most 18 vertices | At most 17 vertices |
| c=d>0; preserve x↔y reflection symmetry | At most 24 vertices | At most 22 vertices |

Here N=∫P n and Bell=∫P ell, and T=N/(6 Vol(P) Bell). Thus every value attained in the strict-endpoint root-only class is attained by a body with at most 38 vertices, or 18 when c=d. For maximization, the smaller 37 and 17 bounds suffice. These bounds are not claimed optimal. No inequality T<51/25 follows merely from these vertex counts.

The exact-moment symmetric reduction also preserves the complete original first moment and the actual volume centroid. The general two-graph reduction preserves the three integrals defining T, but does not assert preservation of the remaining transverse first moment or of mechanical equilibria.

A second result identifies a concrete obstruction to extending this reduction by simply deleting the other vertices. There is a complete rational interval of genuine 10/21/13 bodies P_delta, each with just two additional positive-density vertices, for which

    T(P_delta)>2>T(conv(T0,F_root)).

Their root facet, its area, its plane, and the coordinate triangles are unchanged by deletion. Throughout the interval, 2<T(P_delta)<2.001. These are not threshold counterexamples. They disprove even the hedged reduction

    T(P) <= max(2,T(conv(T0,F_root)))

when the original root facet is retained unchanged.

The unrestricted compact weighted maximum remains undetermined. Additional positive-density vertices, zero opposite endpoints, and the global patch/equality boundary are not eliminated by the new reduction.

## 2. Input authority and verification status

The complete supplied update and its literal parent were read through EOF in this continuation. The update research-journal(20260920-032821).md has 310150 bytes and SHA-256 1db1718d7193ede70a0d157265a3926ba6e61cac30d76b42c3f4e556db87fe21. The required immutable parent is minimum-0119, envelope 35388 bytes, SHA-256 fa7cc0adc9cb9b49505b808cd10b74f1d5e035cdd329d849dbe2b508db77dc00. Its literal result, not a class alias, is the source authority. No scientific or incidence conflict was found.

The parent’s whole constant-deficit theorem and its continuous counterexample to maximal-width filling remain unchanged. In particular, the original affine-density integration is retained; no uniformly refilled balanced image is substituted for the original body.  The new argument does not assume width-filling monotonicity, which the parent explicitly disproves. 

The finite-vertex theorem below has a direct geometric and linear-algebraic proof. The counterfamily has complete literal coordinates, a continuous supporting-plane certificate, exact integrals, and three positive integer inequality certificates below. Fresh automated build/verify calls were issued, but a readable terminal receipt was not retained in this continuation. Consequently I do not assert a new observed report checksum or an independently observed cold replay. The complete additional audit source is included at the end; it emits source/report byte counts and SHA-256 values when run. No unobserved numerical LP endpoint is promoted to a verified body.

## 3. Original affine coordinates for unequal endpoints

Put

    alpha=1-b,
    kx=1+b+c,  ky=1+b+d,
    ell=1+(d-1)x+(c-1)y-alpha*z,
    n=kx*x+ky*y.

Thus ell(A),ell(B),ell(C),ell(D)=(1,b,c,d). Use the AFFINE coordinates

    s=n,  w=ell,  t=x.

The inverse and absolute Jacobian are

    x=t,
    y=(s-kx*t)/ky,
    z=[1+(d-1)t+(c-1)(s-kx*t)/ky-w]/alpha,
    |Jac|=alpha*ky.

This is an affine coordinate change of the original uniformly filled body, not the balanced projectivity and not a new density model.

The four projected canonical points are

    A0=(0,1), B0=(0,b), C0=(ky,c), D0=(kx,d).

The genuine root projects onto a nondegenerate interval {(s,0):r<=s<=R}. Nondegeneracy follows because a two-dimensional F cannot lie in the intersection of the two independent planes ell=0 and n=constant. Set

    D=conv(A0,B0,C0,D0,(r,0),(R,0)).

Write the actual fibers as v(s,w)<=t<=u(s,w), with u concave and v convex. Introduce two convex functions

    f=s/kx-u,  g=v,
    W=u-v=s/kx-f-g.

The upper graph has the fixed zero-deficit core triangle A0 B0 D0. The lower graph has the fixed zero core A0 B0 C0. Each graph has at most four fixed off-root nodes. An optional C0 on the upper graph has f(C0)=ky/kx; an optional D0 on the lower graph has g(D0)=1. A canonical point not actually on that graph is not inserted as a fictitious graph node.

When c=d, C0=D0. Each graph then has exactly three fixed off-root nodes with graph height zero. This supplies the sharper bounds in the table.

### Positive coordinate clearance is available for each strict body

Because ell is strictly positive on ABC and ABD when 1,b,c,d>0, F cannot meet either coordinate plane. Compactness of this one root gives an epsilon>0 such that x,y>=epsilon everywhere on F. Fix such an epsilon, rather than taking it to zero. The root profiles satisfy

    g(s,0)>=epsilon,
    f(s,0)>=ky*epsilon/kx.

At r and R also impose

    f(r,0)+g(r,0)<=r/kx,
    f(R,0)+g(R,0)<=R/kx.

Both root profiles are convex. Therefore W(s,0) is concave, and these two endpoint inequalities imply W>=0 on the entire root interval. They also bound both endpoint heights above; convexity then bounds every root nodal height above. The feasible root-height set used below is therefore bounded.

## 4. A geometric moment fiber, not a free-moment relaxation

First suppose F is a polygon. Choose triangulations of the actual upper and lower graphs, using their actual root knots and their fixed canonical graph nodes. Preserve the entire zero core triangle in each mesh. The upper and lower triangulations may differ.

Vary only the root nodal heights. Impose local graph convexity across every mesh edge, one-dimensional convexity on the root boundary, the positive floors, and the two endpoint coupling inequalities above. Local graph convexity suffices globally: restriction to a line crossing the triangulation has nondecreasing slope at each crossed edge, and is therefore convex.

Every feasible pair reconstructs ONE actual body of the form conv(T0,F_new). Here is the needed converse, including the coupling that independent moment relaxations lose.

At all upper-graph nodes, 0<=u<=s/kx; at all lower-graph nodes, 0<=g<=s/kx. The root endpoint coupling gives g<=u on the entire root. At the canonical nodes the same comparison holds because the corresponding coordinate core is fixed. Since g is convex and u is affine on each upper triangle, comparison at that triangle’s nodes gives g<=u throughout it. Thus the two graphs never cross.

The fiber body {g<=t<=u} is convex and contains T0 and F_new. Conversely, every point on either graph is a convex combination of its triangle’s canonical or root nodes, and every fiber point is between such graph points. Hence the fiber body is exactly conv(T0,F_new), not a larger independently refilled set.

All its root points have x,y>=epsilon. Therefore its entire coordinate facets are exactly ABC and ABD, and their true common edge is AB. Fixing positive root area below ensures that ell=0 is still a genuine maximal facet. Auxiliary triangulation diagonals are not counted as true edges.

### The four affine moment rows

For these actual fibers,

    Vol(P)=∫D W/(alpha*ky),
    N=∫D sW/(alpha*ky),
    Bell=∫D wW/(alpha*ky),
    Area(F)=|grad ell|*∫r^R W(s,0)ds/(alpha*ky).

Each expression is affine in the root nodal heights on the fixed meshes. Upper and lower graph contributions can be integrated separately; no common mesh or independent scalar assignment is needed.

For a triangle of area A and affine nodal values H_i, the complete formulas are

    ∫H=A*sum(H_i)/3,
    ∫sH=A*[(sum s_i)(sum H_i)+sum s_i H_i]/12,
    ∫wH=A*[(sum w_i)(sum H_i)+sum w_i H_i]/12.

On the root interval, ordinary trapezoidal sums give ∫f and ∫g exactly. The physical root-area multiplier is constant, so preserving physical area is one rational affine row for rational input even when the area itself contains a square root.

Fixing Vol,N,Bell and root area defines a nonempty compact polytope of actual bodies: the original root heights are feasible. Take a vertex of this polytope. Alternatively fix Vol,Bell and root area and maximize the affine numerator N. A vertex of the maximizing face is also a vertex of the feasible polytope, and the original denominator remains exactly fixed and positive. This proves the requisite direction of trace comparison without any width monotonicity assumption.

### Deterministic rational construction

This existence argument is constructive. For rational polygonal input, all graph vertices, inequality coefficients, and moment coefficients are rational. Order canonical nodes by A,B,C,D, root nodes by increasing s, and use a fixed pulling triangulation on each polygonal graph face.

At the current feasible height vector, form the matrix of the preserved moment rows and all active inequality rows. Compute its rational reduced row-echelon form. If its rank equals the number of variables, stop. Otherwise take the null vector associated with the first free column. In the three-row version orient it so that N has nonnegative slope; in a zero-slope tie use its first nonzero component. In the four-row version N is already constant. Move by the exact largest admissible positive step, namely the minimum of slack divided by minus directional slope over the inequalities with negative slope. Boundedness ensures this minimum exists. Every previously active row remains active and at least one independent row becomes active. Thus the process terminates after at most the number of height variables in steps.

Every intermediate point is an actual coupled body with the same positive coordinate clearance and root area. A graph face may merge with another; no formula is extrapolated through a forbidden triangulation flip. Rational input produces a rational successor.

## 5. Complete vertex-count proof

### General unequal-endpoint case

Consider either graph separately. Let n be its number of root nodes and m<=4 its number of fixed off-root nodes. Let h0 be the number of off-root boundary nodes of its projected triangulation. A0 and B0 are boundary nodes, so h0>=2.

A triangulation with these nodes has

    number of triangles = n+2m-2-h0.

Exactly n-1 triangles use two consecutive root nodes and one off-root anchor: one for each root boundary edge. Call them root-fan triangles. There is at least one all-off-root triangle, namely the fixed coordinate core. Consequently the number Ccap of triangles with one root node and two off-root nodes satisfies

    Ccap <= 2m-2-h0 <= 2m-4 <= 4.

Two adjacent root-fan triangles necessarily have the same off-root anchor; their convexity inequality is the corresponding one-dimensional root slope inequality. An edge joining two all-off-root triangles has constant data. Every other variable mesh inequality is incident to a cap triangle. There are at most 3*Ccap<=12 such inequalities per graph.

At an extreme feasible height vector, let k be the number of genuine root-profile knots, counting both endpoints. The n-k active root collinearity rows are independent. One can see this directly by using the first two heights and all successive slope jumps as coordinates.

Modulo these active collinearities, active constant-floor inequalities have rank at most two per profile: the contact set of a convex function with its constant lower floor is an interval, and its two endpoints determine all remaining floor contacts. Across the two graphs, floors therefore contribute at most four to the remaining rank. Root endpoint coupling contributes at most two, and exceptional mesh inequalities contribute at most 24.

With K preserved moment rows, full rank at a polytope vertex gives

    k_f+k_g <= 4+2+24+K = 30+K.

The actual root polygon has at most k_f+k_g vertices, with fewer when its upper and lower endpoints coincide. Adding the four canonical vertices yields

    f0(P_new) <= 34+K.

K=4 gives 38; K=3 gives 37.

### Three-zero-anchor refinement

When a graph has only its three zero-height canonical anchors, it has at most two caps, one on each non-AB edge of the core. A core/cap convexity inequality is strict: the cap root height is positive while all three core heights are zero.

A cap with two root-fan neighbors has at most one independent active mesh row modulo active root collinearity. Indeed, let the root heights adjacent to its root node j be H_minus,H_j,H_plus, with consecutive spacings a,b. Restrict the cap’s affine plane to w=0 and call its values L_minus,H_j,L_plus. The two fan-edge equalities are H_minus=L_minus and H_plus=L_plus. Because this plane is affine on the root line,

    (H_minus-L_minus)/a + (H_plus-L_plus)/b
      = H_minus/a-H_j*(1/a+1/b)+H_plus/b.

If both fan equalities are active, the root collinearity row is active, and the two edge rows have only one additional independent contribution.

If the two caps share the edge from the third core anchor to the same root node, their mutual convexity inequality is strict. Equality would make one affine plane zero at all three noncollinear core anchors and positive at the root node, which is impossible. The remaining fan-edge rows then contribute at most two in total.

Thus each three-anchor graph contributes at most two exceptional active ranks, rather than 12. For c=d, the two-graph count becomes

    k_f+k_g <= 4 floors + 2 endpoint couplings + 4 mesh ranks + K
             =10+K,
    f0(P_new)<=14+K.

This proves 18 and 17.

If x↔y symmetry is retained, f=g and there is only one height profile. Its floor, endpoint, and mesh contributions are each at most two. Hence k<=6+K, and at most two root vertices occur at each knot:

    f0(P_new)<=4+2k<=16+2K.

This proves 24 and 22. The asymmetric 18/17 successors need not preserve the transverse centroid; the larger symmetric bounds enforce that additional geometric restriction.

### Arbitrary convex roots, not just polygons

Approximate a compact convex F by inscribed root polygons, including points attaining r and R, and retain the same positive coordinate clearance epsilon. Their areas and original body integrals converge to those of F. Apply the polygonal reduction to each.

All reduced roots remain in the same bounded strip: r<=n<=R, x,y>=epsilon, ell=0. Pad their vertex tuples to the established uniform vertex bound and take a convergent subsequence. Its convex hull has no more vertices than the bound. Root area converges to the original positive area; Vol,N,Bell converge to their required values; and positive coordinate clearance remains. The limit is therefore a genuine finite-vertex successor, not a coordinate-patch or zero-area-root surrogate.

For the three-row version the same argument preserves Vol,Bell and area, while the limiting N is no smaller than the original N. This completes the whole root-only reduction for arbitrary compact convex roots.

## 6. Exact complement and boundary scope

The reduction fixes one body’s positive endpoint data and positive clearance. It does not assert a uniform clearance as bodies vary. At c=0 or d=0, the root may contain C or D, so the floor argument above does not apply unchanged. At b=1 the displayed affine coordinates are singular. Those strata are not silently included by division or by a compactness assertion. The previously accepted endpoint and balanced results retain their own scopes.

For each body covered by the theorem, root area stays strictly positive and the coordinate facets stay exactly triangular throughout the construction. Thus a threshold-equality or threshold-exceeding body in this strict root-only class would have an actual finite-vertex representative with the same or greater T. There is no need to appeal to a patch limit for that implication.

Across the unrestricted compact closure, however, root area can vanish, coordinate triangles can become patches, and b can approach one. This reduction gives no new universal strict gap or equality classification on those boundary strata. Nor does it preserve a mechanical sign chamber or imply a census change.

Most importantly, a general body can have additional vertices with ell>0. Deleting all of them while keeping the original root is not a valid maximization step, as the following exact family shows.

## 7. A continuous fixed-root deletion obstruction

For this explicit family only, use s=x+y rather than the general-coordinate s=n. Fix

    b=1/8, c=d=q=67/1000,
    alpha=7/8, K=1+b+q=149/125,
    r=13/16, R=1, eta=1/10000, S=107/100,
    1/2000 <= delta <= 1/1000,
    ell=1-(933/1000)(x+y)-(7/8)z,
    n=(149/125)(x+y).

The ten literal vertices, in their exact index order, are

    0=(0,0,0),
    1=(0,0,1),
    2=(0,1,0),
    3=(1,0,0),
    4=(1/20000,16249/20000,553/2000),
    5=(16249/20000,1/20000,553/2000),
    6=(1/20000,19999/20000,67/875),
    7=(19999/20000,1/20000,67/875),
    8=(1/20000,21399/20000,(8/7)(169/100000-delta)),
    9=(21399/20000,1/20000,(8/7)(169/100000-delta)).

Let P0 be the hull of vertices 0 through 7, and P_delta the hull of all ten. Vertices 8 and 9 have ell=delta>0. The common root is exactly conv(4,5,6,7), on

    933x+933y+875z=1000.

Its xy-projected area is 54369/320000 and its physical area is

    (54369/320000)*sqrt(2506603)/875.

It is positive and unchanged. All added vertices have positive x,y. The entire coordinate facets remain ABC and ABD.

### Actual maximal facets and incidence

The unordered maximal facet vertex sets of P0 are

    012, 013, 023, 124, 135, 145, 246, 357, 4567, 2367.

For P_delta replace only 2367 by

    268, 379, 6789, 2389.

Thus P0 is true 8/16/10 and every P_delta in the interval is true 10/21/13. The quadrilaterals are maximal facets; no integration diagonal is counted as an edge. These are not 10/17/9 bodies.

### Continuous supporting-graph certificate

In the parent’s original affine density coordinates (s,w)=(x+y,ell), the projection nodes are

    A0=(0,1), B0=(0,b), C0=(1,q),
    E=(r,0), F=(1,0), U=(S,delta).

The actual width is W=s-p, where the lower convex deficit envelope has the following four planes and projected triangles:

    ABC: p=0;
    BCE: p=eta*[b+(q-b)s-w]/[b+(q-b)r];
    CEF: p=eta*(1-w/q);
    CFU: p=eta*[1-w/q+delta*(s-1)/(q*(S-1))].

Each plane is below all six prescribed lifted values, which are zero at A0,B0,C0 and eta at E,F,U. They agree with the displayed values at their own triangle vertices. Hence they form the actual lower hull, not a fitted integration profile.

The projected polygon A0 B0 E F U C0 is strictly convex on the entire interval. The last potentially limiting orientation is proportional to 169/100000-delta, which is at least 69/100000>0. The E-F-U turn is positive because delta>0. These conditions also show that the old root remains exactly EF in projection and that all listed actual facets persist.

The new cell CFU lies in s>=1, so P_delta∩{s<=1}=P0. Unlike a generic prism-cut example, this cut removes only positive-density vertices and leaves the entire original root unchanged.

### Original volume and moments

Set A6=6 alpha Vol, M24=24 alpha ∫s, E24=24 alpha Bell. Direct integration over the three old triangles and the one added triangle gives

    Aold=168235227/160000000,
    Mold=5805762499/2560000000,
    Eold=181944063209/160000000000;

    Anew=4263470123/4000000000,
    Mnew=3722919180291/1600000000000,
    Enew(delta)=4553716993241/4000000000000
                 +(19415193/1000000000)*delta.

Consequently the actual original-body data are

    Vol(P0)=56078409/280000000,
    Bell(P0)=181944063209/3360000000000,
    N(P0)=865058612351/6720000000000;

    Vol(P_delta)=4263470123/21000000000,
    Bell(P_delta)=(4553716993241+77660772000*delta)/84000000000000,
    N(P_delta)=184904985954453/1400000000000000.

The volume and numerator of P_delta are constant on the interval; Bell increases linearly. Thus its trace is strictly decreasing in delta.

For complete own-centroid reconstruction let

    S0_integral=5805762499/53760000000,
    Sdelta_integral=3722919180291/33600000000000.

For either body, with its own V, Bell and corresponding S_integral,

    g=(S_integral/(2V), S_integral/(2V),
       [V-(933/1000)S_integral-Bell]/[(7/8)V]).

No old or transported centroid is held fixed.

The exact traces are

    T(P0)=10430000000*5805762499/
           [168235227*181944063209],

    T(P_delta)=10430000000*3722919180291/
           [4263470123*(4553716993241+77660772000*delta)].

For orientation, T(P0) is approximately 1.978284492. The endpoint values of T(P_delta) are approximately 2.000022830 at delta=1/2000 and 2.000005776 at delta=1/1000.

### Three literal integer certificates

Define

    top=10430000000*3722919180291,
    den(delta)=4263470123*(4553716993241+77660772000*delta).

The following exact positive integers certify the entire comparison:

    2*168235227*181944063209-10430000000*5805762499
      =664698685966926886;

    top-2*den(1/1000)
      =112143112034892802;

    2001*den(0)-1000*top
      =18640284474943273724643.

Together with the strictly increasing positive denominator, they prove

    T(P0)<2<T(P_delta)<2001/1000<51/25

on the WHOLE closed parameter interval. This is not a finite sample comparison.

The same data supply the weighted projective integrals exactly. Here the projective normalization has S0=1259/1000 and J=1585081/8000000. Under the actual positive map from the parent,

    I4=J*Vol, Iell=J*Bell, In=J*N,
    T=J*In/(6*I4*Iell).

The recovery below reconstructs the actual image and evaluates those integrals on two genuine tetrahedral fans. It does not use the image’s uniform-refill centroid.

At delta=0, vertices 8 and 9 reach the root plane and the root expands to span r through S. Vertices 6 and 7 are then nonextreme root points. This is an eight-vertex constant-deficit root trapezoid, not a ten-vertex body with the same original root. Root projection succeeds in this particular family; the counterexample does not disprove reductions that are allowed to enlarge or otherwise change F.

## 8. What was tried and the useful continuation

The effective change of framing was to hold the actual graph triangulations and the original moment integrals together, then exploit the low number of canonical off-root anchors. The resulting rank bound removes arbitrarily many root knots without assuming either a constant deficit or monotonicity in width. The construction permits genuine facet coalescences and keeps their distinction from auxiliary mesh edges.

An exploratory frozen-basis LP was not used as a certificate, and no numerical endpoint from that exploration is a claimed successor. The exact RREF construction and active-rank proof above replace dependence on an optimizer’s returned basis. No finite numerical search is reported as a shape exclusion.

The strongest next question is now finite-dimensional within the root-only strict-endpoint sector: bound the trace on its at-most-37-vertex representatives, or at-most-17 representatives when c=d. The more consequential unrestricted bridge must allow additional positive-density vertices to be controlled while retaining the common-body moment coupling. The exact deletion interval rules out keeping the root unchanged and merely discarding those vertices; it leaves root-changing, moment-preserving deformations open.

No new upper or lower global complexity bound, incidence-registry removal, or 110 construction is asserted.

## 9. Complete autonomous counterfamily audit

The following single source unit contains the exact input, true maximal-facet reconstruction, supporting-plane intersection check, two original-volume fans, original centroid and four-primitives-per-edge audit, exact balanced-image weighted integration on two fans, and the interval orientation and inequality certificates. Mechanical weak edge packets are recorded as edge packets, not silently identified with a deduplicated physical weak-point census.

Dependency specification: CPython 3.13.5 standard library, assertions enabled, exact Fraction arithmetic. There are no random seeds, floating tolerances, numerical geometry libraries, or missing parent imports.

Save as root_trace_audit_v1.py and run:

    python -S root_trace_audit_v1.py build root_trace_audit_v1.json
    python -S root_trace_audit_v1.py verify root_trace_audit_v1.json

Expected terminal markers are ROOT_TRACE_INPUT_SOURCE and ROOT_FIXED_ROOT_DELETION_EXACT_PASS, followed by byte counts and SHA-256 values. The full literal input and certificates above are the durable exact object; no generated report or sandbox link is its sole recovery source. A new report hash is not asserted without a retained execution receipt.

```python
# ROOT_ONLY_MOMENT_REDUCTION_AND_FIXED_ROOT_DELETION_OBSTRUCTION_V1
# Exact input parent: minimum-0119
# Parent envelope SHA256:
# fa7cc0adc9cb9b49505b808cd10b74f1d5e035cdd329d849dbe2b508db77dc00
# Python 3.13.5 standard library; no numerical geometry or optimizer.
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib,json,sys
assert __debug__

def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(c,a):return tuple(c*x for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def mean(P,weights=None):
    weights=[F(1)]*len(P) if weights is None else weights
    return tuple(sum(w*p[j] for w,p in zip(weights,P))/sum(weights) for j in range(3))
def solve3(rows,rhs):
    c=list(zip(*rows));d=det(*c)
    assert d
    return (det(rhs,c[1],c[2])/d,det(c[0],rhs,c[2])/d,det(c[0],c[1],rhs)/d)

def hull2(ids,coords):
    ids=sorted(ids,key=lambda i:(coords[i][0],coords[i][1],i))
    def turn(i,j,k):
        a,b,c=(coords[z] for z in (i,j,k))
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    def chain(seq):
        out=[]
        for i in seq:
            while len(out)>1 and turn(out[-2],out[-1],i)<=0:out.pop()
            out.append(i)
        return out
    return chain(ids)[:-1]+chain(ids[::-1])[:-1]

def hull(P):
    assert len(P)==len(set(P))
    found={}
    for i,j,k in combinations(range(len(P)),3):
        n=cross(sub(P[j],P[i]),sub(P[k],P[i]))
        if not any(n):continue
        d=dot(n,P[i]);slack=[dot(n,p)-d for p in P]
        if min(slack)<0<max(slack):continue
        if max(slack)>0:n=mul(-1,n);d=-d;slack=[-x for x in slack]
        on=tuple(z for z,t in enumerate(slack) if t==0)
        drop=max(range(3),key=lambda z:abs(n[z]));axes=[z for z in range(3) if z!=drop]
        projected=[(p[axes[0]],p[axes[1]]) for p in P]
        cycle=hull2(on,projected)
        if dot(cross(sub(P[cycle[1]],P[cycle[0]]),sub(P[cycle[2]],P[cycle[0]])),n)<0:cycle.reverse()
        j0=cycle.index(min(cycle));cycle=cycle[j0:]+cycle[:j0]
        found.setdefault(tuple(sorted(cycle)),(tuple(cycle),n,d))
    faces=[found[k] for k in sorted(found)];edges={}
    assert {i for face,n,d in faces for i in face}==set(range(len(P)))
    for fi,(face,n,d) in enumerate(faces):
        assert all(dot(n,p)<=d for p in P)
        assert {i for i,p in enumerate(P) if dot(n,p)==d}==set(face)
        for i,j in zip(face,face[1:]+face[:1]):edges.setdefault(tuple(sorted((i,j))),[]).append(fi)
    assert all(len(v)==2 for v in edges.values())
    assert len(P)-len(edges)+len(faces)==2
    intersections=set()
    for ids in combinations(range(len(faces)),3):
        rows=[faces[i][1] for i in ids]
        if det(*rows)==0:continue
        v=solve3(rows,[faces[i][2] for i in ids])
        if all(dot(n,v)<=d for face,n,d in faces):intersections.add(v)
    assert intersections==set(P)
    fans=[];moments=[]
    for ref in (mean(P),mean(P,[F(i+1) for i in range(len(P))])):
        V=F(0);J=[F(0)]*3;cells=[]
        assert all(dot(n,ref)<d for face,n,d in faces)
        for face,n,d in faces:
            for j in range(1,len(face)-1):
                ids=(face[0],face[j],face[j+1]);a,b,c=[P[i] for i in ids]
                vol=det(sub(a,ref),sub(b,ref),sub(c,ref))/6
                assert vol>0
                V+=vol
                for k in range(3):J[k]+=vol*(ref[k]+a[k]+b[k]+c[k])/4
                cells.append((ids,vol))
        moments.append((V,tuple(J)));fans.append((ref,cells))
    assert moments[0]==moments[1]
    V,J=moments[0]
    return dict(points=P,faces=faces,edges=sorted(edges),edge_faces=[edges[e] for e in sorted(edges)],
                f_vector=(len(P),len(edges),len(faces)),V=V,first_moment=J,g=tuple(x/V for x in J),fans=fans)

def mechanics(H):
    P=H['points'];g=H['g'];v=[sub(p,g) for p in P]
    poles=[mul(1/(d-dot(n,g)),n) for face,n,d in H['faces']]
    packets=[];U=[True]*len(P);S=[True]*len(poles);saddles=[];weak=[];zeros=0
    for (i,j),(f,h) in zip(H['edges'],H['edge_faces']):
        row=(dot(v[i],sub(v[j],v[i])),dot(v[j],sub(v[i],v[j])),
             dot(poles[f],sub(poles[h],poles[f])),dot(poles[h],sub(poles[f],poles[h])))
        U[i]&=row[0]<0;U[j]&=row[1]<0;S[f]&=row[2]<0;S[h]&=row[3]<0
        if max(row)<0:saddles.append((i,j))
        if max(row)<=0 and 0 in row:weak.append((i,j))
        zeros+=sum(x==0 for x in row);packets.append(((i,j),(f,h),row))
    return dict(poles=poles,strict_U=[i for i,x in enumerate(U) if x],strict_S=[i for i,x in enumerate(S) if x],
                strict_H=saddles,weak_edge_packets=weak,primitive_zero_count=zeros,packets=packets)

B,Q=F(1,8),F(67,1000)
ALPHA=1-B;K=1+B+Q
R0,R1,ETA,SPLUS=F(13,16),F(1),F(1,10000),F(107,100)
LO,HI=F(1,2000),F(1,1000)
OLD_FACES={(0,1,2),(0,1,3),(0,2,3),(1,2,4),(1,3,5),(1,4,5),(2,4,6),(3,5,7),(4,5,6,7),(2,3,6,7)}
NEW_FACES=(OLD_FACES-{(2,3,6,7)})|{(2,6,8),(3,7,9),(6,7,8,9),(2,3,8,9)}

def vertices(delta=None):
    P=[tuple(map(F,p)) for p in ((0,0,0),(0,0,1),(0,1,0),(1,0,0))]
    data=[(R0,F(0)),(R1,F(0))]
    if delta is not None:data.append((SPLUS,F(delta)))
    for ss,ww in data:
        z=(1-(1-Q)*ss-ww)/ALPHA
        P.extend(((ETA/2,ss-ETA/2,z),(ss-ETA/2,ETA/2,z)))
    return P

def ell(p):return 1-(1-Q)*(p[0]+p[1])-ALPHA*p[2]
def tri_integrals(tr):
    z=abs((tr[1][0]-tr[0][0])*(tr[2][1]-tr[0][1])-(tr[1][1]-tr[0][1])*(tr[2][0]-tr[0][0]))
    sw=sum(p[2] for p in tr);ss=sum(p[0] for p in tr);se=sum(p[1] for p in tr)
    return (z*sw,z*(sw*ss+sum(p[0]*p[2] for p in tr)),z*(sw*se+sum(p[1]*p[2] for p in tr)))
def planar(delta=None):
    a=(F(0),F(1),F(0));b=(F(0),B,F(0));c=(F(1),Q,F(1))
    e=(R0,F(0),R0-ETA);f=(R1,F(0),R1-ETA)
    tris=[(a,b,c),(b,c,e),(c,e,f)]
    if delta is not None:tris.append((c,f,(SPLUS,delta,SPLUS-ETA)))
    rows=list(map(tri_integrals,tris))
    return tuple(sum(row[j] for row in rows) for j in range(3))

AOLD=F(168235227,160000000)
MOLD=F(5805762499,2560000000)
EOLD=F(181944063209,160000000000)
ANEW=F(4263470123,4000000000)
MNEW=F(3722919180291,1600000000000)
ECONST=F(4553716993241,4000000000000)
ESLOPE=F(19415193,1000000000)

def body(delta=None):
    P=vertices(delta);H=hull(P);V=H['V'];X,Y,Z=H['first_moment']
    assert X==Y
    Bell=V-(1-Q)*(X+Y)-ALPHA*Z;N=K*(X+Y)
    assert V>0 and Bell>0 and min(map(ell,P))==0
    assert tuple(ell(P[i]) for i in range(4))==(1,B,Q,Q)
    expected=OLD_FACES if delta is None else NEW_FACES
    assert {tuple(sorted(face)) for face,n,d in H['faces']}==expected
    assert H['f_vector']==((8,16,10) if delta is None else (10,21,13))
    assert [i for i,p in enumerate(P) if ell(p)==0]==[4,5,6,7]
    assert (0,1) in H['edges']
    root_cycle=hull2([4,5,6,7],[(p[0],p[1]) for p in P])
    root_area=abs(sum(P[i][0]*P[j][1]-P[i][1]*P[j][0] for i,j in zip(root_cycle,root_cycle[1:]+root_cycle[:1])))/2
    assert root_area==F(54369,320000)
    values=planar(delta)
    assert values==(6*ALPHA*V,24*ALPHA*(X+Y),24*ALPHA*Bell)
    assert values==((AOLD,MOLD,EOLD) if delta is None else (ANEW,MNEW,ECONST+ESLOPE*delta))
    T=N/(6*V*Bell);assert T==ALPHA*K*values[1]/(values[0]*values[2])
    S0=1+B+2*Q;Jac=B*S0*S0;den=[ell(p)+K*(p[0]+p[1]) for p in P]
    assert min(den)>0
    PP=[(S0*p[0]/d,S0*p[1]/d,B*p[2]/d) for p,d in zip(P,den)]
    I=hull(PP);assert I['f_vector']==H['f_vector']
    assert {tuple(sorted(face)) for face,n,d in I['faces']}==expected
    def L(p):return 1-(1-1/S0)*(p[0]+p[1])+(1/B-1)*p[2]
    def ep(p):return 1-(1-Q/S0)*(p[0]+p[1])
    weighted=[]
    for ref,cells in I['fans']:
        row=[F(0)]*3
        for ids,vol in cells:
            tet=[ref]+[PP[i] for i in ids];ls=list(map(L,tet));prod=F(1)
            assert min(ls)>0
            for x in ls:prod*=x
            w=vol/prod;row[0]+=w
            row[1]+=w*sum(ep(p)/l for p,l in zip(tet,ls))/4
            row[2]+=w*sum((1-ep(p))/l for p,l in zip(tet,ls))/4
        weighted.append(tuple(row))
    assert weighted[0]==weighted[1]==(Jac*V,Jac*Bell,Jac*N)
    assert Jac*weighted[0][2]/(6*weighted[0][0]*weighted[0][1])==T
    H.update(Bell=Bell,N=N,T=T,root_projected_area=root_area,mechanics=mechanics(H),
             affine_moments=values,projective_J=Jac,weighted_integrals=weighted[0],image=I)
    return H

def orientation_interval():
    P=vertices(F(0));vel=[(F(0),F(0),F(0))]*8+[(F(0),F(0),-1/ALPHA)]*2
    rows=[]
    for i,j,k,l in combinations(range(10),4):
        a,b,c=(sub(P[v],P[i]) for v in (j,k,l));u,v,w=(sub(vel[z],vel[i]) for z in (j,k,l))
        co=(det(a,b,c),det(u,b,c)+det(a,v,c)+det(a,b,w),
            det(u,v,c)+det(u,b,w)+det(a,v,w),det(u,v,w))
        assert co[2]==co[3]==0
        left,right=co[0]+LO*co[1],co[0]+HI*co[1]
        guard=any(len(set((i,j,k,l)) & set(face))>=3 for face in NEW_FACES)
        if guard:assert left*right>0 or left==right==0
        rows.append(((i,j,k,l),co,(left,right),guard))
    assert len(rows)==210
    return rows

def clean(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):clean(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [clean(v) for v in x]
    return x

def report():
    assert planar()==(AOLD,MOLD,EOLD)
    top=10430000000*3722919180291
    denominator=lambda d:4263470123*(4553716993241+77660772000*d)
    certificates=(2*168235227*181944063209-10430000000*5805762499,
                  top-2*denominator(HI),2001*denominator(F(0))-1000*top)
    assert certificates==(664698685966926886,112143112034892802,18640284474943273724643)
    assert min(certificates)>0
    old=body();new={str(d):body(d) for d in (LO,(LO+HI)/2,HI)}
    assert old['T']<2
    for d,H in new.items():
        assert H['T']==top/denominator(F(d)) and 2<H['T']<F(2001,1000)
    return dict(tag='ROOT_ONLY_MOMENT_REDUCTION_AND_FIXED_ROOT_DELETION_OBSTRUCTION_V1',
                parent='minimum-0119',
                parent_sha256='fa7cc0adc9cb9b49505b808cd10b74f1d5e035cdd329d849dbe2b508db77dc00',
                old=old,new=new,interval=(LO,HI),orientation_certificate=orientation_interval(),
                strict_integer_certificates=certificates)

if __name__=='__main__':
    assert len(sys.argv)==3 and sys.argv[1] in ('build','verify')
    data=(json.dumps(clean(report()),sort_keys=True,separators=(',',':'))+'\n').encode()
    target=Path(sys.argv[2])
    if sys.argv[1]=='build':target.write_bytes(data)
    else:assert target.read_bytes()==data
    source=Path(__file__).read_bytes()
    print('ROOT_TRACE_INPUT_SOURCE',len(source),hashlib.sha256(source).hexdigest())
    print('ROOT_FIXED_ROOT_DELETION_EXACT_PASS',len(data),hashlib.sha256(data).hexdigest())
```
