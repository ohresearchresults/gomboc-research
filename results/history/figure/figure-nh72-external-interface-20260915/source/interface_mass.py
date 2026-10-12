"""Change inlet/outlet through actual exterior contacts, close filled moments,
and remove the parent's ten-link necessary energy deficit. Not a 110 certificate."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import sys,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from interface_model import Interface
from interface_search import OLD

def main(base,gen,outname):
 m=Interface(base,gen);out=Path(outname);out.mkdir(exist_ok=False);rng=np.random.default_rng(150917);records=[];clock=time.monotonic()
 z0=np.r_[np.zeros(13),OLD]
 def fun(z):
  _,_,g,gap,den,vol=m.calc(z);mask=gap.real.copy();mask[m.mesh.inc]=np.inf;j=mask.argmin(axis=1);gm=gap[np.arange(m.mesh.nf),j]-1e-7;gm[gm.real>=0]=0
  P,_=m.points(z);u=P[m.ix[111]]-g;v=P[m.ix[150]]-g;delta=10*(v@v-u@u)-(v-u)@(v-u)
  return np.r_[1e5*(g-m.c),1e4*gm,10*(delta-.01),1e3*np.minimum(vol.real,0),1e-5*z]
 def jac(z):
  J=np.empty((len(fun(z)),25))
  for k in range(25):
   zz=z.astype(complex);zz[k]+=1e-25j;J[:,k]=fun(zz).imag/1e-25
  return J
 for it in range(4):
  z=z0.copy() if it==0 else z0+rng.normal(size=25)*.1
  sol=least_squares(fun,z,jac=jac,bounds=(-5,5),max_nfev=400,x_scale='jac',ftol=1e-12,xtol=1e-12,gtol=1e-12)
  z=sol.x;s=m.brief(z);P,_=m.points(z);g=np.array(s['centroid']);u=P[m.ix[111]]-g;v=P[m.ix[150]]-g
  s.update(start=it,nfev=sol.nfev,loss=float(np.linalg.norm(sol.fun)),energy10=float(10*(v@v-u@u)-(v-u)@(v-u)),centroid_error=float(np.max(abs(g-m.c))))
  records.append(s);(out/'ALL.json').write_text(json.dumps(records,sort_keys=True));print('MASS_ENERGY',it,s['counts'],s['min_gap'],s['centroid_error'],s['energy10'],sol.nfev,time.monotonic()-clock,flush=True)
  if s['min_gap']>1e-9 and s['centroid_error']<1e-11 and s['energy10']>0:
   (out/'CLOSED.json').write_text(json.dumps(s,sort_keys=True));break
 (out/'DONE.json').write_text(json.dumps(dict(seed=150917,starts_run=len(records),max_starts=4,max_nfev=400,energy_target=.01)))
 print('FINITE_INTERFACE_MASS_ENERGY_SEARCH_DONE',len(records),flush=True)
if __name__=='__main__':sys.set_int_max_str_digits(0);main(*sys.argv[1:])
