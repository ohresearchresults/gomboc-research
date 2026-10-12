# minimum-0296

AI research report · 2026-09-28 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# FOUR_CENTRAL_SECTIONS_TETRAHEDRAL_SHELL_1OVER42_AND_FULL_CUT_STACK_1OVER512_V1

## 1. Result: the larger positive-pencil gap is closed

The full `1/1024` lateral region left open by the parent is now excluded for every positive pencil parameter. In fact, the following theorem doubles both lateral allowances and covers the entire maximal pencil.

**Theorem A — full pencil, independent cuts and full weight triangle.** Let

```text
0 < beta < 1,  s > 0,
u_j >= 0,  u_0+u_1+u_2 = 1,
0 < p_j <= s/512,
0 < q_j <= min(1,s)/512,
Q = max(q_0,q_1,q_2).
```

For every

```text
-1/s < a < 1 + 1/Q,
```

the actual uniformly filled cut-stack hull at its own volume centroid has **at least two strict unstable equilibria under every SPD metric**. Every complete true weak rooted tree is impossible even for every nonzero PSD matrix. No stable-root, conditioning, weak-freedom or selected-tree assumption is imposed.

This includes the regular sections `a=0,1`, every positive `a`, both outer sectors, and arbitrarily close approaches to both genuine horizons. The singular horizon endpoints themselves are not included as ten-vertex bodies. This is not a renaming of the old negative-sector theorem: the new argument works across the entire positive sector at a larger lateral scale.

**Theorem B — unrestricted relative left cuts and a majority positive tail.** Retain all beta, s and the complete closed weight triangle, but suppose

```text
0 < p_j < s,
0 < q_j <= min(1,s)/1024.
```

Then the same all-metric conclusions hold throughout

```text
256/s <= a < 1 + 1/Q.
```

This is strictly more than the last three quarters of the full positive interval. All three ratios `p_j/s` vary independently over `(0,1)`.

Theorem A enlarges the parent's full-pencil coefficient box by a factor of 256. Theorem B permits right coefficients 256 times the parent's majority-tail allowance and lowers its starting value of `a s` by a factor of 256. More importantly, Theorem A resolves the specific `1/1024` positive-pencil residual rather than constructing another neighborhood of one parameter tuple. Both conclusions retain all eleven chart parameters and the entire weight triangle.

The mechanism is a **four-central-section alternative for the comparison tetrahedron**, together with a substantially sharper bound on the actual uniform centroid. It raises the universal tetrahedral-shell allowance from `1/8192` to **`1/42`**. No claim of optimality is made.

## 2. Input audit and evidence boundary

I read the complete new journal, lines 1–1711 through EOF, including the complete literal parent `minimum-0294`. The attachment is 340120 bytes, SHA-256 `ea98998fba024e7b90ebd5404df18f306f5b8fc8fe7d8b7926d2c49ea2337a7f`. Reconstructing the parent's compact UTF-8 JSON envelope gives 32924 bytes and the required SHA-256 `015c3b231f371f6869d91db389602a4073caa96d21dd5408be8857c7d4e92100`. Its Markdown alone is 32225 bytes, SHA-256 `4d5f19b1a3d2d76961b5bacb63572a71f68ce6c227d85e452967ff848ef1b025`. There is no parent-identity conflict.

Earlier unchanged context was retained. The previously supplied 11970-byte `positive_shell.py` was read completely before reusing its exact geometry utilities. The new audit below is standalone: it imports no parent module and needs none of the older numerical pencil/beta packages. Those unprovided packages were not replayed. No necessary unread dependency remains for the new result.

The accepted parent's shell, actual-centroid convention, complete weight-boundary treatment and unresolved larger scale are the antecedent, not a substitute for the new proof. Its three encoded DATA corrections remain part of its historical recovery; the new readable source needs **no patches**. fileciteturn6file0L19-L38

## 3. Actual geometry, fresh uniform moments and true weight boundaries

Use labels `0,1,2=B0,B1,B2`, `3,4,5=L0,L1,L2`, `6,7,8=R0,R1,R2`, `9=S`. The literal chart is

```text
B0=(0,-beta,0),  B1=(0,1-beta,0),  B2=(0,0,1),
d_j=1+a p_j,  e_j=1+(1-a)q_j,  d_s=1+a s,
L_j=(-p_j,(B_j)_y,(B_j)_z)/d_j,
R_j=( q_j,(B_j)_y,(B_j)_z)/e_j,
S=(-s,sum_j u_j(B_j)_y,sum_j u_j(B_j)_z)/d_s,
Delta=s-sum_j u_j p_j.
```

The actual body is their convex hull. Theorems A and B have `s>max p_j`, hence `Delta>0` for every allowed weight and maximal positive-denominator interval exactly `(-1/s,1+1/Q)`. These are the parent's actual coordinates. fileciteturn7file0L17-L31

For positive weights the outward maximal cycles and genuine edges are

```text
F0=(0,3,4,1,7,6)  F1=(0,2,5,3)  F2=(0,6,8,2)
F3=(1,4,5,2)      F4=(1,2,8,7)  F5=(3,9,4)
F6=(3,5,9)        F7=(4,9,5)    F8=(6,7,8)

02,03,06,12,14,17,25,28,34,35,39,45,49,59,67,68,78.
```

These are true mechanical features, not integration diagonals. At `a=0`, the left part is the prismatoid between the transverse triangle and the affine graph `x=-sum p_j lambda_j`; the right vertices lie on the three segments from B_j towards `(1,0,0)`. The stack point lies beyond the left triangular cut and within its side halfspaces. The positive projectivity `X/(1-a X_x)` gives precisely the displayed general-a hull. This establishes geometry only; every resulting hull is refilled uniformly. fileciteturn7file0L33-L43

Its seven actual positive tetrahedra have the following six-volumes:

```text
(0,1,2,5): p2/d2
(0,1,4,5): p1/(d1 d2)
(0,3,4,5): p0/(d0 d1 d2)
(3,4,5,9): Delta/(d_s d0 d1 d2)
(0,1,2,8): q2/e2
(0,1,7,8): q1/(e1 e2)
(0,6,7,8): q0/(e0 e1 e2).
```

For weights w_t, vertex sums C_t and outer-product sums J_t, the **one actual uniform centre and covariance** are

```text
D=sum_t w_t,
Vol(P_a)=D/6,
g_a=sum_t w_t C_t/(4D),
E[XX^T]=sum_t w_t(C_t C_t^T+J_t)/(20D),
Sigma_a=E[XX^T]-g_a g_a^T.
```

They are recomputed after every shape/projective change. fileciteturn7file0L45-L64

The actual weight-boundary changes remain explicit:

```text
u0=0: merge F3/F7, delete L1--L2;
u1=0: merge F1/F6, delete L0--L2;
u2=0: merge F0/F5, delete L0--L1.
```

Exactly one zero weight gives **10/16/8**, with a pentagonal merger in the first two cases and a heptagonal merger in the third. At `u_j=1`, two mergers occur, L_j lies strictly between B_j and S and is removed as a redundant label, giving **9/14/7**. The proof uses the resulting true vertices and edges; it does not apply a nine-vertex exclusion to a ten-vertex facet-merging edge of the weight triangle. fileciteturn7file0L68-L78

## 4. New four-section alternative on a regular tetrahedron

Let

```text
z0=(1,1,1), z1=(1,-1,-1),
z2=(-1,1,-1), z3=(-1,-1,1),
T=conv(z0,z1,z2,z3).
```

Its centroid is zero, covariance `I/5`, diameter `sqrt(8)` and circumradius `sqrt(3)`.

Normalize a nonzero PSD matrix M by `tr M=1`. An orthogonal symmetry of T allows the ordering

```text
n0 >= n1 >= n2 >= n3,  n_i=z_i^T M z_i,  sum_i n_i=4.
```

Consider these four planes, their section vertices and witnesses on opposite sides:

```text
A: x1=0; section vertices +/-e2,+/-e3; witnesses z0,z2; m_A=n2.
B: x2=0; section vertices +/-e1,+/-e3; witnesses z0,z1; m_B=n1.
C: x3=0; section vertices +/-e1,+/-e2; witnesses z0,z1; m_C=n1.
D: z0.x=0; section vertices w_j=(z0+3z_j)/4, j=1,2,3;
   witnesses z0,z1; m_D=n1.
```

**Four-section lemma.** At least one of these planes H satisfies

```text
m_H - max_{y in T intersect H} y^T M y > 7/32.
```

This is a complete all-metric alternative, including singular matrices and all norm-order ties.

### Exact finite proof

Set `P_i=z_i z_i^T`, `E_k=e_k e_k^T`, using zero-based coordinate indices below. Failure of each proposed section permits selection of one corresponding row whose contraction with M is nonpositive:

```text
C_A = [32(P2-E1)-7I, 32(P2-E2)-7I],
C_B = [32(P1-E0)-7I, 32(P1-E2)-7I],
C_C = [32(P1-E0)-7I, 32(P1-E1)-7I],
C_D = [32(P1-w_j w_j^T)-7I : j=1,2,3].
```

Convexity makes the section maximum occur at a displayed section vertex. The three norm-order rows

```text
O_j=32(P_{j+1}-P_j), j=0,1,2
```

also have nonpositive contraction with M. There are exactly `2*2*2*3=24` failure choices.

The complete source in Section 9 contains, literally, a nonnegative integer multiplier vector for every choice in lexicographic order. It combines the four selected rows followed by `O0,O1,O2` into a strictly positive definite matrix. All 72 leading principal minors are checked using exact fractions; their minima by minor order are `(60,17328,857539)`.

For example, failure choice `(0,0,0,0)` uses `(15,0,0,45,0,22,18)` and gives

```text
Q=[[60,-48,16],[-48,660,-808],[16,-808,1140]],
leading minors=(60,37296,4417728).
```

Thus failure of all four sections would give `tr(MQ)<=0` for a PD Q, contradicting nonzero PSD M. The literal 24-case table and verifier supply the entire finite alternative, not a sampled metric test. No tree on the actual ten-vertex graph has been omitted: this lemma will be used through a geometric cut argument applying to every tree.

## 5. Universal shell theorem with the actual centroid

**Shell theorem.** If an actual uniformly filled convex polytope K satisfies

```text
T subset K subset (1+delta)T,  0<=delta<=1/42,
```

then at its own volume centroid it has U>=2 for every SPD metric, and admits no complete weak rooted tree under any nonzero PSD metric. There is no vertex-count bound for these assertions.

### 5.1 A sharper uniform-centroid estimate

Put `r=1+delta` and let g be the actual centroid of K. For any Euclidean unit v, using the positive part of the linear functional,

```text
v.int_K x
 = int_(K minus T) v.x
 <= int_(rT minus T) (v.x)_+
 = (r^4-1) int_T(v.x)_+.
```

Since T has mean zero and covariance `I/5`,

```text
E_T[(v.X)_+]=E_T|v.X|/2 <= 1/(2sqrt(5)).
```

Division by the actual `Vol(K)>=Vol(T)`, followed by choosing v in the direction of g, yields

```text
|g| <= (r^4-1)/(2sqrt(5)).
```

This is a bound on the true uniformly refilled centroid, not a vertex average or a transported old centroid. The same inclusion and the PSD integrand `xx^T` give

```text
Sigma_K <= E_K[xx^T] <= r^5 I/5.
```

At `delta=1/42`, the scalar on the right is

```text
147008443/653456160 < 1/4.
```

### 5.2 Two separated high-energy halves

Use the four-section lemma for the normalized M. Its two witnesses z have `z^T M z>=m_H`. Since they are two distinct corners and `sum n_i=4`, we have `m_H<=2`.

The plane H is central in the comparison tetrahedron gauge. It is **not assumed to pass through g**. Its section satisfies `K intersect H subset r(T intersect H)`. Write `x=r y` on that section and `f(x)=(x-g)^T M(x-g)`. For either witness,

```text
f(z)-f(x)
 = z^T M z-r^2 y^T M y-2g^T M(z-r y)
 > (7/32)r^2-2(r^2-1)
   -(r^4-1)[sqrt(8/5)+delta sqrt(3/5)].
```

Here `||M||op<=1`, `|z-y|<=sqrt(8)` and `|y|<=sqrt(3)`. The common `g^T M g` term cancels rather than being bounded twice.

Using `sqrt(8/5)<81/64` and `sqrt(3/5)<25/32`, define

```text
G(delta)=(7/32)(1+delta)^2-2[(1+delta)^2-1]
         -[(1+delta)^4-1](81/64+25delta/32).
```

It is decreasing for `delta>=0`, and exact arithmetic gives

```text
G(1/42)=12909517/2091059712 > 0.
```

Therefore each open halfspace of H contains a witness whose energy is strictly greater than the energy of **every point of the actual section**.

Maximize f over K clipped by each closed halfspace. A maximum occurs at a true vertex off H: all newly created clipping vertices lie on the lower-energy section. For SPD M, a same-half neighbor has a strictly negative primitive because

```text
2D_ij=f(v_j)-f(v_i)-|v_j-v_i|_M^2.
```

An edge crossing H also has a strictly negative initial primitive, since it first reaches a lower-energy section point. Each half consequently contains a strict U, proving U>=2.

For PSD M, any weak arrow `D_ij>=0` makes f nondecreasing along its entire edge segment. A complete root path from a half-maximum to a root outside that open half must cross the lower-energy section, which is impossible. This also handles a root on H and includes every zero primitive or coincident projected endpoint. Thus every complete weak rooted alternative is excluded.

### 5.3 Uniform actual-tree and covariance margins

For at most ten true vertices, suppose every selected tree arrow satisfied

```text
D_ij >= -(1/4096) tr(M).
```

After `tr M=1`, energy decreases by at most `2/4096` on any whole edge or traversed fraction. A simple root path has at most nine edges. But

```text
G(1/42)-18/4096 = 14881159/8364238848 > 0.
```

Starting at the maximum of a half whose interior does not contain the root again makes the first section crossing impossible. Hence every tree has at least one selected arrow strictly below `-tr(M)/4096`.

Separation of the convex hull of its negative arrow matrices from the open cone `I/4096+PD` now gives probability weights, depending on the actual body and tree but not on M, with

```text
Q_tree=-sum_e w_e sym[(v_i-g)(v_j-v_i)^T] > I/4096
       > Sigma_K/1024.
```

Equivalently, the weighted forward primitive is below `-tr(M Sigma_K)/1024`. The covariance formulation survives undoing the affine normalization by congruence. This is an analytic existence theorem for the complete selected tree, not a computed library of actual graph stresses.

For rational geometry these weights are reconstructible by enumerating dyadic probability vectors on that tree's edges and checking the three leading minors of `Q_tree-I/4096`. Strict separation guarantees termination. No bound on that enumeration's size is claimed.

The proof also preserves a useful centre-aware sufficient test: before replacing g by its uniform envelope, it suffices that

```text
(7/32)r^2-2(r^2-1) > 2|g|[sqrt(8)+delta sqrt(3)].
```

Here g must be the actual centroid in the comparison gauge. A failure is only failure of this sufficient test.

## 6. Transfer to the full cut-stack chart

The contained comparison tetrahedron is

```text
T_a^R=conv(R0,R1,R2,S),
```

**not** the older base-and-stack tetrahedron `conv(B0,B1,B2,S)`.

Set

```text
o=(1-beta,beta,0),
v_i=u_i+s o_i,
H=s+sum_i q_i v_i,
A_j=p_j(1+sum_i o_i q_i)+q_j.
```

The exact barycentric coordinates in ordered `(R0,R1,R2,S)` are

```text
lambda_S(B_j)=d_s q_j/H,
lambda_Ri(B_j)=e_i[delta_ij-v_i q_j/H],
lambda_S(L_j)=d_s A_j/(H d_j),
lambda_Ri(L_j)=(e_i/d_j)[delta_ij+p_j o_i-v_i A_j/H].
```

The R and S rows are unit rows. Every row reconstructs its literal vertex and sums to one; its S-coordinate is nonnegative. Also `6Vol(T_a^R)=H/(d_s e0 e1 e2)>0`. These inherited identities are used without changing their comparison tetrahedron. fileciteturn8file0L48-L83

Let eta(a) be the largest negative part of all these barycentric coordinates. The bracket signs are independent of a, and

```text
e_i'=-q_i,
(e_i/d_j)'=-(q_i+p_j+p_j q_i)/d_j^2 <0.
```

Thus eta is nonincreasing on the admissible pencil. This transports **inclusion only**; all uniform centres and physical arrows remain those of the newly refilled body. fileciteturn8file0L85-L100

Map the four comparison vertices affinely to z0,z1,z2,z3. Since their sum is zero, coordinates bounded below by `-eta` imply

```text
T subset K subset (1+4eta)T.
```

The **new pointwise threshold is `eta(a)<=1/168`**, rather than the parent's `1/32768`. Passing at one a certifies every later admissible a. General pointwise use requires `Delta>0` and every denominator positive; its left endpoint is `-1/max(s,p0,p1,p2)`. A test at one fixed weight does not, by itself, certify the complete weight triangle.

### 6.1 Whole-pencil estimate and Theorem A

Put `r_p=max p_j/s<1` and `ell=Q/s+Q`. Throughout the maximal pencil,

```text
d_j>=1-r_p,  e_i<=1+ell.
```

With

```text
C_j=(s q_j-p_j sum_i u_i q_i)/H,
```

the bracket in lambda_Ri(L_j) is

```text
delta_ij-u_i A_j/H-o_i C_j,
A_j/H<=p_j/s+q_j/s,  max(C_j,0)<=q_j.
```

Consequently, uniformly in beta, the entire weight triangle and the whole pencil,

```text
eta(a) <= (1+ell)(r_p+ell)/(1-r_p).
```

This gives the broader sufficient full-pencil domain

```text
r_p<1,  (1+ell)(r_p+ell)/(1-r_p) <= 1/168.
```

For Theorem A take `epsilon=1/512`; then `r_p<=epsilon`, `ell<=2epsilon`, and

```text
eta(a) <= 3epsilon(1+2epsilon)/(1-epsilon)
       =771/130816 < 1/168.
```

The shell theorem proves the entire asserted pencil. No numerical pencil certificate or nine-vertex theorem is used.

### 6.2 Large-left estimate and Theorem B

For positive a,

```text
p_j/[s(1+a p_j)] <=1/(a s),
```

and the same barycentric identities give

```text
eta(a) <= (1+Q)[1/(a s)+Q/s+Q].
```

Under Theorem B and `a s>=256`, this is at most

```text
(1+1/1024)(1/256+1/512)=3075/524288 <1/168.
```

Moreover `s(1+1/Q)>1024`, so `(256/s)/(1+1/Q)<1/4`. The tail is nonempty and longer than three quarters of the positive pencil. The condition `p_j<s` is retained to guarantee the actual stack geometry for **every** weight.

## 7. Exact controls and a meaningful limit of the method

The continuous result comes from the preceding proof and the complete 24-case matrix alternative, not from finite geometry sampling. The exact auditor additionally reconstructs thirteen new bodies, including all three weight edges and corners.

For the first eleven, put

```text
epsilon=1/512, beta=2/5, s=1,
p=epsilon(1/2,2/3,3/4), q=epsilon(1,3/4,1/2).
```

Five use `u=(1/5,2/5,2/5)` at `a=-1/2,0,1,256,512`. Six use `a=256` and respectively

```text
u=(0,2/5,3/5),(2/5,0,3/5),(2/5,3/5,0),
  (1,0,0),(0,1,0),(0,0,1).
```

The twelfth has

```text
beta=1/2, s=1, p=q=(1/512,1/512,1/512),
u=(1/3,1/3,1/3), a=513/2.
```

After the comparison normalization, every B_j has squared distance greater than 1 from every tetrahedral corner, but

```text
eta=855/1052672,
lambda(B2)=(-855/1052672,-855/1052672,263511/526336,515/1028).
```

It is a genuine near-edge refinement, not a four-corner cluster. The thirteenth has

```text
beta=2/5, s=1, p=(1/2,2/3,3/4),
q=(1/1024,1/2048,3/4096), u=(1/5,2/5,2/5), a=256.
```

Every control is uniformly refilled, affinely normalized by `(R0,R1,R2,S)->(z0,z1,z2,z3)`, and centred at its actual transformed centroid. The single physical pair is

```text
M=[[7,1,2],[1,5,-1],[2,-1,6]], N=M^(-1).
```

All thirteen have **strict `(S,U,H)=(4,4,6)`, physical weak count zero and no zero primitive**. The audit performs **836 exact genuine-edge primitive checks**. The seven interior controls have 10/17/9, the three weight-edge controls 10/16/8, and the three weight corners 9/14/7. All thirteen have eta larger than the old `1/32768` shell threshold. None is a U1 or class110 survivor.

Each true hull is independently reconstructed from supporting planes; active-normal rank removes redundant labels, maximal cycles and genuine edges are rebuilt, and an origin-to-true-facet fan checks volume, centroid and covariance against the seven actual tetrahedra. Raw-to-normalized moment transport is also checked. The report retains every normalized coordinate, barycentric row, true feature and four-primitive edge packet.

**Failed stronger four-section claim.** Attempting to replace `7/32` by `1/4` for these same four section types fails. On the genuine regular tetrahedron at centroid zero, take

```text
M=(1/800)[[410,190,190],[190,221,190],[190,190,169]].
```

It is SPD with trace one and leading minors `(41/80,5451/64000,15109/51200000)`. Its corner norms are `(97/40,21/40,21/40,21/40)`, and the four gaps are exactly

```text
(199/800, 1/80, 1/80, 79/320),
```

all below `1/4`. This is a counterexample to that stronger **fixed-four-section constant**, not a U1 body, not a counterexample to another adaptive section family, and not proof that `7/32` or `1/42` is optimal.

## 8. Recovery, verification status and exact pins

The complete readable acceptance source below is `large_shell.py`: **14141 bytes**, SHA-256 `795697874480e3c429b6bc4e2824e6b89f943de9eda3c1d4811791f1f02039f0`. It contains all 24 multiplier rows, the exact failed-quarter control, every new actual-body input, hull/moment routines and complete same-inverse mechanical audit. No external input, cache, parent import or encoded-source patch is required.

Exact acceptance stack: **CPython 3.13.5, standard library only, assertions enabled**. Save the code with LF line endings and a final newline, then run

```text
python -B -S large_shell.py > large_shell_stdout.txt
sha256sum large_shell.py large_shell_report.json large_shell_stdout.txt
```

Expected outputs:

```text
large_shell_report.json: 136225 bytes
SHA256 9b89ebf2e2371cfdf9d0ffb736b97ceeb9d2f857bc6ea5cc8a9dc16aff1277d8
large_shell_stdout.txt: 1067 bytes
SHA256 9813b38e65986967558ee57070f4116a3d7d67f3ca5ae0fcf23408f001598f76
```

Expected final stdout markers:

```text
FOUR_CENTRAL_SECTIONS_24_PD_ALTERNATIVES_PASS
SHELL_1OVER42_ACTUAL_CENTROID_AND_GAMMA_PASS
CUT_STACK_FULL_1OVER512_PENCIL_AND_1OVER1024_TAIL_PASS
ALL_13_TRUE_HULLS_REFILLS_AND_836_PRIMITIVES_PASS
```

Normal execution, a fresh-directory source-only execution, and a further reconstruction extracting the source solely from this Markdown handoff were all completed. Source, report and stdout matched their exact pins; the last reconstruction returned `MARKDOWN_ONLY_RECOVERY_ALL_EXACT_PINS_PASS`. The analytical argument plus exact finite matrix alternative is not a proof-assistant formalization.

The optional discovery source in Section 10 is included because numerical eigenvector-cut linear programming materially located the new integer weights. Its only input is `7/32`; the acceptance source does not trust its floating calculations. Observed discovery stack: CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, one OpenBLAS thread. Different numerical stacks may select different weights; only exact verified matrices constitute a certificate.

## 9. Complete standalone exact acceptance source

```python
#!/usr/bin/env python3
"""Exact four-section shell certificate and actual cut-stack controls; stdlib only.
Run: python -B -S large_shell.py
The continuous proof is analytic; finite controls do not replace it.
"""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import sys

Z = [(F(1),F(1),F(1)), (F(1),F(-1),F(-1)),
     (F(-1),F(1),F(-1)), (F(-1),F(-1),F(1))]
CELLS = [(0,1,2,5),(0,1,4,5),(0,3,4,5),(3,4,5,9),
         (0,1,2,8),(0,1,7,8),(0,6,7,8)]
M = [[F(7),F(1),F(2)], [F(1),F(5),F(-1)], [F(2),F(-1),F(6)]]
ZERO = (F(0),F(0),F(0))

def add(x,y): return tuple(a+b for a,b in zip(x,y))
def sub(x,y): return tuple(a-b for a,b in zip(x,y))
def scale(a,x): return tuple(a*b for b in x)
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def cross(x,y): return (x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])
def det(A): return dot(A[0],cross(A[1],A[2]))
def mv(A,x): return tuple(dot(r,x) for r in A)
def transpose(A): return list(map(list,zip(*A)))
def mm(A,B): return [[dot(r,c) for c in zip(*B)] for r in A]
def outer(x,y): return [[a*b for b in y] for a in x]
def matadd(A,B): return [[A[i][j]+B[i][j] for j in range(3)] for i in range(3)]
def matscale(a,A): return [[a*x for x in r] for r in A]
def zero_matrix(): return [[F(0) for _ in range(3)] for _ in range(3)]
def symouter(x,y): return matscale(F(1,2),matadd(outer(x,y),outer(y,x)))
def inverse(A):
    n=len(A)
    B=[list(r)+[F(i==j) for j in range(n)] for i,r in enumerate(A)]
    for j in range(n):
        k=next((k for k in range(j,n) if B[k][j]),None)
        if k is None: raise ValueError('singular matrix')
        B[j],B[k]=B[k],B[j]
        z=B[j][j]; B[j]=[x/z for x in B[j]]
        for i in range(n):
            if i!=j:
                z=B[i][j]; B[i]=[x-z*y for x,y in zip(B[i],B[j])]
    return [r[n:] for r in B]
def rank(A):
    B=[list(r) for r in A]; r=0
    for j in range(3):
        k=next((k for k in range(r,len(B)) if B[k][j]),None)
        if k is None: continue
        B[r],B[k]=B[k],B[r]; z=B[r][j]; B[r]=[x/z for x in B[r]]
        for i in range(len(B)):
            if i!=r:
                z=B[i][j]; B[i]=[x-z*y for x,y in zip(B[i],B[r])]
        r+=1
    return r
def minors(A): return [A[0][0],A[0][0]*A[1][1]-A[0][1]**2,det(A)]
def six(T): return abs(det([sub(T[i],T[0]) for i in (1,2,3)]))
def moments(tets):
    D=F(0); J=ZERO; W=zero_matrix()
    for T in tets:
        w=six(T); assert w>0
        C=tuple(sum(x[j] for x in T) for j in range(3))
        Q=zero_matrix()
        for x in T: Q=matadd(Q,outer(x,x))
        D+=w; J=add(J,scale(w,C)); W=matadd(W,matscale(w,matadd(outer(C,C),Q)))
    g=scale(1/(4*D),J)
    cov=matadd(matscale(1/(20*D),W),matscale(-1,outer(g,g)))
    return D,g,cov

def core_certificate():
    """24 exhaustive failure choices for four central sections, after norm sorting."""
    I=[[F(i==j) for j in range(3)] for i in range(3)]
    P=[outer(z,z) for z in Z]
    E=[[[F(i==j==k) for j in range(3)] for i in range(3)] for k in range(3)]
    def row(A,B): return matadd(matscale(32,matadd(A,matscale(-1,B))),matscale(-7,I))
    C=[[row(P[2],E[k]) for k in (1,2)],
       [row(P[1],E[k]) for k in (0,2)],
       [row(P[1],E[k]) for k in (0,1)],
       [row(P[1],outer(scale(F(1,4),add(Z[0],scale(3,Z[j]))),
                       scale(F(1,4),add(Z[0],scale(3,Z[j]))))) for j in (1,2,3)]]
    O=[matscale(32,matadd(P[j+1],matscale(-1,P[j]))) for j in range(3)]
    W=[
      (15,0,0,45,0,22,18),(0,13,0,38,0,34,15),(14,0,0,42,0,23,21),
      (15,0,0,45,0,22,18),(0,13,0,38,0,34,15),(14,0,0,42,0,23,21),
      (15,0,0,45,0,22,18),(0,5,8,39,0,34,14),(14,0,0,42,0,23,21),
      (15,0,0,45,0,22,18),(0,132,0,395,0,341,132),(14,0,0,42,0,23,21),
      (151,0,0,452,0,226,171),(152,0,0,455,0,241,152),(0,123,0,368,0,326,184),
      (151,0,0,452,0,226,171),(152,0,0,455,0,241,152),(0,5,7,37,0,32,19),
      (151,0,0,452,0,226,171),(152,0,0,455,0,241,152),(0,0,123,368,0,326,184),
      (151,0,0,452,0,226,171),(152,0,0,455,0,241,152),(0,0,123,368,0,326,184)]
    records=[]
    choices=list(product(range(2),range(2),range(2),range(3)))
    assert len(W)==len(choices)==24
    for choice,w in zip(choices,W):
        R=[C[k][j] for k,j in enumerate(choice)]+O
        Q=zero_matrix()
        assert min(w)>=0 and sum(w)>0
        for weight,A in zip(w,R): Q=matadd(Q,matscale(weight,A))
        mi=minors(Q); assert min(mi)>0
        records.append({'choice':choice,'weights':w,'matrix':Q,'minors':mi})
    delta=F(1,42); b=F(7,32); r=1+delta; gamma=F(1,4096)
    # sqrt(8/5)<81/64, sqrt(3/5)<25/32.
    assert F(81,64)**2>F(8,5) and F(25,32)**2>F(3,5)
    gap=b*r*r-2*(r*r-1)-(r**4-1)*(F(81,64)+F(25,32)*delta)
    assert gap==F(12909517,2091059712) and gap>18*gamma
    assert r**5/5<F(1,4)
    eps=F(1,512); bound=3*eps*(1+2*eps)/(1-eps)
    assert bound<F(1,168)
    tail=(1+F(1,1024))*(F(1,256)+F(1,512))
    assert tail<F(1,168)
    # A genuine regular-tetrahedron metric refutes the stronger four-cut 1/4 claim.
    fail=[[F(x,800) for x in row] for row in ((410,190,190),(190,221,190),(190,190,169))]
    assert min(minors(fail))>0 and sum(fail[i][i] for i in range(3))==1
    n=[dot(z,mv(fail,z)) for z in Z]
    assert n==[F(97,40),F(21,40),F(21,40),F(21,40)]
    section_points=[[(F(0),F(1),F(0)),(F(0),F(0),F(1))],
                    [(F(1),F(0),F(0)),(F(0),F(0),F(1))],
                    [(F(1),F(0),F(0)),(F(0),F(1),F(0))],
                    [scale(F(1,4),add(Z[0],scale(3,Z[j]))) for j in (1,2,3)]]
    gaps=[n[k]-max(dot(x,mv(fail,x)) for x in S)
          for k,S in zip((2,1,1,1),section_points)]
    assert gaps==[F(199,800),F(1,80),F(1,80),F(79,320)] and max(gaps)<F(1,4)
    return {'core_gap':b,'failure_cases':records,'delta':delta,'transferred_gap':gap,
            'gamma':gamma,'covariance_upper_scalar':r**5/5,
            'whole_pencil_eta_bound':bound,'tail_eta_bound':tail,
            'four_cut_quarter_countermetric':fail,'four_cut_quarter_gaps':gaps}

def raw_chart(beta,s,p,q,u,a):
    assert 0<beta<1 and s>0 and min(p+q)>0 and min(u)>=0 and sum(u)==1
    assert s>dot(u,p)
    b=[(F(0),-beta,F(0)),(F(0),1-beta,F(0)),(F(0),F(0),F(1))]
    d=[1+a*x for x in p]; e=[1+(1-a)*x for x in q]; ds=1+a*s
    assert min(d+e+[ds])>0
    X=b+[scale(1/d[j],(-p[j],b[j][1],b[j][2])) for j in range(3)]
    X += [scale(1/e[j],(q[j],b[j][1],b[j][2])) for j in range(3)]
    ub=tuple(sum(u[j]*b[j][k] for j in range(3)) for k in range(3))
    X += [scale(1/ds,(-s,ub[1],ub[2]))]
    prod_d=d[0]*d[1]*d[2]
    weights=[p[2]/d[2],p[1]/(d[1]*d[2]),p[0]/prod_d,
             (s-dot(u,p))/(ds*prod_d),q[2]/e[2],q[1]/(e[1]*e[2]),q[0]/(e[0]*e[1]*e[2])]
    for C,w in zip(CELLS,weights): assert six([X[i] for i in C])==w
    o=(1-beta,beta,F(0)); v=add(u,scale(s,o))
    H=s+dot(q,v); zeta=dot(o,q)
    bary=[]
    for j in range(3):
        bary.append(tuple([e[i]*(F(i==j)-v[i]*q[j]/H) for i in range(3)]+[ds*q[j]/H]))
    for j in range(3):
        A=p[j]*(1+zeta)+q[j]
        bary.append(tuple([e[i]*(F(i==j)+p[j]*o[i]-v[i]*A/H)/d[j] for i in range(3)]+[ds*A/(H*d[j])]))
    bary += [tuple(F(i==j) for i in range(4)) for j in range(3)]
    bary += [(F(0),F(0),F(0),F(1))]
    vertices=[X[6],X[7],X[8],X[9]]
    for x,lam in zip(X,bary):
        assert sum(lam)==1 and lam[3]>=0
        assert x==tuple(sum(lam[i]*vertices[i][j] for i in range(4)) for j in range(3))
    K=[tuple(sum(lam[i]*Z[i][j] for i in range(4)) for j in range(3)) for lam in bary]
    eta=max(F(0),-min(t for lam in bary for t in lam))
    assert eta<=F(1,168)
    W=transpose([sub(X[i],X[9]) for i in (6,7,8)])
    A=mm(transpose([sub(Z[i],Z[3]) for i in range(3)]),inverse(W))
    shift=sub(Z[3],mv(A,X[9]))
    assert K==[add(mv(A,x),shift) for x in X]
    assert six(vertices)==H/(ds*e[0]*e[1]*e[2])
    rawD,rawg,rawcov=moments([[X[i] for i in C] for C in CELLS])
    D,g,cov=moments([[K[i] for i in C] for C in CELLS])
    assert D==abs(det(A))*rawD and g==add(mv(A,rawg),shift)
    assert cov==mm(mm(A,rawcov),transpose(A))
    return K,D,g,cov,bary,eta

def hull(K):
    supports={}
    for i,j,k in combinations(range(len(K)),3):
        n=cross(sub(K[j],K[i]),sub(K[k],K[i]))
        if n==ZERO: continue
        h=dot(n,K[i]); signs=[h-dot(n,x) for x in K]
        if min(signs)<0 and max(signs)>0: continue
        if max(signs)<=0: n=scale(-1,n); h=-h
        div=abs(next(x for x in n if x)); n=scale(1/div,n); h/=div
        supports[tuple(n)+(h,)]=(n,h)
    S=sorted(supports.values(),key=lambda nh:tuple(nh[0])+(nh[1],))
    active=[{i for i,(n,h) in enumerate(S) if dot(n,x)==h} for x in K]
    true=[j for j,A in enumerate(active) if rank([S[i][0] for i in A])==3]
    E=[(i,j) for i,j in combinations(true,2) if len(active[i]&active[j])>=2]
    facets=[]; fan=[]
    for f,(n,h) in enumerate(S):
        V=[i for i in true if f in active[i]]
        adjacency={i:sorted(j for j in V if (min(i,j),max(i,j)) in E) for i in V}
        assert all(len(v)==2 for v in adjacency.values())
        C=[min(V),adjacency[min(V)][0]]
        while len(C)<len(V): C.append(next(j for j in adjacency[C[-1]] if j!=C[-2]))
        assert C[0] in adjacency[C[-1]]
        if dot(cross(sub(K[C[1]],K[C[0]]),sub(K[C[2]],K[C[0]])),n)<0:
            C=[C[0]]+list(reversed(C[1:]))
        facets.append(C)
        for k in range(1,len(C)-1): fan.append([ZERO,K[C[0]],K[C[k]],K[C[k+1]]])
    assert len(true)-len(E)+len(S)==2
    return S,active,true,E,facets,fan

def mechanics(K,g,S,active,true,E):
    X=[sub(x,g) for x in K]; N=inverse(M)
    poles=[scale(1/(h-dot(n,g)),n) for n,h in S]
    assert min(minors(M))>0
    P={(i,j):dot(X[i],mv(M,sub(X[j],X[i]))) for e in E for i,j in (e,e[::-1])}
    dual_edges={tuple(sorted(active[i]&active[j])) for i,j in E}
    assert all(len(t)==2 for t in dual_edges)
    Q={(i,j):dot(poles[i],mv(N,sub(poles[j],poles[i]))) for e in dual_edges for i,j in (e,e[::-1])}
    U=[i for i in true if all(v<0 for (a,b),v in P.items() if a==i)]
    stable=[i for i in range(len(S)) if all(v<0 for (a,b),v in Q.items() if a==i)]
    saddles=[]; weak={}; rows=[]; physical_zero=0
    for a,b in E:
        i,j=sorted(active[a]&active[b]); r=[P[a,b],P[b,a],Q[i,j],Q[j,i]]
        rows.append({'edge':[a,b],'facets':[i,j],'primitives':r})
        if max(r)<0: saddles.append([a,b])
        if max(r)<=0 and 0 in r:
            physical_zero+=r.count(0)
            if r[0]==0: point=X[a]
            elif r[1]==0: point=X[b]
            else:
                k=i if r[2]==0 else j
                point=scale(1/dot(poles[k],mv(N,poles[k])),mv(N,poles[k]))
            weak.setdefault(point,[]).append([a,b])
    zeros=sum(v==0 for v in list(P.values())+list(Q.values()))
    assert len(stable)+len(U)-len(saddles)==2
    return {'strict_SUH':[len(stable),len(U),len(saddles)],'U_labels':U,
            'S_facets':stable,'saddles':saddles,'weak_points':len(weak),
            'zero_primitives':zeros,'harmless_zeros':zeros-physical_zero,'edge_rows':rows}

def control(name,beta,s,p,q,u,a):
    K,D,g,cov,bary,eta=raw_chart(beta,s,p,q,u,a)
    S,active,true,E,facets,fan=hull(K)
    assert moments(fan)==(D,g,cov)
    census=mechanics(K,g,S,active,true,E)
    assert census['strict_SUH'][1]>=2
    neg=sum(x==0 for x in u)
    expected=[10,17,9] if neg==0 else ([10,16,8] if neg==1 else [9,14,7])
    assert [len(true),len(E),len(facets)]==expected
    distances=[min(dot(sub(K[j],z),sub(K[j],z)) for z in Z) for j in range(3)]
    return {'name':name,'input':{'beta':beta,'s':s,'p':p,'q':q,'u':u,'a':a},
            'vertices':K,'true_labels':true,'facets':facets,'edges':E,
            'f_vector':expected,'volume':D/6,'centroid':g,'covariance':cov,
            'barycentric_rows':bary,'eta':eta,'base_nearest_corner_distance_squared':distances,
            'metric':M,'census':census}

def encode(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [encode(v) for v in x]
    return x

def main():
    eps=F(1,512); beta=F(2,5); s=F(1)
    p=(eps/2,2*eps/3,3*eps/4); q=(eps,3*eps/4,eps/2)
    u=(F(1,5),F(2,5),F(2,5)); controls=[]
    for name,a in [('negative',F(-1,2)),('zero',F(0)),('one',F(1)),
                   ('positive_middle',F(256)),('right_near_horizon',F(512))]:
        controls.append(control(name,beta,s,p,q,u,a))
    weights=[(0,F(2,5),F(3,5)),(F(2,5),0,F(3,5)),(F(2,5),F(3,5),0),
             (1,0,0),(0,1,0),(0,0,1)]
    for j,w in enumerate(weights):
        controls.append(control('weight_boundary_'+str(j),beta,s,p,q,tuple(map(F,w)),F(256)))
    controls.append(control('interior_edge_refinement',F(1,2),s,(eps,)*3,(eps,)*3,
                            (F(1,3),)*3,F(513,2)))
    assert min(controls[-1]['base_nearest_corner_distance_squared'])>1
    controls.append(control('large_left_tail',beta,s,(F(1,2),F(2,3),F(3,4)),
                            (F(1,1024),F(1,2048),F(3,4096)),u,F(256)))
    for C in controls:
        assert C['census']['strict_SUH']==[4,4,6]
        assert C['census']['weak_points']==C['census']['zero_primitives']==0
    assert sum(4*len(C['edges']) for C in controls)==836
    report=encode({'schema':'CUT_STACK_LARGE_SHELL_1OVER512_V1',
                   'parent':'minimum-0294',
                   'proof_checks':core_certificate(),'controls':controls})
    out=(json.dumps(report,sort_keys=True,separators=(',',':'))+'\n').encode()
    Path('large_shell_report.json').write_bytes(out)
    for C in controls:
        print(C['name'],'f='+str(C['f_vector']),'SUH='+str(C['census']['strict_SUH']),
              'weak='+str(C['census']['weak_points']),'zeros='+str(C['census']['zero_primitives']))
    print('REPORT_BYTES',len(out))
    print('REPORT_SHA256',hashlib.sha256(out).hexdigest())
    print('PYTHON',sys.version.split()[0])
    print('FOUR_CENTRAL_SECTIONS_24_PD_ALTERNATIVES_PASS')
    print('SHELL_1OVER42_ACTUAL_CENTROID_AND_GAMMA_PASS')
    print('CUT_STACK_FULL_1OVER512_PENCIL_AND_1OVER1024_TAIL_PASS')
    print('ALL_13_TRUE_HULLS_REFILLS_AND_836_PRIMITIVES_PASS')

if __name__=='__main__': main()
```

## 10. Complete optional discovery source

`fourcuts.py` is 2205 bytes, SHA-256 `70d2e0005e95cd69b7d781a759ecf7ab9dc328d367b0f8b201ef5bd727f8358a`. Run

```text
OPENBLAS_NUM_THREADS=1 python fourcuts.py 7/32
```

The expected terminal line is `GOOD 24 BOUND 7/32`. The `rows` function computes the actual common scale by `lcm(16,b.denominator)`, which is 32 for this input; the earlier top-level comment about scale 16 is not the operative rule. Rounding is accepted only after positive exact integer principal minors. The literal accepted table is already preserved in the standalone source above.

```python
from fractions import Fraction as F
from itertools import product
import numpy as np
from scipy.optimize import linprog
Z=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],dtype=int)
ZZ=np.einsum('ki,kj->kij',Z,Z)
D=[np.outer(e,e) for e in np.eye(3,dtype=int)]
# all coefficients scaled by 16, so b in multiples of 1/16

def rows(b):
    # Rational b: scale all exact coefficients to lcm(16,b.denominator).
    from math import lcm
    sc=lcm(16,b.denominator)
    A=[[sc*(ZZ[2]-D[k])-int(sc*b)*np.eye(3,dtype=int) for k in (1,2)],
       [sc*(ZZ[1]-D[k])-int(sc*b)*np.eye(3,dtype=int) for k in (0,2)],
       [sc*(ZZ[1]-D[k])-int(sc*b)*np.eye(3,dtype=int) for k in (0,1)],
       [sc*ZZ[1]-(sc//16)*np.outer(Z[0]+3*Z[j],Z[0]+3*Z[j])-int(sc*b)*np.eye(3,dtype=int) for j in (1,2,3)]]
    return A,[sc*(ZZ[i+1]-ZZ[i]) for i in range(3)]

def getcert(C):
    init=np.array([x for x in product((-1,0,1),repeat=3) if x!=(0,0,0)],float)
    U=init/np.linalg.norm(init,axis=1)[:,None]
    for it in range(100):
        A=np.column_stack((-np.einsum('ki,lij,kj->kl',U,C,U),np.ones(len(U))))
        out=linprog(np.r_[np.zeros(len(C)),-1.],A_ub=A,b_ub=np.zeros(len(U)),
                    A_eq=[np.r_[np.ones(len(C)),0]],b_eq=[1],bounds=[(0,None)]*len(C)+[(None,None)],method='highs')
        if not out.success: return None,None
        w=out.x[:-1]; Q=np.einsum('k,kij->ij',w,C); eig,V=np.linalg.eigh(Q)
        if eig[0]>1e-7:
            for den in (10,100,1000,10000,100000,1000000):
                wi=np.round(w*den).astype(int);Qi=np.einsum('k,kij->ij',wi,C)
                a,b,c=map(int,Qi[0]); d,e=map(int,Qi[1,1:]);f=int(Qi[2,2])
                minors=(a,a*d-b*b,a*d*f+2*b*c*e-a*e*e-d*c*c-f*b*b)
                if min(minors)>0: return wi,minors
        if out.x[-1]<1e-8: return None,eig
        U=np.vstack((U,V[:,0]))
    return None,eig

if __name__=='__main__':
    import sys
    b=F(sys.argv[1]) if len(sys.argv)>1 else F(1,8)
    A,O=rows(b)
    good=0
    for idx in product(range(2),range(2),range(2),range(3)):
        C=np.array([A[k][i] for k,i in enumerate(idx)]+O)
        w,mi=getcert(C)
        print(idx,w,mi,flush=True)
        good+=w is not None
    print('GOOD',good,'BOUND',b)
```

## 11. Remaining obstacle and most useful continuation

The parent's `1/1024` small-lateral **positive-pencil gap is closed by Theorem A**, including the entire stack-weight triangle. It should not remain in the unresolved register. Theorem B additionally handles all relative left cuts in `(0,1)` over a majority positive tail at that same right-side scale.

The unresolved domain is now genuinely larger independent left/right geometry outside the explicit eta or centre-aware section criteria. In particular, with unrestricted `p_j/s` and right cuts at `1/1024`, the initial positive interval below `256/s` is not universally settled by Theorem B; individual points can still pass the exact barycentric criterion. Large right coefficients, different comparison simplices and arbitrary eleven-parameter shapes remain separate.

A failed shell estimate or failed finite multiplier search is not a feasible complete rooted system. No genuine U1 or same-inverse joint110 survivor was obtained. The new finite alternatives concern four comparison sections; they are not 24 actual graph stresses or a claimed exhaustive numerical enumeration of 46410 trees. Complete root coverage follows instead from the actual section-crossing proof.

The most useful continuation is to exploit the centre-aware gap before its uniform estimate, or choose a geometry-adaptive contained simplex and section family for the remaining larger cuts. The exact `1/4` four-section obstruction explains why simply raising that particular constant without changing the sections cannot finish the next enlargement.

No whole cut-stack incidence, E17 type or canonical root registry count is subtracted. The global working bracket remains **34 <= C_min <= 622**, and all thirteen new controls are nonattainers. fileciteturn0file0L9-L11

Convenience files, not recovery dependencies: [exact acceptance source](sandbox:/mnt/data/shell2/large_shell.py), [discovery source](sandbox:/mnt/data/shell2/fourcuts.py), [complete exact report](sandbox:/mnt/data/shell2/large_shell_report.json), [complete Markdown handoff](sandbox:/mnt/data/shell2/result_markdown.md).
