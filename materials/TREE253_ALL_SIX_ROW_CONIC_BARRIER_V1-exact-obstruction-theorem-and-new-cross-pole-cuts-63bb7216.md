# material-63bb7216eef9

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# TREE253_ALL_SIX_ROW_CONIC_BARRIER_V1

## 0. Mathematical status

This is an exact negative result about a specified certificate family, together with a new necessary local geometric inequality. It is NOT a homogeneous polyhedron, a feasible physical Gram matrix, a C=34 construction, or a proof excluding a whole polyhedral incidence domain.

For the full TREE253 row-zero relaxation, a certificate with one common centering multiplier is impossible: even allowing the complete two-by-two raw-norm cones for all six labelled quadrivalent windows and the additional cross-pole inequalities below, its only positive-semidefinite certificate family is the zero family. This is proved using two explicitly reconstructible positive-definite abstract Grams with cancelling, individually nonzero centering residuals. A second exact pair places the rows strictly inside the known row constraints, below even a rational value smaller than the accepted sharp entry cap. Thus the obstruction is not caused merely by zero row weights or by the loose cap 10/9.

The all-six interior pair is a NEW object, not an alias of the earlier interior pair constructed using only the 3456 cone. Both are preserved, as is the initial boundary pair. Their exact identities and input checkpoints are different.

Accepted global conclusions do not change: the internal universal bounds remain V>=10, F>=9, C>=34. K2 remains 278/550 excluded root positions, not 550/550. K3 remains 11743 open labelled root positions or 8739 rooted primal facet/tree classes. No new whole incidence/root domain has been removed. The exact minimum, existence at C=34, exclusion of all E=17 bodies, and the alleged Figure C=650 certificate remain unresolved.

## 1. Exact authorities and physical setup

The actual-body row and Gram restrictions are from the completely read immutable result minimum-0069, SHA256 d0f91982420a008eef0bc169a4c7b9f999710361057096a930facbf9715942ff. The forced complementary primal tree and the nonzero-tangential-pole restriction under the FULL graph are from minimum-0078, SHA256 2a0d3544bfb7f0c3b6366bdda3555bc650eede67a1444d51a2d7207a0079eecd. Both were read from cursor 0 through eof:true before use in this continuation.

The geometric angular parent is [internal-source-reference], SHA256 844ae3e67f523827df904cb541c79b63f82185d61a54608339397abdd8f84b65. The reviewed raw-norm projection theorem is [internal-source-reference], SHA256 f553f4ec1f8da175be5b2aab0c706b06a75309c1403b14dfe275c9e7fc0f2a0d, with its complete recovery input [internal-source-reference]. These sources establish the geometric scope of the local cone; they are not replaced by the abstract Grams constructed here.

Retain the literal pole labels

p=(0,0,1,2,3,4,5,0,7),
Z=(6,5,4,3,2,1,0,7,8).

This is the FULL graph of nonnegative distinct pole shadows, not an arbitrary spanning tree selected from a larger graph. At the own volume centroid of a genuine homogeneous body P={x:q_i^T x<=1}, with one positive-definite M and N=M^{-1}, set

G=Q N Q^T, n_i=G_ii, Y_i(x)=1-q_i^T x,
d_i=A_i/(Vol(P)||q_i||), Lambda[:,i]=d_i E_Fi Y.

Then Lambda Q=-Q. The actual row vector

w=e_0+Lambda[0,:]^T

satisfies G w=0, w_0=1, sum_{j=1}^8 w_j=3, and the inherited strict row inequalities

0<w_j<10/9,
w_1<1/32,
2w_1+w_7<1/10,
w_1+w_2+w_7+w_8<1,
w_5+w_6>51/25.

Actual G also has rank 3. That rank, the other actual Lambda rows, the true incidence equations, and the common volume/area moment data are deliberately NOT present in the certificate family studied below. They cannot be silently supplied to its abstract counterexample.

## 2. Exact row polytope and its 48 vertices

Let R be the closed relaxation obtained by replacing the strict row inequalities by non-strict ones. Write u=10/9 and l=209/225. The heavy pair (w_5,w_6) ranges over the triangle with vertices

(l,u), (u,l), (u,u).

The small pair (w_1,w_7) ranges over the trapezoid with vertices

(0,0), (0,1/10), (1/32,0), (1/32,3/80).

The remaining four coordinates w_2,w_3,w_4,w_8 are nonnegative and have sum

R(h,s)=3-w_5-w_6-w_1-w_7.

Here 61/90<=R(h,s)<=24/25, so the fibre never collapses. Each of the four remaining coordinate upper bounds is automatic. Also

w_1+w_2+w_7+w_8 <= 3-w_5-w_6 <=24/25<1,

so the older sum cut is redundant on this row polytope.

Every vertex has a heavy-pair vertex, a small-pair vertex, and all remaining mass in exactly one of the four remaining coordinates. To prove completeness, two positive remaining coordinates would permit an immediate fibre perturbation. With only one positive remaining coordinate, a nonextreme heavy/small base point could still be perturbed, with the remaining coordinate changed by the affine amount needed to preserve the sum; its positivity is protected by R>0. Conversely an extreme base point and one-coordinate fibre support are plainly extreme. Thus there are exactly 3*4*4=48 vertices.

The exact auditor generates these vertices and sorts the nine-coordinate rational tuples lexicographically. This is a local row-polytope enumeration, NOT a census of polyhedral combinatorial types. Its row_vertices.json is a new 5043-byte serialization of the same 48 rational tuples as the earlier 2594-byte exploratory file; equality was checked after JSON parsing, not asserted as byte identity.

## 3. The 84 homogeneous scalar Gram restrictions

Let e_i be the standard coordinate vectors in R^9. For each ordered distinct pair (i,j), define

T_ij=2 e_i e_i^T-e_i e_j^T-e_j e_i^T.

Use A_ij=T_ij if i!=0 and j=p_i, and A_ij=-T_ij otherwise. These 72 inequalities tr(A_ij G)<=0 encode the eight permitted nonnegative arrows and the closed relaxations of all other strictly negative shadows. Some are redundant; none is omitted from the exact audit.

Add the two diagonal forms

A_half=diag(1,-2,0,0,0,0,0,0,0),
A_threequarters=diag(-3,0,0,0,0,0,0,4,0),

and the ten scatter forms

19J-75I,
20 e_a e_a^T+3J-15I, a=0,...,8.

Call the resulting 84 matrices A_1,...,A_84. They have integer entries, are generated literally by the audit source, and all satisfy tr(A_i G)<=0 for the intended actual-body sector.

## 4. A new necessary cross-pole cut at a quadrivalent unstable corner

This geometric lemma retains information not contained in the four raw squared norms alone.

Let the four actual incident poles be A,B,C,D in cyclic order. In physical coordinates at a true vertex x, put sigma=1/(x^T M x) and write the poles as a common perpendicular component plus tangential vectors y_A,y_B,y_C,y_D. Assume all tangential vectors are nonzero and the three consecutive selected edges are weak arrows forming a rooted path. Assume the corner is strictly unstable, or is on the permitted weak wall where the origin lies on the unselected closing edge.

Let beta_1,beta_2,beta_3 be the three selected central angles. Convexity and the weak-arrow inequalities give

0<beta_i<pi/2, beta_1+beta_2+beta_3>=pi.

Consequently

pi/2<beta_1+beta_2<pi,
pi/2<beta_2+beta_3<pi,
pi<=beta_1+beta_2+beta_3<3pi/2.

All three relevant cosines are strictly negative. Therefore

y_A dot y_C<0, y_B dot y_D<0, y_A dot y_D<0,

and hence

G_AC<sigma, G_BD<sigma, G_AD<sigma.

Since sigma<min(n_A,n_B,n_C,n_D), this implies the homogeneous linear necessary restrictions

G_AC<n_t, G_BD<n_t, G_AD<n_t

for every t in {A,B,C,D}. The strict inequalities survive a zero-derivative selected arrow and the allowed weak instability wall. The nonzero-tangential-pole hypothesis is essential; under FULL TREE253 it follows from the outdegree condition, as proved in the cited parent.

For a directed chain, the least raw norm is n_A. Two of the projected cuts are already weaker than full-graph restrictions, but the cross cut G_BD<n_A is additional. On the literal 3456 block, cyclically (6,5,4,3), it reads G_35<n_6. The other chains give G_24<n_5, G_13<n_4, and G_02<n_3. For an inward block the minimum can be either terminal tail, so the all-four-norm formulation avoids a false ordering assumption.

Only the ACTUAL incident block and ACTUAL candidate unstable corner may impose these geometric restrictions on a body. No body is required to satisfy all six different labelled corner conditions simultaneously.

## 5. The six exact projected raw-norm cones

The four directed-chain matrices are

3456: [[n4-n5,n5-n6],[n5-n6,n3-n4-n5+n6]],
2345: [[n3-n4,n4-n5],[n4-n5,n2-n3-n4+n5]],
1234: [[n2-n3,n3-n4],[n3-n4,n1-n2-n3+n4]],
0123: [[n1-n2,n2-n3],[n2-n3,n0-n1-n2+n3]].

For inward cyclic labels A,B,C,D, let a=n_A,b=n_B,c=n_C,d=n_D, p=d-a, q=c-d, h=b-c. The lifted matrix is

L(G,z)=[[q,z],[z,h+p-2z]], z>=0, z>=p.

Block 0127 has cyclic labels (7,0,1,2); block 0178 has cyclic labels (1,0,7,8). These cones are the exact projection conditions established in [internal-source-reference]. Their strict positive definiteness is necessary at the actual corner; non-strict positivity is a safe relaxation for an impossibility certificate.

For the exact abstract controls below, each inward block uses the explicit canonical lift z=max(0,p). The audit checks its two-by-two determinant and first diagonal entry exactly. The numeric locator's lift values are not needed for reconstruction or acceptance.

## 6. The specified common-centering-multiplier certificate family

For a chain cone L_b(G), write L_b^* for its trace adjoint. Then -L_b^*(W) has nonpositive pairing with every G satisfying L_b(G)>=0 whenever W>=0.

For an inward cone, the valid eliminated dual forms require care. Let W=[[W11,W12],[W12,W22]]>=0 and alpha,beta>=0 with

alpha+beta=2(W22-W12).

The expression

-tr(W L(G,z))-alpha z-beta(z-p(G))

is independent of z and equals

-W11 q(G)-W22(h(G)+p(G))+beta p(G).

This is the admissible homogeneous scalar form in G. Equivalently 0<=beta<=2(W22-W12). Omitting this restriction or assigning an independent second metric would create a different, invalid certificate family.

Let C_s(G)<=0 denote any of the cross-pole cuts in Section 4, represented by their symmetric matrices. Allow arbitrary nonnegative coefficients for them. For each row w, a candidate certificate matrix has the form

B(w)=gamma w^T+w gamma^T
     +sum_i mu_i(w) A_i
     +sum_s kappa_s(w) C_s
     +sum_b D_b(w),

where gamma is ONE vector shared by all rows, mu_i(w),kappa_s(w)>=0, and D_b(w) is a valid nonpositive cone-dual form just described. All other coefficients and cone duals may depend freely on the row. They are not required to be common, bounded, rational, or continuous.

For an actual G with G w=0, pairing gives tr(B(w)G)<=0. Thus B(w)>0 on the entire row domain would prove impossibility. One standard finite scheme finds B(v)>0 at every row-polytope vertex and interpolates its row-dependent multipliers; the common gamma makes the centering term interpolate correctly.

The theorem below refutes this entire family, not merely the earlier smaller ansatz with common scalar multipliers or a finite list of tangent cuts. The complete two-by-two cones contain every finite conic combination of their supporting linear cuts. It also refutes each of the six separate corner-specific certificate searches. For that purpose we test a STRONGER ABSTRACT cone imposing all six local cones and cross-cut sets simultaneously. This is not an assertion about simultaneous physical incidences: each legitimate one-block certificate is a special case of this larger algebraic multiplier family, with other block multipliers set to zero.

## 7. Exact obstruction theorem

THEOREM. On the row domain R of Section 2, the common-centering-multiplier family of Section 6 has no nonzero positive-semidefinite certificate. More generally, the conclusion already follows for any row domain containing both of the two strict interior rows displayed below. It remains true with all six local raw-norm cones and all 72 labelled cross-pole comparisons available to the certificate.

Take

e=1/10000, h=1109/1000, r=1563/2000,

w^A=(1,e,e,e,e,h,h,e,r),
w^B=(1,e,e,e,r,h,h,e,e).

The complete capsule constructs two DIFFERENT rational symmetric matrices G_A,G_B with the following exact properties:

1. G_A>0 and G_B>0, each of rank 9.
2. tr(A_i G_k)<0 for all 84 scalar forms and k=A,B.
3. Every one of the six local matrices is strictly positive definite for each G_k, with the explicit inward lifts z=max(0,p).
4. All 72 labelled cross comparisons of Section 4 are strict for each G_k; repeated algebraic comparisons are intentionally retained.
5. G_A w^A+G_B w^B=0 exactly, but neither summand is zero.
6. tr(G_A)+tr(G_B)=1.

The exact construction is the object TREE253_ALL_SIX_CORNER_INTERIOR_ROW_CONIC_DUAL_BARRIER_V1. Its common denominator is

1733367017333670000000000000.

All 90 independent matrix entries are uniquely reconstructed by exact rational elimination from the complete 80-integer checkpoint embedded in the source. The generator imposes the nine mixed-centering equations and the trace normalization, with a specified diagonal-first upper-triangle order and exact RREF rule. No numerical optimizer, external checkpoint, missing coordinate, or choice of rounding is part of this reconstruction.

Proof of the obstruction. Pair B(w^A) with G_A and B(w^B) with G_B, and add. The common gamma term is exactly

2 gamma^T(G_A w^A+G_B w^B)=0.

Every scalar-constraint contribution is nonpositive, and is strictly negative if its nonnegative multiplier is nonzero, by property 2 or 4. For a chain block, -tr(W L_b(G_k)) is strictly negative whenever W is nonzero and positive semidefinite, by property 3. For an inward block, use its displayed canonical lift: the complete expression is -tr(W L)-alpha z-beta(z-p), which is nonpositive and again strictly negative for nonzero W. Thus the summed pairing is <=0.

If B(w^A) and B(w^B) are positive semidefinite, their pairings with the positive-definite G_A,G_B are >=0. Equality of the sum forces both B matrices to be zero, every scalar and cross multiplier at the two rows to be zero, and every W there to be zero. For an inward block, W=0 and alpha+beta=0 force alpha=beta=0. We are left with gamma(w^A)^T+w^A gamma^T=0. Since w^A is nonzero, this implies gamma=0: multiplication by w^A first shows gamma is parallel to w^A, and substitution makes its coefficient zero.

At any other row, gamma is now zero. Pairing its B with, for example, G_A again shows that a positive-semidefinite B can only have zero scalar/cross/cone multipliers and B=0. Therefore the whole common-gamma semidefinite certificate family is trivial. In particular there is no positive-definite family, no family B>=I, and no rescue by adding more rational tangent cuts from the same local cones.

This proof uses no assertion that G_A or G_B comes from one actual body. Their different centering residuals are exactly why they provide a dual obstruction rather than a physical witness.

## 8. Strict interior and robustness of the obstruction

Both rows have sum of nonroot coordinates 3. All eight entries are positive. Their largest entry is h=1109/1000, and

1109/1000 < 196425/176993 < 10/9.

The intermediate rational is exactly

3(1+2t+3t^2)/[(1+t+t^2)(3+2t+t^2)] at t=7/15.

It is no larger than the accepted sharp cap c3, which is the maximum of this function. Thus both rows remain allowed after the loose 10/9 cap is replaced by c3. They also satisfy all the other inherited row inequalities strictly, including w5+w6=1109/500>51/25.

The audit gives a positive convex combination of ALL 48 row vertices for each interior row, not merely a numerical membership test. For completeness, with u,l as above, heavy coefficients are

alpha_0=(u-w5)/(u-l), alpha_1=(u-w6)/(u-l), alpha_2=1-alpha_0-alpha_1.

Let a=32w1 and b=w7/(1/10-2w1). The four trapezoid coefficients are

(1-a)(1-b), (1-a)b, a(1-b), ab.

The four fibre coefficients are w_k/R(h,s), k in (2,3,4,8). Tensoring these three coefficient lists gives all 48 positive coefficients; their sum is 1, and their weighted vertices reconstruct w exactly. The full fractions are in the report.

Consequently a certificate verified at all 48 closed row vertices would interpolate to the forbidden interior pair. This also explains why deleting zero-weight boundary points does not repair the full-domain common-gamma method.

The obstruction is stable under sufficiently small perturbations, rather than an isolated rational coincidence. For positive w^A, the nine mixed-centering equations can first solve the nine G_A diagonal entries. The trace equation then solves one off-diagonal entry, with nonzero coefficient proportional to -(w^A_1/w^A_0+w^A_0/w^A_1). The remaining 80 entries form free coordinates. Near the displayed positive rows this reconstruction depends continuously on both rows and on the free entries; all strict scalar, matrix, cross, and row inequalities therefore persist in a relative neighbourhood. This is a local continuity statement, not a globally certified radius.

## 9. Preserved predecessors and exact-data distinction

The initial boundary pair has

w^A=(1,0,0,0,0,10/9,10/9,0,7/9),
w^B=(1,0,0,0,7/9,10/9,10/9,0,0),

the lexicographic row-vertex indices 4 and 7. It has common denominator 63000000000000000. It too passes all six local cones and all cross comparisons. It is retained because it gives a particularly transparent obstruction to the 48-vertex certificate system, despite lying outside the sharper actual entry cap.

The first strict-interior pair, object TREE253_QUADRIVALENT_INTERIOR_ROW_CONIC_DUAL_BARRIER_V1, has the same rows as Section 7 but DIFFERENT Grams, with denominator 577789005777890000000000000. It was built for the 3456 cone. It does not pass every other local cone and is not used to claim the all-six result.

The all-six pair in Section 7 is a separate exact reconstruction. The new complete source reproduces all three predecessor/current data files byte-for-byte. Neither predecessor is discarded or silently renamed after strengthening the conclusion.

## 10. Complete durable recovery and independent exact checks

The first, narrower complete capsule is preserved as [internal-source-reference], 8105 bytes, SHA256 c39f08cf94853b3cf6ce5bf2541243d463f0228563d16bc8f59b49d43c77b4fb. It reconstructs the boundary and first interior pairs. Its 12587-byte source has SHA256 7ccdb86d39c323fbc077c46ede70aa5b30a77ed0311ac332b6cadcb47727dd42; its 30981-byte report has SHA256 bcab014f612748459cbcebe9dcbbf94867fdb15241554f1ef19313c2b85181a7.

The authoritative all-six self-contained capsule is

[internal-source-reference],
TREE253_ALL_SIX_ROW_CONIC_BARRIER_V1 complete exact recovery.py.txt,
9543 bytes, SHA256 013c41edf597461a4a7e679439cb6a50d76c0e199b3661b5af3899a3529be92b.

Save that exact material as recover_all_six_row_conic_barrier.py and run, with assertions enabled:

python -S recover_all_six_row_conic_barrier.py build
python -S recover_all_six_row_conic_barrier.py check

No other attachment or sandbox file is required. The capsule contains its entire deterministic source compressed losslessly, checks the 6520-byte compressed payload SHA256 273f3d8feee6921af09f387cd26815ac6a72bf6366ce122edbb30d02d4f1d289, and reconstructs

row_conic_barrier_all_six_audit.py,
15355 bytes, SHA256 579a639ecd07234077b5848e733ec2e0f4b96495d1f5adce23e4b4bdc3a3907a.

The stored capsule has one harmless trailing space within its encoded DATA line compared with the original local 9542-byte drafting copy. Its ACTUAL durable pin is the 9543-byte value above. The stored bytes were matched locally and cold build/check were rerun from that exact version; the decoder removes DATA whitespace and recovers the same pinned source. Do not cite the drafting-copy hash as the immutable material hash.

Only the standard library is used in decisive reconstruction and verification. The observed interpreter was CPython 3.13.5. There is no solver version, random seed, eigenvalue tolerance, or missing numerical candidate affecting acceptance. Every Gram is checked by two exact routes: Fraction Schur elimination with all pivots positive, and independent integer Bareiss computation of all leading principal minors; their determinants are cross-checked exactly. Every local two-by-two cone is checked by its positive first diagonal and determinant. All mixed-centering cancellations, row sums, strict row inequalities, cross cuts, and convex decompositions are exact rational equalities or inequalities.

Reproduced output pins:

mixed_barrier_data.json: 8371 bytes, SHA256 bd045d9f345b1353e73c668113527f4649c0d6a829f4e8200eaa840eb0c60104.

mixed_interior_barrier_data.json: 9190 bytes, SHA256 cc632b78cf4d543622689875b992194f849d13768abe65a434d9425dda333879.

mixed_all_corners_barrier_data.json: 9242 bytes, SHA256 88d24f6da84bc816a85ae2193aabfe6731019ee274a73962b4382c001594d5d6.

row_vertices.json: 5043 bytes, SHA256 b4c1ad248cf8c30d1f061f66b80c679f25a849f8ffc8556089d9edb3bf82c4ff.

row_conic_barrier_all_six_report.json: 77004 bytes, SHA256 ea8972f9bc5dcadf6c5bc3eec268008bcd887c56626f8254548734efce0c7e13.

Fresh cold build and check both produced

TREE253_ALL_SIX_ROW_CONIC_BARRIER_EXACT_PASS 48 6 504 54 26 288
BOUNDARY_AND_STRICT_INTERIOR_MIXED_CENTER_PASS_NOT_A_BODY
ALL_SIX_ROW_CONIC_BARRIER_COMPLETE_SOURCE_RECOVERY_PASS build 15355 579a639ecd07234077b5848e733ec2e0f4b96495d1f5adce23e4b4bdc3a3907a

and the corresponding check marker with the same pins. The counters mean 48 row vertices, six total Gram blocks in three preserved pairs, 504 strict base scalar checks, 54 positive leading minors, 26 distinct block-labelled local two-by-two checks, and 288 labelled cross comparisons. Repeated algebraic cross comparisons are included. These are NOT numbers of excluded polyhedral domains.

## 11. Consequences for the research map and remaining routes

The theorem identifies a specific information loss: replacing the one actual Gram and its exact row-centering relation by a family that only sees a summed centering residual permits distinct high-rank Grams at different rows. The local raw-norm conditions and the new cross-pole cuts do not recover the missing actual incidences, rank, and moments.

There is no contradiction with the accepted terminal-concentration proof t>51/25. That proof excludes the complementary row region t<=51/25; every current counter-row has t>51/25 and lies outside its denied region.

There is also no prohibition on partitioning the row domain and choosing a DIFFERENT gamma in each cell. A cell not containing both counter-rows may admit a genuine certificate. In particular the sector w8<=1/4 excludes the first interior row and is not refuted by this theorem. Numerical failure or success of a locator on such a sector remains separate from a complete exact certificate. At the time this proof was stored, no new certified row-sector exclusion had been accepted.

Other genuinely stronger directions retain the complete actual Lambda identities and shared area/volume moments, impose the real local affine dependence of four incident poles, preserve the physical rank-three geometry, or extend the existing actual-cell joint Gram certificates without dropping their old moment span. The durable mixed-Gram controls should be used as negative tests for any claimed reduction to independent row or cell Grams, not as purported geometric witnesses.
