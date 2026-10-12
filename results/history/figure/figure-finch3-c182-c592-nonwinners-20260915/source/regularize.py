"""Grow near-zero geometric clearances before own-mass optimization.
This is an explicitly unprotected mechanical phase, not a no-birth continuation.
"""
import numpy as np,json,time,argparse
from scipy.linalg import cho_factor,cho_solve
from model import Model,HERE

def run(tag,steps=30,floor=1e-5):
 M=Model();z=M.z0.copy();R=M.evaluate(z);trace=[];lam=1e-5
 def res(R):
  g=np.r_[R['s']-floor,R['det']-floor*.1];J=np.vstack((R['ds'],R['ddet']));ix=g<0;return g[ix],J[ix]
 for it in range(steps):
  c,J=res(R);D=R['dP'].reshape(-1,M.D);W=D.T@D+.02*R['dq'].reshape(-1,M.D).T@R['dq'].reshape(-1,M.D)+1e-5*np.eye(M.D);dz=cho_solve(cho_factor(J.T@J+lam*W),-J.T@c);a=1.;old=c@c;ok=False
  for ls in range(30):
   Q=M.evaluate(z+a*dz);v,_=res(Q);co=v@v
   if co<old*(1-1e-4*a) and Q['s'].min()>0 and Q['det'].min()>0:ok=True;break
   a*=.5
  if ok:z+=a*dz;R=Q;lam=max(1e-9,lam*.7)
  else:lam*=10
  row={'it':it,'accepted':ok,'alpha':a,'cost':float(old),'slack':float(R['s'].min()),'det':float(R['det'].min()),'class':M.summary(R)};trace.append(row);print(json.dumps(row),flush=True)
  np.save(HERE/(tag+'.npy'),z);(HERE/(tag+'.trace.json')).write_text(json.dumps(trace,sort_keys=True,separators=(',',':')))
  if co<1e-20 or lam>1e3:break
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--tag',default='REG1');p.add_argument('--steps',type=int,default=30);p.add_argument('--floor',type=float,default=1e-5);v=p.parse_args();run(v.tag,v.steps,v.floor)
