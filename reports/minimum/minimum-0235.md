# minimum-0235

Historical AI scientific report · saved 2026-09-25 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# H5_TWO_CORNER_CUT_NINE_BLOCK_REDUCTION_V1

## 1. Result and scope

The useful new basal mechanism is an **exact two-corner-cut representation of the entire admissible (c,p) rectangle**, followed by a rank-one cubic correction that reduces a constant-weight stress test to **nine matrix conditions**. It retains the actual uniformly refilled volume, first moment and covariance. It also works after any fixed projectivity that is positive on the released carrier.

Two concrete continuous results accompany that reduction:

**An unrestricted-metric complete-packet exclusion.** On an explicit off-parent two-dimensional basal family, one complete nine-arrow rooted primal tree has a uniform mean-arrow gap `1/180` for every nonzero PSD metric. The conclusion extends to a specified actual-refill coordinate collar and hence to an explicit eleven-parameter cylinder. This excludes every complete primal/polar packet containing that primal tree, in the exact capped reciprocal hull as well as physically.

**An all-root metric-sector exclusion.** On the same entire basal family, vertices 8 and 9 are both strict U for every SPD metric with `lambda_max(M)/lambda_min(M) <= 3` in the stated coordinate frame. This has a uniform positive margin and an explicit actual-refill collar. It excludes all roots and all complete tree alternatives in that sector.

**No unrestricted all-root basal exclusion, complete U1 surviving cone, or proper110 body is claimed.** Outside the metric sector, the new continuous packet certificate directly covers one of the 48,790 rooted primal trees. The general nine-block mechanism is a way to address the remaining alternatives, not a completed cover of them.

The direct numerical parent remains `minimum-0231`, SHA-256 `caca8b2fe76419e5069d48126156237d6afc6c344dae2add7fdfcced9a7be10b`. Its all-rho, normalized-projectivity `1/25` exclusion on the old basal box is retained unchanged. The earlier H5 packet `D28, D43, E86` also retains its literal three-arrow identity; it is not the complete tree introduced below.

## 2. Geometry: release the whole (c,p) corner rather than enlarge its old box

Use the unchanged H5 outward maximal cycles and true edges:

```
FACES = (
 (6,5,4,3,2,1,0), (8,7,0,1), (7,6,0),
 (1,2,8), (9,8,2,3), (9,3,4),
 (4,5,7,9), (6,7,5), (7,8,9)
)
EDGES = 01,06,07,12,18,23,28,34,39,45,49,56,57,67,78,79,89.
```

The six other basal parameters may be any values satisfying

```
0<b<1, 0<q<1, 0<a<d<1,
u>0, v>0, u/b+v/a<1.
```

Put `r=1-lambda`, initially `0<lambda<1`. Release the corner between vertices 1 and 2 to

```
A=(r,0,0).
```

The released carrier K0 has the nine vertices with labels

```
0=(r*b,0,0), A, 3=(r*q,r*(1-q),0),
4=(0,r*d,0), 5=(0,r*a,0), 6=(r*u,r*v,0),
7=(0,0,1), 8=(lambda,0,1), 9=(0,lambda,1).
```

A is a simple vertex with neighbors 0, 3 and 8. Its true maximal cycles are

```
(6,5,4,3,A,0), (8,7,0,A), (7,6,0),
(9,8,A,3), (9,3,4), (4,5,7,9),
(6,7,5), (7,8,9).
```

Now set

```
z1=A+x*e,  e=z0-A,
z2=A+y*f,  f=z3-A,
0<=x,y<=1,
T=z8.
```

For `0<x,y<1`, this cuts off exactly the tetrahedron

```
conv(A,z1,z2,T)
```

and gives the literal ten-vertex, seventeen-edge, nine-facet H5 body. In the unprojected chart,

```
c=1-(1-b)*x,   p=(1-q)*y.
```

Thus x and y range over **both entire admissible corner-cut coordinates**, not over a larger local approximation to their old intervals.

All four edges of the parameter square are actual lower-vertex boundaries: at x=0 or y=0 the body is K0 with refinement labels; at x=1 or y=1 a cut vertex coincides with the corresponding neighbor. These are not extra E17 bodies. The formulas below include them as closed limits of the same labelled rows.

### Project first, then use physical cut fractions

Apply a fixed projectivity to K0, with positive denominator everywhere on K0, and use the images of A, 0, 3 and 8 in the preceding construction. The same physical cut-square representation remains exact. Uniform refilling is performed after projectivity.

If t is a raw edge fraction from A to an endpoint B, and `dA,dB` are their positive projective denominators, its physical affine fraction is

```
x = t*dB / ((1-t)*dA+t*dB),
t = x*dA / ((1-x)*dB+x*dA).
```

This is a bijection of [0,1]. Consequently the physical x,y square represents all raw c,p values after each such fixed projectivity. Positivity only on a smaller already-cut body is not enough to assert a bounded released carrier; I do not extend this construction across a horizon through K0.

## 3. Actual moments are polynomial before the final centroid division

Let `V0,J0,T20` be the actual volume, first moment and uncentred second moment of the uniformly filled, already-projectively-transformed K0. Define

```
k = -det(e,f,T-A)/6 >= 0,
S = 3*A+T+x*e+y*f,
w = k*x*y.
```

For interior lambda, k is positive. The complete actual moments of the cut body are

```
V  = V0-w,
J  = J0-w*S/4,
T2 = T20 - w*(S*S^T + A*A^T + z1*z1^T + z2*z2^T + T*T^T)/20,
g  = J/V,
C  = T2/V-g*g^T.
```

This is subtraction of one genuine tetrahedron from one genuine uniformly filled carrier. It is not a transported pre-refill centroid, a free mass assignment, or a frozen covariance. The cut formulas also give a direct audit against a true apex fan of the ten labelled vertices.

For the parallel compact chart there is an additional useful closed form. Let

```
Kx=(1-c)*p,  Ky=(1-d)*q,  K0=a*u+b*v,
Ahat=1-Kx-Ky-K0,
Xhat=1-Kx*(2+c-p)-q*q*(1-d)-a*u*u-b*v*(u+b),
Yhat=1-Ky*(2+d-q)-p*p*(1-c)-b*v*v-a*u*(v+a).
```

Then

```
6V  = Ahat*r*r+r*lambda+lambda*lambda,
24Jx = Xhat*r^3+(1-Kx)*r*r*lambda+r*lambda^2+lambda^3,
24Jy = Yhat*r^3+(1-Ky)*r*r*lambda+r*lambda^2+lambda^3,
24Jz = Ahat*r*r+2*r*lambda+3*lambda*lambda.
```

These identities expose the actual basal dependence without dividing Taylor models by a moving volume at every intermediate operation.

## 4. Rank-one cubic correction: three tests in one cut coordinate, nine in two

For nonnegative weights on genuine directed primal edges, write

```
Dij(M)=(zi-g)^T M(zj-zi),
G(x,y)=-sum_(i,j) w_ij*sym[(V*zi-J)*(zj-zi)^T].
```

Here `sym(a*b^T)=(a*b^T+b*a^T)/2`. The exact mechanical identity is

```
sum w_ij*Dij(M) = -tr(M*G(x,y))/V.
```

Let `s_i` and `t_i` be the total outgoing and incoming weights at vertex i. Set

```
B1 = k*(3*s_1+t_1)*e*e^T/4,
B2 = k*(3*s_2+t_2)*f*f^T/4.
```

Both matrices are PSD. Expansion of the actual moment formula gives

```
[x^3*y]G = -B1,
[x*y^3]G = -B2,
```

and there are no other terms of degree greater than two in either variable. Therefore

```
G(x,y) = R(x,y)
       + y*x^2*(1-x)*B1
       + x*y^2*(1-y)*B2,
```

where R is biquadratic. The two displayed corrections are PSD on the entire closed square.

### Why the sign is structural

In one cut coordinate, V is affine decreasing, J has quadratic coefficient `-k*e/4`, and the quadratic coefficient of `sum w*sym[zi*(zj-zi)^T]` is `-s_i*e*e^T`. Their combined cubic coefficient is exactly

```
-k*(3*s_i+t_i)*e*e^T/4.
```

The sign is forced by nonnegative arrow weights and actual tetrahedral mass, not by a numerical observation.

### Three-matrix interval certificate

For any normalized one-cut interval, write `G(t)=G0+G1*t+G2*t^2-C3*t^3`, with `C3>=0`. Then

```
G(t)=(1-t)^2*G(0)
     +2*t*(1-t)*(G(0)+G'(0)/2)
     +t^2*G(1)
     +C3*t^2*(1-t).
```

Thus the three matrices

```
G(0),  G(0)+G'(0)/2,  G(1)
```

being PSD, with both endpoints at least `gamma*I`, imply `G(t)>=gamma*I/2` throughout the closed interval.

### Nine-matrix square certificate

Expand R in the biquadratic Bernstein basis:

```
R(x,y)=sum_(i,j=0..2) binom(2,i)*x^i*(1-x)^(2-i)
                         *binom(2,j)*y^j*(1-y)^(2-j)*H_ij.
```

If all nine H_ij are PSD and the four corner matrices are at least `gamma*I`, then

```
G(x,y) >= gamma*I/4
```

on the entire closed square. The bound follows because the sum of the four corner basis weights is at least 1/4. Exact PSD checks require all principal minors, not just the leading minors.

The same reduction works on every closed subrectangle. If `x=a+dx*s`, `y=b+dy*t`, subtract

```
dx^3*(b+dy*t)*s^2*(1-s)*B1
+dy^3*(a+dx*s)*t^2*(1-t)*B2
```

before forming the nine biquadratic coefficients.

This supplies a smaller exact robust-stress target than treating both broad cut coordinates with second-order Taylor remainders. To cover a box in the other basal, rho or projective variables, the actual moving `V0,J0,e,f,k` must still be enclosed over that box. Centre-only matrices do not certify such a box.

### The remaining mixed term cannot be discarded

Let `h_i=t_i-s_i`. The mixed coefficient is

```
[x^2*y^2]G
 = k*(w_12+w_21-(h_1+h_2)/4)*sym(e*f^T).
```

It survives in R and need not be PSD. This is the concrete remaining interaction after removing the two automatically positive cubic corrections. A coefficientwise power-basis PSD shortcut is therefore invalid. Failure of the nine sufficient matrix conditions is likewise not a surviving physical cone.

## 5. A macroscopic off-parent basal family with a complete-packet exclusion

Fix

```
b=q=a=1/4, d=3/4, u=v=1/16,
lambda=1/2, sigma=tau=0,
0<=x,y<=1.
```

Its literal vertices are

```
z0=(1/8,0,0),
z1=(1/2-3*x/8,0,0),
z2=(1/2-3*y/8,3*y/8,0),
z3=(1/8,3/8,0), z4=(0,3/8,0), z5=(0,1/8,0),
z6=(1/32,1/32,0),
z7=(0,0,1), z8=(1/2,0,1), z9=(0,1/2,1).
```

Equivalently, `c=1-3*x/4`, `p=3*y/4`, and rho=1. The entire interior family is outside the old basal box, already because q=1/4 rather than approximately 2/25.

The actual carrier data are

```
V0=31/256,  k=3/128,
J0=(679/32768,1933/98304,63/1024),
g0=(679/3968,1933/11904,63/124).
```

The cut volume is `k*x*y`; its centroid is

```
(1/2-3*(x+y)/32, 3*y/32, 1/4).
```

In particular `V>=25/256`. Directly bounding the removed mass gives the uniform actual-centroid box

```
9/100 <= gx <= 7/40,
4/25  <= gy <= 21/100,
1/2   <= gz <= 29/50.
```

### The complete labelled tree

Take root U=0 and all weights equal to one on

```
T0 = (1->0, 2->1, 3->2, 4->3, 5->4, 6->5,
      7->0, 8->7, 9->7).
```

This is a complete nine-arrow true-edge rooted primal tree, not a widened version of the old three-row packet.

Its dual complement consists of the primal edges

```
06,18,28,39,49,57,67,89.
```

For polar root S=0 the complete complementary dual tree is

```
1->3, 2->0, 3->4, 4->5, 5->6, 6->7, 7->2, 8->4.
```

The other eight polar-root orientations are obtained by rooting that same dual tree elsewhere. All are excluded by the primal certificate below.

### Uniform all-metric stress

Define the unscaled physical stress `Q=-sum_T0 sym[(zi-g)*(zj-zi)^T]`. A path-energy telescoping identity gives

```
Q = H(g) + (d10*d10^T+d21*d21^T+d32*d32^T)/2,
```

where

```
H(g) = H0+sym(g*L^T),
H0 = ((257/1024,-1/1024,3/16),
      (-1/1024,293/1024,1/4),
      (3/16,1/4,1)),
L=(-9/32,-17/32,-1).
```

The three omitted edge-square matrices are PSD. On the actual-centroid box, rigorous diagonal-dominance lower bounds for H are

```
673/12800, 773/12800, 497/1600,
```

all strictly greater than 1/20. Thus, throughout the entire closed cut square,

```
Q > I/20,
(sum_T0 Dij(M))/9 < -tr(M)/180
```

for every nonzero PSD M.

This is a complete selected-packet exclusion with a substantial uniform gap. It is not an all-root conclusion. On the interior E17 stratum it directly certifies **one rooted primal tree and its nine complementary polar-root pairs**. The other 48,789 rooted primal alternatives, or 439,101 raw complementary pairs, are not covered by this unrestricted-metric certificate.

### Exact reciprocal-hull consequence for this packet

Every body in this family has diameter squared at most 3/2. Scalar variance on an interval gives `C < (3/8)I` for its actual volume covariance. A convex combination of genuine normalized inverse-pair atoms has `Pbar>0` and `tr(C*Pbar)=1`, hence `tr(Pbar)>8/3`.

Therefore the mean of the nine primal rows at Pbar is strictly below

```
-2/135.
```

No complete capped-hull packet containing T0 is feasible, regardless of the caps or number of atoms. This does not exclude a complete packet using another primal tree.

## 6. All-root exclusion for the metric sector kappa(M)<=3

The same actual-centroid calculation can be sharpened to

```
gx >= 439/3200 > 27/200,
gy <= 9/50,
gz >= 63/124,
```

while retaining `gx<=7/40`, `gy>=4/25`, `gz<=29/50`.

For completeness, the x-bound follows by maximizing

```
x*y*(1/2-439/3200-3*(x+y)/32)
```

on the unit square; both partial derivatives are positive, so its maximum is at (1,1). For the y-bound, after taking x=1 the remaining quadratic is bounded by

```
max_(0<=y<=1) y*(9/50-3*y/32)=54/625,
```

which is strictly below `93/100-1933/2304`.

These bounds imply

```
|X8| < 129/200,   |X9| < 5/8.
```

Let `m=(lambda_max(M)+lambda_min(M))/2`. When kappa(M)<=3,

```
||M/m-I||op <= 1/2.
```

The following are lower bounds for `-Dij(I)` and upper bounds for `|Xi|*|zj-zi|`:

| Arrows | Lower Euclidean margin | Product bound |
|---|---:|---:|
| 8->7 | 13/80 | 129/400 |
| 9->7 | 4/25 | 5/16 |
| 8->9 | 97/400 | 9159/20000 |
| 9->8 | 91/400 | 71/160 |
| 8->1, 8->2, 9->3, 9->4 | 21/50 | 387/500 |

Subtracting one half of the last column leaves at least 1/800 in every case. Consequently all eight outgoing true-edge arrows at vertices 8 and 9 satisfy

```
Dij(M)/m < -1/800.
```

**Vertices 8 and 9 are both strict U throughout the whole family for every metric in this sector.** Thus all ten roots, all 48,790 rooted primal trees and all 439,110 raw complementary rooted pairs are excluded there. The conclusion includes incidental weak contacts elsewhere.

This is an eigenvalue-ratio restriction on M in the displayed coordinate frame. It is not the covariance-gauge cap from the global S1/U1 theory; those caps do not imply this sector.

## 7. Actual-refill collars and explicit eleven-parameter domains

These extensions recompute the new body's own centroid.

Suppose a genuine uniformly filled body with the same labelled maximal facet cycles has vertices z'i with

```
max_i |z'i-zi| <= epsilon
```

for a source member of the cut-square family. Its apex-0 fan has eight tetrahedra. Since the source has diameter less than 2, determinant expansion gives

```
sum_t |V't-Vt| <= 33*epsilon
```

for the epsilon values used below. Since `V>=25/256`, the perturbed volume is greater than 1/12. First-moment comparison then gives

```
|g'-g| <= 793*epsilon,
max_i |X'i-Xi| <= 794*epsilon = delta.
```

For every nonzero PSD M,

```
|D'ij(M)-Dij(M)| <= (6*delta+2*delta^2)*tr(M).
```

**Unrestricted-metric packet collar.** With `epsilon=1/2000000`, the error is less than `tr(M)/360`. Hence T0 remains excluded, with mean gap `1/360`.

**All-root metric-sector collar.** With `epsilon=1/40000000`, and kappa(M)<=3, use `tr(M)/m<=9/2`. The error is less than `m/1600`. Vertices 8 and 9 remain strict U, with every outgoing arrow below `-m/1600`.

An explicit eleven-parameter cylinder lies in each corresponding collar. Use

```
x,y in [0,1],
c=1-(1-b)*x, p=(1-q)*y,
```

and allow each of

```
b-1/4, q-1/4, a-1/4, d-3/4,
u-1/16, v-1/16, lambda-1/2, sigma, tau
```

to vary independently in `[-delta0,delta0]`, where

```
delta0=1/40000000   for the unrestricted T0 packet exclusion,
delta0=1/800000000  for the all-root kappa(M)<=3 exclusion.
```

Apply the actual compact-chart projectivity `Y/(1+sigma*Yx+tau*Yy)` and refill uniformly. Comparing at the same raw x,y, the vertex displacement is less than `6*delta0`, which is smaller than the relevant epsilon. All intervals are closed. Interior x,y give the genuine H5 incidence; boundary rows are its labelled limits. The cylinders include two independent nonparallel projective directions.

## 8. Exact actual controls and the mixed-coefficient warning

At x=y=1/2 in the unprojected family,

```
V=59/512,
g=(601/3776,953/5664,123/236).
```

For T0 with unit weights, `s1=t1=s2=t2=1`. Its surviving mixed power coefficient is

```
[x^2*y^2]G =
((27/8192,-27/16384,0),
 (-27/16384,0,0),
 (0,0,0)).
```

The leading 2-by-2 minor is `-729/268435456`. Thus this coefficient is indefinite **even though the complete stress is positive definite over the entire square**, as proved in Section 5. This is an exact obstruction to a coefficientwise-power-PSD shortcut, not a feasible tree or a failure of joint-linear separation.

Two physical metrics on this same actual body are preserved:

```
M0=I,
a=(1,2,-1), epsilon=1/1000000,
M1=a*a^T+epsilon*I,
N1=I/epsilon-a*a^T/[epsilon*(epsilon+6)].
```

Their strict primal U sets are

```
M0: {0,1,2,4,5,6,7,8,9},
M1: {3,7}.
```

All 34 primal primitives are nonzero in both controls. For M1, the projection values are

```
(1/8,5/16,11/16,7/8,3/4,1/4,3/32,-1,-1/2,0),
a*g=-289/11328.
```

Every rank-one primitive has absolute value at least `289/362496`; the perturbation by epsilon*I changes one by less than `4*epsilon`. This proves the stated U2 control exactly. The supplied source reconstructs the actual covariance, inverse metrics, poles, all primal/polar primitives and strict census data. No S1, physicalweak000, or proper110 assertion is inferred merely from the primal checks.

## 9. What was tried, acceptance status and continuation

I tried broader independent basal boxes and then full corner fractions with the parent's Taylor/stress machinery. Those searches did not produce an all-root certificate that I could accept in this continuation. Later tool responses were not readable to me, so I do not assert an observed terminal pass, a generated-report hash, or completion of those searches. No search failure or finite-library gap enters the proofs above.

The durable new work is the exact released-carrier representation, the three/nine-matrix reduction, the unrestricted complete-packet family certificate, and the all-root metric-sector certificate with actual-refill collars. Their proofs are given explicitly. The source below is complete and independent of the parent implementation; its execution is an audit step, not an asserted completed numerical search.

The next concrete task is to find, for each remaining rooted tree, nonnegative weights satisfying the nine block conditions, possibly on a closed subdivision of the cut square and of the remaining basal moduli. The mixed `sym(e*f^T)` term must be retained. The already accepted parent interval engine can enclose the moving carrier coefficients, but it must not freeze them at a centre.

**Whole-incidence coverage does not change. The C34 lower prohibition is not completed. The accepted interval remains 34<=C_min<=622, and attainment remains a separate obligation.** No actual complete U1 cone or reciprocal-hull survivor is supplied here.

## 10. Complete source-only recovery

Save the following complete unit as `h5_corner_cut.py` and run

```
python -B -S h5_corner_cut.py h5_corner_cut_report.json
```

It requires Python>=3.11, standard library only, assertions enabled. It reconstructs all exact inputs, tests actual fan moments against tetrahedral subtraction, checks the polynomial identities on rational parallel/nonparallel/boundary controls, verifies the stated numerical rational inequalities, reconstructs the complete primal/dual tree census, and writes the full exact control report. It also writes the nine block matrices for T0; their PSD flags are diagnostic and are not substituted for the independent packet proof.

Expected terminal marker, not claimed as observed in this continuation:

```
H5_CORNER_CUT_PASS 150 216 4879 48790 439110 9 2
```

The following output line supplies the generated report's byte count and SHA-256. No unseen stress-array or report pin is asserted. All continuation-critical data are literal or reconstructed by this source.

```python
#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
from pathlib import Path
import hashlib, json, sys
assert __debug__ and sys.version_info >= (3,11)
FACES=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
       (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
EDGES=tuple(sorted({tuple(sorted((f[i],f[(i+1)%len(f)])))
                    for f in FACES for i in range(len(f))}))
ARROWS=tuple(sorted((i,j) for a,b in EDGES for i,j in ((a,b),(b,a))))
EF={e:tuple(k for k,f in enumerate(FACES)
             if any(tuple(sorted((f[i],f[(i+1)%len(f)])))==e
                    for i in range(len(f)))) for e in EDGES}
assert len(EDGES)==17 and all(len(v)==2 for v in EF.values())
T0=((1,0),(2,1),(3,2),(4,3),(5,4),(6,5),(7,0),(8,7),(9,7))
W0=tuple((i,j,F(1)) for i,j in T0)
I=tuple(tuple(F(i==j) for j in range(3)) for i in range(3))
Z=tuple(tuple(F(0) for j in range(3)) for i in range(3))
def va(a,b):return tuple(x+y for x,y in zip(a,b))
def vs(a,b):return tuple(x-y for x,y in zip(a,b))
def vm(s,a):return tuple(s*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def sy(a,b):return tuple(tuple((a[i]*b[j]+b[i]*a[j])/2 for j in range(3)) for i in range(3))
def ma(a,b):return tuple(tuple(a[i][j]+b[i][j] for j in range(3)) for i in range(3))
def ms(s,a):return tuple(tuple(s*x for x in row) for row in a)
def mm(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)) for i in range(3))
def mv(a,b):return tuple(dot(row,b) for row in a)
def det(a):
 n=len(a)
 if n==1:return a[0][0]
 return sum((-1)**j*a[0][j]*det(tuple(tuple(a[i][k] for k in range(n) if k!=j)
                                      for i in range(1,n))) for j in range(n))
def psd(a):return all(det(tuple(tuple(a[i][j] for j in ix) for i in ix))>=0
                      for n in (1,2,3) for ix in combinations(range(3),n))
def pd(a):return all(det(tuple(tuple(a[i][j] for j in range(n)) for i in range(n)))>0 for n in (1,2,3))
def inv(a):
 w=[list(a[i])+list(I[i]) for i in range(3)]
 for j in range(3):
  k=next(k for k in range(j,3) if w[k][j]);w[j],w[k]=w[k],w[j]
  q=w[j][j];w[j]=[v/q for v in w[j]]
  for i in range(3):
   if i!=j:
    q=w[i][j];w[i]=[x-q*y for x,y in zip(w[i],w[j])]
 return tuple(tuple(row[3:]) for row in w)
def moments(Y):
 V=F(0);J=(F(0),)*3;T2=Z
 for f in FACES:
  if 0 in f:continue
  for j in range(1,len(f)-1):
   z=tuple(Y[i] for i in (0,f[0],f[j],f[j+1]));a,b,c,d=z
   w=dot(vs(b,a),cross(vs(c,a),vs(d,a)))/6
   assert w>=0
   s=tuple(sum(v[i] for v in z) for i in range(3))
   R=sy(s,s)
   for v in z:R=ma(R,sy(v,v))
   V+=w;J=va(J,vm(w/4,s));T2=ma(T2,ms(w/20,R))
 assert V>0
 return V,J,T2

def frame(theta,la,s=F(0),t=F(0)):
 b,q,a,d,u,v=map(F,theta);la,s,t=map(F,(la,s,t));r=1-la
 assert 0<b<1 and 0<q<1 and 0<a<d<1 and u>0 and v>0 and u/b+v/a<1
 assert 0<=la<=1
 Y=((r*b,0,0),(r,0,0),(r,0,0),(r*q,r*(1-q),0),
    (0,r*d,0),(0,r*a,0),(r*u,r*v,0),(0,0,1),(la,0,1),(0,la,1))
 Y=tuple(tuple(map(F,z)) for z in Y)
 den=tuple(1+s*z[0]+t*z[1] for z in Y);assert min(den)>0
 Y=tuple(vm(1/h,z) for z,h in zip(Y,den))
 A=Y[1];e=vs(Y[0],A);f=vs(Y[3],A);T=Y[8]
 k=-dot(e,cross(f,vs(T,A)))/6;assert k>=0
 V0,J0,T20=moments(Y)
 return dict(Y=Y,A=A,e=e,f=f,T=T,k=k,V0=V0,J0=J0,T20=T20,la=la)

def model(h,x,y):
 x,y=F(x),F(y);assert 0<=x<=1 and 0<=y<=1
 Y=list(h['Y']);Y[1]=va(h['A'],vm(x,h['e']));Y[2]=va(h['A'],vm(y,h['f']))
 S=va(va(vm(3,h['A']),h['T']),va(vm(x,h['e']),vm(y,h['f'])))
 w=h['k']*x*y;V=h['V0']-w;J=vs(h['J0'],vm(w/4,S))
 R=sy(S,S)
 for z in (h['A'],Y[1],Y[2],h['T']):R=ma(R,sy(z,z))
 T2=ma(h['T20'],ms(-w/20,R));assert V>0
 return tuple(Y),V,J,T2

def true_faces(Y):
 assert len(set(Y))==10
 for f in FACES:
  n=cross(vs(Y[f[1]],Y[f[0]]),vs(Y[f[2]],Y[f[0]]));assert n!=(0,0,0)
  h=dot(n,Y[f[0]])
  assert all(dot(n,Y[i])==h if i in f else dot(n,Y[i])<h for i in range(10))

def stress(Y,V,J,weights):
 return tuple(tuple(sum(-w*((V*Y[i][a]-J[a])*(Y[j][b]-Y[i][b])
                              +(V*Y[i][b]-J[b])*(Y[j][a]-Y[i][a]))/2
                            for i,j,w in weights) for b in range(3)) for a in range(3))

class P:
 def __init__(self,x=0):
  if isinstance(x,P):self.c=x.c.copy()
  else:self.c={} if not x else {(0,0):F(x)}
 @classmethod
 def new(cls,d):
  z=cls();z.c={k:F(v) for k,v in d.items() if v};return z
 def __add__(self,b):
  d=self.c.copy()
  for k,v in P(b).c.items():d[k]=d.get(k,F(0))+v
  return P.new(d)
 __radd__=__add__
 def __neg__(self):return P.new({k:-v for k,v in self.c.items()})
 def __sub__(self,b):return self+-P(b)
 def __rsub__(self,b):return P(b)+-self
 def __mul__(self,b):
  d={}
  for (i,j),v in self.c.items():
   for (k,l),w in P(b).c.items():d[i+k,j+l]=d.get((i+k,j+l),F(0))+v*w
  return P.new(d)
 __rmul__=__mul__
 def __truediv__(self,b):return self*(1/F(b))
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  z=P(1)
  for j in range(n):z=z*self
  return z
 def __eq__(self,b):return self.c==P(b).c
 def at(self,x,y):return sum(v*x**i*y**j for (i,j),v in self.c.items())
X=P.new({(1,0):1});YVAR=P.new({(0,1):1})
def co(A,i,j):return tuple(tuple(P(v).c.get((i,j),F(0)) for v in row) for row in A)
def substitute(A,x,y):return tuple(tuple(P(v).at(x,y) for v in row) for row in A)

def nine_blocks(h,weights,box=(F(0),F(1),F(0),F(1))):
 Y=list(h['Y']);Y[1]=va(h['A'],vm(X,h['e']));Y[2]=va(h['A'],vm(YVAR,h['f']))
 S=va(va(vm(3,h['A']),h['T']),va(vm(X,h['e']),vm(YVAR,h['f'])))
 V=h['V0']-h['k']*X*YVAR;J=vs(h['J0'],vm(h['k']*X*YVAR/4,S))
 G=stress(Y,V,J,weights)
 out=lambda z:sum(w for i,j,w in weights if i==z)
 inc=lambda z:sum(w for i,j,w in weights if j==z)
 B1=ms(h['k']*(3*out(1)+inc(1))/4,sy(h['e'],h['e']))
 B2=ms(h['k']*(3*out(2)+inc(2))/4,sy(h['f'],h['f']))
 internal=sum(w for i,j,w in weights if {i,j}=={1,2})
 gamma=internal-(inc(1)-out(1)+inc(2)-out(2))/4
 assert co(G,3,1)==ms(-1,B1) and co(G,1,3)==ms(-1,B2)
 assert co(G,2,2)==ms(h['k']*gamma,sy(h['e'],h['f']))
 assert psd(B1) and psd(B2)
 a,b,c,d=map(F,box);dx=b-a;dy=d-c
 assert 0<=a<b<=1 and 0<=c<d<=1
 xx=a+dx*X;yy=c+dy*YVAR;GG=substitute(G,xx,yy)
 bonus=ma(ms(dx**3*yy*X**2*(1-X),B1),ms(dy**3*xx*YVAR**2*(1-YVAR),B2))
 R=ma(GG,ms(-1,bonus))
 assert all(i<=2 and j<=2 for row in R for p in row for i,j in P(p).c)
 blocks=[]
 for i,j in product(range(3),repeat=2):
  H=Z
  for a1 in range(i+1):
   for b1 in range(j+1):
    H=ma(H,ms(F(comb(i,a1),comb(2,a1))*F(comb(j,b1),comb(2,b1)),co(R,a1,b1)))
  blocks.append(H)
 bx=((1-X)**2,2*X*(1-X),X**2);by=((1-YVAR)**2,2*YVAR*(1-YVAR),YVAR**2)
 rebuilt=Z
 for (i,j),H in zip(product(range(3),repeat=2),blocks):rebuilt=ma(rebuilt,ms(bx[i]*by[j],H))
 assert rebuilt==R
 return blocks,co(G,2,2)

def orient(n,edges,root):
 adj=[[] for i in range(n)]
 for i,j in edges:adj[i].append(j);adj[j].append(i)
 parent={root:root};stack=[root]
 while stack:
  i=stack.pop()
  for j in adj[i]:
   if j not in parent:parent[j]=i;stack.append(j)
 if len(parent)!=n:return None
 return tuple((i,parent[i]) for i in range(n) if i!=root)

def census():
 trees=0;rooted=0;pairs=0
 for ee in combinations(EDGES,9):
  if orient(10,ee,0) is None:continue
  trees+=1
  dd=tuple(EF[e] for e in EDGES if e not in ee)
  assert len(dd)==8 and all(orient(9,dd,r) is not None for r in range(9))
  for r in range(10):
   tt=orient(10,ee,r);assert tt is not None and len(tt)==9
   rooted+=1;pairs+=9
 assert (trees,rooted,pairs)==(4879,48790,439110)
 return trees,rooted,pairs

def physical(h,M):
 Y,V,J,T2=model(h,F(1,2),F(1,2));true_faces(Y)
 g=vm(1/V,J);C=ma(ms(1/V,T2),ms(-1,sy(g,g)));assert pd(C) and pd(M)
 N=inv(M);assert pd(N) and mm(M,N)==I
 XX=tuple(vs(z,g) for z in Y)
 D={(i,j):dot(XX[i],mv(M,vs(Y[j],Y[i]))) for i,j in ARROWS}
 poles=[]
 for f in FACES:
  n=cross(vs(Y[f[1]],Y[f[0]]),vs(Y[f[2]],Y[f[0]]));hh=dot(n,vs(Y[f[0]],g));assert hh>0
  poles.append(vm(1/hh,n))
 qa=sorted({(a,b) for f,g1 in EF.values() for a,b in ((f,g1),(g1,f))})
 E={(f,g1):dot(poles[f],mv(N,vs(poles[g1],poles[f]))) for f,g1 in qa}
 U=tuple(i for i in range(10) if all(D[i,j]<0 for a,j in ARROWS if a==i))
 S=tuple(f for f in range(9) if all(E[f,g1]<0 for a,g1 in qa if a==f))
 H=tuple((i,j) for i,j in EDGES if all(v<0 for v in (D[i,j],D[j,i],E[EF[i,j]],E[EF[i,j][::-1]])))
 if all(D.values()) and all(E.values()):assert len(S)+len(U)-len(H)==2
 return dict(vertices=Y,V=V,J=J,T2=T2,g=g,C=C,M=M,N=N,poles=poles,
             D=tuple((i,j,D[i,j]) for i,j in ARROWS),
             E=tuple((f,g1,E[f,g1]) for f,g1 in qa),U=U,S=S,H=H,
             zero_primal=tuple(k for k,v in D.items() if v==0),
             zero_polar=tuple(k for k,v in E.items() if v==0))

def domain_checks(h):
 assert h['V0']==F(31,256) and h['k']==F(3,128)
 assert h['J0']==(F(679,32768),F(1933,98304),F(63,1024))
 g0=vm(1/h['V0'],h['J0']);assert h['V0']-h['k']==F(25,256)
 assert F(31,25)*g0[0]-F(3,25)>=F(9,100) and g0[0]<=F(7,40)
 assert g0[1]>=F(4,25) and F(31,25)*g0[1]<=F(21,100)
 assert g0[2]>=F(1,2) and F(31,25)*g0[2]-F(3,50)<=F(29,50)
 aa=F(257,1024)-F(9,32)*F(7,40)
 dd=F(293,1024)-F(17,32)*F(21,100);ff=F(21,50)
 bb=F(1,1024)+(17*F(7,40)+9*F(21,100))/64
 cc=F(3,16)-F(9,200)-F(9,128)
 ee=max(abs(F(1,4)-F(21,200)-F(493,3200)),abs(F(1,4)-F(2,25)-F(17,128)))
 assert F(3,16)-F(7,80)-F(261,3200)>0
 gaps=(aa-bb-cc,dd-bb-ee,ff-cc-ee)
 assert gaps==(F(673,12800),F(773,12800),F(497,1600)) and min(gaps)>F(1,20)
 xmin=F(439,3200);B=F(1,2)-xmin
 assert B-F(9,32)>0
 assert (h['J0'][0]-xmin*h['V0'])/h['k']==F(5,16)-xmin
 assert xmin>F(27,200)
 assert F(93,100)-F(1933,2304)>F(54,625)
 assert F(73,200)**2+F(9,50)**2+F(1,2)**2<F(129,200)**2
 assert F(7,40)**2+F(17,50)**2+F(61,124)**2<F(5,8)**2
 tests=((F(13,80),F(129,400)),(F(4,25),F(5,16)),
        (F(97,400),F(9159,20000)),(F(91,400),F(71,160)),
        (F(21,50),F(387,500)))
 assert min(a-b/2 for a,b in tests)==F(1,800)
 for eps,sector in ((F(1,2000000),False),(F(1,40000000),True)):
  assert eps<F(1,100) and F(25,256)-33*eps>F(1,12)
  delta=794*eps;err=6*delta+2*delta*delta
  if sector:assert F(9,2)*err<F(1,1600)
  else:assert err<F(1,360)
  assert 6*(eps/20)<eps
 return gaps

def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [enc(v) for v in x]
 return x

def main():
 central=tuple(map(F,('1/4','1/4','1/4','3/4','1/16','1/16')))
 old=tuple(map(F,('3/20','2/25','1/5','2/5','1/20','1/25')))
 fixtures=((central,F(1,2),0,0),(central,F(1,2),F(1,25),F(-1,25)),
           (old,F(1,65),F(1,25),F(-1,25)),(old,F(64,65),F(1,25),F(-1,25)),
           (old,F(0),F(1,25),F(-1,25)),(old,F(1),F(1,25),F(-1,25)))
 grid=tuple(map(F,('0','1/3','1/2','2/3','1')));nc=0;ni=0
 for theta,la,s,t in fixtures:
  h=frame(theta,la,s,t)
  for x,y in product(grid,repeat=2):
   Y,V,J,T2=model(h,x,y);assert moments(Y)==(V,J,T2)
   g=vm(1/V,J);assert pd(ma(ms(1/V,T2),ms(-1,sy(g,g))))
   if 0<la<1 and 0<x<1 and 0<y<1:true_faces(Y)
   nc+=1
  for weights in [((i,j,F(1)),) for i,j in ARROWS]+[W0]:
   nine_blocks(h,weights);ni+=1
  nine_blocks(h,W0,(F(1,7),F(5,6),F(2,9),F(7,8)));ni+=1
 h=frame(central,F(1,2));gaps=domain_checks(h)
 H0=((F(257,1024),F(-1,1024),F(3,16)),
     (F(-1,1024),F(293,1024),F(1,4)),(F(3,16),F(1,4),F(1)))
 L=(F(-9,32),F(-17,32),F(-1))
 for x,y in product(grid,repeat=2):
  Y,V,J,T2=model(h,x,y);g=vm(1/V,J);rhs=ma(H0,sy(g,L))
  for i,j in ((1,0),(2,1),(3,2)):rhs=ma(rhs,ms(F(1,2),sy(vs(Y[j],Y[i]),vs(Y[j],Y[i]))))
  assert stress(Y,F(1),g,W0)==rhs
 blocks,mixed=nine_blocks(h,W0)
 assert mixed==((F(27,8192),F(-27,16384),F(0)),(F(-27,16384),F(0),F(0)),(F(0),)*3)
 assert det(tuple(tuple(mixed[i][j] for j in range(2)) for i in range(2)))==F(-729,268435456)
 u=(F(1),F(2),F(-1));eps=F(1,1000000);M=ma(sy(u,u),ms(eps,I))
 N=ma(ms(1/eps,I),ms(-1/(eps*(eps+6)),sy(u,u)));assert mm(M,N)==I
 controls=(physical(h,I),physical(h,M))
 assert controls[0]['V']==F(59,512)
 assert controls[0]['g']==(F(601,3776),F(953,5664),F(123,236))
 assert controls[0]['U']==(0,1,2,4,5,6,7,8,9) and controls[1]['U']==(3,7)
 assert all(not c['zero_primal'] for c in controls)
 assert F(289,362496)>4*eps
 counts=census();assert (nc,ni)==(150,216)
 te={tuple(sorted(e)) for e in T0};de=tuple(EF[e] for e in EDGES if e not in te)
 dual=tuple(orient(9,de,r) for r in range(9))
 assert dual[0]==((1,3),(2,0),(3,4),(4,5),(5,6),(6,7),(7,2),(8,4))
 report=dict(version=1,parent_id='minimum-0231',
  parent_sha256='caca8b2fe76419e5069d48126156237d6afc6c344dae2add7fdfcced9a7be10b',
  faces=FACES,edges=EDGES,packet=W0,complementary_dual_trees=dual,
  carrier=h,gershgorin_gaps=gaps,mixed_coefficient=mixed,
  nine_blocks=blocks,nine_block_psd_flags=tuple(psd(b) for b in blocks),
  nine_block_flags_are_diagnostic_not_an_asserted_cover=True,
  controls=controls,tree_counts=counts,moment_checks=nc,identity_checks=ni)
 raw=(json.dumps(enc(report),sort_keys=True,separators=(',',':'))+'\n').encode()
 target=Path(sys.argv[1] if len(sys.argv)>1 else 'h5_corner_cut_report.json');target.write_bytes(raw)
 print('H5_CORNER_CUT_PASS',nc,ni,*counts,len(controls[0]['U']),len(controls[1]['U']))
 print('REPORT_BYTES_SHA256',len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__':main()
```
