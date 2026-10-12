"""Actual-centroid correction respecting the strict Thales radial domain.

An unconstrained minimum-norm centroid correction can cross rho=1 even when
the predictor respected its linear bounds. Here the correction itself solves
the three physical mass equations together with radial and interior bounds.
No reference-centre census substitutes for the accepted body's own census.
"""
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from primal_log_thales import evaluate,metric
OPT={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10}

def project(c,z,eta,rho_floor=1e-9):
 for iteration in range(18):
  e=evaluate(c,z,eta)
  if np.linalg.norm(e['g'])<1e-14 and np.max(z[2::3])<-rho_floor*.8:return z,e
  W,sx=metric(e);d=len(z);rad=np.arange(2,d,3);R=np.vstack((-e['DI']@W,W[rad],-W[rad]));bR=np.r_[e['inside']*.9,-rho_floor-z[rad],z[rad]+25];I=eye(d);A=vstack([hstack([csr_matrix(R),csr_matrix((len(bR),d))]),hstack([I,-I]),hstack([-I,-I])],format='csr');mass_scale=1e5;AE=hstack([csr_matrix(mass_scale*e['Dg']@W/sx),csr_matrix((3,d))]);bound=.2/np.sqrt(d);sol=linprog(np.r_[np.zeros(d),np.ones(d)],A_ub=A,b_ub=np.r_[bR,np.zeros(2*d)],A_eq=AE,b_eq=-mass_scale*e['g']/sx,bounds=[(-bound,bound)]*d+[(0,None)]*d,method='highs',options=OPT)
  if not sol.success:raise ValueError('radial-constrained actual-centroid projection infeasible: '+sol.message)
  dz=W@sol.x[:d];ok=False;norm=np.linalg.norm(e['g'])
  for j in range(18):
   zz=z+dz*2.**-j
   try:ee=evaluate(c,zz,eta)
   except (ValueError,np.linalg.LinAlgError):continue
   nn=np.linalg.norm(ee['g'])
   if nn<max(1e-14,norm*(1-1e-5)) and np.max(zz[2::3])<-rho_floor*.8:
    z=zz;ok=True;break
  if not ok:raise ValueError('radial-constrained actual-centroid projection stalled')
 raise ValueError('radial-constrained actual-centroid projection incomplete')
