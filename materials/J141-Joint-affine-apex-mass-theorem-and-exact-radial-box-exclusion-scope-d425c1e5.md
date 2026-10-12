# material-d425c1e53fbd

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J141 — one common affine apex-mass matrix

## Result and scope
No new own110 body is asserted. This is a stronger necessary condition for actual homogeneous centering, beyond independent apex-triangulation/Z3 coefficient rows. It has an exact application to the two all-path radial envelopes of the literal QW49J_LOW62_G9 input, not an exclusion of every radial deformation, every root, or new angular geometry.

The direct exact geometric source is the completely read immutable result figure-0622, SHA256 f63d80e0ada03ac98308d1bd82ccb12165bfc671f6f98a9f940ef747fa5d511e. LOW62 itself remains62/180/120,own121/weak000/primitive000,sole P .27022312879824795,Q[]. Its RAW unstable labels9/45 differ from audit9/46. The complete earlier J140 source and proof is coordinator material [internal-source-reference],SHA d9137e79a50317a555fc855b4238ab43529c213d1ea3895b641db6ba82e07396. J140 proved row-wise Z3 feasibility of BOTH all-path envelopes for EVERY normal; it did not prove common homogeneous mass.

## Common-matrix theorem in dimension three
Let K=conv{x_1,...,x_n} be full-dimensional, of homogeneous volume V and centroid0. Submitted points may be nonextreme. Choose a consistently outward triangulation of the entire maximal-facet boundary, using only submitted extreme vertices. For each oriented triangle f=(a,b,c), set n_f=(x_b-x_a) cross (x_c-x_a). Define

nu_j=(1/(6V)) sum_{f containing j} n_f,
omega_j=nu_j dot x_j,
B_ij=nu_j dot (x_j-x_i).

Set nu_j=0 at unused submitted points. Then

sum_j nu_j=0;
sum_j x_j nu_j^T=I_3;
sum_j omega_j x_j=0;
sum_j omega_j=3;
omega_j>=0;
B_ii=0;
0<=B_ij<=1;
B 1=3 1;
B X=-X,

where X has rows x_i^T. In particular ALL apex coefficient rows arise from ONE collection of n three-vectors nu_j. They are not independent solutions of -x_i=sum_j beta_ij x_j.

Proof. The divergence identities for constant and linear vector fields give sum nu=0 and sum x nu^T=I. Each origin-to-boundary tetrahedron has volume (n_f dot x_a)/6 and centroid (x_a+x_b+x_c)/4. Summing its moment gives sum omega_j x_j=4g=0, and tracing the matrix identity gives sum omega=3. Since0 is interior, each facet height is positive, so omega>=0. For an arbitrary submitted apex x_i, the tetrahedra from x_i to all boundary triangles have nonnegative volumes summing to V; triangles containing x_i have volume0. The sum of the fractions belonging to triangles containing x_j is exactly nu_j dot(x_j-x_i). It lies in[0,1]. Their row sum is3, because each tetrahedron has three opposite-face vertices. Their barycentric moment identity gives sum_j B_ij x_j=-x_i. These arguments still hold when the nominated apex is nonextreme. Boundary diagonals affect the chosen coefficients, not the existence of a common valid collection.

Write N with rows nu_j^T. Then

B=1 omega^T-X N^T,
rank(B)=4,
omega^T B=3 omega^T,
B^2+B=4 1 omega^T.

Indeed rank<=4 follows from the displayed factorization; the independent columns1,X have eigenvalues3,-1,-1,-1, proving rank>=4. The last two identities follow from omega^T X=0 and N^T X=I. Thus the nonzero spectrum is precisely3,-1,-1,-1. This is a statement about the particular geometric coefficient matrix, not every row-wise feasible Z3 matrix. In uncentred coordinates the third identity is sum omega_j x_j=4g rather than0; use centred coordinates before applying the stated stationary identities.

## A linear relaxation at fixed coordinates
For specified X, use3n real unknowns nu_j. Impose the15 scalar equalities sum nu=0, sum x nu^T=I, and sum (nu_j dot x_j)x_j=0, together with all bounds0<=nu_j dot(x_j-x_i)<=1 and nu_j dot x_j>=0. Feasibility is necessary, not sufficient: a feasible arbitrary N need not be the gradient of an actual filled convex hull. This is a joint affine-mass relaxation, not a full reconstruction theorem.

At both LOW62 all-path envelope coordinate arrays the floating phase-I LP was infeasible even with omega>=0 (no positive epsilon). The original actual-centred LOW62 and each envelope translated to its own numerical centroid passed the same floating relaxation. Those tests nominated the following exact certificates; floating HiGHS status alone is not the proof.

## Exact envelope reconstruction
Read the2182-byte literal QW49J_LOW62_G9_INPUT.json,SHA25690cc88f1a89396ed5cbe20e84cb4fc8265ae1b4170cc2d5bf245c024d4c4662e. The exact capsule validates all120 triangular supporting facets,all180 true edges and the homogeneous centroid g. Set R_i=x_i-g. For root r=9 or45, set p_r=1 and define p_i as the maximum product of C_ij=max(0,R_i dot R_j/|R_i|^2) along all paths to r. The capsule reconstructs p by nominated rational equality paths and checks EVERY exact Bellman inequality, including the root. This proves the all-path values rather than just one tree. Set H_i=p_i R_i. The maximum numerator/denominator bit lengths of p are4329(root9) and4104(root45).

## Rational residual certificates, including whole radial boxes
Use the relaxation convention B_ub nu<=b, A nu=e. The recipe contains nonnegative rational multipliers lambda for its inequalities and arbitrary rational mu for its equalities, with denominator10^12. Let

q=b dot lambda+e dot mu,
r=B_ub^T lambda+A^T mu.

A feasible nu would satisfy r dot nu<=q. The rounded dual is NOT claimed to have r=0. Instead its exact residual is bounded using three independent difference constraints at each point. If D_j has rows H_j-H_i for its three nominated indices, then ||nu_j||_infinity<=||D_j^{-1}||_infinity, since every component of D_j nu_j lies in[0,1]. This gives an exact contradiction when q+sum_j ||D_j^{-1}||_infinity ||r_j||_1<0.

For a WHOLE closed box Y_i=k_i H_i,1-epsilon<=k_i<=1, the same fixed dual is retained. Let L_j=||D_j^{-1}||_infinity and delta_j=max_i (||H_j||_1+||H_i||_1) over the three selected indices. If epsilon L_j delta_j<1, Neumann's bound gives ||nu_j||_infinity<=L_j/(1-epsilon L_j delta_j). Each residual coordinate is a constant plus terms linear in the k_i plus one term quadratic in k_j. The recipe evaluates its value r_j at k=1 and a rational slope bound T_j valid throughout the box; |k_j^2-1|<=2epsilon suffices. Therefore

q+sum_j [L_j/(1-epsilon L_j delta_j)] (||r_j||_1+epsilon T_j)<0

certifies infeasibility of the common affine-mass relaxation for EVERY body in that radial box. All signs and this final inequality are checked with standard-library Fraction arithmetic, not floating interval claims.

The executed exact results are:

root9: epsilon=1/27728; fixed-envelope certificate gap approximately -0.0005667081082642509; whole-box gap approximately -0.0002834344980930449.
root45: epsilon=1/11892; fixed-envelope gap approximately -0.0014276921649000686; whole-box gap approximately -0.0007143026447979477.

Consequently no homogeneous convex hull of these62 submitted points Y_i=k_i H_i has centroid0 when ALL k_i lie in the corresponding closed interval[1-epsilon,1]. This even permits input-point retirement and does not assume U1. In a root-normalized sole-U construction on these rays, at least one radius must leave this excluded neighborhood. These are sufficient small exclusions, NOT optimal necessary contraction values and NOT exclusions of the full box0<k_i<=1. New rays, another origin and other root choices remain outside this certificate. In particular the construction goal is not ruled out.

## Exact recovery evidence
The companion source capsule contains all three files required by the standard-library command

python -B -S replay_joint141.py

It recomputes the exact input centering, verifies the common identities on that actual parent as a geometric control, verifies both all-path policies, and checks both whole-box inequalities. Executed terminal markers:

J141_JOINT_APEX_EXACT_RADIAL_BOX_EXCLUSION 9 1/27728 -0.0002834344980930449
J141_JOINT_APEX_EXACT_RADIAL_BOX_EXCLUSION 45 1/11892 -0.0007143026447979477
J141_JOINT_TWO_RADIAL_BOXES_PARENT_CONTROL_PASS 1082059 e885f9098aaa37404e5af3ee0c8ecbdf6efa41c73f6ae4c9734f190619471876

The generated JOINT141_EXACT_AUDIT.json is1082059bytes/SHA256e885f9098aaa37404e5af3ee0c8ecbdf6efa41c73f6ae4c9734f190619471876. Its very long rational inequalities are reconstructed from the compact complete recipes. Exact replay uses CPython3.13.5 standard library only. Floating nomination used NumPy2.3.5,SciPy1.17.0/HiGHS with one numerical thread; that solver is not trusted by the exact checker.

## Next scientific question
The independent Z3 fixed point was a genuine limit of the old relaxation; the common affine identities now separate its two fixed envelopes from homogeneous centering. The remaining question is finite compatible radial or angular geometry, not more independent Z3 iterations. The new necessary condition does not impose actual facet-gradient integrability, and the small-box certificates do not prevent larger coordinated contraction. Both are explicit remaining gaps, not construction impossibility.
