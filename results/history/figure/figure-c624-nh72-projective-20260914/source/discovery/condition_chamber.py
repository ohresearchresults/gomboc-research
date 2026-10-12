"""Numerically seek a positive reserve inside a specified S/U chamber."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import json,numpy as np
from pathlib import Path
from scipy.optimize import minimize
from forest_search import Forest

def main():
 import argparse
 pa=argparse.ArgumentParser();pa.add_argument('report');pa.add_argument('seed');pa.add_argument('out');args=pa.parse_args();m=Forest(args.report);r=json.loads(Path(args.seed).read_text());z=np.array(r['z']);roots=[set(r['U']),set(r['S'])];cache=[None,None]
 def compute(z):
  if cache[0] is not None and np.array_equal(cache[0],z):return cache[1]
  data,info=m.data(z);vv=[];jj=[]
  for (v,dv,_),(src,dst),n,rr in zip(data,m.edges,m.n,roots):
   for i in range(n):
    ids=np.flatnonzero(src==i);k=ids[np.argmax(v[ids])];s=-1 if i in rr else 1;vv.append(s*v[k]);jj.append(s*dv[k])
  out=(np.array(vv),np.array(jj));cache[0]=z.copy();cache[1]=out;return out
 vv,jj=compute(z);x0=np.r_[z,min(vv.min(),0.)];trust=np.array([5,5,5,.3,.3,.5,.5,.5]);bounds=list(zip(z-trust,z+trust))+[(0,0.1)]
 def con(x):return compute(x[:8])[0]-x[8]
 def jac(x):return np.c_[compute(x[:8])[1],-np.ones(314)]
 res=minimize(lambda x:-x[8],x0,jac=lambda x:np.r_[np.zeros(8),-1.],method='SLSQP',bounds=bounds,constraints=[dict(type='ineq',fun=con,jac=jac)],options={'maxiter':600,'ftol':1e-12})
 z=res.x[:8];v,j,info=m.evaluate(z);psi=compute(z)[0];info.update(chamber_roots=[sorted(x) for x in roots],reserve=float(psi.min()),slsqp_success=bool(res.success),message=res.message)
 Path(args.out).write_text(json.dumps(info,sort_keys=True));print('CHAMBER_CONDITIONED_NUMERIC_ONLY',info['U'],info['S'],info['reserve'],info['condition'],info['min_den'],res.message,flush=True)
if __name__=='__main__':main()
