# figure-0131

Historical AI scientific report · saved 2026-08-28 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Calm Atlas 34 — finite endpoint, obstruction, and continuation

## Result

No literal own-centroid strict `(S,U,H)=(1,1,0)` polyhedron was certified in this direction. I therefore do **not** claim a Gömböc winner.

The work nevertheless produced three reusable advances beyond the supplied journal:

1. A finite source-specific actual-hull cell with only one residual stable–saddle pair beyond the target: Q-class `(2,1,1)`, together with the exact local circuit that relays rather than destroys that pair.
2. A fixed-physical-size dedicated critical patch giving a fully rebuilt 706-vertex Q with strict construction-origin class `(3,1,2)`. Its polar has class `(1,3,2)`. All three critical faces, the unique critical vertex, and both true saddle edges were identified with positive margins.
3. A primal/dual spanning-tree separator lemma that converts the desired mechanics into a finite sparse system of local strict inequalities. A tested angular-shortest-path instance on 4,321 actual source-polar samples reduces the unstable count from 3,761 to exactly one while retaining every hull vertex. This isolates the missing part of the construction as the dual-face separator problem rather than another axial refinement problem.

A deterministic reconstruction, full-hull verifier, dyadic coordinate materialization, Santaló solver, and OBJ/STL exporter are included here:

- [Complete reproducibility bundle](sandbox:/mnt/data/calm_atlas34_bundle.zip)
- [Generator and verifier](sandbox:/mnt/data/calm_atlas34_bundle/generate_and_verify.py)
- [Bundle README](sandbox:/mnt/data/calm_atlas34_bundle/README.md)
- [Machine audit](sandbox:/mnt/data/calm_atlas34_bundle/generated/audit.json)

The dyadic Q coordinates in the bundle are literal rational coordinates. The current Santaló solve and normal-cone audit are numerical rather than interval-certified, so the bundle is an exact finite endpoint but not an exact own-centroid winner certificate.

---

## 1. Exact smooth source and centring

The source radial body is

`R(θ,φ)^4 = 1 + 4β sinθ cos(φ-P(θ))`,

with

`β=1/160`,

`P(θ)=η(θ)-(1/3)sin(3η(θ))`,

`η(θ)=(3π/2)(cosθ-cos^3θ/3)`.

Its uniform-volume first moment is

`M = (1/4) ∫_{S²} R(u)^4 u dω`.

The constant term integrates to zero. After integrating over `φ`, the nonconstant horizontal component is proportional to

`∫_0^π sin^3θ exp(iP(θ)) dθ`.

Since

`dη/dθ = -(3π/2)sin^3θ`, `η(0)=π`, and `η(π)=-π`,

this becomes

`(2/(3π)) ∫_{-π}^{π} exp(i[η-(1/3)sin(3η)]) dη`.

Using the Fourier expansion of `exp(-(i/3)sin(3η))`, every Fourier frequency in the integrand is `1+3n`, which is never zero. The integral therefore vanishes exactly. The vertical component already vanishes in the `φ` integral. Thus the smooth source is exactly centred at the origin, independently of numerical quadrature.

For the polar formulation, write Q by its irredundant maximal-face inequalities

`n_f · x ≤ h_f`.

For a point `a` in the interior of Q,

`P(a)=(Q-a)^polar`

has polar vertices

`p_f(a)=n_f/(h_f-n_f·a)`.

Equilibria dualize as

`S_P = U_Q`, `U_P = S_Q`, and `H_P = H_Q`.

Since the target class is symmetric under swapping S and U, the target is also Q-class `(1,1,0)` relative to its Santaló point.

---

## 2. Full-normal-cone audit used throughout

No triangulation diagonal was counted as a true edge. Every candidate was treated as follows:

1. Rebuild `ConvexHull` from all candidate coordinates.
2. Delete inactive candidate rows.
3. Group coplanar hull triangles into maximal polygonal faces.
4. Reconstruct true edges as intersections of two distinct maximal faces.
5. Audit mechanics relative to the declared centre `a`.

For a maximal face `f` with outward unit normal `n_f`, support `h_f`, and oriented boundary edge `q_i q_j`, the foot of `a` on its plane is

`x_f=a+(h_f-n_f·a)n_f`.

The face primitive is

`σ(f,i,j)=cross(q_j-q_i,x_f-q_i)·n_f / ||q_j-q_i||`.

The face is strictly stable for Q precisely when all its boundary primitives are positive.

A vertex `q_i` is strictly unstable for Q precisely when

`(q_i-a)·(q_j-q_i)<0`

for every adjacent vertex `q_j`.

For a true edge `q_i q_j`, let `d=q_j-q_i` and

`t=-((q_i-a)·d)/||d||²`,

`z=q_i-a+td`.

If its incident face normals are `n_1,n_2`, solve

`z=λ_1 n_1+λ_2 n_2`.

It is a strict saddle edge exactly when

`0<t<1`, `λ_1>0`, and `λ_2>0`.

These tests were applied to maximal faces, all hull vertices, and true edges after every reported topology change.

---

## 3. Source-specific near-target cell

### 3.1 Deterministic construction

Set

`L=400`, `m=12`, `g_cut=0.05`, `r_A=1.2`, `r_0=1.15`,

`extra_drop=2.4`, `λ_offset=π/78`.

For

`γ_i=0.05+i(π-0.1)/399`, `t_i=-cosγ_i`,

and

`λ_j=2πj/12+π/78`,

form the Sloan-twisted direction as follows. Put

`v=(t,sqrt(1-t²)cosλ,sqrt(1-t²)sinλ)`,

`θ=acos(v_z)`, `ψ=atan2(v_y,v_x)`, `φ=ψ+P(θ)`,

and

`d(t,λ)=(sinθ cosφ,sinθ sinφ,cosθ)`.

The row radii are defined recursively by

`r_i=r_{i-1} min_j(d_{i-1,j}·d_{i,j}) exp(-2.4/399)`.

Add the apex `(-1.2,0,0)`. The final candidate ring is projected onto its common mean-x plane. Rebuilding the actual hull reduces the 4,801 candidates to 703 active vertices.

### 3.2 Construction-origin mechanics

The actual 703-vertex hull has strict Q-class

`(S_Q,U_Q,H_Q)=(2,1,1)`.

The two stable maximal faces are the C2-related triangles with source-grid metadata

- `[(12,7),(152,9),(169,10)]`, active vertices `[76,665,700]`;
- `[(12,1),(152,3),(169,4)]`, active vertices `[73,663,699]`.

Each has stable margin

`0.0103545704215949`.

The unique unstable vertex is the apex, with normalized vertex margin

`0.5642381592667428`.

The unique saddle is the true edge `[296,298]`, whose endpoints have metadata

`(62,4)` and `(62,10)`.

Its two incident maximal triangles are

- `[(61,10),(62,4),(62,10)]`;
- `[(61,4),(62,10),(62,4)]`.

Its normal-cone data are

`t=1/2`,

`λ_1=λ_2≈0.2421078041620747`.

Thus the polar at the construction origin has class `(1,2,1)`, not the target.

### 3.3 Hard-centering scale separation remains fatal

At the construction origin the polar centroid is approximately

`c_P=(0.253665535,0,0)`.

This displacement is orders of magnitude larger than the local mechanical walls. Rescaling Q does not repair the ratio between the required recentering and the normalized mechanical margins. This is the same mechanism as the axial-refinement failure recorded in the journal, now exhibited in a source-twisted finite actual-hull cell rather than a regular axial mesh.

---

## 4. Exact local obstruction circuit

The intended local saddle kill was to decrease the x-coordinate of active vertex 296. In the fixed incidence lattice, one saddle cone coefficient has derivative of order `6.37×10²`, suggesting a crossing after a displacement of approximately `-3.8×10^-4`.

The relevant four-point circuit is

- vertex 292: metadata `(61,4)`;
- vertex 294: metadata `(61,10)`;
- vertex 296: metadata `(62,4)`;
- vertex 298: metadata `(62,10)`.

With

`Δ=det(q_294-q_292,q_296-q_292,q_298-q_292)`,

one obtains

`Δ=2.994807824858352×10^-6`.

The derivative under `q_296,x -> q_296,x+δ` is

`dΔ/dδ=7.782986195845095×10^-3`.

Consequently the associated coplanarity wall is exactly located along that ray by

`δ* = -(2.994807824858352×10^-6)/(7.782986195845095×10^-3)`,

approximately `-3.85×10^-4`.

Crossing the wall and rebuilding the complete hull does **not** produce `(1,1,0)`. Vertex `(62,4)` becomes inactive and the saddle relays to the true edge joining metadata

`(61,4)` and `(62,10)`,

with new incident faces involving levels 62 and 63. The rebuilt class remains `(2,1,1)`.

This is the literal local circuit obstruction: the apparent fixed-incidence saddle cancellation is a circuit-driven diagonal/vertex relay, not an equilibrium annihilation.

The analogous fixed-incidence attempt on stable face `[(12,1),(152,3),(169,4)]` predicts a face wall near a z-displacement of `6.6×10^-3` at vertex 663. Before a target chamber appears, that vertex acquires an unstable cone and adjacent saddle edges; after full hull rebuilding, the stable and saddle features again relocate. Sweeps through displacements as large as `±0.1` did not expose a `(1,1,0)` chamber.

---

## 5. Fixed-physical-size dedicated critical patch

To provide the missing Q-stable/P-unstable critical patch, add the fixed triangle

`c_j=(0.485,0.005 cos(2πj/3+7π/39),0.005 sin(2πj/3+7π/39))`, `j=0,1,2`.

A complete hull rebuild gives 706 active vertices and strict construction-origin Q-class

`(S_Q,U_Q,H_Q)=(3,1,2)`.

The three stable Q faces are:

1. The dedicated triangular cap `[703,704,705]`, margin `0.0021428126746386575`.
2. The source face `[(12,7),(152,9),(169,10)]`, margin `0.0103545704215949`.
3. Its C2 mate `[(12,1),(152,3),(169,4)]`, with the same margin.

The apex remains the unique unstable Q vertex, with margin approximately `0.564238`.

The two true saddle edges are:

- `[296,703]`: `t=0.9941397033696755`, `λ_1≈0.07569669`, `λ_2≈0.09502249`;
- `[296,705]`: `t=0.9942511176303518`, `λ_1≈0.07517678`, `λ_2≈0.07459865`.

The dedicated cap therefore removes the previous invariant saddle but replaces it with two cap-connector saddles. It adds one stable face and one net saddle, as required by Euler:

`3+1-2=2`.

The construction-origin polar has class

`(S_P,U_P,H_P)=(1,3,2)`.

Its uniform-volume centroid is approximately

`(0.2772519115,-0.0003132997,0.0005481113)`;

hence

`||M||/V = ||c_P|| ≈ 0.2772526`.

The polar volume is approximately `0.208198125`, and the smallest origin polar denominator is approximately `0.08636477`, strictly positive. These values show that the cap mechanics are locally strict but the construction origin is not remotely close to hard Santaló centring.

Regular caps with 3, 4, 5, 6, 8, 10, and 12 vertices, as well as 300 asymmetric triangular caps over a broad physical-size range, produced only relabelled `(2,1,1)` cells or `(3,1,2)` cells. No actual-hull `(1,1,0)` chamber was found. Repeating cap sweeps is therefore not a useful continuation.

The bundle rounds this endpoint to the dyadic lattice `2^-46 Z³`, rebuilds the hull again, and records the post-rounding lattice and audit. The quoted margins above refer to the unrounded deterministic construction; the generated `audit.json` is authoritative for the dyadic materialization.

---

## 6. New finite separator result on the actual smooth source polar

A second construction used actual points of the smooth polar Q rather than the collapsing recursive radial profile.

Take 120 source level rows, 36 azimuthal points per row, `g_cut=0.02`, and the exact source-polar map. Add the maximum point as the root. The actual hull contains all 4,321 samples. At the construction origin it has the expected very large class

`(4094,3761,7853)`,

while its polar centroid is numerically within about `3×10^-8` of the exact source centre.

Let `G` be the true-edge graph of this actual hull. For adjacent vertices define the nonnegative angular edge cost

`w_ij=-log((q_i·q_j)/(||q_i||||q_j||))`.

Let `D_v` be shortest-path distance from the chosen maximum vertex, and let `p(v)` be a shortest-path parent. Define the logarithmic radial separator field

`s_v=-log(||q_v||/||q_root||)-D_v-μ depth(v)`

with `μ=10^-6`, and replace `q_v` by `exp(s_v)q_v`.

For every nonroot vertex the parent inequality is exact:

`q_v(s)·(q_p(s)-q_v(s))>0`

if and only if

`s_p-s_v > log(||q_v||²/(q_v·q_p))`.

The shortest-path definition makes this inequality strict by the `μ depth` term. Therefore every nonroot vertex has an explicit outgoing witness, while the root retains all inward inequalities.

After rebuilding the actual hull:

- all 4,321 vertices remain active;
- the Q-class is `(1144,1,1143)`;
- the polar class is `(1,1144,1143)`;
- the logarithmic support range has width about `0.0604`;
- the polar centroid norm is about `0.0150`.

This is a finite local-separator field with a certified unique unstable Q vertex, hence a unique stable face of the polar. It does not rely on the journal's axial cumulative strip refinement. Its failure is entirely on the dual-face side: 1,143 stable–saddle pairs remain.

---

## 7. Primal/dual separator lemma

The preceding computation suggests the correct finite formulation.

### Lemma

Let K be the irredundant maximal-face complex of a convex polyhedron Q, homeomorphic to a sphere. Choose:

- a root vertex `v∞`, intended to be the unique unstable Q vertex;
- a root maximal face `f0`, intended to be the unique stable Q face;
- a primal spanning tree T rooted at `v∞`.

The edges not in T form a spanning tree of the dual graph. Root that dual tree at `f0`.

Match every nonroot vertex to its parent edge in T, and every nonroot face to its parent edge in the dual tree. Suppose, relative to a centre `a`, that the following strict conditions hold:

1. Every edge derivative at `v∞` is inward, so `v∞` is unstable.
2. For each nonroot vertex v, its matched primal edge toward `p(v)` satisfies `(q_v-a)·(q_p-q_v)>0`.
3. Every boundary primitive of `f0` is positive.
4. For each nonroot face f, the boundary primitive across its matched dual-parent edge is negative.

Then Q has exactly one unstable vertex, exactly one stable maximal face, and no saddle true edge.

### Proof

Condition 2 supplies an explicit violating edge for every nonroot vertex, so no such vertex is unstable. Condition 1 makes the root strictly unstable.

Condition 4 supplies an explicit outside boundary edge for every nonroot face, so none is stable. Condition 3 makes the root face strictly stable.

Every true edge belongs to exactly one of the two trees. If it belongs to T, its matched child-vertex inequality places the orthogonal line foot outside the open edge on the child side, excluding a saddle. If it belongs to the dual tree, write the edge-foot normal decomposition as `z=λ_f n_f+λ_g n_g`. In the normal two-plane, the signed face primitive of the child face across that edge is a positive geometric factor times the opposite coefficient `λ_g`. A negative primitive therefore makes one cone coefficient nonpositive, again excluding a saddle. Hence there are no saddle edges. ∎

This lemma turns the target into a finite, local, auditable system. It also explains why ordinary uniform strips fail: they do not realize a compatible primal/dual perfect matching.

For radial variables `q_v(s)=exp(s_v)q_v`, all primal-tree inequalities are exact linear difference constraints in `s`. Every dual-face separator is an analytic local inequality involving only the vertices of one maximal face. The target can therefore be searched by a sparse incidence-cell program rather than by global refinement.

---

## 8. Hard Santaló equations inside one incidence cell

For fixed maximal-face incidence, orient the dual polygon around each Q vertex and triangulate that polygon only for volume integration. These triangulation diagonals are never mechanical edges.

For each oriented polar triangle `(p_i,p_j,p_k)`, define

`V_ijk=det(p_i,p_j,p_k)/6`,

`M_ijk=V_ijk(p_i+p_j+p_k)/4`.

Then

`V(a,z)=Σ V_ijk`,

`M(a,z)=Σ M_ijk`,

where `z` denotes shape variables, and the three normalized hard-centering equations are

`F(a,z)=M(a,z)/V(a,z)=0`.

The primary residual is `||M||/V`, not raw `||M||`. For comparison between differently scaled bodies, one should additionally divide by a declared body length such as the polar inradius.

Every solve must also certify

`δ_pol=min_f(h_f(z)-n_f(z)·a)>0`.

Inside a fixed strict incidence cell, `F` is analytic. The Santaló point is the unique zero. Thus `a` should be treated as three dependent variables and solved by interval Newton or Krawczyk iteration while the separator variables are changed. Post-hoc translation after mechanics have been optimized is the failed procedure recorded in the journal.

The mechanical margins must be evaluated at `a(z)`, not at the construction origin. If an interval for any hull circuit determinant reaches zero, the solve must stop, rebuild the complete hull, regroup maximal faces, reconstruct true edges, and restart with the new lattice. A graph diagonal flip without this rebuild is invalid.

---

## 9. Balanced local dyadic blocks

The remaining viable construction is now sharply specified.

1. Start from the 4,321-vertex actual source-polar hull, not the collapsing recursive profile.
2. Delete fixed physical neighborhoods of the two smooth critical points and replace them by a dedicated unstable-Q apex patch and a dedicated stable-Q polygonal cap. Their physical angular radii must remain fixed as the noncritical mesh is refined.
3. Choose a primal spanning tree and its complementary dual tree. The tree choice is part of the optimization; it should be changed by local fundamental-cycle exchanges, not by another global axial ordering.
4. Cover the noncritical region by bounded-diameter blocks following the true-edge graph. In each ordinary separator block, choose dyadic log-offset coefficients in the kernel of both the degree-one spherical response and the first projective centroid response. These blocks implement the primal and dual inequalities without accumulating a global Santaló shift.
5. Reserve three spatially separated control blocks whose projective response vectors are linearly independent. Solve their three amplitudes together with the dependent Santaló point so that `M/V=0` while all mechanical margins remain positive.
6. Convert all offsets to one common dyadic denominator, rebuild the actual hull, and certify every determinant, face primitive, vertex primitive, edge projection, cone coefficient, Santaló residual, and polar denominator by outward-rounded intervals.

The key algebraic object for block selection is the local response matrix

`R_B = D_z(M/V)`.

Ordinary blocks should be combined in exact dyadic null combinations of `R_B` and of the degree-one moment map. Three deliberately unbalanced control combinations should span `R³`. This separates mechanical separator work from global centring work and avoids the broad-support-mode failure in the journal.

---

## 10. What should not be repeated

The following directions have now failed for structural rather than merely numerical reasons:

- increasing the axial row count while keeping cumulative one-way offsets;
- scaling a construction-centred candidate after the fact;
- broad Fourier support modes used as centroid correctors;
- uniform regular cap sweeps;
- single-coordinate attempts to kill the residual saddle or one of the paired stable faces;
- graph-only diagonal flips without rebuilding the hull;
- determinant-one SPD metric searches around the axisymmetric prototype.

The immediate next computation should be a sparse primal/dual matching solve with localized block variables on the 4,321-vertex source hull, followed at every accepted step by a full hull rebuild and a dependent normalized Santaló solve. The first rejection criterion is a circuit determinant interval containing zero; the second is loss of rank of the three selected projective response columns.

---

## 11. Certification status

### Certified or directly reproducible

- Exact smooth-source centroid identity.
- Deterministic source-twisted recursive endpoint.
- Actual-hull construction-origin classes and identified critical features quoted above.
- The explicit four-point saddle-relay circuit and its affine wall equation.
- The primal/dual separator lemma.
- A materialized dyadic finite endpoint and deterministic reconstruction script.
- Complete algorithms for maximal-face, vertex, true-edge, polar-volume, Santaló, OBJ, and STL reconstruction.

### Not certified

- No own-centroid `(1,1,0)` winner.
- No interval-isolated Santaló root for the dyadic endpoint.
- No rational or directed-rounding proof of every dyadic hull determinant in a second independent implementation.
- No positive global perturbation radius for a target chamber, because no target chamber was reached.
- No claim that the strongly dropped 706-vertex endpoint is a close Hausdorff approximation of the smooth source; it is source-twisted but mechanically deformed. The 4,321-point smooth-polar construction is the appropriate starting point when closeness is required.

Journal locators for integration are the entries containing `30724`, `nr=320`, `4,324-row`, and `||M||/V`. The new material here begins with the 703-vertex `(2,1,1)` source cell, the four-point relay circuit, the 706-vertex dedicated-cap endpoint, the 4,321-vertex angular shortest-path separator field, and the primal/dual separator lemma.
