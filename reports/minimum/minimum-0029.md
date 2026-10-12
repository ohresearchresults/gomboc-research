# minimum-0029

AI research report · 2026-09-08 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

# NOVA24_C32_CONDITIONED_CORE_OBSTRUCTIONS_V1

## 1. Determination and authority

**No F≥10 theorem, complete nonpyramidal C32 stable-root/type exclusion, or C32 attainer was obtained.** The new results exclude continuous, unbounded physical subdomains, uniformly over their full affine metric freedom. They do not exclude the complete realization space of a nonpyramidal catalogue type. The requested terminal determination therefore remains open.

The strongest new theorem is a mechanically conditioned, uniform gap from tetrahedral-core saturation:

> If P is a homogeneous own-centred convex three-polytope with strict (S,U,H)=(1,1,0), every contained tetrahedron K satisfies
> 
> Vol(K)/Vol(P) < 1−epsilon_T,
> 
> epsilon_T = 1/(32768·9000^6) = 1/17414258688000000000000000000.

This is about actual volume and actual equilibria, not an arbitrary trace matrix. In particular, two edge-adjacent triangular facets cannot approach reciprocal-product one inside the strict110 mechanical domain. A second theorem gives substantially larger excluded sectors when a four- or five-vertex facet-pair core is closed under an actual escape tree to the unique unstable vertex. A third, weaker but general nine-vertex estimate excludes the symmetric saturation tail left by the preserved physical counterexample.

The immutable analytical parent is **minimum-0024**, SHA-256 **b578a01ead261c6f7745122c22f4bb4767884e46ac46e1531b4e749a19332f95**, `NOVA24_F9_SYNTHESIS_AND_RECIPROCAL_ACTUAL_TRACE_V1`. Its complete payload was read and authenticated: the Markdown, with terminal LF, is 57109 bytes, SHA-256 `927f610bfdf4e8a21074a32aa5581fffe4e1725727bf7ec848a22a26db66b6c3`; its prescribed indented v2 JSON envelope is 57975 bytes and reproduces the declared parent hash. No parent/title/formula conflict was found. The parent's older restricted-wheel discussion is superseded by the journal's complete all-pyramid theorem, not treated as a remaining wheel problem.

The inherited bracket remains **32≤C_min≤1374**. Equality requires (V,E,F)=(9,16,9). The accepted catalogue has 296 types and 21682 joint-root orbits; removing wheel192 removes seven such orbits. Thus the post-wheel catalogue has 295 types and 21675 joint-root orbits, before intersecting any separately recorded root/tree exclusions. This turn removes **zero additional complete types and zero complete joint-root orbits**. The upper construction and the parent's 1890 eight-vector certificates were not reverified in this turn.

## 2. Same-body trace and pole mechanics: retained context

Translate the actual volume centroid of P to zero and write its irredundant facets as q_i·x≤1. With actual volume V, facet areas A_i, support distances h_i and area centroids c_i, define

    d_i=A_i h_i/V,
    Lambda_ij=d_j(1−q_i·c_j),
    T=diag(d) Lambda diag(d)^−1.

Here T is only a diagonal similarity of the physical trace matrix; it is not a new physical pole configuration, and it is not the separate vertex/facet incidence-area matrix called B elsewhere in the journal. The identities are

    Lambda 1=3·1,  Lambda Q=−Q,
    Lambda^2+Lambda=4·1·d^t,
    4d_i=sum_{j≠i} Lambda_ij Lambda_ji.

For K_ij=conv(F_i∪F_j), put v_ij=Vol(K_ij)/V. Then

    T_ij=A_i dist(c_j,aff F_i)/V,
    Lambda_ij Lambda_ji=T_ij T_ji≤v_ij^2.

These quantities all come from the same body's actual mass. In particular, the entries are not chosen independently. The parent proves the uniform physical entry cap c3<10/9 and hence F≥9; that inherited theorem is not extended merely by adding a new matrix identity here.

The preserved `NOVA24_PHYSICAL_C32_CYCLE_BARRIERS_V1` is settled context, not a new discovery of this turn:

* Edge-adjacent triangular facets satisfy **T_ij=T_ji=v_ij exactly**, hence Lambda_ij=v_ij d_j/d_i. An individual Lambda entry is not thereby bounded by one.
* For triangles with exactly one common vertex, let t_ij be the volume of the tetrahedron on their four noncommon vertices, divided by V; it may be zero. With s_ij=(T_ij−T_ji)/2,

      T_ij+T_ji=2v_ij−t_ij,
      Lambda_ij Lambda_ji=(v_ij−t_ij/2)^2−s_ij^2.

* For a three-triangle chain, the normalized forward/reverse cycle sum is 2−tau, not two separately valid bounds by one. Actual nonpyramidal controls can approach reciprocal product one. The negative third principal minor also rules out treating I+Lambda as P0 without an additional hypothesis. These controls are not strict110 bodies.

I reran the preserved complete barrier source and reproduced its 57105-byte report, SHA-256 `5ce27a7e13b1eb0ea63f46d5a60c5d2c0d4f6c65f068af774ca0d9cfc7e2f42a`, including the negative minor `−2626495209961/103553973712244`. This is a replay of inherited evidence, not a new counterexample.

### Where the unique unstable pole enters

An actual stable facet corresponds to an unstable vertex of Q=P^polar at reference zero. Thus S(P)=1 gives a unique strict unstable **pole**. Its weak escape arrows q_i·(q_parent−q_i)≥0 strictly increase squared norm and terminate at that unique pole. The polar is not assumed own-centred.

A stronger consequence of this same actual pole-root condition is needed below. For the actual covariance Sigma of P,

    sqrt(5/3) Sigma^(1/2) Ball ⊆ P ⊆ sqrt(15) Sigma^(1/2) Ball.

The outer inclusion follows by coning from any actual vertex a: if G is the weighted sum of squared tetrahedron vertex-sums, and alpha_i are the actual incidence weights of the other vertices, then

    20(Sigma−aa^t/15)=G+sum_i alpha_i(x_i+a/3)(x_i+a/3)^t ⪰0.

The inner inclusion is the p=1,2 instance of classical Berwald: for f=h_P(n)−n·x, `10 E(f^2)≤16(Ef)^2`, giving `h_P(n)^2≥(5/3)n^t Sigma n`. The classical inequality was checked against the authors' primary HTML statement, equation (1); the mechanical consequences are journal deductions, not claims made by that paper.

For completeness, if a central plane has section radius R0 and both open half-bodies contain points of larger norm, maximizing norm separately on the two half-bodies gives two strict unstable vertices. Off-plane maximizers are actual vertices. An edge crossing the plane has a point of smaller norm, and the squared-edge identity makes its outgoing derivative strictly negative; norm ties do not spoil strictness.

Apply this lemma to P and then to its actual polar. If lambda1≥lambda2≥lambda3 are covariance eigenvalues, U(P)=1 forces lambda1≤9lambda2. The unique unstable pole forces lambda2≤9lambda3. Therefore

    R(P)/r(P)≤3 sqrt(lambda1/lambda3)≤27.                 (A)

This imports neither an independently centred polar nor an arbitrary metric cutoff. Every affine metric is allowed; (A) is a consequence of the hypothetical joint mechanics in its actual Euclidean coordinates. The inherited journal theorem also permits zero nonroot primitives.

## 3. New whole-domain tetrahedral-core exclusion

The following proof is independent of the quantitative eight-vertex certificate. It works for any number of facets and vertices, so covers every C32 root choice.

Normalize R(P)=1. Suppose K⊆P is a tetrahedron and alpha=1−Vol(K)/Vol(P)≤epsilon_T. Set

    delta=1/9000,
    eta=delta^2/16=1/1296000000,
    rho=1/28,
    epsilon_T=delta^6/32768.

### 3.1 Actual missing volume controls Hausdorff distance

For any convex K⊆P⊆Ball(0,1),

    d_H(P,K)≤2 alpha^(1/3).                             (B)

Indeed, take x∈P at distance h from K and the normal of its nearest-point supporting plane. The homothetic copy `x+(h/2)(P−x)` lies on the x-side of that plane, outside K except possibly on the plane. It occupies fraction (h/2)^3 of P. This proves (B), including points and facets on the separating boundary.

Here `2 epsilon_T^(1/3)=eta`. By (A), support functions imply

    Ball(0,rho)⊆K⊆Ball(0,1),

because eta<1/27−1/28. The actual mass partition, not adjustable weights, gives

    |g(K)|≤alpha/(1−alpha)<2 epsilon_T.                 (C)

### 3.2 Two quantitatively unstable tetrahedron vertices

Every edge of K has length at least 2rho: the altitude from one endpoint to its opposite facet is a width of K and is at least 2rho; the edge is at least that altitude.

Call a K vertex v delta-unstable when `v·(w−v)<−delta` for every other K vertex w. Suppose at most one is delta-unstable. Every other vertex has an arrow with shadow at least −delta. Along that arrow,

    |w|^2−|v|^2≥4rho^2−2delta>0.

Thus the arrows form a tree to one root, necessarily the maximum-radius vertex a. Let R_K=|a|≥rho.

For a path x0,...,xd with shadows D_i=x_i·(x_{i−1}−x_i)≥−delta, exact positive-semidefinite quadratic identities give

    x0·xd≥−b_d |x0|^2−e_d delta,
    (b_1,b_2,b_3)=(0,1/8,1/4),
    (e_1,e_2,e_3)=(1,5/2,7/2).

These identities hold coordinatewise and hence for vectors. Their scalar remainders are

    x0 x1−D1=x1^2,
    x0 x2+x0^2/8−D1/2−2D2=(x0−2x1+4x2)^2/8,
    x0 x3+x0^2/4−D1/2−D2−2D3
      =[(x0−x1+2x3)^2+(x1−2x2+2x3)^2]/4.

For every rooted four-vertex tree, the sum of the three b-depths is at most 3/8, and the sum of their e-depths is at most 7. The six increasing-parent arrays exhaust these cases and are checked exactly by the recovery source. Since `4g(K)` is the sum of the four tetrahedron vertices,

    4a·g(K)≥(5/8)R_K^2−7delta.

But (C) gives `4a·g(K)<8epsilon_T`, whereas the exact constants satisfy

    8epsilon_T+7delta < 5rho^2/8,
    5rho^2/8−7delta = 137/7056000.

Contradiction. K has at least two delta-unstable vertices.

### 3.3 Both local maxima persist in the actual P

Fix one such vertex v. For z∈K, writing z as a convex combination of v and the opposite triangle yields

    v·(z−v)≤−(delta/2)|z−v|.

For x∈P at distance s=delta/2 from v, choose z∈K with |x−z|≤eta. Since |v|≤1,

    |x|^2−|v|^2
      ≤−delta s+s^2+(2+delta)eta
      ≤−delta^2/4+3eta
      =−delta^2/16<0.

The norm maximum on `P∩closed Ball(v,delta/2)` therefore occurs in the open ball. A local maximum of this strictly convex quadratic on a polytope is an actual vertex. Every incident-edge derivative is strictly negative: a zero derivative would make squared norm increase quadratically along that edge. It is consequently a strict unstable vertex of P.

The two balls are disjoint because distinct tetrahedron vertices are separated by at least 2rho>delta. P therefore has at least two strict unstable vertices, contradicting the target. This proves the theorem, including alpha=epsilon_T.

No genericity of the remaining P features, minimum nonroot escape margin, chosen escape-tree branch, or bounded raw-chart metric was imposed. A flat K has zero volume and is already outside the forbidden saturation region. Approaching flatness or arbitrarily singular raw affine coordinates does not leave a hole in the proof.

### 3.4 Actual reciprocal-trace consequence

For every pair of edge-adjacent triangular maximal facets in a strict110 body,

    T_ij=T_ji=v_ij<1−epsilon_T,
    Lambda_ij Lambda_ji<(1−epsilon_T)^2.                (D)

Thus the complete physical domain `Lambda_ij Lambda_ji≥(1−epsilon_T)^2` for such a pair is excluded. Equation (D) is not asserted unconditionally: it uses both the actual centroid and the unique unstable pole through (A), as well as actual primal instability in the persistence argument. It does not repair the false unconditional cycle-product or P0 proposals.

## 4. New root-closed four/five-vertex core sectors

Let u be P's unique unstable vertex and let W be four or five actual vertices, including u. Say W is root-closed when every vertex in W\{u} has a weak escape toward another member of W. Strict norm increase then gives a tree terminating at u. True-edge arrows suffice, but are not necessary: a direction toward any retained vertex is legitimate. Assume K=conv(W) has positive volume.

Then the following entire continuous mechanical sectors are impossible:

    |W|=4 and Vol(K)/V≥32/37;
    |W|=5 and Vol(K)/V≥1024/1095.                     (E)

The proof uses the same body's actual mass. Coning K from u gives

    4g(K)=u+sum_{i∈W\{u}} lambda_i v_i,
    0≤lambda_i≤1,  sum lambda_i=3.

Here lambda_i is an actual tetrahedral incidence probability, not a free substitute for the centroid. For four vertices the path bounds above give `|g(K)|≥5|u|/32`.

For five vertices add the exact depth-four bound b4=89/256. In the quadratic

    Q=b4 x0^2+x0 x4−sum_{i=1}^4 mu_i(x_i x_{i−1}−x_i^2),
    mu=(34,52,79,121)/64,

the five leading principal minors are

    89/256,
    935/8192,
    9269/262144,
    22673/134217728,
    4415/8589934592.

They are positive, so Q is positive definite. Over all 24 increasing-parent arrays on five vertices, the sum of the three largest b-depths is at most 185/256. Thus `|g(K)|≥71|u|/1024`.

Since u is also the global radius maximum of P, the centroid of any positive-volume removed part has norm strictly less than |u|. The exact partition

    (1−alpha)g(K)+alpha g(P\K)=0

therefore forces `alpha>gamma/(1+gamma)`, giving respectively **5/37** and **71/1095**. This proves (E) with its equality boundaries excluded.

For an edge-adjacent triangular pair, root closure strengthens (D) to `v_ij<32/37`. For a one-common-vertex triangular pair it gives

    v_ij<1024/1095,
    Lambda_ij Lambda_ji
      <(1024/1095−t_ij/2)^2−s_ij^2.                 (F)

The actual outer-tetrahedron and skew losses are retained. The t_ij=0 stratum is explicitly allowed. If u is outside W, or an escape must leave W, (E) is not available. That complement is not silently discarded.

## 5. New uniform actual ear-volume gap at nine vertices

This section additionally uses the journal's quantitative eight-vertex theorem and its already proved geometric corollaries. They are inherited inputs, not new certificates or fresh replays here. For a nine-vertex own-centred strict110 P with R=1 they give

    N=13827953664,
    pair distances>1/N,
    dist(v,conv(other vertices))>1/(8N^3),
    every three-vertex triangle area>1/(16N^4).

For the unique unstable root the distance bound improves to 1/(2N^2). The proofs permit weak nonroot escapes; the old C30 label does not restrict these nine-vertex lemmas to E=15. Their geometric premises also hold at C32.

**New conversion to actual volume.** Put

    epsilon=1/(165888 N^7),
    epsilon_u=1/(41472 N^6).

For every actual vertex v,

    1−Vol(conv(other vertices))/V>epsilon,             (G)

and for the unique unstable root the left side is greater than epsilon_u.

Proof: denote the deletion hull by K and its missing fraction by alpha. A lower-dimensional K has alpha=1. Otherwise suppose alpha≤epsilon. By (B) and the exact inequality `64epsilon≤(1/27)^3`, K contains the radius-r/2 ball, where r≥1/27. Write eta0=1/(8N^3). The deleted vertex is at distance greater than eta0 from K. Its Minkowski gauge t relative to K satisfies t−1>eta0, because the point v/t lies in K and |v|≤1. Some facet of K therefore sees v at height greater than eta0 r/2. A triangle in that facet has three actual P vertices and area greater than 1/(16N^4). The tetrahedron on that triangle and v lies inside P and outside K. Using V≤8 gives

    alpha > [1/(16N^4)] eta0 r/48
          ≥1/(165888 N^7)=epsilon,

a contradiction. Substituting the root distance 1/(2N^2) gives epsilon_u; its required Hausdorff inequality also holds. This proof does not require that deleting v preserve an escape tree.

Consequently, whenever a facet pair omits an actual vertex,

    v_ij<1−epsilon,
    Lambda_ij Lambda_ji<(1−epsilon)^2.                (H)

Use epsilon_u when the pair omits u. For one-vertex triangular pairs, the stronger same-body version retains the loss:

    Lambda_ij Lambda_ji<(1−epsilon−t_ij/2)^2−s_ij^2.

This closes the possibility of saturation along a mechanically valid nine-vertex sequence, though the constant is very small. It does not supply the missing finite-type elimination.

The separate eligible-leaf estimate **alpha_v>1/7169** is already in the journal and is not claimed new. It requires that the retained full-dimensional hull inherit escape to the retained root.

## 6. A fully reconstructed physical C32 family and explicit excluded sectors

The following is a proper two-parameter family of canonical **type139**, not a parametrization of that type's entire realization space. Take a,b>0 and the nine raw column vectors

    0=(0,0,0)
    1=(a,0,0)
    2=(b,1,0)
    3=(0,1,0)
    4=(−1,1/2,0)
    5=(0,0,1)
    6=(−1/4,1/4,2/3)
    7=(−1/4,3/4,1/6)
    8=(−3/4,1/2,1/6).

Its complete outward facet cycles, indexed 0 through 8, are

    (0,4,3,2,1), (0,1,5), (0,5,4),
    (1,2,5), (2,3,5), (3,4,8,7),
    (3,7,6,5), (4,5,6,8), (6,7,8).

Its true edges are

    01,04,05,12,15,23,25,34,35,37,45,48,56,67,68,78.

Set L=96a+96b+103. Actual integration gives

    V=L/576,
    Mx=(a^2+ab+b^2−1)/24−41/9216,
    My=(2a+4b+3)/48+7/1152,
    Mz=(a+b+1)/24+7/1728,
    g=(Mx,My,Mz)/V.

The physical family is **A(P_raw−g)** for every nonsingular real A. Equivalently use every positive-definite metric A^t A on the centred raw vertices. No shape or metric sampling is used in the exclusions.

The local-to-canonical vertex permutation is `(5,8,7,4,2,6,3,1,0)` and the facet permutation is `(4,7,5,8,6,1,3,2,0)`. The canonical facets are

    (0,1,3), (0,2,4,1), (0,3,6,2),
    (1,4,6,3), (2,5,8,7,4), (2,6,5),
    (4,7,6), (5,6,8), (6,7,8).

The complete automorphism group consists of the identity and `(1,0,4,3,2,7,6,5,8)`. Taking the least image of each of the 81 ordered vertex/facet pairs generates all **45 joint-root orbits**; the recovery code performs that complete calculation. The canonical catalogue pin is `efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450930f704d`, 240929 bytes. Its type139 record, including combinatorial dual179, was checked against the freshly recovered accepted catalogue. No physical polarity quotient is used.

### Exact nine-ear table

All nine deletion hulls are reconstructed symbolically for the entire domain a,b>0. The exact missing fractions, in vertex order, are

    (48a,96a,96b,16b,28,32a+32b+36,1,1,1)/L.          (I)

The source checks every supporting triple, exact facet coplanarity, all polygon side signs, extremality, true-edge multiplicities, and volume/moment polynomials. A triple is rejected only with opposite signs proved uniformly for all positive a,b. These are whole-domain determinant sign certificates, not hulls guessed from finitely many parameter samples.

Combining (G) with (I) excludes, **for every affine metric and every root choice**, the entire tail

    a+b ≥ (epsilon^−1−103)/96.                        (J)

If the unique unstable root is one of 6,7,8, replace epsilon by epsilon_u. If any of 6,7,8 is an eligible nonroot escape leaf, the inherited leaf theorem gives the far stronger necessary condition

    a+b < 3533/48.                                   (K)

Equation (K) is a new application of an inherited leaf bound, not a new leaf theorem. Every numerator in (I), not just the last three, must also pass its applicable bound.

### All intersecting triangular pairs

The six such pairs have the following exact core-volume numerators over L:

    facets     core vertices       numerator
    (1,2)      {0,1,4,5}           48a
    (1,3)      {0,1,2,5}           96a
    (1,4)      {0,1,2,3,5}         96(a+b)
    (2,3)      {0,1,2,4,5}         96a+48b+96
    (2,4)      {0,2,3,4,5}         96b+96
    (3,4)      {1,2,3,5}           96b.

The three one-vertex pairs have t_ij=0 identically: their four noncommon vertices lie on the raw base plane. Thus this family includes, rather than excludes by genericity, precisely the troublesome flat-outer-tetrahedron stratum.

The new unconditional-in-metric tetrahedral theorem excludes

    a ≥ (epsilon_T^−1−1)(b+103/96),
    b ≥ (epsilon_T^−1−1)(a+103/96).                  (L)

For root-closed cores, the stronger exact exclusions are obtained by comparing every four-point numerator with `(32/37)L` and every five-point numerator with `(1024/1095)L`. For example,

    core {0,1,2,5}:   a ≥ (32/5)b+103/15,
    core {1,2,3,5}:   b ≥ (32/5)a+103/15,
    core {0,1,2,3,5}: a+b ≥ 3296/213.               (M)

These are full continuous mechanical sectors, not just selected centre or metric samples. The root-closure premise is essential.

For the preserved chain (1,3,4), the physical trace numerators satisfy

    V T_13=V T_31=a/6,
    V T_34=V T_43=b/6,
    V T_14=a/3,  V T_41=b/3,
    Lambda_14 Lambda_41=36864ab/L^2.

At a=b=t this tends to one as t→infinity, as already known unconditionally. Equations (J) and (I) now prove that its saturation tail cannot carry the strict own-centroid110 mechanics under **any** affine transformation. The asymmetrical tetrahedral saturation tails are excluded much earlier by (L). This is the actual continuous-domain advance over the preserved counterexample, not a new claim that the unconditioned family fails a universal cycle inequality.

## 7. Exact remaining complement and continuation

Let D_old mean the actual C32 realization domains remaining after previously accepted exclusions. The new surviving necessary domain is the intersection of D_old with: (D) for every edge-adjacent triangular pair; (G) for every vertex; (H) for every proper facet-pair union; and (E)/(F) whenever the corresponding actual root-closed core exists. These conditions retain all outer-tetrahedron and asymmetry losses. They do not assert feasibility of the intersection.

For the explicit type139 family, the complement of the displayed excluded sectors is specified exactly by a,b>0, all nine cap tests from (I), both strict reversals of (L), and the strict core-fraction tests for every applicable row of the six-pair table. Root-specific and eligible-leaf bounds apply only when their stated actual mechanical conditions hold. The remaining problem still quantifies over all positive-definite metrics and all 81 root labels subject to those stated tests; no unmentioned finite metric box is imposed. The other realizations of type139 are not represented by this family and are not excluded by its parameter formulas.

I did not prove that the remaining intersection is empty, nor that every possible escape tree supplies a root-closed heavy core. In particular, the distinction between an internal escape and an excursion through omitted vertices remains decisive. The new proof does not make I+Lambda P0, does not give an unconditional oriented-cycle product bound, and does not identify free-mass feasibility with a physical body.

The most useful continuation is to analyze those **forced excursions with actual incidence and moments**. In the family above, when a+b≥3533/48, none of 6,7,8 can be an eligible nonroot leaf. Their only external ports are 6−5, 7−3 and 8−4. For a root in {0,...,5}, a valid tree must therefore use this cap as a communicating transit component rather than a terminal ballast appendage. The unresolved task is to combine that forced transit with the actual pole root and the moderate-mass five-vertex cores. Another unconditional cycle-product inequality would not resolve this complement.

## 8. Complete deterministic recovery capsule

The executable source contains the full bivariate-polynomial hull reconstruction, all exact input rows and facet cycles, all nine deletion hulls, all six intersecting triangular-pair hulls and traces, the complete automorphism/root calculation, every small-tree array, the PSD matrices and all their principal minors, and all exact constants. No external file is needed to recover the new result. The analytical geometric proofs are Sections 3–5 above; the executable checks their finite algebra and the exact family, not an automatic proof of all remaining C32 realizations.

Reference environment actually executed: **CPython 3.13.5, standard library only, assertions enabled**. Two separate clean-directory executions were observed and their complete transcripts and reports compared byte-for-byte. This is reproducible exact execution, not independent mathematical peer review.

Save the complete code below as `recover_nova24_conditioned.py`, UTF-8/LF with final LF. Run

    python -S recover_nova24_conditioned.py

For a direct second execution of the recovered mathematical source, run

    python -S nova24_mass_gap.py

Pinned identities:

    recover_nova24_conditioned.py
      8952 bytes
      c41fc82286520380aeab1e7eb9afa5a17a5cddc7ff634c6f9eed2b1efec8e1d4
    whitespace-free base85(zlib-9) stream
      7895 bytes
      8934edfdde5a2c6918b5153a4fe4ff6e78c1d7e7b7e795afeddfc81831a1d876
    decoded nova24_mass_gap.py
      16221 bytes
      9d61305151df997c2515d4d96a268b5ed8ca45a257d11f1be89c67ba04e6fbc9
    nova24_mass_gap.json
      63296 bytes
      2e787b76337194b0d6f7a9eb27ab443897e7162fca81b8df5b5c9cf84adc5548
    full recovery transcript
      618 bytes
      f7b68bc5984b3186cbfc6c125bf2f88e337f60237ef76cf54204f58f0a37eb4b

Observed terminal output:


[Encoded source block omitted; the code in this passage is incomplete.]

    SOURCE 16221 9d61305151df997c2515d4d96a268b5ed8ca45a257d11f1be89c67ba04e6fbc9
    NOVA24_C32_MASS_GAP_PASS_NO_F10_OR_WHOLE_TYPE_CLAIM
    NOVA24_CONDITIONED_CORE_COMPLETE_RECOVERY_PASS

The following encoded stream is complete executable source, not a hash-only or download-dependent handoff.

```python
"""NOVA24 conditioned C32 recovery. CPython 3.13.5, standard library.
Run with assertions enabled: python -S recover_nova24_conditioned.py
Decodes the complete source; no parent files or downloads are required.
"""
from pathlib import Path
import base64,hashlib,subprocess,sys,zlib
assert __debug__
STREAM = r"""
c-o~qYjfMWj^F(&bk3dKNDiG?@-ueX87Fnx?B+Fz+wB>zuST}yM2Rf9lAJp2_P;LxQW7OQJ-c%=tu2uN2!J5*ApPf`e_r2w8Ch-n
tYz6(<Fikr>x;9|<>g=Y+0FHbi^;{!_4tE*HM+mIKaOtgFXmD0?DjQ%j6$t-WVVhvLoG?2&~;*03;cQP#IITu2CqZSNfIwk{U}T{
FLdUC=N{GWHsL^93-rdl7Dg`)47~zS`@vZstzT=S&<S2sf1$0N*bCDEka@5#+yB|TFwf>m)bIOecF(=sw0l?9b#311^_`~aIj+?;
7u{vA*Y22>wXm#Zdp>XXy1jnC?X|nkqTTh(PRpFPy<YpoF;7}8YkAVCT}N8ttk%Gs7RA~!_Phpiqb)rr@#lWvr>}(|nxAMZ$MueC
fByMrZ5c-^z;G5qMt`-A;#51A4S=Pc3m88I^e75)m_@Xj`=LX4Oj~>LYLkjLfv|ScN6=*kehaUnV-W>`S03*y+Jr#ACSM<&1W}px
ltf`oaIV?5>&-V0wq2{a-V&&UNvgjXgPI0^v6pV*Q2Y5y^OrCosrI6ILE>pY^(Jc?gL44<MQH0_ljshcOS}bl{Y9!f2E8pod(Z4e
^FwWZ1Ol%TUBVIU^m)b?M-N`AKeKbaX&8qud8Zr}VFsG(1@xq{wxHpYg%fx%ergPIo}ULV^;8|($;L*i&?h(#y$9ekN6RQROoO^t
eway?fk;^qac)ScO;D2l=dWCF-Dgh*+m;w8geQn+78vaH4fO~W`G?Q!=`hF?rOS6iDr{SSEzK9mu1dZrNiJtB*{t+!B1ih6vP{fw
lL54ntUuV+P|5!w0*>pJ^^$I2spy2UWv_-HCFJ_yuL)LYE7{EVVG33M4XV&|TE!L9wuO#D0!N^@QCgWllpN{&eyBwpC8|wJY{@3^
F*RpwKDA~B6R#G&nlr;-rRh^K2&9=~G$n!GU^FFBrVI%LB$uv7(y>J$pAcBEj~xPV9VLG1zrX|)kaO60;9Y|)8i&-^M=wsW@xV}w
_s!ZrwDF4vJ9Zd_KfE{s3c+g_t$ZiYQZGqiSDe2VWDVQ^lQf2P9~8}`Uf}P2^GFy?s;`;D&vnyabNVW47pF#F)SY_Wug~lCCuIpO
aEjKMB}>aEqA)1ffUT%PC5alW>!`x|0#w~VeZv!Iw1L{hu4cIlw0np%m3NugWy-GFi2u}0vHh9Guc3CzaXU2Sd+jTqN_%$JI&G)0
d<wHf)~2|90tKdgo2BoD3G$iDGIA(Wnuy-Oj<&(_FN?JdM9CXkS$Ee^kn&b5@0`tQUqLRekC@o^VX*AM7;0ZZ2V6guO{UUU`zsR?
CUmQ;xj6bR-rxb>zs_oxHxM$|=cBXnJ=Z~$Hfu2p#UWuk^xZ+;kTrS-f$+PuA~fWm^;r-4Tdc>r1lb16F6+Zn7ux#3*xBg%hJqAj
L=zN*qgX&ejN1Y%i$-k2Q>!`_jR(Boc*L2Nj|U^ecXiY+<GacDD?~!KT$fl3aauH;HDqNXdXWM`bdf87X(G#$(dEs@&tv=k(}*8<
%emQf+TBji>7SSj*K94j%dX|lPuga;J$KvlR<qghPMUpp(djsj*YCOWcBgsLYA$=twtFBQ`Rf9v$9EGJ%JmS2JfE|*n58w&Q7ATd
H;&eP<!trX2_HNil=AGo^1xZmT}OK!IP*jgL-4+a0C%=t!l%!|&Ct|KH1sjge{duxJarViUd$7SKs=WiQt0{v!O~w-e+IM*YDiv=
L`xi2GHwIxS#gc9*g3-G4cQhA<ep|zXVxIH&djJo%kykHmo0Nx`#Uo(kQ5M!q>vH(1QDOkhL1jc<}NewzOiVNBImkJ0<$0j1EI(1
V9<bV`_VTlp5I4!KrMUw?~i`qX@M8&K+$+_()LUWfcI$wJP3UQMc;VGn*$AAkJiyzH%er%)mg8-5R@)@z$ADOO_7<yN1wjMREkIt
M+6Xqb9{n{l2|bpz69O&*C{~2mN8@EsW}73RCHLS4uS8}u8&S>5rZun?|@@~IEp>+E{P|(e&X2Xhpx9p4@-;~L*y8#Jq>1u_&s=%
9B=)Ehu#)K#{CAEyCt$%4Bv|uh}(o6i;)xmA>?KS2?qc?3U(W2KFvOJa3n9>ti0GsJz}$%y*V)p!I^3NTc*ufX~xNkL34S=e{d1M
sCu5GCY?gN^3@QmG32^D-*Of)T>eoK_(v&t6YC8*6Z^#DCJ1P<1xw2WBEca5KS3_xxxA^!4y%vYS27e@&n-m-VaZsYkZV5|;#s~H
j3=;%plO5>;#&qmLw>{IV1z=4Qb;F!)sw_v+JOjBmeD3|L~&yk#U2Rmhqw~gupS>hXn??E2~sv(f8~V<u<Zm#2RTW|ia=EyN#-g`
#P|uV&%{t+!F<ZFXitgp1_D@>pihffpqJ-9)AS)Xhu~jRi2OVi-GS-BIZaA)T48VidZ*Ahq{JmdNAn%zI@?R=x7;tCg(rQ+H!&eB
$pU4Zc!13^G!-j3O1u<o%h?2}jx?AwReXjC7p`dutwa<aXkg(W06Pou#I$=0F7sGj#`*$KU!pxNr}}fY+?GbZsFgn&0tcYctJ{UZ
%Y2&96mYM5iy{{0{HOJcCNSF=8~ETYj6*_4x&UP5OXWq{t+FgY>`;}q5R-B;YT9e&`AlJWTThMM%`EFMc7qtfPP(&dLtL~1{v`@%
#jhe*9BIP!pTC$U{ukMMp}(>Ndny!ZGNDSazp{Z-NX}{X7s`jpYvSZR(Z``Vt8nk~BAPFCAiI=e!UGe#rkjPcWynk*%v0qvQ<Ftp
E-qWkn7F-PeQ#)#;wDOfWfF{OR>_9)83H~_`!5wn#6qA?=D82>ER7m$iU9_=7mfmEGGzSkun4(XvRPww#}6NDkq9OBcRzi!)9;bJ
34LI9Wuv#i*3bj)5}xfj-~v8zasWaxVkS>e6lE!39<z+2AFy|NDf=`%AifV~xG;A6m2e-(T#Ct}525xEJAnvVJfGromR6WeG|4a0
6<*S`bb8QVyV`P*5R0yYB2M9mjYMiZVy8f>$ed5%Jx^VXVwz>!x!yL}iDi=AT)lFI#a))Ig5!chOA>AO6{0<6njMR1{@71*RN`xw
Euhe|`pO)D#)U~7%sBr-`w%oqlfX9pYRj%(*%dhY597-*mSyiTL|r&*2vib`Q}bOZn_{s>AJy6Si<mTn!oA7=gTF}IUdYK2O8&wg
3(gFhtGz2gu3*Vc7L&@>oZ+mU)`#l_9!4K84Ef`a43KRZbVacpfz!7yIhHoO?V3#41_+Qen=qIY_J+OfETXIrOhHZpsDB5lI+rw!
Eh{&MuCa?#Nt~63S?wR%<k7=jd5xlK>llI-&qXb1DHg;rYQb<Al>!qTV2~3pM9~FYc|)#sir+NEeTZpuKg!G|n|)qV5z}QmD>cJT
@DFXYNH<QPIm@LVdJR8(abn+rQ0mn7pR`>2!iA>5e2U!<!0O`B0i!V+twvjvd1B|geOgQy6>wyH$(0QPBE8{5so`lSBU#FP<N>~0
qBHg!5$&j<=2B)QOEo81%8W!bX5|lQk57U~wvB(CJ|GmsZxc!2gM|->mAOl`#s+-k;~?hZsaUjC4Il;1tF0|&;wCB$Rl2daNMHeH
mqeQgXEyvdBupZqj@Nn{xUDdEngcH&#1^{-RaQi;#u#Qs2fgZcRb4O@{?N$_4VtL<W<GIN`L!iqF%<iiA>-uj6Oio_B$p&}6~qd-
IyC$<2mGiH-LQ}rJ}kF|r$Mmff=^}G6m0Mjm!0;6$wecMAmokWxer?N*0Gns3UzR^OY-H1;dbs7^`byDeVG+8A{uuARH<D}^Rf}F
lUXS|5&77%oQsw{FD^q0Eg+(<)L2ER@v|CD`xH(4<!D+7|B|YIkg+qwiI66Uu__`MLl@GeDOPm}Pt=1wibp+T*Wb))&L+(r)&o_1
l@qWcKpEtv1qhL03}F5bj^Fq++a+uaO1Tvv{w(zVP??iL=88DK_60muk<|hf2$T7>hur8%L_W=zk0@gHsGw-FtUyX7PG|#Fz$gh1
{N!&(t}UIcE=x$Vp7OS&Z;L8=Xa<nqSq)7-4^w|)i3X@`W)K5lp@e|hV}6PPC~WCS`kPWnk!PA&%dcEBXizi`EQ@vrSLQ_s8N82<
@!JMmkuO%6NbZxN7JA>&&o#t`gZ>t4N_fIbjutRrL4F+F@}Al44@dX6<Fg63dbMjVp6k6j^wxFr&}`RbQ{Bq>x#rw#^{w7Xr`7GY
YY;`R=<I@B8$&MzCxi|4dh5796i!LJw~x*4FeX5&2O$asCirZ2JN<sYeqFEk0DYa<C@S@|&34bij&43QB5@>Ihk@$xF@&pqwNoGq
2wjeA9a}~Yitz=65TFOw7w6LuY4{K@Sam@6gDCu`ZXUM`?H$+RV~c5+G++sH8AJ|d6B^A#zMpm5i1&`iATPzBqJj7jtyS*c!^8U~
!RCM{EzHG<Q42h0$@ACYGb|H_n+<Hv2vOVnbKUAOh{(XWSAOtnFE%L$&VghDQ-<S{Zq|b%DBbj4g+clm3_j=ma?C0iu-NLfT1?S?
!N>c`!0#*A@0<CWPxVVI5u9{LAMpCcK-$nC0%r-Q9I6}>P;s<UMEQV;c><^f%%(|4Ko)r6ll-yY??}g%g_qveS)_D#ps~RF3QO>I
(2Tqw^PbyCRv1;H|Aqw*CUcY>FT(!ohp>|LmE74@e41}Y=L}DLN=H7c*)XJtZ3R(5NT#n`11J`LsBDyLQOw;<L7uTl1iST0oDUf6
Itsl~d2Nk>GPVw+d&6_V62Kq)d9a$UXKaNx4e*2ED>2uAk6KZN#ZLH#U3LCrw^lEiIy6~WsdA)TvUvQXR;?C1?Vu9u)2zYMIt}?$
y3>F>i8EW6FMH)coW0fOEO4?J5c<XULv#3zPp2p|4P~qPo$YBN{BICT!9PA9(i5Hsh~3J726%(UtU)RNelLd`Fg#OhJ>O6!9}vF-
5g)1eAmI07Ybbi4g<e%jztw8Dqsb@x6b-s5&U7g->nrD*{S#(&FlZ#u%h46rb#Rq*hAh6tk)~y+Z)Vn{Ob7I~+N?`dJC=OtoyZ5%
GVuupBE2sjy~T4Li$EflKC0EOjuibHS7%8`GbQL5%NUmLhFlomgjQi$K{myw>KdC)zX{VQ4Ch`6XYR{kV0B4>Z9()#t@k@Mzsv;K
vr$U2(3J~TjQ6tK?=OYC;DrbKzyy@^FhcT!MD8)*r(MiM7q~9x^=<Q?*5S5U-@*>FS!rN2wqO5X`$t4VQFJB$$I<DN&3Rd=5WuHC
x-!sRMZxU1B|O0>|HfdWvoYUZ_-iMy<upjy<f#blhISfz5YuK$9h_r!<cA<He&XXn>OkFWaC+CUKZoVr0odbsl_1=iJ-;-2#sDC}
08sQPKFkiy5=szJ0WS;M3(f2cdyybyL*kr`PvVVNwjM8zIbFEG4^@>&Ox&;7Pf}dHc;m2<CQw|^lV=BOgXI&-(r9g`kDyo^Wuftf
P}4z64*L6P1Pq((2H1~cTQvu0fmBrNEpOGS#S9q(Iemw))?^`^8gTo|NT5`;Nt>(2&^CsXPN}6+3STFfV0ZJwf=LIxemhTDovofu
56U_?m=#reLdUxrMYthx-WGcYzxRJ1u0z9_{SIxhwU2FxiyC5l<G4Ni*b(m;0JPQ4K7&d=wvQob{s`KD*AD;Kq1Qqc`o}i=*kK5Z
9~}|0bf{nkTP_5{O-pRUtkuh#PGs2fS(L4{)JtRM(S!X&Mkd}Ca&e6B2XeQ`!+ewmYf?^rMHJ$i<x%bK(~a<CePj4xd^s7>+exzt
LBja<-kyvnoZ2DyhRC^P^|}E0Y4o|&WkHu&L}?kK2<v+gzFVDsx8HB>{N*V9dXAJ4S3>5j>7C3O8o+ke*RI10u+XsT#ElH8>G_>i
S0M8-4toOhT}R>`_cIvLF76bx>iM|2oVlqsil)N?kn^J5>{j&gUXA>zP&7I%m5Q)Xgw3aCvN^9G)s*_t=ybP&v{M`tWOf0I5|{|e
!QwsF#>Iot{5hR6K)%-?qdeA6x^;TWYhZhja6MWlU1piBGS$(kodnU^<APq>IL6N^2-arf1?+$2(cAgx?Y*Pt#A$fYQ68-Cr7egv
vqK9=oQhL#f_H);n_D}6tVK)B5k+26yWIp%Oy_#p0s^1?{V@tWndBVRCU+O3>yMXX`|Rd!e4j-_K6~1UFS5Hpzbi{+E)wfru-jYN
h1qDeibATbl&izWzgOF`-8#D%Oqk{3&I=|uc)nIDaP1-fKYNHvza|exGExw^ZC294ltYi=%wz69@qI<_;rz+p>3Cv(E(Bc@AtBIF
45}x<NS7lGt_(X2{FR?_VMew5pudV+B3*<L5p0wBbu83CE@VSOR|yqWTEdlucJZtf+eL#_?X2zf;RQmgf*@+V6&9$149Z}ji@cPp
&IF_`idH&=U$)&+d?IX~i<_mn!DJ5%cNbe8J=OBV9B32c?H)xzL$&M-)H8;28W2zbc<$DsP!i;n_^68;T(`f%4G2fgen`Mc#9|Yi
>ajSD#dAOg&%fjGK$huZa{MLL!0tH}_e4eZq@1EbN=1c#^)yYiwX?ROx_?q!IHg;u?DvPi%E2jODyVIVsvg^^fV#NNs-7axMBwg)
i^%o#ZBZeHu#RGc1>O%oH?lH8lE(Vh*b9UfQV#2}%B+Aqi;DzCk$-KC>a89cWIDxLQ#jN@X5-3TX1N5nmHRH`d;C(K7el?zpQHTR
%fF808OdTU@3c%w&?%K2wzb&9n*`#w8+Z(o`sph__<#Ne=zz)8jxvCQ-~B{Kg8EsJ*H(+XHm*i*i@*KJ>V$oR6|hc%=a=?8+Jr8*
dV<t7zozs~;<~<2ioFb?DCS=3FcG+mgG(FBr?QVu^F&@;;N!7#w)ip{>x6Ak*K@!ZD|Rms^$CL6Ees``73-QX2|-3sOx+q>FGw8`
feJcm=O<^AxKX@ZQe>Zi&vx^`vP8uXW5@M335Q5fkP*oXF(C5qq9B-XB_k(Q;mx{C8<g*Gi0G+9nIhTI5%kq<3`dc_;lkWQN=s=$
6|A!ltW&iRFYq6HRK2LN<_g4DChr-fP7pn8JUe-GAZg*H`_*ibo%Px2D@0dj>qKdCH+g&SBqNt~N}o|VC}BaQbSlvV%YzZn&<c#W
I0Iw^O^x{(A9FTow2I<2#9*t0(+LV4HVPxF95Zq%&gU!5Sz!&ycB7T!hp^_}H<>nn-yCXQ_6rW!A4Ie#PWK@-To1EYF#3+iabX%q
zAKkx^17NwfxobG-}sf`9ZKO8KQX$Xf%cB?3D0kFWI9t;1neUbR=2<t@k>_fQha50D<NNjYVc|o(W+3ijnOPvT*-^cMUt&;1mVI@
;Un1?#}DSXPY%i})&S%vBI~HMLy{trjDjc7atu15EYy_|_|kUl2T#Q6_S{CdrG({E^H?rz@rw=!(ZN|k3Q#l~v$qF0J;MR!#Q@H~
FhC`D$Orj55%y&z?5#v(&sZRYI@WKc`B%ppomJ$b0dPpZC$$s!R7oInvDb0rZr~+1%<83qR=1DE;<xZrTSuHrc9{c9u9Rs`9X}|s
Sez_XkO&gwAsPJ8?%F-O&nu@-Z{R@eVtXLQTJD)u^z5)opoiXfn=(MVyiwYD=_TP!whv0#tV*y%_8ceOY@(uGJeQw4kgza}D4Z1d
3?U(*CZp!U?#*@lf$EXFS*;UYhAkpAfshYA?Pu>bp?W6s>2egejKhQf4iAhY32oHycd`0G^*6*w7ofhQFR|yZ;P7-D(5TV%EB)a9
udCCW%ZoD`0v!AH<{rYEFJpTIVg31MX!(R6qw5d$^~Lqr&Ne-2zPE271Ukqmjm{>Y!4rJBx%_+u`_uS(a(8nf5zj`jG?9$hzdm1%
?%)v|fqn4-0AbK^m0aO;CV$<IZSY#eV!LDi$IZp{#J;<^nb<dXrx%kd=J+eHVpDbZ_WlEKayPj+2TGH%-~q{W?b}NT9Y9m}SNJ};
8}D#%cXRsreu6v7-RRT!!yT}KyDs5hK_e(_{PhgTphh4xyq}D&cbIuIepIMTMi-ZF61W@R-rP+N=&mu%9Fsq4J`&DeG#)*ATi1W^
AYXuFDTx=H%)y4B1x(g9jv&@^<@^_OfAjh7Y%E9v$_{00D-)K8YJ8l9!N|3JePf@4&EMSF|MlqxycA8{+2!cs3IzIJ#uA3s
"""
b=''.join(STREAM.split()).encode('ascii')
assert len(b)==7895 and hashlib.sha256(b).hexdigest()=='8934edfdde5a2c6918b5153a4fe4ff6e78c1d7e7b7e795afeddfc81831a1d876'
s=zlib.decompress(base64.b85decode(b))
assert len(s)==16221 and hashlib.sha256(s).hexdigest()=='9d61305151df997c2515d4d96a268b5ed8ca45a257d11f1be89c67ba04e6fbc9'
Path('nova24_mass_gap.py').write_bytes(s)
subprocess.run([sys.executable,'-S','nova24_mass_gap.py'],check=True)
r=Path('nova24_mass_gap.json').read_bytes()
assert len(r)==63296 and hashlib.sha256(r).hexdigest()=='2e787b76337194b0d6f7a9eb27ab443897e7162fca81b8df5b5c9cf84adc5548'
print('NOVA24_CONDITIONED_CORE_COMPLETE_RECOVERY_PASS')
```

Supplementary convenience files: Markdown handoff (`NOVA24_C32_CONDITIONED_CORE_OBSTRUCTIONS_V1.md`), complete decoded source (`nova24_mass_gap.py`), exact report (`nova24_mass_gap.json`), and standalone recovery (`recover_nova24_conditioned.py`). The inline capsule above is sufficient without these files.
