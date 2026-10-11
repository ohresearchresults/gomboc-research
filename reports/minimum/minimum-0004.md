# minimum-0004

Historical AI scientific report · saved 2026-09-07 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: unreviewed-encoded-blocks-omitted.

---

# Determination: a replacement proof of the universal bound V ≥ 8

**Theorem established in this run.** A finite, full-dimensional convex 3-polytope of constant positive solid density, with exactly one unstable vertex at its own volume centroid, has **at least eight vertices**. No restriction on the number of stable equilibria, symmetry, graph, simpliciality, or simplicity is imposed. The proof below also allows other degenerate equilibrium contacts, provided there is only one strictly unstable vertex in the precise sense stated below.

This is a **new, fully reconstructible computer-assisted proof**, not a recovery of the missing 5,341 certificates. It replaces the inherited proof mechanism with a stronger centroid relaxation. It uses 48 abstract rooted trees, 76 rational parameter cells, and 2,166 positive-definite 6-by-6 matrices. Every matrix was checked both by integer Bareiss leading principal determinants and independently by rational LDLᵀ. The complete input and verification source are embedded below.

**Advance beyond the seven-vertex exclusion.** The same method exactly excludes **109 of all 115 abstract rooted eight-vertex trees**, over their entire capped-centroid parameter domains. The remaining six tree shapes are specified below. Those exclusions use 702 cells and 41,405 positive-definite 7-by-7 matrices, again checked by both exact implementations. This does **not** prove V ≥ 9: an explicit rational, strictly feasible solution of the stronger eight-point relaxation is also supplied.

## 1. What was recovered, and what was corrected

The published baseline is Bozóki–Domokos–Papp–Regős, *The smallest mono-unstable, homogeneous convex polyhedron has at least 7 vertices*, arXiv:2401.17906v2. It proves V ≥ 7 using 5,943 systems and explicitly says that approximately 99% of its V=7 systems were excluded, not all. Its Algorithm 2 retains shadow inequalities and only one scalar coordinate inequality for one root-coned tetrahedron. Its public repository supplies its earlier certificates. The relevant primary-source locations are Algorithm 2 and Sections 5–6 of that paper.

The inherited journal asserts all 139,636 seven-vertex systems were closed, including a residual 1,714 systems in 869 orbits using 5,341 additional integer certificates. No original certificate array or original generator for that claim was recovered here. The supplied later journal itself identifies that evidentiary gap. Source locations: `research-journal(2).md`, the entry headed `2026-08-22T23:04:19.193Z — Run adSA: exact low-vertex lower bound and eight-vertex frontier`, and the final entry headed `2026-09-07T04:52:15.544Z — Independent minimality run: complete source absorbed and global proof landscape`.

There is a decisive correction: **the unaugmented seven-vertex shadow-tree/single-scalar-tetrahedron systems are not all infeasible.** Section 5 supplies a strict rational solution of one such system, with its selected triangle exposed in a genuine full-dimensional seven-vertex polyhedron. Thus a claimed exclusion of *all those unaugmented systems* cannot be valid. Missing certificates might have used additional constraints or subdivisions not documented in the summary; that possibility is not resolved by this counterexample. The asserted vertex bound itself is nevertheless now proved by a different, stronger argument.

Vertex point-mass results, including the eleven-vertex minimum for equal vertex masses established in the distinct primary paper arXiv:2302.04252, do not establish the solid-density theorem. No point-mass bound is imported here.

Source identity: the supplied `source-research-journal(3).md` has 1,737,149 bytes and SHA-256 `1e54e3291077a0f4f0fe4588bb6793b823c7f904caab1c1ac8712bde2c014722`; the extended `research-journal(2).md` has 1,740,620 bytes and SHA-256 `2c0e93da0f0bd25ef846dc9ff724285fcbbc29ed5656b7cdce1eb864bd4b4ec4`. The new certificate identity is **CAP-CENTROID-7/8-v1**. Neither an absent legacy assignment payload nor the old numerical counts are inputs to the new proof.

## 2. Geometric reductions, including nonsimplicial and degenerate scope

Translate the actual volume centroid to 0. Write the vertices as p₀,…,pₙ₋₁.

### 2.1. Shadow-tree lemma

Here a strictly unstable vertex p means

    p · (q − p) < 0  for every other vertex q.

Equivalently, its radial vector is in the interior of its normal cone. If a vertex is not strictly unstable, there is an adjacent vertex q with p·(q−p) ≥ 0: otherwise the functional p·x strictly decreases on every generating ray of the tangent cone, so p would be strictly unstable. This is the shadow-tree mechanism used in arXiv:2401.17906v2; the proof just given specifies the weak boundary case needed here.

For distinct p,q satisfying that weak inequality,

    |q|² − |p|² = 2p·(q−p) + |q−p|² > 0.

Choose one such neighbour for each vertex other than the sole strictly unstable vertex p₀. Norms strictly increase along every chosen arrow. Thus there are no directed cycles, every path terminates at p₀, and the arrows form a rooted spanning tree. Relabel in any parent-before-child order, writing π(i)<i for i≥1. The necessary inequalities are

    fᵢ = |pᵢ|² − pᵢ·pπ(i) ≤ 0.                       (S)

A farthest vertex is strictly unstable: equality in the relevant Cauchy–Schwarz comparison with a distinct vertex of no greater norm is impossible. Thus the root exists and is nonzero. This argument allows degenerate contacts at other vertices, edges, and facets; none requires a perturbation argument.

### 2.2. Full capped-centroid lemma

Triangulate every polygonal facet using its existing vertices. Cone the resulting boundary triangles to p₀. Discard zero-volume cones; the positive tetrahedra partition the polytope up to boundaries. In particular, triangles in a facet containing p₀ may give zero cones even when the triangle itself does not contain p₀. Discarding them is harmless.

Let t_T=Vol(T)/Vol(P). Then t_T>0, Σ_T t_T=1, and the exact homogeneous centroid formula gives

    0 = 4c(P) = p₀ + Σ_T t_T Σ_{i in the opposite triangle of T} pᵢ.

Consequently there are coefficients b₁,…,bₙ₋₁ satisfying

    p₀ + Σᵢ bᵢpᵢ = 0,
    0 ≤ bᵢ ≤ 1,
    Σᵢ bᵢ = 3.                                     (C)

Indeed, bᵢ is the sum of the tetrahedral volume fractions whose opposite triangle contains i. Each tetrahedron contains a given nonroot vertex at most once, proving the upper cap bᵢ≤1. These are **volume-derived variable coefficients**, not equal masses at vertices.

This proof applies directly to every nonsimplicial convex 3-polytope. It introduces no extra vertex and no small geometric perturbation. In particular, the theorem needs **no catalogue of maximal-planar types**: it forgets the graph after retaining its shadow tree and applies to the larger class of all rooted trees. This is an explicit completeness argument covering nonsimplicial bodies rather than an assumed passage to a generic simplicial case.

## 3. The exact algebraic exclusion and its complete enumeration

### 3.1. Certificate matrix

For a parent array π and positive integers wᵢ, form the symmetric n-by-n matrix Q with

    Qᵢᵢ += 2wᵢ,
    Qᵢ,π(i) -= wᵢ,
    Qπ(i),ᵢ -= wᵢ                      for i=1,…,n−1.

All other contributions are zero, especially Q₀₀=0. For one coordinate column x of the vertex array,

    xᵀQx = 2Σᵢ wᵢ(xᵢ² − xᵢxπ(i)).

Under (C), eliminate x₀=−bᵀy, where y=(x₁,…,xₙ₋₁). With S(b)=[−bᵀ; I], define

    Mπ,w(b) = S(b)ᵀ Q S(b).

If Mπ,w(b) is positive definite, summing over the spatial coordinates gives

    2Σᵢ wᵢfᵢ = Σ_coordinates yᵀMπ,w(b)y > 0

unless every nonroot vertex is zero. The latter also makes p₀=0 by (C). Thus a positive-definite certificate contradicts (S) for every nonzero configuration, without needing convexity or even a rank-three assumption.

Crucially, **Mπ,w(b) is affine in b**, because Q₀₀=0. Therefore one fixed positive multiplier vector w certifies an entire bounded parameter polytope whenever its matrix is positive definite at every vertex of that parameter polytope.

### 3.2. Finite parameter coverage

The parameter domain is Hₙ={b∈[0,1]ⁿ⁻¹:Σb=3}. Certificate records partition its containing box by binary bisection. At each step bisect a longest coordinate interval, breaking ties by the smallest coordinate index. A path string records lower (`0`) or upper (`1`) halves. The empty path is the unsplit box.

For each leaf box, intersect with Σb=3. Every vertex of that intersection has all but at most one coordinate at a box endpoint. The verifier enumerates exactly those possibilities, solving the remaining coordinate by the sum equation, and discards candidates outside their intervals. A bounded nonempty intersection has a vertex, so an empty enumeration certifies an empty cell. Prefix-tree checks prove that the leaf boxes cover the full original box, including all boundaries.

Every positive-definiteness test is exact. The verifier builds an integer-scaled congruence SᵀQS independently of the discovery formula, checks every leading principal determinant using fraction-free Bareiss elimination, and separately checks rational LDLᵀ pivots. It never accepts an eigenvalue estimate, SDP status, floating tolerance, or a sampled parameter value.

### 3.3. Complete tree coverage

Every rooted tree can be labelled with each parent preceding its children. Exhaustively enumerate

    π(1)∈{0}, π(2)∈{0,1}, …, π(n−1)∈{0,…,n−2}.

There are (n−1)! such arrays. Canonicalize a rooted tree recursively by enclosing the sorted canonical strings of its children in parentheses. This is a complete rooted-tree isomorphism invariant: an isomorphism exists precisely when the multisets of child subtrees agree, recursively.

The standalone verifier performs this exhaustive enumeration, with **720 arrays at n=7** and **5,040 at n=8**, and checks exact equality of the resulting canonical-key sets with the certificate records plus the explicitly listed unresolved records. No NetworkX atlas, graph download, graph-isomorphism oracle, or published tree count is trusted by the proof checker.

The actual exact terminal results are:

    n=7: 48 rooted shapes; 48 excluded; 76 cells; 2,166 matrices; 0 unresolved.
    n=8: 115 rooted shapes; 109 excluded; 702 cells; 41,405 matrices; 6 unresolved.

### 3.4. Conclusion for all V≤7

For seven vertices, (S)+(C) is impossible by the preceding complete certificate. A smaller configuration satisfying (S)+(C) can be padded to seven abstract points by attaching copies of p₀ as new root children, giving them coefficient b=0. Their shadow inequalities hold with equality; the centroid equation and Σb=3 remain unchanged. The algebraic certificate allows repeated points, so it excludes the padded configuration as well. Padding is only an algebraic device, not a claimed enlargement of the original polytope.

The geometric reductions therefore exclude every full-dimensional homogeneous mono-unstable convex polytope with V≤7. **V≥8 follows**, including the requested strict Gömböc subclass. This is the strongest universal vertex bound established in this handoff; neither eight-vertex existence nor an exact minimum is claimed.

## 4. The precise eight-vertex frontier

A parent string gives π(1),…,π(7), with root 0. The six unexcluded rooted shapes are

    0013456
    0123456
    0123455
    0123445
    0123346
    0123444

For each, the remaining relaxation is exactly (S)+(C) with b∈[0,1]⁷ and Σb=3. The data do not claim all six are feasible. What is proved is that every eight-vertex homogeneous mono-unstable polytope must admit a shadow tree in this list; in fact, every one of its chosen shadow spanning trees must avoid the 109 excluded shapes.

A concrete finite continuation is now available: for each of these six labelled trees, enumerate every 18-edge subset of the 28 possible edges containing its seven tree edges; retain planar triangulations. This is at most six enumerations of 11 additional edges chosen from 21. It covers all triangulated eight-vertex polyhedral boundaries, including triangulations of nonsimplicial bodies. For each retained oriented boundary, restore actual convex-hull support, positive three-dimensional volume, and all three exact moment equations

    Σ_f D_f (p₀+p_i+p_j+p_k) = 0,
    D_f = det(p_i−p₀,p_j−p₀,p_k−p₀) ≥ 0,

with f=(i,j,k) ranging over its outward boundary triangles and zero root cones omitted. Maintain genuine facets/flat diagonals correctly. These are actual volume equations, unlike freely choosing b. If geometric branching is used, weak coplanar cells must not be discarded.

There is also a useful additional necessary condition not yet used in these exclusions. Fix the boundary triangulation and cone it to an arbitrary x∈P. Let w_f(x) be the normalized volume of the cone over triangle f; it is affine in x. Define λ_j(x)=Σ_{f containing j}w_f(x). Then

    0≤λ_j(x)≤1,  Σ_j λ_j(x)=3,  Σ_j λ_j(x)p_j=−x,
    λ_j(p_j)=0.

The last equality holds because every triangle counted there lies in a facet incident to p_j. Put Λ_ij=λ_j(p_i). It is a nonnegative matrix with diagonal zero, row sums 3, entries at most 1, and ΛP=−P. Since each column is affine in p_i, rank(Λ)≤4. Full dimensionality makes the four eigenvectors 1 and the three coordinate columns independent, with eigenvalues 3,−1,−1,−1, so rank is exactly 4 and all remaining eigenvalues are zero. These conclusions follow directly from the displayed affine cone formula; they are not numerical conjectures. Enforcing one common affine family λ_j instead of unrelated root-wise coefficients can tighten the six remaining cases before introducing full determinant moments. No exclusion based on this additional condition is claimed here.

## 5. Two exact witnesses explaining the limits of the relaxations

### 5.1. A strict solution of the old seven-vertex scalar relaxation

Use common denominator D=50,625 and these complete integer rows:

    I0=( 50625,     0,0)
    I1=( 33750, 23625,0)
    I2=( 11475, 31500,0)
    I3=( −7050, 26355,0)
    I4=(−16999, 14280,0)
    I5=(−16999, 14280,1)
    I6=(−16999, 14281,0).

Set p_i=I_i/D and parents (−1,0,1,2,3,3,3). The exact positive shadow numerators I_i·(I_parent−I_i), in order, are

    11390625, 7543125, 4995225, 3307949, 3307948, 3305743.

Yet

    1+x4+x5+x6 = −372/50625 = −124/16875 < 0.

Triangle 456 is exposed by the minimum-x plane, and cone 0456 has positive volume. A maximal-planar boundary subdivision containing both the tree and this triangle has facial triples

    013,123,034,346,015,125,235,356,456,045.

The first four triangulate the planar base of the actual pyramid; the other six are its side triangles. All seven rows are vertices. This lies in the stated graph/tree/tetrahedron relaxation, not merely in an arbitrary nongeometric vector system. Its mass centroid is not 0: all y-coordinates are nonnegative and the filled body has positive-volume points with y>0. Therefore it is not a physical counterexample to V≥8. It is an exact counterexample to the claimed infeasibility of every *unaugmented scalar* system.

### 5.2. A strict interior-coefficient solution of the new eight-point relaxation

Using the preceding I rows, let

    a=(3,3,3,3,9996,9996,9996),
    J0=−Σ_i a_i I_i=(509499612,−428483076,−9996),
    J_{i+1}=10000 I_i  (i=0,…,6),
    v_i=J_i/506250000,
    b_i=a_{i−1}/10000  (i=1,…,7).

The tree has parent string `0123444`. Every shadow inequality is strict; every b_i is strictly between 0 and 1; Σb=3; and v₀+Σb_iv_i=0 exactly. Thus the stronger relaxation itself is genuinely feasible at eight points, even away from the coefficient boundary. The positive barycentric relation and full dimensionality also put 0 in the interior of their convex hull.

The verifier exhaustively enumerates all supporting triples of these eight points, obtaining the twelve actual triangular facets

    012,016,023,034,047,056,057,126,236,346,467,567.

The displayed relaxation tree uses a nonedge witness for vertex 5. This is not a hidden graph assumption: replace the parents of vertices 5 and 6 by vertex 7, retaining the other parents. All seven resulting arrows are genuine hull edges, their shadow inequalities remain strict, and this tree is isomorphic to parent string `0123455`. The verifier checks these additional assertions. Thus the feasibility barrier persists even with genuine-edge shadow witnesses.

It then integrates the genuine solid exactly. Its centroid has z-coordinate **1/506250000**, not zero. Thus this is a strict mono-unstable body relative to an interior auxiliary reference, and an exact barrier to proving V≥9 from (S)+(C) alone—not a homogeneous own-centroid eight-vertex construction.

## 6. Complete recovery capsule

The following single source unit contains every accepted certificate and both exact witnesses. **No download, original journal, solver, external graph package, or local checkpoint is required.** The certificate text is UTF-8/ASCII with LF line endings and one final LF. The eight-vertex text is compressed only to keep the handoff manageable; the complete encoded payload is included.

Exact verification was executed with **CPython 3.13.5**, standard library only. Numerical proposal generation used NumPy 2.3.5, SciPy 1.17.0, and NetworkX 3.6.1, but none of those is part of the accepted proof or needed to reproduce its exclusions. The embedded exact inputs plus verifier reproduce the mathematical findings, rather than rerunning nondeterministic numerical searches.

Save the complete source block as `cap_centroid.py` and run, without Python's `-O` option:

    python3.13 cap_centroid.py

It reconstructs the two certificate files in the working directory and verifies every exclusion. Expected identities:

    cap7.cert: 2244 bytes
    SHA256 0143e6e4118407c44221772451a82d2f2863a4689431e078a53d81fb1e968f66
    cap8.cert: 23319 bytes
    SHA256 15ae74840c1a17192c4b619afa810827eb35b7256d8388bc39b1b5b62e6c6e95
    cap_centroid.py: 17382 bytes
    SHA256 22e8da63c19aef394139e785536264a24929532163eeaaa2cd0d41cc0333f3a7

Expected terminal transcript:

    INPUT 7 2244 0143e6e4118407c44221772451a82d2f2863a4689431e078a53d81fb1e968f66
    EXACT_CAP 7 ROOTED 48 EXCLUDED 48 LEAVES 76 MATRICES 2166 MISSING 0
    INPUT 8 23319 15ae74840c1a17192c4b619afa810827eb35b7256d8388bc39b1b5b62e6c6e95
    EXACT_CAP 8 ROOTED 115 EXCLUDED 109 LEAVES 702 MATRICES 41405 MISSING 6
    SCALAR_V7_RELAXATION_STRICTLY_FEASIBLE
    CAP_V8_RELAXATION_STRICTLY_FEASIBLE_NOT_OWN_CENTROID
    ALL_EXACT_CHECKS_PASS


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]


The executable is also available as a convenience attachment: [cap_centroid.py](sandbox:/mnt/data/lowerbound/cap_centroid.py). The inline capsule, not that link, is the durable definition.
