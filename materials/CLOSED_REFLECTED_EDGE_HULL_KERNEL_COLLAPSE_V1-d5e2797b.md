# material-d5e2797b9b8b

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# CLOSED_REFLECTED_EDGE_HULL_KERNEL_COLLAPSE_V1

## Scope and relationship to existing work
This is a new analytic strengthening of the local source-subtree lemma in [internal-source-reference] (SHA256 e75611e233be3c63e18cb811e475ecd7d9fc98bb1df811827ca26cd09eacb063). The antecedent geometry and actual-centroid reflection theorem are the fully read immutable minimum-0245 (SHA256 3a4889dd902249e2904ddfa747f00575a10c16646d44cf15224164893c8056be). No antecedent computation was independently replayed here.

The strengthening removes strict containment, treats arbitrary source/target layers, and identifies the exact metric-kernel consequence. No new H5 tree census, all-root domain, actual body, weak-equilibrium density or global complexity improvement is asserted by this note. The accepted interval remains 34 <= C_min <= 622, with attainment a separate problem. The proof is mathematical reasoning, not a proof-assistant formalization or a numerical computation.

## Theorem
Let z_i be points of R^d, let g be one fixed common reference point, and let T be a rooted directed tree whose arrows point toward its root. Let a -> b be one selected edge. Let D be its source component after deleting this edge, so a is in D and every i in D has a directed path to a. Put S = D union {b}.

Suppose for some real t with 0 <= t < 1 the point

    w = 2g - (1-t) z_b - t z_a

belongs to the CLOSED convex hull of {z_i : i in S}. If a positive-semidefinite matrix M obeys all weak arrow inequalities

    (z_i-g)^T M (z_parent(i)-z_i) >= 0

on the paths from D to a and on a -> b, then

    M (z_i-g) = 0   for every i in S.

Consequently, if the centred vectors {z_i-g : i in S} span R^d, no nonzero PSD metric realizes the selected weak tree. With SPD M and distinct edge endpoints a,b, the tree is impossible without any full-span assumption.

## Proof
Map all centred vectors by M^(1/2). Write A, B, X_i for the images of z_a-g, z_b-g, z_i-g. The weak arrows imply

    ||Y_parent||^2 - ||Y_child||^2
       = 2 Y_child . (Y_parent-Y_child)
         + ||Y_parent-Y_child||^2 >= 0.

Thus ||X_i|| <= ||A|| for every i in D, and A.B >= ||A||^2. Moreover, equality of endpoint norms along a directed path forces every mapped edge increment on that path to vanish.

Closed containment supplies coefficients theta_b >= 0, theta_i >= 0, theta_b + sum_D theta_i = 1, such that

    -(1-t)B - t A = theta_b B + sum_D theta_i X_i.

Equivalently,

    0 = (1-t+theta_b) B + t A + sum_D theta_i X_i.        (1)

Suppose first that A is nonzero. Dot (1) with A. The coefficient 1-t+theta_b is positive, A.B >= ||A||^2, and A.X_i >= -||A||^2 by Cauchy-Schwarz and the descendant norm bound. Therefore

    0 >= 2 theta_b ||A||^2.

If theta_b > 0 this is a strict contradiction. If theta_b = 0, equality is required in every inequality. At least one theta_i is positive, and every such i satisfies X_i = -A. Its norm equals ||A||, but it has a directed path to a, so equality of norms forces X_i = A. This contradicts A != 0.

Hence A = 0. All descendant X_i vanish by their norm bounds. Equation (1), with 1-t+theta_b > 0, then forces B = 0. Mapping back gives the stated kernel conclusion. QED.

## Consequences for the literal two-layer H5 body
For the actual volume centroid g=(c,gamma), gamma in (0,1/2), a top-to-basal edge has the old reflection point in the basal plane at t=2gamma. Its source component may include additional top vertices; the theorem is valid whether or not they are used in the convex representation.

The earlier local theorem required relative-interior containment in a basal hull with three noncollinear basal vertices. It is enough to have CLOSED containment and that same three-vertex span, since their centred vectors span R^3 when gamma != 0. This is a proved strengthening of the lemma, not a claim that the earlier 64/86 accepted guards or 22941/26409 tree counts increase. Such a census must actually be recomputed.

For a basal-to-basal edge, the reflected point has height 2gamma; top descendants can now participate. This addresses a mechanism outside the purely basal source-hull test. For any edge, certificate search is the affine feasibility problem

    2g = (1-t)z_b + t z_a + sum_{i in S} theta_i z_i,
    theta_i >= 0, sum theta_i=1, 0 <= t < 1.

The convex hull is mixed-dimensional when appropriate. Do not require a full-dimensional raw hull: the relevant condition for excluding nonzero PSD M is the span of the CENTRED vectors, and the theorem already states the kernel conclusion when that span is deficient.

## Boundary at t=1
The proof for t<1 must not be silently used at t=1. If theta_b>0 at t=1, it still forces the entire S into the kernel. If theta_b=0 at t=1, it forces D into the kernel but does not in general force b into the kernel. A full-span D suffices in the latter case. No t>1 extension is claimed.

## Research frontier
A meaningful continuation is an actual mixed-layer all-tree cut catalog or a genuine common-metric surviving cone, using moving uniform moments rather than a frozen centre. Another is a quantitative tree-path energy certificate that survives small failures of exact convex containment and couples multiple source components. Basal-only or small-component failures of this particular criterion are not physical feasibility results.
