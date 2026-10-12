# minimum-0144

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# GLOBAL_TRIANGLE_METRIC_AND_CENTROID_SEPARATION_V1

## Determination

**The parent’s mixed triangle identities have an exact global interpretation: nine of them reconstruct the entire defect `MN−I`.** On the whole strict balanced domain, stacking all84 identities and all48 product circuits therefore enforces one reciprocal metric, but supplies no additional centroid equation. Their selected-tree path consequences also have an exact boundary: they are already implied by exclusion of triangular stable-root leaves and simple unstable-root leaves. This is a theorem about globally selected complementary trees, not a statement about all available-arrow arguments.

**The missing mass information can be characterized sharply.** Fix the actual surface weights and the six true triangular area centroids. For EVERY two-apex/octagonal-base realization with ridge not parallel to the base, the common affine divergence identity forces the other three area centroids, and the completed cone first moment forces the TRUE uniform volume centroid. In the parallel-ridge case the precise residual is one axial false-center parameter. An exact continuous positive-contact family realizes that residual; it is not merely a rank estimate.

**A genuinely common-metric global control separates these two issues.** One exact balanced shape has a fully positive complementary9/8 tree pair, all local identities, and strict110/weak000 at a specified interior reference. Its actual uniformly filled own-centroid census is instead334/weak000. An explicit positive two-level NONUNIFORM density realizes the reference as its genuine mass centroid. A whole closed19-parameter box retains this separation. Thus this is NOT a homogeneous110 construction or a false positive of every uniform-centroid relaxation: the control explicitly fails the necessary uniform support-ratio bound.

The useful successor is the metric-versus-mass separation theorem, the full nonparallel mass-compatibility sector, its exact parallel exception, and the precise selected-tree overlap—not a new minimum bound. The full homogeneous balanced joint problem remains unresolved.

## 1. Sources, exact domain, and evidence boundary

The complete1945-line update, common and branch memory, and the literal parent `minimum-0141` were read consecutively through EOF. The update is347732 bytes, SHA-256 `a728d2394f9b97ebda967cccd51aeaf50b2657088e2266cb609ec5857c804527`. The parent’s declared immutable SHA-256 is `e79d71a14bb612f97a157af9fbb102ae49960c17325b2c53f40bac3d1d824d41`. Its literal title is **BALANCED_TRIANGULAR_RECIPROCAL_CIRCUITS_V1**; the branch’s descriptive alias `TRIANGLE_RECIPROCAL_PRODUCT_AND_SCALARIZATION_LIMIT_V1` is not its literal title. No mathematical datum conflicts. The readable17089-byte parent source is present and matches its accepted pin; it was not routinely rerun. No missing archive or computational dependency is used below.

The parent’s actual mixed identity, its four-distinct-edge product consequence, and its scalarization limitation are inherited premises. Their precise statements include the VF boundary and do not claim full selected-pattern coverage. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

For clarity the complete balanced chart is restated. Choose eight positive cuts `((sx,sy),(wx,wy),(nx,ny),(ex,ey))`, with

` sx+ex<2, wx+nx<2, sy+wy<2, ny+ey<2, a>0. `

Set

```text
P0=(-1+sx,-1,0)       P1=(-1,-1+sy,0)
P2=(-1,1-wy,0)        P3=(-1+wx,1,0)
P4=(1-nx,1,0)         P5=(1,1-ny,0)
P6=(1,-1+ey,0)        P7=(1-ex,-1,0)
P8=(-a,0,1)           P9=(a,0,1),
Y_i=P_i/(1+u P_ix+v P_iy).
```

All ten denominators must be positive; u,v are real. The actual maximal facets, in the fixed labels used below, are

```text
F0=(0,1,2,3,4,5,6,7)
F1=(0,8,1) F2=(1,8,2) F3=(2,8,3) F4=(3,8,9,4)
F5=(4,9,5) F6=(5,9,6) F7=(6,9,7) F8=(7,9,8,0).
```

Their cycles determine17 TRUE edges. This is the accepted full type(5,5) cover; the unbalanced types(3,7),(4,6) are not silently assigned these labels. :contentReference[oaicite:2]{index=2}

Let `K=conv(Y_i)`, V its actual uniform volume, g its actual uniform centroid. At an interior reference c write `X_i=Y_i−c` and `q_f=n_f/(b_f−n_f·c)`, where `n_f·Y≤b_f` are actual unnormalized support inequalities. Mechanical calculations always use one M>0 and N=M⁻¹. A reference c different from g is explicitly labelled as such; its mechanics is not presented as homogeneous own-COM mechanics. The actual polar is never independently recentered.

## 2. Global metric theorem: the triangle residual IS the inverse defect

First temporarily let M and N be independent SPD matrices. This is an algebraic diagnostic, not a physical relaxation being asserted exact.

At a true triangular facet `F=conv{x,y,z}`, pole q, take the actual neighboring pole r across xz and p across xy. Define

```text
δ_y=1−r·y>0, δ_z=1−p·z>0,
a=xᵀM(y−x), b=yᵀM(z−y), ℓ=(y−x)ᵀM(y−x),
s=qᵀNq, χ=s(xᵀMx)−1,
E_y=qᵀN(r−q), E_z=qᵀN(p−q).
```

### Theorem 1 — exact residual and global reconstruction

Without assuming N=M⁻¹,

**(1)** `χ+s a−(a+ℓ)E_y/δ_y−(a+ℓ+b)E_z/δ_z = yᵀ(MN−I)q`.

Consequently choose three triangular facets with independent poles. For each use three parent identities whose middle vertex runs through that facet’s three vertices. These NINE equations are equivalent to `MN=I`.

**Proof of (1).** The point f=Nq/s always lies in aff(F), since q·f=1. Its unique affine coordinates satisfy

`λ_y=−E_y/(sδ_y), λ_z=−E_z/(sδ_z), λ_x=1−λ_y−λ_z`.

The left side of(1) expands as

` s[xᵀMy+λ_y(yᵀMy−xᵀMy)+λ_z(yᵀMz−xᵀMy)]−1 `

` =s yᵀMf−1 =yᵀMNq−1. `

Since q·y=1, this is the claimed defect. No false Cauchy sign for independent M,N is used. When N=M⁻¹ the parent’s zero identity and χ≥0 are recovered.

For reconstruction, let `V_f` have the three facet vertices as rows and let r_f be the corresponding three residuals. A true triangular facet whose supporting plane avoids the interior origin gives invertible V_f. With E=MN−I,

`V_f⁻¹ r_f=E q_f`.

For `Q3=[q_f1,q_f2,q_f3]`,

**(2)** `E=[V_f1⁻¹r_f1,V_f2⁻¹r_f2,V_f3⁻¹r_f3] Q3⁻¹`.

The determinant of this nine-dimensional residual map, with compatible column-major ordering, is

`det(Q3)^3 ∏_j det(V_fj) ≠0`.

This concerns the full nine-dimensional algebraic defect E; it is NOT a claim of nine independent constraints on six symmetric entries of N for fixed M.

### Full balanced scope

Use F1,F2,F3, all incident to apex8. Their unnormalized normals satisfy on the ENTIRE strict chart

**(3)** `det(n1,n2,n3)=−sx wx(2−sy−wy)(1−u a)<0`.

The last factor is exactly the positive denominator of apex8. Thus there is no excluded slope, cut size, apex separation, projective direction, or mechanical wall. Alternatively, three distinct extreme poles on one actual polar facet are noncollinear and hence linearly independent because its plane avoids0.

The84 parent identities reduce to30 distinct vertex/facet defect pairings:18 from the six primal triangles,24 from the eight triangular polar facets, with12 overlaps. The four missing incidences are precisely

`(8,F4),(8,F8),(9,F4),(9,F8)`.

Equations(2) already force those four as well. Every parent product-circuit equation is a rewriting of the same residual by norm telescoping. Therefore **adding all these identities globally exactly restores common reciprocity, but cannot impose uniform centering**. This does not prevent mixed-product positivity from interacting usefully with separate, genuine mass constraints.

The nine-equation argument also applies to the two unbalanced octagonal-base types: one apex is incident to at least three of the six actual triangles. The numerical labels,84/48 counts and exact control below are balanced only.

## 3. Global tree theorem: the local path tests collapse to root-leaf tests

Let T be a selected true-edge primal spanning tree and T* its complementary dual spanning tree, both oriented toward their selected roots. Suppose all selected escape arrows are nonnegative. Their norms increase STRICTLY along each directed edge even at a zero derivative.

### Theorem 2 — exact selected-pair overlap

If two boundary edges of a true triangular facet F are selected primal, its pole has degree1 in T*. If F is not the stable root, its only dual edge is already directed OUT of F. If F is the root, the triangle’s two primal arrows contradict strict stability. The dual statement holds for the triangular polar facet of a simple primal vertex.

In particular, once triangular stable-root leaves and simple unstable-root leaves are removed, **every parent direct four-arrow circuit and every parent longer-path clause using ONLY selected-tree paths is automatically avoided**.

**Proof.** A true triangle has three dual incident edges. Exactly two are absent from T*, so its dual degree is1. The two selected primal orientations are a chain or a converging fork: a diverging fork would give two outgoing selected arrows at one vertex. If the dual leaf is not the root, its unique edge is outward. A selected path from its neighbor back to it is therefore impossible; in particular the parent’s two-path obstruction cannot occur.

If the leaf is the root, all other pole norms are strictly smaller, hence the root is strictly stable. Let f be its actual interior foot. For a chain x→y→z, the tangent vector y−f has strictly positive M-pairing with all three tangent vertex vectors, using the two weak arrow inequalities. For a fork x→y←z the same follows from the two incoming arrows. This contradicts the strictly positive barycentric relation among x−f,y−f,z−f. The same proof on the actual polar excludes an unstable simple root of primal degree1. It requires no polar mass centroid.

This explains the inherited triangular root-leaf theorem rather than renaming it. :contentReference[oaicite:3]{index=3} It is distinct from the centroid-dependent theorem excluding an outside root whose sole child is the other apex.

### Complete native overlap audit, not a registry subtraction

The source enumerates all `C(17,9)=24310` candidate primal edge subsets in the displayed labels, verifies connected primal/dual complements, and checks all10×9 root choices for each tree. Exact results:

```text
unrooted primal trees                         4095
raw labelled complementary rooted pairs     368550
simple unstable-root leaf                   132300
triangular stable-root leaf                 135900
both leaf conditions                         50700
union of the two leaf conditions            217500
parent direct four-circuit flag               78168
parent selected longer-path chain flag      150184
neither root-leaf condition                  151050
```

Every direct flag implies a longer-path flag; every longer-path flag lies in the root-leaf union. All151050 root-leaf-clean pairs satisfy all corresponding chain/fork selected-path implications. These151050 are **not** asserted feasible, globally unexcluded, or disjoint from other accepted closures. No FULL/LOCAL/tree410/global-root ledger delta follows. The complete generator, labels, template list and deterministic full-pair stream hash are in the recovery.

This theorem does not cover arbitrary AVAILABLE arrows outside the selection, additional quantitative norm/slack information, or products coupled to actual moments. Those remain possible sources of genuinely new exclusions.

## 4. Actual mass theorem: six triangle means close the nonparallel sector

The metric theorem does not by itself select the reference. The next result identifies exactly what genuine surface information does.

Use actual unnormalized supports `n_f·Y≤b_f`. Put

`w_f=Area(F_f)/||n_f||>0`, `C_f=actual uniform area centroid of F_f`.

These weights are fixed by the real geometry; they are not independently fitted cone masses. Direct divergence and actual facet triangulation give

```text
Σ w_f n_f=0,
Σ w_f C_f n_fᵀ=V I,
Σ w_f b_f=3V,
Σ w_f b_f C_f=4V g.
```

Hence at an arbitrary interior c,

**(4)** `Σ w_f(b_f−n_f·c)(C_f−c)=4V(g−c)`.

Consider candidate means `Ctilde_f∈aff(F_f)` that agree with the actual mean on ALL SIX triangular facets and obey the SAME affine divergence identity

`Σ w_f Ctilde_f n_fᵀ=V I`.

Only the base and two ridge quadrilateral means may differ.

### Theorem 3 — full nonparallel closure and exact parallel exception

**Nonparallel ridge.** If the ridge is not parallel to the base, all three remaining means are forced to be their ACTUAL means. If the common completed cone first moment is0, then c=g exactly.

**Parallel ridge.** If the ridge is parallel to the base, the only possible change of these three weighted means has the form

**(5)** `[w_f(Ctilde_f−C_f)]_{f=B,Q+,Q−}=t e κᵀ`,

where e is parallel to the true ridge and κ spans the one-dimensional relation among these three normals. The completed zero-first-moment condition is equivalent to

**(6)** `c=g+[t(κ·b)/(4V)]e`.

Here κ·b≠0. The possible false references therefore form exactly an axial interval subject to the actual facet-containment and interior-reference restrictions. A sufficiently small interval about g is genuinely available. One correct axial component of any one of the three remaining means removes it.

**Proof.** Set `R=[n_B,n_Q+,n_Q−]`, and let U have columns `w_f(Ctilde_f−C_f)` for these three facets. All triangle contributions are unchanged, so `URᵀ=0`.

The two quadrilateral planes intersect along the true ridge. R is invertible exactly when that line is not parallel to the base plane. In that case U=0, and(4) forces c=g.

In the parallel case rankR=2. None of the three normal-relation coefficients is0, since each pair of these planes meets in a true edge and has independent normals. Thus `U=a κᵀ`. Because every changed mean remains in its own plane, `n_f·a=0` for all three f, so a=t e along the ridge. The offsets have κ·b≠0: otherwise the three plane equations would have a common line, contradicting the disjoint parallel base and ridge. Substituting into(4), or expanding the common completed first moment, yields `4V(g−c)+t(κ·b)e`, proving(6). Actual area means lie in the relative interiors of their facets, so small signed t remain admissible.

This is a whole-geometric-sector theorem, not an isolated fibre: it applies to all three octagonal-base/two-apex incidence types, all actual metrics, all root choices and all mechanical weak walls. It is a **centroid-compatibility theorem**, not an exclusion of S=U=1 in that sector.

### Explicit balanced reconstruction

In the complete balanced chart,

`det R=2u`.

Thus the nonparallel sector is exactly u≠0, with no other omitted shape condition. If

`K0=V I−Σ_triangles w_f C_f n_fᵀ`,

then the three true missing weighted means are explicitly

**(7)** `[w_B C_B,w_Q+ C_Q+,w_Q− C_Q−]=K0 R⁻ᵀ`.

This closes the relevant false-facet-mean freedom using the true triangle means and true area weights. It does not license replacing the actual w_f by arbitrary positive numbers. In u=0, a relation is

`κ=(2,1−v,1+v), κ·b=2`,

and positivity of the basal denominators gives |v|<1.

## 5. Six signed tetrahedra: the required mass cancellation has a sign

For the nonparallel case let O be the intersection of the base plane and the extended ridge. All three nontriangular support planes contain O. The actual signed boundary-fan formula therefore reduces to SIX tetrahedra, one per true triangular facet:

**(8)**

```text
ν_f = w_f(b_f−n_f·O)/3,
V = Σ_triangles ν_f,
4Vg = Σ_triangles ν_f [O+Σ_{i∈F_f}Y_i].
```

These are signed exact volume/first-moment formulas, not independently chosen masses or a positive fan at an interior apex. In the balanced chart `O=(1/u,0,0)`.

Every tetrahedron attached to the higher apex has positive ν_f, and every one attached to the lower apex has negative ν_f. To see this, translate O to0 and write the lower apex as t times the higher apex, 0<t<1. On a facet through the higher apex, strict support of the lower gives `t b_f<b_f`, hence b_f>0. On a facet through the lower, strict support of the higher gives `b_f/t<b_f`, hence b_f<0. Its w_f is positive in both cases.

Thus a proposed sum of local nonnegative triangle products cannot silently use these six coefficients as positive multipliers. The actual cancellation between the two apex blocks is essential. As u→0, O escapes to infinity; the separate signed moments need not stay bounded even though V,g do. Dropping that cancellation would also erase the real axial exception in Theorem3.

For the exact control below, O=(−100/21,0,0), higher apex9, and the six signed volumes in facet order1,2,3,5,6,7 are

```text
−1437500000000/2437435142373,
−906250000000/3064287799881,
−50000000000/47783900031,
 2000000000000/947532106017,
 1437500000000/678008751147,
 2875000000000/1223309992671.
```

The exact source checks their sum and full first moment against both genuine positive apex integrations.

## 6. A fully compatible global reference pair, and its actual homogeneous companion

Use the exact terminating-rational input

```text
(sx,sy,wx,wy,nx,ny,ex,ey,a,u,v)
=(.18,1.38,1.15,.33,.67,.16,.18,1.61,.27,−.21,−.66),
L=((1,0,0),(1/10,119/50,0),(−101/50,27/20,79/25)),
M=L Lᵀ,
N=L⁻ᵀ L⁻¹,
c=(−23/50,−1/2,7/500).
```

This is the parent’s11-shape checkpoint with a DIFFERENT metric and a deliberately distinguished reference. Explicitly,

```text
M=((1,1/10,−101/50),
   (1/10,7093/1250,3011/1000),
   (−101/50,3011/1000,31777/2000)).
```

The rational physical affine map is A=Lᵀ. At reference c the physical body is A(K−c); its actual uniform centroid is A(g−c), not0. Its rational poles are L⁻¹q_f(c).

The exact volume is

`V=831029321026158812776613018750000000/178745809468888532386940039010475509`.

The actual uniform centroid, regenerated rather than transported, is

```text
gx=1241631989974360947308333582022021599459150549407366324165025/
   1440417053858924468932907515488976554777461630465003208896318,
gy=5272726637881288057842671281738583427844092415713175/
   4128750776323077495560868008921706748028488250778268,
gz=3669230030700827264556703976997500/
   13253722450756560401136089813154413.
```

For orientation only, g≈(.8619947859,1.2770755426,.2768452444). In particular gz−cz>1/4 exactly.

The full true-feature censuses are

```text
At the designated reference c:
  S={F1}, U={5}, H={}, physical weak=0, zero primitives=0.

At the ACTUAL UNIFORM CENTROID g:
  S={F0,F3,F6}, U={5,7,8},
  H={(0,8),(2,3),(4,9),(6,7)}, physical weak=0, zero primitives=0.
```

The latter is the actual homogeneous own334 control; the former is NOT a homogeneous own110.

### Complete globally converging selected pair

The reference pair has parent arrays

```text
PV=(7,2,3,4,5,5,5,6,9,4), U-root5,
PQ=(1,1,1,2,3,6,7,8,1), S-root1.
```

All17 selected arrows are strictly positive at the SAME actual reciprocal pair:

```text
Primal:
0→7, 1→2, 2→3, 3→4, 4→5, 9→4, 6→5, 7→6, 8→9.
Polar:
F0→F1, F8→F1, F2→F1, F3→F2, F4→F3,
F5→F6, F6→F7, F7→F8.
```

They partition ALL17 true physical edges; the primary lex-edge mask is77482. This is not separate feasibility of two aggregates or a convexified inverse.

The active local selected implications are explicit. F5 has primal9→4→5 and its opposite selected escape is F5→F6. The polar triangle at vertex0 has the fork F0→F1←F8 and its opposite escape is0→7. At vertex1 the fork F0→F1←F2 has opposite escape1→2. Thus the nonbasal triangles and globally converging forests really coexist in the control.

### An honest stronger-test limitation

The reference control does NOT satisfy the uniform-centroid support-reflection condition: its base pole has

`q_B(c)·(Y9−c)=−4933969/66031<−3`.

It therefore does not refute a scheme that retains that necessary uniform condition, much less all actual volume moments. Its precise role is to prove that actual incidence, exact reciprocity, all triangle identities and a complete global positive pair can coexist before the correct homogeneous centroid is imposed.

### A genuine—but expressly nonuniform—mass realization

Set T=1000, ε=1/1000 and

```text
p=c+(c−g)/T,
H=p+ε(K−g),
ρ(Y)=1+10^12·1_H(Y).
```

The small homothet H is strictly inside K. Its true volume is ε³V and its centroid is p. Hence total mass is1001V and

`[Vg+10^12 ε³V p]/(1001V)=c`.

Thus A(K−c), filled with the displayed two-level positive NONUNIFORM density, is a genuine own-density110/weak000 body. The internal density interface is not an outer mechanical facet or edge. This is not an attaining construction for the uniform problem.

For external context only, weighted mono-monostatic representatives for every legal non-tetrahedral f-vector were already proved by Almádi–Dawson–Domokos–Regős, *On equilibria of tetrahedra*, Theorem5, arXiv2304.06984v1. That is an f-vector statement, not a theorem for every prescribed combinatorial class. The present use is the exact labelled balanced common-metric comparison and explicit density—not a priority claim for weighted existence. :contentReference[oaicite:4]{index=4}

### Whole closed counterdomain

All nineteen coordinates

`(cuts8,a,u,v,L21,L22,L31,L32,L33,cx,cy,cz)`

may vary independently within10⁻⁶ of the displayed rational center. Exact outward rational arithmetic on the fixed2⁻¹⁰⁰ grid certifies294 strictly positive guards on the WHOLE closed box. They retain the strict geometric domain, actual positive apex cells/supports, positive pole heights at both references, all17 reference tree arrows, all68 own334 primitive signs, gz−cz>1/4, and containment of the same density construction.

Throughout the box the reference and explicitly weighted body have110/weak000, whereas the homogeneous body has its own334/weak000. Unselected reference primitives need not stay nonzero throughout the box; they remain harmless because each edge has a selected positive escape. This is a robust counterdomain for a center-unconstrained method, not a positive homogeneous outer-domain exclusion.

## 7. Exact parallel exception and actual reference walls

### Positive-contact false means on a complete interval

Take all eight cuts1/2, a=1,u=v=0. Then

```text
V=11/6, g=(0,0,15/44),
w_B=7/2, w_Q+=w_Q−=3/2,
C_B=(0,0,0), C_Q±=(0,±4/9,5/9).
```

For EVERY `|s|≤1/100`, set

```text
c(s)=g+s e1,
Ctilde_B=C_B+(44s/21)e1,
Ctilde_Q±=C_Q±+(22s/9)e1,
```

leaving all six triangle means unchanged. These are exactly Theorem3’s one-dimensional solutions. The source constructs strictly positive facet–vertex contact weights representing these altered means, retaining the actual cone masses `w_f(b_f−n_f·c)/V`, common affine divergence, and zero completed first moment. Every support and positive quadrature condition holds on the whole closed interval. Yet the true uniform centroid stays g, not c(s) for s≠0.

With the same displayed L, all references on this interval have

`S={F0,F2,F4,F6,F8}, U={4,7,8}, H={(0,8),(1,2),(3,8),(4,9),(5,6),(7,9)}`,

strict536, weak000, all68 primitives nonzero. The physical body centered at g is genuinely own536. Other references are explicitly non-own references, not extra homogeneous constructions. The false means are positive contact completions, NOT claimed to be real area centroids.

The continuous proof is not three-point sampling: the altered vertex quadratures, reference support heights and cleared mechanical rows are affine in s; endpoint positivity and the analytic identities certify the full interval. This negative control shows why the parallel exception in Theorem3 cannot be suppressed.

### Complete reference chamber and event audit

For fixed actual K,M, let `h_f(c)=b_f−n_f·c`. The primal escape rows are affine in c. After multiplying a polar escape by the positive `h_f(c)^2 h_h(c)`, its numerator is also affine:

```text
primal i→j:
Y_iᵀM(Y_j−Y_i)−cᵀM(Y_j−Y_i),

polar f→h, α=n_fᵀNn_f, β=n_fᵀNn_h:
β b_f−α b_h+(α n_h−β n_f)·c.
```

Thus the17 selected positive rows and nine interior support inequalities define an exact OPEN CONVEX reference chamber for the full pair. This is a reference-space fact, not a permission to replace actual g.

The source audits the WHOLE segment `c(t)=(1−t)c+t g`,0≤t≤1:24 event/endpoints,47 strata, eight VE walls, ten EF walls, four harmless-zero walls, no VF. The first wall is

```text
35201844668559929961747312887668078410611532614845663771759046990317/
71041067571383234906835449979568450986628163186120206794663921029157817.
```

There the reference has strict110 PLUS one VE at vertex7 on edge(6,7); immediately afterwards the reference census is121/weak000. This is NOT a homogeneous weak110 candidate or an own-centroid deformation. The exact event method is retained as an ancillary audit, not presented as the main research advance.

## 8. Actual verification, uncertainty, and continuation

The five principal reference/own/parallel records have independently reconstructed actual maximal hull facets, the actual polar hull at the same origin, both genuine positive volume/first-moment fans, rational physical affine maps and fresh physical mass checks. All17 true edge feet and normal-cone coefficients satisfy `M p=λ_f q_f+λ_h q_h`; strict features and weak points are fully audited and duplicate physical points merged. Across these records the source checks420 triangle and240 product identities. The47 reference strata additionally receive full exact physical-packet audits. A deliberately independent positive perturbation of N is detected and reconstructed by the nine-residual map.

The universal metric and mass theorems have the analytic proofs above; the finite records are not substituted for those proofs. The294 box guards are exact outward intervals, not sampled positivity. The native tree audit is exhaustive for its literal labelled objects, not a claim to have reopened or recomputed the entire external registry.

The optional locator uses only the first three fixed-shape metric draws with seed20260920. Its third trial produced the checkpoint rounded to the exact L,c above. Floating discovery is not acceptance; the independent rational audit supplies acceptance. Broader exploratory searches did not yield a homogeneous110 and provide no exclusion theorem. No missing floating checkpoint is needed to recover any claimed object.

The decisive remaining issue is now explicit. The local identities can already recover global reciprocity, and their selected-tree sign/path consequences are absorbed by root-leaf compatibility. What they do not automatically supply is a contradiction with the **same actual uniform mass**. In the entire nonparallel sector the six true triangle means and true surface weights recover that mass exactly, but the external-ridge reconstruction necessarily uses signed apex blocks. A useful next proof must couple those actual weights/cancellations—or an equivalent genuine positive fan—to the remaining globally compatible mechanical patterns. Reweighting identities solely inside one star, adding their redundant selected-tree path clauses, or freely completing the nontriangle means will not do so.

No homogeneous110, whole balanced exclusion, all-SPD exclusion of the nineteen-dimensional control box, or new registry delta is claimed. The accepted internal interval34≤C_min≤622 remains unchanged.

## 9. Complete source-only recovery

Save the following THREE complete readable files with their indicated names, UTF-8/LF with one final LF. The exact files have no parent-source, archive, connector, report-download or originating-sandbox dependency. Assertions must be enabled.

```sh
python -S global_triangle_bridge.py build
python -S global_triangle_bridge.py check
python -S triangle_tree_overlap.py build
python -S triangle_tree_overlap.py check
```

Executed exact environment: CPython3.13.5, standard library only. Both ordinary build/check and fresh source-only build/check were completed and matched byte for byte. The optional discovery replay, also executed in the fresh directory, uses NumPy2.3.5/SciPy1.17.0 and one BLAS/OMP thread:

```sh
python locate_global_triangle.py
```

Its exact seed, distributions, three-trial limit, MILP bounds/tolerances and rounding rules are all in that complete third file. None is an exact proof dependency.

```text
global_triangle_bridge.py 21216 bytes
8bfa5e510cbbe9dfba8ad4ca78f5beecb908c79fc9f7bc936bd66d1edd2cdb34
triangle_tree_overlap.py 4781 bytes
6b035f76ee9c5fb7f54f5ad789c7d7480c807ce092d45d35c93cab0352d6ad0e
locate_global_triangle.py 3775 bytes
23bb0070802718b4aeeb4391206413fc2129b7c1dbeee0a92ed49d12e769308d
global_triangle_bridge.json 659835 bytes
c487e9780ad0c9da4394f80a956e000d9057b18515ad956c953841aec3634a7e
triangle_tree_overlap.json 2864 bytes
0a6fe1fbb11cba2f5252aa44cd50490fab2f180989d5d77dfedd663bb117d56e
locate_global_triangle.json 691 bytes
ea79f9cea8d86be3ca19f4754e8b90722c98ad9943390150dc9e303c06a841c7
```

Expected terminal markers include


[Encoded source block omitted; the code in this passage is incomplete.]


### global_triangle_bridge.py

```python
"""GLOBAL_TRIANGLE_METRIC_AND_CENTROID_SEPARATION_V1.
CPython3.13.5 standard library; assertions enabled; no input files.
Parent minimum-0141, SHA256
 e79d71a14bb612f97a157af9fbb102ae49960c17325b2c53f40bac3d1d824d41.
Run python -S global_triangle_bridge.py build|check.
The reference110 control is NOT an own-uniform-centroid110 body.
Its homogeneous companion is334; explicit positive NONUNIFORM density
realizes the designated reference as its mass centroid.
"""
from fractions import Fraction as F
from itertools import combinations,permutations
from pathlib import Path
import json,hashlib,sys
assert __debug__
FAC=((0,1,2,3,4,5,6,7),(0,8,1),(1,8,2),(2,8,3),(3,8,9,4),(4,9,5),(5,9,6),(6,9,7),(7,9,8,0))
ED=tuple(sorted({tuple(sorted((f[i],f[(i+1)%len(f)]))) for f in FAC for i in range(len(f))}))
EF=tuple(tuple(f for f,vs in enumerate(FAC) if i in vs and j in vs) for i,j in ED)
PE=dict(zip(ED,EF));QE={tuple(sorted(fs)):e for e,fs in zip(ED,EF)}
SHAPE=tuple(map(F,('.18','1.38','1.15','.33','.67','.16','.18','1.61','.27','-.21','-.66')))
LPAR=tuple(map(F,('.10','2.38','-2.02','1.35','3.16')))
REF=tuple(map(F,('-.46','-.50','.014')))
SELECT=(2,0,3,0,3,0,3,0,3,0,1,1,2,1,2,2,0)
PV=(7,2,3,4,5,5,5,6,9,4);PQ=(1,1,1,2,3,6,7,8,1)
GRID=1<<100
EPS=F(1,10**6)
DENSITY_T=F(1000);DENSITY_R=F(1,1000)

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,c):return tuple(c*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def tr(A):return tuple(zip(*A))
def mv(A,x):return tuple(dot(a,x) for a in A)
def mm(A,B):return tuple(tuple(dot(a,b) for b in tr(B)) for a in A)
def ma(A,B):return tuple(add(a,b) for a,b in zip(A,B))
def ms(A,c):return tuple(mul(a,c) for a in A)
def outer(a,b):return tuple(tuple(x*y for y in b) for x in a)
def det(A):return dot(A[0],cross(A[1],A[2]))
def inv(A):
 d=det(A)
 return tuple(tuple((A[(j+1)%3][(i+1)%3]*A[(j+2)%3][(i+2)%3]-A[(j+1)%3][(i+2)%3]*A[(j+2)%3][(i+1)%3])/d for j in range(3)) for i in range(3))
def eye():return tuple(tuple(F(i==j) for j in range(3)) for i in range(3))
def bil(x,M,y):return dot(x,mv(M,y))
def sg(x):return (x>0)-(x<0)
def pd(A):
 assert A==tr(A);v=(A[0][0],A[0][0]*A[1][1]-A[0][1]**2,det(A));assert min(v)>0;return v

def mass(Y,root):
 D=0;J=(0,0,0)
 for f in FAC:
  if root in f:continue
  for j in range(1,len(f)-1):
   p=[Y[i] for i in (root,f[0],f[j],f[j+1])]
   d=det(tuple(sub(x,p[0]) for x in p[1:]));D+=d
   J=add(J,mul(tuple(sum(x[k] for x in p) for k in range(3)),d))
 return D/6,mul(J,1/(4*D))

def geometry(params):
 sx,sy,wx,wy,nx,ny,ex,ey,a,u,v=params
 P=((-1+sx,-1,0),(-1,-1+sy,0),(-1,1-wy,0),(-1+wx,1,0),(1-nx,1,0),(1,1-ny,0),(1,-1+ey,0),(1-ex,-1,0),(-a,0,1),(a,0,1))
 f=tuple(1+u*x+v*y for x,y,z in P);Y=tuple(mul(p,1/h) for p,h in zip(P,f))
 D=(0,sx+sy-sx*sy,1,wx+wy-wx*wy,1,nx+ny-nx*ny,1,ex+ey-ex*ey,1)
 raw=((0,0,-1),(-sy,-sx,D[1]-a*sy),(-1,0,1-a),(-wy,wx,D[3]-a*wy),(0,1,1),(ny,nx,D[5]-a*ny),(1,0,1-a),(ey,-ex,D[7]-a*ey),(0,-1,1))
 ns=tuple((n[0]+h*u,n[1]+h*v,n[2]) for n,h in zip(raw,D));V,g=mass(Y,8)
 return dict(params=params,P=P,den=f,Y=Y,ns=ns,offset=D,rawnormals=raw,V=V,g=g)

def metrics(p):
 b,c,d,e,f=p;L=((1,0,0),(b,c,0),(d,e,f));LI=((1,0,0),(-b/c,1/c,0),((b*e-c*d)/(c*f),-e/(c*f),1/f))
 return L,LI,mm(L,tr(L)),mm(tr(LI),LI)

def poles(z,c):
 h=tuple(d-dot(n,c) for n,d in zip(z['ns'],z['offset']))
 return tuple(mul(n,1/a) for n,a in zip(z['ns'],h)),h

def affine_rows(z,M,N):
 rows=[]
 for (i,j),(f,h) in zip(ED,EF):
  for x,y in ((i,j),(j,i)):
   e=sub(z['Y'][y],z['Y'][x]);rows.append((bil(z['Y'][x],M,e),mul(mv(M,e),-1)))
  for x,y in ((f,h),(h,f)):
   a=bil(z['ns'][x],N,z['ns'][x]);b=bil(z['ns'][x],N,z['ns'][y])
   rows.append((b*z['offset'][x]-a*z['offset'][y],sub(mul(z['ns'][y],a),mul(z['ns'][x],b))))
 return tuple(rows)

def at(row,c):return row[0]+dot(row[1],c)

def hull(V):
 fs=set()
 for i,j,k in combinations(range(len(V)),3):
  n=cross(sub(V[j],V[i]),sub(V[k],V[i]))
  if n==(0,0,0):continue
  h=tuple(dot(n,sub(v,V[i])) for v in V)
  if min(h)>=0 or max(h)<=0:fs.add(tuple(i for i,x in enumerate(h) if x==0))
 return fs

def surface(z):
 Y=z['Y'];out=[]
 for f,n in zip(FAC,z['ns']):
  k=next(i for i in range(3) if n[i]!=0);w=F(0);J=(F(0),)*3;lam={i:F(0) for i in f}
  for j in range(1,len(f)-1):
   ids=(f[0],f[j],f[j+1]);a,b,c=[Y[i] for i in ids];cr=cross(sub(b,a),sub(c,a));d=cr[k]/(2*n[k]);assert d>0 and cr==mul(n,2*d)
   w+=d;J=add(J,mul(add(add(a,b),c),d/3))
   for i in ids:lam[i]+=d/3
  out.append(dict(w=w,C=mul(J,1/w),lambda_vertex={i:q/w for i,q in lam.items()}))
 assert tuple(sum(r['w']*n[k] for r,n in zip(out,z['ns'])) for k in range(3))==(0,0,0)
 assert sum(r['w']*d for r,d in zip(out,z['offset']))==3*z['V']
 A=tuple(tuple(sum(r['w']*r['C'][i]*n[j] for r,n in zip(out,z['ns'])) for j in range(3)) for i in range(3))
 assert A==ms(eye(),z['V'])
 assert tuple(sum(r['w']*d*r['C'][i] for r,d in zip(out,z['offset'])) for i in range(3))==mul(z['g'],4*z['V'])
 return out

def tetra_checks(z):
 assert min(z['params'][:9])>0
 p=z['params'];assert max(p[0]+p[6],p[2]+p[4],p[1]+p[3],p[5]+p[7])<2
 assert min(z['den'])>0 and mass(z['Y'],9)==(z['V'],z['g']) and z['V']>0
 assert hull(z['Y'])=={tuple(sorted(f)) for f in FAC}
 for f,n,d in zip(FAC,z['ns'],z['offset']):
  assert all(dot(n,x)==d if i in f else dot(n,x)<d for i,x in enumerate(z['Y']))
 assert {tuple(sorted(set(f)&set(h))) for f,h in combinations(FAC,2) if len(set(f)&set(h))==2}==set(ED)
 # Whole-domain determinant factors from the actual normal-form geometry.
 sx,sy,wx,wy,nx,ny,ex,ey,a,u,v=z['params']
 assert det(tuple(z['ns'][i] for i in (1,2,3)))==-sx*wx*(2-sy-wy)*(1-u*a)
 assert det(tr(tuple(z['ns'][i] for i in (0,4,8))))==2*u


def one_identity(X,Q,emap,f,xyz,M,N):
 i,j,k=xyz;x,y,z=X[i],X[j],X[k];q=Q[f]
 r=next(h for h in emap[tuple(sorted((i,k)))] if h!=f)
 p=next(h for h in emap[tuple(sorted((i,j)))] if h!=f)
 dy=1-dot(Q[r],y);dz=1-dot(Q[p],z);assert dy>0 and dz>0
 a=bil(x,M,sub(y,x));b=bil(y,M,sub(z,y));s=bil(q,N,q);ell=bil(sub(y,x),M,sub(y,x));chi=s*bil(x,M,x)-1
 Ey=bil(q,N,sub(Q[r],q));Ez=bil(q,N,sub(Q[p],q))
 T=chi+s*a-(a+ell)*Ey/dy-(a+ell+b)*Ez/dz
 defect=bil(y,M,mv(N,q))-1;assert T==defect
 return dict(face=f,xyz=xyz,opposite=(r,p),slacks=(dy,dz),values=(a,b,Ey,Ez),chi=chi,ell=ell,s=s,residual=T)

def local_audit(X,Q,M,N):
 records=[];circuits=[]
 for side,V,W,E,A,B,faces in (('P',X,Q,PE,M,N,FAC),('Q',Q,X,QE,N,M,tuple(tuple(f for f,vs in enumerate(FAC) if i in vs) for i in range(10)))):
  for f,vs in enumerate(faces):
   if len(vs)!=3:continue
   for xyz in permutations(vs):
    r=one_identity(V,W,E,f,xyz,A,B);assert r['residual']==0 and r['chi']>=0
    records.append((side,r))
    i,j,k=xyz
    if sum(i in e for e in E)!=3:continue
    h,p=r['opposite'];q,rr,pp=W[f],W[h],W[p]
    other=QE if side=='P' else PE;assert tuple(sorted((h,p))) in other
    real=(tuple(sorted((i,j))),tuple(sorted((j,k))),other[tuple(sorted((p,h)))],other[tuple(sorted((h,f)))])
    if side=='Q':real=tuple(QE[tuple(sorted(e))] for e in real)
    assert len(set(real))==4 and all(e in ED for e in real)
    a,b=r['values'][:2];c=bil(pp,B,sub(rr,pp));d=bil(rr,B,sub(q,rr))
    m=bil(sub(rr,q),B,sub(rr,q));n=bil(sub(pp,rr),B,sub(pp,rr));o=bil(sub(pp,q),B,sub(pp,q))
    dy,dz=r['slacks'];ell=r['ell']
    terms=(r['chi'],r['s']*a,(a+ell)*(d+m)/dy,(a+ell+b)*(c+d+(m+n+o)/2)/dz)
    assert sum(terms)==0 and min(m,n,o)>0 and not all(t>=0 for t in (a,b,c,d))
    circuits.append((side,f,xyz,real,(a,b,c,d),terms))
 assert len(records)==84 and len(circuits)==48
 contacts={(r['xyz'][1],r['face']) if side=='P' else (r['face'],r['xyz'][1]) for side,r in records}
 missing={(i,f) for f,vs in enumerate(FAC) for i in vs}-contacts
 assert len(contacts)==30 and missing=={(8,4),(8,8),(9,4),(9,8)}
 return dict(triangles=records,four_circuits=circuits,distinct_contact_defects=sorted(contacts),four_missing_contacts_forced_by_gluing=sorted(missing))


def inverse_gluing(X,Q,M,N):
 records=[];columns=[]
 for f in (1,2,3):
  vs=FAC[f];res=[]
  for j in range(3):
   xyz=(vs[(j+2)%3],vs[j],vs[(j+1)%3])
   rec=one_identity(X,Q,PE,f,xyz,M,N);records.append(rec);res.append(rec['residual'])
  columns.append(mv(inv(tuple(X[i] for i in vs)),res))
 Q3=tr(tuple(Q[f] for f in (1,2,3)));error=mm(tr(columns),inv(Q3))
 jac=det(Q3)**3
 for f in (1,2,3):jac*=det(tuple(X[i] for i in FAC[f]))
 assert jac!=0
 assert error==ma(mm(M,N),ms(eye(),-1))
 return dict(nine_identities=records,reconstructed_MN_minus_I=error,determinant_of_nine_by_nine_defect_map=jac)


def audit(z,c,lpar,physical=True):
 L,LI,M,N=metrics(lpar);pd(M);pd(N);assert mm(M,N)==eye()
 X=tuple(sub(y,c) for y in z['Y']);Q,h=poles(z,c);assert min(h)>0
 assert hull(Q)=={tuple(f for f,vs in enumerate(FAC) if i in vs) for i in range(10)}
 rows=affine_rows(z,M,N);S=set(range(9));U=set(range(10));H=[];weak={};pack=[];zeros=0
 for ei,((i,j),(f,k)) in enumerate(zip(ED,EF)):
  ds=(bil(X[i],M,sub(X[j],X[i])),bil(X[j],M,sub(X[i],X[j])),bil(Q[f],N,sub(Q[k],Q[f])),bil(Q[k],N,sub(Q[f],Q[k])))
  assert tuple(at(rows[4*ei+t],c) for t in range(4))==(ds[0],ds[1],ds[2]*h[f]*h[f]*h[k],ds[3]*h[k]*h[k]*h[f])
  zeros+=sum(t==0 for t in ds)
  if ds[0]>=0:U.discard(i)
  if ds[1]>=0:U.discard(j)
  if ds[2]>=0:S.discard(f)
  if ds[3]>=0:S.discard(k)
  t=ds[0]/(ds[0]+ds[1]);p=add(X[i],mul(sub(X[j],X[i]),t))
  ff=bil(Q[f],N,Q[f]);fk=bil(Q[f],N,Q[k]);kk=bil(Q[k],N,Q[k]);dd=ff*kk-fk*fk;assert dd>0
  lam=((kk-fk)/dd,(ff-fk)/dd);assert mv(M,p)==add(mul(Q[f],lam[0]),mul(Q[k],lam[1]))
  assert (max(ds)<=0)==(0<=t<=1 and min(lam)>=0)
  r=dict(edge=(i,j),facets=(f,k),values=ds,t=t,foot=p,normal_coefficients=lam)
  if max(ds)<0:H.append((i,j))
  elif max(ds)<=0:
   if p not in weak:weak[p]=dict(point=p,packets=[])
   weak[p]['packets'].append(r)
  pack.append(r)
 feet={f:mul(mv(N,Q[f]),1/bil(Q[f],N,Q[f])) for f in S}
 assert all(all(dot(q,p)<1 for k,q in enumerate(Q) if k!=f) for f,p in feet.items())
 assert all(bil(X[i],M,sub(y,X[i]))<0 for i in U for j,y in enumerate(X) if j!=i)
 out=dict(reference=c,uniform_centroid_minus_reference=sub(z['g'],c),M=M,N=N,X=X,Q=Q,S=sorted(S),U=sorted(U),H=H,weak=list(weak.values()),zeros=zeros,packets=pack,stable_feet=feet)
 if physical:
  A=tr(L);AI=tr(LI);Y=tuple(mv(A,x) for x in X);qq=tuple(mv(LI,q) for q in Q)
  assert hull(Y)=={tuple(sorted(f)) for f in FAC}
  assert mass(Y,8)==mass(Y,9)==(det(A)*z['V'],mv(A,sub(z['g'],c)))
  assert all(dot(a,b)==bil(x,M,y) for a,x in zip(Y,X) for b,y in zip(Y,X))
  assert all(dot(a,b)==bil(x,N,y) for a,x in zip(qq,Q) for b,y in zip(qq,Q))
  out.update(physical_map=A,physical_vertices=Y,physical_poles=qq,physical_uniform_mass=mass(Y,8),local=local_audit(X,Q,M,N),gluing=inverse_gluing(X,Q,M,N))
 return out


def tree_check(parent,arrows):
 roots=[i for i,p in enumerate(parent) if i==p];assert len(roots)==1;root=roots[0]
 assert set(arrows)=={(i,p) for i,p in enumerate(parent) if i!=p}
 for i in range(len(parent)):
  seen=set()
  while i!=root:assert i not in seen;seen.add(i);i=parent[i]
 return root


def pair_check():
 pa=[];qa=[]
 for e,fs,k in zip(ED,EF,SELECT):
  if k<2:pa.append((e[k],e[1-k]))
  else:qa.append((fs[k-2],fs[3-k]))
 assert tree_check(PV,pa)==5 and tree_check(PQ,qa)==1 and len(pa)==9 and len(qa)==8
 witness=[]
 for side,faces,edges,parent,opar,emap in (('P',FAC,pa,PV,PQ,PE),('Q',tuple(tuple(f for f,vs in enumerate(FAC) if i in vs) for i in range(10)),qa,PQ,PV,QE)):
  eset={tuple(sorted(e)) for e in edges}
  for f,vs in enumerate(faces):
   if len(vs)!=3:continue
   chosen=[e for e in combinations(vs,2) if tuple(sorted(e)) in eset]
   if len(chosen)!=2:continue
   remain=next(tuple(sorted(e)) for e in combinations(vs,2) if tuple(sorted(e)) not in eset)
   nei=next(g for g in emap[remain] if g!=f)
   assert opar[f]==nei and f!=opar[f]
   orientations=[(a,b) if parent[a]==b else (b,a) for a,b in chosen]
   assert all(parent[a]==b for a,b in orientations)
   typ='fork' if orientations[0][1]==orientations[1][1] else 'chain'
   witness.append((side,f,typ,orientations,(f,nei)))
 return dict(primal=pa,polar=qa,PV=PV,PQ=PQ,primal_mask=sum(1<<i for i,k in enumerate(SELECT) if k<2),root_leaf_implications=witness)


def centroid_closure(z,area):
 non=(0,4,8);tri=(1,2,3,5,6,7);R=tr(tuple(z['ns'][f] for f in non));V=z['V']
 assert det(R)!=0
 K=ms(eye(),V)
 for f in tri:K=ma(K,ms(outer(area[f]['C'],z['ns'][f]),-area[f]['w']))
 recovered=mm(K,tr(inv(R)));assert recovered==tr(tuple(mul(area[f]['C'],area[f]['w']) for f in non))
 O=mv(inv(tr(R)),tuple(z['offset'][f] for f in non));assert O==(1/z['params'][9],0,0)
 signed=[];J=(F(0),)*3
 for f in tri:
  nu=area[f]['w']*(z['offset'][f]-dot(z['ns'][f],O))/3
  ids=FAC[f];dd=det(tuple(sub(z['Y'][i],O) for i in ids))/6;assert nu==dd
  J=add(J,mul(add(O,tuple(sum(z['Y'][i][k] for i in ids) for k in range(3))),nu))
  signed.append((f,nu))
 assert sum(x for f,x in signed)==V and J==mul(z['g'],4*V)
 reconstructed=mul(J,1/(4*V));assert reconstructed==z['g']
 higher=8 if z['Y'][8][2]>z['Y'][9][2] else 9
 assert all((nu>0)==(higher in FAC[f]) for f,nu in signed)
 return dict(nontriangle_normal_matrix=R,determinant=det(R),missing_surface_first_moments=recovered,external_point=O,signed_six_tetrahedra=signed,recovered_centroid=reconstructed)


def density(z,c):
 V=z['V'];g=z['g'];T=DENSITY_T;eps=DENSITY_R;p=add(c,mul(sub(c,g),1/T))
 small=tuple(add(p,mul(sub(y,g),eps)) for y in z['Y'])
 assert all(dot(n,y)<h for n,h in zip(z['ns'],z['offset']) for y in small)
 assert hull(small)==hull(z['Y']) and mass(small,8)==mass(small,9)==(eps**3*V,p)
 height=T/(eps**3);mass_total=V+height*eps**3*V
 J=add(mul(g,V),mul(p,height*eps**3*V));assert mul(J,1/mass_total)==c
 return dict(density='1 + height*indicator(small_homothet)',height=height,scale=eps,small_centroid=p,small_vertices=small,total_mass=mass_total,actual_density_centroid=c)


def reference_line(z,M,N):
 rows=affine_rows(z,M,N);c=REF;d=sub(z['g'],c)
 cut={F(0),F(1)}
 for a,b in rows:
  aa=a+dot(b,c);bb=dot(b,d)
  if bb and 0<-aa/bb<1:cut.add(-aa/bb)
 cut=sorted(cut);out=[]
 for j,t in enumerate(cut):
  for is_wall,v in ((True,t),)+(((False,(t+cut[j+1])/2),) if j+1<len(cut) else ()):
   rr=audit(z,add(c,mul(d,v)),LPAR,False)
   out.append(dict(t=v,wall=is_wall,S=rr['S'],U=rr['U'],H=rr['H'],weak=rr['weak'],zeros=rr['zeros']))
 return dict(events=cut,strata=out,meaning='REFERENCE path, NOT an own-uniform-centroid deformation')


class I:
 def __init__(self,a,b=None):
  a=F(a);b=a if b is None else F(b);assert a<=b
  self.lo=F((a.numerator*GRID)//a.denominator,GRID);self.hi=F(-((-b.numerator*GRID)//b.denominator),GRID)
 @staticmethod
 def cv(x):return x if isinstance(x,I) else I(x)
 def __add__(a,b):
  b=I.cv(b);return I(a.lo+b.lo,a.hi+b.hi)
 __radd__=__add__
 def __neg__(a):return I(-a.hi,-a.lo)
 def __sub__(a,b):return a+-I.cv(b)
 def __rsub__(a,b):return I.cv(b)+-a
 def __mul__(a,b):
  b=I.cv(b);v=(a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi);return I(min(v),max(v))
 __rmul__=__mul__
 def __truediv__(a,b):
  b=I.cv(b);assert b.lo*b.hi>0;return a*I(1/b.hi,1/b.lo)
 def __rtruediv__(a,b):return I.cv(b)/a

def box(zref,own):
 p=tuple(I(x-EPS,x+EPS) for x in SHAPE+LPAR+REF);z=geometry(p[:11]);L,LI,M,N=metrics(p[11:16]);c=p[16:];rows=affine_rows(z,M,N);guards=[]
 def keep(label,x):
  q=I.cv(x);assert q.lo>0,(label,str(q.lo),str(q.hi));guards.append((label,q.lo,q.hi))
 for j,x in enumerate(p[:9]):keep('positive_shape'+str(j),x)
 for j,(a,b) in enumerate(((0,6),(2,4),(1,3),(5,7))):keep('side'+str(j),2-p[a]-p[b])
 for j,x in enumerate(z['den']):keep('denominator'+str(j),x)
 keep('L22',p[12]);keep('L33',p[15]);keep('volume',z['V'])
 # All actual selected positive apex-fan cells; the other cells are absent.
 for apex in (8,9):
  for f,vs in enumerate(FAC):
   if apex in vs:continue
   for j in range(1,len(vs)-1):
    pts=[z['Y'][i] for i in (apex,vs[0],vs[j],vs[j+1])]
    keep('fan'+str((apex,f,j)),det(tuple(sub(x,pts[0]) for x in pts[1:])))
 for f,(n,d) in enumerate(zip(z['ns'],z['offset'])):
  keep('reference_poleheight'+str(f),d-dot(n,c));keep('own_poleheight'+str(f),d-dot(n,z['g']))
  for i,y in enumerate(z['Y']):
   if i not in FAC[f]:keep('support'+str((f,i)),d-dot(n,y))
 for i,k in enumerate(SELECT):keep('chosen_escape'+str(i),at(rows[4*i+k],c))
 for i,row in enumerate(rows):keep('own_sign'+str(i),at(row,z['g'])*sg(own['packets'][i//4]['values'][i%4]))
 keep('uniform_center_separation',z['g'][2]-c[2]-F(1,4))
 # The same actual two-level density works on the ENTIRE box.
 cc=add(c,mul(sub(c,z['g']),1/DENSITY_T))
 for f,(n,d) in enumerate(zip(z['ns'],z['offset'])):
  for j,y in enumerate(z['Y']):keep('dense_copy_inside'+str((f,j)),d-dot(n,add(cc,mul(sub(y,z['g']),DENSITY_R))))
 return dict(epsilon=EPS,dimension=19,grid=GRID,guards=guards,guard_count=len(guards))


def parallel_control():
 params=(F(1,2),)*8+(F(1),F(0),F(0));z=geometry(params);tetra_checks(z);a=surface(z)
 assert z['V']==F(11,6) and z['g']==(0,0,F(15,44))
 non=(0,4,8);k=(F(2),F(1),F(1));d=(F(1),F(0),F(0));R=tr(tuple(z['ns'][i] for i in non))
 assert mv(R,k)==(0,0,0) and det(R)==0 and dot(k,tuple(z['offset'][i] for i in non))==2
 cases=[]
 for s in (F(-1,100),F(0),F(1,100)):
  c=add(z['g'],mul(d,s));C=[r['C'] for r in a];lam=[dict(r['lambda_vertex']) for r in a]
  for f,kk in zip(non,k):
   shift=2*z['V']*s*kk/a[f]['w'];C[f]=add(C[f],mul(d,shift))
   i,j=(3,4) if f==0 else (8,9);length=z['Y'][j][0]-z['Y'][i][0]
   lam[f][i]-=shift/length;lam[f][j]+=shift/length
  assert all(all(v>0 for v in l.values()) and sum(l.values())==1 for l in lam)
  assert all(tuple(sum(l[i]*z['Y'][i][j] for i in l) for j in range(3))==cc for l,cc in zip(lam,C))
  assert all(C[f]==a[f]['C'] for f in (1,2,3,5,6,7))
  A=tuple(tuple(sum(r['w']*cc[i]*n[j] for r,cc,n in zip(a,C,z['ns'])) for j in range(3)) for i in range(3))
  assert A==ms(eye(),z['V'])
  Q,h=poles(z,c);X=tuple(sub(y,c) for y in z['Y']);mu=[{i:r['w']*hh*l[i]/z['V'] for i in l} for r,hh,l in zip(a,h,lam)]
  assert tuple(sum(sum(m.values())*q[j] for m,q in zip(mu,Q)) for j in range(3))==(0,0,0)
  B=tuple(tuple(sum(v*q[i]*X[k][j] for m,q in zip(mu,Q) for k,v in m.items()) for j in range(3)) for i in range(3));assert B==eye()
  assert tuple(sum(v*X[k][i] for m in mu for k,v in m.items()) for i in range(3))==(0,0,0)
  rr=audit(z,c,LPAR);cases.append(dict(s=s,reference=c,fake_centroids=C,contact_weights=mu,mechanics=rr))
 assert all(tuple(sg(v) for p in r['mechanics']['packets'] for v in p['values'])==tuple(sg(v) for p in cases[1]['mechanics']['packets'] for v in p['values']) for r in cases)
 # Positivity/containment are affine in s before the positive h-factor;
 # endpoint checks certify the entire CLOSED interval, not three samples.
 return dict(geometry=z,area=a,normal_relation=k,interval=(F(-1,100),F(1,100)),cases=cases)


def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return list(map(enc,x))
 return x

def main():
 assert sys.argv[1:] in (['build'],['check']);z=geometry(SHAPE);tetra_checks(z);a=surface(z)
 ref=audit(z,REF,LPAR);own=audit(z,z['g'],LPAR)
 assert (ref['S'],ref['U'],ref['H'],ref['weak'],ref['zeros'])==([1],[5],[],[],0)
 assert (own['S'],own['U'],own['H'],own['weak'],own['zeros'])==([0,3,6],[5,7,8],[(0,8),(2,3),(4,9),(6,7)],[],0)
 for i,k in enumerate(SELECT):assert ref['packets'][i]['values'][k]>0
 pair=pair_check();closure=centroid_closure(z,a);heterogeneous=density(z,REF)
 ref['base_min_pairing']=min(dot(ref['Q'][0],x) for x in ref['X'])
 assert ref['base_min_pairing']<-3
 # This countercontrol does NOT pass the necessary uniform-centroid
 # Minkowski support-ratio condition; no stronger relaxation is refuted.
 v=(F(1),F(2),F(3));badN=ma(ref['N'],ms(outer(v,v),F(1,100)));pd(badN)
 test=inverse_gluing(ref['X'],ref['Q'],ref['M'],badN);assert test['reconstructed_MN_minus_I']!=ms(eye(),0)
 b=box(z,own);line=reference_line(z,ref['M'],ref['N']);parallel=parallel_control()
 out=dict(name='GLOBAL_TRIANGLE_METRIC_AND_CENTROID_SEPARATION_V1',geometry=z,surface=a,reference_control=ref,uniform_control=own,positive_pair=pair,centroid_closure=closure,nonuniform_density=heterogeneous,independent_N_detected=test,box=b,reference_line=line,parallel_boundary=parallel)
 raw=(json.dumps(enc(out),sort_keys=True,separators=(',',':'))+'\n').encode();path=Path(__file__).with_suffix('.json')
 if sys.argv[1]=='build':path.write_bytes(raw)
 else:assert path.read_bytes()==raw
 print('REFERENCE_STRICT110_IS_NOT_UNIFORM_COM_UNIFORM_STRICT334_PASS')
 print('NINE_LOCAL_TRIANGLE_RESIDUALS_RECONSTRUCT_GLOBAL_MN_MINUS_I_PASS')
 print('SIX_TRIANGLE_CENTROID_RECONSTRUCTION_EXACT_CONTROL_PASS')
 print('SELECTED_TREE_TRIANGLE_PATH_IMPLICATIONS_ARE_ROOT_LEAF_IMPLICATIONS_PASS')
 print('WHOLE_CLOSED_19_PARAMETER_REFERENCE_DENSITY_COUNTERDOMAIN_PASS',b['guard_count'])
 print('PARALLEL_RIDGE_EXACT_ONE_DIMENSIONAL_FALSE_MEAN_FAMILY_PASS')
 print('REFERENCE_LINE_EVENTS_STRATA',len(line['events']),len(line['strata']))
 print(path.name,len(raw),hashlib.sha256(raw).hexdigest())
 print('GLOBAL_TRIANGLE_METRIC_AND_CENTROID_SEPARATION_RECOVERY_PASS')
if __name__=='__main__':main()
```

### triangle_tree_overlap.py

```python
"""Exact native balanced tree/circuit-overlap audit, NOT a registry update.
CPython3.13.5 stdlib. Requires the complete global_triangle_bridge.py unit.
python -S triangle_tree_overlap.py build|check
"""
from itertools import combinations,permutations
from pathlib import Path
from collections import Counter
import json,hashlib,sys
from global_triangle_bridge import FAC,ED,EF,PE,QE,PV,PQ,SELECT
assert __debug__

def orientation(n,edges,root):
 adj=[[] for _ in range(n)]
 for a,b in edges:adj[a].append(b);adj[b].append(a)
 p=[-1]*n;p[root]=root;todo=[root]
 for v in todo:
  for w in adj[v]:
   if p[w]<0:p[w]=v;todo.append(w)
 if len(todo)!=n:return None
 assert len(edges)==n-1
 return tuple(p)

def ancestors(p):
 out=[]
 for i in range(len(p)):
  s=set()
  while i not in s:s.add(i);i=p[i]
  out.append(s)
 return out

def templates():
 t=[];direct=[]
 for side,faces,emap,other in ((0,FAC,PE,QE),(1,tuple(tuple(f for f,vs in enumerate(FAC) if i in vs) for i in range(10)),QE,PE)):
  for f,vs in enumerate(faces):
   if len(vs)!=3:continue
   for x,y,z in permutations(vs):
    r=next(h for h in emap[tuple(sorted((x,z)))] if h!=f)
    p=next(h for h in emap[tuple(sorted((x,y)))] if h!=f)
    rec=(side,x,y,z,p,r,f);t.append(rec)
    if sum(x in e for e in emap)!=3:continue
    assert tuple(sorted((p,r))) in other
    e=(tuple(sorted((x,y))),tuple(sorted((y,z))),other[tuple(sorted((p,r)))],other[tuple(sorted((r,f)))])
    real=e if side==0 else tuple(QE[tuple(sorted(ee))] for ee in e)
    assert len(set(real))==4 and all(ee in ED for ee in real)
    direct.append(rec)
 assert len(t)==84 and len(direct)==48
 return t,direct

def run():
 ts,ds=templates();counts=Counter();digest=hashlib.sha256();witness=None
 for ids in combinations(range(17),9):
  mask=sum(1<<i for i in ids);ee=tuple(ED[i] for i in ids)
  if orientation(10,ee,0) is None:continue
  qe=tuple(EF[i] for i in range(17) if not(mask>>i)&1)
  assert orientation(9,qe,0) is not None;counts['unrooted_trees']+=1
  ps=[orientation(10,ee,u) for u in range(10)];qs=[orientation(9,qe,s) for s in range(9)]
  pa=list(map(ancestors,ps));qa=list(map(ancestors,qs))
  dp=[sum(i in e for e in ee) for i in range(10)];dq=[sum(f in e for e in qe) for f in range(9)]
  for u,pv in enumerate(ps):
   for s,pq in enumerate(qs):
    badp=(u<8 and dp[u]==1);badq=(len(FAC[s])==3 and dq[s]==1);leaf=badp or badq
    haspath=False;hasdirect=False
    for side,x,y,z,p,r,f in ts:
     a,b,anc=(pv,pq,qa[s]) if side==0 else (pq,pv,pa[u])
     if a[x]==y and a[y]==z and f in anc[p] and f in anc[r]:haspath=True;break
    for side,x,y,z,p,r,f in ds:
     a,b=(pv,pq) if side==0 else (pq,pv)
     if a[x]==y and a[y]==z and b[p]==r and b[r]==f:hasdirect=True;break
    assert not hasdirect or haspath
    assert not haspath or leaf
    if not leaf:
     # The chain/fork version of every TWO-boundary-edge triangle test
     # already has the mandatory opposite-tree OUTGOING edge.
     for side,faces,ee0,emap,a,b in ((0,FAC,ee,PE,pv,pq),(1,tuple(tuple(f for f,vs in enumerate(FAC) if i in vs) for i in range(10)),qe,QE,pq,pv)):
      selected={tuple(sorted(e)) for e in ee0}
      for f,vs in enumerate(faces):
       if len(vs)!=3:continue
       boundary=[tuple(sorted(e)) for e in combinations(vs,2)]
       if sum(e in selected for e in boundary)!=2:continue
       missing=next(e for e in boundary if e not in selected);nei=next(g for g in emap[missing] if g!=f)
       assert b[f]==nei and b[f]!=f
    counts['rooted_pairs']+=1;counts['bad_simple_U_leaf']+=badp;counts['bad_triangle_S_leaf']+=badq
    counts['both_leaf']+=badp and badq;counts['leaf_union']+=leaf
    counts['direct_four_circuit']+=hasdirect;counts['long_path_chain']+=haspath;counts['root_leaf_clean']+=not leaf
    digest.update(f'{mask},{u},{s},{int(badp)},{int(badq)},{int(hasdirect)},{int(haspath)}\n'.encode())
    if pv==PV and pq==PQ:
     assert u==5 and s==1 and not leaf and not haspath and not hasdirect
     witness=dict(mask=mask,U=u,S=s,PV=pv,PQ=pq)
 assert counts['unrooted_trees']==4095 and counts['rooted_pairs']==368550 and witness is not None
 return dict(name='NATIVE_BALANCED_TRIANGLE_TREE_OVERLAP_NOT_REGISTRY_DELTA',facets=FAC,edges=ED,counts=dict(counts),all_pair_stream_sha256=digest.hexdigest(),reference_realized_pair=witness,triangular_templates=ts,direct_four_templates=ds)

if __name__=='__main__':
 assert sys.argv[1:] in (['build'],['check']);out=run()
 raw=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode();path=Path(__file__).with_suffix('.json')
 if sys.argv[1]=='build':path.write_bytes(raw)
 else:assert path.read_bytes()==raw
 print(out['counts']);print(path.name,len(raw),hashlib.sha256(raw).hexdigest())
 print('ALL_368550_NATIVE_PAIRS_DIRECT_AND_PATH_CIRCUITS_SUBSUMED_BY_ROOT_LEAVES_PASS')
```

### locate_global_triangle.py

```python
"""Optional NONPROOF fixed-body reference locator. CPython3.13.5,
NumPy2.3.5, SciPy1.17.0. One BLAS/OMP thread. No input files.
Replays precisely the first three metric trials used for the rational
reference control. This NEVER asserts a uniform own-centroid110 body.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from pathlib import Path
import hashlib,json
from fractions import Fraction
FAC=((0,1,2,3,4,5,6,7),(0,8,1),(1,8,2),(2,8,3),(3,8,9,4),(4,9,5),(5,9,6),(6,9,7),(7,9,8,0))
ED=tuple(sorted({tuple(sorted((f[i],f[(i+1)%len(f)]))) for f in FAC for i in range(len(f))}))
EF=tuple(tuple(k for k,f in enumerate(FAC) if i in f and j in f) for i,j in ED)
TRI=np.array([(8,f[0],f[j],f[j+1]) for f in FAC if 8 not in f for j in range(1,len(f)-1)])
FT=np.array([f[:3] for f in FAC])
assert __debug__

def geometry():
 sx,sy,wx,wy,nx,ny,ex,ey,a,u,v=(.18,1.38,1.15,.33,.67,.16,.18,1.61,.27,-.21,-.66)
 P=np.array([[-1+sx,-1,0],[-1,-1+sy,0],[-1,1-wy,0],[-1+wx,1,0],[1-nx,1,0],[1,1-ny,0],[1,-1+ey,0],[1-ex,-1,0],[-a,0,1],[a,0,1]],float)
 f=1+u*P[:,0]+v*P[:,1];Y=P/f[:,None]
 T=Y[TRI];d=np.abs(np.linalg.det(T[:,1:]-T[:,:1]));g=d@T.sum(axis=1)/(4*d.sum());X=Y-g
 Q=np.linalg.solve(X[FT],np.ones((9,3,1)))[:,:,0]
 T=X[TRI];w=np.abs(np.linalg.det(T[:,1:]-T[:,:1]));s=T.sum(axis=1)
 Sigma=(np.einsum('k,ki,kj->ij',w,s,s)+np.einsum('k,kni,knj->ij',w,T,T))/(20*w.sum())
 return X,Q,Sigma,g

def solve(X,Q,M):
 N=np.linalg.inv(M);R=[]
 for (i,j),(f,h) in zip(ED,EF):
  for i0,j0 in ((i,j),(j,i)):
   d=X[j0]-X[i0];R.append(np.r_[X[i0]@M@d,-M@d])
  for f0,h0 in ((f,h),(h,f)):
   b=Q[f0]@N@Q[h0];a=Q[f0]@N@Q[f0]
   R.append(np.r_[b-a,a*Q[h0]-b*Q[f0]])
 R=np.array(R);scale=np.max(np.abs(R[:,:1]+R[:,1:]@X.T),axis=1);assert np.all(scale>0);R=R/scale[:,None]
 C=[];lo=[];hi=[]
 for k,(c,*v) in enumerate(R):
  r=np.zeros(72);r[:3]=v;r[3]=-1;r[4+k]=-2
  C.append(r);lo.append(-2-c);hi.append(np.inf)
 for i in range(17):
  r=np.zeros(72);r[4+4*i:8+4*i]=1;C.append(r);lo.append(1);hi.append(np.inf)
 for q in Q:
  r=np.zeros(72);r[:3]=-q;r[3]=-max(1-X@q);C.append(r);lo.append(-1);hi.append(np.inf)
 cost=np.zeros(72);cost[3]=-1
 res=milp(cost,integrality=np.r_[np.zeros(4),np.ones(68)],bounds=Bounds(np.r_[X.min(0),0,np.zeros(68)],np.r_[X.max(0),.1,np.ones(68)]),constraints=LinearConstraint(np.array(C),lo,hi),options={'time_limit':10.0,'mip_rel_gap':.0001})
 return res

def main():
 X,Q,Sigma,g=geometry();C=np.linalg.cholesky(Sigma);CI=np.linalg.inv(C)
 rng=np.random.default_rng(20260920);trials=[]
 for k in range(3):
  R,_=np.linalg.qr(rng.normal(size=(3,3)));ev=np.exp(rng.uniform(-2,2,3));M=CI.T@R@np.diag(ev)@R.T@CI
  r=solve(X,Q,M);e=None if r.x is None else float(r.x[3]);trials.append(dict(metric=k,status=int(r.status),margin=e))
  if e is None or e<=1e-6:continue
  assert k==2
  L=np.linalg.cholesky(M/M[0,0]);c=r.x[:3]+g
  rounded_L=[str(Fraction(str(round(float(x),2)))) for x in (L[1,0],L[1,1],L[2,0],L[2,1],L[2,2])]
  rounded_c=[str(Fraction(str(round(float(x),2 if j<2 else 3)))) for j,x in enumerate(c)]
  assert rounded_L==['1/10','119/50','-101/50','27/20','79/25'] and rounded_c==['-23/50','-1/2','7/500']
  out=dict(name='NONPROOF_REFERENCE_LOCATOR',seed=20260920,trials=trials,raw_M=M.tolist(),raw_L=L.tolist(),raw_reference=c.tolist(),rounded_L=rounded_L,rounded_reference=rounded_c)
  raw=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode();p=Path(__file__).with_suffix('.json');p.write_bytes(raw)
  print('REFERENCE_LOCATOR_ROUNDS_TO_EXACT_INPUT_PASS');print(p.name,len(raw),hashlib.sha256(raw).hexdigest());return
 raise AssertionError('Numerical replay did not find the pinned reference control')
if __name__=='__main__':main()
```

Supplemental copies: [complete readable handoff](sandbox:/mnt/data/global_triangle_handoff.md), [source and exact reports](sandbox:/mnt/data/global_triangle_handoff.zip), and [main exact generator/verifier](sandbox:/mnt/data/global_triangle_bridge.py). The three source blocks above are the complete recovery; these copies are conveniences.
