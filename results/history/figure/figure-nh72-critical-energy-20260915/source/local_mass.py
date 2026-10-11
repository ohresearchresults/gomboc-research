"""Try compensation by actual critical-support geometry, with caps held identity."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import sys,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from atlas_model import Atlas
m=Atlas(Path(os.environ['NH72_BASE_REPORT']));out=Path(sys.argv[1]);out.mkdir(exist_ok=False)
clock=time.monotonic();rows=[];rng=np.random.default_rng(141419)
def values(z):
 _,_,g,gap,_,vol=m.calc(np.r_[z,np.zeros(6)])
 gmask=gap.real.copy();gmask[m.mesh.inc]=np.inf;j=gmask.argmin(axis=1)
 geom=gap[np.arange(m.mesh.nf),j]-1e-9
 # Mask must be determined from real parts, preserving complex derivatives.
 ng=geom.copy();ng[geom.real>=0]=0
 return np.r_[1e5*(g-m.c),1e4*ng,1e-5*z]
def jac(z):
 J=np.empty((len(values(z)),len(z)))
 for i in range(len(z)):
  x=z.astype(complex);x[i]+=1e-26j;J[:,i]=values(x).imag/1e-26
 return J
for k in range(12):
 z=np.zeros(12) if k==0 else rng.normal(size=12)*10**rng.uniform(-4,-.1)
 sol=least_squares(values,z,jac=jac,max_nfev=500,ftol=1e-13,xtol=1e-13,gtol=1e-13,bounds=(-10,10),x_scale='jac')
 z=sol.x;s=m.brief(np.r_[z,np.zeros(6)]);s.update(start=k,nfev=sol.nfev,com_error=float(np.linalg.norm(np.array(s['centroid'])-m.c)),loss=float(np.linalg.norm(sol.fun)))
 rows.append(s);(out/'ALL.json').write_text(json.dumps(rows,sort_keys=True));print(k,s['counts'],s['com_error'],s['min_gap'],s['loss'],time.monotonic()-clock,flush=True)
 if s['min_gap']>1e-10 and s['com_error']<1e-12:
  (out/'CLOSED.json').write_text(json.dumps(s,sort_keys=True));break
print('LOCAL_CRITICAL_MASS_SEARCH_FINISHED',len(rows),flush=True)
