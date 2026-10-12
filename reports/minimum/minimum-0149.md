# minimum-0149

AI research report · 2026-09-21 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# UNEQUAL_ENDPOINT_APEX_FAN_ROOT_BOUND_203_V1

## 1. Determination

A complete nonaxial root-only sector with independently varying unequal endpoint values is now resolved. The original uniformly filled trace satisfies

    T <= H(b,rho) <= Cstar < 203/100 < 51/25,
    H(b,r)=2(1-b^2)(1-br^3)/[(1-br^2)(1-b^2r^2)].

The class has arbitrary positive b,c,d<1 and an arbitrary compact convex root within the explicit triangle in Section 2, containing its specified base edge. No root vertex count, root edge directions, fixed root deficit, endpoint closeness, height cutoff or bounded aspect ratio is imposed.

For polytopes, the geometric description is particularly useful: this includes the entire proper, positive-octant root-only stratum in which the root and z=0 are the only maximal facets not incident to B, and their intersection is an edge. Every other actual maximal facet, however many, contains B. The two coordinate facets remain the genuine maximal triangles ABC and ABD.

At fixed endpoints and fixed base, there is an actual dominating replacement with at most four root vertices, hence at most eight true vertices and seven maximal facets. It preserves the original volume, positive root area, Bell, and in fact the entire volume distribution under the ORIGINAL affine function ell. It increases the original n-moment. The mechanism works for unequal b,c,d because the changing part is one actual pyramid from B, not because an unweighted parallelized image is substituted for the original density.

The supremum over this new proper four-canonical class is exactly the previously known Cstar, approximately 2.02878303567341172514. The sharpness statement is for a proper positive-endpoint sequence; its limit has zero endpoints and enlarged coordinate patches. No proper attainer is asserted.

An exact nonempty 10/17/9 sector is demonstrated by a six-vertex root. Two continuous root slides reduce its actual hull through 9/15/8 to 8/13/7, preserving V, Bell and root area and strictly increasing T. Since this control already has nine maximal facets, the theorem reaches the remaining terminal range rather than merely reducing oversized input hulls. All three endpoint controls have own-centroid strict S/U/H=4/4/6 and no weak points. Thus they are not 110 bodies, and this result makes no unlabelled E17 census subtraction or change to the global 34..622 interval.

## 2. Authority and exact geometric class

The complete new research-journal(20260921-004038).md was read through line 1874/EOF, including the entire immutable parent. Its 322365 bytes have SHA-256 eef591702897e81e6bcfd945953685198774f0ed1ea8d537f6af8ed57d420235. The required literal parent is minimum-0146, SHA-256 343b1c30bfa2f3d225bf9cc2ab1675beee4c784a2e88659a18aa45e6509d390f, PARALLEL_ROOT_MINKOWSKI_SECTION_DOMINANCE_201_V1. Its all-convex-root 201/100 theorem has endpoints (1,b,b,b); it is not an unequal-endpoint theorem.

The parent's warning is retained exactly: unequal endpoint parallelization requires L^-4 and L^-5 weights, and equal unweighted section areas do not preserve those original integrals. No source-authority conflict was found. The one-zero shell and joint root-stationarity discussions are background, not missing computational dependencies of this proof.

Put

    A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
    T0=conv(A,B,C,D),
    ell=1+(d-1)x+(c-1)y+(b-1)z,
    n=(1+b+c)x+(1+b+d)y.

Choose FIVE independent positive parameters beta,s,t,e,f and set

    b=1/(1+beta), c=e/(1+e), d=f/(1+f),
    Z=beta+s+t,
    DU=1+(s+t)f, DV=1+(s+t)e,

    U=((1+f)(1+sf)/DU, t(1+e)f/DU, 0),
    V=(s(1+f)e/DV, (1+e)(1+te)/DV, 0),
    W=(s(1+f)/Z, t(1+e)/Z, (1+beta)/Z).
                                                        (1)

All three points lie on ell=0 and have positive x,y. W has positive z. Let K be ANY compact convex subset of

    Delta={(u,v):u>=0,v>=0,u+v<=1}

that contains the whole edge [(1,0),(0,1)] and has positive area. Define

    F={W+u(U-W)+v(V-W):(u,v) in K},
    P=conv(T0,F), theta=2 Area(K) in (0,1].               (2)

W is a container corner, not a vertex of P unless it belongs to F. It must not be counted as an additional body vertex in a truncated-root example.

For this entire class the explicit bound in Section 1 uses

    rho^2=1-beta*theta/(beta+s+t).                       (3)

The original integrals are V=integral_P1, Bell=integral_Pell, N=integral_Pn, and T=N/(6 V Bell). Since every root point has positive x,y, the intersections x=0 and y=0 are exactly ABC and ABD. All four canonical points are true vertices with positive ell. The true zero-root face is exactly F and has positive area. Also z>=0 throughout P and its z=0 facet is the actual pentagon conv(A,D,U,V,C).

### Why this is the whole indicated fan stratum

The parent's positive canonical-fixing projectivity sends a positive-octant root to x'+y'+z'=2. This is used only for geometric classification, never for uniform-image integration. If the base-root edge has endpoints U',V', the side facets through BD and BC cut the root plane in y'=eta and x'=xi. Properness gives xi,eta>0; positive root area gives xi+eta<2. Thus the permitted root is precisely a convex subset of the triangle

    x'>=xi, y'>=eta, x'+y'<=2,

containing its z'=0 edge. Conversely every such root gives the indicated fan. The substitutions

    xi=2fs/(1+fs+et), eta=2et/(1+fs+et)

and the actual inverse projectivity give exactly (1). They cover every xi,eta>0 with xi+eta<2 when e,f>0. The full triangle yields six facets: x=0, y=0, z=0, ell=0 and the planes BDUW and BCVW. Cutting the root inside this triangle while retaining UV lifts each new root boundary line to a plane through B; these planes retain the base pentagon. This proves the description for arbitrary root combinatorics.

The result does not claim to cover every parallel-root body from the parent: some have a different side fan or a root disjoint from z=0. It resolves a different complete sector with full independent endpoint freedom.

## 3. The original-density variational mechanism

Let G=conv(A,D,U,V,C) in z=0. There is a genuine decomposition, with disjoint interiors,

    P=conv(B,G) union conv(B,F).                         (4)

Both pyramids share the triangle BUV. This is not a signed triangulation relaxation. It follows either from the six-halfspace description above and the lifted cuts, or by checking the two sides of the plane BUV. The base pyramid is fixed whenever the endpoints and U,V are fixed.

Write alpha=1-b, Ar=Area_xy(F), and Jr=integral_(F projected to xy) n. The exact contributions of the changing root pyramid are

    Vroot=b Ar/(3alpha),
    Bellroot=b^2 Ar/(12alpha),
    Nroot=b Jr/(4alpha).                               (5)

Thus preserving the actual root area preserves BOTH denominator integrals. There are no independent moment choices.

In fact this preserves more. With h=b/|grad ell|, use the real pyramid parametrization B+lambda(r-B), r in F, 0<=lambda<=1. Its volume element is h lambda^2 dArea(r) dLambda, ell=b(1-lambda), and n=lambda n(r). Therefore, for any integrable psi,

    integral_rootpyramid psi(ell)
      =h Area(F) integral_0^1 lambda^2 psi(b(1-lambda)) dLambda.

For nonnegative psi, increasing integral_F n also increases integral_rootpyramid n psi(ell), with the analogous lambda^3 factor. Adding the fixed base proves preservation of the full original ell-marginal and domination of every such nonnegative reweighted n-integral.

### Root reduction at fixed original moments

For a polygon K, keep its mandatory endpoints (1,0),(0,1). Move an interior true root vertex parallel to the chord between its two neighbours. The triangle between those neighbours and the moving vertex has constant area. Its affine n-integral varies linearly, with derivative equal to one third of that area times the directional derivative of n. Choose the nondecreasing direction.

All polygon supporting-side inequalities and the three containing-triangle inequalities are affine in this one displacement. The feasible interval is bounded because Delta is compact. Move to its first wall. Either a true vertex disappears or the moving vertex reaches the boundary of Delta. Previously fixed boundary vertices do not move. Repeating terminates: each step reduces the true vertex count or reduces the number of interior vertices without increasing the former count.

A terminal polygon has all its true vertices on the boundary of Delta and contains the two prescribed corners. Each remaining side can contain at most one additional true vertex. Hence it has at most FOUR vertices and is

    K(u,v)=conv((1,0),(0,1),(0,v),(u,0)),
    0<=u,v<=1, uv<1, theta=1-uv.                       (6)

The endpoint cases u=0 or v=0 give the full triangle after removing redundant generators; u=1 or v=1 gives a triangular root. The area and original V,Bell are unchanged throughout the actual deformation, and N does not decrease. No assumption about the signs of n(U)-n(W) and n(V)-n(W) is needed.

For a nonpolygonal compact convex K, take inscribed polygons containing the mandatory edge, apply this reduction, and take a subsequential limit of (u,v) in the compact square. Area and first moments converge. The limiting quadrilateral has exactly the original area and no smaller n-moment. This gives the same conclusion without assuming polyhedral attainment of the unrestricted trace problem.

Full J and the own centroid generally change. The method does not preserve a mechanical class, even though the reported static controls happen to have equal strict counts.

## 4. Exact quadrilateral moments and a coupled endpoint comparison

The remaining family has SEVEN parameters beta,s,t,e,f,u,v, with five unrestricted positive parameters and the complete closed unit square for u,v. All integrals below are in original physical coordinates.

Let h=1+b, j=det(U-B,V-B,W-B)>0, DeltaUV=x_U y_V-y_U x_V, and write nU=n(U), nV=n(V), nW=n(W). The scaled base-pyramid integrals are

    Lb=y_U+DeltaUV+x_V,
    Eb=y_U(h+d)+DeltaUV*h+x_V(h+c),
    Mb=y_U[n(D)+nU]+DeltaUV[nU+nV]+x_V[nV+n(C)].

The actual full integrals satisfy L=6V, E=24Bell, M=24N and

    L=Lb+j(1-uv),
    E=Eb+b*j(1-uv),
    M=Mb+j{nU+nV+nW
          -uv[3nW+u(nU-nW)+v(nV-nW)]},
    T=M/(LE).                                         (7)

These are the three real base tetrahedra from B, plus the root pyramid, minus its genuine corner tetrahedron. The removed corner tetrahedron has root area fraction uv; it is not an independently selected weight.

### A genuine zero-endpoint comparison body

Keep beta,s,t,u,v fixed, set e=f=0 in (1), and RECONSTRUCT the body. Then c=d=0,

    U0=D, V0=C,
    W0=(s/Z,t/Z,(1+beta)/Z),
    F0=conv(D,C,W0+v(C-W0),W0+u(D-W0)),
    P0=conv(T0,F0).

Its C,D are root points, not positive-ell auxiliaries. Re-hulling is essential; the generic comparison body has 6/11/7, rather than the original 8/13/7. It is an actual uniformly filled body. Its scaled formulas reduce to

    L0hat=Z+1-uv,
    E0hat=(beta+2)Z+1-uv,
    M0hat=(beta+2){2Z^2+2Z+s+t
                 -uv[3(s+t)+beta(u+v)]},

    V0=L0hat/(6Z),
    Bell0=E0hat/[24(1+beta)Z],
    N0=M0hat/[24(1+beta)Z^2],
    T0=M0hat/(L0hat E0hat).                            (8)

The new whole-domain inequality is

    T(P)<=T(P0).                                      (9)

It does NOT state that V, Bell or the root area remain fixed during this endpoint change. It also does not assert coordinatewise monotonicity along every partial decrease of e or f. It is the endpoint comparison (9), retaining the common actual numerator and denominator, that is proved.

### Complete exact certificate for (9)

Put Dcal=Z DU DV and Hcal=(1+beta)(1+e)(1+f), and define

    Lhat=Dcal L, Ehat=Hcal Dcal E,
    Mhat=Hcal Dcal^2 M,
    Fpoly=M0hat Lhat Ehat-L0hat E0hat Mhat.             (10)

Every multiplier and both trace denominators are positive on the actual domain. The source constructs (10) directly from (1) and (7), verifies the root-plane identities and the cleared determinant identity for j, and proves Fpoly>=0 on the ENTIRE unbounded orthant beta,s,t,e,f>=0 times [0,1]^2 in u,v.

The polynomial has 16648 terms and degree vector (6,8,8,5,5,4,4). There are 4319 ordinary orthant coefficient polynomials. Their exact tensor Bernstein representations in u,v have 35765 positive and 1533 zero coefficients, with none negative. The verifier independently recovers each power polynomial from the Bernstein tensor by finite differences.

Exactly two remaining orthant pieces are handled together in their free orthant variable, rather than falsely discarding their negative power coefficients. They are f S(t;u,v) and e S(s;v,u), where

    S(z;u,v)=z{2z^3
      +z^2[-8u^2v^2+2u^2v+7uv-1]
      +z[6u^3v^3-3u^3v^2-8u^2v^2+3u^2v+uv+1]
      +u^4v^3-3u^3v^3-2u^3v^2+8u^2v^2+u^2v-7uv+2}.

Each has 25 degree-(4,4) Bernstein coefficient polynomials a0+a1 z+...+a4 z^4. Every row has a0,a1,a2>=0 and a4>0. Whenever a3<0, its exact coefficients satisfy 4a2a4-a3^2>=0, so

    a4 z^4+a3 z^3+a2 z^2
      =z^2[a4(z+a3/(2a4))^2+(4a2a4-a3^2)/(4a4)]>=0.

All 50 rows and their margins are regenerated. This covers the whole orthant, including controller and root-merger boundaries, without a finite search cutoff, guessed extremizer, unlisted subdivision or feasibility pruning.

## 5. From the actual comparison root to the sharp envelope

The xy projection of F0 lies in Delta and contains CD. Its ACTUAL area is

    A0=beta(1-uv)/(2Z)=beta*theta/(2Z).

At c=d=0, the base pyramid is precisely T0. Formula (5) shows that fixed root area again fixes V and Bell. Among measurable subsets of Delta of this same area, the upper band

    Rstar={(x,y) in Delta:rho<=x+y<=1},
    rho^2=1-2A0,

maximizes the integral of x+y. This is a direct comparison: subtract rho from the integrand; points exchanged below the cut have nonpositive value, and those exchanged above have nonnegative value. The maximizing band is itself convex and contains CD. Thus it is a genuine permissible root for the comparison, not a relaxation whose moments lack a body.

Its lift is z=(1-x-y)/(1-b). The resulting body can have enlarged coordinate patches, which is correctly retained in this stage. Its exact original data are

    Lstar=(1-b*rho^2)/(1-b),
    Estar=(1-b^2*rho^2)/(1-b),
    Mstar=2(1+b)(1-b*rho^3)/(1-b),

with the same convention Lstar=6Vstar, Estar=24Bellstar, Mstar=24Nstar. Therefore its original trace is exactly H(b,rho). Combining the three genuine comparisons proves the bound in Section 1, including an initial equality T=51/25.

### Independent below-threshold proof

The new source also proves, on the complete closed square 0<=b,r<=1,

    203(1-br^2)(1-b^2r^2)-200(1-b^2)(1-br^3)
      >=(1-b)^2/1000.                                (11)

There are exactly 23 closed binary-subdivision leaves, degree (3,4), 457 positive and three zero Bernstein coefficients. The full paths are embedded; prefix coverage and Kraft sum one are checked, and every restricted power polynomial is independently reconstructed. For b<1 and r<1 the denominator is positive, so (11) gives H<203/100 with a strict explicit remainder. The claimed exclusion does not require importing an older sharp-constant certificate.

### Supremum and proper sharpness

Define Cstar=sup H(b,r) for 0<b,r<1. For ANY fixed such b,r, set

    beta=(1-b)/b, s=t=epsilon,
    e=epsilon, f=2epsilon, u=v=r,
    epsilon>0.

Every member constructed by (1),(2),(6) is a genuine proper 8/13/7 four-canonical body with positive root area and unequal c,d. As epsilon decreases to zero, its original vertices and integrals converge to the axis-root band r<=x+y<=1. Its trace tends to H(b,r). Hence the supremum of the new proper class is EXACTLY sup H, not just bounded by it.

The identification of sup H with the previously isolated algebraic Cstar is inherited: if rstar is the unique root in (0,1) of

    r^8+4r^7-2r^6-12r^5-7r^4-4r^3-12r^2+12r+8,

then

    bstar=(3rstar^7+11rstar^6-9rstar^5-33rstar^4
           -20rstar^3-12rstar+40)/16,
    Cstar=H(bstar,rstar).

The new proper-class supremum equality follows from the explicit sequence above; it does not identify the limiting coordinate quads as proper triangles or establish a proper maximizer. A fully rational nonrecord sequence in the audit uses beta=3, r=5/6 and epsilon=10^-m; its exact limit is 133020/65569.

## 6. Exact actual E17 control and continuous reduction

The control parameters, in the source order (beta,s,t,e,f), are

    (3,1/10,1/5,1/9,1/4),
    (a,b,c,d)=(1,1/4,1/10,1/5).

Its container points are

    U=(205/172,20/387,0),
    V=(5/372,920/837,0),
    W=(5/132,20/297,40/33).

Use the canonical labels 0=A,1=B,2=C,3=D and the SIX root generators, labels 4..9, obtained from W+u(U-W)+v(V-W) with the complete ordered barycentric list

    [(1,0),(0,1),(0,4/5),(1/5,1/2),(1/2,1/5),(4/5,0)].

This is an exact 10/17/9 body. W itself is not a body vertex. Its maximal facet cycles are

    012, 031, 02543, 1652, 1349,
    176, 187, 198, 456789.

In particular 012 and 031 are the actual adjacent triangles. The base is a pentagon, the root is a hexagon, two other facets are quadrilaterals and three are triangles. No integration diagonal is counted as an edge.

The two whole root slides terminate at these exact root polygons:

    First wall:
      [(1,0),(0,1),(0,37/50),(1/2,1/5),(4/5,0)].
    Second wall:
      [(1,0),(0,1),(0,37/50),(53/74,0)].

The first wall is 9/15/8 and the second is 8/13/7. These are continuous convex-body slides, not a comparison inferred from three samples: the recovery computes their complete affine polygon and containing-triangle guards and goes to the exact first endpoint. The proof in Section 3 supplies the original mass identities along each segment.

All three bodies have

    V=7415825/28504872,
    Bell=33757283/456077952,
    Area_xy(F)=442975/1583604,
    Area(F)^2=6318504590125/22570214659344.

Their original trace values are, respectively,

    480828559454379/250338103203475,
    480875975747199/250338103203475,
    1046802371948499/544853518736975,

approximately 1.9207166360, 1.9209060450 and 1.9212546785. Both increases are strict. The original first moment of the 10/17/9 body is

    J=(553818596665/6687471010176,
       380888099095/5015603257632,
       258595825/3762643104).

The complete changed J, true own centroid, N, supporting planes, maximal cycles, true edges and all four primitives per edge are regenerated separately for every body; they are not transported from this first J. Each endpoint has strict 4/4/6, weak zero and every primitive nonzero. No whole-interval mechanical preservation is asserted.

The zero-endpoint comparison of the final quadrilateral is an actual proper 6/11/7 body, with

    V0=377/1980, Bell0=1697/31680,
    N0=1596403/12893760,
    T0=47892090/23671453 approximately 2.0232002657.

The changed V and Bell explicitly show that Section 4 is not a moment-preserving endpoint deletion.

A second proper 8/13/7 control has

    (beta,s,t,e,f)=(3,1/10000,1/10000,1/10000,1/5000),
    u=v=5/6.

Its original trace is approximately 2.028641707578095, strictly above 253/125 and 201/100, but below 133020/65569<203/100. The complete rational recipe, all its own volume and moment fractions, actual root area, maximal facets and weak-free 4/4/6 audit are in the same standalone source. It is a nonrecord control demonstrating that the new unequal-endpoint class cannot simply inherit the parent's 201/100 ceiling.

## 7. Exact complement and effect on E17

The proof covers the entire stated class, not all root-only bodies. A genuinely remaining proper root-only body may have another maximal facet not containing B, a root not meeting z=0 in the required base edge, root points outside the containing B-side triangle, negative-z root geometry, or an opposite endpoint c or d at least one. Positive-ell auxiliary vertices are not removed by this theorem. The general finite root-only and all-body maximum reductions retain their separate hypotheses.

The fixed-fan condition is substantive. The parent's mixed-canonical chord counterexample has changing contributions from other positive-density boundary fans. Our equation (4) is precisely the extra geometry that makes root area sufficient to preserve the original denominator distribution here. Root-area preservation is not again asserted for arbitrary mixed stars.

All quadrilateral and triangle-root seams u=0, v=0, u=1 or v=1 are included by the formulas after re-hulling. The excluded uv=1 set has zero root area and is only an algebraic boundary. Setting e or f to zero changes canonical/root status and is evaluated as the new actual hull. Finite full-dimensional Hausdorff limits retain the uniform 203/100 ceiling, because T0 remains and Bell is bounded below by 1/24. This includes relevant endpoint limits; a collapsed support is not called a facet, and no division by 1-b is made at b=1. Formal zero-denominator or infinite-coordinate parameter faces are not asserted to be bodies.

A coordinate patch can occur in the last axis-band comparison or in a sharp limit. Its uniform ceiling still bounds the preceding proper body, so exclusion of T>=51/25 does not rely on transferring equality through a resolution. Conversely, the sharp proper sequence establishes a supremum only, not attainment or preservation of the limiting face lattice.

For E17, this is a new complete continuous trace exclusion wherever the actual labelled facets and root meet the fan condition. The exact 10/17/9 control proves that the geometric sector is nonempty. There is no literal FULL253 or other registry incidence mapping here, so no census decrement, whole E17 exclusion, 110 construction, or improved Cmin bound is inferred.

The useful continuation is now the next root-only stratum with an additional non-B facet. One must compensate or control that additional genuine pyramid contribution while retaining the original ell-marginal, rather than apply the fixed-fan invariant outside (4).

## 8. Complete recovery and observed evidence

All new proof-bearing computations use CPython 3.13.5 and SymPy 1.14.0 with assertions enabled. There is no random input, optimizer, tolerance, parent-code import or external coefficient file. The source reconstructs the cleared original determinant and root-plane identities, the whole unbounded-orthant certificate, the 23-leaf strict envelope bound, the continuous polygon first-wall reductions, five real body audits, two positive original volume fans per body and their own-centroid mechanical primitives. Its root-area calculation is independently checked by planar integration.

Normal build and verify both completed. A fresh source-only extraction through the final embedded recovery also completed and reproduced the same report. The final wrapper verification was observed after its final formatting change. The original parent audit was additionally executed once successfully; this is a new observed execution, not a claim that its previously unobserved historical receipt existed.

|Object|Bytes|SHA-256|
|---|---:|---|
|recover_unequal_fan_root_v1.py|9329|24451e05e650f276f6d360135761144f92401e483b604bee2ae3a63d37c92571|
|Complete decoded unequal_fan_root_v1.py|16754|49d3a52c703b531e7559d548d75f434fa4942021cf745a8185b94686682c6549|
|Complete new exact report|978620|acfacc2c0885960cee4a7cf75ae3627a4cb2c00abc8f6763f8cdc33064d5cd2b|

Save the complete wrapper below as recover_unequal_fan_root_v1.py, UTF-8/LF with one final LF. In a clean directory run

    python -S recover_unequal_fan_root_v1.py sources work
    python -S recover_unequal_fan_root_v1.py build work
    python -S recover_unequal_fan_root_v1.py verify work

The wrapper uses only the standard library; its child is deliberately launched without -S so that the pinned SymPy is available. Observed markers were

    UNEQUAL_FAN_SOURCE
    UNEQUAL_FAN_ORIGINAL_MOMENTS_AND_ALL_ORTHANTS_PASS
    UNEQUAL_FAN_ROOT_203_RECOVERY_PASS
    UNEQUAL_ENDPOINT_FAN_SELF_CONTAINED_RECOVERY_PASS

The ordinary certificate statistics were 4319 tensors, 35765 positive and 1533 zero coefficients, plus two special tensors with 50 coefficient-polynomial rows. The direct H certificate has 23 leaves and 457 positive/three zero coefficients. These are exact computational checks supporting the mathematical reductions above, not a proof-assistant formalization.

Convenience copies are the complete recovery (`recover_unequal_fan_root_v1.py`), the decoded readable source (`unequal_fan_root_v1.py`) and all exact certificates and actual-body data (`unequal_fan_root_v1.json`). They are not required: the following capsule contains every source byte, input and reconstruction rule for the new result.

### Complete autonomous source

```python
# UNEQUAL_ENDPOINT_APEX_FAN_ROOT_BOUND_203_V1 complete recovery.
# Parent minimum-0146, SHA256
# 343b1c30bfa2f3d225bf9cc2ab1675beee4c784a2e88659a18aa45e6509d390f.
# CPython 3.13.5; child uses SymPy 1.14.0; no external inputs.
import base64,zlib,hashlib,subprocess,sys
from pathlib import Path
assert __debug__
SOURCE_PIN=(16754, '49d3a52c703b531e7559d548d75f434fa4942021cf745a8185b94686682c6549')
REPORT_PIN=(978620,'acfacc2c0885960cee4a7cf75ae3627a4cb2c00abc8f6763f8cdc33064d5cd2b')
BLOB='''
c-o~q`*RvO(!cw!;Ogp%(I9LFY;OWqs_ad2S#RRttnEBFjvAN&#vX?83}8qq|NGYuX&yk5+V3{CgVbuZq*lMwlK)w`y?S+hd
;WIt>gr|p{U291gY)jIPlMOzSA!4l-`@-_-rrum95frP!JTvP&q~)#{Akgxxanl@VNySxOg3}>Jbb);IDI`ErNPa`(<Pw&_2
#^Ja$0E}w}#HB)fkT5=D6iGn<vBZ^U<j34xQ8APKLhkACG=}cI-C&XU|Sgp1aO7*F8S*Pfr@pz1H)_7%2VT-7Kc_sM0!gT8A
f{%3qsVcT;f=o#Vqsr{b^O(W2re!D2e|7r{uv#8N+51oJ4Bm1ti1aP{xQgK;vSRmKURBD@mJ;(4;Dyw(8dQhCid!2<fu=V69
3n$Lzo<WfIInYoK;v6Z1QK*L~Y8oE$D(B-L{Vw1d2=aEb|=>gBMG8lONa5)(a4h}qjT=C`$%audXt|b0qnM9RzIkT*_y{U}n
No6fJl_08o4PrtP^0n0vf;y(lVY%aC8Hc{LuJ7;3eMT;zjHJ8WYh<sv7xr-(d6dl4v^<36_ME;w>^1v!7d}vO`cjt~2y1Yw)
FlUD4!1H<&!^?eQBIUOz@uRUBf2X;aVNgjl}~;!nJ!XwHIIDJKB&Nd2Go0PIihceeq?n;B^aBAN|06%z2b+dZ-CUZv}$DalO
6Z&`?UBc85@@AF0w1c5n*v%5Z*mvC2j<>qmglOhQaf2<+rS4{*=mOn(FC}K(bUAqzema+t?~Zr{XE(hK;RI)8gS3r)ePq(2<
CPyr$n~UmST7o2c68%M4|=$@Ik89C?C;Zn_M^rWJU&K%U|}@%%)kAh^C~rO+Q5g?#WgDs*Q<&#eS)SZL5klJpBC16VZnMT$6
GE0Fi{K@-IPXrmSM`^pUdij31(BEvFk%|uAp*2svCs9TvB5!~QpBTwCM3^RT#j5}X0RIi^^ap(Yt2CN*3<Y*d%eg!uXx`-D}
#f>~(3e<ab5M=tLwVtU)8z~>g^Vkw4G6;3!*pECb*jX1e7Ppk9OWYQ{Hc+nRfL<E`49@qdWtlzF5`xpk9Rk@@ibbEA$L`2a)
wk~l*_x5jxbC7gvkHO>_M}x{TclVC(Xw<wDQKgG<m!X2=IaA>i{@a2qm31THjn1fB8ZlL)(+wgnjLYsP9+Uhj{&i$do)2(w{
E{kaTdVhLUGnOo4IQ&?IDb4-1q{vBvNeE>W+*^sp=jNR$tK|E86)mA7vh?o^Fz4@BC;v17oxBkt9-IE7i#Hy<{FM9FRHJDyh
Y)?G95b>aF^y(e4^{pjQ~zbU~`Ce<&oC6OLomV?z`}|GX1Y5qlXl+9+0Ca4B(I+6rWCar;Ia&=}k^C^Y)nHbSjg1Pfr=8E|p
5IZS*oxv5`}?R4QL3k6L<<oRn0_hz)gb;3Nf-`MmBsok$Zu}$TEPJl%65QG(k*<FSUOWR#GGe}FqS4PqkMH%kV4~QHwfkaq$
p$5^10Kl8%!mbtLTR`|s5IYfeuKuIVccoBsN-7{SeHjPYY|3K6qZaHMkLQM=WhDAc6-8QXqw1*z>|t`s?6nLLr93@DU`^S4$
$R6PV1~H2n&V(E+RTg}vKb97EK~OS!dR)XHdBR#AUDP-OrgoVNNJ)(c;$vmKedF|wnAM|#~;EHHKIVA0wUVvjpiUzzDH}y84
bSWCuWIhluZ-5Od}TLeDYldVkHYgK9yXoLW{j)Jyxpdq;s0hEt)0m%C~xzZS|I%Q9z^Dd+2(ewJPx|=Y?Y9t>ry}b%8w3<}-
+|Q{%RfegX~v{bd#j37H2)5cvc(N90p3$u#KoPoxzHi?jV}$U5CAj5IryON_A^5M#AK>-{iHw;k&ig|dI$ik2LS^8?wgJEDw
8Z1z%Rky%0kzvpkwLEpiFL=Qd54>msA-FZk+6-URoQZjtQyf~twI6BQjF6i^3u|w&url4U5oLMAe+S`>&uvCO>TR<8sE`Emi
8No*!9q*7KUK(|zNDTTHoU4|H4C79+PG1VNzbH0Y6O1W|Tv<Ui1z@LArtC1o?&PJ)n~Twj7mOBGJP%M5yOOOjeI*-QZBkg{2
{zCsn?OCE_s1`oY{u=&T}}>G{%A2zl$KhV+Y(u{19uANdnqT{=d6$J^0UgNkfcNS(ZOvTx{;e?QB&qK%Yjc9*m%7yQlkxX<G
d{Wbn40#GnS9W7+=e4GR4<yiL*6+RWY7`9x-%{@dWe;)lTKSroJ9E4}PE?O_HU1kfpD-g{P9*BYZ$oi`#mxMOAOuc_tU~`ry
DEv6|+L_5X~m=>V4a?trC)d8wK5iGM!R&%riBx)53*L%JD5_OpUH(fOp;+Q79oaIKxs8ss3z;pJzGwLZzuA`6XqUftrcrHe|
C9Sc|nrfjov_e}eg$Np0j`4i`+6!%Xl>W?YvpXMR|)My<AUnZnKC<XW3Vqo7b1@&}93<D1$zIh0S6Q_qIl2C$)4yF`T56duV
p5#rk^l{GP#P?P22cZP@Mqh>8e9@o<As2NKPqDBZvH&`AM{-6&a8ztj2*eGF6NMCe0nED-`CK8N^DpEXjn?mYfwCgRug3`*Z
YVoccF2F?K)Cr{fIA%F?nBY(L&S+a>jal|f+0TgX9jN4T4bWzi;>FxKUBbnc@~xhlawST3nr=$=X?3m*Tg4FH}O(q8_W=^f^
6hrIE_RjNT<&16a8ARpk9Ov#r?w1?lFttCk>@X=Y5_yrcNuyOa_>CW4s~Mo;1V@g~|@{rVvnHA6c9FT5RWcCJi}pXzMp;>x=
~SB2#e=#<Qr)JbJWVu+Y)qfD2=vJMz*g;Q|(Ji!nWpQs<d4Mc~=&OQ#g28#@LQ&r$Yc9F!tS9Ox{Qs|sKf!+$Et`KD#PQFxI
u=@dXonKG3{(rh9Zegrnd@*s4XX{&8yp-1_*k^S1j@DyTaS4b*FP!a}wFNYdDqvYC7h(LKWNxSbI1`B@%@iPUIXCTP9is6~M
H|e~}PhzGSXk33g%!?4nO9>)~2^Rysq8nLU6NzWJSG(kVhUIa}F&TyZDqFjqE!QR%!GT-Yw&m7_^`L&Qn_U^`(hv?E_6-Ks_
x-&=RAD);iDV1w9s+D1e@x6qlT+T|1dKj2yP-E1hL7DONaxXDgel>1FhV<^SEsYH>1Gyhm`Rw&rRpI{NP3tA(IiU*V`V>@H=
nsdo>jiSE_!K391QS84ab|oK&dL{uB(LhL0-tNyq3Nk%cWc?9LB1aU{!g2%}f8HE^6J{b?4=|a%vWoggx%OyvQnk=SF?8U!L
19F9`pQvMzvow&l}z4ByV5%5rKx)STLwzFm7<yS9BE;dZJlpm0%Y7Lq{MHuoIM4~Jj<WX?VAxW~EO)qQ+P)oc``UFz`>de9t
ohpx<O(BnF<UFaRZfDTMR(~&o&0M~^1w^MmB<=Fl%FMgyVoB{u|Z|s|5zuPIgq`N74s$2YG8KdMc_MaLvvn)s)h<=>zo~Pc}
H}xW)(O4P4m;o@rMR6AZ)P!*wI>w~IJHIO$o?us>lm#T3g1J)jH9weTjPkjFG8VOQ0Y&d-v{YB0Y+7dR>a)$mL@NZ|8Q>iQ9
})P`06$L63E{0eul-&FhSdH9!u6%C53{e-xqbDy_Pc%c30v*LWc7S9{34Y4zJtCN40ltDmI6pvFd~#!f+<ByDw|R*dPFj|)v
}|<+7hAl=uy-F60NYLrQ~fxeW}riomUOT^U(kv)c~!g{l&JMHTXeoGQ>%RYOqbq+RD%*_wlY_zqMc0-!|-54g1}8>Vuq#QqJ
k=@iTT%066sg33wnd^-5W%@)`U)fq%#HnCYgmKMLFs5B$q?Co3|BFq(zVI+jf#t(J6(=lC=>`L0YvpV-6D*xJdIZ8(O5PrY#
rQpX`KW&r?lk7BrOa!<%Z-BWCc)1V27Jty@v?g5R*7^0)6-U)qA`+YbNq>IEFK_r2zqZ~;5w37;>^fl(XoM&6<okE^-?vKaY
nFg;o)AFQZPko~_S9`?Xmp4Kph*^}zMK8?Fm~JbPnYjz49ck>*wsp$x6%eFpp*fn^0vg1@54_v<WOul}%V1aah<wlMvj^Q}z
^+p*gpO{n-RfiX$a~&9?(a!(ctJW!)Ui$XcZdUrzg8bq<VTdT8EN8Fu<r}COB8p~Folu{lsZ<lIWnF<fj?BPd|bL71n0qMK!
gIAvl}f2GdGz8ks?^Z?Q69ukp-7K#V%nG`ED{;fx~x)p|3z@O%n!#dBbBYNy_;0jc8Aj`7$ounEYI!NSTawpoq7bLNW6Ss?Y
|F`1W0(ik!5IYC(ipk|^mH&(mNLtbB#eP4iOE!Yd?D^dNdVrTZGZl?aLnVo!8t1iddq5B7*SM~ZtSoEvg+4xx`eBLVl2AYc{
lIOb3N;<*L!MNu})I%{+&SiNZEeF?XN>(`COEaj~k8O^!9VxT1pImad#j-{{$Nm>+)0?MtTk{SaK=&<Bu1{(o;CiM=Lgg~>u
C<|g=vMeW6C`+@?`d1p;uYYCnl4TL3pbM!Yf=nv&F(A$!Xh*Uc7>d}W%Z1iVm`q_e;g(&1nLZ?U6j|w6Wn(lm2r118M&T4(5
8c#9o%>a2jgKq%#(gLg1uC+c4d-EMRfm<Nsy6|^U09;kY_u?F7}|-Q2rhBC-fT2<T^J0zCF<$n2f8(IL(7p)qtW12IF2;oT%
Hv6Sbdw#qc$GecyFNwGC?YSNQ}0`_YO#kinZ?^&^3K_h$bllXWlX{9C?uVATF>~ARLK5S`;+W+xF0G_guCqFrWQidh2u?)b^
#v*UGi^k@P{>I50$Q7|GgJPzQ)*KoE82t-zCqy~nRGAMbwec(k70gADuTlm%sdBCD-!eGCruR2)5(`+8`m;^b3t^i;y_%W;0
~04gwg07bMcoo&UVU!e?VJ6WxYekb(Zm7hfloE)Rhg_|N64~#&(m`ci|Q8Op-I-c6zy3US0+`f!n@3VVrZTHa3Z3SFEu%>$I
CF4c&!;i$dz*c~pqUrBit<KIhR(1%2m7X>83kENkDFXhh*$L&82=)Nj@5};ESz&D|wldIxx0V5Cyg;2SK$BDCe?wZKgqqk60
Y|`hkKeN}6A3_rs9@D$j+@&FeNT)Sg7>B7(9YD*=EB%n&<!xy+PGK6QnjBS!kBfu=l&Y(5^SI9RYC8o621<89bI#>x})ok)5
uGv&EbN^$xt#3CvPHDs%bPt$_tJz7z~YX>RBJhpdv!Qc%0ycE3-0YM&geHd`$2y?zMvgF9><xtseyH-^*uLL!(`|0E}y^ViS
gP29yzIQK-_itK~Z-^WLLGe`|6gOVWYv%BF4W*=?i20pK7HFV@@JT~s@eiK0qq*)U32VkYr|DPSI8X03I&vCaYt2Ae=5hohZ
uf}ub8O}502pVzTzl^o4~n@22g+92rx*+owL`OIG=z$G_vp#*`6R-i1u14<oRuVn$jIGhWe<m~F-YyIn+V18^Ot6ye?IJ2Xy
QcmaS<+;o<I#|gwY<J4ak~v2&FJvi|gMb|MqoLY8`l9i!xpX0pzLc1EEAQk-=^Rm;^p6Nzj*mDmaKIUVOg0Z-H)hMwEwD{e1
jM{!Izu^<p4!LZ&c#Yu*<~I3jZU-%b_{EyPPCx{E7$&v_}2Z}eRhp}D=$_$y_A(cVkzr$ulsl_bxXM=N-a@l39nN0y}5-D+2
ctHyCo^-FS9uddD|DosLk?LMRec*v|C8B2)-+LN~Y7-VJgOIm#UY)U$m`@6<$hnZvCNPR=_C=@C(QM4w8^1!01ktu9kQ2z4d
+QG7K;E#Vn17^zUu!Bc}e(Yp~{rejO{qzQimOOuqoY>%C(@KeuUOM^1Bh9F``$*UuO7!)YF!BDJFy`-(8cTlqSutOwGLGo>7
zQy-bCL)D?FHv2k(HdE0$>rsm~8TyW0xWgeppa?-;;F$2gyi!0!-r)DhI<@g}0Dy(ub6}n?2J6iL1yb=`a0Np-ga~~E;tAmj
H=dV3EW7G*&%HX#WI$v+R1H2`t9zqt{s>M?aN4lmXwB-XH{f&W&cE94Ot3bA!U`p4XvK1}`xXr}2E#CZcn7-e)%j(~gx-^Fy
$b<)bd_K2>&{En>-CE?JC9o+q7MgT2qb)Z6w`U~-3QK>byC;!LcjD>hQn-Y43V+96oXOeEkU&}b#b6)QB3916U9|8=#y5j@Y
TtRUO9G#L)~_7+5&95FTQ{r5eiMVH)b@hJoKf33Jg1Qw1*<v*q}WWse(&Wc%wnKPITfWjBLUwm+JRfeK-`rJRoEMBdR}S^}^
9#b2E#~3QWV)Ncm+ay>|rQS);A_oj+E==VW_vwTo(K$6SsY7s@@t+aj1T37a+=^q4roOI&($3dOnxu^c5OTR?KanMI_r$4&d
F9jf|Am07FkD~%-S-%M#BR>kB{cBifbj{NrcaVg5|=*wmF%U<zruWUpuz4}+;f(H7<jm|hANJu=F4`R%X;b}fqrKkn(pG|PY
ODdmBw6eQPFIfD*p;D5Yf_V0SzjCnrn8uCfU_3B~&D*B~nPPZn!N~#s(Fvj<9r|^s?hxE0QNThOD(DYt^h~7SFlzK#q~I|2_
=b|n(2sZGg??<00&$4<b`Sn0wX&(#aAXjrH;SKE1HS0IQ@@BpN<k)Alsh&omtapIZhXgpcMQnZM}}Kc>3+T8!e}!B+0l=bdi
f)R!deioUw%Dkh$#hQ6n%z1OBg7{HR<CLe!Xg6WiZ=r+LlR@)Yt`b!NY<$GHtum$m7fd4@Lxv<_%WXUKBiD=g!+wy2n?Ai~O
wIq;kHA3oU0pcpnI4y}G_wt68JEzEZ1M!@9moD|Ia8ApMmv_iWoQaJQa(1EzWM{awLv3k)Q`c8<3;r1aGIhmUaZZ$$JP9DGE
sR1bx}+5dZ;onq%!9?hW#Q<1;M2f_s}yX9uhgH@o%4_l4Z&~MyCE}(ypppQ;)Ke57YJKXSda?ozBnaskZnUE&==5QH%$d`AZ
tEQZ*CF}UkK}xWe6+$KQ0h`PKQ!^%M0(`fKH3^Z~09>24!W@>f_mx?=q>6!4Y0a>(n`-~;HRdrf8(DHnZ_Jwn)S)oT{K14%R
kWa1wT0*HBTgF}ozV9=eUGaqMe-vP4fZQCe~|Fhw&=(s>?hJ2I`&}2DVp8<=ut|vW#wae!Zim9k`D5w-sHM&Kj!w#s&mebp1
2Wft;o6+^~m}NfuVKBC9u8t8anYxF&u7^$qp3mT)eg73_K}iVcr-<fCuA8YTmjH4g`yBDEAHhENn7<P#g2o{`C@&O#K#Brxr
NqU>c}~mII3Tn|uySelDF8`3wrrq|=hWiT<|uC*%s0(%mr)ivTis(1s_3?Pi7<jIwnvW0u=?=DMScF3aX{NWUg@$R4ceZqf|
lv`rv7hEqeB4PAH4*hRgnW+s=he=Sz6-{gsII|1e$mqf>0EvS6A@EWsb6;8-BP<HM%J!o++N|U|OelbtEAid5~nUUdqW9HM*
sT3oM=>PxLqk$vK(oYVcN9hSdS<*`LRZ0&<7*jaQl2L%wwphb3!_@d$@dQgE>#q4`D9K;$#)&-DdjSQLIw;N;NilE1xB=Uo<
_Wil7?lG5oK~yRY{=7-lhfzfu4KK=2yG`sC+lEDi^E)Fd<U5fn1V!V5C+d<KT%lTbAr})L4(wPT>23>G#chYp-Jtks?+#yeO
8s%S;@~zV^wY1y1Z1?lcUqBT<Kq4BYjOc4S|~*S!;9MHLe6{fQJDX(^|{d*_&0&Y_G*$B%E4?_YDyrM4RcZbbu=<0lPL=Mc?
<*;k>#;A1Ly-vL!-Hrj)T*9~=Oo!5{)}NpI2y1AN3b7*u!v!f*rDGnrr<)#8k<2H+pxP=a{43_=e)6!_9$yr~+uhj)PbCexj
$>fiV?^J=!YG5xi<s{ZV+&8w2J2I<soo}9vN|Bruko)4eDAXGnkOel9Gb*tU@XO+8t%^??#_xMNQhu(4)!?}d^jQJ)c9svh<
UQzhyTc$pSHVeFxwSd*K+J<1DR{c*@6^9_|bI<&_9{FAT^Yd)u@Na>Q=oI!2Hk~)FO>bkL5)iY&aI^67Pq6fB9eilrF5FHWg
17NB637GK@wMH2nSi#@sDr^c2tlSq30L1`fM#2nAmG;j_5Sw5@2{%#XC6#NNd5QnhrFEzd^q*jUNG_TQuc@B-hcSx-+x>|<=
y*tudZ(X8k~bnoxgnx4L5Jj5zsyV>#wS0CgWv-+0-hyiu?lJ9NqQ|LBfh+`r*~@@9$oH_^e6d3XpHx(??i&?*9iW$#J{
'''
def checked(raw,pin):
    assert (len(raw),hashlib.sha256(raw).hexdigest())==pin
if __name__=='__main__':
    assert len(sys.argv)==3 and sys.argv[1] in ('sources','build','verify')
    mode=sys.argv[1];folder=Path(sys.argv[2]).resolve();folder.mkdir(parents=True,exist_ok=True)
    raw=zlib.decompress(base64.b85decode(''.join(BLOB.split())));checked(raw,SOURCE_PIN)
    source=folder/'unequal_fan_root_v1.py'
    if source.exists():assert source.read_bytes()==raw
    else:source.write_bytes(raw)
    if mode!='sources':
        report=folder/'unequal_fan_root_v1.json'
        subprocess.run([sys.executable,str(source),mode,str(report)],check=True)
        checked(report.read_bytes(),REPORT_PIN)
    print('UNEQUAL_ENDPOINT_FAN_SELF_CONTAINED_RECOVERY_PASS',mode)
```
