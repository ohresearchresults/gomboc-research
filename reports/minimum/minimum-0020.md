# minimum-0020

AI research report · 2026-09-08 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# HEX17_ACTUAL_CAP_RELAXATION_BARRIER_V1

## Determination

**No whole joint-root orbit or combinatorial type is excluded, and no C30 strict110 attainer is claimed.** I obtained two exact relaxation barriers instead. They identify a concrete limitation of the proposed shape-only continuation and a stronger limitation that persists with actual centering, actual disjoint cap moments, and one physical reciprocal metric.

First, **every one of the 17 hexagonal types has a strict actual-shape witness satisfying every atlas volume-only cap inequality simultaneously**. This remains true when all 347 admissible deletion subsets are imposed unconditionally, and when each adaptive coefficient is replaced by its strongest possible value, one. Consequently the present volume-only cap inequalities plus complete convex base/roof geometry cannot exclude even one of the 41,454 hexagonal records.

Second, the representative old record `(31,1,0,6826)` has an exact, uniformly volume-centered, physically reciprocal C30 control satisfying all 23 admissible uniform cap systems, all five attached adaptive signed-moment systems, both prescribed global norm maxima, and the single-child square-identity ingredients. A directed-rounding certificate preserves these properties throughout a **14-dimensional parameter cube of radius `2^-40`**. Its actual equilibrium class is **`(6,6,10)`**, not110. The missing information is the complete escape-arrow geometry; neither centering nor cap-weight compatibility is missing from this control.

## Authority and work performed

The immutable catalogue parent remains `minimum-0009`, SHA-256 `6f905a98d5d84d11e1369aebb34643ad59248a2485b95270c59bb52c48b92326`. Its literal remainder is 178,131 records, 890,655 bytes in `raven_remaining.bin`, SHA-256 `5d3329d312adf3db48d9e22314d6cec046f4ec9b00b29fe248fa96f699bb3f1f`; it is not silently relabeled as the later filtered remainder.

I recovered and executed the complete `HEX17_ACTUAL_CAP_ATLAS_V1` source, 32,064 bytes, SHA-256 `f37ea08f97d022629d02ca7d5356dfed5c2058658691bf45eeca9ca925691cf1`, and reproduced its catalogue attachment and representative branch hashes. The atlas itself explicitly supplies formulas, not exclusions, and proposes trying the shape-only adaptive inequalities next. The first theorem below rules out exclusion by that particular relaxation, rather than merely generating another formula.

The later TREE24 correction leaves the global frontier at **178,103 records / 4,366 joint-root orbits / 74 types**, with the same **41,454 hexagonal records**. Nothing is subtracted here. The bracket remains `30 <= C_min <= 1374`. The captured atlas's earlier 178,115 count is chronological, not a conflicting immutable-parent identity.

I tried common-separator and full-shape numerical locators before switching to a precisely certifiable barrier. Their solver statuses are not exclusion evidence. Numerical optimization was used only to locate the second control; all promoted results below are reconstructed by the complete standard-library rational/interval checker. It requires neither numerical packages nor the optimization trajectory.

## 1. A universal barrier to the current volume-only route

For an admissible deletion `S`, let `D_S=6 Vol(P minus K_S)`, `D0=6 Vol(K_S)`, and `x_S=D_S/D0`, where `K_S` is the actual retained convex hull. Components within one deletion are the atlas's **actual disjoint block caps**, not overlapping original vertex ears. Their disjointness and exact material interpretation are inherited from the atlas theorem; the new checker independently rebuilds every retained hull and every component hull and verifies both volume and all three first-moment additions.

Use the 17 exact atlas control shapes, whose complete literal vertices and maximal facets are embedded below. Across all 347 admissible deletions, the exact minima are:

| Number deleted | Minimum `x_S` | One attaining `(type code, mask)` |
|---:|---:|---:|
|1|`7/52`|`(38054,16)`|
|2|`15/44`|`(38054,18)`|
|3|`52/75`|`(37542,42)`|
|4|`106/21`|`(37542,58)`|

These are minima over the displayed finite controls, **not lower bounds over all realizations**.

For every adaptive retained decomposition, put `t_S=T_S/D0`. Positive actual tetrahedral volumes and the atlas's coefficients give `0<t_S<=1`. Its two possible volume tests are `4x_S>t_S` and `16x_S^2+12x_S>t_S`; its uniform tests are weaker.

At all of the controls, every deletion of at least two vertices obeys

```text
x_S >= 15/44,
4x_S - 1 >= 4/11 > 0,
16x_S^2 + 12x_S - 1 >= 599/121 > 0.
```

Single deletions obey `x_S>=7/52>1/7168`. Thus every possible anchor case, every attached tree pattern, and every positive-weight triangulation with coefficients at most one passes simultaneously. This argument does not need to sample the 3,988 directional patterns: it dominates all of them. The 17-type classification and full nine-shape charts supply coverage; the controls and 347 material identities are reverified here.

All inequalities are strict, so each control has an open nine-dimensional chart neighborhood with the same property. No common neighborhood radius is asserted for those 17 neighborhoods. Volume ratios are affine invariant, so this volume-only feasibility is unaffected by any SPD metric, including arbitrarily large finite anisotropies and shears. This is **not** feasibility of the full mechanical formulas: the required escape inequalities have deliberately not been inferred from the cap volumes.

## 2. An actual-centered, shared-metric barrier for the representative record

### Exact physical body and labels

The old tuple is `(graph,stable,unstable,Q-tree-mask)=(31,1,0,6826)`, old graph mask `7427831`, canonical cross-edge code `37478`. The canonical parent arrays are

```text
P=(8,-1,1,6,3,4,7,0,1),
Q=(5,0,4,0,-1,4,7,1).
```

Thus the proposed canonical roots are primal vertex1 and polar vertex/facet4. The seven tree-closed masks are exactly `(4,32,36,48,52,56,60)`. These labels and the five complete adaptive decompositions are the literal atlas branch, not a new alias.

Take the following raw vertices:

```text
0=(0,0,0)
1=(1,0,0)
2=(227/32,37/32,0)
3=(157/32,47/32,0)
4=(147/32,47/32,0)
5=(0,1,0)
6=(0,0,1)
7=(0,-407/3169,1024/3169)
8=(459/2336,-259/2336,16/73).
```

In the inherited inward orientation, the eight maximal facet cycles, in canonical facet order, are

```text
012345, 0567, 078, 081, 18762, 263, 364, 465.
```

Let `g` be their exact ordinary volume centroid and define `p_i=L(v_i-g)`, where

```text
L=(1/32)*[[7,-19,-5],[0,28,38],[0,0,32]],
M=L^T L=(1/1024)*[[49,-133,-35],[-133,1145,1159],[-35,1159,2493]].
```

The leading principal minors of `M` are `49/1024`, `2401/65536`, and `2401/65536`, all positive. The actual poles are reconstructed from the transformed physical facets; equivalently the untransformed poles use `M^-1`, not a separately chosen dual metric.

The checker computes

```text
6 Vol(conv(v)) = 1313690577/118444544,
g_x = 1589425881289/767195296968,
g_y = 11603023218492689/19449935168732736,
g_z = 304946087963641/1215620948045796,
Vol(conv(p)) = 21456946091/60643606528,
g(conv(p)) = (0,0,0).
```

Every vertex and maximal facet is actual. All supporting triples are enumerated, all 56 dual-plane triples are independently checked, the two reconstructions give the same nine physical vertices, and the polar is bounded. All nonincidences are strict. The checker also verifies `q_f dot p_i > -3` for all pairs, hence both strict factor-1/3 reflection inclusions. No assertion that the polar itself has zero ordinary centroid is made.

### Exactly which strong inequalities pass

Write `R2=||p_1||^2`, `Q2=||q_4||^2`, and `c_S=g(K_S)` in these already centered physical coordinates. For `n=5,6,7`, set `b_n=kappa_n/12`; set `b_8=1/7168`. The inherited constants are `kappa_5=5/8`, `kappa_6=71/256`, and `kappa_7=1/16`. Since

```text
Gamma(kappa)=kappa/[2(sqrt(9+4kappa)+3)] < kappa/12,
```

the tests using `b_n` are stronger than the atlas's exact Gamma norm-gap requirement, not just its rounded gamma consequence. The Gamma identity and constants are inherited; their application to this actual control is new.

The following strict rational bounds hold at the control and throughout the certified parameter cube:

| Verified quantity | Strict lower bound |
|---|---:|
|`min_(i!=1) (R2-||p_i||^2)/R2`|`1/64`|
|`min_(f!=4) (Q2-||q_f||^2)/Q2`|`1/16`|
|`min_S (||c_S||^2/R2-b_(9-|S|)^2)` over **all23** admissible deletions|`1/65536`|
|Uniform volume-test residual over all23 deletions|`1/128`|
|Adaptive signed-moment residual divided by `R2`, over all five patterns|`1/34`|
|Adaptive volume-test residual over all five patterns|`3`|
|Single-child `F1/R2`, over the three anchor8 patterns|`3/20`|
|Single-child `F3/R2`, over the three anchor8 patterns|`3`|

Here the uniform volume residual is `x_S-1/7168` for a single deletion and `16x_S^2+12x_S-kappa_(9-|S|)` otherwise. The signed-moment residual is

```text
F2 = p_w dot (4c_S-p_1+p_w) - t_S ||p_w||^2,
t_S = sum_T d_T theta_T / sum_T d_T,
```

using the exact actual retained tetrahedra. The additional square-identity ingredients are

```text
F1=p_w dot (p_1-p_w),
F3=9||p_w||^2-||4c_S-p_1||^2.
```

All three ingredients are strict for the single-child cases. The anchor labels are the atlas's designated anchors for the recorded hypothetical tree; they do **not** assert that the physical control realizes that entire escape tree.

Every uniform cap system passes **unconditionally**, including the 16 admissible deletions not tree-closed for this record. Thus the atlas's conditional norm-order alternatives also pass without using their escape disjunct. Actual first moments and actual component volumes agree with direct retained-hull integration. This is stronger than merely assigning feasible free masses.

### The precise missing information

The full mechanical result is

```text
stable facets = [0,1,4,5,6,7]
unstable vertices = [0,1,2,3,5,6]
saddles = [(0,1),(0,5),(1,2),(2,3),(2,6),
           (3,6),(4,5),(4,6),(5,6),(6,7)]
(S,U,H) = (6,6,10).
```

All 15 true edges receive the complete four-component cone audit. The recorded arrow `0->8`, for example, has the exact **wrong** sign

```text
p_0 dot (p_8-p_0)
= -4496549521272374087479/23262744859729751703552 < 0.
```

There is a more specific loss inside the adaptive averaging. Define the individual-triangle residual

```text
J_(S,T) = [p_w dot sum_(i in T) p_i + (1-theta_T)||p_w||^2]/R2.
```

Then the actual control has

```text
mask36, anchor8, triangle(3,4,6), theta=1/16: J < -1/2;
mask48, anchor1, triangle(2,3,6), theta=59/256: J < -1/4.
```

Nevertheless their actual-volume-weighted averages `F2/R2` are positive. These two triangles are genuine original maximal triangular facets, not display diagonals. Both negative bounds also persist in the certified cube. This pinpoints information discarded by the integrated `T_S` tests.

Unlike the existing eight-pole cone-concentration barrier, the present control is an actual C30 polyhedron with exact own-volume centering and actual disjoint cap material. It is not a false-centroid, free-weight, rank-deficient, or noncoplanar control. Its failure is explicitly mechanical. The prior eight-pole control was expressly noncentered and not C30.

## 3. Continuous-domain and boundary status

For the representative type, the nine shape variables are `(a,b,c,d,e,f,alpha,beta,gamma)`, with base vertices `(a,b,0),(c,d,0),(e,f,0)` and

```text
h7=1+alpha(1-a), h8=1+beta+gamma,
v7=(0,alpha*b/h7,1/h7),
v8=((beta+gamma*a)/h8,gamma*b/h8,1/h8).
```

These identities preserve every intended coplanarity exactly. The other five variables are the two positive diagonal entries and three shears of an upper-triangular `L` with `L33=1`. This is a full local chart for physical metrics up to scale. Each of all14 coordinates varies independently by at most `2^-40` around `SHAPE+LPAR` below. The checker uses outward intervals on the `2^-100` grid and verifies 264 positive guards, 60 signed true-edge primitives, and the two negative individual-triangle bounds. It recomputes the actual centroid as a rational function throughout the box.

The box is entirely inside the strict incidence/SPD domain; it is not a norm-tie or zero-volume wall. The all-type volume argument is affine invariant and does not assume bounded shears or condition numbers. **No complementary unbounded shape region, SPD boundary approach, alternative root, coplanarity merger, or norm-tie stratum has been excluded.** All 17 full-type problems and all current hexagonal records remain open as physical110 systems. This result certifies nonemptiness of specified relaxations, not a whole-domain mechanical exclusion.

## 4. Complete recovery capsule

Save the following exact UTF-8/LF source, including its final newline, as `hex17_cap_relaxation_barrier.py`. Dependencies: **CPython3.13.5, standard library only, assertions enabled**. There are no external input files, numerical solvers, random seeds, or omitted helpers. The literal subset of the parent needed to reconstruct all controls, caps, record labels, and the reciprocal metric is embedded.

```python
"""HEX17_ACTUAL_CAP_RELAXATION_BARRIER_V1.
CPython 3.13.5; standard library; run with assertions enabled: python -S FILE.
No exclusion or 110 attainer. All inputs and exact verification are in this file.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
from pathlib import Path
import json, hashlib
assert __debug__
PARENT='minimum-0009'
PARENT_SHA='6f905a98d5d84d11e1369aebb34643ad59248a2485b95270c59bb52c48b92326'
FRONTIER_SHA='5d3329d312adf3db48d9e22314d6cec046f4ec9b00b29fe248fa96f699bb3f1f'
ATLAS_SHA='f37ea08f97d022629d02ca7d5356dfed5c2058658691bf45eeca9ca925691cf1'
# code, inward maximal face cycles, exact roof vertices 7 and 8.
# Common base is 00,10,21,22,12,01; vertex 6 is 001.
DATA=[
(37460,'012345 0568 0871 1762 263 364 465 678','1/18 -1/18 8/9;0 -1/18 8/9'),
(37478,'012345 0567 078 081 18762 263 364 465','0 -1/65 64/65;1/67 -2/67 64/67'),
(37524,'012345 0568 0871 172 2763 364 465 678','2/17 -3/17 16/17;0 -3/17 16/17'),
(37541,'012345 056 0678 081 1872 2763 364 465','2/65 -8/65 64/65;3/70 -6/35 32/35'),
(37542,'012345 0567 078 081 1872 2763 364 465','0 -1/2 1;1/18 -1/2 8/9'),
(37556,'012345 05678 081 172 187 2763 364 465','0 -1/32 1;0 -1/22 32/33'),
(37604,'012345 05678 081 1872 263 276 364 465','0 -1/11 32/33;0 -2/17 16/17'),
(37670,'012345 0567 078 081 182 28763 364 465','0 -1/32 1;2/65 -3/65 64/65'),
(38052,'012345 0568 081 1872 273 3764 465 678','2/15 -2/15 16/15;0 -4/15 16/15'),
(38053,'012345 056 0678 081 1872 273 3764 465','1/30 -2/15 16/15;3/65 -12/65 64/65'),
(38054,'012345 0567 078 081 1872 273 3764 465','0 -2/3 4/3;1/14 -9/14 8/7'),
(38068,'012345 05678 081 172 187 273 3764 465','0 -2/15 16/15;0 -3/17 16/17'),
(38179,'012345 056 067 0781 182 2873 3764 465','1/15 -2/15 16/15;3/16 -1/8 1'),
(38181,'012345 056 0678 081 182 2873 3764 465','1/30 -2/15 16/15;4/61 -16/61 64/61'),
(38194,'012345 0567 071 178 182 2873 3764 465','0 -2/3 4/3;2/7 -1/2 8/7'),
(38308,'012345 05678 081 182 273 287 3764 465','0 -2/15 16/15;0 -1/4 1'),
(42149,'012345 056 0678 081 1872 273 374 4765','1/59 -4/59 64/59;1/32 -1/8 1')]
parse=lambda s:tuple(map(F,s.split()))
BASE=[parse(s)for s in ('0 0 0','1 0 0','2 1 0','2 2 0','1 2 0','0 1 0','0 0 1')]
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
scale=lambda c,a:tuple(c*x for x in a)
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def norm(a):return dot(a,a)
def edges(fs):return sorted({tuple(sorted((a,b)))for f in fs for a,b in zip(f,f[1:]+f[:1])})
def facets(text):return [tuple(map(int,s[::-1]))for s in text.split()]
def hull2(pts):
 def turn(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
 halves=[]
 for seq in (sorted(pts),sorted(pts,reverse=True)):
  h=[]
  for p in seq:
   while len(h)>1 and turn(h[-2],h[-1],p)<=0:h.pop()
   h.append(p)
  halves.append(h[:-1])
 return halves[0]+halves[1]
def hull(v):
 # Enumerate ALL supporting triples; merge coplanar maximal faces exactly.
 planes={}
 for a,b,c in combinations(sorted(v),3):
  n=cross(sub(v[b],v[a]),sub(v[c],v[a]));vals=[dot(n,sub(x,v[a]))for x in v.values()]
  if not any(n) or (min(vals)<0<max(vals)) or min(vals)==max(vals):continue
  if max(vals)>0:n=scale(-1,n)
  ids=tuple(i for i in v if dot(n,sub(v[i],v[a]))==0);planes[ids]=n
 fs=[]
 for ids,n in sorted(planes.items()):
  k=max(range(3),key=lambda j:abs(n[j]));xy=[j for j in range(3)if j!=k]
  flat={tuple(v[i][j]for j in xy):i for i in ids};assert len(flat)==len(ids)
  f=tuple(flat[x]for x in hull2(flat));assert len(f)==len(ids)
  if dot(n,cross(sub(v[f[1]],v[f[0]]),sub(v[f[2]],v[f[0]])))<0:f=f[::-1]
  k=f.index(min(f));fs.append(f[k:]+f[:k])
 es=edges(fs);assert set().union(*map(set,fs))==set(v)
 assert len(v)-len(es)+len(fs)==2
 assert all(sum(a in f and b in f for f in fs)==2 for a,b in es)
 return fs,es

def integrate(v,fs,apex=None):
 # D=6 volume, N=24 first moment. Two independent triangulations are used.
 D=0;N=(0,0,0)
 for f in fs:
  if apex is not None and apex in f:continue
  for j in range(1,len(f)-1):
   a,b,c=[v[i]for i in (f[0],f[j],f[j+1])]
   if apex is None:d=det(a,b,c);s=add(add(a,b),c)
   else:
    o=v[apex];d=det(sub(a,o),sub(b,o),sub(c,o));s=add(add(add(o,a),b),c)
    assert d>0
   D+=d;N=add(N,scale(d,s))
 assert D>0
 return D,N,scale(1/(4*D),N)

def components(fs):
 adj=[set()for _ in range(9)]
 for a,b in edges(fs):adj[a].add(b);adj[b].add(a)
 ans=[]
 for mask in range(1,64):
  if mask.bit_count()>4:continue
  S={i for i in range(6)if mask>>i&1};cc=[];ok=True
  for a in sorted(S):
   if (a-1)%6 in S:continue
   block=[];j=a
   while j in S:block.append(j);j=(j+1)%6
   owners=set(range(6,9))
   for i in block:
    if len(adj[i])!=3:owners.clear();break
    owners &= adj[i]
   if len(owners)!=1:ok=False;break
   cc.append((tuple(block),next(iter(owners))))
  if ok and cc:ans.append((mask,cc))
 return ans

def cap(v,co):
 block,a=co;cyc=((block[0]-1)%6,)+block+((block[-1]+1)%6,)
 area=0;J=(0,0,0)
 for i,j in zip(cyc,cyc[1:]+cyc[:1]):
  w=v[i][0]*v[j][1]-v[i][1]*v[j][0];area+=w;J=add(J,scale(w,add(v[i],v[j])))
 return v[a][2]*area,scale(v[a][2],add(scale(area,v[a]),J))

def all_caps(v,fs,check):
 D,N,g=integrate(v,fs,6);out={}
 for mask,cc in components(fs):
  dc=0;H=(0,0,0)
  for co in cc:
   a,b=cap(v,co);dc+=a;H=add(H,b)
   if check:
    block,owner=co;ids={(block[0]-1)%6,*block,(block[-1]+1)%6,owner}
    cv={i:v[i]for i in ids};cf,ce=hull(cv);dd,nn,cg=integrate(cv,cf)
    assert (a,b)==(dd,nn)
  retained={i:v[i]for i in v if not(i<6 and mask>>i&1)}
  D0=D-dc;N0=sub(N,H);cg=sub(scale(1/(4*D0),N0),g)
  if check:
   rf,re=hull(retained);rd,rn,rg=integrate(retained,rf)
   assert (D0,N0)==(rd,rn) and cg==sub(rg,g)
  out[mask]=(dc,D0,cg,cc)
 return D,N,g,out

def check_all_types():
 minima={i:None for i in range(1,5)};at={};counts=Counter();comps=Counter();rows=[]
 for code,text,roof in DATA:
  v=dict(enumerate(BASE+[parse(s)for s in roof.split(';')]));fs=facets(text)
  hf,es=hull(v);assert set(map(frozenset,hf))==set(map(frozenset,fs))
  assert (len(v),len(es),len(hf))==(9,15,8)
  assert sum(1<<(3*a+b-6)for a,b in es if a<6<=b)==code
  D,N,g,cs=all_caps(v,fs,True);assert integrate(v,hf)[:2]==(D,N)
  by={}
  for mask,(dc,D0,cg,cc)in cs.items():
   x=dc/D0;k=mask.bit_count();counts[k]+=1;comps[len(cc)]+=1
   if minima[k] is None or x<minima[k]:minima[k]=x;at[k]=[code,mask]
   by[k]=min(x,by.get(k,x))
   if k==1:assert x>=F(7,52)>F(1,7168)
   else:
    assert x>=F(15,44)
    assert 4*x-1>=F(4,11)
    assert 16*x*x+12*x-1>=F(599,121)
  rows.append(dict(code=code,caps=len(cs),min_ratio={str(k):str(x)for k,x in by.items()}))
 assert dict(counts)=={1:88,2:150,3:94,4:15}
 assert dict(comps)=={1:140,2:187,3:20}
 assert minima=={1:F(7,52),2:F(15,44),3:F(52,75),4:F(106,21)}
 return dict(types=rows,total_caps=sum(counts.values()),by_size=dict(counts),by_components=dict(comps),minima={str(k):str(v)for k,v in minima.items()},minimum_locations=at)

# The exact current-record control. All 14 coordinates are free locally.
SHAPE=parse('227/32 37/32 157/32 47/32 147/32 47/32 -11/32 4 -7/16')
LPAR=parse('7/32 7/8 -19/32 -5/32 19/16')
PP=(8,-1,1,6,3,4,7,0,1)
QP=(5,0,4,0,-1,4,7,1)
MASKS=(4,32,36,48,52,56,60)
DIR={
36:(8,((0,6,4),(0,7,6),(0,8,7),(3,4,6)),parse('21/64 5/8 7/8 1/16')),
48:(1,((0,6,3),(0,7,6),(0,8,7),(2,3,6)),parse('27/256 71/256 5/8 59/256')),
52:(8,((0,6,3),(0,7,6),(0,8,7)),parse('103/256 5/8 7/8')),
56:(1,((0,6,2),(0,7,6),(0,8,7)),parse('135/256 71/256 5/8')),
60:(8,((0,7,6),(0,8,7)),parse('5/8 7/8'))}
FS=facets(DATA[1][1]);ES=edges(FS)
QE=sorted({tuple(sorted((i,j)))for a,b in ES for i in range(8)for j in range(i+1,8)if a in FS[i]and b in FS[i]and a in FS[j]and b in FS[j]})
KAP={5:F(5,8),6:F(71,256),7:F(1,16)}
# Literal old-graph31 edge order and canonical-to-old maps from the catalogue.
OLD_PE=((0,5),(1,3),(2,4),(0,3),(1,4),(2,5),(6,8),(6,7),(0,7),(5,8),(3,6),(1,8),(4,8),(2,8),(3,7))
OLD_QE=((0,1),(0,2),(0,3),(0,5),(0,6),(0,7),(1,2),(1,4),(1,5),(1,7),(2,4),(2,6),(3,6),(3,7),(4,5))
VP=(3,0,5,2,4,1,8,6,7);FP=(0,2,4,5,1,7,3,6)
def bind_record():
 all_pairs=list(combinations(range(8),2))
 assert sum(1<<all_pairs.index(e)for e in OLD_QE)==7427831
 def parents(ee,root,n):
  adj=[[]for _ in range(n)]
  for a,b in ee:adj[a].append(b);adj[b].append(a)
  p=[None]*n;p[root]=-1;todo=[root]
  for a in todo:
   for b in adj[a]:
    if p[b] is None:p[b]=a;todo.append(b)
  assert len(todo)==n;return p
 pp=parents([e for i,e in enumerate(OLD_PE)if not(6826>>i&1)],0,9)
 qp=parents([e for i,e in enumerate(OLD_QE)if 6826>>i&1],1,8)
 assert tuple(-1 if pp[j]<0 else VP.index(pp[j])for j in VP)==PP
 assert tuple(-1 if qp[j]<0 else FP.index(qp[j])for j in FP)==QP
 assert set(OLD_PE)=={tuple(sorted((VP[a],VP[b])))for a,b in ES}
 assert set(OLD_QE)=={tuple(sorted((FP[a],FP[b])))for a,b in QE}
 for (a,b),(f,g)in zip(OLD_PE,OLD_QE):
  assert {f,g}=={FP[i]for i,face in enumerate(FS)if a in {VP[j]for j in face}and b in {VP[j]for j in face}}


def chart(t):
 a,b,c,d,e,f,al,be,ga=t
 h7=1+al*(1-a);h8=1+be+ga
 v=[(0,0,0),(1,0,0),(a,b,0),(c,d,0),(e,f,0),(0,1,0),(0,0,1),
    (0,al*b/h7,1/h7),((be+ga*a)/h8,ga*b/h8,1/h8)]
 return dict(enumerate(v)),(h7,h8)

def model(t):
 v,heights=chart(t[:9]);a,b,c,d,e=t[9:];L=((a,c,d),(0,b,e),(0,0,1))
 transform=lambda x:tuple(dot(row,x)for row in L)
 D,N,g=integrate_generic(v,FS);p=[transform(sub(v[i],g))for i in range(9)]
 q=[];guards={}
 def put(k,x):guards[k]=x
 put('height7',heights[0]);put('height8',heights[1]);put('L00',a);put('L11',b)
 for fi,f in enumerate(FS):
  v0,v1,v2=[v[i]for i in f[:3]];n=cross(sub(v1,v0),sub(v2,v0));put('normal:'+str(fi),norm(n))
  for j in v:
   if j not in f:put('support:%d:%d'%(fi,j),-dot(n,sub(v[j],v0)))
  for i,j in zip(f,f[1:]+f[:1]):
   for k in f:
    if k not in (i,j):put('side:%d:%d:%d:%d'%(fi,i,j,k),dot(n,cross(sub(v[j],v[i]),sub(v[k],v[i]))))
  nn=cross(sub(p[f[1]],p[f[0]]),sub(p[f[2]],p[f[0]]));hh=dot(nn,p[f[0]])
  put('pole_height:'+str(fi),hh);q.append(scale(1/hh,nn))
 R=norm(p[1]);Q=norm(q[4]);put('D',D)
 for i in range(9):
  if i!=1:put('Pmax:'+str(i),(R-norm(p[i]))/R)
 for i in range(8):
  if i!=4:put('Qmax:'+str(i),(Q-norm(q[i]))/Q)
 caps={}
 for mask,cc in components(FS):
  dc=0;H=(0,0,0)
  for co in cc:
   dd,nn=cap(v,co);dc+=dd;H=add(H,nn)
  D0=D-dc;cg=transform(sub(scale(1/(4*D0),sub(N,H)),g));x=dc/D0;k=mask.bit_count()
  put('cap_volume:'+str(mask),dc);put('retained_volume:'+str(mask),D0)
  # kappa/12 is a STRICT rational upper bound for Gamma(kappa).
  upper=F(1,7168)if k==1 else KAP[9-k]/12
  put('cap_norm:'+str(mask),(norm(cg)-upper*upper*R)/R)
  put('cap_ratio:'+str(mask),x-F(1,7168)if k==1 else 16*x*x+12*x-KAP[9-k])
  if mask in DIR:
   w,tri,th=DIR[mask];ds=[det(*(sub(v[i],v[1])for i in tr))for tr in tri]
   for j,z in enumerate(ds):put('tet:%d:%d'%(mask,j),z)
   theta=sum(z*c for z,c in zip(ds,th))/D0
   F2=dot(p[w],sub(scale(4,cg),sub(p[1],p[w])))-theta*norm(p[w])
   put('direction:'+str(mask),F2/R)
   put('adaptive_ratio:'+str(mask),4*x-theta if w==1 else 16*x*x+12*x-theta)
   if w!=1:
    put('square_F1:'+str(mask),dot(p[w],sub(p[1],p[w]))/R)
    put('square_F3:'+str(mask),(9*norm(p[w])-norm(sub(scale(4,cg),p[1])))/R)
   caps[mask]=(x,theta)
  else:caps[mask]=(x,None)
 arcs={}
 for name,pts,ee in (('P',p,ES),('Q',q,QE)):
  for i,j in ee:
   arcs['%s:%d:%d'%(name,i,j)]=dot(pts[i],sub(pts[j],pts[i]))
   arcs['%s:%d:%d'%(name,j,i)]=dot(pts[j],sub(pts[i],pts[j]))
 return v,L,D,N,g,p,q,guards,arcs,caps

def integrate_generic(v,fs):
 # Same positive apex-6 formula, usable with outward intervals as well.
 D=0;N=(0,0,0)
 for f in fs:
  if 6 in f:continue
  for j in range(1,len(f)-1):
   ids=(6,f[0],f[j],f[j+1]);o=v[6]
   d=det(*(sub(v[i],o)for i in ids[1:]));D+=d
   N=add(N,scale(d,tuple(sum(v[i][k]for i in ids)for k in range(3))))
 return D,N,scale(1/(4*D),N)

# Small directed-rounding interval implementation; each endpoint on 2^-100.
GRID=1<<100
class I:
 def __init__(self,a,b=None):
  if isinstance(a,I):self.lo,self.hi=a.lo,a.hi;return
  a=F(a);b=a if b is None else F(b);assert a<=b
  self.lo=F((a*GRID).__floor__(),GRID);self.hi=F((b*GRID).__ceil__(),GRID)
 def __add__(a,b):
  b=I(b);return I(a.lo+b.lo,a.hi+b.hi)
 __radd__=__add__
 def __neg__(a):return I(-a.hi,-a.lo)
 def __sub__(a,b):return a+-I(b)
 def __rsub__(a,b):return I(b)+-a
 def __mul__(a,b):
  b=I(b);v=[x*y for x in (a.lo,a.hi)for y in (b.lo,b.hi)];return I(min(v),max(v))
 __rmul__=__mul__
 def __truediv__(a,b):
  b=I(b);assert b.lo*b.hi>0
  return a*I(1/b.hi,1/b.lo)
 def __rtruediv__(a,b):return I(b)/a

def verify_witness():
 bind_record()
 t=SHAPE+LPAR;v,L,D,N,g,p,q,gs,arcs,caps=model(t)
 assert all(x>0 for x in gs.values()) and all(x!=0 for x in arcs.values())
 hf,he=hull(v);assert he==ES and set(map(frozenset,hf))==set(map(frozenset,FS))
 assert integrate(v,hf)==(D,N,g);assert all_caps(v,FS,True)[:3]==(D,N,g)
 pv=dict(enumerate(p));pf,pe=hull(pv);PD,PN,PG=integrate(pv,pf)
 assert PN==(0,0,0) and PG==(0,0,0) and PD==D*L[0][0]*L[1][1]
 qf,qe=hull(dict(enumerate(q)));assert qe==QE
 for f in qf:
  a,b,c=[q[i]for i in f[:3]];assert dot(cross(sub(b,a),sub(c,a)),a)>0
 # Independent H-driven enumeration: every one of the 56 plane triples.
 hp=set()
 for aa,bb,cc in combinations(q,3):
  dd=det(aa,bb,cc)
  if not dd:continue
  x=scale(1/dd,add(add(cross(bb,cc),cross(cc,aa)),cross(aa,bb)))
  if all(dot(n,x)<=1 for n in q):hp.add(x)
 assert hp==set(p)
 M=tuple(tuple(sum(L[k][i]*L[k][j]for k in range(3))for j in range(3))for i in range(3))
 assert M==tuple(tuple(F(x,1024)for x in row)for row in ((49,-133,-35),(-133,1145,1159),(-35,1159,2493)))
 assert det(*M)==F(2401,65536)

 assert all(dot(q[i],p[j])==1 for i in range(8)for j in FS[i])
 assert all(dot(q[i],p[j])<1 for i in range(8)for j in range(9)if j not in FS[i])
 # Both reflection inclusions follow from actual centering; check independently.
 assert all(dot(qi,pj)>-3 for qi in q for pj in p)
 closed=[]
 for mask,cc in components(FS):
  retained={i for i in range(9)if not(i<6 and mask>>i&1)}
  if 1 in retained and all(PP[i] in retained for i in retained if i!=1):closed.append(mask)
 assert tuple(closed)==MASKS
 for i,j in enumerate(PP):
  if j>=0:assert tuple(sorted((i,j)))in ES
 for i,j in enumerate(QP):
  if j>=0:assert tuple(sorted((i,j)))in QE
 for mask,(w,ts,theta)in DIR.items():
  ids={i:v[i]for i in range(9)if not(i<6 and mask>>i&1)};rf,re=hull(ids)
  rd,rn,rg=integrate(ids,rf)
  ds=[det(*(sub(v[i],v[1])for i in tr))for tr in ts]
  assert min(ds)>0 and sum(ds)==rd
  tn=(0,0,0)
  for d,tr in zip(ds,ts):tn=add(tn,scale(d,add(v[1],add(add(v[tr[0]],v[tr[1]]),v[tr[2]]))))
  assert tn==rn and 0<caps[mask][1]<=1
 # Exact complete face, vertex and true-edge mechanics, with independent feet.
 stable=[];unstable=[];saddles=[];edge_rows=[]
 for i,f in enumerate(FS):
  foot=scale(1/norm(q[i]),q[i])
  signs=[dot(q[i],cross(sub(p[b],p[a]),sub(foot,p[a]))) for a,b in zip(f,f[1:]+f[:1])]
  yes=min(signs)>0
  assert yes==all(dot(q[i],sub(q[j],q[i]))<0 for j in range(8)if j!=i)
  if yes:stable.append(i)
 for i in range(9):
  if all(dot(p[i],sub(p[j],p[i]))<0 for j in range(9)if j!=i):unstable.append(i)
 for a,b in ES:
  f,gf=[i for i,f in enumerate(FS)if a in f and b in f]
  d=sub(p[b],p[a]);tt=-dot(p[a],d)/norm(d);foot=add(p[a],scale(tt,d))
  aa,bb,cc=norm(q[f]),dot(q[f],q[gf]),norm(q[gf]);dd=aa*cc-bb*bb;assert dd>0
  ff,gg=dot(foot,q[f]),dot(foot,q[gf]);be=(cc*ff-bb*gg)/dd;ga=(aa*gg-bb*ff)/dd
  components4=(tt,1-tt,be,ga);assert all(z!=0 for z in components4)
  yes=min(components4)>0
  neg4=all(arcs[k]<0 for k in ('P:%d:%d'%(a,b),'P:%d:%d'%(b,a),'Q:%d:%d'%(f,gf),'Q:%d:%d'%(gf,f)))
  assert yes==neg4
  if yes:saddles.append([a,b])
  edge_rows.append(dict(edge=[a,b],facets=[f,gf],components=list(map(str,components4))))
 assert stable==[0,1,4,5,6,7] and unstable==[0,1,2,3,5,6]
 assert len(saddles)==10 and len(stable)+len(unstable)-len(saddles)==2
 # 14-dimensional incidence-stratum and metric box, actual centroid recomputed.
 radius=F(1,1<<40);it=[I(x-radius,x+radius)for x in t]
 iv,iL,iD,iN,ig,ip,iq,igs,ia,ic=model(it)
 for k,x in igs.items():assert I(x).lo>0,('interval guard',k)
 for k,x in ia.items():assert (I(x).lo>0 if arcs[k]>0 else I(x).hi<0),('interval arc',k)
 assert len(ia)==60
 lost=[]
 for mask,idx in ((36,3),(48,3)):
  w,ts,ths=DIR[mask];tr=ts[idx];theta=ths[idx]
  z=(dot(p[w],tuple(sum(p[i][k]for i in tr)for k in range(3)))+(1-theta)*norm(p[w]))/norm(p[1])
  bound=F(-1,2)if mask==36 else F(-1,4)
  assert z<bound
  iz=(dot(ip[w],tuple(sum(ip[i][k]for i in tr)for k in range(3)))+(1-theta)*norm(ip[w]))/norm(ip[1])
  assert I(iz).hi<bound
  lost.append(dict(mask=mask,triangle=tr,theta=str(theta),normalized_primitive=str(z)))
 groups={}
 for k,x in gs.items():
  name=k.split(':')[0];groups[name]=min(x,groups.get(name,x))
 bounds={'Pmax':F(1,64),'Qmax':F(1,16),'cap_norm':F(1,65536),'cap_ratio':F(1,128),'direction':F(1,34),'adaptive_ratio':F(3),'square_F1':F(3,20),'square_F3':F(3)}
 for name,bound in bounds.items():
  assert groups[name]>bound
  assert all(I(x).lo>bound for k,x in igs.items()if k.split(':')[0]==name)
 return dict(rational_lower_bounds={k:str(x)for k,x in bounds.items()},failed_individual_triangle_bounds=lost,record=[31,1,0,6826],old_graph_mask=7427831,code=37478,shape=list(map(str,SHAPE)),L=[[str(x)for x in row]for row in L],raw_vertices=[[str(x)for x in v[i]]for i in range(9)],raw_D=str(D),raw_centroid=list(map(str,g)),physical_volume=str(PD/6),physical_centroid=list(map(str,PG)),P_parent=PP,Q_parent=QP,tree_closed_masks=MASKS,all_admissible_masks=list(caps),cap_ratios_and_theta={str(k):[str(x),None if y is None else str(y)]for k,(x,y)in caps.items()},guard_count=len(gs),group_minima={k:str(x)for k,x in groups.items()},P_selected_arrows=[str(arcs['P:%d:%d'%(i,j)])for i,j in enumerate(PP)if j>=0],Q_selected_arrows=[str(arcs['Q:%d:%d'%(i,j)])for i,j in enumerate(QP)if j>=0],stable=stable,unstable=unstable,saddles=saddles,edge_audit=edge_rows,interval_radius=str(radius),interval_grid_bits=100,interval_guards=len(igs)+len(ia)+len(lost))

def main():
 a=check_all_types();print('ALL_17_ACTUAL_SHAPES_347_DISJOINT_CAP_SUBSETS_PASS')
 print('MIN_CAP_RATIOS_BY_SIZE','7/52','15/44','52/75','106/21')
 b=verify_witness();print('ACTUAL_CENTERED_C30_SHARED_METRIC_ALL_23_CAPS_AND_FIVE_DIRECTIONS_PASS')
 print('STRICT_ROOT_NORMS_AND_SQUARE_IDENTITY_INGREDIENTS_PASS')
 print('EXACT_MECHANICS',len(b['stable']),len(b['unstable']),len(b['saddles']))
 print('FOURTEEN_DIMENSIONAL_BOX_PASS',b['interval_radius'],b['interval_guards'])
 report=dict(version=1,parent=PARENT,parent_sha256=PARENT_SHA,parent_frontier_sha256=FRONTIER_SHA,atlas_source_sha256=ATLAS_SHA,volume_only_barrier=a,shared_metric_barrier=b,scope='RELAXATION_BARRIERS_ONLY_NO_ROOT_OR_TYPE_EXCLUSION_NO_ATTAINER')
 raw=(json.dumps(report,sort_keys=True,separators=(',',':'))+'\n').encode();Path('hex17_cap_relaxation_barrier.json').write_bytes(raw)
 print('REPORT',len(raw),hashlib.sha256(raw).hexdigest())
 src=Path(__file__).read_bytes();print('SOURCE',len(src),hashlib.sha256(src).hexdigest())
 print('HEX17_ACTUAL_CAP_RELAXATION_BARRIER_PASS_NO_FRONTIER_CHANGE')
if __name__=='__main__':main()
```

Run:

```bash
python3 -S hex17_cap_relaxation_barrier.py
sha256sum hex17_cap_relaxation_barrier.py hex17_cap_relaxation_barrier.json
```

The following markers were **observed**, including a second execution in a clean directory containing only the source. The generated reports were byte-identical:

```text
ALL_17_ACTUAL_SHAPES_347_DISJOINT_CAP_SUBSETS_PASS
MIN_CAP_RATIOS_BY_SIZE 7/52 15/44 52/75 106/21
ACTUAL_CENTERED_C30_SHARED_METRIC_ALL_23_CAPS_AND_FIVE_DIRECTIONS_PASS
STRICT_ROOT_NORMS_AND_SQUARE_IDENTITY_INGREDIENTS_PASS
EXACT_MECHANICS 6 6 10
FOURTEEN_DIMENSIONAL_BOX_PASS 1/1099511627776 326
REPORT 11141 eb6e868921149cba97809d571ce5fc3cb901739b5ce85d5e5f2d3d0012ed939d
SOURCE 19287 1b82d75c3aae61caebaa65e0cf97f1de2f1df31fd9295bcb585b959755c00cfc
HEX17_ACTUAL_CAP_RELAXATION_BARRIER_PASS_NO_FRONTIER_CHANGE
CLEAN_REPORT_BYTE_IDENTICAL_PASS
```

`CLEAN_REPORT_BYTE_IDENTICAL_PASS` is the observed result of the external `cmp` between the two generated reports, not a marker printed by the checker itself. Reproduce it by running the source in a second empty directory and comparing the reports.

| Object | Bytes | SHA-256 |
|---|---:|---|
|`hex17_cap_relaxation_barrier.py`|19287|`1b82d75c3aae61caebaa65e0cf97f1de2f1df31fd9295bcb585b959755c00cfc`|
|`hex17_cap_relaxation_barrier.json`|11141|`eb6e868921149cba97809d571ce5fc3cb901739b5ce85d5e5f2d3d0012ed939d`|

Convenience copies: complete source (`hex17_cap_relaxation_barrier.py`) and exact generated report (`hex17_cap_relaxation_barrier.json`). The inline source, not these links alone, is the recovery authority for the new objects.

## 5. Most useful continuation

The current atlas volume-only route is now blocked by explicit strict witnesses for every type, even after imposing all admissible deletion sets simultaneously. A continuation should therefore retain the complete true-edge escape system and its individual directional projection consequences in the same physical shape/metric chart, rather than attempting another exclusion from the presently bounded coefficients `0<t_S<=1` alone. In the representative record, the two literal negative facet-triangle residuals above identify exactly where weighted averaging discarded relevant information.

I have **not** proved that adding those two inequalities closes this record, much less its whole joint-root group. No solver failure is promoted to UNSAT. The durable output is the universal volume-relaxation barrier and the exact, open, actual-centered shared-metric cap-relaxation barrier; the global minimum bracket and canonical frontier are unchanged.
