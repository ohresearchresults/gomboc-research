"""Barrier-protected reference-cell continuation with a moving centre and true mass.
The two defective reference facets are deliberately not protected. No fixed-centre cap.
"""
import json,time,argparse,os
from pathlib import Path
import numpy as np
from scipy.linalg import cholesky,solve_triangular,cho_solve,cho_factor,lstsq
from model import Model,HERE
from coupled import Phase

def run(tag,steps=100,start=None,mu=1e-10,lam=.0001):
 M=Model();entry=np.r_[M.z0,M.m];phase=Phase(M,entry);z=entry.copy() if start is None else np.load(start);R=M.evaluate(z);c,J=phase.constraints(R,True);assert min(c)>0;trace=[];K=len(z)
 def cost(R):
  c,_=phase.constraints(R,True)
  if min(c)<=0:return np.inf
  return .5*R['gap']@R['gap']-mu*np.log(c).sum()
 for it in range(steps):
  t=time.time();c,J=phase.constraints(R,True);D=R['dP'].reshape(-1,K);DQ=R['dq'].reshape(-1,K);W=D.T@D+.02*DQ.T@DQ+1e-5*np.eye(K);W[-3:,-3:]+=np.eye(3);T=solve_triangular(cholesky(W,lower=True).T,np.eye(K),lower=False)
  A=(J/c[:,None])@T;B=R['dgap']@T;H=B.T@B+mu*A.T@A+lam*np.eye(K);b=-B.T@R['gap']+mu*A.sum(axis=0)
  try:u=cho_solve(cho_factor((H+H.T)*.5),b)
  except np.linalg.LinAlgError:u=lstsq(np.vstack((B,np.sqrt(mu)*A,np.sqrt(lam)*np.eye(K))),np.r_[-R['gap'],np.full(len(A),np.sqrt(mu)),np.zeros(K)],lapack_driver='gelsy')[0]
  dz=T@u;a=min(1.,.3/max(np.linalg.norm(u),1e-12));co=cost(R);ok=False
  for ls in range(30):
   try:
    Q=M.evaluate(z+a*dz);cc=cost(Q)
    if np.isfinite(cc) and cc<co-1e-16:ok=True;break
   except (np.linalg.LinAlgError,ValueError,FloatingPointError):pass
   a*=.5
  row={'iteration':it,'accepted':ok,'alpha':a,'lambda':lam,'mu':mu,'cost':float(co),'gap':float(np.linalg.norm(R['gap'])),'guard_min':float(c.min()),'seconds':time.time()-t}
  if ok:z+=a*dz;R=Q;row['after']=M.summary(R);row['after_gap']=float(np.linalg.norm(R['gap']));lam=max(1e-8,lam*(.8 if a>.25 else 1.2))
  else:lam*=10
  trace.append(row);np.save(HERE/(tag+'.npy'),z);(HERE/(tag+'.trace.json')).write_text(json.dumps(trace,sort_keys=True,separators=(',',':')))
  if it%5==0:print(json.dumps(row),flush=True)
  if lam>1e6:break
 print('FINAL','gap',R['gap'].tolist(),'reference',M.summary(R),'own',M.summary(M.evaluate(z[:M.D])),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--tag',default='MI1');p.add_argument('--steps',type=int,default=100);p.add_argument('--start');p.add_argument('--mu',type=float,default=1e-10);p.add_argument('--lam',type=float,default=.0001);a=p.parse_args();run(a.tag,a.steps,a.start,a.mu,a.lam)
