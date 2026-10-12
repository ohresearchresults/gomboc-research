# material-1a6700a7983b

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# COMMON_VOLUME_PROJECTION_PROFILE_C_V1

## General common-projection theorem
Let P be a full-dimensional convex polyhedron in R^3 with ten genuine vertices v_0,...,v_9, constant solid density, and its own volume centroid at zero. Let M be any common positive-definite real matrix. Suppose the weak rooted path with root v_3 has parents p=(1,2,3,3,3,4,5,6,7,8), so g_i=||v_i||_M^2-<v_i,v_{p(i)}>_M<=0 for each i other than 3. No assumption about S=1, the absence of additional arrows, or strict genericity is required for this theorem.

Put
w=(-4v_0-6v_1+100v_2+100v_3+100v_4+100v_5+85v_6+30v_7)/100.
The coefficients of v_8,v_9 are zero. This is ONE common vector for the entire body, not a different direction chosen for each tetrahedron.

The exact certificate establishes, for every triple A of distinct labels other than 3 except the six triples
018,019,078,079,089,189,
that <w,v_3+sum_{i in A}v_i>_M>0.

Indeed, write a=(-4,-6,100,100,100,100,85,30,0,0)/100 and let c_A be the 0/1 incidence vector of {3} union A. For every one of these 78 triples the preserved source supplies nine nonnegative rational multipliers lambda_i, in increasing tail order 0,1,2,4,5,6,7,8,9, with denominator 100000000. It forms
Q_A=(a c_A^T+c_A a^T)/2 + sum_{i!=3} lambda_i G_i,
where G_i has entry ii=1 and entries i,p(i) and p(i),i equal -1/2. All other entries are zero. Exact rational LDL factorization verifies Q_A positive definite, reconstructs every entry, and gives ten strictly positive pivots for each of the 78 matrices. For the actual vectors this implies
<w,v_3+sum_A v_i>_M + sum_i lambda_i g_i >0.
An invertible square root of M reduces this to three scalar positive quadratic forms with coefficient matrix Q_A. At least one scalar coordinate array is nonzero because the body is full dimensional. Subtracting sum_i lambda_i g_i cannot decrease the expression. This proves the asserted strict positivity, including weak arrow walls.

Suppose every genuine maximal facet not incident with v_3 admits a triangulation into these certified triples, using only its existing vertices. Cone these true facet triangles to v_3. The tetrahedra have positive actual volumes, pairwise disjoint interiors, and partition P. The projection on w of each tetrahedral centroid is one quarter of the strict positive expression just proved. Their positive volume-weighted average is the projection of P's own volume centroid, which is zero. Contradiction. Thus any such body MUST have a genuine nonincident maximal facet with no triangulation avoiding the six listed triples.

This theorem does not say that one of those triples is itself a facet, that an uncertified triangle is realizable, or that failure of the sufficient screen proves feasibility. It works for any common SPD M; the path edges need not be genuine edges in the general theorem. The K3 census application separately checks that they are the marked genuine tree. Artificial diagonals are used only inside genuine facets for a volume decomposition and are never counted in E.

## Exact self-contained recovery
Material [internal-source-reference] is the complete literal source common_profile_c.py, 10718 UTF-8 bytes, SHA256 d7069f70083d752f16268d7d3b06998f9c0e28398e45567c22dbcb05ccdcbbe1. Save that material exactly under that filename. It includes the full 78-by-9 multiplier checkpoint, all profile coefficients, parent labels, precision denominators, matrix construction, rational factorization with reconstruction, and output serialization. No originating sandbox, omitted array, optimizer, random seed, numerical eigenvalue, or external dependency is needed.

Reconstruction: python -S common_profile_c.py build
Verification: python -S common_profile_c.py check
Both commands actually completed in this continuation with assertions enabled. They reproduce common_profile_c.json, 83738 bytes, SHA256 590b34219964bb00343cf5f3c01226a5b864a4e4ae536a1e65d619ed49322e23. Each prints the exact terminal line:
COMMON_VOLUME_PROJECTION_PROFILE_C_EXACT_PASS 78 780 83738 590b34219964bb00343cf5f3c01226a5b864a4e4ae536a1e65d619ed49322e23
Only the Python standard library is used. The 83738-byte output contains every rational pivot and every exact multiplier, not just a marker or hash.

## Current scope
The profile is now independently reconstructible and its geometric implication is proved. Exploratory application to the prior K3 TREE585 remainder suggests 788 newly excluded root positions, leaving 251 in that rooted path shape. Those census counts are NOT promoted by this material alone: their exact application source and literal domain/class transports must be persisted separately first. The accepted universal bounds remain V>=10,F>=9,C>=34. Neither all E17 impossibility, C>=36, an attaining construction nor an exact minimum is proved here. The profile does not use or authenticate Figure650.
