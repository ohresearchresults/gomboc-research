# minimum-0125

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# BALANCED_E17_COMPLETE_EIGHT_CUT_TWO_PROJECTIVE_NORMAL_FORM_V1

## 1. Determination and evidence boundary

**This continuation establishes a complete actual-geometry reduction for the entire balanced two-apex E17 incidence type, together with three exact nonrecord controls. It does not establish a new all-SPD exclusion or a class110 construction.**

Every genuine balanced two-apex body is an affine image of a member of an explicit eleven-real-parameter family: eight independently variable corner-cut lengths, one positive apex-separation parameter, and two projective denominator coefficients. The construction has no isosceles-cut restriction, no small-cut restriction, no parallel-middle-sides restriction on the original body, and no equal-apex-height restriction on the original body. Its centroid is always the centroid of the actual uniformly filled image.

The three new controls are outside the **full projective orbits of every body in the parent's isosceles-cut classes**, not merely outside its stated parameter boxes. They are also outside the full projective orbit of the older literal balanced pencil. One control has a below-COM apex and strict222; another has both strict unstable vertices in the base and strict222. None is110.

The accepted parent remains `minimum-0120`, declared SHA-256 `a4c45b5618195f1a579a49db25bfc93d945d69697fde14db4f689d25a098e26e`. Its two all-SPD exclusions are inherited results, not new results of this continuation. The global interval remains **34 <= C_min <= 622**, and no incidence registry changes.

The new 1,939-line journal update was read through EOF, including the literal parent. Its mounted bytes are 335566, SHA-256 `65830298e80a2c03aa3ced87984be6801658f72e958a5db1b08e8f85639f454a`. The unchanged supplied recovery wrapper still matches 20099 bytes and SHA-256 `0dfcb0c3b855b1d1e1a6256e958c6af3503d780353add523b559639411c8c44f`. No parent coefficient search was replayed. No unavailable archive, decoded BNw source, or research connector is a dependency of the new work.

## 2. Complete balanced normal form

Write

```text
t=((sx,sy),(wx,wy),(nx,ny),(ex,ey)).
```

The complete cut domain is

```text
sx,sy,wx,wy,nx,ny,ex,ey > 0,
sx+ex < 2,    wx+nx < 2,
sy+wy < 2,    ny+ey < 2.
```

For any a>0, define C(t,a) by these ten vertices:

```text
0=(-1+sx,-1,0)       1=(-1,-1+sy,0)
2=(-1,1-wy,0)        3=(-1+wx,1,0)
4=(1-nx,1,0)         5=(1,1-ny,0)
6=(1,-1+ey,0)        7=(1-ex,-1,0)
8=(-a,0,1)           9=(a,0,1).
```

For two further real parameters u,v put

```text
T_uv(x,y,z)=(x,y,z)/(1+u*x+v*y).
```

Require positivity at all ten vertices, equivalently

```text
1+u*x_i+v*y_i > 0     for i=0,...,7,
1-u*a > 0,           1+u*a > 0.
```

**Normal-form theorem.** Every full-dimensional convex3-polytope with a true octagonal facet, exactly two other vertices, E=17, and outside degrees(5,5), is an invertible affine image of `T_uv(C(t,a))` for parameters satisfying exactly the strict conditions above. Conversely, every member of this parameter domain has the balanced true maximal-face lattice.

This is an eleven-parameter cover, not a claim of a unique or minimal parametrization. All mechanical root locations and all SPD metrics remain available.

### Actual facets and edges throughout the domain

The maximal facets are exactly

```text
F0=(0,1,2,3,4,5,6,7)
F1=(0,8,1)   F2=(1,8,2)   F3=(2,8,3)
F4=(3,8,9,4)
F5=(4,9,5)   F6=(5,9,6)   F7=(6,9,7)
F8=(7,9,8,0).
```

The true edges are the basal eight-cycle, the four spokes from8 to0,1,2,3, the four spokes from9 to4,5,6,7, and(8,9). Thus V/E/F=10/17/9 everywhere in the stated domain.

The cut conditions say precisely that each original square side retains a positive-length segment. The four removed corner triangles are disjoint. The actual eight side supports are the nonnegative regions of

```text
1+y-z,
1-y-z,
1+x+(a-1)z,
1-x+(a-1)z,

sy*(1+x)+sx*(1+y)-sx*sy
  +(a*sy-sx-sy+sx*sy)*z,
wy*(1+x)+wx*(1-y)-wx*wy
  +(a*wy-wx-wy+wx*wy)*z,
ny*(1-x)+nx*(1-y)-nx*ny
  +(a*ny-nx-ny+nx*ny)*z,
ey*(1-x)+ex*(1+y)-ex*ey
  +(a*ey-ex-ey+ex*ey)*z.
```

Together with z>=0 these expose the listed facets. Each corner-cut support vanishes at its designated two basal vertices and its designated apex. At the other apex its value is respectively `2a*sy`, `2a*wy`, `2a*ny`, or `2a*ey`, strictly positive. The remaining nonincident supports are strict by the disjoint-cut conditions. Positive projectivity then preserves the complete lattice.

The geometric boundary where a cut vanishes or a side sum becomes2 is not silently included as the same E17 lattice. Mechanical weak walls inside the strict geometric domain are not excluded.

## 3. Proof that the normal form covers all balanced realizations

### 3.1 Equalizing the apex heights uses a positive projectivity

Start with the actual base in z=0 and apices A=(p,h), Z=(q,k), h,k>0. These are heights above the base, not above the body's centroid.

When h!=k, their line meets the base plane at a point E outside the closed base polygon. Otherwise the lower apex would lie in the convex hull of the base and the higher apex and would not be a vertex.

Choose an affine function ell on the base plane with ell(E)=0 and ell>0 on the entire base. Since A,Z,E are collinear,

```text
ell(p)/h = ell(q)/k = sigma.
```

Extend the denominator to `f(x,y,z)=ell(x,y)+eta*z`, choosing eta so sigma+eta>0. Then f is positive on the base and both apices, hence on the whole body. The projective map X/f(X) sends both apices to the same positive height `1/(sigma+eta)`. Choose the initial planar origin inside the base, so the denominator's constant term is positive and the map is invertible. When h=k this step is unnecessary.

After an affine change, take the equal-height apices to(-a,0,1),(a,0,1), and the two horizontal base supports to y=-1,+1. The two quadrilateral side facets force their basal edges to be parallel to the apex edge. Their intervening chains have three triangular facets each. Label the base as in Section2.

### 3.2 Rectifying the four intrinsic outer support lines

The middle edges of the left and right three-edge chains lie on

```text
x=l(y)=l0+l1*y,
x=r(y)=r0+r1*y.
```

These are actual supporting lines. Put

```text
d=r0-l0,       e=r1-l1.
```

Because the real top and bottom basal edges are nondegenerate and strictly separated from the other chain's support, `r(1)>l(1)` and `r(-1)>l(-1)`. Thus d>|e|.

The following explicit projectivity has denominator d+e*y, positive on the whole body:

```text
x'=[2*x-l(y)-r(y)+(l0+r0)*z]/(d+e*y),
y'=[d*y+e-e*z]/(d+e*y),
z'=d*z/(d+e*y).
```

It maps the four support lines on the base to x'=±1,y'=±1 and maps the apices to

```text
(-2a/d,0,1), (2a/d,0,1).
```

The eight transformed basal vertices therefore cut off exactly four corners of this square, with independent positive x- and y-cut lengths. Their surviving side lengths give exactly the four strict sum conditions of Section2. This proves projective equivalence to C(t,a'). It is not a declaration that an arbitrary graph realization is physical: the map was constructed from an existing convex body's actual supports.

### 3.3 Only two denominator directions are needed

Any projectivity positive on C(t,a) can be written

```text
H(X)=b+L*T_p(X),       T_p(X)=X/(1+p.X),
```

with L invertible. To see this, normalize its homogeneous matrix so the lower-right entry is1, and write its numerator as A*X+b. Then L=A-b*p^T. The constant denominator is positive because0 lies in the interior of the basal polygon.

Let p=(u,v,w) and c=1+w. Positivity at both apices gives c>|u|a, hence c>0. There is the exact body identity

```text
T_(u,v,w)(C(t,a))
 = diag(1,1,1/c) * T_(u,v,0)(C(t,a/c)).
```

It holds at every vertex, and positive projectivities map convex hulls to convex hulls. Thus the vertical denominator coefficient is absorbed into the positive apex-separation parameter and a final affine map. No denominator directions have been discarded without accounting for their effect on the actual shape.

### 3.4 One physical reciprocal metric

The projective normalization is a representation theorem, not a metric isometry. A mechanical metric is never pulled through a nonlinear projectivity by pretending it remains constant.

Instead reconstruct the actual normal-form image K=T_uv(C(t,a)), integrate its true centroid g_K, and express the original body as P=b+A*K. Then

```text
g_P=b+A*g_K,
X_P=A*X_K,
M_K=A^T*M_P*A,
N_K=A^(-1)*N_P*A^(-T),
q_K=A^T*q_P,
M_K*N_K=I.
```

All primal and polar Gram values agree. Varying M_P over SPD3 varies M_K bijectively over SPD3. This is the common metric convention throughout the reduction.

## 4. Exact actual centroid over the full independent-cut domain

The parent's compact moment formula extends to independent cut lengths without adding any free mass parameter.

Use corner signs

```text
sigma_x=(-1,-1,1,1),
sigma_y=(-1,1,1,-1).
```

For corner pairs(t_ix,t_iy), set

```text
Q  = sum_i t_ix*t_iy,
A  = 4-Q/2,
Hx = sum_i sigma_x[i]*t_ix*t_iy*(t_ix-3),
Hy = sum_i sigma_y[i]*t_ix*t_iy*(t_iy-3),
Rx = sum_i sigma_x[i]*t_ix*t_iy,
D  = 32-4Q+16a.
```

Then the uniform volume and centroid of C(t,a) are exactly

```text
Vol=(A+2a)/3,
g=(Hx-a*Rx, Hy, 8-Q+8a)/D.
```

**Derivation.** The corner removed at signs(sigma_x,sigma_y) has area `t_x*t_y/2` and centroid `(sigma_x*(1-t_x/3),sigma_y*(1-t_y/3))`. Subtracting its actual area moments gives basal first moments(Hx/6,Hy/6). Integrating the true transverse chord midpoints gives mixed center(-Rx/8,0). The actual slice at height z=s is `(1-s)B+[-as,as]e_x`. Its area is `A(1-s)^2+4as(1-s)`. Integrating this area and its true first moments yields the displayed formula. This is a continuous analytic identity, not an inference from sampled moment agreement.

For a positive projective change, let `f_i=1+u*x_i+v*y_i`, `Y_i=P_i/f_i`. In either actual apex fan, a tetrahedron tau with original six-volume d_tau has image six-volume

```text
d'_tau=d_tau/product_{i in tau} f_i.
```

Therefore

```text
Vol(T_uv C)=sum_tau d'_tau/6,
g(T_uv C)=sum_tau d'_tau*sum_{i in tau}Y_i
           /(4*sum_tau d'_tau).
```

There is also an explicit positive-denominator polynomial representation. Put

```text
F=product_{i=0}^9 f_i,
W_tau=d_tau*product_{i not in tau} f_i,
W=sum_tau W_tau,
D_projective=4*F*W,
N_projective=sum_tau W_tau*sum_{i in tau} P_i*(F/f_i).
```

Then `Vol=W/(6F)` and `g=N_projective/D_projective`; D_projective>0 everywhere in the physical domain. Here F/f_i denotes the product of the other nine factors, so the numerator is polynomial in the exact input parameters. The determinants are the actual fan determinants. Neither the fan selections nor their masses are independently fitted.

For full-domain searches, the eight cut variables have an exact open-unit-cube parametrization. Parametrize each of the disjoint side pairs `(sx,ex)`, `(wx,nx)`, `(sy,wy)`, `(ny,ey)` as

```text
(first,second)=(2*r*s,2*r*(1-s)),       0<r,s<1.
```

This covers the whole cut domain, including arbitrarily steep or shallow corner slopes and arbitrarily small surviving side segments. It does not impose a uniform artificial bound on the two projective coefficients; their ten actual positivity inequalities remain necessary.

## 5. Projective orbit separation

The four support lines used above are intrinsic to a labelled balanced roof: two carry the basal edges of the quadrilateral facets, and two carry the middle basal edges of the two three-triangle blocks. A projectivity of balanced bodies must map this set to the corresponding set.

Four lines in general projective position determine a frame in the dual plane. After normalizing this frame to the square, an equivalence between two normalized bases preserves the square's interior component: an interior point of one base maps to an interior point of the other. Its permutation of the square corners consequently preserves or reverses cyclic order. The eight possibilities are the ordinary affine dihedral symmetries of the square. Thus the eight normalized cut lengths, modulo these finite symmetries, provide a projective fingerprint for this purpose.

In particular, the property

```text
sx=sy, wx=wy, nx=ny, ex=ey
```

is invariant under those symmetries. It holds for every base in both parent classes, even after arbitrary further positive projective transformations and arbitrary affine maps. It fails for the new control below. This separates the new controls from the full projective orbits of the entire parent's isosceles-cut family, not just from one specimen.

For comparison, normalizing the older literal balanced base with its actual coordinate convention(x/100,y/10) gives the exact fingerprint

```text
((12/37,81/170),
 (11/27,37/59),
 (55/108,74/145),
 (113/148,189/335)).
```

Its multiset of eight lengths differs from the new fingerprint. Thus no square dihedral symmetry identifies them, and the new controls are outside that full projective orbit too. The other two older pencils have outside degree pairs(3,7),(4,6), so they cannot be projectively equivalent to these balanced bodies.

This fingerprint calculation uses the literal old basal coordinates only. It is not a new execution of the old pencil's mass or equilibrium certificate.

## 6. Three new exact actual controls

All three controls use the independent-cut fingerprint

```text
t=((1/5,7/10),(9/10,3/5),(4/5,1/4),(2/3,6/5)).
```

All three use the same displayed chart metric

```text
M=diag(10000,100,1),       N=diag(1/10000,1/100,1).
```

To obtain rational Euclidean coordinates, subtract each body's own actual centroid and apply `diag(100,10,1)`. The exact recovery records every centered vertex, pole, true edge, primitive, and strict label.

### 6.1 Independent-slope equal-height roof

Take C(t,3/2). Its actual moments are

```text
Vol=154/75,
g=(-1891/73920,-3/1760,229/616).
```

Its strict counts are323, with

```text
S={F0,F4,F8},
U={8,9},
H={(0,7),(3,4),(8,9)}.
```

All68 primitives are nonzero; there is no weak physical point.

### 6.2 Genuine two-direction projective, below-COM222 control

Uniformly refill `T_(1/2,1/8,0)(C(t,3/2))`. Its complete raw vertices are

```text
0=(-32/19,-40/19,0)
1=(-80/37,-24/37,0)
2=(-20/11,8/11,0)
3=(-4/43,40/43,0)
4=(8/49,40/49,0)
5=(32/51,8/17,0)
6=(40/61,8/61,0)
7=(8/25,-24/25,0)
8=(-6,0,4)
9=(6/7,0,4/7).
```

The actual filled moments are

```text
Vol=241082056337152/26611653516525,
g_x=-4704935355037216902671137/2386753032848083772992350,
g_y=-99969303202670662101794/397792172141347295498725,
g_z=6723928601317/6592087477969.
```

The centered apex heights are

```text
X8_z=19644421310559/6592087477969 > 0,
X9_z=-2957021471049/6592087477969 < 0.
```

Thus only8 is above the base-parallel central plane. The actual strict counts are222:

```text
S={F0,F8},
U={8,9},
H={(0,8),(2,8)}.
```

All68 primitives are nonzero and weak000 holds. This is an exact below-COM control outside all the preceding projective orbits. It is not110 and does not prove an all-SPD theorem for its neighborhood or orbit.

### 6.3 Nonparallel-middle-sides control with both unstable roots in the base

Let H act in homogeneous coordinates(x,y,z,1) by

```text
H=((2,-2/15,1,-1),
   (0,5,8/15,-8/15),
   (0,0,5,0),
   (0,-8/15,0,5)).
```

Take the actual body `H^(-1)(C(t,3/5))`. Its middle basal support lines are

```text
x=-2+y/3,       x=3-y/5,
```

which are not parallel. Its actual volume is `2394913788791/660478118850`, and its actual centroid is

```text
(1259488459028849458726349/5624135658768376518436800,
 -441712687274691121831/56241356587683765184368,
 3055391907641/9579655155164).
```

Its strict counts are222:

```text
S={F0,F8},
U={1,6},
H={(0,7),(2,3)}.
```

Both unstable vertices are basal; neither apex is unstable. All68 primitives are nonzero and weak000 holds.

The recovery converts this same body back to the two-denominator normal form, obtaining

```text
a'=3375/5561,       (u,v)=(0,8/75),
A=((5561/2250,5561/84375,-1141/2250),
   (0,5561/5625,-8/75),
   (0,0,1)),
b=(1141/2250,8/75,0).
```

It verifies actual body equality, centroid and volume transport, the common inverse metric, all100 primal Gram equalities and all81 polar Gram equalities, and identical strict feature labels. This chart is not counted as a fourth physical control.

## 7. Verification status, uncovered complement and continuation

The normal-form coverage and moment formulas above have analytic proofs. The executable independently reconstructs all120 supporting triples for each of the three controls, checks the genuine maximal facets and true edges, integrates both positive apex fans, reconstructs centered poles, and checks all four primitives on every actual edge. It also checks the projective fan-moment formula and the explicit affine/projective factorization.

A local source build/check and a source-only build/check in a fresh directory both completed with identical report bytes. These are new executed exact checks. No floating solver, random search, condition-number assumption or missing parent coefficient table is used.

**Uncovered equilibrium problem:** the reduction itself excludes no additional point of the eleven-parameter domain. The existence or impossibility of U1, or of strict110/weak000, outside the previously certified sectors remains unresolved. The arbitrary realizations of the(3,7) and(4,6) types and E17 geometries without a B8 facet are not covered by this balanced normal-form theorem. There is no global or local registry delta.

The useful continuation is to work on this complete independent-cut/two-denominator domain, using its exact determinant moments and one M,N pair, rather than enlarge an isosceles-cut collar. The decisive missing step is a genuine common-metric exclusion or a verified110 point in that domain; the three222/323 controls must not be mistaken for either.

No literature priority is claimed. Projective centroid fitting is a separate established topic, including Izmestiev's *Fitting centroids by a projective transformation*; no theorem from that paper is required by the elementary normalization and exact control checks supplied here.

## 8. Complete recovery capsule

Save the following complete source as `balanced_cut_normal_form.py`, UTF-8/LF with one terminal LF. Environment executed: CPython3.13.5, standard library only, assertions enabled. There are no external inputs, dependency packages, random seeds or nondefault solver settings.

```sh
python -S balanced_cut_normal_form.py build
python -S balanced_cut_normal_form.py check
sha256sum balanced_cut_normal_form.py balanced_cut_normal_form.json
```

Exact pins:

```text
balanced_cut_normal_form.py
9927 bytes
a4cf71ce483c0d8012461b73aea0b3f99b29c7dd47f145ecf476980c9abb798b

balanced_cut_normal_form.json
24161 bytes
2c7c960cf460a1c407064ce26de8d4a7dc8d848d47322833f83b6085557bf54a
```

Expected terminal output:

```text
raw SUH 3 2 3 WEAK 0 ZEROS 0
projective_below_COM SUH 2 2 2 WEAK 0 ZEROS 0
trapezoid SUH 2 2 2 WEAK 0 ZEROS 0
REPORT 24161 2c7c960cf460a1c407064ce26de8d4a7dc8d848d47322833f83b6085557bf54a
BALANCED_E17_EIGHT_CUT_TWO_PROJECTIVE_TRUE_GEOMETRY_RECOVERY_PASS
```

Supplementary copies: source (`balanced_cut_normal_form.py`) and complete exact report (`balanced_cut_normal_form.json`). The literal source below reconstructs the report without either link or any parent file.

```python
"""Exact balanced-E17 normal form and independent-slope controls.
CPython 3.13.5, standard library only, assertions enabled.
python -S balanced_cut_normal_form.py build|check
No external input, random input, or parent code is used.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib, json, sys
assert __debug__

def vadd(a,b): return tuple(x+y for x,y in zip(a,b))
def vsub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(a,t): return tuple(t*x for x in a)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def trans(A): return tuple(zip(*A))
def mv(A,x): return tuple(dot(r,x) for r in A)
def mm(A,B): return tuple(tuple(dot(r,c) for c in trans(B)) for r in A)
def ident(n): return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))
def inv(A):
 n=len(A); B=[list(map(F,r))+list(ident(n)[i]) for i,r in enumerate(A)]
 for j in range(n):
  k=next(k for k in range(j,n) if B[k][j]); B[j],B[k]=B[k],B[j]
  B[j]=[x/B[j][j] for x in B[j]]
  for i in range(n):
   if i!=j:
    t=B[i][j]; B[i]=[x-t*y for x,y in zip(B[i],B[j])]
 return tuple(tuple(r[n:]) for r in B)
def det(A):
 B=[list(map(F,r)) for r in A]; ans=F(1); n=len(B)
 for j in range(n):
  k=next((k for k in range(j,n) if B[k][j]),None)
  if k is None:return F(0)
  if k!=j:B[j],B[k]=B[k],B[j];ans=-ans
  t=B[j][j];ans*=t
  for i in range(j+1,n):
   q=B[i][j]/t
   for k in range(j,n):B[i][k]-=q*B[j][k]
 return ans
FACETS=((0,1,2,3,4,5,6,7),(0,8,1),(1,8,2),(2,8,3),(3,8,9,4),
        (4,9,5),(5,9,6),(6,9,7),(7,9,8,0))
EDGES=tuple(sorted({tuple(sorted((f[i],f[(i+1)%len(f)]))) for f in FACETS for i in range(len(f))}))
assert len(EDGES)==17

def domain(t):
 (sx,sy),(wx,wy),(nx,ny),(ex,ey)=t
 assert all(x>0 for c in t for x in c)
 assert sx+ex<2 and wx+nx<2 and sy+wy<2 and ny+ey<2

def roof(t,a):
 domain(t);assert a>0
 (sx,sy),(wx,wy),(nx,ny),(ex,ey)=t
 return tuple(tuple(map(F,p)) for p in ((-1+sx,-1,0),(-1,-1+sy,0),(-1,1-wy,0),
  (-1+wx,1,0),(1-nx,1,0),(1,1-ny,0),(1,-1+ey,0),(1-ex,-1,0),(-a,0,1),(a,0,1)))

def moment_formula(t,a):
 Q=sum(x*y for x,y in t); A=4-Q/2
 sx=(-1,-1,1,1);sy=(-1,1,1,-1)
 Hx=sum(s*x*y*(x-3) for s,(x,y) in zip(sx,t))
 Hy=sum(s*x*y*(y-3) for s,(x,y) in zip(sy,t))
 Rx=sum(s*x*y for s,(x,y) in zip(sx,t));D=32-4*Q+16*a
 assert A>0 and D>0
 return (A+2*a)/3,tuple(z/D for z in (Hx-a*Rx,Hy,8-Q+8*a))

def cells(V,apex):
 out=[]
 for f in FACETS:
  if apex in f:continue
  for j in range(1,len(f)-1):
   ids=(apex,f[0],f[j],f[j+1]);p=V[apex]
   d=abs(dot(vsub(V[ids[1]],p),cross(vsub(V[ids[2]],p),vsub(V[ids[3]],p))))
   assert d>0;out.append((ids,d))
 return out

def moment(V,apex):
 C=cells(V,apex);D=sum(d for _,d in C)
 J=tuple(sum(d*sum(V[i][k] for i in ids) for ids,d in C) for k in range(3))
 return D/6,tuple(x/(4*D) for x in J)

def project(V,p):
 f=tuple(1+dot(p,x) for x in V);assert min(f)>0
 return tuple(scale(x,1/y) for x,y in zip(V,f)),f

def project_moment(V,p,apex):
 Y,f=project(V,p);C=cells(V,apex)
 D=F(0);J=(F(0),)*3
 for ids,d in C:
  d=d/prod(f[i] for i in ids);D+=d
  J=vadd(J,scale(tuple(sum(Y[i][k] for i in ids) for k in range(3)),d))
 return D/6,scale(J,1/(4*D))
def prod(it):
 a=F(1)
 for x in it:a*=x
 return a

def hull(V):
 found=set()
 for i,j,k in combinations(range(len(V)),3):
  n=cross(vsub(V[j],V[i]),vsub(V[k],V[i]))
  if not any(n):continue
  vals=[dot(n,vsub(x,V[i])) for x in V]
  if max(vals)<=0 or min(vals)>=0:found.add(tuple(i for i,x in enumerate(vals) if x==0))
 assert found=={tuple(sorted(f)) for f in FACETS}
 edges=set()
 for a,b in combinations(found,2):
  s=set(a)&set(b)
  if len(s)==2:edges.add(tuple(sorted(s)))
 assert edges==set(EDGES)
 return sorted(found)

def audit(V,M):
 H=hull(V);vol,g=moment(V,8);assert (vol,g)==moment(V,9)
 X=tuple(vsub(x,g) for x in V);N=inv(M);assert mm(M,N)==ident(3)
 assert M==trans(M) and all(det(tuple(tuple(M[i][j] for j in range(k)) for i in range(k)))>0 for k in (1,2,3))
 Q=[]
 for f in FACETS:
  ids=next(ids for ids in combinations(f,3) if det(tuple(X[i] for i in ids)))
  q=mv(inv(tuple(X[i] for i in ids)),(F(1),)*3)
  assert all(dot(q,x)<=1 for x in X)
  assert {i for i,x in enumerate(X) if dot(q,x)==1}==set(f)
  Q.append(q)
 U=set(range(10));S=set(range(9));packets=[];saddles=[];weak={};zeros=0
 for i,j in EDGES:
  f,h=tuple(k for k,z in enumerate(FACETS) if i in z and j in z)
  d=(dot(X[i],mv(M,vsub(X[j],X[i]))),dot(X[j],mv(M,vsub(X[i],X[j]))),
     dot(Q[f],mv(N,vsub(Q[h],Q[f]))),dot(Q[h],mv(N,vsub(Q[f],Q[h]))))
  if d[0]>=0:U.discard(i)
  if d[1]>=0:U.discard(j)
  if d[2]>=0:S.discard(f)
  if d[3]>=0:S.discard(h)
  zeros+=sum(x==0 for x in d);packets.append(((i,j),(f,h),d))
  if max(d)<0:saddles.append((i,j))
  elif max(d)<=0:
   t=d[0]/(d[0]+d[1]);r=vadd(X[i],scale(vsub(X[j],X[i]),t));assert 0<=t<=1
   G=tuple(tuple(dot(Q[a],mv(N,Q[b])) for b in (f,h)) for a in (f,h))
   lam=mv(inv(G),(F(1),F(1)));assert min(lam)>=0
   assert mv(M,r)==vadd(scale(Q[f],lam[0]),scale(Q[h],lam[1]))
   weak[str(r)]={'point':r,'edge':(i,j),'t':t,'normal_coefficients':lam}
 assert len(U)+len(S)-len(saddles)==2 or weak
 return {'vertices':V,'centroid':g,'volume':vol,'maximal_facets':H,'edges':EDGES,
         'centered_vertices':X,'poles':Q,'M':M,'N':N,'S':sorted(S),'U':sorted(U),
         'H':saddles,'weak':list(weak.values()),'zero_primitives':zeros,'packets':packets}

def hmap(H,V):
 W=[]
 for x in V:
  y=mv(H,x+(F(1),));assert y[3]>0;W.append(scale(y[:3],1/y[3]))
 return tuple(W)

def rectify(V):
 # Equal-height apices (+/- a,0,1), horizontal basal supports y=+/-1.
 a=V[9][0]; assert V[8]==(-a,0,1) and V[9]==(a,0,1)
 assert V[0][1]==V[7][1]==-1 and V[3][1]==V[4][1]==1
 def line(i,j):
  slope=(V[j][0]-V[i][0])/(V[j][1]-V[i][1]);return V[i][0]-slope*V[i][1],slope
 l0,l1=line(1,2);r0,r1=line(5,6);d=r0-l0;e=r1-l1
 assert d>abs(e)
 H=((F(2),-l1-r1,l0+r0,-l0-r0),(0,d,-e,e),(0,0,d,0),(0,e,0,d))
 W=hmap(H,V)
 t=((W[0][0]+1,W[1][1]+1),(W[3][0]+1,1-W[2][1]),
    (1-W[4][0],1-W[5][1]),(1-W[7][0],W[6][1]+1))
 aa=2*a/d;domain(t);assert W==roof(t,aa)
 return t,aa,H

def split_projective(H,a,t):
 # H is positive on the source roof. Return affine after horizontal projectivity.
 assert H[3][3]>0
 H=tuple(tuple(x/H[3][3] for x in r) for r in H)
 p=H[3][:3]; b=tuple(H[i][3] for i in range(3))
 L=tuple(tuple(H[i][j]-b[i]*p[j] for j in range(3)) for i in range(3))
 c=1+p[2];assert c>0
 A=tuple(tuple(L[i][j]*(1/c if j==2 else 1) for j in range(3)) for i in range(3))
 source=roof(t,a/c);Y,f=project(source,(p[0],p[1],F(0)))
 Z=tuple(vadd(mv(A,x),b) for x in Y)
 assert Z==hmap(H,roof(t,a))
 return {'cuts':t,'a':a/c,'p':(p[0],p[1],F(0)),'affine_linear':A,'affine_translation':b}

def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [encode(v) for v in x]
 return x

def run():
 t=((F(1,5),F(7,10)),(F(9,10),F(3,5)),(F(4,5),F(1,4)),(F(2,3),F(6,5)))
 a=F(3,2);V=roof(t,a);assert moment_formula(t,a)==moment(V,8)==moment(V,9)
 M=((F(10000),F(0),F(0)),(F(0),F(100),F(0)),(F(0),F(0),F(1)))
 raw=audit(V,M)
 p=(F(1,2),F(1,8),F(0));Y,f=project(V,p);image=audit(Y,M)
 assert (image['volume'],image['centroid'])==project_moment(V,p,8)==project_moment(V,p,9)
 assert image['centroid'][2]>Y[9][2] and image['centroid'][2]<Y[8][2]
 # A genuine trapezoid example, rather than another parallelogram base.
 d=F(5);e=F(-8,15);l0=F(-2);r0=F(3);l1=F(1,3);r1=F(-1,5)
 H=((F(2),-l1-r1,l0+r0,-l0-r0),(0,d,-e,e),(0,0,d,0),(0,e,0,d))
 trapezoid=hmap(inv(H),roof(t,F(3,5)));tt,aa,HH=rectify(trapezoid)
 assert tt==t and aa==F(3,5) and HH==H
 trap=audit(trapezoid,M);fact=split_projective(inv(H),F(3,5),t)
 Z,_=project(roof(fact['cuts'],fact['a']),fact['p'])
 vz,gz=moment(Z,8);A=fact['affine_linear'];b=fact['affine_translation']
 assert trap['centroid']==vadd(mv(A,gz),b) and trap['volume']==abs(det(A))*vz
 Mc=mm(mm(trans(A),M),A);Nc=mm(mm(inv(A),inv(M)),trans(inv(A)))
 assert Nc==inv(Mc)
 for x in range(10):
  for y in range(10):
   x0=vsub(trapezoid[x],trap['centroid']);y0=vsub(trapezoid[y],trap['centroid'])
   xx=vsub(Z[x],gz);yy=vsub(Z[y],gz)
   assert dot(x0,mv(M,y0))==dot(xx,mv(Mc,yy))
 chart=audit(Z,Mc)
 assert chart['S']==trap['S'] and chart['U']==trap['U'] and chart['H']==trap['H']
 for i in range(9):
  assert chart['poles'][i]==mv(trans(A),trap['poles'][i])
  for j in range(9):
   assert dot(trap['poles'][i],mv(inv(M),trap['poles'][j]))==dot(chart['poles'][i],mv(Nc,chart['poles'][j]))
 # Projective normalization fingerprint of the older literal balanced B8 base.
 oldpairs=((-10,-10),(-14,-4),(-12,5),(-6,10),(7,10),(14,6),(16,-3),(5,-10))
 old=tuple((F(x,100),F(y,10),F(0)) for x,y in oldpairs)+((-F(1),F(0),F(1)),(F(1),F(0),F(1)))
 ot,oa,oH=rectify(old)
 assert sorted(x for c in ot for x in c)!=sorted(x for c in t for x in c)
 assert any(x!=y for x,y in t)
 return {'identity':'BALANCED_E17_COMPLETE_EIGHT_CUT_TWO_PROJECTIVE_NORMAL_FORM_V1',
  'parent':'minimum-0120',
  'parent_declared_sha256':'a4c45b5618195f1a579a49db25bfc93d945d69697fde14db4f689d25a098e26e',
  'cuts':t,'a':a,'p':p,'old_balanced_base_fingerprint':ot,'new_fingerprint':t,
  'raw':raw,'projective_below_COM':image,'trapezoid':trap,'trapezoid_factorization':fact}

if __name__=='__main__':
 assert sys.argv[1:] in (['build'],['check'])
 R=run();data=(json.dumps(encode(R),sort_keys=True,separators=(',',':'))+'\n').encode()
 path=Path(__file__).with_name('balanced_cut_normal_form.json')
 if sys.argv[1]=='build':path.write_bytes(data)
 else:assert path.read_bytes()==data
 for k in ('raw','projective_below_COM','trapezoid'):
  r=R[k];print(k,'SUH',len(r['S']),len(r['U']),len(r['H']),'WEAK',len(r['weak']),'ZEROS',r['zero_primitives'])
 print('REPORT',len(data),hashlib.sha256(data).hexdigest())
 print('BALANCED_E17_EIGHT_CUT_TWO_PROJECTIVE_TRUE_GEOMETRY_RECOVERY_PASS')
```
