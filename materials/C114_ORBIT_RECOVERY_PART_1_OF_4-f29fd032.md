# material-f29fd032681d

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# C114 own-centroid projective-affine numerical search — Recovery capsule part 1/4

Floating-point discovery method and unsuccessful bounded search, NOT an accepted construction or an exclusion theorem. Literal grid input: C114 own211, 21 vertices/57 edges/38 faces, studied in immutable result figure-0438. SciPy face indices are local, not aliases for the exact parent's face ordering.

Extract this block verbatim with a final LF as search.py. Environment: Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0. Command: python search.py 3 20260920. Terminal marker: PROJECTIVE_C114_NUMERICAL_SEARCH_COMPLETE. Numerical optimizer trajectories may vary across platforms; part 4 will supply recorded endpoint replay. Parts 2 and 3 supply two other complete search objectives. All four parts form the recovery capsule.

search.py: 3677 bytes, SHA-256 0cdbb78ed4f389add5a51accbba2f451a2b809071775ef0d7668468a974bfb11.

The eight-parameter map applies x/(1+b.x), recomputes the actual uniform solid centroid g, and applies an invertible determinant-one lower-triangular A to the centered body. Positive denominators preserve incidences. This is fixed-combinatorics exploration, not arbitrary movement of the mass center or nonuniform density. The polar is centered at that physical centroid. S/U diagnostics are floating; no weak-equilibrium certificate is claimed.

```python
"""Own-centroid projective/affine search; floating discovery, not certification.
Python 3.13.5, numpy 2.3.5, scipy 1.17.0. Run: python search.py NSTART SEED.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'): os.environ[k]='1'
import sys,json,hashlib,time
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
from pathlib import Path
RAW={"grid":10000,"points":[[-13513,10001,-9032],[7585,971,-5336],[9215,2535,-2766],[9859,3065,-261],[10414,1455,1511],[10533,-561,2627],[10245,-2747,3309],[9489,-4870,3884],[8292,-6612,4622],[6777,-7643,5870],[4984,-8225,7187],[2841,-8790,8032],[556,-8903,8725],[-1868,-8784,9006],[-4342,-8346,8933],[-6808,-7570,8472],[-9197,-6461,7561],[-11427,-4979,6139],[-13362,-2964,4209],[-14798,-281,1613],[-15515,3415,-2186]]}
CENTROID=np.array([242198547478883/204849101435960000,231436767908883/51212275358990000,386646611479453/204849101435960000])
X0=np.array(RAW['points'],float)/RAW['grid']-CENTROID
H=ConvexHull(X0); TRI=H.simplices.copy()
for i,t in enumerate(TRI):
 if np.linalg.det(X0[t])<0: TRI[i,[1,2]]=TRI[i,[2,1]]
Q0=H.equations[:,:3]/(-H.equations[:,3,None])
R=max(np.linalg.norm(X0,axis=1)); X0/=R; Q0*=R

def mass(Y):
 t=Y[TRI]; d=np.einsum('ij,ij->i',t[:,0],np.cross(t[:,1],t[:,2]))
 return (d[:,None]*t.sum(axis=1)).sum(axis=0)/(4*d.sum())

def geometry(z):
 b=z[:3]; s=1+X0@b
 if s.min()<=1e-5: return None
 Y=X0/s[:,None]; g=mass(Y); A=np.array([[np.exp(z[3]),0,0],[z[5],np.exp(z[4]),0],[z[6],z[7],np.exp(-z[3]-z[4])]])
 P=(Y-g)@A.T; Q=Q0+b; h=1-Q@g
 if h.min()<=0: return None
 Q=(Q/h[:,None])@np.linalg.inv(A)
 return P,Q,g,A,float(s.min()),float(np.linalg.cond(A))

def escape(X):
 D=X[None,:,:]-X[:,None,:]; rr=np.linalg.norm(X,axis=1)
 dd=np.linalg.norm(D,axis=2); np.fill_diagonal(dd,1.)
 e=np.einsum('ik,ijk->ij',X,D)/(rr[:,None]*dd)
 np.fill_diagonal(e,-np.inf)
 mx=e.max(axis=1); root=int(np.argmax(rr)); valid=np.arange(len(X))!=root
 return mx[valid],root,int(np.sum(mx<0)),mx

MARGIN=2e-4

def objective(z):
 geo=geometry(z)
 if geo is None:
  s=1+X0@z[:3]; return 100.+float(np.sum(np.minimum(s-1e-5,0)**2))
 P,Q,g,A,den,cond=geo
 ep=escape(P)[0]; eq=escape(Q)[0]
 penalty=np.square(np.maximum(MARGIN-ep,0)).sum()+np.square(np.maximum(MARGIN-eq,0)).sum()
 # A tiny regularizer prevents unbounded collapse, but does not certify shape.
 penalty+=1e-11*np.sum(z*z)
 return float(penalty)

def run(count,seed):
 rng=np.random.default_rng(seed); records=[]; best=None
 bounds=[(-5,5)]*3+[(-2.5,2.5)]*2+[(-5,5)]*3
 for k in range(count):
  z=np.zeros(8) if k==0 else rng.normal(0,.5,8)
  while (1+X0@z[:3]).min()<.25: z[:3]*=.7
  opt=minimize(objective,z,method='L-BFGS-B',bounds=bounds,options={'maxiter':900,'ftol':1e-14,'gtol':1e-10,'maxls':40})
  geo=geometry(opt.x)
  if geo is None: continue
  P,Q,g,A,den,cond=geo
  ep,rp,up,_=escape(P); eq,rq,uq,_=escape(Q)
  rec={'k':k,'loss':float(opt.fun),'z':opt.x.tolist(),'U':up,'S':uq,'physical_root':rp,'polar_root':rq,'min_p':float(ep.min()),'min_q':float(eq.min()),'denominator_min':den,'condition_A':cond,'nit':int(opt.nit),'nfev':int(opt.nfev),'success':bool(opt.success)}
  records.append(rec)
  if best is None or rec['loss']<best['loss']: best=rec
  Path(f'result_{seed}.json').write_text(json.dumps({'seed':seed,'count_requested':count,'records':records,'best':best},indent=2)+'\n')
  print(json.dumps(rec),flush=True)
  if up==1 and uq==1 and min(ep.min(),eq.min())>1e-7: break
 if best: print('PROJECTIVE_C114_NUMERICAL_SEARCH_COMPLETE',json.dumps(best),flush=True)
if __name__=='__main__': run(int(sys.argv[1]) if len(sys.argv)>1 else 8,int(sys.argv[2]) if len(sys.argv)>2 else 20260920)
```
