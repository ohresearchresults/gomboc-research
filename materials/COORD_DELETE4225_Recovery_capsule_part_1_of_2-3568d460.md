# material-3568d4602e48

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# COORD_DELETE4225 — Recovery capsule part 1/2

Object identity: the complete finite family obtained by deleting exactly one or two literal vertices from NC57 C372_ALT_FULL_G4 or C378_ALT_POLY_G6, taking the convex hull of the unchanged surviving exact points, and recomputing the ordinary filled-solid centroid. Both parts of this capsule and the immutable NC57 input dependency are necessary. This is a new executed finite exclusion, not a global impossibility theorem or a new own110 winner. Canonical own110 remains C622.

## Exact input dependency
Accepted result figure-0398, 73935 bytes, SHA256 b6c84be62ea56d1c11575d4d6309563f525d734f79b0ad2a299f0b7abd2ccdd3, contains the complete standalone 37-file NC57 recovery capsule. It was read completely at cursors 0 and 50000 with unchanged SHA. Its literal decoder and all 37 source manifest entries were reconstructed and checked in this execution. Reconstruct its source and exact reports by the parent command `python -B -S RECOVER_NC57.py NC57_SOURCE 4`. The parent supplies every input byte, not merely hashes.

Required generated reports, with original exact point order unchanged:
- NC57_SOURCE/proof/C372_ALT_FULL_G4/REPORT.json: 14190 bytes, SHA256 639b7dd56caf48ee99f1175e20b1f305100dc0fb3f75440dd20aba8df57b4cb5. Parent V64/E186/F124, own211/weak000. Integer lattice denominator 660000.
- NC57_SOURCE/proof/C378_ALT_POLY_G6/REPORT.json: 18534 bytes, SHA256 fc46fb08252486d5c2474d70c6834b2f4849f8de25bcf18ccb059a7aa9ced661. Parent V65/E189/F126, own211/weak000. Integer lattice denominator 66000000.

All deletion indices here and in output are THESE report point rows, not earlier C384 ancestry, control coordinates, or the canonical C622 body. Rank starts at zero, singletons then lexicographic pairs. No seed, rounding, refitting, coordinate change, or hidden option.

## Observed result and evidence scope
All 2080 C372 cases and all 2145 C378 cases were successfully certified by A and independently reconstructed by B. Every shared field of every record matches: true V/E/F/C, stable face owner sets, unstable vertex indices, weak S/U, exact filled volume, exact reduced centroid, rank and deletion set. Every one has S>=2; there are no weak-only equilibria in B's complete S/U/H census. A does NOT compute H; B independently adds all four edge primitives and verifies S+U-H=2. Thus two independent exact hull/mass/stability methods establish the scoped exclusion, but this is not a claim that A independently checks H.

Exactly 21 C372 descendants and 45 C378 descendants have own211/weak000. Among the double deletions, 14 C372 descendants have V62/E180/F120,C360; 36 C378 descendants have V63/E183/F122,C366. They are useful exact nonwinners; their coordinates are completely defined by parent literal points and the CENSUS deletion rows. Both complete censuses, including every nonwinner, regenerate deterministically using this capsule. No assertion is made about three-or-more deletions, additions, continuous deformations, other parent coordinates, or global minimal complexity.

Prior numerical DELETE_CENSUS.py ([internal-source-reference]) was freshly executed for kmax2,start0,end0 on both inputs: tested2080/2145, errors0, no numericSU11. That gate is superseded by the independently reproducible exact evidence here and is not used as a proof. The old journals' unpreserved executions remain unpreserved; this is a genuinely new run.

## Recovery and verification
Save the following fenced source exactly as EXACT_DELETE.py, UTF-8, one final newline: 6704 bytes, SHA256 9f7e13e00a1d9eb6226360908a78e6efbbd3edc341b12275a4830817aec4b628. Part 2 supplies the independent B and whole-census comparison sources, observed output sizes/hashes, and commands.

Executed A environment: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, binary64 only for Qhull proposals, one OpenBLAS/OMP/MKL thread, assertions enabled. Every accepted predicate, plane grouping, volume and equilibrium decision is exact integer arithmetic. Qhull is not trusted to certify the hull: every triangle is an exact supporting triangle; the closed connected oriented sphere and each maximal convex polygon boundary are checked. Every retained parent extreme point is used. Uncertified proposals would be separately recorded; observed uncertified=0 in both complete censuses.

```python
#!/usr/bin/env python3
"""Exact finite vertex-subset census, Qhull proposes triangles only.
Every proposed surface is checked using integers for support, closure, maximal
facet boundaries and strict/weak stable/unstable equilibria at filled centroid.
A result S=U=1 is a candidate for separate full saddle and independent A/B audit.
Usage: EXACT_DELETE.py REPORT.json OUT kmax [start=0] [end=0]
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib,itertools,math,platform
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
import scipy
from scipy.spatial import ConvexHull
assert __debug__

def pack(x):return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def load(path):
 raw=Path(path).read_bytes();obj=json.loads(raw)
 points=[tuple(Q(x) for x in p) for p in obj['points']]
 den=math.lcm(*(v.denominator for p in points for v in p))
 P=[tuple(int(v*den) for v in p) for p in points]
 return raw,obj,P,den

def audit(P,den,keep,full=False):
 A=[P[i] for i in keep];nV=len(A)
 assert nV>=4 and len(set(A))==nV
 h=ConvexHull(np.array(A,dtype=float)/den)
 # All retained vertices were extreme in the exact convex parent; they must stay so.
 assert set(map(int,h.vertices))==set(range(nV))
 T=[];groups={};tri_edges={};D=0;N=(0,0,0)
 for ids in h.simplices:
  a,b,c=map(int,ids);normal=cross(sub(A[b],A[a]),sub(A[c],A[a]))
  assert normal!=(0,0,0)
  height=dot(normal,A[a]);values=[dot(normal,p)-height for p in A]
  if max(values)>0:
   assert min(values)>=0
   b,c=c,b;normal=tuple(-x for x in normal);height=-height;values=[-x for x in values]
  assert max(values)==0 and min(values)<0
  g=math.gcd(*normal,height);row=tuple(x//g for x in (*normal,height))
  groups.setdefault(row,[]).append((a,b,c));T.append((a,b,c))
  det=dot(A[a],cross(A[b],A[c]));D+=det;N=add(N,tuple(det*x for x in add(add(A[a],A[b]),A[c])))
  for u,v in ((a,b),(b,c),(c,a)):tri_edges.setdefault(tuple(sorted((u,v))),[]).append((u,v,len(T)-1))
 assert D>0
 assert len(T)==2*nV-4 and nV-len(tri_edges)+len(T)==2
 assert all(len(z)==2 and z[0][:2]==z[1][:2][::-1] for z in tri_edges.values())
 # Connected triangular boundary, exact support on all retained points.
 adj=[set() for _ in T]
 for vals in tri_edges.values():a,b=vals[0][2],vals[1][2];adj[a].add(b);adj[b].add(a)
 seen={0};todo=[0]
 while todo:
  a=todo.pop()
  for b in adj[a]-seen:seen.add(b);todo.append(b)
 assert len(seen)==len(T)
 Z=4*D;S=[];WS=[];cycles=[];H=[];true_edges={}
 for row,tris in sorted(groups.items()):
  n=row[:3];hh=row[3];nn=dot(n,n);owner={i for i,p in enumerate(A) if dot(n,p)==hh};ed={}
  for a,b,c in tris:
   for u,v in ((a,b),(b,c),(c,a)):ed.setdefault(tuple(sorted((u,v))),[]).append((u,v))
  assert all(len(v) in (1,2) for v in ed.values())
  assert all(len(v)==1 or v[0]==v[1][::-1] for v in ed.values())
  boundary=[v[0] for v in ed.values() if len(v)==1]
  succ=dict(boundary);assert len(succ)==len(boundary)==len(owner)
  assert set(succ)==owner and set(succ.values())==owner
  first=min(owner);cy=[first]
  while succ[cy[-1]]!=first:
   cy.append(succ[cy[-1]]);assert len(cy)<=len(owner)
  assert set(cy)==owner
  # Convex, strict polygon corner tests (none of the parent extreme points can be collinear).
  for i in range(len(cy)):
   u,v,w=cy[i-1],cy[i],cy[(i+1)%len(cy)]
   assert dot(n,cross(sub(A[v],A[u]),sub(A[w],A[v])))>0
  for u,v in boundary:
   inward=cross(n,sub(A[v],A[u]))
   assert all(dot(inward,sub(A[j],A[u]))>=0 for j in owner)
  height_num=Z*hh-dot(n,N);assert height_num>0
  foot_num=add(tuple(nn*x for x in N),tuple(height_num*x for x in n));denfoot=Z*nn
  signs=[dot(cross(n,sub(A[v],A[u])),sub(foot_num,tuple(denfoot*x for x in A[u]))) for u,v in boundary]
  owners=sorted(keep[i] for i in owner)
  if min(signs)>0:S.append(owners)
  elif min(signs)==0:WS.append(owners)
  for u,v in boundary:true_edges.setdefault(tuple(sorted((u,v))),[]).append(len(cycles))
  cycles.append(cy);H.append(row)
 assert all(len(v)==2 for v in true_edges.values())
 assert nV-len(true_edges)+len(cycles)==2
 U=[];WU=[]
 for i,p in enumerate(A):
  radial=sub(tuple(Z*x for x in p),N)
  signs=[dot(radial,sub(q,p)) for j,q in enumerate(A) if j!=i]
  if max(signs)<0:U.append(keep[i])
  elif max(signs)==0:WU.append(keep[i])
 g=math.gcd(Z,*N);zn=Z//g;ng=[x//g for x in N]
 result=dict(V=nV,E=len(true_edges),F=len(cycles),C=2*len(true_edges),S=S,U=U,weakS=WS,weakU=WU,
             volume6_lattice=D,centroid_lattice_numerators=ng,centroid_lattice_denominator=zn)
 if full:result.update(triangles=[[keep[i] for i in t] for t in T],facets=[[keep[i] for i in c] for c in cycles],supports=H)
 return result

def main(src,out,kmax,start=0,end=0):
 raw,obj,P,den=load(src);out=Path(out);out.mkdir(parents=True,exist_ok=False)
 (out/'INPUT_REPORT.json').write_bytes(raw)
 opts=dict(version='COORD_EXACT_DELETE_V1',input_sha256=hashlib.sha256(raw).hexdigest(),denominator=den,
           kmax=kmax,start=start,end=end,order='k=1..kmax then lexicographic combinations',
           python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,threads=1)
 (out/'OPTIONS.json').write_bytes(pack(opts));counts={};rows=[];failures=[];candidates=[];rank=-1
 for k in range(1,kmax+1):
  for deleted in itertools.combinations(range(len(P)),k):
   rank+=1
   if rank<start:continue
   if end and rank>=end:break
   keep=[i for i in range(len(P)) if i not in deleted]
   try:
    r=audit(P,den,keep);r['deleted']=list(deleted);r['rank']=rank;rows.append(r)
    cl=str(len(r['S']))+','+str(len(r['U']));counts[cl]=counts.get(cl,0)+1
    if len(r['S'])==len(r['U'])==1:candidates.append(r);print('EXACT_SU11_CANDIDATE',r,flush=True)
   except Exception as e:
    fail=dict(rank=rank,deleted=list(deleted),error=type(e).__name__+': '+str(e));failures.append(fail);print('UNCERTIFIED',fail,flush=True)
   if len(rows)%100==0:
    (out/'CENSUS.json').write_bytes(pack(rows));print('EXACT_DELETE_PROGRESS',len(rows),len(failures),counts,flush=True)
  if end and rank>=end:break
 (out/'CENSUS.json').write_bytes(pack(rows));(out/'FAILURES.json').write_bytes(pack(failures))
 summary=dict(tested=len(rows),uncertified=len(failures),counts=counts,candidates=candidates,options=opts,last_rank=rank)
 (out/'SUMMARY.json').write_bytes(pack(summary));print('COORD_EXACT_DELETE_FINISHED',summary,flush=True)
if __name__=='__main__':main(sys.argv[1],sys.argv[2],*map(int,sys.argv[3:]))
```
