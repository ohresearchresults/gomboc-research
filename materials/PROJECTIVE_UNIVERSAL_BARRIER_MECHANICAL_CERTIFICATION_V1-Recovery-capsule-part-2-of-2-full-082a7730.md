# material-082a7730fe9f

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# PROJECTIVE_UNIVERSAL_BARRIER_MECHANICAL_CERTIFICATION_V1
## Recovery capsule part 2 of 2: full proof, scope, exact controls and reconstruction

This coordinator result gives a stronger certified true-centering window and a globally convergent rational rounded Newton procedure for locating the unique projectively centered, uniformly refilled body. It does NOT produce class110, a smaller attaining C, an E17 exclusion, or an incidence-registry change. The accepted interval remains 34 <= C_min <= 622. The present finite controls are actual convex 8/12/6 bodies with exact centered strict counts 6/8/12 and no weak points, not candidates for the minimum.

Part 1 is the complete executable `projective_barrier.py`, material `[internal-source-reference]`, 15986 UTF-8/LF bytes, SHA-256 fae3748c00d735b3e04f019d113d41a1cabc0e6b3785e97998d112a52a104bbe. It needs no parent code, archived arrays, floating solver, network data or local sandbox dependency. This part supplies the analytic argument and exact recovery manifest. BOTH parts constitute the canonical capsule.

## 1. Setup and external analytic premise

Let K be an actual compact full-dimensional convex 3-polytope with 0 in its interior, true vertices x_i and true maximal-facet poles a_f, so a_f.x <= 1 on K. Let M be ONE positive definite metric and N=M^{-1}. For p in

D = {p : 1+p.x_i > 0 for every true vertex i} = int(-K^polar),

put T_p(x)=x/(1+p.x), and REFILL T_pK uniformly. Every denominator is positive throughout K. This positive projectivity preserves the full true face lattice; facet poles become a_f+p. The image's own volume centroid is not T_p applied to the old centroid.

The actual volume potential and its logarithm are

Phi(p)=Vol(T_pK)= integral_K (1+p.x)^(-4) dx,
F(p)=log Phi(p).

A prior result in this branch established the unique minimizer p_* and g(p_*)=0 using actual moments. Its complete canonical source/proof are [internal-source-reference] and [internal-source-reference]. No old code is needed by this capsule. General projective centering is known: Ivan Izmestiev, Fitting centroids by a projective transformation, arXiv:1409.6176v1, Theorem 2 and Section 4, https://arxiv.org/html/1409.6176v1 . It is not claimed as a new theorem here.

The decisive identification is

(D-p)^polar = -T_pK.

Indeed, the closure of D is conv{-a_f}. Translating gives vertices -a_f-p. For each x in K, y=-x/(1+p.x) satisfies y.(-a_f-p)=(a_f.x+p.x)/(1+p.x)<=1. Conversely, the same inequality and the inverse positive projective map recover K. Equivalently, the polar inequalities are precisely the transformed original facet inequalities; full-dimensional polarity makes the equality exact, not an inclusion or a vertex-mass representation.

Thus F is the universal barrier of D. The external analytic premise is Yin Tat Lee and Man-Chung Yue, Universal Barrier Is n-Self-Concordant, arXiv:1809.03011v4, Theorem 2 (definitions in Section 2.1), https://arxiv.org/html/1809.03011v4 . Applied in dimension 3 it says that F blows up at the boundary and satisfies

|D^3F(p)[h,h,h]| <= 2 (h^T H(p) h)^(3/2),
|DF(p)[h]| <= sqrt(3 h^T H(p) h),
H(p)=D^2F(p)>0.

Only this known analytic theorem is imported. The mechanical localization, the explicit rational iteration below, its controls and its exact method-boundary comparison are derived here. No priority assertion is made for generic Newton or self-concordant optimization. Finite code checks cannot prove the external analytic theorem by sampling.

## 2. Actual moments and the Newton decrement

Write g=E_{T_pK}y, W=E_{T_pK}yy^T and Sigma=W-gg^T. Differentiating the actual integral, or composing T_u T_p=T_{p+u}, gives

grad F=-4g,
H=20 Sigma+4gg^T=20W-16gg^T.

Sigma is positive definite for a full-dimensional uniformly filled body, hence so is H. The Newton decrement obeys

lambda^2 = (grad F)^T H^{-1}grad F = 16 g^T H^{-1}g <= 3.

For e^2=g^T W^{-1}g, the rank-one inverse identity also gives

lambda^2 = 4e^2/(5-4e^2).

The denominator is positive since H>0. In particular lambda<1 iff e^2<5/8, and the parameter bound implies e^2<=15/16. These are statements about actual uniform moments, not free moments or extra mechanical assumptions.

F has a unique minimizer: D is bounded, F tends to infinity at its boundary, and H>0. Its stationarity condition is exactly g=0. Thus it gives a single actual centered projective image, not an arbitrary correction of an old center.

## 3. A certified local mechanical window

At any p_0 in D with lambda_0<1,

||p_*-p_0||_{H_0} <= lambda_0/(1-lambda_0).

Here and below ||z||_H^2=z^THz. For completeness, let delta=p_*-p_0 and r=||delta||_{H_0}. Along the actual segment p_0+t delta in D, set q(t)=delta^TH(p_0+t delta)delta. Self-concordance implies |(q^{-1/2})'|<=1, hence q(t)>=r^2/(1+tr)^2. By stationarity at the endpoint,

-grad F(p_0).delta = integral_0^1 q(t) dt >= r^2/(1+r).

Cauchy-Schwarz bounds the left side by lambda_0 r. For r>0 this implies r<=lambda_0/(1-lambda_0); r=0 is trivial. This argument does NOT assume that the entire resulting ellipsoid lies in D. The actual endpoint and its segment are already in D.

Choose a rational upper bound ell with lambda_0^2<=ell^2 and 0<=ell<1, and put R=ell/(1-ell). For an affine row h(p)=a+b.p, if

h(p_0)!=0 and h(p_0)^2 > R^2 b^T H_0^{-1}b,

its sign at p_* is the same as at p_0. This follows directly from the proved displacement bound and dual-norm Cauchy-Schwarz. All quantities in this test are rational when the original geometry, metric and p_0 are rational.

At REFERENCE ZERO the true primal directed-edge escape i->j has positive denominator f_i^2 f_j and numerator a+b.p, where

f_i=1+p.x_i,
a=x_i^T M(x_j-x_i),
b=(x_i^T M x_j)x_i-(x_i^T M x_i)x_j.

For a true dual directed edge f->h, its row is affine without such a denominator:

a=a_f^T N(a_h-a_f),
b=N(a_h-a_f).

All 4E rows use the SAME p, M and reciprocal N. Their reference-zero signs are not the own-centroid mechanics of an arbitrary intermediate image. They ARE the actual own-centroid rows at p_*.

Applying the window to every nonzero row certifies a full strict census at the exact centered image. For strict110 without physical weak points, it is sufficient to certify only the positive rows of a primal spanning tree and its complementary dual spanning tree. These E true edges cover every edge with a positive escape primitive, excluding saddle and weak packets; every nonroot primal vertex and dual facet has a positive escape, so only the two tree roots can be unstable and stable. Actual norm maxima supply those roots. This is the established true-edge mechanics criterion, not a triangulation-edge argument. Harmless unselected zero primitives need not be ruled out. No claim is made that arbitrary desired positive trees exist or can be made positive by centering.

## 4. Global rational quarter-Newton and controlled dyadic rounding

Let d=-H^{-1}grad F=4H^{-1}g. The ideal quarter-Newton iterate is p+d/4=p+H^{-1}g. Its H-displacement has norm lambda/4<=sqrt(3)/4<7/16.

The elementary self-concordant upper bound is, for ||h||_H=r<1,

F(p+h) <= F(p)+grad F(p).h+omega_*(r),
omega_*(r)=-r-log(1-r) <= r^2/[2(1-r)].

For clarity, these standard consequences require no further external hypothesis. Along h, |(q^{-1/2})'|<=1 also gives q(t)<=r^2/(1-tr)^2 before any boundary. Integrating twice gives omega_*. If the ray met the boundary before t=1 while r<1, this finite upper bound would contradict the barrier blowup. Thus the H-unit Dikin ellipsoid is inside D.

With no rounding, the quarter step therefore stays inside D and decreases F by at least 7 lambda^2/36. More usefully, choose a rational q and let

e=q-(p+H^{-1}g),       e^T H e <= lambda^2/4096.

Then for h=q-p,

||h||_H <= (1/4+1/64)lambda = 17lambda/64 < 119/256 <1,
grad F(p).h <= -lambda^2/4 + lambda*lambda/64 = -15lambda^2/64.

The upper remainder is at most

(17lambda/64)^2 / [2(1-119/256)] = 289lambda^2/4384.

Consequently

F(q) <= F(p) - (1477/8768)lambda^2 < F(p)-lambda^2/6.

The final strict comparison uses 1477/8768-1/6=47/26304>0. Every accepted rounded step remains in D; the theorem is not conditional on a successful numerical line search.

A fully specified rational rounding rule is to take k=0,1,2,... in order and floor each component of p+H^{-1}g to a multiple of 2^{-k}, accepting the FIRST k for which the displayed exact H-error test passes. For lambda>0 the loop terminates because the dyadic rounding error tends to zero. If lambda=0, p=p_* and no step is needed. This rounding rule and every nondefault constant are in the source.

Starting at any rational p_0 in D for any actual rational polytope, all iterates are rational. Their F-values decrease, so they lie in a compact interior sublevel of F. Summing the uniform decrement yields sum lambda_k^2<infinity, hence lambda_k->0. Compactness and positive definiteness on that sublevel imply every cluster point is stationary. Uniqueness of p_* then gives p_k->p_*.

This is also a finite-certificate completeness statement for any fixed FINITE set of rows which are strict at p_*. Eventually lambda<=1/2. Choose ell among 1/2,1/4,1/8,... as the smallest such dyadic upper bound still at least lambda (the source halves while lambda^2<=(ell/2)^2). Then ell<=2lambda, except for the irrelevant equality convention, so R->0. The row values converge to their nonzero values at p_*, and the dual norms stay bounded. Every selected row window therefore passes after finitely many steps. Zero rows at the exact endpoint can prevent an all-row strict certificate; a positive selected tree pair can avoid harmless zeros. The method does not force class110 and a failed early window is not an exclusion.

No polynomial bit-complexity, uniform running-time bound, or proof-assistant formalization is asserted. The exact moment and matrix computations are finite on a polytope; the analytic convergence is separate from the two finite tests below.

## 5. Strict strengthening over the previous radial window

Take the actual rational box K=[-1,3/2]x[-1,1]^2 with M=N=I. It has eight true vertices, twelve true edges and six maximal quadrilateral facets, not a triangulated hull. At p_0=0,

Vol=10,
g=(1/4,0,0),
W=diag(7/12,1/3,1/3),
H=diag(32/3,20/3,20/3),
lambda^2=3/32.

Choose ell=5/16 and R=5/11. All 48 affine true-edge rows are negative and pass the new strict window. The minimum squared row margin is 12383/78408>0. Thus the exact, generally irrational, centered projective image has strict S/U/H=6/8/12 and weak000. It is NOT class110.

The previous sufficient window from the canonical branch result used raw W and required

5R_old/(1+R_old Lbar)^6 > e,
R_old Lbar<1,
Lbar>=L=max_i sqrt(x_i^T W^{-1}x_i).

This old condition fails for EVERY radius and every admissible upper bound, not merely one attempted parameter. Indeed, max_{u>0} 5u/(1+u)^6=(5/6)^6, attained at u=1/5. Hence a necessary condition for any old window is e^2 L^2<(5/6)^12. Here e^2=3/28, L^2=69/7 and

e^2 L^2-(5/6)^12 = 100685595263/106662334464 >0.

The new control therefore demonstrates a genuine larger certified centering domain, rather than a reparametrization of a known passing control.

## 6. Executed genuinely three-dimensional rational continuations

The following controls use the same original boxes and the identity metric throughout. At each iterate the source reconstructs all actual maximal facets and true edges and computes positive origin-fan moments, then checks the exact rounding norm, positive denominators and the additional rational descent inequality

Phi(q)*(1+lambda^2/6) < Phi(p).

This latter comparison is directly rational and is asserted for every actual executed step. No logarithm is evaluated by the verifier.

### Control A

Original a=3/2 and p_0=(4/5,1/100,-1/200). The initial Newton decrement squared is

244948756680840120133222775857743522116746037 /
84909895133083780333007976814952789226499328 >1.

Thus the initial local lambda<1 window is unavailable. Twelve rounded quarter steps suffice to certify all 48 rows at p_*.

Rounding bits in order:
[11,11,11,11,12,11,11,11,11,12,13,12].

Terminal rational p=(325/2048,-1/2048,-1/2048), ell=1/4, R=1/3. Its exact lambda^2 is

3171649999313203135350529970093806700007 /
60460501778309043835803583227626098203280.

Initially the REFERENCE-ZERO strict census is 6/4/8, while that same intermediate image at its actual OWN centroid is 6/8/12. At the terminal rational iterate both separately checked censuses are 6/8/12 with no zeros or weak points. The window proves the same strict 6/8/12 at the EXACT p_*, not just at the rational iterate.

### Control B

Original a=10 and p_0=(-9/100,1/100,-1/200). The initial lambda^2 is

8918778478600708666414982575657497776 /
2980060504394845321309758761541173153 >1.

Nineteen rounded steps suffice. Their bits are
[13,12,12,12,11,11,11,10,10,10,10,10,11,10,11,12,11,12,12].

Terminal p=(59/256,-1/4096,-1/4096), ell=1/4, R=1/3. Initially the REFERENCE census is 6/8/12 while the actual OWN census is 6/4/8. At the terminal rational iterate the reference and separately refilled own censuses are both 6/8/12weak000. All exact volumes, centroids, Hessians, step margins and final 48 row margins are regenerated in barrier.json.

These two starts are not confined to a symmetry axis. Intermediate mechanics need not be preserved, and the source explicitly records their difference. They establish a usable exact numerical procedure, not a universal mechanical homotopy theorem.

## 7. Exact algebraic descriptions of the centered controls

For the axial boxes, reflection symmetry and uniqueness force p_*=(t_*,0,0). For a>0 put d=a-1, c=a^2-a+1 and U=(1-t)(1+at). Direct integration gives

Phi(t)=4(a+1)*(3+3dt+ct^2)/(3U^3).

Its derivative is 4(a+1)/(3U^4) times

P_a(t)=-6d+(20a-4d^2)t+d(15a-c)t^2+4ac t^3.

For a=3/2 the primitive polynomial is
84t^3+83t^2+232t-24;
for a=10 it is
3640t^3+531t^2-124t-54.

Their leading coefficients are nonzero modulo 11 and 23 respectively, and the exact source checks that neither cubic has a root in its corresponding finite field. Thus both are irreducible over Q. The unique exact centering parameters are irrational algebraic numbers. They are specified exactly as the unique roots in (9/100,1/10) and (1/5,1/3), respectively. Uniqueness throughout the allowed axial domain also follows from F''>0.

The source performs 80 exact rational bisections on each interval. Final brackets are

a=3/2:
[2406873262227884719393779/24178516392292583494123520,
 188036973611553493702639/1888946593147858085478400];

a=10:
[736538754249717806937377/3022314549036572936765440,
 552404065687288355203033/2266735911777429702574080].

The original eight vertices together with the unique-root rule reconstruct each exact centered body independently of any optimizer or originating sandbox. Each rational interval midpoint defines a DIFFERENT body. The source uniformly refills and separately audits those rational midpoint bodies and records their nonzero own-centroid corrections; it does not confuse them with the algebraic centered bodies.

## 8. Exact identity and real-incidence checks

A further control uses a=3/2,
p=(1/5,-1/20,1/30),
M=[[2,1/4,1/5],[1/4,3/2,1/7],[1/5,1/7,1]], N=M^{-1}.

At each actual vertex y, differentiation in parameter direction e_k has velocity -y_k y. Positive-fan differentiation checks dV=-4Vg_k and that differentiation of -4g gives the displayed H. All 48 reference rows are recomputed on the actual projective hull and checked against the affine numerators, including their exact positive f_i^2 f_j factors. All polar facet/vertex incidences in (D-p)^polar=-T_pK and the lambda/e rank-one identity are checked exactly.

For every finite body control, all triples of the eight actual vertices are reenumerated as possible supporting planes. The resulting maximal facets, their strict off-facet supports, cyclic convexity, all true edges, two-facet incidence per edge and Euler relation are checked independently of declared triangle fans. Moments use only actual positive tetrahedral fan volumes. Triangulation diagonals are never counted as mechanical edges. The centroid-dependent pole rescaling is computed from the actual own centroid for every separately reported own census.

## 9. Scope and next connection to minimum search

The theorem supplies a rigorous centering oracle and terminal sign certificate for a rational candidate shape. It makes a failed small radial window unnecessary as a stopping rule. It does not establish that the unique centered image lies in a desired 110 chamber, and it does not bound all simultaneous metrics or shape parameters. The all-row oracle can legitimately stall on a terminal zero; that is not proof of a weak physical point, because unselected zeros can be harmless.

In particular, if K is already centered at the chosen reference origin, p_*=0. Applying T_q and then applying the unique origin-fixing projective centering correction merely undoes q. This is not an independent way to move the centroid while retaining a centered shape. A useful compression application must first change the actual body, its chosen reference point, or an additional genuine shape variable. At fixed M the endpoint chamber then has to be checked. Actual edge or facet merging remains separate from projective lattice preservation.

This connects to the canonical C622 reduction and the lower-incidence searches only as a new tool. No deleted-vertex or cut child of C622 has yet been run through this new oracle in this result. No weakened equilibrium definition, transported density or independent primal/dual metric is permitted.

## 10. Complete reconstruction and verification

Executed environment: CPython 3.11.8, standard library only, assertions enabled. Exact arithmetic uses fractions.Fraction. There is no random input. No SymPy, NumPy, SciPy, BLAS or external package is used by the canonical code. Save the exact Part 1 text as projective_barrier.py and run

```sh
python -S projective_barrier.py build --output barrier.json
python -S projective_barrier.py check --input barrier.json
```

Expected file identities:

projective_barrier.py: 15986 bytes,
SHA-256 fae3748c00d735b3e04f019d113d41a1cabc0e6b3785e97998d112a52a104bbe;

barrier.json: 99836 bytes,
SHA-256 0b885970a917583ad33df5180f5253267c48f98a777deeb54c49d4f76a481689.

Expected build markers:

```text
PROJECTIVE_BARRIER_BUILD_OK 99836 0b885970a917583ad33df5180f5253267c48f98a777deeb54c49d4f76a481689
PROJECTIVE_UNIVERSAL_BARRIER_MECHANICAL_CERTIFICATION_PASS
```

Check prints the same first marker with CHECK instead of BUILD, then the same final marker. Original build/check and a cold fresh-directory source-only `python -S` build/check actually completed; generated outputs were byte-identical. The stored Part 1 receipt has exactly the source hash and byte count above. Earlier development variants of this local source/output are superseded; they were not promoted as canonical material.

The output itself is supplementary, because the complete exact source, geometry, start parameters, dyadic rounding rule, fixed constants, precision, 80-step algebraic root isolation and checks reconstruct every byte. No table or coordinate row is omitted by an ellipsis.

## 11. Optional exploratory locator, explicitly NONPROOF

The following full 958-byte probe, SHA-256 feaf68fff331067414a643e48b9c1fd79038eacc822e27941ba95e054d80b844, used NumPy 2.3.5 to locate a simple rational box for the method comparison. It scans the literal finite list and is not used by either proof or exact recovery. Its observations were replaced by the exact checks above. This is the full reusable exploratory source, not a claimed exclusion from optimizer failure.

```python
import numpy as np
from itertools import product
for a in [1.1,1.2,1.3,1.4,1.5,1.75,2,3,10]:
 g=np.array([(a-1)/2,0,0]);W=np.diag([(a*a-a+1)/3,1/3,1/3]);H=20*W-16*np.outer(g,g)
 vi=np.array(list(product([-1,a],[-1,1],[-1,1])))
 e2=g@np.linalg.solve(W,g);L2=max(x@np.linalg.solve(W,x) for x in vi)
 lam2=16*g@np.linalg.solve(H,g); rr=(np.sqrt(lam2)/(1-np.sqrt(lam2))) if lam2<1 else np.inf
 # All true primal/dual affine rows with identity M, N
 poles=np.array([[-1,0,0],[1/a,0,0],[0,-1,0],[0,1,0],[0,0,-1],[0,0,1]])
 rows=[]
 for i,x in enumerate(vi):
  for j,y in enumerate(vi):
   if np.count_nonzero(x!=y)==1:
    aa=x@(y-x);bb=(x@y)*x-(x@x)*y
    rows.append((aa,bb))
 for f,x in enumerate(poles):
  for h,y in enumerate(poles):
   if f//2!=h//2:
    rows.append((x@(y-x),y-x))
 margins=[aa*aa-rr*rr*bb@np.linalg.solve(H,bb) for aa,bb in rows]
 print(a,'oldfail',e2*L2>=(5/6)**12,'eL',np.sqrt(e2*L2),'lam',np.sqrt(lam2),'R',rr,'new_margin',min(margins))
```
