# minimum-0117

Historical AI scientific report · saved 2026-09-20 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# VERTEX_STAR_CENTROID_RANK2_FOLD_AND_PURE_A_RESCUE_V1

## 1. Resolution of the vertex-controllability question

**A freely movable true simplicial vertex need not have a nonsingular uniform-volume-centroid Jacobian. The failure already occurs at degree five, in an exact seven-vertex convex polytope.** The example is genuinely nonplanar, noncentral, uniformly filled, and evaluated at its own volume centroid. Its singularity is a fold: with all other vertices fixed, one side of a nearby centroid target is actually unattainable. This is an all-orders local limitation of that one-vertex actuator, not merely a vanishing first jet.

The obstruction is sharply limited by a new general theorem. For **every** vertex whose incident maximal facets are triangles, at **every degree**, the centroid Jacobian has rank at least two. A tensor formed from the true incident cone is always invertible with positive determinant. It reduces centroid singularity to one scalar equation. Every singular case has either a nonzero transverse quadratic term, hence a fold, or a strictly nonzero transverse cubic term. The latter still provides local centroid controllability, although not a differentiable inverse. Higher-order flatness in this transverse direction is excluded.

The resulting pure-A regularization theorem covers arbitrary numbers of simple A contacts, and hence four, whenever the free vertices jointly control all three centroid coordinates. It also covers the transverse-cubic alternative, oppositely directed free folds, and a fold that can be unlocked using one scalar motion of a single-contact endpoint. These are complete continuous geometric sectors with no degree bound, symmetry premise, or zero-direction tensor-stress hypothesis. A further exact identity characterizes the stresses of the **full genuine shape derivative**, and yields a second-order rescue even for some one-sided folds.

For the exact degree-five fold, two coordinates of that vertex and one coordinate of a second vertex already have a nonsingular centroid-control minor. A separate explicit two-vertex curve keeps the true centroid exactly constant, crosses from positive to negative one-vertex determinant, and preserves the entire lattice and strict mechanics on a proved closed interval. Thus the fold does **not** obstruct general shape regularization.

**The example is strict233/weak000, not a four-A body and not weak110. General simplicial pure-A all4 remains open in the precisely stated residual configurations below; mixed A/B and the earlier VF remainder are not closed.** There is no new attaining body, lower-bound change, catalogue subtraction, or general barrier≥5 assertion. The inherited bracket remains **34≤C_min≤622** and the first open minimum layer is10/17/9. :contentReference[oaicite:0]{index=0}

## 2. Input authority and what was actually read

The new `research-journal(20260919-154628).md` was read consecutively from line1 through line1845 and EOF, including the complete shared notebook, branch memory, literal parent and its complete recovery stream. The file has325895 bytes and SHA-256 `dd9dd66ee88869225ff097275d36be220addd841d36a8ab7f44f869b83ff9b71`.

The authoritative parent is `minimum-0114`, **FACET_MOMENT_AND_DEGREE4_VERTEX_OWN_COM_ACTUATORS_V1**,63488 bytes, SHA-256 `be6f8c354f3fc1dee4427ab7081abd98d0b34646ca7a7c72eda409ab5f313bfb`. Its degree-four and planar-cap theorems remain valid. In particular, the new degree-five fold is outside those hypotheses and does not contradict the parent's indefinite-symmetric-part control with positive determinant. :contentReference[oaicite:1]{index=1}

The parent envelope was authenticated from its literal journal payload. The separately mounted convenience `centroid_actuator/result.json` has different serialized bytes; comparison showed citation/link rendering and an input-list clarification, not a mathematical or coordinate conflict. The literal journal payload retains authority; no parent was repinned.

The predecessor executable gap was already closed by this parent. Its complete literal recovery contains the unchanged `four_vf_sectors.py` and `tetra_four.py`, together with `actuator.py` and the optional probes. No old malformed or truncated immutable payload is silently repaired again. The present exact program has **no import from any predecessor**, no missing computational dependency, and all its inputs are included below. Unchanged earlier sources are retained as inherited evidence rather than described as newly replayed suites. The old numerical determinant probes are not used as proof. :contentReference[oaicite:2]{index=2}

The new analytic arguments below use true boundary integration, elementary cone geometry, the inverse/implicit-function theorem and finite-dimensional strict separation. No external research result is invoked as a proof of the new assertions, and no literature-priority or proof-assistant certification is claimed.

## 3. Universal true-star tensor: all valences, rank at least two

### 3.1 Definitions from actual geometry

Let P be a full-dimensional convex3-polytope, uniformly filled, with volume V>0 and actual centroid g. Let w be a true vertex and suppose **every maximal facet incident to w is triangular**. Other facets of P need not be triangles for this one-vertex theorem.

Write its true neighbors in cyclic order as v₁,…,vₘ, m≥3, and set rᵢ=vᵢ−w, with cyclic indices. Choose the orientation so that

    cᵢ=rᵢ×rᵢ₊₁

points inward to the tangent cone Γ=cone{r₁,…,rₘ}. Define

    a=Σᵢ cᵢ,
    S=Σᵢ(rᵢ+rᵢ₊₁)cᵢᵀ,
    r=4(g−w),
    ℓ=aᵀS⁻¹,    η=ℓr−1.                                (1)

Here S is a star tensor, not an equilibrium count. The use of S⁻¹ is justified by the theorem below. The cone facets are precisely the pairs of consecutive rays. For each i, cᵢ·rⱼ≥0, with equality precisely at j=i,i+1. This is where the hypothesis on **maximal** triangular incident facets matters.

No deletion cap is assumed planar, and no degree-four two-triangle description is extrapolated. If K=conv(other vertices) is full-dimensional, its visible boundary can have many faces. Each newly exposed facet uses true neighbors of w: a supporting functional whose value at w is larger than on K must have an increasing true edge from each exposed vertex toward w. Those actual visible facets may be triangulated for integration, but their diagonals are never asserted to be mechanical edges. The proof below works directly with the original true incident ring.

### 3.2 The cone theorem

**The tensor S is nonsingular and det S>0.** Moreover a lies in the interior of Γ*, r lies in the interior of Γ, and aᵀr>0.

First, tr S=0 because each cᵢ is perpendicular to rᵢ and rᵢ₊₁. Also

    Sx=Σᵢ(cᵢ·x)(rᵢ+rᵢ₊₁)

maps Γ∖{0} into Γ∖{0}. If m≥4, applying S to an extreme ray gives a positive combination containing at least three distinct rays. Such a combination is interior: no actual cone facet contains three distinct rays. Hence S maps every nonzero point of Γ into its interior. For m=3, S maps each ray to a positive combination of the other two, so S² maps every nonzero cone point into its interior. In all cases S² is strongly cone-positive.

For completeness, the needed spectral argument can be obtained without assuming symmetry of S. On the compact convex base {x∈Γ:a·x=1}, the map x↦Sx/(a·Sx) has a fixed point by Brouwer’s fixed-point theorem. Thus Sv=λv with λ>0; strong positivity of S² forces v∈intΓ. The order-unit norm defined by −cv≤Γx≤Γcv gives ||S||≤λ, so every eigenvalue has modulus at most λ.

If S were singular, its trace zero and eigenvalue λ would force the remaining eigenvalues to be0 and−λ. A real eigenvector z for−λ is independent of v. Choose a nonzero boundary point v+tz of Γ. But S²(v+tz)=λ²(v+tz) remains on the boundary, contradicting strong positivity. Therefore S is invertible. Its other two eigenvalues are either a conjugate pair with positive product, or two negative real numbers: a second positive real eigenvalue would force the third below−λ. Consequently det S>0.

This is a statement about the genuine cone of a true triangular star. It is not inferred from a formal stress array or a finite determinant census. It does **not** say S is symmetric, that S⁻¹ preserves the cone, or that ℓ is nonnegative on Γ. The exact example below explicitly disproves the last possible shortcut.

### 3.3 Exact uniform-centroid Jacobian

Let A_w=D_wg denote the derivative when only w moves and the other vertices stay fixed. The outward area vector of triangle(w,vᵢ,vᵢ₊₁) is−cᵢ/2. Actual surface first variation, or exact tetrahedral integration, gives

    A_w=(r aᵀ−S)/(24V),
    det A_w=det S·(ℓr−1)/(24V)³.                          (2)

Indeed, the triangle's contribution is

    (2w+vᵢ+vᵢ₊₁−4g)(−cᵢᵀ)/(24V),

and summing yields(2). The determinant is the rank-one determinant identity applied to−S.

It follows that **rank A_w≥2 for every such vertex, at every degree**. It is nonsingular exactly when η≠0. If η=0, define

    k=S⁻¹r,    aᵀk=1,    ρ=ℓk=aᵀS⁻²r.                  (3)

Then ker A_w=span{k}, the left kernel is span{ℓ}, and rank A_w=2. Also

    D_wV=−aᵀ/6,    D_wV·k=−1/6.                          (4)

Therefore the combined derivative of (V,g), with three vertex coordinates as input, **always has rank three**, even at a centroid singularity. One vertex can always control volume and two independent centroid coordinates; it does not control four independent outputs.

For a fixed true star, the entire effect of the rest of the uniformly filled body on this singularity is the scalar condition

    ℓ·(g−w)=1/4.                                         (5)

The center in(5) is the actual integrated centroid. The equation does not authorize choosing a reference on that plane. Affine changes of chart conjugate A_w, so the rank and determinant sign statements are coordinate invariant. No independent polar mass or metric is used.

## 4. Exact nonlinear structure: regular, fold, or transverse cubic

### 4.1 A quadratic first-moment identity

Fix the original actual centroid g and displace only w by h. Inside the same face-lattice chamber, the **exact** uniformly refilled moments satisfy

    V(h)=V−a·h/6,
    J(h)−gV(h)=[Bh−(a·h)h]/24,
    B=r aᵀ−S=24VA_w.                                    (6)

This is not a truncated Taylor series. Volume is affine and first moment is quadratic in one moving vertex. One way to derive it is to decompose the actual added cap over the fixed visible faces of K. Each cell has an affine volume and centroid(w+three fixed vertices)/4; its quadratic contribution is h(D_wV·h)/4. Alternatively the unchanged oriented boundary integration gives the same identity, including the case in which K is planar. The exact program below independently checks all three components for arbitrary h in the counterexample.

At a singular vertex, the kernel-line formula is particularly simple:

    g(w+sk)−g=−s²k/[24(V−s/6)].                           (7)

A first-order zero can therefore have a real second-order mass effect.

### 4.2 Complete transverse alternative

At η=0, use ξ=a·h as kernel coordinate and write h=ξk+z, with a·z=0. The restriction B:ker aᵀ→kerℓ is an isomorphism. Choose a projection Π onto kerℓ. The two tangential centroid equations are equivalent to

    Π[Bz−ξ²k−ξz]=0.

They solve uniquely for z=z(ξ) near0, with z=O(ξ²). On this exact tangential-zero fiber,

    ℓ·(g(h)−g)=−ρξ²/(24V)+O(ξ³).                         (8)

If **ρ≠0**, this has the fixed sign−signρ for every sufficiently small nonzero ξ. Thus centroid targets on the opposite normal ray, with tangential target zero, are not in the image of any sufficiently small movement of this one vertex. This proves a genuine local **fold barrier for the one-vertex actuator**, not just absence of a positive first or second jet. It says nothing by itself about moving other vertices.

If **ρ=0**, then k∈kerℓ and

    z(ξ)=−ξ²S⁻¹k+O(ξ³).

Using tr S=0 in Cayley–Hamilton,

    S³+σ₂S−det(S)I=0,    σ₂=−tr(S²)/2,
    aᵀS⁻³r=[aᵀr+σ₂ρ]/det S,

so the normal component instead satisfies

    ℓ·(g(h)−g)= [aᵀr/(24V det S)]ξ³+O(ξ⁴).               (9)

Its cubic coefficient is strictly positive. In particular the centroid map is locally open at this singularity. Solve the two tangential equations first; the opposite signs at ξ=±ε then give every sufficiently small normal target by the intermediate-value theorem. The same argument survives sufficiently small prescribed changes of the other vertices. For a prescribed O(τ) perturbation, ξ=±τ^(1/4) gives cubic terms dominating that perturbation and produces compensators tending to0.

This proves the full local alternative: **nonsingular, fold, or nonflat transverse cubic**. There is no further fourth-or-higher-order flat transverse case. A differentiable inverse, a unique analytic inverse, and an actually constructed cubic example are **not** asserted in the cubic case. The theorem covers any genuine occurrence; the exact constructed singularity below is a fold.

## 5. Consequences for genuine pure-A regularization

In this section P is fully simplicial, has its own uniform centroid0, and its only weak physical points are k simple A contacts xᵢ→yᵢ. All other strict or inactive physical guards are fixed initially. A vertex is called free only when it is **neither endpoint of any weak edge**.

For each contact, put rᵢ=|xᵢ|² and sᵢ=|yᵢ|². Prescribing both endpoints radially gives

    xᵢ(t)=(1+trᵢ)xᵢ,  yᵢ(t)=(1+tsᵢ)yᵢ,
    xᵢ(t)·(yᵢ(t)−xᵢ(t))=trᵢ(sᵢ−rᵢ)(1+trᵢ)>0.          (10)

Whenever the actual centroid is kept exactly0, these positive functions remove the complete simple physical contacts. Simpliciality and smallness preserve all maximal triangles and true edges. Every old strict feature retains its strict guards, and every other inactive feature retains a chosen strictly positive excluding guard. Hence no new strict or weak equilibrium appears. Harmless primitive zeros do not have to disappear individually. No VF packet is represented by one selected scalar in these theorems.

### 5.1 Joint free-vertex control, without a valence bound

Let U be the free vertices. If the block matrix

    [A_w : w∈U]

has rank three, prescribe the other vertices, choose an invertible three-column minor, and solve the true centroid equations by the analytic implicit-function theorem. This keeps J=0 exactly and proves arbitrary-small regularization through(10).

The universal rank theorem makes the exact residual clear. For nonempty U, block rank can be below three **only when every free vertex is singular and all its left-kernel covectors ℓ_w are proportional**. One nonsingular free vertex, of any degree and either determinant sign, suffices. Two singular free vertices with different left-kernel lines also suffice. This is a full geometric theorem, not a sampled genericity claim.

Any free vertex in the transverse-cubic case of(9) also suffices, even if the block derivative has rank two. The preceding local-openness argument solves the actual centroid after the prescribed radial motion, with a compensating displacement tending to0. A single analytic parametrization is not needed for the arbitrary-small existence statement.

### 5.2 Oppositely directed folds

Suppose the block rank is two with common left covector ν. Normalize each free kernel vector by a_w·k_w=1. If two free vertices w,z have

    (ν·k_w)(ν·k_z)<0,                                    (11)

they still jointly control the centroid locally. On a pure kernel displacement at w the missing normal coordinate has quadratic coefficient−ν·k_w/(24V), and the corresponding coefficient at z has the opposite sign. Correcting the two tangential centroid coordinates changes neither normal quadratic coefficient. Thus the reduced scalar takes both signs arbitrarily near0. After a small prescribed motion of the other vertices, the same tangential implicit-function and intermediate-value argument restores the actual centroid. This again gives regularization through(10).

These are genuine nonlinear shape controls. Rank-two block data are not automatically a regularization obstruction.

### 5.3 Unlocking a free fold with a single-contact endpoint

There is another complete sector that does not require a second free vertex. Let w be a free fold, η_w=0 and ρ_w≠0. Let z≠w belong to at most one weak A edge, and let E_z be its allowed tangent space while that contact is kept exactly zero:

    E_z=R³                       if z is free;
    E_z=x⊥                       if x→z is its only contact;
    E_z=(y−2z)⊥                  if z→y is its only contact.

The target constraint x·z=|x|² is a plane. The source constraint z·(y−z)=0 is the smooth sphere centered at y/2 with radius |y|/2. Thus every h∈E_z is the tangent of an actual local curve preserving that contact exactly.

**If there exists h∈E_z with ℓ_w A_z h≠0, the whole pure-A body regularizes.** Two complementary coordinates of w and this one parameter at z have a rank-three centroid derivative. Prescribe the kernel movement sk_w and solve those three controls for actual centroid0. Their corrections are O(s²), so all original weak contact equalities remain exact. The old strict/inactive guards stay open.

This preliminary curve makes w nonsingular. To see the sign rather than invoke genericity, differentiate(6) at fixed centroid. At s=0,

    B'(0)=−(k_w a_wᵀ+I),
    adj(B)=det(S_w) k_wℓ_w,
    d/ds det A_w =−2det(S_w)ρ_w/(24V)³ ≠0.                (12)

The auxiliary endpoint changes only at O(s²), so it does not alter this derivative. Fix an arbitrarily small nonzero s, then apply the radial one-free-vertex construction. This is an exact contact-preserving prestep followed by a true constant-centroid rescue, not a statement that the original global projective first jet was positive.

A vertex incident to several weak edges needs the tangent space of their genuine common zero set and a separate smoothness argument; that extension is not silently included here.

### 5.4 Actual shape stresses and an additional second-order rescue

The full genuine shape derivative has a useful physical identity. At g=0, for arbitrary vertex velocities δv_j,

    δφᵢ=(uᵢ−xᵢ)·δxᵢ+xᵢ·δyᵢ−uᵢ·ΣⱼAⱼδvⱼ,
    uᵢ=yᵢ−xᵢ.                                           (13)

If there is no simultaneous positive first shape derivative, the finite strict alternative gives αᵢ≥0, not all zero, such that, with c=Σαᵢuᵢ,

    Σ_{i:source i=j}αᵢ(uᵢ−xᵢ)
      +Σ_{i:target i=j}αᵢxᵢ = Aⱼᵀc       for EVERY j.     (14)

Necessarily c≠0. Otherwise dot(14) with radial velocities |v_j|²v_j and sum: the left side is Σαᵢ|xᵢ|²|uᵢ|²>0, while the right side is0. Affine and genuine uniformly refilled projective velocity fields also force

    Σαᵢ sym(xᵢuᵢᵀ)=0,
    5Σ_P c=Σαᵢ|xᵢ|²uᵢ.                                 (15)

For every free w, (14) forces A_wᵀc=0. Thus every actual first-shape stress requires all free vertices to be critical in the same covector direction. Equations(14) are stronger than a formal global tensor stress: they include the genuine uniform centroid Jacobian of **every vertex of the same body**.

Even such a first-order stress need not obstruct regularization. Move a free singular vertex along sk while leaving all endpoints fixed, and then subtract the **actual** new centroid. Equation(7) gives second contact coefficients

    bᵢ=(k·uᵢ)/(24V).

Let K_shape be the entire cone of nonnegative stresses of(13). If

    (Σαᵢuᵢ)·k>0  for every nonzero α∈K_shape,             (16)

a second-order genuine vertex correction makes all contacts positive. Indeed α·b>0 on the full stress cone, so strict separation supplies δ with b+R_shapeδ>0. Using vertex corrections s²δ and recomputing the true centroid gives φᵢ(s)=s²(b+R_shapeδ)ᵢ+O(s³)>0. This path need not keep the raw centroid fixed; it is evaluated at its own exact new centroid throughout. A single chosen stress is insufficient when the cone has more than one ray.

Equations(14)–(16) are a necessary first-order identity and a sufficient second-order theorem, respectively. Neither failed stress testing nor a vanishing jet is an all-orders exclusion.

### 5.5 Precise uncovered pure-A complement

For four contacts, at most eight vertices are endpoints. A simplicial body with at least nine vertices therefore has a free vertex, but **this alone no longer proves control**, because of the genuine degree-five fold.

After the new sufficient sectors, a still-unresolved body with a nonempty free set must have every free vertex a fold, all free left-kernel covectors proportional, no pair satisfying(11), and no single-contact endpoint satisfying the unlocking criterion. It must also fail the sufficient second-order condition(16) if no positive first shape derivative exists. The full physical compatibility of this residual with(14) is not resolved here. Bodies with no free vertex also remain unless covered by previously accepted theorems. This is a localization of the remaining problem, not a claim that a residual body exists.

## 6. Exact nonplanar degree-five fold family

### 6.1 Literal vertices and all-parameter true geometry

For t>0 take the uniformly filled hull of these **raw Euclidean** vertices, in the displayed order:

    v0=(0,0,0),             v1=(1,0,0),
    v2=(0,1,0),             v3=(10,0,1),
    v4=(0,9,1),             w=v5=(−1/10,−1/10,−1/10),
    v6=(11t,11t,10t).                                     (17)

Subtract the actual centroid below to obtain the physical ownCOM0 body. For **every t>0**, the true f-vector is(7,15,10), C=30, and all maximal facets are triangles. Their sorted vertex sets are

    (0,3,5),(0,3,6),(0,4,5),(0,4,6),(1,2,3),
    (1,2,5),(1,3,5),(2,3,4),(2,4,5),(3,4,6).             (18)

The source recovers all orientations and the fifteen actual edges from exhaustive supporting triples. Forty nonincident supporting polynomials are nonzero with nonnegative coefficients, proving strict support for the whole t>0 family. The two actual positive vertex fans, from v0 and v5, agree on volume, first moment and second moment; selected zero cones are retained as zero, not converted into mechanical edges.

The degree-five vertex w has true ring(0,3,1,2,4). Its neighbors are noncoplanar. Deleting w exposes exactly the three true triangles(0,1,2),(0,1,3),(0,2,4); the removed volume is1/20. This is a real higher-degree visible cap, not an artificial two-triangle reduction. The whole body is noncentral, already because it has an odd number of true vertices.

Put D=6910t+113. The actual uniform moments give

    V=D/60,
    g_x=(760100t²+691000t+11217)/(40D),
    g_y=(760100t²+621900t+10207)/(40D),
    g_z=(691000t²+138200t+2117)/(40D).                     (19)

All subsequent derivatives are derivatives of this actual uniformly filled body, with other vertices fixed when A_w is evaluated. They are not derivatives along the t-family: t moves v6, whereas A_w concerns v5.

### 6.2 Star tensor, exact root and singular Jacobian

For w, (1) gives the t-independent data

    a=(1,1,1),
    S=[[0,113/10,13/10],[103/10,0,13/10],[13/10,13/10,0]],
    det S=4563/125,
    ℓ=(515/1404,565/1404,−44155/18252).                   (20)

In particular

    ℓ·(v0−w)=−6023/36504<0.

Thus ℓ is not cone-positive, despite cone positivity and invertibility of S. Replacing it by a positive moment weight is a false architecture.

The **true** Jacobian determinant is

    det A_w=−F(t)/[64(6910t+113)⁴],
    F(t)=3967860200t²−199657540t−4471071.                  (21)

There is exactly one positive root,

    t*=14447/574220+sqrt(277063679919871)/396786020.        (22)

The other root is negative. Thus det A_w is positive on0<t<t*, zero at t*, and negative on t>t*. At t*, rank A_w=2 by the universal theorem and by an explicit nonzero2×2 minor. All coordinates in(17)–(22) are exact; the approximate value0.0671094887489693 is orientation only.

At t*, let r=4(g−w), k=S⁻¹r. The exact quantity

    ρ=5(54893591556200t²+775607988620t−2078245743)
         /[666271008(6910t+113)]                         (23)

is strictly positive after t=t*. Its approximate value is3.86715657450760. Hence this is the fold case of(8), not the cubic case. The complete k and A_w matrices are regenerated from(17)–(20), without a stored numerical null vector. The entire five-neighbor star and its cone remain unchanged as t varies; only the nonneighbor v6 moves. Its actual added volume and first moment carry g across the critical plane(5). Thus local star convexity alone cannot supply the missing centroid inequality.

The source isolates t* by80 exact bisections starting with[671/10000,672/10000], giving

    lo=811303936897664519234976783/12089258196146291747061760000,
    hi=50706496056104032452186049/755578637259143234191360000.

Quadratic-field identities are reduced modulo F, and nonzero signs are checked on the resulting linear remainders over this rational isolating interval. Denominators are checked before zero numerators are accepted.

### 6.3 Complete physical mechanics, not an invented weak110 seed

On the **whole closed interval**671/10000≤t≤672/10000, all sixty true edge primitives are nonzero and have constant signs. At the actual ownCOM, with the facet order(18),

    strict S facets=[7,9],
    strict U vertices=[3,4,5],
    strict H edges=[(3,4),(3,5),(4,5)].                    (24)

There are no physical weak points: weak000. Every VE/EF/VF packet would force a zero among the true primitives, so this excludes all of them, not merely a selected feature description. Consequently the singular centroid Jacobian is **not a weak mechanical equilibrium**. The body is strict233 throughout this interval, including at t*, and is neither110 nor a four-contact regularization counterexample.

The sixty rational sign guards have120 numerator/denominator polynomial certificates,499 strictly positive exact Bernstein coefficients and maximum degree6. This is a continuum proof, not a finite t-grid.

## 7. A true constant-centroid shape curve through the fold

### 7.1 Only three control coordinates already suffice

Let A₆ be the actual centroid derivative of the degree-three tip v6. For every t>0,

    det[A_w e1,A_w e2,A₆ e1]
      =−(491805430000t³+54098597300t²+1529729300t+12045033)
          /[64(6910t+113)⁴] <0.                          (25)

Thus two coordinates of w and just one coordinate of the tip give an invertible centroid control, including exactly at the fold. This is a specific realization of the rank-two-plus-one-scalar mechanism. The tip's own determinant is also positive:

    det A₆=11937025t²(47748100t²+1561660t+12493)
                 /[16(6910t+113)⁴].                      (26)

A singular one-vertex derivative does not make the actual shape family uncontrollable.

### 7.2 An explicit exact curve, not only an implicit jet

For a convenient literal constant-centroid curve, fix t=t*, all quantities in(17)–(23), and g*=g(t*). Let

    n=(−9,−10,90),   δ₀=n·v6=691t*,
    svec=v3+v4−4g*,  b=n·svec.

The true tip-base triangle is(0,3,4), lies in n·x=0, and has area91/2; |n|=91. For

    −2⁻²⁰≤u≤2⁻²⁰

define

    w(u)=w+uk,
    Δ(u)=[−b+sqrt((2δ₀+b)²+4(n·k)u²)]/2,
    v6(u)=−svec+[δ₀(v6+svec)+ku²]/Δ(u).                  (27)

Every other vertex is fixed. Finally subtract the **fixed true g*** from every point. The square root is the positive branch; 2δ₀+b>0 and Δ>0 are proved. All rational expressions in t are evaluated at the single positive algebraic root(22).

Here is the actual moment verification. Let K(u)=conv(v0,…,v5(u)), the true body with tip6 deleted. The base(0,3,4) remains a true facet and the tip ear remains a genuine disjoint pyramid. Write its core moments V_K,J_K. The kernel relation and(6) give, exactly,

    V_K(u)=V_K(0)−u/6,
    J_K(u)=J_K(0)−g*u/6−ku²/24.                          (28)

The scalar equation for Δ is

    Δ²+bΔ=δ₀(δ₀+b)+(n·k)u².

It implies n·v6(u)=Δ. The new ear therefore has actual volumeΔ/6 and actual first momentΔ(v6(u)+v3+v4)/24. Combining with(28),

    J_K(u)+Δ(v6(u)+v3+v4)/24
       =g*[V_K(u)+Δ/6]                                  (29)

identically. Thus the actual uniform centroid is g* at **every** point of this curve. This is not the centroid of the polar, a moving chosen reference, or a first-order centering approximation. The tip has v6'(0)=0; its genuine second-order shape change compensates the fold's mass displacement.

At this constant centroid the exact varying one-vertex determinant is

    det A_w(u)=−2u[u²−(a·r)u+det(S)ρ]/[24V(u)]³.          (30)

The bracket and V(u) are strictly positive on the whole stated interval. Hence the determinant is positive for u<0, singular at0, and negative for u>0, while the true center and every strict mechanical feature remain unchanged.

### 7.3 Whole-interval certification

The source proves142 strictly positive rational interval guards over the whole closed u-interval and the exact isolating interval for t*. These comprise the full body's forty nonincident supports, ten interior-centroid plane guards and sixty signed true primitives, plus the deleted-tip core's twenty-four nonincident supports and eight interior-reference guards. The latter reference is its vertex average used only to orient and check its geometry, **not** substituted for its uniform centroid in(28)–(29).

Square-root enclosures use outward-rounded rational intervals on a fixed100-bit binary grid. Volume, Δ, the discriminant branch and the bracket in(30) are also checked positive. The exact polynomial identities(28)–(30) are independently expanded and reduced modulo F in the code. There is no reliance on an interval enclosure alone to establish the centroid equality.

All maximal facets and true edges therefore remain those of(18), all sixty primitive signs remain those of(24), and the centered body remains strict233/weak000 on the entire curve. This is an actual geometric bypass of the one-vertex fold, not a proof of universal pure-A all4.

## 8. Preserved nonwinning controls and method boundaries

The recovery includes three separate finite rational bodies, their actual hulls, complete true moments, covariance, all edge primitives and feature lists.

1. In(17), t=1/100 gives V=607/200,

    g=(606767/242800,550067/242800,35681/72840),
    det A_w=7588575475/87969023309448>0.

It is simplicial7/15/10, strict233/weak000.

2. In(17), t=1/10 gives V=67/5,

    g=(14653/5360,199/80,341/480),
    det A_w=−15241777/26742633283584<0.

It is another simplicial7/15/10, strict233/weak000. This is a rational negative-determinant control separate from the algebraic singular body.

3. The initial symmetric architecture replaces v4 by(0,10,1) and takes t=1/10. Its true f-vector is7/14/9, with the genuine quadrilateral(1,2,3,4); it is **not globally simplicial**. It has V=893/60,

    g=(97797/35720,97797/35720,1343/1880),
    det A_w=−22259079/40699194086464,

and strict233/weak000. The local star at w is still triangular. This preliminary failure of the intended global simplicial architecture is preserved, not silently renamed as the accepted body. Changing the9-coordinate in(17) is a real geometric change that removes that quadrilateral.

The cone-positive S nevertheless has non-cone-positive ℓ in(20). The parent's indefinite symmetric part did not show a singular derivative; the new determinant sign change does. Individual tetrahedron-centroid references and numerical failures remain inappropriate substitutes for actual ownCOM. No random determinant census was performed or promoted in this continuation.

The remaining scientific uncertainty is not the blanket nonsingularity conjecture—it is disproved—but whether the unresolved co-aligned free folds can coexist with the true four-A shape-stress equations in a body that also defeats all available alternative controls. No example with that full conjunction is supplied.

## 9. Execution, recovery and consequences for the minimum problem

The universal cone/rank and nonlinear-classification arguments are analytic. The finite exact computation establishes the literal bodies, root, masses, determinant identities, complete mechanics and continuous control curve. Neither direction is inferred solely from a PASS marker.

The final source was executed with **CPython3.13.5, SymPy1.14.0, assertions enabled, PYTHONHASHSEED=0**. It requires no other package, input file, numerical seed, solver or old module. Build and exact-recomputation check both completed. The final source was then copied alone into a fresh directory; separate cold build and cold check completed, and source, complete report and stdout matched byte-for-byte. Earlier combined calls that timed out are not counted as completed checks. An implementation-stage exact-expression comparison and an interval reverse-division helper were corrected before this frozen version; neither was a mathematical counterexample or an accepted object. No predecessor full suite or C622 audit was rerun here.

Save the complete next source as `vertex_fold.py`, UTF-8/LF with one final LF. Run:

```bash
export PYTHONHASHSEED=0
python vertex_fold.py build > build.txt
python vertex_fold.py check > check.txt
cmp build.txt check.txt
```

|File|Bytes|SHA-256|
|---|---:|---|
|vertex_fold.py|16692|c170ec179b96f692a3e2cb6d9a3cf6530b076912e9d5169b18658356183c0abc|
|vertex_fold.json|209180|71854d14d7d3ed1d8d94f9d223765f4c600ebd139f6d381615405b7d981c6746|
|build.txt or check.txt|368|8592c3dcfb02fdd324a6c4792fce5386238f091f650bb177e9bb1a6bf24ace2b|

The complete deterministic stdout is:


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]


The actual additional byte-comparison marker was `VERTEX_FOLD_SOURCE_ONLY_COLD_BYTE_PARITY_PASS`. The report includes every pole/edge/primitive, both positive fans, full covariance, all exact Bernstein arrays, all interval bounds, the complete kernel/Jacobian matrices and all three preserved controls. They reconstruct from the following one complete source; a hash or link is not the recovery input.

For weak110, the new sufficient pure-A sectors would turn a genuine seed into proper110 with the same lattice and C, but no such seed is produced. The seven-vertex C30 controls have three strict unstable vertices and two stable facets, so they do not challenge the accepted lower chain for110. The simple pure-B/F≥9 theorem is already settled by the parent and is not reannounced as new. The nonsimple10/17/9 minimum layer, general all4, mixed contacts, VF residual and all global registry counts are unchanged.

The most useful continuation is the actual compatibility of(14) with a nonempty pool of co-aligned same-side folds, especially when every potential one-scalar endpoint actuator fails. The rank-two theorem and the quadratic/cubic dichotomy reduce this to one genuine missing centroid direction, rather than an arbitrary3×3 determinant problem.

## 10. Complete smallest executable source closure

```python
"""TRUE_VERTEX_CENTROID_FOLD_V1. Exact nonplanar degree-five countercontrol.
CPython 3.13.5, SymPy 1.14.0, assertions enabled; no inputs/RNG/network.
python vertex_fold.py build|check
All source coordinates, root isolation, true hull/masses and interval guards here.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction as Q
from math import comb,isqrt
import hashlib,json,sys
import sympy as s
assert __debug__ and s.__version__=='1.14.0'
R=s.Rational;t=s.Symbol('t');Z=s.zeros(3,1);I3=s.eye(3)
POL=s.Poly(3967860200*t*t-199657540*t-4471071,t)
LOW=R(671,10000);HIGH=R(672,10000)
FACES=[(0,3,5),(0,3,6),(0,4,5),(0,4,6),(1,2,3),(1,2,5),
       (1,3,5),(2,3,4),(2,4,5),(3,4,6)]
RAW=[(0,0,0),(1,0,0),(0,1,0),(10,0,1),(0,9,1),(-R(1,10),)*3]
X=list(map(s.Matrix,RAW+[(11*t,11*t,10*t)]))
def sm(A):return A.applyfunc(s.cancel)
def det(a,b,c):return s.det(s.Matrix.hstack(a,b,c))
def signq(x):return int(s.sign(x))
def hull(X,sg):
    inside=sum(X,Z)/len(X);faces={}
    for i,j,k in combinations(range(len(X)),3):
        n=(X[j]-X[i]).cross(X[k]-X[i]);h=n.dot(X[i])
        if all(sg(v)==0 for v in n):continue
        a=[sg(n.dot(x)-h) for x in X]
        if min(a)<0<max(a):continue
        f=tuple(j for j,v in enumerate(a) if not v)
        if f in faces:continue
        if sg(n.dot(inside)-h)>0:n=-n;h=-h
        faces[f]=(n,h)
    fs=sorted(faces);E={}
    for i,j in combinations(range(len(fs)),2):
        ab=tuple(sorted(set(fs[i])&set(fs[j])))
        if len(ab)==2:
            assert ab not in E;E[ab]=(i,j)
    cyc=[]
    for f in fs:
        adj={j:[] for j in f}
        for a,b in E:
            if a in f and b in f:adj[a].append(b);adj[b].append(a)
        assert all(len(v)==2 for v in adj.values())
        p=min(f);row=[p,min(adj[p])]
        while len(row)<len(f):
            nxt=next(j for j in adj[row[-1]] if j!=row[-2]);assert nxt not in row
            row.append(nxt)
        assert row[0] in adj[row[-1]]
        n=faces[f][0]
        if sg((X[row[1]]-X[row[0]]).cross(X[row[2]]-X[row[0]]).dot(n))<0:
            row=row[:1]+row[:0:-1]
        cyc.append(row)
    assert len(X)-len(E)+len(fs)==2
    assert all(sum(j in e for e in E)>=3 for j in range(len(X)))
    tri=[(c[0],c[k],c[k+1]) for c in cyc for k in range(1,len(c)-1)]
    return fs,cyc,E,tri

def mass(X,tri,apex):
    V=s.S(0);J=Z.copy();Q2=s.zeros(3);ds=[]
    for f in tri:
        verts=[apex]+[X[j] for j in f]
        d=s.cancel(det(*(x-apex for x in verts[1:])));ds.append(d)
        total=sum(verts,Z);V+=d/6;J+=d*total/24
        Q2+=d*(total*total.T+sum((x*x.T for x in verts),s.zeros(3)))/120
    return s.cancel(V),sm(J),sm(Q2),ds

def jac(X,tri,V,g,w):
    A=s.zeros(3)
    for i,j,k in tri:
        if w not in (i,j,k):continue
        n=(X[j]-X[i]).cross(X[k]-X[i])/2
        A+=(X[i]+X[j]+X[k]+X[w]-4*g)*n.T/(12*V)
    return sm(A)

def mechanics(X,fs,cyc,E,V,g,sg):
    Y=[sm(x-g) for x in X];poles=[]
    for c in cyc:
        a,b,d=[X[i] for i in c[:3]];n=(b-a).cross(d-a);h=n.dot(a-g)
        assert sg(h)>0;poles.append(sm(n/h))
    pv=[[] for x in X];dq=[[] for f in fs];rows=[];H=[];zeros=[]
    for (a,b),(f,h) in sorted(E.items()):
        vals=[Y[a].dot(Y[b]-Y[a]),Y[b].dot(Y[a]-Y[b]),
              poles[f].dot(poles[h]-poles[f]),poles[h].dot(poles[f]-poles[h])]
        vals=[s.cancel(z) for z in vals];ss=list(map(sg,vals))
        pv[a].append(ss[0]);pv[b].append(ss[1]);dq[f].append(ss[2]);dq[h].append(ss[3])
        if max(ss)<0:H.append((a,b))
        if 0 in ss:zeros.append([(a,b),ss])
        rows.append({'edge':(a,b),'facets':(f,h),'values':vals,'signs':ss})
    return {'centered_vertices':Y,'poles':poles,'primitives':rows,
            'S':[i for i,a in enumerate(dq) if max(a)<0],
            'U':[i for i,a in enumerate(pv) if max(a)<0],'H':H,'zero_rows':zeros}

def bern(p,lo,hi):
    y=s.Symbol('y');f=s.Poly(s.expand(p.subs(t,lo+(hi-lo)*y)),y)
    n=max(0,f.degree());B=[sum(f.nth(j)*R(comb(k,j),comb(n,j)) for j in range(k+1)) for k in range(n+1)]
    assert all(v>0 for v in B),(p,min(B))
    return B

def positive_guard(expr,lo,hi):
    p,q=s.fraction(s.cancel(expr))
    if q.subs(t,lo)<0:p=-p;q=-q
    return [bern(p,lo,hi),bern(q,lo,hi)]

class IV:
    def __init__(self,a,b=None):
        self.a=Q(a);self.b=Q(a if b is None else b);assert self.a<=self.b
    def __add__(self,o):
        o=iv(o);return IV(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return IV(-self.b,-self.a)
    def __sub__(self,o):return self+-iv(o)
    def __rsub__(self,o):return iv(o)+-self
    def __mul__(self,o):
        o=iv(o);p=[a*b for a in (self.a,self.b) for b in (o.a,o.b)]
        return IV(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=iv(o);assert not o.a<=0<=o.b
        return self*IV(1/o.b,1/o.a)
    def __rtruediv__(self,o):return iv(o)/self
    def sqrt(self):
        assert self.a>0
        d=1<<100
        a=isqrt((self.a*d*d).numerator//(self.a*d*d).denominator)
        b=isqrt((self.b*d*d).numerator//(self.b*d*d).denominator)+1
        return IV(Q(a,d),Q(b,d))
def iv(x):return x if isinstance(x,IV) else IV(x)
def add(a,b):return [x+y for x,y in zip(a,b)]
def sub(a,b):return [x-y for x,y in zip(a,b)]
def mul(c,a):return [c*x for x in a]
def dot(a,b):return sum((x*y for x,y in zip(a,b)),IV(0))
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def iev(expr,T):
    p,q=s.fraction(s.cancel(expr))
    def val(p):
        z=IV(0)
        for c in s.Poly(p,t).all_coeffs():z=z*T+Q(c)
        return z
    return val(p)/val(q)
def viet(A,T):return [iev(z,T) for z in A]

def interval_geometry(Y,center,fs,cyc,E,signrows):
    guards=[];poles=[]
    for f,c in zip(fs,cyc):
        a,b,d=[Y[j] for j in c[:3]];n=cross(sub(b,a),sub(d,a));h=dot(n,sub(a,center))
        assert h.a>0;guards.append(['centroid_inside',f,h])
        for j,x in enumerate(Y):
            if j in f:continue
            slack=dot(n,sub(a,x));assert slack.a>0
            guards.append(['nonincident_support',f,j,slack])
        poles.append([x/h for x in n])
    if signrows is not None:
        Xc=[sub(x,center) for x in Y]
        for row in signrows:
            a,b=row['edge'];f,h=row['facets']
            vals=[dot(Xc[a],sub(Xc[b],Xc[a])),dot(Xc[b],sub(Xc[a],Xc[b])),
                  dot(poles[f],sub(poles[h],poles[f])),dot(poles[h],sub(poles[f],poles[h]))]
            for k,(z,sg) in enumerate(zip(vals,row['signs'])):
                zz=z*sg;assert zz.a>0,(row['edge'],k,zz.a)
                guards.append(['strict_primitive',row['edge'],k,zz])
    return guards

def enc(x):
    if isinstance(x,s.MatrixBase):return [[enc(z) for z in row] for row in x.tolist()]
    if isinstance(x,(s.Basic,Q)):return str(x)
    if isinstance(x,IV):return [str(x.a),str(x.b)]
    if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [enc(v) for v in x]
    return x

def build():
    fs,cyc,E,tri=hull([x.subs(t,R(1,10)) for x in X],signq)
    assert fs==FACES and len(E)==15
    V,J,Q2,ds=mass(X,tri,X[0]);g=sm(J/V)
    for ds0 in [ds,mass(X,tri,X[5])[3]]:
        for d in ds0:
            assert all(c>=0 for c in s.Poly(d,t).all_coeffs())
    v1,j1,q1,_=mass(X,tri,X[5]);assert v1==V and sm(j1-J)==Z and sm(q1-Q2)==s.zeros(3)
    support=[]
    for f,c in zip(fs,cyc):
        a,b,d=[X[j] for j in c[:3]];n=(b-a).cross(d-a)
        for j,x in enumerate(X):
            z=s.Poly(s.expand(n.dot(a-x)),t)
            if j in f:assert z.is_zero;continue
            assert not z.is_zero and all(a>=0 for a in z.all_coeffs())
            support.append((f,j,z.as_expr()))
    A=jac(X,tri,V,g,5);A6=jac(X,tri,V,g,6)
    avec=Z.copy();S=s.zeros(3);ring=[0,3,1,2,4]
    for i,j in zip(ring,ring[1:]+ring[:1]):
        u=X[i]-X[5];v=X[j]-X[5];c=u.cross(v)
        assert all(c.dot(X[k]-X[5])>=0 for k in range(6))
        avec+=c;S+=(u+v)*c.T
    assert avec==s.ones(3,1)
    assert S==s.Matrix([[0,R(113,10),R(13,10)],[R(103,10),0,R(13,10)],[R(13,10),R(13,10),0]])
    assert S.det()==R(4563,125) and s.trace(S)==0
    r=4*(g-X[5]);ell=avec.T*S.inv();k=sm(S.inv()*r);rho=s.cancel((ell*k)[0]);B=r*avec.T-S
    assert sm(24*V*A-B)==s.zeros(3)
    # Independent full moment differentiation with all three vertex coordinates.
    hh=s.Matrix(s.symbols('h1 h2 h3'));XX=X.copy();XX[5]=X[5]+hh
    Vh,Jh,_,_=mass(XX,tri,XX[0]);ah=avec.dot(hh)
    assert s.cancel(Vh-V+ah/6)==0
    assert sm(24*(Jh-g*Vh)-(B*hh-ah*hh))==Z
    eta=s.cancel((ell*r)[0]-1)
    assert s.cancel(A.det()-S.det()*eta/(24*V)**3)==0
    assert s.cancel(A.det()+POL.as_expr()/(64*(6910*t+113)**4))==0
    assert V==(6910*t+113)/60
    root=R(14447,574220)+s.sqrt(277063679919871)/396786020
    assert s.simplify(POL.as_expr().subs(t,root))==0 and root>0
    assert POL.LC()>0 and POL.TC()<0
    lo,hi=LOW,HIGH
    assert POL.eval(lo)<0<POL.eval(hi)
    for _ in range(80):
        mid=(lo+hi)/2
        if POL.eval(mid)<0:lo=mid
        else:hi=mid
    def sg(expr):
        p,q=s.fraction(s.cancel(expr));ans=1
        for j,f in enumerate((q,p)):
            z=s.rem(s.Poly(f,t),POL).as_expr()
            if z==0:
                assert j==1,'Zero denominator at the algebraic root'
                return 0
            a,b=signq(z.subs(t,lo)),signq(z.subs(t,hi));assert a==b and a!=0
            ans*=a
        return ans
    assert hull(X,sg)[:3]==(fs,cyc,E)
    assert sg(A.det())==0 and sg(rho)>0
    assert all(sg(z)==0 for z in A*k) and all(sg(z)==0 for z in ell*A)
    assert sg((avec.T*k)[0]-1)==0
    assert sg(A[:2,:2].det())!=0 and sg(A6.det())>0
    joint=s.cancel(s.Matrix.hstack(A[:,0],A[:,1],A6[:,0]).det())
    assert s.cancel(joint+(491805430000*t**3+54098597300*t**2+1529729300*t+12045033)/(64*(6910*t+113)**4))==0
    assert sg(joint)<0
    Qbody=mechanics(X,fs,cyc,E,V,g,sg)
    assert Qbody['S']==[7,9] and Qbody['U']==[3,4,5]
    assert Qbody['H']==[(3,4),(3,5),(4,5)] and not Qbody['zero_rows']
    mech_guards=[]
    for row in Qbody['primitives']:
        for val,sign in zip(row['values'],row['signs']):
            mech_guards.append(positive_guard(sign*val,LOW,HIGH))
    # Actual deletion cap: no artificial fan diagonal is a mechanical edge.
    inds=[0,1,2,3,4,6];K=[X[j] for j in inds];KF,KC,KE,KT=hull(K,sg)
    visible=[]
    for f,c in zip(KF,KC):
        a,b,d=[K[j] for j in c[:3]];n=(b-a).cross(d-a)
        if sg(n.dot(X[5]-a))>0:visible.append(tuple(sorted(inds[j] for j in f)))
    assert sorted(visible)==[(0,1,2),(0,1,3),(0,2,4)]
    VK,JK,_,_=mass(K,KT,K[0]);assert s.cancel(V-VK)==R(1,20)
    # Delete the independent degree-three tip 6; its base is (0,3,4).
    XF=X[:6];CF,CC,CE,CT=hull(XF,signq)
    V0,J0,_,_=mass(XF,CT,XF[0]);normal=s.Matrix([-9,-10,90]);d0=691*t
    assert normal.dot(X[6])==d0
    assert s.cancel(V-V0-d0/6)==0
    assert sm(J-J0-d0*(X[6]+X[3]+X[4])/24)==Z
    b0=s.cancel(normal.dot(X[3]+X[4]-4*g))
    assert sg(2*d0+b0)>0
    # Complete exact constant-centroid shape arc through the fold. Parameter u.
    Tbox=IV(Q(lo),Q(hi));gb=viet(g,Tbox);kb=viet(k,Tbox);xb=[viet(x,Tbox) for x in X]
    n=[IV(v) for v in normal];delta0=iev(d0,Tbox);bb=iev(b0,Tbox)
    radius=Q(1,1<<20);Ubox=IV(-radius,radius);U2=IV(0,radius*radius)
    Delta=(-bb+((2*delta0+bb)*(2*delta0+bb)+4*dot(n,kb)*U2).sqrt())/2
    assert Delta.a>0
    sv=sub(add(xb[3],xb[4]),mul(4,gb))
    tip=add(mul(-1,sv),mul(1/Delta,add(mul(delta0,add(xb[6],sv)),mul(U2,kb))))
    Y=xb.copy();Y[5]=add(xb[5],mul(Ubox,kb));Y[6]=tip
    arc_guards=interval_geometry(Y,gb,fs,cyc,E,Qbody['primitives'])
    # The deleted-tip core retains its true boundary as well.
    core_center=mul(IV(Q(1,6)),[sum((Y[j][a] for j in range(6)),IV(0)) for a in range(3)])
    arc_guards+=interval_geometry(Y[:6],core_center,CF,CC,CE,None)
    volbox=iev(V0,Tbox)-Ubox/6+Delta/6;assert volbox.a>0
    ar=s.cancel((avec.T*r)[0]);rho_box=iev(rho,Tbox)
    cross_bracket=U2-iev(ar,Tbox)*Ubox+S.det()*rho_box;assert cross_bracket.a>0
    # Algebraic reductions of exact kernel and scalar-cubic identities.
    sig2=-s.trace(S*S)/2
    assert S**3+sig2*S-S.det()*I3==s.zeros(3)
    assert sg((avec.T*S**-3*r)[0]-(ar+sig2*rho)/S.det())==0
    # Exact polynomial verification of the whole moving-vertex/ear moment recipe.
    u,dd=s.symbols('u dd')
    def fieldzero(expr):
        num=s.fraction(s.cancel(expr))[0]
        return all(sg(c)==0 for c in s.Poly(num,u,dd).coeffs())
    XX=XF.copy();XX[5]=sm(X[5]+u*k)
    Vu,Ju,_,_=mass(XX,CT,XX[0])
    assert fieldzero(Vu-(V0-u/6))
    assert all(fieldzero(c) for c in Ju-J0+g*u/6+k*u*u/24)
    sv0=X[3]+X[4]-4*g
    tip0=sm(-sv0+(d0*(X[6]+sv0)+k*u*u)/dd)
    totalJ=Ju+dd*(tip0+X[3]+X[4])/24
    assert all(fieldzero(c) for c in totalJ-g*(Vu+dd/6))
    plane_relation=dd*dd+b0*dd-d0*(d0+b0)-normal.dot(k)*u*u
    assert fieldzero(dd*(normal.dot(tip0)-dd)+plane_relation)
    Bu=s.zeros(3)
    for i,j,l in tri:
        if 5 not in (i,j,l):continue
        n=(XX[j]-XX[i]).cross(XX[l]-XX[i])
        Bu+=(XX[i]+XX[j]+XX[l]+XX[5]-4*g)*n.T
    assert all(fieldzero(c) for c in Bu-(B-u*(k*avec.T+I3)))
    assert fieldzero(Bu.det()+2*u*(u*u-ar*u+S.det()*rho))
    # Exact rational checks on either side, plus the non-simplicial rejected seed.
    controls=[]
    for name,z,eheight in [('POSITIVE_JACOBIAN',R(1,100),9),('NEGATIVE_JACOBIAN',R(1,10),9),('SYMMETRIC_QUAD_NON_SIMPLICIAL',R(1,10),10)]:
        P=[x.subs(t,z) for x in X];P[4]=s.Matrix([0,eheight,1])
        FF,CC0,EE,TT=hull(P,signq);vv,jj,qq,_=mass(P,TT,P[0]);gg=jj/vv
        aa=jac(P,TT,vv,gg,5);mm=mechanics(P,FF,CC0,EE,vv,gg,signq)
        assert not mm['zero_rows']
        controls.append({'name':name,'raw_vertices':P,'facets':FF,'cycles':CC0,'edges':list(sorted(EE.items())),
          'volume':vv,'centroid':gg,'covariance':sm(qq/vv-gg*gg.T),'jacobian5':aa,'determinant5':s.factor(aa.det()),'mechanics':mm})
    assert controls[0]['determinant5']>0 and controls[1]['determinant5']<0
    assert (1,2,3,4) in controls[2]['facets']
    return {'identity':'TRUE_VERTEX_CENTROID_FOLD_V1','environment':'CPython3.13.5 SymPy1.14.0 assertions',
      'scope':'Actual own-COM degree-five fold and constant-centroid two-vertex escape; NOT110, NOT all4.',
      'root_polynomial':POL.as_expr(),'root_formula':R(14447,574220)+s.sqrt(277063679919871)/396786020,
      'root_isolation':[lo,hi],'raw_vertices':X,'facets':fs,'cycles':cyc,'edges':list(sorted(E.items())),
      'volume':V,'first_moment':J,'centroid':g,'covariance':sm(Q2/V-g*g.T),
      'all_t_positive_supports':support,'two_actual_fan_determinants':[ds,mass(X,tri,X[5])[3]],
      'ring':ring,'a':avec,'S_tensor':S,'S_determinant':S.det(),'ell':ell,'r':r,'kernel':k,'rho':rho,
      'jacobian5':A,'jacobian6':A6,'determinant5':s.factor(A.det()),'determinant6':s.factor(A6.det()),
      'joint_2plus1_minor':joint,'deletion_visible_faces':visible,'deletion_volume':VK,'deletion_moment':JK,
      'physical_root_mechanics':Qbody,'mechanics_interval':[LOW,HIGH],'Bernstein_guards':mech_guards,
      'fold_normal_second_coefficient':s.cancel(-rho/(24*V)),
      'centroid_fixed_arc':{'radius':radius,'tip_base':(0,3,4),'n':normal,'Delta0':d0,'b':b0,
          'exact_recipe':'w(u)=w+u*k; Delta(u)=(-b+sqrt((2*Delta0+b)^2+4*(n.k)*u^2))/2; svec=x3+x4-4*g; x6(u)=-svec+(Delta0*(x6+svec)+k*u^2)/Delta(u); all other vertices fixed; finally subtract the fixed actual g. All t expressions evaluated at the unique positive root.',
          'coordinate_enclosures':Y,'Delta_enclosure':Delta,'volume_enclosure':volbox,
          'positive_determinant_crossing_bracket':cross_bracket,'interval_guards':arc_guards,
          'exact_jacobian_determinant':'-2*u*(u^2-(a.r)*u+det(S)*rho)/(24*V(u))^3'},
      'static_controls':controls}

def main():
    assert sys.argv[1:] in (['build'],['check'])
    obj=build();b=(json.dumps(enc(obj),sort_keys=True,separators=(',',':'))+'\n').encode()
    assert len(b)==209180 and hashlib.sha256(b).hexdigest()=='71854d14d7d3ed1d8d94f9d223765f4c600ebd139f6d381615405b7d981c6746'
    p=Path('vertex_fold.json')
    if sys.argv[1]=='build':p.write_bytes(b)
    else:assert p.read_bytes()==b
    print('ACTUAL_NONPLANAR_DEGREE5_SINGULAR_OWN_CENTROID_JACOBIAN_PASS')
    print('ONE_POSITIVE_ROOT_ALL_T_POSITIVE_TRUE_FACE_LATTICE_PASS')
    print('TRUE_UNIFORM_TWO_FANS_STRICT_233_WEAK000_AT_FOLD_PASS')
    print('CONSTANT_CENTROID_TWO_VERTEX_ARC_FULL_INTERVAL_PASS')
    print('STATS',len(obj['all_t_positive_supports']),len(obj['Bernstein_guards']),len(obj['centroid_fixed_arc']['interval_guards']))
    print(p.name,len(b),hashlib.sha256(b).hexdigest())
    print('TRUE_VERTEX_CENTROID_FOLD_RECOVERY_PASS')
if __name__=='__main__':main()
```

Supplementary convenience files: [exact executable source](sandbox:/mnt/data/vertex_frontier/vertex_fold.py), [complete exact report](sandbox:/mnt/data/vertex_frontier/vertex_fold.json), [complete handoff](sandbox:/mnt/data/vertex_frontier/result.json). All reconstruction-critical source and data are already literal above.
