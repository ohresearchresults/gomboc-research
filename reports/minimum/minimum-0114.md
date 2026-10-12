# minimum-0114

AI research report · 2026-09-19 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# FACET_MOMENT_AND_DEGREE4_VERTEX_OWN_COM_ACTUATORS_V1

## 1. New coverage: a complete large pure-B sector and a larger pure-A actuator class

**Every simple, uniformly filled convex 3-polytope at its own volume centroid, with exactly four simple B=EF weak points and at least nine facets, admits arbitrarily small genuine shape regularization preserving the entire face lattice and every original feature-labelled strict S/U/H, with no new strict or weak equilibrium.** No symmetry, stress-rank, covariance, radius, or zero-direction assumption is required. In particular, all rank-three positive-stress configurations in this sector are covered without testing the parent's full-cone criterion.

More generally, for any finite number k of simple B weak points, a simple body regularizes whenever one actual facet is neither endpoint of any of the k native polar contact edges. The numerical sufficient condition is F>2k. The deformation moves the other facet planes radially in pole coordinates and uses the remaining facet as an **exact actuator of the actual primal volume centroid**. The uniform centroid of the polar is never substituted.

On the pure-A side, a new universal local theorem proves that moving **any degree-four vertex with triangular incident faces** has an invertible derivative of the true volume centroid. This extends the accepted degree-three-ear actuator. Consequently a simplicial body with only simple A weak points regularizes whenever a vertex of degree three or four avoids all weak-edge endpoints. The same conclusion holds for a free vertex whose deleted cap has a planar polygonal base, of any degree. For exactly four A points, nine vertices of degree at most four suffice. One full combinatorial consequence is: **every realization of a combinatorial n-gonal bipyramid with n≥9 and only four simple A weak points regularizes**, regardless of central symmetry or geometric coplanarity of the equatorial vertices.

Two further results are useful outside regularization. An independently movable genuine facet has an SPD unnormalized first-moment derivative, with a local strictly convex potential. Two such distinct facets jointly control **volume and all three first moments**, with a universally rank-four Jacobian. These are physical moment-control lemmas, not free-center completion statements.

Two new exact noncentral bodies and two whole-interval arcs verify the mechanisms. Their four contact tensors have positive rank-three stress, but the physical source positions are not regular-tetrahedral up to similarity. An actual degree-four vertex Jacobian has positive determinant yet an indefinite symmetric part: treating it as SPD would be false. All 240 directed primitives are audited on 0<t≤1/65536, with true uniform centroids, actual hulls, and M=N=I.

**General all4 remains open.** The remaining simple pure-B slice has F≤8 and no free facet. The uncovered simplicial pure-A slice has no available free degree≤4 or planar-cap actuator; arbitrary nonplanar degree≥5 vertex controllability is not proved. Mixed A/B and ≤2VF configurations outside earlier accepted sectors are not closed here. There is no new weak110 seed, attaining improvement, or registry subtraction. The accepted bracket remains **34≤C_min≤622**, and the first open layer remains 10/17/9.

## 2. Source authority and the now-complete executable closure

The newly supplied research-journal(20260919-135400).md was read consecutively through all 1638 lines and EOF, including the complete shared notebook, branch memory and literal parent. It is 320120 bytes, SHA-256 `529e5f4db88a2729d34432aad7f9c9c01afc2a6e271f77c667437895df34829a`.

Literal parent `minimum-0110` was authenticated at 60946 bytes, SHA `ae32dbe1b0de3e635f0635f2d8a06648ad36bb63230458b6349bb32da96b9d3c`. Its accepted tetrahedral all16, noncentral full-cone criterion and degree-three-ear statements are inherited, not claimed as new. The parent's last explicit disclaimer, rather than its earlier completeness sentence, controls its displayed truncated DATA. Neither immutable predecessor has been rewritten.

The settled conversation actually supplies independently mounted full readable `four_vf_sectors.py` and `tetra_four.py`, and the complete working `recover_tetra.py`. These readable units and the complete decoder were read through EOF. The working decoder was executed into a fresh directory, and its two recovered files matched the independently mounted source bytes exactly. This does not infer a repair by removing suspicious padding from the malformed immutable text.

The older malformed capsule belongs to `minimum-0106`, SHA `c90a0c5de774f74977d6074f9db6ad9931d9b17f622ca157ac90b23d4b0c1bac`. Its immutable text is also unchanged. The final capsule in section11 now contains, in full, both unchanged predecessor source units, the complete new exact source, and the complete optional numerical exploration source. It restores the exact old code identities:

- `four_vf_sectors.py`:21083 bytes, SHA `795826c79faba62cd0c0e865d2716c715346a4d3d3ac779f1f745d0da224b873`.
- `tetra_four.py`:19131 bytes, SHA `8baa6cee6a1edb2a7d35d823543f5aeaf18b73f3cb27771e23227cb396eeb3e1`.

Thus the specifically omitted old/new executable closure is delivered literally here, not delegated to supplementary links. Exact source recovery is distinguished below from which old and new audits were executed in this continuation. The new notebook's later correction recording the coordinator's C622 replay is retained; this worker did not execute that replay or apply the new actuator to C622.

## 3. Physical conventions and preservation of complete packets

Use physical orthonormal coordinates with the actual uniform-volume centroid g(P)=0. A fixed change from an initial SPD metric to this Euclidean chart is permitted only with the corresponding reciprocal transformation of poles. All new deformations below can use the constant physical metric M=N=I.

A simple A point is a true vertex x whose radial supporting plane exposes exactly the true edge [x,y], with x·(y−x)=0 and all other local guards strict. A simple B point is equivalently a true native polar edge q→r with q·(r−q)=0 and the other local guards strict. Its physical location is q/|q|² in the relative interior of the corresponding primal edge.

For either native directed contact, write a·b=|a|²=r and |b|²=s. Then s−r=|b−a|²>0. Under radial motion a(t)=(1+tr)a, b(t)=(1+ts)b,

    a(t)·(b(t)−a(t)) = t r(s−r)(1+tr)>0.                 (1)

For simple A or B, this is the escape side that deletes the entire local physical weak point without creating the strict unstable/saddle, respectively stable/saddle pair. The other local conditions remain strict by continuity. Every other original feature either has all its required strict guards or has a strictly positive excluding guard. Select such a guard for each inactive feature; there are finitely many. Hence sufficiently small deformation preserves the exact old strict feature lists and creates no other equilibrium. Harmless zero primitives need not all be made nonzero.

The universal regularization theorems below concern pure simple A or pure simple B. They do not replace a VF packet by one chosen primitive. Complete VE/EF/VF grouping is nevertheless checked in the finite audits, including exclusion of unexpected packets.

## 4. A facet controls the actual uniform centroid; two facets also control volume

### 4.1 Exact derivative and its positivity

Let

    P(q)={x:q_j·x≤1 for all j},
    V=Vol(P), J=∫_P x dx, g=J/V.

Choose an actual facet a. Assume every vertex incident to that facet is simple. This makes its three pole coordinates independently movable in a neighborhood with the full lattice unchanged. Indeed, in the combinatorial polar every face incident to q_a is triangular; moving q_a changes only those triangles, while all strict nonincidences remain strict. This is a lattice argument, not a statement about polar mass. In a simple P every facet qualifies.

Define actual unnormalized surface moments

    H_a=(1/|q_a|)∫_{F_a} xx^T dA,
    m_a=(1/|q_a|)∫_{F_a} x dA.

Under q_a→q_a+εδq, the normal velocity on F_a is −δq·x/|q_a|. Other fixed planes have zero normal velocity; intersections of facets have area zero. Therefore exact first variation gives

    D_{q_a}J=−H_a,
    D_{q_a}V=−m_a^T,
    D_{q_a}g=−H_a/V                 when g=0.             (2)

These are derivatives of uniformly refilled actual bodies. The matrix H_a is SPD: a nonzero linear form c·x cannot vanish identically on a relatively open two-dimensional set in q_a·x=1, a plane not through the origin. Moreover

    H_a q_a=m_a.                                          (3)

Thus, for any sufficiently small analytic deformation of the other prescribed geometry that admits this independently movable facet, the analytic implicit-function theorem supplies a unique small q_a restoring **J=0 exactly**. The origin remains inside, the actual volume stays positive, and the true centroid is precisely zero. There is no chosen moving reference.

### 4.2 A local strictly convex potential

Keep the other inequalities fixed and put K=∩_{j≠a}{q_j·x≤1}, possibly unbounded. In a neighborhood of the original q_a,

    Φ(q)=∫_K (1−q·x)_+ dx,
    ∇Φ(q)=−J(P(q)), Hess Φ(q)=H_a(q)≻0.                  (4)

The integral is finite locally: boundedness of P means q is strictly positive on every nonzero recession direction of K, uniformly on the compact set of such unit directions in a sufficiently small neighborhood. The truncated regions are then uniformly bounded. Differentiation gives (4), either by coarea or by the fixed face-lattice integration chart. The own-centered pole is a locally unique minimizer. This supplies a true geometric actuator and local uniqueness, not a claim that an arbitrary reference is the centroid of an unchanged body.

### 4.3 Two genuine facets give rank four

Let a,b be distinct independently movable facets, both with simple incident vertices. The Jacobian of (V,J) with respect to their six pole coordinates is

    [ −m_a^T   −m_b^T ]
    [ −H_a     −H_b   ].                                 (5)

A left annihilator (λ,c) must satisfy H_a(c+λq_a)=0 and H_b(c+λq_b)=0. Positivity and q_a≠q_b force λ=0,c=0. Consequently (5) has rank four. Choose an invertible four-column minor and hold the other two controls fixed. The analytic implicit-function theorem permits local prescription of true volume and all three first moments, including constant volume and ownCOM0 together.

These lemmas also apply locally to a nonsimple body when the particular actuator facets have only simple vertices and the rest of the prescribed deformation genuinely preserves the lattice. They do not license arbitrary plane movements through nonsimple vertices. No C622 actuator-incidence test or compression was executed here.

## 5. Pure B theorem: all simple bodies with a free facet, hence every four-B body with F≥9

Suppose all weak physical points of a simple P are k simple B contacts. Let a be a facet whose pole is not an endpoint of any native contact edge. Prescribe

    q_j(t)=(1+t|q_j|²)q_j, j≠a.

By section4 choose the remaining q_a(t) analytically so that the uniformly filled primal intersection P_t has J(P_t)=0 exactly. Simplicity and strict supporting inequalities preserve the entire lattice. For every contact, both native endpoints follow the prescribed radial motion, so (1) holds exactly. Its physical B point is removed; section3 preserves every other strict or inactive feature. The deformation approaches the initial body as t→0.

There are at most 2k used pole endpoints. Thus F>2k guarantees an unused facet without any metric-stress computation. For k=4 this proves the announced **entire F≥9 slice**. For F≤8 the theorem still applies whenever a free facet exists; only the no-free-facet slice is left by this argument.

This result covers full-rank positive stresses regardless of whether their weighted direction sum vanishes. It does not assert that the finite controls below violate the parent's sufficient criterion; they do not. The new coverage is the universal free-facet theorem, whose hypotheses contain no stress-cone condition.

If a genuine simple weak110 seed with four B points is ever supplied, the accepted S1⇒F≥9 lower theorem puts it in this regularizable sector. No such seed is constructed here. The 10/17/9 first layer is nonsimple, so this observation does not settle that layer or improve the minimum.

## 6. Degree-four vertex controllability and the new pure-A classes

### 6.1 Deleting a genuine vertex gives a local visible cap

Let w be a degree-four vertex with triangular incident faces, and K=conv(all other vertices). K is full-dimensional unless the whole body is a pyramid over a planar neighbor polygon, treated below.

Every vertex p of a newly exposed visible facet of K is a neighbor of w in P. To prove this, take its supporting linear functional ℓ with ℓ(w)>max_Kℓ. At p there is a true incident edge along which ℓ increases: otherwise ℓ would attain its maximum over all P at p. Every original vertex except w lies in K, so the increasing neighbor must be w.

All four neighbors lie on the horizon of the visible patch. A vertex strictly inside that patch would disappear upon adding w, contradicting its being an original vertex of P. Hence with four neighbors the visible patch is either one planar quadrilateral, or exactly two triangles on four noncoplanar vertices. There is no arbitrary triangulation or inserted mechanical diagonal.

### 6.2 Noncoplanar degree four: exact determinant for every actual body

Label the two visible triangles (a,c,b) and (a,b,d), sharing ab. For the moment calculation, use the affine chart

    a=0, c=e1, d=e2, b=e3,
    w=(−u,−v,z), u,v>0, T=u+v.

This is a moment coordinate chart, **not** a mechanical normalization of contact data. K lies in x1,x2≥0 and contains the tetrahedron conv(0,e1,e2,e3). Let V_K>0, J_K=V_K g_K, and G_K=(g_K)1+(g_K)2. True apex-fan integration of the nonnegative affine function x1+x2 gives G_K≥1/4: its maximum on K is at least1, and each tetrahedron in a fan from a maximizing vertex has mean at least one quarter of that maximum.

The removed cap consists of two genuine tetrahedra. Thus

    V=V_K+T/6,
    J=J_K+[T w+(v,u,T)]/24.                              (6)

Differentiating g=J/V with respect to w gives the exact identity

    det D_w g = T(T+1){V_K[2T−1+4G_K]+T²/6}
                /{24³(V_K+T/6)^4}
              ≥ T²(T+1)(2V_K+T/6)
                /{24³(V_K+T/6)^4} >0.                    (7)

The source verifies the identity and the difference from the lower bound symbolically. The positive bound is analytic and uses the actual K centroid, not a fitted mass. Under any affine chart change D_wg is conjugated, so its determinant is unchanged. Equation(7) therefore proves invertibility for **every** actual noncoplanar degree-four triangular star, with no symmetry or shape restriction.

There is also an explicit local inverse. Suppose other vertices have moved, re-form this chart, integrate the new actual K, and let c be the chart image of the fixed desired physical origin. Write J_K=(j1,j2,j3), c_s=c1+c2. Solve

    T²+(4c_s−1)T+24(V_K c_s−j1−j2)=0,
    T=[1−4c_s+sqrt((4c_s−1)²−96(V_K c_s−j1−j2))]/2,
    u=[T+24j1−24V_K c1−4T c1]/(T+1),
    v=[T+24j2−24V_K c2−4T c2]/(T+1),
    z=24[(V_K+T/6)c3−j3]/T−1.                            (8)

The displayed square-root branch is the initial one: at the original center, (7) implies 2T+4c_s−1>0. Hence the discriminant stays positive locally, u,v stay positive and all support guards remain strict. Substitution in (6) gives J=Vc exactly. Transforming back gives the fixed physical ownCOM0, not an independently chosen moving reference.

### 6.3 Planar caps, including the inherited degree-three ear

If the neighbors lie on a planar polygonal base, the actual cap is a pyramid with base area A, plane n·x=h and height u=n·w−h>0. Let v=Au/3, and let c_T be its actual volume centroid. For full-dimensional K,

    D_wg=v I/(4V)+A(c_T−g)n^T/(3V),
    det D_wg=(v/(4V))³[2+4(h−n·g)/u]>0.                  (9)

The bracket is greater than1 because g is the positive volume mixture of the K centroid strictly behind the base and c_T at height h+u/4. If K is just the planar base, the whole body is a pyramid and D_wg=I/4. This includes the degree-three-ear result, and also planar neighbor caps of arbitrary degree. It does not establish arbitrary nonplanar degree≥5 vertex controllability.

### 6.4 Pure A regularization

Let P be simplicial, all its weak physical points simple A, and choose a free vertex w of degree three or four, or with the planar-cap property. Free means **not an endpoint of any weak A edge**. Prescribe radial motion (1+t|x_j|²)x_j for every other vertex. Sections6.2–6.3 and the implicit-function theorem, or explicit formula(8), choose w(t) with actual J=0 exactly. Each weak edge has both endpoints prescribed radially, so (1) gives its positive escape. All triangular facets and strict nonincidences remain, and section3 preserves the old strict feature lists without creating equilibria.

At most 2k vertices are used by k A contacts. Thus 2k+1 degree≤4 vertices guarantee a free one. For four contacts, nine such vertices suffice. A combinatorial n-gonal bipyramid has n degree-four equatorial vertices; for n≥9 this gives the claimed entire realization-class corollary, even when its equatorial vertices are not coplanar geometrically. These bipyramid graphs have no degree-three vertex, so this is not merely a relabelled application of the old ear theorem.

### 6.5 A genuine negative result: the vertex derivative need not be SPD

For the exact noncentral body Q below, the degree-four actuator w8 has

    D_wg = [[159/66472,0,255/33236],
            [0,159/66472,505/66472],
            [495/16618,−495/33236,426/8309]],
    det D_wg=2545749/146854156193024>0.

Yet for v=(−4,0,1), v^T(D_wg)v=−501/8309<0. Thus its symmetric part is indefinite. The facet SPD argument cannot be transplanted to vertex motion. This is an exact actual ownCOM countercontrol to that stronger architecture, **not** an obstruction to regularization: invertibility holds and is used successfully.

## 7. Two new actual noncentral four-point controls and complete arcs

### 7.1 Exact input; neither body is a tetrahedral normal form

Let the ordered eight-point list B be

    (1,1,1),(2/3,4/3,1),(1,−1,−1),(4/3,−2/3,−1),
    (−1,1,−1),(−4/3,2/3,−1),(−1,−1,1),(−2/3,−4/3,1).

Put

    O=[[0,−1,0],[1,0,0],[0,0,−1]],
    a=(1/50,1/100,6/5), C=diag(1,1,3/2),
    X=(C B0,...,C B7,Ca,COa,CO²a,CO³a), Q=conv X.

This formula includes all eight listed B points followed by the four displayed orbit points, in that order. The O-symmetry has no nonzero fixed vector, so both Q and its actual polar P=Q° have own uniform COM0. Both centers are independently checked by exact volume integration; neither body is centrally symmetric. The four A source positions in Q have squared mutual distances8 and13, so they are not regular-tetrahedral up to orthogonal similarity. The four source radii squared are17/4 and the four contact-edge lengths squared2/9.

All geometry, including P's full vertices and poles, is recovered from these literal rational inputs by exhaustive supporting triples. There is no missing coordinate table. The source computes all maximal faces, actual edges, volumes, covariances, strict lists and grouped physical weak points.

### 7.2 Q: genuine simplicial AAAA

Q has (V,E,F)=(12,30,20), C=60, volume8309/1125. Its maximal facet sets, in canonical order, are

    (0,1,3),(0,1,8),(0,3,7),(0,7,8),(1,3,4),
    (1,4,5),(1,5,6),(1,6,10),(1,8,10),(2,3,7),
    (2,3,11),(2,5,7),(2,5,11),(3,4,9),(3,9,11),
    (4,5,9),(5,6,7),(5,9,11),(6,7,10),(7,8,10).

Exactly four weak physical points are simple A, on0→1,2→3,4→5,6→7; exactly four of120 directed primitives vanish. Strict lists are

    S=[1,2,4,6,10,11,15,18],
    U=[1,3,5,7,8,9,10,11],
    H=[(0,3),(0,8),(1,4),(1,8),(2,7),(2,11),(3,11),
       (4,9),(5,6),(5,9),(6,10),(7,10),(8,10),(9,11)].

Thus strict8/8/14, not110. The four tensor rows have rank3 and sum zero; the four directions sum zero. Hence there is an all-affine-orders escape barrier, and the equal radii imply no positive initial global projective-affine first jet. No second-order or all-orders projective barrier is asserted for these new bodies. They satisfy the parent's zero-direction criterion; they are **not** counterexamples to it.

Vertex8 has neighbors0,1,7,10, which are noncoplanar. Deleting it exposes exactly triangles(0,1,10),(0,7,10). In the affine chart with origin X0 and columns X1−X0,X7−X0,X10−X0,

    w8=(−9/200,−3/200,1),
    V_K=16609/900,
    g_K=(41378451/13287200,40380417/13287200,−166189/33218).

The exact Jacobian and negative quadratic value in section6.5 are computed from this same actual Q.

### 7.3 P=Q°: genuine simple BBBB, with primal—not polar—moments

Uniformly fill the actual polar as a **new body**. Independently compute its own moments. It has (20,30,12), C=60, volume620762/492723, ownCOM0, strict8/8/14 and exactly four B weak points; four of120 directed primitives vanish. In the canonical facet and vertex order produced by the exact hull:

    S=[1,2,3,4,6,8,10,11],
    U=[1,2,4,6,10,11,15,18],
    H=[(0,2),(1,3),(1,8),(4,5),(6,16),(7,18),(8,19),
       (9,11),(10,12),(10,14),(13,15),(14,17),(15,17),(18,19)].

The four actual B points, with their canonical physical edge and facet labels, are `(−4/17,−4/17,6/17):E(16,18),F7`; `(−4/17,4/17,−6/17):E(5,15),F5`; `(4/17,−4/17,−6/17):E(9,10),F9`; `(4/17,4/17,6/17):E(0,1),F0`. Each paired edge/facet description is one physical point, not two.

The free input pole X8 is canonical primal facet3; input X9 is canonical facet11. Code resolves these labels by exact equality of pole coordinates, not by assuming input and hull order agree. For facet3, the actual H principal minors are

    322686570925/107160535700064,
    14395678296875/29400256488129421356,
    26921831513251953125/12907188676642128255004017708,

all positive. For free facets3 and11 the four-column minor with columns(0,1,2,3) in(5) equals

    −3339163146550944740179398388671875 /
     135547842791135518904824900266088870407864576 ≠0.

Full H matrices, surface moments and the four-by-six Jacobian are deterministically recovered. They use uniform P surface and volume moments, not those of Q.

### 7.4 Computed A arc: first-order actuator, exact recentering

The universal theorems above keep the raw COM exactly0 by a nonlinear analytic actuator. The following computational arcs instead use a **linear first-order actuator and then the exact full recentering**. Their raw g'(0)=0, but generally g(t)≠0 at higher order. This distinction is important.

For Q initially set velocities v_j=|X_j|²X_j and add e1/10 to v9, a free noncontact vertex. Let A_j=D_{X_j}g, computed from the actual triangular boundary:

    A_j=(1/(12V)) Σ_{F=(a,b,c)∋j}(a+b+c+X_j) n_F^T,
    n_F=((b−a)×(c−a))/2.

At COM0, ΣA_j=I and ΣA_jX_j=0, checked exactly. Replace

    v8=−A8⁻¹ Σ_{j≠8} A_j v_j, Y_j(t)=X_j+t v_j.

The uncompensated raw COM derivative is (159/664720,0,−99/66472), nonzero. The compensating velocity is

    v8=(−282586767/59300000,−551656767/118600000,43334097/5930000).

Now integrate the true uniformly filled hull Y(t), obtaining the full rational g(t), and use Y_j(t)−g(t). The source checks g'(0)=0 and

    [t²]g=(794806631/11815406400,
           471393732793/7012443698400,
           30368263989/66785178080) ≠0.

On the whole0<t≤1/65536, every old strict label stays unchanged, weak000, and each of the four A escapes has leading term(17/18)t. Metric M=N=I throughout. The asymmetric v9 change prevents an unused actuator hidden by the original O symmetry.

### 7.5 Computed B arc: genuine first moments of the refilled primal

Start from P and its input-order true poles q_j=X_j. Initially use pole velocities v_j=|q_j|²q_j, add e1/10 at input index9, and replace the input-index8 velocity by

    v8=−H8⁻¹ Σ_{j≠8} H_j v_j.                            (10)

Here H_j are actual P facet integrals. Reconstruct each true primal vertex from its three incident moving planes q_j+t v_j. The uncompensated raw COM derivative is

    (−407707635065/3307678182924192,
     −153483535295/945050909406912,
      53952330475/206729886432762) ≠0.

Equation(10) makes the actual derivative zero. The full rational uniform-primal g(t), including its nonzero second coefficient, is integrated and subtracted. The true centered poles are

    q_j^c(t)=(q_j+t v_j)/(1−(q_j+t v_j)·g(t)).

On the same whole interval, every original strict feature is retained, weak000, and every B escape has leading term(17/18)t. Again M=N=I. This is not a path evaluated at a chosen center and not a uniform-polar COM calculation.

## 8. Complete exact verification and a reusable denominator-clearing method

For each actual facet, triangulate only for integration. For an outward triangle a,b,c in q·x=1, let d=det(a,b,c)>0 and u=a+b+c. Exact contributions are

    H += d(uu^T+aa^T+bb^T+cc^T)/24,
    m += d u/6,  area/|q| += d/2.

The code checks Hq=m, ΣH=5VΣ_P and Σm=0 at ownCOM. A separate positive vertex fan verifies actual volume, first and second moments. Integration diagonals are not used as mechanical edges.

Large rational expressions in the B arc were the computational bottleneck. The final source retains exact common-denominator polynomial arithmetic. Write raw vertices v_i/R and true centroid U/S, with positive R,S normalized at0, and T_j=S−q_j·U. Centered vertices and poles are

    (S v_i−R U)/(RS),  S q_j/T_j.

The exact primal escape numerator is (S v_a−RU)·(v_b−v_a), with denominator R²S. The polar escape is

    S²[T_i(q_i·q_j)−T_j(q_i·q_i)]/(T_i² T_j).             (11)

After proving R,S,T_j>0 on the whole interval, signs reduce to complete rational-coefficient polynomial tests. No independent primal/dual metric, approximate center or sampled sign enters(11).

For a polynomial P(t)=Σ a_jt^j of degree n, Bernstein coefficients on[0,ε], ε=1/65536, are

    b_k=Σ_{j≤k} a_j ε^j binom(k,j)/binom(n,j).

All claimed signs have every b_k strictly positive. Initially zero escapes have their exact factor t removed first. The A arc has341 rational guard records,3533 positive numerator/denominator coefficients,maxdegree15. The B arc has371 polynomial guard records,8173 positive coefficients,maxdegree45. Together:712 guard records,1053 positive-polynomial checks,11706 positive Bernstein coefficients;240 true directed primitives,232 initially nonzero signs preserved and8 simple zero escapes made positive.

Both endpoints are additionally re-hulled from all supporting triples, re-integrated at their actual COM, and checked for the identical maximal-face/true-edge lattice and full physical census. The initial and endpoint audits group coincident feature descriptions into physical points and exclude VF or other weak points. These finite audits prove their continuum signs; the general theorems are proved independently in sections4–6.

## 9. Preserved negative searches and execution boundary

The exact negative Jacobian quadratic form in section6.5 is a genuine geometric finding. The optional numerical probes are a different evidence tier. Their complete source, exact seeds and all best checkpoint arrays are in the capsule; no floating result is promoted to an exclusion or general controllability theorem.

With twelve Gaussian/lognormal points per hull and exact stated NumPy/SciPy versions, the completed probes were:

- determinant:2000 hulls,seed92137,log-radius spread1.5;13927 vertex matrices,zero negative determinants,minimum approximately1.0166251894945952e−16;
- symmetric part:250 hulls,same seed/spread;1729 matrices,539 negative minimum eigenvalues,minimum approximately−0.4699535797825562;
- real eigenvalue:250 hulls,same seed/spread;1729 matrices,zero negative minimum real parts,minimum approximately6.922233378386598e−8;
- individual fan-cell reference:400 hulls,seed92138,spread1.2;19700 matrices,51 negative determinants,minimum approximately−0.0024056109866696803.

The last mode intentionally replaces the reference by an individual apex-tetrahedron centroid, **not the body's COM**. Its failure defeats that numerical per-cell positivity architecture only; it is not a physical ownCOM counterexample. No equilibrium census was asserted for the random hulls. Failure to find a negative ownCOM determinant is not proof for degree≥5.

Naive symbolic B-arc cancellation and several combined calls exceeded runtime limits. The final exact common-denominator source completed its original build and check for every part. The frozen source capsule was then decoded into an empty directory: cold builds of all three parts reproduced every byte; cold checks0 and1 completed. A further cold check2 reached its endpoint stage but timed out without a final PASS; it is **not** counted as an additional completed check2. The original frozen-source check2 did complete with the exact final marker. Cold assemble and verify completed and matched the original full report/stdout. No incomplete invocation is described as a completed audit.

The complete old predecessor suites were not rerun in full in this continuation. Their exact source bytes are now restored and delivered, while their previous execution reports retain their inherited status. There is no new peer review or proof-assistant certification claim, and no external literature theorem is needed for the new proofs.

## 10. Reconstruction, expected outputs, and scientific effect

Exact environment: CPython3.13.5, SymPy1.14.0, assertions enabled, PYTHONHASHSEED=0. The optional NONPROOF probes additionally use NumPy2.3.5,SciPy1.17.0 and OPENBLAS_NUM_THREADS=1. There is no RNG or numerical solver in the exact reconstruction.

Save the entire section11 source as `recover_actuators.py`, UTF-8/LF with one final LF. From an empty directory:

```bash
python -S recover_actuators.py recovered
cd recovered
export PYTHONHASHSEED=0
python actuator.py build 0
python actuator.py build 1
python actuator.py build 2
python actuator.py assemble
python actuator.py check 0
python actuator.py check 1
python actuator.py check 2
python actuator.py verify
```

`ACTUATOR_TRACE=1` optionally prints guard/stage boundaries without changing formulas or assertions. Its elapsed-time text is not a deterministic output pin. Each check recomputes its entire part; verify checks exact part pins and assembly, and is not a substitute for those computations. Optional numerical reproduction is `OPENBLAS_NUM_THREADS=1 python optional_probes.py > optional_probes.json`; floating portability beyond the stated environment is not asserted.

|File|Bytes|SHA-256|
|---|---:|---|
|four_vf_sectors.py|21083|795826c79faba62cd0c0e865d2716c715346a4d3d3ac779f1f745d0da224b873|
|tetra_four.py|19131|8baa6cee6a1edb2a7d35d823543f5aeaf18b73f3cb27771e23227cb396eeb3e1|
|actuator.py|16873|b5c7350caf717f347490732e0f75bab19672a182485a285233f9b5683a501333|
|optional_probes.py|2209|e26f0b17cb87bf0c925cc27515cb033d7c3f7794da442005ae8b1fbacab9690c|
|actuator_part_0.json|16659|1afd4e65206120bf6d0da0152659fc1854b5744f405ba80501589f48100d7f0c|
|actuator_part_1.json|573482|bf34d669742f2edbc75f7afe2a72416113dae010b4eeb0cde947a65e2f2c4852|
|actuator_part_2.json|23721011|e79f7b74d98a5910c9ef9bd3fdd6d52f2a5fa65fb6ab70f27f778329480523e1|
|actuator.json|24311230|df437cc2c9eca53311f27d836971937f5c6d30c35aa49a32dee553efdb5b0f02|
|assemble/verify stdout|488|5e19ad243283e0f63533492cc3dfd7094ff6227c83ec052011498a90ecf99832|
|optional_probes.json|4939|2aabcc04a4d4475ea75c1a5ac830780ae42020bb1ec424a2a673e1241c83fa5e|
|recover_actuators.py|27750|a1244fbec58b3842cc16b80c711df9007fbfa820b3f6b16df33175abeb99d934|

Each exact part prints `ACTUATOR_EXACT_PART_PASS k bytes SHA` with its table entry. Complete stable assemble/verify output is:

```text
TRUE_FACET_MOMENT_SPD_AND_TWO_FACET_RANK4_PASS
ALL_DEGREE4_TRIANGULAR_STARS_TRUE_COM_DETERMINANT_PASS
NONCENTRAL_A_B_TRUE_FIRST_ORDER_ACTUATORS_240_PRIMITIVES_PASS
STATS [{"guards":341,"maximum_degree":15,"positive_bernstein_coefficients":3533,"primitives":120},{"guards":371,"maximum_degree":45,"positive_bernstein_coefficients":8173,"primitives":120}]
actuator.json 24311230 df437cc2c9eca53311f27d836971937f5c6d30c35aa49a32dee553efdb5b0f02
FACET_MOMENT_AND_DEGREE4_VERTEX_RECOVERY_PASS
```

The original check2 marker and all cold output pins were actually observed. Byte comparison of recovered sources, all three cold-built parts, the complete report and stable stdout yielded `ACTUATORS_SOURCE_ONLY_COLD_BUILD_AND_REPORT_BYTE_PARITY_PASS`. This marker does not claim completion of the separately timed-out cold check2.

The recovered predecessor methods remain runnable without any further source: `four_vf_sectors.py build|check PART` for PART0..6, then assemble|verify; `tetra_four.py build|check PART` for PART0..3, then assemble|verify. Their exact terminal pins are embedded in their unchanged sources. Both immutable parent payloads keep their original identities and recorded display defects.

The most useful continuation is now the small no-free-facet simple-B slice and general nonplanar degree≥5 vertex moment controllability, with the exact degree-four proof and indefinite-symmetric-part control preventing the wrong SPD shortcut. The two-facet volume/first-moment actuator is also transferable to genuine local lattice-preserving compression charts when its incidence hypotheses have been checked. None of these implications supplies a new attaining body or changes the minimum bracket or any catalogue count.

## 11. Complete literal executable closure

The following decoder contains all four complete source units. Its JSON bundle is60504 bytes, SHA `9bc1997ded9307b29eb9839f7ef0f14617f84dd5c897f897902e664ca31d609f`; its LZMA stream is19344 bytes, SHA `fb147ef0b742ace1e0cf6a84d7c5d2716eeef1fa2eb34adfde5ec4229af4dbda`; Base64 has25792 characters, SHA `bb168403846b89fb4692e344bba7e2441ae6d0e0e9ae541dbd286bdef4d4ef4e`. The full literal stream is present, with no omitted helper or continuation-critical array.

```python
"""Complete immutable-predecessor and new centroid-actuator source closure.
Decoder: CPython3.13.5 standard library, assertions enabled.
python -S recover_actuators.py DIRECTORY
Exact proof units require SymPy1.14.0, PYTHONHASHSEED=0.
optional_probes.py additionally uses NumPy2.3.5/SciPy1.17.0; NONPROOF.
No old file, download, missing helper or external checkpoint is needed.
"""
from pathlib import Path
import base64,hashlib,json,lzma,sys
assert __debug__ and len(sys.argv)==2
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
SOURCE_PINS={'four_vf_sectors.py': [21083, '795826c79faba62cd0c0e865d2716c715346a4d3d3ac779f1f745d0da224b873'], 'tetra_four.py': [19131, '8baa6cee6a1edb2a7d35d823543f5aeaf18b73f3cb27771e23227cb396eeb3e1'], 'actuator.py': [16873, 'b5c7350caf717f347490732e0f75bab19672a182485a285233f9b5683a501333'], 'optional_probes.py': [2209, 'e26f0b17cb87bf0c925cc27515cb033d7c3f7794da442005ae8b1fbacab9690c']}
RAW_PIN=[60504, '9bc1997ded9307b29eb9839f7ef0f14617f84dd5c897f897902e664ca31d609f']
PACK_PIN=[19344, 'fb147ef0b742ace1e0cf6a84d7c5d2716eeef1fa2eb34adfde5ec4229af4dbda']
DATA="""
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
"""
encoded=''.join(DATA.split())
assert len(encoded)==25792 and '=' not in encoded[:-2]
packed=base64.b64decode(encoded,validate=True)
assert pin(packed)==PACK_PIN
raw=lzma.decompress(packed);assert pin(raw)==RAW_PIN
units=json.loads(raw);assert set(units)==set(SOURCE_PINS)
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True)
for name,text in units.items():
    b=text.encode('utf-8');assert pin(b)==SOURCE_PINS[name]
    (out/name).write_bytes(b)
    print('COMPLETE_SOURCE_RESTORED',name,*pin(b))
print('ACTUATORS_COMPLETE_PREDECESSOR_AND_NEW_SOURCE_CLOSURE_PASS')
```

Supplementary convenience copies: complete recovery (`recover_actuators.py`), complete exact report (`actuator.json`), full literal handoff file (`result.json`). The reconstruction does not require any of these links.
