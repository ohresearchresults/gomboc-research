# material-f40f0cdce3b7

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# ALL_FACET_FLIP_V1: complete triangulation-span compression and an actual-centroid exclusion

## Status and exact scope

This is a new finite-dimensional compression theorem for genuine facet retriangulations, a complete runnable implementation, and one frozen exact separating certificate. It excludes native TREE253/K2 incidence 10 with weak complementary-path root at position 1, and, by the literal maximal-facet/path permutation below, incidence 11 with root at position 8. These are two whole continuous incidence/root domains, not two particular shapes. They were both unresolved in the accepted214 endpoint. Subject to the previously accepted214 proof, coverage therefore becomes216/550,334 unresolved; W06 becomes66/200,134 unresolved. The whole-row set is unchanged. No global polyhedral type count is changed.

The universal lower bound remains V>=10,F>=9,C=2E>=34. This material does not give C>=36, a C34 attainer, an exact minimum, or an authenticated Figure650 upper bound. Other numerical outputs generated in this turn are not included in this first certificate theorem; their separate complete coefficients must be preserved before they change the accepted count.

The combinatorial domain is exactly the literal native55 input inherited from minimum-0078 (39043 bytes,SHA256 2a0d3544bfb7f0c3b6366bdda3555bc650eede67a1444d51a2d7207a0079eecd), read completely in this turn. Its theorem A supplies the weak complementary Hamilton path when the full pole-arrow graph is TREE253. Its theorem B excludes the two endpoints. No other positive primal arrows are declared absent. The path-only exclusion proved here needs neither those off-path signs nor the full pole graph once the path hypotheses hold.

## 1. An exact integer basis for every convex polygon triangulation

Label the vertices of a genuine convex m-gon in cyclic order by0,...,m-1. Formal oriented triangles use increasing cyclic-position labels. For i<j<k write [ijk], with boundary

partial[ijk]=[jk]-[ik]+[ij].

For 0<i<j<k<m put

q_ijk=[0ij]+[0jk]-[0ik]-[ijk].

Each q is a cycle. The q_ijk form an INTEGER basis for the group of triangle2-chains with zero boundary. In particular their number/rank is binomial(m-1,3).

Proof: q_ijk has coefficient-1 at the unique triangle[ijk] that avoids0, and no other such triangle. They are therefore independent. Given a cycle h, subtract -h_ijk times q_ijk for every triple avoiding0. The residual is supported only on triangles[0ij]. The edge[ij] with i,j>0 occurs in the boundary of just[0ij] among these triangles. The zero-boundary condition forces every remaining coefficient to vanish. This also gives the exact integer expansion

h=-sum_(0<i<j<k<m) h_ijk q_ijk.

If T0 is the triangulation fan from0 and T is any triangulation, the two oriented boundaries are the same polygon boundary, so T-T0 has this expansion. Conversely, q_ijk is precisely the difference of the two triangulations of the convex quadrilateral with cyclic vertices0,i,j,k. Triangulate the rest of the m-gon identically on both sides: the four quadrilateral sides partition the remaining regions into convex polygons, and these can be triangulated. Thus every basis vector is a difference of two genuine full polygon triangulations, not a formal relation without geometric meaning.

The implementation stores unordered triangle labels for integration. Its signs are the two positive tetrahedra on one quadrilateral diagonal minus the two on the other. The chain argument is performed in cyclic-position labels before forgetting triangle orientation; it is not an assumption that arbitrary native vertex labels are cyclic.

This proof holds for every finite m. The exact census additionally enumerates all triangulations and checks the expansion for m=3,...,7, with counts1,2,5,14,42 and ranks0,1,4,10,20. No literature connectivity theorem is needed for the proof.

## 2. Lift the local identities to one actual body

Let P be any full-dimensional convex3-polytope of constant volume density, with its own volume centroid translated to0. Let x_i be its true vertices, X the matrix of their row coordinates, M any positive-definite symmetric3x3 matrix, and G=X M X^T. G is nonzero positive semidefinite.

For any genuine maximal facet and any vertex a outside it, every triangle of a facet triangulation gives a tetrahedron t consisting of a and those three vertices. All these tetrahedra are nondegenerate: a is strictly off the facet plane; three distinct extreme vertices of a convex polygon cannot be collinear. Write d_t=6Vol(t)>0, using one and the SAME d_t whenever the unordered fourset appears again. Let chi_t be its vertex-indicator column and

J_t=chi_t chi_t^T+diag(chi_t).

For a uniform tetrahedron, barycentric integration gives

E_t x = X^T chi_t/4,
E_t xx^T = X^T J_t X/20.

For example these follow directly by integrating barycentric monomials on the standard3-simplex: E lambda_i=1/4, E lambda_i^2=1/10, E lambda_i lambda_j=1/20 for i!=j. Affine change of variables preserves these normalized identities.

Lift q_ijk from a facet to apex a, obtaining an integer signed vector h indexed by unordered tetrahedral foursets. The two pairs of tetrahedra triangulate the same genuine pyramid over that quadrilateral, with interiors disjoint on each side. Hence equality of actual volume, first moment, and second moment gives

sum_t h_t d_t=0,                                      (1)
X^T sum_t h_t d_t chi_t=0,                            (2)
sum_t h_t d_t X^T J_t X=0.                           (3)

These are identities of one physical body. They do not allow separately assigned occurrence-masses or independently centered sub-bodies.

For each vertex a, a complete fan over triangulated facets not containing a covers P, with interiors disjoint. Let f_a be its0/1 tetrahedron vector, using a fixed reference triangulation in each facet. Every f_a has total volume6Vol(P), first moment0, and the same second moment. Therefore h=f_a-f_0 satisfies(1)-(3), and the reference satisfies

X^T sum_t f_0(t)d_t chi_t=0.                          (4)

## 3. Compression of ALL independently chosen facet triangulations

Take the finite tetrahedral universe consisting of all facets, all exterior vertex apices and all facet triangles. Include the differences f_a-f_0 and, independently for EVERY apex/facet pair, the anchored quadrilateral basis of section1. Any complete apex fan with ANY independently chosen triangulations differs from its default f_a by a sum of these local identities; then subtract f_0. Conversely every local identity is a difference of two genuine complete fans at its apex, and every f_a-f_0 is already such a difference. Their rational linear span is therefore EXACTLY the span of all complete-fan differences.

The source selects independent ORIGINAL integer rows h_s by rational sparse Gaussian elimination. Consequently the selected rows themselves remain genuine signed moment identities; discarded rows are rational linear combinations and lose no zeroth, first, or second moment equality. This is equivalence of the finite moment-identity span, not a claim that arbitrary solutions of the resulting relaxation are geometrically realizable, or that every infeasible physical domain must admit this particular quadratic certificate.

The tetrahedron universe implemented by the default triangles and anchored quadruples is complete. For a facet with at least4 vertices, the negative[ijk] entries include every triangle avoiding its anchor, and the remaining entries include all anchor triangles. Triangular facets are covered by the default fan. Repeated unordered foursets are identified across all facets and all apices.

For all55 literal rows the census gives132 through147 cells and51 through73 independent zeroth-moment relation rows. The (raw-row-count,independent-rank) multiplicities are (59,59):25; (67,67):11; (51,51):6; (67,66):5; (73,73):4; (59,58):3; (73,71):1. These are coefficient-space ranks, not ranks of a body's covariance and not equilibrium exclusions by themselves.

A subtle monotonicity issue deserves explicit treatment. Enlarging the cell universe means an old certificate cannot simply be assigned zero matrices on newly appearing cells. Nevertheless a strict old certificate can be extended: express its old fan identities in the complete span, take an old fan as reference, and add epsilon times I times the sum of(new fan-reference fan) zeroth-moment identities, choosing added fans whose union includes every new cell. New cells acquire strictly positive multiples of epsilon I; negative reference contributions occur only on old cells and are absorbed by the old finite strict margin for a sufficiently small positive rational epsilon. Thus the complete identity system does not invalidate old strict proofs. This does not assert that a particular bounded numerical locator will find the extended coefficients.

## 4. The exact separating identity

Suppose the true Hamilton path is indexed0,...,n-1 with weak arrows toward root r. For i!=r let p(i)=i+1 when i<r and i-1 when i>r. Define

D_i=x_i^T M(x_p(i)-x_i)>=0,
L_i=2e_i e_i^T-e_i e_p(i)^T-e_p(i)e_i^T.

Then tr(G L_i)=-2D_i<=0. These mechanical arrows refer only to actual path edges, not facet diagonals used for integration.

Choose an arbitrary vector g_0 for the reference first moment. For each selected h_s choose vector g_s, symmetric matrix C_s and scalar k_s. For each tetrahedron t and each i!=r choose mu_ti>=0. Put

B_t=f_0(t)(g_0 chi_t^T+chi_t g_0^T)
    +sum_s h_st(g_s chi_t^T+chi_t g_s^T+C_s+k_s J_t)
    +sum_(i!=r) mu_ti L_i.                           (5)

If B_t-I is positive definite for every cell, the physical realization is impossible. Indeed, tr(G B_t)>0 for every t because G is nonzero PSD. Multiplication by the actual positive d_t and summation gives a strictly positive quantity. But (4) kills the reference term; (2) kills the other g terms; (1) kills C; (3), contracted with M, kills k; and all remaining arrow terms are nonpositive. This is a contradiction.

The proof covers every full-dimensional convex realization of the specified TRUE maximal facets, its own uniform-volume centroid, all common SPD metrics with no condition-number cutoff, and every mechanical weak-arrow equality. It does not require positive lower bounds on tetrahedral volumes, off-path sign assumptions, or a centroid condition for the polar body. Incidence-changing or dimension-losing limits are not silently added to this fixed-incidence theorem.

## 5. Frozen first certificate and literal transport

The exact input row10 is

0134 018 0237 078 1245 127 178 2356 346 456.

The true complementary path, in native vertex labels, is

P10=(3,1,6,5,2,0,4,7,8,9).

The frozen record uses root POSITION1 (native vertex1). It has137 distinct actual tetrahedral cells,59 raw relations,58 selected independent rows, and5071 integer coefficients. Their order is exactly the source: the10 g-coordinates for reference then each selected relation; for every selected relation the55 upper-triangular C entries followed by k; then for each lexicographic tetrahedral fourset the9 nonnegative mu entries in increasing i excluding r. Formula(5) is reconstructed from these integers, and I is subtracted. All137 symmetric10x10 matrices passed positive leading-minor tests:1370 positive minors, with minimum leading minor117. Fraction-free Bareiss and an independently implemented rational Schur/LDL calculation agree on every minor.

The maximal-facet/path permutation10->11 is, in native vertex order0..9,

pi=(0,7,4,9,2,6,8,5,1,3),
facet permutation=(4,3,2,1,0,7,8,5,6).

The literal target path is P11=(3,1,5,2,0,4,6,8,7,9), and pi(P10[j])=P11[9-j]. Thus root1 maps to target root8 (native vertex7). For every source maximal facet its pi-image is exactly the target facet specified by the displayed facet permutation. This is directly checked from the two literal rows. The permutation preserves the physical point set, own volume COM, and metric; transported triangulations need not match any target default convention. It does NOT identify the full pole-labelled arrow domains. The path-only theorem of section4 qualifies for this transport, as formalized more generally in [internal-source-reference].

## 6. Complete durable recovery and pins

Save the following exact immutable materials as the named files in one directory, without added fences or extra newline changes:

- [internal-source-reference] as flip_moments.py:13811 bytes,SHA256 7542ef43f2e0e5b4759f076086c8de3539da8ef5051c80dae2a71e778a21faa7.
- [internal-source-reference] as native55.txt:2630 bytes,SHA256 58126aee072933749b18eca00ac4d32842e56e6ac8d662d06713bacef28bf96e. This is the unchanged literal input also contained in the full transport and pZ sources, not a relabelled catalogue.
- [internal-source-reference] as case_flip_10_1.py:12639 bytes,SHA256 cbba8276f6279472511166ee8a4f1816083cbb333e810f75c0b1eb5ac8d283f3.

Run with assertions enabled:

python -S flip_moments.py census
python -S case_flip_10_1.py
python -S flip_moments.py check certificate_10_1.json

The capsule contains all5071 signed integers as lossless little-endian16-bit data compressed by LZMA preset9 and base64-wrapped100 columns. It reconstructs the literal JSON record and automatically runs the exact checker. No numerical library, network, sandbox residue or random input is required. Python's standard-library integers and Fraction implement all proof arithmetic.

Expected products:

flip_census.json:11760 bytes,SHA256 6dd8e17b2cd48eeb6f2e0f7f94afe8f9640d460e0b8d75e63302f4a35d3682bd.
certificate_10_1.json:22359 bytes,SHA256 913ee3472bc33be747f282b027d40e10bab156802a930c7ae4d96a56a1e59776.
certificate_10_1.verified.json:604 bytes,SHA256 fee14e9f0e1f93b00806090dc0f5ed247c4e97abf47c02ba30d2ff4887d45edb.
Decoded signed-coefficient bytes:10142 bytes,SHA256 7290b05efe43f73dcb0813e8370f7fd0cd97365578266a650582e33294ffb24d.
Compact coefficient-array JSON with LF:22154 bytes,SHA256 8920df508b1daa23024b2c80f64e49c74caee14c66a6439944d9ff6e1b2f826d.
System-description JSON:7343 bytes,SHA256 23f738fa96100eb3acb6175d8beb583d5e5ad0921b0d19dc4c4cb1e25001a245.
Streamed exact block SHA256:265664c6197f422130feae0905f9d3a0fca4d9bc28d98969c7be475c565d20e3.
Streamed leading-minor SHA256:88914234ea69d2e1897fa0d59f33d6a55eec980f642aa51153cd260303f35d6f.
Streamed rational-pivot SHA256:d95531c752f36b1a40b86e983ef1a694307ecdd15fd1a8500d2bb36a85934b3b.

Expected terminal markers:
ALL_FACET_TRIANGULATIONS_EXACT_SPAN_PASS 55 11760 6dd8e17b2cd48eeb6f2e0f7f94afe8f9640d460e0b8d75e63302f4a35d3682bd
ALL_FACET_FLIP_EXACT_CHECK_PASS 10 1 137 604 fee14e9f0e1f93b00806090dc0f5ed247c4e97abf47c02ba30d2ff4887d45edb
ALL_FACET_FLIP_EXACT_RECORD_RECOVERY_PASS 10 1 22359 913ee3472bc33be747f282b027d40e10bab156802a930c7ae4d96a56a1e59776

These exact checks were executed successfully in this turn. An earlier temporary self-contained wrapper recover_flip10.py (21815 bytes,SHA256 71066462345e873c013f19e3d2f7a8aecff628e9f794260832230e4743090871) additionally passed a clean-directory cold replay of the same source/input/certificate and emitted ALL_FACET_FLIP_NATIVE10_ROOT1_RECOVERY_PASS 137 1370. That redundant local wrapper is not a required dependency and is not being substituted for the three fully preserved materials above.

## 7. Numerical discovery is separated from proof

The preserved source also contains the complete locator. Command: python flip_moments.py locate 10 1. Observed discovery environment:Python3.13.5,NumPy2.3.5,SciPy1.17.0,one OpenBLAS/OMP thread,zero initial vector,no random input. Free coefficients are numerically bounded[-1,1], nonnegative mu by[0,1]. This is only a scaling/search convention, not a physical metric or mass bound.

The objective is the log-sum-exp smooth minimum of all block eigenvalues, optimized by L-BFGS-B. Ordered tau schedule:(0.1,0.03,0.01,0.003,0.001,0.0003,0.0001,0.00003). Each stage has maxiter2500,maxcor30,ftol1e-15,gtol1e-10,maxls40. Stop stages once the actual numerical minimum exceeds1e-5. Round with numpy.rint at powers12,14,16,18,20,24 in that order, guard magnitude<2^62, and accept ONLY a passing exact integer check. This record passed at12 after the first three stages, whose numerical minima were approximately-0.1196359293,-0.02216507654,+0.007227537272. These floating values are provenance, not premises of the theorem.

Frozen integer recovery is independent of floating replay. A failed locator, failed rounding, or library-dependent different proposal is UNKNOWN, never evidence of geometric feasibility or impossibility. No historical novelty or contest eligibility is inferred from the new method.
