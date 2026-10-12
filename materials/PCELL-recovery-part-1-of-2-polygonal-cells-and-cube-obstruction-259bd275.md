# material-259bd27542aa

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# PCELL-20260925 recovery capsule part 1/2

## Status and relation to prior research

This is a coordinator derivation and an executed exact regression, NOT a class-110 construction, NOT an improved C622 record, and NOT a target-class search below C34. The cube is solely a method test. The affine-moment identity in the earlier CCELL package is a reimplementation of the independent-star formula already present in the shared notebook under Core mechanics and Independent finite-amplitude centroid-neutral mechanism. The current notebook was finally read completely at SHA-256 02c6127d1d3945d0543dd1d6fee02b5cc5b7d8ecef2d696cd97b16eef01f5b9a, 247499 characters. No novelty claim is made for that old identity. Additional work here concerns explicit geometric-face constraints and their second-order obstruction.

Complete dependencies: canonical centroid_cell.py from [internal-source-reference], with proof [internal-source-reference] and corrected manifest [internal-source-reference]. Part 2/2 of this PCELL capsule contains the complete new polygon_cell.py. Both PCELL parts and the three CCELL documents form the full source/proof package.

## 1. Quadratic cells with actual polygonal faces

Let a closed oriented polyhedral sphere have specified geometric polygonal faces and a fixed triangulation of each face. Require proper intersections of geometric faces: any shared two vertices constitute one boundary edge, and distinct faces never share more than an edge. Select moving vertices so that no integration triangle contains two distinct selected vertices. Impose the exact star-volume tangency and true first-volume-moment equations of CCELL. Eliminating these linear equations makes all vertex coordinates affine functions of free parameters z, with constant positive signed volume and zero first moment.

For each geometric face f choose an oriented reference triangle (a,b,c) from its triangulation and set n_f=(b-a) cross (c-a). Its normal is affine because at most one reference vertex moves. Require:
- coplanarity n_f dot(p_j-a)=0 for every other vertex j of f;
- strict external support -n_f dot(p_j-a)>0 for every vertex j not in f;
- n_f dot n_f>0 and n_f dot a>0, the latter putting the origin on the inner side.
All these expressions have degree at most two in z. They are equalities PLUS strict inequalities, not an unconstrained open design box.

Why these are actual polygonal facets: for any boundary edge of f, its adjacent geometric face g has all remaining vertices of f strictly on the same side of g's plane, by proper intersections and strict external support. The two supporting planes intersect in the edge line; their normals cannot be parallel, since a vertex of f outside g would then violate the strict support requirement. Thus every listed boundary edge supports conv(vertices(f)) strictly at its endpoints. Every listed vertex is an extreme polygon vertex, and the cycle is the convex boundary, not a crossing triangulation. The validated closed sphere and its strict supporting planes therefore describe the actual hull. The code separately checks oriented edge ownership, vertex-link cycles, proper face intersections, reference triangles, and consistency of each integration triangulation with its geometric boundary. No integration diagonal is counted as an edge or a saddle carrier.

For actual boundary edges use r_ij=p_i dot(p_i-p_j), and for oriented boundary edge a->b of f use s_fab=n_f dot(a cross b). Both are quadratic or lower. In the latter expression, at most one endpoint moves because the edge is contained in an integration triangle. Stable polygons have all boundary s>0; unstable vertices all incident r>0; saddle edges both directed r>0 and both incident oriented s>0. The corresponding closed predicates detect weak feature equilibria. Coplanarity zeros are imposed geometric equalities and must not be misreported as weak-equilibrium zeros.

This extends the exact cell representation, not the reachable freedom. Planarity equations can eliminate every genuine deformation even when their linearization leaves nonzero tangent directions. The following fixture proves this concretely.

## 2. Exact cube fixture and parameter basis

Start with vertices p0=(1,1,1), p1=(1,-1,-1), p2=(-1,1,-1), p3=(-1,-1,1), p4=-p0, p5=-p1, p6=-p2, p7=-p3. The four last vertices stay fixed. The six geometric faces are coordinate-plane squares. Triangulate each along its diagonal joining two fixed vertices, so every triangle has exactly one movable vertex. At each p0..p3 use the deterministic two-vector basis of the exact volume-gradient perpendicular plane, as in the source.

The true moment-response rank is 3, so the exactly volume-preserving, centroid-zero family has five free parameters z0..z4. In the deterministic source's basis its movable vertices are exactly:
p0=(1+z2+z3, 1+z0-z3+z4, 1-z0-z2-z4),
p1=(1-z1-z4, -1-z0-z1-z4, -1+z0),
p2=(-1+z1-z2, 1+z1, -1+z2),
p3=(-1-z3+z4, -1+z3, 1+z4).
The four fixed vertices above complete the literal family. The oriented triangulated volume is identically 8 and first moment identically zero, including formal points outside the hull chamber; only members satisfying the geometric conditions are physical bodies.

At z=0 the actual cube has S6,U8,H12, no weak features. There are 12 true edges, not the 18 edges of its integration triangulation. This is a diagnostic fixture, not a target candidate.

## 3. Exact local planarity obstruction, including corrected tangent count

Number the faces by coordinate axis 0,1,2 and side -1,+1. Divide each oriented fourth-vertex coplanarity determinant by 4 and call it F0..F5 in that order. The full source records their 90 equality/inequality quadratic tables. The coplanarity Jacobian at zero has rank 2, leaving THREE infinitesimal directions in the five-dimensional centroid-zero family. A provisional earlier narration of rank 3/two directions was incorrect and is withdrawn.

Put u=z2, v=z3, w=z4, a=z0+z2, b=-z1+z2+z3-z4, so z=(a-u,u+v-w-b,u,v,w). Exact polynomial identities, checked coefficient by coefficient in the source, give
F0=b(1-v+w)+(v-w)^2,
F4=-a(1+u)+u^2,
Q=F0+F2+F4=u^2+v^2+(v-w)^2+a(v-u)+b(w-2v).

Suppose the faces are planar and |u|,|v|,|w|<=1/10. Then F0=F4=0 imply
 a=u^2/(1+u), b=-(v-w)^2/(1-v+w).
The denominators are positive. Therefore
 Q >= (1-2r/(1-r))u^2 + v^2 + (1-3r/(1-2r))(v-w)^2
at r=1/10, hence
 Q >= (7/9)u^2 + v^2 + (5/8)(v-w)^2.
But planarity also implies Q=0, forcing u=v=w=0, then a=b=0, then z=0. Thus the original cube is the ONLY planar member in the stated parameter neighborhood. No bound on a,b is needed once the two exact equations are imposed. Only three of the six coplanarity equations already suffice for this local obstruction.

On the linear tangent kernel a=b=0, Q restricts to u^2+v^2+(v-w)^2, a positive-definite form. This is an explicit second-order obstruction. It does not exclude general cube deformations, global affine maps, other handles, translations of adjacent blocks, changed geometry, or any class-110 family. Four fixed affinely independent vertices eliminate any nonidentity global affine motion in this particular fixture.

## 4. Recovery, verification and evidence level

Required input source centroid_cell.py: 15241 UTF-8 bytes, SHA-256 569337ddefb62900e5bb27ed351f857001460885613e195e70bdd408f44e6ef5. Required new source polygon_cell.py in PCELL part 2/2: 11992 bytes, SHA-256 10910aae6d82c9f9593fd8a7192a9890135cafa44cfecf780a60b766a18a3c5e. Dependencies Python 3.10+ standard library only; executed CPython 3.13.5. No random seed, external data, numerical tolerance, or omitted parameter.

Reconstruction and verification:
python polygon_cell.py --output polygon_cell.json
sha256sum centroid_cell.py polygon_cell.py polygon_cell.json
wc -c centroid_cell.py polygon_cell.py polygon_cell.json

Expected polygon_cell.json: 62760 bytes, SHA-256 f36bff8b7eff40124765381a51d33c399dffad26528f2a83fcaf05326cd880d5. Includes complete cube coordinates, geometric faces, reference and integration triangles, tangent handles, exact response/nullspace, coplanarity Jacobian and kernel, and all 90 quadratic tables. The 243 deterministic rational grid points give 21870 exact quadratic comparisons and exact mass-identity checks. These tests check the implementation; the degree and isolation proofs above are not inferred from sampled values.

Observed terminal markers:
POLYGON_GEOMETRIC_EDGES 12 NOT_INTEGRATION_EDGES 18
POLYGON_FIXTURE_S_U_H 6 8 12
EXACT_CENTROID_RESPONSE_RANK 3 FREE_DIMENSION 5
COPLANARITY_JACOBIAN_RANK 2 TANGENT_DIMENSION 3
QUADRATIC_IDENTITY_CHECKS 21870
EXACT_LOCAL_ISOLATION_BOUND 1/10 LOWER_COEFFICIENTS 7/9 1 5/8
POLYGON_CELL_PLANARITY_OBSTRUCTION_PASS

The package preserves a reusable actual-geometric-face tool and a scoped meaningful negative result. It supplies no new figure of proper strict class110 with C<500. Canonical C622 remains unchanged. A constructive successor must choose actual facet-compatible patches with finite freedom and address a specific unwanted equilibrium wall, rather than treating moment-response rank as sufficient or spending true edge budget on artificial facet splitting.
