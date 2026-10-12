# material-8a94e6540b44

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Complete exploratory locator and fixed-height-cone methods

These numerical methods produced the octagon preserved exactly in [internal-source-reference]. They are NOT the proof of its no-lift statement. CPython3.13.5, NumPy2.3.5, SciPy1.17.0 were used. The files below are complete, with all seeds, parameters and generated-input dependencies. Work in a fresh writable directory containing both source files. Run:
OPENBLAS_NUM_THREADS=1 python polygon_search.py
OPENBLAS_NUM_THREADS=1 python lift_search.py 8
The locator writes polygon_7.npz through polygon_10.npz; the lift tool rounds the chosen planar coordinates to denominator10000 before testing. The exact accepted octagon is separately stored literally, so no floating reproducibility assumption is needed for its reconstruction.

Observed discovery: positive margins at8,9,10; at7 this finite local search returned a degenerate near-zero margin, which is NOT a seven-corner exclusion. At8 the lift tool enumerated all132 polygon triangulations and8646 unordered distinct top/bottom pairs, all numerically infeasible. Swapping top and bottom negates heights and preserves projected centroid. Equal top/bottom triangulations force an affine zero-volume lifting. These numeric statuses are NOT exact infeasibility certificates; the accepted all-height theorem instead uses the root-star separator in the exact capsule.

The height LP subtracts lower moments from upper moments. It gauges the first three noncollinear corner heights to0, fixes volume1 and projected first moments0, and enforces each upper/lower supporting-plane inequality. Zero slacks allow merged true faces. The method can search any fixed convex rational polygon, but its success and topology must subsequently be certified exactly. The full facet lattice must not count the integration diagonals as physical edges.

Source pins:
polygon_search.py:1676 bytes; SHA256 f82a8022cb56bf324e1e6586a23f7b0212aa68ec339813c1002a74368410142a
lift_search.py:1902 bytes; SHA256 39b8c344adf6ac94ad5e2c85d62866dc1427ebd53656794c4a39042a49989a68
No floating output hash is promoted as a proof; the separately preserved exact report has pinned bytes and a standard-library verifier.

## polygon_search.py
```python
import numpy as np
from scipy.optimize import minimize
from math import pi,cos,sin

def cross(a,b): return a[...,0]*b[...,1]-a[...,1]*b[...,0]
def cons(v,k,m):
 q=np.vstack(([1.,0.],v[:-1].reshape(-1,2)))
 e=np.roll(q,-1,axis=0)-q
 t=v[-1]
 inclusion=cross(e[:,None,:],-q[None,:,:]/3-q[:,None,:]).ravel()
 # all distinct vertices left of every edge; incident edges give equality
 cv=cross(e[:,None,:],q[None,:,:]-q[:,None,:])
 mask=np.ones((k,k),bool)
 for i in range(k): mask[i,i]=mask[i,(i+1)%k]=False
 ar=[]
 for i in range(1,k):
  parent=i-1 if i<=m else (i+1)%k
  ar.append(np.dot(q[i],q[parent]-q[i]))
 return np.r_[inclusion,cv[mask],ar]-t

def search(k,m,seed):
 rng=np.random.default_rng(seed)
 n=k-1-m
 aa=rng.uniform(.85,1.10)*pi/min(6,m+1)
 bb=rng.uniform(.85,1.10)*pi/min(6,n+1)
 aa=min(aa,pi/m*.999);bb=min(bb,pi/n*.999)
 q=[[1,0]]
 for i in range(1,m+1): q.append([cos(aa)**i*cos(aa*i),cos(aa)**i*sin(aa*i)])
 for j in range(n,0,-1): q.append([cos(bb)**j*cos(bb*j),-cos(bb)**j*sin(bb*j)])
 x=np.r_[np.array(q)[1:].ravel(),-.02]
 fit=minimize(lambda v:-v[-1],x,method='SLSQP',constraints=[{'type':'ineq','fun':lambda v:cons(v,k,m)}],bounds=[(-1,1)]*(2*k-2)+[(-1,.1)],options={'ftol':1e-12,'maxiter':2000})
 return fit
if __name__=='__main__':
 for k in range(7,11):
  best=None
  for m in range((k-1+1)//2,k-1):
   for seed in range(3):
    f=search(k,m,seed)
    if best is None or f.x[-1]>best[0]:
     best=(f.x[-1],m,f)
   print('candidate',k,m,best[0],flush=True)
  print('BEST',k,best[0],best[1],best[2].success,best[2].message,flush=True)
  np.savez('./polygon_'+str(k)+'.npz',q=np.vstack(([1.,0.],best[2].x[:-1].reshape(-1,2))),m=best[1],margin=best[0])
```

## lift_search.py
```python
import numpy as np,itertools,time,json
from scipy.optimize import linprog
from functools import lru_cache
@lru_cache(None)
def triangulations(poly):
 if len(poly)==2: return ((),)
 out=[]
 for j in range(1,len(poly)-1):
  t=(poly[0],poly[j],poly[-1])
  for a in triangulations(poly[:j+1]):
   for b in triangulations(poly[j:]):out.append((t,)+a+b)
 return tuple(out)
def setup(q,tri):
 k=len(q);sup=[];V=np.zeros(k);M=np.zeros((2,k))
 for ids in tri:
  a,b,c=q[list(ids)];area=np.linalg.det(np.array([b-a,c-a]))/2
  assert area>0
  A=np.vstack([q[list(ids)].T,np.ones(3)])
  for j in range(k):
   if j in ids:continue
   row=np.zeros(k);row[list(ids)]=np.linalg.solve(A,np.r_[q[j],1]);row[j]-=1;sup.append(row)
  V[list(ids)]+=area/3
  for i in ids:M[:,i]+=area*(a+b+c+q[i])/12
 return np.array(sup)[:,3:],V[3:],M[:,3:]
if __name__=='__main__':
 import sys
 k=int(sys.argv[1]) if len(sys.argv)>1 else 8
 d=np.load('./polygon_'+str(k)+'.npz')
 qi=np.rint(d['q']*10000).astype(int);q=qi/10000
 tris=triangulations(tuple(range(k)));print('triangulations',len(tris),flush=True)
 bases=[setup(q,t) for t in tris]
 t0=time.time();nf=0;last=0
 pairs=itertools.combinations(range(len(tris)),2)
 for a,b in pairs:
  Sa,Va,Ma=bases[a];Sb,Vb,Mb=bases[b]
  S=np.vstack([Sa,-Sb]); A=np.vstack([Va-Vb,Ma-Mb]);B=np.array([1.,0.,0.])
  f=linprog(np.zeros(k-3),A_ub=-S,b_ub=np.zeros(len(S)),A_eq=A,b_eq=B,bounds=(None,None),method='highs')
  nf+=1
  if f.success:
   z=np.r_[0,0,0,f.x]
   out={'q_integer':qi.tolist(),'denominator':10000,'z':z.tolist(),'upper':tris[a],'lower':tris[b],'pairs_tested':nf,'triangle_ids':[a,b]}
   print('FEASIBLE',json.dumps(out),flush=True)
   open('./lift_'+str(k)+'.json','w').write(json.dumps(out,indent=2))
   break
  if time.time()-last>10:print('tested',nf,'elapsed',time.time()-t0,flush=True);last=time.time()
 else: print('ALL_INFEASIBLE_NUMERIC',k,nf,time.time()-t0,flush=True)
```
