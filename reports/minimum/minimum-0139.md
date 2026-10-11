# minimum-0139

Historical AI scientific report · saved 2026-09-20 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# ALL_BODY_POLYHEDRAL_FREE_BOUNDARY_V1

## Result and exact remaining boundary

**The polyhedrality assumption can be removed from the local-maximum theorem.** In the full marked support-patch class of this assignment, every Hausdorff local maximum among arbitrary admissible convex bodies is a polytope. The proof below first gives a deliberately coarse bound of 162 extreme points without invoking the supplied polyhedral combinatorics. The supplied sixteen-vertex theorem then applies, giving at most sixteen true vertices.

**Global attainment is not proved here.** In particular, this is not yet an unconditional sixteen-vertex supremum reduction. What is resolved is the complete free-boundary alternative for an attained local maximum: smooth, ruled, developable, singular-continuous, and infinitely faceted nonpolyhedral maximizers are all excluded. The remaining global issue is attainment inside the stated class, including positive root area, rather than regularity or polyhedrality of an attained maximizer.

A precise consequence is proved at the end: a maximizing sequence that has a common bounded container and a Hausdorff limit with positive root area attains its supremum at a polytope with at most sixteen vertices. Neither of those compactness/noncollapse hypotheses is silently imposed on the unrestricted problem.

The argument uses actual three-dimensional convex competitors and the original uniformly filled volume integrals. It does not preserve the input centroid, volume, first moment, face lattice, or number of vertices. Those quantities are recomputed by exact integral formulas throughout.

## Input closure and evidence status

The complete supplied journal and all four supplied materials were read through EOF. Their mounted byte identities were checked:

- Journal: 263427 bytes, SHA-256 `729b1b35d09da4b6d0332aff7c695a46518c8436be776022d354f9307af9342d`. Its embedded working-memory hash identifies the inner memory, not this complete branch-wrapper file.
- `[internal-source-reference]`, foundational analytic proof: 14798 bytes, SHA-256 `8dc6ce8812298f59a61b404ccba7c09fef867bb8844a8952bf1cacc638bcc2b9`.
- `[internal-source-reference]`, sixteen-vertex extension: 14026 bytes, SHA-256 `00cf0ab29376360d8dd417d71fb8e87bab0d02fbb93bfce0937614e7fd106757`.
- `[internal-source-reference]`, authoritative exploratory source: 1030 bytes, SHA-256 `d164a50a0950ef359de36376c77838dcce6c81eeb658cd4252cbe362d1654b60`.
- `[internal-source-reference]`, ancillary correction: 1817 bytes, SHA-256 `f49c8c9723077de629921c049d6e09d2466072e6feb41a7738bd27b9cecc7823`.

The corrected 1030-byte source, not the longer illustrative fence, is authoritative. That enumeration is not used in this proof and was not claimed as a new computational replay. The correction expressly leaves the analytic theorem unchanged. :contentReference[oaicite:0]{index=0}

The supplied theorem is used only after polyhedrality has been established below. Its premise is local maximality against all nearby admissible convex bodies, not maximality in a fixed realization stratum. :contentReference[oaicite:1]{index=1}

This handoff contains a new analytic proof, not a numerical finding. No new coefficient array, computed body, solver output, or unavailable archive source is a dependency. The argument has not been proof-assistant formalized or independently audited by a second executor. The two particularly useful audit points are the angular-edge variation in Section 7 and the finite-extreme-point argument in Section 9.

## 1. Problem, notation, and an exact variation identity

Fix `0<b<1` and `c,d>0`. Put

    A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
    M={A,B,C,D}, T0=conv(M),
    ell=1+(d-1)x+(c-1)y+(b-1)z,
    n=(1+b+c)x+(1+b+d)y,
    W={x>=0, y>=0, ell>=0}.

An admissible body P is bounded, full-dimensional, and convex, with `T0 subset P subset W`, and its root `F0=P intersect {ell=0}` has positive two-dimensional area. Coordinate support patches may exceed the canonical triangles. These are exactly the supplied original-body definitions. :contentReference[oaicite:2]{index=2}

Write

    V=integral_P 1,
    E=integral_P ell,
    N=integral_P n,
    T(P)=N/(6VE),
    r=N/V, q=N/E,
    g=n-r-q ell.

Here E denotes the ell-integral, not an edge count. All of V,E,N,r,q are positive. Also

    integral_P g=-N,
    g(A)=-r-q<0,
    g(B)=-r-qb<0,
    g(B)-g(A)=q(1-b)>0.

For any admissible competitor P', let `Delta V`, `Delta E`, and `Delta N` be its actual changes. Cross multiplication gives the exact identity

    T(P')>T(P)
      iff Delta N-r Delta V-q Delta E
           > [N/(VE)] Delta V Delta E.                 (1)

The expression on the left is the signed integral of the frozen affine function g over the change of body. In particular, for an added or removed region of volume w in a common bounded container, the right side has magnitude `O(w^2)`. The added-region and removed-region forms agree with the supplied finite tests. :contentReference[oaicite:3]{index=3}

For centroid bookkeeping, write `J=integral_P p dp`, where p is the position vector. Every variation below has

    J'=J+Delta J,
    centroid(P')=(J+Delta J)/(V+Delta V).                (2)

No separate centroid constraint is introduced.

We use the following standard finite-dimensional convexity facts. A compact convex set is the convex hull of its extreme points. A convex-body boundary has finite surface area, is locally a Lipschitz graph, and has a unique supporting normal at almost every boundary point; the last assertion follows from Rademacher's theorem in those graph charts. Such regular boundary points are dense. The supporting halfspaces at regular boundary points determine the body. An elementary justification of this last fact is included in Section 3.

A facet always means a genuine positive-area maximal planar face, whether or not its outline is polygonal.

## 2. Extreme-point deletion without any polyhedral assumption

### Lemma 2.1: noncanonical extreme points have nonnegative g

At a Hausdorff local maximum, every extreme point `p notin M` satisfies `g(p)>=0`.

Suppose instead that `g(p)<0`. Choose a sufficiently small open ball `B(p,epsilon)` avoiding all four marks and on which `g<=-a<0`. Define the actual convex competitor

    P_epsilon=conv(P minus B(p,epsilon)).

The set being convex-hulled is compact. Because p is extreme and is absent from that set, p is not in its convex hull. Thus the deletion is proper. It removes a positive-volume region: a full-dimensional convex body has interior points arbitrarily close to any boundary point, whereas the new compact convex set has positive distance from p.

Every removed point lies in the chosen ball. The four marks remain. A fixed nondegenerate triangle in the relative interior of the root can also be chosen away from that ball and remains in the new root. Consequently the new body is admissible.

The bodies converge to P in Hausdorff distance. For example, a point in the removed ball can be joined to a fixed retained point; the first exit from the ball is retained and is at distance at most `2 epsilon`.

If w is the removed volume, its g-integral is at most `-a w`, while the right side of the removal version of (1) is `O(w^2)`. The deletion therefore strictly improves T for small epsilon, a contradiction.

This proves the lemma for exposed and nonexposed extreme points alike. No edge, tangent simplicial cone, or finite face lattice was used.

### Consequences

All root extreme points are noncanonical, because every canonical ell-value is positive. Hence

    g>=0 on F0.

On the root, `g=n-r`, and this affine function is nonconstant: the root plane has a nonzero z-normal component, whereas n has no z-component and has nonzero gradient. Positive root area therefore gives

    max_P g>0.                                         (3)

Together with `g(A)<0`, this means P straddles the plane `g=0`.

The endpoints of `P intersect {x=y=0}` are extreme points of P. On that axis,

    g=-r-q ell<0.

They must consequently be canonical. Containment of A and B now gives

    P intersect {x=y=0}=AB.                             (4)

These conclusions hold for arbitrary convex-body local maxima. At this stage the noncanonical inequality is only nonnegative; no unjustified extension of the polyhedral thin-edge equality argument has been made.

## 3. Every free regular support plane touches a negative mark

Call a boundary point regular when its outer unit normal is unique. Call it free when it lies strictly inside all three protected halfspaces.

### Lemma 3.1: localization of a small visible addition

Let p be a regular boundary point with normal u, and let

    F=P intersect {u dot x=h_P(u)}.

For `a_epsilon=p+epsilon u`, the visible boundary of P from `a_epsilon` approaches F as epsilon tends to zero.

Indeed, for any convergent sequence of visible contact points and associated supporting normals, the limiting supporting plane contains both p and the limiting contact point. Regularity at p forces its normal to be u, so that contact point belongs to F. Compactness makes this localization uniform.

The added region `conv(P,a_epsilon) minus P` is star-shaped about `a_epsilon`. Along each ray it runs from the apex to its first contact with P. Radial integration in dimension three gives, for any affine f,

    average_added f
      = f(a_epsilon)/4
        + (3/4) times a positive weighted average
                    of f at the first-contact points. (5)

The weights are proportional to the cubes of the ray lengths. Thus, if `g>=0` on F and `g(p)>0`, the mean g on the added region is bounded below by a positive constant for all sufficiently small epsilon. Equation (1) then gives a strict improvement. At a free point the apex remains in W, and the addition retains all marks and the entire root.

### Lemma 3.2: negative-mark support

Set

    M_-={X in M:g(X)<0}.

Every free regular supporting plane of a local maximum contains a point of `M_-`.

Suppose a free regular point p has a supporting face F containing no negative mark. Extreme points of F are extreme points of P. Lemma 2.1 and the absence of negative marks imply `g>=0` on F. Lemma 3.1 excludes `g(p)>0`; hence `g(p)=0`.

This conclusion holds in a whole relative boundary neighborhood. To see this, the supporting plane at p has a strictly positive slack at each of the finitely many negative marks. Uniqueness of the normal at p and upper semicontinuity of the normal correspondence imply that all supporting normals at sufficiently nearby boundary points have the same strictly positive mark slacks. The neighborhood also remains free. Every nearby regular boundary point therefore has g-value zero.

Regular points are dense, so the whole boundary neighborhood lies in the plane `g=0`. A planar open boundary patch of a full-dimensional convex body is supporting. This contradicts the fact, established in (3), that P has points on both sides of that plane.

### Exact finite-cone representation

For `X in M_-`, define the translated closed tangent cone

    C_X = X + closure(cone(P-X)).

Equivalently, C_X is the intersection of all supporting halfspaces of P whose boundary contains X. Then

    P = W intersect intersection_{X in M_-} C_X.        (6)

The forward inclusion is immediate. For the reverse inclusion, every regular supporting halfspace of P is present: at a protected regular point it is a protected halfspace, and at a free regular point Lemma 3.2 assigns it to a negative mark.

For completeness, these regular supports determine P. Choose an interior ball of radius rho centered at o. For an exterior point q, let z be the intersection of the ray oq with the boundary. Every unit supporting normal v at z satisfies `v dot (z-o)>=rho`, and hence strictly separates q from P. Approximate z by regular boundary points and take a convergent subsequence of their normals. The strict separation persists. Thus some retained regular support excludes q.

Representation (6) has at most four marked apex cones, but the cones are not yet asserted polyhedral.

It also follows immediately that no facet of P is constant at a positive g-value. An unprotected facet contains a negative mark. The coordinate planes are not constant-g planes because they contain A and B with different g-values; the root plane is nonconstant as already noted.

## 4. Exact cone variations and a nonsmooth generator balance

The next construction is the body-level replacement for a smooth-point Euler equation.

Fix a negative mark X for which the direction cone `C_X-X` is pointed. Choose a linear functional lambda strictly positive on that cone away from zero, and form its compact planar section

    D_X={v in C_X-X:lambda(v)=1}.

Choose a closed cube H with P strictly inside its interior and put

    K_X=H intersect W intersect intersection_{Z in M_-, Z!=X} C_Z.

Then `P=K_X intersect C_X`. The cube only makes every competitor below bounded; none of its planes is active on P.

For a direction v define

    R_X(v)=max{t>=0:X+t v in K_X}.

Whenever some positive point on this ray is interior to K_X, R_X is positive and continuous in a neighborhood of v. One proof uses the gauge of the convex set `K_X-X`: it is finite on an open neighborhood of such a direction, hence continuous there, and equals `1/R_X`. Boundedness of K_X gives a uniform upper bound for R_X on the angular chart.

Choose affine coordinates on `lambda(v)=1`, so `v=v0+s e1+t e2`. The original Euclidean volume element under `p=X+rho v` is

    J0 rho^2 d rho ds dt,
    J0=abs(det(v0,e1,e2))>0.

For any angular region U and any affine function f, its actual cone-sector integral is therefore

    J0 integral_U [ f(X) R_X(v)^3/3
                 + (gradient f dot v) R_X(v)^4/4 ] dv. (7)

In particular,

    sector volume = J0 integral_U R_X(v)^3/3 dv,
    sector first moment
      = J0 integral_U [X R_X(v)^3/3+v R_X(v)^4/4] dv.    (8)

Equations (7) and (8) apply to f=ell, f=n, and each coordinate. They are integrals over the original body, not uniform integrals over a projectively transformed image.

Call v a good angular point for X if:

1. v is regular in the planar convex set D_X and its supporting line exposes only v;
2. `R_P(v)>0`;
3. its ray contains no canonical mark other than X.

Let Y be the far endpoint of that ray in P.

### Lemma 4.1: the other constraints are inactive along the open generator

At a good angular point, every point of the open segment XY is interior to K_X. Consequently `R_X(v)=R_P(v)` and R_X is continuous near v.

Suppose a factor defining K_X were active at an interior point of XY. A supporting plane of that factor also supports P there and contains X and Y. Every such plane supports the tangent cone at X. Regularity of the angular point gives a unique such cone normal, whose contact with the cone is exactly the ray XY.

If the active factor were another marked cone C_Z, the plane would contain Z as well. This would put another canonical mark on that exposed ray, contrary to condition 3. A protected plane cannot be active either: it would contain X, and its genuine positive-area P-facet would give a two-dimensional contact cone, not an exposed ray. The cube is strictly inactive on P.

### Lemma 4.2: exact generator balance

At every good angular point,

    g(Y)=-g(X)/3>0.                                    (9)

Cut a small cap from D_X by moving its exposing line inward. The cap shrinks to v. All other canonical directions have a strict slack, so they remain. A fixed nondegenerate root triangle can be chosen with directions different from v and also remains. Intersecting the new cone with the fixed K_X gives an admissible convex deletion converging to P.

For the opposite comparison, take the convex hull of D_X with `v+epsilon eta`, where eta is the outer planar normal, and intersect its cone with K_X. This is an admissible addition. Since v is both regular and exposed, the added angular region also shrinks to v. This assertion follows directly by separation: a limiting separating normal supports D_X at v; regularity identifies the normal, and exposedness identifies its entire contact face as the singleton v.

Formula (7), continuity of R_X, and positivity of the sector-volume density show that the mean g of either the removed or added three-dimensional region tends to

    g(X)+(3/4)(g(Y)-g(X))=(g(X)+3g(Y))/4.               (10)

The removed-region inequality requires this limit to be nonnegative. The added-region inequality requires it to be nonpositive. Otherwise the linear-in-volume term beats the quadratic remainder in (1). This proves (9).

The corresponding mean position tends to `(X+3Y)/4`. The actual centroid change is then given by (2) and (8), not set to zero.

No curvature, second derivative, or power-law cap asymptotic is assumed in this argument. It applies to singular planar cone outlines as well as smooth ones.

## 5. Only countably many good generators can survive

This section rules out a hidden singular-continuous free surface.

We first record elementary planar countability facts. A compact planar convex body has at most countably many maximal nondegenerate boundary segments, since their relative interiors are disjoint arcs of positive length. It has at most countably many nonregular boundary points, since each such point has a normal interval of positive angular length and those interval interiors are disjoint. A regular boundary point that is not exposed either lies on a boundary segment or is an endpoint of one. Consequently its boundary is the union of its regular exposed points, countably many segments, and countably many additional points.

Fix X and write `h_X=-g(X)/3`. A good endpoint Y is an extreme point of P: the supporting face supplied by its exposed cone ray is exactly `[X,Y]`. All such Y lie in the fixed plane

    H_X={g=h_X}.

Because Y is the terminal point in K_X, at least one factor defining K_X is active there.

A protected factor accounts for at most two such extreme points on each of its planes: its intersection with H_X is a line, since g is nonconstant on every protected plane. Three collinear points cannot all be extreme.

A nonpointed marked cone also accounts for only finitely many such endpoints. A full-dimensional nonpointed cone in dimension three is the inverse image of a cone of dimension at most two after quotienting by its lineality. It therefore has at most two bounding planes. Each contains its negative apex Z and cannot be H_X; its intersection with H_X is a line.

It remains to consider a pointed cone C_Z with `Z!=X`. Project Y radially from Z to the compact section D_Z. If the projected point lies on one of D_Z's countably many boundary segments, Y lies on the corresponding cone-face plane. That plane contains Z, so it is not H_X, and it contributes at most two extreme points. Nonregular angular points and segment endpoints contribute at most countably many rays. Rays through another canonical mark contribute only finitely many more. Each such ray meets H_X in at most one point, because `g(Z)<0<h_X`.

All remaining Y are good endpoints for Z as well. Extremality of Y ensures that it is the terminal point of the ray from Z; otherwise it would be interior to a segment in P. Applying (9) at Z gives

    g(X)=g(Z),  h_X=h_Z.                               (11)

These double-good endpoints are also countable. Here is the geometric reason, including the potentially singular case.

Let `P_h=P intersect {g=h_X}`. If it has dimension at most one, it contains at most two extreme points of P. Otherwise it is a genuine planar convex body. Let u_X and u_Z be normals exposing the two generator faces `[X,Y]` and `[Z,Y]`. Then

    u_X dot (X-Y)=0,  u_X dot (Z-Y)<0,
    u_Z dot (Z-Y)=0,  u_Z dot (X-Y)<0.                  (12)

Their restrictions to the direction plane `ker(gradient g)` are nonzero. They cannot be positive multiples. Indeed, if

    u_Z=a u_X+t gradient g,  a>0,

evaluation at X-Y and (11) imply `t>0`; evaluation at Z-Y then makes the right side strictly negative, contradicting its zero left side. They cannot be negative multiples either, because the two supporting inequalities would confine P_h to a line. Thus they define two different supporting lines of P_h at Y.

Therefore every double-good Y is a nonregular point of the planar body P_h. There are at most countably many such points.

We have exhausted the finitely many possible active factors. It follows that, for each X, its good endpoints and good generators form a countable set.

## 6. The entire surface-area measure is atomic

### Proposition 6.1

At a local maximum, almost every boundary point belongs to a facet. Equivalently, the surface-area measure of P is purely atomic, supported on its countably many facet normals.

Consider a regular free boundary point p and its supporting face F. By Lemma 3.2, F contains a negative canonical mark.

If F is two-dimensional, p belongs to a facet. If F is a singleton, it is a canonical point. If F is one-dimensional and contains two canonical marks, it lies on one of the six fixed lines through canonical pairs; these sets have zero surface area.

In the remaining case F is one-dimensional and contains exactly one canonical mark X. Away from X, every factor of K_X is inactive at p: an active marked factor would put a second mark on the unique supporting plane, and a protected factor is excluded because p is free. Thus locally P agrees with C_X.

The contact face of this cone must be one-dimensional. A two-dimensional cone contact, intersected with the neighborhood in K_X, would give a genuine facet of P. Regularity excludes a one-dimensional lineality contact of a nonpointed cone. Hence the cone is pointed and the contact is a regular exposed ray. Its open segment is one of the good generators counted in Section 5.

The remaining regular nonfacet points consequently lie on countably many line segments, together with finitely many canonical-pair lines. They have zero two-dimensional measure. Nonregular boundary points already have zero surface area by the Lipschitz-graph fact stated in Section 1. The three protected faces are themselves facets.

Distinct facet interiors are disjoint and have positive area, so there are at most countably many facets. Writing their areas and normals as `A_i,u_i`, the result is the exact measure identity

    S_P=sum_i A_i delta_{u_i}.                         (13)

In particular the union of the facets is dense in the boundary: every nonempty relative boundary neighborhood has positive surface area.

Atomicity alone would not imply a finite polytope. The next two sections exclude precisely that remaining infinite-facet possibility.

## 7. A complete angular-edge variation lemma

The required whole-facet stationarity can be obtained without assuming that a facet normal is isolated from other normals. This avoids the invalid operation of merely deleting one inequality from an infinite supporting-halfspace representation.

### Planar variation lemma

Let D be a compact planar convex body with a genuine exposed edge E. Put coordinates `(s,t)` so

    E=[0,1] times {0},  D subset {t<=0}.

Let w be bounded near D and continuous in a neighborhood of every point in the relative interior of E. Let L(s) be affine and strictly positive on `[0,1]`.

For the inward cut

    D_epsilon^-=D intersect {t<=-epsilon L(s)},

Fubini and rescaling of t give

    (1/epsilon) integral_{D minus D_epsilon^-} w
      -> integral_0^1 w(s,0)L(s) ds.                   (14)

The removed set is in a strip of thickness O(epsilon), and its horizontal projection outside `[0,1]` has length tending to zero. On every compact subinterval of `(0,1)`, the original body contains a fixed inward strip, so the claimed rescaled thickness is exact for small epsilon. Endpoint contributions are o(epsilon).

For the outward comparison, fix `0<delta<1/2` and take

    D_epsilon^+=conv(D,
       {(s,epsilon L(s)):delta<=s<=1-delta}).

Define the nonnegative piecewise-affine function psi_delta to be zero at 0 and 1, equal to L on `[delta,1-delta]`, and linear on the two remaining intervals. Then

    (1/epsilon) integral_{D_epsilon^+ minus D} w
      -> integral_0^1 w(s,0) psi_delta(s) ds.           (15)

Here is an endpoint estimate that makes (15) valid even when other edges accumulate at an endpoint of E. If a supporting normal `(xi,eta)` of D sees either new endpoint, comparison with the whole old edge gives

    eta>0,  delta |xi| <= epsilon max_E(L) eta.

Thus its slope is O(epsilon). Any visible contact outside E converges to an endpoint of E. The supporting inequality at that old endpoint further gives

    |contact height|
       <= O(epsilon) times its horizontal distance from E
       =o(epsilon).

The newly added region outside the vertical strip over E therefore has area o(epsilon). Inside the strip, its rescaled upper boundary converges to psi_delta, and is uniformly bounded by `max_E L`. Dominated convergence proves (15), including bounded weights that may fail to be continuous at the two endpoints.

Finally `psi_delta -> L` almost everywhere and boundedly as delta decreases to zero.

### Application to a canonical cone

Suppose F is an unprotected facet containing exactly one canonical mark X. Lemma 3.2 gives `g(X)<0`. Lemma 2.1 shows that X is an extreme point of F and P, and is isolated among the extreme points of P: other noncanonical extremes have nonnegative g, and the remaining marks are finite.

Let K be the compact convex hull of the closure of all other extreme points. Extremality and isolation give `X notin K`, and strict separation makes the cone at X pointed. Moreover, its contact with the plane of F is exactly `cone(F-X)`. Thus F corresponds to a genuine exposed edge E of D_X.

For angular directions in the relative interior of E, points on the open rays in F are relative-interior facet points. All other factors of K_X are inactive there, because an active factor would put another mark on F or make F protected. Hence R_X is continuous in a neighborhood of every such direction.

Apply (14) and (15) to the bounded angular weight

    W_g(v)=g(X)R_X(v)^3/3
             +(gradient g dot v)R_X(v)^4/4.            (16)

These angular changes define actual competitors by intersecting the changed cone with the fixed K_X. Every other canonical direction has strict slack at E, so it is retained for sufficiently small epsilon. A fixed nondegenerate root triangle with strict slack at the plane of F is retained by the inward cuts. Outward changes contain P. Boundedness is supplied by H. The competitors converge to P in Hausdorff distance.

Their volume and ell-integral changes are O(epsilon), by (7). The quadratic term in (1) is consequently O(epsilon squared). Local maximality and (14) imply

    integral_E W_g L >=0.

Local maximality and (15) imply `integral_E W_g psi_delta<=0`. Passing delta to zero gives the reverse inequality. Therefore

    integral_E W_g L=0                                (17)

for every strictly positive affine L. By linearity it holds for every affine L on E.

To interpret this on F, parametrize it by `p=X+rho v(s)`. Its area element is a positive constant times `rho d rho ds`. Any affine function A_F on the facet plane that vanishes at X has the form

    A_F(X+rho v(s))=rho L(s),

where L is affine on E. Equation (17) is therefore precisely

    integral_F g A_F=0
      for every affine A_F with A_F(X)=0.              (18)

In particular,

    integral_F g(g-g(X))=0.                            (19)

This establishes the needed whole-facet first variation for an arbitrary convex body, including a facet with a nonpolygonal outline or accumulating neighboring normals. It does not assume a two-sided fixed-lattice tilt exists.

## 8. Every ordinary facet is a rigid triangle

We also need the facet addition inequality for an arbitrary convex body.

Choose p in the relative interior of an unprotected facet F, with outer normal u, and add `p+epsilon u`. The contribution with visible base in F is exactly the usual pyramid contribution. All other visible boundary approaches F, and its area outside F tends to zero. Its visible height is at most epsilon because p belongs to P.

More explicitly, radial parametrization from an exterior apex a gives

    added volume
      =(1/3) integral_visible (a-x) dot nu(x) dA(x),

    integral_added f
      =(1/12) integral_visible [(a-x) dot nu(x)]
                                      [f(a)+3f(x)] dA(x)

for affine f. These follow by integrating the radial parameter squared from zero to one. The extra visible base outside F contributes o(epsilon), whereas F contributes `epsilon area(F)/3` to volume. Equation (1) therefore gives

    g(p)+3 average_F g<=0.

Approaching a maximizing point of g on F through its relative interior proves

    max_F g+3 average_F g<=0.                          (20)

Now let F contain exactly one canonical mark X. Put `a=-g(X)>0` and `f=g/a`, so `f(X)=-1`. Every other extreme point of F has nonnegative f. As in Section 7, F is the convex hull of X and a compact set of points with nonnegative f, strictly separated from X.

Use polar coordinates in the plane of F centered at X. The angular interval is a sector of angle less than pi. Let R(theta) be the far radial endpoint and let

    u(theta)=f(X+R(theta)e_theta)>=0,
    M=max_F f,
    dmu=R(theta)^2 dtheta/(2 area(F)).

The measure mu is a probability measure, and `0<=u<=M`. Direct one-dimensional integration along each radial segment gives

    average_F f=(2 E_mu[u]-1)/3,
    average_F f(f+1)=(3 E_mu[u^2]+2 E_mu[u]-1)/6.

Equation (19) and inequality (20) become

    3 E[u^2]+2 E[u]=1,
    M+2 E[u]-1<=0.                                    (21)

First, `1<=3M^2+2M`, so `M>=1/3`. On the other hand, `u^2<=M u` gives

    1 <= (3M+2)E[u]
      <= (3M+2)(1-M)/2
       = 1+(M-3M^2)/2.

The last expression is less than one when `M>1/3`. Therefore `M=1/3`. Equality then forces `u=1/3` almost everywhere.

The far radial boundary thus lies on the single affine line `f=1/3` almost everywhere. The radial domain is the triangle bounded by that line and the two extreme rays from X, up to a null set. Two full-dimensional compact convex planar sets that agree almost everywhere agree exactly. Hence F is that triangle.

We have proved, without assuming P polyhedral,

    F=[X,v,w],
    g(v)=g(w)=-g(X)/3>0.                               (22)

The two other vertices are genuine noncanonical extreme points. This is the full arbitrary-body extension of ordinary-facet rigidity, not an application of the old polyhedral lemma to approximants.

## 9. Infinite facet accumulation is impossible

Let S be the collection consisting of the root and every facet containing at least two canonical marks. The coordinate facets belong to S. Write s for its cardinality.

### Finitely many special facets

Two distinct points of a convex three-body can belong to at most two distinct genuine facets. To verify this beyond polytopes, intersect by a plane transverse to their line through an interior point of their segment. The intersection is a full-dimensional planar convex set. Each genuine facet containing the segment supplies a nondegenerate straight boundary segment through the intersection point. A planar convex boundary has at most two such distinct segments there.

The canonical-pair incidence count therefore remains valid: AB already occurs in both coordinate facets; each of AC,BC,AD,BD can supply at most one additional facet, and CD at most two. Adding the root gives

    3<=s<=9.                                          (23)

Every remaining facet is ordinary and satisfies (22).

Let

    L={-g(X)/3:X in M_-},  l=|L|<=4,
    H_h={g=h},
    B_X=conv({X} union (P intersect H_{-g(X)/3})).

The notation B_X in this section is a compact convex set, not the canonical point B. Every ordinary facet with mark X lies in B_X. Since there are only finitely many negative marks,

    closure(union of ordinary facets)
       subset union_{X in M_-} B_X.                    (24)

If an extreme point p of P lies in B_X, then either `p=X` or `g(p)=-g(X)/3`. This follows immediately from extremality applied to the defining convex hull.

### Extreme points away from the special facets

Let p be a noncanonical extreme point not lying on any special facet. Density of the facets, together with the closedness of the finite union of special facets, places p in the left side of (24). Thus `g(p)=h` for some `h in L`.

For every X with a different level, p does not belong to the compact set B_X. Choose a small ball around p avoiding all those compact sets and all special facets. Every facet meeting this ball is ordinary with the same level h, and hence all its points have g-value at most h. Facet density gives

    g<=h on the boundary of P in this ball.            (25)

The following elementary observation is useful here. If an extreme boundary point p has `g(p)=h` and satisfies (25), then h is the global maximum of g on P. Otherwise a segment from p to a point with larger g enters the open half-ball `{g>h}`. That half-ball contains no boundary point of P. It is connected, so its nonempty intersection with the interior of P is both open and closed in the half-ball; the entire half-ball lies in P. Its closure contains a planar disk through p in `g=h`, contradicting extremality of p.

Consequently every noncanonical extreme point outside the special facets lies in the exposed maximum face of g. The maximum is positive by (3). This face cannot be a facet, by the conclusion following (6). It has dimension at most one and therefore at most two extreme points.

### Extreme points on special facets

A noncanonical extreme point on a special facet that belongs to the closure of the ordinary facets has g-value in L, by (24). No special facet is constant at a positive g-level. Its intersection with any H_h, `h in L`, is therefore a line or is empty, and contains at most two extreme points of P. This accounts for at most

    2 s l                                               (26)

points.

For the remaining extreme points, form the finite polyhedron

    Q=intersection of the s special supporting halfspaces.

Let p be an extreme point of P outside the closure of the ordinary facets. In a sufficiently small boundary neighborhood of p, facet density implies that the boundary consists entirely of special facets. P and Q agree locally there.

Here is a direct justification of that last assertion. Choose a nearby interior point of P. A segment from it to any sufficiently nearby point of the interior of Q remains strictly inside all special halfspaces. If that endpoint were outside P, the segment would cross the local boundary of P at a point on a special facet, a contradiction. Taking closures gives local equality with Q.

It follows that p is a vertex of Q. Otherwise a small nontrivial segment through p in Q would also belong to P. A full-dimensional polyhedron described by s planes has at most `binomial(s,3)` vertices, since every vertex has three linearly independent active planes. This elementary bound works whether Q is bounded or unbounded.

Combining the four canonical marks, the at most two exceptional maximum-face points, (26), and the vertices of Q gives

    number of extreme points of P
       <=4+2+2sl+binomial(s,3)
       <=4+2+72+84
       =162.                                           (27)

Thus P has finitely many extreme points and is a polytope.

This finishes the arbitrary-convex-body polyhedrality proof. Notice that the supplied sixteen-vertex theorem has not been used to obtain (27).

### Applying the supplied sharp local count

P is now known to be polyhedral, and its local maximality is still against the entire original marked class. The precise hypotheses of `POLYHEDRAL_TRACE_SKELETON_16_V1` are therefore satisfied. Its conclusion gives

    number of true vertices of P<=16.                   (28)

The inherited theorem and its stronger special-incidence formula are available in the supplied exact source. :contentReference[oaicite:4]{index=4}

Accordingly, (28) is no longer conditional on an a priori polyhedrality assumption. It remains conditional on P actually being a local maximum in the admissible class.

## 10. Global attainment: a precise corollary and the unresolved part

### Attainment corollary

Fix b,c,d as above. Let P_j be a maximizing sequence for the unrestricted marked problem. Suppose all P_j lie in one bounded container and a subsequence converges in Hausdorff distance to P with positive root area. Then P is an admissible global maximizer and has at most sixteen true vertices.

Indeed, containment of T0 and the protected halfspaces passes to the limit. The positive root-area hypothesis supplies the remaining admissibility condition. Characteristic functions of uniformly bounded full-dimensional convex bodies converge almost everywhere under Hausdorff convergence, since their boundaries have volume zero. Dominated convergence therefore gives convergence of V,E,N and J. The fixed tetrahedron gives positive lower bounds for V and E, so T is continuous. The limiting body attains the supremum, hence is a local maximum, and (28) applies.

A uniform lower bound on the root areas would suffice for root noncollapse. The root sections themselves have a planar Hausdorff-convergent subsequence in the common container; their limit is contained in the limiting root, and planar area is continuous for compact convex sets. This is a sufficient hypothesis, not a proved property of unrestricted maximizing sequences.

### What is still not established

No proof here supplies a common bounded container for every maximizing sequence at every fixed endpoint triple, or proves that a maximizing sequence cannot lose root area. The class in the assignment is open at zero root area. A compactified maximum on a collapsed-root boundary is not an admissible maximum to which this theorem may automatically be applied.

There is also no finite monotone improvement algorithm for an arbitrary input body. The cap, cone, and angular-edge variations are used as contradictions at a genuine local maximum; their succession is not claimed to terminate for a nonstationary input.

Thus the exact remaining global bridge is:

    prove attainment with positive root area
    in the original fixed-parameter marked class,

or establish a separate valid treatment of every maximizing boundary escape. Once that bridge is supplied, the polyhedral-maximizer question is resolved by this handoff, with the existing bound of sixteen. The old warning about applying the theorem to arbitrary polytope approximants remains valid. :contentReference[oaicite:5]{index=5}

## 11. What was tried, reusable mechanisms, and continuation

The initial route was to analyze smooth conical/developable patches generated by the mandatory marks. That suggested the endpoint balance `g(Y)=-g(X)/3`, but smooth stationarity alone would have left singular curvature and infinite facet accumulation unresolved.

The useful replacement was to work with the exact tangent-cone envelope (6), hold all other cone constraints fixed, and integrate radial sectors with their actual `rho^2` Jacobian. Angular deletion and angular convex-hull addition then prove the same balance without any curvature hypothesis. A planar countability argument removes non-atomic boundary area. The angular-edge lemma subsequently supplies whole-facet stationarity even when neighboring normals accumulate; this is what permits ordinary-facet rigidity to extend to arbitrary bodies. Finally, compact level-cones and extremality replace finite vertex-link arguments and eliminate an infinite collection of facets.

The planar polygonality literature was checked as an alternative route. Its standard sufficient theorem uses a strong concavity condition in an angular derivative variable and separately treats corner accumulation at active constraints. Those hypotheses were not established for the present radial weights, so that theorem was not imported. The elementary angular-edge argument above is independent of it. :contentReference[oaicite:6]{index=6}

The most useful continuation is now attainment/noncollapse, using the original integrals and the positive-root condition explicitly. There is no remaining need to assume regularity of an attained maximizing boundary or to classify smooth ruled candidates first. The exact variation formulas (7), (8), and the angular-edge limits (14), (15) are also reusable for that continuation.

No universal numerical trace bound, `T<51/25` theorem, mechanical exclusion, attaining 110 body, or registry change follows merely from this structure theorem. The accepted mechanical interval remains `34<=C_min<=622`. :contentReference[oaicite:7]{index=7}
