# material-3792130b3735

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Recovery capsule part 1 of 2: all homothetic frusta, sharp whole-facet bound

## Result and precise scope
For every compact full-dimensional convex planar base D and every 0<=s<1, let

    P_s={(r u,r): u in D, s<=r<=1}.

This is an actual uniformly filled homothetic frustum; s=0 is a pyramid. For every genuine whole flat facet F of P_s, with actual volume centroid g, covariance Sigma, uniform facet second moment T_F about THAT SAME g, and alpha_F=distance(g,aff F)*Area(F)/Volume(P_s),

    alpha_F T_F <= kappa(s) Sigma,
    kappa(s)=45(1+s)^2(1+s^2)^2/[32(1+s+s^2)(1+s+s^2+s^3+s^4)].

The inequality is in positive-semidefinite order and includes all mixed tests, all lateral facets, BOTH end facets when present, every asymmetric base, and every nonsingular affine image of this body. For every fixed s the constant is sharp: a rectangular base and a lateral facet attain it in a base-normal test direction. In particular EVERY facet of EVERY homogeneous pyramid satisfies the sharp full matrix bound45/32. As s increases from0 to1, the sharp frustum constant increases strictly from45/32 to3/2, always remaining below3/2 for a genuine nonzero-height frustum.

This is NOT the universal3D whole-facet inequality, an S2/U2 mechanical theorem, an incidence exclusion, or a new110 construction. A particular affine image's Euclidean equilibrium census need not agree with the native one's. No lower or upper minimum bound changes: the accepted lower prohibition34 and canonical attaining construction622 remain separate.

## Source dependency and evidence level
The coordinator read [internal-source-reference] completely, SHA240b58ed6bde2703c5788573c8c20ca2a4278a3abc1cfc66fb8f607645eb646d,13829B. Its accepted analytical theorem is: for every actual uniform planar convex D and whole edge e, alpha_D T_e <=(3/2) Sigma_D, about the actual area centroid. It also gives alpha_D<=2/3 and the affine-prism all-facet corollary. It is a uniform-density theorem, not a nonconstant-affine-density one. We use that exact scope, not a polygon-localization assumption.

The reduction and new scalar inequalities below are analytical identities. The complete new program in Recovery capsule part2 is source-only runnable and was actually executed normally and in a fresh directory containing only that source. It verifies all scalar certificates and four independent actual-polytope controls, including their full moment matrices and physical edge packets. These executions are coordinator executions of the new source, not an independent replay of the imported planar proof or proof-assistant formalization.

## 1. Normalization and actual moments
An affine shear places the apex of the extended cone over the actual area centroid of D. Translate that centroid to0. No symmetry of D or of a marked edge is assumed. Define

    A_k=int_s^1 r^k dr=(1-s^(k+1))/(k+1),
    mu=A_3/A_2,
    v=A_4/A_2-mu^2>0.

The actual volume measure in coordinates(u,r) is r^2 du dr. Thus

    Volume(P_s)=Area(D) A_2,
    g=(0,0,mu),
    Sigma=diag((A_4/A_2) Sigma_D, v).

The vanishing cross block is due to the actual mean of u being0. This is a legitimate affine normalization, not an independently prescribed mass centre.

## 2. Every whole lateral facet: the mixed terms cancel exactly
Let e be a genuine whole edge of D, lying in q.u=1 with outward q. Its lateral facet has parametrization(r u,r),u in e. Surface measure is a constant times r dr ds_e. Multiplying by the actual distance from g to the side plane gives mu r dr ds_e/|q|. Therefore

    alpha_F=alpha_D A_1 A_3/A_2^2,
    T_F=diag((A_3/A_1)T_e, mu^2-A_3/A_1).

Here the potentially nonzero mixed block is

    [A_3/A_1-mu A_2/A_1] c_e=0,

where c_e is the generally nonzero edge centroid about the actual base centroid. This cancellation, rather than symmetry, is essential. The second-moment matrices all use the same actual g.

Consequently the planar generalized-eigenvalue block is multiplied by

    K(s)=A_3^2/(A_2 A_4),

and the radial generalized ratio is alpha_D Q(s), where

    Q(s)=A_3^2(A_1 A_3-A_2^2)/[A_2^2(A_2 A_4-A_3^2)].

The imported whole-edge theorem gives the full planar block <=(3/2)K(s)=kappa(s), without discarding mixed base moments. To handle the radial block, put

    U=1+s+s^2,
    W=1+s+s^2+s^3+s^4,
    P=1+4s+10s^2+4s^3+s^4.

Direct simplification yields

    Q=15(1+s)^2(1+s^2)^2(s^2+4s+1)/(8U^2 P),
    15/8-Q=15s^2(9s^4+20s^3+26s^2+20s+9)/(8U^2 P)>=0.

Thus alpha_D Q<=(2/3)(15/8)=5/4<45/32<=kappa(s). This closes every lateral matrix block, not only the test that attains equality.

## 3. Both caps lie below the same sharp constant
For the cap r=1 the tangential and radial generalized ratios are respectively

    Tplus=(1-mu)/A_4,
    Nplus=(1-mu)^3/(A_2 v).

For the cap r=s>0 they are

    Tminus=(mu-s)s^4/A_4,
    Nminus=(mu-s)^3s^2/(A_2 v).

The cross blocks vanish because the actual base centroid is0. In the polynomials above,

    Nplus=5(3s^2+2s+1)^3/(4U^2 P),
    Nminus=5s^2(s^2+2s+3)^3/(4U^2 P).

The exact positive gap certificates are

    kappa-Nplus=5(1-s)^2 Pplus/(32U^2 W P),
    kappa-Nminus=5(1-s)^2 Pminus/(32U^2 W P),

where Pplus has ascending power coefficients

    [1,9,45,108,162,206,234,252,189,81,9],

and Pminus has ascending coefficients

    [9,81,189,252,234,206,162,108,45,9,1].

The tangential gaps are

    kappa-Tplus=5(9s^6+18s^5+27s^4+36s^3+3s^2+2s+1)/(32UW),
    kappa-Tminus=5(s^6+2s^5+3s^4+36s^3+27s^2+18s+9)/(32UW).

All are strictly positive on0<=s<1; the bottom cap is omitted, rather than counted as a zero-area facet, at s=0. The complete source independently forms these rational differences and records their exact positive numerator/denominator coefficient certificates.

## 4. Sharpness, monotonicity and the prism limit
The precise identities are

    kappa-45/32=45s^3/(32UW),
    3/2-kappa=3(1-s)^2 P/(32UW),
    kappa'=45s^2(1-s)(1+s)(1+s^2)(3s^2+4s+3)/(32U^2 W^2).

A rectangular base attains the planar3/2 theorem in an edge-normal direction; that direction transports to the lateral block and attains kappa(s). Thus this is a sharp all-base constant for each fixed s, not just an upper estimate. At s=0 all homogeneous pyramids have the sharp universal-within-this-class45/32 bound. At s approaching1, the unscaled body's volume tends to0; an affine rescaling produces the familiar prism limit. We do not count the s=1 unscaled set as a full-dimensional frustum. Actual prisms were already covered separately by the accepted uniform-planar theorem.

## 5. New nodal marked-vertex trimming obstruction
There is a useful general variational reason why the sharp pyramid example does not produce a maximum over all convex bodies.

Let P be any uniformly filled full-dimensional convex polytope in R^3, F a genuine whole facet, t an inward affine coordinate with F={t=0}, and Y a nonzero affine test centred at the actual volume mean. Assume B2=int_F Y^2 d_sigma>0. Use

    V=int_P1, J=int_Pt, I=int_PY^2, R=J B2/(V I).

If a genuine vertex p of F satisfies Y(p)=0, choose a linear functional uniquely exposing p and trim a sufficiently small cap. Locally the polyhedral cap is p+sC for a fixed positive-volume cone section C. Its removed mass delta V=c s^3. Since t(p)=Y(p)=0, the removed J and first Y moment are O(s delta V), and the removed raw Y-square moment is O(s^2 delta V). The removed part of the old whole facet has area O(s^2) and Y^2=O(s^2), so its raw B2 loss is O(s^4)=O(s delta V). After actual recentering, the test mean changes only O(s delta V), and its additional facet-inertia correction has that order. All denominators remain positive. Therefore

    R_s/R=1+delta V/V+O(s delta V)>1

for all sufficiently small positive s. The remaining part of F is again its genuine WHOLE facet, not an arbitrarily selected subface. The additional cut facet changes incidence. Hence this is an obstruction to a local maximum in the unrestricted convex-body class, NOT an incidence-preserving mechanical deformation or an E17 exclusion.

The planar affine-height analogue includes density-zero endpoints. Let K have a genuine straight-sided corner p at an endpoint of its whole marked edge, with affine ell>=0 and nonzero positive interior mass, and Y(p)=0. A similar corner cap p+sC removes weighted mass c s^2 if ell(p)>0, or c s^3 if ell(p)=0. In the second case ell(p+s x)=s ell_linear(x) exactly. The same moment orders show raw whole-edge B2 loss is O(s delta V), and all actual mean corrections obey the preceding estimate. Therefore the same strict ascent holds. The statement requires a genuine exposed corner with straight adjacent segments; it is not asserted for a smooth endpoint, an interior nodal point of the marked edge, or a degenerate wedge. At a supercritical finite-conic candidate, the arcs stay above t>m/2 and the marked endpoints have genuine straight stems, so this rules out endpoint zeros of the distinguished actual-centred test in that setting.

## 6. Exact nodal trimming family and honest scope
An affine image of a square frustum gives an exact continuous control. In coordinates(r,x,z) use

    (r,x,z) -> (t=(r+x)/2, y=1+2x, z).

The planar support at s=0 is the triangle with vertices

    (0,-1), (0,1), (1,3),

and the actual filled lift is2|z|<=ell, ell=1-y+4t. Trim its marked nodal apex(0,1) by ell>=2s. The original marked facet remains t=0, now -1<=y<=1-2s. Throughout0<=s<1 the ACTUAL centred test is Y=y-1 and

    V=4(1-s^3)/3,
    mean t=3(1+s)(1+s^2)/(8U),
    I=16(1-s^5)/15,
    B2=4(1-s^4),
    R=kappa(s).

The exact gain is45s^3/(32UW)>0, and the leading logarithmic gain is s^3=delta V/V_0. At s=0 this is a sharp triangular-lift/pyramid control45/32; every nonzero trim improves it in the enlarged support class but remains strictly below3/2. No contradiction to the sharp triangular-lift theorem follows, because the trim changes the support and the polytope incidence. The program does not transfer the native square-frustum Euclidean census through the nonorthogonal affine map.

## 7. Complete recovery and actual execution
Recovery capsule part2 contains the COMPLETE frustum_all_facets.py,11727B, SHA

    e5c94f2463f8c4c0b4e752edf56f64123bc8a01f1000a6f98a18016a4a85a92b.

Use CPython3.13.5, SymPy1.14.0, assertions enabled. No input files, optimization, seed, tolerance or hidden coefficients are needed. Reconstruction and verification are the same command:

    python -B frustum_all_facets.py > frustum_all_facets.log

Output frustum_all_facets_report.json is68684B, SHA

    784340feb962f4c06b48776c225a37c8da15c2bde586fbb82372bd702ddb1d12.

Output frustum_all_facets.log is367B, SHA

    e71fba3aad07059cea2ed2989a25cf727589ef9130ce3eb017584191644f4df6.

The last marker is

    FRUSTUM_ALL_FACETS_SHARP_KAPPA_AND_NODAL_TRIM_PASS.

Normal and fresh source-only executions produced BYTE-IDENTICAL reports and logs. Full exact vertices, maximal oriented facet cycles, true edges, actual volume centroid/covariance, every whole-facet matrix, and all physical edge-packet primitives are generated for the square and an asymmetric pentagonal base at s=0 and1/2. The raw pentagon is(0,0),(3,0),(4,1),(2,3),(-1,2), translated by its actual area centroid; no free vertex masses are used.

The four native Euclidean controls have:

    square,s0: actual5/8/5, own558, physicalweak000;
    square,s1/2: actual8/12/6, own244, physicalweak000;
    asymmetric pentagon,s0: actual6/10/6, own558, physicalweak000;
    asymmetric pentagon,s1/2: actual10/15/7, own244, physicalweak000.

These are NONATTAINERS for110. They verify genuine hull incidence and the full centred matrix calculation, not a global equilibrium statement about all frusta. All arbitrary-base generality follows from the analytical reduction and the imported planar theorem, not four samples. No finite f-vector is assigned to an arbitrary curved base.
