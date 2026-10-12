# minimum-0282

AI research report · 2026-09-27 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# W_TRIANGULAR_HORIZON_U2_AND_POSITIVE_FLAG_COMPACTIFICATION_V1

## 1. New result and exact scope

There is a new unconditional, all-root exclusion at a genuine projective horizon of the literal W body.

Let the raw projective image be

`Z_i = Y_i / (1+h Y_ix+k Y_iy+l Y_iz)`,

and write `a=1+l`. Then

**For every `0<=h,k<=1/500` and `0<a<=1/500`, the uniformly refilled image, centered at its actual volume centroid, has at least two strict unstable equilibria under every SPD metric.**

The members with `h+k>0` are genuinely nonparallel. Arbitrarily large `h/a` and `k/a`, every simultaneous approach to the projective horizon, all metric conditioning, and incidental physical weak contacts are included. The normalized closed cube, including `a=0`, consists of full-dimensional bodies; it is not a dimensional-loss argument.

The proof excludes every weak rooted tree even for a nonzero PSD matrix. For every such tree, three of its actual arrows, selected by a four-group quotient, satisfy the quantitative contradiction

`D_1(M)+D_2(M)+D_3(M) < -tr(M)/40`

in the specified regular-tetrahedron normalization. Thus no stable-root choice or same-inverse polar configuration can produce S1/U1 on this domain. No covariance or joint-S1 assumption is used.

The new wedge is disjoint from the completed parent square `h,k in [1,2]`. It is narrow in the raw denominator coefficients, but not a small raw-vertex collar: `Z7=(0,0,1/a)` is unbounded, and the angle between the two displayed end planes can tend to a right angle. The theorem includes unrestricted relative rates among all three small denominator coefficients.

A second result supplies **24 explicit rational closed-cube charts covering the entire positive coefficient sector `h,k>0,a>0`**, with a fixed full-dimensional tetrahedron in every normalized body. The charts resolve all simultaneous parameter rates. Their volume and actual centroid extend rationally through their boundaries. A general version applies to any four independent nonnegative affine functions on a fixed polytope; using bases of actual facet slacks gives at most `24*binom(F,4)` charts for its entire positive-projective domain.

This compactification also identifies an important obstruction to a proposed shortcut: the raw limit `h=k=a→infinity` has a **full 10/17/9 affine-normalized limit**, not a lower-vertex body. More generally an entire positive two-dimensional coefficient face has this property. Lower-vertex exclusion cannot be applied to that face merely because the original raw coordinates collapse.

The full positive horizontal sector remains undecided by this handoff. The proposed numerical 24-cube cover and the balanced/corridor variants are not promoted: a verified complete terminal certificate and reproducible output pins for those larger searches are not established here. The new mechanical theorem below is analytic and does not depend on those searches.

No canonical incidence count or global complexity bound changes. The inherited interval remains `34<=C_min<=622`; no U1 or 110 attainer is supplied. fileciteturn30file0L19-L23

## 2. Input authority and evidence status

The retained reading record covers the entire current journal through line 1745/EOF, including the literal parent. The supplied journal is 341318 bytes, SHA-256

`d32d23e00f48b5b30b9345780d0d1279965fea98f5b71b9e039913f6adff821b`.

The direct parent is

`minimum-0277`,

SHA-256

`608c65e59a5ceb3ffec054f22bff22e0e1831212acdd4510e6e7d1820d88401c`.

Its completed `NONPARALLEL_W_THREE_CHART_ALLROOT_V2` theorem and recorded author cold execution remain accepted. They are not replaced or weakened here. The earlier root-hull gap and actual-foot disjunction remain useful methods, but neither is needed in the new triangular-horizon wedge.

The proof certificate in Sections 4–6 is given completely as literal matrices and rational inequalities. It has no external computational dependency. The consolidated reconstruction program in Section 10 has **not been observed completing in this resumed handoff**. Its terminal marker is therefore an expected verification target, not an observed execution receipt. No new source/output byte count or hash is fabricated. Its full source and all inputs are included, and it prints those pins when executed.

The physical controls below are specified by a finite exact construction. Their 222 count is proved by the rational-frame argument, rather than asserted from an unobserved numerical census. The program reconstructs their actual labelled censuses, metrics, inverses and every primitive. They are nonattaining controls, not physical survivors of a complete U1 packet.

## 3. Literal W geometry and genuine uniform moments

The source vertices, with unchanged labels, are

```
Y0=(17/80,0,0)
Y1=(629/800,0,0)
Y2=(187/250,51/500,0)
Y3=(51/100,17/50,0)
Y4=(0,221/800,0)
Y5=(0,17/80,0)
Y6=(17/320,17/320,0)
Y7=(0,0,1)
Y8=(3/20,0,1)
Y9=(0,3/20,1).
```

The true outward maximal facet cycles are

```
F0=(6,5,4,3,2,1,0)
F1=(8,7,0,1)
F2=(7,6,0)
F3=(1,2,8)
F4=(9,8,2,3)
F5=(9,3,4)
F6=(4,5,7,9)
F7=(6,7,5)
F8=(7,8,9).
```

The true edges are

```
01,06,07,12,18,23,28,34,39,45,49,56,57,67,78,79,89.
```

Use exactly the positive fan

```
(7,6,5,4), (7,6,4,3), (7,6,3,2),
(7,6,2,1), (7,6,1,0), (7,1,2,8),
(7,9,8,2), (7,9,2,3), (7,9,3,4).
```

These are integration tetrahedra. Their diagonals are not mechanical edges. The literal geometry and the actual-refill convention agree with the supplied parents. fileciteturn37file0L49-L108

For a tetrahedron T, let `w_T` be its source six-volume determinant. Set

```
d_i=1+h Y_ix+k Y_iy+(a-1)Y_iz.
```

For finite `a>0` and `h,k>=0`, all denominators are positive. The projective map preserves the true lattice and orientation. Its tetrahedral six-volume is

`w_T / product_{i in T} d_i`.

The new uniform centroid is consequently

```
D=sum_T w_T/product d_i                        =6 Vol(P)
J=sum_T (w_T/product d_i) sum_{i in T} Z_i       =24 integral_P z dz
g=J/(4D).
```

All moment weights in this handoff are these actual tetrahedral volumes or their common affine rescalings. No freely assigned vertex or fan masses occur.

The source calibration is

```
Vol(P_source)=881291/9600000
source centroid=(7368835529/28201312000,
                 3427883561/28201312000,
                 50317/153268).
```

## 4. A full-dimensional triangular-horizon normalization

Put

```
b=17/320, tau=3/20, epsilon=1/500.
```

For each finite positive input, apply the unique affine map sending the four actual image vertices `(6,7,8,9)` to `(0,e1,e2,e3)`. This tetrahedron is nondegenerate. For a basal source point `Y_i=(x,y,0)`, write

```
xi=x-b, upsilon=y-b, d=1+h*x+k*y.
```

The normalized point is exactly

```
B_i=(-a*(xi+upsilon)/(tau*d),
      (a+tau*h)*xi/(tau*d),
      (a+tau*k)*upsilon/(tau*d)),       i=0,...,6,
B7=e1, B8=e2, B9=e3.
```

In particular `B6=0`. These formulas extend to the whole closed cube

`0<=h,k,a<=epsilon`.

Every denominator of a basal point is at least one. The fixed standard tetrahedron remains inside the convex hull even on every boundary. Thus the normalized six-volume `D` satisfies `D>=1`; no raw dimensional loss is used.

The source six-volume of `(6,7,8,9)` is `tau^2=9/400`. After cancellation, the normalized fan weight is

```
W_T=(w_T/tau^2)*(1+b*(h+k))
       * product_{j in {7,8,9}\T} A_j
       / product_{i in T, i<7} (1+h Y_ix+k Y_iy),
A7=a, A8=a+tau*h, A9=a+tau*k.
```

Every fan tetrahedron contains 7, so no uncancelled division by a occurs. The weights are nonnegative on the closed cube and are the actual normalized determinants. Their sum and first moments give the actual limiting uniform centroid as well.

### Complete limiting bodies in this wedge

At `a=h=k=0`, all seven basal labels coincide at 0 and the true body is the standard tetrahedron. Its six-volume is 1 and its centroid is `(1/4,1/4,1/4)`.

At `a=0`, `h,k>0`, the true body is the pentagonal pyramid with apex `e1` and basal cycle

```
B0=(0, 3*b*h/(1+4*b*h), -b*k/(1+4*b*h))
e2
e3
B5=(0, -b*h/(1+4*b*k), 3*b*k/(1+4*b*k))
0.
```

It has f-vector `(6,10,6)`. If `c_base` is the actual area centroid of that displayed pentagon, its volume centroid is exactly

`e1/4+3*c_base/4`.

The usual signed polygon formula, or the supplied fan, recovers both remaining coordinates rationally. At `a=0,h>0,k=0`, the true body is the tetrahedron with vertices `e1,e2,e3,(0,-b*h,0)`, six-volume `1+b*h`, and centroid `(1,1-b*h,1)/4`. The reflected statement holds for `a=0,h=0,k>0`. All these limits are full-dimensional.

These formulas identify every simultaneous-rate limit in the closed wedge by continuity. They are affine normalizations of actual uniformly refilled images, not centroids transported through a non-affine map. The pentagonal-pyramid limit is consistent with the literal parent's lower compactification. fileciteturn37file0L141-L175

## 5. Actual-centroid bounds on the entire cube

Use the linear map

```
L=((0,-2,-2),(-2,0,-2),(-2,-2,0))
```

and regular tetrahedron vectors

```
R0=(1,1,1)
R1=(1,-1,-1)
R2=(-1,1,-1)
R3=(-1,-1,1).
```

If `g` is the newly integrated centroid in the B coordinates and `g_T=(1/4,1/4,1/4)`, set

```
eta=L*(g-g_T),       d_i=L*B_i, i<7.
```

The actual centered vertices are

```
X_i=R0+d_i-eta, i<7,
X7=R1-eta, X8=R2-eta, X9=R3-eta.
```

The same eta occurs at every vertex.

### Basal displacement

For each basal source point,

```
d_i=(2/d)*(-a*(xi+upsilon)/tau-h*xi-k*upsilon,
            a*xi/tau-k*upsilon,
            a*upsilon/tau-h*xi).
```

The exact source bounds are

```
|xi|<=1173/1600,
|upsilon|<=459/1600,
0<=xi+upsilon<=119/160,
max(xi,0)+max(upsilon,0)<=119/160.
```

They give component bounds, in units of epsilon,

```
2737/240, 24837/2400, 12699/2400.
```

The sum of their squares is

`1527258070/5760000 < 17^2`.

Hence, throughout the whole cube,

`max_{i<7} ||d_i|| < 17*epsilon`.

### The centroid is not independent

Group the actual normalized fan weights by their number m of top labels. There is one m=3 tetrahedron, three m=2 tetrahedra and five m=1 tetrahedra. The source sums are exactly

```
sum_{m=1} w_T=641291/1600000
sum_{m=2} w_T=51/400
w_{m=3}=9/400.
```

With `mu=17/160`, the cancelled weight formula yields

```
W3 <= 1+mu*epsilon
W2 <= (391/60)*epsilon*(1+mu*epsilon)
W1 <= 24*epsilon^2*(1+mu*epsilon).
```

For the last inequality, the exact coefficient before rounding upward is

`(641291/36000)*(23/20)^2 =339242939/14400000 <24`.

The centroid identity is

`4D*eta=sum_T W_T*L*(sum_{i in T}B_i-e1-e2-e3)`.

For an m=3 tetrahedron its vector in this sum is one basal displacement. For m=2 it is two basal displacements minus one `L*e_j`, whose norm is less than 3. For m=1 it is three basal displacements minus two such columns; the latter sum has norm less than 5. Since `D>=1`,

```
||eta||/epsilon
 <= (1+mu*epsilon)/4
       *[17+(391/60)*(3+34*epsilon)
             +24*epsilon*(5+51*epsilon)]
 <10
```

at `epsilon=1/500`. The displayed right side is increasing for nonnegative epsilon, so the bound holds on the entire cube:

`||eta||<10*epsilon`.

This estimate uses the common actual fan and its actual centroid. An arbitrary reference point or separately optimized mass vector would not satisfy its derivation.

## 6. Complete mechanical certificate

### Four literal regular-tetrahedron matrices

For a rooted tree on four vertices, let

`P0=-sum_(i->j) sym(R_i*(R_j-R_i)^T)`.

There are 64 labelled rooted trees on the complete four-vertex graph. Under the orthogonal permutations of the regular tetrahedron, they have four rooted forms. Complete representatives are

```
Star, root at centre; arrows 1->0,2->0,3->0:
P0=((4,0,0),(0,4,0),(0,0,4)).

Star, root at leaf; arrows 1->0,2->1,3->1:
P0=((4,-2,-2),(-2,4,0),(-2,0,4)).

Path, root at endpoint; arrows 1->0,2->1,3->2:
P0=((2,-2,-1),(-2,6,-1),(-1,-1,4)).

Path, root internal; arrows 0->1,2->1,3->2:
P0=((2,0,1),(0,6,-1),(1,-1,4)).
```

The leading principal minors of `P0-I/2` are respectively

```
(7/2,49/4,343/8)
(7/2,33/4,119/8)
(3/2,17/4,31/8)
(3/2,33/4,175/8).
```

All are strictly positive. This is the complete constant-matrix certificate. The orbit counts are 4,12,24,24, summing to 64; no omitted four-vertex rooted type remains.

### Actual corrections and a reusable criterion

For a quotient edge let `E=R_j-R_i`. A top-to-top negative arrow matrix differs from its P0 term by `sym(eta*E^T)`. A top-to-basal term has correction

`sym(eta*E^T)-sym(R_i*d^T)+sym(eta*d^T)`.

A basal-to-top term has correction

`sym(eta*E^T)+sym(d*(2R0-R_j)^T)-sym(eta*d^T)+d*d^T`.

The last square is PSD and may be retained or safely dropped for a lower bound. Use

```
||R_i||<2, ||E||<3, ||2R0-R_j||<9/2.
```

A rooted four-group tree has at most one basal-source edge. Different edges entering the basal group may use different actual basal endpoints; their displacements are not identified.

More generally, whenever all basal displacements have norm at most d and the one common centroid shift has norm at most e, the sum P of its three actual negative arrow matrices obeys

`P > [1/2-9*e-(17/2)*d-3*e*d] I`.

Thus

`9*e+(17/2)*d+3*e*d <= 1/2`

is a sufficient all-root, all-SPD four-cluster exclusion criterion. Strict inequality gives an explicit matrix margin. This is a geometric/actual-centroid condition, not a covariance restriction.

For the entire W wedge take `d=17*epsilon`, `e=10*epsilon`. The error is bounded by

`(469/2)*epsilon+510*epsilon^2`.

At `epsilon=1/500`,

`1/2-(469/2)*epsilon-510*epsilon^2=181/6250>1/40`.

Therefore `P>I/40` throughout the entire closed normalized cube.

### Why this covers every original root and escape alternative

Suppose a weak rooted tree exists on the actual vertices. Contract all seven basal labels to group 0 and retain the three top labels as groups 1,2,3. Every quotient group can reach the root group, so the quotient directed graph contains a rooted tree on these four groups. Select one actual arrow realizing each of its three edges. These are genuine original arrows; no integration diagonal or artificial root-cell edge is introduced.

The exact matrix certificate above gives

`sum_selected D_ij(M)=-tr(M P)<-tr(M)/40<0`

for every nonzero PSD M, contradicting the three weak arrows.

For SPD M, a nonnegative true arrow satisfies strict norm growth

`||X_j||_M^2-||X_i||_M^2=2D_ij(M)+||X_j-X_i||_M^2>0`.

A hypothetical unique strict U therefore supplies the weak rooted tree just excluded. All ten possible roots and all true escape alternatives are covered. There is no assumption about which facet is stable, whether its foot is proper or on its boundary, or whether additional weak rests exist.

The same four-group argument is independent of the number of vertices in the basal cluster and of the graph among them. It also applies to the actual limiting polytopes, using their true graph, because their three top corners remain distinct extreme points and the remaining vertices stay in the basal cluster. No physical equilibrium count is assigned to a singular metric.

## 7. Complete positive-functional flag compactification

This is a realization and moment theorem, not a completed mechanical cover of every chart.

Let `phi0,...,phi3` be four independent nonnegative affine functions on a fixed full-dimensional rational polytope with vertices Y_i. For the current positive sector use

`(phi0,phi1,phi2,phi3)=(1-z,x,y,z)`.

The raw denominator is

`phi0+h*phi1+k*phi2+a*phi3`.

For each permutation pi of four indices, order its coefficients and divide by the largest:

```
theta[pi0]=1
theta[pi1]=t1
theta[pi2]=t1*t2
theta[pi3]=t1*t2*t3,
0<t1,t2,t3<=1.
```

These 24 cubes cover all positive coefficients, including ties. Define the leading level of a source vertex by

`k_i=min{j:phi[pi_j](Y_i)>0}`.

Then its denominator is

`d_i=(t1*...*t_{k_i}) F_i(t)`,

where

`F_i=phi[pi_{k_i}](Y_i)+sum_{j>k_i} phi[pi_j](Y_i)*product_{r=k_i+1}^j t_r`.

Every F_i has a strictly positive constant term and nonnegative coefficients on the full closed cube.

Choose a source affine basis S of four vertices by greedily taking independent homogeneous vertex rows in decreasing order of k_i. Let beta_i,s be the affine barycentric coordinates of Y_i in S. The nested-span construction gives

`beta_i,s != 0 => k_s>=k_i`.

After sending the four projective images of S to the standard tetrahedron, the three coordinates of vertex i are exactly

`beta_i,s * (product_{r=k_i+1}^{k_s} t_r) * F_s/F_i`,

for the three non-origin members s of S. All powers are nonnegative. Hence every coordinate extends rationally to `[0,1]^3`, and the standard tetrahedron stays fixed.

For any independent source tetrahedron T, its normalized signed determinant is

```
(det_source(T)/det_source(S))
  * product_s_in_S F_s / product_i_in_T F_i
  * product_{r=1}^3 t_r^e(T,r),

e(T,r)=#{s in S:k_s>=r}-#{i in T:k_i>=r} >=0.
```

The exponent inequality follows because the high-level members of S form a basis of the span of all vertices at that level or above. An independent T can contain no more such vertices. Coplanar source tetrahedra remain identically flat.

Consequences are exact:

* Every simultaneous parameter rate has a subsequence in one of these 24 closed cubes and a full-dimensional normalized limit.
* Every determinant sign, and therefore the oriented incidence data of a relative boundary stratum, is determined solely by which of t1,t2,t3 are zero. The remaining positive parameter values do not create additional determinant walls.
* The actual positive fan weights have the same monomial/positive-denominator form. Their sum is bounded below by the unit tetrahedron's six-volume. The uniformly refilled volume and centroid therefore extend rationally and continuously to every boundary stratum.

This is not an assertion that the old maximal faces remain maximal at the boundary. The limiting body is the convex hull of the displayed limiting vertices; its true hull must be recovered, with coincident or nonextreme labels removed.

The construction is reusable beyond the four chosen W slacks. The cone of affine functions nonnegative on a bounded three-polytope is generated by its actual facet slacks. A conical Caratheodory reduction uses at most four independent generators. Applying the construction to every independent four-slack basis gives at most `24*binom(F,4)` closed charts. For F=9 this is at most 3024. This is a finite rational compactification recipe, not a claim that 3024 mechanical systems have been solved.

## 8. A full-E17 face at apparent horizontal infinity

The sequence

`h=k=a=R, R→infinity`

has denominator

`1-z+R*(x+y+z)`.

Raw rescaling alone sends the vertices toward a plane and is misleading. Let r be the actual source centroid and put `f=x+y+z`. On the literal W source,

`min_i f(Y_i)=17/160>0`.

The actual full-dimensional limiting projective image is

`A_i=(Y_i-r)/f(Y_i)`.

Its homogeneous determinant is `f(r)>0`, and its denominator is positive on the entire source. It therefore has exactly the original 10/17/9 true lattice.

An explicit affine normalization of the raw finite images is

`A_R(Z)=R*(I+r*p_R^T)*Z-R*r`,

where `p_R=(R,R,R-1)`. Applied to a raw image vertex, this equals

`(Y_i-r)/[(1/R)*(1-Y_iz)+f(Y_i)]`,

and converges to A_i. Thus the full-dimensional limit is an actual affine-normalized uniform refill. Its own centroid must still be recomputed by the actual fan.

The same conclusion holds for the entire coefficient face

`theta0=0, theta1,theta2,theta3>0`.

For example, with all three positive coefficients in [1,2], the limiting denominators stay uniformly positive on the source. This is a full-E17, two-projective-modulus family after common scaling. It is not a true positive-denominator horizon of the source centered at an interior point, and it does not contradict the existing properness theorem in that centered chart.

This is a precise failure of the rule 'raw horizontal infinity implies a lower-vertex limit'. It is not a U1 survivor. The source below prescribes a rational same-inverse 222 control both on this regular limiting body and on a genuine member of the newly excluded wedge. For each, it computes the actual centroid before selecting its metric.

## 9. What is and is not completed

The triangular-horizon wedge and the four-cluster criterion are complete analytic continuum exclusions. Their literal certificate is the four matrices, the four minor triples, the actual fan bounds and the rational gap in Sections 5–6. No floating-point sign or sampled SDP result is a premise.

The 24-chart construction resolves the positive-sector realization geometry, including simultaneous rates, but does not exclude all 24 cubes mechanically. In particular the full-E17 regular face just identified cannot be discarded using a lower-vertex theorem.

The exploratory full-cube and balanced/corridor stress searches do not have a substantiated complete execution receipt in this handoff. Their libraries are not presented as durable exclusion certificates, physical survivors, or evidence that primal stresses fail. No new numerical margin, row count or output pin from those searches is claimed.

The source below is a complete exact reconstruction and verification target, not a claimed observed run. The theorem's small literal analytic certificate is independently sufficient. The control-ray census is an analytic construction: for the actual centered primal vertices and polar vertices, a finite rational-frame selection makes all leading primal and polar arrow coefficients nonzero. A common exact large-L bound then fixes all 68 signs. It yields two strict U, two strict S, two strict H and no weak points, using one M and its inverse. It supplies no S1/U1 metric.

The next useful mechanical target is the actual full-E17 regular face `theta0=0` and its neighboring flag cells, or the other true horizon faces after their explicit normalized limits have been reconstructed. A complete one-sided survivor would justify using the retained actual-foot disjunction or mixed inverse conditions. An unfinished stress library does not.

## 10. Complete reconstruction source

Save this as `w_horizon_flags.py`, preserving its final newline, and run with assertions enabled:

```
python -B -S w_horizon_flags.py
```

Dependencies: CPython 3.13.5 standard library only; the source is written for Python >=3.10. There is no numerical optimizer, random seed, external certificate, parent executable or hidden geometry input. The program prints its source/report byte counts and SHA-256 values when run. Those output pins are deliberately not supplied as observed values here.

Expected terminal marker, **not an observed execution claim**:

```
W_TRIANGULAR_HORIZON_U2_AND_24_FLAG_RECOVERY_PASS
```

```python
#!/usr/bin/env python3
# Exact reconstruction target; assertions must remain enabled.
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import json
import sys

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)

PARENT = ('minimum-0277',
          '608c65e59a5ceb3ffec054f22bff22e0e1831212acdd4510e6e7d1820d88401c')
EPS = Q(1, 500)
b = Q(17, 320)
tau = Q(3, 20)
Y = tuple(tuple(map(Q, row)) for row in (
    ('17/80',0,0), ('629/800',0,0),
    ('187/250','51/500',0), ('51/100','17/50',0),
    (0,'221/800',0), (0,'17/80',0),
    ('17/320','17/320',0), (0,0,1),
    ('3/20',0,1), (0,'3/20',1)))
FACES = ((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),
         (1,2,8),(9,8,2,3),(9,3,4),
         (4,5,7,9),(6,7,5),(7,8,9))
FAN = tuple((7,f[0],f[j],f[j+1]) for f in FACES if 7 not in f
            for j in range(1,len(f)-1))
EDGES = tuple(sorted({tuple(sorted(e)) for f in FACES
                      for e in zip(f,f[1:]+f[:1])}))
ARROWS = tuple(e for a in EDGES for e in (a,a[::-1]))
EF = {e:tuple(i for i,f in enumerate(FACES) if set(e)<=set(f))
      for e in EDGES}
DUAL_EDGES = tuple(sorted(tuple(sorted(v)) for v in EF.values()))
R = tuple(tuple(map(Q,v)) for v in
          ((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)))
I = tuple(tuple(Q(i==j) for j in range(3)) for i in range(3))
ZERO = tuple(tuple(Q(0) for j in range(3)) for i in range(3))


def dot(a,c):
    return sum((x*y for x,y in zip(a,c)),Q(0))


def add(a,c):
    return tuple(x+y for x,y in zip(a,c))


def sub(a,c):
    return tuple(x-y for x,y in zip(a,c))


def scale(t,a):
    return tuple(t*x for x in a)


def cross(a,c):
    return (a[1]*c[2]-a[2]*c[1],
            a[2]*c[0]-a[0]*c[2],
            a[0]*c[1]-a[1]*c[0])


def det(A):
    return dot(A[0],cross(A[1],A[2]))


def transpose(A):
    return tuple(zip(*A))


def mv(A,v):
    return tuple(dot(row,v) for row in A)


def mm(A,B):
    return tuple(tuple(dot(row,col) for col in transpose(B)) for row in A)


def inv(A):
    d=det(A)
    assert d
    cof=(cross(A[1],A[2]),cross(A[2],A[0]),cross(A[0],A[1]))
    return tuple(tuple(x/d for x in row) for row in transpose(cof))


def outer(a,c):
    return tuple(tuple(a[i]*c[j] for j in range(3)) for i in range(3))


def plus(A,B):
    return tuple(add(a,c) for a,c in zip(A,B))


def times(t,A):
    return tuple(scale(t,row) for row in A)


def sym(a,c):
    return tuple(tuple((a[i]*c[j]+c[i]*a[j])/2 for j in range(3))
                 for i in range(3))


def minors(A):
    return A[0][0],A[0][0]*A[1][1]-A[0][1]**2,det(A)


def six(z,ids):
    a,c,d,e=(z[i] for i in ids)
    return dot(sub(c,a),cross(sub(d,a),sub(e,a)))


W0=tuple(six(Y,t) for t in FAN)
assert len(FAN)==9 and min(W0)>0
assert len(EDGES)==17 and len(set(DUAL_EDGES))==17
assert all(len(v)==2 for v in EF.values())


def moments(z,weights=None):
    actual=tuple(six(z,t) for t in FAN)
    assert min(actual)>=0
    if weights is not None:
        assert tuple(weights)==actual
    D=sum(actual,Q(0))
    J=(Q(0),)*3
    for t,w in zip(FAN,actual):
        J=add(J,scale(w,tuple(sum(z[i][j] for i in t) for j in range(3))))
    assert D>0
    return D,J,scale(1/(4*D),J)


def horizon_geometry(h,k,a):
    h,k,a=map(Q,(h,k,a))
    assert min(h,k,a)>=0
    db=tuple(1+h*y[0]+k*y[1] for y in Y[:7])
    td={7:a,8:a+tau*h,9:a+tau*k}
    z=[]
    for i,(x,y,unused) in enumerate(Y[:7]):
        xi,up=x-b,y-b
        z.append((-a*(xi+up)/(tau*db[i]),
                  td[8]*xi/(tau*db[i]),td[9]*up/(tau*db[i])))
    z+=((Q(1),Q(0),Q(0)),(Q(0),Q(1),Q(0)),(Q(0),Q(0),Q(1)))
    z=tuple(z)
    weights=[]
    for t,w in zip(FAN,W0):
        v=w/(tau*tau)*db[6]
        for j in (7,8,9):
            if j not in t:
                v*=td[j]
        for i in t:
            if i<7:
                v/=db[i]
        weights.append(v)
    D,J,g=moments(z,weights)
    assert six(z,(6,7,8,9))==1 and D>=1
    return dict(parameters=(h,k,a),vertices=z,D=D,J=J,centroid=g,
                fan_weights=tuple(weights))


def constant_certificate():
    groups={m:sum((w for t,w in zip(FAN,W0)
                   if sum(i>=7 for i in t)==m),Q(0)) for m in (1,2,3)}
    assert groups=={1:Q(641291,1600000),2:Q(51,400),3:Q(9,400)}
    assert six(Y,(6,7,8,9))==tau*tau
    for x,y,unused in Y[:7]:
        xi,up=x-b,y-b
        assert abs(xi)<=Q(1173,1600) and abs(up)<=Q(459,1600)
        assert 0<=xi+up<=Q(119,160)
        assert max(xi,0)+max(up,0)<=Q(119,160)
    bounds=(Q(2737,240),Q(24837,2400),Q(12699,2400))
    norm_bound=sum(x*x for x in bounds)
    assert norm_bound==Q(1527258070,5760000)<17**2
    mu=Q(17,160)
    c2=groups[2]/(tau*tau)*(1+tau)
    c1=groups[1]/(tau*tau)*(1+tau)**2
    assert c2==Q(391,60)
    assert c1==Q(339242939,14400000)<24
    eta_bound=(1+mu*EPS)*(17+c2*(3+34*EPS)+24*EPS*(5+51*EPS))/4
    assert eta_bound<10
    error=Q(469,2)*EPS+510*EPS*EPS
    gap=Q(1,2)-error
    assert gap==Q(181,6250)>Q(1,40)
    expected=(
        (((1,0),(2,0),(3,0)),((4,0,0),(0,4,0),(0,0,4)),
         (Q(7,2),Q(49,4),Q(343,8))),
        (((1,0),(2,1),(3,1)),((4,-2,-2),(-2,4,0),(-2,0,4)),
         (Q(7,2),Q(33,4),Q(119,8))),
        (((1,0),(2,1),(3,2)),((2,-2,-1),(-2,6,-1),(-1,-1,4)),
         (Q(3,2),Q(17,4),Q(31,8))),
        (((0,1),(2,1),(3,2)),((2,0,1),(0,6,-1),(1,-1,4)),
         (Q(3,2),Q(33,4),Q(175,8))))
    def matrix(arrows):
        out=ZERO
        for i,j in arrows:
            out=plus(out,times(-1,sym(R[i],sub(R[j],R[i]))))
        return out
    for arrows,rows,expected_minors in expected:
        A=matrix(arrows)
        assert A==rows
        assert minors(plus(A,times(-Q(1,2),I)))==expected_minors
    records=[]
    for edges in combinations(tuple(combinations(range(4),2)),3):
        adj=[[] for unused in range(4)]
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        for root in range(4):
            todo=[root]
            parent={root:root}
            arrows=[]
            for i in todo:
                for j in adj[i]:
                    if j not in parent:
                        parent[j]=i
                        todo.append(j)
                        arrows.append((j,i))
            if len(parent)!=4:
                continue
            A=matrix(arrows)
            m=minors(plus(A,times(-Q(1,2),I)))
            assert min(m)>0
            records.append(dict(root=root,arrows=arrows,matrix=A,shifted_minors=m))
    assert len(records)==64
    return dict(epsilon=EPS,source_weight_groups=groups,component_bounds=bounds,
                squared_bound=norm_bound,centroid_coefficient_bound=eta_bound,
                correction_bound=error,strict_matrix_gap=gap,
                quotient_trees=records)


def rank(rows):
    A=[list(map(Q,row)) for row in rows]
    if not A:
        return 0
    r=0
    for j in range(len(A[0])):
        pivot=next((i for i in range(r,len(A)) if A[i][j]),None)
        if pivot is None:
            continue
        A[r],A[pivot]=A[pivot],A[r]
        p=A[r][j]
        A[r]=[x/p for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][j]:
                p=A[i][j]
                A[i]=[x-p*y for x,y in zip(A[i],A[r])]
        r+=1
        if r==len(A):
            break
    return r


def flag_spec(perm):
    phi=tuple((1-y[2],y[0],y[1],y[2]) for y in Y)
    lead=tuple(next(j for j,k in enumerate(perm) if p[k]>0) for p in phi)
    ids=[]
    for i in sorted(range(10),key=lambda i:(-lead[i],i)):
        rows=[(Q(1),)+Y[j] for j in ids+[i]]
        if rank(rows)>len(ids):
            ids.append(i)
        if len(ids)==4:
            break
    assert len(ids)==4
    ids=tuple(ids)
    if six(Y,ids)<0:
        ids=ids[:2]+(ids[3],ids[2])
    B=transpose(tuple(sub(Y[i],Y[ids[0]]) for i in ids[1:]))
    BI=inv(B)
    bary=[]
    for i,y in enumerate(Y):
        v=mv(BI,sub(y,Y[ids[0]]))
        beta=(1-sum(v),)+v
        assert tuple(sum(beta[s]*Y[ids[s]][j] for s in range(4))
                     for j in range(3))==y
        assert all(not beta[s] or lead[ids[s]]>=lead[i] for s in range(4))
        bary.append(beta)
    exponent_rows=[]
    for t in combinations(range(10),4):
        if not six(Y,t):
            continue
        e=tuple(sum(lead[i]>=j for i in ids)-sum(lead[i]>=j for i in t)
                for j in (1,2,3))
        assert min(e)>=0
        exponent_rows.append((t,e))
    return dict(permutation=perm,phi=phi,lead=lead,simplex=ids,
                barycentric=tuple(bary),all_nonflat_exponents=exponent_rows)


def flag_geometry(spec,t):
    t=tuple(map(Q,t))
    assert all(0<=x<=1 for x in t)
    perm=spec['permutation']
    lead=spec['lead']
    ids=spec['simplex']
    factors=[]
    for i,phi in enumerate(spec['phi']):
        f=phi[perm[lead[i]]]
        mon=Q(1)
        for j in range(lead[i]+1,4):
            mon*=t[j-1]
            f+=phi[perm[j]]*mon
        assert f>0
        factors.append(f)
    z=[]
    for i,beta in enumerate(spec['barycentric']):
        row=[]
        for s in (1,2,3):
            v=beta[s]
            if v:
                for j in range(lead[i],lead[ids[s]]):
                    v*=t[j]
                v*=factors[ids[s]]/factors[i]
            row.append(v)
        z.append(tuple(row))
    z=tuple(z)
    assert six(z,ids)==1
    ws=six(Y,ids)
    weights=[]
    for tet,w in zip(FAN,W0):
        v=w/ws
        for j in (1,2,3):
            power=sum(lead[i]>=j for i in ids)-sum(lead[i]>=j for i in tet)
            assert power>=0
            v*=t[j-1]**power
        for i in ids:
            v*=factors[i]
        for i in tet:
            v/=factors[i]
        weights.append(v)
    D,J,g=moments(z,weights)
    assert D>=1
    for tet,e in spec['all_nonflat_exponents']:
        v=six(Y,tet)/ws
        for j,power in enumerate(e):
            v*=t[j]**power
        for i in ids:
            v*=factors[i]
        for i in tet:
            v/=factors[i]
        assert six(z,tet)==v
    return z,D,J,g


def hull(z):
    pts=tuple(dict.fromkeys(z))
    labels=tuple(tuple(i for i,v in enumerate(z) if v==p) for p in pts)
    supports={}
    for i,j,k in combinations(range(len(pts)),3):
        n=cross(sub(pts[j],pts[i]),sub(pts[k],pts[i]))
        if not any(n):
            continue
        values=tuple(dot(n,sub(p,pts[i])) for p in pts)
        if min(values)<0<max(values):
            continue
        supports[frozenset(i for i,v in enumerate(values) if not v)]=n
    extreme=tuple(i for i in range(len(pts))
                  if any(det(ns)!=0 for ns in combinations(
                      [n for f,n in supports.items() if i in f],3)))
    faces=tuple(sorted({tuple(i for i in sorted(f) if i in extreme)
                        for f in supports}))
    edges=tuple(sorted({tuple(sorted(set(f)&set(g)))
                        for f,g in combinations(faces,2)
                        if len(set(f)&set(g))==2}))
    fv=(len(extreme),len(edges),len(faces))
    assert fv[0]-fv[1]+fv[2]==2
    return dict(points=pts,original_labels=labels,extreme_indices=extreme,
                facets=faces,edges=edges,fvector=fv)


def ceilq(x):
    x=Q(x)
    assert x>=0
    return (x.numerator+x.denominator-1)//x.denominator


def physical_ray(z):
    D,J,g=moments(z)
    x=tuple(sub(y,g) for y in z)
    hu=hull(z)
    assert hu['fvector']==(10,17,9)
    assert set(hu['facets'])=={tuple(sorted(f)) for f in FACES}
    poles=[]
    for f in FACES:
        a,c,d=(z[i] for i in f[:3])
        n=cross(sub(c,a),sub(d,a))
        hh=dot(n,a)
        assert all(hh-dot(n,z[i])==0 if i in f else hh-dot(n,z[i])>0
                   for i in range(10))
        height=hh-dot(n,g)
        assert height>0
        poles.append(scale(1/height,n))
    poles=tuple(poles)
    A=list(x)+[sub(x[j],x[i]) for i,j in EDGES]
    B=list(poles)+[sub(poles[j],poles[i]) for i,j in DUAL_EDGES]
    assert len(A)==27 and len(B)==26
    chosen_r=None
    for r in range(1,82):
        u=(Q(1),Q(r),Q(r*r))
        if all(dot(u,v)!=0 for v in A) and all(any(cross(u,v)) for v in B):
            chosen_r=r
            break
    assert chosen_r is not None
    chosen_s=None
    for s in range(1,28):
        v=(Q(-chosen_r-s*chosen_r*chosen_r),Q(1),Q(s))
        if all(dot(v,q)!=0 for q in B):
            chosen_s=s
            break
    assert chosen_s is not None
    w=cross(u,v)
    assert dot(u,v)==dot(u,w)==dot(v,w)==0
    primal_mats=(outer(v,v),outer(w,w),outer(u,u))
    inverse_mats=tuple(times(1/dot(q,q)**2,outer(q,q)) for q in (u,w,v))
    rows=[]
    for side,points,edges,mats in (
            ('P',x,EDGES,primal_mats),
            ('Q',poles,DUAL_EDGES,inverse_mats)):
        for edge in edges:
            for i,j in (edge,edge[::-1]):
                co=tuple(dot(points[i],mv(M,sub(points[j],points[i]))) for M in mats)
                assert co[2]!=0
                rows.append(dict(side=side,arrow=(i,j),coefficients=co))
    assert len(rows)==68
    L0=1+max([1]+[ceilq(2*(abs(r['coefficients'][0])+abs(r['coefficients'][1]))
                         /abs(r['coefficients'][2])) for r in rows])
    def evaluate(mats):
        out=ZERO
        for k,M in enumerate(mats):
            out=plus(out,times(Q(L0)**k,M))
        return out
    M=evaluate(primal_mats)
    N=times(Q(1,L0*L0),evaluate(inverse_mats))
    assert min(minors(M))>0 and mm(M,N)==I and inv(M)==N
    pp={}
    qq={}
    for r in rows:
        c0,c1,c2=r['coefficients']
        sign=1 if c2>0 else -1
        shifted=(sign*(c0+c1*L0+c2*L0*L0),
                 sign*(c1+2*c2*L0),sign*c2)
        assert min(shifted)>0
        value=c0+c1*L0+c2*L0*L0
        if r['side']=='Q':
            value/=L0*L0
            qq[r['arrow']]=value
        else:
            pp[r['arrow']]=value
        r.update(sign=sign,shifted_coefficients=shifted,endpoint_value=value)
    U=[i for i in range(10) if all(t<0 for (a,c),t in pp.items() if a==i)]
    S=[i for i in range(9) if all(t<0 for (a,c),t in qq.items() if a==i)]
    H=[]
    weak={}
    packets=[]
    for (i,j),(f,k) in EF.items():
        vals=(pp[i,j],pp[j,i],qq[f,k],qq[k,f])
        e=sub(x[j],x[i])
        t=-pp[i,j]/dot(e,mv(M,e))
        foot=add(x[i],scale(t,e))
        normal=mv(M,foot)
        aa,bb,cc=dot(poles[f],poles[f]),dot(poles[f],poles[k]),dot(poles[k],poles[k])
        dd=aa*cc-bb*bb
        assert dd>0
        q0,q1=dot(poles[f],normal),dot(poles[k],normal)
        co=((cc*q0-bb*q1)/dd,(aa*q1-bb*q0)/dd)
        assert add(scale(co[0],poles[f]),scale(co[1],poles[k]))==normal
        is_h=max(vals)<0
        assert is_h==(0<t<1 and min(co)>0)
        if is_h:
            H.append((i,j))
        if max(vals)<=0 and 0 in vals:
            weak.setdefault(foot,[]).append((i,j))
        packets.append(dict(edge=(i,j),facets=(f,k),primitives=vals,
                            foot_fraction=t,foot=foot,normal_coefficients=co))
    assert (len(S),len(U),len(H))==(2,2,2)
    assert not weak and all(t!=0 for t in (*pp.values(),*qq.values()))
    for f in S:
        foot=scale(1/dot(poles[f],mv(N,poles[f])),mv(N,poles[f]))
        assert all(dot(q,foot)<1 for k,q in enumerate(poles) if k!=f)
    return dict(vertices=z,D=D,J=J,centroid=g,poles=poles,
                frame_indices=(chosen_r,chosen_s),axes=(u,w,v),L_lower=L0,
                M_polynomial=primal_mats,L_squared_N_polynomial=inverse_mats,
                M_at_lower=M,N_at_lower=N,all_68_rows=rows,edge_packets=packets,
                S=S,U=U,H=H,physical_weak_points=0,zero_primitives=0,
                ray_scope='Every real L>=L_lower, with the literal same inverse')


def encode(x):
    if isinstance(x,Q):
        return str(x)
    if isinstance(x,dict):
        return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):
        return [encode(v) for v in x]
    return x


def main():
    if not __debug__:
        raise RuntimeError('Assertions must remain enabled')
    D0,J0,g0=moments(Y)
    assert D0==Q(881291,1600000)
    assert g0==(Q(7368835529,28201312000),Q(3427883561,28201312000),Q(50317,153268))
    certificate=constant_certificate()
    closed_checks=[]
    for h,k,a in product((Q(0),EPS),repeat=3):
        body=horizon_geometry(h,k,a)
        body['hull']=hull(body['vertices'])
        if not a:
            if h and k:
                assert body['hull']['fvector']==(6,10,6)
                assert body['centroid'][0]==Q(1,4)
            else:
                assert body['hull']['fvector']==(4,6,4)
        closed_checks.append(body)
    flag_records=[]
    for perm in permutations(range(4)):
        spec=flag_spec(perm)
        strata=[]
        for mask in range(8):
            t=tuple(Q(0) if mask>>j&1 else Q(1,2) for j in range(3))
            z,D,J,g=flag_geometry(spec,t)
            strata.append(dict(zero_mask=mask,parameters=t,vertices=z,
                               D=D,J=J,centroid=g,hull=hull(z)))
        flag_records.append(dict(specification=spec,strata=strata))
    assert len(flag_records)==24
    finite=horizon_geometry(EPS,EPS,EPS)
    control1=physical_ray(finite['vertices'])
    denominators=tuple(sum(y) for y in Y)
    assert min(denominators)==Q(17,160)>0
    apparent=tuple(scale(1/d,sub(y,g0)) for y,d in zip(Y,denominators))
    control2=physical_ray(apparent)
    assert hull(apparent)['fvector']==(10,17,9)
    out=dict(object='W_TRIANGULAR_HORIZON_U2_AND_POSITIVE_FLAG_COMPACTIFICATION_V1',
             parent=PARENT,source_vertices=Y,source_faces=FACES,source_edges=EDGES,
             source_fan=FAN,source_six_volumes=W0,source_centroid=g0,
             literal_analytic_certificate=certificate,
             closed_wedge_checks=closed_checks,positive_flag_charts=flag_records,
             controls=(control1,control2),
             apparent_horizon=dict(functional=(0,1,1,1),anchor=g0,
                                   denominators=denominators),
             scope='The wedge is an analytic all-root U2 theorem. The 24 cubes are a complete realization compactification, not a completed all-sector mechanical cover.')
    raw=(json.dumps(encode(out),sort_keys=True,indent=2)+'\n').encode()
    path=Path('w_horizon_flags_report.json')
    path.write_bytes(raw)
    for p in (Path(__file__),path):
        data=p.read_bytes()
        print(p.name,len(data),hashlib.sha256(data).hexdigest())
    print('W_TRIANGULAR_HORIZON_U2_AND_24_FLAG_RECOVERY_PASS')


if __name__=='__main__':
    main()
```

The source is deliberately complete without a sandbox attachment. The literal four-matrix certificate and rational estimates above are the accepted mathematical content of this handoff; the unobserved executable and larger numerical libraries must not be described as author cold-replayed outputs.
