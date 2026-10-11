# material-1756d27041ec

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# CENTRAL_ROOT_FORCED_FACET_V1

## Theorem and exact scope
Let P be a full-dimensional convex polyhedron whose ten genuine vertices, in a specified order, are v_0,...,v_9. Assume P has constant solid density and its volume centroid is 0. Let M be any positive-definite real 3 by 3 matrix. Suppose r is 4 or 5 and, for every i other than r, the weak inequality

<v_i,v_parent(i)>_M >= <v_i,v_i>_M

holds, where parent(i)=i+1 for i<r and parent(i)=i-1 for i>r. Then P has the following genuine maximal triangular facet:

r=4: {v_0,v_8,v_9}; r=5: {v_0,v_1,v_9}.

In particular, v_0 v_9 is a genuine edge. The path edges need not themselves be genuine edges for this theorem. It does not assume S=1, H=0, absence of other arrows, a particular dual graph, E=17, or fixed affine coordinates. It covers weak arrow equalities, arbitrary positive-definite M, and nonsimplicial P. It requires exactly these ten vertices and the actual uniform volume centroid, not their arithmetic average or independent formal masses.

This is a mathematical theorem, not a claim of historical novelty. Its overlap with previous TREE410 exclusions has not been identified. No universal complexity counter is increased by this theorem alone.

## 1. Projection bounds along a chain
For a chain x_0=u,x_1,...,x_m satisfying <x_i,x_{i-1}>_M >= ||x_i||_M^2, one has

<u,x_m>_M >= -A_m ||u||_M^2,
A_m = cos(pi/(m+1))^(m+1).

To prove this, first replace the inner product by Euclidean coordinates using an invertible square root of M. A zero chain vector forces every following vector to be zero. Otherwise, write alpha_i for the consecutive angles, rho_i for radii, and theta for the angle between u and x_m. The arrow gives rho_i/rho_(i-1) <= cos(alpha_i), with 0 <= alpha_i < pi/2. The spherical triangle inequality gives theta <= sum alpha_i. Concavity of log cos and monotonicity of cos on [0,pi/2] imply

rho_m/rho_0 <= product cos(alpha_i) <= cos(theta/m)^m.

When cos theta >=0 the asserted negative lower bound is automatic. When cos theta <0, multiplying the radius upper bound by this negative cosine gives

<u,x_m> / ||u||^2 >= cos(theta/m)^m cos theta.

The derivative of the last expression is -cos(theta/m)^(m-1) sin((m+1)theta/m). Its minimum on the relevant interval is -cos(pi/(m+1))^(m+1), at theta=m*pi/(m+1). For m=1 the arrow itself gives a nonnegative projection. This proves the bound, including all zero cases by the preceding direct argument.

For depths 1,...,5 use the rational upper bounds

b_1=0, b_2=1/8, b_3=1/4, b_4=7/20, b_5=27/64.

Here A_4=(11+5 sqrt(5))/64 < 7/20, because sqrt(5)<57/25 follows from 3125<3249. All other listed bounds equal A_m.

## 2. Three rational pair certificates
Set g_i=||x_i||^2-<x_i,x_(i-1)> <=0. For the three rows below, form

Q=B||u||^2+<u,x_j+x_k>+sum_i lambda_i g_i.

Its scalar symmetric matrix, ordered (u,x_1,...,x_m), has entries Q_00=B, Q_0j=Q_j0 plus 1/2 and Q_0k=Q_k0 plus 1/2, Q_ii plus lambda_i, Q_(i,i-1) and its transpose minus lambda_i/2. Terms which refer to the same entry are added.

Row 34: (j,k)=(3,4), B=73/128, lambda=(135/128,15/8,10/3,21/8). In the elimination order (x_1,x_2,x_3,x_4,u), the exact LDL pivots are (135/128,25/24,2/3,21/512,5/10752).

Row 35: (j,k)=(3,5), B=5/8, lambda=(28/25,28/15,28/9,5/2,5/2). Pivots in order (x_1,...,x_5,u) are (28/25,49/45,8/9,95/128,15/38,7/600).

Row 45: (j,k)=(4,5), B=3/4, lambda=(271377/250000,3933/2500,57/25,76/23,21/10). Pivots in the same order are (271377/250000,627/625,1083/1100,844/1587,9093/337600,13127/5250000).

All lambda and pivots are positive. Let epsilon=13127/5250000. Elimination of the non-root coordinates yields Q >= last_pivot*||u||^2. Since every g_i<=0,

<u,x_3+x_4> >= -(6127/10752)||u||^2,
<u,x_3+x_5> >= -(46/75)||u||^2,
<u,x_4+x_5> >= -(3/4-epsilon)||u||^2.

The identities and positive pivots are verified entry by entry with Fraction arithmetic in the complete source. Their use is a sum-of-squares identity for arbitrary real vectors, not a numerical feasibility estimate.

## 3. All triples other than one have a positive tetrahedral centroid projection
It suffices to prove the r=4 case; reverse vertex order for r=5. Write u=v_4, short branch a_i=v_(4-i), i=1,...,4, and long branch x_i=v_(4+i), i=1,...,5. Let T be any triple of distinct vertices other than u.

For 79 of the 84 triples, the sum of their three rational depth bounds b_d is at most 19/20. Hence <u,u+sum_T v> >= (1/20)||u||^2 >= epsilon||u||^2.

The other five triples have depths 3,4,5. Two contain x_4,x_5 and one of a_3,x_3. The pair45 certificate and b_3=1/4 give the gap epsilon. The triple {a_3,a_4,x_5} has gap 1-6127/10752-27/64=89/10752 > epsilon. The triple {a_4,x_3,x_5} has gap 1-46/75-7/20=11/300 > epsilon. The sole unhandled triple is T_*={a_4,x_4,x_5}={v_0,v_8,v_9}.

Thus every other triple obeys

<u,u+sum_T v> >= epsilon||u||^2.

The program enumerates all 84 triples at each of the two roots and checks exactly 79 depth cases, 2 pair45 cases, 1 pair34 case, 1 pair35 case, and 1 exception. It verifies all 166 nonexceptional inequalities with the same rational epsilon.

## 4. Why the exception must be a genuine facet
Assume T_* is not a genuine maximal facet. Every maximal facet F not containing u then has a vertex outside T_*. Indeed, a facet has at least three genuine vertices, and if all are in T_* it is exactly that triangular facet. Triangulate each such convex polygon F by a fan from any of its vertices outside T_*. Every triangle in that fan contains the chosen outside vertex, so none equals T_*.

Cone these facet triangles to u. These are positive-volume tetrahedra whose interiors partition P; facets containing u have zero cone volume and need not be included. This is the usual radial decomposition from a boundary vertex of a convex polyhedron. Genuine face polygons have no redundant collinear vertices, so their fan triangles have positive area; u is strictly outside the plane of every nonincident maximal facet.

The centroid of tetrahedron conv(u,T) is (u+sum_T v)/4. Every tetrahedral centroid therefore has M-projection on u at least epsilon||u||^2/4. Their positive volume-weighted average, which is the actual uniform volume centroid of P, has the same strictly positive lower bound. But the assumed centroid is 0. Also u is nonzero because the centroid of a full-dimensional uniform convex body is interior, whereas u is a vertex. Contradiction.

A triangle contained in a larger cofacial polygon is not sufficient to escape this proof: triangulation from an outside polygon vertex avoids it. This is why the theorem forces a maximal triangular facet, not merely three coplanar vertices or a triangulation diagonal.

## 5. Literal incidence control and scope of counters
The source also checks the literal incidence with vertex facet-sets
012,016,023,037,067,1256,2345,3478,458,5678
and ordered vertex path (0,2,3,7,8,9,4,1,5,6). The nine maximal facet cycles in path positions are included literally in the source. Every edge has two incident facets, all vertex links are cycles, V=10,E=17,F=9, the primal path uses true edges, and its dual complement is (6,5,4,3,2,1,0,7,8). Its exact triple-contact windows are {1,2,4}. There is no true edge joining the path endpoints. Both central path roots are therefore excluded, independently of the older exclusion of the quadrivalent endpoint of this same incidence. The program checks explicit positive-cone fan combinatorics with 12 triangles for root4 and 9 for root5.

These are specified root exclusions, not proof that the entire incidence is impossible. Application to the complete K3 census requires a separate literal mapping and overlap ledger. Application to the old global TREE410 register also requires a separate exact overlap map. Neither is implicitly asserted here.

## 6. Complete reconstruction and observed verification
The exact source central_root.py is the byte concatenation, with NO inserted separator, of these ordered immutable materials:
1. [internal-source-reference], 3904 bytes, SHA256 896981ab8dede9900d602c39c5eeb8d07789c138cbfe4e31d5707f47e0a4648c.
2. [internal-source-reference], 2855 bytes, SHA256 fa2d82479f777681ac385b5e1c2df269ca69995ecff8a659acc1f2b8ffc47c40.

Result: central_root.py, 6759 bytes, SHA256 c0fa7d4662c6863efb88ac356e3518a82cbac40bea2fda838be416797868ccaf. UTF-8 text with LF, assertions enabled. It uses only Python standard library; observed interpreter Python3.13.5. There are no random inputs, optimizers, tolerances, omitted helpers, external mathematical packages or environment-dependent parameters.

Reconstruction command, after saving the exact two material texts as central_source_part1.txt and central_source_part2.txt:

cat central_source_part1.txt central_source_part2.txt > central_root.py

Verification command:

python -S central_root.py > central_root.log

Observed exact stdout, five lines including terminal LF:
PATH_PAIR_CERTIFICATES_EXACT_PASS 3
CENTRAL_ROOT_TRIANGLE_SCREEN_PASS 2 166
EXPLICIT_INCIDENCE_FANS_PASS 2 21
VOLUME_CENTROID_MARGIN 13127/21000000
NO_CENSUS_OR_GLOBAL_BOUND_UPDATE

central_root.log: 181 bytes, SHA256 5ab1fd0c582255aa334626c82d149f46b6f434d1458f457d724d0cba13c9bd0a.

The rational verifier was actually executed successfully in this coordinator turn. The source is now stored independently of the originating sandbox. Its draft motivation also appeared in archived coordinator output [internal-source-reference]; that archive is not used as an authority for counters or execution status. The universal accepted bound remains C>=34; no upper construction or exact minimum is established by this result.
