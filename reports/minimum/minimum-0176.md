# minimum-0176

Historical AI scientific report · saved 2026-09-22 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced; runtime-path-removed; unreviewed-encoded-blocks-omitted.

---

# PROPER33_NEGATIVE_Z_HIGH_TRACE_TWO_CHART_REDUCTION_V1

## 1. New result and precise remaining question

The positive-ell auxiliary-vertex complement has a much smaller actual geometry than the previous ten-facet overcover. The following is a new analytic deduction from the accepted full-maximum premises, not a conclusion from a numerical search.

Let P be a polyhedral local maximum of the full marked-body[private-runtime-path] problem. Assume a>b>0, c,d>0, positive root area, all four canonical marks true, the two true maximal facets ABC and ABD, min(G(C),G(D))<0, some material below z=0, and T>=2. Reflect C/D and x/y so that c>=d, hence G(C)<0. Then either

**P is root-only, P=conv(A,B,C,D,F0),**

or all of the following hold:

* c>d. There is no ordinary one-mark facet and no free facet containing both C and D, including the three-mark BCD facet.
* P has exactly **8 vertices, 13 true edges and 7 maximal facets**. Its root is a triangle. Exactly one auxiliary vertex U has ell(U)>0; it has z(U)<0. A and B have degree four and every other vertex has degree three.
* The entire true incidence is one of the two charts L_D and U_D in Section 5. L_D has the genuine maximal triangle ADU; U_D has the genuine maximal triangle BDU. There are no other positive-ell-auxiliary possibilities, including nonsimple auxiliary boundary cases.

In particular, **every complete negative-z class with a CD facet or with any ordinary facet is root-only at T>=2**. The result includes both mixed and both-negative C/D signs. It does not require d<=a, a bound on the number of original integration triangles, or an independently assigned G.

There is also a new necessary endpoint-gap inequality for every non-root-only member of the residual class:

    c-d > 3(T-2)a/(3-T) + (T-2)d/T.                    (1)

The parent already ensures T<3. At the target threshold this yields

    T>=51/25 and an off-root auxiliary
        ==> c-d > a/8+d/51.                           (2)

Thus the entire closed complementary endpoint-gap sector is root-only as well. At T>=51/25, **L_D is necessarily mixed**, G(C)<0<G(D). The both-negative and G(D)=0 complements can only be U_D. In U_D with G(D)<=0 one additionally has b<47M/68, where M=max(a,c); if c<=a this reads b<47a/68.

Combining the new CD/ordinary root-only theorem with the accepted actual root-only high-endpoint height-law theorem excludes T>=51/25 for the entire specified CD-or-ordinary full-maximum class with max(c,d)>=a, even below z=0. That value corollary uses the inherited height-law theorem, not a new replay of its certificate. The height-law source explicitly covers actual proper33 root-only bodies, without stationarity. :contentReference[oaicite:0]{index=0}

**What remains open here:** simultaneous full stationarity and the value problem in the two explicit seven-plane charts, especially U_D with both C/D negative. I have not proved that either chart contains a full maximum, nor excluded both charts. Negative-z low-endpoint root-only VALUE remains the separate direction specified in the assignment. No mechanical E17 exclusion or new attaining construction follows.

## 2. Reading, source authority, and one arithmetic correction

I read the complete new 2,423-line journal through EOF, including the common notebook, branch memory, both literal parents and their source payloads. Truncated display portions were recovered consecutively in smaller windows. The earlier unchanged journal and earlier result remain available; they were not restarted as a new research task. The complete earlier supplied source, JSON and stdout were also read. The csS2 encoded payload was decoded, authenticated, and all twelve decoded units were read through EOF. Its inherited full audit was not rerun.

Mounted new journal: 340,819 bytes; SHA-256

    299b953c13aa59becaad7a4237a1a2a5f01af85c95f6d197dc56034c85aaa711

Required literal authorities:

    minimum-0174
    75a778882cc680e10036501e71396ca70222ddd9ed56de6b5aa1fa5aa66759d1

    minimum-0165
    078f5b8df8a0c5b0ccb7a22bc3fa7aa26301717b0635893ed1c728e9efffebeb

The first parent closes the expanded-Fx mixed sector, not proper33. That scope is preserved. :contentReference[oaicite:1]{index=1}

**Arithmetic discrepancy inside B-B:** its prose says ell(vertex7)=41/2040 at p=100. The literal coordinates and literal affine function give instead

    1-(99/100)(50/51)-(3/4)(1/102)+(4/5)(1/102)
      =61/2040.

The source/report already have 61/2040. This is a proposed correction to that prose line, not a new parent identity or a change in the control. Both values are positive, and no parent structural argument depends on the mistaken numerator. The new exact source checks the corrected arithmetic. :contentReference[oaicite:2]{index=2}

The adjacent-ordinary-B level lemma and the archived root-only height-law value theorem are used only at their accepted scope in the supplied memory. Their larger original archives are not attached for computation; no new computational result below depends on those archives. There is no missing exact input for the new controls or the new finite reconstruction. No research connector or external research source was used.

## 3. Definitions and accepted premises

Use the original canonical frame and actual uniform integrals:

    A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
    alpha=a-b>0, s=a+b, hc=s+c, hd=s+d,
    ell=a+(d-a)x+(c-a)y-alpha*z,
    n=hc*x+hd*y,
    V=int_P 1, J=(X,Y,Z)=int_P (x,y,z),
    E=int_P ell, N=int_P n,
    t=6V, mu=E/V, r=N/V, q=N/E=Tt,
    T=N/(6VE), G=n-r-q*ell.

E in these formulas is an integral, not an edge count. All these quantities belong to the same actual body. P contains T0=conv(A,B,C,D), so t>=1. Since the root has positive area and positive endpoint values, P is not T0.

The accepted full-maximum inputs are auxiliary true-vertex positivity G>0; the free-facet spike inequality; true ordinary-facet triangle rigidity; and the whole-facet hinge equations for affine motions vanishing on that facet's marks. An ordinary facet has one canonical mark and its other two vertices on a minimum-G root edge. There is no ordinary A facet and at most one ordinary facet total. An ordinary C requires c<min(b,d); the reflected condition holds at D. These are full-class facts, not assumptions about a stationary optimization inside a prescribed incidence or sign chamber. :contentReference[oaicite:3]{index=3}

For an ordinary B triangle, put L=-G(B)/3>0. Every root vertex has G>=L. Each adjacent special BY facet has G(Y)<L. The supplied notebook expressly gives this last statement at full body maximum, fixed ell, with all canonical marks true; it does not require the extra joint-mass inequality J. :contentReference[oaicite:4]{index=4}

The literal negative-z value theorem is

    T < 3(a+b+c)/(2a+b+c),                            (3)

after choosing c=max(c,d). Thus T<3 and, for T>=2,

    b+c > [(2T-3)/(3-T)]a >= a.                       (4)

This is an inherited maximum theorem, not monotonicity of clipping z<0. :contentReference[oaicite:5]{index=5}

The only free maximal facets possible here are AC, AD, BC, BD, up to two CD facets, the optional ordinary facet, and the possible BCD merger of BC/BD. ACD cannot support a body having points on both sides of z=0. A free facet with no canonical mark violates the spike inequality because all its vertices have positive G. AB already has the two protected coordinate facets. This list concerns actual maximal facets.

For a two-mark true triangle X0 X1 U, its whole hinge gives

    G(X0)+G(X1)+2G(U)=0.                              (5)

No equation of this form is inferred from an integration triangle of a larger polygon.

## 4. New same-body cone budget and elimination proof

### 4.1 The proper33 budget uses the entire volume, not a local cap volume

For **any actual proper33 body** with ell>=0 and for every p in P,

    24E >= n(p)+t*ell(p).                             (6)

No maximum or G-sign hypothesis is needed for (6). To prove it, triangulate each true maximal boundary facet for integration and cone that actual boundary from p. In a tetrahedron of volume v, the ell integral is v times the sum of its four vertex ell values divided by four. The contribution of ell(p), summed across this one actual fan, is V ell(p)/4. The protected maximal triangle ABC has pyramid volume x(p)/6 and remaining ell sum hc. The protected triangle ABD similarly contributes y(p)/6 and hd. Every other remaining endpoint contribution is nonnegative. Multiplying by 24 proves (6). Flat cells at a boundary apex contribute zero. The fan is not an independently chosen mass completion.

This strengthens the parent's cap budget by replacing the volume parameter of conv(T0,p) with the **whole actual t=6V**, precisely because ABC and ABD themselves are maximal triangles.

A reusable stronger proper33 auxiliary-height consequence is

    ell(U) < [(4-T)/(T+1)]mu.                         (6a)

Indeed G(U)>0 gives n(U)>r+q*ell(U), and (6) then gives (q+t)ell(U)<(4/T-1)r. With the accepted root-fan bound mu<=3M/4, every positive-ell auxiliary at T>=2 has ell(U)<M/2; at T>=51/25 the sharper bound is ell(U)<147M/304. These are same-body bounds, not an independently imposed auxiliary-height truncation.

Combine (5) and (6), writing w=ell(U)>=0. For any two-mark triangle,

    q[ell(X0)+ell(X1)]+2(q+t)w
       <= n(X0)+n(X1)+(8/T-4)r.                      (7)

Indeed (5) gives twice n(U) as 4r+q[ell(X0)+ell(X1)+2w]-n(X0)-n(X1), while (6) bounds 2n(U)+2tw by 48E=8r/T.

At T>=2, (7) immediately excludes a true ACU triangle: its left side is at least 2(a+c), whereas its right side is at most hd=a+b+d and

    2(a+c)-(a+b+d)=a-b+2c-d>0.

It also excludes a true BCU triangle, because (4) and c>=d give

    2(b+c)-(a+b+d)=(b+c-a)+(c-d)>0.                   (8)

These exclusions allow U on the root as well as off it. They are therefore stronger than a local sign classification of off-root vertices.

### 4.2 Complete off-root incidence analysis

Any positive-ell auxiliary U has x(U),y(U)>0, since the coordinate facets are exactly ABC and ABD. It belongs neither to the root nor to an ordinary facet: the latter has only its canonical anchor off the root. At least three independent incident facet planes must therefore come from AC, AD, BC, BD and CD.

Temporarily suppose BC and BD are distinct. Their true inward supports, together with AC and AD, can be uniquely normalized as

    fAC=z+u*x,                         u>0,
    fAD=z+v*y,                         v>0,
    fBC=1-z-y-(1-kappa)*x,              kappa>0,
    fBD=1-z-x-(1-lambda)*y,             lambda>0.

Every proper two-mark CD support is

    fCD=1-x-y-k*z,                     k<1.           (9)

The strict inequalities follow by evaluating at the omitted canonical vertices. Two distinct CD planes intersect in the line CD. A point of that line inside P lies on the segment CD and is not an auxiliary true vertex. Thus at most one CD plane can occur at U.

Here is the complete list of possible independent triples. The conclusions use intersections of true facets, hence true edges:

    AC,AD,BC  -> ACU is the whole triangle; C is simple.
    AC,AD,BD  -> ADU is the whole triangle; D is simple.
    AC,BC,BD  -> BCU is the whole triangle; C is simple.
    AD,BC,BD  -> BDU is the whole triangle; D is simple.
    AC,AD,CD  -> ACU and ADU are whole triangles.
    BC,BD,CD  -> BCU and BDU are whole triangles.

For example AC intersect AD is the true edge AU, and AC intersect BC is CU. Together with AC these close the whole polygon ACU. At C the three actual adjacent facets Fx,AC,BC already form a closed triangle in its vertex figure, so C is simple: no fourth facet through C is possible. The reflected assertions use D.

The remaining four three-plane subsets do not supply another case. AC,BC,CD all pass through C, so if they meet also at U they are dependent; AD,BD,CD is the reflected situation. For the cross triple AC,BD,CD, subtracting the two actual support equations at U gives

    (1-k)z(U)=lambda*y(U)>0,

whereas AC gives z(U)=-u*x(U)<0. This is impossible. AD,BC,CD similarly gives (1-k)z(U)=kappa*x(U)>0, also impossible. No CD triangle hinge is used in either argument.

If BCD is a true maximal facet, the true edges BC and BD are already occupied by Fx/BCD and Fy/BCD. B is simple, and no separate BC, BD or ordinary B facet remains. An off-root vertex would have to use AC,AD and BCD or a second CD plane; in either event ACU is a true triangle, already excluded. A triple using both CD planes instead lies on CD and is not an auxiliary vertex. This handles the three-mark merger rather than assuming it away.

Consequently, if any proper CD facet exists, the first four triples would force C or D simple despite the additional CD incidence; the fifth and sixth have the forbidden AC or BC triangle; and the other possibilities are impossible. **Every class with any CD facet is therefore root-only.** This proof works even when C and D are nonadjacent vertices of a single large CD polygon. It never treats CDU as a separately movable triangle.

### 4.3 All ordinary-facet cases are root-only

It remains to consider no CD facet. Ordinary C is impossible because c>=d. If ordinary D is present, the only triples not excluded by (8) would make D simple, contradicting that additional ordinary incidence. Thus ordinary D permits no positive-ell auxiliary.

Suppose instead that an ordinary B triangle is present. A BC/BD intersection edge from B to an auxiliary would close B's vertex figure with Fx,Fy,BC,BD, leaving no place for the ordinary B facet. Hence the B-side triples are impossible. Both A-side triples share the same true edge AC intersect AD, so there can be at most one such auxiliary. ACU is forbidden. The only candidate is

    U=AC intersect AD intersect BD, with FAD=ADU.

The ordinary B facet is adjacent to both BC and BD: it cannot be adjacent along an edge of either protected coordinate triangle without acquiring another canonical mark. Use the inherited L=-G(B)/3 and G(D)<L. Since G(A)<G(B)=-3L, the true ADU hinge forces

    G(U)=-(G(A)+G(D))/2 > L.                          (10)

Every other auxiliary vertex of BD is on the root, hence has G>=L. In the actual BD boundary cycle the first part is B,D,U; the remaining vertices form the root chain back to B. Triangulate **the whole BD facet** from B for integration of G*y. On BDU, the coefficient is

    G(B)+G(D)+2G(U)=G(B)-G(A)=q(a-b)>0.

Here y(U)>0, so this contribution is strictly positive. On every other triangle BRS, both auxiliary G values are >=L and y(R),y(S)>=0. Its two coefficients are

    G(B)+2G(R)+G(S)>=0,
    G(B)+G(R)+2G(S)>=0.

Their contributions are nonnegative. The resulting **whole-facet** integral int_BD G*y/|grad fBD| is strictly positive, contradicting its whole hinge. Thus the ordinary B case is root-only too.

### 4.4 Exactly two simple residual charts

With neither CD nor ordinary facets, and with BCD already excluded, there are exactly seven maximal facets. A and B have degree four. If vcount is the number of vertices and ecount the number of true edges, Euler and the degree sum give

    ecount=vcount+5,
    2*ecount >= 4+4+3(vcount-2),
    vcount<=8.

An off-root auxiliary requires four canonical vertices, at least three root vertices, and itself. Hence vcount=8, ecount=13; the root is a triangle, there is one off-root U, and every non-A/B vertex is simple. The two remaining triples are precisely L_D and U_D below. This also excludes all potentially troublesome nonsimple auxiliary boundary cases; no genericity assumption is needed.

### 4.5 New endpoint gap and sign separation

Both residual triangles have the form XDU, with X=A or B. Put e=ell(X), so e>=b, and w=ell(U)>0. Apply (6) also at C. Since r=6TE,

    r >= T(hd+t*c)/4.

Using this in (7), with T>=2, yields the coherent necessary inequality

    t[T(e+d)+(T-2)c+2(T+1)w]+(T-2)hd <= hc.            (11)

At T>=51/25 it implies the useful rational cut

    [51(e+d)+c+152w]t + hd <= 25hc.                   (12)

Replace e by b, use t>=1 and w>0 in (11), and put S=b+c, Delta=c-d. One obtains

    T*Delta > (2T-3)S-(3-T)a+(T-2)d.

Substitution of the strict parent bound (4) proves (1), because

    (2T-3)^2-(3-T)^2=3T(T-2).

The right side of (1) increases with T on [2,3). At T=51/25 its coefficients are exactly 1/8 and 1/51. At T=2 the strict conclusion is still c>d. Thus equal C/D endpoints have no off-root residual.

For L_D, (12) also gives

    b+c>9a/8+13d/6.

Finally, if G(D)<=0, then hc<=r+qd. The triangle inequality (7) gives

    e+2(1+t/q)w <= (8/T-3)mu,
    e < (8/T-3)mu.                                  (13)

The accepted height premise is mu<=3M/4. The accepted general high-trace endpoint screen is c<943(a+b)/1352; since b<a, M=max(a,c)<943a/676. Therefore at T>=51/25, a putative L_D with G(D)<=0 would require

    a < (47/68)M < (44321/45968)a < a,

a contradiction. The exact final gap is 1647/45968. For U_D, the same argument preserves the useful necessary condition b<47M/68 instead of falsely excluding that chart. The height premise is recorded in the supplied negative-anchor authority; the endpoint screen is in the common notebook. :contentReference[oaicite:6]{index=6} :contentReference[oaicite:7]{index=7}

## 5. Complete actual recovery charts and remaining equations

The common seven supports are x>=0,y>=0,ell>=0 and fAC,fAD,fBC,fBD from Section 4.2. Normalize a=1 if desired; the remaining independent input parameters are

    b,c,d,u,v,kappa,lambda,
    0<b<1, c>d>0, u,v,kappa,lambda>0.

These positivity conditions alone are not a realization certificate. Recover all plane intersections, require the strict off-facet slacks and the exact true facets below, positive root area, ell(U)>0, and boundedness. The complete source uses the stronger exact test that the input halfspaces equal the independently reconstructed bounded hull's maximal halfspaces. It does not assume the six-plane body obtained by removing the root is bounded.

Label the vertices A,B,C,D,U,P,Q,R as 0,1,2,3,4,5,6,7. All root points have positive x and y.

### L_D

    U = AC intersect AD intersect BD,
    P = AC intersect BC intersect root,
    Q = AC intersect BD intersect root,
    R = BC intersect BD intersect root.

All maximal facet cycles, in order Fx,Fy,AC,AD,BC,BD,root:

    (A,B,C), (A,B,D), (A,C,P,Q,U), (A,D,U),
    (B,C,P,R), (B,D,U,Q,R), (P,Q,R).

All thirteen true edges:

    AB,AC,AD,AU,BC,BD,BR,CP,DU,UQ,PQ,PR,QR.

At the target threshold this chart must have G(C)<0<G(D). The three integration triangles of either pentagon are not additional facets.

### U_D

    U = AD intersect BC intersect BD,
    P = AC intersect BC intersect root,
    Q = AC intersect AD intersect root,
    R = AD intersect BC intersect root.

All maximal facet cycles:

    (A,B,C), (A,B,D), (A,C,P,Q), (A,D,U,R,Q),
    (B,C,P,R,U), (B,D,U), (P,Q,R).

All thirteen true edges:

    AB,AC,AD,AQ,BC,BD,BU,CP,DU,UR,PQ,PR,QR.

This chart allows mixed or both-negative signs at the level of actual geometry and selected necessary tests; the controls below exhibit both. All three root vertices in this chart have negative z because each is incident to AC or AD.

### Exact remaining full-maximum obstruction

For either chart, compute V,J,E,N from its actual boundary fan and use its own G. The four required whole-facet equations are

    int_AC G*x/|grad fAC| = int_AD G*y/|grad fAD|
      = int_BC G*x/|grad fBC| = int_BD G*y/|grad fBD| =0. (14)

All four coarea measures equal projected xy area in this normalization. Let p=X+Y and k0=|grad ell|. The full root equations are

    int_F0 G/k0       = qV-3p,
    int_F0 G*x/k0     = qX-Y,
    int_F0 G*y/k0     = qY-X,
    int_F0 G*z/k0     = qZ-p.                          (15)

Their ell-linear combination is identically zero, so there are three independent root equations. They follow by moving the whole root and changing the affine endpoint data simultaneously: the bulk numerator derivative for h=delta ell is 3p*h(w0), where w0=(Y/(3p),X/(3p),1/3). Thus (15) is not stationarity of a root polygon while unrelated volume moments are held fixed.

For a triangle with affine data f_i,h_i,

    integral(f*h) = Area*[ (sum f_i)(sum h_i)+sum f_i*h_i ]/12.

For the root, divide projected xy area by alpha. This formula and the literal cycles give every equation in (14)-(15) as a rational function of the seven parameters. Clearing the proven-positive denominators gives a finite polynomial equality/inequality problem, with no unknown facet count or free moment weights. The source computes both sets of residuals for the controls.

A useful additional diagnostic is the four-by-four matrix whose rows are int_F H*(1,x,y,z). It must annihilate the **actual** coefficient vector

    (-r-qa, hc-q(d-a), hd-q(c-a), q*alpha).

A determinant-zero test alone is not sufficient. A numerical investigation of that matrix is preserved below as NONPROOF; it has not been converted into a complete certificate on the necessary endpoint domain.

## 6. Exact genuine controls: both residual incidences really occur

The following three bodies share

    (a,b,c,d)=(1,1/2,7/10,1/20),
    ell=1-19x/20-3y/10-z/2.

They all have the seven true facets and thirteen true edges just listed, true proper33, a positive-area root triangle, positive G at every auxiliary, and negative-z positive-ell material. They also satisfy b+c=6/5>9/8, so they are not discarded by the old negative-z endpoint screen alone. They are **nonstationary actual controls**, not high-trace examples or full maxima.

L_mixed uses

    (u,v,kappa,lambda)=(1/99,1/10,10,4/5),
    U=(99/100,1/10,-1/100),
    P=(1386/7223,19711/7223,-14/7223),
    Q=(990/1069,445/1069,-10/1069),
    R=(10/59,125/59,24/59).

Its own original moments are

    V=32423528653/54667419960,
    J=(584937528836369686637/3320585338981118224000,
       465677886297558420139/996175601694335467200,
       1544540340049201738111/9961756016943354672000),
    E=90964296040777/437339359680000,
    N=110785949279321954439587/99617560169433546720000,
    T=4431437971172878177583480/2949383459078107515883381.

Here T is approximately 1.50249638, G(C)<0<G(D), ell(U)=69/2000, and all four whole hinges are negative. Its actual own-centroid Euclidean mechanics are strict(S,U,H)=(4,4,6), weak000.

U_mixed uses

    (u,v,kappa,lambda)=(1,2,1/50,101/49),
    U=(101/98,1/100,-1/50),
    P=(175/114,235/228,-175/114),
    Q=(5/3,5/6,-5/3),
    R=(25/22,5/44,-5/22).

Its own original moments are

    V=3119791/6144600,
    J=(1321200141929/4530733099200,
       974668794371/4623197040000,
       -275385450821/2311598520000),
    E=410115277057/1806512400000,
    N=4387162210893349/4530733099200000,
    T=5374273708344352525/3838421850974805261.

Here T is approximately 1.40012586, G(C)<0<G(D), ell(U)=171/6125, and the whole AC,AD,BC,BD hinge signs are (-,+,+,-). Its own mechanics are strict(3,4,5), weak000.

U_both_negative changes only u to 11/10. Its U and R are unchanged; the other root vertices are

    P=(175/109,130/109,-385/218),
    Q=(200/113,110/113,-220/113).

Its own original moments, recomputed rather than transferred from U_mixed, are

    V=1146726319/1991658900,
    J=(3148268239499931/8814900386553800,
       2377378542293269/8994796312810000,
       -20300997774881281/107937555753720000),
    E=32688881497689/130121714800000,
    N=10537428132643323811/8814900386553800000,
    T=51633397849952286673900/37485200752072113976791.

Here T is approximately 1.37743421, G(C)<G(D)<0, all four auxiliary G values remain positive, and the same four hinge signs are (-,+,+,-). Its own mechanics are strict(3,4,5), weak000.

The actual B-apex and A-apex pyramid volumes and their J,E,N are independently recomputed and summed in the capsule. The genuine B-root pyramid satisfies E_root=b*V_root/4. All 156 true-edge primal/polar primitives across the three controls are nonzero, using each body's actual volume centroid and M=N_metric=I. No polar recentering occurs.

A nonzero whole hinge supplies a genuine local ascent by moving that entire supporting plane in the appropriate sign; the strict incidence guards preserve these actual bodies for sufficiently small motion. No finite interval or stationary successor is asserted. These controls demonstrate why auxiliary positivity, coordinate-mark exposure and the old endpoint screen must not be promoted to full stationarity or to an automatic root-only theorem.

## 7. Exact source-only recovery and verification status

The theorem in Sections 1-5 is analytic under the listed accepted premises. The following computation verifies finite arithmetic identities and actual controls; it does not formally certify the universal geometric proof.

    CPython 3.13.5, standard library only, assertions enabled.
    python -S proper33_negative_z_two_charts_v1.py > proper33_negative_z_two_charts_v1.out

The normal execution and an empty-directory source-only execution were actually completed. Both generated JSON and stdout matched byte for byte.

    source: 12055 bytes
    SHA256 4c9477bb815b71f6781371e42fe1564dfa6b7004e9bd1cdab5e71e8693b48ed6
    report: 42662 bytes
    SHA256 891f5bec143dd3fca156a8548fd4c98e4e2398cf687900f8afb00bf3c6a76a73
    stdout: 644 bytes
    SHA256 327b8fda52769b02fcbbbb2b228f00c40b10ee4e80d2be9191a6e935431123a3

Complete expected stdout:


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]

    U_mixed T=5374273708344352525/3838421850974805261 SUH=(3, 4, 5)
    U_both_negative T=51633397849952286673900/37485200752072113976791 SUH=(3, 4, 5)
    report_bytes=42662
    report_sha256=891f5bec143dd3fca156a8548fd4c98e4e2398cf687900f8afb00bf3c6a76a73
    PROPER33_NEGATIVE_Z_TWO_CHARTS_V1_RECOVERY_PASS

Optional copies: [source](sandbox:/mnt/data/proper33_negative_z_two_charts_v1.py), [full report](sandbox:/mnt/data/proper33_negative_z_two_charts_v1.json), [stdout](sandbox:/mnt/data/proper33_negative_z_two_charts_v1.out). The entire source follows; no download or parent import is required.

```python
#!/usr/bin/env python3
"""PROPER33_NEGATIVE_Z_HIGH_TRACE_TWO_CHART_REDUCTION_V1 recovery.
CPython 3.13.5, standard library, assertions enabled, no RNG/external input.
Parents: minimum-0174
75a778882cc680e10036501e71396ca70222ddd9ed56de6b5aa1fa5aa66759d1;
minimum-0165
078f5b8df8a0c5b0ccb7a22bc3fa7aa26301717b0635893ed1c728e9efffebeb.
The theorem is analytic. Computation audits three genuine NONSTATIONARY
controls, their full facets/edges, actual moments, and whole-facet work.
Geometry helpers below are the supplied csS2 geometry.py, with no imports
of a parent file. Each control is independently rehull-checked.
"""
"""Exact actual-polytope geometry; CPython 3.13.5, standard library only."""
from fractions import Fraction as F
from itertools import combinations

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(c,a): return tuple(c*x for x in a)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def solve(a,b):
 d=det(*a)
 if not d:return None
 return tuple(det(*[tuple(b[i] if k==j else a[i][k] for k in range(3)) for i in range(3)])/d for j in range(3))
def hull2(pts):
 pts=sorted(set(pts))
 def turn(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
 lo=[];hi=[]
 for p in pts:
  while len(lo)>1 and turn(lo[-2],lo[-1],p)<=0:lo.pop()
  lo.append(p)
 for p in reversed(pts):
  while len(hi)>1 and turn(hi[-2],hi[-1],p)<=0:hi.pop()
  hi.append(p)
 return lo[:-1]+hi[:-1]
def hrep(vs):
 faces={}
 for a,b,c in combinations(vs,3):
  n=cross(sub(b,a),sub(c,a))
  if not any(n):continue
  h=dot(n,a);d=[dot(n,v)-h for v in vs]
  if min(d)<0<max(d):continue
  if max(d)>0:n=mul(-1,n);h=-h
  scale=abs(next(x for x in n if x));n=mul(1/scale,n);h/=scale
  faces[n,h]=None
 return sorted(faces)
def vrep(planes):
 out=set()
 for ids in combinations(range(len(planes)),3):
  p=solve([planes[i][0] for i in ids],[planes[i][1] for i in ids])
  if p is not None and all(dot(n,p)<=h for n,h in planes):out.add(p)
 return sorted(out)
def body(vs,ep,required_marks=None):
 vs=[tuple(F(x) for x in v) for v in vs];planes=hrep(vs);vs=vrep(planes)
 faces=[]
 for n,h in planes:
  ids=[i for i,v in enumerate(vs) if dot(n,v)==h]
  drop=next(i for i,x in enumerate(n) if x);axes=[i for i in range(3) if i!=drop]
  mp={tuple(vs[i][j] for j in axes):i for i in ids}
  cyc=[mp[v] for v in hull2(mp)]
  assert len(cyc)>=3 and set(cyc)==set(ids)
  if dot(cross(sub(vs[cyc[1]],vs[cyc[0]]),sub(vs[cyc[2]],vs[cyc[0]])),n)<0:cyc.reverse()
  p=cyc.index(min(cyc));faces.append(tuple(cyc[p:]+cyc[:p]))
 edges=sorted({tuple(sorted((cyc[j],cyc[(j+1)%len(cyc)]))) for cyc in faces for j in range(len(cyc))})
 inc={e:[i for i,cyc in enumerate(faces) if set(e)<=set(cyc)] for e in edges}
 assert all(len(a)==2 for a in inc.values()) and len(vs)-len(edges)+len(faces)==2
 O=tuple(sum(v[j] for v in vs)/len(vs) for j in range(3))
 assert all(dot(n,O)<h for n,h in planes)
 def integrate(o):
  vol=F(0);J=(F(0),)*3
  for cyc in faces:
   for k in range(1,len(cyc)-1):
    pts=[o,vs[cyc[0]],vs[cyc[k]],vs[cyc[k+1]]]
    v=det(*(sub(p,o) for p in pts[1:]))/6;assert v>=0
    vol+=v;J=add(J,mul(v/4,tuple(sum(p[j] for p in pts) for j in range(3))))
  return vol,J
 vol,J=integrate(O);assert (vol,J)==integrate((F(0),)*3)
 a,b,c,d=ep;alpha=a-b;hc=a+b+c;hd=a+b+d
 ell=lambda p:a+(d-a)*p[0]+(c-a)*p[1]-alpha*p[2]
 nn=lambda p:hc*p[0]+hd*p[1]
 g=mul(1/vol,J);E=vol*ell(g);N=vol*nn(g);r=N/vol;q=N/E;T=N/(6*vol*E)
 GG=lambda p:nn(p)-r-q*ell(p)
 mark=[(F(0),F(0),F(0)),(F(0),F(0),F(1)),(F(0),F(1),F(0)),(F(1),F(0),F(0))]
 if required_marks is not None:mark=required_marks
 assert all(all(dot(n,p)<=h for n,h in planes) for p in mark)
 assert min(ell(p) for p in vs)>=0
 def fi(index,axes,f1,f2=lambda p:F(1)):
  cyc=faces[index];z=F(0)
  for j in range(1,len(cyc)-1):
   pp=[vs[cyc[0]],vs[cyc[j]],vs[cyc[j+1]]]
   a0,b0,c0=[tuple(p[i] for i in axes) for p in pp]
   area=abs((b0[0]-a0[0])*(c0[1]-a0[1])-(b0[1]-a0[1])*(c0[0]-a0[0]))/2
   aa=[f1(p) for p in pp];bb=[f2(p) for p in pp]
   z+=area*(sum(aa)*sum(bb)+sum(x*y for x,y in zip(aa,bb)))/12
  return z
 return dict(vs=vs,planes=planes,faces=faces,edges=edges,inc=inc,V=vol,J=J,g=g,E=E,N=N,r=r,q=q,T=T,
  ell=ell,nn=nn,G=GG,fi=fi,marks=mark)

from pathlib import Path
import hashlib
import json

EP=(F(1),F(1,2),F(7,10),F(1,20))
INPUTS=(('L_mixed','L',F(1,99),F(1,10),F(10),F(4,5)),
        ('U_mixed','U',F(1),F(2),F(1,50),F(101,49)),
        ('U_both_negative','U',F(11,10),F(2),F(1,50),F(101,49)))
FACETS={
 'L':((0,1,2),(0,1,3),(0,2,5,6,4),(0,3,4),
      (1,2,5,7),(1,3,4,6,7),(5,6,7)),
 'U':((0,1,2),(0,1,3),(0,2,5,6),(0,3,4,7,6),
      (1,2,5,7,4),(1,3,4),(5,6,7))}
NAMES=('Fx','Fy','AC','AD','BC','BD','root')

def planes(u,v,k,l):
 a,b,c,d=EP
 # Outward n.X<=h; f=h-n.X is the corresponding inward slack.
 return [(tuple(map(F,n)),F(h)) for n,h in
         [((-1,0,0),0),((0,-1,0),0),((-u,0,-1),0),
          ((0,-v,-1),0),((1-k,1,1),1),((1,1-l,1),1),
          ((a-d,a-c,a-b),a)]]

def normalized(hs):
 return sorted((mul(1/abs(next(x for x in n if x)),n),
                h/abs(next(x for x in n if x))) for n,h in hs)

def fan(P,apex,which=None):
 o=P['vs'][apex];pieces=[]
 for i,cyc in enumerate(P['faces']):
  if which is not None and i not in which:continue
  if apex in cyc:continue
  vol=F(0);jj=(F(0),)*3
  for j in range(1,len(cyc)-1):
   pp=[o,P['vs'][cyc[0]],P['vs'][cyc[j]],P['vs'][cyc[j+1]]]
   w=det(*(sub(p,o) for p in pp[1:]))/6
   assert w>0
   vol+=w;jj=add(jj,mul(w/4,tuple(sum(p[h] for p in pp) for h in range(3))))
  a,b,c,d=EP
  ee=a*vol+dot((d-a,c-a,b-a),jj)
  nn=dot((a+b+c,a+b+d,0),jj)
  pieces.append((i,vol,jj,ee,nn))
 return pieces

def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [encode(v) for v in x]
 return x

def audit(inp):
 name,kind,u,v,k,l=inp;hs=planes(u,v,k,l)
 P=body(vrep(hs),EP)
 # Both inclusions: all input halfspaces are exactly the independently
 # reconstructed bounded hull's maximal supporting halfspaces.
 assert normalized(hs)==P['planes']
 marks=P['marks'];assert all(p in P['vs'] for p in marks)
 def meet(ids):return solve([hs[i][0] for i in ids],[hs[i][1] for i in ids])
 if kind=='L':triples=((2,3,5),(2,4,6),(2,5,6),(4,5,6))
 else:triples=((3,4,5),(2,4,6),(2,3,6),(3,4,6))
 pts=marks+[meet(ids) for ids in triples]
 assert len(set(pts))==8 and set(pts)==set(P['vs'])
 oldnew={P['vs'].index(p):i for i,p in enumerate(pts)}
 actual={frozenset(oldnew[j] for j in cy) for cy in P['faces']}
 assert actual=={frozenset(cy) for cy in FACETS[kind]}
 edges=sorted(tuple(sorted(oldnew[j] for j in ed)) for ed in P['edges'])
 expected=sorted({tuple(sorted((cy[i-1],cy[i])))
                  for cy in FACETS[kind] for i in range(len(cy))})
 assert edges==expected and len(edges)==13 and len(P['faces'])==7
 assert [len([ed for ed in edges if j in ed]) for j in range(8)]==[4,4,3,3,3,3,3,3]
 assert all(P['ell'](pts[j])>0 for j in range(5))
 assert all(P['ell'](pts[j])==0 for j in (5,6,7))
 assert all(pts[j][0]>0 and pts[j][1]>0 for j in range(4,8))
 assert pts[4][2]<0 and P['G'](pts[2])<0
 assert (P['G'](pts[3])<0)==(name=='U_both_negative')
 assert min(P['G'](pts[j]) for j in range(4,8))>0
 assert EP[1]+EP[2]>F(9,8)*EP[0]
 assert F(0)<P['T']<F(51,25)
 a,b,c,d=EP;t=6*P['V'];r=P['r'];q=P['q']
 hC=[(b+2*c)*(p[1]-1)-(a-b)*p[2] for p in pts if p[0]==0]
 hD=[(b+2*d)*(p[0]-1)-(a-b)*p[2] for p in pts if p[1]==0]
 assert max(hC)==max(hD)==0
 facetmap=[next(i for i,cy in enumerate(P['faces'])
                if frozenset(oldnew[j] for j in cy)==frozenset(want))
           for want in FACETS[kind]]
 hinges={}
 for j,axis in ((2,0),(3,1),(4,0),(5,1)):
  # |f_z|=1: dS/|grad f| is exactly projected xy area.
  hinges[NAMES[j]]=P['fi'](facetmap[j],(0,1),P['G'],lambda p,axis=axis:p[axis])
 assert any(hinges.values())
 tri=3 if kind=='L' else 5
 mark=0 if kind=='L' else 1
 # Direct triangle formula, independent of polygon integration routines.
 A0=pts[mark];D0=pts[3];U=pts[4]
 area=abs((D0[0]-A0[0])*(U[1]-A0[1])-(D0[1]-A0[1])*(U[0]-A0[0]))/2
 direct=area*U[1]*(P['G'](A0)+P['G'](D0)+2*P['G'](U))/12
 assert hinges[NAMES[tri]]==direct
 coneguards=[24*P['E']-P['nn'](p)-t*P['ell'](p) for p in pts]
 assert min(coneguards)>=0
 bp=fan(P,P['vs'].index(marks[1]));ap=fan(P,P['vs'].index(marks[0]))
 for pieces in (bp,ap):
  assert sum(z[1] for z in pieces)==P['V']
  assert tuple(sum(z[2][j] for z in pieces) for j in range(3))==P['J']
  assert sum(z[3] for z in pieces)==P['E']
  assert sum(z[4] for z in pieces)==P['N']
 rootpiece=next(z for z in bp if z[0]==facetmap[6])
 assert rootpiece[3]==b*rootpiece[1]/4
 # The full root reaction is reported as a residual, never imposed.
 pxy=P['J'][0]+P['J'][1]
 rhs=[q*P['V']-3*pxy,q*P['J'][0]-P['J'][1],
      q*P['J'][1]-P['J'][0],q*P['J'][2]-pxy]
 rr=[]
 for j in range(4):
  val=P['fi'](facetmap[6],(0,1),P['G'],
               lambda p,j=j:F(1) if j==0 else p[j-1])/(a-b)
  rr.append(val-rhs[j])
 assert any(rr)
 assert a*rr[0]+(d-a)*rr[1]+(c-a)*rr[2]+(b-a)*rr[3]==0
 # All mechanical primitives use this body's own uniform centroid and M=I.
 xx=[sub(p,P['g']) for p in pts]
 poles=[mul(1/(h-dot(n,P['g'])),n) for n,h in hs]
 packets=[];pu=[[] for _ in pts];pd=[[] for _ in hs]
 for i,j in edges:
  fs=[f for f,cy in enumerate(FACETS[kind]) if i in cy and j in cy]
  assert len(fs)==2;f,g=fs
  z=(dot(xx[i],sub(xx[j],xx[i])),dot(xx[j],sub(xx[i],xx[j])),
     dot(poles[f],sub(poles[g],poles[f])),dot(poles[g],sub(poles[f],poles[g])))
  pu[i].append(z[0]);pu[j].append(z[1]);pd[f].append(z[2]);pd[g].append(z[3])
  packets.append(dict(edge=(i,j),facets=(f,g),primitives=z))
 assert all(z!=0 for row in packets for z in row['primitives'])
 Ulist=[i for i,z in enumerate(pu) if max(z)<0]
 Slist=[i for i,z in enumerate(pd) if max(z)<0]
 Hlist=[row['edge'] for row in packets if max(row['primitives'])<0]
 assert len(Slist)+len(Ulist)-len(Hlist)==2
 def packpieces(pieces):
  return [dict(facet=NAMES[facetmap.index(z[0])],V=z[1],J=z[2],E=z[3],N=z[4]) for z in pieces]
 return dict(name=name,kind=kind,endpoints=EP,parameters=(u,v,k,l),
             vertices=pts,facets=FACETS[kind],facet_names=NAMES,edges=edges,
             halfspaces=[dict(n=n,h=h) for n,h in hs],
             V=P['V'],J=P['J'],g=P['g'],E=P['E'],N=P['N'],T=P['T'],
             G=[P['G'](p) for p in pts],ell=[P['ell'](p) for p in pts],
             whole_hinges=hinges,root_reaction_residual=rr,
             cone_budget_slacks=coneguards,A_fan=packpieces(ap),B_fan=packpieces(bp),
             S=Slist,U=Ulist,H=Hlist,weak_packets=0,primitives=packets,
             status='actual uniform nonstationary body; not a high-trace or 110 witness')

def main():
 tau=F(51,25)
 assert (3*(tau-2)/(3-tau),(tau-2)/tau)==(F(1,8),F(1,51))
 assert F(8)/tau-3==F(47,51)
 assert F(47,68)*F(943,676)==F(44321,45968)<1
 assert 1-F(44321,45968)==F(1647,45968)
 # Correct the literal B-B prose typo without altering its source/control.
 assert 1-F(99,100)*F(50,51)-F(3,4)*F(1,102)+F(4,5)*F(1,102)==F(61,2040)
 controls=[audit(x) for x in INPUTS]
 raw=(json.dumps(encode(dict(version=1,controls=controls)),sort_keys=True,indent=2)+'\n').encode()
 Path('proper33_negative_z_two_charts_v1.json').write_bytes(raw)
 print('THREE_TRUE_8_13_7_HULLS_AND_COMPLETE_INCIDENCES_PASS')
 print('SAME_BODY_A_B_FANS_V_J_E_N_AND_ROOT_MOMENTS_PASS')
 print('MIXED_AND_BOTH_NEGATIVE_AUXILIARY_POSITIVE_CONTROLS_PASS')
 print('TWELVE_WHOLE_HINGES_AND_ROOT_RESIDUALS_COMPUTED_NOT_STATIONARY')
 print('ALL_156_OWN_CENTROID_MECHANICAL_PRIMITIVES_NONZERO_PASS')
 for z in controls:
  print(z['name']+' T='+str(z['T'])+' SUH='+str((len(z['S']),len(z['U']),len(z['H']))))
 print('report_bytes='+str(len(raw)))
 print('report_sha256='+hashlib.sha256(raw).hexdigest())
 print('PROPER33_NEGATIVE_Z_TWO_CHARTS_V1_RECOVERY_PASS')

if __name__=='__main__':main()
```

## 8. What was tried, and a preserved nonproof diagnostic

The expanded-Fx parent's CD-support/root-barrier argument cannot simply be transferred: proper33 has no positive-z auxiliary on Fx to supply that support comparison, and BC is now present. I instead used the stronger full-boundary cone budget (6), then the actual vertex figures, and only then the ordinary-B root minimum. This avoids trying to enumerate G sign choices on arbitrary triangulations.

I also investigated whether four whole-facet weighted centroids always provide a nonsingular affine-hinge matrix. The following numerical diagnostic did not yield a universal proof. It generated 100,000 parameter arrays for a truncated six-vertex outer-chart model. The numerical determinant signs were 99,958 negative and 42 nonnegative; the 918 arrays passing the displayed necessary high-trace endpoint screen all had negative numerical determinant. Neither count certifies a whole domain. These arrays were not tested as full stationary actual-own-G bodies, and no sampled zero, maximum or exclusion is asserted. The arrays are not durable exact body successors to the three rational controls above.

The code preserves the full inputs and the diagnostic, not a certificate. Its four rows integrate whole facets; the triangles appearing in the formulas are solely integration pieces. A separate earlier test of outer parameters (p,q,r,s)=(2,1,2,-2) failed the intended outer support condition and is not an actual proper33 control. No conclusion uses that test.

    CPython 3.13.5, SymPy 1.14.0, NumPy 2.3.5.
    OPENBLAS_NUM_THREADS=1 python proper33_hinge_diagnostic.py
    source: 2000 bytes
    SHA256 600adc1498c22f6eb5572de64d004a51dbd8c0f1df5c7e354bd4454ec39228b0
    stdout: 130 bytes
    SHA256 df40c0854256f0518154f2e0cbacb15261e3afb6dafb318b9cd7870b175d7453

The compact diagnostic was actually run. Complete expected stdout:

    all negative/nonnegative 99958 42
    ordered endpoints/nonnegative 16982 42
    high screen/nonnegative 918 0
    NONPROOF_HINGE_LOCATOR_END

```python
#!/usr/bin/env python3
"""NONPROOF diagnostic only; CPython3.13.5/SymPy1.14.0/NumPy2.3.5.
OPENBLAS_NUM_THREADS=1. No own-G/body optimality is asserted.
Outer coordinates: Z=0,A=e1,B=e2,W=e3,C=(p,0,q),D=(0,r,s).
Root cut points are (1-e)W+eC, (1-f)W+fB, (1-v)W+vZ.
The four rows are complete facet integrals, not independent triangle moves.
"""
import sympy as S
p,q,r,s,v,e,f=S.symbols('p q r s v e f')
z,x,y,w=S.symbols('Gz Gx Gy Gw')
GZ=z; GA=z+x; GB=z+y; GC=z+p*x+q*w; GD=z+r*y+s*w; GW=z+w
hc=q+p-1;hd=1-r-s
pc=(1-e)*GW+e*GC;pb=(1-f)*GW+f*GB;p0=(1-v)*GW+v*GZ
ha_pc=(1-e)*hc;ha_p0=(1-v)*hc+v*q
hd_pb=(1-f)*hd;hd_p0=(1-v)*hd-v*s
prod=lambda G,H:S.expand(sum(G)*sum(H)+sum(a*b for a,b in zip(G,H)))
FAC=q*q*(2*GZ+GA+GC)+p*prod([GZ,GC,GW],[q,0,hc])-p*e*v*prod([GW,pc,p0],[hc,ha_pc,ha_p0])
FBD=s*s*(2*GZ+GB+GD)+prod([GZ,GW,GB],[-s,hd,0])-f*v*prod([GW,p0,pb],[hd,hd_p0,hd_pb])
FBC=GB+GC+2*GW-e*f*prod([GW,pc,pb],[1,1-e,1-f])
FAD=GA+GD+2*GZ
mat=S.Matrix([[S.expand(a).coeff(b) for b in [z,x,y,w]] for a in [FAD,FAC,FBD,FBC]])

import numpy as np
if __name__=='__main__':
 rng=np.random.default_rng(542100);n=100000
 fun=S.lambdify((p,q,r,s,v,e,f),list(mat),'numpy')
 qv=np.exp(rng.uniform(-4,4,n));hv=np.exp(rng.uniform(-4,4,n))
 pmin=np.maximum(0,1-qv);pmax=1+qv/hv
 pv=pmin+(pmax-pmin)*rng.uniform(.0001,.9999,n)
 rv=(1+(1-pv)*hv/qv)*rng.uniform(.0001,.9999,n)
 vv,ee,ff=rng.uniform(.0001,.9999,(3,n))
 vals=fun(pv,qv,rv,-hv,vv,ee,ff)
 rows=np.stack([np.full(n,x) if np.isscalar(x) else x for x in vals],axis=1).reshape(n,4,4)
 dets=np.linalg.det(rows)
 hu=(1-vv)/vv;bb=(1-ff)/ff;cc=(1-ee)/ee
 aa=(cc-(1-pv-qv)*hu+qv)/pv
 dd=(1-rv+hv)*hu+rv*bb+hv
 keep=(aa>bb)&(cc>=dd)
 high=keep&(bb+cc>9*aa/8)&(cc<943*(aa+bb)/1352)&(dd<3*aa/4)&(bb>aa/25)
 print('all negative/nonnegative',int(sum(dets<0)),int(sum(dets>=0)))
 print('ordered endpoints/nonnegative',int(sum(keep)),int(sum(keep&(dets>=0))))
 print('high screen/nonnegative',int(sum(high)),int(sum(high&(dets>=0))))
 print('NONPROOF_HINGE_LOCATOR_END')
```

## 9. Scope, uncertainty, and most useful continuation

The new durable object is the analytic root-only sector theorem and the complete two-chart reduction, together with the exact actual controls. It is not a formalization in a proof assistant. The most important independent audit points are the vertex-figure closure in Section 4.2 and the ordinary-B **whole-polygon** integral in Section 4.3. Both are written without moving an integration diagonal or assigning independent star moments.

The proof uses the full local-maximum premises; it does not cover maxima artificially constrained to fixed endpoint chambers, fixed signs or a fixed face lattice. It uses neither the extra joint-mass upper bound 4(gx+gy)<=t+1 nor a surrogate G, independently chosen root area, free cell weights, or a stationary local hinge/spike relaxation. All-positive endpoints, a>b and positive root area are genuine hypotheses. Balanced/zero-endpoint limits and other coordinate facet sizes are outside this theorem.

The most consequential continuation is now the **actual seven-parameter system (11), (14), (15)** on U_D, with all facets and moments reconstructed from the same seven supports. At the target threshold L_D already needs mixed signs; U_D is the sole both-negative possibility. The explicit gap (2), the lower-chart cut b+c>9a/8+13d/6, the upper both-negative constraint b<47M/68, and the actual root-triangle moment equations should be retained together rather than relaxed into independent volumes. There is no remaining need to search arbitrary CD polygons, ordinary D caps, ordinary B5 stars or nonsimple positive-ell auxiliaries for this high-trace complement.

I do not infer a full proper33 trace theorem from this reduction. The two residual charts are not excluded, and low-endpoint negative-z root-only VALUE is still separate. No 110 control was found or claimed. These 8/13/7 trace-body counts do not remove mechanical 10/17/9 incidences without the missing trace-to-mechanics bridge. The accepted global interval remains 34<=C_min<=622, and the whole minimum remains unresolved. :contentReference[oaicite:8]{index=8}
