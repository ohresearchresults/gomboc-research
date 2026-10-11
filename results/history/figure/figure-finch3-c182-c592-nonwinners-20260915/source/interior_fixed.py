"""Interior geometry / actual own-mass descent in the complete C598 contact chart.
All equilibrium witnesses may change: not a protected no-birth search.
"""
import json,time,argparse,os
from pathlib import Path
import numpy as np
from scipy.linalg import cho_factor,cho_solve,cholesky,solve_triangular,lstsq
from model import Model,HERE

def run(tag,steps=100,start=None,mu=1e-8,lam=.001):
 M=Model();z=M.z0.copy() if start is None else np.load(start)[:M.D];R=M.evaluate(z);assert min(R['s'])>0 and min(R['det'])>0; sf=.1*R['s'];tf=.1*R['det'];trace=[]
 def res(R):
  ui,fi=M.choices(R);U=ui[np.arange(len(ui))!=M.root];F=fi[np.arange(len(fi))!=M.stable];root=M.u_indices[M.root];st=M.f_indices[M.stable]
  v=np.r_[R['u'][U]-1e-6,R['f'][F]-1e-6,-R['u'][root]-1e-5,-R['f'][st]-1e-5];J=np.vstack((R['du'][U],R['df'][F],-R['du'][root],-R['df'][st]));ix=v<0;return v[ix],J[ix]
 def cost(R):
  if min(R['s']-sf)<=0 or min(R['det']-tf)<=0 or not .1<R['volume']<2:return np.inf
  v,_=res(R);return .5*v@v-mu*(np.log(R['s']-sf).sum()+np.log(R['det']-tf).sum())
 for it in range(steps):
  t=time.time();v,J=res(R);D=R['dP'].reshape(-1,M.D);DQ=R['dq'].reshape(-1,M.D);W=D.T@D+.02*DQ.T@DQ+1e-5*np.eye(M.D);T=solve_triangular(cholesky(W,lower=True).T,np.eye(M.D),lower=False)
  B=np.vstack((R['ds']/(R['s']-sf)[:,None],R['ddet']/(R['det']-tf)[:,None]));JT=J@T;BT=B@T
  H=JT.T@JT+mu*BT.T@BT+lam*np.eye(M.D);b=-JT.T@v+mu*BT.sum(axis=0)
  try:u=cho_solve(cho_factor((H+H.T)*.5),b)
  except np.linalg.LinAlgError:
   A=np.vstack((JT,np.sqrt(mu)*BT,np.sqrt(lam)*np.eye(M.D)));u=lstsq(A,np.r_[-v,np.full(len(BT),np.sqrt(mu)),np.zeros(M.D)],lapack_driver='gelsy')[0]
  dz=T@u;a=min(1.,.5/max(np.linalg.norm(u),1e-12));c=cost(R);ok=False
  for ls in range(30):
   try:
    Q=M.evaluate(z+a*dz);cc=cost(Q)
    if cc<c-1e-15 and np.isfinite(cc):ok=True;break
   except (np.linalg.LinAlgError,ValueError,FloatingPointError):pass
   a*=.5
  row={'iteration':it,'accepted':ok,'alpha':a,'lambda':lam,'mu':mu,'cost':float(c),'seconds':time.time()-t}
  if ok:z+=a*dz;R=Q;row['after']=M.summary(R);row['after_cost']=float(cc);lam=max(1e-7,lam*(.8 if a>.25 else 1.3))
  else:lam*=10
  trace.append(row);np.save(HERE/(tag+'.npy'),z);(HERE/(tag+'.trace.json')).write_text(json.dumps(trace,sort_keys=True,separators=(',',':')))
  if it%5==0:print(json.dumps(row),flush=True)
  if lam>1e8:break
 print('FINAL',M.summary(R),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--tag',default='INT2');p.add_argument('--steps',type=int,default=100);p.add_argument('--start');p.add_argument('--mu',type=float,default=1e-8);p.add_argument('--lam',type=float,default=.001);a=p.parse_args();run(a.tag,a.steps,a.start,a.mu,a.lam)
