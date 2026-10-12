# material-3c7fa044db5b

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# H5_MACRO_R_HALF_TRIANGLE_ALLROOT_V1

## Theorem and exact scope

For the SAME literal H5 heptagon-triangle geometry used in H5_ORIGINAL_CUBIC_MACRO_BAND_20_ROOTED_TREES_V1, every one of the 48,790 complete rooted primal trees is excluded, uniformly for every nonzero positive-semidefinite physical metric, on

15/16 <= x <= 1,
1/4 <= r <= 1/2,
0 <= lambda <= 1/64,
p >= 0, q >= 0, p+q <= 1/2.

Consequently every genuine interior body in this parameter class has at least two unstable vertices under every positive-definite physical metric. In particular it cannot be proper110, even without invoking a stable-root condition, covariance cap, reciprocal coupling or weak-contact regularization.

This is a MACROSCOPIC independent-r ALL-ROOT class, rather than twenty selected trees. The restriction p+q<=1/2 is essential to the proved statement. It is NOT the entire physical p/q triangle, the full H5 incidence, the entire E17 layer, or an improved global lower bound. The separate accepted C622 attaining construction is unchanged; the global internal interval remains34<=C_min<=622.

The physically reflected class, with x in[1/4,1/2], r in[15/16,1], the same lambda interval and p+q<=1/2, is also excluded. This does not enlarge either rectangular interval on the original prism.

## 1. Literal actual geometry and moving uniform centroid

Let s=1-lambda. The seven basal points are

B0=(1/4,0), B1=(1-3x/4,0), B2=(1-p,p), B3=(q,1-q),
B4=(0,1-3r/4), B5=(0,1/4), B6=(1/16,1/16).

The ten vertices are z_i=(s B_i,0), i=0,...,6, and
z7=(0,0,1), z8=(lambda,0,1), z9=(0,lambda,1).

The literal face cycles are
(6,5,4,3,2,1,0), (8,7,0,1), (7,6,0), (1,2,8),
(9,8,2,3), (9,3,4), (4,5,7,9), (6,7,5), (7,8,9).

They give exactly17 undirected true edges in the strict shape domain. For 0<x,r<1, p,q>0, p+q<1 and0<lambda<1, this is the genuine uniformly filled V10/E17/F9 polyhedron. Closed prism boundaries may collapse indexed vertices or facets. The polynomial certificate includes those indexed limits; it does NOT claim the limits retain the proper lattice.

The oriented fan from z0 is
(0,1,2,8), (0,9,8,2), (0,9,2,3), (0,9,3,4),
(0,4,5,7), (0,4,7,9), (0,6,7,5), (0,7,8,9).

Define
A=(31-24xp-24rq)/64,
Bx=509/3072-3xp/8+3x^2 p/32+xp^2/8-rq^2/8,
By=509/3072-3rq/8+3r^2 q/32+rq^2/8-xp^2/8.
Then the true volume and unnormalized first moments are
V=A s^2/3+lambda/6,
Jx=s^3 Bx/4+s^2 lambda(1-3xp/4)/24+lambda^2/24,
Jy=s^3 By/4+s^2 lambda(1-3rq/4)/24+lambda^2/24,
Jz=A s^2/12+lambda/12+lambda^2/24.

The executable proves all four as exact FIVE-VARIABLE fan identities. The centre is g=J/V and moves with every parameter. It is not the old r=1/3 centre. On the larger natural closed domain, 7/64<=A<=31/64 and7/192<=V<=1/6. For the lower bound compare with7(1-lambda)^2/192+lambda/6, which is increasing; the upper bound follows from the convex quadratic's endpoint bounds. These bounds therefore hold on the present smaller class too.

## 2. Original polynomial stresses and continuous positivity

For each true directed arrow i->j define
G_ij=-sym(V z_i-J,z_j-z_i),
where sym(u,v)=(uv^T+vu^T)/2.
For nonnegative integer weights w_ij, W=sum w_ij>0, put G=sum w_ij G_ij. The accompanying303 sparse weight rows specify every weight literally. Arrow indices are in lexicographic order over the34 directed versions of the17 edges computed from the displayed face cycles. No coordinate, incidence, seed weight or rounding parameter is omitted.

Each entry of the ORIGINAL G has degrees at most3 inx,3 inr,total3 in(p,q), and4 inlambda. No cubic term is discarded and no global quadratic lowering is used. Set p=u/2,q=v/2 with u,v>=0,u+v<=1. Expand on the tensor product of the degree3 x basis, degree3 r basis, degree3 physical-triangle basis and degree4 lambda basis. There are800 coefficient matrices per stress.

For every one of the303 stresses and all800 of its coefficient matrices C, the verifier proves

C > W*2^-34 I.

This consists of242,400 exact symmetric3x3 tests, each by three positive leading principal minors:727,200 strictly positive integer minors in total. The exact monomial-to-Bernstein transforms are constructed with Fraction arithmetic. Their denominators and the polynomial denominators are then cleared globally. All matrix arithmetic and definiteness decisions thereafter use arbitrary-size integers, not eigenvalue approximations.

The generic physical-triangle transform expands each old degree3 Bernstein basis polynomial at the three new triangle vertices and converts it back to the degree3 basis. The source checks that every transition coefficient is nonnegative and every row sums to1. Here it is precisely the actual half triangle with vertices(0,0),(1/2,0),(0,1/2), not a rectangular q/y axis swap. Polynomial degree and support bounds are checked explicitly for all34 arrows.

Since all tensor Bernstein bases are nonnegative partitions of unity, the same strict matrix bound holds at every point of the whole closed parameter class. Thus for every nonzero PSD physical M,

(sum w_ij (z_i-g)^T M(z_j-z_i))/W
= -tr(MG)/(WV)
< -2^-34 tr(M)/V
<= -3 tr(M)/2^33.

Every complete tree containing the positive support of a row therefore has at least one strictly negative required arrow.

## 3. Complete tree coverage and the U>=2 consequence

The checker enumerates every nine-edge subset of the17-edge graph, retaining exactly the connected subsets. These are exactly its4879 spanning trees. It orients each toward each of its ten possible roots, obtaining48,790 distinct complete rooted trees. For every one it checks inclusion of the positive support of at least one of the303 certified stress rows. All ten roots have4879 covered trees. This is full coverage, not a count of selected packets or a finite-library survivor claim.

For a genuine body and an SPD M, any vertex that is not a strict unstable vertex has a neighbour with D_ij=(z_i-g)^T M(z_j-z_i)>=0. Along such an arrow,
|z_j-g|_M^2-|z_i-g|_M^2=2D_ij+|z_j-z_i|_M^2>0.
If there were just one strict unstable vertex, choosing one exit at every other vertex would therefore give an acyclic functional graph ending at that root, hence one of the covered rooted trees. The negative stress average contradicts all its required nonnegative arrows. A maximum-distance vertex is itself strictly unstable by the same identity. Thus every genuine body has at least two strict unstable vertices. The conclusion does not assume an absence of other weak contacts.

Reflection swaps physical X/Y and sends the labels by
(0,1,2,3,4,5,6,7,8,9)->(5,4,3,2,1,0,6,7,9,8),
with(x,r,p,q)->(r,x,q,p). The source checks30 vertex identities, V and the three J identities, and reflected-edge equality. The triangle condition p+q<=1/2 is invariant. Orthogonal congruence preserves the PSD cone and trace, proving the reflected-class statement with the same gap.

## 4. Evidence and reproducibility

This is new coordinator computation, not an independent replay of the former20-tree author result. The former literal proof and both of its source units were read fully. Its actual geometry was retained while all34 directed polynomials and all rooted trees were generated.

The numerical proposal stage used common-coefficient eigenvector cuts and a nonnegative linear program. Rounded integer candidates were only proposals. A finite greedy support cover reduced604 candidate rows on the half triangle to303. Every retained row was then checked exactly as above; no retained row failed. A preliminary175-row global-prism library covered9952 trees, but this half-triangle all-root result is the canonical result of this capsule. Neither finite-search failures on the other triangles nor unverified wider searches are physical survivors.

Observed stack: CPython3.13.5, NumPy2.3.5, SciPy1.17.0. Default verification needs only Python and NumPy; SciPy is imported solely inside the optional numerical find() helper. NumPy object arrays hold exact Fraction/integer values in the acceptance path. Assertions must remain enabled. OPENBLAS_NUM_THREADS=1 is the recorded invocation. Normal, clean two-input source-only, and clean THREE-durable-input recovery executions passed. The latter is the complete recovery contract below.

## 5. Complete recovery capsule: THREE inputs required

Input1: material [internal-source-reference], h5_half_triangle_verify.py.txt. Save as h5_half_triangle_verify.py.12320 bytes, SHA25683638e66cfb7a85a0cf7e3123dafe9a7caa20d041288b13b833d053fd979a929.

Input2: material [internal-source-reference], h5_half_triangle_weights.txt. This is the immutable TRANSPORT copy,15549 bytes,SHA256fd119b3865ea589d5637c59292213a7778958e44e313b5b60a227f2468828469. Save it as h5_half_triangle_weights_transport.txt. Eleven consecutive rows were omitted during transport, not in the verified computation. It is not silently treated as the full303-row checkpoint.

Input3: material [internal-source-reference], repair_h5_half_triangle_weights.py.txt. Save as repair_h5_half_triangle_weights.py.1703 bytes,SHA256c62cc2cb9e0a75ed48331c15dd1a2da061bcf4c842e1a4c4bed64cab2bb58368. This COMPLETE hash-checked patch contains all532 missing bytes, requires the exact incomplete-input hash and checks the full reconstructed-output hash.

Reconstruction:
python repair_h5_half_triangle_weights.py h5_half_triangle_weights_transport.txt h5_half_triangle_weights.txt

Reconstructed303-row h5_half_triangle_weights.txt:16081 bytes,SHA256e79e0c50f9b102f81d64b1f3892af660c066bcabd117255442918b0d5b4e70b9.

Verification:
OPENBLAS_NUM_THREADS=1 python h5_half_triangle_verify.py h5_half_triangle_weights.txt --out h5_half_triangle_report.json

Reproduced report: h5_half_triangle_report.json,3713 bytes,SHA256f1a8f9eae6cd48d2973ed37eb1fd57ba374b4479dd5a88651619c21f0ce31225.

Expected terminal markers:
H5_HALF_TRIANGLE_CHECKPOINT_RECOVERY_PASS16081
H5_MACRO_R_HALF_TRIANGLE_ALLROOT_PASS30324240072720048790

The executable prints spaces between the marker numbers. The three exact inputs reconstruct all303 stresses, every coefficient matrix, actual moments, reflection and every covered complete tree without any former sandbox, worker retrieval service or5982-stress archive. The report and local downloadable files are supplementary outputs, not substitutes for these inputs.

## Consequential frontier

The original-cubic approach has now delivered an actual macroscopic-r all-root exclusion, not only a repaired troublesome tree. The remaining physical triangle p+q>1/2, the rest of x/lambda, larger basal moduli and the complete E17 layer are still open. Pointwise common-metric geometry may distinguish a true surviving cone from a need to localize the polynomial certificate further. No exact minimum or new attaining polyhedron is asserted.
