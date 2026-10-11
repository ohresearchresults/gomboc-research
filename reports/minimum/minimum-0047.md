# minimum-0047

Historical AI scientific report · saved 2026-09-11 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

**FACET_EDGE_MOMENT_OBSTRUCTION_V1 — completed research handoff.**

The new result is a physical obstruction, not an F>=10 theorem: **the journaled global quadratic facet conditions do not force the facet matrices to be the actual uniform-area moments, even for a genuine nine-facet body with the true volume centroid, true volume covariance, one actual Lambda, correct rank and kernels, complete incidences, and facet-supported completely positive representing measures.** I give an exact nine-facet/fourteen-vertex countercontrol, then an exact shared-edge identity that rejects every altered facet matrix in it. The edge identity reconstructs the actual facet moments from the actual edge geometry. A second result eliminates the quadratic moments to obtain new copositive necessary inequalities on the same actual Lambda.

No remaining tree was closed. No F>=10, C>=34, new whole C32 exclusion, or monostable realization is asserted. The exact unexcluded parent arrays remain:

```text
TREE253 (0,0,1,2,3,4,5,0,7)
TREE266 (0,0,1,2,3,4,5,4,0)
TREE272 (0,0,1,2,3,4,5,5,0)
TREE278 (0,0,1,2,3,4,5,6,0)
TREE285 (0,0,1,2,3,4,5,6,7)
```

These are rooted-tree ordinals, not canonical C32 IDs. I used the literal payload of `minimum-0037`, declared upstream SHA-256 `ae4df745aca2add81c72f0c89bec859bd3af211defc8e00d55b5b5766687b596`, and the journal's QUADRATIC_FACET_TRACE_V1 and FACET_QUADRATIC_FLUX_COUPLING_V1. I did not regenerate the parent's 281 certificates. No array or incidence-label conflict was found. A byte-level provenance caveat is reported after the recovery capsule.

**Continuous scope and notation.** All theorems below concern any compact full-dimensional convex three-polytope P, with all maximal facets retained, at its original homogeneous body's own ordinary volume centroid 0. Write P={x:q_i^T x<=1}, V=Vol(P), Q with rows q_i^T, Y(x)=1-Qx, and let Sigma=E_P(xx^T) be the actual volume covariance. The polar is not assumed volume-centred. Let F_i have actual area A_i, area centroid c_i, and area covariance S_i. Define

```text
d_i=A_i/(V ||q_i||),  omega_i=d_i/3,
lambda_i=Lambda[:,i]=d_i E_Fi Y,
K_i=d_i E_Fi(YY^T),  J=11^T,  H=J+Q Sigma Q^T.
```

All expectations defining these objects are genuine uniform measures. Mechanical shadows always use one reciprocal pair M>0, N=M^(-1), G=Q N Q^T. There is no condition-number bound, coordinate box, positive lower bound on cone or edge volumes, simplicity assumption, or restriction to nine vertices. The identities include all weak-shadow equality strata.

For reference, coning and divergence give sum omega=1, sum omega_i q_i=0, sum omega_i c_i=0, 3 sum omega_i c_i q_i^T=I, and

```text
sum_i K_i=5H-2J,
sum_i (q_i)_k K_i=-(q^(k)1^T+1(q^(k))^T),
K_i omega=lambda_i,  omega^T K_i omega=d_i,
Lambda^2+Lambda=4*1*d^T.
```

For the quadratic identities, apply divergence to x*y_a*y_b and coordinate derivatives of y_a*y_b; their divergences are 5*y_a*y_b-y_a-y_b and -q_a[k]*y_b-q_b[k]*y_a. Own-volume centring gives E_P y_a=1. This explains where the actual common Sigma enters.

**Theorem 1: sharp actual polygon moment bounds.** If t is nonconstant affine on a positive-area convex polygon, min t=0, max t=T, m=E t, then

```text
T/3 <= m <= 2T/3,
(9m^2-3Tm+T^2)/6 <= E(t^2) <= Tm-T^2/6,
(9/8)m^2 <= E(t^2) <= (3/2)m^2.
```

If the zero set is a genuine positive-length edge, the last lower inequality is strict. The upper equality occurs precisely for a triangle with t zero on its base; the lower equality occurs for a triangle with t zero at its opposite vertex and maximal on its base. For a genuine zero edge, 9/8 remains a sharp infimum, approached by truncating that zero vertex with an arbitrarily short edge. For arbitrary nonnegative affine f, including positive minimum, E(f^2)<=(3/2)(E f)^2.

Proof: the parallel slice-length density w(t) is nonnegative, concave, and piecewise affine. If kappa_u=w'_-(u)-w'_+(u)>=0 at each interior breakpoint, then exactly

```text
w(t)=w(0)(1-t/T)+w(T)t/T
     +sum_u kappa_u min(t(T-u)/T, u(T-t)/T).
```

Both sides have the same endpoints and slope jumps. Normalize the summands by their masses. They are triangular probability laws on [0,T] with mode u, including endpoint modes, and moments (T+u)/3 and (T^2+Tu+u^2)/6. If U is the resulting random mode, then m=(T+E U)/3 and E(t^2)=(T^2+T E U+E U^2)/6. The inequalities (E U)^2<=E U^2<=T E U give the range-dependent bounds. The gaps to 9m^2/8 and 3m^2/2 are respectively (3/8)(m-2T/3)^2 and (3/2)(m-T/3)^2. Equality forces the indicated endpoint mode. Affine slice width forces both polygon boundary graphs to be affine, yielding the stated triangles. A zero edge gives w(0)>0, ruling out the lower equality. Finally subtract min f; its variance is unchanged and is at most half the square of the smaller mean. This proves the general upper bound without importing a localization or Berwald theorem.

Consequently, for every actual adjacent pair i,j,

```text
9*Lambda_ji^2/(8*d_i) < K_i[j,j] <= 3*Lambda_ji^2/(2*d_i).
```

For D_i=lambda_i lambda_i^T/d_i,

```text
K_i-D_i is PSD,
z^T K_i z <= (3/2) z^T D_i z for every z>=0.
```

The upper inequality is copositive, not a PSD upper bound. It also gives the actual covariance ellipse c_i+sqrt(2)*S_i^(1/2)B_2 contained in F_i. Thus a selected weak escape i->j, whose perpendicular foot o_i=Nq_i/G_ii satisfies 1-q_j^T o_i<=0, obeys

```text
(o_i-c_i)^T S_i^+ (o_i-c_i)
 >= (Lambda_ji/d_i - (1-G_ij/G_ii))^2
    / (K_i[j,j]/d_i-(Lambda_ji/d_i)^2)
 >= 2.
```

Here the inverse is on the facet tangent plane. The first inequality is covariance Cauchy-Schwarz and the second uses the upper moment bound. Strict escape makes the last inequality strict. No summable nine-facet bound is inferred from this individual test.

**Theorem 2: eliminate Sigma and all K_i to obtain a coupled Lambda obstruction.** For every facet a, set

```text
t_ia=Lambda_ia-d_a,
B_a=2*d_a*J-lambda_a*1^T-1*lambda_a^T,
D_i=lambda_i*lambda_i^T/d_i,
t^+=max(t,0), t^-=max(-t,0).
```

Then both matrices

```text
U_a=sum_i (t_ia+t_ia^+/2)*D_i-B_a,
L_a=B_a-sum_i (t_ia-t_ia^-/2)*D_i
```

are copositive: z^T U_a z>=0 and z^T L_a z>=0 for all z>=0. These are necessary inequalities on one actual Lambda; PSD is not asserted.

Proof: Lambda_ia=d_a(1-q_i^T c_a) and the global coordinate flux give

```text
sum_i Lambda_ia*K_i+lambda_a*1^T+1*lambda_a^T=5*d_a*H.
```

Subtract d_a sum K_i to get the exact covariance-eliminated identity sum_i t_ia K_i=B_a. Write V_i=K_i-D_i=d_i Q S_i Q^T. For every z>=0, 0<=z^T V_i z<=z^T D_i z/2 by Theorem 1. Multiplying by t_ia with its sign retained and summing proves both formulas. All t_ia=0 strata remain covered continuously.

These conditions are explicit from Lambda alone: s_i=(Lambda^2)_ii=4d_i>0, so recover d_i=s_i/4. For a scalar form put m_bi=Lambda_bi^2/d_i. Then

```text
sum_i(t_ia-t_ia^-/2)*m_bi
 <= 2*(d_a-Lambda_ba)
 <= sum_i(t_ia+t_ia^+/2)*m_bi.
```

Genuine adjacency sharpens this. Set ell_bi=9/8 when F_i and F_b share an actual edge, and ell_bi=1 otherwise. Then

```text
sum_i(t_ia^+*ell_bi-(3/2)*t_ia^-)*m_bi
 <= 2*(d_a-Lambda_ba)
 <= sum_i((3/2)*t_ia^+-ell_bi*t_ia^-)*m_bi.
```

The left inequality is strict if some adjacent i,b has t_ia>0; the right is strict if some adjacent i,b has t_ia<0. At t_ia=0 there is no asserted strict contribution. In the particularly simple case b=a, put u_ia=4Lambda_ia-s_a. The weaker incidence-free pair becomes

```text
sum_i(2u_ia-u_ia^-)*Lambda_ai^2/s_i
 <= s_a
 <= sum_i(2u_ia+u_ia^+)*Lambda_ai^2/s_i.
```

On a fixed reciprocal sign stratum, multiplying by product_i s_i>0 gives denominator-free polynomial inequalities. For two-coordinate copositivity tests, a symmetric block [[u,v],[v,w]] is copositive exactly when u,w>=0 and v+sqrt(uw)>=0; for v<0 the last condition is v^2<=uw. Thus rational negative vectors or failed diagonal/two-coordinate tests provide small exact obstruction certificates. I have not established that these constraints alone eliminate a surviving tree or are independent of every previous relaxation.

**Theorem 3: actual shared-edge moments reconstruct the actual facet moments.** For every genuine edge ij, take its actual endpoints x^-,x^+ and their common vertex slack vectors u=Y(x^-), v=Y(x^+). These same vertex vectors must occur on every incident edge. Write x^+-x^-=tau_ij(q_i cross q_j), and define

```text
eta_ij=abs(tau_ij)/V,
e_ij=eta_ij*(u+v)/2,
W_ij=eta_ij*(2uu^T+uv^T+vu^T+2vv^T)/6.
```

They are shared under ij<->ji. The weights are actual geometric quantities. Equivalently,

```text
eta_ij=length_M(E_ij)/(V_M*sqrt(G_ii*G_jj-G_ij^2)).
```

To check metric independence, for c=q_i cross q_j use length_M=abs(tau)*sqrt(c^T M c), V_M=sqrt(det M)*V, and G_ii G_jj-G_ij^2=(c^T M c)/det M. The metric factors cancel.

Uniform interval integration gives exactly

```text
W_ij*omega=e_ij,  omega^T W_ij omega=eta_ij,
W_ij-e_ij e_ij^T/eta_ij=eta_ij*(u-v)(u-v)^T/12.
```

The last matrix has rank one and W_ij has rank two. Their zeros retain all genuine endpoint incidences, including nonsimple vertices. If facet a contains exactly one endpoint, W_ij[a,a]=4e_ij[a]^2/(3eta_ij); if a,b contain opposite endpoints, W_ij[a,b]=2e_ij[a]e_ij[b]/(3eta_ij).

For any z_i on q_i^T z_i=1, write s_i=Y(z_i). Then the exact local equations are

```text
sum_(j~i) s_i[j]*eta_ij = 2*d_i,
sum_(j~i) s_i[j]*e_ij = 3*lambda_i-d_i*s_i,
sum_(j~i) s_i[j]*W_ij = 4*K_i-s_i*lambda_i^T-lambda_i*s_i^T.
```

All sums run over actual edges. Proof: intrinsic divergence on F_i gives

```text
div_Fi((x-z_i)*y_a*y_b)=4*y_a*y_b-s_i[a]*y_b-s_i[b]*y_a.
```

On edge ij, the outward conormal flux of x-z_i is s_i[j]/sqrt(G_jj-G_ij^2/G_ii). Divide the boundary integral by V_M sqrt(G_ii). The coefficient becomes exactly eta_ij s_i[j]. Constant and linear divergence, or contractions by omega, prove the other two equations. The reference point may lie outside the polygon; no positivity of s_i is assumed.

Combining the radial identities for all reference points gives the useful metric-free vector equations

```text
sum_(j~i)(q_i-q_j)*eta_ij = 2*d_i*q_i,
sum_(j~i)(q_i-q_j)*e_ij[a]
 = 3*q_i*Lambda_ai+(q_a-q_i)*d_i,
sum_(j~i)(q_i-q_j)*W_ij[a,b]
 = 4*q_i*K_i[a,b]+(q_a-q_i)*Lambda_bi+(q_b-q_i)*Lambda_ai.
```

Dotting with any z_i in the supporting plane proves these vector equalities from the radial form, since the linear span of that affine plane is all of R^3. Varying an auxiliary metric only repackages radial plus tangential flux; it is not an additional mechanical metric. For the single physical foot z_i=Nq_i/G_ii, s_i[j]<=0 is precisely the parent's weak escape i->j. Zero coefficients do not authorize deleting that edge or its endpoint incidences.

Taking z_i=c_i yields the positive identity

```text
sum_(j~i) (Lambda_ji/d_i)*W_ij=4*K_i-2*lambda_i*lambda_i^T/d_i.
```

For D=diag(d_i), summing and using the body's common covariance gives

```text
5H-2J = (1/2)*Lambda*D^(-1)*Lambda^T
       +(1/4)*sum_(true unordered edges ij)
        (Lambda_ji/d_i+Lambda_ij/d_j)*W_ij.
```

At fixed genuine geometry, actual eta and endpoints determine W and e. The three radial equations then reconstruct d, lambda, and K successively, with divisors 2,3,4. Hence replacing K_i by K_i+Delta K_i while retaining actual means and actual edge data creates the exact quadratic residual 4Delta K_i. This forces the actual first two facet-area moments; it does not claim that first two moments uniquely determine a representing measure. If eta, endpoint vectors, or edge blocks are instead fitted independently, the construction is again only a relaxation.

There is also an exact strict common-covariance bound. Put P_q=sum_i omega_i q_i q_i^T and R_i=c_i-P_q^(-1)q_i/3. Then

```text
15*Sigma-P_q^(-1)=9*sum_i omega_i*(R_i R_i^T+S_i) > 0.
```

Indeed, actual coning gives Sigma=(3/5)sum omega_i(c_i c_i^T+S_i), while sum omega_i c_i q_i^T=I/3 expands the R_i square. Strictness follows because every omega_i is positive, ker S_i=span(q_i), and the poles span R^3. No quantitative gap uniform over nine-facet shapes was obtained.

**Exact nine-facet countercontrol and observed obstruction.** Let t be the root

```text
t^3+t^2-2t-1=0,
1246979603717467/10^15 < t < 1246979603717468/10^15.
b=1-t^2/4, a=(2-t)/(3*(2+t)), s=(1+a)/4, delta=a/2.
N2=diag(1,b), N=diag(1,b,1), M=diag(1,1/b,1).
```

Define C_0=1,C_1=t/2 and R_0=0,R_1=1, with each sequence satisfying U_(j+1)=t U_j-U_(j-1). Set q_j=(C_j,R_j,0) for j=0,...,6, q_7=(0,0,1), q_8=(0,0,-1). The body is an affine regular heptagonal prism. Its planar vertices v_j solve q_j.x=q_(j+1).x=1, indices modulo 7; its fourteen vertices are (v_j,+1),(v_j,-1), with incidences {j,j+1,7} and {j,j+1,8}. The source reconstructs and checks every strict nonincidence and all 21 genuine edges.

Its actual centroid is 0 and actual Sigma=diag(s,s*b,1/3), verified by exact polygon integration and the product interval. Its actual d is seven entries 2/7 followed by 1/2,1/2. The actual facet means are c_j=(C_j,bR_j,0), c_7=(0,0,1), c_8=(0,0,-1). Put T_j=N2-c_j[0:2]c_j[0:2]^T. Actual and altered facet covariances are

| Facet | Actual covariance | Altered covariance |
|---|---|---|
| Side j=0,...,6 | diag(a*T_j,1/3) | diag((a/2)*T_j,1/3) |
| Cap 7 or 8 | diag(s*N2,0) | diag((s+a/2)*N2,0) |

Keep the geometry, d, means, actual Lambda, actual volume Sigma and the same reciprocal M,N fixed. The altered covariance matrices have explicit positive measures supported strictly inside the correct facets: on each cap use equal masses at (v_j/sqrt(2),+/-1). On side j set h_j=(v_j-v_(j-1))/2 and use equal masses at the four points

```text
(c_j[0:2]+epsilon*h_j/sqrt(6), eta/sqrt(3)),
epsilon,eta in {-1,+1}.
```

The moment formulas follow immediately; the exact cap vertex-average identity is also checked by the source. Consequently altered K_i are completely positive, have the correct common rank-four ambient slack space and rank-three facet kernels, and have all required strict positive entries. Complete positivity and correct facet support therefore do not remove this gap.

All global quadratic sums survive: the two cap covariance perturbations contribute delta*N2, while seven sides contribute -(2/7)*delta*sum T_j=-delta*N2 because sum T_j=(7/2)N2. Coordinate-weighted changes vanish by the first and third angular harmonic sums; the source checks these tensor equations directly over Q(t). Actual first moments preserve K_i omega=Lambda[:,i], omega^T K_i omega=d_i and the actual Lambda square identity.

The exact execution verifies all entries of (3/2)H-K_i are nonnegative. Since the journaled QUADRATIC_FACET_TRACE_V1 proves c2>=4455/2888>3/2, this passes every journaled c2 cap. It additionally verifies all entries of (3/2)D_i-K_i are nonnegative and all strict adjacent 9/8 diagonal bounds from Theorem 1. Thus even those new planar constraints do not catch this example.

Nevertheless, all nine altered matrices differ from their actual counterparts. The source independently constructs all 21 actual edge weights from endpoint differences and all edge moments from the interval formula. Every actual facet passes the scalar, linear and full vector quadratic edge identities. Every altered facet fails a quadratic identity. For cap 7 and slack coordinate 0, the exact radial residual RHS-LHS is

```text
4*K_7[0,0]-2*Lambda_07-sum_(j~7) W_7j[0,0] = a > 0.
```

The corresponding raw-coordinate second-moment residual on either cap is diag(a,a*b,0). This is a concrete violated physical equation, not just a discrepancy with independently computed area moments.

This control is deliberately outside all five survivor escape strata: G_ii=1 and G_ij<1 for every i!=j, so all nine facets are strictly stable in the displayed physical metric. It neither realizes nor disproves a remaining monostable case. It proves that the proposed inference from global quadratic feasibility to actual facet physicality is false at F=9, including V=14 outside C32.

**Delimited failures and useful continuation.** The planar scalar bound alone does not close the gap, as the exact countercontrol demonstrates. Complete positivity alone does not close it either. No feasibility claim was established for the global quadratic system intersected with any of the five actual weak-escape trees. Numerical non-success is not being promoted to infeasibility.

A naive summation of the individual covariance-ellipse costs is provably unbounded over physical metrics. For the fixed actual cube [-1,1]^3, q_(+/-k)=c_(+/-k)=+/-e_k, d_i=1/2, Sigma=I/3, S_(+/-k)=(I-e_k e_k^T)/3. Use

```text
N_t=[[1,t,0],[t,t^2+1,0],[0,0,1]],
M_t=[[t^2+1,-t,0],[-t,1,0],[0,0,1]]=N_t^(-1).
```

Both are SPD with determinant one. Directly substituting o_i=N_t q_i/(q_i^T N_t q_i) gives rho_(+/-1)=3t^2, rho_(+/-2)=3t^2/(1+t^2)^2, rho_(+/-3)=0 for rho_i=(o_i-c_i)^T S_i^+(o_i-c_i). Therefore sum_i d_i rho_i=3t^2+3t^2/(1+t^2)^2 tends to infinity. This exact failure uses true fixed-body moments; it is neither a nine-facet survivor nor a counterexample to the desired minimum theorem.

The immediate continuation is to combine the Lambda copositive sandwich with the true-edge formulas on the same realization. Use all actual vertex slack vectors consistently across edges, actual eta=abs(tau)/V, the exact rank-one endpoint variance, and the common covariance identity. Once geometry is supplied, eliminate K by the local recurrences instead of optimizing independent facet matrices. In an exact branch certificate the signs of Lambda_ia-d_a give explicit polynomial inequalities, and genuine adjacency supplies the strict 9/8 contributions without dropping zero-shadow strata. All five arrays above remain in scope, for every admissible vertex count; a C32-only test cannot establish the universal F>=10 conclusion.

**Recovery capsule.** The complete source below is the durable exact object `NINE_FACET_SHARED_EDGE_MOMENT_OBSTRUCTION_V2`. It needs no parent coefficient file, catalogue, download, randomness, floating-point calculation, solver, or omitted helper. Save it as `facet_edge_gap.py`, UTF-8/LF, including its final LF, and run `python -S facet_edge_gap.py` with assertions enabled. The observed environment was CPython 3.12.14, Clang 22.1.3, standard library only. The cubic is irreducible over Q by the rational-root test; it is strictly increasing on (1,2), and the displayed rational interval has opposite endpoint signs, so it specifies exactly one embedding. All arithmetic uses three Fraction coefficients in (1,t,t^2); sign assertions use outward rational bounds on that exact interval.

Observed final execution exited 0. The normative pins are:

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| facet_edge_gap.py | 11143 | 011d273634033f6e790e7c5eecfafd66bd05c72045435df1b5c4dc338ae39de7 |
| facet_edge_gap.json | 74882 | e99cc52fb2b2f9213204a691e7f09073d44d6b90adc69a84696ba096bd396acf |
| facet_edge_gap.log | 450 | 3a5e133589a24fdc4ef13a5c5721a4014f0c479c84e38e44abecaec7b614b5b1 |

The exact terminal transcript was:

```text
EXACT_NINE_FACET_TRUE_COVARIANCE_FLUX_GAP_PASS
FACETS_VERTICES_ALL_FAKE_RANKS 9 14 [3, 3, 3, 3, 3, 3, 3, 3, 3]
ALL_21_TRUE_EDGE_SCALAR_LINEAR_QUADRATIC_FLUX_PASS
FAKE_SHARP_PLANAR_MOMENT_BANDS_PASS
FAKE_FACET_LOCAL_FLUX_FAILURES [0, 1, 2, 3, 4, 5, 6, 7, 8]
NO_SURVIVOR_FEASIBILITY_OR_F10_CLAIM
OUTPUT 74882 e99cc52fb2b2f9213204a691e7f09073d44d6b90adc69a84696ba096bd396acf
SOURCE 11143 011d273634033f6e790e7c5eecfafd66bd05c72045435df1b5c4dc338ae39de7
```

The JSON contains every reconstructed pole, vertex, incidence, metric, actual and altered moment matrix, all 21 exact edge blocks, and all detected failures. It is optional: the following complete source reconstructs and verifies all of it.

```python
"""Exact nine-facet flux gap plus true shared-edge audit. CPython 3.12.14.
Parent: minimum-0037
Parent SHA256: ae4df745aca2add81c72f0c89bec859bd3af211defc8e00d55b5b5766687b596
Run: python -S facet_edge_gap.py
No random choices or external inputs. All arrays are reconstructed over Q(t).
"""
from fractions import Fraction as R
from pathlib import Path
import hashlib,json
assert __debug__
LO=R(1246979603717467,10**15)
HI=R(1246979603717468,10**15)
def poly(t): return t**3+t**2-2*t-1
assert poly(LO)<0<poly(HI) and 1<LO<HI<2
class F:
    def __init__(self,x=0):
        self.c=x.c if isinstance(x,F) else tuple(map(R,x)) if isinstance(x,(list,tuple)) else (R(x),R(0),R(0))
        assert len(self.c)==3
    def __add__(self,y):
        y=F(y);return F(tuple(a+b for a,b in zip(self.c,y.c)))
    __radd__=__add__
    def __neg__(self):return F(tuple(-a for a in self.c))
    def __sub__(self,y):return self+-F(y)
    def __rsub__(self,y):return F(y)+-self
    def __mul__(self,y):
        y=F(y);c=[R(0)]*5
        for i,a in enumerate(self.c):
            for j,b in enumerate(y.c):c[i+j]+=a*b
        for k in (4,3):
            z=c[k];c[k]=0;c[k-1]-=z;c[k-2]+=2*z;c[k-3]+=z
        return F(c[:3])
    __rmul__=__mul__
    def inv(self):
        cols=[self*F(tuple(int(i==j) for i in range(3))) for j in range(3)]
        a=[[cols[j].c[i] for j in range(3)]+[R(i==0)] for i in range(3)]
        for j in range(3):
            p=next(i for i in range(j,3) if a[i][j]);a[j],a[p]=a[p],a[j]
            z=a[j][j];a[j]=[x/z for x in a[j]]
            for i in range(3):
                if i!=j:
                    z=a[i][j];a[i]=[x-z*y for x,y in zip(a[i],a[j])]
        return F(tuple(a[i][3] for i in range(3)))
    def __truediv__(self,y):return self*F(y).inv()
    def __rtruediv__(self,y):return F(y)*self.inv()
    def __bool__(self):return any(self.c)
    def __eq__(self,y):return self.c==F(y).c
    def positive(self):
        return sum(c*(LO**i if c>=0 else HI**i) for i,c in enumerate(self.c))>0
Z=F();O=F(1);t=F((0,1,0))
def zeros(n,m):return [[Z for _ in range(m)] for _ in range(n)]
def transpose(a):return list(map(list,zip(*a)))
def mm(a,b):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(a,k):return [[x*k for x in r] for r in a]
def outer(x,y):return [[a*b for b in y] for a in x]
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def rank(a):
    a=[r[:] for r in a];r=0
    for j in range(len(a[0])):
        ids=[i for i in range(r,len(a)) if a[i][j]]
        if not ids:continue
        p=ids[0];a[r],a[p]=a[p],a[r];z=a[r][j];a[r]=[x/z for x in a[r]]
        for i in range(r+1,len(a)):
            z=a[i][j];a[i]=[x-z*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r
def diag(v):return [[v[i] if i==j else Z for j in range(len(v))] for i in range(len(v))]
b=1-t*t/4;a=(2-t)/(3*(2+t));s=(1+a)/4;delta=a/2
assert a.positive() and (F(R(1,3))-a).positive()
assert b.positive() and s.positive()
N=diag([O,b,O]);M=diag([O,1/b,O]);assert mm(N,M)==diag([O,O,O])
C=[O,t/2];S=[Z,O]
for j in range(2,8):C.append(t*C[-1]-C[-2]);S.append(t*S[-1]-S[-2])
assert C[7]==1 and S[7]==0
q=[[C[j],S[j],Z] for j in range(7)]+[[Z,Z,O],[Z,Z,-O]]
G=mm(mm(q,N),transpose(q))
assert all(G[i][i]==1 for i in range(9))
assert all((1-G[i][j]).positive() for i in range(9) for j in range(9) if i!=j)
verts=[]
for j in range(7):
    u=q[j];v=q[(j+1)%7];d=u[0]*v[1]-u[1]*v[0]
    verts.append([(v[1]-u[1])/d,(u[0]-v[0])/d])
area=Z;first=[Z,Z];second=zeros(2,2)
for u,v in zip(verts,verts[1:]+verts[:1]):
    cross=u[0]*v[1]-u[1]*v[0];assert cross.positive();area+=cross/2
    first=[first[k]+cross*(u[k]+v[k])/6 for k in range(2)]
    term=add(scale(add(outer(u,u),outer(v,v)),2),add(outer(u,v),outer(v,u)))
    second=add(second,scale(term,cross/24))
assert area.positive() and first==[Z,Z]
assert scale(second,1/area)==diag([s,s*b])
# Seven contracted vertex atoms v_j/sqrt(2) give each fake cap covariance.
atomic_cap=zeros(2,2)
for v in verts:atomic_cap=add(atomic_cap,scale(outer(v,v),F(R(1,14))))
assert atomic_cap==diag([s+delta,(s+delta)*b])
Sigma=diag([s,s*b,F(R(1,3))])
vertices=[v+[F(z)] for z in (1,-1) for v in verts]
incidences=[]
for v in vertices:
    slack=[1-dot(p,v) for p in q]
    assert all(x==0 or x.positive() for x in slack)
    inc=[i for i,x in enumerate(slack) if x==0];assert len(inc)==3;incidences.append(inc)
d=[F(R(2,7))]*7+[F(R(1,2))]*2
omega=[x/3 for x in d]
means=[];covs=[];truecovs=[]
for j in range(7):
    c=[C[j],b*S[j],Z];means.append(c)
    assert dot(q[j],c)==1
    u=verts[(j-1)%7];v=verts[j]
    assert (u[0]*v[1]-u[1]*v[0])/area==d[j]
    assert [(u[k]+v[k])/2 for k in range(2)]==c[:2]
    T=add(diag([O,b]),scale(outer(c[:2],c[:2]),-1))
    edgecov=scale(outer([v[k]-u[k] for k in range(2)],[v[k]-u[k] for k in range(2)]),F(R(1,12)))
    assert edgecov==scale(T,a)
    fake=zeros(3,3);true=zeros(3,3)
    for k in range(2):
        for l in range(2):fake[k][l]=a*T[k][l]/2;true[k][l]=a*T[k][l]
    fake[2][2]=true[2][2]=F(R(1,3));covs.append(fake);truecovs.append(true)
for z in (1,-1):
    means.append([Z,Z,F(z)]);covs.append(diag([s+delta,(s+delta)*b,Z]));truecovs.append(diag([s,s*b,Z]))
L=[[O]+[-x for x in row] for row in q]
def moment(c,cov):
    B=outer([O]+c,[O]+c)
    for k in range(3):
        for l in range(3):B[k+1][l+1]+=cov[k][l]
    return B
K=[scale(mm(mm(L,moment(c,v)),transpose(L)),di) for c,v,di in zip(means,covs,d)]
Ktrue=[scale(mm(mm(L,moment(c,v)),transpose(L)),di) for c,v,di in zip(means,truecovs,d)]
J=[[O]*9 for _ in range(9)];H=add(J,mm(mm(q,Sigma),transpose(q)))
Lambda=[[d[i]*(1-dot(q[j],means[i])) for i in range(9)] for j in range(9)]
assert rank(L)==4
for i in range(9):
    assert rank(K[i])==3 and all(x==0 for x in K[i][i])
    assert all(K[i][j][k].positive() for j in range(9) for k in range(9) if j!=i and k!=i)
    assert mm(K[i],[[x] for x in omega])==[[Lambda[j][i]] for j in range(9)]
    assert dot(omega,[sum(K[i][j][k]*omega[k] for k in range(9)) for j in range(9)])==d[i]
    assert all(x==0 or x.positive() for j in range(9) for k in range(9) for x in [3*H[j][k]/2-K[i][j][k]])
    assert K[i]!=Ktrue[i]
for family in (K,Ktrue):
    total=zeros(9,9)
    for Ki in family:total=add(total,Ki)
    assert total==add(scale(H,5),scale(J,-2))
    for k in range(3):
        total=zeros(9,9)
        for i in range(9):total=add(total,scale(family[i],q[i][k]))
        assert total==[[-q[j][k]-q[l][k] for l in range(9)] for j in range(9)]
assert all(sum(row)==3 for row in Lambda)
assert all((F(R(10,9))-x).positive() for row in Lambda for x in row)
assert mm(Lambda,q)==scale(q,-1)
assert mm(Lambda,Lambda)==add(scale(outer([O]*9,omega),12),scale(Lambda,-1))
# Cap-facet intrinsic radial quadratic flux with actual edges: 4*Ctrue.
# Actual edge moments equal the integral required by the true uniform area.
# The artificial covariance has residual 4*d_cap*delta*N2 = a*N2.
cap_residual=scale(add(covs[7],scale(truecovs[7],-1)),4*d[7])
assert cap_residual==diag([a,a*b,Z])
# Independent boundary construction: no facet triangulations or fitted edge mass.
edges=[]
for i in range(9):
    for j in range(i+1,9):
        ids=[k for k,inc in enumerate(incidences) if i in inc and j in inc]
        if not ids:continue
        assert len(ids)==2
        u,v=[vertices[k] for k in ids]
        cross=[q[i][1]*q[j][2]-q[i][2]*q[j][1],q[i][2]*q[j][0]-q[i][0]*q[j][2],q[i][0]*q[j][1]-q[i][1]*q[j][0]]
        h=next(k for k in range(3) if cross[k])
        tau=(v[h]-u[h])/cross[h]
        assert [v[k]-u[k] for k in range(3)]==[tau*x for x in cross]
        if not tau.positive():tau=-tau
        assert tau.positive()
        eta=tau/(2*area)
        U=[1-dot(p,u) for p in q];V=[1-dot(p,v) for p in q]
        e=[eta*(x+y)/2 for x,y in zip(U,V)]
        W=scale(add(scale(add(outer(U,U),outer(V,V)),2),add(outer(U,V),outer(V,U))),eta/6)
        assert rank(W)==2
        assert add(W,scale(outer(e,e),-1/eta))==scale(outer([x-y for x,y in zip(U,V)],[x-y for x,y in zip(U,V)]),eta/12)
        edges.append(dict(i=i,j=j,vertices=ids,eta=eta,e=e,W=W))
assert len(edges)==21
# Even the sharp planar moment bands do not detect this counterfeit.
for i in range(9):
    DD=scale(outer([Lambda[r][i] for r in range(9)],[Lambda[r][i] for r in range(9)]),1/d[i])
    assert all(x==0 or x.positive() for row in add(scale(DD,F(R(3,2))),scale(K[i],-1)) for x in row)
    neighbors=[ed['j'] if ed['i']==i else ed['i'] for ed in edges if i in (ed['i'],ed['j'])]
    assert all((K[i][j][j]-F(R(9,8))*DD[j][j]).positive() for j in neighbors)
fake_fail=[]
for i in range(9):
    incident=[(ed,ed['j'] if ed['i']==i else ed['i']) for ed in edges if i in (ed['i'],ed['j'])]
    for k in range(3):
        assert sum((q[i][k]-q[j][k])*ed['eta'] for ed,j in incident)==2*d[i]*q[i][k]
        for r in range(9):
            assert sum((q[i][k]-q[j][k])*ed['e'][r] for ed,j in incident)==3*q[i][k]*Lambda[r][i]-(q[i][k]-q[r][k])*d[i]
    failed=False
    for r in range(9):
        for h in range(9):
            for k in range(3):
                lhs=sum((q[i][k]-q[j][k])*ed['W'][r][h] for ed,j in incident)
                low=(q[i][k]-q[r][k])*Lambda[h][i]+(q[i][k]-q[h][k])*Lambda[r][i]
                assert lhs==4*q[i][k]*Ktrue[i][r][h]-low
                failed=failed or lhs!=4*q[i][k]*K[i][r][h]-low
    if failed:fake_fail.append(i)
assert fake_fail==list(range(9))
cap_lhs=sum(ed['W'][0][0] for ed in edges if 7 in (ed['i'],ed['j']))
assert 4*K[7][0][0]-2*Lambda[0][7]-cap_lhs==a
def enc(x):
    if isinstance(x,F):return [str(z) for z in x.c]
    if isinstance(x,list):return [enc(z) for z in x]
    if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
    return x
out=dict(identity='NINE_FACET_SHARED_EDGE_MOMENT_OBSTRUCTION_V2',field='t^3+t^2-2t-1=0;1246979603717467/10^15<t<1246979603717468/10^15',
         parent='minimum-0037',parent_sha256='ae4df745aca2add81c72f0c89bec859bd3af211defc8e00d55b5b5766687b596',
         q=q,vertices=vertices,incidences=incidences,N=N,M=M,Sigma=Sigma,d=d,omega=omega,Lambda=Lambda,
         facet_means=means,fake_facet_covariances=covs,true_facet_covariances=truecovs,K=K,Ktrue=Ktrue,H=H,cap_edge_flux_residual=cap_residual,edges=edges,fake_local_flux_failures=fake_fail,
         scope='Relaxation gap only: actual9-facet prism, actualSigma and Lambda, fake supported facet measures. No monostability or surviving-tree feasibility claim.')
payload=(json.dumps(enc(out),sort_keys=True,separators=(',',':'))+'\n').encode('ascii')
Path('facet_edge_gap.json').write_bytes(payload)
print('EXACT_NINE_FACET_TRUE_COVARIANCE_FLUX_GAP_PASS')
print('FACETS_VERTICES_ALL_FAKE_RANKS',9,14,[rank(Ki) for Ki in K])
print('ALL_21_TRUE_EDGE_SCALAR_LINEAR_QUADRATIC_FLUX_PASS')
print('FAKE_SHARP_PLANAR_MOMENT_BANDS_PASS')
print('FAKE_FACET_LOCAL_FLUX_FAILURES',fake_fail)
print('NO_SURVIVOR_FEASIBILITY_OR_F10_CLAIM')
print('OUTPUT',len(payload),hashlib.sha256(payload).hexdigest())
source=Path(__file__).read_bytes();print('SOURCE',len(source),hashlib.sha256(source).hexdigest())
```

**Parent provenance caveat.** The attachment header declares the upstream immutable SHA `ae4df745aca2add81c72f0c89bec859bd3af211defc8e00d55b5b5766687b596`. Extracting the rendered attachment suffix from its literal `# NOVA24_CAP9_NEW_281_RESTORED_V1` heading through EOF instead yields **45130 bytes**, SHA-256 `b977739c35bb336dfbac45323c75e6a5070cfd23d083ffd13c74823771ec3b03`. These are different byte identities; I cannot certify the upstream payload hash from that rendered suffix. The five embedded Python source units do match their individually published length/SHA pins. This is a reported rendering/provenance discrepancy, not an invented replacement parent or an array conflict. The new reconstruction above requires only its own literal inputs; the upstream SHA is recorded as parent identity, not asserted as the hash of this attachment extraction.

The complete standard-library check for that observation is below. Run it with the exact attached input: `python -S provenance_check.py 'upload/research-journal(20260911-084328).md'`.

```python
from pathlib import Path
import hashlib,re,sys
raw=Path(sys.argv[1]).read_bytes()
start=raw.index(b'# Immutable parent result payloads')
p=raw[raw.index(b'# NOVA24_CAP9_NEW_281_RESTORED_V1',start):]
assert len(p)==45130
assert hashlib.sha256(p).hexdigest()=='b977739c35bb336dfbac45323c75e6a5070cfd23d083ffd13c74823771ec3b03'
expected={
'engine.py':(3924,'382527ea22bb7a02d448ac2eb1f9c1b5785f15384df6c9248f1639714b87ab00'),
'build.py':(2924,'7ee0832cf805272cc47e587dff7a8710250eef481b7a5ca55af9e36633dcec78'),
'verify.py':(5792,'c572e6bb3ff4ef19db498b436972f4304229ab3f26562a74a179765519bea8f9'),
'frames.py':(4681,'c4389bb0b7e05e0c0294f1214fe29eb8b913c6fadd94d902681c9c52795e4158'),
'replay.py':(3114,'93968859a1d831acf122fb7291639787061f32044c6e718aefa8a67f6b5dddc3')}
for name,want in expected.items():
    pattern=rb'### 7\.\d `'+re.escape(name.encode())+rb'`\n\n```python\n(.*?)```'
    b=re.search(pattern,p,re.S).group(1)
    assert (len(b),hashlib.sha256(b).hexdigest())==want
print('ATTACHMENT_RENDERED_SUFFIX_AND_FIVE_SOURCE_PINS_PASS')
```
