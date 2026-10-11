# minimum-0154

Historical AI scientific report · saved 2026-09-21 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# MULTI_APEX_CORNER_ROOT_203_AND_DETACHED_OBSTRUCTION_V1

## 1. Determination

This continuation gives a new continuous exclusion with several genuine pyramid contributions, a complete combinatorial reduction of a positive-octant E17 root-only sector, and an exact obstruction to extending the parent's endpoint comparison.

**New exclusion.** In the explicit unequal-endpoint class of Sections 2–4, the root may be any compact convex set containing a prescribed central polygon of its containing triangle. It can have arbitrarily many vertices or a curved boundary. Additional root-adjacent facets need not contain B: their positive-density anchors may be C or D. A computable condition on the actual containing body's volume, ell-integral and corner-pyramid numerator gives an actual dominating replacement in the parent's single-B-fan class. Consequently

    T(P) <= T(Q) <= Cstar < 203/100 < 51/25.

The concrete closed sector below allows removal of three quarters of the containing root's area. It includes bodies whose root meets z=0 only at a vertex, and nonempty continuous sectors in all ten marked E17 fan patterns described below. It is not a small contraction collar. The replacement retains the root plane, endpoint data and genuine ABC/ABD triangles, but generally changes the original volume, first moment and ell-integral; their changes are computed together.

**Complete E17 structural conclusion.** For a proper positive-octant root-only 10/17/9 body with 0<b,c,d<1, the root necessarily meets z=0 along an edge. Its six root vertices are simple. Its five remaining root-side facets have the exact order

    i triangles anchored at D,
    one BD quadrilateral,
    j triangles anchored at B,
    one BC quadrilateral,
    k triangles anchored at C,
    i+j+k=3.

There are ten marked patterns, or six under x-y reflection. Only one is the parent's all-B pattern. This is a classification of this specified marked geometric sector, not an identification with six entries of an unavailable global registry.

**Detached-root result.** A separate complete six-parameter containing geometry has a root disjoint from z=0 and a new non-B quadrilateral CDUV. Arbitrary convex roots in this geometry admit an exact original-moment reduction to at most four root vertices. Their fixed-container shape supremum is explicitly reduced to two one-variable rational/algebraic branches. However, the parent's subsequent e=f=0 trace comparison is false in this larger class: the rational interval in Section 7 has

    T(P_zeta)>201/100>max(2,T(P_zero)),
    every finite zeta>=100000000.

Every member is a genuine proper 8/14/8 body with a positive-area root. These countercontrols are nevertheless in the already closed prism class and have T<203/100. They are not threshold counterexamples. The obstruction is a surviving mixed C-D pyramid contribution, not a uniformly refilled projective surrogate.

The unrestricted root-only threshold, arbitrary positive-ell auxiliaries and the global minimum remain unresolved. No 110 construction, whole-E17 exclusion, registry decrement or change to 34<=Cmin<=622 is claimed.

## 2. Authority and common actual geometry

The complete current research-journal(20260921-015138).md, including the literal parent and its complete recovery, was read through line 1724/EOF in the resumed work. The authoritative parent is

    minimum-0149
    SHA-256 4ebbd83f4ad331b2b2a819368f40f83df9cdc61ac0128806f11bffedbca9f66b
    UNEQUAL_ENDPOINT_APEX_FAN_ROOT_BOUND_203_V1.

Its single-B-fan bound is used as a working premise. Its scope and its genuine marginal-preserving first replacement are not enlarged by fiat.  In particular, its e=f=0 operation is a coupled trace comparison, not preservation of V or Bell.  No source-authority conflict was found.

Use

    A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
    ell=1+(d-1)x+(c-1)y+(b-1)z,
    n=(1+b+c)x+(1+b+d)y,
    V=integral_P 1, J=integral_P (x,y,z),
    Bell=integral_P ell, N=integral_P n,
    T=N/(6 V Bell).

All these are ORIGINAL uniform-volume integrals.

Choose beta,s,t,e,f>0 and put

    b=1/(1+beta), c=e/(1+e), d=f/(1+f),
    Z=beta+s+t, Kc=1+sf+te,
    DU=1+(s+t)f, DV=1+(s+t)e,

    U=((1+f)(1+sf)/DU, t(1+e)f/DU, 0),
    Vroot=(s(1+f)e/DV, (1+e)(1+te)/DV, 0),
    W=(s(1+f)/Z, t(1+e)/Z, (1+beta)/Z).

To avoid ambiguity, Vroot denotes a point, whereas V denotes volume. Below, the root triangle is R=conv(U,Vroot,W) and the containing body is P_R=conv(T0,R). All three root points have positive x,y and satisfy ell=0. W is a containing-triangle corner, not automatically a vertex of a truncated-root body.

The actual original moments of P_R can be recovered from four positive tetrahedra. Define

    j=det(U-B,Vroot-B,W-B),
    d1=abs(det(D-B,U-B,Vroot-B)),
    d2=abs(det(D-B,Vroot-B,C-B)).

Then

    6 V_R=1+d1+d2+j,
    24 Bell_R=1+b+c+d+d1(b+d)+d2(b+c+d)+bj,

    24 J_R=B+C+D
      +d1(B+D+U+Vroot)
      +d2(B+C+D+Vroot)
      +j(B+U+Vroot+W).
                                                        (1)

N_R is obtained by applying the fixed linear function n to J_R. These data are not transported from a different centroid.

## 3. Three genuine corner contributions and their entire ell-marginal

Choose a central convex polygon K0 inside R by cutting off disjoint corner triangles at U,Vroot,W. On each side, the two endpoint cut fractions must sum to at most one, and K0 must have positive area. A particularly simple choice is the medial triangle. Let

    K0 subset F subset R,
    F compact and convex,
    P=conv(T0,F).

All these bodies are proper: every point of R has positive x,y, so the entire maximal coordinate facets of P are exactly ABC and ABD. The root plane remains ell=0 and its area remains positive.

The actual missing root regions R_U,R_V,R_W lie in the three chosen corner triangles. They need not be convex. Define cone(a,S) as the union of the segments from a to points of S; for a nonconvex S this is NOT the convex hull of a and S. There is an exact disjoint-interior decomposition

    P_R minus P
       = cone(D,R_U) union cone(C,R_V) union cone(B,R_W).
                                                        (2)

### Proof of the geometric partition

Use the parent's positive canonical-fixing projectivity only to verify set geometry. It sends the root plane to x'+y'+z'=2 and the containing triangle to a translated homothetic copy of the canonical BCD triangle. At heights between one and two, the true sections are Minkowski sums of that canonical triangle and the root.

A supporting line of a root corner chain has its normal in the normal cone of that containing-triangle corner. Otherwise a retained endpoint of the allowed corner triangle would have larger support value. Minkowski addition therefore translates that chain by the corresponding canonical vertex: D at U, C at Vroot and B at W. The three missing section regions are precisely the three scaled and translated root deficits. Their interiors are disjoint. Polygonal approximation retaining the central polygon proves the same statement for arbitrary compact convex F. Inverting the positive projectivity proves (2) in the original body. No uniform-image moment is used.

### Original density formulas

Let a_i be D,C or B, let h_i=ell(a_i) be d,c or b, let A_i be the PHYSICAL area of the corresponding actual missing root region, and let rbar_i be its actual area centroid. Put g=|grad ell|. The original missing moments are

    v_i=h_i A_i/(3g),
    E_i=h_i v_i/4,
    J_i=(v_i/4)(a_i+3 rbar_i),
    N_i=(v_i/4)(n(a_i)+3 mean_(R_i)n).           (3)

These formulas are valid for the possibly nonconvex region R_i because they integrate its actual union of pyramid rays, not its convex hull.

More strongly, its original ell-marginal has density

    A_i/g * (1-w/h_i)^2,  0<=w<=h_i,

and is zero above h_i. Equivalently, for every integrable psi,

    integral_cone(a_i,R_i) psi(ell)
      =(h_i A_i/g) integral_0^1 lambda^2 psi(h_i(1-lambda)) dLambda.
                                                        (4)

Its n-weighted version is

    (h_i/g) [n(a_i) A_i integral lambda^2(1-lambda)psi
                + integral_(R_i)n integral lambda^3 psi],

with the same argument h_i(1-lambda) in psi. Thus keeping the THREE actual corner areas fixed preserves the whole original ell-marginal. Total root area alone does not do so when the anchor heights differ.

When b,c,d are distinct, preservation of root area, V and Bell is equivalent to preservation of the three corner areas: the three linear rows have coefficients 1,h_i,h_i^2 and form a nonsingular Vandermonde matrix. This is a precise additional invariant for this geometric stratum, not a general replacement of actual moment constraints by free weights.

## 4. A complete multi-apex sector with a dominating parent body

Fill the U and Vroot deficits, retaining only the W deficit. More intrinsically, retain the original containing-triangle halfplanes and the root support halfplanes belonging to the W normal cone. The resulting root F_Q is convex, contains the entire U--Vroot edge, and satisfies F subset F_Q subset R. Put Q=conv(T0,F_Q).

Q belongs to the parent's complete single-B-fan class. Therefore T(Q)<=Cstar<sigma, where sigma=203/100. The actual difference Q minus P consists only of the D- and C-cone pieces in (2).

Let

    Wv=v_U+v_V, epsilon=E_U+E_V, etaN=N_U+N_V,
    m=max(c,d).

Then the ORIGINAL data obey

    V_P=V_Q-Wv, Bell_P=Bell_Q-epsilon, N_P=N_Q-etaN,
    epsilon<=m Wv/4.                                  (5)

Let kappa be any certified lower bound for each removed pyramid's mean n. One directly computable choice, using the two allowed root corner triangles T_U,T_V, is

    kappa=min((n(D)+3 min_(T_U)n)/4,
              (n(C)+3 min_(T_V)n)/4).

Consequently etaN>=kappa Wv. All extrema here are over real triangles and occur at their literal vertices.

**General criterion.** If

    kappa >= 6 sigma (Bell_R + m V_R/4),                (6)

then T(P)<=T(Q), strictly if Wv>0. Indeed, with tau=T(Q),

    6 tau V_P Bell_P-N_P
      =etaN-6 tau(Bell_Q Wv+V_Q epsilon-Wv epsilon)>0

whenever Wv>0, because tau<sigma, V_Q<=V_R, Bell_Q<=Bell_R, and all quantities are original integrals of nested bodies. If Wv=0 the bodies agree up to volume zero. This proves a real dominating replacement, not merely a comparison with an independently chosen moment tuple.

### An explicit closed numerical sector

The following simpler hypotheses imply (6):

    max(c,d)<=21/100,
    V_R<=27/100,
    Bell_R<=3/40,
    n>=109/100 at D,C and at the vertices of T_U,T_V.
                                                        (7)

The exact positive margin is

    109/100-6(203/100)[3/40+(21/100)(27/100)/4]
      =7697/2000000>0.                                (8)

Thus EVERY compact convex root between the prescribed central polygon and R is excluded below 51/25. No root-complexity, controller genericity or nondegeneracy of an individual corner chain is assumed. At a merger, the actual maximal facets are merged. If the medial triangle is the protected polygon, roots may lose three quarters of the original area and may cease to meet z=0 in an edge.

After filling the two corners, the parent's genuine area-preserving root reduction can be applied to Q. Hence the entire class in (6), or in (7), has an actual dominating proper successor with at most eight vertices and seven facets. Root area, V and Bell generally change in the filling step; the subsequent parent reduction preserves the new Q moments. Full J and mechanics are not preserved by the combined operation.

### A nonempty unequal-endpoint sector

Take

    (beta,s,t,e,f)=(3,1/2,9/8,1/9,1/4),
    (b,c,d)=(1/4,1/10,1/5),
    U=(1,2/9,0), Vroot=(1/17,18/17,0),
    W=(5/37,10/37,32/37).

For the medial protected triangle,

    V_R=8791/33966 <27/100,
    Bell_R=199873/2717280 <3/40,
    Area_xy(R)=640/1887,
    j=1280/5661, d1=32/153, d2=2/17.

The minimum of n on the two allowed half-corner triangles and their canonical apices is

    13769/12580=109/100+71/15725.

All inequalities have strict slack, so they describe a nonempty open five-parameter region, not just this one example.

Two large root changes at these same endpoints are retained:

|Actual root|True V/E/F|Original volume|Original Bell|Root xy area|
|---|---:|---|---|---|
|Full triangle R|7/11/6|8791/33966|199873/2717280|640/1887|
|conv(W,(W+U)/2,(U+Vroot)/2,(Vroot+W)/2)|8/14/8|8407/33966|198593/2717280|320/1887|
|Medial triangle of R|7/14/9|8087/33966|196993/2717280|160/1887|

The last two roots meet z=0 only at (U+Vroot)/2. Their coordinate facets remain the genuine triangles. Their full original first moments are given by (1) minus the actual corner moments (3). For a half-corner, rbar is the mean of its three specified root vertices. Its removed volumes at D,C,B are respectively 128/16983,64/16983,160/16983, and its removed Bell values are 32/84915,8/84915,10/16983. This is a complete exact reconstruction of X,Y,Z,N for every displayed change, not an old centroid carried along.

## 5. Complete positive-octant E17 root-fan classification

Assume P is a proper root-only 10/17/9 polytope, P subset {x,y,z>=0}, 0<b,c,d<1. Its four canonical points are true off-root vertices, so the root has exactly six true vertices.

Every root edge meets a distinct neighboring maximal facet. The coordinate facets x=0 and y=0 are not root-edge neighbors, because all root points have positive x,y. If z=0 were not a root-edge neighbor either, the root, its six different neighbors and these three coordinate facets would require at least ten facets. Therefore F meets z=0 in an edge U0V0. The base is the actual pentagon A D U0 V0 C.

The root's six neighbors, the root itself and the two coordinate triangles already exhaust the nine facets. No further facet is available. A has only its three positive-octant facets. A nonbase facet cannot contain both C and D, since CD is an interior diagonal of the base pentagon. It cannot contain B,C,D, since the plane x+y+z=1 separates A from every positive-endpoint root point. Thus the five remaining root-side facets consist of triangles anchored at B,C or D, and exactly one quadrilateral through each of BD and BC.

Following the root from U0 to V0 away from the base edge gives exactly

    D^i, BD, B^j, BC, C^k,  i+j+k=3.                   (9)

A change of triangle anchor needs the corresponding two-canonical facet; each such facet occurs only once. This proves the stated order, not merely its facet-size count. The canonical degrees are 3, j+4, k+3, i+3. Their sum is 16, leaving total degree 18 at the six root vertices; each root vertex is therefore simple.

The six reflection representatives are

    (0,3,0), (0,2,1), (0,1,2),
    (0,0,3), (1,1,1), (1,0,2).

The first is the parent's closed all-B pattern. The present corner criterion gives nonempty continuous exclusions in the other five patterns, but does not exclude their entire unrestricted parameter spaces.

### Exact realizations of all ten marked patterns

In the canonical-fixing root-parallel image use the triangle with xy corners

    U'=(9/5,1/5), V'=(1/5,9/5), W'=(1/5,1/5),
    z'=2-x'-y'.

At each corner p, let prev,next be its two neighboring corners in the order U',V',W'. For a corner chain with l>0 segments use ALL l+1 points

    p+((1-r/l)^2/8)(prev-p)+(r/l)^2(next-p)/8,
    r=0,1,...,l.

For l=0 retain p. Choose chain lengths (i,k,j) at U',V',W'. Map every point back to the ORIGINAL coordinates by

    L=6+x'+6y',
    (x,y,z)=(5x'/L,10y'/L,4z'/L).

This projectivity is used to construct geometry; every body's uniform moments are reintegrated in these original coordinates. All ten roots contain the ORIGINAL medial triangle, so all ten controls satisfy (7). The construction gives exactly six true root vertices and the facets (9), including zero-length triangle blocks. It is not a numerical search for realizations.

For (i,j,k)=(1,1,1), the six original root vertices, labels 4..9, are

    (4/5,2/5,0), (10/11,5/22,1/11),
    (5/19,5/19,14/19), (5/43,20/43,28/43),
    (5/79,80/79,4/79), (1/8,1,0).

Together with canonical labels 0..3, its complete maximal facet vertex sets are

    012, 013, 02349, 345, 1356,
    167, 1278, 289, 456789.

It is an actual proper 10/17/9 body, with additional non-B D- and C-triangles. Its original data are recovered exactly from the containing body by subtracting the three triangular corner cones. Their root xy areas at D,C,B are

    1/132, 15/10744, 375/30229,

their volumes are

    1/1485, 1/16116, 125/90687,

and their Bell values are

    1/29700, 1/644640, 125/1450992.

For their first moments use v/4 times the sum of the canonical apex and the three literal root vertices of the corner triangle: (U,4,5), (Vroot,8,9), (W,6,7), respectively. These complete formulas give V>32/125, Bell>73/1000 and N<27/125, hence T<2 for this control. The useful result is the whole continuous sector, not this nonwinning numerical value. No equilibrium-preservation or 110 assertion follows from the root manipulation.

## 6. A complete detached-root geometry and its exact shape optimum

Now introduce a sixth independent positive parameter zeta. Put

    R0=s+t+zeta Z,
    DU=1+f R0, DV=1+e R0,

    U=((1+f)(1+fs(1+zeta))/DU,
       t(1+e)f(1+zeta)/DU,
       (1+beta)zeta f/DU),
    Vroot=(s(1+f)e(1+zeta)/DV,
       (1+e)(1+et(1+zeta))/DV,
       (1+beta)zeta e/DV),
    W=(s(1+f)/Z,t(1+e)/Z,(1+beta)/Z).             (10)

All root coordinates are positive. Let F be the image under W+u(U-W)+v(Vroot-W) of any compact convex K subset Delta containing the edge [(1,0),(0,1)] and having positive area. Then P=conv(T0,F) is proper, its root is disjoint from z=0, and it has the new actual non-B quadrilateral CDUVroot.

There is a genuine three-piece decomposition

    P=T0 union conv(B,CDUVroot) union conv(B,F),          (11)

with disjoint interiors. In the root-parallel image the containing triangle has the same W' corner as before, but its two other sides are shortened by 1/(1+zeta). The plane CDUVroot is then directly supporting. In original coordinates it is

    x+y+kappa_zeta z<=1,
    kappa_zeta=1-(1+zeta)Kc/[(1+beta)zeta].             (12)

The changing root pyramid in (11) again has formula (3) with anchor B. Therefore arbitrary root complexity can be reduced to

    K=conv((1,0),(0,1),(0,v),(u,0)), 0<=u,v<=1, uv<1,

at fixed V, Bell, root area and the entire original ell-marginal, with no smaller N. The successor has at most eight true vertices and eight facets. This extends the geometric first part of the parent; the endpoint-comparison second part will fail below.

### Full original moments

Let j,d1,d2 be the positive determinants of BUVrootW, BDUVroot and BDVrootC. Their exact values are

    j=(1+e)(1+f)Kc/(Z DU DV),
    d1=f(1+zeta)(1+e)Kc/(DU DV),
    d2=e(1+zeta)Kc/DV.

For w=uv, with nU,nV,nW denoting actual n-values,

    L=6V=1+d1+d2+j(1-w),
    E=24Bell=1+b+c+d+d1(b+d)+d2(b+c+d)+bj(1-w),

    M=24N=n(C)+n(D)+d1(n(D)+nU+nV)
       +d2(n(C)+n(D)+nV)
       +j[nU+nV+nW-w(3nW+u(nU-nW)+v(nV-nW))],
    T=M/(LE).                                          (13)

The complete vector first moment is

    24J=B+C+D+d1(B+D+U+Vroot)+d2(B+C+D+Vroot)
       +j[B+U+Vroot+W
          -w(B+3W+u(U-W)+v(Vroot-W))].                  (14)

Root xy area is beta*j*(1-w)/2. These formulas include all changes in the mixed C-D pyramid.

### Exact fixed-container supremum, not a global six-parameter bound

Let Lb,Eb,Mb be the first two-pyramid parts of (13), set a=nW, p=nU-nW, q=nV-nW and

    A=Lb+j, B0=Eb+bj, C0=Mb+j(3a+p+q),
    D0=A B0, D1=j(B0+bA), D2=bj^2.

For each fixed w=uv, the only optimization is the genuine constrained minimum g(w)=min(pu+qv). If p,q>0, write m=min(p,q), M0=max(p,q). Then

    g(w)=2 sqrt(pq w), 0<=w<=m/M0,
    g(w)=m+M0 w,      m/M0<=w<=1.

If p,q are not both positive, the second formula holds throughout [0,1]. Thus the ENTIRE root-shape supremum for the fixed six containing parameters is

    max_[0<=w<=1] [C0-3ja w-jw g(w)]/[D0-D1w+D2w^2].   (15)

Every w<1 is realized by an actual triangular or quadrilateral root. The w=1 endpoint is only a zero-area-root limit, so (15) is an equality of suprema, not an assertion of a genuine facet at that endpoint.

For explicit algebraic reconstruction, on the square-root branch put r=sqrt(w), P0=3ja, Q0=2j sqrt(pq). Its interior stationary roots are those of

    2(C0D1-P0D0)-3Q0D0 r-4C0D2 r^2
      +Q0D1 r^3+2P0D2 r^4+Q0D2 r^5.

On the other branch put P0=j(3a+m), Q0=jM0. Its stationary polynomial is

    C0D1-P0D0-2(Q0D0+C0D2)w+(P0D2+Q0D1)w^2.

Evaluate the branch endpoints and the real roots in their stated intervals. This is a complete finite shape prescription. The maximum over the six containing parameters is not determined here.

## 7. Continuous failure of the parent's endpoint comparison

Fix

    beta=3, s=t=2, e=1/20000, f=1/10000,
    u=v=99/100,
    every finite zeta>=100000000.

The endpoints are genuinely unequal:

    b=1/4, c=1/20001, d=1/10001.

Let a_z=7zeta+10004, b_z=7zeta+20004. The exact root-container points are

    U=(10001(zeta+5001)/(5000a_z),
       20001(zeta+1)/(10000a_z), 4zeta/a_z),
    Vroot=(10001(zeta+1)/(5000b_z),
       20001(zeta+10001)/(10000b_z), 4zeta/b_z),
    W=(10001/35000,20001/70000,4/7).

The four actual root vertices, labels 4..7, are

    U, Vroot, W/100+99 Vroot/100, W/100+99 U/100.

For every finite parameter in the interval this is proper 8/14/8, with maximal facet vertex sets

    012, 013, 023, 1256, 1347, 2345, 167, 4567.

The root is a genuine positive-area quadrilateral and has no point in z=0. W is not an actual vertex of these bodies.

Set e=f=0 while keeping beta,s,t,zeta,u,v fixed and RE-HULL. The comparison body is independent of zeta and has the two additional vertices

    (1/350,139/140,1/175),
    (139/140,1/350,1/175)

besides A,B,C,D. It is proper 6/11/7, with c=d=0 and

    V_zero=70199/420000,
    Bell_zero=350199/6720000,
    J_zero=(49208503/1176000000,
            49208503/1176000000,4095041/98000000),
    N_zero=49208503/470400000,
    T_zero=49208503000/24583619601.

Exactly,

    2<T_zero<201/100,
    201*24583619601-100*49208503000=20457239801>0.

### Whole-interval certificate for the larger original trace

Let Kc=10003/10000 and j0=Kc/7. For the full containing detached triangle,

    6V_full-(1+j0)
      =(4Kc/7)[e+f+ef(R0+1)]/[(1+fR0)(1+eR0)]
      <=(4Kc/7)[1/(7zeta)+30001/(49zeta^2)]<1/10000000.

The final root truncation only decreases V and Bell. Since the added tetrahedral mean ell-values are at most b+c+d,

    24Bell <=1+b+c+d+(b+c+d)[j0+1/10000000].

Also d2=j0 lambda, where

    lambda=(zeta+1)/(zeta+20004/7)>=9999/10000.

The actual Vroot has n(Vroot)>=lambda n(W), n(W)>=5/7, and n(C)+n(D)>=5/2. Dropping only positive numerator contributions in (13) gives

    N >=[5/2+(lambda/7)(5/2+5lambda/7)]/24
       >=14499725005/117600000000>12329/100000.

The preceding original-volume bounds give, throughout the whole interval,

    V<19049/100000, Bell<5359/100000.

The final strict arithmetic margin is

    12329/100000
      -(201/100)*6*(19049/100000)*(5359/100000)
      =177189254/1000000000000>0.

Consequently T(P_zeta)>201/100 for EVERY finite zeta>=100000000. This disproves

    T(P)<=max(2,T(P with e=f=0))

in the complete detached class, with an open strict failure around each finite control. It is not a finite parameter sample.

The surviving mixed C-D tetrahedron explains the failure. At fixed positive e,f and zeta tending to infinity, all four root points converge to W; the actual body tends to conv(T0,W), whose supporting root has area zero. The mixed-pyramid coefficient d2 tends to j0>0. Setting e=f=0 first instead keeps a root near CD and excludes W. These are different limits, not a violation of continuity of actual moments.

The counterfamily is NOT a possible 51/25 violation. In (12), kappa_zeta>0 throughout this interval. Hence x+y<=1 on the entire actual body, and the accepted all-shape prism theorem gives T<203/100. The new failure concerns a specific endpoint reduction, not that prism theorem or the unrestricted target.

### A retained genuine three-pyramid root reduction

A second detached control uses

    (beta,s,t,e,f,zeta)=(3,1/10,1/5,1/9,1/4,1),
    U=(105/152,10/171,10/19),
    Vroot=(5/252,470/567,20/63),
    W=(5/132,20/297,40/33).

Its root barycentric polygon is

    [(1,0),(0,1),(0,4/5),(1/5,1/2),(1/2,1/5),(4/5,0)].

Slide (1/5,1/2) in direction (-1/2,3/5) for 0<=t<=2/5, and re-hull at the first wall. Then slide (1/2,1/5) in direction (-4/5,37/50) for 0<=t<=5/8. The terminal root polygons are

    [(1,0),(0,1),(0,37/50),(1/2,1/5),(4/5,0)],
    [(1,0),(0,1),(0,53/80),(4/5,0)].

The actual hulls are 10/18/10, 9/16/9 and 8/14/8, respectively, NOT E17. Along both complete intervals,

    V=8320735/34128864,
    Bell=40028983/546061824,
    Area_xy(F)=442975/3792096.

Let h1,h2 be the physical lifts of the two displayed root-coordinate directions, and j=235625/1422036. The exact vector first-moment gains are j h1/2000 and 31j h2/19200. Their n-values are

    n(h1)=20007/93632>0,
    n(h2)=988741/9480240>0.

Thus N and T strictly increase while the entire original ell-marginal stays fixed. The independent source retains every body, its own J and centroid, and every actual maximal facet. No mechanical preservation along either interval is inferred.

## 8. Precise complement, verification status and continuation

The new positive theorem covers disjoint canonical corner contributions satisfying (6), with (7) a concrete whole sector. It does not prove that those quantitative conditions hold for every E17 realization. Outside them, even the same marked fan pattern remains a genuine continuous problem. The detached-root comparison shows why a new CD-controlled contribution cannot simply be absorbed into the parent's e=f=0 operation.

Root corners with coincident support lines, zero individual deficits and maximal-facet mergers are included by the actual sets and integrals. A protected central polygon has positive area, so no root disappears in the positive theorem. Finite full-dimensional limits retaining T0 inherit a ceiling below 51/25; a zero-area limit is not called a root facet. No formula is evaluated by dividing by 1-b at b=1. Positive-ell auxiliary vertices, negative-z roots, c or d at least one, and all-body attainment retain their separate hypotheses.

The E17 classification supplies ten explicit marked fan patterns and a new geometric test on each. There is no literal global-registry mapping in this pack, so no catalogue subtraction is justified. The lower and upper minimum endpoints remain distinct and unchanged: 34<=Cmin<=622.

The decisive next step is to control the actual corner-pyramid mean n when (6) fails, or the extra CD contribution in (13), while retaining the same body's ell-distribution and convexity. The new marginal formula specifies which geometric areas must be held fixed; it does not license independent optimization of their moments.

### Execution status

The current journal and parent reading were completed. Container-backed audit commands were submitted during the resumed work, but readable terminal results were unavailable. Accordingly, no observed new pass, cold replay, report digest or source-byte pin is asserted. The analytic constructions, full interval inequalities and complete recovery below do not rely on an unseen terminal receipt. The audit is an additional exact check, not a substitute for the proofs above.

Save the complete source below as multi_apex_root_v1.py and run

    python -S multi_apex_root_v1.py build multi_apex_root_v1.json
    python -S multi_apex_root_v1.py verify multi_apex_root_v1.json

It uses only the Python standard library with exact Fraction arithmetic and assertions enabled; CPython 3.13.5 is a suitable pinned interpreter. There are no random seeds, numerical tolerances, optimization packages, parent imports or external data. It prints source/report byte counts and SHA-256 values together with the expected markers MULTI_APEX_ROOT_SOURCE and MULTI_APEX_ROOT_EXACT_PASS. New pins are deliberately not asserted without readable execution evidence.

The complete unit reconstructs true maximal facets, true edges, supporting-plane intersections, two positive volume fans, original V,X,Y,Z,Bell,N, own-centroid primitive packets, correctly weighted balanced images, all ten E17 controls, large root replacements, detached slides, and the exact negative interval bounds. Weak edge packets are recorded as packets, not silently equated with a deduplicated physical-point census.

## Complete standalone source

```python
# MULTI_APEX_CORNER_ROOT_203_AND_DETACHED_OBSTRUCTION_V1
# Parent minimum-0149
# SHA256 4ebbd83f4ad331b2b2a819368f40f83df9cdc61ac0128806f11bffedbca9f66b
# Standard library only. Assertions must remain enabled.
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib, json, sys
assert __debug__

CAN=[tuple(map(F,p)) for p in ((0,0,0),(0,0,1),(0,1,0),(1,0,0))]
A,B,C,D=CAN
SIGMA=F(203,100)

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(c,a): return tuple(c*x for x in a)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def lc(items): return tuple(sum((c*p[j] for c,p in items),F(0)) for j in range(3))
def avg(P,weights=None):
    weights=[F(1)]*len(P) if weights is None else weights
    return tuple(sum(w*p[j] for w,p in zip(weights,P))/sum(weights) for j in range(len(P[0])))
def orient(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def solve3(rows,rhs):
    cols=list(zip(*rows)); z=det(*cols); assert z
    return (det(rhs,cols[1],cols[2])/z,det(cols[0],rhs,cols[2])/z,det(cols[0],cols[1],rhs)/z)

def h2(P):
    unique={}
    for i,p in enumerate(P): unique.setdefault(tuple(p),i)
    order=sorted(unique.values(),key=lambda i:(P[i][0],P[i][1],i))
    if len(order)<=1: return order
    def half(ids):
        out=[]
        for i in ids:
            while len(out)>1 and orient(P[out[-2]],P[out[-1]],P[i])<=0: out.pop()
            out.append(i)
        return out
    return half(order)[:-1]+half(order[::-1])[:-1]

def poly(P):
    # Ordered polygon, not its convex hull: missing corners may be nonconvex.
    if len(P)<3: return F(0),(F(0),F(0))
    ar=F(0); jx=F(0); jy=F(0)
    for p,q in zip(P,P[1:]+P[:1]):
        z=p[0]*q[1]-p[1]*q[0]
        ar+=z/2; jx+=z*(p[0]+q[0])/6; jy+=z*(p[1]+q[1])/6
    if ar<0: ar=-ar; jx=-jx; jy=-jy
    return ar,(jx,jy)

def convex_points(P):
    P=[tuple(map(F,p)) for p in P]
    return [P[i] for i in h2(P)]

def hull(P):
    found={}
    for i,j,k in combinations(range(len(P)),3):
        n=cross(sub(P[j],P[i]),sub(P[k],P[i]))
        if not any(n): continue
        d=dot(n,P[i]); sl=[dot(n,p)-d for p in P]
        if min(sl)<0<max(sl): continue
        if max(sl)>0: n=mul(-1,n); d=-d; sl=[-x for x in sl]
        on=[i for i,z in enumerate(sl) if z==0]
        drop=max(range(3),key=lambda j:abs(n[j])); axes=[j for j in range(3) if j!=drop]
        pp=[tuple(P[i][j] for j in axes) for i in on]
        cy=[on[j] for j in h2(pp)]
        if len(cy)<3: continue
        if dot(cross(sub(P[cy[1]],P[cy[0]]),sub(P[cy[2]],P[cy[0]])),n)<0: cy.reverse()
        start=cy.index(min(cy)); cy=tuple(cy[start:]+cy[:start])
        found.setdefault(tuple(sorted(cy)),(cy,n,d))
    faces=[found[k] for k in sorted(found)]; edges={}
    vertices=sorted({i for cy,n,d in faces for i in cy})
    for fi,(cy,n,d) in enumerate(faces):
        assert all(dot(n,p)<=d for p in P)
        for i,j in zip(cy,cy[1:]+cy[:1]): edges.setdefault(tuple(sorted((i,j))),[]).append(fi)
    assert all(len(fs)==2 for fs in edges.values())
    assert len(vertices)-len(edges)+len(faces)==2
    recovered=set()
    for ids in combinations(range(len(faces)),3):
        rows=[faces[i][1] for i in ids]
        if not det(*rows): continue
        p=solve3(rows,[faces[i][2] for i in ids])
        if all(dot(n,p)<=d for cy,n,d in faces): recovered.add(p)
    assert recovered=={P[i] for i in vertices}
    moments=[]; fans=[]
    for ref in (avg(P),avg(P,[F(i+1) for i in range(len(P))])):
        assert all(dot(n,ref)<d for cy,n,d in faces)
        vol=F(0); J=[F(0)]*3; cells=[]
        for cy,n,d in faces:
            for j in range(1,len(cy)-1):
                ids=(cy[0],cy[j],cy[j+1]); p,q,r=[P[i] for i in ids]
                v=det(sub(p,ref),sub(q,ref),sub(r,ref))/6; assert v>0
                vol+=v
                for k in range(3): J[k]+=v*(ref[k]+p[k]+q[k]+r[k])/4
                cells.append((ids,v))
        moments.append((vol,tuple(J))); fans.append((ref,cells))
    assert moments[0]==moments[1]
    vol,J=moments[0]
    return dict(points=P,vertices=vertices,faces=faces,edges=sorted(edges),
                edge_faces=[edges[e] for e in sorted(edges)],fans=fans,V=vol,J=J,
                g=tuple(x/vol for x in J),f_vector=(len(vertices),len(edges),len(faces)))

def mechanics(G):
    P=G['points']; g=G['g']; centered=[sub(p,g) for p in P]
    poles=[mul(1/(d-dot(n,g)),n) for cy,n,d in G['faces']]
    U={i:True for i in G['vertices']}; S=[True]*len(poles)
    packets=[]; H=[]; weak=[]
    for edge,fs in zip(G['edges'],G['edge_faces']):
        i,j=edge; f,h=fs
        row=(dot(centered[i],sub(centered[j],centered[i])),
             dot(centered[j],sub(centered[i],centered[j])),
             dot(poles[f],sub(poles[h],poles[f])),dot(poles[h],sub(poles[f],poles[h])))
        U[i]&=row[0]<0; U[j]&=row[1]<0; S[f]&=row[2]<0; S[h]&=row[3]<0
        if max(row)<0: H.append(edge)
        if max(row)<=0 and 0 in row: weak.append(edge)
        packets.append((edge,tuple(fs),row))
    return dict(M='identity',poles=poles,strict_U=[i for i in U if U[i]],
                strict_S=[i for i,x in enumerate(S) if x],strict_H=H,
                weak_edge_packets=weak,packets=packets)

def weighted_check(G,b,c,d):
    P=G['points']; S0=1+b+c+d; jac=b*S0*S0
    ell=lambda p:1+(d-1)*p[0]+(c-1)*p[1]+(b-1)*p[2]
    nn=lambda p:(1+b+c)*p[0]+(1+b+d)*p[1]
    den=[ell(p)+nn(p) for p in P]; assert min(den)>0
    image=[(S0*p[0]/f,S0*p[1]/f,b*p[2]/f) for p,f in zip(P,den)]
    I=hull(image); assert I['f_vector']==G['f_vector']
    L=lambda p:1-(1-1/S0)*(p[0]+p[1])+(1/b-1)*p[2]
    ep=lambda p:1-(1-d/S0)*p[0]-(1-c/S0)*p[1]
    rows=[]
    for ref,cells in I['fans']:
        row=[F(0)]*3
        for ids,vol in cells:
            tet=[ref]+[image[i] for i in ids]; ls=[L(p) for p in tet]
            assert min(ls)>0
            product=F(1)
            for z in ls: product*=z
            w=vol/product; row[0]+=w
            row[1]+=w*sum(ep(p)/z for p,z in zip(tet,ls))/4
            row[2]+=w*sum((1-ep(p))/z for p,z in zip(tet,ls))/4
        rows.append(tuple(row))
    assert rows[0]==rows[1]==(jac*G['V'],jac*G['Bell'],jac*G['N'])
    assert jac*rows[0][2]/(6*rows[0][0]*rows[0][1])==G['T']
    return dict(Jp=jac,weighted=rows[0],image_points=image,image_faces=I['faces'],image_volume=I['V'])

def physical(raw,b,c,d,require_root=True):
    P=list(dict.fromkeys(tuple(map(F,p)) for p in raw)); G=hull(P)
    assert set(range(4))<=set(G['vertices'])
    assert all(min(p)>=0 for p in P)
    ell=lambda p:1+(d-1)*p[0]+(c-1)*p[1]+(b-1)*p[2]
    assert min(map(ell,P))>=0
    J=G['J']; vol=G['V']; E=vol+(d-1)*J[0]+(c-1)*J[1]+(b-1)*J[2]
    N=(1+b+c)*J[0]+(1+b+d)*J[1]
    assert vol>0 and E>0 and N>0
    root=[i for i in G['vertices'] if ell(P[i])==0]
    R=[P[i][:2] for i in root]; R=[R[i] for i in h2(R)] if R else []
    ar,jr=poly(R)
    if require_root:
        assert ar>0
        assert tuple(sorted(root)) in {tuple(sorted(cy)) for cy,n,d0 in G['faces']}
    assert {i for i in G['vertices'] if P[i][0]==0}=={0,1,2}
    assert {i for i in G['vertices'] if P[i][1]==0}=={0,1,3}
    G.update(endpoints=(F(1),b,c,d),Bell=E,N=N,T=N/(6*vol*E),root=root,root_xy_area=ar,
             root_area_squared=ar*ar*(1+((1-d)/(1-b))**2+((1-c)/(1-b))**2),proper33=True)
    G['mechanics']=mechanics(G); G['weighted_image']=weighted_check(G,b,c,d)
    return G

def context(par):
    beta,s,t,e,f,zeta=map(F,par); assert beta>0 and s>0 and t>0 and e>=0 and f>=0 and zeta>=0
    b=1/(1+beta); c=e/(1+e); d=f/(1+f); Z=beta+s+t; kc=1+s*f+t*e
    R=s+t+zeta*Z; du=1+f*R; dv=1+e*R
    U=((1+f)*(1+f*s*(1+zeta))/du,t*(1+e)*f*(1+zeta)/du,(1+beta)*zeta*f/du)
    V=(s*(1+f)*e*(1+zeta)/dv,(1+e)*(1+e*t*(1+zeta))/dv,(1+beta)*zeta*e/dv)
    W=(s*(1+f)/Z,t*(1+e)/Z,(1+beta)/Z)
    j=(1+e)*(1+f)*kc/(Z*du*dv)
    d1=f*(1+zeta)*(1+e)*kc/(du*dv); d2=e*(1+zeta)*kc/dv
    assert j==det(sub(U,B),sub(V,B),sub(W,B))>0
    assert d1==abs(det(sub(D,B),sub(U,B),sub(V,B)))
    assert d2==abs(det(sub(D,B),sub(V,B),sub(C,B)))
    for p in (U,V,W): assert 1+(d-1)*p[0]+(c-1)*p[1]+(b-1)*p[2]==0
    return dict(par=tuple(map(F,par)),b=b,c=c,d=d,U=U,V=V,W=W,j=j,d1=d1,d2=d2)

def lifted(ctx,p):
    return lc([(1,ctx['W']),(p[0],sub(ctx['U'],ctx['W'])),(p[1],sub(ctx['V'],ctx['W']))])

def make(par,K):
    ctx=context(par); K=convex_points(K)
    start=K.index((F(1),F(0))); K=K[start:]+K[:start]
    assert (F(0),F(1)) in K and all(min(p)>=0 and sum(p)<=1 for p in K)
    ar,jk=poly(K); assert ar>0
    U,V,W=(ctx[x] for x in ('U','V','W')); b,c,d=(ctx[x] for x in ('b','c','d'))
    j,d1,d2=(ctx[x] for x in ('j','d1','d2'))
    G=physical(CAN+[lifted(ctx,p) for p in K],b,c,d)
    L=1+d1+d2+2*j*ar
    E=1+b+c+d+d1*(b+d)+d2*(b+c+d)+2*b*j*ar
    ir=lc([(ar,W),(jk[0],sub(U,W)),(jk[1],sub(V,W))])
    J24=lc([(1,add(add(B,C),D)),(d1,add(add(add(B,D),U),V)),
            (d2,add(add(add(B,C),D),V)),(2*j*ar,B),(6*j,ir)])
    assert G['V']==L/6 and G['Bell']==E/24 and G['J']==mul(F(1,24),J24)
    assert G['root_xy_area']==ctx['par'][0]*j*ar
    G.update(container=ctx,K=K,scaled_integrals=(L,E,24*G['N']))
    return G

def cap(ctx,anchor,polygon):
    if len(polygon)<3:
        return dict(area=F(0),V=F(0),Bell=F(0),J=(F(0),)*3,N=F(0),polygon=polygon)
    ar,j=poly([p[:2] for p in polygon]); assert ar>0
    b,c,d=ctx['b'],ctx['c'],ctx['d']; alpha=1-b
    mean=(j[0]/ar,j[1]/ar,(1+(d-1)*j[0]/ar+(c-1)*j[1]/ar)/alpha)
    h=1+(d-1)*anchor[0]+(c-1)*anchor[1]+(b-1)*anchor[2]
    v=h*ar/(3*alpha); J=mul(v/4,add(anchor,mul(3,mean)))
    return dict(area=ar,V=v,Bell=h*v/4,J=J,N=(1+b+c)*J[0]+(1+b+d)*J[1],polygon=polygon)

PROTO=(F(3),F(1,2),F(9,8),F(1,9),F(1,4),F(0))

def corner_record(full,chains,ordered=None):
    ctx=full['container']; corners=[ctx[x] for x in ('U','V','W')]; anchors=[D,C,B]
    raw=[]; caps=[]
    for p,a,chain in zip(corners,anchors,chains):
        raw.extend(chain if chain else [p]); caps.append(cap(ctx,a,[p]+chain if chain else []))
    root=convex_points(raw) if ordered is None else ordered
    G=physical(CAN+root,ctx['b'],ctx['c'],ctx['d'])
    assert G['V']==full['V']-sum(q['V'] for q in caps)
    assert G['Bell']==full['Bell']-sum(q['Bell'] for q in caps)
    assert G['J']==sub(full['J'],lc([(1,q['J']) for q in caps]))
    assert G['root_xy_area']==full['root_xy_area']-sum(q['area'] for q in caps)
    medial=[mul(F(1,2),add(corners[i],corners[(i+1)%3])) for i in range(3)]
    cy=convex_points([p[:2] for p in root])
    assert all(orient(p,q,m[:2])>=0 for p,q in zip(cy,cy[1:]+cy[:1]) for m in medial)
    qr=[corners[0],corners[1]]+(chains[2] if chains[2] else [corners[2]])
    Q=physical(CAN+convex_points(qr),ctx['b'],ctx['c'],ctx['d'])
    removed=caps[0]['V']+caps[1]['V']
    assert G['T']<=Q['T']<SIGMA
    if removed>0: assert G['T']<Q['T']
    assert Q['V']-G['V']==removed
    assert Q['Bell']-G['Bell']==caps[0]['Bell']+caps[1]['Bell']
    G.update(corner_caps=caps,filled_comparison=Q)
    return G

def inverse_root(p):
    x,y=p; z=2-x-y; L=6+x+6*y
    return (5*x/L,10*y/L,4*z/L)

def expected_pattern(i,j,k):
    fs=[(0,1,2),(0,1,3),(0,2,3,4,9),tuple(range(4,10))]; r=4
    for unused in range(i): fs.append((3,r,r+1)); r+=1
    fs.append((1,3,r,r+1)); r+=1
    for unused in range(j): fs.append((1,r,r+1)); r+=1
    fs.append((1,2,r,r+1)); r+=1
    for unused in range(k): fs.append((2,r,r+1)); r+=1
    assert r==9
    return {tuple(sorted(f)) for f in fs}

def corner_controls():
    full=make(PROTO,[(1,0),(0,1),(0,0)])
    assert full['f_vector']==(7,11,6)
    assert (full['V'],full['Bell'],full['root_xy_area'])==(F(8791,33966),F(199873,2717280),F(640,1887))
    ctx=full['container']; corners=[ctx[x] for x in ('U','V','W')]
    nn=lambda p:(1+ctx['b']+ctx['c'])*p[0]+(1+ctx['b']+ctx['d'])*p[1]
    half=[]
    for i,p in enumerate(corners):
        half.append([mul(F(1,2),add(p,corners[(i-1)%3])),mul(F(1,2),add(p,corners[(i+1)%3]))])
    guard=min(nn(p) for i,a in ((0,D),(1,C)) for p in [a,corners[i]]+half[i])
    assert guard==F(13769,12580)>F(109,100)
    assert max(ctx['c'],ctx['d'])<F(21,100) and full['V']<F(27,100) and full['Bell']<F(3,40)
    gap=F(109,100)-6*SIGMA*(F(3,40)+F(21,100)*F(27,100)/4)
    assert gap==F(7697,2000000)>0
    large=corner_record(full,[half[0],half[1],[]]); medial=corner_record(full,half)
    assert (large['f_vector'],large['V'],large['Bell'])==((8,14,8),F(8407,33966),F(198593,2717280))
    assert (medial['f_vector'],medial['V'],medial['Bell'])==((7,14,9),F(8087,33966),F(196993,2717280))
    image=[(F(9,5),F(1,5)),(F(1,5),F(9,5)),(F(1,5),F(1,5))]
    assert [inverse_root(p) for p in image]==corners
    records=[]; reps=set()
    for i in range(4):
        for j in range(4-i):
            k=3-i-j; lengths=(i,k,j); chains=[]; raw=[]
            for h,l in enumerate(lengths):
                p=image[h]
                if not l: chains.append([]); raw.append(corners[h]); continue
                chain=[]
                for r in range(l+1):
                    t=F(r,l)
                    point=add(p,add(mul((1-t)**2/8,sub(image[(h-1)%3],p)),mul(t*t/8,sub(image[(h+1)%3],p))))
                    chain.append(inverse_root(point))
                chains.append(chain); raw.extend(chain)
            cy=convex_points(raw); zids=[h for h,p in enumerate(cy) if p[2]==0]; assert len(zids)==2
            start=max(zids,key=lambda h:cy[h][0]); cy=cy[start:]+cy[:start]
            if cy[1][2]==0: cy=[cy[0]]+list(reversed(cy[1:]))
            G=corner_record(full,chains,cy)
            assert G['f_vector']==(10,17,9)
            assert {tuple(sorted(f)) for f,n,d0 in G['faces']}==expected_pattern(i,j,k)
            degree={r:0 for r in G['vertices']}
            for r,s0 in G['edges']: degree[r]+=1; degree[s0]+=1
            assert [degree[r] for r in range(4)]==[3,j+4,k+3,i+3]
            assert all(degree[r]==3 for r in range(4,10))
            if (i,j,k)==(1,1,1):
                literal=[(F(4,5),F(2,5),F(0)),(F(10,11),F(5,22),F(1,11)),
                         (F(5,19),F(5,19),F(14,19)),(F(5,43),F(20,43),F(28,43)),
                         (F(5,79),F(80,79),F(4,79)),(F(1,8),F(1),F(0))]
                assert cy==literal
                assert [q['area'] for q in G['corner_caps']]==[F(1,132),F(15,10744),F(375,30229)]
                assert G['V']>F(32,125) and G['Bell']>F(73,1000) and G['N']<F(27,125) and G['T']<2
            records.append(dict(pattern=(i,j,k),body=G)); reps.add(min((i,j,k),(k,j,i)))
    assert len(records)==10 and len(reps)==6
    return dict(container=full,corner_floor=guard,strict_margin=gap,large=large,medial=medial,
                reflection_representatives=sorted(reps),ten_patterns=records)

def slide_guard(K,index,direction,end):
    K=[tuple(map(F,p)) for p in K]; direction=tuple(map(F,direction)); end=F(end)
    stop=list(K); stop[index]=add(K[index],mul(end,direction))
    for P in (K,stop):
        assert all(min(p)>=0 and sum(p)<=1 for p in P)
        assert all(orient(p,q,r)>=0 for p,q in zip(P,P[1:]+P[:1]) for r in P)
    assert poly(K)[0]==poly(stop)[0]
    # Each support determinant is affine in this single moving point.
    return stop

def detached_slides():
    par=(3,F(1,10),F(1,5),F(1,9),F(1,4),1)
    K0=[(1,0),(0,1),(0,F(4,5)),(F(1,5),F(1,2)),(F(1,2),F(1,5)),(F(4,5),0)]
    K1=[(1,0),(0,1),(0,F(37,50)),(F(1,2),F(1,5)),(F(4,5),0)]
    K2=[(1,0),(0,1),(0,F(53,80)),(F(4,5),0)]
    stop1=slide_guard(K0,3,(F(-1,2),F(3,5)),F(2,5))
    stop2=slide_guard(K1,3,(F(-4,5),F(37,50)),F(5,8))
    assert set(convex_points(stop1))==set(tuple(map(F,p)) for p in K1)
    assert set(convex_points(stop2))==set(tuple(map(F,p)) for p in K2)
    bodies=[make(par,K) for K in (K0,K1,K2)]
    assert [G['f_vector'] for G in bodies]==[(10,18,10),(9,16,9),(8,14,8)]
    for G in bodies:
        assert (G['V'],G['Bell'],G['root_xy_area'])==(F(8320735,34128864),F(40028983,546061824),F(442975,3792096))
    ctx=bodies[0]['container']; h1=add(mul(F(-1,2),sub(ctx['U'],ctx['W'])),mul(F(3,5),sub(ctx['V'],ctx['W'])))
    h2v=add(mul(F(-4,5),sub(ctx['U'],ctx['W'])),mul(F(37,50),sub(ctx['V'],ctx['W'])))
    nn=lambda p:(1+ctx['b']+ctx['c'])*p[0]+(1+ctx['b']+ctx['d'])*p[1]
    assert nn(h1)==F(20007,93632)>0 and nn(h2v)==F(988741,9480240)>0
    assert sub(bodies[1]['J'],bodies[0]['J'])==mul(ctx['j']/2000,h1)
    assert sub(bodies[2]['J'],bodies[1]['J'])==mul(31*ctx['j']/19200,h2v)
    mid=[]
    for K,h,end in ((K0,(F(-1,2),F(3,5)),F(2,5)),(K1,(F(-4,5),F(37,50)),F(5,8))):
        P=[tuple(map(F,p)) for p in K]; P[3]=add(P[3],mul(end/2,h)); mid.append(make(par,P))
    for i,G in enumerate(mid):
        assert G['J']==mul(F(1,2),add(bodies[i]['J'],bodies[i+1]['J']))
        assert G['V']==bodies[i]['V'] and G['Bell']==bodies[i]['Bell']
    return dict(endpoints=bodies,midpoint_checks=mid,directions=(h1,h2v),intervals=((F(0),F(2,5)),(F(0),F(5,8))))

def detached_counter():
    lo=F(10**8); kc=F(10003,10000); small=F(1,10**7); delta=F(1,10000)
    excess=4*kc/7*(1/(7*lo)+F(30001,49)/(lo*lo)); assert excess<small
    lam=(lo+1)/(lo+F(20004,7)); assert lam>=F(9999,10000)
    jmax=F(2501,17500)
    vu=(1+jmax)/6+small/6; eu=(F(5,4)+2*delta+jmax*(F(1,4)+2*delta))/24+small
    nl=(F(5,2)+(F(9999,10000)/7)*(F(5,2)+5*F(9999,10000)/7))/24
    assert vu<F(19049,100000) and eu<F(5359,100000)
    assert nl==F(14499725005,117600000000)>F(12329,100000)
    gap=F(12329,100000)-F(201,100)*6*F(19049,100000)*F(5359,100000)
    assert gap==F(177189254,10**12)>0
    assert 1-(1+1/lo)*kc/4>0
    K=[(1,0),(0,1),(0,F(99,100)),(F(99,100),0)]
    records=[]
    facets={(0,1,2),(0,1,3),(0,2,3),(1,2,5,6),(1,3,4,7),(2,3,4,5),(1,6,7),(4,5,6,7)}
    for zeta in (10**8,2*10**8,10**9):
        G=make((3,2,2,F(1,20000),F(1,10000),zeta),K)
        assert G['f_vector']==(8,14,8)
        assert {tuple(sorted(f)) for f,n,d0 in G['faces']}==facets
        assert F(201,100)<G['T']<SIGMA and G['V']<F(19049,100000) and G['Bell']<F(5359,100000) and G['N']>F(12329,100000)
        kap=1-(1+F(zeta))*kc/(4*F(zeta))
        assert kap>0 and all(p[0]+p[1]+kap*p[2]<=1 for p in G['points'])
        records.append(G)
    zero=make((3,2,2,0,0,10**8),K)
    assert zero['f_vector']==(6,11,7)
    assert (zero['V'],zero['Bell'],zero['N'],zero['T'])==(F(70199,420000),F(350199,6720000),F(49208503,470400000),F(49208503000,24583619601))
    assert zero['J']==(F(49208503,1176000000),F(49208503,1176000000),F(4095041,98000000))
    assert 2<zero['T']<F(201,100)
    assert 201*24583619601-100*49208503000==20457239801
    ctx=records[0]['container']; limit=physical(CAN+[ctx['W']],ctx['b'],ctx['c'],ctx['d'],False)
    assert limit['f_vector']==(5,9,6) and limit['root_xy_area']==0
    j0=kc/7
    assert limit['V']==(1+j0)/6
    assert limit['Bell']==(1+ctx['b']+ctx['c']+ctx['d']+j0*(ctx['b']+ctx['c']+ctx['d']))/24
    return dict(lower_parameter=lo,excess_bound=excess,lambda_lower=lam,volume_upper=vu,
                ell_upper=eu,numerator_lower=nl,strict_integer_gap=gap,
                finite_controls=records,zero_endpoint_comparison=zero,zero_area_limit=limit)

def clean(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {str(k):clean(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [clean(v) for v in x]
    return x

def report():
    return dict(tag='MULTI_APEX_CORNER_ROOT_203_AND_DETACHED_OBSTRUCTION_V1',
                parent='minimum-0149',
                parent_sha256='4ebbd83f4ad331b2b2a819368f40f83df9cdc61ac0128806f11bffedbca9f66b',
                corner_sector=corner_controls(),detached_slides=detached_slides(),
                detached_counter=detached_counter())

if __name__=='__main__':
    assert len(sys.argv)==3 and sys.argv[1] in ('build','verify')
    raw=(json.dumps(clean(report()),sort_keys=True,separators=(',',':'))+'\n').encode()
    p=Path(sys.argv[2])
    if sys.argv[1]=='build': p.write_bytes(raw)
    else: assert p.read_bytes()==raw
    source=Path(__file__).read_bytes()
    print('MULTI_APEX_ROOT_SOURCE',len(source),hashlib.sha256(source).hexdigest())
    print('MULTI_APEX_ROOT_EXACT_PASS',len(raw),hashlib.sha256(raw).hexdigest())
```
