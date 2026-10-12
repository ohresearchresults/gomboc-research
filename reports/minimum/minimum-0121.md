# minimum-0121

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# FREE_VERTEX_FOUR_A_AFFINE_SHAPE_REGULARIZATION_V1

## 1. Result: the nonempty free-clique remainder is closed

**Theorem.** Let P be a full-dimensional simplicial convex three-polytope of uniform volume density, evaluated at its own actual volume centroid. Suppose its only physical weak equilibria are at most four distinct simple A=VE points. If at least one true vertex is neither endpoint of any weak edge, then P has arbitrarily small genuine regularizations with the same full face lattice and exactly the original feature-labelled strict S/U/H equilibria, and with no additional strict or weak equilibrium.

In particular, **every simplicial pure-four-A body with n≥9 vertices regularizes**. The theorem includes a singleton free fold and every adjacent free edge, triangle or K4, without restrictions on degrees, common left kernels, fold signs, metric condition number, or endpoint overlap. It closes the entire previously unresolved nonempty-free sector, not just a subset of its adjacent pairs. The older n≥13 nonadjacent theorem remains valid, including its any-number-of-contacts scope.

The new mechanism does not attempt to make the free-vertex centroid maps nonsingular. Their ranks are unchanged by the affine preliminary motion. Instead, one or at most two arbitrarily small genuine affine motions destroy the obstructing FULL vertex-shape stress, after which an all-positive actual shape derivative exists. The final motion may use every actual vertex and is recentered by its true uniform-volume centroid.

Two stronger statements are also proved. For any number of simple A points with a free vertex, the **entire signed full-shape stress space has dimension at most one**. For any number with contact-tensor rank at most two, the same affine-plus-shape regularization works. Moreover, when the tensor rank is at most two, or when the four tensors have rank three and the full stress has all four coefficients positive, a genuine **quadratic raw vertex arc at the original body** suffices. The proper-support rank-three case is closed by successive small motions; no uniform original-body order bound for that case is claimed here.

This is not a claim that a full stress and co-aligned same-side free folds cannot coexist at the original body. It proves that such a configuration cannot obstruct arbitrary-small regularization in the stated sector. No new exact body realizing that original coexistence is supplied. No minimum bound or incidence-registry count changes, and no weak110 seed or new110 attainer is claimed.

## 2. Source closure and verification status

I read the entire new 1933-line journal, including the literal required parent and all its executable source, through EOF. The unchanged earlier journal remains available and had already been read in full in this chat. The supplied source and report `nonadjacent_free.py` and `nonadjacent_free.json` were also read completely. Nothing needed for the new proof or capsule is missing.

Current journal: `research-journal(20260920-032441).md`, 314514 bytes, SHA-256 `7fe9401313f4587148eacfdfcca7f0f84794b2874638d7352570afc7a954f86c`.

Required parent: `minimum-0118`, authenticated at 41544 bytes and SHA-256 `259e7b4e515ce6b410d6f2351defa241288252361b2f0739c3364f504ff792cc`. Authentication uses compact UTF-8 JSON, keys `version,result_markdown`, `ensure_ascii=False`, separators `(',',':')`, exactly one final LF inside the Markdown string, and no envelope-final LF. No source-identity or scientific conflict was found. The notebook has two headings numbered51; the nonadjacent theorem is identified here by its title and immutable parent, not the duplicate section number.

The sole substantial inherited mathematical input needed below is the actual triangular-star theorem `rank D_w g≥2`, together with the genuine contact and shape-derivative semantics. The new argument, including the small-forest lemma, is proved below. The exact computations are new executed audits, not the universal proof inferred from samples. The parent suites were not routinely rerun. External lookup supplied no additional premise; no literature-priority or proof-assistant certification is claimed.

## 3. Actual full-shape stresses and the contact forest

Work in physical Euclidean coordinates with actual centroid g=0. An initial common SPD metric can be absorbed into a genuine invertible affine image, which transports the actual uniform centroid. All vectors below are columns.

For contact i write x_i→y_i, u_i=y_i−x_i and

    x_i·u_i=0,  x_i≠0,  u_i≠0,
    T_i=sym(x_i u_i^T),  W=span{T_i},  r=dim W.

The radial supporting plane at x_i exposes precisely its true edge [x_i,y_i]. Let A_j=D_(v_j)g be the actual uniform-centroid derivative. The complete shape matrix R has rows

    (Rh)_i=(u_i−x_i)·h_(x_i)+x_i·h_(y_i)
                         −u_i·Σ_j A_j h_j.                (1)

This is the FULL actual vertex derivative, not the affine or projective tensor restriction. Put

    c_alpha=Σ_i alpha_i u_i,
    F_j(alpha)=Σ_(source i=j) alpha_i(u_i−x_i)
                       +Σ_(target i=j) alpha_i x_i.

Then, for signed coefficients as well as nonnegative ones,

    R^T alpha=0  iff  F_j(alpha)=A_j^T c_alpha
                           for every actual vertex j.    (2)

These are the literal full equations from the parent. Testing actual affine fields h_j=K v_j in (1) gives

    R^T alpha=0  implies  Σ_i alpha_i T_i=0.              (3)

There is no converse assertion.

### Lemma 1. The weak contact graph is a rooted forest, and F is injective

A source vertex has at most one outgoing simple A edge: its radial plane exposes one edge, and two outgoing exposed edges would not be a simple VE point. Every arrow strictly increases squared radius:

    |y_i|²−|x_i|²=|u_i|²>0.

Thus directed cycles are impossible. An undirected cycle, with outdegree at most one, would force each of its vertices to have one outgoing cycle edge and hence a directed cycle. The graph is therefore a forest, oriented toward one sink root per component.

Take a source leaf with no incoming contact edge. Its force is alpha_i p_i, where

    p_i=u_i−x_i=y_i−2x_i,
    x_i·p_i=−|x_i|²<0.

In particular p_i≠0. If every F_j(alpha)=0, this leaf forces alpha_i=0. Delete its edge and repeat. This proves **injectivity of the endpoint-force map alpha↦(F_j(alpha)) for arbitrary signed coefficients**.

### Corollary 1. One free vertex makes the complete signed stress space at most one-dimensional

Let w be free. If alpha is a full stress, A_w^T c_alpha=0. The actual triangular-star theorem gives rank A_w≥2. If c_alpha=0, (2) and Lemma1 give alpha=0. Even without a free vertex, injectivity of alpha↦c_alpha on ker R^T gives dimension at most three. With w free it maps into a space of dimension at most one:

    dim ker R^T≤1.                                      (4)

If A_w is nonsingular, ker R^T=0. Otherwise, whenever a nonzero full stress alpha exists,

    ker A_w^T=span(c_alpha).                             (5)

This argument concerns the whole signed stress space. It is stronger than selecting or orienting a particular nonnegative stress ray. The accepted rank input applies at every degree; no positive symmetric part or cone-positive inverse is assumed.

For clarity, the strict linear alternative used below also has a short direct proof. There is a nonzero alpha≥0 with R^T alpha=0 exactly when 0 belongs to the convex hull of the row vectors of R. Otherwise its closest point z is nonzero and satisfies row_i·z≥|z|²>0 for every i. Taking h=z gives Rh>0. Thus absence of the full nonnegative stress cone gives a genuine positive shape velocity.

## 4. Exact affine transport, including every possible new stress

Take symmetric H∈W^perp and

    M_epsilon=I+epsilon H>0,  B_epsilon^T B_epsilon=M_epsilon.

The actual body B_epsilon P has uniform centroid0 and preserves every contact equality exactly:

    (B_epsilon x_i)·(B_epsilon u_i)
          =x_i^T M_epsilon u_i=0.

All other strict/excluding physical guards persist for sufficiently small epsilon. Its actual vertex-centroid derivatives are

    A_j(new)=B_epsilon A_j B_epsilon^(-1).                (6)

In particular the free maps remain singular if they started singular. Uniform density, rather than transported nonuniform density, is preserved because this is an affine map with constant Jacobian.

In the original chart, a signed stress beta at metric M satisfies the exact equations

    M F_j(beta)=A_j^T M c_beta  for every j.              (7)

Suppose alpha is an original nonzero full stress and write c=c_alpha, f_j=F_j(alpha). A new nonzero stress beta must, at the free vertex, satisfy

    M c_beta=lambda c,  lambda≠0.

Consequently, after normalization beta'=beta/lambda, every vertex equation becomes

    F_j(beta')=M^(-1) f_j.                               (8)

Equation(8) is an exact identity, not an assumed differentiable continuation of the old stress. In particular it addresses new stresses whose support could change.

## 5. All low-rank contact-tensor sectors, with any number of contacts

### Lemma 2. If r≤2 and a free vertex exists, a contact-preserving affine motion removes the full shape stress

Assume the positive shape velocity does not already exist, and choose the nonzero alpha≥0 in ker R^T. Strip source leaves whose alpha coefficient is zero until the first nonzero-coefficient leaf e is reached. Under (8), each stripped zero leaf also has beta'_e=0, so the same stripping is legitimate for every candidate new stress. At the first active leaf,

    beta'_e p_e=alpha_e M^(-1)p_e.                        (9)

Thus existence of any new full stress would require p_e to be an eigenvector of M.

For nonzero p define

    W(p)={sym(p q^T):q·p=0};  dim W(p)=2.

The line span(p) is invariant under every H∈W^perp exactly when W(p)⊂W, since q^T H p=⟨H,sym(p q^T)⟩.

But T_e does not belong to W(p_e). Indeed set

    q=|u_e|² x_e+|x_e|² u_e.

Then q·p_e=0 and

    q^T T_e q=|x_e|^4 |u_e|^4>0,

whereas q^T Tq=0 for every T∈W(p_e). Since T_e∈W and dim W≤2, containment W(p_e)⊂W is impossible. Choose H∈W^perp with Hp_e not parallel to p_e. For every nonzero sufficiently small epsilon, M_epsilon p_e is not parallel to p_e, contradicting (9). There is **no signed full stress at all** at the new body, so its shape matrix has full row rank and a positive first shape velocity exists.

This proves the any-number low-rank theorem. An exact H can be selected from any basis of W^perp; at least one basis element breaks the leaf line. The proof did not assume that the new stress equals alpha, that its support stays fixed, or that an endpoint supplies a normal centroid direction by itself.

## 6. The positive weighted four-edge forest lemma

### Lemma 3. A positive contact forest with at most four edges has weighted matrix nullity at most one

Use only the vertices incident to its edges: **omit all isolated/free vertices**. Give every edge child j→parent p(j) a positive weight a_j. Define the symmetric matrix K by

    K_(j,p(j))=K_(p(j),j)=a_j,
    K_jj=−2a_j for nonroots,  K_jj=0 for roots,
    all other entries=0.

Then dim ker K≤1 whenever there are at most four edges.

A one-edge component has determinant −a². A two-edge component has determinant 2a²b when its root is an end (a is the edge incident to that root), and 2ab(a+b) when its root is the middle vertex. Thus these components are nonsingular. There can be at most one component having three or more edges.

It remains to treat one tree on at most five vertices. A path has nullity at most one: its nonzero consecutive off-diagonal entries determine every coordinate of a kernel vector from the first coordinate by recurrence, irrespective of its diagonal. A star reduces to a path by Schur-eliminating nonroot leaves; enough such leaves exist, each pivot is its original nonzero −2a_j, and only the center diagonal changes. The only remaining five-vertex shape has one degree-three vertex with arms of lengths2,1,1. At least one of its two short leaves is not the root. Eliminating that leaf, again at its nonzero original diagonal, leaves a path. Schur elimination preserves nullity. This exhausts all cases and proves the lemma for **all positive weights**, not merely generic weights.

The executable independently enumerates the rooted types of sizes2,3,4,5 as 1,2,4,9 and all19 rooted forests with four edges and no isolates, and verifies these symbolic Schur/path reductions. These are proof-space graph types, not polytope incidence counts.

Invertibility would be a false strengthening. For parents (-1,0,1,2,3), child weights (1,1/3,1,1), K has the exact kernel vector (-1,0,3,2,1) and rank4. Also three length-two arms about a root, with root-adjacent weight1 and leaf weight4 in each arm, have six edges and nullity2. In vertex order root,arm1,leaf1,arm2,leaf2,arm3,leaf3, two kernel vectors are (0,2,1,−2,−1,0,0) and (0,2,1,0,0,−2,−1). These are exact graph-algebra controls, **not realized own-centroid bodies or mechanical obstructions**. They delimit the lemma actually used.

## 7. Rank-three four-contact stresses: the physical W(c) exception is also removed

Assume r=3 and the original full stress has alpha_i>0 for all four contacts. The tensor relation space is then exactly span(alpha). It remains the same coefficient line under every invertible affine congruence of the tensors.

For H∈W^perp define the full residual

    L(H)_j=H f_j−A_j^T Hc.                               (10)

If L(H) is nonzero for some H, equation(7) for the only possible stress alpha has residual epsilon L(H). Hence every nonzero sufficiently small epsilon removes **all signed full stresses**, and ordinary first-order shape regularization follows.

Suppose, to the contrary, L(H)=0 for every H∈W^perp. At the free vertex this gives A_w^T Hc=0, so by (5)

    Hc=lambda_H c for every H∈W^perp.                    (11)

This is precisely the previously exceptional situation W(c)⊂W. It is not being dismissed as nonphysical: the literal parent contains an actual four-A body with that tensor geometry.

Since dim W^perp=3 and I∈W^perp, the maps H−lambda_H I, restricted to c^perp, form a two-dimensional subspace of symmetric2×2 matrices. Its common kernel is zero: the symmetric2×2 matrices annihilating one prescribed nonzero vector form only a one-dimensional space. Thus the common kernel of all H−lambda_H I in three dimensions is exactly span(c).

Using f_j=A_j^T c, equations(10)–(11) now give

    (H−lambda_H I)f_j=0 for all H,
    hence f_j is parallel to c for every j.              (12)

Apply Lemma3 to the actual four-contact forest with weights alpha_i>0. Let X be its endpoint-coordinate matrix, with row v_j^T, and let Pi be orthogonal projection onto c^perp. The endpoint forces are exactly

    F(alpha)=KX.

Equation(12) says K X Pi=0. Lemma3 therefore gives rank(X Pi)≤1. All contact endpoints lie in one linear plane through0 containing c, or in a line. Consequently all T_i are symmetric, trace-zero tensors supported in that plane; that space has dimension at most two. This contradicts r=3.

So an H with L(H)≠0 necessarily exists, including throughout the W(c) exceptional sector. Its choice is constructive: evaluate (10) on a basis of W^perp and select a nonzero value. It is the **complete actual endpoint force equations**, not the tensor condition alone, that close the exception.

### Proper supports and the remaining tensor ranks

If r=4, there is no tensor stress and hence no full shape stress. If r≤2, Lemma2 applies. In the remaining r=3 case, suppose the unique nonnegative tensor/full stress alpha has a proper support S, of size at most three. The tensor-row map has image alpha^perp. Therefore a symmetric H can be chosen with

    ⟨H,T_i⟩=0 for i∈S,  ⟨H,T_i⟩=1 for i∉S.

The genuine affine metric I+epsilon H, epsilon>0, removes every off-support contact while leaving those in S exactly zero. The remaining tensors have rank |S|−1≤2: a second independent relation in that subset would contradict the original one-dimensional tensor relation space. A previously free vertex remains free. Apply Lemma2 at this new actual body, taking its preliminary motion and final shape step sufficiently small to retain the already positive off-support escapes.

This exhausts every tensor rank and every support of a nonnegative full stress for at most four contacts. It also explains why zero coefficients were not silently treated as positive weights in Lemma3.

## 8. Direct quadratic regularization in the full-support and low-rank sectors

Here is a reusable original-body version, beyond the successive-motion existence proof. In either Lemma2 or the full-support rank-three case, H can be chosen so that

    R_H^T alpha is not in im R^T,                         (13)

where R_H is formula(1) with every dot product replaced by its H-bilinear form. Consequently some v∈ker R has sigma=alpha^T R_H v≠0.

For Lemma2, a contrary first-order stress correction beta would satisfy

    F_j(beta)+H f_j=A_j^T(c_beta+Hc).

The free equation gives c_beta+Hc=lambda c. Replacing beta by beta−lambda alpha leaves F_j(beta)+H f_j=0. Strip the zero leaves as before. At the first active leaf this requires beta_e p_e=−alpha_e Hp_e, contradicting the chosen H. Thus (13) holds.

For rank three, if R^T beta=−R_H^T alpha, evaluate both sides on every actual infinitesimal affine field. The right side annihilates those fields because Σalpha_i T_i=0. Hence beta is a tensor relation and therefore proportional to alpha. This forces R_H^T alpha=0, contrary to the nonzero residual chosen in section7. Again (13) follows.

Write the true centroid of the raw straight motion X+s v as

    g(s)=s g1+s² g2+O(s³).

For the original outward boundary triangles, with z0=sum of their vertices, z1=sum of their velocities and d0,d1,d2 the determinant coefficients of orders0,1,2,

    V1=Σd1/6,
    J1=Σ(d1 z0+d0 z1)/24,
    J2=Σ(d2 z0+d1 z1)/24,
    g1=J1/V,  g2=J2/V−V1 J1/V².

Every shared-triangle mixed determinant is included in d2. The true quadratic escape coefficient is

    b_i(v)=(v_(x_i)−g1)·(v_(y_i)−v_(x_i))−u_i·g2.       (14)

These are the complete jets retained in the literal parent, now used with the new rank-lifting direction.

Reverse v if necessary so sigma>0. Put tau=alpha·b(v) and choose

    a=sigma/[2(sigma+|tau|)]>0,
    b*=a R_H v+a² b(v).

Then alpha·b*>0. Set q=(alpha·b*)/Σalpha_i and solve

    R delta=q 1−b*.

This is solvable because im R=alpha^perp by (4). The actual raw shape X+s a v+s² delta, with metric I+sH and exact actual recentering, has all four—or all k in the low-rank version—escapes q s²+O(s³)>0.

It can also be realized by a quadratic raw vertex arc in the original Euclidean metric. Expand the genuine symmetric square root

    (I+sH)^(1/2)=I+sH/2−s²H²/8+O(s³)

and use raw vertices

    v_j+s[a v_j^(motion)+H v_j/2]
       +s²[delta_j+(a/2)H v_j^(motion)−H² v_j/8].         (15)

Here v_j^(motion) denotes the velocity block previously called v, and v_j without that superscript is the original position. The polynomial arc has the same two physical shape jets as the analytic affine composition; the true centroid functional is analytic in this simplicial chamber. After its own actual recentering, all escapes retain the same positive second coefficients. No uncomputed higher-order cancellation is required.

## 9. Why this solves the physical question, rather than only its first jet

Once an actual body has a velocity with all required A escapes positive to first order, or an arc with all positive second coefficients as above, its true volume and first moment are the complete boundary polynomials

    V(s)=Σ_(i,j,k) det(v_i(s),v_j(s),v_k(s))/6,
    J(s)=Σ_(i,j,k) det(v_i(s),v_j(s),v_k(s))
                         [v_i(s)+v_j(s)+v_k(s)]/24,
    g(s)=J(s)/V(s).

These formulas do not assume nonadjacency. V(0)>0 makes g analytic. The positive leading terms therefore persist on a sufficiently short punctured interval. Every original strict or excluding feature guard is open, the complete simplicial face chamber is open, and the positive A primitive removes its complete original simple packet. Harmless zeros with another positive primitive remain excluded from the weak census. All old strict labels remain, no new strict equilibrium is born, and no physical weak packet remains. This is the same physical escape convention as the parent, not independent sign choices for primitive zeros.

In particular, singular co-aligned free maps need not become nonsingular and need not compensate a prescribed missing normal centroid displacement. The affine motion breaks the full contact stress, sometimes at an endpoint equation while the free centroid ranks are entirely unchanged. The final vertex motion and its genuine recentering supply the physical regularization.

## 10. Complete adjacent mixed moments, retained as a reusable method

For adjacent w,z with the two outward triangles (w,z,a) and (z,w,b), put d=a−b and D=det(h,l,d), where h,l displace w,z respectively. Let a_w,a_z be the inward star sums and B_j=24V A_j at the original actual centroid g. The exact joint formulas are

    V(h,l)=V−(a_w·h+a_z·l)/6+D/6,
    24[J(h,l)−g V(h,l)]
       =B_w h+B_z l−(a_w·h)h−(a_z·l)l+C(h,l),

    C(h,l)=D(w+z−4g+h+l)
           +det(h,l,a)a−det(h,l,b)b
           +det(h,z,d)l+det(w,l,d)h.                     (16)

Proof: in each shared boundary determinant multiply its constant, h-linear, l-linear and hl-bilinear terms by the triangle vertex sum. Subtract its two one-vertex changes. The two orientations give exactly (16); all other triangles have no mixed contribution. C contains both quadratic and cubic terms. This is not the parent's nonadjacent additivity formula.

The new actual free-edge fixture below verifies (16) symbolically in all six displacement coordinates, including a nonzero mixed volume polynomial and a nonzero cubic moment polynomial. The general regularization theorem avoids solving that adjacent nonlinear control problem, but the complete method is preserved for larger-contact continuation.

## 11. Newly executed exact controls and meaningful negative boundaries

### Four rational own-centroid bodies with a true adjacent free edge

These are new nonrecord controls, not aliases of the parent's nine-vertex or fourteen-vertex controls. Set

    d(h)=(-21h²−12h+344)/(36h²−9h−9),
    X(h)=[(1,0,0),(1,1/3,1),(0,1,0),(-1/3,1,2),
          (-1,0,0),(-1,-1/3,1),(0,-1,0),(1/3,-1,2),
          (d(h),0,h),(-d(h),0,h)].

The four executed heights are -41/10,-4,-39/10,-7/2, giving d=4019/63306,56/603,7139/57366,5/18 respectively. Every one is a true simplicial10/24/16 body, actual COM0, strict8/6/12, with exactly four simple A packets on 0→1,2→3,4→5,6→7 and exactly four zero primitives among96. Vertices8,9 are the two free vertices, form a true edge, and both have degree5. Their actual Jacobians are nonsingular, and the full shape matrix has rank4. Thus these controls do **not** realize the difficult full-stress/fold conjunction and are not evidence by themselves for the new universal theorem.

The primary h=-7/2 body has V=125/18 and

    A8=[[49/600,41/3000,-179/9000],
        [1/125,19/250,-1/375],
        [-309/1000,-3/200,83/600]],
    det A8=det A9=217561/562500000>0.

Its covariance is

    [[176053/1215000,-113/101250,0],
     [-113/101250,5197/33750,0],
     [0,0,3947/3000]].

Its complete sorted maximal facets are

    017,018,067,068,123,128,137,234,
    249,289,345,357,459,567,569,689.

Strict S facets are [3,5,6,8,9,11,14,15], U vertices [1,3,5,7,8,9], and H edges [(0,8),(1,3),(1,7),(2,8),(2,9),(3,5),(3,7),(4,9),(5,7),(6,8),(6,9),(8,9)]. Facet indices are zero-based in that sorted order.

The tensors have rank3, unique positive relation (1,1,1,1), c=(0,0,6), and W is the off-diagonal symmetric subspace, so W(c)⊂W. But A8^T c=(-927/500,-9/100,83/100)≠0: this tensor stress is not FULL. The source explicitly checks every actual vertex equation symbolically in four arbitrary stress coefficients and six arbitrary metric coefficients, not just this one stress.

### A fully certified regularization arc using the complete actual moments

For the primary body start with h_j=|v_j|²v_j and replace

    h8 by h8−A8^(-1)Σ_j A_j h_j.

The original radial centroid derivative is (0,0,-999/125). The corrected derivative is exactly0; h9 still moves, so the adjacent free edge is not frozen. The corrected h8 is

    (21509398177/634407876,
     263736/217561,
     5839736869/70489764).

Take the raw straight arc v_j(t)=v_j+t h_j and subtract its complete actual g(t). The four first escape coefficients are (10/9,37/9,10/9,37/9). The actual second centroid coefficient, which is not discarded, is

    (593090726561213/106498774622250,
     -12974125640506/17749795770375,
     -208763286199554492751/1863302560790886000).

On the WHOLE interval 0<t≤1/65536, 225 positive polynomial guards—112 nonincident supports,16 centroid-plane guards,1 volume guard,92 old primitive signs and4 positive weak quotients—have1376 strictly positive exact Bernstein coefficients, maximum degree10. All original strict8/6/12 labels persist and weak000 holds throughout. The endpoint is independently re-hulled and re-integrated from two different positive apex fans, with a full mechanical census. This is a continuous certificate, not endpoint sampling.

For the isolated six-variable displacement test on edge8–9, the outward opposite vertices are a=2,b=6, and

    D=−2 h0 l2+2 h2 l0,

which is nonzero. The complete cubic C from(16) is reconstructed in the report. Thus extending nonadjacent additivity to this actual adjacent edge would be false.

### Wrong-chamber centroid extension, preserved rather than silently accepted

In the first four bodies' facet chamber, exact integration gives

    V=−(18dh−9d+21h−94)/27,
    Jz=−(36dh²−9dh−9d+21h²+12h−344)/108.

Solving Jz=0 yields d(h). But at h=-3,d=191/342 the true hull has changed. Its independently computed true V=7343/1026 and J=(0,0,-5/513), hence g=(0,0,-10/7343), not0. After actual recentering it has strict8/6/12 and weak000, not four A contacts. The complete new lattice and mechanics are preserved by the capsule. This is an exact negative control against extending a chamber-specific moment polynomial across a hull change.

The regularization constructor included in the source supplies genuine small metric premoves and a positive actual vertex velocity for any eligible rational input. It uses the complete signed stress space and a finite-dimensional tensor basis, with dyadic steps and all nonzero mechanical guard checks. Its default total entrywise metric budget is1/65536 and can be made smaller. The nonempty-stress branches are justified by the proof above, but **were not exercised on a newly realized obstructed physical fixture**. The executed constructor check is the rank4 primary body. A finite arc interval for a different input must still be certified; the primary arc's exact certification is separate and complete.

## 12. Remaining scope and useful continuation

The genuinely adjacent nonempty-free simplicial pure-four-A remainder is no longer open under the stated hypotheses. Remaining four-A cases not covered by this theorem are the **no-free-vertex endpoint-cover sector**, necessarily 5≤n≤8 by the forest count, except for affine-separable cases and where older accepted results already apply; and nonsimplicial bodies where arbitrary vertex velocities need not preserve maximal-facet planarity. The latter includes the minimum's10/17/9 layer. Mixed A/B and VF configurations outside the previously accepted sectors remain separate. For five or more A contacts, the signed-stress dimension bound and low-tensor-rank theorem persist, but general tensor rank≥3 beyond the older nonadjacent and other accepted criteria is not closed.

The existence of an original actual full stress with only same-side co-aligned free folds is still not settled here. What is settled is that it cannot be an all-orders regularization obstruction for four simple A contacts with a free vertex. The new theorem does not say that a frozen free clique alone has an open centroid map. Nor does it turn the graph nullity controls or the rational nonwinning bodies into a weak110 construction. The accepted global bracket34≤C_min≤622 is unchanged.

The most useful continuation is the no-free four-A endpoint-cover problem using the same full-force map and its at-most-three-dimensional signed stress space. Repeating a search for an all-orders obstruction in the now-closed free-clique sector is not necessary.

## 13. Complete source-only recovery capsule

Save the complete source below as `free_vertex_four_a.py`, UTF-8/LF with one final LF. Its exact parent identity, every rational input, the five height parameters, all facet labels, the generic constructor's entry budget, the whole-arc interval, both graph controls, and every helper are included. There is no parent-code import or unprovided data file.

Observed environment: CPython3.13.5, SymPy1.14.0, mpmath1.3.0, assertions enabled, PYTHONHASHSEED=0. No random input, numerical optimizer, network or floating acceptance test is used. The build, check, and a fresh final-source-only cold build/check all completed; source, report and stdout matched byte for byte.

    export PYTHONHASHSEED=0
    python free_vertex_four_a.py build > build.txt
    python free_vertex_four_a.py check > check.txt
    cmp build.txt check.txt

Exact pins:

    free_vertex_four_a.py  20872 bytes
    SHA256 44b617b5a25b057e220b0d4a8bf57e888f54729246395d3f4544be92338b91d3
    free_vertex_four_a.json  181974 bytes
    SHA256 e88a440b55d6fd58eb3a684945c47f9a6dccbaeff148b64ee30297e65cc507d6
    build.txt / check.txt  523 bytes
    SHA256 fcfd9847af5703bf6997188e5a5274dd6eaf782ddb2248dd2ab96d1fd792a764

Exact stdout:


[Encoded source block omitted; the code in this passage is incomplete.]

    free_vertex_four_a.json 181974 e88a440b55d6fd58eb3a684945c47f9a6dccbaeff148b64ee30297e65cc507d6
    FREE_VERTEX_FOUR_A_AFFINE_SHAPE_REGULARIZATION_RECOVERY_PASS

The separate cold comparison marker was `FREE_VERTEX_FOUR_A_FINAL_SOURCE_ONLY_COLD_BYTE_PARITY_PASS`. The report is regenerated from source; it is not an input. For a nonidentity metric returned by the constructor, exact physical coordinates are obtained with `B=M.cholesky().T`, so `B.T*B==M`, followed by the prescribed actual-centroid subtraction. The dual metric is always `M.inv()`.

Convenience copies: plain complete source (`free_vertex_four_a.py`) and complete exact report (`free_vertex_four_a.json`). They are optional: all recovery bytes follow in this handoff.

```python
"""FREE_VERTEX_FOUR_A_AFFINE_SHAPE_REGULARIZATION_V1.
CPython 3.13.5, SymPy 1.14.0, mpmath 1.3.0; assertions, no RNG/network.
python free_vertex_four_a.py build|check
The geometric theorem is analytic. The actual free-edge fixtures below have
nonsingular free Jacobians: they are NOT full-stress/fold coexistence examples.
"""
from pathlib import Path
from itertools import combinations, combinations_with_replacement, product
from math import comb
import hashlib, json, sys
import sympy as s
assert __debug__ and s.__version__ == '1.14.0'
Q=s.Rational; Z=s.zeros(3,1); I=s.eye(3); t=s.Symbol('t')
PARENT='minimum-0118'
PARENT_SHA='259e7b4e515ce6b410d6f2351defa241288252361b2f0739c3364f504ff792cc'
HEIGHTS=[-Q(41,10),-4,-Q(39,10),-Q(7,2),-3]
EPS=Q(1,65536)
CONTACTS=[(0,1),(2,3),(4,5),(6,7)]
FACES=[(0,1,7),(0,1,8),(0,6,7),(0,6,8),(1,2,3),(1,2,8),
       (1,3,7),(2,3,4),(2,4,9),(2,8,9),(3,4,5),(3,5,7),
       (4,5,9),(5,6,7),(5,6,9),(6,8,9)]
SYMBASIS=[]
for i,j in [(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]:
    H=s.zeros(3);H[i,j]=H[j,i]=1;SYMBASIS.append(H)
def simp(x):
    return x.applyfunc(s.cancel) if isinstance(x,s.MatrixBase) else s.cancel(x)
def det(a,b,c):return a.dot(b.cross(c))
def enc(x):
    if isinstance(x,s.MatrixBase):return [[enc(v) for v in row] for row in x.tolist()]
    if isinstance(x,s.Basic):return str(x)
    if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [enc(v) for v in x]
    return x

def hull(X):
    inside=sum(X,Z)/len(X);faces={}
    for i,j,k in combinations(range(len(X)),3):
        n=(X[j]-X[i]).cross(X[k]-X[i])
        if n==Z:continue
        vals=[n.dot(v-X[i]) for v in X]
        if min(vals)<0<max(vals):continue
        f=tuple(a for a,v in enumerate(vals) if v==0)
        assert len(f)==3, ('Nontriangular maximal face',f)
        if f in faces:continue
        if n.dot(inside-X[i])>0:j,k=k,j
        faces[f]=(i,j,k)
    fs=sorted(faces);tri=[faces[f] for f in fs];edges={}
    for fi,f in enumerate(fs):
        for e in combinations(f,2):edges.setdefault(e,[]).append(fi)
    assert all(len(a)==2 for a in edges.values())
    assert len(X)-len(edges)+len(fs)==2
    assert set(sum((list(f) for f in fs),[]))==set(range(len(X)))
    return fs,tri,dict(sorted(edges.items()))

def mass(X,tri,apex=Z,second=True):
    V=s.S(0);J=Z.copy();R=s.zeros(3);weights=[]
    for f in tri:
        p=[apex]+[X[i] for i in f]
        d=det(p[1]-apex,p[2]-apex,p[3]-apex);z=sum(p,Z)
        weights.append(simp(d));V+=d/6;J+=d*z/24
        if second:R+=d*(z*z.T+sum((v*v.T for v in p),s.zeros(3)))/120
    return simp(V),simp(J),simp(R),weights

def jacobians(X,tri,V,g):
    A=[]
    for w in range(len(X)):
        B=s.zeros(3)
        for i,j,k in tri:
            if w in (i,j,k):
                n=(X[j]-X[i]).cross(X[k]-X[i])
                B+=(X[i]+X[j]+X[k]+X[w]-4*g)*n.T
        A.append(simp(B/(24*V)))
    assert sum(A,s.zeros(3))==I
    return A

def star(X,tri,w):
    a=Z.copy();S=s.zeros(3)
    for f in tri:
        if w not in f:continue
        j=f.index(w);u=X[f[(j+1)%3]]-X[w];v=X[f[(j+2)%3]]-X[w]
        c=-u.cross(v)
        assert all(c.dot(x-X[w])>=0 for x in X)
        a+=c;S+=(u+v)*c.T
    return a,S

def mechanics(X,tri,edges,g,M=I):
    N=M.inv();Y=[x-g for x in X];poles=[]
    for i,j,k in tri:
        n=(X[j]-X[i]).cross(X[k]-X[i]);h=n.dot(X[i]-g)
        assert h>0;poles.append(simp(n/h))
    pv=[[] for x in X];pq=[[] for f in tri];rows=[];weak=[];zeros=0
    for (a,b),(f,h) in edges.items():
        vals=list(map(simp,[(Y[a].T*M*(Y[b]-Y[a]))[0],
             (Y[b].T*M*(Y[a]-Y[b]))[0],
             (poles[f].T*N*(poles[h]-poles[f]))[0],
             (poles[h].T*N*(poles[f]-poles[h]))[0]]))
        sg=[int(s.sign(v)) for v in vals];zeros+=sg.count(0)
        pv[a].append(sg[0]);pv[b].append(sg[1]);pq[f].append(sg[2]);pq[h].append(sg[3])
        rows.append([a,b,f,h,vals])
        if max(sg)==0:weak.append([a,b,sg])
    return {'poles':poles,'rows':rows,'S':[j for j,p in enumerate(pq) if max(p)<0],
            'U':[j for j,p in enumerate(pv) if max(p)<0],
            'H':[(a,b) for a,b,f,h,v in rows if all(x<0 for x in v)],
            'weak_packets':weak,'zero_primitives':zeros}

def shape_matrix(X,A,contacts,M=I):
    R=s.zeros(len(contacts),3*len(X))
    for i,(a,b) in enumerate(contacts):
        x=X[a];u=X[b]-x
        for j in range(len(X)):R[i,3*j:3*j+3]=-u.T*M*A[j]
        R[i,3*a:3*a+3]+=(u-x).T*M
        R[i,3*b:3*b+3]+=x.T*M
    return R

def endpoint_forces(X,contacts,alpha):
    F=[Z.copy() for x in X];c=Z.copy()
    for (a,b),w in zip(contacts,alpha):
        x=X[a];u=X[b]-x;c+=w*u;F[a]+=w*(u-x);F[b]+=w*x
    return F,c

def tensor_rows(X,contacts):
    return s.Matrix([[(X[a].T*H*(X[b]-X[a]))[0] for H in SYMBASIS]
                     for a,b in contacts])

def solve_zero_free(R,b):
    x,params=R.gauss_jordan_solve(b)
    return x.subs({p:0 for p in params})

def valid_metric(M,old,X,tri,edges):
    if not all(M[:j,:j].det()>0 for j in (1,2,3)):return False
    mm=mechanics(X,tri,edges,Z,M)
    return all(v0==0 or v0*v1>0 for a,b in zip(old['rows'],mm['rows'])
               for v0,v1 in zip(a[4],b[4]))

def affine_regularizer(X,tri,edges,contacts,entry_budget=Q(1,65536)):
    """Exact rational construction for an eligible <=4-A body with a free vertex.
    Returns a final chart metric, a genuine shape velocity and all premoves.
    Termination on the stated sector is supplied by the analytic theorem, not
    inferred from any bounded search. The signed shape-stress space has dim<=1.
    """
    V,J,_,_=mass(X,tri,second=False);assert J==Z
    A=jacobians(X,tri,V,Z);M=I.copy();active=list(contacts);moves=[]
    assert 0<entry_budget<Q(1,6)
    assert 1<=len(active)<=4 and set(range(len(X)))-set(sum((list(e) for e in active),[]))
    assert len({a for a,b in active})==len(active)
    initial=mechanics(X,tri,edges,Z)
    actual=[]
    for a,b,sg in initial['weak_packets']:
        assert sg in ([0,-1,-1,-1],[-1,0,-1,-1])
        actual.append((a,b) if sg[0]==0 else (b,a))
    assert sorted(actual)==sorted(active)
    def allowed(H,power,old):
        return max(abs(z) for z in H)/2**power<=entry_budget/2 and valid_metric(M+H/2**power,old,X,tri,edges)
    while True:
        old=mechanics(X,tri,edges,Z,M);R0=shape_matrix(X,A,active,M)
        ns=R0.T.nullspace();assert len(ns)<=1
        if not ns:q=s.ones(len(active),1)
        else:
            alpha=ns[0]
            if all(z<=0 for z in alpha):alpha=-alpha
            if min(alpha)<0<max(alpha):
                pp=sum(z for z in alpha if z>0);nn=-sum(z for z in alpha if z<0)
                q=s.Matrix([nn if z>0 else pp if z<0 else 1 for z in alpha])
                assert (alpha.T*q)[0]==0
            else:
                assert min(alpha)>=0 and max(alpha)>0
                T=tensor_rows(X,active);rank=T.rank()
                assert T.T*alpha==s.zeros(6,1)
                if rank==3 and any(z==0 for z in alpha):
                    target=s.Matrix([1 if z==0 else 0 for z in alpha])
                    coef=solve_zero_free(T,target)
                    H=sum((c*h for c,h in zip(coef,SYMBASIS)),s.zeros(3))
                    power=1
                    while not allowed(H,power,old):power+=1
                    M=M+H/2**power
                    moves.append({'kind':'remove_zero_stress_support','H':H,'power':power})
                    active=[e for e,z in zip(active,alpha) if z!=0]
                    continue
                assert rank<=2 or (rank==3 and min(alpha)>0)
                directions=[sum((z*h for z,h in zip(v,SYMBASIS)),s.zeros(3)) for v in T.nullspace()]
                lifted=False;power=1
                while not lifted:
                    for H in directions:
                        MM=M+H/2**power
                        if shape_matrix(X,A,active,MM).rank()!=len(active):continue
                        if not allowed(H,power,old):continue
                        M=MM;moves.append({'kind':'destroy_entire_shape_stress','H':H,'power':power})
                        lifted=True;break
                    power+=1
                continue
        vel=solve_zero_free(R0,q)
        assert all(z>0 for z in R0*vel)
        return M,[vel[3*j:3*j+3,0] for j in range(len(X))],moves,active

def forest_certificates():
    def canonical(p):
        def f(j):return tuple(sorted(f(k) for k in range(1,len(p)) if p[k]==j))
        return f(0)
    types=[];counts=[]
    for n in range(2,6):
        reg={}
        for tail in product(*(range(j) for j in range(1,n))):
            p=(-1,)+tail;reg.setdefault(canonical(p),p)
        counts.append(len(reg));types.extend(sorted(reg.values()))
    assert counts==[1,2,4,9]
    def component(p):
        n=len(p);a=s.symbols('a1:'+str(n),positive=True);K=s.zeros(n)
        for j,w in enumerate(a,1):K[j,j]=-2*w;K[j,p[j]]=K[p[j],j]=w
        adj={j:set() for j in range(n)}
        for j in range(1,n):adj[j].add(p[j]);adj[p[j]].add(j)
        remaining=list(range(n));B=K.copy();steps=[]
        while max(map(len,adj.values()))>2:
            leaves=[j for j in remaining if j!=0 and len(adj[j])==1 and len(adj[next(iter(adj[j]))])>2]
            assert leaves
            j=min(leaves);i=remaining.index(j);nb=next(iter(adj[j]))
            assert B[i,i]==-2*a[j-1]
            keep=[k for k in range(len(remaining)) if k!=i]
            pivot=B[i,i];B=simp(B.extract(keep,keep)-B.extract(keep,[i])*B.extract([i],keep)/pivot)
            steps.append([j,nb,pivot]);remaining.remove(j);adj[nb].remove(j);del adj[j]
        assert max(map(len,adj.values()))<=2
        assert sum(map(len,adj.values()))==2*(len(adj)-1)
        # The remaining graph is a path with every off-diagonal edge nonzero.
        for j in remaining:
            for k in adj[j]:assert B[remaining.index(j),remaining.index(k)]!=0
        small_det=None
        if n<=3:
            small_det=s.factor(K.det());P=s.Poly(small_det,*a)
            assert all(c>0 for c in P.coeffs()) if n==3 else -small_det==a[0]**2
        return {'parents':p,'matrix':K,'leaf_schur_steps':steps,
                'remaining_path':remaining,'path_matrix':B,'small_determinant':small_det}
    comp=[component(p) for p in types];forests=[]
    for count in range(1,5):
        for ids in combinations_with_replacement(range(len(types)),count):
            if sum(len(types[i])-1 for i in ids)!=4:continue
            assert sum(len(types[i])-1>=3 for i in ids)<=1
            forests.append(list(ids))
    assert len(forests)==19
    # Positive-weight singularity is real; invertibility must not replace nullity<=1.
    p=(-1,0,1,2,3);weights=[1,Q(1,3),1,1];K=s.zeros(5)
    for j,w in enumerate(weights,1):K[j,j]=-2*w;K[j,p[j]]=K[p[j],j]=w
    v=s.Matrix([-1,0,3,2,1])
    assert K*v==s.zeros(5,1) and K.rank()==4
    # Six edges already permit nullity two; this is a GRAPH control, not a body.
    K6=s.zeros(7)
    for j in (1,3,5):
        K6[j,j]=-2;K6[j+1,j+1]=-8
        K6[0,j]=K6[j,0]=1;K6[j,j+1]=K6[j+1,j]=4
    N=s.Matrix([[0,0],[2,2],[1,1],[-2,0],[-1,0],[0,-2],[0,-1]])
    assert K6*N==s.zeros(7,2) and K6.rank()==5 and N.rank()==2
    # Uniform leaf tensor identity, in an orthogonal physical two-plane.
    a,b=s.symbols('a b',positive=True);x=s.Matrix([a,0,0]);u=s.Matrix([0,b,0]);p=u-x;q=s.Matrix([b,a,0])
    T=(x*u.T+u*x.T)/2
    assert p.dot(q)==0 and (q.T*T*q)[0]==a*a*b*b
    return {'rooted_type_counts':counts,'components':comp,'four_edge_forests':forests,
            'positive_singular_four_edge':{'parents':(-1,0,1,2,3),'weights':weights,'K':K,'kernel':v},
            'six_edge_nullity_two_GRAPH_ONLY':{'K':K6,'kernel':N},
            'leaf_tensor_identity':(q.T*T*q)[0]}

def fixture(height):
    height=s.S(height)
    d=simp((-21*height**2-12*height+344)/(36*height**2-9*height-9))
    X=list(map(s.Matrix,[(1,0,0),(1,Q(1,3),1),(0,1,0),(-Q(1,3),1,2),
             (-1,0,0),(-1,-Q(1,3),1),(0,-1,0),(Q(1,3),-1,2),(d,0,height),(-d,0,height)]))
    fs,tri,edges=hull(X);V,J,R,ds=mass(X,tri,X[0]);v,j,r,dd=mass(X,tri,X[8])
    assert V==v and J==j and R==r and all(x>=0 for x in ds+dd)
    g=J/V;mm=mechanics(X,tri,edges,g)
    assert len(edges)==24 and len(fs)==16 and (8,9) in edges
    A=jacobians(X,tri,V,g);centered=[x-g for x in X]
    R0=shape_matrix(centered,A,CONTACTS)
    Ts=tensor_rows(centered,CONTACTS)
    if height!=-3:
        assert fs==FACES and J==Z and mm['zero_primitives']==4
        for a,b in CONTACTS:
            assert X[a].dot(X[b]-X[a])==0
            assert all(X[a].dot(X[j]-X[a])<0 for j in range(len(X)) if j not in (a,b))
        assert mm['weak_packets']==[[a,b,[0,-1,-1,-1]] for a,b in CONTACTS]
        assert mm['S']==[3,5,6,8,9,11,14,15] and mm['U']==[1,3,5,7,8,9]
        assert mm['H']==[(0,8),(1,3),(1,7),(2,8),(2,9),(3,5),(3,7),(4,9),(5,7),(6,8),(6,9),(8,9)]
        assert Ts.rank()==3 and Ts.T*s.ones(4,1)==s.zeros(6,1)
        assert A[8].det()>0 and A[9].det()>0 and R0.rank()==4
        assert sum(8 in e for e in edges)==sum(9 in e for e in edges)==5
    else:
        assert fs!=FACES and J==s.Matrix([0,0,-Q(5,513)])
        assert mm['zero_primitives']==0 and mm['weak_packets']==[]
    out={'height':height,'separation':d,'vertices':X,'facets':fs,'triangles':tri,
         'edges':[[e,f] for e,f in edges.items()],'volume':V,'first_moment':J,'centroid':g,
         'covariance':simp(R/V-g*g.T),'positive_fans':[ds,dd],'mechanics':mm,
         'jacobians':A,'contact_shape_matrix':R0,'tensor_rows':Ts}
    return out,X,fs,tri,edges,V,A,mm

def adjacent_identity(X,tri,V,A):
    w,z=8,9;h=s.Matrix(s.symbols('h0:3'));l=s.Matrix(s.symbols('l0:3'))
    aa=bb=None
    for f in tri:
        if w not in f or z not in f:continue
        j=f.index(w)
        if f[(j+1)%3]==z:aa=f[(j+2)%3]
        else:bb=f[(j+1)%3]
    assert aa is not None and bb is not None
    a,b=X[aa],X[bb];d=a-b;D=det(h,l,d)
    aw,Sw=star(X,tri,w);az,Sz=star(X,tri,z)
    assert 24*V*A[w]==-4*X[w]*aw.T-Sw
    Y=X.copy();Y[w]=X[w]+h;Y[z]=X[z]+l
    vv,jj,_,_=mass(Y,tri,second=False)
    cross=D*(X[w]+X[z]+h+l)+det(h,l,a)*a-det(h,l,b)*b+det(h,X[z],d)*l+det(X[w],l,d)*h
    expected=24*V*(A[w]*h+A[z]*l)-aw.dot(h)*h-az.dot(l)*l+cross
    assert simp(vv-(V-(aw.dot(h)+az.dot(l))/6+D/6))==0
    assert simp(24*jj-expected)==Z
    assert s.Poly(D,*list(h),*list(l)).total_degree()==2 and D!=0
    assert any(s.Poly(z,*list(h),*list(l)).total_degree()==3 for z in cross)
    return {'edge':[w,z],'oriented_opposite_vertices':[aa,bb],'mixed_six_volume':D,
            'mixed_twentyfour_first_moment':cross,'star_a':[aw,az]}

def jet(X,tri,H,V):
    V1=s.S(0);J1=Z.copy();J2=Z.copy()
    for i,j,k in tri:
        a,b,c=X[i],X[j],X[k];h,l,m=H[i],H[j],H[k]
        d0=det(a,b,c);d1=det(h,b,c)+det(a,l,c)+det(a,b,m)
        d2=det(h,l,c)+det(h,b,m)+det(a,l,m)
        z0=a+b+c;z1=h+l+m
        V1+=d1/6;J1+=(d1*z0+d0*z1)/24;J2+=(d2*z0+d1*z1)/24
    return simp(V1),simp(J1/V),simp(J2/V-V1*J1/V**2)

def bern(p):
    p=s.Poly(s.expand(p),t);n=max(0,p.degree())
    b=[sum(p.nth(j)*EPS**j*Q(comb(k,j),comb(n,j)) for j in range(k+1)) for k in range(n+1)]
    assert all(z>0 for z in b),p.as_expr()
    return b

def certified_arc(X,fs,tri,edges,V,A,old):
    vel=[x.dot(x)*x for x in X];radg=sum((a*h for a,h in zip(A,vel)),Z)
    vel[8]=simp(vel[8]-A[8].inv()*radg)
    assert sum((a*h for a,h in zip(A,vel)),Z)==Z
    R0=shape_matrix(X,A,CONTACTS);hv=s.Matrix.vstack(*vel)
    assert R0*hv==s.Matrix([Q(10,9),Q(37,9),Q(10,9),Q(37,9)])
    Y=[x+t*h for x,h in zip(X,vel)];Vt,Jt,_,_=mass(Y,tri,second=False)
    v1,g1,g2=jet(X,tri,vel,V)
    assert g1==Z and all(s.expand(z).coeff(t,1)==0 for z in Jt)
    assert simp(s.Matrix([s.expand(z).coeff(t,2) for z in Jt])/V-g2)==Z
    guards=[['volume',bern(Vt)]];normals=[];slacks=[]
    for f,(i,j,k) in zip(fs,tri):
        n=(Y[j]-Y[i]).cross(Y[k]-Y[i]);normals.append(n)
        L=s.expand(Vt*n.dot(Y[i])-n.dot(Jt));slacks.append(L)
        guards.append(['centroid_inside',f,bern(L)])
        for z in range(len(X)):
            if z not in f:guards.append(['support',f,z,bern(n.dot(Y[i]-Y[z]))])
    weak_quotients=[]
    for a,b,f,h,values in old['rows']:
        e=Y[b]-Y[a]
        nums=[(Vt*Y[a]-Jt).dot(e),(Vt*Y[b]-Jt).dot(-e),
              normals[f].dot(normals[h])*slacks[f]-normals[f].dot(normals[f])*slacks[h],
              normals[h].dot(normals[f])*slacks[h]-normals[h].dot(normals[h])*slacks[f]]
        for k,(v,p) in enumerate(zip(values,nums)):
            if v==0:
                assert k==0 and (a,b) in CONTACTS
                p=s.cancel(p/t);assert not s.denom(p).has(t)
                weak_quotients.append([(a,b),p])
                guards.append(['weak_quotient',[a,b],bern(p)])
            else:guards.append(['primitive',[a,b,f,h],k,bern(s.sign(v)*p)])
    end=[simp(v.subs(t,EPS)) for v in Y];ff,tt,ee=hull(end)
    ve,je,re,ds=mass(end,tt,end[0]);v2,j2,r2,dd=mass(end,tt,end[8])
    assert ve==v2 and je==j2 and re==r2 and all(z>=0 for z in ds+dd)
    assert ff==fs and ee==edges and ve==Vt.subs(t,EPS) and je==Jt.subs(t,EPS)
    ge=je/ve;mm=mechanics(end,tt,ee,ge)
    assert mm['zero_primitives']==0 and mm['weak_packets']==[]
    for key in ('S','U','H'):assert mm[key]==old[key]
    # Check all literal vertex equations of the full shape-stress transpose.
    al=s.Matrix(s.symbols('alpha0:4'));F,c=endpoint_forces(X,CONTACTS,al)
    assert simp(R0.T*al-s.Matrix.vstack(*(F[j]-A[j].T*c for j in range(len(X)))))==s.zeros(30,1)
    H=sum((m*h for m,h in zip(s.symbols('m0:6'),SYMBASIS)),s.zeros(3))
    RH=shape_matrix(X,A,CONTACTS,H)
    assert simp(RH.T*al-s.Matrix.vstack(*(H*F[j]-A[j].T*H*c for j in range(len(X)))))==s.zeros(30,1)
    assert len(guards)==225
    return {'interval':[0,EPS],'velocity':vel,'radial_centroid_first':radg,
            'actual_volume_polynomial':Vt,'actual_first_moment_polynomial':Jt,
            'volume_first':v1,'centroid_first':g1,'centroid_second':g2,
            'all_guards':guards,'weak_quotient_numerators':weak_quotients,
            'endpoint':{'vertices_raw':end,'vertices_own_centered':[x-ge for x in end],
                        'volume':ve,'centroid_raw':ge,'covariance':simp(re/ve-ge*ge.T),
                        'positive_fans':[ds,dd],'mechanics':mm}}

def build():
    forests=forest_certificates();records=[];chosen=None
    for h in HEIGHTS:
        r,*data=fixture(h);records.append(r)
        if h==-Q(7,2):chosen=data
    X,fs,tri,edges,V,A,old=chosen
    assert V==Q(125,18) and A[8].det()==Q(217561,562500000)
    # Exact derivation of d(h), explicitly limited to its original true chamber.
    hh,dd=s.symbols('h d');Y=X.copy();Y[8]=s.Matrix([dd,0,hh]);Y[9]=s.Matrix([-dd,0,hh])
    vf,jf,_,_=mass(Y,tri,second=False)
    assert simp(vf+(18*dd*hh-9*dd+21*hh-94)/27)==0
    assert jf[:2,0]==s.zeros(2,1)
    assert simp(jf[2]+(36*dd*hh**2-9*dd*hh-9*dd+21*hh**2+12*hh-344)/108)==0
    adj=adjacent_identity(X,tri,V,A);arc=certified_arc(X,fs,tri,edges,V,A,old)
    M,v,moves,active=affine_regularizer(X,tri,edges,CONTACTS)
    assert M==I and moves==[] and active==CONTACTS
    assert shape_matrix(X,A,CONTACTS)*s.Matrix.vstack(*v)==s.ones(4,1)
    return {'identity':'FREE_VERTEX_FOUR_A_AFFINE_SHAPE_REGULARIZATION_V1','parent':[PARENT,PARENT_SHA],
            'scope':'Analytic theorem: <=4 simple A with any free vertex on a simplicial own-COM body. Actual fixtures do not realize obstructing full shape stress or singular free folds.',
            'forest_algebra':forests,'rising_pair_chamber_polynomials':{'V':vf,'J':jf},
            'actual_records':records,'full_adjacent_moment_identity':adj,'certified_arc':arc,
            'generic_constructor_smoke_test':{'metric':M,'velocity':v,'premoves':moves}}

def main():
    assert sys.argv[1:] in (['build'],['check'])
    obj=build();b=(json.dumps(enc(obj),sort_keys=True,separators=(',',':'))+'\n').encode()
    assert len(b)==181974 and hashlib.sha256(b).hexdigest()=='e88a440b55d6fd58eb3a684945c47f9a6dccbaeff148b64ee30297e65cc507d6'
    path=Path('free_vertex_four_a.json')
    if sys.argv[1]=='build':path.write_bytes(b)
    else:assert path.read_bytes()==b
    guards=obj['certified_arc']['all_guards'];coeff=sum(len(g[-1]) for g in guards)
    assert len(guards)==225 and coeff==1376
    print('ALL_19_ROOTED_FOUR_EDGE_FORESTS_NULLITY_AT_MOST_ONE_PASS')
    print('POSITIVE_SINGULAR_FOUR_EDGE_AND_SIX_EDGE_NULLITY_TWO_GRAPH_CONTROLS_PASS')
    print('FOUR_ACTUAL_FOUR_A_FREE_EDGE_BODIES_AND_WRONG_CHAMBER_CENTER_CONTROL_PASS')
    print('COMPLETE_ADJACENT_MIXED_VOLUME_QUADRATIC_AND_MOMENT_CUBIC_PASS')
    print('WHOLE_0_LT_T_LE_1_65536_STRICT_8_6_12_WEAK000_PASS')
    print('GUARDS',len(guards),'POSITIVE_BERNSTEIN_COEFFICIENTS',coeff)
    print(path.name,len(b),hashlib.sha256(b).hexdigest())
    print('FREE_VERTEX_FOUR_A_AFFINE_SHAPE_REGULARIZATION_RECOVERY_PASS')
if __name__=='__main__':main()
```
