"""Coupled centroid-gap continuation, LP minimum infinity-norm predictor/corrector.
Original centre is not imposed: centre variables move with all319 shape controls.
"""
import sys,time,json,argparse,os
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.linalg import cholesky,solve_triangular
from model import Model,HERE
from coupled import Phase

def matrix(R,K):
 X=R['dP'].reshape(-1,K);Q=R['dq'].reshape(-1,K);W=X.T@X+.02*Q.T@Q+.00001*np.eye(K);W[-3:,-3:]+=np.eye(3)
 return solve_triangular(cholesky(W,lower=True).T,np.eye(K),lower=False)

def correct(M,phase,z,target,maxit=20,trust=.04):
 z=z.copy();R=M.evaluate(z);K=len(z);record=[]
 for it in range(maxit):
  c,J=phase.constraints(R,True);v=R['gap']-target
  if c.min()>-2e-10 and np.linalg.norm(v)<2e-10:
   return True,z,record
  T=matrix(R,K);A=J@T;B=R['dgap']@T;scale=np.maximum(np.linalg.norm(A,axis=1),1e-5)
  # Full all-nonincidence protection, retain only potentially active rows at trust bound.
  use=c < .025
  A=A[use]/scale[use,None];cc=c[use]/scale[use]
  AA=np.vstack((np.c_[-A,np.zeros(len(A))],np.c_[np.eye(K),-np.ones(K)],np.c_[-np.eye(K),-np.ones(K)]))
  bb=np.r_[cc-1e-9,np.zeros(2*K)]
  r=linprog(np.r_[np.zeros(K),1.],A_ub=AA,b_ub=bb,A_eq=np.c_[B,np.zeros(3)],b_eq=-v,bounds=[(None,None)]*K+[(0,trust)],method='highs-ipm',options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9,'time_limit':12})
  if not r.success:
   record.append({'it':it,'lp_status':int(r.status),'message':r.message,'gap_error':float(np.linalg.norm(v)),'guard_min':float(c.min())});return False,z,record
  dz=T@r.x[:-1];alpha=1.;accepted=False
  oldmer=np.linalg.norm(v)+20*np.linalg.norm(np.minimum(c/scale,0))
  for ls in range(16):
   try:
    Q=M.evaluate(z+alpha*dz);qq,jj=phase.constraints(Q,True);newmer=np.linalg.norm(Q['gap']-target)+20*np.linalg.norm(np.minimum(qq/scale,0))
    if np.isfinite(newmer) and newmer<oldmer*(1-1e-4*alpha):accepted=True;break
   except (np.linalg.LinAlgError,ValueError,FloatingPointError):pass
   alpha*=.5
  print('CORRECT',it,'rho',r.x[-1],'alpha',alpha,'gaperr',np.linalg.norm(v),'minguard',c.min(),flush=True)
  record.append({'it':it,'accepted':accepted,'rho':float(r.x[-1]),'alpha':alpha,'gap_error':float(np.linalg.norm(v)),'guard_min':float(c.min())})
  if not accepted:return False,z,record
  z+=alpha*dz;R=Q
 return False,z,record

def run(tag,steps,start,frac,maxit):
 M=Model();z=np.r_[M.z0,M.m] if start is None else np.load(start);phase=Phase(M,np.r_[M.z0,M.m]);trace=[]
 R=M.evaluate(z);gap0=R['gap'];print('START',M.summary(R),'gap',gap0.tolist(),flush=True)
 for it in range(steps):
  goal=R['gap']*(1-frac);t=time.time();ok,w,rec=correct(M,phase,z,goal,maxit=maxit)
  row={'iteration':it,'fraction':frac,'accepted':ok,'seconds':time.time()-t,'corrector':rec}
  if ok:z=w;R=M.evaluate(z);row['gap']=R['gap'].tolist();row['reference']=M.summary(R);row['own']=M.summary(M.evaluate(z[:M.D]));np.save(HERE/(tag+'.npy'),z);frac=min(.3,frac*1.25)
  else:frac*=.4
  trace.append(row);print(json.dumps(row),flush=True);(HERE/(tag+'.trace.json')).write_text(json.dumps(trace,sort_keys=True,separators=(',',':')))
  if np.linalg.norm(R['gap'])<1e-8 or frac<1e-5:break
 np.save(HERE/(tag+'.npy'),z);print('END',np.linalg.norm(R['gap']),M.summary(M.evaluate(z[:M.D])),flush=True)
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--tag',default='CLOSE1');a.add_argument('--steps',type=int,default=10);a.add_argument('--fraction',type=float,default=.1);a.add_argument('--maxit',type=int,default=16);a.add_argument('--start');v=a.parse_args();run(v.tag,v.steps,v.start,v.fraction,v.maxit)
