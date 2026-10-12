# material-7a7d98ef8123

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# ACTUAL_SATURATED_VE_PAIR_CENTROID_HALFSPACE_REDUCTION_V1

## Scope and evidence

This coordinator result continues the fully read immutable parent minimum-0243, SHA256 f1787b59aa7ef14d2e4fb0a713f71f978f5f0ddea762226b426e54aea8d13b7d (SATURATED_OCCUPIED_TRIANGLE_PAIRS_ESV_ESCAPE_AND_BALANCED_FIBRES_V1). Its actual uniform-centroid moment map, valid local facet chart and T-carrier gluing are working premises from that author's proof, not independently replayed constructions. The linear image theorem and the target-VE local formulas below are proved here. The latter were checked by a new complete symbolic/rational source unit in both a normal and a source-only cold directory.

No new polyhedron, weak110 input, full-E17 exclusion, universal regularization theorem, numerical radius or improvement of 34<=C_min<=622 is claimed. In particular the exact local control in Section 5 is NOT an actual uniform-centred V10/E17/F9 body. It refutes a proposed LOCAL algebraic implication, not a theorem incorporating global actual-centroid or S1U1 restrictions.

## 1. Image of a two-contact opening cone under a rank-three moment map

Let W:R^4 -> R^3 have rank three and kernel span{k}. Let Q and P be independent real linear forms on R^4. They are the signed EF and VE first derivatives, with Q>0 and P>0 denoting the desired local openings. Write q_k=Q(k), p_k=P(k). The image

C = W{z: Q(z)>0, P(z)>0}

has the following exact classification.

* If q_k*p_k>0, C=R^3. Indeed, add an appropriately oriented sufficiently large multiple of k to any preimage.
* If q_k*p_k<0, set h=|p_k| Q+|q_k| P. It annihilates k. There is a unique nonzero covector m on R^3 with W^T m=h^T. Then C={c:m.c>0}.
* If q_k=0 and p_k!=0, Q factors uniquely through W and C={c:Q_bar(c)>0}. The case p_k=0,q_k!=0 is symmetric.
* If both vanish, both forms factor through W and C={c:Q_bar(c)>0,P_bar(c)>0}. This is a genuine two-halfspace wedge because independence descends to the quotient.

For the second assertion, fix a preimage z of c. Any other is z+t k. The inequalities Q(z)+t q_k>0 and P(z)+t p_k>0 give one lower and one upper bound for t. The interval is nonempty exactly when |p_k|Q(z)+|q_k|P(z)>0. This is h(z)=m.c. The other cases follow by the same one-variable argument. Independence ensures that the halfspace normal is nonzero. This proves the classification, not merely a sufficient dual test.

## 2. Actual two-pair regularization: only oriented normal coincidence remains at first order

Use the parent's actual homogeneous heptagon-triangle setting: V10/E17/F9, disjoint true heptagonal F and triangular T containing all vertices, not necessarily parallel; two interior-spoke EF pairs use FOUR DISTINCT triangular source/target planes. Keep F,T, the three top vertices and all other planes fixed while the occupied triangles vary in their genuine four-plus-four coordinate chart. There is at most one basal VE partner per pair here; this section does not replace the separate VF selector analysis. Suppose the complete off-T weak packet consists of those pairs and their specified partners.

For each pair i, the author's actual centroid derivative is L_i=-c_i W_i, c_i>0, and rank W_i=3. The two local contact derivatives depend only on the pair's own source/target plane velocities. For a target VE, motion of the other endpoint caused by a third plane is already included in the formula in Section 3 and cancels from this dependency; it must not be artificially frozen.

When q_ki*p_ki<0 for both pairs, form m_i by Section 1 in COMMON physical coordinates. The image of the pair's admissible velocities under the actual centroid derivative is the strict halfspace H_i={g_i:n_i.g_i>0}, where n_i=-m_i. The positive scalar c_i does not affect its orientation. There is a simultaneous first-order opening with g_1+g_2=0 IF AND ONLY IF n_1 and n_2 are not positive scalar multiples of each other.

Proof: write g_1=v,g_2=-v. We need n_1.v>0 and n_2.v<0. If n_2 is a positive multiple of n_1 this is impossible. If they are linearly independent, solve n_1.v=1,n_2.v=-1. If they are negative multiples, take n_1.v>0. Section 1 supplies actual plane velocities for each chosen centroid derivative. This also applies to the single-zero halfspace cases of Section 1, with their appropriate normals. A pair with image R^3 can correct any feasible other pair, recovering the parent's balanced-fibre mechanism. Double-zero wedges require their full intersection test and are not silently promoted to halfspaces.

The simultaneous nonzero contact velocities integrate to a genuine analytic actual-centred shape curve. The full centroid map in the eight genuine plane coordinates is analytic, with rank-three derivative (already one W_i has rank three), so its zero level is a smooth analytic manifold. Every vector in its tangent space extends to an analytic curve on that manifold. The four chosen contact derivatives are strictly positive, hence those exits hold for small positive parameter. True lattice and previously strict guards persist by openness. The top triangle and its adjacent non-triangular planes are unchanged, so the complete T-carried packet remains fixed during this first-order motion; the parent's later T-carrier construction opens it at order two, with centroid correction on the occupied planes of the same higher order. The already positive order-one exits survive that correction. The result is an actual same-lattice fixed-physical-metric regularization germ, not merely a first-jet claim.

Important limits: positive parallel normals rule out a STRICT FIRST-ORDER opening in this four-plane fixed-metric chart only. They do not rule out higher-order contact-flat motion, additional facet freedoms, changes in physical metric, or a different selector. No all-orders obstruction follows. The two pair coordinate frames can differ: if physical vertices equal B_i times their adapted coordinates, transform an adapted m_i to B_i^{-T}m_i before comparison. The two adapted metric matrices must come from the SAME physical metric; choosing them independently does not construct a two-pair example.

## 3. Complete local adapted inverse-metric form for an EF with target VE

Use a,b,c as a vector basis, represented by the coordinate unit vectors, and physical inverse metric N=M^{-1} in this adapted basis (do not reset it to identity). The triangular source and target poles and the basal pole are

r=(1,1,1), s=(1,1,1-j), q=(1-H,1,1),
e=(-ju/H, 1+u+(1-H)ju/H, -u),

where R=[a,b,c], S=[a,b,e], H,j,u>0. Thus q.b=q.c=q.e=1, q.a=1-H, s.e=1, and critically r.e=1-ju, not 1+ju. Actual uniform nonpyramid bodies in the parent's class impose 0<H<4,0<j<4,0<ju<4.

An interior EF has Nr=(mu,lambda,0), mu,lambda>0. A target-side VE at b on basal edge b-e has

b=beta N s+psi N q, beta,psi>0.

Set nu=j N_33>0. The third component implies t=1+j N_23/nu>0 and psi/beta=j/(Ht). Put

D=Ht(mu+lambda)+j((1-H)mu+lambda),
beta=Ht/D, psi=j/D,
alpha=mu/H+mu t/j,
v=(-t,t-1,1).

Then the symmetric inverse metric is necessarily

N = [[alpha, mu-alpha, 0],
     [mu-alpha, lambda-mu+alpha, 0],
     [0,0,0]] + (nu/j) v v^T.

Conversely, for positive H,j,mu,lambda,t,nu and D>0 this N is SPD and satisfies both contact identities with beta,psi above. Its Schur complement at N_33 is the displayed leading 2x2 block, whose leading entry is alpha>0 and determinant mu D/(Hj)>0. Also det N=mu nu D/(Hj^2)>0. This is a local metric/contact parameterization, not a global actual-centroid existence theorem.

Let the source velocity w have evaluations (a.w,b.w,c.w)=(0,x,y), and target velocity v_s have (a.v_s,b.v_s,e.v_s)=(0,X,Z). With q fixed,

b'=(-x/H, -x+x/H-(X-x)/j, (X-x)/j).

Solving N ell=e-b gives the exact physical edge covector

ell=M(e-b)=(-ju/mu,0,-ju/nu-jtu/mu).

The actual target-VE derivative, including motion of e, is

P' = b'.M(e-b)+beta(X-Z).

Indeed b^T M=beta s^T+psi q^T, while differentiated plane incidences give s.e'=-v_s.e, s.b'=-v_s.b and q.e'=q.b'=0. Any contribution from the third facet determining e therefore cancels; freezing e would be incorrect.

Writing L=ju/(mu H) and A=u/nu+ut/mu+L yields the two independent rows

Q=(-lambda-nu(t-1), -nu, lambda, 0),
P=(A, 0, beta-A+L, -beta).

The EF formula follows from Q'=w^T N(s-2r)+r^T N v_s. Independence follows from Q_y=-nu!=0 and P_Z=-beta!=0.

## 4. Explicit normal with the actual triangular moments

The author's moment map is

W=[a+2b+c, a+b+2c, u(a+2b+e), u(a+b+2e)],
k=(2u,-u,-2,1),
det W_{123}=ju^2(H-4)/H!=0.

Consequently

q_k=u nu(3-2t)-2lambda(u+1),
p_k=2(u+1)A-2L-3beta.

For any row z=(z1,z2,z3,z4) annihilating k, put

D_n=(z2-z1)/j,
B_n=(z4-z3)/(j u^2),
K_n=2z1-z2,
A_n=[K_n+4(B_n+D_n)]/(4-H).

Then m=A_n q-B_n r-D_n s is the UNIQUE solution W^T m=z^T. This follows by evaluating m on the four columns:

(K_n+jD_n, K_n+2jD_n, uK_n+ju^2B_n, uK_n+2ju^2B_n).

For opposed nonzero q_k,p_k, take z=|p_k|Q+|q_k|P. Section 2 then uses the physically transformed normal -m. This formula gives an exact, directly computable reduction of saturated target-VE packets to oriented normal coincidence.

## 5. Exact local negative control against importing the E/S/V support-sign proof

Choose H=j=u=mu=lambda=nu=1/2 and t=3. All three necessary uniform height bounds 0<H,j,ju<4 hold. Then

e=(-1/2,7/4,-1/2), beta=4/5, psi=4/15,
N=[[13,-19/2,-3],[-19/2,8,2],[-3,2,1]],
M=[[16/15,14/15,4/3],[14/15,16/15,2/3],[4/3,2/3,11/3]].

M has leading minors 16/15,4/15,4/15, hence is SPD. Nr=(1/2,1/2,0) puts the EF in the relative interior of a-b. Also b=beta Ns+psi Nq is an actual positive VE cone equality for this local geometry. The derivative rows are

Q=(-3/2,-1/2,1/2,0), P=(5,0,-16/5,-4/5),
q_k=-9/4, p_k=53/5,
z=|p_k|Q+|q_k|P=(-93/20,-53/10,-19/10,-9/5).

The corresponding positive-combination conormal has

(A_n,B_n,D_n)=(-12/7,4/5,-13/10),
m=(-5/14,-17/14,-261/140),
(m.a,m.b,m.c,m.e)=(-5/14,-17/14,-261/140,-71/70).

In the unique orientation with positive q coefficient, -m=(12/7)q-(-4/5)r-(13/10)s, so B_n=-4/5<0 and (-m).a=5/14>0. Thus the parent's E/S/V normal pattern A,B,D>0 with a negative top value cannot simply be asserted for target VE from local contact positivity and the necessary height bounds. This is not a full-body counterexample: no remaining six vertices, actual centroid, full lattice or equilibrium census has been constructed. Global uniform-centroid/S1U1 constraints may still prohibit this local pattern.

## 6. Exact recovery and observed checks

The complete independent source is material [internal-source-reference], filename target_pair_centroid_cone.py.txt, 3954 bytes, SHA256 7c89e962c8d30da5a86702ad94dcae346ff518511acc14c95c1adedaf9bf1306. It includes every symbolic formula and every rational input above and requires no other research source files. It does not reconstruct the parent558 body and makes no claim to do so.

Save the exact source as target_pair_centroid_cone.py. Reconstruction/verification command:

python target_pair_centroid_cone.py > target_pair_centroid_cone_report.json

Observed environment: CPython3.13.5, SymPy1.14.0. Both normal and source-only cold-directory runs passed. Reproduced report target_pair_centroid_cone_report.json is 1619 bytes, SHA256 ce4c3711c7d6dd4ba87a869630470b398a1dfbd44566729413b70c9f979eb09f. The report includes environment version strings, so another interpreter version may change its bytes without invalidating the assertions.

Expected terminal markers are TARGET_VE_CENTROID_CONE_IDENTITIES_PASS and LOCAL_TARGET_CONORMAL_ESV_SIGN_EXTENSION_FAILS_PASS. Exact assertions cover the symbolic metric/contact identities, Schur determinants, physical edge covector, endpoint-inclusive derivatives, W kernel/determinant, q_k/p_k formulas, general conormal reconstruction and rational control. The general strict-halfspace image and analytic integration arguments are the proofs above, not conclusions inferred from a numerical scan.

## Next consequential question

For actual saturated pairs with at least one target VE, determine whether equal oriented centroid-opening normals can occur under a common physical metric, actual uniform centring and the full heptagon-triangle lattice, particularly with strictS1U1. If they can, use physical metric variations or genuine higher-order/full-plane motions to resolve them. Single-zero cases fit the halfspace reduction; double-zero cases retain a wedge. An arbitrary pair of independently chosen local metrics is not evidence of a global obstruction.
