# material-52786c239b2e

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# GLOBAL_HIGH_TRACE_ATTAINMENT_AND_ROOT_CUT_FIRST_VARIATION_V1

## Evidence status and purpose
Coordinator analytical theorem, with complete new arguments below. It uses the explicitly identified accepted cone-tail and joint-mass theorems as premises; it does not claim a new computation, a full trace upper bound, an E17 exclusion, or an attaining class110 polyhedron. The new results are conditional global attainment of a high-trace maximum, a uniform positive gap for its common-edge endpoint values, the exact root-cut first variation with actual uniform moments and changing marked triangles, and a quantitative positive-area root-face bound. They close the escape-to-infinity and collapsed-root obstructions for the VARIABLE-ENDPOINT marked-body optimization problem. They do not by themselves finish the zero-endpoint extension of the existing local-maximizer polyhedrality theorem.

### Exact accepted dependencies, fully read by the coordinator
1. [internal-source-reference], SHA256 48ee32688f80abfcd84b1f50f0648ba3942734c55e4bb3dc417beca668a3393b: cone-tail concentration. Its result T>=51/25 implies m>13/15. The proof's extension from full triangular facets to fixed supporting triangular patches is explained explicitly below.
2. [internal-source-reference], SHA256 2c460625df162099bfba6437818bd8eff154d6d2f17d3f21e9ac2e4211c4d18e: extended joint mass/centroid inequalities and the containing-tetrahedron pointwise support bound for arbitrary convex bodies with fixed supporting triangle patches.
3. minimum-0111, SHA256 64909830719ea325d6660a5d6d081ded07c9b30b980c16c647d4b81ee5d2c822: endpoint-and-span envelope, including the canonical-point fan lower bounds on the actual affine moment. The endpoint-sum strengthening used here is derived explicitly, not substituted for this parent.
4. minimum-0139, SHA256 c58993f6099c9026b8aece0f2dcedf5b45aed4f8c933eacc92d639040f2c8a2f: every attained Hausdorff local maximum in the all-bounded-convex-body marked class with fixed a=1,0<b<1,c,d>0 and positive root area is a polytope with at most16 true vertices. This theorem is used only in the conditional corollary with its exact endpoint hypotheses.

No computer code materially contributes to the present analytical proof. The formulas and all constants needed to reproduce the deductions are given literally.

## 1. Actual body, marked support patches, and original trace
Let
A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
T0=conv(A,B,C,D).
Consider every bounded convex body P containing T0 and contained in {x>=0,y>=0}. It is full dimensional. ABC and ABD are the fixed triangular SUPPORT PATCHES in the two coordinate supporting planes. They need not be full maximal faces; the four marked points need not be true vertices of P.

P is uniformly filled throughout. Write V=Vol(P), g=(gx,gy,gz) for its ACTUAL uniform volume centroid, and let ell be an auxiliary nonzero affine function nonnegative on P. It is NOT a material density. Set
 a=ell(A), b=ell(B), c=ell(C), d=ell(D),
 mu=(1/V) integral_P ell = ell(g)>0,
 t=6V,
 Bell=integral_P ell=V mu,
 mx=gx/(2V), my=gy/(2V), m=mx+my,
 n=(a+b+c)x+(a+b+d)y,
 N=integral_P n.
The ORIGINAL trace is
 T=[mx(a+b+c)+my(a+b+d)]/(3mu)=N/(6V Bell).
The cone over each marked triangular patch with apex g has volume V mx/3 or V my/3. Thus these definitions, the trace, and its positive rescaling in ell are invariant under invertible affine changes of coordinates carrying the marked tetrahedron along. No affine or projective transport of a nonuniform density is used.

The accepted joint-mass source gives, throughout this closed marked class,
 mx+my <= 3/4+1/(8V) = (3/4)(1+1/t) <= 3/2,
 4gx<=t, 4gy<=t, 4(gx+gy)<=t+1.
Its containing-tetrahedron argument also gives, for every (x,y,z) in P,
 x>=0, y>=0, x+y<=t, 1-t<=z<=t-x-y.
The last upper bound may harmlessly be weakened to z<=t.

### Why the cone-tail theorem applies to these fixed patches
For a uniformly filled convex body with interior g the boundary cone probability measure is
 dnu(y)=[(y-g).n(y)]/(3V) dH^2(y).
A triangular subset of a planar supporting face has cone probability equal to its cone volume divided by V; its conditional law is uniform on that triangle. The two marked patches have disjoint relative interiors and their cones have disjoint interiors. They therefore provide precisely the two selected boundary components of masses mx/3 and my/3 used by the accepted tail proof. A larger coordinate face merely contributes additional boundary mass to the unselected remainder; none of the selected-triangle second-moment or tail estimates requires that a patch be a whole maximal facet. The same boundary-cone integration applies to arbitrary convex bodies, or follows by bounded convex approximation. Consequently the accepted implication
 T>=51/25 => m>13/15
holds for the present support-patch class as well. Combining with m<=(3/4)(1+1/t) gives
 T>=51/25 => t<45/7.
This is a high-trace implication, not an unconditional volume bound.

## 2. Endpoint gauges and an endpoint-sum inequality
For any affine ell>=0 on a bounded convex body, let L=max_P ell. If q is a maximizing point, q_s=sq+(1-s)P lies in P and in {ell>=sL}, and has volume (1-s)^3 V. Integrating these superlevel estimates over 0<=s<=1 gives mu>=L/4. Thus
 0<=a,b,c,d<=4mu.
This proof does not require the marked points to be vertices.

We claim the stronger trace estimate
 T <= 1+(a+b)/(4mu).                         (2.1)
Assume c>=d, the other order being symmetric. Put K=a+b+c and k=a+b+d. The accepted centroid inequalities imply
 K(4gx)+k(4gy)=(c-d)(4gx)+k[4(gx+gy)]
 <= (c-d)t+k(t+1)=Kt+k.
Hence T<=(Kt+k)/(4tmu).
Fan the body from C. The average ell on a tetrahedral fan simplex is one quarter the sum of its four endpoint values, all nonnegative. The fixed opposite patch ABD supplies the additional term a+b+d with its tetrahedron of volume1/6, while C contributes c on the entire fan. Equivalently, using the accepted canonical-point fan inequality,
 4tmu>=ct+(a+b+d)=ct+k.
The same fan formula is valid when C lies within an edge or face, or is not an extreme point: choose finite polyhedral approximations or integrate the fan over the supporting boundary; triangles contained in the opposite supporting face remain valid selected pieces. Since Kt+k=ct+k+(a+b)t, (2.1) follows.

Normalize ell by positive scaling so that mu=1. If T>=51/25, then (2.1) implies a+b>=4(T-1). As each of a,b is at most4, both satisfy
 a,b >=4(T-2)>=4/25.                        (2.2)
More generally this gap is 4mu(T-2). In particular neither common-edge endpoint can vanish at a trace above2. No assumption c,d>0 was used.

## 3. Conditional GLOBAL attainment above the threshold
Let tau=51/25. Suppose at least one marked pair (P,ell) in Section1 has T>=tau. Normalize mu=1 for every such pair. By the preceding estimates, every high-trace P is contained in the same compact convex set
 K0={x>=0,y>=0,x+y<=45/7, -38/7<=z<=45/7-x-y},
and its endpoint vector lies in [0,4]^4 with a,b>=4/25. The enclosing rectangular box has squared diagonal
 [45^2+45^2+83^2]/49=10939/49<225,
so diam(K0)<15.

Take the class of all convex P with T0 subset P subset K0, and all endpoint vectors in [0,4]^4 whose affine ell is nonnegative on P, has mean mu=1, and trace T>=tau. This class is closed and compact. Indeed support functions of the bodies are uniformly bounded and uniformly Lipschitz on the unit sphere, hence any sequence has a uniformly convergent subsequence, corresponding to a Hausdorff-convergent convex body. Containment of T0 persists and gives V>=1/6, so the limiting body stays full dimensional. The finite coefficient vectors have a convergent subsequence. Affine nonnegativity passes to the limit. Bounded Hausdorff convergence of full-dimensional convex bodies gives convergence of volume and integrals of uniformly converging affine functions: their indicators converge except on a boundary of volume zero. Therefore mu,N,Bell,T are continuous, and Bell=V>=1/6 never vanishes.

It follows that T attains its maximum on this compact high-trace class. This is a maximum over the ENTIRE variable-endpoint marked class whenever the class has any high-trace member: any competitor with still greater T is itself high-trace and can be normalized into the same compact class. It is not merely a maximum in an artificially bounded truncation.

This theorem says that a hypothetical high-trace counterexample forces a genuine attained maximum of a geometrically larger marked class. It does not say that every fixed-endpoint problem attains its supremum, or that the actual maximum is high-trace.

## 4. An attained high-trace maximum must touch ell=0
Let (P,ell) be the global maximum just obtained. If min_P ell>0, keep P and both marked triangles fixed and replace ell by ell-epsilon for small positive epsilon. In the original formula its numerator divided by3 changes by -epsilon m, and its denominator mu changes by -epsilon. Thus
 dT/depsilon at0 = (T-m)/mu>0,
since T>=tau>2 and m<=3/2. Rescaling to mean1 is harmless. This contradicts maximality. Consequently min_P ell=0, and the root contact set F=P intersect {ell=0} is nonempty. Since mu>0, grad ell is nonzero.

## 5. The admissible root cut, with zero marked endpoint repair
Write h=max(a,b), k=min(a,b)>0, and let H be the one of A,B with value h. Define
 F=P intersect {ell=0},
 P_epsilon=P intersect {ell>=epsilon}.
For sufficiently small positive epsilon keep A,B and each of C,D with positive ell value. For each zero-valued mark X in {C,D}, replace it by
 X_epsilon=(1-epsilon/h)X+(epsilon/h)H.
It belongs to P_epsilon and has old ell value epsilon. Thus the new marked tetrahedron is contained in P_epsilon, is nondegenerate, and its two marked triangles remain supporting patches in x=0 and y=0. A zero-mark triangle has area multiplied by 1-epsilon/h; an unchanged-mark triangle keeps its area. The common edge AB is retained. The auxiliary function becomes ell-epsilon. Its new canonical values at A,B are a-epsilon,b-epsilon; its values at retained positive C/D decrease by epsilon, while its value at every repaired zero mark is zero.

An affine map carrying this new tetrahedron back to T0 produces another admissible marked-body pair of Section1. Both the trace and uniform-filling interpretation are preserved because the map has a constant Jacobian. Positive normalization back to mean1 also leaves T unchanged. This is a VARIABLE-ENDPOINT deformation. It is not a fixed-ell or fixed-lattice ascent statement.

## 6. Full exact right first variation
Define
 m0=mx*1_{c=0}+my*1_{d=0},
 r=N/V, q=N/Bell,
 G=n-r-q ell.
All quantities in the next formula are evaluated at the original body and auxiliary function. Then the full deformation of Section5 satisfies

 dT/depsilon|_{0+}
 = [T-m-(k/(3h))m0]/mu
   - [integral_F G dA]/[6V Bell |grad ell|].       (6.1)

Here dA is ordinary Euclidean two-dimensional area in the ORIGINAL canonical coordinates. The integral is zero if F has area zero. Formula (6.1) includes the true changes in uniform volume, centroid, affine moment, and marked-patch areas.

Proof of the shape term. Parallel sections at ell=s converge as s decreases to0 to F after the natural translation of planes. Convexity gives both the upper Hausdorff inclusion and the lower scaled copy of F obtained by joining it to an interior point. Consequently section areas and affine section integrals converge, even when F is lower dimensional and their limit is zero. Coarea therefore gives, with the original n and ell frozen,
 Vdot=-Area(F)/|grad ell|,
 Ndot=-integral_F n dA/|grad ell|,
 Belldot=0.
The last identity uses ell=0 on F. Differentiating N/(6V Bell) yields exactly the second term in (6.1), because G=n-r on F. In the zero-area case all removed volume and fixed affine moments are o(epsilon), not an assumed zero density correction.

Proof of the explicit endpoint/patch term. If a mark X is positive, the sum of the three new triangle endpoint values is reduced by3epsilon, and its area is unchanged. If X is zero, its old sum is h+k and its new area-weighted sum is
 (1-epsilon/h)(h+k-2epsilon)
 =h+k-epsilon(3+k/h)+O(epsilon^2).
Holding the old body's integrals fixed for this part, the trace numerator divided by3 therefore has derivative -m-(k/(3h))m0, while the new mean has derivative -1. Its contribution is the first term in (6.1). Mixed terms between the body cut and these explicit changes are o(epsilon); adding the two derivatives proves the formula. In particular no full-centroid invariance is being postulated.

## 7. Collapsed roots are impossible, and a root-average inequality
Since m0<=m<=3/2 and k/h<=1,
 T-m-(k/(3h))m0 >=T-2>0.                       (7.1)
If the root set F has area zero, the second term of (6.1) vanishes, so the cut strictly increases T. This contradicts global maximality. Thus every global maximum with T>=51/25 has a genuine positive-area root face.

Moreover the admissible right derivative at a global maximum is nonpositive. Multiplying (6.1) by 6V Bell and using Bell=Vmu gives the sharper root-average stationarity inequality

 [integral_F G dA]/|grad ell|
 >=6V^2 [T-m-(k/(3h))m0]
 >=6V^2(T-2)>0.                               (7.2)

This is a positive AVERAGE over the root face, stronger than merely finding one root point where G>0. It holds also when one or both noncommon canonical marks have value zero. It is not the sign condition for an unconstrained fixed-endpoint root tilt: the repaired marked patches matter.

## 8. A uniform canonical-coordinate root-area lower bound
Continue with mu=1 and T>=51/25. Choose z in F. Since g,z belong to K0 and ell(g)-ell(z)=1,
 |grad ell|>=1/|g-z|>1/15.
On P, each endpoint value is at most4, so n<=12(x+y)<=12t<540/7. On F we have G=n-r<=n, because r=N/V>0. Also V>=1/6 and T-2>=1/25. Applying (7.2) gives
 Area(F)*(540/7) >= integral_F G dA
 >= |grad ell|*6V^2*(T-2)
 > (1/15)*(1/6)*(1/25).
Therefore the explicit, deliberately nonsharp bound is

 Area(F) > 7/1215000.                          (8.1)

The normalization and coordinate dependence are essential: this is the area in the canonical tetrahedron coordinates, with mean ell normalized to1 for deriving the common container/gradient estimates. The trace itself is affine invariant. The body remains uniformly filled.

## 9. Consequence for finite localization, and the exact remaining boundary
If any actual adjacent-triangle instance has trace at least51/25, it is contained in the marked support-patch class. Sections3-8 force an attained global maximum in that class with a,b>=4/25 after mean normalization and a root face of area>7/1215000. Thus neither infinity, disappearance of both common endpoints, nor root collapse can be the missing global-attainment mechanism.

If this maximizing pair additionally has a!=b and c,d>0, exchange A,B when necessary and rescale ell to a=1. It is then an attained local maximum in the fixed-endpoint class of accepted result minimum-0139, with positive root area. That theorem applies literally and gives at most16 true vertices.

This source alone does NOT eliminate the alternatives a=b or c*d=0; other accepted boundary-sector theorems may eliminate some of them, but their hypotheses must be used explicitly. In particular no unconditional global16-vertex reduction, sharp Cstar bound, global T<51/25 theorem, E17 prohibition or class110 attainer is asserted here. The useful next step is a positive-area zero-endpoint extension of the local-maximizer theorem, or a direct sharp boundary bound. The global uniform-polyhedron bounds remain34<=C_min<=622.
