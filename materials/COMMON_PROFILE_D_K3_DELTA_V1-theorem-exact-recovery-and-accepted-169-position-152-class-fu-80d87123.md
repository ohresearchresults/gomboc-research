# material-80d87123cc3d

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# COMMON_VOLUME_PROJECTION_PROFILE_D_V1 and COMMON_PROFILE_D_K3_DELTA_V1

## General theorem and full proof
Let P be a full-dimensional convex polyhedron of constant solid density with ten distinct genuine vertices v0,...,v9 and its OWN volume centroid at zero. Let M be a common positive-definite real mechanical matrix. Suppose the weak root3 path has parents p=(1,2,3,3,3,4,5,6,7,8): g_i=||v_i||_M^2-<v_i,v_p(i)>_M<=0 for all i other than3. Set the single body-wide vector
w=(-v0-v1+20v2+100v3+20v4+20v5+17v6+6v7)/100.

For every triple A excluding3 except089 and789, the exact source [internal-source-reference] supplies nine nonnegative rational multipliers lambda_i, increasing tail order0,1,2,4,5,6,7,8,9, denominator100000000. Let a=(-1,-1,20,100,20,20,17,6,0,0)/100 and c be incidence of{3}union A. Form Q=Sym(a,c)+sum_i lambda_i G_i, where G_i has entryii=1 and entriesi,p(i) andp(i),i equal-1/2. All82 matrices have strictly positive exact rational LDL pivots,820 in total; every matrix entry is reconstructed from LDL, not just checked by floating eigenvalues.

For any actual vector configuration the sum of the three scalar quadratic forms with coefficient matrix Q, after applying a square root of common M, is
<w,v3+sum_A v_i>_M+sum_i lambda_i g_i>0.
At least one coordinate vector is nonzero because P is full dimensional. Since every g_i<=0, the projection term is strictly positive. This also covers weak-arrow equalities. The algebraic statement does not require the path edges to be genuine or S=1, but the geometric census application additionally checks all genuine edges and actual facets.

If every genuine maximal facet not containingv3 can be triangulated by these82 triples, cone each actual facet triangle to v3. These tetrahedra have positive ACTUAL volumes, disjoint interiors and union P. Each tetrahedral centroid projects positively onto the SAME w. Their actual volume-weighted average therefore also projects positively, contradicting P's own uniform volume centroid0. No arbitrary tetrahedral weights, different body for different terms, different metric, or different w among tetrahedra is allowed or used. An artificial facet diagonal is only a decomposition aid and never increases E.

When the path edges are genuine, the only nonincident maximal facet cycles that have no certified triangulation are exactly
089,789,0789
modulo cyclic rotation and reversal. To see this directly, any facet with a vertex outside{0,7,8,9} has a certified fan from that vertex. For a triangle on those labels the only bad triples are089 and789. A four-vertex facet contains both genuine path edges78 and89, which must be boundary edges of that facet, so its only possible cyclic order is0789 up to rotation/reversal. Both quadrilateral triangulations contain a bad triangle: the diagonal08 gives089, and the diagonal79 gives789. Conversely each of the listed three cycles fails the screen. The application source also independently checks this classification on all1470 path-compatible nonincident polygon cycles. Thus any actual body with this weak TRUE path must have at least one of these three genuine maximal facets. This necessary condition is not a realization theorem.

## Exact current K3 delta
The parent accepted endpoint is COMMON_PROFILE_C_K3_DELTA_V1, [internal-source-reference]: TREE585251positions/228classes, overallK35871positions/4316classes. The new source [internal-source-reference] starts with precisely those251 literal positions and applies one complete profileD to each actual facet fan. It excludes169 more positions in152 WHOLE genuine rooted facet/tree classes, using1613 actual facet triangles. TREE585 now has82positions/76classes. Overall K3 now has5702positions/4164classes.

These169 new removals are disjoint from profileC's788 because they are selected only from its explicit remaining list. C andD are complete alternative body-wide proofs, not profiles mixed between facets in one proof. Combined they exclude957 of the previously1039 TREE585 positions and653 of729 classes. Every251 class-member transport in the parent open subset is rechecked on true edges, marked tree, all maximal facet cycles, incidence, common orientation and the unique root3 short-to-long path order; removed and remaining classes are disjoint. No representative is substituted for a different unverified incidence or root.

Of the82 remaining TREE585 positions,45 have genuine maximal triangle089;37 do not. Complete literal lists of both categories are in the output. Those37 must instead have789 or0789 under the new necessary-facet theorem AND a facet obstructing profileC. Passing these conditions does not prove feasibility. No further exclusion of those37 is claimed here.

Whole-domain counts were NOT recomputed: the pre-C1776 open domains and531 wholly excluded out of2307 remain upper/lower bounds respectively. Counts here are positions and genuine rooted primal facet/tree classes, not counts of unmarked polytope types. Central17/15, endpoint265/185, separate globalTREE410, global632dual-types/52585joint-roots, K2=278/550, and other pole-tree shapes are unchanged. V>=10,F>=9,C=2E>=34 remains the accepted universal statement. No C>=36, C34 attainer, exact minimum or authenticated Figure650 is established.

## Complete recovery graph
1. Recover k3_census.py from complete immutable halves [internal-source-reference] and [internal-source-reference], using [internal-source-reference]. Join without separator, strict base64 decode, zlib decompress. Source13141 bytes,SHA2569d87d21a211545b6174a755b75feda6620e3df8ac4074f0e4703cc51bb9be68a. python -S k3_census.py build reconstructs k3_domains.json2724409 bytes,SHA256f0fae254b43adff66173b78de6f77853370253113b1d331e6f45c9c94ec85ed6. This cold reconstruction actually passed in this continuation.
2. Recover common_profile_c.py from [internal-source-reference],10718 bytes,SHA256d7069f70083d752f16268d7d3b06998f9c0e28398e45567c22dbcb05ccdcbbe1, and common_profile_c_k3.py from [internal-source-reference],9186 bytes,SHA256a97b63ccc19bf76cf71dee4f24dcb46fbfe058f2abb4a014d7de23d1c5068aeb. python -S common_profile_c_k3.py build/check reconstructs common_profile_c_k3.json437927 bytes,SHA25652ea6972118e05a23568a0570ba620dd218acf175391006e69875289bc2c5e91. The full parent proof and older dependencies are in [internal-source-reference].
3. Save the complete literal new source [internal-source-reference] as common_profile_d.py,10944 bytes,SHA25639645ab603eb042278e64b130fb60a3435b291e43f9b464a1768a9a4c8c6ee71. It contains EVERY row of the82-by-9 exact multiplier checkpoint, vector coefficients, parent, all denominators, rational matrix constructor, exact factorization and serialization. No optimizer or omitted array is needed. Run python -S common_profile_d.py build and python -S common_profile_d.py check. Both actually passed and reproduce common_profile_d.json86676 bytes,SHA2563d04c92de704abe3f734569bac130c67461b386c79755db1b229e670acc47523.
Expected terminal line:
COMMON_VOLUME_PROJECTION_PROFILE_D_EXACT_PASS 82 820 86676 3d04c92de704abe3f734569bac130c67461b386c79755db1b229e670acc47523
4. Save [internal-source-reference] as common_profile_d_k3.py,4980 bytes,SHA2569e260f7b6dd49585a162a0370d0a1fda37538182a8f1f4c19b8e075c9226eb4a. Run python -S common_profile_d_k3.py build and python -S common_profile_d_k3.py check. Both actually passed in this continuation. They reproduce common_profile_d_k3.json101526 bytes,SHA256a471cef2825e71eb1a179e08c5ae8b150398258d1751fe99bb5d6813080a5cb5.
Expected terminal line:
COMMON_PROFILE_D_K3_EXACT_DELTA_PASS 101526 a471cef2825e71eb1a179e08c5ae8b150398258d1751fe99bb5d6813080a5cb5

The exact output includes all251 prior positions,169 removals,82 remaining positions,152 removed and76 remaining class IDs,1613 actual triangle witnesses,251 complete class transports, the three-cycle theorem check, and45/37 genuine-triangle partition. Exact checks use CPython3.13.5 standard library with assertions enabled. No floating tolerance, random seed, unsupported determinant sign, false symmetry or local filename replaces the preserved proof/data.
