# material-e85c93ac090a

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# C114 own-centroid projective-affine numerical search — Recovery capsule part 3/4

Requires search.py from part 1, [internal-source-reference], and basin_search.py from part 2, [internal-source-reference]. Extract the block with final LF as guarded_search.py. This adds positive physical escape constraints to retain one unstable equilibrium while reducing full polar radial merge bars. It is numerical exploration, not an exact weak-equilibrium check or an exclusion theorem.

Command: python guarded_search.py 2 20260920. Terminal marker: PROJECTIVE_C114_GUARDED_NUMERICAL_SEARCH_COMPLETE. Endpoint replay is in part 4. All parameters are literal below, including margin 1e-7, denominator guard 0.02, fixed physical root, initial seed and optimizer settings.

guarded_search.py: 2103 bytes, SHA-256 90c42fb56cdb73ff14dc2b67ff756e3a334ce9121cbc31af4d7d79915558cd13.

```python
"""U=1 guarded full polar merge-bar search, floating discovery only.
Requires search.py and basin_search.py unchanged. python guarded_search.py N SEED.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
import search as s
import basin_search as b
EPS=1e-7
ROOT=int(np.argmax(np.linalg.norm(s.X0,axis=1)))
OTHERS=np.arange(len(s.X0))!=ROOT

def constraints(z):
 geo=s.geometry(z)
 if geo is None:return np.r_[1+s.X0@z[:3]-.02,np.full(len(s.X0),-10.)]
 P=geo[0]; mx=s.escape(P)[3]
 return np.r_[1+s.X0@z[:3]-.02,mx[OTHERS]-EPS,-mx[ROOT]-EPS]

def objective(z):
 geo=s.geometry(z)
 if geo is None:return 100.+float(np.square(np.minimum(1+s.X0@z[:3]-.02,0)).sum())
 Q=geo[1]
 return sum(r['birth_relative']**2 for r in b.bars(Q,b.EQ,0))+1e-9*float(z@z)

def run(n,seed):
 rng=np.random.default_rng(seed); records=[]
 for k in range(n):
  z=np.zeros(8) if k==0 else rng.normal(0,.12,8)
  for _ in range(100):
   if constraints(z).min()>=0:break
   z*=.7
  opt=minimize(objective,z,method='SLSQP',bounds=[(-4,4)]*3+[(-2,2)]*2+[(-4,4)]*3,constraints={'type':'ineq','fun':constraints},options={'maxiter':300,'ftol':1e-12,'disp':False})
  r=b.diagnostics(opt.x)
  if r is None:r={'z':opt.x.tolist(),'geometry_valid':False}
  r.update(k=k,loss=float(opt.fun),constraint_min=float(constraints(opt.x).min()),nit=int(opt.nit),nfev=int(opt.nfev),success=bool(opt.success),message=str(opt.message))
  records.append(r)
  Path(f'guarded_{seed}.json').write_text(json.dumps({'seed':seed,'n':n,'epsilon':EPS,'physical_root':ROOT,'records':records},indent=2)+'\n')
  print(json.dumps({key:val for key,val in r.items() if key not in ('Pbars','Qbars')}),'Pbars',[q['birth_relative'] for q in r.get('Pbars',[])],'Qbars',[q['birth_relative'] for q in r.get('Qbars',[])],flush=True)
 print('PROJECTIVE_C114_GUARDED_NUMERICAL_SEARCH_COMPLETE',flush=True)
if __name__=='__main__':run(int(sys.argv[1]) if len(sys.argv)>1 else 2,int(sys.argv[2]) if len(sys.argv)>2 else 20260920)
```
