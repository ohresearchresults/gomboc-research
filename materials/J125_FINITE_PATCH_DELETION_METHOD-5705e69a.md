# material-5705e69ac12b

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J125 — 101 finite patch deletions with rebuilt homogeneous mass

## Result and limits
The coordinator executed all 101 distinct nominated survivor sets on the literal APEX2_MATCH_G6 parent. All returned numerically valid hulls under the stated plane-grouping tolerance; none had U1 or own110. Only the parent and deleting its old U10 alone retained numerical S1. Deleting full trapped blocks of 66 and 96 vertices gave respectively V98/E195/F99 with S5/U15 and V68/E143/F77 with S7/U6. The disappearance of old roots therefore did not remove the complete landscapes. Smaller scalar P in other cases came with new P and/or Q. This is a finite numerical negative result, NOT an exact census of every child or an exclusion of arbitrary adjacent patches, moved vertices or mass correction. The separate exact independent-deletion theorem is [internal-source-reference]; it does not rely on this scan.

Deleting U10 alone gives numerical V163/E247/F86,S1/U2,P~.1601791891041, with old U10 replaced by original vertex6; the parent P is ~.16017849212. Deleting old U153 alone gives V163/E247/F86,S42/U11, including a main P~.14722 and Q~.0011505 plus many small positive bars. These inherited-coordinate bodies were not newly promoted as exact endpoints. All survivor sets are literally generated below from the exact original true-edge graph and fixed nomination blocks. No coordinate optimization or rounding is performed.

## Complete exact dependencies
APEX2_MATCH_G6_AUDIT.json,139796 bytes,SHA86bf822bdd1b37e1215d34fb0afaa6b5692eac01743f35da9ef27e45c3714f88, is reconstructed from the complete already immutable materials [internal-source-reference], [internal-source-reference] and [internal-source-reference]. The precise commands and their hashes are in [internal-source-reference]. That certificate also contains the complete CUT125_NOMINATION.json,775 bytes,SHA8f58bc40ba8a8d7972682c699431e87ca26aee6514f73b03f92fe2d27d7aae75. Supply all four materials to reconstruct this scan's inputs; a result hash alone is not input data.

Python3.13.5,NumPy2.3.5,SciPy1.17.0, assertions enabled, one BLAS/OpenMP thread. Execute:
```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python patchscan125.py > PATCH125_SCAN.log
```
Observed terminal: J125_FINITE_PATCH_SCAN_DONE_NUMERICAL_ONLY 101.
PATCH125_SCAN.json:200716 bytes,SHAa7bb2e7176ffce7ab9d0f5f7d7d643076b594582f0e3cbc3a0630cd584c8e560.
PATCH125_SCAN.log:65174 bytes,SHA863432b087c35b60a5f04a21db7f7053296a4b507073197ea15d2b034f9b38f7.
These numerical byte identities describe this execution, not cross-platform floating invariance. The full runnable generator below is sufficient to regenerate all 101 exact-coordinate survivor selections and their numerical evaluations from the fixed inputs. No hidden checkpoint or originating sandbox is needed.

## patchscan125.py
4605 bytes,SHAe77073b88655d6f1314a501de129b4b75195f3beedd0330221bb39f9bbf6fa92. Save with final newline.
```python
"""Finite old-vertex patch deletion search with rebuilt actual hull/mass.
Numerical nominations only. Exact surviving vertex coordinates are inherited
from the named rational input; no coordinate rounding is performed here.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
from pathlib import Path
from fractions import Fraction as Q
import json,sys,itertools,heapq
import numpy as np
from scipy.spatial import ConvexHull,QhullError
sys.set_int_max_str_digits(0)

def input_data():
 a=json.loads(Path('APEX2_MATCH_G6_AUDIT.json').read_text());X=np.array([[float(Q(v))for v in x]for x in a['vertices']]);return a,X

def bars(X,edges):
 r=np.einsum('ij,ij->i',X,X);e=np.array(edges,int);d=X[e[:,1]]-X[e[:,0]];t=np.clip(-np.einsum('ij,ij->i',X[e[:,0]],d)/np.einsum('ij,ij->i',d,d),0,1);f=X[e[:,0]]+t[:,None]*d;w=np.einsum('ij,ij->i',f,f);order=sorted(range(len(e)),key=lambda k:(-w[k],int(e[k,0]),int(e[k,1])));p=list(range(len(X)));out=[]
 def find(i):
  while p[i]!=i:p[i]=p[p[i]];i=p[i]
  return i
 for k in order:
  i,j=map(int,e[k]);a,b=find(i),find(j)
  if a==b:continue
  if (r[a],-a)<(r[b],-b):a,b=b,a
  dep=1-w[k]/r[b]
  if dep>1e-10:out.append(dict(root=b,edge=[i,j],depth=float(dep)))
  p[b]=a
 return sorted(out,key=lambda b:-b['depth'])

def state(Y):
 if len(Y)<4:return None
 h=ConvexHull(Y);tri=h.simplices.copy();c=Y.mean(0);p=Y[tri]-c;sign=np.einsum('ij,ij->i',np.cross(p[:,1]-p[:,0],p[:,2]-p[:,0]),h.equations[:,:3]);flip=sign<0;tri[flip,1],tri[flip,2]=tri[flip,2].copy(),tri[flip,1].copy();p=Y[tri]-c;D=np.einsum('ij,ij->i',p[:,0],np.cross(p[:,1],p[:,2]));V=D.sum()/6;g=c+np.einsum('i,ij->j',D,p.sum(1))/(4*D.sum())
 # Group only almost identical normalized support planes; final exact hull is required.
 plane=[];group=[]
 for row in h.equations:
  found=next((k for k,q in enumerate(plane)if np.max(abs(row-q))<1e-9),None)
  if found is None:found=len(plane);plane.append(row)
  group.append(found)
 owners={}
 for k,t in enumerate(tri):
  for i,j in zip(t,np.roll(t,-1)):owners.setdefault(tuple(sorted((int(i),int(j)))),set()).add(group[k])
 edges=sorted(e for e,f in owners.items()if len(f)==2);dual=[sorted(owners[e])for e in edges];active=sorted(set(h.vertices.tolist()));N=np.array(plane);q=N[:,:3]/(-N[:,3]-N[:,:3]@g)[:,None];P=Y-g
 def scores(Z):
  d=Z[None,:,:]-Z[:,None,:];raw=np.einsum('ik,ijk->ij',Z,d);den=np.linalg.norm(Z,axis=1)[:,None]*np.linalg.norm(d,axis=2);np.fill_diagonal(den,1);rho=raw/den;np.fill_diagonal(rho,-np.inf);return rho.max(1)
 sp,sq=scores(P),scores(q);U=np.flatnonzero(sp<0).tolist();S=np.flatnonzero(sq<0).tolist();PB=bars(P,edges);QB=bars(q,dual);F=len(plane);E=len(edges)
 assert len(active)-E+F==2,(len(active),E,F)
 return dict(V=len(active),E=E,F=F,volume=float(V),centroid=g.tolist(),S=S,U=U,P=PB,Q=QB,guardP=float(np.min(np.delete(sp,U)))if len(U)<len(P)else None,guardQ=float(np.min(np.delete(sq,S)))if len(S)<len(q)else None)

def run():
 a,X=input_data();adj=[set()for _ in X]
 for i,j in a['edges']:adj[i].add(j);adj[j].add(i)
 cases=[('none',set())];blocks=json.loads(Path('CUT125_NOMINATION.json').read_text())['blocks']
 for k,B in enumerate(blocks):cases.append((f'wholeblock{k}',set(B)))
 for root in a['U']:
  seen={root};front={root}
  for depth in range(1,13):
   cases.append((f'ball{root}_{depth-1}',set(seen)));front=set.union(*(adj[i]for i in front))-seen if front else set();seen|=front
 # Actual radial height cuts in a cone around each old U, retaining a flexible coarse core.
 g=np.array([float(Q(v))for v in a['centroid']]);P=X-g
 for root in a['U']:
  u=P[root]/np.linalg.norm(P[root]);z=P@u
  for k in range(1,min(115,len(X)-4),3):cases.append((f'top{root}_{k}',set(np.argsort(-z)[:k].tolist())))
 seen=set();out=[]
 for name,B in cases:
  key=tuple(sorted(B))
  if key in seen:continue
  seen.add(key);ids=[i for i in range(len(X))if i not in B]
  if len(ids)<4:continue
  try:s=state(X[ids])
  except (ValueError,QhullError,AssertionError) as e:
   out.append(dict(name=name,deleted=list(key),error=str(e)));continue
  s.update(name=name,deleted=list(key),U_original=[ids[i]for i in s['U']],source='APEX2_MATCH_G6');out.append(s)
 Path('PATCH125_SCAN.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
 for s in out:
  if 'error'in s:print(s['name'],'ERROR',s['error']);continue
  print(s['name'],len(s['deleted']),[s[k]for k in ('V','E','F')],len(s['S']),len(s['U']),[b['depth']for b in s['P']],[b['depth']for b in s['Q']],s['U_original'])
 print('J125_FINITE_PATCH_SCAN_DONE_NUMERICAL_ONLY',len(out))
if __name__=='__main__':run()
```
