# material-b3fdaa066fb7

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# C114 own-centroid projective-affine numerical search — Recovery capsule part 2/4

Requires complete search.py from part 1, material [internal-source-reference]. Extract the following block verbatim with final LF as basin_search.py. It computes radial merge bars on the complete fixed edge graphs in the primal and centered polar; its own numerical objective is not a proof of existence or nonexistence. Dependencies and input geometry are exactly those of part 1.

Commands: python basin_search.py (baseline diagnostics); python basin_search.py 2 20260920 1 (two joint-objective starts). Terminal marker for search: PROJECTIVE_C114_FULL_BAR_NUMERICAL_SEARCH_COMPLETE. Recorded endpoints will be in part 4. SciPy local face ordering is not the immutable parent's face ordering.

basin_search.py: 3726 bytes, SHA-256 1c5195a120be35da6afec777621e9f471ce1ac1dcb1da617aeda3b183c4e9335.

```python
"""Complete fixed-lattice radial merge-bar objective on the same own-centered orbit.
Numerical exploration only. Imports the complete search.py in this capsule.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'): os.environ[k]='1'
import sys,json
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
import search as s
edge_faces={}
for f,t in enumerate(s.TRI):
 for i in range(3): edge_faces.setdefault(tuple(sorted([int(t[i]),int(t[(i+1)%3])])),[]).append(f)
assert len(edge_faces)==57 and all(len(v)==2 for v in edge_faces.values())
EP=np.array(sorted(edge_faces)); EQ=np.array([edge_faces[e] for e in sorted(edge_faces)])

def bars(X,E,cutoff=1e-13):
 r=np.einsum('ij,ij->i',X,X); a=X[E[:,0]]; d=X[E[:,1]]-a
 t=np.clip(-np.einsum('ij,ij->i',a,d)/np.einsum('ij,ij->i',d,d),0,1)
 foot=a+t[:,None]*d; levels=np.einsum('ij,ij->i',foot,foot)
 p=np.arange(len(X)); peak=np.arange(len(X))
 def root(i):
  while p[i]!=i:
   p[i]=p[p[i]]; i=p[i]
  return int(i)
 records=[]
 for k in np.argsort(-levels,kind='stable'):
  i,j=map(root,E[k]);
  if i==j: continue
  if (r[peak[i]],-peak[i])<(r[peak[j]],-peak[j]): i,j=j,i
  birth=float(r[peak[j]]); death=float(levels[k]); gap=max(0.,birth-death)
  rec={'peak':int(peak[j]),'older_peak':int(peak[i]),'edge':E[k].tolist(),'birth':birth,'death':death,'global_relative':gap/float(r.max()),'birth_relative':gap/birth}
  if gap>cutoff*float(r.max()): records.append(rec)
  p[j]=i
 return sorted(records,key=lambda x:-x['birth_relative'])

def diagnostics(z):
 geo=s.geometry(z)
 if geo is None:return None
 P,Q,g,A,den,cond=geo
 bp=bars(P,EP); bq=bars(Q,EQ)
 ep,rp,up,_=s.escape(P); eq,rq,uq,_=s.escape(Q)
 return {'z':z.tolist(),'S_float':uq,'U_float':up,'Pbars':bp,'Qbars':bq,'minimum_escape_P':float(ep.min()),'minimum_escape_Q':float(eq.min()),'denominator_min':den,'condition_A':cond,'r_over_R':1/(float(np.linalg.norm(P,axis=1).max())*float(np.linalg.norm(Q,axis=1).max()))}

MODE='joint'; WP=1.; REG=1e-8

def objective(z):
 geo=s.geometry(z)
 if geo is None: return 100.+float(np.square(np.minimum(1+s.X0@z[:3]-1e-5,0)).sum())
 P,Q,g,A,den,cond=geo
 bp=bars(P,EP,0); bq=bars(Q,EQ,0)
 lp=sum(x['birth_relative']**2 for x in bp); lq=sum(x['birth_relative']**2 for x in bq)
 # Tiny positive-escape targets discourage primitive-zero optima. No exact claim.
 ep=s.escape(P)[0]; eq=s.escape(Q)[0]
 guard=np.square(np.maximum(1e-5-ep,0)).sum()+np.square(np.maximum(1e-5-eq,0)).sum()
 return WP*lp+lq+.001*guard+REG*float(z@z)

def run(n,seed,wp):
 global WP
 WP=wp; rng=np.random.default_rng(seed); best=None; records=[]
 for k in range(n):
  z=np.zeros(8) if k==0 else rng.normal(0,.35,8)
  while (1+s.X0@z[:3]).min()<.3:z[:3]*=.7
  opt=minimize(objective,z,method='L-BFGS-B',bounds=[(-5,5)]*3+[(-2,2)]*2+[(-4,4)]*3,options={'maxiter':450,'maxls':40,'ftol':1e-13,'gtol':1e-9})
  r=diagnostics(opt.x);r.update(k=k,loss=float(opt.fun),nit=int(opt.nit),nfev=int(opt.nfev),success=bool(opt.success))
  records.append(r)
  if best is None or r['loss']<best['loss']:best=r
  Path(f'basin_{seed}_{wp}.json').write_text(json.dumps({'seed':seed,'physical_weight':wp,'records':records,'best':best},indent=2)+'\n')
  print(json.dumps({k:v for k,v in r.items() if k not in ('Pbars','Qbars')}), 'bars',[x['birth_relative'] for x in r['Pbars']],[x['birth_relative'] for x in r['Qbars']],flush=True)
  if r['S_float']==r['U_float']==1 and min(r['minimum_escape_P'],r['minimum_escape_Q'])>1e-7:break
 print('PROJECTIVE_C114_FULL_BAR_NUMERICAL_SEARCH_COMPLETE',seed,wp,flush=True)
if __name__=='__main__':
 if len(sys.argv)==1:print(json.dumps(diagnostics(np.zeros(8)),indent=2))
 else:run(int(sys.argv[1]),int(sys.argv[2]),float(sys.argv[3]))
```
