# material-9fc46cf305a5

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# COORD_DELETE4225 — Recovery capsule part 2/2

Requires part 1 [internal-source-reference] and its explicit complete NC57 input result figure-0398, SHA256 b6c84be62ea56d1c11575d4d6309563f525d734f79b0ad2a299f0b7abd2ccdd3. Both immutable materials plus the complete immutable input result are a fully specified source-based recovery capsule. No originating sandbox or Library item is required. The full original exact input reports are regenerated from that literal parent capsule; their sizes, SHA values and point identities are in part 1.

## Independent method B and proof scope
B uses only standard-library exact integer/Fraction arithmetic and imports neither A nor any NC57 checker. Every possible supporting facet of every deletion child contains three noncollinear retained parent points. B enumerates every parent triple and both plane orientations that could become supporting after <=2 deletions. A plane with >2 parent points strictly on both sides cannot be a child support. The resulting complete plane catalogue has728 candidates from41664 triples for C372, and740 from43680 triples for C378. Each deletion child selects exactly those planes whose positive-side points have all been deleted. Exact planar monotone-chain hulls recover maximal polygons; their edge pairs, extremality, strict internal centroid position and Euler relation are checked. All retained parent extreme points occur.

B uses a different triangulation fan and a strictly interior arithmetic-mean anchor, requiring every tetrahedral determinant positive. This yields an independent filled-volume and first-moment integration. It evaluates stable-face projection using edge-wall inequalities, unstable vertices through true-edge tangent-cone generators, and saddles by all four edge-projection/normal-cone primitives. All observed weakS/weakU/weakH are empty. B checks the unchanged parent separately too. A independently checks all pairwise vertex inequalities and an explicit projected-foot formula; every common A/B field matches for all4225 cases. Only B computes H in this capsule, so do not describe it as two independent full H audits. Two independent exact S>=2 certifications suffice for the finite own110 exclusion.

## Complete runnable commands
Use a new working directory, save both sources from the two materials and COMPARE_DELETE.py below, and recover NC57 there. Commands, every option explicit:
```
python EXACT_DELETE.py NC57_SOURCE/proof/C372_ALT_FULL_G4/REPORT.json EXACT_DELETE372_K2 2 0 0
python EXACT_DELETE.py NC57_SOURCE/proof/C378_ALT_POLY_G6/REPORT.json EXACT_DELETE378_K2 2 0 0
python -B -S EXACT_DELETE_B.py NC57_SOURCE/proof/C372_ALT_FULL_G4/REPORT.json EXACT_B372_K2 2
python -B -S EXACT_DELETE_B.py NC57_SOURCE/proof/C378_ALT_POLY_G6/REPORT.json EXACT_B378_K2 2
python -B -S COMPARE_DELETE.py .
```
Assertions enabled, CPython3.13.5; A additionally NumPy2.3.5/SciPy1.17.0, one BLAS/OMP/MKL thread. B and comparison are standard-library-only, no randomness. A terminal COORD_EXACT_DELETE_FINISHED twice; B terminal COORD_EXACT_ALL_TRIPLES_DELETE_FINISHED twice; comparison terminal COORD_DELETE4225_INDEPENDENT_HULL_MASS_SU_ALL_MATCH_NO_OWN110. Both A failure arrays must be empty. Changing runtime version changes only version-bearing summary/options metadata; compare all hashes in the specified environment.

## Reproduced output byte counts and SHA256
These hashes were observed after complete successful execution, not predicted. Full census bytes regenerate from the preserved complete sources and exact parent inputs; no rows or defining choices are omitted.
- EXACT_DELETE372_K2/CENSUS.json:636242,c171b3b581a7412bc36bfcad0db28ea647cfc391dd6cdda2553aeeb5cf2c5221
- EXACT_DELETE372_K2/INPUT_REPORT.json:14190,639b7dd56caf48ee99f1175e20b1f305100dc0fb3f75440dd20aba8df57b4cb5
- EXACT_DELETE372_K2/OPTIONS.json:281,b56e9a78cc4379ce3a9e5719abe89863196ef5da5ad95369aff6bf03b444c0f8
- EXACT_DELETE372_K2/FAILURES.json:3,37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- EXACT_DELETE372_K2/SUMMARY.json:825,bf6ba962822286e727722f31b1184e47859a948b650cd3dcc910542454e1c09c
- EXACT_B372_K2/CENSUS.json:736087,46f88d56ec3b11520f1a997203fdb0748b27befb6961c21e70744f898557c1c7
- EXACT_B372_K2/PARENT.json:293,2ae372daffca3d9a8fe986153ea7ba49c93a143d46a4f3b92ade809ea209d87f
- EXACT_B372_K2/SUMMARY.json:933,d38d1004ed1cc0f174dcbd9f39f3eda32262547fe969dd73b4798898da3de4ed
- EXACT_DELETE378_K2/CENSUS.json:737620,630d2eba5902b82fb4b4eaca07a5452460eb9d4522a7af9af7c4814efb8af132
- EXACT_DELETE378_K2/INPUT_REPORT.json:18534,fc46fb08252486d5c2474d70c6834b2f4849f8de25bcf18ccb059a7aa9ced661
- EXACT_DELETE378_K2/OPTIONS.json:283,8701b9f721153bddd4f5fb23e97549d5c3dec82106c1f4066861b53a69c5f4c1
- EXACT_DELETE378_K2/FAILURES.json:3,37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- EXACT_DELETE378_K2/SUMMARY.json:882,41f03ce173c2d3be40fec4f70bbcd11d4a009585ab0a0e76ff96c41365588aa7
- EXACT_B378_K2/CENSUS.json:850190,4fcf66a23910e1988aff41d339a048cf6d9f986cf444bdfa901d579ba26bafdb
- EXACT_B378_K2/PARENT.json:328,84b0f402e29443672bc59bf8cb009923e77166621ba85949dae75bc9f638ff48
- EXACT_B378_K2/SUMMARY.json:1009,f53a67f81ab4cb2d22c63dc4186504b800c7e1da2676f7bdc62585e7526163e6

## EXACT_DELETE_B.py
6371 bytes, SHA2560569ca2bbdf86a5e79345ddebdfe5f5f702a58c3868f75950da1f50a15baa925, UTF8 with one final newline.
```python
#!/usr/bin/env python3
"""Independent all-triple hull and positive-anchor moment census; standard library.
No imports from the Qhull-based census or NC57 auditors.
Usage: EXACT_DELETE_B.py REPORT.json OUT kmax
Also evaluates the unchanged parent (rank -1). All exact integers.
"""
from pathlib import Path
from fractions import Fraction
from itertools import combinations
from math import gcd,lcm
import json,hashlib,sys,platform
assert __debug__

def enc(v):return (json.dumps(v,sort_keys=True,separators=(',',':'))+'\n').encode()
def minus(a,b):return (a[0]-b[0],a[1]-b[1],a[2]-b[2])
def plus(a,b):return (a[0]+b[0],a[1]+b[1],a[2]+b[2])
def times(a,k):return (a[0]*k,a[1]*k,a[2]*k)
def scalar(a,b):return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
def wedge(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def polygon(P,ids,n):
 drop=max(range(3),key=lambda k:abs(n[k]));axes=[i for i in range(3) if i!=drop]
 q=lambda i:(P[i][axes[0]],P[i][axes[1]])
 order=sorted(ids,key=q)
 def turn(i,j,k):
  a,b,c=q(i),q(j),q(k);return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
 def half(order):
  ans=[]
  for i in order:
   while len(ans)>1 and turn(ans[-2],ans[-1],i)<=0:ans.pop()
   ans.append(i)
  return ans
 cy=half(order)[:-1]+half(order[::-1])[:-1]
 assert set(cy)==set(ids) and len(cy)==len(ids)
 if scalar(n,wedge(minus(P[cy[1]],P[cy[0]]),minus(P[cy[2]],P[cy[1]])))<0:cy.reverse()
 j=cy.index(min(cy));return cy[j:]+cy[:j]

def catalogue(P,kmax):
 rows={};rejected=0;triples=0
 for a,b,c in combinations(range(len(P)),3):
  triples+=1;n=wedge(minus(P[b],P[a]),minus(P[c],P[a]));h=scalar(n,P[a])
  if n==(0,0,0):continue
  g=gcd(*n,h);row=tuple(x//g for x in (*n,h))
  if next(x for x in row if x)!=abs(next(x for x in row if x)):row=tuple(-x for x in row)
  if row in rows:continue
  pos=[];neg=[];zero=[]
  for i,p in enumerate(P):
   x=scalar(row[:3],p)-row[3]
   if x>0:pos.append(i)
   elif x<0:neg.append(i)
   else:zero.append(i)
   if len(pos)>kmax and len(neg)>kmax:break
  if len(pos)>kmax and len(neg)>kmax:rejected+=1;continue
  # A full-dimensional parent and at most kmax deletions can only expose one side.
  assert len(pos)+len(neg)+len(zero)==len(P)
  assert len(pos)>kmax or len(neg)>kmax
  if len(pos)>kmax:row=tuple(-x for x in row);pos=neg
  rows[row]=(tuple(pos),tuple(zero))
 by_out={}
 for row,(out,zero) in rows.items():by_out.setdefault(out,[]).append((row,zero))
 return by_out,dict(triples=triples,candidate_planes=len(rows),rejected_triple_tests=rejected)

def census(P,den,by_out,deleted):
 de=set(deleted);keep=[i for i in range(len(P)) if i not in de];nv=len(keep)
 faces=[]
 for k in range(len(deleted)+1):
  for outside in combinations(deleted,k):
   for row,zeros in by_out.get(outside,[]):
    ids=[i for i in zeros if i not in de]
    if len(ids)>=3:faces.append((row,polygon(P,ids,row[:3])))
 faces.sort();edges={};anchor=tuple(sum(P[i][k] for i in keep) for k in range(3))
 DS=0;NS=(0,0,0)
 for fi,(row,cy) in enumerate(faces):
  for u,v in zip(cy,cy[1:]+cy[:1]):edges.setdefault(tuple(sorted((u,v))),[]).append((fi,u,v))
  # A different fan from a strictly interior arithmetic-mean anchor.
  cy=cy[1:]+cy[:1]
  for a,b,c in ((cy[0],cy[j],cy[j+1]) for j in range(1,len(cy)-1)):
   det=scalar(minus(times(P[a],nv),anchor),wedge(minus(times(P[b],nv),anchor),minus(times(P[c],nv),anchor)))
   assert det>0
   DS+=det;NS=plus(NS,times(plus(anchor,times(plus(plus(P[a],P[b]),P[c]),nv)),det))
 assert DS%(nv**3)==0;D=DS//(nv**3);ZZ=4*nv*DS
 gg=gcd(ZZ,*NS);Z=ZZ//gg;N=tuple(x//gg for x in NS)
 assert nv-len(edges)+len(faces)==2
 assert all(len(vals)==2 and vals[0][1:]==vals[1][1:][::-1] for vals in edges.values())
 assert set(i for _,cy in faces for i in cy)==set(keep)
 S=[];WS=[];U=[];WU=[];HS=[];WH=[]
 for row,cy in faces:
  n=row[:3];assert Z*row[3]-scalar(n,N)>0
  margins=[scalar(wedge(n,minus(P[v],P[u])),minus(N,times(P[u],Z))) for u,v in zip(cy,cy[1:]+cy[:1])]
  if min(margins)>0:S.append(sorted(cy))
  elif min(margins)==0:WS.append(sorted(cy))
 adj={i:[] for i in keep}
 for u,v in edges:adj[u].append(v);adj[v].append(u)
 for u in keep:
  radial=minus(times(P[u],Z),N);margins=[scalar(radial,minus(P[v],P[u])) for v in adj[u]]
  if max(margins)<0:U.append(u)
  elif max(margins)==0:WU.append(u)
 for (a,b),vals in sorted(edges.items()):
  e=minus(P[b],P[a]);e2=scalar(e,e);at=scalar(minus(N,times(P[a],Z)),e);bt=Z*e2-at
  r1=faces[vals[0][0]][0];r2=faces[vals[1][0]][0];n1,n2=r1[:3],r2[:3]
  h1=Z*r1[3]-scalar(n1,N);h2=Z*r2[3]-scalar(n2,N)
  n11=scalar(n1,n1);n22=scalar(n2,n2);n12=scalar(n1,n2)
  assert n11*n22-n12*n12>0
  c=h1*n22-h2*n12;d=h2*n11-h1*n12
  m=min(at,bt,c,d)
  if m>0:HS.append([a,b])
  elif m==0:WH.append([a,b])
 if not WS and not WU and not WH:assert len(S)+len(U)-len(HS)==2
 return dict(V=nv,E=len(edges),F=len(faces),C=2*len(edges),S=S,U=U,H=HS,weakS=WS,weakU=WU,weakH=WH,
             volume6_lattice=D,centroid_lattice_numerators=list(N),centroid_lattice_denominator=Z)

def main(src,out,kmax):
 raw=Path(src).read_bytes();d=json.loads(raw);p=[tuple(Fraction(x) for x in r) for r in d['points']]
 den=lcm(*(x.denominator for row in p for x in row));P=[tuple(int(x*den) for x in row) for row in p]
 out=Path(out);out.mkdir(parents=True,exist_ok=False)
 cat,meta=catalogue(P,kmax);print('EXACT_ALL_TRIPLES_CATALOGUE',meta,flush=True)
 parent=census(P,den,cat,());(out/'PARENT.json').write_bytes(enc(parent))
 counts={};data=[];rank=-1
 for k in range(1,kmax+1):
  for deleted in combinations(range(len(P)),k):
   rank+=1;r=census(P,den,cat,deleted);r.update(rank=rank,deleted=list(deleted));data.append(r)
   cl=','.join(str(len(r[x])) for x in ['S','U','H']);counts[cl]=counts.get(cl,0)+1
   if rank%200==0:print('EXACT_B_PROGRESS',rank,counts,flush=True)
 (out/'CENSUS.json').write_bytes(enc(data))
 opts=dict(kmax=kmax,input_sha256=hashlib.sha256(raw).hexdigest(),integer_lattice_denominator=den,
           version='COORD_EXACT_ALL_TRIPLES_DELETE_V1',python=platform.python_version(),catalogue=meta)
 summary=dict(tested=len(data),counts=counts,min_stable=min(len(r['S']) for r in data),
              any_weak=sum(bool(r['weakS'] or r['weakU'] or r['weakH']) for r in data),options=opts)
 (out/'SUMMARY.json').write_bytes(enc(summary));print('COORD_EXACT_ALL_TRIPLES_DELETE_FINISHED',summary,flush=True)
if __name__=='__main__':main(sys.argv[1],sys.argv[2],int(sys.argv[3]))
```

## COMPARE_DELETE.py
1062 bytes,SHA256297fb86911a4a8d092340956e8a404de51a579307f1d278ccf8432b5a98aec46,UTF8 one final newline.
```python
#!/usr/bin/env python3
"""Compare every exact A field with independently computed B; assert scoped result."""
import json,sys,hashlib
from pathlib import Path
root=Path(sys.argv[1]);record=[]
for n,total,number211 in ((372,2080,21),(378,2145,45)):
 a=json.loads((root/f'EXACT_DELETE{n}_K2/CENSUS.json').read_text())
 b=json.loads((root/f'EXACT_B{n}_K2/CENSUS.json').read_text())
 assert len(a)==len(b)==total
 for x,y in zip(a,b):
  assert all(x[k]==y[k] for k in x),(n,x['rank'])
  assert len(y['S'])>=2 and not(y['weakS'] or y['weakU'] or y['weakH'])
  assert len(y['S'])+len(y['U'])-len(y['H'])==2
 good=[r for r in b if [len(r[k]) for k in ('S','U','H')]==[2,1,1]]
 assert len(good)==number211
 sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
 record.append(dict(parent=n,tested=total,own211=number211,minS=min(len(r['S']) for r in b),
                    A=sha(root/f'EXACT_DELETE{n}_K2/CENSUS.json'),B=sha(root/f'EXACT_B{n}_K2/CENSUS.json')))
print('COORD_DELETE4225_INDEPENDENT_HULL_MASS_SU_ALL_MATCH_NO_OWN110',json.dumps(record,sort_keys=True))
```
