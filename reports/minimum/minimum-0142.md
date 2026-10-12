# minimum-0142

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# HIGH_TRACE_VARIABLE_ENDPOINT_LOCALIZATION_16_V1

## 1. Main result and its precise scope

**The high-trace attainment/localization bridge can be completed for the original adjacent-triangular-facet polytope problem.** Relative to the accepted balanced proper-pair exclusion and the immutable arbitrary-body local-maximum proof, the following is proved.

**Global counterexample-localization theorem.** Suppose an actual uniformly filled convex three-polytope has two genuine adjacent maximal triangular facets and original trace `T0 >= 51/25`. Then there is a uniformly filled convex three-polytope with two genuine adjacent maximal triangular facets, a genuine positive-area root facet, **at most sixteen true vertices**, and original trace at least `T0`. Endpoint values and the rest of the body may change. No bound on the original number of positive-ell auxiliary vertices is assumed.

Moreover, the global variable-endpoint marked support-patch problem has a genuine positive-root polyhedral maximizer of trace `M >= T0`. A maximizer can be selected with unequal positive common-edge endpoint values and at most sixteen true vertices. Its coordinate support facets are allowed to be larger than the marked triangles. This last distinction is not suppressed: attainment in the proper-triangle subclass is not asserted when `M > T0`. Instead, proper polytopes with at most sixteen vertices approach M, and one already has trace greater than T0.

The weak threshold is covered without using an invalid limit of strict inequalities. If `M=T0`, the original proper counterexample is itself a global marked-class maximizer and the local-structure theorem applies to it directly. If `M>T0`, strict improvement makes proper-patch resolution legitimate.

The new boundary mechanisms are:

1. A closed, arbitrary-body endpoint inequality forces both common-edge endpoint values to stay positive at high trace.
2. The coordinator's root shave extends to a complete first-variation formula even when the root already has positive area. At a joint maximum this gives a strictly positive integral of the frozen variation density on the root.
3. That root integral supplies exactly the missing hypothesis for extending the accepted arbitrary-body proof to roots containing C and/or D. The resulting vertex bounds are **16, 13, and 12** when respectively zero, one, or two of C,D lie on the root.
4. The canonical-incidence penalties pay for every redundant mark introduced during proper-patch resolution. The proper resolution therefore also has at most sixteen vertices, rather than a naive twenty or eighteen.

Thus, for the original polytope problem, proving `T<51/25` universally is equivalent to proving it for genuine adjacent-triangle pairs on polytopes with at most sixteen true vertices. **The trace-value inequality itself is not proved here.** No E17 exclusion, mechanical attainer, equilibrium-preserving surgery, or change to `34 <= C_min <= 622` follows from this localization alone.

## 2. Optimization class and inherited premises

Use the fixed affine frame

    A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
    Tetra=conv(A,B,C,D).

For nonnegative endpoint values a,b,c,d, not all zero, put

    ell=a+(d-a)x+(c-a)y+(b-a)z,
    n=(a+b+c)x+(a+b+d)y.

The variable-endpoint marked class K consists of every compact, full-dimensional convex body P such that

    Tetra subset P subset {x>=0,y>=0},
    ell>=0 on P,
    a+b+c+d=1.

Initially impose **no condition at all on the zero set of ell**: it may be empty, a point, a segment, or a positive-area face. Nor must C,D remain vertices, nor must the coordinate support faces equal their marked triangles. This is the closed relaxation actually used for attainment.

Every integral is over the original uniformly filled P:

    V=int_P 1,
    J=(X,Y,Z)=int_P (x,y,z),
    E=int_P ell,
    N=int_P n,
    mu=E/V,
    T=N/(6VE).

The true volume centroid is `J/V`; it is never an independently chosen parameter. Scaling ell and n by the same positive number leaves T unchanged, so endpoint-sum normalization loses no original counterexample.

The proper subclass has exactly

    P intersect {x=0}=ABC,
    P intersect {y=0}=ABD,

and a positive-area root. Those equalities make the two triangles genuine maximal facets and AB their genuine common edge.

The two selected original proofs give the cone-tail concentration and the joint mass inequality in the extended fixed-patch setting. The latter explicitly permits larger coordinate facets and redundant canonical marks. Its proof is for compact convex bodies, not only polytopes.

The inherited local proof is `ALL_BODY_POLYHEDRAL_FREE_BOUNDARY_V1`, parent `minimum-0139`, advertised assignment SHA-256 `c58993f6099c9026b8aece0f2dcedf5b45aed4f8c933eacc92d639040f2c8a2f`. Its exact original scope is fixed `0<b<1,c,d>0`, positive root area, and local maximality against all nearby admissible convex bodies. It proves polyhedrality before applying the sixteen-vertex count.

One further accepted notebook premise is used, in its **minimal needed scope**:

> A proper adjacent-triangle POLYTOPE with a=b has T<51/25.

This is the balanced proper-pair exclusion recorded in the shared notebook. We do not assume a strict balanced bound on arbitrary marked-patch limits. The argument in Section 8 deliberately avoids needing that stronger statement. The full balanced proof source is not one of the newly selected attachments; its accepted statement, rather than an invented reconstruction of its certificates, is the inherited premise here.

## 3. High-trace compactness, including closed endpoint faces

### 3.1 The selected cones really are the marked triangle cones

The two fixed-patch cone masses at the true centroid are

    m_x=X/(2V^2), m_y=Y/(2V^2), m=m_x+m_y,
    h=1/(6V).

Their normalized ell-traces are

    lambda_x=m_x(a+b+c)/(3mu),
    lambda_y=m_y(a+b+d)/(3mu),
    lambda_x+lambda_y=T.

These formulas concern the actual triangles ABC and ABD, not their possibly larger containing facets. The pyramids from the true interior centroid over those two triangles lie in P and have disjoint interiors. Each radial ray from the centroid has a unique boundary exit, so the same disjointness remains valid for nonsmooth P and for proper subpatches of larger support faces.

Normalize ell temporarily by mu. The exact radial density in each such cone is `3r^2`, and Jensen on the actual selected boundary patches gives the same lower tail expression as in the selected proof:

    (m/3) K(T/m,t) <= E_P[(ell/mu-t)_+],
    K(z,t)=int_0^1 3r^2(1+r(z-1)-t)_+ dr.

The supplied Brunn-Minkowski argument gives the upper bound

    E_P[(ell/mu-t)_+] <= (1-t/4)_+^4

for any convex body. No facet enumeration is needed for this upper bound.

At `t=11/8`, the monotonicity argument at `m=13/15,T=51/25` has the exact positive gap

    29035697/279130931200.

Consequently the same strict mass conclusion holds for every member of K with high trace:

    T>=51/25  implies  m>13/15.

The extended joint mass theorem gives

    m<=3(1+h)/4,

hence

    h>7/45,   6V<45/7,   V<15/14.                     (C1)

The quoted rational gap and the conversion from mass to h are proved in the supplied tail source; the only extension made above is the explicitly justified use of the two fixed support patches instead of whole selected facets.

Also `h<=1`, because Tetra is retained, and therefore

    m<=3/2.                                           (C2)

### 3.2 A closed common-edge endpoint inequality

For every P in K, including arbitrary convex bodies and redundant C,D,

    ell(p)/mu >= 4(T-2)  for every p in AB.             (C3)

Here is a proof using actual boundary integrals. First take a polytope, put its own centroid at the origin, and let F_i have outward unit normal nu_i and distance h_i>0. Define its normalized support slack and ell-weighted boundary mass by

    Y_i(p)=1-nu_i.p/h_i,
    lambda_i=(area(F_i) h_i/V) mean_Fi(ell/mu).

Divergence for the affine function ell, or direct tetrahedral integration, gives

    sum_i lambda_i=3,
    sum_i lambda_i Y_i(p)=4-ell(p)/mu.                 (C4)

For example, the second identity follows from

    int_boundary ell nu dA = V grad ell,
    int_boundary h ell dA = 3E.

Every Y_i is nonnegative on P and has true volume mean one. The maximum-at-most-four consequence of the same Brunn-Minkowski tail proof gives `Y_i<=4` throughout P.

Split the boundary measure in (C4) into the two selected fixed triangles and its nonnegative remainder. At p in AB the selected slacks are both zero. The selected mass is exactly T, even when it is only part of a larger coordinate facet. Thus

    4-ell(p)/mu <= 4(3-T),

which is (C3).

For a general convex body, inscribe finite polytopes containing all four marks and converging to P. The same inequalities hold on every approximant with the fixed triangles still contained in their coordinate faces. Uniform volume and first-moment convergence passes (C3) to the limit. This approximation transfers a universal integral inequality; no local-maximum theorem is applied to an approximant.

In particular,

    min(a,b) >= 4mu(T-2).                              (C5)

Thus a=0 and b=0 are impossible already at T>2. Since `max(a,b)<=4mu`, one also obtains the closed relative bound

    min(a,b)/max(a,b) >= T-2.

On the high-trace endpoint-sum normalization,

    E>=int_Tetra ell=1/24,
    mu>=7/180,
    min(a,b)>=7/1125.                                 (C6)

These bounds include the equality threshold T=51/25. They require neither a prescribed root face nor a maximum assumption.

### 3.3 The actual compact set

For every point R=(x,y,z) in a body containing Tetra in the quadrant,

    6 Vol(conv(Tetra,R))
      =1+(-z)_+ +(x+y+z-1)_+ <=6V.

It follows that

    0<=x,y,  x+y<=6V,
    1-6V<=z<=6V.

This is the exact pointwise container calculation in the supplied joint-mass proof.

Let

    H={x,y>=0, x+y<=45/7, -38/7<=z<=45/7}.

Consider all pairs (P,ell) with `Tetra subset P subset H`, `V<=15/14`, normalized nonnegative endpoints, ell>=0 on P, and T>=51/25. This is a closed Hausdorff/Euclidean-parameter compact set. One direct proof uses uniformly bounded, equi-Lipschitz support functions and a convergent subsequence. The retained full-dimensional Tetra prevents dimensional collapse. On the common bounded container, Hausdorff convergence of convex bodies gives convergence of V and J; uniform convergence of the affine coefficients then gives convergence of E and N. In particular,

    V>=1/6, E>=1/24, N>=1/24,

so no denominator can vanish.

Canonical containment is closed; being a canonical vertex is deliberately not required to be closed. Root area is likewise not assumed continuous or positive at this stage: the class allows all root degenerations, including no contact at all.

If an original counterexample exists, this compact high-trace set is nonempty and T has a maximum M on it. It is also a global maximum on the entire, unbounded-volume class K: every pair with trace at least 51/25 was already shown to belong to the compact set, and every other pair has trace below M. Thus the container does not artificially restrict any improving variation at a maximum.

## 4. Root shave with all four actual integral changes

This completes and extends the coordinator's supplied collapsed-root calculation. It is a variable-endpoint, actual-body variation, not a fixed-ell ascent.

Relabel A,B if necessary so a>=b>0. The relabeling is the genuine affine involution

    R(x,y,z)=(x,y,1-x-y-z).

It swaps A,B and fixes C,D. Its determinant has absolute value one. It sends J to `(X,Y,V-X-Y-Z)`, leaves V unchanged, and, with ell transported and a,b exchanged, leaves E,N,T unchanged. This is affine transport of a uniform body, not projective transport of a centroid.

Set

    z_c=1 if c=0, otherwise 0,
    z_d=1 if d=0, otherwise 0,
    s_C=1-z_c epsilon/a,
    s_D=1-z_d epsilon/a.

Take epsilon>0 smaller than a,b and every positive one of c,d. Cut the actual body at

    P_minus=P intersect {ell>=epsilon}.

Keep A,B. Replace C by `C_e=s_C C` only when c=0, and D by `D_e=s_D D` only when d=0. In the zero cases,

    ell(C_e)=epsilon, ell(D_e)=epsilon.

Every retained mark lies in P_minus. Their convex hull is a nondegenerate tetrahedron of determinant factor `s_C s_D>0`. The triangles ABC_e and ABD_e are genuine contained support patches of P_minus, regardless of whether they are whole coordinate facets.

Normalize that tetrahedron by the actual linear map

    Phi_e(x,y,z)=(x/s_D,y/s_C,z),
    j_e=1/(s_C s_D).

On the new body use `ell_e=(ell-epsilon) composed with Phi_e^{-1}`. Its endpoint values before optional sum normalization are

    a_e=a-epsilon, b_e=b-epsilon,
    c_e=0 if c=0, otherwise c-epsilon,
    d_e=0 if d=0, otherwise d-epsilon.

Let `R_e=P minus P_minus`, and define actual lost integrals

    w=int_Re 1, J_R=int_Re (x,y,z), E_R=int_Re ell.

Put `V_minus=V-w`, `J_minus=J-J_R=(X_minus,Y_minus,Z_minus)`, and `E_minus=E-E_R`. The original uniform integrals of the normalized new body are EXACTLY

    V_e=j_e V_minus,
    J_e=j_e Phi_e J_minus,
    E_e=j_e(E_minus-epsilon V_minus),
    N_e=j_e[(a_e+b_e+c_e) X_minus/s_D
            +(a_e+b_e+d_e) Y_minus/s_C].              (S1)

Its actual centroid is `J_e/V_e`. In particular, the numerator is not obtained by pretending that the old n was transported unchanged: changing the marked triangle changes its coefficient and its area.

After cancellation, the exact trace is

    T_e = [k_x(epsilon) X_minus+k_y(epsilon) Y_minus]
          /[6 V_minus(E_minus-epsilon V_minus)],      (S2)

where

    k_x=s_C(a_e+b_e+c_e)
       =a+b+c-[3+(b/a)z_c]epsilon+(2/a)z_c epsilon^2,
    k_y=s_D(a_e+b_e+d_e)
       =a+b+d-[3+(b/a)z_d]epsilon+(2/a)z_d epsilon^2.

Scaling the four new endpoint values to sum one changes neither (S2) nor the body. Hausdorff convergence also holds without regularity: for a fixed interior point u with ell(u)>0, put t=epsilon/ell(u). Then `(1-t)P+t u subset P_minus subset P`, so the cutting distance is O(epsilon); Phi_e tends to the identity. Thus the normalized pair converges to the original pair and is an admissible small variation in K, including at the closed faces c=0 and d=0.

### 4.1 Coarea, including singular or collapsed roots

If the minimum of ell is positive, the body is unchanged for small epsilon. All four endpoint values are then positive, and (S2) gives

    dT_e/depsilon at 0 = (T-m)/mu >0 at T>2.

Therefore a joint local maximum with T>2 must have a nonempty zero set F.

Such a high-trace affine function is nonconstant: for a constant ell one has T=m<=3/2. For nonconstant ell, translate the parallel sections `P intersect {ell=t}` into the plane ell=0. They converge in planar Hausdorff distance to F as t decreases to zero. Compactness gives the upper inclusion; segments from points of F to an interior point give the lower inclusion. Consequently their planar areas and first moments converge, even when F is a segment or point.

Write

    S_0=int_F 1/|grad ell| dA,
    S_J=int_F (x,y,z)/|grad ell| dA.

Coarea gives

    w=epsilon S_0+o(epsilon),
    J_R=epsilon S_J+o(epsilon),
    E_R=O(epsilon^2).                                 (S3)

If F has zero area, `w=o(epsilon)`, `J_R=o(epsilon)`, and `E_R=o(epsilon^2)`. Thus no curvature assumption, regular root outline, polyhedral tangent cone, or guessed cap exponent is being used. For every sufficiently small positive epsilon the new level section has positive area because it is an interior level of a full-dimensional convex body.

### 4.2 The complete root first variation

At the original pair freeze

    r=N/V, q=N/E, g=n-r-q ell,
    m_0=(z_c X+z_d Y)/(2V^2),
    G_F=int_F g/|grad ell| dA.

Equations (S1)-(S3) give

    dT_e/depsilon at 0
      =[T-m-(b/(3a))m_0]/mu - G_F/(6VE).             (S4)

On F, `g=n-r`, so every term in (S4) is an actual original volume or area integral. Since `0<=m_0<=m<=3/2` and `b/a<=1`,

    T-m-(b/(3a))m_0 >= T-2.                           (S5)

For a collapsed root, G_F=0 and (S4) is strictly positive at T>2. This excludes every collapsed-root joint local maximum, including collapse onto C, D, or CD.

For a positive-area root, local maximality instead gives the important quantitative sign

    G_F >= 6V^2[T-m-(b/(3a))m_0]
        >= 6V^2(T-2)>0.                              (S6)

**Therefore every joint local maximum in K with T>2 has a genuine positive-area root, and its frozen variation density has a strictly positive root integral.** Both assertions apply to the arbitrary-body global maximum obtained by compactness. This is stronger than merely declaring that a limiting support plane is a root facet.

## 5. Extending the arbitrary-body proof to zero C/D endpoints

### 5.1 Exact proof patch, not passage to a limit of local maxima

The following extension is sufficient and is proved by a precise modification of the immutable parent proof:

**Boundary extension lemma.** Fix `a>b>0,c,d>=0`. Let P be a Hausdorff local maximum of the fixed-endpoint marked positive-root problem. If `max_F g>0`, then P is a polytope. The independent coarse bound 162 from the parent remains valid.

To obtain the lemma, first divide ell and n by a. The only lost sign argument in the parent's analytic polyhedrality proof is the paragraph asserting that all root extreme points are noncanonical because all four endpoint values are positive. Replace that paragraph by:

    A point of F has g>0 by hypothesis, while g(A)=-r-qa<0.
    Therefore P straddles g=0. The root restriction g=n-r is
    nonconstant: grad ell has nonzero z component b-a,
    whereas grad n has zero z component and is nonzero.
    On each coordinate support plane, g(A)!=g(B).

The rest of the analytic proof needs these sign and nonconstancy facts, not positive values of ell at C,D. Here are the admissibility checks at the new boundary, so that this is not an unsupported theorem-by-continuity claim.

- Noncanonical extreme-point deletion still avoids all four marks and retains a nondegenerate root triangle away from the deleted neighborhood. It therefore proves `g>=0` at every noncanonical extreme point even when a canonical mark lies on the root.
- A good angular cone cap exposes a single ray. A positive-area protected face through its apex has a two-dimensional contact cone and cannot be this exposed ray. Thus a root-canonical apex does not invalidate the other-factor-inactivity argument. A root triangle can be chosen with directions strictly away from the exposed ray, and all other canonical directions retain their positive slack.
- For an ordinary facet through one root-canonical mark, the facet plane is still distinct from the root plane. There is a nondegenerate root triangle strictly on its retained side. It survives the inward angular-edge variations; outward variations contain the old body. The angular-edge integral and its endpoint o(epsilon) estimates are unchanged.
- The protected-plane level intersections are still lines, because g is nonconstant on every protected plane. Hence the good-generator countability, atomic surface-area argument, ordinary-triangle rigidity, and finite special/level accumulation argument have precisely the hypotheses they use in the parent.

In particular, none of the new zero-endpoint cases is treated by approximating it with fixed positive c,d local maxima. Such approximants need not be local maxima at all.

The parent then gives at most `4+2+2sl+binomial(s,3)<=162` extreme points, with `s<=9,l<=4`, and thus polyhedrality. Its exact cone-sector formulas, nonsmooth angular variations, and finite-extreme-point argument remain the accepted proof machinery.

At a joint maximum with T>2, (S6) supplies `max_F g>0`. Thus the extension covers all zero-C/D endpoint strata needed for the global problem.

### 5.2 Polyhedral lemmas remain valid at these endpoints

Once P is known polyhedral, the foundational local lemmas extend with the same fixed-root-plane variations. Small caps avoid all canonical marks; the thin-edge cap used to make noncanonical g strictly positive retains a root triangle away from that edge. Ordinary-facet tilts retain a root triangle strictly off the ordinary plane, including when their pivot is C or D on the root. Thus:

    every auxiliary true vertex has g>0;
    every ordinary facet is [X,v,w] with
         g(v)=g(w)=-g(X)/3>0;
    no facet is constant at a positive g-value;
    every auxiliary vertex lies on a special facet.

A special facet is the root or a facet containing at least two canonical marks. The coordinate facets are special and `3<=s<=9`. All these are statements about true facets and true vertices, not an input list or an integration triangulation.

Let Q be the intersection of its s special halfspaces. Each retained plane supports a genuine Q-facet because it contains the corresponding positive-area P-facet. Q is pointed: a lineality vector must have x=y=0 and `(b-a)z=0`.

An auxiliary vertex on exactly one special facet has no increasing g edge direction, because all its incident edges occur in ordinary triangles. It is therefore a global maximizer of g. The positive maximum face cannot be a facet and has at most two vertices. Write e for this number of exceptional auxiliary vertices, so `e<=2`. The same vertex-link argument as in the supplied sixteen-vertex proof makes an exception simple, with neighbors X,Y,w, where X,Y are distinct canonical vertices and

    g(v)=g(w)=h>0, g(X)=g(Y)=-3h.

These are precisely the local ingredients of the original skeleton argument.

### 5.3 Closed-endpoint incidence accounting

Let

    k=#{C,D lying on the root},
    t=number of unprotected special facets containing three marks,
    r_X=number of special facets containing canonical mark X,
    I_j=#{canonical marks with r_X=j},
    R=sum_X r_X.

The root has k canonical incidences, rather than zero. Thus the corrected identity is

    R=6+k+2(s-3)+t=2s+k+t.                            (V1)

A mark with `r_X>=3` is a Q-vertex, hence a true P-vertex, and its Q-degree is r_X. This does not assume that C,D were vertices initially. Let E_Q include finite edges and edge rays, and let Delta_Q be the degree excess over three at finite Q-vertices. Euler, with a transverse truncation when Q is unbounded, gives

    E_Q<=3s-6-Delta_Q,
    Delta_Q>=sum_{r_X>=3}(r_X-3).

Every Q-edge contains at most two true P-vertices. Counting their incidences and subtracting the extra incidences at the canonical Q-vertices gives

    v_skeleton<=2E_Q-sum_{r_X>=3}(r_X-1).

Outside the skeleton there are only the e exceptional auxiliary vertices and at most I_1 canonical true vertices. Since

    sum_{r_X>=3}(3r_X-7)=3R-28+4I_1+I_2,

one obtains the closed-endpoint formula

    v(P)<=16+e-3(k+t)-3I_1-I_2.                       (V2)

The new `-3k` term is important. The root may not be counted as having zero mark incidences after c or d has become zero.

For k=0 the supplied exceptional-ear argument gives `e>0 => t>=1`; hence v<=16. For k=2, (V2) already gives v<=12. For k=1, the coarse immediate bound would be 15, but the trace-flat ear improves it to 13, as follows.

### 5.4 The one-zero stratum has no exceptional vertices

At an exceptional v, move only v to

    v_u=v+u(Y-X)

for small positive or negative u. The fixed special plane through v,X,Y is preserved. Every other protected inequality at v is strict; if that special plane is itself the root, the motion stays in the root plane and its positive area persists. All other canonical marks are strictly off the two moving ordinary planes. Thus the motion remains admissible also with zero endpoint marks. We do not claim that the root outline is unchanged when its vertex moves.

Let eta be the volume of the simple-vertex ear tetrahedron `[v,X,Y,w]`. The exact uniform changes are

    V_u=V,
    J_u=J+eta u(Y-X)/4,
    E_u=E+eta u(ell(Y)-ell(X))/4,
    N_u=N+eta u(n(Y)-n(X))/4.

Since g(X)=g(Y), `N_u=q E_u`; the trace is exactly constant. Nearby points of this trace-flat segment are themselves local maxima. Put `Delta r=q(E_u-E)/V`. Ordinary-triangle rigidity at the moved maximum requires

    h-Delta r = -(-3h-Delta r)/3,

so Delta r=0. Therefore

    ell(X)=ell(Y), n(X)=n(Y).

With a>b>0, the only distinct canonical pair satisfying both equalities is C,D, and then c=d. This is the original exact ear mechanism, with the root-admissibility check above replacing the old statement that the root is unchanged.

Exactly one of c,d being zero makes c=d impossible. Therefore e=0 when k=1. Substitution in (V2) proves

    k=0: v(P)<=16,
    k=1: v(P)<=13,
    k=2: v(P)<=12.                                   (V3)

Consequently every joint local maximum in K with `T>2` and `a!=b` is a positive-root polytope satisfying (V3). The high-trace compactness theorem is what supplies an actual global maximum to which this statement can be applied.

## 6. Proper-patch resolution does not increase the sixteen-vertex budget

Let P be a positive-root marked body, and choose q in the relative interior of its root with q_x,q_y>0. Such a q exists because the root is a genuine two-dimensional face and cannot coincide with either coordinate plane when a,b>0.

For `0<rho<1`, set

    H_rho=rho P+(1-rho)q,
    K_rho=conv(Tetra,H_rho).

All points of H_rho have strictly positive x,y. Therefore

    K_rho intersect {x=0}=ABC,
    K_rho intersect {y=0}=ABD.

The root contains `rho F+(1-rho)q`, of area `rho^2 area(F)>0`, together with any zero-endpoint canonical marks. Thus its positive-area root is genuine, and its coordinate triangles and common edge are genuine. These facts do not depend on a face-lattice limit.

The actual uniform homothetic integrals are

    V_H=rho^3 V,
    J_H=rho^4 J+rho^3(1-rho)Vq,
    E_H=rho^4 E,
    N_H=rho^4 N+rho^3(1-rho)n(q)V.                     (P1)

Since `H_rho subset K_rho subset P`, the actual removed set `D_rho=P minus K_rho` gives

    (V_K,J_K,E_K,N_K)
      =(V,J,E,N)-int_Drho (1,p,ell,n).

Its volume is at most `(1-rho^3)V`, so all four integrals converge to the originals. In particular `centroid(K_rho)=J_K/V_K` converges to J/V; it is not held fixed. Because n and ell are nonnegative,

    T(K_rho)>=rho^4 T(P)
               +rho^3(1-rho)n(q)/(6E)
             >=rho^4 T(P).                            (P2)

This is a one-sided lower bound, not a monotonicity claim for root contraction. Given `T(P)>T0`, any rho sufficiently close to one with `rho^4 T(P)>T0` already yields `T(K_rho)>T0`.

For an arbitrary nonpolyhedral P, take finite inscribed approximants containing the four marks and three noncollinear root points, and apply this contraction. Let the approximation error and 1-rho tend to zero. This gives proper POLYTOPES with traces converging to T(P). Thus strict violations transfer to proper polytopes before polyhedrality of P is known.

Now assume P is one of the polyhedral maxima of Section 5. Let `v_c` count its canonical true vertices. The transformed image of a canonical vertex X lies strictly inside the segment from X to q, both of whose endpoints belong to K_rho. It is therefore not a true vertex of K_rho. No separate q vertex has to be added: q is already in H_rho and in the relative interior of its root. Hence

    v(K_rho)<=v(P)+4-v_c.                             (P3)

Every redundant canonical mark has `r_X<=2`, because a mark with r_X>=3 is already a true vertex of P. Therefore

    4-v_c<=I_1+I_2.

Combining this with (V2) gives

    v(K_rho)<=16+e-3(k+t)-2I_1.                       (P4)

For k=0 use the accepted `e>0 => t>=1`; for k=1 use e=0; for k=2 use e<=2. Consequently the proper resolutions satisfy the SAME respective bounds

    16, 13, 12.

This is a true-vertex count, not a count of labeled input points. Redundant C,D are explicitly paid for by the incidence terms; silently treating them as initial vertices would miss this step.

## 7. Equal-endpoint and equality-threshold boundaries

Let M be the arbitrary-body global marked maximum from Section 3. Section 4 has already proved that its root is positive-area and a,b>0, without requiring a!=b.

If `M>51/25`, no maximizer can have a=b. Otherwise the proper POLYTOPE density construction in Section 6 produces a proper balanced polytope of trace greater than 51/25, contradicting the accepted proper-pair balanced exclusion. This argument needs only a strict violation, and therefore assumes no uniform balanced gap on marked patches.

If `M=51/25` and an original proper polytope counterexample exists, its trace is exactly M. Select that original counterexample as the maximizer. Its endpoints cannot be equal by the same accepted proper-pair theorem. Thus an unequal-endpoint maximizer is available in this case too.

This selection argument is the reason the theorem includes `T>=51/25`, not merely `T>51/25`. It does not claim that every balanced marked-patch equality limit has already been excluded.

## 8. Assembly of the global theorem

Start with any original proper polytope counterexample of trace T0>=51/25. Normalize its tetrahedron and endpoint sum. The compact high-trace class has a global marked maximum M>=T0.

If M=T0, the input itself is a global marked maximum. It has unequal common-edge endpoints by the accepted balanced exclusion, positive endpoints by (C5), and a positive root-density integral by (S6). Section 5 therefore bounds its true vertices by sixteen, including c=0 and/or d=0. No approximation is made in this case.

If M>T0, then M>51/25. Section 7 excludes a=b at a maximizer. Apply the affine A/B reflection if needed, then Section 5 gives a genuine positive-root marked polyhedral maximizer P* with at most sixteen true vertices. Section 6 gives a proper polytope K_rho with at most sixteen true vertices and trace greater than T0 as soon as `rho^4 M>T0`.

Both cases prove the stated nondecreasing replacement theorem. All maximizing bodies were initially allowed to be arbitrary convex bodies. No maximum at a fixed vertex count, maximum in a fixed realization stratum, or finite ascent termination has been substituted for that maximum.

In particular, conditional on the existence of any original high-trace counterexample,

    sup_K T = M
      = sup over proper adjacent-triangle polytopes T
      = sup over proper adjacent-triangle polytopes
                   with at most sixteen true vertices T.

The first supremum is attained by a selected positive-root marked polytope. Attainment of the last two is neither proved nor needed when M is strictly above the input value; the finite counterexample consequence does not require it.

The same replacement proof applies to a proper arbitrary convex-body input with unequal endpoints and T>=51/25, and to a strict high-trace proper convex-body input. If one asks separately about a balanced NONPOLYHEDRAL proper input at exactly T=51/25, the minimal polytope-only balanced premise stated in Section 2 does not itself exclude that isolated possibility. The original mechanical polytope theorem above does not rely on excluding it. A blanket assertion about every balanced marked maximizer at equality is likewise not made.

## 9. Evidence, limitations, and most useful continuation

The new result is an analytic localization theorem with an exact algebra audit, not a newly computed maximizing body. Its conditional existence premise has not been witnessed here. No numerical maximum, universal trace value, actual T>=51/25 body, or mechanical 110 body has been produced. The new geometric argument has not been independently refereed or proof-assistant formalized; the executable replay verifies the stated algebra, not the geometric lemmas.

What changed from the accepted parent is specific. High trace supplies the common container. Closed cone flux eliminates the zero A/B endpoint faces. The full root-shave derivative both removes root collapse and supplies positive frozen-g root integral at a maximum. That sign permits the zero-C/D extension of the accepted three-dimensional free-boundary proof. The corrected root incidences and trace-flat ear handle the endpoint vertex counts. Finally, redundant-mark penalties keep proper resolution inside the sixteen-vertex budget.

This does not prove fixed-endpoint attainment, does not assert a finite monotone algorithm for arbitrary input bodies, and does not preserve their original centroid, full first moment, mechanical metric, face lattice, or equilibrium counts. The balancing/centering conditions used are always those of each actual uniform body.

The remaining original trace problem is now its value on the genuine finite class. A useful continuation is to exploit the special-facet skeleton and exact ordinary-triangle relations in that at-most-sixteen-vertex class, retaining all actual hull-volume and first-moment formulas and the c=0/d=0 boundary sectors. A free-weight matrix relaxation, a mere support-plane list without a true hull, or a fixed-vertex-count stationary point is not a replacement for those conditions. The polyhedral marked maximizer can have coordinate patches, but (P4) makes strict counterexamples proper without expanding the bound.

### Input closure and hash scope

The new journal and both new selected proof files were read completely through EOF. The earlier unchanged foundational proof, sixteen-vertex extension, ancillary source and correction remain supplied in this same chat; the literal arbitrary-body parent was also read through its complete new journal payload.

Mounted identities:

    research-journal(20260920-202946).md
    304294 bytes
    SHA256 2f57d18c6d81177ce31b2d322e4c0c2bbbda31679b8590c4868d71ffd4fa79c4

    [internal-source-reference]
    31160 bytes
    SHA256 48ee32688f80abfcd84b1f50f0648ba3942734c55e4bb3dc417beca668a3393b

    [internal-source-reference]
    40615 bytes
    SHA256 2c460625df162099bfba6437818bd8eff154d6d2f17d3f21e9ac2e4211c4d18e

There is a hash-scope limitation, not an identified mathematical conflict: the rendered Markdown subsection of the supplied arbitrary-body parent is 40851 bytes with SHA256 `f0fe07cbb36de5ab09d1ef1237896eb094942e06dcd67afef4a322f7a4822214`. It does not reproduce the advertised 41450-byte assignment-envelope pin `c58993f6099c9026b8aece0f2dcedf5b45aed4f8c933eacc92d639040f2c8a2f`. The separate raw envelope was not supplied, so that advertised envelope hash was not independently reconstructed. The literal mathematical payload and its accepted theorem are the authority used here, not a guessed envelope reconstruction.

The full balanced proof source is also not newly attached; its accepted proper-polytope statement is the explicitly named inherited premise. No unavailable tail-control script, old auxiliary-body coordinates, parent numerical certificate, or external archive was used by the new derivation.

## 10. Complete exact algebra recovery capsule

This post-derivation audit verifies the four endpoint-stratum versions of (S1)-(S4), the corrected incidence algebra, the resulting 16/13/12 bounds under their proved ear conditions, and the rational compactness constants. It does not purport to verify convexity, the free-boundary proof, or the balanced theorem by enumeration.

Exact parent/checkpoint identities are the arbitrary-body parent and two selected proofs specified above. The mathematical inputs are the four literal strata `(z_c,z_d) in {0,1}^2`, the symbolic formulas in Sections 3-6, `tau=51/25`, and the inherited rational tail comparison at mass 13/15 and threshold 11/8. There are no external data files, random seeds, or non-default options.

Save the following exact source as `high_trace_endpoint_bridge.py`, UTF-8/LF with its final LF. Observed environment: CPython 3.13.5 and SymPy 1.14.0, assertions enabled. Source: 2589 bytes, SHA256 `be5e5fc370151d4a2841a19da63141b5885d052e0cf05d484faa2e81b3495c84`.

```python
"""Exact algebra audit; geometric admissibility is proved in the handoff.
CPython 3.13.5, SymPy 1.14.0. No external inputs, randomness or options.
"""
from fractions import Fraction as F
from itertools import product
import sympy as s


def main():
    a, b, c, d, V, E, X, Y = s.symbols('a b c d V E X Y', positive=True)
    t, S, Sx, Sy = s.symbols('t S Sx Sy', real=True)
    for zc, zd in product((0, 1), repeat=2):
        cc, dd = (0 if zc else c), (0 if zd else d)
        sc, sd = 1-zc*t/a, 1-zd*t/a
        ce, de = (0 if zc else c-t), (0 if zd else d-t)
        A, B = a-t, b-t
        kx, ky = sc*(A+B+ce), sd*(A+B+de)
        assert s.expand(kx-(a+b+cc)+(3+zc*b/a)*t-2*zc*t*t/a) == 0
        assert s.expand(ky-(a+b+dd)+(3+zd*b/a)*t-2*zd*t*t/a) == 0
        N = (a+b+cc)*X+(a+b+dd)*Y
        T = N/(6*V*E)
        m = (X+Y)/(2*V*V)
        mz = (zc*X+zd*Y)/(2*V*V)
        G = (a+b+cc)*Sx+(a+b+dd)*Sy-N*S/V
        Vm, Xm, Ym = V-t*S, X-t*Sx, Y-t*Sy
        Em = E-t*Vm  # Exact through first order; root loss of ell is O(t^2).
        physical = (kx*Xm+ky*Ym)/(6*Vm*Em)
        normalized = ((A+B+ce)*Xm/sd+(A+B+de)*Ym/sc)/(sc*sd)
        normalized /= 6*(Vm/(sc*sd))*(Em/(sc*sd))
        assert s.cancel(physical-normalized) == 0
        expected = (T-m-b*mz/(3*a))/(E/V)-G/(6*V*E)
        assert s.cancel(s.diff(physical, t).subs(t, 0)-expected) == 0
    print('HIGH_TRACE_ROOT_SHAVE_FOUR_STRATA_ALGEBRA_PASS 4')

    ss, k, tt, e, m1, m2 = s.symbols('ss k tt e m1 m2', integer=True)
    R = 2*ss+k+tt
    degree_sum = 3*(R-m1-2*m2)-7*(4-m1-m2)
    bound = 6*ss-12-degree_sum+e+m1
    sharp = 16+e-3*(k+tt)-3*m1-m2
    assert s.expand(bound-sharp) == 0
    resolution = s.expand(sharp+m1+m2)
    assert resolution == 16+e-3*(k+tt)-2*m1
    for kk, ee, ttt in product(range(3), range(3), range(3)):
        if kk == 0 and ee > 0 and ttt == 0:
            continue  # Accepted interior-root exceptional-ear theorem.
        if kk == 1 and ee > 0:
            continue  # Equal endpoint values on C,D cannot have exactly one zero.
        assert 16+ee-3*(kk+ttt) <= (16, 13, 12)[kk]
    print('CLOSED_ENDPOINT_SKELETON_AND_RESOLUTION_BOUNDS_PASS 16 13 12')

    mass = F(13, 15)
    h = 4*mass/3-1
    volume = 1/(6*h)
    mu = F(1, 24)/volume
    endpoint = 4*mu*(F(51, 25)-2)
    assert (h, volume, mu, endpoint) == (F(7,45), F(15,14), F(7,180), F(7,1125))
    gap = F(51799877897,279130931200)-F(194481,1048576)
    assert gap == F(29035697,279130931200) > 0
    print('HIGH_TRACE_COMPACTNESS_CONSTANTS_PASS 15/14 1/24 7/180 7/1125')


if __name__ == '__main__':
    main()
```

Reconstruction and verification commands:

```text
python high_trace_endpoint_bridge.py > high_trace_endpoint_bridge.out
sha256sum high_trace_endpoint_bridge.py high_trace_endpoint_bridge.out
```

Expected complete output, including one LF after each line:

```text
HIGH_TRACE_ROOT_SHAVE_FOUR_STRATA_ALGEBRA_PASS 4
CLOSED_ENDPOINT_SKELETON_AND_RESOLUTION_BOUNDS_PASS 16 13 12
HIGH_TRACE_COMPACTNESS_CONSTANTS_PASS 15/14 1/24 7/180 7/1125
```

Output: 172 bytes, SHA256 `5e3d2c791b0fc2a6e0704e5aaf4bf654b97e3bba13373107652c99f5424c77bc`. The source was executed, then copied alone into a new temporary directory and executed again. Both output files matched byte for byte. This is an actual completed algebra replay, not a promised future check or proof-assistant formalization.

Convenience copies: complete handoff (`high_trace_variable_endpoint_localization.md`), complete runnable audit (`high_trace_endpoint_bridge.py`), and observed audit output (`high_trace_endpoint_bridge.out`). The full recovery unit and all continuation-critical formulas are embedded above; none depends on those links.
