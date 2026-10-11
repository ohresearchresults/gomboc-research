# material-a7f00acbff76

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Recovery capsule part 2/2: FACE_PIVOT_EXACT_V1 — physical centroid steering and nonsimple-incidence filter

## Status and scope
This is a coordinator-derived exact differential method with rational tests, not a new accepted class110 body. The accepted C622 uniform own-centroid example remains unchanged. No record-body geometry was available to these computations. No historical worker object is renamed. Part 1 is the complete literal runnable source `[internal-source-reference]`, named FACE_PIVOT_EXACT_V1_recovery_part1_source.txt. Both parts are required when this method is supplied as evidence.

## First variation with true polygonal facets
Let P={x:n_i dot x<=h_i} be bounded, convex, full dimensional. Let V>0 and g be its uniform volume and own volume centroid. Facet i has area centroid c_i, area second moment Q_i=average(xx^T), covariance Sigma_i=Q_i-c_i c_i^T, and weight w_i=A_i/||n_i||. All these values are rational for rational vertices and rational outward normals. In particular w_i=(n_i dot area_vector_i)/(n_i dot n_i), avoiding square roots.

For support perturbation n_i(t)=n_i+t dn_i, h_i(t)=h_i+t dh_i, the facet normal speed is (dh_i-dn_i dot x)/||n_i||. Integrate this speed for volume and x times this speed for first moment, then subtract g*dV. Edge/vertex overlap layers contribute only higher-order terms. The result is

    dV = sum_i w_i (dh_i - dn_i dot c_i)
    dg = (1/V) sum_i w_i [(c_i-g)(dh_i-dn_i dot c_i) - Sigma_i dn_i].

The derivative formula does not itself assert preservation of nonsimple incidence.

Pivot facet i through its original area centroid: dh_i=c_i dot dn_i. Then

    dV=0,
    dg=-(w_i/V) Sigma_i dn_i.

Sigma_i has rank two and kernel span(n_i), because a positive-area polygon has strictly positive variance in every nonzero tangent direction. Two nonparallel facets therefore supply raw centroid derivative rank three: their image tangent planes have combined orthogonal complement span(n_i) intersect span(n_j)={0}. At a simple polytope, sufficiently small changes with the remaining support planes fixed preserve the graph; the implicit function theorem gives local control of the three centroid coordinates. This does NOT show a distant target centroid is reachable before incidence/equilibrium walls. Volume is preserved only to first order, not exactly. Density remains uniform.

## Remove translation gauge for fixed normals
Set B[:,i]=w_i(c_i-g)/V and let N have rows n_i. Translating all planes by an arbitrary vector gives B*N=I_3. Scaling the body about the origin gives B*h=g. Hence P0=I-N*B satisfies P0^2=P0, B*P0=0 and P0*N=0. It projects offset controls onto centroid-neutral directions and eliminates the unhelpful whole-body translation gauge. The code tests both identities exactly.

## Nonsimple vertices: raw rank is insufficient
For every original vertex v, choose three independent incident facet normals. They determine dx_v from

    n_i dot dx_v = dh_i - dn_i dot v.

Every additional incident facet supplies another equality. Collect these linear equations as K*z=0 for coefficients z of the chosen control modes. The correct usable first-order centroid map is D restricted to ker(K), NOT the unconstrained D. The compatibility equations are necessary, not sufficient, for an exact finite continuation preserving multiple contacts. Intentional contact release may remove selected rows, but then the finite body and true face/edge counts must be reconstructed.

Exact control examples included in the complete source:
- Standard tetrahedron, two nonparallel faces: raw rank3, compatibility-constrained rank3, four control dimensions.
- Unit cube, two nonparallel faces: raw and constrained rank3. Parallel opposite faces: both rank2.
- Regular octahedron, faces 0 and1 generated in the exact test: raw rank3 but four extra-incidence rows leave only one control dimension and constrained centroid rank1.

The octahedron is a concrete warning against assuming that rank-three facet-pivot steering preserves the low-C graph at nonsimple vertices. The tetrahedron derivative was also checked independently against the average of four vertex velocities obtained by differentiating their three incident support planes.

## Intended application and remaining burden
Supply the exact true vertices and complete outward true facets of C616/C622 or another durable candidate. Do not supply artificial coplanar triangulation edges. Evaluate candidate face pairs away from protected terminal structures using steering_rank; add target-contact compatibility rows when needed. A rank-three constrained map can correct physical centroid error locally while other changes address the unwanted saddle/extremum. Every finite candidate still needs complete exact geometry, actual uniform-volume recentering, all true-face/vertex/edge strict and weak equilibrium tests, C<622, and its own durable recovery capsule. This method alone proves no new endpoint and no global exclusion.

## Reconstruction and verification
Part 1 is the full literal contents of face_pivot.py, UTF-8 with LF. Save its text without a wrapper as face_pivot.py. This final stored version has a docstring-only two-character change compared with the initially tested local file; its final stored bytes were independently matched locally and the same exact tests were rerun.

Environment exercised: Python 3.13.5, standard library only; source requires Python>=3.10. No external packages, hidden helper files, seeds, or non-default precision settings.

    python face_pivot.py --self-test > expected_selftest.txt

Input/source face_pivot.py: 11814 bytes; SHA-256 4af35c279491d98ad5deb946757cf54602b66637393cf92e7c6c3b21524779e4.
Output expected_selftest.txt: 455 bytes; SHA-256 c13b134bccb9a24f07fdfd8d6c878086eabaa663ed80afdd5b2c2f8b232bbb25.
Expected exact output below, with LF after each of the two lines:

```text
{"cube_nonparallel":{"allowed_dimension":4,"incidence_preserving_rank":3,"incidence_rows":0,"raw_rank":3},"cube_parallel":{"allowed_dimension":4,"incidence_preserving_rank":2,"incidence_rows":0,"raw_rank":2},"octa_nonsimple":{"allowed_dimension":1,"incidence_preserving_rank":1,"incidence_rows":4,"raw_rank":3},"octa_pair":[0,1],"tetra":{"allowed_dimension":4,"incidence_preserving_rank":3,"incidence_rows":0,"raw_rank":3}}
FACE_PIVOT_EXACT_SELFTEST_PASS
```
