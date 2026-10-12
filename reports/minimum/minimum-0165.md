# minimum-0165

AI research report · 2026-09-21 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# NEGATIVE_ANCHOR_EXPOSED_EDGE_ROOT_BASE_AND_VALUE_V1

## 1. Main results and exact remaining boundary

This continuation proves a new value bound on a whole negative-anchor geometric sector, removes most possible ordinary third/fourth-anchor facets at a genuine maximum, and supplies the correct coordinate-rotation test when a negative marked vertex is nonsimple or its coordinate face is enlarged.

Let a>b>0 and c,d>0. All maxima below are polyhedral local maxima in the **full joint marked-body/affine-root class**, with the original uniform volume filling, not maxima constrained to a fixed lattice or to fixed G signs. At least one of G(C),G(D) is negative.

**Whole negative-z sector.** Every such maximum with actual material below z=0 satisfies

    T < 3[a+b+max(c,d)]/[2a+b+max(c,d)].                 (V)

Consequently, throughout the complete endpoint sector

    b+max(c,d) <= 9a/8,

a putative maximum with T>=51/25 must lie entirely in z>=0. Its plane z=0 is then a genuine maximal facet containing A,C,D. This applies to enlarged coordinate patches, nonsimple C/D, arbitrary numbers and sizes of free polygons, and ordinary C/D facets. The proof supplies a strictly improving **whole AC or AD facet hinge** whenever the contrary geometry satisfies the necessary mark and auxiliary-vertex conditions. It is not a claim that cutting off z<0 monotonically improves an arbitrary nonstationary body.

**Ordinary-facet reduction.** No ordinary A facet can occur at any full joint negative-anchor maximum. If either the body is proper33 or it has material below z=0, there is **at most one ordinary facet in total**. Its base is a true edge at the minimum of G on the root. An ordinary C facet then requires

    c<min(b,d),

and an ordinary D facet requires d<min(b,c). In particular, in the entire proper33 sector with exactly one negative C/D value, there are no ordinary C or D facets at all; only a possible ordinary B root-minimum triangle survives. In the same proper-or-negative-z domain,

    F_true<=10, V_true<=16, E_true<=24, deg(A)<=4.

These are trace-extremizer counts, not mechanical complexity exclusions.

**Height and marked-edge consequences.** At any full-class fixed-ell polyhedral maximum with T>=2, independently of the C/D signs,

    max_P ell = max(a,b,c,d)=:M,

and every auxiliary true vertex satisfies ell(v)<49M/68 when T>=51/25. This is a relative endpoint-height theorem; ell<=a follows only when a is the largest endpoint. At a full joint maximum, G(C)<0 forces C to be a true vertex and AC to be a true edge, even when the full coordinate face is a polygon and C is nonsimple. Its coordinate face has at most six true vertices, or at most five if G(D)>=0.

**Correct nonsimple coordinate reaction.** Releasing and rotating a coordinate plane produces two tangent-cone linear programs, not generally a single two-sided third-edge equation. Their exact support interval and the true whole-coordinate-polygon integral must contain a moment-dependent threshold. Failure gives an actual improving joint rotation with its determinant, changed endpoint, and original V,E,N accounted for. A new rational 10/17/9 body with four free quadrilaterals and degree-four C has a strict gap between the two tangent-cone endpoints; the old simple-C direction is genuinely infeasible on one side.

Seven exact actual bodies are preserved, including this nonsimple negative-C control, enlarged coordinate quadrilateral and pentagon controls, a strictly improving joint rotation, its properization, and an independent fixed-ell whole-facet improvement. None is stationary or a 110 attainer. The whole negative-anchor problem remains open on the explicitly described residual geometry in Section 10. No E17 registry count or bound 34<=Cmin<=622 changes.

## 2. Reading, source authority, and dependencies

I read the complete 1,753-line new journal, its complete branch memory and literal parent payload through EOF. The initially truncated line 272 was separately recovered in full. The two required unchanged analytic sources remain fully available in this chat and were read in full. No source needed for the new proof is inferred from an inaccessible identifier.

| Supplied source | Bytes | SHA-256 |
|---|---:|---|
| research-journal(20260921-135318).md | 298241 | ca057516800b577dfb4c79ebd09bf6891f44758bc93ca19555945ae9eb7f4674 |
| POLYHEDRAL_TRACE_STATIONARITY_RIGIDITY_V1, [internal-source-reference] | 14798 | 8dc6ce8812298f59a61b404ccba7c09fef867bb8844a8952bf1cacc638bcc2b9 |
| ROOT_DUALITY_JOINT_VARIATIONS_V1, [internal-source-reference] | 18784 | 73eb04d63deeab693d29533819d3b95c4e1af3cc01d756987381aaa2bb4c2ed8 |

The literal parent is **minimum-0163**, immutable SHA-256 **6cbb192cd6ad2b1027cf9bf21d2f2a75ab372b307fe4c5c0fa1091b9b63bb0fc**, TWO_ANCHOR_JOINT_ROTATION_EXCLUSION_254_OVER_125_V1. Its completed positive-G sector is not reopened. Its actual tetrahedron-plus-visible-caps identity is reused and explicitly distinguished from the new negative-sector deductions.

The background theorem requiring at least three free polygons at a proper33 full joint maximum is retained, not re-enumerated. Its full old capsule is not an input to the new proof. The source discrepancy in its historical Case R/P trace fractions is already explicitly corrected in the new journal; I use neither those incorrect fractions nor a relabelled body.

**No inherited joint-mass upper bound, upper-defect theorem, negative-G endpoint cover, Berwald covariance completion, or absent old greedy/root executable is a premise of the new results.** The input statements used are auxiliary-vertex positivity, the free-facet spike inequality, ordinary-facet rigidity, whole-plane first variation, and genuine joint mark admissibility. Their proofs are supplied. Global localization and attainment are not reproved or strengthened here.

## 3. Common actual-body setup and permitted reactions

Put

    A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
    T0=conv(A,B,C,D), alpha=a-b>0, s=a+b, S=c+d,
    hc=s+c, hd=s+d,
    ell=a+(d-a)x+(c-a)y-alpha z,
    n=hc x+hd y.

Let P be bounded and full-dimensional, with

    T0 subset P subset {x>=0,y>=0,ell>=0},

and with a positive-area root F0=P intersect {ell=0}. All quantities below use the actual uniformly filled P:

    V=int_P 1, J=(X,Y,Z)=int_P(x,y,z), g=J/V,
    E=int_P ell, N=int_P n, t=6V,
    r=N/V, q=N/E=Tt, T=N/(6VE)=r/(6E),
    G=n-r-q ell, LA=(r+qa)/3, LB=(r+qb)/3.

The coordinate faces may initially be larger than ABC and ABD. Proper33 means those are the actual maximal coordinate triangles. A free facet is any true maximal facet other than the two coordinate facets and the root. An ordinary facet contains exactly one canonical mark.

At a full-class fixed-ell local maximum, every auxiliary true vertex has G>0, A and B are true vertices, and the actual axial section is exactly AB. Every free facet F satisfies

    max_F G+3 mean_F G<=0.                              (3.1)

An ordinary facet with mark X is the true triangle [X,U,V], with

    G(X)<0, G(U)=G(V)=LX:=-G(X)/3>0.                    (3.2)

These are whole-body statements permitting lattice changes; they follow from the exact finite trace comparison, thin-edge caps, whole-plane pivots and actual added pyramids.

For a convex polygon F, a true vertex X, and an affine function phi>=0 on F with phi(X)=0, a true fan from X gives

    int_F G phi <= [G(X)+3 max_F G]/4 * int_F phi.       (3.3)

On a fan triangle [X,U,V], with phi(U)=u and phi(V)=v, the exact product integral is

    area/12 * [G(X)(u+v)+G(U)(2u+v)+G(V)(u+2v)].

Thus no integration diagonal is being treated as an independently movable edge. When a free facet contains exactly two negative canonical vertices X,Y sharing a true edge, its hinge around XY is admissible in both signs. If phi is the nonnegative transverse affine coordinate, stationarity gives int_F G phi=0. Applying (3.3) from both endpoints, with strictness on the fan triangle incident to XY, yields

    max_F G > max(LX,LY).                               (3.4)

The strictness follows because G(Y)<0<LX and its coefficient on that triangle is positive. Simplicity of X or Y is unnecessary. The supplied whole-polygon hinge proof justifies this operation directly.

## 4. Negative marked vertices expose genuine canonical edges

### 4.1 The joint mark reaction, with the determinant retained

Hold the physical P and ell fixed. Choose C'=(0,y,z) in the actual x=0 face, with y>0, and affinely restore A,B,C',D to the canonical frame. The new trace is exactly

    T_new={y[s+ell(C')]X+(s+d)Y}/(6VE).

The determinant and changed endpoint are already included. Differentiating along the segment from C to any point of that face gives, at a full joint maximum,

    FC(y,z):=(b+2c)(y-1)-alpha z<=0                     (4.1)

throughout the whole coordinate face. This is the supplied exact marked support reaction.

Suppose G(C)<0. The line FC=0 supports that face at C, while A and B are strictly below it. If C were not a true vertex, the true vertices of its exposed face would all be auxiliary, with strictly positive G. Their convex combination could not have negative G(C). Hence **C is a true vertex**.

Now let R=(0,y,z) be an auxiliary true vertex of the coordinate face with z<=0. Equation (4.1) gives 0<=y<=1. But

    G(0,y,z)=(1-y)G(A)+yG(C)+q alpha z<0,

contradicting auxiliary positivity. Therefore every auxiliary vertex of that face has z>0. Its intersection with z=0 is exactly the segment AC. Thus **AC is a true edge** of P, even for an enlarged coordinate polygon and a nonsimple C. The reflected argument gives D a true vertex and AD a true edge whenever G(D)<0.

### 4.2 A true coordinate-face size bound

The boundary of the negative-C coordinate polygon has order A,B,U1,...,Uk,C. An edge joining two consecutive auxiliary vertices has a second incident facet. That facet cannot contain A,B or C: three noncollinear points on the coordinate plane would make it the same maximal facet. It is therefore either the root or an ordinary D triangle.

The root contributes at most one such edge. Every ordinary D base has both endpoint values LD, so it is a supporting maximum-G edge of the coordinate polygon, which contains negative A and B. There is at most one edge at that fixed supporting level. Hence k-1<=2 and

    |vertices(Fx)|<=6.

If G(D)>=0, ordinary D facets are impossible and the bound improves to five. The same five-vertex bound applies when the later root-base reduction has eliminated nonroot ordinary facets.

This is not proper33. In particular (4.1) bounds ell on the coordinate face **from above**:

    ell<=s+2c-(s+c)y.

It does not force auxiliary y>1. The exact enlarged-face controls in Section 8 exhibit a positive-G root point with y=4/5.

## 5. Actual visible-cap mass gives a new relative height theorem and value bound

### 5.1 The same-body pointwise budget

For p=(x,y,z), sigma=x+y and w=ell(p), let

    tp=6 Vol(conv(T0,p))=1+(-z)_+ +(sigma+z-1)_+.

The two visible canonical facets are ACD and BCD; their exterior pyramids have disjoint interiors. Thus sigma<=tp<=t and their literal uniform ell integral is

    24 E_conv(T0,p)
      =s+S+(a+S+w)(-z)_+ +(b+S+w)(sigma+z-1)_+
      =n(p)+w tp+(b+S)(1-sigma-z)_+ +(a+S)z_+.

Since ell is nonnegative on the actual remainder,

    24E>=n(p)+ell(p)tp.                                 (5.1)

This identity is inherited from the literal parent; its use below does not import the parent's positive-G endpoint restrictions.

### 5.2 All-sign auxiliary height bound

At an auxiliary vertex, G>0, so n>r+q ell. Since r=Tt mu and 24E=4t mu, where mu=E/V, (5.1) gives

    ell(v)<[(4-T)t/(Tt+tv)]mu
          <=[(4-T)t/(Tt+1)]mu.                         (5.2)

A root vertex is auxiliary with n>r, so (5.1) also gives T<4 at such a maximum. For T>=2 the factor in (5.2) is strictly less than one. Write M=max(a,b,c,d). If mu>=M, every canonical vertex would have ell<=mu and every auxiliary vertex ell<mu. The nonconstant affine ell would then have uniform mean strictly below mu, a contradiction. Hence mu<M, all auxiliary heights are below M, and

    max_P ell=M.

A positive tetrahedral fan from a root point gives mu<=3M/4. At T>=51/25, (5.2) therefore yields

    ell(v)<[(4-T)/T]mu<=49M/68.                         (5.3)

This holds for either sign of G(C),G(D). It proves ell<=a in the negative sector only under the separate hypothesis c,d<=a. When c,d<a, A is the unique maximum-height vertex. The result is not asserted for arbitrary nonstationary bodies.

### 5.3 Whole negative-z value theorem

Assume a full joint maximum has material below z=0 and G(C)<0, after swapping C,D if necessary. Section 4 supplies the true edge AC. Its other incident facet H cannot contain D, because then its plane would be z=0, contrary to the negative-z material. It cannot contain B, because that would be the coordinate plane. Thus H contains exactly A,C and has an admissible whole-plane hinge with phi=x. Equation (3.4) gives max_H G>LA.

On the other hand, (5.1) and 4r=24TE imply

    3[G(p)-LA]
      <=(3-T)n(p)-qa-(3q+Ttp)ell(p).                  (5.4)

If T>=3 this is negative everywhere. Otherwise n(p)<=Ht, with H=a+b+max(c,d), and q=Tt. Consequently

    T>=3H/(a+H)

would force G<=LA throughout P. The inequality is strict at C because c>0. The actual fan formula on H then gives int_H Gx<0, contradicting its zero hinge reaction. This proves (V).

At T>=51/25 the sufficient endpoint condition for this contradiction is exactly

    b+max(c,d)<=9a/8.

The value bound is not a small-endpoint collar: for example a=1,b=1/2,c=3/5,d=1/10 lies within it. Whenever a candidate in this class already satisfies the necessary mark and auxiliary conditions, the proof gives an explicit ascent. The free AC plane has equation z=-u x with u>0; replacing it by z=(-u+epsilon)x, epsilon>0 small, has derivative numerator -int_H Gx>0. All canonical marks and protected halfspaces remain admissible. The exact finite trace test has only a quadratic-volume correction, so sufficiently small positive epsilon strictly improves T.

The conclusion for a hypothetical high-trace full maximum is **P subset {z>=0}**. It is not a theorem that the finite operation P intersect {z>=0} improves every input, nor that repeatedly following the hinges terminates at that plane.

## 6. Ordinary-facet erasure and the genuine residual finite geometry

### 6.1 A supporting-plane identity that caps G globally

Let F=[X,U,V] be an ordinary facet, G(X)=-3L and G(U)=G(V)=L>0. Let J be the other facet incident to its true base UV.

If J is not the root, it contains a negative canonical point Y different from X. For a coordinate facet this can be A or B; for a free facet it follows from (3.1) and auxiliary positivity. Choose its affine slack h>=0 on P normalized by h(X)=1. Then

    K=G-L+4Lh

vanishes at X,U,V, and K(Y)=G(Y)-L<0. Thus its zero plane is precisely F, the body lies on K<=0, and

    G<=L throughout P.                                 (6.1)

If J is the root and UV is its maximum-G edge, use h=ell/ell(X). A root interior point gives K<0 and the same conclusion. For X=A the root case always gives (6.1), even if UV were a root minimum, because

    K(B)=(b-a)(4r+qa)/(3a)<0.

These orientations are actual support-plane orientations, not free signs attached to a formal G-level edge.

### 6.2 No ordinary A facet

If P lies in z>=0, containment of T0 makes the tangent cone at A the positive octant. Its only incident facets are x=0,y=0,z=0, and the latter contains A,C,D. Hence there is no ordinary A facet.

Otherwise the negative marked vertex exposes AC or AD as in Section 5. Its free two-negative-mark hinge has maximum strictly greater than LA. But every ordinary A facet gives the global cap G<=LA from Section 6.1. This contradiction proves:

    No ordinary A facet occurs at a full joint negative-anchor maximum.

Every free facet through A therefore contains C or D. Each pair AC,AD already uses a coordinate facet and can supply at most one additional facet. There are at most two free A facets, so deg(A)<=4. The pair-count statement is the literal true-facet incidence argument of the supplied rigidity source.

### 6.3 At most one ordinary facet, based at the root minimum

First suppose P has material below z=0. A negative C supplies a free AC facet with max G>LA and max G>LC; a negative D similarly supplies AD with max G>LD. Since LA>LB, every possible ordinary B,C,D level is exceeded on one of these genuine hinge facets. Therefore the global cap (6.1) is impossible for any ordinary facet. Every ordinary base must be on the root, and must be its minimum-G edge.

The same conclusion holds whenever P is proper33, including P subset {z>=0}. In that remaining case the free facet at BC is a genuine two-mark facet whenever C is negative. It cannot contain D: z>=0 together with the BCD support and x,y>=0 would force P=T0 and eliminate the positive root. Thus the BC hinge has max G>LB,LC. The reflected BD hinge handles a negative D. Again every nonroot or root-maximum ordinary base is impossible.

On the root, G=n-r is nonconstant because a>b and n has no z coefficient. A convex polygon has at most one true edge at its minimum supporting level. A physical edge has exactly two incident facets. Hence in the entire proper-or-negative-z domain,

    number of ordinary facets <=1.                     (6.2)

No sum of counts from separate realizations is used.

### 6.4 A third/fourth-anchor cap can only be anchored at the smallest endpoint

For the surviving ordinary root-minimum triangle with anchor X, put

    eX=ell(X), nX=n(X), LX=-G(X)/3,
    NX=r+LX, betaX=(NX-nX)/eX.

Its actual oriented halfspace is

    n+betaX ell >= NX.                                 (6.3)

For X=C, the other canonical vertices are strictly off that ordinary facet. The B inequality gives betaC b>NC>0 and

    betaC(b-c)>hd.

Thus betaC>0, b>c, and betaC>1. The D inequality is

    (d-c)(betaC-1)>0,

so d>c. Therefore an ordinary C facet requires c<min(b,d). Reflection gives d<min(b,c) for an ordinary D facet.

Since

    G(C)-G(D)=(d-c)(q+1),

the uniquely negative C/D mark has the larger of c,d. It cannot meet the strict minimum-endpoint requirement. Thus **every proper33 full joint maximum with exactly one negative C/D mark has no ordinary C/D facet**, regardless of endpoint size or trace. This is a whole third-anchor stationary exclusion, not just the former at-most-two-polygons boundary.

### 6.5 Counts, actual supporting planes, and the positive-octant remainder

The root and all true facets containing at least two canonical marks number at most nine: the two coordinate facets, at most one extra incidence for each of AC,AD,BC,BD, at most two for CD, and the root. Combining this with (6.2) gives F_true<=10. Euler then gives V_true<=16 and E_true<=24. These counts concern the auxiliary trace maximum only.

For a negative-z maximum, all free nonordinary planes are drawn from the actual types

    AC: z+u x>=0, u>0;
    AD: z+v y>=0, v>0;
    BC: z+y+(1-kappa)x<=1;
    BD: z+x+(1-lambda)y<=1;
    CD: x+y+rho z<=1, at most two distinct planes.

A genuine two-mark BC or BD plane has kappa>0 or lambda>0; their BCD merger is one facet. A CD plane not containing B has rho<1. Two CD planes need not lie on opposite sides of CD or supply opposite upper/lower graphs. The only possible additional free plane is the single actual ordinary root-minimum plane (6.3). Missing or redundant planes must not be counted as facets, and r,q in that plane are the moments of the resulting body, not independently selected coefficients.

At T>=2 and c,d<a, Section 5 makes A the unique ell-maximum. Its true tangent cone, truncated by ell>=0, is therefore a bounded actual pyramid Q containing P. Its base is a triangle or quadrilateral because deg(A)<=4; all sections ell=w are homothetic with factor 1-w/a. P is obtained by at most five further non-A supporting cuts. This is a container, not a trace-monotone filling or a replacement of P's section areas by those of Q.

In the endpoint sector b+max(c,d)<=9a/8, a proper33 maximum with T>=51/25 has z>=0 by (V). Its whole supporting-plane list then reduces to at most eight:

    x>=0, y>=0, z>=0, ell>=0;
    the two true BC and BD planes;
    at most one additional CD plane;
    at most one ordinary root-minimum plane.

For exactly one negative C/D mark, that last plane can only be a B plane. This is **not** the closed flat-A two-anchor family: the additional CD plane may contain neither A nor B. If the additional CD plane is present, the z=0 facet is exactly triangle ACD and CD is a true edge; without it, CD may be only a diagonal of a larger maximal base polygon. The original positive root area and all actual reactions still have to be imposed.

## 7. The correct coordinate rotation at a nonsimple negative mark

The preceding theorem deliberately did not assume C simple. Here is a complete replacement for the old single third-edge reaction.

Let G(C)<0, so C is a true vertex. Remove the physical x>=0 inequality, keeping every other physical supporting halfspace fixed. Let Ni be the outward normals of the other facets active at C. Define two actual tangent polyhedra

    K+={(L,Z): Ni.(1,L,Z)<=0 for every active i},
    K-={(L,Z): Ni.(1,L,Z)>=0 for every active i}.

Both are nonempty. A point in relint ABC is strictly inside every other active halfspace; adding a sufficiently large multiple of its direction from C to either ex or -ex proves feasibility in the respective cones.

For e>0 choose (L,Z) in K+; for e<0 choose it in K-. Put

    beta=1+Le, Ce=(e,beta,Ze),
    beta x-e y>=0                                     (new physical coordinate plane),
    x'=x-e y/beta, y'=y/beta, z'=z-Ze y/beta.           (7.1)

The normalization has determinant 1/beta and sends A,B,Ce,D to the canonical frame. The new affine root endpoint is

    ce=c+e[(d-a)+(c-a)L-alpha Z].                       (7.2)

All other endpoints are unchanged. For sufficiently small parameters, active inequalities are satisfied by Ce, inactive inequalities remain strict, boundedness persists, and a relative-interior patch of the genuine root survives. The normalized body lies in x',y'>=0 and contains T0. The physical body before normalization need not contain old C; Ce is the new marked point.

With Ve,Ee,Xe,Ye denoting the actual physical uniform integrals before normalization, the exact trace is

    Te={beta(s+ce)Xe+[hd-(s+ce)e]Ye}/(6VeEe).            (7.3)

The only moving physical facet has outward speed -y. Let

    IC=int_(actual Fx) G y dy dz.

The derivative numerator at e=0 is

    DC(L,Z)=X[(b+2c)L-alpha Z+d-a]-hcY-IC.              (7.4)

At a full joint maximum, DC<=0 on K+ and DC>=0 on K-. Equivalently, writing

    w=(b+2c,-alpha),
    HC=(hcY+IC)/X-(d-a),

one must have the exact interval condition

    sup_(K+) w.(L,Z) <= HC <= inf_(K-) w.(L,Z).          (7.5)

The C-mark support condition controls the recession costs, so these two-dimensional linear-program extrema are finite and attained. Their geometric order follows directly: the difference of a K+ point and a K- point is a tangent direction in the old coordinate face, where the mark reaction is nonpositive.

For a proper simple C, the two extrema coincide at its unique third-edge direction, recovering the parent equality. For a nonsimple C they can have a strict gap. If the coordinate face is a polygon, IC must be its actual whole-polygon integral. The formula

    IC=[G(A)+G(B)+2G(C)]/24

is available only for the actual triangle ABC. The enlarged controls below show the two integrals differ exactly.

This is a joint marked/root variation even though the physical ell is held fixed before normalization: after (7.1), its coefficients and ce change. Root-area motion, normalization, and the changed n are not optional corrections. A violated endpoint of (7.5) gives a genuine one-sided ascent. A strict marked-patch improvement can subsequently be properized by conv(T0,(1-eta)Q+eta qroot), using a root-interior point and sufficiently small eta; only strict convergence of the actual integrals is asserted, not monotonicity of properization.

## 8. Seven exact actual controls and a genuine failed simplification

### 8.1 Primary nonsimple negative-C body

The new primary body P has endpoints

    (a,b,c,d)=(1,1/4,1/5,1/100),

and these nine literal supporting halfspaces:

    x>=0, y>=0,
    z>=-x/100, z>=-y/200,
    z-9x+y<=1, z+x-9y<=1,
    ell=1-99x/100-4y/5-3z/4>=0,
    z+(1313/1500)x+(2551/3750)y<=1,
    -900901x+100080y+75z<=100080.

The last plane is a genuine ordinary C triangle. All nine planes are irredundant. The body is bounded, proper33, has four genuine free quadrilaterals, degree-four C, degree-three D, and a hexagonal root. Every auxiliary true vertex is on the root with positive G, while G(C)<0<G(D). Thus it is not a two-anchor body and is not merely a control in the already closed at-most-two-free-polygons class.

Its complete true vertices, in lexicographic order, are

    0: (0,0,0)
    1: (0,0,1)
    2: (0,1,0)
    3: (20001/819050,2497738/2047625,-181/4095250)
    4: (10008/409525,19984607/16381000,-2502/10238125)
    5: (59950/2226377,1851625/2226377,914302/2226377)
    6: (400/1033,800/1033,-4/1033)
    7: (1815050/2448373,23375/2448373,843698/2448373)
    8: (1,0,0)
    9: (196025/194224,25/24278,-1/194224).

The true maximal facet cycles are

    (0,2,4,6), (0,1,2), (2,3,4), (1,5,3,2), (0,6,9,8),
    (0,8,1), (1,8,9,7), (1,7,5), (3,5,7,9,6,4).

The seventeen physical edges are

    (0,1),(0,2),(0,6),(0,8),(1,2),(1,5),(1,7),(1,8),
    (2,3),(2,4),(3,4),(3,5),(4,6),(5,7),(6,9),(7,8),(8,9).

Its original uniform integrals are

    V=408461183647981648982861918267
      /1679543245419896091530680500000,
    E=3041594536329115266110692427481
      /44787819877863895774151480000000,
    N=406830659770173595392150331710366558292488232483
      /2115979238688049766217602422130031338800000000000.

The exact trace is

    2410472249317345914795071210891604311818999728417141657276025
    /1242373304486224342126736658961256650495768204321606446695427
    =1.9402157472420751... .

It is nonstationary: its ordinary C cap violates the stationary endpoint selection and its actual AC hinge is strictly negative. Its purpose is to audit real negative-anchor geometry and variations, not to challenge the threshold.

### 8.2 Enlarged coordinate faces really occur under the necessary sign and mark tests

Let

    R1=(0,4/5,12/25), R2=(0,11/10,4/25).

Both are on the same physical root. Define PE=conv(P,R1) and PEN=conv(P,R1,R2). PE has true 10/17/9 and an actual coordinate quadrilateral; PEN has true 10/16/8 and an actual coordinate pentagon. Both retain G(C)<0<G(D), positive G on every auxiliary vertex, and the full C-mark support inequality (4.1). Their root point R1 has y=4/5<1. Thus these necessary conditions do not imply proper33 or auxiliary y>1. Their full coordinate G-y integrals are computed; substituting the ABC triangle integral is exactly wrong.

These are actual bodies, not planar reaction data. They are not claimed to satisfy all joint reactions.

### 8.3 Nonsimple tangent interval and exact joint ascent

For the primary P, the released C constraints are

    K+: Z>=-1/100, L+Z<=9, 100080L+75Z<=900901;
    K-: all three inequalities reversed.

The cost is w=(13/20,-3/4). Exact primal and dual linear-program calculations give

    (L+,Z+)=(3603607/400320,-1/100),
    max_K+ w.h=46906939/8006400,
    (L-,Z-)=(901/100,-1/100),
    min_K- w.h=733/125.

Their strict gap is 212953/40032000. The actual threshold HC is below the first endpoint, so the positive rotation improves trace. The old simple-C direction (1,901/100,-1/100) is infeasible for that positive side: with e=1/1000000, it violates the displayed integer C-plane by exactly 16381/20000000. It remains feasible for the opposite parameter sign. Therefore one cannot import the old two-sided third-edge equality at this nonsimple mark.

Use e=1/1000000, L=L+, Z=-1/100 in (7.1). The normalized successor Q has

    ce=400303619/2001600000,

true 11/18/9, a genuine coordinate quadrilateral, and T=1.9402199899769939...>T(P). The physical root before normalization is exactly unchanged. The audit independently integrates both the unnormalized cut and the normalized image and checks (7.3), the volume determinant, E, and all three original first-moment transformation identities exactly.

Let qroot be the arithmetic mean of Q's true root vertices and eta=1/10^10. The genuine properization

    QP=conv(T0,(1-eta)Q+eta qroot)

has true 11/24/15, proper33, and T=1.9402199899917154...>T(P). No general monotonicity relative to Q is claimed.

Independently, replacing only z>=-x/100 in P by

    z>=-(1/100-1/1000000)x

gives a fixed-ell whole-facet successor PH, true 10/17/9 and proper33, with T=1.9402158532986824...>T(P). This is the explicit hinge supplied by the new value proof.

### 8.4 Full own-centroid mechanical audits, not 110 claims

The complete source rebuilds the true hulls and maximal facets, integrates V and J by two independent positive fans, and evaluates primal and polar primitives using the same actual centroid and M=Nmetric=I. All primitives of all seven bodies are nonzero; every physical weak count is zero.

| Body | True V/E/F | Strict S/U/H | Trace, approximately |
|---|---|---|---:|
| B0, the eight-plane body before the C cut | 9/15/8 | 5/4/7 | 1.940215748165762 |
| P, primary nonsimple negative-C body | 10/17/9 | 5/4/7 | 1.9402157472420751 |
| PE, coordinate quadrilateral | 10/17/9 | 4/4/6 | 1.933867314749446 |
| PEN, coordinate pentagon | 10/16/8 | 4/4/6 | 1.9350590304410504 |
| Q, actual joint rotation | 11/18/9 | 5/4/7 | 1.9402199899769939 |
| QP, properized joint improvement | 11/24/15 | 5/4/7 | 1.9402199899917154 |
| PH, fixed-ell whole AC hinge | 10/17/9 | 5/4/7 | 1.9402158532986824 |

All coordinates, exact V,E,N,J, own centroids, true facets/edges, same-origin poles and edge packets are regenerated by the capsule. No centroid is held fixed by selecting a reference. The coincident equilibrium counts in these examples are audited outcomes, not a general preservation theorem.

## 9. Failed approaches and evidence limits

I first examined whether the mark support inequality forced proper33 or all coordinate auxiliaries beyond y=1. Its algebra has the opposite ell-bound direction. The exact PE/PEN constructions preserve that failed reduction as a genuine geometric countercontrol; they do not refute the weaker exposed-AC theorem.

The source-only recovery also preserves the completed exact discovery grids. Six root-only-auxiliary hulls and twelve three-anchor halfspace controls were integrated. A fifteen-input aligned C-cap architecture retains the actual auxiliary point (16/25,8/25,-8/125) with ell=1/5,n=8/5 and G=G(C)<0 at endpoints (1,1/2,1/5,1/10); that particular architecture cannot be a full marked maximum. A separate root-corner grid completed sixteen inputs, then stopped because its next proposed B plane excluded D. No assertion is made that the rest of that grid ran or was excluded.

The optional actual two-anchor floating locator used seed 5201, NumPy 2.3.5 and SciPy 1.17.0. It ended at its iteration cap after 16091 evaluations, reporting T=1.9769038541389679 and **G(C)=+0.0005563187809783376**, violating its intended negative-G constraint. It is not an accepted negative-sector counterexample, much less evidence of a universal bound. Its complete source, bounds, population size, tolerances, iteration limit and frozen output are preserved in the capsule.

No numerical search supplies a proof step. The new value and ordinary-base theorems use actual support geometry and exact uniform moments. They do not close all positive-octant negative-anchor maxima, prove arbitrary negative-z deletion monotonicity, remove positive-ell auxiliary vertices, or show that every trace maximization can retain a chosen G-sign sector.

## 10. Continuation-ready reduced problem

The most useful residual class in the broad endpoint sector b+max(c,d)<=9a/8 is now positive-octant geometry with a genuine ACD facet, at least one negative C/D mark, and—when proper33 is imposed—the actual eight-plane list in Section 6.5. In the exactly-one-negative sector, ordinary C/D facets have been removed altogether. The additional CD plane remains the essential distinction from the previously closed flat-A two-anchor theorem.

Outside that endpoint sector, a negative-z maximum still has no ordinary A, at most one ordinary facet, a root-minimum base for it, the strict endpoint selector for C/D caps, deg(A)<=4, and the actual ten-plane bound. When c,d<a, its actual bounded A-pyramid container has a triangular/quadrilateral root section and at most five further cuts. Enlarged coordinate faces and nonsimple negative vertices remain allowed; (7.5), not a guessed equality, is the correct joint coordinate test.

The full affine root reaction remains available on either residual class:

    int_F0 G h/|grad ell|=qV h(g)-3(X+Y)h(w0),
    w0=(gy/[3(gx+gy)],gx/[3(gx+gy)],1/3),

for every affine h, because all four endpoints are positive. These are actual root integrals of the same P. The new reductions use weaker necessary parts of joint stationarity; they do not replace or discard this remaining root compatibility.

## 11. Complete exact recovery and actual replay status

The three exact source units are:

| Source | Bytes | SHA-256 |
|---|---:|---|
| geometry.py | 3745 | 2d043e6a83af2870d05e749b2291ce2678719ddf668419336e92b20a13ef3b2a |
| negative_anchor_certificate.py | 5079 | 2c0ec1f1d4f825e7ce3cb3e4b61b950989ddeb0abaa672f7c75a54dda75518d7 |
| negative_anchor_actual_audit.py | 11506 | 47f03ed60659a4e1c4781da1d21dab8be19d37845421544cbe187b6d5ee47263 |

The exact certificate checks the visible-cap identity in all four regions, mark and coordinate normalization, ordinary root-plane algebra, the 49/68 height arithmetic, the value threshold 9/8, and the whole-triangle product identity. The actual audit reconstructs all seven bodies and all stated finite improvements, including independent original-mass calculations and the true mechanical packets.

| Generated exact output | Bytes | SHA-256 |
|---|---:|---|
| negative_anchor_certificate.json | 1147 | 778f84be158f84f5c99b8dce86eacf89cea2e93e0bc1d891b1f2325d95999dfa |
| negative_anchor_actual_audit.json | 212502 | 4037bc0007f1a1eb83fcd233fc761647c958211ff404ac4f770ec28978d66e77 |
| negative_anchor_certificate_stdout.txt | 372 | b56bf6a913f4554a6fdfd62f5d7456c480aaa3bfa8a6f8dd721765deba7c33f4 |
| negative_anchor_actual_audit_stdout.txt | 1248 | ce5840e5b6a882cd4e4d9526e03feb8f0767a41f8d2e14fb3eb195394310e41d |

Both exact units were executed, then copied with only their complete geometry helper into a fresh directory and executed again. All four output files were byte-identical. The complete capsule below was subsequently executed in another fresh directory, and every final pin passed. No stochastic replay is claimed by these exact checks. The analytic shape-variation arguments are proved above; this is not a proof-assistant formalization of them.

Save the entire following unit as `recover_negative_anchor_v1.py`, UTF-8/LF with one final LF. It is **19965 bytes**, SHA-256 **38b6ce596726f990d9a0dd449dbf4313c29c8fc09aa77452af43d6ef511cebfd**. The decoded twelve-file payload is **34523 bytes**, SHA-256 **31386000004329eb7e10ec9b4ffcadc74043950a8fcfca9fe29fce473bd858e9**. It contains all ten complete exact/discovery source programs and two frozen discovery reports. It needs no parent file, downloaded archive, hidden helper or external input data.

Executed environment: CPython 3.13.5; SymPy 1.14.0 for the symbolic child; standard library for the actual-body audit. Assertions must remain enabled. Run

    python -S recover_negative_anchor_v1.py recovered > recovery_stdout.txt

The observed recovery stdout has **1861 bytes**, SHA-256 **70d64d73e1c8674fe4fac802e2e349cc1ce428dc042a5bbb99c6c2a5ba706d53**. Expected final marker:

    NEGATIVE_ANCHOR_V1_SOURCE_ONLY_COLD_RECOVERY_ALL_HASHES_PASS

Other exact markers include:


[Encoded source block omitted; the code in this passage is incomplete.]

### Complete runnable recovery source

```python
"""Complete negative-anchor exact recovery, CPython 3.13.5.
The symbolic child requires SymPy 1.14.0; the actual-body child is standard-library.
Usage: python -S recover_negative_anchor_v1.py [OUTPUT_DIRECTORY]
Only the two exact units run. Extracted locator programs remain NONPROOF.
No parent file, archive, network, hidden helper or optimization is needed.
"""
from pathlib import Path
from hashlib import sha256
import base64,json,platform,subprocess,sys,zlib
assert __debug__ and platform.python_version()=='3.13.5'
assert len(sys.argv)<=2
DATA="""
c-p;vYj@hZ((w1^SNQC+o`nrE!CZ2q>RJh<N%m%wG)ddEl;vfN2~NN`HV{Zx|NA>Ll6)Z~ZTC6vbM|Slbs0&cnbFK>B!B<Iokf8c
+1|===XMy)23|Q_|8e-oD4I>RXf~VMvIOO6{xqCLb8X<n-nW3t+<LRAH;>jTtN1PW77V?SChF-Pf3I82s#Ge5ariCJE-D;r>qb-a
Lasxm!LUSK{4~Umg~gi=8!(p*xfeDU3XIXb$H$5Ru>P%0j!N-y$<w{b#B`0fyaK5~#C21@H?7j5<Q4Uy=@<sHOn7wRk-@KH4gmUW
G~!l?UR{J1dGkdSXoJ~stuG@l)GsQ%LO5{(FD~>;Jw1pRR5AJhB82k(NVDz0nR>R(dBL`)jvv@|fyT(?;L{<zGS24M<xXi(a+^2o
3%}?U{w(x+ht)m+8m)NXt>*fjHkw7+9dp;N<_DS=ET&%M%sm}Sj~o{}XlT$OXEMR0CA|0iey`H!yh2rdtOm7V*k>-bG4cz2eY9dd
i&gs!5>5(zHgTqdp`(R|VbAI#N?KTS>O}Vlu-b0|k?@}Cj2^JD@vJ)vVbq`DY!0Pb2IphV35MF;zxZf{0}CTRnCpe(^LJkgY~lr~
*M@rWhPPh!U5%0zt_y55nK^Szy{43t*1H1hC5bQ+Jv0pJWr+RDj^VK1X9Z`mn)-o)1CMF7TrKPo4kOfp**p))FpP8<N3H9#PwfH&
^k6EX2aCh|p(t|4GN|d@5ys_^;7wJE{o4TR!K9d0A1O&&E_n|TCT5WlSa&uZ_<=L`XF;q(8>~v4rD=iB#y-!s<oBDw9UI^AeDhR#
=<&dZi7p0rFt;ZB#b>`)71=Ou9QDvUbZ5cb4;CIJcYwK|P(@ZN!QYCkX6y{T=2wv~z*Z<<fUQuz0*#c4!!06-WIK0{WXpgxI_#@q
ypi;KFVQInsx6%f*9WC)(KU)4lNh@ARb;*6H$@%tOUU@<*e!lB&s<q+S$4wE3x>K5sKgc+6lCvcF4bhVj=Dfj*f+LZW+wTQ*4DZO
oVZT~n!mRA=@xMQ{$PI${n(u?y=ZO6b7#JY%XjfC08#oKfq$cHCmMP~+Yd%w<OQzx?T<sqxE^~NQk6H<;zdY8)DOIeg){NzYY<0^
U>Iv4;53rAN5|)%+S&}T0dz2nhDZpWhO|`H&S1J`UQF`_SaUr@vj)`ePkaYN^!lw;*08w|)S74{^fhQ`82J-`5<wbrDPU;s+|H2D
f_XHX#M;<d0xT_@#s1u1dgci&4e$<_(ew(d?=+ZI-KjQ=^0z;j7_V4TZX<sf<2ZX_3ciaUEC6I2PP{oGBwWm?)GkZ&BQIV|<^o4Y
Fpk(?$u7?#|CUAo&3m`d?HG9iV0go_)&;JZ6La8@v7hEFn5@kd4Qg0TLX@|1CyN+)N%dVcAI}z%nj%==Y*-h3FNW3e+aIFP5B5t#
vZ^nP>H5)|09wV6=HtloOeb*1K<#5^GKxc((sTx57xDvdh<(;F<HOSa?bw`0R2-(yA0k1x6UUzdI$j)-w+bh-$g@S0|6o{+7lzeF
7NAuWS5#OOV@<bqfi~Da{xSD=ET9wZ(Vvfzs<{QU6Y%|=2GQOLKhaypn+npYAB)Ku0!h#DEe<``ANj84MDEz1doC>4o?wg70w_dr
kwOpf52HCoHfWhb#=J7iI0q6Tw#0m*6a5l;klLY!H}Y46qbxb&LN4%^VF!^l03=j1-6EinW>q#4LDjl-c(n#O71be4>%TCbXX+ab
BU_l{lqh^PpMhu`YR(*~XcqXc11c3D0cLOt0zq@)*ozRahcFo)NW~e51E>HZ%Zs#Qjj)?e*gNDzL55J?nNy|6LoLY<ZZ*V|_UPaY
doD5VD+tbU%~-LF7@43nB%Qev++s&V$B$y|5kxG?Q!j!}LN}4#W{Y{MuexI_uMO7JGc|`=;5~xG9QyN@>13<UoOB<5`cejxf&s&|
Co|WX&mycZ#{~p2@|J>1DhC!*si1hm3IMcp(!$J288qicW4C7Q@9kF(_V#PFz1`=9iTw#!`CxDNpi<j!)UDe7!S3EcQaJX!Ar@&=
D`|7taRoqJDBkV)<4m!E?0A-P@^o{C>jshqkWI)yU5Nb%(0$T+!%fRG8(R1LT8p7XJo1Hj22#>gQ%d5wu*v}-Kq*cGO()6br9Z@l
Qk#uZIbF{7WZ{AmMO_)eGC=CZ4~cwOjYB!IcWP+{3WV8%_0$3Cz!qToW}_IzC~|*1o=t`uor%lZIjkQ<C1Tx-y`@Lm2rSVXYb1#w
7lBMYBrxBN1vSO#!YEK~<Dw*K2&Qr3tVLIkXDAnmz!w43)1n3Ggbv6#=$|$O^tv!3Yau~rs%s>?QZg2ez!Ha|Zv-zI5I@Ks7y=9l
sDAF5h}${xIq}{PQevJh3(6LJ(axJX_h5fzO}Q%m)KU`%%r8yZZw6a(Y5&|iAw1R$G&|q{YPlho_1y>gL<(PO2ckMgQk?g6-IOg>
#2@un*C{E@O*6~|OY=6%FE^7d6S~OMunhHA7bCSy==Vm3Wey?Tg@1!I(UmaV2btF2W^9UK{oJ-hZJ3O}USdX8#Sda!7!6b=ga)ac
p3Dg$lqGnRuQJ=*$XD+IB-pex(YaZ6(+P&DqZT=glFH-aliG@-Uol%j8vq+DwO@^#^*S<yUE<Du6YLAt@W?=}-za1Cx3(G1ChPcD
n?;LtWW22ji&vSBh>wyxlkkK|an`-~2<EKI2z9LRsr~-HVGZy6ra26P#lsO67>$z^V*d%ivz{0U)f~y1vSp|>1kKy?pj5n=st%WZ
5D6<ZqY*(vstG@$sv5+$o=6i4g^W!-7m`QH8o+c2Ydjb>p^`ct7;ZLkPv}HU*g?^nUq=g%L<R{AwqQ$k&n6to^bYs>O@{+#LN3e_
TK%~~WNSjt25-4_DA^Ni30zVpvqv6;WhaW9wchK26seT^tXC<6(4ejhC5ZQWATpSRc~%((L?5R+09B6MJHe11hN1(i&%|D{DfJP$
C_pJYwTB|boK1^?YwS2+7Mm`;4dE@*aMC$?HRK4Lm3Z$RGBCd1S|wPIEgEAs%Sy90h7Ecd5Iu|%MkFPV6Ol*(gfOa~${XUB2vsT_
$;OEcX{#sR5RvIC6CM^H4#j#tbk3w-=!uCbcQWOU2``lN7z|<^>Og0qt91!PTX9{MOknIlDVYn^DsNVAtV0}%!s*ITV~a_7(qnI~
<GW!rWA8Q=4i_XcpfP>KR))gM2wfek(g-~oFcmB1x9PA`9N?255*&tqde&iI40X!&PU+OxsWyFwBj3|(-QpbdL<`dlj{$1?&=G&|
^P*w~g!AHKhCt;i)Hg~_5y16)r{Da%E#GvCf(rZr$)%4S_VJWsLmyekVB+D_XnyXn&m#S^O8*S$SVeLY)kF^3AR%oy;e+DGj`_LM
9FFnv)ckzfbY0#9r1d3);iNbmzo{IG<W5OHH9JOeIN8yM6LUB=WJw(OWX8sRf^3kSZi?t!|0gpwfU%z+fy()eIq6z8D8eX8IEv4m
(&tmkxSz25G1sa8#DCO%cv5aGa)Y3pM<h@q+mN7qX}Qt_duwSV!o*QU17^O%`~jo!F=~cUb%qd$0FYeIs<N~@VeUAgT7B%BFy<ZI
ofIKi6|Tv`&V)JR7phc?x-$_Kscy*`OECDBfU4&}4JK^x62KY)EDi+BVvS%@${0XHI`p!NZ56B7MzLy8a?)tAMvZ>rZQkWK{0py?
o0k=Sx#E{=ei^_|fWMgBxg^mAg1XtcNFF~@YQKmgO32FQ$BWG*$<;r{JklXf7Exa?;eiYMRtknF9ALD~V2nv)UnWU%lVl@E)~_yj
GH-&5ntt^$O%p^#WtYxy$aSb;4iI-x4A8Y(bd08#&8f?rY8|qKUzoC!84o5b7|X^)g^euHCV;T23dAZ8BHP~$5ZP|$K&<m15Je1;
vK>sCy#>@|rKE;C5TmV%^q}<0IBPGBvnDF9O0SHt_R<Jt<#p*NW2?P3HVGu4F4S}FY?-ZX1r(&ZgtX2=N*jCy+Ge2~L=TK>NwN1S
aS9oh5~qK^vnz>FuayQy(Z4sV>9_?KiApeK^^`a_CPoz5v8pNUZD2ns(Ol<p(?R55d@6D5V6$D~*u7@A#IfDxO^GA)=9dyjIH_v*
iM3gmT~@XT=m*~2X*VPI`>A;ie}M%*72Ak~u@4$fj4SPv7tLb5{{LH)xE6D(T&}*!dW3VO>FL~r;|UALu#QnTs2pe_pzVr+3CgIj
7z64IC2s0b>A^_nPXc1pED&uep&gYIOiB;1+`}B=@2M(TmvYY^yr~K*+SaGROMOz~{M^|Y0NQp2FOOCAzghyFMvkC3`28__mSgyw
8v`~OXEZ7OGBBeeP|1#C>JP<FCaiBar7vhi121FNN@m@dUnp^niEEko#k?{4V(U5fhYKK`i675(F$AMTFVv*5VKS)lN=q2*2<ySr
>qRl(omyr~d+57!{hD91PaNo)17-6ryWzOq{DnR62Nv;&owVNZUNAHx^P%Xnz@>*_pGl$?KSZmX`ou&hoJoog)h&bJqFiC5P2-=R
yEK+$SCF%lfr5V^42zKW%GEl<WQ+bnZW*7K%tE^a{*|k>esjh%_F!f+FJ#~E4`;pme!7W>W-?gX@UIR3x&^s?ToB`f2OM0X|06X>
(d#A5(Qou$o1AmP{b!=ZJfDSL;vZ{jt&8=1JPWj1*{YQr47VeKp%V?Yi9d*F&nB3x%L0}Rq8LR04!59`ckR7QK%@7)EacC<Xg)(%
qb!u&2Ud152r=DZ1LIK5{d^HlJbhJK6AD&rt(0dhWr#}gVz9N6`C6svVxqgu*{tLiSE3R*EoE8U<jpmJJ_CJK+zwwj;A9jD$k8}o
S9j3<8sMI_1ApMj>NEL-h9eqjn9Jl7nuelArLX$qQGb}5LKR&U&0&T@&1|ytMEj`ia;zz|5Vb$Pu{z|CL8W`*dC>DInBboCJ0Z3l
^f+Z{Q&`9~>8$ayNodw?n$k7Z$?;+`sp=uf3G8H;w`?(4Y3kTDHE@N^1ZhT5cNMb05Kj<C>8cEQL%>3Aj(uS#C(aybhj{jJ>`y#$
g2B4=))HGY*zRQ3GhtTn2PQ0}m31;JhqF*8mW5|2&O###IP#XXiIWU4(*!IK*(Sz5HGw}#6JtMZ0-m!?NEASi4xxMrs^PE1DLQ4B
qCs+c@$WyB69f_XED&QEvzq8$zy%p0TMd9i7(O7YDD|JVB!jgc7`fPrF&FVNpwJI_PdqOTbDRpuW!%pg-9zI|<qi4<hIu&B_cJu!
Rt^J>d}>-OFq&g-jxj%Wor%ZMpF+V!8Ga?IUKyZnP&I3Zic;MjPS0eABRYBk8~1sh=q1%rz9h}8ZyS*_Tg*99rJ7-X7(c^g>P3<j
4Taf|3x4d04B^#HnFWCLStifg$W!<SvJycO*nOfNbOQ^7Bhd(q!vKk{W#^&iWt6U2%8>(xEIC}^&ySfG!t(gAz^yQwT%3d{8pJZ@
QX;(9S4N8arIDNGrrhUHbl8M?S!5<;nQ&pQzl1IrGw=B_bZD7(S_8;5LTiZ;T0~mIXcmf?GgWVuuNN4CMw-sbOQC0l66tdP;s}XA
PDB1(40uVia@Ws9NUadHer}p*2i0A>yf+Pd%YKR#A?Bu`aLSAQXp#aL*!GqShdVj*;GGkh0XQ}3IMS3ap({`dD5THiW2N60oGRa|
`78st09{mTw=4yc5Gf(YB;of)rW8STG&M@r$b}IAg@^qT{vL+HZAUI~C9EZq<QtX0>to1YProZ!#{a63V(gjN;t|n+)Yj(Opb8s5
Xsrrd{@puFXyI8Lp<r1=6JpH+9#D7``1gcEA9{<kBT<h`L%v=>c2!75n!>;>gEj_wpbj0yIl)3eZzlc{5YTOLYk?Ytx&ZQ=%h7{k
uv8=>dBNC`0JbiG+1?0hJ~!TM<6yZ4%9tS-^h^kq<!r)H<7ocL#ZI76tR=f>85F1P?95_qF@<T<Ql4#GfP1qH@u<i9%wq{iuP?*W
gjPXx8M2v?TT{usX@FTRhq)9%t{U|ltXk+bN~J#;3hd=houzmT6&@9=Z3q;Ll9XovlKuHj{_+%4=Z0!tr!1JXG&4b(k=v?mI+Jkh
aK{{^0j}dAJ)oV9p+8BysZ*jb-C~FlgA}G)3`zY!5b#JLi9wK77`vkEct`~y_g1c0qJPachle6GqTd?LF1-W+KBL_ZZ%tvvOZy$O
$$~#QN!x((p+Qy<f+4YwqMY~iWXoA?6=xHyOoEjuk=v^73k5R2Mr2o|Lux9YpQrVoFInl_WAzNHpqvt8N{aw{3Ccnq8TmR%G=}n-
jVv~*rg)(t9x5R%lmRN;Z$1$tDdxF*l}$o0?w+&AUFI=m5vRfi73Nmd${C_AovazOh-3&ol$9dSAuUHAR7iiVNF}#Iq*ak>Zsv{h
l9I})=s3JLvU13RCYpl*Bv&_+sm4=@W8+2QLI;Q$e+L7jgumOY9^e|Vdz7<EGUL;R0gnnm%%oZ%ewa`J=r0qC3H@a#@ZldA{DPJL
WVie_G5yipN3$PY0>ZgB;qZ?EhXnyU;U_0-<nxiwgz6%x2h8ClLP$mj2_x7R@lqKR`2<!LKk(8ppBBd91+kCODP}7Tn!(jU1iRc}
Ea}e3UwK1QIK-x5G+TNYdlr|!1$nFb1*2NSI8hO!2pJU7N&%B0Oh+&mIU)iEAYKaQibV$|8*yM6%U_GfKE=ktbYYp;nR*mRL=i=<
6UK{)2LN*>{g!wcN*_D%82YS|<FQk1?8>~*nP>AZ;PqP|Uoe;$Cw~sKGyN7wPPXl#H(1=-wg}vn+0bXim5pi&Xw*80>w>^r;akwY
c>UA`z?L$+eE~B3B>_&m=1z#gJ4}QnDhMJvL_TExR%?{~E%-N0ljq-#VM-zpZwr`8n4To;HO6=^5oG91{3-doRJ_&vai)UCP}v5w
A0J({?TgM)w|(_bqJn?{elIYHD*SG25LI%_A#+Ty1SbZXg*v5}guUVzH~1$E52L7*A*E!X^bvPg^T;Q1RngeEW$Z<QX(DInQ&5^W
8u_kI;gHBhv4|u0h9ESM_A?6scEOnx7uYj=Sc2IINUiWRHYtN)gS9Wj6as|{CI|Jyr+8b8v88x48ODxro+2vLo%mr)GujgU6d{z*
5pV9K2ZWHzJ9K!*3B~c9xsy4-gD>I;4?F=5vG^$-;lT`Xi05K^uS-20ATubA$9HH1(!HcYU2U)w^oztR(#r?5JP9HHv=OwT4m!;u
jEu&D7wkTPkvqBbTailln^8#8x}<<!+0cK`%+KPil<N({ATtg9PGC~Dzd6Ka&b{PDBXNmQ#Z(;iqZQAi7F2Y9y^&@?TEugpzL6El
H>Y-EHN}>^s8-|TB+GQmU-eVtv3FSO8;M<+Ew#o{-?2!g&+x|*Kehf3;&u^K;72SyrD0=bunly7#r(CwL<AMs3aAzk?!DC5+6<UV
9UP=yVWc|xo^N4Q{m%l^L~ocM(N=^M3}Wt&D=<d=fLRT;FR-9!0+Ou?v-a3QT1U-Yub^;S=!<13$&e$a!(^P-ld9zFNlN7gS3o@1
6EiYHQjorzK#+lMx#Mc+9($f%%M4R8gb0y)TcK7G1_=|s_?7cuC=)R@T}ef?SEIEw5ZIsuPdp`x=_~_<t-~*dM>|_qwaue<u0LEo
qiHgXTnZ)rRU$w-9vNjc-=f%~O$L1vEK)YM_oJViA<+<ITFG=|I6~x-uY~g&3RqYqk}zp6m^jg`H{3k5Btyg3xK`l$5O^5Rjd<HQ
5;gbYc^P4z!7AsC7VxeKI>RLmgWA?_Esc&=Vf;A^-h-8h)GDQgY9}q>>`P7poxH7}BIvCAm@AvDF14X5t2R&+UbMxUBIm!<qvCzB
iYV%9E25!HA{=aq-iT1zqIRwZ5oY@t#cs)YMzie<(WVsI-bSMBERFiBc3yzCS!I*!FWOo5PN%w^m62^?%Uq|_c|2Y9L%3kU;6t?{
n^^6?$*wrhASYlqJYsn=Z5t?hpC?wyK_=l!8Tu_aYjbJ`&%Ht;OhhnCL_RzDdImh(=K8j|0L!qnEgkB?_+OY;5$zyHb=LkDrv@aG
08fHJG!$pmh+@RSIxrz87>Nt=;r5w9m1QJ#U{BF<H6dn8#M~oQD{Ag;BWEV+Nvif&-3=<~ZX=VfqLW><JP11JW~Z}@gwn{+eODo<
`<(K(<vpkU?xw`Xl<hJbbGEQVH_H>-Nw~X}hP$s2@#e6_?26suS>TzmkLQroDJ7Wk)Xo7}<vDR)I+EsG#>sf520@=)q=NtSEVhql
u`}nvK@*T{k>iS|!zaNNo9EL{-N>JF9naX7&cJ@TF-ckf7Cc()vC0XV3=o%I2@rU;Jb^=}e@V}Sgme?*g(J=|Sar%d*gWA39N7#u
PdGy&ZD+iC#(Db@=bxN##v;FP$oZe2afY!<7a4ic`J+|rlpd?{d^2E6?JJNTD=OG{=#As4W`lJ&faPC7@r>u3K!Bzh`AZTU@^JLR
GimaK`!~Ov1ud|9Z>=1D(V-so3LPK^`1x9(jf-%y00lcco1lk-F}axve3RGlpdM`&C}BZ$P^0)3j6;sQmRKa)e0&)93OE#KxjCM4
G+C+EONEjK^>HZrjlW+>j|8z;+pWO=_gKABsa2)LpEy2L#i^_~%~U+7NcYB;8rXtp{tea<k2FZkNwHt(qiqd346p-EAqs-dg@#cy
@*E|Z=|m2HmB@8P{EX|HHVfze)PEwTKoj0#4hZ^ZWS_cTvF!|b2(t{D8hUf?SV*x>m7*xB^lTAVJl@VNt^>`9JfJ(u2C^14sRXnu
06bPrs#kopG9@zJ1q8>ihVU*w!x!f!7QxmleSD<$D&*<-%R~_VbTQRPi%M`dSu1yjI=)FRx#W2IbTOIx;lu}gVxN8uS<`=jtocuo
HUAxCAviXFhOB7@S@RTG^Bl6!_P}$8g+<^$Ebu&_9}Q{Ct{~40VmOgBI7YDA_=AZsH_6ead`a#Cwd`?4`Uvlxu(U8OW-d}<M`?!M
lyQYTMH}01&rnR|q=>uAh`4ld3}(?3H63w`lr;3jZWsXpz+#xLpTaGS=7Q*|x?iSP+%=jVE_uHBl}oN~4$#Gf_q=paZjtkx0_(Et
V^hTptomHnO{~Jatd|g~j@L1=VQv$?+48vVF;TwwHQ6O=kqNJ=WTz)_feRIH>Cf=y1vF(m*N;8vh0eIvV92dR7kG?j!7a8(_twbC
0g2=lx6BU}Hca%9adeS+MZnZ<ZJ(U8V(wgzyYh}4x$V|LJ?AR`Q<LJQ8$UX3xj|c~Bk$0dvrj<(UyGScfbl`7n!N;8ez!!T2UbGz
IKwiP5vkBMm|2w4Ag`?h?6b9t5r7#*^aGuFdn=B<W&9H#NHGPf*w6YWaJ~7Eu~#!n)dx_jQa^({7aYa_DC^AFklZj=7?D6#lHE|6
zK`AR`Q_h7owKj)cgZl3UNM~S5j54ZA_;ij39|0mSR3QPbv&Ltmn4$_7%c)3B`7a7ptI_u2t*$#{*MCNsyL|fn=vT8i>w*LF0#f8
Yk4f^B|!oBDI9YEOjn*X+v=qaFE`<seSv>pRpOr+;})xNq=DiGs!AwoXA|3*(jTZY%$N>9fxG~$ARs|m>a|#`G98*DD$AFFo_0f+
3ISfHtqRX50=SYs9-2u4{2wYN4O1No-www`=pGP&ps1w8_wYHnl4kefel=}YgAMY7^Y5vLH4`M0`mcT<5nOuld<K&(cdIaP%LiW3
j*eS9N5}7QeM^O*9|X$LPdjKTMiljoMM716ocNV!6zC0^0l{Fb6Bru86*8Y`ADUw6r2Pc#)`8yPj+S<T)!nh@-s7zdK@?^}Gd`sD
&)v3BeK16@MmAw<)J8h@!f=bi#Ay;CR^KMi7U@hdv9{pEMBdXKU?R=Nkc$rq^_F@V5<&3*W?GSj1_eoEQli|!SUEVD{tt2=A%(tG
MoA&D#pU_oA}gAdl^;4JBHo|fwBMO{qtD}b28-}f%OuaRh+T)3G@i*>nXJ_|sPr0Mph4*5F9rJr+i$FJ8vvVSHpuW16<HY4X)84Y
9j1d-Z)~|1tdh~MPg`#ik139|CO8k3co)%xN4atdpjYHpYZ|Wo;+mYz#`6fcGV2R->>1DZ>b?cA%B5RB*{Vj~Q+N7o&5(}g(+ycq
lP36X_86G1hg;S@$gzbx0ZjzBGQHw~y!NykJX}N$Dpqob8znWUU+A2HX)VjhX<5&i$eoVW3ikj8`VujIt33Y8jMtg&Oaod087{(H
^sy-ndRYU*)3PBT8BEIi)~5XXk0!<I!*A%g_s@*(bjv}U>Sgyx5`N$!!!vPf*wUvU)zu0_07c8e(_Np@yJ0k!cPjfX$@VGxP99WU
j;I6;rZ*CW#LIo3sZ@k?pDA~rEjLo-?)%BbT~q2HU;0gYxnn-O+|h7*Fb;SbiI;mef|q-$1~^ELSqjrxhqCZ@>9ge>TaMWBUKq%W
ZIO;B=T<8t*;#vfBa~d-sW97Mv{{I~DT8RA#=0n1;oPU_AF$20gQT&&4wa0W?NA-wOU~W1k%I?a$pMXnRe`~nX1pN>$)o4o|8fl}
Ln;(51StrB4mxpM8lIHrZ3~!W^OOLkfk>#vU>6d9Ks*<rfeRTe7&|gPFuQe!aTUJH3*!Eg`C5~=3pok5YKmJ6f>b#DWkRUp^=!bR
Jf725noL{-GI^1fgH;48$DrQI#oxx>+9J{h9~q9{##tuwDdvO^hJ(hPKKxDgnuSwDzrf&NJP4D-Lw~<NyvUsc(2?hvVqhj!RwlVq
oL>18{@rFyv0N8Wp+I=$ML48LU1)>j9|jao=0?n+>72v-*^Uy9eL?qXakU{wSX!bYv9eD{hkW6x#6FXyFrKKF*+<(_GLfA;Ck->+
C>Tj{*+by!E3qd$0_DWVsRG+YU$OVe#xnF<ob2B$f+Ula`i{l!jYEVe1Fr8yWb{fg)Q>GNL<ld#HOfe11TsJbh|I+<D^Q$-6O8xd
#2;5sB`<W_Cr5Z)q}{TwKcCx2-PY;(rQJR6UR^`_dH3k@i;bZR1wwp6G#gdlpMSix-(R-d_J@y0?=H_eN7wDkqs|opI{W*g1BLPs
+M6KSHy20UckOp}>-_xk-B}kP<biF}@BRt^D0Y2xa^B6={gBa~SmC_ewy(}M>a{*z+n>*_Pwk`D^~a-5z9aU<(RJ%I5Aq@h^WyUS
qJ4?>mVI@7dDgnN|2#kIUfY0)%kxj|zoA$8(VWs?NE5T$osRwa^c+xj)Ur>{x+m>?y*|z*ZbEVrKg3rl9^?c9GS06M*gL3xd47IP
lL)!*>`zCXk8S&trN(yj@!i>V0egct;VK0v6RyJK4P#(2@+5FYC881u5)c$&w2m;6b`?743$rtk2Bd#Wp4YQGJO<lVT-~F{&)Uon
KuG&|rI^^YwqfOsLCh}D))4zv*lMOWbTiv4CbTH&&&l^!Dc({+OR~lu!d#?Yhao|o&M5qke+Q9ws0>k*eTT~C1OaG+k&GfoCgQc6
g)SuqGO1hW)1_e2zt>WM7;<AFGZYYho{h1a8I-t8hB+oTgmLnnGt$X~-^?brH;O;srRYppMUr62e4cP#XX}zumhqIPHAPP97Q||S
gE_*FWG9|IKCUp4lYkYzCCq#75n`l)&?=WSM#c!T08I`*Z80Um<S$6q$a&;Ch9Z`Siz%!QC;|m<z{&xC?R#$>(=9wqnme-yC=k{s
RyZseMyc@aTTn2{P;WM*6BHQas25%hEXDSq&LiO5v+?FKJR<Z+#vfgy^rBe2vac_J^Q?+(?b!!e(FhXd>Z*`}I06xHetC8R!U*~E
=B#sua`;pG^7^dRzOv7|f~S$4fzQvVxsy#ONk>jvir3rS&e7$`hKxjMMxcb$xj6590g-8gz-pfeahC(zz5!r%DmJf=KtzFXYhhC7
!hZJ=1wX<&>w>H~0~siW`R?qp-NH5H*>FYYgp9mA7YmOVoD`%YMat5QG`!jb^`Z!UUN@<VD<;sCINV31g=;%VRd@p<Ua1C!^rmRa
K*5X5om`VescAeKz2+j)C?&ZpE4fLtaP{$2K$v>HLQX4GH8UAXGu)CTHN-sd&+VhXQs`SWN4lo#Yy0y2s=%<wh7O5CyuLhYwbj*L
G>U7v^Cqx<*}gcxyp~u1USJ}Qn4ZgHZ#DFxow;sop-s77W!EB_7+?>eZ`%THIl8_+I_tJC3)`c<T@+;_7}VU`axQvu>kT4@w4#5o
Mm~%5X4=(yda>55vQ;lv=u%M`;EhBCE7@$SL9bA>LfsP;b&Uqa(t#yRMy5K$sUOGwz^6-<(Y;D;l_aLyaWV4S2`CV0j9^Ej&5-V`
;n}YRb#D*dR)yB`QnRan9?ebVuFAH`qqFq_Q-vgso2}TIJ+X*AuxmDF^N>v!>~A)m@~bj*VlbP;dcn~KnyU@9m9_>;Ez%yeYYnWb
P@68azqRQUNx`EVvv1fJhPMc0DtlT-`>Ne&U$jqJ8%xTt@fd@}o3YE?(hy_FV-Z0fWBfSU2+EDRl0MWmI#8d!1+bdAkT@O|*Ub|i
s53Y)y+@p0oaV`~cp5ZMT6`>TEogR*I9>SQ(2Xjt6WWOq-WOsgp=B~h_4jybC`)dQ!x95;Jqw2RU|YU6e&Xg6#SNrz=qxv#$r=y%
s<bXWnHCmF0Hp=yq>^!~G=3_L2XyoTnFcTtyCvPhzc5at2-*4|eWQ}mIOYK+6a^Gf!YJyM=Z#tB%3PaIhJdNcZ1(xd$eg3RDhtI>
ryiNm8aia@luwGr<XXBE6jLpu<)|l6L?4Z8OlgvLQbv^$%&LlEVkG_AD4raZ*2R++P90EyA)5ZT_MVP|P^hE`2Q*vx-9m<^4JV)_
0N3JWsYBEz@xVZUdxKwG_SMZ2>K9l0>e33tzqmy`Ms$kKd|w?_*!mD^JRN>@e;7vb2I=n$6deMDp+6ewBlg8LWbrTVp#{JXD?hdj
a5OYkB+-o+N>V}s`nnAe=ScrIIB>iL)}+q?<l-f#{$#B^iXEZ}hW#fS;6j`y(M8Dx@;-^hfd@3#DSF?6BN)uz4y;})y@#I}@OB0s
tKemZ%t{||j|JbXes2C?B?Wy>KPuySMZ?4jx#1lZQ{cEO$^Z;*tEH*X3ajK`k|OJm)&LbO4}hBMpXyN3Gk{3FBB<h)9XxmV%0?#M
XzRQFoDV#laoQLX+d^@&DfD~_<xHu{%#-uw5z*ch_4Mll*iQPffrNHx#}`jSw9L#Ll3&;#EYxm1&Ydzf#P$oOpxP?#5|&}mw6*h|
PS^?yDh(>eHkjBQNC3gJ4lH$YT&kY5F!r$ge1xh1upNx3S_F*Lizr3`FF3MfAV)zO%zPw*6wz)~M?0J_)=uz)1lV!0p&=b{>TVQh
{4aiDc8*H*V&@1YIbNXm*D+5h>aQFVR)7bsAI28S`|B7O3ujl}a|3c-ufbo{)oeTg3iBxj*ukQn4q&7EO_Cb32)AAxH7D}umhWPC
!HNYdHd*DCyOkEKw8;tuN#{naINr((R<P<cyEi;4b#9u+?Q2+!x;K>Ut+wDlS=Y?Y4PxeoFypOYHi8mXr@Zb>IuTmDh?YJDKV-to
X-Fzi2Brg+?07D&qjuj6#J2dGAxVL`(_-CLb}W>pbz6lkVoV>qCCV=Xvy6xG87Kq8{BTvF1k*A$WSp!niVt#CO_>U_2ruJdj$2UP
0WG!6lXsf%?T&<SqtNk4Q*KODnlM>Lx+LM<^3G~d6W)OWA?`2Qvicx=HG+qd>U~N+z@jloPj&Bj8Z9m@Yf>Qb#*x(Jj94EmK)1(L
=br0z^V%rRcl7JxyfhED5VB?7!_rqRUYm78lt~J2AoEgcuzHQvk?ze*Qp2LC-koPjC>)cd`T^VBPtGS`P_Z`hqZnw0yel%~?A8~X
jIflLVjofjq<O*8n+PVJfCf@4>d46`S7ip*YdG2f)iM*f@u36*2@RpJJyR}ZB@<xLWmV>N5vYA0VsRyMPPy1foYF;`)V)+x)QYD&
x>Y*Oi3b<`v=g0*nra_%n(jbOH?b;#Q3WA;rc;)|*#X-(iuhHTE$GfrEUdK{oF|TNj7G5Pnkq;m70}5x#Uhp)EsjREvL<$YM-Gbj
TZi3-?Dm1hA&VcF6S1k2Wz<_oyA8G52Q3b@_yI5CojS<0B=flw74=&@a2%H62cvWw7Gdb><$==S{Xrfv7MBJ?g;K3J1!;=4MPbU`
oHQzKQbQ&d)u)bm3p1QHK`9SLz8!%m={d!(9tZ>e@SnI&$y-_g>hYr)eU74V_`M+PA^<3@Ayy!p3KFCVL{7hg^d&8Q3VE}II(v(8
G=;;AZY#<vX1B+5KGmjg8vw*jmKGgKJc3Z7VeM4051^RYCpO74+nL+f_N`|(EF0H$yV|hR7SyF*_H1NNot3S`8^Ed`?CkD~CK641
ieKpQVIb+(Uu=rxwTX%ghp2zkqml1h0@#k}%K-pC-IRaB4~ou?Y)dUF_K|cT;}R(wfuS6WHvT#`@}*n0TzzcvXD2~N$+i=;m|2N7
+Isg3wTH6y@Qo|6G7Cmv9^11>dX!T)rWhn)G-*TldkcqFuJX1j^Vu9woRqIng^Yt(aJikaGXzpLm1A+_7iRAf(38$=&PD?5)7XTs
6iz!6G@P&Xnr15DsSq_6w12>!jA8)FGt(t(Cl394Z-*2%8Ge%eZjLx2K&vfUUU~ls1t$9e*dabf7f~^D3SuJ{#0-LN=#4!3xRE!D
yeSF5a^c5wH?j~C|5Xoi)=Bj<2eR~qeLA~3J4WyD(S`l7d-neP@^AZZ^o*UoYj>~DuD{smCMFm2W&7mpynD6HjeK=>(#^P#PupiF
r`Pr+I#fxd)er3RPwh*4cmGBA@!v<6e+jAh@lwb^;X4L!8S&UTX&+x6Jp*#yecw5{wl{^Wkfc}b)-}8w+ZUaWSN7jFj8=AMe+wYx
El*w7sS{d7I7-*?_Rjo<n=<QX-17aI{I}GENY8yur!Bvh(`eMKy}gFjs5PwWUcH`tD(0m1F8AT3*S@TSxw}@Swp%-B>{bqTt^Ml0
$mu8Wx}rg=c2KQUcWd>%YPGUgsaKN%*FX6l&nE$(YFT@``@09#J!q~`OY?8kh-v^}_rN-U0W})dZaSndvczuv;9$36RqM5bN(07{
6cCqM=7w!Td27FMP_I>X0ZCSUuU4<IT<$Kk*4W+KgP#MdV%3veSXQeCdk2Ww{l;#!QQh~<%3hMaUvBIk>{n`yeHd+Zw^7G$3T&e7
0ee#|H!MOs46C-kZ`CrNG!kRlZS2+He+LJR{YIrxPltpH)3X5qUiJZr`}OLcWm%Qo-Q0jG_5E6-T8H+aTNUVfF1NY|U4==20`-09
i|larOF~mTl6ot@CG<B&Xo95`ET#jHbzmX*>Jv!#5ujKbcph%bx*mRaD*f!w^Upnf`(rk^^JoteGfbkD{XJ`MzgmZp9303}$u?<r
CZXpCb)+~z5lm)ncUOJX321V!wpWLlwRWr4!EW8!Pjc`gRs09E4MVl|cddlrEX>@6nFVSGf;~8Zxou?g8V3h}!@a$Oy?U*l$vikH
9~=PYfCcs&)!n2uNZ*HfY3x<@U^c6JjkJH*fl9qms{pkeSoMSKH?y97rfS<)o__pPU}QEXK$2a6+<d>~3X$YI<%y;$s{32zMKj&S
^kQ8t<Kva<U#x)#_R4r__+k;^2ha}bWU{<FCb*N|q`Q72Z$uMOf!psc5npgRX}v*k-Rx1Hk>gJgjE^_uWWIc*eGGhZYe;}}OEv9g
BmwBd%&tXd{~>wFeM^NlFJjjZ*JXLSDEY)MDjE2d$~mf>-f}h}msRF+8}XeMRXn+W_qDwe74;Qv>{t+b3+c`Xb|@(=y7z30V~@5t
C^|^!MXT(0Ulwe+WcT-MGGUK=m4@Z?L_P+fLK*y7F6jr#;t!UWS5W|ON|;ZX+l7<HWT?>-#aiQqU9ttstEbJGPqcAY0%|X!#tpA{
+b~Ao;}=&Npt2Q<RcYhmH?7K*y2Z)|`v%kLp5x>ZpYajul&jg_D$D$osY-()R`~WA)L~pqw8xOuIPqCH3-O~re4k+eI!0tv8x=O6
O*mf0j6rmMJQiBn<1D&|so)l)I5Svbc)_1ey`c}(M{7TqNQ%lUqxrOPH8TdhQ5a38@kGAykR>9K%gxU+Sk!niBZ&Y$n9U}TCSMIE
MKebgIV#IHgQ2jc52!?Cd^BVT2Zq|gB;5DQ^BDyk8ylfsn8$!V@ouTeSsQYr1Vc?<yF&T~{(XUe4|sp{YgbC6;+xTX0U4W0uTN)7
cvUL8%?<7L1=T3gZs!;oj_OrYZk#)h82-l#axZt=Hz9xei8uOSx2wL}HsJE+s9}2LQ~G&s`F%IK|4DwSn@!~JBTsID65n;B&tkuF
$<+Vt$KGDM&gq2@z2$Fmdd%J8^tk;7r<Xtdrppam<LB3<50Wpy)pOt6t7pFemz0sWaJ}%gI4b-o3(M)D0`l4}bvsy9mDeuBC){1=
?jr|M1Iv>4!e6~ArJsD#>4i&Ml27Dp2{nbL@LFT3z~#TAhRA!|`bji*=VbWXp9ufS_rb9z#y|LGo8ZG&zcu@7-&{m)5|h+HK02Te
@nt`knExPS=9V|3iQj8f)b<+xiCf;-#Np5As7Azr%iuBBJLt>b!Ov{}Tbx@<w<qw}Cf#gVI>zH}Z+J(XJ33BsAhq<U1#kJF{D1y^
$5*d#`!6v)qn(svag!Mv5Al)iF*A?x8Z*|x-~arpkcx$C$vn{%?Xjxl=Y7S_sf_5TI;xZ)BP@<bE;l~@_{ci{jM)XBLiPXJHxA$Z
Hai0w{~AZTL+`f0o`2OaFQ#7m!r?D{K~c(q?3cxVjqg!`jo2mgvTLYXl;tJ0$UhYZ{~3&aE&8?S-J<lq{G5q8-n(M!LmeZ9bPJ<$
EE$ypziVSh$E^@UTwYG#OLTji9+@6=gFXtPdko%^=gZ{zlFB@z?)Z0>yJX1e2Te0qR>DJr?c&dF?j}q2azQH<W<M?ZtXMUXqp!DI
`=xT#j9h-HoM1!Ah3Wh^>4NuX-`?Ezea-ZnC`omu{R3vyo^zvCI1#P<8b@w^I@JH^w?fma@3dcKtRMgL{{X$+;=}
"""
raw=zlib.decompress(base64.b85decode(''.join(DATA.split())))
assert len(raw)==34523 and sha256(raw).hexdigest()=='31386000004329eb7e10ec9b4ffcadc74043950a8fcfca9fe29fce473bd858e9'
files=json.loads(raw)
PINS={'geometry.py': [3745, '2d043e6a83af2870d05e749b2291ce2678719ddf668419336e92b20a13ef3b2a'], 'negative_anchor_certificate.py': [5079, '2c0ec1f1d4f825e7ce3cb3e4b61b950989ddeb0abaa672f7c75a54dda75518d7'], 'negative_anchor_actual_audit.py': [11506, '47f03ed60659a4e1c4781da1d21dab8be19d37845421544cbe187b6d5ee47263'], 'geom_float.py': [3630, '16125d6b2648234d8598272b37edf50a2c13c4861825fd8f03c8d6084dfa5c77'], 'negative_two_anchor_locator.py': [1264, '017332231e0cef93c1666cb62f6594f0b1bd15d5e5c2cdc50432e13db76b5bf9'], 'negative_two_anchor_locator.json': [955, 'c66aff2788c816c154d017873c23494334e0b1d43583d3a7552c3e802df2e40f'], 'try_bodies.py': [826, 'f91be37c600c84e1a00e812b494d595cc02479e963808836fc3f108d3af948ac'], 'explore_anchor.py': [1113, '5b419baab554235100d8330f510aef2316fdf0914066625a47dee94a56f8923b'], 'three_anchor_control_probe.py': [983, '472023c217f9711137118da26c747ce7a28a4683bceae1ebd531f03658e3b2c7'], 'root_corner_probe.py': [865, '5272f0544cd5efb62d1b4283578d5722fb5e75d5480f2df481bc8c2eb05cc21d'], 'corner_exact_probe.py': [1300, '46a9aa74536adcc2bfeb034db90fe3f97799f0d5f924e3960cdd9f44ae4701c0'], 'discovery_status.json': [2083, '7315deb3a50c4b96c442c358b3f7091cbace7effd6d9957255908fdc306f311c'], 'negative_anchor_certificate.json': [1147, '778f84be158f84f5c99b8dce86eacf89cea2e93e0bc1d891b1f2325d95999dfa'], 'negative_anchor_actual_audit.json': [212502, '4037bc0007f1a1eb83fcd233fc761647c958211ff404ac4f770ec28978d66e77'], 'negative_anchor_certificate_stdout.txt': [372, 'b56bf6a913f4554a6fdfd62f5d7456c480aaa3bfa8a6f8dd721765deba7c33f4'], 'negative_anchor_actual_audit_stdout.txt': [1248, 'ce5840e5b6a882cd4e4d9526e03feb8f0767a41f8d2e14fb3eb195394310e41d']}
out=Path(sys.argv[1] if len(sys.argv)==2 else 'negative_anchor_v1_recovered').resolve()
out.mkdir(parents=True,exist_ok=True)
for name,text in files.items():
 assert Path(name).name==name
 (out/name).write_bytes(text.encode('utf-8'))
for name,log in [('negative_anchor_certificate.py','negative_anchor_certificate_stdout.txt'),('negative_anchor_actual_audit.py','negative_anchor_actual_audit_stdout.txt')]:
 cmd=[sys.executable]+(['-S'] if name=='negative_anchor_actual_audit.py' else [])+[name]
 run=subprocess.run(cmd,cwd=out,capture_output=True,check=True)
 assert not run.stderr
 (out/log).write_bytes(run.stdout)
for name,(size,digest) in PINS.items():
 b=(out/name).read_bytes()
 assert len(b)==size and sha256(b).hexdigest()==digest,name
 print('EXACT_FILE_PASS',name,size,digest)
print('NEGATIVE_ANCHOR_V1_SOURCE_ONLY_COLD_RECOVERY_ALL_HASHES_PASS')
```

Supplementary convenience archive: complete exact sources, reports and discovery records (`negative_anchor_v1_recovery.zip`), 124711 bytes, SHA-256 ba036e3559143297b3c0d93ecd3cbfba5825dc6a4c528405096ef42fe1dd7aa9. The literal capsule above is sufficient without the archive.
