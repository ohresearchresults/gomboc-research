"""Full-chart actual-mass semismooth least-squares proposals; no no-birth assertion.
Sufficient max-over-all-true-neighbour/side escape residuals, actual filled centroid.
"""
import time,json,argparse,os
from pathlib import Path
import numpy as np
from scipy.linalg import cho_factor,cho_solve
from model import Model,HERE

def run(tag,steps=120,start=None,lam=.001):
 M=Model();z=M.z0.copy() if start is None else np.load(start)[:M.D];base=M.evaluate(M.z0);sf=np.maximum(1e-12,.01*base['s']);tf=np.maximum(1e-14,.01*base['det']);trace=[];R=M.evaluate(z)
 best=(100000,100000);bestz=z.copy()
 def residual(R):
  ui,fi=M.choices(R);U=ui[np.arange(len(ui))!=M.root];F=fi[np.arange(len(fi))!=M.stable];root=M.u_indices[M.root];st=M.f_indices[M.stable]
  cv=np.r_[R['u'][U]-1e-6,R['f'][F]-1e-6,-R['u'][root]-1e-5,-R['f'][st]-1e-5];cj=np.vstack((R['du'][U],R['df'][F],-R['du'][root],-R['df'][st]))
  cg=R['s']-sf;ct=R['det']-tf
  i=cv<0;j=cg<0;k=ct<0
  return np.r_[cv[i],100*cg[j],100*ct[k]],np.vstack((cj[i],100*R['ds'][j],100*R['ddet'][k]))
 for it in range(steps):
  t=time.time();v,J=residual(R);D=R['dP'].reshape(-1,M.D);DQ=R['dq'].reshape(-1,M.D);W=D.T@D+.02*DQ.T@DQ+1e-5*np.eye(M.D)
  H=J.T@J+lam*W;dz=cho_solve(cho_factor(H),-J.T@v);a=1.;cost=v@v;ok=False
  for ls in range(18):
   try:
    Q=M.evaluate(z+a*dz);vv,_=residual(Q);cost2=vv@vv
    if np.isfinite(cost2) and cost2<cost*(1-1e-4*a) and Q['volume']>.3 and Q['volume']<1.:ok=True;break
   except (np.linalg.LinAlgError,ValueError,FloatingPointError):pass
   a*=.5
  row={'iteration':it,'accepted':ok,'alpha':a,'lambda':lam,'cost':float(cost),'seconds':time.time()-t}
  if ok:z+=a*dz;R=Q;row['after']=M.summary(R);row['after_cost']=float(cost2);lam=max(1e-6,lam*(.75 if a>.5 else 1.3))
  else:lam*=10
  trace.append(row)
  S=M.summary(R);score=(len(S['S'])+len(S['U']),float(cost2 if ok else cost))
  if S['min_slack']>0 and S['min_det']>0 and score<best:best=score;bestz=z.copy();np.save(HERE/(tag+'_best.npy'),z)
  if it%5==0:print(json.dumps(row),flush=True)
  np.save(HERE/(tag+'.npy'),z);(HERE/(tag+'.trace.json')).write_text(json.dumps(trace,sort_keys=True,separators=(',',':')))
  if lam>1e5 or (cost<1e-15 and S['min_slack']>0):break
 print('FINAL',M.summary(R),'BEST',best,M.summary(M.evaluate(bestz)),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--tag',default='OWN1');p.add_argument('--steps',type=int,default=120);p.add_argument('--start');p.add_argument('--lam',type=float,default=.001);a=p.parse_args();run(a.tag,a.steps,a.start,a.lam)
