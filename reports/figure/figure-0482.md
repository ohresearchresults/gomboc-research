# figure-0482

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Steady Quartz 74 — C486 full-SPD handoff

## Status

I read the supplied `research-journal.md` completely through EOF, including the full shared memory, branch memory, and literal immutable parent payload `figure-0475` (SHA-256 `efd788f7d4157e152a2b25e672629ee6cb2723c80893d348a43ae4fd334d0f69`). The authoritative checkpoint is `NW37_C486_PACKET56_12_Q15_27_AFF2_G5`, V162/E243/F83,C486, all vertices trivalent, strict S=[20,52], U=[0,161], H=[[22,106],[100,156]], weak000/primitivezero000, with physical packet 56/12 and same-centre polar packet 16/28. The already-proved identity-entry box and complete positive-diagonal SPD obstruction are preserved and were not repeated.

No strict110 endpoint is promoted in this handoff. I obtained two exact structural results for the *full* SPD problem that substantially sharpen how the remaining search should be conducted: (1) the complete fixed-incidence affine feasibility problem is coordinate/congruence invariant, so AFF2's packet contraction is a local sign-cell advantage rather than a smaller global affine orbit; and (2) strict S1/U1 metrics are uniformly separated from the singular PSD boundary. The second result converts the observed high-condition/near-PSD phenomenon from a sampling curiosity into an exact obstruction: a solution cannot hide arbitrarily close to rank loss.

There is also an exact semidefinite/Farkas certificate framework that can decide the physical U1 part of the full off-diagonal problem once the literal AFF2 report is restored.

## Exact source limitation encountered

The bounded input pack contains the parent payload and its generators, hashes and audit summaries, but it does **not** contain the literal 26,975,062-byte `NW37_C486_PACKET56_12_Q15_27_AFF2_G5_EXACT.json` report or the prerequisite literal `NW37_MONO85_PACKET3CUT_T999_AFFINE_M1E5.json`. Parent source unit 2 explicitly requires the former report, while source unit 1 requires the latter. The recovery commands likewise assume the earlier source-complete chain. Therefore the 162 exact centred physical points, all 243 true edges, the fixed polar point set, and hence the 486 full six-entry directed Gram forms cannot be regenerated from this bounded pack alone. I did not invent those coordinates or treat their hashes as bytes.

Continuation-critical receipts from the authoritative parent are:

- AFF2 input `NW37_C486_PACKET56_12_Q15_27_AFF2_G5.json`: 10,450 bytes, SHA-256 `fe4b1204f21d970981d6da718e45c4f4f44cd4c16874f695960229c683613a8f`.
- Exact report `NW37_C486_PACKET56_12_Q15_27_AFF2_G5_EXACT.json`: 26,975,062 bytes, SHA-256 `2cbd0724d7f265e5ef273a0c6e94dd375df88ea97a67e612fb94a262ac14169c`.
- Its affine input parent `NW37_MONO85_PACKET3CUT_T999_AFFINE_M1E5.json`: SHA-256 `d79f7ae7bbca7fdb575c4fca57f271dce1d75c43bafe0b40afc9a842c0929d59`.
- Generated diagonal-form file, reconstructible only after the exact report is restored: 7,230,880 bytes, SHA-256 `df94b7b1edd0c6a4f0df4af98895e7c00738f74dfc0345ab2962b29908746f61`.

This is a source-delivery limitation, not negative evidence about the full SPD orbit.

## Exact result 1 — AFF2 does not change the global fixed-incidence affine feasibility problem

Let the centred raw polyhedron be P, and let an invertible affine linear coordinate change B produce P'=BP. A further affine metric on P' is represented by an SPD Gram matrix H. Pull it back to

`G = B^T H B`.

Congruence by an invertible B is a bijection SPD→SPD. For every centred vertex p and raw edge direction d,

`(Bp)^T H (Bd) = p^T G d`.

Thus every physical vertex-equilibrium sign is preserved under this correspondence. The same statement holds on the stable side: a stable face of P under G is the corresponding unstable vertex of the fixed same-centre polar under `G^{-1}`; after the B-coordinate change this is merely the congruent inverse-metric problem. Mixed-edge equilibrium is likewise an affine-image statement and is preserved under the same one-to-one correspondence.

**Consequence.** Existence or nonexistence of a strict110/weak000 metric anywhere in the complete SPD orbit is invariant under the AFF2 reparameterization. AFF2's 56/12 physical and 16/28 polar packet contraction is therefore extremely useful for organizing a *local* sign-cell continuation near its identity metric, but it does not by itself reduce the global set of affine images. The positive-diagonal theorem remains substantive because “diagonal in the AFF2 frame” is a proper frame-dependent subcone of SPD.

A related practical consequence is that a large condition number measured in the AFF2 coordinate frame is not intrinsically geometric: an arbitrary nonsingular change of raw coordinates can make the same affine image appear better or worse conditioned. Only approach to the projective PSD boundary is coordinate-invariant in the relevant sense.

## Exact result 2 — strict S1/U1 is bounded away from the PSD boundary

This is a general fixed-incidence theorem and directly addresses the high-condition survivors requested in the assignment.

### Rank-one two-U lemma

Let K be any convex 3-polyhedron with 0 in its strict interior. For a symmetric metric H define the directed edge score

`D_H(v,w) = v^T H (w-v)`.

Let the limiting nonzero PSD metric be rank one,

`H0 = u u^T`.

Let F+ be the exposed face where `u·x` is maximal, with value `a>0`, and F- the exposed face where it is minimal, with value `b<0`.

For a vertex v in F+ and an incident neighbour w outside F+,

`D_H0(v,w) = a (u·w-a) < 0`.

For v in F-, w outside F-,

`D_H0(v,w) = b (u·w-b) < 0`.

Because there are finitely many leaving edges, these signs remain strictly negative for every SPD H sufficiently close to H0.

Now, for each such nearby SPD H choose a vertex `v+` of F+ maximizing the H-squared radius `x^T Hx` among vertices of F+. For every neighbour w of v+ that also lies in F+,

`2 D_H(v+,w) = ||w||_H^2 - ||v+||_H^2 - ||w-v+||_H^2 < 0`.

The inequality is strict even if the first two radii tie, because H is SPD and `w != v+`. Combining the in-face and leaving-edge inequalities proves v+ is a strict unstable vertex. The same construction on F- produces a distinct strict unstable vertex v-. Hence:

> **Every SPD metric sufficiently close to any nonzero rank-one PSD metric has at least two strict U roots.**

No genericity, unique exposed vertex, or sampling assumption is used.

### Rank-two boundary gives at least two stable roots

Fix the centred physical polyhedron P and its same-centre polar Q. If trace-normalized SPD metrics `G_n` converge to a rank-two PSD matrix G*, then

`adj(G_n) -> adj(G*)`,

and `adj(G*)` is nonzero rank one. Stable equilibria of P under G are exactly unstable vertices of Q under `G^{-1}`; positive rescaling does not affect signs, so one may use `adj(G)` instead of `G^{-1}`. Applying the rank-one lemma to Q and `adj(G_n)` therefore gives:

> **Every SPD metric sufficiently close to a rank-two PSD boundary metric has at least two strict stable faces.**

### Compactness corollary

Normalize Gram matrices by `tr(G)=1`. The closure is the compact PSD trace-one spectrahedron. Every boundary point has rank one or rank two. Rank-one boundary points have a neighbourhood with U>=2; rank-two boundary points have a neighbourhood with S>=2. Compactness of the boundary supplies a finite subcover.

Therefore there exists an `epsilon(P)>0` such that every trace-one SPD metric with

`lambda_min(G) < epsilon(P)`

fails strict(S,U)=(1,1). Equivalently:

> **Any strict S1/U1 Gram cell for a fixed polyhedron is uniformly separated from the PSD boundary, and hence has a finite condition-number bound after trace normalization.**

This theorem is stronger than a finite high-condition search. In particular, a sequence of numerical candidates that seems to improve only by driving G toward singularity cannot converge to a strict110 fixed-incidence solution. The supplied pack does not contain enough literal C486 geometry to compute an explicit rational numerical epsilon for this particular checkpoint, so I do not claim one.

This also gives the requested exact interpretation of near-PSD behaviour: it is an obstruction regime, not an unexplored asymptotic refuge for strict110.

## Exact result 3 — PSD/Farkas certificates for the complete physical-U1 problem

Once the exact AFF2 report is restored, the physical U side can be attacked independently and exactly before paying for the quadratic polar and mixed-H algebra.

For centred physical vertex `p_i` and directed true edge `i->j`, put `d_ij=p_j-p_i` and

`A_ij = sym(p_i d_ij^T)`.

Then

`D_ij(G) = p_i^T G d_ij = <A_ij,G>`

is linear in the six independent symmetric entries. In the exact entry convention used by the parent, the coefficient vector is

`[p0*d0, p1*d1, p2*d2, p0*d1+p1*d0, p0*d2+p2*d0, p1*d2+p2*d1]`.

For a proposed unique strict U root r in a weak-U-free cell:

1. every outgoing edge of r must satisfy `D_rj<0`;
2. every other vertex i must possess at least one outgoing edge `D_ij>0`.

Choosing one positive outgoing edge at every nonroot is not merely heuristic. The identity

`2 D_ij(G) = ||p_j||_G^2 - ||p_i||_G^2 - ||p_j-p_i||_G^2`

shows that `D_ij>0` strictly increases squared G-radius. Hence chosen positive arrows cannot contain a directed cycle; on the connected finite polytope graph they form an r-rooted escape arborescence. Thus weak-free U1 is equivalent to the existence of at least one such root-labelled strict linear system together with `G≻0`.

### Exact blocker certificate

For one candidate system define its desired-positive matrices C_k by

- `C_k=-A_rj` for each root exit required negative;
- `C_k=A_ij` for every chosen positive nonroot escape.

If exact nonnegative rational multipliers `y_k`, not all zero, satisfy

`B = sum_k y_k C_k <= 0`

in the negative-semidefinite Loewner order, then no SPD G can realize the candidate, because

`sum_k y_k <C_k,G> = <B,G> <= 0`,

while every term on the left is strictly positive.

This is an exact semidefinite Gordan/Farkas certificate. For a rational 3x3 B, negative semidefiniteness is checkable with integer/rational arithmetic by verifying positive semidefiniteness of `-B` (all principal minors nonnegative, or exact LDL).

A particularly useful automatic blocker is any directed cycle. With unit multipliers,

`2 sum_cycle D_ij(G) = - sum_cycle ||p_j-p_i||_G^2 < 0`,

so the coefficient-matrix sum is negative semidefinite. This recovers the radius-order obstruction algebraically and allows blocker learning without imposing a preselected root tree.

### Durable full-U1 exclusion format

A complete fixed-incidence physical-U1 exclusion can therefore consist only of:

- the exact 486 directed six-entry forms (243 undirected edges, both directions);
- a finite list of blocker certificates, each storing the selected directed forms plus exact nonnegative rational multipliers;
- a deterministic combinatorial verifier proving that for every possible root and every choice of one positive outgoing edge at each nonroot, at least one blocker is contained in the choice.

No floating LP result is needed in the final proof. Conversely, if a candidate system survives and has a strict SPD numerical solution, openness gives a nearby rational SPD matrix with the same strict signs; that rational matrix can be promoted to an exact U1 checkpoint.

This suggests a SAT/cutting-plane implementation: choose a root, Boolean-select one outgoing arrow for each nonroot, reject directed cycles immediately, solve the remaining strict SDP cone numerically only to nominate an exact rational blocker or rational interior point, add the blocker as a clause, and repeat. Exact verification is only rational matrix arithmetic plus finite clause coverage.

## Stable and mixed-H continuation after a physical U1 cell

Do not enumerate the much more expensive polar/mixed signs before knowing that a physical U1 cone exists. If an exact rational physical U1 Gram matrix G is found, retain its open linear U1 cell and add the same-centre polar conditions. With fixed polar vertices `q_f`, a stable face f is a polar U root under inverse metric, so its directed score has the homogeneous quadratic form

`q_f^T adj(G) (q_g-q_f)`.

Because `det(G)>0`, adjugate scaling introduces no sign ambiguity. Search the physical-U1 open cone for exactly one polar U root, explicitly allowing stable-root exchange across these quadratic walls. Only then run the complete mixed-edge H audit and weak-boundary checks. A promoted endpoint must retain the parent's standard: exact maximal incidence, actual filled centroid, full strict/additional-weak S/U/H census and complete P/Q landscapes.

The new PSD-boundary theorem also applies to this second stage: a genuine S1/U1 chamber cannot be forced arbitrarily close to singular G, so branch-and-certificate subdivision may impose a sufficiently interior SPD slice once a body-specific exact epsilon is derived.

## What I tried and what is not claimed

I first audited the supplied exact parent and its dependency chain, then attempted to reduce the requested full off-diagonal task to the literal six-entry physical forms. The bounded pack stops one level before the exact report bytes needed to instantiate those forms. Rather than reconstruct unseen coordinates from hashes or broaden the already-proved diagonal result, I worked on the complete projective SPD geometry itself.

I did **not** repeat the positive-diagonal theorem, the `||G-I||_entry,infinity<1/3` exclusion, or numerical high-condition sampling. I did **not** infer a global C486 exclusion from the missing source. No new endpoint, no new incidence, and no C<500 strict110 body is claimed.

The new boundary theorem is exact and global over the full fixed-incidence SPD orbit, but it does not by itself exclude interior off-diagonal U1/S1 cells.

## Decision and most useful continuation

**Fixed C486 remains worth exactly one decisive full-SPD physical-U1 certificate pass, but not another unconstrained metric-sampling campaign.** Metrics themselves cost no edges, so the E243 incidence is still attractive despite only six edge units of final headroom. The rank-one/rank-two boundary theorem removes the main rationale for chasing progressively more ill-conditioned samples: strict110 cannot live arbitrarily near the PSD boundary.

The continuation order should be:

1. Restore the literal `NW37_C486_PACKET56_12_Q15_27_AFF2_G5_EXACT.json` report with SHA `2cbd0724d7f265e5ef273a0c6e94dd375df88ea97a67e612fb94a262ac14169c`, or equivalently restore the exact input plus the source-complete auditor chain that regenerates it.
2. Deterministically emit all 486 directed physical six-entry Gram forms and verify the six present-root forms against the parent's identity-box certificate.
3. Run the blocker/SAT exact physical-U1 atlas with **all 162 possible roots**, permitting root exchange and using cycle/PSD blockers rather than preserving roots 0 or161.
4. If every physical-U1 candidate is covered by exact NSD blockers, the entire fixed C486 affine orbit is excluded immediately—no polar or H calculation is needed. At that point deliberately switch geometry to the source-complete low-edge `NW37_MONO47` C270 / `NW37_MONO49` C282 architectures instead of implicitly consuming the remaining six-edge budget.
5. If an open rational physical-U1 Gram cell survives, intersect it with the adjugate polar sign cells to seek S1, then perform the complete mixed-H/weak audit. That is the only branch on which further fixed-C486 work should continue.

The principal durable scientific gain is therefore an exact separation of the problem into an interior, finitely certifiable SPD search and an excluded PSD-boundary regime. High-condition root-exchange behaviour is no longer a reason to leave the fixed-incidence question indefinitely open.
