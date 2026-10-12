# material-a59e6de3d73d

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J125 — complete finite numerical nomination methods

These two complete runnable units produced the cap-mass and two-trapped-block nominations used in the exact J125 certificate [internal-source-reference]. They are numerical discovery code, not the proof. The exact certificate uses the literal CUT125_NOMINATION.json and exact rational checker already stored there, so does not depend on solver or floating-path reproducibility.

Exact input dependency is APEX2_MATCH_G6_AUDIT.json,139796 bytes,SHA86bf822bdd1b37e1215d34fb0afaa6b5692eac01743f35da9ef27e45c3714f88, reconstructed with the three complete J124/J115 materials [internal-source-reference],[internal-source-reference],[internal-source-reference] and the commands in the exact certificate. No hidden numerical checkpoint is consumed. Python3.13.5,NumPy2.3.5,SciPy1.17.0,one BLAS/OpenMP thread. All nondefault parameters are literal in these sources.

Executed commands:
```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python probe125.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python cutprobe125.py
```
Observed finite outcomes:162 simple-vertex caps sum0.029493450257594464 versus parent volume1.7020728735202417. The numerical mixed-integer independent-simple-cap maximum was0.016787746438070357, with matching reported floating dual bound and optimal solver status. This is NOT an exact MILP optimality proof, not used by the rational theorem, and excludes the two degree-four vertices from its variables. The later exact theorem includes both degree-four vertices without relying on this optimization.

The four centre boxes tested by cutprobe produced disjoint exclusive predecessor sets of sizes67/96 for its coordinatewise simple-cap bound,66/96 for cube radius.0125,63/95 for.02,60/94 for.03. Only the literal1/80 case and the all164-cap mass inclusion were subsequently certified exactly. The first source writes CAPS125_NUM.npz as a disposable diagnostic; it is not an input to the proof. The second writes CUT125_NOMINATION.json,775 bytes/SHA8f58bc40ba8a8d7972682c699431e87ca26aee6514f73b03f92fe2d27d7aae75. A prior NumPy-int JSON-serialization error was fixed by explicit int conversion in this complete current source; no result is inferred from that failed serialization call.

## probe125.py
2383 bytes,SHA8e9120e74bb785e16ef3728a49416fd9b15d7d253248c687cf5e7f47f8a6ba81.
```python
"""Finite independent simple-vertex deletion diagnostics, numerical nomination only."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import json,itertools,sys
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
from scipy.optimize import milp,LinearConstraint,Bounds,linprog
from scipy.spatial import ConvexHull
sys.set_int_max_str_digits(0)
def load():
 a=json.loads(Path('APEX2_MATCH_G6_AUDIT.json').read_text());X=np.array([[float(Q(z))for z in p]for p in a['vertices']]);g=np.array([float(Q(z))for z in a['centroid']]);V=float(Q(a['volume']));adj=[set()for _ in X]
 for i,j in a['edges']:adj[i].add(j);adj[j].add(i)
 ids=[i for i in range(len(X))if len(adj[i])==3];cs=[];dv=[];nb=[]
 for i in ids:
  nn=sorted(adj[i]);v=X[nn]-X[i];dv.append(abs(np.linalg.det(v))/6);cs.append((X[i]+X[nn].sum(0))/4);nb.append(nn)
 return a,X,g,V,adj,ids,np.array(dv),np.array(cs),nb

def main():
 a,X,g,V,adj,ids,dv,cs,nb=load();print('ROOTS',a['U'],'S',a['S'],'VOLUME',V,'CENTRE',g)
 print('CAPSUM',dv.sum(), 'PARENTFRACTION',dv.sum()/V,'LARGEST',sorted(zip(dv,ids),reverse=True)[:10])
 idx={j:k for k,j in enumerate(ids)}; conflicts=[(idx[i],idx[j])for i,j in a['edges']if i in idx and j in idx];A=np.zeros((len(conflicts),len(ids)))
 for k,(i,j)in enumerate(conflicts):A[k,i]=A[k,j]=1
 opts={'time_limit':15,'mip_rel_gap':1e-8};res=milp(-dv,integrality=np.ones(len(ids)),bounds=Bounds(0,1),constraints=LinearConstraint(A,0,1),options=opts)
 print('MAXCAP',res.message,res.fun,'BOUND',getattr(res,'mip_dual_bound',None))
 for u in a['U']:
  print('ROOT',u,'degree',len(adj[u]),'neighbors',sorted(adj[u]),'capV',dv[idx[u]] if u in idx else None)
  for j in adj[u]:print('guard',j,float(np.dot(X[u]-g,X[j]-X[u]))/np.linalg.norm(X[j]-X[u]))
 # Broad independent-cap centroid enclosure via unconstrained boxes.
 M=V*g;coeff=dv[:,None]*(cs-g);delta=np.sum(np.abs(coeff),axis=0)/(V-dv.sum());print('BOX',delta)
 t=np.zeros(len(ids));t[idx[a['U'][0]]]=1
 for u in a['U']:
  if u not in idx:continue
  x=np.zeros(len(ids));x[idx[u]]=1;c=(V*g-dv[idx[u]]*cs[idx[u]])/(V-dv[idx[u]]);print('DELETE_ROOT',u,'dg',c-g)
 print('CHANGESCAP',[(i,float(dv[k]),[float(z)for z in cs[k]-g])for k,i in enumerate(ids)if i in a['U']])
 np.savez('CAPS125_NUM.npz',X=X,g=g,V=V,ids=ids,dv=dv,cs=cs,A=A)
if __name__=='__main__':main()
```

## cutprobe125.py
1359 bytes,SHAf6d2ccfc0e0b293f8e6ad0e0937ddfe906b209f50f00947433f1e90eb1bd0c0f.
```python
from probe125 import *
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

def scan():
 a,X,g,V,adj,ids,dv,cs,nb=load();delta=np.sum(np.abs(dv[:,None]*(cs-g)),axis=0)/(V-dv.sum());P=X-g
 for eps in [delta,np.repeat(.0125,3),np.repeat(.02,3),np.repeat(.03,3)]:
  D=X[None,:,:]-X[:,None,:];scores=np.einsum('ik,ijk->ij',P,D);possible=scores+np.einsum('ijk,k->ij',abs(D),eps)>=0;np.fill_diagonal(possible,False)
  reachable=possible.copy();np.fill_diagonal(reachable,True)
  for k in range(len(X)):reachable|=reachable[:,k,None]&reachable[k,None,:]
  labels=[set(np.flatnonzero(reachable[:,u])) for u in a['U']];exclusive=[list(map(int,sorted(labels[0]-labels[1]))),list(map(int,sorted(labels[1]-labels[0])))]
  print('EPS',eps,'EXCLUSIVE',list(map(len,exclusive)))
  for B in exclusive:
   inside=[e for e in a['edges']if e[0]in B and e[1]in B];crossing=[(i,j)for i in B for j in range(len(X))if j not in B]
   mx=max((scores[i,j]+abs(D[i,j])@eps,i,j)for i,j in crossing)if crossing else(None,None,None)
   print('edges',len(inside),'first',inside[:5], 'maxoutside',mx)
  if np.all(eps==.0125):Path('CUT125_NOMINATION.json').write_text(json.dumps({'cube_radius':'1/80','blocks':exclusive,'edges':[next(e for e in a['edges']if e[0]in B and e[1]in B)for B in exclusive]},sort_keys=True)+'\n')
if __name__=='__main__':scan()
```
