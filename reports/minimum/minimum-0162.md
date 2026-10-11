# minimum-0162

Historical AI scientific report · saved 2026-09-21 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# TWO_ANCHOR_HIGH_ANCHOR_ERASURE_AND_NONFLAT_VALUE_SECTORS_V1

## 1. Result and exact boundary

The whole positive-endpoint two-anchor sector is not yet closed. This continuation supplies a substantially smaller **genuine full-class stationary geometry**, two original-trace value inequalities on actual bodies, and two exactly audited nonstationary controls.

**Stationary reduction.** In the remaining proper33, two-nonflat-star sector, **there are no ordinary A facets**. Consequently the lower star has exactly two facets and the upper star has two special facets and at most one ordinary, root-based triangle. The literal maximal-face bounds improve to

    F_true <= 8,  V_true <= 9,  E_true <= 15,  root edges <= 5.

There is at most one positive-ell auxiliary true vertex. At a full joint maximum with T>=2, every auxiliary vertex satisfies **ell(v)<7a/10**. In particular A is the unique ell-maximum. With a=1 and U=(1-d)x+(1-c)y+(1-b)hA, the reduced lower star satisfies the quantitative bound

    U(x,y) > 3(x+y)/(10t),    t=6 Vol(P),    x+y>0.

This is stronger than nonnegative U, and is not hA=0.

**Actual-body value estimates.** Normalize a=1, put s0=1+b, alpha=1-b, m=max(c,d), and

    epsilon_B = 6 alpha integral_Delta (x+y-hB(x,y)) dxdy.

For every bounded proper33 two-anchor polytope with positive endpoints and G(C),G(D)>=0, irrespective of stationarity or the numbers of lower/upper facets, I prove

    T < (2029/1000)(1+m/s0) + 16m(s0+m)/alpha.              (V1)

Thus the entire endpoint sector

    m[16000(s0+m)/alpha + 2029/s0] <= 11                  (V2)

has T<51/25. In particular, throughout the complete geometric class

    0<b<=2/3,   0<c,d<=1/8000,

one has the unconditional uniform bound

    T < 3262807/1600000 = 2.039254375 < 51/25,
    51/25 - 3262807/1600000 = 1193/1600000.

Separately, using the explicitly inherited actual joint-mass theorem, I prove the whole-class defect estimate

    T < max(129/64, 2+epsilon_B).                          (V3)

It enlarges the previous upper-defect exclusion from epsilon_B<=1/64 to **epsilon_B<=1/25**. Neither (V1) nor (V3) treats projected moments as a realizability certificate. The main new step in (V1) is an actual endpoint-root clipping comparison, with all three uniform integrals changed and accounted for.

**Controls.** Two new actual bodies have true (V_true,E_true,F_true)=(9,15,8), both stars nonflat, epsilon_B>1/25, already greedy vertical placement, and traces 2.028343714870837... and 2.028598946540442... . The first has all auxiliary vertices on a pentagonal root; the second has a quadrilateral root and one positive-ell auxiliary vertex. Both have strict own-centroid Euclidean census (S,U,H)=(4,4,6), weak count zero. They fail genuine facet reactions and are not stationary or threshold counterexamples.

No T>=51/25 body, whole E17 exclusion, or new attaining minimum is claimed. The mechanical interval remains 34<=Cmin<=622; the smaller auxiliary stationary fan is not a mechanical census decrement.

## 2. Read sources, identity, and inherited premises

I read the complete new 2,008-line journal, its complete literal parent payload, and the complete new height proof through EOF. The six earlier geometric sources and earlier parent result remain available in this same chat; their unchanged mathematical content was retained and consulted rather than reconstructed from missing archive IDs.

The new journal is 313472 bytes, SHA-256 e2ac334d495fee7830ffa7b973db925532db8cd648c10c39b2de71e2ad437c69. The new material [internal-source-reference] is 10958 bytes, SHA-256 c23e9d7f45f6fa3436daac568156befa6dd5bd7d7c8d43205a47d23601a50337. The required literal parent is minimum-0158, with declared immutable payload SHA-256 dc5a857ac21b3a00a6c6532258d95c8dd2f7740134c37e86d65e3261f57764a5. I found no mathematical identity or incidence conflict with that payload. Its proper33 conclusion and distinction between its genuine control and stationarity are retained. :contentReference[oaicite:0]{index=0}

The full geometric first-variation, hinge, projection, and greedy proofs are supplied. The old greedy executable [internal-source-reference] and old root-duality executable [internal-source-reference] are not computational dependencies and were not replayed. The original full source proving the inherited actual joint-mass inequality

    gx,gy>=1/4,    4(gx+gy)<=t+1

is not separately attached; (V3) explicitly uses that accepted theorem as recorded in the parent. The new ordinary-A reduction, auxiliary-height bound, and (V1) do **not** use the joint upper bound. The separate notebook localization/attainment results are neither reproved nor enlarged here; the stationary statements below concern the genuine polyhedral full-class maxima stipulated in this branch.

The scalar H(b,z) kernel appearing below is already in the accepted Cstar work. I am not claiming a new Cstar value or a better constant. The fresh 28-cell certificate is an independent self-contained proof of the weaker numerical bound H<2029/1000, so the present recovery needs none of that work's absent executable data. :contentReference[oaicite:1]{index=1}

## 3. Common actual-body notation and admissible variations

Let

    A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
    ell=1+(d-1)x+(c-1)y-alpha z,
    n=hc x+hd y,  hc=1+b+c,  hd=1+b+d,
    V=integral_P 1, E=integral_P ell, N=integral_P n,
    t=6V, r=N/V, q=N/E=Tt, T=N/(6VE),
    G=n-r-q ell,
    LA=(r+q)/3, LB=(r+qb)/3, LA>LB>0.

All integrals belong to the same uniformly filled P; its centroid is integral_P(x,y,z)/V. Scaling the four ell endpoints together allows a=1 without changing T. Throughout the positive-endpoint statements, 0<b<1 and c,d>0.

The actual two-anchor description is

    P={x,y>=0: hA(x,y)<=z<=min(1-hB(x,y),[1-(1-d)x-(1-c)y]/alpha)},

with finite convex homogeneous piecewise-linear hA,hB. Proper33 means hA equals zero on both unit axes and hB equals one there. Thus hA<=0 and hB<=x+y. The full joint mark variations, not merely fixed-lattice optimization, force proper33 in the sector under study: lowering a nonminimal marked C increases the transformed trace by alpha epsilon X, and extending its radius when hB(C)<1 has positive derivative (b+2c)X. The corresponding D variations give the other axis. These changes include the affine determinant and the changed endpoint value. :contentReference[oaicite:2]{index=2}

For clarity about the strength of stationarity used, at fixed ell the exact frozen-density comparison is

    T(P')>T(P) iff Delta integral G > (q/V) Delta V Delta E.

The supplied full-class cap and facet arguments imply: every auxiliary true vertex has G>0; every free maximal facet F satisfies max_F G+3 mean_F G<=0; and an ordinary facet with only the canonical vertex X is a true triangle [X,Y,Z] with G(Y)=G(Z)=-G(X)/3. Thin-edge caps handle equality G=0; whole-facet two-sided pivots allow nonsimple vertices to split. None of these facts assumes a fixed lattice. :contentReference[oaicite:3]{index=3} :contentReference[oaicite:4]{index=4}

A special AC lower facet admits the two-sided hinge z=p x -> z=(p+epsilon)x, hence integral_F G x=0. The AD hinge uses y. On an arbitrary such polygon the exact fan inequality is

    integral_F G phi <= (G(A)+3 max_F G)/4 * integral_F phi,

for nonnegative affine phi vanishing on the canonical hinge. The two B hinges are analogous. This is an actual polygon reaction, not a triangle substituted for a maximal polygon. :contentReference[oaicite:5]{index=5}

## 4. New high-anchor ordinary-facet erasure

### 4.1 An ordinary A triangle caps G globally

Suppose an ordinary A facet is F=[A,Y,Z], with G(Y)=G(Z)=LA. Its base YZ can meet only the root or a special B facet. The other possibilities are excluded by the common-anchor plane argument, the protected coordinate planes, or the incompatible levels LA and LB. This is the literal base-neighbor classification, not an inference from a triangulation. :contentReference[oaicite:6]{index=6}

First suppose YZ lies on a B facet J. Let h>=0 be its affine slack, normalized by h(A)=1; h(B)=0. Define

    K=G-LA+4LA h.

K vanishes at A,Y,Z, while K(B)=G(B)-LA<0. Thus K=0 is exactly the plane of F, and the actual body is on its K<=0 side. Since h>=0,

    G<=LA everywhere on P.                               (4.1)

If YZ instead lies on the root, take h=ell. Again K vanishes at A,Y,Z, and now

    K(B)=(b-1)(4r+q)/3<0.

The same conclusion follows. The orientation is important: the corresponding calculation for an ordinary B root triangle has the opposite sign at A and does not give this global upper cap.

### 4.2 The special lower hinge contradicts that cap

A nonflat proper lower star has a genuine special facet S containing AC and not D. Use phi=x. Its hinge reaction is zero, and (4.1) gives

    0=integral_S G phi <= (G(A)+3LA)/4 integral_S phi=0.

Equality forces every non-A true vertex of S to have G=LA. To see this without assuming S triangular, fan-triangulate S from A. On a positive-area fan triangle [A,P,Q], put s=phi(P), u=phi(Q). Here s,u>=0 and s+u>0. The exact integral has the terms G(P)(2s+u)+G(Q)(s+2u); both coefficients are positive. Equality in the upper bound therefore forces G(P)=G(Q)=LA on every fan triangle.

Consequently all non-A vertices of S lie on a single level line, so S is a true triangle with a base edge at G=LA. Its base and the ordinary base YZ cannot be collinear: a common line, together with A off that line, would determine the same facet plane. Their convex hull is two-dimensional. Because G<=LA globally, P therefore has a positive-area exposed facet on which G is the positive constant LA.

Such a facet cannot be free, by max G+3 mean G<=0. It cannot be either coordinate facet, which contains A with negative G. It cannot be the root, because there G=n-r is nonconstant: grad ell has nonzero z-component and grad n does not. This is a contradiction.

**Therefore rA=0.** The argument actually needs only a special A hinge and the stated two-anchor base classification. In the proper nonflat sector there are exactly two such special A facets, so all lower facets have now been accounted for.

### 4.3 True counts and the surviving positive-ell vertex

Both stars nonflat now gives

    FA=2, FB=2+rB, rB in {0,1}, F_true=7+rB.

The supplied polygon hinge obstruction still makes every ordinary B base root-based and gives rB<=1. Since deg A+deg B=F_true+1, all other true degrees are at least three, and Euler applies to the true lattice,

    V_true<=F_true+1, E_true<=2F_true-1.

This yields the announced 9/15/8 upper bounds. The root has at most two A neighbors, two special B neighbors, and one ordinary B neighbor; proper33 removes coordinate neighbors. Hence it has at most five physical edges. :contentReference[oaicite:7]{index=7}

There is also at most one positive-ell auxiliary vertex. Write theta=x/(x+y). The reduced hA has one angular breakpoint. If rB=0, hB has one; the convex root-shadow function has positive axis values and a nonempty negative interval I. At least one of those two breakpoints must lie strictly inside I, since an affine function cannot be negative between two zero endpoints. Only a breakpoint outside the closed root shadow can produce an off-root silhouette vertex, so at most one remains.

If rB=1, the two hB breakpoints are the rays through the two root endpoints of the ordinary B triangle. Both belong to the closed root shadow. Only the single hA breakpoint can produce an off-root vertex. An interior positive-ell vertex must use a lower or upper breakpoint, since there are no other facet types or vertical facets. Coordinate vertices are exactly A,B,C,D. This accounts for every possible positive-ell auxiliary vertex.

In particular, rB=0 with a positive-ell auxiliary forces a triangular root; rB=1 with such an auxiliary allows at most a quadrilateral root. The exact controls below realize the two different root/auxiliary alternatives as actual geometries, not as stationary maxima.

## 5. A strict auxiliary height gap and a bounded lower cone

This strengthens the new height-one input for polyhedral maxima. The input's actual tetrahedron and G-sign argument gives, for T>=2,

    m<=s0/(4t)<=s0/4<1/2.

It also supplies the sharper T-dependent endpoint bound recorded in the assignment. :contentReference[oaicite:8]{index=8}

Put C0=(s0+m)/(1-m). Since m<=s0/4,

    alpha C0 <= 5(1-b^2)/(3-b) < 2,

where the strict final inequality is the exact identity

    2(3-b)-5(1-b^2)=5(b-1/5)^2+4/5>0.

For any p in this actual body, the containing-tetrahedron volume formula gives z>=1-t. Writing h=ell(p), it follows that

    (1-m)(x+y) <= 1-h+alpha(t-1),
    n(p) <= C0[1-h+alpha(t-1)].

At an auxiliary vertex, G(p)>0. Consequently

    1-h > [q+r-alpha C0(t-1)]/(q+C0)
         >= (r+2)/(q+C0),                               (5.1)

with strictness retained in the subsequent bounds. Here q=Tt>=2t. Independently, a genuine tetrahedral fan from A gives E/V>=1/4, so q<=4r. The mark inequalities give r<s0+m<5/2, and C0<5. Therefore

    1-h > (r+2)/(4r+5) > 3/10,

since the last difference is (5-2r)/[10(4r+5)]>0. Thus every auxiliary vertex has ell<7/10. A is the unique ell-maximum, because b<1 and c,d<1/2. This direct polyhedral argument uses the new endpoint restriction; it neither transfers the height conclusion into a negative-G sector nor requires an independently selected centroid.

After Section 4,

    hA=max(-u x,-v y),  u,v>0.

Its breakpoint ray theta0=v/(u+v) is the genuine lower-lower edge issuing from A. Let L be that edge's other endpoint. It is auxiliary, x(L)+y(L)<=t, and ell(L)<7/10. Hence

    U(theta0)=(1-ell(L))/(x(L)+y(L))>3/(10t).

On the axes U is 1-d and 1-c, both greater than 1/2. U is affine on the two angular intervals, so U(theta)>3/(10t) everywhere. In particular the actual lower-cone section KA={x,y>=0:U<=1} is a bounded quadrilateral contained in (10t/3)Delta. This is a bounded auxiliary cone constructed from the real lower planes, not an assertion that KA equals the projection of P or its root.

## 6. Actual zero-endpoint geometry and quantitative positive-endpoint clipping

This section proves (V1) for **arbitrary proper two-anchor hA,hB**, not just the reduced small fan. The two-plane lower-star monotonicity is an additional reusable consequence.

### 6.1 An elementary actual planar area-moment bound

For any bounded convex polygon K in the first quadrant containing Delta, with area A_K,

    integral_K(x+y) <= A_K(1+2A_K)/3.                     (6.1)

Here is a constructive proof, included to avoid a missing capacity-source dependency. The origin is a true vertex; the two axis endpoints have coordinates at least one. At an interior boundary vertex P with neighbors U,V, slide P parallel to V-U. The local double-area det(U,P)+det(P,V) stays constant. The local sixfold first moment is

    det(U,P)[s(U)+s(P)] + det(P,V)[s(P)+s(V)],  s=x+y,

which is affine along this slide. Convexity and quadrant constraints give a nonempty two-sided interval of allowed positions. The interval is bounded: containing Delta and preserving area force s(P)<=2A_K, by the literal area of conv(Delta,P). At a terminal position a true vertex disappears, possibly an old axis endpoint becoming redundant. The old axis points remain in the hull, so Delta remains contained. Choose an endpoint that does not decrease the first moment, and repeat.

The final polygon is the triangle with vertices (0,0),(a0,0),(0,b0), where a0,b0>=1 and a0 b0=2A_K. Its first moment is A_K(a0+b0)/3. Since (a0-1)(b0-1)>=0, a0+b0<=1+2A_K, proving (6.1). Integration diagonals in this proof are not physical edges.

### 6.2 Exact original uniform integrals when c=d=0

Temporarily set ell0=1-x-y-alpha z and n0=s0(x+y), while retaining actual hA,hB. In coordinates w=ell0, original volume measure is dx dy dw/alpha. On theta=(theta,1-theta), put

    U0(theta)=1+alpha hA(theta),
    W0(theta)=1-alpha hB(theta),
    Z(theta)=W0(theta)/b>=1.

Boundedness implies U0>0. Indeed W0>=b>0, so U0<=0 on any ray would make the body unbounded on that ray. Canonical containment gives U0<=1, and W0>=b U0. Thus every interior ray is root-visible or on its limiting boundary, and its genuine fibre is

    max(0,b-rho W0) <= w <= 1-rho U0.

Define the integrals over the actual unit angular interval

    A2=integral U0^(-2), A3=integral U0^(-3),
    D2=integral Z^(-2),  D3=integral Z^(-3).

Literal radial integration, with the Jacobian rho, gives the original three-dimensional moments

    6V0=(A2-b D2)/alpha,
    24E0=(A2-b^2 D2)/alpha,
    12N0=s0(A3-b D3)/alpha.                              (6.2)

The section {U0<=1} is a genuine bounded convex polygon containing Delta. Its area is A2/2 and its s-moment is A3/3. Hence (6.1) gives

    A2>=1,  A3<=A2(1+A2)/2.

Set k=1/A2, so 0<k<=1. Equations (6.2) imply

    T0 <= F(k) := (1-b^2)[1+k-2b k^2 D3]
                  /[(1-bkD2)(1-b^2 kD2)].                (6.3)

These are linked integrals of the same actual gauges, not free area and centroid data.

### 6.3 The lower-area envelope increases to the flat case

The numerator Q of F'(k), after removing its positive factors, obeys

    Q-Q|_(D3=D2)
      =2bk[2-b(1+b)kD2](D2-D3)>=0.

Write Q0=Q|_(D3=D2). Since 0<D3<=D2<=1,

    dQ0/dk <= -4bD2(1-bD2)<=0,
    Q0(1)=(1-bD2)[1-b(2-b)D2]>0.

Therefore F'(k)>0. Jensen gives D3>=D2^(3/2). With z=sqrt(D2),

    T0 <= F(1) <= H(b,z)
       =2(1-b^2)(1-b z^3)/[(1-bz^2)(1-b^2z^2)].          (6.4)

The exact certificate below proves

    2029(1-bz^2)(1-b^2z^2)-2000(1-b^2)(1-bz^3)>0

for 0<=b,z<=1 except (1,1). Its deterministic binary subdivision has 55 nodes, 28 closed leaves, depth at most 10, and 560 nonnegative degree-(3,4) Bernstein coefficients. Relative-face zero checks prove that the only zero is (1,1); b<1 excludes it. An independent direct power-basis substitution checks every leaf. Consequently **T0<2029/1000**.

For the reduced hA=max(-u x,-v y), the planar inequality is an equality:

    k=1-alpha uv/(u+v), A2=1/k, A3=(1+k)/(2k^2).

Then (6.3) is the exact trace, not just an upper bound. Scaling the actual lower gauge toward zero increases k and strictly increases T0 while all actual moments follow (6.2). This proves genuine simultaneous lower-star flattening at c=d=0. For an arbitrary lower star, (6.3) is only an envelope; I do not claim the corresponding actual flattening is monotone. No such monotonicity is asserted directly at positive c,d.

### 6.4 A genuine positive-endpoint comparison

Return to the original positive c,d body P. Form the actual clipped body

    Q=P intersect {ell0>=0},  ell0=ell-dx-cy,
    n0=s0(x+y).

Q contains T0, is bounded, and is represented by the same two gauges with zero endpoints. Thus Section 6.3 applies, regardless of whether Q preserves the original G-signs or stationarity.

Let W=Vol(P\Q), K=projection_xy P, and S_P=integral_P(x+y). The removed length on each fibre is at most (dx+cy)/alpha. Using the **actual projected identity** 4 S_P=integral_K s+(b/alpha)integral_R s, and the containing-tetrahedron point budget s<=t, gives

    W <= (m/alpha) integral_K s <= (4m/alpha) S_P,
    integral_(P\Q) s <= tW <= (4mt/alpha) S_P.            (6.5)

The projection identity is that of the actual body/root pair. :contentReference[oaicite:9]{index=9}

Moreover N<=(s0+m)S_P, while N0(Q)=s0 integral_Q s. Also Vol(P)>=Vol(Q) and E(P)>=E0(Q). Therefore, whenever 4mt/alpha<1,

    T(P) < (2029/1000)(1+m/s0)/(1-4mt/alpha).             (6.6)

This retains the correct n-change, ell-change, removed mass, and original uniform filling. It is not a moment-preserving deformation.

Now impose G(C),G(D)>=0. The genuine A-based tetrahedral fan gives q<=4r, and the mark signs give r<=s0+m. Hence

    t <= 4(s0+m)/T.

Put B0=16m(s0+m)/alpha. If T<=B0, (V1) is immediate. Otherwise 4mt/alpha<=B0/T<1, and (6.6) implies

    T-B0 < (2029/1000)(1+m/s0),

which proves (V1) unconditionally. Multiplication by 1000 gives (V2). For b<=2/3 and m<=1/8000,

    (2029/1000)(1+m/s0)+16m(s0+m)/alpha
      <=(2029/1000)(1+1/8000)
         +48(1/8000)(5/3+1/8000)
      =3262807/1600000.

The value theorem allows arbitrary nonflat stars and positive-ell auxiliary vertices. Neither the small-fan reduction nor the height-one theorem is needed for this particular estimate.

## 7. A whole upper-defect value inequality

This section alone additionally uses the inherited actual bound 4(gx+gy)<=t+1, together with gx,gy>=1/4. Set nu=min(c,d), m=max(c,d). After exchanging x,y if needed, these bounds and the mark at endpoint m give

    4r <= (s0+m)t+s0+nu,
    r+qm <= s0+nu.                                      (7.1)

The exact A-based upper-facet flux is

    4E=V+integral_(K\R) ell_upper.

Restricting to Delta retains the positive part of ell_upper. Since

    ell_upper=b+(d-b)x+(c-b)y-alpha(x+y-hB),

one obtains

    R0:=24E >= t+b+m+nu-epsilon_B,
    R0 >= s0+m+nu.                                     (7.2)

The second inequality is the literal T0 integral. The first does not assume that the root misses Delta; retaining the positive part before integrating is essential. :contentReference[oaicite:10]{index=10}

Suppose, contrary to (V3), that T>=129/64 and epsilon_B<=T-2. Put delta=T-2>=1/64 and tau=T.

If s0+m<=tau, use tau R0=4r and (7.1) to eliminate t in (7.2). Because the coefficient of R0 is nonnegative, its actual tetrahedral lower bound yields

    epsilon_B >= delta+[m+(tau-1)nu]/(s0+m)>delta,

a contradiction.

Otherwise put x=m-alpha-delta>0. The flux and mark inequalities, weakened only by epsilon_B<=delta, imply

    t >= tau+[alpha+delta+(1+delta)nu]/x,
    tau t(1+4m) <= 6-delta-4alpha-tau x+(2-delta)nu.

Substitution would force H<=0, where

    H=tau[tau x+alpha+delta+(1+delta)nu](1+4alpha+4delta+4x)
        -x[6-delta-4alpha-tau x+(2-delta)nu].

Its expansion consists of the following nonnegative terms and one quadratic Q_delta(x):

    (8+4delta)alpha^2 +(8+12delta+4delta^2)alpha nu
    +(28+20delta+4delta^2)alpha x +(2+17delta+8delta^2)alpha
    +(6+13delta+4delta^2)nu x
    +(2+11delta+13delta^2+4delta^3)nu,

    Q_delta(x)=(18+17delta+4delta^2)x^2
       +(-2+29delta+21delta^2+4delta^3)x
       +(2delta+9delta^2+4delta^3).

For delta>=7/100 all coefficients of Q are positive. For the remaining two closed intervals, its 4AC-B^2 equals

    -16delta^6-104delta^5-257delta^4-270delta^3
       +27delta^2+260delta-4.

Let M(d)=16d^6+104d^5+257d^4+270d^3. On [1/64,1/50] this is at least 1/16-M(1/50)=58885299/976562500>0. On [1/50,7/100] it is at least 6/5-M(7/100)=4300948261/3906250000>0. Thus Q_delta(x)>0 in every case, contradicting H<=0. This proves (V3).

At the requested threshold delta=1/25, an especially short integer certificate is

    15625 H =127500 alpha^2+132600 alpha nu+450100 alpha x
       +42075 alpha+101975 nu x+38454 nu
       +291975 x^2-12596 x+1479,

with 4*291975*1479-12596^2=1568664884>0. Therefore all epsilon_B<=1/25 are excluded at T>=51/25. The old stronger flat-B constant is retained; (V3) is not advertised as improving that epsilon_B=0 endpoint.

## 8. Two durable actual reduced-fan controls

These are new nonwinning constructions, not modifications of the old control's claimed equilibrium class. Both use

    a=1, b=6/25, c=1/10000, d=1/20000,
    alpha=19/25, hc=12401/10000, hd=24801/20000,
    omega=23/100,
    hA=max(-x/1000,-v y),
    hB=max(y-9x, x-9y,
             [(1-d-omega hc)x+(1-c-omega hd)y]/alpha).

Case R has v=1/2000; case P has v=1/1000000000. Together with x,y>=0 and ell>=0 these are all eight literal halfspaces. The lower bound U>0 proves boundedness. The reconstruction enumerates exact halfspace triples, extracts and orients every maximal facet, obtains true edges, and integrates twice: an interior positive fan and an independent A-based fan. All V,J,E,N agree exactly.

Case R has

    V=16415067903001281415600007452095040379789500
      /90174602375141119310903193993197765889079161,
    E=189747805463843456303660960762892371242890463
      /3606984095005644772436127759727910635563166440,
    N=1520902910076974385397492155787175497918538142342173914320314357521
      /13050216235006635954296430846752653192878402233936763733639508079264.

Its T=2.028343714870837..., epsilon_A=19/75000, and all five auxiliary vertices are root vertices.

Case P has

    V=54716146023456233934566920780730628959409231196709887193500
      /300669709940756927346768023753206159460857117326178241227839,
    E=1265008834092464298854729304984368177663308862765370276888770057308513
      /24053360289015820047493198039537948548177264812101215063799176657692880,
    N=9389601416836478520838024118863025775612602176051700204286828165203941243331720552566057343695849
      /80603906014506256509476748884788450514927197850487975288931315944825349085476126160355981340968480.

Its T=2.028598946540442..., epsilon_A=19/25000025000, and its sole positive-ell auxiliary vertex is

    (1000,1000000000,-1)/999990999.

Both have

    epsilon_B=6934639490846/77013333331357 >1/25,
    507/250<T<51/25,
    true (V_true,E_true,F_true)=(9,15,8),
    strict own-centroid (S,U,H)=(4,4,6), physical weak count 0.

In lexicographic vertex order, the eight **maximal** facet cycles are:

    R: (0,1,2),(0,7,1),(0,2,3,5),(0,5,8,7),
       (1,4,3,2),(1,7,8,6),(1,6,4),(3,4,6,8,5).
    P: (0,1,2),(0,7,1),(0,2,3),(0,3,4,8,7),
       (1,5,4,3,2),(1,7,8,6),(1,6,5),(4,5,6,8).

The complete vertices, fifteen physical edges, original first moments, exact centroid, same-origin poles, and all sixty nonzero edge primitives are regenerated by the capsule. Both coordinate facets are exactly ABC and ABD; C,D are true simple vertices. The ordinary B facet really is a triangle with root-based edge n=b/omega, not a triangulated quadrilateral.

Every tail curvature atom is fully assigned to the lower gauge; there is no later unfilled tail atom. The exact angular audit therefore verifies the actual greedy placement criterion. But the lower hinge reactions are strictly negative, and the ordinary B level differs from LB. For case R the two projected hinge integrals are approximately -0.00488854709 and -0.01955343315. For case P they are approximately -4.40e-14 and -0.04396883283; the latter is not a near-zero numerical diagnosis. All signs are checked as exact rational numbers. Thus both controls admit genuine facet improvements. They illustrate why height, greedy placement, and the new small fan still cannot be substituted for full joint stationarity.

Both lie inside the newly closed endpoint sector, while outside the enlarged upper-defect sector. The two value arguments therefore cover genuinely different geometry. The old parent 10/17/9 positive-ell control remains separately preserved and is not relabelled as either new body.

## 9. Exact recovery, computation status, and source-only replay

The complete executable recovery unit below contains the literal compressed bytes of **all four complete source programs** and both original exploratory locator reports. It extracts them, executes the new exact value certificate and actual-body audit, and verifies every generated output's byte count and SHA-256. It needs no parent program, library item, downloaded table, earlier sandbox file, omitted helper, optimizer checkpoint, or random input for the exact proofs and controls.

Save it as recover_two_anchor_v2.py, UTF-8/LF with one final LF. Executed environment: CPython 3.13.5; SymPy 1.14.0 for value_certificate.py; standard library only for the body audit and recovery. Assertions must remain enabled. Run

    python -S recover_two_anchor_v2.py recovered

The capsule has 13224 bytes and SHA-256 3e31da87490d4ab87f03b760347177c782ebb8514fd9429a627aa5ca4b6b1ee7. Its uncompressed six-file source/report payload has 20092 bytes and SHA-256 356f05bb9aa4c0a973a84eb5c1148083d84e757ca20c17a2f9199b9223470be5.

| Exact file | Bytes | SHA-256 |
|---|---:|---|
| value_certificate.py | 6328 | 64548f86f0e62a65b8629c7171295f69ec208d25a71e3fd878bfe4668239225d |
| reduced_star_control.py | 8239 | a1e6d445be10b398dee1d88e6eb3eb5b7bd1f69e82e7828fa1b6438e1558eb89 |
| square_bound_cells.json | 10358 | fbe27af5a284010932ef319c361c8de3366afa5f0455acce872b73be2d2d8268 |
| value_certificate.json | 657 | 22d45edb86c4fa33dfeccdfdb0f9c98d28d542d0a973a4f4be886a53a95748a5 |
| reduced_star_control.json | 61272 | a38fdc443ea26a25c0e455cb76487a2199d0ab597cec82cb2c5ac90ba56ccb0b |
| value_certificate_stdout.txt | 1057 | 24700686a62954b30bbfb3f99e75683c9fa52cf5d579e19c1b7b0cbdc4ec27a9 |
| reduced_star_stdout.txt | 2441 | 4251628b43b1ef7102348ddbf7d7bfaa964167073a127843e18d193dee125448 |

The two exact units were executed and cold-replayed source-only. After the final cone-moment and coefficient-stream additions, the complete capsule was run in another fresh directory, and all final files again matched every pin. The final recovery stdout has 1247 bytes and SHA-256 3ae8c469eb8602aab17a4523c4c201397a99846dbed9257c1ccc0b344d582e92. The required terminal marker is

    TWO_ANCHOR_V2_SOURCE_ONLY_COLD_RECOVERY_ALL_HASHES_PASS

The value program prints 55/28/560 for the exact square certificate and the rational rectangle bound 3262807/1600000. The actual-body program ends with

    REDUCED_TWO_NONFLAT_STARS_ACTUAL_MASS_AND_GREEDY_CONTROLS_PASS_NOT_STATIONARY

The analytic geometry is proved above; the programs check the finite polynomial algebra, the entire closed-square certificate, and the literal body controls. This is not a proof-assistant formalization of shape derivatives.

### Preserved nonproof exploration

Two preliminary scalar locators used CPython 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. Their complete programs, all bounds, seeds, tolerances, iteration limits, and original best-point records are embedded in the recovery, but are deliberately not run by its proof command. They are reproducible separately as

    OPENBLAS_NUM_THREADS=1 python relax_locator.py
    OPENBLAS_NUM_THREADS=1 python defect_locator.py

The seeds are 5171 and 5181. The first looked at canonical/root G-level inequalities on necessary scalar data; it supplied no body or exclusion. The second approached epsilon_B=0.04 in its scalar relaxation and guided the stronger baseline-plus-flux case split. Its best reported minimum was 0.03999999996016901 with a small infeasibility and unsuccessful solver status, **not** a counterexample below 1/25. These floating reports were not cold-replayed or promoted to certificates. The exact geometric and polynomial arguments, not those solver statuses, establish the results.

### Complete runnable capsule

```python
"""Recover and independently rerun the complete new source-only handoff.
CPython 3.13.5; proof child requires SymPy 1.14.0. No parent files or downloads.
Usage: python -S recover_two_anchor_v2.py [OUTPUT_DIRECTORY]
The saved NumPy/SciPy locators are nonproof and are NOT run by this capsule.
"""
from pathlib import Path
import base64,hashlib,json,platform,subprocess,sys,zlib
assert __debug__ and platform.python_version()=='3.13.5'
assert len(sys.argv)<=2
DATA="""
c-pNzYjdN>uHWykV0Y^l4>t}k<5!rfJUoxBOfs8fX7^mjMPY+u5)1^e<78_7`<2vyapLUmIeU_c-
E>Q8wOUfEyTyF}*$?KytZ<`b<`qfSzRQ#N=fTh4Z+@O7ab9Fz7#I1?&jVqs8f~p_n|8Nr_xo1Q)NCtIb(;xVyWi=Wy?(FT)wFKk>
N7#r+gevMI#!>W?2gt4SQ8rTwx;zpz0=XUmS*TZ1L}38(KY)WTQ~Y<A9{fA2@`I9UWReFTrIJGt*x2;^2gS68;Br8zM9Q~oH(3&Q
66C3hWORm(5tESy0)qJ`(~$aU^f~Q-WrF#+k<Ws0zh@Gu4VTPQ@1U<Gx>27|IA*BEqwx^-O%rOfDC!rlbX-
G$jgLalSWB~U{6AnJO-J-
k%ba@D8xx2c)~RCpM)e6(kw~l?VI?^Q?W>5!EEbhyTgR@)$+>|Fi#Ixvk)Hiw%)}N<w4*J9lfUm7H8rno@dEYNWEeag;OD1rb$)^
U*Pd3E+25F>xX!?OrHcV7vi);&1Yfy)K1bOT!zm<MS&&+o^Rr7r=uSjott=?tYSZR#*)@%dRu1rZS@ay&3sYTq1-
v>QmxMHwmi9sK@tKgnzWGzH?c5fOSWbO%bd+Hcl6d2>aw6%Wic?;_Oi@-
lEzDQ%`7ETua%<wmh#rJwU!w`3s{zwqLsJSDzq~ECRk-Tk$H#nRs6cYZBIpOisTUc;QA)c;#&tg&%D@AmTkcIR#D+Xt%MSnhtnW0
obx0GnapAK?t~C1dGT!^>6%8pY@9KGw^wlp082?@y3BSf+UBd87ce?Ab}K*&^mYejC_FpWv`8>CwqfOz@GsUdWM}+cES}Op9Ef2Y
JcvvL1aW{6KPGG$fWrBXcy)I5+ZU1H+(U!&U7Qz5Bo1^i6N8CMZxa?lCJs89_5&m;gmY92iKg+ny^-
a2jta0n0VF0!C>|lq1(XnK_j4P%Jj7Zo$O97J^G%$r3g~GgQbl{yhAzXrkYwnPI{|Spj}ottYE&jRM#cxh8#i(TyL1phH%TJiURK
Fq$(i@)pdqw<Fo0YFCRh%7?%oGaxpSSZ0=XsL+{EG#O-
B;<I7?A(KV~2hw+J?c1oY%#ngK^tBv+9I{%RKZZeDnq3tSdi5;Yyh(X3c`kx+uEb1xQ3sGN~&07RS#a47-`f9atdi$xaXizM>VZ-
hY(rhoFnV*p<4dzmkQ3&;>ViK8d<HlU*Esu1R36y!*Y>o%`_=|bk2HzPf$T)_LX0=>oi5(pKd0QuHHvt&69V`4imVHRHA^hNo?Gd
lL)_ETP-Ll=VU`oVN{>$=>MJ>Qo+HkAjJ>8{c!kT$I+0Znnkp3oSd!<2wZ>(5uyeK_i$;Vf5?G-
KWioSCxWIEdkupng*9kk403N!lp;sk8TzR`oH<l04r*mAtV&QKn;KqI&QFC4Iuml7@8}Z)Igk$2y(2R@?-
{4V%?OIe)w}tgob!MC(AxlE<87i=5onse{-G)|F<C%6M84;x13vkq9A-
c^Sxz!wI6@JI<XDz~U?*EvOvdPe>g1TVH9)GF64ms)>AXD!g#2X2tPh6-
9=WCTRV{Z<;%3yMZs|z((0152M5xPlk&SJ^=_Zk>M9ok!p#`iZrVvDXUT~RjRLGfDp2kB3o&WoePf(uqGi2Vkt`GcRD#g>L^Mebe
b^yg6T`;Lq{7#Njpta3F$x-(Du?ah<z#Dp_>KkAj@GiDIZ>=hef#4!y=>}@T=}&5pH{ca<hkW$iUD5;9G!(-
(09cJWKqbTpeNR!aR)8jm)5qz27Qzkpave5I>w1HPm+myO#$g(KVmpd$z{mZQ9^8mbrvp_!Sw6REVJumuqt4T{@h~WIG^O!k1olp
F3Rt_~(1zb8Dojyp^v6t1SFtIKpU2#)X-
lb*e`_BPC(J^Ip=?R&8c<@LOlFw8P>~MT3d}8#$gj9WG{$2LZ%vxbUgq50hnZ>j4SFL^Oa5qR5H7<<$3tbl|llU-e`q1-
)uXGhRfUi{RUU;l=S5croK}3!i{);uXwm2C<j=Ug{G&;8P^xmTKTZ(p6t27L>(IKJX$KpE|2*e5|PgF>mFEg|uGN<Wr=|Df8i$&I
-vxSp_hZed(7m0KksC=-|D?p`jP~ohJMud_{Euy@;NKG|9svTn9seVw1p+VI6Lx?M5CHp*!l2cUAUR_F8sZx0aui8d+#L0^oy-
<xnL+)9=!l_F_~B`Yr;A_Z0#R6i3HEavTLA*5G}>?NlZl`Z*G4u7eVHU_F_c+@Mp3d)+aoj*d~AY`q|mn6O5h{-
TX+8!RWq@Cscsg;?knyeN{;&&T8p7K9eF1z7-
*lLza(jf*EagmvvW*SS2Ldo!GgNjZ=mJYqY<Xg}n<Ffye8whsa9Z~`QNELEL5&I0KOewL(8i~-
Ue_vdW0ix(5xMjm<_?ELPv*T?p|pB$t_B$ui4otyZYq;ogf;vf-u5blTz-Hb4I#>;e^PPSfvuOiEo=CIOc^s#dYV@;AKPU{?og5N
->5<8BOFQXVy026bVp$VgcHkrt*t~Q$0GK=LyZ7^?_{++w%duQGb!5}sgTGCuDr=jxOe4z93{b16Xj|cY?bWTFx-
v;&6mBJ{W05+Vk`B(~Dy8OR<Jb=WNdyWGq`Y)GU4k+`mKAt(>gF!VHY`!~Vgio`AatT1sxSY6b0|G|=er%ltswMBiaf~e|&{2EsM
XLZ719=NgprB6-zljtt@{WOo)Mt8!^$=wl`py_snv1aM<!MD|I4WWiDc~~B=M<2~19Kv8C!5-
JZ2yjp8f=Z=OXpwa<i(IM!Xp_5FNO~I=2pUpYYZmxF0yv$z;Ym=o$6bz*Lef%FKmsYJB~haK)Z?E#(0|pFeX3BS)u_N<&c{o<}Qf
YWOrL_Ph=2vf$B?J0Tf{+EPe8WsMb@3&>)C6=%^J^v)e9pOMy4wNC|hB>m+i}r4N5~_+lU{=5XYkQzcn9Y7`Kt)tk^>Mw)u9MY5`
M%HWD|Z=8^oLIaAhF5frHEimy3M|tGoF<F1gl7`L!v9S&_Eg#q%v>f>3J4fRcFqD?_2m?VM{42xl#p8j+N)rZsN-KX>5tR4D!DKD
)GXh!)VsTa2#XGQu=T&<g?`cLFWdsFmv0vGUokLyXyu}UZ-9c%adxP_)dh>-
Kkq`GRLIC=W_ve)JJgjWLtOv!R7P8_p@V<3WT>1fk$ivJzKlnC$fX~tJ8a^dk`KFBI;n|TRWvvJKz#N_(Q&E}11E7D{MpGmXHB%o
HF1Ri0BggqhmABkP&hZ(*ZwY3#sn@?<*9j6KlMHD&<~IK#NczB+tHx#r$h9ip@DB9@f}|b#08rUE$9<<E(O-no#-
me22x`<t2u#2{mYa1ZpncwgpMZJ+H|zY6Ve^E?i+9{?G4LY1?P@;{*(^yip9jbWg~JfG%G^%o4!6&FI2n@1-
Z8zqS2ngauvBBI&QinSL)Z>Z!c`F#syq4s^D33v%N%c-OH!)irYqI>&MY-BG=?YIn?YOsL~S*sd|(ijTae_39i5jdPGr~<LTfsv@
lN(a5Dgk=%keUWY~ePS$(CS~+(PZX%^4Ks1Kr?TEf{{aY7?fsJO2a#0RT*&C)|QF4<TkN9uqYWAspuTLJ>v<o`qz|8rJA*oTn)eb
m&ZLzx!--6Qd%I5rF~@$7xjPR53lE@E@%_^FusXa<c#!01a_I>>#UW$6La$fPW%?Rw-hZBy_CfCy!(_)1+A78B}%NowtQg@hn>Tf
q<dU6D(!xAWG7JAAP{caiCsN87LlevSNT=c)n4zsH9I62*3**?`#EL`+K=n&}kz{I!uwbM0UX_f-kifXBa2;RbW2PnNcdLAH+_nb
6mSnt6HRY)Q*8)5SOdQ#;G(CVdVp8;SB(#9c~Ww0kTMe_NH3V(h%<lB;H+7hi?cd5AhI`Y>}9axVOa9q9SMIqQbi_94TroDm4#1a
Fd&Ie__b%K6t8xcsKA0E($a;*i8?^X#?1N4NMX%fr&aWRcW*YEV0mI;gq+P>jprSqdPs7s2Pxn(XS5fmhe0tcbzhyx)$thYpy~Md
qUXX_ra<hmNOMjE7-
E*sq$6*y`1)%HCkbsQuZU}FPxe+*tON=MIFsYiobxkyq>VAB`wrQR{ZEd@*~w>(1_FAsYnkq+^<5f@}BN<q*?b;&J~zF&h00Mg8Z
mC#~B2-I4g@6l@#V5IVc4>NF<h|9pObF&*t+&-pdeCI(Bvm8S0K~BYF4vPe_$60eC}_Qhi9Etk?3v_OS(z<P3u2cXU|NA><-
imRrmm9YAgI16&Q%IX5=yIhYqL3vU-iWeI7{(uO6}tT_lejNo~}?mTukbqI~-
KX9m<$__m6Yt0IfnmqLHA)agT>e2+JHC!zcxv@)x(A^K<@4ix@`vDECHkJkR1Loh;Bo<y6!D_QzW(btF?=a*;=M!%Iu?@c8!IRz$
;wh2}9O#PhT}~INAX%Aw@KF>A-
WndgX%tXB_{VJRft>`xZ362^kqE^iD6b%Iz13|n0Ll<D_)o%Z76kqi`rkjCF^_0(<z~o7hagFWn{yt1fd=v5?v}Q+ufsdS$igM8D
c^q#X>Eb;)SKN0MdN${cS`k+iJvd9I|rYJbGC3`b2!F_2|qBwF8{!-
E%NvWdMSJYua;JAcU4=6ZFgln@l35WfbpC|@Q1~ORkc9nxe2#u!p$qVMM;qlZ4As#oOD<|-LVj!QX1_T*q=Dhyu4s@C_fV-mq4v0
I65W)FoaquOH=mDo}cBHfi!J2VZ9}p(E|6(Wgf6OdnT!Kx`?;JlT=WHzX(&2=JO#ZDc!Mqxg<nmsg7sq+{JN1iiX}K+xs(uD1rUt
z|kVPVDCuiViA1ebLlr5hclcHxrOCwu(C=mL=q1ewixfFj@AX&qsfQYhwxCjp_!Muw<|C6X+fMZSbL<NZfgqeBJg0eWoSnKK=N9A
xkGq<;QC&|meS)%daJ@OVGm&GvXm{+l3Zg->#h%Vevp5CSW|DZm<4zT=6n~|Zt7*;GN7B+^_q#?$ixBvW+FsXML5HnH9TQ}h?k-
iC^C_ZOB~P_-ja*7p%MoWJTmc{IQYiIU&X<%OdN@W5fjhF!8sFW0bW9ezBssL;<Y%qCQQ&-
x>|8(QJAI>wDEC>gL+784@{8(BYb!ql8QtS84ortY;VND_~i~391p7?K0y12SFK2*I#xy^E^L>=D1<N-
WRt+yF)Vd?SSk)a0dr{{MoH`*fjo}3kH_$MOw?+(>5`8YxmRZ*`qZil%S<F!>Qc<^)>|)eKovx)j+l?@m{}aW3Zr2%(X}AIQ8im`
X#`No3q+4=x?9aIe`I210`67`swyUOi*QR7;7`!w;wcYjUgSOo-
n~0ZR&gN?v>)7O$Au)GT%2EDUYv;xmF?T;y~zIbJPtJE^5|qFGJZ*a4HaK5uH4ZXP@rkJ`udTRD6N(4*e+|>uDoU9^Tp@U`Sq2^z
Ts&A6F+`B|1g3_zKhyk{ctnkNd#kljZt0A!0NQE&^1Nr(|LWvnE(<jy5qOB2scbxeWZoJ`kw>qJgq=#<Q0@RSAZ<P$S+`dfQDTp5
KT%VgWrKDmq`b5yTpT$^8ACnsRTP&2-Bw`$jjV=QizwMFBg~BT=>|)_|-d=+lyf1hcK4~oxRo=r(aJ-r|$Ld7w-
AR`TMh@YxnB<=<>=vI=TLObmo3Ox`Oigsr%t_G&=p4TPn+y`vn`$F9`hl)5ZDG<-
f!#3nKD1FVoD%xFCM#d#2YJXS`m(Y_guw?HP8r+v^#6uWNKEYpiN-
q=t2EL+jXPmo;$Bu5O#QZuT_IH2a<Y4zAwrcY1)`?b}+<)Ox*M-
DI?lo&`wg>TRp5n~e?u9)CKzZdw{}w694s46}))T5Y@2@0yy~?VG07!L&2&-)Qai`g*5t7zT9Mvv-
=cb_d%ibFJ4gj9!noOjsq`+r*0~jjpbFl{r^6@U!^c82}O6T{I_Cx4Txy)EW|Qv~_zn{OLQ5x(On(`-
asw;1?$7C2O0Vu0VkNr#ZcK*=%>ZwyhghuWK4s_tj)J6am0`%_)QRzxvU2OY7`3Re66_2eiO0k8LUD{K5X7jv62Z(=dCM-Rs++XF
OY~F$PVufbV|S0&RjR*390n0(W}djs|vV88&LwUJcbOqi1*aXs8Lzme$*=hMLy5?e5=cQq6YHwhfprTkCf$+v@BL;-
57)bhO_$K@;9mQGK6^7U(PgriQ}MFyYf?f48wx(T-
v2W=HSX|3pQb<z`ALPM_J`)jCiWn04FIJG~u$2D+*PuZCrIy2z~cpDCoFW6mm=NyqHaZ0z_<4K)o%3_>wY(8(Qr#Jt@uI+Lz#+5N
rRXmvV$YoEU~E!)Ht+r2smrVIVO(PUfOu5bjv9C#H2M4(xgzUvaHx!37*Em#$LJdO8Na~I~*0A{RC?=6qn16_o{zNL=FKlYd)#J&
c$&E9J4cFeu%2&;hB)BAtZWA;ihcDD|~Zd))q%htf*k+3KWd)wO8dKS1s8?B;anmerx-
R*T@j$Y_)uWw>fv~Jpcd)JrhnvDxY4;Ea|s;1`N#FIU-Kr?qbi7ETJN{z;w3rwF5XCbDK#8qmwz*DPpN@k?I=`b(1R)PO-
q)y|Bbh?7ACcpX({9Kp@5Y;!5Aa}A5|1w$eKggp#`dVdDA76YuKfQ9sQd_fVnPQcrq2#1(Qgt(@nlEToW;KW(i$-
s!T;})8!yxjvsn)PJWd&QYb(L(5xl1|ET*_PiFm+a~_3*&~4wYh<Ig6RH!px)fHtuc^VL4mO*urNidte#J?{#kX8?a8z7ae5%iaS
TT_+{kv1-hWYv-
$wc4zIQr0iNusNgOcYgOG=}Sb44C4H@CJ_hpS2E!>l*tborIeex{w2WBb{lqpX4H$L450&_De_&mcLBp`ugT0YM)uj^)%Xb!b?jZ
ZZ*nLVhcl2&P$;2{1zF+^T<e~CAqGpFKfc<VbAYtZsYk_dc9g3f>in4+}`Q?!x~Bx0bkN0M%5YUHt7A3rNZD9hDcEnyMiC+2^a^4
`@O*A%!DM?cxT0j4v&MpFFi3-~fE9`8@K^RtuNj+)<jl@f3KRSj4}hZ!%E>Cq0_oxOGZJQtH+w<+}HS@dS0ma{g-5l*&g_1sJ=m-
nA$*O%z~lI-
<HlD$<X*$X>q_Q3Eq(Z0Js(H>#;q}oGud0t&1RH<Ww#zoI}5eF>}@RRM$%I9mIIG|^eRGEAKU&zZRt^KRae1^$Bap4%dDf+MXnSY
U?50Y@**jom!>o}t8q8YfZIN;_$>lKaFo#EliJOsi)bIp1WiUY1GpgYh83{S4Y6Zbg43sEn6D#95q01>w1tnbO$zj|8o)yZmWw7T
WVDw_odzE^n7w0&y($9elp5Lq*2|Ib#qKTG1@_exRzR4#>Aue0|_W3SpS9$4kT6N#P=TD*y;?Af_$1O7AtwGyYoGoB%Qfx0hA^dw
!iAtV3-bOwvJgj3~Nd6s#JmsO0d$_lvxQB2THppEAol-
&9~*bLrFs0p+3qAS?289J&jZ7{wvIr$giI*38_gySFswGQa=IGDpEhoFABkl>9l-
k;=x$t;XmaLykWNd!w*l;i<K77r^g3t)zho$;8i-
)72t2?Z{NcuGzs6H0PbeTTP{RI;EXSK(Ee%_QAZGo6*=NScT1_lHi%Ppb}{yJik-BR!)dPhKA2TUC&dgL)RyF#`w0^Ukp{0)Hm0%
NsZEDZs1G_2fm`JJn+fy8KS({{7L}Rt|Zwaxh~$DL>$8fF7Gx*L#obkuLWp&1>HAx=M_tq;F1X!k}8!8})U@JO`jF2E3JkkvI-
#DfL3+oyL<Tk6bcPK=k8Dv&*#VlBY@`9%kcKS-6ebn|OyTcZhN$Ngc<f9LtSV^>GRG0!G@?sVqacZ-VQ4z;EzSb#@PNq$rlz+RdD
5OmqfjhEd?HDbaTrCq5Lk;d78B{AP~NDv_Z#E5HH3>bGGh4%P8j3pid2&pWHdY3ZeSx6Mv)ZPG~MzX(U*s^U1f_3*s3VMQqzbDS(
g2p`s79Oesr8428zfG(V1p-
W2S<8;Ww!Y<%(5yWK%$zGGhTqndPOZ18|B`_Coc<m}4@m_^2LKr$Ie$*H|@ue45#%5Jvly9(<)>3B{&R!D|?(Ql|vn?g7s@S2_k?
V{RygfVNsmxA!(Z`dQ!>#?^-
Bo?mmxDh!{03?E6U_u=GhztsNFctkcW_`#aPG!NYldZc7oCGTcs5?OkQ&t2lQj1pe^CgGpOj{|krYFghj<<x#;aiWst!TqLkkmy$
Pnwg|22kZ?9$=>=7js3ronRc@hDsl9Oz`YbiirMz-bKO=?os&65C{aymX``2c<*@5b!>9zZEpmv29tQ<KvQ}b0u#MvL)&w4)l^;!
btbEYt(+m&gi|7GSd}ZJzYd73XQw;3Mq4$OP-9xS$b)@Irs&3q<(;eQIq{J!xx3g$*V=8ZuK3)t2oC{mLdt-CzC}0MSORddcnylM
;XZMWZNNszhg!>@?{iXE-7F|uU3^hd8)Bo+_$RCz86bNR5$P*_ysu?+qXd>!Gc$<N-
gY7p+)YVg)%Qi(5!fhBHgPYzH)`{!ziKRLrtVYlN4Zzka7oIoSf9FDH8g(7Sugs<~;tFR?^A>fJf&9XZ1@25g@poEb!Dc3!rh0nV
I}*Q^=zbT<M?;A`ytc#{n)4g84c4b=VOnOHc`z+m*&vI^$W2YmKdS7A>3c(n=Fnx{zu@stapPSnEQx!~iPYIH}f(mWs62)RhKN@R
O73yh2x3X#alXtTZKkf+r>24E@YWHwrYSPs&=W)w&MAuG)S$pG$t!@-
tupRT!XvQOA!IX{EJRdMn+u(kB@JV7bC#Ypu1`y8I?Fzy?yxD2e?doRRWV9^o9;g(8SSa03dm%A{7hTo$<1&=PXbP7QWyV(=OAaI
AW#zHDiV>s~lDgi{kG6t9+!-nv%}2qW*|_tYF>J|M-9@MP36COzE1Y{x+cR%C2LO-Vlh+c>ya6azdBRGyl!7spyG69p>LLsJSfeD
y7oN|I_t5Lm*rLN1KooR`vqX3%m4AXF$S)r15wqqL*nH0L+iR!wv1)MUi+OR4{+{-%}Vm5^OYhp-HIQ-
G>;YN)_I@B0;^#tGlU!oj(%<%5J|8sA>blF8pR;IU<qBvgS*1f&Mo@DG`wd8pOkcM7O)1F!;oo2>dj6lhN_Tpwbxg>Li@Y>OGK`c
7YlDL;apd(2LoQ+_0DgjhHg<zeBi9HVtQ1Ptf&CjR(pj{yJ*eQa7sty4uZTc>ghgmem1qhdW^QVNKr9Kqiy{Lul9pl%e&R!!wpJ%
vALRXG(94&t^dT$vpKdx+EAfPAbrAmw|Q!3Nf7{+{CC^*T#=H}81JKp8aUC}!+bZbPF>(NXEvo_}&MXZyip4^#Fqt492>?d2{EI+
J8RvEPpd8jA<o4;i@Ip#pv)%x75$k)8*^!&Mt1EZA&Imh#{!4>R>)sys}$y0!!CsJgA3DvGV@nuUdqYIM3-
uvDX~VZm$}RAICXTSM91VDwn!2>Jsc0Ly{hLIP0ew2%N4tQHc0f(e%CrMg2m{<f?FHm$-
PaNt8|F&uoAvr{#6>9x!)zZl3OK0{D^g%Mpb>@+J#)xb1;Xmpw*E6t2uwJ-VG`Vmie+|or1r`g=Gd$w)$dZ4nFrCXW};O|J;Kh`I
l<-3#ko+R;6C6A~_ly6OG<4}oluUF>uXY8S=?3wT&HeZNn7-
Ttb5}hYbW%UeI`0NOZplwrC2gSCOS6J2V8;k+$T<uiOPnDoJRd)mc<Hw0?)LB?p8TEC&Q=T3=#(~L%<)Nb=^kDa1zbmR%*+c@yLa
@X}xRd@&vx|W8Fk0l!XUajfc|z8Esl!aU^;yQ3QL)7HwHkAQC`iG!G?-LClMi)@zP`p_UVg}#MZw;JxFeM>G2GdN<-
VfH4z;{W3;PWIt*3l$FjO<Z5dgz9Y@=5)QNBprfN11`Rj<a-
u8Wd6s^}4Y9}h40Mwd95oend4z}TJ@2h;+VDw=38iN;Lf>&iH(;D$3yY15PvsGL5~%)ndXp(jR~;vi)rM8M);%-
;^*zI6??6DA%*%c~~XdQX~r@RP}patySq*p6cII;n>D{~zYlG<GO>3<$BeW_I|0S@K4DjN^#&X<&4{dB-z)mZocc(+K9K-
k+JaKI{2`Y1+0o_d0XD8TDqfpw~5~T@#Re!|xe(PptBI_<@j1Q|!VdMEToUJaq~no>9VRFe&Hg{N&@srTg*IhmTcxba{03^>Rd6I
aSWix1+PKBll`_a(!`m<$lxY)LE=I5iY5cIN%!9sOKUV2TdizBWV|6ES%}TP&l4N*Ek~+2ZpBX5Nn(WxTP>~+v(;(0Yk+9r$nGFs
rZtX%V(WSh;v9eP5WT@M2dqqCX`51uXVoSPMV@f*`H|4phdN@yHgj2kF5vhPW`g1=k5!d%Kt2eUX)yWkqiDmFRcTY7nzkML!Q*YA
POH}+L|FWCioGA%(nSv+YZaTON0S;ChulKZoziOgutYAZ;-4yt=x{vfq(GSx~BDUwfslfY_E^i_ZR`@%+-
l$SHFEd0v)Ft7#F9<z4$h|ba9T{(H}=A*Y5G?^8D(0^y!>Z(M0yzTkfjjmiC9yIoQyd`+uX$3wLyW`sL!&`E`}>c5-
n(a(Oml+56Gihtcun5$|S8rG!T#{c?5$NM{$n1BaMB_kuE7==JFQ)A@(DX#M{2;%roLa5{Pqc3hhD*|q!m=nq$~1YldP0sVcwaz|
gTKAl~hyT@-Z_T}R0)Agrsqb(noK=$bT1N6jckN!9TLZ2=w333hCn@z~`8M$>~d2co$-YWS4pLvFFv5Axs_~U>6AC*UTdj
"""
raw=zlib.decompress(base64.b85decode(''.join(DATA.split())))
assert len(raw)==20092 and hashlib.sha256(raw).hexdigest()=='356f05bb9aa4c0a973a84eb5c1148083d84e757ca20c17a2f9199b9223470be5'
files=json.loads(raw)
PINS={'value_certificate.py': [6328, '64548f86f0e62a65b8629c7171295f69ec208d25a71e3fd878bfe4668239225d'], 'reduced_star_control.py': [8239, 'a1e6d445be10b398dee1d88e6eb3eb5b7bd1f69e82e7828fa1b6438e1558eb89'], 'relax_locator.py': [1644, 'd3b9ec201a595982abd75b3bb9bac47cfaa867bf93c657a13192649025aa7844'], 'defect_locator.py': [1014, 'ce290c4c587a7ce35f19cfeb10d5ebcbda7aa6cff0cc23c8bf5248b469c08a3f'], 'relax_locator.json': [1914, '623e8cec119e27b9af3416e8d3e82d966d55a2ba1799aaf50f15b67f362a44c7'], 'defect_locator.json': [277, 'fb1b11bdf4a848bc8e7b1b3a4adf9ccf03b33ce8cefbe17f5cdf6017ea161c4c'], 'value_certificate.json': [657, '22d45edb86c4fa33dfeccdfdb0f9c98d28d542d0a973a4f4be886a53a95748a5'], 'square_bound_cells.json': [10358, 'fbe27af5a284010932ef319c361c8de3366afa5f0455acce872b73be2d2d8268'], 'reduced_star_control.json': [61272, 'a38fdc443ea26a25c0e455cb76487a2199d0ab597cec82cb2c5ac90ba56ccb0b'], 'value_certificate_stdout.txt': [1057, '24700686a62954b30bbfb3f99e75683c9fa52cf5d579e19c1b7b0cbdc4ec27a9'], 'reduced_star_stdout.txt': [2441, '4251628b43b1ef7102348ddbf7d7bfaa964167073a127843e18d193dee125448']}
out=Path(sys.argv[1] if len(sys.argv)==2 else 'two_anchor_v2_recovered').resolve()
out.mkdir(parents=True,exist_ok=True)
for name,text in files.items():
 assert Path(name).name==name
 (out/name).write_bytes(text.encode('utf-8'))
for source,stdout in [('value_certificate.py','value_certificate_stdout.txt'),('reduced_star_control.py','reduced_star_stdout.txt')]:
 command=[sys.executable]+(['-S'] if source=='reduced_star_control.py' else [])+[source]
 run=subprocess.run(command,cwd=out,check=True,capture_output=True)
 assert not run.stderr
 (out/stdout).write_bytes(run.stdout)
for name,(length,digest) in PINS.items():
 b=(out/name).read_bytes()
 assert len(b)==length and hashlib.sha256(b).hexdigest()==digest,name
 print('EXACT_FILE_PASS',name,length,digest)
print('TWO_ANCHOR_V2_SOURCE_ONLY_COLD_RECOVERY_ALL_HASHES_PASS')
```

## 10. Continuation-ready residual chart and limits

Every remaining all-positive full-class polyhedral maximum at T>=51/25 must now satisfy all of the following simultaneously: proper33; two nonflat stars; no ordinary A facet; at most one ordinary B root triangle; at most one positive-ell auxiliary vertex, of ell-height below 7/10; root perimeter at most five; U>3(x+y)/(10t); epsilon_B>T-2>=1/25; and

    m[16000(s0+m)/alpha+2029/s0] > 11.

The tighter endpoint-sum and individual endpoint inequalities from the new source remain in force. This is an actual small geometric remainder, not a proposed completion of its moments.

A complete parameter chart before imposing the remaining reactions is

    hA=max(-u x,-v y),                  u,v>0,
    hB=max((1-kappa)x+y, x+(1-lambda)y), kappa,lambda>0,

with an optional third upper form

    [(1-d-omega hc)x+(1-c-omega hd)y]/alpha,  omega>0.

That optional plane is ell=b-omega n. At a genuine stationary ordinary B triangle its root base must satisfy

    n=(4r+qb)/3,   omega=3b/(4r+qb),

using the **actual** r,q of this same hull. The axis guards are omega hc>=b-d and omega hd>=b-c. Irredundancy, boundedness, root area, the actual ordinary triangle, and the true facets/edges still have to be checked; an arbitrary parameter tuple is not automatically an eligible stationary body.

The four special hinge integrals must vanish. In addition, for every affine h the full positive-endpoint root reaction remains

    integral_Froot G h/|grad ell|
       =qV h(g)-3(X+Y)h(w0),
    w0=(gy/[3(gx+gy)], gx/[3(gx+gy)], 1/3).

These are legitimate both-sign root motions in the full marked class, not fixed-lattice equations assigned to a zero-endpoint boundary. :contentReference[oaicite:11]{index=11}

The useful next step is to impose these reactions on the seven/eight-plane chart, separating the all-auxiliary-on-root case from the now uniquely possible positive-ell auxiliary. The supplied exact controls are immediate tests against a false identification of greedy placement with stationarity. The endpoint clipping estimate may also be sharpened by retaining its beneficial volume and ell-integral factors rather than discarding them in (6.6).

There is no asserted monotonicity of directly flattening an arbitrary positive-endpoint lower star, no replacement of the actual root polygon by a free moment tuple, and no identification of the positive-endpoint root-only-auxiliary class with P=conv(A,B,Froot): C and D are still off the root when c,d>0. The whole surviving endpoint/defect region and its full root reactions remain unresolved by this handoff. No mechanical lower endpoint, attaining upper endpoint, or registry count is changed.

Supplementary convenience archive: [complete new sources and exact reports](sandbox:/mnt/data/two_anchor_v2_recovery.zip). The literal recovery capsule above is sufficient without this archive.
