# material-2c914bd63d84

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# NONPARALLEL_TWO_TRIANGLE_ACTUATOR_AND_PAIRED_BLIND_ESCAPE_V1

Coordinator analytic continuation of the completely read literal result minimum-0239, SIGNED_NORMAL_BLIND_CONTACT_AND_TRIANGLE_CAGE_ESCAPE_V1, SHA256 02d2c6a3a9b0e54366f01c86b298d2055aea3037c342d8389b23e4b4dd465a38. No new numerical computation, physical input, weak110 witness, proof-assistant check or executable recovery claim is made. The proofs and exact local construction below are the complete new source. The global interval34<=C_min<=622 is unchanged.

## I. A nonparallel two-triangle actual-centroid actuator

### Statement
Let P be a uniformly filled full-dimensional convex3-polytope with actual centroid0. Let F have normalized true supporting pole q, so q.x=1 on F. Suppose G_i=[a_i,b_i,c_i], i=1,2, are two distinct triangular facets meeting F in distinct true edges [b_i,c_i], with a_i outside F. Suppose P is not a pyramid over F. Then the two linear actual-centroid images obtained by rotating each G_i plane while fixing a_i are distinct two-dimensional planes and together span R^3. Parallelism of a top plane and F is NOT required; a_1 and a_2 may coincide or differ.

For a genuine local plane-motion realization and implicit centroid correction, assume in addition that every vertex of F is simple. Hold F, all other supporting planes and all vertices outside F fixed; allow r_i to vary subject to a_i.r_i=1. These are four genuine local shape coordinates. Three of their coordinates can correct an arbitrary sufficiently small compatible prescribed perturbation of the other planes to keep the original uniformly filled body's actual centroid0. No uniform conditioning bound or neighborhood radius is asserted.

### 1. Uniform support-height inequality, including its equality case
For any vertex a outside F put theta=q.a<1. Cone a true boundary triangulation to a. Each positive-volume tetrahedron [a,u,v,w] has average q-coordinate at most(theta+3)/4 since q.u,q.v,q.w<=1. The actual volume-weighted mean is0, hence theta>=-3. If theta=-3, every positive-volume tetrahedron must have all three other vertices on F. Their union is then contained in conv(a,F), so P=conv(a,F). Conversely the centroid of that pyramid has theta=-3 in this normalization. Thus a nonpyramid over F satisfies -3<theta<1 for EVERY such a. This is a statement about the true uniform volume measure, not a freely assigned centroid or polar volume.

### 2. The exact triangular second-moment identity
For a triangular facet G=[a,b,c] with pole r define
T_G=mean_G xx^T=[(a+b+c)(a+b+c)^T+aa^T+bb^T+cc^T]/12.
T_G is SPD because the facet plane does not pass through0 and its three vertices span R^3 linearly. With theta=q.a and q.b=q.c=1,
T_G r=(a+b+c)/3,
T_G q=[(2theta+2)a+(theta+3)(b+c)]/12.
Consequently, putting c_G=(theta+3)/4,
T_G^{-1}a=12/(theta-1) [q-c_G r],              (1)
with 0<c_G<1.

For a moving normalized pole r, actual boundary normal velocity is -(delta r.x)/|r|. At centroid0 the true filled-volume centroid derivative is
D_r g= -Area(G)/(V|r|) T_G delta r.
Allowed rotations fixing a satisfy a.delta r=0. Their image plane therefore has normal T_G^{-1}a, proportional to q-c_G r. This calculation is coordinate-invariant and does not choose independent primal/polar metrics.

### 3. Why the two image normals cannot be parallel
The required argument is slightly stronger than affine collinearity of three polar vertices: proportionality of q-c_1 r_1 and q-c_2 r_2 does not by itself imply that q,r_1,r_2 are affinely collinear. Use both the geometry of the true F edges and polar convexity instead.

Choose f in relint F. Make a fixed invertible linear coordinate change, preserving centroid0, such that q=e_3 and f=e_3. Write r_i=(v_i,z_i). The corresponding supporting edge line in F is v_i.y=1-z_i. Since f is in the relative interior and G_i is a different true facet, 1-z_i>0 and v_i is nonzero. Distinct true edges of a convex polygon cannot have positively proportional outward horizontal normals: in any fixed direction there is a unique supporting line and one maximal true edge. Hence v_1 and v_2 cannot be positive proportional.

Suppose q-c_1 r_1=t(q-c_2 r_2). Horizontal parts exclude t>0, and t=0 is impossible. If t=-u<0, then
q=[c_1/(1+u)]r_1+[u c_2/(1+u)]r_2.
The two positive coefficients have sum strictly less than1 because 0<c_i<1. This expresses the boundary point q of the polar P^circ as a convex combination of r_1,r_2 and a strictly positive weight of its interior point0. The combination is interior, a contradiction. Thus the two image planes are distinct and their sum is R^3. This establishes the rank without assuming equal theta_i or parallel end planes.

### 4. Actual realization and centroid correction
When F has only simple vertices, every moving basal vertex is the intersection of the F plane and its two incident lateral planes. The apex of a moving triangular facet is held fixed by the exact equation a_i.r_i=1, even when that apex is nonsimple. No other outside vertex lies on that triangular facet. Thus all outside vertices stay fixed and all true incidences are preserved; strict nonincident supports remain strict for sufficiently small motions. Triangles sharing an apex or a basal vertex cause no exception.

Choose two independent pole coordinates in each plane a_i.delta r_i=0, and the first nonsingular three-column minor of the actual centroid derivative. Hold the fourth coordinate fixed. The actual centroid is analytic in these genuine local coordinates through rational fan-volume moments with V>0. The analytic implicit function theorem gives a uniquely specified local correction in the chosen three coordinates. If the prescribed outside vertices vary in an auxiliary family, impose their current equations a_i(epsilon).r_i=1; the same nonsingular choice persists locally. This is a real uniformly refilled shape construction, not formal vertex loading. The rank claim itself did not require simplicity of F; simplicity is used only to ensure these independent plane motions are genuine realization coordinates.

## II. The forced basal VE and equal-height blind spoke EF have the SAME first-order request

Use the literal parent's physical normalization: initial M=N=I, F:z=h, T:z=k, h>0>k, q_F=e_z/h, q_T=e_z/k. Let r->s be an actual interior-spoke EF with equal vertical pole components r_z=s_z and r_z<=0. Its spoke has basal endpoint b and top endpoint a. The literal parent proves that b is a genuine VE on the true basal edge [b,b'] contained in F cap R, with
b=beta r+psi q_F, beta,psi>0.
It also proves, putting e=b'-b, that
s-r=-c e, c>0.                                    (2)
These facts follow from actual normal-cone incidence, not from arbitrary contact tensors. This VE is a separate physical weak point from the interior EF.

Keep the two end planes, all top vertices, and M=N=I fixed. Prescribe lateral pole rates exactly as in the parent:
r(t)=q_T+(1+t k_r)(r-q_T),
s(t)=q_T+(1+t k_s)(s-q_T).
Other compatible plane motions are allowed, including actual-centroid correction, provided they do not change these two prescribed poles or the end planes. Reconstruct basal vertices by their true plane intersections. Put C=1-q_T.b=1-h/k>0 and A=|r|^2-q_T.r>0.

The parent dual response is, because q_T.(s-r)=0,
Q_rs'=A(k_s-k_r).                                  (3)
For the forced basal primal row P_bb'=b.(b'-b), differentiate. Since q_F is fixed and b,b' both stay in the r(t) plane,
b.(delta b'-delta b)
=beta r.(delta b'-delta b)+psi q_F.(delta b'-delta b)
=-beta delta r.(b'-b)=0,
because r.e=q_T.e=0. Therefore P_bb'=delta b.e. Meanwhile the two source incidences give
r.delta b=-k_r C, s.delta b=-k_s C.
Subtract and use(2):
P_bb'=(C/c)(k_s-k_r).                               (4)
Thus the two independently required physical exits have the same sign, with the exact positive ratio P'/Q'=C/(cA). The simultaneous inequality k_s>k_r opens BOTH, regardless of how the target vertex b' moves under other allowed planes. In particular it is unnecessary to freeze both EF poles merely to protect this particular basal VE. The identity is first-order; no false all-orders preservation of equal pole heights is asserted.

The r_z<=0 hypothesis is used to ensure that the basal point is actually a VE. The algebraic differentiation remains valid whenever the displayed actual VE and equal-height hypotheses hold. The other blind mechanism r_z=0 with s_z!=r_z is NOT included. Equal-height r_z>=0 may instead force a top VE or a labelled strict top U as in the parent; that is a different conclusion.

## III. Reduced-footprint complete-packet theorem

This advances the parent's isolation theorem without claiming unconditional regularization. Begin with any actual uniformly filled parallel heptagon-triangle V10/E17/F9 body and its complete original weak packet. Let D be its directed forest of interior-spoke EF arrows. Choose any subset B of the equal-height blind arrows with r_z<=0 from SectionII, and omit their forced basal VE groups when building the parent's non-spoke protected footprint H. Retain every other zero primal/polar group and the full complementary VF protections exactly as in the literal source. Call the resulting set H_red.

Assume there are two distinct lateral triangles outside H_red and outside all endpoint poles of D. Assume the parent's exact rate test succeeds with k_i=0 on H_red: start forced-positive targets of fixed-source arrows and of arrows with B_i=0, propagate positivity across B_i>0 arrows, and require that the resulting set avoid H_red. Equivalently the complete physical forest admits A_i k_j-B_i k_i>0 on every D arrow with these fixed nodes. Use the parent's explicit backward assignment to choose such rates.

Then the ENTIRE original weak packet has analytic same-lattice actual-COM regularization, retaining all strict labels, with selected positive orders at most20. The gamma signs of the other spoke EFs are arbitrary. Compared with the parent's sufficient test, the footprint need not freeze a VE merely because it is the forced partner of a chosen equal-height blind EF. This is a weakened sufficient hypothesis, not a claim that all remaining inputs satisfy it.

### Construction and proof
Use the literal parent's partial construction R(epsilon) to open all non-spoke contacts while initially ignoring the spoke-EF signs. It gives their positive exits at orders at most10, a true same-lattice realization and the actual uniform centroid. Set epsilon=t^2. On R(epsilon), apply the top-fixed lateral pole rates with k=0 on H_red, keeping its current end planes fixed. Use the two unused triangular planes for the actual-centroid correction, by SectionI (so even an auxiliary loss of end parallelism does not obstruct the actuator).

All original spoke-EFs have c_ij t+O(t^2)+O(epsilon), c_ij>0. Their source and target poles are not correction planes. For an arrow in B, B_i=A_i, so its strict forest inequality forces k_j-k_i>0. Equation(4) gives the matching basal VE a positive first-order coefficient as well; auxiliary movement contributes O(epsilon), hence cannot spoil it. A correction plane may touch that VE's target vertex, but the cancellation in(4) is valid for arbitrary compatible target motion. It cannot touch its source through one of the two EF poles, because all D endpoint poles are excluded from the correcting pair.

Every remaining selected non-spoke row is kept exactly fixed, or multiplied by the parent's positive T-source factor, by H_red and the fixed end/top coordinates. This includes both members of each selected VF pair. Those exits remain positive with orders at most20 after epsilon=t^2. Original nonzero guards persist locally. The actual centroid correction is analytic and the physical metric and its actual inverse are held fixed during this support-plane stage. The selector and index conclusions are therefore the same as in the literal full-packet theorem.

### Limits and next real obstruction
The compulsory basal-VE/EF overlap alone no longer blocks this sufficient support-plane mechanism: it can be treated as a single shared rate request rather than two frozen poles. Other contacts may still put those poles in H_red. The two unused triangular actuators may not exist, or the residual fixed-node rate propagation may still conflict. None of these failures proves all-shape nonregularizability. There is no supplied weakS1U1 input. The nonparallel actuator theorem by itself is not a nonparallel full-packet theorem; SectionsII-III use an initially parallel end configuration and the literal parent's opening construction. Proper110 density, exclusion of the whole E17 layer and the separate attaining problem all remain unresolved.
