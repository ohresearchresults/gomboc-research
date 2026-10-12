# material-29b81610f3ea

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# TWO_ANCHOR_FIBRE_GREEDY_DOMINANCE_V1

## Status and scope
This is a proved actual-body reduction for the original adjacent-triangle trace, together with an executed exact rational nonrecord control. It does NOT prove the proposed universal trace threshold 51/25, an E17 exclusion, or a smaller own110 attainer. The preserved bounds remain 34<=Cmin<=622.

The theorem solves the vertical-placement freedom of a two-anchor polyhedron for FIXED actual projected body K and actual projected root facet R. It does not replace these polygons with prescribed moments. Convexity of both boundary gauges is retained. The original uniformly filled body's volume moments, including its changing actual vertical centroid, are integrated throughout.

Two-anchor geometry is known to hold at a positive-endpoint joint all-auxiliary marked maximum with G(C),G(D)>=0; the prior proof is [internal-source-reference], with exact-source erratum [internal-source-reference]. The general one-mark facet rigidity used to obtain that sector is [internal-source-reference]. The theorem below assumes the geometric two-anchor representation explicitly and is self-contained after that assumption. It also applies to many nonstationary bodies.

## 1. Coordinates, original functional, and admissible gauges
Let A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0), and T0=conv(A,B,C,D). Fix a>b>0 and c,d>0. Write

alpha=a-b, H=a/alpha>1,
l0(x,y)=((a-d)x+(a-c)y)/alpha,
ell(x,y,z)=alpha(H-l0(x,y)-z),
n(x,y)=(a+b+c)x+(a+b+d)y.

Let hA,hB be finite convex positively homogeneous piecewise linear functions on the nonnegative quadrant. The actual body is

P={x,y>=0: hA(x,y)<=z<=min(1-hB(x,y), H-l0(x,y))}.

Assume P is bounded, three-dimensional, contains T0, and its root ell=0 is a genuine positive-area facet. The lower noncoordinate facets pass through A and the nonroot upper facets through B. Coordinate facets may initially be marked supporting patches; genuine maximal coordinate triangles are specified separately below.

Define original Lebesgue integrals V=int_P1, X=int_Px, Y=int_Py, Z=int_Pz, Eell=int_Pell, N=int_Pn. The original trace is T=N/(6 V Eell). Here Eell is an integral, not the number of physical edges. The actual centroid is (X,Y,Z)/V. All denominators are positive.

Put j=hA+l0 and k=hA+hB. Both j and k-j are convex homogeneous piecewise linear; conversely this pair of convexity conditions reconstructs convex hA=j-l0 and hB=k-j+l0.

Let ei be either quadrant unit vector. T0 containment is equivalent to hA(ei)<=0 and hB(ei)<=1, or

k(ei)+l0(ei)-1 <= j(ei) <= l0(ei).

Indeed the four canonical points then satisfy every halfspace, hence so does their convex hull. The values ell(A),ell(B),ell(C),ell(D) are a,b,c,d by construction.

If hA(ei)=0 and hB(ei)=1 on BOTH axes, then the coordinate supports are exactly the maximal triangles ABC and ABD: on an axis of radius s the lower graph is z=0 and the nonroot upper is z=1-s. The root is inactive on this triangle since all three canonical endpoint values of ell are positive. Conversely these exact coordinate triangles force those gauge equalities. In j,k notation this proper33 condition is k(ei)=1 and j(ei)=l0(ei).

## 2. Actual projected polygons and exact fibre reconstruction
The vertical length is

L(x,y)=max(0,min(1-k(x,y),H-j(x,y))).

The actual projected body and root are

K={x,y>=0: k<=1, j<=H},
R={x,y>=0: j<=H, j-k>=H-1}.

The latter inequalities imply k<=1, so R is already inside K. Boundaries have no effect on the integrals. The full three-dimensional root facet is the graph z=H-l0 over R.

Use angular t=x/(x+y) in [0,1] and radial s=x+y. Write k=s kappa(t), j=s eta(t). Convexity of the homogeneous functions is equivalent to convexity of their restrictions to x+y=1; this follows from the perspective formula f(x,y)=(x+y) f(x/(x+y),1-x/(x+y)). Thus

0 <= eta'' <= kappa''

as nonnegative distributional measures. Define

D(t)=H kappa(t)-eta(t)=(H-1)eta(t)+H(kappa(t)-eta(t)).

It is convex. Therefore the strict angular shadow I={t:D(t)<0} of the positive-area root is one interval, possibly reaching an axis. Positive root area ensures I has nonempty interior.

On a nonroot ray t outside I, boundedness implies kappa>0, the outer radius of K is RK=1/kappa, and L=1-s kappa up to that radius. On a root-visible ray t in I, boundedness implies eta>0. The outer radius and the entry into R are

RK=H/eta,
r0=(H-1)/(eta-kappa),
0<r0<RK.

The fibre length is 1-s kappa on 0<=s<=r0, H-s eta on r0<=s<=RK, and zero afterwards. These statements follow by comparing the two affine branches of L. If D<0 but eta<=0, both branches would remain positive indefinitely, contradicting boundedness; the tail case is similar.

For every ray theta=(t,1-t), with characteristic functions restricted to that ray, one obtains the exact identity

L(s theta)=s int_s^infinity [1_K(r theta)+(H-1)1_R(r theta)]/r^2 dr.       (2.1)

Proof: away from the finitely many breakpoints, L-s dL/ds equals 1 on K\R, H on R, and zero outside K. Hence d(L/s)/ds is minus the integrand in (2.1). Integrate to infinity, where L vanishes, and use continuity at the branch switch and the outer endpoint.

Consequently K and R determine the entire length function L and EVERY projected volume moment int_P f(x,y). They also determine kappa everywhere: on nonroot rays kappa=1/RK; on root rays eta=H/RK and kappa=H/RK-(H-1)/r0. They determine eta on I, but not generally on the two nonroot angular tails. The remaining freedom is vertical placement, not fictitious freedom in volume or projected moments.

As a corollary, for a homogeneous f(x,y) of degree m>=0, integration of (2.1) in radial coordinates gives

(m+3) int_P f = int_K f +(H-1) int_R f.                 (2.2)

The proof uses the actual radial Jacobian s; it does not assume a chosen probability completion.

## 3. Original ell integral and strict fibre-lift monotonicity
Direct integration along each actual fibre gives

Eell=alpha int_K L(H-j-L/2).                            (3.1)

There are also useful exact boundary-divergence identities:

4 Eell=b V+alpha int_K(H-j),                            (3.2)
4 Eell=a V+int_(K\R)[b-alpha(j-k)].                     (3.3)

For (3.2), div(ell(X-B))=4ell-b. The lower graph's flux factor is 1 because hA is homogeneous; nonroot upper facets contain B and have zero flux; the root contributes zero because ell=0; coordinate supports also contribute zero. The lower value of ell is alpha(H-j). Formula (3.3) follows identically from A: the lower facets then have zero flux, while each nonroot upper facet has flux factor 1. These identities also follow by direct radial integration of (3.1).

Suppose k is fixed, j_new>=j_old, j_new=j_old on I, and both j_new and k-j_new remain convex homogeneous, satisfy canonical containment, and have no additional root-visible rays. The last condition will be automatic in the construction below. Then K,R,L are unchanged. On every changed nonroot fibre both endpoints move upward by delta j=j_new-j_old; root fibres do not move. Therefore

V_new=V_old, X_new=X_old, Y_new=Y_old, N_new=N_old,
Z_new-Z_old=int_K L delta j,
Eell_old-Eell_new=alpha int_K L delta j.                 (3.4)

Unless the functions agree, continuity gives strict positivity on a set of positive projected area, so T_new>T_old. The actual centroid moves by (0,0,int L delta j/V); it is NOT held fixed by choosing a reference point. This is a genuine comparison of uniformly filled bodies.

The interpolation j_lambda=(1-lambda)j_old+lambda j_new preserves both convexity inequalities and all containment inequalities. The proof in the next section ensures that every member has the same root and length function. Thus a nontrivial dominance produces arbitrarily small Hausdorff perturbations with strictly increasing T, not merely a distant better competitor.

## 4. Exact optimal allocation on a nonroot angular tail
Let v<1 be the right endpoint of I. The data eta(v), d0=eta'_-(v) are fixed by the root-side germ. On [v,1], every admissible extension has a unique representation

eta(t)=eta(v)+d0(t-v)+int_[v,t] (t-s) dmu(s),           (4.1)
0<=mu<=kappa''|_[v,1).

The atom at v is included, if kappa has a corner there. An atom at 1 changes no function value on the closed interval and is omitted. For polyhedra these are finite atomic measures.

The upper canonical containment condition eta(1)<=l0(1) is exactly

int_[v,1) (1-s)dmu(s)<=B,
B=l0(1)-eta(v)-d0(1-v).                                (4.2)

Existence of the original body implies B>=0. The lower endpoint containment inequality will automatically remain true when eta is raised.

There is NO additional root-avoidance capacity cut at v. Since D is convex, is negative at some point left of v, and D(v)=0, its left derivative D'_-(v) is strictly positive. Adding a possible curvature atom mu{v} changes this derivative by H kappa''{v}-mu{v}> = (H-1)kappa''{v}>=0. Thereafter D''=H kappa''-mu>=0. Hence D stays nonnegative on the whole tail for EVERY mu in the stated interval. This proves that no new root rays arise. A separate artificial slope cap at v would therefore be redundant.

Define weighted measures dw=(1-s)dmu and dW=(1-s)dkappa''. They obey 0<=w<=W and w([v,1))<=B. Let w* fill W from the earliest position v towards 1 until the mass budget B is exhausted, taking a partial last atom when necessary. If B is at least W's total mass, take w*=W. For the piecewise linear problem this is a finite exact greedy algorithm.

For any t<=1, the value added to eta(t) is int phi_t(s)dw(s), where

phi_t(s)=(t-s)_+/(1-s).

This kernel is nonnegative and nonincreasing in s: on s<t its derivative is (t-1)/(1-s)^2<=0, and after t it is zero. Among measures dominated by W with total mass at most B, the front-loaded w* maximizes the integral of EVERY such decreasing kernel. One direct proof is that its cumulative masses dominate all other feasible cumulative masses at every point, followed by integration by parts against -dphi_t; endpoint constants are also nonnegative. Thus

eta*(t)>=eta(t) for all t in [v,1].                    (4.3)

The reflected construction solves the left tail independently. On I leave eta unchanged. The measures glue to convex eta* and kappa-eta*, including at both endpoints of I, and Section 3 proves original-trace dominance.

In geometric terms, moving from the root shadow towards either axis, the maximizer first assigns all available kappa curvature to eta, then possibly splits a single curvature atom, and assigns none of the remaining curvature to eta. The first block makes hB=k-j+l0 affine, and the last makes hA=j-l0 affine. There can still be many curvature atoms within either block. This is NOT a theorem that only two facets remain, nor that every auxiliary vertex moves to the root.

### Proper33 preservation
For a proper33 original body, kappa(0)=kappa(1)=1 and eta(0)=l0(0), eta(1)=l0(1). Since c,d>0, D is positive on both axes, so both nonroot tails exist. On each tail the original endpoint budget is exactly spent. Hence available curvature capacity is at least that budget, and the greedy construction spends exactly the same amount. Both endpoint values remain equal to l0. Thus the two genuine maximal coordinate triangles ABC and ABD, as well as the actual three-dimensional root facet, are preserved. The other facets, physical edges and equilibrium classes need not be preserved.

### Consequence for actual local maxima
A local maximum in the unrestricted marked two-anchor body class, or in its proper33 subclass with no fixed f-vector requirement, must already equal the greedy extension for its own K,R. Otherwise the interpolation in Section 3 is an arbitrarily small strict improvement. This is a new necessary actual-body normal form. It does not establish existence of a maximum by itself and is not applicable to a restriction requiring exactly E=17 along every perturbation.

## 5. Finite vertical realizability test for fixed compatible projected data
The remaining vertical compatibility can be stated exactly, not merely as positivity of moments. Assume kappa is fixed and convex, eta is fixed on the nonempty root interval I with eta and kappa-eta convex there, and the root-side boundary germ satisfies the preceding strict-shadow condition. On the right tail the attainable endpoint values form the whole interval

[B0,B0+Ccap],
B0=eta(v)+eta'_-(v)(1-v),
Ccap=int_[v,1)(1-s)dkappa''(s)
    =kappa(1)-kappa(v)-kappa'_-(v)(1-v).

Every value in this interval is achieved, for example by scaling the full capacity measure. Canonical containment requires eta(1) in

[kappa(1)+l0(1)-1, l0(1)].

Thus this tail has an admissible convex two-gauge extension if and only if these two intervals intersect. The greatest feasible endpoint is min(l0(1),B0+Ccap), and the greedy construction with its corresponding budget pointwise dominates all other extensions. The left test is identical after reflection. A tail absent because I reaches an axis needs no extension and its already fixed axis value is checked directly.

These tests are conditional on ACTUAL compatible radial projected data: on each root-visible ray R must be the outer interval [r0,RK], kappa must be reconstructed from RK and r0 as in Section 2, and its global convexity and the root-side convexities must hold. The tests do not say that arbitrary polygons or moment tuples are realizable. They expose exactly which additional curvature/mark conditions remain when one starts from projected information.

## 6. Executed rational proper33 control
Set a=1,b=1/2,c=d=1/10, alpha=1/2, H=2, l0=9(x+y)/5, ell=1-9(x+y)/10-z/2 and n=8(x+y)/5.

Original gauges:
hA_old=max(-x,-y,-x/250-4y/5),
hB_old=max(x,y,99x/100+y/5).

Improved gauges:
hA_new=max(-x,-x/250-4y/5,-22y/25),
hB_new=max(y,99x/100+y/5,249x/250+2y/25,x-3y/25).

Both bodies use exactly the inequalities in Section 1. Each is bounded because j_old>=1.3(x+y)>0, and j_new>=j_old. Each contains the canonical tetrahedron, has exactly the coordinate triangles ABC,ABD, and has a genuine four-sided root facet. Their projected K and R are exactly equal; their entire length functions coincide.

The right root-shadow endpoint is v=25/27. The available tail curvature of kappa consists of mass21/100 at s1=20/21 and mass51/250 at s2=50/51. The old eta uses the late mass51/250 and none of the early mass. Its exact endpoint budget is1/250. Greedy allocation puts mass21/250 at s1 and none at s2, since

(1-s1)(21/250)=(1-s2)(51/250)=1/250.

This is precisely the new pair of gauges above. It is a nontrivial actual-body realization of the theorem.

The true f-vectors are old(10,17,9) and new(10,18,10). Thus the first body really lies on the first open combinatorial layer, but the improving path does not keep that layer. No equilibrium census is claimed for either body.

Their common volume is79373293181891/207703589072616. The exact differences in actual moments are

Z_new-Z_old=307/57383900,
Eell_old-Eell_new=307/114767800.

The traces are

T_old=1456531658987191226894334238693552/896874836091543517945295885827897
     approximately1.6240077214503583,
T_new=7282658294935956134471671193467760/4484270889882488808689738612293877
     approximately1.624045128800593.

The common K has the following cyclic vertices:
(0,0),(1,0),(50/49,1/49),(250/239,25/478),(500/469,40/469),(2000/3041,2490/3041),(1/13,14/13),(0,1).
The common R has cyclic vertices:
(1/13,14/13),(100/279,55/124),(500/469,40/469),(2000/3041,2490/3041).

The recovery code outputs every true vertex, maximal facet, physical edge, original first moment, actual own centroid, ell integral, n integral and trace. Its computations use exact Fraction arithmetic throughout. Halfspace triple intersections give all vertices; genuine facet polygons are extracted and oriented; their positive tetrahedral fans about an interior point give actual volume moments. Exact supporting inequalities, canonical true vertices, maximal coordinate triangles, positive root area, Euler identity, unchanged K/R, greedy curvature and strict trace improvement are asserted. Polygonal length equality is also checked on every piecewise-affine angular interval, not just a sample grid.

## 7. Complete reconstruction and verification capsule
This is Recovery capsule part 2 of 2 for the object TWO_ANCHOR_FIBRE_GREEDY_DOMINANCE_V1. Part1 is material [internal-source-reference]. Its complete text is the literal file two_anchor_fibre.py; save those bytes without a Markdown fence or other wrapper. There is no additional checkpoint, omitted helper, hidden data file, random seed or parameter. Both exact inputs and the whole geometry/greedy method are inside that source.

Environment executed: Python3.13.5, standard library only. Reconstruction and proof assertions use the same command:

```sh
python3 two_anchor_fibre.py | tee two_anchor_fibre_stdout.txt
sha256sum two_anchor_fibre.py two_anchor_fibre_report.json two_anchor_fibre_stdout.txt
```

The program must terminate without an assertion error and print the initial terminal marker

TWO_ANCHOR_FIBRE_GREEDY_DOMINANCE_V1 PASS

and final markers

DELTA_Z 307/57383900 DELTA_E 307/114767800
REPORT 11035 6bc0017088af8b120b72d478f8e0c3ede704b0b2fb3734c126ff96628ed0b9ae

Expected byte records:
- two_anchor_fibre.py:8407bytes, SHA256743352761b9b92bdc13d71cc61bb5b07aa881df65f6494b79108d3c8f98c45e4.
- two_anchor_fibre_report.json:11035bytes, SHA2566bc0017088af8b120b72d478f8e0c3ede704b0b2fb3734c126ff96628ed0b9ae.
- two_anchor_fibre_stdout.txt:1008bytes, SHA256c7b72ecefc7d1ffd572aeedb235c917e8a21ee293f475802895b6a054133ec5d.

The manifest identifies generated output bytes but does not replace their recovery: the complete deterministic input source is preserved in part1. The analytic theorem in Sections1-5 does not depend on numerical optimization.

## 8. Remaining scientific question
For fixed K,R the actual vertical maximization is now finite and exact. The hard remaining variation is the jointly convex projected pair and the root coefficients, combined with canonical mark reactions and actual root/facet stationarity. The greedy normal form retains all projected volume moments but generally changes the ell distribution. It gives no automatic marginal-preserving deletion, no reduction to the already solved positive-octant root-only fan, and no all-E17 exclusion. No canonical upper construction or accepted registry counter changes.
