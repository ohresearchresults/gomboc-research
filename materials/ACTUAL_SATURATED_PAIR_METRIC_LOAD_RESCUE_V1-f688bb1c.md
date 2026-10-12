# material-f688bb1cedba

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# ACTUAL_SATURATED_PAIR_METRIC_LOAD_RESCUE_V1

## Status, dependencies and scope

This analytic continuation uses ACTUAL_SATURATED_VE_PAIR_CENTROID_HALFSPACE_REDUCTION_V1, material [internal-source-reference] (SHA256 7a7d98ef8123c94760af538f9a470d8b712336fe4444bfaa4aa68797b9088101), and its fully read immutable parent minimum-0243 (SHA256 f1787b59aa7ef14d2e4fb0a713f71f978f5f0ddea762226b426e54aea8d13b7d). The latter supplies the genuine occupied-triangle chart, actual uniform-centroid derivatives and later T-carrier gluing. These parent claims are working premises, not a fresh computational replay.

The result gives an additional sufficient complete-packet regularization mechanism on the positive-parallel-normal locus left by the four-plane theorem. It uses a physical metric variation exactly neutral on the entire T-carried packet. It does NOT prove that the remaining scalar cancellation is impossible, that its equations have a specified codimension, or that every weak110 body regularizes. There is no new computed body, radius, census, C34 exclusion or attaining construction. Bounds remain34<=C_min<=622. The new linear and matrix arguments below need no executable code.

## 1. Actual pair data and affine centroid halfspaces

Use the actual homogeneous V10/E17/F9 setting of the parent: true disjoint heptagonal F and triangular T contain all ten vertices; two interior-spoke EF pairs use FOUR DISTINCT triangular source/target planes. Nonparallel end facets are allowed. The off-T weak packet consists precisely of these EF points and their specified basal VE partners. The entire T-carried packet is allowed: VE along T edges and EF/VF borne by T in the parent's sense. This does not silently include arbitrary other top-located cross contacts or unrelated off-packet obligations.

Let z_i in R4 be the fixed-apex plane velocities for pair i. In COMMON physical centroid coordinates write

L_i z_i=-c_i W_i z_i, c_i>0, rank W_i=3, ker W_i=span{k_i}.

L_i is the true derivative of the uniformly filled centroid, not an assigned load. Let Q_i and P_i be the physical EF and VE derivative rows, positive for the desired exits. Assume in this theorem that q_i=Q_i k_i and p_i=P_i k_i satisfy q_i p_i<0 for both pairs. Define the physical covector m_i uniquely by

W_i^T m_i=(|p_i|Q_i+|q_i|P_i)^T, and put n_i=-m_i.

An adapted m_i must first be transformed by the inverse transpose of its physical vertex-basis matrix. Independently chosen adapted metrics are not one common physical problem.

For a symmetric physical metric velocity H, let Q_{H,i},P_{H,i} be the contact derivatives at FIXED shape in M+tau H. Set

ell_i(H)=|p_i|Q_{H,i}+|q_i|P_{H,i}.

For a first-order metric amplitude h, the actual-centroid image of pair velocities satisfying

Q_i z_i+h Q_{H,i}>0, P_i z_i+h P_{H,i}>0

is exactly the affine strict halfspace

n_i.g_i+c_i h ell_i(H)>0, where g_i=L_i z_i.

Proof: along z_i+t k_i the lower and upper strict bounds overlap exactly when m_i.W_i z_i+h ell_i(H)>0. Substitute g_i=-c_i W_i z_i and multiply by c_i>0. The true c_i factors cannot be dropped independently from the metric-load balance.

## 2. Additional compatibility scalar on the failed fixed-metric locus

Non-positive-parallel normals already admit fixed-metric escape. Suppose instead

n_2=alpha n_1, alpha>0.

For actual first-order centroid balance g_1+g_2=0, write g_1=v,g_2=-v and s=n_1.v. The two inequalities are equivalent to

-c_1 h ell_1(H)<s<(c_2/alpha)h ell_2(H).

Therefore strict simultaneous opening with this ONE metric direction exists exactly when

h Lambda(H)>0, where Lambda(H)=alpha c_1 ell_1(H)+c_2 ell_2(H).

Because h may have either sign and SPD is open, some opening exists iff Lambda(H)!=0. If Lambda(H)=0, this four-plane/one-metric tangent family has no strict first-order solution. This is not an all-orders obstruction or a statement about other facets/metric directions.

For an allowed vector space of symmetric metric velocities, the same proof says that rescue occurs exactly when Lambda does not vanish identically on that space. No generic nonvanishing or dimension count is assumed.

## 3. A metric pencil exactly neutral on the T-carried packet

Let t be the normalized pole of true facet T, with t.x=1 on T. Consider

M_tau=M+tau t t^T.

For sufficiently small positive OR negative tau this is SPD. Its inverse is exactly

N_tau=N-[tau/(1+tau t^T N t)]N t t^T N.

Direct multiplication proves the identity; the denominator is positive near zero. In particular

N_tau t/(t^T N_tau t)=N t/(t^T N t).

The metric-orthogonal foot on T is exactly fixed. For every tangent direction d of T, t.d=0, and hence the restriction of the metric to T is unchanged. For any T vertex x and T-edge direction d,

x^T M_tau d=x^T M d.

Thus all T-carried VE signs and all T-bearing EF/VF locations remain exactly neutral, not just to first order. In the parent's occupied-plane chart, T, its vertices and its edge-bearing quadrilateral planes stay fixed. Combining that shape chart with this metric pencil therefore leaves the T-carried packet fixed until its later carrier opening.

For the off-T contacts, denote the EF source/target poles by r_i,s_i, and the basal VE vertex and other edge endpoint by b_i,e_i. At fixed shape,

Q_{H,i}=-(N r_i)^T H N(s_i-r_i),
P_{H,i}=b_i^T H(e_i-b_i).

The first follows from N'=-NHN; the second from the primal physical row b_i^T M(e_i-b_i). For H=t t^T they read

Q_{T,i}=-(r_i^T N t)[t^T N(s_i-r_i)],
P_{T,i}=(t.b_i)[t.(e_i-b_i)].

These are fixed-shape partial derivatives. The separate shape row P_i already includes motion of BOTH endpoints: none is frozen or counted twice.

Define

ell_i^T=-|p_i|(r_i^T N t)[t^T N(s_i-r_i)]
        +|q_i|(t.b_i)[t.(e_i-b_i)],
Lambda_T=alpha c_1 ell_1^T+c_2 ell_2^T.

If Lambda_T!=0, choose h with h Lambda_T>0, choose s in the nonempty interval in Section2, and lift the resulting g_1=v,g_2=-v through the exact affine halfspaces. All four physical contacts then have strictly positive first derivatives while the true centroid derivative vanishes.

The full actual-centroid map is analytic and its shape derivative is onto R3. The analytic implicit-function theorem integrates this tangent vector, together with the prescribed analytic metric pencil, to an exactly uniformly centred shape-and-metric curve. True lattice and all pre-existing strict guards persist. The four off-T exits open at order one. The parent's T-carrier construction, applied with the nearby physical metric, opens the still-neutral entire T packet at order two; its higher-order occupied-plane centroid correction cannot reverse the order-one exits. Thus Lambda_T!=0 yields a genuine complete-packet regularization germ, not merely a formal tangent test. A nearby physical metric is equivalently realized by a nearby invertible linear Euclidean map, which preserves uniform density and incidence.

## 4. Parallel ends and the normal-EF coefficients

If F and T are parallel, let q be the normalized F pole and theta=q.a for any top vertex a. All top vertices share theta<0, so t=q/theta. Both endpoints b_i,e_i of each basal VE lie on F, giving P_{T,i}=0. Write

gamma_i=(r_i^T N q)[q^T N(s_i-r_i)].

Then

ell_i^T=-|p_i|gamma_i/theta^2,
Lambda_T=-[alpha c_1|p_1|gamma_1+c_2|p_2|gamma_2]/theta^2.

The positive-parallel-normal locus is consequently rescued whenever

alpha c_1|p_1|gamma_1+c_2|p_2|gamma_2!=0.

Opposite-sign gamma pairs are included unless their ACTUAL weighted responses cancel exactly. The weights involve the true centroid maps and physical proportionality of their normals, not arbitrary adjustable positive numbers. If all nonzero gamma have the same sign, noncancellation is immediate, consistent with older signed-normal results; this old sector is not counted again as new coverage.

The residual requires both same-oriented normal coincidence and the additional compatible metric-load cancellation, or a zero-derivative case outside this theorem. No independence of these equations and no codimension claim is made.

## 5. Unrestricted physical metric directions when the T packet is empty

If T has no weak contacts requiring neutrality and the entire weak packet consists only of the two specified pairs, arbitrary symmetric H is allowed. Let sym(u,v)=(uv^T+vu^T)/2 and put

S_i=-|p_i|sym(Nr_i,N(s_i-r_i))
    +|q_i|sym(b_i,e_i-b_i),
S=alpha c_1 S_1+c_2 S_2.

Then Lambda(H)=tr(H S). Therefore S!=0 is necessary and sufficient for rescue within this full-metric/four-plane STRICT-FIRST-ORDER model; H=S gives tr(S^2)>0. Original contact equalities imply

tr(M S_i)=0,

since r_i^T N(s_i-r_i)=0 and b_i^T M(e_i-b_i)=0. A pure metric scaling is correctly neutral; quotienting out that scale does not remove a nonzero S.

If S=0, the first-order obstruction survives all symmetric metric directions in this restricted shape chart, but this is not a conclusion about higher jets or extra facets. With a nonempty T packet, arbitrary H can spoil it; use only the T-neutral pencil or another explicitly justified compatible metric cone. This distinction is essential.

## Remaining research boundary

For opposed nonzero balanced-fibre derivatives, the concrete residual is now actual same-oriented centroid normals together with vanishing compatible metric load, under one physical inverse metric and actual uniform centring. Single-zero halfspaces can be treated by the same affine-image principle using their invariant row; double-zero cases remain wedges and are not claimed covered by the opposed-product formulas above. Whether these residual equalities occur in actual strictS1U1 geometry is open. Their occurrence alone is never proof of nonregularizability.
