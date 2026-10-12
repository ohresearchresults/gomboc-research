# figure-0128

AI research report · 2026-08-28 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Quantitative refinement-plus-Santaló handoff

## Result type and decisive delta

No accepted finite homogeneous polyhedral Gömböc was produced. The run’s gate requires a materialized finite H/V representation, exact own-volume centroid, grouped maximal faces and true edges, an exhaustive positive-margin face/vertex/edge audit, an independent exact or directed verifier, and matching meshes; neither a smooth body nor an unexpanded astronomical generator qualifies.

This direction nevertheless closes the quantitative part of the refinement-plus-Santaló bridge and localizes the remaining obstruction to one finite combinatorial object:

1. **The materialized cumulative axial ladder is quantitatively obstructed.** Its strongest level moves by `90.66453549010153` weakest-margin units under the true Santaló correction. Keeping a factor-four reserve would require suppressing its degree-one response by `362.6581419604061×`. All ten saved levels fail after true centring.
2. **Curvature, active-star diameter, exact dyadic target primitives, support error, and normalized Santaló displacement do close at an explicit finite scale.** Among the tested uniform cubed-sphere levels, level `19` gives a conditional root/chamber factor `3.2035528738770935`; level `20` gives `23.9056467237352` and a factor-ten reserve. Level `18` provably consumes the noncritical separator.
3. **The exact remaining obstruction is not centring.** It is a missing finite collar/cross-seam incidence complex. Its rebuilt *actual* maximal faces, nonsimple full normal cones, and true edges must all have the prescribed signs with margin at least `1.915868198716011e-6`, while its support deficit stays inside the stated `L¹` budget. No such collar lattice, complete H/V reconstruction, or mesh is present in this result.

The journal records an earlier branch-complete but unexpanded theorem with fewer than `2^391` rows and six common-separator classes. It remains theorem-level existence evidence only and was explicitly rejected as a materialized endpoint.

### Reproducible artifacts

- Directed certificate script (`refinement_santalo_quantitative_certificate.py`) — SHA-256 `230bd87b239e3754aa11dac571c0991885c133fe05a354b6b20d13fe618600e0`.
- Certificate constants (`refinement_santalo_quantitative_constants.json`) — SHA-256 `7dda2e87c6ad95e38183740c6176c8a2d1e6ff0a8687b227845fef4d99d0ffd6`.
- Reproduction notes (`refinement_santalo_README.md`) — SHA-256 `08d919859a1511399525816ae03e8e500ac678b5c114cf9c79a4e27776c2f46b`.
- Bundle (`refinement_santalo_quantitative_handoff.zip`) — SHA-256 `cef727cc04f6077bb9b7952ae7d215fa2ded6952d5de1619dcbf11fbdb1c8181`.

The default checker scans a fixed `512×1024` partition. It uses `mpmath.iv` for trigonometric ranges, exact-rational degree-12 binomial series with an explicit geometric tail for the three fractional powers, and outward `nextafter` arithmetic for the remaining interval operations. A clean run reproduces the JSON ledger and deliberately reports `materialized_object_exists_in_this_artifact=false`.

---

## 1. Exact centred source and the correct polar problem

Use the corrected high-conditioning seed

```text
r(θ,φ)^4 = 1 + 4β sinθ cos(φ-P(θ)),
β = 1/160,
P(θ)=η(θ)-(1/3)sin(3η(θ)),
η(θ)=(3π/2)(cosθ-cos^3θ/3).
```

This is the journal’s exact Fourier seed. It was previously identified as having `P'(π/2)=0` and minimum Gaussian curvature near `0.515`.

The centring is symbolic, not numerical. Since

\[
d\eta=-\frac{3\pi}{2}\sin^3\theta\,d\theta,
\qquad
P=\eta-\frac13\sin(3\eta),
\]

the transverse volume moment is proportional to one full-period integral of

\[
e^{i\eta}e^{-i\sin(3\eta)/3}.
\]

The second factor has only Fourier frequencies `3j`; multiplication by `e^{iη}` leaves no zero-frequency term. The axial moment vanishes after the `φ` integration. Thus the smooth body `K` is exactly centred.

Let `Q₀=K°`. Its support function and contact map are

\[
h_0(u)=\frac1{r(u)},
\qquad
q(u)=h_0(u)u+\nabla_S h_0(u).
\]

The exact centroid identity becomes the Santaló equation at zero:

\[
\int_{S^2}u\,h_0(u)^{-4}\,d\omega
=
\int_{S^2}u\,r(u)^4\,d\omega=0.
\]

For a finite `Q`, the own-centred output is `(Q-s(Q))°`; one must audit `Q` relative to its Santaló point, not treat centring as an ordinary Euclidean translation of `Q°`.

Lángi’s Theorem 2 proves qualitatively that a centred smooth nondegenerate body has centred polyhedral approximants with the same stable/unstable counts. The proof explicitly separates four moment-controlling regions, critical-point truncations, and a compact finite cover of the remaining boundary, but its “sufficiently small/close” choices do not provide the finite constants or actual collar lattice needed here.

---

## 2. Directed smooth ledger

Write `ψ=φ-P(θ)`. The exact fourth-power shell is

\[
\frac{39}{40}\le r^4\le\frac{41}{40}.
\]

The directed shell used below is

```text
0.9936905367902893 ≤ r ≤ 1.0061922463256379,
0.9938458616151641 ≤ h0=1/r ≤ 1.006349525306029.
```

The interval scan certifies:

| Quantity | Directed enclosure |
|---|---:|
| principal curvature of `K` | `[0.507468650485451, 1.4653968222614255]` |
| eigenvalues of `∇²_Sh₀+h₀I` | `[0.5075592157825982, 1.4653427616533286]` |
| `sup |∇_Sr|` | `≤0.053996859411044554` |
| `sup |∇_Sh₀|` | `≤0.054033652711927116` |
| noncritical `inf |∇_Sh₀|` | `≥6.846773169824779e-5` |
| signed critical Hessian of `h₀` | `≥0.0050275859578619315` |
| signed critical Hessian of `r` | `≥0.0050900431184167415` |
| `|P'|` on the critical boxes | `≤0.07073175598333716` |

The theorem ledger rounds inward/outward to

```text
r_curv = 0.507,
R_curv = 1.466,
G_h = 0.0548,
g0 = 5.8e-5,
λcrit = 0.0049.
```

The exact critical radial-Hessian magnitudes are

```text
β(41/40)^(-3/4) = 0.006135318575156318,
β(39/40)^(-3/4) = 0.006369811133271091.
```

### Critical-box geometric correction

The interval Hessian boxes are

```text
|θ-π/2|≤ρ,
|ψ|≤ρ at +x,
dist(ψ,{−π,π})≤ρ at −x,
ρ=π/256.
```

They are **not** spherical balls of radius `ρ`. With

\[
|\eta|\le0.057832616304767506,
\qquad
|P|\le\frac32|\eta|^3\le0.00029014145110278403,
\]

the full physical spherical radius of either rectangular box is at most

```text
0.017561145356057663.
```

The signed Hessian bound `λcrit=0.0049` gives the local Morse conditioning and certifies that the two boxes contain only the intended smooth critical points. It does not, by itself, control a polyhedral feature whose full normal cone crosses a box boundary. This correction matters below: the small target truncation cap reaches only `0.015516915870714923`. The remaining normal-width gap

```text
0.002044229485342709
```

is assigned explicitly to the unresolved collar. No false `ρ = geodesic radius` or Hessian-to-mixed-cone inference is used.

---

## 3. Deterministic finite background net

For level `L`, subdivide each of the six cube faces into `2^L×2^L` dyadic squares and radially project every grid vertex to `S²`. If a cube-face cell has Euclidean diagonal

\[
D_L=2\sqrt2\,2^{-L},
\]

normalization is `1`-Lipschitz in chord distance because every cube-face point has norm at least `1`, and the spherical cell diameter is bounded by

\[
\delta_L=2\arcsin(D_L/2).
\]

At level `20`,

```text
δ20 = 2.697398304698039e-6,
number of face cells = 6·4^20 = 6,597,069,766,656.
```

For each direction `u`, start from the exact polar contact `q(u)`, round each coordinate to the nearest multiple of `2^-64`, and multiply by `1-2^-54`. The final denominator divides `2^118`. Since `Q₀` contains `h_min B³`, convexity gives an exact inward certificate.

```text
Euclidean rounding error           ≤ 4.6947331210536274e-20,
guaranteed interior slack          ≥ 5.512258059346853e-17,
support-error addition             ≤ 5.599333191626019e-17,
rounded background point norm      ∈ [0.993845861615164,1.007840467079822],
rounding direction-angle addition  ≤ 5.63400564200788e-17.
```

### Rolling-ball active-star theorem

The inequalities

\[
r_{\rm curv}I\le\nabla_S^2h_0+h_0I\le R_{\rm curv}I
\]

mean that `Q₀` has an interior rolling ball of radius `r_curv` and an exterior supporting ball of radius `R_curv`. If a rounded source point associated with `u` is active in a face with outward normal `n`, then, including rounding on the active point and on the nearest net point,

\[
r_{\rm curv}(1-\cos d(u,n))
\le
R_{\rm curv}(1-\cos\delta_L)+2\varepsilon_{\rm round}.
\]

Thus at level `20`,

```text
active source-to-face-normal radius ≤ 4.586830009706858e-6,
active source-normal diameter       ≤ 9.17366001941373e-6,
complete-star budget 4δ             = 1.078959321879217e-5.
```

For the complete rounded background hull before target deletions, every actual maximal face therefore has all of its source normals in one `4δ` star. The same conclusion remains valid in the modified hull for every feature whose relevant nearest-net points were not deleted; features meeting a deletion boundary are classified as collar/cross-seam features and are not covered by this sentence. At a nonsimple certified-background vertex, every generator of the full normal cone is an incident face normal containing the same source vertex, so it has the same bound. At a certified-background true edge, both incident face normals contain both edge endpoints, so the same bound covers the whole two-face cone. This is an active-set theorem, not a triangulation-diagonal or selected-facet proxy.

---

## 4. Common separator for every mixed background feature

For an exact smooth contact,

\[
q(u)=h_0u+\nabla_Sh_0,
\qquad
|q-h_0u|=|\nabla_Sh_0|.
\]

Outside the two critical coordinate boxes,

```text
projection-foot separation dfoot ≥ g0 = 5.8e-5,
radial/normal angle α0 ≥ 5.754879063356851e-5 radians.
```

The normal direction moves at unit speed. The radial direction `q/|q|` moves at speed at most

\[
\frac{R_{\rm curv}}{|q|_{\min}},
\]

so the combined Lipschitz constant is

```text
L* = 1 + Rcurv/|q|min = 2.475077833113386.
```

A complete level-20 `4δ` star plus exactification consumes at most

```text
4L*δ + rounding angle = 2.670508300419934e-5,
```

leaving the directed angular gap

```text
αres ≥ 3.084370762936911e-5.
```

### Why this covers faces, vertices, and edges jointly

Choose an anchor source `u₀` in an actual feature. All feature-point rays lie in one spherical cap around `q(u₀)/|q(u₀)|`; every generator of the feature’s full normal cone lies in a disjoint cap around `u₀`. If the angular gap between the two caps is `d>0`, a unit vector `w` separates them with directional margin at least `sin(d/2)`. Therefore

\[
w\cdot x>0
\quad\text{for every point }x\text{ of the feature},
\qquad
w\cdot n<0
\quad\text{for every nonzero }n\text{ in its normal cone}.
\]

An equilibrium would require `x-c=λn` with `λ>0`, which is impossible while the separator survives. Retaining an eightfold reserve and using `sin(d/2)≥sin(d)/2` gives the common centre-motion radius

\[
m_{\rm bg}
=
\frac{|q|_{\min}\sin\alpha_{\rm res}}{16}
\ge
1.915868198716011\times10^{-6}.
\]

This single separator excludes equilibria on every actual certified-background maximal face, every simple or nonsimple vertex/full normal cone, and every true edge. It directly addresses the mixed-feature failure that invalidated the earlier per-facet approximation claim.

The statement is deliberately restricted to features whose active source normals lie wholly in a certified noncritical background star. Every feature meeting a target cap or the annular/corner gap belongs to the explicit collar obligation below.

---

## 5. Exact dyadic target primitives

Let

```text
D = 2^118 = 332306998946228968225951765070086144,
τ = 2^-14 = 20282409603651670423947251286016 / D.
```

The exact rounded axial support coordinates are

```text
h+ = 330261935688464622741803522472384852 / D,
h− = 334416990645408040140947785717004757 / D.
```

Their inward errors from the algebraic smooth contacts are respectively below

```text
5.5188473913540776e-17,
5.583845153163748e-17.
```

### Stable square at `+x`

Delete every other rounded source point with `x≥x_s`, where

```text
x_s = 330241653278860971071379575221098836 / D = h+−τ.
```

Insert the four exact vertices

\[
(x_s,\pm a,\pm a),
\qquad
a=2^{-9}
=
\frac{649037107316853453566312041152512}{D}.
\]

The square’s circumradius is at most

```text
0.002762135864009955,
```

while the guaranteed rolling-ball cross-section radius at depth `τ` is at least

```text
0.007866760651449955.
```

Hence every square vertex lies strictly inside `Q₀`. Since all other retained points lie behind the plane, this is one maximal stable face. Its projected foot is the square centre and its exact in-face perturbation margin is

```text
mstable = a = 0.001953125.
```

### Unstable apex at `−x`

Use the exact apex

```text
v− = (−334416990645408040140947785717004757/D,0,0).
```

Delete every other point whose `−x` axial coordinate exceeds

```text
334396708235804388470523838465718741 / D = h−−τ.
```

Every actual neighbor `w` then satisfies an axial gap of at least `τ`. Since all points remain in `Q₀` and edge lengths are at most `2|q|max`, every extreme tangent ray obeys

\[
-\,v_-\cdot\frac{w-v_-}{|w-v_-|}
\ge
3.0472432158403256\times10^{-5}.
\]

Thus the entire tangent cone, equivalently the full normal cone, certifies one strict unstable vertex; no selected-facet approximation is used.

### Target support-error budget

Including rounding, a point deleted by either axial rule has source normal within

```text
0.015516915870714923
```

of the corresponding critical axis. Adding one level-20 net cell gives cap radius

```text
0.015519613269019635
```

and one-cap area at most

```text
0.000756663779906703.
```

The global support deficits contributed by the target primitives are bounded by

```text
stable cap   ≤ 2.3758081694793463e-4,
unstable cap ≤ 1.7654566069793518e-4,
critical L1  ≤ 3.1335450593497304e-7.
```

The intended stable face and unstable apex are therefore no longer the bottleneck. This does **not** certify the square’s four vertices, its four boundary edges, any side face incident to them, or the nonvertex features incident to the unstable apex; those complete stars are collar/cross-seam features and remain in the audit obligation. The target cap is intentionally smaller than the full rectangular Hessian box; the remaining `0.002044229485342709` normal-width corner/annular sectors are likewise part of the finite collar that still has to be built and audited.

---

## 6. Literal all-feature mechanics for an eventual verifier

For a fixed finite convex polyhedron `Q`, first merge coplanar triangles into maximal faces and retain only true edges. Let `c` be the reference point.

### Maximal face score

For a maximal face `F` in `n_F·x=h_F`, `|n_F|=1`, let

\[
z_F(c)=c+(h_F-n_F\cdot c)n_F.
\]

For each boundary edge `e⊂∂F`, let `b_{F,e}` be the inward unit conormal in the face plane and choose `x_e∈e`. Define

\[
\sigma_F(c)=
\min_{e\subset\partial F}b_{F,e}\cdot(z_F(c)-x_e).
\]

`F` is strict stable iff `σ_F>0`. Every primitive is `1`-Lipschitz in `c`.

### Vertex/full tangent-cone score

For every actual neighbor `w` of vertex `v`, define

\[
\sigma_v(c)=
\min_{w\sim v}
-\,(v-c)\cdot\frac{w-v}{|w-v|}.
\]

The vertex is strict unstable iff `σ_v>0`. This checks every extreme ray of the full tangent cone and is `1`-Lipschitz in `c`.

### True-edge four-component score

For `e=[v_0,v_1]`, put `t=(v_1-v_0)/|v_1-v_0|` and

\[
p_0(c)=(c-v_0)\cdot t,
\qquad
p_1(c)=(v_1-c)\cdot t.
\]

Let `n_0,n_1` be the two incident maximal-face normals. In `t⊥`, choose inward unit conormals `b_0,b_1` describing `pos{n_0,n_1}`, and set

\[
r_e(c)=(I-tt^T)(v_0-c),
\]

\[
\sigma_e(c)=
\min\{p_0(c),p_1(c),b_0\cdot r_e(c),b_1\cdot r_e(c)\}.
\]

The edge is a strict saddle iff all four components are positive; every component is `1`-Lipschitz.

The background common-separator theorem proves the correct negative sign for all three feature types jointly. The exact target primitives prove the one intended stable and one intended unstable sign. A finished collar must be accepted only after the actual hull is rebuilt and these literal scores are evaluated for every collar or cross-seam feature.

---

## 7. Directed normalized Santaló enclosure

For any finite `Q`, define

\[
P(a)=(Q-a)^\circ,
\qquad
\rho_a(u)=\frac1{h_Q(u)-a\cdot u}.
\]

Then

\[
V(a)=\frac13\int_{S^2}\rho_a^3\,d\omega,
\qquad
M(a)=\frac14\int_{S^2}u\rho_a^4\,d\omega,
\]

and the Santaló point is the unique zero of

\[
F(a)=4M(a)=
\int_{S^2}\frac{u}{(h_Q(u)-a\cdot u)^4}\,d\omega.
\]

Its Jacobian is positive definite:

\[
DF(a)=4\int_{S^2}
\frac{uu^T}{(h_Q(u)-a\cdot u)^5}\,d\omega.
\]

The scale-invariant residual is `||M||/V`, exactly as required by the journal’s correction of the false small-volume polar roots.

Let `e=h_Q-h₀`, `E₁=∫|e|dω`. If denominators on `|a|≤A` lie in `[r,R]`, exact centring of `Q₀` gives

\[
\|F(0)\|\le\frac{4E_1}{r^5},
\qquad
\lambda_{\min}(DF(a))
\ge\frac{16\pi}{3R^5}.
\]

Hence

\[
|s(Q)|
\le
\frac{3}{4\pi}
\left(\frac{R}{r}\right)^5E_1.
\]

For the exact target primitives plus the level-20 background, under the collar support-budget hypothesis stated below,

```text
E1,critical                    ≤ 3.1335450593497304e-7,
E1,background+rounding         ≤ 6.70206381393878e-11,
E1,total                       ≤ 3.1342152657311286e-7,
hQ(u)−a·u on |a|≤10^-3        ∈ [0.9926082807982153,1.0073495253060292],
||F(0)||                       ≤ 1.2945320330719007e-6,
||M(0)||                       ≤ 3.236330082679756e-7,
V(0)                           ≥ 4.110002358338481,
||M(0)||/V(0)                  ≤ 7.874277921310212e-8,
λ(DF)                          ∈ [16.152794579457645,17.388380330974222].
```

On the boundary `|a|=10^-3`, the directed outward margin is

```text
λmin·10^-3−||F(0)|| ≥ 0.016151500047424546.
```

Degree gives a zero in the trial ball; strict positivity of `DF` gives global uniqueness. Strong monotonicity then yields

\[
s(Q)\in B\!\left(0,8.014291438573815\times10^{-8}\right).
\]

Comparison with the conditional complete-feature chamber gives

```text
8.014291438573815e-8 < 1.915868198716011e-6,
mechanical radius / Santaló bound = 23.90564672373519.
```

The normalized Santaló equation is therefore no longer the dominant inequality.

### Conditional finite theorem, stated without hiding the missing object

Let `Q20` be the level-20 rounded background with the exact dyadic square and apex above. Suppose a finite dyadic collar is inserted such that:

1. every collar vertex lies in `Q₀`, all noncollar deletion rules are exactly those stated above, and the final support function satisfies the displayed global `E₁` and pointwise lower-support bounds;
2. the actual final hull is rebuilt, coplanar triangles are grouped, and every true edge is identified;
3. every actual collar/cross-seam maximal face, vertex/full normal cone, and true edge has the required target or exclusion sign with absolute score greater than `1.915868198716011e-6` at reference point zero;
4. the complete collar and target stars stay in one fixed incidence cell throughout the stated coordinate and Santaló boxes.

Then the unique Santaló point lies strictly inside the same all-feature chamber, `Q20` relative to `s(Q20)` has exactly one stable, one unstable, and no saddle, and polarity gives an own-centred strict `(1,1,0)` polyhedron `(Q20-s(Q20))°`.

The antecedent is finite and directly checkable, but it has not been instantiated. This is a rigorous finite-level theorem boundary, not a claimed object.

---

## 8. Uniform finite-level comparison

| Level | Face cells | Cell diameter | Active-source diameter | Residual separator angle | Conditional chamber | Santaló bound | Ratio |
|---:|---:|---:|---:|---:|---:|---:|---:|
| `18` | `412,316,860,416` | `1.0789593218841223e-5` | `3.669427891027153e-5` | `−4.927154138354566e-5` | fails | `8.055495973152922e-8` | — |
| `19` | `1,649,267,441,664` | `5.394796609400985e-6` | `1.8347175571871548e-5` | `4.138624625177583e-6` | `2.5707218478122536e-7` | `8.024596281131588e-8` | `3.2035528738770935` |
| `20` | `6,597,069,766,656` | `2.697398304698039e-6` | `9.17366001941373e-6` | `3.084370762936911e-5` | `1.915868198716011e-6` | `8.014291438573813e-8` | `23.9056467237352` |

Consequently:

- level `18` is rigorously too coarse for this uniform common-separator proof;
- level `19` is the first of the tested uniform levels whose Santaló bound fits the conditional chamber;
- level `20` is the first tested level with the chosen factor-ten reserve.

This does **not** satisfy the run’s materialization gate. Level `20` has trillions of cells, and the collar lattice is absent. There is no expanded H/V list, actual incidence reconstruction, interval root for an actual generated hull, perturbation box, OBJ, or STL.

---

## 9. Quantitative obstruction for the existing axial architecture

The journal’s strongest materialized axial level has

```text
nr = 320,
m = 96,
κ = 0.01895,
rows = 30,724,
raw stable margin = 1.5674376561e-4,
raw centroid norm ≈ 1.42128033e-2,
Santaló displacement ≈ 1.42111007e-2,
Santaló-centred class = (11035,10333,21366).
```

 The endpoint archive itself was not attached, so no row-by-row reconstruction is claimed. The supplied arithmetic is independently reproduced:

```text
|s|/κ                         = 0.7499261583113456,
margin/κ                      = 0.008271438818469656,
|s|/margin                    = 90.66453549010153,
|s|−margin                    = 0.01405435693439,
required suppression, ×4     = 362.6581419604061.
```

### First-order Santaló response theorem

For any differentiable refinement family

\[
h_\kappa=h_0+\kappa f+O(\kappa^2),
\]

put

\[
J_0=4\int_{S^2}uu^T h_0^{-5}\,d\omega,
\qquad
b_f=\int_{S^2}u f h_0^{-5}\,d\omega.
\]

Implicit differentiation of `Fκ(s(κ))=0` gives

\[
s(\kappa)=4J_0^{-1}b_f\,\kappa+O(\kappa^2).
\]

Therefore:

- `b_f≠0` forces a first-order Santaló displacement;
- if an isotropic all-feature certificate has radius `o(κ)`, the ordinary ball-comparison proof can never close at sufficiently small `κ`; this alone does **not** prove that the actual directed correction crosses a wall;
- a genuine asymptotic wall-crossing obstruction follows when some signed wall score has expansion `σ(κ,a)=m(κ)-ℓ·a+o(κ+|a|)`, with `m(κ)=o(κ)` and `ℓ·(4J₀^{-1}b_f)>0`;
- if a certified chamber contains a Euclidean ball of radius `Bκ+o(κ)`, `|4J₀^{-1}b_f|<B` is a sufficient, not necessary, survival criterion.

The ten saved levels have `||s||/κ` near `0.75002`, while the fitted weakest isotropic margin decays much faster. This is finite scaling evidence, not an asymptotic identification of `f` or a direction-independent impossibility theorem, but it closes every materialized level and the present one-dimensional cumulative axial profile.

The fixed `4,324`-row cover shows the same mismatch: its weakest reported construction-centre witness is `1.43388e-4`, while its exact Santaló point is near `(-0.03000124168057223,…)`; centring preserves the lattice but creates thousands of equilibria. The shift/witness ratio is

```text
209.23118866691934.
```

The exact distributed correction hits its first circuit wall at amplitude `0.002051991092060539` with `93.6887%` of the original `x` moment still present, so only `6.3113%` of the needed correction fits in the old chamber: a capacity deficit of about `15.845×`.

This identifies the dominating bound in the failed architecture: a global weighted degree-one support error, not insufficient mesh density.

---

## 10. Smallest geometry change capable of reversing the scaling

The smooth seed does not need replacement. The smallest nonrepeating change is local and finite:

1. **Keep the exact dyadic target square and apex.** Their margins already exceed the level-20 common chamber by factors above `10^3` and `15`, respectively.
2. **Fill precisely the missing critical annulus/corners.** The collar must bridge from target-cap normal radius `0.015516915870714923` to the full interval-box radius `0.017561145356057663`, a normal-width of at least `0.002044229485342709`, and then meet the certified background stars.
3. **Use gradient-following monotone strips with one common separator per complete actual star.** A per-facet or per-link sign is not enough. Every maximal face, full vertex cone, and true edge created by the collar must satisfy the literal scores in Section 6.
4. **Cancel the weighted degree-one response locally.** For separated local offset blocks, enforce to first order

   \[
   \sum_j A_j u_j e_j h_0(u_j)^{-5}=0,
   \]

   or reserve four positive control rays whose weighted moment cone contains the required correction in its interior. This converts the axial `Θ(κ)` global mode into a localized higher-order error.
5. **Use three support coefficients as dependent Santaló controls inside each actual incidence cell.** Solve `G=M/V=0` by interval Newton or Krawczyk only after rebuilding the actual hull.
6. **Enumerate circuit walls in their true order.** The journal’s exact collar atlas found a primitive four-row wall long before the nominal controls, after thousands of expected facets had already disappeared. A formal root in an inherited incidence model is not evidence.

A finite local-control acceptance inequality is

\[
\sigma_{\min}(J)r-L_{\rm ctrl}r^2>\|G(0)\|,
\]

where `J` is the normalized moment Jacobian on the chosen collar-control block and `r` is the distance to the first actual circuit or mechanical wall. The old distributed cover violates this by the measured `15.845×` capacity deficit. The redesigned collar must satisfy it locally while retaining all-feature margin `>1.915868198716011e-6` and the support-error budget used in the Santaló enclosure.

---

## 11. Most useful continuation and acceptance sequence

Start from the exact target numerators above, not from another cumulative axial profile.

1. Materialize a finite dyadic collar around each target primitive, including the four annular/corner sectors identified quantitatively here.
2. Rebuild the actual local hull after every ring/strip addition; merge coplanar faces and enumerate all true edges.
3. Evaluate every `σ_F`, `σ_v`, and four-component `σ_e`; require all collar/cross-seam signs to clear `1.915868198716011e-6` at level `20`, or `2.5707218478122536e-7` at level `19`.
4. Verify that every collar vertex lies in `Q₀` and that the final pointwise and `L¹` support deficits remain below the Santaló ledger.
5. Introduce three dependent local support controls and isolate the normalized `M/V=0` root inside one literal incidence/sign cell.
6. Only after the literal own-centred class is `(1,1,0)`, emit the expanded H/V data, grouped face cycles, true-edge list, perturbation radius, independent verifier, and OBJ/STL.

An adaptive background can reduce the astronomical uniform count by taking local diameter proportional to the certified projection-foot separator. It must, however, prove the same rolling-ball active-star diameter across neighboring adaptive cells; a nominal mesh size alone is insufficient.

## Final status

- **Accepted finite object:** none.
- **Exact finite data produced:** the dyadic target square and apex, deletion thresholds, common denominator `2^118`, and all target margins.
- **Independent calculations produced:** exact centring derivation; directed curvature, polar-radius, gradient, critical-Hessian and critical-box geometry; complete-active-star theorem; mixed-feature common separator; dyadic rounding; global support-error budget; normalized Santaló root enclosure; levels `18/19/20`; and axial suppression arithmetic.
- **Rigorous finite-level obstruction:** level `18` is too coarse for the uniform separator; all ten materialized axial levels fail; the strongest needs `90.66453549×` degree-one suppression, or `362.65814196×` with the stated reserve.
- **Rigorous conditional finite theorem:** level `19` closes by factor `3.20355287`; level `20` closes by `23.90564672`, provided the finite collar satisfies the four explicit hypotheses.
- **Exact unresolved obstruction:** no finite collar/cross-seam incidence complex has been generated whose actual maximal faces, nonsimple full normal cones, and true edges all clear `1.915868198716011e-6` while preserving the support/Santaló budget. That finite combinatorial bridge—not the Santaló equation—is now the dominant bound.
