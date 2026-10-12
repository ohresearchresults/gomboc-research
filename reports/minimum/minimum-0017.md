# minimum-0017

AI research report · 2026-09-07 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

# RAVEN_HEPTAGON_HEIGHT_COUPLING_ANALYTIC_V1

## Determination

**Neither complete heptagonal realization space, nor a complete joint-root system, is excluded here. No C30 attainer is supplied.** The new result is a genuinely coupled actual-mass/physical-metric obstruction. It excludes two explicitly specified, full-dimensional continuous cylinders, including the entire unbounded positive range of one physical anisotropy parameter. It also eliminates that parameter exactly from every full physical tree-record system, reducing the inherited fourteen-variable formulation to thirteen variables without introducing an independent inverse metric or independent mass variables.

The graph3 cylinder is rigorously bound to parent stable facet 1 and parent unstable vertex 7, and its proof covers all three records of `g3_s1_u7` simultaneously. It also excludes the other apex as sole unstable vertex in the same cylinder. The graph29 theorem below uses the literal canonical quadrilateral `(0,1,8,7)` and either canonical apex. Its parent unstable-apex labels are fixed by the supplied vertex map. **I do not certify a newly observed graph29 parent-facet rebinding in this handoff.** The supplied audit program derives that binding from the hash-pinned parent catalogue rather than assuming it. Consequently, the graph29 result must not yet be registered as a labeled closure of `g29_s1_u8`.

All **3,042 heptagonal records**, all **78 heptagonal joint-root orbits**, and the **178,131-record global frontier** remain globally unresolved. In particular, do not subtract five records, two root orbits, or either graph from the inherited frontier. The accepted bracket remains **30 ≤ C_min ≤ 1374**. The inherited physical reduction and its distinction between generated systems and proved exclusions are explicit in the supplied source. 

### Execution provenance

This is an analytic handoff with complete literal rational data and runnable verification source. **No successful execution marker from the new checker or parent audit was captured for this handoff.** The markers listed below are expected markers, not observed ones. No new source-file hash, binary frontier hash, successful SMT run, or machine-verified catalogue rebinding is asserted. The mathematical exclusion is proved below independently of an alleged solver run. The unobserved verification/audit is an explicit computational limitation, not evidence of feasibility or infeasibility outside the proved domain.

## 1. Parent identity, labels, and unchanged frontier

The immutable parent remains:

```text
minimum-0009
6f905a98d5d84d11e1369aebb34643ad59248a2485b95270c59bb52c48b92326
```

The late-preserved `RAVEN_HEPTAGON_PHYSICAL_V1` is journal evidence, not a new immutable parent. Its canonical vertex maps are used literally:

```text
canonical vertex -> parent vertex

graph3:  (0,6,4,1,5,2,3,7,8)
graph29: (6,0,1,3,2,5,4,8,7)
```

The canonical maximal-facet cycles used throughout this handoff are:

```text
graph3:
(0,4,5,6,2,3,1), (0,1,8,7), (2,7,8,3),
(0,7,4), (4,7,5), (5,7,6), (6,7,2), (3,8,1).

graph29:
(0,4,5,2,3,6,1), (0,1,8,7), (2,7,8,3),
(0,7,4), (4,7,5), (5,7,2), (3,8,6), (6,8,1).
```

These are maximal facets, not integration triangles promoted to facets. Each base vertex has exactly two base neighbors and one apex neighbor. The latter neighbors, in canonical base-vertex order 0 through 6, are:

```text
graph3:  (7,8,7,8,7,7,7)
graph29: (7,8,7,8,7,7,8)
```

For graph3 the canonical-to-parent facet map is exactly

```text
(0,1,2,6,3,4,5,7).
```

It can be checked directly against the literal parent facets:

```text
(0,5,2,3,4,1,6), (0,6,8,7), (1,4,7,8), (2,5,7),
(2,7,3), (3,7,4), (0,7,5), (1,8,6).
```

Thus canonical facet 1 and canonical apex 7 are precisely parent S1/U7 in graph3. The supplied canonical geometry and maps are recorded in the preserved physical result; the graph3 parent facets are also explicit in the immutable parent.  

The unchanged, reconstructible parent inputs are:

```text
e15_frontier.json
106553 bytes
9b7354d49fa9fb07ede494140fc0cde9a06f994f0359cb0a26b6ee3e8debe833

raven_remaining.bin
890655 bytes
5d3329d312adf3db48d9e22314d6cec046f4ec9b00b29fe248fa96f699bb3f1f
```

Their order-preserving filter to graph indices 3 and 29 remains:

```text
3042 records; 15210 bytes
c02fe56b8c0aaecd0c0cd13098723327c81ead01ea2a103c13df8d43a1aa71bd
```

No replacement remainder is defined by this result.

## 2. Actual shape and mass retained

Use the inherited nine shape parameters

```text
(beta,tau,s,x4,y4,x5,y5,x6,y6)
```

and points

```text
p0=(0,0,0), p1=(1,0,0), p2=(0,1,0),
p3=(beta*s,1+(tau-1)*s,0),
p4=(x4,y4,0), p5=(x5,y5,0), p6=(x6,y6,0),
p7=(0,0,1), p8=(beta,0,tau).
```

The domain is the complete inherited strict shape domain Phi: beta, tau, s, beta+tau-1, and 1+(tau-1)s are positive; the displayed base cycle is strictly convex and clockwise; and every prescribed maximal facet has strictly positive noncontact slacks. The first three outward planes are

```text
n0=(0,0,-1), h0=0;
n1=(0,-1,0), h1=0;
n2=(1-tau,beta,beta), h2=beta.
```

The other outward planes are the cross products from the displayed oriented triangular facets. This chart includes tau=1 and does not divide by tau-1. 

Write a=p7, b=p8, and C for the base cycle. Define

```text
S = -sum cross2(pi,pj),
M = -sum cross2(pi,pj)*(pi+pj),
```

where the sums run over the directed edges of C. For each displayed b-side triangle `(i,8,j)`, put

```text
dij = det(pi-a,b-a,pj-a).
```

There is one such triangle in graph3 and two in graph29. The actual six-volume and first-moment numerator are

```text
D = S + sum dij,
N = S*a + M + sum dij*(a+b+pi+pj),
B = 4D,
g = N/B.
```

These are actual positive apex-cone tetrahedral volumes. For a physical linear map T, volume is multiplied by |det T| and the centroid is T g. There are no free cone weights or free centroid coordinates. The checker independently compares this formula with the oriented boundary integral at both exact central shapes. The inherited all-parameter mass identity supplies the same formula on the full shape domain. 

Below write `g=(gx,gy,gz)`, `N=(X0,X1,Z)`, and `Y=X1`. Actual interior centering gives gy>0 and gz>0.

## 3. A complete physical-metric parameterization with one eliminable variable

Split chart coordinates into horizontal x in R2 and vertical z. Every positive-definite physical metric, up to a positive global scale, has the unique form

```text
A = ((a,c),(c,2-a)),    A positive definite,
ell = (ellx,elly),
kappa > 0,

G = ((A,       A ell),
     (ell^T A, ell^T A ell + kappa)).
```

The normalization is trace A=2, not trace G=1. Every inherited trace-G-normalized SPD metric reaches this normalization by positive scaling. Mechanical signs and all root norm orderings are unchanged by that scaling.

The SAME inverse metric is

```text
H = G^(-1)
  = ((A^(-1)+ell ell^T/kappa, -ell/kappa),
     (-ell^T/kappa,            1/kappa)),

det G = kappa det A.
```

This is a block factorization identity, not an independent choice of H. A physical realization is obtained by choosing R with R^T R=A and taking

```text
T = ((R, R ell),
     (0, sqrt(kappa))).
```

The orthogonal projection of the actual centroid to the base plane has chart coordinates

```text
c_base = (gx,gy) + gz ell.
```

### 3.1 Exact global elimination of kappa

For any vertex i, put

```text
Ri = B*(xi + zi*ell) - ((X0,X1)+Z*ell).
```

For a primal arrow i->j its physical shadow numerator is exactly

```text
ap_ij*kappa + bp_ij,

ap_ij = (B*zi-Z)*(zj-zi),
bp_ij = Ri^T A ((xj-xi)+(zj-zi)*ell).
```

For a facet f, write `nf=(mf,nfz)` and define

```text
Lf = B*hf - nf.N,
kf = nfz - mf.ell,
d = det A.
```

For a dual arrow f->h, the inherited adjugate numerator is exactly

```text
ad_fh*kappa + bd_fh,

ad_fh = mf^T adj(A) (Lf*mh-Lh*mf),
bd_fh = d*kf*(Lf*kh-Lh*kf).
```

Indeed, multiplying the inverse-metric expression by `det G=kappa*d` gives precisely this identity. Thus all fifteen selected arrow inequalities of every record are affine in the same kappa. Actual mass, shape incidence, the inherited leaf inequalities, and the core inequalities do not depend on kappa.

There is an exact quantifier-free elimination, including every zero-coefficient stratum. Given inequalities

```text
ak*kappa + bk > 0,
```

append `(a0,b0)=(1,0)` to enforce kappa>0. Existence of kappa is equivalent to the conjunction of

```text
ak != 0 OR bk > 0                         for every k,

ai <= 0 OR aj >= 0 OR ai*bj-aj*bi > 0     for every ordered pair i,j.
```

The first condition handles zero slopes. The second says that every strict lower endpoint is below every strict upper endpoint. When there is no upper endpoint, a sufficiently large kappa exists. When there is no lower endpoint besides zero, the appended row handles positivity. No bounded kappa interval is assumed.

Consequently the inherited full physical systems have **exact thirteen-variable equivalents**: nine shape variables, two normalized entries of A, and two shear coordinates ell. This is a reconstruction recipe for equivalent systems, **not an assertion that those thirteen-variable systems have been solved**.

## 4. New actual-mass/common-metric obstruction

For a base vertex i, let j(i) be its unique apex neighbor, and write

```text
pi=(xi,0), pj(i)=(yj,hi),   hi>0.
```

Define

```text
Ki = (xi-c_base)^T A (yj-xi+hi*ell),
Ui = Ki/(gz*hi),

L = ((gy/gz)^2-elly^2)/(A^(-1))yy.
```

These quantities depend only on the thirteen parameters retained after eliminating kappa.

### Theorem: common-height interval obstruction

For either displayed heptagonal lattice, an actual body whose sole stable facet is canonical facet 1 and whose sole unstable vertex is either apex must satisfy

```text
kappa > L,
0 < kappa < max_i Ui.
```

In particular, every parameter point satisfying

```text
L > max(0,U0,U1,U2,U3,U4,U5,U6)
```

is excluded for **every kappa>0**.

#### Proof of the primal upper bound

The shadow from base vertex i to its apex neighbor is exactly

```text
Ki - kappa*gz*hi.
```

Choose a base vertex i maximizing the actual squared distance to the actual centroid among the seven base vertices. For either of its base neighbors r,

```text
vi.(vr-vi)
 = (|vr|^2-|vi|^2-|vr-vi|^2)/2 < 0.
```

The strict inequality holds even when the two radii tie, because distinct vertices have positive separation. If all seven base-to-apex shadows are negative, this maximizing vertex also has negative shadow on its only remaining true edge. It is therefore a strict unstable vertex on the base. This contradicts either apex being the sole unstable vertex. Under the inherited strict class, some base-to-apex shadow must consequently be positive, giving kappa<max Ui.

Only true edges enter this argument. No integration diagonal is used as an escape edge.

#### Proof of the dual lower bound

The actual physical poles of the first two facets are the transforms of

```text
q0_chart = (0,0,-1)/gz,
q1_chart = (0,-1,0)/gy.
```

Using the same H=G^(-1),

```text
|q0|^2 = 1/(kappa*gz^2),
|q1|^2 = ((A^(-1))yy + elly^2/kappa)/gy^2.
```

A sole stable facet must be the unique closest supporting facet to the actual centroid. To see the needed necessity directly, a ball centered at the centroid with radius equal to the minimum supporting-plane distance lies inside the polytope. Its contact with a minimizing facet is in that facet's relative interior: equality with a different facet would require coinciding outward normal directions. Thus every minimizing facet gives a stable equilibrium. A prescribed sole stable facet must be the unique minimizer.

Therefore sole stability at facet 1 requires `|q1|>|q0|`, which rearranges to kappa>L. This uses the actual poles about the actual centroid, not a separately centered polar.

Combining the two inequalities proves the theorem.

### 4.1 Polynomial certificate without division

A fixed rational cut kappa0>0 suffices. Put

```text
J = det(A)*(Y^2-Z^2*elly^2) - kappa0*Z^2*A00,

Ei = (B*xi-(X0,X1)-Z*ell)^T A (yj-xi+hi*ell)
     - kappa0*Z*hi.
```

If

```text
J>0 and E0<0, E1<0, E2<0, E3<0, E4<0, E5<0, E6<0,
```

then the whole positive kappa axis is excluded. For `0<kappa<=kappa0`, facet 0 has larger pole norm than facet 1. For `kappa>=kappa0`, every base-to-apex shadow is strictly negative, producing a base unstable vertex.

This defines an explicit semialgebraic forbidden region in the full, otherwise unbounded thirteen-parameter domain. The result is not limited to the boxes constructed next.

## 5. Two literal non-affine cylinders, with the whole positive kappa axis closed

Use the SAME rational cut for both graphs:

```text
kappa0 = 2/5,
epsilon = 1/10000000.
```

For each graph, independently vary all thirteen coordinates listed below within the closed interval of radius epsilon about their listed centers. The two A coordinates are A00 and A01; set A11=2-A00. Leave kappa completely unrestricted in `(0,infinity)`.

```text
graph3 shape center:
(beta,tau,s,x4,y4,x5,y5,x6,y6)
= (1,1,1,-3/5,1/5,-4/5,1/2,-3/5,4/5)

(A00,A01) = (1,0)
ell = (-2151/635,1043/1270)

graph29 shape center:
(beta,tau,s,x4,y4,x5,y5,x6,y6)
= (1,1,1,-3/5,1/4,-3/5,3/4,13/10,1/2)

(A00,A01) = (1,0)
ell = (-8367/2600,577/650)
```

All nine shape parameters vary independently, including tau on both sides of 1. These are not fixed-affine bodies or equal-height-only slices. Together with the independent positive kappa coordinate, each cylinder has nonempty interior in the fourteen-dimensional physical chart.

### 5.1 Exact central certificates

The actual central masses, projected centroids, and decisive bounds are:

```text
graph3:
D = 102/25
N = (621/125,281/50,127/25)
g = (207/680,281/816,127/408)
c_base = (-3/4,3/5)
L = 221544/403225
max Ui = U5 = 25194/80645
J at kappa0 = 60254/15625
max Ei at kappa0 = E5 = -7064/15875

graph29:
D = 21/5
N = (657/100,29/5,26/5)
g = (219/560,29/84,13/42)
c_base = (-121/200,31/50)
L = 48174/105625
max Ui = U5 = 52521/3380000
J at kappa0 = 23696/15625
max Ei at kappa0 = E5 = -1299479/650000
```

At both centers, U5 is positive and every other Ui is negative. The following simpler rational margins hold for both:

```text
L - 2/5 > 1/20,
2/5 - max Ui > 2/25.
```

The base facet is not itself stable at these centers. Its orthogonal centroid projection lies strictly outside the base polygon. The relevant outward cross products are

```text
graph3, edge 5->6:  1/200 > 0,
graph29, edge 4->5: 1/400 > 0.
```

Thus this is not merely the observation that a stable heptagonal base conflicts with a different stable root.

At the two central shapes, all inherited branch-indexed leaf-mass conditions still pass for every kappa>0, because the actual deletion-volume fractions are invariant under the invertible physical map T. Those central shapes are exactly the inherited two actual mass controls. I do not claim that every point of the new boxes passes every inherited leaf condition. 

The coupling is nonvacuous even at the level of the new necessary tests. At either center, choosing a separate primal value `kappaP=1/100` makes the base exit 5->7 available, whereas a separate dual value `kappaQ=1` makes the pole comparison `|q1|>|q0|` hold. No common kappa satisfies both necessary conditions. This demonstrates only these two tests separately, not separate feasibility of complete primal and dual trees.

### 5.2 An explicit checker-independent bound over the boxes

Here are coarse rational error bounds sufficient to extend the central certificates to every point in the stated boxes. They deliberately avoid numerical eigenvalues and optimizer output.

Each point coordinate changes by at most `3 epsilon`, and all point coordinates have absolute value below 2. The shoelace and positive-cone formulas give

```text
|D-D_center| <= 600 epsilon,
|Nk-Nk_center| <= 5500 epsilon,
|gk-gk_center| <= 420 epsilon.
```

For the last bound, use D>4, central |Nk|<8, and the preceding two inequalities. In particular gz>3/10 throughout both boxes.

With the A and ell boxes, these imply

```text
|c_base,k-c_base,k_center| <= 2102 epsilon,
|L-L_center| < 50000 epsilon,
|Ui-Ui_center| < 760000 epsilon  for every i.
```

For reproducibility, the last bound follows by putting `u=xi-c_base`, `v=yj-xi+hi*ell`: componentwise `|u|<=3`, `|v|<=12`, `|delta u|<=2105 epsilon`, and `|delta v|<=20 epsilon`. Expanding the four entries of `u^T A v` bounds its change by `205000 epsilon`. The denominator gz*hi is greater than 3/10 and changes by at most `843 epsilon`; its central numerator has absolute value below 8. Division gives a change below `760000 epsilon`.

For L, write

```text
L = det(A)/A00 * ((gy/gz)^2-elly^2).
```

The ratio gy/gz changes by less than `6067 epsilon`, remains below 2, and |elly|<1. Also `|delta(det(A)/A00)|<=6 epsilon` and det(A)/A00<2. These give the displayed `50000 epsilon` bound.

At epsilon=1/10000000, the two errors are respectively less than 1/200 and 19/250. Hence throughout both boxes,

```text
L - 2/5 > 9/200 > 0,
2/5 - max Ui > 1/250 > 0.
```

The shape domain is also preserved throughout each box. At the central shapes, the minimum of the 35 base convexity guards and 42 noncontact guards is 3/25 for graph3 and 1/4 for graph29. A base cross-product guard changes by at most `96 epsilon`. A triangular-facet noncontact determinant changes by at most `1728 epsilon`, by telescoping its six triple products with coordinate differences bounded by 4 and perturbations bounded by `6 epsilon`. The three explicitly normalized planes have smaller errors. All guards therefore remain positive; A remains SPD because its least eigenvalue is at least `1-2 epsilon`.

This proves the two complete cylinders without restricting kappa to a finite interval, imposing a positive floor on kappa, or inferring anything from failed optimization.

## 6. Complete verifier source

Save the following as `verify_height.py`, UTF-8 with LF line endings. Reproduction target: CPython 3.13.5, standard library only, assertions enabled. No third-party dependency is used. The code checks the exact central fractions, actual mass by two integrations, strict interval guards for both thirteen-coordinate boxes, and 120 primal/dual affine-in-kappa identities with the same exact G and inverse H.

```python
from fractions import Fraction as F
from pathlib import Path
import hashlib

EPS = F(1,10**7)
CUT = F(2,5)
FAC = {
 3: ((0,4,5,6,2,3,1),(0,1,8,7),(2,7,8,3),
     (0,7,4),(4,7,5),(5,7,6),(6,7,2),(3,8,1)),
 29: ((0,4,5,2,3,6,1),(0,1,8,7),(2,7,8,3),
      (0,7,4),(4,7,5),(5,7,2),(3,8,6),(6,8,1))}
VM = {3:(0,6,4,1,5,2,3,7,8),29:(6,0,1,3,2,5,4,8,7)}
SH = {
 3: tuple(map(F,('1','1','1','-3/5','1/5','-4/5','1/2','-3/5','4/5'))),
 29: tuple(map(F,('1','1','1','-3/5','1/4','-3/5','3/4','13/10','1/2')))}
ELL = {3:(F(-2151,635),F(1043,1270)),
       29:(F(-8367,2600),F(577,650))}
TARGET = {3:(7,8,7,8,7,7,7),29:(7,8,7,8,7,7,8)}

class I:
 def __init__(self,a,b=None):
  if isinstance(a,I): self.lo,self.hi=a.lo,a.hi
  else: self.lo,self.hi=F(a),F(a if b is None else b)
  assert self.lo<=self.hi
 def __add__(self,x):
  x=I(x); return I(self.lo+x.lo,self.hi+x.hi)
 __radd__=__add__
 def __neg__(self): return I(-self.hi,-self.lo)
 def __sub__(self,x): return self+-I(x)
 def __rsub__(self,x): return I(x)+-self
 def __mul__(self,x):
  x=I(x)
  v=(self.lo*x.lo,self.lo*x.hi,self.hi*x.lo,self.hi*x.hi)
  return I(min(v),max(v))
 __rmul__=__mul__
 def __truediv__(self,x):
  x=I(x); assert x.lo>0 or x.hi<0
  return self*I(1/x.hi,1/x.lo)
 def __rtruediv__(self,x): return I(x)/self
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  r=I(1)
  for _ in range(n): r=r*self
  return r

def low(x): return x.lo if isinstance(x,I) else x
def high(x): return x.hi if isinstance(x,I) else x
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def scale(a,s): return tuple(s*x for x in a)
def cross(a,b):
 return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],
         a[0]*b[1]-a[1]*b[0])
def cross2(a,b): return a[0]*b[1]-a[1]*b[0]
def det(a,b,c): return dot(a,cross(b,c))
def mv(A,x): return tuple(dot(r,x) for r in A)

def points(q):
 b,t,s,x4,y4,x5,y5,x6,y6=q
 return ((0,0,0),(1,0,0),(0,1,0),(b*s,1+(t-1)*s,0),
         (x4,y4,0),(x5,y5,0),(x6,y6,0),(0,0,1),(b,0,t))

def planes(k,P,q):
 b,t=q[:2]
 ns=[(0,0,-1),(0,-1,0),(1-t,b,b)]
 hs=[0,0,b]
 for f in FAC[k][3:]:
  n=cross(sub(P[f[1]],P[f[0]]),sub(P[f[2]],P[f[0]]))
  ns.append(n); hs.append(dot(n,P[f[0]]))
 return ns,hs

def mass(k,P):
 C=FAC[k][0]; S=0; M=(0,0,0)
 for i,j in zip(C,C[1:]+C[:1]):
  w=-cross2(P[i],P[j]); S+=w
  M=add(M,scale(add(P[i],P[j]),w))
 D=S; N=add(scale(P[7],S),M)
 for f in FAC[k][3:]:
  if 8 not in f: continue
  i,_,j=f
  w=det(sub(P[i],P[7]),sub(P[8],P[7]),sub(P[j],P[7]))
  assert low(w)>0
  D+=w
  N=add(N,scale(add(add(P[7],P[8]),add(P[i],P[j])),w))
 assert low(D)>0
 return D,N

def boundary_mass(k,P):
 D=0; N=(0,0,0)
 for f in FAC[k]:
  for j in range(1,len(f)-1):
   a,b,c=(P[i] for i in (f[0],f[j],f[j+1]))
   w=det(a,b,c); D+=w
   N=add(N,scale(add(add(a,b),c),w))
 return D,N

def geometry(k,q,P):
 b,t,s=q[:3]
 for x in (b,t,s,b+t-1,1+(t-1)*s): assert low(x)>0
 C=FAC[k][0]; guards=[]
 for i,j in zip(C,C[1:]+C[:1]):
  for r in C:
   if r not in (i,j):
    guards.append(-cross2(sub(P[j],P[i]),sub(P[r],P[i])))
 ns,hs=planes(k,P,q)
 for f,n,h in zip(FAC[k],ns,hs):
  for i in range(9):
   if i not in f: guards.append(h-dot(n,P[i]))
 assert len(guards)==77
 assert min(map(low,guards))>0
 return min(map(low,guards))

def verify(k,q,a,c,ell,box=False):
 P=points(q); guard=geometry(k,q,P)
 D,N=mass(k,P); B=4*D; X=N[:2]; Y,Z=N[1:]
 A=((a,c),(c,2-a)); d=a*(2-a)-c*c
 assert low(a)>0 and low(d)>0
 J=d*(Y*Y-Z*Z*ell[1]*ell[1])-CUT*Z*Z*a
 exits=[]
 for i,j in enumerate(TARGET[k]):
  x=P[i][:2]; y=P[j][:2]; h=P[j][2]
  W=tuple(B*x[r]-X[r]-Z*ell[r] for r in range(2))
  V=tuple(y[r]-x[r]+h*ell[r] for r in range(2))
  exits.append(dot(W,mv(A,V))-CUT*Z*h)
 assert low(J)>0
 assert max(map(high,exits))<0
 g=scale(N,1/B)
 foot=tuple(g[r]+g[2]*ell[r] for r in range(2))
 i,j=(5,6) if k==3 else (4,5)
 outside=cross2(sub(P[j][:2],P[i][:2]),sub(foot,P[i][:2]))
 assert low(outside)>0
 if box:
  return guard,low(J),max(map(high,exits)),low(outside)
 assert guard=={3:F(3,25),29:F(1,4)}[k]
 assert boundary_mass(k,P)==(D,N)
 expected={
  3:(F(102,25),(F(621,125),F(281,50),F(127,25)),
     F(60254,15625),F(-7064,15875),F(221544,403225),F(25194,80645)),
  29:(F(21,5),(F(657,100),F(29,5),F(26,5)),
      F(23696,15625),F(-1299479,650000),F(48174,105625),F(52521,3380000))}[k]
 L=d/a*((Y/Z)**2-ell[1]**2)
 U=[(v+CUT*Z*P[TARGET[k][i]][2])/(Z*P[TARGET[k][i]][2])
    for i,v in enumerate(exits)]
 assert (D,N,J,max(exits),L,max(U))==expected
 assert [i for i,u in enumerate(U) if u>0]==[5]
 assert L-CUT>F(1,20) and CUT-max(U)>F(2,25)
 assert F(1,100)<max(U) and L<1
 H2=((A[1][1]/d,-c/d),(-c/d,a/d))
 Al=mv(A,ell)
 G=(A[0]+(Al[0],),A[1]+(Al[1],),
    (Al[0],Al[1],dot(ell,Al)+CUT))
 H=(tuple(H2[0][j]+ell[0]*ell[j]/CUT for j in range(2))+(-ell[0]/CUT,),
    tuple(H2[1][j]+ell[1]*ell[j]/CUT for j in range(2))+(-ell[1]/CUT,),
    (-ell[0]/CUT,-ell[1]/CUT,1/CUT))
 assert all(sum(G[i][r]*H[r][j] for r in range(3))==int(i==j)
            for i in range(3) for j in range(3))
 ns,hs=planes(k,P,q)
 slack=[B*h-dot(n,N) for n,h in zip(ns,hs)]
 assert min(slack)>0
 q0=B*B*dot(ns[0],mv(H,ns[0]))/(slack[0]*slack[0])
 q1=B*B*dot(ns[1],mv(H,ns[1]))/(slack[1]*slack[1])
 assert q0-q1==B*B*J/(CUT*d*Z*Z*Y*Y)
 edgefac={}
 for f,Fc in enumerate(FAC[k]):
  for i,j in zip(Fc,Fc[1:]+Fc[:1]):
   edgefac.setdefault(tuple(sorted((i,j))),[]).append(f)
 assert len(edgefac)==15 and all(len(v)==2 for v in edgefac.values())
 count=0
 for (i,j),(f,h) in edgefac.items():
  for u,v in ((i,j),(j,i)):
   W=sub(scale(P[u],B),N); e=sub(P[v],P[u])
   rp=tuple(W[r]+W[2]*ell[r] for r in range(2))
   re=tuple(e[r]+e[2]*ell[r] for r in range(2))
   ap=W[2]*e[2]; bp=dot(rp,mv(A,re))
   assert dot(W,mv(G,e))==ap*CUT+bp
   count+=1
  for u,v in ((f,h),(h,f)):
   mu,mv_=ns[u][:2],ns[v][:2]
   ku=ns[u][2]-dot(mu,ell); kv=ns[v][2]-dot(mv_,ell)
   adjA=((A[1][1],-c),(-c,a))
   ad=dot(mu,mv(adjA,sub(scale(mv_,slack[u]),scale(mu,slack[v]))))
   bd=d*ku*(slack[u]*kv-slack[v]*ku)
   z=sub(scale(ns[v],slack[u]),scale(ns[u],slack[v]))
   assert CUT*d*dot(ns[u],mv(H,z))==ad*CUT+bd
   count+=1
 assert count==60
 return expected

def main():
 for k in (3,29):
  print('EXACT_CENTER',k,verify(k,SH[k],F(1),F(0),ELL[k]))
  q=tuple(I(x-EPS,x+EPS) for x in SH[k])
  ell=tuple(I(x-EPS,x+EPS) for x in ELL[k])
  bounds=verify(k,q,I(1-EPS,1+EPS),I(-EPS,EPS),ell,True)
  print('CYLINDER_ALL_POSITIVE_KAPPA_PASS',k)
  print('STRICT_INTERVAL_BOUNDS',*(str(x) for x in bounds))
 print('COMMON_G_INVERSE_AND_120_SHADOW_IDENTITIES_PASS')
 print('BOTH_ACTUAL_MASS_CENTER_CERTIFICATES_PASS')
 print('TWO_13_PARAMETER_BOXES_TIMES_ALL_POSITIVE_KAPPA_PASS')
 b=Path(__file__).read_bytes()
 print('SOURCE_BYTES_SHA256',len(b),hashlib.sha256(b).hexdigest())

if __name__=='__main__': main()
```

## 7. Complete parent binding and unchanged-record audit source

This second unit does not assume the graph29 facet map. It locates literal ordered facet cycles in the pinned catalogue, checks their canonical dual mask, and matches cycles after the supplied canonical-to-parent vertex map. It then obtains the ordered dual-edge list from the same catalogue and reconstructs both parent arrays for every record in the two requested smallest root systems. Every returned record is printed completely.

Save as `audit_parent.py` beside `verify_height.py`:

```python
from pathlib import Path
from itertools import combinations
import hashlib,json,struct,sys
from verify_height import FAC,VM

PINS={
 'catalogue':(106553,'9b7354d49fa9fb07ede494140fc0cde9a06f994f0359cb0a26b6ee3e8debe833'),
 'remainder':(890655,'5d3329d312adf3db48d9e22314d6cec046f4ec9b00b29fe248fa96f699bb3f1f')}
MASK={3:5675263,29:7427327}

def read_pinned(path,key):
 b=Path(path).read_bytes();n,h=PINS[key]
 assert len(b)==n and hashlib.sha256(b).hexdigest()==h
 return b

def walk(x):
 yield x
 if isinstance(x,dict):
  for v in x.values(): yield from walk(v)
 elif isinstance(x,list):
  for v in x: yield from walk(v)

def cycle_key(c):
 c=tuple(c);r=c[::-1]
 return min(*(c[i:]+c[:i] for i in range(len(c))),
            *(r[i:]+r[:i] for i in range(len(r))))

def cycle_edges(c):
 c=tuple(c)
 return {tuple(sorted(e)) for e in zip(c,c[1:]+c[:1])}

def facet_array(x):
 return (isinstance(x,list) and len(x)==8 and
         all(isinstance(c,list) and len(c)>=3 and
             len(set(c))==len(c) and
             all(type(v) is int and 0<=v<9 for v in c) for c in x))

def dual_edges(faces):
 edges=[]
 for i,j in combinations(range(8),2):
  common=set(faces[i])&set(faces[j])
  assert len(common)<=2
  if len(common)==2:
   e=tuple(sorted(common))
   assert e in cycle_edges(faces[i]) and e in cycle_edges(faces[j])
   edges.append((i,j))
 return tuple(edges)

def dual_mask(edges):
 S=set(edges)
 return sum(1<<i for i,e in enumerate(combinations(range(8),2)) if e in S)

def parents(n,edges,root):
 assert len(edges)==n-1
 adj=[[] for _ in range(n)]
 for a,b in edges:adj[a].append(b);adj[b].append(a)
 p=[None]*n;p[root]=-1;queue=[root]
 for u in queue:
  for v in adj[u]:
   if p[v] is None:p[v]=u;queue.append(v)
 assert len(queue)==n
 return tuple(p)

def main():
 assert len(sys.argv)==3
 obj=json.loads(read_pinned(sys.argv[1],'catalogue'))
 raw=read_pinned(sys.argv[2],'remainder')
 nodes=list(walk(obj)); rows=list(struct.iter_unpack('<BBBH',raw))
 hept=[r for r in rows if r[0] in (3,29)]
 hb=b''.join(struct.pack('<BBBH',*r) for r in hept)
 assert len(hept)==3042 and len(hb)==15210
 assert hashlib.sha256(hb).hexdigest()=='c02fe56b8c0aaecd0c0cd13098723327c81ead01ea2a103c13df8d43a1aa71bd'
 assert [sum(r[0]==k for r in hept) for k in (3,29)]==[1446,1596]
 for k in (3,29):
  wanted=tuple(cycle_key(tuple(VM[k][v] for v in f)) for f in FAC[k])
  found=set()
  for x in nodes:
   if not facet_array(x):continue
   keys=tuple(map(cycle_key,x))
   if set(keys)!=set(wanted):continue
   de=dual_edges(x)
   if dual_mask(de)==MASK[k]:found.add(keys)
  assert len(found)==1
  keys=next(iter(found))
  fm=tuple(keys.index(w) for w in wanted)
  if k==3:assert fm==(0,1,2,6,3,4,5,7)
  expected_edges=set(dual_edges(keys)); orders=set()
  for x in nodes:
   if not isinstance(x,list) or len(x)!=15:continue
   if not all(isinstance(e,list) and len(e)==2 and
              all(type(v) is int and 0<=v<8 for v in e) for e in x):continue
   q=tuple(tuple(sorted(e)) for e in x)
   if set(q)==expected_edges:orders.add(q)
  assert len(orders)==1
  qe=next(iter(orders))
  pe=tuple(tuple(sorted(set(keys[f])&set(keys[h]))) for f,h in qe)
  assert all(len(e)==2 for e in pe)
  selected=[r for r in hept if r[:3]==((3,1,7) if k==3 else (29,1,8))]
  assert len(selected)==(3 if k==3 else 2)
  iv={v:i for i,v in enumerate(VM[k])}; iff={v:i for i,v in enumerate(fm)}
  print('LITERAL_PARENT_BINDING',k,'vertex_map',VM[k],'facet_map',fm)
  print('CANONICAL_F1_APEX7_PARENT_ROOTS',fm[1],VM[k][7])
  for graph,s,u,m in selected:
   assert m.bit_count()==7
   pp=parents(9,[e for j,e in enumerate(pe) if not (m>>j)&1],u)
   qq=parents(8,[e for j,e in enumerate(qe) if (m>>j)&1],s)
   pc=tuple(-1 if pp[v]<0 else iv[pp[v]] for v in VM[k])
   qc=tuple(-1 if qq[f]<0 else iff[qq[f]] for f in fm)
   print(json.dumps({'record':[graph,s,u,m],
                    'parent_primal':pp,'parent_dual':qq,
                    'canonical_primal':pc,'canonical_dual':qc},
                   sort_keys=True,separators=(',',':')))
 print('ALL_3042_HEPTAGON_RECORDS_PRESERVED_PASS')
 print('FIVE_SMALLEST_ROOT_RECORDS_LITERALLY_RECONSTRUCTED_PASS')

if __name__=='__main__':main()
```

The structural catalogue lookup is exact: it compares complete cycle keys, the complete supplied vertex map, and the exact canonical dual mask. If the catalogue schema or literal data do not expose a unique matching ordered edge list, it stops rather than substituting a guessed ordering.

### Reconstruction and verification commands

Reconstruct the two parent inputs from the immutable parent's complete capsule. Its cleaned base85 stream has 20,550 bytes and SHA-256 `f3fa7774ce124b35b8358211437a1495447fc413be9eda8e2586d2353cf8209e`; its decoded source-bundle JSON has 65,756 bytes and SHA-256 `673877e4fb7b06ff8abc907055f90b7f7efa1538bd8ca8555cff5bf8b3004ce2`.

```sh
python -S unpack_raven.py
python -S e15_graphs.py
python -S raven_frontier.py verify
python -S raven_frontier.py sweep 0 40
python -S raven_frontier.py sweep 40 74
python -S raven_frontier.py join
python -S verify_height.py
python -S audit_parent.py e15_frontier.json raven_remaining.bin
```

Expected new markers, **not observed markers in this handoff**, are:


[Encoded source block omitted; the code in this passage is incomplete.]


## 8. What remains and the useful continuation

The substantive advance is the **shared physical height interval**, not additional leaf-mass screening. Actual volume centering fixes the coefficients of the base-to-apex upper bounds, while the reciprocal metric fixes the stable-facet lower bound. At the exact controls these bounds are separately attainable with different metrics but incompatible with one metric. The explicit cylinders retain all nine moving shape parameters and the full unbounded positive kappa axis.

The next useful continuation is to run the literal parent audit, then apply the exact affine-in-kappa elimination to the five smallest full records, retaining every sign-zero coefficient case and every inherited actual-mass condition. The new forbidden region `L>max(0,Ui)` can be removed analytically first. The unresolved complement requires other true-facet pole comparisons, the remaining primal/dual arrows, or additional actual-mass geometry; its nonemptiness is not implied by the fact that this particular obstruction fails there. No finite subdivision in the remaining variables is justified as a global proof without a separate compact reduction or an algebraic treatment of the unbounded domain.
