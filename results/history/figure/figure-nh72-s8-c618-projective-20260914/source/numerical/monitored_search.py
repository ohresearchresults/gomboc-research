"""Keep every mechanically interesting actual evaluated body, not only solver endpoints."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse,json,sys,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from centroid_metric import CentroidOrbit
from isotropic_metric import IsotropicOrbit
class Found(Exception):pass

def main():
 p=argparse.ArgumentParser();p.add_argument('report');p.add_argument('out');p.add_argument('--starts',type=int,default=500);p.add_argument('--evals',type=int,default=400);p.add_argument('--seed',type=int,default=720620);p.add_argument('--chart',choices=['raw','isotropic'],default='raw');p.add_argument('--sigma',type=float,default=.03);p.add_argument('--loss',choices=['linear','cauchy','soft_l1'],default='soft_l1');p.add_argument('--range',type=float,default=30.);p.add_argument('--condition',type=float,default=100.);a=p.parse_args();out=Path(a.out);out.mkdir(exist_ok=False)
 model=(IsotropicOrbit if a.chart=='isotropic' else CentroidOrbit)(a.report);base=model.all_data;best={};pools={};st=0;observed=0
 def watch(z):
  nonlocal observed
  v,J,info,data=base(z);observed+=1
  count=(len(info['S']),len(info['U']));loss=float(np.minimum(v-1e-6,0)@np.minimum(v-1e-6,0))
  if info['min_den']>1e-5 and info['condition']<a.condition and sum(count)<=6:
   key=str(count);score=loss
   if key not in best or score<best[key][0]:
    result=dict(info,start=st,score=score,evaluation=observed);best[key]=(score,np.array(z).copy());pools[key]=result
    name=f'S{count[0]}U{count[1]}'
    (out/(name+'.json')).write_text(json.dumps(result,sort_keys=True))
    with (out/'IMPROVEMENTS.jsonl').open('a') as f:f.write(json.dumps(result,sort_keys=True)+'\n')
    print('EVALUATED_BEST',observed,count,score,info['min_nonroot'],info['min_den'],info['condition'],flush=True)
   if count==(1,1) and info['min_nonroot']>1e-8:
    (out/'NUMERICAL_WINNER.json').write_text(json.dumps(info,sort_keys=True));raise Found
  return v,J,info,data
 model.all_data=watch
 z0=np.r_[model.b0,np.zeros(5)]
 if a.chart=='isotropic':
  _,g,K,_,_=model.state(np.zeros(3));L=np.linalg.cholesky((K-np.outer(g,g))/5);Q,R=np.linalg.qr(L);R=np.diag(np.sign(np.diag(R)))@R;R/=np.linalg.det(L)**(1/3)
  z0[3:]=[np.log(R[0,0]),np.log(R[1,1]),R[0,1]/R[0,0],R[0,2]/R[0,0],R[1,2]/R[1,1]]
 low=np.r_[np.full(3,-a.range),[-1.5,-1.5,-3,-3,-3]];high=-low;rng=np.random.default_rng(a.seed);failures=0;clock=time.monotonic()
 watch(z0)
 for st in range(a.starts):
  keys=list(best)
  if st==0:z=z0.copy()
  elif st%3==0 and keys:
   key=keys[int(rng.integers(len(keys)))];z=best[key][1]+rng.normal(size=8)*10**rng.uniform(-5,-.3)
  elif st%3==1:z=z0+rng.normal(size=8)*10**rng.uniform(-5,0)
  else:z=np.r_[rng.normal(size=3)*10**rng.uniform(-1.5,1.5),rng.normal(size=5)]
  z=np.clip(z,low+1e-6,high-1e-6)
  try:
   least_squares(model.residual,z,jac=model.jacobian,bounds=(low,high),max_nfev=a.evals,loss=a.loss,f_scale=a.sigma,gtol=1e-11,ftol=1e-10,xtol=1e-11)
  except Found:
   print('NUMERICAL_ONLY_WINNER_REQUIRES_RATIONAL_AND_FULL_AUDIT',flush=True);break
  except (ArithmeticError,np.linalg.LinAlgError,ValueError) as ex:
   failures+=1;model.last_t=np.zeros(3);model.last=None
   with (out/'FAILURES.txt').open('a') as f:f.write(str(st)+' '+repr(ex)+'\n')
  if st%25==0:print('START',st,'time',time.monotonic()-clock,'evaluations',observed,flush=True)
 (out/'CONFIG.json').write_text(json.dumps(vars(a),sort_keys=True))
 (out/'SUMMARY.json').write_text(json.dumps(dict(starts=st+1,observed=observed,failures=failures,seconds=time.monotonic()-clock),sort_keys=True))
 print('MONITORED_CENTROID_METRIC_FINISHED',st+1,observed,failures,flush=True)
if __name__=='__main__':main()
