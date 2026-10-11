# minimum-0011

Historical AI scientific report · saved 2026-09-07 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# EFFECTIVE_SEVEN_POINT_REFLECTION_V1

## Determination

**A stronger factor than the proposed target closes, including weak escape inequalities.** The new theorem is:

> Let X be a nonempty set of at most seven distinct nonzero vectors in any finite-dimensional real Euclidean space. Suppose X admits a rooted tree such that every nonroot vector x, with parent p, satisfies x·(p−x) ≥ 0. Then, for q₀ = 1663/5000,
>
> **−q₀ conv(X) is not contained in conv(X).**

Here 1663/5000 = 0.3326 < 3333/10000 < 1/3. Failure at the new factor implies failure at the proposed factor: an inclusion −qK⊆K for any q>0 puts 0 in K, and then implies every smaller positive reflection factor by convexity.

No full-dimensionality, extremality, planar-chain, prescribed graph, or centroid assumption is imposed on X. In particular, the theorem includes strict escape trees and lower-rank sets. The empty set and the zero vector are explicitly outside the statement.

This produces effective geometry for eight reflected escape vertices. If Q has exactly eight vertices, admits such a weak escape tree, satisfies −Q/3 ⊆ Q, and

    B(0,ρ) ⊆ Q ⊆ B(0,M),       0 < ρ ≤ M,

put

    c = 1−3q₀ = 11/5000,
    σ = ρc/(1+6M/ρ),
    Δ = σ³/(4M²+σ²).

Then **every two vertices are more than σ apart**, and **every vertex has distance more than Δ from the convex hull of the other seven**. These are universal analytic bounds for this stated class, not sampling results.

For the eight actual facet poles of a hypothetical homogeneous joint110 C30 body, normalize the original body's actual centroid to zero and its circumradius to one. Using the supplied joint normalization B(0,1/27) ⊆ P ⊆ B(0,1), its polar satisfies B(0,1) ⊆ Q ⊆ B(0,27). Consequently the new explicit constants are

    pair separation > 11/815000;
    pole vertex essentiality > 1331/1578557281500098615000.

The unique stable pole has the stronger essentiality bound

    distance to the other-pole hull > 121/35868150000000.

There is also a new actual-volume centroid-separation corollary: if an interior reference o makes a uniformly filled polytope with at most seven facets mono-stable, then its actual centroid g satisfies |g−o|>(11/6652)rₒ, where rₒ is its inradius about o. There are explicit triangle-area, incident-pole determinant, and root-stability bounds below. The very small essentiality constant is conservative; it is nevertheless positive, rational, and proved uniformly over the entire normalized domain.

**There is no new F≥9 theorem or full C30 exclusion in this handoff.** The accepted integer bounds remain F≥8, V≥9, E≥15 and C≥30. The new result makes the eight-pole geometry effective without applying a primal centroid theorem to the wrong polar center.

## Source identity and change from the parents

The literal parents are `minimum-0003`, SHA-256 `520200e9b9541f54133e00931fc6ce2021fa752d2e8bb06df574ed1248720893`, and `minimum-0008`, SHA-256 `210f1968ce162060b752db868a0f9930508f1b487f1a4bd406218f1edddf75bc`.

The first parent's theorem has factor 1/3 and strict arrows; its full proof is the starting point, not an unlocated earlier certificate array. :contentReference[oaicite:0]{index=0} The second parent has a genuine own-centroid 222 counterexample to an unconditional polar capped-triple assertion, but does not have S1. No property of that counterexample is silently promoted to a monostable example. :contentReference[oaicite:1]{index=1}

The current journal's `2026-09-07T11:57:01.620Z` entry expressly labels q₀=3333/10000 a proposed target and describes the general two-sided sandwich. The theorem proved here resolves that target; it was not already an accepted premise. :contentReference[oaicite:2]{index=2} The current mounted journal is 1,430,146 bytes, SHA-256 `9cc9c16a4809574f4f66a34e6a96223eb8a8c4de1a6d7052699c68fda4f985a4`. I read the relevant current direction and both complete literal parent payloads. No substantive parent conflict was found.

The productive changes were to retune the near-antipode angle from π/56 to π/53, strengthen the usable tangent estimate, redo the two broom cases, replace two chain thresholds by slightly more permissive rational thresholds, and then build a controlled seven-point replacement of any allegedly collapsing eight-point configuration. The stronger factor increases the reflection reserve 1−3q₀ from the proposed target's 1/10000 to 11/5000. In the essentiality argument, pair separation is used to prove that newly selected approximate arrows cannot form a cycle. This is a necessary step, not an assumed persistence of an old tree.

The external primary source checked for context is the 2024 homogeneous mono-unstable paper, which proves V≥7 through quadratic necessary conditions and exact-checkable infeasibility certificates. It is not a source for the new reflection factor or the constants in this handoff; no publication-priority claim is made. :contentReference[oaicite:3]{index=3}

## 1. Weak escape estimates and the effective near-antipode lemma

Write K=conv(X). For a child x and parent p,

    |p|²−|x|² = 2x·(p−x)+|p−x|² > 0.

The strict inequality follows from distinctness, even when the escape inequality is an equality. Thus the root is the unique largest-radius vector. For consecutive ray angles α along a descending path,

    |child| ≤ |parent| cos α,       0 ≤ α < π/2.

The upper bound on α follows from x·p ≥ |x|² > 0. If the last vector has positive projection on a unit vector w, append its angle β with w. The sum of the path angles and β is at least the angle between the root and w. Concavity and monotonicity of log cos, padding with zero angles when necessary, give

    w·x ≤ R cos^m(angle(root,w)/m)                       (1)

for a node at depth at most m−1 from a root of norm R. All uses of (1) have m≥2. Nonpositive projections already satisfy the positive upper bounds used below. This argument uses only angular triangle inequalities, so spatial paths are included.

In particular, nodes of depth at most three have projection at most R/4 onto the negative root direction. Two descending edges also give

    |y|/|x| ≤ cos²(angle(x,y)/2).                         (2)

### Effective bottleneck lemma

Set

    φ = π/53,       a₀ = 1659/5000.

Suppose a tree has height four and every depth-four path passes through one common nonroot node z. Write e=r/R and z/|z|=cos θ e+sin θ u, with u perpendicular to e, and choose

    w = −cos φ e−sin φ u.

For collinear r,z choose any perpendicular u. A one-dimensional configuration may first be isometrically embedded in a plane; this changes neither its tree inequalities nor its reflection inclusion.

Every node of depth at most three has projection at most

    R cos⁴((π−φ)/4).

For a depth-four path, let the common node z occur at depth k. If θ≥φ, the prefix angles sum to at least θ and the suffix angles together with the final projection angle sum to at least π+φ−θ. Applying log-cos concavity to all five factors gives the bound

    R cos⁵((π+φ)/5).

If θ<φ, the suffix together with the final projection uses at most four factors and spans angle at least π−φ. Its projection is bounded by the preceding four-factor expression, using |z|≤R. Thus every node satisfies

    w·x < a₀ R.

The following strict scalar bounds are certified by rational arithmetic in Section 7:

    cos⁴((π−φ)/4) < 1659/5000,
    cos⁵((π+φ)/5) < 1659/5000,
    cos φ > 499/500,
    sin φ < 3/50,
    tan φ < 3/50.                                      (3)

Crucially,

    q₀(499/500)−1659/5000 = 337/2500000 > 0.             (4)

Therefore w strictly separates −q₀r from the entire tree, with the explicit support gap

    w·(−q₀r)−h_K(w) > (337/2500000)R.

Trees of height at most three are covered by w=−r/R, since q₀>1/4.

For a tree with at most eight nodes and height four, every depth-four path has the same first child of the root. Two different root branches each reaching depth four would require at least nine nodes. Hence the lemma applies to every height-at-most-four tree needed here, including branching below the first child.

## 2. Complete exclusion of the non-chain cases

Assume for contradiction that −q₀K ⊆ K and normalize the root r to norm one. Heights at most four have just been excluded.

### Height five with a unique first child

Let a be the sole child of r. Every other vector has norm at most |a|. The negative-root support required by −q₀r∈K forces |a|≥q₀. The weak first escape gives

    cos angle(r,a) ≥ |a| ≥ q₀ > sin φ.

After removing r, the subtree has at most six nodes and height four. Its near-antipode separator lies within φ of −a/|a| and therefore has strictly negative projection on the removed r as well. The same direction separates −q₀a from all of K, a contradiction.

### The only remaining height-five tree: the broom

A five-edge path uses six nodes. If the root has another child and there are at most seven nodes, the tree is exactly

    r,a,x₂,x₃,x₄,x₅,    together with a leaf b attached to r.

Put t=|a| and α=angle(r,a). Then t≤cos α, and both r and b belong to the closed diameter ball

    D = B(r/2,1/2).

The five-node tail rooted at a has height four.

First, t<2/3. Otherwise its near-antipode separator w has

    h_D(w) ≤ [1−t cos φ+sqrt(1−t²) sin φ]/2 < 83/400,

using cos φ>99/100, sin φ<1/10 and sqrt(1−t²)≤sqrt(5)/3<3/4. But

    w·(−q₀a) ≥ q₀t cos φ > q₀(2/3)(99/100) > 83/400.

The tail is excluded by its own separator lemma, so −q₀a cannot belong to K.

Now reflect the original root. If α≤π/5, use w=−a/t. The tail support is at most t cos⁵(π/5), and

    t cos⁵(π/5)/cos α
        ≤ t cos⁴(π/5) < (2/3)(7/16) = 7/24 < q₀.

For the diameter ball, its support is (1−cos α)/2<q₀ cos α, because cos α≥cos(π/5)>4/5>1/(1+2q₀). Thus −q₀r is separated.

If α>π/5, put ψ=(π−α)/4 and tilt −r by ψ away from a in their plane. The angle between a and this direction is exactly 5ψ. Here α>π/5 ensures ψ<α, so the formula does not cross the antipodal angle-wrap boundary. Also ψ<π/5, so the diameter-ball support remains strictly below q₀ cos ψ. The tail support is at most t cos⁵ψ. Reflection of r would therefore require

    q₀ ≤ t cos⁴ψ
       ≤ f₁(t) = (t/4)(1+sqrt((1−t)/2))².                (5)

The second inequality uses α≤arccos t. With z=sqrt((1−t)/2), the derivative of f₁ has the sign of 2z+4z²−1, positive on 0<t≤2/3 because z≥1/sqrt(6)>1/3. Consequently

    f₁(t) ≤ f₁(2/3)
          = 7/36+1/(3sqrt(6))
          < 119/360 < q₀.                               (6)

The rational upper bound uses 1/sqrt(6)<49/120. Equations (5)–(6) contradict reflection. Every height-five case is now excluded.

## 3. Complete exclusion of the seven-node chain

Height six requires exactly seven nodes and a Hamiltonian chain. Write its vertices in descending order as x₀,…,x₆, with root r=x₀ of norm one. Define

    b=x₂,     s=|b|,     c₄=x₄,     t=|c₄|,     u=t/s.

Only the required reflections of x₀ and x₂ will be used.

### 3.1 The second-node norm satisfies q₀<s<5/11

Nodes of depth at most three cannot provide the negative-root projection q₀>1/4. Therefore some node among x₄,x₅,x₆ has norm at least q₀. Monotonicity of radii gives t≥q₀ and s>q₀.

Apply the near-antipode lemma to the five-node tail x₂,…,x₆. The vector x₁ projects negatively on its separator, since

    cos angle(x₁,b) ≥ s/|x₁| ≥ s > q₀ > sin φ.

Thus r alone must provide the support required for −q₀b. Put α=angle(r,b). By (2), α≤2 arccos sqrt(s). This upper bound plus φ is below π: s>q₀>1/4 gives α<2π/3, and φ<π/3. Any separator within φ of −b/s consequently satisfies

    w·r ≤ (1−2s)cos φ+2sqrt(s(1−s))sin φ.

Since w·r≥q₀s cos φ, division gives

    (2+q₀)s ≤ 1+2tan φ sqrt(s(1−s))
             ≤ 1+tan φ < 53/50.

The exact reserve `(2+q₀)(5/11)−53/50=3/11000>0` proves s<5/11. This is one place where merely retaining the parent's weaker tangent estimate would not justify retaining its old threshold after lowering q.

### 3.2 The root cannot support the reflection of b

Suppose −r·b≥q₀s². Then cos α≤−q₀s, whereas (2) gives cos α≥2s−1. Hence

    s ≤ 1/(2+q₀) < 43/100,       α>π/2.

The prefix {x₀,x₁} lies in D=B(r/2,1/2). Tilt −r away from b by ψ=(π−α)/4. Now 0<ψ<π/8, the angle between b and the separator is 5ψ, and the diameter-ball support is below q₀ cos ψ. Formula (1) bounds the four-edge tail by s cos⁵ψ. Thus reflection of r would require

    q₀ ≤ s cos⁴ψ
       ≤ f₂(s) = (s/4)(1+sqrt(1−s))².

The derivative of f₂ has the sign of sqrt(1−s)+1−2s, positive for s≤43/100. Since sqrt(57/100)<151/200,

    f₂(s) ≤ f₂(43/100)
           < (43/400)(351/200)²
           = 5297643/16000000 < q₀.                      (7)

This is a contradiction. Therefore r cannot provide negative-b projection q₀s.

The vector x₁ has positive dot product with b. Nodes x₂,…,x₅ are at depth at most three from b and provide negative-b projection at most s/4<q₀s. Consequently the endpoint must satisfy

    −b·x₆ ≥ q₀s².                                      (8)

Its angle with b is greater than π/2. The four-edge radius-angle bound and s<5/11 give

    |x₆| < s cos⁴(π/8)
          < (5/88)(3+2sqrt(2))
          < 51/154 < q₀,                               (9)

where sqrt(2)<99/70. Thus x₆ cannot provide the required negative-root support either. Nodes x₀,…,x₃ already fail by depth. **One of x₄,x₅ must therefore have negative-root projection at least q₀.**

### 3.3 The two-step split is incompatible with both reflections

Since t≥q₀ and s<5/11,

    u>11q₀/5>73/100.

By (2), angle(b,c₄)≤2 arccos sqrt(u). Projecting the two-edge tail from c₄ to x₆ onto −b/s and using (8) yields

    q₀ ≤ B(u) = u cos³((π−2 arccos sqrt(u))/3).           (10)

This function decreases when u>cos²(π/5). Indeed, for v=arccos sqrt(u)<π/5,

    d(log B)/dv = −2tan v+2tan((π−2v)/3)>0,

while v decreases with u. Our lower bound u>73/100 lies in that range.

Put U=39/50. If z=cos((π−2 arccos sqrt(U))/3), then z>1/2 and

    4z³−3z=1−2U.

The cubic is strictly increasing for z>1/2. Exact substitution of Z=751/1000 gives

    4Z³−3Z>1−2U,       UZ³=16519025289/50000000000<q₀.

Thus B(U)<q₀ and (10) forces u<39/50.

Put a=arccos sqrt(s), v=arccos sqrt(u). The angle from r to c₄ is at most 2(a+v). Moreover a+v<π/2, since

    s+u ≥ 2sqrt(su)=2sqrt(t) ≥ 2sqrt(q₀)>1.

Using (1) with two factors for the one-edge tail {x₄,x₅}, its negative-root support is at most

    A(s,u) = su (sqrt(s(1−u))+sqrt(u(1−s)))².              (11)

It must be at least q₀ by the conclusion following (9).

On the rectangle

    q₀ ≤ s ≤ 5/11,       73/100 ≤ u ≤ 39/50,

A increases in both variables. For s, differentiate

    sqrt(A)=sqrt(u)[s sqrt(1−u)+sqrt(s(1−s))sqrt(u)],

using s<1/2. For u, use `sqrt(A)=sqrt(s)cos v sin(a+v)`. Its derivative in v is `sqrt(s)cos(a+2v)<0`, because s<1/2<4u(1−u) throughout the rectangle and v<π/4. Since v decreases with u, A increases with u.

Finally,

    A(s,u) ≤ A(5/11,39/50)
           = 11271/60500+117sqrt(1430)/30250
           < 251511/756250 < q₀,                        (12)

using sqrt(1430)<1891/50. The final rational reserve is

    q₀−251511/756250 = 71/3025000 > 0.

Equations (11)–(12) contradict the required negative-root support. This completes the chain and the theorem.

### Coverage and a direct reflection-defect corollary

Every rooted tree has a parent-before-child labeling. With at most seven nodes its height is at most six. Heights at most four, height five with a unique first child, the remaining seven-node broom, and the seven-node chain are exhaustive by the node-count arguments above. The proof does not infer a spatial exclusion from a sampled collection of embeddings.

The exact program additionally enumerates all increasing-labeled parent arrays on one through seven nodes. Its totals are:

| Case | Increasing-labeled arrays | Rooted isomorphism types, with sizes distinguished |
|---|---:|---:|
| Height at most four | 853 | 78 |
| Height five, one root child | 14 | 5 |
| Height-five broom | 6 | 1 |
| Height-six chain | 1 | 1 |
| Total | 874 | 85 |

This is a finite audit of the stated combinatorial split, not a substitute for the analytic estimates.

If such a seven-point hull additionally contains B(0,ρ), the theorem also gives an additive statement: some unit direction w satisfies

    h_{−K/3}(w)−h_K(w) > 11ρ/15000.

Indeed, failure at q₀ provides w with `h_K(w)<q₀h_K(−w)`, and `h_K(−w)≥ρ`; now use 1/3−q₀=11/15000.

## 4. Controlled deletion and pair separation for eight vertices

The following reductions use no centroid equation. Let Q have exactly eight true vertices, satisfy −Q/3 ⊆ Q, admit a weak escape tree, and lie between the balls B(0,ρ) and B(0,M).

Every vertex has norm at least ρ. No two vertices lie on the same positive ray: the nearer point would be a nontrivial convex combination of the farther point and the interior origin, and hence an interior point rather than a vertex. Positive radial rescalings of the eight vertices are consequently distinct whenever their labels are retained.

### Two elementary replacement lemmas

**Inward sandwich.** If Q'⊆Q and every point of Q is within distance d<ρ of Q', then for every unit w,

    h_Q'(w) ≥ h_Q(w)−d ≥ (1−d/ρ)h_Q(w).

Therefore `(1−d/ρ)Q⊆Q'⊆Q`. From −Q/3⊆Q it follows that

    −[(1−d/ρ)/3]Q' ⊆ Q'.                               (13)

Our replacements are inward, so (13) is stronger than the general two-sided sandwich in the assignment: the extra denominator 1+t is unnecessary. In particular, d≤ρc supplies reflection with factor q₀.

**Depth repair.** Suppose a rooted tree on at most seven nonzero vectors obeys

    x·p ≥ (1−η)|x|²,       0≤η<1.

For a node of depth d_i replace x_i by

    x_i'=(1−η)^{d_i} x_i.

A parent has depth d_i−1, so direct expansion gives `x_i'·(p_i'−x_i')≥0`. Since all depths are at most six, a vector of norm at most M moves by at most 6Mη, using `1−(1−η)^6≤6η`. If the original vectors are vertices of Q, the replacements lie in Q and remain distinct by the ray observation above. They need not remain vertices; the seven-point theorem does not require that.

### Pair-separation proof

Suppose two vertices a,b have distance ε≤σ, where

    σ=ρc/(1+6M/ρ).

Choose a as the one of smaller or equal norm and delete it. It is not the root, because the root has strictly greater norm than every other vertex. For every child x formerly pointing to a, point it instead to b. Its new escape inequality is

    x·b ≥ |x|²−|x|ε ≥ (1−ε/ρ)|x|².

All other arrows are unchanged. Each new arrow increases the **original** norm: a former child of a has norm below |a|≤|b|. Thus the new parent map is acyclic, retains the original root, and is a tree on seven vertices. This argument does not assume that a,b are neighbors or that the original matching has any particular form.

Apply depth repair with η=ε/ρ<1. The retained vertices move by at most 6Mε/ρ. The deleted a is within ε of b and hence within `ε+6Mε/ρ` of its replacement. Convexity extends the same distance bound to every point of Q. Thus the new seven-point hull Q' is contained in Q and satisfies

    d_H(Q,Q') ≤ ε(1+6M/ρ) ≤ ρc.

By (13), −q₀Q'⊆Q'. Its seven distinct nonzero generators have a weak escape tree, contradicting the theorem. Therefore

    |a−b| > σ        for every pair of distinct vertices. (14)

No original equilibrium margin was assumed bounded away from zero. This is why weak escape coverage in the first theorem is useful.

## 5. Vertex essentiality, including the rerouting-cycle issue

Retain σ from (14), and define

    Δ=σ³/(4M²+σ²),       η*=σ²/(2Mρ).

### The root already has a stronger bound

For any other vertex x, sum the strict squared-radius increments along its escape path. Each increment is at least the squared length of that edge, which exceeds σ². Thus, if r is the root and R=|r|,

    R²−|x|² > σ².

Every point of the other-vertex hull has norm at most the largest other-vertex norm. It follows that

    dist(r,conv(X\{r})) > σ²/(2R) ≥ σ²/(2M) > Δ.         (15)

Also, for every x≠r,

    |r|²−r·x
      = [R²−|x|²+|r−x|²]/2 > σ².                        (16)

### Deleting a nearly redundant nonroot

For a true nonroot vertex z, its distance δ from the convex hull of the other seven is positive. Suppose δ≤Δ. Take an exact closest point

    y=Σ_{v≠z} λ_v v,       λ_v≥0,       Σλ_v=1,
    |y−z|=δ.

For a child x formerly pointing to z, put α=1−λ_x. Since |z−x|>σ and every vertex has norm at most M,

    σ−δ < |y−x| ≤ 2Mα.

Hence α>(σ−δ)/(2M)>0. Averaging over the vertices different from both x and z gives at least one p with

    x·(p−x)
      ≥ x·(y−x)/α
      ≥ −|x|δ/α
      > −2M|x|δ/(σ−δ).                                  (17)

Here the original weak escape x·(z−x)≥0 was used in the second inequality.

There are two separate consequences of (17). First,

    x·(p−x) > −2M²Δ/(σ−Δ)=−σ²/2.

Together with |p−x|>σ this gives

    |p|²−|x|²=2x·(p−x)+|p−x|²>0.                        (18)

Therefore replacing the lost parent z by this p cannot create a directed cycle. Keeping every unaffected arrow produces a rooted tree on seven vectors, with the original root. A prescribed old parent or a presumed acyclic replacement would not suffice; (18) proves the needed acyclicity.

Second, since |x|≥ρ,

    x·(p−x) > −η*|x|²,

because

    2MΔ/[ρ(σ−Δ)] = σ²/(2Mρ)=η*.

Apply depth repair with η*. Each retained vertex moves by at most `6Mη*=3σ²/ρ`. The barycentric point y moves by at most the same amount. Consequently the deleted z is within `Δ+3σ²/ρ` of the new hull Q', and

    Q'⊆Q,       d_H(Q,Q')≤Δ+3σ²/ρ.                       (19)

### Uniform verification of the replacement scale

Write κ=M/ρ≥1 and s=σ/ρ=c/(1+6κ)≤c/7. Then

    η*=s²/(2κ)<1,
    Δ/ρ = s³/(4κ²+s²) ≤ s³/4,
    (Δ+3σ²/ρ)/ρ ≤ (c/7)³/4+3(c/7)² < c.                 (20)

The last inequality is an exact rational comparison for c=11/5000, checked in the source. It covers every κ≥1 analytically, not a grid of radius ratios.

Equations (19)–(20) and the inward sandwich provide −q₀Q'⊆Q'. The seven distinct nonzero generators satisfy a repaired escape tree, contradicting the seven-point theorem. Combining with (15), every vertex satisfies

    dist(z,conv(X\{z})) > Δ.                             (21)

The barycentric point y, weights λ, and replacement parents were used existentially in a proof over all configurations. They are not unprinted numerical witness data for a new polytope.

## 6. Consequences for the actual eight facet poles

Let P be a full-dimensional uniformly filled convex three-polytope with actual volume centroid zero. For any z∈P, cone a boundary triangulation from z. The nonnegative-volume tetrahedra partition P, and their volume-weighted centroids give

    0 = [z+Σ_T λ_T(a_T+b_T+c_T)]/4,
    λ_T≥0,       Σ_T λ_T=1.

Therefore −z/3 is a convex combination of boundary-triangle centroids and belongs to P. Thus −P/3⊆P. Polarity gives

    −Q/3⊆Q,       Q=P°.

Only this reflected containment is transferred. Neither g(Q)=0 nor a polar distinct-triple identity is asserted.

Write the actual maximal facets as `q_f·x≤1`. The perpendicular foot of facet f is `q_f/|q_f|²`. If it is not strictly inside that maximal facet, some other pole obeys `q_f·q_j≥|q_f|²`; if the foot lies outside P, one inequality is strict. Consequently one strictly stable facet supplies a weak escape tree on the poles. The strict joint110 class supplies strict nonroot escapes. The argument uses maximal facets and actual poles, not unit normals or fan-triangulation pieces. Artificial arrows used in the reductions are not added to the count of genuine edges.

### Actual-volume centroid separation with at most seven facets

More quantitatively, suppose an interior reference o gives a uniformly filled full-dimensional polytope P with at most seven maximal facets exactly one strictly stable facet. Other facets may have weak escape equalities. Let g be its actual uniform-volume centroid and let rₒ>0 be its inradius about o. Then

    |g−o| > (11/6652)rₒ.                                (22)

To prove this, translate o to zero. The actual-centroid reflection established by the cone identity gives

    −x/3+4g/3 ∈ P        for every x∈P.

If |g|≤crₒ/(4q₀), the point y=−4q₀g/c belongs to B(0,rₒ)⊆P. Since 3q₀+c=1,

    −q₀x = 3q₀(−x/3+4g/3)+cy ∈ P.

Thus −q₀P⊆P and, by polarity about the same reference, −q₀P°⊆P°. The at-most-seven actual poles admit a weak escape tree by the facet-foot argument above. This contradicts the new theorem. Finally c/(4q₀)=11/6652, proving (22). No centroid of P° enters this proof. This is an actual-volume quantitative facet-side result, not an F≥9 result.

### The normalized eight-pole boundary

The eight-pole geometry theorem therefore applies already to a homogeneous S1 body with F=8 whenever explicit ρ,M bounds on its polar are supplied. **The uniform number 27 is used only for the joint-normalized application, not assumed for S1 alone.** In the requested C30 domain take

    B(0,1/27)⊆P⊆B(0,1),
    B(0,1)⊆Q⊆B(0,27),
    N=815000,
    σ=11/N,
    Δ=1331/[N(2916N²+121)]
      =1331/1578557281500098615000.

All the following inequalities are strict and use the original body's fixed centroidal Euclidean coordinates:

| Quantity | Uniform lower bound |
|---|---:|
| Distance between any two distinct poles | 11/815000 |
| Distance of any pole from the convex hull of the other seven | 1331/1578557281500098615000 |
| Distance of the unique stable pole from the other-pole hull | 121/35868150000000 |
| Root quadratic guard `|r|²−r·q_f`, f≠root | 121/664225000000 |
| Slack `1−q_f·(r/|r|²)` at the stable foot | 121/484220025000000 |
| Area of any triangle of three distinct poles | 14641/2573048368845160742450000000 |
| Absolute determinant of any three poles incident to one primal vertex | 14641/1286524184422580371225000000 |

The root bounds follow from (15)–(16), with M=27. For the triangle bound, use the longest side as base. The perpendicular foot of the opposite vertex lies in that segment. Its altitude exceeds Δ by (21), while the base exceeds σ by (14). Thus every such area exceeds σΔ/2. No three true vertices can be collinear, and no triangular-facet assumption is being made.

For the last row, three poles incident to a primal vertex v lie in the plane `v·q=1`. Their determinant has absolute value `2 area/|v|`; since |v|≤1, it exceeds σΔ. This holds for any three incident poles even when v is nonsimple. It supplies a uniform ingredient for the lead's edge-determinant/slack conversion without claiming that conversion or a complete nonincidence-slack theorem has been independently finished here.

These constants also prevent pole coalescence and loss of a pole into the other-pole hull in limits of normalized candidates. They do **not** assert a uniform positive lower bound for every nonroot mechanical escape, prohibit all incidence changes, or prove an empty C30 realization space. The auxiliary Q' used in the proof is not claimed to have either its own volume centroid or its polar's volume centroid at zero; its reflected containment and escape tree are sufficient for the contradiction.

## 7. Self-contained exact recovery capsule

Identity: **EFFECTIVE_SEVEN_POINT_REFLECTION_V1**, based on the two named literal parents and the `2026-09-07T11:57:01.620Z` checkpoint. The written proof above supplies the spatial and geometric reasoning. The source below reproduces every scalar certificate, every finite tree-count assertion, and all printed normalized constants. It imports no parent program and needs no journal, solver, normal pool, graph catalogue, or unprinted input.

The trigonometric certificates use Machin's identity `π=16 arctan(1/5)−4 arctan(1/239)`, checked by rational tangent addition: the angle θ=4 arctan(1/5)−arctan(1/239) lies in (0,4/5)⊂(0,π/2) and has tangent one, so θ=π/4. Alternating arctangent sums enclose π between 314159/100000 and 3927/1250. On the argument intervals used, which lie in [0,1], the alternating cosine polynomial through degree eight is an upper bound, and `1−x²/2` is a lower bound. The square-root comparisons in the proof are exact comparisons of positive rational squares. No numerical transcendental evaluation is a premise.

Executed environment: **CPython 3.13.5, standard library only**, assertions enabled. Save the complete block below as `reflection_effective_v1.py`, UTF-8 with LF line endings and its final LF. Source: **6749 bytes**, SHA-256 **`03770f45c94b13e1413b09d55b59585d7738d5c7f11b8f046a8565a47cd10e87`**.

Run in an empty writable directory:

```sh
python -S reflection_effective_v1.py
sha256sum reflection_effective_v1.py reflection_effective_v1_report.json
```

Observed terminal output, reproduced by a separate clean-directory execution with byte-identical output:

```text
ALL_Q1663_5000_SCALAR_CERTIFICATES_PASS
ALL_874_INCREASING_TREES_85_ROOTED_TYPES_COVERED_PASS
EIGHT_POLE_SEPARATION_ESSENTIALITY_CONSTANTS_PASS
REPORT 4522 6a549a06658fe9a5badfb76f7d1380f64002be40b9a74aa29957687f7a0104c7
SOURCE 6749 03770f45c94b13e1413b09d55b59585d7738d5c7f11b8f046a8565a47cd10e87
EFFECTIVE_SEVEN_POINT_REFLECTION_RECOVERY_PASS
```

The generated `reflection_effective_v1_report.json` is **4522 bytes**, SHA-256 **`6a549a06658fe9a5badfb76f7d1380f64002be40b9a74aa29957687f7a0104c7`**. It is an exact proof ledger, not a new physical polytope. The program has no optional arguments or non-default solver parameters.

```python
"""EFFECTIVE_SEVEN_POINT_REFLECTION_V1; CPython 3.13.5, stdlib only.
Run with assertions enabled: python -S reflection_effective_v1.py
The spatial inequalities and geometric reductions are proved in the handoff.
This unit checks every scalar certificate and the complete finite tree split.
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter
from math import factorial
from pathlib import Path
import hashlib
import json

assert __debug__
PARENTS = {
    'minimum-0003':
    '520200e9b9541f54133e00931fc6ce2021fa752d2e8bb06df574ed1248720893',
    'minimum-0008':
    '210f1968ce162060b752db868a0f9930508f1b487f1a4bd406218f1edddf75bc'}
CHECKPOINT = '2026-09-07T11:57:01.620Z'
q = F(1663, 5000)
assert q < F(3333, 10000) < F(1, 3)
c = 1-3*q
checks = {}


def pos(name, x):
    assert x > 0, (name, x)
    checks[name] = str(x)


def atan_sum(x, n):
    return sum((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(n))


def cos_upper(x):
    assert 0 <= x <= 1
    return 1-x*x/2+x**4/24-x**6/720+x**8/40320


# Exact tangent addition for Machin's identity, then alternating bounds.
z = F(1, 5)
z = 2*z/(1-z*z)
z = 2*z/(1-z*z)
assert (z-F(1, 239))/(1+z/F(239)) == 1
pi_low = 16*atan_sum(F(1, 5), 6)-4*atan_sum(F(1, 239), 3)
pi_high = 16*atan_sum(F(1, 5), 5)-4*atan_sum(F(1, 239), 2)
pL, pU = F(314159, 100000), F(3927, 1250)
pos('pi_lower', pi_low-pL)
pos('pi_interval', pi_high-pi_low)
pos('pi_upper', pU-pi_high)
phiU = pU/53
A4 = cos_upper(13*pL/53)**4
B5 = cos_upper(54*pL/265)**5
pos('A4_cap', F(1659, 5000)-A4)
pos('B5_cap', F(1659, 5000)-B5)
pos('cos_phi', 1-phiU**2/2-F(499, 500))
pos('sin_phi', F(3, 50)-phiU)
pos('tan_phi', F(3, 50)-phiU/(1-phiU**2/2))
pos('near_antipode_gap', q*F(499, 500)-F(1659, 5000))
assert checks['near_antipode_gap'] == '337/2500000'
pos('q_vs_depth3', q-F(1, 4))
pos('q_vs_sin_phi', q-F(3, 50))
pos('cos_pi5_lower', 1-(pU/5)**2/2-F(4, 5))
pos('cos_pi5_fourth', F(7, 16)-cos_upper(pL/5)**4)
pos('cos_pi5_squared', F(73, 100)-cos_upper(pL/5)**2)
pos('diameter_ball_ratio', F(4, 5)-1/(1+2*q))
pos('sqrt5_over3', F(9, 16)-F(5, 9))
pos('broom_large_t', q*F(2, 3)*F(99, 100)-F(83, 400))
pos('broom_small_angle', q-F(7, 24))
pos('inverse_sqrt6', 6*F(49, 120)**2-1)
f1cap = F(7, 36)+F(49, 360)
pos('broom_f1', q-f1cap)
pos('chain_s_upper', (2+q)*F(5, 11)-1-F(3, 50))
pos('chain_angle_no_wrap', 2*q-F(3, 50))
pos('chain_root_support_s', F(43, 100)-1/(2+q))
pos('sqrt57_over100', F(151, 200)**2-F(57, 100))
f2cap = F(43, 400)*(1+F(151, 200))**2
pos('chain_f2', q-f2cap)
pos('sqrt2', F(99, 70)**2-2)
endpointcap = F(5, 88)*(3+2*F(99, 70))
assert endpointcap == F(51, 154)
pos('chain_endpoint', q-endpointcap)
pos('chain_u_lower', q/F(5, 11)-F(73, 100))
U, Z = F(39, 50), F(751, 1000)
pos('cubic_monotone_domain', Z-F(1, 2))
pos('cubic_comparison', 4*Z**3-3*Z-(1-2*U))
pos('chain_B_upper', q-U*Z**3)
pos('A_s_derivative', F(1, 2)-F(5, 11))
pos('A_u_derivative', 4*U*(1-U)-F(1, 2))
pos('sqrt1430', F(1891, 50)**2-1430)
Acap = F(11271, 60500)+F(117, 30250)*F(1891, 50)
assert Acap == F(251511, 756250)
pos('final_chain_gap', q-Acap)
print('ALL_Q1663_5000_SCALAR_CERTIFICATES_PASS')


def tree_data(p):
    ch = [[] for _ in p]
    depth = [0]*len(p)
    for i in range(1, len(p)):
        assert 0 <= p[i] < i
        ch[p[i]].append(i)
        depth[i] = depth[p[i]]+1
    def enc(i):
        return '('+''.join(sorted(enc(j) for j in ch[i]))+')'
    return ch, depth, enc(0)


broom = tree_data((-1, 0, 1, 2, 3, 4, 0))[2]
chain = tree_data((-1, 0, 1, 2, 3, 4, 5))[2]
coverage = []
for n in range(1, 8):
    labeled, types = Counter(), {}
    for tail in product(*(range(i) for i in range(1, n))):
        p = (-1,)+tail
        children, depth, code = tree_data(p)
        height = max(depth)
        if height <= 4:
            case = 'height_le_4'
            firsts = set()
            for i in range(n):
                if depth[i] == 4:
                    j = i
                    while p[j] != 0:
                        j = p[j]
                    firsts.add(j)
            assert len(firsts) <= 1
        elif height == 5 and len(children[0]) == 1:
            case = 'height_5_single_child'
            assert n <= 7
        elif height == 5:
            case = 'height_5_broom'
            assert n == 7 and code == broom
        else:
            case = 'height_6_chain'
            assert height == 6 and n == 7 and code == chain
        labeled[case] += 1
        if code in types:
            assert types[code] == case
        types[code] = case
    assert sum(labeled.values()) == factorial(n-1)
    coverage.append(dict(n=n, labeled=dict(sorted(labeled.items())),
                         rooted_types=dict(sorted(Counter(types.values()).items()))))
assert [sum(r['rooted_types'].values()) for r in coverage] == [1,1,2,4,9,20,48]
assert sum(sum(r['labeled'].values()) for r in coverage) == 874
assert sum(sum(r['rooted_types'].values()) for r in coverage) == 85
print('ALL_874_INCREASING_TREES_85_ROOTED_TYPES_COVERED_PASS')

# Uniform symbolic envelopes use kappa=M/rho >= 1, s=sigma/rho <= c/7.
assert c == F(11, 5000)
pos('universal_eta_below_one', 1-(c/7)**2/2)
pos('universal_inner_sandwich', c-3*(c/7)**2-(c/7)**3/4)
rho, M = F(1), F(27)
sigma = rho*c/(1+6*M/rho)
Delta = sigma**3/(4*M*M+sigma*sigma)
eta = sigma*sigma/(2*M*rho)
root_height = sigma*sigma/(2*M)
assert sigma == F(11, 815000)
assert Delta == F(1331, 1578557281500098615000)
assert eta == F(121, 35868150000000)
assert 2*M*Delta/(rho*(sigma-Delta)) == eta
assert sigma*(1+6*M/rho) == rho*c
pos('normalization_inner_sandwich', rho*c-Delta-6*M*eta)
pos('root_height_vs_Delta', root_height-Delta)
assert c/(4*q) == F(11, 6652)
constants = dict(q0=q, reflection_loss=c,
    facet_centroid_gap_per_inradius=c/(4*q),
    two_sided_sandwich_tolerance=c/(1+3*q), rho=rho, outer_radius=M,
    pair_separation=sigma, vertex_essentiality=Delta,
    essentiality_repair_eta=eta, root_essentiality=root_height,
    root_quadratic_gap=sigma*sigma,
    root_foot_slack=sigma*sigma/(M*M), triangle_area=sigma*Delta/2,
    incident_pole_determinant=sigma*Delta)
print('EIGHT_POLE_SEPARATION_ESSENTIALITY_CONSTANTS_PASS')
report = dict(version=1, name='EFFECTIVE_SEVEN_POINT_REFLECTION_V1',
    parents=PARENTS, checkpoint=CHECKPOINT, checks=checks,
    constants={k:str(v) for k,v in constants.items()}, coverage=coverage)
raw = (json.dumps(report, sort_keys=True, separators=(',', ':'))+'\n').encode('ascii')
Path('reflection_effective_v1_report.json').write_bytes(raw)
print('REPORT', len(raw), hashlib.sha256(raw).hexdigest())
src = Path(__file__).read_bytes()
print('SOURCE', len(src), hashlib.sha256(src).hexdigest())
print('EFFECTIVE_SEVEN_POINT_REFLECTION_RECOVERY_PASS')
```

## 8. Remaining frontier and continuation

The new universal conclusions are the weak seven-point exclusion at **1663/5000**, the actual-volume facet-reference centroid gap **11rₒ/6652** at at most seven facets, and the explicitly quantified separation and essentiality theorem for eight reflected escape vertices. Their proofs have complete tree and spatial coverage. The rational scalar checks and a clean replay have run; this is not a proof-assistant formalization or a claim of external mathematical review, and the constants are not asserted optimal.

The eight-pole theorem does not replace actual volume compatibility, nor does it justify selecting just one primal/dual tree pair. The numerical lower bound on the number of facets remains **F≥8** and the accepted joint lower bound remains **C≥30**; no complete C30 graph type or continuous realization cell is newly declared empty by this handoff. The original seven-point fixture at factor 5/16 and eight-point reflection fixture do not conflict with the stronger factor proved here.

The most useful continuation is to insert σ, Δ and the incident-pole determinant floor into the lead's quantitative edge identity, together with its independently derived primal separation. That can bound genuine nonincidence slacks while retaining actual centroid equations and all existentially compatible matching branches. Nonroot escape equalities must remain allowed in limit arguments: this work bounds the geometry and the root margins, not every nonroot mechanical margin.

Convenience copies: [complete recovery source](sandbox:/mnt/data/atlas13_effective/reflection_effective_v1.py) and [exact scalar/tree/constant ledger](sandbox:/mnt/data/atlas13_effective/reflection_effective_v1_report.json). The full inline source and proofs, not these links, are the durable handoff.
