# minimum-0164

Historical AI scientific report · saved 2026-09-21 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# POSITIVE_OCTANT_ROOT_ONLY_TRACE_203_AND_CORNER_DOMINANCE_V1

## 1. Determination

**The entire positive-octant root-only class with strictly positive endpoint values below the common endpoint is now excluded below the target:**

    T(P) < 203/100 < 51/25.

Precisely, let

    A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
    T0=conv(A,B,C,D),
    0<b,c,d<1,
    ell=1+(d-1)x+(c-1)y+(b-1)z,
    n=(1+b+c)x+(1+b+d)y.

Let F be any compact convex positive-area subset of

    {ell=0, x>0, y>0, z>=0},

and let P=conv(T0,F), filled with its original uniform volume density. Then the entire coordinate support faces are the genuine maximal triangles ABC and ABD, the actual root is F, and

    V=integral_P 1,
    J=(X,Y,Zmoment)=integral_P (x,y,z),
    Bell=integral_P ell,
    N=integral_P n,
    T=N/(6 V Bell)<203/100.                            (1)

No restriction on the number of root vertices is imposed. Curved compact convex roots are included.

**Consequently every geometric realization of all ten marked positive-octant proper10/17/9 root-only fan patterns in the parent satisfies (1).** This is a whole-shape value theorem, not another open parameter collar. The ten-pattern classification itself is inherited, not counted as a new result. The parent had closed quantitative subdomains of those patterns, not their complete parameter spaces. :contentReference[oaicite:0]{index=0}

The new geometric mechanism is stronger than a vertex-count reduction. There is an actual proper root-only successor with at most six root vertices and ten total true vertices that preserves the same root plane, all four endpoint values, actual root area, V, Bell, and the **entire original ell-marginal**, while not decreasing N. In fact it does not decrease

    integral_P n psi(ell)

for any bounded nonnegative measurable psi. Full J, the own centroid, face lattice and mechanical equilibrium counts generally change.

An additional complete sector has the stronger bound T<=2; its exact containing-corner condition is given in Section6.

The sharp supremum of this whole class is not determined. The proved interval is

    Cstar <= sup T <=203/100,
    Cstar approximately2.02878303567341172514.

The lower side follows from the proper detached sequence already preserved in the preceding handoff. It is not an assertion of proper attainment.

The unrestricted adjacent-triangle problem remains open outside this class. In particular, negative-z root geometry, an opposite endpoint at least1, and positive-ell auxiliary vertices are not silently absorbed into the theorem. No whole mechanical E17 exclusion, catalogue decrement,110 construction or change to34<=Cmin<=622 follows. Those endpoints remain the accepted lower and upper bounds, respectively. :contentReference[oaicite:1]{index=1}

## 2. Authority and evidence boundary

This continues the same-chat result DETACHED_ROOT_FULL_203_AND_OUTER_CONTAINER_2_V1. Its complete delivered source was inspected through EOF. Its source identity remains

    detached_full_203_v1.py
    18845bytes
    SHA256 00636c48a52dfe38779fb67474f1c164fd13df9eb0d95d7d06226fb421bb259f.

The immutable upstream parent remains

    minimum-0154
    SHA256 dde6883671865bbf789ac1510835c336922a211baaff8a05b9224d6e2574e1f3
    MULTI_APEX_CORNER_ROOT_203_AND_DETACHED_OBSTRUCTION_V1.

The complete2179-line current journal, including that literal parent and its complete source, had already been read consecutively through EOF in this chat. No new external scientific source is used here, and no inaccessible older source is imported into the new computation.

The only inherited value input needed for the full-class conclusion is the accepted **original-body projection-prism theorem**: a proper body containing T0 with actual xy projection Delta={x,y>=0,x+y<=1} has T<203/100. Its authority is minimum-0089, SHA891b41773841961163f155590af8f226a198ce4a68017e870a8a492b3c7c1f52. That theorem is used only on an actual containing-body support sector, never on a uniformly refilled projective image. Its older393-leaf proof is not rerun or imported by this capsule. :contentReference[oaicite:2]{index=2}

Everything new—the corner replacement, its complete parameter coverage, the complementary polynomial certificates, and the actual controls—is reconstructed by the single autonomous capsule below. Normal build, normal verification, fresh-directory build, and a separately completed fresh-directory verification were observed. An initial combined cold command reached its timeout after the build; that uncompleted verification was not counted. The subsequent separate cold verification completed and matched every pin.

## 3. The decisive planar corner lemma

### Statement

Consider a missing corner S in the unit triangle conv((0,0),(1,0),(0,1)). Suppose

    S={(x,y):0<=x<=1,0<=y<=f(x)},

where f is nonnegative, convex and nonincreasing, f(1)=0 and f(0)<=1. This is the geometry of a possibly nonconvex missing corner whose complement is convex. Put

    m=integral_0^1 f(x) dx,
    Xc=integral_0^1 x f(x) dx,
    Yc=(1/2)integral_0^1 f(x)^2 dx.

For every affine cost q0+p x+q y, there is an actual triangular missing corner

    S*=conv((0,0),(a,0),(0,h)),
    0<=a,h<=1, ah=2m,

with the same area and no larger integral of that affine cost.

The replacement triangle stays inside the allowed corner triangle. It is not an independently chosen centroid or a signed mass.

### Three exact moment inequalities

For0<m<=1/2,

    2m^2/3 <= Xc <= m/3,                              (2)
    Xc+Yc <= (m+2m^2)/3,                              (3)
    Xc Yc >= 2m^3/9.                                  (4)

Here is an elementary proof retaining all coupling.

A polygonal convex decreasing f is a nonnegative combination of hinges (1-x/t)+. Add an atom at t=0 to make the coefficients a probability measure mu on[0,1]; that atom contributes zero to all displayed integrals. Thus

    2m=E_mu t,
    6Xc=E_mu t^2.

This proves (2). For0<=t<=u<=1, the exact product integral of two hinges is

    I(t,u)=t/2-t^2/(6u),

with its continuous value0 when u=0. The identity

    (t^2+u^2)/2+3I(t,u)-(t+u)/2-tu
      =-(1-u)(u-t)^2/(2u)<=0                          (5)

gives (3) after averaging over mu×mu. The complete source verifies this identity symbolically.

For (4), extend f by zero to the positive half-line. Set a=3Xc/m and h=2m/a, and put g(x)=h(1-x/a)+. Then integral g=m and integral xg=Xc. Moreover

    integral g f >= h(m-Xc/a)=integral g^2.

Indeed, discarding the part of (1-x/a)f beyond a discards a nonpositive contribution. Hence

    integral f^2-integral g^2
      =integral(f-g)^2+2 integral g(f-g)>=0.

Since integral g^2=4m^3/(9Xc), inequality (4) follows. These arguments extend to arbitrary convex f by polygonal approximation.

### Explicit selection rule

If q>=0, choose

    a=3Xc/m, h=2m/a.

By (2), both intercepts are at most1. This triangle has the same Xc and has Yc*=2m^3/(9Xc)<=Yc, so its cost is no larger, regardless of the sign of p.

If q<0, consider the two triangles with intercept pairs

    (2m,1) and (1,2m).

Their moment pairs are the endpoints of the segment

    X+Y=(m+2m^2)/3,
    2m^2/3<=X<=m/3.

By (2),(3), a convex combination matching the original Xc has Y at least the original Yc. Because q<0, its average affine cost is no larger than the original cost. At least one of the two actual endpoint triangles has no larger cost. Choose that triangle.

The cases m=0 and m=1/2 are harmless: respectively leave the corner unchanged, or use the full unit corner triangle. No singular optimization is needed.

For an allowed triangle with axis intercepts A0,H0, apply the affine scaling x/A0,y/H0. In unscaled coordinates the first selection is

    a=3Xc/m, h=2m/a,

and the two endpoint choices are

    (2m/H0,H0), (A0,2m/A0).

Thus rational polygonal input gives a rational replacement by a deterministic finite comparison. No radical or numerical optimizer is required.

## 4. Why every body in the theorem has three such actual corners

### A projectivity used only for set geometry

Use

    phi=(1-x-y-z)/2+dx+cy+bz,
    (x',y',z')=(dx,cy,bz)/phi.

It fixes A,B,C,D and sends the root plane to x'+y'+z'=2. Its denominator is positive on T0 and on the root, hence on P. On the root, phi=(x+y+z-1)/2>0.

The inverse on the root plane is

    L=-2+x'/d+y'/c+z'/b,
    (x,y,z)=(x'/(dL),y'/(cL),z'/(bL)).

Because0<b,c,d<1, L is positive on the entire nonnegative root-plane triangle x'+y'+z'=2. This is where the endpoint hypotheses matter.

Let F' be the image of F and define its actual coordinate minima

    xi=min_F' x'>0,
    eta=min_F' y'>0,
    h0=min_F' z'>=0.

Positive root area implies xi+eta+h0<2. Its smallest containing triangle with sides parallel to BCD is

    R'={x'>=xi,y'>=eta,z'>=h0,x'+y'+z'=2}.             (6)

The root touches every side of R', possibly at a point rather than an edge.

Between levels x'+y'+z'=1 and2, the actual sections of conv(T0,F') are Minkowski sums of the canonical BCD triangle and F'. Below level1, both this body and conv(T0,R') have the same tetrahedral part. Along each of the three root-corner normal cones, Minkowski addition translates the root boundary chain by the corresponding canonical vertex: D at the U corner, C at Vroot, and B at W.

Consequently, if S_U,S_V,S_W are the three actual missing corner regions R minus F in original coordinates, then

    P_R minus P
      =cone(D,S_U) union cone(C,S_V) union cone(B,S_W), (7)

with disjoint interiors. Here cone(a,S) means the union of segments from a to points of S; when S is nonconvex it does not mean conv(a,S).

For polygons, this follows directly by following the three translated boundary chains. Approximation retaining all root-side contact points proves it for arbitrary compact convex F. Inverting the positive projectivity preserves the segment unions and the disjointness. No uniform-image moment is used.

Each S_i lies inside the triangle formed by its containing corner and the two nearest root-side contact points. In affine coordinates along those two sides, it is exactly an undergraph of a convex decreasing function. The three allowed corner triangles have disjoint interiors: their endpoint fractions on each shared side sum to at most1. This remains true when a side-contact interval shrinks to a point.

### Original marginal and first-moment formulas

Write gell=|grad ell|, let a_i be D,C,B, and let h_i=ell(a_i) be d,c,b. If Ai is the physical area of S_i and rbar_i its actual area centroid, then

    vi=h_i Ai/(3gell),
    Ei=h_i vi/4,
    Ji=(vi/4)(a_i+3rbar_i),
    Ni=(vi/4)(n(a_i)+3 mean_Si n).                    (8)

Its original ell-marginal has density

    Ai/gell * (1-w/h_i)^2, 0<=w<=h_i.                 (9)

These are the parent's genuine separate corner contributions; they are not replaced by total area alone. :contentReference[oaicite:3]{index=3}

Apply the corner lemma separately in original affine root coordinates with cost n. The replacement missing triangles have the same three individual areas Ai and no larger three individual n-area integrals. Their allowed triangles are disjoint, so their complements intersect in one actual convex positive-area root F*. The old side-contact marks remain in F*. In particular the same containing triangle is retained.

By (7)–(9), P*=conv(T0,F*) preserves the original V, Bell, root area and entire ell-marginal. Its N does not decrease. For bounded psi>=0, the n-weighted integral over a missing cone is

    h_i/gell [n(a_i) Ai integral_0^1 lambda^2(1-lambda)psi(h_i(1-lambda)) dLambda
             +(integral_Si n) integral_0^1 lambda^3 psi(h_i(1-lambda)) dLambda].

The same comparison proves integral_P* n psi(ell)>=integral_P n psi(ell).

This is an endpoint dominance construction. A trace-monotone homotopy between the old and new roots is not asserted. It preserves neither the full first moment nor mechanics.

The successor has at most six root vertices and ten body vertices. It has at most ten maximal facets, or at most nine when h0=0. This already reduces all ten parent E17 patterns to three single corner cuts, including zero individual cuts and genuine facet mergers.

## 5. Complete actual parameterization and moments after reduction

Every triangle (6) is represented by

    beta,s,t,e,f>0, zeta>=0,
    b=1/(1+beta), c=e/(1+e), d=f/(1+f),
    Z0=beta+s+t, Kc=1+sf+te,
    R0=s+t+zeta Z0,
    DU=1+fR0, DV=1+eR0,

    U=((1+f)(1+fs(1+zeta))/DU,
       t(1+e)f(1+zeta)/DU,(1+beta)zeta f/DU),

    Vroot=(s(1+f)e(1+zeta)/DV,
       (1+e)(1+et(1+zeta))/DV,(1+beta)zeta e/DV),

    W=(s(1+f)/Z0,t(1+e)/Z0,(1+beta)/Z0).             (10)

For completeness, if chi=2-xi-eta, the inverse parameter recovery is

    s=xi/(f chi), t=eta/(e chi), zeta=h0/(chi-h0).

Thus the parameterization is not a selected subfamily of the minima triangles.

Use six cut fractions in the exact order

    (a,h,k,l,u,v),
    a,h,k,l,u,v>=0,
    a+l<=1, h+u<=1, k+v<=1,
    ah+kl+uv<1.                                      (11)

The six root generators are

    U+a(Vroot-U), U+h(W-U),
    W+u(U-W), W+v(Vroot-W),
    Vroot+k(W-Vroot), Vroot+l(U-Vroot).               (12)

Redundant generators are removed by the true hull. The domain is a product of three closed two-dimensional simplexes, with the positive-root-area condition retained.

Define positive determinant quantities

    j=(1+e)(1+f)Kc/(Z0 DU DV),
    d1=f(1+zeta)(1+e)Kc/(DU DV),
    d2=e(1+zeta)Kc/DV.

For the full containing body P_R, four actual positive tetrahedra give

    LR=6VR=1+d1+d2+j,
    ER=24BellR=1+b+c+d+d1(b+d)+d2(b+c+d)+bj,

    24JR=B+C+D+d1(B+D+U+Vroot)
          +d2(B+C+D+Vroot)+j(B+U+Vroot+W),
    MR=24NR=n(24JR).                                 (13)

Set

    pD=j(d/b)ah, pC=j(c/b)kl, pB=juv,

    vD=D+3U+a(Vroot-U)+h(W-U),
    vC=C+3Vroot+k(W-Vroot)+l(U-Vroot),
    vB=B+3W+u(U-W)+v(Vroot-W).

The complete ORIGINAL reduced-body integrals are

    L=6V=LR-pD-pC-pB,
    E24=24Bell=ER-dpD-cpC-bpB,
    24J=24JR-pD vD-pC vC-pB vB,
    M24=24N=MR-pD n(vD)-pC n(vC)-pB n(vB),
    T=M24/(L E24).                                   (14)

The root xy-area is

    beta j(1-ah-kl-uv)/2.

These formulas retain all three distinct corner masses and the mixed C-D contribution in the detached containing body. They recompute X,Y,Zmoment after every replacement; no old centroid is carried along.

## 6. Complete value proof on the reduced domain

The proof has three exhaustive sectors. The newly executed certificate covers all cut fractions in (11), not only symmetric cuts or small deficits.

### Positive clearing factors

Put

    Dcal=Z0 DU DV,
    Hcal=(1+beta)(1+e)(1+f),
    Lhat=Dcal L,
    Ehat=Hcal Dcal E24,
    Mhat=Hcal Dcal^2 M24.

The displayed actual integrals give these polynomials directly, and

    T=Mhat/(Lhat Ehat).                               (15)

Both denominator factors are positive on every actual body in the domain.

### Sector A: an entire T<=2 region

Suppose beta<=sf+te. Substitute

    beta=A0(sf+te), 0<=A0<=1

into 2LhatEhat-Mhat. Expand in the unrestricted nonnegative variables s,t,e,f,zeta. Every one of the3699 coefficient polynomials has nonnegative tensor Bernstein coefficients on the remaining product domain

    A0 in[0,1],
    (a,l), (h,u), (k,v) in the unit two-simplex.

The exact check gives611242 positive and108889 zero coefficients. No subdivision or feasibility pruning is used. Thus T<=2 throughout this sector.

Its geometric meaning is

    x(W)+y(W)>=1.

W is the canonical containing corner determined above, not necessarily a true vertex of P. The theorem does not replace this condition by a statement about an arbitrary actual root point.

### Sector B: the full complementary nonprism region

Let

    gamma=beta-sf-te>0.

The actual containing-body support is

    x+y+kappa_zeta z<=1,
    kappa_zeta=1-(1+zeta)Kc/[(1+beta)zeta]             (16)

when zeta>0. Its nonprism sector kappa_zeta<=0 is equivalent to

    q=gamma zeta/Kc in[0,1].

Use the full substitution

    beta=gamma+sf+te,
    zeta=q(1+sf+te)/gamma.                            (17)

The cleared threshold polynomial is

    P203=gamma^4[203LhatEhat-100Mhat] after (17).        (18)

It has50992 nonzero terms. Its exact decomposition proves

    P203>=P00>0,                                     (19)

where P00 is its complete e=f=0 coefficient.

**Ordinary groups.** Except for endpoint exponent pairs

    (e,f)=(0,0),(1,0),(0,1),(2,0),(0,2),

expand also in s,t. There are2361 groups. For2357 of them, one tensor certificate on gamma>0, q in[0,1] and the three cut simplexes proves nonnegativity. The positive gamma axis is compactified by gamma=x/(1-x), with only positive factors cleared.

The other four groups have (s,t,e,f) exponents

    (0,3,1,1),(1,2,1,1),(2,1,1,1),(3,0,1,1).

They contain none of a,h,k,l, and are certified on the larger cube in gamma,q,u,v with2,3,3,2 leaves. The ordinary part totals2367 leaves,2622968 positive coefficients and1017628 zeros.

**The linear endpoint coefficients stay coupled in s,t.** By the exact symmetry exchanging s,t; e,f; a,l; h,k; and u,v, it suffices to treat the f coefficient. Divide it by gamma^3 and set

    S=s+t>0, lambda=s/S in[0,1].

The resulting polynomial is affine separately in lambda,q,a and quadratic in h. It is independent of k,l. Its h^2 coefficient is exactly

    -100a gamma^2(gamma+1)(gamma+2)<=0.

At a=0 it is independent of h. Consequently its complete domain is covered by checking a=1, h=0 or1-u, and the four lambda,q endpoint combinations. These eight four-variable certificates have3,3,6,8,26,11,13,11 leaves, in the source's deterministic order.

**The pure quadratic coefficients also stay coupled.** Divide the f^2 coefficient by gamma^2 and use the same S,lambda. Its h^2 coefficient is

    -100a gamma^2[
       S gamma^3 lambda+S gamma^3
       +6S gamma^2 lambda+3S gamma^2
       +7S gamma lambda+3S gamma
       +S lambda+S+2gamma^3+6gamma^2+4gamma],

which is nonpositive on the whole domain. Thus h=0 and h=1-u suffice. On each face, the three degree-two Bernstein coefficient polynomials in lambda are nonnegative for gamma,S>0 and q,a,u,v in[0,1]. Their six certificates have1,1,1,1,4,4 leaves.

The fourteen coupled certificates total93 leaves,27779 positive coefficients and4693 zeros. The linear and quadratic e cases follow from the explicitly checked exact symmetry.

This proves that every nonconstant e,f coefficient of P203 is nonnegative on its actual coupled cut domain. It is not a comparison of independently selectable moments. The parameter change (17) varies beta and zeta together, so (19) must not be renamed into the parent's false fixed-parameter endpoint-zero trace comparison.

### Strictness comes from one real zero-endpoint body

Put Z1=gamma+s+t and w=uv. Exact expansion gives

    P00=gamma^4 F0,

    F0=203(Z1+1-w)[(gamma+2)Z1+1-w]
       -100(gamma+2)[2Z1^2+2Z1+s+t
                        -w(3(s+t)+gamma(u+v))].       (20)

This is the cleared original threshold deficit of the real zero-opposite-endpoint body with

    b0=1/(1+gamma), c0=d0=0,
    U0=D, V0=C,
    W0=(s/Z1,t/Z1,(1+gamma)/Z1),
    root=conv(D,C,W0+v(C-W0),W0+u(D-W0)).

The D- and C-corner cones have zero volume at these endpoints, and the canonical marks restore the corresponding actual root corners. Their disappearing coefficients are not free mass choices.

The root xy projection lies in Delta and contains CD. Replacing it by the actual upper band rho<=x+y<=1 of the same area preserves original V and Bell and increases N. This follows directly by comparing the affine function x+y on two sets of the same area. The band's trace is

    H(b0,rho)=2(1-b0^2)(1-b0 rho^3)
                  /[(1-b0 rho^2)(1-b0^2 rho^2)].

The complete source independently certifies on the closed unit square

    203(1-br^2)(1-b^2r^2)-200(1-b^2)(1-br^3)
      >=(1-b)^2/1000.                                (21)

This scalar certificate has15 leaves,297 positive coefficients and three zeros. Thus H<203/100 for0<b<1,r<1. If uv=1, the constant-coefficient body is exactly T0 with trace2. In either case F0>0. Equations (19)–(21) prove the strict bound throughout Sector B, including zeta=0 through q=0.

### Sector C: the actual projection-prism region

If gamma>0 and kappa_zeta>=0, inequality (16), together with z>=0, gives x+y<=1 on the entire actual P_R and hence on P. Since T0 is retained, its actual xy projection is exactly Delta. Apply the accepted original-body projection-prism theorem to P itself.

The walls gamma=0 and kappa_zeta=0 are covered explicitly. These three sectors exhaust every positive beta,s,t,e,f and every zeta>=0. Together with the corner dominance, they prove (1) for the original arbitrary root.

## 7. Boundary and proper-patch bookkeeping

The three cut-simplex boundaries are included in the certificate. Zero individual deficits, coincident root generators, a vanishing middle side segment and maximal-facet mergers are handled by the actual hull, not by treating integration diagonals as edges. Positive root area is equivalent to ah+kl+uv<1 in the reduced model.

For marked coordinate patches with x,y>=0 on F, choose q in relint F with qx,qy>0 and contract the root toward q. The contraction remains in z>=0 and ell=0 and gives proper ABC/ABD for every positive contraction parameter. Actual moments converge. Therefore the marked positive-area closure has T<=203/100. This is a uniform ceiling separated from51/25, so exclusion of T=51/25 does not depend on transferring equality through a proper resolution.

Finite full-dimensional limits with finite endpoint limits have V>=1/6 and Bell>=1/24 because T0 remains. The original ratio is continuous there. Such limits inherit T<=203/100 even if the root area disappears or b tends to1. A collapsed support is not called a root facet, and no formula containing1/(1-b) is evaluated at b=1. Infinite-coordinate parameter limits are not declared bodies.

The actual corner replacement preserves positive root area exactly. It therefore does not require an equality-versus-strict-violation rescue to prove the proper theorem. Its change of full J is retained explicitly in (14).

## 8. Exact controls and useful negative reduction boundary

The autonomous source contains28 audited body records: the ten parent's marked fan constructions and their ten actual dominating successors, plus eight additional controls. The111 input and successor coincide, so28 is a record count, not a claim of28 distinct bodies.

### All ten fan reductions

The common endpoint/container input is

    (beta,s,t,e,f,zeta)=(3,1/2,9/8,1/9,1/4,0).

In the root-parallel image, use corners

    U'=(9/5,1/5), V'=(1/5,9/5), W'=(1/5,1/5),
    z'=2-x'-y'.

At a corner p with previous and next corners in the order U',V',W', a chain of length L>0 consists of all L+1 points

    p+((1-r/L)^2/8)(prev-p)+(r/L)^2(next-p)/8,
    r=0,...,L.

For L=0 retain p. The lengths at U',V',W' are i,k,j, where i+j+k=3. Map each point to the ORIGINAL coordinates by

    Limage=6+x'+6y',
    (x,y,z)=(5x'/Limage,10y'/Limage,4z'/Limage).

Every original is true proper10/17/9. The corner lemma is executed using exact original polygon areas and first moments, not image area. It preserves each body's own V,Bell and root area. All nine patterns other than111 have strictly increased trace. The successors have

    8/13/7 if only one corner chain is nonempty,
    9/15/8 if two are nonempty,
    10/17/9 for111.

Every original and successor has its true maximal facets, true edges, two positive volume fans, own centroid, original integrals and full primitive packet audit in the generated report. Coinciding equilibrium counts in these examples are not promoted into a mechanics-preservation theorem.

### A genuine high-trace proper111 control

Use

    (beta,s,t,e,f,zeta)=(3,1/100,1/100,1/100,1/200,0),
    (a,h,k,l,u,v)=(1/100,1/100,1/100,1/100,5/6,5/6).

Thus b=1/4,c=1/101,d=1/201. Equations (10),(12) give all six rational root vertices in labels4..9. Its complete outward maximal cycles are

    012,031,02943,1782,1356,167,289,345,498765.

Its17 true edges are

    01,02,03,12,13,16,17,28,29,34,35,45,49,56,67,78,89.

Its original data include

    V=5064842321083/27188154543600,

    J=(31826483935109874620122657/657062886654824288267520000,
       47976448074397743518008171/985594329982236432401280000,
       295257221547259/6158117004125400),

    Bell=79387314465011357/1471857934372329600,
    N=142677889988168377926158949941/1168382510538358062141803520000,
    root_xy_area=12317787391/80024001600,

    T=19546870928379067775883776141917
        /9650021521428339402716052951144
      approximately2.0255779621811514.

The own centroid is exactly J/V, not a transported point. Under the identity metric its actual strict S/U/H is4/4/6, with no physical weak point and no zero primitive. This is a useful nonwinning10/17/9 control, not110 and not a threshold counterexample.

### Further complete inputs

In the same parameter order, the other controls are:

    regular cut=(1/5,3/10,1/4,1/10,2/5,3/10);

    detached_three_corners:
      (3,1/10,1/5,1/9,1/4,1/10), regular cut;

    outer:
      (3,2,3,1/2,1,1), regular cut;

    outer_wall:
      (7/6,1,2,1/3,1/2,1), regular cut;

    prism_wall:
      (3,1/10,1/5,1/9,1/4,377/1063), regular cut;

    beyond_prism_wall:
      (3,1/10,1/5,1/9,1/4,754/1063), regular cut;

    near_high_detached:
      (3,1/10000,1/10000,1/10000,1/5000,1/6),
      cut=(1/100,1/100,1/100,1/100,5/6,5/6);

    side_gap_seam:
      (3,1/10,1/5,1/9,1/4,1/10),
      cut=(1/5,3/5,1/4,1/10,2/5,3/10).

The six generic detached controls are10/18/10. The side-gap seam is9/17/10, not E17's10/17/9. The near-high detached trace is approximately2.028641029297955. The eight extra records, in source order, have strict counts

    446,7611,648,446,446,446,446,446,

where7611 means(S,U,H)=(7,6,11), not a concatenated vertex count. All28 records together have1832 nonzero audited true-edge primitives and no weak edge packet.

### What failed and what repaired it

The initial three-triangle calculation did not by itself cover curved or multiedge missing corners. The planar lemma supplies the missing actual-body reduction, preserving three separate masses rather than pretending total area is enough.

A plain coefficientwise separation in s,t also fails. In the linear-f coefficient, the s^2 group evaluated at gamma=1,q=a=h=k=l=u=v=0 is exactly-86. The source checks this negative value. It is a failed polynomial proof requirement, not a body. Retaining S=s+t and lambda=s/S, together with h-concavity and the actual cut-simplex constraints, repairs the proof on the complete domain.

Floating probes were used only to choose an algebraic organization. No finite sample failure is used as an exclusion, and no floating point located by those probes is asserted as a construction.

## 9. Scientific effect and precise remaining complement

The entire positive-octant proper root-only landscape with0<b,c,d<1 is now below51/25. This includes both the attached ten-fan sector and arbitrary detached roots with D-,C- and B-controlled boundary chains. The preceding detached single-B theorem is a proper subcase of the present result, not the full new scope.

The reusable advance is the original-density three-corner dominance: it controls arbitrary corner-chain complexity, preserves each anchor's ell-law separately, and is compatible with unequal positive root values. It does not require a fixed-lattice derivative, an all-body stationarity assumption or polyhedral attainment.

The remaining root-only target must lie outside this octant/endpoint domain after the allowed canonical normalization. Negative-z geometry destroys the lower-tetrahedron/upper-Minkowski decomposition used in (7). An opposite endpoint at least1 destroys the automatic positivity of the inverse projective denominator on the entire minimum-coordinate containing triangle; positivity on the actual root alone is insufficient. Positive-ell auxiliary vertices remain a separate obstruction because the body is no longer conv(T0,F).

These are geometric obstacles, not missing coefficient files. The most useful continuation is a genuine replacement or signed-section formulation for the negative-z root sector, retaining the additional canonical reaction and its actual volume law. The sharp constant within the newly closed positive-octant class is also unresolved, but another small threshold collar there is no longer needed for51/25.

For E17, the exact conclusion is a trace theorem on every realization of the ten specified marked fans. A mechanical exclusion still needs the literal incidence/root identification showing that the relevant mechanical trace demand uses these genuine triangles and this root-only octant chart. No such global identification is supplied or inferred here. The minimum bounds34..622 and all catalogue counts remain unchanged.

## 10. Exact recovery and observed receipts

The new reconstruction uses CPython3.13.5, NumPy2.3.5 and SymPy1.14.0, assertions enabled. It has no external data, random seed, numerical tolerance, parent import or omitted helper. The wrapper fixes OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1.

The initial cube and simplex Bernstein transforms are independently inverted to the original power coefficients using exact finite differences. Cube subdivision is integer de Casteljau arithmetic. Both children are retained at every split; the full prefix cover and exact Kraft sum are checked. The simplex tensors certify their whole domains without subdivision. Intentional zero coefficients are retained; strictness comes from the actual constant-coefficient body and (21).

|Component|Groups or cases|Leaves|Positive coefficients|Zero coefficients|
|---|---:|---:|---:|---:|
|Outer T<=2|3699|3699|611242|108889|
|Inner ordinary groups|2361|2367|2622968|1017628|
|Inner coupled cases|14|93|27779|4693|
|Scalar H envelope|1|15|297|3|

These are certificate counts, not incidence or body counts. The analytic geometry is not claimed proof-assistant formalized or independently peer-reviewed.

Observed pins:

    positive_octant_root_203_v1.py
    28298bytes
    SHA256 8c39f3c5fcc647d89794aa13a81c9c8f475ddedf323a56fb65c001f9e36f8cb9

    positive_octant_root_203_v1.json
    1671422bytes
    SHA256 3f6f06cb16c4ef76651ba7d4b0422698f082d2b1e367ccf453d5dbf40c5c77ac

    recover_positive_octant_root_203_v1.py
    14045bytes
    SHA256 dfe24653811c89ee1351d504f19bde49b140c1f3266d567140f78324b8bba70f

Save the complete capsule below with UTF-8/LF and one final LF. In a fresh directory run

    python -S recover_positive_octant_root_203_v1.py sources work
    python -S recover_positive_octant_root_203_v1.py build work
    python -S recover_positive_octant_root_203_v1.py verify work

The standard-library wrapper deliberately launches its exact child without-S so the pinned NumPy and SymPy are available. Expected and observed markers are

    POSITIVE_OCTANT_ROOT_SOURCE
    POSITIVE_OCTANT_ROOT_SUMMARY
    POSITIVE_OCTANT_ROOT_ONLY_203_EXACT_PASS
    POSITIVE_OCTANT_ROOT_203_SELF_CONTAINED_RECOVERY_PASS

Convenience copies: [complete readable source](sandbox:/mnt/data/positive_octant_root_203_v1.py), [exact certificate and actual-body report](sandbox:/mnt/data/positive_octant_root_203_v1.json), and [autonomous recovery wrapper](sandbox:/mnt/data/recover_positive_octant_root_203_v1.py). The following literal capsule contains every source byte and exact new input; none of those links is a dependency.

## Complete autonomous capsule


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]
