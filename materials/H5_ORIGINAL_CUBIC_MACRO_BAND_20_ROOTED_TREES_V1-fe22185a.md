# material-fe22185a4085

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# H5_ORIGINAL_CUBIC_MACRO_BAND_20_ROOTED_TREES_V1

## Result and exact scope

For the literal H5 heptagon-triangle family below, consider the closed five-dimensional parameter prism

15/16 <= x <= 1, 1/4 <= r <= 1/2, 0 <= lambda <= 1/64,
p >= 0, q >= 0, p+q <= 1.

One explicitly given nonnegative rational stress excludes TWENTY complete rooted primal trees on this entire prism, uniformly over every nonzero positive-semidefinite physical metric. It includes the literal T56/root2 tree that obstructed the earlier global quadratic lowering. Its reflected twenty trees are excluded on the reflected prism with x in[1/4,1/2], r in[15/16,1], the same lambda range and complete physical p/q triangle.

This is NOT all48790 rooted trees, not a whole-H5 exclusion, not a physical survivor, and not a whole-E17 exclusion or an improvement of34<=C_min<=622. It is a macroscopic independent-r certificate for a definite set of complete tree cones. In contrast with the earlier one-shape-parameter-section rescue, x,r and lambda now vary on the full displayed intervals simultaneously. The original polynomial is used WITHOUT ANY quadratic lowering:800 coefficient matrices replace the obstructed smaller folded basis.

The exact earlier sources were read completely: [internal-source-reference] (global-fold obstruction/original-cubic pointwise rescue, SHA7cb55b4bddd49a3f952640171fc5d1e6a8f807eab82d6e238101eca9ffb282e0) and [internal-source-reference] (complete source, SHA54cef57d721ee9167377de3fcaca380d67ec75cd5cf44f0df6f31f59fd2e7ccf). The present source is a new self-contained generator using the SAME literal incidence and actual moving uniform moments. It is not a renaming of another body or tree. The full-ratio all-root r=1/3 theorem remains a separate result from minimum-0240, SHAe9e9cb5a41c6f3efb409de269963537ed1616b34e6847d48b16feac43b6c92b7.

## 1. Exact family and uniformly filled centroid

Put s=1-lambda and define the basal polygon

B0=(1/4,0), B1=(1-3x/4,0), B2=(1-p,p), B3=(q,1-q),
B4=(0,1-3r/4), B5=(0,1/4), B6=(1/16,1/16).

The ten vertices are z_i=(s B_i,0), i=0,...,6, and

z7=(0,0,1), z8=(lambda,0,1), z9=(0,lambda,1).

The true face cycles are

(6,5,4,3,2,1,0), (8,7,0,1), (7,6,0), (1,2,8),
(9,8,2,3), (9,3,4), (4,5,7,9), (6,7,5), (7,8,9).

For strict shape parameters 0<x,r<1, p,q>0, p+q<1 and0<lambda<1, these are the literal V10/E17/F9 heptagon-triangle faces. One may see their convexity from the convex basal heptagon and top triangle: the three common edge directions give the three lateral quadrilaterals, and the four remaining basal edge directions give the four lateral triangles. The displayed closed parameter prism also contains collapsed indexed limits at x=1, lambda=0 and some p/q edges; these limits are used algebraically, NOT asserted to remain proper E17 bodies.

An oriented fan from z0 has tetrahedra

(0,1,2,8), (0,9,8,2), (0,9,2,3), (0,9,3,4),
(0,4,5,7), (0,4,7,9), (0,6,7,5), (0,7,8,9).

Write

A=(31-24xp-24rq)/64,
Bx=509/3072-3xp/8+3x^2 p/32+xp^2/8-rq^2/8,
By=509/3072-3rq/8+3r^2 q/32+rq^2/8-xp^2/8.

The actual volume and first moments are

V=A s^2/3+lambda/6,
Jx=s^3 Bx/4+s^2 lambda(1-3xp/4)/24+lambda^2/24,
Jy=s^3 By/4+s^2 lambda(1-3rq/4)/24+lambda^2/24,
Jz=A s^2/12+lambda/12+lambda^2/24.

The source checks V and all three J against that fan as exact FIVE-VARIABLE polynomial identities. The physical centre is always g=J/V; it is never frozen at the old r=1/3 body. Over the larger natural domain x,r in[0,1], p/q in the closed triangle and lambda in[0,1], one has7/64<=A<=31/64. Thus7/192<=V<=1/6: the upper bound follows by convexity in lambda and endpoint bounds; the lower comparison7(1-lambda)^2/192+lambda/6 is increasing on[0,1]. In particular the centroid is defined throughout the displayed closed prism.

## 2. Literal stress and the original polynomial certificate

The reference complete tree, rooted at2, is ordered as

T=((0,1),(1,2),(3,2),(4,3),(5,6),(6,0),(7,0),(8,2),(9,3)).

In precisely this order choose

w=(13996235,7149463,13426643,6625331,26409982,17217951,15174395,0,0)/100000000.

Every weight is nonnegative and their sum is1. With sym(u,v)=(uv^T+vu^T)/2, put

G(x,r,p,q,lambda)=-sum_(i,j in T) w_ij sym(V z_i-J, z_j-z_i).

This is the ORIGINAL physical-moment polynomial. Its coordinate degrees are at most3 in x,3 in r, total degree3 in(p,q), and4 in lambda. On the displayed prism expand it in the product Bernstein basis of degrees(3,3,3,4), where the third factor is the ordinary degree-three physical-triangle basis. There are

4*4*10*5=800 symmetric3x3 coefficient matrices.

Every coefficient matrix C satisfies

C-(1/100000)I positive definite.

The source verifies this by EXACT rational arithmetic, checking all2400 leading principal minors. The observed minima of the three shifted leading-minor orders are respectively

169537472711396281/879609302220800000000,
141854317717121457713743322936340223/3094850098213450687247810560000000000000000,
803028137070611530977890237/14843406974976000000000000000000000000.

All are strictly positive. The basis is nonnegative and sums to1, hence G>(1/100000)I at EVERY parameter point of the closed prism. No discarded cubic, local sample, numerical eigenvalue, or vertex-only parameter test is used in this implication.

For transparency the one-variable Bernstein transform of x^k on[a,b] at index i, degree n, used by the code is

sum_(h=0 to min(k,i)) binom(k,h)binom(i,h)/binom(n,h) * a^(k-h)(b-a)^h.

For p^a q^b on the degree-three triangle its coefficient at(i,j), i+j<=3, is

binom(i,a)binom(j,b)/[binom(3,a+b)binom(a+b,a)]

when a<=i,b<=j, and zero otherwise. Their tensor product gives the exact800 matrices; all coefficients and shifts are Fractions, including the object-array arithmetic.

For every nonzero PSD physical M,

sum w_ij (z_i-g)^T M(z_j-z_i)=-tr(MG)/V
                              <-tr(M)/(100000 V)
                              <=-3 tr(M)/50000.

Thus all positively weighted physical arrows cannot be nonnegative. This excludes every complete rooted tree containing the seven-arrow support, even if the other two arrows are not constrained strictly.

## 3. Exact complete-tree coverage, not an all-root claim

The support is

0->1,1->2,3->2,4->3,5->6,6->0,7->0.

It is a directed tree on vertices0,...,7 rooted at2; vertices8 and9 are isolated. The only possible roots of a complete extension are2,8,9. The full H5 adjacency permits8 to point to any of1,2,7,9, and9 to any of3,4,7,8. Vertex2 can leave its existing component only via2->8.

For root2 there are4*4-1=15 extensions: the only excluded choice is the8<->9 cycle. For root8, use2->8 and any of the four9 arrows, giving4. For root9, use2->8 and8->9, giving1. Total20. The code independently enumerates these exact extensions and emits their complete nine-arrow lists; it asserts the count {2:15,8:4,9:1}.

Reflection exchanges x and r, p and q, and the first two physical coordinates. The label permutation is

(0,1,2,3,4,5,6,7,8,9)->(5,4,3,2,1,0,6,7,9,8).

The source checks all30 vertex coordinate identities plus V and the three J reflection identities, and checks the reflected support's complete rooted extensions. Congruence preserves nonzero PSD metrics. This gives twenty reflected exclusions on the REFLECTED prism, not forty trees on the original prism and not a rectangular y/q axis-swap assertion.

## 4. Finding and verification evidence

The numerical proposal method uses the original800 coefficient matrices, nonnegative weights summing to1, and a linear-program eigenvector cutting-plane loop. It found a candidate in seven iterations; the lowest floating coefficient eigenvalue was about1.8182995e-5. Those floating figures are search evidence ONLY. Rounding to the explicit denominator10^8 weights above was followed by the exact2400-minor verification; that exact verification is the certificate.

Observed environment: CPython3.13.5, NumPy2.3.5, SciPy1.17.0. The default verifier uses Fraction arithmetic throughout all polynomial and definiteness checks. NumPy's object matrix product performs Fraction additions/multiplications, not floating-point tests. SciPy is used only by the optional proposal search. All required code, weights, geometry, intervals, degrees and shifts are in the recovery inputs below. There is no dependency on a former sandbox or the5982-stress parent archive.

The complete normal verification passed. A source-only cold directory containing only the exact verified source also passed and reproduced both output hashes. After preserving the source, a single comprehension was noticed to have been mistyped during transport in the OPTIONAL search tensor function; the exact default verification code was unaffected. The durable recovery patch below corrects this one line and verifies the whole reconstructed source hash. A fresh directory with only the TWO durable input units reconstructed the byte-identical source and reproduced both exact output hashes. The typo is not silently reinterpreted as the original source.

## 5. Complete recovery capsule: two exact inputs

Recovery input1/2: material [internal-source-reference], h5_original_band.py.txt,13199 bytes, SHA2567d3e8927d60dabd004a751f699f3d52e58d5fde25f58be81e6e528452005b3f4.

Recovery input2/2: material [internal-source-reference], repair_h5_original_band.py.txt,1251 bytes, SHA25672ae410eb8537a5fc4d6bc422f85f08da76cf3641fe2c3bfc95f863dcbeb4ad7. Save this second unit as repair_h5_original_band.py. Its complete script requires the exact first-input hash, replaces exactly one search-only line, and checks the entire output hash.

Reconstruction command:

python repair_h5_original_band.py h5_original_band.py.txt h5_original_band.py

Reconstructed source: h5_original_band.py,13210 bytes, SHA256d6755a22a6ac68b9a865ea260113501ddba0abb81dd730f43d1dc533a7f91e4a.

Verification command, assertions enabled:

OPENBLAS_NUM_THREADS=1 python h5_original_band.py --out output

Optional numerical proposal command, not needed to verify the exact certificate:

OPENBLAS_NUM_THREADS=1 python h5_original_band.py --search --out search-output

Reproduced exact matrix file: output/h5_original_band_matrices.json,547025 bytes, SHA256a784015e6b1c912d14031ee6c122a9ecba88dba6683dff21b220c225b31448e2.

Reproduced report: output/h5_original_band_report.json,21543 bytes, SHA256f7514de1f69938d70130e1de4f44522b133f2c47efc3716d400632be21cd7a6f. It includes environment version strings, so a different installed version can change the report bytes without changing the rational certificate.

Expected terminal markers:

H5_ORIGINAL_BAND_EXACT_SOURCE_RECOVERY_PASS
H5_ACTUAL_FAN_AND_REFLECTION_IDENTITIES_PASS 4 34
H5_ORIGINAL_CUBIC_MACRO_BAND_20_ROOTED_TREES_PASS 800 2400 20

The generated matrix file is a supplementary explicit rendering; the two exact recovery inputs already reconstruct every coefficient matrix, all complete trees and all checks. They must be supplied together to a computational successor. Their hashes alone are not the capsule.

## Next substantive use

The old global lowering's problematic tree is not an obstruction to macroscopic-r certificates using the ORIGINAL polynomial. This complete800-block source is a second usable route beside the450-block local-fold basis. The next scientific advance would cover all remaining complete trees and the omitted x/lambda regions, or exhibit a genuine common-metric actual-centred surviving cone. A failed finite stress search is neither that survivor nor a lower-bound theorem.
