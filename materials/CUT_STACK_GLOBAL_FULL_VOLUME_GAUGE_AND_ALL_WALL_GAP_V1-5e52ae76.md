# material-5e52ae768f93

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# CUT_STACK_GLOBAL_FULL_VOLUME_GAUGE_AND_ALL_WALL_GAP_V1

## Evidence and scope

Coordinator analytic extension of the actual cut-and-stack geometry. No new numerical search, certificate replay, all-interior exclusion or attaining body is claimed. This result resolves every parameter boundary of the ENTIRE native eight-parameter family by one uniformly full-dimensional affine normalization. It also gives explicit necessary parameter separations for a complete weak rooted system, and hence for U=1. The interior remains open outside previously certified regions. The global proper110 bracket remains 34 <= C_min <= 622.

Exact sources read completely:

- minimum-0285, CUT_STACK_E17_ALLROOT_FULL_B_T_V1, SHA256 383ab22af4a74c7ba8d2604d95d2f259b60928871a59f7b9d332622ab016f35f. This is the literal native family, complete admissible domain, actual moments and previously certified six-cut box for all b,t. Its standalone exact source is sufficient without older parent inputs. Its author's observed normal and cold executions are accepted, not independently replayed here.
- [internal-source-reference], NINE_VERTEX_NONZERO_PSD_REFINEMENT_COLLAR_V1, SHA256 3052074db1f19530ac423145576607e4c86366b7e45a96cf9f17f880f0aee65b. For an actual uniformly filled full-dimensional hull with at most nine true vertices, any finite contained labelled refinement containing every true vertex has no complete weak rooted tree under any nonzero PSD metric.
- [internal-source-reference], HEPTAGON_TRIANGLE_UNIFORM_GAUGE_AND_ALL_WALL_GAP_V1, SHA256 a78ff4287c53f66c405271a3c0f63170a77c72763d2f81dd2a9b33ec724aa6f6. Sections 3-4 give a universal deletion transfer on Q=[-1,1]^2 x [0,1], not just a heptagon statement. Its proof and constants are recalled below.
- [internal-source-reference], TEN_VERTEX_EFFECTIVE_DELETION_GAP_AND_CLOSED_CENTROID_CYCLES_V1, SHA256 c891d9f5064e9d1d2a244f62481ec9814edb08a5f8248117f64c9fa1c30dc890. Its effective Gamma_9,192 > 2^(-2^178) is used only in the final optional explicit corollary. This depends on the accepted nine-vertex theorem and the primary effective minimum theorem of Jeronimo, Perrucci and Tsigaridas, arXiv:1112.0544, Theorem 1. No new proof or execution of that earlier compiler is asserted here.

## 1. The native family and its actual moments

Start with B-=(-1,0,0), B+=(1,0,0), B0=(0,-b,0), B1=(0,1,0), B2=(0,0,1). Let b>0 and independently 0<f_j,k_j,t<1 for j=0,1,2. Define

L_j = B- + f_j(B_j-B-),
R_j = B+ + k_j(B_j-B+),
C = (L_0+L_1+L_2)/3,
S = C+t(B--C).

The vertex order is (B0,B1,B2,L0,L1,L2,R0,R1,R2,S). The convex hull has true 10/17/9 incidence, with outward maximal cycles

(0,3,4,1,7,6), (0,2,5,3), (0,6,8,2),
(1,4,5,2), (1,2,8,7), (3,9,4),
(3,5,9), (4,9,5), (6,7,8).

These native cuts are valid on the whole stated open domain, without further coupling between the six fractions. The two removed corner tetrahedra have disjoint interiors in x<0 and x>0. The stack point is strictly inside the removed left tetrahedron and sees exactly its cut face. This geometric proof is in the literal parent; it is not a claim that this family exhausts all realizations of the graph.

Set beta=b/(1+b) and first scale y by 1/(1+b). In these coordinates retain the same labels, so B0=(0,-beta,0), B1=(0,1-beta,0), B2=(0,0,1), and B-/B+ are unchanged. Put

p=f0 f1 f2, q=k0 k1 k2, a=(1-t)p,
s_f=sum_j f_j(B_j-B-), s_k=sum_j k_j(B_j-B+),
D=2-a-q,
J=2 sum_j B_j-a[4B-+(3-t)s_f/3]-q[4B++s_k].

Then actual uniform volume is D/6 and actual volume centroid is J/(4D). The two original tetrahedra, the two removed tetrahedra and the added stack tetrahedron have signed six-volume coefficients 1,1,-p,-q,tp. Thus these formulas are actual solid moments, not assigned vertex masses.

## 2. A single positive-volume normalization for every parameter and rate

Write

alpha_j=1-f_j, gamma_j=1-k_j,
A=sum_j alpha_j, B=sum_j gamma_j,
epsilon=t+A+B > 0.

Apply additionally x -> x/epsilon. Denote the final vertices by Z and their convex hull by K. In native coordinates the entire invertible affine map has linear part

G=diag(1/epsilon,1/(1+b),1).

Every final vertex lies in Q=[-1,1]^2 x [0,1]. Indeed the B_j have x=0, the L_j have x=-alpha_j/epsilon, the R_j have x=gamma_j/epsilon, and

S_x=-[t+(1-t)A/3]/epsilon.

All these x coordinates have absolute value at most one. The y,z coordinates remain in the original compact pyramid and hence in [-1,1] x [0,1].

The exact uniform six-volume in the final coordinates is D/epsilon. It satisfies

1/4 <= D/epsilon <= 1,
1/24 <= Vol(K) <= 1/6.                                      (1)

For the upper bound use 1-p<=A, 1-q<=B and tp<=t. For the lower bound observe

1-(1-t)p >= max(t,alpha_0,alpha_1,alpha_2) >= (t+A)/4,
1-q >= max(gamma_0,gamma_1,gamma_2) >= B/3.

Adding yields D >= (t+A)/4+B/3 >= epsilon/4. No small-parameter approximation enters this bound.

The physical metric is transported, not reset: if M_native was used originally, then H=G^(-T) M_native G^(-1). Positive definiteness, positive semidefiniteness and the same-inverse coupling are preserved. Actual centroids transform by G because this is affine with constant Jacobian. For a U1-only obstruction no dual metric relaxation is required.

## 3. Complete boundary classification

Consider a sequence of parameters in the native domain, compactified by beta,t,f_j,k_j in [0,1], approaching its boundary. By (1), any convergent subsequence of the normalized labelled vertices has a full-dimensional actual limiting hull.

### 3.1 Limits with epsilon bounded away from zero

The normalized formulas are continuous. Every parameter boundary removes at least one true vertex:

- At beta=0, B0=(0,0,0) lies on the segment L0 R0. At beta=1, B1 lies on L1 R1.
- At f_j=1, L_j=B_j; at k_j=1, R_j=B_j.
- At f_j=0, L_j=B-. The stack point S and the other left cut points lie in the hull of B- and the B_j, so in particular a label is redundant.
- At k_j=0, R_j=B+. The remaining right cut points are redundant on the corresponding B+ B_l segments.
- At t=0, S=C is redundant.
- At t=1, S=B-, and all L_j are redundant on S B_j.

Simultaneous boundaries can only add coincidences or redundancies. The actual limiting hull therefore has at most nine true vertices.

### 3.2 The joint zero-volume corner in the old gauge

The only way epsilon can tend to zero is t->0, all f_j->1 and all k_j->1. Pass to ratios

alpha_j/epsilon -> a_j,
gamma_j/epsilon -> c_j,
t/epsilon -> tau,

with all ratios nonnegative and sum_j(a_j+c_j)+tau=1. The limiting final coordinates are

B_j=(0,(B_j)yz),
L_j=(-a_j,(B_j)yz),
R_j=(c_j,(B_j)yz),
S=(-tau-sum_j a_j/3, ((B0)yz+(B1)yz+(B2)yz)/3).

The beta limit is allowed to be 0 or 1. Every B_j lies in the segment L_j R_j, so the actual hull has at most seven true vertices. Expanding the finite products gives D=epsilon+O(epsilon^2), uniformly for these nonnegative ratios; therefore its limiting volume is exactly 1/6. The old unscaled volume collapse is not a surviving ten-vertex weak packet.

### 3.3 Mechanical consequence

Suppose U1 bodies approached any parameter boundary. Transport each SPD metric into the final coordinates and normalize its trace to one. A subsequence has a nonzero PSD limit. Choose the true weak escape tree supplied by U1, and pass to one fixed labelled tree among finitely many possibilities. Actual volume centroids converge because the limiting hull has positive volume. The nine selected weak inequalities pass to the limit. Sections 3.1-3.2 give an actual at-most-nine-vertex full-dimensional hull, with the remaining labels merely contained refinements. This contradicts the accepted nonzero-PSD refinement theorem.

Thus the parameter projection of all possible U1 bodies has compact closure strictly inside the entire open native eight-parameter domain in (beta,t,f,k). The same conclusion holds directly for complete weak rooted systems with nonzero PSD metrics. This is not a bound on metric conditioning and does not decide the positive interior.

## 4. Universal deletion gap used for quantitative wall separation

For ten-labelled actual hulls in Q with volume at least 1/96, define

Gamma_9,192 = min max_{i->j in T} -(z_i-g)^T H(z_j-z_i),

where the minimization is over ten-label contained refinements of actual hulls with at most nine true vertices and volume at least 1/192, H PSD with trace one, and all rooted trees T. The hull centroid g is the actual uniform volume centroid. Compactness and the accepted theorem give Gamma_9,192>0.

Put xi=min(1/960,Gamma_9,192/12969). Any smaller positive xi may also be used. Every vertex of a ten-vertex hull in Q with volume at least 1/96 admitting a complete weak rooted system must have deletion distance at least xi.

For completeness, delete a vertex at distance delta from the hull K' of the other nine and replace its label by a nearest point q in K'. The whole hull lies in K'+[0,delta w]. The projected area of Q normal to w is 2|w_x|+2|w_y|+4|w_z|<5, so volume loss is at most 5delta. If delta<=1/960, K' has volume at least 1/192. Actual centroid displacement is at most 1440delta, by decomposing the lost first moment and using diameter(Q)=3. Centred labelled rows change by at most 1441delta. For every trace-normalized PSD arrow its change is at most 9*1441delta=12969delta. A weak tree with delta<xi would therefore contradict the defining positive defect on the nine-vertex refinement. This reproduces the cited universal transfer rather than transferring the heptagon's unrelated raw parameter inequalities.

Our normalized K satisfies the stronger volume bound (1), so this deletion conclusion applies uniformly to the entire native family.

## 5. Exact replacement witnesses and every parameter wall

All distances below are in the final normalized coordinates. Each witness lies in the convex hull of labels other than the deleted label.

First combine L_j and R_j with weights gamma_j/(alpha_j+gamma_j) and alpha_j/(alpha_j+gamma_j). The resulting point has x=0 and yz coordinates

[1-2alpha_j gamma_j/(alpha_j+gamma_j)] (B_j)yz.

Consequently the deletion distance of B_j is at most

[2alpha_j gamma_j/(alpha_j+gamma_j)] ||(B_j)yz||
 <= (alpha_j+gamma_j)/2 <= epsilon/2.

Therefore epsilon>=2xi. Since ||(B0)yz||=beta and ||(B1)yz||=1-beta, and 2alpha gamma/(alpha+gamma)<=1 for alpha,gamma in [0,1], the same witnesses give

beta>=xi, 1-beta>=xi.                                    (2)

Every normalized vector G(B_j-B-) or G(B_j-B+) has norm at most 1+1/epsilon. Use the following additional witnesses:

- For t: delete S and replace it by C. The distance is at most t(1+1/epsilon).
- For 1-t: delete any L_j and replace it by (1-f_j)S+f_j B_j. The distance is at most (1-t)(1+1/epsilon).
- For f_j: delete S and replace it by (1-t)C+t L_j. The distance is at most f_j(1+1/epsilon).
- For 1-f_j: delete L_j and replace it by B_j. The distance is at most (1-f_j)(1+1/epsilon).
- For k_j: choose l different from j, delete R_l and replace it by (1-k_l)R_j+k_l B_l. The distance is at most k_j(1+1/epsilon).
- For 1-k_j: delete R_j and replace it by B_j. The distance is at most (1-k_j)(1+1/epsilon).

Every coefficient used is in [0,1]; C uses no S, and the chosen l ensures that the k_j witness does not use its deleted label. In particular these are actual convex witnesses, not merely estimates of formal coordinate collisions.

Writing theta for any of t,1-t,f_j,1-f_j,k_j,1-k_j gives the necessary bounds

theta >= xi epsilon/(1+epsilon)
       >= 2xi^2/(1+2xi) > xi^2.                           (3)

Also

xi/(1-xi) <= b <= (1-xi)/xi.                             (4)

Equations (2)-(4) explicitly separate all sixteen walls of the eight-coordinate compact cube. They allow arbitrary metric orientation, scale and conditioning, and do not assume S1 or absence of extra weak contacts.

## 6. Optional explicit but extremely small numerical-scale constants

The cited effective gap theorem gives Gamma_9,192>b0, where b0=2^(-2^178). Thus xi=b0/2^14 is an allowed concrete choice in Sections 4-5. It follows that beta and 1-beta are at least b0/2^14 and every cut/stack coordinate and its complement is strictly greater than

b0^2/2^28 = 2^(-(2^179+28)).

This is an explicit theoretical compact box, not a practically evaluated geometric margin or a completed interval search. It must not be confused with the much stronger observed 1/10000 stress margin in the literal parent's restricted six-cut box.

## 7. What this advances and what it does not

The earlier all-root certificate covers all b,t only while six independent cut fractions remain in prescribed intervals. The present proof adds no all-interior exclusion. It instead removes the entire native parameter boundary, including the single coupled t->0,f,k->1 corner at which the previous beta-only gauge lost volume. The continuation problem is now confined to a compact positive interior, albeit with a very small explicit general margin.

All actual moment and inverse-metric obligations are retained. No singular limiting metric is treated as an ordinary equilibrium census. The family remains a native eight-parameter realization class, not a complete eleven-affine-modulus incidence atlas. No whole E17 incidence is subtracted, no 110 construction is produced, and neither lower nor upper global bound changes.
