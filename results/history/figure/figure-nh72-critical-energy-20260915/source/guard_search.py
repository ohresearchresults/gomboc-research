"""SLSQP with nonlinear fixed positive witnesses and complete geometric slack checks."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import sys,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from atlas_model import Atlas
from atlas_search import route
m=Atlas(Path(os.environ['NH72_BASE_REPORT']));out=Path(sys.argv[1]);out.mkdir(exist_ok=False)
n=12;z0=np.zeros(n);expand=lambda z:np.r_[z,np.zeros(6)]
v,w,g,gap,den,vol=m.calc(expand(z0),True)
v0=v.copy();v0[(m.src==m.ix[124])&(m.dst==m.ix[146])]=.1
pi=route(m.mesh.n,m.src,m.dst,v0,m.rU);di=route(m.mesh.nf,m.fs,m.fd,w,m.rS)
targetedge=np.where((m.src==m.ix[124])&(m.dst==m.ix[146]))[0][0]
assert targetedge in pi and all(v[i]>0 for i in pi if i!=targetedge)
pi=pi[pi!=targetedge]
floors=np.r_[np.minimum(1e-7,.2*v[pi]),np.minimum(1e-7,.2*w[di])];assert min(floors)>1e-9

def quantities(z):
 v,w,g,gap,den,vol=m.calc(expand(z),True)
 mask=gap.real.copy();mask[m.mesh.inc]=np.inf;j=mask.argmin(axis=1)
 return v[targetedge],np.r_[v[pi],w[di]],gap[np.arange(m.mesh.nf),j]
def objective(z):return -quantities(z)[0]
def constraint(z):
 _,ex,gap=quantities(z);return np.r_[(ex-floors)*1e3,(gap-1e-9)*1e3]
def derivative(fun,z):
 val=np.atleast_1d(fun(z));J=np.empty((len(val),len(z)))
 for k in range(len(z)):
  a=z.astype(complex);a[k]+=1e-26j;J[:,k]=np.atleast_1d(fun(a)).imag/1e-26
 return J if len(val)>1 else J[0]
steps=[];clock=time.monotonic()
def callback(z):
 d=m.brief(expand(z));_,ex,gg=quantities(z);steps.append(dict(z=z.tolist(),value=float(-objective(z)),margin=float(constraint(z).min()),own=d['counts']))
 if len(steps)%10==0:print('ITER',len(steps),steps[-1]['value'],steps[-1]['margin'],flush=True)
 (out/'HISTORY.json').write_text(json.dumps(steps,sort_keys=True))
r=minimize(objective,z0,jac=lambda z:derivative(objective,z),method='SLSQP',bounds=[(-20,20)]*n,constraints=[dict(type='ineq',fun=constraint,jac=lambda z:derivative(constraint,z))],callback=callback,options=dict(maxiter=700,ftol=1e-14,disp=True))
P,_=m.points(expand(r.x));s=m.brief(expand(r.x));s.update(reference=m.mesh.brief(m.mesh.state(P,m.c)),success=bool(r.success),message=str(r.message),margin=float(constraint(r.x).min()),value=float(-r.fun));(out/'FINAL.json').write_text(json.dumps(s,sort_keys=True));print('GUARDED_CRITICAL_PATCH_DONE',s['value'],s['margin'],s['reference']['counts'],time.monotonic()-clock,flush=True)
