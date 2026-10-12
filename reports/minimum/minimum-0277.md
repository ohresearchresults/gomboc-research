# minimum-0277

AI research report · 2026-09-27 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# NONPARALLEL_W_THREE_CHART_ALLROOT_V2

## 1. Completed result

**For every h,k in [1,2] and every l>-1, the actual uniformly refilled projective image of the literal W body has at least two strict unstable equilibria under every SPD metric.** Every nonsingular affine image has the same conclusion. Incidental physical weak contacts, arbitrarily ill-conditioned metrics, and all ten choices of unstable root are included.

The exclusion is stronger than joint S1/U1 infeasibility: all **48,790 labelled true-edge rooted primal trees** are infeasible even for a nonzero PSD matrix, in each of three closed normalized charts. Thus no stable-root choice, actual root-foot position, or reciprocal polar escape alternative can produce S1/U1 in this domain. No covariance cap or independent polar metric is used. There is no assertion that S>=2 for every metric.

This completes a substantial nonparallel region that the literal parent had left unverified. It is a **newly generated and checked certificate**, not a recovery claim for the parent's unfinished certificate files. The eight basal projective invariants remain those of W; this is not the full eleven-modulus incidence. No canonical registry subtraction or global minimum improvement follows. The recorded interval remains 34<=C_min<=622. fileciteturn38file0L15-L33 fileciteturn29file0L9-L11

## 2. Input authority and observed parent replay

I read the current journal consecutively through line 1781/EOF, including the entire literal parent and its source. The mounted file has 330022 bytes and SHA-256 `e6420b699adf2b7ff8580d45c2b7158b15baf08a0b7fe3bd249eb135c78bef3a`.

The required parent is `minimum-0272`, manifest SHA-256 `51da02e247f4ec433c0cb936d8cf81aba1ed7724a3987ff134b945cc30a1e26c`. Its literal geometry, not an alias or an old unfinished library, is the input. The new proof programs import no earlier research program or certificate.

I also extracted and actually executed the parent's formerly unobserved consolidated source. `nonparallel_rational_controls.py` is 15676 bytes, SHA `c7ba52cfdf4562cfb9c708d2f7b9c4f5f212bd7352054070f572c7053f705ef0`; its regenerated report is 353698 bytes, SHA `71026ca27b8a6650fec69e34b996ba4c3e6847b1fa0872cc00d7a1cf6147033d`. Execution exited successfully with `NONPARALLEL_CHART_AND_RATIONAL_222_RECOVERY_PASS` and empty stderr. This repairs that execution gap; those generic 222 rays are not the new exclusion mechanism. No parent-geometry conflict was found. The parent's previous execution qualification is explicit. fileciteturn38file0L35-L51

## 3. Exact continuous domain and actual refill

The source vertices Y0,...,Y9 are

```
(17/80,0,0),       (629/800,0,0),
(187/250,51/500,0),(51/100,17/50,0),
(0,221/800,0),     (0,17/80,0),
(17/320,17/320,0), (0,0,1),
(3/20,0,1),       (0,3/20,1).
```

The complete outward maximal facet cycles F0,...,F8 are

```
(6,5,4,3,2,1,0), (8,7,0,1), (7,6,0),
(1,2,8), (9,8,2,3), (9,3,4),
(4,5,7,9), (6,7,5), (7,8,9).
```

The true lexicographic edges are

```
01,06,07,12,18,23,28,34,39,45,49,56,57,67,78,79,89.
```

Use exactly the nine positive tetrahedra

```
(7,6,5,4), (7,6,4,3), (7,6,3,2),
(7,6,2,1), (7,6,1,0), (7,1,2,8),
(7,9,8,2), (7,9,2,3), (7,9,3,4).
```

These are integration tetrahedra, not additional mechanical faces or edges. The source is the compact W body at `(x,r,p,q,lambda)=(1/10,9/10,3/25,3/5,3/20)`. Its literal parent supplies precisely these coordinates, cycles and fan. fileciteturn37file0L49-L108

For the theorem's entire domain, set

```
d_i=1+h*Y_ix+k*Y_iy+l*Y_iz,
Z_i=Y_i/d_i,
1<=h<=2, 1<=k<=2, -1<l<infinity.
```

All d_i are positive: basal denominators are at least 1, and the three top denominators are `1+l`, `1+l+3h/20`, `1+l+3k/20`. The homogeneous projective map has determinant 1 and is positive on the whole convex hull. It preserves the true lattice. A source support `n.Y<=b` becomes `(n+b*(h,k,l)).Z<=b`; there is no facetwise approximation.

Let w_T be the source six-volume determinant of a fan tetrahedron. Its projective six-volume is `w_T/prod_{i in T} d_i`. Therefore

```
D=sum_T w_T/prod_{i in T} d_i                 =6 Vol(P),
J=sum_T (w_T/prod_{i in T} d_i) sum_{i in T}Z_i=24 integral_P z dz,
g=J/(4D).
```

This is the new **uniform-volume** centroid. It is never replaced by the projective image of the old centroid. The independent audit checks the same moments using a different positive fan, with apex 0.

The two distinguished end planes are `z=0` and `h*x+k*y+(1+l)*z=1`. They are genuinely nonparallel throughout the domain. Since the heptagon determines its three outside vertices, which determine the triangular end, an affine equivalence cannot turn this distinguished pair into parallel planes.

### Three closed proof charts

| Chart | Third chart variable | Raw axial interval | Additional affine height normalization |
|---|---|---|---|
| Middle | l in [-1/2,1] | [-1/2,1] | Identity |
| Upper | t in [0,1/2], l=1/t-1 | [1,infinity) for t>0 | `diag(1,1,1/t)` |
| Lower | a in [0,1/2], l=a-1 | (-1,-1/2] for a>0 | `diag(1,1,a)` |

In every chart h,k range independently over the entire closed square [1,2]^2. The shared finite axial boundaries are included. The zero endpoints of the last two charts are used in the certificate but are not extra 10/17/9 bodies.

In the upper chart the basal vertices remain `Y_i/(1+hY_ix+kY_iy)` and the top vertices are

`(t*Y_ix,t*Y_iy,1)/(1+t*(hY_ix+kY_iy))`.

A fan tetrahedron with m top labels has normalized weight `w_T*t^(m-1)/prod dbar_i`. At t=0 the top labels coincide at 001. The actual full-dimensional limit is the **8/14/8 heptagonal pyramid**, with centroid height 1/4.

In the lower chart vertex 7 is 001 and

```
Z8=((3/20)/(a+3h/20),0,a/(a+3h/20)),
Z9=(0,(3/20)/(a+3k/20),a/(a+3k/20)).
```

Its normalized tetrahedral weight is `w_T/prod_{i in T, i!=7} dbar_i`; cancellation of the old denominator a is exact. At a=0 the actual base has old labels 0,8,9,5,6, and the limit is a **6/10/6 pentagonal pyramid**, also with centroid height 1/4. For c=17/80 this limiting base is the intersection

```
x>=0, y>=0, h*x+k*y<=1,
(1+c*h)*x+(3+c*k)*y>=c,
(3+c*h)*x+(1+c*k)*y>=c.
```

These five inequalities prove the limiting hull for every h,k in the square. Both limits retain positive volume; neither is a raw dimensional-loss artifact. The positive fan moments extend to the true limiting volume moments. These compactifications were established in the literal parent; the advance here is the completed mechanical certificate on their **entire closed cubes**, not an unevaluated neighborhood argument. fileciteturn37file0L118-L175

## 4. Complete true-tree implication

For any chart let z_i denote its normalized raw vertices, g its actual centroid, and fix the invertible gauge `G=diag(2,4,1)`. Put

```
X_i=G*(z_i-g),
R_i=4D*G*z_i-G*J=4D*X_i,
Q_ij=-sym(R_i,(G*z_j-G*z_i)).
```

For every physical metric A on these gauged coordinates,

`tr(A Q_ij)=-4D*X_i^T A (X_j-X_i)`.

An arbitrary SPD metric on the original body corresponds bijectively to an arbitrary SPD A after the chart's affine normalization and G. No restriction on A is introduced.

A strict unstable vertex has every true outgoing derivative negative. Every other vertex has a nonnegative true outgoing derivative. For SPD A, such an arrow gives

`||X_j||_A^2-||X_i||_A^2=2D_ij(A)+||X_j-X_i||_A^2>0`.

Thus a hypothetical sole strict U supplies a true-edge tree directed to that root, including when some selected derivatives are zero. The source enumerates all connected nine-edge subsets of the 17 true edges and roots each at all ten vertices. It obtains 4879 unrooted trees and 48790 rooted trees. The independent audit verifies 4879 by an exact Laplacian cofactor.

For each chart cell and each tree not already eliminated by an ancestor, the certificate supplies a nonnegative integer stress supported on arrows of that tree. Writing W for its weight sum, the exact acceptance proves

`sum w_ij Q_ij > (W/2^30) I`

throughout the entire closed cell. Therefore those arrows cannot all be nonnegative under any nonzero PSD A. Every remaining tree is passed to **both closed children**; a leaf is accepted only with no remaining tree. The checker validates every child, remaining-tree count, path and leaf, and rejects omitted or orphan nodes. Each chart's dyadic parameter-volume fraction is exactly one; this is parameter coverage, not physical body volume.

The stress shift 2^-30 is **not an eigenvalue floor for A**. No S1, covariance, conditioning, weak-freedom or chosen-foot premise appears.

There is also a uniform normalized-coordinate implication. The source has `D0=881291/1600000<1`. Middle weights give D<=8D0; upper weights give D<=D0; lower weights give D<=(400/9)D0<32. Hence every tree has a selected arrow satisfying

`D_ij(A)<-2^-37 tr(A)`

in its gauged normalized chart. This is a tree-stress margin, not a fixed labelled pair of unstable vertices.

## 5. Exact continuum acceptance, not a sampled matrix test

The source uses a degree-two polynomial enclosure with an explicitly bounded remainder, in normalized cell variables v in [-1,1]^3. A scalar is represented as

`f(v)=sum_{|alpha|<=2} c_alpha v^alpha / 2^96 + error(v),`

with `|error(v)|<=e/2^96`, where all c_alpha and e are integers. There are ten monomials. The following arithmetic is the analytic basis of the exact checker.

Addition adds coefficient arrays and error bounds. Multiplication convolves coefficients, retains total degree at most two, and bounds discarded monomials by the sum of their absolute coefficients. The product error additionally includes `e_f*||p_g||_1+e_g*||p_f||_1+e_f*e_g`, with the common scale accounted for. Every coefficient-rounding error is added with outward integer rounding. These estimates require no independence of errors.

For a reciprocal, choose the positive constant coefficient c0/2^96 and write `f=(c0/2^96)*(1+u)`. If the computed uniform bound is `|u|<=n/2^96<1`, use `1-u+u^2` and add the exact geometric-series remainder. In integer error units its additional bound is

`ceil(n^3/[c0*(2^96-n)])`.

A cell that fails this denominator-radius test is subdivided; it is never discarded as infeasible. The actual moment and arrow formulas are evaluated with this arithmetic. In particular, their common g is retained through R_i=4D*G*z_i-G*J rather than frozen or replaced by independent coordinate intervals.

The resulting quadratic polynomial converts exactly to tensor Bernstein degree (2,2,2), giving 27 coefficient matrices. In one variable the coefficient vectors for `1,v,v^2` are respectively `(1,1,1)`, `(-1,0,1)`, `(1,-1,1)`. Products give the three-variable transform.

For a symmetric matrix with entry-error bounds e_ij, its error is bounded below by `-diag(sum_j e_ij)`, since `2|x_i x_j|<=x_i^2+x_j^2`. The checker subtracts this diagonal correction and `I/2^30` **for each arrow**, before applying stress weights. It then checks all 27 weighted lower matrices by exact integer Sylvester minors. This proves the displayed strict Loewner inequality on the continuum: the Bernstein weights are nonnegative and sum to one, and the explicit remainder correction holds everywhere in the cell.

The 27 matrices are lower matrices of a rational-function enclosure, **not alleged exact polynomial coefficients of the original rational arrows**. The 18720 exact scalar spot comparisons in the auxiliary audit are implementation checks only; they are not the continuum proof.

Numerical LP/eigenvector cuts only locate weights and choose subdivisions. Every accepted weight row passes the exact integer test before use, and the saved certificate is checked again without invoking an optimizer. Failed LPs cause subdivision, never a feasibility or impossibility claim.

## 6. Observed complete certificates

| Chart | Nodes | Closed leaves | Maximum depth | Row records | Stress uses | Strict PD lower matrices | Positive leading minors |
|---|---:|---:|---:|---:|---:|---:|---:|
| Middle | 347 | 174 | 9 | 1389 | 46185 | 1246995 | 3740985 |
| Upper | 49 | 25 | 5 | 1039 | 7522 | 203094 | 609282 |
| Lower | 1107 | 554 | 13 | 2211 | 101900 | 2751300 | 8253900 |

There are **155607 stress applications, 4201389 strictly PD lower-matrix checks, and 12604167 positive leading-minor checks** across the three chart certificates. All 48790 rooted alternatives are covered in every chart; missing cells and missing tree alternatives are zero. Row records are counted per separately built library, not claimed mutually distinct across libraries or canonical classes. Supports have three through seven true arrows. The three builds made 1558, 1063 and 2755 locator calls respectively; their numerical outcomes are not proof acceptance.

Normal exact acceptance was observed for every chart. The initial middle invocation timed out after candidate generation; its subsequent separate exact check completed. A fresh directory initially containing only the two source files below then rebuilt all three certificates from empty libraries, ran three further optimizer-free checks, and ran the complete audit. All six certificate/report JSON files and the audit report reproduced byte-for-byte, and all cold-run stderr files were empty. The cold driver exited zero. These are observed author computations, not a proof-assistant formalization or independent peer review.

A first completed `unit` milestone, h,k in [1,2], l in [0,1], is retained by the same source: 947 rows, 71 leaves and 18734 uses. It is now subsumed by the middle chart and contributes no additional domain claim.

## 7. Actual physical controls

Three new-domain controls use the single rational metric

```
M=((3,1,0),(1,2,1),(0,1,2)), N=M^-1.
```

They are integrated at their own new centroids and tested on all 17 true edges, including both primal and both same-inverse polar primitives per edge.

| Raw projectivity (h,k,l) | Strict S facets | Strict U vertices | Strict H edges | Counts |
|---|---|---|---|---|
| `(1,2,-7/8)` | `1,4,6,7` | `0,1,7` | `01,18,57,67,79` | `(4,3,5)` |
| `(3/2,3/2,0)` | `1,4,5,6,7` | `1,6,7` | `06,18,39,49,57,67` | `(5,3,6)` |
| `(2,1,7)` | `0,1,2,4` | `1,4,7` | `06,07,18,34,49` | `(4,3,5)` |

All 204 primitives across these three controls are nonzero, and all have **zero physical weak contacts**. The audit applies the complete four-primitive closed-contact test and deduplicates contact locations; it does not equate an isolated primitive zero with a physical rest. These controls are nonattainers and not U1. No census is asserted on a path between them. The complete exact coordinates, centroids, poles, metric/inverse, edge feet and primitives regenerate from the small inputs in the source; no large coordinate array is a hidden dependency.

## 8. Recovery capsule and pins

Use CPython 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. The observed discovery stack used OpenBLAS 0.3.30, pthreads, SkylakeX, with one BLAS thread. Exact checking uses Python integers/Fractions and NumPy object arrays, and imports no optimizer. All tolerances, rounding denominators, iteration/node limits, tree orders and input data are explicit below. Numerical discovery on a different stack can produce different valid weights; exact acceptance, not matching floating output, remains mandatory.

Save the two full source blocks with their final LF. From a directory containing those files and no preexisting chart directories, run:

```sh
for chart in middle upper lower; do
  OPENBLAS_NUM_THREADS=1 python -B nonparallel_cover.py build "$chart" "$chart"
  OPENBLAS_NUM_THREADS=1 python -B nonparallel_cover.py check "$chart/certificate.json"
done
OPENBLAS_NUM_THREADS=1 python -B nonparallel_audit.py
```

Do not disable assertions. No old certificate, journal file, saved seed or parent executable is a runtime input. The full saved certificate arrays are regenerated from scratch by the first program.

Expected terminal markers, all actually observed:

```
NONPARALLEL_W_THREE_CHART_ALLROOT_V2_ALL_48790_TRUE_ROOTED_TREES_PASS middle
NONPARALLEL_W_THREE_CHART_ALLROOT_V2_ALL_48790_TRUE_ROOTED_TREES_PASS upper
NONPARALLEL_W_THREE_CHART_ALLROOT_V2_ALL_48790_TRUE_ROOTED_TREES_PASS lower
NONPARALLEL_COMPLETE_GEOMETRY_AND_ENCLOSURE_AUDIT_V2_PASS
```

| File | Bytes | SHA-256 |
|---|---:|---|
| `nonparallel_cover.py` | 14532 | `c67f69b1e5286aa9ff6aff52fd120a780d6405001c87ba58e6b185f4066796eb` |
| `nonparallel_audit.py` | 6673 | `9f9c22234dc4339284644bde6aa30b23711c684deff63eaf1b023a0e043937e9` |
| `middle/certificate.json` | 251232 | `bb8724df782fc792cc9b237ea4bd9cbe7f572defdebd7df053e8a097895d8f3f` |
| `middle/report.json` | 585 | `eed6f5dfcbee327f48d5949e200077c974973ddb84abbb6a629d0d4d7faaaf5d` |
| `upper/certificate.json` | 70772 | `a264a09014fdaf22862c17cdedee4b233c5adb1be4cddbeca4637678d0bf5fc0` |
| `upper/report.json` | 579 | `7ba6b59692a7556b5ba4d27efc567493800bcaa2c272b45d2a60ea2288e86646` |
| `lower/certificate.json` | 561443 | `63b8ba56aae91b948a81b7ef76e7083c9b14d8d37a5b37ab88af01caa4cbb1b6` |
| `lower/report.json` | 585 | `2dc6984becdba82acbfc18372dc3e5530c140ae2630f9333a8571ed8a7fc75d8` |
| `nonparallel_audit_report.json` | 82161 | `24b06b92bb867c1e269f70c4a10a4423ad31ccc03a0b5c6b7e01795af9562417` |

The supplementary cold receipt is 2481 bytes, SHA `c8148c95ae372a09f4d185d78cb9fa15e41650e6a1cdcf7e86249f9d2d7afe72`. It records observed replay, not an additional proof input. For the retained `unit` milestone, `unit/certificate.json` is 113371 bytes, SHA `646499b8304564e87f1207d106ee6e24125dbb790d5b7c94b3f6fd82da02d511`; its 579-byte report has SHA `f5b6a174efe8ba59559221166283d680f417da651acaaff527a34abdbba77aa9`. It regenerates with `python -B nonparallel_cover.py build unit unit`.

### Source 1 — nonparallel_cover.py

```python
#!/usr/bin/env python3
"""Actual nonparallel W family: complete true-tree exclusion.
CPython 3.13.5; exact acceptance uses integer fixed-point Taylor models.
Discovery uses NumPy 2.3.5 / SciPy 1.17.0, HiGHS, one BLAS thread.
No parent program, seed, or saved certificate is needed for build.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import sys,json,hashlib,time
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,product
from math import gcd
import numpy as np

NAME='NONPARALLEL_W_THREE_CHART_ALLROOT_V2'
PARENT=('minimum-0272','51da02e247f4ec433c0cb936d8cf81aba1ed7724a3987ff134b945cc30a1e26c')
Y=tuple(tuple(map(F,a)) for a in (('17/80',0,0),('629/800',0,0),('187/250','51/500',0),('51/100','17/50',0),(0,'221/800',0),(0,'17/80',0),('17/320','17/320',0),(0,0,1),('3/20',0,1),(0,'3/20',1)))
FACES=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),(9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
FAN=tuple((7,f[0],f[j],f[j+1]) for f in FACES if 7 not in f for j in range(1,len(f)-1))
EDGES=tuple(sorted({tuple(sorted(e)) for f in FACES for e in zip(f,f[1:]+f[:1])}))
ARROWS=tuple(a for e in EDGES for a in (e,e[::-1]))
PACK=((0,0),(0,1),(0,2),(1,1),(1,2),(2,2))
GAUGE=(2,4,1)
BITS=96; SCALE=1<<96; MARGIN=1<<30
EXP=((0,0,0),(1,0,0),(0,1,0),(0,0,1),(2,0,0),(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2))
INDEX={e:i for i,e in enumerate(EXP)}
MUL=tuple((i,j,INDEX.get(tuple(a+b for a,b in zip(e,f)),-1)) for i,e in enumerate(EXP) for j,f in enumerate(EXP))
CORNERS=tuple(product(range(3),repeat=3))
BERN=tuple(tuple(np.prod([((1,1,1) if e[k]==0 else (-1,0,1) if e[k]==1 else (1,-1,1))[a[k]] for k in range(3)],dtype=object) for e in EXP) for a in CORNERS)
DOMAINS={
 'middle':((F(1),F(2)),(F(1),F(2)),(F(-1,2),F(1))),
 'upper':((F(1),F(2)),(F(1),F(2)),(F(0),F(1,2))),
 'lower':((F(1),F(2)),(F(1),F(2)),(F(0),F(1,2))),
 'unit':((F(1),F(2)),(F(1),F(2)),(F(0),F(1)))
}

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def svolume(z,ids):
 a,b,c,d=(z[i] for i in ids);return det(sub(b,a),sub(c,a),sub(d,a))
W0=tuple(svolume(Y,t) for t in FAN)
assert len(FAN)==9 and len(EDGES)==17 and min(W0)>0

def ceildiv(n,d):
 assert n>=0 and d>0;return (n+d-1)//d

def nearest(n,d):
 assert d>0;return (2*n+d)//(2*d)

class TM:
 """p(t)+[-e,e], |t_i|<=1. All coefficients and e are /SCALE."""
 __slots__=('c','e')
 def __init__(self,x=0,c=None,e=0):
  if c is not None:self.c=tuple(c);self.e=e;return
  x=F(x);n=x.numerator*SCALE;d=x.denominator;q=nearest(n,d)
  self.c=(q,)+(0,)*9;self.e=int(q*d!=n)
 def __add__(self,b):
  if not isinstance(b,TM):b=TM(b)
  return TM(c=tuple(x+y for x,y in zip(self.c,b.c)),e=self.e+b.e)
 __radd__=__add__
 def __neg__(self):return TM(c=tuple(-x for x in self.c),e=self.e)
 def __sub__(self,b):return self+-b if isinstance(b,TM) else self+(-F(b))
 def __rsub__(self,b):return -self+b
 def times(self,n,d=1):
  if d<0:n,d=-n,-d
  q=tuple(nearest(x*n,d) for x in self.c)
  err=ceildiv(self.e*abs(n)+sum(abs(x*n-y*d) for x,y in zip(self.c,q)),d)
  return TM(c=q,e=err)
 def __mul__(self,b):
  if not isinstance(b,TM):
   b=F(b);return self.times(b.numerator,b.denominator)
  n=[0]*10;tail=0
  for i,j,k in MUL:
   a=self.c[i]*b.c[j]
   if k<0:tail+=abs(a)
   else:n[k]+=a
  c=tuple(nearest(x,SCALE) for x in n)
  err=tail+self.e*sum(map(abs,b.c))+b.e*sum(map(abs,self.c))+self.e*b.e
  err+=sum(abs(x-y*SCALE) for x,y in zip(n,c))
  return TM(c=c,e=ceildiv(err,SCALE))
 __rmul__=__mul__
 def reciprocal(self):
  a=self.c[0];assert a>0
  u=self.times(SCALE,a)-1;n=sum(map(abs,u.c))+u.e
  if n>=SCALE:raise ArithmeticError('Reciprocal Taylor radius')
  out=(1-u+u*u).times(SCALE,a)
  out.e+=ceildiv(n**3,a*(SCALE-n))
  return out
 def __truediv__(self,b):
  if isinstance(b,TM):return self*b.reciprocal()
  b=F(b);return self.times(b.denominator,b.numerator)
 def __rtruediv__(self,b):return self.reciprocal()*b
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  out=TM(1)
  for _ in range(n):out=out*self
  return out
 def lower(self):return self.c[0]-sum(map(abs,self.c[1:]))-self.e

def variables(box):
 out=[]
 for axis,(lo,hi) in enumerate(box):
  a=TM((lo+hi)/2);c=list(a.c);w=F(hi-lo,2)*SCALE
  v=nearest(w.numerator,w.denominator);c[axis+1]=v
  out.append(TM(c=c,e=a.e+int(v*w.denominator!=w.numerator)))
 return out

def geometry(par,chart):
 h,k,t=par;den=[];z=[]
 for i,y in enumerate(Y):
  if chart in ('middle','unit'):
   d=1+h*y[0]+k*y[1]+t*y[2];v=y
  elif i<7:
   d=1+h*y[0]+k*y[1];v=y
  elif chart=='upper':
   d=1+t*(h*y[0]+k*y[1]);v=(t*y[0],t*y[1],1)
  elif i==7:
   d=1;v=(0,0,1)
  else:
   assert chart=='lower';d=t+h*y[0]+k*y[1];v=(y[0],y[1],t)
  ri=1/d if isinstance(d,TM) else F(1)/d
  den.append(d);z.append(tuple(ri*x for x in v))
 weights=[]
 for ids,w0 in zip(FAN,W0):
  w=w0
  if chart=='upper':w=w*t**(sum(i>=7 for i in ids)-1)
  for i in ids:
   if chart=='lower' and i==7:continue
   w=w/den[i]
  weights.append(w)
 D=sum(weights);J=tuple(sum(w*sum(z[i][j] for i in ids) for w,ids in zip(weights,FAN)) for j in range(3))
 zz=[tuple(a*g for a,g in zip(v,GAUGE)) for v in z]
 jj=tuple(a*g for a,g in zip(J,GAUGE))
 R=[tuple(4*D*v[j]-jj[j] for j in range(3)) for v in zz]
 mats=[]
 for i,j in ARROWS:
  e=sub(zz[j],zz[i]);mats.append(tuple(-(R[i][a]*e[b]+R[i][b]*e[a])/2 for a,b in PACK))
 return z,D,J,mats

def cell_model(box,chart):
 z,D,J,mats=geometry(variables(box),chart)
 assert isinstance(D,TM)
 c=np.array([[a.c for a in row] for row in mats],dtype=object)
 errors=np.array([[a.e for a in row] for row in mats],dtype=object)
 arr=np.einsum('ase,be->abs',c,np.array(BERN,object),optimize=True)
 # sym matrix error >= -diag(sum of absolute entry-error bounds).
 rs=np.array([errors[:,0]+errors[:,1]+errors[:,2],errors[:,1]+errors[:,3]+errors[:,4],errors[:,2]+errors[:,4]+errors[:,5]]).T
 for k,j in enumerate((0,3,5)):arr[:,:,j]-=rs[:,k,None]+SCALE//MARGIN
 variation=[max(abs(c[a,s,k+1]) for a in range(34) for s in range(6)) for k in range(3)]
 return arr,variation,D.lower()

def as_matrices(a):
 out=np.empty(a.shape[:-1]+(3,3),dtype=a.dtype)
 for j,(r,c) in enumerate(PACK):out[...,r,c]=out[...,c,r]=a[...,j]
 return out

def is_pd_packed(v):
 a,b,c,d,e,f=v
 return a>0 and a*d-b*b>0 and a*d*f+2*b*c*e-a*e*e-d*c*c-f*b*b>0

def exact_row(arr,row,return_min=False):
 q=sum((w*arr[a] for a,w in row),np.zeros((27,6),object))
 vals=[]
 for v in q:
  a,b,c,d,e,f=map(int,v)
  mm=(a,a*d-b*b,a*d*f+2*b*c*e-a*e*e-d*c*c-f*b*b)
  if min(mm)<=0:return False
  vals.append(mm)
 if return_min:return tuple(min(m[k] for m in vals) for k in range(3))
 return True

def trees():
 ai={a:i for i,a in enumerate(ARROWS)};out=[]
 for es in combinations(EDGES,9):
  nb=[[] for _ in range(10)]
  for i,j in es:nb[i].append(j);nb[j].append(i)
  todo=[0];seen={0}
  for i in todo:
   for j in nb[i]:
    if j not in seen:seen.add(j);todo.append(j)
  if len(seen)!=10:continue
  for root in range(10):
   par={root:root};todo=[root]
   for i in todo:
    for j in nb[i]:
     if j not in par:par[j]=i;todo.append(j)
   ids=tuple(sorted(ai[i,par[i]] for i in range(10) if i!=root))
   out.append((root,ids,sum(1<<i for i in ids)))
 assert len(out)==48790 and len(set((r,m) for r,ids,m in out))==48790
 return out

def locate(arr,ids):
 from scipy.optimize import linprog
 exact=arr[list(ids)];A=as_matrices(np.array(exact,float)/SCALE)
 scale=np.max(np.abs(A),axis=(1,2,3));scale=np.maximum(scale,1e-100);A=A/scale[:,None,None,None]
 n=len(ids)
 vv=np.array(((1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,-1,0),(1,0,1),(1,0,-1),(0,1,1),(0,1,-1)),float)
 vv/=np.linalg.norm(vv,axis=1)[:,None]
 rows=np.einsum('vi,nbij,vj->bvn',vv,A,vv).reshape(-1,n)
 for iteration in range(50):
  ans=linprog(np.r_[np.zeros(n),-1.],A_ub=np.c_[-rows,np.ones(len(rows))],b_ub=np.zeros(len(rows)),A_eq=[np.r_[np.ones(n),0]],b_eq=[1.],bounds=[(0,None)]*n+[(None,None)],method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
  if not ans.success or ans.x[-1]<1e-9:return None
  w=ans.x[:-1];B=np.einsum('n,nbij->bij',w,A)
  values,axes=np.linalg.eigh(B)
  if values.min()>1e-10:
   raw=w/scale
   for den in (100,1000,10000,100000,1000000,10000000):
    wi=np.rint(raw/raw.max()*den).astype(np.int64)
    row=tuple((int(i),int(v)) for i,v in zip(ids,wi) if v>0)
    if exact_row(arr,row):
     g=0
     for i,v in row:g=gcd(g,v)
     return tuple((i,v//g) for i,v in row)
  bad=np.where(values[:,0]<max(ans.x[-1]-1e-9,1e-10))[0]
  if not len(bad):return None
  vectors=axes[bad,:,0]
  rows=np.concatenate((rows,np.einsum('bi,nbij,bj->bn',vectors,A[:,bad],vectors)))
 return None

def split_box(box,axis):
 lo,hi=box[axis];mid=(lo+hi)/2
 return (box[:axis]+((lo,mid),)+box[axis+1:],box[:axis]+((mid,hi),)+box[axis+1:])

def wire(a):return (json.dumps(a,sort_keys=True,separators=(',',':'))+'\n').encode()
def sh(b):return hashlib.sha256(b).hexdigest()

def build(chart,directory):
 import scipy
 assert np.__version__=='2.3.5' and scipy.__version__=='1.17.0'
 directory=Path(directory);directory.mkdir(exist_ok=False)
 ts=trees();masks=np.array([t[2] for t in ts],np.uint64)
 library=[];lookup={};nodes=[];calls=0;start=time.time()
 todo=[('',DOMAINS[chart],np.arange(len(ts)),0)]
 while todo:
  path,box,left,depth=todo.pop()
  if depth>21 or len(nodes)>12000:raise RuntimeError(('UNCLOSED_BUDGET',path,box,len(left)))
  try:arr,var,dlo=cell_model(box,chart)
  except ArithmeticError:
   arr=None;var=[float(b-a) for a,b in box];dlo=0
  used=[]
  if arr is not None and dlo>0:
   af=as_matrices(np.array(arr,float)/SCALE)
   for begin in range(0,len(library),512):
    if not len(left):break
    rows=library[begin:begin+512];weights=np.zeros((len(rows),34))
    for a,row in enumerate(rows):
     for i,w in row:weights[a,i]=w
    vals=np.linalg.eigvalsh(np.einsum('ra,abij->rbij',weights,af,optimize=True))
    good=np.where(vals.min(axis=(1,2))>1e-12*weights.sum(axis=1))[0]
    for a in good:
     ri=begin+int(a);row=library[ri];mask=np.uint64(sum(1<<i for i,w in row))
     hit=(masks[left]&mask)==mask
     if hit.any() and exact_row(arr,row):
      used.append(ri);left=left[~hit]
      if not len(left):break
   attempts=0
   while len(left) and attempts<750:
    row=locate(arr,ts[int(left[0])][1]);calls+=1;attempts+=1
    if row is None:break
    if row not in lookup:lookup[row]=len(library);library.append(row)
    ri=lookup[row];used.append(ri);mask=np.uint64(sum(1<<i for i,w in row));hit=(masks[left]&mask)==mask
    assert hit.any();left=left[~hit]
  node={'path':path,'rows':used}
  if not len(left):node['leaf']=True
  else:
   axis=int(np.argmax(var));b0,b1=split_box(box,axis)
   node.update(split=axis,left=len(left))
   todo.extend(((path+str(axis)+'1',b1,left.copy(),depth+1),(path+str(axis)+'0',b0,left.copy(),depth+1)))
  nodes.append(node)
  rec={'object':NAME,'parent':PARENT,'chart':chart,'domain':[[str(x) for x in a] for a in DOMAINS[chart]],'bits':BITS,'margin_denominator':MARGIN,'gauge':GAUGE,'rows':library,'nodes':nodes,'complete':not todo,'lp_calls':calls}
  (directory/'certificate.json').write_bytes(wire(rec))
  print('NODE',len(nodes),path,'DEPTH',depth,'LEFT',len(left),'ROWS',len(library),'USES',sum(len(n['rows']) for n in nodes),'OPEN',len(todo),'SEC',round(time.time()-start,2),flush=True)
  if len(nodes)%50==0:print('COVER_LEAVES',sum(n.get('leaf',False) for n in nodes),flush=True)
 print('DISCOVERY_COMPLETE',chart,flush=True)
 return rec

def check(cert):
 assert cert['object']==NAME and cert['complete']
 assert cert['parent']==list(PARENT) or cert['parent']==PARENT
 chart=cert['chart'];assert cert['domain']==[[str(x) for x in a] for a in DOMAINS[chart]]
 assert cert['bits']==BITS and cert['margin_denominator']==MARGIN and tuple(cert['gauge'])==GAUGE
 ts=trees();masks=np.array([a[2] for a in ts],np.uint64);rows=cert['rows']
 for row in rows:
  assert row and len({i for i,w in row})==len(row)
  assert all(type(i)==type(w)==int and 0<=i<34 and w>0 for i,w in row)
 nd={n['path']:n for n in cert['nodes']};assert len(nd)==len(cert['nodes'])
 todo=[('',DOMAINS[chart],np.arange(48790),0)];seen=set();volume=F(0);uses=leaves=0;stream=hashlib.sha256();dmin=None;depthmax=0
 while todo:
  path,box,left,depth=todo.pop();assert path in nd and path not in seen;seen.add(path);node=nd[path]
  if node['rows']:
   arr,var,dlo=cell_model(box,chart);assert dlo>0;dmin=dlo if dmin is None else min(dmin,dlo)
   for ri in node['rows']:
    assert type(ri)==int and 0<=ri<len(rows)
    row=rows[ri];mins=exact_row(arr,row,True);assert mins,(path,ri)
    mask=np.uint64(sum(1<<i for i,w in row));hit=(masks[left]&mask)==mask;assert hit.any()
    stream.update(wire([path,ri,mins]));left=left[~hit];uses+=1
  if node.get('leaf'):
   assert not len(left) and 'split' not in node
   leaves+=1;volume+=F(1,2**depth);depthmax=max(depthmax,depth)
  else:
   assert len(left)==node['left']>0 and node['split'] in (0,1,2)
   axis=node['split'];b0,b1=split_box(box,axis)
   todo.extend(((path+str(axis)+'1',b1,left.copy(),depth+1),(path+str(axis)+'0',b0,left.copy(),depth+1)))
 assert seen==set(nd) and volume==1
 report={'object':NAME,'chart':chart,'trees':48790,'unrooted_trees':4879,'closed_nodes':len(nd),'closed_leaves':leaves,'max_depth':depthmax,'parameter_volume_fraction':str(volume),'distinct_rows':len(rows),'weight_terms':sum(len(r) for r in rows),'uses':uses,'PD_blocks':27*uses,'positive_leading_minors':81*uses,'minimum_proved_D_lower':str(F(dmin,SCALE)),'check_stream_sha256':stream.hexdigest(),'certificate_sha256':sh(wire(cert)),'status':'EXACT_COMPLETE'}
 print(json.dumps(report,sort_keys=True),flush=True)
 return report

def main():
 if not __debug__:raise RuntimeError('Assertions must remain enabled')
 if len(sys.argv)<3:raise SystemExit('build CHART DIRECTORY | check CERTIFICATE')
 if sys.argv[1]=='build':
  rec=build(sys.argv[2],sys.argv[3]);directory=Path(sys.argv[3])
 elif sys.argv[1]=='check':
  p=Path(sys.argv[2]);rec=json.loads(p.read_bytes());directory=p.parent
 else:raise SystemExit('Unknown command')
 report=check(rec);raw=wire(report);p=directory/'report.json'
 if sys.argv[1]=='check' and p.exists():assert p.read_bytes()==raw
 else:p.write_bytes(raw)
 for p in (Path(__file__),directory/'certificate.json',directory/'report.json'):
  b=p.read_bytes();print(p.name,len(b),sh(b))
 print(NAME+'_ALL_48790_TRUE_ROOTED_TREES_PASS',rec['chart'])
if __name__=='__main__':main()
```

### Source 2 — nonparallel_audit.py

```python
#!/usr/bin/env python3
"""Independent geometry, physical census, and Taylor-enclosure spot audits.
Dependency: the complete nonparallel_cover.py from this handoff.
These finite audits supplement, not replace, the analytic enclosure proof.
Run in a directory containing middle/upper/lower certificate+report JSONs.
"""
import json,hashlib
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,product
import nonparallel_cover as C

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(t,a):return tuple(t*x for x in a)
def matvec(A,v):return tuple(C.dot(row,v) for row in A)
def inverse(A):
 d=C.det(*A);assert d
 cols=(C.cross(A[1],A[2]),C.cross(A[2],A[0]),C.cross(A[0],A[1]))
 return tuple(tuple(cols[j][i]/d for j in range(3)) for i in range(3))
def determinants(A):
 return A[0][0],A[0][0]*A[1][1]-A[0][1]**2,C.det(*A)
def hull(z):
 pts=tuple(dict.fromkeys(z));fs={}
 for a,b,c in combinations(range(len(pts)),3):
  n=C.cross(C.sub(pts[b],pts[a]),C.sub(pts[c],pts[a]))
  if not any(n):continue
  s=[C.dot(n,C.sub(p,pts[a])) for p in pts]
  if min(s)<0<max(s):continue
  fs[frozenset(i for i,t in enumerate(s) if t==0)]=n
 extreme=[i for i in range(len(pts)) if any(C.det(*t)!=0 for t in combinations([n for f,n in fs.items() if i in f],3))]
 facets={tuple(i for i in sorted(f) if i in extreme) for f in fs}
 edges={tuple(sorted(set(f)&set(g))) for f,g in combinations(facets,2) if len(set(f)&set(g))==2}
 result=(len(extreme),len(edges),len(facets));assert result[0]-result[1]+result[2]==2
 return result,tuple(sorted(facets))
def moment_audit(z,D,J):
 dd=F(0);jj=(F(0),)*3
 for face in C.FACES:
  if 0 in face:continue
  for k in range(1,len(face)-1):
   ids=(0,face[0],face[k],face[k+1]);w=C.svolume(z,ids);assert w>=0
   dd+=w;jj=add(jj,mul(w,tuple(sum(z[i][j] for i in ids) for j in range(3))))
 assert dd==D>0 and jj==J

def physical(p):
 p=tuple(map(F,p));den=tuple(1+C.dot(p,y) for y in C.Y);assert min(den)>0
 z,D,J,unused=C.geometry(p,'middle');moment_audit(z,D,J)
 g=mul(1/(4*D),J);x=tuple(C.sub(a,g) for a in z);poles=[]
 for face in C.FACES:
  a,b,c=(z[i] for i in face[:3]);n=C.cross(C.sub(b,a),C.sub(c,a));h=C.dot(n,a)
  assert all(h-C.dot(n,z[i])==0 if i in face else h-C.dot(n,z[i])>0 for i in range(10))
  hh=h-C.dot(n,g);assert hh>0;poles.append(mul(1/hh,n))
 fv,facets=hull(z);assert fv==(10,17,9) and set(facets)=={tuple(sorted(f)) for f in C.FACES}
 M=tuple(tuple(map(F,r)) for r in ((3,1,0),(1,2,1),(0,1,2)));N=inverse(M);assert min(determinants(M))>0
 assert all(sum(M[i][k]*N[k][j] for k in range(3))==int(i==j) for i in range(3) for j in range(3))
 ef={e:tuple(i for i,f in enumerate(C.FACES) if set(e)<=set(f)) for e in C.EDGES}
 dp={(i,j):C.dot(x[i],matvec(M,C.sub(x[j],x[i]))) for i,j in C.ARROWS}
 dq={(f,k):C.dot(poles[f],matvec(N,C.sub(poles[k],poles[f]))) for fs in ef.values() for f,k in (fs,fs[::-1])}
 U=[i for i in range(10) if all(v<0 for (a,b),v in dp.items() if a==i)]
 S=[i for i in range(9) if all(v<0 for (a,b),v in dq.items() if a==i)]
 H=[];weak={};packets=[]
 for (i,j),(f,k) in ef.items():
  vals=(dp[i,j],dp[j,i],dq[f,k],dq[k,f]);e=C.sub(x[j],x[i]);t=-dp[i,j]/C.dot(e,matvec(M,e));pt=add(x[i],mul(t,e))
  if max(vals)<0:H.append((i,j))
  if max(vals)<=0 and 0 in vals:
   assert 0<=t<=1;weak.setdefault(pt,[]).append((i,j))
  packets.append(((i,j),(f,k),vals,t,pt))
 assert len(S)+len(U)-len(H)==2
 assert len(dp)==len(dq)==34 and not weak and all(v!=0 for v in (*dp.values(),*dq.values()))
 return dict(p=p,vertices=z,denominators=den,D=D,J=J,centroid=g,poles=poles,M=M,N=N,S=S,U=U,H=H,weak_points=tuple(weak),zero_primitives=0,packets=packets)

def bareiss_det(A):
 A=[list(map(int,r)) for r in A];old=1;sign=1;n=len(A)
 for k in range(n-1):
  if A[k][k]==0:
   i=next(i for i in range(k+1,n) if A[i][k]);A[k],A[i]=A[i],A[k];sign=-sign
  pivot=A[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    num=A[i][j]*pivot-A[i][k]*A[k][j];assert num%old==0;A[i][j]=num//old
  for i in range(k+1,n):A[i][k]=0
  old=pivot
 return sign*A[-1][-1]

def value(poly,t):
 return sum(F(c,C.SCALE)*product_term(t,e) for c,e in zip(poly.c,C.EXP))
def product_term(t,e):
 v=F(1)
 for a,n in zip(t,e):v*=a**n
 return v

def main():
 assert __debug__
 lap=[[0]*10 for _ in range(10)]
 for i,j in C.EDGES:lap[i][i]+=1;lap[j][j]+=1;lap[i][j]-=1;lap[j][i]-=1
 count=bareiss_det([row[:9] for row in lap[:9]]);assert count==4879
 source=physical((0,0,0));assert source['D']/6==F(881291,9600000)
 assert source['centroid']==(F(7368835529,28201312000),F(3427883561,28201312000),F(50317,153268))
 controls=[physical(p) for p in ((1,2,F(-7,8)),(F(3,2),F(3,2),0),(2,1,7))]
 limits=[]
 for chart in ('upper','lower'):
  for h,k in product((F(1),F(2)),repeat=2):
   z,D,J,unused=C.geometry((h,k,F(0)),chart);moment_audit(z,D,J);fv,_=hull(z)
   assert fv==((8,14,8) if chart=='upper' else (6,10,6));assert J[2]/(4*D)==F(1,4)
   limits.append(dict(chart=chart,h=h,k=k,D=D,J=J,fvector=fv))
 stats=[];comparisons=0
 for chart in ('middle','upper','lower'):
  cert=json.loads(Path(chart+'/certificate.json').read_bytes());nodes=[n for n in cert['nodes'] if n['rows']]
  for index in sorted({0,len(nodes)//2,len(nodes)-1}):
   path=nodes[index]['path'];box=C.DOMAINS[chart]
   for j in range(0,len(path),2):box=C.split_box(box,int(path[j]))[int(path[j+1])]
   unused,dt,jt,mt=C.geometry(C.variables(box),chart)
   for t in tuple(product((F(-1),F(1)),repeat=3))+((F(0),)*3,(F(1,3),-F(1,2),F(2,3))):
    p=tuple((lo+hi)/2+(hi-lo)*r/2 for (lo,hi),r in zip(box,t))
    z,D,J,exact=C.geometry(p,chart);moment_audit(z,D,J)
    for a,b in [(D,dt)]+list(zip(J,jt))+[(a,b) for ar,br in zip(exact,mt) for a,b in zip(ar,br)]:
     assert abs(a-value(b,t))<=F(b.e,C.SCALE);comparisons+=1
   stats.append((chart,path))
 assert C.SCALE%C.MARGIN==0 and sum(C.W0)<1 and F(400,9)*sum(C.W0)<32
 report=dict(object='NONPARALLEL_COMPLETE_GEOMETRY_AND_ENCLOSURE_AUDIT_V2',source=source,controls=controls,limits=limits,Kirchhoff=count,enclosure_nodes=stats,scalar_enclosure_comparisons=comparisons,normalized_D_upper=32,status='PASS')
 def enc(x):
  if isinstance(x,F):return str(x)
  if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
  if isinstance(x,(tuple,list)):return [enc(a) for a in x]
  return x
 raw=(json.dumps(enc(report),sort_keys=True,indent=2)+'\n').encode();out=Path('nonparallel_audit_report.json');out.write_bytes(raw)
 for file in (Path(__file__),out):
  b=file.read_bytes();print(file.name,len(b),hashlib.sha256(b).hexdigest())
 print('CONTROLS',[(c['S'],c['U'],c['H']) for c in controls])
 print('NONPARALLEL_COMPLETE_GEOMETRY_AND_ENCLOSURE_AUDIT_V2_PASS')
if __name__=='__main__':main()
```

## 9. What remains and the useful continuation

There is **no unclosed cell inside h,k in [1,2], l>-1** in this result. The lower and upper axial tails are proved directly on their full closed normalized charts, rather than inferred from the existence of unspecified lower-vertex collars.

The theorem does not decide horizontal denominator parameters outside this square, arbitrary positive denominators with mixed-sign h,k, any of the remaining basal projective freedoms, or the whole incidence. It does not prove S>=2 under every metric, or construct 110. The earlier wider target with h or k below 1 is not silently included.

Ordinary actual-centroid primal stresses suffice here. The exact inverse/root-foot method remains relevant outside this domain, but this computation neither needs it nor proves it necessary. The most useful continuation is to enlarge the actual horizontal-denominator domain or release basal invariants while retaining the complete true-tree cover, invoking foot disjunction only after a genuine one-sided survivor—not a failed finite library—has been established.

Convenience copy: [complete sources, exact certificates, reports and replay receipt](sandbox:/mnt/data/nonparallel_v2/nonparallel_complete_handoff.zip). Every proof-critical reconstruction input is also inline above.
