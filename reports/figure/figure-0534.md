# figure-0534

AI research report · 2026-09-24 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# W50 — whole-basin material removal, an exact moving-root obstruction, and a finite support-deletion obstruction

## Result and source-authority correction

**No own110 body is claimed.** The substantive new results are seven exactly audited rational bodies, an exact obstruction for an entire one-parameter material-change family and a neighborhood of affine metrics, and an exhaustive exact obstruction for 127 support-deletion bodies.

There is a material conflict between the assignment/journal summary and its literal parent. The summary names `H44_FROM_G45_QSRC38`, `H45_Q12STEP12`, `w49_general_exact.py`, and a G45 reconstruction bundle. Those objects and that auditor are not in the supplied immutable parent payload. The literal payload under `figure-0531`, headed SHA-256 `cdadf1fd175ad297d3d77738f88d2a85ebefc9f0d8c576774c2bd2f7aeb5d533`, instead contains the earlier W49 result and its complete `RECOVER_W49.py` capsule. The summary's proposed objects are therefore missing exact dependencies, not aliases that can safely be reconstructed from their names. The conflicting summary and the actual beginning of the literal payload are visible in the supplied update.  

The actual, recoverable parent controls are:

| Literal parent body | Actual V/E/F | C | Strict S/U/H | Additional weak; primitive zero | P/Q |
|---|---:|---:|---:|---|---:|
| `R3_H44_GROWN_S1_G6` | 84/126/44 | 252 | 1/2/1 | 000; 000 | 1/0 |
| `R3_HBRIDGE_S1_G3` | 44/66/24 | 132 | 1/2/1 | 000; 000 | 1/0 |

These are not the requested 68/126/60 and 38/66/30 bodies. In particular, the actual H44 has U0/U82 and saddle [4,17], not U25/U49 and saddle [3,20]. Its remaining P component has 54 vertices and 22 cut edges. The actual small H24 control has U0/U43, saddle [7,23], and a 17-vertex P component. The literal parent also retains the original R3 identity U57, Q33/cut21 and depth 0.3682015269855614; the conflicting U41/Q32/depth 0.3343046 summary was not used as an input.  

The entire supplied update and literal payload were read during the preceding stages of this continuation. Research proceeded on the genuinely supplied H44/H24 controls rather than inventing the missing G45 objects. The completed certificates below concern the actual H24 control. The corresponding H44 deletion batch did not finish with a retained aggregate certificate and is not presented as an exact exclusion.

## 1. One plane removes the entire actual P17 component

Let K be the literal `R3_HBRIDGE_S1_G3`, with its canonical sorted vertex labels. Its finite P component is exactly

```text
T = [18,23,26,30,31,32,33,34,35,36,37,38,39,40,41,42,43].
```

Use the rational normal

```text
n = (1000,-144,-720).
```

Direct exact evaluation on the parent vertices gives

```text
L = max_{i not in T} n·p_i = -6821960000/154504117
R = min_{i in T}     n·p_i =   454940000/37147643
L ≈ -44.153904326057535
R ≈  12.246806614352357.
```

Thus, for every **L < h < R**, the physical body

```text
K(h) = K ∩ {x : n·x ≤ h}
```

removes all 17 old component vertices, including the old junior U43, and retains all 27 complementary old vertices. There are precisely 17 crossed genuine parent edges and 17 new vertices. Throughout the open interval the actual complex is **V44/E66/F24**. There are 25 supplied inequalities, but only 24 maximal facets: the new cap replaces one old facet. These are actual polygonal facets and edges, not a triangulated count.

This is a finite whole-basin material replacement with no increase in edge count. It is not a cancellation of the homogeneous body's remaining U/H defect.

### Seven complete exact endpoint audits

The offsets

```text
h = -40, -30, -20, -16, -10, 0, 10
```

were all executed through the full parent exact H auditor. Every endpoint has:

```text
V/E/F = 44/66/24, C = 132
strict S/U/H = 10/2/10
closed-weak S/U/H = 10/2/10
additional weak = 0/0/0
primitive zero = 0/0/0
positive P bars = 1
positive Q bars = 9.
```

All exact positive bars remain in the generated audits. No numerical cutoff is used. The audits contain the actual rational vertices, maximal facets, true edges, filled volume, first moment, centroid, direct mechanical census, and complete positive P/Q bar records.

The material change is large, not a frozen-centre construction. The parent centroid is approximately

```text
(-0.263480795088, -0.201453201058, -0.046194462859).
```

For the new endpoints, the actual homogeneous centroids are approximately:

| h | Actual centroid |
|---:|---|
| -40 | (-1.319050799852948, -0.49234791025775226, 0.2541756719506645) |
| -30 | (-1.3137419629399811, -0.4904659009011793, 0.2520837718175434) |
| -20 | (-1.3084484589509946, -0.48859569318740576, 0.25000206971216804) |
| -16 | (-1.3063354056367382, -0.48785091928024343, 0.24917230605733715) |
| -10 | (-1.3031705329778576, -0.48673730761786715, 0.24793084100611615) |
| 0 | (-1.2979084253553037, -0.4848907609904548, 0.24587035942930335) |
| 10 | (-1.2926623718645074, -0.4830560665467361, 0.24382089717749847) |

The complete rational masses and centroids regenerate from the code below; these decimal displays are not verification inputs.

### The surviving and replacement roots

At h = -16, the exact strict U are canonical vertices 0 and 39:

```text
p_0  = (-824520000,-310160500,282508500)/203480401
p_39 = (24484790,76376768,22744542)/180595927.
```

Their support triples in the literal input-row numbering are

```text
p_0:  [0,3,23]
p_39: [18,19,24], where row24 is the added cap.
```

The elder p0 is an unchanged parent vertex. Vertex39 is a genuinely new cap vertex, not the old junior under another label. The old U43 has been removed. The cap has transferred the defect to a new root while the own centroid has moved substantially.

At this endpoint the strict stable facets are canonical

```text
[0,2,3,4,5,7,8,9,10,12].
```

The remaining P depth is approximately 0.8990052154002719. The largest of the nine Q depths is approximately 0.40100049836616347. These are useful negative controls, not improvements over the inherited own121 controls.

## 2. Exact obstruction for every offset and a full affine-metric box

### Proven statement

For every **L < h < R** and every symmetric positive-definite matrix G satisfying

```text
|G_ab - δ_ab| ≤ 1/64   for every a,b,
```

K(h) has at least two strict U at its own homogeneous centroid in metric G. Equivalently, for every nonsingular affine linear part A with G = AᵀA in this box, the uniformly filled physical body A K(h) has at least two strict U at its own centroid.

The two roots are followed by their support triples [0,3,23] and [18,19,24]. Labels 0 and 39 identify them at h = -16; they are not an instruction to reuse sorted vertex IDs after every parameter change.

Consequently, **none of this continuous offset/metric family is own110**, regardless of its other equilibria. The result does not cover rotating the cap normal, changing any of the remaining parent planes, arbitrary additional material changes, or all positive-definite metrics.

### Certificate mechanism

Set t = (h-L)/(R-L). Every retained vertex is constant in t; every new cap vertex is affine in t. The code verifies that the entire moving vertex set is exactly the union of the 27 retained vertices and the 17 crossed-edge intersection recipes.

Using outward-oriented maximal-facet fans only for mass integration, define

```text
W(t) = 6 Vol(K(h)),
M(t) = 24 ∫_{K(h)} x dx,
g(t) = M(t)/(4W(t)).
```

W has degree at most 3 and M degree at most 4. Exact Bernstein coefficients certify W(t)>0. The polynomial volume and centroid were also compared exactly with ordinary full H audits at h=-40,-16,10.

For each root i and each of the other 43 vertices j, form the nine degree-at-most-five polynomials

```text
B_ab(t) = [4W(t)p_i,a(t)-M_a(t)] [p_j,b(t)-p_i,b(t)].
```

Let b_ab,k be their degree-five Bernstein coefficients. For ε=1/64, every one of the 86 root/vertex pairs satisfies, coefficient by coefficient,

```text
Σ_a b_aa,k + ε Σ_{a,b}|b_ab,k| ≤ 0,
```

with at least one strict coefficient for each pair. All Bernstein basis functions are positive on 0<t<1. Therefore

```text
(p_i-g)ᵀ G (p_j-p_i) < 0
```

for every other vertex j. This is a direct strict supporting-cone test for U, not a bar-depth surrogate. It explicitly includes the entire varying filled-volume moment.

The tested values ε=0,1/4096,1/1024,1/256,1/64 all passed. Each required exactly 86 polynomial checks and **no subdivision**. Endpoints L and R are deliberately excluded; no claim about strictness at their combinatorial degenerations is made.

Observed terminal markers:

```text
CAP_INTERVAL_GRAM_U2_PASS {'denominator': 0, 'leaves': 86, 'maxdepth': 0}
CAP_INTERVAL_GRAM_U2_PASS {'denominator': 4096, 'leaves': 86, 'maxdepth': 0}
CAP_INTERVAL_GRAM_U2_PASS {'denominator': 1024, 'leaves': 86, 'maxdepth': 0}
CAP_INTERVAL_GRAM_U2_PASS {'denominator': 256, 'leaves': 86, 'maxdepth': 0}
CAP_INTERVAL_GRAM_U2_PASS {'denominator': 64, 'leaves': 86, 'maxdepth': 0}
CAP_INTERVAL_CERTIFICATE 13182 a59e30af2a752c683f5022942be3e0fa80073ad6e9c78b965b876a48cc145d42
```

This enhanced 13182-byte certificate includes the crossed-edge completeness check and supersedes the earlier, smaller certificate generated before that check was added.

## 3. Exhaustive finite support-deletion obstruction

A separate executed family deletes any nonempty subset of the actual H24 input rows

```text
D = [0,2,3,6,9,15,23].
```

This is the seven-row block comprising the original two U stars and saddle carriers. The remaining plane positions and normals are held fixed; the actual homogeneous centre is not.

**All 127 members were reconstructed exactly and have at least two strict S at their own homogeneous centroid.** Their hulls are bounded. Thus none is own110. This conclusion does not rely on a numerical optimizer failing to find a cancellation.

For every member the certificate stores actual V/E/F, rational volume, first moment and centroid, all directly detected strict S, and at least two actual stable facet polygons. Since every member has at most 23 maximal facets, its actual E is at most 63 by the three-dimensional polytope inequalities. These are low-complexity negative controls.

Verification scope is important: this family certificate proves a sufficient **S≥2** obstruction. It is not a complete U/H/weak/P/Q census of all 127 members. The seven cap endpoints in Section 1 do have that complete census.

Observed:

```text
FINITE_STAR_DELETION_EXACT_NO110_PASS R3_HBRIDGE_S1_G3 127 2 906248 5b9584228c0f882567558ce9b4df825579b3239c12256e79ca6e5973eb4d4bc9
```

The analogous H44 block `[2,6,9,15,26,40,41]` was explored, but its complete exact batch did not finish with a retained aggregate certificate. No exact 127-member H44 exclusion is claimed. The optional command in the source is an uncompleted continuation, not an observed result.

## 4. What these results change

The new cap result distinguishes access from cancellation particularly sharply. One plane accesses and removes the entire P17 material component, stays at E66, removes the old junior U, and changes the actual centroid by order one. Nevertheless, a new cap-root persists throughout the whole separating interval and a nontrivial metric neighborhood. Further offset tuning inside this family is now excluded exactly, not merely discouraged by a finite search.

Likewise, deleting only subsets of the seven inherited star/saddle supports creates at least two stable equilibria throughout the executed finite family. This is not a theorem against moving those planes, rotating them, replacing them by a different coupled set, or changing other material.

A concrete next finite freedom is the replacement-root junction **input rows [18,19,24]**, together with whatever complementary material must move to control S. Rows18/19 were not in the seven-row deletion block. Jointly moving or rotating this junction leaves the certified fixed-parent/fixed-normal cap family. Moving other parent supports to alter the bulk moment is another legitimate way to leave it; the certificate does not prove that star motion is the only possible escape. Neither the elder identity nor the inherited stable carrier needs to be preserved.

There is ample actual budget: the cap controls use E66, leaving 183 edges below E249. This headroom is useful only if the new supports change the mechanical architecture, rather than reconstructing another member of the excluded family.

### A correction about empty auxiliary diagrams

For the exact radial graph used by the literal parent auditor—true vertices, true edges, vertex value ||p_i-g||², and edge value equal to the minimum squared radius along that edge—two strict U necessarily imply at least one strictly positive finite P bar. At a strict U, the radial derivative into every incident edge is negative, so every incident edge enters the superlevel graph strictly below that vertex's birth level. Its component therefore persists positively before merging. At most one component is essential; with two such vertices, at least one finite positive bar remains. Equal birth levels do not change this argument.

This argument needs no simple-vertex assumption. Therefore the summary's alleged own121/P0/Q0 observation cannot establish a failure of this exact graph on non-simple vertices. It may concern a different auxiliary graph or faulty reconstruction, but its purported body and code are unavailable here. Direct maximal-face/true-edge mechanics remain the acceptance criterion; no empty auxiliary diagram is promoted to an own110 certificate.

## 5. Recovery capsule and verification status

The following is a **complete additive source patch to the supplied literal parent capsule**, not a dependency on the missing G45 bundle. It uses only the two unchanged modules `exact_h.py` and `exact_poly.py` that are fully embedded in that parent. The exact H24 input is also repeated below. No optimizer, floating checkpoint, external library or unprovided historical input is required.

Parent source identity:

```text
RECOVER_W49.py
51501 bytes
SHA256 ec89b9ef3b7daeb409a6bd1ed2cecfd2592b2b6c5435f60e7507c92c0026d670

Decoded parent source dictionary:
151541 bytes
SHA256 216c04b45a65fdf0791ea06cabae5edcdf6c8f9a833ffc8c0c648b8141b71dfb
60 files

Unchanged exact_poly.py:
6134 bytes
SHA256 898f77989193886996d6f2dc121ccdfdf611b8a9ac52fd3207557eac6a69c0c4
```

The parent dictionary digest binds the exact `exact_h.py` dependency as well. Its hull engine exhausts rational plane triples, reconstructs maximal polygonal facets and true edges, proves boundedness, and integrates the actual filled body. This continuation uses that one full exact hull engine. The polynomial mass comparisons are supplementary checks, not a claim of two independent hull implementations. The parent describes this auditor and its strict/weak conventions explicitly. 

Completed exact executions used **CPython 3.13.5, standard library only**. The source below combines the completed source units without changing their calculations. The receipts are of the observed generated data, not a claimed byte identity or an additional cold execution of this presentation wrapper. Runtime resets did not preserve the unaccepted floating optimization pins; none is promoted to a durable successor.

Save the code as `W50_PATCH.py` inside the recovered parent source directory. Commands:

```sh
python -B -S RECOVER_W49.py W49_SOURCE
cd W49_SOURCE
python -B -S W50_PATCH.py caps
python -B -S W50_PATCH.py interval
python -B -S W50_PATCH.py delete-h24
python -B -S W50_PATCH.py receipts
```

The first three scientific commands reproduce the completed computations. The final command checks all listed byte/hash receipts. `delete-h44` is optional and has **no completed aggregate result claimed here**.

### Complete runnable patch

```python
# W50_PATCH.py
# Exact additive patch to the literal W49 parent source dictionary
# SHA256 216c04b45a65fdf0791ea06cabae5edcdf6c8f9a833ffc8c0c648b8141b71dfb.
# Requires its unchanged exact_h.py and exact_poly.py; Python stdlib only.
import json
import hashlib
import sys
from pathlib import Path
from fractions import Fraction as F
from math import comb
from exact_h import hull_h, audit_h, dot, cross, sub, neg

H24 = [
 [-754,596,-826,1000],[-853,1454,-237,1000],
 [-624,235,-911,1000],[-843,1043,-595,1000],
 [-729,1915,472,1000],[-612,2025,98,1000],
 [-221,-694,-1011,1000],[-260,921,-1181,1000],
 [101,-548,-937,1000],[-211,1301,-1116,1000],
 [-552,2046,997,1000],[-384,2123,-267,1000],
 [-265,1914,-694,1000],[249,-1378,-625,1000],
 [92,-867,-1106,1000],[794,-2056,714,1000],
 [-268,2239,-150,1000],[-392,2067,1304,1000],
 [-299,2014,1499,1000],[167,1596,2401,1000],
 [517,822,2784,1000],[757,-11,2758,1000],
 [888,-775,2419,1000],[915,-1438,1812,1000]
]
PARENT = 'R3_HBRIDGE_S1_G3'
TARGET = [18,23,26,30,31,32,33,34,35,36,37,38,39,40,41,42,43]
NORMAL = (1000,-144,-720)

def encode(x):
 return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()

def parent():
 r = dict(name=PARENT,halfspaces=H24)
 # This independently binds the literal rows, their order and cap convention
 # to an observed exact endpoint input receipt.
 z = dict(name='H24_CAP_-16',halfspaces=H24+[[*NORMAL,-16]])
 b = encode(z)
 assert len(b)==574
 assert hashlib.sha256(b).hexdigest()==(
  'c2e66f1a954bbba175f509154e1edf0dab2ee40d7cd203351acfddebfd498008')
 return r

def caps():
 r=parent();a=audit_h(r)
 P=[tuple(F(x) for x in p) for p in a['points']]
 T=a['P_bars'][0]['component']
 C=[i for i in range(len(P)) if i not in T]
 n=NORMAL
 lo=max(dot(P[i],n) for i in C)
 hi=min(dot(P[i],n) for i in T)
 assert T==TARGET
 assert lo==F(-6821960000,154504117)
 assert hi==F(454940000,37147643)
 print('H24_PACKET_SEPARATION',str(lo),str(hi),flush=True)
 for hh in [-40,-30,-20,-16,-10,0,10]:
  assert lo<hh<hi
  z=dict(name='H24_CAP_'+str(hh),halfspaces=r['halfspaces']+[[*n,hh]])
  aa=audit_h(z)
  assert (aa['V'],aa['E'],aa['F'])==(44,66,24)
  assert aa['strict']==[10,2,10]
  assert aa['additional_weak']==aa['primitive_zero']==[0,0,0]
  assert len(aa['P_bars'])==1 and len(aa['Q_bars'])==9
  newpoints={tuple(F(x) for x in p) for p in aa['points']}
  assert [i for i,p in enumerate(P) if p not in newpoints]==T
  assert len(newpoints-set(P))==17
  ib=encode(z)
  aa['input_sha256']=hashlib.sha256(ib).hexdigest()
  ab=encode(aa)
  Path(z['name']+'.json').write_bytes(ib)
  Path(z['name']+'_AUDIT.json').write_bytes(ab)
  print('H24_WHOLE_P17_EXACT_CAP_PASS',hh,len(ib),
        hashlib.sha256(ib).hexdigest(),len(ab),
        hashlib.sha256(ab).hexdigest(),flush=True)

# Rational polynomial helpers. Coefficients are in increasing power order.
def trim(a):
 while len(a)>1 and a[-1]==0:
  a.pop()
 return a

def add(a,b):
 c=[F(0)]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,x in enumerate(b):c[i]+=x
 return trim(c)

def pneg(a):
 return [-x for x in a]

def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return trim(c)

def scale(a,c):
 return [x*c for x in a]

def pdot(a,b):
 z=[F(0)]
 for x,y in zip(a,b):z=add(z,mul(x,y))
 return z

def pcross(a,b):
 return [
  add(mul(a[1],b[2]),pneg(mul(a[2],b[1]))),
  add(mul(a[2],b[0]),pneg(mul(a[0],b[2]))),
  add(mul(a[0],b[1]),pneg(mul(a[1],b[0])))
 ]

def peval(a,t):
 z=F(0)
 for x in reversed(a):z=z*t+x
 return z

def bern(a,n):
 assert len(a)<=n+1
 return [sum((a[j]*F(comb(k,j),comb(n,j))
              for j in range(min(k,len(a)-1)+1)),F(0))
         for k in range(n+1)]

def split(a):
 lo=[a[0]];hi=[a[-1]]
 while len(a)>1:
  a=[(x+y)/2 for x,y in zip(a,a[1:])]
  lo.append(a[0]);hi.append(a[-1])
 return lo,list(reversed(hi))

def solve(rows):
 a,b,c=rows
 bc=cross(b[:3],c[:3]);ca=cross(c[:3],a[:3]);ab=cross(a[:3],b[:3])
 d=dot(a[:3],bc)
 assert d
 return tuple(F(a[3]*bc[k]+b[3]*ca[k]+c[3]*ab[k],d)
              for k in range(3))

def check_bank(bank,eps,depth=0):
 upper=[sum(bank[a*3+a][k] for a in range(3))
        +eps*sum(abs(row[k]) for row in bank)
        for k in range(len(bank[0]))]
 if max(upper)<=0 and min(upper)<0:
  return 1,depth
 if depth==24:
  raise ArithmeticError('BERNSTEIN_UNCERTIFIED')
 both=[split(row) for row in bank]
 a=check_bank([z[0] for z in both],eps,depth+1)
 b=check_bank([z[1] for z in both],eps,depth+1)
 return a[0]+b[0],max(a[1],b[1])

def interval():
 raw=parent()
 p0,f0,e0,_=hull_h(raw)
 a=audit_h(raw)
 T=set(a['P_bars'][0]['component'])
 assert T==set(TARGET)
 n=NORMAL
 L=max(dot(n,v) for i,v in enumerate(p0) if i not in T)
 R=min(dot(n,p0[i]) for i in T)
 assert L<R
 mid=dict(name='H24_CAP_-16',halfspaces=raw['halfspaces']+[[*n,-16]])
 p,facets,edges,rows=hull_h(mid)
 polys=[];signature=[]
 for v in p:
  inc=[i for i,row in enumerate(mid['halfspaces'])
       if dot(row[:3],v)==row[3]]
  assert len(inc)==3
  ids=tuple(inc)
  rr=[[F(x) for x in mid['halfspaces'][i]] for i in ids]
  for j,i in enumerate(ids):
   if i==len(raw['halfspaces']):rr[j][3]=L
  pL=solve(rr)
  for j,i in enumerate(ids):
   if i==len(raw['halfspaces']):rr[j][3]=R
  pR=solve(rr)
  polys.append([[x,y-x] for x,y in zip(pL,pR)])
  signature.append(ids)

 # Complete clipped-vertex recipe, not just feasible candidate points.
 crossed=[(i,j) for i,j in e0 if (i in T)!=(j in T)]
 assert len(crossed)==17 and len(p0)-len(T)==27
 clip_polys=[[[v,F(0)] for v in p0[i]]
             for i in range(len(p0)) if i not in T]
 for i,j in crossed:
  d=sub(p0[j],p0[i]);den=dot(n,d)
  t0=(L-dot(n,p0[i]))/den;t1=(R-dot(n,p0[i]))/den
  clip_polys.append([[p0[i][k]+t0*d[k],(t1-t0)*d[k]]
                     for k in range(3)])
 key=lambda z:tuple(tuple(row) for row in z)
 assert sorted(map(key,clip_polys))==sorted(map(key,polys))
 for pp in polys:
  for ti,hh in [(F(0),L),(F(1),R)]:
   v=tuple(peval(x,ti) for x in pp)
   assert all(dot(row[:3],v)<=row[3] for row in raw['halfspaces'])
   assert dot(n,v)<=hh

 W=[F(0)];M=[[F(0)] for _ in range(3)]
 for ring,_,_ in facets:
  for k in range(1,len(ring)-1):
   x,y,z=[polys[i] for i in [ring[0],ring[k],ring[k+1]]]
   det=pdot(x,pcross(y,z));W=add(W,det)
   M=[add(M[j],mul(det,add(add(x[j],y[j]),z[j])))
      for j in range(3)]
 assert min(bern(W,3))>0
 for h in [-40,-16,10]:
  aa=audit_h(dict(name='check',halfspaces=raw['halfspaces']+[[*n,h]]))
  t=(F(h)-L)/(R-L)
  assert F(aa['volume'])==peval(W,t)/6
  assert [F(x) for x in aa['centroid']]==[
   peval(m,t)/(4*peval(W,t)) for m in M]
 roots=audit_h(mid)['U']
 assert roots==[0,39]
 banks=[]
 for i in roots:
  Y=[add(scale(mul(W,x),4),pneg(mm))
     for x,mm in zip(polys[i],M)]
  for j in range(len(p)):
   if j==i:continue
   d=[add(x,pneg(y)) for x,y in zip(polys[j],polys[i])]
   banks.append([bern(mul(Y[a],d[b]),5)
                 for a in range(3) for b in range(3)])
 receipts=[]
 for denom in [0,4096,1024,256,64]:
  eps=F(1,denom) if denom else F(0)
  checks=[check_bank(bank,eps) for bank in banks]
  rec=dict(denominator=denom,leaves=sum(x[0] for x in checks),
           maxdepth=max(x[1] for x in checks))
  receipts.append(rec)
  assert rec['leaves']==86 and rec['maxdepth']==0
  print('CAP_INTERVAL_GRAM_U2_PASS',rec,flush=True)
 out=dict(parent=PARENT,normal=n,offset_interval=list(map(str,[L,R])),
          roots=roots,root_supports=[signature[i] for i in roots],
          crossed_parent_edges=crossed,V6=list(map(str,W)),
          M24=[[str(x) for x in m] for m in M],
          inequalities=len(banks),receipts=receipts)
 data=encode(out)
 Path('CAP_INTERVAL_CERTIFICATE.json').write_bytes(data)
 print('CAP_INTERVAL_CERTIFICATE',len(data),
       hashlib.sha256(data).hexdigest(),flush=True)

# Exact stable witnesses for finite deletion families.
# This is deliberately not advertised as a full mechanical audit per member.
def stable_certificate(raw,need):
 p,facets,edges,rows=hull_h(raw)
 W=F(0);M=[F(0)]*3
 for ring,n,h in facets:
  for k in range(1,len(ring)-1):
   a,b,c=[p[i] for i in [ring[0],ring[k],ring[k+1]]]
   d=dot(a,cross(b,c));W+=d
   for j in range(3):M[j]+=d*(a[j]+b[j]+c[j])
 assert W>0
 g=tuple(m/(4*W) for m in M)
 assert all(dot(n[:3],g)<n[3] for n in rows)
 Y=[sub(v,g) for v in p]
 S=[]
 for k,(ring,n,h) in enumerate(facets):
  vals=[dot(cross(n,sub(p[j],p[i])),neg(Y[i]))
        for i,j in zip(ring,ring[1:]+ring[:1])]
  if min(vals)>0:S.append(k)
 assert len(S)>=need
 return dict(V=len(p),E=len(edges),F=len(facets),volume=str(W/6),
             centroid=list(map(str,g)),
             first_moment=[str(m/24) for m in M],S=S,
             witnesses=[facets[k][0] for k in S[:need]])

def deletions(which):
 if which=='h24':
  name=PARENT;raw=parent();block=[0,2,3,6,9,15,23];need=2
 elif which=='h44':
  # No completed aggregate receipt is claimed for this optional branch.
  name='R3_H44_GROWN_S1_G6'
  raw=json.loads(Path(name+'.json').read_text())
  block=[2,6,9,15,26,40,41];need=3
 else:
  raise ValueError(which)
 ledger=[]
 for mask in range(1,128):
  gone=[i for k,i in enumerate(block) if mask>>k&1]
  z=dict(name=name+'_DELETE_'+str(mask),
         halfspaces=[row for i,row in enumerate(raw['halfspaces'])
                     if i not in gone])
  a=stable_certificate(z,need)
  a.update(mask=mask,removed=gone);ledger.append(a)
 data=encode(ledger)
 Path(name+'_DELETE_CERTIFICATE.json').write_bytes(data)
 print('FINITE_STAR_DELETION_EXACT_NO110_PASS',name,127,
       min(len(a['S']) for a in ledger),len(data),
       hashlib.sha256(data).hexdigest(),flush=True)

# Observed exact input and complete-audit receipts, ordered by cap height.
CAP_RECEIPTS = [
 (-40,574,'86ae3a556a32ff978b60c4c9bb85d74473ecdf51280dabfb32ed492d9501af3e',
  90076,'ca312ccafcec523a45144a120a2c0285fab18d6c978ade32a35501c43b41e9a1'),
 (-30,574,'7fcf057c1bb89a96e76c67a5c96b311ef97726ea76a8629a122cdf5999be278d',
  90302,'63c59b8e480d528ead6b49465ee367df28a084c684cbcc166fd3a74f1403bc4f'),
 (-20,574,'6d8a516724e9659d00b630387bbba06fcaa460942c8e9fbeae756b1e4175a285',
  90296,'d9c17eb68546a7c02ac30626a3cf32ade8983a278daa28aa92e7819e6ee19f4a'),
 (-16,574,'c2e66f1a954bbba175f509154e1edf0dab2ee40d7cd203351acfddebfd498008',
  90291,'146f16618b5cf310053409764edf4afc7604d6ad2adf67af2beb9ae71c9df0d6'),
 (-10,574,'00dab0705fa557e68ea2376c11256b684ab307092431fb021d4dc0beb6264e9a',
  90467,'9826a969f4b02b2032e54f7f574efc0c330818bf14652aec243ca773e2fcc2a8'),
 (0,570,'be4f76bcb0d89af535aaa19857d4358ca5364c5fb9c109c1d9d3bccc22e6326b',
  88940,'5c1ce31f42cf16e1a2dccc5ac2b41007b498706055c9bd27d0d2cf00e34ef11e'),
 (10,572,'d338a7899cb90a55f0104197ae92d85df299b8c11a551d5638bbb0d04a58d504',
  90463,'1c38568cc94f10f0154f83ec28f6dd0f42c5407b29b17b06b98171183f4e9296')
]

def verify_receipts():
 items=[]
 for h,nb,sha,ab,ash in CAP_RECEIPTS:
  stem='H24_CAP_'+str(h)
  items.extend([(stem+'.json',nb,sha),(stem+'_AUDIT.json',ab,ash)])
 items.extend([
  ('CAP_INTERVAL_CERTIFICATE.json',13182,
   'a59e30af2a752c683f5022942be3e0fa80073ad6e9c78b965b876a48cc145d42'),
  (PARENT+'_DELETE_CERTIFICATE.json',906248,
   '5b9584228c0f882567558ce9b4df825579b3239c12256e79ca6e5973eb4d4bc9')
 ])
 for name,size,sha in items:
  b=Path(name).read_bytes()
  assert len(b)==size,(name,'byte count',len(b),size)
  assert hashlib.sha256(b).hexdigest()==sha,(name,'SHA256')
  print('W50_RECEIPT_MATCH',name,size,sha,flush=True)
 print('W50_ALL_LISTED_RECEIPTS_MATCH',len(items),flush=True)

def main():
 if len(sys.argv)!=2:
  raise SystemExit('usage: W50_PATCH.py caps|interval|delete-h24|receipts|delete-h44')
 action=sys.argv[1]
 if action=='caps':caps()
 elif action=='interval':interval()
 elif action=='delete-h24':deletions('h24')
 elif action=='delete-h44':deletions('h44')
 elif action=='receipts':verify_receipts()
 else:raise SystemExit('unknown action: '+action)

if __name__=='__main__':
 main()
```

## Continuation status

The durable new objects are the seven literal cap recipes and their full audits. The durable mathematical results are the all-offset/metric-box U≥2 certificate and the 127-member exact S≥2 deletion certificate. The most useful constructive departure is a replacement of the actual new cap-root junction or a different coupled material family, not another offset inside the proven interval.

The requested G45-derived H44/H45 objects remain missing exact dependencies. Their recovery input and claimed general auditor must be supplied before their labels, star geometry or auxiliary-diagram anomaly can be used. The actual parent H44/H24 controls, the new finite cap bodies, and the exact methods above remain available without them.
