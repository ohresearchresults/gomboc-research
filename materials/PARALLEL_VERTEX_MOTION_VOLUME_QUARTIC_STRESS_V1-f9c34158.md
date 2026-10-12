# material-f9c34158d85e

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# PARALLEL_VERTEX_MOTION_VOLUME_QUARTIC_STRESS_V1

## Evidence, scope and sources

This is a coordinator analytic theorem with an executed exact algebraic and physical control. It replaces one-parameter matrix Bernstein sufficient tests by a COMPLETE scalar quartic test for a fixed stress under parallel vertex motion. It also gives a multivariate quartic reduction on parallel-motion shape cells. It is NOT a complete free-r H5 all-root atlas, a new proper110 body, an all-E17 exclusion, or a change to 34<=C_min<=622.

The exact H5 geometry and moments are retained from the fully read immutable result minimum-0240, SHA256 e9e9cb5a41c6f3efb409de269963537ed1616b34e6847d48b16feac43b6c92b7, and the complete coordinator material [internal-source-reference], H5_RANKONE_TRIANGLE_QUADRATIC_90_270_REDUCTION_V1, SHA256 c62b1baaaae15c0b646a691490e35a5d32d2a6e9124761aa9cf7d6a9b72c2ff0. Their claims are not independently replayed here. The new source [internal-source-reference], edge_slide_quartic.py.txt, is self-contained for every new executed check below: 8754 bytes, SHA256 3e00ec4e7db539c3d94be2ebfffb6494578959bcc16b67f22025a3bb8409b976.

The broad rooted-shadow-tree exclusion mechanism also appears in Bozoki, Domokos, Papp and Regos, arXiv:2401.17906, Sections 2-4. The volume-divided parallel-motion quartic and its executed H5 control here are separate deductions, not attributed to that paper. No external published bound is substituted for the internally accepted bounds.

## 1. Actual homogeneous parallel-motion cells

Let P(u) be a full-dimensional convex d-polytope with vertices
 z_i(u)=a_i+ell_i(u)e,
where e is one fixed nonzero direction, u is a vector of real parameters and every ell_i is affine. Work in a parameter cell on which a fixed genuine vertex triangulation is valid, with fixed orientations of its d-simplices, and the actual uniform volume V(u) is strictly positive. Vertices and true facets may degenerate at a boundary only when the fixed oriented decomposition and its actual moments remain valid there. No claim is made that arbitrary prescribed motions preserve a face lattice.

For each simplex, subtract its first vertex from the others. Its determinant is affine in u: all varying columns are multiples of the SAME e, so every determinant term with two varying columns vanishes. Summing the actual oriented simplex volumes gives affine V. The uniform first moment is the sum of each simplex volume times its vertex-average centroid. Hence J has total degree at most two. Its entire homogeneous degree-two part is parallel to e, because the moving part of every simplex vertex sum is parallel to e. In particular the projection J_perp onto e-perp is affine.

The single-moving-vertex case is included. If z_a=a_0+t e and all other vertices are fixed, then V=V_0+V_1 t and J_[2]=V_1 e t²/(d+1). Several moving vertices with different parallel speeds need not satisfy this last coefficient formula, but J_[2] is still parallel to e, which is all the theorem needs.

For H5, independent variation of r alone, or of x alone, is a one-vertex parallel motion. With x,r,lambda fixed, arbitrary joint variation of p,q in their physical triangle is also a parallel motion: labels 2 and 3 move parallel to (-1,1,0). Joint free x and r variation is NOT one parallel-motion cell; nor is general lambda variation. The theorem must not be silently applied across those different directions.

## 2. Exact stress and the rank-two centroid correction

Choose constant nonnegative weights w_ij on true directed edges, with W=sum w_ij>0. Define
 F=sum w_ij(z_j-z_i),
 Q=sum w_ij sym[z_i(z_j-z_i)^T],
 G=-sum w_ij sym[(V z_i-J)(z_j-z_i)^T]
   =-V Q+sym(J F^T).
Here sym(a b^T)=(a b^T+b a^T)/2. F is a vector flux, not a facet label. The actual centroid is g=J/V, and for every physical M>=0,
 (1/W) sum w_ij (z_i-g)^T M(z_j-z_i)=-tr(MG)/(W V).

Thus G>0 excludes those simultaneous nonnegative arrows for every nonzero PSD M. More usefully, G-eta W V I>0 implies the strict uniform mean-arrow bound
 (1/W) sum w_ij (z_i-g)^T M(z_j-z_i)<-eta tr M.
This uses the actual uniformly filled centroid throughout and makes no inverse-metric or polar-centroid relaxation.

Put Q_eta=Q+eta W I. The shifted stress is
 G_eta=G-eta W V I=-V Q_eta+sym(J F^T).
Consequently the natural V-scaled quantitative margin preserves the structure exactly. A different unscaled constant shift G-epsilon I need not preserve the volume factor discussed next.

## 3. The three-dimensional volume factor and explicit quartic

In d=3, for every symmetric Q, scalar V and vectors J,F, one has the exact polynomial identity
 det[-V Q+sym(J F^T)]
 =V{-V² det Q+V F^T adj(Q)J+(J cross F)^T Q(J cross F)/4}.                 (3.1)

One proof expands the determinant by the number of columns selected from the rank-at-most-two update sym(J F^T). The terms with zero and one such columns are -V³ det Q and V² F^T adj(Q)J. The two-column term is V(J cross F)^T Q(J cross F)/4; the three-column term vanishes. Alternatively the generic symmetric 3x3 identity is expanded and checked exactly by the complete new source.

Define the explicit polynomial
 R_eta=-V² det Q_eta+V F^T adj(Q_eta)J
       +(J cross F)^T Q_eta(J cross F)/4.                              (3.2)
Then det G_eta=V R_eta without polynomial division or any assumption that V has nonzero slope.

### The quartic theorem
On every parallel-motion cell, R_eta has total degree at most FOUR in all motion parameters, including when V is constant.

Choose a fixed orthonormal frame with its last direction parallel to e. The blocks have the following degree pattern:
 Q_eta = [[Q_0, b(u)], [b(u)^T, c(u)]],
 where Q_0 is constant, b is affine and c is quadratic;
 J = (j(u), j_3(u)), where j is affine and j_3 is quadratic;
 F = (f_0, f_3(u)), where f_0 is constant and f_3 is affine;
 V is affine.

In this frame det Q_eta has degree at most two. The upper-left block of adj Q_eta has degree at most two, its off-diagonal block degree at most one, and its bottom entry degree zero. Therefore F^T adj(Q_eta)J has degree at most three. The horizontal part of C=J cross F has degree at most two, while C_3 has degree at most one: the potentially cubic cross product of the two highest terms vanishes because both are parallel to e. It follows that C^T Q_eta C has degree at most four. Every term of (3.2) thus has degree at most four. Fixed coordinate changes do not change total degree.

The new executable independently checks this degree bound with generic coefficients for V,J,F,Q of the displayed one-parameter pattern. Each of the three terms can genuinely have degree four. Its physical H5 control also has a nonzero quartic leading coefficient. One cannot replace the theorem by a universal cubic claim.

## 4. A complete interval certificate, not a one-sided Bernstein relaxation

Let u=t range over a closed interval [a,b] where V>0. Let A_eta(t) be the 2x2 compression of G_eta to e-perp. It is AFFINE:
 A_eta=-V Q_0+sym(j f_0^T).
Thus A_eta(t)>0 on the whole interval if and only if A_eta(a)>0 and A_eta(b)>0. No commutation of endpoint matrices is assumed; positive definiteness is preserved by their convex combinations.

By the scalar Schur complement, whenever A_eta>0,
 G_eta>0 iff det G_eta>0 iff R_eta>0,
because V>0. Conversely G_eta>0 necessarily has A_eta>0. Therefore the following criterion is necessary AND sufficient for this fixed stress and margin on the entire closed interval:

  1. A_eta(a) and A_eta(b) are positive definite;
  2. the scalar polynomial R_eta is strictly positive throughout [a,b].

For rational input and endpoints, each 2x2 endpoint test uses two exact positive leading minors. The quartic can be decided exactly by a rational Sturm chain: verify positive endpoint values and zero distinct roots in (a,b). Repeated interior roots must also be counted, since they violate strict positivity even without a sign change. A nonpositive endpoint or identically zero polynomial fails. A constant quartic is handled directly. No floating-point eigenvalue, algebraic-root approximation, matrix coefficient positivity, local folding loss or subdivision in t is required to accept or reject this particular stress.

This does not mean that one stress works over an entire desired family. Different trees or intervals may need different weights. Weight selection is still a substantive problem, and R_eta depends cubically on weights; it is not an additional linear locator constraint. After a fixed candidate stress is found, however, the test is exact. Failure is failure of that stress/margin on that interval, not feasibility of a full tree or failure of all stresses.

## 5. Multivariate and higher-dimensional consequences

For u in a compact parameter polytope, A_eta is affine and is positive definite everywhere exactly when it is positive definite at every parameter vertex. The remaining condition is positivity of the scalar total-degree-four R_eta. This is a quartic reduction, NOT an automatic exact bivariate positivity algorithm. On a physical (p,q) triangle, fifteen positive degree-four scalar Bernstein coefficients give a sufficient certificate, together with the three 2x2 vertex tests. Scalar Bernstein positivity may be conservative; local subdivision recovers strict positive cases by continuity. In particular this method does not inherit the rank-one cubic folding loss of the earlier 90/270-matrix scheme, but it sacrifices linear dependence of the sufficient conditions on stress weights. Neither scheme is asserted to dominate the other in overall runtime or number of cells.

The quartic degree is not special to dimension three. For d>=2 the determinant expansion of the same rank-two centroid update gives
 det G_eta=V^(d-2) R_eta,
where R_eta is polynomial. In an e-aligned block frame, G_eta has affine (d-1)x(d-1) upper block, off-diagonal degree at most two, and bottom degree at most three; hence its determinant has total degree at most d+2. If V is nonconstant affine, division by its guaranteed factor leaves degree at most four. The constant-V case follows as a polynomial identity by replacing V by V+epsilon ell(u), with nonconstant affine ell: for every nonzero epsilon all higher coefficients of the explicit rank-two cofactor expansion vanish, so they also vanish at epsilon=0. A_eta endpoint/parameter-vertex positivity and the same scalar quartic condition then decide the stress in arbitrary dimension. The explicit cross-product formula (3.2) and the executed checks here remain three-dimensional.

## 6. Exact physical free-r H5 control

Fix x=1/2,p=3/8,q=1/4,lambda=1/2 and vary r over [0,1]. The ten literal vertices are
 z0=(1/8,0,0),
 z1=(5/16,0,0),
 z2=(5/16,3/16,0),
 z3=(1/8,3/8,0),
 z4=(0,1/2-3r/8,0),
 z5=(0,1/8,0),
 z6=(1/32,1/32,0),
 z7=(0,0,1),
 z8=(1/2,0,1),
 z9=(0,1/2,1).
Their oriented true facets, edges and genuine tetrahedral fan are completely literal in the new executable. For 0<r<1 it checks all 34 true plane-incidence identities, all 56 strict nonincident supporting inequalities, basal convex turns and the stated edge/facet intersections. Every strict-support polynomial has nonnegative interval Bernstein coefficients with at least one positive coefficient, so it is strictly positive on the open interval. The genuine fan volumes have the same nonnegativity check. Summed fan volume and first moments equal the actual formulas identically; no fixed or vertex-average centroid is used.

The actual volume is V=181/1536-r/128>0. Boundary r=0 has collinear basal labels 2,3,4, and r=1 has coincident labels 4=5. They are actual positive-volume limits, not claimed genuine ten-vertex E17 bodies. The stress remains positive there as a labelled limiting statement.

Take unit weights on ONLY the true arrows 7->0, 8->2, 9->4, so W=3. The unshifted exact quartic is
 R_0=(-13824 r^4+363276 r^3-5435748 r²+17071173 r+2513908)/103079215104.
The compression to the XZ plane is affine. For the volume-scaled mean margin eta=1/500, all four compression endpoint leading minors are strictly positive, and the exact shifted quartic has positive values at both endpoints and zero interior roots by Sturm. Consequently
 [D_70(M)+D_82(M)+D_94(M)]/3 < -(1/500) tr M
for EVERY r in [0,1] and EVERY nonzero PSD M, where D_ij(M)=(z_i-J/V)^T M(z_j-z_i).

This rules out these three simultaneous nonnegative arrows on the entire released interval. It does not cover every rooted tree and is not an all-root free-r exclusion. A tree containing all three arrows inherits this stress, but a tree that omits one need not. This distinction remains essential even though the interval reaches far beyond the earlier r=1/3 slice.

The larger proposed margin eta=1/100 is rejected: its compression endpoint matrices still pass, but the shifted quartic has a negative left endpoint and one interior root. This is a control showing why the scalar Schur condition cannot be discarded. It is NOT a claim that the full endpoint 3x3 matrices passed while an interior matrix failed.

## 7. Complete reconstruction and observed execution

Save the EXACT text of [internal-source-reference] as edge_slide_quartic.py. It has 8754 UTF-8 bytes and SHA256 3e00ec4e7db539c3d94be2ebfffb6494578959bcc16b67f22025a3bb8409b976. Run with assertions enabled:
 python -B edge_slide_quartic.py report.json

Observed dependencies: CPython 3.13.5 and SymPy 1.14.0. There are no external input files, solvers, random seeds, omitted helpers, numerical tolerances or non-default search parameters. The script itself contains every coordinate, incidence, moment, margin and parameter needed for these checks. The first execution and a new directory initially containing only this source both passed and produced identical report.json: 3506 bytes, SHA256 54466085f4aa697567b2b504ddfce6c84d3009981f8b51f3dfa14845d5874c4b.

Expected markers:
 GENERIC_VOLUME_DIVIDED_QUARTIC_IDENTITY_PASS 4 4 4
 H5_FREE_R_THREE_ARROW_EXACT_STURM_PASS 1/500 0 34 56
 OVERSIZED_MARGIN_REJECTED_PASS 1/100 1
 REPORT_BYTES_SHA256 3506 54466085f4aa697567b2b504ddfce6c84d3009981f8b51f3dfa14845d5874c4b

This proof and the complete executable form the new recovery capsule. The output records exact endpoint minors, the full quartic coefficients and Sturm evaluations, true volume/first moments and the negative-margin control. No independently replayed 48,790-tree atlas or new complexity-bound proof is asserted.
