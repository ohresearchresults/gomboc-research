# figure-0046

AI research report · 2026-08-23 UTC

---

# Decisive audit of SPG-EFFECTIVE

## Verdict

**SPG-EFFECTIVE cannot be accepted as a proved explicit homogeneous polyhedral Gömböc.** The smooth spectral-phase seed survives the audit, and several scalar approximation lemmas can be repaired. The fatal defect is the local-to-global equilibrium step: inequalities checked separately on incident patch facets do not exclude an equilibrium on a mixed edge or vertex of the final intersection. An exact centered rational prism refutes that implication at stronger numerical margins than those claimed.

No rational H-representation with exact own-centroid counts `(S,U,H)=(1,1,0)` was materialized. The strongest exact finite figure recovered has `(V,E,F)=(21,40,21)` and `(S,U,H)=(2,3,3)`.

This is a counterdiagnosis of the supplied construction and certificate, not a contradiction of Lángi's qualitative existence theorem. Lángi proves equilibrium-preserving approximation, but his proof treats mixed local boundaries and then separates the remaining compact boundary from the complete family of radial support planes before taking a finite subcover; that stronger common-support argument is precisely what SPG-EFFECTIVE omitted. :contentReference[oaicite:0]{index=0}

## 1. Smooth seed: retained

For

\[
\rho(u)^4=1+\frac{q(u)}{15},\qquad
q(x,y,z)=x\cos p(z)+y\sin p(z),
\]

\[
p(z)=\eta(z)+\frac1{50}\sin(2\eta(z))+\frac1{100}\cos(4\eta(z)),\qquad
\eta(z)=\frac{3\pi}{2}\left(z-\frac{z^3}{3}\right),
\]

the transcript's exact centroid cancellation, two nondegenerate equilibria, and global strict-convexity certificate remain valid. :contentReference[oaicite:1]{index=1}

The independent exact/symbolic audit rederived:

\[
|p'|\le \frac{891}{175}<5.1,\qquad |p''|<16,\qquad |p'''|<127,
\]

\[
|\nabla q|<\frac{31}{5},\qquad \|\nabla^2q\|<54,
\]

and, for `h=(1+q/15)^(-1/4)`,

\[
\frac{9839}{10000}<h<\frac{509}{500},\qquad
\frac1{66}<|H'|<\frac{1091}{60000},\qquad
0<H''<\frac1{600},\qquad |H'''|<\frac1{3000}.
\]

Consequently the conservative polar principal-radius estimate

\[
\frac1{500}I\preceq \nabla^2h+hI\preceq\frac{21}{10}I
\]

is certified, the critical Hessian gap exceeds `1/(66·29)>2^-11`, and the displayed component bounds give `||∇³h||<32`. One old cap calculation was wrong: `2^30·2^-42` is not below `2^-16`. Replacing it by the proved variation bound `512d` restores the claimed sign on radius-`2^-42` caps. The executable audit contains 38 passing rational or symbolic checks.

## 2. Exact countertheorem to the transition step

Set

\[
s=2^{-52},\qquad x_1=1-\frac{s^2}{2},\qquad y_1=\frac{s}{2}.
\]

Take the centrally symmetric rational octagon

\[
(1,0),(x_1,y_1),(0,1),(-x_1,y_1),(-1,0),
(-x_1,-y_1),(0,-1),(x_1,-y_1)
\]

and extrude it through `-1≤z≤1`. Its uniform-volume centroid is exactly zero. At the vertical edge over `(1,0)`, the two incident side planes are

\[
x+sy=1,\qquad x-sy=1.
\]

They satisfy all of the following exact statements:

1. The incident affine-normal slopes differ by
   \[
   2s=2^{-51}<2^{-48}.
   \]
2. Each facet separately passes the proposed one-normal residual test with
   \[
   \frac{s^2}{1+s^2}>2^{-105}>2^{-106}.
   \]
3. Neither facet is a stable equilibrium: its perpendicular foot lies beyond the short section edge at parameter
   \[
   \frac{2}{1+s^2}>1.
   \]
4. The common edge is nevertheless a strict saddle. Its perpendicular foot is `(1,0,0)`, and
   \[
   (1,0,0)=\frac12(1,s,0)+\frac12(1,-s,0),
   \]
   so the radial vector lies in the strict interior of the full edge normal cone.

The certificate is generated and checked with `fractions.Fraction`, then independently rechecked by a second script using a different centroid calculation. Therefore the inference

> every incident facet is individually excluded, with close normals and a positive residual, hence every mixed edge or vertex is excluded

is false. A valid replacement must test the **convex hull of all active normal rays** for every mixed active set, or provide one common separator valid simultaneously for the entire normal cone.

## 3. Component-by-component audit

| Component | Result | Reason |
|---|---|---|
| Smooth derivative, curvature and Hessian bounds | Pass after one arithmetic repair | Exact rational/symbolic checks reproduce the needed conservative margins. |
| Support-gap lemma | Pass | It follows from the tangent outer rolling ball. |
| Inward rational normal net | Pass for `Q0` alone | Correct constants give `(1-10δ)L⊂Q0⊂L` and support deficit `<11δ`. |
| Stable tangent collar | Local algebra passes | Internal central/side incidences are exact; collar/global mixed active sets are not classified. |
| Thales spiral | Meridional identities pass | Linkwise radial decrease does not determine bridge facets after rotation and intersection. |
| Fixed-origin polar equilibrium duality | Pass | A `k`-face equilibrium is dual to a `(2-k)`-face equilibrium relative to the same origin. |
| Polar and centroid scalar transfer | Pass conditionally | Their premises are valid only after the final support/Hausdorff inclusion is proved. |
| Universal body-scale `64` reference transfer | Not established; false for the dimensionless edge-foot branch | Short edges have sensitivity proportional to the reciprocal edge length. |
| Final active-lattice certificate | Fail | The astronomical object was never enumerated, so no true faces, edges, vertices, or mixed normal cones were audited. |

## 4. Correct quantitative lemmas

### Support-gap lemma

If the principal radii of a smooth strictly convex body `L` are at most `M`, then the tangent ball

\[
B(x(n)-Mn,M)
\]

contains `L`. Thus for every `y∈L`,

\[
|y-x(n)|^2\le 2M\,[h(n)-n\cdot y].
\]

If `y` is an equilibrium relative to a reference point `e`, tangential projection yields

\[
|\nabla h(n)|\le \sqrt{2M\varepsilon}+|e|
\]

whenever the support gap is at most `ε`. This validly excludes global-region equilibria once a uniform support gap and gradient separation are available; it does not by itself classify local patch joins.

### Correct inward-net lemma

Suppose `rB⊂L⊂RB`, `{n_i}` is a chordal `δ`-net, and

\[
h(n_i)-a-\eta\le b_i\le h(n_i)-a,
\qquad Q_0=\bigcap_i\{x:n_i\cdot x\le b_i\}.
\]

Put

\[
B_0=\frac{R-a}{1-\delta^2/2}.
\]

If `a>(R+B0)δ`, then `Q0⊂L`; if additionally `αr≥a+η`, then `(1-α)L⊂Q0`. At

\[
\delta=2^{-300},\quad a=8\delta,\quad r=49/50,\quad R=51/50,\quad \eta<\delta,
\]

one obtains exactly

\[
(1-10\delta)L\subset Q_0\subset L,
\qquad 0\le h_L-h_{Q_0}<11\delta.
\]

The six-chart rational stereographic net with `D=2^304` has fewer than `2^613` listed normals. This proves the global approximation only, not the later gluing taxonomy.

### Conditional polarity and centroid bounds

If `rB⊂K,L` and `||h_K-h_L||∞≤δ<r`, then

\[
\|\rho_{K^\circ}-\rho_{L^\circ}\|_\infty
\le \frac{\delta}{r(r-\delta)}.
\]

At `r=24/25`, `δ=2^-300`, this is `<2^-299`.

If centered `K` satisfies

\[
rB\subset K\subset RB,\qquad K\subset P\subset K+\delta B,
\]

then, with `t=δ/r`,

\[
\|c(P)\|\le (1+t)R\big((1+t)^3-1\big).
\]

At `r=24/25`, `R=26/25`, `δ=2^-300`, exact rational arithmetic gives `||c(P)||<2^-298`. This is stronger than the previous `2^-160` claim, but it is conditional on an inclusion that the unverified mixed patch never established.

## 5. Exact replacement for the centroid-reference argument

A body-radius-only constant cannot control the dimensionless edge-foot parameter. For

\[
P_\varepsilon=[-1,1]^3\cap\{x+y+z\le3-\varepsilon\},\qquad \varepsilon=2^{-100},
\]

one has `B⊂Pε⊂2B`. On the short cut edge

\[
A=(1,1,1-\varepsilon),\qquad B=(1,1-\varepsilon,1),
\]

the foot parameter changes from `1/2` at `c0=0` to `3/4` at

\[
c_1=(0,-\varepsilon/4,\varepsilon/4),
\]

and exact squared arithmetic gives

\[
|\Delta t|^2>64^2\,|c_1-c_0|^2.
\]

The correct finite statement is featurewise. For a materialized rational polytope, every required face, vertex, and edge branch is affine in the reference point:

- face side: gradient `n×e`;
- vertex comparison: gradient `w-v`;
- edge start/end foot branches: gradients `±e`;
- edge support branch against `z`: gradient
  \[
  \left(I-\frac{ee^T}{|e|^2}\right)(z-v).
  \]

Freeze every positive branch of an equilibrium feature and one strict negative exclusion branch for every non-equilibrium feature. For `g(c)=g(c0)+b·(c-c0)`, the exact `L∞` sign radius is

\[
\rho_g=\frac{|g(c_0)|}{\|b\|_1}.
\]

The minimum of these rational radii is a rigorous reference-point stability radius. The supplied checker computes it from the **actual** maximal-face and true-edge lattice.

## 6. Executable theorem checker

The package includes two independent exact components:

1. `exact_polytope_verifier.py` accepts rational vertices or halfspaces, enumerates H-vertices, reconstructs maximal faces and true edges, verifies the closed Euler sphere, computes the exact uniform-volume centroid by oriented tetrahedra, classifies every face/vertex/edge, rejects degeneracies, and can require `(S,U,H)=(1,1,0)`.
2. `exact_reference_stability.py` computes the exact featurewise reference radius described above.

All mathematical decisions use integers and `fractions.Fraction`. The cube smoke test returns `(V,E,F,S,U,H)=(8,12,6,6,8,12)` and exact reference radius `1`.

## 7. Materialized finite results

### Exact proof counterexample

The rational prism has `(V,E,F)=(16,24,10)`, exact centroid zero, and a certified mixed saddle despite both incident facets passing the proposed individual transition tests.

### Strongest circumscribed near-witness

A separate materialized rational polyhedron has

\[
(V,E,F)=(21,40,21),\qquad c(P)=0,
\]

strictly contains the radius-2 ball and therefore contains the spectral-phase seed, but its complete exact own-centroid audit is

\[
\boxed{(S,U,H)=(2,3,3)}.
\]

All equilibrium and exclusion signs are nonzero. The failure is open and exact, not numerical noise: one balancing cap supplies one additional stable face, two additional unstable vertices, and three saddle edges.

## 8. What was actually executed

The rerunnable package executed all of the following:

- 38 rational/symbolic analytic and local-geometry checks;
- construction and exact verification of the mixed-transition prism;
- an independently written exact prism verifier;
- the conditional polarity/centroid arithmetic and exponent correction;
- the short-edge reference-transfer counterexample;
- the generic exact polytope checker and exact reference-radius checker;
- an independent exact verifier for the 21-vertex circumscribed near-witness.

The package-level rerun verdict is:

```json
{"overall":"PASS: fatal counterdiagnosis and all advertised exact checks reproduced; no Gomboc claimed."}
```

What was **not** executed is the claimed `<2^616` SPG-EFFECTIVE object. No expanded H-list, active face lattice, exact centroid, or full mixed-feature witness table exists for it.

## 9. Deliverables

- [Complete decisive audit](sandbox:/mnt/data/spg_decisive/DECISIVE_AUDIT.md)
- [Rerunnable audit and checker package](sandbox:/mnt/data/spg_decisive_package.zip) — SHA-256 `b0287942747fb17c45f89c8e10f41d9d8c71e53dbbc5978a11e149102bde4ea4`
- [Verification summary](sandbox:/mnt/data/spg_decisive/verification_summary.json)
- [Exact mixed-transition prism certificate](sandbox:/mnt/data/spg_decisive/audit/mixed_transition_prism.json)
- [Exact rational polytope verifier](sandbox:/mnt/data/spg_decisive/checker/exact_polytope_verifier.py)
- [Exact featurewise reference-radius checker](sandbox:/mnt/data/spg_decisive/checker/exact_reference_stability.py)
- [Materialized 21-vertex circumscribed near-witness](sandbox:/mnt/data/spg_decisive/near_witness/rational_circumscribed_near_witness.json)

## Publication-grade conclusion

The supplied SPG-EFFECTIVE proof fails at a specific, exactly refuted normal-cone inference. The valid scalar estimates cannot compensate for the missing mixed active-set classification. The next valid construction must either materialize the entire final active lattice and audit every exact normal cone, or prove one common-separator lemma for every possible global/collar/spiral/apex tie, including nonsimplicial ties. Plane-count optimization is premature until that topology problem is closed.
