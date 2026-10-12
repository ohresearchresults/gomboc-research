# minimum-0242

AI research report · 2026-09-25 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# H5_GLOBAL_TRIANGLE_FOLD_COMPLETE_TREE_DUAL_OBSTRUCTION_V1

## 1. Status and strongest finding

**No new macroscopic actual-shape r exclusion is claimed in this handoff.** The result obtained is a complete-tree dual obstruction to the proposed **global quadratic triangle test**, including its stronger aggregate-weight version. It is not a physical surviving tree cone and does not contradict the accepted full-ratio theorem.

The obstruction persists throughout the macroscopic parameter box

\[
\boxed{15/16\le x\le1,\qquad1/4\le r\le1/2,\qquad0\le\lambda\le1/64.}
\]

On every point of this box, one of two explicit complete primal trees rooted at vertex 2 defeats every positive stress tested by the six **global degree-two triangle Bernstein matrices**. Subdividing only x, r or lambda cannot repair this particular test. The physical `(p,q)` triangle must also be treated differently—for example, subdivided and locally refolded—or the triangle certificate must be changed.

The distinction is important: the box contains the already excluded section **r=1/3**. Thus the obstruction is demonstrably in the sufficient certificate mechanism, not evidence of feasible actual mechanics. A genuine interior control on that section has an explicit rational **SPD coefficient-space witness**, while the same metric violates an actual arrow of the complete tree after the true uniform centroid is used.

The analytic derivation and complete standalone checking source are below. **No terminal pass or report hash was observable for the new source in this execution.** The source is therefore supplied as an unobserved verification unit, not as an executed certificate receipt.

## 2. Actual family and moments

Use the parent's labels, put `s=1-lambda`, and take

\[
\begin{aligned}
B_0&=(1/4,0),&B_1&=(1-3x/4,0),\\
B_2&=(1-p,p),&B_3&=(q,1-q),\\
B_4&=(0,1-3r/4),&B_5&=(0,1/4),&B_6&=(1/16,1/16).
\end{aligned}
\]

Set `z_i=(s B_i,0)` for i=0 through 6, and

\[
z_7=(0,0,1),\quad z_8=(\lambda,0,1),\quad z_9=(0,\lambda,1).
\]

The physical triangle is `p>=0,q>=0,p+q<=1`. Genuine E17 bodies require `0<x,r,lambda<1`, `p,q>0`, `p+q<1`. The maximal outward facets and true edges are

```text
FACES = (
 (6,5,4,3,2,1,0), (8,7,0,1), (7,6,0),
 (1,2,8), (9,8,2,3), (9,3,4),
 (4,5,7,9), (6,7,5), (7,8,9)
)
EDGES = 01,06,07,12,18,23,28,34,39,45,49,56,57,67,78,79,89.
```

The actual basal area and first moments are

\[
\begin{aligned}
A_B&=(31-24xp-24rq)/64,\\
B_x&=509/3072-3xp/8+3x^2p/32+xp^2/8-rq^2/8,\\
B_y&=509/3072-3rq/8+3r^2q/32+rq^2/8-xp^2/8.
\end{aligned}
\]

Consequently the actual uniformly filled solid has

\[
\begin{aligned}
V&=A_Bs^2/3+\lambda/6,\\
J_x&=s^3B_x/4+s^2\lambda(1-3xp/4)/24+\lambda^2/24,\\
J_y&=s^3B_y/4+s^2\lambda(1-3rq/4)/24+\lambda^2/24,\\
J_z&=A_Bs^2/12+\lambda/12+\lambda^2/24,\qquad g=J/V.
\end{aligned}
\]

The recovery unit checks these identities against the genuine eight-tetrahedron apex-0 fan. No basal centroid, frozen centroid, or transported projective centroid is used.

The closed parameter faces retain their genuine limiting meanings. In particular, lambda=0 collapses the three top labels to a pyramid apex; lambda=1 collapses the basal labels to a tetrahedral vertex. The obstruction uses these limits honestly and also has a strictly interior control.

## 3. Which certificate is obstructed

For a nonnegative directed-edge stress w, write

\[
G=-\sum w_{ij}\operatorname{sym}[(Vz_i-J)(z_j-z_i)^T].
\]

Then `sum w D=-tr(MG)/V`, with `D_ij=(z_i-g)^T M(z_j-z_i)`.

Let `f=(-1,1,0)`, and define

\[
\begin{aligned}
I_a&=w_{12}+w_{82},&O_a&=w_{21}+w_{28},\\
I_b&=w_{43}+w_{93},&O_b&=w_{34}+w_{39},\\
a&=w_{23},&b&=w_{32}.
\end{aligned}
\]

The triangle cubic of G is

\[
\frac{s^4}{32}[-Ap^3-Ep^2q-Fpq^2-Dq^3]ff^T,
\]

where

\[
\begin{aligned}
A&=x(I_a+3O_a+3a+b),\\
D&=r(I_b+3O_b+a+3b),\\
E&=x(O_b+3a+5b-I_b)+4r(O_a+a),\\
F&=r(O_a+5a+3b-I_a)+4x(O_b+b).
\end{aligned}
\]

The global quadratic lower replacement is

\[
-\frac{s^4}{32}(Ap^2+Dq^2+Lpq)ff^T,
\]

with

\[
L=x\max(O_b+3a+5b-I_b,4(O_b+b))
+r\max(4(O_a+a),O_a+5a+3b-I_a).
\]

The difference from G is PSD on the physical triangle. Thus this is a legitimate sufficient lower-bound construction. The issue is its subsequent **degree-two triangle Bernstein test**, not the validity of that lower bound.

For a quadratic triangle polynomial, the coefficient at index `(1,1)` is the functional

\[
\mathcal B_{11}(P)=P_{00}+\frac12(P_{10}+P_{01}+P_{11}).
\]

Here indices refer to ordinary powers of p and q before conversion. This coefficient is not evaluation at a physical point.

## 4. Two complete rooted trees and an aggregate-stress dual

The two trees differ only in the exit selected at vertex 5:

```text
T56 = 0->1, 1->2, 3->2, 4->3, 5->6,
      6->0, 7->0, 8->2, 9->3.

T54 = 0->1, 1->2, 3->2, 4->3, 5->4,
      6->0, 7->0, 8->2, 9->3.
```

Both are complete true-edge trees rooted at 2. This is not a collection of independently selected favorable rows.

For either tree, `O_a=O_b=a=0`, so the aggregate envelope simplifies to

\[
L=x\max(5b-I_b,4b)+r\max(0,3b-I_a)
\ge(4x+3r)b-rI_a.
\]

This inequality is valid for **every nonnegative stress supported on that complete tree**. It proves an obstruction even when the maxima are computed after aggregation; it is not merely a weakness of separately folding individual arrows.

Introduce

\[
\begin{aligned}
v_0&=31s^2/192+\lambda/6,&v_p&=s^2x/8,&v_q&=s^2r/8,\\
h_p&=s^3x(12-3x)/128+s^2\lambda x/32,\\
h_m&=s^3r(12-3r)/128+s^2\lambda r/32,\\
H&=h_p-h_m,&v_*&=v_0-(v_p+v_q)/2,\\
K&=[H+s(v_p-v_q)]/2,&C&=s(h_p+h_m)/2.
\end{aligned}
\]

Set

\[
F_*(t)=v_*t-H/2,\qquad Q_*(t)=-v_*t^2+Kt+C,
\]

and `t0=-s/4`, `t1=-s(1-3x/4)`, `t4=s(1-3r/4)`, `t5=s/4`.

Using the displayed linear lower bound for L, the negative of the folded `(1,1)` coefficient, paired with the PSD matrix `ff^T`, is bounded below by the weighted sum of these nine scalar quantities:

| Arrow | Scalar dual quantity Z |
|---|---|
| `0->1` | `F_*(t0)(t1-t0)` |
| `1->2` | `Q_*(t1)-r s^4/16` |
| `3->2` | `3r s^4/16` |
| `4->3` | `Q_*(t4)` |
| `5->6` | `-t5 F_*(t5)` |
| `5->4` | `(t4-t5)F_*(t5)` |
| `6->0`, `7->0` | `sH/8` |
| `8->2` | `Q_*(-lambda)-r s^4/16` |
| `9->3` | `Q_*(lambda)` |

Choose T54 when `F_*(t5)>=0`, and T56 otherwise. Its selected vertex-5 quantity is then nonnegative. All other quantities are nonnegative throughout the stated box, with the six nontrivial groups strictly positive.

It follows that for every nonzero nonnegative stress on the selected complete tree,

\[
f^T\mathcal B_{11}(G_{\rm lower})f\le0.
\]

Therefore that coefficient cannot be positive definite. A fortiori it cannot satisfy any positive shifted margin required by a nonzero-PSD all-root certificate.

Additional x/r cubic folds do not fix this: their PSD corrections are proportional to p or q, whose `(1,1)` triangle coefficients are positive. They can only decrease the displayed quadratic form. Subdivision or degree elevation in x, r and lambda likewise cannot turn this coefficient function into a pointwise PD function.

**Scope of the obstruction:** it concerns the six global degree-two triangle coefficients, hence the corresponding 90/270-block construction with the physical triangle left intact. It does not exclude triangle subdivision with local refolding, a different triangle degree, the unfurled 150/450-block mechanism, or a different physical stress argument.

## 5. Exact macroscopic bounds

Let `S=(63/64)^4`. On the box, the following are uniform lower bounds:

| Quantity | Strict positive lower bound |
|---|---|
| `Z12` | `S * 23087/12582912` |
| `Z32` | `3S/64` |
| `Z43` | `S * 19411/1572864 - 169/98304` |
| `Z60,Z70` | `S * 861/262144` |
| `Z82` | `S * 1501/65536 - 1/12288 - 1/512` |
| `Z93` | `S * 2925/65536 - 1/12288` |

Every right-hand side is strictly positive. `Z01>=0` because `H>0`, `v_*>0`, `t0<0` and `t1<=t0`. The vertex-5 selector handles its sign without assuming a uniform strict margin.

For the most restrictive incoming arrow, put `t=1-x`, so `0<=t<=1/16`. Its lambda=0 numerator is

\[
768\,[Q_*(t_1)-rs^4/16]_{\lambda=0}
=\frac{14-357t-72t^2-81t^3}{4}
+r(12+81t+27t^2)-\frac{45+27t}{4}r^2.
\]

It increases with r on `[1/4,1/2]`. Substitution of r=1/4 and bounding t by 1/16 gives `23087/16384`, hence the first bound above. Its remaining lambda term is

\[
s^2\lambda\left[\frac{s((x+r)-c(x-r))}{64}-\frac{c^2}{6}\right],\quad c=1-3x/4,
\]

whose bracket is at least `3223/12582912>0`.

The other bounds follow from

\[
\begin{aligned}
X&=x(12-3x)/128\ge2205/32768,\\
R&=r(12-3r)/128\in[45/2048,21/512],\\
X-R&\ge861/32768,\quad
31/192-(x+r)/16\le67/768,\\
K&>0,\quad K<1/8,\quad v_*<1/3,
\end{aligned}
\]

and `5/8<=1-3r/4<=13/16`. The checking unit verifies the polynomial identities and all rational endpoint comparisons, rather than substituting a numerical eigenvalue tolerance.

## 6. Literal rational dual and a genuine interior countercontrol

At `(x,r,lambda)=(1,1/3,0)`, the T56 dual quantities, in its listed order, are exactly

\[
\boxed{(0,25,192,161,1,16,16,88,152)/3072.}
\]

This is a complete-tree certificate of failure of the global coefficient test. The zero is the genuinely collapsed `0--1` edge; this endpoint is not called a ten-vertex body.

For a strictly interior control use

\[
\boxed{x=63/64,\quad r=1/3,\quad\lambda=1/256,\quad p=q=1/4.}
\]

All nine selected coefficient quantities are strictly positive there. The actual body is on the already excluded parent section r=1/3, and all its coordinates and its actual centroid are reconstructed from the formulas above.

A concrete rational SPD coefficient witness is specified without an unspecified tolerance as follows. Let `A_e=sym[(Vz_i-J)(z_j-z_i)^T]`, and define the coefficient matrices

\[
Z_e=\mathcal B_{11}(A_e)+\frac{s^4\ell_e}{64}ff^T,
\]

where `ell32=4x+3r`, `ell12=ell82=-r`, and the other selected `ell_e` are zero. Evaluate at the boxed interior control. Let

\[
m=\min_e f^TZ_ef>0,\quad B=\max_e|\operatorname{tr}Z_e|,
\]

and `a43=f^T A43 f<0`. Set

\[
\epsilon=\min\left(1,\frac{m}{2(1+B)},
\frac{-a_{43}}{2(1+|\operatorname{tr}A_{43}|)}\right),
\]

\[
M=ff^T+\epsilon I,\qquad
M^{-1}=I/\epsilon-ff^T/[\epsilon(\epsilon+2)].
\]

Every datum is rational and fixed by the displayed formulas. This gives `tr(M Z_e)>0` for all nine selected coefficient rows, but

\[
\boxed{D_{43}(M)=\operatorname{tr}(M A_{43})/V<0.}
\]

Thus the same SPD matrix passes the complete artificial coefficient cone and fails the actual complete tree. The true centroid has not been omitted. The recovery unit also computes the actual strict equilibrium census and reports any zero primitives; no unobserved census values are asserted here.

## 7. Recovery and evidence boundary

The exact predecessor remains `minimum-0240`, SHA256 `e9e9cb5a41c6f3efb409de269963537ed1616b34e6847d48b16feac43b6c92b7`. No accepted parent certificate is retracted, and no new all-root r atlas was obtained in this execution.

There is an input-reading limitation as well as an execution limitation: the continuation record preserves the earlier consecutive journal reads through its parent payload, but the renewed reads of the missing beginning and the two new exact source files returned no readable contents in this execution. I cannot attest to a completed fresh reading of all required input. This does not establish that the attachments themselves are inaccessible. The fold convention used in the theorem is therefore explicitly specified above and checked against the actual moment polynomials by the source below.

The following unit requires Python >=3.11, standard-library modules, and assertions enabled. It has no parent-file or sandbox dependency. Save it as `h5_global_fold_obstruction.py` and run

```sh
python -B -S h5_global_fold_obstruction.py output
```

Expected marker, not an observed execution receipt:

```text
H5_GLOBAL_TRIANGLE_FOLD_COMPLETE_TREE_DUAL_OBSTRUCTION_PASS 136 9
```

The script writes a complete exact report containing the interior coordinates, actual centroid, rational SPD metric and inverse, both tree data and coefficient values, the negative physical arrow, and the physical census. It prints the report byte count and SHA256. Those pins are intentionally not invented here.

### Complete standalone verification source

```python
#!/usr/bin/env python3
'''Complete-tree obstruction to the global quadratic triangle Bernstein test.
This is NOT an actual feasible tree. Python >=3.11, stdlib, assertions enabled.
'''
from fractions import Fraction as F
from pathlib import Path
import hashlib, json, sys
if not __debug__ or sys.version_info < (3, 11):
    raise RuntimeError('Python >=3.11 with assertions enabled is required')
N=5
ZERO=(0,)*N
class P:
    def __init__(self,a=0):
        if isinstance(a,P): self.d=a.d.copy()
        elif isinstance(a,dict): self.d={k:F(v) for k,v in a.items() if v}
        else: self.d={} if not a else {ZERO:F(a)}
    def __add__(self,o):
        o=P(o); d=self.d.copy()
        for k,v in o.d.items(): d[k]=d.get(k,F(0))+v
        return P(d)
    __radd__=__add__
    def __neg__(self): return P({k:-v for k,v in self.d.items()})
    def __sub__(self,o): return self+-P(o)
    def __rsub__(self,o): return P(o)+-self
    def __mul__(self,o):
        o=P(o); d={}
        for a,u in self.d.items():
            for b,v in o.d.items():
                k=tuple(a[i]+b[i] for i in range(N))
                d[k]=d.get(k,F(0))+u*v
        return P(d)
    __rmul__=__mul__
    def __truediv__(self,o): return self*(F(1)/F(o))
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        a=P(1)
        for _ in range(n): a=a*self
        return a
    def __eq__(self,o): return self.d==P(o).d
    def val(self,a):
        return sum((v*product(F(a[i])**k[i] for i in range(N))
                    for k,v in self.d.items()),F(0))
def product(xs):
    a=F(1)
    for x in xs:a*=x
    return a
def var(i):
    k=list(ZERO);k[i]=1
    return P({tuple(k):1})
x,r,l,p,q=(var(i) for i in range(N));s=1-l
f=(F(-1),F(1),F(0))
def sub(a,b):return tuple(a[i]-b[i] for i in range(3))
def dot(a,b):return sum(a[i]*b[i] for i in range(3))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def sym(a,b):
    return [[(a[i]*b[j]+a[j]*b[i])/2 for j in range(3)]for i in range(3)]
def form(A,u,v=None):
    if v is None:v=u
    return sum(u[i]*A[i][j]*v[j]for i in range(3)for j in range(3))
def tr(A):return sum(A[i][i]for i in range(3))
def pair(A,B):return sum(A[i][j]*B[i][j]for i in range(3)for j in range(3))
def pc(a,i,j):
    return P({(k[0],k[1],k[2],0,0):v for k,v in a.d.items() if k[3:]==(i,j)})
def bern11(a):
    return pc(a,0,0)+(pc(a,1,0)+pc(a,0,1)+pc(a,1,1))/2
FACES=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
       (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
EDGES=tuple(sorted({tuple(sorted((a,b)))for c in FACES
                    for a,b in zip(c,c[1:]+c[:1])}))
assert len(EDGES)==17
ARROWS=tuple((a,b)for e in EDGES for a,b in (e,e[::-1]))
FAN=((0,1,2,8),(0,9,8,2),(0,9,2,3),(0,9,3,4),
     (0,4,5,7),(0,4,7,9),(0,6,7,5),(0,7,8,9))
B=((P(F(1,4)),P(0)),(1-3*x/4,P(0)),(1-p,p),(q,1-q),
   (P(0),1-3*r/4),(P(0),P(F(1,4))),
   (P(F(1,16)),P(F(1,16))))
z=[(s*a,s*b,P(0))for a,b in B]+[
    (P(0),P(0),P(1)),(l,P(0),P(1)),(P(0),l,P(1))]
area=(31-24*x*p-24*q*r)/64
assert area-F(7,64)==F(3,8)*(1-p-q+p*(1-x)+q*(1-r))
bx=F(509,3072)-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8
by=F(509,3072)-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
V=area*s*s/3+l/6
J=(s**3*bx/4+s*s*l*(1-3*x*p/4)/24+l*l/24,
   s**3*by/4+s*s*l*(1-3*r*q/4)/24+l*l/24,
   area*s*s/12+l/12+l*l/24)
vfan=P(0);jfan=[P(0)for _ in range(3)]
for ids in FAN:
    a,b,c,d=(z[i]for i in ids)
    w=dot(sub(b,a),cross(sub(c,a),sub(d,a)))/6
    vfan+=w
    for k in range(3):jfan[k]+=w*sum(z[i][k]for i in ids)/4
assert vfan==V and all(jfan[k]==J[k]for k in range(3))
U=[tuple(V*a[k]-J[k]for k in range(3))for a in z]
Amat={e:sym(U[e[0]],sub(z[e[1]],z[e[0]]))for e in ARROWS}
# Verify the four triangle cubic matrix identities on all 34 arrows.
identities=0
for edge in ARROWS:
    w={edge:1}
    get=lambda a,b:w.get((a,b),0)
    Ia=get(1,2)+get(8,2);Oa=get(2,1)+get(2,8)
    Ib=get(4,3)+get(9,3);Ob=get(3,4)+get(3,9)
    a=get(2,3);b=get(3,2)
    A=x*(Ia+3*Oa+3*a+b);D=r*(Ib+3*Ob+a+3*b)
    E=x*(Ob+3*a+5*b-Ib)+4*r*(Oa+a)
    H=r*(Oa+5*a+3*b-Ia)+4*x*(Ob+b)
    for ij,T in (((3,0),A),((2,1),E),((1,2),H),((0,3),D)):
        for i in range(3):
            for j in range(3):
                assert pc(-Amat[edge][i][j],*ij)==-s**4*T*f[i]*f[j]/32
        identities+=1
assert identities==136
vp=s*s*x/8;vq=s*s*r/8;v0=31*s*s/192+l/6
hp=s**3*x*(12-3*x)/128+s*s*l*x/32
hm=s**3*r*(12-3*r)/128+s*s*l*r/32
H=hp-hm;ve=v0-(vp+vq)/2;K=(H+s*(vp-vq))/2;C=s*(hp+hm)/2
assert J[1]-J[0]==hp*p-hm*q-s**3*x*p*p/16+s**3*r*q*q/16
Fa=lambda a:ve*a-H/2
Qa=lambda a:-ve*a*a+K*a+C
T56=((0,1),(1,2),(3,2),(4,3),(5,6),(6,0),(7,0),(8,2),(9,3))
T54=tuple((5,4)if e==(5,6)else e for e in T56)
UNION=set(T56)|set(T54)
# On either tree L >= (4x+3r)w32-r(w12+w82).
ell={e:(4*x+3*r if e==(3,2)else -r if e in ((1,2),(8,2))else P(0))
     for e in UNION}
Z={e:[[bern11(Amat[e][i][j])+s**4*ell[e]*f[i]*f[j]/64
       for j in range(3)]for i in range(3)]for e in UNION}
a0=-s/4;a1=-s*(1-3*x/4);a4=s*(1-3*r/4);a5=s/4
expected={(0,1):Fa(a0)*(a1-a0),(1,2):Qa(a1)-r*s**4/16,
 (3,2):3*r*s**4/16,(4,3):Qa(a4),(5,6):Fa(a5)*(-a5),
 (5,4):Fa(a5)*(a4-a5),(6,0):s*H/8,(7,0):s*H/8,
 (8,2):Qa(-l)-r*s**4/16,(9,3):Qa(l)}
for e in UNION:assert form(Z[e],f)==expected[e]
# Symbolic numerator and lambda remainder for the restrictive arrow.
t=1-x;c=1-3*x/4
X=x*(12-3*x)/128;R=r*(12-3*r)/128
A0=F(31,192)-(x+r)/16
Q0=-A0*c*c-c*(X-R+(x-r)/8)/2+(X+R)/2-r/16
NN=(14-357*t-72*t*t-81*t**3)/4+r*(12+81*t+27*t*t)-(45+27*t)*r*r/4
assert 768*Q0==NN
assert expected[(1,2)]==s**4*Q0+s*s*l*(s*((x+r)-c*(x-r))/64-c*c/6)
smin=F(63,64)
bounds={
 '12':smin**4*F(23087,12582912),
 '32':3*smin**4/64,
 '43':smin**4*F(19411,1572864)-F(169,98304),
 '60_and_70':smin**4*F(861,262144),
 '82':smin**4*F(1501,65536)-F(1,12288)-F(1,512),
 '93':smin**4*F(2925,65536)-F(1,12288),
 '12_lambda_bracket':F(3223,12582912)}
assert all(v>0 for v in bounds.values())
assert F(371,64)-F(4443,64)/16-F(45,4)/256-F(81,4)/4096==F(23087,16384)
assert smin*F(995,1024)/64-F(361,4096)/6==F(3223,12582912)
assert -F(67,768)*F(169,256)+F(2653,65536)*F(5,8)+F(2925,65536)==F(19411,1572864)
base=(F(1),F(1,3),F(0),F(0),F(0))
table=[expected[e].val(base)for e in T56]
assert table==[F(v,3072)for v in (0,25,192,161,1,16,16,88,152)]
# Genuine interior body, on the previously excluded r=1/3 section.
pt=(F(63,64),F(1,3),F(1,256),F(1,4),F(1,4))
zz=[tuple(a.val(pt)for a in v)for v in z]
v=V.val(pt);jj=[a.val(pt)for a in J];g=[a/v for a in jj]
assert v>0
for cyc in FACES:
    a,b,c=(zz[i]for i in cyc[:3]);n=cross(sub(b,a),sub(c,a));h=dot(n,a)
    assert any(n)
    for i in range(10):
        slack=h-dot(n,zz[i])
        assert slack==0 if i in cyc else slack>0
    assert h-dot(n,g)>0
T=T54 if Fa(a5).val(pt)>=0 else T56
out=dict(T);assert len(T)==9 and set(out)==set(range(10))-{2}
for i in out:
    j=i
    for _ in range(10):
        if j==2:break
        j=out[j]
    assert j==2
zmat={e:[[a.val(pt)for a in row]for row in Z[e]]for e in T}
rayvalues=[form(zmat[e],f)for e in T]
assert min(rayvalues)>0
actual43=[[a.val(pt)for a in row]for row in Amat[(4,3)]]
ray43=form(actual43,f);assert ray43<0
eta=min(F(1),min(rayvalues)/(2*(1+max(abs(tr(zmat[e]))for e in T))),
        -ray43/(2*(1+abs(tr(actual43)))))
M=[[f[i]*f[j]+(eta if i==j else 0)for j in range(3)]for i in range(3)]
Mi=[[(F(i==j)/eta)-f[i]*f[j]/(eta*(eta+2))for j in range(3)]for i in range(3)]
assert eta>0
assert all(sum(M[i][k]*Mi[k][j]for k in range(3))==F(i==j)
           for i in range(3)for j in range(3))
false_values={str(e):pair(M,zmat[e])for e in T}
assert min(false_values.values())>0
actual_D43=pair(M,actual43)/v;assert actual_D43<0
# Physical census with the same inverse; any zeros are reported.
xx=[sub(a,g)for a in zz];poles=[]
for cyc in FACES:
    a,b,c=(zz[i]for i in cyc[:3]);n=cross(sub(b,a),sub(c,a));h=dot(n,sub(a,g))
    poles.append(tuple(u/h for u in n))
Dp={(i,j):form(M,xx[i],sub(zz[j],zz[i]))for i,j in ARROWS}
De={};Hedges=[]
for a,b in EDGES:
    pairfaces=[k for k,c in enumerate(FACES)if a in c and b in c]
    assert len(pairfaces)==2
    u,w=pairfaces
    De[u,w]=form(Mi,poles[u],sub(poles[w],poles[u]))
    De[w,u]=form(Mi,poles[w],sub(poles[u],poles[w]))
    if all(z<0 for z in (Dp[a,b],Dp[b,a],De[u,w],De[w,u])):
        Hedges.append((a,b))
Ul=[i for i in range(10)if all(v<0 for (a,b),v in Dp.items()if a==i)]
Sl=[i for i in range(9)if all(v<0 for (a,b),v in De.items()if a==i)]
def encode(a):
    if isinstance(a,F):return str(a)
    if isinstance(a,dict):return {str(k):encode(v)for k,v in a.items()}
    if isinstance(a,(list,tuple)):return [encode(v)for v in a]
    return a
report=encode({
 'title':'H5_GLOBAL_TRIANGLE_FOLD_COMPLETE_TREE_DUAL_OBSTRUCTION_V1',
 'domain':{'x':['15/16','1'],'r':['1/4','1/2'],'lambda':['0','1/64'],
           'triangle':'p>=0,q>=0,p+q<=1; obstructed Bernstein index (1,1)'},
 'cubic_matrix_identities':136,'ray':f,
 'base_table_tree':T56,'base_table':table,
 'uniform_positive_bounds':bounds,
 'genuine_control':{'parameters':pt,'vertices':zz,'V':v,'g':g,
 'tree':T,'epsilon':eta,'coefficient_SPD_metric':M,'inverse':Mi,
 'nine_positive_coefficient_values':false_values,
 'physical_D43_negative':actual_D43,
 'strict_S_U_H':(len(Sl),len(Ul),len(Hedges)),
 'stable_facets':Sl,'unstable_vertices':Ul,'saddle_edges':Hedges,
 'zero_primitives':sum(v==0 for v in list(Dp.values())+list(De.values()))},
 'scope':'No new all-root actual-shape exclusion and no actual feasible complete tree.'})
outdir=Path(sys.argv[1]if len(sys.argv)>1 else '.')
outdir.mkdir(parents=True,exist_ok=True)
data=(json.dumps(report,sort_keys=True,indent=2)+'\n').encode()
(outdir/'h5_global_fold_obstruction.json').write_bytes(data)
print('H5_GLOBAL_TRIANGLE_FOLD_COMPLETE_TREE_DUAL_OBSTRUCTION_PASS',136,9)
print('REPORT_BYTES_SHA256',len(data),hashlib.sha256(data).hexdigest())
print('ACTUAL_TREE_REJECTED_D43',actual_D43)
```

## 8. Continuation boundary

The accepted actual all-root domain remains the full parent section r=1/3, its reflected x=1/3 section, and their previously established collars. The present result does not enlarge that actual domain or alter `34<=Cmin<=622`.

It does settle a concrete implementation fork: **a whole-triangle global quadratic test has a complete-tree dual obstruction on a macroscopic free-r box, even on the accepted section.** A failed atlas there must not be interpreted as physical feasibility. The useful next computation is to partition and locally refold the physical triangle in this region, or use the unfurled triangle mechanism, while retaining the complete tree alternatives and moving actual moments.
