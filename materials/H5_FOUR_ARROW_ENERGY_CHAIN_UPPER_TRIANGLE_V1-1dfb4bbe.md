# material-1dfb4bbeed04

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# H5_FOUR_ARROW_ENERGY_CHAIN_UPPER_TRIANGLE_V1

## Status and significance
Coordinator-derived exact original-polynomial certificate. This excludes a four-arrow path uniformly on a five-parameter macroscopic H5 domain lying wholly above p+q=1/2. It covers 807 labelled rooted trees, including 190 pure basal-route trees which the previously proved maximal scalar norm oracle cannot exclude. It is NOT an all-H5 theorem, a whole V10/E17/F9 exclusion, an attaining example, or a complexity-bound improvement. The accepted interval remains 34 <= C_min <= 622.

The norm-oracle comparison uses the completely read immutable author result minimum-0246, SHA256 af162492fd1bf1598c3c52ebc979b310c73e8a8d04ae4b557455be4e4cae8ce1. The new polynomial certificate and coverage enumeration were executed by the coordinator, including a fresh source-only recovery. No independent replay of that parent was required. The exact counts of a full union with earlier stress libraries have NOT been computed here; 807 is support coverage, not 807 guaranteed new trees beyond every prior method.

## 1. Genuine physical family
Put s=1-lambda. The seven basal vertices are z_i=(s B_i,0), where
B0=(1/4,0), B1=(1-3x/4,0), B2=(1-p,p), B3=(q,1-q), B4=(0,1-3r/4), B5=(0,1/4), B6=(1/16,1/16).
The apical vertices are z7=(0,0,1), z8=(lambda,0,1), z9=(0,lambda,1).
The oriented facet cycles are
(6,5,4,3,2,1,0), (8,7,0,1), (7,6,0), (1,2,8), (9,8,2,3), (9,3,4), (4,5,7,9), (6,7,5), (7,8,9).
These yield the true 17-edge H5 graph in the genuine family.

The theorem's physical domain is
15/16 <= x < 1,
1/4 <= r <= 1/2,
p >= 2/5, q >= 1/5, p+q < 1,
0 < lambda <= 1/64.
In particular p+q>=3/5>1/2. The closure x=1, lambda=0, or p+q=1 is used by the polynomial proof as an indexed limit. Those boundary lists are not claimed to be genuine V10/E17/F9 bodies.

The exact true volume and first moments are
A=(31-24*x*p-24*r*q)/64,
Bx=509/3072-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8,
By=509/3072-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8,
V=A*s*s/3+lambda/6,
Jx=s*s*s*Bx/4+s*s*lambda*(1-3*x*p/4)/24+lambda*lambda/24,
Jy=s*s*s*By/4+s*s*lambda*(1-3*r*q/4)/24+lambda*lambda/24,
Jz=A*s*s/12+lambda/12+lambda*lambda/24.
The reference point is g=(Jx,Jy,Jz)/V, the actual centroid of the uniformly filled body. The verifier proves these four moment polynomials equal the oriented-facet tetrahedral formulas exactly, coefficient by coefficient. The body is not recentered at a freely chosen point.

## 2. Four-arrow stress
For a common symmetric nonzero PSD matrix M define
D_ij(M)=(z_i-g)^T M (z_j-z_i).
Select the true edges
(2,3), (3,4), (4,5), (8,2),
namely the path 8 -> 2 -> 3 -> 4 -> 5.
In that order use positive integer weights
(218532,289114,307070,185284), with W=1000000.
Let sym(a,b)=(ab^T+ba^T)/2 and
Cbar=-sum_(i,j) w_ij*sym(V*z_i-J,z_j-z_i).
The certificate proves throughout the CLOSED indexed domain
Cbar > (W/2^20)*I
in the positive-definite matrix order. This retains the original cubic p/q terms and every actual arrow. There is no scalar norm relaxation, global folding, cubic lowering, or independent-centroid approximation.
Consequently
sum w_ij*D_ij(M)/W < -(1/(2^20*V))*trace(M) <= -(3/2^19)*trace(M).
For the final inequality use V<=1/6: A<=1/2 and (1-lambda)^2+lambda<=1 on 0<=lambda<=1 suffice. At least one selected arrow is strictly negative. Therefore no nonzero PSD common metric can satisfy all four weak inequalities D_ij>=0. The exclusion includes singular metrics and ties, not only generic positive-definite metrics.

## 3. Exact uniform positivity
Use interval Bernstein degrees 3 in x, 3 in r, and 4 in lambda. Write
p=2/5+(2/5)*u, q=1/5+(2/5)*v,
u>=0, v>=0, u+v<=1.
Use total-degree-3 triangular Bernstein polynomials in (u,v). This is a triangle, NOT the independent rectangle suggested by the separate p/q coordinate ranges.
There are 4*4*5*10=800 coefficient matrices. After conversion to a common positive integer denominator, multiply each matrix by 2^20 and subtract denominator*W*I. All three leading principal minors of every resulting integer symmetric matrix are strictly positive: 2400 positive minors in total. Sylvester's criterion makes each shifted coefficient matrix positive definite. Nonnegative Bernstein basis functions summing to one establish the uniform matrix inequality, including parameter-boundary points.
The exact triangle power-to-Bernstein factor for u^a v^b at coefficient (i,j), i+j<=3, is C(i,a)*C(j,b)/(C(3,a+b)*C(a+b,a)); common multiplier 6 clears these denominators. The verifier asserts a+b<=3 for every original term. It does not silently discard higher degrees. All checks use integers and fractions; the verification step has no optimizer or floating-point tolerance.

## 4. Exact tree coverage
The verifier constructs the graph from the true facet cycles and enumerates all 4879 unrooted spanning trees, then all ten roots. A rooted tree is covered exactly when it contains all four directed arrows above.
Total covered: 807.
Rootwise counts in label order 0,...,9:
[117,39,0,0,0,307,184,128,0,32].
Among trees with a basal root and with every other basal vertex's parent basal, the counts are
[38,19,0,0,0,76,57,0,0,0], total 190.
These 190 lie inside the parent's 3185 pure basal-route norm-oracle survivors, so the new stress genuinely crosses that method's information ceiling. They are no longer actual-arrow survivors on this domain. A literal covered root-1 example, parent array indexed 0,...,9, is
[1,-1,3,4,5,6,0,0,2,3].
The report preserves all 807 complete parent arrays. No orbit normalization is inferred.

Coordinate exchange gives the reflected theorem by (x,r,p,q)->(r,x,q,p) and label permutation [5,4,3,2,1,0,6,7,9,8]. Its path is 9->3->2->1->0 and its parameter restrictions are the reflected ones. The two shape domains differ; their 807 counts must not be added as coverage at a single common shape.

## 5. Complete recovery capsule and executed pins
Both source parts below are REQUIRED. The proof material alone and a hash alone do not reconstruct the computation.
Recovery capsule part 1/2: [internal-source-reference], save as h5_energy_chain_certificate.py, 7315 bytes, SHA256 cc89f73f6535e443c4ec7097490e8d32723cc65da86ccb6ed107adebf32b7159.
Recovery capsule part 2/2: [internal-source-reference], save as recover_h5_upper_triangle.py, 2878 bytes, SHA256 e56795d71075e535e263c3017fb1ca85448e17c6598b10cce468642175d176be.
The first part is itself a complete retained smaller-box certificate. The second is a complete exact patch with source and target hash checks; it changes bounds, weights and the original-polynomial Bernstein conversion, without omitted helpers.

Reconstruction and verification commands, in a fresh directory containing only the two source files:
python -B -S recover_h5_upper_triangle.py
python -B -S h5_energy_chain_upper_triangle.py output
Use normal assertions; do not use -O. Executed with Python 3.13.5 standard library only. No package dependencies, random seeds, non-default precision, downloads, or external input files are required.
Expected reconstructed source: h5_energy_chain_upper_triangle.py, 7607 bytes, SHA256 84191a070c4fcfa26af3fa5627039bb51d92aac198014e2e15c7b075c1e51f18.
Expected output report.json: 19489 bytes, SHA256 8882ad4a5eae92e5ace9b3f0c221a1a0f53c556afb2fa84efeb84ceebbeff8a4.
Expected output bernstein_matrices.json: 286198 bytes, SHA256 baf531e7cdbfa7c5a5fab297d812dad5b7ca3bdd3ef9a5cccb84b51c67cdd12f.
Expected terminal markers:
H5_UPPER_TRIANGLE_SOURCE_RECOVERY_PASS 7607 84191a070c4fcfa26af3fa5627039bb51d92aac198014e2e15c7b075c1e51f18
H5_CHAIN_ACTUAL_FAN_MOMENTS_PASS 4
H5_CHAIN_ORIGINAL_BERNSTEIN_PD_PASS 800 2400
H5_CHAIN_ROOTED_SUPPORT_COVER_PASS 807 190
H5_CHAIN_CERTIFICATE_PASS
Normal and fresh source-only executions completed with these markers and byte-identical output hashes. Rootwise counts and output hashes here were read directly from the executed report, not inferred from a context summary.

The smaller part-1 box is x in[15/16,1], r in[1/4,1/2], p in[1/2,13/20], q in[1/5,3/10], lambda in[0,1/64], restricted to genuine endpoints as above. Its weights are (3204,2267,1707,2822), W=10000, with1280 original coefficient matrices and3840 positive shifted minors, same807/190 support counts and same normalized arrow margin. Its executed report is19447 bytes SHA256 9382b698539e734c6e0222196dedffdd02ce95a09437c69473d5ec030a004568; matrices445416 bytes SHA256 1346d5c4695627a5199d08ed361526c3930782747c731c4bd3e59c07da1d9fb0. Retaining it preserves the earlier non-record result as well as the final recovery dependency.

## 6. Limits and next mechanism
A failed chosen weight vector or failed coefficient-positivity test is not an actual tree/metric survivor. The successful proof is still a sparse nonnegative stress inside the original complete-arrow cone, not a stronger relaxation. It neither excludes all3185 basal-route trees nor all48790 trees. It does show that sparse directed energy chains can yield macroscopic uniform exclusions precisely where every scalar norm-hull rule is powerless. A useful continuation is a modest library of such genuine-edge chains, chosen for coverage of the residual basal routes and certified by original polynomial matrices, rather than an ever larger norm-order library. The global class110 lower bound and the separately required attaining construction remain open beyond the accepted34..622 interval.
