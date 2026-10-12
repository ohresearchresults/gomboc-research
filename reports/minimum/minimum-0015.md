# minimum-0015

AI research report · 2026-09-07 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# C30_CENTROID_BOUNDARY_HANDOFF_V1

## 1. Disposition and scope

**The intended vertex-only, fourteen-triangle C30 degree-three assertion remains unresolved in this handoff.** I have neither a universal proof on those realization spaces nor a counterexample using only the nine actual vertices as triangulation nodes. All 74 C30 types remain globally open; the bracket remains 30 <= C_min <= 1374.

There is, however, an important distinction in the phrase *all genuine triangulations*. **When facet-interior Steiner nodes are permitted, the assertion is false on the literal C30 double-frustum parent.** I constructed and exactly verified a counterexample with nine actual vertices, fifteen true edges, eight maximal facets, and a genuine refined boundary triangulation with sixteen integration nodes and twenty-eight triangles. It has positive beta, B3 beta = 0, the correct ordinary volume normalization, common physical poles and apex weights, strict full reflection, and all eighteen centered quadratic Gauss identities, but its weighted centroid is not the actual homogeneous centroid. This is not a fourteen-triangle counterexample, and it must not be installed as one.

The other durable results are:

* A complete twenty-six-row polynomial representation of B3 and a finite, rank-stratified centroid criterion covering every exceptional zero-minor stratum.
* A new universal **B7 full-density-rigidity theorem for every vertex-only triangulation of a nine-vertex convex polyhedron**, with a projection-and-residue proof rather than the old facet-product isolation argument.
* An exact **vertex-only C32 counterexample with V9,E16,F9**. Thus nine actual vertices alone do not imply cubic centroid rigidity. A related pyramid theorem explains the sharp seven-versus-eight base-vertex obstruction.
* A proof that **no fixed finite potential degree works uniformly over all refinements of the fixed C30 double frustum**. Degree four repairs the particular twenty-eight-triangle counterexample, but there is no uniform refinement-independent replacement order.

The parent’s fourteen-triangle C30 control and its harmless hexagonal-bipyramid density kernel are consistent with all these results. The journal explicitly left the vertex-only C30 exceptional-stratum question open. 

## 2. Exact twenty-six-row matrix and complete centroid characterization

Let T = (a,b,c) be an outward-oriented boundary triangle. Define

    n_T = (b-a) cross (c-a)
    s_T = a+b+c
    H_T = s_T s_T^T + aa^T + bb^T + cc^T
    D_T = det(a,b,c)
    M_(k,T) = D_T (s_T)_k.

Use coordinate indices 0,1,2. The following twenty-six rows form a matrix C having exactly the row space of B3, at every real realization, including rank-deficient ones:

    n_i                                                   [3 rows]
    n_j s_i, i != j                                       [6 rows]
    n_i s_i - n_0 s_0, i = 1,2                            [2 rows]
    2 n_k H_ij - delta_ik n_j H_jj - delta_jk n_i H_ii      [15 rows]

The last family is indexed by 0 <= i <= j <= 2 and k in {0,1,2}, excluding i=j=k.

**Proof of the representation.** The rows are the fluxes, multiplied respectively by 2, 6, and 24, of a basis of constant divergence-free fields, traceless linear fields, and homogeneous quadratic divergence-free fields. The quadratic basis is

    2 x_i x_j e_k - delta_ik x_j^2 e_j - delta_jk x_i^2 e_i.

Its fifteen nonreserved monomial coefficients establish independence. Every divergence-free homogeneous field X_d of degree d has polynomial vector potential

    A_d = -(x cross X_d)/(d+2),

because curl(x cross X_d) = -(d+2)X_d. Therefore these fields exhaust curls of potentials of degree at most three. This is an identity of polynomial spaces, not a generic-rank argument. The recovery program additionally compares this matrix with exact segment-integral circulation rows.

Put

    W = D 1 = 6 Vol(P) > 0
    A = [C; D].

The ordinary centroid and beta-weighted centroid, under D beta = W, are

    g(P) = M 1/(4W),
    g_beta = M beta/(4W).

Consequently the following are equivalent for a fixed genuine realization and triangulation:

    Every positive beta satisfying C beta=0 and D beta=W has g_beta=g(P).
    ker(A) is contained in ker(M).
    row(M) is contained in row(A).
    rank([C;D;M]) = rank([C;D]).

Since C 1=0 and D 1=W>0, the volume row always raises rank by exactly one. Thus full beta rigidity on a vertex-only C30 triangulation is equivalent to rank(C)=13. Centroid rigidity may still hold below that rank.

**Positivity cannot conceal a centroid-changing kernel.** If A z=0 and M z != 0, choose any positive epsilon with epsilon max_i |z_i| < 1. Then beta=1+epsilon z is positive, has the actual volume normalization, and

    g_beta-g(P) = epsilon M z/(4W) != 0.

This establishes both directions without a genericity assumption or an optimization argument.

### A polynomial certificate for every rank stratum

This removes the need to divide by an arbitrarily selected nonzero minor. Let G=A^T A, and let e_j(G) be the sum of its j-by-j principal minors, with e_0=1. On the exact rank-r stratum,

    e_r(G)>0,  e_(r+1)(G)=0.

Define

    K_r(G) = sum_(j=0)^r (-1)^j e_(r-j)(G) G^j.

The spectral theorem gives

    K_r(G) = e_r(G) times the orthogonal projector onto ker(A).

Therefore

    Phi_r = trace(M K_r(G) M^T) >= 0,

and centroid rigidity is equivalent to Phi_r=0. Failure is equivalent to Phi_r>0. If its k-th diagonal summand is positive, the explicit vector

    z = K_r(G) M_k^T

is a centroid-changing, zero-volume kernel vector.

For a vertex-only C30 triangulation, there are fourteen columns and only the strata r=4,...,14 to consider; set e_15=0 for the final stratum. The lower limit follows because the actual facet normals span three-space and the volume row is independent. All exceptional strata are retained.

This is a **complete finite characterization**, not a claim that Phi_r has already been proved zero on the C30 domains. Apply it to every actual realization of every one of the 74 parent maps and every vertex-only facet triangulation. The triangulations themselves are generated finitely by splitting a cyclic polygon at triangles (v_0,v_j,v_last), recursively triangulating the two remaining intervals, and taking the product over facets. Convexity makes all those combinatorial triangulations geometrically valid.

A useful rank-adaptive exact formulation retains only

    d = rank([A;M])-rank(A),   0 <= d <= 3,

additional independent first-moment conditions after reduction modulo row(A). Exactly d linear conditions in beta are necessary and sufficient on that fixed geometry; harmless density kernels need not be removed. The coefficients obtained by elimination can be rational functions of the shape, so this should not be advertised as an unconditionally low-degree global elimination.

## 3. Exact C30 counterexample for refined triangulations

### Actual polyhedron

The nine actual vertices, in order, are

    P = [(0,0,0),(8,0,0),(0,8,0),
         (1,1,4),(5,1,4),(1,5,4),
         (1,1,-4),(5,1,-4),(1,5,-4)].

Use the outward maximal-facet cycles

    [(3,4,5),(6,8,7),
     (0,1,4,3),(1,2,5,4),(2,0,3,5),
     (1,0,6,7),(2,1,7,8),(0,2,8,6)].

These are the literal actual-mass control coordinates from the authoritative adapted-mass parent.  The new checker independently reconstructs the supporting facets from all triples, reconstructs their cyclic boundaries and true edges, and verifies extremality using the incident-normal ranks. It obtains exactly V9,E15,F8.

The true edges are

    [(0,1),(0,2),(0,3),(0,6),(1,2),(1,4),(1,7),
     (2,5),(2,8),(3,4),(3,5),(4,5),(6,7),(6,8),(7,8)].

The ordinary volume and centroid are

    Vol(P) = 448/3,
    g(P) = (71/28,71/28,0).

### Genuine refinement and exact density

First fan-triangulate every displayed facet from its first vertex, obtaining fourteen triangles in the displayed facet order. Number them 0,...,13. Refine exactly

    (0,1,2,4,6,8,10).

For each selected triangle (a,b,c), append its centroid q=(a+b+c)/3 as the next integration node, and replace the triangle by

    (a,b,q), (b,c,q), (c,a,q),

in that order. Unselected triangles retain their position in the traversal. The result has sixteen integration nodes, forty-two mesh edges, and twenty-eight triangles. The seven new nodes are strictly facet-interior integration nodes, **not actual vertices**. Twenty-seven mesh edges are not mechanical edges.

In this triangle order, define the complete integer vector

    z = [-10886303014,14047213328,-4700016166,
         -15326749934,-1162865192,17819488114,
         31232995172,-1957160008,-27137052928,7762028660,
         -5398979172,-1731547887,13185140151,-6634321756,
         -1049689164,-3628733268,6184337244,-3013603788,
         -36482654004,788728872,38445801024,-10987595268,
         6383842788,3322247223,-16213921359,6971339404,
         -55800548,2156133820].

Set

    epsilon = 1/3844580102400,
    beta = 1 + epsilon z.

All beta lie between 99/100 and 101/100. Exact rational elimination and direct multiplication establish

    C z = 0,
    D z = 0,
    M z != 0,
    rank(C)=26,
    rank([C;D])=27,
    rank([C;D;M])=28.

Both the ordinary and weighted volumes are exactly 448/3. The false weighted centroid is

    c = (34122307461161/13456030358400,
         11373402934867/4485343452800,
         -68742713/192229005120).

Translate every actual vertex and integration node by -c. The weighted first moment is then zero, whereas the **actual homogeneous centroid** is

    g(P)-c = (-1659052361/13456030358400,
              -2113478667/4485343452800,
               68742713/192229005120) != 0.

The checker evaluates the ordinary volume and moment independently on the original fourteen-triangle boundary and on the refined boundary; it does not infer actual mass from the weighted equations.

### Physical-pole, apex, and quadratic checks

At the translated reference, let q_f be the actual maximal-facet poles, D_t the positive cone determinants, sigma_t the sums of triangle vertices, and

    omega_t = beta_t D_t/(6 Vol(P)).

The exact checks give

    min beta = 317341453533/320381675200 > 0,
    min D_t = 6818959585054/320381675200 > 0,
    min omega = 98230810682946844050071/4105776712338307895296000 > 0,
    min_(i,f) (3+q_f dot p_i) = 16102949005454/19074787820321 > 0.

They also verify, literally,

    sum omega = 1,
    sum omega q = 0,
    sum omega sigma = 0,
    sum omega sigma q^T = I,

and every one of the eighteen equations

    sum_t omega_t [sigma_ti sigma_tj + sum_(v in t) v_i v_j] q_(f(t),k) = 0,

for i<=j and k=0,1,2. For each of the nine actual apex vertices a, the same weights give

    w_(a,t) = omega_t (1-q_(f(t)) dot a),
    sum_t w_(a,t)=1,
    sum_t w_(a,t)(a+sigma_t)=0.

Incident weights are zero and nonincident weights are strictly positive by the separately checked actual incidence slacks. Thus this is not an independent-apex or fictitious-pole construction.

There is no equilibrium-count assertion and no claim that this solid is a Gömböc.

### Smallest repair order for this exact mesh

The exact B4 rank is 27 on twenty-eight triangles. Hence degree-four potentials force beta to be constant after normalization. Since degree three already fails, **four is the smallest sufficient potential order for this particular realization and refinement**. This does not imply a universal degree-four theorem for other refinements.

## 4. Sharp obstruction to any refinement-independent finite order

The same fixed C30 solid can be written

    -4 <= z <= 4,
    x >= |z|/4,
    y >= |z|/4,
    x+y <= 8-|z|/2.

Its eight facet planes also bound the tetrahedral arrangement chamber

    Q = conv{(1,1,4),(5,1,4),(1,5,4),(2,2,8)}.

The checker verifies that its four facet planes are among those same eight planes, that its interior has the appropriate strict plane-sign pattern, and that

    Vol(Q)=32/3,
    g(Q)=(9/4,9/4,5).

Let U(x,y,z)=z(x,y,z). Suppose, for any finite degree, there were a divergence-free polynomial field X and constant a such that on every facet of P

    U dot n = X dot n + a (x dot n).

The polynomial field T=U-X-a x would have zero normal trace on an open subset of every facet plane. Polynomial identity therefore makes its normal trace zero on each entire plane. In particular it has zero total flux on both P and Q. But

    div(T)=4z-3a.

Integration over P, whose z-centroid is zero, forces a=0. Integration over Q then gives 4 Vol(Q) g(Q)_z = 20 Vol(Q) != 0, a contradiction.

Thus the z-first-moment normal trace is outside the span of the volume trace and polynomial divergence-free normal traces of **every fixed finite degree**.

To pass from this trace statement to genuine finite triangulations, use repeated conforming midpoint four-splits of the original facet triangles. Their mesh sizes tend to zero. On any fixed finite-dimensional trace space, the Gram matrices of cellwise-average projections converge to the corresponding L2 Gram matrix. Since the target trace is independent of the flux-plus-volume trace space, sufficiently fine finite refinements retain that independence. Equivalently, at such a refinement,

    rank([B_m;D;M_z]) > rank([B_m;D]).

A zero-volume kernel perturbation of the constant density then gives positive beta and a false z-centroid. All refinement vertices can be rational. A deterministic existence construction is: for fixed m, perform successive midpoint four-splits, form the exact circulation and mass rows, and stop at the first strict rank increase. The argument proves termination; it does not prescribe a small stopping level.

**Conclusion:** no fixed finite potential degree is sufficient simultaneously for all refinements of this one C30 polyhedron. This explains why arbitrary refinement cannot silently be included in a bounded-degree vertex-only theorem. It does not contradict eventual rigidity for a particular finite mesh.

## 5. A closer vertex-only obstruction: exact C32, already with nine vertices

The recovery program also constructs a vertex-only counterexample one true edge above the C30 boundary. Its base is the rational octagon

    b(t)=((1-t^2)/(1+t^2), 2t/(1+t^2), 0),
    t=-4,-3,-2,-1,0,1,2,

followed by (-1,0,0), and its apex is (0,0,1). The outward base cycle is (7,6,5,4,3,2,1,0); the other facets are (i,i+1 mod 8,8). Fan-triangulate the base from its first displayed vertex. There are fourteen triangles and no Steiner nodes.

Exact hull reconstruction gives V9,E16,F9. Its ordinary volume and centroid are

    Vol = 1042/1275,
    g = (-58329/745024,-40923/5960192,1/4).

The exact ranks are

    rank(B3)=12,
    rank([B3;D])=13,
    rank([B3;D;M])=14,
    rank(B4)=13.

The complete deterministic kernel-to-beta construction is in the capsule. It gives a positive normalized density whose actual centroid relative to the false weighted reference is

    (-580854027567072/483831509175813213125,
     -160425398342448/483831509175813213125,
      0).

Thus a proof based only on nine actual vertices is impossible. This example is C32, not C30.

### Why seven versus eight base vertices is a genuine threshold

There is a short universal centroid theorem for pyramids with at most seven base vertices, when the lateral triangular facets are not refined. Arbitrary genuine triangulation of the base is harmless.

Affinely put the apex at 0 and the base in z=1. For a polynomial potential A=phi(x,y) dz of degree at most three, the base-triangle circulations vanish. On a lateral triangle its circulation is a difference of radial integrals at its two base vertices. The operator

    phi -> [b -> integral_0^1 phi(tb) dt]

is invertible on planar polynomials of degree at most three: it divides each degree-d homogeneous component by d+1. Consequently B3 imposes

    sum_i (gamma_(i-1)-gamma_i) p(b_i)=0

for every planar cubic p, where gamma_i is the density on lateral facet i.

At any n<=7 strictly convex planar vertices, cubics interpolate arbitrary nodal data. To isolate one vertex, pair the other vertices, take the product of lines through the pairs, and use one extra line when necessary. At most three factors are needed; no factor passes through the target because no three actual polygon vertices are collinear. Hence every gamma_i is the same.

Subtracting that common density leaves a perturbation supported only on the base. B3 then annihilates all scalar quadratic moments on that plane, in particular its constant and linear moments. It changes neither volume nor first moment. Volume normalization therefore fixes the centroid.

For eight points on a conic, cubic nodal evaluation has dimension at most seven, so this interpolation argument genuinely breaks. The exact C32 example shows that the break can change the centroid, not merely the density. This does not classify all possible C30 obstructions, but it gives a concrete structural boundary rather than another generic sample.

## 6. New universal B7 theorem for the entire vertex-only C30 domain

**Theorem.** Let a connected, closed triangulated polyhedral boundary use N distinct nodes, with no three nodes collinear. If B_(N-2) beta=0, then beta is constant on all triangles. In particular, every vertex-only triangulation of every genuine nine-vertex convex polyhedron has B7 rank equal to the number of triangles minus one. At C30 this rank is exactly thirteen, on every exceptional geometric stratum and for every vertex-only facet triangulation.

**Proof.** Let lambda_e be the coefficient of an oriented edge e in the boundary of the beta-weighted triangle chain. For a generic vector u, the numbers s_i=u dot v_i are distinct. For each vector component define the vertex residues R_i(u) by collecting endpoints in

    sum_e lambda_e (v_j-v_i)/(s_j-s_i) [F(s_j)-F(s_i)]
      = sum_i R_i(u) F(s_i).

The residues are vectors. Their sum is zero. Taking potentials (u dot x)^k dx_l for k=0,...,N-2 shows, by integrating each segment exactly, that

    sum_i s_i^q R_i(u)=0,  q=1,...,N-1.

Together with q=0, these are an invertible N-by-N Vandermonde system. Therefore every R_i(u)=0 for every generic u, and hence as a rational-function identity in u.

Fix an incident edge ij. In R_i its contribution is a nonzero constant multiple of

    lambda_ij (v_j-v_i)/(u dot (v_j-v_i)).

No other incident edge has the same denominator hyperplane, since no three nodes are collinear. Multiply the rational identity by u dot (v_j-v_i) and specialize to a generic point of that hyperplane. The residue gives lambda_ij(v_j-v_i)=0. Thus every lambda_e=0. Adjacent triangle densities agree, and connectedness gives global constancy.

Actual extreme vertices of a convex polyhedron cannot contain a collinear triple. The argument therefore covers all real vertex-only C30 realizations without a nonzero-minor assumption. With D beta=D 1, the constant is one, so the formulation is exact for physical mass.

This is a vertex-count isolation bound with a different proof from the journal’s facet-product degree-nine bound. **It is not a proof of the degree-three assertion**, and it is not asserted to be computationally preferable to the parent’s thirteen actual-volume ratio equations.

## 7. Recovery capsule and observed verification

### Dependencies, identity, and commands

The executed reconstruction uses **CPython 3.13.5, standard library only, assertions enabled**. There are no numerical geometry, SVD, optimization, SAT, or symbolic-algebra dependencies. All coordinates, triangulations, density vectors, and parameters are supplied literally or deterministically constructed in the source.

The source independently implements segment polynomial integration, exact rational row reduction, the twenty-six-row matrix, exhaustive supporting-plane reconstruction, true-edge reconstruction, ordinary and weighted mass integration, actual poles, strict incidence checks, reflection, common-apex equations, and all eighteen quadratic Gauss equations.

Its exact identities are:

    Encoded ASCII payload, whitespace removed:
      4478 bytes
      SHA-256 d355b1d7f751870a571a47a00d6d347799a2d1bd810b27b78066d0b0efc339a19

    Decoded c30_centroid_boundary.py:
      11083 bytes
      SHA-256 2c0586c401994a9f00669b3f8ab717f2d27a6a4b20dd2133d3247bd117b12b93

    Generated c30_centroid_boundary.json:
      13684 bytes
      SHA-256 250bd01180a67f823576ef3d0c7c58e5bfb5b97544b2f5c48df4741147b0821b2

The JSON report contains the complete exact vertices, maximal facets, true edges, integration meshes, C matrices, D and M rows, primitive kernel vectors, beta, ordinary and false centroids, ranks, and margins for both counterexamples.

Save the following complete ASCII stream as c30_centroid_boundary.b85. Whitespace is discarded by the decoder.


[Encoded source block omitted; the code in this passage is incomplete.]


Save and run this complete decoder as unpack_c30_centroid.py:

```python
from pathlib import Path
import base64,zlib,hashlib
b=b''.join(Path('c30_centroid_boundary.b85').read_bytes().split())
assert len(b)==4478
assert hashlib.sha256(b).hexdigest()=='d355b1d7f751870a571a47a00d6d347799a2d1bd810b27b78066d0b0efc339a19'
s=zlib.decompress(base64.b85decode(b))
assert len(s)==11083
assert hashlib.sha256(s).hexdigest()=='2c0586c401994a9f00669b3f8ab717f2d27a6a4b20dd2133d3247bd117b12b93'
Path('c30_centroid_boundary.py').write_bytes(s)
print('C30_CENTROID_SOURCE_RECOVERY_PASS')
```

Commands:

```sh
python3 -S unpack_c30_centroid.py
python3 -S c30_centroid_boundary.py
```

A fresh clean-directory decode and execution was performed. Its observed output was:

```text
C30_CENTROID_SOURCE_RECOVERY_PASS
C30_REFINED_B3_FALSE_CENTROID_V1 PASS [26, 27, 28] B4 27 VOLUME 448/3
C32_VERTEX_ONLY_B3_FALSE_CENTROID_V1 PASS [12, 13, 14] B4 13 VOLUME 1042/1275
SOURCE 11083 2c0586c401994a9f00669b3f8ab717f2d27a6a4b20dd2133d3247bd117b12b93
REPORT 13684 250bd01180a67f823576ef3d0c7c58e5bfb5b97544b2f5c48df4741147b0821b2
C30_REFINEMENT_COUNTER_AND_C32_BOUNDARY_CHECKS_PASS
C30_VERTEX_ONLY_B3_UNIVERSALITY_NOT_DECIDED
```

Convenience copies, not required by the inline recovery: complete decoded source (`c30_centroid_boundary.py`) and complete exact report (`c30_centroid_boundary.json`).

## 8. Parent authority, limitations, and continuation

The conceptual parents remain exactly

    minimum-0012
    f09c802ac38060cd54f4546a2fba39ef7fa4d9bde606e7cd101c934a3ca5b80b

    minimum-0009
    6f905a98d5d84d11e1369aebb34643ad59248a2485b95270c59bb52c48b92326.

No mathematical incidence or alias conflict was found. There is a rendered-byte discrepancy worth preserving: extracting each appended parent body beginning at its first top-level title and stripping trailing whitespace gives respectively 35056 bytes with SHA-256 ea751e07a87351cfb45dabb6a3649ca829267e6255137b574220c73e287d093e, and 43477 bytes with SHA-256 b073e42c222c9c578aaae909d64c18b1abd1a1385cc5fb2b52f733713db34e44. These are not the supplied envelope hashes. I do not infer different mathematical parents from that representation mismatch. The new capsule requires neither rendered parent bytes nor a sandbox predecessor: all of its exact inputs and helpers are embedded.

I explored vertex-only rational geometries and triangulations, then used conic pyramids and controlled boundary refinement to isolate where cubic compatibility can fail. The certified results above, rather than a finite collection of successful generic ranks, are the promoted findings. External searches produced background moment and finite-element material, not a theorem resolving the missing exceptional C30 strata; none of the proofs above relies on an unverified external rank claim.

**The useful remaining target is precise:** on every genuine vertex-only C30 realization and every fourteen-triangle facet triangulation, prove Phi_r=0 on each realizable rank stratum r=4,...,13, or produce one exact point with Phi_r>0. The C32 conic-pyramid mechanism shows a real obstruction that C30’s incidence budget forbids, but I have not proved that every centroid-changing cubic kernel must arise from such a configuration. The refined C30 counterexample cannot substitute for that missing classification. Until it is proved or an actual fourteen-triangle counterexample is found, B3 alone must remain a relaxation in a vertex-only C30 exclusion argument; the new B7 theorem and the parent’s actual-volume compatibility remain exact fallbacks.
