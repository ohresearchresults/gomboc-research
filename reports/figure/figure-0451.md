# figure-0451

AI research report · 2026-09-21 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Nimble Willow 00 — a support-contact chart with 156 maximal supports and E≤310

Branch: `[internal-source-reference]`.

## Outcome and acceptance boundary

**No new own110 endpoint is certified in this handoff. BF35REC_G4 and BA69REC_G5 remain the reconstructible own121 construction frontier.** No numerical checkpoint from the present continuation is promoted to an exact successor.

The new substantive result is a finite, nonlinear **coupled support-stack construction**. It permits **156 genuine maximal supporting planes with only309 or308 true edges**, preserves its non-simple contact geometry exactly, and has an explicit uniformly filled volume/centroid formula. A specified rational-grid subfamily has a **common actual-centred coordinate denominator of at most270 bits**. These are geometry and arithmetic guarantees, not equilibrium guarantees.

I also prove an **actual-centroid, two-apex obstruction** for a precisely specified part of this chart. It does not assume a fixed escape tree and permits arbitrary root/witness changes elsewhere. The obstruction identifies a finite mass condition that a useful construction in this chart must break; it is not an exclusion of BF35, BA69, or the whole support-stack family.

Five fully specified rational controls exercise both stable/saddle and unstable/saddle cancellations at unchanged maximal incidence. Their exact masses, strict/additional-weak mechanics and complete radial bar multisets are derived below. A complete standalone generator/auditor reconstructs their maximal geometry, all physical/polar paths and cuts, and arithmetic/conditioning data.

**Execution limitation:** numerical lens, cap and profile campaigns were issued during this continuation, but their terminal tool receipts and candidate payloads were not available for reliable inspection in the retained execution context. The standalone exact unit below was also issued for execution, but I do not have an observed success receipt to report. Consequently, the new certified statements here are the mathematical derivations and explicitly defined rational controls—not a claimed hash-matched computer audit or a claimed completed numerical search. The unreviewed execution pack is supplemental evidence, not an accepted construction.

## 1. Parent identity and one source correction

Authoritative parent: `figure-0450`, runtime-declared SHA-256 `4acbb52f78b198f4db9f9fc83e18ec2b6b446d3703b82c4ab1b238b5275533f8`.

The retained reading log reaches EOF of the entire supplied1605-line journal, including the literal parent. The journal `research-journal(20260921-095550).md` is297352 bytes, SHA-256 `87e9f6a91ecaa72955bea7eebd8de3f8817e633dfc46f105075032b4182ad578`. The parent's portable32-unit exact dictionary is156800 bytes, SHA-256 `2ab044fb2306d7ffe31d58a05e5458e2b6b06c593ccfd255d828d9831be708db`. No unavailable historical producer was used as an assumed dependency for the mathematical results below.

There is a concrete discrepancy in the assignment's basin cardinality. The literal BF35REC_G4 component is

```text
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,20,21,23,24,25,27,35,38,40,41,46,47]
```

It contains **29 vertices**, not30. Its literal cut has25 edges. I retain that29-entry list rather than inventing a thirtieth vertex. BA69REC_G5's supplied34-vertex/30-edge component/cut does not have this discrepancy.

The supplied run's canonical own110 remains C622. The new class-unspecified C618/C616 charts below are not aliases of any older named C616 or C618 candidate and are not new records.

## 2. Finite coupled support-stack construction

Choose rational knots

`0=t0<t1<...<tM<t(M+1)=1`

and strictly positive rational curvatures `kappa[j,k]`. Define the Green function and concave profiles

```text
G(t,s) = min(t,s)*(1-max(t,s)),
f_j(t) = sum_k kappa[j,k]*G(t,t_k).
```

Every profile is continuous, positive in the open height interval, zero at the two endpoints, and piecewise affine. Its slope jump at knot t_k is exactly `-kappa[j,k]`. Strict positivity therefore supplies an exact contact/nondegeneracy parameter, rather than a tolerance-based plane merge.

### Triangular sections: N=3

At height t impose

```text
-x <= f0(t),
-y <= f1(t),
 x+y <= f2(t).
```

The three section vertices are

```text
(-f0,-f1,t),
(-f0,f0+f2,t),
(f1+f2,-f1,t).
```

With `w=f0+f1+f2`, the section area and transverse centroid are

```text
area = w^2/2,
cx = (-2*f0+f1+f2)/3,
cy = (f0-2*f1+f2)/3.
```

### Rectangular sections: N=4

At height t impose

```text
-f0(t) <= x <= f1(t),
-f2(t) <= y <= f3(t).
```

Its section area and centroid are

```text
area = (f0+f1)*(f2+f3),
cx = (f1-f0)/2,
cy = (f3-f2)/2.
```

These sections need not be concentric. Height asymmetry and transverse motion are genuine material changes, not density choices.

### Actual H-description and maximal geometry

On slab i, write a profile as `f_j(t)=m[j,i]*t+b[j,i]`. For the corresponding fixed planar normal n_j, the slab supplies the actual three-dimensional inequality

`n_j·(x,y)-m[j,i]*t <= b[j,i]`.

Concavity makes every segment's affine extension a global majorant of its profile. Intersecting all these inequalities therefore gives exactly the stated sections. No fictitious cap planes or free centroid are introduced. Outside the interval[0,1], the endpoint extensions are incompatible: the triangular normals sum to zero, and the rectangular normals occur in opposite pairs.

For strictly positive curvatures, every slab-side facet is maximal. There are two apices, N vertices at each interior knot, triangular first/last bands, and quadrilateral intermediate bands. The exact counts are

```text
V = N*M+2,
E = 2*N*M+N,
F = N*(M+1).
```

There are `2N` triangular facets and `N*(M-1)` quadrilateral facets. Every ring vertex is four-valent; the two apices have degree N. Triangulating a quadrilateral for integration does not create a true edge.

Two especially relevant parameter budgets are:

| Chart | V | True E | Maximal F | C=2E |
|---|---:|---:|---:|---:|
| N=3, M=51 |155|309|156|618|
| N=4, M=38 |154|308|156|616|

This is the important architectural distinction from a generic105-support budget: **156 active supports are possible inside E≤310 because four-plane concurrence is built into the geometry.** The statements do not assert that either chart contains a presently certified own121 or own110 member.

The chart permits all profile coefficients and an invertible affine map to change. No radial root, positive witness or escape tree is fixed. Allowing zero curvature extends the construction to support coalescences, but such a continuation must merge coplanar facets and remove redundant vertices before counting its true geometry. The supplied auditor intentionally uses the strict-positive chart and rejects unmerged degeneracies rather than silently treating a subdivision as the maximal complex.

## 3. Exact finite filled-mass closure

On each slab the profiles are affine. Section area is a polynomial of degree at most2, and each component of the section first moment has degree at most3. Thus Simpson integration is **exact**, not an approximation:

```text
integral_a^b p(t) dt = (b-a)*(p(a)+4*p((a+b)/2)+p(b))/6.
```

Apply this to

```text
(area, area*cx, area*cy, area*t).
```

Summing slabs gives exact uniform volume V and exact first moment M; the actual centroid is `c=M/V`.

For a rational invertible map `p -> A*p+b`, with positive determinant,

```text
V_new = det(A)*V,
c_new = A*c+b.
```

Consequently `A*(p-c)` is the actual own-centred uniformly filled body. This is not independent recentering of a polar and not first-order moment neutrality.

If a raw support is `n·p<=h`, the same body's own-centred support is `n·x<=h-n·c`, with strictly positive right-hand side. Under A, use `A^(-T)*n`. The recovery program also obtains every maximal support directly from the exact physical facet cycles and emits primitive integer own-centred H rows.

### Arithmetic guarantee for a specified grid family

Use uniform knots `t_k=k/(M+1)`. Put every curvature and every entry of an upper-triangular A on grid10^-6, subject to

```text
0 < kappa <= 149,
0 < A00,A11 <= 8,
0 < A22 <= 55,
|A01|,|A02|,|A12| <= 4.
```

Take either of the E≤310 charts above or a smaller M. The untranslated physical vertices lie on the common grid

`G = 10^12*(M+1)^2 < 2^52`.

Since `G(t,s)<=1/4`, every profile value is below1900. Every triangular transverse coordinate has absolute value below3800, and the rectangular bounds are smaller. After A, all coordinates have absolute value below50000. Thus the integer vertices I=G*p satisfy `|I_coordinate|<50000*G`.

There are `T=2*N*M<=306` boundary integration triangles. Let

`D6=sum det(Ia,Ib,Ic)>0`.

Each determinant has absolute value at most six times the coordinate bound cubed. The common denominator of the actual-centred physical coordinates divides `4*G*D6`, hence is bounded by

```text
4*G*D6 <= 24*G*T*(50000*G)^3 < 2^270.
```

Therefore the common own-centred coordinate denominator has **at most270 bits throughout this specified grid chart**. An arbitrary translation cancels on own-centering and does not change this bound.

This guarantee is about physical coordinates and actual mass. It is not a bound on a common polar denominator, not a conditioning guarantee, and not a guarantee that rounding preserves an equilibrium class. Round curvatures and affine coefficients jointly; independently rounding the physical vertices would generally destroy the exact four-plane contacts and quadrilateral facets.

## 4. Exact two-apex obstruction: a finite mass condition that must be broken

Consider any full-dimensional support stack whose two apices are endpoints of a line perpendicular to its section planes. If its **actual uniformly filled centroid lies on that apex line**, both apices are strict unstable equilibria.

Proof: use coordinates with bottom apex0, top apex e3, section heights strictly between0 and1, and actual centroid `c=gamma*e3`, where `0<gamma<1`. For any other vertex v,

```text
(0-c)·(v-0) = -gamma*v_z < 0,
(e3-c)·(v-e3) = (1-gamma)*(v_z-1) < 0.
```

The same inequalities hold against the other apex. Both radial vectors therefore lie strictly inside their respective normal cones. Additional roots or witness exchanges elsewhere cannot remove these two strict unstable vertices.

In affine coordinates the sufficient orthogonality condition is that `G=A^T*A` have `G13=G23=0`, together with the actual raw centroid's transverse coordinates being zero.

This obstruction covers asymmetric height profiles and does **not** require central symmetry. The mass condition is explicit. For triangular sections, transverse centroid zero is equivalent to

```text
integral w^2*f0 = integral w^3/3,
integral w^2*f1 = integral w^3/3.
```

For rectangular sections it is equivalent to

```text
integral (f1-f0)*(f0+f1)*(f2+f3) = 0,
integral (f3-f2)*(f0+f1)*(f2+f3) = 0.
```

All integrals are exact cubic slab integrals. Thus this is a finite actual-mass exclusion, not a linearized projection condition.

**Scope:** the balanced-axis/orthogonal-section subfamily has U≥2 for every M and cannot contain own110. The entire support-stack family is not excluded: genuine transverse mass displacement or an oblique metric can break the hypothesis. BF35REC_G4 and BA69REC_G5 are not asserted to belong to this excluded subfamily. This theorem is also not an explanation of the unreviewed numerical campaign outcomes.

A constructive continuation in this chart must avoid accidentally enforcing both exact transverse moment balance and orthogonal slicing. That would build the extra unstable root into the architecture before any optimizer starts.

## 5. Five exact rational bifurcation controls

Define, for rational h>1,

`K_h = conv({(±1,±1,±1)} union {(0,0,±h)})`.

Use these labels:

```text
0=(0,0,-h)
1=(-1,-1,-1), 2=(1,-1,-1), 3=(1,1,-1), 4=(-1,1,-1)
5=(-1,-1,1),  6=(1,-1,1),  7=(1,1,1),  8=(-1,1,1)
9=(0,0,h)
```

Its maximal facet cycles are

```text
[0,2,1], [0,3,2], [0,4,3], [0,1,4],
[1,2,6,5], [2,3,7,6], [3,4,8,7], [4,1,5,8],
[9,5,6], [9,6,7], [9,7,8], [9,8,5].
```

For every h>1, this is V10/E20/F12/C40, with eight triangular and four quadrilateral maximal facets. Its actual centroid is exactly0 by central symmetry, and its uniformly filled volume is

`8*(h+2)/3`.

It is a literal member of the rectangular stack chart with

```text
N=4,
knots=[(h-1)/(2*h),(h+1)/(2*h)],
kappa[j,1]=kappa[j,2]=2*h/(h-1), for j=0,1,2,3,
A=diag(1,1,2*h), translation=(0,0,-h).
```

### Full strict/additional-weak census

| h | Volume | Strict(S,U,H) | Additional weak(S,U,H) | Primitive zeros(S,U,H) |
|---|---:|---:|---:|---:|
|3/2|28/3|(12,10,20)|(0,0,0)|(0,0,0)|
|2|32/3|(4,10,12)|(8,0,8)|(8,0,8)|
|5/2|12|(4,10,12)|(0,0,0)|(0,0,0)|
|3|40/3|(4,2,4)|(0,8,8)|(0,8,8)|
|4|16|(4,2,4)|(0,0,0)|(0,0,0)|

The four lateral quadrilaterals are always strictly stable. A triangular facet's perpendicular foot lies in its relative interior exactly when `1<h<2`; at h=2 it reaches its horizontal boundary edge. At a ring vertex, the outgoing dot product toward its apex is `h-3`, while the other three outgoing products are−2. Thus the ring vertices are strictU below3, weakU at3, and escape above3. The two apices remain strictU throughout.

The four vertical edges are always strict saddles. The eight horizontal ring edges are strict saddles below2, weak at2, and absent above2. The eight apex edges are strict saddles below3, weak at3, and absent above3.

Hence this finite, actual-centroid family removes eight stable/saddle pairs at h=2 and eight unstable/saddle pairs at h=3 **without changing the maximal hull incidence**. It still cannot achieve own110: at least four strictS and two strictU persist. This is a scoped control-family exclusion, not a global polyhedral obstruction.

### Complete positive radial bar multisets

Each pair below is `(squared birth radius, squared death radius)`; multiplicities are exact.

```text
h=3/2:
 P = 7*(3,2) + 2*(9/4,2)
 Q = 3*(1,1/2) + 8*(5/9,1/2)

h=2:
 P = 8*(3,8/3) + 1*(4,2)
 Q = 3*(1,1/2)

h=5/2:
 P = 8*(3,50/17) + 1*(25/4,2)
 Q = 3*(1,1/2)

h=3:
 P = 1*(9,2)
 Q = 3*(1,1/2)

h=4:
 P = 1*(16,2)
 Q = 3*(1,1/2)
```

The horizontal and vertical physical edges have chord-min squared radius2. For an apex edge below h=3, its chord minimum is

`2*h^2/((h-1)^2+2)`;

at and above3, it is the ring endpoint value3. The triangular polar vertices have radius squared `((h-1)^2+1)/h^2`, while the four lateral polar vertices have radius squared1. These exact edge levels give the listed complete bar multisets.

At h=3/2, **all twenty physical edges have the same chord-min level2, but additionalweak and primitivezero counts are000**. Equal filtration levels are not mechanical degeneracies. At h=2 and3, genuine weak equilibria instead produce zero-length attachments; the verifier does not turn them into positive bars or silently treat them as strict roots.

For h=5/2 and4, the large Pbar's strict-upper component is `[5,6,7,8,9]`; its complete cut is `[[5,1],[6,2],[7,3],[8,4]]`. An attaining path is `[9,5,1,0]`. At h=5/2, each of the eight small Pbars has a singleton component at a ring vertex and its full four-edge incident cut.

With the facet indexing above, the four strict-upper Q components at level1/2 are

`C_j=[j,4+j,8+j]`, for j=0,1,2,3.

Each has six boundary edges: the two neighbours at its lower-triangle, middle-quadrilateral and upper-triangle levels, using cyclic j±1. Three positive bars merge these four components. The complete program emits the deterministic elder choices, every attaining path, and every full cut for all five controls.

### Arithmetic and conditioning examples

At h=5/2: centroid0, volume12, common centred denominator2 (two bits), circumradius5/2, inradius1, minimum true edge2. Thus

```text
r/R=2/5,
minedge/R=4/5,
Vol/R^3=96/125,
sum(P depths)=321/68,
sum(Q depths)=3/2.
```

With the parent's normalization, `TP=(321/68)/12^(2/3)` and `TQ=(3/2)*12^(2/3)`. All ten physical vertices are strict roots; its physical forest therefore has no positive arrows. The polar forest has eight positive arrows, depth1, and minimum squared positive cosine1/26.

At h=4: centroid0, volume16, common centred denominator1, `r/R=1/4`, `minedge/R=1/2`, `Vol/R^3=1/4`. P has exactly the two apex roots and eight positive arrows of depth1, with minimum squared positive cosine1/33. Q has four roots and eight arrows of depth1, with minimum squared positive cosine1/5.

These are diagnostic nonwinners, not arithmetic simplifications of BF35 or BA69.

## 6. Numerical work: launch coverage, not a completed-search claim

The principal requested campaigns were:

```text
lens.py --scouts 1200 --refine 12 --steps 220 --out LENS1
caps.py --caps 4 --scouts 1800 --refine 12 --steps 220 --out CAPS4
caps.py --input BA69REC_G5_ACTIVE.json --caps 6 --scouts 1500 --refine 10 --steps 220 --seed 2026092102 --out CAPS6BA
stack.py --sides 3 --layers 25 --runs 12 --steps 800 --out STACK3
stack.py --sides 4 --layers 25 --runs 12 --steps 800 --seed 2026092111 --out STACK4
```

The lens combined the actual BF35 body with a transformed H38 support block. The cap experiments used real physical truncations and recomputed uniform mass. The profile experiments varied all positive curvatures and a determinant-one affine chart. Two subsequent section-fit launches were also attempted.

**These numbers are requests, not completed trial/iteration counts.** I do not report a numerical minimum, a terminal equilibrium class, a successful freeze, or an exclusion from those campaigns. Their source/inputs/logs/checkpoints are in the supplemental unreviewed pack. Those checkpoints remain unreviewed and are not durable exact successors in this result.

The new exact geometry, mass formula, arithmetic bound, apex obstruction and rational controls do not depend on any of those numerical outputs.

## 7. Complete standalone recovery and audit source

Save the following as `NWD_PROFILE_EXACT.py` and run

```text
python -B -S NWD_PROFILE_EXACT.py NWD_PROFILE_OUT
```

The unit uses only the CPython3.13.5 standard library. It reconstructs all five literal controls, checks maximal facets independently by exhaustive supporting triples, computes mass by boundary tetrahedra and positive interior-anchor tetrahedra, compares it with exact section integration, checks full strict/additional-weak/mixed-edge mechanics, and reconstructs every positive P/Qbar/path/component/cut without numerical thresholds.

Expected terminal marker:

`NWD_PROFILE_EXACT_MASS_AND_FIVE_BIFURCATION_CONTROLS_PASS 5`

It writes `PROFILE_RESULTS.json` and `MANIFEST.json`, the latter containing output/source byte counts and SHA-256 values. **No particular hash receipt is claimed as observed in this handoff.** The literal inputs and complete source—not an unseen output hash—define the controls and their reproducibility.

For a new rational chart input, use `--profile INPUT.json`; supply `sides`, `knots`, `kappa`, and optionally `A` and `shift`. Rational numbers must be integers or fraction strings. Independent exhaustive hull checking can additionally be requested with `--exhaustive`. Such a new input still requires its own complete class audit; the five control classes must not be transferred to it.

```python
"""Exact concave support stacks, actual mass, maximal geometry and radial basins.
CPython 3.13.5 standard library. Default: five analytically specified controls.
python -B -S NWD_PROFILE_EXACT.py OUT
Optional rational profile: --profile INPUT.json (no floating JSON numbers).
"""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter, deque
from math import lcm, isqrt, gcd
from pathlib import Path
import argparse, hashlib, json, sys
sys.set_int_max_str_digits(0)
SCALE=10**12

def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def mul(a,t): return tuple(x*t for x in a)
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def enc(x):
 if isinstance(x,F): return str(x)
 if isinstance(x,dict): return {str(k):enc(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)): return [enc(v) for v in x]
 return x

def primitive(row):
 d=lcm(*(v.denominator for v in row));rr=[int(v*d) for v in row];g=gcd(*rr);assert g>0
 return [v//g for v in rr]

def sqrt_interval(x):
 assert x>=0
 n=isqrt(x.numerator*SCALE*SCALE//x.denominator)
 assert F(n*n,SCALE*SCALE)<=x<F((n+1)**2,SCALE*SCALE)
 return [n,n+1]

def profile(N,knots,kappa,A=None,shift=None):
 assert N in (3,4)
 ts=[F(0)]+list(map(F,knots))+[F(1)];M=len(knots)
 assert M>=1 and all(a<b for a,b in zip(ts,ts[1:]))
 K=[list(map(F,row)) for row in kappa]
 assert len(K)==N and all(len(row)==M and min(row)>0 for row in K)
 A=[tuple(map(F,row)) for row in (A or [[1,0,0],[0,1,0],[0,0,1]])]
 shift=tuple(map(F,shift or [0,0,0]));dA=det(*A);assert dA>0
 def values(t): return [sum((v*min(t,s)*(1-max(t,s)) for v,s in zip(row,ts[1:-1])),F(0)) for row in K]
 def section(t):
  f=values(t)
  if N==3:
   w=sum(f);ar=w*w/2;cx=(-2*f[0]+f[1]+f[2])/3;cy=(f[0]-2*f[1]+f[2])/3
  else:
   ar=(f[0]+f[1])*(f[2]+f[3]);cx=(f[1]-f[0])/2;cy=(f[3]-f[2])/2
  return (ar,ar*cx,ar*cy,ar*t)
 V=F(0);mom=[F(0)]*3
 for a,b in zip(ts,ts[1:]):
  aa,mm,bb=section(a),section((a+b)/2),section(b)
  integ=[(b-a)*(x+4*y+z)/6 for x,y,z in zip(aa,mm,bb)]
  V+=integ[0]
  for j in range(3):mom[j]+=integ[j+1]
 assert V>0
 raw=[(F(0),F(0),F(0))]
 for t in ts[1:-1]:
  f=values(t)
  if N==3:xy=[(-f[0],-f[1]),(-f[0],f[0]+f[2]),(f[1]+f[2],-f[1])]
  else:xy=[(-f[0],-f[2]),(f[1],-f[2]),(f[1],f[3]),(-f[0],f[3])]
  raw.extend((x,y,t) for x,y in xy)
 raw.append((F(0),F(0),F(1)));top=len(raw)-1
 ring=lambda i,j:1+i*N+(j%N)
 faces=[[0,ring(0,j+1),ring(0,j)] for j in range(N)]
 for i in range(M-1):faces.extend([ring(i,j),ring(i,j+1),ring(i+1,j+1),ring(i+1,j)] for j in range(N))
 faces.extend([top,ring(M-1,j),ring(M-1,j+1)] for j in range(N))
 P=[add(tuple(dot(row,p) for row in A),shift) for p in raw]
 c0=tuple(m/V for m in mom);c=add(tuple(dot(row,c0) for row in A),shift)
 return P,faces,dict(volume=V*dA,centroid=c,raw_volume=V,raw_first_moment=mom,raw_centroid=c0,N=N,M=M,knots=knots,kappa=K,A=A,shift=shift,expected_VEF=[N*M+2,2*N*M+N,N*(M+1)])

def landscape(P,E):
 R=[dot(p,p) for p in P];adj=[[] for p in P];events=[]
 for i,j in sorted(E):
  e=sub(P[j],P[i]);ll=dot(e,e);assert ll>0
  t=max(F(0),min(F(1),-dot(P[i],e)/ll));w=dot(add(P[i],mul(e,t)),add(P[i],mul(e,t)))
  assert w<=min(R[i],R[j]);events.append((w,i,j));adj[i].append((j,w));adj[j].append((i,w))
 uf=list(range(len(P)))
 def find(i):
  while uf[i]!=i:uf[i]=uf[uf[i]];i=uf[i]
  return i
 bars=[]
 for death,i,j in sorted(events,reverse=True):
  a,b=find(i),find(j)
  if a==b:continue
  if (R[a],-a)<(R[b],-b):a,b=b,a
  assert R[b]>=death
  if R[b]>death:
   component={b};todo=[b]
   while todo:
    u=todo.pop()
    for v,w in adj[u]:
     if w>death and v not in component:component.add(v);todo.append(v)
   assert a not in component
   cut=sorted((u,v) for u in component for v,w in adj[u] if v not in component)
   assert cut and all(w<=death for u in component for v,w in adj[u] if v not in component)
   pred={b:None};todo=deque([b])
   while todo and a not in pred:
    u=todo.popleft()
    for v,w in sorted(adj[u]):
     if w>=death and v not in pred:pred[v]=u;todo.append(v)
   assert a in pred;path=[a]
   while path[-1]!=b:path.append(pred[path[-1]])
   path.reverse()
   assert min(next(w for v,w in adj[u] if v==v1) for u,v1 in zip(path,path[1:]))==death
   bars.append(dict(peak=b,elder=a,death_edge=[i,j],birth=R[b],death=death,depth=R[b]-death,component=sorted(component),boundary=cut,path=path))
  uf[b]=a
 strict=[];weak=[];arrows=[];scores=[]
 for i,p in enumerate(P):
  options=[];vv=[]
  for j,w in adj[i]:
   e=sub(P[j],p);g=dot(p,e);vv.append(g)
   if g>0:options.append((g*g/(R[i]*dot(e,e)),j))
  if max(vv)<0:strict.append(i)
  elif max(vv)<=0:weak.append(i)
  else:
   score,j=max(options);arrows.append((i,j));scores.append(score)
 roots=set(strict+weak);parents=dict(arrows);depth=0
 for i in range(len(P)):
  n=0
  while i not in roots:i=parents[i];n+=1;assert n<=len(P)
  depth=max(depth,n)
 return dict(strict_roots=strict,additional_weak_roots=weak,bars=bars,sum_depth=sum((b['depth'] for b in bars),F(0)),radius2=max(R),forest=dict(exempt_roots=sorted(roots),arrows=arrows,depth=depth,min_positive_cosine_bracket_1e12=sqrt_interval(min(scores)) if scores else None))

def audit(P,cycles,exhaustive=False):
 P=[tuple(map(F,p)) for p in P];assert len(set(P))==len(P)
 anchor=tuple(sum(p[k] for p in P)/len(P) for k in range(3));faces=[];owners={};tri=[]
 for fid,cy0 in enumerate(cycles):
  cy=list(cy0);assert len(cy)>=3 and len(set(cy))==len(cy)
  n=cross(sub(P[cy[1]],P[cy[0]]),sub(P[cy[2]],P[cy[0]]));assert dot(n,n)>0
  h=dot(n,P[cy[0]])
  if dot(n,anchor)>h:cy.reverse();n=mul(n,-1);h=-h
  assert dot(n,anchor)<h and all(dot(n,P[i])==h for i in cy)
  assert all(dot(n,p)<h for i,p in enumerate(P) if i not in cy)
  for i,j in zip(cy,cy[1:]+cy[:1]):
   assert all(dot(cross(sub(P[j],P[i]),sub(P[k],P[i])),n)>0 for k in cy if k not in (i,j))
   owners.setdefault(tuple(sorted((i,j))),[]).append((fid,i,j))
  faces.append(dict(n=n,h=h,cycle=cy));tri.extend((cy[0],cy[k],cy[k+1]) for k in range(1,len(cy)-1))
 assert set(sum([f['cycle'] for f in faces],[]))==set(range(len(P)))
 assert all(len(o)==2 and o[0][1:]==o[1][1:][::-1] for o in owners.values())
 E=sorted(owners);assert len(P)-len(E)+len(faces)==2
 adj={i:set() for i in range(len(P))}
 for i,j in E:adj[i].add(j);adj[j].add(i)
 def connected(ad):
  seen={next(iter(ad))};todo=list(seen)
  while todo:
   for j in ad[todo.pop()]-seen:seen.add(j);todo.append(j)
  return len(seen)==len(ad)
 assert connected(adj)
 for i in adj:
  link={j:set() for j in adj[i]}
  for f in faces:
   cy=f['cycle']
   if i in cy:
    k=cy.index(i);a,b=cy[k-1],cy[(k+1)%len(cy)];link[a].add(b);link[b].add(a)
  assert all(len(v)==2 for v in link.values()) and connected(link)
 if exhaustive:
  found=set()
  for i,j,k in combinations(range(len(P)),3):
   n=cross(sub(P[j],P[i]),sub(P[k],P[i]))
   if dot(n,n)==0:continue
   h=dot(n,P[i]);s=[dot(n,p)-h for p in P]
   if min(s)>=0 or max(s)<=0:found.add(tuple(t for t,v in enumerate(s) if v==0))
  assert found=={tuple(sorted(f['cycle'])) for f in faces}
 D=sum((det(P[i],P[j],P[k]) for i,j,k in tri),F(0));assert D>0
 W=tuple(sum((det(P[i],P[j],P[k])*(P[i][t]+P[j][t]+P[k][t]) for i,j,k in tri),F(0)) for t in range(3));V=D/6;c=mul(W,1/(4*D));M=mul(c,V)
 V2=F(0);M2=[F(0)]*3
 for i,j,k in tri:
  a,b,d=P[i],P[j],P[k];v=det(sub(a,anchor),sub(b,anchor),sub(d,anchor))/6;assert v>0;V2+=v
  for t in range(3):M2[t]+=v*(anchor[t]+a[t]+b[t]+d[t])/4
 assert V2==V and tuple(M2)==M
 X=[sub(p,c) for p in P];normals=[f['n'] for f in faces];heights=[f['h']-dot(f['n'],c) for f in faces];assert min(heights)>0
 strict=[[],[],[]];weak=[[],[],[]];zeros=[0,0,0]
 def classify(vals,kind,label):
  zeros[kind]+=sum(v==0 for v in vals)
  if min(vals)>0:strict[kind].append(label)
  elif min(vals)>=0:weak[kind].append(label)
 for i,(n,h) in enumerate(zip(normals,heights)):
  classify([hh*dot(n,n)-h*dot(n,nn) for j,(nn,hh) in enumerate(zip(normals,heights)) if i!=j],0,i)
 for i,p in enumerate(X):classify([-dot(p,sub(X[j],p)) for j in sorted(adj[i])],1,i)
 for i,j in E:
  f,g=[a[0] for a in owners[(i,j)]];n,m=normals[f],normals[g];a,b=X[i],X[j];e=sub(b,a);ll=dot(e,e);t=-dot(a,e);w=add(mul(a,ll),mul(e,t));nn,mm,nm=dot(n,n),dot(m,m),dot(n,m);assert nn*mm>nm*nm
  classify([t,ll-t,dot(w,n)*mm-dot(w,m)*nm,dot(w,m)*nn-dot(w,n)*nm],2,[i,j])
 if not any(weak):assert len(strict[0])+len(strict[1])-len(strict[2])==2
 Q=[mul(n,1/h) for n,h in zip(normals,heights)];QE=[tuple(a[0] for a in own) for own in owners.values()];LP=landscape(X,E);LQ=landscape(Q,QE)
 assert LP['strict_roots']==strict[1] and LP['additional_weak_roots']==weak[1]
 assert LQ['strict_roots']==strict[0] and LQ['additional_weak_roots']==weak[0]
 R2=max(dot(x,x) for x in X);r2=1/max(dot(q,q) for q in Q);e2=min(dot(sub(X[i],X[j]),sub(X[i],X[j])) for i,j in E)
 return dict(V=len(P),E=len(E),F=len(faces),C=2*len(E),strict=list(map(len,strict)),weak=list(map(len,weak)),primitive_zeros=zeros,S=strict[0],U=strict[1],H=strict[2],weak_S=weak[0],weak_U=weak[1],weak_H=weak[2],points=P,faces=faces,edges=E,own_H=[primitive(tuple(n)+(h,)) for n,h in zip(normals,heights)],volume=V,first_moment=M,centroid=c,positive_anchor_tetrahedra=len(tri),independent_exhaustive_facet_check=exhaustive,face_histogram=dict(Counter(len(f['cycle']) for f in faces)),vertex_degree_histogram=dict(Counter(len(v) for v in adj.values())),common_centered_denominator_bits=lcm(*(x.denominator for p in X for x in p)).bit_length(),P=LP,Q=LQ,TP_cube=LP['sum_depth']**3/V**2,TQ_cube=LQ['sum_depth']**3*V**2,edge_R_bracket_1e12=sqrt_interval(e2/R2),r_R_bracket_1e12=sqrt_interval(r2/R2),V_R3_bracket_1e12=sqrt_interval(V*V/R2**3))

def control(h):
 h=F(h);assert h>1;knots=[(h-1)/(2*h),(h+1)/(2*h)];kap=[[2*h/(h-1)]*2 for j in range(4)]
 P,faces,section=profile(4,knots,kap,[[1,0,0],[0,1,0],[0,0,2*h]],[0,0,-h]);a=audit(P,faces,True)
 assert a['volume']==section['volume']==8*(h+2)/3 and a['centroid']==section['centroid']==(0,0,0)
 expected={F(3,2):([12,10,20],[0,0,0],[0,0,0]),F(2):([4,10,12],[8,0,8],[8,0,8]),F(5,2):([4,10,12],[0,0,0],[0,0,0]),F(3):([4,2,4],[0,8,8],[0,8,8]),F(4):([4,2,4],[0,0,0],[0,0,0])}
 assert [a[k] for k in ['V','E','F']]==[10,20,12]
 assert (a['strict'],a['weak'],a['primitive_zeros'])==expected[h]
 if h==F(3,2):pbar=[(F(3),F(2))]*7+[(h*h,F(2))]*2;qbar=[(F(5,9),F(1,2))]*8+[(F(1),F(1,2))]*3
 else:
  pbar=([(F(3),2*h*h/((h-1)**2+2))]*8 if h<3 else [])+[(h*h,F(2))];qbar=[(F(1),F(1,2))]*3
 for key,expect in [('P',pbar),('Q',qbar)]:assert sorted((b['birth'],b['death']) for b in a[key]['bars'])==sorted(expect)
 a['section_mass']=section
 if h==F(5,2):assert a['P']['sum_depth']==F(321,68) and a['Q']['sum_depth']==F(3,2)
 if h==4:assert a['P']['sum_depth']==14 and a['Q']['sum_depth']==F(3,2)
 return a

def main():
 ap=argparse.ArgumentParser();ap.add_argument('out',nargs='?',default='NWD_PROFILE_OUT');ap.add_argument('--profile');ap.add_argument('--exhaustive',action='store_true');o=ap.parse_args();out=Path(o.out);out.mkdir(parents=True,exist_ok=True)
 result={str(h):control(h) for h in [F(3,2),F(2),F(5,2),F(3),F(4)]}
 if o.profile:
  d=json.loads(Path(o.profile).read_text(),parse_float=lambda x:(_ for _ in ()).throw(ValueError('Use rational strings, not JSON floats')))
  P,faces,sec=profile(d['sides'],d['knots'],d['kappa'],d.get('A'),d.get('shift'));a=audit(P,faces,o.exhaustive)
  assert a['volume']==sec['volume'] and a['centroid']==sec['centroid'];assert [a[k] for k in ['V','E','F']]==sec['expected_VEF'];a['section_mass']=sec;result['candidate']=a
 b=(json.dumps(enc(result),sort_keys=True,separators=(',',':'))+'\n').encode();(out/'PROFILE_RESULTS.json').write_bytes(b)
 source=Path(__file__).read_bytes();manifest={'PROFILE_RESULTS.json':[len(b),hashlib.sha256(b).hexdigest()],'source':[len(source),hashlib.sha256(source).hexdigest()]};(out/'MANIFEST.json').write_text(json.dumps(manifest,sort_keys=True,indent=2)+'\n')
 print('NWD_PROFILE_EXACT_MASS_AND_FIVE_BIFURCATION_CONTROLS_PASS',len(result),json.dumps(manifest,sort_keys=True),flush=True)
if __name__=='__main__':main()
```

## 8. Continuation-critical conclusion

The useful new construction resource is **not another reference escape chain**. It is an exact nonlinear contact chart that raises the available active-support count from the generic105-support sufficient ceiling to156 while retaining E≤310, and makes the actual uniform mass a small-degree rational calculation.

Its balanced-axis subfamily is rigorously the wrong place to seek uniqueU: both apices remain strictly unstable regardless of changes elsewhere. A meaningful continuation must allow finite transverse mass displacement or oblique slicing, then audit both complete actual-centroid landscapes. The arithmetic bound alone supplies neither conditioning nor equilibrium reserve.

BF35's literal29/25 physical basin and BA69's34/30 basin remain the actual parent targets. No new obstruction to their full nonlinear continuation has been proved here. No unknown numerical output is used to claim that the present finite searches failed mathematically.

Supplementary files: standalone exact profile/control source (`NWD_PROFILE_EXACT.py`), unreviewed numerical sources, inputs, logs and receipts (`NWD_UNREVIEWED_EXPERIMENTS.zip`), and unreviewed tool-receipt collection (`NWD_TOOL_RECEIPTS_UNREVIEWED.json`). The mathematical construction and complete inline source above do not depend on these links.
