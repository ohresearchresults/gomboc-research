# minimum-0127

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# BEVEL_JOINT_QUANTIFIED_HORIZON_V1

## Main result

For the literal bevel B=P(1/4,1/4,2,3), define ell_i(p)=1+p·X_i and D={p:ell_i(p)>0 for all ten vertices}. There is now an explicit cutoff:

```
K   = 184025088000000000
eta = 2^(-184025088000000002) = 2^(-K-2).
```

Every uniformly refilled positive projective image of this B that has exactly one strict stable facet and one strict unstable vertex, under one positive-definite M and its actual inverse N, satisfies **ell_i(p)>eta for every i**. Equivalently,

```
J(B) ⊂ (1-eta)D.
```

Thus the entire closed horizon collar {p in D:min ell_i(p)<=eta}, in every projective direction and at every metric, is excluded for the **joint** condition. Additional physical weak equilibria are allowed in this statement. This is a quantitative consequence of the supplied properness theorem, not a new exclusion of the full orbit, not U>=2 throughout D, and not a 110 attainer.

The bound is extremely conservative: its direct numerical pruning power is negligible. Its useful content is that the previous unknown cutoff has been replaced by an exact explicit number and a fully specified compact polynomial feasibility problem. No claim of computational tractability or completed satisfiability decision is made.

With raw-coordinate metric normalization tr M=1, every joint candidate also obeys the independently obtained effective bounds

```
M >= 2^(-184025087999999998) I,
27/20^10 <= sigma <= 2^(184025088000000000),
sigma = 1 / [(product_i(4+4p·X_i)) det M].
```

No metric-conditioning restriction was imposed on the original problem; these are necessary consequences for every candidate.

## 1. Sources and exact input boundary

The entire new journal and its literal parents, and the entire supplied properness proof, were read through EOF. The new journal is 334752 bytes and 2654 lines, SHA-256 546ad7c3bf3cf0d7663e15306683c986e0ba5f38228e19f1acabbc841ef69a0f. The properness upload is 16904 bytes, SHA-256 c1fb348aa34b5357be23eb9c19209c106053f6e38989e0768bb8d39608f7c39e. Unchanged previous evidence was not restarted.

The authoritative body/source parent is minimum-0122, advertised SHA-256 a57548bf7f7db6cdd82467ad12462e1f201c78a3b343270a89caa20f94b4229b. The strict all-pyramid premise is minimum-0022, SHA-256 85b0f28d8e4c53b1e4d13566ebcacb6b1bfcd92547d5524599743dde7534de92. Their accepted results were not routine-reverified. The new executable has no parent-file import or missing checkpoint dependency.

The inherited bridge says that J(B), including candidates with extra weak points, is a compact subset of D. It uses maximum-image-tetrahedron limits, their actual uniformly filled centroids, strict-equilibrium persistence, and the all-pyramid strict conclusion. It supplies no number eta. That qualitative result is the premise used here.

One new external mathematical input is Theorem 1 of Jeronimo, Perrucci and Tsigaridas, *On the minimum of a polynomial function on a basic closed semialgebraic set and applications*, arXiv:1112.0544. Its exact statement was checked in the primary PDF, printed page 2, including a page-image inspection. The theorem and its quantitative formula are stated below. No external archive or research connector was used.

## 2. Actual mass and one reciprocal metric: complete polynomial model

All literal integer vertices U_i=4X_i, the nine true outward maximal facet cycles, and integer-scaled supporting pairs (a_f,b_f) are in the source. The body is the actual 10/17/9 bevel, not a B8 roof. The program reconstructs the maximal supporting facets from all supporting triples and derives only the 17 true edges for mechanics. The 16 facet-fan triangles are used for integration, never as extra equilibrium edges.

Put

```
h_i = 4 + U_i·p = 4 ell_i,
H = product_i h_i,
H_i = product_(j!=i) h_j,
Y_i = U_i/h_i.
```

Here H is a denominator polynomial, not a saddle count. From the true outward origin fan,

```
R = sum_(triangle t) det(U_t) product_(i not in t) h_i,
A = R/8192,
V = 4096 A/(3H).
```

Exact expansion gives the inherited degree-six adjoint: A has 84 nonzero integer coefficients and A(0)=9168. Positivity of the actual fan makes A>0 throughout D. Define

```
C = 4 A H,
G_k = A sum_i U_ik H_i - H ∂_k A,
g = G/C,
Znum_i = 4 A U_i H_i - G.
```

This g is the refilled image's own volume centroid. Indeed the Jacobian is (1+p·x)^(-4), so differentiating its actual volume gives g=-(1/4)grad log V. Equivalently, the displayed formulas are obtained by integrating the actual image tetrahedra. The centered vertex is Z_i=Y_i-g=Znum_i/C. No transported old centroid appears.

Use five free metric entries and define

```
M = ((m11,m12,m13),
     (m12,m22,m23),
     (m13,m23,1-m11-m22)).
```

This fixes tr M=1 without losing any candidate. Starting with M0, the normalization is M=M0/tr M0 and N=(tr M0)M0^(-1), so MN=I remains exact.

For every directed true primal edge i->j, define

```
P_ij = Znum_i^T M (h_i U_j-h_j U_i).
```

Its exact physical meaning is

```
Z_i^T M(Z_j-Z_i) = P_ij/(C h_i h_j).
```

For the true facet a_f·x<=b_f, define

```
n_f = a_f+b_f p,
s_f = b_f C-n_f·G,
q_f = C n_f/s_f.
```

The true centroid is interior, hence s_f>0 throughout D. For each directed true polar edge f->k, define

```
Q_fk = n_f^T adj(M)(s_f n_k-s_k n_f).
```

Then, for the SAME M and N=M^(-1),

```
q_f^T N(q_k-q_f) = C^2 Q_fk / [det(M) s_f^2 s_k].
```

Every denominator in these sign equivalences is strictly positive at a physical point. Using the cofactor matrix rather than separate free entries of N preserves reciprocal coupling while keeping only five metric variables. It does not assign uniform mass or a separate centroid to the polar.

### A basic closed formulation with no spurious horizon points

Add one reciprocal variable sigma and the polynomial equality

```
sigma H det(M)-1=0.
```

Fix a proposed unstable root r and stable root s. At each of the nine primal nonroots choose one true outgoing edge; at each of the eight polar nonroots choose one true outgoing edge. The corresponding branch is defined by exactly:

| Number | Conditions |
|---:|---|
|1|sigma H det(M)-1=0|
|10|h_i>=0|
|7|Every nonempty principal minor of M is nonnegative|
|9|The chosen primal P_ij>=0|
|8|The chosen polar Q_fk>=0|

There are nine real variables: three p coordinates, five metric entries and sigma. The equality and principal-minor constraints force all h_i>0 and M positive definite, despite every defining inequality being closed. Thus algebraically clearing denominators has not admitted a projective-horizon point, a rank-deficient metric, or a zero true-centroid denominator.

A nonroot with a nonnegative outgoing primitive is not strict U. A farthest vertex always is strict U, so the primal conditions force exactly one strict U at r. Applying the same argument to the actual polar with M^(-1) forces exactly one strict S at s. Conversely, every joint candidate supplies such choices of true edges. All zero-arrow walls are retained.

There is no need to impose acyclicity separately: each nonnegative edge strictly increases squared norm by the positive squared edge length, even when its derivative is zero. Nor may one silently require complementary primal and dual trees for this joint-count problem with additional weak points. The implementation keeps the two compatible-by-the-same-metric arrow systems independent combinatorially.

The SMT file uses an OR over roots and, at each nonroot, an OR over its actual neighbors. This compact Boolean organization represents all choices without enumerating a huge list of paired trees. The predicates are exact S=U=1, not the stronger weak000 condition.

## 3. Why the reciprocal-variable branches are compact before any numerical cutoff

Every point of any such branch projects to J(B). By the accepted properness theorem, these p coordinates lie in a compact subset of D. For p in that compact subset, the actual own-centered bodies have uniform positive interior radius and a uniform finite exterior radius. The supplied two-half argument and its application to the actual polar give positive lower bounds on both adjacent eigenvalue ratios for any jointly monostatic metric. With trace one, the least eigenvalue therefore stays uniformly positive.

Consequently H det(M) is bounded away from zero and sigma is bounded above. The p and trace-one metric coordinates are already bounded. Each branch is closed by its polynomial definition, so it is compact; every connected component is compact. This argument uses only an unknown qualitative positive distance supplied by properness. It does NOT assume the explicit eta subsequently derived. Empty branches require no special treatment.

## 4. The explicit arithmetic cutoff

For integer polynomial constraints in n variables, with m defining polynomials of degree at most an even d and coefficient magnitudes at most Bcoef, the cited theorem bounds any nonzero polynomial minimum on a compact connected component below by

```
(2^(4-n/2) Btilde d^n)^(-n 2^n d^n),
Btilde=max(Bcoef,2n+2m),
```

provided the objective has degree at most d and coefficient magnitudes at most Bcoef. No generic critical-point assumption is required.

The new exact expansion divides each nonzero constraint by its positive coefficient gcd. This changes neither its equality nor its inequality. The complete resulting library has **86 polynomials and 750976 nonzero monomials**. Its exact parameters are

```
n=9,
m=35 for every basic branch,
d=20 (even; actual maximum constraint degree is 19),
Bcoef=Btilde=514705477720.
```

The degrees are one for h, at most three for the metric minors, fourteen for the reciprocal-variable equality, seventeen for primal arrows, and nineteen for polar arrows. The height is attained in the primitive s8_3 polynomial by the two terms

```
+514705477720 px^3 py^6 pz^3 m12 m13
-514705477720 px^3 py^6 pz^3 m11 m23.
```

All remaining coefficients are bounded by the same value, as verified by the complete exact expansion, not by coefficient sampling.

The theorem applies on every nonempty branch component to each of the following strictly positive objectives:

```
h_0,...,h_9, det(M), H det(M).
```

The last two have degrees three and thirteen. Their coefficients, and those of the unscaled h_i objectives, also obey the same height bound. The arithmetic is

```
20^9 = 512000000000,
Bcoef*20^9 = 263529204592640000000000 < 2^78,
n*2^n*20^9 = 2359296000000000,
78*(n*2^n*20^9) = 184025088000000000 = K.
```

Since 2^(4-9/2)=1/sqrt(2)<1, each listed objective is strictly greater than 2^(-K). Therefore ell_i=h_i/4>2^(-K-2)=eta. This establishes the full-horizon statement. The same theorem also gives algebraic degree at most 131072000000000 for each such minimum; neither the minimizing points nor their minimal polynomials were computed.

The determinant objective gives a better raw metric bound than simply substituting eta into a geometric radius estimate. With eigenvalues summing to one, lambda1 lambda2<=1/4, hence

```
lambda3 = det(M)/(lambda1 lambda2) > 4*2^(-K)=2^(-(K-2)).
```

The objective H det(M) gives sigma<2^K directly. These are consequences of the same compact-branch argument, not additional imposed hypotheses. The coefficient bound is specific to the literal fixed body; no uniform eta over a changing realization class follows.

### Preserved simpler geometric bound

The exact supporting planes show that the original B contains the Euclidean unit ball, and max_i|X_i|^2=14. Thus D lies in the unit parameter ball. Every P_p contains the ball of radius 1/2: for |y|<=1/2, its inverse x=y/(1-p·y) belongs to the original unit ball. The true centroid depth bound then gives an interior ball of radius 1/4 for EVERY centered P_p throughout D.

When ell_i>=eta, the raw image diameter is at most 8/eta and its own-centered outer radius at most 6/eta. The two-half lemma therefore also yields

```
M > (eta^4/995328) I > 2^(-(4(K+2)+20)) I,  tr M=1.
```

This is weaker than the direct determinant bound, but is a reusable elementary check on the normalization. It does not need a limiting metric or an independently centered polar.

## 5. The precise remaining compact feasibility problem

A whole-orbit joint exclusion is now equivalent to proving that the generated nine-variable polynomial/Boolean system is empty. Its feasible set is contained in the explicitly bounded region

```
||p||<=1,
ell_i(p)>=2^(-K-2),
M>=2^(-(K-2)) I,
tr M=1,
27/20^10 <= sigma <= 2^K.
```

For the last elementary lower bound, h_i<20 follows from ||p||<=1 and |U_i|<=4sqrt(14)<16, and det(M)<=1/27 follows from trace one. The physical problem has only eight independent continuous variables; sigma is uniquely determined. Its purpose is to give an exact basic CLOSED algebraic description without inserting astronomically large expanded integers into the model.

The generated SMT model does not have to encode the dyadic bounds as giant numerals: they have been proved for all of its feasible points. All coefficients in that model are the modest exact integers whose height was audited above. The full model remains equivalent to the original full-D joint question.

Relative to this result plus the named inherited C9 and complete-pencil theorems, the shape region still requiring a decision is contained in

```
[(1-eta) closure(D)] minus
[C9 union {(0,h,0):-1/2<h<1}].
```

For an explicit definition of the inherited cone, put d_f=-a_f/b_f using the literal supports in the source, F9=conv(d_1,d_2,d_6,d_7,d_4), and c9=(-1/30,-16/75,-9/50). Then C9=conv(0,c9+(3/4)(F9-c9)) intersect D. Its all-SPD U2 theorem remains an inherited premise, not a new output of this computation.

This is not a classification of overlaps with every previously excluded affine family. C9 is still only its original cone; no part of its metric/tree certificate is relabelled as an all-D proof. The much larger eleven-dimensional realization-space problem is untouched.

## 6. What was actually executed

Only exact, deterministic standard-library computation was needed. The execution reconstructed the literal maximal hull, expanded all 86 integer polynomials, audited all 750976 coefficients, computed the displayed degree/height/exponent bounds, and generated the complete SMT model. It then used the parent's actual three-parameter control

```
p=(-1/60,-8/75,-9/100),
M=diag(484,1,1)/486,
N=diag(486/484,486,486).
```

Two distinct positive tetrahedral fans independently reproduced its own volume and centroid. Every one of the 34 primal and 34 reciprocal polar polynomial sign identities was checked against actual rational mechanics. All seventeen edge-foot vector identities and the complete strict census were checked:

```
S=[4,5,6], U=[4,9], H-edge IDs=[7,9,11],
strict323, weak000, all 68 edge primitives nonzero.
```

This is the inherited control under a trace-one normalization, not a new attaining construction. Its exact centroid, volume, reciprocal pair, full ledger and all polynomial values are regenerated in joint_controls.json. No unlisted fixture is required.

A separate S-expression evaluator then evaluated the serialized SMT arithmetic exactly at that same rational control. All 86 polynomial values agreed; all eighteen basic positivity/equality assertions passed, while both unique-root predicates correctly failed. This tests serialization and physical interpretation, not global infeasibility.

Cold recovery in a fresh directory containing only joint_bevel.py completed build and check separately. All four output files and both 646-byte transcripts matched byte for byte. **No satisfiability solver, CAD, quantifier elimination, finite metric scan or numerical optimizer was run.** The all-pyramid theorem and analytic properness were accepted premises, not replays or proof-assistant verifications.

## 7. Recovery capsule

The complete source is appended below and is also supplied as joint_bevel.py. It is self-contained except for the explicitly stated mathematical properness and polynomial-minimum premises. Tested interpreter: CPython 3.13.5. There are no third-party Python dependencies, seeds, tolerances, numerical solver parameters or parent imports. Keep assertions enabled; do not use -O.

Run as separate commands in a directory containing only this source:

```sh
python -S joint_bevel.py build
python -S joint_bevel.py check
```

Both commands actually ended with

```
EXACT_FULL_ORBIT_COMMON_METRIC_OWN_CENTROID_POLYNOMIALS_PASS
N_D_M_H 9 20 35 514705477720
ETA_GE_2_TO_MINUS 184025088000000002
TRACE_ONE_RAW_METRIC_GE_2_TO_MINUS 184025087999999998
SATURATION_COORDINATE_LE_2_TO_PLUS 184025088000000000
BEVEL_JOINT_QUANTIFIED_HORIZON_RECOVERY_PASS
```

Exact identities:

| File | Bytes | SHA-256 |
|---|---:|---|
|joint_bevel.py|16510|b41d54ce690bf3b1d81a53aa24817b2514f6098a23c4635ffef59841cd978434|
|joint_polynomials.json|23523048|7849971decfc970f0acd65de82a32cbaa2b0cc1ec226198e66fcd20b4450c166|
|joint_full.smt2|31598981|de8626cb377b54435e097b0920982bc4006d0397adf7d5d164f14cb764389e45|
|joint_controls.json|32261|9f9e9add13c15519b789b9ebdac1fab09a4314242d86508f6ae3fee00a78e61e|
|joint_report.json|7573|72866499a9fe3afd79aa9ceb9cd3cc37233db2d0e97583886f2e8f59d18d1445|
|recovery.stdout|646|3c53a07076e09288586c4c4a24b168465d430cf5bf4ff098cb7ac43ae63b6e91|

The large coefficient and model files are reconstructible in full from the compact source; their hashes are not substitutes for the generator. A solver's later SAT response would certify only joint strict counts after independent exact verification; an actual strict110weak000 claim would additionally require its own complete physical census.

## 8. Most useful continuation and unchanged boundary

The new effectiveness step is complete, but the interior decision is open. The useful next computation is a continuous sign/feasibility treatment of this exact common-metric eight-variable problem, exploiting the existing C9/pencil exclusions and the much better accepted covariance-gauge metric bounds where helpful. A practical horizon collar would require sharper body-specific pyramid-neighborhood estimates; the universal algebraic cutoff is too small to serve as a sensible floating-point mesh width. Neither a failed solver run nor finitely many sampled metrics would decide the residual set.

No joint110 point, no full projective-orbit exclusion, no U-only full-orbit theorem, no E17 registry exclusion, and no change to 34<=C_min<=622 are claimed.

Supplemental artifacts: complete generated bundle (`bevel_joint_horizon_bundle.zip`) and standalone source (`joint_bevel.py`).

## Complete runnable source: joint_bevel.py

```python
"""BEVEL_JOINT_QUANTIFIED_HORIZON_V1. CPython 3.13.5, standard library.
Commands: python -S joint_bevel.py build; python -S joint_bevel.py check
Exact body parent: minimum-0122, advertised SHA256
 a57548bf7f7db6cdd82467ad12462e1f201c78a3b343270a89caa20f94b4229b.
Properness: c1fb348aa34b5357be23eb9c19209c106053f6e38989e0768bb8d39608f7c39e.
The all-pyramid theorem and properness are mathematical premises, not replays.
External effective bound: Jeronimo--Perrucci--Tsigaridas, arXiv:1112.0544,
Theorem 1. No solver, numerical approximation, random input, or parent import.
"""
from fractions import Fraction as F
from itertools import combinations
from math import gcd
from pathlib import Path
import hashlib,json,sys,re
assert __debug__
NV=9
ZERO=(0,)*NV
U=((-4,-4,-3),(-4,-4,4),(-4,-3,-4),(-4,4,-4),(-4,4,4),
   (4,-4,-3),(4,-4,4),(4,-3,-4),(4,4,-4),(4,8,12))
CY=((0,1,4,3,2),(1,9,4),(3,4,9),(0,5,6,1),(1,6,9),
    (2,3,8,7),(3,9,8),(5,7,8,9,6),(0,2,7,5))
AN=((-1,0,0),(-2,0,2),(-1,2,0),(0,-1,0),(0,-2,3),
    (0,0,-1),(0,4,-1),(1,0,0),(0,-4,-4))
HT=(1,4,3,1,5,1,5,1,7)
ED=tuple(sorted({tuple(sorted((i,j))) for cy in CY for i,j in zip(cy,cy[1:]+cy[:1])}))
ADJ=tuple(tuple(j if i==v else i for i,j in ED if v in (i,j)) for v in range(10))
DE=tuple(sorted(tuple(f for f,cy in enumerate(CY) if i in cy and j in cy) for i,j in ED))
DADJ=tuple(tuple(j if i==v else i for i,j in DE if v in (i,j)) for v in range(9))
AR=tuple((i,j) for i in range(10) for j in ADJ[i])
DR=tuple((i,j) for i in range(9) for j in DADJ[i])
TRI=tuple((cy[0],cy[k],cy[k+1]) for cy in CY for k in range(1,len(cy)-1))
NAMES=('px','py','pz','m11','m22','m12','m13','m23','sat')

def add(P,Q):
 R=P.copy()
 for e,a in Q.items():
  v=R.get(e,0)+a
  if v:R[e]=v
  elif e in R:del R[e]
 return R

def scale(c,P):return {e:c*a for e,a in P.items() if c*a}
def neg(P):return scale(-1,P)
def sub(P,Q):return add(P,neg(Q))
def mul(P,Q):
 R={}
 for e,a in P.items():
  for f,b in Q.items():
   k=tuple(x+y for x,y in zip(e,f));R[k]=R.get(k,0)+a*b
 return {e:a for e,a in R.items() if a}
def const(c):return {ZERO:c} if c else {}
def var(k):
 e=list(ZERO);e[k]=1;return {tuple(e):1}
def summ(xs):
 R={}
 for P in xs:R=add(R,P)
 return R
def prod(xs):
 R=const(1)
 for P in xs:R=mul(R,P)
 return R
def deriv(P,k):
 R={}
 for e,a in P.items():
  if e[k]:f=list(e);f[k]-=1;R[tuple(f)]=e[k]*a
 return R
def degree(P):return max(map(sum,P),default=0)
def prim(P):
 g=gcd(*P.values())
 return {e:a//g for e,a in P.items()} if g else P

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def vm(A,x):return [dot(r,x) for r in A]
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def det(A):return dot(A[0],cross(A[1],A[2]))
def minus(a,b):return [x-y for x,y in zip(a,b)]
def pdot(a,b):return summ(mul(x,y) for x,y in zip(a,b))
def pmv(A,x):return [pdot(r,x) for r in A]
def pdet(M):
 a,b,c=M[0];_,d,e=M[1];_,_,f=M[2]
 return summ([prod([a,d,f]),scale(2,prod([b,c,e])),neg(prod([a,e,e])),neg(prod([d,c,c])),neg(prod([f,b,b]))])
def padj(M):
 a,b,c=M[0];_,d,e=M[1];_,_,f=M[2]
 z00=sub(mul(d,f),mul(e,e));z01=sub(mul(c,e),mul(b,f));z02=sub(mul(b,e),mul(c,d))
 z11=sub(mul(a,f),mul(c,c));z12=sub(mul(b,c),mul(a,e));z22=sub(mul(a,d),mul(b,b))
 return [[z00,z01,z02],[z01,z11,z12],[z02,z12,z22]]
def evalp(P,x):
 powers=[[F(1)] for _ in x]
 for k,v in enumerate(x):
  for _ in range(max((e[k] for e in P),default=0)):powers[k].append(powers[k][-1]*v)
 z=F(0)
 for e,a in P.items():
  w=F(a)
  for k,n in enumerate(e):
   if n:w*=powers[k][n]
  z+=w
 return z

def polynomial_system():
 p=[var(k) for k in range(3)]
 h=[add(const(4),summ(scale(u,p[k]) for k,u in enumerate(v))) for v in U]
 H=prod(h);Hi=[prod(h[j] for j in range(10) if j!=i) for i in range(10)]
 R=summ(scale(det([U[i] for i in t]),prod(h[i] for i in range(10) if i not in t)) for t in TRI)
 assert all(a%8192==0 for a in R.values())
 A={e:a//8192 for e,a in R.items()};assert len(A)==84 and degree(A)==6 and A[ZERO]==9168
 C=scale(4,mul(A,H))
 G=[sub(mul(A,summ(scale(U[i][k],Hi[i]) for i in range(10))),mul(H,deriv(A,k))) for k in range(3)]
 Z=[[sub(scale(4*U[i][k],mul(A,Hi[i])),G[k]) for k in range(3)] for i in range(10)]
 a,d,b,c,e=[var(k) for k in range(3,8)];f=sub(sub(const(1),a),d)
 M=[[a,b,c],[b,d,e],[c,e,f]];AM=padj(M);dm=pdet(M)
 minors=[a,d,f,AM[2][2],AM[1][1],AM[0][0],dm]
 normal=[[add(const(AN[i][k]),scale(HT[i],p[k])) for k in range(3)] for i in range(9)]
 sf=[sub(scale(HT[i],C),pdot(normal[i],G)) for i in range(9)]
 primal=[]
 for i,j in AR:
  edge=[sub(scale(U[j][k],h[i]),scale(U[i][k],h[j])) for k in range(3)]
  primal.append(pdot(Z[i],pmv(M,edge)))
 dual=[]
 for i,j in DR:
  edge=[sub(mul(sf[i],normal[j][k]),mul(sf[j],normal[i][k])) for k in range(3)]
  dual.append(pdot(normal[i],pmv(AM,edge)))
 saturation=sub(prod([var(8),H,dm]),const(1))
 raw=[('h'+str(i),v) for i,v in enumerate(h)]+[('psd'+str(i),v) for i,v in enumerate(minors)]+[('sat_eq',saturation)]+[('u%d_%d'%a,v) for a,v in zip(AR,primal)]+[('s%d_%d'%a,v) for a,v in zip(DR,dual)]
 out=[(name,prim(v)) for name,v in raw]
 assert len(out)==86 and max(degree(v) for _,v in out)<=20
 return out,dict(h=h,H=H,A=A,C=C,G=G,Z=Z,M=M,AM=AM,dm=dm,normal=normal,sf=sf,primal=primal,dual=dual)

def encode(obj):
 if isinstance(obj,F):return str(obj)
 if isinstance(obj,dict):return {str(k):encode(v) for k,v in obj.items()}
 if isinstance(obj,(list,tuple)):return [encode(v) for v in obj]
 return obj
def canon(obj):return (json.dumps(encode(obj),sort_keys=True,separators=(',',':'))+'\n').encode()
def put(name,b,check):
 if check:assert Path(name).read_bytes()==b,name
 else:Path(name).write_bytes(b)
 print(name,len(b),hashlib.sha256(b).hexdigest(),flush=True)
 return [len(b),hashlib.sha256(b).hexdigest()]

def integrations(Y):
 q=F(0);J=[F(0)]*3
 for t in TRI:
  dd=det([Y[i] for i in t]);assert dd>0;q+=dd
  for k in range(3):J[k]+=dd*sum(Y[i][k] for i in t)/4
 V=q/6;g=[v/q for v in J]
 # A different positive fan at original vertex 9.
 q2=F(0);J2=[F(0)]*3;o=Y[9]
 for cy in CY:
  if 9 in cy:continue
  for k in range(1,len(cy)-1):
   vs=[Y[i] for i in (cy[0],cy[k],cy[k+1])];dd=det([minus(v,o) for v in vs]);assert dd>0;q2+=dd
   for j in range(3):J2[j]+=dd*(o[j]+sum(v[j] for v in vs))/4
 assert q2==q and [v/q2 for v in J2]==g
 return V,g

def exact_control(label,p,m,S0,U0,H0):
 p=list(map(F,p));m=[[F(x) for x in r] for r in m];trace=sum(m[k][k] for k in range(3));m=[[x/trace for x in r] for r in m]
 point=p+[m[0][0],m[1][1],m[0][1],m[0][2],m[1][2],F(0)]
 h=[4+dot(v,p) for v in U];assert min(h)>0
 Y=[[F(u)/l for u in v] for l,v in zip(h,U)];V,g=integrations(Y);Z=[minus(v,g) for v in Y]
 am=[[m[1][1]*m[2][2]-m[1][2]**2,m[0][2]*m[1][2]-m[0][1]*m[2][2],m[0][1]*m[1][2]-m[0][2]*m[1][1]],
     [m[0][2]*m[1][2]-m[0][1]*m[2][2],m[0][0]*m[2][2]-m[0][2]**2,m[0][1]*m[0][2]-m[0][0]*m[1][2]],
     [m[0][1]*m[1][2]-m[0][2]*m[1][1],m[0][1]*m[0][2]-m[0][0]*m[1][2],m[0][0]*m[1][1]-m[0][1]**2]]
 dm=det(m);assert dm>0 and m[0][0]>0 and am[2][2]>0
 n=[[v/dm for v in r] for r in am]
 assert [[dot(r,c) for c in zip(*n)] for r in m]==[[F(i==j) for j in range(3)] for i in range(3)]
 normal=[[a+hh*v for a,v in zip(aa,p)] for aa,hh in zip(AN,HT)]
 support=[hh-dot(a,g) for a,hh in zip(normal,HT)];assert min(support)>0
 Q=[[v/s for v in a] for a,s in zip(normal,support)]
 uvals=[dot(Z[i],vm(m,minus(Z[j],Z[i]))) for i,j in AR]
 svals=[dot(Q[i],vm(n,minus(Q[j],Q[i]))) for i,j in DR]
 uu={ar:v for ar,v in zip(AR,uvals)};ss={ar:v for ar,v in zip(DR,svals)}
 ur=[i for i in range(10) if all(uu[i,j]<0 for j in ADJ[i])]
 sr=[i for i in range(9) if all(ss[i,j]<0 for j in DADJ[i])];hr=[];weak=[];ledger=[]
 for k,(i,j) in enumerate(ED):
  f,gf=[f for f,cy in enumerate(CY) if i in cy and j in cy];v=[uu[i,j],uu[j,i],ss[f,gf],ss[gf,f]]
  L=-v[0]-v[1];delta=dot(Q[f],vm(n,Q[f]))*dot(Q[gf],vm(n,Q[gf]))-dot(Q[f],vm(n,Q[gf]))**2
  t=-v[0]/L;co=[-v[3]/delta,-v[2]/delta];foot=[a+t*b for a,b in zip(Z[i],minus(Z[j],Z[i]))]
  assert vm(m,foot)==[co[0]*a+co[1]*b for a,b in zip(Q[f],Q[gf])]
  if max(v)<0:hr.append(k)
  if max(v)<=0 and 0 in v:weak.append(k)
  ledger.append(dict(edge=[i,j],facets=[f,gf],values=v,foot=foot,components=[t,1-t]+co))
 assert (sr,ur,hr)==(S0,U0,H0) and not weak and 0 not in uvals+svals
 assert len(sr)+len(ur)-len(hr)==2
 point[8]=1/(dm*product_num(h))
 return point,dict(label=label,p=p,M=m,N=n,volume=V,centroid=g,primal=uvals,dual=svals,S=sr,U=ur,H=hr,weak=weak,ledger=ledger)

def product_num(xs):
 z=1
 for x in xs:z*=x
 return z

def audits(polys,fields):
 out=[]
 controls=[('C9_323',[-F(1,60),-F(8,75),-F(9,100)],[[484,0,0],[0,1,0],[0,0,1]],[4,5,6],[4,9],[7,9,11])]
 for args in controls:
  x,record=exact_control(*args)
  A=evalp(fields['A'],x);H=evalp(fields['H'],x);C=evalp(fields['C'],x);G=[evalp(v,x) for v in fields['G']]
  assert record['volume']==F(4096,3)*A/H and record['centroid']==[v/C for v in G]
  h=[evalp(v,x) for v in fields['h']];sf=[evalp(v,x) for v in fields['sf']];dm=evalp(fields['dm'],x)
  for (i,j),P,v in zip(AR,fields['primal'],record['primal']):assert evalp(P,x)==v*C*h[i]*h[j]
  for (i,j),P,v in zip(DR,fields['dual'],record['dual']):assert evalp(P,x)*C*C==v*dm*sf[i]**2*sf[j]
  vals={name:evalp(P,x) for name,P in polys};assert vals['sat_eq']==0
  assert all(vals['h'+str(i)]>0 for i in range(10)) and all(vals['psd'+str(i)]>0 for i in range(7))
  record['saturation_coordinate']=x[8];record['polynomial_values']=vals;out.append(record)
 return out

def smt_poly(P):
 ts=[]
 for e,a in sorted(P.items()):
  fs=[str(a) if a>=0 else '(- %d)'%(-a)]
  for n,k in zip(NAMES,e):
   if k==1:fs.append(n)
   elif k:fs.append('%s_pow%d'%(n,k))
  ts.append(fs[0] if len(fs)==1 else '(* '+' '.join(fs)+')')
 return '0' if not ts else ts[0] if len(ts)==1 else '(+ '+' '.join(ts)+')'

def smt_program(polys):
 lines=['; Exact FULL-orbit joint S=U=1, additional physical weak points allowed.',
        '; All-C9 exclusion and properness are not supplied as solver assumptions.',
        '(set-logic QF_NRA)']
 lines += ['(declare-fun %s () Real)'%n for n in NAMES]
 for k,n in enumerate(NAMES):
  highest=max(e[k] for _,P in polys for e in P)
  for power in range(2,highest+1):
   prev=n if power==2 else '%s_pow%d'%(n,power-1)
   lines.append('(define-fun %s_pow%d () Real (* %s %s))'%(n,power,prev,n))
 lines += ['(define-fun %s () Real %s)'%(n,smt_poly(P)) for n,P in polys]
 lines += ['(assert (= sat_eq 0))']
 lines += ['(assert (>= h%d 0))'%i for i in range(10)]
 lines += ['(assert (>= psd%d 0))'%i for i in range(7)]
 def disjoint_unique(root,n,adj,prefix):
  xs=[]
  for i in range(n):
   if i!=root:xs.append('(or '+' '.join('(>= %s%d_%d 0)'%(prefix,i,j) for j in adj[i])+')')
  return '(and '+' '.join(xs)+')'
 lines += ['(assert (or '+' '.join(disjoint_unique(r,10,ADJ,'u') for r in range(10))+'))']
 lines += ['(assert (or '+' '.join(disjoint_unique(r,9,DADJ,'s') for r in range(9))+'))']
 lines += ['(check-sat)','(get-model)']
 return ('\n'.join(lines)+'\n').encode()

def smt_control(program,record):
 # Independent exact evaluation of the serialized standard SMT arithmetic.
 # This is a control audit, not execution of check-sat or an SMT solver.
 m=record['M'];point=record['p']+[m[0][0],m[1][1],m[0][1],m[0][2],m[1][2],record['saturation_coordinate']]
 env=dict(zip(NAMES,point));checked=0;assertions=[];powers=0
 def expression(text):
  tokens=(m.group(0) for m in re.finditer(r'\(|\)|[^\s()]+',text))
  def go(t=None):
   t=next(tokens) if t is None else t
   if t!='(':return F(t) if t.lstrip('-').isdigit() else env[t]
   op=next(tokens);args=[]
   while True:
    t=next(tokens)
    if t==')':break
    args.append(go(t))
   if op=='+':return sum(args)
   if op=='*':return product_num(args)
   if op=='-':assert len(args)==1;return -args[0]
   if op=='>=':assert len(args)==2;return args[0]>=args[1]
   if op=='=':assert len(args)==2;return args[0]==args[1]
   if op=='and':return all(args)
   if op=='or':return any(args)
   raise AssertionError(op)
  result=go();assert next(tokens,None) is None;return result
 for line in program.decode().splitlines():
  if line.startswith('(define-fun '):
   _,name,arguments,kind,text=line.split(' ',4)
   assert arguments=='()' and kind=='Real' and text[-1]==')'
   env[name]=expression(text[:-1])
   if name in record['polynomial_values']:
    assert env[name]==record['polynomial_values'][name];checked+=1
   else:powers+=1
  elif line.startswith('(assert '):assertions.append(expression(line[8:-1]))
 assert checked==86 and assertions==[True]*18+[False,False]
 return dict(exact_polynomial_values=checked,power_definitions=powers,base_assertions_pass=18,
             unique_U_predicate=False,unique_S_predicate=False,solver_executed=False)

def geometry_audit():
 assert (len(ED),len(DE),len(AR),len(DR),len(TRI))==(17,17,34,34,16)
 assert len(set(DE))==17
 for a,h,cy in zip(AN,HT,CY):
  assert {i for i,u in enumerate(U) if dot(a,u)==4*h}==set(cy)
  assert all(dot(a,u)<4*h for i,u in enumerate(U) if i not in cy)
  assert h*h>=dot(a,a) # B contains the Euclidean unit ball.
  for i,j in zip(cy,cy[1:]+cy[:1]):
   inward=cross(a,minus(U[j],U[i]))
   assert all(dot(inward,minus(U[k],U[i]))>0 for k in cy if k not in (i,j))
 found=set()
 for i,j,k in combinations(range(10),3):
  a=cross(minus(U[j],U[i]),minus(U[k],U[i]))
  if not any(a):continue
  ds=[dot(a,minus(u,U[i])) for u in U]
  if max(ds)<=0 or min(ds)>=0:found.add(frozenset(i for i,v in enumerate(ds) if v==0))
 assert found==set(map(frozenset,CY))
 assert all(det([U[i] for i in t])>0 for t in TRI)
 assert max(dot(u,u) for u in U)==224

def main(check=False):
 geometry_audit()
 polys,fields=polynomial_system();height=max(max(map(abs,P.values())) for _,P in polys)
 height=max(height,max(abs(u) for v in U for u in v),4,88)
 n=9;d=20;m=35;alpha=n*2**n*d**n;base=height*d**n
 ceil_log=(base-1).bit_length();K=alpha*ceil_log;E=K+2
 objectives=[('h'+str(i),v) for i,v in enumerate(fields['h'])]+[('detM',fields['dm']),('HdetM',mul(fields['H'],fields['dm']))]
 assert all(degree(v)<=d and max(map(abs,v.values()))<=height for _,v in objectives)
 assert height==514705477720 and ceil_log==78 and K==184025088000000000
 assert 995328<2**20
 summary=dict(identity='BEVEL_JOINT_QUANTIFIED_HORIZON_V1',variables=list(NAMES),basic_branch_n=n,basic_branch_m=m,
  even_degree_bound=d,coefficient_height=height,JPT_tilde_H=height,JPT_degree_bound=2**(n-1)*d**n,
  JPT_exponent=alpha,base_upper=base,base_upper_ceil_log2=ceil_log,eta_dyadic_exponent=E,
  positive_objective_dyadic_exponent=K,raw_metric_dyadic_exponent=K-2,saturation_upper_dyadic_exponent=K,
  geometric_raw_metric_dyadic_exponent=4*E+20,
  positive_objectives=[dict(name=name,degree=degree(P),height=max(map(abs,P.values()))) for name,P in objectives],
  total_monomials=sum(len(P) for _,P in polys),
  height_attainers=[[name,list(e),a] for name,P in polys for e,a in sorted(P.items()) if abs(a)==height],
  polynomials=[dict(name=name,terms=len(P),degree=degree(P),height=max(map(abs,P.values()))) for name,P in polys],
  primal_edges=ED,dual_edges=DE,facet_cycles=CY,integer_vertices=U,normal_vectors=AN,heights=HT,
  theorem_status='Quantified reduction, NOT a full-orbit infeasibility certificate; properness and JPT Theorem 1 are premises.')
 assert alpha==2359296000000000 and max(r['degree'] for r in summary['polynomials'])<=d
 # Every arbitrary choice of one outgoing edge at each nonroot uses exactly
 # 9+8 arrow inequalities. A connected component of each 35-polynomial
 # basic closed saturated system is compact by joint properness.
 assert m==1+10+7+9+8
 data=[[name,[[*e,a] for e,a in sorted(P.items())]] for name,P in polys]
 objects={}
 objects['joint_polynomials.json']=put('joint_polynomials.json',canon(data),check)
 model=smt_program(polys);records=audits(polys,fields)
 objects['joint_full.smt2']=put('joint_full.smt2',model,check)
 objects['joint_controls.json']=put('joint_controls.json',canon(records),check)
 summary['serialized_model_control']=smt_control(model,records[0])
 summary['objects']=objects
 put('joint_report.json',canon(summary),check)
 print('EXACT_FULL_ORBIT_COMMON_METRIC_OWN_CENTROID_POLYNOMIALS_PASS')
 print('N_D_M_H',n,d,m,height)
 print('ETA_GE_2_TO_MINUS',E)
 print('TRACE_ONE_RAW_METRIC_GE_2_TO_MINUS',K-2)
 print('SATURATION_COORDINATE_LE_2_TO_PLUS',K)
 print('BEVEL_JOINT_QUANTIFIED_HORIZON_RECOVERY_PASS')
if __name__=='__main__':
 if sys.argv[1:] not in (['build'],['check']):raise SystemExit('Use build or check; no solver or search is run.')
 main(sys.argv[1]=='check')
```
