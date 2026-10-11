# material-c5a7ddce398f

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# SECTION_STRESS_HELLY3_E17_V1 — Recovery capsule part 2 of 2

## Identity, exact dependencies, and evidence status

This is the complete analytic companion to immutable material `[internal-source-reference]`, named Recovery capsule part 1-2 SECTION_STRESS_HELLY3_E17_V1 section_stress.py.txt. Its literal ASCII text is the entire runnable `section_stress.py`, 10447 bytes, SHA256 e7d76e7640274c9195a90c4f2bd849c08eadf7ba9bea04d9a50fa502a5e5cf97. The two parts together are the full recovery capsule. No other source, input file, random seed, numerical optimizer, downloaded library, or originating sandbox is required. The code and exact inputs are not duplicated here.

The general central-half lemma was developed in ACTUAL_SECTION_PAIR_SHEAR_CONES_V1, immutable result `minimum-0102`, SHA256 690f7751a44b598c31c7d3259b8d3f44ec1902b7f0251874edaba663bbb90e2d, read completely by the coordinator. The present proof includes that lemma independently, then extends the pair identity to the exact minimax, proves the support bound of three, and exhibits a true own-volume-centroid E17 control where every two-support certificate fails but a three-support certificate succeeds. The explicit source-only part had previously been stored without its promised companion proof. This part closes that recovery boundary. Both build and check were actually executed from the exact source hash under CPython3.13.5, standard library only, with assertions enabled. This is a new accepted method and a non-record exclusion control, NOT an110 construction or a proof excluding allE17.

## 1. Actual central sections force two strict unstable vertices

Let P be a full-dimensional convex3-polytope with an interior origin. Let M be symmetric positive definite and write |x|_M^2=x^TMx. Let L be any plane through the origin, K=P∩L, and R^2=max_{r∈K}|r|_M^2. The maximum may be evaluated on all true vertices of K. Assume each of the two open halfspaces bounded by L contains an actual vertex of P of squared M-norm at least R^2.

Then P has at least two strict unstable equilibria relative to this origin and M. To prove it, consider either closed half P_+. A convex quadratic attains its maximum on a vertex of P_+. Every new vertex produced by clipping lies in K and has norm at most R. Our hypothesis ensures that a maximizing actual vertex b can be chosen strictly outside L: if the half maximum exceeds R^2 it cannot be a new cut vertex; if it equals R^2, the supplied outside actual vertex itself maximizes it. For any actual incident edge direction d≠0 from b, a sufficiently short positive segment b+td remains in P_+. Therefore

2t b^TMd+t^2 d^TMd <= 0.

Since d^TMd>0, this implies b^TMd<0. All true incident directions have strictly negative radial derivative. Their positive cone is the full tangent cone, so b is a strict unstable equilibrium of the full P. The two halfspaces give two distinct such vertices. The conclusion includes equality in the initial radius comparisons; no weak-contact ambiguity is concealed by rounding.

For a physical uniform polytope take the origin to be its actual volume centroid. Any affine realization with metric M keeps that centroid at the affine image of the origin, since affine maps have constant Jacobian. No free origin or polar centroid is introduced.

## 2. Shear-height coordinates and a finite positive stress

Choose coordinates L={z=0}. Write each actual vertex X_i=(u_i,z_i), u_i∈R^2, and let I be the nonempty collection of vertices in one open halfspace. Thus every z_i in I is nonzero and has the same sign. Every positive definite3×3 matrix has the unique Schur form

M(G,v,y) = [[G,Gv],[v^TG,v^TGv+y]],

with G positive definite2×2, v∈R^2, y>0. Hence

|X_i|_M^2 = |u_i+z_i v|_G^2+z_i^2 y.

The actual section radius R_G^2=max_{r∈K}r^TGr depends only on G, not on v or y.

Choose nonnegative weights λ_i with sum1 on I, and define

S_λ=Σ_i λ_i z_i^2>0,
b_λ=Σ_i λ_i z_i u_i,
v_λ=−b_λ/S_λ,
T_λ=Σ_i λ_i u_i u_i^T−b_λ b_λ^T/S_λ.

The exact completion of squares is

Σ_i λ_i |X_i|_M^2 = tr(GT_λ)+S_λ(|v−v_λ|_G^2+y).     (1)

This follows by expanding the left side into Σλu^TGu+2v^TGb+S v^TGv+S y and completing its quadratic square. In particular T_λ is positive semidefinite: for any vector a, a^TT_λa is the minimum over scalar t of Σλ(a·u_i+z_i t)^2.

If tr(GT_λ)>=R_G^2, equation(1) gives Σλ|X_i|_M^2>R_G^2 for EVERY v and y>0. Some actual vertex on that side therefore has squared norm strictly greater than R_G^2. One such stress on each side, combined with Section1, proves U_strict>=2 at all shears and all positive heights. These λ are mathematical convex-duality multipliers, not independently assigned physical masses and not replacements for uniform volume integration.

For any fixed stress, the sufficient conditions are the closed linear inequalities

tr(G(T_λ−r_k r_k^T))>=0

for every actual section vertex r_k. Thus one can certify a whole cone of planar G without bounding the condition number of the full3D metric. The choice of the same actual geometry and same G on both sides is essential.

## 3. Exact minimax and the support bound of three

Define the zero-height shear minimax on one side by

L_I(G)=min_{v∈R^2} max_{i∈I}|u_i+z_i v|_G^2.

It satisfies the exact identity

L_I(G)=max_{λ_i>=0,Σλ_i=1} tr(GT_λ),               (2)

and the maximum has a realizing λ with at most THREE nonzero components.

Here is a complete proof, including existence and support size. Put f_i(v)=|u_i+z_i v|_G^2 and F(v)=max_i f_i(v). Because all z_i≠0, every Hessian is2 z_i^2 G. Let m>0 be the smallest of z_i^2 times the least eigenvalue of G. Then each f_i(v)−m|v|^2 is convex; so is their maximum. F is strongly convex and tends to infinity with |v|, and thus has a unique minimizer v_*.

Let A={i:f_i(v_*)=F(v_*)} be the nonempty active set. The origin lies in the convex hull of the active gradients ∇f_i(v_*). Otherwise, let h be the point of that finite convex hull nearest to0. It is nonzero and h·g>=|h|^2 for each active gradient g. Along direction−h all active f_i have strictly negative derivative at v_*. Every inactive f_i has a strictly positive value gap below F(v_*); finiteness and continuity ensure these cannot reach the old maximum during a sufficiently short step. The common negative active derivatives then strictly decrease F, contradicting minimality.

Consequently weights λ on the active set exist with sum1 and Σλ_i∇f_i(v_*)=0. They can be chosen on at most three indices. Indeed, if more than three positive weights remain, the corresponding vectors(1,∇f_i(v_*)) inR^3 are linearly dependent. There is a nonzero coefficient vector c with Σc_i=0 and Σc_i∇f_i=0; c has both signs. Replacing λ by λ−t c for the largest t>=0 maintaining nonnegativity preserves the two equalities and removes at least one positive weight. Repeating yields at most three.

For this λ, the positive definite quadratic Σλ_i f_i has derivative0 at v_* and therefore its unique minimum there. All positively weighted f_i are active, so that minimum is F(v_*)=L_I(G). Completing the square gives that minimum as tr(GT_λ). Conversely, for any other simplex weights μ, max_i f_i(v)>=Σμ_i f_i(v), whence L_I(G)>=min_vΣμ_i f_i(v)=tr(GT_μ). This proves(2), attainment, and the three-support bound without an unproved minimax-interchange assumption.

A useful extension is valid at any fixed y_0>=0:

min_v max_i [|u_i+z_i v|_G^2+z_i^2 y_0]
 = max_λ [tr(GT_λ)+S_λ y_0],                     (3)

again with a maximizing stress supported on at most three actual vertices. The same argument applies because the added terms are constants in v and do not change the gradients or strong convexity.

## 4. Exact scope of this obstruction, not of U=1 itself

For fixed actual P,L,G, the condition that each half has an outside vertex of squared norm at least R_G^2 at every v and y>0 is equivalent to

L_{I+}(G)>=R_G^2 and L_{I−}(G)>=R_G^2.            (4)

Sufficiency follows from Sections2–3, with a three-support stress for each half. To see necessity, suppose one side has L_I(G)<R_G^2. At its minimizing v_*, all f_i(v_*)<=L_I(G)<R_G^2. Choose

0<y<min_{i∈I}(R_G^2−f_i(v_*))/z_i^2.

The finite minimum is positive. Then every actual vertex on that side has norm strictly below R_G, so the premise of the two-half obstruction fails. This is a precise limitation of the chosen central-section radius method. It does NOT show that U=1 is possible at that metric: the other side may contain several unstable vertices, other planes may exclude it, or the dual stable geometry may exclude110. Conversely equality L_I=R_G^2 is enough because S_λ y is strictly positive for actual3D metrics y>0.

If a candidate110 survives this method for one plane, at least one side must have L_I(G)<R_G^2. It must also satisfy all individual strict ellipsoidal inequalities at its common v,y. Conditions from several planes and from primal and dual geometry must use one common3D metric and the actual polar, not separate optimizing metrics.

## 5. A genuine E17 body requiring a three-vertex stress

The exact ten raw vertices are encoded literally in part1. The eight base points at z=0 are

(1,0), (3/5,4/5), (−3/5,4/5), (−4/5,3/5),
(−4/5,−3/5), (−5/13,−12/13), (5/13,−12/13), (35/37,−12/37).

All lie on the unit circle and are actual vertices of their convex octagon. The two upper points are(−41/40,0,1),(41/40,0,1). The exact hull code enumerates all supporting planes from triples, merges coplanar facets, constructs strict convex facet cycles, validates all incidences and both oriented uses of each actual edge, checks rank3 at every vertex and Euler's identity. It obtains V10/E17/F9, facet sizes8,4,4,3,3,3,3,3,3 and vertex degrees3 eight times,5 twice. Thus this is precisely a genuine two-apex E17 realization, not the unrelated9/19/12 trace control.

Two actual positive tetrahedral fans, independently anchored at the two apices, give the same volume and centroid:

Vol=689614/468975,
g=(7313081/510314360, −37207819/1326817336, 241427/689614).

The script subtracts this g from every vertex, recomputes actual supports q_f·X=1, checks strict nonincidences, and intersects all actual crossing edges with z=0. There are eight true crossing edges. Their section polygon agrees exactly with the Minkowski description

K=(1−g_z)B+g_z[−41/40,41/40]e_x−g_{xy}.

No arbitrary barycentric origin, surface centroid, or centroid of the polar is used.

At G=I_2 the lower stress uses actual base vertices(0,2,5) with weights(1/3,5/14,13/42). These are strictly positive and have weighted raw planar center0. Its energy tr(T)=1. All base vertices have the same centered height−g_z, so the translation by g_{xy} cancels in T. For ANY pair of base vertices and ANY simplex weights λ,1−λ, its stress energy is λ(1−λ)|B_i−B_j|^2, at most one quarter of their squared distance. The script enumerates all28pairs and obtains

max_pairs |B_i−B_j|^2/4 =64/65.

The true section radius is

R_I^2=4708764616531538513/4757957413811180800,

and exact rational comparison proves64/65<R_I^2<1. Thus every stress with at most two lower-side vertices fails the uniform all-shear/all-height certificate, while the displayed three-vertex stress succeeds. This is a genuine strict improvement over all pair tests, not merely failure of a selected pair or of equal weights. In fact the lower minimax is exactly1: the stress proves a lower bound1 and the shear centering the raw base circle gives an upper bound1.

The upper stress uses the two apices with weights1/2,1/2; its energy is(41/40)^2=1681/1600>1. Both sides therefore pass the true central-section obstruction at G=I_2 for every v∈R^2,y>0.

The same TWO FIXED stresses prove more. For the entire closed planar metric box

G=[[1,b],[b,s]], |b|<=1/200, 99/100<=s<=101/100,

all G are positive definite. For each fixed section vertex r, energy(stress,G)−r^TGr is affine in(b,s); its minimum on the rectangle occurs at a corner. Part1 tests all four corners, both stresses, and the actual maximum over all section vertices exactly. The minimum margin is

7974100576564053397/1760444243110136896000 >0.

Therefore the whole box, ALL shears v, and ALL positive heights y have U_strict>=2. The full3D condition number is unbounded in this theorem. No position assumption on a possible unique U or stable base facet is used.

## 6. Complete physical mechanics of three rational affine controls

For G=I_2 the code realizes the metric by the actual rational affine map

(u,z) -> (u+v z, sqrt(y) z).

It uses(v,y)=(0,1/100),(0,1),((4,−3),1/4), so all square roots are rational. It explicitly transforms the actual poles contragrediently, checks M N=I, independently rebuilds each true hull and volume centroid, and checks that the new centroid is exactly0.

It evaluates strict stable, unstable and saddle counts and all four edge primitives on every true primal/dual edge pair. A physical weak edge packet is tested only when all four primitives are nonpositive and at least one is zero; the true projected contact is reconstructed, checked against all supports, classified asVE,EF orVF, and duplicate feature descriptions are merged by exact coordinates. Zeros outside physical packets are retained as harmless zeros, not falsely counted as extra equilibria. The exact results in(S,U,H) order are

(2,9,9), (6,10,14), (2,2,2),

with zero physical weak contacts for all three. Euler S+U−H=2 is asserted. These controls illustrate the family exclusion, not a110 attainer. The exact output contains all coordinates, facets, edges, supports, mass data, stress coefficients, section cuts and every primitive.

## 7. Reconstruction, verification, and observed terminal markers

Save the literal text of part1 as section_stress.py in an empty directory. Required input pin:

section_stress.py 10447 bytes SHA256 e7d76e7640274c9195a90c4f2bd849c08eadf7ba9bea04d9a50fa502a5e5cf97.

Environment actually used: CPython3.13.5, standard library fractions,itertools,math,pathlib,json,hashlib,sys. No installed packages are needed; use -S. Assertions MUST stay enabled: never run -O. There are no optional parameters or randomness. All Fractions, source ordering, JSON separators and trailing newline are fixed in the source.

Reconstruction command:

python -S section_stress.py build

Verification command, rerunning the exact hull, both mass fans, section, all guards and mechanics from source and comparing output bytes:

python -S section_stress.py check

Both commands were actually run successfully. They emit the following terminal lines:

ACTUAL_E17_HULL_TRUE_COM_TWO_FANS_PASS
ALL_28_BASE_PAIRS_FAIL_BUT_HELLY3_STRESS_PASSES
WHOLE_GBOX_ALL_SHEARS_ALL_HEIGHTS_U2_PASS
COUNTS [(2, 9, 9), (6, 10, 14), (2, 2, 2)]
WEAK_COUNTS [0, 0, 0]
VOLUME 689614/468975 CENTROID (Fraction(7313081, 510314360), Fraction(-37207819, 1326817336), Fraction(241427, 689614))
WEIGHTS (Fraction(1, 3), Fraction(5, 14), Fraction(13, 42)) R2 4708764616531538513/4757957413811180800
MIN_GBOX_MARGIN 7974100576564053397/1760444243110136896000
section_stress.json 18556 cf5ad162fe96541c2826f5c3088fdc3f9dc544fbf35e90a9a5e17c0075b2e988
SECTION_STRESS_HELLY3_E17_RECOVERY_PASS

The reproduced output pin is section_stress.json,18556bytes,SHA256 cf5ad162fe96541c2826f5c3088fdc3f9dc544fbf35e90a9a5e17c0075b2e988. This hash identifies bytes; the complete generator and literal inputs in part1, not the hash alone, preserve the object. The analytical all-parameter result follows Sections1–5, not from the three sample metrics or the finite identity smoke tests.

## 8. Consequences and the next mathematical gap

This proves an exact support-three reduction for the strongest all-shear,all-height radius certificate attached to one actual central plane. The support-three bound is necessary in general, as witnessed within the very first open10/17/9 layer. It supplies closed linear planar metric cones and fixed-height minimax constraints that can be combined with actual ridge/rim dual exclusions, shape parameters, or additional planes while keeping one shared metric.

It does not exclude every metric for the displayed body, every two-apex shape, the whole E17 layer, or all weak110 objects. It supplies no attaining110 construction. The accepted global bracket remains34<=C_min<=622, and all global FULL/LOCAL and incidence catalogs are unchanged. The useful frontier is joint shape dependence and multiple-plane/primal-dual compatibility, not another arbitrary cap on full3D condition number.
