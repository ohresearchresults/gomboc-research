# material-3b76eb47fe85

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# H5_THREE_FIFTHS_NONPARALLEL_TRANSFER_V2

## Status and scope
Coordinator analytic theorem using the accepted original-arrow stress atlas H5_FULL_BASAL_LAMBDA_GE_3_5_DYADIC_V1. The new rational constant checker was executed exactly; the parent atlas was not independently replayed for this transfer. This is a local extension off the parallel-end slice with the actual homogeneous volume centroid. It is not a whole-H5 exclusion, not an E17-wide exclusion, not an attaining construction, and does not change the accepted global interval 34 <= C_min <= 622.

All coordinates and perturbation radii below are in the literal normalized prototype frame. Every subsequent invertible affine realization is included by allowing every common SPD Gram matrix H. No lower eigenvalue bound on H is imposed. Collapsed parameter endpoints refer only to the indexed polynomial matrices unless a genuine true-facet body is explicitly supplied.

## Exact parent and recovery dependencies
The authoritative parent theorem and complete verifier are in [internal-source-reference], H5_THREE_FIFTHS_Recovery_capsule_part_3_of_3_proof_and_verifier.md, 15124 bytes, SHA256 bd58b38571299c10ed358b4d8d66d1740169b700bf2f794b8969c4e9e93b2994. It was read completely in this coordinator turn. Reconstructing that parent atlas requires its actual four dependencies, not a similarly named older capsule:

- [internal-source-reference]: complete geometry Python block h5_collar_weighted.py, 9389 bytes, SHA256 18d63fc0ed4267051d54e63e780554d042d92d44a38bd445b14effe066c4ac7d.
- [internal-source-reference]: h5_three_fifths_root_rows.txt, 16844 bytes, SHA256 4a2eb99c3df47cf4e34eb74694d4a6b5f33340d894f81000cc309acb41dcdeb0.
- [internal-source-reference]: h5_three_fifths_cell_rows.txt, 6431 bytes, SHA256 efd1b9732d6c6046222bb34d22cb1b486a92b13252136c12f0a67c6d9841e7b7.
- [internal-source-reference]: complete recovery and verification programs plus the parent proof.

The generic boundary-moment perturbation argument was previously proved on the smaller lambda >= 2/3 domain in [internal-source-reference], H5_QUANTITATIVE_NONPARALLEL_NEIGHBORHOOD_V1.md, 6879 bytes, SHA256 316c801e45257a027720d59a9c373a10b344b254c684df9fff99ce6bc97f73e6. It was read completely. The present proof repeats the needed analytic argument and adds the projective covariance estimate, so that historical source is not a missing computational dependency.

The complete new standalone constant-checking source is [internal-source-reference]. Save its exact text as verify_h5_projective_three_fifths.py. It is 3176 bytes, SHA256 e6e9bb057c2b18a5231cf6d795fbc855e5969581ee41f85105939ae7c0789681. Together that literal source and this proof constitute the complete new recovery unit, conditional on the explicitly identified accepted parent theorem. No sandbox file is the sole copy of the new code.

## Literal family and accepted stress premise
Write s = 1-lambda, with 0 <= s <= 2/5. Basal labels 0,...,6 are s times
(1/4,0), (1-3x/4,0), (1-p,p), (q,1-q), (0,1-3r/4), (0,1/4), (1/16,1/16)
at height zero, where 0 <= x,r <= 1, p,q >= 0 and p+q <= 1. Top labels 7,8,9 are (0,0,1), (lambda,0,1), (0,lambda,1). Genuine instances have the nine outward true cyclic facets
(6,5,4,3,2,1,0), (8,7,0,1), (7,6,0), (1,2,8), (9,8,2,3), (9,3,4), (4,5,7,9), (6,7,5), (7,8,9).
There are 17 true edges and 16 oriented boundary fan triangles. No triangulation diagonal is a true graph arrow.

Let D=6V, K=6J and g=K/D be the actual homogeneous volume centroid. Put sym(M)=(M+M^T)/2 and
B_ij = sym((D z_i-K)(z_i-z_j)^T),
C_ij = B_ij/D = sym((z_i-g)(z_i-z_j)^T).
The accepted parent proves: at every point of the full stated parameter domain, every complete rooted true-edge spanning tree contains a positive integer arrow certificate with total weight at most W=16385 and
P = sum w_ij B_ij >= delta I,
delta = 178029/44800000000.
The certificate can depend on the parameter cell and on the tree; no global common choice is assumed. The literal atlas covers all 48790 rooted orientations of the 4879 spanning trees. Its 686 certificates have the stated uniform gap and weight bound.

## Uniform prototype bounds
Let R=3/2 and eta=1/100. Every vertex norm and every pairwise distance is <= sqrt(2) < R. For cross-layer distances the horizontal squared distance is <= s^2+lambda^2 <= 1 and the height difference is 1. Convexity gives the diameter bound throughout the body and ||z_i-g|| <= R. Also 0 <= z_1 <= 1 throughout the body.

The exact source identity D=1-s+2As^2, with 7/64 <= A <= 31/64, gives 3/5 <= D <= 1. Thus ||D z_i-K|| <= R. These are prototype bounds only; the actual moments after perturbation are recomputed below.

## Theorem A: arbitrary same-facet perturbations
Let z'_i be the corresponding vertices of a genuine convex polyhedron with the same listed true cyclic facets, coherently outward, and let max_i ||z'_i-z_i|| <= epsilon=2^-42. No parallelism or transported centroid is assumed. Then every nonzero PSD weak rooted true-edge cone of the perturbed body is excluded. In particular every SPD affine realization has at least two strict unstable vertices, even allowing additional weak contacts.

Proof. It suffices first to assume epsilon <= eta. For one outward fan triangle (a,b,c), determinant multilinearity gives
|det(a',b',c')-det(a,b,c)| <= (3R^2+3R eta+eta^2)epsilon.
There are N=16 such triangles, hence |D'-D| <= 112 epsilon. The signed moment identity
K = (1/4) sum det(a,b,c)(a+b+c)
is valid without requiring the coordinate origin to be inside the body. Since sum |det(a,b,c)| <= N R^3, it follows that
||K'-K|| <= [112(3R+3eta)+3 N R^3]epsilon/4 <= 168 epsilon.
These are the actual uniform volume moments of the new true-facet body.

For A_i=D z_i-K, the preceding bounds give
||A'_i-A_i|| <= (112R+1+112eta+168)epsilon <= 340 epsilon.
The true-edge vector changes by at most 2epsilon. Using ||sym(ab^T)||_op <= ||a|| ||b||, including the product of both changes, gives
||B'_ij-B_ij||_op <= (340R+2R+680eta)epsilon <= 520epsilon.
For each prototype certificate choose the same literal arrow support and the same weights at the perturbed body. Its positive gap is at least delta-520W epsilon. Exact arithmetic gives
(delta/2)-520W/2^42 = 74653252889/1503238553600000000 > 0,
D' >= 3/5-112/2^42 = 824633720797/1374389534720 > 0.
Thus every inherited certificate is > (delta/2) I. Original-arrow tree containment is unchanged because the true graph and labels are retained. This proves the PSD cone exclusion.

## A general actual-centroid projective estimate
Let X be uniform in any convex body with diameter and point norms at most R, and with 0 <= X_1 <= 1. For T_t(x)=x/(1+t x_1), |t| <= eta < 1, the Jacobian determinant is
w_t(x) = det DT_t(x) = (1+t x_1)^-4.
The actual homogeneous centroid of T_t(P), not the projective image of the old centroid, is therefore
g_t = E[w_t(X) T_t(X)] / E[w_t(X)].

For bounded scalar random variables a,b, Cauchy-Schwarz and Var(a) <= range(a)^2/4 give |Cov(a,b)| <= range(a)range(b)/4. Apply this to each unit projection of X and to w_t. Since E[w_t] >= (1+eta)^-4 and range(w_t) <= 4|t|/(1-eta)^5, the vector covariance obeys
||Cov(X,w_t)|| / E[w_t] <= R |t| (1+eta)^4/(1-eta)^5.
Splitting the centroid difference into the weighted mean of T_t(X)-X and the covariance term yields
||g_t-g|| <= R |t| [1/(1-eta)+(1+eta)^4/(1-eta)^5].
This argument explicitly accounts for the nonconstant Jacobian weight.

## Theorem B: a larger explicit nonparallel projective path
For any genuine prototype in the entire lambda >= 3/5 domain, all T_t(P) with |t| <= 2^-37 exclude every nonzero PSD weak rooted true-edge cone. They therefore have U >= 2 in every SPD affine realization, even with weak contacts.

Proof. On |t| <= eta=1/100, the preceding bounds imply
||T_t(z_i)-z_i|| <= [R/(1-eta)]|t| <= 2|t|,
||g_t-g|| <= 4|t|.
Hence the centered vertex vector changes by at most 6|t|, and a true-edge vector by at most 4|t|. Their prototype norms are at most R. Consequently
||C_ij(t)-C_ij(0)||_op <= (6R+4R+24eta)|t| <= 16|t|.
At the prototype, D <= 1 and sum w B >= delta I give sum w C >= delta I. Thus each certificate at time t has gap at least delta-16W|t|. At |t| <= 2^-37,
(delta/2)-16W/2^37 = 1866499801/23488102400000000 > 0.
Every tree therefore retains a positive certificate with gap > delta/2.

All denominators remain positive. In this chart a projective map sends each segment to the segment of its endpoints, with positive reweighted affine parameters, so convexity and the true face lattice are preserved. A supporting plane n.x=h transforms to (n+h t e_1).y=h. The basal plane is still y_3=0, while the top is y_3+t y_1=1; for t != 0 they are nonparallel. No assumption about projective transport of the uniform centroid entered the proof.

## From a stress obstruction to U >= 2
For any nonzero PSD H, weak tree-arrow increase means trace(H B_ij) <= 0 (or trace(H C_ij) <= 0). A positive weighted sum of such inequalities contradicts trace(H P)>0 for a positive definite certificate. For a genuine SPD body, a vertex that is not strict unstable has an incident true-edge direction with nonnegative radial derivative. Such an arrow strictly increases squared H-distance because its distance difference equals twice that derivative plus the positive squared edge length. Choosing one such arrow from every non-strict-unstable vertex gives an acyclic graph. If there were just one strict unstable vertex, it would yield an excluded rooted spanning tree. Thus there must be at least two. Translation and invertible affine realization are absorbed into the actual centroid and a common SPD metric.

## Reconstruction and exact executed check
Save the complete text of [internal-source-reference] as verify_h5_projective_three_fifths.py and run
python verify_h5_projective_three_fifths.py
No input data, seeds, numerical optimizer, external package or nondefault parameter is required by this new checker. Execution used Python 3.13.5 and only its standard library. It checks all rational inequalities and positive reserves above; it is not a verifier of the parent atlas.

Expected source: verify_h5_projective_three_fifths.py, 3176 bytes, SHA256 e6e9bb057c2b18a5231cf6d795fbc855e5969581ee41f85105939ae7c0789681.
Expected output: h5_three_fifths_transfer_report.json, 1308 bytes, SHA256 be5cd2d0b3f91ce5c09c23ede27b475796623bcb836692a8f96fb48bd9d08c1f.
Expected terminal marker: H5_THREE_FIFTHS_NONPARALLEL_TRANSFER_V2_PASS.
These exact bytes and the terminal marker were obtained in the coordinator container before immutable preservation.

## Boundaries and next scientific use
Theorem A enlarges the covered prototype domain to lambda >= 3/5 but does not dominate the older larger arbitrary-perturbation radius on lambda >= 2/3. Theorem B improves the former explicit projective |t| <= 2^-42 continuation to |t| <= 2^-37 while also extending the prototype domain. Both radii remain very small in normalized coordinates; neither controls far-from-parallel H5 realizations.

The reusable new mechanism is the Jacobian/covariance estimate for the actual uniform centroid. It can be paired with other finite complete tree atlases without retaining their parallel parameterization. Useful unresolved directions remain the literal H5 parameter region not already excluded below lambda=3/5 and substantial nonparallel realizations; there is no new evidence here that either is feasible. No global minimum or attaining example follows from these local transfers.
