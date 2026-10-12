"""Geometry-feasible exterior-interface optimization from the energy/mass endpoint.
Each accepted result is checked at its own mass; finite failure is not exclusion.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import sys,json
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from interface_model import Interface

def main(base,gen,checkpoint,outname):
 m=Interface(base,gen);out=Path(outname);out.mkdir(exist_ok=False);z0=np.array(json.loads(Path(checkpoint).read_text())['z']);n=25
 maskp=np.arange(m.mesh.n)!=m.rU;maskd=np.arange(m.mesh.nf)!=m.rS;logs=[]
 def allval(z):
  p,d,g,gap,den,v=m.calc(z)
  ip=np.array([np.where(m.src==i)[0][np.argmax(p.real[m.src==i])] for i in range(m.mesh.n)])
  jp=np.array([np.where(m.fs==i)[0][np.argmax(d.real[m.fs==i])] for i in range(m.mesh.nf)])
  pp=p[ip][maskp]-1e-7;dd=d[jp][maskd]-1e-7
  pp[pp.real>=0]=0;dd[dd.real>=0]=0
  mask=gap.real.copy();mask[m.mesh.inc]=np.inf;ii=mask.argmin(axis=1);gg=gap[np.arange(m.mesh.nf),ii]-1e-9
  return np.r_[pp,dd],gg
 def fun(z):p,g=allval(z);return p@p
 def grad(z):
  ans=[]
  for k in range(n):zz=z.astype(complex);zz[k]+=1e-25j;ans.append(fun(zz).imag/1e-25)
  return np.array(ans)
 def con(z):return allval(z)[1]
 def cjac(z):
  J=np.empty((m.mesh.nf,n))
  for k in range(n):zz=z.astype(complex);zz[k]+=1e-25j;J[:,k]=con(zz).imag/1e-25
  return J
 def callback(z):
  r=m.brief(z);r['iteration']=len(logs);r['objective']=float(fun(z));logs.append(r)
  if len(logs)%10==0:print('ITER',len(logs),r['counts'],r['min_gap'],r['objective'],flush=True)
  (out/'HISTORY.json').write_text(json.dumps(logs,sort_keys=True))
 sol=minimize(fun,z0,jac=grad,method='SLSQP',bounds=[(-5,5)]*n,constraints=[dict(type='ineq',fun=con,jac=cjac)],callback=callback,options=dict(maxiter=300,ftol=1e-13,disp=False))
 r=m.brief(sol.x);r.update(status=int(sol.status),success=bool(sol.success),message=str(sol.message),objective=float(sol.fun),iterations=int(sol.nit));(out/'FINAL.json').write_text(json.dumps(r,sort_keys=True));print('GUARDED_INTERFACE_FINISHED',r['counts'],r['min_gap'],r['objective'],sol.message,flush=True)
if __name__=='__main__':sys.set_int_max_str_digits(0);main(*sys.argv[1:])
