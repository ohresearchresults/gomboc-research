# minimum-0075

Historical AI scientific report · saved 2026-09-16 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# E17_QUADRATIC_FLUX_MASS_RIGIDITY_V1

## Determination

The completed universal result is stronger than a further family test, but it must be distinguished from the exact matrix in the assignment:

**For every genuine convex three-polytope with (V,E,F)=(10,17,9), one can select a single actual vertex r such that the matrix with columns**

`(q_i, vec(q_i c_iᵀ), c_i, vec_sym(T_i), (q_i·r) vec_sym(T_i))`

**has column rank 9.** The selection uses only genuine vertex–facet incidence. It covers every realization, every admissible facet shape, nonsimple vertices, internal determinant-zero strata, and arbitrary reciprocal physical metrics. Thus **actual moments of spatial degree two, together with one directional quadratic boundary flux, are sufficient to determine the actual cone weights throughout E17**. Degree-four scalar moments are not required for this physical mass-closure task.

This does **not** prove that the smaller matrix `[Φ;c;T]` always has rank 9. I do not install a new counterexample to that smaller assertion in this handoff. A promising algebraic counterexample proposal and its complete exact-verification source are preserved below, but I do not have a captured successful complete verification transcript and authenticated new output pins for it. It remains a proposal, not an accepted negative answer.

Two additional conclusions are fully proved without numerical search: pure scalar degree-two facet moments are insufficient even on E17, as shown by an explicit rational body; and the degree-four scalar theorem is sharp among all nine-facet bodies, although that latter sharpness example is outside E17. No complete 110 root or type is excluded. The accepted bounds and register remain `V≥10,F≥9,C≥34`, with `632 types / 52585 joint-root orbits`. 

## 1. Authority and actual geometric scope

The authority used is the literal parent **minimum-0071**, **50197 bytes**, SHA-256 **d89e787ec8814b7a71d06c1c0ab7cb2674454f613f04273f0d193dfd30fc784e**. Its complete mathematical payload and both source units were read. Its belt family, exceptional curve, kernel, actual covariance, false-weight line and rational Euclidean 222 image are unchanged. In particular, the parent proves rank restoration by actual T_yy on its entire stated family, not on all E17 geometries. 

The current attachment is `research-journal(20260916-160152).md`, 4879169 bytes, SHA-256 `928ec32b519837a5ca18237393d0739e18bc4081fca239af378eda31e11dcaef`. The current synthesis was read before the relevant parent material. No unrelated archived payload or missing material file is used as an unstated premise. No incidence or object-identity conflict was found.

Throughout, P is one bounded full-dimensional convex polyhedron, with all maximal facets retained, translated to its **own uniform-volume centroid** 0. Let

`P={x:q_i·x≤1}`, `c_i=E_Fi x`, `T_i=E_Fi xxᵀ`, `Σ=E_P xxᵀ`,
`ω_i=Area(F_i)/(3 Vol(P) ||q_i||)`.

The area expectations are actual uniform measures. The physical metric, when used, is one SPD matrix M with its actual inverse N. No homogeneous centring of the polar is assumed.

The true balances are

`Σ_i ω_i q_i=0`, `Σ_i ω_i q_i c_iᵀ=I/3`,
`Σ_i ω_i c_i=0`, `Σ_i ω_i T_i=5Σ/3`, `Σ_i ω_i=1`.

For every fixed vector r, the true directional quadratic flux additionally gives

`Σ_i ω_i(q_i·r)T_i=0`.                                      (QF)

Indeed, apply divergence to the vector field `r x_a x_b`. The boundary integral is `Σ_i Area(F_i)(q_i·r)E_Fi(x_a x_b)/||q_i||`; its volume integral is `r_a ∫_P x_b+r_b ∫_P x_a=0`. The own-volume centroid is essential to this zero right-hand side. The identity itself is not claimed as a new discovery; the universal rank consequence below is the new step.

## 2. Sparse scalar-moment independence

Let M_d be the matrix whose i-th column contains all actual scalar facet moments `E_Fi x^α`, `|α|≤d`, including the constant row.

**Lemma. Any at most 2d+1 columns of M_d are linearly independent.** This holds for a subset of facets of a larger body as well.

Proof. Suppose a nonzero vector ν supported on at most 2d+1 facets annihilates M_d. The constant row gives `Σν_i=0`, so both signs occur. Change the overall sign so that the negative support I has cardinality at most d. The polynomial

`f(x)=Π_{j∈I}(1−q_j·x)`

has degree at most d. It vanishes identically on every negative facet. It is strictly positive in the relative interior of every other maximal facet, because distinct maximal facets cannot contain one another’s relative interiors. Hence every positively weighted facet has strictly positive actual mean of f, and

`Σ_i ν_i E_Fi f>0`,

contradicting the moment equations. This proof uses neither a lower area bound nor generic position. In particular, any three columns of M_1 and any five columns of M_2 are independent.

The parent’s degree-floor(F/2) theorem is the full-column version of this argument. Its proof and scope are preserved literally. 

## 3. Genuine vertex localization

For an actual vertex v define the coefficient vector

`ℓ_v(i)=1−q_i·v`.

It is zero exactly on the facets containing v and strictly positive on every other facet. Write `Star(v)` for the set of actual facets containing v.

If ν belongs to the kernel of `[Φ;c]`, then

`M_1(ℓ_v ⊙ ν)=0`                                             (L1)

for every actual v. The constant component follows from `Σν=0` and `Σνq=0`; here `Σν=0` is already the trace of `Σν q_i c_iᵀ=0`, since `q_i·c_i=1`. The linear components are

`Σ_i ν_i c_i − (Σ_i ν_i c_i q_iᵀ)v=0`.

If ν also annihilates the actual T block and the six additional rows `(q_i·r)T_i`, then

`M_2(ℓ_r ⊙ ν)=0`.                                           (L2)

This is a localization of coefficients on **actual facets**. It is not a selection of shadow arrows, independent cap rows or independently fitted moment matrices.

## 4. Universal E17 theorem with one directional quadratic flux

**Theorem.** A genuine nine-facet three-polytope having a vertex of degree 4, 5, 6 or 7 admits an actual vertex r for which

`rank [Φ;c;T;(q_i·r)T_i]=9`.

A deterministic selection is as follows. Choose any vertex v of degree 4 through 7. If its degree is 4 or 5, set r=v. If its degree is 6 or 7, let r be any genuine neighbour of v.

Proof for degree 4 or 5. Suppose ν annihilates this augmented matrix. By (L2), `ℓ_v⊙ν` is a scalar quadratic-moment kernel supported on at most `9−deg(v)≤5` facets. Sparse independence forces it to vanish. Thus ν is supported on `Star(v)`, which itself has at most five facets. Since `M_2ν=0`, sparse independence again gives ν=0.

Proof for degree 6 or 7. Equation (L1) first localizes at v. Its support outside `Star(v)` has at most three facets, so scalar affine independence forces `supp ν⊆Star(v)`. Now apply (L2) at the actual neighbour r. In a convex three-polytope exactly two maximal facets contain a given true edge. Thus

`|Star(v) \ Star(r)|=deg(v)−2≤5`.

The localized scalar quadratic kernel vanishes. Consequently ν is supported on the two facets containing the edge vr and must again be zero.

Every E17 body has such a vertex: every vertex degree is at least 3 and

`Σ_v(deg(v)−3)=2E−3V=34−30=4`.

At least one degree is at least 4, and no degree exceeds 7. This proves the theorem for **all** actual `(10,17,9)` realizations, independently of the catalogue and independently of which types have already been mechanically excluded.

Nonsimplicity causes no gap. The vertex figure is a polygon, so the number of incident maximal facets equals the true graph degree. Two adjacent vertices share exactly the two facets containing their true edge. Neither statement uses simplicial facets or a simple polyhedron.

### What is sufficient

At a fixed actual geometry, impose on candidate weights w the five displayed true balances in Section 1 and the single matrix equation (QF), with r selected as above. Subtract the actual weights ω. The theorem gives `w−ω=0`. The conclusion holds for arbitrary real candidate weights, not only positive ones.

There are at most **27 scalar rows**: 3 normal, 9 affine flux, 3 facet-centroid, 6 symmetric second-moment, and 6 directional quadratic-flux rows. The normalization is redundant by the trace. This is a degree-two **spatial-moment** system, with coefficients linear in the actual poles. It is not a claim that the resulting polynomial equations in unknown coordinates have total algebraic degree two.

The complete matrix `(1,q_i)⊗M_2[:,i]` therefore also has full column rank 9 on E17. Conversely, order one in this normal-linear hierarchy is insufficient: the parent’s exact belt has rank `[Φ;c]=8`. Thus **order two is the minimal universal spatial-moment order in this hierarchy**. 

This is a sufficient criterion for **mass identification**, not a realization criterion. If c_i and T_i are replaced by arbitrary vectors and PSD blocks, the sparse-independence proof no longer applies. If geometry is genuine, ω always exists; its uniqueness alone cannot exclude 110. A mechanical exclusion still requires showing that the genuine geometry and its unique actual weights cannot satisfy the requisite joint escapes.

No quantitative inverse bound is derived here. The lead’s separate degree-four stability argument is not duplicated or superseded by an unproved condition-number claim.

## 5. Exact E17 obstruction to pure scalar degree two

The distinction between scalar moments and normal-coupled moments is substantive. Consider the rational body

`P={|x|+|z|≤1, |y|+|z|≤1, x≤1/2}`.

This is an affine presentation of an edge-cut octahedron. The complete literal data, before translating by its actual centroid, are:

~~~text
V=[(-1,-1,0),(-1,1,0),(0,0,-1),(0,0,1),
   (1/2,-1,0),(1/2,1,0),(1/2,-1/2,-1/2),(1/2,-1/2,1/2),
   (1/2,1/2,-1/2),(1/2,1/2,1/2)]

N=[(-1,0,-1),(-1,0,1),(1,0,-1),(1,0,1),
   (0,-1,-1),(0,-1,1),(0,1,-1),(0,1,1),(1,0,0)]
h=(1,1,1,1,1,1,1,1,1/2)

F=[[0,1,2],[0,3,1],[2,8,6],[3,7,9],
   [0,2,6,4],[0,4,7,3],[1,5,8,2],[1,3,9,5],
   [4,6,8,5,9,7]]

E=[[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,5],
   [2,6],[2,8],[3,7],[3,9],[4,6],[4,7],[5,8],[5,9],[6,8],[7,9]].
~~~

The H inequalities give these ten vertices by their actual intersections; the listed supporting polygons have strict nonincidences. They comprise four triangles, four quadrilaterals and one hexagon. All seventeen listed edges are true edges.

Direct integration gives

`Vol(P)=9/4`, `o=(−1/8,0,0)`,
`Σ=diag(43/320,23/120,121/1080)`.

The actual area-to-raw-normal factors are

`(1,1,1/4,1/4,7/8,7/8,7/8,7/8,3/2)`.

The actual cone weights after centring are

`ω=(7/54,7/54,1/24,1/24,7/54,7/54,7/54,7/54,5/36)`.

Here are complete reconstruction formulas for the actual area moments. In each row below the six second-moment entries are ordered `(xx,yy,zz,xy,xz,yz)`, before centring. The signs τ and σ take the values determined by the displayed facet normal.

~~~text
F0,F1: τ=-1,+1
 g=(-2/3,0,τ/3)
 R=(1/2,1/6,1/6,0,-τ/6,0)

F2,F3: τ=-1,+1
 g=(1/3,0,2τ/3)
 R=(1/8,1/24,11/24,0,5τ/24,0)

F4,F5,F6,F7: (σ,τ)=(-1,-1),(-1,1),(1,-1),(1,1)
 g=(-2/21,9σ/14,5τ/14)
 R=(1/8,79/168,31/168,-9σ/112,-5τ/336,29στ/168)

F8:
 g=(1/2,0,0)
 R=(1/4,5/24,5/72,0,0,0).
~~~

The centred moments are exactly `c_i=g_i−o` and `T_i=R_i−g_ioᵀ−og_iᵀ+ooᵀ`. The actual poles are

`q0=(-8/7,0,-8/7), q1=(-8/7,0,8/7),`
`q2=(8/9,0,-8/9), q3=(8/9,0,8/9),`
`q4=(0,-1,-1), q5=(0,-1,1), q6=(0,1,-1), q7=(0,1,1), q8=(8/5,0,0)`.

The complete scalar quadratic kernel is

`ν=(85,−85,55,−55,−91,91,−91,91,0)`.

All ten scalar moments through degree two annihilate ν. Reflection in z cancels every even-z row; reflection in y cancels yz. The two remaining checks are

`−85(1/3)−55(2/3)+182(5/14)=0`,
`−85(−1/6)−55(5/24)+182(−5/336)=0`.

The rank is exactly eight. Under the two reflections, the even-even block has the following 4×4 minor:

~~~text
[[1,1,1,1],
 [-2/3,1/3,-2/21,1/2],
 [1/2,1/8,1/8,1/4],
 [1/6,1/24,79/168,5/24]],
 det=-45/448.
~~~

The odd-z block has 2×2 determinant `13/72` from rows z,xz and the left/right triangular pairs. The other two characters have nonzero entries `9/14` and `29/168`. Hence `rank M_2=4+2+1+1=8`.

Actual cubic moments remove the kernel. The means of x²z on the three upper-facet representatives are `1/10,3/40,1/35`; their lower counterparts have opposite signs. Therefore

`Σ_i ν_i E_Fi x²z=−297/20 ≠0`.

Centring does not change this kernel evaluation because the lower-degree rows already vanish. Thus `rank M_3=9` for this exact body.

This example does **not** disprove the assignment’s smaller normal-coupled matrix: `Σν_i q_iz=4532/63 ≠0`, so already adding the q_z row restores rank nine. Its false scalar-quadratic mass line is exactly `ω+tν`, `|t|<1/1320`; it is rejected by the normal balance. With M=N=I, vertices0 and1 are both strictly unstable, so this is not 110. Some other vertex primitives vanish; no strict chamber claim is made for this control.

More generally, replacing 1/2 by any `h∈(0,1)` gives the same genuine f-vector and the same reflection-character count: the odd-z scalar quadratic block has three facet-pair columns but only the two rows z,xz. Thus scalar degree-two rank is at most eight on that whole continuous family. Only the exact rank and cubic restoration at h=1/2 are asserted here.

## 6. Why the nine-facet count alone does not imply quadratic-flux rigidity

A separate exact non-record control shows the role of the E17 incidence hypothesis. Put `t=√2/2`, and take the eight base directions

`u=((1,0),(t,t),(0,1),(-t,t),(-1,0),(-t,-t),(0,-1),(t,-t))`.

Let the centred pyramid have base vertices `(u_j,−1/4)` and apex `(0,0,3/4)`. Its complete facets are the base cycle in reverse order and the eight triangles `(apex,j,j+1 mod8)`; its edges are the eight base edges and eight apex edges. Thus its f-vector is **(9,16,9), not E17**.

Its actual volume is `2√2/3`, centroid0 and covariance

`diag((4+√2)/40,(4+√2)/40,3/80)`.

The base cone weight is1/4 and every side weight3/32. The base pole is `(0,0,−4)`; each side pole is

`q_j=(4(u_j+u_{j+1})/[3(1+t)],4/3)`.

Each true triangular centre is the mean of its three vertices; its true second moment is `(ssᵀ+Σ_v vvᵀ)/12`, with s their sum. The base centre is `(0,0,−1/4)` and its second moment is `diag((4+√2)/24,(4+√2)/24,1/16)`. These formulas specify every facet moment exactly over Q(√2).

In base-first facet order, `ν=(0,1,−1,1,−1,1,−1,1,−1)` annihilates **all scalar moments through degree three** and also the full normal-linear quadratic matrix `(1,q_i)⊗M_2[:,i]`. Indeed the side facets are rotated through angles jπ/4. A scalar polynomial of degree≤3 has angular modes only −3 through3; normal times a scalar quadratic has the same restriction. Alternating coefficients annihilate every such mode.

The ranks are exactly eight: scalar moments supply all modes0,±1,±2,±3 on the side facets, and the base column is separated by `z−1/12`. The corresponding complex triangle-moment coefficient of degree r is proportional to `sin((r+1)π/8)/sin(π/8)`, nonzero for r=1,2,3. The degree-four alternating mode is nonzero, so scalar degree four restores rank nine. Consequently degree four is genuinely sharp for the unrestricted class of nine-facet bodies, while **pure scalar degree three on E17 remains unresolved here**.

For M=N=I all nine vertices are strictly unstable, all nine facets are strictly stable, and all sixteen edges are saddles. This is an exact physical `(9,9,16)` control, not a 110 witness. Its apex has degree8 and its other vertices degree3, so it does not meet the degree4–7 hypothesis of Section4.

## 7. Proposed algebraic counterexample to the bare matrix — not accepted without replay

A numerical proposal led to a particularly economical exact reconstruction problem. It could settle the remaining bare `[Φ;c;T]` question negatively, but **it is not counted as a certified counterexample in this handoff**. The exact interval-verifier calls were attempted; a captured successful complete transcript and authenticated new output pins are not available here. No observed PASS, byte count or SHA is invented for this new capsule.

The proposal uses reflection in z, not independent moment blocks. There are four upper facet planes `(a_i,b_i,1)·x=h_i`, their four reflected lower planes, and the true cap x=0. With b=1/2, the five unknowns are `(a,c,m,d,e)`, where m is a plane coefficient, not the volume centroid:

~~~text
upper normals: (0,-1,1),(a,1/b,1),(c,m,1),(d,e,1)
upper supports: 1,1,1,H; H=-d-e
cap: x<=0
~~~

The proposed isolating centre is literally

~~~text
(1.715701158033858,
 -0.1467378366871057,
 0.2967491976190772,
 -4.188209982907966,
 -0.6681749617245179)
~~~

with radius `2^-30` in every coordinate. Every displayed decimal is an exact rational input. The continuation parameter is `|b−1/2|≤2^-42`.

The top vertices are `C=(0,0,1)`, `P=intersection(upper0,upper2,upper3)`, `Q=intersection(upper1,upper2,upper3)`. The four equatorial vertices are `(0,-1,0)`, `(0,b,0)`, `(-1,-1,0)` and `R`, where `R_z=0` and R lies on upper1 and upper3. Reflect C,P,Q to obtain the other three vertices. The complete labelled cycles and edges are in the source below.

For the four actual upper facets, let A_i be projected xy area, g_i the actual uniform-area centre, and R_i its actual raw second moment. Then

`V=2ΣA_i g_iz`,
`o=(2ΣA_i(R_i)_xz/V,2ΣA_i(R_i)_yz/V,0)`.

Let κ be the signed four cofactors of the 3×4 matrix with rows `1,g_x,g_y`, and let `hhat_i=h_i−n_i·o`. The five rational equations are

~~~text
Σκ_i n_ix g_iz=0,
Σκ_i n_iy g_iz=0,
Σκ_i h_i g_iz=0,
Σκ_i hhat_i (R_i)_xz=0,
Σκ_i hhat_i (R_i)_yz=0.
~~~

At any genuine solution the full exact kernel is

`ν=(hhat0κ0,hhat1κ1,hhat2κ2,hhat3κ3,−hhat0κ0,−hhat1κ1,−hhat2κ2,−hhat3κ3,0)`.

This is not merely an interval-zero test. Cofactor identities kill `Σκ`, `Σκg_x`, `Σκg_y`. Reflection kills every even-z row. The first two equations kill the remaining normal-affine rows. The third, minus the appropriate multiples of the first two, kills `Σνc_z`. The fourth and fifth, minus the corresponding centroid terms, kill `ΣνT_xz` and `ΣνT_yz`. Hence all rows of `[Φ;c;T]` vanish **algebraically** at an exact solution.

The verifier is intended to prove existence and uniqueness by a rational interval contraction, not by declaring its decimal centre to be a zero. Its other checks seek an actual scalar quadratic rank-eight minor, nonzero actual cubic and directional quadratic-flux kernel images, genuine maximal facets, and a strict 222 Euclidean image using one rational reciprocal pair. Until the full verifier reaches its final marker, these remain proposed checks, not accepted findings.

The following is the complete candidate recovery source. It requires CPython3.13.5 standard library only, assertions enabled, no random choices and no optimizer. Save as `second_flux_candidate.py` and run `python -S second_flux_candidate.py`. It prints the resulting report’s bytes/SHA and its own bytes/SHA only after all checks succeed. The intended final marker is `PROPOSED_E17_SECOND_MOMENT_COUNTEREXAMPLE_ALL_CHECKS_PASS`. The literal equations and inputs below, rather than a worker-local file, preserve the proposal. No normative output pin is asserted before that replay.

```python
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib,json
assert __debug__
BITS=144; SCALE=1<<BITS
CENTER=tuple(map(F,['1.715701158033858','-0.1467378366871057','0.2967491976190772','-4.188209982907966','-0.6681749617245179']))
B0=F(1,2); RAD=F(1,2**30); BRAD=F(1,2**42)
class I:
 def __init__(self,x=0,hi=None):
  if hi is not None:self.lo,self.hi=x,hi
  elif isinstance(x,I):self.lo,self.hi=x.lo,x.hi
  else:
   x=F(x)*SCALE
   self.lo=x.numerator//x.denominator
   self.hi=-((-x.numerator)//x.denominator)
 def __add__(self,y):
  y=I(y);return I(self.lo+y.lo,self.hi+y.hi)
 __radd__=__add__
 def __neg__(self):return I(-self.hi,-self.lo)
 def __sub__(self,y):return self+-I(y)
 def __rsub__(self,y):return I(y)+-self
 def __mul__(self,y):
  y=I(y);v=[a*b for a in(self.lo,self.hi)for b in(y.lo,y.hi)]
  return I(min(v)//SCALE,-((-max(v))//SCALE))
 __rmul__=__mul__
 def inv(self):
  assert self.lo>0 or self.hi<0
  return I(SCALE*SCALE//self.hi,-((-SCALE*SCALE)//self.lo))
 def __truediv__(self,y):return self*I(y).inv()
 def __rtruediv__(self,y):return I(y)*self.inv()
 def __pow__(self,n):
  assert isinstance(n,int)and n>=0
  z=I(1)
  for _ in range(n):z=z*self
  return z
 def mag(self):return F(max(abs(self.lo),abs(self.hi)),SCALE)
 def mid(self):return F(self.lo+self.hi,2*SCALE)
 def pos(self):return self.lo>0
 def has0(self):return self.lo<=0<=self.hi
 def sign(self):
  assert not self.has0()
  return 1 if self.lo>0 else -1
class D:
 def __init__(self,v=0,d=None):
  if isinstance(v,D):self.v,self.d=v.v,v.d
  else:self.v=I(v);self.d=[I(0)]*6 if d is None else d
 def __add__(self,y):
  y=D(y);return D(self.v+y.v,[a+b for a,b in zip(self.d,y.d)])
 __radd__=__add__
 def __neg__(self):return D(-self.v,[-a for a in self.d])
 def __sub__(self,y):return self+-D(y)
 def __rsub__(self,y):return D(y)+-self
 def __mul__(self,y):
  y=D(y);return D(self.v*y.v,[a*y.v+self.v*b for a,b in zip(self.d,y.d)])
 __rmul__=__mul__
 def inv(self):return D(1/self.v,[-a/(self.v*self.v)for a in self.d])
 def __truediv__(self,y):return self*D(y).inv()
 def __rtruediv__(self,y):return D(y)*self.inv()
 def __pow__(self,n):
  z=D(1)
  for _ in range(n):z=z*self
  return z

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return [x-y for x,y in zip(a,b)]
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def det3(a):return dot(a[0],cross(a[1],a[2]))
def solve3(a,b):
 d=det3(a)
 return [det3([[b[i]if j==k else a[i][j]for j in range(3)]for i in range(3)])/d for k in range(3)]
def solve2(a,b):
 d=a[0][0]*a[1][1]-a[0][1]*a[1][0]
 return [(b[0]*a[1][1]-a[0][1]*b[1])/d,(a[0][0]*b[1]-b[0]*a[1][0])/d]
def tr(a):return list(map(list,zip(*a)))
def mm(a,b):return [[dot(r,c)for c in zip(*b)]for r in a]
def inverse(a):
 n=len(a);a=[list(map(F,row))+[F(i==j)for j in range(n)]for i,row in enumerate(a)]
 for j in range(n):
  p=next(i for i in range(j,n)if a[i][j]);a[j],a[p]=a[p],a[j]
  z=a[j][j];a[j]=[v/z for v in a[j]]
  for i in range(n):
   if i!=j:
    z=a[i][j];a[i]=[v-z*w for v,w in zip(a[i],a[j])]
 return [r[n:]for r in a]
def determinant(a):
 a=[row[:]for row in a];ans=I(1)
 for j in range(len(a)):
  p=next(i for i in range(j,len(a))if not a[i][j].has0())
  if p!=j:a[p],a[j]=a[j],a[p];ans=-ans
  z=a[j][j];ans=ans*z
  for i in range(j+1,len(a)):
   v=a[i][j]/z
   for k in range(j+1,len(a)):a[i][k]=a[i][k]-v*a[j][k]
 return ans

def geometry(p,b):
 a,c,m,d,e=p;H=-d-e
 n=[[0,-1,1],[a,1/b,1],[c,m,1],[d,e,1]];h=[1,1,1,H]
 hi=solve2([n[1][:2],n[3][:2]],[1,H])+[0]
 P=solve3([n[i]for i in(0,2,3)],[1,1,H])
 Q=solve3([n[i]for i in(1,2,3)],[1,1,H])
 vertices=[[0,-1,0],[0,b,0],[-1,-1,0],hi,[0,0,1],P,Q,[0,0,-1],[P[0],P[1],-P[2]],[Q[0],Q[1],-Q[2]]]
 upper=[[4,0,2,5],[4,6,3,1],[4,5,6],[5,2,3,6]]
 area=[];g=[];T=[];Z3=[]
 for face in upper:
  ar=0;fm=[0,0,0];sm=[[0]*3 for _ in range(3)];zm=0
  for j in range(1,len(face)-1):
   tri=[vertices[k]for k in(face[0],face[j],face[j+1])]
   u=sub(tri[1],tri[0]);v=sub(tri[2],tri[0])
   w=-(u[0]*v[1]-u[1]*v[0])/F(2)
   sums=[sum(v[k]for v in tri)for k in range(3)];ar=ar+w
   for k in range(3):
    fm[k]=fm[k]+w*sums[k]/F(3)
    for l in range(3):
     sm[k][l]=sm[k][l]+w*(sums[k]*sums[l]+sum(v[k]*v[l]for v in tri))/F(12)
   z=[v[2]for v in tri];zs=sum(z)
   zm=zm+w*(zs**3+3*zs*sum(v*v for v in z)+2*sum(v**3 for v in z))/F(60)
  area.append(ar);g.append([v/ar for v in fm])
  T.append([[v/ar for v in row]for row in sm]);Z3.append(zm/ar)
 volume=2*sum(ar*gi[2]for ar,gi in zip(area,g))
 o=[2*sum(ar*ti[k][2]for ar,ti in zip(area,T))/volume for k in range(2)]+[0]
 hh=[h[i]-dot(n[i],o)for i in range(4)]
 B=[[1]*4,[gi[0]for gi in g],[gi[1]for gi in g]]
 kap=[(-1)**i*det3([[row[j]for j in range(4)if j!=i]for row in B])for i in range(4)]
 rows=[[n[i][k]*g[i][2]for i in range(4)]for k in(0,1)]
 rows += [[h[i]*g[i][2]for i in range(4)]]
 rows += [[hh[i]*T[i][k][2]for i in range(4)]for k in(0,1)]
 eq=[dot(row,kap)for row in rows]
 return dict(equations=eq,vertices=vertices,n=n,h=h,area=area,g=g,T=T,Z3=Z3,volume=volume,centroid=o,hh=hh,kap=kap)

def differentiated(p,b):
 vals=list(p)+[b]
 v=[D(x,[I(int(i==j))for j in range(6)])for i,x in enumerate(vals)]
 f=geometry(v[:5],v[5])['equations']
 return [a.v for a in f],[a.d for a in f]
def box(c,r):return I(I(c-r).lo,I(c+r).hi)
def round64(x):
 z=F(x)*(1<<64)
 return F((2*z.numerator+z.denominator)//(2*z.denominator),1<<64)

f0,j0=differentiated([I(x)for x in CENTER],I(B0))
A=[[round64(v)for v in row]for row in inverse([[v.mid()for v in row[:5]]for row in j0])]
inverse(A)
X=[box(x,RAD)for x in CENTER];BI=box(B0,BRAD)
cert=[]
for bb in(I(B0),BI):
 fc,_=differentiated([I(x)for x in CENTER],bb)
 _,jac=differentiated(X,bb)
 L=[[I(int(i==j))-sum(A[i][k]*jac[k][j]for k in range(5))for j in range(5)]for i in range(5)]
 gamma=max(sum(v.mag()for v in row)for row in L)
 err=max((-sum(A[i][j]*fc[j]for j in range(5))).mag()for i in range(5))
 assert gamma<F(1,2)and err+gamma*RAD<RAD
 cert.append([gamma,err])
print('RATIONAL_CONTRACTION_FIXED_ROOT_AND_ENTIRE_PARAMETER_INTERVAL_PASS')

FC=[[4,5,2,0],[4,1,3,6],[4,6,5],[5,6,3,2],[7,0,2,8],[7,9,3,1],[7,8,9],[8,2,3,9],[0,7,1,4]]
INC=[[0,4,8],[1,5,8],[0,3,4,7],[1,3,5,7],[0,1,2,8],[0,2,3],[1,2,3],[4,5,6,8],[4,6,7],[5,6,7]]
E=[[0,2],[0,4],[0,7],[1,3],[1,4],[1,7],[2,3],[2,5],[2,8],[3,6],[3,9],[4,5],[4,6],[5,6],[7,8],[7,9],[8,9]]
g=geometry(X,BI)
V=[[I(v)for v in row]for row in g['vertices']]
n=[[I(v)for v in row]for row in g['n']];h=[I(v)for v in g['h']]
norm=n+[[a[0],a[1],-a[2]]for a in n]+[[I(1),I(0),I(0)]]
rhs=h+h+[I(0)];ef={}
for i,(face,ni,hi)in enumerate(zip(FC,norm,rhs)):
 for j,v in enumerate(V):
  s=hi-dot(ni,v)
  if i in INC[j]:assert s.has0()
  else:assert s.pos()
 for j in range(len(face)):
  p,q,r=[V[face[(j+k)%len(face)]]for k in range(3)]
  assert dot(ni,cross(sub(q,p),sub(r,q))).pos()
 for u,v in zip(face,face[1:]+face[:1]):
  ef.setdefault(tuple(sorted((u,v))),[]).append(i)
assert sorted(ef)==list(map(tuple,E))and all(len(v)==2 for v in ef.values())
assert [sum(v in e for e in E)for v in range(10)]==[3,3,4,4,4,3,3,4,3,3]
# Incidence equalities are identities of the defining linear solves.
# Nonincidences and convex turns above are strict interval inequalities.
# The closed, consistently oriented maximal-face lattice gives the whole hull.
areas=g['area']+g['area']+[BI+1]
rawg=g['g']+[[a[0],a[1],-a[2]]for a in g['g']]+[[I(0),(BI-1)/3,I(0)]]
rawT=g['T']+[[[(-1)**((i==2)+(j==2))*a[i][j]for j in range(3)]for i in range(3)]for a in g['T']]
rawT += [[[I(0),I(0),I(0)],[I(0),(BI*BI-BI+1)/6,I(0)],[I(0),I(0),I(F(1,6))]]]
o=[I(v)for v in g['centroid']];volume=g['volume'];assert volume.pos()
assert (volume-sum(a*b for a,b in zip(areas,rhs))/3).has0()
assert all((o[k]-sum(ar*hi*gi[k]for ar,hi,gi in zip(areas,rhs,rawg))/(4*volume)).has0()for k in range(3))
support=[hi-dot(ni,o)for hi,ni in zip(rhs,norm)]
assert all(v.pos()for v in support)
Q=[[v/hi for v in ni]for hi,ni in zip(support,norm)]
C=[sub(v,o)for v in rawg];XV=[sub(v,o)for v in V]
T=[[[a[i][j]-gi[i]*o[j]-gi[j]*o[i]+o[i]*o[j]for j in range(3)]for i in range(3)]for gi,a in zip(rawg,rawT)]
Sigma=[[sum(ar*hi*a[i][j]for ar,hi,a in zip(areas,rhs,rawT))/(5*volume)-o[i]*o[j]for j in range(3)]for i in range(3)]
omega=[ar*hi/(3*volume)for ar,hi in zip(areas,support)]
nu=[support[i]*g['kap'][i]for i in range(4)]
nu=nu+[-v for v in nu]+[I(0)]
assert all(not v.has0()for v in nu[:8])
Phi=tr([q+[q[i]*ci[j]for i in range(3)for j in range(3)]for q,ci in zip(Q,C)])
pairs=((0,0),(0,1),(0,2),(1,1),(1,2),(2,2))
S2=tr([[I(1)]+ci+[a[i][j]for i,j in pairs]for ci,a in zip(C,T)])
B=Phi+tr(C)+[[a[i][j]for a in T]for i,j in pairs]
assert all(dot(row,nu).has0()for row in B)
# Exact zero is proved by the cofactor identities and five root equations,
# not by the preceding interval-containment sanity check.
cols=[0,1,2,3,4,5,6,8];rows=None
for cand in combinations(range(10),8):
 try:z=determinant([[S2[i][j]for j in cols]for i in cand])
 except (AssertionError,StopIteration):continue
 if not z.has0():rows=list(cand);minor=z;break
assert rows is not None
Z3=g['Z3']+[-v for v in g['Z3']]+[I(0)]
cubic=dot(Z3,nu);assert not cubic.has0()
r=XV[2]
flux=[[sum(v*dot(q,r)*ti[i][j]for v,q,ti in zip(nu,Q,T))for j in range(3)]for i in range(3)]
assert not flux[0][2].has0()or not flux[1][2].has0()
tau=F(1,1000000);fake=[a+tau*b for a,b in zip(omega,nu)]
assert all(v.pos()for v in fake)
Lam=[[3*fake[j]*(1-dot(Q[i],C[j]))for j in range(9)]for i in range(9)]
for i in range(9):
 for j in range(9):
  if i==j:assert Lam[i][j].has0()
  else:assert Lam[i][j].pos()and(I(F(10,9))-Lam[i][j]).pos()
print('ACTUAL_E17_SCALAR2_AND_PHI_C_T_RANK8_KERNEL_CHECKS_PASS')
print('ACTUAL_CUBIC_AND_DIRECTIONAL_QUADRATIC_FLUX_RESTORE_RANK9_PASS')

AM=[[F(10),F(3),F(2)],[F(0),F(1),F(3)],[F(0),F(0),F(1,10)]]
M=mm(tr(AM),AM);N=inverse(M)
assert M==[[F(100),F(30),F(20)],[F(30),F(10),F(9)],[F(20),F(9),F(1301,100)]]
GX=mm(mm(XV,M),tr(XV));GQ=mm(mm(Q,N),tr(Q))
DP=[[GX[i][j]-GX[i][i]for j in range(10)]for i in range(10)]
AP=[[GQ[i][j]-GQ[i][i]for j in range(9)]for i in range(9)]
sp=[[0 if i==j else DP[i][j].sign()for j in range(10)]for i in range(10)]
sa=[[0 if i==j else AP[i][j].sign()for j in range(9)]for i in range(9)]
U=[i for i in range(10)if all(sp[i][j]<0 for j in range(10)if i!=j)]
S=[i for i in range(9)if all(sa[i][j]<0 for j in range(9)if i!=j)]
H=[list(e)for e,(i,j)in sorted(ef.items())if sp[e[0]][e[1]]<0 and sp[e[1]][e[0]]<0 and sa[i][j]<0 and sa[j][i]<0]
assert S==[0,5]and U==[2,4]and H==[[4,6],[7,8]]
print('SAME_RECIPROCAL_METRIC_EUCLIDEAN_222_ALL162_STRICT_SHADOWS_PASS')

def enc(v):
 if isinstance(v,I):return [str(F(v.lo,SCALE)),str(F(v.hi,SCALE))]
 if isinstance(v,F):return str(v)
 if isinstance(v,dict):return {k:enc(x)for k,x in v.items()}
 if isinstance(v,(list,tuple)):return [enc(x)for x in v]
 return v
out=dict(identity='E17_SECOND_MOMENT_KERNEL_ALGEBRAIC_CANDIDATE_V1',
parent=['minimum-0071','d89e787ec8814b7a71d06c1c0ab7cb2674454f613f04273f0d193dfd30fc784e'],
center=CENTER,radius=RAD,b_center=B0,b_radius=BRAD,precision=BITS,
preconditioner=A,contraction_certificates=cert,facets=FC,incidence=INC,edges=E,
vertices=V,H_normals=norm,H_rhs=rhs,volume=volume,centroid=o,
area_over_raw_normal=areas,poles=Q,area_centroids=C,facet_second_moments=T,
volume_covariance=Sigma,actual_cone_weights=omega,null_vector=nu,
full_Phi_c_T=B,scalar_degree2=S2,rank=8,minor_rows=rows,minor_columns=cols,
minor=minor,cubic_kernel_image=cubic,directional_vertex=2,
directional_quadratic_kernel_image=flux,fake_parameter=tau,fake_weights=fake,
physical_map=AM,M=M,N=N,vertex_shadow_signs=sp,pole_shadow_signs=sa,
stable_facets=S,unstable_vertices=U,saddle_edges=H,
representation='The exact object is the unique root of geometry(p,1/2)[equations] in CENTER+[-RAD,RAD]^5. Intervals enclose the entire certified b-curve, not substitutes for that algebraic definition.')
blob=(json.dumps(enc(out),sort_keys=True,separators=(',',':'))+'\n').encode('ascii')
Path('second_flux_candidate.json').write_bytes(blob)
print('PROPOSED_E17_SECOND_MOMENT_COUNTEREXAMPLE_ALL_CHECKS_PASS')
print('REPORT',len(blob),hashlib.sha256(blob).hexdigest())
raw=Path(__file__).read_bytes();print('SOURCE',len(raw),hashlib.sha256(raw).hexdigest())
```

## 8. Exact remaining questions and continuation

The **accepted** bare question remains: can a genuine E17 body have a nonzero ν simultaneously annihilating Φ, c and T? The proposed algebraic source is an immediate exact replay target, not a completed exclusion or authenticated counterexample. Its prospective interval proof is entirely finite: for the rational preconditioner A, it checks that `p↦p−AF(p,b)` maps the closed box strictly into itself and is a contraction, uniformly over the displayed b interval. Iteration then proves existence and uniqueness; no small residual is promoted to an exact zero. If that replay succeeds, the algebraic reduction supplies the full null certificate and the minor proves rank exactly eight. Until it succeeds with a saved transcript and pins, it must not change the accepted answer to the bare question.

The completed universal theorem is independent of that proposal: **actual quadratic normal flux with one incidence-selected vertex already gives full mass rigidity throughout E17**. Pure scalar degree two is definitively insufficient on the same slice. Pure scalar degree three may or may not be sufficient on every E17 geometry; the pyramid shows only that this cannot be inferred from F=9 alone. No result here identifies free moment arrays with geometry, transfers a volume centroid through polarity, or derives a 110 exclusion from rank alone.
