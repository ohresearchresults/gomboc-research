# figure-0538

AI research report · 2026-09-24 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# W52 — exact finite moment-preserving joint-star reconstruction; execution unverified

## Status

**There is no newly verified endpoint and no own110 claim from this continuation.** The current journal and literal W51 parent were read through EOF in the preceding attempt. During this continuation, the runtime inventory, extraction, preparation and scientific-run calls did not yield inspectable tool returns. I therefore cannot establish whether the submitted computation completed, and I report neither new equilibrium counts nor new byte/hash receipts as observed. This is a limitation of the available execution evidence, not evidence that an input file is absent and not a mathematical obstruction.

The work below is a complete additive research patch implementing a finite actual-material family. Its finite volume/first-moment identities are proved here. Its pack selection, endpoint construction and exact audits remain **unverified executions**. The last accepted computational checkpoints remain those in literal W51.

The controlling parent is `figure-0537`, SHA-256 `05577e4a0b36b334bf63e1fd41ffdbb8b9c663892f7da776c851bf47acf7af21`. No withdrawn G45/H45 aliases were used.

## Why I selected the small W51 geometry

I selected **W51_ROBUST_G3** for a material construction, not for the affine-metric investigation being pursued separately by the coordinator. The literal parent gives its actual V31/E87/F58, C174, own211, additionalweak000, primitivezero000, P0/Q1. Its32-row input has common denominator1000; input row3 is interior. Its remaining Q bar is deeper than that of H48, so this selection is an arithmetic and parameterization choice, not a claim of superiority on persistence depth.

The two actual stable triangles, expressed in the original32-row input numbering rather than a new H-auditor numbering, are

```text
elder:  [31,30,4]
junior: [30,10,29].
```

The actual saddle edge has input endpoints `[2,5]`. The old unique U is input row0. Thus moving a junior-only vertex, input10 or29, together with one saddle endpoint, input2 or5, changes the relevant physical carriers. These are coordinate-identified carriers from the literal W51 result; the code additionally reconstructs and checks those incidences.

The reason to use this simplicial body rather than triangulate H48's polygonal faces is substantive: independent vertex stars in a genuinely simplicial maximal complex admit an exact finite moment formula. Treating fan diagonals of H48 as physical edges would not justify the same construction.

## The finite material construction

Let P have its actual outward-oriented triangular maximal facets. Choose k pairwise nonadjacent actual vertices. No facet then contains two selected vertices. All unselected vertices stay fixed; selected vertex i moves from v_i to v_i+d_i.

For each incident facet, cyclically rotate its outward vertex order to `(v_i,b,c)`. Define

```text
A_i = Σ (b×c),
B_i = Σ (b+c)(b×c)^T,
L_i = (A_i·v_i) I + B_i,
```

where each sum is over the actual incident maximal facets.

Use the homogeneous integration numerators

```text
W = 6 Volume(P),
T = 24 ∫_P x dx.
```

The selected star contributes

```text
W_i(v) = A_i·v,
T_i(v) = (A_i·v)v + B_i v.
```

Consequently its exact finite changes are

```text
ΔW_i = A_i·d_i,
ΔT_i = L_i d_i + (A_i·d_i)v_i + (A_i·d_i)d_i.
```

Impose the rational linear equations

```text
A_i·d_i = 0                   for every selected star i,
Σ L_i d_i = 0.
```

Then **both actual volume and first moment are exactly unchanged**, for finite displacements, provided the deformed maximal complex remains the actual boundary. This is not merely cancellation of the differential of the centroid. In particular, imposing only the first-order total moment equations without the individual `A_i·d_i=0` equations would leave quadratic terms; the patch does not make that substitution.

There are at most k+3 independent equations in3k displacement coordinates. For an accepted five-star pack the nullspace therefore has dimension at least7. The implementation constructs the exact rational matrix and nullspace, verifies that the junior and saddle blocks can both move, and selects deterministic joint directions. It first tries to keep the elder triangle fixed, but permits its release if that guard prevents a compatible pack. The old root coordinate is held fixed in this particular family, but its incident facets may change and its U status is not prescribed.

This uses the independent-star moment mechanism already present in the broader notebook; I am not presenting that general mechanism as a new discovery. The contribution here is an explicit input-specific joint-carrier formulation, a complete exact implementation, and a finite geometric-domain check instead of a local mass-Jacobian approximation.

### It is actual material geometry, not a reference-centre substitution

The inherited exact mass is

```text
V0 = 10865185711/1500000000
M0 = (-386613615871/1500000000000,
      -3857015486057/3000000000000,
       57133873364297/24000000000000)
g0 = M0/V0.
```

These are the literal W51_ROBUST_G3 mass data. The patch proves the finite polynomial identities for the selected displacements and independently reintegrates every sampled boundary. Each retained endpoint is then reconstructed by the complete H auditor and required to have volume V0 and centroid g0. Thus evaluating mechanics at g0 is justified only after verifying that it is still the actual homogeneous centroid.

The patch also finds four affinely independent fixed vertices. A nonzero motion of the selected vertices cannot be a single global affine deformation of this marked vertex configuration: an affine map fixing those four points is the identity. This is therefore a different local material freedom from varying one global affine metric.

## Finite scope of the proposed computation

For a chosen joint direction, write every moving point as `p_i(t)=p_i+t d_i`. Because each actual triangle contains at most one moving vertex, its oriented normal is affine in t. Every all-point supporting inequality is therefore a polynomial of degree at most two.

The implementation checks positivity over the **whole segment** `[0,t]`, including the interior minimum of every convex quadratic. It brackets the first failure of the original strict maximal-facet chart and bisects that bracket with rational arithmetic. Checking the whole segment matters: checking only a sequence of endpoint values could miss an earlier contact followed by re-entry.

The default finite screen uses five selected stars, up to12 deterministic signed directions,16 rational samples per direction, and32 bisections of each first-contact bracket. There is no random seed, floating tolerance, or bar-depth objective. It retains representatives of each exact S/U/closed-weak-S/U outcome, every S1/U1 screen candidate, and the largest-displacement sampled own-S2/U1 candidate. Every retained representative receives the full actual-hull S/U/H strict and closed-weak audit and all positive P/Q data.

This is **not an interval-complete equilibrium atlas**. Even a completed run with no target would exclude only its explicitly sampled finite set, not all parameters of these linear material spaces. Crossing a hull contact and constructing a new compatible star chart is also outside this version. No pack size, rank, chart width, sampled census, target absence, or target success is reported as observed here.

## Recovery dependency and commands

This is an additive patch to the **complete literal W51 capsule**, not a dependency on a current sandbox. It needs only the unchanged `exact_h.py` and its `exact_poly.py` dependency from that capsule. The32-row geometric input is repeated in full below.

The parent recovery identities are:

```text
RECOVER_W51.py: 61061 bytes
SHA256 9cad65f5688d803d536d995be50f2ae475c7d53d5791f960a72b027f9dbfb577

Decoded W51 source dictionary: 171845 bytes,82 files
SHA256 ce7c3f1ad9ce6d5696792ac9fd6ad791c37c39dbb5442783e9413477c1eea559
```

The specified exact environment is CPython3.13.5 and the standard library. No NumPy, SciPy, Torch, optimizer checkpoint or external source is needed for this patch. Current runtime versions were not inspectably confirmed.

Save the complete code below as `W52_MASS_RAIL.py` in the recovered W51 directory:

```sh
python -B -S RECOVER_W51.py W51_SOURCE
cd W51_SOURCE
python -B -S W52_MASS_RAIL.py --prepare-only --stars 5 --rays 12 --samples 16 --bits 32 --out W52_PREPARE
python -B -S W52_MASS_RAIL.py --stars 5 --rays 12 --samples 16 --bits 32 --out W52_RAIL
```

The program computes and records its own source byte count/hash, the exact matrix, nullspace, selected stars, every direction, each rational parameter and first-contact bracket. It writes complete rational H inputs, full audits and byte/hash receipts for retained endpoints. A fresh continuation should preserve those outputs only after inspecting the actual run and verification results.

These marker names are **programmed conditions, not observed receipts from this continuation**:

```text
W52_EXACT_MASS_RAIL_PREPARED
W52_EXACT_FINITE_RAY_SCREEN
W52_EXACT_RAIL_ENDPOINT
W52_FINITE_MATERIAL_RAIL_RUN_COMPLETE
```

`W52_EXACT_OWN110_WITH_NO_ADDITIONAL_WEAK` is emitted only after the full auditor returns strict110, additionalweak000 and no positive P or Q bars. Its presence is not claimed.

## Complete source unit

```python
"""Exact finite isovolumetric, isocentroid material rails for W51_ROBUST_G3.
Additive patch to the literal W51 capsule. Requires only its exact_h.py
(and that module's unchanged exact_poly.py dependency), plus Python stdlib.
No floating arithmetic is used to accept a body or choose a parameter.
"""
import argparse, hashlib, itertools, json, sys
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path
from exact_h import hull_h, audit_h
if hasattr(sys, 'set_int_max_str_digits'): sys.set_int_max_str_digits(0)

INPUT = [
 [-2678,-1136,975],[-2745,-769,406],[-2212,-627,45],[96,-637,-245],
 [465,1184,-402],[80,119,-1160],[294,781,-935],[157,537,-1075],
 [311,1098,-580],[681,814,-815],[565,-379,-1032],[883,11,-962],
 [947,461,-856],[1007,793,-634],[840,1037,-473],[1206,848,-369],
 [1174,1065,103],[1389,818,-95],[1535,736,189],[1603,668,465],
 [1571,172,-108],[1639,563,721],[1644,425,972],[1609,244,1244],
 [1506,4,1547],[1301,-295,1859],[970,-604,2131],[548,-896,2304],
 [78,-1126,2365],[-418,-1288,2323],[-968,-1386,2170],[-1604,-1391,1853]
]
PARENT = 'figure-0537'
PARENT_SHA = '05577e4a0b36b334bf63e1fd41ffdbb8b9c663892f7da776c851bf47acf7af21'
V0 = F(10865185711,1500000000)
M0 = (F(-386613615871,1500000000000),
      F(-3857015486057,3000000000000),
      F(57133873364297,24000000000000))
G0 = tuple(x/V0 for x in M0)
Z = (F(0),F(0),F(0))

def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(a,t): return tuple(x*t for x in a)
def cross(a,b):
 return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def enc(a): return (json.dumps(a,sort_keys=True,separators=(',',':'))+'\n').encode()
def strings(a):
 if isinstance(a,F): return str(a)
 if isinstance(a,(list,tuple)): return [strings(x) for x in a]
 if isinstance(a,dict): return {k:strings(v) for k,v in a.items()}
 return a

def write(out,name,data):
 b=enc(strings(data));(out/name).write_bytes(b)
 return dict(file=name,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())

def integral_row(row):
 row=[F(x) for x in row];D=lcm(*(x.denominator for x in row))
 v=[int(x*D) for x in row];d=gcd(*v)
 assert d>0
 return tuple(x//d for x in v)

def supports(P):
 ans=set()
 for ia,ib,ic in itertools.combinations(range(len(P)),3):
  a,b,c=P[ia],P[ib],P[ic];n=cross(sub(b,a),sub(c,a))
  if n==Z: continue
  h=dot(n,a);v=[dot(n,x)-h for x in P]
  if min(v)<0<max(v): continue
  if min(v)==max(v)==0: continue
  if max(v)>0:n=mul(n,-1);h=-h
  ans.add(integral_row((*n,h)))
 assert len(ans)>=4
 return sorted(ans)

def mass(P,faces):
 W=F(0);T=[F(0)]*3
 for face in faces:
  assert len(face)==3
  a,b,c=[P[i] for i in face];d=det(a,b,c);W+=d
  for k in range(3):T[k]+=d*(a[k]+b[k]+c[k])
 assert W>0
 return W/6,tuple(x/24 for x in T)

def nullspace(A):
 A=[list(map(F,r)) for r in A];m=len(A);n=len(A[0]);piv=[];r=0
 for c in range(n):
  q=next((q for q in range(r,m) if A[q][c]),None)
  if q is None:continue
  A[r],A[q]=A[q],A[r];s=A[r][c];A[r]=[v/s for v in A[r]]
  for q in range(m):
   if q!=r and A[q][c]:
    s=A[q][c];A[q]=[x-s*y for x,y in zip(A[q],A[r])]
  piv.append(c);r+=1
  if r==m:break
 ans=[]
 for j in range(n):
  if j in piv:continue
  v=[F(0)]*n;v[j]=F(1)
  for k,c in enumerate(piv):v[c]=-A[k][j]
  ans.append(v)
 assert all(all(dot(row,v)==0 for row in A) for v in ans)
 return ans,piv

def star_system(P,faces,active):
 k=len(active);R=[[F(0)]*(3*k) for _ in range(k+3)];parts=[]
 for j,i in enumerate(active):
  A=Z;B=[[F(0)]*3 for _ in range(3)]
  for f in faces:
   if i not in f:continue
   z=f.index(i);_,ib,ic=f[z:]+f[:z];b,c=P[ib],P[ic]
   r=cross(b,c);A=add(A,r)
   for a in range(3):
    for q in range(3):B[a][q]+=(b[a]+c[a])*r[q]
  assert A!=Z
  w=dot(A,P[i]);L=[[B[a][q]+(w if a==q else 0) for q in range(3)] for a in range(3)]
  for q in range(3):R[j][3*j+q]=A[q]
  for a in range(3):
   for q in range(3):R[k+a][3*j+q]=L[a][q]
  parts.append(dict(vertex=i,A=A,L=L))
 N,piv=nullspace(R)
 return R,N,piv,parts

def choose_pack(P,faces,edges,stars):
 bypoint={p:i for i,p in enumerate(P)}
 ip=lambda j:bypoint[tuple(F(v,1000) for v in INPUT[j])]
 elder={ip(j) for j in [31,30,4]};junior=[ip(10),ip(29)]
 saddle=[ip(2),ip(5)];root=ip(0)
 assert set([ip(30),ip(10),ip(29)]) in [set(f) for f in faces]
 assert elder in [set(f) for f in faces]
 assert tuple(sorted(saddle)) in edges
 def independent(q):
  return all(tuple(sorted(e)) not in edges for e in itertools.combinations(q,2))
 # Prefer holding the elder triangle fixed, but explicitly permit its release
 # if no compatible full-rank joint-star pack is available with that guard.
 for guard in [elder,set()]:
  pairs=[(a,b) for a in junior for b in saddle if independent([a,b])]
  for a,b in pairs:
   pool=[i for i in range(len(P)) if i not in guard|{root,a,b}
         and independent([a,b,i])]
   choices=[]
   for extra in itertools.combinations(pool,stars-2):
    q=(a,b)+extra
    if not independent(q):continue
    score=sum((dot(sub(P[i],P[j]),sub(P[i],P[j]))
               for i,j in itertools.combinations(q,2)),F(0))
    choices.append((score,q))
   choices.sort(key=lambda z:(-z[0],z[1]))
   for _,active in choices:
    R,N,piv,parts=star_system(P,faces,active)
    if not N:continue
    if any(not any(any(v[3*j+c] for c in range(3)) for v in N) for j in [0,1]):
     continue
    fixed=[i for i in range(len(P)) if i not in active]
    tetra=next((f for f in itertools.combinations(fixed,4)
                if det(sub(P[f[1]],P[f[0]]),sub(P[f[2]],P[f[0]]),sub(P[f[3]],P[f[0]]))),None)
    if tetra is None:continue
    assert all(len(set(f)&set(active))<=1 for f in faces)
    return list(active),R,N,piv,parts,list(tetra),sorted(guard)
 raise ArithmeticError('NO_JOINT_INDEPENDENT_STAR_PACK_WITH_REQUESTED_SIZE')

def directions(N,active,npoints,wanted):
 q=len(N);cand=list(N)
 # Nonzero coordinate projections are vector polynomials of degree <=q-1.
 # The finite integer set below suffices to avoid both identically nonzero
 # critical projections' roots, independently of rounding or random starts.
 for s in range(1,2*q+2):
  cand.append([sum((F(s**j)*N[j][i] for j in range(q)),F(0)) for i in range(len(N[0]))])
 ans=[];seen=set()
 for v in cand:
  if any(not any(v[3*j+c] for c in range(3)) for j in [0,1]):continue
  size=max(map(abs,v));v=tuple(x/size for x in v)
  for sign in [1,-1]:
   vv=tuple(sign*x for x in v)
   if vv in seen:continue
   seen.add(vv);d=[Z]*npoints
   for j,i in enumerate(active):d[i]=tuple(vv[3*j:3*j+3])
   ans.append(d)
   if len(ans)==wanted:return ans
 if not ans:raise ArithmeticError('NO_JOINT_RAY')
 return ans

def slack_polynomials(P,faces,d):
 ans=[]
 for f in faces:
  ia,ib,ic=f;a,b,c=[P[i] for i in f];da,db,dc=[d[i] for i in f]
  b0=sub(b,a);c0=sub(c,a);b1=sub(db,da);c1=sub(dc,da)
  n0=cross(b0,c0);n1=add(cross(b1,c0),cross(b0,c1))
  assert cross(b1,c1)==Z
  for j in range(len(P)):
   if j in f:continue
   v0=sub(a,P[j]);v1=sub(da,d[j])
   row=(dot(n0,v0),dot(n1,v0)+dot(n0,v1),dot(n1,v1))
   assert row[0]>0
   ans.append(row)
 return ans

def positive_segment(rows,t):
 for a,b,c in rows:
  if a+b*t+c*t*t<=0:return False
  if c>0:
   z=-b/(2*c)
   if 0<z<t and a+b*z+c*z*z<=0:return False
 return True

def chart_bound(rows,bits):
 lo=F(0);hi=F(1)
 for _ in range(64):
  if not positive_segment(rows,hi):break
  lo=hi;hi*=2
 else:raise ArithmeticError('GEOMETRY_BOUND_NOT_BRACKETED_WITHIN_2_TO_64')
 for _ in range(bits):
  mid=(lo+hi)/2
  if positive_segment(rows,mid):lo=mid
  else:hi=mid
 while lo==0:
  mid=hi/2
  if positive_segment(rows,mid):lo=mid
  else:hi=mid
 assert positive_segment(rows,lo) and not positive_segment(rows,hi)
 return lo,hi

def screen(P,faces,edges):
 S=[];U=[];Sw=[];Uw=[];sz=[];uz=[]
 for k,f in enumerate(faces):
  a,b,c=[P[i] for i in f];n=cross(sub(b,a),sub(c,a))
  vals=[dot(cross(n,sub(P[j],P[i])),sub(G0,P[i]))
        for i,j in zip(f,f[1:]+f[:1])]
  if min(vals)>0:S.append(k)
  elif min(vals)>=0:Sw.append(k)
  if 0 in vals:sz.append(k)
 for i in range(len(P)):
  js=[b if a==i else a for a,b in edges if i in (a,b)]
  vals=[dot(sub(P[i],G0),sub(P[j],P[i])) for j in js]
  if max(vals)<0:U.append(i)
  elif max(vals)<=0:Uw.append(i)
  if 0 in vals:uz.append(i)
 return dict(S=S,U=U,additional_weak_SU=[Sw,Uw],primitive_zero_SU=[sz,uz])

def endpoint(out,name,P,faces,expected):
 rows=[]
 for f in faces:
  a,b,c=[P[i] for i in f];n=cross(sub(b,a),sub(c,a))
  rows.append(integral_row((*n,dot(n,a))))
 raw=dict(name=name,halfspaces=[list(r) for r in rows])
 receipt=write(out,name+'.json',raw)
 a=audit_h(raw)
 assert (a['V'],a['E'],a['F'])==(31,87,58)
 assert set(tuple(F(x) for x in p) for p in a['points'])==set(P)
 assert F(a['volume'])==V0 and tuple(F(x) for x in a['centroid'])==G0
 assert a['strict'][:2]==[len(expected['S']),len(expected['U'])]
 assert a['additional_weak'][:2]==list(map(len,expected['additional_weak_SU']))
 a['input_sha256']=receipt['sha256']
 receipt2=write(out,name+'_AUDIT.json',a)
 print('W52_EXACT_RAIL_ENDPOINT',name,a['strict'],a['additional_weak'],
       a['primitive_zero'],len(a['P_bars']),len(a['Q_bars']),receipt,receipt2,flush=True)
 target=(a['strict']==[1,1,0] and a['additional_weak']==[0,0,0]
         and not a['P_bars'] and not a['Q_bars'])
 if target:print('W52_EXACT_OWN110_WITH_NO_ADDITIONAL_WEAK',name,flush=True)
 return dict(name=name,input=receipt,audit=receipt2,strict=a['strict'],
             additional_weak=a['additional_weak'],primitive_zero=a['primitive_zero'],
             P=len(a['P_bars']),Q=len(a['Q_bars']),target=target)

def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--out',default='W52_RAIL')
 ap.add_argument('--stars',type=int,default=5)
 ap.add_argument('--rays',type=int,default=12)
 ap.add_argument('--samples',type=int,default=16)
 ap.add_argument('--bits',type=int,default=32)
 ap.add_argument('--prepare-only',action='store_true')
 ar=ap.parse_args()
 assert 3<=ar.stars<=8 and ar.rays>0 and ar.samples>0 and ar.bits>=8
 out=Path(ar.out);out.mkdir(parents=True,exist_ok=True)
 rawpoints=[tuple(F(x,1000) for x in p) for p in INPUT]
 hp=dict(name='W52_PARENT_HCHECK',halfspaces=supports(rawpoints))
 P,ff,ee,_=hull_h(hp);P=list(P);faces=[list(f[0]) for f in ff];edges=set(ee)
 assert (len(P),len(edges),len(faces))==(31,87,58)
 assert all(len(f)==3 for f in faces)
 assert mass(P,faces)==(V0,M0)
 base=audit_h(hp)
 assert base['strict']==[2,1,1] and base['additional_weak']==base['primitive_zero']==[0,0,0]
 assert len(base['P_bars'])==0 and len(base['Q_bars'])==1
 active,R,N,piv,parts,tetra,guard=choose_pack(P,faces,edges,ar.stars)
 rays=directions(N,active,len(P),ar.rays)
 for d in rays:
  vv=[x for i in active for x in d[i]]
  assert all(dot(row,vv)==0 for row in R)
 code=Path(__file__).read_bytes()
 params=dict(version=1,parent=PARENT,parent_sha256=PARENT_SHA,
             source_bytes=len(code),source_sha256=hashlib.sha256(code).hexdigest(),
             literal_input=INPUT,denominator=1000,actual_parent_points=P,
             parent_faces=faces,parent_edges=sorted(edges),active=active,
             fixed_tetrahedron=tetra,fixed_elder_vertices=guard,
             linear_constraints=R,rank=len(piv),nullspace=N,star_parts=parts,
             directions=rays,volume=V0,first_moment=M0,centroid=G0,
             options=vars(ar))
 pr=write(out,'W52_PARAMETERS.json',params)
 print('W52_EXACT_MASS_RAIL_PREPARED',len(active),len(piv),len(N),len(rays),pr,flush=True)
 if ar.prepare_only:return
 ledger=[];representatives={};best211=None;target_screens=[]
 for ri,d in enumerate(rays):
  polys=slack_polynomials(P,faces,d);lo,hi=chart_bound(polys,ar.bits)
  for k in range(1,ar.samples+1):
   t=lo*F(k,ar.samples);PP=[add(p,mul(v,t)) for p,v in zip(P,d)]
   assert mass(PP,faces)==(V0,M0)
   s=screen(PP,faces,edges)
   rec=dict(ray=ri,sample=k,t=t,chart_lower=lo,chart_upper=hi,screen=s)
   ledger.append(rec)
   key=(len(s['S']),len(s['U']),*[len(x) for x in s['additional_weak_SU']])
   representatives.setdefault(key,(rec,PP))
   if key[:2]==(1,1):target_screens.append((rec,PP))
   if key==(2,1,0,0) and (best211 is None or t>best211[0]['t']):best211=(rec,PP)
  print('W52_EXACT_FINITE_RAY_SCREEN',ri,str(lo),str(hi),flush=True)
 selected=list(representatives.values())+target_screens
 if best211 is not None:selected.append(best211)
 done=set();audits=[]
 for rec,PP in selected:
  key=(rec['ray'],rec['sample'])
  if key in done:continue
  done.add(key);name='W52_RAIL_R%02d_K%02d'%key
  audits.append(endpoint(out,name,PP,faces,rec['screen']))
 summary=dict(parameters=pr,screen_status='exact S/U on certified fixed maximal-facet cells; full H/weak/PQ only for retained endpoints',
              samples=len(ledger),ledger=ledger,endpoints=audits)
 sr=write(out,'W52_FINITE_SCREEN.json',summary)
 print('W52_FINITE_MATERIAL_RAIL_RUN_COMPLETE',len(ledger),len(audits),
       sum(a['target'] for a in audits),sr,flush=True)

if __name__=='__main__':main()
```

## Handoff boundary and continuation

The finite moment identity is established algebraically; the default pack and its scientific outputs are not established by an observed execution. A failure to find a compatible pack would concern this prescribed independent-star choice, not arbitrary material reconstruction. A completed finite screen without110 would likewise not exclude its unsampled parameter space, another star pack, a contact-crossing continuation, H48 carrier replacement, or another architecture.

The next useful action is to obtain an inspectable preparation result, then the full retained-endpoint audits. The exact matrix and first-contact brackets would permit a continuation to replace a purely local centroid constraint with a finite mass-preserving material space. Until those results are actually read and verified, **W51_ROBUST_G3, W51_TREE_U1_G5 and W51_PRUNE_211 remain the durable numerical/exact entrances; no W52 successor should be entered as an accepted body.**
