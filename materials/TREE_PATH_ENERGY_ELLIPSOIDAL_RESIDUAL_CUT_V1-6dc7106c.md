# material-6dc7106cabaa

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# TREE_PATH_ENERGY_ELLIPSOIDAL_RESIDUAL_CUT_V1

## Scope and antecedents
This is an analytic, dimension-independent common-metric tree obstruction. It gives explicit negative-arrow stresses from a source subtree, including a quantitative neighbourhood of the closed-reflection obstruction. It does not assert new H5 tree counts, all-root coverage, a construction or a complexity improvement. The accepted research interval remains 34 <= C_min <= 622, with lower exclusion and attainment distinct.

The actual read sources are CLOSED_REFLECTED_EDGE_HULL_KERNEL_COLLAPSE_V1.md, [internal-source-reference], SHA256 d5e2797b9b8bbeba4458e339927569867ff855e828b975d6c0fbd82fc3492f71; H5_LOCAL_SOURCE_SUBTREE_REFLECTION_CUTS_V1.md, [internal-source-reference], SHA256 e75611e233be3c63e18cb811e475ecd7d9fc98bb1df811827ca26cd09eacb063; its complete code [internal-source-reference], SHA256 9e76632309f3ddff40cb7fbe52c6a7df417a009b965cb510bb42dbdee3ab567d; and completely read parent minimum-0245, SHA256 3a4889dd902249e2904ddfa747f00575a10c16646d44cf15224164893c8056be. The antecedent computations were not independently replayed. This theorem is proved below without computational premises.

## 1. Rational path identity
Let P0=A,P1,...,Pd=X be the reverse of a directed path toward A, d>=1. Set

q_j = P_j dot (P_{j-1}-P_j),
sigma_d = (d-1)/(d+1),
Delta_j = P_{j-1}-P_j.

For arbitrary vectors (no arrow assumptions needed), the exact identity is

A dot X + sigma_d |A|^2
 = sum_{j=1}^d q_j
 + (1/2) sum_{j=1}^d |Delta_j-(A-X)/d|^2
 + (d+1)/(2d) |X+sigma_d A|^2.                    (1)

Proof: telescope |A|^2-|X|^2=2 sum q_j+sum |Delta_j|^2, subtract |A-X|^2/d, and complete the square in X. Expansion gives (1) exactly. Thus weak arrows q_j>=0 imply A dot X >= -sigma_d |A|^2. For depth zero put sigma_0=-1, q and both square remainders empty; the corresponding expression is identically zero.

Apply (1) to the images of centred physical vectors under M^(1/2). The statement therefore holds for every PSD M, with no rank or conditioning restriction. Define sym(v,w)=(v w^T+w v^T)/2 and H_{i,p}=sym(u_i,u_p-u_i). Define S_i as the PSD matrix sum of the two square remainders in (1) for the path from descendant i to source a. Then

sym(u_a,u_i)+sigma_depth(i) u_a u_a^T
 = sum_{e on i-to-a path} H_e + S_i.              (2)

## 2. Ellipsoidal residual cut and its explicit stress
Fix one directed edge a->b of a rooted tree. Let D be the source component after deleting that edge, including a. Every i in D has a unique path to a. All u_i=z_i-g use ONE fixed common reference g; for physical applications g must be the actual uniform volume centroid.

Choose arbitrary eta>=0, v_i>=0 for i in D, and mu_i>=0 with sum_D mu_i=1. Put

r = u_a + eta (u_b-u_a)
      + sum_D v_i (u_i+sigma_depth(i) u_a),
G = sum_D mu_i u_i u_i^T,
C = -eta H_ab
      - sum_D (v_i+mu_i) sum_{e on i-to-a path} H_e.             (3)

Every coefficient on the negative-arrow stress C is nonnegative. The following is an EXACT matrix identity:

C = (G-r r^T)/2 + (u_a-r)(u_a-r)^T/2
      + sum_D v_i S_i
      + (1/2) sum_D mu_i sum_{e on i-to-a path} Delta_e Delta_e^T.       (4)

Proof: taking the symmetric outer product of u_a with the definition of r, and using (2), gives

-eta H_ab - sum_D v_i sum_path H_e
 = u_a u_a^T - sym(u_a,r) + sum_D v_i S_i.

The norm telescope gives -sum_path H_e=(u_i u_i^T-u_a u_a^T+sum_path Delta_e Delta_e^T)/2. Average this with mu and complete the square u_a u_a^T/2-sym(u_a,r)=(u_a-r)(u_a-r)^T/2-r r^T/2. This proves (4).

THEOREM. If G-r r^T is positive definite, no nonzero PSD common metric can obey every selected weak arrow on D and a->b. Indeed (4) makes C positive definite, while the weak arrows imply tr(M C)<=0, contradicting tr(M C)>0 for nonzero PSD M.

For G positive definite, the test is equivalently r^T G^(-1) r<1. This is the exact rank-one Schur-complement criterion. No approximate residual is silently declared zero. If only semidefiniteness is proved, keep the residual kernel and analyze its intersection; do not call that a full nonzero-PSD exclusion.

The test needs only a nonnegative cone fit of -u_a to the columns u_b-u_a and u_i+sigma_i u_a, followed by an EXACT rational check of G-r r^T (or directly C). A numerical fit is discovery, not acceptance. Rational v,eta,mu and actual rational coordinates/centroid give an exact certificate. A pointwise certificate excludes only that shape and, by continuity, an unspecified open neighbourhood when geometry is genuine; an explicit parameter domain requires a separate uniform proof.

## 3. Recovering and strengthening the closed-reflection lemma
Suppose theta_i>=0 on S=D union {b}, sum_S theta_i=1, and define the literal physical reflection residual

r0 = 2g - [(1-t)z_b+t z_a+sum_S theta_i z_i],
beta = 1-t+theta_b >= 0,
delta = 1+theta_b-sum_D theta_i sigma_depth(i).

For maximum descendant depth h, delta>=2/(h+1)>0. This includes h=0. The identity

delta u_a+beta(u_b-u_a)
 +sum_D theta_i(u_i+sigma_i u_a)=-r0

shows that (3) with eta=beta/delta and v_i=theta_i/delta has r=-r0/delta. Consequently

  delta^2 G-r0 r0^T positive definite                         (5)

is an explicit sufficient common-metric exclusion, even if r0 is nonzero and the reflected point is OUTSIDE the selected hull.

When r0=0, weak arrows force u_a into the kernel of M by the strict delta gap, and norm monotonicity forces all of D into the kernel. If beta>0, the balance identity also forces b into the kernel. Thus the previous closed-containment conclusion extends to any real t satisfying beta>0 for the supplied representation; the old 0<=t<1 is sufficient but not necessary. At beta=0 only D is forced without an additional span argument. Never remove this qualification.

If r0=0 and centred S spans the ambient space, beta>0 implies span(D)=span(S). Choosing mu positive on D makes G positive definite, so (3)-(4) produce an EXPLICIT positive-definite negative-arrow stress. This algebraizes the earlier path-equality proof. There is no need to infer a strict margin merely from compactness of a metric set.

## 4. Sharp scalar path constant (optional analytic refinement)
For d>=2 the best possible constant replacing sigma_d in the inequality is

kappa_d = cos(pi/(d+1))^(d+1).

Let rho=cos(pi/(d+1)), lambda_j=rho^(d+1-2j), and write P_j=rho^j Z_j. The difference

A dot X+kappa_d |A|^2-sum_j lambda_j q_j

is rho^d times

rho sum_{j=0}^d |Z_j|^2-sum_{j=1}^d Z_{j-1} dot Z_j+Z_0 dot Z_d.

This is PSD: the signed cycle with one negative wrap edge has adjacency eigenvalues cos((2m+1)pi/(d+1)), whose maximum is rho. This eigenvalue formula follows directly by substituting anti-periodic Fourier modes Z_j=exp(i(2m+1)pi j/(d+1)). Equality is attained in R^2 by P_j=rho^j(cos(j pi/(d+1)),sin(j pi/(d+1))); all q_j vanish and A dot X=-kappa_d |A|^2. For d=1 use kappa_1=0 and q_1+|X|^2=A dot X. Depth zero remains kappa_0=-1.

The rational identity (1), not this optional trigonometric refinement, is the premise of the simple stress weights (v_i+mu_i) in (3). If using tighter constants, replace v_i's path contribution by the corresponding lambda_j v_i; the additional mu_i telescope contribution stays mu_i. Do not combine a tighter constant with the unit path weights.

## 5. Coupling scope and negative boundary
For several cuts, any nonnegative combination of their matrices C is still a negative-arrow stress. Positive definiteness of the sum excludes the common metric even when individual cuts have deficient span. However this does NOT enlarge the full original arrow-stress cone: every derived C already is a nonnegative combination of -H_e. Conversely choosing only v=0, eta positive and allowing the unexpanded source expression recovers an individual arrow. The value of this route is explicit geometric weights, a quantitative floor and potential uniform parameter certificates, not a magical stronger SDP relaxation or a repair of the previously failed global quadratic lowering.

An elementary genuine control is the uniformly filled tetrahedron with vertices e1,e2,e3,(-1,-1,-1), whose centroid is zero. For its three-leaf star rooted at (-1,-1,-1), none of the individual two-point source/target affine lines contains zero, so no exact reflected-edge inclusion on a single leaf pair is possible for any t. Nevertheless the sum of the three negative-arrow matrices is I+11^T, positive definite. This illustrates coupling relative to individual reflection tests only; it is not an H5/E17 result or a new lower bound.

## 6. Evidence boundary and continuation
The proofs (1)-(5) are analytic and complete in this material. An auxiliary standard-library checker was executed for 32 formal path identities, nine tighter rational PSD path constants, and the tetrahedron example, but its attempted material upload was blocked; its current sandbox bytes are not a durable canonical source. No computed H5 exclusion is claimed here. The scientific next test is the actual moving-centroid H5 residual p+q>1/2, especially trees with no closed mixed-layer reflection guard, using cone fitting only to discover exact rational stresses and then proving their explicit parameter domains without dropping polynomial terms.
