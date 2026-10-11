"""Optimize the phase of a smooth, centroid-balanced shifted-disk seed.

For r(z)=sqrt(1-z^2), mu(z)=beta*(cos P(z),sin P(z)), P odd,
the horizontal mass equation is integral_0^1 (1-z^2) cos P(z) dz=0.
Concavity of every horizontal slice support follows from
beta^2*(P''^2+P'^4)*(1-z^2)^3 <=1. These are NUMERIC seed-design
constraints sampled densely, not a certificate for a polyhedral Figure.
The exact smooth radial identity does not depend on the chosen odd phase.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from numpy.polynomial.legendre import leggauss

def run(out,modes):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);z=np.linspace(0,1,2401)[:-1];powr=2*np.arange(modes)+1;F=z[:,None]**powr;D=powr[None,:]*z[:,None]**(powr-1);DD=np.zeros_like(F)
 for k in range(1,modes):DD[:,k]=powr[k]*(powr[k]-1)*z**(powr[k]-2)
 zz,ww=leggauss(320);zz=(zz+1)/2;ww=ww/2*(1-zz*zz);M=zz[:,None]**powr;weight=(1-z*z)**3;records=[];start=time.time()
 def equality(x):return float(ww@np.cos(M@x[:-1]))
 def eqjac(x):return np.r_[-(ww*np.sin(M@x[:-1]))@M,0.]
 def convex(x):
  a=x[:-1];beta=x[-1];p=D@a;q=DD@a;return 1-beta*beta*(q*q+p**4)*weight
 def convexjac(x):
  a=x[:-1];beta=x[-1];p=D@a;q=DD@a;return np.column_stack((-beta*beta*weight[:,None]*(2*q[:,None]*DD+4*(p**3)[:,None]*D),-2*beta*(q*q+p**4)*weight))
 a=np.zeros(modes);a[:2]=[1.5*np.pi,-.5*np.pi];x=np.r_[a,.04]
 def cb(x):
  row=dict(beta=float(x[-1]),mass_residual=equality(x),min_sampled_convexity=float(min(convex(x))),coefficients=x[:-1].tolist(),seconds=time.time()-start);records.append(row);np.save(out/'latest.npy',x);(out/'history.json').write_text(json.dumps(records,indent=2))
 r=minimize(lambda x:(-x[-1],np.r_[np.zeros(modes),-1.]),x,jac=True,method='SLSQP',constraints=[dict(type='eq',fun=equality,jac=eqjac),dict(type='ineq',fun=convex,jac=convexjac)],bounds=[(-1000,1000)]*modes+[(.001,.8)],callback=cb,options=dict(maxiter=2000,ftol=1e-12,disp=False));cb(r.x);x=r.x;dense=np.linspace(0,1,200001)[:-1];p=sum(x[k]*powr[k]*dense**(powr[k]-1) for k in range(modes));q=sum(x[k]*powr[k]*(powr[k]-1)*dense**(powr[k]-2) for k in range(1,modes));cv=1-x[-1]**2*(q*q+p**4)*(1-dense*dense)**3;report=dict(success=bool(r.success),message=r.message,beta=float(x[-1]),coefficients=x[:-1].tolist(),mass_residual=equality(x),minimum_dense_convexity=float(min(cv)),iterations=r.nit,scope='numerical smooth-seed optimization only; no polyhedron and no exact proof');(out/'result.json').write_text(json.dumps(report,indent=2));print('SHIFTED_DISK_PHASE',out,report,flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('out');p.add_argument('--modes',type=int,default=9);a=p.parse_args();run(a.out,a.modes)
