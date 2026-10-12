# minimum-0115

AI research report · 2026-09-19 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# COMMON_EDGE_ROOT_EXTENSION_35_4_COMPACTIFICATION_V1

## 1. Result and its exact scope

**The previously unclosed positive-height end of the balanced-root image is excluded for the original weighted trace.** Normalize a=1>b>0 and use exactly the parent's projectivity and weights. Then, for every actual compact convex body with the prescribed adjacent maximal triangles ABC, ABD and actual edge AB,

```text
max_{P'} z' >= 35/4  ==>  T_original < 51/25.
```

There is no restriction on c,d, the two height graphs, the projection, the number of vertices, the overhang, or the dimension of the density-zero set. A quantitative version is

```text
6 Vol(P) <= 45/7 and max_{P'} z' >= 35/4
    ==> T_original < 1152256/564975 < 51/25.
```

The simpler height-nine companion gives the stronger conditional estimate `T_original < 651881/320000` on `6Vol(P)<=45/7, max z'>=9`.

The decisive operation is a **genuine common-edge extension to the zero-density point**, not vertical truncation of the image and not uniform refilling of it. Its extra volume and density integral satisfy a dimension-independent, first-power enlargement bound. In particular the remaining problem now has a compact actual-body formulation with

```text
-38/7 <= z' <= 35/4,
2366/50201 <= L <= 211.
```

The coupled original trace remains `J In/(6 I4 Iell)`. It is not replaced by the image's uniform trace. The lower-graph comparison body also yields a complete weighted epigraph inequality, and the remaining upper-graph defect is expressed by three actual tail fractions of that same epigraph.

**This is not a universal 51/25 theorem.** The maximum in the resulting bounded actual-body problem has not been bounded below 51/25, and no actual threshold counterexample was obtained. A second result resolves enlarged coordinate-face patches into genuine adjacent triangular facets while retaining a true root facet and the same endpoint values. A complete rational family demonstrates that construction with

```text
1013/500 < T_original < 2027/1000,
```

but this family is in an already closed prism/low-endpoint domain. Its role is a constructive boundary control, not a new record or an exclusion of the residual. Neither FULL253, the entire E17 layer, nor pairs of sizes 5,3 are closed. The accepted minimum bracket remains 34<=C_min<=622.

## 2. Evidence and inherited inputs

Read the new `research-journal(20260919-145148).md` consecutively through EOF, including the complete literal parent and source capsule: 1828 logical lines, 306425 bytes, SHA256 `ed0d302df615e2f83deecac10983a528e2a251dce7c713fc38a780f2a42c2130`. The earlier unchanged context remains the same-chat evidence. The source-only extraction of the parent's three complete Python units was authenticated and read; it was not a new replay of its old certificates.

The authoritative parent is `minimum-0111`, immutable envelope SHA256 `64909830719ea325d6660a5d6d081ded07c9b30b980c16c647d4b81ee5d2c822`, LARGE_ENDPOINT_FLOORS_AND_TRUE_PROJECTIVE_REDUCTION_V1. Its six literal original controls, five image controls, map, and weighted-integral definitions are unchanged. No conflict requiring alteration of that payload was found.

Only two inherited trace results are needed for the new height exclusion: the unrestricted **zero-common-endpoint bound T<=2**, and `T>=51/25 ==> 6Vol(P)<45/7`. Both are explicitly supplied mathematical premises. No new replay of their older proof sources, the free-prism 393-cell program, or either earlier endpoint program is claimed. The new exact capsule has no computational dependency on those programs. The parent states the zero-endpoint theorem and its genuine tetrahedral equality case; it also records the high-trace volume bound. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

The compact endpoint and projection bounds used after the new height theorem are inherited unchanged. They are not assumed for its proof. The coordinator's new one-facet centroid actuator and centering-cut theorem were read, but are not used to assign a centroid or mass to any trace body here. :contentReference[oaicite:2]{index=2}

## 3. The actual extension theorem

### 3.1. Notation and the new true pair

Put A=0, B=(0,0,1), C=(0,1,0), D=(1,0,0), h=1+b, alpha=1-b, nu=min(c,d), and

```text
ell=1-(1-d)x-(1-c)y-alpha*z,
n=(h+c)x+(h+d)y,
V=Vol(P), B_ell=integral_P ell, N=integral_P n,
T(P)=N/(6 V B_ell).
```

Let

```text
E=(0,0,1/alpha),   Q=conv(P,E),
chi=alpha*(1+b+nu)/(1+nu) <= 1-b^2 <1.
```

Since b>0, E is strictly beyond B and is not in P. Both ell(E) and n(E) are zero. Most importantly,

```text
Q intersect {x=0}=triangle AEC,
Q intersect {y=0}=triangle AED.
```

These are the **entire actual maximal facets** of Q and their intersection is its true edge AE. The old B is now an interior point of AE. It is not used as a vertex or as the endpoint of a purported Q facet.

After the genuine affine normalization `z_new=alpha*z`, the endpoint values on A,E,C,D are `(1,0,c,d)`. Thus the inherited zero-endpoint theorem applies to Q at its own filled centroid. Writing `T_n(Q)=N(Q)/(6V(Q)B_ell(Q))` merely for the original-n comparison functional, it gives

```text
T_AE(Q) <= 2,
T_n(Q) <= chi*T_AE(Q) <= 2chi.
```

Indeed the ratio of the old and new x/y coefficients is at most `(1+b+nu)/(1+nu)`, while the volume normalization contributes alpha. `T_n(Q)` is not mislabeled as the trace of the old AB pair. No assumption that ell=0 is a facet is required: its zero set in Q may be a vertex, edge, or facet.

### 3.2. A sharp first-power hull-enlargement budget

Here is a reusable dimension-d statement. Suppose K is an actual full-dimensional compact convex body and

```text
E=(1+beta)r-beta*q,   q,r in K,   beta>=0,
Q=conv(K,E).
```

For any affine u>=0 on Q with u(E)=0,

```text
Vol(Q) <= (1+beta)Vol(K),
integral_Q u - integral_K u
   <= beta*(integral_K u-u(q)Vol(K)/(d+1)).
```

In particular `integral_Q u <= (1+beta)integral_K u`. The exponent is one for both quantities; it is not a homothetic volume-power estimate.

For a polytope, let `v_F(q)=Area(F)*inward_height(q,F)/d` be the actual cone volume of each facet. The additional volume over a visible facet F is exactly

```text
W_F=beta*v_F(q)-(1+beta)*v_F(r) >0.
```

Consequently `W_F<=beta*v_F(q)` and summing gives the volume claim. If u_F is the actual area mean of u on F, the extra u-integral is `d*W_F*u_F/(d+1)`. The genuine q-fan identity is

```text
integral_K u = u(q)Vol(K)/(d+1)
              + d/(d+1) sum_F v_F(q)u_F.
```

All omitted terms are nonnegative. This proves the sharper mass claim, retaining the same facets, area means and cone volumes. Selected flat cells may have zero volume. For a compact nonpolyhedral K, apply this result to inscribed polytope approximations containing q,r and pass to the actual volume and affine integrals. Thus no surface smoothness or facet genericity is being assumed.

Apply the lemma to the preceding Q and u=ell. Since Q\P has positive volume and n>0 almost everywhere in it, **N(Q)>N(P)**. Therefore every genuine representation of E by q,r gives

```text
T(P) < 2chi*(V(Q)/V(P))*(B_ell(Q)/B_ell(P))
     <= 2chi*(1+beta)^2.
```

With mu=ell(g_P), the retained density saving improves the last expression to

```text
T(P) < 2chi*(1+beta)*(1+beta-beta*ell(q)/(4mu)).
```

The common product of volumes and density masses was never broken into unrelated realizations. These inequalities close the full actual geometric sectors where either displayed upper expression is <=51/25, including equality of that sufficient test.

One may minimize beta over actual q,r. The exact geometric quantity is

```text
beta_*(E;P)=min{beta>=0:E in (1+beta)P-beta P}.
```

For a rational polytope it has the finite linear-program description

```text
minimize sum_i v_i;
u_i,v_i>=0;
sum_i(u_i-v_i)=1;
sum_i(u_i-v_i)p_i=E.
```

Here r and q are the associated convex combinations of actual points, not freely fitted volume weights. Equivalently beta_* is the maximum positive directional support excess divided by the corresponding width of P. No optimal beta_* computation is claimed for the finite controls below; they use the explicit point recipe next.

### 3.3. An explicit representation from one actual point

For p=(x,y,z) in P with z>0, set s=x+y, w=alpha*z. Then

```text
E=p/w-(x/w)D-(y/w)C+(s+w-1)A/w,
beta=max(s,1-w)/w.
```

If s+w>=1, take `r=p/(s+w)` and `q=(xD+yC)/s`. Here s>0. If s+w<1, take `r=p` and `q=(xD+yC+(1-s-w)A)/(1-w)`. Both cases are convex combinations of actual points. The zero denominators cannot occur for the stated actual cases: a point with s=0 is on AB, not beyond B.

Now use exactly the parent's map. With S0=1+b+c+d,

```text
f=ell+n,
x'=S0*x/f, y'=S0*y/f, z'=b*z/f,
ell'=ell/f=1-(1-d/S0)x'-(1-c/S0)y',
L=1/f=1-(1-1/S0)(x'+y')+(1/b-1)z',
J=b*S0^2,
x=x'/(S0*L), y=y'/(S0*L), z=z'/(b*L).
```

For the image point write s'=x'+y' and Z=z'>0. The explicit beta becomes

```text
beta = b/(alpha*Z) * max(s'/S0, 1-(1-1/S0)s')
     <= b/(alpha*Z).
```

The second entry of the maximum is <=1. The first is <=`1/(1+b+nu)<1`, since `1-ell'=n/f >= (1+b+nu)s'/S0`. This is a pointwise statement on the actual image, not an independently assigned moment bound. It yields

```text
T(P) < 2chi*(1+beta)^2
     <= 2(1-b^2)*(1+b/((1-b)Z))^2.
```

The map and target being transformed are exactly the parent's `I4,Iell,In`, not the ordinary volume trace of the image. :contentReference[oaicite:3]{index=3}

## 4. Closing the complete high-image end

Suppose first that t=6V(P)<=45/7 and an actual point has Z>=35/4. The actual pyramid `conv(p,A,C,D)` lies in P and has volume z/6, so z<=t. Also

```text
z*(1-b+b/Z)=1+(b+c+d)s >=1.
```

It follows that

```text
1-b+4b/35 >=7/45,
0<b<=266/279.
```

The preceding actual extension bound gives

```text
T(P) < U35(b)=2(1+b)(35-31b)^2/[1225(1-b)].
51/25-U35(b)=P35(b)/[1225(1-b)],
P35(b)=49-609b+2418b^2-1922b^3.
```

This polynomial is strictly positive on the **entire closed** interval [0,266/279]. For 0<=b<=1/4 the complete identity is

```text
P35(b)=(3875/2)*(b-609/3875)^2+8869/7750
       +(961/2)*b^2*(1-4b).
```

On [1/4,266/279], all four cubic Bernstein coefficients are

```text
571/32, 18359/248, 975149/3348, 14357/22599.
```

Thus `P35>=14357/22599` on the full interval, and

```text
T(P) < 51/25-293/564975 =1152256/564975.
```

For the height-nine companion, t<=45/7 and Z>=9 force b<=19/20. The corresponding exact polynomial is

```text
P9(b)=81-981b+4000b^2-3200b^3,
51/25-2(1+b)(9-8b)^2/[81(1-b)]=P9(b)/[2025(1-b)].
```

Its low-interval identity and high-interval coefficients are

```text
P9(b)=3200*(b-981/6400)^2+74439/12800
      +800*b^2*(1-4b),                 0<=b<=1/4;

143/4, 8011/60, 29557/60, 309/20,     1/4<=b<=19/20.
```

This proves `T(P)<51/25-919/320000=651881/320000` there.

Finally a putative T>=51/25 already has t<45/7 by the inherited volume theorem. Therefore its entire actual image satisfies **z'<35/4**. The a=b=0 normalization-zero case is already closed at T<=1. The b=0 endpoint after a=1 normalization is independently closed at T<=2, and b=1 by the accepted balanced theorem; neither is divided by alpha or silently discarded. Both polynomial covers include all their seams and endpoint equalities. No monotonicity of either the old s=1 cut or a new z'-cut is used.

## 5. The remaining weighted variational problem is compact

Combine the new ceiling with the parent's endpoint and lower-coordinate bounds. Every potential counterexample has

```text
1/25<b<1,
nu=min(c,d)<3/4,
m=max(c,d)<(943/1352)(1+b), R(m,nu,1+b)<0,
R(m,nu,h)=9405m^2+1013m*nu+10418m*h+1750nu^2-6737nu*h-8487h^2,

S0=(1+b)/(1-gamma-delta), gamma=c/S0, delta=d/S0,
26/25<S0<1401/338,
gamma+delta<943/1619, gamma,delta<943/2295,
0<=s'<2295/1352,
-38/7<z'<35/4,
2366/50201<L<=211.
```

The new upper bound on L follows directly from `L=1-(1-1/S0)s'+(1/b-1)z'`, b>1/25 and z'<35/4. In the original body this gives the genuine separating inequality

```text
ell+n >=1/211.
```

On any actual zero-density point it implies, using the inherited endpoint bounds,

```text
x+y >=676/484245.
```

These are necessary physical inequalities, not a realization of their scalar intersection.

For an explicit compact overcover, replace the strict inequalities just displayed by non-strict ones, use the closed endpoint constraints, and range over **actual compact convex sets K containing T0** in

```text
x',y'>=0, x'+y'<=2295/1352, -38/7<=z'<=35/4,
ell'>=0, L>=2366/50201,
6 I4/J<=45/7.
```

All masses are still their own volume integrals. The original weighted objective is

```text
F(K;b,gamma,delta)=J In/(6 I4 Iell),
I4=integral_K L^-4,
Iell=integral_K ell' L^-5,
In=integral_K (1-ell')L^-5.
```

This is a compact family in the Hausdorff topology together with the closed endpoint parameters. Its objective is continuous: the sets contain the fixed full-dimensional T0; the weights are uniformly bounded and continuous after the positive lower bound on L; convex boundaries have volume zero. The denominator has the explicit lower contributions

```text
I4(T0)=J/6,
Iell(T0)=J*S0/24.
```

Hence a maximum exists on this actual-body overcover. The formulas never supply a free centroid. The missing result is a bound on that maximum, not control of an unbounded positive-height or singular-weight end.

### What remains on the boundary

Exact maximality of the two coordinate triangles is not Hausdorff-closed: a limiting coordinate facet can grow. A true density-root facet can also lose area, and b can tend to 1. These strata have **not** been declared harmless by compactness alone.

They nevertheless admit an exact geometric resolution. Let K contain T0 in the quadrant and choose q in K with q_x,q_y>0. For 0<epsilon<1 put

```text
K_epsilon=conv(T0, (1-epsilon)K+epsilon*q).
```

This is a real convex body inside K. Its entire coordinate facets are exactly ABC and ABD, with true edge AB; all contracted points have positive x and y. It converges to K, and all its true volume and affine integrals converge. The same statement applies directly in the balanced image with its fixed L,ell', then through the exact inverse projectivity.

If F=K intersect {ell'=0} is two-dimensional, choose q in relint F. Its x,y coordinates are positive because ell'(A)=ell'(B)=1. Then the zero set of K_epsilon is exactly

```text
conv((1-epsilon)F+epsilon*q,
     {C if gamma=0}, {D if delta=0}),
```

and remains a true two-dimensional root facet. Thus the resolution preserves the **same endpoint values and the same root plane**, not just the value of a scalar objective. For a positive-density contraction point it need not preserve a root facet, and no such preservation is claimed.

Consequently a value strictly above 51/25 in the compact patch closure would yield genuine nearby counterexamples. A rational polytope counterexample would then be obtainable by inner approximation, a small strictly interior perturbation of the density when necessary, and rational approximation. Optimizing the density afterwards over the actual polar can supply a rational facet root, but can change its endpoint sector. **An exact maximum equal to 51/25, and the location of any such equality, remain unresolved.** No assertion that inward resolution increases T is made; the exact control below decreases it slightly.

## 6. Complete two-graph form and the real upper-tail defect

For b<1 put kappa=(1-b)/b and `L0=1-(1-1/S0)(x'+y')`. Let Omega be the true xy projection of P', u its convex lower graph and v its concave upper graph. Define

```text
r=L0+kappa*u,  R=L0+kappa*v,
A3=integral_Omega(r^-3-R^-3),
Aell=integral_Omega ell'*(r^-4-R^-4),
An=integral_Omega (1-ell')*(r^-4-R^-4).
```

The **original** objective is exactly

```text
T(P)=(1-b)*S0^2*An/(2 A3 Aell).
```

The data have a complete actual-body interpretation. Omega is convex, contains Delta, and has exactly the unit coordinate-axis segments. On those segments, for s=x'+y',

```text
r=1-(1-1/S0)s,
R=1/b-(1/b-1/S0)s.
```

The functions r and R are respectively convex and concave, positive, with r<=R, and ell'>=0 on Omega. On Delta the mandatory T0 requires `r<=L0` and `R>=L0+kappa(1-s)`. With the displayed bounds and closed-graph conditions, these data conversely construct the true body between the two graphs, with exactly the prescribed triangular coordinate facets. Zero-length fibres are allowed. A root facet requires a positive integral of `(R-r)/kappa` along the true root segment of Omega; a line or point alone is not called a facet.

The comparison body Q=conv(P,E) has an especially useful image:

```text
Q' = P' + [0,infinity)*e_z.
```

Indeed the segment from p to E maps to the vertical ray above p'. Thus its **actual** upper graph has R=infinity. Its weighted volume and affine integrals remain finite, even though its uniformly filled image has infinite volume. They are the real integrals of the compact Q under the inverse map, not artificial tail masses.

Writing `A3inf=integral r^-3`, `Aellinf=integral ell' r^-4`, `Aninf=integral (1-ell')r^-4`, the zero-endpoint comparison proves the full lower-graph inequality

```text
S0^2*Aninf <=4*(1+b+nu)/(1+nu)*A3inf*Aellinf.
```

This holds for all the actual lower graphs just described. It does not by itself bound the finite-upper-graph problem. Its remaining defect is exactly

```text
thetaV   = integral R^-3 / integral r^-3,
thetaell = integral ell' R^-4 / integral ell' r^-4,
thetan   = integral (1-ell')R^-4 / integral (1-ell')r^-4,

T(P)=T_n(Q)*(1-thetan)/[(1-thetaV)(1-thetaell)].
```

All three fractions come from one Omega and the same two graphs. The extension lemma bounds their actual volume and density costs; it is not permission to choose the fractions independently. This is the precise remaining weighted roof problem. At b=1 the three-dimensional integral formulation remains continuous; the divided-by-kappa formula is not used as a boundary formula.

## 7. Exact controls, including two complete families

### 7.1. An actual unbounded-image family

For every 0<epsilon<=1/20 use endpoints `(1,1/4,1/4,1/4)` and the eight ordered points

```text
A, B, C, D,
(epsilon,epsilon,4/3-2epsilon),
(1,epsilon,1/3-epsilon),
(1,1,-2/3),
(epsilon,1,1/3-epsilon).
```

Their exact maximal facet cycles are

```text
012, 026, 031, 063, 1354, 1472, 276, 365, 4567.
```

Thus f=(8,15,9), ABC and ABD are genuine, and 4567 is the genuine quadrilateral density root. The entire interval has actual integrals

```text
V=(5-3epsilon+epsilon^2)/9,
Mx=My=(16-6epsilon-4epsilon^2+3epsilon^3)/72,
Mz=(11-26epsilon+27epsilon^2-9epsilon^3)/108,
B_ell=7/48-epsilon/36+epsilon^2/144,
N=2/3-epsilon/4-epsilon^2/6+epsilon^3/8.
```

The complete continuous certificate proves T<3/2 throughout. The balanced image has

```text
max z'=1/(9epsilon)-1/6,
```

so its positive height is genuinely unbounded. The original trace tends to 48/35; the image's uniform volume tends to infinity and its uniform trace tends to zero. The inverse weighted integrals instead tend to the finite original integrals multiplied by J. This is a realized noncompact-boundary control, not a formal scalar construction.

At epsilon=0 the actual limiting hull has f=(7,12,7), V=5/9, g=(2/5,2/5,11/60). B is no longer a vertex and the coordinate facets are quadrilaterals. Its value 48/35 is the limiting **patch functional**, not a claim that the limit retains the original triangular pair.

All eleven exact inputs

```text
epsilon=1/d, d in (100,1000,10000,50,40,35,32,30,28,25,20)
```

are retained, with their complete true hulls, all edges, own centroids, real s=1 sections, both cut bodies, balanced images and common-edge extensions in both coordinate frames. The original eleven have strict S/U/H=(5,7,10), weak000. For example, at epsilon=1/100,

```text
V=16567/30000,
g=(5313201/13253600,5313201/13253600,3580897/19880400),
T=177106700/128609621,
max z'=197/18.
```

Its real section S has normalized area `Area(S)/sqrt(2)=149/300` and centroid `(1/2,1/2,98/1341)`, with points on both sides of z=0. Its uniform image has f=(8,15,9), V=6503/2424 and T=57435670/137662007, different from the original weighted trace.

The chosen extension certificate for this entire family has `q=(1/2,1/2,0)` and `beta=4epsilon/(2-3epsilon)`. The density saving is genuinely useful: at epsilon=1/30 the coarser bound is `3721/1805>51/25`, whereas the same-body corrected bound is `68807817/33899705<51/25`. At epsilon=1/28 even the corrected sufficient test fails, although the whole family still has T<3/2. Failure of this test is not a counterexample or a feasibility certificate.

### 7.2. Resolving a real 4,5 patch pair into true 3,3 facets

A separate exact construction starts with the following ten rational bevel vertices:

```text
(-1,-1,-3/8), (-1,-1,1), (-1,0,-1), (-1,1,-1), (-1,1,1),
(1,-1,-3/8), (1,-1,1), (1,0,-1), (1,1,-1), (1,3,5).
```

Apply `p -> p/(1+v.p)` with `v=(-2/25,-1/20,171/200)`. Every denominator is positive; the minimum is 3/200. The resulting actual body has f=(10,17,9), own S/U/H=(3,2,3), weak000. The common edge (7,8) lies between a quadrilateral and a pentagon. Choose the triangular patches with third vertices 3 and 9, and use the exact canonical frame

```text
A=point 8, B=point 7, C=point 3, D=point 9.
```

In that frame normalize the true root-facet slack to endpoints

```text
(1,3/13,0,3/1009).
```

The original body has only triangular **patches**, not the required maximal triangles. Let q be the average of its five root vertices 0,1,2,3,4, expressed in the canonical frame:

```text
q=(555556409/1162928130,
   108401186/249198885,
   77363492/670920075).
```

This is a specified interior point of the true root facet, not a freely selected center of mass. For every 0<epsilon<=1/100, take the hull of A,B,C,D and the contracted points `(1-epsilon)p_i+epsilon q`. Equivalently only the six indices `(0,1,2,4,5,6)` need be added to the four canonical anchors.

The entire resulting family has **true f=(10,21,13), genuine adjacent maximal triangles ABC,ABD, and a genuine pentagonal root**, and the exact certificate gives

```text
1013/500 < T < 2027/1000.
```

At the stored epsilon=1/10000 control,

```text
V=188726464392128779093853/1035670566060000000000000,
T=606022759975307647666934631307905489143701910738410000000000000 /
  299060338353635921640612107497704442159168078223771268773287629.
```

Its own strict counts are (4,4,6), weak000. The true T is approximately 2.02642303995086, slightly **less** than the original patch value approximately 2.026423830214158. The image's uniform trace is approximately 1.99027025282176. All exact centroids and all maximal face/edge data reconstruct from the capsule. The family has rho=1 and is also in the earlier low-endpoint chamber: it is not a newly surviving endpoint-domain example, not E17 after resolution, and not a 5,3-to-3,3 theorem.

### 7.3. Verification and locator boundaries

For the two continuous families, all 280 four-point orientation polynomials are retained: 267 nonzero polynomials with 783 strictly positive Bernstein coefficients after factoring possible powers of epsilon, and 13 identically zero coplanarity polynomials. These prove the entire face lattices on the stated open-left, closed-right intervals. The genuine volume and first-moment identities have explicit degree bounds; the trace-gap polynomials are certified on the full intervals. Exact evaluations used for coefficient reconstruction are not used as positivity samples.

The independent checker imports no builder. It reconstructs every continuous coefficient from direct formulas, enumerates vertices from triples of **reported supporting planes** rather than from point triples, proves boundedness through positive normal balance, and independently integrates 71 actual body records by signed boundary cones. It also verifies all twelve weighted image calculations using a signed-origin fan, different from either builder positive fan. All 49 complete own-centroid mechanical records have every primitive nonzero and weak000. None is 110.

The optional locator used NumPy 2.3.5, SciPy 1.17.0, seed 941379 and one BLAS thread. It checked 4000 random actual projective bevel shapes, then a separate differential-evolution run with population multiplier 8, 150 iterations, tol=1e-9, no polishing and one worker, totaling 8456 evaluations. Every evaluation recomputed the true filled centroid. The best located patch values were approximately 2.00174679173199 and 2.026417616814314, respectively. These are **not** optimum certificates or exclusions. The complete source and both complete frozen checkpoints are included; the simpler rational parameters above, not either floating checkpoint, are the exact construction input.

## 8. Remaining obstacle and useful continuation

The new theorem removes the entire unbounded positive-height end without changing the objective to the image's uniform filling. The genuine extension budget gives more than a height cap: it preserves the actual density saving and permits an exact geometric beta certificate, or direct actual Q/P mass-ratio tests. The full epigraph inequality identifies the remaining freedom as one convex lower graph and one concave upper graph with fixed axis data and three coupled tail fractions.

A potential T>=51/25 body must now satisfy the parent's endpoint remainder and all applicable old rho/Psi/Phiold/PhiS and low-endpoint restrictions **inside the bounded weighted body space of §5**. No intersection of these necessary scalar conditions is claimed to be realizable. No additional mandatory exact dependency is missing for the new recovery. The most useful continuation is a bound on the actual compact roof problem or a genuine maximizing body in it, while retaining root area and the coordinate-patch boundary. A maximum strictly above the threshold would be convertible to true triangular facets by §5; a maximum equal to the threshold still needs a separate equality argument.

## 9. Self-contained recovery and actual receipts

Exact environment: CPython 3.13.5, standard library, assertions enabled. The proof computations require no solver, RNG, network, archive or parent file. The optional locator is separate. Save the full source below as `recover_weighted_tail.py` and run

```bash
python -S recover_weighted_tail.py sources weighted_tail_replay
python -S recover_weighted_tail.py build weighted_tail_replay
python -S recover_weighted_tail.py check weighted_tail_replay
```

A clean source-only build and check were actually executed in a new directory. The complete report was regenerated byte for byte. Pins:

| Object | Bytes | SHA256 |
|---|---:|---|
| recover_weighted_tail.py | 21932 | 8d109e5f4aad5813d868e6016b8837af63d58a3dc7356144c6a65a11d2207541 |
| Decoded complete five-file payload | 46056 | 61ce1858a1ddfdc655a1f185c0042d010fc513d5916e14aff1351132d5db41ca |
| trace_tail_exact.py | 27708 | cdc976c1d2f9ca433c5a7ab8927577a18870a00a8292acc823b131935e99f65b |
| trace_tail_check.py | 11580 | 594f12c0d7f7a09284f96d44ac71118602601bda23f41a3a820f910b86015cbc |
| patch_locator.py | 3597 | 0f7ef035ba0b8d7718b98c29bd0d76c67af7b91ec406a83883ee4ab2f1ccd9d1 |
| Random locator checkpoint | 1051 | e1e442ee0ef3e6fadd31455fb104dbe4b967c27dfb24b622605b2210010f0a70 |
| Differential-evolution checkpoint | 1049 | 78ad4b97fa663432d7755778d7b43323b2192c2b760baf0be7de46669b156c4e |
| trace_tail_exact.json | 560930 | 1db69c3c46f6dce71ff39897a4266f1906084fd5b05e09306f7b08e29a8a0606 |
| Cold build stdout | 999 | 0a6ad9be63a68ba8756b9986966199c4a0ffccaa2ca7be9d8a4e60490858f828 |
| Cold check stdout | 999 | 81060e4cb531c46ad17c34600f5b29ca8a009db6591ec0205621863b14a49292 |

Actual terminal markers include


[Encoded source block omitted; the code in this passage is incomplete.]


These receipts verify the finite algebra, complete interval certificates and actual constructions. They do not turn the accepted mathematical premises into newly replayed proofs, or formalize the continuous geometric argument in a proof assistant.

Convenience copies: [autonomous recovery source](sandbox:/mnt/data/recover_weighted_tail.py) and [complete exact geometries and certificates](sandbox:/mnt/data/weighted_tail_cold_v2/trace_tail_exact.json). The complete source below contains all five files, including both numerical checkpoints; no download or predecessor file is needed for reconstruction.

### Complete autonomous source

```python
"""COMMON_EDGE_ROOT_EXTENSION_35_4_COMPACTIFICATION_V1 recovery.
CPython 3.13.5 standard library, assertions enabled; no external files or network.
Parent minimum-0111, immutable SHA256
64909830719ea325d6660a5d6d081ded07c9b30b980c16c647d4b81ee5d2c822.
Commands: python -S recover_weighted_tail.py sources|build|check DIRECTORY.
The optional locator requires NumPy 2.3.5 and SciPy 1.17.0; it is NOT proof.
"""
import base64,hashlib,json,subprocess,sys,zlib
from pathlib import Path
assert __debug__
PAYLOAD_PIN=(46056, '61ce1858a1ddfdc655a1f185c0042d010fc513d5916e14aff1351132d5db41ca')
SOURCE_PINS={'patch_locator.py': (3597, '0f7ef035ba0b8d7718b98c29bd0d76c67af7b91ec406a83883ee4ab2f1ccd9d1'), 'patch_locator_de_checkpoint.json': (1049, '78ad4b97fa663432d7755778d7b43323b2192c2b760baf0be7de46669b156c4e'), 'patch_locator_random_checkpoint.json': (1051, 'e1e442ee0ef3e6fadd31455fb104dbe4b967c27dfb24b622605b2210010f0a70'), 'trace_tail_check.py': (11580, '594f12c0d7f7a09284f96d44ac71118602601bda23f41a3a820f910b86015cbc'), 'trace_tail_exact.py': (27708, 'cdc976c1d2f9ca433c5a7ab8927577a18870a00a8292acc823b131935e99f65b')}
REPORT_PIN=(560930, '1db69c3c46f6dce71ff39897a4266f1906084fd5b05e09306f7b08e29a8a0606')
BLOB='''
c-p;v`&Z*Q(&+E^ugLD4^Tke-
U^{Qp>a%n=J<V)GGeEOFo6gB`VgrWY7&`>$`R0GWRVB%m9|2}|@0|y+WvTQkm8wcrrQiP^x$DK%Y`I#v>s8#2p8mf3_wV%YmuMZV
LU&nn7wda>*}A%4E^F&JaKp>{r5m@XU`-XQ9o^p^Kkb|@g5xJv^Zd0R-
v(ijtb;`@@qMrTJv>^~HtzD?udU+Rg&Qn=55BlD011+s8`k{C#qvIZI>+z`mDXZcwjlPSrTc{05<hYw*#~f<mEXhQHd@8&+A8@TU
I65qS`gNZ`j_MVqj#V8PG?774`*kePWJacoYq<W%i(b$<?x@Mb1CNTDrx)SCWu$z<Yvn2c0H{lyuXc}YHm^sBd9E1-
PV#t5Iwb5FjTj}55Fe!dBMenAN%1taF;WGvs&I`M_3I<1oNc;sW`h%;A8TXFn|KzKJLBWKjnsDF`IQ+hdCxQY&K$D`0YT-
2!1WrV|`}Rmp-L9kaNfelxM_-
@Y`bpNExv{<#*t%XPV!`{SQ9__ynr=J>&QFeYErq`DO&{+BD4?j^hQ6BQ=Fy;R`1G2qNQxT}<rVY4c*TYfsHT0OY~Zdp?=mP{tcZ
C4CqxA7{!S7-lWFsJZw7enPJ{r^hLka2dT(yQbg6vy%fJMr}8a-
6vyWTuiJfRCrB)nowa?>!@upV5Se_vGhaZ!fe^*6q@!^?exlx{2B}{AqEWUlu?y$?RM>Wl?3Zx<JY2ib?q<UF<3v<mVuvO=JgeP0
Cc-WY_3JC<<oi<A?kVl1-u5~Ix+6d-
R~hnX8@DmO?JD`h1#*+gO<(czvdbyLcG}OshPkZ@nUOFVq&vWX(7E#TExb>O&Fl%%3VXBYY|nShz8tEy1P?z?D-
+Lo5%kE%*DBY*EXP|VZPyQ%kJ&Q{`x)+Ye%aPFt8@yj&~s2WS3zobW3#H$3=`2d&gjz!#d_4-
DTp_I2`kISVT3)xM;DsssQ>S>sayQ_O0)RhGmY|F+ZNb#81bY4Yhrq81Ul<VRC<K)PrjlT({l^b+(S7Io7nbV(@tpuad-
|BpZ|H$$=-
p;hjEIan3iJHbOARm)zKFR96~Mh|+DdxiWXUCcRkZ&N&ncwYf_xIi3K{Pp2*XwWd>szfSgEL`oR%t2`KQwKiOq%kGMmf=eo7VwE7
q)^6|lRV)0*<rrGBb9=8E4G^#36*BnCCBIV1kn^~GCPo`R$VqM4eru49xueE>?k8(*$T`5ezVYMMCH&G7_n8s6ESQ`51xyQ*rnly
~JROp6lfa!a_&Z1JN~i7HKRg#9*A}Y~DuX6LOCe`dKFz1&b;2jpaRB5RA22VCUVzmCDVYTRlxnLjo)(-
2W^xfs$Jg12!UuDFgYWTbxiqeE9Z(6+;@$>`#n|)k;bz+Mtnt#4&A6U6sa5HadQ15QGO8>D$91^pO)wMNoi@DX*tPY9rPcJT+-
IoQ(moTAhhTkGLo|-#WQ`-~0e$g&UJowARqWSU5W-ptyfnew#eA?;@Rn=u7*4}=M7P#!?CZl7Y$}G~I&UoVe+-
%Rt@iu|sDXTBR$CN>8WQeWP1kO$*G<=fzwjS@`l+_R@#Ci&{8{^twbf#AA1AoI;b!bz0?}N%@w!cUqhN6(#{crxeKZg%b033*+vb
>db&g3B%0YA(_9QGLhI5^?-6--y&!D`fn0%FHTu&$~yOF=^bp;@k`V+4n5^k&$SVm3w3;V&2(Qlla<9M}NbD%v&)=122s^;O#1T#
^KV6jm0TU-$UYgeocqM)*k%nKH41IK~W3P7}E7w*Cb^p#l3s8amH1Y@-
H0iz9UMIh=j8NOVr7Xg1QUrn{MioJ=(M0Aq~G}2aT7xc1yA9;vD=Ujj|H`yh>Y_C^KV6hAsA+=2<oKkMxNOXqXnedf}GSFL<-
^^${R)C}(s+`S205Y3#UZ2fw-5{LJ>a@E7|HemMyE7P#Z&!f8z^mXGZ=hk=RNQb?lKIvKGL-nWI?SH8x~-4%G-
teUmw=GCK%yAOrhdMEa(eLP2zW7=x!DYm5qZGbj0xUKPq_g8@QR<s_e8sJGg=}g5_@p%a=DrVvxxOEs)eW!J~X*K-
Y}16TbHSjAVmPeQ);WW!BJIX*z`lAo@10}n6r(H8?cZMb+i2t2T%eN+8%I;i9y&yBZq%PgE;+V0wHC^4CdA4a++cJ0w*@R@t+dW&
1U`k_pmNjvK+5>`=@7h0govdviPK);Xz$XMI_eW5&i1Z!f+~tXl(=n(oAzTjWj-Scu6#ulG-r-?)`E-gH-CMsVKR|jdd-
{60=iFkPqV%$lbmNY+J>*M%%K8t$8WUro>KFV$T#51{!?*#(~;)BR;Vh{43HC7e)QR6=888w72dO_`o*s)~5UtDZYgo*^~gx@p8p
+KaHY)L^3O)`|3@rJ=%>LJlAfUwMRXmMy=&a<R#n`0BO}lwCwz4HnyHG#?=iIUM({i2!u`2QOO?CF-Zpkc*ph#8d32uWf>+$t0(~
(gbx|eNI=?{+dYc`W#GUwjNmgg_Db+{>|qt(AWgAF%V8*EH-
N=`ju^Zj$E(=Du9(?s{_y2!zlfbVJo`J#i<~phpDnKZ#SP5>Eh!K|fB*h>v4sD=TN{i<HmiOAJ1!J_hi~Wj>-
2g~d(d(0j??Rm`u#x{b0Mzd*U5m@hEq%tG@H_TtTv#uOM0~j?S8*I7+C$zXwbJieO9yk0J7^0`lCUwGaT90kOBW>wL8vW*tPq8XE
^MQtUdwB78^mc+N061XW4zn?hpE%t_3Zy+I^>I4WNy^P6tTn&|x(P^4aj%>)LjIXxR?5s@op*2c1#J>Do~5Xf%Rat+q9^x^~xsF9
WFF>B-dY2x{m;bD){M5q8^Z4|_dmcCX`fI=z0+8HolGQd8q5ExYY>`u1?p?Lh}dgN_YNsZO-oU1<K$ww(^t)9pC@4uG3Lde7<%hC
OKYpbI0^vng{qv7AQbyX|h*?m?R&c{u8e(w5cl_aLWZ^*X&Sj6HU;n3Ib4+Wlc4#<$xU4y;b!fqqvcm9wd~cPwjQ;gs54r_*z&nX
gF0;&!{&bw)5M{ecZ*(&^FAmD8X!pvkDy8$x2Y+ebVByy$g@j^)6-
^#_PtU6HetSWct5dyqUB^*S`!0~io7ZcfL6Y<7PHtA8}KdI+_g7a{cfnCj5@0+NjYKt)oklqMQ)1Ge`1fEj=&BUl+7YUrpp=#5}4
bVh*iogt=;h9hS<7yuC-
j9}b{Q^G;qYY+o1d`Y<^fs+7=N?KSG%zIzFO#i^VNUSiMU_3B|_Dx#((EC2Dls+IB%(LD7qk^u8UFrqe0$5i~Te_Wg2hgD703tZH
)y>nEPBm@mYqX`)cDj8;1`EfiH?;b=$^kuWn5#jr599$RiKf!AheK-
!WTRsZ0cQqVs0$FEez!Nop&#I~BI?rVb^%wrFx|G@8;+2=*gzlP9caO@KkN;OxQsfu7JAT|0W4}+E5Pb^VRa(u87icNdGGWAxkeo
ukPGXud);2Y-|0Xn23^1gr%YR*AW%N115^mw1|&~Ht4f4!4hN$yV2ag&akU(^J{=3&W;-
JbzKQaMq+*IJIfNzC=>pnXL%ZiVf`mB(tJeq8VcE6?L|ZP;Vpf7+!^Yi1lm}AVLjnv9txBuND9hsv_5kU7Ky+X=_OSeG(!>e_(hi
M<RR$CTW>T#0%0!q^*sL8W+ZlANu3Vu&1qRLt<`ED8HXD((oLEj1q|I?)6#=3EP}{QPCey`P0unRmK}WlteqU@Bg{%a?X#;r}0=B
~rXTctXyJ$sPtDK0%9cWe8u}2o{aIoo8O}#eaH;@r)2u%RQ1BkF5f!_9DzaQE#hr@oJymTwb3t)_+lb7M^$%|zVVD*k{*bzq~L0#
4{to0cRWrC*Yy7Gh2^HG!q_N_)A{g^o6z4vEd_dd_we>pt-ax_CRa<>2NZ2t%ap4q?l4}Si1w*O&vws-
J(c5Z{9{r>oAeYFZ}oi_Bh2lBVK4Cb{}xO{5YPJGu(NGEyehoqVDl%Cv2Wipf6=cE>{YV-
SG>G?5&#O5TmPc0anXz7!%A1wT&24ZT~=+y;5mc{CcP;aU-sQNeA_b>@AL#TDWx(_`!egZas?OzHlJ*z$V!Q~Y;>e*bV{Pj`m@I9
mqzSr{LtM8+}XdQ(2tNR2V{fmoW5kSkJ-}k^=ieYJ;)+%P9d=`L&UMlD>AV1ceDBb)=nSgqZk1`W-!Rys(nPyt7Zs$QrO-
^K<TX%h>f0oIx=Um|&$uGz7`aN`$1OS3O?fLWj%h^n+PK6S1ZYsqbY8@XNPlPIu>`7?@F^efmB=_@N38AikY&};-
sOR)jh6`d}V?J@FEf@a46L3`W$-*>Cd}Z><#xz@el|Vh8n$8v}P|+Dt8K#>`FTQ*-
BK9byzS`=3%|9BJ6rV`%iEWN1ySpuWx{IIT|HfnUqv6U-
vI0m}19x!&AVW{Vq=tYzA9`b%*KHbJ%QYJj>V=Gjc(mbhE*_m!eeDIYzgUC(9*4==2jPyEeWF1BRNJRD_1V272^RYE0E-
#QpyDvT7r3)R?E_+M(?)ED^;t_IKuizTp64e*WmXG0YDOgdmYoWaA?KDFMe$XNp;#54;Al-
7M%c8qK?~SZkXOs*+l~J`!axTsG{+zUKLyk5LqRA<$XYSks%y@JUAYMT{MRP{e2swb($-<mA~S8GUegV8^DT|c-
8)ppa<}ocgUAbjCO1u(9`1_wJdlXrWeIXn9-
AeUr!Op$3IK&Q6I@jEX>vVnd^B*a(zzC+rw~uLiUSfrKcq4)KT0Xq5UrWbSKgBmtFe<>wTW1hsB!xUtr2h{f-
|X$JoTw;<5eO1CsnPNuurlGvXof~NlJiUHE_Xwn(Trs7MXAOr%6W~pHaE1B&$}`sq_^ga*)2Dfjog#tRdAWcEEnYB09Y@t`gSK@q
<<y7d0Qy-
(T?W_yf;~LY5ma=|cgzeyW|U9ul?32n7t%(>Qn>*WM$Si#rZ#QSO&+Z4<bHgyEr_2MbOurwl#B5E?iHjf?=nd^ZoWqy=*+>6a`CX
(A+<J0FS|&@s)@f>2}r&veZHsmA=DV$99m-0-$t&oh*wNKRaS{Q2)<awfr4L$^s?ZOZlOAF_1pyEDLKwca}8bE2Z-
!z{)3`0syc6asMQ>MD;!+C+TfI^tbjndTTPNx^CJEn1E%9AKJnd53mw#2tKxP6S&TPkQSNOI25)2u{@>d4i;!C}Y#%e>zphUp!YX
;E?aNp#f6mXjGkAv&qy<PZTI=D*+T|#Mqfui4qEIpH$2f7C?0t{#?r+JdmE|0W4xJunqU_IUpg!2gF7gaWS+wMvIuyFqv<y3KFVg
<}S_?(9b5og`XWKpZ`HyhCBW7d6Pf91n`icJv0mgJI6l@_+##LOISd=Jk*~ymT*BXr!1XwgLI~aF)#N6k(z3kol?7QdJ;c(mu|T5
ky^l(8iql5DM<zqgpDtF;7_@gRg=7AJ5My#B2pS*YP%ag88l*qq;vYapiU@j1h%NAiDro;)BX;fcL?$Zu!D0v6%ou0!Q0SY=(WXm
Z73k5IG81Pm^4u<>-Ad!*6aSy97vL*n^5GMoYlabwCQBZGebQ_!t=Ht2+n*RFm>jGMWFA0<eG<_@jXb_>&oX46;dX-8~UPVU-
p~I6#IS7fdazE^LmPgqVOTW(P<mxIjm0$vn3hlopZrOU_}+>E=%RGpE(+5wlE1A-
^AZ5q=!z90kQKu156k44FSx(I9HVPW&s$x=2prS21x)6CZfK`N5_vkae_R*D}I7W)L?R`Sk^!W1H@ne7<A^3H?-
r+dZ|VrA{i?qKIE4y;VXSeQ8r&v?~p7@XBwpr;Gu`!fjsmVfy&{eZ22L*aBl+;GEiry;LqK}=MzbT82#GxYty?;=@OqvN?9j>bcz
Yz&cY$wX>(!#+sQr}cw*E-
epP2hCx*{_sN<snHKq^v2cCWLkn(>4;4rouaC}At49229#gjj^H$WE1V>3t5(r^|2@Z%M?#*w6vGfh5D6bfOB;?)DTNK~-
63gQ(SEX@{(8;~D(@jOoev<A<`Cv|wJPsf-~ylW-
u+V=KS?c?e`mRbiPNC|<5<Rd^qBF%V)6@xr~KM#PAqIw}%Keh9CKr4N66*N#{>6Ccyt~ssRmO<p3h?&c6%+UJ69;`MmK>pG$Ob;G
z$DEU}ik(GH9Yluul=*pHR(!+>fRWQEFiNW+#$^I+4vIN03sQ0(@hn=%H0eS8N0u*aj!}ieMIt`J+^k{`iio6*8wSZ0Y>YEX)n`a
+;YKxYBZLB!h<2&KRO{m1{c4SP1iKJa)OgIuqbNZIcBkbk(t=g}ka(){WK=a1i`6$^!Nz2xGNH*($xPx#xJ57{Ia*j6s3KVn^Es~
)^Aoew3&>e+e_9CJO&bj!0?+3;R;_X|HmPfnv$Tgiza{~d24YK7tDW~diZ%Km^keS2cDqW}FdFyqZtVhjrJ|-
yS}u^fi+CkO1SoZjZEI(ABDeawr2+2cRv#XY)0!)bAo(?oTT(`T<n~_{M7Hwdn6-i-
*O~Gt&yZsYI$*}%YxP^flfQ~j{*QU(b4gId0N@e+tv{=xD>DBfmq;HmU)ys;@rxi%)-
y483W(OLcl^Bd5zT?k1}Z!b&G8Y(cgJiPho}TQ#7(7C<-
1%Hfi?pYKWS|w96ZWpl4_h)T<Qw#7b25T%P!Zm^%dai?8;pNqdv=RBV)1d^Q2B`#i~~9q=GuXKo#=q?yoKGKfOR?ZIyco=cC4RIM
H}^Hd?Qm2Fb)o%E2lLQ=WlRs(J%=sd%+iOD^<s46*zQyh`XPMHULNnfCRRBl3lwIsS#ajd|m=aVi<wTldoEDF7+dc{54}TtN1d(+
hlrXGn_js<B5o#k3b;mXb0p^lY9nTWqm&%DkOZGh^~T8;_X^+-^OhuKN*{+m90m7O>mI-
<^5Wz%R{5GA2CD%UYb<DUKjGZF@`+=0MTIzM|Oragd<VtyLUcqRG1(GMK4#%@2T8imT3Dq#O)6b&`#wO~{2}EXs8C&(PF$43y{9v
~-
NSbH4ZMxIkea)<j+#>zE8Om#8Vhzc&4a;T|90AoGWHzT5$7=^?dY*iFQxiwoejVP?&prDU>~N=vkk8EoNZj`9i+jsSt>VV+YE+hG
(zl*#_V<fhrlz&@hl<t1nmX%2E!M<Tgeax-
}vwoEdnNZ^LM)Ygkw61d^2k3#T;%~yk+ebWS9*cloy1o~Ra@{xdxCn>O97;bakT$l~oF6hO>7dtO@8#r$ar-
|V}qo(JV#yR_?@eck!GK+aTQ&@%vldkyb!SYI_>|b>5@-ScWmj(hy%)#m!Se?mpy+5l@&FAE7Vf-OQLl9yV%6n3xNlzDHT!k10bS
+AP<tltZ60<EOiU}!mtFZW@{5dVm_jXXwIF)O*aDlYLCc2!Z1aN$pBh;SgpFG(V*)oJE%e&Z*rmP$m3~WP>O}~5&nGSw1MKj`zSU
`P=zl7bI@YxG=EmbD2Zk19ch}R0Jsd$QyTO`xJE>l{}v;I@5(n`fjOP4FR3zgLp<zp&Q(h^y`Qk*QFmFX;xE>zy|MTP7*PEgcTa%
QC@`Iu{#lq7F-?h<5#Nm3;~-
hk*R8NVn>xxME(z9{+=!e11XncS426Ru_jF0jA?W~E;#$UQ5?Ikr{FN)Zjpu~C1K**yNU!dMln@E?d^$FJua{yz#_6`VEAeI{XLB
9@}BFAG>r;A~+-gYl4iB)mHE)fTU|e08*vu(R4t`qrcZs<f8and&=jm3;QHaQ2)?K%?qEF<jIPMY7~-we-XuRbOJ}oNNZW6zzvni
c=JW8TI=pD&}qFGE)Z3tmD^$dlRT0c>0KEB&eDWlvco?v;u}@%B_i9G_{<Q`pS52Xj=V7Iuwnqc+=QE{^oz3dTDeChQ<7^kg|d}S
S1CbZ;zoCdCbXcWw~;_#6bHcqplfQk*-%bx|r?QcfHx#e_W@>SP@^kw{y>}&38W<L)&bPhIV7#M7IwR2j{JhLl2Eqne}<~Aoa(|-
Mt(8)UPYxjcd9&n$R7;Q=L<`0h&BSM^qCW=HBbX^N&W)W=_v+IVft(&4w{*4IA*=aCV^Okl32j)@{r|f^jUTCzHy8zJWX~^~{*JJ
{r(v)`uRO2&?(g7<9Xx5wo2kBsGU(AP`o!p|+E1>_J%;=s!XLp3{_UOcfvVteOLuBzJk~&tn(Z**XsGY`e}Q-
`X75bind?c5rBrG4A*5A@m%_AuUQQnpS&q<;F-rI=xvJ2tW!MF!zcCqS@kpT^Fo=rw5&vSk>w2c-0-
j+O<Z2S5DU+5?<LO$I<ZWzl0H;UaMm(oUok~1pq5LJ;Dnuv5Xg#hq^Kx^hgtj=m9Nfn4r*OIP8zuV9>L0rqK%mGL|r8xdJM}(`8P
xm`N$-xEh0?0n1g>xC+n*>969?;w7XZsi@oO4Hyi@Xq4(f@+9kx-cu@`j<?LQgM&%H&=kAZXT5%R1ml#0X2YB}Byu2oWvk=!Tb?@
%jPoL%IVO3KSILGG>B<LNf%LMX5v9||@^NG=+oJ?{(s&isXkw5T^7vYc@z{)JA!l{vRVU6G5YBC(g-YANZF%M_y{-
<9KI|Xw!=IxwVNHDc>({-L{n_5phuPj|G(bK&J2?9K<?HF}-
TukZ>Dm6l5hU(^{CM#G01BPXj`vPa>%hL<np*)M@14E>G&|Wp{qp(i85uBt`to^yc5rmIe{zmi&if~42LN#IY+u2nzHW#3X?AvUa
11c8jb|rc_h;|Ed^mv8*zVJVpO5xGK+4yn4|^xSp%Jx&DrROoSXuJR$-
&PDnwj;%;oi@pxj&!meO66WW10tdcCz<=Uks%V`TeK;_x}_H&FwC;VtXwbjf<UBGaCPojl*3$_3?m-
0BRdQjU@un>5m_}^QG^N(H0!`Ygo!IYOSJsItTiU2G5WXx#(~R<t}GWzYYJr+I%?u=WqA@<M`{pZ@Lf5&El6CT9x14uMt}9^wS<J
)9)cHQ)@KrSOa_HyB(+J_4|Fxg&)rv+Me%OgT-jxvF4+pwXpk(es|z?=R@1~d!DlxIu5kp)BSSEYU}vkZ(X=y4!K*TF~f<tB~2(E
E(=RQ-
>Z?$HEK*RFdB_$zX&ZO`y%YH$3mmJL#q$UD~tI=*q+xe0)HuiE#+9GgQIN8|4ZiMOqnrmu_I@f3y&=qx6j#=%a<!R!Eb52m?}f_v
%Rle5!!L>{oXOsSBs6zf(3f*&zqpv{+bPX?f;1pdhK~Dba!JM7h6n*!62k&TDD_z2dV9`S!oW6aIPGLBS^!s3Yvp9HOIPk4J#=&%
t(6$e858W#%vjB&nR8x$&BSE(~PG{{5uk}kJ+&>DbpqMc=eEGRt2bAP^us=JzNE_erab}J)n!eu%3$PebREKq@V!!Waet^BJ6gwi
j0C)EGA16OI_~*&2EyK6`Q!th99M)%T=h4CyefP73eW+%C$YA<*0p=zrPiH3GUfOVIPhW8jv0r%||_cj~In^d98cID74c9&`s{?w
v^xCy<uS1CT2jDMeR44W@8#25A}0f^`2sV6f&aEzY4a%$h>xs2@L}`zOmmBXC!{!dx6TDjR$dI2&9d)0HXjHTZc!Mg)xbiZiwc5x
-BrfW;Z1xK7rc;<ITK{cc|H{9-
|@$^*lnSc|5t1uTYoAalwV+J*U&eLoGC|3}FeBwUx=zUEJ`AC>)tBPoL);9ApkDxB13;gHb%h3kD6#K5?FXL1&7J8groDVxCZH<X
W1RGNeAWJPlj?kOMh38pdNAo>#Xxe5*JsVl+bL<z#i?27r9SV*`qq#k_!QUa;Xn=#7SEny*`Be>5I<b|8~hwvbcI^5oMLYLast<=
rff&4T^4w7Z^W7N<#$x_m+#X2K<c-G+VaHZgKbCtgK7M1lXhOd_$iPiRgLoW~=A-
je6~Zye!h(|j8#<5R>VMUtr?LNa%QoEly?9EVQu$!#==G%^lkM943&K=Q~W46QT7CiSE(;x`G+Ws2nV?&Lq2(z^K#U=Jp?V`Lu^U
nh&nn$ss#UpyL!a->9sL7@RpEz(7Q33Rf?=xO-
0n_yI!Pr6ZX(#BoJfbz<uGmX_26i$LEdp1(|`iHW}Bn#h{gS=J2(jvX#XEA1Ji)F~Sg21BMs;pz7c3~h(a5Ed(w6UsyPJ;l2XuK<
%h8Cvkt>TzM8g)0;qGRh4@e4Hz?o{VU4c$!*lYv1X^JP=m&0fes(wdR=#0`@N42?0Fj_IsEx3XgYLhRcU)lZ5V23$!&fv!FSu4yA
7b^A5V*#qk+?e>K+`VTeyc-Z!gLVrwF1II6%k!6-
v4O(*%gR#)It#xeD&MJre;Vrky0A71kP)pAWpb~r(EZ)tuP+zwKm>Xu!B3{BCata+Ww`qoRrYz0Hx(?G%wBx&x|Hz>QY~f>&ANXE
$6%g>qJwQF%${Rs_g8vjdan25T_Td>8BP9{)fe9*4f0-Zx^p{<5BezajwoX~LPEB^svGPN9$tx}98KFA<Nm-f25-
7z96FwRMYvV6j5_o>b)|_OfJ7W=#OfUkXM1(X03Y9qm;)WxUuJd_h%83L4t7&Wig{C>y2XmgJUIcj)dWupO01t@2*HfVE1<M#NbL
<%Mp(V2xSYc?KLIQ0o0~}m8h=W3hN10@nQP<q+>Ix{d#n&}g;x!Jh2rj(14_^aM8G}T+F-
Sy5RMe_44i;B9%^r)~Al70&!ap$B@9I;W=kxlsfju}OQxh^Y!LLWzS87o9Ik!#(9C_G*TWLBN8FFaIWTwR9gzQ7Os0pn|WMu-NtV
B550B8Nf56k5Jr08ygrze2wX?Be#IVn25$u6sgp}|Cm?k!4GIT10pW<f#*v1@26ffv%+I!V1iaBRz(>Z}oDQR0}UDo7($_}nRc#z
Zr}CUR4Mk{%2Biz_z_7Kw49X7(GO2r4dSta=_`RfBL>U@o)0>7?oi`UkP5t&Cfh6{I`EkG!$<GGnC_Vfv8~Cc&mD72byb9_&u0Tj
uKzXzg7wM<yCkRi-I<P6{`OTl|CX-hhZTt|hMLiN20&S8jX@&-
so&M}RKa6;I>j3ij$#A=+j(T4s*tp{cyC;DA1G@>2bVNQZOv4Y%!YB(E{?;aYtN@WZwGKs}vYh>zms3cWT(YA(~2p6Nnmx|-
(1plAaXs7d;OBJ?=ISe#iBauLxT0LYRYk#wacb#zjT6Oh|%DIlY8=$6444H#9Eec&I=yhMs3;s@g0<(zHv4$boNjPzhEQ{Ce60|}
bN%>ui*L!E7k?g_bEZl2$=E#aHo625KU5(+9CKsepymEb<-
<4R6g$Oq@mbv^)_r0}$=XhOQ(RH!6z@J<a0%uImd58(QJSe0{==G@4fRon`$7y8RGtu6)RWD=(MVQC%efvMFdf7$8RPlAyV-
v#fYa*H>a74VnV>?Gru_>E+Vq?mmpm<lNu(SS=4*qpL-ZL0@jc)o}4_D=U-<7tKjHTK=*EWtBQ+Bp?bmF_NxG!a>lR8!S-
Q&0g{Ni~-
b)C~W;=W=rvIwi@DQFLfannt&5GWuj`sK;9E%gd!iq0$Zw`zq(}>9_fXeu_B`F^8nm<**I!DFgdb<)tYZ2?YO6fQKJil9GwQFGu3
bk*XMt&lH#VL)D@UWX3Q4;Qvilap~T^mRXFV{N|PC6_7*#utqLfkc(2rXL!j|u2ifO1Cfg%7pQ9tBQzv@WQ!jhcF)sE9Tk-
IX+|m_Nhm8*mT3Xh6-wAGDrT0~_F@(L{5=Ey)sOiXCf%`Tk3aZn`m*rxBs1{%B4K4gOy!d1HW-iDfQ*26><7?c5r1=HYa-pL#sO9
U`~k~_)PvhgrLs%jFCn)`H7^Gx#VIQs#hILPVw#&?(feVw^m0NE>J%p_FWby`@~nAKWLi2#M`fa_>==m7DY54}7wnW+b9k5&tG}Z
p>@1=<z++haHNFzR=4rt(E_+)i7TM~|*eK3_&2hnUk;;`sUvtc+gz@{!{P!Q6Z_V{<maEvbB7==BD5UAGA(8GHg2UP(S{zB&kVv|
Qq*S`-8X`PGBK^Q3=Ry>*IFndmHcVyfOCWb(F0r)9Xd<;Yw1S_DH{dwplClY8?-
_**&NJI#IyzyVkcrJkI;f2CT8^ZoM?wXNFoYBQWr%jx%VpVURE4~uEU5N?ZL0aAPDr?qM5V)v={Sn<c(Njf5Yh2vvKz$>{-
ekk;W;rE?cIsu(g_uxh%EAGpZqt};<HUDHfURgXpHpas30gc4Gvn%r=VVfH7zx**5tK`1`dxSUjS0psTaVC39i^^DMmY<_f5sL=k
#4-_?XPGUH3(MXNq)XwU>qoQvF4By-EQl8JsQ)<}3(97Cf@xi3LAOx-YeI(yYP@MKB}m7b)h8hohoBjS;|R2Y~U<k8SQKf@>-
Iq(DumObEJ-0Luw2gQS_TS1NHCh)pIs|5~w2lDFHhEVcjUNMC>9zp&4<RD)MoA;;4SOe{MQX+xD-vdol@j;5>v%o;E$iHPf+0cFZ
IXfZI8(}obniB9FUIn9FlrfLI*jZp!x|00070^qz1KyK&X!{fb^{i8Epf6knxuCmQeKkf1Qe`?7B;P$^A@4r9W2PwSQw?-
X{)#|o4?~fLpMYn&^_ZI%ZzPRX&hNFSob^84adt~*kVfVu8&8?n~Mfw+mxi$2ikvnwZTOVzUjy`1jHQxM_`=Jj1RQnQpL5P0eZUR
&2VWb=ptqxDak})}dyK%6-y7loIrXWdgRFZettU(&XjWD(46=BMy!CPuG5Gjj+2u%b~432c;0Ey{QdeBc{u-
IK@U@W&EWXc3Q64dU@TztF7QqZ^<_LU}od?wRfA(OKAz<$Lkmlq`q7w|e_ZWc!ob4=Wv!-}#piEi(gmF-tS??mHU_6yA~xMm8%Tx
@&u8e89Zdba)O*AFd9qp2j%MN|Y~xv_4#Ie@9<H`$Pan1Bs<OxRPRhiMeu)H{W7PYU`e+*w3Py@yEj`Q)h>b5QJQS>eZ|BJg1FH-
5cK0Mta`1YiQ2w0;o73XHyukph31d8-
pnxCRdlvzOyDiIKza=v!6VA!R?dsp2!!+K7=sE)zi?Io)Kjo66@hfT_CaNM;hqqFf!cvr<fa!$q#Dz>g}jr0&a65mIrh=kE=McT^
D&n;@A`;KLhsZ8nyxM#H#i!ILr)Ze0JF=!v3fuMVM@_9Ts?2#mOJ$`D@820BZmPL>%Vl7uN!i(?3{>8`$~l9M6IC`^o=%1xnDY$_
y|%~i1Dpa%tcT&VfDOOcJ7Wbl?4bc|C63WE6E5yN8b-
tjv;0hf7Fm%I6#XDD*VaQdJ!v&tH}%20@UAnsX^U7)6rCkre1>2dMSN}*Nw9ZTE5$zM&9b~HJamiR_7xGCxh(6R;19%XzUagab){
5`B%QQ$9f5qV|3Ss<SX(RE1s6Z(AMFWvQl@8}Ys=!k+ZR;nEHiQL)njy5*58)ti8tN8$(AWTy6b;?x2h@cE1MSlUNqU97g(6k-
dyi=5=UaALOCAl`LDq5*~hpf9I4S%T9CVthuB?>GhR#F}~eY}(}f!IT3Tc8-
}@MIu6C|@zsIc$tHhGB%Uq@FeTpO8Vn$Ud}e=o^7|Fxt6%?pOq-sIaT{BPn<UY;hnNLCbR9BQiT+Lo4@no3}|sNZ1wg4$K#|xoZy
vYK<HxMZ#b^`jJOR1p>Z=dYzt_0f`dYYbE*xfOwI_v@M91I*MqBR!F0n5Y8opYMF;c5zz#m<;O;rtirSm)e4v<98`(}I$!9xrXd?
JxXc-his-hW*7OEAfz*{@rw91drKuVXdUhAO*%7b0Ye`upHeZzdPja3n1;o?yrT!+)s8i`{A`nmey45*F`ZaN)<C!Ou@?v6h;TOr
X0bv=<1w^PKcFWa6>f(dEzm;<POt{MF0bMdDqbg7;zmMR!=7Pj1inUASvoWgz;Xi_uh_0Zs*hhZ`+=I5DL{;&e!xA^j_`&i%Mtr`
g0z*NpJmEi~`J0xfr9$Y|eb2aj$;|?LZp2q;Jy)r(uAB>`!>l;$*)CBAqfLZP9N9DDo+tVhFt-
i5+yP2MKCf<<7YHG7CVgYokav4{y=)HKM>?vDYARrEpT#^?uWZh31RTrkv+zpB1%)?6^eo4+i6@m`)8%H{RbbLs8W$-
Xz+ucw8sa2P?GO5_JM22$UUo<z{l-#`--
mpK*h|~3*zvgVzZ5`H8fl1VZZo`GQbbo%`a)sCm9lzYM8u&zx?P!$BGpBY7_lD1$)O+3lFnnpOA0F_dAo9`X`$IGns-
zg9{w4l!<P&WDN0c}4s%(-{E)>S>gT`wnP|wB#)C!MK^lo_%Rz|?nX#Zyh^BUODL1V=5!HA|5eOE~IB{>GEJu-
Le8R<fjLa=QWkICzzyyyuj3Kjo<lv)Od0#wh+VoRx4;cM{h3f)|l?U=WEX*t4i&vp09VEL-wtd5E9gv3??mfs*fHw-xVznYA6uMT
CH#ZQ)P?*-XYadD2L*(*nS0G<3W$fl~6-
HN235K+R#bnhUKvY*(CSWvC{%jDJF@@jAo7@O9_6lbQ;3&Fg=`^G&a17O4K+t2JuKhIXnNd3JFw6S*R8RhV08-
s}hU=;sY78rctfX*zRRXjrh9sw)$F+snsfBK!=%MDz;Z23Gts9mkzWS!eByAX(nQy`PE%!=M)2C)`%ut+${wqP@r`oA|>(>Bxf^{
0!Qe7esyClU#RN=o-
t(gG9U&TbY#2q!l)GddZxLnr0pj0rbsAflNm#5l&h|2m)UpS!%k3j2<|AyNjn^YoVWmJ|iE|fe~)Nj7j(eCL_Al+ueZg1sTN(He`
F;dd|!c867!Occq>LC>$x3`n)RxTtYHD6^fV_&8jJ7<UA*x_&N@ZV%%kQBpmBWuruq(L`QA~7rS?uXwvKm3jII%!_pQ4fOi2Z^9q
?B7(xMg@_S>wr7g_2B}HEcNbKh*sxHoDtFu{-
G|I&<DXoA(tn+cXZ74+%lsGrfDj4dbe6%)pUO#jY=xit36z;mcHZ{>IooQ3`<djXRV#R>FhXdbpj0~ISGE}?A@`f<kF3Df+6KXej
Cq)MbgnRNoQ&PN|FHSL=@x@%4}-
Ya;3f6==y?l;4raFPKogDSfrMOuuU3~q@dm+ZX$0@An_IX&!Z2fmTlVs8htEyn27vjd2~LJar|W>85_Z*ArEo*8~y!v=1`djK(<8
~UIQde9mbJJcW}eelFvkPcgQ*gNwLBp7yaLmncHT$AYm3aVxf>j&RqIE12v@~3(zs;NBu4D^me+ilrL&Ppt?I9#~xGiNToSDcE8s
y%DtpeeS>|1ulNA0r(>IMu7a|p<QJtNm~-IUF4i-
3Vmb347t4Fk_k_l^B07{7?N@pq<n9{CEJIZK1s4oV71LiCUyD;R(*ySKb5@Sx#0^EQsw9D2R38o)UWgRLVTozWJY7{Bke&giS0AT
7AN!WeC0J3G=6oh)s<bIQ)leY~nzCFjt#yJyClWDbBFKP@Xqd`uH0vNJxpCspLg39xSp<euwC&Ol@38=3E?pSF=`jr_DTO()=+!!
@03@$S7DiTuLeTvDXF0zfjCqWhBh8Sc8^Yrn=Wi8CPlOqH-92NnrQ)|*Z{}~*Nz5|3a=G1_kM~od-@@}H`hb^b>D-
H~VyX__QhT8B1E&IHfHh9tnIs{c`)gPDs4~0tVD3Dq9QfgFcI!jZe0a<4vc-R*TffJtFOC8Eb1`VOK<-=^7A3-
>D4|~IhSYu(`w6TP;*WVf<`IGuefVLH5y0bz=F@v~C#kDz9n!nAMKhvubq01%8Zpu1%hhI8HK9n-
Qcc*y_&VuZJx9^@mDL7D>VY9N8;>pgEk`bhS?*l<;u#+V?TQ=WgK($r)k2iXl4F^yX!eOuI8jShwCf-
3|4Xfvn(JM=sQ)2H4wSt2*gkvDKD5<sToIq>=mp!=evVsq^2~E*I&JFj-Ce~WEthvvJ_MjjAujxo^O1cqr*5g2$$+A1wbf#A9|K}
S314!<z=cR9kklDaAd%Z3Nd(7z@5}Udr3E3hLj;+9(Ml$FI|~$>>~<-
{?4KJWWvz<BC>OdGg+>ZJ#7Q*NpzL>wX46<U)4c#e07_yCBgpZu@3;2jeZC{V3cn*kWB9MaOq$T?S7JZ(FYgMbk(dT7$D7o{G&?f
RnOeg5P}=)kqFl15J{0O3dVD9Ir5nquy>kMKOTElE6gR((!%({Zhq?$6udYQHSPFKKSta~gRS?Zke%hrX=0;q-
WmPDMibmGC#x!}}`TL1I3d#Eih8Blj>=;fX)I0N2?d%FxEG}9oZ+tX&{x|$zLVOvj4t0eXhd_^1hgC_tthOFR;GzZ_+00!Vo7Cnc
-@b;CIzWYNW12f!0ME@Gm!<E_@g`O;F}(QdWj|%`i6g&bo7l`b)5@<cD8h+UZthws_1wgIzXcO2yo`hb=hk<_+C8oIV4c)f4`h@g
F4t}6-SKasqW@s#QOWn`ro9-I_n|P;>lh=;z+X!`_rs&35-Mk2?@E)q52?xMV``-
RsPuuIeD7yCQd||@$<J}#oxm@75NtLare`cikS=rBY#J%p%9xj%%^NkHg&Xp4y*K%0BUgTtBixb+YTlcQ;wca@5PTODXVCG~z>r{
69?fh2+|5+sI~J$UF#*bt5j~kzB$G@3&?YrrqnPyJo%--DSCo?EaGaD~QA7#(-
4I~NeD@BgRhHQ4mYM_N;M)_;!6c3)tB1>{iOUW52IN+<mm&-z<Z;}{h<YQAize&zL1b<iVjOlvt4w--C*I!`EmKc4n2mHz%Ll<1m
AYwkl{akaE~4&kxQKX_bHX@@_-
P~AxroL;BCb3QqKv_H_<YBpV2F($kxAx#Nwjkc94{o=JEvwNDcpuhY%$G;^Cnlg+Gci^#X!Gu<2C=4Q7ZBuGt^mT@~Qm(z5-
SE`951*t$+s=fzi2S>De6zbmcLlM&Tb;U{>?5RR>#Ai#^)}Nibi6RQeQy?CweDHgT3G*8{!CBqfB>!WUTjjHsHp8=%9ydRnUt)^G
2Z>mXVNAl}8XI3$aM1Vla(y$V><aH<YD<=N>AWnYbPFG#-
pM<iw3geQ@bR>iz%NRk;u7D6a$22Oh^E52_J)Rs&4N>Ypg)ElE}1+ARqj&{Fv;~K>_+&={(k1+)lFt-
L9zZVCn6~!2F6tJNdAx2!{W#+*B1Ako${RgQ4sdZR~PSTKzNN<cz@1;yEa(5W7@wdl@u!SSj)FHhaq^M;8TiOH_oAh6EjedpV%~n
s%#6nFVz1iAR{`Awxfk+|b0Hoz@=DMiim}-sKezmdtfZiKwbWxCQIcQBKG_sC3N*~~pl|@Pm`NVFLS8-
aBMMbCu|0gc4HPWn#qV%Si&5oztaHf2qyi^o)A9Nom^vaU*No0=UZ5vaM-a4uoluewo*%q@0=|S5bdxz2!h{1)6REBK8I*`pA-
?I&S;K+e|V0(fUd9NPc!Nb_|*B5yGF&$r0?mW3v-~XogI&s|vkh;79=npQO^!IXtw{UJk&_4+DjsnL-bw4W7Hta{1ro<||e}Yd`y
*Y=%G}yfooI1?zNCApoEURb?Q~}74gK17Vf8i*-
Wa69dTyLe<Gv%c=E2)?w!RDns`b?V~ecgr$di>JVUW)P;Jj;Z6y!ZrL^IHtMh$j`Pt(wU1C0nC+i6*IF5|NA_kuHa{JX(XmvH}!S
{zZ2j;|fvv{Jqk$$TTM@+)Z|!^a9nCW^;vMzOu$mTONcV+Mv96TS%1N5t7Y-
k~r^|%a<m$N%dq5mpD9tf@lYD@28$;kdp6ZT%p`hYK62Q>J?szTd=Lb{+Y*@3{d7rJr)_ap^o^P#~oFo3VGDG0`|bO(}Q*76iy)U
xS^r}c+rr1Q=gU;U=laCD#4z)U|x`BSy$>qTiG$#_TR{w&I|o|mwkFy?(&;#?WoQ7y*j{^BIzphTfmF}U4qS69<qtMv{vEri8OJ^
dKLR#ExCo>w1oX~yi%qG>c$$ifV!;5`kG7VMP&F<&OhO`#y#26fbzIFqNKb$)cVZdq@x;@$6IU)I)4_%JZCL}=R4z9nM(k~<dx<U
wpFl~s5-cgl5I!VuEpk-
x>84u=L@DgPi0#Pi@8>Iv5uA9tYhUYCa7O8+B_5wM=Q^{@xaS`#(+jmggU$%zt%e7FB=DJA7g1Au&A^R5JN641IB;W7~n710+f#3
wexGpsP0e6r~k&(MJnoC`|#gPU8a&dmd``W->SkgaQT~6(h&MmX3?nW_$o*f9m^TeMwjNt<G+%94L0HEnCZsabY{<5{f4T-
)ciigv05dVGK_vhHK=&RUpjZE=4FTYR88qjUpJI4p6%z3>`Q0-DR-TjsR`@m;vH#QkBEU13&}hat7a4`Y|D{x&Mvcf#~G&tR=j15
s{~fM?+k?b>N>WaCL{T%2$!eUx;n0|2KuK?p<i?6TwRTJArDu`#&i=}g+8owsSl?VR=U7PV2-I@(^-guAx0nz{i17SK%|-
_S1t@@x)mqf09kTvN%4_kmei{mMX*YPU@87(V7M+5X5Y2bZa_#se9pKRBz|#BjlnNSf=TfvmC9tgW?RNn5vUA$xmwUP;Vwyy757M
puv26XEv*@dO)PyMR$4<-rpzK4bI-(S+KfWf8EA+C&4tncqmNIFY=Ei?CczKv9xyXib?F}GvOH<fwyssmQvpcH5-
^~mmt3V(u0%ae5)kfJTbt+0B3FF$<!t88q{{C7m&0uYgr-^|YaWHg&9aOlFL5mhQ-
;}0BXilK7SqyqL*r5N@eGoH4E7hk@yI@=XFAC`hHTZjaKWS*f4|ukK=ZMu9#zDtKdNDfctH$(wagUOBnL^r$;aJ#OkG&<8U#ak@)
hB*=&}SZT;Z8`!*$Iw=XfTa2YKF;uzKK9i)L0-&GE9XPTebvY>#$Q4~v_00k9?0wk(8D*tS{MVx1oAz^bsAGh|K=^-
CICBxF|9^o&m`jn8~CKGP%GY>#R~ZgI+Z*i>O{Dg(*L$d1+W--&Lhos-
Z`zkVWp63`F4=c&{n6lqSLk?OV*?h~}IOJ#kEfaGW*T<*GMO_CG0oQ}*Lzl9I|yoE3f>st;}vHPdtz8z^(^tk4_@ea&Jx7>5cF{$
f{VH~H|SE$Jb`E{Qg7)Y4ZF|-s&oz@%q=0579d(KnG@%*(y&)({OC{0w9-
?4tDdj+Jb`v=QIV#pvTGC&ES4RGL<NQ_dnFj^&~Eez6Sefl?b;r6!pAN6T*=4nB~s_Qsu_#&F4ZRZ2fgtNV`ZzxasTP1YIq6IxnD
@XxsuOt@(K))&}Cl2DxJiNYt`hM^D;OOVs$rspH>P@8BNGe#iFJ-$Vpydl^o%-
H$QoZe@c#aq^HzD|6$t7xC<Nd#y`eCtJB5P}`=GSIE4xP3kz(={Ql%go8WkA?Aza|{eXoyVS&1zR;1*th=QxT16BTKgdvG0AnB0#
lvQw%^^Xl#D}+77t{FddHjbvfF6)(Kb;-
BC#=j1=@%5ltEinWADj%2dp|`J2=mV|XTL4CKm!RLbah8=+2pnAAV07`V5TH)}__!DeIWE(Nm{`-
@eKHyHCm+qcD?$X(B<bvr?UKEB*w5PE9AO29yOxR&a)-Pc*2?men&$4Lg=@#x*(Mu{P~2gw<rt7E*L;awww&q{n`$%)-
I01~V3)=jfn|Nb2>fb_$~%1f_5z`Kh0vo}U&c8*y~IhW1c#q#Zk7&xHW{ArDMt-
0y|ME5zNY;^Uc$c36Q_aOzX0`TCG8%{ID;84_)uDk)LOx~T;2BPBh`jpnb@*lkbq&&RNl5+(ocMq7nqwC-MCttQ))J0d7eFC=W!|
eRa=dXwRvk&;??6=vwuaNUBy)8_Gdi(`49GvgZKG7{-<f2M|jt-8*tz)ONvwwYoTA+S<N-tSE{_^>^qc4XC=>=wa$as<3{_*L-
XK2}QX7^?zajzN?zmI!|2cLhN4J^DG4cI(r@`rtZdw6iPm)-
%FhqwQE|9l@hDTaZd$Sd0DHnr1iAjG9@RM{zvBc)UT6nDmzu9A~Yb8IW$B-
Gr@dX_c&4C6p|vcUstZf3|GR#ouv%L$A<4dj=99nr0EAHTw=9PYpWw0Csyo-
V38I{kWz*UUls@yWp<O~xq*9!E6MRn1N>kvlryKRMN}k;CaZ*$1#6_n^yI=hveHXvLwta4x;KZtD$mVwz9(-
+uwvzsY;)UX8i0xQFhK|MPzV`aL~J
'''
def verify(raw,pin):
    assert (len(raw),hashlib.sha256(raw).hexdigest())==pin

def main():
    assert len(sys.argv)==3 and sys.argv[1] in ('sources','build','check')
    mode=sys.argv[1];out=Path(sys.argv[2]).resolve();out.mkdir(parents=True,exist_ok=True)
    raw=zlib.decompress(base64.b85decode(''.join(BLOB.split())))
    verify(raw,PAYLOAD_PIN);data=json.loads(raw);assert set(data)==set(SOURCE_PINS)
    for name in sorted(data):
        value=data[name].encode();verify(value,SOURCE_PINS[name]);p=out/name
        if p.exists():assert p.read_bytes()==value
        else:p.write_bytes(value)
    if mode!='sources':
        for name,args in [('trace_tail_exact.py',[mode]),('trace_tail_check.py',[])]:
            subprocess.run([sys.executable,'-S',str(out/name),*args],cwd=out,check=True)
        verify((out/'trace_tail_exact.json').read_bytes(),REPORT_PIN)
    print('COMMON_EDGE_ROOT_EXTENSION_WEIGHTED_TAIL_SELF_CONTAINED_RECOVERY_PASS',mode)
if __name__=='__main__':main()
```
