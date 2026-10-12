# minimum-0048

AI research report · 2026-09-11 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

**Main result: a new facet-moment/flux sandwich, including constraints expressed entirely in the actual matrix Λ, and an exact nine-facet application proving that the added geometric information is essential.** The universal inequality excludes a complete interval of proposed covariance data that satisfies the full parent rank-four, rank-three, coordinate-flux and sharp-trace necessary system. A sharper inequality for centrally symmetric facets excludes every nonphysical member of the demonstrated family. This proves no F≥10 theorem, no nine-facet monostability exclusion, and no new C32 whole-type or root exclusion. The accepted C≥32 and 116-whole/180-remaining status is unchanged.

I first pursued elimination of the face matrices through matrix Cauchy–Schwarz and the unused part of the signed Loewner cap. That gives useful two-sided, vertex-weighted matrix inequalities. The substantive additional physical ingredient is that a true uniform planar facet has stronger affine moment restrictions than a free rank-three PSD block. Combining those restrictions with the common quadratic flux gives the new obstruction below. Its strictness is demonstrated against the full parent moment relaxation, beyond independent capped rows.

The relevant authority is the attached research-journal(20260911-092023).md, 3,778,686 bytes, SHA-256 556f87b85a084abb2b90d8ada18fa59ef86be28611b4d5e8e211cc47285fd461, specifically the lead's QUADRATIC_FACET_TRACE_V1, FACET_QUADRATIC_FLUX_COUPLING_V1 and SIGNED_QUADRATIC_FACET_TRACE_V1 records. This assignment uses those analytic records directly; no unlisted immutable worker parent is assumed. No parent-payload conflict was encountered in the material used. The journal was not modified.

**1. One physical body and the retained common geometry**

Let P={x∈R³:q_i·x≤1, i=0,…,F−1} be bounded and full-dimensional, with its own uniform volume centroid exactly 0. All following quantities belong to this same body:

- Σ=E_P xxᵀ is its actual positive-definite volume covariance.
- c_i is the actual uniform area centroid of its maximal facet F_i.
- d_i=A_i/(Vol(P)||q_i||)>0, D=diag(d), and ω=d/3.
- Y(x)=1−Qx, H=E_P YYᵀ=11ᵀ+QΣQᵀ, and λ_i=Λ[:,i]=d_i(1−Qc_i).
- K_i=d_i E_Fi YYᵀ.

Here rank H=4, rank K_i=3, K_i e_i=0, K_iω=λ_i, Hω=1, and ωᵀλ_i=d_i. The inherited common identities are

    Σ_i K_i = 5H−2·11ᵀ,
    Σ_i q_ik K_i = −(q^(k)1ᵀ+1(q^(k))ᵀ),  k=1,2,3.

These also follow directly from divergence applied to products of affine functions. In physical homogeneous coordinates X=(1,x)ᵀ, put G=diag(1,Σ), L=[1,−Q], and T_i=d_i E_Fi XXᵀ. Then H=LGLᵀ, K_i=LT_iLᵀ, and

    Σ_i T_i = diag(3,5Σ),
    Σ_i q_ik T_i = e_0 e_(k+1)ᵀ+e_(k+1)e_0ᵀ.

For example, the spatial-spatial part of the second identity is zero because the actual volume centroid is zero. This retains the full coordinate flux, not only its scalar trace.

For every ξ∈P define

    w_i(ξ)=1−q_i·ξ ≥ 0,
    T(ξ)=5H−2·11ᵀ+(Qξ)1ᵀ+1(Qξ)ᵀ.

The common flux gives the exact identity

    Σ_i w_i(ξ)K_i = T(ξ).                                      (1)

The reciprocal physical metric pair is preserved throughout. Under an actual linear deformation x↦Ax, poles become A^(−T)q_i, facet centroids become Ac_i, and covariance becomes AΣAᵀ. The quantities d, Λ, H and K_i are invariant after these simultaneous transformations. Mechanics in the original coordinates uses the paired pullback metrics AᵀA and (AᵀA)^(−1). Neither metric is selected independently, and no centroid of a polar body is substituted for the original volume centroid.

**2. The additional physical facet inequality**

For every nonnegative affine function f on a true uniform two-dimensional convex facet F,

    E_F f² ≤ (3/2)(E_F f)².                                   (2)

The constant 3/2 is sharp: on a triangle, take f equal to a barycentric coordinate, so E f=1/3 and E f²=1/6. This is the planar p=1,q=2 case of classical Berwald: sqrt(6 E f²)≤3 E f. I checked the primary statement in Langharst–Putterman, Weighted Berwald's Inequality, arXiv:2210.04438v7, Introduction equation (1). The classical inequality is imported; the coupled Λ/flux consequences here are deductions. [Primary source](https://arxiv.org/pdf/2210.04438).

A self-contained specialized derivation of (2), using planar Brunn–Minkowski, is short. The zero and constant cases are immediate. Otherwise put μ=E_F f>0, M=max_F f, and

    h(t)=sqrt(Area{u∈F:f(u)≥t}/Area(F)),  0≤t≤M.

The superlevel sets satisfy the Minkowski inclusion supplied by affine f, so h is concave, h(0)=1 and h(M)=0. Thus h(t)≥1−t/M and μ=∫h(t)²dt≥M/3. Set a=3μ≥M and compare h(t)², extended by zero beyond M, with (1−t/a)² on [0,a]. The difference h(t)−(1−t/a) is concave on [0,M] and vanishes at 0; its quotient by t is nonincreasing. Consequently the difference of the two squared tails changes sign at most once, from positive to negative. Their integrals are both μ. Multiplication by increasing t therefore makes the integral of their difference nonpositive. Hence

    E_F f² = 2∫t h(t)²dt
           ≤ 2∫_0^a t(1−t/a)²dt
           = a²/6 = (3/2)μ².

There is a useful stronger geometric version:

    E_F f² ≤ (4/3)(E_F f)²                                    (3)

for every centrally symmetric planar facet F and every affine f≥0 on it. This includes parallelograms and is sharp on parallelograms.

To prove (3), translate within the facet to its symmetry center, which is its actual area centroid, and write f=A+t, where t is a linear functional. Its support interval is [−h,h], and f≥0 implies A≥h. The chord-length density ℓ(t) is even and concave, hence nonincreasing on [0,h]. Reverse Chebyshev, applied to increasing t² and decreasing ℓ, gives E t²≤h²/3. Therefore E f²=A²+E t²≤(4/3)A². The constant and zero cases are immediate. In parallelogram coordinates u,v∈[−1,1], this is also the elementary identity E(A+Bu+Cv)²=A²+(B²+C²)/3, together with A≥|B|+|C|.

These are restrictions of uniform area on actual facet geometry. They do not follow merely from positive semidefiniteness and rank three.

**3. New multi-column inequalities, with a complete test domain**

For each facet choose a valid geometric constant κ_i: always κ_i=3/2, and κ_i=4/3 when the actual facet is centrally symmetric. Define

    M(ξ)=Λ diag(w_i(ξ)/d_i) Λᵀ,
    M_κ(ξ)=Λ diag(κ_i w_i(ξ)/d_i) Λᵀ.

Then every physical body above satisfies

    M(ξ) ≼ T(ξ),                                              (4)
    T(ξ) ≼_cop M_κ(ξ),                                       (5)

for every ξ∈P. Here ≼ is Loewner order. The notation A≼_cop B means zᵀ(B−A)z≥0 for every z≥0.

Proof of (4): ordinary matrix Cauchy–Schwarz on each facet gives

    λ_i λ_iᵀ/d_i ≼ K_i.

Multiply by w_i(ξ)≥0, sum, and use (1). Proof of (5): for z≥0 the affine function f=zᵀY is nonnegative on P, so the facet inequality gives

    zᵀK_i z = d_i E_Fi f²
             ≤ κ_i d_i(E_Fi f)²
             = κ_i(zᵀλ_i)²/d_i.

Weighting and summing again gives (5). In particular, with all κ_i=3/2,

    (2/3) zᵀT(ξ)z ≤ zᵀM(ξ)z ≤ zᵀT(ξ)z,  z≥0.             (6)

The upper inequality (5) uses copositive order. Sign-changing affine functions still use the separate signed Loewner cap; replacing (5) by a Loewner inequality would be invalid, since a nonconstant signed affine function on a facet can have zero mean and positive second moment.

The function domain is complete: every affine f≥0 on P has a nonnegative slack representation. Indeed, writing f=α+β·x, its actual volume mean is α. If α=0 then f is identically zero. Otherwise −β/α belongs to the polar conv{q_i}; a convex representation there gives f=Σ_i z_i(1−q_i·x) with z_i≥0.

The weighting domain is also complete and finite for fixed actual geometry. Both sides of (4) and (5) depend affinely on ξ, so checking every actual vertex of P is equivalent to checking every ξ∈P. More generally, every nonnegative affine weighting α+q_i·v is a nonnegative multiple of w_i(ξ): averaging with ω gives α≥0; if α=0 all weights vanish, and otherwise ξ=−v/α∈P.

Thus these are multi-column constraints using the same covariance and the same actual body, with no independent row optimization.

**4. A consequence expressed entirely in Λ**

The facet-centroid choices ξ=c_j eliminate explicit vertex coordinates. Put

    A_j = Λ diag(Λ_ij/d_i) Λᵀ,
    B_j = λ_j1ᵀ+1λ_jᵀ,
    A_j^(κ) = Λ diag(κ_i Λ_ij/d_i) Λᵀ.

Since 1−Qc_j=λ_j/d_j, equations (4)–(5) imply

    A_j ≼ 5d_j H−B_j ≼_cop A_j^(κ).                          (7)

Combining the lower inequality for j with the upper inequality for k eliminates H:

    (A_k^(κ)+B_k)/d_k − (A_j+B_j)/d_j ≽_cop 0               (8)

for every pair j,k. With the universal constant, A_k^(κ)=(3/2)A_k.

This can literally be written using Λ alone. The inherited physical identity Λ²+Λ=4·1dᵀ and Λ_ii=0 gives

    d_i=(Λ²)_ii/4>0.

For example, the diagonal consequences of (8) are the explicit scalar inequalities

    [(3/2)Σ_i Λ_ik Λ_ai²/d_i + 2Λ_ak]/d_k
       ≥ [Σ_i Λ_ij Λ_ai²/d_i + 2Λ_aj]/d_j

for every a,j,k. Full copositivity retains more information than these diagonal tests. An additional unweighted index can be included by setting d_*=1, A_*=ΛD^(−1)Λᵀ, B_*=2·11ᵀ and A_*^(κ)=Λdiag(κ_i/d_i)Λᵀ.

These are necessary physical Λ constraints. The exact strictness application below proves added strength of the joint (Λ,H,K_i) system; I have not separately proved that the Λ-only projection (8) is independent of every previously known identity involving Λ.

**5. Complementary elimination using the signed Loewner cap**

The original direction also yields a useful second matrix bound. Set c=25/12 and

    P_i=H−(He_i)(He_i)ᵀ/H_ii,
    π_i=ωᵀP_iω,
    δ_i=cπ_i−d_i,
    r_i=cP_iω−λ_i,
    L_i=λ_iλ_iᵀ/d_i,
    U_i=cP_i−r_i r_iᵀ/δ_i.

For a physical body δ_i>0: the sharper parent cap gives d_i≤c_aff π_i<cπ_i. Matrix Cauchy–Schwarz applied first to K_i and then to cP_i−K_i proves

    L_i ≼ K_i ≼ U_i.

Consequently

    Σ_i w_i(ξ)L_i ≼ T(ξ) ≼ Σ_i w_i(ξ)U_i                    (9)

for every ξ∈P. This eliminates all K_i from the signed-cap/common-flux relaxation. Again the complete ξ-domain consists of the actual vertices.

A complete analytic application is covariance rigidity of the regular tetrahedron. Take the four poles (1,1,1), (1,−1,−1), (−1,1,−1), (−1,−1,1), actual Λ=J−I and d_i=3/4, but allow any proposed SPD covariance Σ. At ξ=−q_i the weights are 4e_i. Both L_i and U_i annihilate e_i, so the sandwich (9) forces T(−q_i)e_i=0. Direct expansion gives

    T(−q_i)e_i=Q(5Σ−I)q_i.

The poles span R³, hence Σ=I/5. Conversely the actual uniform tetrahedron has Σ=I/5 and supplies feasible matrices. This covers the entire SPD covariance domain; it is an analytic result without numerical search.

The next control shows why (9), even together with actual common K_i satisfying all parent flux equations, still needs the new facet-shape information.

**6. Exact nine-facet body and the full parent-relaxation family**

Let

    B=conv[(-3,-2),(1,-2),(3,0),(3,1),(2,2),(-2,2),(-3,1)],
    g=(-2/9,1/21),
    P=(B−g)×[-1,1].

The polygon has area 21. The actual homogeneous prism has volume 42, own centroid 0 and (V,E,F)=(14,21,9). Its physical reciprocal metric pair is M=N=I₃. Its actual covariance is

    Σ₀=diag(S,1/3),
    S=[[2833/1134,8/27],[8/27,1055/882]].

Index side facets 0,…,6 in the listed polygon-edge order, top z=1 as 7 and bottom z=−1 as 8. The complete exact Q,d,c_i,Λ and face matrices are reconstructed by the source below from these literal vertices. In particular d_7=d_8=1/2 and Σ_(i<7)d_i=2.

Let T_i⁰=d_i E_Fi XXᵀ be the actual four-dimensional face moments, with X=(1,x,y,z)ᵀ. Keep Q,d,c_i and therefore Λ fixed. For every parameter

    1/3 ≤ a < 3/5,

define a proposed volume moment matrix and proposed face moments by

    G(a)=diag(1,S,a),
    s(a)=(5a−1)/2,
    T_i(a)[3,3]=d_i s(a),  i=0,…,6,

leaving every other entry of every T_i⁰ unchanged. Both base matrices remain completely unchanged. Set H(a)=LG(a)Lᵀ and K_i(a)=LT_i(a)Lᵀ.

Every member of this entire interval satisfies all of the following:

- rank H=4; every K_i is PSD of rank three with exactly the required common affine kernel plus e_i.
- K_i e_i=0, K_iω=λ_i, and all entries away from the own zero row and column are strictly positive.
- The full global and all three coordinate quadratic flux identities hold, not only their traces.
- K_i≼2P_i(a), stronger than the sharp signed parent cap because c_aff≥1408/679>2.
- Entrywise 0≤K_i≤(3/2)H, hence the earlier copositive cap holds with a constant stronger than c₂, since c₂≥4455/2888>3/2.
- Λ is the actual trace matrix of the fixed prism. Its row sums, rank, matrix-square identity, ΛQ=−Q, caps and reciprocal products therefore remain physical. The source explicitly checks the row caps, matrix-square identity and reciprocal products as well.

The whole-interval proof is essential. The changed global entry is correct because 2s(a)+1=5a. The changed coordinate-flux entries vanish because the side poles have z-component zero and Σ_(i<7)d_i q_i=0. All T_i(a), G(a), undeﬂated cap differences 2G(a)−T_i(a), and entrywise differences (3/2)H(a)−K_i(a) are affine in a. The exact endpoint PSD and entrywise checks at a=1/3 and a=3/5 therefore prove the corresponding inequalities throughout the closed interval. The fixed face kernel then gives the deflated cap. Rank three holds throughout because the two side tangent variances are positive; the other face matrices remain actual. Strict off-facet positivity excludes a=3/5: the potentially vanishing side moment is d_i E[(1−z)(1+z)]=d_i(1−s(a)).

Thus these controls also satisfy every consequence (9) of the full parent system. They have one common rank-four H and common rank-three blocks; this is not a rank-free construction.

Nevertheless every a≠1/3 is nonphysical. The fixed nine halfspaces uniquely specify the product body P, whose actual uniform axial variance is 1/3. The proposed H(a) uses a different covariance. The mean data remain actual, while selected second moments have been altered. At a=1/2, for example, the proposed volume z-variance is 1/2 and each proposed side-face z-variance is 3/4.

**7. Complete exclusions, exact residual barrier, and the missing same-body condition**

Take ξ=(0,0,−1)∈P and f=1−z, which is slack coordinate 7. Then the seven side weights are 1, the top weight is 2 and the bottom weight is 0. The top contribution is zero because f is zero there. Throughout the entire family,

    T_f(a):=Σ_i w_i K_i[7,7]=1+5a,
    M_f:=Σ_i w_i Λ_7i²/d_i=2.

The new universal facet inequality requires 2T_f≤3M_f, equivalently

    a≤2/5.

It therefore excludes the complete interval 2/5<a<3/5, although every member passes the full parent common-moment and sharp-trace system. The exact certificate gap is

    3M_f−2T_f=4−10a.

At a=1/2 this equals −1. Removing the new facet inequality restores this exact feasible parent-relaxation control, so the improvement is not attributable to independent row caps or to a cap-only ablation.

The weak universal factor-3/2 inequalities still admit every a∈(1/3,2/5]. This is a statement about the entire cone of nonnegative affine functions on every face. On a side rectangle use standardized coordinates u,z∈[−1,1]. Any such function has the form f=A+Bu+Cz with A≥|B|+|C|. The proposed moments give

    E f²=A²+B²/3+s(a)C².

When a≤2/5, s(a)≤1/2, so the variance is at most (B²+C²)/2≤A²/2. Every side-face inequality (2) follows; the base moments remain actual and satisfy it as well. The exact survivor a=3/8 has s=7/16 and the displayed universal gap 1/4. This residual statement concerns the weak inequalities; adding equality-case characterizations can remove their endpoint a=2/5.

The missing same-body condition is explicit here: the side facets are actual parallelograms, so their uniform affine moment constant is 4/3. Their contributions are the only nonzero ones in this test. Applying (3) through (5) gives

    3T_f≤4M_f,
    3(1+5a)≤8,
    a≤1/3.

Hence the shape-aware physical inequality excludes every nonphysical member of the full interval (1/3,3/5). Its exact gap is

    4M_f−3T_f=5−15a.

At the universal-relaxation survivor a=3/8 it equals −5/8. The genuine a=1/3 member attains equality. This is a complete demonstrated application on the specified nine-facet domain.

The scope is important: this prism has at least its two stable base facets and is not a monostability witness. It is also outside the C32 equality f-vector (9,16,9). The example establishes strictness and a realizability barrier of necessary moment systems. It does not establish feasibility or infeasibility of a nine-facet monostability system.

There is also an exact barrier to obtaining the improved constant from quadrilateral combinatorics alone. For 0<ε<1, the quadrilateral

    (0,0), (1−ε,0), (1−ε,ε), (0,1)

is the triangle u,v≥0, u+v≤1 cut by u≤1−ε. For f=v, direct subtraction of the removed triangle gives

    E f=(1−ε³)/(3(1−ε²)),
    E f²=(1−ε⁴)/(6(1−ε²)),
    E f²/(E f)²=3(1−ε²)(1−ε⁴)/(2(1−ε³)²) → 3/2.

Thus actual symmetry or quantitative shape information is required for a uniform improvement below 3/2 on quadrilaterals.

**8. Self-contained recovery capsule**

New exact object identity: NINE_FACET_AXIAL_SHARED_MOMENT_BARRIER_V1. The following final source includes the actual-facet incidence, rank and Λ checks added during the root verification. It supersedes the shorter intermediate source; use these pins.

Dependencies: CPython 3.12.14, standard library only, assertions enabled. There are no random inputs, optimizers, third-party packages or external data files. The literal polygon, face ordering, parameter family, endpoints and witnesses are all in the source. The interval arguments and the universal facet inequalities are analytic parts of this capsule; evaluating five rational parameters alone would not prove the intervals.

Save as axial_control.py, UTF-8/LF with one final LF. Reconstruct and verify with:

    python -S axial_control.py > axial_control.log
    sha256sum axial_control.py axial_control.json axial_control.log

Observed final pins:

- axial_control.py: 6130 bytes; SHA-256 c1b3b8e07095ebd1d0788b3cbe7dd7667fc5a78e307a4d51192659579464d85c.
- axial_control.json: 1886 bytes; SHA-256 b0fc78f6eac930f265616181c0baece3b42c82aa0bff9cf98e2c1b97edfd5fef.
- axial_control.log: 2032 bytes; SHA-256 82ae7a36f6e02402afd490928a2ed765d0eaa6218d93666cee63bf49ba4bb671.

Expected final marker: NINE_FACET_AXIAL_SHARED_MOMENT_BARRIER_V1_PASS. The final source was executed successfully with captured stdout and no stderr; an earlier standalone copy was also reproduced in a fresh directory. All arithmetic relevant to acceptance uses Fraction and exact principal minors.

```python
#!/usr/bin/env python3
"""Python 3.11+ stdlib. Exact nine-facet shared-moment relaxation barrier."""
from fractions import Fraction as F
from itertools import combinations
import json,hashlib
assert __debug__

P=[[-3,-2],[1,-2],[3,0],[3,1],[2,2],[-2,2],[-3,1]]
P=[[F(x) for x in v] for v in P]
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def tr(A): return list(map(list,zip(*A)))
def mm(A,B): return [[dot(r,c) for c in tr(B)] for r in A]
def mv(A,v): return [dot(r,v) for r in A]
def outer(x,y): return [[a*b for b in y] for a in x]
def sc(t,A): return [[t*a for a in r] for r in A]
def add(A,B): return [[a+b for a,b in zip(r,s)] for r,s in zip(A,B)]
def zeros(n): return [[F(0)]*n for _ in range(n)]
def det(A):
    A=[r[:] for r in A]; ans=F(1)
    for j in range(len(A)):
        p=next((i for i in range(j,len(A)) if A[i][j]),None)
        if p is None: return F(0)
        if p!=j: A[p],A[j]=A[j],A[p]; ans=-ans
        ans*=A[j][j]
        for i in range(j+1,len(A)):
            t=A[i][j]/A[j][j]
            for k in range(j+1,len(A)): A[i][k]-=t*A[j][k]
    return ans
def minors(A):
    return [det([[A[i][j] for j in S] for i in S])
            for k in range(1,len(A)+1) for S in combinations(range(len(A)),k)]
def psd(A): return min(minors(A))>=0
def cross(a,b): return a[0]*b[1]-a[1]*b[0]
area=F(0); m=[F(0)]*2; R=zeros(2)
for a,b in zip(P,P[1:]+P[:1]):
    w=cross(a,b)/2; area+=w
    for r in range(2):
        m[r]+=w*(a[r]+b[r])/3
        for s in range(2):
            R[r][s]+=w*((a[r]*a[s]+b[r]*b[s])/6+(a[r]*b[s]+b[r]*a[s])/12)
g=[x/area for x in m]
S=[[R[r][s]/area-g[r]*g[s] for s in range(2)] for r in range(2)]
V=[[v[r]-g[r] for r in range(2)] for v in P]
Q=[]; d=[]; C=[]; T0=[]
for a,b in zip(V,V[1:]+V[:1]):
    N=[b[1]-a[1],a[0]-b[0]]; h=dot(N,a)
    Q.append([N[0]/h,N[1]/h,F(0)]); d.append(h/area)
    c=[(a[0]+b[0])/2,(a[1]+b[1])/2,F(0)]; C.append(c)
    W=zeros(4); W[0][0]=1
    for r in range(3): W[0][r+1]=W[r+1][0]=c[r]
    for r in range(2):
        for s in range(2): W[r+1][s+1]=(a[r]*a[s]+b[r]*b[s])/3+(a[r]*b[s]+b[r]*a[s])/6
    W[3][3]=F(1,3); T0.append(sc(d[-1],W))
for z in [F(1),F(-1)]:
    Q.append([F(0),F(0),z]); d.append(F(1,2)); C.append([F(0),F(0),z])
    W=zeros(4); W[0][0]=W[3][3]=1; W[0][3]=W[3][0]=z
    for r in range(2):
        for s in range(2): W[r+1][s+1]=S[r][s]
    T0.append(sc(F(1,2),W))
L=[[F(1)]+[-x for x in q] for q in Q]
Lambda=[[d[i]*(1-dot(Q[j],C[i])) for i in range(9)] for j in range(9)]
def family(a):
    G=zeros(4); G[0][0]=1; G[3][3]=a
    for r in range(2):
        for s in range(2): G[r+1][s+1]=S[r][s]
    T=[[r[:] for r in W] for W in T0]
    for i in range(7): T[i][3][3]=d[i]*(5*a-1)/2
    H=mm(mm(L,G),tr(L)); K=[mm(mm(L,W),tr(L)) for W in T]
    return G,T,H,K
assert area==21 and g==[F(-2,9),F(1,21)]
assert sum(d)==3 and mv(tr(Q),d)==[0]*3
assert all(t>0 for t in d) and det(S)>0
assert det(mm(tr(L),L))>0
assert all(sum(r)==3 for r in Lambda)
assert all(Lambda[i][i]==0 and all(0<Lambda[i][j]<F(10,9)
           for j in range(9) if j!=i) for i in range(9))
assert mm(Lambda,Q)==sc(-1,Q)
assert add(mm(Lambda,Lambda),Lambda)==sc(4,outer([F(1)]*9,d))
assert all(Lambda[i][j]*Lambda[j][i]<=1 for i in range(9) for j in range(9))
for i in range(7):
    for j,p in enumerate(V):
        slack=1-dot(Q[i][:2],p)
        assert (slack==0) if j in [i,(i+1)%7] else (slack>0)
berwald=[]
for a in [F(1,3),F(3,8),F(2,5),F(1,2),F(3,5)]:
    G,T,H,K=family(a); total=zeros(4)
    for W in T: total=add(total,W)
    expected=sc(5,G); expected[0][0]=3; assert total==expected
    for k in range(3):
        flux=zeros(4)
        for i in range(9): flux=add(flux,sc(Q[i][k],T[i]))
        expected=zeros(4); expected[0][k+1]=expected[k+1][0]=1
        assert flux==expected
    for i in range(9):
        assert psd(T[i]) and det(T[i])==0
        assert any(det([[T[i][r][s] for s in I] for r in I])>0 for I in combinations(range(4),3))
        assert mv(T[i],L[i])==[0]*4
        assert mv(K[i],[z/3 for z in d])==[Lambda[j][i] for j in range(9)]
        u=mv(G,L[i]); Pi=add(G,sc(-1/dot(L[i],u),outer(u,u)))
        assert psd(add(sc(2,Pi),sc(-1,T[i])))
        assert all(0<=K[i][r][s]<=F(3,2)*H[r][s] for r in range(9) for s in range(9))
        if a<F(3,5): assert all(K[i][r][s]>0 for r in range(9) for s in range(9) if r!=i and s!=i)
    # x=(0,0,-1) in P; w_i=1+q_iz. f=1-z is coordinate7 of Y.
    w=[1+q[2] for q in Q]
    lhs=sum(w[i]*K[i][7][7] for i in range(9))
    mean=sum(w[i]*Lambda[7][i]**2/d[i] for i in range(9))
    assert lhs==1+5*a and mean==2
    gap=3*mean-2*lhs; assert gap==4-10*a
    shape_gap=4*mean-3*lhs; assert shape_gap==5-15*a
    berwald.append(dict(a=a,weighted_second_moment=lhs,weighted_squared_means=mean,
                       gap=gap,parallelogram_gap=shape_gap))
bad=[F(1,2),F(3,4)] # synthetic volume z variance and side-face z variance
def ser(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,list): return [ser(v) for v in x]
    if isinstance(x,dict): return {k:ser(v) for k,v in x.items()}
    return x
out=ser(dict(identity='NINE_FACET_AXIAL_SHARED_MOMENT_BARRIER_V1',polygon=P,
    z_interval=[-1,1],volume=2*area,original_centroid=g+[F(0)],centered_planar_covariance=S,
    Q=Q,d=d,face_centroids=C,parameter_interval=['1/3','3/5 (excluded)'],
    strict_nonphysical_interval=['1/3 (excluded)','3/5 (excluded)'],
    explicit_nonphysical_variances=bad,signed_cap=2,entrywise_copositive_cap='3/2',
    exact_checked_parameters=['1/3','3/8','2/5','1/2','3/5'],berwald_witnesses=berwald,
    berwald_excluded_interval=['2/5 (excluded)','3/5 (excluded)'],
    nonphysical_interval_surviving_full_face_berwald=['1/3 (excluded)','2/5'],
    parallelogram_shape_bound_excludes=['1/3 (excluded)','3/5 (excluded)'],
    genuine_body_axial_volume_variance='1/3',genuine_side_face_axial_variance='1/3'))
raw=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode()
open('axial_control.json','wb').write(raw)
print(raw.decode(),end='')
print('CONTROL_BYTES',len(raw))
print('CONTROL_SHA256',hashlib.sha256(raw).hexdigest())
print('NINE_FACET_AXIAL_SHARED_MOMENT_BARRIER_V1_PASS')
```

**9. Most useful continuation and unresolved scope**

The next useful integration is to impose (4), (5) and (9) at all actual vertices, or initially impose the coordinate-free centroid version (7) and Λ-only consequence (8). The universal κ_i=3/2 requires no face classification. Improvements such as κ_i=4/3 require actual geometric symmetry, not merely a quadrilateral label. All d_i and the denominators in the signed-cap completion must remain those of the same body.

The regression controls are exact and complementary: a=1/2 must pass the full parent system and fail the new universal facet inequality; a=3/8 must pass that universal augmentation and fail the actual parallelogram constraint; a=1/3 is the genuine body. These distinguish implementation errors, cap-only improvements, and genuine use of same-body facet geometry.

The remaining research problem is applying this stronger geometry to a complete mechanically relevant nine-facet domain. No monostable control satisfying the strengthened system has been produced here, and no failed search has been interpreted as infeasibility. The five TREE253/266/272/278/285 batch was not duplicated. The continuation should combine the new multi-column inequalities with actual incidence and reciprocal-metric mechanical constraints while retaining true uniform facet moments and the actual volume covariance.
