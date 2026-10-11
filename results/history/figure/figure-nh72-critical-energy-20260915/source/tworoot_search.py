"""Finite compensated critical-disk search allowing one residual primal maximum.
This run seeks nonwinner preparation, not a claimed 110: an exact independent
energy/path certificate is developed separately for this fixed boundary.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import sys,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from atlas_model import Atlas
m=Atlas(Path(os.environ['NH72_BASE_REPORT']));out=Path(sys.argv[1]);out.mkdir(exist_ok=False)
seed=json.loads(Path(os.environ['NH72_LOCAL_MASS_CHECKPOINT']).read_text())['z'];z=np.zeros(18);z[:12]=seed[:12]
clock=time.monotonic();rng=np.random.default_rng(141420);rows=[];bestloss=np.inf;best=z.copy()
changed=[106,109,114,117,120,124,112,146,148,149]

def data(z,ru):
 pv,dv,g,gap,den,vol=m.calc(z,True)
 pi=np.array([np.where(m.src==i)[0][np.argmax(pv[m.src==i].real)] for i in range(m.mesh.n) if i not in (m.rU,ru)])
 di=np.array([np.where(m.fs==i)[0][np.argmax(dv[m.fs==i].real)] for i in range(m.mesh.nf) if i!=m.rS])
 mask=gap.real.copy();mask[m.mesh.inc]=np.inf;j=mask.argmin(axis=1)
 def neg(v):
  w=v.copy();w[v.real>=0]=0;return w
 return np.r_[neg(pv[pi]-1e-8),neg(dv[di]-1e-8),1e6*(g-m.c),1e4*neg(gap[np.arange(m.mesh.nf),j]-2e-8),100*neg(den-.1),100*neg(1+z[12:18]-.1)]
for start in range(30):
 zz=best.copy() if start%3 else z.copy()
 if start:zz+=rng.normal(size=18)*10**rng.uniform(-5,-.7)
 zz=np.clip(zz,np.r_[np.full(12,-10),np.full(6,-.85)]+1e-9,np.r_[np.full(12,10),np.full(6,3)]-1e-9)
 P,_=m.points(zz);ru=max((m.ix[i] for i in changed),key=lambda i:np.dot(P[i]-m.c,P[i]-m.c))
 def jac(z):
  J=np.empty((len(data(z,ru)),18))
  for i in range(18):
   a=z.astype(complex);a[i]+=1e-26j;J[:,i]=data(a,ru).imag/1e-26
  return J
 sol=least_squares(lambda x:data(x,ru),zz,jac=jac,max_nfev=600,x_scale='jac',bounds=(np.r_[np.full(12,-10),np.full(6,-.85)],np.r_[np.full(12,10),np.full(6,3)]),ftol=1e-12,xtol=1e-12,gtol=1e-12)
 r=m.brief(sol.x);r.update(start=start,nfev=sol.nfev,residualroot=m.keep[ru],loss=float(np.linalg.norm(sol.fun)),com_error=float(np.linalg.norm(np.array(r['centroid'])-m.c)))
 rows.append(r);(out/'ALL.json').write_text(json.dumps(rows,sort_keys=True))
 if r['min_gap']>1e-10 and r['min_den']>0 and r['planarity']<1e-9 and r['loss']<bestloss:
  bestloss=r['loss'];best=sol.x.copy();(out/'BEST.json').write_text(json.dumps(r,sort_keys=True));print('BEST',start,r['counts'],r['loss'],r['com_error'],r['min_gap'],time.monotonic()-clock,flush=True)
 if r['counts']==[1,2,1] and r['min_gap']>1e-9 and r['com_error']<1e-12:print('NUMERICAL_PREPARATION121',flush=True);break
print('TWO_ROOT_PREPARATION_FINISHED',len(rows),flush=True)
