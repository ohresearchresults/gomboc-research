# minimum-0058

AI research report · 2026-09-11 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

**Result.** I obtained new physical inequalities from a three-roof affine-density lift, an entire-column facet-pair constraint with a geometric equality classification, a complete positive-pole-circuit extension of common-row energy, and a sharp rank-three pole-scatter inequality. Exact certificates exclude substantial closed continuous sectors of all three assigned literal forms. They impose no covariance condition-number restriction. **No whole remaining tree is excluded, and the accepted global bounds remain V≥10, F≥9, C≥34.**

Write n_i=q_iᵀNq_i, α=n₁/n₀ and β=n₈/n₀. The new necessary frontiers are:

| Literal form | Complete closed domains excluded | Exact remaining restriction | Discrete premise |
|---|---|---|---|
| TREE266 | α≤3/8; α≥1/2; β≤1/16; β≥1/2 | 3/8<α<1/2 and 1/16<β<1/2 | All three stronger OJ frames, retaining their mandatory negative shadows |
| TREE272 | 2Λ₀₁+Λ₀₈≥1/3 | 0<2Λ₀₁+Λ₀₈<1/3 | Bare eight-arrow TREE272; arbitrary additional shadows allowed |
| TREE278 | α≤1/4; Λ₀₁≥1/6; Λ₀₈≥7/8 | α>1/4, Λ₀₁<1/6, Λ₀₈<7/8 | Bare eight-arrow TREE278; arbitrary additional shadows allowed |

All equality walls in the excluded sectors are covered. The 272 and 278 statements need no root-stability or incidence premise. The 266 statement needs the journal's stronger OJ frame theorem; it is not asserted for a bare 266 tree with unrestricted additional positive shadows. None assumes simplicity, positive lower bounds on facet areas, strict escape margins, or bounded SPD conditioning. Exact acceptance comprises **1992 positive-definite integer matrices and 17928 positive leading principal minors**, checked by both integer Bareiss elimination and Fraction LDL.

**Source authority and literal bindings.** I read the supplied `research-journal(20260911-182303).md`, 4431148 bytes, SHA-256 `309a6155769dc91dc22edb4dc3384681f79b2744958e80a20bffa21dfa020eeb`, including the literal parent `minimum-0055`, declared SHA-256 `1ba8b094d0d18ef42023d28e1d0fc1e171ed73104955b186da6b88e48166541e`.

A provenance discrepancy must be preserved: the appended Markdown after that parent header is 44286 UTF-8 bytes, SHA-256 `68591f890ea5e9b9b491da18fe82dda044174c8c6fa318b51cd4aa1d091e23dd`, which does not reproduce the declared immutable-payload hash. An original transport/serialization wrapper was not supplied, so I cannot independently verify the declared hash from those Markdown bytes. No mathematical array or incidence conflict was found. I use the supplied literal text as authority and the declared hash as its stated identity, without claiming a reproduced byte hash. No journal was edited.

These are the exact surviving forms and all ten maximal frames of the stronger OJ cover, separately from the parent's weaker 17-frame cover:

```python
TREES={253:(0,0,1,2,3,4,5,0,7),
       266:(0,0,1,2,3,4,5,4,0),
       272:(0,0,1,2,3,4,5,5,0),
       278:(0,0,1,2,3,4,5,6,0)}
OJ={253:[[]],
    266:[[(5,7),(6,7)],[(6,7),(7,5)],[(7,5),(7,6)]],
    272:[[(6,4),(6,7)],[(6,4),(7,6)],[(6,7),(7,4)],[(7,4),(7,6)]],
    278:[[(6,4),(7,5)],[(7,4),(7,5)]]}
```

Index zero is the root convention; every i>0 has arrow i→p[i]. Extras are optional nonnegative-shadow arrows, not required arrows or true-edge labels. The full nonnegative-shadow graph contains the base tree and lies in a listed frame. Pairs outside a frame are negative and may safely be weakened to nonpositive in a certificate. TREE285=(0,0,1,2,3,4,5,6,7) remains excluded by the parent; it is unrelated to canonical C32:285.

**One actual body throughout.** Let P={x:q_iᵀx≤1} be a bounded full-dimensional three-polytope with distinct maximal facets, centered at its own uniform-volume centroid. Set V=Vol(P), Σ=E_P xxᵀ, Y=1−Qx, J=11ᵀ, d_i=A_i/(V‖q_i‖), ω=d/3, H=E_P YYᵀ=J+QΣQᵀ, Λ[:,i]=d_iE_FiY, and K_i=d_iE_FiYYᵀ. Let c_i be the actual facet centroid. Fix any reciprocal SPD pair M,N=M⁻¹ and G=QNQᵀ. Every volume, area and edge expectation below belongs to this same P. On a true edge ij, η_ij=length(E_ij)/(V‖q_i×q_j‖).

Divergence gives ∑d_i=3, ∑d_iq_i=0, ∑d_ic_i=0, ∑d_ic_iq_iᵀ=I and hence

- Λ1=3·1, ΛQ=−Q, HΛᵀ=ΛH=4J−H;
- Λ²+Λ=4·1dᵀ and d_i=(Λ²)ᵢᵢ/4;
- Hd=3·1, K_iω=Λ[:,i], ∑K_i=5H−2J;
- rank H=rank Λ=4, rank K_i=3, Λᵢᵢ=0, and Λᵢⱼ>0 for i≠j.

For example, Λ=1dᵀ−QCᵀdiag(d), and Cᵀdiag(d)Q=I proves the square identity. Integrating div(xYYᵀ) proves the K sum. These are necessary physical identities, not a realization criterion.

**Three-roof affine-density theorem.** Let f,g be nonzero nonnegative affine functions and c an actual facet. Define a=E_Pf, b=E_Pg, A=E_Pfg, h_f=E_P(fY_c), h_g=E_P(gY_c), m=E_P(fgY_c)>0, u=d_cE_Fc(fg), and ρ=5/(6m). Then the following 3×3 matrix is PSD:

```text
ρ (h_g,h_f,A)ᵀ(h_g,h_f,A) − [[0,1,b],[1,0,a],[b,a,u]].                 (T1)
```

This is a signed Loewner inequality in its three test coordinates; its roof densities f,g,Y_c must be nonnegative.

Here is the physical proof, including weak and nonsimple cases. First replace the three roofs by f+ε,g+ε,Y_c+ε and form their actual six-dimensional box lift over P. Vary the original supports and the three roof offsets. Its normalized volume is the integral of the product of the three affine roofs. Original-support derivatives use the actual facet integrals; derivatives in distinct original supports use η_ij times the actual shared-edge integral, and vanish on nonedges. At nonsimple vertices, changing a corner contributes cubic order, so fixed-normal volume and these weighted polynomial integrals have the required C² regularity. The support-Hessian statement is also recorded in [Izmestiev, Appendix A.3](https://arxiv.org/pdf/0704.0349).

Minkowski containment of the lifts and Brunn–Minkowski give concavity of the sixth root of their volume. Therefore ρ times the gradient outer product minus its Hessian is PSD. Pass to ε↓0 in the explicit derivative matrices. At original side c, the product and its first derivative vanish, the diagonal Hessian is −u, and the side/roof block is (0,0,u). The roof Hessian is C=[[0,1,b],[1,0,a],[b,a,0]], and the roof gradient is h=(h_g,h_f,A). The four-variable quadratic form is

```text
u(s−r₃)² + rᵀ(ρhhᵀ−C−u e₃e₃ᵀ)r.
```

Set s=r₃. This proves T1, including u=0, repeated roofs, zero values on faces, weak walls and nonsimple P. It does not assume C² regularity of the limiting six-dimensional lift after a side disappears; differentiation is at positive ε followed by closedness of PSD.

The matrix D=C+u e₃e₃ᵀ is bounded above by a rank-one PSD matrix. Its upper-left 2×2 determinant is −1, so it has exactly one positive direction. Since det D=2ab−u, its inertia gives u≤2ab. The principal minor and determinant of T1 give, with Δ=10h_fh_g−6m,

```text
u≤2ab,   Δ≥0,   (2ab−u)Δ≥5(A−a h_g−b h_f)².                       (T2)
```

These are division-free on Δ=0. For f=g, the actual probability measure Y_c dV/V gives m≥h² by Cauchy. Combining this with T2 yields

```text
d_c E_Fc f² ≤ 2(E_Pf)² − (5/4)(E_Pf²/E_P(fY_c)−2E_Pf)².           (T3)
```

In particular K_c,aa≤2−(5/4)(H_aa/H_ac−2)². Facet Jensen and the common identities now give

```text
Λ_ac² ≤ d_c K_c,aa ≤ 2d_c = (Λ²)_cc/2,                            (T4)
∑_{c≠a}(H_aa/H_ac−2)² ≤ 8F/5−4H_aa.                              (T5)
```

Facet Jensen is strict for nonparallel supporting planes, hence on a true edge. A shadow arrow alone does not imply this. The cap 2 is sharp at nine facets: opposite caps of a centered heptagonal prism have d_c=1/2, Y_a|Fc=2, K_c,aa=2, H_aa=4/3, H_ac=E_PY_a²Y_c=2/3. This nonnegative-affine cap is not 2J−K_c⪰0. On the same prism, the signed affine z=(Y₈−Y₇)/2 has mean zero and d₇E_F7z²=1/2, giving signed value −1/2. The exact recovery reconstructs the actual prism, its common moments and true-edge flux, and checks all 84 distinct triple matrices, 405 bilinear matrices and 81 square-defect bounds.

**Three facets and an entire-column pair constraint.** For distinct a,b,c put u=K_a,bc, v=K_b,ac, w=K_c,ab, h=(H_bc,H_ac,H_ab)ᵀ and m=E_PY_aY_bY_c. Eliminating all three original sides of the same lift gives

```text
(5/(6m))hhᵀ − [[u,1,1],[1,v,1],[1,1,w]] ⪰ 0.                      (T6)
```

The limiting side Hessian is −diag(u,v,w), its side/roof block is diag(u,v,w), and the roof Hessian is J₃−I₃; the preceding square completion proves T6. Here u,v,w>0. Its one-positive-direction property implies

```text
uv≤1, uw≤1, vw≤1,   u+v+w≤2+uvw.                                 (T7)
```

Rewriting the last bound as u+v+w(1−uv)≤2 proves u+v≤2 and its cyclic versions. Thus u+v+w≤3, with equality only at (1,1,1). The determinant wall occurs physically at nine facets: a prism lateral facet and its two caps give (u,v,w)=(2d_lateral/3,1,1). It must not be replaced by a strict inequality.

Using T3 for repeated indices extends the pair-sum bound to every column:

```text
K_a e_b + K_b e_a ≤ 2·1   entrywise, for every a≠b.                 (T8)
```

This contains more information than its ω-average Λ_ab+Λ_ba≤2. Define s=Λ_ab, t=Λ_ba, ε=2−s−t, z_ab=d_aE_Fa(Y_bx), and δ=2·1−K_a e_b−K_b e_a. Then δ=ε1+Q(z_ab+z_ba). Consequently

```text
ε>0  ⇒  −(z_ab+z_ba)/ε ∈ the same actual P.                        (T9)
```

Also Λδ=4ε1−δ, so 0≤δ_c≤4ε, without a lower facet-mass bound. If u_c=K_a,bc, v_c=K_b,ac, w_c=K_c,ab, then

```text
∑_c ω_c w_c[(u_c−1)²+(v_c−1)²] ≤ 2ε.                              (T10)
```

For distinct indices, T7 gives δ_c≥w_c(1−u_cv_c), and

```text
2δ_c−w_c[(u_c−1)²+(v_c−1)²]
=2[δ_c−w_c(1−u_cv_c)]+w_cδ_c(2−δ_c)≥0.
```

At c=a,b, w_c=0. Average with the same actual ω. Vanishing masses in degenerating families prevent T10 alone from yielding a uniform geometric gap.

**Exact pair-equality geometry.** For an actual pair a≠b, the following are equivalent:

1. Λ_ab+Λ_ba=2.
2. Λ_ab=Λ_ba=1.
3. There exists v with Qv=e_a−e_b.

The two-roof determinant forces s=t=1 in the first case. Positivity of ω and T8 then force δ=0. For c distinct from a,b, T7 and w_c>0 force u_c=v_c=1; repeated entries are 2. Thus K_a e_b=1+e_b−e_a, so Qz_ab=e_a−e_b and v=z_ab.

Conversely, write x=y+τv with y∈v⊥. All other facets are parallel to v; a,b give affine endpoints ℓ(y)=q_bᵀy−1 and u(y)=1−q_aᵀy. The actual projection B includes u−ℓ≥0. The width may vanish on a projected boundary edge where the caps meet. Volume equals ‖v‖∫_B(u−ℓ), and A(F_a)/‖q_a‖=A(F_b)/‖q_b‖=‖v‖Area(B). Direct integration gives both cross-Λ entries 1. Neither parallel caps nor prism combinatorics is assumed.

The linear involution R=I−v(q_a−q_b)ᵀ maps the same P onto itself, exchanges a,b and fixes every other facet setwise. Therefore

```text
RΣRᵀ=Σ,
H_aa=H_bb,  H_ac=H_bc for c∉{a,b},
Σ(q_a−q_b)=(H_aa−H_ab)v.
```

It forces d_a=d_b≥1/2, with equality exactly for parallel caps. Indeed, for w=u−ℓ, the own-centroid identity ∫_B yw=0 gives ∫_B w²=2∫_B w. Cauchy gives ∫_B w/Area(B)≤2 and hence d_a=d_b≥1/2. Equality makes the affine width constant. For F≥5, d_a=d_b<3/4: equality in the centroid facet-cone bound would make both facets pyramid bases, forcing a tetrahedron. This affine reflection need not be an isometry of M, so it does not alone prove two stable facets.

There is a useful Λ-only projection. For a,b≠i define

```text
L_i(a,b)=max(0,
 [Λ_aiΛ_bi−sqrt((2d_i−Λ_ai²)(2d_i−Λ_bi²))]/d_i).
```

PSD of K_i−λ_iλ_iᵀ/d_i and T3 give K_i,ab≥L_i(a,b). For distinct a,b,c, the lower triple (L_a(b,c),L_b(a,c),L_c(a,b)) satisfies T7 and its pair-sum bounds. This substitution is valid because u+v+w−uvw is coordinatewise nondecreasing where pair products are at most one. All masses remain d_i=(Λ²)_ii/4.

A concrete continuous physical exclusion follows: d_a,d_b≤3/5 together with Λ_ba,Λ_ca,Λ_ab,Λ_cb≥19/20 is impossible. The first two lower moments are each at least 121/120, contradicting their sum≤2. Independence from every earlier combined necessary identity is not asserted.

**Common-row energy over every positive pole circuit.** Define symmetric W with W_aa=0 and, for s=Λ_ab,t=Λ_ba,

```text
W_ab=(s+t−2st)/(1−st) when st<1; W_ab=1 when s=t=1.
```

The boundary definition is justified by the actual two-roof inequality; it is not asserted to be the path-independent limit of the rational expression. Eliminating the two original sides from that lift yields (4/(5H_ab))11ᵀ−[[t,1],[1,s]]⪰0. Hence st≤1, 5H_ab(1−st)+4(s+t)≤8, W_ab≥max(s,t), and 5H_ab+4W_ab≤8. The repeated-roof bound gives H_aa≤8/5. Therefore

```text
A:=8J−5H−4W ≥0 entrywise.                                        (R1)
```

Since I+Λᵀ is entrywise positive and HΛᵀ=4J−H,

```text
A(I+Λᵀ)=12J−4W(I+Λᵀ),  so W(I+Λᵀ)≤3J entrywise.                 (R2)
```

The diagonal is the parent's nonlinear energy Φ_a=∑Λ_ajW_aj≤3; at F9 the 72 off-diagonal entries are additional coupled bounds. They imply ΛΛᵀ≤J+(5/4)H entrywise and (ΛΛᵀ)_ab+W_ab≤3. These entrywise statements are not signed PSD differences.

More strongly, every normalized nonnegative pole balance satisfies

```text
z≥0, 1ᵀz=1, Qᵀz=0  ⇒  Wz≤(3/4)1.                               (R3)
```

Indeed Hz=1, so multiply R1 by z. The complete balance polytope is equivalently

```text
Z(Λ)={z≥0:1ᵀz=1, Λᵀz=d},  d_i=(Λ²)_ii/4.
```

For the converse, Λᵀz=d−diag(d)CQᵀz, and C has rank three. These four affine equations have rank four. Thus every vertex has support at most four. At F9, solving all subsets of sizes 2,3,4—at most 246 subsets—covers every positive-pole circuit and hence the entire continuous balance domain. Lower-support circuits cover degeneracies. The nine row balances (e_b+Λ[b,:]ᵀ)/4 are strictly interior points of this five-dimensional polytope; their convex hull does not cover its boundary vertices.

For every positive z∈Z, the symmetric nonnegative matrix diag(√z)Wdiag(√z) sends √z to at most (3/4)√z. Perron comparison gives W⪯(3/4)diag(z)⁻¹. At F≥5 this is strict: W is irreducible, and at least one row inequality is strict. In particular

```text
Wd≤(9/4)1,   W≺(9/4)diag(d)⁻¹.                                  (R4)
```

The physical equality classification is exact: equality in any entry [W(I+Λᵀ)]_ab=3, or in (Wd)_a=9/4, holds precisely when F_a is a pyramid base. Positivity forces the entire a-th row of A to vanish, hence H_aa=8/5. To identify equality geometrically, use the four-dimensional lift 0≤t≤Y_a. Its floor-cone fraction at its own centroid is H_aa/8≤1/5. The sharp facet-cone inequality follows by integrating concavity of the fourth root of inward remaining volume; equality makes the lift a pyramid over its floor. Every original vertex off F_a creates an off-floor lift vertex, so P has exactly one vertex off F_a. Conversely a centered pyramid base has d_a=3/4, Λ_ja=1, Λ_aj=4d_j/3, H_aj=4/5 and W_aj=1, giving the zero row. At F>4 at least one facet is not a pyramid base: two different bases would contain all but their respective apex vertices, so their common edge would contain all but two vertices, forcing at most four vertices. This proves strict Perron comparison. The row and mass constants are attained by nine-facet octagonal pyramids; the spectral constant is a sharp supremum near tetrahedra.

There is also a strict nonnegative-affine common-row inequality. C=J+(5/4)H−ΛΛᵀ is entrywise positive for F≥5. Equality in C_ab would force every positively weighted directed gap 8−5H_aj−4Λ_aj to vanish. For j distinct from a,b, the pair determinant then gives −4st²(s−1)²≥0, with s=Λ_aj,t=Λ_ja>0, hence s=1. If a≠b there are F−2 such entries plus Λ_ab>0, contradicting row sum 3. The diagonal case similarly forces F−1 entries equal to 1. By affine linear-program duality, every nonzero nonnegative affine f=a+bᵀx has f=∑z_iY_i with z≥0; a nonnegative constant remainder is represented using Yᵀω=1. Therefore

```text
∑_i(d_i E_Fi f)² < a²+(5/4)E_P f², for F≥5.
```

This is positivity on nonnegative affine densities, not a signed Loewner bound. For the centered cube, Q has rows (e₁,−e₁,e₂,−e₂,e₃,−e₃), Λ=(J−QQᵀ)/2, H=J+QQᵀ/3 and C=3J/4−QQᵀ/12. The signed vector (1,−1,0,0,0,0) gives −1/3. The factor 5/4 is a sharp supremum at nine facets by the actual E17 family below, whose tetrahedral limit has Λ=J−I and H=(4/5)(I+J).

The exact common-energy control is an actual octagonal pyramid with base vertices (−2,−1),(−1,−2),(1,−2),(2,−1),(2,1),(1,2),(−1,2),(−2,1), apex (0,0,1), own centroid (0,0,1/4), and M=N=I. It checks common Q,Σ,Λ,H,d, all 81 row inequalities, nine mass inequalities, strict signed spectral positivity and all 12 positive circuits.

A separate coefficient control isolates the extra force of R2: split nine indices into groups of sizes 2,3,4, put zero on the diagonal and use symmetric block values

```text
[[1/10,362/375,1/1000],
 [362/375,251/750,1/10],
 [1/1000,1/10,1349/1500]].
```

All rows sum to 3, all off-diagonals are below 1, every old Φ_a and row squared norm is below 3, but [W(I+Λᵀ)]₀₁=3+8968/335335. Its rank is nine. It is explicitly a separation from independent coefficient energies, not a physical or common-rank-four control.

**Sharp rank-three pole-scatter inequality.** Put s=∑q_i, S=∑q_iq_iᵀ and k=F−4>0. Actual row energy gives ∑Λ_aj²<3. For any projection x_i=vᵀq_i, center the F−1 other coefficients at 3/(F−1) and their projected poles at their mean. Use ∑Λ_ajx_j=−x_a and Cauchy with ∑(Λ_aj−3/(F−1))²<3−9/(F−1). Expansion yields the signed physical inequality

```text
4k q_aq_aᵀ+3ssᵀ ⪯ 3kS.                                         (S1)
```

The scalar difference is strictly positive unless all other projected poles are equal. Its kernel is the orthogonal complement of their affine span. It is PD except when all poles other than a lie in one affine plane, exactly when F_a is a pyramid base; then its rank is two. This uses actual rank three. At F9,V10,E17 a pyramid is impossible, because an F9 pyramid has V9,E16, so all nine S1 differences are PD on that slice.

For completeness, the strict row-energy premise follows from 5H_aj+4Λ_aj≤8: multiply by Λ_aj and use HΛᵀ=4J−H to obtain ∑Λ_aj²≤1+5H_aa/4≤3. Equality would make every off-diagonal pair gap vanish, forcing every Λ_aj=1 by the pair determinant, and row sum 3 would force F=4.

Set T=S−ssᵀ/k. S1 gives T⪰(4/3)q_aq_aᵀ for all a. Since the poles span three dimensions, T is PD; hence q_aᵀT⁻¹q_a≤3/4, with at least one strict inequality. If r=sᵀS⁻¹s, Sherman–Morrison gives

```text
3+r/(k−r)=tr(T⁻¹S)<3F/4,
r<3(F−4)²/(3F−8).                                                (S2)
```

At F9,

```text
r<75/19,
Qᵀ(75I−19J)Q ≻0,
19·1ᵀG1 <75 tr G.                                               (S3)
```

The nine cheaper scalar forms from S1 are 20G_aa+3·1ᵀG1≤15tr G. Along an escape tree the root has greatest norm, so the root form dominates these nine scalar cuts. Every statement retains the same arbitrary reciprocal SPD pair.

**A sharpness barrier on a complete genuine E17 incidence.** Define, in the literal order,

```text
DELTA=((1,-1,0),(1,0,-1),(0,1,-1),
       (-1,1,0),(-1,0,1),(0,-1,1))
HEIGHT=(0,0,0,1,1,0)
q_i(ε)=(1,1,1)+ε*DELTA_i+ε²*HEIGHT_i*(1,1,1), i=0,...,5
q_6=(1,-1,-1), q_7=(-1,1,-1), q_8=(-1,-1,1)
0<ε≤1/10.
```

Take the actual body defined by these nine supports, integrate its own centroid g_ε, and recenter with the correct poles q_i'=q_i/(1−q_iᵀg_ε). Throughout the entire interval the body has exactly V10,E17,F9, with seven quadrilateral facets, two triangular facets and four nonsimple vertices. Its complete vertex active-facet sets are

```text
[(0,1,3,4),(0,1,6),(0,4,5),(0,5,6,8),(1,2,3),
 (1,2,6,7),(2,3,7),(3,4,7,8),(4,5,8),(6,7,8)].
```

No canonical catalogue alias or parallelogram property is assigned. This is not the parent's octagon-based E17 incidence.

The complete-domain certificate examines all 84 support triples by exact polynomial Cramer formulas. After orienting each nonzero determinant, required signs are certified by expanding (1+t)^m p(t/[10(1+t)]). Every accepted sign polynomial has nonnegative rational coefficients, at least one positive coefficient, and p(1/10)>0. This proves strict sign over 0<ε<1/10 and checks the endpoint separately. Identically zero slacks retain nonsimple incidence. Every rejected triple has a certified negative slack; every accepted triple has its complete active set and positive other slacks. Every vertex has three independent active normals, so this enumeration is complete. Two listed vertices share a true edge precisely when they share two active facets, giving all seventeen edges.

The cluster poles are exposed against (1,1,1)+DELTA_i, with gap at least ε−3ε²>0. The other three remain exposed against themselves. The cluster average is (1+ε²/3)(1,1,1), so the original tetrahedron lies inside their hull and the origin is interior. This separately proves boundedness and maximality throughout the interval.

As ε↓0, the actual bodies and their own centroids tend to the centered tetrahedron. The centered pole multiplicities tend to (6,1,1,1), so S→4I+5v₀v₀ᵀ and s→5v₀, v₀=(1,1,1), giving r→75/19. **Thus the constant in S2 cannot be improved merely by restricting to this complete actual E17 incidence.**

Exact physical audits at ε=1/10,1/100,1/1000 integrate actual volume covariance, facet centroids and K_i; check rank H=4, rank K_i=3, K_iω=λ_i, the common K sum; and verify 810 scalar true-edge flux identities through degree two. The fixed metric is M=[[5,1,2],[1,4,1],[2,1,6]], with leading principal minors 5,19,97, and N is its exact inverse. The r values are approximately 3.7531188808, 3.9274733537, 3.9453744540. These bodies have four or five stable facets under that metric and are not monostability witnesses. Uniform sharpness of the scalar trace constant over metrics follows by taking v=S⁻¹s and N=vvᵀ+δI as δ↓0; the fixed metric audit itself is not claimed to attain that ratio.

Every facet in this incidence has at most four vertices, so no pair covers all ten vertices. Pair-equality geometry therefore gives Λ_ab+Λ_ba<2 for all pairs. Nevertheless the actual adjacent old pair 6,7 has sum tending to 2. Thus this incidence supplies no uniform improvement of the pair constant either. The capsule also preserves the simpler coplanar six-pole split, with HEIGHT=0, whose actual controls have V8,E15,F9 and the same sharp limit; those also are not S1 witnesses.

**Exact sector proofs and complete continuous coverage.** The inherited scalar cap is the literal parent's actual affine facet trace theorem, Λ_aj≤c₃<10/9, where

```text
c₃=max_{r≥0} 3(1+2r+3r²)/[(1+r+r²)(3+2r+r²)].
```

It concerns actual uniform-volume and facet-area measures. The strict comparison follows from

```text
10(1+r+r²)(3+2r+r²)−27(1+2r+3r²)
=(r−7/15)²(10r²+118r/3+203/15)+44r/675+178/3375.
```

Each selected actual row lies in its closed capped simplex: x_a=0, other x_j∈[0,10/9], ∑x_j=3. Its 168 vertices are precisely the permutations of (10/9,10/9,7/9,0,0,0,0,0). At a vertex all but at most one coordinate are at bounds; the sum forces this pattern. Insert 1 at index a to get w=e_a+x. Convex averaging gives Qᵀw=0 for the actual row.

For an escape i→j use L_ij=2e_ie_iᵀ−e_ie_jᵀ−e_je_iᵀ, whose contraction with G is nonpositive. A mandatory nonpositive shadow uses −L_ij. Norm sectors use their literal diagonal forms. The new physical forms are 20e_ae_aᵀ+3J−15I and 19J−75I, also with nonpositive contractions. For every row vertex the recovery supplies common integer gamma vectors, offsets O_a with ∑O_a=0, and nonnegative integer multipliers, such that the exact denominator-cleared matrix

```text
B_(a,w)=D[γ_awᵀ+wγ_aᵀ+O_a+∑_k μ_(a,w,k)L_k]
```

satisfies B_(a,w)−I≻0. The complete sources contain their precise scaling conventions. Average over each actual row's convex decomposition and sum the selected rows. The gamma terms annihilate against G, offsets cancel, and every remaining contraction is nonpositive. But the averaged matrix is PD and G is nonzero PSD, so the contraction is strictly positive: contradiction. This establishes physical impossibility on the whole covered domain; it does not identify relaxed arrays as bodies.

For 266, the mandatory 33 negative pairs are exactly

```python
p=(0,0,1,2,3,4,5,4,0)
optional={(5,7),(6,7),(7,5),(7,6)}
NEG=[(i,j) for i in range(9) for j in range(i)
     if j!=p[i] and (i,j) not in optional]+[(i,8) for i in range(1,8)]
```

They lie outside the tree and every one of its three frames. The sectors α≤3/8, α≥1/2, β≤1/16, β≥1/2 use rows [0], [0,1], [0,1], [0,1], respectively. Their norm forms are e₁e₁ᵀ−(3/8)e₀e₀ᵀ, (1/2)e₀e₀ᵀ−e₁e₁ᵀ, e₈e₈ᵀ−(1/16)e₀e₀ᵀ, and (1/2)e₀e₀ᵀ−e₈e₈ᵀ. The last three use the new root energy form. There are 1176 matrices and 10584 positive leading minors. The 198 frozen gamma/offset integers and every local completion parameter are included in the capsule.

For 272, use rows 0 and 2. The root simplex has the additional halfspace 2x₁+x₈≥1/3 and exactly 228 vertices; row 2 has 168. At a cut-slack vertex at most one coefficient is between bounds; at a cut-active vertex at most two are, with independent sum and cut equations. This gives the complete cover. An independent exact enumeration starts from the 168 original vertices and all 588 genuine simplex edges; 120 crossing edges plus retained vertices give exactly the same 228 root vertices. All 396 matrices and 3564 leading minors pass. This sector needs no negative shadows or new spectral premise. Its complete frozen coefficient data are 6462 bytes with unpack format `<63h3168H`.

For 278, only row 0 is used. The three domains have 168,168,84 vertices and denominators 36,18,72. A box intersected with one sum hyperplane has a vertex only when all but at most one coordinate are fixed at a literal bound; this also gives the complete cover after the respective coefficient lower bound. The α≤1/4 record uses eight tree forms, −e₁e₁ᵀ and e₁e₁ᵀ−e₀e₀ᵀ/4. Each coefficient record uses eight tree forms and all ten new physical Gram forms. All 420 matrices and 3780 leading minors pass.

Separate workers audited the spectral proof, certificate signs and scaling, OJ coverage for 266, and the independent 272 cover. The 266 and 278 numerical procedures are only certificate producers; their outputs are accepted by exact arithmetic and pinned bytes. Whole-domain locator failures prove neither feasibility nor impossibility.

**Unresolved complement and continuation.** No whole new form, map or root orbit has been removed. The journal's ten-frame/24-subgraph OJ frontier remains, with the additional restrictions in the opening table. TREE253 was left to the lead; its inherited region uses α=n₁/n₀, β=n₇/n₀ and is α>1/2, β<3/4. That is context, not a new certificate here.

I tried mandatory OJ negatives, norm partitions, coefficient halfspaces, common-row spectral cuts, exact row-polytope truncations from Cauchy bounds and paired-row multipliers. They produced the accepted sectors, but no whole-domain certificate. Exploratory failures are not promoted to durable controls. An intermediate branch formula transposed the facet-trace row of the density T_i−Y_i into a column; that formula is withdrawn. The correctly oriented trace vector is T_i d−Λ[i,:]ᵀ. No accepted certificate used the erroneous orientation.

The useful next step is to impose T4, the radical triple bounds and every positive-circuit test on the same Λ within the surviving sectors. Near reciprocal-pair equality, retain actual tilted facet moments, genuine incidence and covariance: these force the affine reflection above, information absent from independent rows. The E17 sharpness family proves that a smaller uniform 75/19 constant or a uniform pair gap cannot replace those additional same-body constraints.

**Complete recovery.** The following literal capsule contains all thirteen source/input files, every frozen datum, the numerical producers, both exact acceptance algorithms, actual moment controls and the full-interval incidence generator. No parent file or download is needed. It flattens two encodings without changing their algorithms: the triple audit reads the included `mixed_lift_exact.py`, and the 272 verifier reads the included binary coefficient file; their exact bytes are pinned in the source manifest.

Reference environment: CPython 3.12.14. The 266 and 278 producers additionally require numpy 2.3.5, scipy 1.17.0, threadpoolctl 3.6.0, with OpenBLAS 0.3.30, one thread and SkylakeX selection. Nondefault parameters and integer rounding scales are in the included native sources. All other computations and exact acceptance use the standard library.

```text
python -m pip install numpy==2.3.5 scipy==1.17.0 threadpoolctl==3.6.0
python -S recover_vivid_next.py build > build.log
python -S recover_vivid_next.py check > check.log
```

Both commands passed in a fresh directory starting with only the capsule. `extract` is also supported. A different numerical reconstruction is rejected by the exact output pins, not silently accepted. The capsule is 33812 bytes, SHA-256 `b24a6e59e69d2073861ba9a0c924b6be14afbd39b7a10f66d1364ef5bd97f9d0`. Its complete uncompressed source archive is 81920 bytes, SHA-256 `c6b8d603ba6ac018b86c88836174a16eb63ddbc05717da0e6799a09f87e7cf99`. All fourteen exact output byte counts and hashes are literal in `OUTPUT` below. The leading-minor stream hashes for 266 and 272 are respectively `4eacae49276cee5189929beb4cce51dda55f615bdf1596592c08160e79cf4e5d` and `d780179aedc6e28b583774b701488c2e85e16d9760f7a098f7386875a77c0196`.

Observed clean build log: 5982 bytes, SHA-256 `69a48d84c81d43858e7a83ea2105679cdd27a8da2fc3b2d932f76555f1844848`. Observed exact check log: 5041 bytes, SHA-256 `713642a1825deb34662d9df84dc0b61927513059bd10bca0046c9437cd4b8a03`. Both exited zero. Decisive markers include:

```text
TRIPLE_LIFT_COMMON_MOMENTS_EXACT_PASS
COMMON_RECIPROCAL_ROW_ENERGY_V1_PASS
E17_SPECTRAL_SHARPNESS_DOMAIN_V1_PASS
N266_ALL_THREE_OJ_FRAMES_CLOSED_NORM_FRONTIER_PASS 1176 10584
TREE272_IMPLIES_2_LAMBDA01_PLUS_LAMBDA08_LT_1_OVER_3_PASS
N278_EXACT_BAREISS_AND_FRACTION_LDL_PASS_420_BLOCKS_3780_MINORS
VIVID_14_EXACT_OUTPUT_PINS_PASS
VIVID_COMMON_MOMENTS_AND_THREE_TREE_FRONTIERS_COMPLETE_PASS
```

Convenience copies are vivid_raven_common_moments_handoff.md and recover_vivid_next.py. The complete literal recovery follows; no encoded bytes or helpers are omitted.


[Encoded source block omitted; the code in this passage is incomplete.]
