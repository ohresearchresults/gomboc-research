# material-d0ec0d224224

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# FACET_INTERIOR_CAP_E17_V1
## Recovery capsule part 2 of 2: continuous geometric proof and exact reconstruction

## 1. Result and exact scope

There is a two-parameter family of genuine uniform convex polyhedra with V10/E17/F9 for which a strictly stable root facet B has an open root-cap intersection with the relative interior of every neighboring maximal facet, although its closed root cap misses the ENTIRE true one-skeleton. This is stronger than failure of a vertex-only test: even exact optimization over all genuine edges cannot find the witnesses. Each family member therefore has at least two strict stable equilibria by the root-star theorem proved below. The construction is not an own110 candidate. It gives neither an all-SPD exclusion of its shape family nor exclusion of the full E17 realization space. No FULL/LOCAL incidence counter or global bound changes. The accepted gap remains34<=C_min<=622.

The method also gives a complete exact finite optimizer of the root-cap quadratic over an actual maximal facet for arbitrary one reciprocal SPD pair M,N=M^-1. Its interior candidate has an explicit formula in the two facet poles. This method is not itself a universal S1 exclusion.

Object identity FACET_INTERIOR_CAP_E17_V1 is distinct from the earlier TWO_SINK_PRISMATOID_V1/PRISMATOID_ALL_SPD_U2_V1 family; their coordinates, centroids and certificate tables are not aliases.

## 2. Exact source dependencies and reconstruction

Part1 is material `[internal-source-reference]`. Save its entire literal text, with LF and final LF, as `facet_interior_cap.py`. Its only executable dependency is the unchanged complete `cap_geometry.py` in `[internal-source-reference]`; save that literal material under that filename. Both sources were fully read. The old root-star proof source `[internal-source-reference]` was also read fully; the needed theorem is reproved here so this proof is self-contained. No numerical checkpoint, private source path, random seed, floating optimization or unstated parameter is needed.

Executed environment: CPython3.13.5, standard library only, assertions enabled. Exact commands:

```sh
python -S facet_interior_cap.py build > build.stdout
python -S facet_interior_cap.py check > check.stdout
mkdir cold
cp cap_geometry.py facet_interior_cap.py cold/
(cd cold && python -S facet_interior_cap.py build > build.stdout && python -S facet_interior_cap.py check > check.stdout)
cmp facet_interior_cap_report.json cold/facet_interior_cap_report.json
cmp build.stdout cold/build.stdout
cmp check.stdout cold/check.stdout
```

All these operations actually completed. The source-only cold reconstruction produced the same exact report. The report is derived output, not an additional missing input; the two source units reconstruct every coordinate, incidence, polynomial coefficient, true moment, cap maximizer and mechanical primitive.

Exact pins:

|File|Bytes|SHA256|
|---|---:|---|
|cap_geometry.py|4942|192e14a57e44b4f31d4b8af0039616fa4cf004af91322f214eef1472bfb71fb5|
|facet_interior_cap.py|11227|db081d5ffd40187b601078dee9e7d33ed83cb70ce5c34c8558d3ed704d86790c|
|facet_interior_cap_report.json|51074|342e2054dec54bdd2f4bbba5896829f73635067aeb2f2806627f750fe1627209|
|build.stdout|354|6dfaebcbd8bc5019fefad800b213f4a8a9ecb3e5326f2f30d000acff842dcd57|
|check.stdout|354|6dfaebcbd8bc5019fefad800b213f4a8a9ecb3e5326f2f30d000acff842dcd57|

Complete observed stdout in each mode:

```text
REPORT 51074 342e2054dec54bdd2f4bbba5896829f73635067aeb2f2806627f750fe1627209
CONTINUOUS_TRUE_10_17_9_SUPPORTS_TURNS_AND_MOMENTS_PASS 140
ROOT_CAP_MISSES_ENTIRE_TRUE_ONE_SKELETON_UNIFORMLY_PASS
ALL_FOUR_ROOT_NEIGHBORS_HAVE_STRICT_FACET_INTERIOR_CAP_WITNESSES_PASS
ACTUAL_SAMPLE_6_5_9_WEAK000_ALL_68_PRIMITIVES_NONZERO_PASS
FACET_INTERIOR_CAP_E17_V1_PASS
```

The code verifies140 exact nonnegative-coefficient Bernstein polynomial guards with strictly positive final coefficient on0<t<=1/100, not140 sample points. Their complete power and Bernstein coefficients are reconstructed in the report. Positive vertical affine scaling treats H. Actual geometry and all physical primitive signs are additionally computed at the explicit rational sample. Analytic proofs below justify the continuous cap and equilibrium implications; a hash receipt is not that proof.

## 3. General finite root-cap optimizer

Let a convex polytope P contain0 in its interior, with true maximal facets p_f.x=1 and inequalities p_f.x<=1. Let M be positive definite, N=M^-1. For a chosen root pole q set

    alpha=q^T N q,
    Delta(x)=(2-q.x)^2-alpha x^T M x,
    K=alpha M-qq^T.

Cauchy gives K positive semidefinite, rank2, kernel span(Nq). Expansion gives

    Delta(x)=4-4q.x-x^T Kx.

On any genuine edge x=a+s d,0<=s<=1,

    Delta(a+s d)=Delta(a)+L s-C s^2,
    C=d^T Kd>=0,
    L=-4q.d-2a^T Kd.

Its exact maximum occurs at an endpoint or at s=L/(2C) when C>0 and this parameter lies inside the edge. If C=0, Delta is affine and endpoints suffice.

On the affine plane p.x=1 define beta=p^T Nq and rho=p^T Np. If beta!=0, K is positive definite on the plane's tangent space; its unique maximum is

    x_*=[(beta-2rho)/beta^2]Nq+(2/beta)Np,
    Delta(x_*)=4alpha(rho-beta)/beta^2.

Indeed p.x_*=1 and Kx_*+2q=(2alpha/beta)p, the exact stationary equation. The negative-definite tangent Hessian then proves the maximum formula. If beta=0, Nq is tangent and the derivative of Delta along Nq is -4alpha!=0, so there is no relative-interior stationary point of a compact facet; every facet maximum lies on its boundary.

Therefore the complete maximum on a true polygonal facet is the maximum of the exact edge candidates and, when beta!=0 and x_* satisfies every actual support inequality, the one interior candidate x_*. This is a finite rational procedure for rational P,M,N. The source obtains the same interior point by an independent2x2 tangent solve and asserts agreement with the closed formula. Degenerate harmless zeros do not invalidate this optimizer. At most three vertices of the facet suffice to express an interior witness, but those barycentric combinations are not genuine new vertices or edges.

The full-plane maximum is positive precisely when rho>beta, the negation of the weak pole arrow p->q given by p^T N(q-p)>=0. It does NOT follow that the corresponding x_* lies in the compact actual facet: the support-inequality test is essential.

## 4. Root-star cap theorem, including strictness

Suppose B is strictly stable, with pole q. Suppose every actual facet F neighboring B has a point a in F with Delta(a)>0. Then P has another STRICT stable facet.

For a neighbor with pole p, a weak exit arrow p->q would mean p^T N(q-p)>=0, equivalently

    ||p-q/2||_N^2<=alpha/4.

Since p.a=1 and q.a<=1, Cauchy yields

    (1-q.a/2)^2 <= (alpha/4) a^T Ma,

contradicting Delta(a)>0. Thus no neighbor can have such a weak arrow into q. Choose a pole p other than q with largest N-norm among those remaining poles. For any neighbor r!=q,

    p^T N(r-p)=(||r||_N^2-||p||_N^2-||r-p||_N^2)/2<0.

For its possible neighbor q the same strict inequality follows from the eliminated weak arrow. Hence p is a strict unstable vertex of the actual polar, equivalently a strict stable primal facet. The polar uses the same origin and reciprocal metric; it is never independently recentered.

Closed witnesses Delta>=0 do not prove this strict conclusion: they can leave a physical EF wall. Our family uses uniformly positive witnesses and uniformly negative values on edges, so this equality issue does not arise.

## 5. Complete two-parameter shape and actual face lattice

Parameters:

    0<t<=1/100,
    53/30<=H<=177/100.

The ten raw vertices, with fixed labels, are:

    0=(-1,-1,0), 1=(1,-1,0), 2=(1,1,0), 3=(-1,1,0),
    4=(3,3,H), 5=(-3,3,H), 6=(-3-t,1,H),
    7=(-3-6t/5,0,H), 8=(-3,-3,H), 9=(3,-3,H).

The actual oriented maximal cycles are exactly:

    F0=(0,3,2,1), F1=(0,1,9,8), F2=(0,7,3),
    F3=(0,8,7), F4=(1,2,4,9), F5=(2,3,5,4),
    F6=(3,6,5), F7=(3,7,6), F8=(4,5,6,7,8,9).

The four lower vertices form the square B, and the upper six form a strictly convex hexagon T. Their intermediate horizontal section is exactly (1-s)B+sT at z=Hs. In the upper polygon, horizontal top and bottom edges and the right vertical edge have the same normals as their base edges, giving the three lateral quadrilaterals F1,F4,F5. The base's left normal exposes only upper vertex7, giving F2. The remaining three upper-edge normals expose base vertex3 twice and base vertex0 once, giving F6,F7,F3. Together with the two horizontal facets these exhaust the normal-fan merge. For t>0 all listed normal intervals are strict; in particular consecutive upper left-edge cross products are positive multiples of t. Thus these are genuine maximal facets, not a triangulation. Their cycles give exactly17true edges and V-E+F=2.

The source independently verifies all exact supporting equalities, strict inequalities off each facet, strict oriented polygon turns, and paired opposite edge uses for this continuous parameter interval. All ten vertices are on the reconstructed genuine boundary. No internal integration diagonal is counted. The root B=F0 has precisely the four neighbors F1,F2,F4,F5.

## 6. Actual homogeneous moments

Let d=51t+520. Genuine positive tetrahedra from the interior arithmetic mean of the ten raw vertices to a triangulation of each maximal facet give the exact polynomial identities

    Vol(P)=H d/30,
    J_x=-H t(107t+810)/200,
    J_y=H t/8,
    J_z=H^2(141t+1360)/120.

The arithmetic mean here is only the positive fan apex, NOT an assigned centroid. Dividing J by the actual volume gives

    g_x=-3t(107t+810)/(20d),
    g_y=15t/(4d),
    g_z=H gamma,
    gamma=(141t+1360)/(4d).

The exact polynomial ring in the source proves these identities symbolically, not by interpolation or parameter samples. The proof of each positive fan coefficient uses Bernstein coefficients on the full t interval. The sample hull also recomputes the actual volume and center directly.

Throughout the family the mechanical metric is M=N=I, and centered points are X=v-g(P). The actual root pole is q=(0,0,-1/(H gamma)). The foot (g_x,g_y,0) lies strictly inside the square because

    |g_x|<1/400, 0<g_y<1/10000.

So B is strictly stable for every family member.

## 7. Uniform positive witnesses in all four relative facet interiors

For a raw point w=(u_1,u_2,Hs), direct expansion gives the scaled identity

    (H gamma)^2 Delta(w-g)=4 H^2 gamma s-||u-g_xy||^2.

Write tau=H^2 gamma. Since141*520-51*1360=3960>0, gamma increases with t. Thus

    17/26<=gamma<131/200,
    tau>=(53/30)^2(17/26)=47753/23400,
    tau<(177/100)^2(131/200)=4104099/2000000<103/50.

Use these four raw witnesses:

    a1=(0,-2,H/2) in relint F1,
    a2=(-2-3t/5,0,H/2) in relint F2,
    a4=(2,0,H/2) in relint F4,
    a5=(0,2,H/2) in relint F5.

Each quadrilateral witness is the mean of its four vertices. The F2 witness is v0/4+v3/4+v7/2. All barycentric coefficients are positive, so each lies in the indicated true facet relative interior. After actual centering, their horizontal squared norms are bounded above by (201/100)^2+(1/400)^2. For F2, use2+3t/5+|g_x|<201/100; the other cases are easier. Hence for all four

    (H gamma)^2 Delta(a_i-g)
      > 2(47753/23400)-(201/100)^2-(1/400)^2
      =774011/18720000 >1/25.

The four witnesses therefore satisfy the strict root-star hypothesis uniformly. Every member of the family has S>=2.

## 8. Uniform absence on the entire true one-skeleton

For a point on any fixed true edge, let u be its raw horizontal coordinates and u0 those obtained at the same affine edge parameter by setting t=0. Only upper vertices6,7 move with t, both toward more negative x. Every edge incident with them lies entirely at negative x, so ||u||^2>=||u0||^2 pointwise. Across all edges |u_x|<151/50 and |u_y|<=3. The actual centering cost satisfies

    ||u-g_xy||^2 >= ||u0||^2-157/10000,

because2[(151/50)(1/400)+3(1/10000)]=157/10000; the omitted ||g_xy||^2 only improves the bound.

At t=0 the four base edges have s=0 and ||u0||^2>=1. All six upper edges have s=1 and ||u0||^2>=9. The seven remaining true edges are precisely:

    corner edges (0,8),(1,9),(2,4),(3,5): ||u0(s)||^2=2(1+2s)^2;
    spine edge (3,6): ||u0(s)||^2=2+4s+4s^2;
    diagonal edges (0,7),(3,7): ||u0(s)||^2=2+2s+5s^2.

These 'diagonal' edges are real edges of the family, not triangulation diagonals. The formulas hold for all0<=s<=1. With tau<103/50, the maxima of4tau*s-||u0(s)||^2 in the three respective classes are bounded above by

    -9991/5000, -2191/2500, -166/3125.

They follow by exactly maximizing the three concave quadratics. Base and upper edges give still smaller upper bounds -1 and4(103/50)-9. Including the centering error therefore gives, on EVERY point of EVERY true edge,

    (H gamma)^2 Delta(w-g)
      < -166/3125+157/10000
      =-1871/50000 <-3/100.

Thus even the closed cap Delta>=0 has no true one-skeleton point. Nevertheless it intersects the interior of all four neighboring facets with the strict positive margin established in section7. No finite or continuous search restricted to the true one-skeleton can certify this root star; genuine two-dimensional facet witnesses are essential for the cap method.

## 9. Full exact rational sample

At t=1/100,H=53/30 the actual values are

    Vol=2758703/90000,
    g=(-243321/104102000,15/208204,7215473/6246120),
    q=(0,0,-6246120/7215473).

Strict stable facets:0,1,2,4,5,8. Strict unstable vertices:4,5,7,8,9. Strict saddle edges:(0,1),(0,3),(1,2),(2,3),(4,5),(4,9),(6,7),(7,8),(8,9). Thus the sample has strict(S,U,H)=(6,5,9). All68 actual edge primitives are nonzero, so its physical weak census is exactly000. The identity6+5-9=2 is a check, not the reason weak points are absent.

The exact maximum over ALL vertices is

    -87265257098822681/130157626534322500.

The exact maximum over ALL17 complete edges occurs on(3,7) and is

    -13619210473647526679/147837249324783207549.

The four exact facet-interior maxima, in neighbor order1,2,4,5, are

    7625869/122526900,
    15713692834/310004084421,
    33884567/612634500,
    7679869/122526900.

Their full exact points, all actual planes, all edge maximizers, raw witnesses,68 primitives and140 continuous polynomial guards are reconstructed in the pinned JSON report. Nothing in that report is required as an unavailable external checkpoint: both literal source units above regenerate it.

## 10. Scientific boundary and next use

This establishes an actual, strictly separated continuous E17 countercontrol to the simplification 'root-cap testing on vertices or all true edges is enough'. The exact finite facet optimizer repairs that simplification. The family itself is not close in equilibrium count to110 and does not improveC622. The cap theorem proves at least two strictS for the stated two-parameter Euclidean family only. It neither excludes its full arbitrary-metric closure nor a whole graph-realization class.

A useful next direction is to combine the finite interior cap constraints with the one common polar metric and genuine-centroid shape parameters in sectors where existing vertex/edge cap certificates fail. The closed-form plane maximum exposes the relation to pole arrows, while the actual-facet membership inequalities retain geometric information that a graph-only orientation loses. Any global coverage claim still needs a complete continuum argument and literal incidence mapping; none is inferred here.
