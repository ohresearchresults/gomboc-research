# minimum-0150

AI research report · 2026-09-21 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# ONE_ZERO_COCONVEX_SECTION_SYNCHRONIZATION_AND_TWO_NORMAL_REDUCTION_V1

## 1. Result, and the precise limit of the result

The unrestricted one-zero trace problem is not closed. This handoff gives a new continuous value sector, an actual-body reduction with no aspect restriction inside a larger geometric class, and two exact physical countercontrols to extending the replacement without its hypotheses.

The geometric class is defined intrinsically: every ell-section is contained below the chord joining its two outer coordinate-axis intercepts, and contains that whole chord. The lower boundary can have arbitrary nonparallel edges, continuously changing intercept ratios, curved pieces, and arbitrarily many positive-ell auxiliary vertices. Three-dimensional convexity, rather than a normalization, forces the OUTER chord aspect to be constant. No proportionality of the lower boundary is assumed.

For this entire class, define h=1+b and let U(w) be the outer y-intercept at height w=ell. Put

    sigma = max_{0<=w<=1} (h+w)U(w)/(h U(0)) >= 1,
    R(sigma) = 1 + (sigma-1)/(3(sigma+1)).

Then

    T(P) <= Cstar R(sigma).

Consequently the WHOLE continuous sector sigma<=103/100 satisfies T<51/25. There is also a directly checkable alternative using the original outer aspect kappa:

    eta = max(h kappa,h+d)/min(h kappa,h+d),
    T(P) < Cstar R(eta).

Thus eta<=103/100 is another complete excluded sector. Neither condition is asserted automatic. The value premise is precisely the supplied parent's homothetic-shell theorem, not an extension of that theorem by analogy. The parent explicitly leaves changing section geometry outside its scope.

For ALL aspects in the intrinsic chord class, there is a trace-nondecreasing sequence of genuine body operations ending at

    0<=w<=1, x,y>=0,
    x/kappa+y <= U(w),
    h x+(h+d)y+(m/b)w >= m,                         (NF)

where U is one actual concave profile, 0<b<1, 0<=d<=1, U(0)=1, kappa U(d)=1, and

    (h+w)U(w) <= (h+d)U(d) for every w,
    h kappa <= h+d, 0<=m<h+d.

The lower surface in (NF) is ONE plane, not a freely fitted volume law. All lower positive-ell curvature has been eliminated. The upper and lower section boundaries generally have DIFFERENT normals. The upper-profile optimization in this genuine two-normal class remains open.

The new proper control has T approximately 2.02680616 and genuine maximal ABC/ABD. Its sectionwise area-preserving, n-aligned triangular-band replacement deletes B and every other point of the common edge below A. Thus preserving every ell-sectional area does not, by itself, preserve the canonical problem. A second actual control shows that the same proposed band can fail three-dimensional convexity altogether.

No claim is made about the entire thirteen-vertex extremal layer, the full max ell>ell(A) sector, E17 exclusion, or an attaining 110 body. The accepted minimum interval is unchanged.

## 2. Source authority and verification status

The complete supplied journal, including the whole literal parent, was read through EOF. No earlier context or source file was assumed present. The supplied journal is 295465 bytes, SHA-256 f4e4c33d45bab242c3119a02e45693646cf4479f53c014f225ff80d4c9254287.

The parent identity was authenticated, not merely copied from the header. Extracting its Markdown from the displayed title through EOF, appending one final LF, and serializing

    {"version":2,"result_markdown":parent_markdown}

with ensure_ascii=False and separators=(',',':') gives exactly 36874 bytes and SHA-256

    80e36a50ac09768d59f513ea33b5340c3a3bad4d301fc4bc083d7a868a162cd9.

This matches minimum-0147. There is no payload/journal identity conflict. The parent itself distinguishes its accepted analytic theorem from an unexecuted old control receipt; that distinction has not been changed.

The sole inherited value theorem needed here is

    Cstar = max_{0<b<1,0<rho<1}
      2(1-b^2)(1-b rho^3)/[(1-b rho^2)(1-b^2 rho^2)] < 203/100,

together with the parent's whole homothetic-shell domination. Its older two-anchor optimizer certificate is not separately attached, and no replay of that unavailable certificate is claimed. This is an explicitly inherited premise.

The five new exact physical audits below were actually executed twice, in separate directories, with identical report bytes. Their source has no external input or parent-code dependency. The continuous proofs below are analytic; they are not proof-assistant formalizations.

## 3. Coordinates, actual moments, and the intrinsic chord hypothesis

Normalize a=1, write alpha=1-b, h=1+b, and retain

    ell=1+(d-1)x-y-alpha z,
    n=h x+(h+d)y,
    A=0, B=e3, C=e2, D=e1,
    V=int_P 1, X=int_P x, Y=int_P y, Z=int_P z,
    E=int_P ell, N=int_P n, T=N/(6VE).

The present geometric theorem assumes max_P ell=1. Hence 0<d<=1. This is a genuine restriction, not a rescaling of an arbitrary max-ell body.

Use the invertible affine coordinates (x,y,w), w=ell. Their inverse is

    z=[1+(d-1)x-y-w]/alpha.

Let K be the image of P. Its marked points are (0,0,1), (0,0,b), (0,1,0), and (1,0,d). All integrals refer to the uniform volume of this one body and its inverse affine image, as in the parent.

For each interior height w, suppose K_w has positive outer axis intercepts a_x(w), a_y(w), contains their joining segment, and is contained in

    x,y>=0, x/a_x(w)+y/a_y(w)<=1.                  (CH)

This does not say that K_w is a triangular shell. Its lower boundary can be any convex boundary compatible with the common K.

### Outer-aspect rigidity

The ratio a_x(w)/a_y(w) is constant.

Indeed a_x,a_y are positive concave functions, hence locally Lipschitz. For each fixed positive p,q, convexity of K implies that

    H_pq(w)=max_{K_w}(p x+q y)

is concave. By (CH), H_pq=max(p a_x,q a_y). At a height where both intercepts are differentiable, choose p=1/a_x(w), q=1/a_y(w). The left derivative of this maximum is the smaller of a_x'/a_x and a_y'/a_y; the right derivative is the larger. Concavity forces equality. Thus log a_x-log a_y has zero derivative almost everywhere and is constant on every compact interior interval. Endpoint continuity follows from compactness and convexity of the axis sections.

Write a_x=kappa U, a_y=U, with kappa>0 constant and U concave. The result concerns arbitrary LOWER geometry with this intrinsically forced outer aspect; it does not assert that general convex sections have an axis-bounding chord.

Set xi=x/kappa, eta=y, s=xi+eta. In these coordinates every section is a convex subset S_w of the triangle s<=U(w), containing its entire top edge.

## 4. The coupled covolume identity: one convex body, all heights

Let C_+=R_+^2 and form the actual upward closure

    Bcal=K+(C_+ x {0}).

In the (xi,eta) coordinates, each section satisfies

    S_w=(Bcal_w) intersect {xi,eta>=0, xi+eta<=U(w)}.

To prove this equality, write a point of the right side as p+c, p in S_w and c>=0. Continue the ray from p through p+c until it reaches s=U. Its endpoint belongs to the full top edge of S_w, so convexity puts p+c in S_w.

The missing set D_w=C_+\Bcal_w is bounded and lies inside s<=U. For theta in [0,1], let r(theta,w) be the radial threshold on the ray (xi,eta)=t(theta,1-theta). Then

    0<=r(theta,w)<=U(w),
    D_w={0<=t<r(theta,w)},
    area(D_w)=1/2 int_0^1 r(theta,w)^2 dtheta.

For EACH theta, r(theta,w) is convex in w: it is the lower boundary of the intersection of the SAME convex Bcal with the corresponding ray-height plane. Consequently

    L(w) = [int_0^1 r(theta,w)^2 dtheta]^(1/2)

is convex. This follows directly from pointwise convexity, monotonicity of the L2 norm for nonnegative functions, and its triangle inequality. In particular L is not being postulated as a free area profile.

The body

    S_w^rad={xi,eta>=0, L(w)<=xi+eta<=U(w)}          (RAD)

is therefore genuinely convex in three dimensions. It has exactly the same area at EVERY height as S_w. Thus the whole w-distribution, V, E, every integral of a function of w, and root area are preserved before re-marking.

Moreover

    int_{S_w} s <= int_{S_w^rad} s,

because

    int_{D_w} s = (1/3) int r^3
       >= (1/3)(int r^2)^(3/2) = L^3/3.

Equality requires the missing radial threshold to be constant almost everywhere at that height. This is the actual geometric reason a simultaneous replacement works here.

The underlying covolume convexity belongs to the established coconvex/reversed Brunn-Minkowski framework. The argument above is self-contained; no novelty is claimed for that standalone inequality. The new use here is the synchronized trace replacement with the canonical endpoint checks.

## 5. A whole value sector, not merely a profile relaxation

Put p=h kappa and q=h+d. For a positive-area convex S_w containing both top-edge endpoints, its uniform area centroid satisfies

    mean(xi)>=U/3, mean(eta)>=U/3.

For polygons, fan from the corresponding top endpoint and use the true area-weighted triangle means. Approximation by inscribed polygons containing both endpoints proves the compact-convex case. Since mean(s)<=U, these inequalities imply

    |int_S(xi-eta)| <= (1/3) int_S s.

Hence, at every height,

    int_S(p xi+q eta)
      <= [1+|p-q|/(3(p+q))] (p+q)/2 int_S s
      <= [1+|p-q|/(3(p+q))] int_{S^rad}(p xi+q eta).

The multiplier is constant across heights. After integrating, V and E are identical while

    N(P) <= R(eta) N(P^rad),
    eta=max(p,q)/min(p,q).

### Re-marking is essential and is explicit

The radial replacement need not contain the OLD C,D. Instead use its actual outer points

    C+=(0,U(0),0), D+=(kappa U(d),0,d)

in level coordinates. Put s_C=U(0)>=1, s_D=kappa U(d)>=1. In original coordinates their z-values are

    z_C=(1-s_C)/alpha,
    z_D=(1-d)(1-s_D)/alpha.

The canonical affine normalization is

    x'=x/s_D,
    y'=y/s_C,
    z'=z-(z_D/s_D)x-(z_C/s_C)y.

It fixes A,B, sends C+,D+ to C,D, and retains endpoint values 1,b,0,d. Its determinant is 1/(s_C s_D). Its TRUE moment changes are

    V'=V*/(s_C s_D), E'=E*/(s_C s_D),
    X'=X*/(s_C s_D^2), Y'=Y*/(s_C^2 s_D),
    Z'=[Z*-(z_D/s_D)X*-(z_C/s_C)Y*]/(s_C s_D).

In particular

    T(P')=[h s_C X*+(h+d)s_D Y*]/(6V*E*) >= T(P^rad).

The resulting body is an actual homothetic shell with aspect kappa s_C/s_D and profiles U/s_C,L/s_C. The supplied whole-shell theorem applies, giving

    T(P)<R(eta) Cstar.

There is no free centroid and no inference from equality of section areas to equality of all first moments.

### The stronger intrinsic upper-growth test

One may first re-mark C at its outer root endpoint, then choose an actual outer x-axis point at a height e maximizing (h+w)U(w). This gives a trace-nondecreasing canonical body with

    U_new(0)=1, kappa_new=U(0)/U(e), d_new=e,
    (h+e)/(h kappa_new)=sigma.

The trace comparison follows directly from

    T_new=alpha[h U(0) int_K x
              +(h+e)kappa U(e) int_K y]/(6 Vol(K) int_K w).

Both coefficients dominate the old ones: C containment gives U(0)>=1, and D containment gives kappa U(d)>=1. The maximum at e includes the old d. If e=0, the resulting aligned d=0 shell is handled by the parent's closed boundary theorem. Otherwise the positive-d theorem applies. Therefore

    T(P)<=Cstar R(sigma).

Since R(103/100)=204/203 and Cstar<203/100, sigma<=103/100 gives T<51/25, including the closed equality boundary. This permits arbitrary original outer kappa; the restriction is on the actual weighted outer-height growth, not on an assumed universal aspect normalization.

## 6. Proper-pair transfer with a quantitative margin

For a positive-root input P in the new class, q0 in relint(root) with positive x,y, and 0<lambda<1, put

    K_lambda=conv(Tetra,lambda P+(1-lambda)q0).

Exactly as a direct containment calculation, not a monotonicity claim,

    lambda^3 V <= V_lambda,
    lambda^4 E <= E_lambda,
    N_lambda <= N,
    T(K_lambda)<=lambda^(-7)T(P).

The coordinate faces are exactly ABC and ABD because every point in the contracted body has positive x,y. The root remains two-dimensional. These are genuine maximal-face statements. The parent's proper-transfer argument is used with its actual hypotheses, not as a representation theorem for all proper bodies.

A convenient whole proper family is:

    either eta<=101/100 or sigma<=101/100,
    2499/2500 <= lambda < 1.

Here R<=604/603 and lambda^7>=9972/10000, so

    T(K_lambda)<3065300/1503279<51/25,
    51/25-3065300/1503279=34729/37581975.

The real controls below lie in this family. This proper consequence does not assert that an arbitrary one-zero proper body admits such a cap-complete parent.

## 7. Actual two-normal dominance for ALL aspects

This reduction is stronger geometrically than the value sector, but does not yet give a full value bound.

First perform the outer C and maximizing-D re-marking just described. Rename the resulting parameters b,d,kappa,U. Then

    U(0)=1, kappa U(d)=1,
    p=h kappa <= q=h+d,
    (h+w)U(w)<=(h+d)U(d).

If d=0, p=q and the radial replacement already reduces to the closed homothetic theorem. Assume d>0.

Let L be the synchronized covolume profile from Section 4. For p<q define

    t(U,L)=sqrt(pq)L,                         L<=sqrt(p/q)U;
    t(U,L)=qU-sqrt(q(q-p))*sqrt(U^2-L^2),      L>=sqrt(p/q)U.       (7.1)

For p=q use t=pL. Define the new sections

    xi,eta>=0, xi+eta<=U(w), p xi+q eta>=t(w).                    (7.2)

These sections have exactly the original areas and maximize the n-first moment among ALL measurable subsets of the same outer triangle with that area. This is the elementary threshold-set comparison: the complement consists of the points with smallest p xi+q eta.

### Joint convexity of (7.2)

The function t(U,L) is convex on 0<=L<=U, nonincreasing in U, and nondecreasing in L. In the second region put c=sqrt(q(q-p)). Its Hessian is

    c/(U^2-L^2)^(3/2) * [[L^2,-UL],[-UL,U^2]],

which is positive semidefinite. At L=sqrt(p/q)U the two formulas have the same value and gradient (0,sqrt(pq)). The boundary L=U follows by continuity. Composition with concave U(w) and convex L(w) is convex: first use monotonicity at the interpolated pair, then convexity of t. Thus (7.2) is ONE actual convex body.

### The endpoint/root checks are not optional

A,B survive because the upward closure contains the origin at w=b,1, so L=0 throughout [b,1]. C is the high-n outer endpoint at w=0 and survives because the root has positive area.

D is also retained, and this is a derived strict guard. At its height,

    t(d)<=pU(d)  iff  L(d)<=sqrt(p/q)U(d).

Since kappa<=q/h and U(d)=1/kappa,

    sqrt(p/q)U(d)=sqrt(h/(kappa q))>=h/q.

For d>=b, L(d)=0. For 0<d<b, convexity and L(0)<=1 give

    L(d)<=1-d/b < h/(h+d)=h/q,

where the strict difference is d(1+d)/(bq). Therefore D is strictly above the lower cut. This covers d=1 as well; d=0 is the separate aligned case. No unrestricted root rotation at a zero endpoint is invoked.

The transformation preserves V,E and the whole ell-law, increases N, and preserves root area. It generally changes X,Y,Z and the true centroid. It can change the maximal facets and need not be polyhedral.

## 8. Elimination of all remaining lower-profile auxiliary curvature

After (7.2), fix the actual U,b,d,kappa. Let M=t(0)<q; strict inequality follows from positive root area. Consider all convex nonnegative f with

    f=0 on [b,1], f(0)<=M.

Every corresponding body

    xi,eta>=0, xi+eta<=U(w), p xi+q eta>=f(w)

is admissible. Indeed f(w)<=M(1-w/b)_+, U(w)>=1-w, and M<q ensure nonempty positive sections. The same strict D guard holds with f in place of t. C,A,B remain contained.

This is a compact family of actual bodies: all lie in one fixed bounded upper container and contain the body with lower profile M(1-w/b)_+. Hausdorff limits remain threshold bodies; the high-axis points (0,U(w),w) remain, and the lower profile can only acquire a smaller allowed root value. V and E have fixed positive lower bounds from the canonical tetrahedron. Thus T attains a maximum in this family.

If the maximizing f has f(0)=0, it is identically zero. Otherwise represent its true convex curvature by

    f(w)=int_(0,b] (1-w/s)_+ dmu(s),  mu((0,b])=f(0).

This is a representation of a convex boundary, not a volume density. Redistributing a small fraction of mu to any s in (0,b] preserves convexity, f(0), and all the established mark guards.

Freeze r0=N/V and q0=N/E. The true first derivative of N-r0 V-q0 E under a lower-threshold variation has sign

    -int j(f(w),U(w))[f(w)-r0-q0 w] delta f(w) dw,

where the actual section coarea factor is

    j=t/(pq),                         t<=pU;
    j=(qU-t)/(q(q-p)),                 t>=pU.

It is positive wherever 0<t<qU, and the two formulas agree at t=pU. Since f is nonincreasing while positive, f-r0-q0w is strictly decreasing. The forcing therefore has only the sign pattern positive, then negative, then possibly zero after f vanishes.

For a unit curvature mass at s, the derivative kernel is

    K(s)=-int_0^s P(w)(1-w/s)dw,
    K'(s)=-s^(-2) int_0^s w P(w)dw,
    P(w)=j(f,U)[f-r0-q0w].

The last cumulative integral first increases and then decreases, with no later increase. Thus K has no admissible interior global maximum: it decreases then increases, or is increasing; a terminal flat segment before b can only occur below K(0)=0. The endpoint s=0 is not a curvature-support point of a continuous actual boundary. The variational support condition therefore forces mu to be concentrated at b.

Consequently some trace-maximizing member of this fixed-upper family has

    f(w)=m(1-w/b)_+,  0<=m<=M.

This proves the stated lower-plane reduction (NF). The operation can change root area and V,E; it does NOT claim those quantities remain fixed during this final optimization. They are recalculated from the actual sections below.

### Exact remaining moment problem

Let t=m(1-w/b)_+, zeta=qU-t, and let A_s,I_xi,I_eta be section area and first moments in xi,eta.

When t<=pU:

    A_s=U^2/2-t^2/(2pq),
    I_xi=U^3/6-t^3/(6p^2q),
    I_eta=U^3/6-t^3/(6pq^2).

When pU<=t<=qU:

    A_s=zeta^2/[2q(q-p)],
    I_xi=A_s*zeta/[3(q-p)],
    I_eta=A_s*[U-zeta/(3q)-zeta/(3(q-p))].

The original uniform moments are exactly

    V=(kappa/alpha) int A_s,
    X=(kappa^2/alpha) int I_xi,
    Y=(kappa/alpha) int I_eta,
    E=(kappa/alpha) int w A_s,
    Z=[V+(d-1)X-Y-E]/alpha,
    N=hX+(h+d)Y.

These formulas include every seam. There is at most ONE high-to-low section transition: t/U is strictly decreasing on [0,b), because concavity and U(b)>0 make U(w)/(b-w) strictly increasing. If the high regime exists, its endpoint w_* solves

    m(1-w_*/b)=pU(w_*),

and the D guard gives w_*<min(b,d). This is useful actual coupling for the remaining upper-profile problem.

The lower plane in original level coordinates is h x+(h+d)y+(m/b)w=m. The root plane, coordinate planes, top cap when two-dimensional, and the supporting lines of the concave U profile determine the true boundary. No facet count is inferred by calling a curved profile polyhedral.

## 9. A second admissible operator that stays inside the chord class

There is a simpler one-sided shaking which can be useful when leaving the chord class is undesirable. After the maximizing-D re-marking, p<=q. In coordinates (xi,s=xi+eta,w), write the genuine fiber as

    l(s,w)<=xi<=r(s,w), length F(s,w)=r-l.

The projected domain is convex and F is jointly concave. Replace the interval by 0<=xi<=F(s,w). This is a convex hypograph in three dimensions, preserves every (s,w)-fiber length, and stays in the quadrant because F<=s. At s=U(w), the original interval is already [0,U], so the whole outer edge and all re-marked canonical points survive.

Writing I=int lF ds dw, its exact changes are

    Delta V=Delta E=0,
    Delta X=-kappa^2 I/alpha,
    Delta Y=kappa I/alpha,
    Delta N=kappa(q-p)I/alpha>=0,
    Delta Z=[(d-1)Delta X-Delta Y]/alpha.

Root area and every height moment are preserved. This is a real convex-body transformation, not independently chosen section centroids. It does not by itself make the lower boundary a parallel band.

## 10. Exact physical controls and failed extensions

All five controls use the original uniform filling, recompute their own centroid, reconstruct maximal faces and true edges, and audit all four true-edge primitives with M=N_metric=I. The symbol E in the trace remains the ell-integral, not the edge count. Every primitive in these five controls is nonzero.

### 10.1 Genuinely changing lower intercepts, T>2.02

In level coordinates choose b=1/5, d=1/1000 and

    x,y,w>=0,
    x+y<=1,
    (999/1000)(x+y)+w<=1,
    101x+99y+400w>=80,
    1881x+1919y+8000w>=1520.

This is one actual convex polytope. Its lower x/y intercept ratios at w=0,1/100,1/10 are respectively

    1, 360/361, 99/101.

Its lower supporting lines are nonparallel, their active sets change with w, and it is not a homothetic shell. The true f-vector is 10/15/7, strict SUH=4/4/6, weak000. Its coordinate faces have 5 and 6 vertices, not 3 and 3.

Its exact original moments are

    V=2003687/11008800,
    X=170561604203/3635810323200,
    Y=1225308577/26156908800,
    Z=3403604614721/72716206464000,
    E=1867601656337/36725356800000,
    N=409225713579403/3635810323200000,
    T=3250421382144972400/1603752497134677651
      approximately 2.026759981950016.

Here U is constant up to d and then affine to zero, so sigma=1201/1200. The new complete value theorem applies.

### 10.2 Proper high-trace control, and the lost-common-edge countercontrol

Take the preceding body's root vertex mean

    q0=(1093/2475,1093/2475,0)

in level coordinates, lambda=2499/2500, and form conv(Tetra,lambda K+(1-lambda)q0). Its actual f-vector is 10/22/14, strict SUH=4/4/6, weak000, and its coordinate maximal facets are exactly ABC and ABD. It has

    T=5143376561928049245757313386078500000000
      /2537675609744762485274771111227896029917
      approximately 2.0268061615823965.

Thus this particular proper contraction INCREASES trace. Only the proved lambda^(-7) estimate, not monotonicity, was used. This is not E17 and not 110.

Now attempt the unprotected area-preserving radial band in the n-aligned aspect kappa=1201/1200. At the actual section w=b its xy vertices are

    (0,0), (800/999,0),
    (34976/247252599,197955776/247252599), (0,4/5).

Its area is 395981434048/1235026732005, its outer maximum U=max(x/kappa+y) is 237786858176/296950371399, and the proposed lower radius satisfies

    L(b)^2=1643224282002125637632
           /3262642353738149377036437 >0.

Therefore the proposed band does not contain B=(0,0,b). Moreover A is the ONLY actual vertex above w=b. The entire upper part is a cone from A, so L(w)=(1-w)L(b)/(1-b)>0 for b<=w<1. The proposed replacement deletes the whole common-edge interval below A. This is an exact failure on a genuine proper one-zero body with T>2, not a formal profile counterexample.

### 10.3 Exact execution of a successful nontriangular-deficit replacement

Use b=1/5,d=1/1000,kappa=1201/1200,u=1200/1201, and the outer broken line through (0,1),(d,u),(1,0). In outer coordinates xi=x/kappa, eta=y, the lower missing root region has vertices

    (0,0), (41/50,0), (16/41,16/41), (0,41/50),

and scales by (1-w/b)_+. Its area is 8/25, so its radial area-equivalent deficit is the triangle of radius rho=4/5, because 2*(41/50)*(16/41)=rho^2.

The source audits BOTH actual bodies. The nontriangular-deficit body has 9/14/7 and strict 5/4/7; the radial-band successor has 8/12/6 and strict 4/4/6. Both are weak000. They have exactly the same

    V=1258256273/6917760000,
    E=468652953067/9223680000000,

but different true centroids. Their traces are respectively

    49028235571896433484800/24177106240317620910931,
    1195852193522162304000/589685518056527339291.

The second exceeds the first by

    1704362512220979200/24177106240317620910931 >0.

Thus the successful synchronized replacement is represented by two independently re-hulled rational three-dimensional bodies, not only by a section integral argument.

### 10.4 Independent convexity failure when the chord hypothesis is removed

Set b=1/5,d=1/2. In level coordinates take the convex hull of the two rectangles

    [0,1] x [1/10,2] at w=0,
    [0,1] x [0,19/10] at w=1/10,

and A=(0,0,1), B=(0,0,1/5), D=(1,0,1/2). C=(0,1,0) lies in its root.

For every 0<=w<=1/10 the actual section is EXACTLY

    [0,1] x [1/10-w,2-w].

All remaining generating points satisfy 0<=x<=1 and 1/10<=y+w<=2, so they add nothing to these already full sections. Their area is 19/10 and U=max(x+y)=3-w. The naive area-equivalent band would require

    L(w)=sqrt((3-w)^2-19/5),
    L''(w)=-(19/5)/[(3-w)^2-19/5]^(3/2)<0.

It is strictly concave, not convex. At w=0,1/20,1/10, L^2 equals 26/5,1961/400,461/100. The exact squared midpoint certificate is

    v=4L(1/20)^2-L(0)^2-L(1/10)^2=49/5,
    v^2-4L(0)^2 L(1/10)^2=19/125>0.

The original body is genuine 10/16/8, strict 5/3/6, weak000. Its actual moments are

    V=133/120, X=323/640, Y=15751/19200, Z=-2641/7680,
    E=2983/9600, N=384047/192000, T=20213/20881.

Its trace is below 1; it is a convexity countercontrol, not a high-trace counterexample. The separate proper control above supplies the T>2 endpoint failure.

## 11. Complete deterministic recovery capsule

Save the following complete unit as coconvex_trace.py, UTF-8/LF with one final LF, and run with assertions enabled:

    python -S coconvex_trace.py > receipt.txt

Tested environment: CPython 3.13.5, standard library only, no seed, no external inputs, no numerical hull library. It enumerates all supporting triples, removes nonvertices/collinear integration nodes, reconstructs maximal facet cycles and true edges, integrates from an interior point and two different actual vertex apices, and checks all true primal/polar edge primitives at the actual volume centroid.

Observed original and clean-directory replay pins:

    coconvex_trace.py: 11172 bytes
    SHA256 aed2ea22202546d65f552179f51a65465aa9b4675d409d0531e603b1802edeaa
    coconvex_trace.json: 8329 bytes
    SHA256 74b78f43c191f7c269879664cfb621a6029f86e632be5c106455821b8587dec0
    receipt.txt: 487 bytes
    SHA256 38dded884ec55963f45fe341a1e3a14c0c0bd60b5af974b10f48ec7ac6370e62

Expected final marker:

    COCONVEX_TRACE_EXACT_GEOMETRY_AND_NONCONVEX_REARRANGEMENT_PASS

The JSON reconstructs every vertex, maximal facet, plane, true edge, all six scalar integrals, centroid, strict equilibrium labels, and the endpoint-loss section. The hashes are verification pins; the source and all exact inputs are embedded here.

```python
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import json

# Exact parent: minimum-0147,
# assignment SHA256 80e36a50ac09768d59f513ea33b5340c3a3bad4d301fc4bc083d7a868a162cd9.
# CPython 3.13.5, standard library only; assertions must be enabled.

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(c,a): return tuple(c*x for x in a)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def average(v): return tuple(sum(p[j] for p in v)/len(v) for j in range(3))
def ratrow(row): return tuple(F(x) for x in row)

def solve3(rows,rhs):
    d=det(*rows)
    if not d: return None
    return tuple(det(*(tuple(rhs[i] if k==j else rows[i][k] for k in range(3))
                      for i in range(3)))/d for j in range(3))

def from_halfspaces(H):
    P=set()
    for ids in combinations(range(len(H)),3):
        p=solve3([H[i][0] for i in ids],[H[i][1] for i in ids])
        if p is not None and all(dot(n,p)<=s for n,s in H): P.add(p)
    assert len(P)>=4
    return sorted(P)

def cycle(P,ids,n):
    drop=next(j for j in range(3) if n[j])
    keep=[j for j in range(3) if j!=drop]
    Q=sorted((P[i][keep[0]],P[i][keep[1]],i) for i in ids)
    def turn(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lo=[]
    for p in Q:
        while len(lo)>=2 and turn(lo[-2],lo[-1],p)<=0: lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(Q):
        while len(hi)>=2 and turn(hi[-2],hi[-1],p)<=0: hi.pop()
        hi.append(p)
    return tuple(p[2] for p in lo[:-1]+hi[:-1])

def hull(candidates):
    Q=sorted(set(candidates)); raw={}
    for i,j,k in combinations(range(len(Q)),3):
        n=cross(sub(Q[j],Q[i]),sub(Q[k],Q[i]))
        if n==(0,0,0): continue
        s=dot(n,Q[i]); vals=[dot(n,p)-s for p in Q]
        if all(v<=0 for v in vals): pass
        elif all(v>=0 for v in vals): n=mul(-1,n); s=-s; vals=[-v for v in vals]
        else: continue
        ids=tuple(i for i,v in enumerate(vals) if v==0)
        raw[ids]=(n,s)
    extreme=set()
    for ids,(n,s) in raw.items(): extreme.update(cycle(Q,ids,n))
    P=[Q[i] for i in sorted(extreme)]
    index={p:i for i,p in enumerate(P)}; ff={}
    for ids,(n,s) in raw.items():
        face=tuple(sorted(index[Q[i]] for i in cycle(Q,ids,n)))
        ff[face]=(n,s)
    faces=[]; planes=[]
    for ids,(n,s) in sorted(ff.items()):
        f=cycle(P,ids,n)
        faces.append(f); planes.append((n,s))
    edges={}
    for f_id,f in enumerate(faces):
        for i in range(len(f)):
            edge=tuple(sorted((f[i],f[(i+1)%len(f)])))
            edges.setdefault(edge,[]).append(f_id)
    assert all(len(v)==2 for v in edges.values())
    assert len(P)-len(edges)+len(faces)==2
    for p in P:
        active=[n for n,s in planes if dot(n,p)==s]
        assert any(det(*triple)!=0 for triple in combinations(active,3))
    return P,faces,planes,edges

def moments(P,faces,o):
    V=F(0); J=(F(0),)*3
    for f in faces:
        a=P[f[0]]
        for i in range(1,len(f)-1):
            b,c=P[f[i]],P[f[i+1]]
            v=abs(det(sub(a,o),sub(b,o),sub(c,o)))/6
            V+=v
            J=add(J,mul(v/4,add(add(o,a),add(b,c))))
    return V,J

def world(p,b,d):
    x,y,w=p
    return x,y,(1+(d-1)*x-y-w)/(1-b)

def audit(K,b,d,proper):
    P,faces,planes,edges=hull([world(p,b,d) for p in K])
    V,J=moments(P,faces,average(P))
    for o in [P[0],P[-1]]: assert moments(P,faces,o)==(V,J)
    g=mul(1/V,J); X=[sub(p,g) for p in P]
    Q=[mul(1/(s-dot(n,g)),n) for n,s in planes]
    E=V+(d-1)*J[0]-J[1]-(1-b)*J[2]
    N=(1+b)*J[0]+(1+b+d)*J[1]
    T=N/(6*V*E)
    ell=lambda p: 1+(d-1)*p[0]-p[1]-(1-b)*p[2]
    assert min(map(ell,P))==0 and max(map(ell,P))==1
    canonical=[ratrow(r) for r in [(0,0,0),(0,0,1),(0,1,0),(1,0,0)]]
    assert all(all(dot(n,p)<=s for n,s in planes) for p in canonical)
    root=[i for i,p in enumerate(P) if ell(p)==0]
    assert any(set(f)==set(root) for f in faces)
    coord=[]
    for j in [0,1]:
        ids=[i for i,p in enumerate(P) if p[j]==0]
        assert any(set(f)==set(ids) for f in faces)
        coord.append(ids)
    if proper:
        assert {P[i] for i in coord[0]}=={canonical[i] for i in [0,1,2]}
        assert {P[i] for i in coord[1]}=={canonical[i] for i in [0,1,3]}
    pv=[[] for p in P]; pf=[[] for f in faces]; saddles=[]; weak=[]; zero=0
    for edge,(f,h) in sorted(edges.items()):
        i,j=edge
        a=dot(X[i],sub(X[j],X[i])); bb=dot(X[j],sub(X[i],X[j]))
        c=dot(Q[f],sub(Q[h],Q[f])); dd=dot(Q[h],sub(Q[f],Q[h]))
        vals=[a,bb,c,dd]; zero+=sum(v==0 for v in vals)
        pv[i].append(a); pv[j].append(bb); pf[f].append(c); pf[h].append(dd)
        if all(v<0 for v in vals): saddles.append(edge)
        if all(v<=0 for v in vals) and any(v==0 for v in vals): weak.append(edge)
    S=[i for i,v in enumerate(pf) if all(x<0 for x in v)]
    U=[i for i,v in enumerate(pv) if all(x<0 for x in v)]
    # Weak edge-packets are reported, not silently equated with physical-point counts.
    return dict(vertices=P,facets=faces,edges=sorted(edges),planes=planes,
                f_vector=[len(P),len(edges),len(faces)],V=V,X=J[0],Y=J[1],Z=J[2],
                E=E,N=N,T=T,centroid=g,root=root,coordinate_faces=coord,
                strict_SUH=[len(S),len(U),len(saddles)],stable=S,unstable=U,
                saddle_edges=saddles,weak_edge_packets=weak,zero_primitives=zero)

def section_stats(report,b,d,w,kap):
    P=[tuple(F(x) for x in row) for row in report['vertices']]
    K=[(x,y,1+(d-1)*x-y-(1-b)*z) for x,y,z in P]
    pts=set(p[:2] for p in K if p[2]==w)
    for i,j in report['edges']:
        p,q=K[i],K[j]
        if min(p[2],q[2])<w<max(p[2],q[2]):
            t=(w-p[2])/(q[2]-p[2])
            pts.add(tuple(p[k]+t*(q[k]-p[k]) for k in [0,1]))
    Q=[(*p,F(0)) for p in sorted(pts)]
    cc=cycle(Q,range(len(Q)),(0,0,1))
    area=abs(sum(Q[cc[i]][0]*Q[cc[(i+1)%len(cc)]][1]
                 -Q[cc[i]][1]*Q[cc[(i+1)%len(cc)]][0]
                 for i in range(len(cc))))/2
    U=max(p[0]/kap+p[1] for p in Q)
    L2=U*U-2*area/kap
    return dict(points=[Q[i][:2] for i in cc],area=area,U=U,L_squared=L2)

def serialize(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {k:serialize(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [serialize(v) for v in x]
    return x

def main():
    assert __debug__
    b,d=F(1,5),F(1,1000)
    H=[((-1,0,0),0),((0,-1,0),0),((0,0,-1),0),((1,1,0),1),
       ((F(999,1000),F(999,1000),1),1),
       ((-101,-99,-400),-80),((-1881,-1919,-8000),-1520)]
    H=[(ratrow(n),F(s)) for n,s in H]
    K=from_halfspaces(H)
    A=audit(K,b,d,False)
    assert A['T']>F(101,50)
    assert not A['weak_edge_packets']
    R=1+F(1,7203)
    assert R==1+abs((1+b)-(1+b+d))/(3*((1+b)+(1+b+d)))
    assert F(1+b+d)/(1+b)<F(103,100)
    # Genuine changing lower-intercept ratios; values are in original x,y,w coordinates.
    intercepts=[]
    for w in [F(0),F(1,100),F(1,10)]:
        lx=max(F(0),(80-400*w)/101,(1520-8000*w)/1881)
        ly=max(F(0),(80-400*w)/99,(1520-8000*w)/1919)
        intercepts.append([w,lx,ly,lx/ly])
    assert len({r[-1] for r in intercepts})==3
    root=[p for p in K if p[2]==0]; q=average(root)
    assert q[0]>0 and q[1]>0 and q[2]==0
    lam=F(2499,2500)
    anchors=[ratrow(r) for r in [(0,0,1),(0,0,b),(0,1,0),(1,0,d)]]
    KP=anchors+[add(mul(lam,p),mul(1-lam,q)) for p in K]
    AP=audit(KP,b,d,True)
    assert AP['T']>2 and AP['T']<F(51,25)
    assert not AP['weak_edge_packets']
    assert AP['T']<=A['T']/lam**7
    # A proper high-trace body defeats the unprotected n-aligned band replacement:
    # at w=b its lower radius is positive, so it deletes the canonical endpoint B.
    B_loss=section_stats(AP,b,d,b,F(1201,1200))
    assert B_loss['L_squared']==F(1643224282002125637632,3262642353738149377036437)>0
    heights=[1+(d-1)*p[0]-p[1]-(1-b)*p[2] for p in AP['vertices']]
    assert sum(w>b for w in heights)==1 and max(heights)==1
    # General one-percent/proper-collar bound using only Cstar<203/100.
    proper_bound=F(203,100)*F(604,603)/F(9972,10000)
    assert proper_bound==F(3065300,1503279)<F(51,25)
    # Exact aligned, nontriangular deficit: the replacement itself is rational.
    kap=F(1201,1200); u=1/kap; rho=F(4,5)
    rr,pp=F(41,50),F(16,41)
    assert 2*rr*pp==rho*rho and 2*pp<rr
    upper=[((-1,0,0),0),((0,-1,0),0),((0,0,-1),0),
           ((1/kap,1,(1-u)/d),1),
           (((1-d)/kap,1-d,u),u)]
    cuts=[((pp/kap,rr-pp,rr*pp/b),rr*pp),
          (((rr-pp)/kap,pp,rr*pp/b),rr*pp)]
    HA=[(ratrow(n),F(s)) for n,s in upper]
    HA += [(mul(-1,ratrow(n)),-F(s)) for n,s in cuts]
    HB=[(ratrow(n),F(s)) for n,s in upper]
    HB += [(ratrow((-1/kap,-1,-rho/b)),-rho)]
    aligned=audit(from_halfspaces(HA),b,d,False)
    band=audit(from_halfspaces(HB),b,d,False)
    assert (1+b)*kap==1+b+d
    assert aligned['V']==band['V'] and aligned['E']==band['E']
    assert aligned['N']<band['N'] and aligned['T']<band['T']<F(203,100)
    assert aligned['centroid']!=band['centroid']
    assert not aligned['weak_edge_packets'] and not band['weak_edge_packets']
    # Negative actual convex-body control: rectangular sections translated in y.
    bn,dn=F(1,5),F(1,2)
    KN=[(F(x),y-w,w) for w in [F(0),F(1,10)]
        for x in [0,1] for y in [F(1,10),F(2)]]
    KN += [ratrow(r) for r in [(0,0,1),(0,0,bn),(1,0,dn)]]
    AN=audit(KN,bn,dn,False)
    # On 0<=w<=1/10, sections are [0,1] x [1/10-w,2-w].
    # U=3-w, area=19/10, naive L=sqrt((3-w)^2-19/5).
    # L''=-(19/5)/((3-w)^2-19/5)^(3/2)<0: the proposed shell is NOT convex.
    for p in KN: assert F(1,10)<=p[1]+p[2]<=2 and 0<=p[0]<=1
    sq=[(3-w)**2-F(19,5) for w in [F(0),F(1,20),F(1,10)]]
    assert sq==[F(26,5),F(1961,400),F(461,100)]
    # Exact midpoint test sqrt(sq[1]) > (sqrt(sq[0])+sqrt(sq[2]))/2.
    v=4*sq[1]-sq[0]-sq[2]
    assert v>0 and v*v>4*sq[0]*sq[2]
    report=dict(parent_assignment='minimum-0147',
       parent_assignment_sha256='80e36a50ac09768d59f513ea33b5340c3a3bad4d301fc4bc083d7a868a162cd9',
       nonhomothetic=A,lower_intercepts=intercepts,root_center=q,lambda_value=lam,
       proper=AP,proper_B_loss=B_loss,aligned=aligned,aligned_band=band,negative=AN,
       negative_midpoint_squares=sq,proper_bound=proper_bound)
    data=(json.dumps(serialize(report),sort_keys=True,separators=(',',':'))+'\n').encode()
    Path('coconvex_trace.json').write_bytes(data)
    print('NONHOMOTHETIC',*A['f_vector'],A['T'],*A['strict_SUH'])
    print('PROPER',*AP['f_vector'],AP['T'],*AP['strict_SUH'])
    print('ALIGNED',*aligned['f_vector'],aligned['T'],*aligned['strict_SUH'])
    print('ALIGNED_BAND',*band['f_vector'],band['T'],*band['strict_SUH'])
    print('NEGATIVE',*AN['f_vector'],AN['T'],*AN['strict_SUH'])
    print('REPORT',len(data),hashlib.sha256(data).hexdigest())
    print('COCONVEX_TRACE_EXACT_GEOMETRY_AND_NONCONVEX_REARRANGEMENT_PASS')

if __name__=='__main__': main()
```

## 12. Remaining complement and the useful continuation

The successful mechanism was to use the upward closure of one actual body, derive the covolume profile from that common geometry, and protect the canonical marks by genuine re-marking before rearrangement. Extending the parent by assigning separate intercept or centroid profiles would miss both countercontrols above.

The most useful successor is the exact normal form (NF), not another independent choice of section area and centroid. It retains one concave U, an actual lower plane, the maximizing-D inequality, original uniform moment formulas, and at most one section-regime switch strictly before d. A valid next upper-profile variation must retain the D reaction and account for the changing exposed portion of the upper chord in the high-root regime. No upper-curvature elimination has been proved here.

The value theorem currently closes eta<=103/100 or sigma<=103/100 in the intrinsic chord class, plus the stated proper-resolution family. The all-aspect chord class has the stronger genuine reduction but not yet a full 51/25 value bound.

Outside it remain sections that extend beyond their two axis intercepts, sections that do not meet both axes, and max ell>1 bodies. In particular a general proper one-zero root need not meet the second coordinate axis, so the chord hypothesis cannot be silently transferred to the thirteen-vertex localization. The supplied branch memory itself warns that the thirteen-vertex conclusion concerns attained joint maxima and does not make arbitrary one-zero bodies members of a special section family.

The proper high-trace B-loss control isolates the canonical difficulty for a broader replacement: the common edge has to survive as a nondegenerate axis interval, not merely as a set of zero-area marked points. The translated-rectangle control separately isolates the three-dimensional convexity difficulty. Neither failure is repaired by preserving all height moments alone.

No claim of universal one-zero exclusion, full maxell>A exclusion, E17 census change, new attaining complexity, or proof-assistant certification follows. The exact controls and both useful failures are durable in the embedded source.

Convenience copies, not dependencies: runnable source (`coconvex_trace.py`), full exact report (`coconvex_trace.json`), and execution receipt (`receipt.txt`).
