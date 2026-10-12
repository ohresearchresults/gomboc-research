# material-73368842a011

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# H5_CANONICAL_REFERENCE_AND_TEMPLATE_BLINDNESS_V1

## Scientific scope

This continues the coordinator's persisted H5_INTRINSIC_REFERENCE_REFLECTION_HYBRID_V1, [internal-source-reference], without changing its literal actual-centroid H5 body or its physical metric. It has two complementary results:

1. A canonical reference adapted to the top triangle reduces its best hybrid product ceiling to one strictly convex scalar minimization, with a unique global optimum identifiable by rational breakpoints or a quintic equation. This is a general analytic identity on the actual H5 family, not a local optimizer assertion.
2. A reference-independent lower bound on this particular finite-height product TEMPLATE proves that no choice of auxiliary ellipsoid, even a different one for each possible top maximum, can close the template at an exact genuine H5 control with lambda=3/25. This is not a110 construction, not feasibility of the full joint metric inequalities, and not a theorem that every stronger spectral or geometric argument must fail.

The first exact hybrid box remains accepted. Whole H5, E17, and the exact minimum remain open; 34<=C_min<=622 remains unchanged. There is no new attaining example here.

## Dependencies and symbols

The actual uniform-centroid H5 family, moment formulas, true nine facet cycles, and hybrid implication are specified completely in [internal-source-reference]. Its exact two source files are [internal-source-reference] and [internal-source-reference]. The accepted original seven-turn parent is minimum-0255, SHA256 b02e9ea175553f06a5fc27b626e52977c8baf76d50df0e70d68eff5fb913393e, read in full. The reference finite-height foundation is [internal-source-reference], SHA256 d40619accf0fc38f68f9155c87c3ea2f5cf8ce8c590dfa1b3477cad75cbbe100, also read in full.

M is always the single physical SPD metric about the actual uniform centroid. N=M^-1 is its actual inverse. C is an auxiliary reference only. Define

    Gamma_C=(max_true_vertex v v^T C^-1 v)(max_true_pole q q^T C q),
    chi_C(a,q)=(a^T C^-1 a)(q^T C q)/(a.q)^2-1,
    L_K(chi)=((K+1)sqrt(1+chi)+(K-1)sqrt(chi))^2/(4K).

Under joint S1/U1 at V10/E17/F9, condition(C^.5 M C^.5)<=F Gamma_C^2, where the exact finite-height factor is

    F=f(10)f(9), f(m)=cos(pi/(2m))^(2m), 9/16<F<16/27.

A larger F such as16/27 is a safe upper majorant, but never an improved smaller condition bound. The scalar product ceiling L_K is nondecreasing for K>=1 and chi>=0. The hybrid geometric argument with reflection parameter alpha requires

    L_K(chi_C(a,qB)) <= gamma/(gamma-alpha^2)

for every possible top maximum a, when alpha^2<gamma. Here qB is the basal true pole, and gamma is the actual fractional centroid height. It is enough to use different references for different possible a, provided each condition statement still concerns the same M.

## A canonical top-triangle reference

Write the raw top vertices as (0,0,1),(lambda,0,1),(0,lambda,1), and the actual centre as g=(g_H,gamma). Put

    h=1-gamma, u=(lambda/3,lambda/3), m=u-g_H,
    D=[[2,-1],[-1,2]], e=2 lambda^2/9,
    s2=(gamma/h)^2.

For k>0 define

    C(k)=[[kD+m m^T, h m], [h m^T, h^2]].                   (1)

The block Schur complement is kD, so C(k) is positive definite. This covariance-looking expression is only a designed reference. It is not the actual uniform covariance and does not alter the body's centre, boundary, or physical metric.

For a centred true vertex v_i=(t_i,z_i), define

    w_i=t_i-(z_i/h)m,
    r_i=w_i^T D^-1 w_i,
    a_i=(z_i/h)^2.

For a true normalized pole q_f=(q_H,q_z), define

    ell_f=q_H^T D q_H,
    b_f=(m.q_H+h q_z)^2.

Direct block inversion gives the identities, for all k>0,

    v_i^T C(k)^-1 v_i = r_i/k+a_i,
    q_f^T C(k) q_f = ell_f k+b_f.                         (2)

Every coefficient r_i,a_i,ell_f,b_f is nonnegative. At all three top vertices a_i=1 and r_i=e, because their displacements from u have the same D^-1 norm. At all seven basal vertices a_i=s2. If R=max_basal r_i, then

    Gamma(k)=max(1+e/k, s2+R/k) max_f(ell_f k+b_f),        (3)
    chi_C(k)(a,qB)=e/k for all three top vertices.         (4)

Thus only two primal pieces and nine polar pieces remain. Formula(3) is the maximum of eighteen expressions A+B k+D0/k, where A,B,D0>=0. The basal pole has ell_B=0 and b_B=(h/gamma)^2, while some nonbasal pole has ell_f>0. These facts also give coercivity below.

## Unique global minimization and exact finite reduction

Assume 0<gamma<1/2 and F Gamma(k)^2>=1 for all k>0. A convenient sufficient condition for H5 is gamma<=4/9 and F>=9/16, because Gamma(k)>=(h/gamma)^2 and hence

    F Gamma(k)^2 >= (9/16)(5/4)^4 =5625/4096>1.

For K=F Gamma(k)^2, put w=sqrt(1+e/k)+sqrt(e/k). Then

    L_K(e/k)=(sqrt(F)Gamma(k)w+[sqrt(F)Gamma(k)w]^-1)^2/4. (5)

The argument sqrt(F)Gamma(k)w is at least1, so minimizing this ceiling is equivalent to minimizing, with t=log k,

    J(t)=log Gamma(exp t)+asinh(sqrt(e)exp(-t/2)).          (6)

Each log(A+B exp t+D0 exp(-t)) is convex: it is a log-sum of nonnegative multiples of exponentials. Its maximum is convex. The second term in(6) is strictly convex for lambda>0; setting x=sqrt(e)exp(-t/2), its second derivative is

    x/[4(1+x^2)^(3/2)] >0.

Consequently J is strictly convex. As t tends to minus infinity, the positive e/k term and basal polar constant force Gamma to diverge; as t tends to plus infinity, the positive top constant and a positive ell_f force divergence. Therefore J is coercive and has exactly one global minimizer. It is not merely unimodal in the sampled interval. The minimizer does not depend on F within the above admissible range, since F adds only the constant(1/2)log F to the logarithm in(5).

All candidate switching values are explicit rational expressions in the actual shape data:

    k=(R-e)/(1-s2), when positive,
    k=(b_j-b_f)/(ell_f-ell_j), when positive and ell_f!=ell_j.

Including inactive crossings is harmless. Between successive such values, the maximizing primal piece and polar line are fixed, and Gamma=A+B k+D0/k. An interior stationary point must satisfy

    2(Bk^2-D0)/(Bk^2+Ak+D0)=sqrt(e/(k+e)),
    Bk^2>D0,

so it solves the quintic

    4(k+e)(Bk^2-D0)^2-e(Bk^2+Ak+D0)^2=0.                (7)

The sign condition must not be discarded when squaring. In ascending powers, its coefficients are

    [3eD0^2, 4D0^2-2eAD0, -10eBD0-eA^2,
     -8BD0-2eAB, 3eB^2, 4B^2].

A change of derivative sign across a rational switching value identifies the unique global minimizer exactly. Otherwise the unique stationary point is isolated in its active interval by rational derivative-sign tests; strict convexity proves uniqueness without assuming that the quintic has only one real root globally. This is a complete finite algebraic reduction of this canonical family, not of all SPD references.

## Reference-independent blindness of the finite-height product template

Let a be any top vertex and qB the basal pole. Their pairing is a.qB=-(1-gamma)/gamma. Set c=(1-gamma)/gamma>1. For every positive-definite C, by the definitions of the two maxima,

    Gamma_C >= (a^T C^-1 a)(qB^T C qB)=c^2(1+chi_C).    (8)

Hence for the template K_ref=F Gamma_C^2, when F c^4>=1,

    L_K_ref(chi_C) >= L_(F c^4)(0)
                   = (F c^4+1)^2/(4F c^4).             (9)

This is a lower bound on the UPPER CEILING produced by that sufficient certificate. It is not a lower bound on the actual physical product, and does not imply a physical feasible metric exists. It says that this particular route cannot manufacture a smaller upper bound merely by changing C.

For actual H5 with gamma<=4/9, set k0=(9/16)c^4>1. Since the exact factor F is strictly greater than9/16, every reference gives the strictly stronger floor

    L_K_ref(chi_C) > (k0+1)^2/(4k0).                    (10)

The same conclusion holds for any safe larger majorant such as16/27. It holds separately for every top vertex, so top-specific references do not evade it. It also holds for a minimum or infimum over arbitrarily many such reference choices. Taking a smaller K from a genuinely stronger geometric or tree-dependent argument is outside this obstruction.

If alpha_max is an upper bound for every R-admissible positive alpha and alpha_max^2<gamma, the largest possible geometric target is gamma/(gamma-alpha_max^2). If it is less than the floor(10), all R-admissible instances of this hybrid template fail for every reference. Equivalently a necessary condition for any success is

    alpha > sqrt(gamma)*(k0-1)/(k0+1),

with the strictness here reflecting the strict bound F>9/16. This is not a condition on possible110 bodies; it is only a test of potential success of the named proof template.

## Exact positive and negative controls

The new source [internal-source-reference] performs complete exact rational calculations for two actual bodies. It derives all true maximal supports from all120 vertex triples, all17 true edges, the actual oriented-boundary uniform moments, and the same moments independently from a positive apex7 tetrahedral fan. It verifies identities(2) as polynomial identities in k, every generated quintic coefficient, all R/A guards, and the full68 primal/polar arrow primitives in a single physical metric and its exact inverse.

Both controls use x=r=p=3/20,q=9/20 and the physical metric

    M=[[5,1,2],[1,3,-1],[2,-1,4]], N=M^-1.

Both are own446physicalweak000, with S={0,1,5,6}, U={1,2,4,8}, H={(0,1),(1,2),(1,8),(2,3),(4,9),(6,7)}. No primitive is zero. Neither is a110 attainer.

### Positive hybrid control, lambda=87/1000

This is exactly the earlier control in [internal-source-reference], not a new body alias. Here the unique canonical global minimizer is the rational primal switching value

    k*=6421797523753550337929956533/40854947291710586982400000000.

The left active pair is basal maximum/true pole1; the right pair is top maximum/true pole1. The maximizing basal vertex is4. Exact one-sided derivative signs are negative and positive. At k*, the radical-free product check proves L<21/2<gamma/(gamma-(251/500)^2), so the canonical family also closes this already accepted control. This does not claim a larger whole-shape region than the preceding fixed-reference box.

### Template-blind control, lambda=3/25

The actual uniform volume and centre are

    Vol=102241/750000,
    g=(184058311/817928000,173571241/817928000,119041/408964).

Take alpha=47/100. The exact smallest R guard is1231953/3271712000>0, the smallest A guard is965911294/679258367>0, and r=5833009/4542127<2. Also alpha>=1-2gamma, alpha^2<gamma, and cos(pi/7)^7<1/2, so the hybrid geometric assumptions hold. The maximum R-admissible alpha is exactly

    alpha_max=145001401/307858325,

again limited by true facet1, basal vertex4, top vertex9. It has alpha_max^2<gamma. The source proves exactly

    gamma/(gamma-alpha_max^2) <421/100,
    (k0+1)^2/(4k0) >109/20,
    (k0+1)^2/(4k0)-gamma/(gamma-alpha_max^2)>5/4.

Thus every SPD auxiliary reference, including arbitrary top-specific choices, fails the specific Gamma-based finite-height product ceiling criterion. Numerical values about4.204 and5.460 merely illustrate the exact rational separation and are not the proof.

For the canonical family, the unique optimum lies strictly inside the basal/pole1 interval and is an admissible quintic root, not a rational switching point. The exact report stores the full six rational coefficients and an80-step rational isolation bracket. The interval begins at42808404204660352665649/301357189233385168000000 and ends at20617693216436557/139769172496000000. The complete exact bracket is generated from those inputs and the specified80 bisections; no floating approximate root is an input. This demonstrates both branches of the exact minimizer method.

## Exact reconstruction and verification capsule

Save these three immutable raw sources with their indicated Python filenames and final LF in a fresh directory:

- [internal-source-reference]: hybrid_exact_region.py,8410B,SHA2564b4d8deb6b3ac50b2f001be38a95fb5da508d7df4cbf70e1bfb2c5a8541f5cbd.
- [internal-source-reference]: hybrid_exact_control.py,5883B,SHA25665f6b996766c4e79ac79d7712c9dc888692654fcf8c0975fd4c2f4cd6407d109.
- [internal-source-reference]: hybrid_reference_frontier.py,10716B,SHA256241807152d6081526098547e5409157104dd593db16909609343464061b4b6a8.

Command:

    python -B -S hybrid_reference_frontier.py HYBRID_REFERENCE_FRONTIER.json

Use CPython3.13.5 standard library with assertions enabled, not -O. It was executed normally and again in a fresh directory containing only these three sources. Both executions regenerated

    HYBRID_REFERENCE_FRONTIER.json,76843B,
    SHA25674f8fc05de61308c30693a0d97dc93ce8aa8ac51950b1b7222831be5fd55eedb.

Expected terminal marker:

    H5_CANONICAL_REFERENCE_IDENTITIES_AND_ALL_REFERENCE_TEMPLATE_BLIND_CONTROL_PASS

The existing exact-region source also contains the rational trigonometric upper checks used in the seven-turn bound, and may be run with its documented command in [internal-source-reference]. The frontier source verifies the lower factor F>9/16 using the Machin identity and alternating rational bounds giving pi<22/7, then cos t>=1-t^2/2. No external solver is used for any exact result here.

## Complete auxiliary scalar locator

This numerical locator helped identify the canonical family controls. Its results are not proof and its failures are not exclusions. It depends on the complete h5_hybrid_explore.py already preserved in [internal-source-reference]; all scientific quantities and exact controls above are regenerated independently by the rational source. Versions: CPython3.13.5,SymPy1.14.0,NumPy2.3.5,SciPy1.17.0. No randomness. Save the following complete source as hybrid_steiner_locator.py,1157B,SHA2564e71eb83a1fdb7aa6263759cc3026bdbc01d19c99473e1998857a2f4585006eb. Run with OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python hybrid_steiner_locator.py. All initial domains and stopping parameters are literal.

```python
"""Deterministic scalar exploration of the canonical top-triangle reference."""
import numpy as np
from scipy.optimize import minimize_scalar
from h5_hybrid_explore import make,stat

def scalars(theta):
 z,v,q,g,S=make(theta,False)
 v=np.array(v,dtype=float)[:,:,0];q=np.array(q,dtype=float)[:,:,0];g=np.array(g,dtype=float)[:,0]
 h=1-g[2];lam=theta[4];m=np.array([lam/3,lam/3])-g[:2]
 D=np.array([[2.,-1.],[-1.,2.]])
 w=v[:,:2]-v[:,2,None]/h*m
 r=np.einsum('ij,jk,ik->i',w,np.linalg.inv(D),w)
 a=(v[:,2]/h)**2
 ell=np.einsum('ij,jk,ik->i',q[:,:2],D,q[:,:2]);b=(q[:,:2]@m+h*q[:,2])**2
 return h,m,r,a,ell,b,2*lam**2/9

def values(t,theta,data):
 h,m,r,a,ell,b,e=data;k=np.exp(t)
 Gamma=(r/k+a).max()*(ell*k+b).max();chi=e/k
 K=max(1,16/27*Gamma*Gamma)
 L=((K+1)*np.sqrt(1+chi)+(K-1)*np.sqrt(chi))**2/(4*K)
 return L,Gamma,k,chi
if __name__=='__main__':
 for lam in [.07,.0825,.087,.09,.1,.12,.15]:
  theta=[.15,.15,.15,.45,lam];data=scalars(theta)
  res=minimize_scalar(lambda t:values(t,theta,data)[0],bounds=(-10,5),method='bounded',options={'xatol':1e-12,'maxiter':1000})
  print(theta,values(res.x,theta,data),'maxRalpha threshold',stat(theta)['need'])
```

## Next scientific frontier

Canonical scale selection is now exact and globally solved within its reference family. Repeating local optimization there is unnecessary. The all-reference negative control shows that a whole-H5 proof cannot come just from improved auxiliary reference selection within the same Gamma-based ceiling. Useful ways past that boundary include a genuinely stronger physical or root-tree spectral restriction, a direct bound on the selected mixed product using additional actual true-arrow inequalities, or a stronger reflection/spoke geometry giving a larger necessary product. The W-only geometric direction and the complete all-root atlas remain complementary, not superseded. The constructive C610 boundary-cancellation direction remains independent and useful.
