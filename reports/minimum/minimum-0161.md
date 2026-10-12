# minimum-0161

AI research report · 2026-09-21 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# ONE_ZERO_MULTI_NORMAL_AREA_PROFILE_COMPLETION_LOW_COVOLUME_V1

## 1. Result and exact scope

A new bounded-height non-CH class is closed:

    T(P) <= T(R) < 203/100 < 51/25.

R is one genuine convex three-dimensional body constructed from P's actual upper container and actual missing lower region. The replacement preserves EVERY ell-section's area, hence the complete ell-law, V, E and root area, and increases the n-first moment at EACH height. More generally it increases int psi(ell) Phi(n) for every nonnegative psi and nondecreasing Phi for which the integrals exist.

The upper sections can have arbitrarily many positive supporting normals, changing outer-axis ratios, and genuinely curved boundaries. No constant upper aspect, homothetic section shape, or one-plane lower surface is assumed. The lower surface can have arbitrarily many nonparallel supporting planes. The genuine restrictions are an inscribed triangle controlled by the ACTUAL section area, and a bound on the area of the root deficit. Neither restriction is declared a normalization of all bodies.

Both coefficient orderings p<q and p>=q are covered. In the latter case the D mark survives by an actual section-area budget; no equality U(d)=u is required. In particular an n-balanced choice p=q has automatic D retention. The exact balanced control below has U(d)=20/27<u=16/21.

There is also a whole proper33 missing-axis family: resolving any positive-root body of this class by the proved root contraction with 9993/10000<=lambda<1 gives T<20300/9951<51/25. These bodies still have 0<=ell<=1. For d>0 their small-positive-height sections miss the y=0 axis. This is a family theorem, not a representation of every proper33 body.

The bound on the root deficit cannot simply be omitted from the area-preservation argument. An exact high-trace pair below has a positive volume and ell-moment mismatch after the proposed triangular replacement. It does not disprove a larger trace theorem; it disproves the asserted preservation of mass in that attempted extension.

The general bounded-height non-CH core is not closed, and no E17 or mechanical minimum conclusion is changed.

## 2. Authority, complete reading and verification

The new journal and the complete coordinator material were read through EOF, including the literal required parent. Unchanged earlier evidence was retained; no historical path or source ID was treated as access to an archive.

    Current journal: 301886 bytes
    SHA256 641cc3db5aa19a41b01bae05721467f66221221c6a69bdef5e8b699863b33ccf
    Coordinator material [internal-source-reference]: 10958 bytes
    SHA256 c23e9d7f45f6fa3436daac568156befa6dd5bd7d7c8d43205a47d23601a50337

The required parent minimum-0155 was authenticated by extracting its Markdown title through EOF, retaining one final LF, and serializing the version-2 envelope with ensure_ascii=False and separators=(',',':'). It gives 37285 bytes and exactly

    0c62c07b9b3fc29f391b55135b5056c9a7f3992257a198d2c4910687f8cd8ecc.

There is no source-authority conflict.

The inherited numerical value premise is the completed whole CH theorem in minimum-0153, SHA377e6ad8854d4bde291d42a305453375447abb5c20136e2af074ded04d492714: every genuine height-one CH body with the canonical marks has T<203/100, without an aspect restriction. Its literal result and complete certificate were supplied earlier in this chat. That certificate was not re-solved here. The new replacement proves that its output actually satisfies CH; it does not transfer the conclusion to a body merely from section-area data.

The planar capacity inequality used below is compatible with the accepted projection-capacity result already recorded in shared memory. A short sufficient proof is included, so no missing capacity-source code is a dependency.

All fourteen new rational bodies were actually audited. Normal and clean-directory execution from the sole new source produced byte-identical reports and receipts. The continuous argument is analytic, not proof-assistant formalized. The variable-profile comparison bodies can be curved; their reconstruction and moments are given by exact formulas, not claimed to be rational polytopes.

## 3. The new physical class

Fix

    0<b<1, 0<=d<=1, alpha=1-b, h=1+b, q=h+d,
    u>0, p=h/u, k=min(p,q), M=max(p,q).

Use auxiliary coordinates (xi,eta,w), with the fixed inverse affine map

    x=xi/u, y=eta,
    z=[1+(d-1)x-y-w]/alpha.

Its volume multiplier is 1/(alpha u). In original physical coordinates,

    ell=w=1+(d-1)x-y-alpha z,
    n=h x+q y=p xi+q eta.

Let K be an ACTUAL compact convex body in R_+^2 x [0,1], whose root section has positive area. Define, from its actual sections,

    S=2 area(K_0),
    U(w)=sqrt(area(K_w)/area(K_0)).

Assume that for every height its actual section contains

    Delta_U(w)={xi,eta>=0: xi+eta<=U(w)}.               (I)

Thus S>=1. The entire section may extend far beyond the chord of its outer intercepts. Hypothesis (I) is an INNER triangle condition, not the CH assertion that the section lies under its outer-axis chord.

Let Bcal be a closed convex subset of R_+^2 x [0,1], upward closed in xi and eta. Its section deficits

    D_w=R_+^2 \ Bcal_w

must be bounded and contained in K_w, up to irrelevant boundary points. Put P_level=K intersect Bcal. Require its physical image P to contain the canonical tetrahedron and to have a positive-area root. Require also (0,0,w) in Bcal for b<=w<=1. The root deficit hypothesis is

    area(D_0) <= k/(2M).                              (D)

This is a real geometric area bound, not a free profile assumption. For example, p=q makes it area(D_0)<=1/2, regardless of S.

Define the reference axis factors by

    (Lx,Ly)=(1,S) when p<q,
    (Lx,Ly)=(S,1) when p>=q.                          (O)

Only in the p<q branch, impose the extra D-retention guard

    u<=U(d).                                         (G)

When p>=q no extra guard is needed. Here U(d)>0: for d<1 this follows by interpolation from K_0 to A. At d=1, the segment from (0,0,0) in K_0 to D supplies (wu,0,w); combining it with (I) gives U(w)>=wu/S for w<1, hence U(1)>=u/S>0 by endpoint continuity. The actual mark D=(u,0,d) and (I) now imply that K_d contains the triangle with vertices (0,0),(u,0),(0,U(d)). Its area is u U(d)/2, whereas area(K_d)=S U(d)^2/2. Therefore

    u<=S U(d)=Lx U(d).                               (3.1)

This is an actual containing-triangle consequence at D, not a normalization. In both branches u<=Lx U(d).

The convenient choice u=h/q gives p=q. It is a permissible coordinate choice when checking (I) and (D), NOT a guarantee that an arbitrary body satisfies them. With this choice (G) disappears, while all physical moments still use the displayed affine Jacobian.

### Direct physical-coordinate sufficient test

A particularly simple subfamily needs no scale search or D calibration. In the original level coordinates (x,y,w), let A0 be the actual xy-area of K_0 and U(w)=sqrt(area(K_w)/A0). Assume

    {x,y>=0: h x+q y<=q U(w)} subset K_w,
    area_xy(D_0)<=q/(2h), D_w subset K_w,

together with the same actual convex K/Bcal structure and marks. Then T(P)<203/100. The comparison is explicitly

    x/(2A0)+y<=U(w),
    h x+q y>=sqrt(2hq area_xy(D_w)).

This is the choice u=h/q, p=q, Lx=S. Its D retention follows from the actual triangle conv((0,0),(1,0),(0,U(d))) in K_d: A0 U(d)>=1/2, with the endpoint limit argument above when d=1. Neither the area profile nor the comparison's D intercept is assigned independently of K.

## 4. Two scalar profiles derived from common convex geometry

Convexity of K gives

    (1-theta)K_s+theta K_t subset K_((1-theta)s+theta t).

The planar Brunn-Minkowski inequality therefore makes U concave. In particular U(0)=1 and U(w)>=1-w. The classical root-of-volume concavity is the only standard input at this step.

For the lower region, intersect Bcal with the ray-height plane

    (xi,eta)=r(theta,1-theta), 0<=theta<=1.

Its radial threshold r_theta(w) is a finite nonnegative convex function of w, because the intersection is the epigraph of that threshold. Closedness, convexity and the uniform bound supplied by D_w subset K_w give endpoint continuity. The actual radial area identity is

    2 area(D_w)=int_0^1 r_theta(w)^2 dtheta.

Consequently

    f(w)=sqrt(2pq area(D_w))
        =sqrt(pq) ||r_theta(w)||_(L2[0,1])

is convex: combine pointwise convexity, monotonicity of the L2 norm on nonnegative functions and its triangle inequality. This reproduces the needed covolume argument directly; no independent interpolation of section areas is being imposed.

We have f=0 on [b,1]. By (D), f(0)<=k, hence

    0<=f(w)<=k(1-w/b)_+<=k U(w).                      (4.1)

The middle inequality is the chord inequality of the SAME convex f. The last uses U>=1-w and b<1.

## 5. Actual planar capacity, with a short proof

Let B be any convex planar body in the quadrant containing Delta={xi+eta<=1}. Suppose area(B)=S/2, S>=1. For p<=q, its n-distribution is first-order stochastically dominated by that of the triangle with axes 1,S. In particular

    int_B n <= S(p+qS)/6.                            (5.1)

To see this, use coordinates (xi,t), t=p xi+q eta. The area density g(t) is the xi-slice length divided by q. Its support is [0,L], and g is concave by the ordinary interval-section inclusion. Since B contains Delta and is contained in the quadrant,

    g(t)=t/(pq), 0<=t<=p, and g(p)=1/q.

Concavity above the broken line through (0,0),(p,1/q),(L,0) yields S/2>=L/(2q), so L<=qS. The comparison triangle has the same density up to p and then the affine density decreasing from 1/q to 0 at qS. On [p,L], the difference between the two densities is concave and starts at zero; its ratio to t-p is nonincreasing. Beyond L the difference is nonpositive. Equal total areas therefore force a single sign pattern, positive then negative. Integrating against any nondecreasing function of t proves the claimed stochastic domination and (5.1). The case p=q,S=1 is simply B=Delta; other zero-length pieces follow by continuity. Swap the coordinate roles for p>=q.

After scaling by U, this proves for every actual K_w

    int_(K_w) n <= S(k+SM) U(w)^3/6.                 (5.2)

The triangle attaining the right-hand distribution is exactly the one with axis factors (Lx,Ly) in (O). The argument does not use axis intercepts of K_w as free data and does not assert that K_w itself is a triangle.

For a measurable lower deficit of area f^2/(2pq), the opposite inequality is

    int_D n >= f^3/(3pq).                            (5.3)

Indeed {n<f} is the quadrant triangle of that area. Subtract its indicator from the indicator of D, multiply by n-f, and integrate. The integrand is nonnegative on both set differences. The same proof works for any nondecreasing function of n in place of n.

## 6. One simultaneous replacement, all marks and all true moments

There is a genuine intermediate lower-boundary replacement

    P1_level=K intersect {p xi+q eta>=f(w)}.

It is convex, and its full removed n-triangle is inside Delta_U by (4.1). Thus it has exactly P's section areas and increases every height-weighted nondecreasing function of n, by (5.3). It retains A,B,C,D by the lower-cut endpoint checks below and their original membership in K. This first reduction remains valid even when the additional p<q guard (G) fails; that guard is used only for the final upper replacement. Its physical first moments are the actual moments of K minus the explicit triangle terms appearing below.

Now define ONE simultaneous upper comparison body by

    R_level={0<=w<=1, xi,eta>=0,
             xi/Lx+eta/Ly<=U(w),
             p xi+q eta>=f(w)}.                     (R)

The upper inequality is a convex sublevel condition because U is concave. The lower inequality is a convex sublevel condition because f is convex. Thus (R) is jointly convex, including at every endpoint and every lower-profile corner.

The full lower n-triangle is inside its upper triangle: the smallest n-value at an upper axis endpoint is k U, while f<=kU. Therefore

    area(R_w)=S U(w)^2/2-f(w)^2/(2pq)
             =area(K_w)-area(D_w)
             =area(P_w).                            (6.1)

The containment D_w subset K_w is exactly what justifies the middle subtraction. There is no unrecorded outside-upper-container correction.

At EACH height, (5.2)-(5.3) give

    int_(P_w) n <= S(k+SM)U(w)^3/6-f(w)^3/(3pq)
                 =int_(R_w) n.                     (6.2)

Thus the complete ell-law is unchanged and every nonnegative height-weighted n-moment is improved. The stronger monotone-function statement in Section 1 follows from the same two set-distribution comparisons, not from fitted centroids.

All marks are retained. A and B survive because f vanishes on [b,1]. C=(0,1,0) satisfies the upper inequality since Ly>=1 and the lower one since f(0)<=k<=q. The upper D inequality is (G) or (3.1). For its lower inequality, d>=b gives f(d)=0. If 0<d<b,

    f(d)<=q(1-d/b)=h-d(1+d)/b<h=n(D).

At d=0, f(0)<=k<=p and U(0)=1; the applicable mark guard and p u=h give the same retained D directly. Alternatively f(0)<=q=h at this closed endpoint. At d=1, the lower cut is zero and the section-area argument still applies. No root rotation or interior-only variation is invoked.

The replacement has the complete upper chord in each section, because both of its outer endpoints satisfy the lower inequality. Its fixed outer aspect in physical x,y coordinates is Lx/(u Ly). Hence R is ACTUAL CH and the inherited theorem applies:

    T(P)<=T(P1)<=T(R)<203/100.

The numerical consequence comes from this actual-body bridge, not from a new independent profile relaxation.

For complete moment recovery, set A_R(w)=S U^2/2-f^2/(2pq) and

    Ixi_R(w)=S Lx U^3/6-f^3/(6p^2q),
    Ieta_R(w)=S Ly U^3/6-f^3/(6pq^2).

Then the original physical quantities are exactly

    V_R=(alpha u)^(-1) int A_R = V_P,
    E_R=(alpha u)^(-1) int w A_R = E_P,
    X_R=(alpha u^2)^(-1) int Ixi_R,
    Y_R=(alpha u)^(-1) int Ieta_R,
    Z_R=[V_R+(d-1)X_R-Y_R-E_R]/alpha,
    N_R=hX_R+qY_R >= N_P,
    g_R=(X_R,Y_R,Z_R)/V_R.

Neither X,Y,Z individually nor the actual centroid is claimed preserved. No covariance-order or equilibrium-preservation conclusion is drawn from the monotone n-moment comparisons.

Equality in T(P)<=T(R) requires, at almost every nondegenerate height, the upper n-slice density to equal the comparison density and D_w to equal {n<f(w)} up to area-zero sets. No equality at 51/25 occurs; every body in the class has a gap greater than 1/100 from that threshold. The sharp supremum inside this new class is not identified. Degenerating sequences have limsup T<=203/100, without declaring a singular b=1 coordinate chart a three-dimensional successor.

## 7. Genuine variable aspect, and a proper missing-axis consequence

Here is a reconstruction of a whole variable-shape subfamily, not just sampled sections. Set S=(1+e)^2>1 and take K in (xi,eta,w) to be the hull of

    (0,0,0),(S,0,0),(0,1,0),
    (0,0,d),(1,0,d),(0,1,d),(0,0,1),

with (1-d)S<=1. For 0<=w<=d let lambda=w/d. Its section is the actual Minkowski interpolation of the root triangle and Delta. The nonzero upper vertices are

    (S(1-lambda)+lambda,0),
    (S(1-lambda),lambda), (0,1).

Thus

    2 area(K_w)=S-(S-1)(w/d)^2,
    U(w)=sqrt(1-(1-1/S)(w/d)^2), 0<=w<=d,
    U(w)=S^(-1/2)(1-w)/(1-d), d<=w<=1.              (7.1)

For 0<w<d, there are two distinct positive upper normals (1,1) and (1,S); the outer axis ratio changes. The section extends above the chord of its outer axis intercepts. Since U<=1 below d and the actual section contains Delta, (I) holds. Above d, (I) follows from U being S^(-1/2) times the actual triangular radius.

Choose physical scale u, retain the original four marks, and remove the genuine lower triangle n<m(1-w/b), where m=rho min(p,q), 0<rho<1. This is a single physical lower plane. The parameter inequalities in the capsule prove complete deficit containment. The principal example has

    b=3/5, d=1/2000, e=1/10000,
    u=10000/10001=U(d), rho=31/32.

It is 8/13/7, own strict446/weak000, with coordinate maximal faces 5/5 and

    T=265967818382122176510961506531840000
      /132311685827752195442987656770515467
      approximately 2.010161209255304.

At w=1/4000 its actual section exceeds the outer-axis chord by exactly 20001/400040002. This is not CH.

The comparison body for (7.1) is generally curved, but is fully recoverable from (R). For m as above, its integrals can be recovered without numerical geometry. Write v=S^(-1/2), c=1-v^2. Then

    int U^2=(v^2+2d)/3,
    int wU^2=[3d^2+v^2(1+2d)]/12,
    int U^3=d[v(3+2v^2)/8+3 asin(sqrt(c))/(8sqrt(c))]
             +v^3(1-d)/4,
    int f^2=bm^2/3, int wf^2=b^2m^2/12, int f^3=bm^3/4.

Use the continuous c=0 limit when needed. These exact formulas and Section 6 give every physical moment of that new curved body. Its convexity and trace domination are analytically verified; the code does not pretend to re-hull a curved surface as a finite rational polytope.

For any positive-root P in the theorem, choose q0 in the relative interior of its root with positive x,y. The actual body

    P_lambda=conv(T0,lambda P+(1-lambda)q0)

has exactly the two maximal coordinate triangles ABC and ABD. It lies in P and retains maxell=1. The SAME-body estimates are

    V_lambda>=lambda^3 V, E_lambda>=lambda^4 E, N_lambda<=N,
    T(P_lambda)<=lambda^(-7)T(P).

Hence 9993/10000<=lambda<1 gives T<20300/9951<51/25, with gap1/248775. No monotonicity of properization was assumed.

The principal example is actually properized at lambda=9999/10000 using the exact root vertex mean

    q0=(1969146905001/4000000000000,630131/1280400,0)

in level coordinates. The result is 9/20/13, own strict446/weak000, genuine proper33, and

    T=116067670379084965689165035681849442424791817966708480000000000000000
      /57740387611222739422745999455415060634399800291351395743461835464477
      approximately 2.0101643785384877.

Properization INCREASES trace here. Its section at w=1/4000 has strictly positive minimum y, equal to 630131/25608000000. More generally every proper body of this family with d>0 misses y=0 at 0<w<min(b,d), because the retained ABD triangle has no point at those heights. The value conclusion covers the whole stated proper-resolution family, not every missing-axis body.

## 8. Exact paired replacements, nonplanar lower data and failed high-deficit extension

Fourteen rational bodies, including the proper body, are reconstructed in the capsule. All have a true positive-area root, maxell=1, and no zero edge primitive. Their mechanics use the original physical Euclidean metric at each body's own newly integrated centroid.

### Exact area-preserving non-CH to CH pair above 2

Take b=3/5,d=1/2000,u=1,m=(1+b)31/32 and U equal to1 up to d, then (1-w)/(1-d). The source upper sections are U times the quadrilateral

    (0,0),(1,0),(1001/2000,1001/2000),(0,1).

Their area is (1001/1000)U^2/2. The reference replaces that quadrilateral by the triangle with axes1,1001/1000; both retain the SAME lower n-cut.

The actual source is10/16/8, strict558/weak000. The reference is8/12/6, strict446/weak000. Their complete ell-law agrees, including

    V=468510067/2560800000,
    E=2835043472201/40972800000000.

Their n-moments differ by exactly

    N_R-N_P=2005003/76800000000000>0,

and their traces are

    T(P)=2668780731415876653400/1328246407108803147467,
    T(R)=2668781187950648746800/1328246407108803147467.

The trace gain is456534772093400/1328246407108803147467. Both exceed2. The own COM changes, and so do the maximal-face lattice and strict equilibrium counts.

A larger nonwinning pair uses the same b,d,u,m but the root quadrilateral (0,0),(4,0),(3,3/4),(0,1), with S=6, and reference axes1,6. It verifies the construction far from a small-area perturbation: source10/16/8 strict424, reference8/12/6 strict323, both weak000. Their traces are respectively53143513948200500/70251239984040531 and59724045375922400/70251239984040531. The theorem has no bound on S.

### Opposite coefficient ordering and automatic D retention

The reverse-order rational pair uses b=3/5,d=3/4,u=1/2, S=1001/1000, m=min(p,q)31/32 and the same small quadrilateral. U joins (0,1),(d,u),(1,0). Here p>q and the comparison triangle has axes S,1. The source/reference f-vectors are10/16/8 and8/12/6; both have own strict558/weak000. Their traces are2049271525899264/2428993927417975 and2049476727503872/2428993927417975.

A separate changing-aspect control uses b=3/5,d=1/2,e=7/20,u=20/27 and rho=31/32. It has p>q and f8/13/7, own457/weak000. Replacing only its physical scale by u=16/21 makes p=q, still has f8/13/7 and own457/weak000, and gives T=82580888576/112129116575. In the latter body U(d)=20/27<u=16/21, so imposing U(d)=u would genuinely omit an eligible body. D is retained by (3.1).

### A genuinely nontriangular deficit

Use the variable-upper body with b=3/5,d=1/200,e=1/1000,u=1000/1001. Let r=41/50 and c=16/41. The lower Bcal is defined by BOTH inequalities

    c xi+(r-c)eta+(rc/b)w>=rc,
    (r-c)xi+c eta+(rc/b)w>=rc.

Its missing root region is the simple concave polygon

    (0,0),(r,0),(c,c),(0,r),

of area8/25. It scales by (1-w/b)_+. It is inside the actual K at every height, and 2pq(8/25)<=min(p,q)^2. The resulting actual body is9/15/8, own446/weak000, with T=21268077719763721292800/11446739335525678773589. This checks the general lower-region argument, not only a one-plane special case. The source explicitly restores all V,X,Y,Z,E,N of the same missing region.

### The failed removal of the root-deficit guard

Take

    b=7/10, d=1/10000, u=501/500,
    p=(1+b)/u, q=1+b+d,
    m=p+(q-p)/1000=2833339167/1670000000,
    S=1+2(m/p-1)=4250017501/4250000000.

Let U join (0,1),(d,u),(1,0). Use upper sections with axes S U,U and lower plane n>=m(1-w/b). The complete removed n-triangle is inside that source upper triangle because m<pS and m<q. The source is a genuine8/12/6 body with

    T=70769546896128654621299138192602870283599500000
      /35382434651157926497472278652477490567267514229>2.

Now exchange the upper axes to U,S U, as the capacity comparison suggests, but keep the same lower cut. Since m>p, the lower triangle is no longer inside the new upper triangle near the root. Both bodies retain all canonical marks and are actual8/12/6, own446/weak000. Nevertheless

    V_R-V_P=1301716614543802501
              /11891312519528120204194758000000000>0,
    E_R-E_P=159469397297917612990007
              /60645702173987829211858533544498390320000000000>0.

The seam is w*=122507/1275000175010. With kappa=m/b+p(u-1)/d, the exact same exterior triangular piece gives

    Delta V=S(m-p)^3/[6 alpha u p(qS-p) kappa],
    Delta E=(w*/4) Delta V.

These identities are independently checked against the two original uniform-volume integrations. The reference's trace is slightly larger in this example; there is NO claimed counterexample to trace domination or51/25. It is an exact counterexample to extending the area-preserving proof without its low-deficit hypothesis. It identifies the precise extra region that would have to be accounted for, rather than assigning new section areas by hand.

## 9. Complete exact recovery capsule

Save the following complete source as area_core.py, UTF-8/LF with one final LF, and run with assertions enabled:

    python -S area_core.py > area_core_receipt.txt

Tested: CPython3.13.5, standard library only, no external inputs, seeds or numerical hull library. The final source was run normally and from a clean directory containing only that source. The exact report and receipt matched byte for byte.

    area_core.py: 16740 bytes
    SHA256 a6ba980e3417d322eee9c71268634c389324cb53f4cb358b1dfc1bd4e7e6d5e2
    area_core.json: 121284 bytes
    SHA256 e6b5d18ffe8dfe0512679d269bbf4d587fc5919a9f7b82d98da4aa21c9d2908f
    area_core_receipt.txt: 1760 bytes
    SHA256 36c106bc6819b9be3c34d3562acada3e1b7d500bdd6f9848a84de6e5d3d53748

Expected final marker:

    ONE_ZERO_VARIABLE_UPPER_AREA_COMPLETION_EXACT_PASS

The report reconstructs every vertex, maximal facet, supporting plane, true edge and all four primitives, each body's own V,X,Y,Z,E,N and COM, the full missing-region restorations, the properization data, and the exact high-deficit mismatch. Three true volume fans agree with a fourth independent exact section integration. The continuous theorem is proved above; finite sampling is not used as a proof for arbitrary K or Bcal.

```python
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import json

# CPython 3.13.5, standard library only, assertions enabled, no external inputs.
PARENT='minimum-0155'
PARENT_SHA256='0c62c07b9b3fc29f391b55135b5056c9a7f3992257a198d2c4910687f8cd8ecc'
KEYS=('V','X','Y','Z','E','N')

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
    assert all(s-dot(n,g)>0 for n,s in planes)
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
    pv=[[] for p in P]; pf=[[] for f in faces]; saddles=[]; weak=[]; zero=0; packets=[]
    for edge,(f,h) in sorted(edges.items()):
        i,j=edge
        a=dot(X[i],sub(X[j],X[i])); bb=dot(X[j],sub(X[i],X[j]))
        c=dot(Q[f],sub(Q[h],Q[f])); dd=dot(Q[h],sub(Q[f],Q[h]))
        vals=[a,bb,c,dd]; zero+=sum(v==0 for v in vals)
        packets.append(dict(edge=edge,facets=[f,h],primitives=vals))
        pv[i].append(a); pv[j].append(bb); pf[f].append(c); pf[h].append(dd)
        if all(v<0 for v in vals): saddles.append(edge)
        if all(v<=0 for v in vals) and any(v==0 for v in vals): weak.append(edge)
    S=[i for i,v in enumerate(pf) if all(x<0 for x in v)]
    U=[i for i,v in enumerate(pv) if all(x<0 for x in v)]
    if zero==0: assert len(S)+len(U)-len(saddles)==2
    # Weak edge-packets are reported, not silently equated with physical-point counts.
    return dict(vertices=P,facets=faces,edges=sorted(edges),planes=planes,
                f_vector=[len(P),len(edges),len(faces)],V=V,X=J[0],Y=J[1],Z=J[2],
                E=E,N=N,T=T,centroid=g,root=root,coordinate_faces=coord,
                strict_SUH=[len(S),len(U),len(saddles)],stable=S,unstable=U,
                saddle_edges=saddles,weak_edge_packets=weak,zero_primitives=zero,packets=packets,
                maxell=max(map(ell,P)),proper33=proper)


def anchors(b,d):
    return [ratrow(r) for r in [(0,0,1),(0,0,b),(0,1,0),(1,0,d)]]

def poly2(poly):
    # Works for an oriented simple polygon, including the concave deficit polygon.
    a=ix=iy=F(0)
    for p,q in zip(poly,poly[1:]+poly[:1]):
        c=p[0]*q[1]-p[1]*q[0]
        a+=c;ix+=(p[0]+q[0])*c;iy+=(p[1]+q[1])*c
    assert a>=0
    return a/2,ix/6,iy/6

def sections(K,w):
    P,faces,planes,edges=hull(K)
    pts=set(p for p in P if p[2]==w)
    for i,j in edges:
        p,q=P[i],P[j]
        if (p[2]-w)*(q[2]-w)<0:
            pts.add(add(p,mul((w-p[2])/(q[2]-p[2]),sub(q,p))))
    pts=sorted(pts)
    if len(pts)>=3:
        cc=cycle(pts,range(len(pts)),(0,0,1));pts=[pts[i] for i in cc]
    a,ix,iy=poly2(pts)
    return dict(vertices=pts,area=a,Ix=ix,Iy=iy)

def section_mass(K,b,d):
    # Between consecutive true vertex heights, all section vertices are affine.
    # Area has degree <=2 and its first moments degree <=3. Exact 3/8 integration.
    P=hull(K)[0];cuts=sorted(set(p[2] for p in P));I=[F(0)]*4
    for l,r in zip(cuts[:-1],cuts[1:]):
        for j,weight in enumerate([1,3,3,1]):
            w=l+(r-l)*F(j,3);s=sections(P,w)
            for k,value in enumerate([s['area'],w*s['area'],s['Ix'],s['Iy']]):
                I[k]+=(r-l)*weight*value/8
    V,E,X,Y=[x/(1-b) for x in I]
    Z=(V+(d-1)*X-Y-E)/(1-b);N=(1+b)*X+(1+b+d)*Y
    return dict(V=V,X=X,Y=Y,Z=Z,E=E,N=N)

def mass(K,b,d):
    P,faces,planes,edges=hull([world(p,b,d) for p in K])
    V,J=moments(P,faces,average(P))
    for o in [P[0],P[-1]]:assert moments(P,faces,o)==(V,J)
    X,Y,Z=J;E=V+(d-1)*X-Y-(1-b)*Z;N=(1+b)*X+(1+b+d)*Y
    out=dict(V=V,X=X,Y=Y,Z=Z,E=E,N=N)
    assert out==section_mass(K,b,d)
    return out

def full_audit(K,b,d,proper=False):
    out=audit(K,b,d,proper)
    check=section_mass(K,b,d)
    assert all(out[k]==check[k] for k in KEYS)
    assert out['zero_primitives']==0 and not out['weak_edge_packets']
    return out

def clipped(K,cuts):
    P,faces,planes,edges=hull(K)
    return from_halfspaces(planes+[(ratrow(n),F(s)) for n,s in cuts])

def deficit_mass(poly,b,d,u):
    A,Ix,Iy=poly2(poly);alpha=1-b
    V=b*A/(3*alpha*u);E=b*b*A/(12*alpha*u)
    X=b*Ix/(4*alpha*u*u);Y=b*Iy/(4*alpha*u)
    Z=(V+(d-1)*X-Y-E)/alpha;N=(1+b)*X+(1+b+d)*Y
    return dict(V=V,X=X,Y=Y,Z=Z,E=E,N=N,root_area=A,
                root_Ixi=Ix,root_Ieta=Iy)

def positive_normals(section,u):
    pts=[(u*p[0],p[1]) for p in section['vertices']]
    found=set()
    for p,q in zip(pts,pts[1:]+pts[:1]):
        nx=q[1]-p[1];ny=p[0]-q[0]
        if nx>0 and ny>0:found.add((F(1),ny/nx))
    return sorted(found)

def properize(K,b,d):
    root=[p for p in hull(K)[0] if p[2]==0];c=average(root)
    assert c[0]>0 and c[1]>0 and c[2]==0
    lam=F(9999,10000)
    KP=anchors(b,d)+[add(mul(lam,p),mul(1-lam,c)) for p in K]
    old=full_audit(K,b,d);a=full_audit(KP,b,d,True)
    assert a['V']>=lam**3*old['V'] and a['E']>=lam**4*old['E']
    assert a['N']<=old['N'] and a['T']<=old['T']/lam**7<F(51,25)
    sec=sections(KP,min(b,d)/2)
    assert sec['area']>0 and min(p[1] for p in sec['vertices'])>0
    return dict(lambda_value=lam,root_center=c,body=a,missing_y_axis_section=sec)

def variable_shape(b,d,e,rho,nontriangular=False,proper=False,scale=None):
    S=(1+e)**2;v=1/(1+e);u=v if scale is None else scale
    h=1+b;q=h+d;p=h/u;m=min(p,q)*rho
    assert 0<b<1 and 0<d<1 and e>0 and 0<rho<1
    assert (1-d)*S<=1 and m<min(p,q) and 0<u<=1
    ref_ax=S if p>=q else F(1)
    assert u<=ref_ax*v
    # Actual K: Minkowski interpolation of two triangles of different aspect.
    K=[ratrow(v) for v in [(0,0,0),(S/u,0,0),(0,1,0),
                           (0,0,d),(1/u,0,d),(0,1,d),(0,0,1)]]
    if nontriangular:
        r=F(41,50);c=F(16,41);k=r*c
        cuts=[((-c*u,-(r-c),-k/b),-k),((-(r-c)*u,-c,-k/b),-k)]
        poly=[(F(0),F(0)),(r,F(0)),(c,c),(F(0),r)]
    else:
        cuts=[((-h,-q,-m/b),-m)]
        poly=[(F(0),F(0)),(m/p,F(0)),(F(0),m/q)]
    assert sorted(set(v[2] for v in hull(K)[0]))==[F(0),d,F(1)]
    P=clipped(K,cuts);a=full_audit(P,b,d);outer=mass(K,b,d)
    removed=deficit_mass(poly,b,d,u)
    assert 2*p*q*removed['root_area']<=min(p,q)**2
    for k in KEYS:assert outer[k]-a[k]==removed[k]
    # Exact area formula on every knot and midpoint; analytic formula in handoff.
    area_checks=[]
    for w in [F(0),d/3,d/2,d,(1+d)/2,F(1)]:
        sec=sections(K,w);actual=u*sec['area']
        expected=(S-(S-1)*(w/d)**2)/2 if w<=d else ((1-w)/(1-d))**2/2
        assert actual==expected
        area_checks.append([w,actual])
    I2=(v*v+2*d)/3;Iw2=(3*d*d+v*v*(1+2*d))/12
    assert outer['V']==S*I2/(2*(1-b)*u)
    assert outer['E']==S*Iw2/(2*(1-b)*u)
    witness=sections(P,d/2);normals=positive_normals(witness,u)
    assert len(normals)==2 and a['T']<F(203,100)
    assert normals==[(F(1),F(1)),(F(1),S)]
    # Both outer intercepts are present; an actual middle vertex lies ABOVE their chord.
    xx=max(v[0] for v in witness['vertices'] if v[1]==0)
    yy=max(v[1] for v in witness['vertices'] if v[0]==0)
    excess=max(v[0]/xx+v[1]/yy-1 for v in witness['vertices'])
    assert excess>0
    out=dict(inputs=dict(b=b,d=d,e=e,rho=rho,S=S,u=u,U_at_d=v,p=p,q=q,m=m,
                         reference_x_axis_factor=ref_ax,
                         outer_level_generators=K,lower_halfspaces=cuts,root_deficit=poly),
             body=a,outer_moments=outer,removed_moments=removed,
             area_formula_checks=area_checks,I2=I2,IwU2=Iw2,section=witness,positive_upper_normals=normals,
             chord_excess=excess)
    if proper:out['proper']=properize(P,b,d)
    return out

def homothetic_pair(big=False,reverse=False):
    b=F(3,5);d=F(1,2000);u=F(1)
    if reverse:d=F(3,4);u=F(1,2)
    h=1+b;q=h+d;p=h/u
    S=F(1001,1000);v=S/2;m=min(p,q)*F(31,32)
    B=[(F(0),F(0)),(F(1),F(0)),(v,v),(F(0),F(1))]
    if big:
        S=F(6);B=[(F(0),F(0)),(F(4),F(0)),(F(3),F(3,4)),(F(0),F(1))]
    ax,ay=(S,F(1)) if p>=q else (F(1),S)
    BR=[(F(0),F(0)),(ax,F(0)),(F(0),ay)]
    def build(base):
        return [(scale*r[0]/u,scale*r[1],w) for w,scale in [(F(0),F(1)),(d,u)]
                for r in base]+[(F(0),F(0),F(1))]
    K=build(B);KR=build(BR);cut=[((-h,-q,-m/b),-m)]
    P=clipped(K,cut);R=clipped(KR,cut)
    a=full_audit(P,b,d);ar=full_audit(R,b,d)
    assert a['V']==ar['V'] and a['E']==ar['E'] and a['N']<ar['N']
    assert a['centroid']!=ar['centroid'] and 0<a['T']<ar['T']<F(203,100)
    if not big and not reverse:assert a['T']>2
    poly=[(F(0),F(0)),(m/p,F(0)),(F(0),m/q)]
    rem=deficit_mass(poly,b,d,u)
    for outer,body in [(K,a),(KR,ar)]:
        mm=mass(outer,b,d)
        for k in KEYS:assert mm[k]-body[k]==rem[k]
    # Exact full ell-law equality: both upper areas are S U(w)^2/2 and the
    # SAME full lower n-triangle is removed at every height.
    assert poly2(B)[0]==poly2(BR)[0]==S/2 and m<=min(p,q)
    ndiff=ar['N']-a['N']
    rootdiff=p*(poly2(BR)[1]-poly2(B)[1])+q*(poly2(BR)[2]-poly2(B)[2])
    # U joins (0,1),(d,u),(1,0); integrate its cubic exactly.
    I3=(d*(1+u+u*u)+u**3)/4
    assert ndiff==rootdiff*I3/((1-b)*u)>0
    return dict(inputs=dict(b=b,d=d,u=u,S=S,m=m,source_base=B,reference_base=BR),
                source=a,reference=ar,removed_moments=rem,N_gain=ndiff,
                trace_gain=ar['T']-a['T'])

def high_deficit_failure():
    b=F(7,10);d=F(1,10000);u=F(501,500);h=1+b;q=h+d;p=h/u
    m=p+(q-p)/1000;S=1+2*(m/p-1)
    def halfspaces(swap):
        cx,cy=(u,1/S) if swap else (u/S,F(1))
        H=[((-1,0,0),0),((0,-1,0),0),((0,0,-1),0),((0,0,1),1),
           ((cx,cy,(1-u)/d),1),((cx*(1-d),cy*(1-d),u),u),
           ((-h,-q,-m/b),-m)]
        return [(ratrow(n),F(s)) for n,s in H]
    HS,HR=halfspaces(False),halfspaces(True)
    K,R=from_halfspaces(HS),from_halfspaces(HR)
    a=full_audit(K,b,d);ar=full_audit(R,b,d)
    assert p<m<q and m<p*S and 2<a['T']<ar['T']<F(203,100)
    slope=m/b+p*(u-1)/d;wstar=(m-p)/slope
    assert 0<wstar<min(b,d)
    dv=S*(m-p)**3/(6*(1-b)*u*p*(q*S-p)*slope)
    assert ar['V']-a['V']==dv>0 and ar['E']-a['E']==dv*wstar/4>0
    return dict(inputs=dict(b=b,d=d,u=u,p=p,q=q,m=m,S=S,
                            source_halfspaces=HS,reference_halfspaces=HR),
                source=a,reference=ar,high_switch=wstar,
                V_mismatch=dv,E_mismatch=dv*wstar/4,
                trace_difference=ar['T']-a['T'])

def serial(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:serial(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [serial(v) for v in x]
    return x

def main():
    assert __debug__
    a=variable_shape(F(3,5),F(1,2000),F(1,10000),F(31,32),proper=True)
    c=variable_shape(F(1,5),F(1,10),F(1,50),F(4,5))
    low=variable_shape(F(3,5),F(1,200),F(1,1000),F(31,32),nontriangular=True)
    report=dict(parent=PARENT,parent_sha256=PARENT_SHA256,variable=a,
                larger_shape=c,nontriangular_deficit=low,exact_pair=homothetic_pair(),
                large_area_pair=homothetic_pair(True),reverse_pair=homothetic_pair(reverse=True),
                reversed_variable=variable_shape(F(3,5),F(1,2),F(7,20),F(31,32)),
                balanced_uncalibrated=variable_shape(F(3,5),F(1,2),F(7,20),F(31,32),scale=F(16,21)),
                high_deficit_failure=high_deficit_failure())
    data=(json.dumps(serial(report),sort_keys=True,separators=(',',':'))+'\n').encode()
    Path('area_core.json').write_bytes(data)
    for name,obj in [('VARIABLE',a['body']),('PROPER',a['proper']['body']),
                     ('LARGER_SHAPE',c['body']),('NONTRIANGULAR_DEFICIT',low['body']),
                     ('SOURCE',report['exact_pair']['source']),('REFERENCE',report['exact_pair']['reference']),
                     ('LARGE_SOURCE',report['large_area_pair']['source']),
                     ('LARGE_REFERENCE',report['large_area_pair']['reference']),
                     ('REVERSED_VARIABLE',report['reversed_variable']['body']),
                     ('BALANCED_UNCALIBRATED',report['balanced_uncalibrated']['body']),
                     ('REVERSE_SOURCE',report['reverse_pair']['source']),
                     ('REVERSE_REFERENCE',report['reverse_pair']['reference']),
                     ('HIGH_SOURCE',report['high_deficit_failure']['source']),
                     ('HIGH_REFERENCE',report['high_deficit_failure']['reference'])]:
        print(name,*obj['f_vector'],'T',obj['T'],'SUH',*obj['strict_SUH'],'ZERO',obj['zero_primitives'])
    print('THREE_VOLUME_FANS_AND_INDEPENDENT_EXACT_SECTION_INTEGRATION_PASS')
    print('SAME_DEFICIT_VXYZEN_RESTORATIONS_AND_VARIABLE_UPPER_SHAPES_PASS')
    print('EXACT_EQUAL_ELL_LAW_TRACE_DOMINATION_AND_HIGH_COVOLUME_FAILURE_PASS')
    print('REPORT',len(data),hashlib.sha256(data).hexdigest())
    print('ONE_ZERO_VARIABLE_UPPER_AREA_COMPLETION_EXACT_PASS')

if __name__=='__main__':main()
```

## 10. Precise continuation

The supplied five-halfspace section envelope remains only a necessary containing-tetrahedron region; it was not used as a realizable section or a body substitute. The successful mechanism here instead couples a real upper body's area concavity to a real upward lower boundary's covolume convexity, applies planar capacity before subtracting the SAME missing region, and proves canonical retention for the resulting simultaneous three-dimensional replacement.

The full new sector consists of actual K/Bcal decompositions satisfying (I),(D), deficit containment, the original marks, and the stated p<q guard. The p>=q branch and the n-balanced branch need no extra D calibration. There is no constant-aspect condition on the input and no upper bound on S. It includes the whole proper-resolution family described above, but not arbitrary proper33 cores.

Even without (G), the exact lower replacement P1 is retained as a valid canonical trace-dominating reduction under the other hypotheses. Its upper multi-normal geometry remains genuine, not freely chosen.

The important remaining complements are: deficits extending outside the chosen actual upper container; root deficits larger than (D); and upper sections lacking the required area-normalized inner triangle. General proper33 bodies with an absent axis near the root commonly fall outside the full-deficit-containment hypothesis, so they cannot be silently included. The high-deficit exact pair shows that even within an otherwise compatible upper family, an outside-upper-cut correction is real and changes both V and E.

A useful next step is to control that outside-upper-cut region jointly in V,E,N while retaining the new actual upper-capacity inequality. The present construction does not license an unconditional corner deletion, and the failed equality-of-areas extension is preserved for that continuation. The parent overshoot theorem can already be applied after a height-one core satisfying this theorem is identified; no new claim is needed about high caps. The d>1 marked range remains separate.

No whole E17 exclusion, universal bounded-core51/25 theorem, equilibrium-preserving map, new110 body or improved complexity endpoint follows. The accepted mechanical interval remains34..622. The continuous reconstruction formulas and all exact nonwinning controls are durable in this handoff.

Convenience copies, not dependencies: source (`area_core.py`), full exact report (`area_core.json`), matched execution receipt (`area_core_receipt.txt`).
