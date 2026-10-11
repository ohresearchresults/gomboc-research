# material-4833c840a42f

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# ORDERED_HEIGHT_TRIANGULAR_SLACK_ACTUATOR_V1

## Status and exact predecessors

New analytic coordinator theorem, no new numerical computation or body. It uses the completely read literal minimum-0241, SHA256 08bb47a0c75336c8605fdad5d2cf800e1e0059f4667088a638a8009efa3d968d, and the coordinator's complete ONE_UNUSED_TRIANGLE_CONTACT_NEUTRAL_CENTROID_ACTUATOR_V1, [internal-source-reference] (SHA256 333abc16f59d09decc7e88cb032e8e61bfa8dcc770673a043480e1f5808b7dc4). The latter's executed source [internal-source-reference] is not needed for this purely analytic theorem.

The new connection is an exact positive-support-slack expression for the TRUE triangular second moment. It turns the previous raw determinant into an explicit geometric sign and bounds all possible resonances. For a target-side basal VE or basal F-VF at a triangular leaf, a local parameter omega>=-1/2 is now sufficient for complete-packet escape with ONE unused triangle whose top-apex F-height is no larger. Parallel ends automatically satisfy the height ordering. Source-side VE partners have a separate exact two-threshold test.

Bounds remain 34 <= C_min <= 622. No weakS1U1 input, universal density, whole-E17 exclusion or attaining improvement is asserted.

## 1. True geometry and notation

Use a constant physical normalization M=N=I. P is uniformly filled, full-dimensional, at its actual volume centroid zero. F,T are disjoint true end facets containing all ten vertices, of sizes seven and three. All F vertices are simple. End planes need not be parallel.

Let G=[a,b,c] be a triangular source of a physical EF r->s on the true spoke [a,b], where a is a T vertex and b,c are F vertices. Define

    d=s-r,
    r=lambda b+mu a,                 lambda,mu>0,
    d.a=d.b=d.r=0.

The actual source foot lies strictly inside [a,b]. The third vertex c is NOT on the target facet S. Hence

    d.c=s.c-r.c=s.c-1<0.

The vectors a,b,d form a basis. Write the UNIQUE decomposition

    c=alpha a+beta b+gamma d,        gamma=(d.c)/|d|^2<0,
    omega=beta+gamma lambda.                                  (1.1)

This omega is a new local geometric parameter, not the radial-resonance kappa or any former Delta. It is determined by actual coordinates and poles. No abstract coefficient assignment is allowed.

For a compatible source-plane velocity w with a.w=0 set

    X=b.w,       Z=c.w,       Y=d.w.

Then Z=beta X+gamma Y. If the target pole stays fixed, the exact first EF response is

    Q_rs'=Y-lambda X=(Z-omega X)/gamma.                       (1.2)

The true triangle incidence determinant is nonzero, so X,Z are two genuine fixed-apex coordinates.

Let J be a different lateral triangle, with top apex a_J and pole r_J. It is neither G nor the target S. Put

    theta_G=q_F.a,       theta_J=q_F.a_J,
    c_J=(theta_J+3)/4>0,
    n_J=q_F-c_J r_J.

Actual uniform centering gives -3<theta_J<1. The parent identity T_J^{-1}a_J=12 n_J/(theta_J-1) means the allowed J centroid image is exactly n_J-perp.

## 2. Exact support-slack reduction of the source moment

Define the actual nonnegative support slacks of J at the three G vertices:

    epsilon_a=1-r_J.a,
    epsilon_b=1-r_J.b,
    epsilon_c=1-r_J.c.

Because J is neither of the two facets at the true edge [a,b], it cannot contain both a and b. Thus epsilon_a+epsilon_b>0. This is true-lattice convex geometry, not an assumed strict matrix inequality.

The normalized second moment of a triangle is

    12 T_G = (a+b+c)(a+b+c)^T + aa^T+bb^T+cc^T.

For a.w=0, direct multiplication gives

    12 n_J.T_G w = A X+B Z,                                  (2.1)

where, writing m=theta_G-theta_J,

    A=m+c_J(epsilon_a+2 epsilon_b+epsilon_c),
    B=m+c_J(epsilon_a+epsilon_b+2 epsilon_c).                 (2.2)

To check the cancellation, n_J.a=theta_G-c_J+c_J epsilon_a, while n_J.b=1-c_J+c_J epsilon_b and likewise c. The common constant in each coefficient is theta_G+3-4c_J=m. Nothing has been substituted for the actual face moment.

Assume the ordered-height condition

    theta_G >= theta_J.                                    (2.3)

Then A,B are strictly positive. Define rho=A/B. The exact bounds are

    1/2 < rho <= 2.                                         (2.4)

Indeed,

    2A-B=m+c_J(epsilon_a+3 epsilon_b)>0,
    2B-A=m+c_J(epsilon_a+3 epsilon_c)>=0.

Equality rho=2 can occur only when m=0 and J contains a,c. The lower endpoint is impossible because J cannot contain the true EF edge a,b. If F,T are parallel, all top apex heights agree and m=0 automatically. More generally a corrector with no larger F-height is sufficient.

## 3. The actual centroid-neutral line and the resonance interval

Allow only G,J to move, keeping both end planes and all top vertices fixed. Their actual centroid differential is

    g'=-alpha_G T_G w_G-alpha_J T_J w_J,
    alpha_G,alpha_J>0.

Equation (2.1) says that a G motion can be compensated by J exactly when

    Z=-rho X.                                              (3.1)

The J velocity is then unique, since T_J is nonsingular on its allowed plane. The full three-component centroid map has rank three: its projection onto n_J is the nonzero row A X+B Z, and J supplies the other two directions. Thus the exact actual-COM level set of these four genuine coordinates is a regular analytic CURVE near P.

On its tangent line,

    Q_rs'=(rho+omega)X/(-gamma).                            (3.2)

Consequently the four-coordinate map to (g,Q_rs) is invertible exactly when rho+omega!=0. This identifies the previous chi determinant geometrically: z=a cross(s-2r) is EF-neutral, its X is nonzero, and

    12 n_J.T_G z = B(rho+omega)(b.z).

Thus chi=0 iff omega=-rho. Under the ordered-height hypothesis, every such resonance lies in

    -2 <= omega < -1/2.                                    (3.3)

Outside this interval the one-unused-triangle contact/centroid actuator cannot be singular. This is a statement about genuine geometry of this actuator, not automatic success of every partnered physical inequality.

## 4. Target-side basal VE and basal VF

For a target-side basal VE, the parent's actual incidence calculation gives, with the target fixed,

    P'=c_T X,                    c_T>0.

For a basal F-VF, the actual complementary pair using the target basal edge has

    P_S'=c_T X,
    Q_(F,G)'=|q_F|^2 X.

These equations include all compatible motion of the other basal endpoint. In particular J may move it. They remain the actual complementary pair at a right corner.

Therefore this pair/VF and the EF have a homogeneous positive first direction with actual COM fixed precisely when

    rho+omega>0.                                           (4.1)

Choose X=1,Z=-rho and solve for the unique correcting J velocity. The physical primal/VF exits are positive and (3.2) is positive. A simple geometric sufficient condition, uniform in the choice of eligible J, is

    omega >= -1/2.                                         (4.2)

No determinant calculation, covariance ansatz or unphysical moment relaxation is needed for (4.2).

If other compatible planes have already prescribed finite velocities, the centroid load and local partner responses acquire fixed inhomogeneous terms. The homogeneous direction just constructed can be multiplied by an arbitrarily large positive constant, so these finite biases cannot obstruct positivity. Invertibility then allows nonlinear actual g=0 and Q_rs=tau t with sufficiently large tau>0, exactly as in the predecessor theorem.

### Scope of a negative sign

With ONLY G,J moving and the target and all other planes fixed, rho+omega<0 prevents simultaneous EF/target-VE escape even by higher-order analytic germs. The actual-COM locus is the regular one-dimensional curve proved above; X is a nonzero tangent coordinate, and P,Q have opposite nonzero first derivatives. Their product is therefore negative at every sufficiently small nonzero point of that curve. This excludes that restricted two-plane correction family, NOT all shape motions. At rho+omega=0 the EF derivative vanishes and no all-orders conclusion follows.

The same negative conclusion for a VF concerns the specified X-positive complementary pair only; it is not asserted for every VF alternative. This distinction must not be dropped.

## 5. Source-side basal VE: the second threshold

If b=beta_N r+psi q_F with beta_N,psi>0 is a source-side basal VE, the parent's actual geometry gives d=-k e, k>0, e=c-b. Thus the decomposition in(1.1) has alpha=0,beta=1,gamma=-1/k. Its exact first response with the target fixed is

    P'=(-X+beta_N Y)/k
      =[gamma+beta_N(rho+1)]X
      =beta_N(rho+nu)X,
    nu=1+gamma/beta_N.                                    (5.1)

Together with (3.2), a homogeneous simultaneous positive direction exists exactly when

    (rho+omega)(rho+nu)>0.                                 (5.2)

Choose the sign of X accordingly. Nonzero factors guarantee invertibility. For example omega,nu>=-1/2 suffice; both strictly below -2 also give a direction, with X<0. If one factor is zero, this statement deliberately leaves higher-order behavior open. If the two factors have opposite signs, the two-plane actual-COM curve gives a restricted all-orders obstruction, by the same nonzero-leading-sign argument. Again this is not a full-shape obstruction.

When beta_N lambda=1 the two thresholds coincide, omega=nu. Every nonresonant one-corrector direction can then open both physical rows. This is a special geometric condition, not assumed universally.

## 6. Complete-packet consequence

Apply the parent's full-packet hypotheses, replacing its two unused triangles by a leaf source G (no incoming EF arrow) and one unused triangle J, both outside the source-local protected footprint H_src. All other partnered sources are triangular and unpaired quad sources obey the parent's B_i!=0 condition.

For a target-side VE or basal VF at G, require theta_G>=theta_J and rho+omega>0; omega>=-1/2 is a sufficient local condition independent of which eligible J is chosen. For a source-side VE use(5.2). For an unpaired G only rho+omega!=0 is needed. Reverse-forest velocities for the other sources do not depend on this leaf. The positive homogeneous direction absorbs their finite centroid/local loads; the nonlinear implicit system completes actual COM and the prescribed EF exit.

The entire T-carried packet stays exactly neutral during this stage; top vertices are fixed, triangles do not share a T edge and moving quads retain the prescribed radial top-edge rescaling. Open T at order two using the parent's actual-COM extension. Every handled pair opens at order one; selected complete-packet orders are at most two. In the initially parallel class with arbitrary other protected groups, the parent's auxiliary opening at epsilon=t^2 and exact H_src protection gives order at most twenty, retaining both VF members. Nonparallel ends are permitted for the direct T-carried theorem under the ordered-height condition.

Thus a substantial paired-leaf class now has one-unused-triangle complete-packet regularization without the predecessor's unevaluated determinant or arbitrary affine-response test. It still does not cover every occupied target cluster or paired quadrilateral source.

## 7. Local nonvacuity check, not a new body

On the literal parent's triangle F3 and arrow3->4, let

    a=(R,-1,-1), b=(R,1,1), c=(R,0,1),
    r=(1/R,0,0), d=(0,1/R^2,-1/R^2).

Direct substitution gives alpha=1/4,beta=3/4,gamma=-R^2/2 and lambda=1/(2R^2), hence omega=1/2. This is an exact hand calculation from the parent's coordinates. It verifies that the new local sufficient region is nonempty on genuine actual contact geometry. In the parent's full two-arrow packet F3 has an incoming arrow, so this local calculation by itself is NOT an assertion that F3 meets the leaf hypothesis for that packet. The predecessor's full escape proof for that body remains the separate accepted result.

## 8. Frontier and evidence boundary

This is analytic work. No new code, numerical radius, exact-body identity or target weakS1U1 construction is claimed. The actual triangular second moment, true support slacks and uniform-centroid height range are essential. An arbitrary matrix with the same coarse signs is not a replacement.

Next: determine whether target-class geometry bounds omega or restricts the source-side second threshold; study the residual resonance interval and coupled centroid loads when no unused triangle exists; and handle paired quad sources. Negative two-plane signs are meaningful restricted-family results, but must not be promoted to full-shape nonregularizability or a minimum-complexity lower bound.
