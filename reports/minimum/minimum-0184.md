# minimum-0184

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# ONE_EXPANDED_TWO_NONPOSITIVE_ROOT_REDUCTION_AND_VALUE_V1

## 1. Result and exact scope

**The one-expanded, two-nonpositive sector is excluded at T>=51/25 for the full marked-body[private-runtime-path] maximum.** More precisely, under the accepted full-maximizer conditions, including the nonpositive-mark exposure supplied by V2, every all-positive-endpoint maximum with exactly one expanded coordinate facet and G(C),G(D)<=0 satisfies

    T<=203/100<51/25.

There are two new components.

**Structural theorem.** Once the supplied A-star theorem has made A simple and the body nonnegative in z, the one-expanded/two-nonpositive sector has no ordinary C or D facets, has the actual base triangle ACD, and is root-only. Its complete true incidence is exactly S5, I4 or I5, with the literal cycles in Section 4. This conclusion is derived afresh for both nonpositive signs; it is not inferred from the name of the earlier mixed-sign theorem. In particular, no order c>d is assumed after choosing Fx to be the expanded coordinate facet.

**New whole-family value theorem.** For these actual S5/I4/I5 bodies, with the coordinate exposure bound on their C-side root endpoint,

    max(c,d)>=a>=min(c,d),  a>b>0,

implies

    T<=2.

This second theorem is an actual-body value inequality: it does not require the body to be stationary, does not require either G(C) or G(D) to have a specified sign, and does not impose the ordinary-B rigidity equation on a surrogate G. A complete three-domain exact certificate covers the full unbounded large-endpoint ranges. It has 1,649,998 nonnegative Bernstein coefficients, of which 1,254,665 are positive.

The structural theorem uses full fixed-parameter **body** maximality, not maximality within a chosen incidence stratum. It also uses V2's canonical-mark exposure, whose stated source hypothesis is full marked-frame variation. Thus the exclusion applies to the full marked-body[private-runtime-path] maximum relevant to the global-attainment setup. The A-star theorem alone is not being silently upgraded into the same statement for a bare fixed-endpoint-only optimizer lacking that exposure. This distinction is material: V2 expressly identifies mark exposure as its additional joint hypothesis. :contentReference[oaicite:0]{index=0}

No new mechanical E17 exclusion or attaining 110 body is claimed.

## 2. Input reading, authority and verification tier

The entire new journal was read consecutively through EOF: 1623 lines, 290726 bytes, SHA-256

    43f7ea4e86439660a9d8aa616559bfda19672008b5cb57bc3b9c7693f062a6ed.

All four newly supplied source units were read in full, including their mathematical qualifications and recovery descriptions. The required literal parent is

    minimum-0181
    SHA256 420ffe89544d6fbfd9ed6301c426209336f6352c0df589d4af045e8423d54beb.

Its proper33 conclusion is an accepted premise, not a task that was rerun. Earlier unchanged sources remain available in this chat.

The actual delivered source pins are:

    FULL_PATCH_A_STAR_FLATTENING_V1.md
    10786 bytes
    3d8b947f80c16dced9a1fbcc48a4c7f5f92159a58e91cac8f365441d4b20ba3d

    JOINT_MASS_EQUALITY_AND_E17_NO_UNIFORM_GAP_V1
    40615 bytes
    2c460625df162099bfba6437818bd8eff154d6d2f17d3f21e9ac2e4211c4d18e

    GLOBAL_HIGH_TRACE_ATTAINMENT_AND_ROOT_CUT_FIRST_VARIATION_V1
    15603 bytes
    52786c239b2ed0a438f276cb7c2baa108b5617168f5398a25da747e2b7515379

    NONPOSITIVE_MARK_COORDINATE_PATCH_ROOT_CHAIN_V2
    8707 bytes
    0fdbce320bac57c70047fa72690c53148726aa159ecbfa6d6075fbe7cab488c1

There is a provenance-pin discrepancy inside FULL_PATCH's dependency paragraph: it names the joint-mass dependency with an af3f... hash and the attainment dependency with a 46e7... hash, rather than the actual delivered bytes above. I use the delivered literal statements, which explicitly contain the needed J, equality and attainment results; I do not claim those historical pins authenticate these delivered files. No mathematical contradiction between the statements used here was found. The separately mentioned joint_equality_exact.py is not attached and was not replayed.

The new structural proof is analytic. The new value certificate and six actual controls were executed normally and then reconstructed from the new source alone in an empty directory, with byte-identical report and stdout. This is not a proof-assistant formalization. The inherited low-endpoint octant value theorem and large-minimum-endpoint theorem are used at their stated accepted scopes; their longer original computational capsules were not independently replayed.

## 3. Structural proof: no imported proper33-only ordinary-facet assumption

### 3.1. Setup and genuine free facets

Use

    A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
    alpha=a-b>0, s=a+b,
    hc=s+c, hd=s+d,
    ell=a+(d-a)x+(c-a)y-alpha*z,
    n=hc*x+hd*y,
    V=int_P1, J=int_P(x,y,z), E=int_Pell, N=int_Pn,
    r=N/V, q=N/E, t=6V, T=N/(6VE), G=n-r-q*ell,
    LB=-G(B)/3, LC=-G(C)/3, LD=-G(D)/3.

E denotes an integral. Every occurrence of r,q,G below belongs to this same actual uniformly filled body.

For T>2, the supplied full-patch theorem permits a>b after interchanging A,B, puts P in z>=0, and makes A simple with facets x=0,y=0,z=0. Its proof allows expanded coordinate patches. :contentReference[oaicite:1]{index=1}

Reflect x,y once, if necessary, so Fx is expanded and Fy=ABD. **Do not subsequently order c,d:** c is now the endpoint of the expanded patch, and either endpoint may be larger.

By V2, C,D are true vertices. Therefore AC and AD are true axis edges, and all auxiliary vertices of Fx have positive z. The expanded coordinate cycle is

    A,B,U,C  or  A,B,U,R,C,

with BC not a true edge. In the pentagonal case UR is a true root edge. All auxiliary true vertices have positive G. A one-mark free facet is a genuine triangle XUV with G(U)=G(V)=-G(X)/3>0. Whole-facet hinges, rather than hinges of arbitrary triangulation pieces, are the allowed reactions. :contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3}

The true edge BD has a second free maximal facet F_BD containing exactly B,D. It cannot also contain C: the BCD plane would support Fx along BC, contradicting expansion. The only other possible free facets, apart from the base Fz and root, are a CD facet and ordinary one-mark B,C,D triangles. No additional A facet survives the A-star theorem; no mark-free free facet survives the positive-G spike condition.

A CD facet, if present, makes CD a true edge: its only nonpositive vertices are C,D, so they are adjacent in that convex polygon. Together AC,AD,CD close the **entire** base facet, hence Fz=ACD. There is at most one additional CD facet.

### 3.2. The whole BD hinge makes all ordinary B/D bases root minima

The whole BD hinge uses H=y>=0. It implies

    max_P G>LB,  max_P G>LD.                          (3.1)

For the first inequality, a hypothetical G<=LB makes every triangle in the integration fan of F_BD from B contribute nonpositively. The triangle incident to the actual edge BD contributes strictly negatively because G(D)<=0<LB. This contradicts the single whole-polygon hinge. Fan from D for the second inequality when G(D)<0; when G(D)=0 it follows from auxiliary positivity.

For an ordinary triangle XUV with equal positive base level L, a nonroot base yields G<=L on P: both incident true facets decrease G away from UV, and their actual edge tangent cone supplies the global support. A root-maximum base yields the same conclusion from its support equation. Consequently (3.1) excludes nonroot and root-maximum bases for ordinary B or D facets. Their bases must be the minimum-G root edge.

Since G=n-r is nonconstant on the positive-area root, that minimum edge is unique. It cannot have root, B and D as three incident facets. Thus there is at most one ordinary B/D facet in total.

This is a **new argument in the enlarged octant**. The previous general “at most one ordinary facet, root-minimum base” theorem was stated only for proper33 or negative-z bodies; I have not imported it without its hypothesis. :contentReference[oaicite:4]{index=4} :contentReference[oaicite:5]{index=5}

### 3.3. The C-side coordinate edge cannot lead to an ordinary C facet

Let R be C's auxiliary neighbor on Fx. The second facet at CR contains either C alone or C,D. Suppose it is an ordinary triangle CRS, and set L=LC>0.

**Root-minimum base.** If RS is a root edge with n=K, its support is

    F=(K-hd)*ell+c*(n-K).

The root-minimum body side is F>=0. But R=(0,y_R,z_R), ell(R)=0 and z_R>0 give

    F(A)=(a-c)K-a*hd=-hd*alpha*z_R<0.

This is impossible.

**Root-maximum base.** Its body side F<=0 implies G<=LC. If c<=d, then LC<=LD, contradicting (3.1). If c>d, D's strict support condition gives

    F(D)=(c-d)(s+c+d-K)<0,
    K>s+c+d.

The actual coordinate exposure at R gives

    K=hd*y_R<=hd*(s+2c)/hc.

These bounds conflict because

    s+c+d-hd*(s+2c)/hc=c(c-d)/hc>0.

Thus neither endpoint order permits a root-maximum ordinary C facet here.

**Nonroot base.** The global cap G<=LC now has maximizing face exactly RS. From (3.1), LC>LB,LD. Hence neither an ordinary B nor an ordinary D triangle can contain R or S; their auxiliary levels would be smaller. The second facet of RS cannot be root, Fx, Fy or Fz, and a different C facet would share the three noncollinear points C,R,S. It must therefore be F_BD.

Thus BR is also an edge of Fx. R is both the B-neighbor and C-neighbor, so Fx=ABRC and B is simple. A CD facet would have a strictly negative whole hinge under the cap G<=LC, using G(C)=-3LC and G(D)<LC; it is absent. C is then simple with Fx,Fz,CRS, so CS is a true edge of Fz. The common D,S points of Fz and F_BD give the true edge DS.

The actual edges now close five entire facets:

    Fx=ABRC, Fy=ABD, Fz=ACSD,
    F_BD=BDSR, F_C=CRS.

Their six vertices have closed vertex figures; this is the complete boundary of a triangular prism. There are at most two possible root vertices R,S, contradicting positive root area. No independent motion of a prism integration triangle was used.

Therefore the second facet at CR is F_CD. It follows that Fz=ACD, C is simple with Fx,Fz,F_CD, and there are **no ordinary C facets anywhere**.

### 3.4. An ordinary D root minimum is also impossible

Suppose an ordinary D facet exists. There is then no ordinary B facet by Section 3.2, so B is simple.

If Fx were the quadrilateral ABUC, F_BD and F_CD would share the true edge DU. The resulting entire facets BDU,CDU,ACD,ABD,ABUC form a closed five-vertex pyramid and leave no positive-area root. Hence Fx must be a pentagon, with a root endpoint R on Fx.

Let K be the ordinary D minimum-root n-level. Its support side must contain A, so

    (a-d)K-a*hc>=0.

This already fails for d>=a. For d<a, combine it with the root minimum and coordinate exposure:

    a*hc/(a-d)<=K<=n(R)<=hd*(s+2c)/hc.

The required inequality is the reverse of the exact positive identity

    a*hc^2-(a-d)*hd*(s+2c)
      =a*c^2+d(b+d)(s+2c)>0.                         (3.2)

No order between c,d was used. Ordinary D is excluded.

### 3.5. All auxiliaries are on the root, and the list is complete

Only F_BD,F_CD and an optional ordinary B minimum-root triangle remain. If B is simple, the quadrilateral Fx case has just been excluded, so Fx is a pentagon and both coordinate auxiliaries are root vertices. If B has its ordinary root triangle, its Fx-neighbor is root; a pentagonal Fx again has both auxiliaries on its unique root edge.

Fy and Fz are the canonical triangles, with strictly positive ell. An auxiliary outside the root cannot occur in them, in Fx, or in the optional B triangle. It would have only the two planes F_BD,F_CD available, insufficient to isolate a true three-dimensional vertex.

Thus P is root-only. Intersections with the root give exactly the three true incidence types below. This proves the structural theorem, including G(C)=0 or G(D)=0.

## 4. Exact remaining geometry before applying the value bound

All true supports are

    x,y,z>=0, ell>=0,
    1-x-beta*y-z>=0,
    1-x-y-k*z>=0,

with beta<1,k<1. An optional ordinary B facet adds

    ell-b+(b/K)n>=0,
    K=(4r+qb)/3 at a stationary body.

The actual support, boundedness, root area and irredundancy conditions remain essential. K is not an independently selected substitute for the body's r,q in the stationary system.

The full cycles, besides Fy=ABD and Fz=ACD, are:

    S5: Fx=ABU0RC, root=U0WR,
        F_BD=BDWU0, F_CD=CDWR.
        True counts 7/11/6.

    I4: Fx=ABUC, root=UVW,
        F_B=BUV, F_BD=BDWV, F_CD=CDWU.
        True counts 7/12/7.

    I5: Fx=ABURC, root=UVWR,
        F_B=BUV, F_BD=BDWV, F_CD=CDWR.
        True counts 8/13/7.

These coincide geometrically with the old S5/I4/I5 labels, but the derivation above covers the newly assigned two-nonpositive signs rather than relying on the old mixed-sign hypothesis.

For I4/I5, release only the ordinary B support. The resulting body is a genuine S5, not an assumed unbounded container. Indeed the retained R satisfies strict F_BD slack, which forces the released root intersection U0 on Fx to have 0<y(U0)<y(R). Its z is positive, as is the retained W. The six listed outer facet cycles then close the bounded S5 hull. The original I5 is exactly that S5 minus the tetrahedron B,U0,U,V; I4 is the closed cut endpoint U=R.

## 5. New actual-body high-endpoint value theorem

### 5.1. An exact five-parameter outer body and one real cut

Normalize a=1. In this section y and zeta denote the **y-coordinates** of U0 and R; zeta is not a spatial z-coordinate. Put

    alpha=1-b, hc=1+b+c, hd=1+b+d,
    Delta=zeta-y>0,
    D=Delta+d[y/b+(1-zeta)/c],
    xW=Delta/D,
    yW=y[1+(d/b-1)xW].

The three root points are

    U0=(0,y,[1+(c-1)y]/alpha),
    R=(0,zeta,[1+(c-1)zeta]/alpha),
    W=(xW,yW,[1+(d-1)xW+(c-1)yW]/alpha).

The exposure of C gives the actual bound

    0<y<zeta<=1+c/hc.                                (5.1)

For every actual outer S5, D>0. Let

    tX=(1+c*zeta-b*y)/alpha,
    tR=d*xW*Delta/alpha,
    t0=tX+tR,
    e0=d*t0+[1+c+c^2*zeta-b^2*y]/alpha,
    n0=hc*t0+hd[1+c*zeta+c*zeta^2-b*y^2]/alpha
                +tR[hd(y+zeta+yW)+hc*xW].             (5.2)

These are **t0=6V0, e0=24E0, n0=24N0 of that actual S5**. One D-apex fan proves them: the only facets not through D are Fx and the root. The planar Fx integrals used are

    2 Area(Fx)=[1+c*zeta-b*y]/alpha,
    6 int_Fx ell=[1+c+c^2*zeta-b^2*y]/alpha,
    6 int_Fx y=[1+c*zeta+c*zeta^2-b*y^2]/alpha.

For a B-root cut, let rho be its fraction along U0R and kappa its fraction along U0W. Put

    A2=b*hc+hd*y(d-b),
    D1=b*c*D,
    M=(n(W)-n(U0))/(n(R)-n(U0))=c*A2/(hd*D1),
    kappa=rho/M,
    0<=rho<=min(1,M),
    K=hd(y+rho*Delta).

The actual removed volume, expressed as six times volume, is

    vcut=b^2*hd*Delta^2*rho^2/(alpha*A2).

The original moments of the cut body satisfy

    t=t0-vcut,
    e=e0-b*vcut,
    ncal=n0-vcut[hd*y+2K],
    T=ncal/(t*e).                                    (5.3)

For full first moments, if deltaV=vcut/6 and the new root vertices are U,V,

    J_cut=J_outer-deltaV*(B+U0+U+V)/4.

Thus E and N are not reweighted independently: the deleted region is one actual tetrahedron, with ell-values b,0,0,0 and n-values 0,n(U0),K,K.

### 5.2. Complete cut-length partition

The identity

    M-1=b(c-d)[1+c/hd-zeta]/D1                       (5.4)

determines the shorter available root edge exactly.

For c>=1>=d, (5.1) gives zeta<=1+c/hc<=1+c/hd, so M>=1 and rho in [0,1] covers all cuts.

For d>=1>=c, split at zeta=1+c/hd. Above this level M>=1 and rho is the cut parameter. Below it M<=1 and kappa in [0,1] is the cut parameter, with rho=M*kappa. The equality is included in both closed domains. This partition is essential: independently allowing rho,kappa to range through [0,1] creates cuts beyond the actual root triangle.

### 5.3. Exact continuous certificate

The recovery source constructs the polynomial numerator of

    2*t*e-ncal

from (5.2)-(5.3), in the following three complete domains. In every row, b and the remaining bounded endpoint, xi,sigma,pi lie in the closed unit cube, and h>=0 is unbounded. Write y=Z*sigma/H and zeta=Z/H.

    highC:
        c=1+h, 0<=d<=1,
        H=hc, Z=(hc+c)*xi, rho=pi.

    highD_R:
        d=1+h, 0<=c<=1,
        H=hc*hd,
        Z=hc*(hd+c)+xi*c*(d-c), rho=pi.

    highD_W:
        d=1+h, 0<=c<=1,
        H=hd, Z=(hd+c)*xi, kappa=pi, rho=M*pi.

After clearing only denominators that are positive on actual bodies, each numerator is a polynomial in h. Every h-coefficient has nonnegative Bernstein coefficients on the whole closed five-dimensional cube. The transformation matrices are integer-scaled; the source independently checks their exact inverse identities, so the computed coefficient representation is not accepted merely from its signs.

Counts:

    highC:   267330 coefficients; 191532 positive, 75798 zero.
    highD_R: 847833 coefficients; 673309 positive, 174524 zero.
    highD_W: 534835 coefficients; 389824 positive, 145011 zero.
    Total:  1649998 coefficients; 1254665 positive, 395333 zero.

Since h>=0, all three numerators are nonnegative on their full domains. Since actual t,e are positive,

    T<=2.

This includes S5 at zero cut and I4 at its appropriate endpoint cut. No geometric or moment-feasibility pruning is used. Closed algebraic boundaries where a body degenerates are included in the polynomial test but are not renamed actual strict-incidence bodies. No noncompact end in the stated endpoint domains is omitted.

### 5.4. Completion of the assigned value exclusion

If 0<c,d<a, contract the actual root slightly toward an interior root point with x,y,z>0. The resulting actual root-only bodies have proper coordinate triangles, retain ell, and their V,E,N converge to the original body's integrals. The accepted octant root-only theorem gives T<203/100 along the contraction, hence T<=203/100 at the enlarged-patch limit. Its stated marked-closure bound has a margin of 1/100 below 51/25. :contentReference[oaicite:6]{index=6}

If one endpoint is at least a and the other at most a, the new certificate above gives T<=2. If both exceed a, the accepted large-minimum-endpoint theorem, min(c,d)>=13a/16 => T<2, applies. Its notebook statement covers all actual shapes/overhangs; no new replay is claimed here. :contentReference[oaicite:7]{index=7}

Thus every endpoint case of the structural family has T<=203/100. This closes the assigned full marked one-expanded/two-nonpositive high-maximizer sector, without borrowing the old mixed-sign high-c certificate.

## 6. Actual controls, nonwinning geometry and two failed shortcuts

The source preserves six independently reconstructed actual bodies. All have the exact facets, true edges, three positive apex fans, original V,J,E,N, own G, whole BD/CD hinge residuals, root reaction residuals and own-centroid Euclidean mechanical packets. All are nonstationary and T<2; none is 110.

Input convention: a=1; the tuple is (b,c,d,beta,k), followed by rho. The ordinary B cut, when rho>0, is the actual plane ell-b+(b/K)n>=0 with K from Section 5, not an imposed stationary G level.

    LOW_S5:
      (1/5,1/2,1/2,3/10,-1/2), rho=0.
      T=13514694459/9679319540, own strict 5/5/8, weak000.

    HIGH_D_S5:
      (1/3,2/5,5/4,1/10,-1/2), rho=0.
      T=48161782001/39242997928, own strict 6/6/10, weak000.

    HIGH_D_I5:
      same tuple, rho=1/4.
      T=249333102156310068427/203062943864410097381,
      own strict 6/7/11, weak000.

    HIGH_C_S5:
      (1/7,21/20,2/3,-1/5,-1/4), rho=0.
      T=113784686308457839/120221914511792284,
      own strict 5/5/8, weak000.

    HIGH_C_I4:
      same tuple, rho=1.
      T=4039375512538562934675211799239/
        4268073726785168089337080114684,
      own strict 5/5/8, weak000.

    HIGH_D_I4_SIGN_EXIT:
      (1/3,2/5,5/4,1/10,-1/2), rho=1.
      T=116944654022124449/95715108287326672,
      own strict 6/5/9, weak000.

The first five have G(C),G(D)<0, positive G at every auxiliary and both coordinate-mark supports. The sixth has G(C)>0>G(D), while retaining the same actual support and auxiliary positivity tests. Thus the root-corner cut need not preserve the two-nonpositive sign sector. The unconditional high-endpoint value proof does not require it to do so.

A second useful negative result is exact:

    T(HIGH_D_I5)>T(HIGH_D_S5).

Therefore releasing the ordinary-B cut does **not** in general increase T. The proof above uses the linked tetrahedral changes in all moments, not an unsupported comparison with the outer S5.

For these two controls the original integrals are:

    HIGH_D_S5:
      V=11941/32712,
      J=(144863/1537464,
         220521059/1426766592,
         370467889/2853533184),
      E=410801/1962720,
      N=48161782001/85605995520.

    HIGH_D_I5:
      V=2427416561/6663303552,
      J=(1502486971626377/15948137293856256,
         39339063593661317/255170196701700096,
         65916440268545107/510340393403400192),
      E=83653933621/399798213120,
      N=19584722500692017/34875197726883840.

All six controls' complete moments and incidences are reconstructed by the source, not only retained by a report hash. All 280 true-edge primal/polar primitives are nonzero. No claim of a whole-path mechanical census is made.

An initial algebraic overcover let a corner-cut fraction run past the shorter root edge. Its failed coefficient test was not a body counterexample. The exact M-partition in (5.4) is the replacement; the final certificate covers only the correct complete parameterizations, without independent root-triangle masses.

## 7. Recovery capsule and actual execution

    CPython 3.13.5; SymPy 1.14.0; NumPy 2.3.5.
    Assertions enabled; no random inputs; no external files or parent import.

    OPENBLAS_NUM_THREADS=1 python one_expanded_v1.py > one_expanded_v1.out
    sha256sum one_expanded_v1.py one_expanded_v1.json one_expanded_v1.out

Pins:

    source: 13251 bytes
    SHA256 954f03ce2d36480d65b4fca3781b31c72e1310bb4664423f081697eebeebf0eb
    report: 93206 bytes
    SHA256 6f2c4c535d7b64db0955d94e1e3c18e10e29c8aa90cd5bee7c0777cc323c854f
    stdout: 959 bytes
    SHA256 d3a34a134ec2b1575f5ebb7361ca36875b8b2cb45bc71e2520883a3a59ea0db2

Complete expected stdout:

    ORDINARY_C_AND_D_ROOT_SUPPORT_IDENTITIES_PASS
    highC NONNEGATIVE=267330 POSITIVE=191532 ZERO=75798
    highD_R NONNEGATIVE=847833 POSITIVE=673309 ZERO=174524
    highD_W NONNEGATIVE=534835 POSITIVE=389824 ZERO=145011
    ALL_THREE_CONTINUOUS_HIGH_ENDPOINT_VALUE_DOMAINS_PASS
    SIX_ACTUAL_TRUE_HULLS_THREE_FANS_OWN_MOMENTS_AND_MECHANICS_PASS
    LOW_S5 T=13514694459/9679319540 SUH=(5, 5, 8)
    HIGH_D_S5 T=48161782001/39242997928 SUH=(6, 6, 10)
    HIGH_D_I5 T=249333102156310068427/203062943864410097381 SUH=(6, 7, 11)
    HIGH_C_S5 T=113784686308457839/120221914511792284 SUH=(5, 5, 8)
    HIGH_C_I4 T=4039375512538562934675211799239/4268073726785168089337080114684 SUH=(5, 5, 8)
    HIGH_D_I4_SIGN_EXIT T=116944654022124449/95715108287326672 SUH=(6, 5, 9)
    B_CORNER_REMOVAL_MONOTONICITY_COUNTERCONTROL_PASS
    total_coefficients=1649998 positive=1254665
    report_bytes=93206
    report_sha256=6f2c4c535d7b64db0955d94e1e3c18e10e29c8aa90cd5bee7c0777cc323c854f
    ONE_EXPANDED_TWO_NONPOSITIVE_V1_RECOVERY_PASS

The final six-control source was run normally and then copied alone into a separate directory. The second report and stdout matched byte for byte. Optional copies: [source](sandbox:/mnt/data/one_expanded_v1.py), [full report](sandbox:/mnt/data/one_expanded_v1.json), [stdout](sandbox:/mnt/data/one_expanded_v1.out).

The complete executable source follows. The coefficient arrays are regenerated and verified by it; hashes in the report are not substitutes for an unavailable coefficient table.

```python
#!/usr/bin/env python3
"""ONE_EXPANDED_TWO_NONPOSITIVE_ROOT_REDUCTION_AND_VALUE_V1.
CPython 3.13.5; SymPy 1.14.0; NumPy 2.3.5. Assertions enabled.
No RNG, external files, parent import or floating arithmetic.
Parent minimum-0181,
420ffe89544d6fbfd9ed6301c426209336f6352c0df589d4af045e8423d54beb.
Universal structural proof is in the handoff. Exact value certificates
cover three whole endpoint/shape domains. Controls are NONSTATIONARY.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb,lcm
from pathlib import Path
import hashlib,json
import numpy as np
import sympy as S


def identities():
    a,b,c,d,K,q=S.symbols('a b c d K q');s=a+b;hc=s+c;hd=s+d
    assert S.expand(a*hc-(a-c)*(s+2*c)-c*(b+2*c))==0
    assert S.expand(a*hc**2-(a-d)*hd*(s+2*c)-a*c*c-d*(b+d)*(s+2*c))==0
    assert S.expand((K-hd)*d+c*(hc-K)-(c-d)*(s+c+d-K))==0
    assert S.cancel(s+c+d-hd*(s+2*c)/hc-c*(c-d)/hc)==0
    y,z=S.symbols('y z');hc1=1+b+c;hd1=1+b+d
    D1=b*c*(z-y)+d*(c*y+b*(1-z));A2=b*hc1+hd1*y*(d-b)
    assert S.expand(c*A2-hd1*D1-b*(c-d)*(1+b+c+d-hd1*z))==0
    return dict(C_min_gap='c*(b+2*c)',D_min_gap='a*c^2+d*(b+d)*(a+b+2*c)',
                C_max_gap='c*(c-d)/(a+b+c)',status='five exact identities; geometric use in handoff')


def value_polynomial(case):
    b,c,d,r,s,p,h=S.symbols('b c d r s p h')
    vs=(b,d if case=='highC' else c,r,s,p,h)
    P=lambda e:S.Poly(e,*vs)
    B=P(b);C=P(1+h if case=='highC' else c)
    D=P(d if case=='highC' else 1+h)
    hc=1+B+C;hd=1+B+D;al=1-B;sp=P(s);pp=P(p)
    if case=='highC':H=hc;Z=(hc+C)*P(r)
    elif case=='highD_R':H=hc*hd;Z=hc*(hd+C)+P(r)*C*(D-C)
    elif case=='highD_W':H=hd;Z=(hd+C)*P(r)
    else:raise ValueError(case)
    # Outer S5 has y(U0)=Z*s/H, y(R)=Z/H. Dn/H is b*c
    # times its common root-intersection denominator. No free masses.
    D0=B*C*Z*(1-sp)
    Dn=D0+D*(C*Z*sp+B*H-B*Z)
    Tx=H+C*Z-B*Z*sp
    Rn=D*B*C*Z**2*(1-sp)**2
    TT=Tx*Dn+Rn
    EX=(1+C)*H+C**2*Z-B**2*Z*sp
    EE=D*TT+EX*Dn
    FY=H**2+C*Z*H+C*Z**2-B*Z**2*sp**2
    NN=hc*H*TT*Dn+hd*FY*Dn**2+Rn*(
        hd*(Z*(2*sp+1)*Dn+C*Z**2*sp*(D-B)*(1-sp))
        +hc*H*B*C*Z*(1-sp))
    AA=B*hc*H+hd*Z*sp*(D-B)
    if case=='highD_W':
        # p is the fraction on U0W; fraction on U0R is M*p.
        DC=B**2*C**2*Z**2*(1-sp)**2*AA*pp**2
        TN=hd*Dn*TT-DC;EN=hd*Dn*EE-B*DC
        NN2=hd*Dn*NN-DC*Z*(3*sp*hd*Dn+2*(1-sp)*C*AA*pp)
        Q=2*TN*EN-al*hd*Dn*NN2
        denominator='(1-b)^2*hd^2*Dn^4*H^2'
    else:
        # p is the fraction on U0R; fraction on U0W is p/M.
        DD=B**2*hd*Z**2*(1-sp)**2*pp**2
        TN=TT*AA-DD*Dn;EN=EE*AA-B*DD*Dn
        NN2=NN*AA-DD*Dn**2*hd*Z*(3*sp+2*(1-sp)*pp)
        Q=2*TN*EN-al*AA*NN2
        denominator='(1-b)^2*Dn^2*AA^2*H^2'
    return Q,denominator


def coefficient_certificate(poly,gens):
    poly=S.Poly(poly,*gens);degrees=tuple(map(int,poly.degree_list()))
    ar=np.zeros(tuple(d+1 for d in degrees),dtype=object)
    for exp,co in poly.terms():ar[exp]=int(co)
    scale=1
    for ax,d in enumerate(degrees):
        m=lcm(*[comb(d,k) for k in range(d+1)]);scale*=m
        mat=np.array([[comb(i,k)*(m//comb(d,k)) if k<=i else 0
                       for k in range(d+1)] for i in range(d+1)],dtype=object)
        inv=np.array([[comb(d,k)*(-1)**(k-i)*comb(k,i) if i<=k else 0
                       for i in range(d+1)] for k in range(d+1)],dtype=object)
        assert np.array_equal(inv@mat,np.eye(d+1,dtype=object)*m)
        ar=np.moveaxis(ar,ax,0)
        ar=np.tensordot(mat,ar,axes=(1,0))
        ar=np.moveaxis(ar,0,ax)
    vals=ar.flat;zero=0;positive=0;minimum=None;sha=hashlib.sha256()
    for v in vals:
        assert isinstance(v,int) and v>=0
        sha.update((str(v)+'\n').encode())
        if v==0:zero+=1
        else:
            positive+=1
            minimum=v if minimum is None else min(minimum,v)
    assert positive>0
    return dict(degrees=degrees,scale=scale,positive=positive,zero=zero,
                min_positive_scaled=minimum,coefficient_sha256=sha.hexdigest())


def all_certificates():
    out={}
    for name in ('highC','highD_R','highD_W'):
        poly,den=value_polynomial(name);records=[];terms=poly.terms()
        for j in range(poly.degree(poly.gens[-1])+1):
            co=S.Poly.from_dict({e[:-1]:v for e,v in terms if e[-1]==j},poly.gens[:-1])
            rec=coefficient_certificate(co,poly.gens[:-1]);rec['height_power']=j;records.append(rec)
        out[name]=dict(degrees=poly.degree_list(),terms=len(terms),denominator=den,
                       height_coefficients=records,
                       domain='first five variables in closed [0,1]^5, h>=0',
                       status='ALL Bernstein coefficients nonnegative; exact inverse matrices checked')
    return out


def dot(x,y):return sum((a*b for a,b in zip(x,y)),F(0))
def sub(x,y):return tuple(a-b for a,b in zip(x,y))
def cross(x,y):return (x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])
def det(x,y,z):return dot(x,cross(y,z))
def norm(n,h):
    k=abs(next(v for v in n if v));return tuple(v/k for v in n),h/k

def solve(ns,hs):
    den=det(*ns)
    if not den:return None
    co=(cross(ns[1],ns[2]),cross(ns[2],ns[0]),cross(ns[0],ns[1]))
    return tuple(sum(hs[i]*co[i][j] for i in range(3))/den for j in range(3))

def product_integral(pts,face,normal,f,h):
    axis=next(i for i in range(3) if normal[i]);value=F(0)
    for j in range(1,len(face)-1):
        ids=(face[0],face[j],face[j+1]);a,b,c=(pts[i] for i in ids)
        area=abs(cross(sub(b,a),sub(c,a))[axis]/normal[axis])/2
        ff=[f[i] for i in ids];hh=[h[i] for i in ids]
        value+=area*(sum(ff)*sum(hh)+sum(x*y for x,y in zip(ff,hh)))/12
    return value

CASES=(('LOW_S5',('1/5','1/2','1/2','3/10','-1/2'),'0'),
       ('HIGH_D_S5',('1/3','2/5','5/4','1/10','-1/2'),'0'),
       ('HIGH_D_I5',('1/3','2/5','5/4','1/10','-1/2'),'1/4'),
       ('HIGH_C_S5',('1/7','21/20','2/3','-1/5','-1/4'),'0'),
       ('HIGH_C_I4',('1/7','21/20','2/3','-1/5','-1/4'),'1'),
       ('HIGH_D_I4_SIGN_EXIT',('1/3','2/5','5/4','1/10','-1/2'),'1'))


def control(case):
    name,raw,fraction=case;b,c,d,beta,k=map(F,raw);p=F(fraction);al=1-b;hc=1+b+c;hd=1+b+d
    y=b/(1-c-al*beta);zr=c/(al+(c-1)*k);z=1-k*zr;delta=z-y
    den=delta+d*(y/b+(1-z)/c);xw=delta/den;yw=y*(1+(d/b-1)*xw)
    CAN=tuple(tuple(map(F,x)) for x in ((0,0,0),(0,0,1),(0,1,0),(1,0,0)))
    U0=(F(0),y,(1+(c-1)*y)/al);R=(F(0),z,zr)
    W=(xw,yw,(1+(d-1)*xw+(c-1)*yw)/al)
    nn=lambda x:hc*x[0]+hd*x[1]
    ell=lambda x:1+(d-1)*x[0]+(c-1)*x[1]-al*x[2]
    A2=b*hc+hd*y*(d-b);M=c*A2/(hd*b*c*den)
    # M=(nW-nU0)/(nR-nU0). Its exact sign partition is essential.
    assert M==(nn(W)-nn(U0))/(nn(R)-nn(U0))>0
    assert p<=1 and p<=M
    K=hd*(y+p*delta);vfrac=p/M
    U=tuple((1-p)*u+p*r for u,r in zip(U0,R))
    Vv=tuple((1-vfrac)*u+vfrac*w for u,w in zip(U0,W))
    hs=[((F(-1),F(0),F(0)),F(0)),((F(0),F(-1),F(0)),F(0)),
        ((F(0),F(0),F(-1)),F(0)),((1-d,1-c,al),F(1)),
        ((F(1),beta,F(1)),F(1)),((F(1),F(1),k),F(1))]
    if p==0:
        pts=CAN+(U0,W,R);kind='S5'
        faces=((0,1,4,6,2),(0,1,3),(0,2,3),(4,5,6),(1,3,5,4),(2,3,5,6))
    else:
        hs.append(((1-d-b*hc/K,1-c-b*hd/K,al),1-b))
        if p==1:
            pts=CAN+(R,Vv,W);kind='I4'
            faces=((0,1,4,2),(0,1,3),(0,2,3),(4,5,6),(1,3,6,5),(2,3,6,4),(1,4,5))
        else:
            pts=CAN+(U,Vv,W,R);kind='I5'
            faces=((0,1,4,7,2),(0,1,3),(0,2,3),(4,5,6,7),(1,3,6,5),(2,3,6,7),(1,4,5))
    assert len(set(pts))==len(pts)
    for face,(n,h) in zip(faces,hs):
        assert all((h-dot(n,x)==0 if i in face else h-dot(n,x)>0) for i,x in enumerate(pts))
    hull=set()
    for i,j,k0 in combinations(range(len(pts)),3):
        n=cross(sub(pts[j],pts[i]),sub(pts[k0],pts[i]))
        if not any(n):continue
        h=dot(n,pts[i]);sg=[h-dot(n,x) for x in pts]
        if min(sg)<0<max(sg):continue
        if max(sg)<=0:n=tuple(-v for v in n);h=-h
        hull.add(norm(n,h))
    assert hull=={norm(n,h) for n,h in hs}
    recovered=set()
    for tri in combinations(range(len(hs)),3):
        x=solve([hs[i][0] for i in tri],[hs[i][1] for i in tri])
        if x is not None and all(h-dot(n,x)>=0 for n,h in hs):recovered.add(x)
    assert recovered==set(pts)
    edges=sorted({tuple(sorted((f[i-1],f[i]))) for f in faces for i in range(len(f))})
    assert all(sum(i in f and j in f for f in faces)==2 for i,j in edges)
    assert len(pts)-len(edges)+len(faces)==2
    def fan(apex):
        out=[];o=pts[apex]
        for idx,f in enumerate(faces):
            if apex in f:continue
            volume=F(0);J=[F(0)]*3
            for j in range(1,len(f)-1):
                pp=(o,pts[f[0]],pts[f[j]],pts[f[j+1]])
                w=abs(det(*(sub(x,o) for x in pp[1:])))/6;assert w>0
                volume+=w
                for i in range(3):J[i]+=w*sum(x[i] for x in pp)/4
            E=volume+(d-1)*J[0]+(c-1)*J[1]-al*J[2];N=hc*J[0]+hd*J[1]
            out.append(dict(facet=idx,V=volume,J=J,E=E,N=N))
        return out
    def total(rows):return (sum(x['V'] for x in rows),tuple(sum(x['J'][j] for x in rows) for j in range(3)),sum(x['E'] for x in rows),sum(x['N'] for x in rows))
    af,bf,df=fan(0),fan(1),fan(3);V,J,E,N=total(af)
    assert (V,J,E,N)==total(bf)==total(df)
    tx=(1+c*z-b*y)/al;tr=d*xw*delta/al;t0=tx+tr
    e0=d*t0+(1+c+c*c*z-b*b*y)/al
    n0=hc*t0+hd*(1+c*z+c*z*z-b*y*y)/al+tr*(hd*(y+z+yw)+hc*xw)
    drop=b*b*hd*delta*delta*p*p/(al*A2)
    assert t0-drop==6*V and e0-b*drop==24*E
    assert n0-drop*(hd*y+2*K)==24*N
    g=tuple(v/V for v in J);r=N/V;q=N/E;T=N/(6*V*E)
    gv=[nn(x)-r-q*ell(x) for x in pts];ev=[ell(x) for x in pts]
    assert gv[3]<0 and min(gv[4:])>0 and min(ev)>=0 and T<2
    assert (gv[2]>0) if name=='HIGH_D_I4_SIGN_EXIT' else (gv[2]<0)
    hC=[(b+2*c)*(x[1]-1)-al*x[2] for x in pts if x[0]==0]
    hD=[(b+2*d)*(x[0]-1)-al*x[2] for x in pts if x[1]==0]
    assert max(hC)==max(hD)==0
    hinge={lab:product_integral(pts,faces[idx],hs[idx][0],gv,[x[axis] for x in pts]) for lab,idx,axis in (('BD',4,1),('CD',5,2))}
    assert any(hinge.values())
    vxy=J[0]+J[1];rhs=(q*V-3*vxy,q*J[0]-J[1],q*J[1]-J[0],q*J[2]-vxy)
    rr=[product_integral(pts,faces[3],hs[3][0],gv,[F(1)]*len(pts) if j==0 else [x[j-1] for x in pts])-rhs[j] for j in range(4)]
    assert any(rr) and rr[0]+(d-1)*rr[1]+(c-1)*rr[2]-al*rr[3]==0
    shifted=[sub(x,g) for x in pts];poles=[tuple(v/(h-dot(n,g)) for v in n) for n,h in hs]
    up=[[] for _ in pts];st=[[] for _ in hs];packets=[]
    for i,j in edges:
        f,k0=[k for k,face in enumerate(faces) if i in face and j in face]
        prim=(dot(shifted[i],sub(shifted[j],shifted[i])),dot(shifted[j],sub(shifted[i],shifted[j])),dot(poles[f],sub(poles[k0],poles[f])),dot(poles[k0],sub(poles[f],poles[k0])))
        assert all(prim)
        up[i].append(prim[0]);up[j].append(prim[1]);st[f].append(prim[2]);st[k0].append(prim[3])
        packets.append(dict(edge=(i,j),facets=(f,k0),primitives=prim))
    suh=(sum(max(x)<0 for x in st),sum(max(x)<0 for x in up),sum(max(x['primitives'])<0 for x in packets))
    assert suh[0]+suh[1]-suh[2]==2
    return dict(name=name,kind=kind,endpoints=(F(1),b,c,d),beta=beta,k=k,cut_fraction=p,K=K,
                vertices=pts,facets=faces,edges=edges,halfspaces=hs,V=V,J=J,E=E,N=N,T=T,g=g,G=gv,ell=ev,
                A_fan=af,B_fan=bf,D_fan=df,BD_CD_hinges=hinge,root_reaction_residual=rr,
                ordinary_B_level_defect=None if p==0 else gv[1]+3*(K-r),
                strict_SUH=suh,weak_packets=0,edge_packets=packets,
                outer_yU0=y,outer_yR=z,outer_t=t0,outer_24E=e0,outer_24N=n0,M=M,
                two_nonpositive=(gv[2]<=0 and gv[3]<=0),
                status='genuine one-expanded uniform NONSTATIONARY control; not 110')


def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    return x


def main():
    ids=identities();cert=all_certificates();controls=[control(x) for x in CASES]
    assert controls[2]['T']>controls[1]['T']
    report=dict(version=1,identities=ids,certificates=cert,controls=controls)
    raw=(json.dumps(encode(report),sort_keys=True,indent=2)+'\n').encode()
    Path('one_expanded_v1.json').write_bytes(raw)
    print('ORDINARY_C_AND_D_ROOT_SUPPORT_IDENTITIES_PASS')
    totalcount=0;positive=0
    for name,z in cert.items():
        pp=sum(x['positive'] for x in z['height_coefficients']);zz=sum(x['zero'] for x in z['height_coefficients'])
        print(name+' NONNEGATIVE='+str(pp+zz)+' POSITIVE='+str(pp)+' ZERO='+str(zz));totalcount+=pp+zz;positive+=pp
    print('ALL_THREE_CONTINUOUS_HIGH_ENDPOINT_VALUE_DOMAINS_PASS')
    print('SIX_ACTUAL_TRUE_HULLS_THREE_FANS_OWN_MOMENTS_AND_MECHANICS_PASS')
    for z in controls:print(z['name']+' T='+str(z['T'])+' SUH='+str(z['strict_SUH']))
    print('B_CORNER_REMOVAL_MONOTONICITY_COUNTERCONTROL_PASS')
    print('total_coefficients='+str(totalcount)+' positive='+str(positive))
    print('report_bytes='+str(len(raw)))
    print('report_sha256='+hashlib.sha256(raw).hexdigest())
    print('ONE_EXPANDED_TWO_NONPOSITIVE_V1_RECOVERY_PASS')

if __name__=='__main__':main()
```

## 8. Remaining scope and useful continuation

There is no T>=51/25 survivor in the assigned one-expanded/two-nonpositive **full marked** sector under the accepted reactions. The most useful independent audit is the ordinary-C nonroot prism closure, followed by the cut-length identity (5.4) that makes the high-endpoint certificate complete. Neither argument uses the old mixed-sign c>d inference.

For a weaker optimization that fixes endpoints and forbids the mark/frame reactions used by V2, this handoff does not manufacture hC<=0 or canonical-mark truth from the A-star theorem alone. Such a weaker high optimizer would have to evade at least one of those hypotheses; it is not an actual countercontrol supplied here. The global-attainment/full marked optimization retains them at their stated scope.

The new value calculation is reusable outside stationarity: it covers all actual members of the stated root-only families with the C-side exposure bound and one endpoint on each side of a. It does not say that releasing a cut is monotone, that G-signs persist under a cut, or that an arbitrary root polygon can be replaced by one of these shapes.

Zero endpoints, other expansion/sign patterns without a proved incidence mapping, and the physical common-SPD/mechanical E17 bridge remain separate. The six controls are nonwinning bodies, not attaining witnesses. No global registry count or lower complexity endpoint changes: 34<=C_min<=622 remains the accepted interval, and the exact mechanical minimum remains unresolved. :contentReference[oaicite:8]{index=8}
