# minimum-0131

Historical AI scientific report · saved 2026-09-20 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# TWO_CANONICAL_VERTEX_ROOT_PATCH_SHARP_TRACE_V1

## 1. Determination

A complete terminal shape class is now solved sharply. Consider an actual root-only support-patch body whose **only vertices off the zero-root plane are the two canonical common-edge vertices A and B**. The root may be any convex polygon, with arbitrary nonconstant transverse deficit, unequal opposite endpoint values, arbitrary height and overhang. Its original trace satisfies

    T <= Cstar < 203/100 < 51/25,
    2.0287830356734117251411563027 < Cstar
      < 2.0287830356734117251411563029.

The bound is sharp over the nonnegative-endpoint patch class. Its unique normalized maximizer is an explicitly specified six-vertex, five-facet body with c=d=0. It is a genuine convex body with a genuine positive-area root, but its coordinate support facets are quadrilaterals, not the required triangles. No proper triangular-pair attainer of Cstar is asserted. When c+d>0 the bound has the uniform fixed-endpoint improvement

    T <= Cstar-(1-b)^2*[b(c+d)+c^2+d^2] < Cstar.

For each fixed b,c,d in this class, the entire shape supremum is also reduced **exactly to the maximum of two explicit one-variable rational functions** below. This is not a numerical search result.

The new geometric mechanism moves root vertices in their root plane parallel to their neighbor chords. It preserves the ORIGINAL volume, the ORIGINAL ell-integral and the positive root area, while making the ORIGINAL numerator nondecreasing. Unlike the preceding transverse chamber, it does not freeze the n-value at each moving root vertex. It removes all nonaxial root vertices, leaving a root quadrilateral supported on the coordinate axes.

There is also an immediate sharpening of the supplied finite reduction: every root edge meets a different neighboring maximal facet. Its terminal f<=9 patch therefore has at most eight root vertices, and its proper resolutions have **at most 12 true vertices, not merely 16**. This remains a supremum/strict-violation reduction, not an equality or attainment theorem.

Consequently, a putative root-only T>=51/25 body with strictly positive opposite endpoints cannot have a terminal patch in the solved two-off-root-vertex class. At least one of C,D must remain a true nonroot vertex in every such dominating terminal patch. The cases with three or four true canonical vertices, arbitrary positive-ell auxiliary vertices, and the unrestricted weighted maximum remain unresolved. No E17 registry count, global complexity bound, or 110 construction changes.

## 2. Input authority and actual execution

Read the complete current journal through EOF, including the literal parent payload and its full encoded recovery, and read the complete supplied analytic proof. The current journal research-journal(20260920-163546).md is 325288 bytes, SHA-256 a399e76e08f716eb760aea2d56f1da26dd78ff3cd9148aafbf9e65432c2e6866.

The required literal parent is minimum-0128, supplied immutable SHA-256 9b8fa9986220926caf778450ec66563e7e5fe300aa1c9fb53433306b415efa34. Its binary countercontrols and its individual-volume-rigidity complement remain authoritative; none is identified with the coordinator's different old-jb58 fixture. The parent's actual single-vertex reduction explicitly leaves root-only, patch and rigid-auxiliary alternatives. :contentReference[oaicite:0]{index=0}

The supplied ROOT_ONLY_TRANSVERSE_FACE_REDUCTION_V1, material [internal-source-reference], is 16425 bytes, SHA-256 5052276824a0f332449deeb71c26427470ebb70eb1201728d8f985722aebc333. It is used as the stated working theorem, not re-presented as an independently verified new result. Its strict-transfer and patch qualifications are retained. :contentReference[oaicite:1]{index=1}

The parent's three-source recovery was decoded in sources mode and its complete sources/checkpoint were read. No old full certificate replay is claimed in this turn. No source-authority conflict or missing dependency affects the new result.

The new geometry build/verify, exact symbolic-algebra build/verify, and a fresh extraction/build/verify from the complete recovery below all ran successfully with observed, matching terminal receipts. No numerical shape optimizer was used. An initial low-precision decimal estimate was replaced by the exact isolating computation; the displayed Cstar interval is the latter result.

## 3. Precise actual-body class

Use

    A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
    alpha=1-b, h=1+b, 0<b<1, c,d>=0,
    ell=1+(d-1)x+(c-1)y-alpha*z,
    n=(h+c)x+(h+d)y.

Let F be a compact positive-area convex subset of ell=0, contained in x,y>=0, and set

    P=conv(A,B,F).

Require A and B to be true vertices and C,D to belong to P. The root is exactly P intersect {ell=0}=F. This is an actual uniformly filled body. Its coordinate support facets may be patches. When c,d>0, C,D are necessarily nonvertices: they are neither A,B nor root points. This is exactly the two-true-canonical-vertex terminal stratum of the supplied strict-endpoint root-only reduction.

Conversely, a terminal root-only patch with c,d>0 and only A,B true among the four canonical points has this form. Containment of C,D forces the root to meet both positive coordinate axes in xy projection. The origin O=(0,0) cannot belong to that projection: its root lift would be (0,0,1/alpha), making B nonextreme on the segment from A. Also c,d<1 automatically, since the only point of P with ell=1 is A. Thus no additional c,d<1 restriction is being imposed on this class.

Write

    V=integral_P 1, Bell=integral_P ell, N=integral_P n,
    T=N/(6 V Bell).

This is the original functional, including both original volume factors, not the uniformly refilled balanced image. The same functional and marked-patch convention are those of the supplied proof. :contentReference[oaicite:2]{index=2}

## 4. Coupled planar integrals of this one body

Use the ORIGINAL affine coordinate w=ell, retaining x,y. Its absolute Jacobian is alpha. Let R be the xy projection of F, and define from that SAME convex root

    K=conv(O,R), G=closure(K minus R).

G need not be convex. It is not a free comparison body or an independently selected density.

Every quadrant ray has a root interval from radius r(theta)>0 to R(theta)>=r(theta). In its vertical ray plane, the actual body is the quadrilateral generated by A, B and these two root endpoints. The upper w graph is 1-s/R(theta). The lower graph is b(1-s/r(theta)) for s<=r(theta), and zero thereafter. Integrating these actual graphs gives

    A2=2 Area(K), G2=2 Area(G),
    MK=6 integral_K n(x,y) dxdy,
    MG=6 integral_G n(x,y) dxdy,

    V=(A2-b G2)/(6 alpha),
    Bell=(A2-b^2 G2)/(24 alpha),
    N=(MK-b MG)/(24 alpha),
    T=alpha*(MK-b MG)/[(A2-b G2)(A2-b^2 G2)].       (1)

For example, on a planar radial set K, integration of the upper graph gives Area(K)/3, of half its square gives Area(K)/12, and of n times that graph gives (integral_K n)/4. The lower graph gives the same three expressions with factors b,b^2,b. This proves (1) without replacing any original moment.

The physical root area is

    Area(F)=sqrt((1-c)^2+(1-d)^2+alpha^2)/alpha
              * (A2-G2)/2.                       (2)

All denominators in (1) are positive. In particular P contains T0, so V>=1/6 and Bell>=(1+b+c+d)/24.

## 5. Whole-root reduction to the coordinate axes

First let R be a polygon in counterclockwise order. Pick a true vertex v with x(v),y(v)>0 and let p,q be its neighbors. Move only v by

    v(t)=v+t(q-p),

lifting z affinely so ell stays zero. Reverse the direction when useful. The triangle (p,v,q) has constant positive area Delta along this motion. Thus the root area is exactly fixed, not just stationary to first order.

The inner and outer chains of R meet only on the axes. Indeed, a supporting line of R through O that touches a positive-x,positive-y point is impossible: because R contains positive points on both axes, such a supporting line could touch R only on an axis. Hence a nonaxial vertex cannot change between the inner and outer chains before an axis contact or a genuine root-polygon degeneration.

If v lies on the outer chain, G is unchanged, and the changing ear in K has constant area Delta. If v lies on the inner chain, K is unchanged, and the change of the missing-region moment is the negative of the root-ear change. Therefore throughout its actual convexity chamber

    d A2/dt=d G2/dt=0,
    dN/dt=Delta*n(q-p)/(12 alpha)          on the outer chain,
    dN/dt=b*Delta*n(q-p)/(12 alpha)        on the inner chain.    (3)

In both cases V, Bell and the positive physical root area are exactly constant. Choose the orientation making n(q-p)>=0. Then N and T are nondecreasing; if this scalar is zero, the entire feasible segment preserves T exactly.

### Feasibility, compactness and finite termination

All root-polygon supporting-edge inequalities and x,y>=0 are affine along this single-vertex line. The current true nonaxial vertex lies in their relative interior. Retain every current axis point as a fixed point during the move. Consequently the two root-axis intervals never shrink, and C,D remain in conv(A,B,R(t)). Neither coordinate mark is silently lost.

The forward chamber endpoint is finite. Two retained positive axis points and constant Area(K) bound both coordinates of v by the areas of their triangles with O and v. At the first boundary, either a root vertex becomes redundant or the moved vertex reaches an axis. Remove redundant root labels, freeze all current axis vertices, and repeat. The pair

    (number of true root vertices, number of nonaxial root vertices)

decreases lexicographically at every step. Thus the process terminates at a root with all vertices on the two axes. It has at most four vertices, retains V,Bell and root area, and has no smaller N or T.

This is a complete finite actual-body mechanism. It changes the n-values of moving root vertices, so it is not just another use of the previous fixed-n transverse direction. It also does not assert preservation of the full first moment or the actual centroid.

For rational input, take the first nonaxial vertex in the fixed counterclockwise order, choose the sign in (3), and set the endpoint equal to the least positive root of the affine support/coordinate inequalities. All coordinates and moments stay rational. The embedded routine implements this construction and independently checks the resulting three-dimensional hull and original moment identities.

For a nonpolygonal compact convex root, take inscribed polygons containing all root-axis extremes. These preserve C,D containment and converge with their moments. Apply the preceding reduction. The output outer axis intercepts are bounded because their product is A2 and both retained axis intercepts have positive lower bounds; the inner intercepts are bounded away from zero because their product is G2>0. A convergent subsequence gives an actual axis-root representative with the same V,Bell,root area and no smaller N. Thus the reduction and bound include arbitrary compact convex roots in this class.

## 6. Exact optimization of the axis-root class

Write the final projected root as

    R=conv((rx,0),(Rx,0),(0,Ry),(0,ry)),
    0<rx<=Rx, 0<ry<=Ry, rx*ry<Rx*Ry.

Triangular endpoint cases with one collapsed axis edge are allowed and are treated by the actual hull. Put u=rx/Rx, v=ry/Ry. Direct substitution in (1) gives

    T=alpha*[(h+c)/Ry*(1-b*u^2*v)
             +(h+d)/Rx*(1-b*u*v^2)]
        /[(1-b*u*v)(1-b^2*u*v)].                 (4)

C,D containment gives

    1/Ry<=1-c, 1/Rx<=1-d.

At fixed u,v, decreasing Rx to 1/(1-d) and Ry to 1/(1-c) is a genuine nondecreasing-trace deformation by (4). It remains feasible: the upper graph contains D,C at equality, while the lower graph at these points is at most bd and bc, respectively. This second deformation generally changes V,Bell and root area; they are all recomputed together in (4). Only the preceding chord slides preserve them.

Set

    X=(h+c)(1-c)=h-bc-c^2,
    Y=(h+d)(1-d)=h-bd-d^2.

The exact remaining objective is

    F_bcd(u,v)=alpha*[X+Y-b*u*v*(X*u+Y*v)]
                         /[(1-b*u*v)(1-b^2*u*v)].       (5)

Every interior parameter pair 0<u,v<=1, uv<1 in (5) is realized by a genuine positive-area root patch with the outer intercepts just stated.

### Fixed endpoint values: an exact one-variable maximum

Let M=max(X,Y), m=min(X,Y)>0, rho=sqrt(m/M). Write r=sqrt(uv). For fixed r, minimize X*u+Y*v on uv=r^2 with u,v<=1. In the range r<=rho the minimizer balances the two terms; beyond rho the variable multiplying the smaller coefficient equals one. Hence the **entire fixed-b,c,d shape supremum** is exactly

    max( max_{0<=r<=rho} Fsmall(r),
         max_{rho^2<=z<=1} Flarge(z) ),

    D(r)=(1-b*r^2)(1-b^2*r^2),
    Fsmall(r)=alpha*[M+m-2*b*sqrt(M*m)*r^3]/D(r),
    Flarge(z)=alpha*[M+m-b*(M*z^2+m*z)]
                         /[(1-b*z)(1-b^2*z)].           (6)

The zero-area and O-contact endpoints in (6) are limits, not asserted genuine facets. They are approximated by positive-area, origin-separated axis roots, so (6) is an equality of suprema even when a maximum occurs at a degenerate endpoint.

Formula (6) is a finite algebraic prescription, not an unbounded variational problem. Evaluate the interval endpoints and the interior roots of the following degree-five and degree-two polynomials, respectively, retaining only roots in the corresponding intervals. With S=sqrt(M*m), A=M+m they are

    Esmall(r)=b^3*S*r^5+b*(1+b)*S*r^3
                 -2*A*b^2*r^2-3*S*r+A*(1+b),
    Elarge(z)=[M*b*(1+b)+m*b^3]*z^2
                 -2*[M*(b^2+1)+m*b^2]*z+M*(1+b)+m*b.

The positive derivative factors are explicitly checked in the symbolic source. Thus the unequal-endpoint freedom, including unequal inner intercepts, is controlled rather than replaced by a symmetric input assumption.

## 7. Universal sharp constant for this complete class

From X,Y<=h and u+v>=2*sqrt(uv), (5) yields

    T <= H(b,r),
    H(b,r)=2*(1-b^2)*(1-b*r^3)
                    /[(1-b*r^2)(1-b^2*r^2)],
    0<b<1, 0<=r<=1.                               (7)

At the axis stage, with Duv=(1-buv)(1-b^2uv), the gap from H is the sum of the nonnegative outer-intercept slack and

    alpha*[(bc+c^2)(1-b*u^2*v)+(bd+d^2)(1-b*u*v^2)]/Duv
    +alpha*h*b*u*v*(u+v-2sqrt(uv))/Duv.

The original body may have an additional nonnegative gap from the chord slides. Because Duv<=1 and both parenthesized factors are at least 1-b, this proves the fixed-endpoint gap stated in Section 1 after the genuine reductions.

### Complete boundary and stationary-point proof

At b=0 or r=1, H=2. At r=0, H=2(1-b^2). As b tends to one with r<1 fixed, H tends to zero. The joint corner is controlled uniformly by

    H-2 = 2*b*(1-r)*Z / D(r),
    Z=b^2*r^3-b*(r+1)+r^2,
    (1-b)^2-Z=(1-r)*[b^2*(1+r+r^2)+1+r-b]>=0.

Since D(r)>=(1-b)(1-b^2),

    H-2 <= 2*b*(1-r)/(1+b) <= 1-r.

Thus every boundary limsup is at most two. But H(1/4,5/6)=133020/65569>2. A global maximum exists in the open square.

The denominator-cleared derivatives, after removing nonzero interior factors, are

    Fb=-b^4*r^4+2*b^3*r^6+2*b^3*r^5-b^2*r^4
          -4*b^2*r^3-b^2*r^2+2*b*r+2*b-r^2,
    Fr=b^3*r^5+b^2*r^3-4*b^2*r^2+b*r^3+2*b-3*r+2.

Their exact resultant in b is

    -4*r^8*(r-1)^6*(r+1)^4*(r^2+1)*g(r),
    g(r)=r^8+4*r^7-2*r^6-12*r^5-7*r^4
             -4*r^3-12*r^2+12*r+8.

Under r=t/(1+t), the coefficients of (1+t)^8*g(t/(1+t)), in ascending order, are

    (8,76,296,624,773,548,176,-8,-12).

There is exactly one sign change, hence at most one positive t-root. The opposite endpoint signs g(0)=8, g(1)=-12 give exactly one root rstar in (0,1). The exact Groebner basis of (Fb,Fr,g), in b,r order, is

    16*b-3*r^7-11*r^6+9*r^5+33*r^4+20*r^3+12*r-40,
    g(r).

Therefore there is exactly one interior stationary pair:

    rstar = unique root of g in (0,1),
    bstar=(3*rstar^7+11*rstar^6-9*rstar^5-33*rstar^4
              -20*rstar^3-12*rstar+40)/16,
    Cstar=H(bstar,rstar).

Exact interval arithmetic places bstar in (0,1) and gives

    rstar approximately 0.830257154286175263672412869160,
    bstar approximately 0.236133083471972754665580307112.

It also proves the Cstar bracket stated above. The source performs 110 deterministic rational bisections of g and outward exact rational interval evaluation, not a floating root solve. The derivative identities, resultant, Groebner basis and substitutions are all checked exactly. Cstar also satisfies the following additional annihilating polynomial:

    y^8-56*y^7-770*y^6+22898*y^5-20936*y^4
        -3044*y^3-3960*y^2-93312*y-139968.

The boundary argument plus uniqueness proves that this stationary pair gives the GLOBAL maximum in (7). No finite sample or failed search is used as an exclusion.

### Actual sharp body and equality

The sharp body has b=bstar,c=d=0 and projected root

    Rstar={(x,y): x,y>=0, rstar<=x+y<=1}.

Its four root points lift by z=(1-x-y)/(1-bstar). Together with A,B they give an actual 6/9/5 body, with positive root area and original data

    V=(1-bstar*rstar^2)/(6*(1-bstar)),
    Bell=(1-bstar^2*rstar^2)/(24*(1-bstar)),
    N=(1+bstar)*(1-bstar*rstar^3)/(12*(1-bstar)).

Both coordinate support facets are quadrilaterals. This is the patch maximizer, not a genuine triangular-pair maximizer.

It is unique in the stated normalized nonnegative-endpoint patch class. Equality forces c=d=0, both outer intercepts equal one, and the final inner intercepts equal rstar. The area-preserving slides then imply that the original K has area 1/2 and contains the canonical triangle Delta, so K=Delta. Its missing region G has area rstar^2/2 and the same n-moment as rstar*Delta. Among measurable subsets of the quadrant with this area, integral(x+y) is minimized uniquely up to null sets by {x+y<=rstar}: subtract rstar from the integrand and compare the portions on either side of this line. Equality therefore forces G=rstar*Delta up to null sets. Convexity and closedness of the original root identify R exactly with Rstar.

Over the class where b,c,d may vary but c,d>0, Cstar is the supremum and is not attained. It is approached as c,d tend to zero; the supremum for fixed positive endpoint values is instead (6), with the strictly positive gap above. This statement concerns the solved patch class. Proper root-only contractions also converge to the sharp patch, giving a lower limiting value Cstar for the wider proper root-only problem; they do not establish an upper bound for that wider problem.

## 8. Threshold boundaries and the smaller remaining domain

The new estimate is uniform over all root shapes, volumes and heights of its class. Its b->0 and b->1 boundary limsups are at most two, by (7) and the preceding joint-corner argument. If the positive physical root area tends to zero, its projected area does too. Since K contains Delta, A2>=1, and r^2=G2/A2 then tends to one; again the trace limsup is at most two. A collapsed root is never relabelled as a facet.

The c=d=0 boundary is different: it contains the actual sharp positive-area patch above. One-zero endpoints are covered directly by the same proof, not by dividing an endpoint parameter. No statement at b=1 uses the singular w-coordinate map; only limits of this class are covered by that argument. The separate accepted balanced theorem keeps its original scope.

Now apply the supplied terminal-patch reduction at fixed 0<b<1,c,d>0. If its dominating patch has only A,B off the root, the new Cstar bound excludes T>=51/25 for the starting proper body, INCLUDING equality, because the dominating patch itself is uniformly below the target. This implication does not require resolving a patch back to triangles.

For the general finite count, a true k-sided root has k distinct neighboring maximal facets: two distinct maximal facets of a convex three-polytope cannot share two different root edges. Therefore

    k<=f-1<=8.

Adding at most four canonical vertices gives at most 12 true vertices in the patch and at most 12 after the supplied root contraction. Thus the full proper root-only supremum equals that on bodies with at most 12 true vertices. Strict violations transfer to that smaller class. Equality/attainment after contraction remains exactly the qualification in the supplied theorem. :contentReference[oaicite:3]{index=3}

A remaining high-trace terminal patch must have three or four true canonical vertices, f<=9 and k<=8. No exclusion of these remaining continuous shape strata, of arbitrary positive-ell auxiliaries, or of all proper contractions of a solved patch is claimed. In particular, no monotonicity of root contraction is assumed.

## 9. Exact actual controls and executed continuous checks

### An unequal-endpoint polygon reduced through both chain types

Take b=3/10,c=1/10,d=1/20. The initial projected root, in counterclockwise order, is

    (0,9/10), (7/20,7/20), (4/5,0),
    (11/10,0), (7/10,4/5), (0,6/5).

Lift every pair by z=[1-(19/20)x-(9/10)y]/(7/10), and take the hull with A,B,C,D. The only true off-root vertices are A,B. First move (7/20,7/20) in direction (-4/5,9/10) for 0<=t<=7/16. Then move (7/10,4/5) in direction (-11/10,6/5) for 0<=t<=7/11. The resulting projected root is

    (0,119/160), (4/5,0), (11/10,0), (0,86/55).

The first move is on the inner chain, the second on the outer chain. Throughout both COMPLETE closed intervals,

    V=3083/8400, Bell=33329/336000, root xy area=9/16.

The numerator slopes in the displayed parameters are respectively 19/89600 and 1/525. The exact endpoint controls are

|Stage|True V/E/F|N|T|Own-centroid strict S/U/H|
|---|---:|---|---|---:|
|Initial|8/13/7|1567599/4480000|164597895/102753307|5/5/8|
|First wall|7/11/6|12544117/35840000|1317132285/822026456|5/6/9|
|Axis root|6/9/5|415389461/1182720000|14538631135/9042291016|4/5/7|

All primitives at these endpoint controls are nonzero; no weak packets occur. These are not whole-interval mechanical census assertions. Their changing own centroids are integrated from their own uniform volumes.

The exact interval checks include all 83 planar convexity/coordinate rows, the original signed three-dimensional moment polynomials, and 251 supporting Bernstein coefficients, 137 negative and 114 zero. Endpoint mergers are re-hulled as real mergers. These checks validate the two entire motions, not just endpoint samples.

### Axis controls, one-zero data and proper resolutions

For the first three axis controls use b=1/4 and rx/Rx=ry/Ry=5/6, with Rx=1/(1-d),Ry=1/(1-c). Each is true 6/9/5:

|c,d|Original V|Exact T|
|---|---|---|
|0,0|119/648|133020/65569|
|1/1000,1/1000|14875000/80838081|8312080599/4098062500|
|1/12,1/1000|59500/296703|16441080599/8196125000|

The last has genuinely unequal endpoints and c>1/15. A separate direct one-zero control uses b=14/61,c=1/4,d=0 and root pairs

    (16/19,0), (1,0), (0,4/3), (0,76/75).

Its unequal inner intercepts exactly balance the fixed-endpoint interior branch of (6) at r=4/5. It is true 6/9/5, with V=2602/10575, Bell=29963/430050, N=1024333/5160600 and T=1203591275/623709808. All four axis controls have own-centroid strict4/4/6 and nonzero primitives. They are patches, not triangle-pair bodies.

For each positive-endpoint axis control, contract its root toward the arithmetic mean of its four root vertices by epsilon=1/100 and 1/10000, and adjoin T0. These are separate, genuine proper root-only bodies. Their actual data include

|Endpoints c,d; epsilon|True V/E/F|Original V|T, for orientation|
|---|---:|---|---:|
|1/1000,1/1000; 1/100|8/16/10|13760843/74850075|2.028221769591203|
|1/1000,1/1000; 1/10000|8/16/10|220368396901/1197601200000|2.028294502990786|
|1/12,1/1000; 1/100|8/17/11|36010331/179820000|2.005594515479792|
|1/12,1/1000; 1/10000|8/17/11|40066780309/199800000000|2.005954147119906|

Their complete rational moments, true maximal facets and roots reconstruct in the source. Every coordinate support is checked to contain exactly A,B,C or A,B,D. All four own-centroid controls are strict4/4/6 with nonzero primitives. An 8/17/11 body is not the open 10/17/9 layer.

The source also includes a deterministic rational proper sequence approaching the sharp patch: bisect g for 2n+20 steps, take the rational midpoint rn, set bn to the displayed polynomial b(rn), c=d=2^-n, form the axis root with ratio rn, and contract it by epsilon=2^-n toward its four-vertex mean. Its coordinates, heights, volumes and moments are entirely rational. The construction converges to the sharp patch, so T tends to Cstar. Values n=5,10,16 were fully audited; their traces are approximately 2.0138187398, 2.0283947437 and 2.0287770100. They are nonwinning controls of the limiting reconstruction, not a claim of unrestricted optimality or new record complexity.

Every actual control uses exact supporting-triple maximal-facet reconstruction, independent supporting-plane intersections, true edges, and two positive interior tetrahedral fans with identical original volume/first moments. The actual balanced image is separately re-hulled and two weighted image fans verify

    I4=Jp*V, Iell=Jp*Bell, In=Jp*N,
    T=Jp*In/(6*I4*Iell), Jp=b*(1+b+c+d)^2.

No image uniform-refill moment is used in the trace. The exact packet audits use the ORIGINAL body's own centroid and one identity metric.

## 10. What was tried and the useful continuation

The decisive step was to exploit the full convex planar root rather than treat its two graphs or their moments independently. In the two-off-root-vertex stratum, the original body is a difference of two coupled radial cone integrals. A root-ear chord motion fixes both denominator integrals exactly and changes the numerator with a known sign. This makes all root-coordinate complexity removable without any maximal-width-filling assumption. The remaining unequal endpoint optimization has an exact two-branch solution, and its universal envelope has a unique algebraic maximum.

The exact source replaces the initial symbolic/numerical probing and reproduces every load-bearing algebraic finding. No finite failed optimizer is being reported as a bound. No computational successor depends on the unsupplied special collective old-jb58 code.

The most useful next direction is the terminal stratum with one of C,D still a true vertex. There the root fan gains a third positive-ell anchor, so a root-ear movement can encounter an anchor-switch constraint away from the two axes. A correct extension must retain those actual fan switches and the original coupled volume and ell-integral. The solved r=2 stratum and the at-most-eight root vertices substantially reduce this question, but do not answer it.

## 11. Self-contained recovery and observed pins

Save the full source below as recover_two_vertex_root.py, UTF-8/LF with a final LF. Run

    python -S recover_two_vertex_root.py sources work
    python -S recover_two_vertex_root.py build work
    python -S recover_two_vertex_root.py verify work

Environment actually used: CPython3.13.5, assertions enabled. The geometry child is standard-library exact Fraction arithmetic. The algebra child uses SymPy1.14.0; the wrapper deliberately starts that child without -S. No NumPy, SciPy, numerical optimizer, random seed or external input is needed.

|Object|Bytes|SHA-256|
|---|---:|---|
|recover_two_vertex_root.py|12813|a17b6b813068e54a0ab7d639ac06177b8307d98bf971fcf54713fc9993595316|
|Complete two-source payload|22877|b086461f27b15241d981b16919378ce60cfa496e373789a7dd0d5bc6d13cbc00|
|two_vertex_root.py|18600|2f811628c558c5181a81da1c0ef839715aade53833d70f429471f96818dd04f5|
|two_vertex_algebra.py|3752|2f8d1b2a5e1736da6ed8090821e046ff848f7874fa910e84c7df50aee027d80f|
|two_vertex_root.json|330612|e6a1040f20f21db2e9016dfc6991177d59f53bd5a1f1e9db71e0bad575ebad8a|
|two_vertex_algebra.json|5715|3efd2b3deb81d6a58360b04fd6c4f2580df6c2c6c0a0286a6204a19cffb251f9|

Observed markers: TWO_CANONICAL_ROOT_SHARP_GEOMETRY_PASS, TWO_CANONICAL_ROOT_UNIQUE_SHARP_MAXIMUM_PASS, TWO_CANONICAL_ROOT_SELF_CONTAINED_RECOVERY_PASS. Original and fresh source-only runs reproduced both report pins. This is exact computational algebra plus the complete geometric proof above, not proof-assistant formalization.

Convenience copies: [autonomous recovery](sandbox:/mnt/data/recover_two_vertex_root.py), [plain geometry generator/verifier](sandbox:/mnt/data/two_vertex_root.py), [plain algebra verifier](sandbox:/mnt/data/two_vertex_algebra.py), and [complete sources and reports](sandbox:/mnt/data/two_vertex_root_complete.zip). The embedded source, not these links or hashes, is the durable reconstruction.

### Complete autonomous source

```python
# TWO_CANONICAL_VERTEX_ROOT_PATCH_SHARP_TRACE_V1 autonomous recovery.
# Parents minimum-0128 SHA256
# 9b8fa9986220926caf778450ec66563e7e5fe300aa1c9fb53433306b415efa34;
# [internal-source-reference] SHA256
# 5052276824a0f332449deeb71c26427470ebb70eb1201728d8f985722aebc333.
# CPython3.13.5; exact algebra child requires SymPy1.14.0.
import base64,hashlib,json,subprocess,sys,zlib
from pathlib import Path
assert __debug__
PAYLOAD_PIN=(22877, 'b086461f27b15241d981b16919378ce60cfa496e373789a7dd0d5bc6d13cbc00')
SOURCE_PINS={'two_vertex_root.py': (18600, '2f811628c558c5181a81da1c0ef839715aade53833d70f429471f96818dd04f5'), 'two_vertex_algebra.py': (3752, '2f8d1b2a5e1736da6ed8090821e046ff848f7874fa910e84c7df50aee027d80f')}
REPORT_PINS={'two_vertex_root.json': (330612, 'e6a1040f20f21db2e9016dfc6991177d59f53bd5a1f1e9db71e0bad575ebad8a'), 'two_vertex_algebra.json': (5715, '3efd2b3deb81d6a58360b04fd6c4f2580df6c2c6c0a0286a6204a19cffb251f9')}
BLOB='''
c-qZ;ZFl0vlJNKESFp+12MHQm5*XXyo^w1e9%ts__%buzBn->Zn~gjm$wGL5oc#B#s_vFr0w>vg+T1(1U#qLD>s>AV{zLvfnLUSD
9&Tpt;vw`h_bA=|F!<re#^?X~dG_Y==I5KA-dz4`cK2@l`Q0zG@y|bhp50!4esewhbbUF#oqZl(zIivhvj>fE<NA4HwOxA2BJvwP
0FCY=-_66LuknwKH@Dk-p2Usrk=;EyVU17Q<?Xg%AKASl>!|T2S*C6rLH|RTEW<q8Hr8>JH=<P|iW~VH{`zjZS}zb-v`mwXmP)q`
chy*ZjqkH$*+|`dzKFbr?7xMoHh9GzS4qs~?g|HejosA>P;AU*LFla?X0wJH2aVOy49T$qOlC9An*zV)*Vtnj%h{SeGoJ-)#FlKw
S4U#EE2HT(vPRxmH=Y}QBWR2o%f_y0!WxTo?sB{14d>i$!=g9qC3ji|w6r`^{LNaeE)0De#$47j*(1td<13Ftt<}S!y|x4GtuB`P
TKPndZ}mF8mMnG^3>rtj9jF1oj2H9T#b7lrYl{XN-^F=f;|C5cXKg~^wByj~9orErpQ?2U47Fx${L?=B8o%ZSEp*zpZ87a!%<6W<
G{-9EwR@I%Z1;=9SsjHN;ETXm9R<<-y#eH7KsTUO2Z}A(3RP$Ytc<K<o2@I)<lOpG7}-G>nJEa>GCYK1cx{B1320fkf&;$?9#1j=
1=aN;cjMf+^4L`d>zn&4!XQDiGl^QO4+Vq@hiMR%%+`Z||Nb?Af5?*1i^I&A2&fNJ28>riUPP<hc>fw^Ozb|K4*a}^LBRh>)<{uQ
1UlxRKqU*8fNq{Vg!vo*r$?)`w=z8T+BA>c)hu2w!wf_qPL_r_v8L>S$qg?P4=}n-7F(F_yRjcG48v~cCT{0JfB~5}rZ&@Lc@51h
L_rDz0{|Vli^a@O!u$J`0b>FEGj`f%&Uv5pogO<q?Xr{J8MC3SbH;!bU`wm$Aztwb2pJR%*KFV(UEE_GU?aM3xYLsS>!q>z55A=d
8@9zMyC^jXAfw-jJ(waI_Sg6~u1O0WPMc(;ewM&1z+uQW$Ri-1z(c<sW;7IDppw)1ts}-69!+Uy2-<8z0S1V<KQ`Wx-dxAw)7o8h
!Z=8iD9#&RvIc#GIw{ImjW~(p@WIWa=dclkpjM#~G~wH~LT9X7&xOvw^4ItmZp_<0HTvf8SF8n83!wAgoD@^b_@yPM<D~Yls`d;u
^Z4!CudzZ$O@N*FZNKH4m5I<Aw1ZY)?gMZ^MUp<35at5Ima%R>qaIPCBn1_p0kw~j*8eUD(kURBg7=;o5c7Cl(DBpU&C*7a=Fu|R
0j0o}B==xC!Uotl-~kXT_|3!24^yD1n>Vh0`sLl*hKCxR2%W5<m+TCXcHw3Zq1yJSy+rO9wRWvtd)eB-=IE56q{zNQ1wfNPnzHDb
&WghnPbd<YhC0_o5U8p~#1*Oo_+{4~A&+>}uul@Hr)UMXGdskCFs;61iCD`iaf3=hs4uIqG2-rjJ8a3r|8^RA(f~<~?zg~m`CQs@
a0Ft19<CbSBQV=*&9JY4PqVO-B}op(7lbWES|iC^7V0+9ZG=shCaZ`j@i|+EKp~hMD5|<Gw;i@Z$uU@Mt+AnCp4Ae>ygnMm&xJu`
H<3y9X@!djCi#6mfRV>8dmgy(H~a(Se@TivOx7!bREL(SiSi*xJAh&zgg}QN$Bkemmn~u4@DKAaR9aAJ(D2xO5dhoa?=kM(JhZR?
PvCT}BjYY<ga)42svsJ2pCqQKOnyg>Z<jqZ=|w)IHNjLUZ3ytQRvi&M9ppU1a;x*k7QLf4DHs>N1$)vt>9@A%S)86)SOCw)IXgeY
;t4ni=UwXVb-Grshox?(d)~*9+s=8n3!cNaV|UNb``~Z*Dc>`Cq`bGNyv@I3{s6NVt^EV@Qy6l<*uNob-#xP}%j%s%;q0_;o!R!u
snfUm&MEwN-h+M8t_4ZRYt=k(k}2h|qB@(A!g_WW%wL2qaC+iB@*whaBX=Ko^MB`}HyL@%yyD}suW>{DS03C9On;t%FJUsRF%ylM
$q>;Q?gQu+xeIE4Fqv0xdu{6Q3o23{)J&!v9<cM!v=K&rgBJV!>nQ_6AFWry&V$Jd;~X3UAW3E5%YMdGU;IAWguzT%li8l8#`Wus
CacZblQf)FZ>;S3O`Rm-_}QCTl^Sn|9CYZsdh~|IY>O~9Ad)!(JfDGux*}$g4HJ7x9$?d3M~k4znnJ6iq-E}RZeaLx6o9^78N^Kn
FcT~Z%r^TLZiPl+t1xvl7r1`K4FJKKgQjV=n_s`iP4g&>{UittbBK`^$M~wiX5vg?9dN`nY#@FTs0?uY(f2IMfwQ)G2x`y$4#UI6
DpZ~-4aq_`kRxDwFz9QXW_aK=Rwo|+a`V%_zr2%7KDzwnr_q-YF#e}cO@?&BB~-L`1SEA%`qXwb4>v*d5Q2+}l>LGIP?Nxa767AV
y#>PvJURfo_%M6(>&f@t_wAcJJbn9o7Y5(|D{|I>^Nx|Ta(xN-G|s)Vd-weOtnYx5bNaq}e|mb>JF!B)-#_Vh!_)BOKI~eS>)QVL
y?4^>b-P`w@Ad4H@ZRnAh6syL`uXNxzalO-p8(NM?`Bts)%e}pFK<5o^z#ki$H3#sXQy^I@I5c=1%3PM<izcH*6GZ$b(~JD6URC2
pE*6(y6<+KUhg~zL+{k~oqo?b?VVbo=i!g-SoW!N7M$ImpMjEd+|cs@y#vvHV+DL3xLE*^0XP=f_NZ}5r;d(8BaB^d5e7$%o20Qy
7H|^B<D2(KQa#>hpoD3hRE$@$0VDq_IS3dl%M-9HYLK5Sy(lIx@b6>?B%6o~0dVkscHk>0UvRt|L6RFTM0<lQ%-2~=!G^JE?FAb+
#$;E9g*=86!R}Nh=IeA38k^4HnPLu@d&6gLZI0jCl-kdgL;WmStttx`E{I^u1HtUL@B<}#%4EsHHcRv}S+cRs7QGT^5YlFuUjP-`
7mH!LLKM}>E&Cou4|CAbH%T0t1EB>~+vLiy&1nlI^Ohnu*?}n@9N$1?pc=*0%C3>n-&^VAaY~#2&Qe7%IfvbX*GQv8U6_bRG7)b4
5E|X$D3HmzMwWbEv24ClnEIUJRs`9?KGPfq97zD-ju;`CBB-Ee;1B@Ad?c`sitspK*yy7}A$n?!G!&OU#&AqvHD50lju8bgJV~;k
Knq$pDrvBA*a@ndFWjXUKqx#g#L!7JC8$LOphu=e8et=%M#LW3HwBfpgGb91jGZ9tj%<h+YnEfxW((c{2hmqNV|I*!f2duJDKYTp
ZUnX~e9{qsxPninWgXX#aD5o34I?(1M~jf`A51b|*<|@>TTq{LfQ{)dZTx~;1E?LPNotr?Fxc#-DHwDk+TR`YR*qI64OBNL0|4DF
>XQN1MXP>(z}kZfs|a@IoD4Ud{;i_vJ%;!E_diq(HjX66&Fi|$5UeY}n5?T)FXloHQM25FT(Da>dNAlz{U)p0CPC(6jM?I?5t{=)
iSsC4hh;x7J4kmd<_%X1*Z;;RqA4{yL8Hhq-A*e&mw2!^+PttXmhMJY4y=HKi~d*EAm*syIyQ?@)H;D$w4*6FYSI==VlEWIPOvM>
aa2f-yqkv-I4+fgkF9M#$dZ)f@=6=%qO=>h5EjHB1R(Y92E6~tt`r9~1EKEzgCisjqclq%Lm%XmPmFYelY#Z8Ocw3w)I3Z&e+zCH
7h(@)rvOtuGCTnNoM{$9WvUE|sZ$pXPOZ}f`d(NAYB-YavMv~p78iXHF!IL0^Q1bELf|MsJz4`00V)n2t%}$JFCPJWgBZBr(;8A^
3#BDNG1)4rEM`F=3a*dzCMdwSL@W{n34l7x=`akyX)8oV3fS)vjYk*=6Q>cpQkP)$56)5gD#B!zqIVxLLqRaB>_osSN>i*0F2A8<
<AUqLVeXBUI7Y%`m9T{!R8Tk%B$~LUS<{N_QJFhJ6n`*@*`~q(bkTsw^WrI>M#n7eWNIn}cpp{G8g2<`gOP<pt3DIH1Q!C4HG1Xd
0rl3wKQzp2V^PoyfJg&|fy^otUL0*uBRwe7Khb#tQcdrnZ3cG1E@A7+vj%8Y-9+Y_j5#QS0~+a>>&`$4)Tsfj%4B)?&&A>IaiBS<
Z2ZU#0^_+#zA9z7Fc3;8F!?<lE|aAQd#5GMGO#viq=naIGU<JRhZVJLvqZeY?w|%V8s2eqO@|-QEwjKa>kj>Ju~=2C@gAqcy5_}8
yRGu;UVqJ;*IYB3sna$)wpkmioFM8)KZpK4s=sYu{-JPXCTO}|;)deLlLdKo!Xd{!k@ED)qEAKhxW7MH(ga|<vi5uL+8lcJ+Y61R
49VaFC^{P4GGHyNxcKAYj}JfQac>_C9g&h=as~l_Zs8@f6hrQq&;cJn@`uP#MGq{>2wY8|B?O={=c;T=BHpnNyzH+yN|chK6v>L;
GNI7vmkFgUm5|U8)Hah^pPDA2IJHpI`eJM)g`=nm!8+#UxMXcssvo8+jXQqF?xSp#&ji-|1ACCZ!{+#|^e{e{jHC^J3U7QFg0mM#
{>r#k{CLZ+Crz=*=5+XgwFf9X^9eFd${r5b`7~MJF44`gkBy)s1nGfH@}8goK*GH_RkOjB2}$^eU-$&`Gb(@@e$wl-3b<^bVraSP
@O$Wf!@s)_TnBEIx`XThSUWa1l|g}JiF(Z`lf{`tqo#E^>49gEF%pw!l)-0mGMVUjR2>m^JYq-f_;4IyJGmEQMP&}|l5Ca0iuQ8Q
y&5#1nmX5if#v=`2mF95FRbAgSXfkTtbT%dqUwn1TvoeK-E&Q$16?Ia$x_zPcpe_iEeb^}67S^u04e{{JUWdwrw5c^kF*>nKpM)^
E+%V7#c+UmNaXOm>6fkY44P)ZD9YW~RNaj)<Zf)HYUHOEM}ATx_k~Z+z2=fc4EH-DrcvCAE#S>YOM37#!%fe8@ZoY!`)6vL{7WK7
8JeY=&-DZjTlh=%;0G!bw2u8sk|zs;wI3>p1;my{s#rD^!F(!-R)&wM3LY^QN-<&_q<W-SNjju5V}Q0hWlv=y2G^Q2z}*LX1Eh*B
1Za`Ou*|mcROxvtdg|60`AE!VVxVa@RQe?jA8<nzjP%e*VYl*K#8pev2>doJUmL8Trl^c)GjhYq2atHQ1s-6B_1M&{a!9JH1~TT%
tBycoO``TAm^l}pXX>;?>@tN;h&k?*<qG1CT$6HbpRgAZ_h83&t-S45!0lABDvO?VdJzqxR$B21bbliSuc!eXV*d&sJnQ{L9ky=R
*8G!fU0P4^Nl*fSILy*Ql+*T8cjc0FST5>Q5A`V{D5C8V+fezMdW2xW-W<>x4zu9bVzybVQ%_wA@xf)7fcfJ7n1K{xC8WK)pah=o
Wd^-4146S!!sd}W;g}2RckH2GFkjr(8Se2f8BX)3zy&l1K6zAb3l)cf$*a~PX|;^U4wQ^})LA5EtM%=L#G((>Y+V^N_Zw<mD#fV1
>#piISj?<rfXElFLl(M=Sv4D!WYGhJHw%6%>I>HcePE%5zOA_S5F^&|8EUG&f6yy13>6r<8UqQfOl%ErRXNQiQNM*@x)*!>U&}bD
bkk0yn|3dzo620%!9){;3zG$bSg_}Mg2+^eJx~8;dgxK6haSuH(Bpo38Noj8rH7F6N9#1ewaXmu#MqUoqFpUjB)6?dDb80p(Fo5R
UQ^=8s6{+tB+wEZIZ<v-fe?Z}4vpMP0H^~v6xNphsfK0MY+h^D7^ngcLg_!tA(KCe<Nj*N7emIWvTd*x2!%hZHSf4oT^Q=#L7cmn
dHB4S5I+z_4g;<!Jw1#@C4I+)1rFF1pw+K9r-ws7nuY~Alhkj($X?(-?7>(N6cPTK1lZ}BH6O5y?~v@$Rapm74kYl{6ALO&Vgmj|
DUs?E7x^%wys7$agI87CPs49pD#!s4ET&2v(t+KEV8%AVxLQ+ic0>`M0MK2XbmB<PinTf4He&d<EsYfeuDPx*hj$oN-9c3K3;UJ*
h7~=6YsyK$x(j|MQTRo!|Epa5w_(g-sb6rNUxzu5kBxrou7z`|u`af}65c!Nl%<;*xJjl(dGdlynWg-_l2p^Atim$Hl{zy6H`mx%
W-;m63##6b|L$(0)j&PzIh--nQ6nob!AVn0bc^ee8*yQp48L3gA8D7K{$Bt@0vMQ!Q~|!f^<|10;V{f_TbSFn^{loA1$56?kCP?E
;gC71P&Bq<@wlor2H8iR8H+5Qs9V!|z7sHD@Q<>c_!pC%rg`jCRTnIvGBRLSiGka}@X__T*IHTde;F2}6?0q1UiUG$q(wW%-=SRS
UeEiaX%Vc!8c3PrdqyQ2OCAZr@x7ATpM=g%OK3j<KgetbC~9K&qFO#X`<Ld`+IXeZK3-Yi)sQsNQM3*F*b_qNXcNP<J~N=1I1y`4
vZjPlJUPV&8P#l~NEIQi5Mej2QVKHzDvemnT8k7Fxflqcme|WfU`zl%ZBNp4U+03!qZkea^Ir@GgY8YTB;fcYSy2!rcd;_-*|;L?
fkkmni*Kp}Tui<lW7kk*4#0P;ju06HbSaT(iIm5}r2uzUF(+WfFo{-A*NJ?Cnhd0-`F|6DItImDLg#2H0J(QHj<R({1@GM$!1%2@
hQFxgs1R2tW0M8|85Q)T-U1@3SAoqqm(NG9l|%CyH8Cx5!(;ZD=i+MEW;+ui4?m&>@7F}AK}n62YOm}l+v;hDA{WQ?tQ=Fw(M_p`
%w4RwhOc^_hAD^-9Cpj1rHfe#k)=%2`YNKkNG?`H^MI2htnFq$csp>NLb^oww7MELZAyRIW3I|RyDE6vY)N5^i}90jMNEWZ7PsvS
uYHV<dB%lD<mUd|pgYcV5M?rRBG?M0>x!kOrp^s8AC`<C(U4FaNp+jr&1&-Zwmren5qhOX-n0!L|8C7=x*1vtDiH~V+ro|AtUNwr
%m`71<8OQ-354kiDLGF{a>i^-HepN_K^YoKuKlJi-Vpatld)^z+Y27ui6_PRgclUr)D}>ijcs-%fRUPH$Fy~SW7U;SeKBQ@ls-~C
!Ip|+<fd0Sicf9BV_uy2@S`eEga=EDz?yQQOE%(r^!q5m4KK%RH0CeTSAclWM(_D$2gi0s;|l(luimR2fCqiq@mlXqR1e}fha~mX
EIOQ?>bc>@2%1Ng*8RLC`6OfZk$+^D4!>mY9S+!h<Re6B^qx}pw8(3rT5dqK+z3AoTgq6Q*n1{?-WoCGR;&x}LL~gG3+|W2;KJSu
e$bet<|~<*C0Q7oGyy}{l=SRNeRjQ1IwN?_{NSNO3?~rRWt4_Ynn)l}JC*a2i0V$~z=2gKAf3~_$Fh_3pofD_Ue$T`3+G*2<3<<a
l{GD&-xeW^0iHQ);sL;)8~FFRS-fa;jZqC3*ngYW5!Q_YIy#2j=B3k|c4YZIlnb{GF(#V9XzIs^7H7}!3Vf6<q7cYQZz2RR#Guz)
S}mtdZ@9<;y@Vrm5R?uFs(2lDhWTY_8H`(t-P-k-Rp?4eDWVGRxKgRPBJGKK0d>@#k`lm_zT0d|byk=QmE|MHniNo(<-=oPq^OGA
o8TnGy3X*IMXWngCC$@)NpWgE*^XB*99~kGddYUCo&v%)5w#NP0&BpK3GK@CK3nZbXju);h~SJEZF9%snw9|drVePeh=LGACrtlL
T}C_(H~C9()7Vs*BM@(uT%L0@x8n&tHUCdxI;TLJ2(NYx<2hIMVoq`*4aL0hmNAJmzpw^#b&F|EvpVryMa(pU%O^yHpO(F!(=!&c
3ZV4e-Q37ayDuMGw)57rG^Wob-_1>tdg441F?}j?sC!h<VgtPJP$np=ybgYfOz%-{^*=>25L~LgY^Y2V>JL8KlZ{r@A3!J*O-sZ6
$fTLW9iOZ_Vq5ESTjd~3VS`UpRVsLvE~@H1C7wb|51^h3HC}SQ%XW&-a&W9U0_mj3Plv`KMV~ILBGAAI$|gR5-oXqbiU~{G*wxy1
P!P&gk5dF)U}HE!z$nRMh%khS$iXbPc01;KI%>=c%7{T9$1k}H!`qL5sMH5VBA=26poh_&6FhS}o{Z%Mu+*HEC-`wJ319IkNdMdx
mhAE)TJK8V$BON`d@pp#N78MV;G+&lqG=?WMq{;=J6>uK7%wW9?-_a$%r3nUIh@>tmu9r&oWd26lWw#bBQ;}Gu2CPa*;T+@T<5&}
s0#08;ZFV~7lm`-YGA{Sd7+Fcy<^D9jVIztRpDlw#7<}*R6_Vu(M(_)6*Ix`BH6J>(vU+#E1m<+c&_3#Mmkgvt)EkI!z73sh~>zd
-5}Eu6gA?<#!tWo7<q<qzSuUT|CopLGNtS1Yj@G;zNP4+kv!vTl{qjn*8D}X3WLTnp$qyL^B+|ofLL62c7Quohh6EYarf=*z6cZ$
SpmWvE~9{>G!|~eNJ}qDB`O{`<_yLPk<G=kR848!g8s(^Wvn>4y;axFN%dWiN*7Gsjk#kVK5&tKE@v_=3qC3s_BAi^yqG*z+2ao%
@FdVNGs_mdQC@9vrVKMZiji+Ldn_PS%&-7avA&W4?(R6hBMt?G$j_z<0OU84wbm&<X0IfJU_<ml27O<80v-GzI6<FJN+MK92NP@e
y~W$kMD<#Fh~5sQv^zan1;8$Z$W-?IvP=N5Y7XhmFD@QA!eml{4EdpU3tZ`BcVo~Lyu~q;+buGBfGQ&>Vu%JJ;iyk-)<cbI>PatP
MGa%1Mk0{}<dYKj#N59miUxu(2N)XS6pi4)2)4yeWLzcwXvL)BM~8uCs2n*^H{^!`q@jC{N=Wa5i4}c)*ypdf@rCOzRwDnO0N4G0
(Fno9^c9z5u~PB(aD9pl$pY~RDw((!$>%J`7w|}~nNXkf%RuRgEE5!1JQJFbeh=JRQJL_Wq{~>Or357qvNT@Ow2MDXiGcijATIsD
KYVy$Ik}Sf!^BGTt34?W*0jk#^K8-cEiYysI#2zI3kIXg&()(*{jG~dz-6Y0VQS>iaC3+R`pyqH-&!mXe*YVQBp1No3s||FP5V;P
hRMx6Q#%H^>>arD<Yw+N#GA8Rm<w2)XhgqEyjOXU@e9J^a}s*jPi4mVm2rYk?&^;!vttS<g*(OY4xe5nF{L)YsAjS%V?KN~jW4W)
fp~xd7)FaERtr7x@)APvZd0oAWacrw$cUx7<L%S}CTZL#(=1k?cct30)_SU_;Q~f=J$jer$Htg$0)UYR5k&jGRUcAV$I;U|Z1`D}
M_^un8KZ32h?B<sB7r&a13{55@qy)k|K?|IoH5(MPkOLUk9AH($zeTa%ZQfbuz1<k17AWBhc1n9>CWo6L)P&c-Hc)*`XoyEMabbv
dma@D1$AwLv?$;uwdi1xKop>HCB2dgs}_yw_0(eGB7u3Y%KAL2o&;g77|oj{_p{8%%D3|V!N+g}C`F=~x{6dJkuf~oqUqmY4s%NZ
YGsDH+*91Jnz${m{GN)4ODK`Coem{b6y}}D&_?de8oVHS*5OGKAqus;XAJ|8pDp<#$6Ly2)WA~UK-QLRN?f&grgkZeh87pYD)gx=
yaRA3oj!u`>krX)MWUhl+BGs2w{5G?2@yZQs?yj-yt)em^@(G$&Xv(cKf%J%36`*>%j`at&Zz**ZOa1nfD);_nqggd5#DZvUwf(&
m!88b+w>ylMdmQ8HG{{HVRN_E?3Am(S+7^>LH%X`N@PRF)Y+6T@x|+96##6}L6kv@uu2C(Gd$=Nr8<&X*EGwQ6Jvg0^4=6&<WQGG
T@skDodU8bpv+)_Dk-mwrgLODXQyXft9#Nv?e=W@)H$)?&q=>)Ij2qY!Y5+;MC`vBf8MOZSF;=o&eF0DB)^HV@CVEe9F7NN_J;dW
=@v-+J4-WgW-=qL30nM0nMJkT8fQAKxb0YQ=Je=8HDdq?iz$sXeByMgq*Z@1NEvhO?tpGApWuHmmD=m3t$?PYwj!jXS!l)fk~JH7
0b?t@2JInHm2$UCz|njs^vDcF8nWY@1W1^R;;*C5V9YT$(qku@{kGLOSwEFk9HlJ!mC>)%&T)(!?NAH-EuV@7eBZGfYJLs$PMYMb
G_^Fl96+7IhiOjfE)2(QS!Z2#)&qVba@7WrdoIRxyUsc5cKcSrdWYeD7US*SN%ySZwe9W+JGXj{b8cIpfz;&`IN)S~@7#e^0IR+h
FDmJ8t;XPri7n!}O^hbq@oq919+j$_8O<2{bgc&|Z&_N&e8G=~|BR;mK2~+UqtC8hNvQFyeBPovg~YS6N9}Zi+nMrf4U+T>)d&1k
`?YoOJAU%(OZ9K~?T35U@(8Z2mZ5#AtF3*f3m>7i=GE(zzLb{$T$lYD55Q648*qXsC3P(G&`VX<haNy3a9B-q&-JhG2DWqHnLcjt
cWZzTsF(xxM3lPf^3w}|fG&Ibvl7OYtVrk8ZqAx*{Dumm3Ws;CjM|1?$psqpnSHJcebs?SY42*a(>^;rDa5&8jb;+dml-^Ff!{*H
iwALtPpEXZqGgfrJ=V8PT@cFjTD~goZtQ=U3=>w-P9)o?IifdI0c!biIQq)jdWjz~%XshjL}uAMkE?};8FDVFvEgWhtm_SzOFkO4
V8A)5tKxx}d^~{fQvt&wH;+c`C4TJA^IH0ZOn#|S+U;bChpnbzZzh@EYZdjXY5Z$aN~tJtI@T6?0TwA7O`~<eC|j(5a?(G4X?fB_
<&?9o?O12l$@w|!S?6a~-#Mvk&vLF(MB0k|UeA{E&+PNQjnmcq6^ssHhZUtMGAk#*-{|gXl6lJ@xLxtO1MsbUR(#7^IOL#0`DYSX
QAnEL4HfG2X{K*xp%!&t=AV6r>fl$7*da-mW)ux7BYj@jBvoL7Ml;<&X=PT>vN#D<C|n8gHKZcsz_)f*QH<ZL@k5AOuF8+S&^M|M
k3w=31AiAJ8wkkH@_hmEaBFiE<>7K=sQa09K;pU=!&^OO`2es2Nx-RQ&^Gk-rP&NMB7M4cHe0$;JexK5zew><J|RU*9sG=x^2Gkx
x1^LlS>=a5C?yGW@S{>V=fFp$iYQ)vtp$f2_^_1tbi+#@ml8bt{@u@`cb~_<{)5j-{qg_)2j36Pqy
'''

def checked(raw,pin):
    assert (len(raw),hashlib.sha256(raw).hexdigest())==pin

def main():
    assert len(sys.argv)==3
    mode=sys.argv[1];assert mode in ('sources','build','verify')
    out=Path(sys.argv[2]).resolve();out.mkdir(parents=True,exist_ok=True)
    raw=zlib.decompress(base64.b85decode(''.join(BLOB.split())))
    checked(raw,PAYLOAD_PIN);files=json.loads(raw);assert set(files)==set(SOURCE_PINS)
    for name,text in files.items():
        data=text.encode();checked(data,SOURCE_PINS[name]);p=out/name
        if p.exists():assert p.read_bytes()==data
        else:p.write_bytes(data)
    if mode!='sources':
        for name in ('two_vertex_root','two_vertex_algebra'):
            command=[sys.executable]+(['-S'] if name=='two_vertex_root' else [])
            report=out/(name+'.json')
            subprocess.run(command+[str(out/(name+'.py')),mode,str(report)],check=True)
            checked(report.read_bytes(),REPORT_PINS[name+'.json'])
    print('TWO_CANONICAL_ROOT_SELF_CONTAINED_RECOVERY_PASS',mode)
if __name__=='__main__':main()
```
